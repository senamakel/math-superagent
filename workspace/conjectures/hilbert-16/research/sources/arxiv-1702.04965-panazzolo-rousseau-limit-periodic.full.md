<!-- source: https://arxiv.org/html/1702.04965 | converted from HTML -->

Topological classification of limit periodic sets of polynomial planar vector fields

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1702.04965v2 [math.CA] 14 Nov 2017

# Topological classification of limit periodic sets of polynomial planar vector fields

André Belotto da Silva and Jose Ginés Espín Buendía Address: AB: Université Paul Sabatier, Institut de Mathématiques de Toulouse, 118 route de Narbonne, F-31062 Toulouse Cedex 9, France Email address, A. Belotto : [andre.belotto_da_silva@math.univ-toulouse.fr][3] Address: JE: Universidad de Murcia, Departamento de Matemáticas, Campus de Espinardo, 30100 Murcia, Spain Email address, J. G. Espín : [josegines.espin@um.es][4]

###### Key words and phrases:

Limit Periodic Sets, Ordinary Differential Equations, Semi-algebraic sets

###### 2010 Mathematics Subject Classification

Primary 34C07, 34C08; Secondary 14P10, 37G15

## Abstract

We characterize the limit periodic sets of families of algebraic planar vector fields up to homeomorphisms. We show that any limit periodic set is topologically equivalent to a compact and connected semialgebraic set of the sphere of dimension 0 0 or 1 1. Conversely, we show that any compact and connected semialgebraic set of the sphere of dimension 0 0 or 1 1 can be realized as a limit periodic set.

## 1. Introduction

The subject of this manuscript is the structure of limit periodic sets of planar polynomial vector fields, a central object in bifurcation theory and in the treatment of the Hilbert 16 t ​ h 16^{th} problem (see Roussarie’s book [15] or Il’yashenko and Yakovenko’s book [7]). For example, the program of Dumortier, Roussarie and Rousseau [6] to solve the existential part of the 16 t ​ h 16^{th} Hilbert problem for quadratic vector fields is divided in 121 121 case-by-case analysis based on the limit periodic sets. Following the spirit of [9], [10] or [13], our objective is to characterize topologically all limit periodic sets of polynomial families of planar vector fields.

We consider a real algebraic manifold Λ \Lambda of dimension n ≥ 1 n\geq 1, which we call parameter space. A family of planar vector fields ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda}, is a vector field X λ X_{\lambda} defined on ℝ 2 × Λ \mathbb{R}^{2}\times\Lambda which is tangent to the fibres of the projection π: ℝ 2 × Λ → Λ \pi:\mathbb{R}^{2}\times\Lambda\to\Lambda. For any parameter λ 0 ∈ Λ \lambda_{0}\in\Lambda, we denote by X λ 0 X_{\lambda_{0}} the restriction of X λ X_{\lambda} to ℝ 2 × { λ 0 } \mathbb{R}^{2}\times\{\lambda_{0}\}, which we identify with ℝ 2 \mathbb{R}^{2}. We say that the family ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda} is polynomial if for each λ 0 ∈ Λ \lambda_{0}\in\Lambda there exist local coordinate systems x = ( x 1, x 2) x=(x_{1},x_{2}) of ℝ 2 \mathbb{R}^{2} and λ = ( λ 1, …, λ n) \lambda=(\lambda_{1},\ldots,\lambda_{n}) centered at λ 0 \lambda_{0} such that X λ ( x) = A 1 ( x, λ) ∂ x 1 + A 2 ( x, λ) ∂ x 2 X_{\lambda}(x)=A_{1}(x,\lambda)\partial_{x_{1}}+A_{2}(x,\lambda)\partial_{x_{2}} where A 1 A_{1} and A 2 A_{2} are polynomials.

Given any polynomial vector field X X on ℝ 2 \mathbb{R}^{2}, we shall extend it to an analytic vector field, which we denote by X ^ \hat{X}, in the sphere 𝕊 2 \mathbb{S}^{2} via a Bendixson compactification (see details in Section 2.1). Also, for every A ⊂ ℝ 2 A\subset\mathbb{R}^{2}, we will write A ^ \hat{A} to denote the closure of A A seen as a subset in the one-point compactification 𝕊 2 \mathbb{S}^{2} of ℝ 2 \mathbb{R}^{2}.

We recall the definition of limit periodic sets, which was first introduced by Françoise and Pugh [8, pp. 141].

###### Definition 1.1.

A limit periodic set for a polynomial family of planar vector fields ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda} at the parameter λ 0 \lambda_{0} is a closed set Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} for which there exist a sequence ( λ n) n (\lambda_{n})_{n} in the parameter space Λ \Lambda and a sequence ( γ n) n (\gamma_{n})_{n} of topological circles in ℝ 2 \mathbb{R}^{2} such that ( λ n) n (\lambda_{n})_{n} converges to λ 0 \lambda_{0} in Λ \Lambda, ( γ n) n (\gamma_{n})_{n} converges to Γ ^ \hat{\Gamma} in the Hausdorff topology of 𝕊 2 \mathbb{S}^{2} and, for every n n, the vector field X λ n X_{\lambda_{n}} has γ n \gamma_{n} as a limit cycle.

In terms of the structure of limit periodic sets, it is well-known that the Poincaré-Bendixson Theorem implies:

###### Proposition 1.2.

(See [8, Proposition 1]) Let ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda} be a polynomial family of planar vector fields and Γ \Gamma be a limit periodic set at the parameter λ 0 \lambda_{0}. Then Γ ^ \hat{\Gamma} is one of the following: (i) a singular point of X ^ λ 0 \hat{X}_{\lambda_{0}}; (ii) a periodic orbit of X ^ λ 0 \hat{X}_{\lambda_{0}}; (iii) a polycycle of X ^ λ 0 \hat{X}_{\lambda_{0}} (that is, a cyclic ordered collection of singular points a 1, …, a k a_{1},\ldots,a_{k} and arcs, given by integral curves, connecting them in the specific order: the j j th arc connects a j a_{j} with a j + 1 a_{j+1}); (iv) a degenerate limit cycle, that is, it contains non-isolated singularities of the vector field X ^ λ 0 \hat{X}_{\lambda_{0}}.

While the above Proposition provides some key information about the nature of limit periodic sets, it does not fully characterize them. The present paper intends to fulfils this gap. A first characterization was provided by Panazzolo and Roussarie in [14], under the additional hypothesis that the first jet of the singular points of X λ 0 X_{\lambda_{0}} is non-vanishing. In the same paper, the authors also showed a first example of a limit periodic set which is not topologically in the list of possibilities of the Poincaré-Bendixson Theorem [14, Example 3.1]. Going further, in [2], the first author has presented a class of examples of limit periodic sets which, topologically, are not in the list of possibilities of Poincaré-Bendixson Theorem either. Here, we improve and generalize the construction of [2] in order to prove the converse of our main result:

###### Theorem 1.3.

Let ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda} be a polynomial family of planar vector fields and Γ \Gamma a limit periodic set. Then there exists a homeomorphism φ: 𝕊 2 → 𝕊 2 \varphi:\mathbb{S}^{2}\to\mathbb{S}^{2} such that φ ⁡ ( Γ ^) \varphi(\hat{\Gamma}) is a compact and connected semialgebraic set of dimension 0 0 or 1 1.

Conversely, if Γ \Gamma is a non-empty closed semialgebraic subset of ℝ 2 \mathbb{R}^{2} of dimension 0 0 or 1 1 whose compactification Γ ^ ⊂ 𝕊 2 \hat{\Gamma}\subset{\mathbb{S}^{2}} is connected, there exists a polynomial family of planar vector fields ( X λ) λ ∈ Λ (X_{\lambda})_{\lambda\in\Lambda} having Γ \Gamma as a limit periodic set.

The following example illustrates the construction performed in Section 3 to prove the converse of Theorem 1.3.

###### Example 1.4.

Let Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} be the semi-algebraic set given by:

 | Γ = { ( x, y) ∈ ℝ 2; f ( x, y) = y ( x 2 + y 2 − 1) = 0 and g ( x, y) = x 2 + y 2 ≤ 4 }. \Gamma=\left\{(x,y)\in\mathbb{R}^{2};\,f(x,y)=y(x^{2}+y^{2}-1)=0\text{ and }g(x,y)=x^{2}+y^{2}\leq 4\right\}. |  |

Following the notation of Subsection 3.2, we consider the set of points

 | S = { ( − 2, 0), ( 2, 0), ( 0, 1), ( 0, − 1) } S=\{(-2,0),(2,0),(0,1),(0,-1)\} |  |

(where notice that S = G ​ e ​ n ​ ( Γ) ∪ T ​ r ​ ( Γ) S=Gen(\Gamma)\cup Tr(\Gamma) and N ​ G ​ ( Γ) = ∅ NG(\Gamma)=\emptyset, see Definition 3.1). Now, consider the three variable polynomial

 | h ⁡ ( x, y, λ) = f ​ ( x, y) 2 − λ ​ ∏ p ∈ S ( ‖ ( x, y) − p ‖ 2 − λ 2) h(x,y,\lambda)=f(x,y)^{2}-\lambda\prod_{p\in S}\left(\|(x,y)-p\|^{2}-\lambda^{2}\right) |  |

where λ \lambda will play the role of the parameter of the family of vector fields. Let t ∈ ℝ + t\in\mathbb{R}^{+} and note that the level curves Z t = { ( x, y) ∈ ℝ 2; h ⁡ ( x, y, t) = 0 } Z_{t}=\{(x,y)\in\mathbb{R}^{2};\,h(x,y,t)=0\} are connected and converge (in the Hausdorff topology) to Γ \Gamma when t t goes to zero (c.f. Proposition 3.7; see Figure 1). It follows that the perturbation of the Hamiltonian vector field given by

 | X λ = ( ∂ h ∂ y + h ∂ h ∂ x) ∂ x + ( − ∂ h ∂ x + h ∂ h ∂ y) ∂ y X_{\lambda}=\left(\frac{\partial h}{\partial y}+h\frac{\partial h}{\partial x}\right)\partial_{x}+\left(-\frac{\partial h}{\partial x}+h\frac{\partial h}{\partial y}\right)\partial_{y} |  |

is an polynomial family of planar vector fields which has Γ \Gamma as a limit periodic set for the parameter λ 0 = 0 \lambda_{0}=0 (for every t > 0 t>0, the set Z t Z_{t} is a limit cycle for X t X_{t}).

Γ \Gamma Figure 1. Limit cycles for λ = 0.001 \lambda=0.001 (red) and λ = 0.0001 \lambda=0.0001 (blue) approaching the limit periodic set Γ \Gamma.

The rest of the paper is divided as follows. In Subsection 1.1 we present some remarks about Theorem 1.3; the aim of Section 2 is to prove the direct implication of Theorem 1.3 while Section 3 deals with the converse one.

### 1.1. Remarks

- (I)

If we restrict our study to compact limit periodic sets of the plane, Theorem 1.3 can be extended to the analytic category. More precisely, with the same ideas and techniques, it is not difficult to show that a compact limit periodic set for an analytic family of vector fields is topologically equivalent to a compact and connected semianalytic set of dimension 0 0 or 1 1; conversely, every compact and connected semianalytic set of dimension 0 0 or 1 1 can be realized as a limit periodic set for an analytic family of vector fields.

- (II)

On the other hand, Theorem 1.3 does not extend, in a trivial, to unbounded limit periodic sets for families of analytic vector fields. The difficulty relies on proving the converse part of the theorem. Let us first exemplify how our methods could be adapted to some unbounded analytic varieties: we claim that the set

 | Γ 1 = { ( x, y) ∈ ℝ 2; f 1 ( x, y) = y 2 − sin ( x) 2 = 0 } \Gamma_{1}=\{(x,y)\in\mathbb{R}^{2};\,f_{1}(x,y)=y^{2}-\sin(x)^{2}=0\} |  |

can be realized as a limit periodic set for an analytic family. Indeed, it suffices to replace the function h h in Section 3.2 by

 | h ⁡ ( x, y, λ, α) = f 1 ​ ( x, y) 2 − λ ⁡ ( 1 − α 2 ​ ( x 2 + y 2)). h(x,y,\lambda,\alpha)=f_{1}(x,y)^{2}-\lambda\left(1-\alpha^{2}(x^{2}+y^{2})\right). |  |

We leave it to the reader to verify that the ideas of Sections 3.2 and 3.3 can be adapted to this function. Nevertheless, it is unclear which connected subsets of

 | Γ 2 = { ( x, y) ∈ ℝ 2; f 2 ( x, y) = y 3 − y sin ( x) 2 = 0 } \Gamma_{2}=\{(x,y)\in\mathbb{R}^{2};\,f_{2}(x,y)=y^{3}-y\sin(x)^{2}=0\} |  |

can be realized as limit periodic sets. Technically, the difficulty is that our construction for Γ 2 \Gamma_{2} would demand the use of transition points (defined in the last paragraph of Section 3.1); but the set of those transition points T ​ r ​ ( Γ 2) Tr(\Gamma_{2}) would need to be infinite in this case.

- (III)

A description of the limit periodic sets Γ \Gamma in the spirit of Proposition 1.2 follows, under the hypotehsis that X λ 0 ≢ 0 X_{\lambda_{0}}\not\equiv 0, from the proof of Lemma 2.6 below. More precisely, with the notation of the direct implication in Theorem 1.3, a limit periodic set Γ \Gamma must be a finite union ⋃ i = 1 m S i ∪ ⋃ j = 1 n γ j \bigcup_{i=1}^{m}S_{i}\cup\bigcup_{j=1}^{n}\gamma_{j}, for some m, n ∈ ℕ m,\,n\in\mathbb{N}, where each S i S_{i} is a connected semi-algebraic subsets of the set of singularities of X ^ λ 0 \hat{X}_{\lambda_{0}} and each γ j \gamma_{j} is a regular orbit of X ^ λ 0 \hat{X}_{\lambda_{0}} which converge to a singular points in ⋃ i = 1 m S i \bigcup_{i=1}^{m}S_{i}. Even more, each γ j \gamma_{j} is characteristic in both extremes; that is, when the orbit is run in either negative or positive time, the orbit converges in a well-defined direction to a singular point of X ^ λ 0 \hat{X}_{\lambda_{0}} and, in a sufficiently small neighbourhood of that limit point, γ j \gamma_{j} is the frontier of a parabolic or hyperbolic sector.

Acknowledgements. We would like to thank the anonymous referee for the useful comments and the University of Toronto for its hospitality. The work of the first author is supported by LabEx CIMI. The second author is supported by Fundación Séneca through the program “Contratos Predoctorales de Formación del Personal Investigador”, grant 18910/FPI/13 and by the MINECO grants MTM2014-52920-P.

## 2. Topology of limit periodic Sets

Along the Section, the reader is assumed to be familiar with some background in elementary Planar Qualitative Theory of Differential Equations; regarding this, [5] is a good reference.

In Subsection 2.1, we recall the constructions of the Bendixson compactification of a polynomial vector field on ℝ 2 \mathbb{R}^{2}. Subsection 2.2 is devoted to present the notion of real semialgebraic sets and some of their elementary properties and, finally, in Subsection 2.3, we prove the direct part of Theorem 1.3

### 2.1. Bendixson Compactification

For the sake of simplicity, we present an adaptation of [15, Section 1.1.3.2] using real analysis notation.

The one-point compactification of the euclidean plane ℝ ∞ 2 = ℝ 2 ∪ { ∞ } \mathbb{R}^{2}_{\infty}=\mathbb{R}^{2}\cup\{\infty\} can be seen as a real analytic compact surface. Indeed, it is enough to consider the two local charts ( ℝ 2, z) (\mathbb{R}^{2},z) and ( ℝ ∞ 2 ∖ { 0 }, Z) (\mathbb{R}^{2}_{\infty}\setminus\{0\},Z) where z: ℝ 2 → ℝ 2 z:\mathbb{R}^{2}\to\mathbb{R}^{2} is the map given by the formula z ⁡ ( x, y) = ( r ⁡ ( x, y), s ⁡ ( x, y)) = ( x, y) z(x,y)=(r(x,y),s(x,y))=(x,y) for every ( x, y) ∈ ℝ 2 (x,y)\in\mathbb{R}^{2} and Z: ℝ ∞ 2 ∖ { 0 } → ℝ 2 Z:\mathbb{R}^{2}_{\infty}\setminus\{0\}\to\mathbb{R}^{2} is given by Z ( x, y) = ( u ( x, y), v ( x, y)) = ( x / ( x 2 + y 2), − y / ( x 2 + y 2)) Z(x,y)=(u(x,y),v(x,y))=(x/(x^{2}+y^{2}),-y/(x^{2}+y^{2})) if ( x, y) ≠ ∞ (x,y)\neq\infty and Z ⁡ ( ∞) = ( u ⁡ ( ∞), v ⁡ ( ∞)) = 0 Z(\infty)=(u(\infty),v(\infty))=0. The equations for the changes of coordinates z ∘ Z − 1: ℝ 2 ∖ { 0 } → ℝ 2 ∖ { 0 } z\circ Z^{-1}:\mathbb{R}^{2}\setminus\{0\}\to\mathbb{R}^{2}\setminus\{0\} and Z ∘ z − 1: ℝ 2 ∖ { 0 } → ℝ 2 ∖ { 0 } Z\circ z^{-1}:\mathbb{R}^{2}\setminus\{0\}\to\mathbb{R}^{2}\setminus\{0\} are given by the analytic formulas r = u / ( u 2 + v 2) r=u/(u^{2}+v^{2}) and s = − v / ( u 2 + v 2) s=-v/(u^{2}+v^{2}) and u = r / ( r 2 + s 2) u=r/(r^{2}+s^{2}) and v = − s / ( r 2 + s 2) v=-s/(r^{2}+s^{2}) respectively; this justifies that { ( ℝ 2, z), ( ℝ ∞ 2 ∖ { 0 }, Z) } \{(\mathbb{R}^{2},z),(\mathbb{R}^{2}_{\infty}\setminus\{0\},Z)\} is an analytic atlas for ℝ ∞ 2 \mathbb{R}^{2}_{\infty}. We denote by ϕ: ℝ ∞ 2 → ℝ ∞ 2 \phi:\mathbb{R}^{2}_{\infty}\to\mathbb{R}^{2}_{\infty} the homeomorphism associated to this transition map (where ϕ ⁡ ( 0) = ∞ \phi(0)=\infty and ϕ ⁡ ( ∞) = 0 \phi(\infty)=0; ; we will call ϕ \phi the transition homeomorphism associated to the Bendixson compactification.

We will also refer to ℝ ∞ 2 \mathbb{R}^{2}_{\infty} as 𝕊 2 {\mathbb{S}^{2}} and we shall call it the Bendixson compactification of ℝ 2 \mathbb{R}^{2}. This notation is justify by the fact that ℝ ∞ 2 \mathbb{R}^{2}_{\infty} is analytically diffeomorphic to the standard euclidean unit sphere 𝕊 2 = { ( x, y, z) ∈ ℝ 3: x 2 + y 2 + z 2 = 1 } \mathbb{S}^{2}=\{(x,y,z)\in\mathbb{R}^{3}:x^{2}+y^{2}+z^{2}=1\}: as a explicit analytic diffeomorphism we may consider the map ψ: 𝕊 2 → ℝ ∞ 2 \psi:\mathbb{S}^{2}\to\mathbb{R}^{2}_{\infty} given by the formulas ψ ⁡ ( 0, 0, 1) = ∞ \psi(0,0,1)=\infty and ψ ⁡ ( x, y, z) = ( x / ( 1 − z), y / ( 1 − z)) \psi(x,y,z)=(x/(1-z),y/(1-z)) if ( x, y, z) ≠ ( 0, 0, 1) (x,y,z)\neq(0,0,1). If we denote by d 2 d_{2} the standard euclidean distance on ℝ 3 \mathbb{R}^{3}, it follows that ℝ ∞ 2 \mathbb{R}^{2}_{\infty}, with its natural topology as the one-point compactification of ℝ 2 \mathbb{R}^{2}, is a metrizable space; and as a compatible distance we can take the one given by d ⁡ ( a, b) = d 2 ​ ( ψ − 1 ​ ( a), ψ − 1 ​ ( b)) d(a,b)=d_{2}(\psi^{-1}(a),\psi^{-1}(b)) for every a, b ∈ ℝ ∞ 2 a,b\in\mathbb{R}^{2}_{\infty}.

Let P P and Q Q be real polynomials in two variables and consider the algebraic planar vector field given by X = P ∂ x + Q ∂ y X=P\partial_{x}+Q\partial_{y}. If d = max ⁡ { deg ⁡ ( P), deg ⁡ ( Q) } d=\max\{\deg(P),\deg(Q)\}, we may consider a vector field in the amplified euclidean plane ℝ ∞ 2 \mathbb{R}^{2}_{\infty}, X ^ \hat{X}, given by the formulas X ^ ( r, s) = 1 1 + ( r 2 + s 2) d ( P ( r, s) ∂ r + Q ( r, s) ∂ s) \hat{X}(r,s)=\frac{1}{1+(r^{2}+s^{2})^{d}}\left(P(r,s)\partial_{r}+Q(r,s)\partial_{s}\right) if ( r, s) ∈ ℝ ∞ 2 ∖ { ∞ } (r,s)\in\mathbb{R}^{2}_{\infty}\setminus\{\infty\} and X ^ ​ ( ∞) = 0 \hat{X}(\infty)=0. It is direct to show that X ^ \hat{X} is well-defined and analytic in the whole ℝ ∞ 2 \mathbb{R}^{2}_{\infty}.

### 2.2. Semialgebraic sets

Let x = ( x 1, …, x n) x=(x_{1},\ldots,x_{n}) be a coordinate system of ℝ n \mathbb{R}^{n}. Given any polynomial f f on ℝ n \mathbb{R}^{n} we shall say that ( f ⁡ ( x) = 0) = { x ∈ ℝ n: f ⁡ ( x) = 0 } (f(x)=0)=\{x\in\mathbb{R}^{n}:\,f(x)=0\} is a algebraic set. A more general concept is the following one.

###### Definition 2.1.

(See [3, Section 1]). A subset Z ⊂ ℝ n Z\subset\mathbb{R}^{n} is *semialgebraic*if there exist polynomials f i f_{i} and g i ​ j g_{ij} on ℝ n \mathbb{R}^{n}, i = 1, …, p i=1,\ldots,p and j = 1, …, q j=1,\ldots,q, such that

 | Z = ⋃ i = 1 p ⋂ j = 1 q { x ∈ ℝ n: f i ​ ( x) = 0 ​ and ​ g i ​ j ​ ( x) > 0 }. Z=\bigcup_{i=1}^{p}\bigcap_{j=1}^{q}\{x\in\mathbb{R}^{n}:\,f_{i}(x)=0\text{ and }g_{ij}(x)>0\}. |  |

A set Z ⊂ 𝕊 2 ⊂ ℝ 3 Z\subset\mathbb{S}^{2}\subset\mathbb{R}^{3} is said to be semialgebraic if Z Z is a semialgebraic set of ℝ 3 \mathbb{R}^{3}.

A fist collection of examples of semialgebraic sets is given by the finite unions of arcs linear by parts. For every a, b ∈ ℝ 2 a,b\in\mathbb{R}^{2}, we will denote [a, b] = { a + s ​ b: 0 ≤ s ≤ 1 } [{a},{b}]=\{{a}+s{b}:0\leq s\leq 1\}, the straight arc joining a {a} and b {b}. Let a 1, …, a n {a}_{1},\ldots,{a}_{n} be points in ℝ 2 \mathbb{R}^{2} and call l j = [a j, a j + 1] l_{j}=[{a}_{j},{a}_{j+1}] for any 1 ≤ j ≤ n − 1 1\leq j\leq n-1. If l j ∩ l j ′ = ∅ l_{j}\cap l_{j^{\prime}}=\emptyset when | j − j ′ | ≠ 1 \left|j-j^{\prime}\right|\neq 1 and l j ∩ l j + 1 = { a j + 1 } l_{j}\cap l_{j+1}=\{{a}_{j+1}\} for any 1 ≤ j ≤ n − 1 1\leq j\leq n-1, we say that L = ∪ j = 1 n − 1 l j L=\cup_{j=1}^{n-1}{l_{j}} is an arc linear by parts. The points a 1 {a}_{1} and a n {a}_{n} are said to be the endpoints of L L.

We next present a family of subsets of 𝕊 2 {\mathbb{S}^{2}} which are topologically equivalent to semialgebraic sets.

Given any positive integer n ∈ ℕ n\in\mathbb{N}, we say that a topological space is an n n -star if it is homeomorphic to S n = { z ∈ ℂ: z n ∈ [0, 1] } S_{n}=\{z\in\mathbb{C}:z^{n}\in[0,1]\}. If Z Z is an n n -star and h: S n → X h:S_{n}\to X is a homeomorphism, then the image of the origin under h h is called a vertex of the star while the components of Z ∖ { h ⁡ ( 0) } Z\setminus\{h(0)\} are called the branches of the star. Note that the vertex and the branches of a star are uniquely defined except in the cases n = 1, 2 n=1,2, when Z Z is just a closed arc and the vertexes are its endpoints (for n = 1 n=1) or its interior points (for n = 2 n=2). We shall also adopt the convention of calling any singleton a 0 0 -star (the point being its vertex). When Y Y is a topological space and a {a} is a point in Y Y which posses a neighbourhood Z ⊂ Y Z\subset Y being an *n n -star*with a {a} as vertex, we will say that a {a} is a star point in Y Y (of order n n); if all the points in Y Y are star points, we will say that Y Y is a generalized graph.

An important family of examples of generalized graphs is given by the set of zeros of planar analytic maps.

###### Proposition 2.2.

Let f: U → ℝ f:U\to\mathbb{R} be an analytic map in an open subset U ⊂ ℝ 2 U\subset\mathbb{R}^{2} and Z = { z ∈ U: f ⁡ ( z) = 0 } Z=\{z\in U:f(z)=0\} be the set of zeros of f f. Then either Z Z is a whole connected component of U U or Z Z is a generalized graph.

###### Proof.

The result follows as a consequence of the Weierstrass Preparation Theorem and the theory of Puiseux Series (for a detailed record of the proof, see, for example, [9, p. 687]). ∎

We focus on a special subfamily of generalized graphs which shall play an important part in the proof of Theorem 1.3.

###### Lemma 2.3.

Let L ⊂ 𝕊 2 {L}\subset\mathbb{S}^{2} be a connected generalized graph. Then L {L} is topologically equivalent to a semialgebraic set; that is, there exists a homeomorphism of 𝕊 2 \mathbb{S}^{2} onto itself taking L L to a semialgebraic set.

###### Proof.

Let us start by noticing that, apart from composing a rotation with the transition homeomorphism ϕ: ℝ ∞ 2 → ℝ ∞ 2 \phi:\mathbb{R}^{2}_{\infty}\to\mathbb{R}^{2}_{\infty} associated to the Bendixson compactification (see Section 2.1), we may suppose that there exists a compact and connected set Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} such that its completion in ℝ ∞ 2 \mathbb{R}^{2}_{\infty} is equal to L {L}. Also, if we call T ⊂ Γ T\subset\Gamma the subset of points which are not star points of order 2 2, then T T is a finite set. It is then enough to prove the result under the hypothesis of Γ \Gamma being non-empty.

If T T is empty, there is nothing to say: L {L} is homeomorphic to { ( x 1, x 2) ∈ ℝ 2: x 1 2 + x 2 2 = 0 } \{(x_{1},x_{2})\in\mathbb{R}^{2}:x_{1}^{2}+x_{2}^{2}=0\} [11, Theorem 2, p. 180]. Otherwise, let us say that T = { a 1, …, a m } T=\{{a}_{1},\ldots,{a}_{m}\} for some m ≥ 1 m\geq 1. For every 1 ≤ j ≤ m 1\leq j\leq m we can take a neighbourhood B j ⊂ ℝ 2 B_{j}\subset\mathbb{R}^{2} of a j {a}_{j} such that B j ∩ T = { a j } B_{j}\cap T=\{{a}_{j}\} and B j ∩ Γ B_{j}\cap\Gamma is an n j n_{j} -star. Without lost of generality we can also assume that, for every 1 ≤ j ≤ m 1\leq j\leq m, B j B_{j} is a standard euclidean compact ball of center a j {a}_{j} in ℝ 2 \mathbb{R}^{2}, that ∂ B j \partial B_{j} meets Γ \Gamma in exactly n j n_{j} points b j, 1, …, b j, n j {b}_{j,1},\ldots,{b}_{j,n_{j}} and, as a consequence, B j ∩ Γ B_{j}\cap\Gamma is homeomorphic to M j = ∪ k = 1 n j [a j, b j, k] M_{j}=\cup_{k=1}^{n_{j}}[{a}_{j},{b}_{j,k}]. Now any of the components of Γ ∖ ∪ j = 1 m B j \Gamma\setminus\cup_{j=1}^{m}B_{j} is a generalized graph consisting only of star points of order 2 2, let us say U 1, …, U τ U_{1},\ldots,U_{\tau} are those components. For any 1 ≤ k ≤ τ 1\leq k\leq\tau, we can take an arc linear by parts N k N_{k} whose endpoints coincide with the points in Cl ( U k) ∖ U k \mathop{\rm Cl}\nolimits(U_{k})\setminus U_{k} and such that ∪ j = 1 m M j ∪ ∪ k = 1 τ N k \cup_{j=1}^{m}M_{j}\,\cup\,\cup_{k=1}^{\tau}N_{k} is homeomorphic to Γ \Gamma. This last homeomorphism can be extended to a homeomorphism from the sphere to the sphere (see, for example, [1, Theorem 1]). ∎

### 2.3. Topological properties of periodic limit sets

Let { X λ } λ ∈ Λ \left\{X_{\lambda}\right\}_{\lambda\in\Lambda} be a polynomial family of planar vector fields and, for every λ ∈ Λ \lambda\in\Lambda, let X ^ λ \hat{X}_{\lambda} be the analytic vector field on 𝕊 2 {\mathbb{S}^{2}} described by the Bendixson compactification as in Section 2.1 (we remark that p N = ( 0, 0, 1) p_{N}=(0,0,1) is a singular point for every X ^ λ \hat{X}_{\lambda}). Together with the family { X ^ λ } λ ∈ Λ \{\hat{X}_{\lambda}\}_{\lambda\in\Lambda} we may consider the associated analytic flow Φ: ℝ × 𝕊 2 × Λ → 𝕊 2 \Phi:\mathbb{R}\times{\mathbb{S}^{2}}\times\Lambda\to{\mathbb{S}^{2}}.

The continuity of the flow already gives some topological and dynamical obstructions for the limit periodic sets: a limit periodic set at a parameter λ 0 \lambda_{0} must be invariant for X λ 0 X_{\lambda_{0}} and its compactification by one point must be connected.

###### Lemma 2.4.

If Γ \Gamma is a limit periodic set at the parameter λ 0 \lambda_{0}, then Γ ^ \hat{\Gamma} is connected and invariant for X ^ λ 0 \hat{X}_{\lambda_{0}} (equivalently, Γ \Gamma is invariant for X λ 0 X_{\lambda_{0}}).

###### Proof.

Let us start fixing a sequence in Λ \Lambda converging to λ 0 \lambda_{0}, ( λ n) n (\lambda_{n})_{n}, and a sequence of topological circles in ℝ 2 \mathbb{R}^{2}, ( γ n) n (\gamma_{n})_{n}, such that ( γ ^ n) n (\hat{\gamma}_{n})_{n} converges to Γ ^ \hat{\Gamma} in the Hausdorff topology of 𝕊 2 \mathbb{S}^{2} and, for every n n, γ n \gamma_{n} is a limit cycle of X λ n X_{\lambda_{n}}.

Firstly, we consider points a ∈ Γ {a}\in\Gamma and b = Φ ⁡ ( s, a, λ 0) {b}={\Phi}(s,{a},\lambda_{0}) for some s ∈ ℝ s\in\mathbb{R} and a sequence of points a n ∈ γ n {a}_{n}\in\gamma_{n} converging to a {a}. By the continuity of X λ X_{\lambda}, the points Φ ⁡ ( s, a n, λ n) {\Phi}(s,{a}_{n},\lambda_{n}) converge to b {b} so b ∈ Γ ^ {b}\in{\hat{\Gamma}}.

Next, to obtain a contradiction, let us suppose that Γ ^ \hat{\Gamma} is not connected and choose two disjoint open sets V 1 V_{1} and V 2 V_{2} of 𝕊 2 {\mathbb{S}^{2}} which disconnect Γ ^ \hat{\Gamma}. Since γ n → Γ ^ \gamma_{n}\to\hat{\Gamma} in the Hausdorff topology, we conclude that γ n ⊂ V 1 ∪ V 2 \gamma_{n}\subset V_{1}\cup V_{2}, γ n ∩ V 1 ≠ ∅ \gamma_{n}\cap V_{1}\neq\emptyset and γ n ∩ V 2 ≠ ∅ \gamma_{n}\cap V_{2}\neq\emptyset, for n n sufficiently big. But this implies that γ n \gamma_{n} is disconnected, which is impossible. ∎

From the analyticity of the flow Φ \Phi (we only need to use that it is of class C 1 C^{1}), the following important local property is established: any limit periodic set can meet at most once with any traversal. We formalize this property below.

Let I ⊂ ℝ I\subset\mathbb{R} be an open interval and λ ∈ Λ \lambda\in\Lambda. An embedding σ: I → 𝕊 2 \sigma:I\to{\mathbb{S}^{2}} of class C 1 C^{1} is called a transverse section of X ^ λ \hat{X}_{\lambda} if, for any s ∈ I s\in I, the vectors σ ˙ ​ ( s) \dot{\sigma}(s) and X ^ λ ​ ( σ ​ ( s)) \hat{X}_{\lambda}(\sigma(s)) are linearly independent. We shall also refer to σ ⁡ ( I) \sigma(I) as a transverse section of X ^ λ \hat{X}_{\lambda}.

If a ∈ 𝕊 2 {a}\in{\mathbb{S}^{2}} is a regular point of X ^ λ 0 \hat{X}_{\lambda_{0}}, then we can always find a positive real number ε > 0 \varepsilon>0 and an analytic embedding σ: ( − ε, ε) → 𝕊 2 \sigma:(-\varepsilon,\varepsilon)\to{\mathbb{S}^{2}} being a transverse section of X ^ λ 0 \hat{X}_{\lambda_{0}} with σ ⁡ ( 0) = a \sigma(0)={a}. On the other hand, given any transverse section of X ^ λ 0 \hat{X}_{\lambda_{0}}, σ: I → 𝕊 2 \sigma:I\to{\mathbb{S}^{2}}, it is clear that for any t ∈ I t\in I we can take I ⁡ ( t) I(t), an open neighbourhood of t t in I I, and Λ ⁡ ( λ 0) \Lambda(\lambda_{0}), a neighbourhood of λ 0 \lambda_{0} in Λ \Lambda, such that the restriction of σ \sigma to I ⁡ ( t) I(t) is a transverse section of X ^ λ \hat{X}_{\lambda} for every λ ∈ Λ ⁡ ( λ 0) \lambda\in\Lambda(\lambda_{0}). These observations, together with the Flow Box Theorem and the fact that any periodic orbit of a C 1 C^{1} vector fields on the sphere can meet any transverse section only once, give the following result.

###### Lemma 2.5.

(see [15, Lemma 2, p. 20]) Let Γ \Gamma be a limit periodic set at the parameter λ 0 \lambda_{0}. Then any transverse section of X ^ λ 0 \hat{X}_{\lambda_{0}} meets Γ ^ \hat{\Gamma} at most once.

The last ingredient we need is the well-known behaviour of analytic vector fields on the neighbourhood of isolated singular points, the so-called finite sectorial decomposition property (see [5, pp. 17–19]): every sufficiently small neighbourhood of an isolated singular point of a planar analytic vector field is either a center, a focus or a finite union of hyperbolic, parabolic and elliptic sectors.

We are now ready to prove the direct implication of Theorem 1.3. The work is done by the combination of Lemma 2.3 and the following result.

###### Lemma 2.6.

Suppose that Γ \Gamma is a limit periodic set at the parameter λ 0 \lambda_{0} and that X λ 0 ≢ 0 X_{\lambda_{0}}\not\equiv 0. Then Γ ^ \hat{\Gamma} is a connected generalized graph.

###### Proof.

According with Lemma 2.4, Γ ^ \hat{\Gamma} is a connected subset of 𝕊 2 \mathbb{S}^{2} which is a union of orbits of X ^ λ 0 \hat{X}_{\lambda_{0}}. Therefore, we only need to prove that all the points of Γ ^ \hat{\Gamma} are star points. We fix a point a ∈ Γ ^ a\in\hat{\Gamma} and we distinguish three cases.

If a a is a regular point of X ^ λ 0 \hat{X}_{\lambda_{0}}, the Flow Box Theorem and Lemma 2.5 imply the existence of a neighbourhood of a a, U a U_{a}, such that Γ ^ ∩ U a \hat{\Gamma}\cap U_{a} is a 2 2 -star.

Let us now assume that a a is an isolated singular point of X ^ λ 0 \hat{X}_{\lambda_{0}} and let U a U_{a} be a neighbourhood of a a such that every point in U a ∖ { a } U_{a}\setminus\{a\} is a regular point of X ^ λ 0 \hat{X}_{\lambda_{0}}. If a a is a center (respectively a node or a focus) for X ^ λ 0 \hat{X}_{\lambda_{0}}, we can always find a transverse section accumulating at a a and meeting at least once (respectively twice) any regular orbits of X ^ λ 0 \hat{X}_{\lambda_{0}} in U a U_{a} so Lemma 2.5 guarantees that, after shrinking U a U_{a} if necessary, Γ ^ ∩ U a = { a } \hat{\Gamma}\cap U_{a}=\{a\}. Otherwise, we can consider characteristics orbits c 0, …, c n − 1 c_{0},\ldots,c_{n-1}, with n ≥ 2 n\geq 2, defining a sectorial decomposition around a a (we follow the notation of [5, pp. 17–19]). Using once again Lemma 2.5, we note that: at each parabolic sector there may exist only one regular orbit contained in Γ ^ \hat{\Gamma}; at each hyperbolic sector, apart from shrinking U a U_{a}, the intersection with Γ ^ \hat{\Gamma} can only be the characteristic orbits c j c_{j} defining this sector; at each elliptic sector, apart from shrinking U a U_{a} and adding two new parabolic sectors, we may suppose that the intersection of the elliptic sector with Γ ^ \hat{\Gamma} is empty. It follows from these observations that, also in this case, Γ ^ ∩ U a \hat{\Gamma}\cap U_{a} is a star of vertex a a.

Finally, if a a is a non-isolated singularity of X ^ λ 0 \hat{X}_{\lambda_{0}}, it is well known that there exist a neighbourhood of a a, U a U_{a}, an analytic map f: U a → ℝ f:U_{a}\to\mathbb{R} and an analytic vector field Y Y on U a U_{a} such that the restriction of X ^ λ 0 \hat{X}_{\lambda_{0}} to U a U_{a} coincides with the product f ​ Y f\,Y and the vector field Y Y has no zeros in U a ∖ { a } U_{a}\setminus\{a\} (e. g. see [9, Theorem 4.5]).

Let us denote by Z Z the analytic set f − 1 ​ ( 0) f^{-1}(0) and note that, after shrinking U a U_{a} if necessary, Z Z is a star (with a a as vertex) decomposing U a U_{a} into finitely many connected components any of which contains no singular points for X ^ λ 0 \hat{X}_{\lambda_{0}}. Furthermore, by analyticity, there is no loss of generality in assuming that the neighbourhood U a U_{a} has been chosen such that each branch of Z Z is either invariant by Y Y or a transverse section of Y Y (see for example [10, Lemma 3.2]). Accordingly, Γ ^ ∩ U a \hat{\Gamma}\cap U_{a} is the union of { a } \{a\} with some of the branches of Z Z and some regular orbits of Y Y.

The above observation allow us to adapt the argument given in the first two cases, mutatis mutandis, to the case when a a is a regular point of Y Y, or when Y Y admits a sectorial decomposition at a a (where we are again considering at least two characteristic orbits and among them appear at least all the branches of Z ∖ { a } Z\setminus\{a\} which are invariant by Y Y). We remark that the latter case includes the scenario of a a being a node point for Y Y.

Finally, if a a is a center or a focus point of Y Y, it is elementary to show that in any of the connected components of U a ∖ Z U_{a}\setminus Z there exists a transverse section accumulating at a a and at the frontier of U a U_{a}. Consequently, in these two cases, it may be conclude that, after shrinking U a U_{a} if necessary, Γ ^ ∩ U a ⊂ Z \hat{\Gamma}\cap U_{a}\subset Z and a a is a star point. ∎

###### Proof of direct implication of Theorem 1.3.

If X λ 0 ≢ 0 X_{\lambda_{0}}\not\equiv 0, the result easily follows from Lemmas 2.3 and 2.6. So, assume that X λ 0 ≡ 0 X_{\lambda_{0}}\equiv 0.

The following argument is due to Roussarie [16, Section 3] and follows an original idea of Bautin. Let Γ \Gamma be the limit periodic set and

 | X λ ( x) = ∑ α ∈ ℕ 2 f 1, α ( λ) x α ∂ x 1 + f 2, α ( λ) x α ∂ x 2 X_{\lambda}(x)=\sum_{\alpha\in\mathbb{N}^{2}}f_{1,\alpha}(\lambda)\,x^{\alpha}\,\partial_{x_{1}}+f_{2,\alpha}(\lambda)\,x^{\alpha}\,\partial_{x_{2}} |  |

We consider the ideal sheaf 𝒥 \mathcal{J} generated by ( f 1, α ​ ( λ), f 2, α ​ ( λ)) α ∈ ℕ 2 (f_{1,\alpha}(\lambda),f_{2,\alpha}(\lambda))_{\alpha\in\mathbb{N}^{2}}. Note that λ 0 \lambda_{0} is in the support of this ideal by hypothesis.

Let ( λ n) (\lambda_{n}) be the sequence of parameters converging to λ 0 \lambda_{0} and note that λ n \lambda_{n} is not contained in the support of 𝒥 \mathcal{J} (because all fibres which belongs to the support of 𝒥 \mathcal{J} are zero). Consider the monomialization σ: Λ ~ → Λ \sigma:\widetilde{\Lambda}\to\Lambda of the ideal sheaf 𝒥 \mathcal{J} (see, e.g. [4]) and denote by ( λ ~ n) (\widetilde{\lambda}_{n}) the pre-image of ( λ n) (\lambda_{n}) (which is well-defined because ( λ n) (\lambda_{n}) is not in the support of 𝒥 \mathcal{J}). Since σ \sigma is a proper map, there exists a subsequence ( λ ~ n k) (\widetilde{\lambda}_{n_{k}}) which converges to a parameter λ ~ 0 ∈ σ − 1 ​ ( λ 0) \widetilde{\lambda}_{0}\in\sigma^{-1}(\lambda_{0}). By construction, moreover, in a neighbourhood U U of λ ~ 0 \widetilde{\lambda}_{0} there exists a multi-index β ∈ ℕ n \beta\in\mathbb{N}^{n} such that σ ∗ ​ ( X λ) | ℝ 2 × U = λ ~ β ​ X ~ λ ~ \sigma^{\ast}(X_{\lambda})|_{\mathbb{R}^{2}\times U}=\widetilde{\lambda}^{\beta}\widetilde{X}_{\widetilde{\lambda}}, where X ~ λ ~ 0 ≢ 0 \widetilde{X}_{\widetilde{\lambda}_{0}}\not\equiv 0. We note that Γ \Gamma is the limit periodic set of σ ∗ ​ ( X λ) \sigma^{\ast}(X_{\lambda}) for the parameter λ ~ 0 \widetilde{\lambda}_{0}, and that the division of the locally defined family by the monomial λ ~ β \widetilde{\lambda}^{\beta} won’t change the topology of Γ \Gamma. The result follows from the first part of the proof.

∎

## 3. Construction of limit periodic sets

### 3.1. Properties of semialgebraic sets

We are interested in planar semialgebraic sets Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} of dimension 0 0 or 1 1. Associated to any of these sets, we introduce a free-square polynomial whose set of zeros shall play an important role in the rest of the paper.

Let us start fixing a coordinate system for the plane x = ( x 1, x 2) x=(x_{1},x_{2}) and let Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} be a semialgebraic set of dimension 0 0 or 1 1 and whose compactification Γ ^ \hat{\Gamma} is connected. If Γ \Gamma is itself an algebraic set we simply take a free-squared polynomial f Γ f_{\Gamma} making ( f Γ ​ ( x) = 0) = Γ (f_{\Gamma}(x)=0)=\Gamma. Assume now that Γ \Gamma is not an algebraic set; in particular, and because Γ ^ \hat{\Gamma} is connected, we note that none of the components of Γ \Gamma can be singletons. Let f i f_{i} and g i, j g_{i,j}, 1 ≤ i ≤ p 1\leq i\leq p and 1 ≤ j ≤ q 1\leq j\leq q, be polynomials such that

(3.1) |  | Γ = ⋃ i = 1 p ⋂ j = 1 q { x ∈ ℝ 2: f i ​ ( x) = 0 ​ and ​ g i ​ j ​ ( x) > 0 }. \Gamma=\bigcup_{i=1}^{p}\bigcap_{j=1}^{q}\{x\in\mathbb{R}^{2}:\,f_{i}(x)=0\text{ and }g_{ij}(x)>0\}. |  |

Without lost of generality, we can assume that all the f i f_{i} are irreducible and also, because Γ \Gamma has empty interior, that all of them are non-constant and ( f i ​ ( x) = 0) ∩ Γ (f_{i}(x)=0)\cap\Gamma is one dimensional. Using the well-known fact that any two co-prime polynomials on ℝ 2 \mathbb{R}^{2} can meet only finitely many times, it is not difficult to reason that under such conditions the polynomials f i f_{i} in ( 3.1) are uniquely defined (up to the multiplication of non-zero constants). Let us take f Γ f_{\Gamma} as the free-square polynomial associated to the product ∏ i = 1 p f i \prod_{i=1}^{p}f_{i}; this polynomial verifies Γ ⊂ ( f Γ ​ ( x) = 0) \Gamma\subset(f_{\Gamma}(x)=0) and is uniquely defined from ( 3.1) in the terms just expressed. In any of the two cases discussed above, we shall refer to the polynomial f Γ f_{\Gamma} as the polynomial associated to Γ \Gamma. The set of zeros of f Γ f_{\Gamma}, which we shall denote by A Γ = ( f Γ ​ ( x) = 0) A_{\Gamma}=(f_{\Gamma}(x)=0), will be also said to be the algebraic set associated to Γ \Gamma.

###### Definition 3.1.

Let Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} be a semialgebraic set of dimension 0 0 or 1 1 and such that Γ ^ \hat{\Gamma} is connected and let f Γ f_{\Gamma} and A Γ A_{\Gamma} be its associated polynomial and algebraic set respectively. A point a ∈ Γ a\in\Gamma is said to be:

(1) an *algebraic*point of Γ \Gamma if there exists a neighbourhood of a a in ℝ 2 \mathbb{R}^{2}, U U, such that U ∩ Γ = U ∩ A Γ U\cap\Gamma=U\cap A_{\Gamma}. We denote the set of algebraic points of Γ \Gamma by A ​ l ​ g ​ ( Γ) Alg(\Gamma);

(2) a generic non-algebraic point of Γ \Gamma if a ∉ A ​ l ​ g ​ ( Γ) a\notin Alg(\Gamma) and A Γ A_{\Gamma} is regular at a a (i. e. the gradient of f Γ f_{\Gamma} at a a is non-zero). We denote the set of generic non-algebraic points of Γ \Gamma by G ​ e ​ n ​ ( Γ) Gen(\Gamma);

(3) a non-generic non-algebraic point of Γ \Gamma if a ∉ A ​ l ​ g ​ ( Γ) a\notin Alg(\Gamma) and A Γ A_{\Gamma} is singular at a a (i. e. the gradient of f Γ f_{\Gamma} vanishes at a a). We denote the set of non-generic non-algebraic point of Γ \Gamma by N ​ G ​ ( Γ) NG(\Gamma).

###### Remark 3.2.

The sets of non-algebraic points G ​ e ​ n ​ ( Γ) Gen(\Gamma) and N ​ G ​ ( Γ) NG(\Gamma) are both finite.

###### Remark 3.3.

Let us assume that N ​ G ​ ( Γ) NG(\Gamma) is non-empty, say N ​ G ​ ( Γ) = { a 1, …, a r } NG(\Gamma)=\{a_{1},\ldots,a_{r}\} for some positive integer r r. For every k ∈ { 1, …, r } k\in\{1,\ldots,r\}, take a sufficiently small euclidean ball B k = B ⁡ ( a k, ρ k) B_{k}=B(a_{k},\rho_{k}) centered at a k a_{k} with radius ρ k > 0 \rho_{k}>0 and denote by n k n_{k} the number of connected components of ( A Γ ∖ Γ) ∩ B k \left(A_{\Gamma}\setminus\Gamma\right)\cap B_{k} (the number n k n_{k} is the same for every sufficiently small ρ k > 0 \rho_{k}>0). By Newton-Puisseux Theorem, for every k ∈ { 1, …, r } k\in\{1,\ldots,r\}, there exist sequences of points ( a i j, k) i ∈ ℕ ⊂ A Γ ∖ Γ (a_{i}^{j,k})_{i\in\mathbb{N}}\subset A_{\Gamma}\setminus\Gamma, j ∈ { 1, …, n k } j\in\{1,\ldots,n_{k}\}, such that each sequence is contained in a different connected component of ( A Γ ∖ Γ) ∩ B k \left(A_{\Gamma}\setminus\Gamma\right)\cap B_{k} and a i j, k → a j a_{i}^{j,k}\to a_{j} when i → ∞ i\to\infty.

The following objects are used in Section 3.3: the number n Γ = ∑ k = 1 r n k n_{\Gamma}=\sum_{k=1}^{r}n_{k}; the sequence of points in ℝ 2 ​ n Γ \mathbb{R}^{2n_{\Gamma}}, ( α i) i ∈ ℕ (\alpha_{i})_{i\in\mathbb{N}}, given by α i = ( a i 1, 1, …, a i n 1, 1, …, a i 1, r, …, a i n r, r) \alpha_{i}=(a_{i}^{1,1},\ldots,a_{i}^{n_{1},1},\allowbreak\ldots\allowbreak{,}a_{i}^{1,r},\ldots,a_{i}^{n_{r},r}); and the limit of ( α i) i (\alpha_{i})_{i}, α 0 ∈ ℝ 2 ​ n Γ \alpha_{0}\in\mathbb{R}^{2n_{\Gamma}}.

###### Remark 3.4.

It follows from Remark 3.3 that there exists a sequence of semialgebraic sets of dimension 0 0 or 1 1 ( Γ i) i ∈ ℕ (\Gamma_{i})_{i\in\mathbb{N}} such that Γ ⊂ Γ i ⊂ A Γ \Gamma\subset\Gamma_{i}\subset A_{\Gamma}, N ​ G ​ ( Γ i) = ∅ NG(\Gamma_{i})=\emptyset and Γ i → Γ \Gamma_{i}\to\Gamma (in the Hausdorff topology) when i → ∞ i\to\infty. Moreover, the polynomials f Γ f_{\Gamma} and the algebraic set A Γ A_{\Gamma} are also the polynomial and the algebraic set associated to any of those Γ i \Gamma_{i} and G ​ e ​ n ​ ( Γ i) = G ​ e ​ n ​ ( Γ) ∪ { a i 1, 1, …, a i n 1, 1, …, a i 1, r, …, a i n r, r } Gen(\Gamma_{i})=Gen(\Gamma)\cup\{a_{i}^{1,1},\ldots,a_{i}^{n_{1},1},\allowbreak\ldots\allowbreak{,}a_{i}^{1,r},\ldots,a_{i}^{n_{r},r}\}.

Now assume that Γ \Gamma is compact and connected. There exists a finite number of (non-unique) points b 1, …, b k ∈ A ​ l ​ g ​ ( Γ) b_{1},\ldots,b_{k}\in Alg(\Gamma) which are regular points of the algebraic set A Γ A_{\Gamma} and such that both Γ ∖ { b 1, …, b k } \Gamma\setminus\{b_{1},\ldots,b_{k}\} and ℝ 2 ∖ ( Γ ∖ { b 1, …, b k }) \mathbb{R}^{2}\setminus(\Gamma\setminus\{b_{1},\ldots,b_{k}\}) are connected. We can always fix a certain number of these points, which we call transition points, and denote their set by T ​ r ​ ( Γ) Tr(\Gamma). We remark that the minimal number k k of transition points corresponds to the number of connected components of ℝ 2 ∖ Γ \mathbb{R}^{2}\setminus\Gamma minus one. Moreover, with the notation of Remark 3.4, the set T ​ r ​ ( Γ) Tr(\Gamma) is a valid set of transition points for Γ i \Gamma_{i}, for all i i sufficiently big.

### 3.2. Construction of generic compact limit periodic sets

Let us fix a connected and compact semialgebraic set Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} of dimension 0 0 or 1 1 and such that N ​ G ​ ( Γ) = ∅ NG(\Gamma)=\emptyset. Let f = f Γ f=f_{\Gamma} be the polynomial associated to Γ \Gamma and A Γ A_{\Gamma} its set of zeros and fix a transition set for Γ \Gamma, T ​ r ​ ( Γ) Tr(\Gamma). Fix a coordinate system x = ( x 1, x 2) x=(x_{1},x_{2}) of ℝ 2 \mathbb{R}^{2} and a parameter λ ∈ ℝ \lambda\in\mathbb{R}. Denote by S S the set G ​ e ​ n ​ ( Γ) ∪ T ​ r ​ ( Γ) Gen(\Gamma)\cup Tr(\Gamma), which is a finite set.

We consider the function

 | h ⁡ ( x, λ) \displaystyle h(x,\lambda) | = f ​ ( x) 2 − λ ​ ∏ p ∈ S ( ‖ x − p ‖ 2 − λ 2), \displaystyle=f(x)^{2}-\lambda\prod_{p\in S}\left(\|x-p\|^{2}-\lambda^{2}\right), |  |

where ∥ ⋅ ∥ \|\cdot\| stands for the euclidean norm on ℝ 2 \mathbb{R}^{2}, and the polynomial family of planar vector fields ( X λ) λ ∈ ℝ (X_{\lambda})_{\lambda\in\mathbb{R}} where

(3.2) |  | X λ = ( ∂ h ∂ x 2 + h ∂ h ∂ x 1) ∂ x 1 + ( − ∂ h ∂ x 1 + h ∂ h ∂ x 2) ∂ x 2. X_{\lambda}=\left(\frac{\partial h}{\partial x_{2}}+h\frac{\partial h}{\partial x_{1}}\right)\partial_{x_{1}}+\left(-\frac{\partial h}{\partial x_{1}}+h\frac{\partial h}{\partial x_{2}}\right)\partial_{x_{2}}. |  |

We devote the rest of the Section to show Γ \Gamma is a limit periodic set of ( X λ) λ ∈ ℝ (X_{\lambda})_{\lambda\in\mathbb{R}} at λ = 0 \lambda=0. The key to achieve it is to understand how the level curves (in respect to the parameter λ \lambda) of h h are. We shall start giving a local description of ( h ⁡ ( x, λ) = 0) (h(x,\lambda)=0) in a neighbourhood of a point ( a, 0) (a,0) where a ∈ Γ a\in\Gamma; we treat separately the cases a ∈ A ​ l ​ g ​ ( Γ) ∖ T ​ r ​ ( Γ) a\in Alg(\Gamma)\setminus Tr(\Gamma) (Lemma 3.5) and a ∈ G ​ e ​ n ​ ( Γ) ∪ T ​ r ​ ( Γ) a\in Gen(\Gamma)\cup Tr(\Gamma) (Lemma 3.6).

Here and subsequently, given any set A ⊂ ℝ 2 × ℝ A\subset\mathbb{R}^{2}\times\mathbb{R} and any t ∈ ℝ t\in\mathbb{R} we will denote A ∩ ( λ = t) = { ( x, λ) ∈ A: λ = t } A\cap(\lambda=t)=\{(x,\lambda)\in A:\lambda=t\}; when convenient, we will also understand that A ∩ ( λ = t) A\cap(\lambda=t) is identified with { x ∈ ℝ 2: ( x, t) ∈ A } \{x\in\mathbb{R}^{2}:(x,t)\in A\}. In particular, Z t Z_{t} which stands for the level curve ( h ⁡ ( x, λ) = 0) ∩ ( λ = t) (h(x,\lambda)=0)\cap(\lambda=t) will repeatedly be seen as a subset of ℝ 2 \mathbb{R}^{2}.

###### Lemma 3.5.

For every a ∈ A ​ l ​ g ​ ( Γ) ∖ T ​ r ​ ( Γ) a\in Alg(\Gamma)\setminus Tr(\Gamma) there exist a number ϵ a > 0 \epsilon_{a}>0 and a compact neighbourhood V a V_{a} of a a such that Z t ∩ V a ⊂ ℝ 2 ∖ Γ Z_{t}\cap V_{a}\subset\mathbb{R}^{2}\setminus\Gamma for every 0 < t < ϵ a 0<t<\epsilon_{a}. Moreover, for any connected component W W of V a ∖ Γ V_{a}\setminus\Gamma and any 0 < t < ϵ a 0<t<\epsilon_{a}, Z t ∩ W Z_{t}\cap W is a non-empty connected regular curve which converges (in the Hausdorff topology) to Cl ( W) ∩ Γ \mathop{\rm Cl}\nolimits(W)\cap\Gamma, when t t tends to 0 0 (see Figure 2).

###### Proof.

Let us start considering a number ϵ a > 0 \epsilon_{a}>0, a compact neighbourhood V a ⊂ ℝ 2 V_{a}\subset\mathbb{R}^{2} of a a and the coordinate system z = x − a z=x-a (which is centered at a a) such that h ⁡ ( z, λ) = f ​ ( z) 2 − λ ​ u ​ ( z, λ) h(z,\lambda)=f(z)^{2}-\lambda u(z,\lambda), where u ⁡ ( z, λ) > 0 u(z,\lambda)>0 at all points in V a × ( ϵ a, − ϵ a) V_{a}\times(\epsilon_{a},-\epsilon_{a}).

By the implicit function theorem, we may assume that there exists an analytic function λ: V a → ℝ \lambda:V_{a}\to\mathbb{R} such that h ⁡ ( z, λ ⁡ ( z)) = 0 h(z,\lambda(z))=0 for every z ∈ V a z\in V_{a}.

We note that the curves Z t a = Z t ∩ V a Z_{t}^{a}=Z_{t}\cap V_{a} correspond to the t t -level curves of λ ⁡ ( z) \lambda(z), that is, Z t a = ( λ ⁡ ( z) = t) Z_{t}^{a}=(\lambda(z)=t). By continuity of λ ⁡ ( z) \lambda(z), shrinking V a V_{a} if necessary, this implies that Z t a Z_{t}^{a} converges (in the Hausdorff topology) to Γ ∩ V a = ( λ ⁡ ( z) = 0) \Gamma\cap V_{a}=(\lambda(z)=0). Furthermore, since the level curves of non-constant analytic functions (restricted to a compact set) are generically regular, we conclude that Z t a Z_{t}^{a} are regular for all t > 0 t>0 sufficiently small.

Next, since λ ⁡ ( z) ≥ 0 \lambda(z)\geq 0 for every z ∈ V a z\in V_{a}, we conclude that, for every component W W of V a ∖ Γ V_{a}\setminus\Gamma, Z t a ∩ W Z_{t}^{a}\cap W is non-empty for all small enough t > 0 t>0.

Finally, fix a component W W of V a ∖ Γ V_{a}\setminus\Gamma and suppose by contradiction that there exists a sequence ( t n) n (t_{n})_{n} converging to 0 0 and such that Z t n a ∩ W Z_{t_{n}}^{a}\cap W is not connected. Without loss of generality, we may suppose that Cl ( W) \mathop{\rm Cl}\nolimits(W) is a compact semialgebraic set. Denote by Γ W \Gamma_{W} the semialgebraic set Cl ( W) ∩ Γ \mathop{\rm Cl}\nolimits(W)\cap\Gamma. By the curve selection Lemma (see for example [12, Lemma 3.1]), there exists an analytic curve ϕ: [0, 1] → Cl ( W) \phi:[0,1]\to\mathop{\rm Cl}\nolimits(W) such that ϕ ⁡ ( 1) = a ∈ Γ W \phi(1)=a\in\Gamma_{W}, ϕ ⁡ ( t) ∈ Cl ( W) ∖ Γ W \phi(t)\in\mathop{\rm Cl}\nolimits(W)\setminus\Gamma_{W} for all t ≠ 0 t\neq 0 and Cl ( W) ∖ ϕ ⁡ ( [0, 1]) \mathop{\rm Cl}\nolimits(W)\setminus\phi([0,1]) is not connected. Since all connected components of Z t a Z_{t}^{a} must converge to Γ W \Gamma_{W}, we conclude that the curve ϕ ⁡ ( [0, 1]) \phi([0,1]) intersects each of the components of Z t a Z_{t}^{a}. This implies that the function λ ∘ ϕ \lambda\circ\phi is constant and equal to 0 0 (the value at ϕ ⁡ ( 1) \phi(1)), which is a contradiction.∎

a a Γ \Gamma Z t Z_{t} a a Γ \Gamma Z t Z_{t} Figure 2. A regular point (left) and a singular point (right).

###### Lemma 3.6.

For every a ∈ G ​ e ​ n ​ ( Γ) ∪ T ​ r ​ ( Γ) a\in Gen(\Gamma)\cup Tr(\Gamma), there exist a neighbourhood V a V_{a} of a a, a positive ϵ a > 0 \epsilon_{a}>0 and a coordinate system ( y, λ) (y,\lambda) defined on V a × ( − ϵ a, ϵ a) V_{a}\times(-\epsilon_{a},\epsilon_{a}) and centered at ( a, 0) (a,0) such that A Γ ∩ V a = ( y 1 = 0) A_{\Gamma}\cap V_{a}=(y_{1}=0) and

(3.3) |  | h ⁡ ( y, λ) = u ⁡ ( y, λ) ​ [y 1 2 − λ ⁡ ( y 2 2 − λ 2)] h(y,\lambda)=u(y,\lambda)\left[y_{1}^{2}-\lambda\left(y_{2}^{2}-\lambda^{2}\right)\right] |  |

where u ⁡ ( y, λ) u(y,\lambda) is a unit over V a × ( − ϵ a, ϵ a) V_{a}\times(-\epsilon_{a},\epsilon_{a}) (see Figure 3).

###### Proof.

Consider the coordinate system z = x − a z=x-a (which is centered at a a) and note that in a sufficiently small neighbourhood of ( a, 0) (a,0) of the form U a = V a × ( − ϵ a, ϵ a) U_{a}=V_{a}\times(-\epsilon_{a},\epsilon_{a}), we can write

 | h ⁡ ( z, λ) = f ​ ( z) 2 − λ ⁡ [z 1 2 + z 2 2 − λ 2] ​ u ​ ( z, λ) h(z,\lambda)=f(z)^{2}-\lambda\left[z_{1}^{2}+z_{2}^{2}-\lambda^{2}\right]u(z,\lambda) |  |

where u ⁡ ( z, λ) > 0 u(z,\lambda)>0 at all points in U a U_{a}. Apart from shrinking U a U_{a}, we can suppose that ∇ f ​ ( z) ≠ 0 \nabla f(z)\neq 0 at all points in U a U_{a}. Therefore (apart from a preliminary rotation) the change of coordinates y ~ 1 = u ​ ( z, λ) − 1 2 ​ f ​ ( z) = ξ ​ z 1 + ψ ⁡ ( z, λ) \widetilde{y}_{1}=u(z,\lambda)^{-\frac{1}{2}}f(z)=\xi z_{1}+\psi(z,\lambda) (where ξ ≠ 0 \xi\neq 0 and ψ ⁡ ( z, λ) \psi(z,\lambda) has order at least two) and y ~ 2 = z 2 \widetilde{y}_{2}=z_{2} is an isomorphism on U a U_{a}. We get

 | h ⁡ ( y ~, λ) = u ⁡ ( y ~, λ) ​ ( y ~ 1 2 − λ ⁡ ( y ~ 1 2 + y ~ 2 2 ​ v ​ ( y ~, λ) − λ 2)) h(\widetilde{y},\lambda)=u(\widetilde{y},\lambda)\left(\widetilde{y}_{1}^{2}-\lambda\left(\widetilde{y}_{1}^{2}+\widetilde{y}_{2}^{2}v\left(\widetilde{y},\lambda\right)-\lambda^{2}\right)\right) |  |

where v ⁡ ( y ~, λ) v(\widetilde{y},\lambda) is an analytic function such that v ⁡ ( 0, 0) > 0 v(0,0)>0. Finally, apart from shrinking U a U_{a}, the change of coordinates y 1 = y ~ 1 ​ 1 + λ y_{1}=\widetilde{y}_{1}\sqrt{1+\lambda} and y 2 = y ~ 2 ​ v ⁡ ( y ~, λ) y_{2}=\widetilde{y}_{2}\sqrt{v(\widetilde{y},\lambda)} is an isomorphism making

 | h ⁡ ( y, λ) = u ⁡ ( y, λ) ​ [y 1 2 − λ ⁡ ( y 2 2 − λ 2)] h(y,\lambda)=u(y,\lambda)\left[y_{1}^{2}-\lambda\left(y_{2}^{2}-\lambda^{2}\right)\right] |  |

and ( y 1 = 0) = ( y ~ 1 = 0) = ( f ⁡ ( z) = 0) ∩ V a (y_{1}=0)=(\widetilde{y}_{1}=0)=(f(z)=0)\cap V_{a} as we wanted to prove. ∎

a a Γ \Gamma Z t Z_{t} a a Γ \Gamma A Γ ∖ Γ A_{\Gamma}\setminus\Gamma Z t Z_{t} Figure 3. A transition point (left) and a generic point (right).

###### Proposition 3.7.

There exist an open neighbourhood U U of Γ × { 0 } \Gamma\times\{0\} and a number ϵ > 0 \epsilon>0 such that, for every 0 < t < ϵ 0<t<\epsilon, Z t ∩ U Z_{t}\cap U contains a compact and regular connected component γ t \gamma_{t} such that γ t → Γ \gamma_{t}\to\Gamma (in the Hausdorff topology) when t → 0 t\to 0.

###### Proof.

For every a ∈ Γ a\in\Gamma take a neighbourhood V a V_{a} of a a and a number ϵ a > 0 \epsilon_{a}>0 as in Lemma 3.5 or 3.6. The compacity of Γ \Gamma allows us to take a relatively compact open neighbourhood U U of Γ × { 0 } \Gamma\times\{0\}, of the form U = V × ( − δ, δ) U=V\times(-\delta,\delta) with V ⊂ ℝ 2 V\subset\mathbb{R}^{2} and δ > 0 \delta>0, such that U ⊂ ⋃ a ∈ Γ U a U\subset\bigcup_{a\in\Gamma}U_{a}.

Note that, from the two previous lemmas, we can assume that Z t ∩ U Z_{t}\cap U is regular for every sufficiently small t > 0 t>0. Also, the continuity of h h guarantees that Z t ∩ U Z_{t}\cap U converges to A Γ ∩ V A_{\Gamma}\cap V when t t tends to 0 0 (in the Hausdorff topology).

Let us fix a point b ∈ A ​ l ​ g ​ ( Γ) ∖ T ​ r ​ ( Γ) b\in Alg(\Gamma)\setminus Tr(\Gamma) and W W a component of V b ∖ Γ V_{b}\setminus\Gamma. For every sufficiently small t > 0 t>0, let us call γ t \gamma_{t} the connected component of Z t Z_{t} which meets W W (see Lemma 3.5). Let γ 0 ⊂ A Γ \gamma_{0}\subset A_{\Gamma} denote the limit of γ t \gamma_{t} when t → 0 t\to 0 (which contains b ∈ Γ b\in\Gamma). We are then left with the task of proving that γ 0 = Γ \gamma_{0}=\Gamma.

We start showing that γ 0 ⊂ Γ \gamma_{0}\subset\Gamma. We proceed by contradiction assuming the existence of a point c ∈ γ 0 ∖ Γ c\in\gamma_{0}\setminus\Gamma. After shrinking V V and V a V_{a} for a ∈ G ​ e ​ n ​ ( Γ) a\in Gen(\Gamma) if necessary, we may suppose that the points b b and c c lies in different connected components of the set R = V ∖ ⋃ a ∈ G ​ e ​ n ​ ( Γ) V a R=V\setminus\bigcup_{a\in Gen(\Gamma)}V_{a}. In particular, γ t ∩ R \gamma_{t}\cap R is disconnected and these disconnected components can only join each other by passing through one of the open sets U a U_{a} with a ∈ G ​ e ​ n ​ ( Γ) a\in Gen(\Gamma). This leads to contradiction with Lemma 3.6.

Since γ t \gamma_{t} is a connected regular curve, ℝ 2 ∖ γ t \mathbb{R}^{2}\setminus\gamma_{t} must consists in exactly two connected components, say C t 1 C^{1}_{t} and C t 2 C^{2}_{t}. Now, for every ϵ 0 > 0 \epsilon_{0}>0, consider the set γ ϵ 0 = γ 0 ∖ ∪ a ∈ T ​ r ​ ( Γ) B ( a, ϵ 0) \gamma_{\epsilon_{0}}=\gamma_{0}\setminus\cup_{a\in Tr(\Gamma)}B(a,\epsilon_{0}). We claim that, for every small enough t > 0 t>0,

(3.4) |  | γ ϵ 0 ⊂ ℝ 2 ∖ γ t. \gamma_{\epsilon_{0}}\subset\mathbb{R}^{2}\setminus\gamma_{t}. |  |

Indeed, let us suppose that γ ϵ 0 \gamma_{\epsilon_{0}} meets both C t 1 C^{1}_{t} and C t 2 C^{2}_{t} for all small t > 0 t>0. Since γ t \gamma_{t} can only cross points of Γ \Gamma near a ∈ T ​ r ​ ( Γ) ∪ G ​ e ​ n ​ ( Γ) a\in Tr(\Gamma)\cup Gen(\Gamma), we conclude that there exists a point a ∈ T ​ r ​ ( Γ) a\in Tr(\Gamma) such that γ t \gamma_{t} crosses Γ ∩ V a \Gamma\cap V_{a} in such a way that γ ϵ 0 ∩ C t 1 ∩ V a \gamma_{\epsilon_{0}}\cap C^{1}_{t}\cap V_{a} and γ ϵ 0 ∩ C t 2 ∩ V a \gamma_{\epsilon_{0}}\cap C^{2}_{t}\cap V_{a} Γ \Gamma are both non-empty. But this gives us again a contradiction with Lemma 3.6.

Finally, let us denote by W i W_{i}, i = 1, … ​ k i=1,\ldots k, the connected components of ℝ 2 ∖ Γ \mathbb{R}^{2}\setminus\Gamma and set I I as the subset of indexes i ∈ { 1, …, k } i\in\{1,\ldots,k\} such that W i ∩ γ t ≠ ∅ W_{i}\cap\gamma_{t}\neq\emptyset for all sufficiently small t > 0 t>0 (note that, by construction, I I is non-empty). The proof is completed by showing that I = { 1, …, k } I=\{1,\ldots,k\} and γ 0 = ∪ i ∈ I ( Cl ( W i) ∖ W i) \gamma_{0}=\cup_{i\in I}{\left(\mathop{\rm Cl}\nolimits(W_{i})\setminus W_{i}\right)}. We argue in two steps.

First, suppose by contradiction that γ 0 ≠ ∪ i ∈ I ( Cl ( W i) ∖ W i) \gamma_{0}\neq\cup_{i\in I}{\left(\mathop{\rm Cl}\nolimits(W_{i})\setminus W_{i}\right)}. Without restriction of generality, we can suppose that 1 ∈ I 1\in I and γ 0 ∩ ( Cl ( W 1) ∖ W 1) ≠ Cl ( W 1) ∖ W 1 \gamma_{0}\cap(\mathop{\rm Cl}\nolimits({W_{1}})\setminus W_{1})\neq\mathop{\rm Cl}\nolimits(W_{1})\setminus W_{1}. We consider a point c ∈ Cl ( W 1) ∖ W 1 c\in\mathop{\rm Cl}\nolimits(W_{1})\setminus W_{1} which does not belong to γ 0 \gamma_{0} and an analogous family of ovals α t ⊂ Z t \alpha_{t}\subset Z_{t} constructed in the same way as γ t \gamma_{t} but in respect to c c and the connected set W 1 W_{1}. By ( 3.4), we conclude that α 0 ∩ γ 0 \alpha_{0}\cap\gamma_{0} can only contain points which lie in T ​ r ​ ( Γ) Tr(\Gamma). This implies that Γ ∖ T ​ r ​ ( Γ) \Gamma\setminus Tr(\Gamma) has at least two disconnected components γ 0 ∖ T ​ r ​ ( Γ) \gamma_{0}\setminus Tr(\Gamma) and α 0 ∖ T ​ r ​ ( Γ) \alpha_{0}\setminus Tr(\Gamma), which is in contradiction with the definition of T ​ r ​ ( Γ) Tr(\Gamma).

Next, suppose, by contradiction, that γ 0 = ∪ i ∈ I ( Cl ( W i) ∖ W i) \gamma_{0}=\cup_{i\in I}{\left(\mathop{\rm Cl}\nolimits(W_{i})\setminus W_{i}\right)} but I ≠ { 1, …, k } I\neq\{1,\ldots,k\}. Denote by Γ 0 = ∪ i ∉ I ( Cl ( W i) ∖ W i) \Gamma_{0}=\cup_{i\notin I}{\left(\mathop{\rm Cl}\nolimits(W_{i})\setminus W_{i}\right)}. Since the level curve Z t Z_{t} can only cross points of Γ \Gamma near a ∈ T ​ r ​ ( Γ) ∪ G ​ e ​ n ​ ( Γ) a\in Tr(\Gamma)\cup Gen(\Gamma) (see Lemmas 3.5 and 3.6), we conclude that γ 0 ∩ Γ 0 ∩ T ​ r ​ ( Γ) = ∅ \gamma_{0}\cap\Gamma_{0}\cap Tr(\Gamma)=\emptyset. Therefore, γ 0 ∩ Γ 0 ⊂ Γ ∖ T ​ r ​ ( Γ) \gamma_{0}\cap\Gamma_{0}\subset\Gamma\setminus Tr(\Gamma) disconnects ℝ 2 \mathbb{R}^{2}, which is again in contradiction with the choice of T ​ r ​ ( Γ) Tr(\Gamma).

We conclude the proof by remarking that, since γ t \gamma_{t} converges to Γ \Gamma, for small enough t > 0 t>0, γ t \gamma_{t} must be a compact set contained in the interior of U U. ∎

After noticing that any compact and regular connected component of a planar algebraic set is a topological circle [11, Theorem 2, p. 180], it follows from Proposition 3.7 that the polynomial family of planar vector fields given by ( 3.2) has Γ \Gamma as a limit periodic set at λ = 0 \lambda=0. Indeed, it is enough to prove that, for every sufficiently small t > 0 t>0, the topological circle γ t ⊂ ℝ 2 \gamma_{t}\subset\mathbb{R}^{2} given by Proposition 3.7 is a limit cycle of X t X_{t}. To show this, it suffices to note that

 | X λ ​ ( h) = ( ∂ h ∂ x 2 + h ​ ∂ h ∂ x 1) ​ ∂ h ∂ x 1 + ( − ∂ h ∂ x 1 + h ​ ∂ h ∂ x 2) ​ ∂ h ∂ x 2 = h ​ ‖ ∇ h ‖ 2 {X_{\lambda}(h)=}\left(\frac{\partial h}{\partial x_{2}}+h\frac{\partial h}{\partial x_{1}}\right)\frac{\partial h}{\partial_{x_{1}}}+\left(-\frac{\partial h}{\partial x_{1}}+h\frac{\partial h}{\partial x_{2}}\right)\frac{\partial h}{\partial_{x_{2}}}=h\left\|\nabla h\right\|^{2} |  |

and, as a consequence, Z t Z_{t} is an invariant set containing any periodic orbit of X t X_{t}. Finally, the fact that γ t \gamma_{t} is regular guarantees that it is a periodic orbit. This proves the converse of Theorem 1.3 (under the extra assumption that Γ \Gamma is compact and generic).

### 3.3. Construction of non-generic compact limit periodic sets

Let us now fix a connected and compact semialgebraic set Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} of dimension 0 0 or 1 1 and N ​ G ​ ( Γ) ≠ ∅ NG(\Gamma)\neq\emptyset. Denote by f = f Γ f=f_{\Gamma} the polynomial associated to Γ \Gamma, A Γ A_{\Gamma} the associated algebraic set and S = G ​ e ​ n ​ ( Γ) ∪ T ​ r ​ ( Γ) S=Gen(\Gamma)\cup Tr(\Gamma). Fix a coordinate system x = ( x 1, x 2) x=(x_{1},x_{2}) of ℝ 2 \mathbb{R}^{2} and parameters ( α, λ) ∈ ℝ 2 ​ n Γ + 1 (\alpha,\lambda)\in\mathbb{R}^{2n_{\Gamma}+1} where α = ( α 1, …, α n) ∈ ℝ 2 ​ n Γ \alpha=(\alpha^{1},\ldots,\alpha^{n})\in\mathbb{R}^{2n_{\Gamma}}. We consider the function

 | h ⁡ ( x, α, λ) \displaystyle h(x,\alpha,\lambda) | = f ​ ( x) 2 − λ ​ ∏ p ∈ S ( ‖ x − p ‖ 2 − λ 2) ​ ∏ i = 1 n ( ‖ x − α i ‖ 2 − λ 2). \displaystyle=f(x)^{2}-\lambda\prod_{p\in S}\left(\|x-p\|^{2}-\lambda^{2}\right)\prod_{i=1}^{n}\left(\|x-\alpha^{i}\|^{2}-\lambda^{2}\right). |  |

Let us take the number n Γ n_{\Gamma}, the sequence ( α i) i ∈ ℕ (\alpha_{i})_{i\in\mathbb{N}} and the point α 0 \alpha_{0} as in Remark 3.3 and, for every i ∈ ℕ i\in\mathbb{N}, let us consider h i ​ ( x, λ) = h ⁡ ( x, α i, λ) h_{i}(x,\lambda)=h(x,\alpha_{i},\lambda). For any i ∈ ℕ i\in\mathbb{N}, we can apply Proposition 3.7 to the semialgebraic set Γ i \Gamma_{i} introduced in Remark 3.4 to deduce that there exists a value 0 < λ i < 1 i 0<\lambda_{i}<\frac{1}{i} such that the level set ( h i ​ ( x, λ) = 0) ∩ ( λ = λ i) (h_{i}(x,\lambda)=0)\cap(\lambda=\lambda_{i}) contains a subset γ i \gamma_{i} which is regular connected, compact and 1 i \frac{1}{i} -close (in respect to the Hausdorff topology) to Γ i \Gamma_{i}. Furthermore, apart from shrinking λ i \lambda_{i} if necessary, we can suppose that γ i ∩ N ​ G ​ ( Γ) = ∅ \gamma_{i}\cap NG(\Gamma)=\emptyset, because N ​ G ​ ( Γ) ⊂ A ​ l ​ g ​ ( Γ i) NG(\Gamma)\subset Alg(\Gamma_{i}) and Lemma 3.5. In particular, note that γ i → Γ \gamma_{i}\to\Gamma when i → ∞ i\to\infty since Γ i \Gamma_{i} converges to Γ \Gamma.

###### Remark 3.8.

We note that, for every point a ∈ Γ a\in\Gamma, there exists N > 0 N>0 such that γ i ∩ { a } = ∅ \gamma_{i}\cap\{a\}=\emptyset for every i > N i>N. Indeed, by construction γ i \gamma_{i} only crosses Γ i ⊃ Γ \Gamma_{i}\supset\Gamma near the points T ​ r ​ ( Γ) ∪ G ​ e ​ n ​ ( Γ i) Tr(\Gamma)\cup Gen(\Gamma_{i}). So, assuming by contradiction that there exists a point a ∈ Γ a\in\Gamma so that γ i ∩ { a } ≠ ∅ \gamma_{i}\cap\{a\}\neq\emptyset for an infinite number of i i, we conclude that a ∈ T ​ r ​ ( Γ) ∪ G ​ e ​ n ​ ( Γ) ∪ N ​ G ​ ( Γ) a\in Tr(\Gamma)\cup Gen(\Gamma)\cup NG(\Gamma). Next, by Lemma 3.6 we conclude that a ∈ N ​ G ​ ( Γ) a\in NG(\Gamma), which contradicts the choice of λ i \lambda_{i}.

It follows from the above considerations (just as in the previous Section) that the algebraic family of vector fields

 | X α, λ = ( ∂ h ∂ x 2 + h ∂ h ∂ x 1) ∂ x 1 + ( − ∂ h ∂ x 1 h + h ∂ h ∂ x 2) ∂ x 2 X_{\alpha,\lambda}=\left(\frac{\partial h}{\partial{x_{2}}}+h\frac{\partial h}{\partial x_{1}}\right)\partial_{x_{1}}+\left(-\frac{\partial h}{\partial{x_{1}}}h+h\frac{\partial h}{\partial{x_{2}}}\right)\partial_{x_{2}} |  |

has Γ \Gamma as a limit periodic set at ( α, λ) = ( α 0, 0) (\alpha,\lambda)=(\alpha_{0},0).

### 3.4. Construction of unbounded limit periodic sets

Finally, let Γ ⊂ ℝ 2 \Gamma\subset\mathbb{R}^{2} be a closed and unbounded semialgebraic set of dimension 0 0 or 1 1 whose compactification Γ ^ \hat{\Gamma} is connected. Apart from considering a translation of ℝ 2 \mathbb{R}^{2}, we can assume that ( 0, 0) ∉ Γ (0,0)\notin\Gamma.

Let us consider the transition map of the Bendixson compactification ϕ: ℝ 2 ∖ { 0 } → ℝ 2 \phi:\mathbb{R}^{2}\setminus\{0\}\to\mathbb{R}^{2} given by ϕ ( x 1, x 2) = ( x 1 / r, − x 2 / r) \phi(x_{1},x_{2})=(x_{1}/r,-x_{2}/r) where r = x 1 2 + x 2 2 r=x_{1}^{2}+x_{2}^{2} (see Section 2.1).

Note that ϕ ⁡ ( Γ) \phi(\Gamma) is a semialgebraic set (by e. g. [3, Corollary 1.8]), whose closure Z = ϕ ⁡ ( Γ) ∪ { 0 } Z=\phi(\Gamma)\cup\{0\} is a compact and connected semialgebraic set of dimension 0 0 or 1 1. By the previous Sections, there exist a polynomial family of planar vector fields ( Y λ) λ ∈ Λ (Y_{\lambda})_{\lambda\in\Lambda} and a parameter λ 0 \lambda_{0} such that Z Z is a limit periodic set for the family ( Y λ) λ (Y_{\lambda})_{\lambda} at λ 0 \lambda_{0}. We denote by ( z λ n) n (z_{\lambda_{n}})_{n} the sequence of limit cycles of Y λ Y_{\lambda} which converge to Z Z.

Let us now consider the map Φ: ( ℝ 2 ∖ { 0 }) × Λ → ℝ 2 × Λ \Phi:(\mathbb{R}^{2}\setminus\{0\})\times\Lambda\to\mathbb{R}^{2}\times\Lambda given by Φ ⁡ ( x 1, x 2, λ) = ( ϕ ⁡ ( x 1, x 2), λ) \Phi(x_{1},x_{2},\lambda)=(\phi(x_{1},x_{2}),\lambda). The pull-back Φ ∗ ​ ( Y λ) \Phi^{\ast}(Y_{\lambda}) is rational and there exists an integer d ≥ 0 d\geq 0 such that X λ = ( x 1 2 + x 2 2) d ​ Φ ∗ ​ ( Y λ) X_{\lambda}=(x_{1}^{2}+x_{2}^{2})^{d}\Phi^{\ast}(Y_{\lambda}) is a polynomial family of vector fields. According to Remark 3.8, for every sufficiently big n n, z λ n z_{\lambda_{n}} does not intersect the origin so Φ − 1 ​ ( z λ n) \Phi^{-1}(z_{\lambda_{n}}) is itself a limit cycles of X λ n X_{\lambda_{n}}. It follows from the construction that Γ \Gamma is a limit periodic set of ( X λ) λ (X_{\lambda})_{\lambda} at λ 0 \lambda_{0}.

## References

- [1] V. W. Adkisson and S. MacLane, Extending maps of plane Peano continua, Duke Math. J. 6 (1940), 216–228.
- [2] A. Belotto. Analytic varieties as limit periodic sets. Qual. Theory Dyn. Syst. 11 (2012), no. 2, 449–465.
- [3] E. Bierstone and P. Milman. Semianalytic and subanalytic sets. Inst. Hautes Études Sci. Publ. Math. (1988), no. 67, 5–42.
- [4] E. Bierstone and P. Milman, Functoriality in resolution of singularities, Publ. R.I.M.S. Kyoto Univ., 44, (2008), 609–639.
- [5] F. Dumortier, J. Llibre and J. C. Artés. Qualitative theory of planar differential systems. Springer-Verlag, Berlin, 2006.
- [6] F. Dumortier, R. Roussarie and C. Rousseau. Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations 110, (1994), no. 1, 86-133.
- [7] Y. Il’yashenko and S. Yakovenko Concerning the Hilbert sixteenth problem, in “Concerning the Hilbert 16th Problem”, 1–19. Amer. Math. Soc. Transl. Ser. 2, 165. Amer. Math. Soc., Providence, RI, 1995.
- [8] J. P. Françoise and C. Pugh, Keeping track of limit cycles, J. Differential Equations 65 (1986), no.2, 139–157.
- [9] V. Jiménez López and J. Llibre. A topological characterization of the ω \omega -limit sets for analytic flows on the plane, the sphere and the projective plane, the sphere and the projective plane. Advances in Mathematics 216 (2007), no.2, 677–710.
- [10] V. Jiménez López and D. Peralta-Salas. Global attractors of analytic plane flows. Ergodic Theory Dyn. Syst. 29 (2009), no.2, 967–981.
- [11] K. Kuratowski, Topology. Vol. II, Academic Press, New York, 1968.
- [12] J. Milnor. Singular points of complex hypersurfaces. Ann. of Math. Stud., vol. 61. Princeton University Press, New Jersey, 1968.
- [13] J. Llibre and G. Rodríguez, Configurations of limit cycles and planar polynomial vector fields. J. Differential Equations 198, (2004), no. 2, 374–380.
- [14] D. Panazzolo and R. Roussarie. A Poincaré-Bendixson theorem for analytic families of vector fields. Bol. Soc. Brasil. Mat. (N.S.) 26 (1995), no. 1, 85–116.
- [15] R. Roussarie. Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem. Progress in Mathematics, vol. 164 Birkhäuser Verlag, Basel, 1998.
- [16] R. Roussarie. Cyclicité finie des lacets et des points cuspidaux. Nonlinearity 2 (1989), no. 1, 73–117.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:andre.belotto_da_silva@math.univ-toulouse.fr
[4]: mailto:josegines.espin@um.es
