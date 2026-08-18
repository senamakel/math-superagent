<!-- source: https://arxiv.org/html/math/0010174 | converted from HTML -->

The Hilbert 16-th problem and an estimate for cyclicity of an elementary polycycle

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0010174v1 [math.DS] 17 Oct 2000

# The Hilbert 16-th problem and an estimate for cyclicity of an elementary polycycle Thanks: The first author is partially supported by the Sloan Dissertation Fellowship and the American Institute of Mathematics Five-year Fellowship

V.Kaloshin Address: Fine Hall, Princeton University, Princeton, NJ, 08540 Email address: [kaloshin@math.princeton.edu][3]

## 1. Introduction

Consider a polynomial line field on the real ( x, y) (x,y) -plane

(1) |  | d ​ y d ​ x = P n ​ ( x, y) Q n ​ ( x, y), P n, Q n − polynomials , deg ⁡ P n, Q n ≤ n. \displaystyle\frac{dy}{dx}=\frac{P_{n}(x,y)}{Q_{n}(x,y)},\ P_{n},Q_{n}-{\text{ polynomials }},\deg P_{n},Q_{n}\leq n. |  |

 | H ( n) = uniform bound for the number of limit cycle of ( 1). \displaystyle H(n)=\boxed{\text{uniform bound for the number of limit cycle of}\ (\ref{H}).} |  |

One way to formulate the Hilbert 16-th Problem is the following:

Hilbert 16-th Problem (HP). Find an estimate for H ⁡ ( n) H(n) for any n ∈ ℤ + n\in\mathbb{Z}_{+}.

We shall discuss problems related to the following:

Existential Hilbert 16-th Problem (EHP). Prove that H ⁡ ( n) < ∞ H(n)<\infty for any n ∈ ℤ + n\in\mathbb{Z}_{+}.

The problem about finiteness of number of limit cycles for an individual polynomial line field ( 1) is called Dulac problem since the pioneering work of Dulac who claimed in 1923 to solve this problem, but an error was found by Ilyashenko.

The Dulac problem was solved by two independent and rather different proofs given almost simultaneously by Ilyashenko [I] and Ecalle [E]. However, both proofs do not allow any generalization to solve Existential Hilbert Problem.

Consider the equation ( 1) for different polynomials ( P n ​ ( x, y), Q n ​ ( x, y)) (P_{n}(x,y),Q_{n}(x,y)) as the family of line fields on ℝ 2 \mathbb{R}^{2} depending on parameters of the polynomials. Using a central projection π: 𝕊 2 → ℝ 2 \pi:\mathbb{S}^{2}\to\mathbb{R}^{2} and homogenuity with respect to parameters of the equation ( 1) (line fields λ ​ P n ​ ( x, y) / λ ​ Q n ​ ( x, y) \lambda P_{n}(x,y)/\lambda Q_{n}(x,y) and P n ​ ( x, y) / Q n ​ ( x, y) P_{n}(x,y)/Q_{n}(x,y) for any λ ≠ 0 \lambda\neq 0 are the same) one can construct a finite parameter family of analytic line fields on the shpere 𝕊 2 \mathbb{S}^{2} with a compact parameter base B B (see e.g. [IY2] for details). After this reduction Existential Hilbert Problem becomes a particular case of the following

Global Finiteness Conjecture (GFC). (see e.g. [R]) For any family of line fields on 𝕊 2 \mathbb{S}^{2} with a compact parameter base B B the number of limit cycles is uniformly bounded over all parameter values.

We refer the reader to the volumes [S] and [IY2] where various development of these and related problems are discussed. Families of analytic fields are extremely difficult to analyze. In the middle of 80’s Arnold [AAI] proposed to consider generic families of smooth vector fields on 𝕊 2 \mathbb{S}^{2}. A smooth analog of Global Finiteness Conjecture is the following

Hilbert-Arnold Problem (HAP). (e.g. [IY2]) Prove that in a generic finite parameter of vector fields on the sphere S 2 S^{2} with compact base B B, the number of limit cycles is uniformly bounded.

Assume for a moment that a polynomial (or a generic smooth) vector field on the sphere § 2 \lx@sectionsign^{2} has an infinite number of limit cycles. By the Poincare-Bendixon Theorem, any limit cycle should surround an equilibrium point and, since our vector field has at most finitely many equilibria, there should be an infinite “nested” sequence around one of equilibria. Then those “nested” limit cycles have to accumulate (in the sense of Hausdorff metric) to a certain contour (polygon) consisting of equilibria (as vertices) and separatric curves (sides of that polygon) connecting them. Such objects are called polycycles. It turns out that a possible solution to Hilbert-Arnold Problem reduces to investigation of bifurcation of polycycles. Let us give several definitions.

###### Definition 1.

A polycycle γ \gamma of a vector field on the sphere 𝕊 2 \mathbb{S}^{2} is a cyclically ordered collection of equilibrium points p 1, …, p k p_{1},\dots,p_{k} (with possible repetitions) and different arcs γ 1, …, γ k \gamma_{1},\dots,\gamma_{k} (integral curves of the vector field) connecting them in the specific order: the j-th arc γ j \gamma_{j} connects p j p_{j} with p j + 1 p_{j+1} for j = 1, …, k j=1,\dots,k.

###### Definition 2.

Let { x ˙ = v ( x, ϵ) } ϵ ∈ B n, x ∈ 𝕊 2, \{\dot{x}=v(x,\epsilon)\}_{\epsilon\in B^{n}},\ x\in\mathbb{S}^{2}, be an n n -parameter family of vector fields on 𝕊 2 \mathbb{S}^{2} having a polycycle γ \gamma for the critical parameter value ϵ ∗ \epsilon_{*}. The polycycle γ \gamma has cyclicity μ \mu in the family { v ⁡ ( x, ϵ) } ϵ ∈ B n \{v(x,\epsilon)\}_{\epsilon\in B^{n}} if there exist neighborhoods U U and V V such that 𝕊 2 ⊇ U ⊃ γ, B ⊇ V ∈ ϵ ∗ \mathbb{S}^{2}\supseteq U\supset\gamma,\ B\supseteq V\in\epsilon_{*} and for any ϵ ∈ V \epsilon\in V the field v ⁡ ( ⋅, ϵ) v(\cdot,\epsilon) has no more than μ \mu limit cycles inside U U and μ \mu is the minimal number with this property.

Examples 1) In a generic n n -parameter family, the maximal multiplicity of a degenerate limit cycle does not exceed n + 1 n+1, e.g. in codimension 1 1 a semistable limit cycle has cyclicity 2 2. Thus, the cyclicity of a trivial polycycle (a polycycle without singular points) in a generic n n -parameter family does not exceed n + 1 n+1.

2) (Andronow-Leontovich, 1930s; Hopf, 1940s). A nontrivial polycycle of codimension 1 1 has cyclicity at most 1 1.

3) (Takens, Bogdanov, Leontovich, Mourtada, Grozovskii, early 1970s-1993 (see [G], [KS] and references there)). A nontrivial polycycle of codimension 2 2 has cyclicity at most 2 2.

###### Definition 3.

The bifurcation number B ⁡ ( k) B(k) is the maximal cyclicity of a nontrivial polycycle occurring in a generic k k -parameter family.

The definition of B ⁡ ( k) B(k) does not depend on a choice of the base of the family, it depends only on the number k k of parameters.

Local Hilbert-Arnold Problem (LHAP) e.g. [IY1] Prove that for any finite k k, the bifurcation number B ⁡ ( k) B(k) is finite and find an upper estimate for B ⁡ ( k) B(k).

It turns out that a solution to Local Hilbert-Arnold Problem implies a solution to Hilbert-Arnold Problem.

Similarly to the generic smooth vector fields, in the case of analytic vector fields one can define so-called a limit periodic set [FP], [R], [IY1], which is either a polycycle or has an arc of equilibrium points 1 1 1 generic vector fields can not have an arc of equilibrium points, and formulate

Local Finiteness Conjecture (LFC) e.g. [R] Prove that any limit periodic set occuring in an analytic family of vector fields on § 2 \lx@sectionsign^{2} has finite cyclicity in this family.

Smooth vector fields are more flexible then analytic vector fields and easier to analyze. A strategy to attack Existential Hilbert Problem proposed by Arnold [AAI] (see also [IK]) is first understand generic smooth vector fields and then try to apply developed methods to analytic vector fields. Let us summarize the discussion in the form of diagramm:

[image: Refer to caption] Figure 1.

Now we shall formulate the Main Result of the paper.

###### Definition 4.

A singular (equilibrium) point of a vector field on the two-sphere is called elementary if at least one eigenvalue of its linear part is nonzero. A polycycle is called an elementary polycycle if all its singularities are elementary.

The Local Hilbert-Arnold problem was solved under the additional assumption that a polycycle have elementary singularities only.

###### Definition 5.

The elementary bifurcation number E ⁡ ( k) E(k) is the maximal cyclicity of a nontrivial elementary polycycle occurring in a generic k k -parameter family.

From examples 2) and 3) above it follows that

 | E ⁡ ( 1) = 1, E ⁡ ( 2) = 2. E(1)=1,\quad E(2)=2. |  |

Information about behavior of the function k ↦ E ⁡ ( k) k\mapsto E(k) has been obtained recently. The First crucial step was done by Ilyashenko and Yakovenko:

Finiteness Theorem (Ilyashenko and Yakovenko [IY3]) For any n n the elementary bifurcation number E ⁡ ( n) E(n) is finite.

###### Corollary 1.

Under the assumption that families of vector fields have elementary singularities only the global Hilbert-Arnold conjecture is solved, i.e. any generic finite parameter family of vector fields on the sphere 𝕊 2 \mathbb{S}^{2} with a compact base and only elementary singularities has a uniform upper bound for the number of limit cycles.

Main Theorem. For any k ∈ ℤ + k\in\mathbb{Z}_{+}

(2) |  | E ⁡ ( k) ≤ 2 25 ​ k 2. \displaystyle E(k)\leq 2^{25k^{2}}. |  |

This is the first known sufficiently general estimate for cyclicity of polycycle. The case of a polycycle consisting only one singular point with no arcs at all, is well known. An elementary equilibrium point can generate limit cycles in its small neighborhood if it is a slow focus, that is the linearization matrix has a pair of two imaginary eigenvalues. This bifurcation was investigated by Takens [Ta].

###### Corollary 2.

Under the assumption that all the polycycles are elementary the Main Theorem gives a solution to the Local Hilbert-Arnold problem.

The Main Theorem is an improvement of Ilyashenko-Yakovenko Finiteness Theorem. It is a great pleasure for the author to say that the paper of Ilyashenko-Yakovenko [IY3] was a corner stone for the present paper. In [IY3] the authors made an extremely important step: they found a pass from bifurcation theory to singularity theory using the Khovanskii reduction method [Kh]. We follow this pass up to some point and using some new ideas getting the first sufficiently general estimate for the cyclicity of polycycles. To make this paper readable we have to reproduce some points from [IY3] and we are sorry for repetition, but we think that it is necessary for a better understanding.

### 1.1. Three stages of the proof

The proof of the Main Theorem consists of three steps. Relation to the proof of the Finiteness Theorem [IY3] is discussed after this short description.

Step 1. Normal forms for local families of vector fields and their integration In section 2 we use normal forms to establish an explicit form for the Poincare correspondence map near equilibrium points on the polycycle under consideration. In [IY3] it is shown that these maps satisfy Pfaffian (polynomial differential) equations with coefficient of polynomials depending smoothly on the parameters of the family. As the result a basic system of equations for determination of limit cycles is obtained.

Step 2. the Khovanskii reduction method In section 3 we discuss a variation of the Khovanskii method [Kh]. This method allows us to investigate systems of equations that involve functions satisfying Pfaffian equations. In section 4 we present a formal reduction from the basic system to a mixed functional-Pfaffian system which is done in [IY3] together with upper bounds for degrees of involved into the procedure polynomials. After application of the Khovanskii method to the mixed functional-Pfaffian system we obtain several chain maps, the maps of the form

(3) |  | x ↦ ( P 1, …, P n) ∘ ( x, f ⁡ ( x), f ′ ​ ( x), …, f ( n) ​ ( x)), \displaystyle x\mapsto(P_{1},\dots,P_{n})\circ(x,f(x),f^{\prime}(x),\dots,f^{(n)}(x)), |  |

where P = ( P 1, …, P n) P=(P_{1},\dots,P_{n}) is a vector-polynomial given by its coordinate functions of known degree and f f is a generic function. The problem of estimating the number of limit cycles reduces to estimating the number of regular preimages of some special points by the chain map. Special points form an open cone-like semialgebraic set K K in the image.

Denote by F F the map F: x ↦ P ∘ ( x, f ⁡ ( x), f ′ ​ ( x), …, f ( n) ​ ( x)) F:x\mapsto P\circ(x,f(x),f^{\prime}(x),\dots,f^{(n)}(x)) which is called the n n -th jet of f f. Denote by L F L_{F} the linearization of F F at point x = 0 x=0.

Step 3. Bezout’s theorem for the Chain maps In section 5 we construct an algebraic set Σ \Sigma in the image of F F (in the space of n n -jets). If F F is transversal to Σ \Sigma, then the number of preimages of any point a a from a set of special points K K is the same for F F and its linearization L F L_{F} at zero, namely,

(4) |  | #⁡ { x: P ∘ F ⁡ ( x) = a } = #⁡ { x: P ∘ L F ​ ( x) = a } ≤ ∏ j = 1 k deg ⁡ P j. \displaystyle\#\{x:P\circ F(x)=a\}=\#\{x:P\circ L_{F}(x)=a\}\leq\prod_{j=1}^{k}\deg P_{j}. |  |

But L F L_{F} is a linear map and one can apply Bezout’s theorem to estimate the right-hand side of the equality. This observation completes the proof of the Main Theorem.

Let us discuss relation of this proof to the proof of the Finiteness Theorem by Ilyashenko & Yakovenko [IY3]. Step 1 of both proof is the same. We just refer to appropriate statements in [IY3]. Step 2 in this proof is slightly different for the one in [IY3]. After application of the Khovanskii method they obtain the same collection of chain maps of the form ( 3). However, they investigate the number of regular preimages of points in the image by the chain maps without any restriction on those points. In the present proof, using additional arguments in the Khovanskii method, we reduce consideration to only preimages of special points, i.e. points from a tiny cone-like set in the image. At his point our proof goes independently, because investigation of the number of regular preimages of special points is more concrete problem.

Let us present a more detailed description of each step of the proof.

### 1.2. Normal forms of local families and their integration

This step is done in [IY3] § ​ 0.3 \lx@sectionsign 0.3 and § ​ 1 \lx@sectionsign 1. We just say several words about it.

It turns out that in a small neighborhood of an elementary equilibrium point there exists a finitely differentiable normal coordinates (in the Cartesian product of the phase space and the parameter space), so-called normal forms of an equilibrium point. The list of finitely differentiable normal forms was obtained in [IY1]. The main feature of the list: all normal forms are polynomial and integrable. The smaller the neighborhood of a normal form, the higher its smoothness. So smoothness can be chosen arbitrary large. All normal forms are summarized in Table 1 sect. 2.

In a small neighborhood of an elementary equilibrium point one can choose two small segments, say Σ − \Sigma^{-} and Σ + \Sigma^{+}, transversal to the vector field for the critical value of parameter and explicitly calculate the Poincare (correspondence) map which maps a point from one segment say Σ − \Sigma^{-} along the corresponding phase curve to a point from the other segment Σ + \Sigma^{+} (see Fig.1). For an appropriate choice of segments Σ −, Σ + \Sigma^{-},\Sigma^{+} and coordinate functions x, x, in Σ −, Σ + \Sigma^{-},\Sigma^{+} respectively, and a smooth function λ ⁡ ( ϵ) \lambda(\epsilon) in the original parameter ϵ \epsilon of the family the Poincare return map Δ ϵ: x → y \Delta_{\epsilon}:x\to y can be explicitly computed. Moreover, there is a Pfaffian (with polynomial coefficients) 1-form ω \omega of the form

(5) |  | P ⁡ ( x, y, λ ⁡ ( ϵ)) ​ d ​ x + Q ⁡ ( x, y, λ ⁡ ( ϵ)) ​ d ​ y = 0 \displaystyle P(x,y,\lambda(\epsilon))\ dx+\ Q(x,y,\lambda(\epsilon))\ dy=0 |  |

which vanishes on the graph y = Δ ϵ ​ ( x) y=\Delta_{\epsilon}(x). For example, in the case of a nonresonant saddle Δ ϵ ​ ( x) = x λ ⁡ ( ϵ) \Delta_{\epsilon}(x)=x^{\lambda(\epsilon)} and ω = x ​ d ​ y + λ ⁡ ( ϵ) ​ y ​ d ​ x \omega=x\ dy+\ \lambda(\epsilon)y\ dx. See Table 1 for the other cases.

[image: Refer to caption] Figure 2. Construction of entrance and exit transversals

### 1.3. Singular-regular systems determining the number of limit cycles

We present a description of a system of equations determining the number of limit cycles. For a detailed description we refer to [IY3] § ​ 0.4 \lx@sectionsign 0.4 and § ​ 1.4 \lx@sectionsign 1.4.

Let γ \gamma be a polycycle, occurring in a generic k k parameter family, with equilibrium points p 1, …, p n p_{1},\dots,p_{n} (possibly with repetitions) and connecting phase curves γ 1, …, γ n \gamma_{1},\dots,\gamma_{n} such that γ j \gamma_{j} connects equilibria p j p_{j} with p j + 1 p_{j+1} respectively. For each 1 ≤ j ≤ n 1\leq j\leq n endow the point p j p_{j} with a C r C^{r} -normal coordinate charts U j U_{j}. Consider transversal segments “entrance” Σ j − \Sigma^{-}_{j} and “exit” Σ j + \Sigma^{+}_{j} which are parallel to coordinate axis of the normal chart. The phase curve γ j − 1 \gamma_{j-1} enters the neighborhood U j U_{j} through Σ j − \Sigma^{-}_{j} and the phase curve γ j \gamma_{j} exists U j U_{j} through Σ j + \Sigma^{+}_{j}. The normal coordinates induce coordinates x j x_{j} and y j y_{j} on Σ j − \Sigma^{-}_{j} and Σ j + \Sigma^{+}_{j} respectively. For some parameter values the corresponding vector field defines the following collection of Poincare maps:

(6) |  | Δ j ( ⋅, ϵ): x j → y j = Δ j ( x j, ϵ), j = 1, …, n f j ( ⋅, ϵ): y j → x j + 1 = f j ( y j, ϵ), j = 1, …, n ( mod n), \displaystyle\begin{aligned} \Delta_{j}(\cdot,\epsilon):x_{j}\to y_{j}=\Delta_{j}(x_{j},\epsilon),\ j=1,\dots,n\\ f_{j}(\cdot,\epsilon):y_{j}\to x_{j+1}=f_{j}(y_{j},\epsilon),\ j=1,\dots,n\ \ (\mod n),\end{aligned} |  |

where Δ j ​ ( ⋅, ϵ) \Delta_{j}(\cdot,\epsilon) is a local Poincare map form the “entrance”segment Σ j − \Sigma^{-}_{j} to the “exit” segment Σ j + \Sigma^{+}_{j} and f j ​ ( ⋅, ϵ) f_{j}(\cdot,\epsilon) is a semilocal Poincare map along the phase curve γ j \gamma_{j} form the “exit” segment Σ j + \Sigma^{+}_{j} to the “entrance” segment Σ j + 1 − \Sigma^{-}_{j+1}.

Now we decompose the monodromy map (the Poincare first return map) along the polycycle γ \gamma into the chain of the local singular maps Δ j \Delta_{j} and the semilocal regular maps f j f_{j} of the total length 2 ​ n 2n. Limit cycles correspond to the fixed points of the monodromy. But instead of writing one equation for the fixed points of the monodromy we consider a system of 2 ​ n 2n equations, which will be called the preliminary basic system:

(7) |  | { y j = Δ j ​ ( x j, ϵ) j = 1, …, n x j + 1 = f j ( y j, ϵ), j = 1, …, n ( mod n) \displaystyle\begin{cases}y_{j}=\Delta_{j}(x_{j},\epsilon)\quad j=1,\dots,n\\ x_{j+1}=f_{j}(y_{j},\epsilon),\ j=1,\dots,n\ (\mod n)\end{cases} |  |

Recall that x j x_{j} ’s are C r C^{r} -normal coordinates on Σ j − \Sigma_{j}^{-} and y j y_{j} ’s are C r C^{r} -normal coordinates on Σ j + \Sigma_{j}^{+}. Thus the system involves C r C^{r} -smooth regular functions f j f_{j} ’s and the maps Δ j \Delta_{j} from the list (modulo reparametrization ϵ → λ ⁡ ( ϵ) \epsilon\to\lambda(\epsilon)), that are essentially singular. The problem now is to estimate the number of solutions uniformly over all sufficiently small parameter values.

### 1.4. The Khovansky reduction method.

The system ( 7) is not easy to analyze, because it has the singular functions Δ j \Delta_{j}. The first key idea of the second step is to replace these singular equations in ( 7) by the Pfaffian (polynomial differential) equations in the form ( 5). As a result we obtain the mixed functional-Pfaffian system of the form

(8) |  | { ω j = 0 F j ​ ( x, y, ϵ) = 0 j = 1, …, n ω j = P j ​ d ​ x j + Q j ​ d ​ y j, F j ​ ( x, y, ϵ) = x j + 1 − f J ​ ( y j, ϵ) ( x, y) = ( x 1, y 1, …, x n, y n) ∈ ( ℝ 2 ​ n, 0), ϵ ∈ ( ℝ k, 0), \displaystyle\begin{aligned} \begin{cases}\omega_{j}=0\\ F_{j}(x,y,\epsilon)=0\quad\quad\quad j=1,\dots,n\quad\end{cases}\\ \omega_{j}=P_{j}\ dx_{j}+Q_{j}\ dy_{j},\quad F_{j}(x,y,\epsilon)=x_{j+1}-f_{J}(y_{j},\epsilon)\\ (x,y)=(x_{1},y_{1},\dots,x_{n},y_{n})\in(\mathbb{R}^{2n},0),\ \epsilon\in(\mathbb{R}^{k},0),\end{aligned} |  |

where ω j \omega_{j} are Pfaffian forms in the form ( 5). This system can be interpreted as follows: one has to take an integral manifold Γ \Gamma for the Pfaffian equations of the system ( 8) and compute its intersection with the level set ℱ − 1 ​ ( 0) \mathcal{F}^{-1}(0), where F: ( ℝ 2 ​ n, 0) → ℝ n F:\ (\mathbb{R}^{2n},0)\to\mathbb{R}^{n} is the map with the coordinate functions F j F_{j}. In order to estimate number of isolated solutions to ( 7) one needs to estimate the number of isolated points in the intersection. It turns out that it is sufficient to analyze only transversal intersections of Γ \Gamma with a generic level set F − 1 ​ ( b) F^{-1}(b) for b b sufficiently close to the origin in ℝ n \mathbb{R}^{n}. Since the integral manifold and the level sets have complimentary dimensions, a transversal intersection always consists of isolated points, which we call regular solutions to the system ( 8). What we are interested in is the upper estimate for their number, uniform over all the integral manifolds Γ \Gamma and all sufficiently small values of the parameters.

The method suggested by A. Khovanski [Kh] allows us to replace a mixed functional-Pfaffian system of the form ( 8) by the two systems of a similar form, but containing n − 1 n-1 Pfaffian equations, n n “simple” functional equations, and one special functional equation: the number of regular solutions to the initial equation is bounded from above by the sum of the number of regular solutions to these two auxiliary systems.

### 1.5. a P a_{P} -stratification and Bezout’s theorem for a chain map P ∘ F P\circ F with a generic F F.

In this section we shall discuss the formula ( 4). The problem of estimating the maximal number of small isolated preimages is equally difficult for a chain map P ∘ F: ℝ n → ℝ n P\circ F:\mathbb{R}^{n}\to\mathbb{R}^{n} with a generic map F: ℝ n → ℝ N F:\mathbb{R}^{n}\to\mathbb{R}^{N}, N ≥ n N\geq n and for a chain map P ∘ j n ​ F: ℝ n → ℝ n P\circ j^{n}F:\mathbb{R}^{n}\to\mathbb{R}^{n} with the n n -jet of a generic map. We shall show that if the map F F (resp. j n ​ F j^{n}F) satisfies a transversality condition in an appropriate space, then F F (resp. j n ​ F j^{n}F) can be replaced by its linear part and we can apply the Bezout theorem to estimate the maximal number of small inverse images of the chain P ∘ F P\circ F (resp. P ∘ j n ​ F P\circ j^{n}F) uniformly over all sequences of numbers ϵ 1, …, ϵ n \epsilon_{1},\dots,\epsilon_{n} decreasing sufficiently fast to 0 0. So, to simplify notations we shall consider a chain map of the form P ∘ F: ℝ n → ℝ n P\circ F:\mathbb{R}^{n}\to\mathbb{R}^{n}.

#### 1.5.1. A Heuristic description

Consider a chain map P ∘ F: ℝ 2 → ℝ 2 P\circ F:\mathbb{R}^{2}\to\mathbb{R}^{2}, where F: ℝ 2 → ℝ N F:\mathbb{R}^{2}\to\mathbb{R}^{N} is a generic C k C^{k} smooth map, k > 2 k>2 and P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} is a polynomial of degree d d. Fix a small positive r r. We would like to estimate the maximal number of small preimages

(9) |  | #{ x ∈ B r ( 0): P 1 ∘ F ( x) = ϵ, P 2 ∘ F ( x) = 0 } \displaystyle\#\{x\in B_{r}(0):\ P_{1}\circ F(x)=\epsilon,\ P_{2}\circ F(x)=0\} |  |

for a small enough ϵ \epsilon.

To show the idea put N = 3 N=3, P 1 ​ ( x, y, z) = x 2 + y 2 P_{1}(x,y,z)=x^{2}+y^{2}, and P 2 ​ ( x, y, z) = x ​ y P_{2}(x,y,z)=xy. Assume also that F ⁡ ( 0) = 0 F(0)=0. Denote the level set by V ϵ = { P 1 = ϵ, P 2 = 0 } V_{\epsilon}=\{P_{1}=\epsilon,\ P_{2}=0\}. The level set V ϵ V_{\epsilon} for ϵ > 0 \epsilon>0 consists of 4 4 parallel lines (see Figure 2).

Notice that in our notation the number of intersections of F ​ ( B r ​ ( 0)) F(B_{r}(0)) with V ϵ V_{\epsilon} equals the number of preimages of the point ( ϵ, 0) (\epsilon,0) ( 9).

It is easy to see from Figure 2 that if F F is transversal to V 0 V_{0} it is transversal to V ϵ V_{\epsilon} for any small ϵ > 0 \epsilon>0. Moreover, the number of intersections F ​ ( B r ​ ( 0)) F(B_{r}(0)) with V ϵ V_{\epsilon} equals 4 (see the points P 1, …, P 4 P_{1},\dots,P_{4} in Figure 2).

Another way to calculate the same number is as follows. Let us replace F F by its linear part L F L_{F} at zero. Then #{ x ∈ B r ( 0): P 1 ∘ F ( x) = ϵ, P 2 ∘ F ( x) = 0 } = #{ x ∈ B r ( 0): P 1 ∘ L F ( x) = ϵ, P 2 ∘ L F ( x) = 0 } \#\{x\in B_{r}(0):\ P_{1}\circ F(x)=\epsilon,\ P_{2}\circ F(x)=0\}=\#\{x\in B_{r}(0):\ P_{1}\circ L_{F}(x)=\epsilon,\ P_{2}\circ L_{F}(x)=0\} and solving this polynomial system also yields 4 4.

[image: Refer to caption] Figure 3. The Idealistic Example

The idea behind this picture is the following: Consider an arbitrary N N and a polynomial P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} of degree at most d d, N > 2 N>2. Define the semialgebraic variety V ϵ = ( P 1, P 2) − 1 ​ ( ϵ, 0) V_{\epsilon}=(P_{1},P_{2})^{-1}(\epsilon,0) as the level set.

Assume for simplicity that for any small ϵ ≠ 0 \epsilon\neq 0 the level set V ϵ V_{\epsilon} is a manifold of codimension 2. We shall get rid of this assumption later (see Theorem 37 b)). It turns out that there exists a stratification of V 0 V_{0} by semialgebraic strata ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) (a decomposition of V 0 V_{0} into a disjoint union of semialgebraic sets see definition 30), depending on P P only, such that

(10) |  | F ​ is transversal to ​ ( V 0, 𝒱 0) ⟹ F ​ is transversal to ​ V ϵ \boxed{F\ \text{is transversal to}\ (V_{0},\mathcal{V}_{0})}\implies\boxed{F\ \text{is transversal to}\ V_{\epsilon}} |  |

Condition ( 10) is written for n = 2 n=2. Below we shall use its analogue for an arbitrary n n. Let us present the key Proposition below and the simple of proof of it. This proof gives an insight to the main idea of the third step.

###### Proposition 1.

Let B r ​ ( a) B_{r}(a) be the r r -ball centered at the point a ∈ ℝ 2 a\in\mathbb{R}^{2} and let L F, a L_{F,a} denote the linearization of F F at the point a a. Under condition ( 10), the number of intersections of the image F ​ ( B r ​ ( a)) F(B_{r}(a)) with V ϵ V_{\epsilon} coincides with the number of intersections of the image L F, a ​ ( B r ​ ( a)) L_{F,a}(B_{r}(a)) with V ϵ V_{\epsilon}, provided r r is small enough. That is

(11) |  | #⁡ { x ∈ B r ​ ( 0): ( P 1, P 2) ∘ F ⁡ ( x) = ( ϵ, 0) } = #⁡ { x ∈ B r ​ ( 0): ( P 1, P 2) ∘ L F, a ​ ( x) = ( ϵ, 0) }. \displaystyle\begin{aligned} \#\{x\in B_{r}(0):\ (P_{1},P_{2})\circ F(x)=(\epsilon,0)\}=\\ \#\{x\in B_{r}(0):\ (P_{1},P_{2})\circ L_{F,a}(x)=(\epsilon,0)\}.\end{aligned} |  |

The argument below is independent of the codimension of V ϵ V_{\epsilon}. We only need condition ( 10) and the fact that the codimension of V ϵ V_{\epsilon} coincides with the dimension of the preimage of a chain map P ∘ F P\circ F.

Proof Consider the 1 1 -parameter family of maps F t = t ​ F + ( 1 − t) ​ L F F_{t}=tF+(1-t)L_{F} deforming the linear part of F F into F F. Clearly, F 1 ≡ F F_{1}\equiv F and F 0 ≡ L F F_{0}\equiv L_{F}. Fix a small r > 0 r>0. Since, F F is transversal to V 0 V_{0} at 0 0 all F t F_{t} are transversal to V 0 V_{0} at 0 0. Condition ( 10) implies that for all small ϵ \epsilon and all t ∈ [0, 1] t\in[0,1] F t F_{t} is transversal to V ϵ V_{\epsilon}.

Therefore, the number of intersections of F t ​ ( B r ​ ( 0)) F_{t}(B_{r}(0)) with V ϵ V_{\epsilon} is independent of t t. Indeed, assume that #⁡ { F t 1 ​ ( B r ​ ( 0)) ∩ V ϵ } ≠ #⁡ { F t 2 ​ ( B r ​ ( 0)) ∩ V ϵ } \#\{F_{t_{1}}(B_{r}(0))\cap V_{\epsilon}\}\neq\#\{F_{t_{2}}(B_{r}(0))\cap V_{\epsilon}\} for some t 1 < t 2 t_{1}<t_{2}. Then as t 1 t_{1} increases to t 2 t_{2} there is a point t ∗ t^{*} where the number of intersections drops or jumps. At this point t ∗ t^{*} the condition of transversality of F t ∗ F_{t^{*}} and V ϵ V_{\epsilon} must fail. This completes the proof of the proposition.

## 2. Normal forms for local families and their applications.

In this section we present the functional–Pfaffian system whose number of solutions bounds from above the number of limit cycles. This system was obtained in [IY3].

### 2.1. Local families and polynomial normal forms

A local family of planar vector fields is the germ of a map,

 | v: ( ℝ 2, 0) × ( ℝ k, 0) → ( ℝ 2, 0), ( x, y, ϵ) ↦ v ⁡ ( x, y, ϵ). v:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to(\mathbb{R}^{2},0),\qquad(x,y,\epsilon)\mapsto v(x,y,\epsilon). |  |

A C r C^{r} -smooth conjugacy between two local families v v and w w of the above form is a map

 | H: ( ℝ 2, 0) × ( ℝ k, 0) → ( ℝ 2, 0), ( x, y, ϵ) ↦ H ⁡ ( x, y, ϵ), \displaystyle H:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to(\mathbb{R}^{2},0),\qquad(x,y,\epsilon)\mapsto H(x,y,\epsilon), |  |

such that

 | H ∗ ​ v ​ ( x, y, ϵ) = w ⁡ ( H ⁡ ( x, y, ϵ), ϵ), \displaystyle\ \ \ H_{*}v(x,y,\epsilon)=w(H(x,y,\epsilon),\epsilon), |  |

where H ∗ H_{*} stands for the Jacobian matrix with respect to the variables x, y x,y. (this definition does not yet allow for reparameterization of a local family). Two families are finitely differentiably equivalent, if for any r < ∞ r<\infty there exists a C r C^{r} -conjugacy between them. The two families v, w v,w are orbitally equivalent, if there exists the germ of a nonvanishing function ϕ: ( ℝ 2, 0) × ( ℝ k, 0) → ℝ 1 \phi:(\mathbb{R}^{2},0)\times(\mathbb{R}^{k},0)\to\mathbb{R}^{1} such that v v is equivalent to ϕ ⋅ w \phi\cdot w.

To allow for a reparameterization of local families, we say that a family v ⁡ ( ⋅, ϵ) v(\cdot,\epsilon) is induced from another family w ⁡ ( ⋅, λ), λ ∈ ( ℝ m, 0) w(\cdot,\lambda),\ \lambda\in(\mathbb{R}^{m},0), if v ⁡ ( ⋅, ϵ) = w ⁡ ( ⋅, λ ⁡ ( ϵ)) v(\cdot,\epsilon)=w(\cdot,\lambda(\epsilon)), where λ ⁡ ( ϵ) \lambda(\epsilon) is the germ of a smooth map ( ℝ k, 0) → ( ℝ m, 0) (\mathbb{R}^{k},0)\to(\mathbb{R}^{m},0). The number of new parameters m m may be different from k k.

Assume that the family w ⁡ ( ⋅, λ) w(\cdot,\lambda) is global (i.e. the expression w ⁡ ( x, y, λ) w(x,y,\lambda) makes sense for all ( x, y, λ) ∈ ℝ m + 2 (x,y,\lambda)\in\mathbb{R}^{m+2}); this happens in particular when w w is polynomial in all its arguments. Restricting the parameters λ \lambda onto a small neighborhood of a certain point ( 0, 0, 𝐜) ∈ ℝ 2 × ℝ m (0,0,{\bf c})\in\mathbb{R}^{2}\times\mathbb{R}^{m}, we obtain a localization of the global family w w, which formally becomes a local family after the parallel translation λ ↦ λ − 𝐜 \lambda\mapsto\lambda-\bf c.

###### Definition 6.

1. A local family v = v ⁡ ( ⋅, λ) v=v(\cdot,\lambda) is finitely smooth orbital versal unfolding (in short, versal unfolding) of the germ v ⁡ ( ⋅, 0) v(\cdot,0), if any other local family unfolding this germ is finitely differentiable orbitally equivalent to a family induced from v v.

2. A polynomial family w ⁡ ( ⋅, λ) w(\cdot,\lambda), λ ∈ ℝ m \lambda\in\mathbb{R}^{m}, is a global finitely smooth orbital versal unfolding (in short, global versal unfolding) for a certain class of local families of vector fields, if any local family from this class is finitely differentiable orbitally equivalent to a local family induced from some localization of w w.

To investigate a versal unfolding means to investigate at the same time all smooth local finite-parametric families which unfold the same germ v ⁡ ( ⋅, 0) v(\cdot,0). The main result describing versal unfoldings of germs of elementary singularities on the plane, is given by the following theorem.

###### Theorem 7.

[IY3] Suppose that a generic finite-parameter family of smooth vector fields on the plane possesses an elementary singular point for a certain value of the parameters. If this point has at least one hyperbolic sector, than the family is finitely differentiable orbitally equivalent to a family induced from some localization of one of the families given in the second column of Table 1.

Table 1. Unfolding of elementary equilibrium points on the plane.

Type | Normal forms | Poincare | Pfaffian equations |

 |  | Correspondence maps |  |

 | x ˙ = x, \dot{x}\ =\ x, |  |  |

S 0 S_{0} | y ˙ = − λ ​ y. \dot{y}\ =\ -\lambda y. | y = x λ, y=x^{\lambda}, | x ​ d ​ y − λ ​ y ​ d ​ x = 0 x\ dy\ -\lambda y\ dx\ =0 |

 |  | x > 0, y > 0 x>0,\ y>0 |  |

 | λ = λ 0 ∈ ℝ 1 \lambda=\lambda_{0}\in\mathbb{R}^{1} |  |  |

 | x ˙ = x ⁡ ( n m + P μ ​ ( u, λ)), \dot{x}\ =\ x\ \left(\frac{n}{m}+P_{\mu}(u,\lambda)\right), |  |  |

 | y ˙ = − y. \dot{y}\ =\ -y. |  |  |

S μ S_{\mu} |  | 0 = m ​ log ⁡ y + 0\ =\ m\log y\ + | y ​ P μ ​ ( y n, λ) ​ d ​ x − y\ P_{\mu}(y^{n},\lambda)\ dx\ - |

 | u = u ⁡ ( x, y) = x m ​ y n, u=u(x,y)=x^{m}\ y^{n}, | ∫ x m y n d ​ u u ​ P μ ​ ( u, λ). \int_{x^{m}}^{y^{n}}\frac{du}{uP_{\mu}(u,\lambda)}. | ( n m + P μ ( y n, λ)) × \left(\frac{n}{m}+P_{\mu}(y^{n},\lambda)\right)\times |

 | P μ ​ ( u, λ) = ± u μ ​ ( 1 + λ μ ​ u μ) P_{\mu}(u,\lambda)=\pm u^{\mu}(1+\lambda_{\mu}u^{\mu}) | x > 0, y > 0 x>0,\ y>0 | x ​ P μ ​ ( x m, λ) ​ d ​ y = 0 xP_{\mu}(x^{m},\lambda)\ dy=0 |

 | + W μ − 1 ​ ( u, λ), +W_{\mu-1}(u,\lambda), |  |  |

 | λ = ( λ 1, …, λ μ) \lambda=(\lambda_{1},\dots,\lambda_{\mu}) |  |  |

 | x ˙ = Q μ ​ ( x, λ), \dot{x}\ =\ Q_{\mu}(x,\lambda), |  |  |

 | y ˙ = − y. \dot{y}\ =\ -y. | y = C ⁡ ( λ) ​ x, y\ =\ C(\lambda)x, |  |

D μ c D^{c}_{\mu} |  | C = ∫ − 1 1 d ​ u Q μ ​ ( u, λ), C={\int_{-1}^{1}}\frac{du}{Q_{\mu}(u,\lambda)}, | x ​ d ​ y − y ​ d ​ x = 0 x\ dy\ -y\ dx=0 |

 | Q μ ​ ( x, λ) = ± x μ + 1 ​ ( 1 + λ μ ​ x μ) Q_{\mu}(x,\lambda)\ =\pm x^{\mu+1}(1+\lambda_{\mu}x^{\mu}) | x, y ∈ ℝ 1 x,\ y\ \in\mathbb{R}^{1} |  |

 | + W μ − 1 ​ ( x, λ), +W_{\mu-1}(x,\lambda), | 0 = log ⁡ y + 0=\ \log y\ + |  |

D μ h D^{h}_{\mu} | λ = ( λ 1, …, λ μ) \lambda=(\lambda_{1},\dots,\lambda_{\mu}) | ∫ x 1 d ​ u Q μ ​ ( u, λ) {\int_{x}^{1}}\frac{du}{Q_{\mu}(u,\lambda)} | Q μ ​ ( x, λ) ​ d ​ y − Q_{\mu}(x,\lambda)\ dy\ - |

 |  | y > 0, x ∈ ℝ 1 y>0,\ x\ \in\mathbb{R}^{1} | y ​ d ​ x = 0 y\ dx\ =0 |

In what follows the following notation for elementary equilibria (the subscript indicates the degree of degeneracy):

S 0 S_{0} — Nonresonant saddle;

S μ S_{\mu} — Resonant saddle whose quotient equation (the differential equation for u = x m ​ y n u=x^{m}\ y^{n} below) has the singular point of multiplicity μ + 1 \mu+1 at the origin, μ ≥ 1 \mu\geq 1; if we want to specify explicitly the resonance between the eigenvalues, we use the extended notation S μ ( n: m) S_{\mu}^{(n:m)} assuming that the natural numbers m, n m,n are mutually prime;

D μ D_{\mu} — Degenerate saddlenode of multiplicity μ \mu;

W μ − 1 ​ ( z, λ) = λ 0 + λ 1 ​ z + ⋯ + λ μ − 1 ​ z μ − 1 W_{\mu-1}(z,\lambda)=\lambda_{0}+\lambda_{1}z+\cdots+\lambda_{\mu-1}z^{\mu-1} is a Weierstrass polynomial of degree μ − 1 \mu-1.

Different technical remarks concerning this table see in [IY3] § ​ 1.1 \lx@sectionsign 1.1. We just briefly describe each column.

The first two columns do not need extra words. In the third column of the table the Poincare correspondence maps y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) for the polynomial normal forms are given. They are implicitly defined by the equations relating x x to y y, these equations depending explicitly on the parameters λ \lambda and thus implicitly on the original parameters ϵ \epsilon. The choice of segments transversal to the phase curves of the family described in fig. 1.

[image: Refer to caption] Figure 4. Poincare Correspondence maps

### 2.2. Basic system

Here we describe the system of equations which will be analyzed from now on. Assume that a polycycle occurs in a generic k k -parameter family of vector fields, and all the vertices of the polycycle are elementary.

Then the number n n of vertices is ≤ k \leq k. Moreover, one can claim that each vertex is of one of the types S μ j, μ j ≥ 0 S_{\mu_{j}},\ \mu_{j}\geq 0, or D μ j h, c, μ j ≥ 1 D_{\mu_{j}}^{h,c},\ \mu_{j}\geq 1, and ∑ μ j ≤ k \sum\mu_{j}\leq k (see [IY3] § ​ 1.4 \lx@sectionsign 1.4).

Next, we proceed with introducing the normalizing C 𝗉 C^{\mathsf{p}} -smooth local coordinates near each elementary vertex, as this is described above (the exact order of smoothness will be specified later on). Then a pair of C 𝗉 C^{\mathsf{p}} -smooth transversals may be chosen near each vertex, and endowed with local C 𝗉 C^{\mathsf{p}} -smooth charts x j, y j x_{j},y_{j} in such a way that the correspondence map taking a point with a coordinate x j x_{j} on the “entrance” transversal to a point with the coordinate y j y_{j} on the “exit” transversal, will be of one of the standard types listed in Table 1.

More precisely, for each vertex j = 1, …, n j=1,\dots,n Theorem 7 yields the localization point 𝐜 j = ( 0, …, 0, c j) ∈ ℝ μ j + 1 {\bf c}_{j}=(0,\dots,0,c_{j})\in\mathbb{R}^{\mu_{j}+1}, where c j ∈ ℝ 1 c_{j}\in\mathbb{R}^{1} is the formal invariant of the unperturbed singular point, and also if j j -th vertex is a resonant saddle, then the rational hyperbolicity ratio n: m n:m is explicitly specified.

Denote by Δ l, μ ​ ( x, λ) \Delta_{l,\mu}(x,\lambda) the correspondence map for each of the four types of singularities from Table 1, l = S 0, S μ, D μ c l=S_{0},S_{\mu},D_{\mu}^{c} or D μ h D_{\mu}^{h}, with the corresponding index μ ∈ ℕ \mu\in\mathbb{N} (for l = S 0 l=S_{0} by definition μ = 0 \mu=0). In case S μ S_{\mu} with μ > 0 \mu>0 we consider the mutually prime pair of natural numbers as an additional parameter of the corresponding map, so in this case the rigorous notation would be Δ S μ, μ ​ ( x, λ, [n, m]) \Delta_{S_{\mu},\mu}(x,\lambda;[n,m]).

###### Definition 8.

1. The unspecified basic system for determination of limit cycles occurring in k k -parametric families of vector fields is the system of n n regular and n n singular functional equations in 2 ​ n 2n variables x j, y j x_{j},y_{j}, depending on parameters λ j, n j, m j, ϵ \lambda^{j},n_{j},m_{j},\epsilon,

(12) |  | { y j = Δ l j, μ j ( x j, λ j; [n j, m j]), λ j ∈ ℝ μ j + 1, x j + 1 = f j ( y j, ϵ), ϵ ∈ ( ℝ k, 0). j = 1, …, n mod ( n), l j ∈ { S 0, S μ, D μ c, D μ h }, n j, m j ∈ ℕ, μ j ∈ ℤ +, ∑ μ j ≤ k, n ≤ k, Δ depends on n j, m j ​ only if l j = S μ with μ > 0. \displaystyle\begin{aligned} \begin{cases}y_{j}\ \ =\Delta_{l_{j},\mu_{j}}(x_{j},\lambda^{j};[n_{j},m_{j}]),\qquad\lambda^{j}\in\mathbb{R}^{\mu_{j}+1},\\ x_{j+1}=f_{j}(y_{j},\epsilon),\qquad\epsilon\in(\mathbb{R}^{k},0).\end{cases}\\ j=1,\dots,n\mod(n),\quad l_{j}\in\{S_{0},S_{\mu},D_{\mu}^{c},D_{\mu}^{h}\},\\ n_{j},m_{j}\in\mathbb{N},\quad\mu_{j}\in\mathbb{Z}_{+},\quad\sum\mu_{j}\leq k,\quad n\leq k,\\ \Delta\ \ {\text{depends on}}\ \ n_{j},m_{j}\ {\text{only if}}\ \ l_{j}=S_{\mu}\ \ {\text{with}}\ \ \mu>0.\end{aligned} |  |

2. A specified basic system is one of a finite number of unspecified basic systems together with an explicit indication of specification, which by definition is the collection of:

∙ \bullet localization points 𝐜 j = ( 0, …, 0, c j) ∈ ℝ μ j + 1 {\bf c}_{j}=(0,\dots,0,c_{j})\in\mathbb{R}^{\mu_{j}+1}; in particular this means that hyperbolicity ratios of all nonresonant saddles are explicitly given;

∙ \bullet hyperbolicity ratios n j: m j n_{j}:m_{j} for all resonant saddles;

∙ \bullet smooth functions f j ​ ( x, ϵ) f_{j}(x,\epsilon) depending on the parameters ϵ \epsilon, are defined in some open neighborhoods ( ℝ k + 1, 0) j (\mathbb{R}^{k+1},0)_{j} and f j ​ ( 0, 0) = 0 f_{j}(0,0)=0;

∙ \bullet characteristic size, that is, the value r > 0 r>0 which determines the domain of the specified basic system as follows:

(13) |  | ( x, y) ∈ I r = { | x j | < r, | y j | < r, j = 1, …, n } ⊂ ℝ 2 ​ n; ( λ, ϵ) ∈ B r = { ‖ λ j − 𝐜 j ‖ < r, ‖ ϵ ‖ < r } ⊂ ℝ k + μ 1 + ⋯ + μ n, \displaystyle\begin{aligned} (x,y)\in I_{r}=\{|x_{j}|<r,\ |y_{j}|<r,\quad j=1,\dots,n\}\subset\mathbb{R}^{2n};\\ (\lambda,\epsilon)\in B_{r}=\{\|\lambda^{j}-{\bf c}_{j}\|<r,\ \|\epsilon\|<r\}\subset\mathbb{R}^{k+\mu_{1}+\cdots+\mu_{n}},\end{aligned} |  |

where λ \lambda is the tuple of all parameters of all normal forms from Table 1, λ = ( λ 1, …, λ n) \lambda=(\lambda^{1},\dots,\lambda^{n}); the characteristic size must be so small that all functions f j f_{j} were defined for the corresponding values of their arguments.

Notations related to definition 8 There is only a finite number of unspecified basic systems, each one being completely characterized by the string of discrete data

(14) |  | 𝒯 = ( l 1, μ 1, …, l n, μ n) \displaystyle\mathcal{T}=(l_{1},\mu_{1},\dots,l_{n},\mu_{n}) |  |

subject to the total restriction n ≤ k n\leq k, ∑ μ j ≤ k \sum\mu_{j}\leq k. We call the data 𝒯 \mathcal{T} the combinatorial type of the unspecified basic system.

The string

(15) |  | 𝒮 a = ( c 1, …, c n, …, m j α, n j α, …) ∈ ℝ n + 2 ​ s r > 0, c j ∈ ℝ 1, m j α, n j α ∈ ℕ, f j ∈ ℂ 𝗉 ( ℝ k + 1, 0). \displaystyle\begin{aligned} \mathcal{S}_{a}=(c_{1},\dots,c_{n},\dots,m_{j_{\alpha}},n_{j_{\alpha}},\dots)\in\mathbb{R}^{n+2s}\\ r>0,\ c_{j}\in\mathbb{R}^{1},\ m_{j_{\alpha}},n_{j_{\alpha}}\in\mathbb{N},\ f_{j}\in\mathbb{C}^{\mathsf{p}}(\mathbb{R}^{k+1},0).\end{aligned} |  |

will be referred to as the algebraic part of the specification (for reasons to be clarified later), while the string of functions

 | 𝒮 f = 𝐟 = ( f 1, …, f n) \mathcal{S}_{f}={\bf f}=(f_{1},\dots,f_{n}) |  |

is called the functional part of the specification. The functions f j f_{j} are defined on the domain I r × B r I_{r}\times B_{r}, where r r is the characteristic size introduced earlier.

Denote by ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟) \mathcal{B}(\mathcal{T},\mathcal{S}_{a},\bf f) the number of isolated solutions to the specified basic system ( 𝒯, 𝒮 a, 𝐟) (\mathcal{T},\mathcal{S}_{a},\bf f) in the domain I r 0 I_{r_{0}}. One can check that ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟) \mathcal{B}(\mathcal{T},\mathcal{S}_{a},\bf f) is defined in such a way that it bounds the cyclicity of the polycycle with such a specification.

After all these notions (or rather the language) being introduced, we may formulate the problem of estimating cyclicity of elementary polycycles occurring in generic k k -parametric families as follows.

###### Theorem 9.

For any type 𝒯 \mathcal{T} of unspecified basic system and any choice of the algebraic part 𝒮 a \mathcal{S}_{a} one may choose the order of smoothness 𝗉 0 \mathsf{p}_{0} and an open dense subset 𝖥 = 𝖥 𝒯, 𝒮 a, r 0 \mathsf{F}=\mathsf{F}_{\mathcal{T},\mathcal{S}_{a},r_{0}} in the space of C 𝗉 0 C^{\mathsf{p}_{0}} -smooth functions C 𝗉 0 ​ ( I r 0 × B r 0, ℝ n) C^{\mathsf{p}_{0}}(I_{r_{0}}\times B_{r_{0}},\mathbb{R}^{n}) such that for every 𝐟 = ( f 1, …, f n) ∈ 𝖥 {\bf f}=(f_{1},\dots,f_{n})\in\mathsf{F} and a sufficiently small characteristic size r 0 = r 0 ​ ( 𝐟) r_{0}=r_{0}(\bf f) the number of isolated solutions ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟, r 0) \mathcal{B}(\mathcal{T},\mathcal{S}_{a},{\bf f};r_{0}) to the specified basic system ( 𝒯, 𝒮 a, 𝐟) (\mathcal{T},\mathcal{S}_{a},\bf f) in the domain I r 0 I_{r_{0}} is uniformly bounded over all parameter values ( λ, ϵ) ∈ B r 0 (\lambda,\epsilon)\in B_{r_{0}}:

(16) |  | ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟, r 0) = sup ( ϵ, λ) ∈ B r 0 #⁡ { ( x, y) ​ satisfying ( 12), ( x, y) ∈ I r 0 } < 2 25 ​ k 2 \displaystyle\begin{aligned} \mathcal{B}(\mathcal{T},\mathcal{S}_{a},{\bf f};r_{0})=\sup_{(\epsilon,\lambda)\in B_{r_{0}}}\#\{(x,y)\ {\text{satisfying (\ref{1})}},\ (x,y)\in I_{r_{0}}\}<2^{25k^{2}}\end{aligned} |  |

and, therefore, E ⁡ ( k) ≤ 2 25 ​ k 2 E(k)\leq 2^{25k^{2}}.

## 3. The Khovanski reduction method.

In this section we describe the method of reducing a functional–Pfaffian system to a chain map of the form ( 3). The construction in its full generality is described in the book [Kh]. Our exposition relies on the one in [IY3], but has new important features so we can’t just refer to neither [Kh], nor [IY3].

### 3.1. Pfaffian systems and their separating solutions

Let M M be a smooth orientable n n -dimensional manifold, not necessarily compact or connected, and ω \omega be a smooth 1-form on it.

###### Definition 10.

A codimension 1 smooth submanifold Γ ⊂ M \Gamma\subset M is the separating solution for the Pfaffian equation ω = 0 \omega=0, if:

a) Γ \Gamma is the integral manifold, that is, the restriction of ω \omega on the tangent bundle of Γ \Gamma is identically zero:

 | ∀ x ∈ Γ, ∀ v ∈ T x ​ Γ ω ⁡ ( v) = 0; \displaystyle\forall x\in\Gamma,\ \forall v\in T_{x}\Gamma\quad\omega(v)=0; |  |

b) Γ \Gamma does not pass through singular points of ω \omega:

 | ∀ x ∈ Γ, ∃ v ∈ T x ​ M ω ⁡ ( v) | T x ​ M ≠ 0; \displaystyle\forall x\in\Gamma,\ \exists v\in T_{x}M\quad\omega(v)|_{T_{x}M}\neq 0; |  |

c) Γ \Gamma is the boundary of a domain D ⊆ M D\subseteq M and the coorientation induced on Γ \Gamma by ω \omega, coincides with its coorientation as the boundary. In other words, on any vector pointing outward from D D, the form is positive.

Let now ω 1, …, ω k \omega_{1},\dots,\omega_{k} be an ordered k k -tuple of smooth 1-forms on M M. Consider the system of Pfaffian equations

(17) |  | ω 1 = 0, …, ω k = 0. \displaystyle\omega_{1}=0,\quad\dots\quad,\omega_{k}=0. |  |

###### Definition 11.

A submanifold Γ \Gamma is the separating solution for the system of Pfaffian equations, if there exists an increasing chain of smooth submanifolds,

(18) |  | Γ = Γ k ⊂ Γ k − 1 ⊂ ⋯ ⊂ Γ 1 ⊂ Γ 0 = M \displaystyle\Gamma=\Gamma_{k}\subset\Gamma_{k-1}\subset\cdots\subset\Gamma_{1}\subset\Gamma_{0}=M |  |

such that for any j = 1, …, k j=1,\dots,k submanifold Γ j \Gamma_{j} is the separating solution for the Pfaffian equation on Γ j − 1 \Gamma_{j-1}, determined by the restriction of the form ω j \omega_{j} on the latter submanifold.

Let ℱ: M → ℝ s \mathcal{F}:M\to\mathbb{R}^{s} be a smooth map s < n − k s<n-k. Recall that a point a ∈ ℝ s a\in{\mathbb{R}}^{s} is called a regular value for the map ℱ \mathcal{F} if the linearization matrix, denoted by J ℱ ​ ( x) J_{\mathcal{F}}(x), has full rank for any x ∈ ℱ − 1 ​ ( y) x\in\mathcal{F}^{-1}(y). By the rank theorem the level set V a = ℱ − 1 ​ ( a) V_{a}=\mathcal{F}^{-1}(a) of a regular value is a smooth manifold of dimension n − s n-s.

We call a ∈ ℝ s a\in{\mathbb{R}}^{s} a regular value for ℱ \mathcal{F} with respect to Pfaffian equations ( 17) if a a is a regular value of F F and the k k -form Ω = ω 1 ∧ ⋯ ∧ ω k \Omega=\omega_{1}\wedge\dots\wedge\omega_{k}, restricted to V a V_{a} Ω | V a \Omega|_{V_{a}} is nondegenerate, i.e., singular points of Ω | V a \Omega|_{V_{a}} have measure zero.

Consider a pair of smooth maps ℱ: M → ℝ s \mathcal{F}:M\to{\mathbb{R}}^{s} and F: M → ℝ n − k − s F:M\to\mathbb{R}^{n-k-s}. Now we add to a Pfaffian system ( 17) two types of functional equations. The first type consists of functional equations ℱ = a \mathcal{F}=a, where a ∈ ℝ s a\in\mathbb{R}^{s} is a fixed regular value of ℱ \mathcal{F} with respect to a Pfaffian system ( 17). The second type consists of functional equations F = b F=b, where b ∈ ℝ n − k − s b\in\mathbb{R}^{n-k-s} is a variable. We call equations ℱ = a \mathcal{F}=a, with a fixed a ∈ ℝ s a\in{\mathbb{R}}^{s}, by rigid equations and F = b F=b, with a varying b ∈ ℝ n − s − 1 b\in{\mathbb{R}}^{n-s-1}, by loose equations.

###### Definition 12.

Let Ω = ( ω 1, …, ω k) ∈ ( Λ 1 ​ ( M)) k \Omega=(\omega_{1},\dots,\omega_{k})\in(\Lambda^{1}(M))^{k} be a k k -tuple of smooth 1-forms, ℱ: M → ℝ s \mathcal{F}:M\to{\mathbb{R}}^{s} and F: M → ℝ n − k − s F:M\to{\mathbb{R}}^{n-k-s} be smooth maps, and a ∈ ℝ s a\in{\mathbb{R}}^{s} be a regular value for ℱ \mathcal{F} with respect to the k k -tuple of smooth 1-forms. A solution to the mixed functional–Pfaffian system

(19) |  | Ω = 0, F = b, ℱ = a, b ∈ ℝ n − k − s \displaystyle\Omega=0,\quad F=b,\quad\mathcal{F}=a,\qquad b\in\mathbb{R}^{n-k-s} |  |

is a pair ( Γ a, L b) (\Gamma^{a},L_{b}), where L b ⊆ M L_{b}\subseteq M is the preimage F − 1 ​ ( b) F^{-1}(b) and Γ a \Gamma^{a} is a separating solution for the Pfaffian system Ω = 0 \Omega=0, restricted to V a V_{a}, and the intersection Γ a ∩ L b \Gamma^{a}\cap L_{b} is nonempty.

The solution is regular, if Γ a \Gamma^{a} is the separating solution for the restriction of Pfaffian equations to V a V_{a} and b b is the regular value for the restriction of the map G G on Γ a \Gamma^{a}. If OPEN ( Γ a, L b)) (\Gamma^{a},L_{b})) is a regular solution, then the intersection Γ a ∩ L b \Gamma^{a}\cap L_{b} is transversal and consists of isolated points.

###### Definition 13.

The Khovanski number 𝒦 ​ { Ω, F; ℱ = a } \mathcal{K}\{\Omega,F;\mathcal{F}=a\} for the mixed system ( 19) is the upper bound for the cardinalities #⁡ { Γ a ∩ L b } \#\{\Gamma^{a}\cap L_{b}\} over all regular solutions of the system.

Remarks 1. The Khovanski number is also defined if k = 0 k=0 (resp. s = 0 s=0), i.e., there are no Pfaffian (resp. rigid) equations at all. In this case one may put formally Γ = M \Gamma=M (resp. V a = M V_{a}=M), and 𝒦 ​ { ω, F; ℱ = a } \mathcal{K}\{\omega,F;\mathcal{F}=a\} (resp. 𝒦 ​ { Ω, F; ∅ } \mathcal{K}\{\Omega,F;\emptyset\}) is equal to the upper bound of the cardinality of preimages #⁡ { L b ∩ V a } \#\{L_{b}\cap V_{a}\} (resp. #​ { L b ∩ Γ } \#\{L_{b}\cap\Gamma\}) of regular values for the map G | V a: V a → ℝ n − k − s G|_{V_{a}}:V_{a}\to{\mathbb{R}}^{n-k-s}.

2. If we want to stress in the notation the phase space M M of the functional–Pfaffian system, we use the notation 𝒦 M ​ { Ω, F, ℱ = a } \mathcal{K}_{M}\{\Omega,F,\mathcal{F}=a\}. Usually this is necessary when F F, ℱ \mathcal{F}, and Ω \Omega are defined on the Euclidean space ℝ n {\mathbb{R}}^{n}, while we are interested only in solutions belonging to some (open) ball.

3. If we fix a coordinate system in ℝ n − k − s \mathbb{R}^{n-k-s}, denote by F 1, …, F s F_{1},\dots,F_{s} coordinate functions of the map F: M → ℝ n − k − s F:M\to\mathbb{R}^{n-k-s}, and introduce the ( n − k − s) (n-k-s) -tuple of 1 1 -forms Ω F = ( d ​ F 1, …, d ​ F s) \Omega_{F}=(dF_{1},\dots,dF_{s}), then we can consider the following mixed system

(20) |  | Ω = 0, Ω F = 0, ℱ = a. \displaystyle\Omega=0,\quad\Omega_{F}=0,\quad\mathcal{F}=a. |  |

Regularity in the definition of the Khovanski number 𝒦 ​ { Ω, F; ℱ = a } \mathcal{K}\{\Omega,F;\mathcal{F}=a\} implies that 𝒦 ⁡ { Ω, F; ℱ = a } = 𝒦 ⁡ { ( Ω, Ω F), ∅; ℱ = a } \mathcal{K}\{\Omega,F;\mathcal{F}=a\}=\mathcal{K}\{(\Omega,\Omega_{F}),\emptyset;\mathcal{F}=a\}.

The goal is using the Khovanski reduction principle estimate the Khovanski number for the mixed functional-Pfaffian system by a linear combination of the Khovanski number for some number of entirely rigid functional systems.

The first step of the reduction principle is to estimate the Khovanski number for a given mixed system by a linear combination of the Khovanski numbers of two auxiliary systems containing a reduced by one number of Pfaffian equations and an increased by one number of rigid equations.

The second step is using remark 3 replace all loose functional equations for pfaffian equations and apply the reduction principle to the mixed system consisting of ( n − s) (n-s) Pfaffian equations ( Ω, Ω F) (\Omega,\Omega_{F}) and s s rigid equations. Thus, after ( n − s) (n-s) steps of the reduction principle we obtain a finite collection of entirely rigid functional systems.

### 3.2. The Reduction principle for one Pfaffian equation

We show how to eliminate the Pfaffian equation from the mixed system with ( n − s − 1) (n-s-1) loose equations and s s rigid functional equations.

(21) |  | ω = 0, F = b, ℱ = a, F: M → ℝ n − s − 1, ℱ: M → ℝ s, \displaystyle\omega=0,\quad F=b,\quad\mathcal{F}=a,\qquad F:M\to\mathbb{R}^{n-s-1},\qquad\mathcal{F}:M\to\mathbb{R}^{s}, |  |

We shall outline only the key ideas.

###### Definition 14.

A smooth positive function ρ: M → ℝ + \rho:M\to\mathbb{R}_{+} is called covering, if it tends to zero along any nonaccumulating sequence of points in M M. In other terms, ρ \rho vanishes “at infinity” on M M, so that all level hypersurfaces of the covering function are compact subsets of M M.

###### Remark 1.

This definition applies both to compact and noncompact manifolds, but in the compact case a smooth function is covering if and only if it is everywhere positive, thus automatically bounded away from zero.

Suppose that the manifold M M is endowed with the Riemann volume. Since it is orientable, one may use the duality between functions and n n -forms on M M. Denote by the asterisk the operator taking an n n -form into the function (dividing by the volume form).

Fix Euclidean structures in ℝ n − s − 1 \mathbb{R}^{n-s-1} and ℝ s \mathbb{R}^{s}. Let F 1, …, F n − s − 1 F_{1},\dots,F_{n-s-1} and ℱ 1, …, ℱ s \mathcal{F}_{1},\dots,\mathcal{F}_{s} be the coordinate functions of the maps F F and ℱ \mathcal{F} in ( 21) respectively.

###### Definition 15.

The contact function for the mixed system ( 21) is

(22) |  | ℱ s + 1 = ∗ ( ω ∧ d F 1 ∧ ⋯ ∧ d F n − s − 1 ∧ d ℱ 1 ∧ ⋯ ∧ d ℱ s). \displaystyle\mathcal{F}_{s+1}=*(\omega\wedge dF_{1}\wedge\cdots\wedge dF_{n-s-1}\wedge d\mathcal{F}_{1}\wedge\cdots\wedge d\mathcal{F}_{s}). |  |

The operator taking the mixed system ( ω, F, ℱ) (\omega,F;\mathcal{F}) into the corresponding contact function, will be denoted by σ: ( ω, F, ℱ) ↦ σ ⁡ ( ω, F, ℱ) = ℱ s + 1 \sigma:(\omega,F;\mathcal{F})\mapsto\sigma(\omega,F;\mathcal{F})=\mathcal{F}_{s+1}.

Define the two maps by their coordinate functions,

(23) |  | ℱ c = ( ℱ 1, …, ℱ s, ℱ s + 1), ℱ ∞ = ( ℱ 1, …, ℱ s, ρ), \displaystyle\mathcal{F}^{c}=(\mathcal{F}_{1},\dots,\mathcal{F}_{s},\mathcal{F}_{s+1}),\qquad\mathcal{F}^{\infty}=(\mathcal{F}_{1},\dots,\mathcal{F}_{s},\rho), |  |

both taking M M to ℝ s + 1 \mathbb{R}^{s+1}, where ℱ s + 1 \mathcal{F}_{s+1} is the contact function ( 22), and ρ \rho is the covering function.

###### Theorem 16.

Suppose that the system ( 21) admits regular solutions in the sense of Definition 19. Then for any sufficiently small regular ϵ \epsilon

(24) |  | 𝒦 ⁡ { ω, F; ℱ = a } ≤ 1 2 ​ 𝒦 ​ { ω, F; ℱ ∞ = ( a, ϵ) } + 𝒦 ⁡ { ω, F; ℱ c = ( a, ϵ) }, \displaystyle\mathcal{K}\{\omega,F;\mathcal{F}=a\}\leq\frac{1}{2}\mathcal{K}\{\omega,F;\mathcal{F}^{\infty}=(a,\epsilon)\}+\mathcal{K}\{\omega,F;\mathcal{F}^{c}=(a,\epsilon)\}, |  |

where regularity of ϵ \epsilon means that ( a, ϵ) (a,\epsilon) is a regular value for both ℱ ∞ \mathcal{F}^{\infty} and ℱ c \mathcal{F}^{c} and is necessary to the right-hand side systems being well defined.

Before proving this theorem recall the Rolle lemma from an elementary calculus.

###### Lemma 1.

Consider C 2 C^{2} Morse functions f: S 1 → ℝ 1 f:S^{1}\to\mathbb{R}^{1} on the circle and g: [0, 1] → ℝ 1 g:[0,1]\to\mathbb{R}^{1} on the segment, i.e., functions f f and g g have only nondegenerate critical points. Then for all a ∈ ℝ a\in\mathbb{R}

(25) |  | #⁡ { x: f ⁡ ( x) = a } ≤ #⁡ { x: f ′ ​ ( x) = ϵ } #⁡ { x: g ⁡ ( x) = a } ≤ #⁡ { x: g ′ ​ ( x) = ϵ } + 1 \displaystyle\begin{aligned} \#\{x:\ f(x)=a\}\leq\#\{x:\ f^{\prime}(x)=\epsilon\}\\ \#\{x:\ g(x)=a\}\leq\#\{x:\ g^{\prime}(x)=\epsilon\}+1\end{aligned} |  |

for any sufficiently small ϵ \epsilon.

Proof Prove the formula for f: S 1 → ℝ 1 f:S^{1}\to\mathbb{R}^{1}. For a sufficiently small ϵ \epsilon the number of local maxima and minima equals #⁡ { x: f ′ ​ ( x) = ϵ } \#\{x:\ f^{\prime}(x)=\epsilon\}. Between any two consecutive preimages x 1 x_{1} and x 2 x_{2} of a point a a, i.e., f ⁡ ( x 1) = f ⁡ ( x 2) = a f(x_{1})=f(x_{2})=a there exists a local minimum or maximum. Q.E.D.

Formula ( 25) in the case of one equation transfers a loose equation into a rigid one.

Proof of theorem 16 Take a regular solution ( Γ a, L b) (\Gamma^{a},L_{b}) for ( 21), where L b = F − 1 ​ ( b) L_{b}=F^{-1}(b), and suppose that the intersection Γ a ∩ L b \Gamma^{a}\cap L_{b} consists of isolated, say d d, points. Since, b b is regular value of the restriction F | Γ a F|_{\Gamma^{a}}, any small variation of b b may only increase the number of intersections. Take b b to be a regular value of the restriction F | V a F|_{V_{a}} or equivalently ( b, a) (b,a) to be a regular value of the map ( F, ℱ) (F,\mathcal{F}) (rather than of the restriction of ℱ \mathcal{F} to Γ a \Gamma^{a}).

Then any level set L b L_{b} is a one dimensional smooth manifold, intersecting Γ \Gamma transversally. By the classification theorem for one-dimensional manifolds, L b L_{b} is the union of compact (circles) and noncompact (lines) components. Fix some orientation on each circle and each curve in L b L_{b}. Consider the function f ′: L b → ℝ f^{\prime}:L_{b}\to\mathbb{R} which maps a point x ∈ L a x\in L_{a} to the value of the 1 1 -form ω \omega on the unit positively oriented vector tangent to L b L_{b} at point x x.

Fix a connected component, denoted by γ ⊂ L b \gamma\subset L_{b}. Between any two consecutive intersection x x and y y of L a L_{a} with Γ \Gamma values f ′ ​ ( x) f^{\prime}(x) and f ′ ​ ( y) f^{\prime}(y) must have different signs. Now we can apply the Rolle lemma with f ′ = f ′ f^{\prime}=f^{\prime}, when γ \gamma is a circle, and f ′ = g ′ f^{\prime}=g^{\prime}, when γ \gamma is a line.

Each point x x where f ′ ​ ( x) = 0 f^{\prime}(x)=0 (resp. f ′ ​ ( x) f^{\prime}(x) is small) is the point where the linear functionals d ​ F 1 ​ ( x), …, d ​ F n − s − k ​ ( x), d ​ ℱ 1 ​ ( x), …, d ​ ℱ s ​ ( x) dF_{1}(x),\dots,dF_{n-s-k}(x),d\mathcal{F}_{1}(x),\dots,d\mathcal{F}_{s}(x). and ω ⁡ ( x) \omega(x) are linear dependent (resp. almost dependent), i.e. ℱ s + 1 ​ ( x) = 0 \mathcal{F}_{s+1}(x)=0 (resp. ℱ s + 1 ​ ( x) = ϵ \mathcal{F}_{s+1}(x)=\epsilon). This completes the proof of the theorem. Q.E.D.

###### Corollary 3.

If the manifold M M is compact, then for any sufficiently small regular ϵ \epsilon

(26) |  | 𝒦 ⁡ { ω, F; ℱ = a } ≤ 𝒦 ⁡ { ω, F; ℱ c = ( a, ϵ) }, \displaystyle\mathcal{K}\{\omega,F;\mathcal{F}=a\}\leq\mathcal{K}\{\omega,F;\mathcal{F}^{c}=(a,\epsilon)\}, |  |

where regularity of ϵ \epsilon means that ( a, ϵ) (a,\epsilon) is a regular value for ℱ c \mathcal{F}^{c}.

Proof Indeed, in this case the first term in ( 21) disappears.

###### Remark 2.

The choice of the Riemann volume form is not essential for the above construction. Indeed, if the volume form v ​ o ​ l n {\text{v}ol}^{n} is replaced by a new one b ⋅ v ​ o ​ l n b\cdot{\text{v}ol}^{n}, where b b is a positive function, then the function ℱ s + 1 \mathcal{F}_{s+1} will be replaced by ℱ ~ s + 1 = b − 1 ​ ℱ s + 1 \tilde{\mathcal{F}}_{s+1}=b^{-1}\mathcal{F}_{s+1}, and the map ℱ ~ c = ( ℱ 1, …, ℱ s, ℱ ~ s + 1) \tilde{\mathcal{F}}^{c}=(\mathcal{F}_{1},\dots,\mathcal{F}_{s},\tilde{\mathcal{F}}_{s+1}) will have the same zero set.

### 3.3. The Khovanski reduction in the general case

Consider now the general case of the mixed system ( 19) with k > 1 k>1. Suppose that Γ a \Gamma^{a} is a separating solution for the Pfaffian system Ω = 0 \Omega=0 restricted to V a V_{a}. By definition, this means that there exists a separating solution Γ k a ⊂ V a \Gamma_{k}^{a}\subset V_{a} to the Pfaffian equation ω k = 0 \omega_{k}=0 on a separating solution Γ k − 1 a ⊂ V a \Gamma_{k-1}^{a}\subset V_{a} to the Pfaffian system Ω ′ = 0 \Omega^{\prime}=0 restricted to V a V_{a}, where Ω ′ = ( ω 1, …, ω k − 1) \Omega^{\prime}=(\omega_{1},\dots,\omega_{k-1}). Note that if ρ \rho is a covering function on the manifold M M, then its restriction on Γ k − 1 a \Gamma_{k-1}^{a} is the covering function for the latter submanifold. Next, one can endow V a V_{a} (resp. Γ k − 1 a \Gamma^{a}_{k-1}) by the Riemann ( n − s) (n-s) -volume (resp. ( n − k − s + 1) (n-k-s+1) -volume) form v ​ o ​ l V a n − s {\text{v}ol}^{n-s}_{V_{a}} (resp. v ​ o ​ l Γ k − 1 a n − k − s + 1 {\text{v}ol}^{n-k-s+1}_{\Gamma^{a}_{k-1}}) in such a way that

(27) |  | d ​ ℱ 1 ∧ ⋯ ∧ d ​ ℱ s ∧ vol V a n − s = vol M n ω 1 ∧ ⋯ ∧ ω k − 1 ∧ vol Γ k − 1 a n − k + 1 = vol V a n − s \displaystyle\begin{aligned} \,\,\,\,\,d\mathcal{F}_{1}\wedge\cdots\wedge d\mathcal{F}_{s}\wedge\operatorname{vol}^{n-s}_{V_{a}}=\operatorname{vol}^{n}_{M}\ \ \ \omega_{1}\wedge\cdots\wedge\omega_{k-1}\wedge\operatorname{vol}^{n-k+1}_{\Gamma^{a}_{k-1}}=\operatorname{vol}^{n-s}_{V_{a}}\end{aligned} |  |

Since the forms ω j, j = 1, …, k − 1 \omega_{j},\ j=1,\dots,k-1 are linear independent in a neighborhood of Γ k − 1 a \Gamma^{a}_{k-1}, these formulas define volume forms near V a V_{a} and Γ k − 1 a \Gamma^{a}_{k-1} respectively. As this was mentioned before, the choice of the Riemann volume form does not affect the assertion of Theorem 17.

Thus one can apply Theorem 17 to the mixed system

(28) |  | ω k = 0, F = b, ℱ = a \displaystyle\omega_{k}=0,\quad F=b,\quad\mathcal{F}=a |  |

on the manifold Γ n − k a ⊂ V a \Gamma^{a}_{n-k}\subset V_{a}. To describe the result, we introduce the following two maps from M M to ℝ n − k + 1 \mathbb{R}^{n-k+1},

(29) |  | ℱ c = ( ℱ 1, …, ℱ s, ρ), ℱ ∞ = ( ℱ 1, …, ℱ s, ℱ ∗), \displaystyle\mathcal{F}^{c}=(\mathcal{F}_{1},\dots,\mathcal{F}_{s},\rho),\qquad\mathcal{F}^{\infty}=(\mathcal{F}_{1},\dots,\mathcal{F}_{s},\mathcal{F}_{*}), |  |

where ρ \rho is the covering function on the manifold M M, and F ∗: M → ℝ F_{*}:M\to\mathbb{R} is the smooth function obtained as

(30) |  | ℱ ∗ = σ ( Ω, F; ℱ) = ∗ ( d F 1 ∧ ⋯ ∧ d F n − k − s ∧ OPEN ∧ d ​ ℱ 1 ∧ ⋯ ∧ d ​ ℱ s ∧ ω 1 ∧ ⋯ ∧ ω k). \displaystyle\begin{aligned} \quad\mathcal{F}_{*}=\sigma(\Omega,F;\mathcal{F})=*(dF_{1}\wedge\dots\wedge dF_{n-k-s}\wedge\\ \wedge d\mathcal{F}_{1}\wedge\dots\wedge d\mathcal{F}_{s}\wedge\omega_{1}\wedge\dots\wedge\omega_{k}).\end{aligned} |  |

The above choice of the Riemann volume on Γ k − 1 a \Gamma^{a}_{k-1} implies that the asterisk operator in the ambient manifold M M agrees with the asterisk operator relevant to Γ k − 1 a \Gamma^{a}_{k-1}, therefore the formula ( 30) defines the same function as the formula ( 22): ω k ∧ d ​ F 1 ∧ ⋯ ∧ d ​ F n − k − s ∧ d ​ ℱ 1 ∧ ⋯ ∧ d ​ ℱ s = ℱ ∗ ⋅ vol Γ k − 1 a n − k + 1 \omega_{k}\wedge dF_{1}\wedge\cdots\wedge dF_{n-k-s}\wedge d\mathcal{F}_{1}\wedge\cdots\wedge d\mathcal{F}_{s}=\mathcal{F}_{*}\cdot\operatorname{vol}^{n-k+1}_{\Gamma^{a}_{k-1}}.

###### Theorem 17.

Let Ω, F, ℱ c \Omega,F,\mathcal{F}^{c}, and ℱ ∞ \mathcal{F}^{\infty} be as above. Then for any sufficiently small regular ϵ \epsilon

(31) |  | 𝒦 ⁡ { Ω, F; ℱ = a } ≤ 1 2 ​ 𝒦 ​ { Ω ′, F; ℱ ∞ = ( a, ϵ) } + 𝒦 ⁡ { Ω ′, F; ℱ c = ( a, ϵ) }, \displaystyle\mathcal{K}\{\Omega,F;\mathcal{F}=a\}\leq\tfrac{1}{2}\mathcal{K}\{\Omega^{\prime},F;\mathcal{F}^{\infty}=(a,\epsilon)\}+\mathcal{K}\{\Omega^{\prime},F;\mathcal{F}^{c}=(a,\epsilon)\}, |  |

where regularity of ϵ \epsilon means that ( a, ϵ) (a,\epsilon) is a regular value for both ℱ ∞ \mathcal{F}^{\infty} and ℱ c \mathcal{F}^{c}.

###### Corollary 4.

If either V a V_{a} is compact or the restriction F | V a: V a → ℝ n − k − s F|_{V_{a}}:V_{a}\to\mathbb{R}^{n-k-s} is a proper map, i.e. preimage of any point is compact, then for any sufficiently small regular ϵ \epsilon

(32) |  | 𝒦 ⁡ { Ω, F; ℱ = a } ≤ 𝒦 ⁡ { Ω ′, F; ℱ c = ( a, ϵ) }, \displaystyle\mathcal{K}\{\Omega,F;\mathcal{F}=a\}\leq\mathcal{K}\{\Omega^{\prime},F;\mathcal{F}^{c}=(a,\epsilon)\}, |  |

where regularity of ϵ \epsilon means that ( a, ϵ) (a,\epsilon) is a regular value for ℱ c \mathcal{F}^{c}.

Proof Straightforward application of Theorem 16.

Iterating the above two statements, one can replace one by one the Pfaffian equations by the rigid functional ones, obtaining new systems whose Khovanski numbers estimate from above that of the initial one, by virtue of the inequalities ( 21) and its compact counterpart ( 24). On each step one has two possibilities, either to replace a Pfaffian equation by the contact function, or by the covering function. But once the covering function appears among the rigid functional equations, the level sets F − 1 ​ ( ⋅) ∩ V a F^{-1}(\cdot)\cap V_{a} becomes compact as a submanifold of a compact V a V_{a}, hence on the next steps the Corollary to Theorem 17 applies rather than the Theorem itself.

Denote by T ϵ c T^{c}_{\epsilon} and T ϵ ∞ T^{\infty}_{\epsilon} the two operators, transforming the mixed system { Ω, F; ℱ = a } \{\Omega,F;\mathcal{F}=a\} into the mixed systems { Ω ′, F; ℱ c = ( a, ϵ) } \{\Omega^{\prime},F;\mathcal{F}^{c}=(a,\epsilon)\} and { Ω ′, F, ℱ ∞ = ( a, ϵ) } \{\Omega^{\prime},F,\mathcal{F}^{\infty}=(a,\epsilon)\} respectively, where the maps ℱ c \mathcal{F}^{c} and ℱ ∞ \mathcal{F}^{\infty} are given by ( 29) and ( 30):

(33) |  | T c ϵ { Ω, F; ℱ = a } = { Ω ′, F; ( ℱ, σ { Ω, F, ℱ }) = ( a, ϵ)) }, T ∞ ϵ { Ω, F; ℱ = a) } = { Ω ′, F; ( ℱ, ρ) = ( a, ϵ)) }. \displaystyle\begin{aligned} T^{c}_{\epsilon}\{\Omega,F;\mathcal{F}=a\}=\{\Omega^{\prime},F;(\mathcal{F},\sigma\{\Omega,F,\mathcal{F}\})=(a,\epsilon))\},\\ T^{\infty}_{\epsilon}\{\Omega,F;\mathcal{F}=a)\}=\{\Omega^{\prime},F;(\mathcal{F},\rho)=(a,\epsilon))\}.\end{aligned} |  |

If we start with the mixed functional–Pfaffian system { ( Ω, Ω F), ω; ℱ = a } \{(\Omega,\Omega_{F}),\omega;\mathcal{F}=a\}, with ( Ω, Ω F) (\Omega,\Omega_{F}) being an ( n − s) (n-s) -tuple ( ω 1, …, ω k, d ​ F 1, …, d ​ F n − k − s) (\omega_{1},\dots,\omega_{k},dF_{1},\dots,dF_{n-k-s}), and eliminate subsequently the forms ω k \omega_{k}, ω k − 1, …, ω 1, \omega_{k-1},\dots,\omega_{1}, d ​ F 1, …, d ​ F n − k − s dF_{1},\dots,dF_{n-k-s}, then the following maps from M M to ℝ n \mathbb{R}^{n} arise:

a) the map ℱ [0] \mathcal{F}_{[0]}, if on each step the contact function was used,

(34) |  | { ω, ℱ [0] = ( a, ϵ n − s)) } = ( T ϵ n − s c ∘ ​ ⋯ ​ ∘ T ϵ 1 c) { Ω, F; ℱ = a }, \displaystyle\{\omega,\mathcal{F}_{[0]}=(a,\epsilon^{n-s}))\}=(T^{c}_{\epsilon_{n-s}}\circ\*\cdots\*\circ T^{c}_{\epsilon_{1}})\{\Omega,F;\mathcal{F}=a\}, |  |

where ϵ n − s = ( ϵ 1, …, ϵ n − s) \epsilon^{n-s}=(\epsilon_{1},\dots,\epsilon_{n-s});

b) the maps ℱ [j] \mathcal{F}_{[j]}, if on the j j th step the covering function was used, while on all other steps the contact ones were, j = 1, …, n − s j=1,\dots,n-s,

(35) |  | { ω; ℱ [j] = ( a, ϵ n − s)) } = ( T c ϵ n − s ∘ ⋯ ∘ T c ϵ j + 1 ∘ ​ T ∞ ϵ j ∘ ∘ ​ T c ϵ j − 1 ∘ OPEN ⋯ ∘ T ϵ 1 c) ​ { Ω, F; ℱ = a }. \displaystyle\begin{aligned} \qquad\{\omega;\mathcal{F}_{[j]}=(a,\epsilon^{n-s}))\}=(T^{c}_{\epsilon_{n-s}}\circ\cdots\circ T^{c}_{\epsilon_{j+1}}&\circ\*T^{\infty}_{\epsilon_{j}}\circ\\ \circ\*T^{c}_{\epsilon_{j-1}}\circ&\cdots\circ T^{c}_{\epsilon_{1}})\{\Omega,F;\mathcal{F}=a\}.\end{aligned} |  |

Then inductive application of Theorem 16 immediately yields the following fundamental result.

###### Theorem 18.

The Khovanski number for the mixed system ( 19) on a manifold M M with the covering function ρ \rho and any sufficiently fast decaying to zero sequence ( ϵ 1, …, ϵ n − s) (\epsilon_{1},\dots,\epsilon_{n-s}) admits the upper estimate by a linear combination of Khovanski numbers of some ( n − s + 1) (n-s+1) auxiliary systems, each of them containing only rigid equations and no Pfaffian equations at all:

(36) |  | 𝒦 ⁡ { Ω, F; ℱ = a } ≤ 𝒦 ⁡ { ω; ℱ [0] = ( a, ϵ n − s) } + 1 2 ​ ∑ j = 1 k 𝒦 ⁡ { ω; ℱ [j] = ( a, ϵ n − s) }, \displaystyle\qquad\mathcal{K}\{\Omega,F;\mathcal{F}=a\}\leq\mathcal{K}\{\omega;\mathcal{F}_{[0]}=(a,\epsilon^{n-s})\}+\frac{1}{2}\sum_{j=1}^{k}\mathcal{K}\{\omega;\mathcal{F}_{[j]}=(a,\epsilon^{n-s})\}, |  |

where the maps ℱ [j] \mathcal{F}_{[j]} are defined by the formula ( 33)-( 35).

### 3.4. Applications

The Khovanski reduction process is constructive. This leads to the result, which will be now formulated.

Assume that the manifold M M is an open domain in ℝ n \mathbb{R}^{n} and admits a polynomial covering function ρ \rho. The main example is the unit ball B = { x ∈ ℝ n: ∑ j x j 2 < 1 } B=\big\{x\in\mathbb{R}^{n}:\sum_{j}x_{j}^{2}<1\big\}, for which one may take ρ ⁡ ( x) = 1 − ∑ j x j 2 \rho(x)=1-\sum_{j}x_{j}^{2}. Then the Riemann volume form can be chosen algebraic, d ​ x 1 ∧ ⋯ ∧ d ​ x n dx_{1}\wedge\cdots\wedge dx_{n}.

Assume also that all the forms ω i, i = 1, …, k \omega_{i},\ i=1,\dots,k are polynomial (i.e. with polynomial coefficients), and the maps ℱ \mathcal{F} and G G are at least C n − s C^{n-s} -smooth. Then, since the operators T ϵ c T^{c}_{\epsilon} and T ϵ ∞ T^{\infty}_{\epsilon} introduced above, involve only algebraic operations and differentiation of functions, the following holds.

###### Theorem 19.

If the system ( 19) has no rigid functional equations at all ( s = 0 s=0) and is defined on a semialgebraic subset M ⊆ ℝ n M\subseteq\mathbb{R}^{n}, all Pfaffian forms and the covering function ρ \rho are polynomial of degrees ≤ d \leq d, then all the maps ℱ [α]: M → ℝ n \mathcal{F}_{[\alpha]}:M\to\mathbb{R}^{n}, α = 0, 1, …, k \alpha=0,1,\dots,k constructed in Theorem 19 are of the form

(37) |  | ℱ [α] = P α ∘ j n − s ​ F, \displaystyle\mathcal{F}_{[\alpha]}=P_{\alpha}\circ j^{n-s}F, |  |

where j n − s ​ F j^{n-s}F is the ( n − s) (n-s) -jet extension of F F, and P α P_{\alpha} are certain polynomials defined on the jet space J n − s ​ ( ℝ n, ℝ n − k) J^{n-s}(\mathbb{R}^{n},\mathbb{R}^{n-k}). For all α = 0, 1, …, k \alpha=0,1,\dots,k the degrees of the polynomial P α P_{\alpha} admits the upper estimate by 2 α ​ ( d ​ k + n) 2^{\alpha}(dk+n) and each map ℱ [α] \mathcal{F}_{[\alpha]} has a regular point for a generic map F F.

Proof The reduction procedure of elimination of a Pfaffian equation boils down to consecutive application ( n − s) (n-s) times of one of the operators T ϵ c T^{c}_{\epsilon} or T ϵ ∞ T^{\infty}_{\epsilon} ( 33). Consider the first step.

 | ℱ 1, α ∗ = σ { ( Ω, Ω F), ∅; ℱ) } = ∗ ( ω 1 ∧ ⋯ ∧ ω k ∧ d F 1 ∧ ⋯ ∧ d F n − k OPEN) = P 1, α ∘ j 1 ​ F, \displaystyle\begin{aligned} \mathcal{F}^{1,\alpha}_{*}=\sigma\{(\Omega,\Omega_{F}),\emptyset;\mathcal{F})\}=*(\omega_{1}\wedge\cdots\wedge\omega_{k}\wedge dF_{1}\wedge\cdots\wedge dF_{n-k}&)=P^{1,\alpha}\circ j^{1}F,\end{aligned} |  |

where P 1, α: J 1 ​ ( ℝ n, ℝ n − k) → ℝ P^{1,\alpha}:J^{1}(\mathbb{R}^{n},\mathbb{R}^{n-k})\to\mathbb{R} is a polynomial of degree at most d ​ k + n dk+n and is defined on the space of 1 1 -jets J 1 ​ ( ℝ n, ℝ n − k) J^{1}(\mathbb{R}^{n},\mathbb{R}^{n-k}).

Denote by Ω ∗ = ( Ω, Ω F) \Omega^{*}=(\Omega,\Omega_{F}) the ( n − s) (n-s) -tuple of the 1-form, d ​ F s dF_{s} by ω k + s \omega_{k+s} for s = 1, …, n − s s=1,\dots,n-s, and the ( n − s − r) (n-s-r) -tuple of the 1-form, which consists of all of 1-forms of Ω ∗ \Omega^{*} except of the first r r, by Ω r ∗ \Omega^{*}_{r}. Consider ℱ ∗ r, α = σ ⁡ { Ω r − 1 ∗, ω r; ℱ r − 1, α } \mathcal{F}^{r,\alpha}_{*}=\sigma\{\Omega^{*}_{r-1},\omega_{r};\mathcal{F}^{r-1,\alpha}\} and ℱ r, α = ( ℱ r − 1, α, ℱ ∗ r, α) \mathcal{F}^{r,\alpha}=(\mathcal{F}^{r-1,\alpha},\mathcal{F}^{r,\alpha}_{*}) for r = 1, …, n − s r=1,\dots,n-s. It is easy to see that ℱ ∗ r, α \mathcal{F}^{r,\alpha}_{*} has the form ℱ ∗ r, α = P r, α ∘ j r ​ F \mathcal{F}^{r,\alpha}_{*}=P^{r,\alpha}\circ j^{r}F.

Using induction in r r it is easy to see that for r ≠ α r\neq\alpha the degrees of corresponding polynomials P r − 1, α P^{r-1,\alpha} and P r, α P^{r,\alpha}, defined above, satisfy the following inequality deg ⁡ P r, α ≤ 2 ​ deg ⁡ P r − 1, α \deg P^{r,\alpha}\leq 2\deg P^{r-1,\alpha}. For r = α r=\alpha the operator T ϵ ∞ T^{\infty}_{\epsilon} will not exceed the degree d ​ k + n dk+n and ℱ r, α = ρ \mathcal{F}^{r,\alpha}=\rho. This implies that deg ⁡ P r, α ≤ 2 α ​ ( d ​ k + n) \deg P^{r,\alpha}\leq 2^{\alpha}(dk+n) and complete the proof.

## 4. Functional-Pfaffian system for limit cycles

In this section we consider a specified basic system ( 𝒯, 𝒮 a, 𝐟, 𝐫) (\mathcal{T},\mathcal{S}_{a},\bf f;r) obtained from the unspecified basic system ( 8), that is we consider a system ( 8) together with a collection of formal invariants ( c 1, …, c n) (c_{1},\dots,c_{n}) of all singularities (which determines a point in the λ \lambda -space), a collection of hyperbolicity ratios n j α: m j α n_{j_{\alpha}}:m_{j_{\alpha}} of all resonant saddles and a tuple of sufficiently smooth functions f j f_{j}, on a sufficiently small open cube I r × B r I_{r}\times B_{r} in the ( ϵ, λ) (\epsilon,\lambda) -space.

Our local goal is to reduce this system to a functional–Pfaffian system having the form described in section 3, with the following properties:

∙ \bullet the new system has the form allowing for application of Theorem 17;

∙ \bullet the number of regular solutions to the functional–Pfaffian system is greater or equal to the number of isolated solutions to ( 8), up to k k, where k k is the number of parameters of the original family.

After application of Theorem 17 we will obtain a number of chain maps with controlled degrees of the exterior polynomial parts.

### 4.1. Upper estimate of the number of solutions for the basic system: statement of results

First of all we make the following remark. The algebraic part of the specialization can be identified with a point

(38) |  | 𝒮 a = ( c 1, …, c n, n j 1, m j 1, …, n j s, m j s) ∈ ℝ n + 2 ​ s, \displaystyle\mathcal{S}_{a}=(c_{1},\dots,c_{n},n_{j_{1}},m_{j_{1}},\dots,n_{j_{s}},m_{j_{s}})\in\mathbb{R}^{n+2s}, |  |

where s ≤ n s\leq n is the number of resonant saddles on the polycycle: the fact that the numbers n j α, m j α n_{j_{\alpha}},m_{j_{\alpha}} are in fact natural will become inessential for our constructions.

###### Theorem 20.

( reduction from basic to functional–Pfaffian system) Consider an unspecified basic system 8 of a certain type 𝒯 \mathcal{T} in codimension k k, together with an arbitrary specification

 | 𝒮 = ( S a, 𝐟, r), 𝒮 a ∈ ℝ n + 2 ​ s, 𝐟 ∈ C 𝗉 ​ ( I r × B r, ℝ n), r > 0. \mathcal{S}=(S_{a},{\bf f};r),\quad\mathcal{S}_{a}\in\mathbb{R}^{n+2s},\quad{\bf f}\in C^{\mathsf{p}}(I_{r}\times B_{r},\mathbb{R}^{n}),\quad\ r>0. |  |

Then one can explicitly construct a functional–Pfaffian system of the form { Ω, F } \{\Omega,F\}, Ω = ( Ω 1, …, Ω n + 2 ​ s) \Omega=(\Omega_{1},\dots,\Omega_{n+2s}), F = ( F 1, …, F n + k + m) F=(F_{1},\dots,F_{n+k+m}), m = ∑ μ j m=\sum\mu_{j}, or in a more traditional notation, the mixed system of loose functional and Pfaffian equations (no rigid equations)

(39) |  | Ω = 0, F = a; \displaystyle\Omega=0,\quad F=a; |  |

defined in a certain open bounded semialgebraic subset

 | M = M ⁡ ( r) ⊂ I r × B r × ℝ 2 ​ s M=M(r)\subset I_{r}\times B_{r}\times\mathbb{R}^{2s} |  |

(see Definition 8), such that the following holds:

∙ \bullet For any choice of the parameters ( ϵ, λ) ∈ B r (\epsilon,\lambda)\in B_{r} the number of isolated ( x, y) (x,y) -solutions, denoted by ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟, r) \mathcal{B}(\mathcal{T},\mathcal{S}_{a},{\bf f};r) of the specified basic system ( 𝒯, 𝒮 a, 𝐟, r) (\mathcal{T},\mathcal{S}_{a},{\bf f};r) admits the estimate by the Khovanski system ( 39) on the manifold M = M ⁡ ( r) M=M(r):

 | ℬ ⁡ ( 𝒯, 𝒮 a, 𝐟, r) ≤ 𝒦 M ⁡ ( r) ​ { Ω, F; ω } + k; \mathcal{B}(\mathcal{T},\mathcal{S}_{a},{\bf f};r)\leq\mathcal{K}_{M(r)}\{\Omega,F;\omega\}+k; |  |

∙ \bullet The forms Ω k \Omega_{k} have coefficients which are polynomial in all their arguments, and also in coordinates of the point 𝒮 a ∈ ℝ n + 2 ​ s \mathcal{S}_{a}\in\mathbb{R}^{n+2s}; the degrees of those polynomials do not exceed 6 ​ μ + 1 6\mu+1, where μ \mu is the order of degeneracy of the corresponding equilibrium point;

∙ \bullet The covering function ρ ⁡ ( ⋅, r) \rho(\cdot\,;r) for the phase space M ⁡ ( r) M(r) is polynomial in all its arguments and also in r r, of the total degree not exceeding 14 ​ k 14k;

∙ \bullet The coordinate functions of the maps F β F_{\beta} are explicitly given as polynomials of the first degree on the 0 0 -jet space of functions J 0 ​ ( I r × B r, ℝ n) J^{0}(I_{r}\times B_{r},\mathbb{R}^{n}) with coefficients ± 1 \pm 1.

The proof of this theorem is completely constructive and given in [IY3]. We only point out degree estimates which are not given in [IY3].

Table 2. Separating solutions for Pfaffian systems associated with unfolding of elementary equilibrium points.

Type | Submanifold γ \gamma | Domain M r M_{r}, Covering function ρ \rho | Pfaffian system Ω = 0 \Omega=0 |

 |  | 0 < x, y < r, 0\ <\ x,\ y\ <\ r, |  |

S 0 S_{0} | y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) | λ ∈ L r, \lambda\in L_{r}, | x ​ d ​ y − λ ​ y ​ d ​ x = 0 x\ dy\ -\lambda y\ dx\ =0 |

 |  | ρ = x ​ y ​ ( r − x) ​ ( r − y) ​ ρ ~ \rho=xy(r-x)(r-y)\tilde{\rho} |  |

 |  | 0 < x, y, z, w < r, 0\ <\ x,\ y,\ z,\ w\ <\ r, | x ​ d ​ z − m ​ z ​ d ​ x = 0, ( 1) x\ dz\ -\ m\ z\ dx=0,\ (1) |

 | y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) | λ ∈ L r, \lambda\in L_{r}, | y ​ d ​ w − n ​ w ​ d ​ y = 0, ( 2) y\ dw\ -\ n\ w\ dy=0,\ (2) |

S μ S_{\mu} | z = x m z=x^{m} | P μ ​ ( z, λ) ≠ 0, P_{\mu}(z,\lambda)\neq 0, | m P μ ( w, λ) × m\,P_{\mu}(w,\lambda)\,\times |

 | w = y n w=y^{n} | ρ = x y z w ( r − x) ( r − y) × \rho=xyzw(r-x)(r-y)\times | y ​ P μ ​ ( z, λ) ​ d ​ x − y\,P_{\mu}(z,\lambda)\,dx\,- |

 |  | ( r − z) ​ ( r − w) ​ P μ 2 ​ ( z, λ) ​ ρ ~ (r-z)(r-w)P_{\mu}^{2}(z,\lambda)\tilde{\rho} | ( m P μ ( w, λ) + n) × (mP_{\mu}(w,\lambda)+n)\,\times |

 |  |  | x ​ P μ 2 ​ ( z, λ) ​ d ​ y = 0 ​ ( 3) x\,P_{\mu}^{2}(z,\lambda)\,dy=0\ (3) |

 |  | | x |, | y | < r, x ≠ 0, |x|,|y|<r,\ x\neq 0, |  |

D μ c D^{c}_{\mu} | y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) | λ ∈ L r, \lambda\in L_{r}, | x ⁡ ( x ​ d ​ y − y ​ d ​ x) = 0 x\ (x\ dy\ -y\ dx)=0 |

 |  | ρ = ( r 2 − x 2) ​ ( r 2 − y 2) ​ x 2 ​ ρ ~ \rho=(r^{2}-x^{2})(r^{2}-y^{2})x^{2}\tilde{\rho} |  |

 |  | 0 < y < r, | x | < r, 0<y<r,\ |x|<r, |  |

 |  | λ ∈ L r \lambda\in L_{r} |  |

D m h ​ u D^{h}_{m}u | y = Δ ⁡ ( x, λ) y=\Delta(x,\lambda) | Q μ ​ ( ⋅, λ) | [x, 1] > 0, Q_{\mu}(\cdot,\lambda)|_{[x,1]}>0, | Q μ ​ ( x, λ) ​ d ​ y − y ​ d ​ x = 0 Q_{\mu}(x,\lambda)\ dy\ -y\ dx\ =0 |

 |  | ρ = y ( r − y) ( r 2 − x 2) × \rho=y(r-y)(r^{2}-x^{2})\times |  |

 |  | Q μ ​ ( x, λ) ​ ρ ~ Q_{\mu}(x,\lambda)\tilde{\rho} |  |

 |  |  |

Notes to the Table Here we use the same notation as in Table 1 (and in fact this Table continues Table 1). In particular, n: m n:m is the hyperbolicity ratio in the resonant saddle case S μ S_{\mu}.

In the third column of the Table the symbol L r L_{r} stands for a small r r -cube in the ( μ + 1) (\mu+1) -dimensional space of the parameters λ \lambda, centered at the localization point 𝐜 = ( 𝟎, …, 𝟎, 𝐜) ∈ ℝ μ + 𝟏 \bf c=(0,\dots,0,c)\in\mathbb{R}^{\mu+1}, corresponding to the unperturbed system:

 | L r = { λ ∈ ℝ μ + 1: | λ i | < r, i = 0, …, μ − 1, | λ μ − c | < r } L_{r}=\{\lambda\in\mathbb{R}^{\mu+1}:|\lambda_{i}|<r,\ i=0,\dots,\mu-1,\ |\lambda_{\mu}-c|<r\} |  |

Everywhere in the Table the function ρ ~ = ρ ~ ​ ( λ) \tilde{\rho}=\tilde{\rho}(\lambda) is the covering function for the set L r L_{r}, defined as

 | ρ ~ ( λ) = ( r 2 − λ 1 2) ⋯ ( r 2 − λ μ − 1 2) ⋅ ( r 2 − ( c − λ μ) 2). \tilde{\rho}(\lambda)=(r^{2}-\lambda_{1}^{2})\cdots(r^{2}-\lambda_{\mu-1}^{2})\cdot(r^{2}-(c-\lambda_{\mu})^{2}). |  |

This is a polynomial of degree 2 ​ μ 2\mu in all variables λ, r, c \lambda,r,c. Recall that deg ⁡ P m ​ u = 2 ​ μ \deg P_{m}u=2\mu and deg ⁡ Q μ = 2 ​ μ + 1 \deg Q_{\mu}=2\mu+1 (see Table 1). Each covering function ρ \rho is therefore a polynomial (explicitly written in the Table). Thus, we obtain the following degree estimates:

Type S 0 S_{0}: deg ⁡ Ω = 1 \deg\Omega=1 and deg ⁡ ρ = 4 ​ μ + 4 \deg\rho=4\mu+4.

Type S μ S_{\mu}, μ > 0 \mu>0: deg ⁡ Ω ≤ 6 ​ μ + 1 \deg\Omega\leq 6\mu+1 and deg ⁡ ρ = 6 ​ μ + 8 \deg\rho=6\mu+8.

Type D μ c D^{c}_{\mu}: deg ⁡ Ω = 2 \deg\Omega=2 and deg ⁡ ρ = 2 ​ μ + 6 \deg\rho=2\mu+6.

Type D μ h D^{h}_{\mu}: deg ⁡ Ω = 2 ​ μ + 1 \deg\Omega=2\mu+1 and deg ⁡ ρ = 4 ​ μ + 5 \deg\rho=4\mu+5.

Along with the estimate ∑ μ j ≤ k \sum\mu_{j}\leq k (the sum of codimension) this gives the estimates deg ⁡ Ω ≤ 6 ​ μ + 1 \deg\Omega\leq 6\mu+1 and deg ⁡ ρ ≤ 14 ​ k \deg\rho\leq 14k.

### 4.2. Principal functional–Pfaffian system

We proceed with writing down the principal functional–Pfaffian system explicitly. Slightly abusing notation, we add the subscript j j for objects related to the j j th singularity, while letters without this subscript refer to objects related to the entire polycycle. In this notation we omit the reference to the characteristic size, still keeping in mind that all formulas are explicitly polynomial in r r.

Notations Denote by M j M_{j} the domain from Table 2, associated with the j j -th singular standard map, let γ j \gamma_{j} be the corresponding manifold (separating solution) and by Ω j \Omega_{j} the tuple of Pfaffian forms on it: if the singularity is of the type D μ D_{\mu} or S 0 S_{0}, then Ω j \Omega_{j} consists of only one form ω j = A j ​ d ​ x j + B j ​ d ​ y j \omega_{j}=A_{j}\,dx_{j}+B_{j}\,dy_{j}, while in the case S μ S_{\mu}, μ > 0 \mu>0, there are three forms, of which we denote the third one by A j ​ d ​ x j + B j ​ d ​ y j A_{j}\,dx_{j}+B_{j}\,dy_{j}, (see Table 2). The covering function for M j M_{j} is denoted by ρ j: M j → ℝ + 1 \rho_{j}:M_{j}\to\mathbb{R}^{1}_{+}.

Construction of the principal system The phase space for the principal functional–Pfaffian system is the Cartesian product of phase spaces corresponding to all the vertices of the polycycle and the r r -cube in the ϵ \epsilon -space:

(40) |  | M = M ( r) = M 1 × ⋯ × M n × B ~ r, M j = M j, r ​ are taken from the second column of Table 2, B ~ r = { | ϵ i | < r, i = 1, …, k }. \displaystyle\begin{aligned} M=M(r)=M_{1}\times&\cdots\times M_{n}\times\tilde{B}_{r},\\ M_{j}=M_{j,r}{\text{ are taken from the}}&{\text{ second column of Table 2}},\\ \tilde{B}_{r}=\{|\epsilon_{i}|<r,&\ i=1,\dots,k\}.\end{aligned} |  |

Dimension of the phase space is equal to 2 ​ n + 2 ​ s + k + m 2n+2s+k+m, where:

∙ \bullet k k is the number of the parameters ϵ \epsilon (the principal integer index);

∙ \bullet n ≤ k n\leq k is the number of vertices;

∙ \bullet s ≤ n s\leq n is the number of resonant saddles on the polycycle (each such a vertex contributes two additional variables z j, w j z_{j},w_{j} into the list of independent variables);

∙ \bullet m = n + ∑ μ j ≤ n + k ≤ 2 ​ k m=n+\sum\mu_{j}\leq n+k\leq 2k is the number of additional free parameters λ = ( λ 1, …, λ n) \lambda=(\lambda^{1},\dots,\lambda^{n}), λ j ∈ ℝ μ j + 1 \lambda^{j}\in\mathbb{R}^{\mu_{j}+1}.

The covering function for such a space is the product

(41) |  | ρ = ρ 1 ⋯ ρ n ⋅ ρ ϵ: M → ℝ 1 +, \displaystyle\rho=\rho_{1}\cdots\rho_{n}\cdot\rho_{\epsilon}:M\to\mathbb{R}^{1}_{+}, |  |

where the last factor is the covering function for B ~ r \tilde{B}_{r}. From Table 2 it is clear that ρ \rho is a polynomial of degree at most ∑ j ( 6 ​ μ j + 8) ≤ 14 ​ k \sum_{j}(6\mu_{j}+8)\leq 14k in both phase variables and the characteristic size r r.

Each form on M j M_{j} can be pulled back on M M, yielding the form which is independent of all the coordinates except for those related to the j j th vertex. Denote by Ω \Omega the union of the tuples Ω ( j) \Omega^{(j)}: thus Ω \Omega is itself the tuple of 1-forms on M M, containing n + 2 ​ s n+2s of them:

(42) |  | Ω = ( Ω ( 1), …, Ω ( n)) = ( Ω 1, …, Ω n + 2 ​ s), Ω ( j) = { { ω j } if j is not a resonant saddle, { ω j ​ 1, ω j ​ 2, ω j } otherwise, where ω j ​ 1 = m j ​ x j ​ d ​ z j − z j ​ d ​ x j, ω j ​ 2 = n j ​ y j ​ d ​ w j − w j ​ d ​ y j, ω j = A j ​ d ​ x j + B j ​ d ​ y j. \displaystyle\begin{aligned} \Omega=(\Omega^{(1)},\dots,\Omega^{(n)})=(\Omega_{1},\dots,\Omega_{n+2s}),\\ \Omega^{(j)}=\begin{cases}\left\{\omega_{j}\right\}\ \ \ {\text{if $j$ is not a resonant saddle,}}\\ \left\{\omega_{j1},\omega_{j2},\omega_{j}\right\}\ \ {\text{otherwise,}}\end{cases}\\ {\text{where}}\ \ \ \omega_{j1}=m_{j}x_{j}\,dz_{j}-z_{j}\,dx_{j},\qquad&\omega_{j2}=n_{j}y_{j}\,dw_{j}-w_{j}\,dy_{j},\\ \omega_{j}=A_{j}\,dx_{j}+&B_{j}\,dy_{j}.\end{aligned} |  |

Each γ j \gamma_{j} is a separating solution to the Pfaffian equation or system of equations Ω ( j) = 0 \Omega^{(j)}=0 on M j M_{j}, therefore the Cartesian product

 | Γ = γ 1 × ⋯ × γ n × B ~ r \Gamma=\gamma_{1}\times\cdots\times\gamma_{n}\times\tilde{B}_{r} |  |

is the separating solution to the Pfaffian system Ω = 0 \Omega=0 on M M. Indeed, one may consider the chain of submanifolds

 | Γ i = γ 1 × ⋯ × γ i × M i + 1 × ⋯ × M n × B ~ r \Gamma_{i}=\gamma_{1}\times\cdots\times\gamma_{i}\times M_{i+1}\times\cdots\times M_{n}\times\tilde{B}_{r} |  |

This chain possesses all the properties required by the definition of a separating solution, see section 3: there are no singular points of Pfaffian forms on all the manifolds from this chain, and the topological condition of Γ i + 1 \Gamma_{i+1} being the boundary of a domain in Γ i \Gamma_{i} is trivially satisfied, because each γ i + 1 \gamma_{i+1} is the boundary of the corresponding subdomain in M j M_{j}. Thus the Pfaffian part of the principal system is constructed.

In this Pfaffian part we have the following information about the polynomials (recall that 𝒮 a \mathcal{S}_{a} stands for the algebraic part of the specification for the basic system, which is identified by ( 38) with a tuple of real variables):

(43) |  | A j, B j ∈ ℤ ⁡ [x, y, λ, 𝒮 a], deg ⁡ A j, deg ⁡ B j ≤ 6 ​ μ + 1, ρ ∈ ℤ [x, y, λ, ϵ, r], deg ρ ≤ 14 k. \displaystyle\begin{aligned} A_{j},B_{j}\in\mathbb{Z}[x,y,\lambda,\mathcal{S}_{a}],\qquad\deg A_{j},\deg B_{j}\leq 6\mu+1,\\ \rho\in\mathbb{Z}[x,y,\lambda,\epsilon,r],\qquad\deg\rho\leq 14k.\end{aligned} |  |

Now we proceed with description of the functional part of the principal system. It is given by the map

(44) |  | F = ( F 1, …, F n + k + m): M → ℝ n + k + m, F j = { x j + 1 − f j ​ ( y j, ϵ), j = 1, …, n mod ( n), ϵ j − n, j = n + 1, …, n + k, λ j − n − k, j = n + k + 1, …, n + k + m. \displaystyle\begin{aligned} F=(F_{1},\dots,F_{n+k+m}):M\to\mathbb{R}^{n+k+m},\\ F_{j}=\begin{cases}x_{j+1}-f_{j}(y_{j},\epsilon),&\quad j=1,\dots,n\mod(n),\\ \epsilon_{j-n},&\quad j=n+1,\dots,n+k,\\ \lambda_{j-n-k},&\quad j=n+k+1,\dots,n+k+m.\end{cases}\end{aligned} |  |

The dimension of a generic fiber F − 1 ​ ( ⋅) F^{-1}(\cdot) is equal to the codimension of separating solutions of the Pfaffian system. An essential feature of the above map is the following one: the coordinate functions of the map F F are polynomial combinations of the coordinates on the source space and generic functions f j f_{j}:

(45) |  | F j ∈ ℤ ⁡ [x, ϵ, λ, 𝐟], deg ⁡ 𝐅 𝐣 = 𝟏, \displaystyle F_{j}\in\mathbb{Z}[x,\epsilon,\lambda,\bf f],\hskip 22.99988pt\deg F_{j}=1, |  |

and all coefficients of those polynomials are ± 1 \pm 1. A more invariant way of formulating the same property is to say that F F is a polynomial map defined on the space of 0 0 -jets of vector-functions

(46) |  | 𝐟: 𝐌 → ℝ 𝐧, \displaystyle\bf f:M\to\mathbb{R}^{n}, |  |

and this phrase makes sense since M M is a subset of a Euclidean space.

###### Definition 21.

The functional–Pfaffian system with the Pfaffian equations ( 42), the functional equations ( 44), defined on the domain ( 40) considered with the covering function ( 41), will be called the principal functional–Pfaffian system. The information provided by the estimates ( 43), ( 45) allows us to say that the principal system is effectively described.

Later on we will refer to the principal system as simply the system ( 39).

### 4.3. Reduction to singularity theory

The system ( 39), whose Khovanski number majorizes the number of solutions to the basic system ( 12), satisfies the conditions of Theorem 18. The conclusion of the latter claims that the number 𝒦 ​ { Ω, F; ω } \mathcal{K}\{\Omega,F;\omega\} is in turn majorized by the combination of Khovanski numbers for some 2 ​ n + 2 ​ s + k + m + 1 2n+2s+k+m+1 entirely rigid systems (recall that n + 2 ​ s n+2s is the number of Pfaffian equations and n + k + m n+k+m is the number of loose functional equations in the principal system, which should be eliminated). The properties of the principal system, listed in the formulation of Theorem 20, yield a complete description of the resulting systems as chain maps (the definition is given below).

In what follows we treat the original variables x j, y j x_{j},y_{j}, the auxiliary variables z j α, w j α z_{j_{\alpha}},w_{j_{\alpha}} and the parameters ϵ, λ \epsilon,\lambda in almost the similar way, as it is suggested by the functional equations ( 44) of the principal system ( 39). The algebraic part 𝒮 a \mathcal{S}_{a} of the specification, however, plays a different role: the coordinates of the localization points 𝐜 𝐣 \bf c_{j} and the integers n j α, m j α n_{j_{\alpha}},m_{j_{\alpha}} determining the hyperbolicity ratios of resonant saddles, would determine the point in the new phase space, around which the resulting chain maps will be considered. Recall that in § ​ 1 \lx@sectionsign 1 we introduced the vectors 𝐜 𝐣 \bf c_{j} and 𝐜 \bf c as

 | 𝐜 j = ( 0, …, 0, c j) ∈ ℝ μ j + 1, c j ∈ ℝ 1, 𝐜 = ( 𝐜 1, …, 𝐜 n) ∈ ℝ m, m = n + ∑ μ j. \displaystyle\begin{aligned} {\bf c}_{j}=(0,\dots,0,c_{j})\in\mathbb{R}^{\mu_{j}+1},\qquad c_{j}\in\mathbb{R}^{1},\\ {\bf c}=({\bf c}_{1},\dots,{\bf c}_{n})\in\mathbb{R}^{m},\qquad m=n+\sum\mu_{j}.\end{aligned} |  |

For our purposes it would be convenient to consider all (new) variables as taking values around the origin in the corresponding phase space. For this sake we make a parallel translation in the λ \lambda -space, which would take the origin into the point 𝐜 \bf c. Clearly, this translation does not affect the algebraic structure of the principal system ( 39), though changes the appearance of the equations.

The characteristic size r r retains its original meaning.

Notations According to what has been said, we introduce the following notations:

 | 𝐱 = ( x, y, z, w, ϵ, λ − 𝐜) ∈ ℝ 2 ​ n + 2 ​ s + k + m, 𝐟 = ( f 1, …, f n), f j = f j ( y j, ϵ) ⇔ 𝐟 = 𝐟 ( 𝐱), \displaystyle\begin{aligned} {\bf x}&=(x,y,z,w,\epsilon,\lambda-{\bf c})\in\mathbb{R}^{2n+2s+k+m},\\ {\bf f}&=(f_{1},\dots,f_{n}),\qquad f_{j}=f_{j}(y_{j},\epsilon)\iff{\bf f}={\bf f}({\bf x}),\end{aligned} |  |

where 𝐟 \bf f is now considered as a vector-function of the argument 𝐱 \bf x, though each coordinate function f j f_{j} of the vector 𝐟 \bf f depends in fact only on some of the coordinates of the vector 𝐱 \bf x. By D 𝗉 ​ 𝐟 D^{\mathsf{p}}\bf f we denote the collection of all partial derivatives of functions f j f_{j} of the order 𝗉 \mathsf{p}.

We will also use the same notation M ⁡ ( r) M(r) for the domain of the principal system, though in fact it would become a subset of the unit cube ‖ 𝐱 ‖ < r \|{\bf x}\|<r centered at the origin in the 𝐱 \bf x -space.

Now we can formulate the properties of the systems of equations which appear after elimination of Pfaffian equations from the principal system ( 39) as this was described in § 3.4. Let 𝐦 = 2 ​ n + 2 ​ s + k + m {\bf m}=2n+2s+k+m

###### Theorem 22.

Let 𝐦 = 2 ​ n + 2 ​ s + k + m {\bf m}=2n+2s+k+m. For any fixed combinatorial type 𝒯 \mathcal{T} of the principal functional-Pfaffian system ( 39), any choice of the algebraic part 𝒮 a \mathcal{S}_{a} of the specification and sufficiently fast decaying to zero sequence of numbers ϵ 1, …, ϵ 𝐦 \epsilon_{1},\dots,\epsilon_{\bf m}, the number of nondegenerate solutions to the principal system in the domain M ⁡ ( r) M(r) for any choice of the characteristic size r > 0 r>0 does not exceed the sum of the Khovanski numbers for 𝐦 + 𝟏 \bf m+1 entirely rigid system of equations in the same domain. Each of these systems has the form

(47) |  | 𝐏 ( 𝐱, 𝐟 ( 𝐱), D 1 𝐟 ( 𝐱), …, D 𝐦 𝐟 ( 𝐱); 𝒮 a, r) = ( ϵ 1, …, ϵ 𝐦), 𝐱 ∈ M ( r) ⊆ ℝ 𝐦, \displaystyle\begin{aligned} {\bf P}\big({\bf x},{\bf f}({\bf x}),D^{1}{\bf f}({\bf x}),\dots,D^{\bf m}{\bf f}({\bf x});\mathcal{S}_{a},r\big)=(\epsilon_{1},\dots,\epsilon_{\bf m}),\ {\bf x}\in M(r)\subseteq\mathbb{R}^{\bf m},\end{aligned} |  |

where

∙ \bullet 𝐦 ≤ 7 ​ k {\bf m}\leq 7k is the total number of variables ( the dimension of the phase space);

∙ \bullet 𝐏 {\bf P} is a vector polynomial, 𝐏 = ( P 1, …, P 𝐦) {\bf P}=(P_{1},\dots,P_{\bf m}), P i ∈ ℤ ⁡ [𝐱, …; 𝒮 a, r] P_{i}\in\mathbb{Z}[{\bf x},\dots;\mathcal{S}_{a},r]; the degrees of each polynomial P i P_{i} is bounded by 14 ​ k ​ 2 i 14k2^{i} i = 1, …, 𝐦 i=1,\dots,\bf m;

∙ \bullet the domain M ⁡ ( r) M(r) belongs to the r r -cube of the space ℝ 𝐦 \mathbb{R}^{\bf m}, centered at the origin.

### 4.4. Chain maps and related finiteness theorems

Now we proceed with a more invariant description of the geometric object corresponding to the system of equations ( 47).

###### Definition 23.

Let ℝ 𝐦 \mathbb{R}^{\bf m} be a Euclidean space with a fixed coordinate system 𝐱 = ( X 1, …, X 𝐦) {\bf x}=(X_{1},\dots,X_{\bf m}), and U ⊆ ℝ 𝐦 U\subseteq\mathbb{R}^{\bf m} a domain of the rectangular form,

 | U = { α i < X i < β i, i = 1, …, 𝐦 }. U=\{\alpha_{i}<X_{i}<\beta_{i},\ i=1,\dots,\bf m\}. |  |

Denote by I I the index subset I = { 1, …, 𝐦 } I=\{1,\dots,\bf m\} enumerating the coordinates in ℝ 𝐦 \mathbb{R}^{\bf m}, and let for any j = 1, …, 𝐧 j=1,\dots,\bf n I j I_{j} be a nonempty subset of I I,

 | ∅ ≠ I j ⊆ I, j = 1, …, 𝐧. \varnothing\neq I_{j}\subseteq I,\qquad j=1,\dots,\bf n. |  |

We say that a vector-valued function

 | 𝐟: U ↦ ℝ 𝐧, 𝐟 = ( f 1, …, f 𝐧), {\bf f}:U\mapsto\mathbb{R}^{\bf n},\qquad{\bf f}=(f_{1},\dots,f_{\bf n}), |  |

is a Cartesian function of the Cartesian type ℐ = ( I 1, …, I 𝐧) \mathcal{I}=(I_{1},\dots,I_{\bf n}), if for any j j the j j th component of this function depends only on the coordinates X i X_{i} with i ∈ I j i\in I_{j}: in other words,

 | ∀ i ∉ I j ∂ f j ∂ X i ≡ 0. \forall i\notin I_{j}\quad\frac{\partial f_{j}}{\partial X_{i}}\equiv 0. |  |

For any given Cartesian type ℐ \mathcal{I} with 𝐧 = 𝟏 {\bf n=1} the set of all C 𝗉 C^{\mathsf{p}} -smooth Cartesian functions (iėĊartesian maps with 𝐧 = 𝟏 \bf n=1) of this type constitutes a Banach space with the natural C 𝗉 C^{\mathsf{p}} -norm. We denote this space by 𝐂 ℐ 𝗉 {\bf C}^{\mathsf{p}}_{\mathcal{I}}, sometimes omitting the explicit reference to the type ℐ \mathcal{I} when the latter is clear from context. The space 𝐂 ℐ 𝗉 {\bf C}^{\mathsf{p}}_{\mathcal{I}} will be referred to as the Cartesian space. In the same way the Cartesian spaces of maps arise. As a consequence, we may say about genericity of Cartesian maps (functions) within the given Cartesian type; the notions of openness and density of subsets are also naturally defined.

###### Definition 24.

Let 𝐟 \bf f be a C 𝗉 C^{\mathsf{p}} -smooth Cartesian map of a given Cartesian type ℐ \mathcal{I}, and s ≥ 0 s\geq 0 an nonnegative integer number, s ≤ 𝗉 s\leq\mathsf{p}. A Cartesian s s -jet of the function 𝐟 \bf f at a point 𝐱 𝟎 ∈ 𝐔 \bf x_{0}\in U is the equivalence class of all Cartesian functions of the same Cartesian type, which differ from 𝐟 \bf f by a term which is s s -flat at 𝐱 𝟎 \bf x_{0}:

 | 𝐣 𝐬 ​ 𝐟 ​ ( 𝐱 𝟎) = { 𝐠 ∈ 𝐂 ℐ 𝗉: | 𝐟 − 𝐠 | = 𝐨 ⁡ ( | 𝐱 − 𝐱 𝟎 | 𝐬) }. \bf j^{s}{\bf f}({\bf x}_{0})=\{{\bf g}\in{\bf C}^{\mathsf{p}}_{\mathcal{I}}:|{\bf f}-{\bf g}|=o(|{\bf x}-{\bf x}_{0}|^{s})\}. |  |

The space of all s s -jets of functions of the given Cartesian type ℐ \mathcal{I} at all points 𝐱 0 ∈ U {\bf x}_{0}\in U will be denoted by 𝐉 ℐ s ​ ( ℝ 𝐦, ℝ 𝐧) {\bf J}^{s}_{\mathcal{I}}(\mathbb{R}^{\bf m},\mathbb{R}^{\bf n}) or simply by 𝐉 𝐬 \bf J^{s}, when the environment is unambiguously defined by the context.

The map

 | 𝐱 ↦ 𝐣 𝐬 ​ 𝐟 ​ ( 𝐱) {\bf x}\mapsto\bf j^{s}{\bf f}(\bf x) |  |

is called the Cartesian s s -jet extension of the Cartesian map 𝐟 \bf f.

The space of Cartesian jets of any type and any finite order admits a natural coordinate system, in which the Cartesian jet extension of a map 𝐟 = ( f 1, …, f 𝐧) {\bf f}=(f_{1},\dots,f_{\bf n}) takes the form

 | 𝐱 = ( X 1, …, X M) ↦ ( 𝐗, ℱ ( 𝐗), { ∂ F j ∂ X i, i ∈ I j }, …, OPEN { all partial derivatives of functions ​ f j ​ of all orders up to s ​ in the variables on which each ​ f j ​ actually depends }) \displaystyle\begin{aligned} {\bf x}=(X_{1},\dots,X_{M})\mapsto\biggl({\bf X},{\mathcal{F}}({\bf X}),\left\{\dfrac{\partial{F_{j}}}{\partial{X_{i}}},\ i\in I_{j}\right\},\dots,\\ \biggl\{\begin{aligned} \text{all partial derivatives of functions}\ f_{j}\ \text{of all orders up to}\\ \ s\ \text{in the variables on which each }\ f_{j}\ \text{actually depends}\end{aligned}\biggr\}\biggr)\end{aligned} |  |

The Cartesian jet spaces possess almost all properties of the standard jet spaces. In particular, the natural projections

(48) |  | ℝ M ⊇ U ← p ​ r 0 𝐉 0 ≃ ℝ M × ℝ K ← p ​ r 1 ⋯ ← p ​ r s 𝐉 s ← p ​ r s + 1 ⋯ \displaystyle\begin{CD}{\mathbb{R}}^{M}\supseteq U@<{pr_{0}}<{}<{\bf J}^{0}\simeq{\mathbb{R}}^{M}\times{\mathbb{R}}^{K}@<{pr_{1}}<{}<\cdots @<{pr_{s}}<{}<{\bf J}^{s}@<{pr_{s+1}}<{}<\cdots\end{CD} |  |

are well defined and endow each 𝐉 ℐ 𝐬 \bf J^{s}_{\mathcal{I}} with the structure of an affine bundle over ℝ 𝐦 \mathbb{R}^{\bf m}. Thus it makes sense to say about polynomial functions defined on Cartesian bundles.

###### Definition 25.

A chain map with the exterior part 𝐏 \bf P and the interior part 𝐟 \bf f is a map of the form

 | ℝ 𝐦 ⊇ U ∋ 𝐱 ↦ 𝐏 ⁡ ( 𝐣 ℐ 𝐬 ​ 𝐟 ​ ( 𝐱)) ∈ ℝ 𝐦, \mathbb{R}^{\bf m}\supseteq U\owns{\bf x}\mapsto{\bf P}(\bf j^{s}_{\mathcal{I}}{\bf f}({\bf x}))\in\mathbb{R}^{\bf m}, |  |

where:

∙ \bullet 𝐟 \bf f is a Cartesian map from a certain Cartesian space 𝐂 ℐ 𝗉 ​ ( ℝ 𝐦, ℝ 𝐧) \bf C^{\mathsf{p}}_{\mathcal{I}}(\mathbb{R}^{\bf m},\mathbb{R}^{\bf n}), and 𝐣 ℐ 𝐬 \bf j^{s}_{\mathcal{I}} is the corresponding s s -jet extension of 𝐟 \bf f;

∙ \bullet 𝐏: 𝐉 ℐ s ​ ( ℝ 𝐦, ℝ 𝐧) → ℝ 𝐦 {\bf P}:{\bf J}^{s}_{\mathcal{I}}(\mathbb{R}^{\bf m},\mathbb{R}^{\bf n})\to\mathbb{R}^{\bf m} is a vector polynomial (eventually depending polynomially on some additional parameters),

∙ \bullet the composite map is between the spaces of the same dimension: dim 𝐱 = dim 𝐏 = 𝐦 \dim{\bf x}=\dim{\bf P}={\bf m}.

Having introduced the notions of Cartesian functions, maps, jets etc, we can describe the system (3.10) as a chain map defined on a small cube of some size r > 0 r>0 with the exterior part 𝐏 \bf P which is a polynomial with integer coefficients and of a controlled complexity; this polynomial depends on r r and some additional variables 𝐀 \bf A as well, and the interior part 𝐟 \bf f belongs to some Cartesian space, since the functions f j f_{j} depend only on some components of the vector 𝐱 = ( x, y, z, w, ϵ, λ − 𝐜) {\bf x}=(x,y,z,w,\epsilon,\lambda-{\bf c}) (recall that all nonzero coordinates of the vector 𝐜 \bf c are already included among the variables 𝒮 a \mathcal{S}_{a}). Thus our problem of estimating cyclicity of a polycycle takes the following form: describe the Cartesian maps 𝐟 \bf f for which the chain map admits an upper estimate for the number of preimages of regular values.

Consider chain maps of the form

 | 𝐱 ↦ 𝐆 r ​ ( 𝐱) = 𝐏 ⁡ ( 𝐣 ℐ 𝐬 ​ 𝐟 ​ ( 𝐱), 𝐫) = ( 𝐏 𝟏, …, 𝐏 𝐦) ​ ( 𝐣 ℐ 𝐬 ​ 𝐟 ​ ( 𝐱), 𝐫), 𝐱 ∈ 𝐔 ⊂ ℝ 𝐦, 𝐫 > 𝟎, \displaystyle{\bf x}\mapsto{\bf G}_{r}(\bf x)={\bf P}(\bf j^{s}_{\mathcal{I}}{\bf f}({\bf x}),r)=(P_{1},\dots,P_{\bf m})(\bf j^{s}_{\mathcal{I}}{\bf f}({\bf x}),r),\hskip 22.99988pt{\bf x}\in U\subset\mathbb{R}^{\bf m},\ r>0, |  |

depending polynomially on an additional variable r r, so that

(49) |  | 𝐏: 𝐉 ℐ s ​ ( ℝ 𝐦, ℝ 𝐧) × ℝ 1 → ℝ 𝐦, 𝐟 ∈ 𝐂 ℐ 𝗉 ​ ( U, ℝ 𝐧). \displaystyle{\bf P}:{\bf J}^{s}_{\mathcal{I}}(\mathbb{R}^{\bf m},\mathbb{R}^{\bf n})\times\mathbb{R}^{1}\to\mathbb{R}^{\bf m},\quad{\bf f}\in{\bf C}^{\mathsf{p}}_{\mathcal{I}}(U,\mathbb{R}^{\bf n}). |  |

We assume that the polynomial 𝐏 \bf P and the Cartesian type ℐ \mathcal{I} are fixed (and U U denotes as before a unit cube) and 𝐏 \bf P is nontrivial polynomial, i.e. at some point x ∈ U x\in U the linearization matrix d ​ P ​ ( x) dP(x) has full rank.

Suppose that the smoothness order 𝗉 \mathsf{p} is sufficiently high,

 | 𝗉 > 𝐦 + 𝟏. \mathsf{p}>\bf m+1. |  |

###### Theorem 26.

For any polynomial 𝐏 = ( P 1, …, P 𝐦) {\bf P}=(P_{1},\dots,P_{\bf m}) as in ( 49) one may choose a subset 𝖥 𝐏 ⊂ 𝐂 ℐ 𝗉 ​ ( U, ℝ 𝐧) \mathsf{F}_{\bf P}\subset{\bf C}^{\mathsf{p}}_{\mathcal{I}}(U,\mathbb{R}^{\bf n}) in the space of Cartesian functions of the given type, which is open and dense in this space such that for any Cartesian function 𝐟 ∈ 𝖥 𝐏 {\bf f}\in\mathsf{F}_{\bf P} and any sufficiently quickly decaying sequence a 1, …, a 𝐦 a_{1},\dots,a_{\bf m} there exists a characteristic size r 0 > 0 r_{0}>0 such that the number of preimages of ( a 1, …, a 𝐦) (a_{1},\dots,a_{\bf m}) admits the following upper estimate:

(50) |  | lim sup r → 0 + #⁡ { 𝐱 ​ 𝐱 ∈ U r, 𝐆 r ​ ( 𝐱) = ( a 1, …, a 𝐦) } ≤ ∏ i = 1 𝐦 deg ⁡ P i ≤ 2 25 ​ k 2. \displaystyle\limsup_{r\to 0^{+}}\#\{{\bf x}\>\ {\bf x}\in U_{r},\ {\bf G}_{r}({\bf x})=(a_{1},\dots,a_{\bf m})\}\leq\prod_{i=1}^{\bf m}\deg P_{i}\leq 2^{25k^{2}}. |  |

A bit of terminology: “Replace an n n -th jet j n ​ F j^{n}F by its linear part at a point a ∈ ℝ n a\in\mathbb{R}^{n} ” means “replace the map j n ​ F: ℝ n → J n ​ ( ℝ n, ℝ n) j^{n}F:\mathbb{R}^{n}\to J^{n}(\mathbb{R}^{n},\mathbb{R}^{n}) by its linear part L F, a, n L_{F,a,n} at the point a a ”.

By the phrase “a map G: M → N G:M\to N of manifolds satisfies a transversality condition ” we mean that for some manifold (resp. a collection of manifolds) in the image N N the map G G is transversal to this manifold (resp. these manifolds).

The second stage consists in constructing a stratification of the n n -jet space J n ​ ( ℝ n, ℝ n) J^{n}(\mathbb{R}^{n},\mathbb{R}^{n}) (a decomposition into a disjoint union of manifolds described below) such that if the n n -jet j n ​ F j^{n}F is transversal to all manifolds of this stratification, then the following theorem is true:

###### Theorem 27.

Let P = ( P 1, …, P n) P=(P_{1},\dots,P_{n}) be a nontrivial polynomial defined on the space of n n -jets P: J n ​ ( ℝ n, ℝ n) → ℝ n P:J^{n}(\mathbb{R}^{n},\mathbb{R}^{n})\to\mathbb{R}^{n} and let F: ℝ n → ℝ n F:\mathbb{R}^{n}\to\mathbb{R}^{n} be a C k C^{k} smooth map, k > n k>n. Suppose the n n -jet j n ​ F j^{n}F satisfies a transversality condition depending only on P P. Then for a sufficiently small r r one can replace in the statement of the previous theorem the n n -jet j n ​ F j^{n}F at the point a a by its linear part L F, a, n L_{F,a,n}. Namely,

(51) |  | #{ x ∈ B r ( a): P 1 ∘ j n F ( x) = a 1, …, P n ∘ j n F ( x) = a n } = #{ x ∈ B r ( a): P 1 ∘ L F, a, n ( x) = a 1, …, P n ∘ L F, a, n ( x) = a n }, \displaystyle\begin{aligned} \#\{x\in B_{r}(a):\ \ P_{1}\circ j^{n}F(x)=a_{1},\dots,P_{n}\circ j^{n}F(x)=a_{n}\}=\\ \#\{x\in B_{r}(a):\ \ P_{1}\circ L_{F,a,n}(x)=a_{1},\dots,P_{n}\circ L_{F,a,n}(x)=a_{n}\},\end{aligned} |  |

where a 1, …, a n a_{1},\dots,a_{n} go to zero sufficiently fast. By Bezout’s theorem the number of solutions to the equation in the right-hand side of ( 51) can be bounded by the product ∏ i = 1 n deg ⁡ P i \prod_{i=1}^{n}\deg P_{i}.

The classical transversality theorem [AGV] says that for a generic map F F its n n -jet j n ​ F j^{n}F satisfies any ahead given transversality condition.

### 4.5. Stratified manifolds

Now we recall basic definitions from the theory of stratified sets.

Let M M be a smooth manifold, which we call the ambient manifold. Consider a singular subset V ⊂ M V\subset M. Roughly speaking a stratification of V V is a decomposition of V V into a disjoint union of manifolds (strata) { V α } α \{V_{\alpha}\}_{\alpha} such that strata of bigger dimension are attached to strata of smaller dimension in a “regular” way.

“Regular” will obtain a precise meaning in a moment, but the most important property is that transversality to a smaller stratum implies transversality to an “attached” bigger stratum. Now we are going to describe the standard language of stratified manifolds and maps of stratified manifolds. This goes back to Whitney and Thom [W], [Th].

Recall the Whitney Conditions (a) and (b). Condition (a) is similar to the notion of a P a_{P} -stratification due to Thom [Th] defined in the next subsection. We shall use a P a_{P} -stratification to prove condition ( 10).

Consider a triple ( V β, V α, x) (V_{\beta},V_{\alpha},x), where V β, V α V_{\beta},\ V_{\alpha} are C 1 C^{1} manifolds, x x is a point in V β V_{\beta} and V β ⊆ V ¯ α ∖ V α V_{\beta}\subseteq\bar{V}_{\alpha}\setminus V_{\alpha}.

###### Definition 28.

A triple ( V β, V α, x) (V_{\beta},V_{\alpha},x) satisfies the Whitney (a) condition if for any sequence of points { x k } ⊂ V α \{x_{k}\}\subset V_{\alpha} converging to a point x ∈ V β x\in V_{\beta} the sequence of tangent planes T k = T x k ​ V α T_{k}=T_{x_{k}}V_{\alpha} converges in the corresponding Grassmanian manifold of dim V α \dim V_{\alpha} -planes in T ​ M TM and lim T k = τ ⊃ T x ​ V β \lim T_{k}=\tau\supset T_{x}V_{\beta}.

###### Definition 29.

A triple ( V β, V α, x) (V_{\beta},V_{\alpha},x) satisfies the Whitney (b) condition if for any two sequences of points { x k } ⊂ V α \{x_{k}\}\subset V_{\alpha}, { y k } ⊂ V α \{y_{k}\}\subset V_{\alpha} converging to a point x ∈ V β x\in V_{\beta} the sequence of “vectors” y k − x k | y k − x k | \frac{y_{k}-x_{k}}{|y_{k}-x_{k}|} converges to a vector v ∈ T x ​ M v\in T_{x}M which belongs to a limiting position of lim T x k ​ V α = τ \lim T_{x_{k}}V_{\alpha}=\tau, i.e. v ∈ τ v\in\tau.

Since condition (b) is local one can think of M M as Euclidean. This explains how to interpret the vector y k − x k | y k − x k | \frac{y_{k}-x_{k}}{|y_{k}-x_{k}|}.

It is easy to show that condition (b) implies condition (a).

###### Definition 30.

A locally closed subset V V in the ambient manifold M M is called a stratified manifold (set, variety) in M M, if it is represented as a locally finite disjoint union of smooth submanifolds V α V_{\alpha} of M M, called strata, of different dimensions in such a way that the closure of each stratum consists of itself and the union of some other strata of strictly smaller dimensions, and Condition (b) of Whitney is satisfied.

Any union of submanifolds satisfying condition of this definition

(52) |  | V = ∪ α V α \displaystyle V=\cup_{\alpha}V_{\alpha} |  |

is called a stratification of V V, and the submanifolds V α V_{\alpha} are called strata. A set V V is stratifiable if there is a “nice” partition into strata. By a stratified manifold we mean a pair ( V, 𝒱) (V,\mathcal{V}) consisting of a manifold V V itself and a partition 𝒱 = { V α } \mathcal{V}=\{V_{\alpha}\}.

### 4.6. Stratified maps and a P a_{P} -stratification

Now we define a smooth map of a stratified manifold ( V, 𝒱) (V,\mathcal{V}):

###### Definition 31.

Let ( V, 𝒱) (V,\mathcal{V}) be a stratified manifold in an ambient manifold M M, V ⊆ M V\subseteq M, then a map f: V → N f:V\to N is called C 2 C^{2} -smooth if it can be extended to a C 2 C^{2} smooth map of the ambient manifold M M F: M → N F:M\to N whose restriction to V V coincides with f f.

A stratification V = ∪ α V α V=\cup_{\alpha}V_{\alpha} stratifies a smooth map f: V → ℝ k f:V\to\mathbb{R}^{k} if the restriction of f f to any stratum V α V_{\alpha} has constant rank, i.e., rank d ​ f | V α ​ ( x) df|_{V_{\alpha}}(x) is independent of x ∈ V α x\in V_{\alpha}.

A map G: L → M G:L\to M is called transversal to a stratified set ( V, 𝒱) (V,\mathcal{V}) if G G is transversal to each strata V α ∈ 𝒱 V_{\alpha}\in\mathcal{V}.

By the Rank Theorem, if a stratification ( V, 𝒱), 𝒱 = { V α } α ∈ I (V,\mathcal{V}),\ \mathcal{V}=\{V_{\alpha}\}_{\alpha\in I} stratifies a smooth map P P, then for each strata V α V_{\alpha} the number d α ​ ( P) = dim V α − rank ​ d ​ P | V α d_{\alpha}(P)=\dim V_{\alpha}-{\text{rank}}\ dP|_{V_{\alpha}} is well defined.

Assume d α ​ ( P) ≥ d β ​ ( P) d_{\alpha}(P)\geq d_{\beta}(P) for each V β ⊆ V ¯ α ∖ V α V_{\beta}\subseteq\bar{V}_{\alpha}\setminus V_{\alpha}, i.e. nonempty level sets inside the bigger stratum V α V_{\alpha} have dimension d α ​ ( P) d_{\alpha}(P) greater or equal to dimension of the level sets d β ​ ( P) d_{\beta}(P) in the smaller stratum V β V_{\beta}. We require that for any sequence of points { a k } ⊂ P ⁡ ( V α) \{a_{k}\}\subset P(V_{\alpha}) converging to a point a ∈ P ⁡ ( V β) a\in P(V_{\beta}), the nonempty level sets { P − 1 ​ ( a k) ∩ V α } \{P^{-1}(a_{k})\cap V_{\alpha}\} approach the limiting level set { P − 1 ​ ( a) ∩ V β } \{P^{-1}(a)\cap V_{\beta}\} “regularly”. In other words, we require that the level sets in the bigger stratum V α V_{\alpha} approach the limit level set in the smaller stratum V β V_{\beta} nicely.

###### Definition 32.

Let P: M → N P:M\to N be a C 2 C^{2} smooth map of manifolds, and let V β V_{\beta} and V α V_{\alpha} be submanifolds of M M such that the restrictions P | V β P|_{V_{\beta}} to V β V_{\beta} and P | V α P|_{V_{\alpha}} to V α V_{\alpha} have constant ranks R V β ​ ( P) R_{V_{\beta}}(P) and R V α ​ ( P) R_{V_{\alpha}}(P), respectively. Let x x be a point in V β V_{\beta}.

We call the manifold V α V_{\alpha} a P a_{P} -regular over V β V_{\beta} with respect to the map P P at the point x x if for any sequence of points { x n } ⊂ V α \{x_{n}\}\subset V_{\alpha} converging to x ∈ V β x\in V_{\beta} the sequence of tangent planes to the level sets T k = k ​ e ​ r ​ d ​ P | V α ​ ( x k) T_{k}=ker\ dP|_{V_{\alpha}}(x_{k}) converges in the corresponding Grassmanian manifold of ( dim V α − R V α ​ ( P)) (\dim V_{\alpha}-R_{V_{\alpha}}(P)) -dimensional planes to a plane τ \tau and

(53) |  | lim k ​ e ​ r ​ d ​ P | V α ​ ( x k) = τ ⊇ k ​ e ​ r ​ d ​ P | V β ​ ( x) \displaystyle\lim ker\ dP|_{V_{\alpha}}(x_{k})=\tau\supseteq ker\ dP|_{V_{\beta}}(x) |  |

###### Definition 33.

A C 2 C^{2} smooth map P: V → N P:V\to N of a stratifiable manifold V V to a manifold N N is called a P a_{P} -stratifiable if there exist a stratification ( V, 𝒱) (V,\mathcal{V}) such that the following conditions hold:

a) ( V, 𝒱) (V,\mathcal{V}) stratifies the map P P (see definition 31);

b) for all pairs V β V_{\beta} and V α V_{\alpha} from 𝒱 \mathcal{V} such that V β ⊆ V ¯ α ∖ V α V_{\beta}\subseteq\bar{V}_{\alpha}\setminus V_{\alpha} the stratum V α V_{\alpha} is a P a_{P} -regular over the stratum V β V_{\beta} with respect to P P at point x x for all x ∈ V β x\in V_{\beta}.

The original definition of a P a_{P} -stratification requires an appropriate stratification of the image also [Ma], but we do not require stratification of the image for our purposes.

### 4.7. Relation between existence of a P a_{P} -stratification and condition ( 5).

In section 1.5.1 we showed that the key to the proof of Theorem 26 is condition ( 10) (see Proposition 1). Now we are going to reduce the question whether condition ( 10) is satisfied to the question whether an a P a_{P} -stratification of the polynomial P P exists.

Let P = ( P 1, P 2): ℝ N → ℝ 2 P=(P_{1},P_{2}):\mathbb{R}^{N}\to\mathbb{R}^{2} be a nontrivial polynomial, V = P 2 − 1 ​ ( 0) V=P_{2}^{-1}(0) and V 0 = ( P 1, P 2) − 1 ​ ( 0) V_{0}=(P_{1},P_{2})^{-1}(0) be level sets. Assume that there exists a stratification ( V, 𝒱) (V,\mathcal{V}) that stratifies the map P | V P|_{V} such that the zero level set V 0 V_{0} can be represented as a union of strata from 𝒱 \mathcal{V}, i.e., V 0 = ∪ α ∈ I 0 V α V_{0}=\cup_{\alpha\in I_{0}}V_{\alpha}. Denote this stratification of V 0 V_{0} by 𝒱 0 \mathcal{V}_{0}. Recall that a map F: ℝ k → ℝ N F:\mathbb{R}^{k}\to\mathbb{R}^{N} is transversal to a stratification ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) if it is transversal to each strata V α ∈ 𝒱 0 V_{\alpha}\in\mathcal{V}_{0}. Associate to each level set V a, a ≠ 0 V_{a},\ a\neq 0 a natural decomposition 𝒱 a = { V a ∩ V α } α ∈ I \mathcal{V}_{a}=\{V_{a}\cap V_{\alpha}\}_{\alpha\in I}.

###### Proposition 2.

With the above notation if a stratum V α ∈ 𝒱 ∖ 𝒱 0 V_{\alpha}\in\mathcal{V}\setminus\mathcal{V}_{0} is a P a_{P} -regular over a stratum V β ∈ 𝒱 0 V_{\beta}\in\mathcal{V}_{0} with respect to the polynomial P P, then any C 2 C^{2} smooth map F: ℝ n → ℝ 2 F:\mathbb{R}^{n}\to\mathbb{R}^{2} transversal to ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) is also transversal to V a ∩ V α V_{a}\cap V_{\alpha} for any small a a. This is equivalent to condition ( 10).

Proof Pick a point x x in V β ⊂ V 0 V_{\beta}\subset V_{0} and a point y ∈ V α y\in V_{\alpha}. Notice that k ​ e ​ r ​ d ​ P | V β ​ ( x) ker\ dP|_{V_{\beta}}(x) is the tangent plane to the level set { P − 1 ​ ( P ⁡ ( x)) ∩ V β } \{P^{-1}(P(x))\cap V_{\beta}\} at the point x x and k ​ e ​ r ​ d ​ P | V α ​ ( y) ker\ dP|_{V_{\alpha}}(y) is the tangent plane to the level set { P − 1 ​ ( P ⁡ ( y)) ∩ V α } \{P^{-1}(P(y))\cap V_{\alpha}\}.

By condition ( 53) if a map F: X → ℝ N F:X\to\mathbb{R}^{N} is transversal to k ​ e ​ r ​ d ​ P | V β ​ ( x) ker\ dP|_{V_{\beta}}(x) at a point x x, then F F is transversal to k ​ e ​ r ​ d ​ P | V α ​ ( y) ker\ dP|_{V_{\alpha}}(y) for any y ∈ V α y\in V_{\alpha} near x x.

Therefore, the condition “ F F is transversal to V β V_{\beta} at a point x x ” implies the condition “ F F is transversal to V α ∩ V a V_{\alpha}\cap V_{a} for any small a a ”. This completes the proof.

### 4.8. Existence of a P a_{P} -stratification for polynomial maps

The existence of a P a_{P} -stratifications is not a trivial question. There are some obvious obstacles. For example, let V ⊂ ℝ n V\subset\mathbb{R}^{n} be an algebraic variety and let P: ℝ n → ℝ k P:\mathbb{R}^{n}\to\mathbb{R}^{k} be a polynomial map. Assume that ( V, 𝒱) (V,\mathcal{V}) stratifies P P. If we have two strata V α V_{\alpha} and V β V_{\beta} so that V α V_{\alpha} lies “over” V β ⊆ V ¯ α ∖ V α V_{\beta}\subseteq\bar{V}_{\alpha}\setminus V_{\alpha}, then condition ( 53) can’t be satisfied if dimension of the level sets d α ​ ( P) d_{\alpha}(P) in the upper stratum V α V_{\alpha} is strictly less than that of d β ​ ( P) d_{\beta}(P) in the lower stratum V β V_{\beta}, i.e., dim k ​ e ​ r ​ d ​ P | V α ​ ( y) < dim k ​ e ​ r ​ d ​ P | V β \dim ker\ dP|_{V_{\alpha}}(y)<\dim ker\ dP|_{V_{\beta}}. In this case a plane k ​ e ​ r ​ d ​ P | V β ​ ( x) ker\ dP|_{V_{\beta}}(x) of the lower stratum V β V_{\beta} should belong to a plane τ \tau of smaller dimension (see condition ( 53)), which is impossible. Thom constructed the first example when this happens [GWPL].

Thom’s example

Consider the vector-polynomial P P in the form P: ( x, y) → ( x, x ​ y) P:(x,y)\to(x,xy). The line { x = 0 } \{x=0\} is the line of critical points of P P. Outside of the line { x = 0 } \{x=0\} P P is a diffeomorphism. Therefore, the preimage of any point a ≠ 0 a\neq 0 P − 1 ​ ( a) P^{-1}(a) is 0 0 -dimensional. On the other hand, the preimage of 0 0 is the line { x = 0 } \{x=0\}.

###### Definition 34.

Let us call an algebraic set V V rank compatible with a polynomial P P if there exists a stratification ( V, 𝒱) (V,\mathcal{V}) which stratifies P P and for any pair V α V_{\alpha} and V β V_{\beta} from 𝒱 \mathcal{V} such that V β ⊆ V ¯ α ∖ V α V_{\beta}\subseteq\bar{V}_{\alpha}\setminus V_{\alpha} dimensions of the levels d β ​ ( P) d_{\beta}(P) in the lower stratum V β V_{\beta} do not exceed dimensions of the level sets d α ​ ( P) d_{\alpha}(P) in the upper stratum V α V_{\alpha}.

It turns out that even if an algebraic set V V is rank compatible with a polynomial P P, then a P a_{P} -stratification still does not always exist. Let us present an example with this property. The example below belongs to M.Grinberg. It seems that the existence of a counterexample was known before, but we did not find an appropriate reference.

### 4.9. Nonexistence of a P a_{P} -stratification

Let V = { ( x, y, z, t) ∈ ℝ 4: x 2 = t 2 ​ y + z } V=\{(x,y,z,t)\in\mathbb{R}^{4}:\ x^{2}=t^{2}y+z\} be the three dimensional algebraic variety and P: V → ℝ 2 P:V\to\mathbb{R}^{2} be the natural projection to the last two coordinates, i.e. P: ( x, y, z, t) → ( z, t) P:(x,y,z,t)\to(z,t).

###### Proposition 3.

With the above notations the set V V is rank compatible with the polynomial map P P and does not have a P a_{P} -stratification.

Proof Consider a rank stratification of V V. Such a stratification consists of three stratum: V 1 = { x = t = z = 0 }, V 2 = { t = 0, x 2 = z, x ≠ 0 }, V_{1}=\{x=t=z=0\},\ V_{2}=\{t=0,\ x^{2}=z,\ x\neq 0\}, and V 3 = { t ≠ 0 }. V_{3}=\{t\neq 0\}. On each stratum rank P | V i = i − 1 P|_{V_{i}}=i-1. Level sets P − 1 ​ ( t, z) P^{-1}(t,z) —parabolas for t ≠ 0 t\neq 0 and lines for t = 0 t=0.

Show that for each point 𝐚 = ( 0, a, 0, 0) ∈ V 1 {\bf a}=(0,a,0,0)\in V_{1} there exists a family of level sets such that at the point 𝐚 \bf a the property a P a_{P} -regularity of V 3 V_{3} over V 1 V_{1} fails.

Consider the preimage of the curve { z = − a t 2 } ⊂ ℝ 2 \{z=-at^{2}\}\subset\mathbb{R}^{2}. This is an algebraic variety of the form W a = { x 2 = t 2 ( y − a) } W_{a}=\{x^{2}=t^{2}(y-a)\}. One can see that W a W_{a} is the Whitney umbrella.©The level x 2 = t 0 2 ​ ( y − a) x^{2}=t_{0}^{2}(y-a) is the parabola. As t 0 → 0 t_{0}\to 0 this parabola tends to semiline x = t = z = 0, y ≥ a {x=t=z=0,y\geq a}. At the point 𝐚 ∈ 𝐕 𝟏 \bf a\in V_{1} the property a P a_{P} -regularity of V 3 V_{3} over V 1 V_{1} clearly fails. This completes the proof of the Proposition.

Let us mention a positive result on existence of a P a_{P} -stratification.

###### Theorem 35.

[Hir1] If V ⊂ ℝ n V\subset\mathbb{R}^{n} is a semialgebraic variety and P: ℝ n → ℝ P:\mathbb{R}^{n}\to\mathbb{R} is a polynomial function, then there exists an a P a_{P} -stratification of ( V, 𝒱) (V,\mathcal{V}) with respect to P P.

## 5. Existence of a P a_{P} -stratification.

In this section we prove existence of a P a_{P} -stratification in the special case we are interested in. As the Example 3 shows, the existence of a a P a_{P} -stratification is a nontrivial question. In general, it does not exist. Unfortunately, the existence of a a P a_{P} -stratification in our case does not follow from the classical results, so we need to prove it.

Let ℝ N \mathbb{R}^{N} and ℝ k \mathbb{R}^{k} be Eucledian spaces with the fixed coordinate systems x = ( x 1, …, x N) ∈ ℝ N x=(x_{1},\dots,x_{N})\in\mathbb{R}^{N} and a = ( a 1, …, a k) ∈ ℝ k a=(a_{1},\dots,a_{k})\in\mathbb{R}^{k} with N ≥ k N\geq k and a non-trivial vector-polynomial P: ℝ N ∈ ℝ k P:\mathbb{R}^{N}\in\mathbb{R}^{k}. Recall that P P is a nontrivial if it has a point x ∈ ℝ N x\in\mathbb{R}^{N}, where rank d ​ P ​ ( x) = k dP(x)=k. In what follows we call vector-polynomial by polynomial for brevity.

###### Definition 36.

Let 𝐦 = ( 1, m 2, …, m k) ∈ ℤ + k {\bf m}=(1,m_{2},\dots,m_{k})\in\mathbb{Z}^{k}_{+} and δ > 0 \delta>0. We call the ( 𝐦, δ) (\bf m,\delta) -cone K 𝐦, δ K_{{\bf{m}},\delta} the following set of points

(54) |  | K 𝐦, δ = { a = ( a 1, …, a k) ∈ ℝ k: 0 < a 1 < δ, 0 < | a j + 1 | < | a 1 … a j | m j + 1 for j = 1, …, k − 1 }. \displaystyle\begin{aligned} K_{{\bf m},\delta}=\{a=(a_{1},\dots,a_{k})\in\mathbb{R}^{k}:\ 0<a_{1}<\delta,\\ 0<|a_{j+1}|<|a_{1}\dots a_{j}|^{m_{j+1}}\ \text{for}\ j=1,\dots,k-1\}.\end{aligned} |  |

Let 𝐦 ′ = ( 1, m 2 ′, …, m k ′) ∈ ℤ + k \mathbf{m}^{\prime}=(1,m^{\prime}_{2},\dots,m^{\prime}_{k})\in\mathbb{Z}^{k}_{+}. Define 𝐦 ′ ≻ 𝐦 \mathbf{m}^{\prime}\succ\mathbf{m} if 𝐦 ′ ≠ 𝐦 \mathbf{m}^{\prime}\neq\mathbf{m} and m i ′ ≥ m i m^{\prime}_{i}\geq m_{i} for all 2 ≤ i ≤ k 2\leq i\leq k. We call the ( 𝐦 ′, δ ′) (\bf m^{\prime},\delta^{\prime}) -cone K 𝐦 ′, δ K_{{\bf{m^{\prime}}},\delta} a refinement of the ( 𝐦, δ) (\bf m,\delta) -cone K 𝐦, δ K_{{\bf{m}},\delta} if 𝐦 ′ ≻ 𝐦 \mathbf{m}^{\prime}\succ\mathbf{m} and δ ≥ δ ′ \delta\geq\delta^{\prime}.

Define the following sets

(55) |  | V 𝐦, δ, P = closure { P − 1 ( K 𝐦, δ) }, V 0, 𝐦, 𝐏 = ∩ δ > 0 V 𝐦, δ, 𝐏 \displaystyle V_{{\bf m},\delta,P}=\textup{closure}\{P^{-1}(K_{\bf m,\delta})\},\ V_{0,\bf m,P}=\cap_{\delta>0}V_{\bf m,\delta,P} |  |

Then one has

###### Theorem 37.

For any nontrivial polynomial P P there exist an integer vector 𝐦 ∈ ℤ + n {\bf{m}}\in\mathbb{Z}_{+}^{n} and positive δ \delta such that the following conditions hold

a) the set V 0 = V 0, 𝐦, P V_{0}=V_{0,{\bf{m}},P} (see ( 55)) is semialgebraic.

b) the set V 𝐦, δ, P V_{{\bf{m}},\delta,P} consists of regular points of P P, i.e. if b ∈ V 𝐦, δ, P b\in V_{{\bf{m}},\delta,P}, then the level set P − 1 ​ ( b) P^{-1}(b) is a manifold of codimension n n.

c) there exists a stratification of V 0 V_{0} by semialgebraic strata ( V 0, 𝒱 0) (V_{0},\mathcal{V}_{0}) satisfying the property: V 𝐦, δ, P V_{{\bf{m}},\delta,P} is a P a_{P} -regular over any strata V α ∈ 𝒱 0 V_{\alpha}\in\mathcal{V}_{0} with respect to P P.

In order to prove Theorem 37 we reformulate it in a convenient for us language. Let a ∈ ℝ k a\in\mathbb{R}^{k}. Denote by L a = P − 1 ​ ( a) L_{a}=P^{-1}(a) the level set of P P. Recall that a ∈ ℝ k a\in\mathbb{R}^{k} is called a regular value if for any x ∈ L a x\in L_{a} the rank of linearity of P P is maximal, i.e. rank d ​ P ​ ( x) = k. dP(x)=k.

###### Definition 38.

Let a, b ∈ ℝ k a,b\in\mathbb{R}^{k} be values of P: ℝ N ∈ ℝ k, B N ⊂ ℝ N P:\ \mathbb{R}^{N}\in\mathbb{R}^{k},\ B^{N}\subset\mathbb{R}^{N} be the unit ball centered at the origin, and

(56) |  | d 0 0: B N × ℝ k ∈ ℝ, d 0 0 ​ ( x, a) = inf y ∈ L a ∩ B N ‖ x − y ‖ 2 d 0: ℝ k × ℝ k ∈ ℝ, d 0 ​ ( a, b) = sup x ∈ L b ∩ B N d 0 0 ​ ( x, a). \displaystyle\begin{aligned} d_{0}^{0}:B^{N}\times\mathbb{R}^{k}\in\mathbb{R},&\ d_{0}^{0}(x,a)=\inf_{y\in L_{a}\cap B^{N}}\|x-y\|^{2}\\ d_{0}:\mathbb{R}^{k}\times\mathbb{R}^{k}\in\mathbb{R},&\ d_{0}(a,b)=\sup_{x\in L_{b}\cap B^{N}}d_{0}^{0}(x,a).\end{aligned} |  |

Then the C 0 C^{0} -distance between level sets L a ∩ B N L_{a}\cap B^{N} and L b ∩ B N L_{b}\cap B^{N}

 | D P 0 ​ ( a, b) = d ​ i ​ s ​ t C 0 ​ ( L a ∩ B N, L b ∩ B N) = 1 2 ​ ( d 0 ​ ( a, b) + d 0 ​ ( b, a)). D_{P}^{0}(a,b)=dist_{C}^{0}(L_{a}\cap B^{N},L_{b}\cap B^{N})=\frac{1}{2}\left(d_{0}(a,b)+d_{0}(b,a)\right). |  |

For any 1 ≤ m ≤ N 1\leq m\leq N denote by G m, N G^{m,N} the set of m m -dimensional planes in the N N -dimensional Euclidean space. G m, N G^{m,N} is so-called the grassmanian manifold. Below we introduce convenient for as distance in the grassmanian manifold G m, N G^{m,N}. Now we define C 1 C^{1} -distance between regular level sets L a L_{a} and L b L_{b} in an appropriate for us way. Write P P using coordinate functions P = ( P 1, …, P k): ℝ N → ℝ k P=(P_{1},\dots,P_{k}):\mathbb{R}^{N}\to\mathbb{R}^{k}. If x ∈ ℝ N x\in\mathbb{R}^{N} is a regular point of P P, then gradients ∇ P 1 ​ ( x), …, ∇ P k ​ ( x) \nabla P_{1}(x),\dots,\nabla P_{k}(x) are linearly independent and span the space which is the orthogonal complement to the tangent space to the level set P − 1 ​ ( P ​ ( x)) P^{-1}(P(x)). Define a Gramm-Schmidt orthogonalization operator:

###### Definition 39.

Let v 1, …, v k ∈ ℝ k v_{1},\dots,v_{k}\in\mathbb{R}^{k} be linear independent vectors. Define the Gramm-Schmidt linear operator by

(57) |  | ∗: ( v 1, …, v k) = ( v 1 ∗, …, v k ∗), where v 1 ∗ = v 1, v 2 ∗ = v 2 − ( v 2, v 1) ( v 1, v 1) v 1, …, v k ∗ = v k − ∑ j < k ( v k, v j) ( v j, v j) v j. \displaystyle\begin{aligned} *:(v_{1},\dots,v_{k})=(v_{1}^{*},\dots,v_{k}^{*}),\ \ {\textup{where}}\\ v_{1}^{*}=v_{1},\ v_{2}^{*}=v_{2}-\frac{(v_{2},v_{1})}{(v_{1},v_{1})}v_{1},\dots,v_{k}^{*}=v_{k}-\sum_{j<k}\frac{(v_{k},v_{j})}{(v_{j},v_{j})}v_{j}.\end{aligned} |  |

Remarks 0. The Gramm-Schmidt linear operator ∗ *has nothing in common with the asterisk operator used for the Khovanski reduction procedure in section 3.

1. Vectors { v 1, …, v k } \{v_{1},\dots,v_{k}\} and { v 1 ∗, …, v k ∗ } \{v_{1}^{*},\dots,v_{k}^{*}\} span the same k k -dimensional space denoted by L L;

2. Vectors { v 1 ∗, …, v k ∗ } \{v_{1}^{*},\dots,v_{k}^{*}\} form an orthonormal basis in the plane L L;

3. Let { L t } t ∈ ( 0, 1] \{L_{t}\}_{t\in(0,1]} be a family of k k -dimensional planes in ℝ N \mathbb{R}^{N} spanned by a family of vectors { v 1 ​ ( t), …, v k ​ ( t) } t ∈ ( 0, 1] \{v_{1}(t),\dots,v_{k}(t)\}_{t\in(0,1]} depending continuously on t t. Consider { v 1 ∗ ( t), …, v k ∗ ( t) } t ∈ ( 0, 1] = ∗ ( v 1 ( t), …, v k ( t)) \{v^{*}_{1}(t),\dots,v^{*}_{k}(t)\}_{t\in(0,1]}=*(v_{1}(t),\dots,v_{k}(t)) as the family of orthonormal basis in { L t } t ∈ ( 0, 1] \{L_{t}\}_{t\in(0,1]}. Then sufficient condition that L t → L L_{t}\to L in the grassmanian manifold G k, N G^{k,N} is existence of an orthonormal basis { v 1 ∗, …, v k ∗ } \{v_{1}^{*},\dots,v_{k}^{*}\} of L L such that

(58) |  | ( v j ∗ ​ ( t), v j ∗) 2 ( v j ∗ ​ ( t), v j ∗ ​ ( t)) ​ ( v j ∗, v j ∗) → 0 as ​ t → 0. \displaystyle\frac{\left(v^{*}_{j}(t),v^{*}_{j}\right)^{2}}{(v^{*}_{j}(t),v^{*}_{j}(t))(v^{*}_{j},v^{*}_{j})}\to 0\ \ \textup{as}\ t\to 0. |  |

Define the Gramm-Schmidt operator for the polynomial map P P

(59) |  | ( ∗ ( d P) 1 ( x), …, ∗ ( d P) k ( x)) = ∗ ( ∇ P 1 ( x), …, ∇ P k ( x)). \displaystyle(*(dP)_{1}(x),\dots,*(dP)_{k}(x))=*(\nabla P_{1}(x),\dots,\nabla P_{k}(x)). |  |

Each vector ∗ ( d ​ P) j ​ ( x) *(dP)_{j}(x) is given by the rational function in x x.

Let Σ ⊂ ℝ N \Sigma\subset\mathbb{R}^{N} be the set of critical points of P P. To measure C 1 C^{1} -distance between two regular level sets we introduce the following function: Let x, y ∉ Σ x,y\notin\Sigma. Then

(60) |  | R P ​ ( x, y) = ∑ j = 1 k ( 1 − ( ∗ ( d P) j ( x), ∗ ( d P) j ( y)) 2 ( ∗ ( d P) j ( x), ∗ ( d P) j ( x)) ( ∗ ( d P) j ( y), ∗ ( d P) j ( y))) Q P ​ ( x, y) = ‖ x − y ‖ 2 + R P ​ ( x, y). \displaystyle\begin{aligned} R_{P}(x,y)=\sum_{j=1}^{k}\left(1-\frac{\left(*(dP)_{j}(x),*(dP)_{j}(y)\right)^{2}}{(*(dP)_{j}(x),*(dP)_{j}(x))(*(dP)_{j}(y),*(dP)_{j}(y))}\right)\\ Q_{P}(x,y)=\|x-y\|^{2}+R_{P}(x,y).\quad\quad\quad\end{aligned} |  |

###### Definition 40.

Let a, b ∈ ℝ k a,b\in\mathbb{R}^{k} be regular values of P: ℝ N → ℝ k P:\mathbb{R}^{N}\to\mathbb{R}^{k}, and L a = P − 1 ​ ( a) L_{a}=P^{-1}(a) and L b = P − 1 ​ ( b) L_{b}=P^{-1}(b) be regular level sets.

 | d 1, P 0: B N × ℝ k ∖ Σ → ℝ, d 1, P 0 ​ ( x, a) = inf y ∈ L a ∩ B N Q P ​ ( x, y), d 1, P: ( ℝ k ∖ Σ) × ( ℝ k ∖ Σ) → ℝ, d 1, P ​ ( a, b) = sup x ∈ L b ∩ B N d 1, P 0 ​ ( x, a). \displaystyle\begin{aligned} d_{1,P}^{0}:B^{N}\times\mathbb{R}^{k}\setminus\Sigma\to\mathbb{R},\quad&d^{0}_{1,P}(x,a)=\inf_{y\in L_{a}\cap B^{N}}Q_{P}(x,y),\\ d_{1,P}:\left(\mathbb{R}^{k}\setminus\Sigma\right)\times\left(\mathbb{R}^{k}\setminus\Sigma\right)\to\mathbb{R},&\quad d_{1,P}(a,b)=\sup_{x\in L_{b}\cap B^{N}}d^{0}_{1,P}(x,a).\end{aligned} |  |

Then the C 1 C^{1} -pseudodistance between regular level sets L a ∩ B N L_{a}\cap B^{N} and L b ∩ B N L_{b}\cap B^{N} is defined by

(61) |  | D P 1 ​ ( a, b) = d ​ i ​ s ​ t C 1 ​ ( L a ∩ B N, L b ∩ B N) = 1 2 ​ ( d 1, P ​ ( a, b) + d 1, P ​ ( b, a)). \displaystyle D^{1}_{P}(a,b)=dist_{C^{1}}\left(L_{a}\cap B^{N},L_{b}\cap B^{N}\right)=\frac{1}{2}\left(d_{1,P}(a,b)+d_{1,P}(b,a)\right). |  |

###### Remark 3.

We call the function D P 1 ​ ( a, b) D^{1}_{P}(a,b) C 1 C^{1} -pseudodistance, not C 1 C^{1} -distance, because it does not satisfy the triangle inequality. However, it satisfies the following triangle-like inequality

(62) |  | 2 ​ ( D P 1 ​ ( a, b) + D P 1 ​ ( b, c)) > D P 1 ​ ( a, b). \displaystyle 2(D^{1}_{P}(a,b)+D^{1}_{P}(b,c))>D^{1}_{P}(a,b). |  |

The reason we define C 1 C^{1} -pseudodistance D P 1 ​ ( a, b) D^{1}_{P}(a,b) in such a way is because the function D P 1 ​ ( a, b) D^{1}_{P}(a,b) is algebraic (see Lemma 3 below).

The inequality ( 62) can be proven as follows. Let v, w ∈ ℝ N v,w\in\mathbb{R}^{N} be vectors. Denote by ∠ ⁡ ( v, w) \angle(v,w) the angle between v v and w w. Direct calculation shows that

 | R P ( x, y) = ∑ j = 1 k sin 2 ( ∠ ( ∗ ( d P) j ( x), ∗ ( d P) j ( y))). R_{P}(x,y)=\sum_{j=1}^{k}\sin^{2}(\angle(*(dP)_{j}(x),*(dP)_{j}(y))). |  |

It is easy to check that 2 ​ ( sin 2 ⁡ α + sin 2 ⁡ β) ≥ sin 2 ⁡ ( α + β) 2(\sin^{2}\alpha+\sin^{2}\beta)\geq\sin^{2}(\alpha+\beta) which is sufficient for the proof of the inequality ( 62) .

Now we can reformulate Theorem 37 in the following way

###### Theorem 41.

For any nontrivial polynomial P P there exist an integer vector 𝐦 = ( 1, m 2, …, m k) ∈ ℤ + n {\bf{m}}=(1,m_{2},\dots,m_{k})\in\mathbb{Z}_{+}^{n} and positive δ \delta such that the following conditions hold

a) for any two values with the same first coordinate a = ( t, a 2, …, a k) a=(t,a_{2},\dots,a_{k}) and b = ( t, b 2, …, b k) b=(t,b_{2},\dots,b_{k}) in K 𝐦, δ K_{\mathbf{m},\delta}

 | D P 0 ​ ( a, b) < t; D_{P}^{0}(a,b)<t; |  |

b) the same as in Theorem 37;

c) for any two values with the same first coordinate a = ( t, a 2, …, a k) a=(t,a_{2},\dots,a_{k}) and b = ( t, b 2, …, b k) b=(t,b_{2},\dots,b_{k}) in K 𝐦, δ K_{\mathbf{m},\delta}

 | D P 1 ​ ( a, b) < t; D_{P}^{1}(a,b)<t; |  |

Let us show that parts a) and c) imply parts a) and c) of Theorem 37 respectively.

Proof a) ⟹ \Longrightarrow from a) of Theorem 37. Consider an algebraic curve of the form γ ⁡ ( t) = ( t, t m 2 + 1, t ( m 2 + 2) ​ ( m 3 + 1), …, t ( m 2 + 2) ​ … ​ ( m k + 1)) \gamma(t)=(t,t^{m_{2}+1},t^{(m_{2}+2)(m_{3}+1)},\dots,t^{(m_{2}+2)\dots(m_{k}+1)}). One can check that γ ⁡ ( t) ∈ K 𝐦, δ \gamma(t)\in\ K_{\mathbf{m},\delta} for any t ∈ ( 0, δ) t\in(0,\delta). Denote by V t, P = P − 1 ​ ( γ ⁡ ( t)) V_{t,P}=P^{-1}(\gamma(t)). The set ∪ 0 < t ≤ δ V t, P \cup_{0<t\leq\delta}V_{t,P} is clearly semialgebraic set. By the Tarski-Seidenberg theorem the following set

 | closure { ∪ 0 < t ≤ δ V t, P } ∖ { ∪ 0 < t ≤ δ V t, P } \textup{closure}\{\cup_{0<t\leq\delta}V_{t,P}\}\setminus\{\cup_{0<t\leq\delta}V_{t,P}\} |  |

is semialgebraic. Since for any smooth curve γ ′ ​ ( t) = ( t, γ 2 ​ ( t), …, γ k ​ ( t)) ∈ K 𝐦, δ, t ∈ ( 0, δ) \gamma^{\prime}(t)=(t,\gamma_{2}{(t)},\dots,\gamma_{k}{(t)})\in K_{\mathbf{m},\delta},\ t\in(0,\delta) Hausdorff distance between the level sets V t, P = P − 1 ​ ( γ ⁡ ( t)) V_{t,P}=P^{-1}(\gamma(t)) and V t, P ′ = P − 1 ​ ( γ ′ ​ ( t)) V^{\prime}_{t,P}=P^{-1}(\gamma^{\prime}(t)) is at most t t, i.e. D P 0 ​ ( γ ⁡ ( t), γ ′ ​ ( t)) < t D_{P}^{0}(\gamma(t),\gamma^{\prime}(t))<t. It implies that Hausdorff distance between any two level sets of the form V t, P V_{t,P} and V t, P ′ V^{\prime}_{t,P} tends to 0 0 as t → 0 t\to 0. Therefore,

 | closure { ∪ 0 < t ≤ δ V t, P } ∖ { ∪ 0 < t ≤ δ V t, P } = closure { P − 1 ( K 𝐦, δ) } ∖ { P − 1 ( K 𝐦, δ) }. \textup{closure}\{\cup_{0<t\leq\delta}V_{t,P}\}\setminus\{\cup_{0<t\leq\delta}V_{t,P}\}=\textup{closure}\{P^{-1}(K_{\mathbf{m},\delta})\}\setminus\{P^{-1}(K_{\mathbf{m},\delta})\}. |  |

This completes the proof of part a).

Proof c) ⟹ \Longrightarrow from c) of Theorem 37. Let us use notations of the proof of part a). By theorem 35 there is a stratification of V 0, 𝐦, P V_{0,\mathbf{m},P} such that the semialgebraic set { ∪ 0 < t ≤ δ V t, P } \{\cup_{0<t\leq\delta}V_{t,P}\} is a a P a_{P} -regular over V 0, 𝐦, P V_{0,\mathbf{m},P}. Indeed, let π 1: ℝ k → ℝ \pi_{1}:\mathbb{R}^{k}\to\mathbb{R} be the natural projection onto the first coordinate. Then a polynomial function p = π 1 ∘ P: ℝ N → ℝ p=\pi_{1}\circ P:\mathbb{R}^{N}\to\mathbb{R} is well-defined and p − 1 ​ ( t) = P − 1 ​ ( γ ⁡ ( t)) p^{-1}(t)=P^{-1}(\gamma(t)). Application of theorem 35 to the map

 | p: closure { ∪ 0 < t ≤ δ V t, P } → ℝ p:\textup{closure}\{\cup_{0<t\leq\delta}V_{t,P}\}\to\mathbb{R} |  |

gives existence of a required stratification.

Since C 1 C^{1} -distance between any two level sets of the form V t, P = P − 1 ​ ( γ ⁡ ( t)) V_{t,P}=P^{-1}(\gamma(t)) and V t, P ′ = P − 1 ​ ( γ ′ ​ ( t)) V^{\prime}_{t,P}=P^{-1}(\gamma^{\prime}(t)) is at most t t, i.e. D P 1 ​ ( γ ⁡ ( t), γ ′ ​ ( t)) < t D^{1}_{P}(\gamma(t),\gamma^{\prime}(t))<t. It implies that C 1 C^{1} -distance between any two level sets of the form V t, P V_{t,P} and V t, P ′ V^{\prime}_{t,P} tends to 0 0 as t → 0 t\to 0. Therefore, a P a_{P} -regularity of P − 1 ​ ( K 𝐦, δ) P^{-1}(K_{\mathbf{m},\delta}) over V 0, 𝐦, P V_{0,\mathbf{m},P} follows from a P a_{P} -regularity of { ∪ 0 < t ≤ δ V t, P } \{\cup_{0<t\leq\delta}V_{t,P}\} over V 0, 𝐦, P V_{0,\mathbf{m},P}. This completes the proof of part c).

Before proving Theorem 41 let us formulate a basic fact from elimination theory [Mu].

### 5.1. Elimination theory

Let ℂ m \mathbb{C}^{m} denote the m m -dimensional complex space z = ( z 1, …, z m) ∈ ℂ m, m ∈ ℤ + z=(z_{1},\dots,z_{m})\in\mathbb{C}^{m},\ \ m\in\mathbb{Z}_{+}. A set V V in ℂ m \mathbb{C}^{m} is called a closed algebraic set in ℂ m \mathbb{C}^{m} if there is a finite set of polynomials F 1, … ​ F s F_{1},\dots F_{s} in z 1, …, z m z_{1},\dots,z_{m} such that

 | V ( F 1, …, F s) = { ( z 1, …, z m) ∈ ℂ m | F j ( z 1, …, z m) = 0, 1 ≤ j ≤ s }. \displaystyle V(F_{1},\dots,F_{s})=\{(z_{1},\dots,z_{m})\in\mathbb{C}^{m}|\ F_{j}(z_{1},\dots,z_{m})=0,\ 1\leq j\leq s\}. |  |

One can define a topology in ℂ m \mathbb{C}^{m}, called the Zariski topology, whose closed sets are closed algebraic sets in ℂ m \mathbb{C}^{m}. This, indeed, defines a topology, because the set of closed algebraic sets is closed under a finite union and an arbitrary intersection. Sometimes, closed algebraic sets are also called Zariski closed sets.

###### Definition 42.

A subset S S of ℂ m \mathbb{C}^{m} is called constructible if it is in the Boolean algebra generated by the closed algebraic sets; or equivalently if S S is a disjoint union T 1 ∪ ⋯ ∪ T k T_{1}\cup\dots\cup T_{k}, where T i T_{i} is locally closed, i.e. T i = T i ′ − T i ′′ T_{i}=T^{\prime}_{i}-T^{\prime\prime}_{i}, T i ′ T^{\prime}_{i} — a closed algebraic set and T i ′′ ⊂ T i ′ T^{\prime\prime}_{i}\subset T^{\prime}_{i} — a smaller closed algebraic.

One of the main results of Elimination theory is the following

###### Theorem 43.

( [Mu], ch.2.2) Let V ⊂ ℂ μ × ℂ N V\subset\mathbb{C}^{\mu}\times\mathbb{C}^{N} be a constructible set and π: ℂ μ × ℂ N → ℂ μ \pi:\mathbb{C}^{\mu}\times\mathbb{C}^{N}\to\mathbb{C}^{\mu} be the natural projection. Then π ⁡ ( V) ⊂ ℂ μ \pi(V)\subset\mathbb{C}^{\mu} is a constructible set.

## 6. Proof of Theorem 41

### 6.1. Existence of the ( 𝐦, δ) (\bf m,\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} of regular values of P P (or Proof of Part a) of Theorem 41).

The set of critical values Σ P ⊂ ℝ k \Sigma_{P}\subset\mathbb{R}^{k} of a nontrivial polynomial map P: ℝ N → ℝ k P:\mathbb{R}^{N}\to\mathbb{R}^{k} is an algebraic set of positive codimension. It follows from Sard’s lemma for algebraic sets [Mu]. Suppose d: ℝ k → ℝ d:\mathbb{R}^{k}\to\mathbb{R} is a nonzero polynomial whose zero level set d − 1 ​ ( 0) ⊇ Σ d^{-1}(0)\supseteq\Sigma. Fix coordinate systems in ℝ N \mathbb{R}^{N}. By writing the linearization matrix d ​ P: ℝ N → ℝ k dP:\mathbb{R}^{N}\to\mathbb{R}^{k} and considering ( N − k + 1) (N-k+1) different k × k k\times k minors one can calculate d d explicitly.

###### Lemma 2.

For a nonzero polynomial d: ℝ k → ℝ d:\mathbb{R}^{k}\to\mathbb{R} there exists an integer vector 𝐦 = ( 1, m 2, …, m k) ∈ ℤ + k \mathbf{m}=(1,m_{2},\dots,m_{k})\in\mathbb{Z}^{k}_{+} and δ > 0 \delta>0 such that d d does not vanish on the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta}.

###### Remark 4.

If Σ P ⊆ d − 1 ​ ( 0) \Sigma_{P}\subseteq d^{-1}(0) and Σ P ∩ K 𝐦, δ ≠ ∅ \Sigma_{P}\cap K_{\mathbf{m},\delta}\neq\emptyset, then there exists x ∈ K 𝐦, δ x\in K_{\mathbf{m},\delta} such that d ⁡ ( x) = 0 d(x)=0. This shows that part a) of Theorem 41 follows from this Lemma.

Proof Let us prove the statement by induction in dimension k k.

For k = 1 k=1 the level set d − 1 ​ ( 0) ⊂ ℝ d^{-1}(0)\subset\mathbb{R} is a finite collection of points and Lemma is obvious.

Without loss of generality assume d ⁡ ( x 1, …, x k) d(x_{1},\dots,x_{k}) is not divisible by x k x_{k}. If d d is divisible by x k x_{k}, then for some β ∈ ℤ + \beta\in\mathbb{Z}_{+} one can decompose d ⁡ ( x 1, …, x k) = x k β ​ d ^ ​ ( x 1, …, x k) d(x_{1},\dots,x_{k})=x_{k}^{\beta}\hat{d}(x_{1},\dots,x_{k}) so that d ^ ​ ( x 1, …, x k − 1, 0) \hat{d}(x_{1},\dots,x_{k-1},0) is not identically zero. If for some 𝐦 ∈ ℤ + k \mathbf{m}\in\mathbb{Z}^{k}_{+} and δ > 0 \delta>0 the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} does not intersect zero locus d ^ − 1 ​ ( 0) \hat{d}^{-1}(0), then K 𝐦, δ K_{\mathbf{m},\delta} does not intersect zero locus d − 1 ( 0) = d ^ − 1 ( 0) ∪ { x k = 0 } d^{-1}(0)=\hat{d}^{-1}(0)\cup\{x_{k}=0\} too.

With the assumption of indivisibility by x k x_{k} the following set Σ P k − 1 = d − 1 ( 0) ∩ { x k = 0 } ⊂ ℝ k − 1 \Sigma^{k-1}_{P}=d^{-1}(0)\cap\{x_{k}=0\}\subset\mathbb{R}^{k-1} is of a positive codimension. By inductive hypothesis there exist an integer vector 𝐦 k − 1 ∈ ℤ + k − 1 \mathbf{m}_{k-1}\in\mathbb{Z}^{k-1}_{+} and δ k − 1 > 0 \delta_{k-1}>0 such that the ( 𝐦 k − 1, δ k − 1) (\mathbf{m}_{k-1},\delta_{k-1}) -cone K 𝐦 k − 1, δ k − 1 k − 1 ⊂ ℝ k − 1 K^{k-1}_{\mathbf{m}_{k-1},\delta_{k-1}}\subset\mathbb{R}^{k-1} has empty intersection with Σ P k − 1 \Sigma^{k-1}_{P}.

Let α = ( α 1, …, α k) ∈ ℤ + k \alpha=(\alpha_{1},\dots,\alpha_{k})\in\mathbb{Z}^{k}_{+} and | α | = ∑ j α j |\alpha|=\sum_{j}\alpha_{j}. Write d ⁡ ( x) = ∑ α ∈ ℤ + k a α ​ x α d(x)=\sum_{\alpha\in\mathbb{Z}^{k}_{+}}a_{\alpha}x^{\alpha} Denote by deg d = max { | α |: α ∈ ℤ + k, a α ≠ 0 } \deg d=\max\{|\alpha|:\alpha\in\mathbb{Z}^{k}_{+},\ a_{\alpha}\neq 0\}. Put m k = deg ⁡ d + 1 m_{k}=\deg d+1.

###### Proposition 4.

With the above notations there exists δ > 0 \delta>0 such that for 𝐦 = ( 𝐦 k − 1, m k) ∈ ℤ + k \mathbf{m}=(\mathbf{m}_{k-1},m_{k})\in\mathbb{Z}_{+}^{k} the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} does not intersect zero locus d − 1 ​ ( 0) d^{-1}(0).

Proof Put d ⁡ ( 0) = 0 d(0)=0 otherwise the proposition is trivial. Write

 | d ⁡ ( x 1, …, x k) = ∑ j = 0 deg ⁡ d a j ​ ( x 1, …, x k − 1) ​ x k j. d(x_{1},\dots,x_{k})=\sum_{j=0}^{\deg d}a_{j}(x_{1},\dots,x_{k-1})x_{k}^{j}. |  |

Without loss of genericity one can assume that a 0 ​ ( x 1, …, x k − 1) a_{0}(x_{1},\dots,x_{k-1}) does not vanish on the ( 𝐦 k − 1, δ k − 1) (\mathbf{m}_{k-1},\delta_{k-1}) -cone K 𝐦 k − 1, δ k − 1 k − 1 K^{k-1}_{\mathbf{m}_{k-1},\delta_{k-1}}. If not, then apply Lemma 2 and refine K 𝐦 k − 1, δ k − 1 k − 1 K^{k-1}_{\mathbf{m}_{k-1},\delta_{k-1}} to a required size. By the definition of the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} the condition ( x 1, …, x k) ∈ K 𝐦, δ (x_{1},\dots,x_{k})\in K_{\mathbf{m},\delta} implies that ( x 1, …, x k − 1) ∈ K 𝐦 k − 1, δ k − 1 k − 1 (x_{1},\dots,x_{k-1})\in K^{k-1}_{\mathbf{m}_{k-1},\delta_{k-1}} and 0 < x k < ( x 1 ​ … ​ x k − 1) m k 0<x_{k}<(x_{1}\dots x_{k-1})^{m_{k}}. Put x k = λ ​ ( x 1 ​ … ​ x k − 1) m k x_{k}=\lambda(x_{1}\dots x_{k-1})^{m_{k}} with λ ∈ ( 0, 1) \lambda\in(0,1). It is easy to check that

(63) |  | d ⁡ ( x 1, …, x k) = a 0 ​ ( x 1, …, x k − 1) ​ ( 1 + p ⁡ ( x 1, …, x k − 1, λ)), \displaystyle d(x_{1},\dots,x_{k})=a_{0}(x_{1},\dots,x_{k-1})(1+p(x_{1},\dots,x_{k-1},\lambda)), |  |

where p p is such a polynomial that p ⁡ ( 0, λ) ≡ 0 p(0,\lambda)\equiv 0. Indeed, the choice of m k m_{k} is such that ( x 1 ​ … ​ x k − 1) m k = a 0 ​ ( x 1, …, x k − 1) ​ q ​ ( x 1, …, x k − 1) (x_{1}\dots x_{k-1})^{m_{k}}=a_{0}(x_{1},\dots,x_{k-1})q(x_{1},\dots,x_{k-1}) for some polynomial q ⁡ ( x 1, …, x k − 1) q(x_{1},\dots,x_{k-1}). Since p ⁡ ( 0, λ) ≡ 0 p(0,\lambda)\equiv 0 for a sufficiently small δ \delta, any ( x 1, …, x k − 1) ∈ K 𝐦 k − 1, δ k − 1 k − 1 (x_{1},\dots,x_{k-1})\in K^{k-1}_{\mathbf{m}_{k-1},\delta_{k-1}}, and any λ ∈ [0, 1] \lambda\in[0,1] the following inequality holds | p ⁡ ( x 1, …, x k − 1, λ) | < 1 / 2 |p(x_{1},\dots,x_{k-1},\lambda)|<1/2. This shows that d d does not vanish on the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} and completes the proof of the Proposition.

As we pointed out above the Proposition implies Lemma 2.

### 6.2. Reduction to an optimization problem (or Proof of parts a) and c) of Theorem 37)

Let P = ( P 1, …, P k): ℝ N → ℝ k P=(P_{1},\dots,P_{k}):\mathbb{R}^{N}\to\mathbb{R}^{k} be a nontrivial polynomial with N ≥ k N\geq k given by its coordinate functions and an ( 𝐦, δ) − (\mathbf{m},\delta)- cone K ( 𝐦, δ) ⊂ Im ​ P ​ ( ℝ N) ⊂ ℝ k K_{(\mathbf{m},\delta)}\subset\textup{Im}\ P(\mathbb{R}^{N})\subset\mathbb{R}^{k} be a cone of regular values of P P. Existence of such a cone is proven in the previous section. Recall that Σ ⊂ ℝ N \Sigma\subset\mathbb{R}^{N} denotes the set of critical points of P P and Q P ​ ( x, y) Q_{P}(x,y) is defined in ( 60). The function Q P ​ ( x, y) Q_{P}(x,y) is a rational function symmetric with respect to permutation of x x and y y. It is defined to measure C 1 C^{1} -distance between level sets (see remarks after definition 39). The singular set of Q P Q_{P} belongs to ( Σ × ℝ N) ∪ ( ℝ N × Σ) (\Sigma\times\mathbb{R}^{N})\cup(\mathcal{\mathbb{R}}^{N}\times\Sigma). Recall that B N = { x: ∑ i = 1 N x i 2 ≤ 1 } ⊂ ℝ N B^{N}=\{x:\ \sum_{i=1}^{N}x_{i}^{2}\leq 1\}\subset\mathbb{R}^{N}. Introduce functions r ⁡ ( x) = 1 − ∑ i = 1 N x i 2. r(x)=1-\sum_{i=1}^{N}x_{i}^{2}.

Assume that the restriction of P to the boundary S N = ∂ B N = { x: ‖ x ‖ = 1 } S^{N}=\partial B^{N}=\{x:\ \|x\|=1\} has only the regular values in the ( 𝐦, δ) − (\mathbf{m},\delta)- cone K ( 𝐦, δ) K_{(\mathbf{m},\delta)}. Indeed, regularity of P | S N: S N → ℝ k P|_{S^{N}}:\ S^{N}\to\mathbb{R}^{k} is equivalent to regularity of the polynomial map ( P, r): ℝ N → ℝ k × ℝ (P,r):\ \mathbb{R}^{N}\to\mathbb{R}^{k}\times\mathbb{R} given by ( P, r) ​ ( x) = ( P ⁡ ( x), ∑ i = 1 N x i 2) (P,r)(x)=(P(x),\sum_{i=1}^{N}x_{i}^{2}). Existence of an ( 𝐦, δ) − (\mathbf{m},\delta)- cone of regular values of the map ( P, r) (P,r) follows from Lemma 2.

###### Lemma 3.

With the notations above let a τ 1, a τ 2 ∈ K ( 𝐦, δ) a_{\tau_{1}},\ a_{\tau_{2}}\in K_{(\mathbf{m},\delta)} be two points with the same first ( k − 1) (k-1) coordinates, i.e. a τ 1 = ( a k − 1, τ 1) a_{\tau_{1}}=(a^{k-1},\tau_{1}) and a τ 2 = ( a k − 1, τ 2) a_{\tau_{2}}=(a^{k-1},\tau_{2}). Then there exists a polynomial R ⁡ ( a k − 1, τ 1, τ 2, c) R(a^{k-1},\tau_{1},\tau_{2},c) in variables a k − 1 ∈ ℝ k − 1, τ 1 ∈ ℝ, τ 2 ∈ ℝ, a^{k-1}\in\mathbb{R}^{k-1},\ \tau_{1}\in\mathbb{R},\tau_{2}\in\mathbb{R}, and c ∈ ℝ c\in\mathbb{R} such that

(64) |  | R ⁡ ( a k − 1, τ 1, τ 2, d 1, P ​ ( a τ 1, a τ 2)) = 0. \displaystyle R(a^{k-1},\tau_{1},\tau_{2},d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}))=0. |  |

Moreover, R ⁡ ( a k − 1, τ, τ, 0) ≡ 0 R(a^{k-1},\tau,\tau,0)\equiv 0.

Proof Recall that { ∗ ( d P) j ( x) } j = 1 k \{*(dP)_{j}(x)\}_{j=1}^{k} form an orthogonal basis in the orthogonal complement to the tangent plane to the level set P − 1 ​ ( P ​ ( x)) P^{-1}(P(x)) at the point x x (see ( 59)). Let us make several remarks about the rational function R P ​ ( x, y) R_{P}(x,y) defined by ( 60).

1. If a τ = ( a k − 1, τ) ∈ K 𝐦, δ a_{\tau}=(a^{k-1},\tau)\in K_{\mathbf{m},\delta} is a regular value for the map ( P 1, …, P k): ℝ N → ℝ k (P_{1},\dots,P_{k}):\mathbb{R}^{N}\to\mathbb{R}^{k} for some τ \tau, then a k − 1 ∈ ℝ k − 1 a^{k-1}\in\mathbb{R}^{k-1} is a regular value for the map ( P 1, …, P k − 1): ℝ N → ℝ k − 1 (P_{1},\dots,P_{k-1}):\mathbb{R}^{N}\to\mathbb{R}^{k-1};

2. If a k − 1 ∈ ℝ k − 1 a^{k-1}\in\mathbb{R}^{k-1} is a regular value for the map ( P 1, …, P k − 1): B N → ℝ k − 1 (P_{1},\dots,P_{k-1}):B^{N}\to\mathbb{R}^{k-1}, then there is a positive ϵ ⁡ ( a k − 1) > 0 \epsilon(a^{k-1})>0 such that for each point x ∈ ( P 1, …, P k − 1) − 1 ​ ( a k − 1) x\in(P_{1},\dots,P_{k-1})^{-1}(a^{k-1}) and each 1 ≤ j ≤ k − 1 1\leq j\leq k-1

(65) |  | ( ∗ ( d P) j ( x), ∗ ( d P) j ( x)) > ϵ ( a k − 1) > 0. \displaystyle(*(dP)_{j}(x),*(dP)_{j}(x))>\epsilon(a^{k-1})>0. |  |

This follows from compactness of B N B^{N} and regularity of the value a k − 1 a^{k-1};

3. Since we consider only those τ \tau that a τ a_{\tau} belongs to the ( 𝐦, δ) ({\mathbf{m},\delta}) -cone K 𝐦, δ K_{\mathbf{m},\delta} of regular values of P P there exists a positive constant ϵ ⁡ ( a k − 1, τ) > 0 \epsilon(a^{k-1},\tau)>0 such that for each x ∈ P − 1 ​ ( a τ) x\in P^{-1}(a_{\tau})

(66) |  | ( ∗ ( d P) k ( x), ∗ ( d P) k ( x)) > ϵ ( a k − 1, τ). \displaystyle(*(dP)_{k}(x),*(dP)_{k}(x))>\epsilon(a^{k-1},\tau). |  |

This shows that Q ⁡ ( x, y) Q(x,y) restricted to P − 1 ​ ( K 𝐦, δ) × P − 1 ​ ( K 𝐦, δ) P^{-1}(K_{\mathbf{m},\delta})\times P^{-1}(K_{\mathbf{m},\delta}) is a smooth function of x x and y y.

Consider irreducible representation of the rational function Q ⁡ ( x, y) Q(x,y) as a ration of two polynomials Q ⁡ ( x, y) = T ⁡ ( x, y) S ⁡ ( x, y) Q(x,y)=\frac{T(x,y)}{S(x,y)}. Because of remarks 2 and 3 S ⁡ ( x, y) ≠ 0 S(x,y)\neq 0 for each pair ( x, y) ∈ P − 1 ​ ( K 𝐦, δ) × P − 1 ​ ( K 𝐦, δ) (x,y)\in P^{-1}(K_{\mathbf{m},\delta})\times P^{-1}(K_{\mathbf{m},\delta}).

Now notice that we deal with smooth objects: smooth level sets P − 1 ​ ( a τ) P^{-1}(a_{\tau}) and the smooth function Q P ​ ( x, y) Q_{P}(x,y). Notice that d 1, P 0 ​ ( x, a τ 2) d^{0}_{1,P}(x,a_{\tau_{2}}) is an extremal value of the function Q P ​ ( x, y) Q_{P}(x,y) provided that P ⁡ ( y) = a τ 2 P(y)=a_{\tau_{2}}. Similarly, d 1, P ​ ( a τ 1, a τ 2) d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}) is an extremal value of the function d 1, P 0 ​ ( x, a τ 2) d^{0}_{1,P}(x,a_{\tau_{2}}) provided that P ⁡ ( y) = a τ 1 P(y)=a_{\tau_{1}}. To find all extremal values of a smooth function on a smooth manifold one can use the Lagrange multipliers method. We prove that functions d 1, P d_{1,P} and d 1, P 0 d^{0}_{1,P} are algebraic functions.

The key point of the Lagrange multipliers method is that at an extremal point of Q P ​ ( x, y) Q_{P}(x,y) under the condition P ⁡ ( y) = a τ 2 P(y)=a_{\tau_{2}} the gradient ∇ y Q P ​ ( x, y) \nabla_{y}Q_{P}(x,y) can be expressed as a linear combination of gradients ∇ P 1 ​ ( y), …, ∇ P k ​ ( y) \nabla P_{1}(y),\dots,\nabla P_{k}(y), and ∇ r ​ ( y). \nabla r(y). The gradient of Q P ​ ( x, y) Q_{P}(x,y) has the form

 | ∇ y Q P ​ ( x, y) = ∇ y ( T P ​ ( x, y) S P ​ ( x, y)) = ( S P ​ ( x, y) ​ ∇ y T P ​ ( x, y) − T P ​ ( x, y) ​ ∇ y S P ​ ( x, y)) ​ S P − 2 ​ ( x, y). \nabla_{y}Q_{P}(x,y)=\nabla_{y}\left(\frac{T_{P}(x,y)}{S_{P}(x,y)}\right)=\left(S_{P}(x,y)\nabla_{y}T_{P}(x,y)-T_{P}(x,y)\nabla_{y}S_{P}(x,y)\right)S_{P}^{-2}(x,y). |  |

Since S | P − 1 ​ ( K 𝐦, δ) × P − 1 ​ ( K 𝐦, δ) ≠ 0 S|_{P^{-1}(K_{\mathbf{m},\delta})\times P^{-1}(K_{\mathbf{m},\delta})}\neq 0 we can rewrite the Lagrange system in the following form

(67) |  | { S P ​ ( x, y) ​ ∇ y T P ​ ( x, y) − T P ​ ( x, y) ​ ∇ y S P ​ ( x, y) + + S P 2 ( x) [∑ j = 1 k λ j ∇ P j ( x) − λ k + 1 ∇ r ( y)] = 0, P ⁡ ( y) − a τ 2 T P ​ ( x, y) − c ​ S P ​ ( x, y) = 0, λ k + 1 ​ r ​ ( y) = 0. \begin{cases}S_{P}(x,y)\nabla_{y}T_{P}(x,y)-T_{P}(x,y)\nabla_{y}S_{P}(x,y)+\\ +S_{P}^{2}(x)\left[\sum_{j=1}^{k}\lambda_{j}\nabla P_{j}(x)-\lambda_{k+1}\nabla r(y)\right]=0,\\ P(y)-a_{\tau_{2}}\\ T_{P}(x,y)-cS_{P}(x,y)=0,\\ \lambda_{k+1}r(y)=0.\end{cases} |  |

Important that all equations are polynomial and we can apply elimination theory! Notice that the last equation is responsible for an extremal point y y which might belong to the boundary ∂ B N \partial B^{N}. If a critical value belongs to the boundary, then r ⁡ ( y) = 0 r(y)=0 and λ k + 1 ∇ r ( y) \lambda_{k+1}\nabla r(y) is not zero and the gradient ∇ y Q P ​ ( x, y) \nabla_{y}Q_{P}(x,y) should be expressed as a linear combination of k + 1 k+1 vectors ∇ P 1 ​ ( y), …, ∇ P k ​ ( y) \nabla P_{1}(y),\dots,\nabla P_{k}(y), and ∇ r ​ ( y). \nabla r(y). If a critical value does not belong to the boundary, i.e. r ⁡ ( y) ≠ 0 r(y)\neq 0, then λ k + 1 = 0 \lambda_{k+1}=0 and λ k + 1 ∇ r ( y) = 0 \lambda_{k+1}\nabla r(y)=0.

Complexify the system ( 67), i.e. consider the system ( 67) for

 | ( x, y, λ, a k − 1, τ 2, c) ∈ ℂ N × ℂ N × ℂ k + 1 × ℂ k − 1 × ℂ × ℂ. (x,y,\lambda,a^{k-1},\tau_{2},c)\in\mathbb{C}^{N}\times\mathbb{C}^{N}\times\mathbb{C}^{k+1}\times\mathbb{C}^{k-1}\times\mathbb{C}\times\mathbb{C}. |  |

It defines a constructible set, denoted by V V, in ℂ 2 ​ N + 2 ​ k + 2 \mathbb{C}^{2N+2k+2}. Let us eliminate variables { λ j } j = 1 k + 1, { y i } i = 1 N \{\lambda_{j}\}_{j=1}^{k+1},\ \{y_{i}\}_{i=1}^{N} by projecting V V along the corresponding ( N + k + 1) (N+k+1) -dimensional ( λ, y) (\lambda,y) -plane. The result of projection is a constructible set W W in the space ( x, a k − 1, τ 2, c) ∈ ℂ N + k + 1 (x,a^{k-1},\tau_{2},c)\in\mathbb{C}^{N+k+1}. By the construction a point ( x, a k − 1, τ 2, c) (x,a^{k-1},\tau_{2},c) belongs to W W if some value of y y the following conditions hold: P ⁡ ( y) = a τ 2 P(y)=a_{\tau_{2}}, Q P ​ ( x, y) = c Q_{P}(x,y)=c, and y y is the critical point of Q P Q_{P} restricted to P − 1 ​ ( a τ 2) P^{-1}(a_{\tau_{2}}).

The constructible set W W has dimension N + k N+k. Indeed, consider a polynomial function ρ x: P − 1 ​ ( a τ 2) → ℝ \rho_{x}:P^{-1}(a_{\tau_{2}})\to\mathbb{R} defined by ρ x ​ ( y) = Q P ​ ( x, y) \rho_{x}(y)=Q_{P}(x,y). By Sard’s lemma for algebraic sets [Mu] critical values of ρ x \rho_{x} form an algebraic set of positive codimension in ℝ \mathbb{R}. Therefore, the set of critical values consists of a finite number of points and a finite number of possible c c so that ( x, a k − 1, τ 2, c) ∈ W (x,a^{k-1},\tau_{2},c)\in W. Thus, dim W \dim W equals dimension of ( x, a k − 1, τ 2,) (x,a^{k-1},\tau_{2},) -plane, i.e. dim W = N + k \dim W=N+k.

Since W W is constructible and has codimension 1 1 there is a non zero polynomial R ~ ​ ( x, a τ 2, c) \tilde{R}(x,a_{\tau_{2}},c) such that W ⊆ R ~ − 1 ​ ( 0) W\subseteq\tilde{R}^{-1}(0). By the definition ( 61) of d 1, P 0 ​ ( x, a τ 2) d^{0}_{1,P}(x,a_{\tau_{2}}) and by the construction

(68) |  | R ~ ​ ( x, a τ 1, a τ 2, d 1, P 0 ​ ( x, a τ 2)) ≡ 0. \displaystyle\tilde{R}(x,a_{\tau_{1}},a_{\tau_{2}},d^{0}_{1,P}(x,a_{\tau_{2}}))\equiv 0. |  |

In order to prove that the function d 1, P ​ ( a τ 1, a τ 2) d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}) defined by ( 61) is also algebraic, calculate critical values of d 1, P 0 ​ ( x, a τ 2) d^{0}_{1,P}(x,a_{\tau_{2}}), provided P ⁡ ( x) = a τ 1 P(x)=a_{\tau_{1}}. By the implicit function theorem the gradient ∇ x d 1, P 0 ​ ( x, a τ 2) \nabla_{x}d^{0}_{1,P}(x,a_{\tau_{2}}) can be expressed in terms of partial derivatives of R ~ ​ ( x, a τ 2, c) \tilde{R}(x,a_{\tau_{2}},c) by the following way

(69) |  | ∂ x j d 1, P 0 ​ ( x, a) = ∂ c R ~ ​ ( x, a, c) ​ ( ∂ x j R ~ ​ ( x, a, c)) − 1, \displaystyle\partial_{x_{j}}d^{0}_{1,P}(x,a)=\partial_{c}\tilde{R}(x,a,c)\left(\partial_{x_{j}}\tilde{R}(x,a,c)\right)^{-1}, |  |

for ( a, c) = ( a τ 2, d 1, P 0 ​ ( x, a τ 2)) (a,c)=(a_{\tau_{2}},d^{0}_{1,P}(x,a_{\tau_{2}})) and provided that ∂ x j R ~ ​ ( x, a τ 2, d 1, P 0 ​ ( x, a τ 2)) ≠ 0 \partial_{x_{j}}\tilde{R}(x,a_{\tau_{2}},d^{0}_{1,P}(x,a_{\tau_{2}}))\neq 0 for all 1 ≤ j ≤ N 1\leq j\leq N. Fix a = a τ 2 a=a_{\tau_{2}} and consider x x outside of the union of algebraic sets ℬ = ∪ j = 1 N { x: ∂ x j R ~ ( x, a, c) = 0 } \mathcal{B}=\cup_{j=1}^{N}\{x:\partial_{x_{j}}\tilde{R}(x,a,c)=0\}. Then d 1, P 0 ​ ( x, a) d^{0}_{1,P}(x,a) is a smooth function in x x. Application of the Lagrange multipliers method shows that at an extremal point of the function d 1, P 0 ​ ( x, a) d^{0}_{1,P}(x,a), provided P ⁡ ( x) = a τ 1 P(x)=a_{\tau_{1}}, the gradient ∇ x d 1, P 0 ​ ( x, a) \nabla_{x}d^{0}_{1,P}(x,a) can be represented as a linear combination ∇ x d 1, P 0 ( x, a) = ∑ j = 1 k λ j ∇ P j ( x) − λ k + 1 ∇ r ( x) \nabla_{x}d^{0}_{1,P}(x,a)=\sum_{j=1}^{k}\lambda_{j}\nabla P_{j}(x)-\lambda_{k+1}\nabla r(x). Plugging in the expression for ∇ x d 1, P 0 ​ ( x, a) \nabla_{x}d^{0}_{1,P}(x,a) in terms of ∂ c R ~ ​ ( x, a τ 2, c) \partial_{c}\tilde{R}(x,a_{\tau_{2}},c) and ∂ x j R ~ ​ ( x, a τ 2, c) \partial_{x_{j}}\tilde{R}(x,a_{\tau_{2}},c) for j = 1, …, N j=1,\dots,N we can present a Lagrange multiplier system in the following form

(70) |  | { ∂ x j R ~ ​ ( x, a τ 2, c) ​ ∂ c R ~ ​ ( x, a τ 2, c) = = [∑ j = 1 k λ j ∇ P j ( x) − λ k + 1 ∇ r 1 ( x)] ( ∂ x j R ~ ( x, a τ 2, c)) 2 R ~ ​ ( x, a τ 2, c) = 0, P ⁡ ( x) = a τ 1, λ k + 1 ​ r ​ ( x) = 0. \displaystyle\begin{cases}\partial_{x_{j}}\tilde{R}(x,a_{\tau_{2}},c)\partial_{c}\tilde{R}(x,a_{\tau_{2}},c)=\\ =\left[\sum_{j=1}^{k}\lambda_{j}\nabla P_{j}(x)-\lambda_{k+1}\nabla r_{1}(x)\right]\left(\partial_{x_{j}}\tilde{R}(x,a_{\tau_{2}},c)\right)^{2}\\ \tilde{R}(x,a_{\tau_{2}},c)=0,\\ P(x)=a_{\tau_{1}},\\ \lambda_{k+1}r(x)=0.\end{cases} |  |

Again the system ( 70) consists of only polynomial equations and we can apply elimination theory. Consider this system for

 | ( x, λ, a k − 1, τ 1, τ 2, c) ∈ ℂ N × ℂ k + 1 × ℂ k − 1 × ℂ × ℂ × ℂ. (x,\lambda,a^{k-1},\tau_{1},\tau_{2},c)\in\mathbb{C}^{N}\times\mathbb{C}^{k+1}\times\mathbb{C}^{k-1}\times\mathbb{C}\times\mathbb{C}\times\mathbb{C}. |  |

It defines a constructible set, denoted by V 1 V_{1}, in ℂ N + 2 ​ k + 3 \mathbb{C}^{N+2k+3}. Let us eliminate variables { λ j } j = 1 k + 1, { x i } i = 1 N \{\lambda_{j}\}_{j=1}^{k+1},\ \{x_{i}\}_{i=1}^{N} by projecting V V along the corresponding ( N + k + 1) (N+k+1) -dimensional ( λ, x) (\lambda,x) -plane. The result of projection is a constructible set W 1 W_{1} in the space ( a k − 1, τ 1, τ 2, c) ∈ ℂ k + 2 (a^{k-1},\tau_{1},\tau_{2},c)\in\mathbb{C}^{k+2}.

Similarly to the arguments for the constructible set W W one can show that W 1 W_{1} has dimension k k. Since W 1 W_{1} is constructible and has codimension 1 1 there is a nonzero polynomial R ⁡ ( a k − 1, τ 1, τ 2, c) R(a^{k-1},\tau_{1},\tau_{2},c) such that W 1 ⊆ R − 1 ​ ( 0) W_{1}\subseteq R^{-1}(0). By the definition ( 61) of d 1, P ​ ( a τ 1, a τ 2) d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}) and by the construction

(71) |  | R ⁡ ( a τ 1, a τ 2, d 1, P ​ ( a τ 1, a τ 2)) ≡ 0. \displaystyle R(a_{\tau_{1}},a_{\tau_{2}},d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}))\equiv 0. |  |

By the construction if a τ 1 = a τ 2 a_{\tau_{1}}=a_{\tau_{2}}, then R ⁡ ( a τ 1, a τ 1, 0) ≡ 0 R(a_{\tau_{1}},a_{\tau_{1}},0)\equiv 0, because in this case both level sets are the same and C 1 C^{1} -distance between them must equal zero. This completes the proof of Lemma 3.

###### Lemma 4.

With the notations above there exists a refinement ( 𝐦 ′, δ ′) (\mathbf{m}^{\prime},\delta^{\prime}) -cone K 𝐦 ′, δ ′ ⊂ K 𝐦, δ K_{\mathbf{m}^{\prime},\delta^{\prime}}\subset K_{\mathbf{m},\delta} such that for any pair of points a τ 1 = ( a k − 1, τ 1) a_{\tau_{1}}=(a^{k-1},\tau_{1}) and a τ 2 = ( a k − 1, τ 2) a_{\tau_{2}}=(a^{k-1},\tau_{2}) from K 𝐦 ′, δ ′ K_{\mathbf{m}^{\prime},\delta^{\prime}}

(72) |  | D P 1 ​ ( a τ 1, a τ 2) ≤ ( a 1 ​ … ​ a 1 ​ k − 1) 2, \displaystyle D^{1}_{P}(a_{\tau_{1}},a_{\tau_{2}})\leq(a_{1}\dots a_{1}{k-1})^{2}, |  |

where a k − 1 = ( a 1, …, a k − 1) ∈ ℝ k − 1 a^{k-1}=(a_{1},\dots,a_{k-1})\in\mathbb{R}^{k-1}.

Proof It follows from Lemma 3 that there is a polynomial R ⁡ ( a τ 1, a τ 2, c) R(a_{\tau_{1}},a_{\tau_{2}},c) such that R ⁡ ( a τ 1, a τ 2, d 1, P ​ ( a τ 1, a τ 2)) ≡ 0 R(a_{\tau_{1}},a_{\tau_{2}},d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}))\equiv 0 and R ⁡ ( a, τ, τ, 0) ≡ 0 R(a,\tau,\tau,0)\equiv 0.

For a τ 1, a τ 2 a_{\tau_{1}},a_{\tau_{2}} belonging to the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} of regular values of P P the function d 1, P ​ ( a τ 1, a τ 2) d_{1,P}(a_{\tau_{1}},a_{\tau_{2}}) depends continuously on τ 1 \tau_{1} and τ 2 \tau_{2}. Let us rewrite R ⁡ ( a τ 1, a τ 2, c) R(a_{\tau_{1}},a_{\tau_{2}},c) in the form R ⁡ ( a k − 1, τ 1, τ 2, c) R(a^{k-1},\tau_{1},\tau_{2},c). Recall that in our notations a τ = ( a k − 1, τ) a_{\tau}=(a^{k-1},\tau).

Suppose for determiness that τ 1 > τ 2 \tau_{1}>\tau_{2}. Notice that each sufficiently small positive root c j ​ ( a k − 1, τ 1, τ 2) c_{j}(a^{k-1},\tau_{1},\tau_{2}) is increasing in τ 1 \tau_{1} and decreasing in τ 2 \tau_{2} in a neighborhood of ( a k − 1, τ 1, τ 2) = 0 (a^{k-1},\tau_{1},\tau_{2})=0. Therefore, c j ​ ( a k − 1, τ 1, 0) > c j ​ ( a k − 1, τ 1, τ 2) c_{j}(a^{k-1},\tau_{1},0)>c_{j}(a^{k-1},\tau_{1},\tau_{2})

Denote R ⁡ ( a k − 1, τ, c) = R ⁡ ( a k − 1, τ, 0, c) R(a^{k-1},\tau,c)=R(a^{k-1},\tau,0,c). Let us show that for some sufficiently large positive integers m ′ m^{\prime} and m ′′ m^{\prime\prime} if 0 < τ < ( a 1 k − 1 ​ … ​ a k − 1 k − 1 ​ c) m ′ 0<\tau<(a^{k-1}_{1}\dots a^{k-1}_{k-1}c)^{m^{\prime}} and 0 < c < ( a 1 k − 1 ​ … ​ a k − 1 k − 1) m ′′ 0<c<(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{m^{\prime\prime}} the following decomposition holds: Put c = ρ ​ ( a 1 k − 1 ​ … ​ a k − 1 k − 1) m ′′ c=\rho(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{m^{\prime\prime}} and τ = λ ​ ( a 1 k − 1 ​ … ​ a k − 1 k − 1 ​ c) m ′ \tau=\lambda(a^{k-1}_{1}\dots a^{k-1}_{k-1}c)^{m^{\prime}} with ρ, λ ∈ ( 0, 1) \rho,\lambda\in(0,1). Then

(73) |  | R ⁡ ( a k − 1, τ, c) = r 0 ​ ( a k − 1) ​ ( 1 + q 1 ​ ( a k − 1, ρ)) ​ ( 1 + q 2 ​ ( a k − 1, ρ, λ)), \displaystyle R(a^{k-1},\tau,c)=r_{0}(a^{k-1})(1+q_{1}(a^{k-1},\rho))(1+q_{2}(a^{k-1},\rho,\lambda)), |  |

where r 0, q 1, q 2 r_{0},\ q_{1},\ q_{2} are polynomials in their variables. Indeed, apply the same arguments as we used to prove ( 63) to the polynomial

 | R ⁡ ( a k − 1, τ, c) = ∑ j = 1 deg ⁡ R R j ​ ( a k − 1, c) ​ τ j + R 0 ​ ( a k − 1, c). R(a^{k-1},\tau,c)=\sum_{j=1}^{\deg R}R_{j}(a^{k-1},c)\tau^{j}+R_{0}(a^{k-1},c). |  |

Then apply the same arguments to

 | R 0 ​ ( a k − 1, c) = ∑ j = 1 deg ⁡ R 0 r j ​ ( a k − 1) ​ c j + r 0 ​ ( a k − 1, c). R_{0}(a^{k-1},c)=\sum_{j=1}^{\deg R_{0}}r_{j}(a^{k-1})c^{j}+r_{0}(a^{k-1},c). |  |

Notice that R ⁡ ( a k − 1, 0, 0) ≡ 0 R(a^{k-1},0,0)\equiv 0 implies that q 1 ​ ( 0, ρ) ≡ q 2 ​ ( 0, ρ, λ) ≡ 0 q_{1}(0,\rho)\equiv q_{2}(0,\rho,\lambda)\equiv 0. Therefore, for a sufficiently small δ ′ > 0 \delta^{\prime}>0 and any ( a k − 1, δ ′) ∈ K 𝐦, δ ′ (a^{k-1},\delta^{\prime})\in K_{\mathbf{m},\delta^{\prime}} polynomials q 1 ​ ( a k − 1, ρ) q_{1}(a^{k-1},\rho) and q 2 ​ ( a k − 1, ρ, λ) q_{2}(a^{k-1},\rho,\lambda) are sufficiently small and R ⁡ ( a k − 1, τ, c) R(a^{k-1},\tau,c) equals 0 0 if and only if r 0 ​ ( a k − 1) r_{0}(a^{k-1}) equals 0 0.

By Lemma cone there is a refinement ( 𝐦 ′, δ ′) (\mathbf{m}^{\prime},\delta^{\prime}) -cone K 𝐦 ′, δ ′ ⊂ K 𝐦, δ ′ K_{\mathbf{m}^{\prime},\delta^{\prime}}\subset K_{\mathbf{m},\delta^{\prime}} such that r 0 ​ ( a k − 1) r_{0}(a^{k-1}) does not vanish on K 𝐦 ′, δ ′ K_{\mathbf{m}^{\prime},\delta^{\prime}}.

Now put m k ′ = m ′ ​ m ′′ m_{k}^{\prime}=m^{\prime}m^{\prime\prime}. As we have just shown all sufficiently small positive roots c j ​ ( a k − 1, τ, 0) < τ 1 / m ′ ​ ( a 1 k − 1 ​ … ​ a k − 1 k − 1) c_{j}(a^{k-1},\tau,0)<\tau^{1/m^{\prime}}(a^{k-1}_{1}\dots a^{k-1}_{k-1}) provided that

 | τ 1 / m ′ ​ ( a 1 k − 1 ​ … ​ a k − 1 k − 1) < ( a 1 k − 1 ​ … ​ a k − 1 k − 1) m ′′. \tau^{1/m^{\prime}}(a^{k-1}_{1}\dots a^{k-1}_{k-1})<(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{m^{\prime\prime}}. |  |

This condition is satisfied for any 0 < τ < ( a 1 k − 1 ​ … ​ a k − 1 k − 1) m ′ ​ m ′′ 0<\tau<(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{m^{\prime}m^{\prime\prime}}. This shows that all sufficiently small positive roots

 | c j ​ ( a k − 1, τ, 0) < ( a 1 k − 1 ​ … ​ a k − 1 k − 1) m ′′ + 1 < ( a 1 k − 1 ​ … ​ a k − 1 k − 1) 2. c_{j}(a^{k-1},\tau,0)<(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{m^{\prime\prime}+1}<(a^{k-1}_{1}\dots a^{k-1}_{k-1})^{2}. |  |

This completes the proof of the Lemma.

Let us complete the proof of part c) Theorem 41 by the following inductive arguments.

Consider a sequence of positive integers m 2, …, m k m_{2},\dots,m_{k}. Let 𝐦 = ( 1, m 2, …, m k) \mathbf{m}=(1,m_{2},\dots,m_{k}) and δ > 0 \delta>0. Define a sequence of polynomials associated to this sequence, defined by their coordinate functions:

(74) |  | P j 0 = P j − ( P 1 … P j − 1) m j, j = 2, …, k P s = ( P 1 0, …, P s 0, P s + 1, …, P k − s), s = 2, …, k \displaystyle\begin{aligned} P_{j}^{0}=P_{j}-(P_{1}\dots P_{j-1})^{m_{j}},\ j=2,\dots,k\\ P^{s}=(P_{1}^{0},\dots,P_{s}^{0},P_{s+1},\dots,P_{k-s}),\ s=2,\dots,k\end{aligned} |  |

Define the restriction of the ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} to the s s -dimensional plane, denoted by K 𝐦, δ s K^{s}_{\mathbf{m},\delta}, generated by the first k k -coordinates by the following way:

(75) |  | K s 𝐦, δ = { a s = ( a 1, …, a s) ∈ ℝ s: 0 < a 1 < δ, 0 < | a j + 1 | < | a 1 … a j | m j + 1 for j = 1, …, s − 1 }. \displaystyle\begin{aligned} K^{s}_{\mathbf{m},\delta}=\{a^{s}=(a_{1},\dots,a_{s})\in\mathbb{R}^{s}:\ 0<a_{1}<\delta,\\ 0<|a_{j+1}|<|a_{1}\dots a_{j}|^{m_{j+1}}\ \text{for}\ j=1,\dots,s-1\}.\end{aligned} |  |

It is shown above that there is an ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} such that any point ( 0, a k − 1) ∈ ℝ × K 𝐦, δ k − 1 (0,a^{k-1})\in\mathbb{R}\times K^{k-1}_{\mathbf{m},\delta} is a regular point for the polynomial P k − 1 P^{k-1}. Therefore, one can apply Lemmas 2, 3, and 64 and show that there is refinement of K 𝐦, δ k − 1 K^{k-1}_{\mathbf{m},\delta}, denoted the same, such that for any two points a τ 1 k − 1 = ( 0, a k − 2, τ 1) a^{k-1}_{\tau_{1}}=(0,a^{k-2},\tau_{1}) and a τ 1 k − 1 ​ ( 0, a k − 2, τ 2) a^{k-1}_{\tau_{1}}(0,a_{k-2},\tau_{2}) from ℝ × K 𝐦, δ k − 1 \mathbb{R}\times K^{k-1}_{\mathbf{m},\delta}

(76) |  | D P 1 1 ​ ( a τ 1 k − 1, a τ 2 k − 1) ≤ ( a 1 ​ … ​ a k − 2) 2. \displaystyle D^{1}_{P^{1}}(a^{k-1}_{\tau_{1}},a^{k-1}_{\tau_{2}})\leq(a_{1}\dots a_{k-2})^{2}. |  |

By induction one can show that there is a refinement an ( 𝐦, δ) (\mathbf{m},\delta) -cone K 𝐦, δ K_{\mathbf{m},\delta} such that for any two points a τ 1 k − s = ( 0, a k − s − 1, τ 1) a^{k-s}_{\tau_{1}}=(0,a^{k-s-1},\tau_{1}) and a τ 1 k − s ​ ( 0, a k − s − 1, τ 2) a^{k-s}_{\tau_{1}}(0,a_{k-s-1},\tau_{2}) from the restriction cone K 𝐦, δ k − s K^{k-s}_{\mathbf{m},\delta} such that

(77) |  | D P s 1 ​ ( a τ 1 k − s, a τ 2 k − s) ≤ ( a 1 ​ … ​ a k − s − 1) 2. \displaystyle D^{1}_{P^{s}}(a^{k-s}_{\tau_{1}},a^{k-s}_{\tau_{2}})\leq(a_{1}\dots a_{k-s-1})^{2}. |  |

Notice that for any 1 ≤ s ≤ k 1\leq s\leq k level sets of the polynomial P s P^{s} correspond to level sets of the initial polynomial P P. Combining this with all estimates for D P s 1 ​ ( a τ 1 k − s, a τ 2 k − s) D^{1}_{P^{s}}(a^{k-s}_{\tau_{1}},a^{k-s}_{\tau_{2}}) and the triangle-like inequality ( 62) one can show that part c) of Theorem 41 holds true. Part a) of Theorem 41 follows from part c) because Q P ​ ( x, y) ≥ ‖ x − y ‖ 2 Q_{P}(x,y)\geq\|x-y\|^{2}, which implies that D P 1 ​ ( a, b) ≥ D P 0 ​ ( a, b) D^{1}_{P}(a,b)\geq D^{0}_{P}(a,b) for any pair a, b ∈ K 𝐦, δ a,b\in K_{\mathbf{m},\delta}.

This completes the proof of Theorem 41.

## References

- [AAI] D. Anosov, V. Arnold, Yu. Ilyashenko, Dynamical systems. I, Encyclopaedia Math. Sci., 1, Springer, Berlin, 1988;
- [AGV] V. Arnold, S. Gusein-Zade, A. Varchenko Singularities of differentiable maps. Vol. I.Monographs in Mathematics, 82, Birkhuser Boston, 1985.
- [BCR] J. Bochnak, M. Coste, M.-F. Roy, Real Algebraic Geometry, Springer-Verlag, Berlin, 1998.
- [D] F. Dumortier, Singularities of vector fields on the plane, J. Diff.Equations, 23, (1977), 53–106.
- [E] J. Ecalle, Introduction aux fonctions analysables et preuve consrustive de la conjecture de Dulac, Herman, Paris, (1992).
- [FP] J.-P. Francoise, C. Pugh, Keeping track of limit cycles. J. Diff. Eqns 65, (1986), no. 2, 139–157.
- [GWPL] C.G. Gibson, K. Wirthmuller, A.A. du Plessis, E.J.N.Loojenga, Topological Stability of Smooth Mappings, Lectures Notes in Mathematics 552, Springer 1976.
- [GG] M. Golubitsky, V. Guillemin, Stable Mappings and Their Singularities, Graduate Texts in Mathematics 14, Springer-Verlag 1973.
- [GM] M. Goresky, R. MacPherson, Stratified Morse Theory, Springer-Verlag 1987.
- [G] T. Grozovskii, Bifurcations of polycycles an “apple” and a “half-apple” in generic two-parameter families, Diff. Equations (in Russian), Vol.32, (1996), no. 4, pp. 458–469.
- [Hir1] H. Hironaka, Stratification and flatness Real and Complex singularities, Nordic Summer School (Oslo, 1976), Sijthoff-Noordhoff, Growhgen, (1977)
- [Hir2] H. Hironaka, Introduction to real-algebraic sets and real-analytic maps,Instituto Mathematico L.Tonelli, Dell’ Universita’di Piza, 1973
- [I] Yu. Ilyashenko, Finiteness theorem for limit cycles, Amer. Math. Soc., Providence, (1991).
- [IK] Yu. Ilyashenko, V. Kaloshin, Bifurcations of planar and spatial polycycles: Arnold’s program and its development, Fields Inst Comm Vol 24, (1999), pp. 241-271
- [IY1] Yu.Ilyashenko, S.Yakovenko, Finitely smooth normal forms of local families of diffeomorphisms and vector fields, Russian Math. Surveys 46 (1991), no. 1, 1–43
- [IY2] Yu.Ilyashenko, S.Yakovenko, Concerning Hilbert sixteenth problem, Amer. Math. Soc. Transl, Ser.2, 165, (1995), 1–20.
- [IY3] Yu.Ilyashenko, S.Yakovenko, Finite Cyclicity of Elementary Polycycles in Generic Families, Amer.Math.Soc.Transl, 165, (1995), 21–95.
- [J] N. Jacobson, Basic Algebra, vol.1, 1974
- [Ka1] V. Kaloshin, A Geometric Proof of Existence of Whitney’s stratifications, submitted to Ann. of Math.
- [Kh] A.Khovanskii, Fewnomials, Amer.Math.Soc. Providence,RI, 1991
- [KS] A. Kotova, V. Stanzo, Few-Parameter Generic Families on the Sphere, Amer. Math. Soc. Translations, Providence, RI, Ser. 2, 213,1996 pp. 155–202
- [Ma] J. Mather, Notes on topological stability, Harvard University
- [Mi] J. Milnor, Singular points of complex hypersurfaces Princeton University Press, Princeton, NJ, 61 1968
- [Mu] D. Mumford, Algebraic Geometry I, Complex Projective Algebraic Varieties, Springer-Verlag, 1976
- [PW] A. du Plessis, T. Wall, The Geometry of Topological Stability, Oxford, 1995;
- [R] R. Roussarie, Cyclicite finie et le 16 problem d’Hilbert, Dynamical systems, (Volparaiso, (1986)), (R.Bauon, R.Lavarca, and J.Palis, eds.), LNM, 1331, Springer-Verlag, Berlin and New York, (1988), 161–188.
- [S] D. Shlomick(ed), Bifurcations and periodic orbits of vector fields, NATO AS1, Series C (Math. and Phys. Sciences), vol. 408, Kluwel, Dordrecht, Boston, London, (1993).
- [Ta] F. Takens, Unfoldings of certain singularities of vector fields: generalized Hopf bifurcations, J. Differential Equations 14 (1973), pp. 476–493.
- [Th] R. Thom, Ensembles et morphismes stratifiés. Bull. Amer. Math. Soc. 75 1969, pp. 240–284.
- [Ti] V. Tikhomirov, Fundamental principles of the theory of extremal problems. Transl. by Bernd Luderer. John Wiley & Sons, 1986.
- [Wa] T. Wall, Regular Stratifications, Lecture Notes in Mathematics, No. 468, pp. 332-344;
- [W] H. Whitney, Elementary structure of real algebraic varieties, Ann. of Math 66 1957 no.3 545–556


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:kaloshin@math.princeton.edu
