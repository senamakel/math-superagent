<!-- source: https://arxiv.org/html/2407.13465 | converted from HTML -->

A note on Hilbert 16th Problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2407.13465v2 [math.DS] 01 Oct 2024

# A note on Hilbert 16th Problem

Armengol Gasull 1 and Paulo Santana 2 Address: 1 Departament de Matemàtiques, Facultat de Ciències, Universitat Autònoma de Barcelona, 08193 Bellaterra, Barcelona, Spain ; and Centre de Recerca Matemàtica, Edifici Cc, Campus de Bellaterra, 08193 Cerdanyola del Vallès (Barcelona), Spain Email address: [armengol.gasull@uab.cat][3] Address: 2 IBILCE–UNESP, CEP 15054–000, S. J. Rio Preto, São Paulo, Brazil Email address: [paulo.santana@unesp.br][4]

###### Abstract.

Let ℋ ⁡ ( n) \mathcal{H}(n) be the maximum number of limit cycles that a planar polynomial vector field of degree n n can have. In this paper we prove that ℋ ⁡ ( n) \mathcal{H}(n) is realizable by structurally stable vector fields with only hyperbolic limit cycles and that it is a strictly increasing function whenever it is finite.

###### Key words and phrases:

Hilbert 16th problem; limit cycles; structurally stable vector fields

###### 2020 Mathematics Subject Classification

Primary: 34C07.

## 1. Introduction and statement of the main results

Consider the planar polynomial system of differential equations X = ( P, Q) X=(P,Q) given by

(1) |  | x ˙ = P ⁡ ( x, y), y ˙ = Q ⁡ ( x, y), \dot{x}=P(x,y),\quad\dot{y}=Q(x,y), |  |

where the dot means the derivative in relation to the independent variable t t and P P, Q: ℝ 2 → ℝ Q\colon\mathbb{R}^{2}\to\mathbb{R} are polynomials. To system ( 1) corresponds a polynomial vector field X = P ​ ∂ ∂ x + Q ​ ∂ ∂ y X=P\frac{\partial}{\partial x}+Q\frac{\partial}{\partial y} in the phase plane of the variables x x and y y. In this paper we make no distinction between system ( 1) and its respective vector field. The degree of X X is the maximum of the degrees of P P and Q Q. Given n ∈ ℕ n\in\mathbb{N}, let 𝒳 n \mathcal{X}^{n} be the set of the planar polynomial systems ( 1) of degree n n, endowed with the coefficients topology. Given X ∈ 𝒳 n X\in\mathcal{X}^{n}, let π ⁡ ( X) ∈ ℤ ⩾ 0 ∪ { ∞ } \pi(X)\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} be its number of *limit cycles*(i.e. isolated periodic orbits).

In his famous address to the International Congress of Mathematicians in Paris 1900, David Hilbert raised his famous list of problems for the 20 20 th century [2], with the second part of the 16 16 th problem being about the limit cycles of planar polynomial vector fields. Hilbert asks if there is a uniform upper bound for the number of limit cycles of polynomial vector fields of degree n n. More precisely, given n ∈ ℕ n\in\mathbb{N} let ℋ ⁡ ( n) ∈ ℤ ⩾ 0 ∪ { ∞ } \mathcal{H}(n)\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} be given by,

 | ℋ ⁡ ( n) = sup { π ⁡ ( X): X ∈ 𝒳 n }. \mathcal{H}(n)=\sup\{\pi(X)\colon X\in\mathcal{X}^{n}\}. |  |

Under this notation the second part of Hilbert’s 16 16 th problem consists in obtaining an upper bound for ℋ ⁡ ( n) \mathcal{H}(n) and it is yet an open problem. Even for the quadratic case, it is not known if ℋ ⁡ ( 2) < ∞ \mathcal{H}(2)<\infty. However, advances has been made and lower bounds for ℋ ⁡ ( n) \mathcal{H}(n) have been found. For small values of n n, the best lower bounds so far are ℋ ⁡ ( 2) ⩾ 4 \mathcal{H}(2)\geqslant 4 [3, 18], ℋ ⁡ ( 3) ⩾ 13 \mathcal{H}(3)\geqslant 13 [10] and ℋ ⁡ ( 4) ⩾ 28 \mathcal{H}(4)\geqslant 28 [15]. In general, it is known that ℋ ⁡ ( n) \mathcal{H}(n) increases at least as fast as O ⁡ ( n 2 ​ ln ⁡ n) O(n^{2}\ln n) [4, 8, 11]. However, although the known lower bounds are given by strictly increasing functions, this does not imply that ℋ ⁡ ( n) \mathcal{H}(n) itself is strictly increasing. In our first main result we prove this fact.

###### Theorem 1.

Given n ∈ ℕ n\in\mathbb{N}, it holds ℋ ⁡ ( n + 1) ⩾ ℋ ⁡ ( n) + 1 \mathcal{H}(n+1)\geqslant\mathcal{H}(n)+1.

In particular, it follows from Theorem 1 that if ℋ ⁡ ( n 0) = ∞ \mathcal{H}(n_{0})=\infty for some n 0 ∈ ℕ n_{0}\in\mathbb{N}, then ℋ ⁡ ( n) = ∞ \mathcal{H}(n)=\infty for every n ⩾ n 0 n\geqslant n_{0}.

The proof of Theorem 1 is essentially a consequence from the fact that given X ∈ 𝒳 n X\in\mathcal{X}^{n}, we can embed X X into 𝒳 n + 1 \mathcal{X}^{n+1} and bifurcate one more limit cycle, while the others persist. This persistence follows from our second main result. To state it properly we will remind the notion of *structural stability*and comment on its particularities when it is restricted to the polynomial case.

Roughly speaking, a smooth vector field is structurally stable if small perturbations do not change the topological character of its orbits. The hallmark work on this area is due to Peixoto [12] and his characterization theorem, which states that a C 1 C^{1} -vector field on a closed (i.e. compact and without boundary) two dimensional manifold is structurally stable if, and only if, the following statements hold.

1. (a)

It has at most a finite number of singularities, all hyperbolic.

2. (b)

It has at most a finite number of periodic orbits, all hyperbolic.

3. (c)

It does not have saddle connections.

Moreover, the family of structurally stable vector fields is open and dense in the set of all C 1 C^{1} -vector fields. For the structural stability of *polynomial*vector fields endowed with the coefficients topology there are two main characterizations, given by Sotomayor [19] and Shafer [16]. The former defines structural stability of X ∈ 𝒳 n X\in\mathcal{X}^{n} as the structural stability of its Poincaré compactification. The latter does not make use of this embedding and thus deals with new objects, such as saddles at infinity. Hence, they obtained different sets of necessary and sufficient conditions for structural stability. Yet, there are many similarities. Let X ∈ 𝒳 n X\in\mathcal{X}^{n}. In both cases for X X to be structurally stable, statements ( a) (a) and ( c) (c) above are necessary and also the following weak version of statement ( b) (b).

1. ( b ′) (b^{\prime})

It has at most a finite number of periodic orbits, none of even multiplicity.

So far it is not known if non-hyperbolic limit cycles of odd multiplicity are possible for a structurally stable vector field in the polynomial world. More precisely, there is the following open question.

###### Question 1 ( [19, 16]).

If X ∈ 𝒳 n X\in\mathcal{X}^{n} has a non-hyperbolic limit cycle of odd multiplicity, then is X X structurally unstable in 𝒳 n \mathcal{X}^{n}?

Question 1 was explicitly raised by Sotomayor [19, Problem 1.1 1.1] and Shafer [16, Question 3.4 3.4] and kept both of them from obtaining necessary *and*sufficient conditions for structural stability in 𝒳 n \mathcal{X}^{n}. For more details, we refer to [17]. Another important similarity between both works is the fact that structural stability is a generic property. That is, if we let Σ n ⊂ 𝒳 n \Sigma^{n}\subset\mathcal{X}^{n} be the family of the structurally stable elements, then Σ n \Sigma^{n} is open and dense, independently of the two approaches. Therefore, from now on we denote by Σ n \Sigma^{n} the set of structurally stable vector fields of degree n n under either one of these two definitions.

Let Σ h n ⊂ Σ n \Sigma^{n}_{h}\subset\Sigma^{n} be the family of structurally stable vector fields such that all their limit cycles are hyperbolic. In our second main result we prove that ℋ ⁡ ( n) \mathcal{H}(n) is realizable by the elements of this family.

###### Theorem 2.

For n ∈ ℕ n\in\mathbb{N}, the following statements hold.

1. (a)

If ℋ ⁡ ( n) < ∞ \mathcal{H}(n)<\infty, then there is X ∈ Σ h n X\in\Sigma_{h}^{n} such that π ⁡ ( X) = ℋ ⁡ ( n) \pi(X)=\mathcal{H}(n).

2. (b)

If ℋ ⁡ ( n) = ∞ \mathcal{H}(n)=\infty, then for each k ∈ ℕ k\in\mathbb{N} there is X k ∈ Σ h n X_{k}\in\Sigma_{h}^{n} such that π ⁡ ( X k) ⩾ k \pi(X_{k})\geqslant k.

Finally, due to its relation with the possible case of ℋ ⁡ ( n) = ∞ \mathcal{H}(n)=\infty, we also include at the end of this note a proof for the following folklore result: *a planar analytic vector field has an enumerable number of limit cycles.*

The paper is organized as follows. In Section 2 we recall some properties of *rotated vector fields*and prove how they can be used to transform non-hyperbolic limit cycles in hyperbolic ones. The main theorems are proved in Section 3. In Section 4 we prove the folklore result and provide some further remarks.

## 2. Rotated vector fields

Given a planar polynomial vector field X = ( P, Q) X=(P,Q), let X α = ( P α, Q α) X_{\alpha}=(P_{\alpha},Q_{\alpha}) be the one-parameter family given by

(2) |  | P α = P ​ cos ⁡ α − Q ​ sin ⁡ α, Q α = Q ​ cos ⁡ α + P ​ sin ⁡ α, P_{\alpha}=P\cos\alpha-Q\sin\alpha,\quad Q_{\alpha}=Q\cos\alpha+P\sin\alpha, |  |

with α ∈ ℝ \alpha\in\mathbb{R}. Observe that X 0 = X X_{0}=X and that X α X_{\alpha} defines a *completed family of rotated vector fields*, see Duff [5]. Throughout out this paper, X α X_{\alpha} will always denote the family given by ( 2).

In his seminal work Duff [5] studied the properties of X α. X_{\alpha}. In particular, he proved the following result that we simply state for family ( 2), but that holds for more general 1 1 -parametric families of 𝒞 1 \mathcal{C}^{1} vector fields.

###### Theorem 3 ( [5]).

Let X α X_{\alpha} be the family of rotated vector fields ( 2) and suppose that X α 0 X_{\alpha_{0}} has a limit cycle γ α 0 \gamma_{\alpha_{0}}. Then:

1. (a)

If γ α 0 \gamma_{\alpha_{0}} has odd multiplicity, then it is persistent for | α − α 0 | |\alpha-\alpha_{0}| small and it either contracts or expands monotonically as α \alpha varies in a certain sense.

2. (b)

If γ α 0 \gamma_{\alpha_{0}} has even multiplicity, then for | α − α 0 | |\alpha-\alpha_{0}| small it splits in two limit cycles, one stable and the other unstable, as α \alpha varies in a certain sense. If α \alpha varies in the opposite sense, then γ α 0 \gamma_{\alpha_{0}} disappears and no other limit cycles appear in its neighborhood.

We observe that Theorem 3 does not provide information about the hyperbolicity of the limit cycles involved. However, it follows from Andronov et al [1, Theorems 71 71 & 72 72] that this information can be given in the analytic case. For sake of simplicity and for the paper to be self-contained, we provide a proof of a simple version of such theorems, sufficient for our goals.

###### Proposition 1.

Let X α X_{\alpha} be the family of rotated vector fields ( 2) and suppose that X α 0 X_{\alpha_{0}} has a limit cycle γ α 0 \gamma_{\alpha_{0}}. Then, for | α − α 0 | > 0 |\alpha-\alpha_{0}|>0 small enough, all the limit cycles detailed in Theorem 3 that bifurcate from γ α 0 \gamma_{\alpha_{0}} are hyperbolic.

###### Proof.

For simplicity, let us assume α 0 = 0 \alpha_{0}=0. If γ 0 \gamma_{0} is hyperbolic, then there is nothing to prove. Hence, suppose that γ 0 \gamma_{0} is not hyperbolic. Let I ⊂ ℝ I\subset\mathbb{R} be a small neighborhood of α 0 = 0 \alpha_{0}=0 and Σ \Sigma be a small normal section of γ 0 \gamma_{0}, endowed with a coordinate system s ∈ ℝ s\in\mathbb{R} such that s = 0 s=0 at p p, where { p } = γ 0 ∩ Σ \{p\}=\gamma_{0}\cap\Sigma. Let D: I × Σ → ℝ D\colon I\times\Sigma\to\mathbb{R} be its associated displacement map. Since X α X_{\alpha} is analytic in ( x, y, α) (x,y;\alpha), it follows that D D is well defined and analytic. Let T > 0 T>0 be the period of γ 0 \gamma_{0} and let γ 0 ​ ( t) \gamma_{0}(t) be the parametrization of γ 0 \gamma_{0} given by the flow of X 0 X_{0} and such that γ 0 ​ ( 0) = p \gamma_{0}(0)=p. It follows from Perko [13, Lemma 2 2] that, for some C ∈ ℝ \ { 0 }, C\in\mathbb{R}\backslash\{0\},

(3) |  | ∂ D ∂ α ​ ( 0, 0) \displaystyle\frac{\partial D}{\partial\alpha}(0,0) | = C ∫ 0 T ( e − ∫ 0 t d i v ( γ 0 ( τ)) d τ) X α ∧ ∂ X α ∂ α ( γ 0 ( t); 0) d t \displaystyle=C\int_{0}^{T}\left(e^{-\int_{0}^{t}div(\gamma_{0}(\tau))\;d\tau}\right)X_{\alpha}\land\dfrac{\partial X_{\alpha}}{\partial\alpha}(\gamma_{0}(t);0)\;dt |  |

 |  | = C ∫ 0 T ( e − ∫ 0 t d i v ( γ 0 ( τ)) d τ) ( P 2 + Q 2) ( γ 0 ( t); 0) d t ≠ 0. \displaystyle=C\int_{0}^{T}\left(e^{-\int_{0}^{t}div(\gamma_{0}(\tau))\;d\tau}\right)\big(P^{2}+Q^{2})(\gamma_{0}(t);0)\;dt\neq 0. |  |

Therefore, from the Implicit Function Theorem we have that there is a unique function α = α ⁡ ( s) \alpha=\alpha(s), with α ⁡ ( 0) = 0 \alpha(0)=0, such that

(4) |  | D ⁡ ( α ⁡ ( s), s) = 0. D(\alpha(s),s)=0. |  |

Moreover, since D D is analytic, it follows that α ⁡ ( s) \alpha(s) is also analytic. Differentiating ( 4) in relation to s s we obtain,

(5) |  | ∂ D ∂ α ​ ( α ⁡ ( s), s) ​ α ′ ​ ( s) + ∂ D ∂ s ​ ( α ⁡ ( s), s) = 0. \frac{\partial D}{\partial\alpha}(\alpha(s),s)\alpha^{\prime}(s)+\frac{\partial D}{\partial s}(\alpha(s),s)=0. |  |

From ( 3) we have that ∂ D ∂ α ​ ( α ​ ( s), s) ≠ 0 \frac{\partial D}{\partial\alpha}(\alpha(s),s)\neq 0 for | s | |s| small. Hence, it follows from ( 5) that,

(6) |  | α ′ ​ ( s) = − ∂ D / ∂ s ∂ D / ∂ α ​ ( α ⁡ ( s), s). \alpha^{\prime}(s)=-\frac{\partial D/\partial s}{\partial D/\partial\alpha}(\alpha(s),s). |  |

Since γ 0 \gamma_{0} is not hyperbolic, it follows that ∂ D ∂ s ​ ( 0, 0) = 0 \frac{\partial D}{\partial s}(0,0)=0 and thus from ( 6) we have α ′ ​ ( 0) = 0 \alpha^{\prime}(0)=0. Since α ′ \alpha^{\prime} is an analytic function, either 0 0 is an isolated zero of α ′ \alpha^{\prime} or α ′ ​ ( s) ≡ 0 \alpha^{\prime}(s)\equiv 0 (and in particular α ⁡ ( s) ≡ 0 \alpha(s)\equiv 0) in a neighborhood of s = 0 s=0. Let us discard this second possibility. In this case, from ( 4), D ⁡ ( 0, s) ≡ 0 D(0,s)\equiv 0 for | s | |s| small and thus γ 0 \gamma_{0} belongs to a continuous band of periodic orbits, contradicting the definition of limit cycle. Therefore, it follows from ( 5) that

 | ∂ D ∂ s ​ ( α ⁡ ( s), s) = − ∂ D ∂ α ​ ( α ⁡ ( s), s) ​ α ′ ​ ( s) ≠ 0, \frac{\partial D}{\partial s}(\alpha(s),s)=-\frac{\partial D}{\partial\alpha}(\alpha(s),s)\alpha^{\prime}(s)\neq 0, |  |

for | s | > 0 |s|>0 small. Hence, any limit cycle of X α X_{\alpha} near γ 0 \gamma_{0} is hyperbolic, for | α | > 0 |\alpha|>0 small, as we wanted to prove. ∎

We observe that Perko [13, Theorem 3 3] also provided a similar result about the hyperbolicity of the limit cycles considered at Theorem 3 ( b) (b). For more details about the theory of rotated vector fields and its generalizations, we refer to Han [7], Perko [14, Section 4.6 4.6] and the references therein.

## 3. Proof of the main theorems

Given X = ( P, Q) ∈ 𝒳 n X=(P,Q)\in\mathcal{X}^{n}, let π h ​ ( X) \pi_{h}(X) be its number of hyperbolic limit cycles. Observe that in general we have π h ​ ( X) ⩽ π ⁡ ( X) \pi_{h}(X)\leqslant\pi(X).

In this paper we also work with the possibility of π ⁡ ( X) = ∞ \pi(X)=\infty for some X ∈ 𝒳 n X\in\mathcal{X}^{n}. We choose to do this because although Il’yashenko [9] and Écalle [6] independently claimed to have proved that this is impossible, it seems that some of their results start to be under discussion. For instance, in the recent work [20] a possible gap was found in Il’yashenko’s proof. Our results are not based on these finiteness results.

###### Proposition 2.

Let X ∈ 𝒳 n X\in\mathcal{X}^{n}. Then the following statements hold.

1. (a)

If π ⁡ ( X) < ∞ \pi(X)<\infty, then there is Y ∈ 𝒳 n Y\in\mathcal{X}^{n} such that π h ​ ( Y) ⩾ π ⁡ ( X) \pi_{h}(Y)\geqslant\pi(X).

2. (b)

If π ⁡ ( X) = ∞ \pi(X)=\infty, then for each k ∈ ℕ k\in\mathbb{N} there is Y k ∈ 𝒳 n Y_{k}\in\mathcal{X}^{n} such that π h ​ ( Y k) ⩾ k \pi_{h}(Y_{k})\geqslant k.

###### Proof.

Let X ∈ 𝒳 n X\in\mathcal{X}^{n} and X α X_{\alpha} be its respective family of rotated vector fields, given by ( 2). Let also:

1. (i)

h ∈ ℤ ⩾ 0 ∪ ∞ h\in\mathbb{Z}_{\geqslant 0}\cup{\infty} be the number of hyperbolic limit cycles of X X;

2. (ii)

m ∈ ℤ ⩾ 0 ∪ ∞ m\in\mathbb{Z}_{\geqslant 0}\cup{\infty} be the number of non-hyperbolic limit cycles X X of odd multiplicity;

3. (iii)

m ± ∈ ℤ ⩾ 0 ∪ ∞ m^{\pm}\in\mathbb{Z}_{\geqslant 0}\cup{\infty} be the number of non-hyperbolic limit cycles γ \gamma of X X of even multiplicity and such that γ \gamma bifurcates in two hyperbolic limit cycles for ± α > 0 \pm\alpha>0 small.

Observe that π ⁡ ( X) = h + m + m + + m − \pi(X)=h+m+m^{+}+m^{-}. Suppose first π ⁡ ( X) < ∞ \pi(X)<\infty. Without loss of generality, suppose m + ⩾ m − m^{+}\geqslant m^{-}. It follows from Proposition 1 that X α X_{\alpha} has at least h + m + 2 ​ m + h+m+2m^{+} hyperbolic limit cycles for α > 0 \alpha>0 small enough. Hence, if we take Y = X α Y=X_{\alpha}, then Y ∈ 𝒳 n Y\in\mathcal{X}^{n} and

 | π h ​ ( Y) ⩾ h + n + 2 ​ m + ⩾ h + n + m + + m − = π ⁡ ( X). \pi_{h}(Y)\geqslant h+n+2m^{+}\geqslant h+n+m^{+}+m^{-}=\pi(X). |  |

If π ⁡ ( X) = ∞ \pi(X)=\infty, then h h, m m, m + m^{+} or m − m^{-} are equal to infinity. In any case we apply the same reasoning on an sequence of vector fields having an increasing number of limit cycles, obtaining the final desired sequence of vector fields. ∎

###### Proof of Theorem 2.

Suppose first ℋ ⁡ ( n) < ∞ \mathcal{H}(n)<\infty and let Z ∈ 𝒳 n Z\in\mathcal{X}^{n} be such that π ⁡ ( Z) = ℋ ⁡ ( n) \pi(Z)=\mathcal{H}(n). It follows from Proposition 2 that there is Y ∈ 𝒳 n Y\in\mathcal{X}^{n} such that π h ​ ( Y) ⩾ π ⁡ ( Z) \pi_{h}(Y)\geqslant\pi(Z). Hence, it follows from the definition of ℋ ⁡ ( n) \mathcal{H}(n) that,

 | π ⁡ ( Y) = π h ​ ( Y) = π ⁡ ( Z) = ℋ ⁡ ( n). \pi(Y)=\pi_{h}(Y)=\pi(Z)=\mathcal{H}(n). |  |

Hence, every limit cycle of Y Y is hyperbolic and any vector field in 𝒳 n, \mathcal{X}^{n}, close enough to Y, Y, has also exactly ℋ ⁡ ( n) \mathcal{H}(n) limit cycles, all of them hyperbolic. In particular, there is an arbitrarily small perturbation X ∈ Σ h n X\in\Sigma^{n}_{h} of Y Y such that π ⁡ ( X) = ℋ ⁡ ( n) \pi(X)=\mathcal{H}(n).

Suppose now ℋ ⁡ ( n) = ∞ \mathcal{H}(n)=\infty. Observe that there is a sequence ( Z j) (Z_{j}), with Z j ∈ 𝒳 n Z_{j}\in\mathcal{X}^{n}, such that π ⁡ ( Z j) → ∞ \pi(Z_{j})\to\infty and π ⁡ ( Z j) < ∞ \pi(Z_{j})<\infty for every j ∈ ℕ j\in\mathbb{N}, or there is Z ∈ 𝒳 n Z\in\mathcal{X}^{n} such that π ⁡ ( Z) = ∞ \pi(Z)=\infty. In either case it follows from statement ( a) (a) or ( b) (b) of Proposition 2, respectively, that for each k ∈ ℕ k\in\mathbb{N} there is Y k ∈ 𝒳 n Y_{k}\in\mathcal{X}^{n} such that π h ​ ( Y k) ⩾ k \pi_{h}(Y_{k})\geqslant k. Therefore, for each k ∈ ℕ k\in\mathbb{N} we can take a small enough perturbation W k ∈ Σ n W_{k}\in\Sigma^{n} of Y k Y_{k} such that π h ​ ( W k) ⩾ k \pi_{h}(W_{k})\geqslant k. It follows from the definition of Σ n \Sigma^{n} that π ⁡ ( W k) < ∞ \pi(W_{k})<\infty. Moreover, some of these limit cycles may be non-hyperbolic and with odd multiplicity. Thus, it follows similarly to the proof of Proposition 2, from the structural stability of W k W_{k} and from the fact that Σ n \Sigma^{n} is open and dense in 𝒳 n \mathcal{X}^{n}, that we can take a small enough rotation X k ∈ Σ n X_{k}\in\Sigma^{n} of W k W_{k} such that the following statements hold.

1. (i)

The hyperbolic limit cycles persist.

2. (ii)

The non-hyperbolic limit cycles become hyperbolic.

3. (iii)

X k X_{k} and W k W_{k} are topologically equivalent.

In particular, it follows from ( i ​ i ​ i) (iii) that we do not have the bifurcation of new limit cycles and thus we conclude that X k ∈ Σ h n X_{k}\in\Sigma_{h}^{n} and π ⁡ ( X k) ⩾ k \pi(X_{k})\geqslant k. ∎

We now prove a technical lemma that we will need to proof Theorem 1.

###### Lemma 1.

Let X ∈ 𝒳 n X\in\mathcal{X}^{n} and B ⊂ ℝ 2 B\subset\mathbb{R}^{2} a closed ball centered at the origin. Then there is an arbitrarily small perturbation Y Y of X X having a regular point p ∈ ℝ 2 \ B p\in\mathbb{R}^{2}\backslash B such that ℓ ∩ B = ∅ \ell\cap B=\emptyset, where ℓ \ell is the straight line p + s ​ Y ​ ( p) p+sY(p), s ∈ ℝ s\in\mathbb{R}.

###### Proof.

It follows from Shafer [16, Theorem 3.2 3.2] that we can take an arbitrarily small perturbation Y ∈ 𝒳 n Y\in\mathcal{X}^{n} of X X such that Y Y has at most a finite number of singularities. Let Y = ( P, Q) Y=(P,Q) and let P i P_{i} and Q i Q_{i}, i ∈ { 0, …, n } i\in\{0,\dots,n\}, be homogeneous polynomials of degree i i such that P = P 0 + ⋯ + P n P=P_{0}+\dots+P_{n} and Q = Q 0 + ⋯ + Q n Q=Q_{0}+\dots+Q_{n}. Replacing Y Y by an arbitrarily small perturbation if necessary, we can also suppose P n ​ ( 1, 0) ​ Q n ​ ( 1, 0) ≠ 0 P_{n}(1,0)Q_{n}(1,0)\neq 0. Let p = ( x, 0) p=(x,0), x > 0 x>0. Since Y Y has at most a finite number of singularities, there is x 0 > 0 x_{0}>0 such that if x > x 0 x>x_{0}, then p p is a regular point of Y Y. Let ℓ + \ell^{+} and ℓ − \ell^{-} be the two straight lines tangents to B B and passing through p p. Let θ = θ ⁡ ( x) \theta=\theta(x) be the angle between ℓ ± \ell^{\pm} and the x x -axis and observe that,

 | lim x → ∞ θ ⁡ ( x) = 0. \lim\limits_{x\to\infty}\theta(x)=0. |  |

Let also φ = φ ⁡ ( x) \varphi=\varphi(x) be the angle between ℓ \ell and the x x -axis, which is given by

 | φ ⁡ ( x) = arctan ⁡ Q ⁡ ( x, 0) P ⁡ ( x, 0), \varphi(x)=\arctan\frac{Q(x,0)}{P(x,0)}, |  |

see Figure 1.

\begin{overpic}[Fig1.eps] \put(98.0,27.0){$x$} \put(20.0,51.0){$y$} \put(5.0,19.0){$B$} \put(45.0,33.0){$\ell^{+}$} \put(45.0,17.0){$\ell^{-}$} \put(73.0,23.0){$p$} \put(74.5,32.5){$Y(p)$} \put(52.0,27.0){$\theta$} \put(70.0,29.0){$\varphi$} \put(69.5,51.0){$\ell$} \end{overpic} Figure 1. Illustration of ℓ ± \ell^{\pm} and ℓ \ell.

Since P n ​ ( 1, 0) ​ Q n ​ ( 1, 0) ≠ 0 P_{n}(1,0)Q_{n}(1,0)\neq 0 it follows that,

 | lim x → ∞ φ ⁡ ( x) = arctan ⁡ Q n ​ ( 1, 0) P n ​ ( 1, 0) ≠ 0. \lim\limits_{x\to\infty}\varphi(x)=\arctan\frac{Q_{n}(1,0)}{P_{n}(1,0)}\neq 0. |  |

As a consequence, | φ ⁡ ( x) | > | θ ⁡ ( x) | |\varphi(x)|>|\theta(x)| for x > 0 x>0 big enough and thus ℓ ∩ B = ∅ \ell\cap B=\emptyset. ∎

###### Proof of Theorem 1.

Suppose first ℋ ⁡ ( n) < ∞ \mathcal{H}(n)<\infty. It follows from Theorem 2 ( a) (a) that there is Z ∈ Σ h n Z\in\Sigma_{h}^{n} such that π ⁡ ( Z) = ℋ ⁡ ( n) \pi(Z)=\mathcal{H}(n). Let B ⊂ ℝ 2 B\subset\mathbb{R}^{2} be a closed ball centered at the origin and such that all the limit cycles of Z Z are in the interior of B B. From Lemma 1 and the structural stability of Z Z, we can suppose that Z Z has a regular point p ∈ ℝ 2 \ B p\in\mathbb{R}^{2}\backslash B such that p + s ​ Z ​ ( p) ∉ B p+sZ(p)\not\in B for every s ∈ ℝ s\in\mathbb{R}. Let Y = ( P, Q) ∈ Σ h n Y=(P,Q)\in\Sigma_{h}^{n} be the vector field obtained from Z Z by translating p p to the origin. Let X = ( R, S) ∈ 𝒳 n + 1 X=(R,S)\in\mathcal{X}^{n+1} be given by

 | R ⁡ ( x, y) = ( a ​ x + b ​ y) ​ P ​ ( x, y), S ⁡ ( x, y) = ( a ​ x + b ​ y) ​ Q ​ ( x, y), R(x,y)=(ax+by)P(x,y),\quad S(x,y)=(ax+by)Q(x,y), |  |

with a = − Q ⁡ ( 0, 0) a=-Q(0,0) and b = P ⁡ ( 0, 0) b=P(0,0). Let ℓ ⊂ ℝ 2 \ell\subset\mathbb{R}^{2} be the line given by a ​ x + b ​ y = 0 ax+by=0 and observe that X X and Y Y are equal on each connected component of ℝ 2 \ ℓ \mathbb{R}^{2}\backslash\ell, except by the rescaling of time characterized by d ​ t / d ​ τ = a ​ x + b ​ y dt/d\tau=ax+by. It follows from Lemma 1 that B ∩ ℓ = ∅ B\cap\ell=\emptyset and thus π h ​ ( X) = π ⁡ ( X) = π ⁡ ( Y) \pi_{h}(X)=\pi(X)=\pi(Y). Observe that ℓ \ell is a line of singularities of X X. In particular, the origin is a singularity of X X and its Jacobian matrix is given by,

 | D ​ X ​ ( 0, 0) = ( a ​ P ​ ( 0, 0) b ​ P ​ ( 0, 0) a ​ Q ​ ( 0, 0) b ​ Q ​ ( 0, 0)) = ( a ​ b b 2 − a 2 − a ​ b). DX(0,0)=\left(\begin{array}[]{cc}aP(0,0)&bP(0,0)\\ aQ(0,0)&bQ(0,0)\end{array}\right)=\left(\begin{array}[]{cc}ab&b^{2}\\ -a^{2}&-ab\end{array}\right). |  |

Hence, det D ​ X ​ ( 0, 0) = 0 \det DX(0,0)=0 and Tr ​ D ​ X ​ ( 0, 0) = 0 \text{Tr}\;DX(0,0)=0. Let X ε, δ = ( R ε, S δ) X_{\varepsilon,\delta}=(R_{\varepsilon},S_{\delta}) be given by

 | R ε ​ ( x, y) = ( a ​ x + ( b + ε) ​ y) ​ P ​ ( x, y), S δ ​ ( x, y) = ( ( a + δ) ​ x + b ​ y) ​ Q ​ ( x, y), R_{\varepsilon}(x,y)=(ax+(b+\varepsilon)y)P(x,y),\quad\quad S_{\delta}(x,y)=((a+\delta)x+by)Q(x,y), |  |

and observe that we can take | ε | > 0 |\varepsilon|>0 and | δ | > 0 |\delta|>0 small enough such that the following statements hold.

1. (i)

All the hyperbolic limit cycles inside B B persist.

2. (ii)

The origin is an isolated singularity.

3. (iii)

det D ​ X ε, δ ​ ( 0, 0) > 0 \det DX_{\varepsilon,\delta}(0,0)>0 and Tr ​ D ​ X ε, δ ​ ( 0, 0) = 0 \text{Tr}\;DX_{\varepsilon,\delta}(0,0)=0.

Hence, the origin is a monodromic singularity of X ε, δ X_{\varepsilon,\delta}. Let L 1 L_{1} be its first *Lyapunov constant*(see Adronov et al. [1, p. 254]). Except perhaps by an arbitrarily small perturbation on the nonlinear terms of X ε, δ X_{\varepsilon,\delta}, we can suppose L 1 ≠ 0 L_{1}\neq 0. Therefore, we can take another small enough perturbation W ∈ 𝒳 n + 1 W\in\mathcal{X}^{n+1} of X ε, δ X_{\varepsilon,\delta} such that a limit cycle bifurcates from the origin, while the others persist. Hence we obtain

 | π ⁡ ( W) ⩾ π ⁡ ( Y) + 1 = ℋ ⁡ ( n) + 1, \pi(W)\geqslant\pi(Y)+1=\mathcal{H}(n)+1, |  |

and thus ℋ ⁡ ( n + 1) ⩾ ℋ ⁡ ( n) + 1 \mathcal{H}(n+1)\geqslant\mathcal{H}(n)+1.

Suppose now ℋ ⁡ ( n) = ∞ \mathcal{H}(n)=\infty. It follows Theorem 2 ( b) (b) that there is a sequence ( Z k) (Z_{k}), with Z k ∈ Σ h n Z_{k}\in\Sigma_{h}^{n}, such that π ⁡ ( Z k) → ∞ \pi(Z_{k})\to\infty. Since π ⁡ ( Z k) < ∞ \pi(Z_{k})<\infty, we can apply the above reasoning on each Z k Z_{k} obtaining a sequence ( W k) (W_{k}), with W k ∈ 𝒳 n + 1 W_{k}\in\mathcal{X}^{n+1}, such that π ⁡ ( W k) → ∞ \pi(W_{k})\to\infty and thus proving that ℋ ⁡ ( n + 1) = ∞ \mathcal{H}(n+1)=\infty. ∎

## 4. Final remarks and a folklore result

Theorem 1 is not the first known result about recurrence properties of ℋ ⁡ ( n) \mathcal{H}(n). It follows from the proof of Christopher and Lloyd [4] that ℋ ⁡ ( 2 ​ n + 1) ⩾ 4 ​ ℋ ​ ( n) \mathcal{H}(2n+1)\geqslant 4\mathcal{H}(n). Roughly speaking, given X ∈ 𝒳 n X\in\mathcal{X}^{n}, the authors translate all the limit cycles of X X to the first quadrant and thus apply the non-invertible transformation ( x, y) ↦ ( u 2, v 2) (x,y)\mapsto(u^{2},v^{2}), followed by the rescaling of time d ​ t / d ​ τ = 2 ​ u ​ v dt/d\tau=2uv. Hence, obtaining Y ∈ 𝒳 2 ​ n + 1 Y\in\mathcal{X}^{2n+1} with a diffeomorphic copy of X X in each open quadrant.

The challenge of Theorem 1 has been to relate ℋ ⁡ ( n + 1) \mathcal{H}(n+1) with ℋ ⁡ ( n) \mathcal{H}(n). It is much more easy for example to prove that ℋ ⁡ ( n + 2) ⩾ ℋ ⁡ ( n) + 1 \mathcal{H}(n+2)\geqslant\mathcal{H}(n)+1. Indeed, given X ∈ 𝒳 n X\in\mathcal{X}^{n} let Y = ( x 2 + y 2) ​ X ∈ 𝒳 n + 2 Y=(x^{2}+y^{2})X\in\mathcal{X}^{n+2} and observe that Y Y is equivalent to X X except at the origin, where it has an extra degenerate singularity. Hence, similarly to the end of the proof of Theorem 1, we can take a small perturbation of Y Y creating an extra limit cycle.

We end this note with the following folklore result.

###### Proposition 3.

Let X X be a planar analytic vector field. Then X X has an enumerable number of limit cycles. In particular, ℋ ⁡ ( n) ⩽ ℵ 0 \mathcal{H}(n)\leqslant\aleph_{0} for every n ∈ ℕ n\in\mathbb{N}.

###### Proof.

If X X has no limit cycles, then there is nothing to prove. Suppose therefore that X X has at least one limit cycle and let Γ = { γ a } a ∈ A \Gamma=\{\gamma_{a}\}_{a\in A} be an indexation of all its limit cycles, A ≠ ∅ A\neq\emptyset. For each a ∈ A a\in A, set

 | δ a = inf { d ( γ a, γ b): b ∈ A, b ≠ a }, \delta_{a}=\inf\{d(\gamma_{a},\gamma_{b})\colon b\in A,\;b\neq a\}, |  |

where d ⁡ ( γ a, γ b) d(\gamma_{a},\gamma_{b}) is the usual distance between the compact sets γ a \gamma_{a} and γ b \gamma_{b},

 | d ( γ a, γ b) = min { | | q a − q b | |: q a ∈ γ a, q b ∈ γ b }. d(\gamma_{a},\gamma_{b})=\min\{||q_{a}-q_{b}||\colon q_{a}\in\gamma_{a},\;q_{b}\in\gamma_{b}\}. |  |

Since X X is analytic, it follows that γ a \gamma_{a} must be isolated (see [14, p. 217 217]) and thus δ a > 0 \delta_{a}>0 for every a ∈ A a\in A. Let N a ⊂ ℝ 2 N_{a}\subset\mathbb{R}^{2} be the open δ a / 2 \delta_{a}/2 -neighborhood of γ a \gamma_{a}, a ∈ A a\in A. Observe that if a ≠ b a\neq b, then N a ∩ N b = ∅ N_{a}\cap N_{b}=\emptyset (for otherwise d ⁡ ( γ a, γ b) < max ⁡ { δ a, δ b } d(\gamma_{a},\gamma_{b})<\max\{\delta_{a},\delta_{b}\}). For each a ∈ A a\in A, choose r a ∈ N a ∩ ℚ 2 r_{a}\in N_{a}\cap\mathbb{Q}^{2} and define i ⁡ ( a) = r a. i(a)=r_{a}. Observe that r a ≠ r b r_{a}\neq r_{b} if a ≠ b a\neq b. Hence, we have an injective map i: A → ℚ 2 i\colon A\to\mathbb{Q}^{2} and thus A A is enumerable. ∎

Notice that Proposition 3 is optimal for the analytic case. For instance, the planar analytic vector field

 | x ˙ = − y + x ​ sin ⁡ ( x 2 + y 2), y ˙ = x + y ​ sin ⁡ ( x 2 + y 2), \dot{x}=-y+x\sin(x^{2}+y^{2}),\quad\dot{y}=x+y\sin(x^{2}+y^{2}), |  |

has infinitely many limit cycles, given by x 2 + y 2 = k ​ π x^{2}+y^{2}=k\pi, with k ∈ ℤ > 0 k\in\mathbb{Z}_{>0}.

## Acknowledgments

This work is supported by the Spanish State Research Agency, through the projects PID2022-136613NB-I00 grant and the Severo Ochoa and María de Maeztu Program for Centers and Units of Excellence in R&D (CEX2020-001084-M), grant 2021-SGR-00113 from AGAUR, Generalitat de Catalunya, and by São Paulo Research Foundation (FAPESP), grants 2019/10269-3, 2021/01799-9 and 2022/14353-1.

## References

- [1] A. A. Andronov et al Theory of Bifurcations of Dynamic Systems on a Plane, Wiley, New York & Toronto (1973).
- [2] F. E. Browder, Mathematical Developments Arising from Hilbert Problems, Proc. Sympos. Pure Math., volume XXVIII, part I (1976).
- [3] L. Chen and M. Wang, The relative position, and the number, of limit cycles of a quadratic differential system, Acta Math. Sinica (Chin. Ser.) 22, 751–758 (1979).
- [4] C. Christopher and N. G. Lloyd, Polynomial Systems: A Lower Bound for the Hilbert Numbers, Proc. R. Soc. Lond., Ser. A 450, No. 1938, 219–224 (1995).
- [5] G. F. D. Duff, Limit-cycles and rotated vector fields, Ann. Math. (2) 57, 15–31 (1953).
- [6] J. Écalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, Actualités Mathématiques. Paris: Hermann, Éditeurs des Sciences et des Arts.
- [7] M. Han, Global behavior of limit cycles in rotated vector fields, J. Differ. Equations 151, No. 1, 20–35 (1999).
- [8] M. Han and J. Li, Lower bounds for the Hilbert number of polynomial systems, J. Differ. Equations 252, No. 4, 3278–3304 (2012).
- [9] Y. S. Il’yashenko, Finiteness theorems for limit cycles, Translations of Mathematical Monographs, American Mathematical Society (1991).
- [10] C. Li, C. Liu and J. Yang, A cubic system with thirteen limit cycles, J. Differ. Equations 246, No. 9, 3609–3619 (2009).
- [11] J. Li, Hilbert’s 16th Problem and bifurcations of Planar Polynomial Vector Fields, Int. J. Bifurc. Chaos 13, 47–106 (2003).
- [12] M. M. Peixoto, Structural stability on two-dimensional manifolds, Topology 1, 101–120 (1962).
- [13] L. M. Perko, Bifurcation of limit cycles: Geometric theory, Proc. Am. Math. Soc. 114, No. 1, 225–236 (1992).
- [14] L. M. Perko, Differential equations and dynamical systems, vol. 7 of Texts in Applied Mathematics, Springer-Verlag, New York, third ed, 2001.
- [15] R. Prohens and J. Torregrosa, New lower bounds for the Hilbert numbers using reversible centers, Nonlinearity 32, No. 1, 331–355 (2019).
- [16] D. Shafer, Structural stability and generic properties of planar polynomial vector fields, Rev. Mat. Iberoam. 3, No. 3-4, 337–355 (1987).
- [17] P. Santana, On the structural instability of non-hyperbolic limit cycles on planar polynomial vector fields, to appear in São Paulo J. Math. Sci. (2024).
- [18] S. Songling, A concrete example of the existence of four limit cycles for plane quadratic systems, Sci. Sin. 23, 153–158 (1980).
- [19] J. Sotomayor, Stable planar polynomial vector fields, Rev. Mat. Iberoam. 1, No. 2, 15–23 (1985).
- [20] M. Yeung, On the monograph “Finiteness Theorems for limit cycles” and a special case of alternant cycles, Preprint, arXiv:2402.12506 (2024).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:armengol.gasull@uab.cat
[4]: mailto:paulo.santana@unesp.br
