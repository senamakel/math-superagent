<!-- source: https://arxiv.org/html/1106.0857 | converted from HTML -->

On the number of limit cycles which appear by perturbation of two-saddle cycles of planar vector fields

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1106.0857v3 [math.DS] 12 Dec 2012

# On the number of limit cycles which appear by perturbation of two-saddle cycles of planar vector fields

Lubomir Gavrilov Affiliation: Institut de Mathématiques de Toulouse, UMR 5219 Affiliation: Université de Toulouse, 31062 Toulouse, France

###### Abstract

We prove that the number of limit cycles, which bifurcate from a two-saddle loop of an analytic plane vector field X 0 X_{0}, under an arbitrary finite-parameter analytic deformation X λ X_{\lambda}, λ ∈ ( ℝ N, 0) \lambda\in(\mathbb{R}^{N},0), is uniformly bounded with respect to λ \lambda.

2000 MSC scheme numbers: 34C07, 37G15, 70K05

## 1 Introduction

Consider a finite-parameter analytic family of analytic plane vector fields

 | X λ = P ⁡ ( x, y, λ) ​ ∂ ∂ x + Q ⁡ ( x, y, λ) ​ ∂ ∂ y, λ ∈ ℝ N X_{\lambda}=P(x,y,\lambda)\frac{\partial}{\partial x}+Q(x,y,\lambda)\frac{\partial}{\partial y},\quad\lambda\in\mathbb{R}^{N} |  | (1) |

such that X 0 X_{0} has a limit periodic set Γ \Gamma. The cyclicity of Γ \Gamma is, roughly speaking, the maximal number of limit cycles of X λ X_{\lambda} which tend to Γ \Gamma as λ → 0 \lambda\rightarrow 0. The Roussarie’s finite cyclicity conjecture claims that *every limit periodic set occurring in an analytic finite-parameter family of plane analytic vector fields, has a finite cyclicity*[23]. If true, the conjecture would imply the finitness of the maximal number H ⁡ ( n) H(n) of the limit cycles, which a plane polynomial vector field of degree n n can have. Therefore it plays a fundamental role in all questions related to the second part of the 16th Hilbert problem and its ramifications.

Recall that a polycycle of the vector field X 0 X_{0} is a topological polygon composed of separatrices and singular points. A k k -saddle cycle of X 0 X_{0} (or a hyperbolic k k -graphic) denoted Γ k \Gamma_{k}, is a polycycle composed of k k distinct saddle-type singular points p 1, p 2, …, p k p_{1},p_{2},\dots,p_{k}, p k + 1 = p 1 p_{k+1}=p_{1} and separatrices (heteroclinic orbits) connecting p i p_{i} to p i + 1 p_{i+1} as on fig. 1.

Figure 1: One, two and three-saddle cycles.

k k -saddle cycles, period orbits and weak foci or centers are the simplest limit periodic sets. The finite cyclicity of period orbits and weak foci is well known and follows from the Gabrielov theorem [23, p.68]. The finite cyclicity of one-saddle loops is due to Roussarie [21, 22].

*The purpose of the present paper is to prove the finite cyclicity of a two-saddle cycle, under finite-parameter analytic deformation*, see Theorem 4.

Several special cases of this result were earlier proved, under different genericity assumptionss either on X 0 X_{0} or on the family X λ X_{\lambda}, by Cherkas, Mourtada, El Morsalani, Dumortier, Roussarie, Rousseau, Jebrane, Żoładek,Li, Caubergh, Luca and others [7, 13, 8, 6, 16], see also [23, section 5.4.1] for survey of the results and references up to 1996. The finite cyclicity of a k-saddle cycle (any k), under finite-parameter analytic deformation was recently announced by Mourtada [18].

For *generic families*of vector fields the analitycity can be relaxed. As it is shown by Ilyashenko and Yakovenko [11], Kaloshin [12]*any nontrivial elementary polycycle occurring in a generic k k - parameter family of C ∞ C^{\infty} vector fields has finite cyclicity*.

In contrast to the aforementioned papers we shall not use the asymptotic expansions of the corresponding Dulac maps. Instead of this, we evaluate the number of the limit cycles near Γ 2 \Gamma_{2} in a complex domain, by making use of a suitable version of the argument principle. This approach was initiated by the author in [10], where we studied cyclicity of Hamiltonian two-loops. As it is well known, the limit cycles of planar systems close to Hamiltonian are closely related to the zeros of associated Abelian integrals depending on a parameter (the so called weakened 16th Hilbert problem [1, Arnold, p.313]). Zeros of complete elliptic integrals were successfully studied by topological arguments in a complex domain (the argument principle) after the pioneering work by G. S. Petrov [19, 20], see also Żoładek [25, section 6] for a description of the method. It has been used in a more general context in several papers, e.g. [3, 2], and in [10] the idea has been used to replace Abelian integrals by the true Poincaré return map.

In the present paper we shall find a relation between the fixed points of the Poincaré first return map and the fixed points of holonomies of the separatrices of the saddle points, which correspond to complex limit cycles. To count such fixed points is a question on the zeros of families of *analytic functions*which is easily solved. The main technical tool is Lemma 2 in which we show that the connected components of the zero locus of the imaginary part of a Dulac map are smooth semianalytic curves. This allows to estimate the variation of the argument of the displacement map along the border of an appropriate complex domain, and finally to apply the argument principle in order to evaluate its zeros in the domain.

Note that previously the relation between the monodromy and the Dulac map was used by Roussarie to compute the Bautin ideal associated to the Dulac map [24]. This combined with [21, 22] also implies the finite cyclicity of one-saddle cycles.

The paper is organized as follows. In section 2 we provide the necessary technical background, and prove the main technical Lemma 2. In section 3, we give a new self-contained proof of Roussarie’s theorem about the finite cyclicity of one-saddle cycles. The origin of our method is then explained in section 4 where we give a brief account of a local version of the so called "Petrov trick". The same method is then easily adapted in section 5 to show that the cyclicity of Γ 2 \Gamma_{2} is finite.

## 2 The Dulac map

Consider an analytic family of plane real analytic foliations ℱ λ \mathcal{F}_{\lambda}, λ ∈ ℝ N \lambda\in\mathbb{R}^{N}, having a non-degenerate isolated saddle point. An appropriate translation analytically depending on λ \lambda will place the saddle point at the origin. The foliation ℱ λ \mathcal{F}_{\lambda} has two analytic separatrices, transversally intersecting at the saddle point, and depending analytically on λ \lambda [5, 17]. Therefore a further real bi-analitic change of the variables x, y x,y,analytically depending on λ \lambda, will identify them to the axes { x = 0 } \{x=0\} and { y = 0 } \{y=0\} as on fig. 2, so

 | ℱ λ: x ⁡ ( 1 + …) ​ d ​ y + α ⁡ ( λ) ​ y ​ ( 1 + …) ​ d ​ x, α ⁡ ( 0) > 0. \mathcal{F}_{\lambda}:x(1+...)dy+\alpha(\lambda)y(1+...)dx,\;\alpha(0)>0. |  | (2) |

where the dots replace higher order terms in x, y x,y with coefficients depending on λ \lambda. The number α ⁡ ( λ) \alpha(\lambda) is the hyperbolic ratio of the saddle point. From now on we shall suppose that the foliation ( 2) is analytic and depends analytically in λ \lambda in a neighborhood of the origin in ℝ 2 × ℝ N \mathbb{R}^{2}\times\mathbb{R}^{N}.

(ii) (i)

Figure 2: The Dulac map

For c 1, c 2 ∈ ℝ c_{1},c_{2}\in\mathbb{R} sufficiently small, let σ ⊂ { y = c 1 } \sigma\subset\{y=c_{1}\}, τ ⊂ { x = c 2 } \tau\subset\{x=c_{2}\} be open complex discs centered at ( 0, c 1) (0,c_{1}) and ( c 2, 0) (c_{2},0), parameterized by x x and y y respectively. The (real) Dulac map is the germ of analytic map at x = 0 x=0

 | 𝒟 λ: σ ∩ ℝ + → τ ∩ ℝ +, 𝒟 λ ​ ( 0) = 0 \mathcal{D}_{\lambda}:\sigma\cap\mathbb{R}^{+}\rightarrow\tau\cap\mathbb{R}^{+},\quad\mathcal{D}_{\lambda}(0)=0 |  |

defined as follows: if x ∈ σ ∩ ℝ ∗ + x\in\sigma\cap\mathbb{R^{+}_{*}} then 𝒟 λ ​ ( x) ∈ τ ∩ ℝ ∗ + \mathcal{D}_{\lambda}(x)\in\tau\cap\mathbb{R^{+}_{*}} is the intersection with τ ∩ ℝ ∗ + \tau\cap\mathbb{R^{+}_{*}} of the orbit γ λ ​ ( x) \gamma_{\lambda}(x) of ( 2), passing through x x, see 2 (ii). This geometric definition of 𝒟 λ \mathcal{D}_{\lambda} allows to control to a certain extent its analytic continuation in a complex domain.

### 2.1 Analytic continuation

The Dulac map allows an analytic continuation on some open subset of the universal covering space σ ∙ \sigma_{\bullet} of σ ∖ { 0 } \sigma\setminus\{0\}, depending on λ \lambda. Let us parameterize σ ∙ \sigma_{\bullet} by polar coordinates ρ > 0, φ ∈ ℝ \rho>0,\varphi\in\mathbb{R}, z = ρ ​ exp ⁡ i ​ φ z=\rho\exp{i\varphi}. The following result is well known (e.g. [10, Appendix A])

###### Theorem 1

There exists ε 0 > 0 \varepsilon_{0}>0 and a continuous function

 | ρ: ℝ → ℝ ∗ + φ ↦ ρ ⁡ ( φ) \begin{array}[]{rcl}\rho:\mathbb{R}&\rightarrow&\mathbb{R}^{+}_{*}\\ \varphi&\mapsto&\rho(\varphi)\end{array} |  |

such that the Dulac map allows an analytic continuation in the domain

 | { ( λ, ρ, φ) ∈ ℂ N × σ ∙: | λ | < ε 0, 0 < ρ < ρ ( φ) } \{(\lambda,\rho,\varphi)\in\mathbb{C}^{N}\times\sigma_{\bullet}:|\lambda|<\varepsilon_{0},0<\rho<\rho(\varphi)\} |  | (3) |

The geometric content of Theorem 1 is as follows. Let { γ λ ​ ( z) } z, λ \{\gamma_{\lambda}(z)\}_{z,\lambda} be a continuous family of paths contained in the leaves of ℱ λ \mathcal{F}_{\lambda}, and connecting z ∈ σ z\in\sigma to τ \tau.

For z ∈ σ ∩ ℝ ∗ + z\in\sigma\cap\mathbb{R^{+}_{*}} we suppose that γ λ ​ ( z) \gamma_{\lambda}(z) is the real orbit of ℱ λ \mathcal{F}_{\lambda} contained in the first quadrant x ≥ 0, y ≥ 0 x\geq 0,y\geq 0, and connecting z z to τ \tau, see fig. 2 (ii). The above Theorem claims that this family of orbits allows an extension to a continuous family of paths { γ λ ​ ( z) } z, λ \{\gamma_{\lambda}(z)\}_{z,\lambda}, contained in the leaves of ℱ λ \mathcal{F}_{\lambda}, and connecting z ∈ σ ∙ z\in\sigma_{\bullet} to τ ∙ \tau_{\bullet}. The family is defined for all ( λ, ρ, φ) (\lambda,\rho,\varphi) which belong to the domain ( 3). Each path starts at z z and terminates at a unique point on σ \sigma, denoted 𝒟 λ ​ ( z) \mathcal{D}_{\lambda}(z). Although the paths { γ λ ​ ( z) } z, λ \{\gamma_{\lambda}(z)\}_{z,\lambda} are not unique, their relative homotopy classes are uniquely defined.

### 2.2 Monodromy of the Dulac map and holonomy of separatrices

To the axes { x = 0 }, { y = 0 } \{x=0\},\{y=0\} parameterized by y y and x x, we associate holonomy maps

 | h σ λ: σ → σ, h τ λ: τ → τ h^{\lambda}_{\sigma}:\sigma\rightarrow\sigma,\quad h^{\lambda}_{\tau}:\tau\rightarrow\tau |  |

defined by two closed paths contained in the axes { x = 0 } \{x=0\} and { y = 0 } \{y=0\} and based at ( 0, c 1) (0,c_{1}), ( c 2, 0) (c_{2},0) respectively. We shall make the convention, that each closed path makes one turn around the origin of the axe in which it is contained, in a positive direction (recall that the axes are parameterized by y y and x x respectively). It is easily seen that in the case of a linear foliation of the form

 | x ​ d ​ y + α ​ y ​ d ​ x = 0, α ∈ ℝ + xdy+\alpha\,ydx=0,\quad\alpha\in\mathbb{R}^{+} |  | (4) |

we have

 | 𝒟 α: x ↦ y = c 1 c 2 − α x α, h σ: x ↦ x e − 2 π i / α, h τ: y ↦ y e − 2 ​ π ​ i ​ α. \mathcal{D}_{\alpha}:x\mapsto y=c_{1}c_{2}^{-\alpha}x^{\alpha},\quad h_{\sigma}:x\mapsto xe^{-2\pi i/\alpha},\quad h_{\tau}:y\mapsto ye^{-2\pi i\alpha}. |  | (5) |

In the general case of a nonlinear foliation of the form ( 2) the Dulac map 𝒟 λ \mathcal{D}_{\lambda} is only asymptotic to c 1 ​ c 2 − α ​ x α c_{1}c_{2}^{-\alpha}x^{\alpha}, while the holonomy maps are analytic in x, y, λ x,y,\lambda and

 | h σ λ: x ↦ x e − 2 π i / α + …, h τ λ: y ↦ y e − 2 ​ π ​ i ​ α + …, α = α ( λ). \quad h_{\sigma}^{\lambda}:x\mapsto xe^{-2\pi i/\alpha}+\dots,\quad h_{\tau}^{\lambda}:y\mapsto ye^{-2\pi i\alpha}+\dots,\alpha=\alpha(\lambda). |  | (6) |

The Dulac map 𝒟 λ \mathcal{D}_{\lambda} is a transcendental multi-valued map. For x > 0 x>0 let 𝒟 λ ​ ( e 2 ​ π ​ i ​ x) \mathcal{D}_{\lambda}(e^{2\pi i}x) be the result of the analytic continuation of 𝒟 λ \mathcal{D}_{\lambda} along an arc of radius x x and angle 2 ​ π ​ i 2\pi i. Similarly, for y > 0 y>0 let 𝒟 λ ​ ( e 2 ​ π ​ i ​ y) \mathcal{D}_{\lambda}(e^{2\pi i}y) be the result of the analytic continuation of 𝒟 λ \mathcal{D}_{\lambda} along an arc of radius y y and angle 2 ​ π ​ i 2\pi i.

###### Lemma 1

For every sufficiently small x > 0 x>0, y > 0 y>0, | λ | |\lambda| holds

 | h τ λ ∘ 𝒟 λ ​ ( e 2 ​ π ​ i ​ x) = 𝒟 λ ​ ( x), h σ λ ∘ 𝒟 λ − 1 ​ ( e 2 ​ π ​ i ​ y) = 𝒟 λ − 1 ​ ( y). h^{\lambda}_{\tau}\circ\mathcal{D}_{\lambda}(e^{2\pi i}x)=\mathcal{D}_{\lambda}(x),\quad h^{\lambda}_{\sigma}\circ\mathcal{D}_{\lambda}^{-1}(e^{2\pi i}y)=\mathcal{D}_{\lambda}^{-1}(y). |  |

Proof. Consider, instead of 𝒟 λ \mathcal{D}_{\lambda} the underlying path γ λ \gamma_{\lambda}. The loop γ λ ​ ( e 2 ​ π ​ i ​ x) \gamma_{\lambda}(e^{2\pi i}x) has the same origin as γ λ ​ ( x) \gamma_{\lambda}(x) so they can be composed and the resulting loop γ ~ λ ​ ( y) \tilde{\gamma}_{\lambda}(y) starts at y = 𝒟 λ ​ ( e 2 ​ π ​ i ​ x) ∈ τ y=\mathcal{D}_{\lambda}(e^{2\pi i}x)\in\tau and terminates at 𝒟 λ ​ ( x) ∈ τ \mathcal{D}_{\lambda}(x)\in\tau. In the special linear case ( 4) with α = 1 \alpha=1 the foliation is a fibration, the paths γ λ (.) \gamma_{\lambda}(.) represent relative cycles in the fibers of x ​ y xy, and the path γ ~ λ ​ ( y) \tilde{\gamma}_{\lambda}(y) is closed and represents a vanishing cycle. The claim of Lemma 1 is then the classical Picard-Lefschetz formula. In the general case the result follows "by deformation". Indeed, in the linear case ( 4) with α = 1 \alpha=1 the family of closed paths { γ ~ λ ​ ( y) } y \{\tilde{\gamma}_{\lambda}(y)\}_{y} is defined for all sufficiently small y y, and γ ~ λ ( 0) ⊂ { y = 0 } \tilde{\gamma}_{\lambda}(0)\subset\{y=0\} is a closed path which makes one turn around the origin in the axe { y = 0 } \{y=0\} in a positive direction. Note that the paths γ ~ λ ​ ( 0) \tilde{\gamma}_{\lambda}(0) are bounded away from the origin in ℂ 2 \mathbb{C}^{2}. It follows that γ ~ λ \tilde{\gamma}_{\lambda} defines the holonomy h τ λ h^{\lambda}_{\tau} of the separatrix { y = 0 } \{y=0\}, and this property holds true also for every sufficiently small deformation of ( 4). The homothety ( x, y) → ( ε ​ x, ε ​ y) (x,y)\rightarrow(\varepsilon x,\varepsilon y) transforms ( 2) to a small deformation of ( 4) which completes the proof of the first identity (but see also [15]). The second identity in Lemma 1 is proved in a similar way. □ \Box

### 2.3 The zero locus of the imaginary part of the Dulac map

Consider the universal covering

 | ℂ ∙ → π ℂ ∖ { 0 } \mathbb{C}_{\bullet}\stackrel{{\scriptstyle\pi}}{{\rightarrow}}\mathbb{C}\setminus\{0\} |  | (7) |

and the zero locus ℋ λ ⊂ ℂ ∙ \mathcal{H}_{\lambda}\subset\mathbb{C}_{\bullet} of the imaginary part of the Dulac map 𝒟 λ \mathcal{D}_{\lambda} corresponding to the domain ( 3)

 | ℋ λ = { z = ( ρ, φ) ∈ ℂ ∙: Im 𝒟 λ ( z) = 0, 0 < ρ < ρ ( φ), φ ∈ ℝ }. \mathcal{H}_{\lambda}=\{z=(\rho,\varphi)\in\mathbb{C}_{\bullet}:\operatorname{Im}\mathcal{D}_{\lambda}(z)=0,\,\,0<\rho<\rho(\varphi),\varphi\in\mathbb{R}\}. |  | (8) |

In the case of a linear foliation ( 4) the zero locus is therefore a union of half-lines:

 | ℋ α = { z ∈ ℂ ∙: I m z α = 0 } = ∪ k ∈ ℤ ℋ α, k, ℋ α, k = { ( ρ, φ) ∈ ℂ ∙: φ = k ​ π α }. \mathcal{H}_{\alpha}=\{z\in\mathbb{C}_{\bullet}:Im\,z^{\alpha}=0\}=\cup_{k\in\mathbb{Z}}\mathcal{H}_{\alpha,k},\quad\mathcal{H}_{\alpha,k}=\{(\rho,\varphi)\in\mathbb{C}_{\bullet}:\varphi=\frac{k\pi}{\alpha}\}. |  |

To describe ℋ λ \mathcal{H}_{\lambda} in the case of a general foliation of the form ( 2), with hyperbolic ratio α ⁡ ( λ) > 0 \alpha(\lambda)>0, consider the germs of real analytic sets at the origin in ℝ 2 = ℂ \mathbb{R}^{2}=\mathbb{C}

 | C λ, k = { z ∈ ℂ = ℝ 2: ( h σ λ) k ​ ( z) = z ¯ } C_{\lambda,k}=\{z\in\mathbb{C}=\mathbb{R}^{2}:(h_{\sigma}^{\lambda})^{k}(z)=\bar{z}\} |  | (9) |

where h σ λ h_{\sigma}^{\lambda} is the holonomy map associated to the separatrix { x = 0 } \{x=0\}.

###### Lemma 2

The zero locus ℋ λ ⊂ ℂ ∙ \mathcal{H}_{\lambda}\subset\mathbb{C}_{\bullet} of the imaginary part of the Dulac map in the domain ( 3) is a union of connected components ℋ λ, k \mathcal{H}_{\lambda,k}, indexed by k ∈ ℤ k\in\mathbb{Z}.

- •

Each set C λ, k C_{\lambda,k}, ( 9), is a germ of a real analytic curve of ℝ 2 \mathbb{R}^{2}, which is smooth at the origin and tangent to the line

 | { z = s ​ e i ​ k ​ π / α ⁡ ( λ): s ∈ ( ℝ, 0) } \{z=se^{ik\pi/\alpha(\lambda)}:s\in(\mathbb{R},0)\} |  | (10) |

there.

- •

Each connected component ℋ λ, k \mathcal{H}_{\lambda,k} is projected on the plane ℂ = ℝ 2 \mathbb{C}=\mathbb{R}^{2} under the map π \pi ( 7) to the connected component of C λ, k ∖ { 0 } C_{\lambda,k}\setminus\{0\} tangent to the half-line ( 10), s > 0 s>0, at the origin.

###### Remark 1

For a general bi-holomorphic map h σ λ h_{\sigma}^{\lambda}, vanishing at the origin, the set ( 9) (\ref{clk}) coincides with the origin itself. The above Lemma shows, however, that for the monodromy map h σ λ h_{\sigma}^{\lambda} of a saddle point of a real-analytic plane vector field, the set C λ, k C_{\lambda,k}, ( 9), is a germ of a real analytic curve of ℝ 2 \mathbb{R}^{2}, which is smooth at the origin. The position of the connected components of C λ, k ∖ { 0 } C_{\lambda,k}\setminus\{0\} tangent to the half-lines ( 10), s > 0 s>0 ( 10), s > 0 s>0 is shown on fig. 3.

Figure 3: The zero locus ℋ λ \mathcal{H}_{\lambda} of the imaginary part of the Dulac map, projected on the complex plane ℂ \mathbb{C}.

The above Lemma is the main technical result of the present paper. The analyticity of the zero locus ℋ λ \mathcal{H}_{\lambda} is responsible for the algebraic-like behavior of the Dulac map.
Proof of Lemma 2 Let x ∈ σ ∩ ℝ + x\in\sigma\cap\mathbb{R}^{+} and suppose that for some φ > 0 \varphi>0, 𝒟 λ ​ ( e i ​ φ ​ x) ∈ ℝ \mathcal{D}_{\lambda}(e^{i\varphi}x)\in\mathbb{R}. As the Dulac map is real along σ ∩ ℝ + \sigma\cap\mathbb{R}^{+}, then 𝒟 λ ​ ( e − i ​ φ ​ x) \mathcal{D}_{\lambda}(e^{-i\varphi}x) is complex conjugate to 𝒟 λ ​ ( e i ​ φ ​ x) \mathcal{D}_{\lambda}(e^{i\varphi}x) and hence

 | 𝒟 λ ​ ( e − i ​ φ ​ x) = 𝒟 λ ​ ( e i ​ φ ​ x). \mathcal{D}_{\lambda}(e^{-i\varphi}x)=\mathcal{D}_{\lambda}(e^{i\varphi}x). |  |

If the point e − i ​ φ ​ x e^{-i\varphi}x is seen as the inverse image of 𝒟 λ ​ ( e − i ​ φ ​ x) \mathcal{D}_{\lambda}(e^{-i\varphi}x) with respect to the Dulac map 𝒟 λ − 1 \mathcal{D}_{\lambda}^{-1}, then the point e i ​ φ ​ x e^{i\varphi}x is the result of the analytic continuation of the map 𝒟 λ − 1 \mathcal{D}_{\lambda}^{-1} along a suitable closed path of τ \tau, starting and terminating at 𝒟 λ ​ ( e − i ​ φ ​ x) \mathcal{D}_{\lambda}(e^{-i\varphi}x). If we put

 | y = 𝒟 λ ​ ( e − i ​ φ ​ x), e − i ​ φ ​ x = 𝒟 λ − 1 ​ ( y) y=\mathcal{D}_{\lambda}(e^{-i\varphi}x),\quad e^{-i\varphi}x=\mathcal{D}_{\lambda}^{-1}(y) |  |

then e ± i ​ φ ​ x e^{\pm i\varphi}x are two values of the multivalued map 𝒟 λ − 1 ​ ( y) \mathcal{D}_{\lambda}^{-1}(y) and hence, by Lemma 1, they differ by a power of the monodromy h σ λ h_{\sigma}^{\lambda}

 | ( h σ λ) k ​ ( e i ​ φ ​ x) = e − i ​ φ ​ x (h_{\sigma}^{\lambda})^{k}(e^{i\varphi}x)=e^{-i\varphi}x |  |

or equivalently

 | ( h σ λ) k ​ ( z) = z ¯, z = e i ​ φ ​ x, for some ​ k ∈ ℤ. (h_{\sigma}^{\lambda})^{k}(z)=\bar{z},\quad z=e^{i\varphi}x,\mbox{ for some }k\in\mathbb{Z}. |  |

Clearly every such relation will correspond to a connected component ℋ λ, k \mathcal{H}_{\lambda,k} of ℋ λ \mathcal{H}_{\lambda}. As ℋ λ, k \mathcal{H}_{\lambda,k} is an analytic set of real dimension one, then C λ, k C_{\lambda,k} is an analytic set of dimension one too. It can be defined therefore by each of the following equivalent relations

 | C λ, k ⊂ { z ∈ ℂ = ℝ 2: Re ⁡ [( h σ λ) k ​ ( z)] = Re ⁡ ( z ¯) } C_{\lambda,k}\subset\{z\in\mathbb{C}=\mathbb{R}^{2}:\operatorname{Re}[(h_{\sigma}^{\lambda})^{k}(z)]=\operatorname{Re}(\bar{z})\} |  |

or

 | C λ, k ⊂ { z ∈ ℂ = ℝ 2: Im ⁡ [( h σ λ) k ​ ( z)] = Im ⁡ ( z ¯) }. C_{\lambda,k}\subset\{z\in\mathbb{C}=\mathbb{R}^{2}:\operatorname{Im}[(h_{\sigma}^{\lambda})^{k}(z)]=\operatorname{Im}(\bar{z})\}. |  |

As ∂ ∂ z ¯ ​ [( h σ λ) k ​ ( z) − z ¯] = − 1 \frac{\partial}{\partial\bar{z}}[(h_{\sigma}^{\lambda})^{k}(z)-\bar{z}]=-1, then the linear part of the complex-analytic function

 | ℝ 2 \displaystyle\mathbb{R}^{2} | → \displaystyle\rightarrow | ℂ \displaystyle\mathbb{C} |  |

 | ( z, z ¯) \displaystyle(z,\bar{z}) | ↦ \displaystyle\mapsto | ( h σ λ) k ​ ( z) − z ¯ \displaystyle(h_{\sigma}^{\lambda})^{k}(z)-\bar{z} |  |

can not be identically zero, and therefore C λ, k ⊂ ℝ 2 C_{\lambda,k}\subset\mathbb{R}^{2} is a real analytic curve, smooth at the origin. It follows from ( 6) that the projection of ℋ λ, k \mathcal{H}_{\lambda,k} under π \pi on the plane ℂ = ℝ 2 \mathbb{C}=\mathbb{R}^{2} is tangent to the half-line ( 10), s > 0 s>0 at the origin. □ \Box

### 2.4 The argument principle

Let 𝐃 ⊂ ℂ \mathbf{D}\subset\mathbb{C} be a relatively compact domain, with piece-wise smooth boundary, and ψ: 𝐃 → ℂ \psi:\mathbf{D}\rightarrow\mathbb{C} an analytic function which allows a continuation to the closure 𝐃 ¯ \overline{\mathbf{D}}. Denote by Z 𝐃 ​ ( ψ) Z_{\mathbf{D}}(\psi) the number of the zeros of ψ \psi in 𝐃 \mathbf{D}, counted with multiplicity. If we assume that ψ \psi does not vanish along the border ∂ 𝐃 \mathbf{\partial D}, then the increment of the argument V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)) Var_{\mathbf{\partial D}}(\arg(\psi)) of ψ \psi along ∂ 𝐃 \partial\mathbf{D} oriented counter-clockwise is well defined. V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)) Var_{\mathbf{\partial D}}(\arg(\psi)) equals the winding number of the curve ψ ⁡ ( ∂ 𝐃) ⊂ ℂ \psi(\partial\mathbf{D})\subset\mathbb{C} about the origin and the classical argument principle states that

 | 2 ​ π ​ Z 𝐃 ​ ( ψ) = V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)). 2\pi Z_{\mathbf{D}}(\psi)=Var_{\mathbf{\partial D}}(\arg(\psi)). |  | (11) |

More generally, if ψ \psi has zeros on ∂ 𝐃 \mathbf{\partial D}, isolated or not, the variation of the argument V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)) Var_{\mathbf{\partial D}}(\arg(\psi)) might be not well defined.

###### Definition 1

We say that z ∈ ∂ 𝐃 z\in\mathbf{\partial D} is a regular zero of ψ \psi if ψ ⁡ ( z) = 0 \psi(z)=0, and ψ \psi allows an analytic continuation in a neighborhood of z z in ℂ \mathbb{C}.

If we assume that ψ \psi has only regular zeros in 𝐃 ¯ \overline{\mathbf{D}}, then V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)) Var_{\mathbf{\partial D}}(\arg(\psi)) is well defined as a sum of the increments of the argument of ψ | ∂ 𝐃 \psi|_{\mathbf{\partial D}} between consecutive zeros of ψ \psi. Indeed, the increments are finite, because the border ∂ D \partial{D} is piece-wise smooth. The argument principle can be reformulated as follows

###### Proposition 1

Let 𝐃 ⊂ ℂ \mathbf{D}\subset\mathbb{C} be a relatively compact domain with piece-wise smooth boundary. If ψ: 𝐃 ¯ → ℂ \psi:\overline{\mathbf{D}}\rightarrow\mathbb{C} is a continuous function, analytic in 𝐃 \mathbf{D}, and having only regular zeros in 𝐃 ¯ \overline{\mathbf{D}}, then

 | 2 ​ π ​ Z 𝐃 ​ ( ψ) ≤ V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( ψ)) ≤ 2 ​ π ​ Z 𝐃 ​ ( ψ) + 2 ​ π ​ Z ∂ 𝐃 ​ ( ψ) 2\pi Z_{\mathbf{D}}(\psi)\leq Var_{\mathbf{\partial D}}(\arg(\psi))\leq 2\pi Z_{\mathbf{D}}(\psi)+2\pi Z_{\mathbf{\partial D}}(\psi) |  | (12) |

Proof. There always exists a polynomial P P, such that ψ / P \psi/P has no zeros in 𝐃 ¯ \overline{\mathbf{D}}, so we need to verify ( 12) for polynomials only. The set 𝐃 \mathbf{D} is open, connected and oriented, with piece-wise smooth boundary, which therefore has no self-intersections and has an induced orientation. The inequality

 | 0 ≤ V ​ a ​ r ∂ 𝐃 ​ ( arg ⁡ ( z)) ≤ 2 ​ π 0\leq Var_{\mathbf{\partial D}}(\arg(z))\leq 2\pi |  |

allows to "remove" the zeros along ∂ 𝐃 \mathbf{\partial D} and hence formula ( 11) implies ( 12). □ \Box

In the present paper the first inequality in ( 12) will be used to bound the number of the zeros Z 𝐃 (.) Z_{\mathbf{D}}(.). For this we shall need estimates on the variation of the argument V a r 𝐥 ( arg (.)) Var_{\mathbf{l}}(\arg(.)) along any compact segment l l of a curve. More precisely, let l ⊂ ℝ 2 = ℂ l\subset\mathbb{R}^{2}=\mathbb{C} be a compact segment of a smooth real analytic curve. Let U ⊂ ℂ U\subset\mathbb{C} be an open set containing l l and ψ λ ​ ( z) \psi_{\lambda}(z), λ ∈ ( ℂ N, 0) \lambda\in(\mathbb{C}^{N},0), be a germ of a family of complex-analytic functions in U U at λ = 0 \lambda=0. For every fixed λ \lambda such that the function ψ λ \psi_{\lambda} is not identically zero, the variation of its argument

 | | V a r l ( arg ( ψ λ) | |Var_{l}(\arg(\psi_{\lambda})| |  |

is well defined.

###### Theorem 2

Let l l be a compact segment of a real analytic curve and let { ψ λ } λ \{\psi_{\lambda}\}_{\lambda} be a family of functions analytic in a neighborhood of l l, and depending analytically in λ \lambda. There exists ε 0 > 0 \varepsilon_{0}>0, such that

 | sup | λ | < ε 0, ψ λ ≠ 0 | V ​ a ​ r l ​ ( arg ⁡ ( ψ λ) | < ∞ CLOSE. \sup_{|\lambda|<\varepsilon_{0},\psi_{\lambda}\neq 0}|Var_{l}(\arg(\psi_{\lambda})|<\infty. |  |

The above result follows from the following theorem due to Gabrielov [14, 9]

###### Theorem 3

Let M, N M,N be real analytic varieties and consider the canonical projection π: M × N → N \pi:M\times N\rightarrow N. For every relatively compact semianalytic set E ⊂ M × N E\subset M\times N, the number of the connected components of the pre-images π − 1 ​ ( n) \pi^{-1}(n) is bounded from above uniformly over n ∈ N n\in N.

Proof of Theorem 2. The number of the isolated zeros of ψ λ \psi_{\lambda} along l l counted with multiplicity is uniformly bounded in λ \lambda at λ = 0 \lambda=0 (Françoise-Yomdin Theorem [14]). On an interval between two zeros of ψ λ (.) \psi_{\lambda}(.) the variation of the argument divided by 2 ​ π 2\pi is bounded by the number of the zeros of the imaginary part of ψ λ \psi_{\lambda} divided by two, plus the sum of the multiplicities of the zeros of ψ λ \psi_{\lambda} at the end of the interval. The imaginary part of ψ λ \psi_{\lambda} is a real analytic function in U ⊂ ℝ 2 U\subset\mathbb{R}^{2} and the Gabrielov Theorem implies that the number of the connected components of { I m ( ψ λ) = 0 } ∩ l \{Im(\psi_{\lambda})=0\}\cap l is uniformly bounded in λ \lambda at λ = 0 \lambda=0. □ \Box

## 3 Cyclicity of one-saddle cycles

Figure 4: The Dulac map 𝒟 λ ​ ( z) \mathcal{D}_{\lambda}(z) and the transport map 𝒯 λ ​ ( z) \mathcal{T}_{\lambda}(z).

Let X λ X_{\lambda}, λ ∈ ( ℝ N, 0) \lambda\in(\mathbb{R}^{N},0) be a germ of an analytic family of analytic plane vector fields, such that X 0 X_{0} has a one-saddle cycle (homoclinic saddle loop) Γ 1 \Gamma_{1}. The first-return map associated to Γ 1 \Gamma_{1} is a composition of a Dulac map 𝒟 λ ​ ( z): σ → τ \mathcal{D}_{\lambda}(z):\sigma\rightarrow\tau and a transport map 𝒯 λ ​ ( z) \mathcal{T}_{\lambda}(z), see fig. 4. We assume that the Dulac map is in a normal form as in section 2.1. The limit cycles of X λ X_{\lambda} near Γ 1 \Gamma_{1} correspond to the zeros of the displacement map

 | ψ λ ​ ( z) = 𝒟 λ ​ ( z) − 𝒯 λ ​ ( z) \psi_{\lambda}(z)=\mathcal{D}_{\lambda}(z)-\mathcal{T}_{\lambda}(z) |  |

near z = 0 z=0. An appropriate choice of the local coordinates on the croos-sections σ \sigma and τ \tau brings the transport map to the form 𝒯 λ ​ ( z) ≡ z \mathcal{T}_{\lambda}(z)\equiv z. Alternatively, we could choose simply σ = τ \sigma=\tau (without supposing that the Dulac map is in the normal form of section 2.1). We shall bound the number of the zeros of ψ λ \psi_{\lambda} in the domain 𝐃 R ⊂ ℂ ∙ \mathbf{D}_{R}\subset\mathbb{C}_{\bullet} delimited by the circle { ρ = R } \{\rho=R\}, and the connected components ℋ λ, 1 \mathcal{H}_{\lambda,1} and ℋ λ, − 1 \mathcal{H}_{\lambda,-1} of the zero locus of the imaginary part of the Dulac map, as it is shown on fig. 5.

Figure 5: Examples of domains 𝐃 R ⊂ ℂ ∙ \mathbf{D}_{R}\subset\mathbb{C}_{\bullet}, projected on the complex plane ℂ \mathbb{C} under π \pi ( 7).

We shall suppose that R > 0 R>0 is so small, that ψ λ (.) \psi_{\lambda}(.) is analytic in 𝐃 R \mathbf{D}_{R} for all λ ∈ ℝ N \lambda\in\mathbb{R}^{N}, such that | λ | ≤ ε 0 |\lambda|\leq\varepsilon_{0} (Theorem 1) and it is analytic even on the closure of 𝐃 R \mathbf{D}_{R} except of course at z = 0 z=0, where ψ λ (.) \psi_{\lambda}(.) is only continuous. Indeed,

 | lim z → 0, z ∈ 𝐃 R 𝒟 λ ​ ( z) = 0 \lim_{z\rightarrow 0,z\in\mathbf{D}_{R}}\mathcal{D}_{\lambda}(z)=0 |  |

while 𝒯 λ ​ ( z) \mathcal{T}_{\lambda}(z) is holomorphic at z = 0 z=0, so

 | lim z → 0, z ∈ 𝐃 R ψ λ ​ ( z) = c ⁡ ( λ) \lim_{z\rightarrow 0,z\in\mathbf{D}_{R}}\psi_{\lambda}(z)=c(\lambda) |  |

where c ⁡ ( λ) c(\lambda) is analytic and c ⁡ ( 0) = 0 c(0)=0. If the family of functions ψ λ \psi_{\lambda} is sufficiently general, then c ⁡ ( λ) ≢ 0 c(\lambda)\not\equiv 0, and in the case when c ⁡ ( λ) ≡ 0 c(\lambda)\equiv 0 we may replace ψ λ \psi_{\lambda} by the new family ψ λ + λ N + 1 \psi_{\lambda}+\lambda_{N+1}, λ N + 1 ∈ ℝ \lambda_{N+1}\in\mathbb{R}, for which the limit at z = 0 z=0 is the parameter λ N + 1 \lambda_{N+1}. After this preparation, we may prove the finite cyclicity of the homoclinic loop Γ 1 \Gamma_{1}. For this we apply Proposition 1 (the argument principle) to the family of functions ψ λ \psi_{\lambda} in the domain 𝐃 R \mathbf{D}_{R}. In the course of the computation, it will be supposed that R > 0 R>0 is sufficiently small, ε 0 \varepsilon_{0} is sufficiently small with respect to R R, and λ \lambda is such that | λ | < ε 0 |\lambda|<\varepsilon_{0}. We may encode this choice of the parameters by the "physical" notation

 | 0 < | λ | < ε 0 << R << 1. 0<|\lambda|<\varepsilon_{0}<<R<<1. |  | (13) |

The hyperbolic ratio of the saddle point will be not bigger than one only in a suitable semi-analytic set in the parameter space, and will be bigger than one in another (complementary) semi-analytic set. After eventual exchanging of σ \sigma and τ \tau, it will be also supposed that the hyperbolic ratio of the saddle point is not bigger than one for all parameter values.

Along the circle { z: | z | = R } \{z:|z|=R\} with angle close or strictly less than 2 ​ π 2\pi the variation of the argument of ψ λ \psi_{\lambda} is uniformly bounded in λ \lambda (Theorem 2).

Along the curve C λ, 1 C_{\lambda,1} the imaginary part of ψ λ \psi_{\lambda} equals the imaginary part of the transport map − 𝒯 λ ​ ( z) = − z -\mathcal{T}_{\lambda}(z)=-z. Therefore the zeros of Im ⁡ ( ψ λ) \operatorname{Im}(\psi_{\lambda}) along C λ, 1 C_{\lambda,1} are exactly the intersection points of C λ, 1 C_{\lambda,1} and the segment ( − R, 0) (-R,0). According to Lemma 2 we have

 | C λ, 1 ∩ ℝ = { x ∈ ℝ: h σ λ ​ ( x) = x } = C λ, − 1 ∩ ℝ. C_{\lambda,1}\cap\mathbb{R}=\{x\in\mathbb{R}:h_{\sigma}^{\lambda}(x)=x\}=C_{\lambda,-1}\cap\mathbb{R}. |  | (14) |

As h σ λ ​ ( x) h_{\sigma}^{\lambda}(x) is an analytic family of analytic functions, then by Gabrielov’s theorem, the number of such fixed points is uniformly bounded in λ \lambda on [− R, 0] [-R,0]. To conclude, we have only to check that the family { ψ λ } λ \{\psi_{\lambda}\}_{\lambda} has regular zeros along the border of the domain 𝐃 R \mathbf{D}_{R}. This is indeed the case, when c ⁡ ( λ) ≠ 0 c(\lambda)\neq 0, as ψ λ ​ ( 0) = c ​ ( λ) \psi_{\lambda}(0)=c(\lambda). We conclude that the number of isolated zeros of the family of functions

 | { ψ λ: c ( λ) ≠ 0, | λ | ≤ ε 0 } \{\psi_{\lambda}:c(\lambda)\neq 0,|\lambda|\leq\varepsilon_{0}\} |  |

in the domain 𝐃 R \mathbf{D}_{R} is uniformly bounded by some integer, say C C. Finally, note that the condition c ⁡ ( λ) ≠ 0 c(\lambda)\neq 0 can be removed. Indeed, if for some λ 0 \lambda_{0}, | λ 0 | ≤ ε 0 |\lambda_{0}|\leq\varepsilon_{0}, c ⁡ ( λ) = 0 c(\lambda)=0, the function ψ λ 0 \psi_{\lambda_{0}} has at least C + 1 C+1 zeros in 𝐃 R \mathbf{D}_{R}, then it has at least C + 1 C+1 zeros in 𝐃 R \mathbf{D}_{R} in a sufficiently small neighborhood of λ 0 \lambda_{0}, in contradiction with the preceding estimate.

To resume, we proved the following classical result
Theorem (Roussarie [21, 22, 24])*Every homoclinic saddle loop (a one-saddle cycle) occurring in an analytic finite-parameter family of plane analytic vector fields, may generate no more than a finite number of limit cycles within the family.*

Let us note that our method, exactly as the Roussarie’s Theorem allows to compute more precisely the cyclicity of Γ 1 \Gamma_{1}. We shall not enter into details here. Just to illustrate this, note that if the hyperbolic ratio α ⁡ ( 0) \alpha(0) is strictly bigger than one, then the overall increase of the argument of the displacement map along the border of 𝐃 R \mathbf{D}_{R} is strictly less than 2 ​ π 2\pi (this computation is omitted) and the cyclicity of Γ 1 \Gamma_{1} is zero.

## 4 The Petrov trick

The content of this section is not necessary for the proof of our main result Theorem 4, but it aims to shed some light on the origin of the method, used to bound the limit cycles near the saddle loop in the preceding section.

With the same notations as in section 3, consider the analytic family of analytic vector fields

 | X λ, λ = ( λ 1, …, λ N) ∈ ( ℝ N, 0) X_{\lambda},\;\lambda=(\lambda_{1},\dots,\lambda_{N})\in(\mathbb{R}^{N},0) |  |

defining a holomorphic foliation ℱ λ \mathcal{F}_{\lambda} of the form

 | ℱ λ = { d H + λ 1 ω λ = 0 }, ω 0 ≠ 0 \mathcal{F}_{\lambda}=\{dH+\lambda_{1}\omega_{\lambda}=0\},\omega_{0}\neq 0 |  |

where H H is a function and ω λ \omega_{\lambda} is an analytic family of differential one-forms, both analytic in a neighborhood of the saddle loop Γ 1 \Gamma_{1}. For definiteness, we put the saddle point at the origin in ℝ 2 \mathbb{R}^{2}, so d ​ H ​ ( 0) = 0 dH(0)=0. We shall further suppose that the saddle loop Γ 1 \Gamma_{1} is contained in the level set { H ( x, y) = 0 } \{H(x,y)=0\}, and the interior of Γ 1 \Gamma_{1} is filled up by a continuous family of periodic orbits γ 0 ( h) ⊂ { H ( x, y) = h } \gamma_{0}(h)\subset\{H(x,y)=h\}, parameterized by h > 0 h>0, where h = H ⁡ ( x, y) | σ h=H(x,y)|_{\sigma} is the restriction of H H on the cross-section σ \sigma. The displacement map is approximated by the usual Poincaré-Pontryagin formula as follows

 | ψ λ ​ ( h) = λ 1 ​ ∫ γ 0 ​ ( h) ω λ + o ⁡ ( λ 1), \psi_{\lambda}(h)=\lambda_{1}\int_{\gamma_{0}(h)}\omega_{\lambda}+o(\lambda_{1}), |  | (15) |

where o ⁡ ( λ 1) / λ 1 o(\lambda_{1})/\lambda_{1} tends to zero as λ \lambda tends to zero, uniformly in h h in every compact interval in which the displacement map is defined. The zeros of ψ λ (.) \psi_{\lambda}(.) correspond to limit cycles and, at least far from Γ 1 ⊂ { H ( x, y) = 0 } \Gamma_{1}\subset\{H(x,y)=0\}, they are approximated there by the zeros of the complete Abelian integral

 | h ↦ I λ ​ ( h) = ∫ γ 0 ​ ( h) ω λ, h ≥ 0. h\mapsto I_{\lambda}(h)=\int_{\gamma_{0}(h)}\omega_{\lambda},\;\;h\geq 0. |  |

We make the assumption (actually justified by the Roussarie’s theorem [21]), that this is so also in a neighborhood of h = 0 h\penalty\ =\penalty\ 0 (corresponding to limit cycles close to the saddle loop Γ 1 \Gamma_{1}). Thus, it makes a sense to prove the finiteness of the maximal number of the zeros of the Abelian integral I λ ​ ( h) I_{\lambda}(h), which tend to h = 0 h=0 as λ \lambda tends to the origin in the parameter space. This follows of course from a well known general result of Varchenko and Khovansky. We shall use, however, a different idea due to G.S. Petrov [20], who showed that the analogous global problem for complete elliptic integrals of second kind is of algebraic nature. This observation has been used in several papers by Petrov to evaluate the precise number of zeros of complete elliptic integrals, and hence of limit cycles of perturbed Hamiltonian vector fields, see for instance Żoładek [25, section 6]. We are ready to describe the local version of the Petrov method.

Consider the sector

 | S R = { z = ρ e i ​ φ ∈ ℂ: 0 < ρ < R, 0 < φ < 2 π }. S_{R}=\{z=\rho e^{i\varphi}\in\mathbb{C}:0<\rho<R,\;0<\varphi<2\pi\}. |  |

For a fixed sufficiently small R > 0 R>0 and all sufficiently small ‖ λ ‖ \|\lambda\| the Abelian integral I λ ​ ( z) I_{\lambda}(z) allows an analytic continuation in S R S_{R}. To bound the number of its zeros on S R S_{R} (and hence on ( 0, R) (0,R)) we apply the argument principle to the domain S R S_{R}. Along the circle { ρ = R } \{\rho=R\} the increase of the argument of I λ I_{\lambda} is bounded uniformly in λ \lambda (due to Gabrielov’s theorem). Along the segment [− R, 0] [-R,0] the Abelian integral allows two analytic continuations I λ ± ​ ( h) I_{\lambda}^{\pm}(h). As I λ (.) I_{\lambda}(.) is real-analytic on ( 0, R) (0,R) then

 | I λ + ​ ( h) = I λ − ​ ( h) ¯, h ∈ ( − R, 0) I_{\lambda}^{+}(h)=\overline{I_{\lambda}^{-}(h)},\;h\in(-R,0) |  |

and by the Picard-Lefschetz formula

 | 2 ​ − 1 ​ Im ⁡ I λ + ​ ( h) = I λ + ​ ( h) − I λ − ​ ( h) = ∫ δ ⁡ ( h) ω λ, h ∈ ( − R, 0) 2\sqrt{-1}\operatorname{Im}I_{\lambda}^{+}(h)=I_{\lambda}^{+}(h)-I_{\lambda}^{-}(h)=\int_{\delta(h)}\omega_{\lambda},\;h\in(-R,0) |  | (16) |

where δ ( h) ⊂ { H ( x, y) = h } \delta(h)\subset\{H(x,y)=h\} is a continuous family of cycles, vanishing at the origin as h h tends to zero.

The imaginary part of I λ ​ ( h) I_{\lambda}(h) on ( − R, 0) (-R,0) is therefore an analytic function, and by Gabrielov’s theorem again, its zeros are uniformly bounded in λ \lambda on the closed interval [− R, 0] [-R,0]. This implies that the increase of the argument of I λ ​ ( h) I_{\lambda}(h) on ( − R, 0) (-R,0) is also uniformly bounded in λ \lambda which combined to the argument principle shows the finiteness of the maximal number of zeros

The proof of the finite cyclicity of the one-saddle loop from the preceding section, may be seen as a generalization of the Petrov method. Indeed, the Picard-Lefschetz formula corresponds to the claim of Lemma 1, and by Lemma 2 the zeros the analytic Abelian integral ( 16) correspond to the fixed points (complex limit cycles) of the holonomy map h σ λ h_{\sigma}^{\lambda} of the separatrix. As it is well known, the holonomy map of a separatrix is analytic, which implies the finite cyclicity of the saddle loop Γ 1 \Gamma_{1}.

## 5 Cyclicity of two-saddle cycles

The main result of the paper is the following

###### Theorem 4

Every heteroclinic saddle loop (a two-saddle cycle) occurring in an analytic finite-parameter family of plane analytic vector fields, may generate no more than a finite number of limit cycles within the family.

Using the notations used in the preceding sections, suppose that the vector field X 0 X_{0} has a two-saddle loop Γ 2 \Gamma_{2}. Consider the Dulac maps

 | 𝒟 i λ: σ → τ, i = 1, 2 \mathcal{D}^{i}_{\lambda}:\sigma\rightarrow\tau,\;i=1,2 |  |

associated to the corresponding foliation, as on fig. 6.

Figure 6: The Dulac maps 𝒟 λ 1 \mathcal{D}^{1}_{\lambda} and 𝒟 λ 2 \mathcal{D}^{2}_{\lambda}

Each map 𝒟 λ i \mathcal{D}^{i}_{\lambda} is a composition of a "local" Dulac map (as in section 2) and two real-analytic transport maps. From this it follows that Lemma 2 applies to 𝒟 λ i \mathcal{D}^{i}_{\lambda}, i = 1, 2 i=1,2, too. From now on we choose a real-analytic local variable z z on the cross-section σ \sigma thus identifying σ \sigma to an open disc centered at 0 ∈ ℂ 0\in\mathbb{C}. We shall also suppose that 0 = σ ∩ Γ 2 0=\sigma\cap\Gamma_{2}. The functions 𝒟 λ i ​ ( z) \mathcal{D}_{\lambda}^{i}(z), i = 1, 2 i=1,2 are multivalued on the cross-section σ \sigma and have critical points at s i ​ ( λ) ∈ ℝ s_{i}(\lambda)\in\mathbb{R}, s i ​ ( 0) = 0 s_{i}(0)=0, respectively. The functions s i s_{i} are real-analytic. The limit cycles of X λ X_{\lambda} near Γ 2 \Gamma_{2} correspond to the zeros of the displacement map

 | ψ λ ​ ( z) = 𝒟 λ 1 ​ ( z) − 𝒟 λ 2 ​ ( z) \psi_{\lambda}(z)=\mathcal{D}_{\lambda}^{1}(z)-\mathcal{D}_{\lambda}^{2}(z) |  |

near z = 0 z=0. Let α i ​ ( λ) > 0 \alpha_{i}(\lambda)>0, i = 1, 2 i=1,2 be the hyperbolic ratios of the saddles. We shall suppose, upon exchanging eventually the roles of σ \sigma and τ \tau, that α 1 ​ ( 0) ​ α 2 ​ ( 0) ≥ 1 \alpha_{1}(0)\alpha_{2}(0)\geq 1. Denote the zero loci of the imaginary parts of the Dulac maps 𝒟 λ 1 ​ ( z) \mathcal{D}_{\lambda}^{1}(z), 𝒟 λ 2 ​ ( z) \mathcal{D}_{\lambda}^{2}(z) by ℋ λ 1 \mathcal{H}_{\lambda}^{1} and ℋ λ 2 \mathcal{H}_{\lambda}^{2} respectively. We shall bound the number of the zeros of ψ λ \psi_{\lambda} in the complex domain 𝐃 R \mathbf{D}_{R} of the universal covering of ℂ ∖ { s 1 ​ ( λ), s 2 ​ ( λ) } \mathbb{C}\setminus\{s_{1}(\lambda),s_{2}(\lambda)\} defined as follows (without loss of generality we assume that s 1 ​ ( λ) ≤ s 2 ​ ( λ) s_{1}(\lambda)\leq s_{2}(\lambda)).

- •

if α 2 ​ ( 0) > 1 \alpha_{2}(0)>1, the domain 𝐃 R \mathbf{D}_{R} is bounded by the circle

 | S R = { z: | z | = R }, S_{R}=\{z:|z|=R\}, |  | (17) |

and by

 | ℋ λ, 1 1, ℋ λ, − 1 1, ℋ λ, 1 2, ℋ λ, − 1 2 \mathcal{H}_{\lambda,1}^{1},\mathcal{H}_{\lambda,-1}^{1},\mathcal{H}_{\lambda,1}^{2},\mathcal{H}_{\lambda,-1}^{2} |  |

as it is shown on fig. 7.

- •

if α 2 ​ ( 0) ≤ 1 \alpha_{2}(0)\leq 1 then necessarily α 1 ​ ( 0) ≥ 1 \alpha_{1}(0)\geq 1. The domain 𝐃 R \mathbf{D}_{R} is bounded by the circle S R S_{R}, by the interval [s 1 ​ ( λ), s 2 ​ ( λ)] [s_{1}(\lambda),s_{2}(\lambda)], and by ℋ λ, 1 1, ℋ λ, − 1 1 \mathcal{H}_{\lambda,1}^{1},\mathcal{H}_{\lambda,-1}^{1}, as it is shown on fig. 8.

Figure 7: The domain 𝐃 R ⊂ ℂ ∙ \mathbf{D}_{R}\subset\mathbb{C}_{\bullet} projected on the complex plane ℂ \mathbb{C} in the case α 2 ​ ( 0) > 1 \alpha_{2}(0)>1.

In the course of the proof the parameters R R and λ \lambda will be chosen as in the one-saddle case: the constant R R will be sufficiently small, ε 0 > 0 \varepsilon_{0}>0 will be sufficiently small with respect to R R, and λ ∈ ℝ N \lambda\in\mathbb{R}^{N} will be such that | λ | < ε 0 |\lambda|<\varepsilon_{0}, see ( 13). Like in section 3 we shall suppose, without loss of generality, that the analytic functions c 1 ​ ( λ), c 2 ​ ( λ) c_{1}(\lambda),c_{2}(\lambda) where

 | lim z → s 1 ​ ( λ), z ∈ 𝐃 R ψ λ ​ ( z) = c 1 ​ ( λ), lim z → s 2 ​ ( λ), z ∈ 𝐃 R ψ λ ​ ( z) = c 2 ​ ( λ) \lim_{z\rightarrow s_{1}(\lambda),z\in\mathbf{D}_{R}}\psi_{\lambda}(z)=c_{1}(\lambda),\lim_{z\rightarrow s_{2}(\lambda),z\in\mathbf{D}_{R}}\psi_{\lambda}(z)=c_{2}(\lambda) |  |

are not identically zero. This will guarantee that for generic values of λ \lambda the displacement map will have only regular zeros in the closure of 𝐃 R \mathbf{D}_{R}, so the argument principle (Proposition 1) can be applied.

Proof of Theorem 4. It follows from the definition of the domain 𝐃 R ⊂ ℂ ∙ \mathbf{D}_{R}\subset\mathbb{C}_{\bullet} that the displacement map ψ λ ​ ( z) \psi_{\lambda}(z) is analytic there. To count the zeros (corresponding to real and complex limit cycles) of the displacement map in 𝐃 R \mathbf{D}_{R} we apply Proposition 1 (the argument principle) to the family of functions ψ λ \psi_{\lambda}. To evaluate the variation of the argument of the displacement map along the border of 𝐃 R \mathbf{D}_{R} we repeat the arguments of section 3.

Consider first the case α 2 ​ ( 0) > 1 \alpha_{2}(0)>1, fig. 7. The connected component of the zero locus of the imaginary part of 𝒟 λ 2 \mathcal{D}_{\lambda}^{2} which is tangent to the line φ = π / α 2 ​ ( λ) \varphi=\pi/\alpha_{2}(\lambda) through s 2 ​ ( λ) s_{2}(\lambda) intersects the circle S R S_{R} transversally, and along this circle the variation of the argument of ψ λ \psi_{\lambda} is uniformly bounded in λ \lambda (Theorem 2). The imaginary part of ψ λ ​ ( z) \psi_{\lambda}(z) restricted to ℋ λ 1 \mathcal{H}_{\lambda}^{1} equals the imaginary part of − 𝒟 λ 2 -\mathcal{D}_{\lambda}^{2} and hence Im ⁡ ψ λ \operatorname{Im}\psi_{\lambda} vanishes along ℋ λ, 1 1, ℋ λ, − 1 1 \mathcal{H}_{\lambda,1}^{1},\mathcal{H}_{\lambda,-1}^{1} exactly at the intersection points

 | ℋ λ, 1 1 ∩ ℋ λ, 1 2, ℋ λ, − 1 1 ∩ ℋ λ, − 1 2. \mathcal{H}_{\lambda,1}^{1}\cap\mathcal{H}_{\lambda,1}^{2},\quad\mathcal{H}_{\lambda,-1}^{1}\cap\mathcal{H}_{\lambda,-1}^{2}. |  |

According to Lemma 2 these intersection points are the solutions of the equation

 | h 2 λ ​ ( z) = h 1 λ ​ ( z) h^{\lambda}_{2}(z)=h^{\lambda}_{1}(z) |  | (18) |

where h 1 λ, h 2 λ h^{\lambda}_{1},h^{\lambda}_{2} are the holonomies of the separatrices intersecting σ \sigma and related to the saddle points s 1 ​ ( λ) s_{1}(\lambda) and s 2 ​ ( λ) s_{2}(\lambda). By Gabrielov’s theorem, the number of such fixed points is uniformly bounded in the disc { z: | z | < R } \{z:|z|<R\}.

Figure 8: The domain 𝐃 R ⊂ ℂ ∙ \mathbf{D}_{R}\subset\mathbb{C}_{\bullet} projected on the complex plane ℂ \mathbb{C} in the case α 2 ​ ( 0) ≤ 1 \alpha_{2}(0)\leq 1, α 1 ​ ( 0) ≥ 1 \alpha_{1}(0)\geq 1.

Consider now the second case α 2 ​ ( 0) ≤ 1 \alpha_{2}(0)\leq 1, α 1 ​ ( 0) ≥ 1 \alpha_{1}(0)\geq 1, see fig. 8. Along this circle S R S_{R} the variation of the argument of ψ λ \psi_{\lambda} is uniformly bounded in λ \lambda (Theorem 2). Along the interval [s 1 ​ ( λ), s 2 ​ ( λ)] [s_{1}(\lambda),s_{2}(\lambda)] the imaginary part of 𝒟 λ 1 \mathcal{D}_{\lambda}^{1} vanishes identically, and the imaginary part of ψ λ ​ ( z) \psi_{\lambda}(z) restricted to this interval equals the imaginary part of − 𝒟 λ 2 -\mathcal{D}_{\lambda}^{2}. Therefore the zeros of Im ⁡ ( ψ λ) \operatorname{Im}(\psi_{\lambda}) along [s 1 ​ ( λ), s 2 ​ ( λ)] [s_{1}(\lambda),s_{2}(\lambda)] are exactly the intersection points of ℋ λ, 1 2 \mathcal{H}_{\lambda,1}^{2} and [s 1 ​ ( λ), s 2 ​ ( λ)] [s_{1}(\lambda),s_{2}(\lambda)]. By Lemma 2, and like in ( 14), these intersection points are the solution of the equation

 | h 2 λ ​ ( z) = z h^{\lambda}_{2}(z)=z |  |

where h ′′ h^{\prime\prime} is the holonomy of the separatrix intersecting σ \sigma and related to the saddle points s 2 ​ ( λ) s_{2}(\lambda). By Gabrielov’s theorem, the number of such fixed points is uniformly bounded. Finally, the zeros of Im ⁡ ( ψ λ) \operatorname{Im}(\psi_{\lambda}) along ℋ λ, 1 1 \mathcal{H}_{\lambda,1}^{1} and ℋ λ, − 1 1 \mathcal{H}_{\lambda,-1}^{1} are evaluated as in the case α 2 ​ ( 0) > 1 \alpha_{2}(0)>1. This completes the proof of Theorem 4. □ \Box

## 6 Concluding remarks.

The identity ( 18) which determines complex limit cycles "responsible" for the cyclicity of the double loop Γ 2 \Gamma_{2} is the main new ingredient in the proof with respect to the one-saddle case. Indeed, solutions of ( 18) are fixed points of the holonomy h 2 λ ∘ ( h 1 λ) − 1 h^{\lambda}_{2}\circ(h^{\lambda}_{1})^{-1} which, for λ = 0 \lambda=0, is generated by a closed loop γ \gamma contained in the complexified separatrix of Γ 2 \Gamma_{2} intersecting the cross-section σ \sigma. The topological type of this separatrix near Γ 2 \Gamma_{2} is a disc with two punctures, corresponding to the two saddle points S 1 ​ ( λ) S_{1}(\lambda) and S 2 ​ ( λ) S_{2}(\lambda). Clearly γ \gamma makes one turn around each of them, but depending on the orientation we have two possibilities shown on fig. 9 (i) and (ii). A simple computation on a model example shows that the loop γ \gamma associated to the holonomy h 2 λ ∘ ( h 1 λ) − 1 h^{\lambda}_{2}\circ(h^{\lambda}_{1})^{-1} is the figure eight-loop on fig. 9 (i). The reader will recognize in the loop γ \gamma a key ingredient in the proof of the local boundedness of the number of zeros of pseudo-Abelian integrals in [3, 4].

Figure 9: The figure eight-loop γ \gamma.

Although the result of Theorem 4 is existential, the proof we use leads to effective upper bounds on the number of the bifurcating limit cycles. This possibility is explored in [10], where we show that the cyclicity of a Hamiltonian two-loop is bounded by the number of the zeros of *a pair*of associated Abelian integrals, a phenomenon which also explains the appearance of alien limit cycles in [8].

Figure 10: Hyperbolic planar polycycles with finite cyclicity.

It worth noting, that our finitness result holds true, with the same proof, for other hyperbolic polycycles (on the plane or on an analytic surface), as those shown on fig. 10.

#### Acknowledgments.

The author thanks Marcin Bobieński for the stimulating discussions, as well to the anonymous referees for the valuable suggestions.

## References

- [1] V. I. Arnol ′ d. Geometrical methods in the theory of ordinary differential equations, volume 250 of Grundlehren der Mathematischen Wissenschaften. Springer-Verlag, New York, second edition, 1988.
- [2] Gal Binyamini, Dmitry Novikov, and Sergei Yakovenko. On the number of zeros of abelian integrals. Invent. Math., 181(2):227–289, 2010.
- [3] Marcin Bobieński, Pavao Mardešić, and Dmitry Novikov. Pseudo-Abelian integrals: unfolding generic exponential. J. Differential Equations, 247(12):3357–3376, 2009.
- [4] Marcin Bobieński, Pavao Mardešić, and Dmitry Novikov. Pseudo-abelian integrals on slow-fast darboux systems. 2010, arXiv:1007.2001 [math.DS].
- [5] Briot and Bouquet. Recherches sur les propriétés des fonctions définies par des équations différentielles. J.E.P., 21(36):133–198, 1856.
- [6] Magdalena Caubergh, Freddy Dumortier, and Robert Roussarie. Alien limit cycles in rigid unfoldings of a Hamiltonian 2-saddle cycle. Commun. Pure Appl. Anal., 6(1):1–21, 2007.
- [7] L.A. Cherkas. The stability of singular cycles. Differ. Equations 4, (1968):524–526, 1972.
- [8] Freddy Dumortier and Robert Roussarie. Abelian integrals and limit cycles. J. Differential Equations, 227(1):116–165, 2006.
- [9] A. M. Gabrièlov. Projections of semianalytic sets. Funkcional. Anal. i Priložen., 2(4):18–30, 1968.
- [10] Lubomir Gavrilov. On the number of limit cycles which appear by perturbation of hamiltonian two-saddle cycles of planar vector fields. Bulletin of the Brazilian Mathematical Society, 42:1–23, 2011. 10.1007/s00574-011-0001-z.
- [11] Yu. Ilyashenko and S. Yakovenko. Finite cyclicity of elementary polycycles in generic families. Providence, RI: American Mathematical Society, 1995.
- [12] V. Kaloshin. The existential Hilbert 16-th problem and an estimate for cyclicity of elementary polycycles. Invent. Math., 151(3):451–512, 2003.
- [13] Chengzhi Li and Robert Roussarie. The cyclicity of the elliptic segment loops of the reversible quadratic Hamiltonian systems under quadratic perturbations. J. Differential Equations, 205(2):488–520, 2004.
- [14] S. Łojasiewicz, J.-Cl. Tougeron, and M.-A. Zurro. Éclatement des coefficients des séries entières et deux théorèmes de Gabrielov. Manuscripta Math., 92(3):325–337, 1997.
- [15] Frank Loray. Pseudo-groupe d’une singularité de feuilletage holomorphe en dimension deux. `http://hal.archives-ouvertes.fr/hal-00016434/en/`, January 2005.
- [16] Stijn Luca, Freddy Dumortier, Magdalena Caubergh, and Robert Roussarie. Detecting alien limit cycles near a Hamiltonian 2-saddle cycle. Discrete Contin. Dyn. Syst., 25(4):1081–1108, 2009.
- [17] J.-F. Mattei and R. Moussu. Holonomie et intégrales premières. Ann. Sci. École Norm. Sup. (4), 13(4):469–523, 1980.
- [18] A. Mourtada. Action de derivations irreductibles sur les algebres quasi-regulieres d’hilbert, arxiv:0912.1560v1, 2009.
- [19] G. S. Petrov. Elliptic integrals and their nonoscillation. Funktsional. Anal. i Prilozhen., 20(1):46–49, 96, 1986.
- [20] G. S. Petrov. The problem of the number of zeros of an elliptic integral is a semi-algebraic problem. Mat. Zametki, 44(3):393–401, 412, 1988.
- [21] Robert Roussarie. On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields. Bol. Soc. Brasil. Mat., 17(2):67–101, 1986.
- [22] Robert Roussarie. Cyclicité finie des lacets et des points cuspidaux. Nonlinearity, 2(1):73–117, 1989.
- [23] Robert Roussarie. Bifurcation of planar vector fields and Hilbert’s sixteenth problem, volume 164 of Progress in Mathematics. Birkhäuser Verlag, Basel, 1998.
- [24] Robert Roussarie. Quasi-conformal mapping theorem and bifurcations. Bol. Soc. Brasil. Mat. (N.S.), 29(2):229–251, 1998.
- [25] Henryk Żoładek. The monodromy group, volume 67 of Mathematics Institute of the Polish Academy of Sciences. Mathematical Monographs (New Series). Birkhäuser Verlag, Basel, 2006.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
