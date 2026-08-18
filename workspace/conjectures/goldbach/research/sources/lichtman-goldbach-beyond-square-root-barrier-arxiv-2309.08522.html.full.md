<!-- source: https://arxiv.org/html/2309.08522v1 | converted from HTML -->

Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root barrier

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2309.08522v1 [math.NT] 30 Aug 2023

# Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root barrier

Jared Duker Lichtman, and appendix with Sary Drappeau Address: I2M, Université d’Aix-Marseille, CNRS, Case 907, Campus de Luminy, 13288 Marseille Cedex 9, France Email address: [sary-aurelien.drappeau@univ-amu.fr][3] Address: Mathematical Institute, University of Oxford, Oxford, OX2 6GG, UK Email address: [jared.d.lichtman@gmail.com][4]

###### Abstract.

We show the primes have level of distribution 66 / 107 ≈ 0.617 66/107\approx 0.617 using triply well-factorable weights. This gives the highest level of distribution for primes in any setting, improving on the prior record level 3 / 5 = 0.60 3/5=0.60 of Maynard. We also extend this level to 5 / 8 = 0.625 5/8=0.625, assuming Selberg’s eigenvalue conjecture. As applications of the method, we obtain new upper bounds for twin primes and for Goldbach representations of even numbers a a. For the Goldbach problem, this is the first use of a level of distribution beyond the ‘square-root barrier’, and leads to the greatest improvement on the problem since Bombieri–Davenport from 1966. Our proof optimizes the Deshouillers–Iwaniec spectral large sieve estimates, both in the exceptional spectrum and uniformity in the residue a a, refining Drappeau–Pratt–Radziwiłł and Assing–Blomer–Li.

###### 2010 Mathematics Subject Classification

Primary 11N35, 11N36; Secondary 11N05

## 1. Introduction

Denote by π 2 ​ ( x) \pi_{2}(x) the number of twin primes p p, p + 2 p+2 up to x x. The twin prime conjecture asserts that π 2 ​ ( x) \pi_{2}(x) diverges as x → ∞ x\to\infty. Also denote by G ⁡ ( a) {\rm G}(a) the number of representations of an even integer a a as a sum of two primes a = p 1 + p 2 a=p_{1}+p_{2}. The Goldbach conjecture asserts that G ⁡ ( a) ⩾ 1 G(a){\,\geqslant}1 for every even a ⩾ 4 a{\,\geqslant}4. These celebrated conjectures were made quantitatively precise by Hardy and Littlewood [21] in 1923, who proposed asymptotic formulae,

(1.1) |  | π 2 ​ ( x) ∼ Π 2 ​ ( x) and G ⁡ ( a) ∼ Π a ​ ( a), \displaystyle\pi_{2}(x)\ \sim\ \Pi_{2}(x)\qquad\text{and}\qquad{\rm G}(a)\ \sim\ \Pi_{a}(a), |  |

where

 | Π a ​ ( x):= 2 ​ 𝔖 a ​ x ( log ⁡ x) 2 and 𝔖 a:= ∏ 2 < p 1 − 2 / p ( 1 − 1 / p) 2 ​ ∏ 2 < p | a 1 − 1 / p 1 − 2 / p. \displaystyle\Pi_{a}(x):=\frac{2\mathfrak{S}_{a}\,x}{(\log x)^{2}}\qquad\text{and}\qquad\mathfrak{S}_{a}:=\prod_{2<p}\frac{1-2/p}{(1-1/p)^{2}}\,\prod_{2<p\mid a}\frac{1-1/p}{1-2/p}. |  |

We prove upper bounds for twin primes and Goldbach representations that are within factors 3.23 and 3.40, respectively, of the predicted Hardy–Littlewood asympototics.

###### Theorem 1.1.

For x ∈ ℝ x\in{\mathbb{R}} sufficiently large, we have π 2 ​ ( x) ≲ 3.2290 ​ Π 2 ​ ( x) \pi_{2}(x)\,\lesssim\,3.2290\,\Pi_{2}(x).

###### Theorem 1.2.

For any even integer a ∈ ℕ a\in{\mathbb{N}} sufficiently large, we have G ⁡ ( a) ≲ 3.3907 ​ Π a ​ ( a) {\rm G}(a)\,\lesssim\,3.3907\,\Pi_{a}(a).

See the table below for a chronology of the known upper bounds on π 2 ​ ( x) \pi_{2}(x) and G ⁡ ( a) {\rm G}(a).

Theorems 1.1 and 1.2 are obtained using refined linear sieve estimates of the author in [25]. To apply such sieve estimates, one must control the remainder terms using equidistribution estimates for primes in arithmetic progressions. Our main proof ingredient is an improved level of distribution for primes, given in Theorem 1.7 below. In particular, Theorem 1.2 uses for the first time a level of distribution beyond the ‘square-root barrier’ for the Goldbach problem.

Year | Author(s) | Twin primes | Goldbach |

 |  | π 2 ​ ( x) / Π 2 ​ ( x) ≲ \pi_{2}(x)/\Pi_{2}(x)\,\lesssim | G ⁡ ( a) / Π a ​ ( a) ≲ {\rm G}(a)/\Pi_{a}(a)\,\lesssim |

1947 | Selberg [32] | 8 | 8 |

1964 | Pan [20] | 6 | 6 |

1966 | Bombieri–Davenport [3] | 4 | 4 |

1978 | Chen [8] | 3.9171 | 3.9171 |

1983 | Fouvry–Iwaniec [15] | 3.7777 ⋯ = 34 / 9 3.7777\cdots=34/9 | — |

1984 | Fouvry [14] | 3.7647 ⋯ = 64 / 17 3.7647\cdots=64/17 | — |

1986 | Bombieri–Friedlander–Iwaniec [4] | 3.5 | — |

1986 | Fouvry–Grupp [16] | 3.454 | — |

1990 | Wu [35] | 3.418 | — |

2003 | Cai–Lu [6] | 3.406 | — |

2004 | Wu [36] | 3.3996 | 3.9104 |

2022 | Lichtman [25] | 3.2996 | — |

In particular, our new bound for G ⁡ ( a) {\rm G}(a) gives a 13.25 % 13.25\% refinement of the prior record of Wu [36] from 2004 (Wu in turn had refined Chen [8] by 0.17 % 0.17\%). This gives the greatest refinement on the problem since Bombieri–Davenport [3] from 1966.

### 1.1. Primes in arithmetic progressions to large moduli

All bounds for G ⁡ ( a) G(a) prior to Theorem 1.1 used the classical Bombieri–Vinogradov theorem from 1965. As usual, we denote by π ⁡ ( x) \pi(x) the number of primes up to x x, and π ⁡ ( x, q, a) \pi(x;q,a) the number of primes up to x x congruent to a ⁡ ( mod ​ q) a\ (\mathrm{mod}\ q). The Bombieri–Vinogradov theorem states that for every ϵ, A > 0 \epsilon,A>0,

(1.2) |  | ∑ q ⩽ x ϑ sup ( a, q) = 1 | π ( x; q, a) − π ⁡ ( x) φ ⁡ ( q) | ≪ A x ( log ⁡ x) A, \displaystyle\sum_{q{\,\leqslant}x^{\vartheta}}\sup_{(a,q)=1}\Big|\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Big|\ \ll_{A}\ \frac{x}{(\log x)^{A}}, |  |

with exponent ϑ < 1 2 \vartheta<\frac{1}{2}, which is often called the ‘level of distribution’ for primes. The estimate ( 1.2) may be viewed as an assertion of the Generalized Riemann Hypothesis on average over moduli up to x ϑ x^{\vartheta}. It remains an important open problem to extend the range in ( 1.2) to ϑ = 1 2 + δ \vartheta=\frac{1}{2}+\delta for some fixed δ > 0 \delta>0. Indeed, Elliott and Halberstam [13] conjectured such an extension up to ϑ = 1 − ϵ \vartheta=1-\epsilon for any ϵ > 0 \epsilon>0.

In contrast to Goldbach representations G ⁡ ( a) {\rm G}(a), there has been comparatively more progress on upper bounding twin primes π 2 ​ ( x) \pi_{2}(x), by leveraging improved level of distribution results in special cases. For example, in case of a fixed nonzero residue a ∈ ℤ a\in{\mathbb{Z}} and ‘well-factorable’ weights λ q ∈ ℂ \lambda_{q}\in{\mathbb{C}} (defined below), Bombieri–Friedlander–Iwaniec [4] proved in 1986 that

(1.3) |  | ∑ q ⩽ x ϑ ( q, a) = 1 λ q ( π ( x; q, a) − π ⁡ ( x) φ ⁡ ( q)) ≪ a, A x ( log ⁡ ( x)) A, \displaystyle\sum_{\begin{subarray}{c}q{\,\leqslant}x^{\vartheta}\\ (q,a)=1\end{subarray}}\lambda_{q}\Bigl(\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Bigr)\ll_{a,A}\frac{x}{(\log{x})^{A}}, |  |

up to level ϑ < 4 7 \vartheta<\frac{4}{7}. They deduced their bound π 2 ​ ( x) ≲ 3.5 ​ Π 2 ​ ( x) \pi_{2}(x)\lesssim 3.5\,\Pi_{2}(x), by choosing the weights in ( 1.3) to be (essentially) the upper bound weights λ q ± \lambda_{q}^{\pm} for the linear sieve. Such weights satisfy the following ‘well-factorable’ property:

###### Definition 1.3 (Well-factorable).

Let Q ∈ ℝ Q\in\mathbb{R}. A sequence λ q ∈ ℂ \lambda_{q}\in{\mathbb{C}} is well-factorable of level Q Q if, for any choice of factorization Q = Q 1 ​ Q 2 Q=Q_{1}Q_{2} with Q 1, Q 2 ⩾ 1 Q_{1},Q_{2}{\,\geqslant}1, there exist 1-bounded sequences γ q 1 ( 1), γ q 2 ( 2) \gamma^{(1)}_{q_{1}},\gamma^{(2)}_{q_{2}}, supported on 1 ⩽ q i ⩽ Q i 1{\,\leqslant}q_{i}{\,\leqslant}Q_{i} for i ∈ { 1, 2 } i\in\{1,2\} such that λ = γ ( 1) ∗ γ ( 2) \lambda=\gamma^{(1)}\ast\gamma^{(2)}, i.e.

 | λ q = ∑ q = q 1 ​ q 2 γ q 1 ( 1) ​ γ q 2 ( 2). \lambda_{q}=\sum_{q=q_{1}q_{2}}\gamma^{(1)}_{q_{1}}\gamma^{(2)}_{q_{2}}. |  |

Heuristically, one may view well-factorability as a property of integers q q in the support { q: λ q ≠ 0 } \{q:\lambda_{q}\neq 0\}: for any splitting Q = Q 1 ​ Q 2 Q=Q_{1}Q_{2}, we may factor q = q 1 ​ q 2 q=q_{1}q_{2} into integers q i ⩽ Q i q_{i}{\,\leqslant}Q_{i}.

For a quarter century, the well-factorable result ( 1.3) constituted the largest level ϑ < 4 7 \vartheta<\frac{4}{7} for primes in arithmetic progressions in any setting. In breakthrough work, Maynard [28] extended ( 1.3) to level ϑ < 3 5 \vartheta<\frac{3}{5}, for λ q \lambda_{q} in the stricter class of ‘triply well-factorable’ weights:

###### Definition 1.4 (Triply well-factorable).

Let Q ∈ ℝ Q\in\mathbb{R}. We say a sequence λ q \lambda_{q} is triply well-factorable of level Q Q if, for any choice of factorization Q = Q 1 ​ Q 2 ​ Q 3 Q=Q_{1}Q_{2}Q_{3} with Q 1, Q 2, Q 3 ⩾ 1 Q_{1},Q_{2},Q_{3}{\,\geqslant}1, there exist 1-bounded sequences γ q 1 ( 1), γ q 2 ( 2), γ q 3 ( 3) \gamma^{(1)}_{q_{1}},\gamma^{(2)}_{q_{2}},\gamma^{(3)}_{q_{3}}, supported on 1 ⩽ q i ⩽ Q i 1{\,\leqslant}q_{i}{\,\leqslant}Q_{i} for i ∈ { 1, 2, 3 } i\in\{1,2,3\}, such that λ = γ ( 1) ∗ γ ( 2) ∗ γ ( 3) \lambda=\gamma^{(1)}\ast\gamma^{(2)}\ast\gamma^{(3)}, i.e.

 | λ q = ∑ q = q 1 ​ q 2 ​ q 3 γ q 1 ( 1) ​ γ q 2 ( 2) ​ γ q 3 ( 3). \lambda_{q}=\sum_{q=q_{1}q_{2}q_{3}}\gamma^{(1)}_{q_{1}}\gamma^{(2)}_{q_{2}}\gamma^{(3)}_{q_{3}}. |  |

Heuristically, one may view triple well-factorability as a property of integers q q the support { q: λ q ≠ 0 } \{q:\lambda_{q}\neq 0\}: for any splitting Q = Q 1 ​ Q 2 ​ Q 3 Q=Q_{1}Q_{2}Q_{3}, we may factor q = q 1 ​ q 2 ​ q 3 q=q_{1}q_{2}q_{3} into integers q i ⩽ Q i q_{i}{\,\leqslant}Q_{i}.

As our main result, we show that primes have level of distribution ϑ < 66 107 ≈ 0.617 \vartheta<\tfrac{66}{107}\approx 0.617 with triply well-factorable weights. This gives the largest level for primes in arithmetic progressions in any setting.

###### Corollary 1.5.

Take nonzero a ∈ ℤ a\in\mathbb{Z} and let A, ϵ > 0 A,\epsilon>0. Let λ q \lambda_{q} be triply well-factorable of level x ϑ x^{\vartheta} with ϑ < 66 107 \vartheta<\tfrac{66}{107}. Then we have

(1.4) |  | ∑ q ⩽ x ϑ ( a, q) = 1 λ q ( π ( x; q, a) − π ⁡ ( x) φ ⁡ ( q)) ≪ a, A, ϵ x ( log ⁡ ( x)) A. \displaystyle\sum_{\begin{subarray}{c}q{\,\leqslant}x^{\vartheta}\\ (a,q)=1\end{subarray}}\lambda_{q}\Bigl(\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Bigr)\ll_{a,A,\epsilon}\frac{x}{(\log{x})^{A}}. |  |

We note that the prior level ϑ < 3 5 \vartheta<\frac{3}{5} has been a natural barrier from works of Bombieri–Friedlander–Iwaniec, Fouvry–Tenenbaum, Drappeau, and Maynard [4, 5, 17, 10, 28].

### 1.2. Exceptional eigenvalues

Our key technical results are given in terms of the best known exponent θ {\theta} towards Selberg’s eigenvalue conjecture. 1 1 1 In this section and hereafter, we denote ϑ {\boldsymbol{\vartheta}} ‘ \ \backslash vartheta’ in bold as the level of distribution for primes, and θ {\theta} ‘ \ \backslash theta’ as the exponent towards Selberg’s eigenvalue conjecture. This is aimed to avoid confusion, while keeping with traditional notation.

###### Definition 1.6.

For q ∈ ℕ q\in{\mathbb{N}}, denote the largest eigenvalue λ 1 = λ 1 ​ ( q) \lambda_{1}=\lambda_{1}(q) of the Laplacian for the congruence subgroup Γ 0 ​ ( q) \Gamma_{0}(q). Define θ q:= max ⁡ ( 0, 1 − 4 ​ λ 1) \theta_{q}:=\max(0,\sqrt{1-4\lambda_{1}}) and θ:= sup q ∈ ℕ θ q {\theta}:=\sup_{q\in{\mathbb{N}}}\theta_{q}. 2 2 2 We use the definition of θ {\theta} as in [9, 10]. However, as a caution, we note some authors’ differ by a factor of 2, e.g. [19, Theorem A] display a bound of 7 64 \frac{7}{64} for | Re μ j, ∞ | ⩽ θ / 2 |\mathop{\rm Re}\mu_{j,\infty}|{\,\leqslant}{\theta}/2.

Selberg’s eigenvalue conjecture asserts that θ = 0 {\theta}=0, namely, λ ⩾ 1 4 \lambda{\,\geqslant}\frac{1}{4} for all eigenvalues λ \lambda of the (hyperbolic) Laplacian for Γ 0 ​ ( q) \Gamma_{0}(q). As such, if λ < 1 4 \lambda<\frac{1}{4} then such an eigenvalue λ \lambda is called *exceptional*. 3 3 3 We elaborate on the role of exceptional eigenvalues in § 9. Corollary 1.5 is a consequence of our main technical result, using the current record bound θ ⩽ 7 32 {\theta}{\,\leqslant}\tfrac{7}{32} of Kim–Sarnak [19, Appendix 2].

###### Theorem 1.7.

Let a ∈ ℤ ≠ 0 a\in\mathbb{Z}_{\neq 0} and A, ϵ > 0 A,\epsilon>0. Let λ q \lambda_{q} be triply well-factorable of level x ϑ x^{{\boldsymbol{\vartheta}}}, with

(1.5) |  | ϑ = 5 − 4 ​ θ 8 − 6 ​ θ − ϵ. \displaystyle{\boldsymbol{\vartheta}}=\frac{5-4{\theta}}{8-6{\theta}}-\epsilon. |  |

Then in the range | a | < x ϵ |a|<x^{\epsilon} we have

(1.6) |  | sup 0 < | a | < x ϵ ∑ q ⩽ x ϑ ( a, q) = 1 λ q ( π ( x; q, a) − π ⁡ ( x) φ ⁡ ( q)) ≪ A, ϵ x ( log ⁡ ( x)) A. \displaystyle\sup_{0<|a|<x^{\epsilon}}\sum_{\begin{subarray}{c}q{\,\leqslant}x^{{\boldsymbol{\vartheta}}}\\ (a,q)=1\end{subarray}}\lambda_{q}\Bigl(\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Bigr)\ll_{A,\epsilon}\frac{x}{(\log{x})^{A}}. |  |

In addition, for ϑ 1 = ( 5 − θ) / 8 − ϵ {\boldsymbol{\vartheta}_{1}}=(5-\theta)/8-\epsilon, in the larger range | a | < x 1 + ϵ |a|<x^{1+\epsilon} we have

(1.7) |  | sup 0 < | a | < x 1 + ϵ ∑ q ⩽ x ϑ 1 ( a, q) = 1 λ q ( π ( x; q, a) − π ⁡ ( x) φ ⁡ ( q)) ≪ A, ϵ x ( log ⁡ ( x)) A. \displaystyle\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}q{\,\leqslant}\,x^{{\boldsymbol{\vartheta}_{1}}}\\ (a,q)=1\end{subarray}}\lambda_{q}\Bigl(\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Bigr)\ll_{A,\epsilon}\frac{x}{(\log{x})^{A}}. |  |

Theorem 1.7 implies Corollary 1.5 with θ = 7 32 {\theta}=\tfrac{7}{32}, extending the level to ϑ < 66 107 ≈ 0.617 {\boldsymbol{\vartheta}}<\tfrac{66}{107}\approx 0.617 beyond ϑ < 3 5 {\boldsymbol{\vartheta}}<\tfrac{3}{5} from Maynard [28]. Using established sieve methods, we input our new level of distribution results for π ⁡ ( x, q, − 2) \pi(x;q,-2) and π ⁡ ( a, q, a) \pi(a;q,a), respectively, to obtain the bounds π 2 ​ ( x) ≲ 3.23 ​ Π 2 ​ ( x) \pi_{2}(x)\,\lesssim\,3.23\Pi_{2}(x) and and G ⁡ ( a) ≲ 3.40 ​ Π a ​ ( a) {\rm G}(a)\,\lesssim\,3.40\,\Pi_{a}(a), in Theorems 1.1 and 1.2.

In particular, all prior bounds on G ⁡ ( a) {\rm G}(a) used level ϑ = 1 2 \boldsymbol{\vartheta}=\frac{1}{2} from the Bombieri–Vinogradov theorem. Now with Theorem 1.7 we obtain level ϑ 1 \boldsymbol{\vartheta}_{1} beyond the ‘square-root barrier’, as large as 153 256 ≈ 0.597 \frac{153}{256}\approx 0.597 with uniformity in the residue | a | < x 1 + ϵ |a|<x^{1+\epsilon}. 4 4 4 As a technical note, for the results uniform in the residue | a | < x 1 + ϵ |a|<x^{1+\epsilon}, we actually need θ \theta for Ramanujan–Petersson, generalizing Selberg eigenvalue. Here the Kim–Sarnak bound θ ⩽ 7 32 \theta{\,\leqslant}\frac{7}{32} still holds. This key ingredient leads to the greatest improvement on bounding G ⁡ ( a) {\rm G}(a) since Bombieri–Davenport [3].

The proof of Theorem 1.7 makes use of a refined estimate for quintilinear forms of Kloosterman sums. Such estimates have a rich history, based on the celebrated work of Deshouillers–Iwaniec [9].

###### Theorem 1.8.

Let C, D, N, R, S ≥ 1 C,D,N,R,S\geq 1, q 0, c 0, d 0 ∈ ℕ q_{0},c_{0},d_{0}\in{\mathbb{N}} with ( c 0 ​ d 0, q 0) = 1 (c_{0}d_{0},q_{0})=1. Let b n, r, s b_{n,r,s} be a sequence supported inside ( 0, N] × ( R, 2 ​ R] × ( S, 2 ​ S] ∩ ℕ 3 (0,N]\times(R,2R]\times(S,2S]\cap{\mathbb{N}}^{3}. Let g: ℝ > 0 5 → ℂ g:{\mathbb{R}}^{5}_{>0}\rightarrow{\mathbb{C}} be a smooth function with compact support in ( C, 2 ​ C] × ( D, 2 ​ D] × ℝ > 0 3 (C,2C]\times(D,2D]\times{\mathbb{R}}_{>0}^{3} such that

 | ∂ ν 1 + ⋯ + ν 5 ∂ c ν 1 ​ ∂ d ν 2 ​ ∂ n ν 3 ​ ∂ r ν 4 ​ ∂ s ν 5 g ( c, d, n, r, s) ≪ ν ( c − ν 1 d − ν 2 n − ν 3 r − ν 4 s − ν 5) 1 − ε 0 \displaystyle\frac{\partial^{\nu_{1}+\cdots+\nu_{5}}}{\partial c^{\nu_{1}}\partial d^{\nu_{2}}\partial n^{\nu_{3}}\partial r^{\nu_{4}}\partial s^{\nu_{5}}}g(c,d,n,r,s)\ll_{{\bf\nu}}(c^{-\nu_{1}}d^{-\nu_{2}}n^{-\nu_{3}}r^{-\nu_{4}}s^{-\nu_{5}})^{1-\varepsilon_{0}} |  |

for all ν ∈ ( ℤ ⩾ 0) 5 {\bf\nu}\in({\mathbb{Z}}_{{\,\geqslant}0})^{5} and some small fixed ε 0 > 0 \varepsilon_{0}>0. Then uniformly for any a ∈ ℤ ≠ 0 a\in{\mathbb{Z}}_{\neq 0}, we have

(1.8) |  | ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ 0 < n ⩽ N b n, r, s ∑ c ≡ c 0 ​ ( mod ​ q 0) d ≡ d 0 ​ ( mod ​ q 0) ( q 0 ​ r ​ d, s ​ c) = 1 g ( c, d, n, r, s) e ( a n r ​ d ¯ s ​ c) ≪ ε, ε 0 ( a q 0 C D N R S) ε + O ⁡ ( ε 0) q 0 3 / 2 𝒥 \displaystyle\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{0<n{\,\leqslant}N}b_{n,r,s}\sum_{\begin{subarray}{c}c\equiv c_{0}\,({\rm mod}\,q_{0})\\ d\equiv d_{0}\,({\rm mod}\,q_{0})\\ (q_{0}rd,sc)=1\end{subarray}}g(c,d,n,r,s)e\Big(an\frac{\overline{rd}}{sc}\Big)\ll_{\varepsilon,\varepsilon_{0}}(aq_{0}CDNRS)^{\varepsilon+O(\varepsilon_{0})}q_{0}^{3/2}\mathcal{J} |  |

where ‖ 𝐛 ‖ 2 = ‖ 𝐛 ~ ​ ( 1) ‖ 2 \|{\bf b}\|_{2}=\|\widetilde{\bf b}(1)\|_{2}, ‖ 𝐛 ~ ​ ( n ′′) ‖ 2 2 = ∑ n, r, s | b n ​ n ′′, r, s | 2 \|\widetilde{\bf b}(n^{\prime\prime})\|_{2}^{2}=\sum_{n,r,s}|b_{nn^{\prime\prime},r,s}|^{2}, and 𝒥 = 𝒥 ⁡ ( a, C, D, N, R, S) \mathcal{J}=\mathcal{J}(a,C,D,N,R,S) is given by

(1.9) |  | 𝒥 2 \displaystyle\mathcal{J}^{2} | = q 0 ​ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ N ( a ​ n ′′) θ ​ ( C ​ S ​ ( N n ′′ + R ​ S) ​ ( C + D ​ R) + a ​ N ​ R ​ S) ​ ‖ 𝐛 ~ ​ ( n ′′) ‖ 2 2 \displaystyle=q_{0}\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2N\end{subarray}}(an^{\prime\prime})^{\theta}\Big(CS\Big(\frac{N}{n^{\prime\prime}}+RS\Big)(C+DR)+aNRS\Big)\|\widetilde{\bf b}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | + ( C ​ S ​ ( C ​ D ​ R) 2 ​ θ ​ ( N + R ​ S) 1 − θ ​ ( C + D ​ R) 1 − 2 ​ θ + D 2 ​ N ​ R) ​ ‖ 𝐛 ‖ 2 2. \displaystyle\quad+\bigg(CS(CD\sqrt{R})^{2{\theta}}(N+RS)^{1-{\theta}}(C+DR)^{1-2{\theta}}+D^{2}NR\bigg)\|{\bf b}\|_{2}^{2}. |  |

A key feature of Theorem 1.8 is the explicit dependence of 𝒥 \mathcal{J} in terms of the exceptional eigenvalue bound θ \theta. Such an approach was initiated by Drappeau [11] and Drappeau–Pratt–Radziwiłł [12]. Theorem 1.8 refines the θ \theta -dependence of [12] in the exceptional spectrum. From private communication, this has since induced the authors to revise [12, Proposition 6] in their published version, which was then applied to prove extended support for one-level density estimates for Dirichlet L-functions. In Appendix A, we show that such θ \theta -dependence is optimal in this context. In particular, we recover that the original argument of Deshoulliers–Iwaniec [9] is optimal when θ = 1 2 \theta=\frac{1}{2}.

We also emphasize the explicit a a -dependence of Theorem 1.8 with the factor of a θ a^{\theta}, following Assing, Blomer, and Li [1] 5 5 5 As mentioned, in [1] Assing–Blomer–Li write a 2 ​ θ a^{2\theta} using different notation for θ \theta. 6 6 6 In applications, the a a -dependence of the term a ​ N ​ R ​ S aNRS in ( 1.9) is often negligible. on a a in 𝒥 ​ ( a, C, D, N, R, S) 2 \mathcal{J}(a,C,D,N,R,S)^{2}. This leads to the uniform estimates in Theorem 1.7, and in turn Theorem 1.2 for the Goldach problem.

As a minor remark, Theorem 1.8 holds for general modulus q 0 q_{0}, following [11], but for our application to Theorem 1.7, we only use q 0 = 1 q_{0}=1. In addition, one should regard the first term n ′′ = 1 n^{\prime\prime}=1 as the main contribution, roughly speaking, and the sum over n ′′ > 1 n^{\prime\prime}>1 as just a technicality. This may be seen heuristically, since the norm ‖ 𝐛 ~ ​ ( n ′′) ‖ 2 2 \|\widetilde{\bf b}(n^{\prime\prime})\|_{2}^{2} decreases with n ′′ n^{\prime\prime}, and the divisor bound handles the sum over n ′′ | a ∞ n^{\prime\prime}\mid a^{\infty}, n ′′ ⩽ 2 ​ N n^{\prime\prime}{\,\leqslant}2N.

## 2. Outline of the proof

In this section, we outline the proof of Theorem 1.7, giving new level of distribution for primes with triply well-factorable weights; we sketch applications to Theorems 1.1 and 1.2 of bounding twin primes and Goldbach respresentations; and we outline the proof of the key input in Theorem 1.8, giving refined estimates for quintilinear forms of Kloosterman sums.

### Proof of Theorem 1.7

The proof is a variant of the approach used to prove Theorem 1.1 in [28], proceeding by the dispersion method. Namely, we use a combinatorial decomposition for the primes (Heath-Brown’s identity) to reduce the problem to estimating certain bilinear sums in arithmetic progressions. By several intermediate manipulations using Poisson summation and Cauchy–Schwarz, this reduces to estimating certain multidimensional exponential sums, which are ultimately bounded using the spectral theory of automorphic forms via the Kuznetsov trace formula. The proof of Maynard in [28, Theorem 1.1] uses well-known bounds of Deshouillers–Iwaniec [9, Theorem 12]. Instead, we apply Theorem 1.8, which gives sharper bounds coming from the exceptional spectrum, and also holds uniformly for all residues a ≠ 0 a\neq 0 in the range | a | < x 1 + ϵ |a|<x^{1+\epsilon}.

For level of distribution with triply well-factorable weights λ q \lambda_{q} we may exploit the additional flexibility of factorizations of the moduli, as observed in [28]. Here we benefit from the fact that now the weights can be factored into three pieces, rather than two in the case of well-factorable weights λ q \lambda_{q} in [4]. Interestingly, there appears to be no further advantage obtained by assuming λ q \lambda_{q} are ‘quadruply well-factorable’ (which can be factored into four pieces).

For example, when a ≪ 1 a\ll 1 (i.e. α = 0 \alpha=0) we prove that any given weights λ q \lambda_{q} satisfy

 | ∑ q ⩽ x ϑ ( a, q) = 1 λ q ​ ( π ⁡ ( x, q, a) − π ⁡ ( x) φ ⁡ ( q)) ≪ x ( log ⁡ ( x)) A, \displaystyle\sum_{\begin{subarray}{c}q{\,\leqslant}x^{{\boldsymbol{\vartheta}}}\\ (a,q)=1\end{subarray}}\lambda_{q}\Bigl(\pi(x;q,a)-\frac{\pi(x)}{{\varphi}(q)}\Bigr)\ll\frac{x}{(\log{x})^{A}}, |  |

provided that (heuristically speaking) all the moduli q q in the support { q: λ q ≠ 0 } \{q:\lambda_{q}\neq 0\} have suitable factorization properties: Namely, for any Q 1 < x 1 / 3 Q_{1}<x^{1/3} there exists a splitting Q = Q 1 ​ Q 2 ​ Q 3 Q=Q_{1}Q_{2}Q_{3} such that the modulus q q factors as q = q 1 ​ q 2 ​ q 3 q=q_{1}q_{2}q_{3} into integers q i ⩽ Q i q_{i}{\,\leqslant}Q_{i} with

 | Q 1 2 ​ Q 2 ​ Q 3 2 \displaystyle Q_{1}^{2}Q_{2}Q_{3}^{2} | < x, \displaystyle\ <\ x, |  |

(2.1) |  | Q 1 2 ​ Q 2 5 ​ Q 3 2 \displaystyle Q_{1}^{2}Q_{2}^{5}Q_{3}^{2} | < x 2, \displaystyle\ <\ x^{2}, |  |

 | ( Q 1 ​ Q 3 / Q 2) 2 ​ θ ​ Q 1 2 ​ Q 2 5 ​ Q 3 2 \displaystyle(Q_{1}Q_{3}/Q_{2})^{2{\theta}}\,Q_{1}^{2}Q_{2}^{5}Q_{3}^{2} | < x 2. \displaystyle\ <\ x^{2}. |  |

In particular, triply-well factorable weights λ q \lambda_{q} will always satisfy these factorization properties: Indeed, for any Q 1 < x 1 / 3 Q_{1}<x^{1/3} we can essentially choose a factorization q = q 1 ​ q 2 ​ q 3 q=q_{1}q_{2}q_{3} into integers q i ⩽ Q i q_{i}{\,\leqslant}Q_{i}, where ( Q 2, Q 3) ≈ ( x 2 ​ ϑ − 1, x 1 − ϑ / Q 1) (Q_{2},Q_{3})\approx(x^{2{\boldsymbol{\vartheta}}-1},\,x^{1-{\boldsymbol{\vartheta}}}/Q_{1}). This choice gives us enough freedom to perfectly balance the contributions coming from diagonal and off-diagonal terms in a wide range. Plugging this in, after a short calculation we find that ( 2) holds up to level ϑ = 5 − 4 ​ θ 8 − 6 ​ θ {\boldsymbol{\vartheta}}=\frac{5-4{\theta}}{8-6{\theta}}, as in Theorem 1.7. Using θ = 7 32 \theta=\frac{7}{32} from Kim–Sarnak [19] this gives ϑ = 66 107 ≈ 0.617 {\boldsymbol{\vartheta}}=\frac{66}{107}\approx 0.617, which improves over the previous record ϑ = 3 5 = 0.60 \boldsymbol{\vartheta}=\frac{3}{5}=0.60 of Maynard [28].

With some additional technicalities, one may similarly handle uniformity in the residue | a | < x α |a|<x^{\alpha} for the range α ⩽ 1 + ϵ \alpha{\,\leqslant}1+\epsilon. This essentially modifies the system ( 2) by an extra factor x α ​ θ x^{\alpha\theta}, given in Lemma 5.1. Proceeding as above one obtains level ϑ = min ⁡ ( 5 − 4 ​ θ 8 − 6 ​ θ, 5 − α ​ θ 8). {\boldsymbol{\vartheta}}=\min\big(\frac{5-4{\theta}}{8-6{\theta}},\,\frac{5-\alpha\theta}{8}\big). See Proposition 3.1.

### Proofs of Theorems 1.1 and 1.2

We apply the improved level of distribution results, used in Theorem 1.7, with the weights λ q ± \lambda_{q}^{\pm} from the linear sieve. 7 7 7 We actually use Iwaniec’s modified linear sieve weights λ ~ q ± \widetilde{\lambda}_{q}^{\pm}, which are not triply well-factorable, but are well-factorable. See § 7.2. However, Theorem 1.7 itself does not directly apply here, since λ q ± \lambda_{q}^{\pm} are not triply well-factorable. Instead, we essentially work with the system ( 2) to obtain increased level of distribution for λ q ± \lambda_{q}^{\pm}. Here the improved level ϑ {\boldsymbol{\vartheta}} will vary, depending on the ‘anatomy’ of an individual modulus q q. That is, heuristically speaking, the level ϑ {\boldsymbol{\vartheta}} will increase proportionally to how close some divisor q 2 | q q_{2}\mid q get to the value q 2 ≈ x 1 − θ 4 − 3 ​ θ q_{2}\approx x^{\frac{1-\theta}{4-3\theta}}. This is made precise in Proposition 6.1 below. Here ϑ {\boldsymbol{\vartheta}} will always be at least 7 12 ≈ 0.583 \frac{7}{12}\approx 0.583 by [28], and may get up to 66 107 ≈ 0.617 \frac{66}{107}\approx 0.617, as in the triply well-factorable case.

We apply our new level of distribution using linear sieve weights, which control the remainder terms in the linear sieve bounds. This increased level is then combined with sieve-theoretic techniques, including the Buchstab identity, the Chen–Iwaniec switching principal, and a recursive argument of Wu [36]. Together, these sieve bounds leads to new results for twin primes and Golbach representations. Specifically, in Theorems 1.1 and 1.2 we obtain π 2 ​ ( x) ≲ 3.23 ​ Π 2 ​ ( x) \pi_{2}(x)\lesssim 3.23\Pi_{2}(x), with residue a = − 2 a=-2 (i.e. α = 0 \alpha=0), and obtain G ⁡ ( a) ≲ 3.40 ​ Π a ​ ( a) {\rm G}(a)\,\lesssim\,3.40\,\Pi_{a}(a) with residue a = x a=x (i.e. α = 1 \alpha=1).

### Proof of Theorem 1.8

The Kuznetsov trace formula translates the quintilinear sums of Kloosterman sums into a spectral expression involving sums

 | ∑ n ∼ N a n ​ ρ j, 1 / s ​ ( a ​ n) \sum_{n\sim N}a_{n}\rho_{j,1/s}(an) |  |

for an arbitrary sequence a n a_{n}, a cusp form f j f_{j} with Fourier coefficients ρ j, 1 / s \rho_{j,1/s} at a cusp 𝔞 = 1 / s \mathfrak{a}=1/s.

Morally, we first wish to ‘factor’ ρ j, 1 / s ​ ( a ​ n) ≈ ρ j, 1 / s ​ ( a) ​ ρ j, 1 / s ​ ( n) \rho_{j,1/s}(an)\approx\rho_{j,1/s}(a)\rho_{j,1/s}(n) and then proceed to apply the spectral large sieve, as in Deshouillers–Iwaniec [9]. This ultimately leads to the bound ρ j, 1 / s ​ ( a) ≪ a θ \rho_{j,1/s}(a)\ll a^{\theta} appearing as the a a -dependence 8 8 8 In this case, a θ a^{\theta} comes from bounding the Hecke eigenvalues at the finite places. As such, it is noteworthy that the Kim–Sarnak bound θ ⩽ 7 32 \theta{\,\leqslant}\frac{7}{32}, towards the Ramanujan–Petersson conjecture, holds equally for the finite places and infinite place. for 𝒥 ​ ( a, C, D, N, R, S) 2 \mathcal{J}(a,C,D,N,R,S)^{2}. However, there are complications to this moral, since the Fourier coefficients ρ j, 1 / s \rho_{j,1/s} are not necessarily multiplicative (much less, completely multiplicative), and moreover, one must take care to separate out the newforms from the oldforms in the spectrum. Such analysis is performed in Assing–Blomer–Li [1], yielding an approximate factorization for ρ j, 1 / s ​ ( a ​ n) \rho_{j,1/s}(an). See Lemma 9.6 below for a precise formulation.

Finally, we establish a refined large sieve estimate for the exceptional spectrum, in terms of the best known bound θ ⩽ 7 32 \theta{\,\leqslant}\frac{7}{32}, from Kim–Sarnak [19]. This extends work of Drappeau–Pratt–Radziwiłł [12] (and induced a revision to be made in their published version). To this, we consider sums over exceptional eigenvalues λ j \lambda_{j} of Γ 0 ​ ( q) \Gamma_{0}(q), on average over the level q ∼ Q q\sim Q, roughly of the form

 | S ⁡ ( Q, N, Y) = ∑ q ∼ Q ∑ λ j < 1 / 4 ( q) Y θ ​ | ∑ n ∼ N a n ​ ρ j ​ ∞ ​ ( n) |. \displaystyle S(Q,N,Y)=\sum_{q\sim Q}\sum_{\lambda_{j}<1/4}^{(q)}Y^{\theta}\Big|\sum_{n\sim N}a_{n}\rho_{j\infty}(n)\Big|. |  |

We adapt the approach in Deshouillers–Iwaniec, which uses a recursive relation between S ⁡ ( Q, N, Y) S(Q,N,Y) and S ⁡ ( N ​ Y / Q, N, Y) S(NY/Q,N,Y) in certain ranges. The main idea is to iteratively apply this recursive relation in steps, interleaved with the spectral large sieve and basic estimates, in a particular order which depends on the relative sizes of the parameters Q Q, N N, and Y Y. This gives bound roughly of the form, for example in Theorem 9.5 with a n = 𝟏 n ∼ N a_{n}={\mathbf{1}}_{n\sim N},

 | S ⁡ ( Q, N, Y) ≪ ( Q ​ N ​ Y) ϵ ​ ( Q + N + ( N ​ Y) θ ​ [N 1 − 2 ​ θ + Q 1 − 2 ​ θ]) ​ N. \displaystyle S(Q,N,Y)\ll(QNY)^{\epsilon}\big(Q+N+(NY)^{\theta}[N^{1-2\theta}+Q^{1-2\theta}]\big)N. |  |

In Appendix A, we prove that such estimates have optimal θ \theta -dependence in this context. In particular, we recover that the original argument of Deshoulliers–Iwaniec [9] is optimal when θ = 1 2 \theta=\frac{1}{2}. To this, we study a heuristic model of the large sieve estimates for the exceptional spectrum. This model is slightly different than the proof, but we feel it better motivates the iterative steps in the original arguments of [9], and explains the shape of the final bound.

## Acknowledgements

The author would like to thank Sary Drappeau, James Maynard, Lasse Grimmelt, Jori Merikoski, Alex Pascadi, and Junxian Li for many helpful discussions. In particular, the author is grateful to Sary Drappeau and Université d’Aix-Marseille for their hospitality, during which a portion of this article was written. The author was supported by Balliol College and the Clarendon Scholarship at the University of Oxford, as well as the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 851318).

## Notation

We will use the Vinogradov ≪ \ll and ≫ \gg asymptotic notation, and the big oh O ⁡ ( ⋅) O(\cdot) and o ⁡ ( ⋅) o(\cdot) asymptotic notation. f ≍ g f\asymp g will denote the conditions f ≪ g f\ll g and g ≪ f g\ll f both hold. We will also use the standard notation f ∼ g f\sim g to denote f = ( 1 + o ⁡ ( 1)) ​ g f=(1+o(1))g, as well as the (non-standard) notation f ≲ g f\lesssim g and f ≳ g f\gtrsim g to denote f ⩽ ( 1 + o ⁡ ( 1)) ​ g f{\,\leqslant}(1+o(1))g and f ⩾ ( 1 + o ⁡ ( 1)) ​ g f{\,\geqslant}(1+o(1))g, respectively. Dependence on a parameter will be denoted by a subscript.

The letter p p will always be reserved to denote a prime number. We use φ {\varphi} to denote the Euler totient function, e ⁡ ( x):= e 2 ​ π ​ i ​ x e(x):=e^{2\pi ix} the complex exponential, τ k ​ ( n) \tau_{k}(n) the k k -fold divisor function, μ ⁡ ( n) \mu(n) the Möbius function. We let P − ​ ( n) P^{-}(n), P + ​ ( n) P^{+}(n) denote the smallest and largest prime factors of n n respectively. We let n | a ∞ n\mid a^{\infty} denote the condition p | n ⟹ p | a p\mid n\implies p\mid a.

We let f ^ \hat{f} denote the Fourier transform of f f over ℝ \mathbb{R} - i.e. f ^ ​ ( ξ) = ∫ − ∞ ∞ f ⁡ ( t) ​ e ​ ( − ξ ​ t) ​ 𝑑 t \hat{f}(\xi)=\int_{-\infty}^{\infty}f(t)e(-\xi t)dt. We use 𝟏 \mathbf{1} to denote the indicator function of a statement. For example,

 | 𝟏 n ≡ a ⁡ ( mod ​ q) = { 1, if ​ n ≡ a ⁡ ( mod ​ q), 0, otherwise. \mathbf{1}_{n\equiv a\ (\mathrm{mod}\ q)}=\begin{cases}1,\qquad&\text{if }n\equiv a\ (\mathrm{mod}\ q),\\ 0,&\text{otherwise}.\end{cases} |  |

For ( n, q) = 1 (n,q)=1, we will use n ¯ \overline{n} to denote the inverse of the integer n n modulo q q; the modulus will be clear from the context. For example, we may write e ⁡ ( a ​ n ¯ / q) e(a\overline{n}/q) - here n ¯ \overline{n} is interpreted as the integer m ∈ { 0, …, q − 1 } m\in\{0,\dots,q-1\} such that m ​ n ≡ 1 ​ ( mod ​ q) mn\equiv 1\ (\mathrm{mod}\ q). Occasionally we will also use λ ¯ \overline{\lambda} to denote complex conjugation; the distinction of the usage should be clear from the context. For a complex sequence α n 1, …, n k \alpha_{n_{1},\dots,n_{k}}, ‖ α ‖ 2 \|\alpha\|_{2} will denote the ℓ 2 \ell^{2} norm ‖ α ‖ 2 = ( ∑ n 1, …, n k | α n 1, …, n k | 2) 1 / 2 \|\alpha\|_{2}=(\sum_{n_{1},\dots,n_{k}}|\alpha_{n_{1},\dots,n_{k}}|^{2})^{1/2}.

Summations assumed to be over all positive integers unless noted otherwise. We use the notation n ∼ N n\sim N to denote the conditions N < n ⩽ 2 ​ N N<n{\,\leqslant}2N.

We will let z 0:= x 1 / ( log ⁡ log ⁡ ( x)) 3 z_{0}:=x^{1/(\log\log{x})^{3}} and y 0:= x 1 / log ⁡ log ⁡ ( x) y_{0}:=x^{1/\log\log{x}} two parameters depending on x x, which we will think of as a large quantity. We will let ψ 0: ℝ → ℝ \psi_{0}:\mathbb{R}\rightarrow\mathbb{R} denote a fixed smooth function supported on [1 / 2, 5 / 2] [1/2,5/2] which is identically equal to 1 1 on the interval [1, 2] [1,2] and satisfies the derivative bounds ‖ ψ 0 ( j) ‖ ∞ ≪ ( 4 j ​ j!) 2 \|\psi_{0}^{(j)}\|_{\infty}\ll(4^{j}j!)^{2} for all j ⩾ 0 j{\,\geqslant}0. (See [5, Page 368, Corollary] for the construction of such a function.)

We will repeatedly make use of the following condition.

###### Definition 2.1 (Siegel-Walfisz condition).

We say that a complex sequence α n \alpha_{n} satisfies the Siegel-Walfisz condition if for every d ⩾ 1 d{\,\geqslant}1, q ⩾ 1 q{\,\geqslant}1 and ( a, q) = 1 (a,q)=1 and every A > 1 A>1 we have

(2.2) |  | | ∑ n ∼ N n ≡ a ⁡ ( mod ​ q) ( n, d) = 1 α n − 1 φ ⁡ ( q) ∑ n ∼ N ( n, d ​ q) = 1 α n | ≪ A N ​ τ ​ ( d) O ⁡ ( 1) ( log ⁡ ( N)) A. \Bigg|\sum_{\begin{subarray}{c}n\sim N\\ n\equiv a\ (\mathrm{mod}\ q)\\ (n,d)=1\end{subarray}}\alpha_{n}-\frac{1}{{\varphi}(q)}\sum_{\begin{subarray}{c}n\sim N\\ (n,dq)=1\end{subarray}}\alpha_{n}\Bigg|\ll_{A}\frac{N\tau(d)^{O(1)}}{(\log{N})^{A}}. |  |

We note that α n \alpha_{n} satisfies the Siegel-Walfisz condition if α n = 1 \alpha_{n}=1, if α n = μ ⁡ ( n) \alpha_{n}=\mu(n), or if α n \alpha_{n} is the indicator function of the primes.

## 3. Level of distribution for primes

In this section we establish Theorem 1.7 assuming two propositions, namely Proposition 3.1 and Proposition 3.2, given below.

###### Proposition 3.1 (Well-factorable Type II estimate).

Let a ∈ ℤ ≠ 0 a\in\mathbb{Z}_{\neq 0}, | a | < x α |a|<x^{\alpha}, N ​ M ≍ x NM\asymp x,

 | x ϵ ⩽ N ⩽ x 1 / 3 + ϵ. x^{\epsilon}{\,\leqslant}N{\,\leqslant}x^{1/3+\epsilon}. |  |

Let λ q \lambda_{q} be triply well-factorable of level Q ⩽ x ϑ Q{\,\leqslant}x^{\boldsymbol{\vartheta}} for

 | ϑ = min ⁡ ( 5 − 4 ​ θ 8 − 6 ​ θ, 5 − α ​ θ 8) − 50 ​ ϵ. {\boldsymbol{\vartheta}}=\min\Big(\frac{5-4{\theta}}{8-6{\theta}},\,\frac{5-\alpha\theta}{8}\Big)-50\epsilon. |  |

Let α n, β m \alpha_{n},\beta_{m} be complex sequences such that | α n |, | β n | ⩽ τ ​ ( n) B 0 |\alpha_{n}|,|\beta_{n}|{\,\leqslant}\tau(n)^{B_{0}} and α n \alpha_{n} satisfies the Siegel-Walfisz condition ( 2.2) and is supported on P − ​ ( n) ⩾ z 0 P^{-}(n){\,\geqslant}z_{0}. Then we have that for every choice of A > 0 A>0 and every interval ℐ ⊆ [x, 2 ​ x] \mathcal{I}\subseteq[x,2x]

 | sup 0 < | a | < x α ∑ q ⩽ Q λ q ∑ n ∼ N α n ∑ m ∼ M m ​ n ∈ ℐ β m ( 𝟏 n ​ m ≡ a ⁡ ( mod ​ q) − 𝟏 ( n ​ m, q) = 1 φ ⁡ ( q)) ≪ A, B 0 x ( log ⁡ ( x)) A. \sup_{0<|a|<x^{\alpha}}\sum_{q{\,\leqslant}Q}\lambda_{q}\sum_{n\sim N}\alpha_{n}\sum_{\begin{subarray}{c}m\sim M\\ mn\in\mathcal{I}\end{subarray}}\beta_{m}\Bigl(\mathbf{1}_{nm\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(nm,q)=1}}{{\varphi}(q)}\Bigr)\ll_{A,B_{0}}\frac{x}{(\log{x})^{A}}. |  |

Proposition 3.1 is our key new ingredient behind the proof, and will be established in Section 5.

###### Proposition 3.2 (Divisor function in progressions).

Let N 1, N 2 ⩾ x 3 ​ ϵ N_{1},N_{2}{\,\geqslant}x^{3\epsilon} and N 1 ​ N 2 ​ M ≍ x N_{1}N_{2}M\asymp x and

 | Q \displaystyle Q | ⩽ ( x M) 2 / 3 − 3 ​ ϵ. \displaystyle{\,\leqslant}\Bigl(\frac{x}{M}\Bigr)^{2/3-3\epsilon}. |  |

Let ℐ ⊂ [x, 2 ​ x] \mathcal{I}\subset[x,2x] be an interval, and let α m \alpha_{m} a complex sequence with | α m | ⩽ τ ​ ( m) B 0 |\alpha_{m}|{\,\leqslant}\tau(m)^{B_{0}}. Then we have that for every A > 0 A>0

 | sup a ≠ 0 ∑ q ∼ Q ( a, q) = 1 | ∑ n 1 ∼ N 1 P − ​ ( n) ⩾ z 0 ∑ n 2 ∼ N 2 P − ​ ( n) ⩾ z 0 ∑ m ∼ M m ​ n 1 ​ n 2 ∈ ℐ α m ( 𝟏 m ​ n 1 ​ n 2 ≡ a ⁡ ( mod ​ q) − 𝟏 ( m ​ n 1 ​ n 2, q) = 1 φ ⁡ ( q)) | ≪ A, B 0 x ( log ⁡ ( x)) A. \sup_{a\neq 0}\sum_{\begin{subarray}{c}q\sim Q\\ (a,q)=1\end{subarray}}\Bigl|\sum_{\begin{subarray}{c}n_{1}\sim N_{1}\\ P^{-}(n){\,\geqslant}z_{0}\end{subarray}}\sum_{\begin{subarray}{c}n_{2}\sim N_{2}\\ P^{-}(n){\,\geqslant}z_{0}\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ mn_{1}n_{2}\in\mathcal{I}\end{subarray}}\alpha_{m}\Bigl(\mathbf{1}_{mn_{1}n_{2}\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(mn_{1}n_{2},q)=1}}{{\varphi}(q)}\Bigr)\Bigr|\ll_{A,B_{0}}\frac{x}{(\log{x})^{A}}. |  |

Moreover, the same result holds when the summand is multiplied by log ⁡ ( n 1) \log{n_1}.

###### Proof.

The proof is given in [28, Proposition 5.2]. This is a quick consequence of the Weil bound (hence admitting the uniformity in the residue, sup a \sup_{a}) and the fundamental lemma of sieves. This is originally due to independent unpublished work of Selberg and Hooley. ∎

Finally, we require a suitable combinatorial decomposition of the primes.

###### Lemma 3.3 (Heath-Brown identity).

Let k ⩾ 1 k{\,\geqslant}1 and n ⩽ 2 ​ x n{\,\leqslant}2x. Then we have

 | Λ ( n) = ∑ j = 1 k ( − 1) j ( k j) ∑ n = n 1 ⋯ n j m 1 ⋯ m j m 1, …, m j ⩽ 2 ​ x 1 / k μ ( m 1) ⋯ μ ( m j) log ⁡ ( n 1). \Lambda(n)=\sum_{j=1}^{k}(-1)^{j}\binom{k}{j}\sum_{\begin{subarray}{c}n=n_{1}\cdots n_{j}m_{1}\cdots m_{j}\\ m_{1},\dots,m_{j}{\,\leqslant}2x^{1/k}\end{subarray}}\mu(m_{1})\cdots\mu(m_{j})\log{n_{1}}. |  |

###### Proof.

See [22]. ∎

###### Lemma 3.4 (Consequence of the fundamental lemma of the sieve).

Let q, t, x ⩾ 2 q,t,x{\,\geqslant}2 satisfy q ​ x ϵ ⩽ t qx^{\epsilon}{\,\leqslant}t and let ( b, q) = 1 (b,q)=1. Recall z 0 = x 1 / ( log ⁡ log ⁡ ( x)) 3 z_{0}=x^{1/(\log\log{x})^{3}}. Then we have

 | ∑ n ⩽ t n ≡ b ⁡ ( mod ​ q) P − ​ ( n) ⩾ z 0 1 = 1 φ ⁡ ( q) ​ ∑ n ⩽ t P − ​ ( n) ⩾ z 0 1 + O A ​ ( t q ​ ( log ⁡ ( x)) A). \sum_{\begin{subarray}{c}n{\,\leqslant}t\\ n\equiv b\ (\mathrm{mod}\ q)\\ P^{-}(n){\,\geqslant}z_{0}\end{subarray}}1=\frac{1}{{\varphi}(q)}\sum_{\begin{subarray}{c}n{\,\leqslant}t\\ P^{-}(n){\,\geqslant}z_{0}\end{subarray}}1+O_{A}\Bigl(\frac{t}{q(\log{x})^{A}}\Bigr). |  |

###### Proof.

This is an immediate consequence of the fundamental lemma of sieve methods - see, for example, [18, Theorem 6.12]. ∎

###### Proof of Theorem 1.7 assuming Proposition 3.1 and 3.2.

By partial summation (noting that prime powers contribute negligibly and retaining the conditon P − ​ ( n) ⩾ z 0 P^{-}(n){\,\geqslant}z_{0}), it suffices to show that for all t ∈ [x, 2 ​ x] t\in[x,2x]

 | sup 0 < | a | < x α ∑ q ⩽ x ϑ λ q ∑ x ⩽ n ⩽ t P − ​ ( n) ⩾ z 0 Λ ( n) ( 𝟏 n ≡ a ⁡ ( mod ​ q) − 𝟏 ( n, q) = 1 φ ⁡ ( q)) ≪ A x ( log ⁡ ( x)) A. \sup_{0<|a|<x^{\alpha}}\sum_{q{\,\leqslant}x^{\boldsymbol{\vartheta}}}\lambda_{q}\sum_{\begin{subarray}{c}x{\,\leqslant}n{\,\leqslant}t\\ P^{-}(n){\,\geqslant}z_{0}\end{subarray}}\Lambda(n)\Bigl(\mathbf{1}_{n\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(n,q)=1}}{{\varphi}(q)}\Bigr)\ll_{A}\frac{x}{(\log{x})^{A}}. |  |

We now apply Lemma 3.3 with k = 3 k=3 to expand Λ ⁡ ( n) \Lambda(n) into various subsums, and put each variable into one of O ⁡ ( log 6 ​ x) O(\log^{6}{x}) dyadic intervals. Thus it suffices to show that for all choices of N 1, N 2, N 3, M 1, M 2, M 3 N_{1},N_{2},N_{3},M_{1},M_{2},M_{3} with M 1 ​ M 2 ​ M 3 ​ N 1 ​ N 2 ​ N 3 ≍ x M_{1}M_{2}M_{3}N_{1}N_{2}N_{3}\asymp x and M i ⩽ x 1 / 3 M_{i}{\,\leqslant}x^{1/3} we have

 | sup 0 < | a | < x α ∑ q ⩽ x ϑ λ q ​ ∑ m 1, m 2, m 3, n 1, n 2, n 3 n i ∼ N i ​ ∀ i m i ∼ M i ​ ∀ i x ⩽ n ⩽ t P − ​ ( n i), P − ​ ( m i) ⩾ z 0 ​ ∀ i μ ⁡ ( m 1) ​ μ ​ ( m 2) ​ μ ​ ( m 3) ​ ( log ⁡ ( n 1)) ​ ( 𝟏 n ≡ a ⁡ ( mod ​ q) − 𝟏 ( n, q) = 1 φ ⁡ ( q)) \displaystyle\sup_{0<|a|<x^{\alpha}}\sum_{q{\,\leqslant}x^{\boldsymbol{\vartheta}}}\lambda_{q}\sum_{\begin{subarray}{c}m_{1},m_{2},m_{3},n_{1},n_{2},n_{3}\\ n_{i}\sim N_{i}\,\forall i\\ m_{i}\sim M_{i}\,\forall i\\ x{\,\leqslant}n{\,\leqslant}t\\ P^{-}(n_{i}),P^{-}(m_{i}){\,\geqslant}z_{0}\,\forall i\end{subarray}}\mu(m_{1})\mu(m_{2})\mu(m_{3})(\log{n_1})\Bigl(\mathbf{1}_{n\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(n,q)=1}}{{\varphi}(q)}\Bigr) |  |

 | ≪ A x ( log ⁡ ( x)) A + 6, \displaystyle\ll_{A}\frac{x}{(\log{x})^{A+6}}, |  |

where we have written n = n 1 ​ n 2 ​ n 3 ​ m 1 ​ m 2 ​ m 3 n=n_{1}n_{2}n_{3}m_{1}m_{2}m_{3} in the expression above for convenience.

By grouping all but one variable together, Proposition 3.1 gives this if any of the N i N_{i} or M i M_{i} lie in the interval [x ϵ, x 1 / 3 + ϵ] [x^{\epsilon},x^{1/3+\epsilon}], and so we may assume all are either smaller than x ϵ x^{\epsilon} or larger than x 1 / 3 + ϵ x^{1/3+\epsilon}. Since M i ⩽ x 1 / 3 M_{i}{\,\leqslant}x^{1/3}, we may assume that M 1, M 2, M 3 ⩽ x ϵ M_{1},M_{2},M_{3}{\,\leqslant}x^{\epsilon}. There can be at most two of the N i N_{i} ’s which are larger than x 1 / 3 + ϵ x^{1/3+\epsilon} since M 1 ​ M 2 ​ M 3 ​ N 1 ​ N 2 ​ N 3 ≍ x M_{1}M_{2}M_{3}N_{1}N_{2}N_{3}\asymp x.

If only one of the N i N_{i} ’s are greater than x 1 / 3 + ϵ x^{1/3+\epsilon} then they must be of size ≫ x 1 − 5 ​ ϵ > x ϵ ​ q \gg x^{1-5\epsilon}>x^{\epsilon}q, and so the result is trivial by summing over this variable first and using Lemma 3.4.

If two of the N i N_{i} ’s are greater, say N 1, N 2 > x 1 / 3 + ϵ N_{1},N_{2}>x^{1/3+\epsilon}, and all the other variables are less than x ϵ x^{\epsilon}, then the result follows from Proposition 3.2 with M = M 1 ​ M 2 ​ M 3 ​ N 3 ⩽ x 4 ​ ϵ M=M_{1}M_{2}M_{3}N_{3}{\,\leqslant}x^{4\epsilon}, since Q ⩽ x 5 / 8 ⩽ ( x / M) 2 / 3 − 3 ​ ϵ Q{\,\leqslant}x^{5/8}{\,\leqslant}(x/M)^{2/3-3\epsilon}. This gives the result. ∎

To complete the proof of Theorem 1.7, we are left to establish Proposition 3.1, which we will do in Section 5.

## 4. Preliminary dispersion method lemmas

In this section, we collect preliminary lemmas that will be used in the dispersion method.

###### Lemma 4.1 (Divisor function bounds).

Let | b | < x − y |b|<x-y and y ⩾ q ​ x ϵ y{\,\geqslant}qx^{\epsilon}. Then we have

 | sup a ≠ 0 ∑ x − y ⩽ n ⩽ x n ≡ a ⁡ ( mod ​ q) τ ​ ( n) C ​ τ ​ ( n − b) C ≪ y q ​ ( τ ⁡ ( q) ​ log ⁡ ( x)) O C ​ ( 1). \sup_{a\neq 0}\sum_{\begin{subarray}{c}x-y{\,\leqslant}n{\,\leqslant}x\\ n\equiv a\ (\mathrm{mod}\ q)\end{subarray}}\tau(n)^{C}\tau(n-b)^{C}\ll\frac{y}{q}(\tau(q)\log{x})^{O_{C}(1)}. |  |

###### Proof.

This follows from Shiu’s Theorem [33], and is given in [27, Lemma 8.7]. ∎

###### Lemma 4.2 (Separation of variables from inequalities).

Let 𝒬 ⊂ [x ϵ, x 1 − ϵ] \mathcal{Q}\subset[x^{\epsilon},x^{1-\epsilon}]. Let N 1, …, N r ⩾ z 0 N_{1},\dots,N_{r}{\,\geqslant}z_{0} satisfy N 1 ⋯ N r ≍ x N_{1}\cdots N_{r}\asymp x. Let α n 1, …, n r \alpha_{n_{1},\dots,n_{r}} be a complex sequence with | α n 1, …, n r | ⩽ ( τ ( n 1) ⋯ τ ( n r)) B 0 |\alpha_{n_{1},\dots,n_{r}}|{\,\leqslant}(\tau(n_{1})\cdots\tau(n_{r}))^{B_{0}}. Then, for any choice of A > 0 A>0 there is a constant C = C ⁡ ( A, B 0, r) C=C(A,B_{0},r) and intervals ℐ 1, …, ℐ r \mathcal{I}_{1},\dots,\mathcal{I}_{r} with ℐ j ⊆ [P j, 2 ​ P j] \mathcal{I}_{j}\subseteq[P_{j},2P_{j}] of length ⩽ P j ​ ( log ⁡ ( x)) − C {\,\leqslant}P_{j}(\log{x})^{-C} such that

 | sup a ≠ 0 ∑ q ∈ 𝒬 ( q, a) = 1 \displaystyle\sup_{a\neq 0}\sum_{\begin{subarray}{c}q\in\mathcal{Q}\\ (q,a)=1\end{subarray}} | | ∑ ∗ n 1, …, n r n i ∼ N i ​ ∀ i ∗ α n 1, …, n r ( 𝟏 n 1 ⋯ n r ≡ a ( mod q) − 𝟏 ( n 1 ⋯ n r, q) = 1 φ ⁡ ( q)) | \displaystyle\Bigl|\,\sideset{}{{}^{*}}{\sum}_{\begin{subarray}{c}n_{1},\dots,n_{r}\\ n_{i}\sim N_{i}\forall i\end{subarray}}\alpha_{n_{1},\dots,n_{r}}\Bigl(\mathbf{1}_{n_{1}\cdots n_{r}\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(n_{1}\cdots n_{r},q)=1}}{{\varphi}(q)}\Bigr)\Bigr| |  |

 |  | ≪ r x ( log ⁡ ( x)) A + ( log ⁡ ( x)) r ​ C sup a ≠ 0 ∑ q ∈ 𝒬 ( q, a) = 1 | ∑ n 1, …, n r n i ∈ ℐ i ​ ∀ i α n 1, …, n r ( 𝟏 n 1 ⋯ n r ≡ a ( mod q) − 𝟏 ( n 1 ⋯ n r, q) = 1 φ ⁡ ( q)) |. \displaystyle\ll_{r}\ \frac{x}{(\log{x})^{A}}+(\log{x})^{rC}\sup_{a\neq 0}\sum_{\begin{subarray}{c}q\in\mathcal{Q}\\ (q,a)=1\end{subarray}}\Bigl|\sum_{\begin{subarray}{c}n_{1},\dots,n_{r}\\ n_{i}\in\mathcal{I}_{i}\forall i\end{subarray}}\alpha_{n_{1},\dots,n_{r}}\Bigl(\mathbf{1}_{n_{1}\cdots n_{r}\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(n_{1}\cdots n_{r},q)=1}}{{\varphi}(q)}\Bigr)\Bigr|. |  |

Here ∑ ∗ \sum^{*} means that the summation is restricted to O ⁡ ( 1) O(1) inequalities of the form n 1 α 1 ⋯ n r α r ⩽ B n_{1}^{\alpha_{1}}\cdots n_{r}^{\alpha_{r}}{\,\leqslant}B for some constants α 1, … ​ α r \alpha_{1},\dots\alpha_{r} and some quantity B B. The implied constant may depend on all such exponents α i \alpha_{i}, but none of the quantities B B.

###### Proof.

This is [27, Lemma 8.10], noting that the argument is uniform in the residue a a. ∎

###### Lemma 4.3.

Let C, B > 0 C,B>0 be constants and let α n \alpha_{n} be a sequence satisfing the Siegel-Walfisz condition ( 2.2), supported on n ⩽ 2 ​ x n{\,\leqslant}2x with P − ​ ( n) ⩾ z 0 = x 1 / ( log ⁡ log ⁡ ( x)) 3 P^{-}(n){\,\geqslant}z_{0}=x^{1/(\log\log{x})^{3}} and satisfying | α n | ⩽ τ ​ ( n) B |\alpha_{n}|{\,\leqslant}\tau(n)^{B}. Then 𝟏 τ ⁡ ( n) ⩽ ( log ⁡ ( x)) C ​ α n \mathbf{1}_{\tau(n){\,\leqslant}(\log{x})^{C}}\alpha_{n} also satisfies the Siegel-Walfisz condition.

###### Proof.

This is [27, Lemma 13.7]. ∎

###### Lemma 4.4 (Most moduli have small smooth part).

Let Q < x 1 − ϵ Q<x^{1-\epsilon} and A, B > 0 A,B>0. Let γ b \gamma_{b} be a complex sequence with | γ b | ⩽ τ ​ ( n) B |\gamma_{b}|{\,\leqslant}\tau(n)^{B} and set z 0:= x 1 / ( log ⁡ log ⁡ ( x)) 3 z_{0}:=x^{1/(\log\log{x})^{3}} and y 0:= x 1 / log ⁡ log ⁡ ( x) y_{0}:=x^{1/\log\log{x}}. Let s ​ m ​ ( n, z) sm(n;z) denote the z z -smooth part of n n. (i.e. s ​ m ​ ( n, z) = ∏ p ⩽ z p ν p ​ ( n) sm(n;z)=\prod_{p{\,\leqslant}z}p^{\nu_{p}(n)}). Then we have that

 | ∑ q ∼ Q s ​ m ​ ( q, z 0) ⩾ y 0 sup ( a, q) = 1 | ∑ b ⩽ x γ b ( 𝟏 b ≡ a ⁡ ( mod ​ q) − 𝟏 ( b, q) = 1 φ ⁡ ( q)) | ≪ A, B x ( log ⁡ ( x)) A. \sum_{\begin{subarray}{c}q\sim Q\\ sm(q;z_{0}){\,\geqslant}y_{0}\end{subarray}}\sup_{(a,q)=1}\Bigl|\sum_{b{\,\leqslant}x}\gamma_{b}\Bigl(\mathbf{1}_{b\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(b,q)=1}}{{\varphi}(q)}\Bigr)\Bigr|\ll_{A,B}\frac{x}{(\log{x})^{A}}. |  |

###### Proof.

This is [29, Lemma 10.11]. ∎

###### Proposition 4.5 (Reduction to exponential sums).

Let α n, β m, γ q, d, λ q, d, r \alpha_{n},\beta_{m},\gamma_{q,d},\lambda_{q,d,r} be complex sequences with | α n |, | β n | ⩽ τ ​ ( n) B 0 |\alpha_{n}|,|\beta_{n}|{\,\leqslant}\tau(n)^{B_{0}} and | γ q, d | ⩽ τ ​ ( q ​ d) B 0 |\gamma_{q,d}|{\,\leqslant}\tau(qd)^{B_{0}} and | λ q, d, r | ⩽ τ ​ ( q ​ d ​ r) B 0 |\lambda_{q,d,r}|{\,\leqslant}\tau(qdr)^{B_{0}}. Let α n \alpha_{n} and λ q, d, r \lambda_{q,d,r} be supported on integers with P − ​ ( n) ⩾ z 0 P^{-}(n){\,\geqslant}z_{0} and P − ​ ( r) ⩾ z 0 P^{-}(r){\,\geqslant}z_{0}, and let α n \alpha_{n} satisfy the Siegel-Walfisz condition ( 2.2). Let

 | 𝒮:= sup 0 < | a | < x 1 + ϵ ∑ d ∼ D ( d, a) = 1 ∑ q ∼ Q ( q, a) = 1 ∑ r ∼ R ( r, a) = 1 λ q, d, r ​ γ q, d ​ ∑ m ∼ M β m ​ ∑ n ∼ N α n ​ ( 𝟏 m ​ n ≡ a ⁡ ( mod ​ q ​ r ​ d) − 𝟏 ( m ​ n, q ​ r ​ d) = 1 φ ⁡ ( q ​ r ​ d)). \mathcal{S}:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}q\sim Q\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r\sim R\\ (r,a)=1\end{subarray}}\lambda_{q,d,r}\gamma_{q,d}\sum_{m\sim M}\beta_{m}\sum_{n\sim N}\alpha_{n}\Bigl(\mathbf{1}_{mn\equiv a\ (\mathrm{mod}\ qrd)}-\frac{\mathbf{1}_{(mn,qrd)=1}}{{\varphi}(qrd)}\Bigr). |  |

Let A > 0 A>0 and C = C ⁡ ( A, B 0) C=C(A,B_{0}) be sufficiently large in terms of A, B 0 A,B_{0}, and let N, M N,M satisfy

 | N > Q ​ D ​ ( log ⁡ ( x)) C, M > ( log ⁡ ( x)) C. N>QD(\log{x})^{C},\qquad M>(\log{x})^{C}. |  |

Then we have

 | | 𝒮 | ≪ A, B 0 x ( log ⁡ ( x)) A + M D 1 / 2 Q 1 / 2 ( log ⁡ ( x)) O B 0 ​ ( 1) ( | ℰ 1 | 1 / 2 + | ℰ 2 | 1 / 2), |\mathcal{S}|\ll_{A,B_{0}}\frac{x}{(\log{x})^{A}}+MD^{1/2}Q^{1/2}(\log{x})^{O_{B_{0}}(1)}\Bigl(|\mathcal{E}_{1}|^{1/2}+|\mathcal{E}_{2}|^{1/2}\Bigr), |  |

where

 | ℰ 1 \displaystyle\mathcal{E}_{1} | : = sup 0 < | a | < x 1 + ϵ ∑ q ( q, a) = 1 ∑ d ∼ D ( d, a) = 1 ∑ r 1, r 2 ∼ R ( r 1 ​ r 2, a) = 1 ψ 0 ​ ( q Q) ​ λ q, d, r 1 ​ λ q, d, r 2 ¯ φ ⁡ ( q ​ d ​ r 2) ​ q ​ d ​ r 1 ​ ∑ n 1, n 2 ∼ N ( n 1, q ​ d ​ r 1) = 1 ( n 2, q ​ d ​ r 2) = 1 α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}q\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1}r_{2},a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q}\Bigr)\frac{\lambda_{q,d,r_{1}}\overline{\lambda_{q,d,r_{2}}}}{{\varphi}(qdr_{2})qdr_{1}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ (n_{1},qdr_{1})=1\\ (n_{2},qdr_{2})=1\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H 1 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1) ​ e ​ ( a ​ h ​ n 1 ¯ q ​ d ​ r 1), \displaystyle\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{1}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}}}{qdr_{1}}\Bigr), |  |

 | ℰ 2 \displaystyle\mathcal{E}_{2} | : = sup 0 < | a | < x 1 + ϵ ∑ q ( q, a) = 1 ψ 0 ​ ( q Q) ​ ∑ d ∼ D ( d, a) = 1 ∑ r 1, r 2 ∼ R ( r 1, a ​ r 2) = 1 ( r 2, a ​ q ​ d ​ r 1) = 1 λ q, d, r 1 ​ λ q, d, r 2 ¯ q ​ d ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q ​ d) ( n 1, n 2 ​ q ​ d ​ r 1) = 1 ( n 2, n 1 ​ q ​ d ​ r 2) = 1 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}q\\ (q,a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q}\Bigr)\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1},ar_{2})=1\\ (r_{2},aqdr_{1})=1\end{subarray}}\frac{\lambda_{q,d,r_{1}}\overline{\lambda_{q,d,r_{2}}}}{qdr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd)\\ (n_{1},n_{2}qdr_{1})=1\\ (n_{2},n_{1}qdr_{2})=1\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H 2 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1 ​ r 2) ​ e ​ ( a ​ h ​ n 1 ​ r 2 ¯ q ​ d ​ r 1 + a ​ h ​ n 2 ​ q ​ d ​ r 1 ¯ r 2), \displaystyle\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{2}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}r_{2}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}r_{2}}}{qdr_{1}}+\frac{ah\overline{n_{2}qdr_{1}}}{r_{2}}\Bigr), |  |

 | H 1 \displaystyle H_{1} | : = Q ​ D ​ R M ​ log 5 ​ x, \displaystyle:=\frac{QDR}{M}\log^{5}{x}, |  |

 | H 2 \displaystyle H_{2} | : = Q ​ D ​ R 2 M ​ log 5 ​ x. \displaystyle:=\frac{QDR^{2}}{M}\log^{5}{x}. |  |

###### Proof.

This is [27, Proposition 14.4] with E = 1 E=1. The argument is uniform in the residue class a a (moreso than we need). ∎

The following lemma imposes the uniformity constraint | a | < x 1 + ϵ |a|<x^{1+\epsilon}.

###### Lemma 4.6 (Simplification of exponential sum).

Let N, M, Q, R ⩽ x N,M,Q,R{\,\leqslant}x with N ​ M ≍ x NM\asymp x and

(4.1) |  | Q ​ R \displaystyle QR | < x 2 / 3, \displaystyle<x^{2/3}, |  |

(4.2) |  | Q ​ R 2 \displaystyle QR^{2} | < M ​ x 1 − 3 ​ ϵ. \displaystyle<Mx^{1-3\epsilon}. |  |

Let λ q, r \lambda_{q,r} and α n \alpha_{n} be complex sequences supported on P − ​ ( n), P − ​ ( r) ⩾ z 0 P^{-}(n),P^{-}(r){\,\geqslant}z_{0} with | λ q, r | ⩽ τ ​ ( q ​ r) B 0 |\lambda_{q,r}|{\,\leqslant}\tau(qr)^{B_{0}} and | α n | ⩽ τ ​ ( n) B 0 |\alpha_{n}|{\,\leqslant}\tau(n)^{B_{0}}. Let H:= Q ​ R 2 M ​ log 5 ​ x H:=\frac{QR^{2}}{M}\log^{5}{x} and let

 | ℰ \displaystyle\mathcal{E} | : = sup 0 < | a | < x 1 + ϵ ∑ ( q, a) = 1 ψ 0 ​ ( q Q) ​ ∑ r 1, r 2 ∼ R ( r 1, a ​ r 2) = 1 ( r 2, a ​ q ​ r 2) = 1 λ q, r 1 ​ λ q, r 2 ¯ q ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q) ( n 1, n 2 ​ q ​ r 1) = 1 ( n 2, n 1 ​ q ​ r 2) = 1 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}(q,a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q}\Bigr)\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1},ar_{2})=1\\ (r_{2},aqr_{2})=1\end{subarray}}\frac{\lambda_{q,r_{1}}\overline{\lambda_{q,r_{2}}}}{qr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ q)\\ (n_{1},n_{2}qr_{1})=1\\ (n_{2},n_{1}qr_{2})=1\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H ψ ^ 0 ​ ( h ​ M q ​ r 1 ​ r 2) ​ e ​ ( a ​ h ​ n 1 ​ r 2 ¯ q ​ r 1 + a ​ h ​ n 2 ​ q ​ r 1 ¯ r 2). \displaystyle\qquad\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H}\hat{\psi}_{0}\Bigl(\frac{hM}{qr_{1}r_{2}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}r_{2}}}{qr_{1}}+\frac{ah\overline{n_{2}qr_{1}}}{r_{2}}\Bigr). |  |

Then we have (uniformly in C C)

 | ℰ ≪ B 0 exp ⁡ ( ( log ⁡ log ⁡ ( x)) 5) sup 0 < | a | < x 1 + ϵ R 1, R 2 ⩽ 2 ​ R sup H ′ ⩽ H Q ′ ⩽ 2 ​ Q | ℰ ′ | + N 2 Q ​ x ϵ, \mathcal{E}\ll_{B_{0}}\exp((\log\log{x})^5)\sup_{\begin{subarray}{c}0<|a|<x^{1+\epsilon}\\ R_{1},R_{2}{\,\leqslant}2R\end{subarray}}\sup_{\begin{subarray}{c}H^{\prime}{\,\leqslant}H\\ Q^{\prime}{\,\leqslant}2Q\end{subarray}}|\mathcal{E}^{\prime}|+\frac{N^{2}}{Qx^{\epsilon}}, |  |

where

 | ℰ ′ = ∑ Q ⩽ q ⩽ Q ′ ( q, a) = 1 ∑ R ⩽ r 1 ⩽ R 1 R ⩽ r 2 ⩽ R 2 ( r 1 ​ a ​ r 2) = 1 ( r 2, a ​ q ​ r 1) = 1 λ q, r 1 ​ λ q, r 2 ¯ q ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q) ( n 1, q ​ r 1 ​ n 2) = 1 ( n 2, q ​ r 2 ​ n 1) = 1 ( n 1 ​ r 2, n 2) ∈ 𝒩 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ ​ ∑ 1 ⩽ | h | ⩽ H ′ e ⁡ ( a ​ h ​ n 2 ​ q ​ r 1 ¯ ​ ( n 1 − n 2) n 1 ​ r 2), \mathcal{E}^{\prime}=\sum_{\begin{subarray}{c}Q{\,\leqslant}q{\,\leqslant}Q^{\prime}\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}R{\,\leqslant}r_{1}{\,\leqslant}R_{1}\\ R{\,\leqslant}r_{2}{\,\leqslant}R_{2}\\ (r_{1}ar_{2})=1\\ (r_{2},aqr_{1})=1\end{subarray}}\frac{\lambda_{q,r_{1}}\overline{\lambda_{q,r_{2}}}}{qr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ q)\\ (n_{1},qr_{1}n_{2})=1\\ (n_{2},qr_{2}n_{1})=1\\ (n_{1}r_{2},n_{2})\in\mathcal{N}\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}}\sum_{1{\,\leqslant}|h|{\,\leqslant}H^{\prime}}e\Bigl(\frac{ah\overline{n_{2}qr_{1}}(n_{1}-n_{2})}{n_{1}r_{2}}\Bigr), |  |

and 𝒩 \mathcal{N} is a set with the property that if ( a, b) ∈ 𝒩 (a,b)\in\mathcal{N} and ( a ′, b ′) ∈ 𝒩 (a^{\prime},b^{\prime})\in\mathcal{N} then we have gcd ⁡ ( a, b ′) = gcd ⁡ ( a ′, b) = 1 \gcd(a,b^{\prime})=\gcd(a^{\prime},b)=1.

###### Proof.

This follows as in [27, Lemma 14.5]. The only minor modification to the proof needed to obtain uniformity in a a is in the application of Bezout’s identity. We provide this for completeness: Indeed, by Bezout’s identity,

 | a ​ h ​ n 1 ​ r 2 ¯ q ​ r 1 \displaystyle\frac{ah\overline{n_{1}r_{2}}}{qr_{1}} | = − a ​ h ​ q ​ r 1 ¯ n 1 ​ r 2 + a ​ h q ​ r 1 ​ r 2 ​ n 1 ​ ( mod ​ 1). \displaystyle=\frac{-ah\overline{qr_{1}}}{n_{1}r_{2}}+\frac{ah}{qr_{1}r_{2}n_{1}}\ (\mathrm{mod}\ 1). |  |

Since | h | ⩽ H = ( Q ​ R ​ log 5 ​ x) / M |h|{\,\leqslant}H=(QR\log^{5}{x})/M, the final fraction is of size O ⁡ ( a ​ log 5 ​ x / x) O(a\log^{5}{x}/x), and so we see that

 | e ⁡ ( a ​ h ​ n 1 ​ r 2 ¯ q ​ r 1 + a ​ h ​ n 2 ​ q ​ r 1 ¯ r 2) = e ⁡ ( a ​ h ​ n 2 ​ q ​ r 1 ¯ ​ ( n 1 − n 2) n 1 ​ r 2) + O ⁡ ( a x ​ log 6 ​ x). e\Bigl(\frac{ah\overline{n_{1}r_{2}}}{qr_{1}}+\frac{ah\overline{n_{2}qr_{1}}}{r_{2}}\Big)=e\Bigl(\frac{ah\overline{n_{2}qr_{1}}(n_{1}-n_{2})}{n_{1}r_{2}}\Bigr)+O\Bigl(\frac{a}{x}\log^{6}{x}\Bigr). |  |

Assuming the residue is | a | < x 1 + ϵ |a|<x^{1+\epsilon}, the error term above contributes to ℰ \mathcal{E} a total

 | ≪ N ( N Q + 1) Q ​ R 2 ​ ( log ⁡ ( x)) O B 0 ​ ( 1) M ​ x 1 − ϵ ≪ B 0 N 2 ​ x ϵ Q ( Q ​ R 2 M ​ x + Q 2 ​ R 2 x 2) ≪ B 0 N 2 Q ​ x ϵ, \ll N\Bigl(\frac{N}{Q}+1\Bigr)\frac{QR^{2}(\log{x})^{O_{B_{0}}(1)}}{Mx^{1-\epsilon}}\ll_{B_{0}}\frac{N^{2}x^{\epsilon}}{Q}\Bigl(\frac{QR^{2}}{Mx}+\frac{Q^{2}R^{2}}{x^{2}}\Bigr)\ll_{B_{0}}\frac{N^{2}}{Qx^{\epsilon}}, |  |

using ( 4.1) and ( 4.2). The proof that ℰ ≪ B 0 exp ⁡ ( ( log ⁡ log ⁡ ( x)) 5) sup | ℰ ′ | + N 2 / Q x ϵ \mathcal{E}\ll_{B_{0}}\exp((\log\log{x})^5)\sup|\mathcal{E}^{\prime}|+N^{2}/Qx^{\epsilon} now follows exactly as in [27, Lemma 14.5]. ∎

###### Lemma 4.7 (Second exponential sum estimate).

Let

(4.3) |  | D ​ R ​ N 3 / 2 \displaystyle DRN^{3/2} | < x 1 − 2 ​ ϵ, \displaystyle<x^{1-2\epsilon}, |  |

(4.4) |  | Q ​ D ​ R \displaystyle QDR | < x 1 − 2 ​ ϵ. \displaystyle<x^{1-2\epsilon}. |  |

Let α n \alpha_{n}, λ d, r \lambda_{d,r} be complex sequences with | λ d, r |, | α n | ⩽ x o ⁡ ( 1) |\lambda_{d,r}|,|\alpha_{n}|{\,\leqslant}x^{o(1)}. Let H 1:= N ​ Q ​ D ​ R ​ ( log ⁡ ( x)) 5 / x H_{1}:=NQDR(\log{x})^{5}/x and let

 | ℬ ~:= sup a ≠ 0 ∑ q ( q, a) = 1 ∑ d ∼ D ( d, a) = 1 ∑ r 1, r 2 ∼ R ( r 1 ​ r 2, a) = 1 ψ 0 ​ ( q Q) ​ λ d, r 1 ​ λ d, r 2 ¯ φ ⁡ ( q ​ d ​ r 2) ​ q ​ d ​ r 1 ​ ∑ n 1, n 2 ∼ N ( n 1, q ​ d ​ r 1) = 1 ( n 2, q ​ d ​ r 2) = 1 α n 1 ​ α n 2 ¯ ​ ∑ 1 ⩽ | h | ⩽ H 1 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1) ​ e ​ ( a ​ h ​ n 1 ¯ q ​ d ​ r 1) \widetilde{\mathcal{B}}:=\sup_{a\neq 0}\sum_{\begin{subarray}{c}q\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1}r_{2},a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q}\Bigr)\frac{\lambda_{d,r_{1}}\overline{\lambda_{d,r_{2}}}}{{\varphi}(qdr_{2})qdr_{1}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ (n_{1},qdr_{1})=1\\ (n_{2},qdr_{2})=1\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}}\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{1}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}}}{qdr_{1}}\Bigr) |  |

Then we have

 | ℬ ~ ≪ N 2 Q ​ D ​ x ϵ. \widetilde{\mathcal{B}}\ll\frac{N^{2}}{QDx^{\epsilon}}. |  |

###### Proof.

This is [28, Lemma 6.10]. The argument is uniform in the residue a a, only applying Cauchy-Schwarz, a smooth majorant, and the Weil bound. See [27, Lemma 17.3]. ∎

###### Lemma 4.8 (Reduction to smoothed sums).

Let N ⩾ x ϵ N{\,\geqslant}x^{\epsilon} and z ⩽ z 0 z{\,\leqslant}z_{0} and let α m \alpha_{m}, c q c_{q} be 1-bounded complex sequences.

Imagine that for every choice of N ′, D, A, C > 0 N^{\prime},D,A,C>0 with N ′ ​ D ≍ N N^{\prime}D\asymp N and D ⩽ y 0 D{\,\leqslant}y_{0}, and every smooth function f f supported on [1 / 2, 5 / 2] [1/2,5/2] satisfying f ( j) ≪ j ( log ⁡ ( x)) C ​ j f^{(j)}\ll_{j}(\log{x})^{Cj}, and for every 1 1 -bounded complex sequence β d \beta_{d} we have the estimate

 | sup a ≠ 0 ∑ q ∼ Q c q ∑ m ∼ M α m ∑ d ∼ D β d ∑ n ′ f ( n ′ N ′) ( 𝟏 m ​ n ′ ​ d ≡ a ⁡ ( mod ​ q) − 𝟏 ( m ​ n ′ ​ d, q) = 1 φ ⁡ ( q)) ≪ A, C x ( log ⁡ ( x)) A. \sup_{a\neq 0}\sum_{q\sim Q}c_{q}\sum_{m\sim M}\alpha_{m}\sum_{d\sim D}\beta_{d}\sum_{n^{\prime}}f\Bigl(\frac{n^{\prime}}{N^{\prime}}\Bigr)\Bigl(\mathbf{1}_{mn^{\prime}d\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(mn^{\prime}d,q)=1}}{{\varphi}(q)}\Bigr)\ll_{A,C}\frac{x}{(\log{x})^{A}}. |  |

Then for any B > 0 B>0 and every interval ℐ ⊆ [N, 2 ​ N] \mathcal{I}\subseteq[N,2N] we have

 | sup a ≠ 0 ∑ q ∼ Q c q ∑ m ∼ M α m ∑ n ∈ ℐ P − ​ ( n) > z ( 𝟏 m ​ n ≡ a ⁡ ( mod ​ q) − 𝟏 ( m ​ n, q) = 1 φ ⁡ ( q)) ≪ B x ( log ⁡ ( x)) B. \sup_{a\neq 0}\sum_{q\sim Q}c_{q}\sum_{m\sim M}\alpha_{m}\sum_{\begin{subarray}{c}n\in\mathcal{I}\\ P^{-}(n)>z\end{subarray}}\Bigl(\mathbf{1}_{mn\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(mn,q)=1}}{{\varphi}(q)}\Bigr)\ll_{B}\frac{x}{(\log{x})^{B}}. |  |

###### Proof.

This is [27, Lemma 19.2]. The argument is completely uniform in the residue a a, using a smooth partition of unity and the Fundamental Lemma of the Sieve. ∎

## 5. Well-factorable disperson estimates

In this section we establish Proposition 3.1, which is the main result toward Theorem 1.7. This can be viewed as a refinement of [4, Theorem 1]. Indeed, Proposition 3.1 essentially includes [4, Theorem 1] as the special case R = 1 R=1. The key advantage in our setup is to make use of the additional flexibility afforded by having a third factor available when manipulating the exponential sums. The argument does not have a specific regime when it is weakest; the critical case for Theorem 1.7 is the whole range x 1 / 10 ⩽ N ⩽ x 1 / 3 x^{1/10}{\,\leqslant}N{\,\leqslant}x^{1/3}. (The terms with N ⩽ x 1 / 10 N{\,\leqslant}x^{1/10} or N > x 1 / 3 N>x^{1/3} can be handled by a combination of the result for N ∈ [x 1 / 10, x 1 / 3] N\in[x^{1/10},x^{1/3}] and Proposition 3.2.)

###### Lemma 5.1 (Well-factorable exponential sum estimate).

Let Q < N ​ x − ϵ Q<Nx^{-\epsilon}, N ​ M ≍ x NM\asymp x, and

(5.1) |  | N 2 ​ R 2 ​ S \displaystyle N^{2}R^{2}S | < x 1 − 7 ​ ϵ, \displaystyle<x^{1-7\epsilon}, |  |

(5.2) |  | a θ ​ N ​ R 2 ​ S 5 ​ Q \displaystyle a^{\theta}\;NR^{2}S^{5}Q | < x 2 − 14 ​ ϵ, \displaystyle<x^{2-14\epsilon}, |  |

(5.3) |  | ( N ​ R / S) 2 ​ θ ​ N ​ R 2 ​ S 5 ​ Q \displaystyle(NR/S)^{2{\theta}}\;NR^{2}S^{5}Q | < x 2 − 14 ​ ϵ. \displaystyle<x^{2-14\epsilon}. |  |

Let Q ′ ⩽ 2 ​ Q Q^{\prime}{\,\leqslant}2Q, H ′ ⩽ x o ⁡ ( 1) ​ Q ​ R 2 ​ S 2 / M H^{\prime}{\,\leqslant}x^{o(1)}QR^{2}S^{2}/M, and γ r, λ s, α n \gamma_{r},\lambda_{s},\alpha_{n} be 1-bounded complex coefficients, and denote

 | 𝒲 \displaystyle\mathcal{W} | : = sup 0 < | a | < x 1 + ϵ ∑ Q ⩽ q ⩽ Q ′ ( q, a) = 1 ∑ r 1, r 2 ∼ R ∑ s 1, s 2 ∼ S ( r 1 ​ s 1, a ​ r 2 ​ s 2) = 1 ( r 2 ​ s 2, a ​ q ​ d ​ r 1 ​ s 1) = 1 r 1 ​ s 1 ⩽ B 1 r 2 ​ s 2 ⩽ B 2 γ r 1 ​ λ s 1 ​ γ r 2 ​ λ s 2 ¯ r 1 ​ r 2 ​ s 1 ​ s 2 ​ q ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q ​ d) ( n 1, n 2 ​ q ​ d ​ r 1 ​ s 1) = 1 ( n 2, n 1 ​ q ​ d ​ r 2 ​ s 2) = 1 ( n 1 ​ r 2 ​ s 2, n 2) ∈ 𝒩 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}Q{\,\leqslant}q{\,\leqslant}Q^{\prime}\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\end{subarray}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\\ (r_{1}s_{1},ar_{2}s_{2})=1\\ (r_{2}s_{2},aqdr_{1}s_{1})=1\\ r_{1}s_{1}{\,\leqslant}B_{1}\\ r_{2}s_{2}{\,\leqslant}B_{2}\end{subarray}}\frac{\gamma_{r_{1}}\lambda_{s_{1}}\overline{\gamma_{r_{2}}\lambda_{s_{2}}}}{r_{1}r_{2}s_{1}s_{2}q}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd)\\ (n_{1},n_{2}qdr_{1}s_{1})=1\\ (n_{2},n_{1}qdr_{2}s_{2})=1\\ (n_{1}r_{2}s_{2},n_{2})\in\mathcal{N}\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H ′ e ⁡ ( a ​ h ​ ( n 1 − n 2) ​ n 2 ​ r 1 ​ s 1 ​ d ​ q ¯ n 1 ​ r 2 ​ s 2) \displaystyle\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H^{\prime}}e\Bigl(\frac{ah(n_{1}-n_{2})\overline{n_{2}r_{1}s_{1}dq}}{n_{1}r_{2}s_{2}}\Bigr) |  |

for some ( d, a) = 1 (d,a)=1 where 𝒩 \mathcal{N} is a set with the property that if ( a, b) ∈ 𝒩 (a,b)\in\mathcal{N} and ( a ′, b ′) ∈ 𝒩 (a^{\prime},b^{\prime})\in\mathcal{N} then gcd ⁡ ( a, b ′) = gcd ⁡ ( a ′, b) = 1 \gcd(a,b^{\prime})=\gcd(a^{\prime},b)=1.

Then we have

 | 𝒲 ≪ N 2 Q ​ x ϵ. \mathcal{W}\ll\frac{N^{2}}{Qx^{\epsilon}}. |  |

###### Proof.

We first make a change of variables. Since we have n 1 ≡ n 2 ​ ( mod ​ q ​ d) n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd), we let f ​ d ​ q = n 1 − n 2 fdq=n_{1}-n_{2} for some integer | f | ⩽ 2 ​ N / d ​ Q ⩽ 2 ​ N / Q |f|{\,\leqslant}2N/dQ{\,\leqslant}2N/Q, and we wish to replace q q with ( n 1 − n 2) / d ​ f (n_{1}-n_{2})/df. We see that

 | ( n 1 − n 2) ​ d ​ q ¯ = f ⁡ ( mod ​ n 1 ​ r 2 ​ s 2). (n_{1}-n_{2})\overline{dq}=f\ (\mathrm{mod}\ n_{1}r_{2}s_{2}). |  |

Thus the exponential simplifies to

 | e ⁡ ( a ​ h ​ f ​ r 1 ​ s 1 ​ n 2 ¯ n 1 ​ r 2 ​ s 2). e\Bigl(\frac{ahf\overline{r_{1}s_{1}n_{2}}}{n_{1}r_{2}s_{2}}\Bigr). |  |

The conditions ( n 1, n 2) = 1 (n_{1},n_{2})=1 and n 1 ≡ n 2 ​ ( mod ​ d ​ q) n_{1}\equiv n_{2}\ (\mathrm{mod}\ dq) automatically imply ( n 1 ​ n 2, d ​ q) = 1 (n_{1}n_{2},dq)=1, and so we find

 | 𝒲 \displaystyle\mathcal{W} | = sup 0 < | a | < x 1 + ϵ ∑ 1 ⩽ | f | ⩽ 2 ​ N / Q ∑ r 1, r 2 ∼ R ( r 1 ​ r 2, a) = 1 ∑ s 2 ∼ S ( r 2 ​ s 2, a ​ d ​ r 1) = 1 r 2 ​ s 2 ⩽ B 2 ∑ ′ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ d ​ f) ′ ​ γ r 1 ​ γ r 2 ​ λ s 2 ¯ ​ d ​ f r 1 ​ r 2 ​ s 2 ​ ( n 1 − n 2) \displaystyle=\sup_{0<|a|<x^{1+\epsilon}}\sum_{1{\,\leqslant}|f|{\,\leqslant}2N/Q}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1}r_{2},a)=1\end{subarray}}\sum_{\begin{subarray}{c}s_{2}\sim S\\ (r_{2}s_{2},adr_{1})=1\\ r_{2}s_{2}{\,\leqslant}B_{2}\end{subarray}}\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ df)\end{subarray}}\frac{\gamma_{r_{1}}\overline{\gamma_{r_{2}}\lambda_{s_{2}}}df}{r_{1}r_{2}s_{2}(n_{1}-n_{2})} |  |

 |  | × ∑ s 1 ∼ S ( s 1, a ​ n 1 ​ r 2 ​ s 2) = 1 r 1 ​ s 1 ⩽ B 1 λ s 1 s 1 ​ ∑ 1 ⩽ | h | ⩽ H ′ α n 1 ​ α n 2 ¯ ​ e ​ ( a ​ h ​ f ​ r 1 ​ s 1 ​ n 2 ¯ n 1 ​ r 2 ​ s 2). \displaystyle\qquad\times\sum_{\begin{subarray}{c}s_{1}\sim S\\ (s_{1},an_{1}r_{2}s_{2})=1\\ r_{1}s_{1}{\,\leqslant}B_{1}\end{subarray}}\frac{\lambda_{s_{1}}}{s_{1}}\sum_{1{\,\leqslant}|h|{\,\leqslant}H^{\prime}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}}e\Bigl(\frac{ahf\overline{r_{1}s_{1}n_{2}}}{n_{1}r_{2}s_{2}}\Bigr). |  |

Here we have used ∑ ′ \sum^{\prime} to denote that fact that we have suppressed the conditions

 |  | ( n 1, n 2 ​ r 1 ​ s 1) = 1, \displaystyle(n_{1},n_{2}r_{1}s_{1})=1, |  | ( n 2, n 1 ​ r 2 ​ s 2) = 1, \displaystyle(n_{2},n_{1}r_{2}s_{2})=1, |  | ( n 1 ​ r 2 ​ s 2, n 2) ∈ 𝒩, \displaystyle(n_{1}r_{2}s_{2},n_{2})\in\mathcal{N}, |  |

 |  | | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C, \displaystyle|n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}, |  | ( ( n 1 − n 2) / d ​ f, a ​ r 2 ​ s 2) = 1, \displaystyle((n_{1}-n_{2})/df,ar_{2}s_{2})=1, |  | Q ​ d ​ f ⩽ n 1 − n 2 ⩽ Q ′ ​ d ​ f. \displaystyle Qdf{\,\leqslant}n_{1}-n_{2}{\,\leqslant}Q^{\prime}df. |  |

We first remove the dependency between r 1 r_{1} and s 1 s_{1} from the constraint r 1 ​ s 1 ⩽ B 1 r_{1}s_{1}{\,\leqslant}B_{1} by noting

 | 𝟏 r 1 ​ s 1 ⩽ B 1 \displaystyle\mathbf{1}_{r_{1}s_{1}{\,\leqslant}B_{1}} | = ∫ 0 1 ( ∑ j ⩽ B 1 / r 1 e ⁡ ( − j ​ u)) ​ e ​ ( s 1 ​ u) ​ 𝑑 u \displaystyle=\int_{0}^{1}\Bigl(\sum_{j{\,\leqslant}B_{1}/r_{1}}e(-ju)\Bigr)e(s_{1}u)du |  |

 |  | = ∫ 0 1 c r 1, u ​ min ⁡ ( B 1 R, | u | − 1) ​ e ​ ( s 1 ​ u) ​ 𝑑 u \displaystyle=\int_{0}^{1}c_{r_{1},u}\min\Bigl(\frac{B_{1}}{R},|u|^{-1}\Bigr)e(s_{1}u)du |  |

for some 1-bounded coefficients c r 1, u c_{r_{1},u}. Thus

 | 𝒲 \displaystyle\mathcal{W} | = ∫ 0 1 min ⁡ ( B 1 R, | u | − 1) ​ 𝒲 2 ​ ( u) ​ 𝑑 u ≪ ( log ⁡ ( x)) ​ sup u | 𝒲 2 ​ ( u) |, \displaystyle=\int_{0}^{1}\min\Bigl(\frac{B_{1}}{R},|u|^{-1}\Bigr)\mathcal{W}_{2}(u)du\ll(\log{x})\sup_{u}|\mathcal{W}_{2}(u)|, |  |

where 𝒲 2 = 𝒲 2 ​ ( u) \mathcal{W}_{2}=\mathcal{W}_{2}(u) is given by

 | 𝒲 2 \displaystyle\mathcal{W}_{2} | : = sup 0 < | a | < x 1 + ϵ ∑ 1 ⩽ | f | ⩽ 2 ​ N / Q ∑ r 1, r 2 ∼ R ( r 1 ​ r 2, a) = 1 ∑ s 2 ∼ S ( r 2 ​ s 2, a ​ d ​ r 1) = 1 r 2 ​ s 2 ⩽ B 2 ∑ ′ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ d ​ f) ′ ​ γ r 1 ​ c r 1, u ​ γ r 2 ​ λ s 2 ¯ ​ d ​ f r 1 ​ r 2 ​ s 2 ​ ( n 1 − n 2) \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{1{\,\leqslant}|f|{\,\leqslant}2N/Q}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1}r_{2},a)=1\end{subarray}}\sum_{\begin{subarray}{c}s_{2}\sim S\\ (r_{2}s_{2},adr_{1})=1\\ r_{2}s_{2}{\,\leqslant}B_{2}\end{subarray}}\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ df)\end{subarray}}\frac{\gamma_{r_{1}}c_{r_{1},u}\overline{\gamma_{r_{2}}\lambda_{s_{2}}}df}{r_{1}r_{2}s_{2}(n_{1}-n_{2})} |  |

 |  | × ∑ s 1 ∼ S ( s 1, a ​ n 1 ​ r 2 ​ s 2) = 1 e ⁡ ( s 1 ​ u) ​ λ s 1 s 1 ​ ∑ 1 ⩽ | h | ⩽ H ′ α n 1 ​ α n 2 ¯ ​ e ​ ( a ​ h ​ f ​ r 1 ​ s 1 ​ n 2 ¯ n 1 ​ r 2 ​ s 2). \displaystyle\qquad\times\sum_{\begin{subarray}{c}s_{1}\sim S\\ (s_{1},an_{1}r_{2}s_{2})=1\end{subarray}}\frac{e(s_{1}u)\lambda_{s_{1}}}{s_{1}}\sum_{1{\,\leqslant}|h|{\,\leqslant}H^{\prime}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}}e\Bigl(\frac{ahf\overline{r_{1}s_{1}n_{2}}}{n_{1}r_{2}s_{2}}\Bigr). |  |

In order to show 𝒲 ≪ N 2 / ( Q ​ x ϵ) \mathcal{W}\ll N^{2}/(Qx^{\epsilon}) we see it is sufficient to show 𝒲 2 ≪ N 2 / ( Q ​ x 2 ​ ϵ) \mathcal{W}_{2}\ll N^{2}/(Qx^{2\epsilon}). We now apply Cauchy-Schwarz in the f f, n 1 n_{1}, n 2 n_{2}, r 1 r_{1}, r 2 r_{2} and s 2 s_{2} variables. This gives

 | 𝒲 2 ≪ N ​ R ​ S 1 / 2 ​ ( log ⁡ ( x)) 2 Q ​ R 2 ​ S 2 ​ 𝒲 3 1 / 2, \displaystyle\mathcal{W}_{2}\ll\frac{NRS^{1/2}(\log{x})^{2}}{QR^{2}S^{2}}\mathcal{W}_{3}^{1/2}, |  |

where

 | 𝒲 3 \displaystyle\mathcal{W}_{3} | : = sup 0 < | a | < x 1 + ϵ ∑ 1 ⩽ | f | ⩽ 2 ​ N / Q ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ d ​ f) ∑ r 1, r 2 ∼ R \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{1{\,\leqslant}|f|{\,\leqslant}2N/Q}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ df)\end{subarray}}\sum_{r_{1},r_{2}\sim R} |  |

 |  | × ∑ s 2 ∼ S ( n 2 ​ r 1, n 1 ​ r 2 ​ s 2) = 1 | ∑ s 1 ∼ S ( s 1, a ​ n 1 ​ r 2 ​ s 2) = 1 ∑ 1 < | h | ⩽ H ′ λ s 1 ′ ​ e ​ ( a ​ h ​ f ​ r 1 ​ s 1 ​ n 2 ¯ n 1 ​ r 2 ​ s 2) | 2, \displaystyle\qquad\times\sum_{\begin{subarray}{c}s_{2}\sim S\\ (n_{2}r_{1},n_{1}r_{2}s_{2})=1\end{subarray}}\Bigl|\sum_{\begin{subarray}{c}s_{1}\sim S\\ (s_{1},an_{1}r_{2}s_{2})=1\end{subarray}}\sum_{1<|h|{\,\leqslant}H^{\prime}}\lambda_{s_{1}}^{\prime}e\Bigl(\frac{ahf\overline{r_{1}s_{1}n_{2}}}{n_{1}r_{2}s_{2}}\Bigr)\Bigr|^{2}, |  |

and where

 | λ s ′:= S s ​ λ s ​ e ​ ( s ​ u) \lambda_{s}^{\prime}:=\frac{S}{s}\lambda_{s}e(su) |  |

are 1-bounded coefficients. Note that we have dropped many of the constraints on the summation for an upper bound. In order to show that 𝒲 2 ≪ N 2 / ( Q ​ x 2 ​ ϵ) \mathcal{W}_{2}\ll N^{2}/(Qx^{2\epsilon}) we see it is sufficient to show that 𝒲 3 ≪ N 2 ​ R 2 ​ S 3 / x 5 ​ ϵ \mathcal{W}_{3}\ll N^{2}R^{2}S^{3}/x^{5\epsilon}. We first drop the congruence condition on n 1, n 2 ​ ( mod ​ d ​ f) n_{1},n_{2}\ (\mathrm{mod}\ df) for an upper bound, and then we combine n 2 ​ r 1 n_{2}r_{1} into a single variable b b and n 1 ​ r 2 ​ s 2 n_{1}r_{2}s_{2} into a single variable c c. Using the divisor bound to control the number of representations of c c and b b, and inserting a smooth majorant, this gives

 | 𝒲 3 \displaystyle\mathcal{W}_{3} | ⩽ x o ⁡ ( 1) ​ sup B ≪ N ​ R C ≪ N ​ R ​ S F ≪ N / Q 𝒲 4, \displaystyle{\,\leqslant}x^{o(1)}\sup_{\begin{subarray}{c}B\ll NR\\ C\ll NRS\\ F\ll N/Q\end{subarray}}\mathcal{W}_{4}, |  |

where

 | 𝒲 4 \displaystyle\mathcal{W}_{4} | : = sup 0 < | a | < x 1 + ϵ ∑ b ∑ c ( b, c) = 1 g ⁡ ( b, c) ​ ∑ f ∼ F | ∑ s 1 ∼ S ( s 1, a ​ c) = 1 ∑ 1 < | h | ⩽ H ′ λ s 1 ′ ​ e ​ ( a ​ h ​ f ​ b ​ s 1 ¯ c) | 2 \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{b}\sum_{\begin{subarray}{c}c\\ (b,c)=1\end{subarray}}g(b,c)\sum_{f\sim F}\Bigl|\sum_{\begin{subarray}{c}s_{1}\sim S\\ (s_{1},ac)=1\end{subarray}}\sum_{1<|h|{\,\leqslant}H^{\prime}}\lambda_{s_{1}}^{\prime}e\Bigl(\frac{ahf\overline{bs_{1}}}{c}\Bigr)\Bigr|^{2} |  |

 | g ⁡ ( b, c) \displaystyle g(b,c) | : = ψ 0 ​ ( b B) ​ ψ 0 ​ ( c C). \displaystyle:=\psi_{0}\Bigl(\frac{b}{B}\Bigr)\psi_{0}\Bigl(\frac{c}{C}\Bigr). |  |

In order to show 𝒲 3 ≪ N 2 ​ R 2 ​ S 3 / x 5 ​ ϵ \mathcal{W}_{3}\ll N^{2}R^{2}S^{3}/x^{5\epsilon}, it is sufficient to show that

(5.4) |  | 𝒲 4 ≪ N 2 ​ R 2 ​ S 3 x 6 ​ ϵ. \mathcal{W}_{4}\ll\frac{N^{2}R^{2}S^{3}}{x^{6\epsilon}}. |  |

We expand the square and swap the order of summation, giving

 | 𝒲 4 = sup 0 < | a | < x 1 + ϵ ∑ s 1, s 2 ∼ S ( s 1 ​ s 2, a) = 1 ∑ 1 < | h 1 |, | h 2 | ⩽ H ′ λ s 1 ′ ​ λ s 2 ′ ¯ ​ ∑ b ∑ f ∼ F ∑ c ( c, b ​ s 1 ​ s 2) = 1 g ⁡ ( b, c) ​ e ​ ( a ​ f ​ k ​ b ​ s 1 ​ s 2 ¯ c), \mathcal{W}_{4}=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\\ (s_{1}s_{2},a)=1\end{subarray}}\sum_{1<|h_{1}|,|h_{2}|{\,\leqslant}H^{\prime}}\lambda_{s_{1}}^{\prime}\overline{\lambda_{s_{2}}^{\prime}}\sum_{b}\sum_{f\sim F}\sum_{\begin{subarray}{c}c\\ (c,bs_{1}s_{2})=1\end{subarray}}g(b,c)e\Bigl(afk\frac{\overline{bs_{1}s_{2}}}{c}\Bigr), |  |

where

 | k = h 1 ​ s 1 − h 2 ​ s 2. k=h_{1}s_{1}-h_{2}s_{2}. |  |

We now split the sum according to whether k = 0 k=0 or not.

 | 𝒲 4 = 𝒲 k = 0 + 𝒲 k ≠ 0. \mathcal{W}_{4}=\mathcal{W}_{k=0}+\mathcal{W}_{k\neq 0}. |  |

To show ( 5.4) it is sufficient to show

(5.5) |  | 𝒲 k = 0 ≪ N 2 ​ R 2 ​ S 3 x 6 ​ ϵ and 𝒲 k ≠ 0 ≪ N 2 ​ R 2 ​ S 3 x 6 ​ ϵ. \mathcal{W}_{k=0}\ll\frac{N^{2}R^{2}S^{3}}{x^{6\epsilon}}\qquad\text{and}\qquad\mathcal{W}_{k\neq 0}\ll\frac{N^{2}R^{2}S^{3}}{x^{6\epsilon}}. |  |

We first consider 𝒲 k = 0 \mathcal{W}_{k=0}, and so terms with h 1 ​ s 1 = h 2 ​ s 2 h_{1}s_{1}=h_{2}s_{2}. Given h 1, s 1 h_{1},s_{1} there are at most x o ⁡ ( 1) x^{o(1)} choices of h 2, s 2 h_{2},s_{2}, and so at most x o ⁡ ( 1) ​ H ​ S x^{o(1)}HS choices of h 1, h 2, s 1, s 2 h_{1},h_{2},s_{1},s_{2}. Thus we see that

 | 𝒲 k = 0 ≪ x o ⁡ ( 1) ​ H ​ S ​ B ​ F ​ C \displaystyle\mathcal{W}_{k=0}\ll x^{o(1)}HSBFC | ≪ x o ⁡ ( 1) ​ R 2 ​ S 2 ​ Q M ⋅ S ⋅ N ​ R ⋅ N Q ⋅ N ​ R ​ S \displaystyle\ll x^{o(1)}\frac{R^{2}S^{2}Q}{M}\cdot S\cdot NR\cdot\frac{N}{Q}\cdot NRS |  |

 |  | ≪ N 4 ​ R 4 ​ S 4 x 1 − ϵ. \displaystyle\ll\frac{N^{4}R^{4}S^{4}}{x^{1-\epsilon}}. |  |

This gives 𝒲 k = 0 ≪ N 2 ​ R 2 ​ S 3 ​ x − 6 ​ ϵ \mathcal{W}_{k=0}\ll N^{2}R^{2}S^{3}x^{-6\epsilon} as in ( 5.5), provided

(5.6) |  | N 2 ​ R 2 ​ S ≪ x 1 − 7 ​ ϵ. N^{2}R^{2}S\ll x^{1-7\epsilon}. |  |

We now consider 𝒲 k ≠ 0 \mathcal{W}_{k\neq 0}. We let y = f ​ k = f ⁡ ( h 1 ​ s 1 − h 2 ​ s 2) ≪ x o ⁡ ( 1) ​ N ​ R 2 ​ S 3 / M y=fk=f(h_{1}s_{1}-h_{2}s_{2})\ll x^{o(1)}NR^{2}S^{3}/M and z = s 1 ​ s 2 ≪ S 2 z=s_{1}s_{2}\ll S^{2}. Recall y = f ​ k ≠ 0 y=fk\neq 0. Putting these variables in dyadic intervals and using the symmetry between y y and − y -y, we see that

 | 𝒲 k ≠ 0 ≪ log ⁡ ( x) ​ sup 0 < | a | < x 1 + ϵ ∑ z ∼ Z ∑ y ∼ Y b z, y ​ | ∑ b ∑ c ( c, z ​ b) = 1 g ⁡ ( b, c) ​ e ​ ( a ​ y ​ z ​ b ¯ c) |, \mathcal{W}_{k\neq 0}\ll\log{x}\sup_{0<|a|<x^{1+\epsilon}}\sum_{z\sim Z}\sum_{y\sim Y}b_{z,y}\Bigl|\sum_{b}\sum_{\begin{subarray}{c}c\\ (c,zb)=1\end{subarray}}g(b,c)e\Bigl(\frac{ay\overline{zb}}{c}\Bigr)\Bigr|, |  |

where Z ≍ S 2 Z\asymp S^{2}, Y ≪ x o ⁡ ( 1) ​ N ​ R 2 ​ S 3 / M Y\ll x^{o(1)}NR^{2}S^{3}/M and

 | b z, y = ∑ s 1, s 2 ∼ S ∑ 1 ⩽ | h 1 |, | h 2 | ⩽ H ′ ∑ f ∼ F s 1 ​ s 2 = z f ⁡ ( h 1 ​ s 1 − h 2 ​ s 2) = y ⁡ 1. b_{z,y}=\mathop{\sum_{s_{1},s_{2}\sim S}\sum_{1{\,\leqslant}|h_{1}|,|h_{2}|{\,\leqslant}H^{\prime}}\sum_{f\sim F}}\limits_{\begin{subarray}{c}s_{1}s_{2}=z\\ f(h_{1}s_{1}-h_{2}s_{2})=y\end{subarray}}1. |  |

By Theorem 1.8 with ( ‘C’, ‘D’,‘N’,‘R’,‘S’,‘q’) → ( C, B, Y, Z, 1, 1) \rightarrow(C,B,Y,Z,1,1), we have that

(5.7) |  | 𝒲 k ≠ 0 ≪ x ϵ ​ 𝒥, \mathcal{W}_{k\neq 0}\ll x^{\epsilon}\;\mathcal{J}, |  |

where

 | 𝒥 2 \displaystyle\mathcal{J}^{2} | ≪ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ N ( a ​ n ′′) θ ​ ( C ​ S ​ ( R ​ S + N n ′′) ​ ( C + D ​ R) + a ​ N ​ R ​ S) ​ ‖ b ~ ​ ( n ′′) ‖ 2 \displaystyle\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2N\end{subarray}}(an^{\prime\prime})^{\theta}\Big(CS\Big(RS+\frac{N}{n^{\prime\prime}}\Big)(C+DR)+aNRS\Big)\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2} |  |

 |  | + ( C ​ S ​ ( C ​ D ​ R) 2 ​ θ ​ ( N + R ​ S) 1 − θ ​ ( C + D ​ R) 1 − 2 ​ θ + D 2 ​ N ​ R) ​ ‖ b ‖ 2 2 \displaystyle\quad+\Big(CS(CD\sqrt{R})^{2{\theta}}(N+RS)^{1-{\theta}}(C+DR)^{1-2{\theta}}+D^{2}NR\Big)\|\textbf{b}\|_{2}^{2} |  |

(5.8) |  |  | ≪ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ Y ( a ​ n ′′) θ ​ ( C ⁡ ( Z + Y n ′′) ​ ( C + B ​ Z) + a ​ Y ​ Z) ​ ‖ b ~ ​ ( n ′′) ‖ 2 \displaystyle\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2Y\end{subarray}}(an^{\prime\prime})^{\theta}\Big(C\Big(Z+\frac{Y}{n^{\prime\prime}}\Big)(C+BZ)+aYZ\Big)\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2} |  |

 |  | + ( C ​ ( C ​ B ​ Z) 2 ​ θ ​ ( Y + Z) 1 − θ ​ ( C + B ​ Z) 1 − 2 ​ θ + B 2 ​ Y ​ Z) ​ ‖ b ‖ 2 2 \displaystyle\quad+\Big(C(CB\sqrt{Z})^{2{\theta}}(Y+Z)^{1-{\theta}}(C+BZ)^{1-2{\theta}}+B^{2}YZ\Big)\|\textbf{b}\|_{2}^{2} |  |

Since the above bound on 𝒥 2 \mathcal{J}^{2} is increasing and polynomial in C, B, Z, Y C,B,Z,Y, the maximal value is at most x o ⁡ ( 1) x^{o(1)} times the value when C = N ​ R ​ S C=NRS, Z = S 2 Z=S^{2}, Y = N ​ R 2 ​ S 3 / M Y=NR^{2}S^{3}/M and B = N ​ R B=NR, and so it suffices to consider this case. We note that our bound M > N ​ R 2 ​ S M>NR^{2}S from ( 5.6) then implies that that Z > Y Z>Y, and so, noting that B ​ Z > C BZ>C and C ​ B ​ Z 2 > B 2 ​ Y ​ Z CBZ^{2}>B^{2}YZ, this simplifies ( 5) to

 | 𝒥 2 \displaystyle\mathcal{J}^{2} | ≪ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ Y ( a ​ n ′′) θ ​ ( C ​ Z ​ ( B ​ Z) + a ​ Y ​ Z) ​ ‖ b ~ ​ ( n ′′) ‖ 2 2 \displaystyle\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2Y\end{subarray}}(an^{\prime\prime})^{\theta}\Big(CZ(BZ)+aYZ\Big)\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | + ( C ​ ( C ​ B ​ Z) 2 ​ θ ​ ( Z) 1 − θ ​ ( B ​ Z) 1 − 2 ​ θ + B 2 ​ Y ​ Z) ​ ‖ b ‖ 2 2 \displaystyle\quad+\Big(C(CB\sqrt{Z})^{2{\theta}}(Z)^{1-{\theta}}(BZ)^{1-2{\theta}}+B^{2}YZ\Big)\|\textbf{b}\|_{2}^{2} |  |

(5.9) |  |  | ≪ ( C ​ B ​ Z + a ​ Y) ​ Z ​ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ Y ( a ​ n ′′) θ ​ ‖ b ~ ​ ( n ′′) ‖ 2 2 + ( C 1 + 2 ​ θ ​ B ​ Z 2 − 2 ​ θ + B 2 ​ Y ​ Z) ​ ‖ b ‖ 2 2. \displaystyle\ll\Big(CBZ+aY\Big)Z\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2Y\end{subarray}}(an^{\prime\prime})^{\theta}\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}\ +\ \Big(C^{1+2{\theta}}BZ^{2-2{\theta}}+B^{2}YZ\Big)\|\textbf{b}\|_{2}^{2}. |  |

Now we consider ‖ b ~ ​ ( n ′′) ‖ 2 \|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}. We note that given a choice of z, y z,y there are x o ⁡ ( 1) x^{o(1)} choices of s 1, s 2, f, k s_{1},s_{2},f,k with z = s 1 ​ s 2 z=s_{1}s_{2} and n ′′ ​ y = f ​ k n^{\prime\prime}y=fk by the divisor bound. Thus by Cauchy-Schwarz,

 | ‖ b ~ ​ ( n ′′) ‖ 2 2 \displaystyle\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2} | = ∑ z ∼ Z ∑ y ∼ Y / n ′′ b z, n ′′ ​ y 2 = ∑ z ∼ Z ∑ y ∼ Y / n ′′ ( ∑ s 1, s 2 ∼ S s 1 ​ s 2 = z ∑ f ∼ F ∑ k ≍ Y / F f ​ k = n ′′ ​ y ∑ 1 ⩽ | h 1 |, | h 2 | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 1) 2 \displaystyle=\sum_{z\sim Z}\sum_{y\sim Y/n^{\prime\prime}}b_{z,n^{\prime\prime}y}^{2}=\sum_{z\sim Z}\sum_{y\sim Y/n^{\prime\prime}}\Bigl(\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\\ s_{1}s_{2}=z\end{subarray}}\sum_{\begin{subarray}{c}f\sim F\end{subarray}}\sum_{\begin{subarray}{c}k\asymp Y/F\\ fk=n^{\prime\prime}y\end{subarray}}\sum_{\begin{subarray}{c}1{\,\leqslant}|h_{1}|,|h_{2}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}\end{subarray}}1\Bigr)^{2} |  |

 |  | ≪ x o ⁡ ( 1) ​ ∑ y ∼ Y / n ′′ ∑ s 1, s 2 ∼ S ∑ f ∼ F ∑ k ≍ Y / F f ​ k = n ′′ ​ y ∑ 1 ⩽ | h 1 |, | h 1 ′ |, | h 2 |, | h 2 ′ | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 = h 1 ′ ​ s 1 − h 2 ′ ​ s 2 1 \displaystyle\ll x^{o(1)}\sum_{y\sim Y/n^{\prime\prime}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\end{subarray}}\sum_{\begin{subarray}{c}f\sim F\end{subarray}}\sum_{\begin{subarray}{c}k\asymp Y/F\\ fk=n^{\prime\prime}y\end{subarray}}\sum_{\begin{subarray}{c}1{\,\leqslant}|h_{1}|,|h_{1}^{\prime}|,|h_{2}|,|h_{2}^{\prime}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}=h_{1}^{\prime}s_{1}-h_{2}^{\prime}s_{2}\end{subarray}}1 |  |

 |  | ≪ x o ⁡ ( 1) ​ ∑ s 1, s 2 ∼ S ∑ k ≍ Y / F ∑ 1 ⩽ | h 1 |, | h 1 ′ |, | h 2 |, | h 2 ′ | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 = h 1 ′ ​ s 1 − h 2 ′ ​ s 2 ∑ n ′′ ( n ′′, k) | f ∼ F 1 \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\end{subarray}}\sum_{k\asymp Y/F}\sum_{\begin{subarray}{c}1{\,\leqslant}|h_{1}|,|h_{1}^{\prime}|,|h_{2}|,|h_{2}^{\prime}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}=h_{1}^{\prime}s_{1}-h_{2}^{\prime}s_{2}\end{subarray}}\sum_{\begin{subarray}{c}\frac{n^{\prime\prime}}{(n^{\prime\prime},k)}\mid f\sim F\end{subarray}}1 |  |

Note k ≍ Y / F ≍ H ​ S k\asymp Y/F\asymp HS. Then letting c = n ′′ / ( n ′′, k) < 2 ​ F c=n^{\prime\prime}/(n^{\prime\prime},k)<2F, we have ∑ c | f ∼ F 1 < 4 ​ F / c \sum_{\begin{subarray}{c}c\mid f\sim F\end{subarray}}1<4F/c and n ′′ / c | k n^{\prime\prime}/c\mid k, so that

 | ‖ b ~ ​ ( n ′′) ‖ 2 2 \displaystyle\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2} | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ k ≍ H ​ S n ′′ / c | k ∑ s 1, s 2 ∼ S ∑ 1 ⩽ | h 1 |, | h 1 ′ |, | h 2 |, | h 2 ′ | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 = h 1 ′ ​ s 1 − h 2 ′ ​ s 2 ∑ c | f ∼ F 1 \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{\begin{subarray}{c}k\asymp HS\\ n^{\prime\prime}/c\mid k\end{subarray}}\sum_{s_{1},s_{2}\sim S}\sum_{\begin{subarray}{c}1{\,\leqslant}|h_{1}|,|h_{1}^{\prime}|,|h_{2}|,|h_{2}^{\prime}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}=h_{1}^{\prime}s_{1}-h_{2}^{\prime}s_{2}\end{subarray}}\sum_{\begin{subarray}{c}c\mid f\sim F\end{subarray}}1 |  |

(5.10) |  |  | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ k ≍ H ​ S n ′′ / c | k ∑ s 1, s 2 ∼ S ( s 1, s 2) = 1 ∑ | h 1 |, | m 1 |, | h 2 |, | m 2 | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 t = m 1 ​ s 1 = m 2 ​ s 2 F c. \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{\begin{subarray}{c}k\asymp HS\\ n^{\prime\prime}/c\mid k\end{subarray}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\\ (s_{1},s_{2})=1\end{subarray}}\sum_{\begin{subarray}{c}|h_{1}|,|m_{1}|,|h_{2}|,|m_{2}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}\\ t=m_{1}s_{1}=m_{2}s_{2}\end{subarray}}\frac{F}{c}. |  |

Here we set m 1 = h 1 − h 1 ′ m_{1}=h_{1}-h_{1}^{\prime} and m 2 = h 2 − h 2 ′ m_{2}=h_{2}-h_{2}^{\prime}, and noted k = h 1 ​ s 1 − h 2 ​ s 2 = h 1 ′ ​ s 1 − h 2 ′ ​ s 2 k=h_{1}s_{1}-h_{2}s_{2}=h_{1}^{\prime}s_{1}-h_{2}^{\prime}s_{2} implies that t:= ( h 1 − h 1 ′) ​ s 1 = ( h 2 − h 2 ′) ​ s 2 t:=(h_{1}-h_{1}^{\prime})s_{1}=(h_{2}-h_{2}^{\prime})s_{2}. We now handle the inner sum in ( 5):

If t = 0 t=0, this forces m 1 = m 2 = 0 m_{1}=m_{2}=0. Then there are O ⁡ ( H ​ S) O(HS) choices h 1, s 1 h_{1},s_{1} and given k k by the divisor bound, x o ⁡ ( 1) x^{o(1)} further choices of h 2, s 2 h_{2},s_{2} such that k = h 1 ​ s 1 − h 2 ​ s 2 k=h_{1}s_{1}-h_{2}s_{2}. Thus

 | ∥ b ~ ( n ′′) ∥ 2 2 [t = 0] \displaystyle\|\underset{[t=0]}{\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}} | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ k ≍ H ​ S n ′′ / c | k ∑ s 1, s 2 ∼ S ∑ | h 1 |, | h 2 | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 t = 0 F c \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{\begin{subarray}{c}k\asymp HS\\ n^{\prime\prime}/c\mid k\end{subarray}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S\end{subarray}}\sum_{\begin{subarray}{c}|h_{1}|,|h_{2}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}\\ t=0\end{subarray}}\frac{F}{c} |  |

(5.11) |  |  | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ k ≍ H ​ S n ′′ / c | k ( H ​ S) ​ F c ≪ x o ⁡ ( 1) ​ ∑ n ′′ / H ​ S ≪ c ≪ F c | n ′′ ( H ​ S n ′′ + 1 c) ​ ( H ​ S) ​ F ≪ x o ⁡ ( 1) ​ ( H ​ S) 2 ​ F n ′′. \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{\begin{subarray}{c}k\asymp HS\\ n^{\prime\prime}/c\mid k\end{subarray}}(HS)\frac{F}{c}\ll x^{o(1)}\sum_{\begin{subarray}{c}n^{\prime\prime}/HS\ll c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\Big(\frac{HS}{n^{\prime\prime}}+\frac{1}{c}\Big)(HS)F\ll x^{o(1)}(HS)^{2}\frac{F}{n^{\prime\prime}}. |  |

Otherwise suppose t ≠ 0 t\neq 0. For this, we factor out d = ( s 1, s 2) ≪ S d=(s_{1},s_{2})\ll S and g = ( m 1, m 2) g=(m_{1},m_{2}). There are O ⁡ ( H ​ S / d) O(HS/d) choices of h 1, s 1 h_{1},s_{1}, and then given k k there are x o ⁡ ( 1) x^{o(1)} choices of h 2, s 2 h_{2},s_{2} such that k = h 1 ​ s 1 − h 2 ​ s 2 k=h_{1}s_{1}-h_{2}s_{2} by the divisor bound. Further, nonzero t = m 1 ​ s 1 = m 2 ​ s 2 t=m_{1}s_{1}=m_{2}s_{2} forces m 2 = s 1 m_{2}=s_{1} and s 2 = m 1 s_{2}=m_{1} by coprimality. In particular, this forces H / g ≍ S / d H/g\asymp S/d. Thus

 | ∥ b ~ ( n ′′) ∥ 2 2 [t ≠ 0] \displaystyle\|\underset{[t\neq 0]}{\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}} | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ d ≪ S ∑ g ≍ d ​ H / S ∑ k ≍ H ​ S / d n ′′ / c | k ​ d ∑ s 1, s 2 ∼ S / d ( s 1, s 2) = 1 ∑ | m 1 |, | m 2 | ≪ H / g ( m 1, m 2) = 1 ∑ | h 1 |, | h 2 | ≪ H k = h 1 ​ s 1 − h 2 ​ s 2 t = m 1 ​ s 1 = m 2 ​ s 2 ≠ 0 F c \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{d\ll S}\sum_{g\asymp dH/S}\sum_{\begin{subarray}{c}k\asymp HS/d\\ n^{\prime\prime}/c\mid kd\end{subarray}}\sum_{\begin{subarray}{c}s_{1},s_{2}\sim S/d\\ (s_{1},s_{2})=1\end{subarray}}\sum_{\begin{subarray}{c}|m_{1}|,|m_{2}|\ll H/g\\ (m_{1},m_{2})=1\end{subarray}}\sum_{\begin{subarray}{c}|h_{1}|,|h_{2}|\ll H\\ k=h_{1}s_{1}-h_{2}s_{2}\\ t=m_{1}s_{1}=m_{2}s_{2}\neq 0\end{subarray}}\frac{F}{c} |  |

 |  | ≪ x o ⁡ ( 1) ​ ∑ c ≪ F c | n ′′ ∑ d ≪ S ∑ g ≍ d ​ H / S ∑ k ≍ H ​ S / d n ′′ / b ​ c | k H ​ S d ​ F c, \displaystyle\ll x^{o(1)}\sum_{\begin{subarray}{c}c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\sum_{d\ll S}\sum_{g\asymp dH/S}\sum_{\begin{subarray}{c}k\asymp HS/d\\ n^{\prime\prime}/bc\mid k\end{subarray}}\frac{HS}{d}\frac{F}{c}, |  |

noting n ′′ / c | k ​ d n^{\prime\prime}/c\mid kd implies n ′′ / b ​ c | k n^{\prime\prime}/bc\mid k, where b:= ( d, n ′′ / c) b:=(d,n^{\prime\prime}/c). In particular n ′′ / b ​ c ≪ H ​ S / d n^{\prime\prime}/bc\ll HS/d, so

 | ∥ b ~ ( n ′′) ∥ 2 2 [t ≠ 0] \displaystyle\|\underset{[t\neq 0]}{\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}} | ≪ x o ⁡ ( 1) ​ ∑ d ≪ S ∑ g ≍ d ​ H / S ∑ n ′′ ​ d / b ​ H ​ S ≪ c ≪ F c | n ′′ ( H ​ S / d n ′′ / b ​ c + 1) ​ H ​ S d ​ F c \displaystyle\ll x^{o(1)}\sum_{d\ll S}\sum_{g\asymp dH/S}\sum_{\begin{subarray}{c}n^{\prime\prime}d/bHS\ll c\ll F\\ c\mid n^{\prime\prime}\end{subarray}}\Big(\frac{HS/d}{n^{\prime\prime}/bc}+1\Big)\frac{HS}{d}\frac{F}{c} |  |

 |  | ≪ x o ⁡ ( 1) ​ ∑ d ≪ S ∑ g ≍ d ​ H / S ( d, n ′′) d 2 ​ n ′′ ​ ( H ​ S) 2 ​ F \displaystyle\ll x^{o(1)}\sum_{d\ll S}\sum_{g\asymp dH/S}\frac{(d,n^{\prime\prime})}{d^{2}n^{\prime\prime}}(HS)^{2}F |  |

(5.12) |  |  | ≪ x o ⁡ ( 1) ​ H 3 ​ S ​ F n ′′ ​ ∑ d ≪ S ( d, n ′′) d ≪ x o ⁡ ( 1) ​ H 3 ​ S ​ F n ′′ ​ ∑ b | n ′′ ∑ d ′ ≪ S / b 1 d ′ ≪ x o ⁡ ( 1) ​ H 3 ​ S ​ F n ′′ \displaystyle\ll x^{o(1)}H^{3}S\frac{F}{n^{\prime\prime}}\sum_{d\ll S}\frac{(d,n^{\prime\prime})}{d}\ll x^{o(1)}H^{3}S\frac{F}{n^{\prime\prime}}\sum_{b\mid n^{\prime\prime}}\sum_{d^{\prime}\ll S/b}\frac{1}{d^{\prime}}\ \ll\ x^{o(1)}H^{3}S\frac{F}{n^{\prime\prime}} |  |

by the divisor bound. Note S > N ​ R 2 ​ S 2 / M > H S>NR^{2}S^{2}/M>H, since M > N ​ R 2 ​ S M>NR^{2}S by ( 5.6). Thus ( H ​ S) 2 > H 3 ​ S (HS)^{2}>H^{3}S, and so ( 5) and ( 5) give

(5.13) |  | ‖ b ~ ​ ( n ′′) ‖ 2 2 \displaystyle\|\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2} | ≪ ‖ b ~ ( n ′′) ∥ 2 2 [t = 0] + ‖ ​ b ~ ( n ′′) ∥ 2 2 [t ≠ 0] ≪ x o ⁡ ( 1) ​ ( H ​ S) 2 ​ F n ′′. \displaystyle\ll\|\underset{[t=0]}{\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}}+\|\underset{[t\neq 0]}{\tilde{\textbf{b}}(n^{\prime\prime})\|_{2}^{2}}\ \ll\ x^{o(1)}(HS)^{2}\frac{F}{n^{\prime\prime}}. |  |

In particular, for n ′′ = 1 n^{\prime\prime}=1 we have ‖ b ‖ 2 2 = ‖ b ~ ​ ( 1) ‖ 2 2 ≪ x o ⁡ ( 1) ​ ( H ​ S) 2 ​ F \|\textbf{b}\|_{2}^{2}=\|\tilde{\textbf{b}}(1)\|_{2}^{2}\ll x^{o(1)}(HS)^{2}F.

Plugging back into ( 5), we obtain

 | 𝒥 2 ​ x − o ⁡ ( 1) \displaystyle\mathcal{J}^{2}\,x^{-o(1)} | ≪ a θ ​ ( C ​ B ​ Z + a ​ Y) ​ Z ​ ∑ n ′′ | a ∞ n ′′ ≤ 2 ​ Y ( n ′′) θ ​ ( H ​ S) 2 ​ F n ′′ + ( C 1 + 2 ​ θ ​ B ​ Z 2 − 2 ​ θ + B 2 ​ Y ​ Z) ​ ( H ​ S) 2 ​ F \displaystyle\ll a^{\theta}\Big(CBZ+aY\Big)Z\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\leq 2Y\end{subarray}}(n^{\prime\prime})^{\theta}(HS)^{2}\frac{F}{n^{\prime\prime}}\ +\ \Big(C^{1+2{\theta}}BZ^{2-2{\theta}}+B^{2}YZ\Big)(HS)^{2}F |  |

 |  | ≪ [a θ ​ ( C ​ B ​ Z + x 1 + ϵ ​ Y) + ( C 1 + 2 ​ θ ​ B ​ Z 1 − 2 ​ θ + B 2 ​ Y)] ​ Z ​ ( H ​ S) 2 ​ F \displaystyle\ll\bigg[a^{\theta}\big(CBZ+x^{1+\epsilon}Y\big)+\Big(C^{1+2{\theta}}BZ^{1-2{\theta}}+B^{2}Y\Big)\bigg]Z(HS)^{2}F |  |

using a ​ Y ≪ x 1 + ϵ ​ Y aY\ll x^{1+\epsilon}Y, and ∑ n ′′ ( n ′′) θ − 1 ≪ x ϵ \sum_{n^{\prime\prime}}(n^{\prime\prime})^{\theta-1}\ll x^{\epsilon}.

Next, observe C ​ B ​ Z < x ​ Y CBZ<xY: Indeed, to see this, we have C ​ B ​ Z = ( N ​ R ​ S) ​ ( N ​ R) ​ ( S 2) = N 2 ​ R 2 ​ S 3 CBZ=(NRS)(NR)(S^{2})=N^{2}R^{2}S^{3} and x ​ Y = x ⁡ ( N ​ R 2 ​ S 3 / M) = x ​ N ​ R 2 ​ S 5 / M ≍ N 2 ​ R 2 ​ S 5 xY=x(NR^{2}S^{3}/M)=xNR^{2}S^{5}/M\asymp N^{2}R^{2}S^{5}. By ( 5.6), B 2 = N 2 ​ R 2 < x B^{2}=N^{2}R^{2}<x and so B 2 ​ Y < x ​ Y B^{2}Y<xY. Thus we obtain

(5.14) |  | 𝒥 2 \displaystyle\mathcal{J}^{2} | ≪ x ϵ ​ [a θ ​ x ​ Y + C ​ B ​ Z ​ ( C / Z) 2 ​ θ] ​ Z ​ ( H ​ S) 2 ​ F. \displaystyle\ll x^{\epsilon}\bigg[a^{\theta}xY+CBZ(C/Z)^{2{\theta}}\bigg]Z(HS)^{2}F. |  |

Thus 𝒲 k ≠ 0 2 < x ϵ ​ 𝒥 2 \mathcal{W}_{k\neq 0}^{2}<x^{\epsilon}\mathcal{J}^{2} is less than ( N 2 ​ R 2 ​ S 3 ​ x − 6 ​ ϵ) 2 (N^{2}R^{2}S^{3}x^{-6\epsilon})^{2}, provided

 | [a θ ​ x ​ Y + C ​ B ​ Z ​ ( C / Z) 2 ​ θ] < ( N 2 ​ R 2 ​ S 3 x 7 ​ ϵ ​ H ​ S) 2 / Z ​ F \displaystyle\bigg[a^{\theta}xY+CBZ(C/Z)^{2{\theta}}\bigg]<\Big(\frac{N^{2}R^{2}S^{3}}{x^{7\epsilon}HS}\Big)^{2}/ZF | = ( N 2 ​ R 2 ​ S 2 x 7 ​ ϵ ​ Q ​ R 2 ​ S 2 / M) 2 / ( S 2 ​ N / Q) \displaystyle=\Big(\frac{N^{2}R^{2}S^{2}}{x^{7\epsilon}QR^{2}S^{2}/M}\Big)^{2}/(S^{2}N/Q) |  |

 |  | = ( N 2 ​ M x 7 ​ ϵ ​ Q ​ S) 2 ​ Q N ≍ N ​ x 2 − 14 ​ ϵ Q ​ S 2. \displaystyle=\Big(\frac{N^{2}M}{x^{7\epsilon}QS}\Big)^{2}\frac{Q}{N}\asymp\frac{Nx^{2-14\epsilon}}{QS^{2}}. |  |

This is equivalent to the inequalities

 | N ​ x 2 − 14 ​ ϵ Q ​ S 2 \displaystyle\frac{Nx^{2-14\epsilon}}{QS^{2}} | > a θ ​ x ​ Y = a θ ​ x ​ N 2 ​ R 2 ​ S 3 x \displaystyle>a^{\theta}xY=a^{\theta}x\frac{N^{2}R^{2}S^{3}}{x} |  |

 | N ​ x 2 − 14 ​ ϵ Q ​ S 2 \displaystyle\frac{Nx^{2-14\epsilon}}{QS^{2}} | > C ​ B ​ Z ​ ( C / Z) 2 ​ θ = ( N ​ R ​ S) ​ ( N ​ R) ​ ( S 2) ​ ( N ​ R ​ S S 2) 2 ​ θ = N 2 ​ R 2 ​ S 3 ​ ( N ​ R S) 2 ​ θ \displaystyle>CBZ(C/Z)^{2{\theta}}=(NRS)(NR)(S^{2})\Big(\frac{NRS}{S^{2}}\Big)^{2{\theta}}=N^{2}R^{2}S^{3}\Big(\frac{NR}{S}\Big)^{2{\theta}} |  |

Simplifying, we conclude 𝒲 k ≠ 0 < N 2 ​ R 2 ​ S 3 ​ x − 6 ​ ϵ \mathcal{W}_{k\neq 0}<N^{2}R^{2}S^{3}x^{-6\epsilon} holds provided

(5.15) |  | a θ ​ N ​ R 2 ​ S 5 ​ Q \displaystyle a^{\theta}NR^{2}S^{5}Q | < x 2 − 14 ​ ϵ, \displaystyle<x^{2-14\epsilon}, |  |

(5.16) |  | ( N ​ R / S) 2 ​ θ ​ N ​ R 2 ​ S 5 ​ Q \displaystyle(NR/S)^{2{\theta}}NR^{2}S^{5}Q | < x 2 − 14 ​ ϵ. \displaystyle<x^{2-14\epsilon}. |  |

∎

###### Proposition 5.2 (Well-factorable estimate for convolutions).

Let N ​ M ≍ x NM\asymp x, and Q 1, Q 2, Q 3 Q_{1},Q_{2},Q_{3} satisfy

 | Q 1 \displaystyle Q_{1} | < N x ϵ, \displaystyle<\frac{N}{x^{\epsilon}}, |  |

 | N 2 ​ Q 2 ​ Q 3 2 \displaystyle N^{2}Q_{2}Q_{3}^{2} | < x 1 − 8 ​ ϵ, \displaystyle<x^{1-8\epsilon}, |  |

 | a θ ​ N ​ Q 1 ​ Q 2 5 ​ Q 3 2 \displaystyle a^{\theta}\;NQ_{1}Q_{2}^{5}Q_{3}^{2} | < x 2 − 15 ​ ϵ, \displaystyle<x^{2-15\epsilon}, |  |

 | ( N ​ Q 3 / Q 2) 2 ​ θ ​ N ​ Q 1 ​ Q 2 5 ​ Q 3 2 \displaystyle(NQ_{3}/Q_{2})^{2{\theta}}\;NQ_{1}Q_{2}^{5}Q_{3}^{2} | < x 2 − 15 ​ ϵ. \displaystyle<x^{2-15\epsilon}. |  |

Let α n, β m \alpha_{n},\beta_{m} be 1 1 -bounded complex sequences such that α n \alpha_{n} satisfies the Siegel-Walfisz condition ( 2.2) and α n \alpha_{n} is supported on n n with all prime factors bigger than z 0 = x 1 / ( log ⁡ log ⁡ ( x)) 3 z_{0}=x^{1/(\log\log{x})^{3}}. Let γ q 1, λ q 2, ν q 3 \gamma_{q_{1}},\lambda_{q_{2}},\nu_{q_{3}} be 1-bounded complex coefficients supported on ( q i, a) = 1 (q_{i},a)=1 for i ∈ { 1, 2, 3 } i\in\{1,2,3\}. Let

 | Δ ⁡ ( q):= ∑ n ∼ N α n ​ ∑ m ∼ M β m ​ ( 𝟏 n ​ m ≡ a ⁡ ( mod ​ q) − 𝟏 ( n ​ m, q) = 1 φ ⁡ ( q)). \Delta(q):=\sum_{n\sim N}\alpha_{n}\sum_{m\sim M}\beta_{m}\Bigl(\mathbf{1}_{nm\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(nm,q)=1}}{{\varphi}(q)}\Bigr). |  |

Then for every A > 0 A>0 we have

 | sup 0 < | a | < x 1 + ϵ ∑ q 1 ∼ Q 1 ∑ q 2 ∼ Q 2 ∑ q 3 ∼ Q 3 γ q 1 λ q 2 ν q 3 Δ ( q 1 q 2 q 3) ≪ A x ( log ⁡ ( x)) A. \sup_{0<|a|<x^{1+\epsilon}}\sum_{q_{1}\sim Q_{1}}\sum_{q_{2}\sim Q_{2}}\sum_{q_{3}\sim Q_{3}}\gamma_{q_{1}}\lambda_{q_{2}}\nu_{q_{3}}\Delta(q_{1}q_{2}q_{3})\ll_{A}\frac{x}{(\log{x})^{A}}. |  |

###### Proof.

First we factor q 2 = q 2 ′ ​ q 2 ′′ q_{2}=q_{2}^{\prime}q_{2}^{\prime\prime} and q 3 = q 3 ′ ​ q 3 ′′ q_{3}=q_{3}^{\prime}q_{3}^{\prime\prime} where P − ​ ( q 2 ′), P − ​ ( q 3 ′) > z 0 ⩾ P + ​ ( q 2 ′′), P + ​ ( q 3 ′′) P^{-}(q_{2}^{\prime}),P^{-}(q_{3}^{\prime})>z_{0}{\,\geqslant}P^{+}(q_{2}^{\prime\prime}),P^{+}(q_{3}^{\prime\prime}) into parts with large and small prime factors. By putting these in dyadic intervals, we see that it suffices to show for every A > 0 A>0 and every choice of Q 2 ′ ​ Q 2 ′′ ≍ Q 2 Q_{2}^{\prime}Q_{2}^{\prime\prime}\asymp Q_{2}, Q 3 ′ ​ Q 3 ′′ ≍ Q 3 Q_{3}^{\prime}Q_{3}^{\prime\prime}\asymp Q_{3} that

 |  | sup 0 < | a | < x 1 + ϵ ∑ q 1 ∼ Q 1 ∑ q 2 ′ ∼ Q 2 ′ P − ​ ( q 2 ′) > z 0 ∑ q 2 ′′ ∼ Q 2 ′′ P + ​ ( q 2 ′′) ⩽ z 0 ∑ q 3 ′ ∼ Q 3 ′ P − ​ ( q 3 ′) ⩾ z 0 ∑ q 3 ′′ ∼ Q 3 ′′ P + ​ ( q 3 ′′) ⩽ z 0 γ q 1 λ q 2 ′ ​ q 2 ′′ ν q 3 ′ ​ q 3 ′′ Δ ( q 1 q 2 ′ q 2 ′′ q 3 ′ q 3 ′′) ≪ A x ( log ⁡ ( x)) A. \displaystyle\sup_{0<|a|<x^{1+\epsilon}}\sum_{q_{1}\sim Q_{1}}\sum_{\begin{subarray}{c}q_{2}^{\prime}\sim Q_{2}^{\prime}\\ P^{-}(q_{2}^{\prime})>z_{0}\end{subarray}}\sum_{\begin{subarray}{c}q_{2}^{\prime\prime}\sim Q_{2}^{\prime\prime}\\ P^{+}(q_{2}^{\prime\prime}){\,\leqslant}z_{0}\end{subarray}}\sum_{\begin{subarray}{c}q_{3}^{\prime}\sim Q_{3}^{\prime}\\ P^{-}(q_{3}^{\prime}){\,\geqslant}z_{0}\end{subarray}}\sum_{\begin{subarray}{c}q_{3}^{\prime\prime}\sim Q_{3}^{\prime\prime}\\ P^{+}(q_{3}^{\prime\prime}){\,\leqslant}z_{0}\end{subarray}}\gamma_{q_{1}}\lambda_{q_{2}^{\prime}q_{2}^{\prime\prime}}\nu_{q_{3}^{\prime}q_{3}^{\prime\prime}}\Delta(q_{1}q_{2}^{\prime}q_{2}^{\prime\prime}q_{3}^{\prime}q_{3}^{\prime\prime})\ll_{A}\frac{x}{(\log{x})^{A}}. |  |

By Lemma 4.4 we have the result unless Q 2 ′′, Q 3 ′′ ⩽ y 0 = x 1 / log ⁡ log ⁡ ( x) Q_{2}^{\prime\prime},Q_{3}^{\prime\prime}{\,\leqslant}y_{0}=x^{1/\log\log{x}}. We let d = q 2 ′′ ​ q 3 ′′ d=q_{2}^{\prime\prime}q_{3}^{\prime\prime} and define

 | λ q, d, r:= 𝟏 P − ​ ( r) > z 0 ​ ∑ q 2 ′′ ​ q 3 ′′ = d q 1 ∼ Q 1 q 2 ′′ ∼ Q 2 ′′ q 3 ′′ ∼ Q 3 ′′ P + ​ ( q 2 ′′ ​ q 3 ′′) ⩽ z 0 ∑ q 2 ′ ​ q 3 ′ = r q 2 ′ ∼ Q 2 ′ q 3 ′ ∼ Q 3 ′ λ q 2 ′ ​ q 2 ′′ ​ ν q 3 ′ ​ q 3 ′′. \lambda_{q,d,r}:=\mathbf{1}_{P^{-}(r)>z_{0}}\sum_{\begin{subarray}{c}q_{2}^{\prime\prime}q_{3}^{\prime\prime}=d\\ q_{1}\sim Q_{1}\\ q_{2}^{\prime\prime}\sim Q_{2}^{\prime\prime}\\ q_{3}^{\prime\prime}\sim Q_{3}^{\prime\prime}\\ P^{+}(q_{2}^{\prime\prime}q_{3}^{\prime\prime}){\,\leqslant}z_{0}\end{subarray}}\,\,\sum_{\begin{subarray}{c}q_{2}^{\prime}q_{3}^{\prime}=r\\ q_{2}^{\prime}\sim Q_{2}^{\prime}\\ q_{3}^{\prime}\sim Q_{3}^{\prime}\end{subarray}}\lambda_{q_{2}^{\prime}q_{2}^{\prime\prime}}\nu_{q_{3}^{\prime}q_{3}^{\prime\prime}}. |  |

We note that λ q, d, r \lambda_{q,d,r} doesn’t depend on q q. With this definition we see it suffices to show that for every A > 0 A>0 and every choice of D, R D,R with D ​ R ≍ Q 2 ​ Q 3 DR\asymp Q_{2}Q_{3} and D ⩽ y 0 2 D{\,\leqslant}y_{0}^{2} we have that

 | sup 0 < | a | < x 1 + ϵ ∑ q ∼ Q 1 ∑ d ∼ D ∑ r ∼ R γ q λ q, d, r Δ ( q d r) ≪ A x ( log ⁡ ( x)) A. \sup_{0<|a|<x^{1+\epsilon}}\sum_{q\sim Q_{1}}\sum_{d\sim D}\sum_{r\sim R}\gamma_{q}\lambda_{q,d,r}\Delta(qdr)\ll_{A}\frac{x}{(\log{x})^{A}}. |  |

We now apply Proposition 4.5 (we may apply this since N > Q 1 ​ x ϵ > Q 1 ​ D ​ ( log ⁡ ( x)) C N>Q_{1}x^{\epsilon}>Q_{1}D(\log{x})^{C} and N < x 1 − ϵ N<x^{1-\epsilon} by assumption of the lemma). This shows that it suffices to show that

 | | ℰ 1 | + | ℰ 2 | ≪ N 2 D ​ Q 1 ​ y 0, |\mathcal{E}_{1}|+|\mathcal{E}_{2}|\ll\frac{N^{2}}{DQ_{1}y_{0}}, |  |

where

 | ℰ 1 \displaystyle\mathcal{E}_{1} | : = sup 0 < | a | < x 1 + ϵ ∑ q ( q, a) = 1 ∑ d ∼ D ( d, a) = 1 ∑ r 1, r 2 ∼ R ( r 1 ​ r 2, a) = 1 ψ 0 ​ ( q Q 1) ​ λ q, d, r 1 ​ λ q, d, r 2 ¯ φ ⁡ ( q ​ d ​ r 2) ​ q ​ d ​ r 1 ​ ∑ n 1, n 2 ∼ N ( n 1, q ​ d ​ r 1) = 1 ( n 2, q ​ d ​ r 2) = 1 α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}q\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1}r_{2},a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q_{1}}\Bigr)\frac{\lambda_{q,d,r_{1}}\overline{\lambda_{q,d,r_{2}}}}{{\varphi}(qdr_{2})qdr_{1}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ (n_{1},qdr_{1})=1\\ (n_{2},qdr_{2})=1\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H 1 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1) ​ e ​ ( a ​ h ​ n 1 ¯ q ​ d ​ r 1), \displaystyle\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{1}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}}}{qdr_{1}}\Bigr), |  |

 | ℰ 2 \displaystyle\mathcal{E}_{2} | : = sup 0 < | a | < x 1 + ϵ ∑ q ( q, a) = 1 ψ 0 ​ ( q Q 1) ​ ∑ d ∼ D ( d, a) = 1 ∑ r 1, r 2 ∼ R ( r 1, a ​ r 2) = 1 ( r 2, a ​ q ​ d ​ r 1) = 1 λ q, d, r 1 ​ λ q, d, r 2 ¯ q ​ d ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q ​ d) ( n 1, n 2 ​ q ​ d ​ r 1) = 1 ( n 2, n 1 ​ q ​ d ​ r 2) = 1 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}q\\ (q,a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q_{1}}\Bigr)\sum_{\begin{subarray}{c}d\sim D\\ (d,a)=1\end{subarray}}\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1},ar_{2})=1\\ (r_{2},aqdr_{1})=1\end{subarray}}\frac{\lambda_{q,d,r_{1}}\overline{\lambda_{q,d,r_{2}}}}{qdr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd)\\ (n_{1},n_{2}qdr_{1})=1\\ (n_{2},n_{1}qdr_{2})=1\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H 2 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1 ​ r 2) ​ e ​ ( a ​ h ​ n 1 ​ r 2 ¯ q ​ d ​ r 1 + a ​ h ​ n 2 ​ q ​ d ​ r 1 ¯ r 2), \displaystyle\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{2}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}r_{2}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}r_{2}}}{qdr_{1}}+\frac{ah\overline{n_{2}qdr_{1}}}{r_{2}}\Bigr), |  |

 | H 1 \displaystyle H_{1} | : = Q ​ D ​ R M ​ log 5 ​ x, \displaystyle:=\frac{QDR}{M}\log^{5}{x}, |  |

 | H 2 \displaystyle H_{2} | : = Q ​ D ​ R 2 M ​ log 5 ​ x. \displaystyle:=\frac{QDR^{2}}{M}\log^{5}{x}. |  |

Since λ q, d, r \lambda_{q,d,r} is independent of q q, we may apply Lemma 4.7 to conclude that

 | ℰ 1 ≪ N 2 Q 1 ​ D ​ x ϵ, \mathcal{E}_{1}\ll\frac{N^{2}}{Q_{1}Dx^{\epsilon}}, |  |

provided we have

(5.17) |  | D ​ R ​ N 3 / 2 \displaystyle DRN^{3/2} | < x 1 − 2 ​ ϵ, \displaystyle<x^{1-2\epsilon}, |  |

(5.18) |  | Q 1 ​ D ​ R \displaystyle Q_{1}DR | < x 1 − 2 ​ ϵ. \displaystyle<x^{1-2\epsilon}. |  |

These are both implied by the conditions of the lemma, recalling that D ​ R ≍ Q 2 ​ Q 3 DR\asymp Q_{2}Q_{3}.

Thus it remains to bound ℰ 2 \mathcal{E}_{2}. Since D ⩽ y 0 2 = x o ⁡ ( 1) D{\,\leqslant}y_{0}^{2}=x^{o(1)}, it suffices to show

 | ℰ 3 ≪ N 2 Q 1 ​ x ϵ / 10, \mathcal{E}_{3}\ll\frac{N^{2}}{Q_{1}x^{\epsilon/10}}, |  |

for each d ⩽ y 0 2 d{\,\leqslant}y_{0}^{2}, where ℰ 3 = ℰ 3 ​ ( d) \mathcal{E}_{3}=\mathcal{E}_{3}(d) is given by

 | ℰ 3 \displaystyle\mathcal{E}_{3} | : = sup 0 < | a | < x 1 + ϵ ∑ ( q, a) = 1 ψ 0 ​ ( q Q 1) ​ ∑ r 1, r 2 ∼ R ( r 1, a ​ r 2) = 1 ( r 2, a ​ q ​ d ​ r 1) = 1 λ q, d, r 1 ​ λ q, d, r 2 ¯ q ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q ​ d) ( n 1, n 2 ​ q ​ d ​ r 1) = 1 ( n 2, n 1 ​ q ​ d ​ r 2) = 1 | n 1 − n 2 | ⩾ N / ( log ⁡ ( x)) C α n 1 ​ α n 2 ¯ \displaystyle:=\sup_{0<|a|<x^{1+\epsilon}}\sum_{\begin{subarray}{c}(q,a)=1\end{subarray}}\psi_{0}\Bigl(\frac{q}{Q_{1}}\Bigr)\sum_{\begin{subarray}{c}r_{1},r_{2}\sim R\\ (r_{1},ar_{2})=1\\ (r_{2},aqdr_{1})=1\end{subarray}}\frac{\lambda_{q,d,r_{1}}\overline{\lambda_{q,d,r_{2}}}}{qr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd)\\ (n_{1},n_{2}qdr_{1})=1\\ (n_{2},n_{1}qdr_{2})=1\\ |n_{1}-n_{2}|{\,\geqslant}N/(\log{x})^{C}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}} |  |

 |  | × ∑ 1 ⩽ | h | ⩽ H 2 ψ ^ 0 ​ ( h ​ M q ​ d ​ r 1 ​ r 2) ​ e ​ ( a ​ h ​ n 1 ​ r 2 ¯ q ​ d ​ r 1 + a ​ h ​ n 2 ​ q ​ d ​ r 1 ¯ r 2). \displaystyle\qquad\qquad\times\sum_{1{\,\leqslant}|h|{\,\leqslant}H_{2}}\hat{\psi}_{0}\Bigl(\frac{hM}{qdr_{1}r_{2}}\Bigr)e\Bigl(\frac{ah\overline{n_{1}r_{2}}}{qdr_{1}}+\frac{ah\overline{n_{2}qdr_{1}}}{r_{2}}\Bigr). |  |

Since λ q, d, r \lambda_{q,d,r} is independent of q q and we treat each d d separately, we may suppress the q, d q,d dependence by writing λ r \lambda_{r} in place of λ q, d, r \lambda_{q,d,r}. We now apply Lemma 4.6. This shows it suffices to show that

 | sup 0 < | a | < x 1 + ϵ R 1, R 2 ⩽ 2 ​ R sup H ′ ⩽ H Q ′ ⩽ 2 ​ Q ℰ ′ ≪ N 2 Q 1 ​ x ϵ / 2, \sup_{\begin{subarray}{c}0<|a|<x^{1+\epsilon}\\ R_{1},R_{2}{\,\leqslant}2R\end{subarray}}\sup_{\begin{subarray}{c}H^{\prime}{\,\leqslant}H\\ Q^{\prime}{\,\leqslant}2Q\end{subarray}}\mathcal{E}^{\prime}\ll\frac{N^{2}}{Q_{1}x^{\epsilon/2}}, |  |

where

 | ℰ ′:= ∑ Q 1 ⩽ q ⩽ Q 1 ′ ( q, a) = 1 ∑ R ⩽ r 1 ⩽ R 1 R ⩽ r 2 ⩽ R 2 ( r 1, a ​ r 2) = 1 ( r 2, a ​ q ​ d ​ r 1) = 1 λ r 1 ​ λ r 2 ¯ q ​ d ​ r 1 ​ r 2 ​ ∑ n 1, n 2 ∼ N n 1 ≡ n 2 ​ ( mod ​ q ​ d) ( n 1, q ​ d ​ r 1 ​ n 2) = 1 ( n 2, q ​ d ​ r 2 ​ n 1) = 1 ( n 1 ​ r 2, n 2) ∈ 𝒩 α n 1 ​ α n 2 ¯ ​ ∑ 1 ⩽ | h | ⩽ H ′ e ⁡ ( a ​ h ​ n 2 ​ q ​ d ​ r 1 ¯ ​ ( n 1 − n 2) n 1 ​ r 2). \mathcal{E}^{\prime}:=\sum_{\begin{subarray}{c}Q_{1}{\,\leqslant}q{\,\leqslant}Q_{1}^{\prime}\\ (q,a)=1\end{subarray}}\sum_{\begin{subarray}{c}R{\,\leqslant}r_{1}{\,\leqslant}R_{1}\\ R{\,\leqslant}r_{2}{\,\leqslant}R_{2}\\ (r_{1},ar_{2})=1\\ (r_{2},aqdr_{1})=1\end{subarray}}\frac{\lambda_{r_{1}}\overline{\lambda_{r_{2}}}}{qdr_{1}r_{2}}\sum_{\begin{subarray}{c}n_{1},n_{2}\sim N\\ n_{1}\equiv n_{2}\ (\mathrm{mod}\ qd)\\ (n_{1},qdr_{1}n_{2})=1\\ (n_{2},qdr_{2}n_{1})=1\\ (n_{1}r_{2},n_{2})\in\mathcal{N}\end{subarray}}\alpha_{n_{1}}\overline{\alpha_{n_{2}}}\sum_{1{\,\leqslant}|h|{\,\leqslant}H^{\prime}}e\Bigl(\frac{ah\overline{n_{2}qdr_{1}}(n_{1}-n_{2})}{n_{1}r_{2}}\Bigr). |  |

We recall the definition of λ q, d, r \lambda_{q,d,r} and expand it as a sum. Since d d is fixed, there are x o ⁡ ( 1) x^{o(1)} possible choices of q 2 ′′, q 3 ′′ q_{2}^{\prime\prime},q_{3}^{\prime\prime}. Fixing one such choice, we then see ℰ ′ \mathcal{E}^{\prime} is precisely of the form considered in Lemma 5.1. This then gives the result, provided

 | Q 1 \displaystyle Q_{1} | < N x ϵ, \displaystyle<\frac{N}{x^{\epsilon}}, |  |

 | N 2 Q 2 ′ Q 3 ′ 2 \displaystyle N^{2}Q_{2}^{\prime}Q_{3}^{\prime}{}^{2} | < x 1 − 7 ​ ϵ, \displaystyle<x^{1-7\epsilon}, |  |

 | a θ N Q 1 Q 2 ′ 5 Q 3 ′ 2 \displaystyle a^{\theta}\;NQ_{1}Q_{2}^{\prime}{}^{5}Q_{3}^{\prime}{}^{2} | < x 2 − 14 ​ ϵ, \displaystyle<x^{2-14\epsilon}, |  |

 | ( N Q 3 ′ / Q 2 ′) 2 ​ θ N Q 1 Q 2 ′ Q 3 ′ 5 2 \displaystyle(NQ_{3}^{\prime}/Q_{2}^{\prime})^{2{\theta}}\;NQ_{1}Q_{2}^{\prime}{}^{5}Q_{3}^{\prime}{}^{2} | < x 2 − 14 ​ ϵ. \displaystyle<x^{2-14\epsilon}. |  |

Since Q 2 ′ ⩽ Q 2 Q_{2}^{\prime}{\,\leqslant}Q_{2} and Q 3 ′ ⩽ Q 3 Q_{3}^{\prime}{\,\leqslant}Q_{3}, these bounds follow from the assumptions of the lemma. ∎

###### Proof of Proposition 3.1.

First we note that by Lemma 4.1 the set of n, m n,m with max ⁡ ( | α n |, | β m |) \max(|\alpha_{n}|,|\beta_{m}|) ⩾ ( log ⁡ ( x)) C {\,\geqslant}(\log{x})^{C} and n ​ m ≡ a ⁡ ( mod ​ q) nm\equiv a\ (\mathrm{mod}\ q) has size ≪ x ​ ( log ⁡ ( x)) O B 0 ​ ( 1) − C / q \ll x(\log{x})^{O_{B_{0}}(1)-C}/q, so these terms contribute negligibly if C = C ⁡ ( A, B 0) C=C(A,B_{0}) is large enough. Thus, by dividing through by ( log ⁡ ( x)) 2 ​ C (\log{x})^{2C} and considering A + 2 ​ C A+2C in place of A A, it suffices to show the result when all the sequences are 1-bounded. ( α n \alpha_{n} still satisfies ( 2.2) by Lemma 4.3.) The result follows from the Bombieri-Vinogradov Theorem if Q ⩽ x 1 / 2 − ϵ Q{\,\leqslant}x^{1/2-\epsilon}, so we may assume that Q ∈ [x 1 / 2 − ϵ, x 5 / 8 − 10 ​ ϵ] Q\in[x^{1/2-\epsilon},x^{5/8-10\epsilon}].

We use Lemma 4.2 to remove the condition n ​ m ∈ ℐ nm\in\mathcal{I}, and see suffices to show for B = B ⁡ ( A) B=B(A) sufficiently large in terms of A A

(5.19) |  | sup 0 < | a | < x 1 + ϵ ∑ q ⩽ Q λ q ∑ n ∈ ℐ N α n ∑ m ∈ ℐ M β m ( 𝟏 n ​ m ≡ a ⁡ ( mod ​ q) − 𝟏 ( n ​ m, q) = 1 φ ⁡ ( q)) ≪ B x ( log ⁡ ( x)) B \sup_{0<|a|<x^{1+\epsilon}}\sum_{q{\,\leqslant}Q}\lambda_{q}\sum_{n\in\mathcal{I}_{N}}\alpha_{n}\sum_{\begin{subarray}{c}m\in\mathcal{I}_{M}\end{subarray}}\beta_{m}\Bigl(\mathbf{1}_{nm\equiv a\ (\mathrm{mod}\ q)}-\frac{\mathbf{1}_{(nm,q)=1}}{{\varphi}(q)}\Bigr)\ll_{B}\frac{x}{(\log{x})^{B}} |  |

uniformly over all intervals ℐ N ⊆ [N, 2 ​ N] \mathcal{I}_{N}\subseteq[N,2N] and ℐ M ⊆ [M, 2 ​ M] \mathcal{I}_{M}\subseteq[M,2M].

Write Q = x ϑ Q=x^{\boldsymbol{\vartheta}} and take v ∈ [.35,.50] v\in[.35,.50] to be determined. Let us define for x ϵ ⩽ N ⩽ x 1 / 3 + ϵ x^{\epsilon}{\,\leqslant}N{\,\leqslant}x^{1/3+\epsilon}

 | Q 1:= N x ϵ, Q 2:= x ϑ − v + ϵ, Q 3:= x v N. Q_{1}:=\frac{N}{x^{\epsilon}},\qquad Q_{2}:=x^{{\boldsymbol{\vartheta}}-v+\epsilon},\qquad Q_{3}:=\frac{x^{v}}{N}. |  |

We note that Q 1 ​ Q 2 ​ Q 3 = x ϑ Q_{1}Q_{2}Q_{3}=x^{\boldsymbol{\vartheta}} and Q 1, Q 2, Q 3 ⩾ 1 Q_{1},Q_{2},Q_{3}{\,\geqslant}1. Since λ q \lambda_{q} is triply well-factorable of level Q = x ϑ Q=x^{\boldsymbol{\vartheta}}, we can write

(5.20) |  | λ q = ∑ q 1 ​ q 2 ​ q 3 = q γ q 1 ( 1) ​ γ q 2 ( 2) ​ γ q 3 ( 3), \lambda_{q}=\sum_{q_{1}q_{2}q_{3}=q}\gamma^{(1)}_{q_{1}}\gamma^{(2)}_{q_{2}}\gamma^{(3)}_{q_{3}}, |  |

for some 1-bounded sequences γ ( 1), γ ( 2), γ ( 3) \gamma^{(1)},\gamma^{(2)},\gamma^{(3)} with γ q ( i) \gamma^{(i)}_{q} supported on q ⩽ Q i q{\,\leqslant}Q_{i} for i ∈ { 1, 2, 3 } i\in\{1,2,3\}.

We now substitute ( 5.20) into ( 5.19) and put each of q 1, q 2, q 3 q_{1},q_{2},q_{3} into one of O ⁡ ( log 3 ​ x) O(\log^{3}{x}) dyadic intervals ( Q 1 ′, 2 ​ Q 1 ′] (Q_{1}^{\prime},2Q_{1}^{\prime}], ( Q 2 ′, 2 ​ Q 2 ′] (Q_{2}^{\prime},2Q_{2}^{\prime}] and ( Q 3 ′, 2 ​ Q 3 ′] (Q_{3}^{\prime},2Q_{3}^{\prime}] respectively. Since Q 1 ′ ⩽ Q 1 Q_{1}^{\prime}{\,\leqslant}Q_{1}, Q 2 ′ ⩽ Q 2 Q_{2}^{\prime}{\,\leqslant}Q_{2} and Q 3 ′ ⩽ Q 3 Q_{3}^{\prime}{\,\leqslant}Q_{3} and Q 1 ​ Q 2 ​ Q 3 = Q = x ϑ Q_{1}Q_{2}Q_{3}=Q=x^{\boldsymbol{\vartheta}} we have

 | Q 1 ′ \displaystyle Q_{1}^{\prime} | ⩽ N x ϵ, \displaystyle{\,\leqslant}\frac{N}{x^{\epsilon}}, |  |

 | N 2 Q 2 ′ Q 3 ′ 2 \displaystyle N^{2}Q_{2}^{\prime}Q_{3}^{\prime}{}^{2} | ⩽ Q 2 Q 2 ​ x ϵ ⩽ Q ​ x v + ϵ < x 1 − 7 ​ ϵ, \displaystyle{\,\leqslant}\frac{Q^{2}}{Q_{2}}x^{\epsilon}{\,\leqslant}Qx^{v+\epsilon}<x^{1-7\epsilon}, |  |

 | a θ N Q 1 ′ Q 2 ′ 5 Q 3 ′ 2 \displaystyle a^{\theta}\;NQ_{1}^{\prime}Q_{2}^{\prime}{}^{5}Q_{3}^{\prime}{}^{2} | ⩽ a θ ​ N 2 ​ Q 2 5 ​ Q 3 2 ⩽ a θ ​ Q 2 ​ Q 2 3 \displaystyle{\,\leqslant}a^{\theta}\;N^{2}Q_{2}^{5}Q_{3}^{2}{\,\leqslant}a^{\theta}\;Q^{2}Q_{2}^{3} |  |

 |  | = x α ​ θ ​ Q 5 x 3 ​ v − 3 ​ ϵ < x 2 − 14 ​ ϵ \displaystyle\ =\frac{x^{\alpha\theta}\;Q^{5}}{x^{3v-3\epsilon}}<x^{2-14\epsilon} |  |

since | a | θ ≪ x α ​ θ |a|^{\theta}\ll x^{\alpha\theta}, as well as,

 | ( N Q 3 ′ / Q 2 ′) 2 ​ θ N Q 1 ′ Q 2 ′ Q 3 ′ 5 2 \displaystyle(NQ_{3}^{\prime}/Q_{2}^{\prime})^{2{\theta}}\;NQ_{1}^{\prime}Q_{2}^{\prime}{}^{5}Q_{3}^{\prime}{}^{2} | ⩽ ( x 2 ​ v / Q) 2 ​ θ ​ Q 5 x 3 ​ v − 3 ​ ϵ \displaystyle{\,\leqslant}(x^{2v}/Q)^{2{\theta}}\;\frac{Q^{5}}{x^{3v-3\epsilon}} |  |

 |  | = Q 5 − 2 ​ θ ​ x v ⁡ ( 4 ​ θ − 3) + 3 ​ ϵ < x 2 − 14 ​ ϵ \displaystyle\ =Q^{5-2{\theta}}x^{v(4{\theta}-3)+3\epsilon}<x^{2-14\epsilon} |  |

provided

 | ϑ + v \displaystyle{\boldsymbol{\vartheta}}+v | < 1 − 8 ​ ϵ, \displaystyle<1-8\epsilon, |  |

 | α ​ θ + 5 ​ ϑ − 3 ​ v \displaystyle\alpha\theta+5{\boldsymbol{\vartheta}}-3v | < 2 − 17 ​ ϵ \displaystyle<2-17\epsilon |  |

 | ϑ ⁡ ( 5 − 2 ​ θ) + v ⁡ ( 4 ​ θ − 3) \displaystyle{\boldsymbol{\vartheta}}(5-2{\theta})+v(4{\theta}-3) | < 2 − 17 ​ ϵ \displaystyle<2-17\epsilon |  |

Choosing v = 1 − ϑ − 9 ​ ϵ v=1-{\boldsymbol{\vartheta}}-9\epsilon, this simplifies as

 | α ​ θ + 8 ​ ϑ \displaystyle\alpha\theta+8{\boldsymbol{\vartheta}} | < 5 − 44 ​ ϵ, \displaystyle<5-44\epsilon, |  |

 | ϑ ⁡ ( 8 − 6 ​ θ) \displaystyle{\boldsymbol{\vartheta}}(8-6{\theta}) | < 5 − 4 ​ θ − 44 ​ ϵ \displaystyle<5-4{\theta}-44\epsilon |  |

Thus for ϑ = min ⁡ ( 5 − 4 ​ θ 8 − 6 ​ θ, 5 − α ​ θ 8) {\boldsymbol{\vartheta}}=\min(\frac{5-4{\theta}}{8-6{\theta}},\,\frac{5-\alpha\theta}{8}), we see that Proposition 5.2 now gives the result.

Note such ϑ ∈ [.57,.625] {\boldsymbol{\vartheta}}\in[.57,.625] by θ ⩽ 7 32 {\theta}{\,\leqslant}\frac{7}{32}, in particular v = 1 − ϑ − 9 ​ ϵ ∈ [.35,.5] v=1-{\boldsymbol{\vartheta}}-9\epsilon\in[.35,.5] as desired. ∎

We have now established both Proposition 3.2 and Proposition 3.1, thereby completing the proof of Theorem 1.7.

## 6. Factorization of well-factorable support

For ϑ ∈ [1 2, 1] {\boldsymbol{\vartheta}}\in[\tfrac{1}{2},1], let D = x ϑ − 2 ​ δ D=x^{{\boldsymbol{\vartheta}}-2\delta} In this section, we establish a suitable factorization of the integers d d in the well-factorable support 𝒟 well \mathcal{D}^{\textnormal{well}},

(6.1) |  | 𝒟 well ( D) = { d = p 1 ⋯ p r: p 1 ⋯ p m − 1 p m 2 < D for all m ⩽ r }. \displaystyle\mathcal{D}^{\textnormal{well}}(D)\ =\ \big\{\,d=p_{1}\cdots p_{r}\ :\ p_{1}\cdots p_{m-1}p_{m}^{2}<D\quad{\rm for\ all}\ \ m{\,\leqslant}r\big\}. |  |

This will serve as the key technical input for the proof of Theorems 1.1 and 1.2, since 𝒟 well \mathcal{D}^{\textnormal{well}} contains the support for the (upper and lower bound) linear sieve weights.

Let us define

(6.2) |  | ϑ ⁡ ( t) = ϑ α ​ ( t) \displaystyle{\boldsymbol{\vartheta}}(t)={\boldsymbol{\vartheta}}_{\alpha}(t) | : = min ⁡ ( 1 + t 2, 1 − ( 3 / 2 − 2 ​ θ) ​ t 1 + θ, 1 − α ​ θ + 3 ​ t 2). \displaystyle:=\min\Big(\frac{1+t}{2},\ \frac{1-(3/2-2{\theta})t}{1+{\theta}},\ 1-\frac{\alpha\theta+3t}{2}\Big). |  |

Observe ϑ ⁡ ( t) {\boldsymbol{\vartheta}}(t) is a unimodal function of t t, with maximum at the balance point μ \mu, given by μ = min ⁡ ( 1 − θ 4 − 3 ​ θ, 1 − α ​ θ 4) \mu=\min(\frac{1-{\theta}}{4-3{\theta}},\,\frac{1-\alpha\theta}{4}), so we may express ϑ ⁡ ( t) {\boldsymbol{\vartheta}}(t) as

 | ϑ ⁡ ( t) \displaystyle{\boldsymbol{\vartheta}}(t) | = { min ⁡ ( 1 − ( 3 / 2 − 2 ​ θ) ​ t 1 + θ, 1 − α ​ θ + 3 ​ t 2) if t > μ, 1 + t 2 if t ⩽ μ. \displaystyle=\begin{cases}\min\big(\frac{1-(3/2-2{\theta})t}{1+{\theta}},\ 1-\frac{\alpha\theta+3t}{2}\big)&\text{if}\ \ t>\mu,\\ \frac{1+t}{2}&\text{if}\ \ t{\,\leqslant}\,\mu.\end{cases} |  |

###### Proposition 6.1.

Let 0 < δ < 10 − 5 0<\delta<10^{-5} and A ∈ [x δ, x 1 / 3 − δ / 2] A\in[x^{\delta},x^{1/3-\delta/2}]. Let p 1 ⩾ ⋯ ⩾ p r p_{1}{\,\geqslant}\cdots{\,\geqslant}p_{r} be primes and write p i = x t i p_{i}=x^{t_{i}}. If d = p 1 ⋯ p r ∈ 𝒟 well ( x ϑ − 2 ​ δ) d=p_{1}\cdots p_{r}\in\mathcal{D}^{\textnormal{well}}(x^{{\boldsymbol{\vartheta}}-2\delta}), then there is a factorization d = a ​ b ​ c d=abc such that a ⩽ A a{\,\leqslant}A and

(6.3) |  | A 2 ​ b ​ c 2 ⩽ x 1 − 3 ​ δ, x α ​ θ ​ A ​ a ​ b 5 ​ c 2 ⩽ x 2 − 3 ​ δ, ( A ​ c / b) 2 ​ θ ​ A ​ a ​ b 5 ​ c 2 ⩽ x 2 − 2 ​ δ, \begin{split}A^{2}\ bc^{2}&\ {\,\leqslant}\ x^{1-3\delta},\\ x^{\alpha\theta}Aab^{5}c^{2}&\ {\,\leqslant}\ x^{2-3\delta},\\ (Ac/b)^{2{\theta}}\,Aab^{5}c^{2}&\ {\,\leqslant}\ x^{2-2\delta},\end{split} |  |

provided

 | ϑ ⩽ ϑ ⁡ ( t 1), \displaystyle{\boldsymbol{\vartheta}}\ {\,\leqslant}\ {\boldsymbol{\vartheta}}(t_{1}), |  |

for ϑ ⁡ ( t) {\boldsymbol{\vartheta}}(t) as in ( 6.2). Moreover if t 1 ⩽ μ:= min ⁡ ( 1 − θ 4 − 3 ​ θ, 1 − α ​ θ 4) t_{1}{\,\leqslant}\,\mu:=\min(\frac{1-{\theta}}{4-3{\theta}},\,\frac{1-\alpha\theta}{4}), then it suffices that

 | ϑ ⩽ ϑ ( t 1, t 2, t 3):= max { ϑ ( t 1) \displaystyle{\boldsymbol{\vartheta}}\ {\,\leqslant}\ {\boldsymbol{\vartheta}}(t_{1},t_{2},t_{3}):=\max\Big\{{\boldsymbol{\vartheta}}(t_{1}) | , ϑ ( t 2), ϑ ( t 1 + t 2), ϑ ( t 1 + t 2 + t 3), w ( t 1, t 2, t 3), w ( t 1, t 3, t 2) \displaystyle,\,{\boldsymbol{\vartheta}}(t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}+t_{3}),\,w(t_{1},t_{2},t_{3}),\,w(t_{1},t_{3},t_{2}) |  |

(6.4) |  |  | ψ ( ϑ ( t 1 + t 3), t 1 + 2 t 2 + t 3), ψ ( ϑ ( t 2 + t 3), 2 t 1 + t 2 + t 3) }, \displaystyle\ \ \psi\big({\boldsymbol{\vartheta}}(t_{1}+t_{3}),\,t_{1}+2t_{2}+t_{3}\big),\ \psi\big({\boldsymbol{\vartheta}}(t_{2}+t_{3}),\,2t_{1}+t_{2}+t_{3}\big)\Big\}, |  |

where ψ ⁡ ( x, y):= x ⋅ 𝟏 x ⩾ y \psi(x,y):=x\cdot{\mathbf{1}}_{x{\,\geqslant}y} and

 | w ⁡ ( t 1, t 2, t 3) \displaystyle w(t_{1},t_{2},t_{3}) | = ψ ⁡ ( min ⁡ { ( 5 − 4 ​ θ) − ( 3 − 4 ​ θ) ​ t 3 8 − 6 ​ θ, 5 − α ​ θ − 3 ​ t 3 8, 1 − 2 ​ t 2 }, 1 + t 1 2). \displaystyle=\psi\Big(\min\Big\{\;\frac{(5-4{\theta})-(3-4{\theta})t_{3}}{8-6{\theta}},\;\frac{5-{\alpha\theta}-3t_{3}}{8},\;1-2t_{2}\Big\},\,\frac{1+t_{1}}{2}\Big). |  |

###### Remark 6.2.

Using Selberg’s bound θ = 1 2 {\theta}=\frac{1}{2}, the result recovers Corollary 3.8 from [25].

For notational ease we are using A = N ​ x − δ A=Nx^{-\delta}. Also, on the first attempt working through technicalities, we encourage the reader to set δ = 0 \delta=0 in order to better view the key features.

Before proving the proposition, we need some lemmas. The first gives a general-purpose criterion to factor an integer d d.

###### Lemma 6.3.

Let D = x ϑ − 2 ​ δ D=x^{{\boldsymbol{\vartheta}}-2\delta} for ϑ < 5 8 {\boldsymbol{\vartheta}}<\frac{5}{8}. If d = a ​ b ​ c d=abc factors for some a, b, c ⩾ 1 a,b,c{\,\geqslant}1, with

(6.5) |  | a ⩽ A, c ⩽ D / A ​ b, b ∈ [x v, x u], \displaystyle a{\,\leqslant}A,\quad c{\,\leqslant}D/Ab,\quad b\in[x^{v},x^{u}], |  |

then factorization d = a ​ b ​ c d=abc satisfies ( 6.3). Here the *critical interval*[x v, x u] [x^{v},x^{u}] is defined by

(6.6) |  | v:= 2 ​ ϑ − 1 and u:= min ⁡ ( 1 − ( 1 + θ) ​ ϑ 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ − α ​ θ 3). \displaystyle v:=2{\boldsymbol{\vartheta}}-1\qquad{\rm and}\qquad u:=\min\Big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}-{\alpha\theta}}{3}\Big). |  |

###### Proof.

Using A ​ c ⩽ D / b Ac{\,\leqslant}D/b we have

 | A 2 ​ b ​ c 2 \displaystyle A^{2}\ bc^{2} | ⩽ D 2 / b ⩽ x 2 ​ ( ϑ − 2 ​ δ) − ( 2 ​ ϑ − 1) = x 1 − 4 ​ δ. \displaystyle\ {\,\leqslant}\ D^{2}/b{\,\leqslant}x^{2({\boldsymbol{\vartheta}}-2\delta)-(2{\boldsymbol{\vartheta}}-1)}=x^{1-4\delta}. |  |

as well as

 | ( A ​ c / b) 2 ​ θ ​ A ​ a ​ b 5 ​ c 2 ⩽ ( D / b 2) 2 ​ θ ​ D 2 ​ b 3 \displaystyle(Ac/b)^{2{\theta}}Aab^{5}c^{2}{\,\leqslant}(D/b^{2})^{2{\theta}}D^{2}b^{3} | = D 2 + 2 ​ θ ​ b 3 − 4 ​ θ \displaystyle=D^{2+2{\theta}}b^{3-4{\theta}} |  |

 |  | ⩽ x 2 − 4 ​ δ provided b 3 − 4 ​ θ ⩽ x 2 − ( 2 + 2 ​ θ) ​ ϑ. \displaystyle{\,\leqslant}\,x^{2-4\delta}\qquad\qquad\text{provided}\qquad b^{3-4{\theta}}{\,\leqslant}x^{2-(2+2{\theta}){\boldsymbol{\vartheta}}}. |  |

 | x α ​ θ ​ A ​ a ​ b 5 ​ c 2 \displaystyle x^{{\alpha\theta}}Aab^{5}c^{2} | ⩽ x α ​ θ ​ D 2 ​ b 3 \displaystyle{\,\leqslant}x^{{\alpha\theta}}D^{2}b^{3} |  |

 |  | ⩽ x 2 − 4 ​ δ provided b 3 ⩽ x 2 − 2 ​ ϑ − α ​ θ. \displaystyle{\,\leqslant}\,x^{2-4\delta}\qquad\qquad\text{provided}\qquad b^{3}{\,\leqslant}\,x^{2-2{\boldsymbol{\vartheta}}-{\alpha\theta}}. |  |

That is, b ⩽ x u b{\,\leqslant}\,x^{u} for u = min ⁡ ( 1 − ( 1 + θ) ​ ϑ 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ − α ​ θ 3) u=\min\big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}-{\alpha\theta}}{3}\big).

Hence for b ∈ [x v, x u] b\in[x^{v},x^{u}] the factorization d = a ​ b ​ c d=abc satisfies ( 6.3). ∎

Next, if the primes dividing d d are small enough, we may use the greedy algorithm to factor d d as follows.

###### Lemma 6.4.

Let D = x ϑ − 2 ​ δ D=x^{{\boldsymbol{\vartheta}}-2\delta} for ϑ < 5 − α ​ θ 8 {\boldsymbol{\vartheta}}<\frac{5-{\alpha\theta}}{8}, and take v = 2 ​ ϑ − 1 v=2{\boldsymbol{\vartheta}}-1 and u u as in ( 6.6). For r ⩾ 3 r{\,\geqslant}3, let p 1 ⩾ ⋯ ⩾ p r p_{1}{\,\geqslant}\cdots{\,\geqslant}p_{r} be primes for which d = p 1 ⋯ p r ∈ 𝒟 well ( D) d=p_{1}\cdots p_{r}\in\mathcal{D}^{\textnormal{well}}(D), and p 3 < x u − v p_{3}<x^{u-v} and ( p 2 2 < x 1 − ϑ p_{2}^{2}<x^{1-{\boldsymbol{\vartheta}}}, p 1 < x v p_{1}<x^{v}) or ( p 1 2 < x 1 − ϑ p_{1}^{2}<x^{1-{\boldsymbol{\vartheta}}}, p 2 < x v p_{2}<x^{v}). Then d d has a factorization d = a ​ b ​ c d=abc satisfying ( 6.3).

###### Proof.

Let ( D 1, D 2, D 3) = ( A, D 2 / x, x 1 − 2 ​ δ / ( D ​ A)) (D_{1},D_{2},D_{3})=(A,\,D^{2}/x,\,x^{1-2\delta}/(DA)). By assumption p 1 ⩽ D 2 p_{1}{\,\leqslant}D_{2} and p 2 2 ⩽ D 1 ​ D 3 p_{2}^{2}{\,\leqslant}D_{1}D_{3}, or p 2 ⩽ D 2 p_{2}{\,\leqslant}D_{2} and p 1 2 ⩽ D 1 ​ D 3 p_{1}^{2}{\,\leqslant}D_{1}D_{3}. Thus for some choice { d 1, d 2, d 3 } = { p 1, p 2, p 3 } \{d_{1},d_{2},d_{3}\}=\{p_{1},p_{2},p_{3}\} we have d i ⩽ D i d_{i}{\,\leqslant}D_{i} for all i i.

We now greedily append primes to d i d_{i} while preserving d i ⩽ D i d_{i}{\,\leqslant}D_{i} for all i i, i.e. where at the j j th step we replace d i ↦ d i ​ p j d_{i}\mapsto d_{i}p_{j} (for one of i = 1, 2, 3 i=1,2,3) provided d i ​ p j ⩽ D i d_{i}p_{j}{\,\leqslant}D_{i}. So starting from j = 3 j=3, we stop either when we have exhausted all primes (i.e. j = r j=r), or d i ​ p j > D i d_{i}p_{j}>D_{i} for each i = 1, 2, 3 i=1,2,3.

In the former case, d 1 d 2 d 3 = d = p 1 ⋯ p r d_{1}d_{2}d_{3}=d=p_{1}\cdots p_{r} and d i ⩽ D i d_{i}{\,\leqslant}D_{i} so we easily get d 1 ⩽ D 1 = A d_{1}{\,\leqslant}D_{1}=A and

 | A 2 ​ D 2 ​ D 3 2 \displaystyle A^{2}D_{2}D_{3}^{2} | = x 1 − 4 ​ δ, \displaystyle=x^{1-4\delta}, |  |

as well as

 | ( A ​ d 3 / d 2) 2 ​ θ ​ A ​ d 1 ​ d 2 5 ​ d 3 2 \displaystyle(Ad_{3}/d_{2})^{2{\theta}}Ad_{1}d_{2}^{5}d_{3}^{2} | = A 2 ​ θ ​ d 1 ​ d 2 5 − 2 ​ θ ​ d 3 2 + 2 ​ θ ⩽ A 2 + 2 ​ θ ​ D 2 5 − 2 ​ θ ​ D 3 2 + 2 ​ θ \displaystyle=A^{2{\theta}}d_{1}d_{2}^{5-2{\theta}}d_{3}^{2+2{\theta}}{\,\leqslant}A^{2+2{\theta}}D_{2}^{5-2{\theta}}D_{3}^{2+2{\theta}} |  |

 |  | = A 2 + 2 ​ θ ​ ( D 2 / x) 5 − 2 ​ θ ​ ( x 1 − 2 ​ δ / D ​ A) 2 + 2 ​ θ \displaystyle=A^{2+2{\theta}}(D^{2}/x)^{5-2{\theta}}(x^{1-2\delta}/DA)^{2+2{\theta}} |  |

 |  | = D 8 ​ x − 3 − 2 ​ δ = x 8 ​ ϑ − 3 − 2 ​ δ < x 2 − 2 ​ δ \displaystyle=D^{8}x^{-3-2\delta}=x^{8{\boldsymbol{\vartheta}}-3-2\delta}<x^{2-2\delta} |  |

using ϑ < 5 8 {\boldsymbol{\vartheta}}<\frac{5}{8}. Similarly, we have

 | x α ​ θ ​ A ​ d 1 ​ d 2 5 ​ d 3 2 \displaystyle x^{\alpha\theta}Ad_{1}d_{2}^{5}d_{3}^{2} | = x α ​ θ ​ A 2 ​ ( D 2 / x) 5 ​ ( x 1 − 2 ​ δ / D ​ A) 2 \displaystyle=x^{\alpha\theta}A^{2}(D^{2}/x)^{5}(x^{1-2\delta}/DA)^{2} |  |

 |  | = x α ​ θ − 3 − 4 ​ δ ​ D 8 = x α ​ θ − 3 − 4 ​ δ + 8 ​ ϑ < x 2 − 2 ​ δ \displaystyle=x^{{\alpha\theta}-3-4\delta}D^{8}=x^{{\alpha\theta}-3-4\delta+8{\boldsymbol{\vartheta}}}<x^{2-2\delta} |  |

using ϑ < 5 − α ​ θ 8 {\boldsymbol{\vartheta}}<\frac{5-{\alpha\theta}}{8}. Thus letting a = d 1, b = d 2, c = d 3 a=d_{1},b=d_{2},c=d_{3} gives the desired factorisation for ( 6.3).

In the latter case, there exists a terminal index j < r j<r for which d i ​ p j > D i d_{i}p_{j}>D_{i} for all i = 1, 2, 3 i=1,2,3. By assumption j ⩾ 3 j{\,\geqslant}3, and so p j ⩽ p 3 ⩽ x u − v p_{j}{\,\leqslant}p_{3}{\,\leqslant}x^{u-v} is smaller than the width of the interval [x v, x u] [x^{v},x^{u}]. And since d 2 ⩽ D 2 = x v < d 2 ​ p j d_{2}{\,\leqslant}D_{2}=x^{v}<d_{2}p_{j}, we deduce b:= d 2 ​ p j b:=d_{2}p_{j} lies in the interval b ∈ [x v, x u] b\in[x^{v},x^{u}]. Thus letting C:= D 2 ​ D 3 / b C:=D_{2}D_{3}/b, for each l > j l>j we have

 | p l 2 ⩽ D p 1 ⋯ p l − 1 = D 1 ​ D 2 ​ D 3 d 1 d 2 d 3 p j ⋯ p l − 1 = D 1 ​ C d 1 d 3 p j + 1 ⋯ p l − 1. \displaystyle p_{l}^{2}{\,\leqslant}\frac{D}{p_{1}\cdots p_{l-1}}=\frac{D_{1}D_{2}D_{3}}{d_{1}d_{2}d_{3}p_{j}\cdots p_{l-1}}=\frac{D_{1}C}{d_{1}d_{3}p_{j+1}\cdots p_{l-1}}. |  |

So there is a factorization a c = d 1 d 3 p j + 1 ⋯ p l ac=d_{1}d_{3}p_{j+1}\cdots p_{l} with a ⩽ D 1 = A a{\,\leqslant}D_{1}=A and c ⩽ C = D / ( A ​ b ​ x 2 ​ δ) c{\,\leqslant}C=D/(Abx^{2\delta}). When l = r l=r, recalling b = d 2 ​ p j b=d_{2}p_{j}, we deduce a factorization

 | a b c = d 1 d 2 d 3 p j ⋯ p r = p 1 ⋯ p r = d. \displaystyle abc=d_{1}d_{2}d_{3}p_{j}\cdots p_{r}=p_{1}\cdots p_{r}=d. |  |

Hence Lemma 6.3 implies that d = a ​ b ​ c d=abc satisfies ( 6.3). ∎

In the following result, we factorize d ∈ 𝒟 well ​ ( D) d\in\mathcal{D}^{\textnormal{well}}(D) for variable level D D, depending on the anatomy of d d. As 𝒟 ± ⊂ 𝒟 well \mathcal{D}^{\pm}\subset\mathcal{D}^{\textnormal{well}}, this has implications to both upper and lower bounds for the standard linear sieve.

###### Proposition 6.5.

Let D = x ϑ − 2 ​ δ D=x^{{\boldsymbol{\vartheta}}-2\delta} with ϑ < 5 8 {\boldsymbol{\vartheta}}<\frac{5}{8}, and take v v, u u as in ( 6.6). Let p r ⩽ ⋯ ⩽ p 1 ⩽ x u p_{r}{\,\leqslant}\cdots{\,\leqslant}p_{1}{\,\leqslant}x^{u} be primes for which d = p 1 ⋯ p r ∈ 𝒟 well ( D) d=p_{1}\cdots p_{r}\in\mathcal{D}^{\textnormal{well}}(D). Then d d has factorization d = a ​ b ​ c d=abc satisfying ( 6.3), provided one of the following holds:

- (i)

b ∈ [x v, x u] b\in[x^{v},\,x^{u}] for some b ∈ { p 1, p 2, p 1 ​ p 2, p 1 ​ p 2 ​ p 3 } b\in\{p_{1},\,p_{2},\,p_{1}p_{2},\,p_{1}p_{2}p_{3}\}

- (ii)

p 1 ​ p 3 ∈ [x v, x u] p_{1}p_{3}\in[x^{v},\,x^{u}] and p 2 2 ⩽ D / p 1 ​ p 3 p_{2}^{2}{\,\leqslant}D/p_{1}p_{3}

- (iii)

p 2 ​ p 3 ∈ [x v, x u] p_{2}p_{3}\in[x^{v},\,x^{u}] and p 1 2 ⩽ D / p 2 ​ p 3 p_{1}^{2}{\,\leqslant}D/p_{2}p_{3}

- (iv)

p 3 ⩽ x u − v p_{3}\ {\,\leqslant}\ x^{u-v}, and ( p 1 ⩽ x v p_{1}\ {\,\leqslant}\ x^{v} and p 2 2 ⩽ x 1 − 2 ​ δ / D p_{2}^{2}{\,\leqslant}x^{1-2\delta}/D) or ( p 2 ⩽ x v p_{2}\ {\,\leqslant}\ x^{v} and p 1 2 ⩽ x 1 − 2 ​ δ / D p_{1}^{2}{\,\leqslant}x^{1-2\delta}/D)

###### Proof.

First suppose b = p 1 ⋯ p i ∈ [x v, x u] b=p_{1}\cdots p_{i}\in[x^{v},\,x^{u}] for some i ∈ { 1, 2, 3 } i\in\{1,2,3\}, and let C = D / A ​ b C=D/Ab. Since p 1 ⋯ p i p i + 1 2 ⩽ D p_{1}\cdots p_{i}p_{i+1}^{2}{\,\leqslant}D, we get p i + 1 2 ⩽ D / b = A ​ C p_{i+1}^{2}{\,\leqslant}D/b=AC so that either p i + 1 ⩽ A p_{i+1}{\,\leqslant}A or p i + 1 ⩽ C p_{i+1}{\,\leqslant}C. Similarly p 1 ⋯ p j − 1 p j 2 ⩽ D p_{1}\cdots p_{j-1}p_{j}^{2}{\,\leqslant}D for all i < j ⩽ r i<j{\,\leqslant}r, we get p j 2 ⩽ A ​ C p i + 1 ⋯ p j − 1 p_{j}^{2}{\,\leqslant}\frac{AC}{p_{i+1}\cdots p_{j-1}} and so by induction we may factor p i + 1 ⋯ p r = a c p_{i+1}\cdots p_{r}=ac where a ⩽ A a{\,\leqslant}A, c ⩽ C c{\,\leqslant}C. Hence since b ∈ [x v, x u] b\in[x^{v},\,x^{u}], by Lemma 6.3 p 1 ⋯ p r = a b c p_{1}\cdots p_{r}=abc satisfies ( 6.3).

Else p 1, p 1 ​ p 2, p 1 ​ p 2 ​ p 3 ∉ [x v, x u] p_{1},p_{1}p_{2},p_{1}p_{2}p_{3}\notin[x^{v},\,x^{u}]. Suppose b ∈ [x v, x u] b\in[x^{v},\,x^{u}] for some b ∈ { p 2 ​ p 3, p 1 ​ p 3, p 2 } b\in\{p_{2}p_{3},\,p_{1}p_{3},\,p_{2}\}. By assumption p 1 ⩽ x u p_{1}{\,\leqslant}\,x^{u}, so p 1 ∉ [x v, x u] p_{1}\notin[x^{v},\,x^{u}] further implies p 1 < x v p_{1}<x^{v}. We have:

- •

If b = p 2 b=p_{2} then p 3 2 ⩽ D / p 1 ​ p 2 = D / p 1 ​ b p_{3}^{2}{\,\leqslant}D/p_{1}p_{2}=D/p_{1}b implies p 1 ​ p 3 = a ​ c p_{1}p_{3}=ac factors for a ⩽ A, c ⩽ D / A ​ b a{\,\leqslant}A,c{\,\leqslant}D/Ab.

- •

If b = p 1 ​ p 3 b=p_{1}p_{3} and p 2 2 ⩽ D / b p_{2}^{2}{\,\leqslant}D/b by (ii), then p 2 ⩽ A p_{2}{\,\leqslant}A or p 2 ⩽ D / A ​ b p_{2}{\,\leqslant}D/Ab.

- •

If b = p 2 ​ p 3 b=p_{2}p_{3} and p 1 2 ⩽ D / b p_{1}^{2}{\,\leqslant}D/b by (iii), then p 1 ⩽ A p_{1}{\,\leqslant}A or p 1 ⩽ D / A ​ b p_{1}{\,\leqslant}D/Ab.

For each b ∈ [x v, x u] b\in[x^{v},\,x^{u}] above, we factored p 1 ​ p 2 ​ p 3 = a ​ b ​ c p_{1}p_{2}p_{3}=abc where a ⩽ A, c ⩽ D / A ​ b a{\,\leqslant}A,c{\,\leqslant}D/Ab. Then since p 1 ⋯ p j − 1 p j 2 ⩽ D p_{1}\cdots p_{j-1}p_{j}^{2}{\,\leqslant}D for all j ⩽ r j{\,\leqslant}r, by induction we may factor p 1 ⋯ p r = a b c p_{1}\cdots p_{r}=abc for a ⩽ A, c ⩽ D / A ​ b a{\,\leqslant}A,c{\,\leqslant}D/Ab. By Lemma 6.3 p 1 ⋯ p r = a b c p_{1}\cdots p_{r}=abc will satisfy ( 6.3).

Finally, suppose (iv) holds: p 3 ⩽ x u − v p_{3}\ {\,\leqslant}\ x^{u-v}, p 2 2 ⩽ x 1 − 2 ​ δ / D p_{2}^{2}{\,\leqslant}x^{1-2\delta}/D, and d 2:= p 1 ⩽ x v d_{2}:=p_{1}\ {\,\leqslant}\ x^{v}. Then Lemma 6.4 completes the proof. ∎

###### Proof of Proposition 6.1.

Recall D = x ϑ − 2 ​ δ D=x^{{\boldsymbol{\vartheta}}-2\delta} and p i = x t i p_{i}=x^{t_{i}}. By Proposition 6.5, d = p 1 ⋯ p r d=p_{1}\cdots p_{r} has a factorization d = a ​ b ​ c d=abc satisfying ( 6.3) provided t 1 ⩽ u t_{1}{\,\leqslant}u, and one of the following holds:

- (i)

τ ∈ [v, u] \tau\in[v,u] for some subsum τ ∈ { t 1, t 2, t 1 + t 2, t 1 + t 2 + t 3 } \tau\in\{t_{1},\,t_{2},\,t_{1}+t_{2},\,t_{1}+t_{2}+t_{3}\}

- (ii)

t 1 + t 3 ∈ [v, u] t_{1}+t_{3}\in[v,u] and ϑ ⩾ t 1 + 2 ​ t 2 + t 3 {\boldsymbol{\vartheta}}{\,\geqslant}t_{1}+2t_{2}+t_{3}

- (iii)

t 2 + t 3 ∈ [v, u] t_{2}+t_{3}\in[v,u] and ϑ ⩾ 2 ​ t 1 + t 2 + t 3 {\boldsymbol{\vartheta}}{\,\geqslant}2t_{1}+t_{2}+t_{3}

- (iv)

t 3 ⩽ u − v t_{3}{\,\leqslant}u-v and ( t 1 ⩽ v t_{1}{\,\leqslant}v and 2 ​ t 2 ⩽ 1 − ϑ 2t_{2}{\,\leqslant}1-{\boldsymbol{\vartheta}}) or ( t 2 ⩽ v t_{2}{\,\leqslant}v and 2 ​ t 1 ⩽ 1 − ϑ 2t_{1}{\,\leqslant}1-{\boldsymbol{\vartheta}})

To this, note

 | 2 ​ ϑ − 1 = v ⩽ t ⩽ u = min ⁡ ( 1 − ( 1 + θ) ​ ϑ 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ − α ​ θ 3) \displaystyle 2{\boldsymbol{\vartheta}}-1=v\ {\,\leqslant}\ t\ {\,\leqslant}\ u=\min\Big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}-{\alpha\theta}}{3}\Big) |  |

so that

(6.7) |  | t ∈ [v, u] ⟺ ϑ ⩽ min ( 1 + t 2, 1 − ( 3 / 2 − 2 ​ θ) ​ t 1 + θ, 1 − α ​ θ + 3 ​ t 2) =: ϑ ( t). \displaystyle t\in[v,u]\qquad\Longleftrightarrow\qquad{\boldsymbol{\vartheta}}\ {\,\leqslant}\ \min\Big(\frac{1+t}{2},\ \frac{1-(3/2-2{\theta})t}{1+{\theta}},\ 1-\frac{{\alpha\theta}+3t}{2}\Big)=:{\boldsymbol{\vartheta}}(t). |  |

For (i), by ( 6.7) we see ( 6.3) holds if ϑ ⩽ max ⁡ { ϑ ⁡ ( t 1), ϑ ⁡ ( t 2), ϑ ⁡ ( t 1 + t 2), ϑ ⁡ ( t 1 + t 2 + t 3) } {\boldsymbol{\vartheta}}{\,\leqslant}\max\big\{{\boldsymbol{\vartheta}}(t_{1}),\,{\boldsymbol{\vartheta}}(t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}+t_{3})\big\}.

For (ii), by ( 6.7) we see ( 6.3) holds if t 1 + 2 ​ t 2 + t 3 ⩽ ϑ ⩽ ϑ ⁡ ( t 1 + t 3) t_{1}+2t_{2}+t_{3}{\,\leqslant}{\boldsymbol{\vartheta}}{\,\leqslant}{\boldsymbol{\vartheta}}(t_{1}+t_{3}). Recalling the notation ψ ⁡ ( x, y) = x ⋅ 𝟏 x ⩾ y \psi(x,y)=x\cdot{\mathbf{1}}_{x{\,\geqslant}y}, this is equivalent to the condition ϑ ⩽ ψ ⁡ ( ϑ ⁡ ( t 1 + t 3), t 1 + 2 ​ t 2 + t 3) {\boldsymbol{\vartheta}}{\,\leqslant}\psi\big({\boldsymbol{\vartheta}}(t_{1}+t_{3}),t_{1}+2t_{2}+t_{3}\big).

For (iii) similarly, ( 6.3) holds if ϑ ⩽ ψ ⁡ ( ϑ ⁡ ( t 2 + t 3), 2 ​ t 1 + t 2 + t 3) {\boldsymbol{\vartheta}}{\,\leqslant}\psi\big({\boldsymbol{\vartheta}}(t_{2}+t_{3}),2t_{1}+t_{2}+t_{3}\big).

For (iv), we have that

 | t 3 ⩽ u − v \displaystyle t_{3}\ {\,\leqslant}\ u-v | = min ⁡ ( 1 − ( 1 + θ) ​ ϑ 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ − α ​ θ 3) − ( 2 ​ ϑ − 1) \displaystyle=\min\Big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}-{\alpha\theta}}{3}\Big)-(2{\boldsymbol{\vartheta}}-1) |  |

(6.8) |  |  | = min ⁡ ( ( 5 / 2 − 2 ​ θ) − ( 4 − 3 ​ θ) ​ ϑ 3 / 2 − 2 ​ θ, 5 − α ​ θ − 8 ​ ϑ 3), \displaystyle=\min\Big(\frac{(5/2-2{\theta})-(4-3{\theta}){\boldsymbol{\vartheta}}}{3/2-2{\theta}},\ \frac{5-{\alpha\theta}-8{\boldsymbol{\vartheta}}}{3}\Big), |  |

and ( t 1 ⩽ v = 2 ​ ϑ − 1 t_{1}{\,\leqslant}\,v=2{\boldsymbol{\vartheta}}-1 and 2 ​ t 2 ⩽ 1 − ϑ 2t_{2}{\,\leqslant}\,1-{\boldsymbol{\vartheta}}) or ( t 2 ⩽ v = 2 ​ ϑ − 1 t_{2}{\,\leqslant}\,v=2{\boldsymbol{\vartheta}}-1 and 2 ​ t 1 ⩽ 1 − ϑ 2t_{1}{\,\leqslant}\,1-{\boldsymbol{\vartheta}}), is equivalent to either

 | 1 + t 1 2 ⩽ ϑ ⩽ min ⁡ { ( 5 / 2 − 2 ​ θ) − ( 3 / 2 − 2 ​ θ) ​ t 3 4 − 3 ​ θ, 5 − α ​ θ − 3 ​ t 3 8, 1 − 2 ​ t 2 }, \displaystyle\frac{1+t_{1}}{2}\ {\,\leqslant}\ {\boldsymbol{\vartheta}}\ {\,\leqslant}\ \min\Big\{\frac{(5/2-2{\theta})-(3/2-2{\theta})t_{3}}{4-3{\theta}},\,\frac{5-{\alpha\theta}-3t_{3}}{8},\,1-2t_{2}\Big\}, |  |

or

 | 1 + t 2 2 ⩽ ϑ ⩽ min ⁡ { ( 5 / 2 − 2 ​ θ) − ( 3 / 2 − 2 ​ θ) ​ t 3 4 − 3 ​ θ, 5 − α ​ θ − 3 ​ t 3 8, 1 − 2 ​ t 1 }. \displaystyle\frac{1+t_{2}}{2}\ {\,\leqslant}\ {\boldsymbol{\vartheta}}\ {\,\leqslant}\ \min\Big\{\frac{(5/2-2{\theta})-(3/2-2{\theta})t_{3}}{4-3{\theta}},\,\frac{5-{\alpha\theta}-3t_{3}}{8},\,1-2t_{1}\Big\}. |  |

Note the maximal ϑ ∈ [y, x] {\boldsymbol{\vartheta}}\in[y,x] is given by ϑ = x ⋅ 𝟏 x ⩾ y =: ψ ⁡ ( x, y) {\boldsymbol{\vartheta}}=x\cdot{\mathbf{1}}_{x{\,\geqslant}y}=:\psi(x,y). Thus ( 6.3) holds if ϑ ⩽ max ⁡ { w ⁡ ( t 1, t 2, t 3), w ⁡ ( t 1, t 3, t 2) } {\boldsymbol{\vartheta}}{\,\leqslant}\,\max\{w(t_{1},t_{2},t_{3}),w(t_{1},t_{3},t_{2})\} where

(6.9) |  | w ⁡ ( t 1, t 2, t 3):= ψ ⁡ ( min ⁡ { ( 5 − 4 ​ θ) − ( 3 − 4 ​ θ) ​ t 3 8 − 6 ​ θ, 5 − α ​ θ − 3 ​ t 3 8, 1 − 2 ​ t 2 }, 1 + t 1 2). \displaystyle w(t_{1},t_{2},t_{3}):=\psi\Big(\min\Big\{\;\frac{(5-4{\theta})-(3-4{\theta})t_{3}}{8-6{\theta}},\;\frac{5-{\alpha\theta}-3t_{3}}{8},\;1-2t_{2}\Big\},\,\frac{1+t_{1}}{2}\Big). |  |

Taking the maximum ϑ {\boldsymbol{\vartheta}} allowed among cases (i)–(iv), we see ( 6.3) holds if

 | ϑ = max { ϑ ( t 1) \displaystyle{\boldsymbol{\vartheta}}=\max\Big\{{\boldsymbol{\vartheta}}(t_{1}) | , ϑ ( t 2), ϑ ( t 1 + t 2), ϑ ( t 1 + t 2 + t 3), w ( t 1, t 2, t 3), w ( t 1, t 3, t 2) \displaystyle,\,{\boldsymbol{\vartheta}}(t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}),\,{\boldsymbol{\vartheta}}(t_{1}+t_{2}+t_{3}),\,w(t_{1},t_{2},t_{3}),\,w(t_{1},t_{3},t_{2}) |  |

(6.10) |  |  | ψ ( ϑ ( t 1 + t 3), t 1 + 2 t 2 + t 3), ψ ( ϑ ( t 2 + t 3), 2 t 1 + t 2 + t 3) }, \displaystyle\ \ \psi\big({\boldsymbol{\vartheta}}(t_{1}+t_{3}),\,t_{1}+2t_{2}+t_{3}\big),\ \psi\big({\boldsymbol{\vartheta}}(t_{2}+t_{3}),\,2t_{1}+t_{2}+t_{3}\big)\Big\}, |  |

crucially provided that t 1 ⩽ u t_{1}{\,\leqslant}\,u holds.

To this, we have ϑ = ϑ ⁡ ( τ) {\boldsymbol{\vartheta}}={\boldsymbol{\vartheta}}(\tau) for some subsum τ \tau in ( 6). If τ = t 1 \tau=t_{1}, then t 1 ⩽ u = min ⁡ ( 1 − ( 1 + θ) ​ ϑ ​ ( t 1) 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ ​ ( t 1) − α ​ θ 3) t_{1}{\,\leqslant}\,u=\min\big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}(t_{1})}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}(t_{1})-{\alpha\theta}}{3}\big) automatically holds, by the definition of ϑ ⁡ ( t 1) {\boldsymbol{\vartheta}}(t_{1}).

Else the subsum is τ ≠ t 1 \tau\neq t_{1}, i.e. ϑ ⁡ ( τ) > ϑ ⁡ ( t 1) {\boldsymbol{\vartheta}}(\tau)>{\boldsymbol{\vartheta}}(t_{1}). Then t 1 ⩽ μ t_{1}{\,\leqslant}\mu by assumption in Proposition 6.1. 9 9 9 Recall μ = min ⁡ ( 1 − θ 4 − 3 ​ θ, 1 − α ​ θ 4) \mu=\min(\frac{1-{\theta}}{4-3{\theta}},\,\frac{1-{\alpha\theta}}{4}) is the balance point of the (unimodal) function ϑ ⁡ ( t) {\boldsymbol{\vartheta}}(t), from ( 6.2). Thus t 1 ⩽ μ < u = min ⁡ ( 1 − ( 1 + θ) ​ ϑ ​ ( τ) 3 / 2 − 2 ​ θ, 2 − 2 ​ ϑ ​ ( τ) − α ​ θ 3) t_{1}{\,\leqslant}\mu<u=\min\big(\frac{1-(1+{\theta}){\boldsymbol{\vartheta}}(\tau)}{3/2-2{\theta}},\,\frac{2-2{\boldsymbol{\vartheta}}(\tau)-{\alpha\theta}}{3}\big). This completes the proof in all cases. ∎

### 6.1. Level of distribution with linear sieve weights

Recall the (upper and lower) linear sieve weights λ ± \lambda^{\pm} of level D D are defined as

 | λ ± ​ ( d) = { μ ⁡ ( d) if ​ d ∈ 𝒟 ± ​ ( D), 0 else, \lambda^{\pm}(d)=\begin{cases}\mu(d)&\text{if }d\in\mathcal{D}^{\pm}(D),\\ 0&\text{else,}\end{cases} |  |

for support sets 𝒟 ± \mathcal{D}^{\pm}, given by

 | 𝒟 + ​ ( D) \displaystyle\mathcal{D}^{+}(D)\  | = { d = p 1 ⋯ p r: p 1 ⋯ p m − 1 p m 3 < D for odd m ⩽ r }, \displaystyle=\ \big\{\,d=p_{1}\cdots p_{r}\ :\ p_{1}\cdots p_{m-1}p_{m}^{3}<D\quad{\rm for\ odd}\ \ m{\,\leqslant}r\big\}, |  |

 | 𝒟 − ​ ( D) \displaystyle\mathcal{D}^{-}(D)\  | = { d = p 1 ⋯ p r: p 1 ⋯ p m − 1 p m 3 < D for even m ⩽ r, p 1 2 < D }. \displaystyle=\ \big\{\,d=p_{1}\cdots p_{r}\ :\ p_{1}\cdots p_{m-1}p_{m}^{3}<D\quad{\rm for\ even}\ \ m{\,\leqslant}r,\ p_{1}^{2}<D\big\}. |  |

Observe the support sets 𝒟 ± \mathcal{D}^{\pm} are contained in 𝒟 well \mathcal{D}^{\rm well} from ( 6.1). Consider the analogous set of well-factorable vectors 𝐃 r well \mathbf{D}_{r}^{\textnormal{well}},

(6.11) |  | 𝐃 r well ​ ( D) \displaystyle\mathbf{D}_{r}^{\textnormal{well}}(D) | = { ( D 1, …, D r): D 1 ⋯ D m − 1 D m 2 < D for all m ⩽ r }, \displaystyle=\{(D_{1},\ldots,D_{r}):D_{1}\cdots D_{m-1}D_{m}^{2}<D\quad\text{ for all }m{\,\leqslant}r\}, |  |

where all entries D 1, …, D r D_{1},\ldots,D_{r} are numbers in the sequence ( D ϵ 2 ​ ( 1 + ϵ 9) j) j ⩾ 1 (D^{\epsilon^{2}(1+\epsilon^{9})^{j}})_{j{\,\geqslant}1}.

In reality, we shall work with Iwaniec’s modified linear sieve weights λ ~ ± \widetilde{\lambda}^{\pm}, which enjoy the same sieve upper and lower bounds as λ ± \lambda^{\pm}, but are also well-factorable (the original weights λ ± \lambda^{\pm} are not, by a minor technicality). The construction of λ ~ ± \widetilde{\lambda}^{\pm} makes use of the vectors in ( 6.11); see [18, §12.4] for a precise definition of λ ~ ± \widetilde{\lambda}^{\pm} and further details.

The key point is that Iwaniec’s well-factorable weights λ ~ ± ​ ( d) \widetilde{\lambda}^{\pm}(d) essentially inherit the same factorization properties enjoyed by the integers d d in the support d ∈ 𝒟 well ​ ( x ϑ) d\in\mathcal{D}^{\rm well}(x^{\boldsymbol{\vartheta}}). As such, the factorization of 𝒟 well \mathcal{D}^{\rm well} in Proposition 6.1 implies an improved level of distribution for primes with linear sieve weights.

###### Proposition 6.6.

Let ( D 1, …, D r) ∈ 𝐃 r well ​ ( D) (D_{1},\ldots,D_{r})\in\mathbf{D}_{r}^{\textnormal{well}}(D) and write D = x ϑ D=x^{\boldsymbol{\vartheta}}, D i = x t i D_{i}=x^{t_{i}} for i ⩽ r i{\,\leqslant}r.

If ϑ ⩽ ϑ ⁡ ( t 1) − ϵ {\boldsymbol{\vartheta}}{\,\leqslant}{\boldsymbol{\vartheta}}(t_{1})-\epsilon as in ( 6.2), then

(6.12) |  | ∑ b = p 1 ⋯ p r D i < p i ⩽ D i 1 + ϵ 9 ∑ d = b ​ c ⩽ x ϑ c | P ⁡ ( p r) ( d, a) = 1 λ ~ ± ( d) ( π ( x; d, a) − π ⁡ ( x) φ ⁡ ( d)) ≪ a, A, ϵ x ( log ⁡ x) A. \displaystyle\sum_{\begin{subarray}{c}b=p_{1}\cdots p_{r}\\ D_{i}<p_{i}{\,\leqslant}D_{i}^{1+\epsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}d=bc{\,\leqslant}x^{{\boldsymbol{\vartheta}}}\\ c\mid P(p_{r})\\ (d,a)=1\end{subarray}}\widetilde{\lambda}^{\pm}(d)\,\Big(\pi(x;d,a)-\frac{\pi(x)}{{\varphi}(d)}\Big)\ \ll_{a,A,\epsilon}\ \frac{x}{(\log x)^{A}}. |  |

And if t 1 ⩽ min ⁡ ( 1 − θ 4 − 3 ​ θ, 1 − α ​ θ 4) t_{1}{\,\leqslant}\,\min(\frac{1-{\theta}}{4-3{\theta}},\,\frac{1-\alpha\theta}{4}) and r ⩾ 3 r{\,\geqslant}3, then ( 6.12) holds if ϑ ⩽ ϑ ⁡ ( t 1, t 2, t 3) − ϵ {\boldsymbol{\vartheta}}\,{\,\leqslant}\,{\boldsymbol{\vartheta}}(t_{1},t_{2},t_{3})-\epsilon as in ( 6.1).

###### Proof.

This follows just as in the proof of [25, Proposition 5.4], just substituting Proposition 6.1 above in for [25, Proposition 3.3], with an updated level ϑ {\boldsymbol{\vartheta}}. ∎

## 7. Bounds for twin primes and Goldbach representations

In this section, we complete the proofs of Theorems 1.1 and 1.2, by combining the sieve bounds from [25] with our level of distribution results for the linear sieve weights λ ~ ± \widetilde{\lambda}^{\pm}, from the previous section. Indeed, we substitute Proposition 6.6 in from [25, Proposition 5.4], which in practice amounts to modifying the level to ϑ {\boldsymbol{\vartheta}}, as in ( 6.2) and ( 6.1), into the prior bounds from [25]. Also see [26] for related applications of level of distribution results.

As a brief summary of the sieve-theoretic ideas, following the spirit of Fouvry–Grupp [16] we essentially use a weighted sieve inequality, and iterate the Buchstab identity in a prescribed fashion. We select certain terms to drop (by positivity), and to certain other terms we apply the Chen–Iwaniec switching principal. This approach was recursively optimized in Wu [36]. Finally, to each such term, we apply the linear sieve upper and lower bounds. The remainder terms in such sieve bounds are controlled using level of distribution results for π ⁡ ( x, q, a) \pi(x;q,a), as in Proposition 6.6. with residue a = − 2 a=-2. We refer the reader to [25] for further details about this computation.

### 7.1. Sieve-theoretic bounds

We now recall the notations and bounds in [25, §6]. Given μ ⩽ μ α \mu{\,\leqslant}\mu_{\alpha} and parameters 0.1 ⩽ ρ ′ ⩽ τ 1 < μ ⩽ τ 2 < τ 3 ⩽ ρ ⩽ 0.3. 0.1{\,\leqslant}\rho^{\prime}{\,\leqslant}\tau_{1}<\mu{\,\leqslant}\tau_{2}<\tau_{3}{\,\leqslant}\rho{\,\leqslant}0.3., we define the following integrals I n = I n ​ ( ρ, ρ ′, τ 1, τ 2, τ 3) I_{n}=I_{n}(\rho,\rho^{\prime},\tau_{1},\tau_{2},\tau_{3}) by

 | I n \displaystyle I_{n} | = ∫ 𝔻 n ω ( 1 − t − u − v u) d t ​ d u ​ d v t ​ u 2 ​ v ( 9 ⩽ n ⩽ 15), \displaystyle=\int_{{\mathbb{D}}_{n}}\omega\Big(\frac{1-t-u-v}{u}\Big)\frac{\differential{t}\differential{u}\differential{v}}{tu^{2}v}\quad\qquad\qquad(9{\,\leqslant}n{\,\leqslant}15), |  |

(7.1) |  | I n \displaystyle I_{n} | = ∫ 𝔻 n ω ( 1 − t − u − v − w v) d t ​ d u ​ d v ​ d w t ​ u ​ v 2 ​ w ( 16 ⩽ n ⩽ 19), \displaystyle=\int_{{\mathbb{D}}_{n}}\omega\Big(\frac{1-t-u-v-w}{v}\Big)\frac{\differential{t}\differential{u}\differential{v}\differential{w}}{tuv^{2}w}\quad\qquad(16{\,\leqslant}n{\,\leqslant}19), |  |

 | I 20 \displaystyle I_{20} | = ∫ 𝔻 20 ω ⁡ ( 1 − t − u − v − w − x w) ​ d t ​ d u ​ d v ​ d w ​ d x t ​ u ​ v ​ w 2 ​ x, \displaystyle=\int_{{\mathbb{D}}_{20}}\omega\Big(\frac{1-t-u-v-w-x}{w}\Big)\frac{\differential{t}\differential{u}\differential{v}\differential{w}\differential{x}}{tuvw^{2}x}, |  |

 | I 21 \displaystyle I_{21} | = ∫ 𝔻 21 ω ⁡ ( 1 − t − u − v − w − x − y x) ​ d t ​ d u ​ d v ​ d w ​ d x ​ d y t ​ u ​ v ​ w ​ x 2 ​ y, \displaystyle=\int_{{\mathbb{D}}_{21}}\omega\Big(\frac{1-t-u-v-w-x-y}{x}\Big)\frac{\differential{t}\differential{u}\differential{v}\differential{w}\differential{x}\differential{y}}{tuvwx^{2}y}, |  |

where ω \omega is the Buchstab function, and where the domains 𝔻 n {\mathbb{D}}_{n} are

 | 𝔻 9 \displaystyle{\mathbb{D}}_{9}\  | = { ( t, u, v): τ 1 < t < u < v < τ 3 }, \displaystyle=\{(t,u,v):\tau_{1}<t<u<v<\tau_{3}\}, |  |

 | 𝔻 10 \displaystyle{\mathbb{D}}_{10} | = { ( t, u, v): τ 1 < t < u < τ 2 < v < ρ }, \displaystyle=\{(t,u,v):\tau_{1}<t<u<\tau_{2}<v<\rho\}, |  |

 | 𝔻 11 \displaystyle{\mathbb{D}}_{11} | = { ( t, u, v): τ 1 < t < τ 2 < u < v < τ 3 }, \displaystyle=\{(t,u,v):\tau_{1}<t<\tau_{2}<u<v<\tau_{3}\}, |  |

 | 𝔻 12 \displaystyle{\mathbb{D}}_{12} | = { ( t, u, v): ρ ′ < t < u < τ 1, τ 3 < v < ρ }, \displaystyle=\{(t,u,v):\rho^{\prime}<t<u<\tau_{1},\ \tau_{3}<v<\rho\}, |  |

 | 𝔻 13 \displaystyle{\mathbb{D}}_{13} | = { ( t, u, v): ρ ′ < t < τ 1 < u < τ 2 < v < ρ }, \displaystyle=\{(t,u,v):\rho^{\prime}<t<\tau_{1}<u<\tau_{2}<v<\rho\}, |  |

 | 𝔻 14 \displaystyle{\mathbb{D}}_{14} | = { ( t, u, v): ρ ′ < t < τ 1, τ 2 < u < v < ρ }, \displaystyle=\{(t,u,v):\rho^{\prime}<t<\tau_{1},\ \tau_{2}<u<v<\rho\}, |  |

 | 𝔻 15 \displaystyle{\mathbb{D}}_{15} | = { ( t, u, v): τ 1 < t < τ 2 < u < τ 3 < v < ρ }, \displaystyle=\{(t,u,v):\tau_{1}<t<\tau_{2}<u<\tau_{3}<v<\rho\}, |  |

 | 𝔻 16 \displaystyle{\mathbb{D}}_{16} | = { ( t, u, v, w): τ 2 < t < u < v < w < τ 3 }, \displaystyle=\{(t,u,v,w):\tau_{2}<t<u<v<w<\tau_{3}\}, |  |

 | 𝔻 17 \displaystyle{\mathbb{D}}_{17} | = { ( t, u, v, w): τ 2 < t < u < v < τ 3 < w < ρ }, \displaystyle=\{(t,u,v,w):\tau_{2}<t<u<v<\tau_{3}<w<\rho\}, |  |

 | 𝔻 18 \displaystyle{\mathbb{D}}_{18} | = { ( t, u, v, w): τ 2 < t < u < τ 3 < v < w < ρ }, \displaystyle=\{(t,u,v,w):\tau_{2}<t<u<\tau_{3}<v<w<\rho\}, |  |

 | 𝔻 19 \displaystyle{\mathbb{D}}_{19} | = { ( t, u, v, w): τ 1 < t < τ 2, τ 3 < u < v < w < ρ }, \displaystyle=\{(t,u,v,w):\tau_{1}<t<\tau_{2},\ \tau_{3}<u<v<w<\rho\}, |  |

 | 𝔻 20 \displaystyle{\mathbb{D}}_{20} | = { ( t, u, v, w, x): τ 2 < t < τ 3 < u < v < w < x < ρ }, \displaystyle=\{(t,u,v,w,x):\tau_{2}<t<\tau_{3}<u<v<w<x<\rho\}, |  |

 | 𝔻 21 \displaystyle{\mathbb{D}}_{21} | = { ( t, u, v, w, x, y): τ 3 < t < u < v < w < x < y < ρ }. \displaystyle=\{(t,u,v,w,x,y):\tau_{3}<t<u<v<w<x<y<\rho\}. |  |

As in ( 6.2), denote

(7.2) |  | ϑ ⁡ ( t) = ϑ α ​ ( t) \displaystyle{\boldsymbol{\vartheta}}(t)={\boldsymbol{\vartheta}}_{\alpha}(t) | : = { min ⁡ ( 1 − ( 3 / 2 − 2 ​ θ) ​ t 1 + θ, 1 − α ​ θ + 3 ​ t 2) if t > μ α, 1 + t 2 if t ⩽ μ α. \displaystyle:=\begin{cases}\min\big(\frac{1-(3/2-2{\theta})t}{1+{\theta}},\ 1-\frac{\alpha\theta+3t}{2}\big)&\text{if}\ \ t>\mu_{\alpha},\\ \frac{1+t}{2}&\text{if}\ \ t{\,\leqslant}\,\mu_{\alpha}.\end{cases} |  |

where μ α = min ⁡ ( 1 − θ 4 − 3 ​ θ, 1 − α ​ θ 4) \mu_{\alpha}=\min(\frac{1-{\theta}}{4-3{\theta}},\,\frac{1-\alpha\theta}{4}), and from ( 6.1),

 | ϑ ( t, u, v):= max { ϑ ( t) \displaystyle{\boldsymbol{\vartheta}}(t,u,v):=\max\Big\{{\boldsymbol{\vartheta}}(t) | , ϑ ( u), ϑ ( t + u), ϑ ( t + u + v), w ( t, u, v), w ( t, v, u) \displaystyle,\,{\boldsymbol{\vartheta}}(u),\,{\boldsymbol{\vartheta}}(t+u),\,{\boldsymbol{\vartheta}}(t+u+v),\,w(t,u,v),\,w(t,v,u) |  |

(7.3) |  |  | ψ ( ϑ ( t + v), t + 2 u + v), ψ ( ϑ ( u + v), 2 t + u + v) }, \displaystyle\ \ \psi\big({\boldsymbol{\vartheta}}(t+v),\,t+2u+v\big),\ \psi\big({\boldsymbol{\vartheta}}(u+v),\,2t+u+v\big)\Big\}, |  |

where ψ ⁡ ( x, y):= x ⋅ 𝟏 x ⩾ y \psi(x,y):=x\cdot{\mathbf{1}}_{x{\,\geqslant}y} and

 | w ⁡ ( t, u, v) \displaystyle w(t,u,v) | = ψ ⁡ ( min ⁡ { ( 5 − 4 ​ θ) − ( 3 − 4 ​ θ) ​ v 8 − 6 ​ θ, 5 − α ​ θ − 3 ​ v 8, 1 − 2 ​ u }, 1 + t 2). \displaystyle=\psi\Big(\min\Big\{\;\frac{(5-4{\theta})-(3-4{\theta})v}{8-6{\theta}},\;\frac{5-{\alpha\theta}-3v}{8},\;1-2u\Big\},\,\frac{1+t}{2}\Big). |  |

We also define

(7.4) |  | G 1 \displaystyle G_{1} | = 4 ​ G ​ ( ρ ′) + G ⁡ ( τ 1), \displaystyle=4G(\rho^{\prime})+G(\tau_{1}), | G 3 \displaystyle G_{3} | = G 0 + G ¯ ​ ( τ 2), \displaystyle=G_{0}+\overline{G}(\tau_{2}), |  |

 | G 2 \displaystyle G_{2} | = G 0 + G ¯ ​ ( ρ), \displaystyle=G_{0}+\overline{G}(\rho), | G 4 \displaystyle G_{4} | = G 0 + G ¯ ​ ( τ 3), \displaystyle=G_{0}+\overline{G}(\tau_{3}), |  |

where for c ⩽ μ c{\,\leqslant}\mu,

 | G ⁡ ( c) \displaystyle G(c) | = 1 ϵ ​ F ​ ( ϑ ϵ / ϵ) − 1 ϵ ​ ∫ ϵ c d t t ​ f ​ ( ( ϑ ⁡ ( t, ϵ, ϵ) − t) / ϵ) + 1 ϵ ​ ∫ ϵ c ∫ ϵ t d t ​ d u t ​ u ​ F ​ ( ( ϑ ⁡ ( t, u, ϵ) − t − u) / ϵ) \displaystyle=\frac{1}{\epsilon}\,F\big({\boldsymbol{\vartheta}}_{\epsilon}/\epsilon\big)-\frac{1}{\epsilon}\int_{\epsilon}^{c}\frac{\differential{t}}{t}f\big(({\boldsymbol{\vartheta}}(t,\epsilon,\epsilon)-t)/\epsilon\big)+\frac{1}{\epsilon}\int_{\epsilon}^{c}\int_{\epsilon}^{t}\frac{\differential{t}\differential{u}}{tu}F\big(({\boldsymbol{\vartheta}}(t,u,\epsilon)-t-u)/\epsilon\big) |  |

(7.5) |  |  | − ∫ ϵ c ∫ ϵ t ∫ ϵ u d t ​ d u ​ d v t ​ u ​ v 2 f ( ( ϑ ( t, u, v) − t − u − v) / v), \displaystyle\ -\int_{\epsilon}^{c}\int_{\epsilon}^{t}\int_{\epsilon}^{u}\frac{\differential{t}\differential{u}\differential{v}}{tuv^{2}}f\big(({\boldsymbol{\vartheta}}(t,u,v)-t-u-v)/v\big), |  |

and for c > μ c>\mu,

(7.6) |  | G ¯ ​ ( c) \displaystyle\overline{G}(c) | = − 1 ϵ ∫ μ c d t t f ( ( ϑ ( t) − t) / ϵ) + ∫ μ c ∫ ϵ ρ ′ d t ​ d u t ​ u 2 F ( ( ϑ ( t) − t − u) / u) \displaystyle=-\frac{1}{\epsilon}\int_{\mu}^{c}\frac{\differential{t}}{t}f\big(({\boldsymbol{\vartheta}}(t)-t)/\epsilon\big)+\int_{\mu}^{c}\int_{\epsilon}^{\rho^{\prime}}\frac{\differential{t}\differential{u}}{tu^{2}}F\big(({\boldsymbol{\vartheta}}(t)-t-u)/u\big) |  |

as well as

(7.7) |  | G 0 \displaystyle G_{0} | = − 1 ϵ ∫ ρ ′ μ d t t f ( ( ϑ ( t, ϵ, ϵ) − t) / ϵ) + 1 ϵ ∫ ρ ′ μ ∫ ϵ ρ ′ d t ​ d u t ​ u F ( ( ϑ ( t, u, ϵ) − t − u) / ϵ) \displaystyle=-\frac{1}{\epsilon}\int_{\rho^{\prime}}^{\mu}\frac{\differential{t}}{t}f\big(({\boldsymbol{\vartheta}}(t,\epsilon,\epsilon)-t)/\epsilon\big)+\frac{1}{\epsilon}\int_{\rho^{\prime}}^{\mu}\int_{\epsilon}^{\rho^{\prime}}\frac{\differential{t}\differential{u}}{tu}F\big(({\boldsymbol{\vartheta}}(t,u,\epsilon)-t-u)/\epsilon\big) |  |

 |  | − ∫ ρ ′ μ ∫ ϵ ρ ′ ∫ ϵ u d t ​ d u ​ d v t ​ u ​ v 2 f ( ( ϑ ( t, u, v) − t − u − v) / v). \displaystyle\ -\int_{\rho^{\prime}}^{\mu}\int_{\epsilon}^{\rho^{\prime}}\int_{\epsilon}^{u}\frac{\differential{t}\differential{u}\differential{v}}{tuv^{2}}f\big(({\boldsymbol{\vartheta}}(t,u,v)-t-u-v)/v\big). |  |

We similarly let

 | G 5 \displaystyle G_{5} | = 1 ϵ ​ ∫ ρ ′ μ ∫ ρ ′ t d t ​ d u t ​ u ​ F ​ ( ( ϑ ⁡ ( t, u, ϵ) − t − u) / ϵ) + 1 ρ ′ ​ ∫ μ τ 2 ∫ ρ ′ t d t ​ d u t ​ u ​ F ​ ( ( ϑ ⁡ ( t) − t − u) / ρ ′) \displaystyle=\frac{1}{\epsilon}\int_{\rho^{\prime}}^{\mu}\int_{\rho^{\prime}}^{t}\frac{\differential{t}\differential{u}}{tu}\,F\big(({\boldsymbol{\vartheta}}(t,u,\epsilon)-t-u)/\epsilon\big)\ +\ \frac{1}{\rho^{\prime}}\int_{\mu}^{\tau_{2}}\int_{\rho^{\prime}}^{t}\frac{\differential{t}\differential{u}}{tu}\,F\big(({\boldsymbol{\vartheta}}(t)-t-u)/\rho^{\prime}\big) |  |

(7.8) |  |  | − ∫ ρ ′ μ ∫ ρ ′ t ∫ ϵ ρ ′ d t ​ d u ​ d v t ​ u ​ v 2 f ( ( ϑ ( t, u, v) − t − u − v) / v), \displaystyle\ -\int_{\rho^{\prime}}^{\mu}\int_{\rho^{\prime}}^{t}\int_{\epsilon}^{\rho^{\prime}}\frac{\differential{t}\differential{u}\differential{v}}{tuv^{2}}\,f\big(({\boldsymbol{\vartheta}}(t,u,v)-t-u-v)/v\big), |  |

 | G 6 \displaystyle G_{6} | = 1 ρ ′ ​ ∫ τ 2 τ 3 ∫ ρ ′ τ 1 d t ​ d u t ​ u ​ F ​ ( ( ϑ ⁡ ( t) − t − u) / ρ ′), \displaystyle=\frac{1}{\rho^{\prime}}\int_{\tau_{2}}^{\tau_{3}}\int_{\rho^{\prime}}^{\tau_{1}}\frac{\differential{t}\differential{u}}{tu}\,F\big(({\boldsymbol{\vartheta}}(t)-t-u)/\rho^{\prime}\big), |  |

 | G 7 \displaystyle G_{7} | = 1 ϵ ​ ∫ ρ ′ τ 1 ∫ ρ ′ t d t ​ d u t ​ u ​ F ​ ( ( ϑ ϵ − t − u) / ϵ) \displaystyle=\frac{1}{\epsilon}\int_{\rho^{\prime}}^{\tau_{1}}\int_{\rho^{\prime}}^{t}\frac{\differential{t}\differential{u}}{tu}\,F\big(({\boldsymbol{\vartheta}}_{\epsilon}-t-u)/\epsilon\big) |  |

 |  | − ∫ ρ ′ τ 1 ∫ ρ ′ t ∫ ϵ u d t ​ d u ​ d v t ​ u ​ v 2 f ( ( ϑ ( t, u, v) − t − u − v) / v), \displaystyle\ -\int_{\rho^{\prime}}^{\tau_{1}}\int_{\rho^{\prime}}^{t}\int_{\epsilon}^{u}\frac{\differential{t}\differential{u}\differential{v}}{tuv^{2}}\,f\big(({\boldsymbol{\vartheta}}(t,u,v)-t-u-v)/v\big), |  |

 | G 8 \displaystyle G_{8} | = 1 ϵ ​ ∫ τ 1 μ ∫ ρ ′ τ 1 d t ​ d u t ​ u ​ F ​ ( ( ϑ ⁡ ( t, u, ϵ) − t − u) / ϵ) + ∫ μ τ 2 ∫ ρ ′ τ 1 d t ​ d u t ​ u 2 ​ F ​ ( ( ϑ ⁡ ( t) − t − u) / u) \displaystyle=\frac{1}{\epsilon}\int_{\tau_{1}}^{\mu}\int_{\rho^{\prime}}^{\tau_{1}}\frac{\differential{t}\differential{u}}{tu}\,F\big(({\boldsymbol{\vartheta}}(t,u,\epsilon)-t-u)/\epsilon\big)\ +\int_{\mu}^{\tau_{2}}\int_{\rho^{\prime}}^{\tau_{1}}\frac{\differential{t}\differential{u}}{tu^{2}}\,F\big(({\boldsymbol{\vartheta}}(t)-t-u)/u\big) |  |

 |  | − ∫ τ 1 μ ∫ ρ ′ τ 1 ∫ ϵ u d t ​ d u ​ d v t ​ u ​ v 2 f ( ( ϑ ( t, u, v) − t − u − v) / v). \displaystyle\ -\int_{\tau_{1}}^{\mu}\int_{\rho^{\prime}}^{\tau_{1}}\int_{\epsilon}^{u}\frac{\differential{t}\differential{u}\differential{v}}{tuv^{2}}\,f\big(({\boldsymbol{\vartheta}}(t,u,v)-t-u-v)/v\big). |  |

Recall the standard linear sieve functions F, f F,f satisfy F ⁡ ( s) = 2 ​ e γ / s F(s)=2e^{\gamma}/s for s ∈ [1, 3] s\in[1,3], f ⁡ ( s) = 2 ​ e γ ​ log ⁡ ( s − 1) / s f(s)=2e^{\gamma}\log(s-1)/s for s ∈ [2, 4] s\in[2,4] and F ⁡ ( s) = 2 ​ e γ / s ⋅ [1 + ∫ 2 s − 1 f ⁡ ( t) ​ d t] F(s)=2e^{\gamma}/s\cdot[1+\int_{2}^{s-1}f(t)\differential{t}] for all s ⩾ 1 s{\,\geqslant}1.

We also use the savings from Wu [36] over G 2 G_{2}. Namely,

(7.9) |  | H 2 Wu \displaystyle H_{2}^{\rm Wu} | = ∫ μ ρ ∫ ϵ ρ ′ d t ​ d u t ​ u 2 ​ F Wu ​ ( ( ϑ ⁡ ( t) − t − u) / u), \displaystyle=\int_{\mu}^{\rho}\int_{\epsilon}^{\rho^{\prime}}\frac{\differential{t}\differential{u}}{tu^{2}}F^{\rm Wu}\big(({\boldsymbol{\vartheta}}(t)-t-u)/u\big), |  |

where F Wu F^{\rm Wu} is given by F Wu ​ ( s) = F ⁡ ( s) ⋅ H ϑ Wu ​ ( s) F^{\rm Wu}(s)=F(s)\cdot H_{\boldsymbol{\vartheta}}^{\rm Wu}(s). Here the savings function H ϑ Wu H_{\boldsymbol{\vartheta}}^{\rm Wu} is monotonically increasing in the level of distribution ϑ {\boldsymbol{\vartheta}}. For ϑ = 4 / 7 {\boldsymbol{\vartheta}}=4/7 and parameters as in Tables 1 and 2 [36, pp.30–32],

 | H 4 / 7 Wu ​ ( t) ⩾ { 0.0287118 if ​ 2.0 ⩽ t ⩽ 2.1, 0.0280509 if ​ 2.1 < t ⩽ 2.2, 0.0264697 if ​ 2.2 < t ⩽ 2.3, 0.0241936 if ​ 2.3 < t ⩽ 2.4, 0.0214619 if ​ 2.4 < t ⩽ 2.5, 0.0183875 if ​ 2.5 < t ⩽ 2.6, 0.0149960 if ​ 2.6 < t ⩽ 2.7, 0.0117724 if ​ 2.7 < t ⩽ 2.8, 0.0094724 if ​ 2.8 < t ⩽ 2.9, 0.0090024 if ​ 2.9 < t ⩽ 3.0, 0 else. H_{4/7}^{\rm Wu}(t)\ {\,\geqslant}\ \begin{cases}0.0287118\qquad\text{if}\ 2.0\,{\,\leqslant}\,t{\,\leqslant}\,2.1,\\ 0.0280509\qquad\text{if}\ 2.1<t{\,\leqslant}\,2.2,\\ 0.0264697\qquad\text{if}\ 2.2<t{\,\leqslant}\,2.3,\\ 0.0241936\qquad\text{if}\ 2.3<t{\,\leqslant}\,2.4,\\ 0.0214619\qquad\text{if}\ 2.4<t{\,\leqslant}\,2.5,\\ 0.0183875\qquad\text{if}\ 2.5<t{\,\leqslant}\,2.6,\\ 0.0149960\qquad\text{if}\ 2.6<t{\,\leqslant}\,2.7,\\ 0.0117724\qquad\text{if}\ 2.7<t{\,\leqslant}\,2.8,\\ 0.0094724\qquad\text{if}\ 2.8<t{\,\leqslant}\,2.9,\\ 0.0090024\qquad\text{if}\ 2.9<t{\,\leqslant}\,3.0,\\ 0\qquad\qquad\qquad\textnormal{else.}\end{cases} |  |

Consider the set of shifted primes 𝒜 = { | p − a |: p ⩽ x } \mathcal{A}=\{|p-a|:p{\,\leqslant}\,x\}, and recall the main object of interest is the sifted sum,

 | S ( 𝒜, z):= #{ n ∈ A: p ∣ n ⟹ p ⩾ z and p ∤ a }. \displaystyle S(\mathcal{A},z):=\#\{n\in A\;:\;p\mid n\implies p{\,\geqslant}\,z\ \ {\rm and}\ \ p\nmid a\}. |  |

###### Proposition 7.1.

For a ≠ 0 a\neq 0 let 𝒜 = { | p − a |: p ⩽ x } \mathcal{A}=\{|p-a|:p{\,\leqslant}\,x\}. Let 0 < ϵ ⩽ 0.1 ⩽ ρ ′ ⩽ τ 1 < μ ⩽ τ 2 < τ 3 ⩽ ρ ⩽ 0.3 0<\epsilon{\,\leqslant}0.1{\,\leqslant}\rho^{\prime}{\,\leqslant}\tau_{1}<\mu{\,\leqslant}\tau_{2}<\tau_{3}{\,\leqslant}\rho{\,\leqslant}0.3. Then for I n I_{n}, G n G_{n}, and G ⁡ ( c) G(c) as in ( 7.1), ( 7.4), ( 7.1), and ( 7.1), we have

(7.10) |  | S ⁡ ( 𝒜, x ρ) ≲ Π a ​ ( x) 5 ​ e γ ​ ( ∑ 1 ⩽ n ⩽ 8 G n − H 2 Wu + G ⁡ ( μ) ​ ∑ 9 ⩽ n ⩽ 21 I n). \displaystyle S(\mathcal{A},x^{\rho})\ \lesssim\ \frac{\Pi_{a}(x)}{5e^{\gamma}}\bigg(\sum_{1{\,\leqslant}n{\,\leqslant}8}G_{n}-H_{2}^{\textnormal{Wu}}\ +\ G(\mu)\sum_{9{\,\leqslant}\,n{\,\leqslant}\,21}I_{n}\bigg). |  |

###### Proof.

This follows just as in the proof of [25, Proposition 6.3] (more precisely, (6.24) in [25]), using Proposition 6.6 above as the key level of distribution input in place of [25, Proposition 5.5]. Also G 2 Wu = G 2 − H 2 Wu G_{2}^{\textnormal{Wu}}=G_{2}-H_{2}^{\textnormal{Wu}} and we use μ \mu in place of 1 / 5 1/5. ∎

### 7.2. Deduction of Theorem 1.1

Let a = − 2 a=-2. The primes in our set 𝒜 = { p + 2: p ⩽ x } \mathcal{A}=\{p+2:p{\,\leqslant}x\} count twin primes, and so π 2 ​ ( x) ⩽ S ⁡ ( 𝒜, z) + O ⁡ ( x) \pi_{2}(x){\,\leqslant}\,S(\mathcal{A},z)+O(\sqrt{x}) for z ⩽ x z{\,\leqslant}\sqrt{x}.

When α = 0 \alpha=0, we may simplify ϑ α ​ ( t) {\boldsymbol{\vartheta}}_{\alpha}(t) in ( 7.2) as

(7.11) |  | ϑ 0 ​ ( t) = { 1 − ( 3 / 2 − 2 ​ θ) ​ t 1 + θ if t > μ 0, 1 + t 2 if t ⩽ μ 0., where μ 0 = 1 − θ 4 − 3 ​ θ. \displaystyle{\boldsymbol{\vartheta}_{0}}(t)=\begin{cases}\frac{1-(3/2-2{\theta})t}{1+{\theta}}&\text{if}\ \ t>\mu_{0},\\ \frac{1+t}{2}&\text{if}\ \ t{\,\leqslant}\,\mu_{0}.\end{cases},\qquad{\rm where}\quad\mu_{0}=\frac{1-{\theta}}{4-3{\theta}}. |  |

Numerically μ 0 = 25 107 ≈ 0.233 \mu_{0}=\frac{25}{107}\approx 0.233, since θ = 7 32 {\theta}=\frac{7}{32} by Kim–Sarnak [19]. We set parameters

 | ρ \displaystyle\rho | = 0.275, \displaystyle=0.275, | τ 3 \displaystyle\tau_{3} | = 0.24589, \displaystyle=0.24589, | μ \displaystyle\mu | = 0.210, \displaystyle=0.210, |  |

(7.12) |  | ρ ′ \displaystyle\rho^{\prime} | = 0.12313, \displaystyle=0.12313, | τ 2 \displaystyle\tau_{2} | = 0.211, \displaystyle=0.211, | ϵ \displaystyle\epsilon | = 0.002. \displaystyle=0.002. |  |

 | τ 1 \displaystyle\tau_{1} | = 0.163 \displaystyle=0.163 |  |

For such choices of parameters, we obtain

 | ∑ 1 ⩽ n ⩽ 8 G n ⩽ 27.7086, H 2 Wu ⩾ 0.019309, G ⁡ ( μ) ⩽ 5.90044, ∑ 9 ⩽ n ⩽ 21 I n ⩽ 0.180677. \displaystyle\sum_{1{\,\leqslant}n{\,\leqslant}8}G_{n}\ {\,\leqslant}\ 27.7086,\quad H_{2}^{\rm Wu}\ {\,\geqslant}\ 0.019309,\qquad G(\mu)\ {\,\leqslant}\ 5.90044,\quad\sum_{9{\,\leqslant}n{\,\leqslant}21}I_{n}\ {\,\leqslant}\ 0.180677. |  |

These computations were performed in Mathematica, using the ‘SieveFunction.m’ standard package (Galway). We also record the integrals I n I_{n}, G n G_{n} in the table below.

n n | G n G_{n} | n n | I n I_{n} | n n | I n I_{n} |

1 | 38.9215 | 9 | 0.0330294 | 17 | 0.000282 |

2 | − - 5.80465 | 10 | 0.0247846 | 18 | 0.000287 |

3 | − - 4.10858 | 11 | 0.0084670 | 19 | 0.000231 |

4 | − - 5.17066 | 12 | 0.0167535 | 20 | ⩽ 3.80 ⋅ 10 − 6 {\,\leqslant}\ 3.80\cdot 10^{-6} |

5 | 1.87682 | 13 | 0.0566827 | 21 | ⩽ 1.02 ⋅ 10 − 8 {\,\leqslant}\ 1.02\cdot 10^{-8} |

6 | 0.636696 | 14 | 0.0264459 |  |  |

7 | 0.428799 | 15 | 0.0136088 |  |  |

8 | 0.928682 | 16 | 0.0000988 |  |  |

Thus by Proposition 7.1, we obtain the bound

 | π 2 ​ ( x) \displaystyle\pi_{2}(x)\  | ≲ S ⁡ ( 𝒜, x ρ) ≲ Π 2 ​ ( x) 5 ​ e γ ​ ( ∑ 1 ⩽ n ⩽ 8 G n − H 2 Wu + G ⁡ ( μ) ​ ∑ 9 ⩽ n ⩽ 21 I n) \displaystyle\lesssim\ S(\mathcal{A},x^{\rho})\ \lesssim\ \frac{\Pi_{2}(x)}{5e^{\gamma}}\bigg(\sum_{1{\,\leqslant}n{\,\leqslant}8}G_{n}-H_{2}^{\textnormal{Wu}}\ +\ G(\mu)\sum_{9{\,\leqslant}\,n{\,\leqslant}\,21}I_{n}\bigg) |  |

(7.13) |  |  | ≲ 3.22899 ​ Π 2 ​ ( x). \displaystyle\lesssim\ 3.22899\,\Pi_{2}(x). |  |

This completes the proof of Theorem 1.1.

### 7.3. Deduction of Theorem 1.2

Let x = a x=a. The primes in our set 𝒜 = { a − p: p ⩽ a } \mathcal{A}=\{a-p:p{\,\leqslant}a\} count Goldbach representations of a a, and so G ⁡ ( a) ⩽ S ⁡ ( 𝒜, z) + O ⁡ ( a) {\rm G}(a){\,\leqslant}\,S(\mathcal{A},z)+O(\sqrt{a}) for z ⩽ a z{\,\leqslant}\sqrt{a}.

When α = 1 \alpha=1, we may simplify ϑ α ​ ( t) {\boldsymbol{\vartheta}}_{\alpha}(t) in ( 7.2) as

 | ϑ 1 ​ ( t) = { 1 − θ + 3 ​ t 2 if t > μ 1, 1 + t 2 if t ⩽ μ 1., where μ 1 = 1 − θ 4. \displaystyle{\boldsymbol{\vartheta}_{1}}(t)=\begin{cases}1-\tfrac{{\theta}+3t}{2}&\text{if}\ \ t>\mu_{1},\\ \frac{1+t}{2}&\text{if}\ \ t{\,\leqslant}\,\mu_{1}.\end{cases},\qquad{\rm where}\quad\mu_{1}=\frac{1-{\theta}}{4}. |  |

Numerically μ 1 = 25 128 ≈ 0.195 \mu_{1}=\frac{25}{128}\approx 0.195, since θ = 7 32 {\theta}=\frac{7}{32} by Kim–Sarnak [19]. We set parameters

 | ρ \displaystyle\rho | = 0.2445, \displaystyle=0.2445, | τ 3 \displaystyle\tau_{3} | = 0.224, \displaystyle=0.224, | μ \displaystyle\mu | = 0.169, \displaystyle=0.169, |  |

(7.14) |  | ρ ′ \displaystyle\rho^{\prime} | = 0.128, \displaystyle=0.128, | τ 2 \displaystyle\tau_{2} | = 0.205, \displaystyle=0.205, | ϵ \displaystyle\epsilon | = 0.002. \displaystyle=0.002. |  |

 | τ 1 \displaystyle\tau_{1} | = 0.163 \displaystyle=0.163 |  |

For such choices of parameters, we obtain

 | ∑ 1 ⩽ n ⩽ 8 G n ⩽ 29.6847, H 2 Wu ⩾ 0.025787, G ⁡ ( μ) ⩽ 6.34862, ∑ 9 ⩽ n ⩽ 21 I n ⩽ 0.084421. \displaystyle\sum_{1{\,\leqslant}n{\,\leqslant}8}G_{n}\ {\,\leqslant}\ 29.6847,\quad H_{2}^{\rm Wu}\ {\,\geqslant}\ 0.025787,\qquad G(\mu)\ {\,\leqslant}\ 6.34862,\quad\sum_{9{\,\leqslant}n{\,\leqslant}21}I_{n}\ {\,\leqslant}\ 0.084421. |  |

These computations were performed in Mathematica, using the ‘SieveFunction.m’ standard package (Galway). We also record the integrals I n I_{n}, G n G_{n} in the table below.

n n | G n G_{n} | n n | I n I_{n} | n n | I n I_{n} |

1 | 37.9006 | 9 | 0.0153459 | 17 | ⩽ 4.63 ⋅ 10 − 5 {\,\leqslant}\ 4.63\cdot 10^{-5} |

2 | − - 4.13212 | 10 | 0.0130481 | 18 | ⩽ 6.53 ⋅ 10 − 5 {\,\leqslant}\ 6.53\cdot 10^{-5} |

3 | − - 3.29997 | 11 | 0.0023251 | 19 | 0.000109 |

4 | − - 3.80586 | 12 | 0.0095937 | 20 | ⩽ 9.20 ⋅ 10 − 7 {\,\leqslant}\ 9.20\cdot 10^{-7} |

5 | 1.53741 | 13 | 0.0296655 | 21 | ⩽ 2.62 ⋅ 10 − 9 {\,\leqslant}\ 2.62\cdot 10^{-9} |

6 | 0.365983 | 14 | 0.0093697 |  |  |

7 | 0.362074 | 15 | 0.0048386 |  |  |

8 | 0.756609 | 16 | ⩽ 1.19 ⋅ 10 − 5 {\,\leqslant}\ 1.19\cdot 10^{-5} |  |  |

Thus by Proposition 7.1, we obtain the bound

 | G ⁡ ( a) \displaystyle{\rm G}(a)\  | ≲ S ⁡ ( 𝒜, a ρ) ≲ Π a ​ ( a) 5 ​ e γ ​ ( ∑ 1 ⩽ n ⩽ 8 G n − H 2 Wu + G ⁡ ( μ) ​ ∑ 9 ⩽ n ⩽ 21 I n) \displaystyle\lesssim\ S(\mathcal{A},a^{\rho})\ \lesssim\ \frac{\Pi_{a}(a)}{5e^{\gamma}}\bigg(\sum_{1{\,\leqslant}n{\,\leqslant}8}G_{n}-H_{2}^{\textnormal{Wu}}\ +\ G(\mu)\sum_{9{\,\leqslant}\,n{\,\leqslant}\,21}I_{n}\bigg) |  |

(7.15) |  |  | ≲ 3.39064 ​ Π a ​ ( a). \displaystyle\lesssim\ 3.39064\,\Pi_{a}(a). |  |

This completes the proof of Theorem 1.2.

## 8. Spectral large sieve

In this section, we briefly recall preliminary results from [9] on the spectral theory of automorphic forms, starting with the Kuznetsov trace formula. See [9, §1] for definitions and further details.

###### Theorem 8.1 (Kuznetsov trace formula).

Let m, n m,n be positive integers and φ {\varphi} a C 3 C^{3} -class function with compact support in ( 0, ∞) (0,\infty). Let 𝔞 \mathfrak{a}, 𝔟 \mathfrak{b} be cusps of Γ = Γ 0 ​ ( q) \Gamma=\Gamma_{0}(q). Then we have

 | ∑ γ ∈ ℝ ∃ ( ∗ ∗ γ ∗) ∈ σ 𝔞 − 1 ​ Γ ​ σ 𝔟 \displaystyle\sum_{\begin{subarray}{c}\gamma\in{\mathbb{R}}\\ \exists\smallmatrixquantity(\lx@physics@smallmatrix*&*\\\gamma&*\endlx@physics@smallmatrix)\in\sigma_{\mathfrak{a}}^{-1}\Gamma\sigma_{\mathfrak{b}}\end{subarray}} | 1 γ ​ S 𝔞 ​ 𝔟 ​ ( m, n, γ) ​ φ ​ ( 4 ​ π γ ​ m ​ n) \displaystyle\frac{1}{\gamma}S_{\mathfrak{a}\mathfrak{b}}(m,n;\gamma)\,{\varphi}\Big(\frac{4\pi}{\gamma}\sqrt{mn}\Big) |  |

(8.1) |  |  | = 1 2 ​ π ​ ∑ even ​ k ∑ 1 ⩽ j ⩽ θ k ​ ( q) i k ​ ( k − 1)! ( 4 ​ π ​ m ​ n) k − 1 ​ ψ j ​ k ​ ( 𝔞, m) ¯ ​ ψ j ​ k ​ ( 𝔟, n) ​ φ ~ ​ ( k − 1) \displaystyle=\frac{1}{2\pi}\sum_{{\rm even}\,k}\sum_{1{\,\leqslant}j{\,\leqslant}\theta_{k}(q)}\frac{i^{k}(k-1)!}{(4\pi\sqrt{mn})^{k-1}}\,\overline{\psi_{jk}(\mathfrak{a},m)}\psi_{jk}(\mathfrak{b},n)\,\widetilde{{\varphi}}(k-1) |  |

 |  | + ∑ j ⩾ 1 ρ j ​ 𝔞 ​ ( m) ¯ ρ j ​ 𝔟 ( n) φ ^ ​ ( κ j) cosh ⁡ π ​ κ j + 1 π ∑ 𝔠 ∫ ℝ ( n m) i ​ r φ 𝔠 ​ 𝔞 ​ m ​ ( 1 2 + i ​ r) ¯ φ 𝔠 ​ 𝔟 ​ n ( 1 2 + i r) φ ^ ( r) d r \displaystyle\ +\sum_{j{\,\geqslant}1}\overline{\rho_{j\mathfrak{a}}(m)}\rho_{j\mathfrak{b}}(n)\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}+\frac{1}{\pi}\sum_{\mathfrak{c}}\int_{\mathbb{R}}\Big(\frac{n}{m}\Big)^{ir}\overline{{\varphi}_{\mathfrak{c}\mathfrak{a}m}(\tfrac{1}{2}+ir)}{\varphi}_{\mathfrak{c}\mathfrak{b}n}(\tfrac{1}{2}+ir)\widehat{{\varphi}}(r)\differential{r} |  |

and

 | ∑ γ ∈ ℝ ∃ ( ∗ ∗ γ ∗) ∈ σ 𝔞 − 1 ​ Γ ​ σ 𝔟 1 γ \displaystyle\sum_{\begin{subarray}{c}\gamma\in{\mathbb{R}}\\ \exists\smallmatrixquantity(\lx@physics@smallmatrix*&*\\\gamma&*\endlx@physics@smallmatrix)\in\sigma_{\mathfrak{a}}^{-1}\Gamma\sigma_{\mathfrak{b}}\end{subarray}}\frac{1}{\gamma} | S 𝔞 ​ 𝔟 ​ ( m, − n, γ) ​ φ ​ ( 4 ​ π γ ​ m ​ n) \displaystyle S_{\mathfrak{a}\mathfrak{b}}(m,-n;\gamma)\,{\varphi}\Big(\frac{4\pi}{\gamma}\sqrt{mn}\Big) |  |

(8.2) |  |  | = ∑ j ⩾ 1 ρ j ​ 𝔞 ​ ( m) ​ ρ j ​ 𝔟 ​ ( n) ​ φ ˇ ​ ( κ j) cosh ⁡ π ​ κ j + 1 π ​ ∑ 𝔠 ∫ ℝ ( m ​ n) i ​ r ​ φ 𝔠 ​ 𝔞 ​ m ​ ( 1 2 + i ​ r) ​ φ 𝔠 ​ 𝔟 ​ n ​ ( 1 2 + i ​ r) ​ φ ˇ ​ ( r) ​ d r \displaystyle=\sum_{j{\,\geqslant}1}\rho_{j\mathfrak{a}}(m)\rho_{j\mathfrak{b}}(n)\frac{\check{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}+\frac{1}{\pi}\sum_{\mathfrak{c}}\int_{\mathbb{R}}(mn)^{ir}{\varphi}_{\mathfrak{c}\mathfrak{a}m}(\tfrac{1}{2}+ir){\varphi}_{\mathfrak{c}\mathfrak{b}n}(\tfrac{1}{2}+ir)\check{{\varphi}}(r)\differential{r} |  |

where κ j \kappa_{j} is defined by λ j = 1 4 + κ j 2 \lambda_{j}=\frac{1}{4}+\kappa_{j}^{2}, and the Bessel transforms are defined by

(8.3) |  | φ ~ ​ ( l) \displaystyle\widetilde{{\varphi}}(l) | = ∫ 0 ∞ J l ​ ( y) ​ φ ​ ( y) ​ d y y \displaystyle=\int_{0}^{\infty}J_{l}(y){\varphi}(y)\frac{\differential{y}}{y} |  |

(8.4) |  | φ ^ ​ ( r) \displaystyle\widehat{{\varphi}}(r) | = π sinh ⁡ π ​ r ​ ∫ 0 ∞ J 2 ​ i ​ r ​ ( x) − J − 2 ​ i ​ r ​ ( x) 2 ​ i ​ φ ​ ( x) ​ d x x \displaystyle=\frac{\pi}{\sinh\pi r}\int_{0}^{\infty}\frac{J_{2ir}(x)-J_{-2ir}(x)}{2i}{\varphi}(x)\frac{\differential{x}}{x} |  |

(8.5) |  | φ ˇ ​ ( l) \displaystyle\check{{\varphi}}(l) | = 4 π ​ cosh ⁡ π ​ r ​ ∫ 0 ∞ K 2 ​ i ​ r ​ ( x) ​ φ ​ ( x) ​ d x x \displaystyle=\frac{4}{\pi}\cosh\pi r\int_{0}^{\infty}K_{2ir}(x){\varphi}(x)\frac{\differential{x}}{x} |  |

###### Proof.

This is [9, Theorem 1]. ∎

A key ingredient is the following large sieve inequality for Fourier coefficients of cusp forms (both holomorphic and Maass) and Eisenstein series.

Denote μ ⁡ ( ∞) = 1 / q \mu(\infty)=1/q, and μ ⁡ ( 𝔞) = ( w, q / w) / q \mu(\mathfrak{a})=(w,q/w)\,/q for a cusp 𝔞 = u / w \mathfrak{a}=u/w.

###### Theorem 8.2 (Spectral large sieve).

Let K ⩾ 1 K{\,\geqslant}1, N ⩾ 1 2 N{\,\geqslant}\frac{1}{2}, ϵ > 0 \epsilon>0 be real numbers, a complex sequence 𝐚 = ( a n) n {\bf a}=(a_{n})_{n}, and 𝔞 \mathfrak{a} a cusp Γ 0 ​ ( q) \Gamma_{0}(q). Then each of the following three expressions

(8.6) |  | ∑ 0 < k ⩽ K k ​ even ( k − 1)! ( 4 ​ π) k − 1 ∑ 1 ⩽ j ⩽ θ k ​ ( q) \displaystyle\sum_{\begin{subarray}{c}0<k{\,\leqslant}K\\ k\,{\rm even}\end{subarray}}\frac{(k-1)!}{(4\pi)^{k-1}}\sum_{1{\,\leqslant}j{\,\leqslant}\theta_{k}(q)} | | ∑ n ∼ N a n ​ n − k − 1 2 ​ ψ j ​ k ​ ( 𝔞, n) | 2 \displaystyle\bigg|\sum_{n\sim N}a_{n}n^{-\frac{k-1}{2}}\psi_{jk}(\mathfrak{a},n)\bigg|^{2} |  |

(8.7) |  | ∑ | κ j | ⩽ K 1 cosh ⁡ π ​ κ j \displaystyle\sum_{|\kappa_{j}|{\,\leqslant}K}\frac{1}{\cosh\pi\kappa_{j}} | | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2} |  |

(8.8) |  | ∑ 𝔠 ∫ − K K \displaystyle\sum_{\mathfrak{c}}\int_{-K}^{K} | | ∑ n ∼ N a n ​ n i ​ r ​ φ 𝔠 ​ 𝔞 ​ n ​ ( 1 2 + i ​ r) | 2 ​ d r \displaystyle\bigg|\sum_{n\sim N}a_{n}n^{ir}{\varphi}_{\mathfrak{c}\mathfrak{a}n}(\tfrac{1}{2}+ir)\bigg|^{2}\differential{r} |  |

are each bounded by

 | ≪ ϵ ( K 2 + μ ( 𝔞) N 1 + ϵ) ∥ 𝐚 N ∥ 2 2. \displaystyle\ll_{\epsilon}(K^{2}+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}. |  |

###### Proof.

This is [9, Theorem 2]. ∎

For the smallest positive eigenvalue λ 1 = λ 1 ​ ( q) \lambda_{1}=\lambda_{1}(q) for Γ = Γ 0 ​ ( q) \Gamma=\Gamma_{0}(q), recall θ = sup q θ q {\theta}=\sup_{q}{\theta}_{q} for

(8.9) |  | θ q = max ⁡ ( 0, 1 − 4 ​ λ 1). \displaystyle{\theta}_{q}=\max\big(0,\,\sqrt{1-4\lambda_{1}}\big). |  |

Note Selberg’s lower bound λ 1 ​ ( q) ⩾ 3 / 16 \lambda_{1}(q){\,\geqslant}3/16 implies θ q ⩽ 1 / 2 {\theta}_{q}{\,\leqslant}1/2. The current record bound is θ q ⩽ 7 / 32 {\theta}_{q}{\,\leqslant}7/32 by Kim–Sarnak [19].

We also use bounds on Bessel-Kuznetsov transforms f ˇ ​ ( r), f ^ ​ ( r), f ~ ​ ( r) \check{f}(r),\,\widehat{f}(r),\,\widetilde{f}(r) from ( 8.3)–( 8.5).

###### Lemma 8.3.

Suppose f ∈ 𝒞 2 f\in\mathcal{C}^{2} is supported in [X, 8 ​ X] [X,8X] and

(8.10) |  | ‖ f ‖ ∞ ⩽ 1, ‖ f ′ ‖ 1 ≪ 1, ‖ f ′′ ‖ 1 ≪ 1 X. \displaystyle\|f\|_{\infty}{\,\leqslant}1,\qquad\|f^{\prime}\|_{1}\ll 1,\qquad\|f^{\prime\prime}\|_{1}\ll\frac{1}{X}. |  |

Then we have

(8.11) |  | f ˇ ​ ( i ​ r), f ^ ​ ( i ​ r) \displaystyle\check{f}(ir),\,\widehat{f}(ir)\  | ≪ 1 + X − 2 ​ r 1 + X r ∈ ( 0, 1 2) \displaystyle\ll\ \frac{1+X^{-2r}}{1+X}\qquad\qquad r\in(0,\tfrac{1}{2}) |  |

and

(8.12) |  | f ˇ ​ ( r), f ^ ​ ( r), f ~ ​ ( r) \displaystyle\check{f}(r),\,\widehat{f}(r),\,\widetilde{f}(r)\  | ≪ 1 + | log ⁡ X | 1 + X r ∈ ℝ \displaystyle\ll\ \frac{1+|\log X|}{1+X}\qquad\qquad r\in{\mathbb{R}} |  |

(8.13) |  |  | ≪ | r | − 3 / 2 + X / | r | 2 | r | ⩾ 1 \displaystyle\ll\ \ |r|^{-3/2}+X/|r|^{2}\qquad\ |r|{\,\geqslant}1 |  |

(8.14) |  |  | ≪ | r | − 5 / 2 + X / | r | 3 | r | ⩾ max ( 2 X, 1). \displaystyle\ll\ |r|^{-5/2}+X/|r|^{3}\qquad|r|{\,\geqslant}\max(2X,1). |  |

###### Proof.

This is [2, Lemma 2.1] with Z = 1 Z=1, correcting an error in ( 8.14) of [9, Lemma 7.1]. ∎

## 9. Exceptional spectrum

In this section, we bound the contribution of exceptional eigenvalues λ j < 1 / 4 \lambda_{j}<1/4. For simplicity of exposition, we assume q 0 = 1 q_{0}=1. Indeed, q 0 = 1 q_{0}=1 is the only case needed for our applications in this article. Results may obtained with general q 0 q_{0} -dependence, as in [11, §4.2.3].

### 9.1. The Case of Fixed Level

We first consider the exceptional spectrum for a fixed congruence subgroup Γ 0 ​ ( q) \Gamma_{0}(q). For a sequence 𝐚 = ( a n) n {\bf a}=(a_{n})_{n} recall the norm ‖ 𝐚 N ‖ 2 2 = ∑ n ∼ N | a n | 2 \|{\bf a}_{N}\|_{2}^{2}=\sum_{n\sim N}|a_{n}|^{2}.

Let φ ⁡ ( x) ∈ 𝒞 ∞ {\varphi}(x)\in\mathcal{C}^{\infty} be a test function, whose derivatives satisfy φ ( l) ​ ( x) ≪ x − l {\varphi}^{(l)}(x)\ll x^{-l}. We have the following result generalizing [9, Theorem 5]. In private communication, A. Pascadi has independently obtained corresponding results.

###### Theorem 9.1.

Let N, X ⩾ 1 N,X{\,\geqslant}1, a sequence 𝐚 = ( a n) n ⊂ ℂ {\bf a}=(a_{n})_{n}\subset{\mathbb{C}}, and 𝔞 \mathfrak{a} a cusp Γ 0 ​ ( q) \Gamma_{0}(q). Then we have

(9.1) |  | ∑ λ j < 1 / 4 ( q) X 2 ​ i ​ κ j | ∑ n ∼ N a n ρ j ​ 𝔞 ( n) | 2 ≪ ϵ ( 1 + ( μ ( 𝔞) N X) θ q) ( 1 + ( μ ( 𝔞) N 1 + ϵ) 1 − θ q) ∥ 𝐚 N ∥ 2 2. \displaystyle\sum_{\lambda_{j}<1/4}^{(q)}X^{2i\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}\ \ll_{\epsilon}\ \big(1+(\mu(\mathfrak{a})NX)^{{\theta}_{q}}\big)(1+(\mu(\mathfrak{a})N^{1+\epsilon})^{1-{\theta}_{q}})\|{\bf a}_{N}\|_{2}^{2}. |  |

###### Proof.

Recall λ j = 1 4 + κ j 2 ⩾ 3 16 \lambda_{j}=\tfrac{1}{4}+\kappa_{j}^{2}{\,\geqslant}\frac{3}{16} by the Selberg bound, so κ j 2 > − 1 16 \kappa_{j}^{2}>-\tfrac{1}{16}. For exceptional λ j < 1 4 \lambda_{j}<\tfrac{1}{4} this means i ​ κ j ∈ [0, 1 4] i\kappa_{j}\in[0,\tfrac{1}{4}]. Thus if μ ⁡ ( 𝔞) ​ N > ϵ \mu(\mathfrak{a})N>\epsilon, by the spectral large sieve in Theorem 8.2 with K = 1 4 K=\tfrac{1}{4}, (note cosh ⁡ π ​ κ ≫ 1 \cosh\pi\kappa\gg 1 for | κ | ⩽ 1 / 4 |\kappa|{\,\leqslant}1/4)

 | ∑ λ j < 1 / 4 ( q) X 2 ​ i ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle\sum_{\lambda_{j}<1/4}^{(q)}X^{2i\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2} | ⩽ ∑ | κ j | ⩽ 1 4 X θ q cosh ⁡ π ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle{\,\leqslant}\sum_{|\kappa_{j}|{\,\leqslant}\tfrac{1}{4}}\frac{X^{{\theta}_{q}}}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2} |  |

 |  | ≪ ϵ X θ q ( 1 + μ ( 𝔞) N 1 + ϵ) ∥ 𝐚 N ∥ 2 2 \displaystyle\ll_{\epsilon}X^{{\theta}_{q}}(1+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ≪ ( 1 + ( μ ⁡ ( 𝔞) ​ N ​ X) θ q) ​ ( 1 + ( μ ⁡ ( 𝔞) ​ N 1 + ϵ) 1 − θ q) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\ll\big(1+(\mu(\mathfrak{a})NX)^{{\theta}_{q}}\big)(1+(\mu(\mathfrak{a})N^{1+\epsilon})^{1-{\theta}_{q}})\|{\bf a}_{N}\|_{2}^{2}. |  |

Hence it suffices to assume Y:= 4 ​ π ​ μ ​ ( 𝔞) ​ N < ϵ Y:=4\pi\mu(\mathfrak{a})N<\epsilon is sufficiently small. Let φ ⁡ ( x) = w ⁡ ( x / Y) {\varphi}(x)=w(x/Y) be a test function supported on [Y, 2 ​ Y] [Y,2Y]. We apply the Kuznetsov formula with 𝔞 = 𝔟 \mathfrak{a}=\mathfrak{b}, multiply both sides by a m ¯ ​ a n \overline{a_{m}}a_{n} and sum over m, n ∼ N m,n\sim N,

 | 0 \displaystyle 0 | = ∑ m, n ∼ N a m ¯ ​ a n ​ ∑ γ ∈ ℝ ∃ ( ∗ ∗ γ ∗) ∈ σ 𝔞 − 1 ​ Γ ​ σ 𝔞 1 γ ​ S 𝔞 ​ 𝔞 ​ ( m, n, γ) ​ φ ​ ( 4 ​ π γ ​ m ​ n) \displaystyle=\sum_{m,n\sim N}\overline{a_{m}}a_{n}\sum_{\begin{subarray}{c}\gamma\in{\mathbb{R}}\\ \exists\smallmatrixquantity(\lx@physics@smallmatrix*&*\\\gamma&*\endlx@physics@smallmatrix)\in\sigma_{\mathfrak{a}}^{-1}\Gamma\sigma_{\mathfrak{a}}\end{subarray}}\frac{1}{\gamma}S_{\mathfrak{a}\mathfrak{a}}(m,n;\gamma)\,{\varphi}\Big(\frac{4\pi}{\gamma}\sqrt{mn}\Big) |  |

 |  | = 1 2 ​ π ​ ∑ even ​ k φ ~ ​ ( k − 1) ​ ∑ 1 ⩽ j ⩽ θ k ​ ( q) i k ​ ( k − 1)! ( 4 ​ π) k − 1 ​ | ∑ n ∼ N a n ​ n 1 − k 2 ​ ψ j ​ k ​ ( 𝔞, n) | 2 \displaystyle=\frac{1}{2\pi}\sum_{{\rm even}\,k}\widetilde{{\varphi}}(k-1)\sum_{1{\,\leqslant}j{\,\leqslant}\theta_{k}(q)}\frac{i^{k}(k-1)!}{(4\pi)^{k-1}}\,\bigg|\sum_{n\sim N}a_{n}n^{\frac{1-k}{2}}\psi_{jk}(\mathfrak{a},n)\bigg|^{2} |  |

(9.2) |  |  | + ∑ j ⩾ 1 φ ^ ​ ( κ j) cosh ⁡ π ​ κ j | ∑ n ∼ N a n ρ j ​ 𝔞 ( n) | 2 + 1 π ∑ 𝔠 ∫ ℝ | ∑ n ∼ N a n n i ​ r φ 𝔠 ​ 𝔞 ​ n ( 1 2 + i r) | 2 φ ^ ( r) d r \displaystyle+\sum_{j{\,\geqslant}1}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}+\frac{1}{\pi}\sum_{\mathfrak{c}}\int_{\mathbb{R}}\bigg|\sum_{n\sim N}a_{n}\,n^{ir}{\varphi}_{\mathfrak{c}\mathfrak{a}n}(\tfrac{1}{2}+ir)\bigg|^{2}\widehat{{\varphi}}(r)\differential{r} |  |

Importantly, we used that the LHS of ( 9.1) is empty, i.e. the sum of Kloosterman sums S 𝔞 ​ 𝔞 ​ ( m, n, γ) S_{\mathfrak{a}\mathfrak{a}}(m,n;\gamma) with respect to γ ∈ σ 𝔞 − 1 ​ Γ ​ σ 𝔞 \gamma\in\sigma_{\mathfrak{a}}^{-1}\Gamma\sigma_{\mathfrak{a}}. Indeed by Lemma 2.4 μ ​ ( 𝔞) − 1 | γ \mu(\mathfrak{a})^{-1}\mid\gamma, in particular 1 / γ ⩽ μ ⁡ ( 𝔞) 1/\gamma{\,\leqslant}\mu(\mathfrak{a}), so the argument of φ ⁡ ( 4 ​ π ​ m ​ n / γ) {\varphi}(4\pi\sqrt{mn}\,/\gamma) lies below the support Y = 4 ​ π ​ μ ​ ( 𝔞) ​ N Y=4\pi\mu(\mathfrak{a})N of φ {\varphi}.

On the RHS of ( 9.1), we shall apply the spectral large sieve in Theorem 8.2. Indeed, we split regular κ ∈ ℝ \kappa\in{\mathbb{R}} into dyadic ranges | κ | ∼ K |\kappa|\sim K, in which range φ ^ ( κ) ≪ ( K − 5 / 2 + Y / K 3) \widehat{{\varphi}}(\kappa)\ll(K^{-5/2}+Y/K^{3}) by ( 8.14) in Lemma 8.3. Thus by Theorem 8.2,

 | ∑ | κ j | ∼ K κ j ∈ ℝ φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle\sum_{\begin{subarray}{c}|\kappa_{j}|\sim K\\ \kappa_{j}\in{\mathbb{R}}\end{subarray}}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2} | ≪ ( K − 5 / 2 + Y / K 3) ( K 2 + μ ( 𝔞) N 1 + ϵ) ∥ 𝐚 N ∥ 2 2 \displaystyle\ll(K^{-5/2}+Y/K^{3})\,(K^{2}+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ≪ ( 1 K + μ ⁡ ( 𝔞) ​ N 1 + ϵ K 5 / 2) ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\ll\,(\frac{1}{\sqrt{K}}+\frac{\mu(\mathfrak{a})N^{1+\epsilon}}{K^{5/2}})\|{\bf a}_{N}\|_{2}^{2} |  |

recalling Y < ϵ Y<\epsilon. Thus summing over all dyadic intervals, the Maass regular spectra is

 | ∑ λ j ⩾ 1 / 4 φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 ≪ ∑ K = 2 l ⩾ 1 / 4 ( 1 K + μ ⁡ ( 𝔞) ​ N 1 + ϵ K 5 / 2) ​ ‖ 𝐚 N ‖ 2 2 ≪ ( 1 + μ ⁡ ( 𝔞) ​ N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\sum_{\lambda_{j}{\,\geqslant}1/4}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}\ll\sum_{K=2^{l}{\,\geqslant}1/4}(\frac{1}{\sqrt{K}}+\frac{\mu(\mathfrak{a})N^{1+\epsilon}}{K^{5/2}})\|{\bf a}_{N}\|_{2}^{2}\ll(1+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}. |  |

Thus for the RHS of ( 9.1), we may similarly bound the regular spectra (with holomorphic and Eisenstein contributions) by O ⁡ ( 1 + μ ⁡ ( 𝔞) ​ N 1 + ϵ) O(1+\mu(\mathfrak{a})N^{1+\epsilon}), so that

 |  | ∑ λ j ⩾ 1 / 4 φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 + 1 π ​ ∑ 𝔠 ∫ ℝ | ∑ n ∼ N a n ​ n i ​ r ​ φ 𝔠 ​ 𝔞 ​ n ​ ( 1 2 + i ​ r) | 2 ​ φ ^ ​ ( r) ​ d r \displaystyle\sum_{\lambda_{j}{\,\geqslant}1/4}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}+\frac{1}{\pi}\sum_{\mathfrak{c}}\int_{\mathbb{R}}\bigg|\sum_{n\sim N}a_{n}\,n^{ir}{\varphi}_{\mathfrak{c}\mathfrak{a}n}(\tfrac{1}{2}+ir)\bigg|^{2}\widehat{{\varphi}}(r)\differential{r} |  |

(9.3) |  |  | + 1 2 ​ π ∑ even ​ k φ ~ ( k − 1) ∑ 1 ⩽ j ⩽ θ k ​ ( q) i k ​ ( k − 1)! ( 4 ​ π) k − 1 | ∑ n ∼ N a n n 1 − k 2 ψ j ​ k ( 𝔞, n) | 2 ≪ ( 1 + μ ( 𝔞) N 1 + ϵ) ∥ 𝐚 N ∥ 2 2. \displaystyle\quad+\frac{1}{2\pi}\sum_{{\rm even}\,k}\widetilde{{\varphi}}(k-1)\sum_{1{\,\leqslant}j{\,\leqslant}\theta_{k}(q)}\frac{i^{k}(k-1)!}{(4\pi)^{k-1}}\,\bigg|\sum_{n\sim N}a_{n}n^{\frac{1-k}{2}}\psi_{jk}(\mathfrak{a},n)\bigg|^{2}\ll\ (1+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}. |  |

Hence combining ( 9.1), ( 9.1) we deduce the exceptional spectra is also bounded by O ⁡ ( 1 + μ ⁡ ( 𝔞) ​ N 1 + ϵ) O(1+\mu(\mathfrak{a})N^{1+\epsilon}). That is,

 | ( 1 + μ ⁡ ( 𝔞) ​ N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2 \displaystyle(1+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2} | ≫ ∑ λ j < 1 / 4 φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 ≫ ∑ λ j < 1 / 4 Y − θ q ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle\gg\sum_{\lambda_{j}<1/4}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\,\rho_{j\mathfrak{a}}(n)\bigg|^{2}\gg\sum_{\lambda_{j}<1/4}Y^{-{\theta}_{q}}\bigg|\sum_{n\sim N}a_{n}\,\rho_{j\mathfrak{a}}(n)\bigg|^{2} |  |

(9.4) |  |  | ≫ 1 1 + ( X ​ Y) θ q ​ ∑ λ j < 1 / 4 X 2 ​ i ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2. \displaystyle\gg\frac{1}{1+(XY)^{{\theta}_{q}}}\sum_{\lambda_{j}<1/4}X^{2i\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}. |  |

noting cosh ⁡ π ​ κ = cos ⁡ ( i ​ π ​ κ) ⩽ 1 \cosh\pi\kappa=\cos(i\pi\kappa){\,\leqslant}1 for 0 < i ​ κ < 1 4 0<i\kappa<\tfrac{1}{4} and, c.f. [9, eq. (8.3)],

(9.5) |  | φ ^ ​ ( κ) ≫ Y − 2 ​ i ​ κ ≫ Y − θ q. \displaystyle\widehat{{\varphi}}(\kappa)\gg Y^{-2i\kappa}\gg Y^{-{\theta}_{q}}. |  |

Recalling Y ≪ μ ⁡ ( 𝔞) ​ N < ϵ Y\ll\mu(\mathfrak{a})N<\epsilon, we conclude

 | ∑ λ j < 1 / 4 X 2 ​ i ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ 𝔞 ​ ( n) | 2 \displaystyle\sum_{\lambda_{j}<1/4}X^{2i\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\rho_{j\mathfrak{a}}(n)\bigg|^{2}\  | ≪ ϵ ( 1 + ( μ ( 𝔞) N X) θ q) ( 1 + μ ( 𝔞) N 1 + ϵ) ∥ 𝐚 N ∥ 2 2 \displaystyle\ll_{\epsilon}\ \big(1+(\mu(\mathfrak{a})NX)^{{\theta}_{q}}\big)(1+\mu(\mathfrak{a})N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ≪ ( 1 + ( μ ⁡ ( 𝔞) ​ N ​ X) θ q) ​ ( 1 + ( μ ⁡ ( 𝔞) ​ N 1 + ϵ) 1 − θ q) ​ ‖ 𝐚 N ‖ 2 2. ∎ \displaystyle\ll\big(1+(\mu(\mathfrak{a})NX)^{{\theta}_{q}}\big)(1+(\mu(\mathfrak{a})N^{1+\epsilon})^{1-{\theta}_{q}})\|{\bf a}_{N}\|_{2}^{2}.\qed |  |

### 9.2. Results on Average

In this section we prove Theorem 9.3. Crucially, the test function φ ⁡ ( x) {\varphi}(x) has smaller support, so the sums over c c of Kloosterman sums S ⁡ ( m, n, q ​ c) S(m,n;qc) will no longer be empty. Let

(9.6) |  | S ⁡ ( Q, Y, N, s) = ∑ Q < q ⩽ 16 ​ Q ∑ λ j < 1 / 4 ( q) Y 2 ​ i ​ κ j ​ | ∑ n ∼ N a n ​ n s ​ ρ j ​ ∞ ​ ( n) | 2. \displaystyle S(Q,Y,N;s)=\sum_{Q<q{\,\leqslant}16Q}\;\sum_{\lambda_{j}<1/4}^{(q)}Y^{2i\kappa_{j}}\bigg|\sum_{n\sim N}a_{n}\,n^{s}\rho_{j\infty}(n)\bigg|^{2}. |  |

###### Lemma 9.2.

(Recurrence for S S) Let Q, N, Y ⩾ 1 Q,N,Y{\,\geqslant}1 and 𝐚 = ( a n) n ⊂ ℂ {\bf a}=(a_{n})_{n}\subset{\mathbb{C}}. Then we have

(9.7) |  | S ( Q, Y, N, 0) ≪ ϵ \displaystyle S(Q,Y,N,0)\ \ll_{\epsilon}\  | ∫ ℝ S ⁡ ( π ​ N ​ Y / Q, Y, N, i ​ t) ​ d t t 4 + 1 + ( Y ​ N) ϵ ​ ( Q + N + N ​ Y / Q) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\int_{{\mathbb{R}}}S(\pi NY/Q,Y,N,it)\frac{\differential{t}}{t^{4}+1}\ +\ (YN)^{\epsilon}(Q+N+NY/Q)\|{\bf a}_{N}\|_{2}^{2}. |  |

###### Proof.

See [9, Lemma 8.1] ∎

###### Theorem 9.3.

Let Q, N, X > 0 Q,N,X>0 and 𝐚 = ( a n) n ⊂ ℂ {\bf a}=(a_{n})_{n}\subset{\mathbb{C}}. Then we have

 | S ⁡ ( Q, X 2, N, 0) \displaystyle S(Q,X^{2},N,0) | = ∑ q ≍ Q ∑ λ j < 1 / 4 ( q) X 4 ​ i ​ κ j ​ | ∑ n ⩽ N a n ​ ρ j ​ ∞ ​ ( n) | 2 \displaystyle=\sum_{q\asymp Q}\sum_{\lambda_{j}<1/4}^{(q)}X^{4i\kappa_{j}}\bigg|\sum_{n{\,\leqslant}N}a_{n}\rho_{j\infty}(n)\bigg|^{2} |  |

 |  | ≪ ϵ ( Q N) ϵ ( Q + N + N X 2 ​ θ + Q ( N X / Q) 2 ​ θ) ∥ 𝐚 N ∥ 2 2. \displaystyle\ll_{\epsilon}\ (QN)^{\epsilon}\,(Q+N+NX^{2{\theta}}+Q(\sqrt{N}X/Q)^{2{\theta}})\|{\bf a}_{N}\|_{2}^{2}. |  |

###### Proof.

If θ = 0 {\theta}=0 there is no exceptional spectrum so S ⁡ ( Q, X 2, N, 0) = 0 S(Q,X^{2},N,0)=0. Else assume θ > 0 {\theta}>0.

First, by the spectral large sieve in Theorem 8.2 with K = 1 4 K=\tfrac{1}{4}, ( μ ⁡ ( ∞) = 1 / q \mu(\infty)=1/q)

 | ∑ λ j < 1 / 4 ( q) 1 cosh ⁡ π ​ κ j ​ | ∑ n ⩽ N ρ j ​ ∞ ​ ( n) | 2 ≪ ( 1 + N 1 + ϵ / q) ​ ‖ 𝐚 N ‖ 2 2, \displaystyle\sum_{\lambda_{j}<1/4}^{(q)}\frac{1}{\cosh\pi\kappa_{j}}\bigg|\sum_{n{\,\leqslant}N}\rho_{j\infty}(n)\bigg|^{2}\ll(1+N^{1+\epsilon}/q)\|{\bf a}_{N}\|_{2}^{2}, |  |

and so summing over q ≍ Q q\asymp Q,

(9.8) |  | S ⁡ ( Q, 1, N, 0) = ∑ q ≍ Q ∑ λ j < 1 / 4 ( q) 1 cosh ⁡ π ​ κ j ​ | ∑ n ⩽ N ρ j ​ ∞ ​ ( n) | 2 ≪ ( Q + N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle S(Q,1,N,0)=\sum_{q\asymp Q}\sum_{\lambda_{j}<1/4}^{(q)}\frac{1}{\cosh\pi\kappa_{j}}\bigg|\sum_{n{\,\leqslant}N}\rho_{j\infty}(n)\bigg|^{2}\ll(Q+N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}. |  |

In particular, when 0 < X ⩽ 1 0<X{\,\leqslant}1 we see S ⁡ ( Q, X 2, N, 0) ⩽ S ⁡ ( Q, 1, N, 0) S(Q,X^{2},N,0){\,\leqslant}S(Q,1,N,0) gives a bound (much stronger than) Theorem 9.3. Thus it suffices to show that, for all Y ⩾ 1 Y{\,\geqslant}1,

(9.9) |  | S ⁡ ( Q, Y, N, 0) ≪ ( Q ​ N) 2 ​ ϵ ​ ( Q + N ​ Y θ + Q ​ ( N ​ Y / Q 2) θ) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle S(Q,Y,N,0)\ll(QN)^{2\epsilon}\,(Q+NY^{{\theta}}+Q(NY/Q^{2})^{{\theta}})\|{\bf a}_{N}\|_{2}^{2}. |  |

We have Y 2 ​ i ​ κ j < Y θ Y^{2i\kappa_{j}}<Y^{\theta} for exceptional λ j < 1 / 4 \lambda_{j}<1/4, so ( 9.8) implies

(9.10) |  | S ⁡ ( Q, Y, N, 0) ⩽ Y θ ​ S ​ ( Q, 1, N, 0) ≪ Y θ ​ ( Q + N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle S(Q,Y,N,0){\,\leqslant}Y^{\theta}S(Q,1,N,0)\ll Y^{{\theta}}(Q+N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}. |  |

If N > Q 1 − ϵ N>Q^{1-\epsilon}, then ( 9.10) implies S ⁡ ( Q, Y, N, 0) ≪ Y θ ​ N 1 + 2 ​ ϵ ​ ‖ 𝐚 N ‖ 2 2 S(Q,Y,N,0)\ll Y^{{\theta}}N^{1+2\epsilon}\|{\bf a}_{N}\|_{2}^{2}, which gives ( 9.9).

Else we assume N ⩽ Q 1 − ϵ N{\,\leqslant}Q^{1-\epsilon}. In this case, we claim that

(9.11) |  | sup ( a n) n ⊂ ℂ S ⁡ ( Q, Y 0, N, 0) ≪ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\sup_{(a_{n})_{n}\subset{\mathbb{C}}}S(Q,Y_{0},N,0)\ll Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2} |  |

for the specific choice

 | Y 0:= min ⁡ ( ( Q 1 − ϵ / N) 1 / θ, Q 2 − ϵ / N). Y_{0}:=\min\big((Q^{1-\epsilon}/N)^{1/{\theta}},\,Q^{2-\epsilon}/N\big). |  |

Assuming ( 9.11), for arbitrary Y ⩾ 1 Y{\,\geqslant}1 we conclude

 | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ⩽ ( 1 + ( Y / Y 0) θ) ​ S ​ ( Q, Y 0, N, 0) \displaystyle{\,\leqslant}\big(1+(Y/Y_{0})^{{\theta}}\big)\,S(Q,Y_{0},N,0) |  |

 |  | ≪ ( 1 + Y θ / min ⁡ ( ( Q 1 − ϵ / N), ( Q 2 − ϵ / N) θ)) ​ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\ll\Big(1+Y^{\theta}/\min\big((Q^{1-\epsilon}/N),\,(Q^{2-\epsilon}/N)^{\theta}\big)\Big)Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ≪ ( 1 + Y θ ​ max ⁡ ( ( N / Q 1 − ϵ), ( N / Q 2 − ϵ) θ)) ​ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\ll\Big(1+Y^{\theta}\max\big((N/Q^{1-\epsilon}),\,(N/Q^{2-\epsilon})^{\theta}\big)\Big)Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ⩽ ( Q ​ N) 2 ​ ϵ ​ ( Q + N ​ Y θ + Q ​ ( N ​ Y / Q 2) θ) ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\ {\,\leqslant}\ (QN)^{2\epsilon}\,\big(Q+NY^{{\theta}}+Q(NY/Q^{2})^{\theta}\big)\|{\bf a}_{N}\|_{2}^{2}. |  |

Hence it suffices to show ( 9.11). We shall prove ( 9.11) for all N ⩽ Q 1 − ϵ N{\,\leqslant}Q^{1-\epsilon}, by induction on Q ⩾ 1 Q{\,\geqslant}1.

To this, if Q ⩽ Q 0 ​ ( ϵ) Q{\,\leqslant}Q_{0}(\epsilon) then the bound ( 9.10) implies ( 9.11), since

 | S ⁡ ( Q, Y 0, N, 0) \displaystyle S(Q,Y_{0},N,0) | ≪ Y 0 θ ​ ( Q + N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\ll Y_{0}^{{\theta}}(Q+N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2} |  |

 |  | ≪ ( Q 1 − ϵ / N) ( Q + N 1 + ϵ) ∥ 𝐚 N ∥ 2 2 ≪ ϵ Q 1 + ϵ ∥ 𝐚 N ∥ 2 2. \displaystyle\ll(Q^{1-\epsilon}/N)(Q+N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}\ll_{\epsilon}Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}. |  |

Now if Q > Q 0 ​ ( ϵ) Q>Q_{0}(\epsilon) then we apply Lemma 9.2, giving

 | S ⁡ ( Q, Y 0, N, 0) \displaystyle S(Q,Y_{0},N,0) | ≪ ∫ ℝ S ⁡ ( Q 1, Y 0, N, i ​ t) ​ d t t 4 + 1 + ( N ​ Y 0) ϵ / 3 ​ ( Q + Q 1 + N) ​ ‖ 𝐚 N ‖ 2 2 \displaystyle\ll\int_{{\mathbb{R}}}S(Q_{1},Y_{0},N,it)\frac{\differential{t}}{t^{4}+1}\ +\ (NY_{0})^{\epsilon/3}(Q+Q_{1}+N)\|{\bf a}_{N}\|_{2}^{2} |  |

(9.12) |  |  | ≪ sup t ∈ ℝ S ⁡ ( Q 1, Y 0, N, i ​ t) + Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2, \displaystyle\ll\sup_{t\in{\mathbb{R}}}S(Q_{1},Y_{0},N,it)+Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}, |  |

where Q 1:= π ​ N ​ Y 0 / Q Q_{1}:=\pi NY_{0}/Q. Note Q 1 ≪ N ⁡ ( Q 2 − ϵ / N) / Q ≪ Q 1 − ϵ Q_{1}\ll N(Q^{2-\epsilon}/N)/Q\ll Q^{1-\epsilon}. In particular Q 1 < Q − 1 Q_{1}<Q-1 provided the constant Q 0 ​ ( ϵ) Q_{0}(\epsilon) is sufficiently large. Next, if N > Q 1 1 − ϵ N>Q_{1}^{1-\epsilon} we obtain ( 9.11), since by ( 9.10) and Y 0 θ ⩽ Q 1 − ϵ / N Y_{0}^{\theta}{\,\leqslant}Q^{1-\epsilon}/N,

 | S ⁡ ( Q 1, Y 0, N, 0) \displaystyle S(Q_{1},Y_{0},N,0) | ≪ Y 0 θ ​ ( Q 1 + N 1 + ϵ) ​ ‖ 𝐚 N ‖ 2 2 ≪ ( Q 1 − ϵ / N) ​ N 1 + 2 ​ ϵ ​ ‖ 𝐚 N ‖ 2 2 ≪ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\ll Y_{0}^{{\theta}}(Q_{1}+N^{1+\epsilon})\|{\bf a}_{N}\|_{2}^{2}\ll(Q^{1-\epsilon}/N)N^{1+2\epsilon}\|{\bf a}_{N}\|_{2}^{2}\ll Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}. |  |

Plugging back into ( 9.2) gives S ⁡ ( Q, Y, N, 0) ≪ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2 S(Q,Y,N,0)\ll Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}. Thus it remains to assume N ⩽ Q 1 1 − ϵ N{\,\leqslant}Q_{1}^{1-\epsilon}. Let Y 1:= min ⁡ ( ( Q 1 1 − ϵ / N) 1 / θ, Q 1 2 − ϵ / N) Y_{1}:=\min\big((Q_{1}^{1-\epsilon}/N)^{1/{\theta}},\,Q_{1}^{2-\epsilon}/N\big).

If Y 1 = ( Q 1 1 − ϵ / N) 1 / θ Y_{1}=(Q_{1}^{1-\epsilon}/N)^{1/{\theta}} then ( Y 0 / Y 1) θ ⩽ ( Q / Q 1) 1 − ϵ (Y_{0}/Y_{1})^{\theta}{\,\leqslant}(Q/Q_{1})^{1-\epsilon}. Also if Y 0 = Q 1 2 − ϵ / N Y_{0}=Q_{1}^{2-\epsilon}/N, then

 | ( Y 0 / Y 1) θ ⩽ ( Q / Q 1) ( 2 − ϵ) ​ θ < ( Q / Q 1) 1 − ϵ / 2, \displaystyle(Y_{0}/Y_{1})^{\theta}{\,\leqslant}(Q/Q_{1})^{(2-\epsilon){\theta}}<(Q/Q_{1})^{1-\epsilon/2}, |  |

since θ ⩽ 1 / 2 {\theta}{\,\leqslant}1/2. Thus since Q 1 < Q − 1 Q_{1}<Q-1 and N ⩽ Q 1 1 − ϵ N{\,\leqslant}Q_{1}^{1-\epsilon}, by the induction hypothesis (now with coefficients a n ​ n i ​ t a_{n}\,n^{it}),

 | S ⁡ ( Q 1, Y 0, N, i ​ t) \displaystyle S(Q_{1},Y_{0},N,it) | ⩽ ( Y 0 / Y 1) θ ​ S ​ ( Q 1, Y 1, N, i ​ t) \displaystyle{\,\leqslant}(Y_{0}/Y_{1})^{\theta}\,S(Q_{1},Y_{1},N,it) |  |

 |  | ≪ ϵ ( Q / Q 1) 1 − ϵ / 2 Q 1 1 + ϵ ∥ 𝐚 N ∥ 2 2 = Q 1 − ϵ / 2 Q 1 3 ​ ϵ / 2 ∥ 𝐚 N ∥ 2 2 \displaystyle\ll_{\epsilon}(Q/Q_{1})^{1-\epsilon/2}\,Q_{1}^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}=Q^{1-\epsilon/2}Q_{1}^{3\epsilon/2}\|{\bf a}_{N}\|_{2}^{2} |  |

(9.13) |  |  | ≪ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2. \displaystyle\ \ll\ Q^{1+\epsilon}\,\|{\bf a}_{N}\|_{2}^{2}. |  |

Hence plugging ( 9.2) back into ( 9.2) gives S ⁡ ( Q, Y, N, 0) ≪ Q 1 + ϵ ​ ‖ 𝐚 N ‖ 2 2 S(Q,Y,N,0)\ll Q^{1+\epsilon}\|{\bf a}_{N}\|_{2}^{2}. This completes the proof of ( 9.11), and hence Theorem 9.3. ∎

We use the following auxiliary estimate for Kloosterman sums.

###### Theorem 9.4.

For C, M, N ⩾ 1 C,M,N{\,\geqslant}1, we have

(9.14) |  | ∑ c ⩽ C | ∑ m ⩽ M ∑ n ⩽ N S ⁡ ( m, n, c) | ≪ ( C ​ M ​ N) ϵ ​ ( C 2 + C ​ M ​ N). \displaystyle\sum_{c{\,\leqslant}C}\bigg|\sum_{m{\,\leqslant}M}\sum_{n{\,\leqslant}N}S(m,n;c)\bigg|\ \ll\ (CMN)^{\epsilon}(C^{2}+CMN). |  |

###### Proof.

This is [9, Theorem 14]. ∎

Now, using Theorem 9.4, we improve upon Theorem 9.3 for the special sequence a n = 1 a_{n}=1.

###### Theorem 9.5.

Let Q, X ⩾ 1 Q,X{\,\geqslant}1 and 1 ⩽ N < N 1 ⩽ 2 ​ N 1{\,\leqslant}N<N_{1}{\,\leqslant}2N. Then we have

(9.15) |  | ∑ q ≍ Q ∑ λ j < 1 / 4 ( q) X 4 ​ i ​ κ j | ∑ N < n ⩽ N 1 ρ j ​ ∞ ( n) | 2 ≪ ϵ ( Q N) ϵ ( 1 + ( N ​ X 2 ( Q + N) 2) θ) ( Q + N) N. \displaystyle\sum_{q\asymp Q}\sum_{\lambda_{j}<1/4}^{(q)}X^{4i\kappa_{j}}\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2}\ \ll_{\epsilon}\ (QN)^{\epsilon}\,\Big(1+\Big(\frac{NX^{2}}{(Q+N)^{2}}\Big)^{\theta}\Big)(Q+N)N. |  |

###### Proof.

Define the sequence a n = 𝟏 [N, N 1] ​ ( n) a_{n}=\mathbf{1}_{[N,N_{1}]}(n). It suffices to show that for Y ⩾ 1 Y{\,\geqslant}1,

(9.16) |  | S ⁡ ( Q, Y, N, 0):= ∑ q ≍ Q ∑ λ j < 1 / 4 ( q) Y 2 ​ i ​ κ j ​ | ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) | 2 ≪ ( Q ​ N) 5 ​ ϵ ​ ( 1 + ( N ​ Y ( Q + N) 2) θ) ​ ( Q + N) ​ N. \displaystyle S(Q,Y,N,0):=\sum_{q\asymp Q}\sum_{\lambda_{j}<1/4}^{(q)}Y^{2i\kappa_{j}}\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2}\ll(QN)^{5\epsilon}\Big(1+\Big(\frac{NY}{(Q+N)^{2}}\Big)^{\theta}\Big)(Q+N)N. |  |

Indeed, by the Kuznetsov formula for the cusps 𝔞 = 𝔟 = ∞ \mathfrak{a}=\mathfrak{b}=\infty of the group Γ 0 ​ ( q) \Gamma_{0}(q), summing over m, n ∼ N m,n\sim N gives

(9.17) |  | ∑ λ j < 1 4 ( q) φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N ρ j ​ ∞ ​ ( n) | 2 \displaystyle\sum_{\lambda_{j}<\tfrac{1}{4}}^{(q)}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}\rho_{j\infty}(n)\bigg|^{2} | = ∑ m, n ∼ N ∑ c ∈ ℤ + 1 q ​ c ​ φ ​ ( 4 ​ π q ​ c ​ m ​ n) ​ S ​ ( m, n, q ​ c) \displaystyle=\sum_{m,n\sim N}\sum_{c\in{\mathbb{Z}}^{+}}\frac{1}{qc}\,{\varphi}\Big(\frac{4\pi}{qc}\sqrt{mn}\Big)\,S(m,n;qc) |  |

 |  | + O ⁡ ( ( 1 + N 1 + ϵ / q) ​ N), \displaystyle\quad+O\big((1+N^{1+\epsilon}/q)N\big), |  |

bounding the regular spectra as in ( 9.1), by the spectral large sieve in Theorem 8.2.

Since cosh ⁡ π ​ κ ⩽ 1 \cosh\pi\kappa{\,\leqslant}1 and φ ^ ​ ( κ) ≫ Y 2 ​ i ​ κ \widehat{{\varphi}}(\kappa)\gg Y^{2i\kappa} by ( 9.5), we see ( 9.17) gives

(9.18) |  | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ≪ ∑ q ≍ Q ∑ λ j < 1 / 4 ( q) φ ^ ​ ( κ j) cosh ⁡ π ​ κ j ​ | ∑ n ∼ N ρ j ​ ∞ ​ ( n) | 2 ≪ 𝒯 + ( Q + N 1 + ϵ) ​ N, \displaystyle\ll\sum_{q\asymp Q}\sum_{\lambda_{j}<1/4}^{(q)}\frac{\widehat{{\varphi}}(\kappa_{j})}{\cosh\pi\kappa_{j}}\bigg|\sum_{n\sim N}\rho_{j\infty}(n)\bigg|^{2}\ \ll\ \mathcal{T}+(Q+N^{1+\epsilon})N, |  |

where

 | 𝒯:= ∑ Q < q ⩽ 16 ​ Q ∑ c ∈ ℤ + 1 q ​ c ​ | ∑ m, n ∼ N φ ⁡ ( 4 ​ π q ​ c ​ m ​ n) ​ S ​ ( m, n, q ​ c) |. \displaystyle\mathcal{T}:=\sum_{Q<q{\,\leqslant}16Q}\sum_{c\in{\mathbb{Z}}^{+}}\frac{1}{qc}\bigg|\sum_{m,n\sim N}{\varphi}\Big(\frac{4\pi}{qc}\sqrt{mn}\Big)\,S(m,n;qc)\bigg|. |  |

Since supp ( φ) ⊂ [1 / 2 ​ Y, 5 / 2 ​ Y] ({\varphi})\subset[1/2Y,5/2Y], we note c c runs over the interval [C / 40, 16 ​ C] [C/40,16C] with C = π ​ N ​ Y / Q C=\pi NY/Q.

Next, by Mellin inversion φ ⁡ ( x) = 1 2 ​ π ​ ∫ ℝ φ ˘ ​ ( i ​ t) ​ x − i ​ t ​ d t {\varphi}(x)=\frac{1}{2\pi}\int_{{\mathbb{R}}}\breve{{\varphi}}(it)x^{-it}\differential{t} for the Mellin transform φ ˘ ​ ( i ​ t) = ∫ ℝ + φ ⁡ ( y) ​ y i ​ t − 1 ​ d y \breve{{\varphi}}(it)=\int_{{\mathbb{R}}^{+}}{\varphi}(y)y^{it-1}\differential{y}, which is bounded by φ ˘ ​ ( i ​ t) ≪ ( 1 + t 4) − 1 \breve{{\varphi}}(it)\ll(1+t^{4})^{-1}.

 | 𝒯 \displaystyle\mathcal{T} | ≪ ∫ ℝ ∑ q ≍ Q ∑ c ≍ C 1 q ​ c ​ | ∑ N ⩽ m, n ⩽ N 1 ( 4 ​ π ​ m ​ n / q ​ c) − i ​ t ​ S ​ ( m, n, q ​ c) | ​ d t 1 + t 4 \displaystyle\ll\int_{{\mathbb{R}}}\sum_{q\asymp Q}\sum_{c\asymp C}\frac{1}{qc}\bigg|\sum_{N{\,\leqslant}m,n{\,\leqslant}N_{1}}(4\pi\sqrt{mn}/qc)^{-it}S(m,n;qc)\bigg|\frac{\differential{t}}{1+t^{4}} |  |

 |  | ≪ ( Q ​ C) ϵ − 1 ​ ∫ ℝ ∑ k ≍ Q ​ C | ∑ N ⩽ m, n ⩽ N 1 ( m ​ n) − i ​ t ​ S ​ ( m, n, k) | ​ d t 1 + t 4. \displaystyle\ll(QC)^{\epsilon-1}\int_{{\mathbb{R}}}\sum_{k\asymp QC}\bigg|\sum_{N{\,\leqslant}m,n{\,\leqslant}N_{1}}(mn)^{-it}S(m,n;k)\bigg|\frac{\differential{t}}{1+t^{4}}. |  |

merging k = q ​ c k=qc as a single variable, and using the divisor bound τ ⁡ ( k) ≪ k ϵ \tau(k)\ll k^{\epsilon}.

Using m − i ​ t = N 1 + i ​ t ​ ∫ m N 1 u − i ​ t − 1 ​ d u m^{-it}=N_{1}+it\int_{m}^{N_{1}}u^{-it-1}\differential{u}, we obtain by Theorem 9.4,

 | 𝒯 \displaystyle\mathcal{T} | ≪ ( Q ​ C) ϵ − 1 ​ sup N ⩽ M ′, N ′ ⩽ N 1 ∑ k ≍ Q ​ C | ∑ m ⩽ M ′ n ⩽ N ′ S ⁡ ( m, n, k) | \displaystyle\ll(QC)^{\epsilon-1}\sup_{N{\,\leqslant}M^{\prime},N^{\prime}{\,\leqslant}N_{1}}\sum_{k\asymp QC}\bigg|\sum_{\begin{subarray}{c}m{\,\leqslant}M^{\prime}\\ n{\,\leqslant}N^{\prime}\end{subarray}}S(m,n;k)\bigg| |  |

 |  | ≪ ( Q ​ C) ϵ − 1 ​ sup N ⩽ M ′, N ′ ⩽ N 1 Q ​ C ​ ( Q ​ C + M ′ ​ N ′) ≪ ( Q ​ C ​ N) ϵ ​ ( Q ​ C + N 2). \displaystyle\ll(QC)^{\epsilon-1}\sup_{N{\,\leqslant}M^{\prime},N^{\prime}{\,\leqslant}N_{1}}QC(QC+M^{\prime}N^{\prime})\ \ll\ (QCN)^{\epsilon}\,(QC+N^{2}). |  |

Plugging back into ( 9.18) gives

 | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ≪ 𝒯 + ( Q + N 1 + ϵ) ​ N \displaystyle\ll\mathcal{T}+(Q+N^{1+\epsilon})N |  |

(9.19) |  |  | ≪ ( Q ​ C ​ N) ϵ ​ ( Q ​ C + N 2) + ( Q + N 1 + ϵ) ​ N ≪ ( N ​ Y) ϵ ​ ( Q + N + Y) ​ N, \displaystyle\ll(QCN)^{\epsilon}\,(QC+N^{2})+(Q+N^{1+\epsilon})N\ll(NY)^{\epsilon}(Q+N+Y)N, |  |

recalling Q ​ C = π ​ N ​ Y QC=\pi NY. When Y ⩾ Q + N Y{\,\geqslant}Q+N, this bound is self-improving in the Y Y -aspect by the following trick: indeed, by ( 9.2) with Y 1 = Q + N Y_{1}=Q+N,

 | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ≪ ( 1 + ( Y / Y 1) θ) ​ S ​ ( Q, Y 1, N, 0) \displaystyle\ll\big(1+(Y/Y_{1})^{{\theta}}\big)S(Q,Y_{1},N,0) |  |

 |  | ≪ ( 1 + ( Y / Y 1) θ) ​ ( N ​ Y 1) ϵ ​ ( Q + N + Y 1) ​ N \displaystyle\ll\big(1+(Y/Y_{1})^{{\theta}}\big)(NY_{1})^{\epsilon}(Q+N+Y_{1})N |  |

(9.20) |  |  | ≪ ( Q ​ N) ϵ ​ ( Q + N + Y θ ​ ( Q + N) 1 − θ) ​ N. \displaystyle\ll(QN)^{\epsilon}(Q+N+Y^{\theta}(Q+N)^{1-{\theta}})N. |  |

In particular, if N > Q 1 − 2 ​ ϵ N>Q^{1-2\epsilon} then

 | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ≪ N ϵ ​ ( N + Y θ ​ N 1 − θ) ​ N ≪ N 2 + ϵ ​ ( 1 + ( N ​ Y ( Q + N) 2) θ) \displaystyle\ll N^{\epsilon}(N+Y^{\theta}\,N^{1-{\theta}})N\ll N^{2+\epsilon}\Big(1+\Big(\frac{NY}{(Q+N)^{2}}\Big)^{\theta}\Big) |  |

as desired for ( 9.16).

It remains to consider N ⩽ Q 1 − 2 ​ ϵ N{\,\leqslant}Q^{1-2\epsilon}. We shall eliminate the Y θ ​ Q 1 − θ Y^{\theta}Q^{1-{\theta}} term in ( 9.2) to complete the proof for all N N. To this, we prove that for all 1 ⩽ N ⩽ Q 1{\,\leqslant}N{\,\leqslant}Q with Y = Q 2 − 2 ​ ϵ / N Y=Q^{2-2\epsilon}/N,

(9.21) |  | sup N 1 ⩽ 2 ​ N a n = 𝟏 [N, N 1] ​ ( n) S ⁡ ( Q, Y, N, 0) ≪ Q 1 + 4 ​ ϵ ​ N. \displaystyle\sup_{\begin{subarray}{c}N_{1}{\,\leqslant}2N\\ a_{n}=\mathbf{1}_{[N,N_{1}](n)}\end{subarray}}S(Q,Y,N,0)\ll Q^{1+4\epsilon}N. |  |

Assuming this, for arbitrary Y ⩾ 1 Y{\,\geqslant}1 we conclude

 | S ⁡ ( Q, Y, N, 0) \displaystyle S(Q,Y,N,0) | ⩽ ( 1 + ( Y / Y 0) θ) ​ S ​ ( Q, Y 0, N, 0) \displaystyle{\,\leqslant}\big(1+(Y/Y_{0})^{\theta}\big)S(Q,Y_{0},N,0) |  |

 |  | ⩽ ( 1 + ( Y / Y 0) θ) ​ Q 1 + 4 ​ ϵ ​ N \displaystyle{\,\leqslant}\big(1+(Y/Y_{0})^{\theta}\big)Q^{1+4\epsilon}N |  |

 |  | ≪ Q 1 + 5 ​ ϵ ​ N ​ ( 1 + ( N ​ Y / Q 2) θ) ≪ Q 1 + 5 ​ ϵ ​ N ​ ( 1 + ( N ​ Y ( Q + N) 2) θ) \displaystyle\ll Q^{1+5\epsilon}N\big(1+(NY/Q^{2})^{\theta}\big)\ \ll\ Q^{1+5\epsilon}N\Big(1+\Big(\frac{NY}{(Q+N)^{2}}\Big)^{\theta}\Big) |  |

as desired for ( 9.16), where Y 0 = Q 2 − 2 ​ ϵ / N Y_{0}=Q^{2-2\epsilon}/N. Hence it suffices to show ( 9.21).

We shall prove ( 9.21) by induction on Q ⩾ 1 Q{\,\geqslant}1. If Q ⩽ Q 0 ​ ( ϵ) Q{\,\leqslant}Q_{0}(\epsilon) the above follows by the spectral large sieve. Namely, by ( 9.10) with a n = 1 a_{n}=1 (so ‖ a N ‖ 2 2 = ∑ n ∼ N 1 = N \|a_{N}\|_{2}^{2}=\sum_{n\sim N}1=N),

 | S ⁡ ( Q, Y 0, N, 0) \displaystyle S(Q,Y_{0},N,0) | ⩽ Y ​ S ​ ( Q, 1, N, 0) ≪ Y 0 ​ ( Q + N 1 + ϵ) ​ ‖ a N ‖ 2 2 \displaystyle{\,\leqslant}\sqrt{Y}S(Q,1,N,0)\ll\sqrt{Y_{0}}(Q+N^{1+\epsilon})\|a_{N}\|_{2}^{2} |  |

 |  | ≪ Q 1 − ϵ N ​ ( Q + N 1 + ϵ) ​ N ≪ Q 0 ​ Q 1 + 4 ​ ϵ ​ N. \displaystyle\ll\frac{Q^{1-\epsilon}}{\sqrt{N}}(Q+N^{1+\epsilon})N\ll Q_{0}\,Q^{1+4\epsilon}N. |  |

Also if Q 1 − 2 ​ ϵ < N ⩽ Q Q^{1-2\epsilon}<N{\,\leqslant}Q, then N < Q 1 + 4 ​ ϵ N<Q^{1+4\epsilon}, so ( 9.2) with Y 0 = Q 2 − 2 ​ ϵ / N < Q Y_{0}=Q^{2-2\epsilon}/N<Q gives

 | S ⁡ ( Q, Y 0, N, 0) ≪ ( Q ​ N) ϵ ​ ( Q + N + N ​ Y 0 + Q ​ Y) ​ N ≪ Q 1 + 4 ​ ϵ ​ N. \displaystyle S(Q,Y_{0},N,0)\ll(QN)^{\epsilon}(Q+N+\sqrt{NY_{0}}+\sqrt{QY})N\ll Q^{1+4\epsilon}N. |  |

Now consider Q > Q 0 ​ ( ϵ) Q>Q_{0}(\epsilon) and 1 ⩽ N ⩽ Q 1 − 2 ​ ϵ 1{\,\leqslant}N{\,\leqslant}Q^{1-2\epsilon}. By Lemma 9.2 with a n = 1 a_{n}=1 (so ‖ a N ‖ 2 2 = N \|a_{N}\|_{2}^{2}=N),

(9.22) |  | S ⁡ ( Q, Y 0, N, 0) ≪ ∫ ℝ S ⁡ ( Q 1, Y 0, N, i ​ t) ​ d t t 4 + 1 + Q 1 + 3 ​ ϵ ​ N \displaystyle S(Q,Y_{0},N,0)\ll\int_{{\mathbb{R}}}S(Q_{1},Y_{0},N,it)\,\frac{\differential{t}}{t^{4}+1}+Q^{1+3\epsilon}N |  |

where Q 1 = π ​ N ​ Y / Q = π ​ Q 1 − 2 ​ ϵ < Q − 1 Q_{1}=\pi NY/Q=\pi Q^{1-2\epsilon}<Q-1, provided the constant Q 0 ​ ( ϵ) Q_{0}(\epsilon) is sufficiently large. Moreover, writing Y 1 = Q 1 2 − 2 ​ ϵ / N Y_{1}=Q_{1}^{2-2\epsilon}/N we have Y 0 / Y 1 = ( Q / Q 1) 1 − ϵ ≪ Q 2 ​ ϵ ​ ( 1 − ϵ) \sqrt{Y_{0}/Y_{1}}=(Q/Q_{1})^{1-\epsilon}\ll Q^{2\epsilon(1-\epsilon)}, and so

 | S ⁡ ( Q 1, Y 0, N, i ​ t) \displaystyle S(Q_{1},Y_{0},N,it) | ⩽ Y 0 / Y 1 ​ S ​ ( Q 1, Y 1, N, i ​ t) \displaystyle{\,\leqslant}\sqrt{Y_{0}/Y_{1}}\,S(Q_{1},Y_{1},N,it) |  |

(9.23) |  |  | ⩽ Q 2 ​ ϵ ​ ( 1 − ϵ) ​ S ​ ( Q 1, Y 1, N, i ​ t). \displaystyle{\,\leqslant}Q^{2\epsilon(1-\epsilon)}\,S(Q_{1},Y_{1},N,it). |  |

We now wish to apply the induction hypothesis (with a n = 1 a_{n}=1), but this is not possible immediately, due to the coefficients a n = n i ​ t a_{n}=n^{it} in S ⁡ ( Q 1, Y 1, N, i ​ t) S(Q_{1},Y_{1},N,it).

To remedy this, by partial summation

 | ∑ N < n ⩽ N 1 n i ​ t ​ ρ j ​ ∞ ​ ( n) = N 1 i ​ t ​ ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) − i ​ t ​ ∫ N N 1 ∑ N < n ⩽ u ρ j ​ ∞ ​ ( n) ​ u i ​ t − 1 ​ d u \displaystyle\sum_{N<n{\,\leqslant}N_{1}}n^{it}\,\rho_{j\infty}(n)=N_{1}^{it}\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)-it\int_{N}^{N_{1}}\sum_{N<n{\,\leqslant}u}\rho_{j\infty}(n)\,u^{it-1}\differential{u} |  |

and so Cauchy-Schwarz gives

 | | ∑ N < n ⩽ N 1 n i ​ t ​ ρ j ​ ∞ ​ ( n) | 2 \displaystyle\bigg|\sum_{N<n{\,\leqslant}N_{1}}n^{it}\rho_{j\infty}(n)\bigg|^{2} | ≪ | ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) | 2 + t 2 ​ | ∫ N N 1 ∑ N < n ⩽ u ρ j ​ ∞ ​ ( n) ​ u i ​ t − 1 ​ d u | 2 \displaystyle\ll\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2}+t^{2}\bigg|\int_{N}^{N_{1}}\sum_{N<n{\,\leqslant}u}\rho_{j\infty}(n)\,u^{it-1}\differential{u}\bigg|^{2} |  |

 |  | ≪ | ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) | 2 + t 2 ​ ∫ N N 1 | ∑ N < n ⩽ u ρ j ​ ∞ ​ ( n) | 2 ​ d u ⋅ ∫ N N 1 d u u 2 \displaystyle\ll\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2}+t^{2}\int_{N}^{N_{1}}\bigg|\sum_{N<n{\,\leqslant}u}\rho_{j\infty}(n)\bigg|^{2}\differential{u}\cdot\int_{N}^{N_{1}}\frac{\differential{u}}{u^{2}} |  |

 |  | ≪ ( 1 + t 2) ​ sup N 1 ⩽ 2 ​ N | ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) | 2. \displaystyle\ll(1+t^{2})\sup_{N_{1}{\,\leqslant}2N}\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2}. |  |

Thus we have

 | S ⁡ ( Q 1, Y 1, N, i ​ t) \displaystyle S(Q_{1},Y_{1},N,it) | : = ∑ q ∼ Q 1 ∑ λ j < 1 / 4 ( q) Y 1 2 ​ i ​ κ j ​ | ∑ N < n ⩽ N 1 n i ​ t ​ ρ j ​ ∞ ​ ( n) | 2 \displaystyle:=\sum_{q\sim Q_{1}}\sum_{\lambda_{j}<1/4}^{(q)}Y_{1}^{2i\kappa_{j}}\bigg|\sum_{N<n{\,\leqslant}N_{1}}n^{it}\rho_{j\infty}(n)\bigg|^{2} |  |

 |  | ≪ ( 1 + t 2) ​ sup N 1 ⩽ 2 ​ N ∑ q ∼ Q 1 ∑ λ j < 1 / 4 ( q) Y 1 2 ​ i ​ κ j ​ | ∑ N < n ⩽ N 1 ρ j ​ ∞ ​ ( n) | 2 \displaystyle\ll(1+t^{2})\sup_{N_{1}{\,\leqslant}2N}\sum_{q\sim Q_{1}}\sum_{\lambda_{j}<1/4}^{(q)}Y_{1}^{2i\kappa_{j}}\bigg|\sum_{N<n{\,\leqslant}N_{1}}\rho_{j\infty}(n)\bigg|^{2} |  |

 |  | = ( 1 + t 2) ​ sup N 1 ⩽ 2 ​ N a n = 𝟏 [N, N 1] ​ ( n) S ⁡ ( Q 1, Y 1, N, 0) \displaystyle=(1+t^{2})\sup_{\begin{subarray}{c}N_{1}{\,\leqslant}2N\\ a_{n}=\mathbf{1}_{[N,N_{1}]}(n)\end{subarray}}S(Q_{1},Y_{1},N,0) |  |

 |  | ≪ ( 1 + t 2) ​ Q 1 1 + 4 ​ ϵ ​ N. \displaystyle\ll(1+t^{2})Q_{1}^{1+4\epsilon}N. |  |

by the induction hypothesis. Hence ( 9.2) becomes

 | S ⁡ ( Q 1, Y 0, N, i ​ t) ≪ Q 2 ​ ϵ ​ ( 1 − ϵ) ​ S ​ ( Q 1, Y 1, N, i ​ t) \displaystyle S(Q_{1},Y_{0},N,it)\ll Q^{2\epsilon(1-\epsilon)}\,S(Q_{1},Y_{1},N,it) | ≪ Q 2 ​ ϵ ​ ( 1 − ϵ) ​ ( 1 + t 2) ​ Q 1 1 + 4 ​ ϵ ​ N \displaystyle\ll Q^{2\epsilon(1-\epsilon)}(1+t^{2})Q_{1}^{1+4\epsilon}N |  |

Plugging back into ( 9.22) we obtain

 | S ⁡ ( Q, Y 0, N, 0) \displaystyle S(Q,Y_{0},N,0) | ≪ ϵ Q 2 ​ ϵ ​ ( 1 − ϵ) Q 1 1 + 4 ​ ϵ N ∫ ℝ t 2 + 1 t 4 + 1 d t + Q 1 + 3 ​ ϵ N \displaystyle\ll_{\epsilon}Q^{2\epsilon(1-\epsilon)}Q_{1}^{1+4\epsilon}N\int_{{\mathbb{R}}}\frac{t^{2}+1}{t^{4}+1}\differential{t}+Q^{1+3\epsilon}N |  |

 |  | ≪ ϵ Q 2 ​ ϵ ​ ( 1 − ϵ) Q 1 1 + 4 ​ ϵ N + Q 1 + 3 ​ ϵ N \displaystyle\ll_{\epsilon}Q^{2\epsilon(1-\epsilon)}Q_{1}^{1+4\epsilon}N+Q^{1+3\epsilon}N |  |

 |  | ≪ ϵ Q 1 + 4 ​ ϵ − 10 ​ ϵ 2 N ≪ Q 1 + 4 ​ ϵ N. \displaystyle\ll_{\epsilon}Q^{1+4\epsilon-10\epsilon^{2}}N\ \ll\ Q^{1+4\epsilon}N. |  |

This completes the proof of ( 9.21), and hence Theorem 9.5. ∎

### 9.3. Factorization of Fourier coefficients

In the proof we assume q 0 = 1 q_{0}=1 and t = 0 t=0 for simplicity, though general results may obtained similarly with q 0 q_{0} -dependence, as in [11, §4.2.3]. Indeed, q 0 = 1 q_{0}=1 is the only case needed for our applications in this article.

We use an approximate factorization of Fourier coefficients by Assing–Blomer–Li [1].

###### Lemma 9.6.

For any r, s ∈ ℕ r,s\in{\mathbb{N}} and any sequence b n = b n, r, s ∈ ℂ b_{n}=b_{n,r,s}\in{\mathbb{C}}, we have

 |  | | ∑ n ∼ N b n ​ ρ j, 1 / s ​ ( a ​ n) | ≪ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′ ​ ρ j, 1 / s ​ ( n) |. \displaystyle\bigg|\sum_{n\sim N}b_{n}\,\rho_{j,\,1/s}(an)\bigg|\ \ll\ \sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}b_{nn^{\prime\prime}}\,\rho_{j,\,1/s}(n)\bigg|. |  |

Corresponding statements hold for holomorphic and Eisenstein contributions.

###### Proof.

This is a slight rephrasing of [1, Lemma 3.2] with q = Q ′′ = K = 1 q=Q^{\prime\prime}=K=1, and follows by the same proof. The basic idea is to expand with respect to an orthonormal basis of newforms, and then apply the approximate factorization of Fourier coefficients, in [1, Lemma 3.1].

This is the only place where the Ramanujan–Petersson exponent θ \theta is needed, generalizing that of Selberg. As noted, [1] use different normalization, with 2 ​ θ 2\theta instead of θ \theta. ∎

## 10. Sums of Kloosterman sums

In this section, we estimate quintilinear sums of Kloosterman sums using the spectral large sieve estimates, and prove Theorem 1.8.

###### Theorem 10.1.

Let C, M, N, R, S > 0 C,M,N,R,S>0 and let g ∈ 𝒞 ∞ ​ ( [C, 2 ​ C] × ( ℝ +) 4) g\in\mathcal{C}^{\infty}\big([C,2C]\times({\mathbb{R}}^{+})^{4}\big) satisfy

(10.1) |  | | ∂ v 1 + v 2 + v 3 + v 4 + v 5 ∂ c v 1 ​ ∂ m v 2 ​ ∂ n v 3 ​ ∂ r v 4 ​ ∂ s v 5 g ( c, m, n, r, s) | ≪ v i c − v 1 m − v 2 n − v 3 r − v 4 s − v 5 \displaystyle\bigg|\frac{\partial^{v_{1}+v_{2}+v_{3}+v_{4}+v_{5}}}{\partial c^{v_{1}}\,\partial m^{v_{2}}\,\partial n^{v_{3}}\,\partial r^{v_{4}}\,\partial s^{v_{5}}}\,g(c,m,n,r,s)\bigg|\ \ll_{v_{i}}\ c^{-v_{1}}m^{-v_{2}}n^{-v_{3}}r^{-v_{4}}s^{-v_{5}} |  |

for any v i ⩾ 0 v_{i}{\,\geqslant}0, i ⩽ 5 i{\,\leqslant}5. For a Dirichlet character χ \chi (mod q 0 q_{0}), t ∈ ℝ t\in{\mathbb{R}}, sequences a m, b n, r, s ⊂ ℂ a_{m},b_{n,r,s}\subset{\mathbb{C}}, define the quintilinear sum ℒ ( a m) ± = ℒ ( a m) ± ​ ( C, M, N, R, S) \mathcal{L}^{\pm}_{(a_{m})}=\mathcal{L}^{\pm}_{(a_{m})}(C,M,N,R,S) by

(10.2) |  | ℒ ( a m) ± = ∑ r ∼ R s ∼ S ( q 0 ​ r, s) = 1 ∑ m ∼ M n ∼ N a m ​ b n, r, s ​ χ ¯ ​ ( c) ​ ∑ ( c, q 0 ​ s) = 1 g ⁡ ( c, m, n, r, s) ​ e ​ ( m ​ t) ​ S ​ ( m ​ r ¯, ± a ​ n, s ​ c). \displaystyle\mathcal{L}^{\pm}_{(a_{m})}=\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (q_{0}r,s)=1\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ n\sim N\end{subarray}}a_{m}\,b_{n,r,s}\,\overline{\chi}(c)\sum_{(c,q_{0}s)=1}g(c,m,n,r,s)\,e(mt)\,S(m\overline{r},\pm an;sc). |  |

Then we have

(10.3) |  | ℒ ( a m) ≪ ϵ ( q 0 C M N R S) ϵ L ∥ 𝐚 ∥ 2 \displaystyle\mathcal{L}_{(a_{m})}\ \ll_{\epsilon}\ (q_{0}CMNRS)^{\epsilon}\,L\,\|{\bf a}\|_{2} |  |

where L = L ⁡ ( C, M, N, R, S) L=L(C,M,N,R,S) is given by

 | L 2 = C 4 ​ S 3 ​ q 0 ​ R a ​ M ​ N + C 2 ​ S 2 ​ q 0 ​ R \displaystyle L^{2}=\frac{C^{4}S^{3}q_{0}R}{aMN+C^{2}S^{2}q_{0}R} | ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ( q 0 ​ N n ′′ + R ​ S + a ​ M ​ N q 0 ​ C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N q 0 ​ C 2 ​ S) ​ ‖ 𝐛 ~ ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\Bigg(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\Big(\frac{q_{0}N}{n^{\prime\prime}}+RS+\frac{aMN}{q_{0}C^{2}S}\Big)\Big(M+RS+\frac{aMN}{q_{0}C^{2}S}\Big)\|\widetilde{\bf b}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | OPEN + ( C ​ S ​ q 0 ​ R) 2 ​ θ ​ ( q 0 ​ N + R ​ S) 1 − θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ) ​ ‖ 𝐛 ‖ 2 2). \displaystyle\qquad\ +\ (CS\sqrt{q_{0}R})^{2{\theta}}(q_{0}N+RS)^{1-{\theta}}\big(M^{1-{\theta}}+(RS)^{1-2{\theta}}\big)\|{\bf b}\|_{2}^{2}\Bigg). |  |

The bound for ℒ ( a m) \mathcal{L}_{(a_{m})} is refined when a m a_{m} is the characteristic sequence of an interval.

###### Theorem 10.2.

Let C, M, N, R, S > 1 C,M,N,R,S>1 and let g ∈ 𝒞 ∞ ​ ( [C, 2 ​ C] × ( ℝ +) 4) g\in\mathcal{C}^{\infty}\big([C,2C]\times({\mathbb{R}}^{+})^{4}\big) satisfy ( 10.1). For a Dirichlet character χ \chi (mod q 0 q_{0}), t ∈ ℝ t\in{\mathbb{R}}, any sequence b n, r, s ⊂ ℂ b_{n,r,s}\subset{\mathbb{C}}, we have

(10.4) |  | ℒ ( 𝟏 m ∼ M) ≪ ϵ ( q 0 C M N R S) ϵ L 1 M \displaystyle\mathcal{L}_{(\mathbf{1}_{m\sim M})}\ \ll_{\epsilon}\ (q_{0}CMNRS)^{\epsilon}\,L_{1}\,\sqrt{M} |  |

for ℒ ( a m) \mathcal{L}_{(a_{m})} in ( 10.2) with the sequence a m = 𝟏 m ∼ M a_{m}=\mathbf{1}_{m\sim M}, and where L 1 = L 1 ​ ( C, M, N, R, S) L_{1}=L_{1}(C,M,N,R,S) is

 | L 1 2 = C 4 ​ S 3 ​ q 0 ​ R a ​ M ​ N + C 2 ​ S 2 ​ q 0 ​ R \displaystyle L_{1}^{2}=\frac{C^{4}S^{3}q_{0}R}{aMN+C^{2}S^{2}q_{0}R} | ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ( q 0 ​ N n ′′ + R ​ S + a ​ M ​ N q 0 ​ C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N q 0 ​ C 2 ​ S) ​ ‖ 𝐛 ~ ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\bigg(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\Big(\frac{q_{0}N}{n^{\prime\prime}}+RS+\frac{aMN}{q_{0}C^{2}S}\Big)\Big(M+RS+\frac{aMN}{q_{0}C^{2}S}\Big)\|\widetilde{\bf b}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | OPEN + ( C ​ S ​ q 0 ​ R) 2 ​ θ ​ ( q 0 ​ N + R ​ S) 1 − θ ​ ( M + R ​ S) 1 − 2 ​ θ ​ ‖ 𝐛 ‖ 2 2). \displaystyle\qquad+\,(CS\sqrt{q_{0}R})^{2{\theta}}(q_{0}N+RS)^{1-{\theta}}(M+RS)^{1-2{\theta}}\|{\bf b}\|_{2}^{2}\Bigg). |  |

Note L L differs from L 1 L_{1} only in the term M 1 − θ M^{1-{\theta}}, compared to M 1 − 2 ​ θ M^{1-2{\theta}}, in the final factor for the exceptional spectrum.

For simplicity of exposition, we assume q 0 = 1 q_{0}=1 and t = 0 t=0. Indeed, q 0 = 1 q_{0}=1, t = 0 t=0 is the only case needed for our applications in this article. Results may obtained with general q 0 q_{0} -dependence, as in [11, §4.2.3].

As usual we restrict ourselves to weights g g of the form

 | g ⁡ ( c, m, n, r, s) = C ​ S ​ R c ​ s ​ r ​ f ​ ( 4 ​ π ​ a ​ m ​ n c ​ s ​ r) \displaystyle g(c,m,n,r,s)=\frac{CS\sqrt{R}}{cs\sqrt{r}}\,f\Big(\frac{4\pi\sqrt{amn}}{cs\sqrt{r}}\Big) |  |

where f ∈ 𝒞 ∞ ​ ( [1 / X, 2 / X]) f\in\mathcal{C}^{\infty}([1/X,2/X]) for X = C ​ S ​ R / 4 ​ π ​ a ​ M ​ N X=CS\sqrt{R}/4\pi\sqrt{aMN}, and whose derivatives satisfy | f ( l) ​ ( x) | ≪ X l |f^{(l)}(x)|\ll X^{l} for l ⩾ 0 l{\,\geqslant}0. Proofs of the general forms of these results may be deduced by adapting the techniques in section 7, using the relevant transforms of smooth weight functions (separation of variables)

###### Proofs of Theorem 10.1 and 10.2.

Consider coprime r, s ∈ ℤ r,s\in{\mathbb{Z}}. Recall that

 | S ∞, 1 / s ​ ( m, a ​ n, γ) = e ⁡ ( a ​ n ​ s ¯ r) ​ S ​ ( m ​ r ¯, a ​ n, s ​ c) \displaystyle S_{\infty,1/s}(m,an;\gamma)=e\Big(\frac{an\overline{s}}{r}\Big)S(m\overline{r},an;sc) |  |

where γ = c ​ s ​ r \gamma=cs\sqrt{r} for ( c, r) = 1 (c,r)=1. Thus letting b n, r, s ′ = e ( − a n s ¯ / r) b n, r, s b^{\prime}_{n,r,s}=e(-an\overline{s}/r)b_{n,r,s}, we have

 | ℒ = C ​ S ​ R ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ m ∼ M n ∼ N a m ​ b n, r, s ′ ​ ∑ γ ∈ ℝ ∃ ( ∗ ∗ γ ∗) ∈ Γ 0 ​ ( r ​ s) ​ σ 1 / s 1 γ ​ f ​ ( 4 ​ π ​ a ​ m ​ n γ) ​ S ∞, 1 / s ​ ( m, ± a ​ n, γ). \displaystyle\mathcal{L}=CS\sqrt{R}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ n\sim N\end{subarray}}a_{m}\,b_{n,r,s}^{\prime}\sum_{\begin{subarray}{c}\gamma\in{\mathbb{R}}\\ \exists\smallmatrixquantity(\lx@physics@smallmatrix*&*\\\gamma&*\endlx@physics@smallmatrix)\in\Gamma_{0}(rs)\sigma_{1/s}\end{subarray}}\frac{1}{\gamma}\,f\Big(\frac{4\pi\sqrt{amn}}{\gamma}\Big)\,S_{\infty,\,1/s}(m,\pm an;\gamma). |  |

where the innermost summation is taken over numbers γ = c ​ s ​ r \gamma=cs\sqrt{r}, which are the left corner entries of matrices from Γ 0 ​ ( r ​ s) ​ σ 1 / s \Gamma_{0}(rs)\sigma_{1/s}. For simplicity we suppose n > 0 n>0 ( n < 0 n<0 is similar). Next for the inner sum we apply the Kuznetsov formula, giving

(10.5) |  | ℒ \displaystyle\mathcal{L} | = ℋ + ℰ + ℳ \displaystyle=\mathcal{H}+\mathcal{E}+\mathcal{M} |  |

where

 | ℋ \displaystyle\mathcal{H} | = C ​ S ​ R ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ m ∼ M n ∼ N a m ​ b n, r, s ′ ​ ∑ even ​ k f ~ ​ ( k − 1) 2 ​ π ​ ∑ 1 ⩽ j ⩽ θ k ​ ( q) i k ​ ( k − 1)! ( 4 ​ π ​ m ​ n) k − 1 ​ ψ j ​ k ​ ( ∞, m) ¯ ​ ψ j ​ k ​ ( 1 / s, a ​ n) \displaystyle=CS\sqrt{R}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ n\sim N\end{subarray}}a_{m}\,b_{n,r,s}^{\prime}\sum_{{\rm even}\,k}\frac{\widetilde{f}(k-1)}{2\pi}\sum_{1{\,\leqslant}j{\,\leqslant}\theta_{k}(q)}\frac{i^{k}(k-1)!}{(4\pi\sqrt{mn})^{k-1}}\,\overline{\psi_{jk}(\infty,m)}\psi_{jk}(1/s,an) |  |

 | ℰ \displaystyle\mathcal{E} | = C ​ S ​ R ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ m ∼ M n ∼ N a m ​ b n, r, s ′ ​ ∑ 𝔠 1 π ​ ∫ ℝ ( n m) i ​ r ​ φ 𝔠 ​ ∞ ​ m ​ ( 1 2 + i ​ r) ¯ ​ φ 𝔠 ​ 1 / s ​ a ​ n ​ ( 1 2 + i ​ r) ​ f ^ ​ ( r) ​ d r \displaystyle=CS\sqrt{R}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ n\sim N\end{subarray}}a_{m}\,b_{n,r,s}^{\prime}\sum_{\mathfrak{c}}\frac{1}{\pi}\int_{\mathbb{R}}\Big(\frac{n}{m}\Big)^{ir}\overline{{\varphi}_{\mathfrak{c}\infty m}(\tfrac{1}{2}+ir)}{\varphi}_{\mathfrak{c}\,1/s\,an}(\tfrac{1}{2}+ir)\widehat{f}(r)\differential{r} |  |

 | ℳ \displaystyle\mathcal{M} | = C ​ S ​ R ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ m ∼ M n ∼ N a m ​ b n, r, s ′ ​ ∑ j ⩾ 1 ρ j ​ ∞ ​ ( m) ¯ ​ ρ j ​ 1 / s ​ ( a ​ n) ​ f ^ ​ ( κ j) cosh ⁡ π ​ κ j. \displaystyle=CS\sqrt{R}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\begin{subarray}{c}m\sim M\\ n\sim N\end{subarray}}a_{m}\,b^{\prime}_{n,r,s}\sum_{j{\,\geqslant}1}\overline{\rho_{j\infty}(m)}\rho_{j\,1/s}(an)\frac{\widehat{f}(\kappa_{j})}{\cosh\pi\kappa_{j}}. |  |

In the following argument, we shall focus on the Maass contribution ℳ \mathcal{M}, and split ℳ = ℳ reg + ℳ exc \mathcal{M}=\mathcal{M}_{\rm reg}+\mathcal{M}_{\rm exc} into regular and exceptional spectra. (the holomorphic ℋ \mathcal{H} and Eisenstein ℰ \mathcal{E} contributions may be handled similarly to ℳ reg \mathcal{M}_{\rm reg}).

For the Maass contribution ℳ \mathcal{M}, we first apply the factorization as in Lemma 9.6, giving

(10.6) |  | ℳ \displaystyle\mathcal{M} | ≪ C ​ S ​ R ​ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j < 1 4 ( r ​ s) | f ^ ​ ( κ j) | cosh ⁡ π ​ κ j ​ | ∑ m ∼ M a m ​ ρ j ​ ∞ ​ ( m) ¯ | ​ | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′, r, s ​ ρ j ​ 1 / s ​ ( n) |. \displaystyle\ll CS\sqrt{R}\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}<\tfrac{1}{4}}^{(rs)}\frac{|\widehat{f}(\kappa_{j})|}{\cosh\pi\kappa_{j}}\bigg|\sum_{\begin{subarray}{c}m\sim M\end{subarray}}a_{m}\overline{\rho_{j\infty}(m)}\bigg|\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}b_{nn^{\prime\prime},r,s}\,\rho_{j\,1/s}(n)\bigg|. |  |

We split ℳ = ℳ reg + ℳ exc \mathcal{M}=\mathcal{M}_{\rm reg}+\mathcal{M}_{\rm exc} according to whether λ j ⩾ 1 4 \lambda_{j}{\,\geqslant}\frac{1}{4} or λ j < 1 4 \lambda_{j}<\frac{1}{4}, and consider each in turn. For the regular spectrum ℳ reg \mathcal{M}_{\rm reg}, we use the bound f ^ ​ ( κ j) ≪ 1 + | log ⁡ X | 1 + 1 / X \widehat{f}(\kappa_{j})\ll\frac{1+|\log X|}{1+1/X} by Lemma 8.3, for X:= | supp ​ f | ≍ C ​ S ​ R / a ​ M ​ N X:=|{\rm supp}f|\asymp CS\sqrt{R/aMN}. Thus by Cauchy-Schwarz,

 | ℳ reg \displaystyle\mathcal{M}_{\rm reg} | ≪ C ​ S ​ R ​ 1 + | log ⁡ X | 1 + 1 / X ​ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j ⩾ 1 4 ( r ​ s) 1 cosh ⁡ π ​ κ j ​ | ∑ m ∼ M a m ​ ρ j ​ ∞ ​ ( m) ¯ | 2) 1 / 2 \displaystyle\ll CS\sqrt{R}\,\frac{1+|\log X|}{1+1/X}\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}{\,\geqslant}\tfrac{1}{4}}^{(rs)}\frac{1}{\cosh\pi\kappa_{j}}\bigg|\sum_{\begin{subarray}{c}m\sim M\end{subarray}}a_{m}\overline{\rho_{j\infty}(m)}\bigg|^{2}\bigg)^{1/2} |  |

 |  | ⋅ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j ⩾ 1 4 ( r ​ s) 1 cosh ⁡ π ​ κ j ​ | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′, r, s ​ ρ j ​ 1 / s ​ ( n) | 2) 1 / 2 \displaystyle\qquad\qquad\cdot\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}{\,\geqslant}\tfrac{1}{4}}^{(rs)}\frac{1}{\cosh\pi\kappa_{j}}\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}b_{nn^{\prime\prime},r,s}\rho_{j\,1/s}(n)\bigg|^{2}\bigg)^{1/2} |  |

For each r, s r,s, we bound the regular spectra by Theorem 8.2 with μ ⁡ ( ∞) = μ ⁡ ( 1 / s) = 1 / r ​ s \mu(\infty)=\mu(1/s)=1/rs, giving

 | ℳ reg \displaystyle\mathcal{M}_{\rm reg} | ≪ ( C ​ M ​ N ​ R ​ S) ϵ ​ C ​ S ​ R ​ 1 + | log ⁡ X | 1 + 1 / X ​ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ( 1 + 1 X 2 + M 1 + ϵ r ​ s) ​ ‖ 𝐚 M ‖ 2 2) 1 / 2 \displaystyle\ll(CMNRS)^{\epsilon}CS\sqrt{R}\,\frac{1+|\log X|}{1+1/X}\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\Big(1+\frac{1}{X^{2}}+\frac{M^{1+\epsilon}}{rs}\big)\|{\bf a}_{M}\|_{2}^{2}\bigg)^{1/2} |  |

 |  | ⋅ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ( 1 + 1 X 2 + ( N / n ′′) 1 + ϵ r ​ s) ​ ‖ 𝐛 ~ N, r, s ​ ( n ′′) ‖ 2 2) 1 / 2 \displaystyle\qquad\cdot\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\Big(1+\frac{1}{X^{2}}+\frac{(N/n^{\prime\prime})^{1+\epsilon}}{rs}\Big)\|\widetilde{\bf b}_{N,r,s}(n^{\prime\prime})\|_{2}^{2}\bigg)^{1/2} |  |

 |  | ≪ ( C ​ M ​ N ​ R ​ S) ϵ ​ C ​ S ​ R ​ 1 + | log ⁡ X | 1 + 1 / X ​ ( 1 + 1 X 2 + M R ​ S) 1 / 2 ​ R ​ S ​ ‖ 𝐚 M ‖ 2 \displaystyle\ll(CMNRS)^{\epsilon}CS\sqrt{R}\,\frac{1+|\log X|}{1+1/X}\Big(1+\frac{1}{X^{2}}+\frac{M}{RS}\Big)^{1/2}\sqrt{RS}\|{\bf a}_{M}\|_{2} |  |

 |  | ⋅ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ ( ( 1 + 1 X 2 + N n ′′ ​ R ​ S) 1 / 2 ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 CLOSE \displaystyle\qquad\cdot\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\bigg(\Big(1+\frac{1}{X^{2}}+\frac{N}{n^{\prime\prime}RS}\Big)^{1/2}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2} |  |

by the divisor bound, and noting ∑ r, s ‖ 𝐛 N, r, s ‖ 2 2 = ∑ n, r, s | 𝐛 n, r, s | 2 = ‖ 𝐛 N, R, S ‖ 2 2 \sum_{r,s}\|{\bf b}_{N,r,s}\|_{2}^{2}=\sum_{n,r,s}|{\bf b}_{n,r,s}|^{2}=\|{\bf b}_{N,R,S}\|_{2}^{2}. Recalling X 2 ≍ C 2 ​ S 2 ​ R / a ​ M ​ N X^{2}\asymp C^{2}S^{2}R/aMN, we have

 | ℳ reg \displaystyle\mathcal{M}_{\rm reg} | ≪ ( C ​ M ​ N ​ R ​ S) ϵ ​ C ​ S ​ R 1 + 1 / C ​ S ​ R / a ​ M ​ N ​ ( 1 + a ​ M ​ N C 2 ​ S 2 ​ R + M R ​ S) 1 / 2 ​ R ​ S ​ ‖ 𝐚 M ‖ 2 \displaystyle\ll(CMNRS)^{\epsilon}\frac{CS\sqrt{R}}{1+1/CS\sqrt{R/aMN}}\Big(1+\frac{aMN}{C^{2}S^{2}R}+\frac{M}{RS}\Big)^{1/2}\sqrt{RS}\|{\bf a}_{M}\|_{2} |  |

 |  | ⋅ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ ( 1 + a ​ M ​ N C 2 ​ S 2 ​ R + Q ′′ ​ N n ′′ ​ R ​ S) 1 / 2 ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 =: J reg. \displaystyle\qquad\cdot\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\Big(1+\frac{aMN}{C^{2}S^{2}R}+\frac{Q^{\prime\prime}N}{n^{\prime\prime}RS}\Big)^{1/2}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}=:J_{\rm reg}. |  |

The same argument holds for holomorphic ℋ \mathcal{H} and Eisenstein ℰ \mathcal{E} contributions, so that

(10.7) |  | ℋ + ℰ + ℳ reg ≪ J reg. \displaystyle\mathcal{H}+\mathcal{E}+\mathcal{M}_{\rm reg}\ \ll\ J_{\rm reg}. |  |

It is remains to handle the exceptional spectra ℳ exc \mathcal{M}_{\rm exc}. Recall | f ^ ​ ( κ j) | ≪ 1 + X 2 ​ i ​ κ j 1 + 1 / X |\widehat{f}(\kappa_{j})|\ll\frac{1+X^{2i\kappa_{j}}}{1+1/X} by ( 8.11) in Lemma 8.3 with r = i ​ κ j ∈ ( 0, 1 / 2) r=i\kappa_{j}\in(0,1/2). This gives

 | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ C ​ S ​ R 1 + 1 / X ​ ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j < 1 4 ( r ​ s) 1 + X 2 ​ i ​ κ j cosh ⁡ π ​ κ j ​ | ∑ m ∼ M a m ​ ρ j ​ ∞ ​ ( m) ¯ | ​ | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′, r, s ​ ρ j ​ 1 / s ​ ( n) | \displaystyle\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\frac{CS\sqrt{R}}{1+1/X}\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}<\tfrac{1}{4}}^{(rs)}\frac{1+X^{2i\kappa_{j}}}{\cosh\pi\kappa_{j}}\bigg|\sum_{m\sim M}a_{m}\overline{\rho_{j\infty}(m)}\bigg|\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}b_{nn^{\prime\prime},r,s}\rho_{j\,1/s}(n)\bigg| |  |

For X 0 X_{0} to be determined, we split 1 + X 2 ​ i ​ κ j ⩽ ( 1 + X / X 0) 2 ​ i ​ κ j ​ X 0 i ​ κ j 1+X^{2i\kappa_{j}}{\,\leqslant}(1+X/\sqrt{X_{0}})^{2i\kappa_{j}}\,X_{0}^{i\kappa_{j}} and apply Cauchy-Schwarz,

(10.8) |  | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ C ​ S ​ R 1 + 1 / X ​ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j < 1 4 ( r ​ s) ( 1 + X / X 0) 4 ​ i ​ κ j ​ | ∑ m ∼ M a m ​ ρ j ​ ∞ ​ ( m) ¯ | 2) 1 / 2 \displaystyle\ll\frac{CS\sqrt{R}}{1+1/X}\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}<\tfrac{1}{4}}^{(rs)}\big(1+X/\sqrt{X_{0}}\big)^{4i\kappa_{j}}\bigg|\sum_{m\sim M}a_{m}\,\overline{\rho_{j\infty}(m)}\bigg|^{2}\bigg)^{1/2} |  |

(10.9) |  |  | ⋅ ( ∑ r ∼ R s ∼ S ( r, s) = 1 ∑ λ j < 1 4 ( r ​ s) ( 1 + X 0) 2 ​ i ​ κ j ​ | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′, r, s ​ ρ j, 1 / s ​ ( n) | 2) 1 / 2. \displaystyle\qquad\qquad\qquad\qquad\quad\quad\ \cdot\bigg(\sum_{\begin{subarray}{c}r\sim R\\ s\sim S\\ (r,s)=1\end{subarray}}\sum_{\lambda_{j}<\tfrac{1}{4}}^{(rs)}(1+X_{0})^{2i\kappa_{j}}\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}\,b_{nn^{\prime\prime},r,s}\,\rho_{j,1/s}(n)\bigg|^{2}\bigg)^{1/2}. |  |

We shall choose X 0 = 1 + R ​ S ​ n ′′ / N X_{0}=1+RSn^{\prime\prime}/N.

Note the sum in ( 10.8) over a m ​ ρ j ​ ∞ ​ ( m) a_{m}\,\rho_{j\,\infty}(m) equals S ⁡ ( R ​ S, ( 1 + X / X 0) 2, M, 0) S(RS,(1+X/\sqrt{X_{0}})^{2},M,0).

For the sum in ( 10.9), we apply Theorem 9.1 (with ‘ 𝔞 \mathfrak{a} ’ = 1 / s =1/s, ‘ X X ’ = 1 + X 0 =1+X_{0}, ‘ a n a_{n} ’ = b n, r, s ∗ =b_{n,r,s}^{*}) to get

 | ∑ λ j < 1 4 ( r ​ s) X 0 2 ​ i ​ κ j | ∑ n ∼ N / n ′′ ( n, a) = 1 b n ​ n ′′, r, s ​ ρ j, 1 / s ​ ( n CLOSE ¯ \displaystyle\sum_{\lambda_{j}<\tfrac{1}{4}}^{(rs)}X_{0}^{2i\kappa_{j}}\bigg|\sum_{\begin{subarray}{c}n\sim N/n^{\prime\prime}\\ (n,a)=1\end{subarray}}\,b_{nn^{\prime\prime},r,s}\,\overline{\rho_{j,1/s}(n} | ) | 2 ≪ ( 1 + X 0 θ) ( 1 + ( ( N / n ′′) 1 + ϵ r ​ s) 1 − θ) ∥ 𝐛 ~ N, r, s ( n ′′) ∥ 2 2 \displaystyle)\bigg|^{2}\ll\big(1+X_{0}^{{\theta}}\big)\Big(1+\Big(\frac{(N/n^{\prime\prime})^{1+\epsilon}}{rs}\Big)^{1-{\theta}}\Big)\|\widetilde{\bf b}_{N,r,s}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | ≪ N ϵ ​ ( 1 + ( N n ′′ ​ R ​ S) θ) ​ ( 1 + ( N n ′′ ​ R ​ S) 1 − θ) ​ ‖ 𝐛 N, r, s ∗ ​ ( n ′′) ‖ 2 2 \displaystyle\ll N^{\epsilon}\Big(1+\Big(\frac{N}{n^{\prime\prime}RS}\Big)^{{\theta}}\Big)\Big(1+\Big(\frac{N}{n^{\prime\prime}RS}\Big)^{1-{\theta}}\Big)\|{\bf b}^{*}_{N,r,s}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | ≪ N ϵ ​ ( 1 + N n ′′ ​ R ​ S) ​ ‖ 𝐛 ~ N, r, s ​ ( n ′′) ‖ 2 2. \displaystyle\ll\ N^{\epsilon}\Big(1+\frac{N}{n^{\prime\prime}RS}\Big)\|\widetilde{\bf b}_{N,r,s}(n^{\prime\prime})\|_{2}^{2}. |  |

Plugging this into ( 10.9), and noting ∑ r, s ‖ 𝐛 N, r, s ‖ 2 2 = ∑ n, r, s | b n, r, s | 2 = ‖ 𝐛 N, R, S ‖ 2 2 \sum_{r,s}\|{\bf b}_{N,r,s}\|_{2}^{2}=\sum_{n,r,s}|b_{n,r,s}|^{2}=\|{\bf b}_{N,R,S}\|_{2}^{2}, we obtain

 | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ ∑ n ′′ | a ∞ n ′′ ≪ N ( a n ′′) θ / 2 S ( R S, ( 1 + X / X 0) 2, M, 0) 1 / 2 ( 1 + N n ′′ ​ R ​ S) 1 / 2 ∥ 𝐛 ~ N, R, S ( n ′′) ∥ 2 × \displaystyle\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\,S\big(RS,(1+X/\sqrt{X_{0}})^{2},M,0\big)^{1/2}\Big(1+\frac{N}{n^{\prime\prime}RS}\Big)^{1/2}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}\,\times |  |

(10.10) |  |  | × ( C ​ M ​ N ​ R ​ S) ϵ ​ C ​ S ​ R 1 + 1 / X. \displaystyle\qquad\times(CMNRS)^{\epsilon}\frac{CS\sqrt{R}}{1+1/X}. |  |

To prove Theorem 10.1, we apply Theorem 9.3 with Q = R ​ S Q=RS, ‘ X X ’ = 1 + X / X 0 =1+X/\sqrt{X_{0}},

 | S ( a m) ​ ( CLOSE \displaystyle S_{(a_{m})}\big( | OPEN R ​ S, ( 1 + X / X 0) 2, M, 0) \displaystyle RS,(1+X/\sqrt{X_{0}})^{2},M,0\big) |  |

 |  | ≪ ( M ​ R ​ S) ϵ ​ ( R ​ S + M + M ​ ( 1 + X / X 0) 2 ​ θ + R ​ S ​ ( ( 1 + X / X 0) ​ M R ​ S) 2 ​ θ) ​ ‖ 𝐚 M ‖ 2 2 \displaystyle\ \ll\ (MRS)^{\epsilon}\,\big(RS+M+M(1+X/\sqrt{X_{0}})^{2{\theta}}+RS\big((1+X/\sqrt{X_{0}})\frac{\sqrt{M}}{RS}\big)^{2{\theta}}\big)\|{\bf a}_{M}\|_{2}^{2} |  |

 |  | ≪ ( M ​ R ​ S) ϵ ​ ( R ​ S + M + ( 1 + X 2 / X 0) θ ​ ( M + M θ ​ ( R ​ S) 1 − 2 ​ θ)) ​ ‖ 𝐚 M ‖ 2 2 \displaystyle\ \ll\ (MRS)^{\epsilon}\,\Big(RS+M+(1+X^{2}/X_{0})^{{\theta}}\Big(M+M^{\theta}\,(RS)^{1-2{\theta}}\Big)\Big)\|{\bf a}_{M}\|_{2}^{2} |  |

 |  | ≪ ( M ​ R ​ S) ϵ ​ ( R ​ S + M + ( 1 + C 2 ​ S 2 ​ R a ​ M ​ ( N + R ​ S ​ n ′′)) θ ​ ( M + M θ ​ ( R ​ S) 1 − 2 ​ θ)) ​ ‖ 𝐚 M ‖ 2 2 \displaystyle\ \ll\ (MRS)^{\epsilon}\,\Big(RS+M+\Big(1+\frac{C^{2}S^{2}R}{aM(N+RSn^{\prime\prime})}\Big)^{{\theta}}\Big(M+M^{\theta}\,(RS)^{1-2{\theta}}\Big)\Big)\|{\bf a}_{M}\|_{2}^{2} |  |

(10.11) |  |  | ≪ ( M ​ R ​ S) ϵ ​ ( R ​ S + M + ( C 2 ​ S 2 ​ R a ⁡ ( N + R ​ S ​ n ′′)) θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ)) ​ ‖ 𝐚 M ‖ 2 2 \displaystyle\ \ll\ (MRS)^{\epsilon}\,\Big(RS+M+\Big(\frac{C^{2}S^{2}R}{a(N+RSn^{\prime\prime})}\Big)^{{\theta}}\big(M^{1-{\theta}}+(RS)^{1-2{\theta}}\big)\Big)\|{\bf a}_{M}\|_{2}^{2} |  |

recalling X 2 ≍ C 2 ​ S 2 ​ R / a ​ M ​ N X^{2}\asymp C^{2}S^{2}R/aMN, X 0 = 1 + R ​ S ​ n ′′ / N X_{0}=1+RSn^{\prime\prime}/N (so X 2 / X 0 ≍ C 2 ​ S 2 ​ R / a ​ M ​ ( N + R ​ S ​ n ′′) X^{2}/X_{0}\asymp C^{2}S^{2}R/aM(N+RSn^{\prime\prime}) along with 1 / ( 1 + 1 / X) ≍ C ​ S ​ R / ( C ​ S ​ R + a ​ M ​ N) 1/(1+1/X)\asymp CS\sqrt{R}/(CS\sqrt{R}+\sqrt{aMN})). Thus ( 10) becomes

 | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ C 2 ​ S 2 ​ R ​ ( C ​ M ​ N ​ R ​ S) ϵ a ​ M ​ N + C ​ S ​ R ∥ 𝐚 M ∥ 2 ∑ n ′′ | a ∞ n ′′ ≪ N ( a n ′′) θ / 2 ∥ 𝐛 ~ N, R, S ( n ′′) ∥ 2 × \displaystyle\ll\frac{C^{2}S^{2}R(CMNRS)^{\epsilon}}{\sqrt{aMN}+CS\sqrt{R}}\,\|{\bf a}_{M}\|_{2}\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}\ \times |  |

 |  | × ( R ​ S + M + ( a ​ n ′′) − θ ​ ( C 2 ​ S 2 ​ R N / n ′′ + R ​ S) θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ)) 1 2 ​ ( 1 + N n ′′ ​ R ​ S) 1 2 \displaystyle\qquad\times\bigg(RS+M+(an^{\prime\prime})^{-{\theta}}\Big(\frac{C^{2}S^{2}R}{N/n^{\prime\prime}+RS}\Big)^{{\theta}}\big(M^{1-{\theta}}+(RS)^{1-2{\theta}}\big)\bigg)^{\frac{1}{2}}\Big(1+\frac{N}{n^{\prime\prime}RS}\Big)^{\frac{1}{2}} |  |

For the third term in the sum over n ′′ | a ∞ n^{\prime\prime}\mid a^{\infty}, we apply ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 ⩽ ‖ 𝐛 N, R, S ‖ 2 \|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}{\,\leqslant}\|{\bf b}_{N,R,S}\|_{2}, θ ⩽ θ \theta{\,\leqslant}\theta, and the divisor bound, giving

 | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ C 2 ​ S ​ R ​ S ​ ( C ​ M ​ N ​ R ​ S) ϵ a ​ M ​ N + C ​ S ​ R ​ ‖ 𝐚 M ‖ 2 ​ ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ( M + R ​ S) ​ ( N n ′′ + R ​ S) ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\ll\frac{C^{2}S\sqrt{RS}(CMNRS)^{\epsilon}}{\sqrt{aMN}+CS\sqrt{R}}\,\|{\bf a}_{M}\|_{2}\Big(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}(M+RS)\Big(\frac{N}{n^{\prime\prime}}+RS\Big)\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2} |  |

(10.12) |  |  | OPEN + ( C ​ S ​ R) 2 ​ θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ) ​ ( N + R ​ S) 1 − θ ​ ‖ 𝐛 N, R, S ‖ 2 2) 1 2 =: J exc, \displaystyle\qquad\qquad+\ (CS\sqrt{R})^{2{\theta}}(M^{1-{\theta}}+(RS)^{1-2{\theta}})(N+RS)^{1-{\theta}}\|{\bf b}_{N,R,S}\|_{2}^{2}\Big)^{\frac{1}{2}}\ =:J_{\rm exc}, |  |

Combining ( 10) and ( 10) (we factor out C ​ S C\sqrt{S} from each parenthesis) gives

 | ℒ \displaystyle\mathcal{L} | = ℋ + ℰ + ℳ reg + ℳ exc ≪ J reg + J exc \displaystyle=\mathcal{H}+\mathcal{E}+\mathcal{M}_{\rm reg}+\mathcal{M}_{\rm exc}\ll J_{\rm reg}+J_{\rm exc} |  |

 |  | ≪ C 2 ​ S ​ R ​ S ​ ( C ​ M ​ N ​ R ​ S) ϵ a ​ M ​ N + C ​ S ​ R ∥ 𝐚 M ∥ 2 ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a n ′′) θ ∥ 𝐛 ~ N, R, S ( n ′′) ∥ 2 2 × \displaystyle\ll\frac{C^{2}S\sqrt{RS}(CMNRS)^{\epsilon}}{\sqrt{aMN}+CS\sqrt{R}}\,\|{\bf a}_{M}\|_{2}\Bigg(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2}\;\times |  |

 |  | × { ( N n ′′ + R ​ S + a ​ M ​ N C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N C 2 ​ S) + ( N n ′′ + R ​ S) ​ ( M + R ​ S) } \displaystyle\qquad\qquad\times\bigg\{\Big(\frac{N}{n^{\prime\prime}}+RS+\frac{aMN}{C^{2}S}\Big)\Big(M+RS+\frac{aMN}{C^{2}S}\Big)+\Big(\frac{N}{n^{\prime\prime}}+RS\Big)(M+RS)\bigg\} |  |

 |  | OPEN + ( C ​ S ​ R) 2 ​ θ ​ ( N + R ​ S) 1 − θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ) ​ ‖ 𝐛 N, R, S ‖ 2 2) 1 2 \displaystyle\qquad\qquad+(CS\sqrt{R})^{2{\theta}}(N+RS)^{1-{\theta}}\big(M^{1-{\theta}}+(RS)^{1-2{\theta}}\big)\|{\bf b}_{N,R,S}\|_{2}^{2}\Bigg)^{\frac{1}{2}} |  |

The term ‘ + ( N / n ′′ + R S) ( M + R S) } +\,(N/n^{\prime\prime}+RS)(M+RS)\big\} ’ in the sum above may be absorbed into the contribution of J reg J_{\rm reg}, giving

 | ℒ \displaystyle\mathcal{L} | ≪ ( C ​ M ​ N ​ R ​ S) ϵ ​ C 2 ​ S ​ R ​ S ​ ‖ 𝐚 M ‖ 2 a ​ M ​ N + C ​ S ​ R \displaystyle\ll(CMNRS)^{\epsilon}\frac{C^{2}S\sqrt{RS}\|{\bf a}_{M}\|_{2}}{\sqrt{aMN}+CS\sqrt{R}} |  |

(10.13) |  |  | ⋅ ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ( N n ′′ + R ​ S + a ​ M ​ N C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N C 2 ​ S) ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\cdot\Bigg(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\Big(\frac{N}{n^{\prime\prime}}+RS+\frac{aMN}{C^{2}S}\Big)\Big(M+RS+\frac{aMN}{C^{2}S}\Big)\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | OPEN + ( C ​ S ​ R) 2 ​ θ ​ ( N + R ​ S) 1 − θ ​ ( M 1 − θ + ( R ​ S) 1 − 2 ​ θ) ​ ‖ 𝐛 N, R, S ‖ 2 2) 1 2. \displaystyle\qquad\qquad\qquad+\ (CS\sqrt{R})^{2{\theta}}(N+RS)^{1-{\theta}}\big(M^{1-{\theta}}+(RS)^{1-2{\theta}}\big)\|{\bf b}_{N,R,S}\|_{2}^{2}\Bigg)^{\frac{1}{2}}. |  |

This completes the proof of Theorem 10.1.

To prove Theorem 10.2, we apply Theorem 9.5 with Q = R ​ S Q=RS, ‘ X X ’ = 1 + X / X 0 =1+X/\sqrt{X_{0}},

 | S ( 𝟏 m ∼ M) ​ ( R ​ S CLOSE, \displaystyle S_{(\mathbf{1}_{m\sim M})}\big(RS, | OPEN ( 1 + X / X 0) 2, M, 0) \displaystyle(1+X/\sqrt{X_{0}})^{2},M,0\big) |  |

 |  | ≪ ( M ​ R ​ S) ϵ ​ ( 1 + ( M ​ ( 1 + X / X 0) 2 ( R ​ S + M) 2) θ) ​ ( R ​ S + M) ​ M \displaystyle\ \ll\ (MRS)^{\epsilon}\,\Big(1+\Big(\frac{M(1+X/\sqrt{X_{0}})^{2}}{(RS+M)^{2}}\Big)^{\theta}\Big)(RS+M)M |  |

 |  | ≪ ( M ​ R ​ S) ϵ ​ ( 1 + ( a ​ n ′′) − θ ​ ( C 2 ​ S 2 ​ R ( R ​ S + M) 2 ​ ( N / n ′′ + R ​ S)) θ) ​ ( R ​ S + M) ​ M \displaystyle\ \ll\ (MRS)^{\epsilon}\,\Big(1+(an^{\prime\prime})^{-{\theta}}\Big(\frac{C^{2}S^{2}R}{(RS+M)^{2}(N/n^{\prime\prime}+RS)}\Big)^{\theta}\Big)(RS+M)M |  |

So plugging back into ( 10) gives

 | ℳ exc \displaystyle\mathcal{M}_{\rm exc} | ≪ C ​ S ​ R 1 + 1 / X ​ ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ / 2 ​ S ​ ( R ​ S, ( 1 + X / X 0) 2, M, 0) 1 2 ​ ( 1 + ( N n ′′ ​ R ​ S)) 1 2 ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 \displaystyle\ll\frac{CS\sqrt{R}}{1+1/X}\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}/2}\,S(RS,(1+X/\sqrt{X_{0}})^{2},M,0)^{\frac{1}{2}}\Big(1+\Big(\frac{N}{n^{\prime\prime}RS}\Big)\Big)^{\frac{1}{2}}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2} |  |

(10.14) |  |  | ≪ ∑ n ′′ | a ∞ n ′′ ≪ N ( ( a ​ n ′′) θ / 2 + ( C 2 ​ S 2 ​ R ( R ​ S + M) 2 ​ ( N / n ′′ + R ​ S)) θ / 2) ​ N / n ′′ + R ​ S \displaystyle\qquad\quad\ll\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}\,\Big((an^{\prime\prime})^{{\theta}/2}+\Big(\frac{C^{2}S^{2}R}{(RS+M)^{2}(N/n^{\prime\prime}+RS)}\Big)^{{\theta}/2}\Big)\sqrt{N/n^{\prime\prime}+RS} |  |

 |  | ⋅ C 2 ​ S ​ R ​ S a ​ M ​ N + C ​ S ​ R ​ M + R ​ S ​ M ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2. \displaystyle\qquad\qquad\qquad\cdot\frac{C^{2}S\sqrt{RS}}{\sqrt{aMN}+CS\sqrt{R}}\sqrt{M+RS}\sqrt{M}\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}. |  |

Thus combining with ( 10), we obtain

 | ℒ \displaystyle\mathcal{L} | = ℋ + ℰ + ℳ reg + ℳ exc ≪ J reg + J exc \displaystyle=\mathcal{H}+\mathcal{E}+\mathcal{M}_{\rm reg}+\mathcal{M}_{\rm exc}\ll J_{\rm reg}+J_{\rm exc} |  |

 |  | ≪ ( C M N R S) ϵ C 2 ​ S ​ R ​ S a ​ M ​ N + C ​ S ​ R M × \displaystyle\ll(CMNRS)^{\epsilon}\frac{C^{2}S\sqrt{RS}}{\sqrt{aMN}+CS\sqrt{R}}\,\sqrt{M}\times |  |

 |  | × ∑ n ′′ | a ∞ n ′′ ≪ N ( ( a ​ n ′′) θ ​ ( N n ′′ + R ​ S + a ​ M ​ N C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N C 2 ​ S) ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\times\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}\Bigg((an^{\prime\prime})^{{\theta}}\Big(\frac{N}{n^{\prime\prime}}+RS+\frac{aMN}{C^{2}S}\Big)\Big(M+RS+\frac{aMN}{C^{2}S}\Big)\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | OPEN + ( ( a ​ n ′′) θ + ( C 2 ​ S 2 ​ R ( R ​ S + M) 2 ​ ( N / n ′′ + R ​ S)) θ) ​ ( N / n ′′ + R ​ S) ​ ( M + R ​ S) ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 2) 1 2 \displaystyle\qquad+\,\Big((an^{\prime\prime})^{{\theta}}+\Big(\frac{C^{2}S^{2}R}{(RS+M)^{2}(N/n^{\prime\prime}+RS)}\Big)^{{\theta}}\Big)(N/n^{\prime\prime}+RS)(M+RS)\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2}\Bigg)^{\tfrac{1}{2}} |  |

The term ‘ ( a ​ n ′′) θ + (an^{\prime\prime})^{{\theta}}\,+ ’ in the factor ( ( a n ′′) θ + ( C 2 S 2 R / ⋯) θ) \big((an^{\prime\prime})^{{\theta}}+(C^{2}S^{2}R/\cdots)^{{\theta}}\big) may be absorbed into the contribution of J reg J_{\rm reg}. Hence applying ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 ⩽ ‖ 𝐛 N, R, S ‖ 2 \|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}{\,\leqslant}\|{\bf b}_{N,R,S}\|_{2} and the divisor bound, we obtain

 | ℒ \displaystyle\mathcal{L} | ≪ ( C M N R S) ϵ C 2 ​ S ​ R ​ S a ​ M ​ N + C ​ S ​ R M × \displaystyle\ll(CMNRS)^{\epsilon}\frac{C^{2}S\sqrt{RS}}{\sqrt{aMN}+CS\sqrt{R}}\,\sqrt{M}\times |  |

 |  | × ( ∑ n ′′ | a ∞ n ′′ ≪ N ( a ​ n ′′) θ ​ ( N n ′′ + R ​ S + a ​ M ​ N C 2 ​ S) ​ ( M + R ​ S + a ​ M ​ N C 2 ​ S) ​ ‖ 𝐛 ~ N, R, S ​ ( n ′′) ‖ 2 2 CLOSE \displaystyle\times\Bigg(\sum_{\begin{subarray}{c}n^{\prime\prime}\mid a^{\infty}\\ n^{\prime\prime}\ll N\end{subarray}}(an^{\prime\prime})^{{\theta}}\Big(\frac{N}{n^{\prime\prime}}+RS+\frac{aMN}{C^{2}S}\Big)\Big(M+RS+\frac{aMN}{C^{2}S}\Big)\|\widetilde{\bf b}_{N,R,S}(n^{\prime\prime})\|_{2}^{2} |  |

 |  | OPEN + ( C 2 ​ S 2 ​ R) θ ​ ( N + R ​ S) 1 − θ ​ ( M + R ​ S) 1 − 2 ​ θ ​ ‖ 𝐛 N, R, S ‖ 2 2) 1 2 \displaystyle\qquad\qquad+\,(C^{2}S^{2}R)^{{\theta}}(N+RS)^{1-{\theta}}(M+RS)^{1-2{\theta}}\|{\bf b}_{N,R,S}\|_{2}^{2}\Bigg)^{\tfrac{1}{2}} |  |

This completes the proof of Theorem 10.2. ∎

###### Proof of Theorem 1.8 from Theorem 10.2.

Standard completion of sums argument, using Poisson summation. See [11, Theorem 2.1] or [9, Theorem 12]. ∎

## Appendix A Optimality of Theorems 9.3 and 9.5

by Sary Drappeau and Jared Duker Lichtman

In this appendix, we give a heuristic argument to illustrate the bounds given in Theorems 9.3 and 9.5. We hope these heuristics shed some light on the proofs of Theorems 9.3 and 9.5. The actual argument we describe is slightly different, but we feel it better motivates the steps in the original arguments of [9], and explains the shape of the final bound.

Let Q, N, Y > 0 Q,N,Y>0, and θ = sup q ∼ Q θ q {\theta}=\sup_{q\sim Q}{\theta}_{q} with θ q = 2 ​ i ​ κ 1 {\theta}_{q}=2i\kappa_{1}. Define

(A.1) |  | S ⁡ ( Q, N, Y):= sup 𝐚 = ( a n) n 1 ‖ 𝐚 N ‖ ​ ∑ q ∼ Q ∑ λ j < 1 / 4 ( q) Y 2 ​ i ​ κ j ​ | ∑ n ∼ N a n ​ ρ j ​ ∞ ​ ( n) |, S(Q,N,Y):=\sup_{{\bf a}=(a_{n})_{n}}\frac{1}{\|{\bf a}_{N}\|}\sum_{q\sim Q}\sum_{\lambda_{j}<1/4}^{(q)}Y^{2i\kappa_{j}}\Big|\sum_{n\sim N}a_{n}\rho_{j\infty}(n)\Big|, |  |

where the supremum is over all non-zero sequences a n a_{n}. The heuristics we explain below will give a genuine proof of Theorems 9.3 and 9.5, but only in the regime where Q = N q Q=N^{q}, Y = N y Y=N^{y} with q, y > 0 q,y>0 fixed, or varying in a bounded set; the implied constant could depend on the size of q q and y y, whereas Theorems 9.3 and 9.5 are uniform.

The upper-bound 2 ​ i ​ κ j ≤ θ 2i\kappa_{j}\leq{\theta} implies, for all 1 ≤ Z ≤ Y 1\leq Z\leq Y,

(A.2) |  | S ⁡ ( Q, N, Y) ≤ ( Y / Z) θ ​ S ​ ( Q, N, Z). S(Q,N,Y)\leq(Y/Z)^{\theta}S(Q,N,Z). |  |

By the recursion in Lemma 9.2, we have

(A.3) |  | S ( Q, N, Y) ≪ ϵ S ( π N Y / Q, N, Y) + ( Y N) ϵ ( Q + N + N Y / Q). S(Q,N,Y)\ll_{\epsilon}S(\pi NY/Q,N,Y)+(YN)^{\epsilon}(Q+N+NY/Q). |  |

Finally, by the spectral large sieve in Theorem 8.2,

(A.4) |  | S ⁡ ( Q, N, 1) + S ⁡ ( Q, N, Q / N) ≪ Q + N 1 + ϵ. S(Q,N,1)+S(Q,N,Q/N)\ll Q+N^{1+\epsilon}. |  |

Our aim is to explain the shape of the best bound for S ⁡ ( Q, N, Y) S(Q,N,Y) one can extract from these three hypotheses only.

For q, y ≥ 0 q,y\geq 0, we define

 | E ⁡ ( q, y):= inf { σ ≥ 0: S ⁡ ( N q, N, N y) ≪ N σ }. E(q,y):=\inf\{\sigma\geq 0\,:\,S(N^{q},N,N^{y})\ll N^{\sigma}\}. |  |

The bounds in ( A.2)–( A.4) translate into the following for E ⁡ ( q, z) E(q,z):

(A.5) |  | E ⁡ ( q, z) ≤ \displaystyle E(q,z)\leq{} | E ⁡ ( q, y) ≤ E ⁡ ( q, z) + θ ⁡ ( y − z) \displaystyle E(q,y)\leq E(q,z)+{\theta}(y-z) |  | for ​ 0 ≤ z ≤ y, \displaystyle\text{for }\ 0\leq z\leq y, |  |

(A.6) |  |  | E ⁡ ( q, y) ≤ max ⁡ ( E ⁡ ( 1 + y − q, y), q, 1, 1 + y − q) \displaystyle E(q,y)\leq\max(E(1+y-q,y),q,1,1+y-q) |  | for ​ 0 ≤ q ≤ y + 1, \displaystyle\text{for }\ 0\leq q\leq y+1, |  |

(A.7) |  |  | E ⁡ ( q, y) ≤ max ⁡ ( q, 1) \displaystyle E(q,y)\leq\max(q,1) |  | for ​ y ≤ max ⁡ ( 0, q − 1). \displaystyle\text{for }\ y\leq\max(0,q-1). |  |

We show that maximal map satisfying ( A.5)–( A.7) is given by the following map M ⁡ ( q, y) M(q,y),

 | M ⁡ ( q, y):= max ⁡ ( q, 1 + θ ​ y, q + θ ⁡ ( 1 + y − 2 ​ q)). M(q,y):=\max\Big(q,\,1+{\theta}y,\,q+{\theta}(1+y-2q)\Big). |  |

###### Proposition A.1.

The map M M satisfies the bounds ( A.5)–( A.7) Moreoover, any map E: ℝ + 2 → ℝ + E:{\mathbb{R}}_{+}^{2}\to{\mathbb{R}}_{+} that satisfies the bounds ( A.5)–( A.7) also satisfies E ⁡ ( q, y) ≤ M ⁡ ( q, y) E(q,y)\leq M(q,y).

Proposition A.1 indicates that the bound

 | S ⁡ ( Q, N, Y) ≪ ( Q ​ N ​ Y) ϵ ​ ( Q + N ​ Y θ + Q ​ ( N ​ Y / Q 2) θ) S(Q,N,Y)\ll(QNY)^{\epsilon}\big(Q+NY^{\theta}+Q(NY/Q^{2})^{\theta}\big) |  |

should hold true, which witnesses Theorem 9.3, as in ( 9.9). Moreover, this is the optimal result possible from the bounds ( A.2)–( A.4).

When the supremum in the definition ( A.1) is restricted to the characteristic sequence of an interval a n = 𝟏 [N, N 1] ​ ( n) a_{n}={\mathbf{1}}_{[N,N_{1}]}(n), then from [9, p.277] with Y = Q + N Y=Q+N, we have

 | S ⁡ ( Q, N, Q + N) ≪ ( Q ​ N) ϵ ​ ( Q + N). S(Q,N,Q+N)\ll(QN)^{\epsilon}(Q+N). |  |

Translating to the model, this gives

(A.8) |  |  | E ⁡ ( q, y) ≤ y for ​ y = max ⁡ ( q, 1). \displaystyle E(q,y)\leq y\qquad\qquad\text{for }\ y=\max(q,1). |  |

We show that maximal map satisfying ( A.5)–( A.8) is given by M ∗ M^{*}, as follows

 | M ∗ ​ ( q, y):= max ⁡ ( q, 1, 1 + θ ⁡ ( y − 1), q + θ ⁡ ( 1 + y − 2 ​ q)). \displaystyle M^{*}(q,y):=\max\Big(q,\,1,\,1+{\theta}(y-1),\,q+{\theta}(1+y-2q)\Big). |  |

###### Proposition A.2.

The map M ∗: ℝ + 2 → ℝ + M^{*}:{\mathbb{R}}_{+}^{2}\to{\mathbb{R}}_{+} satisfies the conditions ( A.5)–( A.8). Moreover, any map E: ℝ + 2 → ℝ + E:{\mathbb{R}}_{+}^{2}\to{\mathbb{R}}_{+} that satisfies ( A.5)–( A.8) also satisfies E ⁡ ( q, y) ≤ M ∗ ​ ( q, y) E(q,y)\leq M^{*}(q,y).

Proposition A.2 may be interpreted as showing

 | S ⁡ ( Q, N, Y) \displaystyle S(Q,N,Y) | ≪ ( Q ​ N ​ Y) ϵ ​ ( Q + N + N ​ ( Y / N) θ + Q ​ ( N ​ Y / Q 2) θ) \displaystyle\ll(QNY)^{\epsilon}\big(Q+N+N(Y/N)^{\theta}+Q(NY/Q^{2})^{\theta}\big) |  |

 |  | ≍ ( Q ​ N ​ Y) ϵ ​ ( Q + N) ​ ( 1 + ( N ​ Y / [Q + N] 2) θ), \displaystyle\asymp(QNY)^{\epsilon}(Q+N)\big(1+(NY/[Q+N]^{2})^{\theta}\big), |  |

when restricting the supremum S S in ( A.1) to characteristic sequences of intervals. This witnesses Theorem 9.5. Moreover, this is the optimal result attained from the bounds ( A.2)–( A.4) and S ⁡ ( Q, N, Q + N) ≪ ( Q ​ N) ϵ ​ ( Q + N) S(Q,N,Q+N)\ll(QN)^{\epsilon}(Q+N).

### A.1. Verifying the maps M M and M ∗ M^{*}

Here we quickly prove the first part of Propositions A.1 and A.2, by verifying that M M and M ∗ M^{*} satisfy the stated conditions.

To show ( A.5) for M M: for z ⩽ y z{\,\leqslant}y by definition we have M ⁡ ( q, z) ⩽ M ⁡ ( q, y) M(q,z){\,\leqslant}M(q,y) and

 | M ⁡ ( q, y) ⩽ max ⁡ ( q + θ ⁡ ( y − z), 1 + θ ​ y, q + θ ⁡ ( 1 + y − 2 ​ q)) = M ⁡ ( q, z) + θ ⁡ ( y − z). \displaystyle M(q,y){\,\leqslant}\max\big(q+{\theta}(y-z),1+{\theta}y,q+{\theta}(1+y-2q)\big)=M(q,z)+{\theta}(y-z). |  |

To show ( A.6) for M M: for q ⩽ 1 + y q{\,\leqslant}1+y we have

 |  | max ⁡ ( M ⁡ ( 1 + y − q, y), q, 1, 1 + y − q) \displaystyle\max\big(M(1+y-q,y),q,1,1+y-q\big) |  |

 |  | = max ⁡ ( 1 + θ ​ y, 1 + y − q + θ ⁡ ( 1 + y − 2 ​ ( 1 + y − q)), q, 1, 1 + y − q) \displaystyle=\max\big(1+{\theta}y,1+y-q+{\theta}(1+y-2(1+y-q)),q,1,1+y-q\big) |  |

 |  | = max ⁡ ( 1 + θ ​ y, q + ( 1 − θ) ​ ( 1 + y − 2 ​ q), q, 1 + y − q) \displaystyle=\max\big(1+{\theta}y,q+(1-{\theta})(1+y-2q),q,1+y-q\big) |  |

 |  | ⩾ max ⁡ ( 1 + θ ​ y, q + θ ⁡ ( 1 + y − 2 ​ q), q, 0) = M ⁡ ( q, y). \displaystyle{\,\geqslant}\max\big(1+{\theta}y,q+{\theta}(1+y-2q),q,0\big)=M(q,y). |  |

To show ( A.7) for M M: If q < 1 q<1 then M ⁡ ( q, 0) = max ⁡ ( q, 1, q + θ ⁡ ( 1 − 2 ​ q)) = 1 M(q,0)=\max\big(q,1,q+{\theta}(1-2q)\big)=1, since θ < 1 / 2 {\theta}<1/2. And if q ⩾ 1 q{\,\geqslant}1 then for y ⩽ q − 1 y{\,\leqslant}q-1 we have

 | M ⁡ ( q, y) ⩽ max ⁡ ( q, 1 + θ ⁡ ( q − 1), q + θ ⁡ ( q − 2 ​ q)) = q. \displaystyle M(q,y){\,\leqslant}\max\big(q,1+{\theta}(q-1),q+{\theta}(q-2q)\big)=q. |  |

Thus combining, we conclude M ⁡ ( q, y) ⩽ max ⁡ ( q, 1) M(q,y){\,\leqslant}\max(q,1) for y ⩽ max ⁡ ( 0, q − 1) y{\,\leqslant}\max(0,q-1).

Hence M ⁡ ( q, y) M(q,y) satisfies ( A.5)–( A.7). We similarly check that M ∗ ​ ( q, y) M^{*}(q,y) satisfies ( A.5)–( A.7).

Finally, to show ( A.8) for M ∗ M^{*}: For 0 ⩽ q ⩽ 1 0{\,\leqslant}q{\,\leqslant}1, since θ < 1 / 2 \theta<1/2 we have

 | M ∗ ​ ( q, 1) = max ⁡ ( q, 1, 1, q + 2 ​ θ ​ ( 1 − q)) = max ⁡ ( 1, 2 ​ θ + q ⁡ ( 1 − 2 ​ θ)) = 1, \displaystyle M^{*}(q,1)=\max(q,1,1,q+2\theta(1-q))=\max(1,2\theta+q(1-2\theta))=1, |  |

and for q ⩾ 1 q{\,\geqslant}1, we have

 | M ∗ ​ ( q, q) = max ⁡ ( q, 1, 1 + θ ⁡ ( q − 1), q + θ ⁡ ( 1 − q)) = max ⁡ ( q, 1 + θ ⁡ ( q − 1)) = q. \displaystyle M^{*}(q,q)=\max(q,1,1+\theta(q-1),q+\theta(1-q))=\max(q,1+\theta(q-1))=q. |  |

Combining gives M ⁡ ( q, y) ⩽ y M(q,y){\,\leqslant}y for y = max ⁡ ( q, 1) y=\max(q,1), showing ( A.8).

### A.2. Region where the optimal bound holds

Define the region

 | K = { ( q, y) ∈ ℝ + 2: E ⁡ ( q, y) ⩽ max ⁡ ( q, 1) }. K=\{(q,y)\in{\mathbb{R}}_{+}^{2}\,:\,E(q,y){\,\leqslant}\max(q,1)\}. |  |

We shall identify certain geometric structures inside K K, which will guide our proofs.

First note if ( q, y) ∈ K (q,y)\in K, then ( q, y ′) ∈ K (q,y^{\prime})\in K for all 0 ≤ y ′ ≤ y 0\leq y^{\prime}\leq y. By ( A.7) we know that K K contains the line { ( 1 + λ, λ): λ ≥ 0 } \{(1+\lambda,\lambda)\,:\,\lambda\geq 0\} and the segment { ( λ, 0): 0 ≤ λ ≤ 1 } \{(\lambda,0)\,:\,0\leq\lambda\leq 1\}. Also ( A.8) implies K K contains the line { ( q, q): q ≥ 1 } \{(q,q)\,:\,q\geq 1\}.

In the following lemma, we show each point ( q, y) ∈ K (q,y)\in K induces another point in K K.

###### Lemma A.3.

Let y, q y,q be such that q ≥ 1 q\geq 1 and y ≤ 2 ​ q − 1 y\leq 2q-1, and assume ( q, y) ∈ K (q,y)\in K. Then ( q ′, y ′) ∈ K (q^{\prime},y^{\prime})\in K, where

 | q ′ = \displaystyle q^{\prime}={} | ( 1 + θ) ​ q − θ ⁡ ( 1 + y) 1 − θ \displaystyle\frac{(1+{\theta})q-{\theta}(1+y)}{1-{\theta}} |  |

 | y ′ = \displaystyle y^{\prime}={} | q − 1 + q ′. \displaystyle q-1+q^{\prime}. |  |

###### Proof.

Note 0 ⩽ θ < 1 / 2 0{\,\leqslant}{\theta}<1/2 and the hypothesis y + 1 ≤ 2 ​ q y+1\leq 2q imply

 | q ′ ⩾ ( 1 + θ) ​ q − 2 ​ θ ​ q 1 − θ = q \displaystyle q^{\prime}{\,\geqslant}\frac{(1+{\theta})q-2{\theta}q}{1-{\theta}}=q |  |

which in turn gives y ′ ⩾ 2 ​ q − 1 ⩾ y y^{\prime}{\,\geqslant}2q-1{\,\geqslant}y. So combining with ( A.6) and ( A.5), we have

 | E ⁡ ( q ′, y ′) ≤ \displaystyle E(q^{\prime},y^{\prime})\leq{} | max ⁡ ( E ⁡ ( 1 + y ′ − q ′, y ′), q ′, 1 + y ′ − q ′) \displaystyle\max(E(1+y^{\prime}-q^{\prime},y^{\prime}),q^{\prime},1+y^{\prime}-q^{\prime}) |  |

 | = \displaystyle={} | max ⁡ ( E ⁡ ( q, y ′), q ′, q) = max ⁡ ( E ⁡ ( q, y ′), q ′) \displaystyle\max(E(q,y^{\prime}),q^{\prime},q)=\max(E(q,y^{\prime}),q^{\prime}) |  |

 | ≤ \displaystyle\leq{} | max ⁡ ( E ⁡ ( q, y) + θ ⁡ ( y ′ − y), q ′) \displaystyle\max(E(q,y)+{\theta}(y^{\prime}-y),q^{\prime}) |  |

 | ≤ \displaystyle\leq{} | max ⁡ ( q + θ ⁡ ( y ′ − y), q ′). \displaystyle\max(q+{\theta}(y^{\prime}-y),q^{\prime}). |  |

Here E ⁡ ( q, y) ⩽ max ⁡ ( q, 1) = q E(q,y){\,\leqslant}\max(q,1)=q since ( q, y) ∈ K (q,y)\in K. Finally, by definition of q ′ q^{\prime} we have

 | q ′ = θ ​ q ′ + ( 1 + θ) ​ q − θ ⁡ ( 1 + y) = q + θ ⁡ ( q − 1 + q ′ − y) = q + θ ⁡ ( y ′ − y). \displaystyle q^{\prime}={\theta}q^{\prime}+(1+{\theta})q-{\theta}(1+y)=q+{\theta}(q-1+q^{\prime}-y)=q+{\theta}(y^{\prime}-y). |  |

Thus E ⁡ ( q ′, y ′) ⩽ max ⁡ ( q ′, q ′) = max ⁡ ( q ′, 1) E(q^{\prime},y^{\prime}){\,\leqslant}\max(q^{\prime},q^{\prime})=\max(q^{\prime},1) and hence ( q ′, y ′) ∈ K (q^{\prime},y^{\prime})\in K. ∎

###### Lemma A.4.

We have { ( 1 + λ, λ / θ): 0 ≤ λ ≤ θ 1 − θ } ⊂ K \{(1+\lambda,\lambda/{\theta})\,:\,0\leq\lambda\leq\frac{{\theta}}{1-{\theta}}\}\subset K.

###### Proof.

Let λ ∈ [0, θ 1 − θ] \lambda\in[0,\frac{{\theta}}{1-{\theta}}]. By ( A.6) we have

 | E ⁡ ( 1 + λ, λ / θ) ≤ max ⁡ ( E ⁡ ( λ / θ − λ, λ / θ), 1 + λ, λ / θ − λ). \displaystyle E(1+\lambda,\lambda/{\theta})\leq\max(E(\lambda/{\theta}-\lambda,\lambda/{\theta}),1+\lambda,\lambda/{\theta}-\lambda). |  |

By assumption on λ \lambda, we have λ / θ − λ ≤ 1 \lambda/{\theta}-\lambda\leq 1, and so ( A.5) and ( A.7) gives

 | E ⁡ ( 1 + λ, λ / θ) ≤ \displaystyle E(1+\lambda,\lambda/{\theta})\leq{} | max ⁡ ( E ⁡ ( λ / θ − λ, λ / θ), 1 + λ) \displaystyle\max(E(\lambda/{\theta}-\lambda,\lambda/{\theta}),1+\lambda) |  |

 | ≤ \displaystyle\leq{} | max ⁡ ( E ⁡ ( λ / θ − λ, 0) + λ, 1 + λ) \displaystyle\max(E(\lambda/{\theta}-\lambda,0)+\lambda,1+\lambda) |  |

 | ≤ \displaystyle\leq{} | max ⁡ ( max ⁡ ( λ / θ − λ, 1) + λ, 1 + λ) \displaystyle\max(\max(\lambda/{\theta}-\lambda,1)+\lambda,1+\lambda) |  |

 | = \displaystyle={} | 1 + λ. \displaystyle 1+\lambda. |  |

This shows that ( 1 + λ, λ / θ) ∈ K (1+\lambda,\lambda/{\theta})\in K. ∎

###### Proof of Proposition A.2.

Define a sequence ( α n) n ≥ 0 (\alpha_{n})_{n\geq 0} by α 0:= 1 \alpha_{0}:=1 and

 | α n + 1 = 2 − θ ​ α n 1 − θ ⁡ ( α n − 1). \alpha_{n+1}=\frac{2-{\theta}\alpha_{n}}{1-{\theta}(\alpha_{n}-1)}. |  |

We claim

(A.9) |  | lim n → ∞ α n = 2. \displaystyle\lim_{n\to\infty}\alpha_{n}=2. |  |

To prove this, first observe the sequence ( α n) (\alpha_{n}) is the orbit a Möbius transformation,

 | α n = g n ⋅ 1, for g:= ( − θ 2 − θ 1 + θ). \displaystyle\alpha_{n}=g^{n}\cdot 1,\qquad\qquad\text{for}\quad g:=\matrixquantity(\lx@physics@matrix-{\theta} & 2 \\ -{\theta} & 1+{\theta}\endlx@physics@matrix). |  |

Since θ < 1 / 2 {\theta}<1/2, the matrix g = ( − θ 2 − θ 1 + θ) g=\smallmatrixquantity(\lx@physics@smallmatrix-{\theta} & 2 \\ -{\theta} & 1+{\theta}\endlx@physics@smallmatrix) has distinct eigenvalues θ {\theta} and 1 − θ 1-{\theta}, with corresponding eigenvectors v 1 = ( 2, 1) v_{1}=(2;1) and v 2 = ( 1 / θ, 1) v_{2}=(1/{\theta};1): Indeed, we have

 | g ​ v 1 \displaystyle gv_{1} | = ( − θ 2 − θ 1 + θ) ​ ( 2 1) = ( 2 − 2 ​ θ 1 − θ) = ( 1 − θ) ​ v 1, \displaystyle=\matrixquantity(\lx@physics@matrix-{\theta} & 2 \\ -{\theta} & 1+{\theta}\endlx@physics@matrix)\matrixquantity(\lx@physics@matrix 2\\1\endlx@physics@matrix)=\matrixquantity(\lx@physics@matrix 2-2{\theta}\\1-{\theta}\endlx@physics@matrix)=(1-{\theta})v_{1}, |  |

 | g ​ v 2 \displaystyle gv_{2} | = ( − θ 2 − θ 1 + θ) ​ ( 1 / θ 1) = ( 1 θ) = θ ​ v 2. \displaystyle=\matrixquantity(\lx@physics@matrix-{\theta} & 2 \\ -{\theta} & 1+{\theta}\endlx@physics@matrix)\matrixquantity(\lx@physics@matrix 1/{\theta}\\1\endlx@physics@matrix)=\matrixquantity(\lx@physics@matrix 1\\{\theta}\endlx@physics@matrix)={\theta}v_{2}. |  |

Then decomposing ( 1; 1) = c ​ v 1 + ( 1 − c) ​ v 2 (1;1)=cv_{1}+(1-c)v_{2} for c = 1 − θ 1 − 2 ​ θ > 0 c=\frac{1-{\theta}}{1-2{\theta}}>0, we see

 | g n ​ ( 1 1) \displaystyle g^{n}\matrixquantity(\lx@physics@matrix 1\\1\endlx@physics@matrix) | = c ​ g n ​ v 1 + ( 1 − c) ​ g n ​ v 2 \displaystyle=cg^{n}v_{1}+(1-c)g^{n}v_{2} |  |

 |  | = c ​ ( 1 − θ) n ​ ( 2 1) + ( 1 − c) ​ θ n ​ ( 1 / θ 1) = ( 2 ​ c ​ ( 1 − θ) n + O ⁡ ( θ n) c ​ ( 1 − θ) n + O ⁡ ( θ n)). \displaystyle=c(1-{\theta})^{n}\matrixquantity(\lx@physics@matrix 2\\1\endlx@physics@matrix)+(1-c){\theta}^{n}\matrixquantity(\lx@physics@matrix 1/{\theta}\\1\endlx@physics@matrix)=\matrixquantity(\lx@physics@matrix 2c(1-{\theta})^n+O({\theta}^n)\\c(1-{\theta})^n+O({\theta}^n)\endlx@physics@matrix). |  |

Hence we deduce α n = g n ⋅ 1 = 2 + O ​ ( θ 1 − θ) n \alpha_{n}=g^{n}\cdot 1=2+O(\tfrac{{\theta}}{1-{\theta}})^{n}. In particular ( A.9) follows, since θ < 1 / 2 {\theta}<1/2.

We claim that K K contains the line { ( 1 + λ, 1 + α n ​ λ): λ ≥ 0 } \{(1+\lambda,1+\alpha_{n}\lambda)\,:\,\lambda\geq 0\} for each n ≥ 0 n\geq 0. This is proved by induction. For n = 0 n=0, this follows from ( A.8). Suppose it is proven for some n ≥ 0 n\geq 0, and let λ ≥ 0 \lambda\geq 0. By assumption the point ( q, y) = ( 1 + λ, 1 + α n ​ λ) (q,y)=(1+\lambda,1+\alpha_{n}\lambda) belongs to K K. By Lemma A.3, we deduce that K K contains the point ( q ′, y ′) (q^{\prime},y^{\prime}), where

 | q ′ = ( 1 + θ) ​ ( 1 + λ) − θ ⁡ ( 2 + α n ​ λ) 1 − θ. q^{\prime}=\frac{(1+{\theta})(1+\lambda)-{\theta}(2+\alpha_{n}\lambda)}{1-{\theta}}. |  |

We compute

 | q ′ = 1 + 1 − θ ⁡ ( α n − 1) 1 − θ ​ λ, y ′ = q + q ′ − 1 = 1 + λ ​ 2 − θ ​ α n 1 − θ. q^{\prime}=1+\frac{1-{\theta}(\alpha_{n}-1)}{1-{\theta}}\lambda,\qquad y^{\prime}=q+q^{\prime}-1=1+\lambda\frac{2-{\theta}\alpha_{n}}{1-{\theta}}. |  |

Letting λ ≥ 0 \lambda\geq 0 vary, we see K K contains a line passing through ( 1, 1) (1,1) of slope y ′ − 1 q ′ − 1 = 2 − θ ​ α n 1 − θ ⁡ ( α n − 1) = α n + 1 \frac{y^{\prime}-1}{q^{\prime}-1}=\frac{2-{\theta}\alpha_{n}}{1-{\theta}(\alpha_{n}-1)}=\alpha_{n+1}. This completes the induction.

Given q ≥ 1 q\geq 1, by definition of K K we have E ⁡ ( q, 1 + α n ​ ( q − 1)) ≤ q E(q,1+\alpha_{n}(q-1))\leq q for each n n. Note E ⁡ ( q, y) E(q,y) is continuous in y y by ( A.5). Thus α n → 2 \alpha_{n}\to 2 as n → ∞ n\to\infty, by ( A.9), gives

(A.10) |  |  | E ⁡ ( q, 2 ​ q − 1) ≤ q, \displaystyle E(q,2q-1)\leq q, | for ​ q ≥ 1. \displaystyle\qquad\text{for }\ q\geq 1. |  |

Let now q, y ≥ 0 q,y\geq 0 be arbitrary.

Assume first q ≤ 1 q\leq 1. If y ≤ 1 y\leq 1, then by ( A.8) we have E ⁡ ( q, y) ≤ E ⁡ ( q, 1) = 1 = M ∗ ​ ( q, y) E(q,y)\leq E(q,1)=1=M^{*}(q,y). If y ≥ 1 y\geq 1, then by ( A.5) we have E ⁡ ( q, y) ≤ E ⁡ ( q, 1) + θ ⁡ ( y − 1) = 1 + θ ⁡ ( y − 1) = M ∗ ​ ( q, y) E(q,y)\leq E(q,1)+{\theta}(y-1)=1+{\theta}(y-1)=M^{*}(q,y).

Assume next that q ≥ 1 q\geq 1. If y ≤ 2 ​ q − 1 y\leq 2q-1, then by ( A.10) we have E ⁡ ( q, y) ≤ E ⁡ ( q, 2 ​ q − 1) = q = M ∗ ​ ( q, y) E(q,y)\leq E(q,2q-1)=q=M^{*}(q,y). If y ≥ 2 ​ q − 1 y\geq 2q-1, then by ( A.5) we have E ⁡ ( q, y) ≤ E ⁡ ( q, 2 ​ q − 1) + θ ⁡ ( y − 2 ​ q + 1) = q + θ ⁡ ( y − 2 ​ q + 1) = M ∗ ​ ( q, y) E(q,y)\leq E(q,2q-1)+{\theta}(y-2q+1)=q+{\theta}(y-2q+1)=M^{*}(q,y). Thus in all cases we have E ⁡ ( q, y) ≤ M ∗ ​ ( q, y) E(q,y)\leq M^{*}(q,y). ∎

Moving on to the proof of Proposition A.1, we first develop intuition in the case θ = 1 / 2 {\theta}=1/2.

###### Lemma A.5.

For θ = 1 / 2 \theta=1/2, we have ( q, 2 ​ q − 2) ∈ K (q,2q-2)\in K for all q ≥ 1 q\geq 1.

###### Proof.

Denote D n = { ( 1 + λ, 2 ​ λ): n ≤ λ ≤ n + 1 } D_{n}=\{(1+\lambda,2\lambda)\,:\,n\leq\lambda\leq n+1\}. We will show by induction that D n ⊂ K D_{n}\subset K for all n ≥ 0 n\geq 0. By Lemma A.4, we have D 0 ⊂ K D_{0}\subset K. Suppose D n ∈ K D_{n}\in K for some n n, and let λ ∈ [n, n + 1] \lambda\in[n,n+1]. By Lemma A.3, since ( 1 + λ, 2 ​ λ) ∈ K (1+\lambda,2\lambda)\in K, we deduce that ( q ′, λ + q ′) ∈ K (q^{\prime},\lambda+q^{\prime})\in K, where for θ = 1 / 2 {\theta}=1/2,

 | q ′ = ( 1 + θ) ​ ( 1 + λ) − θ ⁡ ( 1 + 2 ​ λ) 1 − θ = λ + 2. q^{\prime}=\frac{(1+{\theta})(1+\lambda)-{\theta}(1+2\lambda)}{1-{\theta}}=\lambda+2. |  |

Therefore { ( 2 + λ, 2 + 2 ​ λ): n ≤ λ ≤ n + 1 } = D n + 1 ⊂ K \{(2+\lambda,2+2\lambda)\,:\,n\leq\lambda\leq n+1\}=D_{n+1}\subset K, which completes the induction. ∎

This implies E ⁡ ( q, 2 ​ q − 2) ≤ q E(q,2q-2)\leq q for q ⩾ 1 q{\,\geqslant}1 and better motivates the choice y = 2 ​ q − 2 y=2q-2 in [9], when θ = 1 / 2 \theta=1/2. With Lemma A.5 in mind, we similarly consider θ < 1 / 2 \theta<1/2.

###### Lemma A.6.

For θ < 1 / 2 \theta<1/2, we have ( q, ( q − 1) / θ) ∈ K (q,(q-1)/{\theta})\in K for 1 ≤ q < 1 − θ 1 − 2 ​ θ 1\leq q<\frac{1-{\theta}}{1-2{\theta}}.

###### Proof.

Consider λ ∈ [0, θ 1 − θ] \lambda\in[0,\frac{{\theta}}{1-{\theta}}]. We have ( 1 + λ, λ / θ) ∈ K (1+\lambda,\lambda/{\theta})\in K by Lemma A.4. Thus by Lemma A.3, we deduce ( q 1, λ + q 1) ∈ K (q_{1},\lambda+q_{1})\in K as well, where

 | q 1 = ( 1 + θ) ​ ( 1 + λ) − θ ⁡ ( 1 + λ / θ) 1 − θ. q_{1}=\frac{(1+{\theta})(1+\lambda)-{\theta}(1+\lambda/{\theta})}{1-{\theta}}. |  |

Letting λ 1:= q 1 − 1 = θ 1 − θ ​ ( 1 + λ) \lambda_{1}:=q_{1}-1=\frac{{\theta}}{1-{\theta}}(1+\lambda), we have ( 1 + λ 1, λ 1 / θ) = ( q 1, λ + q 1) ∈ K (1+\lambda_{1},\lambda_{1}/{\theta})=(q_{1},\lambda+q_{1})\in K, since

 | λ + q 1 = λ + 1 + λ 1 = ( λ + 1) ​ ( 1 + θ 1 − θ) = λ + 1 1 − θ = λ 1 θ. \displaystyle\lambda+q_{1}=\lambda+1+\lambda_{1}=(\lambda+1)(1+\tfrac{{\theta}}{1-{\theta}})=\frac{\lambda+1}{1-{\theta}}=\frac{\lambda_{1}}{{\theta}}. |  |

Let ρ:= θ 1 − θ \rho:=\frac{{\theta}}{1-{\theta}} so λ 1 = ρ ⁡ ( 1 + λ) \lambda_{1}=\rho(1+\lambda). As λ \lambda varies in [0, ρ] [0,\rho], we see λ 1 \lambda_{1} varies in [ρ, ρ + ρ 2] [\rho,\rho+\rho^{2}], and hence ( 1 + λ, λ / θ) ∈ K (1+\lambda,\lambda/{\theta})\in K for all 0 ≤ λ ≤ ρ + ρ 2 0\leq\lambda\leq\rho+\rho^{2}. An immediate induction shows that in fact ( 1 + λ, λ / θ) ∈ K (1+\lambda,\lambda/{\theta})\in K whenever 0 ≤ λ ≤ ρ + ⋯ + ρ n 0\leq\lambda\leq\rho+\cdots+\rho^{n} for any n ≥ 1 n\geq 1. Since ∑ n ≥ 1 ρ n = θ 1 − 2 ​ θ \sum_{n\geq 1}\rho^{n}=\frac{{\theta}}{1-2{\theta}}, we deduce that ( 1 + λ, λ / θ) ∈ K (1+\lambda,\lambda/{\theta})\in K for all 0 ≤ λ < θ 1 − 2 ​ θ 0\leq\lambda<\frac{{\theta}}{1-2{\theta}}, that is, 1 ⩽ q = 1 + λ < 1 − θ 1 − 2 ​ θ 1{\,\leqslant}q=1+\lambda<\frac{1-{\theta}}{1-2{\theta}}. ∎

###### Lemma A.7.

We have ( q, 2 ​ q − 1) ∈ K (q,2q-1)\in K for all q ≥ 1 − θ 1 − 2 ​ θ q\geq\frac{1-{\theta}}{1-2{\theta}}.

###### Proof.

Define the sequences

 | λ 0 \displaystyle\lambda_{0} | : = 0, λ n + 1 = θ 1 − θ ​ ( 1 + λ n), \displaystyle:=0,\qquad\lambda_{n+1}=\frac{{\theta}}{1-{\theta}}(1+\lambda_{n}), |  |

 | α 0 \displaystyle\alpha_{0} | : = 1, α n + 1 = 2 − θ ​ α n 1 − θ ⁡ ( α n − 1). \displaystyle:=1,\qquad\alpha_{n+1}=\frac{2-{\theta}\alpha_{n}}{1-{\theta}(\alpha_{n}-1)}. |  |

Recall from ( A.9) that α n → 2 \alpha_{n}\to 2 as n → ∞ n\to\infty. Also the sequence ( λ n) (\lambda_{n}) is increasing and converges to θ 1 − 2 ​ θ \frac{{\theta}}{1-2{\theta}}. We prove by induction that for all n ≥ 0 n\geq 0, K K contains the line

(A.11) |  | { ( 1 + λ n + μ, λ n / θ + μ ​ α n): μ ≥ 0 } ⊂ K. \displaystyle\{(1+\lambda_{n}+\mu,\,\lambda_{n}/{\theta}+\mu\alpha_{n})\,:\,\mu\geq 0\}\ \subset\ K. |  |

Indeed, for the base case n = 0 n=0, we have ( 1 + μ, μ) ∈ K (1+\mu,\mu)\in K for all μ ⩾ 0 \mu{\,\geqslant}0. Then assuming ( 1 + λ n + μ, 1 θ ​ λ n + α n ​ μ) ∈ K (1+\lambda_{n}+\mu,\tfrac{1}{\theta}\lambda_{n}+\alpha_{n}\mu)\in K, by Lemma A.3 we have ( q ′, q ′ + λ n + μ) ∈ K (q^{\prime},q^{\prime}+\lambda_{n}+\mu)\in K, where q ′ q^{\prime} is

 | q ′ \displaystyle q^{\prime} | = 1 + θ 1 − θ ​ ( 1 + λ n + μ) − θ 1 − θ ​ ( 1 + 1 θ ​ λ n + α n ​ μ) = 1 + θ ​ λ n 1 − θ + 1 + θ − θ ​ α n 1 − θ ​ μ. \displaystyle=\tfrac{1+{\theta}}{1-{\theta}}(1+\lambda_{n}+\mu)-\tfrac{{\theta}}{1-{\theta}}(1+\tfrac{1}{\theta}\lambda_{n}+\alpha_{n}\mu)=\frac{1+{\theta}\lambda_{n}}{1-{\theta}}+\frac{1+{\theta}-{\theta}\alpha_{n}}{1-{\theta}}\mu. |  |

Noting 1 + θ ​ λ n 1 − θ = 1 + θ 1 − θ ​ ( 1 + λ n) = 1 + λ n + 1 \frac{1+{\theta}\lambda_{n}}{1-{\theta}}=1+\tfrac{{\theta}}{1-{\theta}}(1+\lambda_{n})=1+\lambda_{n+1}, we let μ ′ = 1 + θ − θ ​ α n 1 − θ ​ μ \mu^{\prime}=\frac{1+{\theta}-{\theta}\alpha_{n}}{1-{\theta}}\mu so that

 | K ∋ ( q ′, q ′ + λ n + μ) \displaystyle K\ni(q^{\prime},q^{\prime}+\lambda_{n}+\mu) | = ( 1 + λ n + 1 + 1 + θ − θ ​ α n 1 − θ ​ μ, 1 + λ n 1 − θ + 2 − θ ​ α n 1 − θ ​ μ) \displaystyle=\bigg(1+\lambda_{n+1}+\frac{1+{\theta}-{\theta}\alpha_{n}}{1-{\theta}}\mu,\,\frac{1+\lambda_{n}}{1-{\theta}}+\frac{2-{\theta}\alpha_{n}}{1-{\theta}}\mu\bigg) |  |

 |  | = ( 1 + λ n + 1 + μ ′, λ n + 1 θ + α n + 1 ​ μ ′). \displaystyle=\bigg(1+\lambda_{n+1}+\mu^{\prime},\,\frac{\lambda_{n+1}}{{\theta}}+\alpha_{n+1}\mu^{\prime}\bigg). |  |

This completes the induction, and hence ( A.11) follows.

Given q > 1 − θ 1 − 2 ​ θ q>\frac{1-{\theta}}{1-2{\theta}} and n ≥ 0 n\geq 0, we have q − 1 > θ 1 − 2 ​ θ q-1>\frac{{\theta}}{1-2{\theta}}, and we let μ:= q − 1 − λ n > 0 \mu:=q-1-\lambda_{n}>0. Since ( 1 + λ n + μ, λ n / θ + α n ​ μ) ∈ K (1+\lambda_{n}+\mu,\lambda_{n}/{\theta}+\alpha_{n}\mu)\in K, we deduce that

 | E ⁡ ( q, y n) ≤ q E(q,y_{n})\leq q |  |

for y n = λ n / θ + α n ​ μ y_{n}=\lambda_{n}/{\theta}+\alpha_{n}\mu. Since α n → 2 \alpha_{n}\to 2 and λ n → θ 1 − 2 ​ θ \lambda_{n}\to\frac{{\theta}}{1-2{\theta}} we obtain

 | y n = λ n θ + α n ​ ( q − 1 − λ n) → 1 1 − 2 ​ θ + 2 ​ ( q − 1 − θ 1 − 2 ​ θ) = 1 − 2 ​ θ 1 − 2 ​ θ + 2 ​ ( q − 1) = 2 ​ q − 1. \displaystyle y_{n}=\frac{\lambda_{n}}{{\theta}}+\alpha_{n}(q-1-\lambda_{n})\ \to\ \tfrac{1}{1-2{\theta}}+2(q-1-\tfrac{{\theta}}{1-2{\theta}})=\tfrac{1-2{\theta}}{1-2{\theta}}+2(q-1)=2q-1. |  |

By ( A.5), the map y ↦ E ⁡ ( q, y) y\mapsto E(q,y) is continuous. So taking the limit as n → ∞ n\to\infty we see E ⁡ ( q, y n) ≤ q E(q,y_{n})\leq q implies E ⁡ ( q, 2 ​ q − 1) ≤ q E(q,2q-1)\leq q. Hence ( q, 2 ​ q − 1) ∈ K (q,2q-1)\in K as claimed. ∎

###### Proof of Proposition A.1.

Assume first that q ≤ 1 q\leq 1. Then we have E ⁡ ( q, y) ≤ θ ​ y + E ⁡ ( q, 0) = 1 + θ ​ y = M ⁡ ( q, y) E(q,y)\leq{\theta}y+E(q,0)=1+{\theta}y=M(q,y). Assume next that 1 ≤ q ≤ 1 − θ 1 − 2 ​ θ 1\leq q\leq\frac{1-{\theta}}{1-2{\theta}}. Then we have E ⁡ ( q, ( q − 1) / θ) ≤ q E(q,(q-1)/{\theta})\leq q by Lemma A.6. If y ≤ ( q − 1) / θ y\leq(q-1)/{\theta}, this implies E ⁡ ( q, y) ≤ E ⁡ ( q, ( q − 1) / θ) ≤ q E(q,y)\leq E(q,(q-1)/{\theta})\leq q, and if y ≥ ( q − 1) / θ y\geq(q-1)/{\theta}, this implies E ⁡ ( q, y) ≤ θ ⁡ ( y − ( q − 1) / θ) + E ⁡ ( q, ( q − 1) / θ) ≤ 1 + θ ​ y E(q,y)\leq{\theta}(y-(q-1)/{\theta})+E(q,(q-1)/{\theta})\leq 1+{\theta}y. In both cases we find E ⁡ ( q, y) ≤ M ⁡ ( q, y) E(q,y)\leq M(q,y). Finally, if q ≥ 1 − θ 1 − 2 ​ θ q\geq\frac{1-{\theta}}{1-2{\theta}}, we have by Lemma A.7 that E ⁡ ( q, 2 ​ q − 1) ≤ q E(q,2q-1)\leq q, and by an argument similar to the proof of Proposition A.2, we obtain E ⁡ ( q, y) ≤ q + max ⁡ ( 0, θ ⁡ ( y − 2 ​ q + 1)) = M ⁡ ( q, y) E(q,y)\leq q+\max(0,{\theta}(y-2q+1))=M(q,y). In all cases, we get E ⁡ ( q, y) ≤ M ⁡ ( q, y) E(q,y)\leq M(q,y) as claimed. ∎

## References

- [1] E. Assing, V. Blomer, J. Li, Uniform Titchmarsh divisor problems, Adv. Math. 393 (2021), 108076.
- [2] V. Blomer, G. Harcos, P. Michel, A Burgess-like subconvex bound for twisted L L -functions, Forum Math. 19 (2007), 61–105, Appendix 2 by Z. Mao.
- [3] E. Bombieri, H. Davenport, Small differences between prime numbers, Proc. Roy. Soc. Ser. A 239 (1966), 1–18.
- [4] E. Bombieri, J. Friedlander, H. Iwaniec, Primes in arithmetic progressions to large moduli, Acta Math. 156 (1986), 203–251.
- [5] E. Bombieri, J. Friedlander, H. Iwaniec, Primes in arithmetic progressions to large moduli. II, Math. Ann. 277 (1987), 361–393,
- [6] Y.C. Cai, M.G. Lu, On the upper bound for π 2 \pi_{2} (x), Acta Arith. 110 (2003), 275–298.
- [7] J.R. Chen, On the representation of a larger even integer as the sum of a prime and the product of at most two primes, Sci. Sinica 16 (1973), 157–176.
- [8] J.R. Chen, On the Goldbach’s problem and the sieve methods, Sci. Sinica 21 (1978), 701–739.
- [9] J.-M. Deshouillers, H. Iwaniec, Kloosterman sums and Fourier coefficients of cusp forms, Invent. Math. 70 (1982), 219–288.
- [10] S. Drappeau. Théorèmes de type Fouvry–Iwaniec pour les entiers friables. Compos. Math. 151 (2015), 828–862.
- [11] S. Drappeau, Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method, Proc. Lond. Math. Soc. 114 (2017), 684–732.
- [12] S. Drappeau, K. Pratt and M. Radziwiłł, One-level density estimates for Dirichlet L-functions with extended support, 17 (2023), 805–830.
- [13] P. D. T. A. Elliott, H. Halberstam, A conjecture in prime number theory, Symposia Mathematica, Vol. IV, Academic Press, London, (1970), 59–72.
- [14] É. Fouvry, Autour du théorème de Bombieri–Vinogradov, Acta Math. 152 (1984), 219–244.
- [15] É. Fouvry, H. Iwaniec. Primes in arithmetic progressions, Acta Arith., 42 (1983), 197–218
- [16] É. Fouvry, F. Grupp, On the switching principle in sieve theory, J. reine angew. Math. 370 (1986), 101–125.
- [17] É. Fouvry, G. Tenenbaum, Répartition statistique des entiers sans grand facteur premier dans les progressions arithmétiques, Proc. London Math. Soc. 72 (1996), 481–514.
- [18] J. Friedlander, H. Iwaniec, Opera de Cribro Amer. Math. Soc. Colloquium Publications, 57 (2010).
- [19] H. H. Kim, Functoriality for the exterior square of G ​ L 4 GL_{4} and the symmetric fourth of G ​ L 2 GL_{2}, J. Amer. Math. Soc. 16 (2003), 139–183, With appendix 1 by D. Ramakrishnan and appendix 2 by H. H. Kim and P. Sarnak.
- [20] C. D. Pan, A new application of the Yu. V. Linnik large sieve method, Chinese Math. Acta 5 (1964), 642–652.
- [21] G. H. Hardy, J. E. Littlewood, Some Problems of ‘Partitio Numerorum.’ III. On the Expression of a Number as a Sum of Primes, Acta Math. 44 (1923), 1–70.
- [22] D. R. Heath-Brown. Prime numbers in short intervals and a generalized Vaughan identity, Canadian J. Math., 34 (1982), 1365–1377.
- [23] H. Iwaniec. A new form of the error term in the linear sieve, Acta Arith., 37 (1980), 307–320.
- [24] H. Iwaniec, E. Kowalski. Analytic number theory, Amer. Math. Soc. Colloquium Publications, 53 (2004).
- [25] J. D. Lichtman, A modification of the linear sieve, and the count of twin primes, submitted.
- [26] J. D. Lichtman, Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors, submitted.
- [27] J. Maynard, Primes in arithmetic progressions to large moduli I: Fixed residue classes, Mem. Amer. Math. Soc., to appear.
- [28] J. Maynard, Primes in arithmetic progressions to large moduli II: well-factorable estimates, Mem. Amer. Math. Soc., to appear.
- [29] J. Maynard, Primes in arithmetic progressions to large moduli II: Uniform residue classes, Mem. Amer. Math. Soc., to appear.
- [30] H. Riesel, R.C. Vaughan, On sums of primes, Ark. Mat. 21 (1983), 45–74.
- [31] Z. Rudnick, P. Sarnak, Zeros of principal L-functions and random matrix theory, Duke Math J. 82 (1996), 269–322.
- [32] A. Selberg, On elementary methods in prime number theory and their limitations, in: 11 Skand. Mat. kongr., Trondheim 1949, 13–22.
- [33] P. Shiu, A Brun–Titchmarsh theorem for multiplicative functions, J. Reine Angew. Math. 313 (1980), 161–170.
- [34] H. Siebert, Montgomery’s weighted sieve for dimension two, Monatsh. Math. 82 (1976), 327–336.
- [35] J. Wu, Sur la suite des nombres premiers jumeaux, Acta Arith. 55 (1990), 365–394.
- [36] J. Wu, Chen’s double sieve, Goldbach’s conjecture and the twin prime problem, Acta Arith. 114 (2004), 215–273.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:sary-aurelien.drappeau@univ-amu.fr
[4]: mailto:jared.d.lichtman@gmail.com
