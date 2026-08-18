<!-- source: https://ar5iv.labs.arxiv.org/html/1306.2340 | converted from HTML -->

[1306.2340] Perturbations of quadratic Hamiltonian two-saddle cycles.

# Perturbations of quadratic Hamiltonian two-saddle cycles.

Lubomir Gavrilov Affiliation: Institut de Mathématiques de Toulouse, UMR 5219 Affiliation: Université de Toulouse, CNRS Affiliation: UPS IMT, F-31062 Toulouse Cedex 9, France Affiliation: Iliya D. Iliev Affiliation: Institute of Mathematics, Bulgarian Academy of Sciences Affiliation: Bl. 8, 1113 Sofia, Bulgaria

###### Abstract

We prove that the number of limit cycles, which bifurcate from a two-saddle loop of a planar quadratic Hamiltonian system, under an arbitrary quadratic deformation, is less than or equal to three.

## 1 Introduction

The theory of plane polynomial quadratic differential systems

 | { x ˙ = P ⁡ ( x, y) y ˙ = Q ⁡ ( x, y) \left\{\begin{array}[]{lcr}\dot{x}&=&P(x,y)\\ \dot{y}&=&Q(x,y)\end{array}\right. |  | (1) |

is one of the most classical branches of the theory of two-dimensional autonomous systems. Despite of the great theoretical interest in studying of such systems, few is known on their qualitative properties. Let H ⁡ ( 2) H(2) be the maximal number of limit cycles, which such a system can have. It is still not known whether H ⁡ ( 2) < ∞ H(2)<\infty (or H ⁡ ( k) < ∞ H(k)<\infty for a polynomial system of degree k k). A survey on the state of art until 1966 was given by Coppel [7] where some basic and specific properties of the quadratic systems are discussed.

It was believed for a long time that H ⁡ ( 2) = 3 H(2)=3, see e.g. [29], until Shi Song Ling gave in 1980 his famous example of a quadratic system with four limit cycles [33].

In 1986 Roussarie [30] proposed a local approach to the global conjecture H ⁡ ( k) < ∞ H(k)<\infty, based on the observation that if the cyclicity is infinite, then a limiting periodic set will exist with infinite cyclicity. All possible 121 limiting periodic sets of quadratic systems were later classified in [8].

Of course, it is of interest to compute explicitly the cyclicity of concrete limiting period sets, the simplest one being the equilibrium point. It is another classical result, due to Bautin (1939), which claims that the cyclicity of a singular point of a quadratic system is at most three. The cyclicity of Hamiltonian quadratic homoclinic loops is two [19, 21], and for the reversible ones see [18].

In his controversial paper [35], Żoła̧dek proved that the cyclicity of the Melnikov functions near quadratic triangles (three-saddle loops) or segments (two-saddle loops) is respectively three and two. From this he deduced that the cyclicity of the triangle or the segment itself is also equal to three or two, respectively. As we know now, this conclusion is not always true. Namely, in the perturbed Hamiltonian case, not all limit cycles near a polycycle are "shadowed" by a zero of a Melnikov function. The bifurcation of "alien" limit cycles is a new phenomenon discovered recently by Caubergh, Dumortier and Roussarie [3, 10]. Li and Roussarie [25] later computed the cyclicity of quadratic Hamiltonian two-loops, when they are perturbed "in a Hamiltonian direction". In the case of a more general perturbation they only noted that "some new approach may be needed".

One of the most interesting developments in this field, starting from the series of papers by Petrovskii and Landis [29], is the proliferation of complex methods, as it can be seen from the 2002 survey of Ilyashenko [23]. A particular interest is given to the study of different infinitesimal versions of the 16th Hilbert problem. Thus, G.S. Petrov [27] used the argument principle to evaluate the zeros of suitable complete Abelian integrals, which on its turn produces an upper bound for the number of limit cycles, which a perturbed quadratic system of the form

 | { x ˙ = y + ε ​ P ​ ( x, y) y ˙ = x − x 2 + ε ​ Q ​ ( x, y) \left\{\begin{array}[]{lcr}\dot{x}&=&y+\varepsilon P(x,y)\\ \dot{y}&=&x-x^{2}+\varepsilon Q(x,y)\end{array}\right. |  |

may have. The result was later generalized for the perturbations of arbitrary generic cubic Hamiltonians in [20, 12].

The present paper studies the cyclicity of quadratic Hamiltonian monodromic two-loops, as on Fig. 1. We use complex methods, in the spirit of [14, 15], which can also be seen as a far going generalization of the original Petrov method. Our main result is that at most three limit cycles can bifurcate from such a two-loop (Theorem 1), although we did not succeed to prove that this bound is exact. It is interesting to note, that even for a generic quadratic perturbation, two limit cycles can appear near a two-saddle loop, while at the same time the (first) Poincaré-Pontryagin (or Melnikov) function exhibits only one zero. The appearance of the missing alien limit cycle is discussed in the Appendix.

Our semi-local results, combined with the known cyclicity of open period annuli lead also to some global results, formulated in Section 5.

## 2 Statement of the result

Let X λ X_{\lambda}, λ ∈ ℝ 12 \lambda\in{\mathbb{R}}^{12} be the (vector) space of all quadratic planar vector fields, and let X λ 0 X_{\lambda_{0}} be a planar quadratic vector field which has two non-degenerate saddle points S 1 ​ ( λ 0), S 2 ​ ( λ 0) S_{1}(\lambda_{0}),S_{2}(\lambda_{0}) connected by two heteroclinic connections Γ 1, Γ 2 \Gamma_{1},\Gamma_{2}, which form a monodromic two-loop as on Figure 1. The union Γ = Γ 1 ∪ Γ 2 \Gamma=\Gamma_{1}\cup\Gamma_{2} will be referred to as a non-degenerate two-saddle loop. The cyclicity C ​ y ​ c ​ l ​ ( Γ, X λ) Cycl(\Gamma,X_{\lambda}) of the two-saddle loop Γ \Gamma with respect to the deformation X λ X_{\lambda} is the maximal number of limit cycles which X λ X_{\lambda} can have in an arbitrarily small neighborhood of Γ \Gamma, as λ \lambda tends to λ 0 \lambda_{0}, see [31].

Figure 1: Monodromic two-saddle loop and the Dulac maps d ε ± {\rm d}_{\varepsilon}^{\pm}

In the present paper we shall suppose in addition, that X λ 0 X_{\lambda_{0}} is a Hamiltonian vector field

 | X λ 0 = X H: { x ˙ = H y y ˙ = − H x X_{\lambda_{0}}=X_{H}:\left\{\begin{array}[]{lcr}\dot{x}&=&H_{y}\\ \dot{y}&=&-H_{x}\end{array}\right. |  | (2) |

where H H is a bivariate polynomial of degree three. Our main result is the following

###### Theorem 1.

The cyclicity of every non-degenerate Hamiltonian two-saddle loop, under an arbitrary quadratic deformation, is at most equal to three.

The result will be proved by making use of complex methods, as explained in [14], combined with the precise computation of the so called higher order Poincaré-Pontryagin (or Melnikov) functions, which can be found in [22].

### 2.1 Outline of the proof of Theorem 1

#### 2.1.1 Principalization of the Bautin ideal

Let h ↦ P λ ​ ( h) h\mapsto P_{\lambda}(h) be the first return map associated to the deformed vector field X λ X_{\lambda} and the period annulus of X λ 0 X_{\lambda_{0}}, bounded by Γ \Gamma. Consider the Bautin ideal

 | ℬ = ⟨ a k ​ ( λ) ⟩ ⊂ ℂ ⁡ [λ] {\cal B}=\langle a_{k}(\lambda)\rangle\subset{\mathbb{C}}[\lambda] |  |

generated by the coefficients of the expansion

 | P λ ​ ( h) − h = ∑ k = 1 ∞ a k ​ ( λ) ​ h k. P_{\lambda}(h)-h=\sum_{k=1}^{\infty}a_{k}(\lambda)h^{k}. |  |

In the quadratic case under consideration its computation is well known, and goes back to Bautin, see [24] for details. It has three generators, in particular the ideal is not principal. By making use of the Hironaka’s desingularization theorem, we can always assume that ℬ {\cal B} is "locally principal". Namely, by abuse of notation, let ℬ {\cal B} be the ideal sheaf generated by the Bautin ideal, in the sheaf of analytic functions 𝒪 X {\cal O}_{X} on X X. The parameter space X = ℝ 12 X={\mathbb{R}}^{12} can be replaced by a new smooth real analytic variety X ~ \tilde{X}, together with a proper analytic map

 | π: X ~ → X \pi:\tilde{X}\rightarrow X |  |

such that the pull back π ∗ ​ ℬ \pi^{*}{\cal B} is a principal ideal sheaf. This means that for every point λ ~ ∈ X ~ \tilde{\lambda}\in\tilde{X} there is a neighborhood U U, such that the ideal π ∗ ​ ℬ ​ ( U) \pi^{*}{\cal B}(U) of the ring 𝒪 X ~ ​ ( U) {\cal O}_{\tilde{X}}(U) is a principal ideal, see [13, section 2.1] and Roussarie [32].

The cyclicity at a point λ 0 ∈ X \lambda_{0}\in X is the lower upper bound of the cyclicities computed at points of the compact set π − 1 ​ ( λ 0) \pi^{-1}(\lambda_{0}). As the cyclicity is an upper semi-continuous function in λ ~ 0 ∈ π − 1 ​ ( λ 0) \tilde{\lambda}_{0}\in\pi^{-1}(\lambda_{0}), and π − 1 ​ ( λ 0) \pi^{-1}(\lambda_{0}) is compact, then there is a λ ~ 0 ∈ π − 1 ​ ( λ 0) \tilde{\lambda}_{0}\in\pi^{-1}(\lambda_{0}) at which the cyclicity C ​ y ​ c ​ l ​ ( Γ, X λ ~) Cycl(\Gamma,X_{\tilde{\lambda}}) is maximal. It suffices therefore to compute this cyclicity.

In more down to earth terms, the above considerations show that, after appropriate analytic change of the parameters λ = λ ⁡ ( λ ~) \lambda=\lambda(\tilde{\lambda}), we can always suppose that the localization of the Bautin ideal at λ 0 \lambda_{0} is a principal ideal of the ring of germs of analytic functions at λ 0 \lambda_{0}. We denote its generator (according to the tradition) by ε \varepsilon. The power series expansion of the first return map takes therefore the form

 | P λ ​ ( h) = h + ε k ​ [M k ​ ( h) + O ⁡ ( ε)], M k ≠ 0 P_{\lambda}(h)=h+\varepsilon^{k}[M_{k}(h)+O(\varepsilon)],\quad M_{k}\neq 0 |  | (3) |

where M k M_{k} is the k k -th order Melnikov function, associated to P λ P_{\lambda}. The function O ⁡ ( ε) O(\varepsilon), by abuse of notation, depends on h, λ h,\lambda too, but it is of O ⁡ ( ε) O(\varepsilon) type uniformly in h, λ h,\lambda, where h h belongs to a compact complex domain in which the return map is regular. The principality of the Bautin ideal is equivalent to the claim, that M k ​ ( h) M_{k}(h) is not identically zero. The perturbed Hamiltonian vector field X ε, λ X_{\varepsilon,\lambda} can be supposed on its turn of the form

 | X ε, λ: { x ˙ = H y + ε ​ Q ​ ( x, y, λ, ε) y ˙ = − H x − ε ​ P ​ ( x, y, λ, ε) X_{\varepsilon,\lambda}:\left\{\begin{array}[]{lcr}\dot{x}&=&H_{y}+\varepsilon Q(x,y,\lambda,\varepsilon)\\ \dot{y}&=&-H_{x}-\varepsilon P(x,y,\lambda,\varepsilon)\end{array}\right. |  | (4) |

where P, Q P,Q are quadratic polynomials in x, y x,y with coefficients depending analytically in ε, λ \varepsilon,\lambda. Of course, we shall need an explicit expression for M k ​ ( h) M_{k}(h) which depends also on the unknown parameter value λ ~ 0 ∈ π − 1 ​ ( λ 0) \tilde{\lambda}_{0}\in\pi^{-1}(\lambda_{0}). Taking analytic curves

 | ε ↦ λ ⁡ ( ε), λ ⁡ ( 0) = λ 0 \varepsilon\mapsto\lambda(\varepsilon),\quad\lambda(0)=\lambda_{0} |  | (5) |

we get from ( 3)

 | P λ ⁡ ( ε) ​ ( h) = h + ε k ​ [M k ​ ( h) + O ⁡ ( ε)], M k ≠ 0 P_{\lambda(\varepsilon)}(h)=h+\varepsilon^{k}[M_{k}(h)+O(\varepsilon)],\quad M_{k}\neq 0 |  |

which allows one to compute M k M_{k} by only making use of analytic one-parameter deformations and the Françoise algorithm [11]. The general form of the first non-vanishing Melnikov function with respect to any analytic curve of the form ( 5) in the Hamiltonian (or more generally, integrable) quadratic case is computed in [22].

By abuse of notation, from now on, the return map of the form ( 3), will be denoted by P ε P_{\varepsilon}, where ε \varepsilon is the generator of the localized Bautin ideal.

#### 2.1.2 The Petrov trick and the Dulac map

The limit cycles of X λ X_{\lambda} are the fixed points of P ε P_{\varepsilon}. We are going to study these fixed points in a complex domain, where they correspond to complex limit cycles. P ε P_{\varepsilon} is obviously a composition of two Dulac maps d ± ​ ( ε) d^{\pm}(\varepsilon) as on Fig. 1

 | P ε = ( d ε −) − 1 ∘ d ε + P_{\varepsilon}=(d_{\varepsilon}^{-})^{-1}\circ d_{\varepsilon}^{+} |  |

so the fixed points h h of P ε P_{\varepsilon} are the zeros of the displacement map d ε + − d ε − d_{\varepsilon}^{+}-d_{\varepsilon}^{-}. In a complex domain this map has two singular points corresponding to the saddles S ± ​ ( ε) S_{\pm}(\varepsilon) and we shall study its zeros in the complex domain 𝒟 ε {\cal D}_{\varepsilon}, shown on Fig. 2. This domain is bounded by a circle, by the segment ( S + ​ ( ε), S − ​ ( ε)) (S_{+}(\varepsilon),S_{-}(\varepsilon)), and by the zero locus of the imaginary part of d ε + d^{+}_{\varepsilon}. The number of the zeros of d ε + − d ε − d_{\varepsilon}^{+}-d_{\varepsilon}^{-} in 𝒟 ε {\cal D}_{\varepsilon} is computed according to the argument principle: it equals the increase of the argument along the boundary of 𝒟 ε {\cal D}_{\varepsilon}.

Along the circle and far from the critical points, the displacement function is "well" approximated by ε k ​ M k ​ ( h) \varepsilon^{k}M_{k}(h) which allows one to estimate the increase of the argument.

Along the segment ( S + ​ ( ε), S − ​ ( ε)) (S_{+}(\varepsilon),S_{-}(\varepsilon)) the zeros of the imaginary part of the displacement function coincide with the fixed points of the holomorphic holonomy map along the separatrix through S − ​ ( ε) S_{-}(\varepsilon). The zeros are therefore well approximated, similarly to ( 3), by an Abelian integral along the cycle δ − ​ ( h) \delta_{-}(h) in the fibers of H H, vanishing at S − ​ ( 0) S_{-}(0). This observation may be seen as a far going generalization of the so called Petrov trick, see [15] for details.

Along the zero locus of the imaginary part of d ε + d^{+}_{\varepsilon}, the zeros of imaginary part of the displacement map coincide with the fixed points of the composition of the holonomies associated to the separatrices through S − ​ ( ε) S_{-}(\varepsilon) and S + ​ ( ε) S_{+}(\varepsilon). As this map is holomorphic, it is similarly approximated by the zeros of an Abelian integral along δ − ​ ( h) + δ + ​ ( h) \delta_{-}(h)+\delta_{+}(h), where δ ± ​ ( h) \delta_{\pm}(h) are cycles in the fibers of H H, vanishing at S ± ​ ( 0) S_{\pm}(0) respectively.

Thus, to count the number of the limit cycles, it is enough to inspect the behavior of certain Abelian integrals.

## 3 Abelian integrals related to quadratic perturbations of reversible quadratic Hamiltonian vector fields.

In this section we recall the Abelian integrals, involved in the proof of Theorem 1, and establish their properties. The details can be found in [21, 22].

Consider the quadratic reversible Hamiltonian system d ​ H = 0, dH=0, where the Hamiltonian function is taken in the normal form [21]

 | H ⁡ ( x, y) = x ⁡ [y 2 + a ​ x 2 − 3 ​ ( a − 1) ​ x + 3 ​ ( a − 2)], a ∈ ℝ H(x,y)=x[y^{2}+ax^{2}-3(a-1)x+3(a-2)],\quad a\in{\mathbb{R}} |  | (6) |

The Hamiltonian system has a center C 0 = ( 1, 0) C_{0}=(1,0) on the level set H = t 0 = a − 3 H=t_{0}=a-3. It is surrounded by a saddle connection containing two saddles S ± = ( 0, ± 3 ​ ( 2 − a)) S_{\pm}=(0,\pm\sqrt{3(2-a)}) if and only if the parameter a a takes values in ( − 1, 2) (-1,2). This connection is a part of the zero-level set H = t s = 0 H=t_{s}=0. When a ∈ ( 0, 2) a\in(0,2), there is a second center

 | C 1 = ( a − 2 a, 0), H ⁡ ( C 1) = t 1 = ( a + 1) ​ ( a − 2) 2 a 2 C_{1}=\left(\frac{a-2}{a},0\right),\quad H(C_{1})=t_{1}=\frac{(a+1)(a-2)^{2}}{a^{2}} |  |

surrounded by other part of the zero level set and containing the same two saddles.

Let δ ( t) ⊂ { H = t } \delta(t)\subset\{H=t\} be a continuous family of ovals surrounding a center. Take a small quadratic one-parameter perturbation

 | d ​ H + ε ​ ω = 0, ω = ω ⁡ ( ε) = f ⁡ ( x, y, ε) ​ d ​ x + g ⁡ ( x, y, ε) ​ d ​ y, dH+\varepsilon\omega=0,\quad\omega=\omega(\varepsilon)=f(x,y,\varepsilon)dx+g(x,y,\varepsilon)dy, |  | (7) |

where f f, g g are real quadratic polynomials of x, y x,y with coefficients analytic with respect to the small parameter ε \varepsilon. Then the first return map P ε P_{\varepsilon} near an oval δ ⁡ ( t) \delta(t) is well defined and has the form

 | P ε ​ ( t) = t + ε ​ M 1 ​ ( t) + ε 2 ​ M 2 ​ ( t) + ε 3 ​ M 3 ​ ( t) + …, P_{\varepsilon}(t)=t+\varepsilon M_{1}(t)+\varepsilon^{2}M_{2}(t)+\varepsilon^{3}M_{3}(t)+\ldots, |  | (8) |

One may show, by making use of [17, Theorem 2], that the first non-vanishing Poincaré-Pontryagin-Melnikov function M k M_{k} associated to an arbitrary polynomial perturbation is an Abelian integral. More precisely, we have

###### Theorem 2 ( [22]).

In the quadratic case M k M_{k} takes the form

 | M 1 ​ ( t) = ∫ δ ⁡ ( t) [α + β ​ x] ​ y ​ 𝑑 x, M k ​ ( t) = ∫ δ ⁡ ( t) [α + β ​ x + γ ​ x − 1] ​ y ​ 𝑑 x, k ≥ 2, M_{1}(t)=\int_{\delta(t)}[\alpha+\beta x]ydx,\quad M_{k}(t)=\int_{\delta(t)}[\alpha+\beta x+\gamma x^{-1}]ydx,\quad k\geq 2, |  | (9) |

where α, β, γ \alpha,\beta,\gamma are appropriate constants depending on the perturbation.

Consider the Abelian integrals

 | J k ​ ( t) = ∫ δ ⁡ ( t) x k ​ y ​ 𝑑 x, k ∈ ℤ J_{k}(t)=\int_{\delta(t)}x^{k}ydx,\quad k\in{\mathbb{Z}} |  |

(oriented clockwise - along with the Hamiltonian vector field).

###### Lemma 1 ( [21]).

The integrals J k ​ ( t) J_{k}(t), k = − 1, 0, 1 k=-1,0,1 satisfy the following system with respect to t t:

 | t ​ J − 1 ′ + ( 4 − 2 ​ a) ​ J 0 ′ + ( a − 1) ​ J 1 ′ = 1 3 ​ J − 1, ( 1 − a) ​ t ​ J − 1 ′ + 2 ​ a ​ t ​ J 0 ′ + ( 3 + 2 ​ a − a 2) ​ J 1 ′ = 4 3 ​ a ​ J 0, ( a − 2) ​ t ​ J − 1 ′ + ( 2 − 2 ​ a) ​ t ​ J 0 ′ + a ​ t ​ J 1 ′ = 3 2 ​ ( 1 − a) ​ J 0 + a ​ J 1. \begin{array}[]{l}tJ_{-1}^{\prime}+(4-2a)J_{0}^{\prime}+(a-1)J_{1}^{\prime}=\frac{1}{3}J_{-1},\\ (1-a)tJ_{-1}^{\prime}+2atJ_{0}^{\prime}+(3+2a-a^{2})J_{1}^{\prime}=\frac{4}{3}aJ_{0},\\ (a-2)tJ_{-1}^{\prime}+(2-2a)tJ_{0}^{\prime}+atJ_{1}^{\prime}=\frac{3}{2}(1-a)J_{0}+aJ_{1}.\end{array} |  | (10) |

###### Lemma 2.

The integrals J k ​ ( t) J_{k}(t), k = − 1, 0, 1 k=-1,0,1 have the following asymptotic expansions near t = − 0 t=-0:

 | J − 1 ​ ( t) = − 2 ​ 3 ​ ( 2 − a) ​ [1 − a − 1 12 ​ ( a − 2) 2 ​ t − 11 ​ a 2 − 22 ​ a + 15 576 ​ ( a − 2) 4 ​ t 2 − 35 ​ ( a − 1) ​ ( 5 ​ a 2 − 10 ​ a + 9) 20736 ​ ( a − 2) 6 ​ t 3 + …] ​ ln ⁡ t + a 0 + a 1 ​ t + a 2 ​ t 2 ​ …, J 0 ​ ( t) = − 2 ​ 3 ​ ( 2 − a) ​ [− 1 6 ​ ( a − 2) ​ t − a − 1 48 ​ ( a − 2) 3 ​ t 2 − 85 ​ a 2 − 170 ​ a + 105 10368 ​ ( a − 2) 5 ​ t 3 + …] ​ ln ⁡ t + b 0 + b 1 ​ t + b 2 ​ t 2 + …, J 1 ​ ( t) = − 2 ​ 3 ​ ( 2 − a) ​ [− 1 72 ​ ( a − 2) 2 ​ t 2 − 5 ​ ( a − 1) 864 ​ ( a − 2) 4 ​ t 3 + …] ​ ln ⁡ t + c 0 + c 1 ​ t + c 2 ​ t 2 ​ …. \begin{array}[]{rl}J_{-1}(t)&=-2\sqrt{3(2-a)}[1-\frac{a-1}{12(a-2)^{2}}t-\frac{11a^{2}-22a+15}{576(a-2)^{4}}t^{2}-\frac{35(a-1)(5a^{2}-10a+9)}{20736(a-2)^{6}}t^{3}+\ldots]\ln t\\[5.69054pt] &+a_{0}+a_{1}t+a_{2}t^{2}\ldots,\\[5.69054pt] J_{0}(t)&=-2\sqrt{3(2-a)}[-\frac{1}{6(a-2)}t-\frac{a-1}{48(a-2)^{3}}t^{2}-\frac{85a^{2}-170a+105}{10368(a-2)^{5}}t^{3}+\ldots]\ln t\\[5.69054pt] &+b_{0}+b_{1}t+b_{2}t^{2}+\ldots,\\[5.69054pt] J_{1}(t)&=-2\sqrt{3(2-a)}[-\frac{1}{72(a-2)^{2}}t^{2}-\frac{5(a-1)}{864(a-2)^{4}}t^{3}+\ldots]\ln t+c_{0}+c_{1}t+c_{2}t^{2}\ldots.\end{array} |  | (11) |

This lemma is a consequence of the following basic property of system ( 10):

###### Lemma 3.

If a ≠ 0 a\neq 0, a fundamental system of solutions ( J − 1, J 0, J 1) t (J_{-1},J_{0},J_{1})^{t} of ( 10) (\ref{p-f}) near t = 0 t=0 is the following:

 | P ⁡ ( t) = ( 3 ​ ( a − 1) 3 ​ ( 3 + 2 ​ a − a 2) 4 ​ a 9 ​ ( a − 1) ​ ( 3 + 2 ​ a − a 2) 8 ​ a 2) + ( 0 0 1) ​ t, Q ⁡ ( t) = ( 1 0 0) − ( a − 1 12 ​ ( a − 2) 2 1 6 ​ ( a − 2) 0) ​ t − ( 11 ​ a 2 − 22 ​ a + 15 576 ​ ( a − 2) 4 a − 1 48 ​ ( a − 2) 3 1 72 ​ ( a − 2) 2) ​ t 2 − ( 35 ​ ( a − 1) ​ ( 5 ​ a 2 − 10 ​ a + 9) 20736 ​ ( a − 2) 6 85 ​ a 2 − 170 ​ a + 105 10368 ​ ( a − 2) 5 5 ​ ( a − 1) 864 ​ ( a − 2) 4) ​ t 3 + …, R ⁡ ( t) = Q ⁡ ( t) ​ ln ⁡ t + S ⁡ ( t), \begin{array}[]{l}P(t)=\left(\begin{array}[]{c}3(a-1)\\ \frac{3(3+2a-a^{2})}{4a}\\ \frac{9(a-1)(3+2a-a^{2})}{8a^{2}}\end{array}\right)+\left(\begin{array}[]{c}0\\ 0\\ 1\end{array}\right)t,\\[8.53581pt] Q(t)=\left(\begin{array}[]{c}1\\ 0\\ 0\end{array}\right)-\left(\begin{array}[]{c}\frac{a-1}{12(a-2)^{2}}\\ \frac{1}{6(a-2)}\\ 0\end{array}\right)t-\left(\begin{array}[]{c}\frac{11a^{2}-22a+15}{576(a-2)^{4}}\\ \frac{a-1}{48(a-2)^{3}}\\ \frac{1}{72(a-2)^{2}}\end{array}\right)t^{2}-\left(\begin{array}[]{c}\frac{35(a-1)(5a^{2}-10a+9)}{20736(a-2)^{6}}\\ \frac{85a^{2}-170a+105}{10368(a-2)^{5}}\\ \frac{5(a-1)}{864(a-2)^{4}}\end{array}\right)t^{3}+\ldots,\\[8.53581pt] R(t)=Q(t)\ln t+S(t),\end{array} |  | (12) |

with S ⁡ ( t) S(t) analytic function in a neighbourhood of t = 0 t=0.

Proof. Rewrite system ( 10) in the form ( A 1 ​ t + A 0) ​ J ′ = B ​ J (A_{1}t+A_{0})J^{\prime}=BJ. System ( 10) has at its critical value t = 0 t=0 a triple characteristic exponent equal to zero, while its characteristic exponents at infinity are − 1 3 -\frac{1}{3}, − 2 3 -\frac{2}{3}, − 1 -1. Hence, there is a polynomial solution P ⁡ ( t) P(t) of degree one which is easy to find. To calculate Q ⁡ ( t) Q(t), we replace

 | Q ⁡ ( t) = q 0 + q 1 ​ t + q 2 ​ t 2 + q 3 ​ t 3 + q 4 ​ t 4 + … Q(t)=q_{0}+q_{1}t+q_{2}t^{2}+q_{3}t^{3}+q_{4}t^{4}+\ldots |  |

in the system to obtain recursive equations

 | ( j A 1 − B) q j + ( j + 1) A 0 q j + 1 = 0, j = 0, 1, 2, 3, …. (jA_{1}-B)q_{j}+(j+1)A_{0}q_{j+1}=0,\quad j=0,1,2,3,\ldots. |  | (13) |

The third equation in the system obtained for j = 0 j=0 implies that 3 2 ​ ( 1 − a) ​ q 0, 0 + a ​ q 0, 1 = 0 \frac{3}{2}(1-a)q_{0,0}+aq_{0,1}=0 where q 0 = ( q 0, − 1, q 0, 0, q 0, 1) ⊤ q_{0}=(q_{0,-1},q_{0,0},q_{0,1})^{\top}. Therefore, one can choose without loss of generality q 0 = ( 1, 0, 0) ⊤ q_{0}=(1,0,0)^{\top}. Then any analytic solution of ( 10) would be a unique linear combination of P ⁡ ( t) P(t) and Q ⁡ ( t) Q(t). Fixing in such a way Q ⁡ ( 0) Q(0), then q 1 q_{1}, q 2 q_{2} and so on are uniquely determined from system ( 13).

Now, if we take a linear combination Q ~ \tilde{Q} of P P and Q Q and replace R ⁡ ( t) = Q ~ ​ ( t) ​ ln ⁡ t + S ⁡ ( t) R(t)=\tilde{Q}(t)\ln t+S(t) in the system ( A 1 ​ t + A 0) ​ R ′ ​ ( t) = B ​ R ​ ( t) (A_{1}t+A_{0})R^{\prime}(t)=BR(t), we obtain A 1 ​ Q ~ + t − 1 ​ A 0 ​ Q ~ + ( A 1 ​ t + A 0) ​ S ′ = B ​ S A_{1}\tilde{Q}+t^{-1}A_{0}\tilde{Q}+(A_{1}t+A_{0})S^{\prime}=BS. Hence, A 0 ​ Q ~ ​ ( 0) = 0 A_{0}\tilde{Q}(0)=0 which means that Q ~ ​ ( t) \tilde{Q}(t) is proportional to Q ⁡ ( t) Q(t). Therefore one can simply take Q ~ = Q \tilde{Q}=Q. □ \Box

Proof of Lemma 2. Let x 1 x_{1} be the (smaller) positive root of the equation r ⁡ ( x) = − a ​ x 2 + 3 ​ ( a − 1) ​ x − 3 ​ ( a − 2) = 0 r(x)=-ax^{2}+3(a-1)x-3(a-2)=0 where a ∈ ( − 1, 2) a\in(-1,2). Then, J k ​ ( 0) = ∫ δ ⁡ ( 0) x k ​ y ​ 𝑑 x = 2 ​ ∫ 0 x 1 x k ​ r ⁡ ( x) ​ 𝑑 x J_{k}(0)=\int_{\delta(0)}x^{k}ydx=2\int_{0}^{x_{1}}x^{k}\sqrt{r(x)}dx for k = 0, 1 k=0,1. Therefore

 | 3 2 ​ ( a − 1) ​ J 0 ​ ( 0) − a ​ J 1 ​ ( 0) = ∫ 0 x 1 r ′ ​ ( x) ​ r ⁡ ( x) ​ 𝑑 x = − 2 3 ​ ( 3 ​ ( 2 − a)) 3 / 2. \frac{3}{2}(a-1)J_{0}(0)-aJ_{1}(0)=\int_{0}^{x_{1}}r^{\prime}(x)\sqrt{r(x)}dx=-\frac{2}{3}(3(2-a))^{3/2}. |  |

On the other hand, the third equation of ( 10) implies

 | 3 2 ​ ( 1 − a) ​ J 0 ​ ( 0) + a ​ J 1 ​ ( 0) = ( a − 2) ​ ( t ​ J − 1 ′ ​ ( t)) | t = 0. \frac{3}{2}(1-a)J_{0}(0)+aJ_{1}(0)=(a-2)\left.(tJ_{-1}^{\prime}(t))\right|_{t=0}. |  |

Finally, if J ⁡ ( t) = λ ⁡ [Q ⁡ ( t) ​ ln ⁡ t + S ⁡ ( t)] + μ ​ P ​ ( t) + ν ​ Q ​ ( t) J(t)=\lambda[Q(t)\ln t+S(t)]+\mu P(t)+\nu Q(t), then ( t ​ J − 1 ′ ​ ( t)) | t = 0 = λ = − 2 ​ 3 ​ ( 2 − a) \left.(tJ_{-1}^{\prime}(t))\right|_{t=0}=\lambda=-2\sqrt{3(2-a)}. Case a = 0 a=0 follows by continuity. □ \Box

## 4 Cyclicity of two-saddle cycles

In the section we prove Theorem 1.

We shall prove it in several steps. A plane quadratic Hamiltonian system with a two-saddle loop can be written, up to an affine change of the variables, in the form d ​ H = 0 dH=0 where H H is in the form ( 6).

### 4.1 The case M 1 ≠ 0 M_{1}\neq 0

In this section we consider the perturbed quadratic plane quadratic Hamiltonian system ( 7) under the generic assumption that

 | M 1 ( t) = ∫ δ ⁡ ( t) ω | ε = 0 = ∫ ∫ { H ≤ t } [α + β x] d x d y M_{1}(t)=\int_{\delta(t)}\omega|_{\varepsilon=0}=\int\int_{\{H\leq t\}}[\alpha+\beta x]dxdy |  |

is not identically zero.

Due to Lemma 2, M 1 ​ ( t) M_{1}(t) vanishes identically in a co-dimension two analytic set defined by { α = β = 0 } \{\alpha=\beta=0\}. The Poincaré-Pontryagin function M 1 M_{1} is well defined at t = 0 t=0 in which case it is the well known Melnikov integral along the heteroclinic loop δ ⁡ ( 0) \delta(0). It is classically known that when M 1 ​ ( t) ≢ 0 M_{1}(t)\not\equiv 0, the vanishing of the Melnikov integral M 1 ​ ( 0) M_{1}(0) is a necessary condition for a bifurcation of a limit cycle (and in the opposite case the heteroclinic loop is broken under the perturbation)

###### Proposition 1.

If M 1 ​ ( 0) ≠ 0 M_{1}(0)\neq 0, then no limit cycles bifurcate from the two-saddle loop Γ \Gamma.

Proof. Suppose that there is a sequence of limit cycles δ ε i \delta_{\varepsilon_{i}} of ( 7) which tend to Γ \Gamma as ε i \varepsilon_{i} tends to 0 0. Then

 | 0 = − ∫ δ ε i d H = ε i ∫ δ ε i ω 0=-\int_{\delta_{\varepsilon_{i}}}dH=\varepsilon_{i}\int_{\delta_{\varepsilon_{i}}}\omega |  |

which implies

 | 0 = lim ε i → 0 ∫ δ ε i ω = ∫ Γ ω | ε = 0 = M 1 ​ ( 0). 0=\lim_{\varepsilon_{i}\rightarrow 0}\int_{\delta_{\varepsilon_{i}}}\omega=\int_{\Gamma}\omega|_{\varepsilon=0}=M_{1}(0). |  |

□ \Box

The complete Abelian integral M 1 ​ ( t) M_{1}(t) has the following convergent expansion near the critical saddle value t = 0 t=0

 | M 1 ​ ( t) = d 0 + d 1 ​ t ​ ln ⁡ t + d 2 ​ t + d 3 ​ t 2 ​ ln ⁡ t + … M_{1}(t)=d_{0}+d_{1}t\ln t+d_{2}t+d_{3}t^{2}\ln t+\dots |  | (14) |

Let δ ± ​ ( t) ∈ H 1 ​ ( Γ t, ℤ) \delta_{\pm}(t)\in H_{1}(\Gamma_{t},{\mathbb{Z}}), Γ t = { ( x, y) ∈ ℂ 2: H ⁡ ( x, y) = t } \Gamma_{t}=\{(x,y)\in{\mathbb{C}}^{2}:H(x,y)=t\}, be the two continuous families of cycles, vanishing at the saddle points S ± S_{\pm} respectively, with orientations chosen in a way that for the respective intersection indices holds

 | δ ⋅ δ + = δ ⋅ δ − = − 1. \delta\cdot\delta_{+}=\delta\cdot\delta_{-}=-1. |  | (15) |

Then

 | M 1 ​ ( t) = ∫ δ ⁡ ( t) ω 0 = ln ⁡ t 2 ​ π ​ − 1 ​ ( ∫ δ + ​ ( t) ω 0 + ∫ δ − ​ ( t) ω 0) + d 0 + d 2 ​ t + O ⁡ ( t 2) M_{1}(t)=\int_{\delta(t)}\omega_{0}=\frac{\ln t}{2\pi\sqrt{-1}}(\int_{\delta_{+}(t)}\omega_{0}+\int_{\delta_{-}(t)}\omega_{0})+d_{0}+d_{2}t+O(t^{2}) |  | (16) |

where ω 0 = ω | ε = 0 \omega_{0}=\omega|_{\varepsilon=0}. The involution ( x, y) → ( x, − y) (x,y)\rightarrow(x,-y) leaves the level set { H = h } \{H=h\} invariant, reversing its orientation. Therefore it acts on δ, δ ± \delta,\delta_{\pm} as follows

 | δ → − δ, δ − → − δ +, δ + → − δ −, \delta\rightarrow-\delta,\;\;\delta_{-}\rightarrow-\delta_{+},\;\;\delta_{+}\rightarrow-\delta_{-}, |  |

which implies

 | ∫ δ + ​ ( t) ω 0 = ∫ δ − ​ ( t) ω 0. \int_{\delta_{+}(t)}\omega_{0}=\int_{\delta_{-}(t)}\omega_{0}. |  | (17) |

Let h δ ± ε h^{\varepsilon}_{\delta_{\pm}} be the two holonomy maps associated to the separatrices of the perturbed foliation, intersecting the cross-section σ \sigma. There are two-possible orientations for the loop defining the holonomy, this corresponds to a choice of orientation of δ ± \delta_{\pm}, see ( 15). Similarly to ( 8) we have

 | h δ + ε ​ ( t) \displaystyle h^{\varepsilon}_{\delta_{+}}(t) | = \displaystyle= | t + ε ​ ∫ δ + ​ ( t) ω 0 + O ⁡ ( ε 2) \displaystyle t+\varepsilon\int_{\delta_{+}(t)}\omega_{0}+O(\varepsilon^{2}) |  | (18) |

 | h δ − ε ​ ( t) \displaystyle h^{\varepsilon}_{\delta_{-}}(t) | = \displaystyle= | t + ε ​ ∫ δ − ​ ( t) ω 0 + O ⁡ ( ε 2) \displaystyle t+\varepsilon\int_{\delta_{-}(t)}\omega_{0}+O(\varepsilon^{2}) |  | (19) |

 | h δ + ε ∘ h δ − ε ​ ( t) \displaystyle h^{\varepsilon}_{\delta_{+}}\circ h^{\varepsilon}_{\delta_{-}}(t) | = \displaystyle= | t + ε ⁡ ( ∫ δ + ​ ( t) ω 0 + ∫ δ − ​ ( t) ω 0) + O ⁡ ( ε 2) \displaystyle t+\varepsilon(\int_{\delta_{+}(t)}\omega_{0}+\int_{\delta_{-}(t)}\omega_{0})+O(\varepsilon^{2}) |  | (20) |

 | h δ − ε ∘ h δ + ε ​ ( t) \displaystyle h^{\varepsilon}_{\delta_{-}}\circ h^{\varepsilon}_{\delta_{+}}(t) | = \displaystyle= | t + ε ⁡ ( ∫ δ + ​ ( t) ω 0 + ∫ δ − ​ ( t) ω 0) + O ⁡ ( ε 2) \displaystyle t+\varepsilon(\int_{\delta_{+}(t)}\omega_{0}+\int_{\delta_{-}(t)}\omega_{0})+O(\varepsilon^{2}) |  | (21) |

###### Proposition 2.

If d 0 = d 1 = 0 d_{0}=d_{1}=0, then α = β = 0 \alpha=\beta=0.

Proof. According to Lemma 2 d 1 = α / 3 ​ ( a − 2) d_{1}=\alpha/\sqrt{3(a-2)}. If α = 0 \alpha=0 then

 | d 0 = β J 1 ( 0) where J 1 ( 0) = ∫ ∫ { H < 0 } x d x ∧ d y ≠ 0. □ d_{0}=\beta J_{1}(0)\mbox{ where }J_{1}(0)=\int\!\!\int_{\{H<0\}}xdx\wedge dy\neq 0.\Box |  |

Therefore M 1 ≠ 0 M_{1}\neq 0 if and only if | d 0 | 2 + | d 1 | 2 ≠ 0 |d_{0}|^{2}+|d_{1}|^{2}\neq 0, and hence at most one zero of M 1 M_{1} can bifurcate from t = 0 t=0. Of course, no conclusion about the number of the limit cycles can be deduced at this stage. For a further use, let us note that the above implies (see also Proposition 1)

###### Corollary 1.

If a limit cycle bifurcates from the two-saddle loop, then the Abelian integral ∫ δ ± ​ ( t) ω 0 \int_{\delta_{\pm}(t)}\omega_{0} has a simple zero at the origin.

###### Proposition 3.

If the Melnikov function M 1 M_{1} is not identically zero, then at most two limit cycles bifurcate from Γ \Gamma.

###### Proposition 4.

There exists a perturbed quadratic system of the form ( 4) and M 1 ≠ 0 M_{1}\neq 0, with exactly two limit cycles bifurcating from the two-saddle loop.

The proof of this proposition will be postponed to the Appendix. To the end of this subsection we shall prove Proposition 3. Although our proof will be self-contained, we shall omit some technical details, for which we refer to [14, section 4].

Consider the Dulac maps d ε + d^{+}_{\varepsilon}, d ε − d^{-}_{\varepsilon} associated to the perturbed foliation, and to the cross sections σ \sigma and τ \tau, see Fig. 1. We parameterize each cross-section by the restriction of the first integral f f on it, and denote t = f | σ t=f|_{\sigma}. Each function d ε ± d^{\pm}_{\varepsilon} is multivalued and has a critical point at S ± ​ ( ε) ∈ ℝ S_{\pm}(\varepsilon)\in\mathbb{R}, S ± ​ ( 0) = 0 S_{\pm}(0)=0. The saddle points S +, S − S_{+},S_{-} depend analytically on ε \varepsilon. Without loss of generality we shall suppose that ε > 0 \varepsilon>0 and S − ​ ( ε) > S + ​ ( ε) S_{-}(\varepsilon)>S_{+}(\varepsilon), see Fig. 2. A limit cycle intersects the cross-section σ \sigma at t t if and only if d ε + ​ ( t) = d ε − ​ ( t) d^{+}_{\varepsilon}(t)=d^{-}_{\varepsilon}(t). Therefore zeros of the displacement map

 | d ε + − d ε − = ( d ε + ∘ ( d ε −) − 1 − i ​ d) ∘ d ε − = ( P ε − i ​ d) ∘ d ε − d^{+}_{\varepsilon}-d^{-}_{\varepsilon}=(d^{+}_{\varepsilon}\circ(d^{-}_{\varepsilon})^{-1}-id)\circ d^{-}_{\varepsilon}=(P_{\varepsilon}-id)\circ d^{-}_{\varepsilon} |  |

correspond to limit cycles. Our aim is to bound the number of those zeros which are real, bigger than S − ​ ( ε) S_{-}(\varepsilon), and tend to 0 0 as ε \varepsilon tends to 0 0. For this, we consider an appropriate complex domain 𝒟 ε \mathcal{D}_{\varepsilon} of the universal covering of ℂ ∖ { S + ​ ( ε) } \mathbb{C}\setminus\{S_{+}(\varepsilon)\} and compute the number of the zeros of the displacement map, by making use of the argument principle. The reader may find useful to compare our method, to the Petrov’s method [28], used to compute zeros of complete elliptic integrals. The crucial fact is that, roughly speaking, *the monodromy of the Dulac map is the holonomy of its separatrix*. The analytical counter-part of this statement is that the zero locus ℋ ε ± \mathcal{H}^{\pm}_{\varepsilon} of the imaginary part of the Dulac map d ε ± d^{\pm}_{\varepsilon} for ℜ ⁡ ( t) < S ± ​ ( ε) \Re(t)<S_{\pm}(\varepsilon) is a real-analytic curve in { ℝ 2 = ℂ } ∩ 𝒟 ε \{\mathbb{R}^{2}=\mathbb{C}\}\cap\mathcal{D}_{\varepsilon}, defined in terms of the holonomies of the separatrices. It follows from [14, section 4] that

 | ℋ ε + = { z ∈ ℂ 2: h δ + ε ​ ( z) = z ¯ }, ℋ ε − = { z ∈ ℂ 2: h δ − ε ​ ( z ¯) = z }. \mathcal{H}_{\varepsilon}^{+}=\{z\in\mathbb{C}^{2}:h^{\varepsilon}_{\delta_{+}}(z)=\overline{z}\},\mathcal{H}_{\varepsilon}^{-}=\{z\in\mathbb{C}^{2}:h^{\varepsilon}_{\delta_{-}}(\overline{z})=z\}. |  |

Note that the above describes, strictly speaking, only one connected component of ℋ ε ± \mathcal{H}_{\varepsilon}^{\pm}, the second one is "complex conjugate" and defined by a similar formula

 | ℋ ε + = { z ∈ ℂ 2: h δ + ε ​ ( z ¯) = z }, ℋ ε − = { z ∈ ℂ 2: h δ − ε ​ ( z) = z ¯ }. \mathcal{H}_{\varepsilon}^{+}=\{z\in\mathbb{C}^{2}:h^{\varepsilon}_{\delta_{+}}(\overline{z})=z\},\mathcal{H}_{\varepsilon}^{-}=\{z\in\mathbb{C}^{2}:h^{\varepsilon}_{\delta_{-}}(z)=\overline{z}\}. |  |

By abuse of notation we use ℋ ε ± \mathcal{H}_{\varepsilon}^{\pm} to denote only the first connected component (the second corresponds to the opposite orientation of δ ± \delta_{\pm}).

The analyticity of the above curves is crucial in computing the complex zeros of the transcendental Dulac maps. For instance, to compute the number of intersection points of ℋ ε ± \mathcal{H}_{\varepsilon}^{\pm} with the real axis { z = z ¯ } \{z=\bar{z}\} we have to solve the equation

 | h δ ± ε ​ ( z) = z, h^{\varepsilon}_{\delta_{\pm}}(z)=z, |  | (22) |

and to compute the number of the intersection point of ℋ ε − \mathcal{H}_{\varepsilon}^{-} with ℋ ε + \mathcal{H}_{\varepsilon}^{+}, we have to solve the equation

 | h δ − ε ∘ h δ + ε ​ ( z) = z. h^{\varepsilon}_{\delta_{-}}\circ h^{\varepsilon}_{\delta_{+}}(z)=z. |  | (23) |

Let us define first the complex domain 𝒟 ε \mathcal{D}_{\varepsilon} in which the computation will take place: it is bounded by the circle

 | S R = { t: | t | = R }, S_{R}=\{t:|t|=R\}, |  |

by the interval [S + ​ ( ε), S − ​ ( ε)] [S_{+}(\varepsilon),S_{-}(\varepsilon)], and by the zero locus ℋ ε + \mathcal{H}_{\varepsilon}^{+}, as it is shown on Fig. 2.

Let R, ε 0 R,\varepsilon_{0} be real numbers subject to certain technical conditions of the form

 | 1 >> R >> ε 0 > 0. 1>>R>>\varepsilon_{0}>0. |  |

The subsequent computations will hold for all ε \varepsilon, such that

 | ε 0 > ε > 0. \varepsilon_{0}>\varepsilon>0. |  |

Figure 2: The domain 𝒟 ε \mathcal{D}_{\varepsilon}

We wish to bound the number of the zeros of the displacement map in the domain 𝒟 ε \mathcal{D}_{\varepsilon}. If the map were an analytic function in a neighborhood of the closure of the domain, and non-vanishing on its border, we could apply the argument principle:

*The number of the zeros (counted with multiplicity) in the complex domain 𝒟 ε \mathcal{D}_{\varepsilon} equals the increment of the argument of this function along the border of 𝒟 ε \mathcal{D}_{\varepsilon}, divided by 2 ​ π 2\pi. *

The above principle holds true with the analyticity condition relaxed: it is enough that the map allows a continuation on the closure of the domain 𝒟 ε \mathcal{D}_{\varepsilon}, considered as a subset of the universal covering of

 | ℂ ∖ { S + ​ ( ε), S − ​ ( ε) }. \mathbb{C}\setminus\{S_{+}(\varepsilon),S_{-}(\varepsilon)\}. |  |

This is indeed the case, and it remains to assure finally the non-vanishing property. Along S R S_{R} the displacement map has a known asymptotic behavior and hence does not vanish. Along the remaining part of the border, including S ± ​ ( ε) S_{\pm}(\varepsilon) the displacement map can have isolated zeros. For this we may add to the displacement map a small real constant c > 0 c>0, sufficiently smaller with respect to ε \varepsilon. The new function d ε + − d ε − + c d^{+}_{\varepsilon}-d^{-}_{\varepsilon}+c which we obtain in this way has at least so many zeros in 𝒟 ε \mathcal{D}_{\varepsilon}, as the original displacement map, but is non-vanishing on the border of the domain. The increase of the argument of d ε + − d ε − + c d^{+}_{\varepsilon}-d^{-}_{\varepsilon}+c along S R S_{R} will be close to the increase of the argument of d ε + − d ε − d^{+}_{\varepsilon}-d^{-}_{\varepsilon} (because c << ε c<<\varepsilon). At last, the imaginary parts of d ε + − d ε − d^{+}_{\varepsilon}-d^{-}_{\varepsilon} and d ε + − d ε − + c d^{+}_{\varepsilon}-d^{-}_{\varepsilon}+c are the same. The intuitive content of this is that when the displacement map has zeros on the border of the domain, it will have less zeros in the interior of the domain.

To resume, according to the argument principle, to evaluate the number of the zeros of the displacement map in the the domain 𝒟 ε \mathcal{D}_{\varepsilon}, it is enough to evaluate

1. 1.

The increase of the argument of the displacement map, along the circle S R S_{R}.

2. 2.

The number of the zeros of the imaginary part of the displacement map, along the interval [S + ​ ( ε), S − ​ ( ε)] [S_{+}(\varepsilon),S_{-}(\varepsilon)].

3. 3.

The number of the zeros of the imaginary part of the displacement map, along the real analytic curve ℋ ε + \mathcal{H}_{\varepsilon}^{+}.

To the end of the section we evaluate the above quantities.

1. 1.

By Proposition 1, if limit cycles bifurcate from the double loop, then

 | d 0 = α J 0 ( 0) + β J 1 ( 0) = ∫ ∫ { H < 0 } ( α + β x) d x ∧ d y = 0 d_{0}=\alpha J_{0}(0)+\beta J_{1}(0)=\int\!\!\int_{\{H<0\}}(\alpha+\beta x)dx\wedge dy=0 |  |

and hence α ≠ 0, β ≠ 0 \alpha\neq 0,\beta\neq 0. From this we conclude that the displacement map along the circle S R S_{R} is approximated by ε ​ M 1 \varepsilon M_{1} which has as a leading term t ​ ln ⁡ t t\ln t (because d 0 = 0 d_{0}=0 but d 1 ≠ 0 d_{1}\neq 0). The increase of the argument of t ​ ln ⁡ t t\ln t, and hence of the displacement map, along the circle S R S_{R} is *close to 2 ​ π 2\pi but strictly less than 2 ​ π 2\pi*.

2. 2.

The imaginary part of the displacement map, along the interval [S + ​ ( ε), S − ​ ( ε)] [S_{+}(\varepsilon),S_{-}(\varepsilon)] equals the imaginary part of d ε − ​ ( t) d^{-}_{\varepsilon}(t). Its zeros equal the number of intersection points of ℋ ε + \mathcal{H}_{\varepsilon}^{+} with the real axes, which amounts to solve h δ − ε ​ ( z) = z h^{\varepsilon}_{\delta_{-}}(z)=z, see ( 22). By ( 19) the number of the zeros is bounded by the multiplicity of the holomorphic Abelian integral ∫ δ − ​ ( t) ω 0 \int_{\delta_{-}(t)}\omega_{0} having a simple zero at the origin (Corollary 1). Note, however, that the holonomy map h δ − ε h^{\varepsilon}_{\delta_{-}} has S − ​ ( ε) S_{-}(\varepsilon) as a fixed point (a zero). *Therefore the imaginary part of the displacement map does not vanish along the open interval ( S + ​ ( ε), S − ​ ( ε)) (S_{+}(\varepsilon),S_{-}(\varepsilon)). *

3. 3.

The number of the zeros of the imaginary part of the displacement map, along the real analytic curve ℋ ε + \mathcal{H}_{\varepsilon}^{+} equals the number of the zeros of the imaginary part of d ε − d^{-}_{\varepsilon} along this curve, that is to say the number of intersection points of ℋ ε + \mathcal{H}_{\varepsilon}^{+} with ℋ ε − \mathcal{H}_{\varepsilon}^{-}. *According to ( 23), ( 21) and Corollary 1, this number is one.*

We conclude that the displacement map can have at most two zeros in the domain 𝒟 ε \mathcal{D}_{\varepsilon}, this for all positive ε \varepsilon smaller than ε 0 \varepsilon_{0} (similar considerations are valid for negative ε \varepsilon).

As we already noted, d 0 = 0 d_{0}=0 implies d 1 ≠ 0 d_{1}\neq 0 in the expansion ( 14) and therefore M 1 M_{1} can have at most one simple zero close to t = 0 t=0. One may wonder, whether two limit cycles can bifurcate from the two-saddle loop in the case. The somewhat surprising answer is "yes", as noticed first in [10]. The bifurcation of the second "alien" limit cycle will be explained in an Appendix. This completes the proof of Proposition 3. □ \Box

### 4.2 The case M 1 = 0 M_{1}=0

In this section we suppose that the Melnikov function M 1 ​ ( t) M_{1}(t) vanishes identically. The first return map has the form ( 3) where

 | M k ( t) = ∫ δ ⁡ ( t) [α + β x + γ x − 1] y d x, k ≥ 2 α, β, γ ∈ ℝ. M_{k}(t)=\int_{\delta(t)}[\alpha+\beta x+\gamma x^{-1}]ydx,\quad k\geq 2\quad\alpha,\beta,\gamma\in\mathbb{R}. |  | (24) |

As we explained, we may suppose that the Bautin ideal is locally principal at λ 0 \lambda_{0} and let ε \varepsilon be the generator. The deformed vector field X λ X_{\lambda} defines a foliation

 | d ​ H − ∑ i = 1 ∞ ε i ​ ω i = 0 dH-\sum_{i=1}^{\infty}\varepsilon^{i}\omega_{i}=0 |  |

with first return map

 | P ε ​ ( h) = h + ε k ​ [M k ​ ( h) + O ⁡ ( ε)], M k ≠ 0. P_{\varepsilon}(h)=h+\varepsilon^{k}[M_{k}(h)+O(\varepsilon)],\quad M_{k}\neq 0. |  |

If ∫ δ ⁡ ( t) ω 1 ≢ 0 \int_{\delta(t)}\omega_{1}\not\equiv 0 then k = 1 k=1 and moreover

 | M 1 ​ ( t) = ∫ δ ⁡ ( t) ω 1. M_{1}(t)=\int_{\delta(t)}\omega_{1}. |  |

If, on the other hand, M 1 = 0 M_{1}=0, then d ​ ω 1 = c ​ y ​ d ​ x ​ d ​ y d\omega_{1}=cydxdy, where c c is a constant (eventually zero). In general, we shall have

 | d ​ ω 1 = ⋯ = d ​ ω d − 1 = 0, d ​ ω d = ( a + b ​ x + c ​ y) ​ d ​ x ​ d ​ y d\omega_{1}=\dots=d\omega_{d-1}=0,\;\;d\omega_{d}=(a+bx+cy)dxdy |  | (25) |

where

 | M d ​ ( t) = ∫ δ ⁡ ( t) ( a + b ​ x + c ​ y) ​ 𝑑 x ​ 𝑑 y. M_{d}(t)=\int_{\delta(t)}(a+bx+cy)dxdy. |  |

The case a 2 + b 2 ≠ 0 a^{2}+b^{2}\neq 0 is completely analogous to the case when the first Melnikov function M 1 M_{1} is not identically zero, and is studied as in Section 4.1. To the end of the section we consider the case a = b = 0 a=b=0, c ≠ 0 c\neq 0, in which case the first non-vanishing Poincaré-Pontryagin function is M k M_{k} with suitable k > d k>d.

###### Proposition 5.

If γ ≠ 0 \gamma\neq 0, then no limit cycles bifurcate from the two-saddle loop Γ \Gamma.

Following the method of the preceding section, we evaluate the number of the zeros of the displacement map

 | d ε + − d ε − = ( P ε − i ​ d) ∘ d ε − = ε k ​ M k ​ ( t) + ε k + 1 ​ M k + 1 ​ ( t) + … d^{+}_{\varepsilon}-d^{-}_{\varepsilon}=(P_{\varepsilon}-id)\circ d^{-}_{\varepsilon}=\varepsilon^{k}M_{k}(t)+\varepsilon^{k+1}M_{k+1}(t)+\dots |  |

in the domain 𝒟 ε \mathcal{D}_{\varepsilon}.

1. 1.

The displacement map, along the circle S R S_{R} is approximated by ε k ​ M k ​ ( t) \varepsilon^{k}M_{k}(t) which has as a leading term ln ⁡ t \ln t as γ ≠ 0 \gamma\neq 0, see Lemma 2. The increase of the argument of ln ⁡ t \ln t, and hence of the displacement map, along the circle S R S_{R} is *close to 0 0 but strictly less than 0 0*.

2. 2.

The imaginary part of the displacement map, along the interval [S + ​ ( ε), S − ​ ( ε)] [S_{+}(\varepsilon),S_{-}(\varepsilon)] equals the imaginary part of d ε − ​ ( t) d^{-}_{\varepsilon}(t). Its zeros equal the number of intersection points of ℋ ε − \mathcal{H}_{\varepsilon}^{-} with the real axes, which amounts to solve h δ − ε ​ ( z) = z h^{\varepsilon}_{\delta_{-}}(z)=z, see ( 22). Zeros of h δ − ε − i ​ d h^{\varepsilon}_{\delta_{-}}-id correspond to complex limit cycles (except the origin S − S_{-}). Their number is the *cyclicity of the saddle point*. We have

 | h δ − ε ​ ( z) = z + ε d ​ M d − ​ ( t) + …, a, b, c ∈ ℝ h^{\varepsilon}_{\delta_{-}}(z)=z+\varepsilon^{d}M^{-}_{d}(t)+\dots,\quad a,b,c\in\mathbb{R} |  |

where

 | M d − ​ ( t) = ∫ δ − ​ ( t) ω d, d ​ ω d = c ​ y ​ 𝑑 x ​ 𝑑 y, c ≠ 0. M_{d}^{-}(t)=\int_{\delta_{-}(t)}\omega_{d},\;\;d\omega_{d}=cydxdy,c\neq 0. |  |

Lemma 2 implies ∫ δ − ​ ( t) y 2 ​ 𝑑 x = ± 2 ​ π ​ i ​ t \int_{\delta_{-}(t)}y^{2}dx=\pm 2\pi it, and hence the cyclicity of the saddle point is zero. We conclude that the imaginary part of the displacement map does not vanish along the interval [S + ​ ( ε), S − ​ ( ε)) [S_{+}(\varepsilon),S_{-}(\varepsilon)).

3. 3.

The number of the zeros of the imaginary part of the displacement map, along the real analytic curve ℋ ε + \mathcal{H}_{\varepsilon}^{+} equals the number of zeros of the imaginary part of d ε − d^{-}_{\varepsilon} along this curve, that is to say the number of intersection points of ℋ ε + \mathcal{H}_{\varepsilon}^{+} with ℋ ε − \mathcal{H}_{\varepsilon}^{-}. According to ( 23) we need the expansion of h δ ± ε ​ ( z) − z h^{\varepsilon}_{\delta_{\pm}}(z)-z. The monodromy of the first return map P ε ​ ( e 2 ​ π ​ i ​ t) − P ε ​ ( t) P_{\varepsilon}(e^{2\pi i}t)-P_{\varepsilon}(t), equals the holonomy h δ − ε ∘ h δ + ε ​ ( z) h_{\delta_{-}}^{\varepsilon}\circ h_{\delta_{+}}^{\varepsilon}(z), where z z is a different chart close to t t, z = t + O ⁡ ( ε) z=t+O(\varepsilon). Therefore, if

 | P ε ( t) = t + ε k ( ln t ∫ δ + ​ ( t) + δ − ​ ( t) [α + β x + γ x − 1] y d x + h. f.) + O ( ε k + 1) P_{\varepsilon}(t)=t+\varepsilon^{k}(\ln t\int_{\delta_{+}(t)+\delta_{-}(t)}[\alpha+\beta x+\gamma x^{-1}]ydx+h.f.)+O(\varepsilon^{k+1}) |  |

then

 | h δ − ε ∘ h δ + ε ​ ( z) = 2 ​ π ​ i ​ ε k ​ ∫ δ + ​ ( t) + δ − ​ ( t) [α + β ​ x + γ ​ x − 1] ​ y ​ 𝑑 x + O ⁡ ( ε k + 1). h^{\varepsilon}_{\delta_{-}}\circ h^{\varepsilon}_{\delta_{+}}(z)=2\pi i\varepsilon^{k}\int_{\delta_{+}(t)+\delta_{-}(t)}[\alpha+\beta x+\gamma x^{-1}]ydx+O(\varepsilon^{k+1}). |  |

The notation O ⁡ ( ε k + 1) O(\varepsilon^{k+1}) has as usual an appropriate meaning. It represents a function which, for a fixed z z or t t, is bounded by a function of the type O ⁡ ( | ε | k + 1) O(|\varepsilon|^{k+1}). Finally, "h.f." stays for a function, holomorphic in t t. As the leading term of P ε ​ ( t) P_{\varepsilon}(t) is ln ⁡ t \ln t multiplied by a non-zero constant, then the above formula shows that the leading term of the holonomy map is a non-zero constant

 | h δ − ε ∘ h δ + ε ​ ( z) = ε k ​ ( c + …) + O ⁡ ( ε k + 1), c ≠ 0. h^{\varepsilon}_{\delta_{-}}\circ h^{\varepsilon}_{\delta_{+}}(z)=\varepsilon^{k}(c+\dots)+O(\varepsilon^{k+1}),\;c\neq 0. |  |

The conclusion is that the imaginary part of the displacement map has no zeros along the real analytic curve ℋ ε + \mathcal{H}_{\varepsilon}^{+}.

Summing up the above information, we conclude that the displacement map has no zeros in the domain 𝒟 ε \mathcal{D}_{\varepsilon}. Proposition 5 is proved. □ \Box

###### Proposition 6.

If γ = 0 \gamma=0, but α ≠ 0 \alpha\neq 0, then at most two limit cycles bifurcate from the two-saddle loop Γ \Gamma.

Proof. The condition α ≠ 0 \alpha\neq 0 is equivalent to the condition d 1 ≠ 0 d_{1}\neq 0 in the expansion of the first non-vanishing Melnikov function

 | M k ​ ( t) = d 0 + d 1 ​ t ​ ln ⁡ t + d 2 ​ t + d 3 ​ t 2 ​ ln ⁡ t + … M_{k}(t)=d_{0}+d_{1}t\ln t+d_{2}t+d_{3}t^{2}\ln t+\dots |  |

1. 1.

The displacement map, along the circle S R S_{R} is approximated by ε k ​ M k ​ ( t) \varepsilon^{k}M_{k}(t) which has as a leading term either a constant, to t ​ ln ⁡ t t\ln t. In both cases the increase of the argument of the displacement map, along the circle S R S_{R} is strictly less than 2 ​ π 2\pi.

2. 2.

The imaginary part of the displacement map, along the interval [S + ​ ( ε), S − ​ ( ε)] [S_{+}(\varepsilon),S_{-}(\varepsilon)] equals the imaginary part of d ε − ​ ( t) d^{-}_{\varepsilon}(t). As in the preceding proposition, we get that the imaginary part of the displacement map does not vanish along the interval [S + ​ ( ε), S − ​ ( ε)) [S_{+}(\varepsilon),S_{-}(\varepsilon)).

3. 3.

The number of the zeros of the imaginary part of the displacement map, along the real analytic curve ℋ ε + \mathcal{H}_{\varepsilon}^{+}, equals the number of intersection points of this curve with ℋ ε − \mathcal{H}_{\varepsilon}^{-}. It is bounded by the cyclicity of

 | d 1 ​ t + d 3 ​ t 2 + … d_{1}t+d_{3}t^{2}+\dots |  |

that is to say by one. This implies the statement of Proposition 6. □ \Box

###### Proposition 7.

If γ = α = 0 \gamma=\alpha=0, but β ≠ 0 \beta\neq 0, then at most three limit cycles bifurcate from the two-saddle loop Γ \Gamma.

The condition α = 0 \alpha=0 but β ≠ 0 \beta\neq 0 implies d 1 = 0 d_{1}=0, d 3 ≠ 0 d_{3}\neq 0, d 0 ≠ 0 d_{0}\neq 0 in the expansion of the first non-vanishing Melnikov function

 | M k ​ ( t) = d 0 + d 1 ​ t ​ ln ⁡ t + d 2 ​ t + d 3 ​ t 2 ​ ln ⁡ t + … M_{k}(t)=d_{0}+d_{1}t\ln t+d_{2}t+d_{3}t^{2}\ln t+\dots |  |

Repeating the preceding arguments, we obtain a bound of three limit cycles (possibly complex). □ \Box

## 5 Global results

Let H ⁡ ( x, y) H(x,y) be a real cubic polynomial, such that X H X_{H} has a non-degenerate two-saddle loop Γ \Gamma as on Figure 1. Denote by Π \Pi the period annulus surrounded by Γ \Gamma, and by Π ¯ = Π ∪ Γ \bar{\Pi}=\Pi\cup\Gamma its closure. Theorem 1 can be generalized as follows

###### Theorem 3.

The cyclicity of the closed period annulus Π ¯ \bar{\Pi} under an arbitrary quadratic deformation, is less then or equal to three.

Let X ε X_{\varepsilon} be a one-parameter family of plane quadratic vector fields, depending analytically on a real parameter ε \varepsilon, and such that X 0 = X H X_{0}=X_{H} is a Hamiltonian vector field having a non-degenerate two-saddle loop Γ \Gamma as above.

###### Theorem 4.

If the first Melnikov function is not identically zero, and

- •

M 1 ​ ( 0) ≠ 0 M_{1}(0)\neq 0, then no limit cycles bifurcate from Γ \Gamma and at most one limit cycle bifurcates from the closed period annulus Π ¯ \bar{\Pi};

- •

M 1 ​ ( 0) = 0 M_{1}(0)=0, then at most two limit cycles bifurcate from the two-saddle loop Γ \Gamma and no limit cycles bifurcate from the open period annulus Π \Pi.

If the first non-vanishing Melnikov function M k M_{k}, k ≥ 2 k\geq 2 is as in ( 24), and

- •

γ ≠ 0 \gamma\neq 0, then no limit cycles bifurcate from Γ \Gamma and at most two limit cycles bifurcate from the closed period annulus Π ¯ \bar{\Pi};

- •

γ = 0 \gamma=0 and M k ​ ( 0) = 0 M_{k}(0)=0, then at most two limit cycles bifurcate from the two-saddle loop Γ \Gamma and no limit cycles bifurcate from the open period annulus Π \Pi;

- •

γ = 0 \gamma=0, α ≠ 0 \alpha\neq 0 and M k ​ ( 0) ≠ 0 M_{k}(0)\neq 0, then no limit cycles bifurcate from Γ \Gamma and at most one limit cycle bifurcates from the closed period annulus Π ¯ \bar{\Pi};

- •

γ = α = 0 \gamma=\alpha=0 and β ≠ 0 \beta\neq 0, then no limit cycles bifurcate from the open period annulus Π \Pi, and at most three limit cycles bifurcate from the two-saddle loop Γ \Gamma.

Let H ⁡ ( x, y) H(x,y) be a real cubic polynomial with four distinct (real or complex) critical points, but only three distinct critical values. Let X H X_{H} be the corresponding quadratic Hamiltonian vector field ( 2).

###### Theorem 5.

There is a neighborhood 𝒰 {\cal U} of X H X_{H} in the space of all quadratic vector fields, such that any X ∈ 𝒰 X\in{\cal U} has at most three limit cycles.

Theorem 5 is the analogue of [12, Theorem 1], [20, Theorem 2], where it is shown that for a cubic Hamiltonian H ⁡ ( x, y) H(x,y) with four distinct critical values, the exact upper bound for the number of the limit cycles of any sufficiently close quadratic system, is two. Let us explain in brief which X H X_{H} Theorem 5 concerns. By using the normal form for cubic Hamiltonians with a center from [20],

 | H ⁡ ( x, y) = x 2 + y 2 2 − x 3 3 + a ​ x ​ y 2 + b 3 ​ y 3, − 1 2 ≤ a ≤ 1, 0 ≤ b ≤ ( 1 − a) ​ 1 + 2 ​ a, H(x,y)=\frac{x^{2}+y^{2}}{2}-\frac{x^{3}}{3}+axy^{2}+\frac{b}{3}y^{3},\;\;-\frac{1}{2}\leq a\leq 1,\;\;0\leq b\leq(1-a)\sqrt{1+2a}, |  |

one can easily verify that the level value corresponding to a critical point ( x 0, y 0) (x_{0},y_{0}) is H ⁡ ( x 0, y 0) = 1 6 ​ ( x 0 2 + y 0 2) H(x_{0},y_{0})=\frac{1}{6}(x_{0}^{2}+y_{0}^{2}). Then, for the generic Hamiltonians (corresponding to internal points ( a, b) (a,b) of the domain of parameters) there are either four distinct critical levels or three distinct critical points in the finite plane and Theorem 5 does not concern them. For the degenerate Hamiltonians (corresponding to points from the boundary of the domain of parameters), there are four distinct critical points with three distinct critical values if and only if ( a, b) ≠ ( − 1 2, 0), ( − 1 3, 0), ( 0, 0), ( 1, 0), ( 1 2, 1 2) (a,b)\neq(-\frac{1}{2},0),(-\frac{1}{3},0),(0,0),(1,0),(\frac{1}{2},\sqrt{\frac{1}{2}}). Therefore, in the normal form ( 6), Theorem 5 concerns all a ∈ ℝ a\in{\mathbb{R}} except a = − 1, 0, 2, 3 a=-1,0,2,3.

Conjecture. The exact upper bound for the number of limit cycles in Theorem 1, Theorem 3 and Theorem 5 is two.

Figure 3: The curves L + L_{+} and L − L_{-}

Proof of Theorems 3, 4, 5. For the saddle-loop cases (that is a ∉ [− 1, 2] a\not\in[-1,2]) in Theorem 5, it is well known that at most two limit cycles can bifurcate from the closed period annulus [16, 5]. Below we are going to apply the results just established to handle the two-saddle loop cases a ∈ ( − 1, 2) a\in(-1,2). The proofs will follow from a careful comparison of the statements in the preceding section and the available results on the cyclicity of open period annuli of quadratic Hamiltonian systems, see [34, 21, 5].

Using the notations of Section 3, denote by Σ + = [a − 3, 0) \Sigma_{+}=[a-3,0) the semi-open interval with respect to t t corresponding to the period annulus surrounding the center C + C_{+} at ( 1, 0) (1,0). When there is a second center C − C_{-} at ( a − 2 a, 0) (\frac{a-2}{a},0) which happens for 0 < a < 2 0<a<2, we shall denote the related interval by Σ − = ( 0, ( a + 1) ​ ( a − 2) 2 a 2] \Sigma_{-}=(0,\frac{(a+1)(a-2)^{2}}{a^{2}}]. Consider the respective Melnikov function(s)

 | M k ​ ( t) = α ​ J 0 ​ ( t) + β ​ J 1 ​ ( t) + γ ​ J − 1 ​ ( t), t ∈ Σ ±. M_{k}(t)=\alpha J_{0}(t)+\beta J_{1}(t)+\gamma J_{-1}(t),\qquad t\in\Sigma_{\pm}. |  |

Next, define the planar curve(s)

 | L ± = { ( ξ ± ( t), η ± ( t)) = ( J 1 ​ ( t) J 0 ​ ( t), J − 1 ​ ( t) J 0 ​ ( t)): t ∈ Σ ± }. L_{\pm}=\left\{(\xi_{\pm}(t),\eta_{\pm}(t))=\left(\frac{J_{1}(t)}{J_{0}(t)},\frac{J_{-1}(t)}{J_{0}(t)}\right):\quad t\in\Sigma_{\pm}\right\}. |  |

The properties of the curves L ± L_{\pm} are well known, see [34], [21] and [5] for the hyperbolic, the parabolic and the elliptic cases. Namely (see Figure 3),

1) ξ + ​ ( t) \xi_{+}(t) is decreasing, η + ​ ( t) \eta_{+}(t) is increasing and L + L_{+} is a convex curve. L + L_{+} begins at point ( 1, 1) (1,1) and has a vertical asymptote ξ = ξ + ​ ( − 0) = c 0 / b 0 \xi=\xi_{+}(-0)=c_{0}/b_{0} as t → − 0 t\to-0.

2) If L − L_{-} exists, then ξ − ​ ( t) \xi_{-}(t) is decreasing, η − ​ ( t) \eta_{-}(t) is increasing and L − L_{-} is a concave curve. L − L_{-} ends at point ( a − 2 a, a a − 2) (\frac{a-2}{a},\frac{a}{a-2}) and has a vertical asymptote ξ = ξ − ​ ( + 0) \xi=\xi_{-}(+0) as t → + 0 t\to+0.

3) The number of limit cycles born from periodic orbits equals the number of the intersections (counted with multiplicities) between the straight line α + β ​ ξ + γ ​ η = 0 \alpha+\beta\xi+\gamma\eta=0 and the curve L + L_{+} (both curves L ± L_{\pm} in the elliptic case).

4) If P ∗ P_{*} is intersection point corresponding to t = t ∗ t=t_{*}, then the related limit cycle approaches the oval H ⁡ ( x, y) = t ∗ H(x,y)=t_{*} as ε → 0 \varepsilon\to 0.

Now, if γ ≠ 0 \gamma\neq 0, then by Proposition 5 above, there are no limit cycles produced by the double loop(s). On the other hand, any line has at most two intersection points with L ± L_{\pm}. Two is the total upper bound of the number of limit cycles produced under the perturbation.

Next, if γ = 0 \gamma=0, then by Proposition 1, a necessary condition for the bifurcation of limit cycles from the double loop(s) is α ​ J 0 ​ ( 0) + β ​ J 1 ​ ( 0) = 0 \alpha J_{0}(0)+\beta J_{1}(0)=0. It is easy to see that limit cycles cannot bifurcate simultaneously from both two-saddle loops existing when a ∈ ( 0, 2) a\in(0,2). Indeed, the system

 | α ​ J 0 ​ ( − 0) + β ​ J 1 ​ ( − 0) = α ​ J 0 ​ ( + 0) + β ​ J 1 ​ ( + 0) = 0 \alpha J_{0}(-0)+\beta J_{1}(-0)=\alpha J_{0}(+0)+\beta J_{1}(+0)=0 |  |

implies α = β = 0 \alpha=\beta=0. This is because the system is equivalent to

 | α + ξ + ​ ( − 0) ​ β = α + ξ − ​ ( + 0) ​ β = 0 ​ and ​ ξ − ​ ( + 0) < 0 < ξ + ​ ( − 0). \alpha+\xi_{+}(-0)\beta=\alpha+\xi_{-}(+0)\beta=0\;\;\mbox{\rm and}\;\;\xi_{-}(+0)<0<\xi_{+}(-0). |  |

Therefore, if γ = 0 \gamma=0 but α ≠ 0 \alpha\neq 0, then by Proposition 6 above, there are at most two limit cycles produced by the double loop(s). On the other hand, any line α + β ​ ξ = 0 \alpha+\beta\xi=0 has at most one intersection point with L ± L_{\pm}. Moreover, if such a point exists, no limit cycles are produced by the double loop(s), according to Proposition 1. Again, two is the total upper bound of the number of limit cycles produced under the perturbation.

If γ = α = 0 \gamma=\alpha=0 but β ≠ 0 \beta\neq 0, then by Proposition 7 above, there are at most three limit cycles produced by the double loop(s). On the other hand, the line ξ = 0 \xi=0 has no intersection points with L ± L_{\pm}. Hence, three is the total upper bound of the number of limit cycles produced under the perturbation. □ \Box

## 6 Appendix : alien limit cycles in quadratic systems

Figure 4: The two-saddle loop Γ u = Γ 1 ∪ Γ 2 ⊂ { H = 0 }. \Gamma_{u}=\Gamma_{1}\cup\Gamma_{2}\subset\{H=0\}.

Consider, using the notations of [26], the perturbed quadratic Hamiltonian system

 | X μ, ε: { x ˙ = H y y ˙ = − H x − ε ​ P X_{\mu,\varepsilon}:\left\{\begin{array}[]{lcl}\dot{x}&=&H_{y}\\ \dot{y}&=&-H_{x}-\varepsilon P\end{array}\right. |  | (26) |

where

 | H = y ⁡ ( x 2 + 1 12 ​ y 2 − 1), P ⁡ ( x, y, μ) = ( 16 + c ​ x − π ​ 3 ​ y) ​ y + μ 1 + μ 2 ​ y, H=y(x^{2}+\frac{1}{12}y^{2}-1),\quad P(x,y,\mu)=(16+cx-\pi\sqrt{3}y)y+\mu_{1}+\mu_{2}y,\;\; |  | (27) |

ε, μ 1, μ 2 \varepsilon,\mu_{1},\mu_{2} are sufficiently small real numbers, and c c is a real constant bigger than 16. Denote the upper two-saddle loop of the non perturbed system ( ε = 0 \varepsilon=0) by Γ u = Γ 1 ∪ Γ 2 \Gamma_{u}=\Gamma_{1}\cup\Gamma_{2}, where Γ 1 \Gamma_{1} is the segment { ( x, y): − 1 ≤ x ≤ 1, y = 0 } \{(x,y):-1\leq x\leq 1,y=0\} and Γ 2 \Gamma_{2} is the half-ellipse { ( x, y): x 2 + 1 12 y 2 = 1, y ≥ 0 } \{(x,y):x^{2}+\frac{1}{12}y^{2}=1,y\geq 0\}, see Fig. 4. Let

 | { γ ⁡ ( h) } h ⊂ { ( x, y) ∈ ℝ 2: H ⁡ ( x, y) = h } \{\gamma(h)\}_{h}\subset\{(x,y)\in{\mathbb{R}}^{2}:H(x,y)=h\} |  |

be the continuous family of ovals, contained in the two-saddle loop Γ u \Gamma_{u}, parameterized by h ∈ ( − 4 / 3, 0) h\in(-4/3,0). The first return map of X μ, ε X_{\mu,\varepsilon} takes the form

 | h ↦ h + ε ​ ∫ γ ⁡ ( h) P ⁡ ( x, y, μ) ​ 𝑑 x + O ⁡ ( ε 2) h\mapsto h+\varepsilon\int_{\gamma(h)}P(x,y,\mu)dx+O(\varepsilon^{2}) |  |

where ∫ γ ⁡ ( h) P ⁡ ( x, y, μ) ​ 𝑑 x \int_{\gamma(h)}P(x,y,\mu)dx is the first Poincaré-Pontryagin function associated to X μ, ε X_{\mu,\varepsilon}. We have

 | ∫ γ ⁡ ( h) P ⁡ ( x, y, μ) ​ 𝑑 x = d 0 ​ ( μ) + d 1 ​ ( μ) ​ h ​ log ⁡ ( h) + O ⁡ ( h) \int_{\gamma(h)}P(x,y,\mu)dx=d_{0}(\mu)+d_{1}(\mu)h\log(h)+O(h) |  |

see ( 14). It is straightforward to check that d ⁡ ( 0) = 0 d(0)=0 and by Proposition 2 then we get d 1 ​ ( 0) ≠ 0 d_{1}(0)\neq 0. It follows that for sufficiently small ‖ μ ‖ \|\mu\|, | h | |h|, h < 0 h<0, the Poincaré-Pontryagin function ∫ γ ⁡ ( h) P ⁡ ( x, y, μ) ​ 𝑑 x \int_{\gamma(h)}P(x,y,\mu)dx has at most one zero. The purpose of this Appendix is to show that the number of the limit cycles, which bifurcate from Γ u \Gamma_{u}, exceeds the number of the zeros of ∫ γ ⁡ ( h) P ⁡ ( x, y, μ) ​ 𝑑 x \int_{\gamma(h)}P(x,y,\mu)dx near h = 0 h=0. The "missing" second limit cycle, which does not correspond to a zero is an "alien" limit cycle.This is a new unexpected phenomenon in the bifurcation theory of vector fields, discovered recently by Caubergh, Dumortier and Roussarie [3, 10]. In contrast to the preceding examples [4, 26, 2, 6]) the system which we consider is quadratic.

###### Proposition 8.

The cyclicity C ​ y ​ c ​ l ​ ( Γ u, X μ, ε) Cycl(\Gamma_{u},X_{\mu,\varepsilon}) of the two-loop Γ u \Gamma_{u} with respect to the deformed vector field X μ, ε X_{\mu,\varepsilon} is two.

Note that, according to Proposition 3, the cyclicity C ​ y ​ c ​ l ​ ( Γ u, X μ, ε) Cycl(\Gamma_{u},X_{\mu,\varepsilon}) is at most two.
Proof of Proposition 8. We shall follow closely [10, section 6.2.]. The traces σ 1, 2 \sigma_{1,2} of the vector field X μ, ε X_{\mu,\varepsilon} at the saddle points determine its "stability".

[image: Refer to caption]

Figure 5: Bifurcation diagram of generic two-parameter deformations of vector fields, containing a two-saddle loop. In the domain E 7 E_{7} the system has two limit cycles.

As the coordinates of the saddle points satisfy

 | x = ± 1 + O ⁡ ( ε), y = O ⁡ ( ε) x=\pm 1+O(\varepsilon),\;\;y=O(\varepsilon) |  |

then for the traces σ 1, 2 \sigma_{1,2} at the saddle points s 1, s 2 s_{1},s_{2} we get

 | σ 1 ​ ( ε, μ) = ( − 16 + c − μ 2) ​ ε + O ⁡ ( ε 2) \sigma_{1}(\varepsilon,\mu)=(-16+c-\mu_{2})\varepsilon+O(\varepsilon^{2}) |  |

 | σ 2 ​ ( ε, μ) = ( − 16 − c − μ 2) ​ ε + O ⁡ ( ε 2) \sigma_{2}(\varepsilon,\mu)=(-16-c-\mu_{2})\varepsilon+O(\varepsilon^{2}) |  |

For small ε \varepsilon and a general perturbation, the connections Γ 1, 2 \Gamma_{1,2} will be broken. The distance between the two branches (stable and unstable separatrix) of the broken connection can be measured on a segment, transverse to Γ 1 \Gamma_{1} or Γ 2 \Gamma_{2}. Let us denote these distances (or shift functions) by b 1, 2 b_{1,2}. It is well known that the shift functions are analytic functions in ε, μ \varepsilon,\mu, and if we use the restriction of H H to the transverse segments as a local parameter h h, then

 | b i ( ε, μ) = ε ∫ Γ i ω μ + O ( ε 2), i = 1, 2. b_{i}(\varepsilon,\mu)=\varepsilon\int_{\Gamma_{i}}\omega_{\mu}+O(\varepsilon^{2}),\quad i=1,2. |  | (28) |

With the notations above we compute

 | ∫ Γ 2 y ​ 𝑑 x = − π ​ 3, ∫ Γ 2 y 2 ​ 𝑑 x = − 16 \int_{\Gamma_{2}}ydx=-\pi\sqrt{3},\quad\int_{\Gamma_{2}}y^{2}dx=-16 |  |

and therefore

 | ∫ Γ 2 ω μ = − 2 ​ μ 1 − π ​ 3 ​ μ 2, ∫ Γ 1 ω μ = 2 ​ μ 1. \int_{\Gamma_{2}}\omega_{\mu}=-2\mu_{1}-\pi\sqrt{3}\mu_{2},\qquad\int_{\Gamma_{1}}\omega_{\mu}=2\mu_{1}. |  |

It is immediately seen that

- •

for every sufficiently small ε ≠ 0 \varepsilon\neq 0 and ‖ μ ‖ \|\mu\|, the traces σ 1, σ 2 \sigma_{1},\sigma_{2} are non-zero and have opposite signs;

- •

for every sufficiently small ε ≠ 0 \varepsilon\neq 0 and ‖ μ ‖ \|\mu\|

 | det ( ∂ b 1 ∂ μ 1 ∂ b 1 ∂ μ 2 ∂ b 2 ∂ μ 1 ∂ b 2 ∂ μ 2) ≠ 0. \det\left(\begin{array}[]{cc}\frac{\partial b_{1}}{\partial\mu_{1}}&\frac{\partial b_{1}}{\partial\mu_{2}}\\ \frac{\partial b_{2}}{\partial\mu_{1}}&\frac{\partial b_{2}}{\partial\mu_{2}}\end{array}\right)\neq 0. |  |

Under these conditions, the bifurcation diagram of limit cycles near the double loop Γ 1 ∪ Γ 2 \Gamma_{1}\cup\Gamma_{2} was computed by Dumortier, Roussarie and Sotomayor [9], see [10, fig. 5]. It follows that the cyclicity of the two loop Γ \Gamma under the quadratic perturbation ( 26) is two. □ \Box
Remark. An alternative proof of Proposition 8 can also be obtained from the classical Roitenberg Theorem, see [1, Theorem 2, fig. 40a], which is illustrated on Fig. 5. Namely, as the deformation ( 26) depends on three parameters, then there is a one-parameter induced deformation

 | μ 1 = μ 1 ​ ( ε) = O ⁡ ( ε), μ 2 = μ 2 ​ ( ε) = O ⁡ ( ε) \mu_{1}=\mu_{1}(\varepsilon)=O(\varepsilon),\quad\mu_{2}=\mu_{2}(\varepsilon)=O(\varepsilon) |  | (29) |

such that the two connections Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2} persist for all sufficiently small ε \varepsilon. This one-parameter deformation is not in an integrable direction at a first order in ε \varepsilon, in the sense that the corresponding first Melnikov function M 1 ​ ( h, μ) | μ = 0 M_{1}(h,\mu)|_{\mu=0} is not identically zero. One easily verifies that this implies the genericity assumptions of [1, Theorem 2]. Thus, making an additional deformation in a direction transversal to the curve ( 29), we get the bifurcation diagram of Roitenberg shown on Fig. 5. This diagram is a two dimensional section { ε = c o n s t } \{\varepsilon=const\} of the three-dimensional diagram [10, fig.5].

Acknowledgments. We are obliged to V. Roitenberg who gave us a permission to reproduce Fig. 5. Part of this work has been done while the second author visited the University of Toulouse. He is very grateful for kind hospitality.

## References

- [1] Dynamical systems. V, volume 5 of Encyclopaedia of Mathematical Sciences. Springer-Verlag, Berlin, 1994. Bifurcation theory and catastrophe theory, A translation of ıt Current problems in mathematics. Fundamental directions. Vol. 5 (Russian), Akad. Nauk SSSR, Vsesoyuz. Inst. Nauchn. i Tekhn. Inform., Moscow, 1986 [ MR0895652 (89a:58088)], Translation by N. D. Kazarinoff.
- [2] Magdalena Caubergh, Freddy Dumortier, and Stijn Luca. Cyclicity of unbounded semi-hyperbolic 2-saddle cycles in polynomial Lienard systems. Discrete Contin. Dyn. Syst., 27(3):963–980, 2010.
- [3] Magdalena Caubergh, Freddy Dumortier, and Robert Roussarie. Alien limit cycles near a Hamiltonian 2-saddle cycle. C. R. Math. Acad. Sci. Paris, 340(8):587–592, 2005.
- [4] Magdalena Caubergh, Freddy Dumortier, and Robert Roussarie. Alien limit cycles in rigid unfoldings of a Hamiltonian 2-saddle cycle. Commun. Pure Appl. Anal., 6(1):1–21, 2007.
- [5] Shui-Nee Chow, Chengzhi Li, and Yingfei Yi. The cyclicity of period annuli of degenerate quadratic Hamiltonian systems with elliptic segment loops. Ergodic Theory Dynam. Systems, 22(2):349–374, 2002.
- [6] B. Coll, F. Dumortier, and R. Prohens. Alien limit cycles in Liénard equations. J. Differential Equations, 254(3):1582–1600, 2013.
- [7] W. A. Coppel. A survey of quadratic systems. J. Differential Equations, 2:293–304, 1966.
- [8] F. Dumortier, R. Roussarie, and C. Rousseau. Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations, 110(1):86–133, 1994.
- [9] F. Dumortier, R. Roussarie, J. Sotomayor, and H. Żołpolhk adek. Bifurcations of planar vector fields, volume 1480 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 1991. Nilpotent singularities and Abelian integrals.
- [10] Freddy Dumortier and Robert Roussarie. Abelian integrals and limit cycles. J. Differential Equations, 227(1):116–165, 2006.
- [11] J. P. Francoise. Successive derivatives of a first return map, application to the study of quadratic vector fields. Ergodic Theory Dynam. Systems, 16(1):87–96, 1996.
- [12] Lubomir Gavrilov. The infinitesimal 16th Hilbert problem in the quadratic case. Invent. Math., 143(3):449–497, 2001.
- [13] Lubomir Gavrilov. Cyclicity of period annuli and principalization of Bautin ideals. Ergodic Theory Dynam. Systems, 28(5):1497–1507, 2008.
- [14] Lubomir Gavrilov. On the number of limit cycles which appear by perturbation of Hamiltonian two-saddle cycles of planar vector fields. Bull. Braz. Math. Soc. (N.S.), 42(1):1–23, 2011.
- [15] Lubomir Gavrilov. On the number of limit cycles which appear by perturbation of two-saddle cycles of planar vector fields, 2011, arXiv:1106.0857 [math.DS].
- [16] Lubomir Gavrilov and Iliya D. Iliev. Second-order analysis in polynomially perturbed reversible quadratic Hamiltonian systems. Ergodic Theory Dynam. Systems, 20(6):1671–1686, 2000.
- [17] Lubomir Gavrilov and Iliya D. Iliev. The displacement map associated to polynomial unfoldings of planar Hamiltonian vector fields. Amer. J. Math., 127(6):1153–1190, 2005.
- [18] Yue He and Chengzhi Li. On the number of limit cycles arising from perturbations of homoclinic loops of quadratic integrable systems. Differential Equations Dynam. Systems, 5(3-4):303–316, 1997. Planar nonlinear dynamical systems (Delft, 1995).
- [19] E. Horozov and I. D. Iliev. On saddle-loop bifurcations of limit cycles in perturbations of quadratic Hamiltonian systems. J. Differential Equations, 113(1):84–105, 1994.
- [20] E. Horozov and I. D. Iliev. On the number of limit cycles in perturbations of quadratic Hamiltonian systems. Proc. London Math. Soc. (3), 69(1):198–224, 1994.
- [21] I. D. Iliev. Higher-order Melnikov functions for degenerate cubic Hamiltonians. Adv. Differential Equations, 1(4):689–708, 1996.
- [22] Iliya D. Iliev. Perturbations of quadratic centers. Bull. Sci. Math., 122(2):107–161, 1998.
- [23] Yu. Ilyashenko. Centennial history of Hilbert’s 16th problem. Bull. Amer. Math. Soc. (N.S.), 39(3):301–354 (electronic), 2002.
- [24] Yulij Ilyashenko and Sergei Yakovenko. Lectures on analytic differential equations, volume 86 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2008.
- [25] Chengzhi Li and Robert Roussarie. The cyclicity of the elliptic segment loops of the reversible quadratic Hamiltonian systems under quadratic perturbations. J. Differential Equations, 205(2):488–520, 2004.
- [26] Stijn Luca, Freddy Dumortier, Magdalena Caubergh, and Robert Roussarie. Detecting alien limit cycles near a Hamiltonian 2-saddle cycle. Discrete Contin. Dyn. Syst., 25(4):1081–1108, 2009.
- [27] G. S. Petrov. The Chebyshev property of elliptic integrals. Funktsional. Anal. i Prilozhen., 22(1):83–84, 1988.
- [28] G. S. Petrov. Nonoscillation of elliptic integrals. Funktsional. Anal. i Prilozhen., 24(3):45–50, 96, 1990.
- [29] I. G. Petrovskiĭ and E. M. Landis. On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx=P(x,\,y)/Q(x,\,y), where P P and Q Q are polynomials of the second degree. In American Mathematical Society Translations, Ser. 2, Vol. 10, pages 177–221. American Mathematical Society, Providence, R.I., 1958.
- [30] R. Roussarie. A note on finite cyclicity property and Hilbert’s 16th problem. In Dynamical systems, Valparaiso 1986, volume 1331 of Lecture Notes in Math., pages 161–168. Springer, Berlin, 1988.
- [31] Robert Roussarie. Bifurcation of planar vector fields and Hilbert’s sixteenth problem, volume 164 of Progress in Mathematics. Birkhäuser Verlag, Basel, 1998.
- [32] Robert Roussarie. Melnikov functions and Bautin ideal. Qual. Theory Dyn. Syst., 2(1):67–78, 2001.
- [33] Song Ling Shi. A concrete example of the existence of four limit cycles for plane quadratic systems. Sci. Sinica, 23(2):153–158, 1980.
- [34] Yulin Zhao and Siming Zhu. Perturbations of the non-generic quadratic Hamiltonian vector fields with hyperbolic segment. Bull. Sci. Math., 125(2):109–138, 2001.
- [35] Henryk Żoładek. The cyclicity of triangles and segments in quadratic systems. J. Differential Equations, 122(1):137–159, 1995.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1306.2339
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1306.2340
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1306.2340
[7]: https://arxiv.org/pdf/1306.2340
[8]: /html/1306.2341
