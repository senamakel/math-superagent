<!-- source: https://arxiv.org/html/2504.07225 | converted from HTML -->

1Introduction

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2504.07225v1 [math.DS] 09 Apr 2025

On the cyclicity of persistent hyperbolic polycycles

Lucas Queiroz Arakaki ∗, Paulo Santana
UNICAMP, Campinas, SP, Brazil.

IBILCE-UNESP, S. J. Rio Preto, SP, Brazil.

e-mail: larakaki@unicamp.br, paulo.santana@unesp.br

Abstract

In this work we consider families of smooth vector fields having a persistent polycycle with n n hyperbolic saddles. We derive the asymptotic expansion of the return map associated to the polycycle, determining explicitly its leading terms. As a consequence, explicit conditions on the leading terms allow us to determine the cyclicity of such polycycles. We then apply our results to study the cyclicity of a polycycle of a model with applications in Game Theory.

Key-words: Limit cycle, cyclicity, polycycle, asymptotic expansion

2020 Mathematics Subject Classification: 34C07, 37C27, 34C23, 37C29

∗ Corresponding author.

## 1 Introduction

As an extensive effort to prove the existential part of Hilbert’s sixteenth problem, several authors worked in proving the finite cyclicity of the limit periodic sets inside polynomial vector fields, since the finite cyclicity of the limit periodic sets implies that the number of limit cycles is also finite [20]. A limit periodic set inside a polynomial vector field is one of the following: a singular point, a periodic orbit or a graphic.

The cyclicity of graphics was extensively studied in the literature (see, for instance [5, 21, 4]). For hyperbolic polycycles, i. e. graphics whose corners are hyperbolic saddles and with a well defined return map on one of its sides, it is essential to understand the behavior and properties of the *Dulac map*which is the transition map in the neighborhood of a hyperbolic saddle. In this regard, the works of A. Mourtada [15, 16, 17, 18] have substantially developed the understanding of the Dulac map by obtaining a normal form for the Dulac map, namely

 | D ⁡ ( s, μ) = s λ ⁡ ( μ) ​ ( A ⁡ ( μ) + R ⁡ ( s, μ)), D(s;\mu)=s^{\lambda(\mu)}(A(\mu)+R(s;\mu)), |  |

where r ⁡ ( μ) r(\mu) is the *hyperbolicity ratio*of the hyperbolic saddle and R ⁡ ( s, μ) R(s;\mu) is a well-behaved remainder. The Mourtada’s normal form was further studied to obtain some results on the stability of a generic polycycle [7] and an upper bound on the cyclicity [19].

Recently Marín and Villadelprat [10, 11, 13] proved several results on the Dulac map, which improved uppon Mourtada’s normal form. More precisely, they obtained an asymptotic development of the Dulac map and proved that the remainder R ⁡ ( s, μ) R(s;\mu) belongs to a class of finitely flat functions. Using their asymptotic development, several advancements in the study of the cyclicity of hyperbolic polycycles have been made (see [12, 3]).

When dealing with perturbations of hyperbolic polycycles, in the context of bifurcation of limit cycles, the generic behavior is the breaking of one of its saddle connections (see, for instance [3, 8]). In the non-generic scenario where all saddle connections remain unbroken throughout the perturbation, we say that the polycycle is *persistent*. This type of polycycle was studied in [12, 14]. In this regard, in [12], the authors studied the cyclicity of the persistent polycycle with three corners that arise in Kolmogorov systems. Their approach was to study the return map associated to the polycycle and obtaining explicit expressions for its leading terms which define three functions that played the same role for the cyclicity of the polycycle as the Lyapunov quantities’ role for the cyclicity of a focus.

In the present paper, we will consider the cyclicity of persistent polycycles. Our goal is to generalize the results of [12] to a more general class of persistent polycycles. In this direction, we obtain the explicit expressions for the leading terms of the return map under some assumptions which then allow us to state some conditions on these leading terms so that the cyclicity of the polycycle is determined.

## 2 Statement of the main results

We now provide the necessary definitions for a precise statement of our main results.

###### Definition 1 (Polycycle).

Let X X be a two-dimensional vector field. A *graphic*Γ \Gamma for X X is a compact non-empty invariant subset which is a continuous image of 𝕊 1 \mathbb{S}^{1} and consists of a finite number of (not necessarily distinct) isolated singular points { p 1, …, p n, p n + 1 = p 1 } \{p_{1},\dots,p_{n},p_{n+1}=p_{1}\} and compatibly oriented separatrices { γ 1, …, γ n } \{\gamma_{1},\dots,\gamma_{n}\} connecting them (meaning that γ i \gamma_{i} has { p i } \{p_{i}\} as the α \alpha -limit set and { p i + 1 } \{p_{i+1}\} as the ω \omega -limit set). A graphic for which all its singular points are hyperbolic saddles is said to be *hyperbolic*. A *polycycle*is a graphic with a well-defined first return map ℛ \mathscr{R} on one of its sides, see Figure 1.

\begin{overpic}[Fig1.eps] \put(95.0,22.0){$p_{1}$} \put(-1.0,23.0){$p_{2}$} \put(76.0,40.0){$L_{1}$} \put(15.0,5.0){$L_{2}$} \put(11.0,41.0){$s$} \put(43.0,31.0){$\mathscr{R}(s)$} \end{overpic}

( a) (a)

\begin{overpic}[Fig2.eps] \put(54.0,22.5){$p_{1}=p_{2}$} \put(74.0,6.0){$L_{1}$} \put(15.0,36.0){$L_{2}$} \put(69.0,30.0){$s$} \put(36.0,46.0){$\mathscr{R}(s)$} \end{overpic}

( b) (b)

Figure 1: Illustration of Γ \Gamma, with ( a) (a) distinct and ( b) (b) non-distinct hyperbolic saddles.

###### Definition 2 (Persistent polycycle).

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth (i.e. of class C ∞ C^{\infty}) family of planar smooth vector fields such that Γ \Gamma is a hyperbolic polycycle of X μ 0 X_{\mu_{0}}. We say that Γ \Gamma is a *persistent polycycle*when all of its separatrix connections remain unbroken inside the family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda}.

###### Definition 3 (Independent functions).

Let Λ \Lambda be a topological space and consider a set of functions f i: Λ → ℝ f_{i}:\Lambda\to\mathbb{R}, i ∈ { 1, …, m } i\in\{1,\dots,m\}. For each k ∈ { 1, …, m } k\in\{1,\dots,m\} we denote by

 | V ( f 1, …, f k) = { μ ∈ Λ: f i ( μ) = 0, i ∈ { 1, …, k } } V(f_{1},\dots,f_{k})=\{\mu\in\Lambda:f_{i}(\mu)=0,\,i\in\{1,\dots,k\}\} |  |

the variety defined by f 1, …, f k f_{1},\dots,f_{k}. Given μ 0 ∈ V ⁡ ( f 1, …, f m) \mu_{0}\in V(f_{1},\dots,f_{m}), we say that f 1, …, f m f_{1},\dots,f_{m}*are independent at*μ 0 \mu_{0}, when the following holds:

- •

If μ 0 ∈ V ⁡ ( f 1) \mu_{0}\in V(f_{1}), then every neighborhood of μ 0 \mu_{0} contains two points μ 1, μ 2 \mu_{1},\mu_{2} such that f 1 ​ ( μ 1) ​ f 1 ​ ( μ 2) < 0 f_{1}(\mu_{1})f_{1}(\mu_{2})<0;

- •

For every k ∈ { 2, …, m } k\in\{2,\dots,m\} and every neighborhood U U of μ 0 \mu_{0}, there are two points μ 1, μ 2 ∈ U ∩ V ⁡ ( f 1, …, f k − 1) \mu_{1},\mu_{2}\in U\cap V(f_{1},\dots,f_{k-1}) such that f k ​ ( μ 1) ​ f k ​ ( μ 2) < 0 f_{k}(\mu_{1})f_{k}(\mu_{2})<0.

Observe that if Λ ⊂ ℝ N \Lambda\subset\mathbb{R}^{N}, N ⩾ m N\geqslant m, is an open set, the functions f 1, …, f m f_{1},\dots,f_{m} are of class C 1 C^{1} and the gradients ∇ f 1 ​ ( μ 0), …, ∇ f m ​ ( μ 0) \nabla f_{1}(\mu_{0}),\dots,\nabla f_{m}(\mu_{0}) are linearly independent vectors of ℝ N \mathbb{R}^{N}, then there is a neighborhood U ⊂ Λ U\subset\Lambda of μ 0 \mu_{0} whose restriction of f 1, …, f m f_{1},\dots,f_{m} to U U are independent at μ 0 \mu_{0}.

In the next definition dist H \rm{dist}_{H} stands for the Hausdorff distance between compact sets of ℝ 2 \mathbb{R}^{2}.

###### Definition 4 (Cyclicity).

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields on and suppose that Γ \Gamma is a polycycle for X μ 0 X_{\mu_{0}}. We say that Γ \Gamma has finite cyclicity in the family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} if there exist κ ∈ ℕ \kappa\in\mathbb{N}, ε > 0 \varepsilon>0 and δ > 0 \delta>0 such that any X μ X_{\mu} with | μ − μ 0 | < δ |\mu-\mu_{0}|<\delta has at most κ \kappa limit cycles γ i \gamma_{i} with dist H ​ ( Γ, γ i) < ε \rm{dist}_{H}(\Gamma,\gamma_{i})<\varepsilon for i ∈ { 1, …, κ } i\in\{1,\dots,\kappa\}. The minimum of such κ \kappa when δ \delta and ε \varepsilon go to zero is called *cyclicity*of Γ \Gamma in { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} at μ = μ 0 \mu=\mu_{0} and denoted by Cycl ⁡ ( Γ, μ 0) \rm{Cycl}(\Gamma,\mu_{0}).

Consider a smooth family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} of planar smooth vector fields having a persistent polycycle Γ \Gamma with m m hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n} (to simplify the notation we have dropped the dependence on μ \mu of the saddles). Let λ i s ​ ( μ) < 0 < λ i u ​ ( μ) \lambda_{i}^{s}(\mu)<0<\lambda_{i}^{u}(\mu) be the associated eigenvalues of p i p_{i}. The *hyperbolicity ratio*of p i p_{i} is the positive real number given by

 | λ i ​ ( μ):= | λ i s ​ ( μ) | λ i u ​ ( μ). \lambda_{i}(\mu):=\frac{|\lambda_{i}^{s}(\mu)|}{\lambda_{i}^{u}(\mu)}. |  | (1) |

The product of the hyperbolicity ratios

 | r ⁡ ( μ) = ∏ i = 1 n λ i ​ ( μ), r(\mu)=\prod_{i=1}^{n}\lambda_{i}(\mu), |  | (2) |

is called *graphic number*of Γ \Gamma. Note that the case n = 1 n=1 corresponds to a saddle loop.

Čerkas [25] proved that if r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1, then Γ \Gamma has a well defined stability. More precisely if r ⁡ ( μ 0) > 1 r(\mu_{0})>1, then Γ \Gamma is stable (i.e. it attracts the orbits in the region where the first return map is defined). Similarly if r ⁡ ( μ 0) < 1 r(\mu_{0})<1, then Γ \Gamma is unstable. Since r ⁡ ( Γ) r(\Gamma) depends continuously on smooth perturbations, it follows that if Γ \Gamma is persistent and r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1, then Γ \Gamma has no change of stability for small perturbations. According with the terminology introduced by Sotomayor [23, Section 2.2], if r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1 then we say that Γ \Gamma is a *simple*polycycle.

As anticipated in the Introduction, in recent years Marín and Villadelprat [10, 11, 13] proved several results on the Dulac map of hyperbolic saddles. For simplicity we postpone their precise statements to Section 3. In what follows we state only a simple version of their results and definitions, sufficient for the statement of our first main result.

###### Definition 5 (Well-behaved remainder).

Consider an open set U ⊂ ℝ N U\subset\mathbb{R}^{N} and a smooth function ψ: ( 0, ε) × U → ℝ \psi\colon(0,\varepsilon)\times U\to\mathbb{R}, with ε > 0 \varepsilon>0 small. Given ℓ ∈ ℝ \ell\in\mathbb{R} and μ 0 ∈ U \mu_{0}\in U, we write ψ ∈ ℱ ℓ ∞ ​ ( μ 0) \psi\in\mathcal{F}^{\infty}_{\ell}(\mu_{0}) if for each ν = ( ν 0, ν 1, …, ν n) ∈ ℤ ⩾ 0 N + 1 \nu=(\nu_{0},\nu_{1},\dots,\nu_{n})\in\mathbb{Z}_{\geqslant 0}^{N+1} there are a neighborhood V ⊂ U V\subset U of μ 0 \mu_{0}, C > 0 C>0 and s 0 > 0 s_{0}>0 such that

 | | ∂ | ν | ψ ∂ s ν 0 ∂ μ 1 ν 1 ⋯ ∂ μ N ν N ​ ( s, μ) | ⩽ C ​ s ℓ − ν 0 ​ for all ​ s ∈ ( 0, s 0) ​ and ​ μ ∈ V, \left|\dfrac{\partial^{|\nu|}\psi}{\partial s^{\nu_{0}}\partial\mu_{1}^{\nu_{1}}\cdots\partial\mu_{N}^{\nu_{N}}}(s;\mu)\right|\leqslant Cs^{\ell-\nu_{0}}\;\text{for all }s\in(0,s_{0})\text{ and }\mu\in V, |  |

where | ν | = ν 0 + ⋯ + ν N |\nu|=\nu_{0}+\dots+\nu_{N} and μ = ( μ 1, …, μ N) \mu=(\mu_{1},\dots,\mu_{N}).

From [10, 11, 13] we have that the Dulac map of the hyperbolic saddle p i p_{i} can be written as

 | D i ​ ( s, μ) = s λ i ​ ( Δ 00 i + ℱ ℓ ∞ ​ ( μ 0)), D_{i}(s;\mu)=s^{\lambda_{i}}\bigl(\Delta_{00}^{i}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  | (3) |

for any given ℓ ∈ ( 0, min ⁡ { λ i 0, 1 }) \ell\in(0,\min\{\lambda_{i}^{0},1\}), where λ i = λ i ​ ( μ) \lambda_{i}=\lambda_{i}(\mu) is the hyperbolicity ratio ( 1), λ i 0 = λ i ​ ( μ 0) \lambda_{i}^{0}=\lambda_{i}(\mu_{0}), and Δ 00 i = Δ 00 i ​ ( μ) \Delta_{00}^{i}=\Delta_{00}^{i}(\mu) is a strictly positive smooth function defined in a neighborhood of μ 0 \mu_{0} (we dropped the μ \mu -dependence at the right-hand side of ( 3) for simplicity). For the explicit expression of Δ 00 i \Delta_{00}^{i}, see Appendix B. Given j j, k ∈ { 0, …, n } k\in\{0,\dots,n\}, j ⩽ k j\leqslant k, we define

 | A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1, Λ i, k 0 = Λ i, k ​ ( μ 0). A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\quad\Lambda_{kk}=1,\quad\Lambda_{i,k}^{0}=\Lambda_{i,k}(\mu_{0}). |  | (4) |

In our first main result we provide an explicit expression for the first return map of a persistent polycycle and use this expression to study its cyclicity. We recall that r ⁡ ( μ) r(\mu) denotes the graphic number ( 2) of Γ \Gamma.

###### Theorem A.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar analytic vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n}. Then the first return map associated to Γ \Gamma is given by

 | ℛ ⁡ ( s, μ) = s r ⁡ ( μ) ​ ( A 1, n + ℱ ℓ ∞ ​ ( μ 0)), \mathscr{R}(s;\mu)=s^{r(\mu)}\bigl(A_{1,n}+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\bigr), |  | (5) |

for any given ℓ ∈ ( 0, min ⁡ { Λ i, n: i ∈ { 0, …, n } }) \ell\in\bigl(0,\min\bigl\{\Lambda_{i,n}\colon i\in\{0,\dots,n\}\bigr\}\bigr). Moreover, the following holds:

- (a)

Cycl ⁡ ( Γ, μ 0) = 0 {\rm Cycl}(\Gamma,\mu_{0})=0, if r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1;

- (b)

Cycl ⁡ ( Γ, μ 0) ⩾ 1 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 1, if r ⁡ ( μ 0) = 1 r(\mu_{0})=1, r ⁡ ( μ) − 1 r(\mu)-1 changes signs at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id;

- (c)

Cycl ⁡ ( Γ, μ 0) ⩽ 1 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 1, if A 1, n ​ ( μ 0) ≠ 1 A_{1,n}(\mu_{0})\neq 1;

- (d)

Cycl ⁡ ( Γ, μ 0) ⩾ 2 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 2, if r ⁡ ( μ 0) = A 1, n ​ ( μ 0) = 1 r(\mu_{0})=A_{1,n}(\mu_{0})=1, r − 1, A 1, n − 1 r-1,\;A_{1,n}-1 are independent at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id.

We observe that the expression ( 5) of the first return map is similar to the expressions ( 3) of the Dulac maps. Hence we say that it is of *Dulac-type*.

In order to obtain conditions for a higher cyclicity, it is necessary to obtain a more refined expression for the first return map. This in turn implies in the necessity to study more refined expressions of the Dulac maps. To this end, we briefly observe that from [10, 11, 13] it follows that the Dulac map can be written as

 | D i ​ ( s, μ) = { s λ i ​ ( Δ 00 i + Δ 10 i ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) if ​ λ i 0 > 1, s λ i ​ ( Δ 00 i + Δ 01 i ​ s λ i + ℱ ℓ 2 ∞ ​ ( μ 0)) if ​ λ i 0 < 1, D_{i}(s;\mu)=\left\{\begin{array}[]{ll}\displaystyle s^{\lambda_{i}}\bigl(\Delta_{00}^{i}+\Delta_{10}^{i}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)&\text{if }\lambda_{i}^{0}>1,\\ \displaystyle s^{\lambda_{i}}\bigl(\Delta_{00}^{i}+\Delta_{01}^{i}s^{\lambda_{i}}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr)&\text{if }\lambda_{i}^{0}<1,\end{array}\right. |  |

for any given ℓ 1 ∈ ( 1, min ⁡ { λ i 0, 2 }) \ell_{1}\in(1,\min\{\lambda_{i}^{0},2\}) and ℓ 2 ∈ ( λ i 0, min ⁡ { 2 ​ λ i 0, 1 }) \ell_{2}\in(\lambda_{i}^{0},\min\{2\lambda_{i}^{0},1\}). The functions Δ 10 i \Delta_{10}^{i} and Δ 01 i \Delta_{01}^{i} may have some poles and thus may not be well-defined everywhere. Nevertheless, the reader shall see at Section 3 that such a poles will not be a problem in this paper.

In [13] the authors provided explicit formulas for Δ 10 \Delta_{10} and Δ 01 \Delta_{01}. Such formulas depend on some other functions S 1 i S_{1}^{i} and S 2 i S_{2}^{i} satisfying the following relationships:

 | Δ 10 i = λ i ​ Δ 00 i ​ S 1 i, Δ 01 i = − ( Δ 00 i) 2 ​ S 2 i. \Delta_{10}^{i}=\lambda_{i}\Delta_{00}^{i}S_{1}^{i},\quad\Delta_{01}^{i}=-(\Delta_{00}^{i})^{2}S_{2}^{i}. |  |

More details are postponed to Section 3.

In our second main result we use the refined expression of the Dulac maps to obtain a refined expression for the first return map, which in turn allow us to obtain conditions for higher cyclicities.

###### Theorem B.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar analytic vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p m, p m + 1, …, p n p_{1},\dots,p_{m},p_{m+1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1 for i ∈ { 1, …, m } i\in\{1,\dots,m\} and λ i ​ ( μ 0) > 1 \lambda_{i}(\mu_{0})>1 for i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\}. Then the first return map of Γ \Gamma is given by

 | . ℛ ( s; μ) = s r ⁡ ( μ) ( A 1, n + 𝒜 s Λ 0, m + ℱ ℓ ∞ ( μ 0)),.\mathscr{R}(s;\mu)=s^{r(\mu)}\bigl(A_{1,n}+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  | (6) |

for any given ℓ ∈ ( Λ 0, m 0, min ⁡ { r ⁡ ( μ 0), 2 ​ Λ 0, m 0, 1 }) \ell\in(\Lambda_{0,m}^{0},\min\{r(\mu_{0}),2\Lambda_{0,m}^{0},1\}), where

 | 𝒜 = Λ m, n ​ A 1, m ​ A 1, n ​ ( S 1 m + 1 − S 2 m). \mathcal{A}=\Lambda_{m,n}A_{1,m}A_{1,n}(S_{1}^{m+1}-S_{2}^{m}). |  | (7) |

Moreover, the following holds:

- (a)

Cycl ⁡ ( Γ, μ 0) ⩽ 2 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 2, if 𝒜 ⁡ ( μ 0) ≠ 0 \mathcal{A}(\mu_{0})\neq 0;

- (b)

Cycl ⁡ ( Γ, μ 0) ⩾ 3 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 3 if r ⁡ ( μ 0) = A 1, n ​ ( μ 0) = 1 r(\mu_{0})=A_{1,n}(\mu_{0})=1, 𝒜 ⁡ ( μ 0) = 0 \mathcal{A}(\mu_{0})=0, r − 1, A 1, n − 1, 𝒜 r-1,\;A_{1,n}-1,\;\mathcal{A} are independent at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id.

Under the hypothesis of Theorem B, we observe from ( 7) that to calculate the non-leading term of the first return map, it is only necessary to know the non-leading terms of the Dulac maps of indexes m m and m + 1 m+1.

The paper is organized as follows. In Section 3 we present the fundamental concepts that will be required to the development of the paper, namely: The finitely flat functions and their properties, and the Dulac map of a hyperbolic saddle. In Section 4 we prove the technical results on the composition and inverse of Dulac maps that allowed us to obtain the coefficients in the asymptotic expansion of the return map ℛ ⁡ ( s, μ) \mathscr{R}(s;\mu). In Section 5 we recall the notion of displacement map, also used in the literature to study the cyclicity of persistent polycycles, and we study its coefficients. The proofs of our main results are presented in Section 6. In Section 7 we state and prove a similar version or our main results for the displacement map and observe that its coefficients are equivalent with the coefficients of the first return map. We conclude the paper in Section 8, presenting an application of our results in the context of Game Theory.

## 3 Preliminary results

### 3.1 Finitely flat functions

We introduce the notion of finitely flat functions that play a substantial role when dealing with the return map of a polycycle.

###### Definition 6.

Consider K ∈ ℤ ⩾ 0 ∪ { ∞ } K\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} and an open set U ⊂ ℝ N U\subset\mathbb{R}^{N}. We say that a function ψ ⁡ ( s, μ) \psi(s;\mu) belongs to class 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}_{s>0}(U) if there exists an open neighborhood Ω \Omega of { 0 } × U \{0\}\times U in ℝ N + 1 \mathbb{R}^{N+1} such that ( s, μ) ↦ ψ ⁡ ( s, μ) (s;\mu)\mapsto\psi(s,\mu) is 𝒞 K \mathscr{C}^{K} on Ω ∩ { ( 0, + ∞) × U } \Omega\cap\left\{(0,+\infty)\times U\right\}.

###### Definition 7 (Finitely flat functions).

Consider K ∈ ℤ ⩾ 0 ∪ { ∞ } K\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} and an open set U ⊂ ℝ N U\subset\mathbb{R}^{N}. Given L ∈ ℝ L\in\mathbb{R} and μ 0 ∈ U \mu_{0}\in U, we say that ψ ⁡ ( s, μ) ∈ 𝒞 s > 0 K ​ ( U) \psi(s;\mu)\in\mathscr{C}^{K}_{s>0}(U) is ( L, K) (L,K) -flat with respect to s s at μ 0 \mu_{0}, and we write ψ ∈ ℱ L K ​ ( μ 0) \psi\in\mathcal{F}^{K}_{L}(\mu_{0}), if for each ν = ( ν 0, …, ν N) ∈ ℤ ⩾ 0 N + 1 \nu=(\nu_{0},\dots,\nu_{N})\in\mathbb{Z}^{N+1}_{\geqslant 0} with | ν | ⩽ K |\nu|\leqslant K, there exist a neighborhood V V of μ 0 \mu_{0} and C C, s 0 > 0 s_{0}>0 such that

 | | ∂ ν ψ ⁡ ( s, μ) |:= | ∂ | ν | ψ ∂ s ν 0 ∂ μ 1 ν 1 ⋯ ∂ μ N ν N ​ ( s, μ) | ⩽ C ​ s L − ν 0 ​ for all ​ s ∈ ( 0, s 0) ​ and ​ μ ∈ V. |\partial_{\nu}\psi(s;\mu)|:=\left|\dfrac{\partial^{|\nu|}\psi}{\partial s^{\nu_{0}}\partial\mu_{1}^{\nu_{1}}\cdots\partial\mu_{N}^{\nu_{N}}}(s;\mu)\right|\leqslant Cs^{L-\nu_{0}}\;\text{for all }s\in(0,s_{0})\text{ and }\mu\in V. |  |

If W W is a (not necessarily open) subset of U U, then ℱ L ∞ ​ ( W) = ⋂ μ 0 ∈ W ℱ L ∞ ​ ( μ 0) \mathcal{F}^{\infty}_{L}(W)=\bigcap\limits_{\mu_{0}\in W}\mathcal{F}^{\infty}_{L}(\mu_{0}).

The usefulness of the finitely flat functions is presented in the next result.

###### Lemma 1 ( [10, Lemma A.3]).

Let U U and U ′ U^{\prime} be open sets of ℝ N \mathbb{R}^{N} and ℝ N ′ \mathbb{R}^{N^{\prime}} respectively and consider W ⊂ U W\subset U and W ′ ⊂ U ′ W^{\prime}\subset U^{\prime}. Then, the following holds:

- (a)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W ^) \mathcal{F}^{K}_{L}(W)\subset\mathcal{F}^{K}_{L}(\hat{W}) for any W ^ ⊂ W \hat{W}\subset W;

- (b)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W × W ′) \mathcal{F}^{K}_{L}(W)\subset\mathcal{F}^{K}_{L}(W\times W^{\prime});

- (c)

𝒞 K ​ ( U) ⊂ ℱ 0 K ​ ( W) \mathscr{C}^{K}(U)\subset\mathcal{F}^{K}_{0}(W);

- (d)

If K ⩾ K ′ K\geqslant K^{\prime} and L ⩾ L ′ L\geqslant L^{\prime} then ℱ L K ​ ( W) ⊂ ℱ L ′ K ′ ​ ( W) \mathcal{F}^{K}_{L}(W)\subset\mathcal{F}^{K^{\prime}}_{L^{\prime}}(W);

- (e)

ℱ L K ​ ( W) \mathcal{F}^{K}_{L}(W) is closed under addition;

- (f)

If f ∈ ℱ L K ​ ( W) f\in\mathcal{F}^{K}_{L}(W) and ν ∈ ℤ ⩾ 0 N + 1 \nu\in\mathbb{Z}^{N+1}_{\geqslant 0} with | ν | ⩽ K |\nu|\leqslant K then ∂ ν f ∈ ℱ L − ν 0 K − | ν | ​ ( W) \partial_{\nu}f\in\mathcal{F}^{K-|\nu|}_{L-\nu_{0}}(W);

- (g)

ℱ L K ​ ( W) ⋅ ℱ L ′ K ′ ​ ( W) ⊂ ℱ L + L ′ K ​ ( W) \mathcal{F}^{K}_{L}(W)\cdot\mathcal{F}^{K^{\prime}}_{L^{\prime}}(W)\subset\mathcal{F}^{K}_{L+L^{\prime}}(W);

- (h)

Assume that ϕ: U ′ → U \phi:U^{\prime}\to U is a 𝒞 K \mathscr{C}^{K} function with ϕ ⁡ ( W ′) ⊂ W \phi(W^{\prime})\subset W and let us take g ∈ ℱ L ′ K ​ ( W ′) g\in\mathcal{F}^{K}_{L^{\prime}}(W^{\prime}) with L ′ > 0 L^{\prime}>0 and verifying g ⁡ ( s, η) > 0 g(s;\eta)>0 for all η ∈ W ′ \eta\in W^{\prime} and s > 0 s>0 small enough. Consider also any f ∈ ℱ L K ​ ( W) f\in\mathcal{F}^{K}_{L}(W). Then h ⁡ ( s, η):= f ⁡ ( g ⁡ ( s, η), ϕ ⁡ ( η)) h(s;\eta):=f(g(s;\eta);\phi(\eta)) is a well-defined function that belongs to ℱ L ​ L ′ K ​ ( W ′) \mathcal{F}^{K}_{LL^{\prime}}(W^{\prime}).

In what follows we prove another technical result about ℱ L K ​ ( W) \mathcal{F}^{K}_{L}(W).

###### Lemma 2.

Given K ∈ ℤ ⩾ 0 ∪ { ∞ } K\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\}, consider a a, b b, η \eta, λ ∈ 𝒞 K ​ ( U) \lambda\in\mathscr{C}^{K}(U) such that b ⁡ ( μ) ≠ 0 b(\mu)\neq 0, λ ⁡ ( μ) > 0 \lambda(\mu)>0 for every μ ∈ U \mu\in U and denote λ 0 = λ ⁡ ( μ 0) \lambda^{0}=\lambda(\mu_{0}). If L ∈ ( λ 0, 2 ​ λ 0) L\in(\lambda^{0},2\lambda^{0}) then

 | ( b + a ​ s λ + ℱ L K ​ ( μ 0)) η = b η + η ​ b η − 1 ​ a ​ s λ + ℱ L K ​ ( μ 0), \bigl(b+as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}=b^{\eta}+\eta b^{\eta-1}as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0}), |  |

for s > 0 s>0 small enough such that | a b ​ s λ | < 1 \bigl|\frac{a}{b}s^{\lambda}\bigr|<1.

###### Proof.

We first prove for the case b ⁡ ( μ) ≡ 1 b(\mu)\equiv 1. From the Generalized Binomial Theorem 3 (GBT) we have that

 | ( 1 + a ​ s λ) − 1 = 1 − a ​ s λ + ℱ L K ​ ( μ 0), (1+as^{\lambda})^{-1}=1-as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0}), |  |

for s > 0 s>0 small enough such that | a ​ s λ | < 1 |as^{\lambda}|<1. In particular we have ( 1 + a ​ s λ) − 1 ∈ ℱ 0 K ​ ( μ 0) (1+as^{\lambda})^{-1}\in\mathcal{F}^{K}_{0}(\mu_{0}). Furthermore it also follows from the GBT that

 | ( 1 + a ​ s λ) η = 1 + η ​ a ​ s λ + ℱ L K ​ ( μ 0), (1+as^{\lambda})^{\eta}=1+\eta as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0}), |  | (8) |

for s > 0 s>0 small enough such that | a ​ s λ | < 1 |as^{\lambda}|<1. Hence ( 1 + a ​ s λ) η ∈ ℱ 0 K ​ ( μ 0) (1+as^{\lambda})^{\eta}\in\mathcal{F}^{K}_{0}(\mu_{0}). Now observe that

 | ( 1 + a ​ s λ + ℱ L K ​ ( μ 0)) η − ( 1 + a ​ s λ) η = ( 1 + a ​ s λ) η ​ [( 1 + ( 1 + a ​ s λ) − 1 ​ ℱ L K ​ ( μ 0)) η − 1] = ( 1 + a ​ s λ) η ​ [( 1 + ℱ L K ​ ( μ 0)) η − 1] = ( 1 + a ​ s λ) η ​ ℱ L K ​ ( μ 0) = ℱ L K ​ ( μ 0), \begin{array}[]{ll}\bigl(1+as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}-(1+as^{\lambda})^{\eta}&=(1+as^{\lambda})^{\eta}\bigl[\bigl(1+(1+as^{\lambda})^{-1}\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}-1\bigr]\\ &=(1+as^{\lambda})^{\eta}\bigl[\bigl(1+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}-1\bigr]\\ &=(1+as^{\lambda})^{\eta}\mathcal{F}^{K}_{L}(\mu_{0})=\mathcal{F}^{K}_{L}(\mu_{0}),\end{array} |  |

where the second equality follows from ( 1 + a ​ s λ) − 1 ∈ ℱ 0 K ​ ( μ 0) (1+as^{\lambda})^{-1}\in\mathcal{F}^{K}_{0}(\mu_{0}) in addition with Lemma 1 (g), the third equality follows from the GBT and the fourth one following from ( 1 + a ​ s λ) η ∈ ℱ 0 K ​ ( μ 0) (1+as^{\lambda})^{\eta}\in\mathcal{F}^{K}_{0}(\mu_{0}) and Lemma 1 (g). Thus we conclude that,

 | ( 1 + a ​ s λ + ℱ L K ​ ( μ 0)) η = ( 1 + a ​ s λ) η + ℱ L K ​ ( μ 0). \bigl(1+as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}=(1+as^{\lambda})^{\eta}+\mathcal{F}^{K}_{L}(\mu_{0}). |  |

This in addition with ( 8) and Lemma 1 (e) implies that

 | ( 1 + a ​ s λ + ℱ L K ​ ( μ 0)) η = 1 + η ​ a ​ s λ + ℱ L K ​ ( μ 0). \bigl(1+as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}=1+\eta as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0}). |  |

The general case now follows from observing that

 | ( b + a ​ s λ + ℱ L K ​ ( μ 0)) η = b η ​ ( 1 + a b ​ s λ + ℱ L K ​ ( μ 0)) η = b η ​ ( 1 + η ​ a b ​ s λ + ℱ L K ​ ( μ 0)) = b η + η ​ b η − 1 ​ a ​ s λ + ℱ L K ​ ( μ 0), \begin{array}[]{l}\displaystyle\bigl(b+as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\bigr)^{\eta}=b^{\eta}\left(1+\frac{a}{b}s^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\right)^{\eta}\\ \qquad\quad\displaystyle=b^{\eta}\left(1+\eta\frac{a}{b}s^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0})\right)=b^{\eta}+\eta b^{\eta-1}as^{\lambda}+\mathcal{F}^{K}_{L}(\mu_{0}),\end{array} |  |

provided s > 0 s>0 is small enough such that | a b ​ s λ | < 1 \bigl|\frac{a}{b}s^{\lambda}\bigr|<1. ∎

###### Definition 8.

The function defined for s > 0 s>0 and α ∈ ℝ \alpha\in\mathbb{R} by means of

 | ω ⁡ ( s, α) = { s − α − 1 α if ​ α ≠ 0, − ln ⁡ s if ​ α = 0, \omega(s;\alpha)=\left\{\begin{array}[]{c}\frac{s^{-\alpha}-1}{\alpha}\quad\text{if }\alpha\neq 0,\\ -\ln s\quad\text{if }\alpha=0,\end{array}\right. |  | (9) |

is called *Écalle–Roussarie compensator*.

The properties of the Écalle–Roussarie compensator are studied in detail in [10, Appendix A]. We highlight three of these properties in the next lemma.

###### Lemma 3 ( [10, Lemma A.4]).

The following holds for the Écalle–Roussarie compensator:

- •

∂ s ω ⁡ ( s, α) = − s − α − 1 \partial_{s}\omega(s;\alpha)=-s^{-\alpha-1};

- •

lim s → 0 + 1 ω ⁡ ( s, α) = max ⁡ { − α, 0 } \lim\limits_{s\to 0^{+}}\dfrac{1}{\omega(s;\alpha)}=\max\{-\alpha,0\} uniformly on α ∈ ℝ \alpha\in\mathbb{R} and in particular,

 | lim ( s, α) → ( 0 +, 0) 1 ω ⁡ ( s, α) = 0; \lim\limits_{(s,\alpha)\to(0^{+},0)}\dfrac{1}{\omega(s;\alpha)}=0; |  |

- •

ω ( s; α), 1 ω ⁡ ( s, α) ∈ ℱ − δ ∞ ( { α < δ }) \omega(s;\alpha),\frac{1}{\omega(s;\alpha)}\in\mathcal{F}^{\infty}_{-\delta}(\{\alpha<\delta\}) for every δ > 0 \delta>0.

### 3.2 The Dulac map

Since we deal with persistent hyperbolic polycycles, we need to work with the Dulac map and Dulac time associated to hyperbolic saddles. We follow closely the construction made in [10, 11, 13] where the specifics are carried out extensively. We encourage the reader to seek these references for a substantial understanding of the Dulac map and time. Here, we only state the results necessary for our investigation.

We consider an open set Λ ⊂ ℝ N \Lambda\subset\mathbb{R}^{N} and the family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} of vector fields given by:

 | X μ:= 1 x n 1 ​ y n 2 ( x P ( x, y; μ) ∂ x + y Q ( x, y; μ) ∂ y). X_{\mu}:=\dfrac{1}{x^{n_{1}}y^{n_{2}}}\left(xP(x,y;\mu)\partial_{x}+yQ(x,y;\mu)\partial_{y}\right). |  | (10) |

Here,

- •

𝚗:= ( n 1, n 2) ∈ ℤ ⩾ 0 2 \mathtt{n}:=(n_{1},n_{2})\in\mathbb{Z}_{\geqslant 0}^{2};

- •

P, Q ∈ 𝒞 ∞ ​ ( V × Λ), P,Q\in\mathscr{C}^{\infty}(V\times\Lambda), for some open set V ⊂ ℝ 2 V\subset\mathbb{R}^{2} containing the origin;

- •

P ⁡ ( x, 0, μ) > 0 P(x,0;\mu)>0 and Q ⁡ ( 0, y, μ) < 0 Q(0,y;\mu)<0, for all ( x, 0), ( 0, y) ∈ V (x,0),(0,y)\in V and μ ∈ Λ \mu\in\Lambda. This means that the origin is a hyperbolic saddle of x n 1 ​ y n 2 ​ X μ x^{n_{1}}y^{n_{2}}X_{\mu} with the y y -axis being the stable manifold and x x -axis the unstable manifold;

- •

λ ⁡ ( μ) = − Q ⁡ ( 0, 0, μ) P ⁡ ( 0, 0, μ) \lambda(\mu)=-\dfrac{Q(0,0;\mu)}{P(0,0;\mu)} is the hyperbolic ratio of the saddle.

For i ∈ { 1, 2 } i\in\{1,2\}, let σ i: ( − ε, ε) × Λ → Σ i \sigma_{i}:(-\varepsilon,\varepsilon)\times\Lambda\to\Sigma_{i} be transverse sections of X μ X_{\mu} to the axis such that

\begin{overpic}[dulac] \put(4.7,14.5){$0$} \put(11.2,14.8){$s$} \put(18.0,30.0){$\sigma_{1}$} \put(28.0,38.0){$\Sigma_{1}$} \put(52.0,20.0){$\varphi(\cdot,\sigma_{1}(s))$} \put(39.0,39.3){$\sigma_{1}(s)$} \put(72.0,10.0){$\sigma_{2}(D(s))=\varphi(T(s),\sigma_{1}(s))$} \put(73.0,-1.0){$\Sigma_{2}$} \put(77.0,25.0){$\sigma_{2}$} \put(81.5,31.4){$0$} \put(90.0,31.4){$D(s)$} \end{overpic} Figure 2: The Dulac map and time.

σ 1 ​ ( 0, μ) ∈ { ( 0, y): y > 0 } \sigma_{1}(0;\mu)\in\{(0,y):y>0\} and σ 2 ​ ( 0, μ) ∈ { ( x, 0): x > 0 } \sigma_{2}(0;\mu)\in\{(x,0):x>0\} for all μ ∈ Λ \mu\in\Lambda. The Dulac map D ⁡ ( ⋅, μ) D(\cdot;\mu) and the Dulac time T ⁡ ( ⋅, μ) T(\cdot;\mu) are defined by the following relationship:

 | φ ⁡ ( T ⁡ ( s, μ), σ 1 ​ ( s, μ), μ) = σ 2 ​ ( D ⁡ ( s, μ), μ), ∀ s ∈ ( 0, ε), \varphi(T(s;\mu),\sigma_{1}(s;\mu);\mu)=\sigma_{2}(D(s;\mu);\mu),\;\forall s\in(0,\varepsilon), |  |

where φ ⁡ ( t, p 0, μ) \varphi(t,p_{0};\mu) is the solution of X μ X_{\mu} with initial condition φ ⁡ ( 0, p 0, μ) = p 0 \varphi(0,p_{0};\mu)=p_{0} (see Figure 2).

The following result is a particular case of Theorem B in [11]. See also Theorem C ​.5 C.5 and Remark 1.1 1.1 of [13].

###### Theorem 1.

Let D ⁡ ( s, μ) D(s;\mu) be the Dulac map of the hyperbolic saddle ( 10) from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2}. Then, for λ 0 = λ ⁡ ( μ 0) \lambda^{0}=\lambda(\mu_{0}), the following holds.

- ( a) (a)

For λ 0 < 1 \lambda^{0}<1, and ℓ ∈ ( λ 0, min ⁡ { 2 ​ λ 0, 1 }) \ell\in(\lambda^{0},\min\{2\lambda^{0},1\}),

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 ​ ( λ, μ) + Δ 01 ​ ( λ, μ) ​ s λ + ℱ ℓ ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}(\lambda,\mu)+\Delta_{01}(\lambda,\mu)s^{\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\bigr), |  |

where Δ 00 ∈ 𝒞 ∞ ​ ( { ( 0, ∞) } × Λ) \Delta_{00}\in\mathscr{C}^{\infty}(\{(0,\infty)\}\times\Lambda) and Δ 01 ∈ 𝒞 ∞ ​ ( { ( 0, ∞) ∖ ℕ } × Λ) \Delta_{01}\in\mathscr{C}^{\infty}(\{(0,\infty)\setminus\mathbb{N}\}\times\Lambda). Moreover, Δ 00 \Delta_{00} is strictly positive;

- ( b) (b)

For λ 0 > 1 \lambda^{0}>1, and ℓ ∈ ( 1, min ⁡ { λ 0, 2 }) \ell\in(1,\min\{\lambda^{0},2\}),

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 ​ ( λ, μ) + Δ 10 ​ ( λ, μ) ​ s + ℱ ℓ ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}(\lambda,\mu)+\Delta_{10}(\lambda,\mu)s+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\bigr), |  |

where Δ 10 ∈ 𝒞 ∞ ​ ( { ( 0, ∞) ∖ 1 ℕ } × Λ) \Delta_{10}\in\mathscr{C}^{\infty}(\{(0,\infty)\setminus\frac{1}{\mathbb{N}}\}\times\Lambda);

- ( c) (c)

For λ 0 = 1 \lambda^{0}=1, and ℓ ∈ ( 1, 2) \ell\in(1,2),

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 ​ ( λ, μ) + 𝚫 10 ​ ( λ, μ) ​ s + ℱ ℓ ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}(\lambda,\mu)+\mathbf{\Delta}_{10}(\lambda,\mu)s+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\bigr), |  |

where 𝚫 10 = Δ 10 + Δ 01 ​ ( 1 + α ​ ω ​ ( s, α)) \mathbf{\Delta}_{10}=\Delta_{10}+\Delta_{01}(1+\alpha\omega(s;\alpha)) and α = 1 − λ \alpha=1-\lambda.

###### Remark 1.

Under the hypothesis of Theorem 1 ( a) (a), although Δ 01 \Delta_{01} may not be well defined for λ ∈ ℕ \lambda\in\mathbb{N}, these values are unreachable due to the hypothesis of λ 0 < 1 \lambda^{0}<1. More precisely, from the initial condition λ 0 < 1 \lambda^{0}<1 we have that there is a neighborhood of U U of μ 0 \mu_{0} such that λ < 1 \lambda<1 for every μ ∈ U \mu\in U. Hence, for our purposes in this paper, we can suppose that Δ 01 \Delta_{01} is always well-defined. Similarly for Theorem 1 ( b) (b).

We observe that that Theorem 1, in the way it was stated, applies to hyperbolic saddles at the origin and for which the separatrices are contained in the orthogonal axis. However, this is not a restrictive assumption since we can translate the saddle and rectify its separatrices via a smooth family diffeomorphism, see [11, Lemma 4.3 4.3].

## 4 The return map of a persistent polycycle

Consider a smooth family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} of planar smooth vector fields having a persistent polycycle Γ \Gamma with n n hyperbolic saddles, namely p 1, …, p n p_{1},\dots,p_{n}. For i ∈ { 1, …, n } i\in\{1,\dots,n\}, let Σ i \Sigma_{i} be a transversal section to the connection γ i \gamma_{i} from p i − 1 p_{i-1} to p i p_{i} (set p 0 = p n p_{0}=p_{n}), and D i = D i ​ ( ⋅, μ) D_{i}=D_{i}(\cdot;\mu) be the corresponding Dulac map, see Figure 3.

\begin{overpic}[Fig4.eps] \put(81.0,74.0){$p_{1}$} \put(15.0,74.0){$p_{2}$} \put(-1.0,3.0){$p_{3}$} \put(46.0,-0.5){$p_{4}=p_{5}$} \put(97.0,3.0){$p_{6}$} \put(84.0,44.0){$\Sigma_{1}$} \put(49.0,69.0){$\Sigma_{2}$} \put(9.5,42.0){$\Sigma_{3}$} \put(30.0,2.0){$\Sigma_{4}$} \put(47.0,30.5){$\Sigma_{5}$} \put(68.0,1.0){$\Sigma_{6}$} \put(67.0,55.0){$D_{1}$} \put(28.0,55.0){$D_{2}$} \put(14.0,15.0){$D_{3}$} \put(27.0,30.0){$D_{4}$} \put(68.0,30.0){$D_{5}$} \put(82.0,15.0){$D_{6}$} \end{overpic} Figure 3: Illustration of the Dulac maps of a polycycle Γ \Gamma.

For the remainder of this paper, we denote with a superscript the index of which Dulac map with which we are working, i.e. Δ j ​ k i \Delta_{jk}^{i} and S j i S_{j}^{i} denotes the coefficient Δ j ​ k \Delta_{jk} and quantity S j S_{j} in the Dulac map D i ​ ( s, μ) D_{i}(s,\mu).

For a point in position s s at Σ 1 \Sigma_{1}, we define the return map of Γ \Gamma by

 | ℛ ( s; μ) = D n ∘ ⋯ ∘ D 1 ( s; μ). \mathscr{R}(s;\mu)=D_{n}\circ\cdots\circ D_{1}(s;\mu). |  |

Thus, it is essential to understand the composition of Dulac maps to investigate the cyclicity as isolated fixed points of ℛ \mathscr{R} correspond to limit cycles.

### 4.1 Composition of Dulac maps

In this section we study the composition of Dulac maps. For our first result, we observe that from Theorem 1 we have that the leading term of a Dulac map does not depend on the sign of λ i 0 − 1 \lambda_{i}^{0}-1 (it could even be zero).

###### Lemma 4.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1 p_{1} and p 2 p_{2} and consider μ 0 ∈ Λ \mu_{0}\in\Lambda. Then for any given ℓ ∈ ( 0, min ⁡ { 1, λ 1 0, λ 1 0 ​ λ 2 0 }) \ell\in(0,\min\{1,\lambda_{1}^{0},\lambda_{1}^{0}\lambda_{2}^{0}\}) it holds

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Υ 0 + ℱ ℓ ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where Υ 0 = ( Δ 00 1) λ 2 ​ Δ 00 2 \Upsilon_{0}=(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2}.

###### Proof.

Let ℓ ∈ ( 0, min ⁡ { 1, λ 1 0, λ 1 0 ​ λ 2 0 }) \ell\in(0,\min\{1,\lambda_{1}^{0},\lambda_{1}^{0}\lambda_{2}^{0}\}). From Theorem 1 we have (even if λ 1 0 = 1 \lambda_{1}^{0}=1 or λ 2 0 = 1 \lambda_{2}^{0}=1) that

 | D 1 ​ ( s, μ) = s λ 1 ​ ( Δ 00 1 + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( Δ 00 2 + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

for any given ℓ 1 ∈ ( 0, min ⁡ { 1, λ 1 0 }) \ell_{1}\in(0,\min\{1,\lambda_{1}^{0}\}) and ℓ 2 ∈ ( 0, min ⁡ { 1, λ 2 0 }) \ell_{2}\in(0,\min\{1,\lambda_{2}^{0}\}). Observe that

 | D 2 ∘ D 1 ​ ( s, μ) = D 2 ​ ( s λ 1 ​ ( Δ 00 1 + ℱ ℓ 1 ∞ ​ ( μ 0))) = s λ 1 ​ λ 2 ​ ( Δ 00 1 + ℱ ℓ 1 ∞ ​ ( μ 0)) λ 2 ​ ( Δ 00 2 + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + ℱ ℓ 1 ∞ ​ ( μ 0)) ​ ( Δ 00 2 + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 ​ Δ 00 2 + Δ 00 2 ​ ℱ ℓ 1 ∞ ​ ( μ 0) + ( Δ 00 1) λ 2 ​ ℱ ℓ 3 ∞ ​ ( μ 0) + ℱ ℓ 1 ∞ ​ ( μ 0) ​ ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 ​ Δ 00 2 + ℱ ℓ 1 ∞ ​ ( μ 0) + ℱ ℓ 3 ∞ ​ ( μ 0) + ℱ ℓ 1 + ℓ 3 ∞ ​ ( μ 0) ⏟ ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 ​ Δ 00 2 + ℱ ℓ 1 ∞ ​ ( μ 0) + ℱ ℓ 3 ∞ ​ ( μ 0)), \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)=D_{2}\bigl(s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigr)\\ \quad=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigl(\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad\quad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2}+\Delta_{00}^{2}\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})+(\Delta_{00}^{1})^{\lambda_{2}}\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \ \par\qquad\qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})+\underbrace{\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})+\mathcal{F}^{\infty}_{\ell_{1}+\ell_{3}}(\mu_{0})}_{\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})}\bigr)\\ \qquad\qquad\quad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr),\end{array} |  |

with ℓ 3 = λ 1 0 ​ ℓ 2 \ell_{3}=\lambda_{1}^{0}\ell_{2} following from Lemma 1 (h), the third equality following from Lemma 2 (with a = 0 a=0), the fifth equality following from Lemma 1 (g) and the last equality following from Lemma 1 (d). It now follows from Lemma 1 (d,e) that

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 ​ Δ 00 2 + ℱ ℓ 4 ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s,\mu)=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr), |  |

for any given ℓ 4 ∈ ( 0, min ⁡ { ℓ 1, ℓ 3 }) \ell_{4}\in(0,\min\{\ell_{1},\ell_{3}\}). Since we can choose from the beginning any ℓ 2 ∈ ( 0, min ⁡ { 1, λ 2 0 }) \ell_{2}\in(0,\min\{1,\lambda_{2}^{0}\}), it follows that we can take any ℓ 3 ∈ ( 0, min ⁡ { λ 1 0, λ 1 0 ​ λ 2 0 }) \ell_{3}\in(0,\min\{\lambda_{1}^{0},\lambda_{1}^{0}\lambda_{2}^{0}\}). This in addition with the fact that we can choose ℓ 1 ∈ ( 0, min ⁡ { 1, λ 1 0 }) \ell_{1}\in(0,\min\{1,\lambda_{1}^{0}\}) freely implies that we can also choose ℓ 4 ∈ ( 0, min ⁡ { 1, λ 1 0, λ 1 0 ​ λ 2 0 }) \ell_{4}\in(0,\min\{1,\lambda_{1}^{0},\lambda_{1}^{0}\lambda_{2}^{0}\}) freely. In particular, we can take ℓ 4 = ℓ \ell_{4}=\ell. ∎

In the next result we apply induction on Lemma 4 to obtain a general formula for the composition of n n Dulac maps. To this end, we recall that

 | A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1, Λ i, k 0 = Λ i, k ​ ( μ 0). A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\quad\Lambda_{kk}=1,\quad\Lambda_{i,k}^{0}=\Lambda_{i,k}(\mu_{0}). |  |

###### Corollary 1.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n} and consider μ 0 ∈ Λ \mu_{0}\in\Lambda. Then for any given ℓ ∈ ( 0, min ⁡ { Λ 0, i 0: i ∈ { 0, …, n } }) \ell\in(0,\min\{\Lambda_{0,i}^{0}\colon i\in\{0,\dots,n\}\}) it holds

 | D n ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, n ​ ( A 1, n + ℱ ℓ ∞ ​ ( μ 0)). D_{n}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n}}\bigl(A_{1,n}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr). |  | (11) |

###### Proof.

For simplicity we write,

 | D 1 ​ ( s, μ) = s λ 1 ​ ( a 1 + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( a 2 + ℱ ℓ 2 ∞ ​ ( μ 0)). D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(a_{1}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(a_{2}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr). |  |

It follows from Lemma 4 that

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( a 1 λ 2 ​ a 2 + ℱ ℓ 1, 2 ∞ ​ ( μ 0)) = s Λ 0, 2 ​ ( A 1, 2 + ℱ ℓ 1, 2 ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(a_{1}^{\lambda_{2}}a_{2}+\mathcal{F}^{\infty}_{\ell_{1,2}}(\mu_{0})\bigr)=s^{\Lambda_{0,2}}(A_{1,2}+\mathcal{F}^{\infty}_{\ell_{1,2}}(\mu_{0})\bigr), |  |

for any given ℓ 1, 2 ∈ ( 0, min ⁡ { 1, λ 1 0, λ 2 0 }) \ell_{1,2}\in(0,\min\{1,\lambda_{1}^{0},\lambda_{2}^{0}\}). Suppose that

 | D n − 1 ∘ ⋯ ∘ D 1 ​ ( s, μ) = s Λ 0, n − 1 ​ ( A 1, n − 1 + ℱ ℓ 1, n − 1 ∞ ​ ( μ 0)), D_{n-1}\circ\dots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n-1}}\bigl(A_{1,n-1}+\mathcal{F}^{\infty}_{\ell_{1,n-1}}(\mu_{0})\bigr), |  | (12) |

and let

 | D n ​ ( s, μ) = s λ n ​ ( a n + ℱ ℓ n ∞ ​ ( μ 0)), D_{n}(s;\mu)=s^{\lambda_{n}}(a_{n}+\mathcal{F}^{\infty}_{\ell_{n}}(\mu_{0})\bigr), |  |

for any given ℓ 1, n − 1 ∈ ( 0, min ⁡ { Λ 0, i 0: i ∈ { 0, …, n − 1 } }) \ell_{1,n-1}\in(0,\min\{\Lambda_{0,i}^{0}\colon i\in\{0,\dots,n-1\}\}) and ℓ n ∈ ( 0, min ⁡ { 1, λ n 0 }) \ell_{n}\in(0,\min\{1,\lambda_{n}^{0}\}). Since ( 12) is also of Dulac-type, from Lemma 4 we have that

 | D n ∘ ( D n − 1 ∘ ⋯ ∘ D 1) ​ ( s, μ) = ( A 1, n − 1 λ n ​ a n + ℱ ℓ 1, n ∞ ​ ( μ 0)) = ( A 1, n + ℱ ℓ 1, n ∞ ​ ( μ 0)), D_{n}\circ(D_{n-1}\circ\dots\circ D_{1})(s;\mu)=\bigl(A_{1,n-1}^{\lambda_{n}}a_{n}+\mathcal{F}^{\infty}_{\ell_{1,n}}(\mu_{0})\bigr)=\bigl(A_{1,n}+\mathcal{F}^{\infty}_{\ell_{1,n}}(\mu_{0})\bigr), |  |

for any given ℓ 1, n ∈ ( 0, min ⁡ { Λ 0, i 0: i ∈ { 0, …, n } }) \ell_{1,n}\in(0,\min\{\Lambda_{0,i}^{0}\colon i\in\{0,\dots,n\}\}). The proof now follows by induction. ∎

We observe that formulas similar to ( 11) were already obtained in the literature. See [11, p. 726 726] and [14, p. 12 12]. Nevertheless, as far as we know the explicit interval associated with ℓ \ell is a new result.

In the following results we shall include the next term of the Dulac maps in the computation. We recall that from Theorem 1 it follows that such a term depend on the sign of λ i 0 − 1 \lambda_{i}^{0}-1. Hence, the compositions must be studied in a case-by-case scenario. Moreover, different from the previous results, from now on in this section we shall assume λ 1 0 ≠ 1 \lambda_{1}^{0}\neq 1 and λ 2 0 ≠ 1 \lambda_{2}^{0}\neq 1 for simplicity.

###### Lemma 5.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1 p_{1} and p 2 p_{2}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 1 0 > 1 \lambda_{1}^{0}>1 and λ 2 0 > 1 \lambda_{2}^{0}>1. Then for any given ℓ ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell\in(1,\min\{\lambda_{1}^{0},2\}) it holds

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 1 ​ s + ℱ ℓ ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{1}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where Υ 0 = ( Δ 00 1) λ 2 ​ Δ 00 2 \Upsilon_{0}=(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2} and Υ 1 = λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 00 2 ​ Δ 10 1 \Upsilon_{1}=\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{00}^{2}\Delta_{10}^{1}.

###### Proof.

Let ℓ ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell\in(1,\min\{\lambda_{1}^{0},2\}). Since λ 1 0 > 1 \lambda_{1}^{0}>1 and λ 2 0 > 1 \lambda_{2}^{0}>1, from Theorem 1 we have that

 | D 1 ​ ( s, μ) = s λ 1 ​ ( Δ 00 1 + Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( Δ 00 2 + Δ 10 2 ​ s + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}s+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

for any given ℓ 1 ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell_{1}\in(1,\min\{\lambda_{1}^{0},2\}) and ℓ 2 ∈ ( 1, min ⁡ { λ 2 0, 2 }) \ell_{2}\in(1,\min\{\lambda_{2}^{0},2\}). In particular, for any given ℓ 1 ∈ ( ℓ, min ⁡ { λ 1 0, 2 }) \ell_{1}\in(\ell,\min\{\lambda_{1}^{0},2\}). Observe that

 | D 2 ∘ D 1 ​ ( s, μ) = D 2 ​ ( s λ 1 ​ ( Δ 00 1 + Δ 10 1 + ℱ ℓ 1 ∞ ​ ( μ 0))) = s λ 1 ​ λ 2 ​ ( Δ 00 1 + Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) λ 2 ​ ( Δ 00 2 + Δ 10 2 ​ s λ 1 ​ ( Δ 00 1 + Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) + ℱ ℓ 3 ∞ ​ ( μ 0)), \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)=D_{2}\bigl(s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigr)\\ \quad=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr),\end{array} |  | (13) |

with ℓ 3 = λ 1 0 ​ ℓ 2 \ell_{3}=\lambda_{1}^{0}\ell_{2} following from Lemma 1 (h). Observe that ℓ 3 > λ 1 0 \ell_{3}>\lambda_{1}^{0}. Applying Lemma 2 at ( 13) we obtain

 | s λ 1 ​ λ 2 ( ( Δ 00 1) λ 2 + λ 2 ( Δ 00 1) λ 2 − 1 Δ 10 1 s + ℱ ∞ ℓ 1 ( μ 0)) ⋅ ⋅ ( Δ 00 2 + Δ 10 2 ​ Δ 00 1 ​ s λ 1 + Δ 10 2 ​ Δ 10 1 ​ s λ 1 + 1 + Δ 10 2 ​ s λ 1 ​ ℱ ℓ 1 ∞ ​ ( μ 0) + ℱ ℓ 3 ∞ ​ ( μ 0) ⏟ ℱ ℓ 4 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) ​ ( Δ 00 2 + Δ 10 2 ​ Δ 00 1 ​ s λ 1 + ℱ ℓ 4 ∞ ​ ( μ 0)), \begin{array}[]{l}s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\cdot\\ \quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}\Delta_{00}^{1}s^{\lambda_{1}}+\underbrace{\Delta_{10}^{2}\Delta_{10}^{1}s^{\lambda_{1}+1}+\Delta_{10}^{2}s^{\lambda_{1}}\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})}_{\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})}\bigr)\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}\Delta_{00}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr),\end{array} |  | (14) |

for any given ℓ 4 ∈ ( λ 1 0, min ⁡ { 1 + λ 1 0, ℓ 1 + λ 1 0, ℓ 3 }) \ell_{4}\in(\lambda_{1}^{0},\min\{1+\lambda_{1}^{0},\ell_{1}+\lambda_{1}^{0},\ell_{3}\}), due to Lemma 1 (d,g). Expanding the last two factors of ( 14) we obtain

 | s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 + λ 2 ​ Δ 00 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 5 ∞ ​ ( μ 0)), s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{5}}(\mu_{0})\bigr), |  |

for any given

 | ℓ 5 ∈ ( 1, min ⁡ { λ 1 0, ℓ 4, 1 + λ 1 0, 1 + ℓ 4, ℓ 1, ℓ 1 + λ 1 0, ℓ 1 + ℓ 4 }) = ( 1, min ⁡ { λ 1 0, ℓ 1, ℓ 4 }) = ( 1, ℓ 1). \ell_{5}\in(1,\min\{\lambda_{1}^{0},\ell_{4},1+\lambda_{1}^{0},1+\ell_{4},\ell_{1},\ell_{1}+\lambda_{1}^{0},\ell_{1}+\ell_{4}\})=(1,\min\{\lambda_{1}^{0},\ell_{1},\ell_{4}\})=(1,\ell_{1}). |  |

In particular for ℓ 5 = ℓ \ell_{5}=\ell. ∎

###### Corollary 2.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i 0 > 1 \lambda_{i}^{0}>1 for i ∈ { 1, …, m } i\in\{1,\dots,m\}. Then for any given ℓ ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell\in(1,\min\{\lambda_{1}^{0},2\}) it holds

 | D n ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, n ​ ( A 1, n + B 1, n ​ s + ℱ ℓ ∞ ​ ( μ 0)), D_{n}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n}}\bigl(A_{1,n}+B_{1,n}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where

 | B j, k = Λ j, k ​ Δ 10 j Δ 00 j ​ A j, k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. B_{j,k}=\Lambda_{j,k}\frac{\Delta_{10}^{j}}{\Delta_{00}^{j}}A_{j,k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

###### Proof.

It follows from Lemma 5 that in this case the composition of Dulac maps is also of Dulac-type. Therefore the proof follows by induction. More precisely if for simplicity we write

 | D 1 ​ ( s, μ) = s λ 1 ​ ( a 1 + b 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( a 2 + b 2 ​ s + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(a_{1}+b_{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(a_{2}+b_{2}s+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

then it follows from Lemma 5 that,

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( a 1 λ 2 ​ a 2 + λ 2 ​ b 1 a 1 ​ ( a 1 λ 2 ​ a 2) ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) = s Λ 0, 2 ​ ( A 1, 2 + B 1, 2 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)). D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\left(a_{1}^{\lambda_{2}}a_{2}+\lambda_{2}\frac{b_{1}}{a_{1}}\bigl(a_{1}^{\lambda_{2}}a_{2}\bigr)s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\right)=s^{\Lambda_{0,2}}\bigl(A_{1,2}+B_{1,2}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr). |  |

Suppose therefore that

 | D n − 1 ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, n − 1 ​ ( A 1, n − 1 + B 1, n − 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D_{n-1}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n-1}}\bigl(A_{1,n-1}+B_{1,n-1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr), |  |

and let

 | D n ​ ( s, μ) = s λ n ​ ( a n + b n ​ s + ℱ ℓ n ∞ ​ ( μ 0)). D_{n}(s;\mu)=s^{\lambda_{n}}\bigl(a_{n}+b_{n}s+\mathcal{F}^{\infty}_{\ell_{n}}(\mu_{0})\bigr). |  |

From Lemma 5 we have that

 | D n ∘ ( D n − 1 ∘ … ∘ D 1) ​ ( s, μ) = s Λ 0, n − 1 ​ λ n ​ ( A 1, n − 1 λ n ​ a n + λ n ​ B 1, n − 1 A 1, n − 1 ​ ( A 1, n − 1 λ n ​ a n) ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) = s Λ 0, n ​ ( A 1, n + λ n ​ Λ 1, n − 1 ​ b 1 a 1 ​ A 1, n ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) = s Λ 0, n ​ ( A 1, n + B 1, n ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), \begin{array}[]{l}\displaystyle D_{n}\circ(D_{n-1}\circ\ldots\circ D_{1})(s;\mu)\\ \displaystyle\quad=s^{\Lambda_{0,n-1}\lambda_{n}}\left(A_{1,n-1}^{\lambda_{n}}a_{n}+\lambda_{n}\frac{B_{1,n-1}}{A_{1,n-1}}\bigl(A_{1,n-1}^{\lambda_{n}}a_{n}\bigr)s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\right)\\ \displaystyle\qquad=s^{\Lambda_{0,n}}\left(A_{1,n}+\lambda_{n}\Lambda_{1,n-1}\frac{b_{1}}{a_{1}}A_{1,n}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\right)\\ \displaystyle\qquad\quad=s^{\Lambda_{0,n}}\bigl(A_{1,n}+B_{1,n}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\end{array} |  |

proving the result. ∎

###### Lemma 6.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1 p_{1} and p 2 p_{2}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 1 0 < 1 \lambda_{1}^{0}<1 and λ 2 0 < 1 \lambda_{2}^{0}<1. Then for any given ℓ ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0, 2 ​ λ 1 0 ​ λ 2 0 }) \ell\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0},2\lambda_{1}^{0}\lambda_{2}^{0}\}) it holds

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 2 ​ s λ 1 ​ λ 2 + ℱ ℓ ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where Υ 0 = ( Δ 00 1) λ 2 ​ Δ 00 2 \Upsilon_{0}=(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2} and Υ 2 = ( Δ 00 1) 2 ​ λ 2 ​ Δ 01 2 \Upsilon_{2}=(\Delta_{00}^{1})^{2\lambda_{2}}\Delta_{01}^{2}.

###### Proof.

Let ℓ ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0, 2 ​ λ 1 0 ​ λ 2 0 }) \ell\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0},2\lambda_{1}^{0}\lambda_{2}^{0}\}). Since λ 1 0 < 1 \lambda_{1}^{0}<1 and λ 2 0 < 1 \lambda_{2}^{0}<1, from Theorem 1 we have that

 | D 1 ​ ( s, μ) = s λ 1 ​ ( Δ 00 1 + Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( Δ 00 2 + Δ 01 2 ​ s λ 2 + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\big), |  |

for any given ℓ 1 ∈ ( λ 1 0, min ⁡ { 2 ​ λ 1 0, 1 }) \ell_{1}\in(\lambda_{1}^{0},\min\{2\lambda_{1}^{0},1\}) and ℓ 2 ∈ ( λ 2 0, min ⁡ { 2 ​ λ 2 0, 1 }) \ell_{2}\in(\lambda_{2}^{0},\min\{2\lambda_{2}^{0},1\}). Similarly to Lemma 6 observe that

 | D 2 ∘ D 1 ( s; μ) = s λ 1 ​ λ 2 ( Δ 00 1 + Δ 01 1 s λ 1 + ℱ ∞ ℓ 1 ( μ 0)) λ 2 ⋅ ⋅ ( Δ 00 2 + Δ 01 2 ​ s λ 1 ​ λ 2 ​ ( Δ 00 1 + Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)) λ 2 + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ( ( Δ 00 1) λ 2 + λ 2 ( Δ 00 1) λ 2 − 1 Δ 01 1 s λ 1 + ℱ ∞ ℓ 1 ( μ 0)) ⋅ ⋅ ( Δ 00 2 + Δ 01 2 ​ s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)) + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)) ⋅ ( Δ 00 2 + ( Δ 00 1) λ 2 ​ Δ 01 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 4 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 + ( Δ 00 1) 2 ​ λ 2 ​ Δ 01 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 5 ∞ ​ ( μ 0)), \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}\cdot\\ \quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\cdot\\ \qquad\quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad\qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\\ \qquad\qquad\quad\cdot\bigl(\Delta_{00}^{2}+(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr)\\ \qquad\qquad\qquad=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}+(\Delta_{00}^{1})^{2\lambda_{2}}\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{5}}(\mu_{0})\bigr),\end{array} |  |

with ℓ 3 = λ 1 0 ​ ℓ 2 \ell_{3}=\lambda_{1}^{0}\ell_{2} and for any given ℓ 4 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0 ​ λ 2 0 + λ 1 0, ℓ 3 }) \ell_{4}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0}+\lambda_{1}^{0},\ell_{3}\}) and ℓ 5 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0, ℓ 4 }) \ell_{5}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0},\ell_{4}\}). Observe that the possibility to take any ℓ 2 ∈ ( λ 2 0, min ⁡ { 2 ​ λ 2 0, 1 }) \ell_{2}\in(\lambda_{2}^{0},\min\{2\lambda_{2}^{0},1\}) implies that we can take any ℓ 3 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { 2 ​ λ 1 0 ​ λ 2 0, λ 1 0 }) \ell_{3}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{2\lambda_{1}^{0}\lambda_{2}^{0},\lambda_{1}^{0}\}), which in turn implies that we can take any

 | ℓ 4 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0 ​ λ 2 0 + λ 1 0, 2 ​ λ 1 0 ​ λ 2 0, λ 1 0 }) = ( λ 1 0 ​ λ 2 0, min ⁡ { 2 ​ λ 1 0 ​ λ 2 0, λ 1 0 }). \ell_{4}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0}+\lambda_{1}^{0},2\lambda_{1}^{0}\lambda_{2}^{0},\lambda_{1}^{0}\})=(\lambda_{1}^{0}\lambda_{2}^{0},\min\{2\lambda_{1}^{0}\lambda_{2}^{0},\lambda_{1}^{0}\}). |  |

This in turn implies that we can take any ℓ 5 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0, 2 ​ λ 1 0 ​ λ 2 0 }) \ell_{5}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0},2\lambda_{1}^{0}\lambda_{2}^{0}\}). In particular, we can take ℓ 5 = ℓ \ell_{5}=\ell. ∎

###### Corollary 3.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i 0 < 1 \lambda_{i}^{0}<1 for i ∈ { 1, …, n } i\in\{1,\dots,n\}. Then for any given ℓ ∈ ( Λ 0, n 0, min ⁡ { Λ 0, n − 1 0, 2 ​ Λ 0, n 0 }) \ell\in(\Lambda_{0,n}^{0},\min\{\Lambda_{0,n-1}^{0},2\Lambda_{0,n}^{0}\}) it holds

 | D n ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, n ​ ( A 1, n + C 1, n ​ s Λ 0, n + ℱ ℓ ∞ ​ ( μ 0)), D_{n}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n}}\bigl(A_{1,n}+C_{1,n}s^{\Lambda_{0,n}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where

 | C j, k = A j, k − 1 2 ​ λ k ​ Δ 01 k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. C_{j,k}=A_{j,k-1}^{2\lambda_{k}}\Delta_{01}^{k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

###### Proof.

Similarly to the proof of Corollary 2, observe that if for simplicity we write

 | D 1 ​ ( s, μ) = s λ 1 ​ ( a 1 + c 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( a 2 + c 2 ​ s λ 2 + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(a_{1}+c_{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(a_{2}+c_{2}s^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

then from Lemma 6 we have

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( a 1 λ 2 ​ a 2 + a 1 2 ​ λ 2 ​ c 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 1, 2 ∞ ​ ( μ 0)) = s Λ 0, 2 ​ ( A 1, 2 + C 1, 2 ​ s Λ 0, 2 + ℱ ℓ 1, 2 ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(a_{1}^{\lambda_{2}}a_{2}+a_{1}^{2\lambda_{2}}c_{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{1,2}}(\mu_{0})\bigr)=s^{\Lambda_{0,2}}\bigl(A_{1,2}+C_{1,2}s^{\Lambda_{0,2}}+\mathcal{F}^{\infty}_{\ell_{1,2}}(\mu_{0})\bigr), |  |

for any ℓ 1, 2 ∈ ( Λ 0, 2 0, min ⁡ { Λ 0, 1 0, 2 ​ Λ 0, 2 0 }) \ell_{1,2}\in(\Lambda_{0,2}^{0},\min\{\Lambda_{0,1}^{0},2\Lambda_{0,2}^{0}\}). Suppose that

 | D n − 1 ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, n − 1 ​ ( A 1, n − 1 + C 1, n − 1 ​ s Λ 0, n − 1 + ℱ ℓ n − 1 ∞ ​ ( μ 0)), D_{n-1}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,n-1}}\bigl(A_{1,n-1}+C_{1,n-1}s^{\Lambda_{0,n-1}}+\mathcal{F}^{\infty}_{\ell_{n-1}}(\mu_{0})\big), |  |

with ℓ n − 1 ∈ ( Λ 0, n − 1 0, min ⁡ { Λ 0, n − 2 0, 2 ​ Λ 0, n − 1 0 }) \ell_{n-1}\in(\Lambda_{0,n-1}^{0},\min\{\Lambda_{0,n-2}^{0},2\Lambda_{0,n-1}^{0}\}) and let

 | D n ​ ( s, μ) = s λ n ​ ( a n + c n ​ s λ n + ℱ ℓ n ∞ ​ ( μ 0)). D_{n}(s;\mu)=s^{\lambda_{n}}\bigl(a_{n}+c_{n}s^{\lambda_{n}}+\mathcal{F}^{\infty}_{\ell_{n}}(\mu_{0})\bigr). |  |

From Lemma 6 we have

 | D n ∘ ( D n − 1 ∘ … ∘ D 1) ​ ( s, μ) = s Λ 0, n − 1 ​ λ n ​ ( A 1, n − 1 λ n ​ a n + A 1, n − 1 2 ​ λ n ​ c n ​ s Λ 0, n − 1 ​ λ n + ℱ ℓ 1, n ∞ ​ ( μ 0)) = s Λ 0, n ​ ( A 1, n + C 1, n ​ s Λ 0, n + ℱ ℓ 1, n ∞ ​ ( μ 0)), \begin{array}[]{ll}D_{n}\circ(D_{n-1}\circ\ldots\circ D_{1})(s;\mu)&=s^{\Lambda_{0,n-1}\lambda_{n}}\bigl(A_{1,n-1}^{\lambda_{n}}a_{n}+A_{1,n-1}^{2\lambda_{n}}c_{n}s^{\Lambda_{0,n-1}\lambda_{n}}+\mathcal{F}^{\infty}_{\ell_{1,n}}(\mu_{0})\bigr)\\ &=s^{\Lambda_{0,n}}\bigl(A_{1,n}+C_{1,n}s^{\Lambda_{0,n}}+\mathcal{F}^{\infty}_{\ell_{1,n}}(\mu_{0})\bigr),\end{array} |  |

with ℓ 1, n ∈ ( Λ 0, n 0 ​ min ⁡ { Λ 0, n − 1 0, 2 ​ Λ 0, n 0 }) \ell_{1,n}\in(\Lambda_{0,n}^{0}\min\{\Lambda_{0,n-1}^{0},2\Lambda_{0,n}^{0}\}). The result now follows by induction. ∎

###### Lemma 7.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1 p_{1} and p 2 p_{2}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 1 0 > 1 \lambda_{1}^{0}>1 and λ 2 0 < 1 \lambda_{2}^{0}<1. Then

 | D 2 ∘ D 1 ​ ( s, μ) = { s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 1 ​ s + ℱ ℓ ∞ ​ ( μ 0)), if ​ λ 1 0 ​ λ 2 0 > 1, s λ 1 ​ λ 2 ​ ( Υ 0 + Υ ω ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ λ 1 0 ​ λ 2 0 = 1, s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 2 ​ s λ 1 ​ λ 2 + ℱ ℓ ′′ ∞ ​ ( μ 0)), if ​ λ 1 0 ​ λ 2 0 < 1, D_{2}\circ D_{1}(s;\mu)=\left\{\begin{array}[]{ll}s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{1}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),&\text{if }\lambda_{1}^{0}\lambda_{2}^{0}>1,\\ s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{\omega}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }\lambda_{1}^{0}\lambda_{2}^{0}=1,\\ s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell^{\prime\prime}}(\mu_{0})\bigr),&\text{if }\lambda_{1}^{0}\lambda_{2}^{0}<1,\end{array}\right. |  |

for any given

 | ℓ ∈ ( 1, min ⁡ { λ 1 0 ​ λ 2 0, 2 }), ℓ ′ ∈ ( 1, min ⁡ { λ 1 0, 2 }), ℓ ′′ ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { 2 ​ λ 1 0 ​ λ 2 0, 1 }); \ell\in(1,\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\}),\quad\ell^{\prime}\in(1,\min\{\lambda_{1}^{0},2\}),\quad\ell^{\prime\prime}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{2\lambda_{1}^{0}\lambda_{2}^{0},1\}); |  |

where

 | Υ 0 = ( Δ 00 1) λ 2 ​ Δ 00 2, Υ 1 = λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 00 2 ​ Δ 10 1, Υ 2 = ( Δ 00 1) 2 ​ λ 2 ​ Δ 01 2, \Upsilon_{0}=(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2},\quad\Upsilon_{1}=\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{00}^{2}\Delta_{10}^{1},\quad\Upsilon_{2}=(\Delta_{00}^{1})^{2\lambda_{2}}\Delta_{01}^{2}, |  |

Υ ω = Υ 1 + ( 1 + α ​ ω ​ ( s, α)) ​ Υ 2 \Upsilon_{\omega}=\Upsilon_{1}+\bigl(1+\alpha\omega(s;\alpha)\bigr)\Upsilon_{2} and α = 1 − λ 1 ​ λ 2 \alpha=1-\lambda_{1}\lambda_{2}.

###### Proof.

Since λ 1 0 > 1 \lambda_{1}^{0}>1 and λ 2 0 < 1 \lambda_{2}^{0}<1, from Theorem 1 we have that

 | D 1 ​ ( s, μ) = s λ 1 ​ ( Δ 00 1 + Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( Δ 00 2 + Δ 01 2 ​ s λ 2 + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

for any given ℓ 1 ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell_{1}\in(1,\min\{\lambda_{1}^{0},2\}) and ℓ 2 ∈ ( λ 2 0, min ⁡ { 2 ​ λ 2 0, 1 }) \ell_{2}\in(\lambda_{2}^{0},\min\{2\lambda_{2}^{0},1\}). Similarly Lemmas 5 and 6 observe that

 | D 2 ∘ D 1 ( s; μ) = s λ 1 ​ λ 2 ( Δ 00 1 + Δ 10 1 s + ℱ ∞ ℓ 1 ( μ 0)) λ 2 ⋅ ⋅ ( Δ 00 2 + Δ 01 2 ​ s λ 1 ​ λ 2 ​ ( Δ 00 1 + Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) λ 2 + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ( ( Δ 00 1) λ 2 + λ 2 ( Δ 00 1) λ 2 − 1 Δ 10 1 s + ℱ ∞ ℓ 1 ( μ 0)) ⋅ ⋅ ( Δ 00 2 + Δ 01 2 ​ s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) ​ ( Δ 00 2 + ( Δ 00 1) λ 2 ​ Δ 01 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 4 ∞ ​ ( μ 0)). \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}\cdot\\ \quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\cdot\\ \qquad\quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad\qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigl(\Delta_{00}^{2}+(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr).\end{array} |  |

with ℓ 3 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { 2 ​ λ 1 0 ​ λ 2 0, λ 1 0 }) \ell_{3}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{2\lambda_{1}^{0}\lambda_{2}^{0},\lambda_{1}^{0}\}) and

 | ℓ 4 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0 ​ λ 2 0 + 1, ℓ 3 }) = ( λ 1 0 ​ λ 2 0, min ⁡ { λ 1 0 ​ λ 2 0 + 1, 2 ​ λ 1 0 ​ λ 2 0, λ 1 0 }). \ell_{4}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0}+1,\ell_{3}\})=(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0}+1,2\lambda_{1}^{0}\lambda_{2}^{0},\lambda_{1}^{0}\}). |  |

So far we have proved that D 2 ∘ D 1 ​ ( s, μ) D_{2}\circ D_{1}(s;\mu) can be expressed as,

 | s λ 1 ​ λ 2 ​ ( ( Δ 00 1) λ 2 + λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) ​ ( Δ 00 2 + ( Δ 00 1) λ 2 ​ Δ 01 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 4 ∞ ​ ( μ 0)). s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\bigl(\Delta_{00}^{2}+(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr). |  | (15) |

However we cannot expand these last two factors in a unique way because the next term after the leading one depend on the sign of 1 − λ 1 0 ​ λ 2 0 1-\lambda_{1}^{0}\lambda_{2}^{0}. Hence we need to continue in a case-by-case basis.

If λ 1 0 ​ λ 2 0 > 1 \lambda_{1}^{0}\lambda_{2}^{0}>1 then we can expand ( 15) in to

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 + λ 2 ​ Δ 00 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ​ s + ℱ ℓ 5 ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}s+\mathcal{F}^{\infty}_{\ell_{5}}(\mu_{0})\bigr), |  | (16) |

for any given ℓ 5 ∈ ( 1, min ⁡ { λ 1 0 ​ λ 2 0, ℓ 1, ℓ 4 }) = ( 1, min ⁡ { λ 1 ​ λ 2, 2 }) \ell_{5}\in(1,\min\{\lambda_{1}^{0}\lambda_{2}^{0},\ell_{1},\ell_{4}\})=(1,\min\{\lambda_{1}\lambda_{2},2\}).

If λ 1 0 ​ λ 2 0 < 1 \lambda_{1}^{0}\lambda_{2}^{0}<1 then we can expand ( 15) in to

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 + ( Δ 00 1) 2 ​ λ 2 ​ Δ 01 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 6 ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}+(\Delta_{00}^{1})^{2\lambda_{2}}\Delta_{01}^{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{6}}(\mu_{0})\bigr), |  | (17) |

for any given ℓ 6 ∈ ( λ 1 0 ​ λ 2 0, min ⁡ { ℓ 1, ℓ 4, 1 }) = ( λ 1 0 ​ λ 2 0, min ⁡ { 2 ​ λ 1 0 ​ λ 2 0, 1 }) \ell_{6}\in(\lambda_{1}^{0}\lambda_{2}^{0},\min\{\ell_{1},\ell_{4},1\})=(\lambda_{1}^{0}\lambda_{2}^{0},\min\{2\lambda_{1}^{0}\lambda_{2}^{0},1\}).

If λ 1 0 ​ λ 2 0 = 1 \lambda_{1}^{0}\lambda_{2}^{0}=1 then let α = 1 − λ 1 ​ λ 2 \alpha=1-\lambda_{1}\lambda_{2} and observe that

 | s − α = 1 + α ​ ω ​ ( s, α), s^{-\alpha}=1+\alpha\omega(s;\alpha), |  | (18) |

where we recall that ω ⁡ ( s, α) \omega(s;\alpha) is the Écalle–Roussarie compensator ( 9). Since λ 1 0 ​ λ 2 0 = 1 \lambda_{1}^{0}\lambda_{2}^{0}=1 it follows that we cannot isolate the monomials of s 1 s^{1} and s λ 1 ​ λ 2 s^{\lambda_{1}\lambda_{2}} from each other, as in ( 16) and ( 17). Hence we expand ( 15) in to

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 ⏟ Υ 0 + λ 2 ​ Δ 00 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 10 1 ⏟ Υ 1 ​ s + ( Δ 00 1) 2 ​ λ 2 ​ Δ 01 2 ⏟ Υ 2 ​ s λ 1 ​ λ 2 + ℱ ℓ 7 ∞ ​ ( μ 0)), = s λ 1 ​ λ 2 ​ ( Υ 0 + ( Υ 1 + Υ 2 ​ s − α) ​ s + ℱ ℓ 6 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( Υ 0 + ( Υ 1 + Υ 2 ​ ( 1 + α ​ ω ​ ( s, α)) ​ s + ℱ ℓ 7 ∞ ​ ( μ 0)) CLOSE = s λ 1 ​ λ 2 ​ ( Υ 0 + Υ ω ​ s + ℱ ℓ 7 ∞ ​ ( μ 0)), \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)\\ \quad=s^{\lambda_{1}\lambda_{2}}\bigl(\underbrace{\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}}_{\Upsilon_{0}}+\underbrace{\lambda_{2}\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{10}^{1}}_{\Upsilon_{1}}s+\underbrace{(\Delta_{00}^{1})^{2\lambda_{2}}\Delta_{01}^{2}}_{\Upsilon_{2}}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell_{7}}(\mu_{0})\bigr),\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+(\Upsilon_{1}+\Upsilon_{2}s^{-\alpha})s+\mathcal{F}^{\infty}_{\ell_{6}}(\mu_{0})\bigr)\\ \qquad\quad=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\bigl(\Upsilon_{1}+\Upsilon_{2}(1+\alpha\omega(s;\alpha)\bigr)s+\mathcal{F}^{\infty}_{\ell_{7}}(\mu_{0})\bigr)\\ \qquad\qquad=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{\omega}s+\mathcal{F}^{\infty}_{\ell_{7}}(\mu_{0})\bigr),\end{array} |  | (19) |

with ℓ 7 ∈ ( 1, min ⁡ { ℓ 1, ℓ 4, λ 1 0 ​ λ 2 0 + 1 }) = ( 1, min ⁡ { λ 1 0, 2 }) \ell_{7}\in(1,\min\{\ell_{1},\ell_{4},\lambda_{1}^{0}\lambda_{2}^{0}+1\})=(1,\min\{\lambda_{1}^{0},2\}) and the last third due to ( 18). The lemma now follows from ( 16), ( 17) and ( 19). ∎

###### Remark 2.

Under the hypothesis of Lemma 7 we observe that the compensator ω ⁡ ( s, α) \omega(s;\alpha) appearing when λ 1 0 ​ λ 2 0 = 1 \lambda_{1}^{0}\lambda_{2}^{0}=1 is a compact way to write D 2 ∘ D 1 D_{2}\circ D_{1} in this case. More precisely suppose λ 1 0 ​ λ 2 0 = 1 \lambda_{1}^{0}\lambda_{2}^{0}=1 and observe that given λ 1 ≈ λ 1 0 \lambda_{1}\approx\lambda_{1}^{0} and λ 2 ≈ λ 2 0 \lambda_{2}\approx\lambda_{2}^{0} we have α = 0 \alpha=0 if and only if λ 1 ​ λ 2 = 1 \lambda_{1}\lambda_{2}=1. Moreover if λ 1 ​ λ 2 ≠ 1 \lambda_{1}\lambda_{2}\neq 1 then it follows from ( 18) that ( 1 + α ​ ω ​ ( s, α)) ​ s = s λ 1 ​ λ 2 (1+\alpha\omega(s;\alpha))s=s^{\lambda_{1}\lambda_{2}}. Replacing this at ( 19) we obtain that if λ 1 0 ​ λ 1 0 = 1 \lambda_{1}^{0}\lambda_{1}^{0}=1, then

 | D 2 ∘ D 1 ​ ( s, μ) = { s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 1 ​ s + Υ 2 ​ s λ 1 ​ λ 2 + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ λ 1 ​ λ 2 > 1, s ⋅ ( Υ 0 + ( Υ 1 + Υ 2) ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ λ 1 ​ λ 2 = 1, s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 2 ​ s λ 1 ​ λ 2 + Υ 1 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ λ 1 ​ λ 2 < 1. D_{2}\circ D_{1}(s;\mu)=\left\{\begin{array}[]{ll}s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{1}s+\Upsilon_{2}s^{\lambda_{1}\lambda_{2}}+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }\lambda_{1}\lambda_{2}>1,\\ s\cdot\bigl(\Upsilon_{0}+(\Upsilon_{1}+\Upsilon_{2})s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }\lambda_{1}\lambda_{2}=1,\\ s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{2}s^{\lambda_{1}\lambda_{2}}+\Upsilon_{1}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }\lambda_{1}\lambda_{2}<1.\end{array}\right. |  | (20) |

That is, the next term after the leading one depend on the sign of 1 − λ 1 ​ λ 2 1-\lambda_{1}\lambda_{2}. Since the initial condition satisfies λ 1 0 ​ λ 2 0 = 1 \lambda_{1}^{0}\lambda_{2}^{0}=1 we have that the explicit expression of D 2 ∘ D 1 D_{2}\circ D_{1} can change with arbitrarily small perturbations at the initial condition. Therefore, to understand the regularity of the compensator ω ⁡ ( s, μ) \omega(s;\mu) helps to understand the regularity of D 2 ∘ D 1 D_{2}\circ D_{1} when interchanging among the explicit expressions given at ( 20). To this end, we refer to Lemma A ​.3 A.3 and Corollary A ​.7 A.7 of [10].

###### Lemma 8.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1 p_{1} and p 2 p_{2}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 1 0 < 1 \lambda_{1}^{0}<1 and λ 2 0 > 1 \lambda_{2}^{0}>1. Then for any given ℓ ∈ ( λ 1 0, min ⁡ { λ 1 0 ​ λ 2 0, 2 ​ λ 1 0, 1 }) \ell\in(\lambda_{1}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\lambda_{1}^{0},1\}) it holds

 | D 2 ∘ D 1 ​ ( s, μ) = s λ 1 ​ λ 2 ​ ( Υ 0 + Υ 3 ​ s λ 1 + ℱ ℓ ∞ ​ ( μ 0)), D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Upsilon_{0}+\Upsilon_{3}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  |

where Υ 0 = ( Δ 00 1) λ 2 ​ Δ 00 2 \Upsilon_{0}=(\Delta_{00}^{1})^{\lambda_{2}}\Delta_{00}^{2} and Υ 3 = λ 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 00 2 ​ Δ 01 1 + ( Δ 00 1) λ 2 + 1 ​ Δ 10 2 \Upsilon_{3}=\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{00}^{2}\Delta_{01}^{1}+(\Delta_{00}^{1})^{\lambda_{2}+1}\Delta_{10}^{2}.

###### Proof.

Let ℓ ∈ ( λ 1 0, min ⁡ { λ 1 0 ​ λ 2 0, 2 ​ λ 1 0, 1 }) \ell\in(\lambda_{1}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\lambda_{1}^{0},1\}). Since λ 1 0 < 1 \lambda_{1}^{0}<1 and λ 2 0 > 1 \lambda_{2}^{0}>1, from Theorem 1 we have that

 | D 1 ​ ( s, μ) = s λ 1 ​ ( Δ 00 1 + Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)), D 2 ​ ( s, μ) = s λ 2 ​ ( Δ 00 2 + Δ 10 2 ​ s + ℱ ℓ 2 ∞ ​ ( μ 0)), D_{1}(s;\mu)=s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr),\quad D_{2}(s;\mu)=s^{\lambda_{2}}\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}s+\mathcal{F}^{\infty}_{\ell_{2}}(\mu_{0})\bigr), |  |

for any given ℓ 1 ∈ ( λ 1 0, min ⁡ { 2 ​ λ 1 0, 1 }) \ell_{1}\in(\lambda_{1}^{0},\min\{2\lambda_{1}^{0},1\}) and ℓ 2 ∈ ( 1, min ⁡ { λ 2 0, 2 }) \ell_{2}\in(1,\min\{\lambda_{2}^{0},2\}). Similarly to the previous cases we observe that

 | D 2 ∘ D 1 ( s; μ) = s λ 1 ​ λ 2 ( Δ 00 1 + Δ 01 1 s λ 1 + ℱ ∞ ℓ 1 ( μ 0)) λ 2 ⋅ ⋅ ( Δ 00 2 + Δ 10 2 ​ s λ 1 ​ ( Δ 00 1 + Δ 01 1 ​ s λ 1 + ℱ ℓ 1 ∞ ​ ( μ 0)) + ℱ ℓ 3 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ( ( Δ 00 1) λ 2 + λ 2 ( Δ 00 1) λ 2 − 1 Δ 01 1 s λ 1 + ℱ ∞ ℓ 1 ( μ 0)) ⋅ ⋅ ( Δ 00 2 + Δ 00 1 ​ Δ 10 2 ​ s λ 1 + ℱ ℓ 4 ∞ ​ ( μ 0)) = s λ 1 ​ λ 2 ​ ( Δ 00 2 ​ ( Δ 00 1) λ 2 + ( λ 2 ​ Δ 00 2 ​ ( Δ 00 1) λ 2 − 1 ​ Δ 01 1 + ( Δ 00 1) λ 2 + 1 ​ Δ 10 2) ​ s λ 1 + ℱ ℓ 5 ∞ ​ ( μ 0)), \begin{array}[]{l}D_{2}\circ D_{1}(s;\mu)=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)^{\lambda_{2}}\cdot\\ \quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{10}^{2}s^{\lambda_{1}}\bigl(\Delta_{00}^{1}+\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)+\mathcal{F}^{\infty}_{\ell_{3}}(\mu_{0})\bigr)\\ \qquad=s^{\lambda_{1}\lambda_{2}}\bigl((\Delta_{00}^{1})^{\lambda_{2}}+\lambda_{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{01}^{1}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)\cdot\\ \qquad\quad\cdot\bigl(\Delta_{00}^{2}+\Delta_{00}^{1}\Delta_{10}^{2}s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{4}}(\mu_{0})\bigr)\\ \qquad\quad=s^{\lambda_{1}\lambda_{2}}\bigl(\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}}+\bigl(\lambda_{2}\Delta_{00}^{2}(\Delta_{00}^{1})^{\lambda_{2}-1}\Delta_{01}^{1}+(\Delta_{00}^{1})^{\lambda_{2}+1}\Delta_{10}^{2}\bigr)s^{\lambda_{1}}+\mathcal{F}^{\infty}_{\ell_{5}}(\mu_{0})\bigr),\end{array} |  |

with ℓ 3 ∈ ( λ 1 0, min ⁡ { λ 1 0 ​ λ 2 0, 2 ​ λ 1 0 }) \ell_{3}\in(\lambda_{1}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\lambda_{1}^{0}\}), ℓ 4 ∈ ( λ 1 0, min ⁡ { 2 ​ λ 1 0, λ 1 0 + ℓ 1, ℓ 3 }) = ( λ 1 0, min ⁡ { λ 1 0 ​ λ 2 0, 2 ​ λ 1 0 }) \ell_{4}\in(\lambda_{1}^{0},\min\{2\lambda_{1}^{0},\lambda_{1}^{0}+\ell_{1},\ell_{3}\})=(\lambda_{1}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\lambda_{1}^{0}\}) and

 | ℓ 5 ∈ ( λ 1 0, min ⁡ { ℓ 1, ℓ 4, 2 ​ λ 1 }) = ( λ 1 0, min ⁡ { λ 1 0 ​ λ 2 0, 2 ​ λ 1 0, 1 }). \ell_{5}\in(\lambda_{1}^{0},\min\{\ell_{1},\ell_{4},2\lambda_{1}\})=(\lambda_{1}^{0},\min\{\lambda_{1}^{0}\lambda_{2}^{0},2\lambda_{1}^{0},1\}). |  |

In particular we can take ℓ 5 = ℓ \ell_{5}=\ell. ∎

### 4.2 Inverse of a Dulac map

Note that if { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} is a smooth family of planar smooth vector fields having a hyperbolic saddle p = p ⁡ ( μ) p=p(\mu) with hyperbolicity ratio λ ⁡ ( μ) \lambda(\mu), then its Dulac map D ⁡ ( s, μ) D(s;\mu) has a well defined inverse D − 1 ​ ( s, μ) D^{-1}(s;\mu) which happens to be the Dulac map of p p in relation to the family { − X μ } μ ∈ Λ \{-X_{\mu}\}_{\mu\in\Lambda}, with hyperbolicity ratio λ ​ ( μ) − 1 \lambda(\mu)^{-1}. With this knowledge, we can use the previous lemmas to obtain a formula for the first coefficients of D − 1 D^{-1} in function of the coefficients of D D.

###### Lemma 9.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a hyperbolic saddle p p. Set ρ = λ − 1 \rho=\lambda^{-1}, ρ 0 = ( λ 0) − 1 \rho^{0}=(\lambda^{0})^{-1} and

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 + ℱ ℓ ∞ ​ ( μ 0)), D − 1 ​ ( s, μ) = s ρ ​ ( Ω 00 + ℱ η ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),\quad D^{-1}(s;\mu)=s^{\rho}\bigl(\Omega_{00}+\mathcal{F}^{\infty}_{\eta}(\mu_{0})\bigr), |  |

with ℓ ∈ ( 0, min ⁡ { λ 0, 1 }) \ell\in(0,\min\{\lambda^{0},1\}), η ∈ ( 0, min ⁡ { ρ 0, 1 }) \eta\in(0,\min\{\rho^{0},1\}). Then Ω 00 = Δ 00 − ρ \Omega_{00}=\Delta_{00}^{-\rho}.

###### Proof.

On one hand we have from Lemma 4 that

 | D − 1 ∘ D ⁡ ( s, μ) = s ⁡ ( Υ 0 + ℱ ℓ ′ ∞ ​ ( μ 0)), D^{-1}\circ D(s;\mu)=s\bigl(\Upsilon_{0}+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr), |  |

for any given ℓ ′ ∈ ( 0, min ⁡ { λ 0, λ 0 ​ ρ 0 }) = ( 0, min ⁡ { λ 0, 1 }) \ell^{\prime}\in(0,\min\{\lambda^{0},\lambda^{0}\rho^{0}\})=(0,\min\{\lambda^{0},1\}), where Υ 0 = Δ 00 ρ ​ Ω 00 \Upsilon_{0}=\Delta_{00}^{\rho}\Omega_{00}. On the other hand we have D − 1 ∘ D ⁡ ( s, μ) = s D^{-1}\circ D(s;\mu)=s. In particular it follows that Υ 0 = 1 \Upsilon_{0}=1, from which we obtain Ω 00 = Δ 00 − ρ \Omega_{00}=\Delta_{00}^{-\rho}. ∎

###### Lemma 10.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a hyperbolic saddle p p. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 0 < 1 \lambda^{0}<1 and denote

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 + Δ 01 ​ s λ + ℱ ℓ ∞ ​ ( μ 0)), D − 1 ​ ( s, μ) = s ρ ​ ( Ω 00 + Ω 10 ​ s + ℱ η ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}+\Delta_{01}s^{\lambda}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),\quad D^{-1}(s;\mu)=s^{\rho}\bigl(\Omega_{00}+\Omega_{10}s+\mathcal{F}^{\infty}_{\eta}(\mu_{0})\bigr), |  |

with ℓ ∈ ( λ 0, min ⁡ { 2 ​ λ 0, 1 }) \ell\in(\lambda^{0},\min\{2\lambda^{0},1\}), η ∈ ( 1, min ⁡ { ρ 0, 2 }) \eta\in(1,\min\{\rho^{0},2\}). Then

 | Ω 00 = Δ 00 − ρ, Ω 10 = − ρ ​ Δ 00 − ( 2 + ρ) ​ Δ 01, \Omega_{00}=\Delta_{00}^{-\rho},\quad\Omega_{10}=-\rho\Delta_{00}^{-(2+\rho)}\Delta_{01}, |  |

where ρ = λ − 1 \rho=\lambda^{-1} and ρ 0 = ( λ 0) − 1 \rho^{0}=(\lambda^{0})^{-1}.

###### Proof.

On the one hand we have from Lemma 8 that

 | D − 1 ∘ D ⁡ ( s, μ) = s ⁡ ( Υ 0 + Υ 3 ​ s λ + ℱ ℓ ′ ∞ ​ ( μ 0)), D^{-1}\circ D(s;\mu)=s\bigl(\Upsilon_{0}+\Upsilon_{3}s^{\lambda}+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr), |  |

for any given ℓ ′ ∈ ( λ 0, min ⁡ { 2 ​ λ 0, 1 }) \ell^{\prime}\in(\lambda^{0},\min\{2\lambda^{0},1\}), where

 | Υ 0 = Δ 00 ρ ​ Ω 00, Υ 3 = ρ ​ Δ 00 ρ − 1 ​ Ω 00 ​ Δ 01 + Δ 00 ρ + 1 ​ Ω 10. \Upsilon_{0}=\Delta_{00}^{\rho}\Omega_{00},\quad\Upsilon_{3}=\rho\Delta_{00}^{\rho-1}\Omega_{00}\Delta_{01}+\Delta_{00}^{\rho+1}\Omega_{10}. |  |

On the other hand we have D − 1 ∘ D ⁡ ( s, μ) = s D^{-1}\circ D(s;\mu)=s. In particular it follows that Υ 0 = 1 \Upsilon_{0}=1 and Υ 3 = 0 \Upsilon_{3}=0. From the former we obtain Ω 00 = Δ 00 − ρ \Omega_{00}=\Delta_{00}^{-\rho}. Replacing this at the latter we obtain the formula for Ω 10 \Omega_{10}. ∎

###### Lemma 11.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a hyperbolic saddle p p. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ 0 > 1 \lambda^{0}>1 and denote

 | D ⁡ ( s, μ) = s λ ​ ( Δ 00 + Δ 10 ​ s + ℱ ℓ ∞ ​ ( μ 0)), D − 1 ​ ( s, μ) = s ρ ​ ( Ω 00 + Ω 01 ​ s ρ + ℱ η ∞ ​ ( μ 0)), D(s;\mu)=s^{\lambda}\bigl(\Delta_{00}+\Delta_{10}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),\quad D^{-1}(s;\mu)=s^{\rho}\bigl(\Omega_{00}+\Omega_{01}s^{\rho}+\mathcal{F}^{\infty}_{\eta}(\mu_{0})\bigr), |  |

with ℓ ∈ ( 1, min ⁡ { λ 0, 2 }) \ell\in(1,\min\{\lambda^{0},2\}), η ∈ ( ρ 0, min ⁡ { 2 ​ ρ 0, 1 }) \eta\in(\rho^{0},\min\{2\rho^{0},1\}). Then

 | Ω 00 = Δ 00 − ρ, Ω 01 = − ρ ​ Δ 00 − ( 1 + 2 ​ ρ) ​ Δ 10, \Omega_{00}=\Delta_{00}^{-\rho},\quad\Omega_{01}=-\rho\Delta_{00}^{-(1+2\rho)}\Delta_{10}, |  |

where ρ = λ − 1 \rho=\lambda^{-1} and ρ 0 = ( λ 0) − 1 \rho^{0}=(\lambda^{0})^{-1}.

###### Proof.

Similarly to Lemma 10, it follows from Lemma 8 that

 | D ∘ D − 1 ​ ( s, μ) = s ⁡ ( Υ 0 + Υ 3 ​ s ρ + ℱ ℓ ′ ∞ ​ ( μ 0)), D\circ D^{-1}(s;\mu)=s\bigl(\Upsilon_{0}+\Upsilon_{3}s^{\rho}+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr), |  |

for any given ℓ ′ ∈ ( ρ 0, min ⁡ { 2 ​ ρ 0, 1 }) \ell^{\prime}\in(\rho^{0},\min\{2\rho^{0},1\}), where

 | Υ 0 = Ω 00 λ ​ Δ 00, Υ 3 = λ ​ Ω 00 λ − 1 ​ Δ 00 ​ Ω 01 + Ω 00 λ + 1 ​ Δ 10. \Upsilon_{0}=\Omega_{00}^{\lambda}\Delta_{00},\quad\Upsilon_{3}=\lambda\Omega_{00}^{\lambda-1}\Delta_{00}\Omega_{01}+\Omega_{00}^{\lambda+1}\Delta_{10}. |  |

The result now follows by observing that Υ 0 = 1 \Upsilon_{0}=1 and Υ 3 = 0 \Upsilon_{3}=0. ∎

### 4.3 Coefficients of the return map

The following results present explicit formulas for the first coefficients in the asymptotic expansion of the return map ℛ ⁡ ( s, μ) \mathscr{R}(s;\mu).

###### Proposition 1.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p m, p m + 1, …, p n p_{1},\dots,p_{m},p_{m+1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1 for i ∈ { 1, …, m } i\in\{1,\dots,m\} and λ i ​ ( μ 0) > 1 \lambda_{i}(\mu_{0})>1 for i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\}. Then the return map of Γ \Gamma is given by

 | . ℛ ( s; μ) = s r ⁡ ( μ) ( A 1, n + 𝒜 s Λ 0, m + ℱ ℓ ∞ ( μ 0)),.\mathscr{R}(s;\mu)=s^{r(\mu)}\bigl(A_{1,n}+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr), |  | (21) |

for any given ℓ ∈ ( Λ 0, m 0, min ⁡ { r ⁡ ( μ 0), 2 ​ Λ 0, m 0, 1 }) \ell\in(\Lambda_{0,m}^{0},\min\{r(\mu_{0}),2\Lambda_{0,m}^{0},1\}), where 𝒜 = Λ m, n ​ A 1, m ​ A 1, n ​ ( S 1 m + 1 − S 2 m) \mathcal{A}=\Lambda_{m,n}A_{1,m}A_{1,n}(S_{1}^{m+1}-S_{2}^{m}).

###### Proof.

From Corollary 3 we have that

 | D m ∘ … ∘ D 1 ​ ( s, μ) = s Λ 0, m ​ ( A 1, m + C 1, m ​ s Λ 0, m + ℱ ℓ 1 ∞ ​ ( μ 0)), D_{m}\circ\ldots\circ D_{1}(s;\mu)=s^{\Lambda_{0,m}}\bigl(A_{1,m}+C_{1,m}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr), |  | (22) |

where ℓ 1 ∈ ( Λ 0, m 0, min ⁡ { Λ 0, m − 1 0, 2 ​ Λ 0, m 0 }) \ell_{1}\in(\Lambda_{0,m}^{0},\min\{\Lambda_{0,m-1}^{0},2\Lambda_{0,m}^{0}\}) and

 | C j, k = A j, k − 1 2 ​ λ k ​ Δ 01 k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. C_{j,k}=A_{j,k-1}^{2\lambda_{k}}\Delta_{01}^{k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

Moreover from Corollary 2 we have that

 | D n ∘ … ∘ D m + 1 ​ ( s, μ) = s Λ m, n ​ ( A m + 1, n + B m + 1, n ​ s + ℱ ℓ m + 1 ∞ ​ ( μ 0)), D_{n}\circ\ldots\circ D_{m+1}(s;\mu)=s^{\Lambda_{m,n}}\bigl(A_{m+1,n}+B_{m+1,n}s+\mathcal{F}^{\infty}_{\ell_{m+1}}(\mu_{0})\bigr), |  | (23) |

with ℓ m + 1 ∈ ( 1, min ⁡ { λ m + 1 0, 2 }) \ell_{m+1}\in(1,\min\{\lambda_{m+1}^{0},2\}), where

 | B j, k = Λ j, k ​ Δ 10 j Δ 00 j ​ A j, k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. B_{j,k}=\Lambda_{j,k}\frac{\Delta_{10}^{j}}{\Delta_{00}^{j}}A_{j,k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

Since ( 22) and ( 23) are of *Dulac-type*(i.e. it has similar expression), it follows mutatis mutandis from Lemma 8 that

 | ℛ ⁡ ( s, μ) = ( D n ∘ … ∘ D m + 1) ∘ ( D m ∘ … ∘ D 1) ​ ( s, μ) = s r ​ ( A 1, m Λ m, n ​ A m + 1, n + 𝒜 ​ s Λ 0, m + ℱ ℓ ∞ ​ ( μ 0)) = s r ​ ( A 1, n + 𝒜 ​ s Λ 0, m + ℱ ℓ ∞ ​ ( μ 0)), \begin{array}[]{ll}\mathscr{R}(s;\mu)&=(D_{n}\circ\ldots\circ D_{m+1})\circ(D_{m}\circ\ldots\circ D_{1})(s;\mu)\\ &=s^{r}\big(A_{1,m}^{\Lambda_{m,n}}A_{m+1,n}+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr)\\ &=s^{r}\big(A_{1,n}+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),\end{array} |  |

where

 | 𝒜 = Λ m, n ​ A 1, n ​ C 1, m A 1, m + A 1, m Λ m, n + 1 ​ B m + 1, n = Λ m, n ​ A 1, n ​ A 1, m − 1 2 ​ λ m A 1, m ​ Δ 0, 1 m + Λ m + 1, n ​ A 1, m Λ m, n ​ A m + 1, n ​ A 1, m ​ Δ 10 m + 1 Δ 00 m + 1 = − Λ m, n ​ A 1, n ​ ( A 1, m − 1 λ m ​ Δ 00 m) 2 A 1, m ​ S 2 m + λ m ​ Λ m + 1, n ​ A 1, n ​ A 1, m ​ S 1 m + 1 = Λ m, n ​ A 1, n ​ A 1, m ​ ( S 1 m + 1 − S 2 m), \begin{array}[]{ll}\mathcal{A}&\displaystyle=\Lambda_{m,n}A_{1,n}\frac{C_{1,m}}{A_{1,m}}+A_{1,m}^{\Lambda_{m,n}+1}B_{m+1,n}\\ &\displaystyle=\Lambda_{m,n}A_{1,n}\frac{A_{1,m-1}^{2\lambda_{m}}}{A_{1,m}}\Delta_{0,1}^{m}+\Lambda_{m+1,n}A_{1,m}^{\Lambda_{m,n}}A_{m+1,n}A_{1,m}\frac{\Delta_{10}^{m+1}}{\Delta_{00}^{m+1}}\\ &\displaystyle=-\Lambda_{m,n}A_{1,n}\frac{(A_{1,m-1}^{\lambda_{m}}\Delta_{00}^{m})^{2}}{A_{1,m}}S_{2}^{m}+\lambda_{m}\Lambda_{m+1,n}A_{1,n}A_{1,m}S_{1}^{m+1}\\ &\displaystyle=\Lambda_{m,n}A_{1,n}A_{1,m}(S_{1}^{m+1}-S_{2}^{m}),\end{array} |  |

and ℓ ∈ ( Λ 0, m 0, min ⁡ { r ⁡ ( μ 0), 2 ​ Λ 0, m 0, 1 }) \ell\in(\Lambda_{0,m}^{0},\min\{r(\mu_{0}),2\Lambda_{0,m}^{0},1\}). ∎

###### Proposition 2.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p m, p m + 1, …, p n p_{1},\dots,p_{m},p_{m+1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i ​ ( μ 0) > 1 \lambda_{i}(\mu_{0})>1 for i ∈ { 1, …, m } i\in\{1,\dots,m\} and λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1 for i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\}. Then the return map of Γ \Gamma is given by

 | ℛ ⁡ ( s, μ) = { s r ⁡ ( μ) ​ ( A 1, n + ℬ ​ s + ℱ ℓ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) > 1, s r ⁡ ( μ) ​ ( A 1, n + 𝒜 ω ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) = 1, s r ⁡ ( μ) ​ ( A 1, n + 𝒞 ​ s r ⁡ ( μ) + ℱ ℓ ′′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) < 1, \mathscr{R}(s;\mu)=\left\{\begin{array}[]{ll}s^{r(\mu)}(A_{1,n}+\mathcal{B}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})),&\text{if }r(\mu_{0})>1,\\ s^{r(\mu)}(A_{1,n}+\mathcal{A}_{\omega}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})),&\text{if }r(\mu_{0})=1,\\ s^{r(\mu)}(A_{1,n}+\mathcal{C}s^{r(\mu)}+\mathcal{F}^{\infty}_{\ell^{\prime\prime}}(\mu_{0})),&\text{if }r(\mu_{0})<1,\end{array}\right. |  | (24) |

for any given

 | ℓ ∈ ( 1, min ⁡ { r ⁡ ( μ 0), 2 }), ℓ ′ ∈ ( 1, min ⁡ { Λ 0, m 0, 2 }), ℓ ′′ ∈ ( r ⁡ ( μ 0), min ⁡ { 2 ​ r ​ ( μ 0), 1 }); \ell\in(1,\min\{r(\mu_{0}),2\}),\quad\ell^{\prime}\in(1,\min\{\Lambda_{0,m}^{0},2\}),\quad\ell^{\prime\prime}\in(r(\mu_{0}),\min\{2r(\mu_{0}),1\}); |  |

where

 | ℬ = r ⁡ ( μ) ​ A 1, n ​ S 1 1, 𝒞 = − A 1, n 2 ​ S 2 n, 𝒜 ω = ℬ + ( 1 + α ​ ω ​ ( s, α)) ​ 𝒞, \mathcal{B}=r(\mu)A_{1,n}S_{1}^{1},\quad\mathcal{C}=-A_{1,n}^{2}S_{2}^{n},\quad\mathcal{A}_{\omega}=\mathcal{B}+\bigl(1+\alpha\omega(s;\alpha)\bigr)\mathcal{C}, |  |

α = 1 − r ⁡ ( μ) \alpha=1-r(\mu), λ i 0 = λ i ​ ( μ 0) \lambda_{i}^{0}=\lambda_{i}(\mu_{0}) and r ⁡ ( μ) = λ 1 ​ ( μ) ​ … ​ λ n ​ ( μ) r(\mu)=\lambda_{1}(\mu)\dots\lambda_{n}(\mu).

###### Proof.

Given ℓ 1 ∈ ( 1, min ⁡ { λ 1 0, 2 }) \ell_{1}\in(1,\min\{\lambda_{1}^{0},2\}) it follows from Corollary 2 that

 | D m ∘ ⋯ ∘ D 1 ​ ( s, μ) = s Λ 0, m ​ ( A 1, m + B 1, m ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D_{m}\circ\dots\circ D_{1}(s;\mu)=s^{\Lambda_{0,m}}\bigl(A_{1,m}+B_{1,m}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr), |  | (25) |

where we recall that

 | B j, k = Λ j, k ​ Δ 10 j Δ 00 j ​ A j, k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. B_{j,k}=\Lambda_{j,k}\frac{\Delta_{10}^{j}}{\Delta_{00}^{j}}A_{j,k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

From Corollary 3 we have that

 | D n ∘ ⋯ ∘ D m + 1 ​ ( s, μ) = s Λ m, n ​ ( A m + 1, n + C m + 1, n ​ s Λ m, n + ℱ ℓ n ∞ ​ ( μ 0)), D_{n}\circ\dots\circ D_{m+1}(s;\mu)=s^{\Lambda_{m,n}}\bigl(A_{m+1,n}+C_{m+1,n}s^{\Lambda_{m,n}}+\mathcal{F}^{\infty}_{\ell_{n}}(\mu_{0})\bigr), |  | (26) |

where ℓ n ∈ ( Λ m, n 0, min ⁡ { Λ m, n − 1 0, 2 ​ Λ m, n 0 }) \ell_{n}\in(\Lambda_{m,n}^{0},\min\{\Lambda_{m,n-1}^{0},2\Lambda_{m,n}^{0}\}) and C j, k = A j, k − 1 2 ​ λ k ​ Δ 01 k C_{j,k}=A_{j,k-1}^{2\lambda_{k}}\Delta_{01}^{k}.

Since ( 25) and ( 26) are of Dulac-type and r ⁡ ( μ 0) = 1 r(\mu_{0})=1, it follows mutatis mutandis from Lemma 7 that the first return map

 | ℛ ⁡ ( s, μ) = ( D n ∘ ⋯ ∘ D m + 1) ∘ ( D m ∘ ⋯ ∘ D 1) ​ ( s, μ), \mathscr{R}(s;\mu)=(D_{n}\circ\dots\circ D_{m+1})\circ(D_{m}\circ\dots\circ D_{1})(s;\mu), |  |

is given by

 | ℛ ⁡ ( s, μ) = { s r ⁡ ( μ) ​ ( A 1, n + ℬ ​ s + ℱ ℓ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) > 1, s r ⁡ ( μ) ​ ( A 1, n + 𝒜 ω ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) = 1, s ( μ) ​ ( A 1, n + 𝒞 ​ s r ⁡ ( μ) + ℱ ℓ ′′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) < 1, \mathscr{R}(s;\mu)=\left\{\begin{array}[]{ll}s^{r(\mu)}\bigl(A_{1,n}+\mathcal{B}s+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr),&\text{if }r(\mu_{0})>1,\\ s^{r(\mu)}\bigl(A_{1,n}+\mathcal{A}_{\omega}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }r(\mu_{0})=1,\\ s^{(\mu)}\bigl(A_{1,n}+\mathcal{C}s^{r(\mu)}+\mathcal{F}^{\infty}_{\ell^{\prime\prime}}(\mu_{0})\bigr),&\text{if }r(\mu_{0})<1,\end{array}\right. |  | (27) |

for any given

 | ℓ ∈ ( 1, min ⁡ { r ⁡ ( μ 0), 2 }), ℓ ′ ∈ ( 1, min ⁡ { Λ 0, m 0, 2 }), ℓ ′′ ∈ ( r ⁡ ( μ 0), min ⁡ { 2 ​ r ​ ( μ 0), 1 }); \ell\in(1,\min\{r(\mu_{0}),2\}),\quad\ell^{\prime}\in(1,\min\{\Lambda_{0,m}^{0},2\}),\quad\ell^{\prime\prime}\in(r(\mu_{0}),\min\{2r(\mu_{0}),1\}); |  |

where

 | 𝒜 ω = ℬ + ( 1 + α ​ ω ​ ( s, α)) ​ 𝒞, ℬ = Λ m, n ​ A 1, m Λ m, n ​ A m + 1, n ​ B 1, m A 1, m = Λ 1, m ​ Λ m, n ​ A 1, n ​ Δ 10 1 Δ 00 1 = r ⁡ ( μ) ​ A 1, n ​ S 1 1, 𝒞 = A 1, m 2 ​ Λ m, n ​ C m + 1, n = A 1, m 2 ​ Λ m, n ​ A m + 1, n − 1 2 ​ λ n ​ Δ 01 n = − ( A 1, m Λ m, n ​ A m + 1, n − 1 λ n ​ Δ 00 n) 2 ​ S 2 n = − A 1, n 2 ​ S 2 n. \begin{array}[]{l}\displaystyle\mathcal{A}_{\omega}=\mathcal{B}+\bigl(1+\alpha\omega(s;\alpha)\bigr)\mathcal{C},\\ \displaystyle\mathcal{B}=\Lambda_{m,n}A_{1,m}^{\Lambda_{m,n}}A_{m+1,n}\frac{B_{1,m}}{A_{1,m}}=\Lambda_{1,m}\Lambda_{m,n}A_{1,n}\frac{\Delta_{10}^{1}}{\Delta_{00}^{1}}=r(\mu)A_{1,n}S_{1}^{1},\\ \displaystyle\mathcal{C}=A_{1,m}^{2\Lambda_{m,n}}C_{m+1,n}=A_{1,m}^{2\Lambda_{m,n}}A_{m+1,n-1}^{2\lambda_{n}}\Delta_{01}^{n}=-\bigl(A_{1,m}^{\Lambda_{m,n}}A_{m+1,n-1}^{\lambda_{n}}\Delta_{00}^{n}\bigr)^{2}S_{2}^{n}=-A_{1,n}^{2}S_{2}^{n}.\end{array} |  | (28) |

and α = 1 − r ⁡ ( μ) \alpha=1-r(\mu). The results now follows from ( 27) and ( 28). ∎

###### Remark 3.

Although the expressions of the return map in Proposition 1 and 2 are different, the situation they described is the same. Indeed, under the hypothesis of Proposition 2, one can always relabel the corners of Γ \Gamma so that the first saddles begin with λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1, see Figure 4.

\begin{overpic}[Fig3.eps] \put(98.0,45.0){$p_{1}$} \put(78.0,55.0){$p_{2}$} \put(18.0,57.0){$p_{m-1}$} \put(-3.0,45.0){$p_{m}$} \put(-8.0,10.0){$p_{m+1}$} \put(20.0,-3.0){$p_{m+2}$} \put(72.0,-4.0){$p_{n-1}$} \put(98.0,9.0){$p_{n}$} \put(10.0,31.0){$D^{m}$} \put(10.0,20.0){$D^{m+1}$} \put(100.0,25.5){$\Sigma_{a}$} \put(-8.0,25.5){$\Sigma_{b}$} \end{overpic}

( a) (a)

\begin{overpic}[Fig3.eps] \put(97.0,45.0){$p_{m+1}$} \put(78.0,55.0){$p_{m+2}$} \put(18.0,57.0){$p_{n-1}$} \put(-3.0,45.0){$p_{n}$} \put(-3.0,10.0){$p_{1}$} \put(22.0,-4.0){$p_{2}$} \put(71.0,-4.0){$p_{m-1}$} \put(97.0,9.0){$p_{m}$} \put(10.0,31.0){$D^{n}$} \put(10.0,20.0){$D^{1}$} \put(100.0,25.5){$\Sigma_{a}$} \put(-8.0,25.5){$\Sigma_{b}$} \end{overpic}

( b) (b)

Figure 4: Illustration of the equivalence between the hypothesis of ( a) (a) Proposition 1 (with the indexation starting at Σ a \Sigma_{a}) and ( b) (b) Proposition 2 (with the indexation starting at Σ b \Sigma_{b}). Observe that regardless of the indexation, the only Dulac maps whose the non-leader term appears in the expressions of ( 21) and ( 24) are those defined near the transversal Σ b \Sigma_{b}.

## 5 The displacement map of a persistent polycycle

Consider a persistent polycycle Γ \Gamma of a smooth family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} of planar smooth vector fields with hyperbolic saddles p 1, …, p m, p m + 1, … ​ p n p_{1},\dots,p_{m},p_{m+1},\dots p_{n}. Throughout the text of the present paper, we dealt with the return map, as its isolated fixed points correspond to limit cycles in a neighborhood of Γ \Gamma. However, there are particular situations (see, for instance [12]) where it is more convenient to work with the difference of the transition maps from p 1 p_{1} to p m p_{m} and from p n p_{n} to p m + 1 p_{m+1}, with the last one following the solution of { − X μ } μ ∈ Λ \{-X_{\mu}\}_{\mu\in\Lambda}. More precisely, the following displacement map:

 | 𝒟 ⁡ ( s, μ) = D m ∘ ⋯ ∘ D 1 ​ ( s, μ) − D m + 1 − 1 ∘ ⋯ ∘ D n − 1 ​ ( s, μ). \mathscr{D}(s;\mu)=D_{m}\circ\dots\circ D_{1}(s;\mu)-D_{m+1}^{-1}\circ\dots\circ D_{n}^{-1}(s;\mu). |  | (29) |

See Figure 5.

\begin{overpic}[Fig5.eps] \put(97.0,45.0){$p_{m+1}$} \put(78.0,55.0){$p_{m+2}$} \put(18.0,57.0){$p_{n-1}$} \put(-3.0,45.0){$p_{n}$} \put(-3.0,10.0){$p_{1}$} \put(22.0,-4.0){$p_{2}$} \put(71.0,-4.0){$p_{m-1}$} \put(97.0,9.0){$p_{m}$} \put(-8.0,25.5){$\Sigma_{b}$} \put(4.5,29.0){$s$} \put(25.0,19.0){$\mathscr{R}(s)$} \end{overpic}

( a) (a)

\begin{overpic}[Fig6.eps] \put(97.0,45.0){$p_{m+1}$} \put(78.0,55.0){$p_{m+2}$} \put(18.0,57.0){$p_{n-1}$} \put(-3.0,45.0){$p_{n}$} \put(-3.0,10.0){$p_{1}$} \put(22.0,-4.0){$p_{2}$} \put(71.0,-4.0){$p_{m-1}$} \put(97.0,9.0){$p_{m}$} \put(100.0,25.5){$\Sigma_{a}$} \put(-8.0,25.5){$\Sigma_{b}$} \put(16.5,30.25){$s$} \put(65.0,34.0){$\mathscr{D}(s)$} \end{overpic}

( b) (b)

Figure 5: Illustration of ( a) (a) the first return map ℛ \mathscr{R} and ( b) (b) the displacement map 𝒟 \mathscr{D}.

Observe that both approaches are equivalent, since

 | ℛ ⁡ ( s, μ) = s \displaystyle\mathscr{R}(s;\mu)=s | ⇔ \displaystyle\iff | D n ∘ ⋯ ∘ D m + 1 ∘ D m ∘ ⋯ ∘ D 1 ​ ( s, μ) = I ​ d ​ ( s) \displaystyle D_{n}\circ\dots\circ D_{m+1}\circ D_{m}\circ\dots\circ D_{1}(s;\mu)=Id(s) |  |

 |  | ⇔ \displaystyle\iff | D m ∘ ⋯ ∘ D 1 ​ ( s, μ) = ( D n ∘ ⋯ ∘ D m + 1 ​ ( s, μ)) − 1 \displaystyle D_{m}\circ\dots\circ D_{1}(s;\mu)=\left(D_{n}\circ\dots\circ D_{m+1}(s;\mu)\right)^{-1} |  |

 |  | ⇔ \displaystyle\iff | 𝒟 ⁡ ( s, μ) = 0. \displaystyle\mathscr{D}(s;\mu)=0. |  |

For these situations, similar to Propositions 1 and 2, the next result determines the leading terms of the displacement map 𝒟 ⁡ ( s, μ) \mathscr{D}(s;\mu).

###### Proposition 3.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar smooth vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p m, p m + 1, …, p n p_{1},\dots,p_{m},p_{m+1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i ​ ( μ 0) > 1 \lambda_{i}(\mu_{0})>1 for i ∈ { 1, …, m } i\in\{1,\dots,m\} and λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1 for i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\}. Then the displacement map of Γ \Gamma is given by

 | 𝒟 ⁡ ( s, μ) = { A 1, m ​ s Λ 0, m − A m + 1, n ∗ ​ s Λ m, n − 1 + ℱ ℓ ∞ ​ ( μ 0), if ​ r ​ ( μ 0) ≠ 1, s Λ m, n − 1 ​ U ​ ( s, μ) ​ ( Ψ 1 ​ ω ​ ( s, α) + Ψ 2 + Ψ 3 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) = 1, \mathscr{D}(s;\mu)=\left\{\begin{array}[]{ll}A_{1,m}s^{\Lambda_{0,m}}-A_{m+1,n}^{*}s^{\Lambda_{m,n}^{-1}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0}),&\text{if }r(\mu_{0})\neq 1,\\ s^{\Lambda_{m,n}^{-1}}U(s;\mu)\bigl(\Psi_{1}\omega(s;\alpha)+\Psi_{2}+\Psi_{3}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }r(\mu_{0})=1,\end{array}\right. |  | (30) |

for any given

 | ℓ ∈ ( max ⁡ { Λ 0, m 0, ( Λ m, n 0) − 1 }, min ⁡ { Λ 0, m 0 + 1, ( Λ m, n 0) − 1 + 1 }), ℓ ′ ∈ ( 1, min ⁡ { λ 1 0, ( λ n 0) − 1, 2 }), \ell\in(\max\{\Lambda_{0,m}^{0},(\Lambda_{m,n}^{0})^{-1}\},\min\{\Lambda_{0,m}^{0}+1,(\Lambda_{m,n}^{0})^{-1}+1\}),\quad\ell^{\prime}\in(1,\min\{\lambda_{1}^{0},(\lambda_{n}^{0})^{-1},2\}), |  |

where

 | Ψ 1 = α ​ A 1, m, Ψ 2 = A 1, m − A m + 1, n ∗, Ψ 3 = A m + 1, n ∗ ​ ( Λ 0, m ​ S 1 1 − Λ m, n − 1 ​ S 2 n), \Psi_{1}=\alpha A_{1,m},\quad\Psi_{2}=A_{1,m}-A_{m+1,n}^{*},\quad\Psi_{3}=A_{m+1,n}^{*}\bigl(\Lambda_{0,m}S_{1}^{1}-\Lambda_{m,n}^{-1}S_{2}^{n}), |  | (31) |

α = Λ m, n − 1 − Λ 0, m \alpha=\Lambda_{m,n}^{-1}-\Lambda_{0,m} and U ⁡ ( s, μ) = 1 + Λ 0, m ​ S 1 1 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0) U(s;\mu)=1+\Lambda_{0,m}S_{1}^{1}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0}).

###### Proof.

For i ∈ { 1, …, m } i\in\{1,\dots,m\} let

 | D i ​ ( s, μ) = s λ i ​ ( Δ 00 i + Δ 10 i ​ s + ℱ ℓ i ∞ ​ ( μ 0)), D_{i}(s;\mu)=s^{\lambda_{i}}\bigl(\Delta_{00}^{i}+\Delta_{10}^{i}s+\mathcal{F}^{\infty}_{\ell_{i}}(\mu_{0})\bigr), |  |

with ℓ i ∈ ( 1, min ⁡ { λ i, 2 }) \ell_{i}\in(1,\min\{\lambda_{i},2\}). It follows from Corollary 2 that

 | D m ∘ ⋯ ∘ D 1 ​ ( s, μ) = s Λ 0, m ​ ( A 1, m + B 1, m ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)), D_{m}\circ\dots\circ D_{1}(s;\mu)=s^{\Lambda_{0,m}}\bigl(A_{1,m}+B_{1,m}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr), |  | (32) |

where we recall that,

 | B j, k = Λ j, k ​ Δ 10 j Δ 00 j ​ A j, k, A j, k = ∏ i = j k ( Δ 00 i) Λ i, k, Λ i, k = ∏ j = i + 1 k λ j, Λ k ​ k = 1. B_{j,k}=\Lambda_{j,k}\frac{\Delta_{10}^{j}}{\Delta_{00}^{j}}A_{j,k},\quad A_{j,k}=\prod_{i=j}^{k}(\Delta_{00}^{i})^{\Lambda_{i,k}},\quad\Lambda_{i,k}=\prod_{j=i+1}^{k}\lambda_{j},\;\Lambda_{kk}=1. |  |

For i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\} let

 | D i ​ ( s, μ) = s λ i ​ ( Δ 00 i + Δ 01 i ​ s λ i + ℱ ℓ i ∞ ​ ( μ 0)), D i − 1 ​ ( s, μ) = s λ i − 1 ​ ( Ω 00 i + Ω 10 i ​ s + ℱ η i ∞ ​ ( μ 0)), D_{i}(s;\mu)=s^{\lambda_{i}}\bigl(\Delta_{00}^{i}+\Delta_{01}^{i}s^{\lambda_{i}}+\mathcal{F}^{\infty}_{\ell_{i}}(\mu_{0})\bigr),\quad D_{i}^{-1}(s;\mu)=s^{\lambda_{i}^{-1}}\bigl(\Omega_{00}^{i}+\Omega_{10}^{i}s+\mathcal{F}^{\infty}_{\eta_{i}}(\mu_{0})\bigr), |  |

with ℓ i ∈ ( λ i 0, min ⁡ { 2 ​ λ i 0, 1 }) \ell_{i}\in(\lambda_{i}^{0},\min\{2\lambda_{i}^{0},1\}) and η i ∈ ( 1, min ⁡ { ( λ i 0) − 1, 2 }) \eta_{i}\in(1,\min\{(\lambda_{i}^{0})^{-1},2\}). From Corollary 2 we have

 | D m + 1 − 1 ∘ ⋯ ∘ D n − 1 ​ ( s, μ) = s Λ m, n − 1 ​ ( A m + 1, n ∗ + B m + 1, n ∗ ​ s + ℱ η n ∞ ​ ( μ 0)), D_{m+1}^{-1}\circ\dots\circ D_{n}^{-1}(s;\mu)=s^{\Lambda_{m,n}^{-1}}\bigl(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr), |  | (33) |

where

 | A j, k ∗ = ∏ i = 0 k − j ( Ω 00 k − i) Λ j − 1, k − 1 − i − 1 = ∏ i = 0 k − j ( Δ 00 k − i) − Λ j − 1, k − i − 1, B j, k ∗ = Λ j − 1, k − 1 − 1 ​ Ω 10 k Ω 00 k ​ A j, k ∗ = − Λ j − 1, k − 1 ​ Δ 01 k ( Δ 00 k) 2 ​ A j, k ∗, \begin{array}[]{l}\displaystyle A_{j,k}^{*}=\prod_{i=0}^{k-j}(\Omega_{00}^{k-i})^{\Lambda_{j-1,k-1-i}^{-1}}=\prod_{i=0}^{k-j}(\Delta_{00}^{k-i})^{-\Lambda_{j-1,k-i}^{-1}},\\ \displaystyle B_{j,k}^{*}=\Lambda_{j-1,k-1}^{-1}\frac{\Omega_{10}^{k}}{\Omega_{00}^{k}}A_{j,k}^{*}=-\Lambda_{j-1,k}^{-1}\frac{\Delta_{01}^{k}}{(\Delta_{00}^{k})^{2}}A_{j,k}^{*},\end{array} |  | (34) |

with the last equality on both lines following from Lemma 10. Observe that r ⁡ ( μ) ≠ 1 r(\mu)\neq 1 if, and only if, Λ m, n − 1 ≠ Λ 0, m \Lambda_{m,n}^{-1}\neq\Lambda_{0,m}. Therefore it follows from ( 32) and ( 33) that if r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1 then

 | 𝒟 ⁡ ( s, μ) = D m ∘ ⋯ ∘ D 1 ​ ( s, μ) − D m + 1 − 1 ∘ ⋯ ∘ D n − 1 ​ ( s, μ) = A 1, m ​ s Λ 0, m − A m + 1, n ∗ ​ s Λ m, n − 1 + ℱ ℓ ∞ ​ ( μ 0), \begin{array}[]{ll}\mathscr{D}(s;\mu)&=D_{m}\circ\dots\circ D_{1}(s;\mu)-D_{m+1}^{-1}\circ\dots\circ D_{n}^{-1}(s;\mu)\\ &=A_{1,m}s^{\Lambda_{0,m}}-A_{m+1,n}^{*}s^{\Lambda_{m,n}^{-1}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0}),\end{array} |  |

for any given

 | ℓ ∈ ( max ⁡ { Λ 0, m 0, ( Λ m, n 0) − 1 }, min ⁡ { Λ 0, m 0 + 1, ( Λ m, n 0) − 1 + 1 }). \ell\in(\max\{\Lambda_{0,m}^{0},(\Lambda_{m,n}^{0})^{-1}\},\min\{\Lambda_{0,m}^{0}+1,(\Lambda_{m,n}^{0})^{-1}+1\}). |  |

Suppose now that r ⁡ ( μ 0) = 1 r(\mu_{0})=1 and let α = Λ m, n − 1 − Λ 0, m \alpha=\Lambda_{m,n}^{-1}-\Lambda_{0,m}. In this case we have,

 | 𝒟 ⁡ ( s, μ) = D m ∘ ⋯ ∘ D 1 ​ ( s, μ) − D m + 1 − 1 ∘ ⋯ ∘ D n − 1 ​ ( s, μ) = s Λ 0, m ​ ( A 1, m + B 1, m ​ s + ℱ ℓ 1 ∞ ​ ( μ 0)) − s Λ m, n − 1 ​ ( A m + 1, n ∗ + B m + 1, n ∗ ​ s + ℱ η n ∞ ​ ( μ 0)) = s Λ m, n − 1 [s − α ( A 1, m + B 1, m s + ℱ ∞ ℓ 1 ( μ 0)) − ( A m + 1, n ∗ + B m + 1, n ∗ s + ℱ ∞ η n ( μ 0))]. \begin{array}[]{ll}\mathscr{D}(s;\mu)&=D_{m}\circ\dots\circ D_{1}(s;\mu)-D_{m+1}^{-1}\circ\dots\circ D_{n}^{-1}(s;\mu)\\ &=s^{\Lambda_{0,m}}\bigl(A_{1,m}+B_{1,m}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)-s^{\Lambda_{m,n}^{-1}}\bigl(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr)\\ &=s^{\Lambda_{m,n}^{-1}}\bigl[s^{-\alpha}\bigl(A_{1,m}+B_{1,m}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0})\bigr)-\bigr(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr)\bigr].\end{array} |  | (35) |

Consider

 | U ⁡ ( s, μ) = 1 + B 1, m A 1, m ​ s + ℱ ℓ 1 ∞ ​ ( μ 0), U(s;\mu)=1+\frac{B_{1,m}}{A_{1,m}}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0}), |  |

and observe that from the Generalized Binomial Theorem 3 we have

 | U ​ ( s, μ) − 1 = 1 − B 1, m A 1, m ​ s + ℱ ℓ 1 ∞ ​ ( μ 0). U(s;\mu)^{-1}=1-\frac{B_{1,m}}{A_{1,m}}s+\mathcal{F}^{\infty}_{\ell_{1}}(\mu_{0}). |  |

Hence it follows from ( 35) that

 | 𝒟 ⁡ ( s, μ) = s Λ m, n − 1 ​ [s − α ​ A 1, m ​ U ​ ( s, μ) − ( A m + 1, n ∗ + B m + 1, n ∗ ​ s + ℱ η n ∞ ​ ( μ 0))] = s Λ m, n − 1 ​ U ​ ( s, μ) ​ [s − α ​ A 1, m − U ​ ( s, μ) − 1 ​ ( A m + 1, n ∗ + B m + 1, n ∗ ​ s + ℱ η n ∞ ​ ( μ 0))] = s Λ m, n − 1 U ( s; μ) [( 1 + α ω ( s; α)) A 1, m − ( 1 − B 1, m A 1, m s + ℱ ∞ ℓ 1) ( A m + 1, n ∗ + B m + 1, n ∗ s + ℱ ∞ η n ( μ 0))] = s Λ m, n − 1 ​ U ​ ( s, μ) ​ [Ψ 1 ​ ω ​ ( s, α) + Ψ 2 + Ψ 3 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)], \begin{array}[]{ll}\mathscr{D}(s;\mu)&=s^{\Lambda_{m,n}^{-1}}\bigl[s^{-\alpha}A_{1,m}U(s;\mu)-\bigl(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr)\bigr]\\ &=s^{\Lambda_{m,n}^{-1}}U(s;\mu)\bigl[s^{-\alpha}A_{1,m}-U(s;\mu)^{-1}\bigl(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr)\bigr]\\ &\displaystyle=s^{\Lambda_{m,n}^{-1}}U(s;\mu)\biggl[\bigl(1+\alpha\omega(s;\alpha)\bigr)A_{1,m}\bigr.\biggr.\\ &\displaystyle\biggl.\bigl.\qquad\qquad\qquad\qquad\qquad-\biggl(1-\frac{B_{1,m}}{A_{1,m}}s+\mathcal{F}^{\infty}_{\ell_{1}}\biggr)\bigl(A_{m+1,n}^{*}+B_{m+1,n}^{*}s+\mathcal{F}^{\infty}_{\eta_{n}}(\mu_{0})\bigr)\biggr]\\ &\displaystyle=s^{\Lambda_{m,n}^{-1}}U(s;\mu)\bigl[\Psi_{1}\omega(s;\alpha)+\Psi_{2}+\Psi_{3}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr],\end{array} |  |

where Ψ 1 = α ​ A 1, m \Psi_{1}=\alpha A_{1,m}, Ψ 2 = A 1, m − A m + 1, n ∗ \Psi_{2}=A_{1,m}-A_{m+1,n}^{*},

 | Ψ 3 = A m + 1, n ∗ ​ B 1, m A 1, m − B m + 1, n ∗ = A m + 1, n ∗ ​ ( Λ 1, m ​ Δ 10 1 Δ 00 1 + Λ m, n − 1 ​ Δ 01 n ( Δ 00 n) 2) = A m + 1, n ∗ ​ ( Λ 0, m ​ S 1 1 − Λ m, n − 1 ​ S 2 n), \begin{array}[]{ll}\Psi_{3}&\displaystyle=A_{m+1,n}^{*}\frac{B_{1,m}}{A_{1,m}}-B_{m+1,n}^{*}\\ &\displaystyle=A_{m+1,n}^{*}\left(\Lambda_{1,m}\frac{\Delta_{10}^{1}}{\Delta_{00}^{1}}+\Lambda_{m,n}^{-1}\frac{\Delta_{01}^{n}}{(\Delta_{00}^{n})^{2}}\right)\\ &\displaystyle=A_{m+1,n}^{*}\bigl(\Lambda_{0,m}S_{1}^{1}-\Lambda_{m,n}^{-1}S_{2}^{n}),\end{array} |  |

with the second equality following from ( 34) and

 | ℓ ′ ∈ ( 1, min ⁡ { ℓ 1, ℓ n, 2 }) = ( 1, min ⁡ { λ 1 0, ( λ n 0) − 1, 2 }). \ell^{\prime}\in(1,\min\{\ell_{1},\ell_{n},2\})=(1,\min\{\lambda_{1}^{0},(\lambda_{n}^{0})^{-1},2\}). |  |

Finally, we now observe that U ⁡ ( s, μ) = 1 + Λ 0, m ​ S 1 1 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0) U(s;\mu)=1+\Lambda_{0,m}S_{1}^{1}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0}). ∎

###### Remark 4.

Similarly to Remark 3, we observe that except by a change of indexation, Proposition 3 is also equivalent to Propositions 1 and 2.

## 6 Proof of the main theorems

###### Proof of Theorem A.

The expression of the return map ( 5) follows directly from Corollary 1. As for the assertions concerning the cyclicity of Γ \Gamma, we need to consider the displacement map given by:

 | 𝒟 ⁡ ( s, μ) = ℛ ⁡ ( s, μ) − s = s r ​ ( A 1, n − s 1 − r + ℱ ℓ ∞ ​ ( μ 0)), \mathscr{D}(s;\mu)=\mathscr{R}(s;\mu)-s=s^{r}\left(A_{1,n}-s^{1-r}+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\right), |  |

It is known that no bifurcation of limit cycles occur at μ 0 \mu_{0} near a persistent polycycle Γ \Gamma with graphic number r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1 (See [14, Remark 2.12]). This is precisely statement (a). To prove (b), we write (recall Definition 8) the displacemet map as

 | 𝒟 ⁡ ( s, μ) = s r ​ ( A 1, n − 1 + ( 1 − r) ​ ω ​ ( s, r − 1) + ℱ ℓ ∞ ​ ( μ 0)). \mathscr{D}(s;\mu)=s^{r}\left(A_{1,n}-1+(1-r)\omega(s;r-1)+\mathcal{F}_{\ell}^{\infty}(\mu_{0})\right). |  | (36) |

Now, since ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot,\mu_{0})\not\equiv Id, given ε > 0 \varepsilon>0 there exists s 1 ∈ ( 0, ε) s_{1}\in(0,\varepsilon) such that 𝒟 ⁡ ( s 1, μ 0) ≠ 0 \mathscr{D}(s_{1},\mu_{0})\neq 0. Without loss of generality, assume that 𝒟 ⁡ ( s 1, μ 0) > 0 \mathscr{D}(s_{1},\mu_{0})>0, since the other case is analogous. Thus, there exists a neighborhood U U of μ 0 \mu_{0} such that 𝒟 ⁡ ( s 1, μ) > 0 \mathscr{D}(s_{1},\mu)>0 for μ ∈ U \mu\in U. Since r − 1 r-1 changes signs at μ 0 \mu_{0} we can take μ 1 ∈ U \mu_{1}\in U such that r ⁡ ( μ 1) > 1 r(\mu_{1})>1. Now, using Lemmas 1 and 3 we have that

 | Z 1 ​ ( s, μ):= s − r ​ 𝒟 ​ ( s, μ) ω ⁡ ( s, r − 1) = A 1, n − 1 ω ⁡ ( s, r − 1) + ( 1 − r) + ℱ ℓ − δ ∞ ​ ( μ 0), Z_{1}(s;\mu):=\frac{s^{-r}\mathscr{D}(s;\mu)}{\omega(s;r-1)}=\frac{A_{1,n}-1}{\omega(s;r-1)}+(1-r)+\mathcal{F}_{\ell-\delta}^{\infty}(\mu_{0}), |  | (37) |

and

 | lim s → 0 + Z 1 ​ ( s, μ) = ( A 1, n − 1) ​ max ⁡ { 1 − r, 0 } + ( 1 − r) = ( 1 − r) ​ β, \lim\limits_{s\to 0^{+}}Z_{1}(s;\mu)=(A_{1,n}-1)\max\{1-r,0\}+(1-r)=(1-r)\beta, |  |

where

 | β = { 1, if ​ 1 − r ⩽ 0, A 1, n, if ​ 1 − r > 0. \beta=\left\{\begin{array}[]{ll}1,&\text{if }1-r\leqslant 0,\\ A_{1,n},&\text{if }1-r>0.\end{array}\right. |  |

In either case, we have β > 0 \beta>0. Since r ⁡ ( μ 1) < 1 r(\mu_{1})<1, we have that lim s → 0 + Z 1 ​ ( s, μ 1) < 0 \lim\limits_{s\to 0^{+}}Z_{1}(s;\mu_{1})<0 and thus, there exists s 2 ∈ ( 0, s 1) s_{2}\in(0,s_{1}) such that Z 1 ​ ( s 2, μ 1) < 0 Z_{1}(s_{2},\mu_{1})<0. Therefore 𝒟 ⁡ ( s 2, μ 1) ​ 𝒟 ​ ( s 1, μ 1) < 0 \mathscr{D}(s_{2},\mu_{1})\mathscr{D}(s_{1},\mu_{1})<0 and by continuity, there is at least one s ∗ ∈ ( s 2, s 1) ⊂ ( 0, ε) s^{\ast}\in(s_{2},s_{1})\subset(0,\varepsilon) such that 𝒟 ⁡ ( s ∗, μ 1) = 0 \mathscr{D}(s^{\ast},\mu_{1})=0. Since X μ 1 X_{\mu_{1}} is analytic, we have that s ∗ s^{*} is an isolated solution and thus Cycl ⁡ ( Γ, μ 0) ⩾ 1 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 1.

Now, we turn to prove statement (c). For r ⁡ ( μ 0) ≠ 1 r(\mu_{0})\neq 1 this statement follows from (a). For r ⁡ ( μ 0) = 1 r(\mu_{0})=1, the upper bound on the cyclicity is obtained by applying the derivation-division algorithm. Using Lemma 3 we have that

 | ∂ s Z 1 ​ ( s, μ) = ( A 1, n − 1) ​ s − r ω ​ ( s, r − 1) 2 + ℱ ℓ − δ − 1 ∞ ​ ( μ 0). \partial_{s}Z_{1}(s;\mu)=\frac{(A_{1,n}-1)s^{-r}}{\omega(s;r-1)^{2}}+\mathcal{F}_{\ell-\delta-1}^{\infty}(\mu_{0}). |  | (38) |

Since s − α ∈ ℱ − δ ∞ ( { α = 0 }) s^{-\alpha}\in\mathcal{F}_{-\delta}^{\infty}(\{\alpha=0\}), for any given δ ∈ ( 0, ℓ / 4) \delta\in(0,\ell/4) we have that

 | lim ( s, μ) → ( 0 +, μ 0) s r ​ ω ​ ( s, r − 1) 2 ​ ∂ s Z 1 ​ ( s, μ) = lim ( s, μ) → ( 0 +, μ 0) ( A 1, n − 1) + ℱ ℓ − 4 ​ δ ∞ ​ ( μ 0) = A 1, n ​ ( μ 0) − 1. \lim\limits_{(s,\mu)\to(0^{+},\mu_{0})}s^{r}\omega(s;r-1)^{2}\partial_{s}Z_{1}(s;\mu)=\lim\limits_{(s,\mu)\to(0^{+},\mu_{0})}(A_{1,n}-1)+\mathcal{F}_{\ell-4\delta}^{\infty}(\mu_{0})=A_{1,n}(\mu_{0})-1. |  |

Under the hypothesis of (c), the above limit is not zero, which implies by Rolle’s Theorem that there is a small neighborhood of μ 0 \mu_{0} and ε > 0 \varepsilon>0 such that Z 1 ​ ( ⋅, μ) Z_{1}(\cdot;\mu) and thus 𝒟 ⁡ ( ⋅, μ) \mathscr{D}(\cdot;\mu) has at most one zero s ∗ ∈ ( 0, ε) s^{\ast}\in(0,\varepsilon). Hence, Cycl ⁡ ( Γ, μ 0) ⩽ 1 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 1.

Finally, we assume the hypothesis of (d). Since ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id, given ε > 0 \varepsilon>0, there exists s 1 ∈ ( 0, ε) s_{1}\in(0,\varepsilon) such that 𝒟 ⁡ ( s 1, μ 0) ≠ 0 \mathscr{D}(s_{1};\mu_{0})\neq 0. Again, we assume without loss of generality that that 𝒟 ⁡ ( s 1, μ 0) < 0 \mathscr{D}(s_{1},\mu_{0})<0 which implies that there exists a neighborhood U U of μ 0 \mu_{0} such that 𝒟 ⁡ ( s 1, μ) < 0 \mathscr{D}(s_{1},\mu)<0 for μ ∈ U \mu\in U. Since r − 1 r-1 and A 1, n − 1 A_{1,n}-1 are independent at μ 0 \mu_{0}, we can take μ 1 ∈ U \mu_{1}\in U such that r ⁡ ( μ 1) = 1 r(\mu_{1})=1 and A 1, n ​ ( μ 1) > 1 A_{1,n}(\mu_{1})>1. Then, by ( 36)

 | lim s → 0 + s − 1 ​ 𝒟 ​ ( s, μ 1) = A 1, n ​ ( μ 1) − 1 > 0. \lim_{s\to 0^{+}}s^{-1}\mathscr{D}(s;\mu_{1})=A_{1,n}(\mu_{1})-1>0. |  |

Therefore, there exists s 2 ∈ ( 0, s 1) s_{2}\in(0,s_{1}) such that 𝒟 ⁡ ( s 2, μ 1) > 0 \mathscr{D}(s_{2},\mu_{1})>0, which implies that there is a neighborhood U 1 ⊂ U U_{1}\subset U of μ 1 \mu_{1} such that 𝒟 ⁡ ( s 2, μ) > 0 \mathscr{D}(s_{2},\mu)>0 for μ ∈ U 1 \mu\in U_{1}. Now, using the independence of r − 1 r-1 and A 1, n − 1 A_{1,n}-1 at μ 0 \mu_{0}, we take μ 2 ∈ U 1 \mu_{2}\in U_{1} such that r ⁡ ( μ 2) > 1 r(\mu_{2})>1. From ( 38), we have that lim s → 0 + Z 1 ​ ( s, μ 2) < 0 \lim\limits_{s\to 0^{+}}Z_{1}(s;\mu_{2})<0 which implies the existence of s 3 ∈ ( 0, s 2) s_{3}\in(0,s_{2}) such that 𝒟 ⁡ ( s 3, μ 2) < 0 \mathscr{D}(s_{3};\mu_{2})<0. Now, since

 | 𝒟 ⁡ ( s 3, μ 2) ​ < 0, 𝒟 ⁡ ( s 2, μ 2) > ​ 0, 𝒟 ⁡ ( s 1, μ 2) < 0, \mathscr{D}(s_{3};\mu_{2})<0,\;\mathscr{D}(s_{2};\mu_{2})>0,\;\mathscr{D}(s_{1};\mu_{2})<0, |  |

we have by continuity that Cycl ⁡ ( Γ, μ 0) ⩾ 2 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 2. ∎

###### Proof of Theorem B.

It follows from Proposition 1 that the return map is given by equation ( 6). Thus, we turn to the proof of the statements concerning the cyclicity of Γ \Gamma. For this purpose, we consider the displacement map 𝒟 ⁡ ( s, μ) = ℛ ⁡ ( s, μ) − s \mathscr{D}(s;\mu)=\mathscr{R}(s;\mu)-s, which under the current hypothesis is written as

 | 𝒟 ⁡ ( s, μ) = s r ​ ( A 1, n − s 1 − r + 𝒜 ​ s Λ 0, m + ℱ ℓ ∞ ​ ( μ 0)). \mathscr{D}(s;\mu)=s^{r}\big(A_{1,n}-s^{1-r}+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0})\bigr). |  | (39) |

To prove (a) we apply the derivation-division algorithm to the function Z 1 ​ ( s, μ) Z_{1}(s;\mu) defined in ( 37), which under the current hypothesis writes as follows.

 | Z 1 ​ ( s, μ) = A 1, n − 1 ω ⁡ ( s, r − 1) + ( 1 − r) + 𝒜 ​ s Λ 0, m ω ⁡ ( s, r − 1) + ℱ ℓ ∞ ​ ( μ 0). Z_{1}(s;\mu)=\frac{A_{1,n}-1}{\omega(s;r-1)}+(1-r)+\frac{\mathcal{A}s^{\Lambda_{0,m}}}{\omega(s;r-1)}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}). |  |

We assume that the hypothesis of items (a) and (c) in Theorem A do not hold, i.e. r ⁡ ( μ 0) = 1 r(\mu_{0})=1 and A 1, n ​ ( μ 0) = 1 A_{1,n}(\mu_{0})=1, otherwise we would have Cycl ⁡ ( Γ, μ 0) < 2 {\rm Cycl}(\Gamma,\mu_{0})<2 immediately. We have that

 | ∂ s Z 1 ​ ( s, μ) = ( A 1, n − 1) ​ s − r ω ​ ( s, r − 1) 2 + Λ 0, m ​ 𝒜 ​ s Λ 0, m − 1 ω ⁡ ( s, r − 1) + 𝒜 ​ s Λ 0, m − r ω 2 ​ ( s, r − 1) + ℱ ℓ − δ − 1 ∞ ​ ( μ 0), \partial_{s}Z_{1}(s;\mu)=\frac{(A_{1,n}-1)s^{-r}}{\omega(s;r-1)^{2}}+\frac{\Lambda_{0,m}\mathcal{A}s^{\Lambda_{0,m}-1}}{\omega(s;r-1)}+\frac{\mathcal{A}s^{\Lambda_{0,m}-r}}{\omega^{2}(s;r-1)}+\mathcal{F}_{\ell-\delta-1}^{\infty}(\mu_{0}), |  |

which yield

 | Θ 1 ​ ( s, μ) \displaystyle\Theta_{1}(s;\mu) | : ⁣ = \displaystyle:= | s r ​ ω 2 ​ ( s, r − 1) ​ ∂ s Z 1 ​ ( s, μ) \displaystyle s^{r}\omega^{2}(s;r-1)\partial_{s}Z_{1}(s;\mu) |  |

 |  | = \displaystyle= | ( A 1, n − 1) + Λ 0, m ​ 𝒜 ​ s Λ 0, m + r − 1 ​ ω ​ ( s, r − 1) + 𝒜 ​ s Λ 0, m + ℱ ℓ − 4 ​ δ ∞ ​ ( μ 0), \displaystyle(A_{1,n}-1)+\Lambda_{0,m}\mathcal{A}s^{\Lambda_{0,m}+r-1}\omega(s;r-1)+\mathcal{A}s^{\Lambda_{0,m}}+\mathcal{F}_{\ell-4\delta}^{\infty}(\mu_{0}), |  |

for any δ ∈ ( 0, ℓ / 4) \delta\in(0,\ell/4). The derivative with respect to s s is given by

 | ∂ s Θ 1 ​ ( s, μ) = ( r − 1 + Λ 0, m) ​ Λ 0, m ​ 𝒜 ​ s r + Λ 0, m − 2 ​ ω ​ ( s, r − 1) + ℱ ℓ − 4 ​ δ − 1 ∞ ​ ( μ 0). \partial_{s}\Theta_{1}(s;\mu)=(r-1+\Lambda_{0,m})\Lambda_{0,m}\mathcal{A}s^{r+\Lambda_{0,m}-2}\omega(s;r-1)+\mathcal{F}_{\ell-4\delta-1}^{\infty}(\mu_{0}). |  |

and finally,

 | Z 2 ​ ( s, μ):= s 2 − Λ 0, m − r ​ ∂ s Θ 1 ​ ( s, μ) ω ⁡ ( s, r − 1) = ( r − 1 + Λ 0, m) ​ Λ 0, m ​ 𝒜 + ℱ ℓ + 1 − 6 ​ δ ∞ ​ ( μ 0). Z_{2}(s;\mu):=\frac{s^{2-\Lambda_{0,m}-r}\partial_{s}\Theta_{1}(s;\mu)}{\omega(s;r-1)}=(r-1+\Lambda_{0,m})\Lambda_{0,m}\mathcal{A}+\mathcal{F}_{\ell+1-6\delta}^{\infty}(\mu_{0}). |  |

Taking δ ∈ ( 0, min ⁡ { ℓ / 4, ( ℓ + 1) / 6 }) \delta\in(0,\min\{\ell/4,(\ell+1)/6\}), we have that

 | lim ( s, μ) → ( 0 +, μ 0) Z 2 ​ ( s, μ) = ( Λ 0, m 0) 2 ​ 𝒜 ​ ( μ 0) ≠ 0, \lim\limits_{(s,\mu)\to(0^{+},\mu_{0})}Z_{2}(s;\mu)=(\Lambda_{0,m}^{0})^{2}\mathcal{A}(\mu_{0})\neq 0, |  |

and by Rolle’s theorem, there is a small neighborhood U U of μ 0 \mu_{0} and ε > 0 \varepsilon>0 such that Θ 1 ​ ( ⋅, μ) \Theta_{1}(\cdot;\mu) has at most one zero in ( 0, ε) (0,\varepsilon) which implies that Z 1 ​ ( s, μ) Z_{1}(s;\mu) and thus 𝒟 ⁡ ( s, μ) \mathscr{D}(s;\mu) have at most two zeros in the interval ( 0, ε) (0,\varepsilon). Thus, Cycl ⁡ ( Γ, μ 0) ⩽ 2 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 2.

To prove the assertion in item (b), we follow steps analogous to those in the proofs of items (b) and (d) in Theorem A: Since ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id, given ε > 0 \varepsilon>0, there exists a s 1 ∈ ( 0, ε) s_{1}\in(0,\varepsilon) such that 𝒟 ⁡ ( s 1, μ 0) ≠ 0 \mathscr{D}(s_{1},\mu_{0})\neq 0, without loss of generality, we assume that 𝒟 ⁡ ( s 1, μ 0) > 0 \mathscr{D}(s_{1},\mu_{0})>0. By continuity, there exists U ∋ μ 0 U\ni\mu_{0} such that 𝒟 ⁡ ( s 1, μ) > 0 \mathscr{D}(s_{1};\mu)>0 for μ ∈ U \mu\in U. Then, by the independence of r − 1 r-1, A 1, n − 1 A_{1,n}-1 and 𝒜 \mathcal{A} at μ 0 \mu_{0}, we take μ 1 ∈ U \mu_{1}\in U for which r ⁡ ( μ 1) = 1 r(\mu_{1})=1, A 1, n ​ ( μ 1) = 1 A_{1,n}(\mu_{1})=1 and 𝒜 ⁡ ( μ 1) < 0 \mathcal{A}(\mu_{1})<0. Then from ( 39) we have

 | lim s → 0 + s − 1 − Λ 0, m ​ 𝒟 ​ ( s, μ 1) = 𝒜 ⁡ ( μ 1) < 0, \lim\limits_{s\to 0^{+}}s^{-1-\Lambda_{0,m}}\mathscr{D}(s;\mu_{1})=\mathcal{A}(\mu_{1})<0, |  |

which implies that there exists s 2 ∈ ( 0, s 1) s_{2}\in(0,s_{1}) such that 𝒟 ⁡ ( s 2, μ 1) < 0 \mathscr{D}(s_{2};\mu_{1})<0. Hence, by continuity, there exists a neighborhood U 1 ⊂ U U_{1}\subset U of μ 1 \mu_{1} such that 𝒟 ⁡ ( s 2, ⋅) | U 1 < 0 \mathscr{D}(s_{2};\cdot)|_{U_{1}}<0. Again, we take μ 2 ∈ U 1 \mu_{2}\in U_{1} with r ⁡ ( μ 2) = 1 r(\mu_{2})=1 and A 1, n ​ ( μ 2) > 1 A_{1,n}(\mu_{2})>1. By ( 39) we have

 | lim s → 0 + s − 1 ​ 𝒟 ​ ( s, μ 2) = A 1, n ​ ( μ 2) − 1 > 0. \lim\limits_{s\to 0^{+}}s^{-1}\mathscr{D}(s;\mu_{2})=A_{1,n}(\mu_{2})-1>0. |  |

Thus, there exists s 3 ∈ ( 0, s 2) s_{3}\in(0,s_{2}) such that 𝒟 ⁡ ( s 3, μ 2) > 0 \mathscr{D}(s_{3};\mu_{2})>0 which in turn implies that there exists a neighborhood U 2 U_{2}, with μ 2 ∈ U 2 ⊂ U 1 \mu_{2}\in U_{2}\subset U_{1} such that 𝒟 ⁡ ( s 3, ⋅) | U 2 > 0 \mathscr{D}(s_{3};\cdot)|_{U_{2}}>0. Finally, taking μ 3 ∈ U 2 \mu_{3}\in U_{2} for which r ⁡ ( μ 3) > 1 r(\mu_{3})>1, we obtain that

 | lim s → 0 + Z 1 ​ ( s, μ 3) = 1 − r ⁡ ( μ 3) < 0. \lim\limits_{s\to 0^{+}}Z_{1}(s;\mu_{3})=1-r(\mu_{3})<0. |  |

Hence, we obtain s 4 ∈ ( 0, s 3) s_{4}\in(0,s_{3}) such that 𝒟 ⁡ ( s 4, μ 3) < 0 \mathscr{D}(s_{4};\mu_{3})<0, 𝒟 ⁡ ( s 3, μ 3) > 0 \mathscr{D}(s_{3};\mu_{3})>0, 𝒟 ⁡ ( s 2, μ 3) < 0 \mathscr{D}(s_{2};\mu_{3})<0 and 𝒟 ⁡ ( s 1, μ 3) > 0 \mathscr{D}(s_{1};\mu_{3})>0 and therefore we conclude that Cycl ⁡ ( Γ, μ 0) ⩾ 3 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 3. ∎

## 7 The equivalence of the displacement map

As anticipated in Section 5, in this paper we focused on the first return map. However, sometimes it may be convenient to work with the displacement map ( 29) instead. Therefore in this section we observe that there is also a similar version of Theorems A and B for the displacement map.

###### Theorem C.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be a smooth family of planar analytic vector fields having a persistent polycycle Γ \Gamma with hyperbolic saddles p 1, …, p m, p m + 1, …, p n p_{1},\dots,p_{m},p_{m+1},\dots,p_{n}. Let μ 0 ∈ Λ \mu_{0}\in\Lambda be such that λ i ​ ( μ 0) < 1 \lambda_{i}(\mu_{0})<1 for i ∈ { 1, …, m } i\in\{1,\dots,m\} and λ i ​ ( μ 0) > 1 \lambda_{i}(\mu_{0})>1 for i ∈ { m + 1, …, n } i\in\{m+1,\dots,n\}. Then the first displacement map of Γ \Gamma is given by

 | 𝒟 ⁡ ( s, μ) = { A 1, m ​ s Λ 0, m − A m + 1, n ∗ ​ s Λ m, n − 1 + ℱ ℓ ∞ ​ ( μ 0), if ​ r ​ ( μ 0) ≠ 1, s Λ m, n − 1 ​ U ​ ( s, μ) ​ ( Ψ 1 ​ ω ​ ( s, α) + Ψ 2 + Ψ 3 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0)), if ​ r ​ ( μ 0) = 1, \mathscr{D}(s;\mu)=\left\{\begin{array}[]{ll}A_{1,m}s^{\Lambda_{0,m}}-A_{m+1,n}^{*}s^{\Lambda_{m,n}^{-1}}+\mathcal{F}^{\infty}_{\ell}(\mu_{0}),&\text{if }r(\mu_{0})\neq 1,\\ s^{\Lambda_{m,n}^{-1}}U(s;\mu)\bigl(\Psi_{1}\omega(s;\alpha)+\Psi_{2}+\Psi_{3}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0})\bigr),&\text{if }r(\mu_{0})=1,\end{array}\right. |  |

for any given

 | ℓ ∈ ( max ⁡ { Λ 0, m 0, ( Λ m, n 0) − 1 }, min ⁡ { Λ 0, m 0 + 1, ( Λ m, n 0) − 1 + 1 }), ℓ ′ ∈ ( 1, min ⁡ { λ 1 0, ( λ n 0) − 1, 2 }), \ell\in(\max\{\Lambda_{0,m}^{0},(\Lambda_{m,n}^{0})^{-1}\},\min\{\Lambda_{0,m}^{0}+1,(\Lambda_{m,n}^{0})^{-1}+1\}),\quad\ell^{\prime}\in(1,\min\{\lambda_{1}^{0},(\lambda_{n}^{0})^{-1},2\}), |  |

where

 | Ψ 1 = α ​ A 1, m, Ψ 2 = A 1, m − A m + 1, n ∗, Ψ 3 = A m + 1, n ∗ ​ ( Λ 0, m ​ S 1 1 − Λ m, n − 1 ​ S 2 n), \Psi_{1}=\alpha A_{1,m},\quad\Psi_{2}=A_{1,m}-A_{m+1,n}^{*},\quad\Psi_{3}=A_{m+1,n}^{*}\bigl(\Lambda_{0,m}S_{1}^{1}-\Lambda_{m,n}^{-1}S_{2}^{n}), |  |

α = Λ m, n − 1 − Λ 0, m \alpha=\Lambda_{m,n}^{-1}-\Lambda_{0,m} and U ⁡ ( s, μ) = 1 + Λ 0, m ​ S 1 1 ​ s + ℱ ℓ ′ ∞ ​ ( μ 0) U(s;\mu)=1+\Lambda_{0,m}S_{1}^{1}s+\mathcal{F}^{\infty}_{\ell^{\prime}}(\mu_{0}). Moreover, the following holds:

- (a)

Cycl ⁡ ( Γ, μ 0) = 0 {\rm Cycl}(\Gamma,\mu_{0})=0, if Ψ 1 ≠ 0 \Psi_{1}\neq 0;

- (b)

Cycl ⁡ ( Γ, μ 0) ⩾ 1 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 1, if Ψ 1 = 0 \Psi_{1}=0, Ψ 1 \Psi_{1} changes signs at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id;

- (c)

Cycl ⁡ ( Γ, μ 0) ⩽ 1 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 1, if Ψ 2 ≠ 0 \Psi_{2}\neq 0;

- (d)

Cycl ⁡ ( Γ, μ 0) ⩾ 2 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 2, if Ψ 1 = Ψ 2 = 0 \Psi_{1}=\Psi_{2}=0, Ψ 1, Ψ 2 \Psi_{1},\;\Psi_{2} are independent at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id;

- (e)

Cycl ⁡ ( Γ, μ 0) ⩽ 2 {\rm Cycl}(\Gamma,\mu_{0})\leqslant 2, if Ψ 3 ≠ 0 \Psi_{3}\neq 0;

- (f)

Cycl ⁡ ( Γ, μ 0) ⩾ 3 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 3 if Ψ 1 = Ψ 2 = Ψ 3 = 0 \Psi_{1}=\Psi_{2}=\Psi_{3}=0, Ψ 1, Ψ 2, Ψ 3 \Psi_{1},\;\Psi_{2},\;\Psi_{3} are independent at μ 0 \mu_{0} and ℛ ⁡ ( ⋅, μ 0) ≢ I ​ d \mathscr{R}(\cdot;\mu_{0})\not\equiv Id.

###### Proof.

The expression of 𝒟 \mathscr{D} follows from Proposition 3. The proof of the statements about the cyclicity follows similarly to the proof of Theorems A and B (also also similarly to the proof of [12, Theorem A A]). ∎

We finish this section by observing that the first return and the displacement maps also shares another type of similarity. More precisely, from Theorems A and B it follows that the cyclicity of Γ \Gamma is governed by the zeros of the functions

 | Φ 1:= r ⁡ ( μ) − 1, Φ 2:= A 1, n − 1, Φ 3:= 𝒜, \Phi_{1}:=r(\mu)-1,\quad\Phi_{2}:=A_{1,n}-1,\quad\Phi_{3}:=\mathcal{A}, |  |

where we recall that 𝒜 = Λ m, n ​ A 1, m ​ A 1, n ​ ( S 1 m + 1 − S 2 m) \mathcal{A}=\Lambda_{m,n}A_{1,m}A_{1,n}(S_{1}^{m+1}-S_{2}^{m}). Therefore if we let Ψ 1 \Psi_{1}, Ψ 2 \Psi_{2} and Ψ 3 \Psi_{3} be given as in Theorem C, then one can apply the formulas ( 4) to verify that

 | V ⁡ ( Φ 1) = V ⁡ ( Ψ 1), V ⁡ ( Φ 1, Φ 2) = V ⁡ ( Ψ 1, Ψ 2), V ⁡ ( Φ 1, Φ 2, Φ 3) = V ⁡ ( Ψ 1, Ψ 2, Ψ 3), V(\Phi_{1})=V(\Psi_{1}),\quad V(\Phi_{1},\Phi_{2})=V(\Psi_{1},\Psi_{2}),\quad V(\Phi_{1},\Phi_{2},\Phi_{3})=V(\Psi_{1},\Psi_{2},\Psi_{3}), |  |

where we recall that V ⁡ ( f 1, …, f k) V(f_{1},\dots,f_{k}) denotes the variety defined by f 1, …, f k f_{1},\dots,f_{k} (see Definition 3).

## 8 An application in Game Theory

The notion of Evolutionary Stable States (ESS) was first introduced in the paper [22] by Smith and Price, in which they applied concepts of Game Theory into Biology. Roughly speaking, given a game with two or more players (modeling a conflict between species, for instance), an ESS is an strategy such that if most of the players follow it, then no other strategy would provide the other players higher advantages, that is, the best course of action for the other players is to also follow the ESS.

In 1978, Taylor and Jonker [24] approached the study of ESS in the scope of Ordinary Differential Equations. One of their significant contributions was the modeling of a multiple-player game by a system of differential equations. In particular, a game with two players can be modeled by a planar polynomial vector field. One of such models is given by the following polynomial system.

 | x ˙ = x ⁡ ( x − 1) ​ f ​ ( x, y), y ˙ = y ⁡ ( y − 1) ​ g ​ ( x, y). \begin{array}[]{l}\dot{x}=x(x-1)f(x,y),\\ \dot{y}=y(y-1)g(x,y).\end{array} |  | (40) |

In the context given by the model ( 40), the limit cycles have an important significance. Hofbauer et al. [9] proved that every ESS is an assymptotically stable singularity, while the converse does not hold. They also observed that there is no special distinction between ESS and assymptotically stability. Hence, one can study assymptotical stability rather than ESS. In this scenario, a stable limit cycle can be interpreted as an *oscillating stable strategy*. In this scope, the model ( 40) has been recently studied in several papers (for instance, [1, 2, 6]).

In the present work, we consider system ( 40) in the case which the boundary of the unit square is a hyperbolic polycycle. More precisely, we work with the family X μ X_{\mu} of vector fields associated to the following systems.

 | x ˙ = x ⁡ ( x − 1) ​ ( − 1 − ( λ 3 − 1) ​ x + y − ( λ 1 − λ 3) ​ x ​ y + λ 1 ​ y 2), y ˙ = y ⁡ ( y − 1) ​ ( λ 2 − ( λ 2 + μ 1) ​ x − ( λ 2 − 1) ​ y + ( μ 1 − 1) ​ x 2 + ( λ 2 − λ 4) ​ x ​ y). \begin{array}[]{l}\dot{x}=x\,(x-1)\biggl(-1-\left(\lambda_{3}-1\right)x+y-\left(\lambda_{1}-\lambda_{3}\right)xy+\lambda_{1}y^{2}\biggr),\\ \dot{y}=y\,(y-1)\biggl(\lambda_{2}-\left(\lambda_{2}+\mu_{1}\right)x-\left(\lambda_{2}-1\right)y+\left(\mu_{1}-1\right)x^{2}+\left(\lambda_{2}-\lambda_{4}\right)xy\biggr).\end{array} |  | (41) |

###### Theorem 2.

There exist parameter values μ 0 ∈ Λ \mu_{0}\in\Lambda, such that X μ X_{\mu} has two limit cycles bifurcating from the polycycle at the boundary of the unit square for μ ≈ μ 0 \mu\approx\mu_{0}.

###### Proof.

Consider the family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} associated to ( 41), with μ = ( λ 1, λ 2, λ 3, λ 4, μ 1) \mu=(\lambda_{1},\lambda_{2},\lambda_{3},\lambda_{4},\mu_{1}) and Λ = { λ i > 0: i ∈ { 1, …, 4 } } \Lambda=\{\lambda_{i}>0:i\in\{1,\dots,4\}\}. Denote by Γ \Gamma the boundary of [1, 0] 2 [1,0]^{2}. We have that Γ \Gamma is a persistent polycycle for the family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda}. Indeed, we have that the lines x = 0 x=0, x = 1 x=1, y = 0 y=0 and y = 1 y=1 are invariant through X μ X_{\mu}. Moreover, the points p 1 = ( 0, 1) p_{1}=(0,1), p 2 = ( 0, 0) p_{2}=(0,0), p 3 = ( 1, 0) p_{3}=(1,0) and p 4 = ( 1, 1) p_{4}=(1,1) are hyperbolic saddles since the Jacobian matrix of X μ X_{\mu} evaluated at p i p_{i} is given by

 | J ​ X μ ​ ( p 1) = ( − λ 1 0 0 1), J ​ X μ ​ ( p 2) = ( 1 0 0 − λ 2), JX_{\mu}(p_{1})=\left(\begin{array}[]{cc}-\lambda_{1}&0\\ 0&1\end{array}\right),\quad JX_{\mu}(p_{2})=\left(\begin{array}[]{cc}1&0\\ 0&-\lambda_{2}\end{array}\right), |  |

 | J ​ X μ ​ ( p 3) = ( − λ 3 0 0 1), J ​ X μ ​ ( p 4) = ( 1 0 0 − λ 4). JX_{\mu}(p_{3})=\left(\begin{array}[]{cc}-\lambda_{3}&0\\ 0&1\end{array}\right),\quad JX_{\mu}(p_{4})=\left(\begin{array}[]{cc}1&0\\ 0&-\lambda_{4}\end{array}\right). |  |

Since the quantities

 | λ 1 λ 1 − 1, λ 2 λ 2 − 1, 1 1 − λ 3, 1 1 − λ 4, \frac{\lambda_{1}}{\lambda_{1}-1},\;\frac{\lambda_{2}}{\lambda_{2}-1},\;\frac{1}{1-\lambda_{3}},\;\frac{1}{1-\lambda_{4}}, |  |

do not lie in the interval ( 0, 1) (0,1) for μ ∈ Λ \mu\in\Lambda, there are no singularities in Γ \Gamma besides p i p_{i}. Thus, Γ \Gamma is a persistent polycycle for μ ∈ Λ \mu\in\Lambda. Notice that Γ \Gamma is oriented counterclockwise.

Since Γ \Gamma is a square, simple translations and rotations suffice to put system ( 40) into the standard form ( 10). Thus, one can readily apply the formulas given in [13, Theorem A] to compute the coefficients Δ 00 i \Delta_{00}^{i}, Δ 10 i \Delta_{10}^{i} and Δ 01 i \Delta_{01}^{i} of each Dulac map D i ​ ( s, μ) D_{i}(s;\mu). We need to compute the functions r ⁡ ( μ) r(\mu), A 1, 4 ​ ( μ) A_{1,4}(\mu) of the return map, to study the cyclicity of Γ \Gamma. We have that

 | r ⁡ ( μ) \displaystyle r(\mu) | = λ 1 ​ λ 2 ​ λ 3 ​ λ 4, \displaystyle=\lambda_{1}\lambda_{2}\lambda_{3}\lambda_{4}, |  |

 | A 1, 4 ​ ( μ) \displaystyle A_{1,4}(\mu) | = exp ( 1 ( λ 1 − 1) ​ ( λ 2 − 1) ​ ( λ 3 − 1) ​ ( λ 4 − 1) ​ λ 1 ( ln ( λ 1 + 1) ( r ( μ) − 1) ( λ 4 − 1) ( λ 3 − 1) ⋅ \displaystyle=\exp\biggl(\frac{1}{(\lambda_{1}-1)(\lambda_{2}-1)(\lambda_{3}-1)(\lambda_{4}-1)\lambda_{1}}\bigg(\ln(\lambda_{1}+1)(r(\mu)-1)(\lambda_{4}-1)(\lambda_{3}-1)\cdot |  |

 |  | ( λ 2 − 1) ​ ( 1 − λ 1 2 ​ λ 4 + ( μ 1 + λ 4 − 2) ​ λ 1) + λ 1 ​ ( ln ⁡ ( 2) ​ ( λ 4 − 1) ​ ( λ 3 − 1) ​ ( λ 2 − 1) ​ ( 1 − μ 1) ​ r ​ ( μ) CLOSE \displaystyle(\lambda_{2}-1)(1-\lambda_{1}^{2}\lambda_{4}+(\mu_{1}+\lambda_{4}-2)\lambda_{1})+\lambda_{1}(\ln(2)(\lambda_{4}-1)(\lambda_{3}-1)(\lambda_{2}-1)(1-\mu_{1})r(\mu) |  |

 |  | − λ 2 ​ λ 3 ​ ( λ 4 − 1) ​ ( λ 3 − 1) ​ λ 4 ​ ( λ 2 − 1) ​ ( 1 − λ 1 2 ​ λ 4 + ( μ 1 + λ 4 − 2) ​ λ 1) ​ ln ⁡ ( λ 1) + ( λ 2 ​ λ 3 2 − 1 CLOSE \displaystyle-\lambda_{2}\lambda_{3}(\lambda_{4}-1)(\lambda_{3}-1)\lambda_{4}(\lambda_{2}-1)(1-\lambda_{1}^{2}\lambda_{4}+(\mu_{1}+\lambda_{4}-2)\lambda_{1})\ln(\lambda_{1})+(\lambda_{2}\lambda_{3}^{2}-1 |  |

 |  | OPEN + ( μ 1 − λ 2) ​ λ 3) ​ ( λ 4 − 1) ​ λ 4 ​ ( λ 1 − 1) ​ ( λ 2 − 1) ​ ln ⁡ ( λ 3) − ( λ 3 − 1) ​ ( ( λ 1 − 1) ​ ( λ 2 − 1) ​ ( λ 1 ​ λ 4 CLOSE CLOSE \displaystyle+(\mu_{1}-\lambda_{2})\lambda_{3})(\lambda_{4}-1)\lambda_{4}(\lambda_{1}-1)(\lambda_{2}-1)\ln(\lambda_{3})-(\lambda_{3}-1)((\lambda_{1}-1)(\lambda_{2}-1)(\lambda_{1}\lambda_{4} |  |

 |  | − ( λ 4 − 1) ( λ 4 λ 3 + 1)) ln ( λ 4) − ( λ 4 − 1) ( ( λ 2 − 1) ( − 1 + μ 1) ln ( 2) + λ 3 λ 4 ln ( λ 2) ⋅ \displaystyle-(\lambda_{4}-1)(\lambda_{4}\lambda_{3}+1))\ln(\lambda_{4})-(\lambda_{4}-1)((\lambda_{2}-1)(-1+\mu_{1})\ln(2)+\lambda_{3}\lambda_{4}\ln(\lambda_{2})\cdot |  |

 |  | ( λ 1 − 1) ( λ 1 λ 2 2 + λ 2 − 1)))))). \displaystyle(\lambda_{1}-1)(\lambda_{1}\lambda_{2}^{2}+\lambda_{2}-1))))\bigg)\biggr). |  |

For μ 0 = ( 8 27, 3 2, 3 2, 3 2, 2 5, 1625 162) \mu_{0}=(\frac{8}{27},\frac{3}{2},\frac{3}{2},\frac{3}{2},\frac{2}{5},\frac{1625}{162}), we have r ⁡ ( μ 0) = A 1, 4 ​ ( μ 0) = 1 r(\mu_{0})=A_{1,4}(\mu_{0})=1 and

 | rank ​ ( ∂ ( r − 1, A 1, 4 − 1) ∂ μ) μ = μ 0 = 2, {\rm rank}\left(\dfrac{\partial(r-1,A_{1,4}-1)}{\partial\mu}\right)_{\mu=\mu_{0}}=2, |  |

which implies that r − 1 r-1 and A 1, 4 − 1 A_{1,4}-1 are independent at μ 0 \mu_{0}. To check if Cycl ⁡ ( Γ, μ 0) ⩾ 2 {\rm Cycl}(\Gamma,\mu_{0})\geqslant 2, by Theorem A, we need to verify if the return map ℛ ⁡ ( s, μ 0) \mathscr{R}(s;\mu_{0}) is not identically the identity map. In order to do so, we compute the expression B ⁡ ( μ 0) = S 1 2 − S 2 1 B(\mu_{0})=S_{1}^{2}-S_{2}^{1}. Notice that for μ = μ 0 \mu=\mu_{0}, we are under the hypothesis of Theorem B and that B ⁡ ( μ 0) B(\mu_{0}) is a factor of 𝒜 ⁡ ( μ 0) \mathcal{A}(\mu_{0}) such that B ⁡ ( μ 0) ≠ 0 B(\mu_{0})\neq 0 implies 𝒜 ⁡ ( μ 0) ≠ 0 \mathcal{A}(\mu_{0})\neq 0. The full expression of B ⁡ ( μ 0) B(\mu_{0}) is too cumbersome, so we omit it from the text. Its numerical value up to 12 decimal places is B ⁡ ( μ 0) ≈ 6.20031365865 B(\mu_{0})\approx 6.20031365865. By Theorem B, we have that Cycl ⁡ ( Γ, μ 0) = 2 {\rm Cycl}(\Gamma,\mu_{0})=2. ∎

## Acknowledgments

The first author is supported by Fundação de Amparo à Pesquisa do Estado de São Paulo (grant number 2024/06926-7). The second is supported by Fundação de Amparo à Pesquisa do Estado de São Paulo (grant number 2021/01799-9)

## Conflict of interest

The authors declare that they have no conflict of interest.

## Appendix A Generalized Binomial Theorem

Given α ∈ ℂ \alpha\in\mathbb{C} and k ∈ ℤ ⩾ 0 k\in\mathbb{Z}_{\geqslant 0}, the *generalized binomial coefficient*is given by

 | ( α k) = α ⁡ ( α − 1) ​ … ​ ( α − k + 1) k!, \binom{\alpha}{k}=\frac{\alpha(\alpha-1)\dots(\alpha-k+1)}{k!}, |  | (42) |

with the convention ( α 0) = 1 \binom{\alpha}{0}=1. Observe that if α ∈ ℤ ⩾ k \alpha\in\mathbb{Z}_{\geqslant k}, then ( 42) reduces to the usual binomial coefficient.

###### Theorem 3 (Generalized Binomial Theorem).

Let x x, y y, α ∈ ℂ \alpha\in\mathbb{C} such that | x | > | y | |x|>|y|. Then

 | ( x + y) α = ∑ k = 0 ∞ ( α k) ​ x α − k ​ y k. (x+y)^{\alpha}=\sum_{k=0}^{\infty}\binom{\alpha}{k}x^{\alpha-k}y^{k}. |  |

###### Proof.

Since x ≠ 0 x\neq 0 it follows that t = y / x ∈ ℂ t=y/x\in\mathbb{C} is well defined and thus we can consider the holomorphic function f: ℂ → ℂ f\colon\mathbb{C}\to\mathbb{C} given by,

 | f ⁡ ( t) = ( 1 + t) α. f(t)=(1+t)^{\alpha}. |  |

From f ( k) ​ ( t) = α ⁡ ( α − 1) ​ … ​ ( α − k + 1) ​ ( 1 + t) α − k f^{(k)}(t)=\alpha(\alpha-1)\dots(\alpha-k+1)(1+t)^{\alpha-k} it follows that expanding f f in Maclaurin’s series we get

 | ( 1 + t) α = ∑ k = 0 ∞ f ( k) ​ ( 0) k! ​ t k = ∑ k = 0 ∞ α ⁡ ( α − 1) ​ … ​ ( α − k + 1) k! ​ t k = ∑ k = 0 ∞ ( α k) ​ t k, (1+t)^{\alpha}=\sum_{k=0}^{\infty}\frac{f^{(k)}(0)}{k!}t^{k}=\sum_{k=0}^{\infty}\frac{\alpha(\alpha-1)\dots(\alpha-k+1)}{k!}t^{k}=\sum_{k=0}^{\infty}\binom{\alpha}{k}t^{k}, |  |

with the series converging provided | t | < 1 |t|<1. The theorem now follows by replacing t = y / x t=y/x and multiplying the equation by x α x^{\alpha}. ∎

## Appendix B Coefficient expressions for the Dulac map

In this section, we present the explicit expressions for the coefficients Δ 00, Δ 10 \Delta_{00},\Delta_{10} and Δ 01 \Delta_{01} obtained by Marín and Villadelprat in [13, Theorem A]. Considering the vector field ( 10), we define the following functions:

 |  | L 1 ( u):= exp ∫ 0 u ( P ⁡ ( 0, y, μ) Q ⁡ ( 0, y, μ) + 1 λ) d ​ y y, \displaystyle L_{1}(u):=\exp\int_{0}^{u}\biggl(\frac{P(0,y;\mu)}{Q(0,y;\mu)}+\frac{1}{\lambda}\biggr)\frac{dy}{y}, |  | L 2 ( u):= exp ∫ 0 u ( Q ⁡ ( x, 0, μ) P ⁡ ( x, 0, μ) + λ) d ​ x x, \displaystyle L_{2}(u):=\exp\int_{0}^{u}\biggl(\frac{Q(x,0;\mu)}{P(x,0;\mu)}+\lambda\biggr)\frac{dx}{x}, |  |

 |  | M 1 ​ ( u):= L 1 ​ ( u) ​ ∂ x ( P Q) ​ ( 0, u), \displaystyle M_{1}(u):=L_{1}(u)\partial_{x}\left(\frac{P}{Q}\right)(0,u), |  | M 2 ​ ( u):= L 2 ​ ( u) ​ ∂ y ( Q P) ​ ( u, 0), \displaystyle M_{2}(u):=L_{2}(u)\partial_{y}\left(\frac{Q}{P}\right)(u,0), |  | (43) |

Let σ i ​ j ​ k \sigma_{ijk} denote the k k th derivative at s = 0 s=0 of the j j th component of the transverse section σ i = ( σ i, 1, σ i, 2) \sigma_{i}=(\sigma_{i,1},\sigma_{i,2}), more precisely,

 | σ i ​ j ​ k = ∂ s k σ i, j ​ ( 0, μ). \sigma_{ijk}=\partial_{s}^{k}\sigma_{i,j}(0;\mu). |  |

Now, we define the following quantities:

 |  | S 1:= σ 112 2 ​ σ 111 − σ 121 σ 120 ​ ( P Q) ​ ( 0, σ 120) − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120), \displaystyle S_{1}:=\frac{\sigma_{112}}{2\sigma_{111}}-\frac{\sigma_{121}}{\sigma_{120}}\left(\frac{P}{Q}\right)(0,\sigma_{120})-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120}), |  |

 |  | S 2:= σ 222 2 ​ σ 221 − σ 211 σ 210 ​ ( Q P) ​ ( σ 210, 0) − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210), \displaystyle S_{2}:=\frac{\sigma_{222}}{2\sigma_{221}}-\frac{\sigma_{211}}{\sigma_{210}}\left(\frac{Q}{P}\right)(\sigma_{210},0)-\frac{\sigma_{221}}{L_{2}(\sigma_{210})}\hat{M}_{2}(\lambda,\sigma_{210}), |  | (44) |

where M ^ i \hat{M}_{i} denotes a sort of incomplete Melin transform. We refer the reader to [13, Appendix B] for a detailed study. For our purposes, the following result suffices to perform accurate computations.

###### Proposition 4 ( [13, [Theorem B.1]).

Consider an open interval I ⊂ ℝ I\subset\mathbb{R} containing x = 0 x=0 and an open subset U ⊂ ℝ N U\subset\mathbb{R}^{N}.

- (a)

Given f ⁡ ( x, ν) ∈ 𝒞 ∞ ​ ( I × U) f(x;\nu)\in\mathscr{C}^{\infty}(I\times U), there exists a unique f ^ ​ ( α, x, ν) ∈ 𝒞 ∞ ​ ( ( ℝ ∖ ℤ ⩾ 0) × I × U) \hat{f}(\alpha,x;\nu)\in\mathscr{C}^{\infty}((\mathbb{R}\setminus\mathbb{Z}_{\geqslant 0})\times I\times U) such that

 | x ​ ∂ x f ^ ​ ( α, x, ν) − α ​ f ^ ​ ( α, x, ν) = f ⁡ ( x, ν); x\partial_{x}\hat{f}(\alpha,x;\nu)-\alpha\hat{f}(\alpha,x;\nu)=f(x;\nu); |  |

- (b)

If x ∈ I ∖ { 0 } x\in I\setminus\{0\}, then ∂ x ( f ^ ​ ( α, x, ν) ​ | x | − α) = f ⁡ ( x, ν) ​ | x | − α x \partial_{x}(\hat{f}(\alpha,x;\nu)|x|^{-\alpha})=f(x;\nu)\frac{|x|^{-\alpha}}{x} and, taking any k ∈ ℤ ⩾ 0 k\in\mathbb{Z}_{\geqslant 0}, with k > α k>\alpha,

 | f ^ ​ ( α, x, ν) = ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, ν) i! ​ ( i − α) ​ x i + | x | α ​ ∫ 0 x ( f ⁡ ( s, ν) − T 0 k − 1 ​ f ​ ( s, ν)) ​ | s | − α ​ d ​ s s, \hat{f}(\alpha,x;\nu)=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;\nu)}{i!(i-\alpha)}x^{i}+|x|^{\alpha}\int_{0}^{x}\biggl(f(s;\nu)-T^{k-1}_{0}f(s;\nu)\biggr)|s|^{-\alpha}\frac{ds}{s}, |  |

where T 0 k ​ f ​ ( x, ν) = ∑ i = 0 k 1 i! ​ ∂ x i f ⁡ ( 0, ν) ​ x i T^{k}_{0}f(x;\nu)=\sum_{i=0}^{k}\frac{1}{i!}\partial_{x}^{i}f(0;\nu)x^{i} is the k k th degree Taylor polynomial of f ⁡ ( x, ν) f(x;\nu) at x = 0 x=0;

- (c)

For each ( i 0, x 0, ν 0) ∈ ℤ × I × U (i_{0},x_{0};\nu_{0})\in\mathbb{Z}\times I\times U the function ( α, x, ν) ↦ ( i 0 − α) ​ f ^ ​ ( α, x, ν) (\alpha,x;\nu)\mapsto(i_{0}-\alpha)\hat{f}(\alpha,x;\nu) extends 𝒞 ∞ \mathscr{C}^{\infty} at ( i 0, x 0, ν 0) (i_{0},x_{0};\nu_{0}) and, moreover, it tends to 1 i 0! ​ ∂ x i 0 f ⁡ ( 0, ν 0) ​ x 0 i 0 \frac{1}{i_{0}!}\partial_{x}^{i_{0}}f(0;\nu_{0})x_{0}^{i_{0}} as ( α, x, ν) → ( i 0, x 0, ν 0) (\alpha,x;\nu)\to(i_{0},x_{0};\nu_{0});

- (d)

If f ⁡ ( x, ν) f(x;\nu) is analytic on I × U I\times U, then f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) is analytic on ( ℝ ∖ ℤ ⩾ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geqslant 0})\times I\times U. Finally, for each ( α 0, x 0, ν 0) ∈ ℤ ⩾ 0 × I × U (\alpha_{0},x_{0};\nu_{0})\in\mathbb{Z}_{\geqslant 0}\times I\times U, the function ( α, x, ν) ↦ ( α 0 − α) ​ f ^ ​ ( α, x, ν) (\alpha,x;\nu)\mapsto(\alpha_{0}-\alpha)\hat{f}(\alpha,x;\nu) extends analytically to ( α 0, x 0, ν 0) (\alpha_{0},x_{0};\nu_{0}).

The coefficients of the Dulac map are given by the next result.

###### Proposition 5 ( [13, Theorem A, item (b)]).

The coefficients Δ i ​ j \Delta_{ij} for ( i, j) ∈ { ( 0, 0), ( 1, 0), ( 0, 1) } (i,j)\in\{(0,0),(1,0),(0,1)\} of the Dulac map are given by

 | Δ 00 = σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120) ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ, Δ 01 = − ( Δ 00) 2 ​ S 2, Δ 10 = λ ​ Δ 00 ​ S 1. \Delta_{00}=\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}},\quad\Delta_{01}=-(\Delta_{00})^{2}S_{2},\quad\Delta_{10}=\lambda\Delta_{00}S_{1}. |  | (45) |

## Appendix C An ODE model in game theory

We now briefly present the construction of model ( 40). Let Γ 1, Γ 2 \Gamma_{1},\Gamma_{2} be two players and { X 1, X 2 } \{X_{1},X_{2}\}, { Y 1, Y 2 } \{Y_{1},Y_{2}\} be the respective *pure strategies*. We denote by a i ​ j ∗ ∈ ℝ a_{ij}^{\ast}\in\mathbb{R} the payoff of strategy X i X_{i} against Y j Y_{j} and by b i ​ j ∗ ∈ ℝ b_{ij}^{\ast}\in\mathbb{R} the payoff of strategy Y i Y_{i} against X j X_{j}. For each probabilistic vector of dimension two

 | x = ( x 1, x 2) ∈ S 2:= { ( x 1, x 2) ∈ ℝ 2: x 1 ⩾ 0, x 2 ⩾ 0, x 1 + x 2 = 1 }, x=(x_{1},x_{2})\in S^{2}:=\{(x_{1},x_{2})\in\mathbb{R}^{2}:x_{1}\geqslant 0,x_{2}\geqslant 0,x_{1}+x_{2}=1\}, |  |

we associate a *mix strategy*given by x 1 ​ X 1 + x 2 ​ X 2 x_{1}X_{1}+x_{2}X_{2}. Similarly, given y ∈ S 2 y\in S^{2}, we associate the respective mix strategy y 1 ​ Y 1 + y 2 ​ Y 2 y_{1}Y_{1}+y_{2}Y_{2}. Let

 | A ∗ = ( a 11 ∗ a 12 ∗ a 21 ∗ a 22 ∗), B ∗ = ( b 11 ∗ b 12 ∗ b 21 ∗ b 22 ∗), A^{\ast}=\left(\begin{array}[]{cc}a_{11}^{\ast}&a_{12}^{\ast}\\ a_{21}^{\ast}&a_{22}^{\ast}\end{array}\right),\quad B^{\ast}=\left(\begin{array}[]{cc}b_{11}^{\ast}&b_{12}^{\ast}\\ b_{21}^{\ast}&b_{22}^{\ast}\end{array}\right), |  |

be the *payoff matrices*. Given x, y ∈ S 2 x,y\in S^{2}, the *average payoff*of the mix strategy associated to x x against the mix strategy associated to y y is given by

 | ⟨ x, A ∗ ​ y ⟩ = a 11 ∗ ​ x 1 ​ y 1 + a 12 ∗ ​ x 1 ​ y 2 + a 21 ∗ ​ x 2 ​ y 1 + a 22 ∗ ​ x 2 ​ y 2, \langle x,A^{\ast}y\rangle=a_{11}^{\ast}x_{1}y_{1}+a_{12}^{\ast}x_{1}y_{2}+a_{21}^{\ast}x_{2}y_{1}+a_{22}^{\ast}x_{2}y_{2}, |  |

and the average payoff of the mix strategy associated to y y against the mix strategy associated to x x is given by

 | ⟨ y, B ∗ ​ x ⟩ = b 11 ∗ ​ x 1 ​ y 1 + b 12 ∗ ​ x 1 ​ y 2 + b 21 ∗ ​ x 2 ​ y 1 + b 22 ∗ ​ x 2 ​ y 2. \langle y,B^{\ast}x\rangle=b_{11}^{\ast}x_{1}y_{1}+b_{12}^{\ast}x_{1}y_{2}+b_{21}^{\ast}x_{2}y_{1}+b_{22}^{\ast}x_{2}y_{2}. |  |

The dynamics between players Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2} is defined by the system of differential equations,

 | x ˙ 1 = x 1 ( ⟨ e 1, A ∗ y ⟩ − ⟨ x, A ∗ y ⟩), y ˙ 1 = y 1 ( ⟨ e 1, B ∗ x ⟩ − ⟨ y, B ∗ x ⟩), x ˙ 2 = x 2 ( ⟨ e 2, A ∗ y ⟩ − ⟨ x, A ∗ y ⟩), y ˙ 2 = y 2 ( ⟨ e 2, B ∗ x ⟩ − ⟨ y, B ∗ x ⟩). \begin{array}[]{l}\dot{x}_{1}=x_{1}\left(\langle e_{1},A^{\ast}y\rangle-\langle x,A^{\ast}y\rangle\right),\qquad\dot{y}_{1}=y_{1}\left(\langle e_{1},B^{\ast}x\rangle-\langle y,B^{\ast}x\rangle\right),\\ \dot{x}_{2}=x_{2}\left(\langle e_{2},A^{\ast}y\rangle-\langle x,A^{\ast}y\rangle\right),\qquad\dot{y}_{2}=y_{2}\left(\langle e_{2},B^{\ast}x\rangle-\langle y,B^{\ast}x\rangle\right).\end{array} |  | (46) |

Essentially, the weight x i x_{i} of the pure strategy X i X_{i} depends on the difference between the payoffs of the pure strategy and the mix strategy. In other words, the bigger this difference, the more superior strategy X i X_{i} is. Since x 1 + x 2 = y 1 + y 2 = 1 x_{1}+x_{2}=y_{1}+y_{2}=1, one can consider only the variables x 1, y 1 x_{1},y_{1} to study the dynamics of the game. Thus, ( 46) simplifies to

 | x ˙ = x ⁡ ( x − 1) ​ ( a 22 ∗ − a 12 ∗ + ( a 12 ∗ + a 21 ∗ − a 11 ∗ − a 22 ∗) ​ y), y ˙ = y ⁡ ( y − 1) ​ ( b 22 ∗ − b 12 ∗ + ( b 12 ∗ + b 21 ∗ − b 11 ∗ − b 22 ∗) ​ x). \begin{array}[]{l}\dot{x}=x(x-1)\left(a_{22}^{\ast}-a_{12}^{\ast}+(a_{12}^{\ast}+a_{21}^{\ast}-a_{11}^{\ast}-a_{22}^{\ast})y\right),\\ \dot{y}=y(y-1)\left(b_{22}^{\ast}-b_{12}^{\ast}+(b_{12}^{\ast}+b_{21}^{\ast}-b_{11}^{\ast}-b_{22}^{\ast})x\right).\end{array} |  |

The search for more realistic models demanded that the payoffs depended on the weights given to strategies X i X_{i} and Y j Y_{j} rather than being constants, i.e. a i ​ j ∗ = a i ​ j ∗ ​ ( x, y) a_{ij}^{\ast}=a_{ij}^{\ast}(x,y) and b i ​ j ∗ = b i ​ j ∗ ​ ( x, y) b_{ij}^{\ast}=b_{ij}^{\ast}(x,y). Hence, assuming a i ​ j ∗, b i ​ j ∗ a_{ij}^{\ast},b_{ij}^{\ast} polynomial, the model is generally written as system ( 40).

By the above construction, to investigate the dynamics between the players Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2}, it is sufficient to study system ( 40) in the unit square, i.e. ( x, y) ∈ [0, 1] 2 (x,y)\in[0,1]^{2}.

## References

- [1] J. Bastos, C. Buzzi, and P. Santana, Evolutionary stable strategies and cubic vector fields, NoDEA Nonlinear Differential Equations Appl., 31 (2024), pp. Paper No. 13, 54.
- [2], On structural stability of evolutionary stable strategies, J. Differential Equations, 389 (2024), pp. 190–227.
- [3] C. Buzzi, A. Gasull, and P. Santana, On the cyclicity of hyperbolic polycycles, J. Differential Equations, 429 (2025), pp. 646–677.
- [4] P. De Maesschalck, F. Dumortier, and R. Roussarie, Cyclicity of common slow-fast cycles, Indag. Math. (N.S.), 22 (2011), pp. 165–206.
- [5] F. Dumortier, R. Roussarie, and C. Rousseau, Elementary graphics of cyclicity 1 and 2, Nonlinearity, 7 (1994), p. 1001.
- [6] A. Gasull, L. F. Gouveia, and P. Santana, On the limit cycles of a quartic model for evolutionary stable strategies, Nonlinear Analysis: Real World Applications, 84 (2025), p. 104313.
- [7] A. Gasull, V. Mañosa, and F. Mañosas, Stability of certain planar unbounded polycycles, J. Math. Anal. Appl., 269 (2002), pp. 332–351.
- [8] A. Gasull, V. Mañosa, and J. Villadelprat, On the period of the limit cycles appearing in one-parameter bifurcations, J. Differential Equations, 213 (2005), pp. 255–288.
- [9] J. Hofbauer, P. Schuster, and K. Sigmund, A note on evolutionary stable strategies and game dynamics, J Theor Biol., (1979), pp. 609–12.
- [10] D. Marín and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: local setting, J. Differential Equations, 269 (2020), pp. 8425–8467.
- [11], Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: general setting, J. Differential Equations, 275 (2021), pp. 684–732.
- [12], On the cyclicity of kolmogorov polycycles, Electron. J. Qual. Theory Differ. Equ., 35 (2022), pp. 1–31.
- [13], Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: coefficient properties, J. Differential Equations, 404 (2024), pp. 43–107.
- [14] D. Marín, L. Queiroz, and J. Villadelprat, The period of the limit cycle bifurcating from a persistent polycycle, 2023.
- [15] A. Mourtada, Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan: mise sous forme normale, in Bifurcations of planar vector fields (Luminy, 1989), vol. 1455 of Lecture Notes in Math., Springer, Berlin, 1990, pp. 272–314.
- [16], Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan. Algorithme de finitude, Ann. Inst. Fourier (Grenoble), 41 (1991), pp. 719–753.
- [17], Bifurcation de cycles limites au voisinage de polycycles hyperboliques et génériques à trois sommets, Ann. Fac. Sci. Toulouse Math. (6), 3 (1994), pp. 259–292.
- [18], Degenerate and non-trivial hyperbolic polycycles with two vertices, J. Differential Equations, 113 (1994), pp. 68–83.
- [19] D. Panazzolo, Solutions of the equation a n + ( a n − 1 + ⋯ ( a 2 + ( a 1 + x r 1) r 2) ⋯) r n = b x a_{n}+(a_{n-1}+\cdots(a_{2}+(a_{1}+x^{r_{1}})^{r_{2}})\cdots)^{r_{n}}=bx, São Paulo J. Math. Sci., 18 (2024), pp. 1505–1526.
- [20] R. Roussarie, A note on finite cyclicity property and Hilbert’s 16th problem, in Dynamical systems, Valparaiso 1986, vol. 1331 of Lecture Notes in Math., Springer, Berlin, 1988, pp. 161–168.
- [21] C. Rousseau, G. Świrszcz, and H. Żoładek, Cyclicity of graphics with semi-hyperbolic points inside quadratic systems, J. Dynam. Control Systems, 4 (1998), pp. 149–189.
- [22] J. Smith and G. Price, The logic of animal conflict, Nature, 246 (1973), pp. 15–18.
- [23] J. Sotomayor, Curvas definidas por equações diferenciais no plano, Instituto de Matemática Pura e Aplicada, Conselho Nacional de Desenvolvimento Científico e Tecnológico, Rio de Janeiro, 1981. 13 o Colóquio Brasileiro de Matemática. [13th Brazilian Mathematics Colloquium].
- [24] P. D. Taylor and L. B. Jonker, Evolutionary stable strategies and game dynamics, Mathematical Biosciences, 40 (1978), pp. 145–156.
- [25] L. A. Č erkas, The stability of singular cycles, Differencial’nye Uravnenija, 4 (1968), pp. 1012–1017.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
