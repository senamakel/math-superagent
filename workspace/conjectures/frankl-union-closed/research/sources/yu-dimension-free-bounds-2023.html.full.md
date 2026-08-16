<!-- source: https://arxiv.org/html/2212.00658v2 | converted from HTML -->

Dimension-Free Bounds for the Union-Closed Sets Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2212.00658v2 [math.CO] 05 May 2023

# Dimension-Free Bounds for the Union-Closed Sets Conjecture

Lei Yu

###### Abstract

The union-closed sets conjecture states that in any nonempty union-closed family ℱ \mathcal{F} of subsets of a finite set, there exists an element contained in at least a proportion 1 / 2 1/2 of the sets of ℱ \mathcal{F}. Using the information-theoretic method, Gilmer Gilmer 2022 recently showed that there exists an element contained in at least a proportion 0.01 0.01 of the sets of such ℱ \mathcal{F}. He conjectured that his technique can be pushed to the constant 3 − 5 2 \frac{3-\sqrt{5}}{2} which was subsequently confirmed by several researchers Sawin 2022; Chase and Lovett 2022; Alweiss et al. 2022; Pebody 2022. Furthermore, Sawin Sawin 2022 showed that Gilmer’s technique can be improved to obtain a bound better than 3 − 5 2 \frac{3-\sqrt{5}}{2}, but this new bound is not explicitly given by Sawin. This paper further improves Gilmer’s technique to derive new bounds in the optimization form for the union-closed sets conjecture. These bounds include Sawin’s improvement as a special case. By providing cardinality bounds on auxiliary random variables, we make Sawin’s improvement computable, and then evaluate it numerically which yields a bound around 0.38234 0.38234, slightly better than 3 − 5 2 ≈ 0.38197 \frac{3-\sqrt{5}}{2}\approx 0.38197.

###### keywords

union-closed sets conjecture; information-theoretic method; coupling

† † firstpage: 1 † † volume: 1 † † issue: 1 † † articlenumber: 0 † † year: 2023 † † copyright-year: 2023 † † hreflink: https://doi.org/ † † titlecitation: Dimension-Free Bounds for the Union-Closed Sets Conjecture † † authornames: Lei Yu † † authorcitation: Yu, L. † † address: 1 School of Statistics and Data Science, LPMC, KLMDASR, and LEBPS, Nankai University, Tianjin 300071, China; leiyu@nankai.edu.cn † † reftitle: References

## 1 Introduction

This paper concerns the union-closed conjecture which is described in the information-theoretic language as follows. Note that each set B ⊆ [n]:= { 1, 2, …, n } B\subseteq[n]:=\{1,2,\dots,n\} uniquely corresponds to an n n -length sequence x n:= ( x 1, x 2, …, x n) ∈ Ω n x^{n}:=(x_{1},x_{2},\dots,x_{n})\in\Omega^{n} with Ω:= { 0, 1 } \Omega:=\{0,1\} in the way that x i = 1 x_{i}=1 if i ∈ B i\in B and x i = 0 x_{i}=0 otherwise. So, a family ℱ \mathcal{F} of subsets of [n] [n] uniquely corresponds to a subset A ⊆ Ω n A\subseteq\Omega^{n}. Denote the (element-wise) OR operation for two finite Ω \Omega -valued sequences as x n ∨ y n:= ( x i ∨ y i) i ∈ [n] x^{n}\vee y^{n}:=(x_{i}\vee y_{i})_{i\in[n]} with x n, y n ∈ Ω n x^{n},y^{n}\in\Omega^{n}, where ∨ \vee is the OR operation. The family ℱ \mathcal{F} is closed under the union operation (i.e., F ∪ G ∈ ℱ, ∀ F, G ∈ ℱ F\cup G\in\mathcal{F},\forall F,G\in\mathcal{F}) if and only if the corresponding set A ⊆ Ω n A\subseteq\Omega^{n} is closed under the OR operation (i.e., x n ∨ y n ∈ A, ∀ x n, y n ∈ A x^{n}\vee y^{n}\in A,\forall x^{n},y^{n}\in A).

Let A ⊆ Ω n A\subseteq\Omega^{n} be closed under the OR operation. Let X n:= ( X 1, X 2, …, X n) X^{n}:=(X_{1},X_{2},\dots,X_{n}) be a random vector uniformly distributed on A A, and denote P X n = Unif ⁡ ( A) P_{X^{n}}=\mathrm{Unif}(A) as its distribution (or probability mass function, PMF). We are interested in estimating

 | p A:= max i ∈ [n] ⁡ P X i ​ ( 1) p_{A}:=\max_{i\in[n]}P_{X_{i}}(1) |  |

where P X i P_{X_{i}} is the distribution of X i X_{i}, and hence, P X i ​ ( 1) P_{X_{i}}(1) is the proportion of the sets containing the element i i among all sets in ℱ \mathcal{F}. Frankl made the following conjecture.

###### Conjecture 1 (Frankl Union-Closed Sets Conjecture).

p A ≥ 1 / 2 p_{A}\geq 1/2 for any OR-closed set A A.

This conjecture equivalently states that for any union-closed family ℱ \mathcal{F}, there exists an element contained in at least a proportion 1 / 2 1/2 of the sets of ℱ \mathcal{F}. Since the union-closed conjecture was posed by Peter Frankl in 1979, it had attracted a great deal of research interest; see, e.g., Balla et al. 2013; Johnson and Vaughan 1998; Karpas 2017; Knill 1994; Wójcik 1999. We refer readers to the survey paper Bruhn and Schaudt 2015 for more details. Gilmer Gilmer 2022 made a breakthrough recently, showing that this conjecture holds with constant 0.01 0.01. Gilmer’s method used a clever idea from information theory in which two independent random vectors were constructed. It was conjectured by him that his method can improve the constant to 3 − 5 2 \frac{3-\sqrt{5}}{2}, which is now confirmed by several groups of researchers Alweiss et al. 2022; Chase and Lovett 2022; Sawin 2022; Pebody 2022. This constant is shown to be the best for an approximate version of the union-closed sets problem Chase and Lovett 2022. Moreover, Sawin Sawin 2022 further develops Gilmer’s idea by allowing the two random vectors to depend with each other. Such a technique was in fact used by the present author in several existing works Yu and Tan 2020; Yu 2021; Yu 2022. By this technique, Sawin Sawin 2022 showed that the constant can be improved to a value that is strictly larger than 3 − 5 2 \frac{3-\sqrt{5}}{2}. However, without cardinality bounds on auxiliary random variables, Sawin’s constant is difficult to compute, and hence, the accurate value of this improved constant is not explicitly given in Sawin 2022.

The present paper further develops Gilmer’s (or Sawin’s) technique to derive new constants (or bounds) in the optimization form for the union-closed sets conjecture. These bounds include Sawin’s improvement as a special case. By providing cardinality bounds on auxiliary random variables, we make Sawin’s improvement computable, and then evaluate it numerically which yields a bound around 0.38234 0.38234, slightly better than 3 − 5 2 ≈ 0.38197 \frac{3-\sqrt{5}}{2}\approx 0.38197.

## 2 Main Results

To state our result, we need to introduce some notations. Since we only consider distributions on finite alphabets, we do not distinguish between the terms “distributions” and “probability mass functions”. For a pair of distributions ( P X, P Y) (P_{X},P_{Y}), a coupling of ( P X, P Y) (P_{X},P_{Y}) is a joint distribution P X ​ Y P_{XY} whose marginals are respectively P X, P Y P_{X},P_{Y}. For a distribution P X P_{X} defined on a finite alphabet 𝒳 \mathcal{X}, a coupling P X ​ X ′ P_{XX^{\prime}} of ( P X, P X) (P_{X},P_{X}) is called symmetric if P X ​ X ′ ​ ( x, y) = P X ​ X ′ ​ ( y, x) P_{XX^{\prime}}(x,y)=P_{XX^{\prime}}(y,x) for all x, y ∈ 𝒳 x,y\in\mathcal{X}. Denote 𝒞 s ​ ( P X) \mathcal{C}_{\mathrm{s}}(P_{X}) as the set of symmetric couplings of ( P X, P X) (P_{X},P_{X}). Denote δ x \delta_{x} as the Dirac measure with atom at x x.

For a joint distribution P X ​ Y P_{XY}, the (Pearson) correlation coefficient between ( X, Y) ∼ P X ​ Y (X,Y)\sim P_{XY} is defined by

 | ρ p ​ ( X, Y):= { Cov ⁡ ( X, Y) Var ⁡ ( X) ​ Var ​ ( Y), Var ⁡ ( X) ​ Var ​ ( Y) > 0 0, Var ⁡ ( X) ​ Var ​ ( Y) = 0. \rho_{\mathrm{p}}(X;Y):=\left\{\begin{array}[]{ll}\frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)\mathrm{Var}(Y)}},&\mathrm{Var}(X)\mathrm{Var}(Y)>0\\ 0,&\mathrm{Var}(X)\mathrm{Var}(Y)=0\end{array}\right.. |  |

The maximal correlation between ( X, Y) ∼ P X ​ Y (X,Y)\sim P_{XY} is defined by

 | ρ m ​ ( X, Y) \displaystyle\rho_{\mathrm{m}}(X;Y) | : = ρ p ​ ( f ⁡ ( X), g ⁡ ( Y)) \displaystyle:=\rho_{\mathrm{p}}(f(X);g(Y)) |  |

 |  | = sup f, g { Cov ⁡ ( f ⁡ ( X), g ⁡ ( Y)) Var ⁡ ( f ⁡ ( X)) ​ Var ​ ( g ⁡ ( Y)), Var ⁡ ( f ⁡ ( X)) ​ Var ​ ( g ⁡ ( Y)) > 0 0, Var ⁡ ( f ⁡ ( X)) ​ Var ​ ( g ⁡ ( Y)) = 0, \displaystyle=\sup_{f,g}\left\{\begin{array}[]{ll}\frac{\mathrm{Cov}(f(X),g(Y))}{\sqrt{\mathrm{Var}(f(X))\mathrm{Var}(g(Y))}},&\mathrm{Var}(f(X))\mathrm{Var}(g(Y))>0\\ 0,&\mathrm{Var}(f(X))\mathrm{Var}(g(Y))=0\end{array}\right., |  |

where the supremum is taken over all pairs of real-valued functions ( f, g) \left(f,g\right) such that Var ⁡ ( f ⁡ ( X)) ​ Var ​ ( g ⁡ ( Y)) < ∞ \mathrm{Var}(f(X))\mathrm{Var}(g(Y))<\infty. Note that ρ m ​ ( X, Y) ∈ [0, 1] \rho_{\mathrm{m}}(X;Y)\in[0,1], and moreover, ρ m ​ ( X, Y) = 0 \rho_{\mathrm{m}}(X;Y)=0 if and only if X, Y X,Y are independent. Moreover, ρ m ​ ( X, Y) \rho_{\mathrm{m}}(X;Y) is equal to the second largest singular value of the matrix [P X ​ Y ​ ( x, y) P X ​ ( x) ​ P Y ​ ( y)] ( x, y) \left[\frac{P_{XY}(x,y)}{\sqrt{P_{X}(x)P_{Y}(y)}}\right]_{(x,y)}; see, e.g., Witsenhausen 1975. Clearly, the largest singular value of the matrix [P X ​ Y ​ ( x, y) P X ​ ( x) ​ P Y ​ ( y)] ( x, y) \left[\frac{P_{XY}(x,y)}{\sqrt{P_{X}(x)P_{Y}(y)}}\right]_{(x,y)} is equal to 1 1 with corresponding eigenvectors ( P X ​ ( x)) x (\sqrt{P_{X}(x)})_{x} and ( P Y ​ ( y)) y (\sqrt{P_{Y}(y)})_{y}.

Denote for p, q, ρ ∈ [0, 1] p,q,\rho\in[0,1],

 | z 1 \displaystyle z_{1} | : = p ​ q − ρ ​ p ⁡ ( 1 − p) ​ q ​ ( 1 − q) \displaystyle:=pq-\rho\sqrt{p(1-p)q(1-q)} |  |

 | z 2 \displaystyle z_{2} | : = p ​ q + ρ ​ p ⁡ ( 1 − p) ​ q ​ ( 1 − q) \displaystyle:=pq+\rho\sqrt{p(1-p)q(1-q)} |  |

and

 | φ ⁡ ( ρ, p, q):= median ⁡ { max ⁡ { p, q, p + q − z 2 }, 1 / 2, min ⁡ { p + q, p + q − z 1 } }, \varphi(\rho,p,q):=\mathrm{median}\left\{\max\{p,q,p+q-z_{2}\},1/2,\min\{p+q,p+q-z_{1}\}\right\}, |  | (1) |

where median ​ A \mathrm{median}A denotes the median value of elements in a multiset A A. We regard the set in ( 1) as a multiset which means median ​ { a, a, b } = a \mathrm{median}\{a,a,b\}=a. Denote h ⁡ ( a) = − a ​ log 2 ​ a − ( 1 − a) ​ log 2 ⁡ ( 1 − a) h(a)=-a\log_{2}a-(1-a)\log_{2}(1-a) for a ∈ [0, 1] a\in[0,1] as the binary entropy function. Define for t > 0 t>0,

 | Γ ( t):= sup P ρ inf P p: 𝔼 ​ h ​ ( p) > 0, 𝔼 ​ p ≤ t 𝔼 ρ [inf P p ​ q ∈ 𝒞 s ​ ( P p): ρ m ​ ( p, q) ≤ ρ 𝔼 p, q ​ h ​ ( φ ⁡ ( ρ, p, q)) 𝔼 ​ h ​ ( p)], \Gamma(t):=\sup_{P_{\rho}}\inf_{P_{p}:\mathbb{E}h(p)>0,\mathbb{E}p\leq t}\mathbb{E}_{\rho}\left[\inf_{P_{pq}\in\mathcal{C}_{\mathrm{s}}(P_{p}):\rho_{\mathrm{m}}(p;q)\leq\rho}\frac{\mathbb{E}_{p,q}h(\varphi(\rho,p,q))}{\mathbb{E}h(p)}\right], |  | (2) |

where the supremum over P ρ P_{\rho} and the infimum over P p P_{p} are both taken over all finitely supported probability distributions on [0, 1] [0,1].

Our main results are as follows.

###### Theorem 1.

If Γ ⁡ ( t) > 1 \Gamma(t)>1 for some t ∈ ( 0, 1 / 2) t\in(0,1/2), then p A ≥ t p_{A}\geq t for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n} (i.e., for any union-closed family ℱ \mathcal{F}, there exists an element contained in at least a proportion t t of the sets of ℱ \mathcal{F}).

The proof of Theorem 1 is given in Section 2 by using a technique based on coupling and entropy. It is essentially the same as the technique used by Sawin Sawin 2022. However, prior to Sawin’s work, such a technique was used by the present author in several works; see Yu and Tan 2020; Yu 2021; Yu 2022.

Equivalently, Theorem 1 states that p A ≥ t max p_{A}\geq t_{\max} for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n}, where t max:= sup { t ∈ ( 0, 1 / 2): Γ ⁡ ( t) > 1 }. t_{\max}:=\sup\{t\in(0,1/2):\Gamma(t)>1\}. To compute Γ ⁡ ( t) \Gamma(t) or its lower bounds numerically, it requires to upper bound the cardinality of the support of P p P_{p} in the outer infimum in ( 2), since otherwise, infinitely many parameters are needed to optimize. This is left to be done in a future work. The following gives a computable bound.

If we choose P ρ = δ 0 P_{\rho}=\delta_{0}, then Theorem 1 implies Gilmer’s bound in Gilmer 2022, since for this case, the couplings constructed in the proof of Theorem 1 (given in the next section) turn to be independent, coinciding with Gilmer’s construction. On the other hand, if we choose P ρ = δ 1 P_{\rho}=\delta_{1}, then the couplings constructed in our proof are arbitrary. In fact, we can make a choice of P ρ P_{\rho} better than these two special cases. As suggested by Sawin Sawin 2022, we can choose P ρ = ( 1 − α) ​ δ 0 + α ​ δ 1 P_{\rho}=(1-\alpha)\delta_{0}+\alpha\delta_{1} which in fact leads to an optimization over mixtures of independent couplings and arbitrary couplings. This final choice yields the following bound.

Substituting ρ = 0 \rho=0 and 1 1 respectively into φ ⁡ ( ρ, p, q) \varphi(\rho,p,q) yields

 | φ ⁡ ( 0, p, q) \displaystyle\varphi(0,p,q) | = p + q − p ​ q, \displaystyle=p+q-pq, |  | (3) |

 | φ ⁡ ( 1, p, q) \displaystyle\varphi(1,p,q) | = median ⁡ { max ⁡ { p, q }, 1 / 2, p + q }, \displaystyle=\mathrm{median}\left\{\max\{p,q\},1/2,p+q\right\}, |  | (4) |

where in the evaluation of φ ⁡ ( 1, p, q), \varphi(1,p,q), the following facts were used: 1)

 | p + q − p ​ q − p ⁡ ( 1 − p) ​ q ​ ( 1 − q) ≤ max ⁡ { p, q } p+q-pq-\sqrt{p(1-p)q(1-q)}\leq\max\{p,q\} |  |

for all p, q ∈ [0, 1] p,q\in[0,1]; 2) if p + q ≤ 1 p+q\leq 1, then

 | p + q − p ​ q + p ⁡ ( 1 − p) ​ q ​ ( 1 − q) ≥ p + q, p+q-pq+\sqrt{p(1-p)q(1-q)}\geq p+q, |  |

and otherwise,

 | 1 / 2 < max ⁡ { p, q } ≤ p + q − p ​ q + p ⁡ ( 1 − p) ​ q ​ ( 1 − q). 1/2<\max\{p,q\}\leq p+q-pq+\sqrt{p(1-p)q(1-q)}. |  |

By defining

 | g ⁡ ( P p ​ q, α) \displaystyle g(P_{pq},\alpha) | : = ( 1 − α) ​ 𝔼 ( p, q) ∼ P p ⊗ 2 ​ h ​ ( p + q − p ​ q) \displaystyle:=(1-\alpha)\mathbb{E}_{(p,q)\sim P_{p}^{\otimes 2}}h(p+q-pq) |  |

 |  | + α ​ 𝔼 ( p, q) ∼ P p ​ q ​ h ​ ( φ ⁡ ( 1, p, q)) \displaystyle\qquad+\alpha\mathbb{E}_{(p,q)\sim P_{pq}}h(\varphi(1,p,q)) |  |

and substituting P ρ = ( 1 − α) ​ δ 0 + α ​ δ 1 P_{\rho}=(1-\alpha)\delta_{0}+\alpha\delta_{1} into Theorem 1, one obtains the following simpler bound.

###### Proposition 1.

For t ∈ ( 0, 1 / 2) t\in(0,1/2),

 | Γ ( t) ≥ Γ ^ ( t):= sup α ∈ [0, 1] inf symmetric ​ P p ​ q: 𝔼 ​ h ​ ( p) > 0 g ⁡ ( P p ​ q, α) 𝔼 ​ h ​ ( p), \Gamma(t)\geq\hat{\Gamma}(t):=\sup_{\alpha\in[0,1]}\inf_{\textrm{symmetric }P_{pq}:\mathbb{E}h(p)>0}\frac{g(P_{pq},\alpha)}{\mathbb{E}h(p)}, |  | (5) |

where the infimum is taken over all distributions P p ​ q P_{pq} of the form ( 1 − β) ​ Q a 1, a 2 + β ​ Q b 1, b 2 (1-\beta)Q_{a_{1},a_{2}}+\beta Q_{b_{1},b_{2}} with

 | 0 ≤ a:= a 1 + a 2 2 ≤ t < b:= b 1 + b 2 2 ≤ 1 0\leq a:=\frac{a_{1}+a_{2}}{2}\leq t<b:=\frac{b_{1}+b_{2}}{2}\leq 1 |  | (6) |

and β = 0 \beta=0 or β = t − a b − a > 0 \beta=\frac{t-a}{b-a}>0 such that 1 1 1 Note that 𝔼 ​ h ​ ( p) = 0 \mathbb{E}h(p)=0 if and only if P p ​ q P_{pq} is a convex combination of δ ( 0, 0) \delta_{(0,0)}, δ ( 0, 1) \delta_{(0,1)}, δ ( 1, 0) \delta_{(1,0)}, and δ ( 1, 1) \delta_{(1,1)}. 𝔼 ​ h ​ ( p) > 0 \mathbb{E}h(p)>0. Here,

 | Q x, y:= 1 2 ​ δ ( x, y) + 1 2 ​ δ ( y, x) Q_{x,y}:=\frac{1}{2}\delta_{(x,y)}+\frac{1}{2}\delta_{(y,x)} |  | (7) |

with δ ( x, y) \delta_{(x,y)} denoting the Dirac measure at ( x, y) (x,y).

As a consequence of two results above, we have the following corollary.

###### Corollary 1.

If Γ ^ ​ ( t) > 1 \hat{\Gamma}(t)>1 for some t ∈ ( 0, 1 / 2) t\in(0,1/2), then p A ≥ t p_{A}\geq t for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n}.

The proof of Corollary 1 is given in Section 3.

The lower bound in ( 5) without the cardinality bound on the support of P p ​ q P_{pq} was given by Sawin Sawin 2022, which was used to show p A > 3 − 5 2. p_{A}>\frac{3-\sqrt{5}}{2}. However, thanks to the cardinality bound, we can numerically compute the best bound on p A p_{A} that can be derived using Γ ^ ​ ( t) \hat{\Gamma}(t). That is, p A ≥ t ^ max p_{A}\geq\hat{t}_{\max} for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n}, where t ^ max:= sup { t ∈ ( 0, 1 / 2): Γ ^ ​ ( t) > 1 }. \hat{t}_{\max}:=\sup\{t\in(0,1/2):\hat{\Gamma}(t)>1\}. Numerical results 2 2 2 Our code can be found on the author’s homepage https://leiyudotscholar.wordpress.com/ show that if we set α = 0.035, t = 0.38234 \alpha=0.035,t=0.38234, then the optimal P p ​ q = ( 1 − β) ​ Q a, a + β ​ Q a, 1 P_{pq}=(1-\beta)Q_{a,a}+\beta Q_{a,1} with a ≈ 0.3300622 a\approx 0.3300622 and β ≈ 0.1560676 \beta\approx 0.1560676 which leads to the lower bound Γ ^ ​ ( t) ≥ 1.00000889 \hat{\Gamma}(t)\geq 1.00000889. Hence, p A ≥ 0.38234 p_{A}\geq 0.38234 for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n}. This is slightly better than the previous bound 3 − 5 2 ≈ 0.38197 \frac{3-\sqrt{5}}{2}\approx 0.38197. The choice of ( α, t) (\alpha,t) in our evaluation is nearly optimal. More decimal places of Sawin’s bound (or equivalently, t ^ max \hat{t}_{\max}) were computed by Cambie in Cambie 2022, i.e., 0.382345533366702 ≤ t ^ max ≤ 0.382345533366703 0.382345533366702\leq\hat{t}_{\max}\leq 0.382345533366703 which is attained by the choice α ≈ 0.03560698136437784 \alpha\approx 0.03560698136437784. This more precise evaluation can be also verified using our code in Footnote 2.

## 3 Proof of Theorem 1

Denote H ( X) = − ∑ x P X ( x) log P X ( x) H(X)=-\sum_{x}P_{X}(x)\log P_{X}(x) as the Shannon entropy of a random variable X ∼ P X X\sim P_{X}. Let A ⊆ Ω n A\subseteq\Omega^{n} be closed under the OR operation. We assume | A | ≥ 2 |A|\geq 2. This is because, Theorem 1 holds obviously for singletons A A, since for this case, p A = 1 p_{A}=1. Let P X n = Unif ⁡ ( A) P_{X^{n}}=\mathrm{Unif}(A). So, H ⁡ ( X n) > 0 H(X^{n})>0, and by the chain rule, H ⁡ ( X n) = ∑ i = 1 n H ⁡ ( X i | X i − 1) H(X^{n})=\sum_{i=1}^{n}H(X_{i}|X^{i-1}).

If P X n ​ Y n ∈ 𝒞 s ​ ( P X n) P_{X^{n}Y^{n}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n}}), then Z n:= X n ∨ Y n ∈ A Z^{n}:=X^{n}\vee Y^{n}\in A a.s. where ( X n, Y n) ∼ P X n ​ Y n (X^{n},Y^{n})\sim P_{X^{n}Y^{n}}. So, we have

 | H ⁡ ( Z n) ≤ log ⁡ | A | = H ⁡ ( X n). H(Z^{n})\leq\log|A|=H(X^{n}). |  |

We hence have

 | sup P X n ​ Y n ∈ 𝒞 s ​ ( P X n) H ⁡ ( Z n) H ⁡ ( X n) ≤ 1. \sup_{P_{X^{n}Y^{n}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n}})}\frac{H(Z^{n})}{H(X^{n})}\leq 1. |  |

If p A ≤ t p_{A}\leq t, then P X i ​ ( 1) ≤ t, ∀ i ∈ [n] P_{X_{i}}(1)\leq t,\forall i\in[n]. Relaxing P X n = Unif ⁡ ( A) P_{X^{n}}=\mathrm{Unif}(A) to arbitrary distributions such that P X i ​ ( 1) ≤ t P_{X_{i}}(1)\leq t, we obtain Γ n ​ ( t) ≤ 1 \Gamma_{n}(t)\leq 1 where

 | Γ n ( t):= inf P X n: P X i ​ ( 1) ≤ t, ∀ i sup P X n ​ Y n ∈ 𝒞 s ​ ( P X n) H ⁡ ( Z n) H ⁡ ( X n). \Gamma_{n}(t):=\inf_{P_{X^{n}}:P_{X_{i}}(1)\leq t,\forall i}\sup_{P_{X^{n}Y^{n}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n}})}\frac{H(Z^{n})}{H(X^{n})}. |  | (8) |

In other words, if given t t, Γ n ​ ( t) > 1 \Gamma_{n}(t)>1, then by contradiction, p A > t p_{A}>t.

We next show that Γ n ​ ( t) ≥ Γ ⁡ ( t) \Gamma_{n}(t)\geq\Gamma(t) which implies Theorem 1. To this end, we need the following lemmas.

For two conditional distributions P X | U, P Y | V P_{X|U},P_{Y|V}, denote 𝒞 ⁡ ( P X | U, P Y | V) \mathcal{C}(P_{X|U},P_{Y|V}) as the set of conditional distributions Q X ​ Y | U ​ V Q_{XY|UV} such that its marginals satisfying Q X | U ​ V = P X | U, Q Y | U ​ V = P Y | V Q_{X|UV}=P_{X|U},Q_{Y|UV}=P_{Y|V}. The conditional (Pearson) correlation coefficient of X X and Y Y given U U is defined by

 | ρ p ​ ( X; Y | U) = { 𝔼 ⁡ [cov ⁡ ( X, Y | U)] 𝔼 ⁡ [var ⁡ ( X | U)] ​ 𝔼 ⁡ [var ⁡ ( Y | U)], 𝔼 ⁡ [var ⁡ ( X | U)] ​ 𝔼 ​ [var ⁡ ( Y | U)] > 0, 0, 𝔼 ⁡ [var ⁡ ( X | U)] ​ 𝔼 ​ [var ⁡ ( Y | U)] = 0. \rho_{\mathrm{p}}(X;Y|U)=\left\{\begin{array}[]{ll}\frac{\mathbb{E}[\mathrm{cov}(X,Y|U)]}{\sqrt{\mathbb{E}[\mathrm{var}(X|U)]}\sqrt{\mathbb{E}[\mathrm{var}(Y|U)]}},&\mathbb{E}[\mathrm{var}(X|U)]\mathbb{E}[\mathrm{var}(Y|U)]>0,\\ 0,&\mathbb{E}[\mathrm{var}(X|U)]\mathbb{E}[\mathrm{var}(Y|U)]=0.\end{array}\right. |  |

The conditional maximal correlation coefficient of X X and Y Y given U U is defined by

 | ρ m ​ ( X; Y | U) = sup f, g ρ p ​ ( f ⁡ ( X, U); g ⁡ ( Y, U) | U), \rho_{\mathrm{m}}(X;Y|U)=\sup_{f,g}\rho_{\mathrm{p}}(f(X,U);g(Y,U)|U), |  |

where the supremum is taken over all real-valued functions f ⁡ ( x, u), g ⁡ ( y, u) f(x,u),g(y,u) (such that 𝔼 ⁡ [var ⁡ ( f ⁡ ( X, U) | U)] \mathbb{E}[\mathrm{var}(f(X,U)|U)], 𝔼 ⁡ [var ⁡ ( g ⁡ ( Y, U) | U)] < ∞ \mathbb{E}[\mathrm{var}(g(Y,U)|U)]<\infty). It has been shown in Yu 2018 that

 | ρ m ( X; Y | U) = sup u: P U ​ ( u) > 0 ρ m ( X; Y | U = u), \rho_{\mathrm{m}}(X;Y|U)=\sup_{u:P_{U}(u)>0}\rho_{\mathrm{m}}(X;Y|U=u), |  |

where ρ m ​ ( X; Y | U = u) = ρ m ​ ( X ′, Y ′) \rho_{\mathrm{m}}(X;Y|U=u)=\rho_{\mathrm{m}}(X^{\prime};Y^{\prime}) with ( X ′, Y ′) ∼ P X ​ Y | U = u (X^{\prime},Y^{\prime})\sim P_{XY|U=u}.

###### Lemma 1 (Product Construction of Couplings).

( Yu and Tan 2020, Lemma 9) ( Yu 2018, Corollary 3) ( Beigi and Gohari 2015, Lemma 6) For any conditional distributions P X i | X i − 1, P Y i | Y i − 1, i ∈ [n] P_{X_{i}|X^{i-1}},\,P_{Y_{i}|Y^{i-1}},\,i\in[n] and any

 | Q X i ​ Y i | X i − 1 ​ Y i − 1 ∈ 𝒞 ⁡ ( P X i | X i − 1, P Y i | Y i − 1), ∀ i ∈ [n], Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}\in\mathcal{C}(P_{X_{i}|X^{i-1}},P_{Y_{i}|Y^{i-1}}),\forall i\in[n], |  |

it holds that

 | ∏ i = 1 n Q X i ​ Y i | X i − 1 ​ Y i − 1 \displaystyle\prod_{i=1}^{n}Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}} | ∈ 𝒞 ⁡ ( ∏ i = 1 n P X i | X i − 1, ∏ i = 1 n P Y i | Y i − 1). \displaystyle\in\mathcal{C}\Big(\prod_{i=1}^{n}P_{X_{i}|X^{i-1}},\prod_{i=1}^{n}P_{Y_{i}|Y^{i-1}}\Big). |  | (9) |

Moreover, for ( X n, Y n) ∼ ∏ i = 1 n Q X i ​ Y i | X i − 1 ​ Y i − 1 (X^{n},Y^{n})\sim\prod_{i=1}^{n}Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}, it holds that

 | ρ m ( X n; Y n) = max i ∈ [n] ρ m ( X i; Y i | X i − 1, Y i − 1). \rho_{\mathrm{m}}(X^{n};Y^{n})=\max_{i\in[n]}\rho_{\mathrm{m}}(X_{i};Y_{i}|X^{i-1},Y^{i-1}). |  | (10) |

For a conditional distribution P X | U P_{X|U} defined on finite alphabets, a conditional coupling P X ​ X ′ | U ​ U ′ P_{XX^{\prime}|UU^{\prime}} of ( P X | U, P X | U) (P_{X|U},P_{X|U}) is called symmetric if P X ​ X ′ | U ​ U ′ ( x, y | u, v) = P X ​ X ′ | U ​ U ′ ( y, x | v, u) P_{XX^{\prime}|UU^{\prime}}(x,y|u,v)=P_{XX^{\prime}|UU^{\prime}}(y,x|v,u) for all x, y ∈ 𝒳, u, v ∈ 𝒰 x,y\in\mathcal{X},u,v\in\mathcal{U}. Denote 𝒞 s ​ ( P X | U) \mathcal{C}_{\mathrm{s}}(P_{X|U}) as the set of symmetric conditional couplings of ( P X | U, P X | U) (P_{X|U},P_{X|U}). Applying the lemma above to symmetric couplings, we have that if couplings Q X i ​ Y i | X i − 1 ​ Y i − 1 ∈ 𝒞 s ​ ( P X i | X i − 1) Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X_{i}|X^{i-1}}) satisfy ρ m ( X i; Y i | X i − 1, Y i − 1) ≤ ρ \rho_{\mathrm{m}}(X_{i};Y_{i}|X^{i-1},Y^{i-1})\leq\rho for some ρ > 0 \rho>0, then

 | ∏ i = 1 n Q X i ​ Y i | X i − 1 ​ Y i − 1 \displaystyle\prod_{i=1}^{n}Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}} | ∈ 𝒞 s ​ ( ∏ i = 1 n P X i | X i − 1), \displaystyle\in\mathcal{C}_{\mathrm{s}}\Big(\prod_{i=1}^{n}P_{X_{i}|X^{i-1}}\Big), |  |

 | ρ m ​ ( X n, Y n) \displaystyle\rho_{\mathrm{m}}(X^{n};Y^{n}) | ≤ ρ, \displaystyle\leq\rho, |  |

with ( X n, Y n) ∼ ∏ i = 1 n Q X i ​ Y i | X i − 1 ​ Y i − 1 (X^{n},Y^{n})\sim\prod_{i=1}^{n}Q_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}. We hence have that for any ρ ∈ [0, 1] \rho\in[0,1],

 |  | sup P X n ​ Y n ∈ 𝒞 s ​ ( P X n): ρ m ​ ( X n, Y n) ≤ ρ H ( Z n) \displaystyle\sup_{\begin{subarray}{c}P_{X^{n}Y^{n}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n}}):\\ \rho_{\mathrm{m}}(X^{n};Y^{n})\leq\rho\end{subarray}}H(Z^{n}) |  |

 |  | ≥ sup P X n − 1 ​ Y n − 1 ∈ 𝒞 s ​ ( P X n − 1): ρ m ​ ( X n − 1, Y n − 1) ≤ ρ H ( Z n − 1) \displaystyle\geq\sup_{\begin{subarray}{c}P_{X^{n-1}Y^{n-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n-1}}):\\ \rho_{\mathrm{m}}(X^{n-1};Y^{n-1})\leq\rho\end{subarray}}H(Z^{n-1}) |  |

 |  | + sup P X n ​ Y n | X n − 1 ​ Y n − 1 ∈ 𝒞 s ​ ( P X n | X n − 1): ρ m ( X n; Y n | X n − 1, Y n − 1) ≤ ρ H ( Z n | Z n − 1) \displaystyle\qquad+\sup_{\begin{subarray}{c}P_{X_{n}Y_{n}|X^{n-1}Y^{n-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X_{n}|X^{n-1}}):\\ \rho_{\mathrm{m}}(X_{n};Y_{n}|X^{n-1},Y^{n-1})\leq\rho\end{subarray}}H(Z_{n}|Z^{n-1}) |  |

 |  | ≥ sup P X n − 1 ​ Y n − 1 ∈ 𝒞 s ​ ( P X n − 1): ρ m ​ ( X n − 1, Y n − 1) ≤ ρ H ( Z n − 1) \displaystyle\geq\sup_{\begin{subarray}{c}P_{X^{n-1}Y^{n-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n-1}}):\\ \rho_{\mathrm{m}}(X^{n-1};Y^{n-1})\leq\rho\end{subarray}}H(Z^{n-1}) |  |

 |  | + inf P X n − 1 ​ Y n − 1 ∈ 𝒞 s ​ ( P X n − 1): ρ m ​ ( X n − 1, Y n − 1) ≤ ρ sup P X n ​ Y n | X n − 1 ​ Y n − 1 ∈ 𝒞 s ​ ( P X n | X n − 1): ρ m ( X n; Y n | X n − 1, Y n − 1) ≤ ρ H ( Z n | Z n − 1) \displaystyle\qquad+\inf_{\begin{subarray}{c}P_{X^{n-1}Y^{n-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{n-1}}):\\ \rho_{\mathrm{m}}(X^{n-1};Y^{n-1})\leq\rho\end{subarray}}\sup_{\begin{subarray}{c}P_{X_{n}Y_{n}|X^{n-1}Y^{n-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X_{n}|X^{n-1}}):\\ \rho_{\mathrm{m}}(X_{n};Y_{n}|X^{n-1},Y^{n-1})\leq\rho\end{subarray}}H(Z_{n}|Z^{n-1}) |  |

 |  | ≥ ⋯ ⋯ \displaystyle\geq\cdots\cdots |  |

 |  | ≥ ∑ i = 1 n inf P X i − 1 ​ Y i − 1 ∈ 𝒞 s ​ ( P X i − 1): ρ m ​ ( X i − 1, Y i − 1) ≤ ρ sup P X i ​ Y i | X i − 1 ​ Y i − 1 ∈ 𝒞 s ​ ( P X i | X i − 1): ρ m ( X i; Y i | X i − 1, Y i − 1) ≤ ρ H ( Z i | Z i − 1), \displaystyle\geq\sum_{i=1}^{n}\inf_{\begin{subarray}{c}P_{X^{i-1}Y^{i-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{i-1}}):\\ \rho_{\mathrm{m}}(X^{i-1};Y^{i-1})\leq\rho\end{subarray}}\sup_{\begin{subarray}{c}P_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X_{i}|X^{i-1}}):\\ \rho_{\mathrm{m}}(X_{i};Y_{i}|X^{i-1},Y^{i-1})\leq\rho\end{subarray}}H(Z_{i}|Z^{i-1}), |  | (11) |

where the first inequality above follows by Lemma 1 and the chain rule for entropies. In fact, in the derivation above, the i i -th distribution P X i ​ Y i | X i − 1 ​ Y i − 1 P_{X_{i}Y_{i}|X^{i-1}Y^{i-1}} is chosen as a greedy coupling in the sense that it only maximizes the i i -th objective function H ⁡ ( Z i | Z i − 1) H(Z_{i}|Z^{i-1}), regardless of other H ⁡ ( Z j | Z j − 1) H(Z_{j}|Z^{j-1}) with j > i j>i (although it indeed affects their values).

By the fact that conditioning reduces entropy, it holds that

 | H ⁡ ( Z i | Z i − 1) ≥ H ⁡ ( Z i | X i − 1, Y i − 1). H(Z_{i}|Z^{i-1})\geq H(Z_{i}|X^{i-1},Y^{i-1}). |  |

Denote

 | g i ​ ( P X i − 1, ρ):= \displaystyle g_{i}(P_{X^{i-1}},\rho):= | inf P X i − 1 ​ Y i − 1 ∈ 𝒞 s ​ ( P X i − 1): ρ m ​ ( X i − 1, Y i − 1) ≤ ρ sup P X i ​ Y i | X i − 1 ​ Y i − 1 ∈ 𝒞 s ​ ( P X i | X i − 1): ρ m ( X i; Y i | X i − 1, Y i − 1) ≤ ρ H ( Z i | X i − 1, Y i − 1). \displaystyle\inf_{\begin{subarray}{c}P_{X^{i-1}Y^{i-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X^{i-1}}):\\ \rho_{\mathrm{m}}(X^{i-1};Y^{i-1})\leq\rho\end{subarray}}\sup_{\begin{subarray}{c}P_{X_{i}Y_{i}|X^{i-1}Y^{i-1}}\in\mathcal{C}_{\mathrm{s}}(P_{X_{i}|X^{i-1}}):\\ \rho_{\mathrm{m}}(X_{i};Y_{i}|X^{i-1},Y^{i-1})\leq\rho\end{subarray}}H(Z_{i}|X^{i-1},Y^{i-1}). |  | (12) |

Then, the expression at the right-hand side of ( 11) is further lower bounded by ∑ i = 1 n g i ​ ( P X i − 1, ρ) \sum_{i=1}^{n}g_{i}(P_{X^{i-1}},\rho). Combing this with ( 8) and ( 11), and by noting that ρ ∈ [0, 1] \rho\in[0,1] is arbitrary, we obtain that

 | Γ n ​ ( t) \displaystyle\Gamma_{n}(t) | ≥ inf P X n: P X i ​ ( 1) ≤ t, ∀ i sup ρ ∈ [0, 1] ∑ i = 1 n g i ​ ( P X i − 1, ρ) ∑ i = 1 n H ⁡ ( X i | X i − 1) \displaystyle\geq\inf_{P_{X^{n}}:P_{X_{i}}(1)\leq t,\forall i}\frac{\sup_{\rho\in[0,1]}\sum_{i=1}^{n}g_{i}(P_{X^{i-1}},\rho)}{\sum_{i=1}^{n}H(X_{i}|X^{i-1})} |  |

 |  | = inf P X n: P X i ​ ( 1) ≤ t, ∀ i sup P ρ 𝔼 P ρ ​ ∑ i = 1 n g i ​ ( P X i − 1, ρ) ∑ i = 1 n H ⁡ ( X i | X i − 1) \displaystyle=\inf_{P_{X^{n}}:P_{X_{i}}(1)\leq t,\forall i}\frac{\sup_{P_{\rho}}\mathbb{E}_{P_{\rho}}\sum_{i=1}^{n}g_{i}(P_{X^{i-1}},\rho)}{\sum_{i=1}^{n}H(X_{i}|X^{i-1})} |  |

 |  | ≥ sup P ρ inf P X n: P X i ​ ( 1) ≤ t, ∀ i ∑ i = 1 n 𝔼 P ρ ​ g i ​ ( P X i − 1, ρ) ∑ i = 1 n H ⁡ ( X i | X i − 1) \displaystyle\geq\sup_{P_{\rho}}\inf_{P_{X^{n}}:P_{X_{i}}(1)\leq t,\forall i}\frac{\sum_{i=1}^{n}\mathbb{E}_{P_{\rho}}g_{i}(P_{X^{i-1}},\rho)}{\sum_{i=1}^{n}H(X_{i}|X^{i-1})} |  |

 |  | ≥ sup P ρ inf P X n: P X i ​ ( 1) ≤ t, ∀ i min i ∈ [n]: H ⁡ ( X i | X i − 1) > 0 𝔼 P ρ ​ g i ​ ( P X i − 1, ρ) H ⁡ ( X i | X i − 1) \displaystyle\geq\sup_{P_{\rho}}\inf_{P_{X^{n}}:P_{X_{i}}(1)\leq t,\forall i}\min_{i\in[n]:H(X_{i}|X^{i-1})>0}\frac{\mathbb{E}_{P_{\rho}}g_{i}(P_{X^{i-1}},\rho)}{H(X_{i}|X^{i-1})} |  | (13) |

 |  | ≥ sup P ρ inf P X j: H ⁡ ( X j | X j − 1) > 0, P X j ​ ( 1) ≤ t 𝔼 P ρ ​ g j ​ ( P X j − 1, ρ) H ⁡ ( X j | X j − 1), \displaystyle\geq\sup_{P_{\rho}}\inf_{P_{X^{j}}:H(X_{j}|X^{j-1})>0,P_{X_{j}}(1)\leq t}\frac{\mathbb{E}_{P_{\rho}}g_{j}(P_{X^{j-1}},\rho)}{H(X_{j}|X^{j-1})}, |  |

where

- •

( 13) follows since a + b c + d ≥ min ⁡ { a c, b d } \frac{a+b}{c+d}\geq\min\{\frac{a}{c},\frac{b}{d}\} for a, b ≥ 0, c, d > 0 a,b\geq 0,c,d>0, and H ⁡ ( X i | X i − 1) = 0 H(X_{i}|X^{i-1})=0 implies X i X_{i} is a function of X i − 1 X^{i-1}, and hence, g i ​ ( P X i − 1, ρ) = 0 g_{i}(P_{X^{i-1}},\rho)=0;

- •

the index j j in the last line is the optimal i i attaining the minimum in ( 13).

Denote X = X j, Y = Y j, U = X j − 1, V = Y j − 1 X=X_{j},Y=Y_{j},U=X^{j-1},V=Y^{j-1}, and Z = X ∨ Y Z=X\lor Y. Then,

 | Γ n ​ ( t) \displaystyle\Gamma_{n}(t) | ≥ sup P ρ inf P U ​ X: H ⁡ ( X | U) > 0, P X ​ ( 1) ≤ t 𝔼 P ρ [inf P U ​ V ∈ 𝒞 s ​ ( P U): ρ m ​ ( U, V) ≤ ρ sup P X ​ Y | U ​ V ∈ 𝒞 s ​ ( P X | U): ρ m ( X; Y | U, V) ≤ ρ H ⁡ ( Z | U, V) H ⁡ ( X | U)]. \displaystyle\geq\sup_{P_{\rho}}\inf_{P_{UX}:H(X|U)>0,P_{X}(1)\leq t}\mathbb{E}_{P_{\rho}}\left[\inf_{\begin{subarray}{c}P_{UV}\in\mathcal{C}_{\mathrm{s}}(P_{U}):\\ \rho_{\mathrm{m}}(U;V)\leq\rho\end{subarray}}\sup_{\begin{subarray}{c}P_{XY|UV}\in\mathcal{C}_{\mathrm{s}}(P_{X|U}):\\ \rho_{\mathrm{m}}(X;Y|U,V)\leq\rho\end{subarray}}\frac{H(Z|U,V)}{H(X|U)}\right]. |  | (14) |

We next further simplify the lower bound in ( 14). Denote

 | p = P X | U ( 1 | U), q = P Y | V ( 1 | V), r = P X ​ Y | U ​ V ( 1, 1 | U, V). p=P_{X|U}(1|U),q=P_{Y|V}(1|V),r=P_{XY|UV}(1,1|U,V). |  | (15) |

So,

 | P X ​ Y | U ​ V ( ⋅ | U, V) = [1 + r − p − q q − r p − r r] P_{XY|UV}(\cdot|U,V)=\begin{bmatrix}1+r-p-q&q-r\\ p-r&r\end{bmatrix} |  |

with

 | max ⁡ { 0, p + q − 1 } ≤ r ≤ min ⁡ { p, q }. \max\{0,p+q-1\}\leq r\leq\min\{p,q\}. |  |

Note that

 | ρ m ( X; Y | U, V) \displaystyle\rho_{\mathrm{m}}(X;Y|U,V) | = sup u, v: P U ​ V ​ ( u, v) > 0 ρ m ( X u; Y v) \displaystyle=\sup_{u,v:P_{UV}(u,v)>0}\rho_{\mathrm{m}}(X_{u};Y_{v}) |  |

 |  | = sup u, v: P U ​ V ​ ( u, v) > 0 | ρ p ( X u; Y v) | \displaystyle=\sup_{u,v:P_{UV}(u,v)>0}\left|\rho_{\mathrm{p}}(X_{u};Y_{v})\right| |  | (16) |

 |  | = sup u, v: P U ​ V ​ ( u, v) > 0 | r − p ​ q | p ⁡ ( 1 − p) ​ q ​ ( 1 − q), \displaystyle=\sup_{u,v:P_{UV}(u,v)>0}\frac{\left|r-pq\right|}{\sqrt{p(1-p)q(1-q)}}, |  |

where ( X u, Y v) ∼ P X Y | U = u, V = v \left(X_{u},Y_{v}\right)\sim P_{XY|U=u,V=v}, ρ p \rho_{\mathrm{p}} denotes the Pearson correlation coefficient, and ( 16) follows since the maximal correlation coefficient between two binary random variables is equal to the absolute value of the Pearson correlation coefficient between them; see, e.g., Anantharam et al. 2013. So, ρ m ( X; Y | U, V) ≤ ρ \rho_{\mathrm{m}}(X;Y|U,V)\leq\rho is equivalent to | r − p ​ q | p ⁡ ( 1 − p) ​ q ​ ( 1 − q) ≤ ρ \frac{\left|r-pq\right|}{\sqrt{p(1-p)q(1-q)}}\leq\rho a.s., and also equivalent to z 1 ≤ r ≤ z 2 z_{1}\leq r\leq z_{2} a.s.

The inner supremum in ( 14) can be rewritten as

 |  | sup P X ​ Y | U ​ V ∈ 𝒞 s ( P X | U): ρ m ( X; Y | U, V) ≤ ρ H ( Z | U, V) \displaystyle\sup_{P_{XY|UV}\in\mathcal{C}_{\mathrm{s}}(P_{X|U}):\rho_{\mathrm{m}}(X;Y|U,V)\leq\rho}H(Z|U,V) |  |

 |  | = 𝔼 p, q ​ sup max ⁡ { 0, p + q − 1, z 1 } ≤ r ≤ min ⁡ { p, q, z 2 } h ⁡ ( p + q − r). \displaystyle=\mathbb{E}_{p,q}\sup_{\max\{0,p+q-1,z_{1}\}\leq r\leq\min\{p,q,z_{2}\}}h(p+q-r). |  |

By the fact that h h is increasing on [0, 1 / 2] [0,1/2] and decreasing on [1 / 2, 1] [1/2,1], it holds that the optimal r r attaining the supremum in the last line above, denoted by r ∗ r^{*}, is the median of max ⁡ { 0, p + q − 1, z 1 } \max\{0,p+q-1,z_{1}\}, p + q − 1 / 2 p+q-1/2, and min ⁡ { p, q, z 2 } \min\{p,q,z_{2}\}, which implies

 | p + q − r ∗ = φ ⁡ ( ρ, p, q). p+q-r^{*}=\varphi(\rho,p,q). |  |

Recall the definition of φ \varphi in ( 1). So, the inner supremum in ( 14) is equal to 𝔼 p, q ​ h ​ ( φ ⁡ ( ρ, p, q)) 𝔼 ​ h ​ ( p) \frac{\mathbb{E}_{p,q}h(\varphi(\rho,p,q))}{\mathbb{E}h(p)}.

We make following observations. Firstly,

 | H ⁡ ( X | U) \displaystyle H(X|U) | = 𝔼 ​ h ​ ( p), \displaystyle=\mathbb{E}h(p), |  |

 | P X ​ ( 1) \displaystyle P_{X}(1) | = 𝔼 ​ p. \displaystyle=\mathbb{E}p. |  |

Secondly, by the definition of maximal correlation, ρ m ​ ( p, q) ≤ ρ m ​ ( U, V) \rho_{\mathrm{m}}(p;q)\leq\rho_{\mathrm{m}}(U;V) holds (which is known as the data processing inequality) since p, q p,q are respectively functions of U, V U,V; see ( 15). Lastly, observe that P U ​ V P_{UV} is symmetric, and p, q p,q are obtained from U, V U,V via the same function P X | U ( 1 | ⋅) P_{X|U}(1|\cdot) (since P X | U = P Y | V P_{X|U}=P_{Y|V} holds by the symmetry of P X ​ Y | U ​ V P_{XY|UV}). Hence, P p ​ q P_{pq} is symmetric as well. Substituting all of these into ( 14) yields Γ n ​ ( t) ≥ Γ ⁡ ( t) \Gamma_{n}(t)\geq\Gamma(t).

## 4 Proof of Proposition 1

By choosing P ρ = ( 1 − α) ​ δ 0 + α ​ δ 1 P_{\rho}=(1-\alpha)\delta_{0}+\alpha\delta_{1} in ( 2), we obtain

 | Γ ( t) ≥ sup α ∈ [0, 1] inf symmetric ​ P p ​ q: 𝔼 ​ h ​ ( p) > 0, 𝔼 ​ p ≤ t g ⁡ ( P p ​ q, α) 𝔼 ​ h ​ ( p). \Gamma(t)\geq\sup_{\alpha\in[0,1]}\inf_{\textrm{symmetric }P_{pq}:\mathbb{E}h(p)>0,\mathbb{E}p\leq t}\frac{g(P_{pq},\alpha)}{\mathbb{E}h(p)}. |  |

Note that P p ​ q ↦ g ⁡ ( P p ​ q, α) P_{pq}\mapsto g(P_{pq},\alpha) is concave, since by ( Alweiss et al. 2022, Lemma 5), P p ↦ 𝔼 ( p, q) ∼ P p ⊗ 2 ​ h ​ ( p + q − p ​ q) P_{p}\mapsto\mathbb{E}_{(p,q)\sim P_{p}^{\otimes 2}}h(p+q-pq) is concave, and P p ​ q ↦ P p P_{pq}\mapsto P_{p} is linear.

Let B B be a finite subset of [0, 1] [0,1]. Let 𝒫 B \mathcal{P}_{B} be the set of symmetric distributions P p ​ q P_{pq} concentrated on B 2 B^{2} such that 𝔼 ​ p ≤ t \mathbb{E}p\leq t. By the Krein–Milman theorem, 𝒫 B \mathcal{P}_{B} is equal to the closed convex hull of its extreme points. These extreme points are of the form ( 1 − β) ​ Q a 1, a 2 + β ​ Q b 1, b 2 (1-\beta)Q_{a_{1},a_{2}}+\beta Q_{b_{1},b_{2}} with 0 ≤ a ≤ t < b ≤ 1 0\leq a\leq t<b\leq 1 and β = 0 \beta=0 or t − a b − a \frac{t-a}{b-a}, where recall the definitions a:= a 1 + a 2 2, b:= b 1 + b 2 2 a:=\frac{a_{1}+a_{2}}{2},b:=\frac{b_{1}+b_{2}}{2}, and Q x, y:= 1 2 ​ δ ( x, y) + 1 2 ​ δ ( y, x) Q_{x,y}:=\frac{1}{2}\delta_{(x,y)}+\frac{1}{2}\delta_{(y,x)} in ( 6) and ( 7). By Carathéodory’s theorem, it is easy to see that the convex hull of these extreme points is closed (in the weak topology, or equivalently, in the relative topology on the probability simplex). So, every P p ​ q P_{pq} supported on a finite set B 2 ⊆ [0, 1] 2 B^{2}\subseteq[0,1]^{2} such that 𝔼 ​ p ≤ t \mathbb{E}p\leq t is a convex combination of the extreme points above, i.e., P p ​ q = ∑ i = 1 k γ i ​ Q i P_{pq}=\sum_{i=1}^{k}\gamma_{i}Q_{i} where Q i, i ∈ [k] Q_{i},i\in[k] are extreme points, and γ i > 0 \gamma_{i}>0 and ∑ i = 1 k γ i = 1 \sum_{i=1}^{k}\gamma_{i}=1. For this distribution,

 | g ⁡ ( P p ​ q, α) 𝔼 ​ h ​ ( p) \displaystyle\frac{g(P_{pq},\alpha)}{\mathbb{E}h(p)} | = g ⁡ ( ∑ i = 1 k γ i ​ Q i, α) ∑ i = 1 k γ i ​ 𝔼 Q i ​ h ​ ( p) \displaystyle=\frac{g(\sum_{i=1}^{k}\gamma_{i}Q_{i},\alpha)}{\sum_{i=1}^{k}\gamma_{i}\mathbb{E}_{Q_{i}}h(p)} |  |

 |  | ≥ ∑ i = 1 k γ i ​ g ​ ( Q i, α) ∑ i = 1 k γ i ​ 𝔼 Q i ​ h ​ ( p) \displaystyle\geq\frac{\sum_{i=1}^{k}\gamma_{i}g(Q_{i},\alpha)}{\sum_{i=1}^{k}\gamma_{i}\mathbb{E}_{Q_{i}}h(p)} |  |

 |  | ≥ min i: 𝔼 Q i ​ h ​ ( p) > 0 g ⁡ ( Q i, α) 𝔼 Q i ​ h ​ ( p) \displaystyle\geq\min_{i:\mathbb{E}_{Q_{i}}h(p)>0}\frac{g(Q_{i},\alpha)}{\mathbb{E}_{Q_{i}}h(p)} |  |

where in the last line, we use the fact that 𝔼 Q i ​ h ​ ( p) = 0 \mathbb{E}_{Q_{i}}h(p)=0 implies Q i = δ ( 0, 0) Q_{i}=\delta_{(0,0)} (note that t < 1 / 2 t<1/2), and hence, g ⁡ ( Q i, α) = 0 g(Q_{i},\alpha)=0.

Therefore,

 | Γ ( t) ≥ sup α ∈ [0, 1] inf P p ​ q: 𝔼 ​ h ​ ( p) > 0 g ⁡ ( P p ​ q, α) 𝔼 ​ h ​ ( p), \Gamma(t)\geq\sup_{\alpha\in[0,1]}\inf_{P_{pq}:\mathbb{E}h(p)>0}\frac{g(P_{pq},\alpha)}{\mathbb{E}h(p)}, |  | (17) |

where the infimum is taken over distributions P p ​ q P_{pq} of the form ( 1 − β) ​ Q a 1, a 2 + β ​ Q b 1, b 2 (1-\beta)Q_{a_{1},a_{2}}+\beta Q_{b_{1},b_{2}} with 0 ≤ a ≤ t < b ≤ 1 0\leq a\leq t<b\leq 1 and β = 0 \beta=0 or β = t − a b − a > 0 \beta=\frac{t-a}{b-a}>0 such that 𝔼 ​ h ​ ( p) > 0 \mathbb{E}h(p)>0. (Recall the definition of a, b a,b in ( 6).)

## 5 Discussion

The breakthrough made by Gilmer Gilmer 2022 shows the power of information-theoretic techniques in tackling problems from related fields. In fact, the union-closed sets conjecture has a natural interpretation in the information-theoretic (or coding-theoretic) sense. Consider the memoryless OR multi-access channel ( x n, y n) ∈ Ω 2 ​ n ↦ x n ∨ y n ∈ Ω n (x^{n},y^{n})\in\Omega^{2n}\mapsto x^{n}\lor y^{n}\in\Omega^{n}. We would like to find a nonempty code A ⊆ Ω n A\subseteq\Omega^{n} to generate two independent inputs X n, Y n X^{n},Y^{n} with each following Unif ⁡ ( A) \mathrm{Unif}(A) such that the input constraint 𝔼 ⁡ [X i] ≤ t, ∀ i ∈ [n] \mathbb{E}[X_{i}]\leq t,\forall i\in[n] is satisfied and the output X n ∨ Y n X^{n}\lor Y^{n} is still in A A a.s. The union-closed sets conjecture states that such a code exists if and only if t ≥ 1 / 2 t\geq 1/2. Based on this information-theoretic interpretation, it is reasonable to see that the information-theoretic techniques work for this conjecture. It is well-known that information-theoretic techniques usually work very well for problems with “approximate” constraints, e.g., the channel coding problem with the asymptotically vanishing error probability constraint (or the approximate version of the union-closed sets problem introduced in Chase and Lovett 2022). It is hard to say whether information-theoretic techniques are sufficient to prove sharp bounds for problems with “exact” constraints, e.g., the zero-error coding problem (or the original version of the union-closed sets conjecture).

Furthermore, as an intermediate result, it has been shown that Γ n ​ ( t) > 1 \Gamma_{n}(t)>1 implies p A > t p_{A}>t for any OR-closed A ⊆ Ω n A\subseteq\Omega^{n}. Here Γ n ​ ( t) \Gamma_{n}(t) is given in ( 8), expressed in the multi-letter form (i.e., the dimension-dependent form). By the super-block coding argument, it is verified that given t > 0 t>0, lim n → ∞ Γ n ​ ( t) \lim_{n\to\infty}\Gamma_{n}(t) exists. It is interesting to investigate this limit, and prove a single-letter (dimension-independent) expression for it.

For simplicity, in this paper, we only consider the maximal correlation coefficient as the constraint function. In fact, the maximal correlation coefficient used here can be replaced by other functionals. The key property of the maximal correlation coefficient we used in this paper is the “tensorization” property, i.e., ( 10) (in fact, only “ ≤ \leq ” part of ( 10) was used in our proof). In literature, there is a class of measures of correlation satisfying this property, e.g., the hypercontractivity constant, strong data processing inequality constant, or more generally, Φ \Phi -ribbons, see Ahlswede and Gács 1976; Raginsky 2016; Beigi and Gohari 2018. (Although the tensorization property in the literature is only defined and proven for independent random variables, this property can be extended to the coupling constructed in ( 9).) Following the same proof steps given in this paper, one can obtain various variants of Theorem 1 with the maximal correlation coefficient replaced by other quantities, as long as these quantities satisfy the tensorization property. Another potential direction is to replace the Shannon entropy with a class of more general quantities, Rényi entropies. However, unfortunately Rényi entropies do not satisfy the chain rule (unlike the Shannon entropy), which leads to a serious difficulty in single-letterizing the corresponding multi-letter bound like Γ n ​ ( t) \Gamma_{n}(t) in ( 8) (i.e., in making the multi-letter bound dimension-independent).

## Funding

This work was supported by the NSFC grant 62101286 and the Fundamental Research Funds for the Central Universities of China (Nankai University).

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

Not applicable.

The author would like to thank Fan Chang for bringing Gilmer’s breakthrough Gilmer 2022 to his attention, and thank Stijn Cambie for sharing his early draft of Cambie 2022. The author also would like to thank the guest editor, Prof. Igal Sason, for his invitation to submit this paper to the Entropy, and thank him and the anonymous referees for their comments, which led to significant improvements in the presentation of this paper.

## Conflicts of Interest

Not applicable.

## References

- Gilmer [2022] Gilmer, J. A constant lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.09055 2022.
- Sawin [2022] Sawin, W. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504 2022.
- Chase and Lovett [2022] Chase, Z.; Lovett, S. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689 2022.
- Alweiss et al. [2022] Alweiss, R.; Huang, B.; Sellke, M. Improved Lower Bound for the Union-Closed Sets Conjecture. arXiv preprint arXiv:2211.11731 2022.
- Pebody [2022] Pebody, L. Extension of a Method of Gilmer. arXiv preprint arXiv:2211.13139 2022.
- Balla et al. [2013] Balla, I.; Bollobás, B.; Eccles, T. Union-closed families of sets. Journal of Combinatorial Theory, Series A 2013, 120, 531–544.
- Johnson and Vaughan [1998] Johnson, R.T.; Vaughan, T.P. On union-closed families, I. Journal of Combinatorial Theory, Series A 1998, 84, 242–249.
- Karpas [2017] Karpas, I. Two results on union-closed families. arXiv preprint arXiv:1708.01434 2017.
- Knill [1994] Knill, E. Graph generated union-closed families of sets. arXiv preprint math/9409215 1994.
- Wójcik [1999] Wójcik, P. Union-closed families of sets. Discrete Mathematics 1999, 199, 173–182.
- Bruhn and Schaudt [2015] Bruhn, H.; Schaudt, O. The journey of the union-closed sets conjecture. Graphs and Combinatorics 2015, 31, 2043–2074.
- Yu and Tan [2020] Yu, L.; Tan, V.Y.F. On Exact and ∞ \infty -Rényi common information. IEEE Transactions on Information Theory 2020, 66, 3366–3406.
- Yu [2021] Yu, L. Strong Brascamp–Lieb inequalities. ArXiv e-prints, arXiv:2102.06935 2021.
- Yu [2022] Yu, L. Exact Exponents for Concentration and Isoperimetry in Product Polish Spaces. arXiv preprint arXiv:2205.07596 2022.
- Witsenhausen [1975] Witsenhausen, H.S. On sequences of pairs of dependent random variables. SIAM Journal on Applied Mathematics 1975, 28, 100–113.
- Cambie [2022] Cambie, S. Better bounds for the union-closed sets conjecture using the entropy approach. arXiv preprint arXiv:2212.12500 2022.
- Yu [2018] Yu, L. On Conditional Correlations. arXiv preprint arXiv:1811.03918 2018.
- Beigi and Gohari [2015] Beigi, S.; Gohari, A. Monotone measures for non-local correlations. IEEE Transactions on Information Theory 2015, 61, 5185–5208.
- Anantharam et al. [2013] Anantharam, V.; Gohari, A.; Kamath, S.; Nair, C. On maximal correlation, hypercontractivity, and the data processing inequality studied by Erkip and Cover. arXiv preprint arXiv:1304.6133 2013.
- Ahlswede and Gács [1976] Ahlswede, R.; Gács, P. Spreading of sets in product spaces and hypercontraction of the Markov operator. Annals of Probability 1976, pp. 925–939.
- Raginsky [2016] Raginsky, M. Strong data processing inequalities and Φ \Phi -Sobolev inequalities for discrete channels. IEEE Transactions on Information Theory 2016, 62, 3355–3389.
- Beigi and Gohari [2018] Beigi, S.; Gohari, A. Φ \Phi -Entropic Measures of Correlation. IEEE Transactions on Information Theory 2018, 64, 2193–2211.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
