<!-- source: https://arxiv.org/html/math/0111053v1 | converted from HTML -->

Around Hilbert-Arnold Problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0111053v1 [math.DS] 06 Nov 2001

# Around Hilbert-Arnold Problem

Vadim Kaloshin

###### Abstract

This lectures notes consists of four lectures. The first lecture discusses questions around Hilbert-Arnold Problem which is naturally arises from Quantitative Hilbert 16-th problem. In the second lecture we outline author’s solution [K1] of a weak form of Local Hilbert-Arnold Problem. This solution provides an independent proof of Ilyashenko-Yakovenko Finiteness Theorem [IY2]. The third lecture discusses question of existence of a P a_{P} -stratification of Thom [T2] and presents a simple geometric proof of existence of such a stratification for polynomial functions, which was originally proven by Hironaka [Hi]. The forth lecture gives application of Grigoriev-Yakovenko’s construction to the problem of growth of the number of periodic points and the problem of bifurcation of spacial polycycles. The latter problem naturally generalizes Local Hilbert-Arnold Problem.

## Chapter 1 Around the Hilbert 16-th problem and an estimate for cyclicity of elementary polycycles.

The author is partially supported by the Sloan Dissertation Fellowship and the American Institute of Mathematics Five-Year Fellowship

### 1.1 The Hilbert 16-th Problem and its offsprings

Consider a polynomial vector field on the real ( x, y) (x,y) -plane

 | { y ˙ = P n ​ ( x, y) x ˙ = Q n ​ ( x, y) P n, Q n − polynomials, deg P n, Q n ≤ n. \displaystyle\left\{\begin{aligned} \dot{y}=P_{n}(x,y)\\ \dot{x}=Q_{n}(x,y)\end{aligned}\right.\quad P_{n},Q_{n}-{\textup{ polynomials}},\ \deg P_{n},Q_{n}\leq n. |  | (1.1) |

A limit cycle of a polynomial vector field ( 1.1) is an isolated periodic solution. Define

 | H ( n) = uniform bound for the number of limit cycle of ( 1.1). \displaystyle H(n)=\boxed{\text{uniform bound for the number of limit cycle of}\ (\ref{H}).} |  |

One way to formulate the Hilbert 16-th Problem is the following:

The Hilbert 16-th Problem (HP). Estimate H ⁡ ( n) H(n) for any n ∈ ℤ + n\in\mathbb{Z}_{+}.

To prove that H ⁡ ( 1) = 0 H(1)=0 is an exercise, but find H ⁡ ( 2) H(2) is already a difficult unsolved problem ( see [DRR], [DMR] for work in this direction). Below we discuss two of the most significant branches of research HP generated: Existential and Tangential Hilbert 16-th Problems.

#### 1.1.1 The Tangential Hilbert 16-th Problem

Consider a polynomials perturbation of a Hamiltonian polynomial line field

 | { y ˙ = − ∂ H ∂ x − ε ​ Q ​ ( x, y) y ˙ = ∂ H ∂ y + ε ​ P ​ ( x, y). \displaystyle\left\{\begin{aligned} \dot{y}=-\frac{\partial H}{\partial x}-\varepsilon Q(x,y)\\ \dot{y}=\frac{\partial H}{\partial y}+\varepsilon P(x,y).\end{aligned}\right. |  | (1.2) |

For ε = 0 \varepsilon=0 the line field ( 1.2) does not have any limit cycles at all (all cycles are nonisolated). An oval (topological circle) γ \gamma of the level curve H ⁡ ( x, y) = h H(x,y)=h generates a limit cycle for small nonzero value of ε \varepsilon if the accumulated energy dissipation is zero in the first approximation, i.e. when

 | ∮ P ( x, y) d x + Q ( x, y) d y = 0, γ ⊆ { H ( x, y) = h }. \displaystyle\oint\ P(x,y)\ dx+\ Q(x,y)\ dy=0,\quad\gamma\subseteq\{H(x,y)=h\}. |  | (1.3) |

The left-hand side expression is called a complete Abelian integral. If polynomials H, P, H,P, and Q Q are fixed the integral ( 1.3) defines a multivalued function I ⁡ ( h) I(h). Multivaluity appears when the corresponding level curve { H ( x, y) = h } \{H(x,y)=h\} has several disjoint ovals.

Tangential Hilbert 16-th Problem (THP). [A1] For any collection of polynomials H, P, H,P, and Q ∈ ℝ ⁡ [x, y] Q\in\mathbb{R}[x,y] of degree ≤ n \leq n give an upper bound T ​ H ​ ( n) TH(n) on the number of real ovals over which the integral ( 1.3) vanishes, but not identically.

In the latter case the perturbation ( 1.2) is a Hamiltonian system for ε ≠ 0 \varepsilon\neq 0 so it does not have limit cycles at all. Even though Tangential Hilbert Problem is not solved yet, in contrast to the Hilbert 16-th, there are several quite general results related to it. Khovanski [Kh1] –Varchenko [V] proved Finiteness Theorem: for any n ∈ ℤ + n\in\mathbb{Z}_{+} the number of isolated zeroes of Abelian integrals is uniformly bounded over all Hamiltonian and forms of degree ≤ n \leq n.

For various other results estimating H ⁡ ( n) H(n) in various particular cases see [Ga], [I1], [Mr], [NY1], [P], and the lecture course [NY2] in the present volume for more references.

If we consider ( 1.3) over the field of complex we have that an Abelian integral satisfies a fuchsian equation or Picard-Fuchs equation (see e.g. [AA]), i.e. an equation of the form

 | z ˙ = ∑ j A j t − α j ​ z j, where the ​ A j ​ are constant matrices \displaystyle\dot{z}=\sum_{j}\frac{A_{j}}{t-\alpha_{j}}z_{j},\quad\textup{where the}\ A_{j}\ \textup{are constant matrices} |  | (1.4) |

and z = ( z 1, …, z p) ∈ ℂ p z=(z_{1},\dots,z_{p})\in\mathbb{C}^{p} is a complex vector for some p p. Investigation of various properties of fuchsian equations is the main topic of lectures of Bolibrukh [Bo] in the present volume.

#### 1.1.2 From Existential Hilbert 16-th Problem to Hilbert-Arnold Problem

A qualitative form of Hilbert 16-th Problem is the following:

Existential Hilbert 16-th Problem (EHP). Prove that H ⁡ ( n) < ∞ H(n)<\infty for any n ∈ ℤ + n\in\mathbb{Z}_{+}.

The problem about finiteness of number of limit cycles for an individual polynomial line field ( 1.1) is called Dulac problem after the pioneering work of Dulac [Du] who claimed in 1923 to solve this problem, but an error was found by Ilyashenko [I2] 60 years later. The Dulac problem was solved by two independent, rather different and incredibly complicated proofs given almost simultaneously by Ilyashenko and Ecalle

Individual Finiteness Theorem (IFT). [I3], [E] Any polynomial line field ( 1.1) has only a finite number of limit cycles.

However, neither proof allows any generalization to solve EHP. Consider the equation ( 1.1) for different polynomials ( P n ​ ( x, y), Q n ​ ( x, y)) ∈ ℝ 2 (P_{n}(x,y),Q_{n}(x,y))\in\mathbb{R}^{2} as the family of vector fields on ℝ 2 \mathbb{R}^{2} depending on parameters of the polynomials. Using a central projection π: 𝕊 2 → ℝ 2 \pi:\mathbb{S}^{2}\to\mathbb{R}^{2} and homogeneity with respect to parameters of the equation ( 1.1) (vector fields ( λ ​ P n ​ ( x, y), λ ​ Q n ​ ( x, y)) (\lambda P_{n}(x,y),\lambda Q_{n}(x,y)) and ( P n ​ ( x, y), Q n ​ ( x, y)) (P_{n}(x,y),Q_{n}(x,y)) for any λ ≠ 0 \lambda\neq 0 have the same trajectories) one can construct a finite parameter family of analytic line fields on the sphere 𝕊 2 \mathbb{S}^{2} with a compact parameter base B B (see e.g. [IY2] for details). After this reduction Existential Hilbert Problem becomes a particular case of the following

Global Finiteness Conjecture (GFC). [R1] For any family of line fields on 𝕊 2 \mathbb{S}^{2} with a compact parameter base B B the number of limit cycles is uniformly bounded over all parameter values.

We refer the reader to the volumes [IY2], [S], and a book [R2], where various development of these and related problems are discussed. Families of analytic fields are difficult to analyze. In the middle of 80’s Arnold [AA] proposed to consider generic families of smooth vector fields as the first step toward understanding families of analytic vector fields. A smooth analog of Global Finiteness Conjecture is the following

Hilbert-Arnold Problem (HAP). [I4] Prove that in a generic finite parameter of vector fields on the sphere S 2 S^{2} with a compact base B B, the number of limit cycles is uniformly bounded.

Assume for a moment that an analytic (or a generic smooth) vector field on the sphere 𝕊 2 \mathbb{S}^{2} has an infinite number of limit cycles. By the Poincaré-Bendixon Theorem, any limit cycle should surround an equilibrium point and, since our vector field has at most finitely many equilibria, there should be an infinite “nested” sequence around one of equilibria. Then this “nested” sequence of limit cycles have to accumulate (in the sense of Hausdorff metric) to a certain contour (polygon) consisting of equilibria (as vertices) and separatric curves (sides of that polygon) connecting them. Such objects are called polycycles. It turns out that a possible solution to Hilbert-Arnold Problem reduces to investigation of bifurcation of polycycles. Let’s give several definitions.

###### Definition 1.1.1.

A polycycle γ \gamma of a vector field on the sphere 𝕊 2 \mathbb{S}^{2} is a cyclically ordered collection of equilibrium points p 1, …, p k p_{1},\dots,p_{k} (with possible repetitions) and arcs γ 1, …, γ k \gamma_{1},\dots,\gamma_{k} (distinct integral curves consisting possibly from equilibrium points) connecting them in the specific order: the j-th arc γ j \gamma_{j} connects p j p_{j} with p j + 1 p_{j+1} for j = 1, …, k j=1,\dots,k.

A polycycle γ \gamma is called monodromic if one can choose a segment Σ \Sigma transversal to γ \gamma such that one side U ⊂ Σ U\subset\Sigma of p = Σ ∩ γ p=\Sigma\cap\gamma a Poincare return map Δ γ: U → Σ \Delta_{\gamma}:U\to\Sigma is defined with Δ γ ​ ( p) = p \Delta_{\gamma}(p)=p.

Nonaccumulation Theorem. [I3], [E] For any analytic monodromic polycycle γ \gamma there is a tube neighborhood free from limit cycles or a Poincare return map Δ γ: Σ ⊃ U → Σ \Delta_{\gamma}:\Sigma\supset U\to\Sigma can’t have infinitely many fixed points accumulating to p = Σ ∩ γ p=\Sigma\cap\gamma.

This Theorem along with above compactness arguments implies IFT. Both proofs of Ilyashenko and Ecallé deal with analysis of type of germs of maps arising as Poincare return maps of an analytic monodromic polycycle. Lectures by van den Dries [Dr1] (see also [Dr2]) in the present volume discusses the theory of o-minimality. This theory deals with classes of functions which satisfy certain axioms. A basic example of o-minimal class of functions is polynomials and analytic functions. In particular, if a map of a compact interval Δ: U → ℝ \Delta:U\to\mathbb{R} belongs to an o-minimal class of functions, then the equation Δ ⁡ ( x) = x \Delta(x)=x has a finitely many solutions. One of hopes is that deeper understanding of o-minimal structures would allow to include Poincare return maps of monodromic polycycles into an o-minimal class and give an independent proof of Nonaccumulation Theorem. Finiteness Theorems for differentiable function fields are discussed in lectures by Buium [Bu] in the present volume.

###### Definition 1.1.2.

Let { x ˙ = v ( x, ε) } ε ∈ B n, x ∈ 𝕊 2, \{\dot{x}=v(x,\varepsilon)\}_{\varepsilon\in B^{n}},\ x\in\mathbb{S}^{2}, be an n n -parameter family of vector fields on 𝕊 2 \mathbb{S}^{2} having a polycycle γ \gamma for some parameter value ε ∗ ∈ B n \varepsilon_{*}\in B^{n}. The polycycle γ \gamma has cyclicity μ \mu in the family { v ⁡ ( x, ε) } ε ∈ B n \{v(x,\varepsilon)\}_{\varepsilon\in B^{n}} if there exist neighborhoods U U and V V such that 𝕊 2 ⊇ U ⊃ γ, B ⊇ V ∈ ε ∗ \mathbb{S}^{2}\supseteq U\supset\gamma,\ B\supseteq V\in\varepsilon_{*} and for any ε ∈ V \varepsilon\in V the field v ⁡ ( ⋅, ε) v(\cdot,\varepsilon) has no more than μ \mu limit cycles inside U U and μ \mu is the minimal number with this property.

Examples: 1) In a generic n n -parameter family, the maximal multiplicity of a degenerate limit cycle does not exceed n + 1 n+1, e.g. in codimension 1 1 a semistable limit cycle has cyclicity 2 2. Thus, the cyclicity of a trivial polycycle (a polycycle without singular points) in a generic n n -parameter family does not exceed n + 1 n+1.

2) (Andronow-Leontovich, 1930s; Hopf, 1940s). A nontrivial polycycle of codimension 1 1 has cyclicity at most 1 1.

3) (Takens, Bogdanov, Leontovich, Mourtada, Grozovskii, early 1970s-1993 (see [Gr], [KS], and references there)). A nontrivial polycycle of codimension 2 2 has cyclicity at most 2 2.

###### Definition 1.1.3.

The bifurcation number B ⁡ ( k) B(k) is the maximal cyclicity of a nontrivial polycycle occurring in a generic k k -parameter family.

The definition of B ⁡ ( k) B(k) does not depend on a choice of the base of the family, it depends only on the number k k of parameters.

Local Hilbert-Arnold Problem (LHAP). [I4] Prove that for any finite k k, the bifurcation number B ⁡ ( k) B(k) is finite and find an upper estimate for B ⁡ ( k) B(k).

It turns out that a solution to Local Hilbert-Arnold Problem implies a solution to Hilbert-Arnold Problem.

Similarly to the generic smooth vector fields, in the case of analytic vector fields one can define so-called a limit periodic set [FP], [R1], which is either a polycycle or has an arc of equilibrium points 1 1 1 generic vector fields can not have an arc of equilibrium points, and formulate

Local Finiteness Conjecture (LFC). [R1] Prove that any limit periodic set occurring in an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} has finite cyclicity in this family.

Smooth vector fields are more flexible then analytic vector fields and easier to analyze. A strategy to attack Existential Hilbert Problem, proposed by Arnold [AA] (see also [IK]), is first understand generic smooth vector fields and then try to apply developed methods to analytic vector fields. Let us summarize the discussion in the form of the diagram:

[image: Refer to caption] Figure 1.1: Existential Hilbert Problem and its offsprings

#### 1.1.3 Cyclicity of Elementary Polycycles

Now we shall formulate the Main Result of this course of lectures.

###### Definition 1.1.4.

An equilibrium point of a vector field on the two-sphere is called elementary if at least one eigenvalue of its linear part is nonzero. A polycycle is called an elementary polycycle if all its singularities are elementary.

The Local Hilbert-Arnold problem was solved under the additional assumption that a polycycle have elementary singularities only.

###### Definition 1.1.5.

The elementary bifurcation number E ⁡ ( k) E(k) is the maximal cyclicity of a nontrivial elementary polycycle occurring in a generic k k -parameter family.

From examples 2) and 3) above it follows that

 | E ⁡ ( 1) = 1, E ⁡ ( 2) = 2. E(1)=1,\quad E(2)=2. |  |

Information about behavior of the function k ↦ E ⁡ ( k) k\mapsto E(k) has been obtained recently. The First crucial step was done by Ilyashenko and Yakovenko:

Finiteness of Elementary Cyclicity (FEC). [IY2] For any n n the elementary bifurcation number E ⁡ ( n) E(n) is finite.

###### Corollary 1.1.6.

Under the assumption that families of vector fields have elementary singularities only the Global Hilbert-Arnold Problem is solved, i.e. any generic finite parameter family of vector fields on the sphere 𝕊 2 \mathbb{S}^{2} with a compact base and only elementary equilibria has a uniform upper bound for the number of limit cycles.

Main Theorem. [Ka1] For any k ∈ ℤ + k\in\mathbb{Z}_{+}

 | E ⁡ ( k) ≤ 2 25 ​ k 2. \displaystyle E(k)\leq 2^{25k^{2}}. |  | (1.5) |

This is the first explicit general estimate for cyclicity of polycycle. The case of a polycycle consisting only one singular point with no arcs at all is well known. An elementary equilibrium point can generate limit cycles in its small neighborhood if it is a slow focus, that is the linearization matrix has a pair of two imaginary eigenvalues. This bifurcation was investigated by Takens [Ta].

###### Corollary 1.1.7.

As in Corollary 1.1.6 under the assumption that all the polycycles are elementary the Main Theorem gives a solution to the Local Hilbert-Arnold Problem.

#### 1.1.4 Resolution of Singularities (RS) or Blow-up of Singularities of Vector Fields and Singular Perturbations (SP)

In this subsection we discuss Resolution of Singularities and Singular Perturbation which might lead to generalization of the Main Result to a solution to Local Hilbert-Arnold Problem (see the box with RS & SP? in the diagram 1.1).

Let x ˙ = v ⁡ ( x) \dot{x}=v(x) be a C ∞ C^{\infty} vector field on ℝ 2 \mathbb{R}^{2} such that v ⁡ ( 0) = 0 v(0)=0. A vector field satisfies a Lojasiewicz condition if there exists k ∈ ℤ + k\in\mathbb{Z}_{+} and c > 0 c>0 such that

 | ‖ v ⁡ ( x) ‖ ≥ c ​ ‖ x ‖ k \displaystyle\|v(x)\|\geq c\|x\|^{k} |  | (1.6) |

for all x x from some neighborhood of 0 0. It can be shown [D] that any generic finite-parameter family of vector fields on the sphere 𝕊 2 \mathbb{S}^{2} has only vector fields with equilibrium points satisfying a Lojasiewicz condition for some k ∈ ℤ + k\in\mathbb{Z}_{+} and c > 0 c>0.

To define a blow up for a C ∞ C^{\infty} vector field x ˙ = v ⁡ ( x) \dot{x}=v(x) on ℝ 2 \mathbb{R}^{2} with an equilibrium at 0 0, i.e. v ⁡ ( 0) = 0 v(0)=0 consider the map

 | ϕ: 𝕊 1 × ℝ → ℝ 2; ϕ ⁡ ( θ, r) ↦ ( r ​ cos ⁡ θ, r ​ sin ⁡ θ). \displaystyle\phi:\mathbb{S}^{1}\times\mathbb{R}\to\mathbb{R}^{2};\quad\phi(\theta,r)\mapsto(r\cos\theta,r\sin\theta). |  | (1.7) |

Then the pull-back v ^ \hat{v} with ϕ ⁡ ( v ^) = v \phi(\hat{v})=v, is a C ∞ C^{\infty} vector field on 𝕊 1 × ℝ \mathbb{S}^{1}\times\mathbb{R}, i.e. d ​ ϕ 0 ​ ( v ^ ​ ( 0)) = X ∘ ϕ ⁡ ( 0) d\phi_{0}(\hat{v}(0))=X\circ\phi(0), where v ^ \hat{v} is the blown-up vector field.

Desingularization Theorem. [D] If a C ∞ C^{\infty} vector field x ˙ = v ⁡ ( x) \dot{x}=v(x) on ℝ 2 \mathbb{R}^{2} with v ⁡ ( 0) = 0 v(0)=0 satisfying a Lojasiewicz condition, then there is a finite sequence of blow-ups leading to a vector field with only elementary equilibria.

Sometimes this theorem is called Bendixon-Seidenberg-Dumortier [Be], [Se], [D]. Bendixon stated it without a proof it on the brink of the twentieth century. Seidenberg proved it in the analytic case and Dumortier did it for C ∞ C^{\infty} vector fields with a Lojasiewicz condition. A quantitative version of the Desingularization Theorem, which estimates number of necessary blow-ups, was obtained by Kleban [Kl].

This Theorem reduces consideration of an individual vector field, occurring in a generic finite-parameter family, with equilibria without restriction to an individual vector field with only elementary equilibria.

However, in order to extend an estimate on cyclicity of elementary polycycles ( 1.5) to an estimate on cyclicity of a generic nonelementary polycycle (LHAP) one needs Desingularization Theorem for families of generic C ∞ C^{\infty} vector fields. Different approaches to attack this problem were proposed by Denkowska and Roussarie [DeR] and by Trifonov [Tr].

An approach proposed by Trifonov leads the dynamical phenomenon called Singular Perturbation (SP): in the simplest case one needs to analyze families of vector fields on the plane, which for some values of parameters have a curve of equilibria. Certainly, a generic finite-parameter family of vector fields has no curve of equilibria, however, after even one step of blow-up such a curves can occur [Tr]. Appearance of curves of equilibria after a desingularization in a family now seems to be the main obstacle between an estimate on cyclicity of elementary polycycles ( 1.5) and Local Hilbert Arnold Problem (see [Tr], [IY2], and [R2] for more).

### 1.2 Bifurcation of Spatial Polycycles and Multiplicity of Generic Germs

In this part we present by-product results the Main Theorem. The first result is an extension of the Main Theorem on estimate of cyclicity of planar elementary polycycle to an estimate on cyclicity of spatial quasielementary polycycle (see section 1.2.1). The second result gives an estimate on cyclicity of generic germs of smooth mappings which is a partial answer to Arnold’s question [A2] (see section 1.2.4).

#### 1.2.1 Bifurcation of Spatial Polycycles

Definition of a polycycle in a multidimensional case is the same as in the planar case verbal (see definition 1.1.1). When Ilyashenko and Yakovenko proved the Finiteness of Cyclicity for elementary polycycles, Arnold posed the question: What can be said about bifurcations of spatial polycycles?

Another sufficient reason to look at this problem is, because the planar argument (the Poincaré-Bendixon Theorem) imply that a collection of an infinite number of limit cycles of uniformly bounded length, located in a bounded domain, accumulate to a limit cycle. Indeed, consider a vector field x ˙ = v ⁡ ( x) \dot{x}=v(x) of a finite codimension in ℝ 3 \mathbb{R}^{3} (dimension 3 3 can be replaced by any N > 2 N>2 anywhere in this section), i.e. a vector field which occurs in a generic finite-parameter family. Then v ⁡ ( x) v(x) has only isolated singular points. Fix a positive number L L and assume that in a compact region of the phase space there are an infinite number of phase curves of length less L L corresponding to limit cycles of v ⁡ ( x) v(x). Then a subset of these limit cycles must accumulate to a separatric polygon (polycycle).

Bifurcation properties of spatial polycycles are much richer then those of planar polycycles. The first important 3 3 -dimensional feature is existence of limit cycles that winds several times around a polycycle. It happens because a Poincaré return map is a 2 2 -dimensional map and it might have not only fixed point, but also periodic points of higher periods too. We call a periodic trajectory that “turns” around a whole polycycle exactly m m -times before closing up an m m - cycle. Such a trajectory corresponds to a periodic point of a corresponding Poincaré return map of minimal period m m. On the plane because of topological reasons only 1 1 -cycles exist. Definition of cyclicity requires some additional care.

Consider an n n -parameter family of flows { x ˙ = v ( x, ε) } ε ∈ B n \{\dot{x}=v(x,\varepsilon)\}_{\varepsilon\in B^{n}} in ℝ 3 \mathbb{R}^{3}. Let γ ⊂ ℝ 3 \gamma\subset\mathbb{R}^{3} be a polycycle of the field x ˙ = v ⁡ ( x, ε ∗) \dot{x}=v(x,\varepsilon^{*}) for some ε ∗ ∈ B n \varepsilon^{*}\in B^{n}. Then γ \gamma can be represented as a union of a finite number of equilibrium points { p j } j ∈ J \{p_{j}\}_{j\in J} and connecting them phase curves { γ j } j ∈ J \{\gamma_{j}\}_{j\in J}. A tube neighborhood T γ T_{\gamma} of the polycycle γ \gamma is a union of neighborhoods of equilibria { p j } j ∈ J \{p_{j}\}_{j\in J} and tube neighborhoods { T j } j ∈ J \{T_{j}\}_{j\in J} of phase curves { γ j } j ∈ J \{\gamma_{j}\}_{j\in J}.

###### Definition 1.2.1.

Let m ∈ ℤ + m\in\mathbb{Z}_{+}. Then m m -cyclicity of the polycycle γ \gamma in the family { x ˙ = v ( x, ε) } ε ∈ B n \{\dot{x}=v(x,\varepsilon)\}_{\varepsilon\in B^{n}}, denoted by μ ⁡ ( m, γ) \mu(m,\gamma), is a minimal number μ ⁡ ( m, γ) \mu(m,\gamma) for which there is a tube neighborhood T γ T_{\gamma} of the polycycle γ ⊂ T γ ⊂ ℝ 3 \gamma\subset T_{\gamma}\subset\mathbb{R}^{3}, a neighborhood V V of the parameter ε ∗ ∈ V ⊂ B n \varepsilon^{*}\in V\subset B^{n} and for each j ∈ J j\in J Poincaré section L γ, j L_{\gamma,j} (a hyperplane) transversal to the corresponding γ j \gamma_{j} such that the following condition holds:

1. for any parameter ε ∈ V \varepsilon\in V the corresponding vector field x ˙ = v ⁡ ( x, ε) \dot{x}=v(x,\varepsilon) has at most μ ⁡ ( m, γ) \mu(m,\gamma) limit cycles in T γ T_{\gamma};

2. Each of those limit cycles l i ​ ( ε) l_{i}(\varepsilon) intersects each Poincaré section L γ, j L_{\gamma,j} in exactly m m different points;

3. In the sense of Hausdorff metric for each j ∈ J j\in J distance between each part of l j ​ ( ε) l_{j}(\varepsilon), which lies between two consecutive intersections of L γ, j L_{\gamma,j}, and the polycycle γ \gamma tends to 0 0 as ε \varepsilon tends to 0 0.

Now we discuss a classical example of a polycycle which has infinite m m -cyclicity for any m ≥ 1 m\geq 1.

#### 1.2.2 The Shilnikov polycycle

Consider a flow ϕ t \phi_{t} in ℝ 3 \mathbb{R}^{3} with a hyperbolic equilibrium point O O that has one positive eigenvalue λ \lambda and two complex conjugates μ ± ω \mu\pm\omega with negative real part. Suppose that the sum of λ + μ \lambda+\mu is positive, and the unstable one-dimensional manifold returns to the stable one, which is two-dimensional. Thus, the equilibrium O O has a homoclinic orbit that tends back to O O along the unstable manifold as t → − ∞ t\to-\infty, and spirals around O O on the stable manifold as t → + ∞ t\to+\infty. In 1965 Shilnikov [Sh] discovered that the Poincaré map along this polycycle has a countable number of pairwise disjoint subdomains so that a restriction to each of them gives a Smale horseshoe. Any of such horseshoes is structurally stable, therefore, the polycycle described above (the Shilnikov polycycle) has an infinite m m -cyclicity for all m ∈ ℤ + m\in\mathbb{Z}_{+} (see e.g. [GH], [IL]). Codimension of this polycycle is 1 1.

[image: Refer to caption] Figure 1.2: The Shilnikov Polycycle

However, it seems reasonable to state the following

Conjecture (Arnold-Ilyashenko-Yakovenko) If a spatial polycycle γ ∈ ℝ 3 \gamma\in\mathbb{R}^{3} has finite codimension k k and all its equilibrium points are saddles with real eigenvalues or saddlenodes with at most one zero eigenvalue and the other eigenvalues are real, then the m m -cyclicity of γ \gamma, denoted C ⁡ ( m, γ) C(m,\gamma), is finite for each m ∈ ℤ + m\in\mathbb{Z}_{+}.

Using the ideas and methods for the planar problem and a result of Grigoriev-Yakovenko [GY] Arnold-Ilyashenko-Yakovenko’s Conjecture has been solved in arbitrary dimension N > 2 N>2 with additional nondegeneracy assumptions on polycycle’s equilibria.

#### 1.2.3 An estimate of the cyclicity of a quasielementary spatial polycycle

In the planar case we considered polycycles with elementary equilibria only, now we define a class of points called quasielementary equilibria. The author has shown that polycycles with quasielementary equilibria only have finite m m -cyclicity for any m ≥ 1 m\geq 1. Moreover, there exists an explicit upper bound for m m -cyclicity.

Recall some standard definitions from the normal form theory.

###### Definition 1.2.2.

The set of complex numbers λ 1, …, λ N ∈ ℂ \lambda_{1},\dots,\lambda_{N}\in\mathbb{C} is called :

a) nonresonant if there is no integral relation among the numbers λ j \lambda_{j} of the form λ j = ∑ i = 1 N k i ​ λ i \lambda_{j}=\sum_{i=1}^{N}k_{i}\lambda_{i}, where k i ∈ ℤ + k_{i}\in\mathbb{Z}_{+} for i = 1, …, n i=1,\dots,n and ∑ i = 1 N k i ≥ 2 \sum_{i=1}^{N}k_{i}\geq 2.

b) strongly simply resonant if all the nontrivial resonance relations λ j = ∑ i = 1 N k i ​ λ i \lambda_{j}=\sum_{i=1}^{N}k_{i}\lambda_{i} follows from the single one ∑ i = 1 N k i ∗ ​ λ i = 0 \sum_{i=1}^{N}k^{*}_{i}\lambda_{i}=0, where k i ∈ ℤ +, i = 1, …, n k_{i}\in\mathbb{Z}_{+},\ i=1,\dots,n and ∑ i = 1 N k i ≥ 2 \sum_{i=1}^{N}k_{i}\geq 2.

###### Definition 1.2.3.

We shall call an equilibrium point of a differential equation quasielementary, if the linearization matrix of the equation at this point has only real eigenvalues, at most one of them is zero, and they satisfy one of the following conditions:

1) they are nonresonant and we call such an equilibrium a nonresonant saddle;

2) they form a strongly simply resonant set of numbers— a strongly simply resonant saddle;

3) one eigenvalue is zero with Lojasiewicz exponent 2 and the others form a nonresonant set.

A polycycle is called quasielementary if all its vertices are quasielementary.

Note that the class of quasielementary points in the case of the plane ( N = 2 N=2) coincides with the class of elementary points, except of multiplicity two condition for saddlenodes. In a sense, Theorem 1.2.5 below is a generalization of Theorem 1.5.

###### Definition 1.2.4.

The quasielementary bifurcation number Q ​ E ​ ( N, n, m) QE(N,n,m) is the maximal m m -cyclicity of a quasielementary polycycle occurring in a generic n n -parameter families of vector fields in ℝ N \mathbb{R}^{N}.

###### Theorem 1.2.5.

[Ka2] For any positive integer N N (dimension of the phase space), n n (number of parameters), m m (number of turns around a polycycle), and T = 6 ​ N ​ n ​ m T=6Nnm we have

 | Q ​ E ​ ( N, n, m) ≤ 2 T 2. QE(N,n,m)\leq 2^{T^{2}}. |  |

In the next section we describe another by-product of the Main Theorem.

#### 1.2.4 Geometric multiplicity of germs of generic maps

Let F: ℝ n → ℝ n F:\mathbb{R}^{n}\to\mathbb{R}^{n} be a generic C k C^{k} smooth map, k ≥ n + 1 k\geq n+1. Fix a point a ∈ ℝ n a\in\mathbb{R}^{n} and denote F ⁡ ( a) F(a) by b b.

###### Definition 1.2.6.

A geometric multiplicity of a map germ F: ( ℝ n, a) → ( ℝ n, b) F:(\mathbb{R}^{n},a)\to(\mathbb{R}^{n},b) at a a, denoted by μ a G = μ a G ​ ( F) \mu^{G}_{a}=\mu^{G}_{a}(F), is the maximal number of isolated preimages F − 1 ​ ( b ~) F^{-1}\left(\tilde{b}\right) close to a a:

 | μ a G ​ ( F) = lim sup r → 0 sup b ~ ∈ ℝ n #⁡ { x ∈ B r ​ ( a): F ⁡ ( x) = b ~ }. \displaystyle\mu^{G}_{a}(F)=\limsup_{r\to 0}\sup_{\tilde{b}\in\mathbb{R}^{n}}\#\{x\in B_{r}(a):F(x)=\tilde{b}\}. |  | (1.8) |

For example, the geometric multiplicity of the function f: x → x 2 f:x\to x^{2} at 0 0 is two, but the geometric multiplicity of f: x → x 3 f:x\to x^{3} at 0 0 is one, even though 0 0 is a degenerate point of the second order.

In the complex case the geometric multiplicity equals the usual multiplicity (see e.g. [AGV]). In the real case the first is no greater than the second.

###### Definition 1.2.7.

Define geometric multiplicity of n n -dimensional germs, μ G ​ ( n) \mu^{G}(n), as follows. Let F: ℝ n → ℝ n F:\mathbb{R}^{n}\to\mathbb{R}^{n} be a generic map. The geometric multiplicity of F F equals the least upper bound of geometric multiplicities of μ a G ​ ( F) \mu^{G}_{a}(F) taken over all points a ∈ ℝ n a\in\mathbb{R}^{n}. Then the geometric multiplicity of n n -dimensional germs is the maximum of the geometric multiplicities of all generic maps F F from ℝ n \mathbb{R}^{n} to ℝ n \mathbb{R}^{n}

 | μ G ​ ( n) = sup F − generic, a ∈ ℝ n μ a G ​ ( F). \displaystyle\mu^{G}(n)=\sup_{F-\text{generic},\ a\in\mathbb{R}^{n}}\mu^{G}_{a}(F). |  | (1.9) |

It turns out that the geometric multiplicity of n n -dimensional germs is finite for all positive integer n n and depends only on dimension n n.

###### Remark 1.2.8.

For example, for n = 2 n=2 the Whitney Theorem about maps of surfaces states that a generic map of two dimensional manifolds F: M 2 → N 2 F:M^{2}\to N^{2} can have only three different types of germs: 1-to-1, a fold, and a pleat (see e.g. [AGV]). This implies that μ G ​ ( 2) = 3 \mu^{G}(2)=3.

A natural problem posed by Arnold [A2] is to give estimates for the geometric multiplicity μ G ​ ( n) \mu^{G}(n) of n n -dimensional germs.

In the case of complex analytic maps of ℂ n \mathbb{C}^{n} into ℂ n \mathbb{C}^{n} Gabrielov and Khovanskii [GK] Thm.7 obtained an estimate on μ G ​ ( n) \mu^{G}(n) of the type μ G ​ ( n) ≤ n n \mu^{G}(n)\leq n^{n}. The upper bound for the geometric multiplicity for n n -dimensional smooth germs of generic maps is given by

###### Theorem 1.2.9.

[Ka1] The geometric multiplicity of germs of a generic C k C^{k} smooth map F: ℝ n → ℝ n, k > n F:\mathbb{R}^{n}\to\mathbb{R}^{n},\ k>n admits the following upper estimate:

 | μ a G ​ ( F) ≤ 2 n ⁡ ( n − 1) / 2 + 1 ​ n n, ∀ a ∈ ℝ n. \displaystyle\mu^{G}_{a}(F)\leq 2^{n(n-1)/2+1}n^{n},\ \forall\ a\in\mathbb{R}^{n}. |  | (1.10) |

Using the same method one can prove

###### Theorem 1.2.10.

[Ka1] Let F: ℝ n → ℝ N F:\mathbb{R}^{n}\to\mathbb{R}^{N} be a generic C k C^{k} smooth map with k > n, N ≥ n k>n,\ N\geq n and P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} be a polynomial of degree d d. Then the geometric multiplicity of germs of a chain map P ∘ F: ℝ n → ℝ n P\circ F:\mathbb{R}^{n}\to\mathbb{R}^{n} admits the following upper estimate:

 | μ a G ​ ( P ∘ F) ≤ 2 n ⁡ ( n − 1) / 2 + 1 ​ ( d ​ n) n, ∀ a ∈ ℝ n. \displaystyle\mu^{G}_{a}(P\circ F)\leq 2^{n(n-1)/2+1}(dn)^{n},\ \forall\ a\in\mathbb{R}^{n}. |  | (1.11) |

An interesting feature of this theorem is that the geometric multiplicity does not depend on dimension N N of the intermediate space.

The problem about an upper estimate of geometric multiplicity of germs of generic smooth maps F: ( ℝ n, 0) → ( ℝ n, 0) F:(\mathbb{R}^{n},0)\to(\mathbb{R}^{n},0) or chain maps P ∘ F: ( ℝ n, 0) → ( ℝ n, 0) P\circ F:(\mathbb{R}^{n},0)\to(\mathbb{R}^{n},0) is closely related to the problem about an estimate cyclicity of elementary polycycles as the reader will see below.

All the results (The Main Theorem, Theorem 1.2.5, Theorem 1.2.9, and Theorem 1.2.10) were announced in [Ka3].

### 1.3 Three stages of the proof of the Main Theorem and outline of the content of the lectures

The Main Theorem is an quantitative extension of Ilyashenko-Yakovenko Finiteness Theorem. The paper of Ilyashenko-Yakovenko [IY2] was a corner stone for the present paper. In [IY2] the authors made an important step: they found a pass from bifurcation theory to singularity theory using the Khovanskii reduction method [Kh1]. In [Ka1] we follow this pass up at the beginning and using some new ideas get an estimate for the cyclicity of elementary polycycles. Below we outline the main steps of the proof of the Main Theorem and describe the content of the coming lectures.

The proof of the Main Theorem consists of three steps. Relation to the proof of the Finiteness Theorem [IY2] is discussed in section 1.3.2

Step 1. Normal forms for local families of vector fields and their integration. We use normal forms to establish an explicit form for the Poincaré correspondence map near equilibrium points on the polycycle under consideration. In [MR] and later in [IY2] it is noticed that these maps satisfy Pfaffian (polynomial differential) equations with coefficient of polynomials depending smoothly on the parameters of the family. As the result a basic system of equations, determining the number of limit cycles, is obtained.

Step 2. The Khovanskii reduction method. We discuss a variation of the Khovanskii method [Kh2]. This method allows us to investigate systems of equations that involve functions satisfying Pfaffian equations. It turns out that the number of solutions to the basic system can be estimated by the number of solutions to a mixed functional-Pfaffian system. After an application of the Khovanskii method to the mixed functional-Pfaffian system we obtain several chain maps: the maps of the form

 | x ↦ ( P 1, …, P n) ∘ ( x, f ⁡ ( x), f ′ ​ ( x), …, f ( n) ​ ( x)), \displaystyle x\mapsto(P_{1},\dots,P_{n})\circ\left(x,f(x),f^{\prime}(x),\dots,f^{(n)}(x)\right), |  | (1.12) |

where x x is a point nearby 0 ∈ ℝ n 0\in\mathbb{R}^{n}, f f is a generic function, f ( k) ​ ( x) f^{(k)}(x) is collection of all derivatives of f f of order k k, and P = ( P 1, …, P n) P=(P_{1},\dots,P_{n}) is a vector-polynomial given by its coordinate functions of known degree.

It turns out that the problem of estimating the number of limit cycles reduces to estimating the number of small regular preimages of some special points by the chain map. Special points form an open cone-like semialgebraic set K K approaching to 0 0 in the image, e.g. if K ⊂ ℝ 2, K\subset\mathbb{R}^{2}, then K = { ( x 1, x 2): 0 < x 2 < x 1 m } K=\{(x_{1},x_{2}):0<x_{2}<x_{1}^{m}\} for some m ∈ ℤ + m\in\mathbb{Z}_{+}.

Denote by F F the map F: x ↦ ( x, f ⁡ ( x), f ′ ​ ( x), …, f ( n) ​ ( x)) F:x\mapsto(x,f(x),f^{\prime}(x),\dots,f^{(n)}(x)) which is called the n n -th jet of f f. Denote by L F L_{F} the linearization of F F at point x = 0 x=0.

Lecture 2 highlights Steps 1 and 2 in a simple nontrivial case.

Step 3. Bezout’s theorem for the Chain maps. We shall construct an algebraic set Σ \Sigma in the image of F F (in the space of n n -jets) so that if F F is transversal to Σ \Sigma, then the number of preimages of any point a a from a set of special points K K is the same for F F and its linearization L F L_{F} at zero:

 | #⁡ { x: P ∘ F ⁡ ( x) = a } = #⁡ { x: P ∘ L F ​ ( x) = a } ≤ ∏ j = 1 k deg ⁡ P j. \displaystyle\#\{x:P\circ F(x)=a\}=\#\{x:P\circ L_{F}(x)=a\}\leq\prod_{j=1}^{k}\deg P_{j}. |  | (1.13) |

Since L F L_{F} is a linear map, one can apply Bezout’s theorem to estimate the right-hand part of the equality. This observation completes the proof of the Main Theorem.

In order to prove existence of such a set Σ \Sigma we need to apply stratification theory originated by works of Whitney [Wh], Thom [Th1], and Mather [Ma]. More exactly, we need to prove existence of so-called a P a_{P} -stratification introduced by Thom in some special case [Ka1]. Lecture 3 presents necessary notions from stratification theory and states the required result on existence of a P a_{P} -stratification.

#### 1.3.1 Multichain maps and bifurcation of spatial polycycles

In order to get an estimate on cyclicity of spatial polycycles Theorem 1.2.5 we face the problem of estimating geometric multiplicity of multichain maps of the form

 | P ∘ ( F, F): B n × B n → ℝ 2 ​ n, \displaystyle P\circ(F,F):B^{n}\times B^{n}\to\mathbb{R}^{2n}, |  | (1.14) |

where B n ⊂ ℝ n B^{n}\subset\mathbb{R}^{n} is a unit ball, F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} is a generic map and P: ℝ 2 ​ N → ℝ 2 ​ n P:\mathbb{R}^{2N}\to\mathbb{R}^{2n} is a vector-polynomial of known degree. Appearance of this problem is described with many more details in lecture 4. It is no longer possible to treat the 2 2 -tuple map

 | ( F, F): B n × B n → ℝ N × ℝ N \displaystyle(F,F):B^{n}\times B^{n}\to\mathbb{R}^{N}\times\mathbb{R}^{N} |  | (1.15) |

as a generic map.

Step 4. Blow-up along the diagonal in the multijet space

Grigoriev and Yakovenko [GY] constructed a so-called space of divided differences or 𝒟 ​ 𝒟 2 {\mathcal{DD}}_{2} -space and the following commutative diagram:

[image: Refer to caption] Figure 1.3: Polynomial blow-up of the multijet space

where 𝒟 2 ​ ( F): B n × B n → 𝒟 ​ 𝒟 2 ​ ( B n, ℝ N) {\mathcal{D}}_{2}(F):B^{n}\times B^{n}\to{\mathcal{DD}}_{2}(B^{n},\mathbb{R}^{N}) is a smooth map, π 2: 𝒟 ​ 𝒟 2 ​ ( B n, ℝ N) → ℝ 2 ​ N \pi_{2}:{\mathcal{DD}}_{2}(B^{n},\mathbb{R}^{N})\to\mathbb{R}^{2N} is an explicitly computable polynomial and

 | π 2 ∘ 𝒟 2 ​ ( F) = ( F, F): B n × B n → ℝ 2 ​ N. \displaystyle\pi_{2}\circ{\mathcal{D}}_{2}(F)=(F,F):B^{n}\times B^{n}\to\mathbb{R}^{2N}. |  | (1.16) |

It turns out that one can treat 𝒟 2 ​ ( F) {\mathcal{D}}_{2}(F) as a generic map for a generic F F and impose various transversality conditions. Therefore, we can represent the multichain map P ∘ ( F, F) P\circ(F,F), given by ( 1.14), in the form

 | P ∘ ( F, F) = ( P ∘ π 2) ∘ 𝒟 2 ​ ( F), \displaystyle P\circ(F,F)=(P\circ\pi_{2})\circ{\mathcal{D}}_{2}(F), |  | (1.17) |

where P ∘ π 2 P\circ\pi_{2} is a polynomial, since π 2 \pi_{2} is a polynomial, and 𝒟 2 ​ ( F) {\mathcal{D}}_{2}(F) is a smooth map. Moreover, it turns out that 𝒟 2 ​ ( F) {\mathcal{D}}_{2}(F) is generic for a generic F F. Now we can apply Bezout’s Theorem to the chain map ( P ∘ π 2) ∘ 𝒟 2 ​ ( F) (P\circ\pi_{2})\circ{\mathcal{D}}_{2}(F). In lecture 4 we describe this construction with details and in greater generality and exhibit application of this construction to an old problem of the rate of growth of the number of periodic points for generic diffeomorphisms in smooth dynamic systems ( see e.g. [AM] and [Sm]).

#### 1.3.2 Relation of the proof of Main Theorem and Ilyashenko-Yakovenko Finiteness Theorem [IY2]

Steps 1 of both proofs [IY2] and [Ka1] are the same. We shall just present the table of required normal forms from [IY2], which were obtained in [IY1]. Step 2 in this proof is slightly different from the one in [IY2] and this is the first novel point. After application of the Khovanskii method we obtain the same collection of chain maps of the form ( 1.12) as in [IY2]. However, in [IY2] the authors investigate the number of regular preimages of points in the image by the chain maps without any restriction on those points. In the present proof, using new additional arguments in the Khovanskii method, we reduce consideration to only preimages of special points, i.e. points from a tiny cone-like set in the image. At this point our proof goes independently. The proof from [Ka1] can be considered as an independent simplified proof of Ilyashenko-Yakovenko’s Finiteness Theorem by modulo of derivation of mixed functional-Pfaffian system.

Acknowledgments: I would like to thank Dana Schlomiuk for giving an great opportunity to give a course of lectures in a workshop held in Montreal during June 2000. Special thank goes to my teacher Yulij Ilyashenko who patiently taught me bifurcation theory and whose long lasting support and encouragement have been crucial source of energy. Discussions with William Cowieson, Andrei Gabrielov, Askold Khovanskii, Pavao Mardesic, John Mather, Robert Moussu, Oleg Shelkovnikov, Sergei Yakovenko have been very helpful for me. I would like also to thank Christiane Rousseau and Robert Roussarie for inviting me to give series of lectures on the bifurcation of limit cycles in Montreal and Dijon and for useful discussions. These series of lectures have been extremely helpful to improve the presentation of the present here lectures. I would like to acknowledge financial support and very productive atmosphere of Institute for Physical Sciences and Technology University of Maryland and Courant Institute of Mathematical Science, NYU, where various parts of the work have been done. While in the Institute for Physical Sciences and Technology I had enjoyed fruitful discussions with James Yorke and Brian Hunt.

## Chapter 2 Normal Forms and The Khovanskii Method.

We explain the proof of the Main Theorem in the simplest nontrivial case n = 2 n=2. Consider a generic 2 2 -parameter family of vector fields { x ˙ = v ( x, ε) } ε ∈ B 2 \{\dot{x}=v(x,\varepsilon)\}_{\varepsilon\in B^{2}} and suppose that for ε = 0 \varepsilon=0 the vector field x ˙ = v ⁡ ( x, 0) \dot{x}=v(x,0) has a polycycle γ \gamma which consists of two saddles p 1, p 2 p_{1},\ p_{2} and two separatrices connecting γ 1, γ 2 \gamma_{1},\ \gamma_{2} them. Consider a segment Σ \Sigma transversal to, say, γ 1 \gamma_{1} and denote by Δ: Σ ⊃ U → Σ \Delta:\Sigma\supset U\to\Sigma the Poincare return map, which is define on some open set U U in Σ \Sigma. In order to estimate the number of limit cycles bifurcating from the polycycle γ \gamma we need to estimate the number of isolated fixed points #​ { x ∈ U: Δ ⁡ ( x) = x } \#\{x\in U:\ \Delta(x)=x\}.

Using the standard approach we decompose the Poincare map Δ \Delta into a composition of four maps: two local Δ 1 \Delta_{1} and Δ 2 \Delta_{2} in neighborhoods of equilibria p 1 p_{1} and p 2 p_{2} respectively and two semilocal f 1 f_{1} and f 2 f_{2} along connecting separatrices γ 1 \gamma_{1} and γ 2 \gamma_{2} respectively to be defined precisely below (see Fig.2.1). After that we replace the equation Δ ⁡ ( x) = x \Delta(x)=x by the system of equations corresponding to Δ ≡ Δ 2 ∘ f 2 ∘ Δ 1 ∘ f 1 \Delta\equiv\Delta_{2}\circ f_{2}\circ\Delta_{1}\circ f_{1}. To understand properties of local maps Δ i, i = 1, 2 \Delta_{i},\ i=1,2 we use normal forms theory.

[image: Refer to caption] Figure 2.1: Construction of “entrance” and “exit” transversals

### 2.1 Normal forms and a Basic system determining the number of limit cycles

#### 2.1.1 Polynomial Normal forms of local families and Pfaffian Poincare return maps

It turns out that in a small neighborhood of an elementary equilibrium point there exists a finitely differentiable normal coordinates (in the Cartesian product of the phase space and the parameter space), so-called normal forms of an equilibrium point. The list of finitely differentiable normal forms was obtained in [IY1]. The main feature of the list: all normal forms are polynomial and integrable. The smaller is the neighborhood of a normal form, the higher is its smoothness. So smoothness can be chosen arbitrary large. All normal forms are summarized in Table 1 below.

In a small neighborhood of an elementary equilibrium point one can choose two small segments, say Σ − \Sigma^{-} and Σ + \Sigma^{+}, transversal to the vector field for the critical value of parameter and explicitly calculate the Poincare (correspondence) map which maps a point from one segment say Σ − \Sigma^{-} along the corresponding phase curve to a point from the other segment Σ + \Sigma^{+} (see Fig.2.1). For an appropriate choice of segments Σ −, Σ + \Sigma^{-},\Sigma^{+} and coordinate functions x, y x,y in Σ −, Σ + \Sigma^{-},\Sigma^{+} respectively, and a smooth function λ ⁡ ( ε) \lambda(\varepsilon) in the original parameter ε \varepsilon of the family the Poincare return map Δ ε: x → y \Delta_{\varepsilon}:x\to y can be explicitly computed. Moreover, there is a Pfaffian 1-form ω \omega of the form, i.e. 1-form of the form

 | P ⁡ ( x, y, λ ⁡ ( ε)) ​ d ​ x + Q ⁡ ( x, y, λ ⁡ ( ε)) ​ d ​ y = 0 \displaystyle P(x,y,\lambda(\varepsilon))\ dx+\ Q(x,y,\lambda(\varepsilon))\ dy=0 |  | (2.1) |

vanishing on the graph y = Δ ε ​ ( x) y=\Delta_{\varepsilon}(x), where P ⁡ ( x, y, λ ⁡ ( ε)) P(x,y,\lambda(\varepsilon)) and Q ⁡ ( x, y, λ ⁡ ( ε)) Q(x,y,\lambda(\varepsilon)) are polynomials. This was first noticed by Moussu-Roche [MR].

###### Example 2.1.1.

Consider a nonresonant saddle on the plane. There is a normal form which after an appropriate rescaling is given by the equation

 | { x ˙ = λ 1 ​ ( ε) ​ x y ˙ = − λ 2 ​ ( ε) ​ y, \displaystyle\begin{cases}\dot{x}=\lambda_{1}(\varepsilon)x\\ \dot{y}=-\lambda_{2}(\varepsilon)y,\end{cases} |  | (2.2) |

where λ 1 ​ ( ε) \lambda_{1}(\varepsilon) and λ 2 ​ ( ε) \lambda_{2}(\varepsilon) are smooth functions and two transversal “exits”-”entrance” sections are Σ − = { y = 1 }, Σ + = { x = 1 }. \Sigma^{-}=\{y=1\},\quad\Sigma^{+}=\{x=1\}.

[image: Refer to caption] Figure 2.2: Poincare Correspondence maps

Then for λ ⁡ ( ε) = λ 1 ​ ( ε) / λ 2 ​ ( ε) \lambda(\varepsilon)=\lambda_{1}(\varepsilon)/\lambda_{2}(\varepsilon) the function u ⁡ ( t) = x ⁡ ( t) ​ y λ ⁡ ( ε) ​ ( t) u(t)=x(t)y^{\lambda(\varepsilon)}(t) is the first integral. Therefore, if a trajectory starts form ( x ⁡ ( 0), y ⁡ ( 0)) ∈ Σ − (x(0),y(0))\in\Sigma^{-} and ends at ( x ⁡ ( t ∗), y ⁡ ( t ∗)) ∈ Σ + (x(t^{*}),y(t^{*}))\in\Sigma^{+} (see Fig.2.2 S μ S_{\mu} -case), then y λ ⁡ ( ε) ​ ( t ∗) = x ⁡ ( 0) y^{\lambda(\varepsilon)}(t^{*})=x(0) or in the induced on Σ − \Sigma^{-} and Σ + \Sigma^{+} coordinates from ℝ 2 \mathbb{R}^{2} we have y λ ⁡ ( ε) = x y^{\lambda(\varepsilon)}=x. It is easy to see that the 1 1 -form ω = x ​ d ​ y + λ ⁡ ( ε) ​ y ​ d ​ x \omega=x\ dy+\ \lambda(\varepsilon)y\ dx vanishes on the graph y λ ⁡ ( ε) = x y^{\lambda(\varepsilon)}=x. All necessary information about normal forms, Poincare correspondence maps, and corresponding Pfaffian forms is in the Table 1 below. For completeness let’s give necessary definitions of from theory of normal forms.

#### 2.1.2 Definitions and a collection of Normal forms

A local family of planar vector fields is the germ of a map,

 | v: ( ℝ 2, 0) × ( ℝ k, 0) → ( ℝ 2, 0), ( x, y, ε) ↦ v ⁡ ( x, y, ε). v:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to(\mathbb{R}^{2},0),\qquad(x,y,\varepsilon)\mapsto v(x,y,\varepsilon). |  |

A C r C^{r} -smooth conjugacy between two local families v v and w w of the above form is a map

 | H: ( ℝ 2, 0) × ( ℝ k, 0) → ( ℝ 2, 0), ( x, y, ε) ↦ H ⁡ ( x, y, ε), \displaystyle H:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to(\mathbb{R}^{2},0),\qquad(x,y,\varepsilon)\mapsto H(x,y,\varepsilon), |  |

such that

 | H ∗ ​ v ​ ( x, y, ε) = w ⁡ ( H ⁡ ( x, y, ε), ε), \displaystyle\ \ \ H_{*}v(x,y,\varepsilon)=w(H(x,y,\varepsilon),\varepsilon), |  |

where H ∗ H_{*} stands for the Jacobian matrix with respect to the variables x, y x,y. (this definition does not yet allow for reparametrization of a local family). Two families are finitely differentiably equivalent, if for any r < ∞ r<\infty there exists a C r C^{r} -conjugacy between them. The two families v, w v,w are orbitally equivalent, if there exists the germ of a nonvanishing function ϕ: ( ℝ 2, 0) × ( ℝ k, 0) → ℝ 1 \phi:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to\mathbb{R}^{1} such that v v is equivalent to ϕ ⋅ w \phi\cdot w.

To allow for a reparametrization of local families, we say that a family v ⁡ ( ⋅, ε) v(\cdot,\varepsilon) is induced from another family w ⁡ ( ⋅, λ), λ ∈ ( ℝ m, 0) w(\cdot,\lambda),\ \lambda\in(\mathbb{R}^{m},0), if v ⁡ ( ⋅, ε) = w ⁡ ( ⋅, λ ⁡ ( ε)) v(\cdot,\varepsilon)=w(\cdot,\lambda(\varepsilon)), where λ ⁡ ( ε) \lambda(\varepsilon) is the germ of a smooth map ( ℝ k, 0) → ( ℝ m, 0) (\mathbb{R}^{k},0)\to(\mathbb{R}^{m},0). The number of new parameters m m may be different from k k.

Assume that the family w ⁡ ( ⋅, λ) w(\cdot,\lambda) is global (i.e. the expression w ⁡ ( x, y, λ) w(x,y,\lambda) makes sense for all ( x, y, λ) ∈ ℝ m + 2 (x,y,\lambda)\in\mathbb{R}^{m+2}); this happens in particular when w w is polynomial in all its arguments. Restricting the parameters λ \lambda onto a small neighborhood of a certain point ( 0, 0, 𝐜) ∈ ℝ 2 × ℝ m (0,0,{\bf c})\in\mathbb{R}^{2}\times\mathbb{R}^{m}, we obtain a localization of the global family w w, which formally becomes a local family after the parallel translation λ ↦ λ − 𝐜 \lambda\mapsto\lambda-\bf c.

###### Definition 2.1.2.

1. A local family v = v ⁡ ( ⋅, λ) v=v(\cdot,\lambda) is finitely smooth orbital versal unfolding (in short, versal unfolding) of the germ v ⁡ ( ⋅, 0) v(\cdot,0), if any other local family unfolding this germ is finitely differentiable orbitally equivalent to a family induced from v v.

2. A polynomial family w ⁡ ( ⋅, λ) w(\cdot,\lambda), λ ∈ ℝ m \lambda\in\mathbb{R}^{m}, is a global finitely smooth orbital versal unfolding (in short, global versal unfolding) for a certain class of local families of vector fields, if any local family from this class is finitely differentiable orbitally equivalent to a local family induced from some localization of w w.

To investigate a versal unfolding means to investigate at the same time all smooth local finite-parametric families which unfold the same germ v ⁡ ( ⋅, 0) v(\cdot,0). The main result describing versal unfoldings of germs of elementary singularities on the plane, is given by the following

###### Theorem 2.1.3.

[IY1] Suppose that a generic finite-parameter family of smooth vector fields on the plane possesses an elementary singular point for a certain value of the parameters. If this point has at least one hyperbolic sector, than the family is finitely differentiable orbitally equivalent to a family induced from some localization of one of the families given in the second column of Table 1.

Table 1. Unfolding of elementary equilibrium points on the plane.

 |  |  |

Type | Normal forms | Poincare | Pfaffian equations |

 |  | Correspondence maps |  |

 | x ˙ = x, \dot{x}\ =\ x, |  |  |

S 0 S_{0} | y ˙ = − λ ​ y. \dot{y}\ =\ -\lambda y. | y = x λ, y=x^{\lambda}, | x ​ d ​ y − λ ​ y ​ d ​ x = 0 x\ dy\ -\lambda y\ dx\ =0 |

 | λ = λ 0 ∈ ℝ 1 \lambda=\lambda_{0}\in\mathbb{R}^{1} | x > 0, y > 0 x>0,\ y>0 |  |

 | x ˙ = x ⁡ ( n m + P μ ​ ( u, λ)), \dot{x}\ =\ x\ \left(\frac{n}{m}+P_{\mu}(u,\lambda)\right), |  |  |

 | y ˙ = − y. \dot{y}\ =\ -y. |  |  |

S μ S_{\mu} |  | 0 = m ​ log ⁡ y + 0\ =\ m\log y\ + | y ​ P μ ​ ( y n, λ) ​ d ​ x − y\ P_{\mu}(y^{n},\lambda)\ dx\ - |

 | u = u ⁡ ( x, y) = x m ​ y n, u=u(x,y)=x^{m}\ y^{n}, |  |  |

 |  | ∫ x m y n d ​ u u ​ P μ ​ ( u, λ). \int_{x^{m}}^{y^{n}}\frac{du}{uP_{\mu}(u,\lambda)}. | ( n m + P μ ( y n, λ)) × \left(\frac{n}{m}+P_{\mu}(y^{n},\lambda)\right)\times |

 | P μ ​ ( u, λ) = ± u μ ​ ( 1 + λ μ ​ u μ) P_{\mu}(u,\lambda)=\pm u^{\mu}(1+\lambda_{\mu}u^{\mu}) |  |  |

 | + W μ − 1 ​ ( u, λ), +W_{\mu-1}(u,\lambda), | x > 0, y > 0 x>0,\ y>0 | x ​ P μ ​ ( x m, λ) ​ d ​ y = 0 xP_{\mu}(x^{m},\lambda)\ dy=0 |

 | λ = ( λ 1, …, λ μ) \lambda=(\lambda_{1},\dots,\lambda_{\mu}) |  |  |

 | x ˙ = Q μ ​ ( x, λ), \dot{x}\ =\ Q_{\mu}(x,\lambda), |  |  |

 | y ˙ = − y. \dot{y}\ =\ -y. | y = C ⁡ ( λ) ​ x, y\ =\ C(\lambda)x, |  |

D μ c D^{c}_{\mu} |  | C = ∫ − 1 1 d ​ u Q μ ​ ( u, λ), C={\int_{-1}^{1}}\frac{du}{Q_{\mu}(u,\lambda)}, | x ​ d ​ y − y ​ d ​ x = 0 x\ dy\ -y\ dx=0 |

 | Q μ ​ ( x, λ) = ± x μ + 1 ​ ( 1 + λ μ ​ x μ) Q_{\mu}(x,\lambda)\ =\pm x^{\mu+1}(1+\lambda_{\mu}x^{\mu}) | x, y ∈ ℝ 1 x,\ y\ \in\mathbb{R}^{1} |  |

 | + W μ − 1 ​ ( x, λ), +W_{\mu-1}(x,\lambda), |  |  |

 |  | 0 = log ⁡ y + 0=\ \log y\ + |  |

D μ h D^{h}_{\mu} | λ = ( λ 1, …, λ μ) \lambda=(\lambda_{1},\dots,\lambda_{\mu}) | ∫ x 1 d ​ u Q μ ​ ( u, λ) {\int_{x}^{1}}\frac{du}{Q_{\mu}(u,\lambda)} | Q μ ​ ( x, λ) ​ d ​ y − Q_{\mu}(x,\lambda)\ dy\ - |

 |  | y > 0, x ∈ ℝ 1 y>0,\ x\ \in\mathbb{R}^{1} | y ​ d ​ x = 0 y\ dx\ =0 |

 |  |  |

In the first column we use the following notation for elementary equilibria (the subscript indicates the degree of degeneracy):

S 0 S_{0} — Nonresonant saddle;

S μ S_{\mu} — Resonant saddle whose quotient equation (the differential equation for u = x m ​ y n u=x^{m}\ y^{n} below) has the singular point of multiplicity μ + 1 \mu+1 at the origin, μ ≥ 1 \mu\geq 1; if we want to specify explicitly the resonance between the eigenvalues, we use the extended notation S μ ( n: m) S_{\mu}^{(n:m)} assuming that the natural numbers m, n m,n are mutually prime;

D μ D_{\mu} — Degenerate saddlenode of multiplicity μ \mu;

W μ − 1 ​ ( z, λ) = λ 0 + λ 1 ​ z + ⋯ + λ μ − 1 ​ z μ − 1 W_{\mu-1}(z,\lambda)=\lambda_{0}+\lambda_{1}z+\cdots+\lambda_{\mu-1}z^{\mu-1} is a Weierstrass polynomial of degree μ − 1 \mu-1.

Different technical remarks concerning this table see in [IY2] § ​ 1.1 \lx@sectionsign 1.1. We just briefly describe each column.

The second column has the corresponding normal forms. In the third column of the table the Poincare correspondence maps y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) for the polynomial normal forms are given. They are implicitly defined by the equations relating x x to y y, these equations depending explicitly on the parameters λ \lambda and thus implicitly on the original parameters ε \varepsilon. The choice of segments transversal to the phase curves of the family described in Fig. 2.1. The last column has Pfaffian equations vanishing on the graphs of corresponding Poincare maps.

#### 2.1.3 Singular-regular systems determining the number of limit cycles

Recall that for simplicity we consider a 2 2 -parameter family of vector fields { x ˙ = v ( x, ε) } ε ∈ B 2 \{\dot{x}=v(x,\varepsilon)\}_{\varepsilon\in B^{2}} and suppose that for ε = 0 \varepsilon=0 the vector field x ˙ = v ⁡ ( x, 0) \dot{x}=v(x,0) has a polycycle γ \gamma which consists of two saddles p 1, p 2 p_{1},\ p_{2} and two separatrices connecting γ 1, γ 2 \gamma_{1},\ \gamma_{2} them (see Fig.2.2). For each saddle { p j } j = 1, 2 \{p_{j}\}_{j=1,2} there is a neighborhood { U j } j = 1, 2 \{U_{j}\}_{j=1,2} with a C r C^{r} -normal coordinate charts. Consider transversal segments “entrance” Σ j − \Sigma^{-}_{j} and “exit” Σ j + \Sigma^{+}_{j} which are parallel to coordinate axis of the normal chart such that the phase curve γ j − 1 \gamma_{j-1} enters the neighborhood U j U_{j} through Σ j − \Sigma^{-}_{j} and the phase curve γ j \gamma_{j} exists U j U_{j} through Σ j + \Sigma^{+}_{j}. The normal coordinates induce coordinates x j x_{j} and y j y_{j} on Σ j − \Sigma^{-}_{j} and Σ j + \Sigma^{+}_{j} respectively. For some parameter values the corresponding vector field defines the following collection of Poincare correspondence maps:

 | Δ j ​ ( ⋅, ε): x j → y j = Δ j ( x j, ε), j = 1, 2 f j ​ ( ⋅, ε): y j → x j + 1 = f j ( y j, ε), j = 1, 2 ( mod 2), \displaystyle\begin{aligned} \Delta_{j}(\cdot,\varepsilon)&:x_{j}\to y_{j}=\Delta_{j}(x_{j},\varepsilon),\ j=1,2\\ f_{j}(\cdot,\varepsilon)&:y_{j}\to x_{j+1}=f_{j}(y_{j},\varepsilon),\ j=1,2\ \ (\mod 2),\end{aligned} |  | (2.3) |

where Δ j ​ ( ⋅, ε) \Delta_{j}(\cdot,\varepsilon) is a local Poincare map form the “entrance” segment Σ j − \Sigma^{-}_{j} to the “exit” segment Σ j + \Sigma^{+}_{j} and f j ​ ( ⋅, ε) f_{j}(\cdot,\varepsilon) is a semilocal Poincare map along the phase curve γ j \gamma_{j} form the “exit” segment Σ j + \Sigma^{+}_{j} to the “entrance” segment Σ j + 1 − \Sigma^{-}_{j+1}.

Now we decompose the monodromy map (the Poincare first return map) along the polycycle γ \gamma into the chain of two the local singular maps { Δ j ​ ( ⋅, ε) } j = 1, 2 \{\Delta_{j}(\cdot,\varepsilon)\}_{j=1,2} and the semilocal regular maps { f j ​ ( ⋅, ε) } j = 1, 2 \{f_{j}(\cdot,\varepsilon)\}_{j=1,2} of the total length 4 4. Limit cycles correspond to the fixed points of the monodromy. But instead of writing one equation for the fixed points of the monodromy we consider a system of 4 4 equations, which we call the preliminary basic system:

 | { y 1 = Δ 1 ​ ( x 1, ε), x 2 − f 1 ​ ( y 1, ε) = 0, y 2 = Δ 2 ​ ( x 2, ε), x 1 − f 2 ​ ( y 2, ε) = 0. \displaystyle\begin{cases}y_{1}=\Delta_{1}(x_{1},\varepsilon),\\ x_{2}-f_{1}(y_{1},\varepsilon)=0,\\ y_{2}=\Delta_{2}(x_{2},\varepsilon),\\ x_{1}-f_{2}(y_{2},\varepsilon)=0.\end{cases} |  | (2.4) |

Recall that x j x_{j} ’s are C r C^{r} -normal coordinates on Σ j − \Sigma_{j}^{-} and y j y_{j} ’s are C r C^{r} -normal coordinates on Σ j + \Sigma_{j}^{+}. Thus the system involves C r C^{r} -smooth regular functions f j f_{j} ’s and the maps Δ j \Delta_{j} from the list (modulo reparametrization ε → λ ⁡ ( ε) \varepsilon\to\lambda(\varepsilon)), that are essentially singular. The problem now is to estimate the number of small isolated solutions uniformly over all sufficiently small parameter values.

Suppose for ε = ε ∗ \varepsilon=\varepsilon^{*} the system ( 2.4) has the maximal number of isolated solutions. Since each isolated solution of this system corresponds to an isolated solution of the 1-dimensional Poincare return map Δ ⁡ ( x 1, ε) = x 1 \Delta(x_{1},\varepsilon)=x_{1}, one can choose a small δ 1 \delta_{1} so that the number of regular (nondegenerate) solutions of Δ ⁡ ( x 1, ε) = x 1 + δ 1 \Delta(x_{1},\varepsilon)=x_{1}+\delta_{1} bounds the number of isolated solutions to ( 2.4) from above (see Fig. 2.3, c.f. Fig.8 [IY2].)

Recall that a point x ∈ ℝ x\in\mathbb{R} is nondegenerate or regular for the map Δ \Delta if the derivative Δ ′ ​ ( x) ≠ 0 \Delta^{\prime}(x)\neq 0 in the 1 1 -dimensional case and x ∈ ℝ n x\in\mathbb{R}^{n} is a regular point of a smooth map F: ℝ n → ℝ m F:\mathbb{R}^{n}\to\mathbb{R}^{m} if the rank of the linearization d ​ F ​ ( x) dF(x) at x x is maximal. Direct calculation shows that regular solution to Δ ⁡ ( x 1, ε) = x 1 \Delta(x_{1},\varepsilon)=x_{1} (resp. Δ ⁡ ( x 1, ε) = x 1 + δ 1 \Delta(x_{1},\varepsilon)=x_{1}+\delta_{1}) corresponds to a regular solution to the system ( 2.4) (see lemma 3.3 [IY2]).

[image: Refer to caption] Figure 2.3: Isolated and regular solutions

Moreover, if δ 2 \delta_{2} is nonzero and much smaller than δ 1 \delta_{1}, then by the implicit function theorem the number of regular solutions of the system

 | { y 1 = Δ 1 ​ ( x 1, ε), x 2 − f 1 ​ ( y 1, ε) = δ 1, y 2 = Δ 2 ​ ( x 2, ε), x 1 − f 2 ​ ( y 2, ε) = δ 2 \displaystyle\begin{cases}y_{1}=\Delta_{1}(x_{1},\varepsilon),\\ x_{2}-f_{1}(y_{1},\varepsilon)=\delta_{1},\\ y_{2}=\Delta_{2}(x_{2},\varepsilon),\\ x_{1}-f_{2}(y_{2},\varepsilon)=\delta_{2}\end{cases} |  | (2.5) |

is the same as the one for Δ ⁡ ( x 1, ε) = x 1 + δ 1 \Delta(x_{1},\varepsilon)=x_{1}+\delta_{1}. Therefore, it suffices to estimate the number of small regular solutions to the system ( 2.5) provided that 1 ≫ | δ 1 | ≫ | δ 2 | ≥ 0 1\gg|\delta_{1}|\gg|\delta_{2}|\geq 0.

### 2.2 The Khovanski reduction method.

#### 2.2.1 A Mixed Singular-Regular Functional System

The system ( 2.5) is not easy to analyze, because it has the singular functions Δ j \Delta_{j}. The first key idea of the second step of the Main Result [MR], [IY2] is to replace these singular equations in ( 2.5) by the singular functional-Pfaffian equations which have polynomial differentials of the form ( 2.1). As a result we can obtain the mixed functional singular-regular system of the following form

 | { ℱ 1 ​ ( x 1, y 1, ε) = 0 F 1 ​ ( x, y, ε) = δ 1, ℱ 1 ​ ( x 1, y 1, ε) = 0, F 2 ​ ( x, y, ε) = δ 2, d ​ ℱ j ​ ( x j, y j, ε) = P j ​ ( x j, y j, ε) ​ d ​ x j + Q j ​ ( x j, y j, ε) ​ d ​ y j, F j ​ ( x, y, ε) = x j + 1 − f j ​ ( y j, ε), X = ( x 1, y 1, x 2, y 2) ∈ ( ℝ 4, 0), ε ∈ ( ℝ 2, 0), \displaystyle\begin{aligned} &\begin{cases}\mathcal{F}_{1}(x_{1},y_{1},\varepsilon)=0\\ F_{1}(x,y,\varepsilon)=\delta_{1},\\ \mathcal{F}_{1}(x_{1},y_{1},\varepsilon)=0,\\ F_{2}(x,y,\varepsilon)=\delta_{2},\end{cases}\\ d\mathcal{F}_{j}(x_{j},y_{j},\varepsilon)&=P_{j}(x_{j},y_{j},\varepsilon)\ dx_{j}+Q_{j}(x_{j},y_{j},\varepsilon)dy_{j},\\ F_{j}(x,y,\varepsilon)=&\ x_{j+1}-f_{j}(y_{j},\varepsilon),\ \ \ X=(x_{1},y_{1},x_{2},y_{2})\in(\mathbb{R}^{4},0),\ \ \ \varepsilon\in(\mathbb{R}^{2},0),\end{aligned} |  | (2.6) |

where ℱ j \mathcal{F}_{j} are such a functions that their differentials are polynomial 1 1 -forms one of the type from column 4 of Table 1 and 1 ≫ | δ 1 | ≫ | δ 2 | ≥ 0 1\gg|\delta_{1}|\gg|\delta_{2}|\geq 0. In order to simplify considerations we replaced functions eigenfunction λ j ​ ( ε) \lambda_{j}(\varepsilon) (see ( 2.2)) by ε \varepsilon. What we are interested in is the upper estimate for the number of small regular solutions to ( 2.6), uniform over all parameters and all sufficiently small values of δ \delta ’s with 1 ≫ | δ 1 | ≫ | δ 2 | ≥ 0 1\gg|\delta_{1}|\gg|\delta_{2}|\geq 0.

#### 2.2.2 Reduction of the Mixed functional system ( 2.6) to Chain maps P ∘ F P\circ F

Let F = ( F 1, F 2): ℝ 4 → ℝ 2 F=(F_{1},F_{2}):\mathbb{R}^{4}\to\mathbb{R}^{2} be a smooth map formed by functions F 1 F_{1} and F 2 F_{2}. Denote by J m ​ ( ℝ 4, ℝ 2) J^{m}(\mathbb{R}^{4},\mathbb{R}^{2}) the space of k k -jets of maps of ℝ 4 \mathbb{R}^{4} to ℝ 2 \mathbb{R}^{2}. Fix coordinates in the source X = ( x 1, …, x 4) X=(x_{1},\dots,x_{4}) and the target ( δ 1, δ 2) (\delta_{1},\delta_{2}). Then the space J m ​ ( ℝ 4, ℝ 2) J^{m}(\mathbb{R}^{4},\mathbb{R}^{2}) consists of coordinates in the source, the target, and all partial derivatives of F F of order at most k k

 | { ( x 1, …, x 4); ( F 1 ( X), F 2 ( X)); ( ∂ α F i ∂ α 1 x 1 ​ … ​ ∂ α n x 4, ∀ i = 1, 2, α j ≥ 0, such that ∑ j = 1 4 α j ≤ m) }. \displaystyle\begin{aligned} \left\{(x_{1},\dots,x_{4});\ (F_{1}(X),F_{2}(X));\right.\\ \left.\left(\frac{\partial^{\alpha}F_{i}}{\partial^{\alpha_{1}}x_{1}\dots\partial^{\alpha_{n}}x_{4}},\ \forall i=1,2,\ \alpha_{j}\geq 0,\ {\textup{such that}}\ \sum_{j=1}^{4}\alpha_{j}\leq m\right)\right\}.\end{aligned} |  | (2.7) |

We shall call these coordinates on the m m -jets space J m ​ ( ℝ 4, ℝ 2) J^{m}(\mathbb{R}^{4},\mathbb{R}^{2}) the natural coordinates. With this coordinate system the space of m m -jets has a natural linear structure. We also denote by j m ​ F j^{m}F the m m -th jet of the map F F. Denote also by B r ​ ( 0) ⊂ ℝ 4 B_{r}(0)\subset\mathbb{R}^{4} the r r -ball centered at the origin. We call a polynomial map P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} nontrivial if the image P ⁡ ( ℝ N) P(\mathbb{R}^{N}) has a nonempty interior in ℝ n \mathbb{R}^{n}.

Our goal now is to realize Step 2 of our program outlined in section 1.3, i.e. estimate the small number of solutions to ( 2.6) via geometric multiplicity of the chain maps ( 1.12) or prove the following

###### Theorem 2.2.1.

(cf. [Ka1] Thm.10) Suppose that degrees of polynomial 1 1 -forms from ( 2.6) are bounded by some d ∈ ℤ + d\in\mathbb{Z}_{+}. Then for a sufficiently small r > 0 r>0 there exists a set of 3 3 (= the number of singular equations + 1 +1) explicitly computable nontrivial polynomials P k = ( P 1 k, …, P 2 k): J 2 ​ ( ℝ 4, ℝ 2) → ℝ 2 P^{k}=(P_{1}^{k},\dots,P_{2}^{k}):J^{2}(\mathbb{R}^{4},\mathbb{R}^{2})\to\mathbb{R}^{2}, k = 0, 1, 2 k=0,1,2 defined on the space of 2 2 -jets J 2 ​ ( ℝ 4, ℝ 2) J^{2}(\mathbb{R}^{4},\mathbb{R}^{2}) such that for a generic C 3 C^{3} smooth 1 1 1 required smoothness 3 3 = the number of singular equations + 1 +1 map F: ℝ 4 → ℝ 2 F:\mathbb{R}^{4}\to\mathbb{R}^{2} the number of regular solutions to the system ( 2.6) inside the ball B r ​ ( 0) B_{r}(0) is bounded by the number of small regular solutions

 | #{ X ∈ B r ( 0): ( F 1, F 2) ( X) = ( δ 1, δ 2), ( P 1 0, P 2 0) ∘ j 2 F ( X) = ( δ 3, δ 4) } + 1 2 ∑ k = 1, 2 #{ X ∈ B r ( 0): ( F 1, F 2) ( X) = ( δ 1, δ 2), ( P 1 k, P 2 k) ∘ j 2 F ( X) = ( δ 3, δ 4) }, \displaystyle\begin{aligned} \#\{X\in B_{r}(0):(F_{1},F_{2})(X)=(\delta_{1},\delta_{2}),(P_{1}^{0},P_{2}^{0})\circ j^{2}F(X)=(\delta_{3},\delta_{4})\}\\ +\frac{1}{2}\sum_{k=1,2}\#\{X\in B_{r}(0):(F_{1},F_{2})(X)=(\delta_{1},\delta_{2}),(P_{1}^{k},P_{2}^{k})\circ j^{2}F(X)=(\delta_{3},\delta_{4})\},\end{aligned} |  | (2.8) |

where 1 ≫ | δ 1 | ≫ ⋯ ≫ | δ 4 | ≥ 0 1\gg|\delta_{1}|\gg\dots\gg|\delta_{4}|\geq 0 decrease to zero sufficiently fast. The degrees of the polynomials satisfy inequalities deg ⁡ P i k ≤ 2 i ​ ( d + 1) \deg P^{k}_{i}\leq 2^{i}(d+1) for all k k and i i.

###### Remark 2.2.2.

We can not find a direct reference in the book of Khovanskii [Kh2], but this Theorem is in the spirit of the results about perturbations discussed in section 5.2 5.2 of this book. In fact this Theorem is due to Khovanskii.

#### 2.2.3 An Application of Khovanskii Method to the System ( 2.6) or a Proof of Theorem 2.2.1

The method is based on the following version of Rolle’s lemma

###### Lemma 2.2.3.

Consider C 2 C^{2} functions f: S 1 → ℝ 1 f:S^{1}\to\mathbb{R}^{1} on the circle and g: [0, 1] → ℝ 1 g:[0,1]\to\mathbb{R}^{1} on the segment, with a finite number of critical points. Then for any a ∈ ℝ a\in\mathbb{R} and any sufficiently small δ > 0 \delta>0

 | #​ { x: f ⁡ ( x) = a } ≤ #⁡ { x: f ′ ​ ( x) = δ } #​ { x: g ⁡ ( x) = a } ≤ #⁡ { x: g ′ ​ ( x) = δ } + 1. \displaystyle\begin{aligned} \#\{x:\ f(x)=a\}\leq&\#\{x:\ f^{\prime}(x)=\delta\}\\ \#\{x:\ g(x)=a\}\leq&\#\{x:\ g^{\prime}(x)=\delta\}+1.\end{aligned} |  | (2.9) |

Proof: One proves first the formula for δ = 0 \delta=0 using the fact that between any two consecutive preimages there is a point where derivative is zero. Then one uses nondegeneracy of critical points. Q.E.D.

Now using this lemma we shall prove Theorem 2.2.1.

Proof of Theorem 2.2.1: Denote by ρ r ​ ( x) = r − ∑ j x j 2 \rho_{r}(x)=r-\sum_{j}x_{j}^{2} the function which measures distance to the boundary of the r r -ball B r ​ ( 0) B_{r}(0) and vanishes on the boundary ∂ B r ​ ( 0) \partial B_{r}(0). Recall that r r is sufficiently small.

Denote by G 1: ℝ 4 → ℝ 3 G_{1}:\mathbb{R}^{4}\to\mathbb{R}^{3} the map defined by coordinate functions ( ℱ 2, F 1, F 2) (\mathcal{F}_{2},F_{1},F_{2}). Then the system ( 2.6) under investigation becomes the map ( ℱ 1, G 1): ℝ 4 → ℝ 4 (\mathcal{F}_{1},G_{1}):\mathbb{R}^{4}\to\mathbb{R}^{4}, given by its coordinate functions. In terms of this map we need to estimate the number of small preimages of points of the form

 | #⁡ { ( ℱ 1, G 1) − 1 ​ ( 0, 0, δ 1, δ 2) ∩ B r ​ ( 0) }, \#\{(\mathcal{F}_{1},G_{1})^{-1}(0,0,\delta_{1},\delta_{2})\cap B_{r}(0)\}, |  |

where 1 ≫ | δ 1 | ≫ | δ 2 | ≥ 0 1\gg|\delta_{1}|\gg|\delta_{2}|\geq 0.

Let’s estimate the number of small preimages of a point

 | #⁡ { ( ℱ 1, G 1) − 1 ​ ( a 1, a 2, δ 1, δ 2) ∩ B r ​ ( 0) }, \displaystyle\#\{(\mathcal{F}_{1},G_{1})^{-1}(a_{1},a_{2},\delta_{1},\delta_{2})\cap B_{r}(0)\}, |  | (2.10) |

where 1 ≫ | δ 1 | ≫ | δ 2 | ≥ 0 1\gg|\delta_{1}|\gg|\delta_{2}|\geq 0 and a 1, a 2 a_{1},\ a_{2} are arbitrary. Since there is no restriction on a 1, a 2 a_{1},\ a_{2} the number of solutions may only increase.

Step 1. Eliminate one singular equation, say, ℱ 1 = 0 \mathcal{F}_{1}=0 and replace it by two chain-type equations { P 1 i ∘ j 1 ​ F } i = 0, 1 \{P^{i}_{1}\circ j^{1}F\}_{i=0,1} so that for a sufficiently small | δ 2 | ≫ | δ 3 | ≥ 0 |\delta_{2}|\gg|\delta_{3}|\geq 0 the number of small regular preimages

 | #​ { ( G 1, P 1 i ∘ j 1 ​ F ​ ( X)) − 1 ​ ( a 2, δ 1, δ 2, δ 3) ∩ B r ​ ( 0) } i = 0, 1 \displaystyle\#\{(G_{1},P^{i}_{1}\circ j^{1}F(X))^{-1}(a_{2},\delta_{1},\delta_{2},\delta_{3})\cap B_{r}(0)\}_{i=0,1} |  | (2.11) |

is at least the number of small regular preimages of ( 2.10) for any a 1 a_{1}, i.e.

 | #⁡ { X ∈ B r ​ ( 0): ( ℱ 1, G 1) ​ ( X) = ( a 1, a 2, δ 1, δ 2) } ≤ #⁡ { X ∈ B r ​ ( 0): ( G 1, P 1 0 ∘ j 1 ​ F) ​ ( X) = ( a 2, δ 1, δ 2, δ 3) } + 1 2 ​ #​ { X ∈ B r ​ ( 0): ( G 1, ρ r) ​ ( X) = ( a 2, δ 1, δ 2, δ 3) } \displaystyle\begin{aligned} \#\{X\in B_{r}(0):\ (\mathcal{F}_{1},G_{1})(X)=(a_{1},a_{2},\delta_{1},\delta_{2})\}\leq\\ \#\{X\in B_{r}(0):\ (G_{1},P^{0}_{1}\circ j^{1}F)(X)=(a_{2},\delta_{1},\delta_{2},\delta_{3})\}+\\ \frac{1}{2}\#\{X\in B_{r}(0):\ (G_{1},\rho_{r})(X)=(a_{2},\delta_{1},\delta_{2},\delta_{3})\}\end{aligned} |  | (2.12) |

Consider a regular value ( a 2, δ 1, δ 2) ∈ ℝ 3 (a_{2},\delta_{1},\delta_{2})\in\mathbb{R}^{3} of the map G 1 G_{1}. By the Rank Theorem [GG] the level set L ( a 2, δ 1, δ 2) = G 1 − 1 ​ ( a 2, δ 1, δ 2) ∩ B r ​ ( 0) ⊂ B r ​ ( 0) L_{(a_{2},\delta_{1},\delta_{2})}=G_{1}^{-1}(a_{2},\delta_{1},\delta_{2})\cap B_{r}(0)\subset B_{r}(0) is a smooth 1 1 -dimensional manifold in the r r -ball. It consists of a finite number of connected parts either compact — topological circles, denoted by { S i } i ∈ I ⁡ ( a 2, δ 1, δ 2) \{S_{i}\}_{i\in I(a_{2},\delta_{1},\delta_{2})}, or noncompact — curves { L j } j ∈ J ⁡ ( a 2, δ 1, δ 2) \{L_{j}\}_{j\in J(a_{2},\delta_{1},\delta_{2})} reaching the boundary ∂ B r ​ ( 0) \partial B_{r}(0). It is easy to see that

 | #⁡ { X ∈ B r ​ ( 0): ( ℱ 1, G 1) ​ ( X) = ( a 1, a 2, δ 1, δ 2) } = ∑ i ∈ I ⁡ ( a 2, δ 1, δ 2) #⁡ { X ∈ S i: ℱ 1 ​ ( X) = a 1 } + ∑ j ∈ J ⁡ ( a 2, δ 1, δ 2) #⁡ { X ∈ L j: ℱ 1 ​ ( X) = a 1 }. \displaystyle\begin{aligned} \#\{X\in B_{r}(0):\ (\mathcal{F}_{1},G_{1})(X)=(a_{1},a_{2},\delta_{1},\delta_{2})\}=\\ \sum_{i\in I(a_{2},\delta_{1},\delta_{2})}\#\{X\in S_{i}:\ \mathcal{F}_{1}(X)=a_{1}\}+\\ \sum_{j\in J(a_{2},\delta_{1},\delta_{2})}\#\{X\in L_{j}:\ \mathcal{F}_{1}(X)=a_{1}\}.\end{aligned} |  | (2.13) |

[image: Refer to caption] Figure 2.4: Application of Rolle’s lemma

Let us estimate the first sum on the right-hand side. Fix a circle, say, S 1 S_{1}. Restrict the function ℱ 1 \mathcal{F}_{1} to S 1 S_{1} and denote the result by f 1 = ℱ 1 | S 1: S 1 → ℝ f_{1}=\mathcal{F}_{1}|_{S_{1}}:S^{1}\to\mathbb{R} (see Fig.4). We get a function f i f_{i} on the circle. Notice that the condition f 1 ′ ​ ( X) = 0 f_{1}^{\prime}(X)=0 is equivalent to the condition the Jacobian of the map ( ℱ 1, G 1) (\mathcal{F}_{1},G_{1}), denoted by J ℱ 1, G 1 ​ ( X) J_{\mathcal{F}_{1},G_{1}}(X), is zero.

 | f 1 ′ ​ ( X) = 0 ⇔ J ℱ 1, G 1 ​ ( X) = 0 \displaystyle\boxed{f_{1}^{\prime}(X)=0}\qquad\Leftrightarrow\qquad\boxed{J_{\mathcal{F}_{1},G_{1}}(X)=0} |  | (2.14) |

Recall now that the differentials d ℱ j ( X) = P j d x j + Q j d y j, j = 1, 2 d\mathcal{F}_{j}(X)=P_{j}\ dx_{j}+Q_{j}\ dy_{j},\ j=1,2 are polynomial, therefore, we have

 | J ℱ 1, G 1 ( X) = ∗ ( d ℱ 1 ( X) ∧ d ℱ 2 ( X) ∧ d F 1 ( X) ∧ d F 2 ( X)) = det ( ∇ ℱ 1 ​ ( X), ∇ ℱ 2 ​ ( X), ∇ F 1 ​ ( X), ∇ F 2 ​ ( X)) = P 1 0 ∘ j 1 ​ F ​ ( X). \displaystyle\begin{aligned} J_{\mathcal{F}_{1},G_{1}}(X)=*(d\mathcal{F}_{1}(X)\wedge d\mathcal{F}_{2}(X)\wedge dF_{1}(X)\wedge dF_{2}(X))=\\ \det(\nabla\mathcal{F}_{1}(X),\nabla\mathcal{F}_{2}(X),\nabla F_{1}(X),\nabla F_{2}(X))=P^{0}_{1}\circ j^{1}F(X).\end{aligned} |  | (2.15) |

where ∗ *is a natural isomorphism between the space of functions on ℝ 4 \mathbb{R}^{4} and 4 4 -forms and ∇ F ​ ( X) \nabla F(X) is the gradient vector of a function F: ℝ 4 → ℝ F:\mathbb{R}^{4}\to\mathbb{R}. Since deg ⁡ P j, Q j ≤ d \deg P_{j},Q_{j}\leq d, degree of P 1 0 P^{0}_{1} is bounded by 2 ​ ( d + 1) 2(d+1).

Now we can apply Rolle’s lemma 2.2.3 with f = f 1 f=f_{1} and get that for any a 1 a_{1} and a sufficiently small δ 3 ≠ 0 \delta_{3}\neq 0

 | ∑ i #⁡ { X ∈ S i: ℱ 1 ​ ( X) = a 1 } ≤ ∑ i #⁡ { X ∈ S i: J ℱ 1, G 1 ​ ( X) = δ 3 }. \displaystyle\begin{aligned} \sum_{i}\#\{X\in S_{i}:\ \mathcal{F}_{1}(X)=a_{1}\}\leq\sum_{i}\#\{X\in S_{i}:\ J_{\mathcal{F}_{1},G_{1}}(X)=\delta_{3}\}.\end{aligned} |  | (2.16) |

The second sum can be estimated in almost the same way. Instead of using lemma 2.2.3 with f = f i f=f_{i} we need to use lemma 2.2.3 with g = g j = ℱ 1 | L j: [0, 1] → ℝ g=g_{j}=\mathcal{F}_{1}|_{L_{j}}:[0,1]\to\mathbb{R} (see Fig. 2.4). Denote the number of component reaching the boundary | J | |J| by k k. Then

 | ∑ j = 1 k #⁡ { X ∈ L j: ℱ 1 ​ ( X) = a 1 } ≤ ∑ j = 1 k #⁡ { X ∈ L j: J ℱ 1, G 1 ​ ( X) = δ 3 } + k \displaystyle\begin{aligned} \sum_{j=1}^{k}\#\{X\in L_{j}:\ \mathcal{F}_{1}(X)=a_{1}\}\leq\sum_{j=1}^{k}\#\{X\in L_{j}:\ J_{\mathcal{F}_{1},G_{1}}(X)=\delta_{3}\}+k\end{aligned} |  | (2.17) |

In order to find the number of component reaching the boundary notice that each such component intersects the sphere ρ r − 1 ​ ( δ 3) \rho_{r}^{-1}(\delta_{3}) for δ 3 > 0 \delta_{3}>0 in at least two points. So P 1 1 ∘ j 1 ​ F ​ ( X) = ρ r ​ ( X) P^{1}_{1}\circ j^{1}F(X)=\rho_{r}(X) and the second term in inequality ( 2.12) corresponds to the number of noncompact component (the boundary term). This completes the proof of Step 1 or proves ( 2.12).

For i = 0, 1 i=0,1 denote by G 2 i: ℝ 4 → ℝ 3 G^{i}_{2}:\mathbb{R}^{4}\to\mathbb{R}^{3} the maps defined by its coordinate functions ( F 1, F 2, P 1 i ∘ j 1 ​ F) (F_{1},F_{2},P^{i}_{1}\circ j^{1}F). Let’s fix i = 0 i=0 or 1 1.

Step 2. Eliminate the second singular equation ℱ 2 = 0 \mathcal{F}_{2}=0 and replace it by two chain-type equations { P 2 i ∘ j 2 ​ F } i = 0, 1, 2 \{P^{i}_{2}\circ j^{2}F\}_{i=0,1,2} so that for a sufficiently small 0 ≤ | δ 4 | ≪ | δ 3 | 0\leq|\delta_{4}|\ll|\delta_{3}| the number of small regular preimages { ( ℱ 2, G 2 i) − 1 ​ ( a 2, δ 1, δ 2, δ 3) } i = 0, 1 \{(\mathcal{F}_{2},G_{2}^{i})^{-1}(a_{2},\delta_{1},\delta_{2},\delta_{3})\}_{i=0,1} is at least the number of small regular preimages ( G 2 i, P 2 i ∘ j 2 ​ F) − 1 ​ ( δ 1, δ 2, δ 3, δ 4) (G_{2}^{i},P^{i}_{2}\circ j^{2}F)^{-1}(\delta_{1},\delta_{2},\delta_{3},\delta_{4}) for any a 2 a_{2}, i.e.

 | #⁡ { X ∈ B r ​ ( 0): ( ℱ 2, G 2 i) ​ ( X) = ( a 2, δ 1, δ 2, δ 3) } ≤ #⁡ { X ∈ B r ​ ( 0): ( G 2 i, P 2 i ∘ j 2 ​ F) ​ ( X) = ( δ 1, δ 2, δ 3, δ 4) } + 1 2 ​ #​ { X ∈ B r ​ ( 0): ( G 1, ρ r) ​ ( X) = ( δ 1, δ 2, δ 3, δ 4) } \displaystyle\begin{aligned} \#\{X\in B_{r}(0):\ (\mathcal{F}_{2},G_{2}^{i})(X)=(a_{2},\delta_{1},\delta_{2},\delta_{3})\}\leq\\ \#\{X\in B_{r}(0):\ (G_{2}^{i},P^{i}_{2}\circ j^{2}F)(X)=(\delta_{1},\delta_{2},\delta_{3},\delta_{4})\}+\\ \frac{1}{2}\#\{X\in B_{r}(0):\ (G_{1},\rho_{r})(X)=(\delta_{1},\delta_{2},\delta_{3},\delta_{4})\}\end{aligned} |  | (2.18) |

Proof of this inequality is very similar to the proof of step 1. We reproduce a shortened version of it in order to show why the condition | δ 4 | ≪ | δ 3 | |\delta_{4}|\ll|\delta_{3}| it is necessary for the Khovanskii method to work.

Let’s choose a regular value ( δ 1, δ 2, δ 3) (\delta_{1},\delta_{2},\delta_{3}) for the map G 2 i G_{2}^{i} and consider the level set L ( δ 1, δ 2, δ 3) = ( G 2 i) − 1 ​ ( δ 1, δ 2, δ 3) L_{(\delta_{1},\delta_{2},\delta_{3})}=\left(G_{2}^{i}\right)^{-1}(\delta_{1},\delta_{2},\delta_{3}) which is by the rank theorem is a smooth 1 1 -dimensional manifold consisting of a finite number of connected components either compact— topological circles, denoted by { S i } i ∈ I ⁡ ( δ 1, δ 2, δ 3) \{S_{i}\}_{i\in I(\delta_{1},\delta_{2},\delta_{3})}, or noncompact — curves { L j } j ∈ J ⁡ ( δ 1, δ 2, δ 3) \{L_{j}\}_{j\in J(\delta_{1},\delta_{2},\delta_{3})} reaching the boundary ∂ B r ​ ( 0) \partial B_{r}(0).

Then we restrict ℱ 2 \mathcal{F}_{2} to L ( δ 1, δ 2, δ 3) L_{(\delta_{1},\delta_{2},\delta_{3})} and get a finite collection of functions { f i = ℱ 1 | S i: S 1 → ℝ } i ∈ I \{f_{i}=\mathcal{F}_{1}|_{S_{i}}:S^{1}\to\mathbb{R}\}_{i\in I} on circles and { g j = ℱ 1 | L j: [0, 1] → ℝ } j ∈ J \{g_{j}=\mathcal{F}_{1}|_{L_{j}}:[0,1]\to\mathbb{R}\}_{j\in J} on the interval [0, 1] [0,1]. In order to use Rolle’s lemma 2.2.3 we need to compute the condition f i ′ ​ ( X) = 0 f_{i}^{\prime}(X)=0 (resp. g j ′ ​ ( X) = 0 g_{j}^{\prime}(X)=0). This is equivalent to the Jacobian J ℱ 2, G 2 i ​ ( X) J_{\mathcal{F}_{2},G_{2}^{i}}(X) of the map ( ℱ 2, G 2 i) (\mathcal{F}_{2},G_{2}^{i}) being equal to 0 0

 | J ℱ 2, G 2 i ( X) = ​ ( d ℱ 2 ( X) ∧ d F 1 ( X) ∧ d F 2 ( X) ∧ d ( P i 1 ∘ j 1 F) ( X)) = det ( ∇ ℱ 2 ​ ( X), ∇ F 1 ​ ( X), ∇ F 2 ​ ( X), ∇ ( P 1 i ∘ j 1 ​ F) ​ ( X)) = P 2 i ∘ j 2 ​ F ​ ( X). \displaystyle\begin{aligned} J_{\mathcal{F}_{2},G_{2}^{i}}(X)=\*(d\mathcal{F}_{2}(X)\wedge dF_{1}(X)\wedge dF_{2}(X)\wedge d(P^{i}_{1}\circ j^{1}F)(X))=\\ \det(\nabla\mathcal{F}_{2}(X),\nabla F_{1}(X),\nabla F_{2}(X),\nabla(P^{i}_{1}\circ j^{1}F)(X))=P^{i}_{2}\circ j^{2}F(X).\end{aligned} |  | (2.19) |

Since d ​ ℱ 2 ​ ( X) = P 2 ​ d ​ x 2 + Q 2 ​ d ​ y 2 d\mathcal{F}_{2}(X)=P_{2}\ dx_{2}+Q_{2}\ dy_{2} and deg ⁡ P 2, Q 2 ≤ s \deg P_{2},Q_{2}\leq s, degree of P 2 i P^{i}_{2} is bounded by 4 ​ ( s + 1) 4(s+1). An easy calculations show that each time we take a Jacobian of a chain-map P ∘ j k ​ F P\circ j^{k}F its degree at most doubles.

Now we would like to apply Rolle’s lemma 2.2.3 with f = f i f=f_{i} (resp. g = g j g=g_{j}) and substitute a singular equation ℱ 2 \mathcal{F}_{2} by the equation J ℱ 2, G 2 i ​ ( X) = δ 4 J_{\mathcal{F}_{2},G_{2}^{i}}(X)=\delta_{4}. This equation have to be equivalent to the fact that the derivative f ′ ​ ( X) f^{\prime}(X) (resp. g ′ ​ ( X) g^{\prime}(X)) is small or covectors ∇ ℱ 2 ​ ( X), ∇ F 1 ​ ( X), ∇ F 2 ​ ( X), \nabla\mathcal{F}_{2}(X),\nabla F_{1}(X),\nabla F_{2}(X), and ∇ ( P 1 i ∘ j 1 ​ F) ​ ( X) \nabla(P^{i}_{1}\circ j^{1}F)(X) have to be almost linear dependent. However, the determinant ( 2.19) can be almost zero not because gradient vectors are almost linear dependent, but because one of gradient vectors is small. In order to avoid this problem let’s make the following remark: for a fix regular value ( δ 1, δ 2, δ 3) (\delta_{1},\delta_{2},\delta_{3}) the level set L ( δ 1, δ 2, δ 3) L_{(\delta_{1},\delta_{2},\delta_{3})} is a smooth compact 1 1 -dimensional manifold possibly with a boundary and lengths of the gradient vectors ∇ F 1 ​ ( X), ∇ F 2 ​ ( X), \nabla F_{1}(X),\nabla F_{2}(X), and ∇ ( P 1 i ∘ j 1 ​ F) ​ ( X) \nabla(P^{i}_{1}\circ j^{1}F)(X) have to be bounded away from zero. Knowing how far these lengths from zero we can choose δ 4 \delta_{4} of much smaller size to guarantee almost linear dependence of the gradient vectors. This proves inequality ( 2.18).

This argument allow to apply Rolle’s lemma 2.2.3 is the described fashion inductively in any dimension and eliminate arbitrary number of singular Pfaffian equations. This completes the proof of Theorem 2.2.1. See [IK] and [Ka1] for more general treatment.

#### 2.2.4 Geometric Multiplicity of Chain Maps.

Let P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} be a nontrivial vector-polynomial, i.e. the image P ⁡ ( ℝ N) ⊂ ℝ n P(\mathbb{R}^{N})\subset\mathbb{R}^{n} has nonempty interior, B n ⊂ ℝ n B^{n}\subset\mathbb{R}^{n} be a unit ball, and F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} be a generic sufficiently smooth map with N ≥ n N\geq n. We call the composition of a generic smooth map and a nontrivial polynomial

 | P ∘ F: B n → ℝ n \displaystyle P\circ F:B^{n}\to\mathbb{R}^{n} |  | (2.20) |

a chain map. More generally, let P: J n ​ ( B n, ℝ N) → ℝ n P:J^{n}(B^{n},\mathbb{R}^{N})\to\mathbb{R}^{n} be a nontrivial vector-polynomial, defined on the space of m m -jets for some m ∈ ℤ + m\in\mathbb{Z}_{+}. Then a chain map is

 | P ∘ j m ​ F: B n → ℝ n \displaystyle P\circ j^{m}F:B^{n}\to\mathbb{R}^{n} |  | (2.21) |

As the result of application of Theorem 2.2.1 to the system ( 2.6) we need to estimate the number of small regular preimages of a special point of a chain map or geometric multiplicity, defined in ( 1.8), of it. Actually application of Theorem 2.2.1 gives not a generic smooth map, but a jet of a generic smooth map. To simplify discussion we consider the case of a smooth map ( 2.20). The general jet case can be treated using the same method.

The next two lectures are devoted to a proof of Bezout’s Theorem for chain maps. Recall that B r ​ ( 0) ⊂ ℝ n B_{r}(0)\subset\mathbb{R}^{n} denotes the r r -ball centered at the origin.

###### Theorem 2.2.4.

(cf. [Ka1], Thm. 3) Let P = ( P 1, …, P n) P=(P_{1},\dots,P_{n}) be a nontrivial polynomial defined on the space of m m -jets P: J m ​ ( B n, ℝ N) → ℝ n P:J^{m}(B^{n},\mathbb{R}^{N})\to\mathbb{R}^{n} and let F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} be a C k C^{k} smooth mapping, k > m k>m, and N > n N>n. Suppose F F satisfies a transversality condition depending only on P P. Then for a sufficiently small r r to find a geometric multiplicity of the chain map ( 2.20) at 0 0 one can replace j m ​ F j^{m}F by L F, 0, m L_{F,0,m} its linear part at 0 0. Namely,

 | #{ X ∈ B r ( 0): P 1 ∘ j m F ( X) = δ 1, …, P n ∘ j m F ( X) = δ n } = #{ X ∈ B r ( 0): P 1 ∘ L F, 0, m ( X) = δ 1, …, P n ∘ L F, 0, m ( X) = δ n }, \displaystyle\begin{aligned} \#\{X\in B_{r}(0):\ \ P_{1}\circ j^{m}F(X)=\delta_{1},\dots,P_{n}\circ j^{m}F(X)=\delta_{n}\}=\\ \#\{X\in B_{r}(0):\ \ P_{1}\circ L_{F,0,m}(X)=\delta_{1},\dots,P_{n}\circ L_{F,0,m}(X)=\delta_{n}\},\end{aligned} |  | (2.22) |

where 1 ≫ | δ 1 | ≫ ⋯ ≫ | δ n | ≥ 0 1\gg|\delta_{1}|\gg\dots\gg|\delta_{n}|\geq 0.

###### Remark 2.2.5.

By Bezout’s theorem the number of isolated solutions to the equation in the right-hand side of ( 2.22) can be bounded by the product ∏ i = 1 n deg ⁡ P i \prod_{i=1}^{n}\deg P_{i}.

The classical transversality theorem [AGV] says that a generic mapping F F satisfies any ahead given transversality condition and generic mappings form an open dense set in the space of smooth mapping of B n B^{n} to ℝ N \mathbb{R}^{N}. Moreover, a mapping F F with “probability one” satisfies any ahead given transversality condition. For definitions of “probability one” or “prevalence” see [HSY] and [Ka7].

Acknowledgments: I would like to thank Askold Khovanski whose deep insight helped me to make significant simplification of application of Khovanski’s method.

## Chapter 3 Stratifications and Bezout’s Theorem for Chain Maps

In this lecture, first in section 3.1 we describe a geometric picture behind Bezout’s Theorem for chain map (Theorem 2.2.4) formulated in the end of the last lecture. It turns out that the proof of this Theorem reduces to a question about existence of a certain, so-called, a P a_{P} -stratification for the outer part P P of the chain map ( 2.21). Then in section 3.2 we define necessary notions from stratification theory, including a P a_{P} -stratification and discuss the question of existence of a P a_{P} -stratification. In general, it is not always exists as examples from 3.3.1 of Thom and Grinberg show. At the end of this section we state Hironaka’s Theorem on existence of a P a_{P} -stratification for polynomial functions, i.e for polynomial maps with 1 1 -dimensional image, and its extension a Theorem on existence of a P a_{P} -stratification for maps with a mutlidimensional image proven in [Ka1]. Such a Theorem is required for the proof of the Main Result. Finally, in section we present a geometric proof of Hironaka’s Theorem is based on the author’s proof of existence of Whitney’s stratification [Ka4]. A proof of existence of Whitney’s stratification is also outlined.

### 3.1 An Heuristic Description

Consider a chain map P ∘ F: ℝ 2 → ℝ 2 P\circ F:\mathbb{R}^{2}\to\mathbb{R}^{2}, where F: ℝ 2 → ℝ N F:\mathbb{R}^{2}\to\mathbb{R}^{N} is a generic C k C^{k} smooth map, N, k > 2 N,\ k>2 and P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} is a polynomial of degree d d. Fix a small positive r r. We would like to estimate the maximal number of small preimages

 | #{ x ∈ B r ( 0): P 1 ∘ F ( x) = ε, P 2 ∘ F ( x) = 0 } \displaystyle\#\{x\in B_{r}(0):\ P_{1}\circ F(x)=\varepsilon,\ P_{2}\circ F(x)=0\} |  | (3.1) |

for a small enough ε \varepsilon.

To show the idea put N = 3 N=3, P 1 ​ ( x, y, z) = x 2 + y 2 P_{1}(x,y,z)=x^{2}+y^{2}, and P 2 ​ ( x, y, z) = x ​ y P_{2}(x,y,z)=xy. Assume also that F ⁡ ( 0) = 0 F(0)=0. Denote the level set by V ε = { P 1 = ε, P 2 = 0 } V_{\varepsilon}=\{P_{1}=\varepsilon,\ P_{2}=0\}. The level set V ε V_{\varepsilon} for ε > 0 \varepsilon>0 consists of 4 4 parallel lines (see Fig. 3.1).

Notice that in our notation the number of intersections of F ​ ( B r ​ ( 0)) F(B_{r}(0)) with V ε V_{\varepsilon} equals the number of preimages of the point ( ε, 0) (\varepsilon,0) under P ∘ F P\circ F see ( 3.1).

It is easy to see from Fig. 3.1 that if F F is transverse to V 0 V_{0} it is transverse to V ε V_{\varepsilon} for any small ε > 0 \varepsilon>0. Moreover, the number of intersections F ​ ( B r ​ ( 0)) F(B_{r}(0)) with V ε V_{\varepsilon} equals 4 (see the points P 1, …, P 4 P_{1},\dots,P_{4}).

Another way to calculate the same number is as follows. Let us replace F F by its linear part L F L_{F} at zero. Then

 | #{ x ∈ B r ( 0): P 1 ∘ F ( x) = ε, P 2 ∘ F ( x) = 0 } = #{ x ∈ B r ( 0): P 1 ∘ L F ( x) = ε, P 2 ∘ L F ( x) = 0 } \displaystyle\begin{aligned} \#\{x\in B_{r}(0):\ P_{1}\circ F(x)=\varepsilon,\ P_{2}\circ F(x)=0\}=\\ \#\{x\in B_{r}(0):\ P_{1}\circ L_{F}(x)=\varepsilon,\ P_{2}\circ L_{F}(x)=0\}\end{aligned} |  |

and solving this polynomial system also yields 4 4.

[image: Refer to caption] Figure 3.1: The Idealistic Example

The idea behind this picture is the following: Consider an arbitrary N N and a polynomial P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} of degree at most d d and N > 2 N>2. Define the algebraic variety V ε = ( P 1, P 2) − 1 ​ ( ε, 0) V_{\varepsilon}=(P_{1},P_{2})^{-1}(\varepsilon,0) as the level set.

Assume for simplicity that for any small ε ≠ 0 \varepsilon\neq 0 the level set V ε V_{\varepsilon} is a manifold of codimension 2. We shall get rid of this assumption later (see Theorem 3.3.6 b). It turns out that there exists a special partition 𝒱 0 = { V i } i ∈ 𝒜 \mathcal{V}_{0}=\{V_{i}\}_{i\in\mathcal{A}} of V 0 = ⨆ i ∈ 𝒜 V i V_{0}=\bigsqcup_{i\in\mathcal{A}}V_{i} into semialgebraic parts which are attached to their neighbors “regularly” see definition 3.2.3) such that it depends on P P only and satisfies the following condition. We say F F is transverse to a stratified set ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) if F F is transverse to each stratum V i ∈ 𝒱 0 V_{i}\in\mathcal{V}_{0}, then

 | F ​ is transverse to ​ ( V 0, 𝒱 0) ⟹ F ​ is transverse to ​ V ε \boxed{F\ \text{is transverse to}\ (V_{0},\mathcal{V}_{0})}\implies\boxed{F\ \text{is transverse to}\ V_{\varepsilon}}\qquad\  |  | (3.2) |

###### Lemma 3.1.1.

Let B r ​ ( 0) B_{r}(0) be the r r -ball centered at the point 0 ∈ ℝ 2 0\in\mathbb{R}^{2} and let L F, 0 L_{F,0} denote the linearization of F F at the point a a. Under condition ( 3.2), the number of intersections of the image F ​ ( B r ​ ( 0)) F(B_{r}(0)) with V ε V_{\varepsilon} coincides with the number of intersections of the image L F, 0 ​ ( B r ​ ( 0)) L_{F,0}(B_{r}(0)) with V ε V_{\varepsilon}, provided r r is small enough. That is

 | #⁡ { x ∈ B r ​ ( 0): ( P 1, P 2) ∘ F ⁡ ( x) = ( ε, 0) } = #⁡ { x ∈ B r ​ ( 0): ( P 1, P 2) ∘ L F, 0 ​ ( x) = ( ε, 0) }. \displaystyle\begin{aligned} \#\{x\in B_{r}(0):\ (P_{1},P_{2})\circ F(x)=(\varepsilon,0)\}=\\ \#\{x\in B_{r}(0):\ (P_{1},P_{2})\circ L_{F,0}(x)=(\varepsilon,0)\}.\end{aligned} |  | (3.3) |

###### Remark 3.1.2.

The argument below is independent of codimension of V ε V_{\varepsilon}. We only need condition ( 3.2) and the fact that codimension of V ε V_{\varepsilon} coincides with dimension of the preimage of a chain map P ∘ F P\circ F.

Proof: Consider the 1 1 -parameter family of maps F t = t ​ F + ( 1 − t) ​ L F F_{t}=tF+(1-t)L_{F} deforming the linear part of F F into F F. Clearly, F 1 ≡ F F_{1}\equiv F and F 0 ≡ L F F_{0}\equiv L_{F}. Fix a small r > 0 r>0. Since, F F is transverse to V 0 V_{0} at 0 0 all F t F_{t} are transverse to V 0 V_{0} at 0 0. Condition ( 3.2) implies that for all small ε \varepsilon and all t ∈ [0, 1] t\in[0,1] we have F t F_{t} is transverse to V ε V_{\varepsilon}.

Therefore, the number of intersections of F t ​ ( B r ​ ( 0)) F_{t}(B_{r}(0)) with V ε V_{\varepsilon} is independent of t t. Indeed, assume that #⁡ { F t 1 ​ ( B r ​ ( 0)) ∩ V ε } ≠ #⁡ { F t 2 ​ ( B r ​ ( 0)) ∩ V ε } \#\{F_{t_{1}}(B_{r}(0))\cap V_{\varepsilon}\}\neq\#\{F_{t_{2}}(B_{r}(0))\cap V_{\varepsilon}\} for some t 1 < t 2 t_{1}<t_{2}. Then as t 1 t_{1} increases to t 2 t_{2} there is a point t ∗ t^{*} where the number of intersections either drops or jumps. At this point t ∗ t^{*} the condition of transversality of F t ∗ F_{t^{*}} and V ε V_{\varepsilon} must fail. This completes the proof of the lemma. Q.E.D.

### 3.2 Basic definitions of stratified sets, maps, and etc

#### 3.2.1 Stratified sets

A stratification of a set, e.g. an analytic variety, is, roughly, a partition of it into manifolds so that these manifolds fit together “regularly”. Stratification theory was originated by Thom [Th1] and Whitney [Wh] for algebraic and analytic sets. It was one of the key ingredients in Mather’s proof of the topological stability theorem [Ma]. For the history and further applications of stratification theory see [GM] and [PW].

We consider here only the category of real (semi)algebraic sets for simplicity. Theorems on existence of stratifications proven here in the category of semialgebraic sets can be proven for the categories of complex or real (semi)analytic sets using similar methods. Call a subset V ⊂ ℝ N V\subset\mathbb{R}^{N} a semivariety if locally at each point x ∈ ℝ N x\in\mathbb{R}^{N} it is a finite union of subsets defined by equations and inequalities

 | f 1 = ⋯ = f k = 0 g 1 > 0, …, g l > 0 \displaystyle f_{1}=\dots=f_{k}=0\quad g_{1}>0,\dots,g_{l}>0 |  | (3.4) |

where f i f_{i} ’s and g j g_{j} ’s are real algebraic depending on. Semivarieties are closed under Boolean operations.

###### Definition 3.2.1.

(Whitney) Let V i, V j V_{i},V_{j} be disjoint manifolds in ℝ N \mathbb{R}^{N}, dim V j > dim V i \dim V_{j}>\dim V_{i}, and let x ∈ V i ∩ V j ¯ x\in V_{i}\cap\overline{V_{j}}. A triple ( V j, V i, x) (V_{j},V_{i},x) is called a a (resp. b b)- regular if

a a) when a sequence { y n } ⊂ V j \{y_{n}\}\subset V_{j} tends to x x and T y n ​ V j T_{y_{n}}V_{j} tends in the Grassmanian bundle to a subspace τ x \tau_{x} of ℝ N \mathbb{R}^{N}, then T x ​ V i ⊂ τ x T_{x}V_{i}\subset\tau_{x};

b b) when sequences { y n } ⊂ V j \{y_{n}\}\subset V_{j} and { x n } ⊂ V i \{x_{n}\}\subset V_{i} each tends to x x, the unit vector ( x n − y n) / | x n − y n | (x_{n}-y_{n})/|x_{n}-y_{n}| tends to a vector v v, and T y n ​ V j T_{y_{n}}V_{j} tends to τ x \tau_{x}, then v ∈ τ x v\in\tau_{x} 1 1 1 This way of defining b b -regularity is due to Mather [Ma]. Whitney’s definition [Wh] is equivalent to this one provided of a a -regularity.

V j V_{j} is called a a (resp. b b)- regular over V i V_{i} if each triple ( V j, V i, x) (V_{j},V_{i},x) is a a (resp. b b)- regular.

###### Remark 3.2.2.

Since the Grassmanian manifold of dim V j \dim V_{j} -panes in m m -dimensional space is compact, existence of limits in the definition above can be reached by choosing a subsequence { x n k } k ∈ ℤ + \{x_{n_{k}}\}_{k\in\mathbb{Z}_{+}} or { y n k } k ∈ ℤ + \{y_{n_{k}}\}_{k\in\mathbb{Z}_{+}} if necessary.

###### Definition 3.2.3.

(Whitney) Let V V be a semivariety in ℝ N \mathbb{R}^{N}. A disjoint decomposition

 | V = ⨆ i ∈ I V i, V i ∪ V j = ∅ for i ≠ j \displaystyle V=\bigsqcup_{i\in I}V_{i},\quad V_{i}\cup V_{j}=\emptyset\ \ \ \textup{for}\ \ \ i\neq j |  | (3.5) |

into smooth semivarieties 𝒱 = { V i } i ∈ I \mathcal{V}=\{V_{i}\}_{i\in I}, called strata, is called an a a (resp. b b)-regular stratification if

1. each point has a neighborhood intersecting only finitely many strata;

2. the frontier V j ¯ ∖ V j \overline{V_{j}}\setminus V_{j} of each stratum V j V_{j} is a union of other strata ⨆ i ∈ J ⁡ ( i) V i \bigsqcup_{i\in J(i)}V_{i};

3. any triple ( V j, V i, x) (V_{j},V_{i},x) such that x ∈ V i ⊂ V j ¯ x\in V_{i}\subset\overline{V_{j}} is a a (resp. b b)-regular.

The classical example of a stratified algebraic set in ℝ 3 \mathbb{R}^{3} is so-called Whitney umbrella. It is defined as follows

###### Example 3.2.4.

Consider the 2 2 -dimensional algebraic variety in ℝ 3 \mathbb{R}^{3}, defined by

 | V = { ( x, y, z) ∈ ℝ 3: y 2 = z ​ x 2 }. \displaystyle V=\{(x,y,z)\in\mathbb{R}^{3}:\ y^{2}=zx^{2}\}. |  | (3.6) |

[image: Refer to caption] Figure 3.2: Whitney’s umbrella

The first natural partition of V V into smooth parts (strata) is the vertical line V 1 = { x = y = 0 } V_{1}=\{x=y=0\} and the complement V 2 = V ∖ V 1 V_{2}=V\setminus V_{1}. However, V 2 V_{2} does not fit regularly to V 1 V_{1} at the origin. To see that consider the sequence of the form ( x n, 0, 0) ∈ V 2 (x_{n},0,0)\in V_{2} with x n → 0 x_{n}\to 0 as n → ∞ n\to\infty. It is easy to see that after we refine V 1 V_{1} into V 0 ′ = { 0 } V_{0^{\prime}}=\{0\} and V 1 ′ = V 1 ∖ V 0 V_{1^{\prime}}=V_{1}\setminus V_{0} and put V 2 = V 2 ′ V_{2}=V_{2^{\prime}} the partition V = ⨆ i ′ = 1, 2, 3 V i ′ V=\bigsqcup_{i^{\prime}=1,2,3}V_{i^{\prime}} becomes the stratified manifold ( V, { V 0 ′, V 1 ′, V 2 ′ }) (V,\{V_{0^{\prime}},V_{1^{\prime}},V_{2^{\prime}}\}).

###### Theorem 3.2.5.

[Wh], [Th2], [Lo1] For any semivariety V V in ℝ N \mathbb{R}^{N} there is an a a (resp. b b)-regular stratification.

###### Remark 3.2.6.

This Theorem is not true for smooth sets. To see that one can construct a 2 2 -surface in ℝ 2 \mathbb{R}^{2} which looks like a corkscrew.

Existence of stratifications in the complex analytic case was proved by Whitney [Wh]. Later Thom published a sketch of a proof [Th2]. Then Lojasiewicz [Lo1] extended these results to the semianalytic case. Later other proofs were found. In [Hi] Hironaka found a nice proof using his resolution of singularities. J.Bochnak, M. Coste, and M.-F. Roy [BCR] and Z. Denkowska, K. Wachta [DeW] follow the classical route of Whitney [Wh] via the wing lemma. [BCR] uses a Nash wing lemma and [DeW] apply the parameterized Puiseux Theorem of W. Pawlucki [Pa]. T. Wall [Wa] and S. Lojasiewicz, J. Stasica, and K. Wachta [LSW] found proofs which use on Milnor’s curve selection lemma [Mi1]. The latter proof also uses the subanalyticity of the tangent map ( for which an elementary proof was given by Z. Denkowska and K. Wachta [DeW]). In [Ka4] the author gives a geometric proof based on a simple observation that regularity of stratifications is related to uniqueness of the limit of the tangent planes to a bigger stratum as they approach to a smaller stratum. This proof is outlined in section 3.4.1. For a nice exposition of the theory of semianalytic and subanalytic sets see [Lo2].

#### 3.2.2 Stratified maps and a P a_{P} -stratification

First we define a smooth map of a stratified set ( V, 𝒱) (V,\mathcal{V}):

###### Definition 3.2.7.

Let ( V, 𝒱) (V,\mathcal{V}) be stratified in ℝ N \mathbb{R}^{N}, V ⊆ ℝ N V\subseteq\mathbb{R}^{N}, then a map P: V → ℝ n P:V\to\mathbb{R}^{n} is called C 2 C^{2} -smooth if it can be extended to a C 2 C^{2} smooth map of an open set V ⊂ U ⊂ ℝ N V\subset U\subset\mathbb{R}^{N}, denoted by 𝐏: U → ℝ n {\bf P}:U\to\mathbb{R}^{n} whose restriction to V V coincides with P P.

A stratification V = ∪ i V i V=\cup_{i}V_{i} stratifies a smooth map P: V → ℝ n P:V\to\mathbb{R}^{n} if the restriction of P P to a stratum V i V_{i} has a constant rank or rank d ​ P | V i ​ ( x) dP|_{V_{i}}(x) is independent of x ∈ V i x\in V_{i}.

A map G: ℝ n → ℝ N G:\mathbb{R}^{n}\to\mathbb{R}^{N} is called transverse to a stratified set ( V, 𝒱) (V,\mathcal{V}) if G G is transverse to each strata V i ∈ 𝒱 V_{i}\in\mathcal{V}.

###### Example 3.2.8.

With the notations of the example 3.2.4 of the Whitney umbrella consider the Whitney umbrella V V and the projection P = π | V: V → ℝ 2 P=\pi|_{V}:V\to\mathbb{R}^{2} along the z z -coordinate restricted to it. Then the stratification ( V, { V 0 ′, V 1 ′, V 2 ′ }) (V,\{V_{0^{\prime}},V_{1^{\prime}},V_{2^{\prime}}\}) of V V is also an a P a_{P} -stratification of P: V → ℝ 2 P:V\to\mathbb{R}^{2}.

Let V i V_{i} be a stratum of a stratification ( V, 𝒱), 𝒱 = { V i } i ∈ 𝒜 (V,\mathcal{V}),\ \mathcal{V}=\{V_{i}\}_{i\in\mathcal{A}} and a ∈ N a\in N. Denote by L a, i = ( P − 1 ​ ( a) ∩ V i) L_{a,i}=(P^{-1}(a)\cap V_{i}) the level sets of P P in V i V_{i}. By the Rank Theorem [GG], if a stratification ( V, 𝒱) (V,\mathcal{V}) stratifies a smooth map P P, then for each strata V i V_{i} the number d i ​ ( P) = dim V i − rank ​ d ​ P | V i d_{i}(P)=\dim V_{i}-{\textup{rank}}\ dP|_{V_{i}} is well defined and equals to dimension of any nonempty level set L a, i L_{a,i}.

Roughly speaking, a P a_{P} -stratification is a stratification of a map P: V → N P:V\to N such that it is also an a a -stratification of its level sets, i.e. for any sequence of points { b k } ⊂ P ⁡ ( V j) \{b_{k}\}\subset P(V_{j}) converging to a point a ∈ P ⁡ ( V i) a\in P(V_{i}) the corresponding level sets L b k, j = ( P − 1 ​ ( b k) ∩ V j) ⊂ V j L_{b_{k},j}=(P^{-1}(b_{k})\cap V_{j})\subset V_{j} approach the limiting level set L a, i ⊂ V i L_{a,i}\subset V_{i} “regularly”. A precise definition is the following

###### Definition 3.2.9.

Let P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} be a C 2 C^{2} smooth map and let V j V_{j} and V i V_{i} be submanifolds of ℝ N \mathbb{R}^{N} such that V i ⊂ V j ¯ ∖ V j V_{i}\subset\overline{V_{j}}\setminus V_{j} the restrictions P | V j P|_{V_{j}} to V j V_{j} and P | V i P|_{V_{i}} to V i V_{i} have constant ranks. V j V_{j} is called a P a_{P} -regular over V i V_{i} with respect to the map P P at a point x ∈ V i ∩ V j ¯ x\in V_{i}\cap\overline{V_{j}} if for any sequence { x n } ⊂ V j \{x_{n}\}\subset V_{j} converging to x x the sequence of tangent planes to the level sets T n = k ​ e ​ r ​ d ​ P | V j ​ ( x n) T_{n}=ker\ dP|_{V_{j}}(x_{n}) converges in the corresponding Grassmanian manifold of dim k ​ e ​ r ​ d ​ P | V j \dim ker\ dP|_{V_{j}} -dimensional planes to a plane τ \tau and

 | lim k ​ e ​ r ​ d ​ P | V j ​ ( x n) = τ ⊇ k ​ e ​ r ​ d ​ P | V i ​ ( x) \displaystyle\lim ker\ dP|_{V_{j}}(x_{n})=\tau\supseteq ker\ dP|_{V_{i}}(x) |  | (3.7) |

###### Definition 3.2.10.

(Thom) A C 2 C^{2} smooth map P: V → ℝ n P:V\to\mathbb{R}^{n} of a stratifiable set V V to ℝ n \mathbb{R}^{n} is called a P a_{P} -stratifiable if there exists a stratification ( V, 𝒱) (V,\mathcal{V}) such that the following conditions hold:

a) ( V, 𝒱) (V,\mathcal{V}) stratifies the map P P (see definition 3.2.7);

b) for all pairs V j V_{j} and V i V_{i} from 𝒱 \mathcal{V} such that V i ⊆ V j ¯ ∖ V j V_{i}\subseteq\overline{V_{j}}\setminus V_{j} the stratum V j V_{j} is a P a_{P} -regular over the stratum V i V_{i} with respect to P P at point x x for all x ∈ V i ∩ V j ¯ x\in V_{i}\cap\overline{V_{j}}.

Remarks 1. The original definition of a P a_{P} -stratification requires an appropriate stratification of the image too [Ma], but for simplicity we do not require existence of stratification of the image and it turns out to be sufficient for our purposes.

2. With the notations above for an a P a_{P} -stratification to exist we must have d i ​ ( P) ≤ d j ​ ( P) d_{i}(P)\leq d_{j}(P) for each V i ⊆ V j ¯ ∖ V j V_{i}\subseteq\overline{V_{j}}\setminus V_{j}, i.e. nonempty level sets L b, j L_{b,j} inside the bigger stratum V j V_{j} have dimension d j ​ ( P) d_{j}(P) greater or equal to dimension d i ​ ( P) d_{i}(P) of nonempty level sets L a, i L_{a,i} in the smaller stratum V i V_{i}. Otherwise dim k ​ e ​ r ​ d ​ P | V j ​ ( x n) < dim k ​ e ​ r ​ d ​ P | V i ​ ( x) \dim ker\ dP|_{V_{j}}(x_{n})<\dim ker\ dP|_{V_{i}}(x) and condition ( 3.7) can’t be satisfied.

#### 3.2.3 For a P a_{P} -stratifications condition ( 3.2) holds.

An heuristic description given above shows that the key to a proof of Bezout’s Theorem is condition ( 3.2) (lemma 3.1.1). Now we prove that existence of an a P a_{P} -stratification of a polynomial P P is sufficient for condition ( 3.2) to hold.

Let P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} be a nontrivial polynomial, i.e. the image P ⁡ ( ℝ N) P(\mathbb{R}^{N}) has nonempty interior. Denote by V = P 2 − 1 ​ ( 0) V=P_{2}^{-1}(0) and V 0 = ( P 1, P 2) − 1 ​ ( 0) V_{0}=(P_{1},P_{2})^{-1}(0) the level sets. Assume that there exists a stratification ( V, 𝒱) (V,\mathcal{V}) which stratifies the map P | V P|_{V} and such that the zero level set V 0 V_{0} is also stratified by a stratification ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) with V 0 = ⨆ i ∈ 𝒜 0 V i V_{0}=\bigsqcup_{i\in\mathcal{A}_{0}}V_{i}

###### Lemma 3.2.11.

With the above notation if each stratum V j ∈ 𝒱 ∖ 𝒱 0 V_{j}\in\mathcal{V}\setminus\mathcal{V}_{0} is a P a_{P} -regular over each stratum V i ∈ 𝒱 0 V_{i}\in\mathcal{V}_{0} with respect to the polynomial P P, then any C 2 C^{2} smooth map F: ℝ 2 → ℝ N F:\mathbb{R}^{2}\to\mathbb{R}^{N} which is transverse to ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) is also transverse to each level set 𝒱 b, j \mathcal{V}_{b,j} for any small b b and this is equivalent to condition ( 3.2).

Proof: Pick a point x x in V i ⊂ V 0 V_{i}\subset V_{0} and a point y ∈ V i y\in V_{i}. Notice that k ​ e ​ r ​ d ​ P | V i ​ ( x) ker\ dP|_{V_{i}}(x) is the tangent plane to the level set { P − 1 ​ ( P ⁡ ( x)) ∩ V i } \{P^{-1}(P(x))\cap V_{i}\} at the point x x and k ​ e ​ r ​ d ​ P | V j ​ ( y) ker\ dP|_{V_{j}}(y) is the tangent plane to the level set { P − 1 ​ ( P ⁡ ( y)) ∩ V j } \{P^{-1}(P(y))\cap V_{j}\}.

By condition ( 3.7) if a map F: X → ℝ N F:X\to\mathbb{R}^{N} is transverse to k ​ e ​ r ​ d ​ P | V i ​ ( x) ker\ dP|_{V_{i}}(x) at a point x x, then F F is transverse to k ​ e ​ r ​ d ​ P | V j ​ ( y) ker\ dP|_{V_{j}}(y) for any y ∈ V j y\in V_{j} nearby x x. This completes the proof of the lemma. Q.E.D.

### 3.3 Existence of a P a_{P} -stratifications for polynomial maps

#### 3.3.1 Examples of nonexistence due to Thom and Grinberg

Existence of a P a_{P} -stratifications is a nontrivial question. There are some obvious obstacles. For example, let V ⊂ ℝ N V\subset\mathbb{R}^{N} be an algebraic variety and let P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} be a polynomial map. Assume that ( V, 𝒱) (V,\mathcal{V}) stratifies P P. Take two strata V i V_{i} and V j V_{j} so that V j V_{j} lies “over” V i V_{i}, i.e. V i ⊆ V j ¯ ∖ V j V_{i}\subseteq\overline{V_{j}}\setminus V_{j}, then condition ( 3.7) can’t be satisfied if dimension of the level sets d i ​ ( P) d_{i}(P) in the upper stratum V i V_{i} is strictly less than that of d j ​ ( P) d_{j}(P) in the lower stratum V j V_{j}, i.e., dim k ​ e ​ r ​ d ​ P | V i ​ ( y) < dim k ​ e ​ r ​ d ​ P | V j \dim ker\ dP|_{V_{i}}(y)<\dim ker\ dP|_{V_{j}}. In this case a plane k ​ e ​ r ​ d ​ P | V j ​ ( x) ker\ dP|_{V_{j}}(x) of the lower stratum V j V_{j} should belong to a plane τ \tau of smaller dimension by condition ( 3.7), which is impossible. Thom constructed the first example when this happens [GWPL].

###### Example 3.3.1.

(Thom) Consider the vector-polynomial P P of the form

 | P: ( x y) → ( x x ​ y). \displaystyle P:{x\choose y}\to{x\choose xy}. |  | (3.8) |

The line { x = 0 } \{x=0\} is the line of critical points of P P. Outside of the line { x = 0 } \{x=0\} the map P P is a diffeomorphism, therefore, the preimage P − 1 ​ ( a) P^{-1}(a) of any point a ≠ 0 a\neq 0 is 0 0 -dimensional. On the other hand, the preimage of 0 0 is the 1 1 -dimensional line { x = 0 } \{x=0\}. Thus, a P a_{P} -regularity fails to exist.

###### Definition 3.3.2.

Let us call an algebraic set V V rank compatible with respect to a polynomial P P if there exists a stratification ( V, 𝒱) (V,\mathcal{V}) which stratifies P P and for any pair V i V_{i} and V j V_{j} from 𝒱 \mathcal{V} such that V i ⊆ V j ¯ ∖ V j V_{i}\subseteq\overline{V_{j}}\setminus V_{j} dimension of the level sets d i ​ ( P) d_{i}(P) in the lower stratum V i V_{i} does not exceed dimension of the level sets d i ​ ( P) d_{i}(P) in the upper stratum V j V_{j}.

It turns out that even if an algebraic set V V is rank compatible with respect to a polynomial P P, then a P a_{P} -stratification still does not always exist. Let us present an example with this property due to M. Grinberg. It seems that the existence of a counterexample was known before, but we did not find an appropriate reference.

Let V = { ( x, y, z, t) ∈ ℝ 4: x 2 = t 2 ​ y + z } V=\{(x,y,z,t)\in\mathbb{R}^{4}:\ x^{2}=t^{2}y+z\} be the three-dimensional algebraic variety and P: V → ℝ 2 P:V\to\mathbb{R}^{2} be the natural projection to the last two coordinates, i.e. P: ( x, y, z, t) → ( z, t) P:(x,y,z,t)\to(z,t).

###### Lemma 3.3.3.

With the above notations the set V V is rank compatible with the polynomial map P P and does not have an a P a_{P} -stratification.

Proof: Consider a rank stratification of V V. Such a stratification consists of three stratum: V 1 = { x = t = z = 0 }, V 2 = { t = 0, x 2 = z, x ≠ 0 }, V_{1}=\{x=t=z=0\},\ V_{2}=\{t=0,\ x^{2}=z,\ x\neq 0\}, and V 3 = { t ≠ 0 }. V_{3}=\{t\neq 0\}. On each stratum rank P | V i = i − 1 P|_{V_{i}}=i-1. The level sets P − 1 ​ ( t, z) P^{-1}(t,z) are parabolas for t ≠ 0 t\neq 0 and lines for t = 0 t=0.

Show that for each point 𝐚 = ( 0, a, 0, 0) ∈ V 1 {\bf{a}}=(0,a,0,0)\in V_{1} there exists a 1 1 -parameter family of level sets such that at the point 𝐚 {\bf a} the property a P a_{P} -regularity of V 3 V_{3} over V 1 V_{1} fails.

Consider the preimage of the curve { z = − a t 2 } ⊂ ℝ 2 \{z=-at^{2}\}\subset\mathbb{R}^{2}. This is an algebraic variety of the form W a = { x 2 = t 2 ( y − a) } W_{a}=\{x^{2}=t^{2}(y-a)\}. One can see that W a W_{a} is the Whitney umbrella (see Fig. 3.2). The level x 2 = t 0 2 ​ ( y − a) x^{2}=t_{0}^{2}(y-a) is the parabola. As t 0 → 0 t_{0}\to 0 this parabola tends to semiline { x = t = z = 0, y ≥ a } \{x=t=z=0,\ y\geq a\}. At the point 𝐚 ∈ V 1 {\bf{a}}\in V_{1} the property a P a_{P} -regularity of V 3 V_{3} over V 1 V_{1} clearly fails. This completes the proof of the lemma. Q.E.D.

#### 3.3.2 Existence of a P a_{P} -stratifications (Hironaka’s Theorem and its extension)

As we have seen above sometimes a P a_{P} -stratifications exist, sometimes they are not. Let us state a positive result on existence of it.

###### Theorem 3.3.4.

(Hironaka) [Hi] If V ⊂ ℝ N V\subset\mathbb{R}^{N} is a semialgebraic variety and P: ℝ N → ℝ P:\mathbb{R}^{N}\to\mathbb{R} is a polynomial function, then there exists an a P a_{P} -stratification ( V, 𝒱) (V,\mathcal{V}) of V V with respect to P P by semialgebraic strata.

In the next section we give a geometric proof of this result based on the proof of existence of Whitney’s stratifications due to the author [Ka4]. Below we describe an extension on Hironaka’s Theorem to maps with a multidimensional image proven in [Ka1]. This extension is sufficient to prove Bezout’s Theorem for chain maps (Theorem 2.2.4).

The Tarsky-Seidenberg Principle (see e.g. [BCR], [Ja]) For any semialgebraic V V in ℝ N \mathbb{R}^{N} and a polynomial map P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} the image P ⁡ ( V) P(V) is semialgebraic.

Let ℝ N \mathbb{R}^{N} and ℝ n \mathbb{R}^{n} be Eucledian spaces with the fixed coordinate systems x = ( x 1, …, x N) ∈ ℝ N x=(x_{1},\dots,x_{N})\in\mathbb{R}^{N} and a = ( a 1, …, a k) ∈ ℝ n a=(a_{1},\dots,a_{k})\in\mathbb{R}^{n} with N ≥ n N\geq n and a non-trivial vector-polynomial P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n}. Recall that P P is a nontrivial if the image P ⁡ ( ℝ N) P(\mathbb{R}^{N}) has nonempty interior. In what follows we call vector-polynomial by polynomial for brevity.

###### Definition 3.3.5.

Let m ∈ ℤ + m\in\mathbb{Z}_{+} and δ > 0 \delta>0. We call the ( m, δ) (m,\delta) -cone K m, δ n K^{n}_{m,\delta} the following set of points

 | K n m, δ = { a = ( a 1, …, a N) ∈ ℝ N: 0 < | a 1 | < δ, 0 < | a j + 1 | < | a 1 … a j | m for j = 1, …, N − 1 }. \displaystyle\begin{aligned} K^{n}_{m,\delta}=\{a=(a_{1},\dots,a_{N})\in\mathbb{R}^{N}:\ 0<|a_{1}|<\delta,\\ 0<|a_{j+1}|<|a_{1}\dots a_{j}|^{m}\ \text{for}\ j=1,\dots,N-1\}.\end{aligned} |  | (3.9) |

Let m ′ ∈ ℤ + N m^{\prime}\in\mathbb{Z}^{N}_{+}. If m ′ ≥ m m^{\prime}\geq m and δ ′ ≤ δ \delta^{\prime}\leq\delta, then we say that the ( m ′, δ ′) (m^{\prime},\delta^{\prime}) -cone K m ′, δ ′ n K^{n}_{m^{\prime},\delta^{\prime}} is a refinement of the ( m, δ) (m,\delta) -cone K m, δ n K^{n}_{m,\delta}.

Define the following sets

 | V m, δ, P = closure { P − 1 ( K m, δ n) }, V 0, m, P = ∩ δ > 0 V m, δ, P \displaystyle V_{m,\delta,P}=\textup{closure}\{P^{-1}(K^{n}_{m,\delta})\},\ V_{0,m,P}=\cap_{\delta>0}V_{m,\delta,P} |  | (3.10) |

Then one has

###### Theorem 3.3.6.

[Ka1] For any nontrivial polynomial P: ℝ N → ℝ n P:\mathbb{R}^{N}\to\mathbb{R}^{n} there exist an integer m ∈ ℤ + m\in\mathbb{Z}_{+} and a positive δ \delta such that the following conditions hold

a) the set V 0 = V 0, m, P V_{0}=V_{0,m,P} (see ( 3.10)) is a semialgebraic set of codimension at least n n.

b) the set V m, δ, P V_{{m},\delta,P} consists of regular points of P P, i.e. if b ∈ V m, δ, P b\in V_{m,\delta,P}, then the level set P − 1 ​ ( P ​ ( b)) P^{-1}(P(b)) is a manifold of codimension n n.

c) there exists a stratification of V 0 V_{0} by semialgebraic strata ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) satisfying the property: V m, δ, P V_{m,\delta,P} is a P a_{P} -regular over any strata V i ∈ 𝒱 0 V_{i}\in\mathcal{V}_{0} with respect to P P.

###### Remark 3.3.7.

In order to have compatibility condition for the limiting set V m, δ, P V_{m,\delta,P} with regular level sets P − 1 ​ ( a) P^{-1}(a) in the definition of the ( m, δ) (m,\delta) -cone K m, δ n K^{n}_{m,\delta} ( 3.9) it is necessary that range of values (“smallness”) of a j + 1 a_{j+1} depends on all a i a_{i} ’s with i = 1, …, j i=1,\dots,j. Indeed, consider the following

###### Example 3.3.8.

Let x = ( x 1, x 2, x 3) x=(x_{1},x_{2},x_{3}) denote a point in ℝ 3 \mathbb{R}^{3} and P = ( P 1, P 2, P 3): ℝ 3 → ℝ 3 P=(P_{1},P_{2},P_{3}):\mathbb{R}^{3}\to\mathbb{R}^{3} be a polynomial map, given by

 | P 1 ​ ( x) = x 1, P 2 ​ ( x) = x 1 ​ x 2, P 3 ​ ( x) = x 1 ​ x 2 ​ x 3. \displaystyle P_{1}(x)=x_{1},\ P_{2}(x)=x_{1}x_{2},\ P_{3}(x)=x_{1}x_{2}x_{3}. |  | (3.11) |

If definition of the ( m, δ) (m,\delta) -cone is

 | K m, δ 3 = { a = ( a 1, a 2, a 3) ∈ ℝ 3: 0 < | a 1 | < δ, 0 < | a 2 ​ ( resp. ​ 3) | < | a 1 | m }, \displaystyle K^{3}_{m,\delta}=\{a=(a_{1},a_{2},a_{3})\in\mathbb{R}^{3}:\ 0<|a_{1}|<\delta,\ 0<|a_{2(\textup{resp.}3)}|<|a_{1}|^{m}\}, |  | (3.12) |

then the limiting set V m, δ, P V_{m,\delta,P}, defined by ( 3.10), is 1 1 -dimensional for any positive m m. However, all level sets P − 1 ​ ( a) P^{-1}(a) with a 1 ​ a 2 ≠ 0 a_{1}a_{2}\neq 0 are 0 0 -dimensional. In this case compatibility condition 3.3.2 fails.

### 3.4 A Proof of Hironaka’s Theorem on existence of a P a_{P} -stratifications for polynomial functions

In this section we present a geometric proof of Hironaka’s Theorem based on a proof of Whitney’s Theorem 3.2.5 on existence of a a -stratifications due to the author [Ka4]. First, we briefly outline the latter proof and then prove Hironaka’s Theorem following the same path.

#### 3.4.1 An Outline of a Proof of Whitney’s Theorem 3.2.5 on existence of a a -stratifications

The outline given below works to prove b b -stratifications too after a slight modification [Ka4].

A semivariety V V has well-defined dimension, say d ≤ N d\leq N. Denote by V r ​ e ​ g V_{reg} the set of points, where V V is locally a real algebraic submanifold of ℝ N \mathbb{R}^{N} of dimension d d. V r ​ e ​ g V_{reg} is a semivariety, moreover, V s ​ i ​ n ​ g = V ∖ V r ​ e ​ g V_{sing}=V\setminus V_{reg} is a semivariety of positive codimension in V V, i.e. dim V s ​ i ​ n ​ g < dim V \dim V_{sing}<\dim V. In the algebraic case they are not difficult (see e.g. [Mi1]).

Step 1. There is a filtration of V V by semivarieties

 | V 0 ⊂ V 1 ⊂ ⋯ ⊂ V d = V, \displaystyle V^{0}\subset V^{1}\subset\dots\subset V^{d}=V, |  | (3.13) |

where for each k = 1, …, d k=1,\dots,d the set V k ∖ V k − 1 V^{k}\setminus V^{k-1} is a manifold of dimension k k. This is not difficult see e.g. [Mi1]. Indeed, consider V s ​ i ​ n ​ g ⊂ V V_{sing}\subset V, then V ∖ V s ​ i ​ n ​ g V\setminus V_{sing} is a manifold of dimension d d and dim V s ​ i ​ n ​ g < d \dim V_{sing}<d. Inductive application of these arguments completes the proof.

A refinement of a decomposition V = ⨆ i ∈ I V i V=\bigsqcup_{i\in I}V_{i} is a decomposition V = ⨆ i ′ ∈ I ′ V i ′ V=\bigsqcup_{i^{\prime}\in I^{\prime}}V_{i^{\prime}} such that any stratum V j V_{j} of the first decomposition is a union of some strata of the second one, i.e. there is a set I ′ ​ ( j) ⊂ I ′ I^{\prime}(j)\subset I^{\prime} such that V j = ⨆ i ′ ∈ I ′ ​ ( j) V i ′ V_{j}=\bigsqcup_{i^{\prime}\in I^{\prime}(j)}V_{i^{\prime}}.

Step 2. Let V ⊂ ℝ N V\subset\mathbb{R}^{N} be a manifold and W ⊂ V W\subset V be a semivariety. Denote by I ​ n ​ t V ​ ( W) Int_{V}(W) the set of interior points of W W in V V w.r.t. the induced from ℝ N \mathbb{R}^{N} topology. Let V i V_{i} and V j V_{j} be a pair of distinct strata. For each point x ∈ V i ∩ V j ¯ x\in V_{i}\cap\overline{V_{j}} denote by V j c ​ o ​ n, x V_{j}^{con,x} a local connected component of V j V_{j} at x x, i.e. a connected component of intersection of V j V_{j} with a small ball centered at x x and call it essential if the closure of V j c ​ o ​ n, x V_{j}^{con,x} has x x is in the interior, x ∈ I ​ n ​ t V i ​ ( V i ∩ V j c ​ o ​ n, x ¯) x\in Int_{V_{i}}(V_{i}\cap\overline{V^{con,x}_{j}}). Denote by V j e ​ s ​ s, x V_{j}^{ess,x} the union of all local essential components of V j V_{j}. A semialgebraic set V j V_{j} can have only a finitely many local connected components (see e.g. [Mi1]).

###### Theorem 3.4.1.

For any two disjoint strata V j V_{j} and V i V_{i} the set of points

 | S ​ i ​ n ​ g a ​ ( V j, V i) = { x ∈ V i ∩ V j ¯: ( V j e ​ s ​ s, x, V i, x) ​ is not ​ a − regular }, \displaystyle Sing_{a}(V_{j},V_{i})=\{x\in V_{i}\cap\overline{V_{j}}:\ (V_{j}^{ess,x},V_{i},x)\ \textup{is not}\ a-\textup{regular}\}, |  |

is a semivariety in V i V_{i} and dim S ​ i ​ n ​ g a ​ ( V j, V i) < dim V i \dim Sing_{a}(V_{j},V_{i})<\dim V_{i}.

Let us show that this Theorem is sufficient to prove the a a -regular case of Theorem 3.2.5. Consider a decomposition V = ⨆ i ∈ I V i V=\bigsqcup_{i\in I}V_{i} and split the strata into two groups: the first group consists of strata of dimension at least k k and the second group is of the rest. Suppose that each stratum from the first group is a a -regular over each stratum from the second group. Then by definition of a a -regularity any refinement of a stratum from the second group preserves this a a -regularity.

Now apply this refinement inductively. Consider strata in V d ∖ V d − 1 V^{d}\setminus V^{d-1} of dimension d d. Using Theorem 3.4.1 and the result of Lojasiewicz [Lo1] that a frontier of a semivariety has dimension less than a semivariety itself, refine V d − 1 V^{d-1} so that each d d -dimensional stratum is a a -regular over each stratum in V d − 1 V^{d-1}. The above remark shows that any further refinement of the strata in V d − 1 V^{d-1} preserves the a a -regularity of strata from V d ∖ V d − 1 V^{d}\setminus V^{d-1} over it. This reduces the problem of existence of stratification for d d -dimensional semivarieties to the same problem for ( d − 1) (d-1) -dimensional semivarieties. Induction on dimension completes the proof of Theorem 3.2.5.

Our proof is based on the observation that if V i ⊂ V j ¯ V_{i}\subset\overline{V_{j}} are a pair of strata a a -regularity of V j V_{j} over V i V_{i} at x x in V i V_{i} is closely related to whether the limit of tangent planes T y ​ V j T_{y}V_{j} is unique or not as y y from V j V_{j} tends to x x. The rest of the paper is devoted to the proof of Theorem 3.4.1 which consists of two steps. In lemma 3.4.2 we relate a a -regularity with (non)uniqueness of limits of tangent planes T y ​ V j T_{y}V_{j}, then based on it and Rolle’s lemma in lemma 3.4.3 one can prove Theorem 3.4.1.

Let V i V_{i} and V j V_{j} be a pair of distinct strata in ℝ N \mathbb{R}^{N}. Define

 | U n ( V j, V i) = { x ∈ V i ∩ V j ¯: for any ​ V j c ​ o ​ n, x, there exists ​ τ x ⊂ T x ​ ℝ N such that for any { y n } ⊂ V j c ​ o ​ n, x tending to x, T y n V j → τ x }, \displaystyle\begin{aligned} Un(V_{j},V_{i})=\{x\in V_{i}\cap\overline{V_{j}}&:\textup{for any}\ V_{j}^{con,x},\ \textup{there exists}\ \tau_{x}\subset T_{x}\mathbb{R}^{N}\\ \textup{such that for any}\ &\{y_{n}\}\subset V_{j}^{con,x}\ \textup{tending to}\ x,\ \ T_{y_{n}}V_{j}\to\tau_{x}\},\end{aligned} |  | (3.14) |

The proof consists of two lemmas.

###### Lemma 3.4.2.

With the above notations we have

 | S ​ i ​ n ​ g a ​ ( V j, V i) ⊂ V i ∖ U ​ n ​ ( V j, V i). \displaystyle Sing_{a}(V_{j},V_{i})\subset V_{i}\setminus Un(V_{j},V_{i}). |  | (3.15) |

###### Lemma 3.4.3.

With notations above there is a set of strata { V j p } p ∈ ℤ \{V_{j}^{p}\}_{p\in\mathbb{Z}} (resp. { V i p } p ∈ ℤ \{V_{i}^{p}\}_{p\in\mathbb{Z}}) in V j V_{j} (resp. in V i V_{i}) each of positive codimension in V j V_{j} (resp. in V i V_{i}) such that

 | S ​ i ​ n ​ g a ​ ( V j, V i) ⊂ ⋃ p ∈ ℤ S ​ i ​ n ​ g a ​ ( V j p, V i) ​ ⋃ p ∈ ℤ V i p. V i ∖ U ​ n ​ ( V j, V i) ⊂ ⋃ p ∈ ℤ V i ∖ U ​ n ​ ( V j p, V i) \displaystyle\begin{aligned} Sing_{a}(V_{j},V_{i})&\subset\ \ \bigcup_{p\in\mathbb{Z}}Sing_{a}(V_{j}^{p},V_{i})\bigcup_{p\in\mathbb{Z}}V_{i}^{p}.\\ V_{i}\setminus Un(V_{j},V_{i})&\subset\ \ \bigcup_{p\in\mathbb{Z}}V_{i}\setminus Un(V_{j}^{p},V_{i})\end{aligned} |  | (3.16) |

Remarks. 1. Inductive application of this lemma to the right-hand side of the first line of ( 3.16) reduces dimensions of V j p V_{j}^{p} ’s up to dim V i \dim V_{i}.

2. Dimension of the frontier of a semivariety ( S ​ i ​ n ​ g a ​ ( V j p, V i) ⊂ V i ∩ V j p ¯ Sing_{a}(V_{j}^{p},V_{i})\subset V_{i}\cap\overline{V^{p}_{j}}) has dimension strictly smaller that a semivariety ( V j p V_{j}^{p}) itself.

3. By lemma 3.4.2 the set S ​ i ​ n ​ g a ​ ( V j, V i) Sing_{a}(V_{j},V_{i}) is a semivariety. Since a countable union of semivarieties of positive codimension in V i V_{i} contains S ​ i ​ n ​ g a ​ ( V j, V i) Sing_{a}(V_{j},V_{i}) we have S ​ i ​ n ​ g a ​ ( V j, V i) Sing_{a}(V_{j},V_{i}) has a positive codimension in V i V_{i} which proves Theorem 3.4.1.

Since this proves Theorem 3.4.1, as a consequence this proves Theorem 3.2.5 too. We are not going to prove these lemmas, however, we would like to exhibit geometric idea behind the proof of lemma 3.4.3. The section below is devoted to the idea of construction of proper subvarieties in the bigger stratum V j V_{j} approaching to non- a a -regular points S ​ i ​ n ​ g a ​ ( V j, V i) ⊂ V i Sing_{a}(V_{j},V_{i})\subset V_{i}.

#### 3.4.2 Separation of Planes and dimension reduction in lemma 3.4.3

Let τ 0 \tau_{0} and τ 1 \tau_{1} be two distinct orientable k k -dimensional planes in ℝ N \mathbb{R}^{N}. An orientable ( m − k) (m-k) -dimensional plane l l in ℝ N \mathbb{R}^{N} separates τ 0 \tau_{0} and τ 1 \tau_{1} if l l is transverse to τ 0 \tau_{0} and τ 1 \tau_{1} and the orientations induced by τ 0 + l \tau_{0}+l and τ 1 + l \tau_{1}+l in ℝ N \mathbb{R}^{N} are different. Notice that there always exists an open set of orientable ( m − k) (m-k) -planes separating any two distinct orientable k k -plane.

Rolle’s Lemma. If a continuous family of orientable k k -planes { τ t } t ∈ [0, 1] \{\tau_{t}\}_{t\in[0,1]} connects τ 0 \tau_{0} and τ 1 \tau_{1} and an orientable ( m − k) (m-k) -plane l l separates τ 0 \tau_{0} and τ 1 \tau_{1}. Then for some t ∗ ∈ ( 0, 1) t^{*}\in(0,1) transversality of τ t ∗ \tau_{t^{*}} and l l fails.

In what follows we use the transversality theorem [GG] which says : if V ⊂ ℝ N V\subset\mathbb{R}^{N} is a manifold, then almost every plane of dimension k k is transverse to V V.

An Outline of the Proof of lemma 3.4.3 Let x ∈ S ​ i ​ n ​ g a ​ ( V j, V i) x\in Sing_{a}(V_{j},V_{i}), then by lemma 3.4.2 there are sequences { y n ′ }, { y n } ⊂ V j c ​ o ​ n, x \{y^{\prime}_{n}\},\ \{y_{n}\}\subset V_{j}^{con,x} with different limiting tangent planes τ = lim T y n ​ V j \tau=\lim T_{y_{n}}V_{j} and τ ′ = lim T y n ′ ​ V j \tau^{\prime}=\lim T_{y_{n}^{\prime}}V_{j}. Choose an orientation of T y 0 ​ V j T_{y_{0}}V_{j}. By connecting y 0 y_{0} locally with all other points { y n ′ } \{y^{\prime}_{n}\} one can induce an orientation on all other T y n ′ ​ V j T_{y^{\prime}_{n}}V_{j} so that the orientations of τ 0 \tau_{0} and τ 1 \tau_{1} coincide with the orientations of the limits.

Denote dim V j \dim V_{j} by k k. There is an orientable ( N − k) (N-k) -plane l j l_{j} separating τ 0 \tau_{0} and τ 1 \tau_{1} and transverse to V j V_{j} (by the transversality Theorem). Consider the orthogonal projection π l j \pi_{l_{j}} along l j l_{j} onto its orthogonal complement l j ⟂ l_{j}^{\perp}. Denote by p l j, j p_{l_{j},j} its restriction to V j V_{j}, p l j, j = π l j | V j: V j → l j ⟂ p_{l_{j},j}=\pi_{l_{j}}|_{V_{j}}:V_{j}\to l_{j}^{\perp}. Denote by C ​ r ​ i ​ t ​ ( l j, V j) Crit(l_{j},V_{j}) the set of critical points of p l j, j p_{l_{j},j} in V j V_{j} where the rank of p l j, j p_{l_{j},j} is not maximal. Then C ​ r ​ i ​ t ​ ( l j, V j) Crit(l_{j},V_{j}) is a semivariety in V j V_{j} and dim C ​ r ​ i ​ t ​ ( l j, V j) < dim V j \dim Crit(l_{j},V_{j})<\dim V_{j}. Connect two points y n 0 y_{n}^{0} and y n 1 y_{n}^{1} by a curve in V j V_{j}, then T y n 0 ​ V j T_{y_{n}^{0}}V_{j} deformates continuously to T y n 0 ​ V j T_{y_{n}^{0}}V_{j}. Then by Rolle’s Lemma there is a critical point of p l j, j p_{l_{j},j} in V j c ​ o ​ n, x V_{j}^{con,x} arbitrarily close to x x. Thus x ∈ C ​ r ​ i ​ t ​ ( l j, V j) ¯ x\in\overline{Crit(l_{j},V_{j})}.

By the transversality Theorem there is a countable dense set of orientable ( N − k) (N-k) -planes { l j p } p ∈ ℤ + \{l^{p}_{j}\}_{p\in\mathbb{Z}_{+}} transverse to V j V_{j} and separating any two distinct orientable k k -planes τ 0 \tau_{0} and τ 1 \tau_{1}. Therefore, we have that

 | S ​ i ​ n ​ g a ​ ( V j, V i) ⊂ V i ∖ U ​ n ​ ( V j, V i) ⊂ ⋃ p ∈ ℤ + { C ​ r ​ i ​ t ​ ( l j p, V j) ¯ ∖ C ​ r ​ i ​ t ​ ( l j p, V j) }. \displaystyle Sing_{a}(V_{j},V_{i})\subset V_{i}\setminus Un(V_{j},V_{i})\subset\bigcup_{p\in\mathbb{Z}_{+}}\left\{\overline{Crit(l^{p}_{j},V_{j})}\setminus Crit(l^{p}_{j},V_{j})\right\}. |  | (3.17) |

These sets { C r i t ( l j p, V j) = V j p } p ∈ ℤ + \{Crit(l^{p}_{j},V_{j})=V_{j}^{p}\}_{p\in\mathbb{Z}_{+}} are proper subsets in V j V_{j} we are looking for. Using some additional simple argument given in [Ka4] one can complete the proof of lemma 3.4.3. Q.E.D.

#### 3.4.3 A Proof of a P a_{P} -stratifications for polynomials functions

The proof below also consists of two steps.

Step 1. Construct a rank stratification of P. Consider an a a -regular stratification ( V, 𝒱 0) (V,\mathcal{V}^{0}) of V V by semialgebraic strata. Such a stratification always exists by Whitney’s Theorem 3.2.5 proved above. Now we refine a stratification 𝒱 0 \mathcal{V}^{0} to a stratification 𝒱 1 \mathcal{V}^{1} so that 𝒱 1 \mathcal{V}^{1} is a rank stratification of P P or restriction of P P to any stratum V i ∈ 𝒱 1 V_{i}\in\mathcal{V}^{1} is a map of constant rank. Notice that it is sufficient to refine each strata V i ⊂ 𝒱 0 V_{i}\subset\mathcal{V}^{0} so that P P restricted to each strata V i j ⊂ V i V_{i}^{j}\subset V_{i} has a constant rank.

There are two cases: if P ⁡ ( V i) P(V_{i}) is a point, then rank of P | V i P|_{V_{i}} is identically zero and V i V_{i} stays unchanged and if P ⁡ ( V i) P(V_{i}) contains an open set, then denote by Σ i, P ⊂ V i \Sigma_{i,P}\subset V_{i} the set of critical points of P | V i P|_{V_{i}}. By Sard’s lemma for algebraic sets [Mu] the set Σ i, P \Sigma_{i,P} is a semialgebraic set of positive codimension in V i V_{i}. Refine now each Σ i, P \Sigma_{i,P} to be an a a -regular stratification of Σ i, P \Sigma_{i,P}. This is possible by Whitney’s Theorem 3.2.5. Denote such a stratification by ( V, 𝒱 1) (V,\mathcal{V}^{1}). By our construction 𝒱 1 \mathcal{V}^{1} is an a a -regular rank stratification of P | V P|_{V}, i.e. P P has constant rank on each stratum and strata “fit” a a -regularly.

Step 2. It is sufficient to prove the following

###### Theorem 3.4.4.

Let V i, V j ⊂ 𝒱 1 V_{i},V_{j}\subset\mathcal{V}^{1} be two strata in ℝ N \mathbb{R}^{N} and P: ℝ N → ℝ P:\mathbb{R}^{N}\to\mathbb{R} has a constant on each strata V i V_{i} and V j V_{j}. Then the set of singular points

 | S ​ i ​ n ​ g a, P ​ ( V j, V i) = { x ∈ V i ∩ V j ¯: V j ​ is not ​ a P ​ -regular over ​ V i ​ at ​ x ​ w.r.t. ​ P } \displaystyle Sing_{a,P}(V_{j},V_{i})=\{x\in V_{i}\cap\overline{V_{j}}:\ V_{j}\ \textup{is not}\ a_{P}\textup{-regular over}\ V_{i}\ \textup{at}\ x\ \textup{w.r.t.}\ P\} |  |

is semialgebraic and has positive codimension in V i V_{i}.

Inductive refinement arguments from section 3.4.1 along with Theorem 3.4.4 complete the proof of Hironaka’s Theorem 3.3.4. The rest of the section is devoted to a proof of Theorem 3.4.4.

Proof of Theorem 3.4.4: Similarly to the proof of existence of Whitney‘s Theorem 3.2.5 above we define the set with a unique limit of tangent planes to level sets of P P

 | U n P ( V j, V i) = { x ∈ V i: for any V j c ​ o ​ n, x there is τ x, P such that lim y n → x k e r d P | V j c ​ o ​ n, x ( y n) = τ x, P and is unique }. \displaystyle\begin{aligned} Un_{P}(V_{j},V_{i})=\{x\in V_{i}:\textup{for any}\ V_{j}^{con,x}\ \textup{there is}\ \tau_{x,P}\ \textup{such that}\\ \lim_{y_{n}\to x}ker\ dP|_{V_{j}^{con,x}}(y_{n})=\tau_{x,P}\ \textup{ and is unique}\}.\end{aligned} |  | (3.18) |

###### Lemma 3.4.5.

With the above notations U ​ n P ​ ( V j, V i) Un_{P}(V_{j},V_{i}) and S ​ i ​ n ​ g a, P ​ ( V j, V i) Sing_{a,P}(V_{j},V_{i}) are semivarieties and

 | S ​ i ​ n ​ g a, P ​ ( V j, V i) ⊂ V i ∖ U ​ n P ​ ( V j, V i). \displaystyle Sing_{a,P}(V_{j},V_{i})\subset V_{i}\setminus Un_{P}(V_{j},V_{i}). |  | (3.19) |

###### Lemma 3.4.6.

With notations above there is a set of strata { V j p } p ∈ ℤ \{V_{j}^{p}\}_{p\in\mathbb{Z}} (resp. { V i p } p ∈ ℤ \{V_{i}^{p}\}_{p\in\mathbb{Z}}) in V j V_{j} (resp. in V i V_{i}) each of positive codimension in V j V_{j} (resp. in V i V_{i}) such that

 | S ​ i ​ n ​ g a, P ​ ( V j, V i) ⊂ ⋃ p ∈ ℤ S ​ i ​ n ​ g a, P ​ ( V j p, V i) ​ ⋃ p ∈ ℤ V i p. \displaystyle Sing_{a,P}(V_{j},V_{i})\subset\bigcup_{p\in\mathbb{Z}}Sing_{a,P}(V_{j}^{p},V_{i})\bigcup_{p\in\mathbb{Z}}V_{i}^{p}. |  | (3.20) |

###### Remark 3.4.7.

Similarly to the remarks after lemma 3.4.3 this lemma allows to reduce dimension of V j V_{j} ’s and prove that S ​ i ​ n ​ g a, P ​ ( V j, V i) Sing_{a,P}(V_{j},V_{i}) has positive codimension in V i V_{i}. This would prove Theorem 3.4.4 and as a consequence it would prove Theorem 3.3.4. So what is left to prove is lemmas 3.4.5 and 3.4.6.

Proof of lemma 3.4.5: The proof goes by contradiction. Let x ∈ U ​ n P ​ ( V j, V i) ∩ S ​ i ​ n ​ g a, P ​ ( V j, V i) x\in Un_{P}(V_{j},V_{i})\cap Sing_{a,P}(V_{j},V_{i}). Then for any local connected component V x, c ​ o ​ n V^{x,con} and any sequence { y n } ⊂ V x, c ​ o ​ n \{y_{n}\}\subset V^{x,con} there a limiting plane lim k ​ e ​ r ​ d ​ P | V j ​ ( x) = τ x, P \lim ker\ dP|_{V_{j}}(x)=\tau_{x,P}. Moreover, we have k ​ e ​ r ​ d ​ P | V i ​ ( x) ⊄ τ x, P ker\ dP|_{V_{i}}(x)\not\subset\tau_{x,P}. Thus, there is a unit vector v ∈ k ​ e ​ r ​ d ​ P | V i v\in ker\ dP|_{V_{i}} and v ∉ τ x, P v\notin\tau_{x,P}. Contradiction we are going to get is to find a sequence of points { y n } ⊂ V x, c ​ o ​ n \{y_{n}\}\subset V^{x,con} such that lim k ​ e ​ r ​ d ​ P | V j ​ ( y n) = τ ′ ⊃ v \lim ker\ dP|_{V_{j}}(y_{n})=\tau^{\prime}\supset v. The rest of the proof is devoted to construction of such a sequence.

By Theorem on implicit function one can straighten V i V_{i} along with nonempty level sets P − 1 ​ ( a) ∩ V i P^{-1}(a)\cap V_{i}. Then the ray l v ​ ( x) = { y ∈ ℝ N: ( y − x) / | y − x | = v } ⊂ P − 1 ​ ( P ⁡ ( x)) ⊂ V i l_{v}(x)=\{y\in\mathbb{R}^{N}:\ (y-x)/|y-x|=v\}\subset P^{-1}(P(x))\subset V_{i} belongs to the level set P − 1 ​ ( P ​ ( x)) P^{-1}(P(x)). By an extension of Wall [Wa] of Milnor’s curve selection lemma there is a 2 2 -dimensional “wing” V j, v ⊂ V j V_{j,v}\subset V_{j} such that l v ​ ( x) ⊂ V j, v ¯ l_{v}(x)\subset\overline{V_{j,v}}.

By lemma 3.4.3 the set of points with nonunique limit U ​ n ​ ( V j, v, l v ​ ( x)) Un(V_{j,v},l_{v}(x)) is 0 0 -dimensional. Therefore, by lemma 3.4.2 there is a neighborhood U x U_{x} of x x such that any y ∈ U x ∩ l v ​ ( x) y\in U_{x}\cap l_{v}(x), may be distinct from x x, V j, v V_{j,v} is a a -regular over l v ​ ( x) l_{v}(x) at y y and the limit τ y \tau_{y} of tangent planes T y n ​ V j, v T_{y_{n}}V_{j,v} as y → x y\to x is unique. The last two properties imply that τ y \tau_{y} depends continuously on y y as long as the limit t ​ a ​ u y tau_{y} is unique. Therefore, there is a neighborhood U y ⊂ U x ∖ x U_{y}\subset U_{x}\setminus x of y y such that V j, v ∩ U y V_{j,v}\cap U_{y} is a C 1 C^{1} -manifold with a boundary.

Consider a C 1 C^{1} -smooth one-sided chart in U y ∩ V j, v U_{y}\cap V_{j,v} and π L \pi_{L} is the map from U y ∩ V j, v U_{y}\cap V_{j,v} into the 2 2 -dimensional plane ℝ 2 \mathbb{R}^{2}. The image π L ​ ( V i) \pi_{L}(V_{i}) is a line in ℝ 2 \mathbb{R}^{2} and π L ​ ( V j, v) \pi_{L}(V_{j,v}) is a one-sided neighborhood of this line. Using Rolle’s type of argument it is easy to show that for a sequence { y n } ⊂ π L ​ ( V j, v) \{y_{n}\}\subset\pi_{L}(V_{j,v}) from a semineighborhood of π L ​ ( x ′) ∈ ℝ 2 \pi_{L}(x^{\prime})\in\mathbb{R}^{2} such that y n → π L ​ ( y) y_{n}\to\pi_{L}(y) and T y n ′ { π L ∘ P − 1 ( P ( π L − 1 ( y n ′)) } → π L ( v) T_{y_{n}^{\prime}}\{\pi_{L}\circ P^{-1}(P(\pi_{L}^{-1}(y_{n}^{\prime}))\}\to\pi_{L}(v). This implies that lim k ​ e ​ r ​ d ​ P | V j, v ​ ( y n ′) \lim ker\ dP|_{V_{j,v}}(y_{n}^{\prime}) tends to v v, however, V j, v ⊂ V j c ​ o ​ n, x V_{j,v}\subset V^{con,x}_{j}. So v = lim n → ∞ k ​ e ​ r ​ d ​ P | V j, v ​ ( π L − 1 ​ ( y n)) ⊂ v=\lim_{n\to\infty}ker\ dP|_{V_{j,v}}(\pi_{L}^{-1}(y_{n}))\subset
lim n → ∞ k ​ e ​ r ​ d ​ P | V j c ​ o ​ n, x ​ ( π L − 1 ​ ( y n)) = τ \lim_{n\to\infty}ker\ dP|_{V_{j}^{con,x}}(\pi_{L}^{-1}(y_{n}))=\tau. This is a contradiction with v ∉ τ v\notin\tau. Q.E.D.

Proof of lemma 3.4.6: The proof is almost the same as the proof of lemma 3.4.3 outlined above [Ka4]. Q.E.D.

This completes the proof of Theorem 3.4.4 of Hironaka. Q.E.D.

Acknowledgments: I would like to thank my thesis advisor John Mather and David Nadler for stimulating discussions and numerous remarks on mathematics of this lecture.

## Chapter 4 Bifurcation of Spatial Polycycles and Blow-up along the diagonal of the space of Multijets

In this lecture we discuss an essential ingredient of the proof of Theorem 1.2.5 [Ka2] about an estimate on cyclicity of spatial quasielementary polycycles. First, in section 4.1 we motivate appearance of multichain maps ( 2.21) to get an estimate on cyclicity of spatial polycycles. Similarly to the planar case the question of estimating cyclicity of a quasielementary polycycle reduces to estimating geometric multiplicity of a multichain map of the form ( 2.21). To get an estimate on geometric multiplicity of a multichain map ( 2.21) one needs to prove a Bezout’s type Theorem for multichain maps. However, a straightforward way to prove Bezout’s type Theorem for multichain maps faces a typical in singularity theory problem, namely, the problem that transversality fails on the diagonal in the space of multijets (see e.g. [GG] or [Ma]). We shall overcome this problem using a construction of Grigoriev-Yakovenko [GY] of blow-up along the diagonal in the space of multijets and a special Multijet Transversality Theorem [GY]. This construction is described in section 4.2 and its relation to Newton Interpolation Polynomials. In section 4.3 we describe the problem of rate of growth of the number of periodic points from Smooth Dynamical Systems ( see e.g. [AM] and [Sm]) and outline the main result of the author along with Brian Hunt [KH] and [Ka9] in this direction. Finally, in section 4.4 we outline how Newton Interpolation Polynomials can be applied to perturb trajectories and control the number of periodic points of diffeomorphisms.

### 4.1 Multichain maps and spatial polycycles

Consider the simplest example of a polycycle γ \gamma in ℝ 3 \mathbb{R}^{3} consisting of a saddle equilibria p p and a connecting separatrix γ p \gamma_{p} (see Fig.4.1).

[image: Refer to caption] Figure 4.1: A saddle loop polycycle

Let Σ − \Sigma^{-} and Σ + \Sigma^{+} be “entrance” and “exit” transverse sections to γ p \gamma_{p} chosen so that in C r C^{r} -normal coordinates the Poincare return map Δ p \Delta_{p} along the polycycle γ \gamma has a “nice” form. We decompose the Poincare return map Δ \Delta along the polycycle γ \gamma into the composition of a local Poincare map Δ p \Delta_{p} in a neighborhood of p p and a semilocal map f f along γ p \gamma_{p}. Consider 2 2 -cycles bifurcating from γ \gamma. Denote by x 1, x 2 x_{1},x_{2} and y 1, y 2 y_{1},y_{2} the first and the second intersection of each of 2 2 -cycles with Σ + \Sigma^{+} and Σ − \Sigma^{-} respectively. Then the equation determining the number of 2 2 -cycles has the form

 | { y 1 = f ⁡ ( x 1, ε) x 2 = Δ ⁡ ( y 1, ε) y 2 = f ⁡ ( x 2, ε) x 1 = Δ ⁡ ( y 2, ε). \displaystyle\begin{cases}y_{1}=f(x_{1},\varepsilon)\\ x_{2}=\Delta(y_{1},\varepsilon)\\ y_{2}=f(x_{2},\varepsilon)\\ x_{1}=\Delta(y_{2},\varepsilon).\end{cases} |  | (4.1) |

Important that the first and the third equation have the same functional parts. Notice also that each of the equations from ( 4.1) is an equality in ℝ 2 \mathbb{R}^{2} so it consists of two 1 1 -dimensional equalities itself. So the total number of equations in ( 4.1) is 8. Following the strategy of the planar case from section 2.2 lecture 2 we apply the Khovanskii method to the system ( 4.1). Compare this system with the system ( 2.4) or ( 2.6). It is not difficult to see that the result of application of the Khovanskii method give the map of the form

 | P ∘ ( j 7 ​ f, j 7 ​ f): ℝ 8 → ℝ 8. \displaystyle P\circ(j^{7}f,j^{7}f):\mathbb{R}^{8}\to\mathbb{R}^{8}. |  | (4.2) |

To simplify our considerations we redenote the seventh jet j 7 ​ f j^{7}f of f f by a map F F and consider the multichain map

 | P ∘ ( F, F): ℝ 8 → ℝ 8, \displaystyle P\circ(F,F):\mathbb{R}^{8}\to\mathbb{R}^{8}, |  | (4.3) |

where F F is a generic map in a sense that it satisfies any ahead given transversality condition. It is clear that even if F F is generic we can not assume that the 2 2 -tuple ( F, F) (F,F) is a generic map. Simply because the first and the second components are the same. Let’s explain why genericity fails for a 2 2 -tuple mapping by an example.

#### 4.1.1 Genericity (resp. Transversality) fails for 2 2 -tuple mappings!

The Classical Transversality Theorem (e.g. [AGV], [GG]) Let N N and m m be positive integer and M M be a smooth compact manifold in ℝ m \mathbb{R}^{m}. Then for an open dense set of smooth mappings F: ℝ N → ℝ m F:\mathbb{R}^{N}\to\mathbb{R}^{m} we have that F F is transverse to M M. In particular, it means that F − 1 ​ ( M) F^{-1}(M) is a smooth manifold.

Remarks 1. It is an exercise from calculus to construct a set on the unit interval [0, 1] [0,1] which is open dense and has an arbitrary small positive measure. To justify that transversality property is, indeed, generic there is so-called prevalent extension of the Classical Transversality Theorem which says that for a.e. mapping F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} we have that F F is transverse to M M. More exactly, for a generic finite-parameter family of mappings { F ε: B n → ℝ N } ε ∈ B k \{F_{\varepsilon}:B^{n}\to\mathbb{R}^{N}\}_{\varepsilon\in B^{k}} for a.e. parameter value F ε F_{\varepsilon} is transverse to M M. See [HSY] and [Ka7] for more.
2. The fact that transversality of F F to M M implies that F − 1 ​ ( M) F^{-1}(M) is a smooth manifold follows from the Theorem on implicit function (see [AGV], [GG]).

Since a genericity condition on F F we need is that F F has to satisfy a transversality condition, to show impossibility of application of the classical transversality Theorem we give a trivial example when a transversality fails for an open set of 2 2 -tuples ( F, F) (F,F).

###### Example 4.1.1.

In the Classical Transversality Theorem put n = m = 1 n=m=1. Consider the function f: x → x 2 f:x\to x^{2} for x ∈ I = [− 1, 1] x\in I=[-1,1] and the corresponding 2 2 -tuple f × f: I × I → ℝ × ℝ f\times f:I\times I\to\mathbb{R}\times\mathbb{R}, given by f × f: ( x 1, x 2) → ( x 1 2, x 2 2) = ( y 1, y 2) f\times f:(x_{1},x_{2})\to(x_{1}^{2},x_{2}^{2})=(y_{1},y_{2}). Let M = { y 1 = y 2 } ⊂ ℝ × ℝ M=\{y_{1}=y_{2}\}\subset\mathbb{R}\times\mathbb{R} be the diagonal. Then for each f ~ \tilde{f} which is C 1 C^{1} -close to f f the preimage ( f ~, f ~) − 1 ​ ( M) (\tilde{f},\tilde{f})^{-1}(M) is a topological cross (not a manifold). This, in particular, implies that ( f ~, f ~) (\tilde{f},\tilde{f}) is not transverse to M M, otherwise the preimage of a manifold should be a manifold.

To see that notice that a function f ~ \tilde{f} close to f f has to have a local minima x ~ \tilde{x} close to 0 0 and x ~ \tilde{x} is a nondegenerate local minimum, i.e. f ~: x → ε ~ + a ~ ​ ( x − x ~) 2 + H ​ O ​ T ​ ( ( x − x ~) 2) \tilde{f}:x\to\tilde{\varepsilon}+\tilde{a}(x-\tilde{x})^{2}+HOT\left((x-\tilde{x})^{2}\right) with a ~ ≠ 0 \tilde{a}\neq 0. Then f ~ ​ ( x 1) − f ~ ​ ( x 2) = 0 \tilde{f}(x_{1})-\tilde{f}(x_{2})=0 has two intersecting curve of solutions x 1 = x 2 x_{1}=x_{2} and x 1 − x ~ ≈ − ( x 2 − x ~) x_{1}-\tilde{x}\approx-(x_{2}-\tilde{x}) which form a cross. This completes the proof of the claim in the example.

To explain what happens in this example and we derive a general frame due to Grigoriev-Yakovenko [GY].

#### 4.1.2 Blow-up along the diagonal for 2 2 -tuples in the 1 1 -dimensional case

For a smooth function f ~: ℝ → ℝ \tilde{f}:\mathbb{R}\to\mathbb{R} consider the map

 | ( x 1, x 2) ⟶ 𝒟 2 ​ f ~ ( x 1, x 2, f ~ ​ ( x 1), f ~ ​ ( x 2) − f ~ ​ ( x 1) x 2 − x 1) = ( x 1, x 1, u 1, u 2) ⊂ ℝ 4, ( x 1, x 2, u 1, u 2) ⟶ π 2 ( x 1, x 2, u 1, u 1 + u 2 ​ ( x 2 − x 1)). \displaystyle\begin{aligned} \ &(x_{1},x_{2})\stackrel{{\scriptstyle\mathcal{D}_{2}\tilde{f}}}{{\longrightarrow}}\left(x_{1},x_{2},\tilde{f}(x_{1}),\frac{\tilde{f}(x_{2})-\tilde{f}(x_{1})}{x_{2}-x_{1}}\right)=(x_{1},x_{1},u_{1},u_{2})\subset\mathbb{R}^{4},\\ \ &(x_{1},x_{2},u_{1},u_{2})\stackrel{{\scriptstyle\pi_{2}}}{{\longrightarrow}}(x_{1},x_{2},u_{1},u_{1}+u_{2}(x_{2}-x_{1})).\end{aligned} |  | (4.4) |

Direct calculation shows that π 2 ∘ 𝒟 2 ​ f ~ ≡ ( f ~, f ~) \pi_{2}\circ\mathcal{D}_{2}\tilde{f}\equiv(\tilde{f},\tilde{f}). Therefore,

 | ( f ~, f ~) − 1 ​ ( M) = ( 𝒟 2 ​ f ~) − 1 ∘ π 2 − 1 ​ ( M). \displaystyle(\tilde{f},\tilde{f})^{-1}(M)=(\mathcal{D}_{2}\tilde{f})^{-1}\circ\pi_{2}^{-1}(M). |  | (4.5) |

This is incorporated into diagram 1.3 of lecture 1 with n = N = 1 n=N=1. By definition 𝒟 2 ​ ( f): I × I → 𝒟 ​ 𝒟 2 ​ ( I, ℝ) {\mathcal{D}}_{2}(f):I\times I\to{\mathcal{DD}}_{2}(I,\mathbb{R}) is a smooth map, π 2: 𝒟 ​ 𝒟 2 ​ ( I, ℝ) → ℝ \pi_{2}:{\mathcal{DD}}_{2}(I,\mathbb{R})\to\mathbb{R} is an explicitly computable polynomial map, and π 2 ∘ 𝒟 2 ​ ( f) = ( f, f): I × I → ℝ 2 \pi_{2}\circ{\mathcal{D}}_{2}(f)=(f,f):I\times I\to\mathbb{R}^{2}. Notice that outside of the diagonal { x 1 = x 2 } \{x_{1}=x_{2}\} the map π 2 \pi_{2} is one-to-one. However, the preimage of the set π 2 − 1 ​ { x 1 = x 2, f ⁡ ( x 1) = f ⁡ ( x 2) } \pi^{-1}_{2}\{x_{1}=x_{2},\ f(x_{1})=f(x_{2})\} is of dimension 3 3 while the set { x 1 = x 2, f ⁡ ( x 1) = f ⁡ ( x 2) } \{x_{1}=x_{2},\ f(x_{1})=f(x_{2})\} itself is of dimension 2 2. This, in particular, means that π 2 \pi_{2} is a blow-up along the diagonal.

Consider π 2 − 1 ( M) = { u 2 ( x 2 − x 1) = 0 } ⊂ ℝ 4 \pi_{2}^{-1}(M)=\{u_{2}(x_{2}-x_{1})=0\}\subset\mathbb{R}^{4}. This is the union of two intersecting hyperplanes. If the map 𝒟 2 ​ f ~ \mathcal{D}_{2}\tilde{f} is transverse to { u 2 ( x 2 − x 1) = 0 }, \{u_{2}(x_{2}-x_{1})=0\}, then the preimage ( 𝒟 2 f ~) − 1 ( { u 2 ( x 2 − x 1) = 0 }) \left(\mathcal{D}_{2}\tilde{f}\right)^{-1}\left(\{u_{2}(x_{2}-x_{1})=0\}\right) has to be the union of two intersecting curves. It turns out that assumption that 𝒟 2 ​ f ~ \mathcal{D}_{2}\tilde{f} is generic for a generic f ~ \tilde{f} is satisfied or for a generic F ~ \tilde{F} the map 𝒟 2 ​ f ~ \mathcal{D}_{2}\tilde{f} is transverse to both hyperplanes of { u 2 ( x 2 − x 1) = 0 } \{u_{2}(x_{2}-x_{1})=0\}. Let’s justify that.

A “Proof” of the Classical Transversality Theorem. (see e.g. [AGV], [GG]) Transversality is an open property, i.e. if F F is transverse to M M, then for all F ~ \tilde{F} sufficiently close to F F we have F ~ \tilde{F} is transverse to M M too. So it is sufficient to show that by an arbitrary small perturbation of any mapping F: ℝ N → ℝ m F:\mathbb{R}^{N}\to\mathbb{R}^{m} one can reach transversality to a compact manifold M M. Let’s prove it now.

Consider a smooth mapping F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N}. Include this mapping into the m m -parameter family 𝐅: ℝ n × ℝ N → ℝ n × ℝ N {\bf F}:\mathbb{R}^{n}\times\mathbb{R}^{N}\to\mathbb{R}^{n}\times\mathbb{R}^{N}, given by 𝐅 ⁡ ( x, ε) = ( x, F ⁡ ( x) + ε) {\bf F}(x,\varepsilon)=(x,F(x)+\varepsilon). The determinant of the linearization of the mapping (the Jacobian) J 𝐅 ​ ( x, ε) J_{\bf F}(x,\varepsilon) is constant and identically equals 1 1. Therefore, 𝐅 {\bf F} is a diffeomorphism and M F = 𝐅 − 1 ​ ( ℝ n × M) M_{F}={\bf F}^{-1}(\mathbb{R}^{n}\times M) is a manifold in the preimage ℝ n × ℝ N \mathbb{R}^{n}\times\mathbb{R}^{N}.

Fact. If ε \varepsilon is a regular point of the projection π M, F = π | M F: ℝ n × ℝ N → ℝ N \pi_{M,F}=\pi|_{M_{F}}:\mathbb{R}^{n}\times\mathbb{R}^{N}\to\mathbb{R}^{N} along the x x -coordinate, restricted to M F M_{F}, then F ε = F ⁡ ( x) + ε F_{\varepsilon}=F(x)+\varepsilon is transverse to M M.

This follows from the implicit function theorem.

Sard’s Lemma. (e.g. [Mi2]) A.e. ε ∈ ℝ N \varepsilon\in\mathbb{R}^{N} value is regular for the projection map π M, F \pi_{M,F}.

Thus, one can choose a regular value ε \varepsilon arbitrary close to 0 0. For such an ε \varepsilon the mapping F ε F_{\varepsilon} is transverse to M M. This completes the proof of the Classical Transversality Theorem. Q.E.D.

Now we are ready to state the main result of this section

#### 4.1.3 Multijet Transversality Theorem due to Grigoriev-Yakovenko

###### Theorem 4.1.2.

[GY] Let M ⊂ ℝ N × ℝ N M\subset\mathbb{R}^{N}\times\mathbb{R}^{N} be an algebraic manifold (or variety) and B n ⊂ ℝ n B^{n}\subset\mathbb{R}^{n} be a unit ball. Then for an open dense set of smooth mappings F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} the set ( F × F) − 1 ​ ( M) \left(F\times F\right)^{-1}(M) is stratified.

Moreover, let k ∈ ℤ + k\in\mathbb{Z}_{+} and M ⊂ ℝ N × ⋯ × ℝ N M\subset\mathbb{R}^{N}\times\dots\times\mathbb{R}^{N} ( k k times) be an algebraic manifold (or variety). Then for an open dense set of smooth mappings F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} the set ( F × ⋯ × F) − 1 ​ ( M) \left(F\times\dots\times F\right)^{-1}(M), with k k repetitions, is stratified.

Moreover, let n, k ∈ ℤ + n,\ k\in\mathbb{Z}_{+} and M ⊂ J m ​ ( B n, ℝ N) × ⋯ × J m ​ ( B n, ℝ N) M\subset J^{m}(B^{n},\mathbb{R}^{N})\times\dots\times J^{m}(B^{n},\mathbb{R}^{N}) ( k k times) be an algebraic manifold (or variety). Then for an open dense set of smooth mappings F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} the set ( F × ⋯ × F) − 1 ​ ( M) \left(F\times\dots\times F\right)^{-1}(M), with k k repetitions, is stratified.

A Proof of the Theorem for the model example n = m = 1 n=m=1 and k = 2 k=2. Consider the map 𝒟 2 ​ ( F): ( x 1, x 2, ε 1, ε 2) ↦ ( x 1, x 2, u 1, u 2), {\mathcal{D}}_{2}(F):(x_{1},x_{2},\varepsilon_{1},\varepsilon_{2})\mapsto(x_{1},x_{2},u_{1},u_{2}), defined by the formula ( 4.4). Direct calculations show that the determinant of the linearization (the Jacobian) J 𝒟 2 ​ ( F) ​ ( x 1, x 2, ε 1, ε 2) ≡ 1 J_{{\mathcal{D}}_{2}(F)}(x_{1},x_{2},\varepsilon_{1},\varepsilon_{2})\equiv 1 and is formed by an upper triangular matrix with units on the diagonal. Since, 𝒟 2 ​ ( F) {\mathcal{D}}_{2}(F) is a diffeomorphism one can apply arguments of the proof of the Classical Transversality Theorem given above. Q.E.D.

A Proof of the Theorem in the general case follows along the same lines. The main difficulty is to construct diagram 1.3 in the general case. This is the subject of the next subsection.

###### Corollary 4.1.3.

For an open dense set of smooth functions F: I → ℝ F:I\to\mathbb{R} the preimage ( F, F) − 1 ​ ( M) (F,F)^{-1}(M) is a 1 1 -dimensional stratified manifold, i.e. locally finite union of points and curves.

### 4.2 Newton Interpolation Polynomials and Blow-up Along the diagonal in the space of Multijets

This section is devoted to description of Grigoriev-Yakovenko construction of Blow-up along the diagonal in the space of Multijets in the general case. Let F: B n → ℝ N F:B^{n}\to\mathbb{R}^{N} be a smooth map of a unit ball B n ⊂ ℝ n B^{n}\subset\mathbb{R}^{n}, j m ​ F: B n → J m ​ ( B n, ℝ N) j^{m}F:B^{n}\to J^{m}(B^{n},\mathbb{R}^{N}) be an m m -th jet of F F, and 𝒥 m, k ​ ( B n, ℝ N) = J m ​ ( B n, ℝ N) × ⋯ × J m ​ ( B n, ℝ N) {\mathcal{J}}^{m,k}(B^{n},\mathbb{R}^{N})=J^{m}(B^{n},\mathbb{R}^{N})\times\dots\times J^{m}(B^{n},\mathbb{R}^{N}) ( k k repetitions) be the space of k k -tuple m m -jets. Denote k k -tuple of m m -jet of a map F: ℝ N → ℝ m F:\mathbb{R}^{N}\to\mathbb{R}^{m} by 𝒥 m, k ​ F ​ ( x 1, …, x k) = ( j m ​ F ​ ( x 1), …, j m ​ F ​ ( x k)) {\mathcal{J}}^{m,k}F(x_{1},\dots,x_{k})=(j^{m}F(x_{1}),\dots,j^{m}F(x_{k})). The goal of this section is to define entries of an extension of diagram 1.3: The, so-called, space of divided differences 𝒟 ​ 𝒟 k m ​ ( B n, ℝ N) {\mathcal{DD}}_{k}^{m}(B^{n},\mathbb{R}^{N}), the Newton map π k m: 𝒟 ​ 𝒟 k m ​ ( B n, ℝ N) → 𝒥 m, k ​ ( B n, ℝ N) \pi^{m}_{k}:{\mathcal{DD}}_{k}^{m}(B^{n},\mathbb{R}^{N})\to{\mathcal{J}}^{m,k}(B^{n},\mathbb{R}^{N}), 𝒟 k m ​ ( F): B n × ⋯ × B n ⏟ k ​ repetitions → 𝒟 ​ 𝒟 k m ​ ( B n, ℝ N) {\mathcal{D}}_{k}^{m}(F):\underbrace{B^{n}\times\dots\times B^{n}}_{k\ \textup{repetitions}}\to{\mathcal{DD}}_{k}^{m}(B^{n},\mathbb{R}^{N}). We use the exposition from [GY].

[image: Refer to caption] Figure 4.2: Polynomial blow-up of the multijet space

#### 4.2.1 Divided Differences

In order to extend the above construction we need to define so called divided differences. Let g: ℝ → ℝ g:\mathbb{R}\to\mathbb{R} be a sufficiently smooth function of one real variables.

###### Definition 4.2.1.

The first order divided difference of g g is defined as

 | Δ ​ g ​ ( x 1, x 2) = g ⁡ ( x 2) − g ⁡ ( x 1) x 2 − x 1 \displaystyle\begin{aligned} \Delta g(x_{1},x_{2})=\frac{g(x_{2})-g(x_{1})}{x_{2}-x_{1}}\end{aligned} |  | (4.6) |

for x 2 ≠ x 1 x_{2}\neq x_{1} and extended by its limit value as g ′ ​ ( x) g^{\prime}(x) for x = x 2 = x 1 x=x_{2}=x_{1}. Clearly, if g g is a C r C^{r} -smooth function, then Δ ​ g \Delta g is at least a C r − 1 C^{r-1} -smooth function of its arguments.

Iterating this construction we define divided differences of the s s -th order for any s ∈ ℤ + s\in\mathbb{Z}_{+} as

 | Δ s ​ g ​ ( x 1, …, x s + 1) = Δ s − 1 ​ g ​ ( x 1, …, x s − 1, x s + 1) − Δ s − 1 ​ g ​ ( x 1, …, x s − 1, x s) x s + 1 − x s \displaystyle\Delta^{s}g(x_{1},\dots,x_{s+1})=\frac{\Delta^{s-1}g(x_{1},\dots,x_{s-1},x_{s+1})-\Delta^{s-1}g(x_{1},\dots,x_{s-1},x_{s})}{x_{s+1}-x_{s}} |  |

for x s + 1 ≠ x s x_{s+1}\neq x_{s} and extended by its limit value as ∂ Δ s − 1 ​ g ∂ x s ​ ( x) \frac{\partial\Delta^{s-1}g}{\partial x_{s}}(x) for x = x s + 1 = x s x=x_{s+1}=x_{s}. Clearly, if g g is a C r C^{r} -smooth function, then Δ ​ g \Delta g is at least a C r − s C^{r-s} -smooth function of its arguments.

Notice that Δ s \Delta^{s} is linear as a function of g g, and one can show that it is a symmetric function of x 1, …, x s + 1 x_{1},\ldots,x_{s+1}; in fact, by induction it follows that

 | Δ s ​ g ​ ( x 1, …, x s) = ∑ i = 1 s + 1 g ⁡ ( x i) ∏ j ≠ i ( x i − x j) \displaystyle\Delta^{s}g(x_{1},\dots,x_{s})=\sum_{i=1}^{s+1}\frac{g(x_{i})}{\prod_{j\neq i}(x_{i}-x_{j})} |  | (4.7) |

Another identity that is proved by induction will be more important for us, namely

 | Δ s ​ x l ​ ( x 1, …, x s + 1) = p l, s ​ ( x 1, …, x s + 1), \displaystyle\Delta^{s}\ x^{l}(x_{1},\dots,x_{s+1})=p_{l,s}(x_{1},\dots,x_{s+1}), |  | (4.8) |

where p l, s ​ ( x 1, …, x s + 1) p_{l,s}(x_{1},\dots,x_{s+1}) is 0 0 for s > l s>l and for s ≤ l s\leq l is the sum of all degree l − s l-s monomials in x 0, …, x s x_{0},\dots,x_{s} with unit coefficients,

 | p l, s ( x 1, …, x s + 1) = ∑ r 0 + ⋯ + r s = l − s ∏ j = 1 s + 1 x j r j. \displaystyle p_{l,s}(x_{1},\dots,x_{s+1})=\sum_{r_{0}+\dots+r_{s}=l-s}\quad\prod_{j=1}^{s+1}x_{j}^{r_{j}}. |  | (4.9) |

The divided differences form coefficients for the Newton interpolation formula. For all C ∞ C^{\infty} functions g: ℝ → ℝ g:\mathbb{R}\to\mathbb{R} we have

 | g ⁡ ( x) = Δ 0 ​ g ​ ( x 1) + Δ 1 ​ g ​ ( x 1, x 2) ​ ( x − x 1) + … + Δ k − 1 ​ g ​ ( x 1, …, x k − 2) ​ ( x − x 1) ​ … ​ ( x − x k − 3) + Δ k ​ g ​ ( x 1, …, x k − 1, x) ​ ( x − x 1) ​ … ​ ( x − x k − 2) \displaystyle\begin{aligned} g(x)=&\Delta^{0}g(x_{1})+\Delta^{1}g(x_{1},x_{2})(x-x_{1})+\dots\\ &+\Delta^{k-1}g(x_{1},\dots,x_{k-2})(x-x_{1})\dots(x-x_{k-3})\\ &+\Delta^{k}g(x_{1},\dots,x_{k-1},x)(x-x_{1})\dots(x-x_{k-2})\end{aligned} |  | (4.10) |

identically for all values of x, x 1, …, x k x,x_{1},\dots,x_{k}. All terms of this representation are polynomial in x x except for the last one which we view as a remainder term. The sum of the polynomial terms is the degree ( k − 1) (k-1) Newton interpolation polynomial for g g at { x s } s = 1 k \{x_{s}\}_{s=1}^{k}. To obtain a degree 2 ​ k − 1 2k-1 interpolation polynomial for g g and its derivative at { x s } s = 1 k \{x_{s}\}_{s=1}^{k}, we simply use ( 4.10) with k k replaced by 2 ​ k 2k and the 2 ​ k 2k -tuple of points { x s ⁡ ( mod ​ k) } s = 1 2 ​ k \{x_{s(\textup{mod}\ k)}\}_{s=1}^{2k}. Similarly one can construct an interpolation polynomial for g g and its derivatives up to any finite order.

All terms of this representation, except for the last one, are polynomial in x x and their sum is the k k -th order Newton Interpolation Polynomial denoted by 𝒫 k − 1 ​ ( x, 𝐗 k) \mathcal{P}_{k-1}(x,{\bf X}_{k}), where 𝐗 k = ( x 1, …, x k) {\bf X}_{k}=(x_{1},\dots,x_{k}).

Now we can define entries of diagram 4.2 in the case m = 0 m=0 Let 𝒟 ​ 𝒟 k ​ ( I, ℝ) = I × ⋯ × I ⏟ k ​ times × ℝ k = ( x 1, …, x k, u 0, u 1, …, u k − 1) {\mathcal{DD}}_{k}(I,\mathbb{R})=\underbrace{I\times\dots\times I}_{k\ \textup{times}}\times\mathbb{R}^{k}=(x_{1},\dots,x_{k};u_{0},u_{1},\dots,u_{k-1}). It is called the space of divided differences. Then

 | 𝒟 k ​ ( f): I × ⋯ × I ⏟ k ​ times → 𝒟 ​ 𝒟 k ​ ( I, ℝ), 𝒟 k ​ ( f): ( x 1, …, x k) ↦ ( x 1, …, x k, u 0, …, u k − 1), u α = Δ α ​ f ​ ( x 1, …, x α + 1) π k: 𝒟 ​ 𝒟 k ​ ( I, ℝ) → ℝ 2 ​ k, \displaystyle\begin{aligned} {\mathcal{D}}_{k}(f):\underbrace{I\times\dots\times I}_{k\ \textup{times}}&\to{\mathcal{DD}}_{k}(I,\mathbb{R}),\\ {\mathcal{D}}_{k}(f):(x_{1},\dots,x_{k})&\mapsto(x_{1},\dots,x_{k};u_{0},\dots,u_{k-1}),\quad u_{\alpha}=\Delta^{\alpha}f(x_{1},\dots,x_{\alpha+1})\\ \pi_{k}:{\mathcal{DD}}_{k}(I,\mathbb{R})&\to\mathbb{R}^{2k},\end{aligned} |  | (4.11) |

where 𝒟 k ​ ( f) {\mathcal{D}}_{k}(f) is smooth, provided that F F is smooth, π n: 𝒟 ​ 𝒟 k ​ ( I, ℝ) → ℝ 2 ​ k \pi_{n}:{\mathcal{DD}}_{k}(I,\mathbb{R})\to\mathbb{R}^{2k} is a Newton Interpolation Polynomial of the form ( 4.10), and

 | π k ∘ 𝒟 k ​ ( f) = ( f, …, f): I × ⋯ × I → ℝ 2 ​ k, \displaystyle\pi_{k}\circ{\mathcal{D}}_{k}(f)=(f,\dots,f):I\times\dots\times I\to\mathbb{R}^{2k}, |  | (4.12) |

where f f and ℝ \mathbb{R} are repeated k k times.

#### 4.2.2 Language of divided differences and the Newton interpolation formula

In this section we introduce construction of divided differences space 𝒟 ​ 𝒟 k ​ ( B n, ℝ N) {\mathcal{DD}}_{k}(B^{n},\mathbb{R}^{N}) and the corresponding map 𝒟 k ​ ( F) \mathcal{D}_{k}(F) and the polynomial π k \pi_{k} presented on diagram 1.3.

Let F: ℝ n → ℝ F:{\mathbb{R}}^{n}\to{\mathbb{R}} be a smooth function in n n real variables x 1, …, x n x_{1},\dots,x_{n}.

###### Definition 4.2.2.

The first order divided difference of F F in the variable x k x_{k} is the function of n + 1 n+1 variables x 1, …, x k − 1, x k ′, x k ′′, …, x n x_{1},\dots,x_{k-1},x^{\prime}_{k},x^{\prime\prime}_{k},\dots,x_{n} defined as

 | Δ x k ​ F ​ ( x 1, …, x k − 1, x k ′, x k ′′, …, x n) = F ⁡ ( x 1, …, x k − 1, x k ′, …, x n) − F ⁡ ( x 1, …, x k − 1, x k ′′, …, x n) x k ′ − x k ′′ \displaystyle\begin{aligned} \Delta_{x_{k}}F(x_{1},\dots,x_{k-1},x^{\prime}_{k},x^{\prime\prime}_{k},\dots,x_{n})=\\ \frac{F(x_{1},\dots,x_{k-1},x^{\prime}_{k},\dots,x_{n})-F(x_{1},\dots,x_{k-1},x^{\prime\prime}_{k},\dots,x_{n})}{x^{\prime}_{k}-x^{\prime\prime}_{k}}\end{aligned} |  | (4.13) |

for x k ′ ≠ x k ′′ x^{\prime}_{k}\neq x^{\prime\prime}_{k} and extended by its limit value as ∂ F ∂ x k ​ ( x 1, …, x k − 1, x k ′, …, x n) \frac{\partial F}{\partial x_{k}}(x_{1},\dots,x_{k-1},x^{\prime}_{k},\dots,x_{n}) for x k ′ = x k ′′ = x k x^{\prime}_{k}=x^{\prime\prime}_{k}=x_{k}. Clearly, if F F is C r C^{r} function, then (e.g., by the Hadamard lemma), Δ x k ​ F \Delta_{x_{k}}F is at least C r − 1 C^{r-1} -smooth function of its arguments.

It turns out that iterating this construction is possible [GY] which leads to

###### Definition 4.2.3.

Let α = ( α 1, …, α n) ∈ ℤ + n \alpha=(\alpha_{1},\dots,\alpha_{n})\in{\mathbb{Z}}^{n}_{+} be a multiindex, let F F be as above. Then Δ x α ​ F = Δ x 1 α 1 ​ … ​ Δ x n α n ​ F \Delta_{x}^{\alpha}F=\Delta_{x_{1}}^{\alpha_{1}}\dots\Delta_{x_{n}}^{\alpha_{n}}F is called the mixed divided difference of order | α | = α 1 + ⋯ + α n |\alpha|=\alpha_{1}+\dots+\alpha_{n}. This divided difference is a smooth function of n + | α | n+|\alpha| arguments subdivided into n n groups of α 1 + 1, …, α n + 1 \alpha_{1}+1,\dots,\alpha_{n}+1 variables, symmetric with respect to permutations of variables within the same groups.

As direct calculations show the operators Δ x j \Delta_{x_{j}} and Δ x i \Delta_{x_{i}} commute for i ≠ j i\neq j, and, therefore, we can use the multiindex notation for divided differences.

#### 4.2.3 The Newton interpolation formula (in multivariables)

Let X 1 = ( x 1 1, …, x N 1) ⊂ ℝ, …, X n = ( x 1 n, …, x N n) ⊂ ℝ X^{1}=(x^{1}_{1},\dots,x^{1}_{N})\subset{\mathbb{R}},\dots,X^{n}=(x^{n}_{1},\dots,x^{n}_{N})\subset{\mathbb{R}} be a subsets consisting of the same number of points, each X j X^{j} belonging to the corresponding j j -th coordinate axis of points in ℝ N. {\mathbb{R}}^{N}. Then, given a multiindex α ∈ ℤ + N \alpha\in\mathbb{Z}^{N}_{+} and a smooth function F ⁡ ( x) = F ⁡ ( x 1, …, x N) F(x)=F(x^{1},\dots,x^{N}) in N N variables we can form the divided difference Δ x α ​ F ​ ( X 1, …, X N) \Delta^{\alpha}_{x}F(X^{1},\dots,X^{N}).

In terms of the divided differences one can write the Newton interpolation polynomial as follows:

 | 𝒫 ⁡ ( t 1, …, t N) = ∑ 0 ≤ α i ≤ n Δ x α ​ F ​ ( X 1, …, X n) ​ ∏ i 1 = 1 α 1 … ​ ∏ i n = 1 α n ( t 1 − x i 1 1) ​ … ​ ( t n − x i n n). \displaystyle\begin{aligned} \mathcal{P}(t^{1},\dots,t^{N})=&\sum_{0\leq\alpha_{i}\leq n}\Delta^{\alpha}_{x}F(X^{1},\dots,X^{n})\prod_{i_{1}=1}^{\alpha_{1}}\dots\prod_{i_{n}=1}^{\alpha_{n}}(t^{1}-x^{1}_{i_{1}})\dots(t^{n}-x^{n}_{i_{n}}).\end{aligned} |  | (4.14) |

The polynomial 𝒫 ⁡ ( t 1, …, t n) \mathcal{P}(t^{1},\dots,t^{n}) has degree ≤ k ​ n \leq kn in variables t = ( t 1, …, t n) t=(t^{1},\dots,t^{n}). The Newton interpolation formula implies that the difference F ⁡ ( t) − 𝒫 ⁡ ( t 1, …, t n) F(t)-\mathcal{P}(t^{1},\dots,t^{n}) vanishes at all points of the Cartesian product grid 𝐗 = X 1 × ⋯ × X n ⊂ ℝ n {\bf X}=X^{1}\times\cdots\times X^{n}\subset{\mathbb{R}}^{n}. Moreover, if for each X j = ( x 1 j, …, x n j) X^{j}=(x^{j}_{1},\dots,x^{j}_{n}) we denote by diag k ​ ( X j) \text{diag}^{k}(X^{j}) the set ( x 1 j, …, x n j) (x^{j}_{1},\dots,x^{j}_{n}) repeated ( m + 1) (m+1) times

 | ( x 1 j, …, x n j ⏟, …, x 1 j, …, x n j ⏟) ( m ​ times), \displaystyle(\underbrace{x^{j}_{1},\dots,x^{j}_{n}},\dots,\underbrace{x^{j}_{1},\dots,x^{j}_{n}})\quad(m\ \textup{times}), |  | (4.15) |

then to obtain interpolation of the m m -th jet of F F we replace each X j = ( x 1 j, …, x n j) X^{j}=(x^{j}_{1},\dots,x^{j}_{n}) by diag m ​ ( X j) \text{diag}^{m}(X^{j}). The degree of interpolating polynomial will be ≤ n ​ k ​ ( m + 1) \leq nk(m+1).

In the case of a multivariate function F: B n → ℝ N F:B^{n}\to{\mathbb{R}}^{N} interpolating polynomial 𝒫 ⁡ ( t 1, …, t n) \mathcal{P}(t^{1},\dots,t^{n}) becomes N N -dimensional vector and is interpolating by coordinate functions of F = ( F 1, …, F N) F=(F^{1},\dots,F^{N}).

###### Definition 4.2.4.

Let 𝒟 ​ 𝒟 k m ​ ( B n, ℝ N) {\mathcal{DD}}^{m}_{k}(B^{n},\mathbb{R}^{N}) be the collection of all divided differences with m m repetitions, { Δ x α ​ F ​ ( diag m ​ ( X 1), …, diag m ​ ( X n)) } α, α i ≤ ( m + 1) ​ k, i = 1, …, n \{\Delta^{\alpha}_{x}F(\text{diag}^{m}(X^{1}),\dots,\text{diag}^{m}(X^{n}))\}_{\alpha},\ \alpha_{i}\leq(m+1)k,\ i=1,\dots,n. This is a linear space naturally equipped with the coordinates { x i, u α: 0 ≤ i ≤ N, α i ≤ ( m + 1) } \{x_{i},u_{\alpha}:\ 0\leq i\leq N,\ \alpha_{i}\leq(m+1)\}, where x i x_{i} (resp. u α u_{\alpha}) are vectors from ℝ n {\mathbb{R}}^{n} (resp., ℝ N {\mathbb{R}}^{N}). Dimension of this space is equal to k ​ n + N ​ ( ( m + 1) ​ k) n kn+N((m+1)k)^{n}.

The map 𝒟 k m ​ F {\mathcal{D}}^{m}_{k}F is defined by

 | 𝒟 k m ​ F: ( x 1, …, x k) → ( x 1, …, x k, { u α } α), where u α = Δ x α ​ F, ∀ i α i ≤ ( m + 1) ​ n. \displaystyle\begin{aligned} {\mathcal{D}}^{m}_{k}F:(x_{1},\dots,x_{k})\ \to\ (x_{1},\dots,x_{k},\{u_{\alpha}\}_{\alpha}),\\ \textup{where}\ \ u_{\alpha}=\Delta^{\alpha}_{x}F,\ \ \forall i\ \ \alpha_{i}\leq(m+1)n.\end{aligned} |  | (4.16) |

The multivariate interpolation formula together with its derivatives in t j t_{j} evaluated at the points of the grid, can be interpreted as a polynomial map restoring multijets from divided differences.

Newton Interpolation on ℝ m {\mathbb{R}}^{m} (abstract version) The multivariate Newton interpolation formula ( 4.14) defines a polynomial interpolation map π k m: 𝒟 ​ 𝒟 k m ​ ( B n, ℝ N) \pi^{m}_{k}:{\mathcal{DD}}^{m}_{k}(B^{n},\mathbb{R}^{N}) → 𝒥 m, k ​ ( B n, ℝ N) \to{\mathcal{J}}^{m,k}(B^{n},\mathbb{R}^{N}) such that 𝒥 m, k ​ f = π k m ∘ 𝒟 k m ​ F \mathcal{J}^{m,k}f=\pi^{m}_{k}\circ\mathcal{D}^{m}_{k}F. Degrees of the components of π k m \pi^{m}_{k} do not exceed ( k + 1) ​ n ​ N. (k+1)nN.

In the next section we present an application of Newton Interpolation Polynomials and diagram 4.2 to an old problem in dynamical systems: the problem of rate of growth of the number of periodic points for generic diffeomorphisms (see e.g. [AM] and [Sm]).

### 4.3 Rate of growth of the number of periodic points for generic diffeomorphisms and Newton Interpolation Polynomials

#### 4.3.1 Statement of the problem

Let Diff ( M) r {}^{r}(M) be the space of C r C^{r} diffeomorphisms of a finite-dimensional smooth compact manifold M M with the uniform C r C^{r} -topology, dim M ≥ 2, \dim M\geq 2, and let f ∈ Diff r ​ ( M) f\in{\textup{Diff}}^{r}(M). Consider the number of isolated periodic points of period n n

 | P n ( f) = #{ isolated x ∈ M: x = f n ( x) }. \displaystyle P_{n}(f)=\#\{\textup{isolated}\ \ x\in M:\ \ x=f^{n}(x)\}. |  | (4.17) |

The main question of this paper is:

 | How quickly can ​ P n ​ ( f) ​ grow with ​ n ​ for a “generic” diffeomorphism ​ f ​? \displaystyle\boxed{\textup{How quickly can}\ P_{n}(f)\ {\textup{grow with}\ n\ \textup{for a ``generic'' diffeomorphism}\ f?}} |  |

We put the word “generic” in brackets because as the reader will see the answer depends on notion of genericity.

We call a diffeomorphism f ∈ Diff r ​ ( M) f\in\textup{Diff}^{r}(M) an Artin-Mazur diffeomorphism (or simply A-M diffeomorphism) if the number of isolated periodic orbits of f f grows at most exponentially fast, i.e. for some number C > 0 C>0

 | P n ​ ( f) ≤ exp ⁡ ( C ​ n) for all n ∈ ℤ +. \displaystyle P_{n}(f)\leq\exp(Cn)\ \ {\textup{for all}}\ \ n\in\mathbb{Z}_{+}. |  | (4.18) |

Artin & Mazur [AM] proved the following

###### Theorem 4.3.1.

For any 0 ≤ r ≤ ∞ 0\leq r\leq\infty, A-M diffeomorphisms form a dense set of diffeomorphisms in Diff r ​ ( M) \textup{Diff}^{r}(M) with the uniform C r C^{r} -topology.

In [Ka5] an elementary proof of the following extension of the Artin-Mazur result is given

###### Theorem 4.3.2.

For any 0 ≤ r < ∞ 0\leq r<\infty A-M diffeomorphisms with all periodic points hyperbolic are dense in Diff r ​ ( M) \textup{Diff}^{r}(M) with the uniform C r C^{r} -topology.

According to the standard terminology a set in Diff ( M) r {}^{r}(M) is called generic ( or residual) if it contains a countable intersection of open dense sets and a property is called (Baire) generic if diffeomorphisms with that property form a residual set. It turns out the A-M property is not generic, as it is shown in [Ka6]. Moreover:

###### Theorem 4.3.3.

[Ka6] For any 2 ≤ r < ∞ 2\leq r<\infty there is an open set 𝒩 ⊂ \mathcal{N}\subset Diff ( M) r {}^{r}(M) such that for any given sequence a = { a n } n ∈ ℤ + a=\{a_{n}\}_{n\in\mathbb{Z}_{+}} there is a Baire generic set ℛ a \mathcal{R}_{a} in 𝒩 \mathcal{N} depending on the sequence a n a_{n} with the property if f ∈ ℛ a f\in\mathcal{R}_{a}, then for infinitely many n i ∈ ℤ + n_{i}\in\mathbb{Z}_{+} we have P n i ​ ( f) > a n i P_{n_{i}}(f)>a_{n_{i}}.

Since any two residual sets have nonempty intersection Theorem 4.3.3 implies that A-M diffeomorphisms are not generic. The proof of this Theorem is based on a result of Gonchenko-Shilnikov-Turaev [GST1]. Two slightly different detailed proofs of their result are given in [Ka6] and [GST2]. The proof in [Ka6] relies on a strategy outlined in [GST1].

However, it seems unnatural that if you pick a diffeomorphism at random then it may have an arbitrarily fast growth of number of periodic points. Moreover, Baire generic sets in Euclidean spaces can have zero Lebesgue measure. Phenomena which are Baire generic, but have a small probability are well-known in dynamical systems, KAM theory, number theory, and etc. (see [O], [HSY], and [Ka7] for various examples).

This partially motivates the problem posed by Arnold [A2]: Prove that “with probability one” f f is an A-M diffeomorphism. Arnold suggested the following interpretation of “with probability one”: for a (Baire) generic finite parameter family of diffeomorphisms { f ε } \{f_{\varepsilon}\}, for Lebesgue almost every ε \varepsilon we have that f ε f_{\varepsilon} is A-M. (cf. [Ka7]). As Theorem 4.3.3 shows, a result on the genericity of the set of A-M diffeomorphisms based on (Baire) topology is likely to be extremely subtle, if possible at all 1 1 1 For example, using techniques from [GST2] and [Ka6] one can prove that for a Baire generic finite-parameter family { f ε } \{f_{\varepsilon}\} and a Baire generic parameter value ε \varepsilon the corresponding diffeomorphism f ε f_{\varepsilon} is not A-M. Unfortunately, how to estimate from below the measure of non-A-M diffeomorphisms in a Baire generic finite-parameter family is so far an unreachable question.. We use instead a notion of “probability one” based on prevalence [HSY, Ka7], which is independent of Baire genericity. We also are able to state the result in the form Arnold suggested for generic families using this measure-theoretic notion of genericity. The main result in this direction is a partial solution to Arnold’s problem. It says that For a prevalent diffeomorphism f ∈ f\in Diff ( M) r, r > 1, {}^{r}(M),\ r>1, and any δ > 0 \delta>0 there exists C = C ⁡ ( δ) > 0 C=C(\delta)>0 such that for all n ∈ ℤ + n\in\mathbb{Z}_{+}

 | P n ​ ( f) ≤ exp ⁡ ( C ​ n 1 + δ) \displaystyle P_{n}(f)\leq\exp(Cn^{1+\delta}) |  | (4.19) |

This Theorem is announced in [KH]. A major part of the proof is worked out in [Ka9]. We omit the precise statement which requires an additional discussion.

### 4.4 Dynamical Usage of Newton Interpolation Polynomials

#### 4.4.1 Perturbation of recurrent trajectories by Newton Interpolation Polynomials

Let us start with several remarks which were the starting point of this paper. In order to keep notations and formulas simple we consider the 1-dimensional maps, but the reader should always have in mind that our consideration is designed for multidimensional diffeomorphisms.

Consider a map f: I ↪ I f:I\hookrightarrow I of the interval I = [− 1, 1] I=[-1,1]. Recall that a trajectory { x k } k ∈ ℤ \{x_{k}\}_{k\in\mathbb{Z}} of f f is called recurrent if it returns arbitrarily close to its initial position — that is, for all δ > 0 \delta>0 we have | x 0 − x n | < δ |x_{0}-x_{n}|<\delta for some n > 0 n>0. A very basic question of Closing lemma type is how much one should perturb f f to create a periodic point x 0 x_{0}. Let us give a “baby” answer

Baby Closing lemma. Let { x k = f k ( x 0) } k = 0 n \{x_{k}=f^{k}(x_{0})\}_{k=0}^{n} be a trajectory of length n + 1 n+1 of a map f: I ↪ I f:I\hookrightarrow I. Let u = ( x n − x 0) / ∏ k = 0 n − 2 ( x n − 1 − x k) u=(x_{n}-x_{0})/\prod_{k=0}^{n-2}(x_{n-1}-x_{k}). Then x 0 x_{0} is a periodic point of period n n of the map

 | f ~ ​ ( x) = f ⁡ ( x) + u ​ ∏ k = 0 n − 2 ( x − x k) \displaystyle\tilde{f}(x)=f(x)+u\prod_{k=0}^{n-2}(x-x_{k}) |  | (4.20) |

Of course f ~ \tilde{f} is close to f f only if u u is sufficiently small, meaning that | x 0 − x n | |x_{0}-x_{n}| is small compared to ∏ k = 0 n − 2 ( x n − 1 − x k) \prod_{k=0}^{n-2}(x_{n-1}-x_{k}). However, this product is likely to contain small factors for a recurrent trajectories. In general, it is difficult to control the effect of perturbations for recurrent trajectories. The simple reason why is because one can not perturb f f at two nearby points independently.

It is important for the proof in [Ka9] to control on derivative of f f along periodic orbits. If for some x ∈ I x\in I γ > 0 \gamma>0 and some positive integer n n we have f n ​ ( x) = x f^{n}(x)=x and | ( f n) ′ ​ ( x) − 1 | > γ |(f^{n})^{\prime}(x)-1|>\gamma, then it implies that the interval around x x of size ‖ f ‖ C 1 − n ​ γ \|f\|_{C^{1}}^{-n}\gamma is free from periodic points of the same period (see Proposition 1.1 [KH]). Quantity γ \gamma is called hyperbolicity and x x is called ( n, γ) (n,\gamma) -hyperbolic. This quantity was introduced by Gromov [Go] and Yomdin [Y]. If one can estimate hyperbolicity for all points of period n n from below, then one can estimate the number of periodic points of period n n. Upper bound ( 4.19) is obtained by proving lower bound on the rate of decay of hyperbolicity with period for prevalent diffeomorphisms. This is the reason the proof needs to control derivative along trajectories.

The Closing Lemma above also gives an idea of how much we must change the parameter u u to make a point x 0 x_{0} that is ( n, γ) (n,\gamma) -periodic not be ( n, γ) (n,\gamma) -periodic for a given γ > 0 \gamma>0, which as we described above is one way to make a map that is “bad” for the initial condition x 0 x_{0} become “good”. To make use of our other alternative we must determine how much we need to perturb a map f f to make a given x 0 x_{0} be ( n, γ) (n,\gamma) -hyperbolic for some γ > 0 \gamma>0.

Perturbation of hyperbolicity. Let { x k = f k ( x 0) } k = 0 n − 1 \{x_{k}=f^{k}(x_{0})\}_{k=0}^{n-1} be a trajectory of length n n of a C 1 C^{1} map f: I → I f:I\to I. Then for the map

 | f v ​ ( x) = f ⁡ ( x) + v ⁡ ( x − x n − 1) ​ ∏ k = 0 n − 2 ( x − x k) 2 \displaystyle f_{v}(x)=f(x)+v(x-x_{n-1})\prod_{k=0}^{n-2}(x-x_{k})^{2} |  | (4.21) |

such that v ∈ ℝ v\in\mathbb{R} and

 | | | ( f v n) ′ ​ ( x 0) | − 1 | = | | ∏ k = 0 n − 1 f ′ ​ ( x k) + v ​ ∏ k = 0 n − 2 ( x n − 1 − x k) 2 ​ ∏ k = 0 n − 2 f ′ ​ ( x k) | − 1 | > γ \displaystyle\left|\vphantom{{f^{\prime}}^{2}}|(f^{n}_{v})^{\prime}(x_{0})|-1\right|=\left|\vphantom{{{\prod_{0}^{n}}^{2}}^{2}}\left|\prod_{k=0}^{n-1}f^{\prime}(x_{k})+v\prod_{k=0}^{n-2}(x_{n-1}-x_{k})^{2}\prod_{k=0}^{n-2}f^{\prime}(x_{k})\right|-1\right|>\gamma |  | (4.22) |

we have that x 0 x_{0} is an ( n, γ) (n,\gamma) -hyperbolic point of f v f_{v}.

One more time we can see the product of distances ∏ k = 0 n − 2 | x n − 1 − x k | \prod_{k=0}^{n-2}|x_{n-1}-x_{k}| along the trajectory is important quantitative characteristic of how much freedom we have to perturb.

The perturbations ( 4.20) and ( 4.21) are reminiscent of Newton interpolation polynomials. Let us put these formulas into a general setting using singularity theory.

#### 4.4.2 Distance to the diagonal in the multijet space

Consider the 2 ​ n 2n -parameter family of perturbation of a map f: I ↪ I f:I\hookrightarrow I by polynomials of degree 2 ​ n − 1 2n-1

 | f ε ​ ( x) = f ⁡ ( x) + ∑ k = 0 2 ​ n − 1 ε k ​ x k. \displaystyle f_{\varepsilon}(x)=f(x)+\sum_{k=0}^{2n-1}\varepsilon_{k}x^{k}. |  | (4.23) |

Define a map

 | 𝒥 n 1 ​ f: I × ⋯ × I ⏟ n ​ times × ℝ 2 ​ n → I × ⋯ × I ⏟ n ​ times × ( I × ℝ) × ⋯ × ( I × ℝ) ⏟ n ​ times 𝒥 1, n ​ f ​ ( x 0, …, x n − 1, ε) = ( x 0, …, x n − 1, f ε ( x 0), f ′ ε ( x 0), OPEN …, f ε ​ ( x n − 1), f ε ′ ​ ( x n − 1)). \displaystyle\begin{aligned} {{\mathcal{J}}}^{1}_{n}f:\underbrace{I\times\dots\times I}_{n\ \textup{times}}\times\mathbb{R}^{2n}&\to\underbrace{I\times\dots\times I}_{n\ \textup{times}}\times\underbrace{(I\times\mathbb{R})\times\dots\times(I\times\mathbb{R})}_{n\ \textup{times}}\\ {{\mathcal{J}}}^{1,n}f(x_{0},\dots,x_{n-1},\varepsilon)=&\\ \left(x_{0},\dots,x_{n-1},f_{\varepsilon}(x_{0}),f^{\prime}_{\varepsilon}(x_{0}),\right.&\left.\dots,f_{\varepsilon}(x_{n-1}),f^{\prime}_{\varepsilon}(x_{n-1})\right).\end{aligned} |  | (4.24) |

This map is called the n n -tuple 1-jet map. The 1 1 -jet of a function means that we take into account not only the image of a point, but also its derivative. The 1 1 -jet of a function is usually denoted by j 1 ​ f ε ​ ( x) = ( x, f ε ​ ( x), f ε ′ ​ ( x)) j^{1}f_{\varepsilon}(x)=(x,f_{\varepsilon}(x),f_{\varepsilon}^{\prime}(x)). The space of 1-jets of functions on the interval I I is denoted by 𝒥 1 ​ ( I, ℝ) {{\mathcal{J}}}^{1}(I,\mathbb{R}). The product of n n copies of 𝒥 1 ​ ( I, ℝ) {{\mathcal{J}}}^{1}(I,\mathbb{R}) is multijet space and is denoted by

 | 𝒥 1, n ​ ( I, ℝ) = 𝒥 1 ​ ( I, ℝ) × ⋯ × 𝒥 1 ​ ( I, ℝ) ⏟ n ​ times. \displaystyle{{\mathcal{J}}}^{1,n}(I,\mathbb{R})=\underbrace{{{\mathcal{J}}}^{1}(I,\mathbb{R})\times\dots\times{{\mathcal{J}}}^{1}(I,\mathbb{R})}_{n\ \textup{times}}. |  | (4.25) |

We need to include into our consideration derivatives, because we are interested in hyperbolicity (property of derivatives) of periodic points. The set of points

 | Δ n ​ ( I) = { { x 0, …, x n − 1 } × ℝ 2 ​ n ⊂ I × ⋯ × I ⏟ n ​ times × ℝ 2 ​ n: ∃ s.t. ​ i ≠ j ​ x i = x j } \displaystyle\Delta_{n}(I)=\left\{\{x_{0},\dots,x_{n-1}\}\times\mathbb{R}^{2n}\subset\underbrace{I\times\dots\times I}_{n\ \textup{times}}\times\mathbb{R}^{2n}:\exists\ \textup{s.t.}\ i\neq j\ x_{i}=x_{j}\right\}\quad |  | (4.26) |

is called the diagonal in the space of multijets. In singularity theory the space of multijets is defined outside of the diagonal Δ n ​ ( I) \Delta_{n}(I) and is usually denoted by 𝒥 1, n ​ ( I, ℝ) = 𝒥 1, n ​ ( I, ℝ) ∖ Δ n ​ ( I) {{\mathcal{J}}}^{1,n}(I,\mathbb{R})={{\mathcal{J}}}^{1,n}(I,\mathbb{R})\setminus\Delta_{n}(I) (see [GG]).

It is easy to see that a recurrent trajectory { x k } k ∈ ℤ + \{x_{k}\}_{k\in\mathbb{Z}_{+}} is located in a neighborhood of the diagonal Δ n ​ ( I) \Delta_{n}(I) in the space of multijets for a sufficiently large n n. If { x k } k = 0 n − 1 \{x_{k}\}_{k=0}^{n-1} is a part of a recurrent trajectory of length n n, then the product of distances along the trajectory

 | ∏ k = 0 n − 2 | x n − 1 − x k | \displaystyle\prod_{k=0}^{n-2}\left|x_{n-1}-x_{k}\right| |  | (4.27) |

measures how close { x k } k = 0 n − 1 \{x_{k}\}_{k=0}^{n-1} to the diagonal Δ n ​ ( I) \Delta_{n}(I), or how independently one can perturb points of a trajectory. One can also say that ( 4.27) is a quantitative characteristic of how recurrent a trajectory of length n n is. Introduction of this product of distances along a trajectory is a new central point of the method.

#### 4.4.3 Newton interpolation and blow-up along the diagonal in multijet space

Now look at Grigoriev-Yakovenko’s construction [GY] in the 1 1 -dimensional case with more details. This construction puts the “Closing Lemma” and “Perturbation of Hyperbolicity” statements above into a general framework.

Again consider the 2 ​ n 2n -parameter family ( 4.23) of perturbations of a C 1 C^{1} map f: I → I f:I\to I by polynomials of degree 2 ​ n − 1 2n-1. Our goal now is to describe how such perturbations affect the n n -tuple 1 1 -jet of f f, and since the operator j 1, n j^{1,n} is linear in f f, for the time being we consider only the perturbations ϕ ε \phi_{\varepsilon} and their n n -tuple 1 1 -jets. For each n n -tuple { x k } k = 0 n − 1 \{x_{k}\}_{k=0}^{n-1} there is a natural transformation 𝒥 1, n: I n × ℝ 2 ​ n → 𝒥 1, n ​ ( I, ℝ) {\mathcal{J}}^{1,n}:I^{n}\times\mathbb{R}^{2n}\to{\mathcal{J}}^{1,n}(I,\mathbb{R}) from ε \varepsilon -coordinates to jet-coordinates, given by

 | 𝒥 1, n ​ ( x 0, …, x n − 1, ε) = j 1, n ​ ϕ ε ​ ( x 0, …, x n − 1). \displaystyle{\mathcal{J}}^{1,n}(x_{0},\dots,x_{n-1},\varepsilon)=j^{1,n}\phi_{\varepsilon}(x_{0},\dots,x_{n-1}). |  | (4.28) |

Instead of working directly with the transformation 𝒥 1, n {\mathcal{J}}^{1,n}, we introduce intermediate u u -coordinates based on Newton interpolation polynomials. The relation between ε \varepsilon -coordinates and u u -coordinates is given implicitly by

 | ϕ ε ​ ( x) = ∑ k = 0 2 ​ n − 1 ε k ​ x k = ∑ k = 0 2 ​ n − 1 u k ​ ∏ j = 0 k − 1 ( x − x j ⁡ ( mod ​ n)). \displaystyle\phi_{\varepsilon}(x)=\sum_{k=0}^{2n-1}\varepsilon_{k}x^{k}=\sum_{k=0}^{2n-1}u_{k}\prod_{j=0}^{k-1}(x-x_{j(\textup{mod}\ n)}). |  | (4.29) |

Based on this identity, we can define functions 𝒟 n 1: I n × ℝ 2 ​ n → I n × ℝ 2 ​ n \mathcal{D}^{1}_{n}:I^{n}\times\mathbb{R}^{2n}\to I^{n}\times\mathbb{R}^{2n} and π n 1: I n × ℝ 2 ​ n → 𝒥 1, n ​ ( I, ℝ) \pi^{1}_{n}:I^{n}\times\mathbb{R}^{2n}\to{\mathcal{J}}^{1,n}(I,\mathbb{R}) so that 𝒥 1, n = π n 1 ∘ 𝒟 n 1 {\mathcal{J}}^{1,n}=\pi^{1}_{n}\circ\mathcal{D}^{1}_{n}, or in other words the diagram in Figure 4.2 commutes. This definition coincides with the one we gave before. We will show later that 𝒟 n 1 \mathcal{D}^{1}_{n} is invertible, while π n 1 \pi^{1}_{n} is invertible away from the diagonal Δ n ​ ( I) \Delta_{n}(I) and defines a blow-up along it in the space of multijets 𝒥 1, n ​ ( I, ℝ) {\mathcal{J}}^{1,n}(I,\mathbb{R}). Consider diagram 4.2 for m = n = N = 1 m=n=N=1.

Recall that the intermediate space, denoted by 𝒟 ​ 𝒟 n 1 ​ ( I, ℝ) {\mathcal{DD}}^{1}_{n}(I,\mathbb{R}), is called the space of divided differences and consists of n n -tuples of points { x k } k = 0 n − 1 \{x_{k}\}_{k=0}^{n-1} and 2 ​ n 2n real coefficients { u k } k = 0 2 ​ n − 1 \{u_{k}\}_{k=0}^{2n-1}. Here are explicit coordinate-by-coordinate formulas defining π n 1: 𝒟 ​ 𝒟 n 1 ​ ( I, ℝ) → 𝒥 1, n ​ ( I, ℝ) \pi^{1}_{n}:{\mathcal{DD}}^{1}_{n}(I,\mathbb{R})\to{\mathcal{J}}^{1,n}(I,\mathbb{R}).

 | ϕ ε ​ ( x 0) = u 0, ϕ ε ​ ( x 1) = u 0 + u 1 ​ ( x 1 − x 0), ϕ ε ​ ( x 2) = u 0 + u 1 ​ ( x 2 − x 0) + u 2 ​ ( x 2 − x 0) ​ ( x 2 − x 1), ⋮ ϕ ε ​ ( x n − 1) = u 0 + u 1 ​ ( x n − 1 − x 0) + ⋯ + u n − 1 ​ ( x n − 1 − x 0) ​ … ​ ( x n − 1 − x n − 2), ϕ ε ′ ​ ( x 0) = ∂ ∂ x ​ ( ∑ k = 0 2 ​ n − 1 u k ​ ∏ j = 0 k − 1 ( x − x j ⁡ ( mod ​ n))) | x = x 0, ⋮ ϕ ε ′ ​ ( x n − 1) = ∂ ∂ x ​ ( ∑ k = 0 2 ​ n − 1 u k ​ ∏ j = 0 k − 1 ( x − x j ⁡ ( mod ​ n))) | x = x n − 1, \displaystyle\begin{aligned} \phi_{\varepsilon}(x_{0})=&\,u_{0},\\ \phi_{\varepsilon}(x_{1})=&\,u_{0}+u_{1}(x_{1}-x_{0}),\\ \phi_{\varepsilon}(x_{2})=&\,u_{0}+u_{1}(x_{2}-x_{0})+u_{2}(x_{2}-x_{0})(x_{2}-x_{1}),\\ \vdots\,&\\ \phi_{\varepsilon}(x_{n-1})=&\,u_{0}+u_{1}(x_{n-1}-x_{0})+\dots+u_{n-1}(x_{n-1}-x_{0})\dots(x_{n-1}-x_{n-2}),\\ \phi_{\varepsilon}^{\prime}(x_{0})=&\,\frac{\partial}{\partial x}\left(\sum_{k=0}^{2n-1}u_{k}\prod_{j=0}^{k-1}(x-x_{j(\textup{mod}\ n)})\right)\Big|_{x=x_{0}},\\ \vdots\,&\\ \phi_{\varepsilon}^{\prime}(x_{n-1})=&\,\frac{\partial}{\partial x}\left(\sum_{k=0}^{2n-1}u_{k}\prod_{j=0}^{k-1}(x-x_{j(\textup{mod}\ n)})\right)\Big|_{x=x_{n-1}},\end{aligned} |  | (4.30) |

These formulas are very useful for dynamics. For a given base map f f and initial point x 0 x_{0}, the image f ε ​ ( x 0) = f ⁡ ( x 0) + ϕ ε ​ ( x 0) f_{\varepsilon}(x_{0})=f(x_{0})+\phi_{\varepsilon}(x_{0}) of x 0 x_{0} depends only on u 0 u_{0}. Furthermore the image can be set to any desired point by choosing u 0 u_{0} appropriately — we say then that it depends nontrivially on u 0 u_{0}. If x 0 x_{0}, x 1 x_{1}, and u 0 u_{0} are fixed, the image f ε ​ ( x 1) f_{\varepsilon}(x_{1}) of x 1 x_{1} depends only on u 1 u_{1}, and as long as x 0 ≠ x 1 x_{0}\neq x_{1} it depends nontrivially on u 1 u_{1}. More generally for 0 ≤ k ≤ n − 1 0\leq k\leq n-1, if pairwise distinct points { x j } j = 0 k \{x_{j}\}_{j=0}^{k} and coefficients { u j } j = 0 k − 1 \{u_{j}\}_{j=0}^{k-1} are fixed, then the image f ε ​ ( x k) f_{\varepsilon}(x_{k}) of x k x_{k} depends only and nontrivially on u k u_{k}.

Suppose now that an n n -tuple of points { x j } j = 0 n \{x_{j}\}_{j=0}^{n} not on the diagonal Δ n ​ ( I) \Delta_{n}(I) and Newton coefficients { u j } j = 0 n − 1 \{u_{j}\}_{j=0}^{n-1} are fixed. Then derivative f ε ′ ​ ( x 0) f^{\prime}_{\varepsilon}(x_{0}) at x 0 x_{0} depends only and nontrivially on u n u_{n}. Likewise for 0 ≤ k ≤ n − 1 0\leq k\leq n-1, if distinct points { x j } j = 0 n \{x_{j}\}_{j=0}^{n} and Newton coefficients { u j } j = 0 n + k − 1 \{u_{j}\}_{j=0}^{n+k-1} are fixed, then the derivative f ε ′ ​ ( x k) f^{\prime}_{\varepsilon}(x_{k}) at x k x_{k} depends only and nontrivially on u n + k u_{n+k}.

As Figure 4.3 illustrates, these considerations show that for any map f f and any desired trajectory of distinct points with any given derivatives along it, one can choose Newton coefficients { u k } k = 0 2 ​ n − 1 \{u_{k}\}_{k=0}^{2n-1} and explicitly construct a map f ε = f + ϕ ε f_{\varepsilon}=f+\phi_{\varepsilon} with such a trajectory. Thus we have shown that π n 1 \pi^{1}_{n} is invertible away from the diagonal Δ n ​ ( I) \Delta_{n}(I) and defines a blow-up along it in the space of multijets 𝒥 1, n ​ ( I, ℝ) {\mathcal{J}}^{1,n}(I,\mathbb{R}).

[image: Refer to caption] Figure 4.3: Newton coefficients and their action

The function 𝒟 1, n: I n × ℝ 2 ​ n → 𝒟 ​ 𝒟 1, n ​ ( I, ℝ) \mathcal{D}^{1,n}:I^{n}\times\mathbb{R}^{2n}\to{\mathcal{DD}}^{1,n}(I,\mathbb{R}) was explicitly defined using so-called divided differences above.

Recall that 𝒟 n 1 \mathcal{D}^{1}_{n} was defined implicitly by ( 4.29). We have described how to use divided differences to construct a degree 2 ​ n − 1 2n-1 interpolating polynomial of the form on the right-hand side of ( 4.29) for an arbitrary C ∞ C^{\infty} function g g. Our interest then is in the case g = ϕ ε g=\phi_{\varepsilon}, which as a degree 2 ​ n − 1 2n-1 polynomial itself will have no remainder term and coincide exactly with the interpolating polynomial. Thus 𝒟 1, n \mathcal{D}^{1,n} is given coordinate-by-coordinate by

 | u m = Δ m ​ ( ∑ k = 0 2 ​ n − 1 ε k ​ x k) ​ ( x 0, …, x m ⁡ ( m ​ o ​ d ​ n)) = ε m + ∑ k = m + 1 2 ​ n − 1 ε k ​ p k, m ​ ( x 0, …, x m ⁡ ( m ​ o ​ d ​ n)) \displaystyle\begin{aligned} u_{m}=&\,\Delta^{m}\left(\sum_{k=0}^{2n-1}\varepsilon_{k}x^{k}\right)(x_{0},\dots,x_{m\ (mod\ n)})\\ =&\,\varepsilon_{m}+\sum_{k=m+1}^{2n-1}\varepsilon_{k}p_{k,m}(x_{0},\dots,x_{m\ (mod\ n)})\end{aligned} |  | (4.31) |

for m = 0, …, 2 ​ n − 1 m=0,\dots,2n-1. We call the transformation given by ( 4.31) the Newton map. Notice that for fixed { x k } k = 0 2 ​ n − 1 \{x_{k}\}_{k=0}^{2n-1}, the Newton map is linear and given by an upper triangular matrix with units on the diagonal. Hence it is Lebesgue volume-preserving and invertible, whether or not { x k } k = 0 2 ​ n − 1 \{x_{k}\}_{k=0}^{2n-1} lies on the diagonal Δ n ​ ( I) \Delta_{n}(I).

We call the basis of monomials

 | ∏ j = 0 k ( x − x j ⁡ ( mod ​ n)) for k = 0, …, 2 ​ n − 1 \displaystyle\prod_{j=0}^{k}(x-x_{j(\textup{mod}\ n)})\ \ \ \textup{for}\ \ \ k=0,\dots,2n-1 |  | (4.32) |

in the space of polynomials of degree 2 ​ n − 1 2n-1 the Newton basis defined by the n n -tuple { x k } k = 0 n − 1 \{x_{k}\}_{k=0}^{n-1}. The Newton map and the Newton basis, and their analogues in dimension N N, are useful tools for perturbing trajectories and proving ( 4.19).

Acknowledgments: In this lecture I have used fragments of the announcement [KH]. Good presentation of it is absolutely due to my coauthor Brian Hunt. Needless to say that numerous communications with him and also John Mather were very important for me.

## References

- [A1] V. Arnold at el., Some unsolved problems in the theory of differential equations and mathematical physics, Russ. Math. Surveys, 44, (1989), no. 4;
- [A2] V. Arnold, Problems for Arnold’s seminar, 1989;
- [AA] D. Anosov, V. Arnold, Dynamical systems. I, Encyclopedia Math. Sci., 1, Springer, Berlin, 1988;
- [AGV] V. Arnold, S. Gusein-Zade, A. Varchenko Singularities of differentiable maps. Vol. I. Monographs in Mathematics, 82, Birkhauser Boston, 1985;
- [AM] M. Artin, B. Mazur, Periodic orbits, Annals of Mathematics, 81, 1965, 82–99;
- [Be] I. Bendixon, Sur les corbes definies par des equations diffirentialles, Acta Math. 24, (1901), 1–88;
- [BZ] I. Berezin, N. Zhidkov, Computing Methods, Vol. 1, Pergamon, Oxford, 1965;
- [BCR] J. Bochnak, M. Coste, M.-F. Roy, Real Algebraic Geometry, Springer-Verlag, Berlin, 1998.
- [Bo] A. Bolibrukh, present volume;
- [Bu] A. Buium, present volume;
- [DeR] Z. Denkowska, R. Roussarie, A Method of Desingularization for Analytic two-dimensional vector field families, Bol. Soc. Bras. Mat. 22, 1, (1991), 93–126;
- [DeW] Z. Denkowska, K. Wachta, A Construction of a subanalytic stratification under the condition (w), Bull. Polish Acad. Sci. Math. 35, (1987), no. 7–8, 401–405;
- [Dr1] L. van den Dries, present volume;
- [Dr2] L. van den Dries, o-minimal structures and real analytic geometry. Current developments in mathematics, 1998 (Cambridge, MA), 105–152, Int. Press, Somerville, MA, 1999;
- [Du] H. Dulac, Sur les cycles limites, Bull. Soc. Math. France 51, (1923), 45–188;
- [D] F. Dumortier, Singularities of vector fields on the plane, J. Diff.Equations, 23, (1977), 53–106;
- [DMR] F. Dumortier, M. El Morsalani, C. Rousseau, Hilbert’s 16th problem for quadratic systems and cyclicity of elementary graphics, Nonlinearity 9 (1996), no. 5, 1209–1261;
- [DRR] F. Dumortier, R. Roussarie, C. Rousseau, Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations, 110, (1994), no. 1, 86–133;
- [E] J. Ecalle, Introduction aux fonctions analysables et preuve consrustive de la conjecture de Dulac, Herman, Paris, (1992);
- [FP] J.-P. Francoise, C. Pugh, Keeping track of limit cycles. J. Diff. Eqns 65, (1986), no. 2, 139–157;
- [GK] A. Gabrielov, A. Khovanskii, Multiplicity of a Notherian Intersection, Geometry of Differential Equations, Amer. Math. Soc. Transl., 1998, 119-131;
- [Ga] L. Gavrilov, The infinitesimal 16th Hilbert problem in the quadratic case. Invent. Math. 143 (2001), no. 3, 449–497;
- [GWPL] C. Gibson, K. Wirthmuller, A. du Plessis, E. Loojenga, Topological Stability of Smooth Mappings, LNM, 552, Springer, 1976;
- [GG] M. Golubitsky, V. Guillemin, Stable Mappings and Their Singularities, Graduate Texts in Mathematics 14, Springer-Verlag, 1973;
- [GST1] S. Gonchenko, L. Shil’nikov, D. Tuvaev, On models with non-rough Poincaré homoclinic curves, Physica D 62 (1993), 1–14;
- [GST2] S. Gonchenko, L. Shil’nikov, D. Tuvaev, Homoclinic tangencies of an arbitrary order in Newhouse’s domains (in Russian), preprint;
- [GM] M. Goresky, R. MacPherson, Stratified Morse Theory, Springer, 1987;
- [GY] A. Grigoriev, S. Yakovenko, Topology of generic multijet preimages and blow-up via Newton interpolation, J. Diff. Eqns 150, (1998), no. 2, 349–362;
- [Go] M. Gromov, On entropy of holomorphic maps, preprint;
- [Gr] T. Grozovskii, Bifurcations of polycycles an “apple” and a “half-apple” in generic two-parameter families, Diff. Equations (in Russian), 32, (1996), no. 4, 458–469;
- [GH] J. Guckenheimer, P. Holmes, Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields, Springer-Verlag, New York, 1983;
- [Hi] H. Hironaka, Number Theory, Algebraic Geometry and Commutative Algebra, Volume in Honor of Y. Akizuki, Kinokunia, Tokyo, 1973;
- [HSY] B. Hunt, T. Sauer, J. Yorke, Prevalence: a translation-invariant ‘almost every’ on infinite-dimensional spaces” Bull. Amer. Math. Soc. (N.S.) 27, (1992), no. 2, 217–238 & 28, (1993), no. 2, 306–307.
- [I1] Yu. Ilyashenko, The multiplicity of limit cycles that arise in the perturbation of a Hamiltonian equation of the class d ​ w / d ​ z = P 2 / Q 1 dw/dz=P_{2}/Q_{1}, in the real and complex domain, Amer. Math.Soc. Transl. (2), 118, (1982), 191–202;
- [I2] Yu. Ilyashenko, Dulac’s memoir ”On limit cycles” and related questions of the local theory of differential equations, Russ. Math. Surveys, 40, (1985), no. 6(246), 41–78;
- [I3] Yu. Ilyashenko, Finiteness theorem for limit cycles, Amer. Math. Soc., Providence, 1991;
- [I4] Yu. Ilyashenko, Normal forms for local families and nonlocal bifurcations, Asterisque, 222, (1994), 233–258;
- [IK] Yu. Ilyashenko, V. Kaloshin, Bifurcation of planar and spatial polycycles: Arnold’s program and its development. The Arnoldfest, 241–271, Fields Inst. Commun., 24, Amer. Math. Soc., Providence, RI, 1999;
- [IL] Yu. Ilyashenko, W. Li, Nonlocal bifurcations. Math. Surv. and Mon., 66. American Mathematical Society, Providence, RI, 1999;
- [IY1] Yu.Ilyashenko, S. Yakovenko, Finitely smooth normal forms of local families of diffeomorphisms and vector fields, Russian Math. Surveys 46, (1991), no. 1, 1–43;
- [IY2] Yu.Ilyashenko, S. Yakovenko, Finite Cyclicity of Elementary Polycycles in Generic Families, Amer.Math.Soc.Transl, 165, (1995), 1–20 & 21–95;
- [Ja] N. Jakobson, Basic Algebra, vol. 1, 1974;
- [Ka1] V. Kaloshin, The Hilbert-Arnold Problem and estimates on cyclicity of elementary polycycles and multiplicity of generic germs, preprint;
- [Ka2] V. Kaloshin, Bifurcations of spatial polycycles, (in Russian) (in preparation);
- [Ka3] V. Kaloshin, The Hilbert-Arnold Problem and estimates on cyclicity of planar and spacial polycycles, Funct. Anal. and Appl. 35, (2001), 78–81;
- [Ka4] V. Kaloshin, A Geometric Proof of Existence of Whitney’s stratifications, preprint;
- [Ka5] V. Kaloshin, An Extension of Artin-Mazur Theorem, Ann of Math. 50, (1999), no. 2, 729–741;
- [Ka6] V. Kaloshin, Generic diffeomorphisms with superexponential growth of number of periodic points, Comm. in Math. Physics 211, (2000) 1, 253–271;
- [Ka7] V. Kaloshin, Some prevalent properties of smooth dynamical systems, Proc. of Steklov Math. Inst. 213, (1997), 123–151;
- [Ka8] V. Kaloshin, Prevalence in spaces of finitely smooth mappings, Funct. Anal. Appl. 31, (1997), no. 2, 95–99;
- [Ka9] V. Kaloshin, Streched exponential estimate on the rate of growth of the number of periodic points for prevalent diffeomorphisms, Thesis, Princeton, 2001;
- [KH] V. Kaloshin, B. Hunt, Streched exponential estimate on the rate of growth of the number of periodic points for prevalent diffeomorphisms, Electronic Research Announcements of AMS, part I, 7, 17–27, 2001 & part II, 7, 28–36, 2001;
- [Kh1] A. Khovanskii, Real analytic manifolds with the property of finiteness and complex abelian integrals, Func. Anal and Appl. 18, (1984), no.2, 40–50;
- [Kh2] A. Khovanskii, Fewnomials, Amer.Math.Soc. Transl., Providence, RI, 1991;
- [Kl] O. Kleban, Order of the topologically sufficient jet of a smooth vector field on the real plane at a singular point of finite multiplicity. Amer. Math. Soc. Transl, Ser.2, 165, (1995), 131–153;
- [KS] A. Kotova, V. Stanzo, Few-Parameter Generic Families on the Sphere, Amer. Math. Soc. Translations, Providence, RI, Ser. 2, 213, (1996), 155–202;
- [Ku] T.-C. Kuo, The ratio test for analytic Whitney stratifications, Lecture Notes, No. 192, 141-149;
- [Lo1] S. Lojasiewicz, Ensemble Semi-Analytiques, IHES Lecture Notes, 1965;
- [Lo2] S. Lojasiewicz, Sur le géometrie semi- et sous-analytic, (French) Ann. Inst. Fourier (Grenoble), 43, (1993), no. 5, 1575–1595.
- [LSW] S. Lojasiewicz, J. Stasica, K. Wachta, Subanalytic stratifications. Verdier’s condition, Bull. Polish Acad. Sci. Math. 34, (1986), no. 9–10, 531–539;
- [Mr] P. Mardesić, An explicit bound for the multiplicity of zeroes of generic Abelian integrals, Nonlinearity, 4, (1991), no.3, 845–852;
- [Ma] J. Mather, Notes on topological stability, Harvard University, 1970;
- [Mi1] J. Milnor, Singularities of Complex Hypersurfaces, Ann. of Math. Studies, no. 61, 1968;
- [Mi2] J. Milnor, Topology from Differentiable viewpoint, Princeton University Press, 1997 ;
- [MR] R. Moussu, C. Roche, Khovanskii’s theory and the Dulac problem, Invent. Math. 105 (1991), no. 2, 431–441;
- [Mu] D. Mumford, Algebraic Geometry I, Springer, New York, 1976;
- [NY1] D. Novikov, S. Yakovenko, Simple Exponential Estimate for the number of zeroes of complete Abelian Integrals, Ann. Inst. Fourier (Grenoble), 45, (1995), no. 4, 897–927;
- [NY2] D. Novikov, S. Yakovenko, present volume;
- [O] J. Oxtoby, Measure and category. A survey of the analogies between topological and measure spaces. Graduate Texts in Mathematics, 2. Springer-Verlag, New York-Berlin, 1980.
- [Pa] W. Pawlucki, The Puiseux Theorem for subanalytic mappings, Polish Acad. Sci. Math. 32, (1984), no. 9–10, 555–560;
- [P] G. Petrov, Nonoscillation of elliptic integrals, Func. Anal. and Appl., 24, (1990), no.3, 205–210;
- [PW] A. du Plessis, T. Wall, The Geometry of Topological Stability, Oxford, 1995;
- [R1] R. Roussarie, Cyclicite finie et le 16 problem d’Hilbert, Dynamical systems, (Volparaiso, (1986)), (R.Bauon, R.Lavarca, and J.Palis, eds.), LNM, 1331, Springer-Verlag, Berlin and New York, (1988), 161–188;
- [R2] R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem, Progress in Mathematics, 164, Birkhauser, 1998;
- [Se] A. Seidenberg, Reduction of singularities of the differential equations A ​ d ​ y = B ​ d ​ x Ady=Bdx, Amer. J. Math. 90, (1968), 248–269;
- [Sh] L. Shilnikov, A case of the existence of a denumerable set of periodic motions. (Russian) Dokl. Akad. Nauk SSSR 160, (1965), 558–561;
- [S] D. Shlomiuck(ed), Bifurcations and periodic orbits of vector fields, NATO AS1, Series C (Math. and Phys. Sciences), vol. 408, Kluwel, Dordrecht, Boston, London, 1993;
- [Sm] S. Smale, Differentiable Dynamical Systems, Bull. Amer. Math. Soc. 73 (1967), 747–817;
- [Ta] F. Takens, Unfoldings of certain singularities of vector fields: generalized Hopf bifurcations, J. Differential Equations 14 (1973), 476–493;
- [Th1] R. Thom, Ensembles et morphismes stratifies. Bull. Amer. Math. Soc. 75, (1969), 240–284;
- [Th2] R. Thom, Propriété Différentielle Locales des Ensembles Analytiques, Seminaire Bourbaki, 1964/65, exp. 281;
- [Tr] S. Trifonov, Desingularization in Families of Analytic Differential Equations, Amer. Math. Soc. Transl, Ser.2, 165, (1995), 97–129;
- [V] A. Varchenko, Estimation of the number of zeros of an abelian integral depending on a parameter, and limit cycles, Func. Anal and Appl. 18, (1984), no.2, 14–25;
- [Wa] T. Wall, Regular Stratifications, Lecture Notes in Mathematics, No. 468, 332-344;
- [Wh] H. Whitney, Tangents to an Analytic Variety, Ann. of Math. 81, (1965), 496–549.
- [Y] Y. Yomdin, A quantitative version of the Kupka-Smale Theorem, Ergod. Th. Dynam. Sys. bf 5, (1985), 449–472.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
