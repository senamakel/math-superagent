<!-- source: https://arxiv.org/html/1501.04585 | converted from HTML -->

Multiplicative functions in short intervals

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1501.04585v4 [math.NT] 15 Oct 2017

# Multiplicative functions in short intervals

Kaisa Matomäki Address: Department of Mathematics and Statistics, University of Turku, 20014 Turku, Finland Email address: [ksmato@utu.fi][3] and Maksym Radziwiłł Address: Department of Mathematics, Rutgers University
Hill Center for the Mathematical Sciences
110 Frelinghuysen Rd., Piscataway, NJ 08854-8019 Email address: [maksym.radziwill@gmail.com][4] Dedicated to Andrew Granville

###### Abstract.

We introduce a general result relating “short averages” of a multiplicative function to “long averages” which are well understood. This result has several consequences. First, for the Möbius function we show that there are cancellations in the sum of μ ⁡ ( n) \mu(n) in almost all intervals of the form [x, x + ψ ⁡ ( x)] [x,x+\psi(x)] with ψ ⁡ ( x) → ∞ \psi(x)\rightarrow\infty arbitrarily slowly. This goes beyond what was previously known conditionally on the Density Hypothesis or the stronger Riemann Hypothesis. Second, we settle the long-standing conjecture on the existence of x ϵ x^{\epsilon} -smooth numbers in intervals of the form [x, x + c ⁡ ( ε) ​ x] [x,x+c(\varepsilon)\sqrt{x}], recovering unconditionally a conditional (on the Riemann Hypothesis) result of Soundararajan. Third, we show that the mean-value of λ ⁡ ( n) ​ λ ​ ( n + 1) \lambda(n)\lambda(n+1), with λ ⁡ ( n) \lambda(n) Liouville’s function, is non-trivially bounded in absolute value by 1 − δ 1-\delta for some δ > 0 \delta>0. This settles an old folklore conjecture and constitutes progress towards Chowla’s conjecture. Fourth, we show that a (general) real-valued multiplicative function f f has a positive proportion of sign changes if and only if f f is negative on at least one integer and non-zero on a positive proportion of the integers. This improves on many previous works, and is new already in the case of the Möbius function. We also obtain some additional results on smooth numbers in almost all intervals, and sign changes of multiplicative functions in all intervals of square-root length.

## 1. Introduction

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. We introduce a general result relating many “short averages” of a multiplicative function over a bounded length interval to “long averages” which are well understood using tools from multiplicative number theory.

###### Theorem 1.

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. There exist absolute constants C, C ′ > 1 C,C^{\prime}>1 such that for any 2 ≤ h ≤ X 2\leq h\leq X and δ > 0 \delta>0,

 | | 1 h ​ ∑ x ≤ n ≤ x + h f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) | ≤ δ + C ′ ​ log ⁡ log ⁡ h log ⁡ h \Bigg|\frac{1}{h}\sum_{x\leq n\leq x+h}f(n)-\frac{1}{X}\sum_{X\leq n\leq 2X}f(n)\Bigg|\leq\delta+C^{\prime}\frac{\log\log h}{\log h} |  |

for all but at most

 | C ​ X ​ ( ( log ⁡ h) 1 / 3 δ 2 ​ h δ / 25 + 1 δ 2 ​ ( log ⁡ X) 1 / 50) CX\Big(\frac{(\log h)^{1/3}}{\delta^{2}h^{\delta/25}}+\frac{1}{\delta^{2}(\log X)^{1/50}}\Big) |  |

integers x ∈ [X, 2 ​ X] x\in[X,2X]. One can take C ′ = 20000 C^{\prime}=20000.

Note that Theorem 1 allows h, δ h,\delta and f f to vary uniformly. For example taking δ = ( log h) − 1 / 200 \delta=(\log h)^{-1/200} gives a saving of 2 ( log h) − 1 / 200 2(\log h)^{-1/200} with an exceptional set of at most C X ( log h) − 1 / 100 CX(\log h)^{-1/100}. Already for the Möbius function μ ⁡ ( n) \mu(n) Theorem 1 goes beyond what was previously known conditionally; The density hypothesis implies that there are cancellations in the sum of μ ⁡ ( n) \mu(n), but “only” in almost all intervals x ≤ n ≤ x + h x\leq n\leq x+h of length h ≥ x ε h\geq x^{\varepsilon} whereas the Riemann hypothesis implies cancellations of μ ⁡ ( n) \mu(n) in almost all intervals but again “only” if h > ( log ⁡ X) A h>(\log X)^{A} for some constant A > 0 A>0 (by unpublished work of Peng Gao). Unconditionally, using results towards the density hypothesis, it was previously known that there are cancellation of μ ⁡ ( n) \mu(n) in almost all intervals of length x 1 / 6 + ε x^{1/6+\varepsilon} (a result due to Ramachandra [34]).

One naturally wonders if it is possible to establish Theorem 1 in all intervals of length h ≍ X h\asymp\sqrt{X}. However, this is not possible in general, since it would require us to control the contribution of the large primes factors which is completely arbitrary for general f f. We prove however a bilinear version of Theorem 1 which holds in all intervals of length ≍ X \asymp\sqrt{X}. The bilinear structure allows us to eliminate the contribution of the large primes.

###### Theorem 2.

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. Then, for any 10 ≤ h ≤ x 10\leq h\leq x,

 | 1 h ​ x ​ log ⁡ 2 ​ ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x f ⁡ ( n 1) ​ f ​ ( n 2) = ( 1 x ​ ∑ x ≤ n ≤ 2 ​ x f ⁡ ( n)) 2 + O ⁡ ( log ⁡ log ⁡ h log ⁡ h + 1 ( log ⁡ x) 1 / 100). \frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\end{subarray}}f(n_{1})f(n_{2})=\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}f(n)\Big)^{2}+O\Big(\frac{\log\log h}{\log h}+\frac{1}{(\log x)^{1/100}}\Big). |  |

An important feature of Theorem 2 is that it holds uniformly in h h and f f. Theorem 2 allows us to show the existence of many X ε X^{\varepsilon} smooth numbers in intervals of length ≍ X \asymp\sqrt{X}. Alternatively we could have deduced this from Theorem 1 using ideas of Croot [4] (building on earlier work of Friedlander and Granville [9]).

###### Corollary 1.

Let ε > 0 \varepsilon>0 be given. There exists a positive constant C ⁡ ( ε) C(\varepsilon) such that the number of X ε X^{\varepsilon} -smooth numbers in [X, X + C ⁡ ( ε) ​ X] [X,X+C(\varepsilon)\sqrt{X}] is at least X ​ ( log ⁡ X) − 4 \sqrt{X}(\log X)^{-4} for all large enough X X.

This recovers unconditionally a conditional (on the Riemann Hypothesis) result of Soundararajan [37] and comes close to settling the long-standing conjecture that every interval [x, x + x] [x,x+\sqrt{x}], with x x large enough, contains x ε x^{\varepsilon} -smooth numbers (see for example [11, Challenge Problem 2000 in Section 4]). The later conjecture is motivated by attempts at rigorously estimating the running time of Lenstra’s elliptic curve factoring algorithm [24, Section 6]. Our result also improves on earlier work of Croot [4], Matomäki [27, 28] and Balog [1]. Finally for small fixed ε \varepsilon, a more difficult to state variant of Theorem 2 (see section 2) shows that C ⁡ ( ε) = ρ ​ ( 1 / ε) − 13 C(\varepsilon)=\rho(1/\varepsilon)^{-13} is admissible, where ρ ⁡ ( u) \rho(u) is the Dickman-de Brujin function. In fact with a little additional work the constant C ⁡ ( ε) C(\varepsilon) can be reduced further to ρ ​ ( 1 / ε) − 7 \rho(1/\varepsilon)^{-7} and the exponent 4 4 in x ​ ( log ⁡ x) − 4 \sqrt{x}(\log x)^{-4} could be refined to log ⁡ 4 \log 4.

Another corollary of Theorem 1 is related to Chowla’s conjecture,

(1) |  | 1 X ​ ∑ n ≤ X λ ⁡ ( n) ​ λ ​ ( n + 1) = o ⁡ ( 1), as ​ x → ∞ \frac{1}{X}\sum_{n\leq X}\lambda(n)\lambda(n+1)=o(1)\ ,\ \text{as }x\rightarrow\infty |  |

with λ ⁡ ( n):= ( − 1) Ω ⁡ ( n) \lambda(n):=(-1)^{\Omega(n)} Liouville’s function. Chowla’s conjecture is believed to be at least as deep as the twin prime conjecture [18]. This motivates the old folklore conjecture according to which the sum ( 1) is, for all X X large enough, bounded in absolute value by ≤ 1 − δ \leq 1-\delta for some δ > 0 \delta>0. For example, Hildebrand writes in [17] “one would naturally expect the above sum to be o ⁡ ( x) o(x) when x → ∞ x\rightarrow\infty, but even the much weaker relation

 | lim inf x → ∞ 1 x ​ ∑ n ≤ x λ ⁡ ( n) ​ λ ​ ( n + 1) < 1 \liminf_{x\rightarrow\infty}\frac{1}{x}\sum_{n\leq x}\lambda(n)\lambda(n+1)<1 |  |

is not known and seems to be beyond reach of the present methods”. Theorem 1 allows us to settle this conjecture in a stronger form.

###### Corollary 2.

For every integer h ≥ 1 h\geq 1, there exists δ ⁡ ( h) > 0 \delta(h)>0 such that

 | 1 X ​ | ∑ n ≤ X λ ⁡ ( n) ​ λ ​ ( n + h) | ≤ 1 − δ ⁡ ( h) \frac{1}{X}\Bigg|\sum_{n\leq X}\lambda(n)\lambda(n+h)\Bigg|\leq 1-\delta(h) |  |

for all large enough X > 1 X>1. In fact the same results holds for any completely multiplicative function f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] such that f ⁡ ( n) < 0 f(n)<0 for some n > 0 n>0.

For h = 1 h=1 Corollary 2 also holds for any multiplicative f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] which is completely multiplicative at the prime 2 2 (this rules out, for example, the f f such that f ⁡ ( 2 k) = − 1 f(2^{k})=-1 and f ⁡ ( p k) = 1 f(p^{k})=1 for all p ≥ 3, k ≥ 1 p\geq 3,k\geq 1). The ternary analogue of Corollary 2 concerning cancellations in the sum of λ ⁡ ( n) ​ λ ​ ( n + 1) ​ λ ​ ( n + 2) \lambda(n)\lambda(n+1)\lambda(n+2) is surprisingly much easier; it is stated as an exercise in Elliott’s book [6, Chapter 33] (see also [5] and [2]).

Corollary 2 is closely related to the problem of counting sign changes of f ⁡ ( n) f(n). Using Halász’s theorem one can show that if ∑ f ⁡ ( p) < 0 1 / p = ∞ \sum_{f(p)<0}1/p=\infty and f ⁡ ( n) ≠ 0 f(n)\neq 0 for a positive proportion of the integers n n then the non-zero values of f ⁡ ( n) f(n) are half of the time positive and half of the time negative (see [30, Lemma 2.4] or [7, Lemma 3.3]). Since we expect f ⁡ ( n) f(n) and f ⁡ ( n + 1) f(n+1) to behave independently this suggests that, for non-vanishing f f such that ∑ f ⁡ ( p) < 0 1 / p = ∞ \sum_{f(p)<0}1/p=\infty, there should be about x / 2 x/2 sign changes among integers n ≤ x n\leq x. When f f is allowed to be zero we say that f f has k k sign changes in [1, x] [1,x] if there are integers 1 ≤ n 1 < n 2 < … < n k + 1 ≤ x 1\leq n_{1}<n_{2}<\ldots<n_{k+1}\leq x such that f ⁡ ( n i) ≠ 0 f(n_{i})\neq 0 for all i i and f ⁡ ( n i), f ⁡ ( n i + 1) f(n_{i}),f(n_{i+1}) are of opposite signs for all i ≤ k i\leq k. For non-lacunary multiplicative f f, i.e multiplicative f f such that f ⁡ ( n) ≠ 0 f(n)\neq 0 on a positive proportion of the integers, we still expect ≍ x \asymp x sign changes in [1, x] [1,x].

###### Corollary 3.

Let f: ℕ → ℝ f:\mathbb{N}\rightarrow\mathbb{R} be a multiplicative function. Then f ⁡ ( n) f(n) has a positive proportion of sign changes if and only if f ⁡ ( n) < 0 f(n)<0 for some integer n > 0 n>0 and f ⁡ ( n) ≠ 0 f(n)\neq 0 for a positive proportion of integers n n.

There is a large literature on sign changes of multiplicative functions. For specific multiplicative functions Corollary 3 improves on earlier results for:

- •

The Möbius function. The previous best result was due to Harman, Pintz and Wolke [15] who obtained more than x / ( log ⁡ x) 7 + ε x/(\log x)^{7+\varepsilon} sign changes for n ≤ x n\leq x, using Jutila’s bounds towards the density hypothesis ( [21]).

- •

Coefficients of L L -functions of high symmetric powers of holomorphic Hecke cusp forms. In this setting the best previous result was x δ x^{\delta} sign changes with some δ < 1 \delta<1 [23].

- •

Fourier coefficients of holomorphic Hecke cusp forms. In this case Corollary 3 recovers a recent result of the authors [30].

As observed by Ghosh and Sarnak in [10], the number of sign changes of λ f ​ ( n) \lambda_{f}(n) for n ≤ k 1 / 2 n\leq k^{1/2} (with k k the weight of f f) is related to the number of zeros of f f on the vertical geodesic high in the cusp. A suitable variation of Corollary 3 (again deduced from Theorem 1) has consequences for this problem. These results are discussed in a paper by the authors and Steve Lester (see [25]).

For general multiplicative functions, Corollary 3 improves on earlier work of Hildebrand [18] and Croot [3]. Croot obtained x ​ exp ⁡ ( − ( log ⁡ x) 1 / 2 + o ⁡ ( 1)) x\exp(-(\log x)^{1/2+o(1)}) sign changes for completely multiplicative non-vanishing functions. Hildebrand showed that there exists an infinite (but quickly growing) subsequence x k x_{k} such that f f has more than x k ​ ( log ⁡ log ⁡ x k) − 4 x_{k}(\log\log x_{k})^{-4} sign changes on the integers n ≤ x k n\leq x_{k}.

Corollary 3 suggests that unless f f is non-negative, there should be few long clusters of consecutive integers at which f f is of the same sign. Our next corollary confirms this expectation.

###### Corollary 4.

Let f: ℕ → ℝ f:\mathbb{N}\rightarrow\mathbb{R} be a multiplicative function. If f ⁡ ( n) < 0 f(n)<0 for some integer n n and f ⁡ ( n) ≠ 0 f(n)\neq 0 for a positive proportion of integers n n, then, for any ψ ⁡ ( x) → ∞ \psi(x)\to\infty, almost every interval [x, x + ψ ⁡ ( x)] [x,x+\psi(x)] contains a sign change of f f.

This is an optimal result, since on probabilistic grounds we expect that for any fixed h > 0 h>0 there is a positive proportion of intervals [x, x + h] [x,x+h] of length h h on which f f is of the same sign. We also have the following analogue of Corollary 4 for all intervals of length ≍ x \asymp\sqrt{x}.

###### Corollary 5.

Let f: ℕ → ℝ f:\mathbb{N}\rightarrow\mathbb{R} be a completely multiplicative function. If f ⁡ ( n) < 0 f(n)<0 for some integer n > 0 n>0 and f ⁡ ( n) ≠ 0 f(n)\neq 0 for a positive proportion of integers n n, then there exists a constant C > 0 C>0 such that f f has a sign change in the interval [x, x + C ​ x] [x,x+C\sqrt{x}] for all large enough x x.

As a consequence of Corollary 5 there exists a constant C > 0 C>0, such that every interval [n, n + C ​ n] [n,n+C\sqrt{n}] has a number with an even number of prime factors, and one with an odd number of prime factors.

Our methods may also be used to demonstrate the existence of smooth numbers in almost all short intervals. It is well-known that the number of X 1 / u X^{1/u} smooth numbers up to X X is asymptotically ρ ⁡ ( u) ​ X \rho(u)X with ρ ⁡ ( u) \rho(u) denoting the Dickman-De Brujin function [38]. We show that this remains true in almost all short intervals, with the interval as short as possible.

###### Corollary 6.

Let ψ ⁡ ( x) → ∞ \psi(x)\rightarrow\infty and let u > 0 u>0 be given. Then, for almost all x x the number of x 1 / u x^{1/u} -smooth integers in [x, x + ψ ⁡ ( x)] [x,x+\psi(x)] is asymptotically ρ ⁡ ( u) ​ ψ ​ ( x) \rho(u)\psi(x).

This improves on earlier work of Matomäki [28] and unpublished work of Hafner [13]. It would be interesting, in view of applications towards the complexity of Lenstra’s elliptic curve factoring algorithm, to extend Corollary 6 to significantly smoother numbers (and one would naturally need somewhat longer intervals [x, x + ψ ⁡ ( x)] [x,x+\psi(x)] with a ψ ⁡ ( x) \psi(x) depending on the smoothness under consideration), even under the assumption of the Riemann Hypothesis.

We end this introduction by discussing extensions and limitations of our main result. Theorem 1 and its variants do not hold for complex valued multiplicative functions as the example f ⁡ ( p) = p i ​ t f(p)=p^{it} shows. However, the result does extend to complex-valued functions which are not n i ​ t n^{it} -pretentious. We carried out this extension in [31] (joint with Terence Tao), where we used this complex variant, together with other ideas, to prove an averaged version of Chowla’s conjecture.

It is also interesting to notice that one cannot hope to establish general results on sign changes of a multiplicative function f: ℕ → ℝ f:\mathbb{N}\rightarrow\mathbb{R} in all short intervals [x, x + y ⁡ ( x)] [x,x+y(x)] with y ⁡ ( x) < exp ⁡ ( ( ( 2 + o ⁡ ( 1)) ​ log ⁡ x ​ log ⁡ log ⁡ x) 1 / 2) y(x)<\exp(((2+o(1))\log x\log\log x)^{1/2}). Indeed in an interval of this length every integer might be divisible by a distinct prime factor. Therefore one can rig the sign of the multiplicative function on those primes so that f ⁡ ( n) f(n) is always positive in [x, x + y ⁡ ( x)] [x,x+y(x)] even though f ⁡ ( n) f(n) has many sign changes in the full interval [x, 2 ​ x] [x,2x].

In forthcoming work, the authors will investigate versions of our results for multiplicative functions vanishing on a positive proportion of the primes. This is naturally related to sieves of small dimensions. In addition we will also look at the related question of what happens when | f ⁡ ( p) | |f(p)| is not bounded by 1 1. In particular we will obtain results for the k k -fold divisor function. In another forthcoming work, related to Theorem 2 and joint with Andrew Granville and Adam Harper, we will try to understand individual averages of a multiplicative function f f in intervals of length x θ x^{\theta} with θ > 1 / 2 \theta>1/2, and with n n restricted to smooth numbers (thus eliminating the contribution of large primes).

## 2. Initial reduction and key ideas

We will deduce Theorem 1 from a variant where n n is restricted to a dense subset 𝒮 X ⊂ [X, 2 ​ X] \mathcal{S}_{X}\subset[X,2X] which contains only those n n which have prime divisors from certain convenient ranges. To define the set 𝒮 \mathcal{S} we need to introduce some notation. Let η ∈ ( 0, 1 / 6) \eta\in(0,1/6). Consider a sequence of increasing intervals [P j, Q j] [P_{j},Q_{j}] such that

- •

Q 1 ≤ exp ⁡ ( log ⁡ X) Q_{1}\leq\exp(\sqrt{\log X}).

- •

The intervals are not too far from each other, precisely

(2) |  | log ⁡ log ⁡ Q j log ⁡ P j − 1 − 1 ≤ η 4 ​ j 2. \frac{\log\log Q_{j}}{\log P_{j-1}-1}\leq\frac{\eta}{4j^{2}}. |  |

- •

The intervals are not too close to each other, precisely

(3) |  | η j 2 ​ log ⁡ P j ≥ 8 ​ log ⁡ Q j − 1 + 16 ​ log ⁡ j \frac{\eta}{j^{2}}\log P_{j}\geq 8\log Q_{j-1}+16\log j |  |

For example, given 0 < η < 1 / 6 0<\eta<1/6 choose any [P 1, Q 1] [P_{1},Q_{1}] with exp ⁡ ( log ⁡ X) ≥ Q 1 ≥ P 1 ≥ ( log ⁡ Q 1) 40 / η \exp(\sqrt{\log X})\geq Q_{1}\geq P_{1}\geq(\log Q_{1})^{40/\eta} large enough, and choose the remaining [P j, Q j] [P_{j},Q_{j}] as follows:

(4) |  | P j = exp ⁡ ( j 4 ​ j ​ ( log ⁡ Q 1) j − 1 ​ log ⁡ P 1) and Q j = exp ⁡ ( j 4 ​ j + 2 ​ ( log ⁡ Q 1) j). P_{j}=\exp(j^{4j}(\log Q_{1})^{j-1}\log P_{1})\quad\text{and}\quad Q_{j}=\exp(j^{4j+2}(\log Q_{1})^{j}). |  |

Let 𝒮 = 𝒮 X \mathcal{S}=\mathcal{S}_{X} be a set of integers X ≤ n ≤ 2 ​ X X\leq n\leq 2X having at least one prime factor in each of the intervals [P j, Q j] [P_{j},Q_{j}] for j ≤ J j\leq J, where J J is chosen to be the largest index j j such that Q j ≤ exp ⁡ ( ( log ⁡ X) 1 / 2) Q_{j}\leq\exp((\log X)^{1/2}).

Notice that, for any j ≤ J j\leq J, the number of integers in [X, 2 ​ X] [X,2X] that do not have a prime factor from [P j, Q j] [P_{j},Q_{j}] is by a standard sieve bound of order X ​ log ⁡ P j log ⁡ Q j X\frac{\log P_{j}}{\log Q_{j}}, which with the choice ( 4) is X ​ log ⁡ P 1 j 2 ​ log ⁡ Q 1 X\frac{\log P_{1}}{j^{2}\log Q_{1}}. Hence once Q 1 Q_{1} is large enough in terms of P 1 P_{1}, most integers in [X, 2 ​ X] [X,2X] belong to 𝒮 \mathcal{S}. It is also worth noticing that with the choice ( 4) a typical integer has about log ⁡ log ⁡ Q j log ⁡ P j = 2 ​ log ⁡ j + log ⁡ log ⁡ Q 1 − log ⁡ log ⁡ P 1 \log\frac{\log Q_{j}}{\log P_{j}}=2\log j+\log\log Q_{1}-\log\log P_{1} distinct prime factors in every fixed interval [P j, Q j] [P_{j},Q_{j}].

We will establish the following variant of Theorem 1 on the integers n ∈ 𝒮 n\in\mathcal{S}.

###### Theorem 3.

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. Let 𝒮 = 𝒮 X \mathcal{S}=\mathcal{S}_{X} be as above with η ∈ ( 0, 1 / 6) \eta\in(0,1/6). If [P 1, Q 1] ⊂ [1, h] [P_{1},Q_{1}]\subset[1,h], then for all X > X ⁡ ( η) X>X(\eta) large enough

 | 1 X ​ ∫ X 2 ​ X | 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) | 2 ​ 𝑑 x ≪ ( log ⁡ h) 1 / 3 P 1 1 / 6 − η + 1 ( log ⁡ X) 1 / 50. \frac{1}{X}\int_{X}^{2X}\left|\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}f(n)-\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}f(n)\right|^{2}dx\ll\frac{(\log h)^{1/3}}{P_{1}^{1/6-\eta}}+\frac{1}{(\log X)^{1/50}}. |  |

We show in Section 9 that for an appropriate choice of 𝒮 \mathcal{S} almost all integers n ∈ [X, 2 ​ X] n\in[X,2X] belong to 𝒮 \mathcal{S}. It follows by taking f ⁡ ( n) = 1 f(n)=1 in Theorem 3 that the same property holds in almost all short intervals. Combining this observation with Theorem 3, and the assumption that | f ⁡ ( n) | ≤ 1 |f(n)|\leq 1 implies Theorem 1.

To prove Theorem 2 we will establish the following variant on the integers n 1, n 2 ∈ 𝒮 n_{1},n_{2}\in\mathcal{S}.

###### Theorem 4.

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. Let 𝒮 \mathcal{S} be as above with η ∈ ( 0, 1 / 6) \eta\in(0,1/6). If [P 1, Q 1] ⊂ [1, h] [P_{1},Q_{1}]\subset[1,h], then for all x > x ⁡ ( η) x>x(\eta) large enough

 | 1 h ​ x ​ log ⁡ 2 ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 f ( n 1) f ( n 2) = ( 1 x ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ( n)) 2 + O ( ( log ⁡ Q 1) 1 / 6 P 1 1 / 12 − η / 2 + ( log X) − 1 / 100). \displaystyle\frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})=\Big(\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}f(n)\Big)^{2}+O\Big(\frac{(\log Q_{1})^{1/6}}{P_{1}^{1/12-\eta/2}}+(\log X)^{-1/100}\Big). |  |

As before, upon specializing the set 𝒮 \mathcal{S} and sieving, we can get rid of the requirement that n 1, n 2 ∈ 𝒮 n_{1},n_{2}\in\mathcal{S}, thus obtaining Theorem 2. While Theorem 4 is more complicated than Theorem 2, it outperforms the latter in certain applications, such as for example estimating the constant C ⁡ ( ε) C(\varepsilon) in Corollary 1. Using Theorem 4 gives C ⁡ ( ε) = ρ ​ ( 1 / ε) − 13 C(\varepsilon)=\rho(1/\varepsilon)^{-13} in Corollary 1, for small fixed ε \varepsilon, while Theorem 4 would only give estimates of the form C ⁡ ( ε) = exp ⁡ ( c / ρ ⁡ ( 1 / ε)) C(\varepsilon)=\exp(c/\rho(1/\varepsilon)). In addition, by using a smoothing in Theorem 4, one could further reduce the estimate for C ⁡ ( ε) C(\varepsilon) to ρ ​ ( 1 / ε) − 7 \rho(1/\varepsilon)^{-7} for small fixed ε \varepsilon. Similarly using Theorem 3 instead of Theorem 1 allows us to give a better bound in Corollary 4 for the exceptional set ℰ ⊂ [X, 2 ​ X] \mathcal{E}\subset[X,2X] of those x x ’s for which [x, x + h] [x,x+h] has no sign change of f f. Indeed we can show using Theorem 3 that ℰ \mathcal{E} has measure O ε ( X h − 1 / 6 + ε + ( log X) − 1 / 50) O_{\varepsilon}(Xh^{-1/6+\varepsilon}+(\log X)^{-1/50}).

### 2.1. Outline of the proofs of Theorems 3 and 4

We now discuss the ideas behind the proofs of Theorems 3 and 4. In both cases the first step consists in reducing the problem essentially to showing that

(5) |  | ∫ ( log ⁡ X) 1 / 15 X / h | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t | 2 ​ 𝑑 t ≪ ( log ⁡ h) 1 / 3 P 1 1 / 6 − η + 1 ( log ⁡ X) 1 / 50. \int_{(\log X)^{1/15}}^{X/h}\left|\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}}\right|^{2}dt\ll\frac{(\log h)^{1/3}}{P_{1}^{1/6-\eta}}+\frac{1}{(\log X)^{1/50}}. |  |

The above bound is established in Proposition 1 in Section 8, and we will now sketch how to prove this bound. We caution the reader that in the actual proof of Proposition 1 we need to argue more carefully and in particular split most Dirichlet polynomials into much shorter ranges to avoid an accumulation of error terms.

We begin by splitting the range of integration ( log ⁡ X) 1 / 15 ≤ t ≤ X / h (\log X)^{1/15}\leq t\leq X/h into J + 1 J+1 disjoint sets 𝒯 1, …, 𝒯 J, 𝒰 \mathcal{T}_{1},\ldots,\mathcal{T}_{J},\mathcal{U} which are defined according to the sizes of the Dirichlet polynomials

(6) |  | ∑ P j ≤ p ≤ Q j f ⁡ ( p) p 1 + i ​ t. \sum_{P_{j}\leq p\leq Q_{j}}\frac{f(p)}{p^{1+it}}. |  |

More precisely, we will define 𝒯 j \mathcal{T}_{j} as follows: t ∈ 𝒯 j t\in\mathcal{T}_{j} if j j is the smallest index such that all appropriate subdivisions of ( 6), i.e

 | ∑ P ≤ p ≤ Q f ⁡ ( p) p 1 + i ​ t ​ with ​ [P, Q] ⊂ [P j, Q j] \sum_{P\leq p\leq Q}\frac{f(p)}{p^{1+it}}\text{ with }[P,Q]\subset[P_{j},Q_{j}] |  |

are small (i.e with an appropriate power-saving). In practice the “sub-divisions” [P, Q] [P,Q] will be narrow intervals covering [P j, Q j] [P_{j},Q_{j}]. We will also define 𝒰 \mathcal{U} as follows: t ∈ 𝒰 t\in\mathcal{U} if there does not exists a j j such that t ∈ 𝒯 j t\in\mathcal{T}_{j}. The set 𝒰 \mathcal{U} is rather sparse (its measure is O ⁡ ( T 1 / 2 − ε) O(T^{1/2-\varepsilon})) and therefore t ∈ 𝒰 t\in\mathcal{U} can be considered an exceptional case. The argument then splits into two distinct parts.

The first is concerned with obtaining a saving for

(7) |  | ∫ 𝒯 j | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t | 2 ​ 𝑑 t \int_{\mathcal{T}_{j}}\Bigg|\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}}\Bigg|^{2}dt |  |

for each 1 ≤ j ≤ J 1\leq j\leq J, and the second part of the argument is concerned with bounding

(8) |  | ∫ 𝒰 | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t | 2 ​ 𝑑 t. \int_{\mathcal{U}}\Bigg|\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}}\Bigg|^{2}dt. |  |

The smaller the length of the interval h h is, the more sets 𝒯 j \mathcal{T}_{j} we are required to work with, which leads to an increasing complication of the proof. It is worth mentioning that for intervals of length h = X ε h=X^{\varepsilon} it is enough to take J = 1 J=1 and most of the work consists in dealing with 𝒰 \mathcal{U}. In addition, in the special case h = X ε h=X^{\varepsilon} and f ⁡ ( n) = μ ⁡ ( n) f(n)=\mu(n) we do not even need to consider the integral over 𝒰 \mathcal{U} and a very simple argument suffices. Both of the above remarks are explained in detail in our short note [29].

When t ∈ 𝒯 j t\in\mathcal{T}_{j} we use an analogue of Buchstab’s identity (a variant of Ramaré’s identity [8, Section 17.3]) to extract from the Dirichlet polynomial

 | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t \sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}} |  |

a Dirichlet polynomial over the primes in [P j, Q j] [P_{j},Q_{j}], which is known to be small (by our assumption that t ∈ 𝒯 j t\in\mathcal{T}_{j}). More precisely, for completely multiplicative f ⁡ ( n) f(n) (the same ideas works for general multiplicative functions, but is more transparent in this case) we have

(9) |  | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t = ∑ P j ≤ p ≤ Q j f ⁡ ( p) p 1 + i ​ t \displaystyle\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}}=\sum_{P_{j}\leq p\leq Q_{j}}\frac{f(p)}{p^{1+it}} | ∑ X / p ≤ m ≤ 2 ​ X / p m ∈ 𝒮 j f ⁡ ( m) m 1 + i ​ t ⋅ 1 #{ P j ≤ q ≤ Q j: q | m } + 𝟏 ( p, m) = 1, \displaystyle\sum_{\begin{subarray}{c}X/p\leq m\leq 2X/p\\ m\in\mathcal{S}_{j}\end{subarray}}\frac{f(m)}{m^{1+it}}\cdot\frac{1}{\#\{P_{j}\leq q\leq Q_{j}:q|m\}+\mathbf{1}_{(p,m)=1}}, |  |

where 𝟏 ( p, m) = 1 \mathbf{1}_{(p,m)=1} is 1 1 1 In the published version of this paper the term 𝟏 ( p, m) = 1 \mathbf{1}_{(p,m)=1} was incorrectly expressed as 1 1 leading to a slight gap in the argument that affected only the proof of Lemma 12. This is corrected here. We thank Alisa Sedunova and Ke Wang for pointing out this issue to us. the indicator function of ( p, m) = 1 (p,m)=1, and 𝒮 j \mathcal{S}_{j} is the set of integers which have a prime factor from each interval [P i, Q i] [P_{i},Q_{i}] with i ≤ J i\leq J except possibly not from [P j, Q j] [P_{j},Q_{j}]. We then do some cosmetic operations: we dispose of the condition X / p ≤ m ≤ 2 ​ X / p X/p\leq m\leq 2X/p by splitting into short segments, and we replace 𝟏 ( p, m) = 1 \mathbf{1}_{(p,m)=1} by 1 1 by noticing that for most t t the contribution of the terms with p | m p|m is negligible. The next step is to use a pointwise bound (which follows from the definition of 𝒯 j \mathcal{T}_{j}) for the polynomial over p ∈ [P j, Q j] p\in[P_{j},Q_{j}] and a mean value theorem for Dirichlet polynomials for the remaining polynomial over m m (by forgetting about the condition t ∈ 𝒯 j t\in\mathcal{T}_{j} and extending the range of integration to | t | ≤ X / h |t|\leq X/h). This gives the desired saving in ( 7) when j = 1 j=1, but for j > 1 j>1 the length of the Dirichlet polynomial

(10) |  | R P ( 1 + i t) = ∑ X / P ≤ m ≤ 2 ​ X / P m ∈ 𝒮 j f ⁡ ( m) m 1 + i ​ t ⋅ 1 #{ P j ≤ p ≤ Q j: p | m } + 1, P ∈ [P j, Q j] R_{P}(1+it)=\sum_{\begin{subarray}{c}X/P\leq m\leq 2X/P\\ m\in\mathcal{S}_{j}\end{subarray}}\frac{f(m)}{m^{1+it}}\cdot\frac{1}{\#\{P_{j}\leq p\leq Q_{j}:p|m\}+1}\ ,\ P\in[P_{j},Q_{j}] |  |

is too short compared to the length of integration to produce a good bound. To get around this issue, we will use the definition of 𝒯 j \mathcal{T}_{j}, namely the assumption that there exists a narrow interval [P, Q] ⊂ [P j − 1, Q j − 1] [P,Q]\subset[P_{j-1},Q_{j-1}] for which

 | ∑ P ≤ p ≤ Q f ⁡ ( p) p 1 + i ​ t \sum_{P\leq p\leq Q}\frac{f(p)}{p^{1+it}} |  |

is large, say ≥ V \geq V. This allows us to bound the mean-value of ( 10) by the mean-value of

(11) |  | ( V − 1 ​ ∑ P ≤ p ≤ Q f ⁡ ( p) p 1 + i ​ t) ℓ ​ R P ​ ( 1 + i ​ t) \Bigg(V^{-1}\sum_{P\leq p\leq Q}\frac{f(p)}{p^{1+it}}\Bigg)^{\ell}R_{P}(1+it) |  |

with an appropriate choice of ℓ \ell, making the length of the above Dirichlet polynomial close to X / h X/h (which is also the length of integration). While computing the moments, the conditions ( 2) and ( 3) on [P j, Q j] [P_{j},Q_{j}] arise naturally: Q j − 1 Q_{j-1} needs to be comparatively small with respect to P j P_{j} so that the length of the Dirichlet polynomial ( 11) is necessarily close to X / h X/h for some choice of ℓ \ell. On the other hand Q j − 1 Q_{j-1} cannot be too small compared to P j P_{j}, so that we are not forced to choose too large ℓ \ell which would increase too much the mean-value of ( 11). Fortunately, it turns out that neither condition is very restrictive and there is a large set of choices of [P j, Q j] [P_{j},Q_{j}] meeting both conditions.

Let us now explain how one bounds the remaining integral ( 8). In this case we split the Dirichlet polynomial

 | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n 1 + i ​ t \sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{1+it}} |  |

into a Dirichlet polynomial whose coefficients are supported on the integers which have a prime factor in the range exp ⁡ ( ( log ⁡ X) 1 − 1 / 48) ≤ p ≤ exp ⁡ ( log ⁡ X / log ⁡ log ⁡ X) \exp((\log X)^{1-1/48})\leq p\leq\exp(\log X/\log\log X), say, and a Dirichlet polynomial whose coefficients are supported on the integers which are co-prime to every prime in this range. The coefficients of the second Dirichlet polynomial are supported on a set of smaller density, and applying the mean-value theorem easily shows that we can ignore its contribution. To the first Dirichlet polynomial we apply the version of Buchstab’s identity discussed before. In addition since 𝒰 \mathcal{U} is a thin set (of size O ⁡ ( T 1 / 2 − ε) O(T^{1/2-\varepsilon})) we can bound the integral by a sum of O ⁡ ( T 1 / 2 − ε) O(T^{1/2-\varepsilon}) well-spaced points. Thus our problem reduces essentially to bounding

(12) |  | ( log ⁡ X) 2 + ε ​ ∑ t ∈ 𝒯 | P ⁡ ( 1 + i ​ t) ​ M ​ ( 1 + i ​ t) | 2 (\log X)^{2+\varepsilon}\sum_{t\in\mathcal{T}}|P(1+it)M(1+it)|^{2} |  |

where 𝒯 \mathcal{T} is a set of well-spaced points from 𝒰 \mathcal{U}, where P ⁡ ( 1 + i ​ t) P(1+it) is a polynomial whose coefficients are supported on the primes in a dyadic range, M ⁡ ( 1 + i ​ t) M(1+it) is the corresponding Dirichlet polynomial over the integers arising from Buchstab’s identity, and the term ( log ⁡ X) 2 + ε (\log X)^{2+\varepsilon} comes from the loss incurred by ensuring that P P is in a dyadic interval.

The Dirichlet polynomial | P ⁡ ( 1 + i ​ t) | |P(1+it)| is small most of the time (in fact for f = μ f=\mu it is always small for | t | ≤ X |t|\leq X), and on the set where it is small we are done by simply bounding P P and applying Halász’s large value estimate to sum | M ⁡ ( 1 + i ​ t) | 2 |M(1+it)|^{2} over the well-spaced points t ∈ 𝒯 t\in\mathcal{T} (Halász’s large values theorem is applicable since | 𝒯 | ≪ T 1 / 2 − ε |\mathcal{T}|\ll T^{1/2-\varepsilon}). On the other hand taking moments we can show that | P ⁡ ( 1 + i ​ t) | |P(1+it)| is large extremely rarely (on a set of size exp ⁡ ( ( log ⁡ X) 1 / 48 + o ⁡ ( 1)) \exp((\log X)^{1/48+o(1)})). We know in addition that | M ⁡ ( 1 + i ​ t) | 2 |M(1+it)|^{2} is always ≪ ( log ⁡ X) − δ \ll(\log X)^{-\delta}, for some small fixed δ > 0 \delta>0, by Halász’s theorem on multiplicative functions (since f ∈ ℝ f\in\mathbb{R} and | t | > ( log ⁡ X) 1 / 15 |t|>(\log X)^{1/15} is bounded away from zero). Applying this pointwise bound to | M ⁡ ( 1 + i ​ t) | 2 |M(1+it)|^{2} we are left with averaging | P ⁡ ( 1 + i ​ t) | 2 |P(1+it)|^{2} over a very sparse set of points, and we need to save one logarithm compared to the standard application of Halász’s large value estimate (which already regains one logarithm from the mean square of coefficients of P P since the coefficients are supported on primes in a dyadic interval). To do this, we derive a Halász type large value estimates for Dirichlet polynomials whose coefficients are supported on the primes. Altogether we regain the loss of ( log ⁡ x) 2 (\log x)^{2} and we win by ( log ⁡ x) − δ + ε (\log x)^{-\delta+\varepsilon} which followed from Halász’s theorem on multiplicative functions.

Finally, we note that an iterative decomposition of Dirichlet polynomials is employed in a different way in two very recent papers on moments of L L -functions (see [33] and [16]).

## 3. Halász theorem

As explained above, in the proof we use Halász’s theorem which says that unless a multiplicative function pretends to be p i ​ t p^{it}, it is small on average. Pretending is measured through the distance function

 | 𝔻 ​ ( f, g, x) 2 = ∑ p ≤ x 1 − ℜ ⁡ f ⁡ ( p) ​ g ⁡ ( p) ¯ p \mathbb{D}(f,g;x)^{2}=\sum_{p\leq x}\frac{1-\Re f(p)\overline{g(p)}}{p} |  |

which satisfies the triangle inequality

 | 𝔻 ⁡ ( f, h, x) ≤ 𝔻 ⁡ ( f, g, x) + 𝔻 ⁡ ( g, h, x) \mathbb{D}(f,h;x)\leq\mathbb{D}(f,g;x)+\mathbb{D}(g,h;x) |  |

for any f, g, h: ℕ → { z ∈ ℂ: | z | ≤ 1 } f,g,h:\mathbb{N}\rightarrow\{z\in\mathbb{C}:|z|\leq 1\}.

Upon noticing that 𝔻 ⁡ ( f ​ p − i ​ t, p i ​ t 0, x) = 𝔻 ⁡ ( f, p i ​ t + i ​ t 0, x) \mathbb{D}(fp^{-it},p^{it_{0}};x)=\mathbb{D}(f,p^{it+it_{0}};x), the following lemma follows immediately from Halász’s theorem (see for instance [12, Corollary 1]) and partial summation.

###### Lemma 1.

Let f: ℕ → [− 1, 1] f\colon\mathbb{N}\to[-1,1] be a multiplicative function, and let

 | F ⁡ ( s) = ∑ x ≤ n ≤ 2 ​ x f ⁡ ( n) n s. F(s)=\sum_{x\leq n\leq 2x}\frac{f(n)}{n^{s}}. |  |

and T 0 ≥ 1 T_{0}\geq 1. Let

 | M ⁡ ( x, T 0) = min | t 0 | ≤ T 0 ⁡ 𝔻 ​ ( f, p i ​ t + i ​ t 0, x) 2 M(x,T_{0})=\min_{|t_{0}|\leq T_{0}}\mathbb{D}(f,p^{it+it_{0}};x)^{2} |  |

Then

 | | F ⁡ ( σ + i ​ t) | ≪ x 1 − σ ​ ( M ⁡ ( x, T 0) ​ exp ⁡ ( − M ⁡ ( x, T 0)) + 1 T 0 + log ⁡ log ⁡ x log ⁡ x) |F(\sigma+it)|\ll x^{1-\sigma}\left(M(x,T_{0})\exp(-M(x,T_{0}))+\frac{1}{T_{0}}+\frac{\log\log x}{\log x}\right) |  |

The following lemma which is essentially due to Granville and Soundararajan is used to get a lower bound for the distance.

###### Lemma 2.

Let f: ℕ → [− 1, 1] f\colon\mathbb{N}\to[-1,1] be a multiplicative function, and let ε > 0 \varepsilon>0. For any fixed A A and 1 ≤ | α | ≤ x A 1\leq|\alpha|\leq x^{A},

 | 𝔻 ⁡ ( f, p i ​ α, x) ≥ ( 1 2 ​ 3 − ε) ​ log ⁡ log ⁡ x + O ⁡ ( 1). \mathbb{D}(f,p^{i\alpha};x)\geq\left(\frac{1}{2\sqrt{3}}-\varepsilon\right)\sqrt{\log\log x}+O(1). |  |

###### Proof.

By the triangle inequality

 | 2 ​ 𝔻 ​ ( f, p i ​ α, x) = 𝔻 ⁡ ( p − i ​ α, f, x) + 𝔻 ⁡ ( f, p i ​ α, x) ≥ 𝔻 ⁡ ( p − i ​ α, p i ​ α, x) = 𝔻 ⁡ ( 1, p 2 ​ i ​ α, x). 2\mathbb{D}(f,p^{i\alpha};x)=\mathbb{D}(p^{-i\alpha},f;x)+\mathbb{D}(f,p^{i\alpha};x)\geq\mathbb{D}(p^{-i\alpha},p^{i\alpha};x)=\mathbb{D}(1,p^{2i\alpha};x). |  |

Furthermore

 | 𝔻 ​ ( 1, p 2 ​ i ​ α, x) 2 = ∑ p ≤ x 1 − ℜ ⁡ p − 2 ​ i ​ α p ≥ ∑ exp ⁡ ( ( log ⁡ x) 2 / 3 + ε) ≤ p ≤ x 1 − ℜ ⁡ p − 2 ​ i ​ α p ≥ ( 1 3 − ε) ​ log ⁡ log ⁡ x + O ⁡ ( 1) − | ∑ exp ⁡ ( ( log ⁡ x) 2 / 3 + ε) ≤ p ≤ x 1 p 1 + 2 ​ i ​ α | ≥ ( 1 3 − ε) ​ log ⁡ log ⁡ x + O ⁡ ( 1) \begin{split}\mathbb{D}(1,p^{2i\alpha};x)^{2}&=\sum_{p\leq x}\frac{1-\Re p^{-2i\alpha}}{p}\geq\sum_{\exp((\log x)^{2/3+\varepsilon})\leq p\leq x}\frac{1-\Re p^{-2i\alpha}}{p}\\ &\geq\left(\frac{1}{3}-\varepsilon\right)\log\log x+O(1)-\left|\sum_{\exp((\log x)^{2/3+\varepsilon})\leq p\leq x}\frac{1}{p^{1+2i\alpha}}\right|\\ &\geq\left(\frac{1}{3}-\varepsilon\right)\log\log x+O(1)\end{split} |  |

by the zero-free region for the Riemann zeta-function. ∎

Actually we will need to apply Halász theorem to a function which is not quite multiplicative and the following lemma takes care of this application to a polynomial arising from the Buchstab type identity ( 9).

###### Lemma 3.

Let X ≥ Q ≥ P ≥ 2 X\geq Q\geq P\geq 2. Let f ⁡ ( n) f(n) be a real-valued multiplicative function and

 | R ( s) = ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) n s ⋅ 1 #{ p ∈ [P, Q]: p ∣ n } + 1. R(s)=\sum_{\begin{subarray}{c}X\leq n\leq 2X\end{subarray}}\frac{f(n)}{n^{s}}\cdot\frac{1}{\#\{p\in[P,Q]\colon p\mid n\}+1}. |  |

Then for any t ∈ [( log ⁡ X) 1 / 16, X A] t\in[(\log X)^{1/16},X^{A}],

 | | R ⁡ ( 1 + i ​ t) | ≪ log ⁡ Q ( log ⁡ X) 1 / 16 ​ log ⁡ P + log ⁡ X ⋅ exp ⁡ ( − log ⁡ X 3 ​ log ⁡ Q ​ log ⁡ log ⁡ X log ⁡ Q). |R(1+it)|\ll\frac{\log Q}{(\log X)^{1/16}\log P}+\log X\cdot\exp\left(-\frac{\log X}{3\log Q}\log\frac{\log X}{\log Q}\right). |  |

###### Proof.

Splitting n = n 1 ​ n 2 n=n_{1}n_{2} where n 1 n_{1} has all prime factors from [P, Q] [P,Q] and n 2 n_{2} has none, we get

 | | R ⁡ ( 1 + i ​ t) | = | ∑ n 1 ≤ X 3 / 4 p | n 1 ⟹ p ∈ [P, Q] f ⁡ ( n 1) n 1 1 + i ​ t ​ ( ω ⁡ ( n 1) + 1) ​ ∑ X / n 1 ≤ n 2 ≤ 2 ​ X / n 1 p | n 2 ⟹ p ∉ [P, Q] f ⁡ ( n 2) n 2 1 + i ​ t | + O ⁡ ( ∑ n 2 ≤ X 1 / 2 p | n 2 ⟹ p ∉ [P, Q] 1 n 2 ​ ∑ X / n 2 ≤ n 1 ≤ 2 ​ X / n 2 p | n 1 ⟹ p ∈ [P, Q] 1 n 1) ≪ ∑ n 1 ≤ X 3 / 4 p | n 1 ⟹ p ∈ [P, Q] 1 n 1 ​ | ∑ X / n 1 ≤ n 2 ≤ 2 ​ X / n 1 p | n 2 ⟹ p ∉ [P, Q] f ⁡ ( n 2) n 2 1 + i ​ t | + ∑ n 2 ≤ X 1 / 2 1 n 2 ​ ∑ X / n 2 ≤ n 1 ≤ 2 ​ X / n 2 p | n 1 ⟹ p < Q 1 n 1 \begin{split}|R(1+it)|&=\left|\sum_{\begin{subarray}{c}n_{1}\leq X^{3/4}\\ p\mid n_{1}\implies p\in[P,Q]\end{subarray}}\frac{f(n_{1})}{n_{1}^{1+it}(\omega(n_{1})+1)}\sum_{\begin{subarray}{c}X/n_{1}\leq n_{2}\leq 2X/n_{1}\\ p\mid n_{2}\implies p\not\in[P,Q]\end{subarray}}\frac{f(n_{2})}{n_{2}^{1+it}}\right|\\ \qquad&+O\left(\sum_{\begin{subarray}{c}n_{2}\leq X^{1/2}\\ p\mid n_{2}\implies p\not\in[P,Q]\end{subarray}}\frac{1}{n_{2}}\sum_{\begin{subarray}{c}X/n_{2}\leq n_{1}\leq 2X/n_{2}\\ p\mid n_{1}\implies p\in[P,Q]\end{subarray}}\frac{1}{n_{1}}\right)\\ &\ll\sum_{\begin{subarray}{c}n_{1}\leq X^{3/4}\\ p\mid n_{1}\implies p\in[P,Q]\end{subarray}}\frac{1}{n_{1}}\left|\sum_{\begin{subarray}{c}X/n_{1}\leq n_{2}\leq 2X/n_{1}\\ p\mid n_{2}\implies p\not\in[P,Q]\end{subarray}}\frac{f(n_{2})}{n_{2}^{1+it}}\right|+\sum_{n_{2}\leq X^{1/2}}\frac{1}{n_{2}}\sum_{\begin{subarray}{c}X/n_{2}\leq n_{1}\leq 2X/n_{2}\\ p\mid n_{1}\implies p<Q\end{subarray}}\frac{1}{n_{1}}\end{split} |  |

By an estimate for the number of Q Q -smooth numbers, the second term is at most O ⁡ ( ( log ⁡ X) − 1 + log ⁡ X ​ exp ⁡ ( − log ⁡ X 3 ​ log ⁡ Q ​ log ⁡ log ⁡ X log ⁡ Q)) O((\log X)^{-1}+\log X\exp(-\frac{\log X}{3\log Q}\log\frac{\log X}{\log Q})). To the first term we apply Halász’s theorem (Lemmas 1 and 2) to the sum over n 2 n_{2} obtaining a saving of ( log X) − 1 / 16 (\log X)^{-1/16} and we bound the sum over n 1 n_{1} by ∏ p ∈ [P, Q] ( 1 − 1 / p) − 1 ≪ log ⁡ Q log ⁡ P \prod_{p\in[P,Q]}(1-1/p)^{-1}\ll\frac{\log Q}{\log P}. Hence

 | | R ⁡ ( 1 + i ​ t) | ≪ log ⁡ Q ( log ⁡ X) 1 / 16 ​ log ⁡ P + ( log ⁡ X) ​ exp ⁡ ( − log ⁡ X 3 ​ log ⁡ Q ​ log ⁡ log ⁡ X log ⁡ Q). |R(1+it)|\ll\frac{\log Q}{(\log X)^{1/16}\log P}+(\log X)\exp\left(-\frac{\log X}{3\log Q}\log\frac{\log X}{\log Q}\right). |  |

∎

We will also evaluate the average of f ⁡ ( n) f(n) on intervals slightly shorter than x x. For this we use the following Lipschitz type result due to Granville and Soundararajan.

###### Lemma 4.

Let f: ℕ → [− 1, 1] f\colon\mathbb{N}\to[-1,1] be a multiplicative function. For any x ∈ [X, 2 ​ X] x\in[X,2X] and X / ( log ⁡ X) 1 / 5 ≤ y ≤ X X/(\log X)^{1/5}\leq y\leq X, one has

 | 1 y ​ ∑ x ≤ n ≤ x + y f ⁡ ( n) = 1 X ​ ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) + O ⁡ ( 1 ( log ⁡ X) 1 / 20). \frac{1}{y}\sum_{x\leq n\leq x+y}f(n)=\frac{1}{X}\sum_{X\leq n\leq 2X}f(n)+O\left(\frac{1}{(\log X)^{1/20}}\right). |  |

###### Proof.

We shall show that, for any X / 4 ≤ Y ≤ X X/4\leq Y\leq X,

(13) |  | | 1 X ​ ∑ n ≤ X f ⁡ ( n) − 1 Y ​ ∑ n ≤ Y f ⁡ ( n) | ≪ 1 ( log ⁡ X) 1 / 4 \left|\frac{1}{X}\sum_{n\leq X}f(n)-\frac{1}{Y}\sum_{n\leq Y}f(n)\right|\ll\frac{1}{(\log X)^{1/4}} |  |

from which the claim follows easily.

Let t f t_{f} be the t t for which 𝔻 ⁡ ( f, p i ​ t, X) \mathbb{D}(f,p^{it};X) is minimal among | t | ≤ log ⁡ X |t|\leq\log X. Notice that if 𝔻 ​ ( f, p i ​ t f, X) 2 ≥ 1 3 ​ log ⁡ log ⁡ X \mathbb{D}(f,p^{it_{f}};X)^{2}\geq\frac{1}{3}\log\log X, then ( 13) follows immediately from Halász’s theorem (Lemma 1). This is in particular the case if | t f | ≥ 1 / 100 |t_{f}|\geq 1/100, since in this case

 | 𝔻 ​ ( f, p i ​ t f, X) 2 ≥ ∑ p ≤ X 1 − | cos ⁡ ( t f ​ log ⁡ p) | p ≥ ( 1 − 1 2 ​ π ​ ∫ 0 2 ​ π | cos ⁡ α | ​ 𝑑 α − o ⁡ ( 1)) ​ log ⁡ log ⁡ X = ( 1 − 2 π − o ⁡ ( 1)) ​ log ⁡ log ⁡ X \begin{split}\mathbb{D}(f,p^{it_{f}};X)^{2}&\geq\sum_{p\leq X}\frac{1-|\cos(t_{f}\log p)|}{p}\geq\left(1-\frac{1}{2\pi}\int_{0}^{2\pi}|\cos\alpha|d\alpha-o(1)\right)\log\log X\\ &=\left(1-\frac{2}{\pi}-o(1)\right)\log\log X\end{split} |  |

by partial summation and the prime number theorem.

Hence we can assume that | t f | ≤ 1 / 100 |t_{f}|\leq 1/100 and 𝔻 ​ ( f, p i ​ t f, X) 2 < 1 3 ​ log ⁡ log ⁡ X \mathbb{D}(f,p^{it_{f}};X)^{2}<\frac{1}{3}\log\log X. By [12, Lemma 7.1 and Theorem 4], recalling that f f is real-valued,

(14) |  | | 1 X ∑ n ≤ X f ( n) − ( X Y) i ​ t f ⋅ 1 Y ∑ n ≤ Y f ( n) | = | 1 X 1 + i ​ t f ​ ∑ n ≤ X f ⁡ ( n) − 1 Y 1 + i ​ t f ​ ∑ n ≤ Y f ⁡ ( n) | = | 1 + i ​ t f X ​ ∑ n ≤ X f ⁡ ( n) n i ​ t f − 1 + i ​ t f Y ​ ∑ n ≤ Y f ⁡ ( n) n i ​ t f | + O ⁡ ( 1 log ⁡ X ​ exp ⁡ ( 𝔻 ​ ( 1, f, X) 2)) ≪ 1 ( log ⁡ X) 1 / 4. \begin{split}&\left|\frac{1}{X}\sum_{n\leq X}f(n)-\left(\frac{X}{Y}\right)^{it_{f}}\cdot\frac{1}{Y}\sum_{n\leq Y}f(n)\right|\\ &=\left|\frac{1}{X^{1+it_{f}}}\sum_{n\leq X}f(n)-\frac{1}{Y^{1+it_{f}}}\sum_{n\leq Y}f(n)\right|\\ &=\left|\frac{1+it_{f}}{X}\sum_{n\leq X}\frac{f(n)}{n^{it_{f}}}-\frac{1+it_{f}}{Y}\sum_{n\leq Y}\frac{f(n)}{n^{it_{f}}}\right|+O\left(\frac{1}{\log X}\exp(\mathbb{D}(1,f;X)^{2})\right)\\ &\ll\frac{1}{(\log X)^{1/4}}.\end{split} |  |

For | t f | ≤ 1 / 100 |t_{f}|\leq 1/100 we have | ( X / Y) i ​ t f − 1 | ≤ 1 / 2 |(X/Y)^{it_{f}}-1|\leq 1/2, so that ( 14) implies

 | | 1 X ∑ n ≤ X f ( n) − 1 Y ∑ n ≤ Y f ( n) | ≤ 1 2 ⋅ 1 Y ∑ n ≤ Y f ( n) + O ( ( log X) − 1 / 4), \left|\frac{1}{X}\sum_{n\leq X}f(n)-\frac{1}{Y}\sum_{n\leq Y}f(n)\right|\leq\frac{1}{2}\cdot\frac{1}{Y}\sum_{n\leq Y}f(n)+O((\log X)^{-1/4}), |  |

which implies that either the left hand side is O ( ( log X) − 1 / 4) O((\log X)^{-1/4}) (i.e. ( 13) holds)) or 1 X ​ ∑ n ≤ X f ⁡ ( n) \frac{1}{X}\sum_{n\leq X}f(n) and 1 Y ​ ∑ n ≤ Y f ⁡ ( n) \frac{1}{Y}\sum_{n\leq Y}f(n) have the same sign. In the latter case we notice that ( 14) implies also (see also [12, Corollary 3])

 | | | 1 X ​ ∑ n ≤ X f ⁡ ( n) | − | 1 Y ​ ∑ n ≤ Y f ⁡ ( n) | | ≪ 1 ( log ⁡ X) 1 / 4, \left|\left|\frac{1}{X}\sum_{n\leq X}f(n)\right|-\left|\frac{1}{Y}\sum_{n\leq Y}f(n)\right|\right|\ll\frac{1}{(\log X)^{1/4}}, |  |

and ( 13) follows, since the averages have the same sign, so that the inner absolute values can be removed. ∎

We will actually need to apply the previous two lemmas for sums with the additional restriction n ∈ 𝒮 n\in\mathcal{S} where 𝒮 \mathcal{S} is as in Section 2. This can be done through the following immediate consequence of the inclusion-exclusion principle.

###### Lemma 5.

Let 𝒮 \mathcal{S} be as in Section 2. For 𝒥 ⊆ { 1, …, J } \mathcal{J}\subseteq\{1,\dotsc,J\}, let g g be the completely multiplicative function

 | g 𝒥 ​ ( p j) = { 1 if p ∉ ⋃ j ∈ 𝒥 [P j, Q j] 0 otherwise. g_{\mathcal{J}}(p^{j})=\begin{cases}1&\text{if $p\not\in\bigcup_{j\in\mathcal{J}}[P_{j},Q_{j}]$}\\ 0&\text{otherwise}.\end{cases} |  |

Then

 | ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 a n = ∑ X ≤ n ≤ 2 ​ X a n ​ ∏ j = 1 J ( 1 − g { j } ​ ( n)) = ∑ 𝒥 ⊆ { 1, …, J } ( − 1) #​ 𝒥 ​ ∑ X ≤ n ≤ 2 ​ X g 𝒥 ​ ( n) ​ a n. \sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}a_{n}=\sum_{\begin{subarray}{c}X\leq n\leq 2X\end{subarray}}a_{n}\prod_{j=1}^{J}(1-g_{\{j\}}(n))=\sum_{\mathcal{J}\subseteq\{1,\dotsc,J\}}(-1)^{\#\mathcal{J}}\sum_{X\leq n\leq 2X}g_{\mathcal{J}}(n)a_{n}. |  |

## 4. Mean and large value theorems for Dirichlet polynomials

Let us first collect some standard mean and large value results for Dirichlet polynomials.

###### Lemma 6.

Let A ⁡ ( s) = ∑ n ≤ N a n ​ n − s A(s)=\sum_{n\leq N}a_{n}n^{-s}. Then

 | ∫ − T T | A ⁡ ( i ​ t) | 2 ​ 𝑑 t = ( T + O ⁡ ( N)) ​ ∑ n ≤ N | a n | 2 \int_{-T}^{T}|A(it)|^{2}dt=(T+O(N))\sum_{n\leq N}|a_{n}|^{2} |  |

###### Proof.

See [20, Theorem 9.1]. ∎

For the rest of the paper we say that 𝒯 ⊆ ℝ \mathcal{T}\subseteq\mathbb{R} is well-spaced if | t − r | ≥ 1 |t-r|\geq 1 for all distinct t, r ∈ 𝒯 t,r\in\mathcal{T}.

###### Lemma 7.

Let A ⁡ ( s) = ∑ n ≤ N a n ​ n − s A(s)=\sum_{n\leq N}a_{n}n^{-s}, and let 𝒯 ⊂ [− T, T] \mathcal{T}\subset[-T,T] be a sequence of well-spaced points. Then

 | ∑ t ∈ 𝒯 | A ⁡ ( i ​ t) | 2 ≪ ( T + N) ​ log ⁡ 2 ​ N ​ ∑ n ≤ N | a n | 2 \sum_{t\in\mathcal{T}}|A(it)|^{2}\ll(T+N)\log 2N\sum_{n\leq N}|a_{n}|^{2} |  |

###### Proof.

See [20, Theorem 9.4]. ∎

###### Lemma 8.

Let

 | P ⁡ ( s) = ∑ P ≤ p ≤ 2 ​ P a p p s with | a p | ≤ 1. P(s)=\sum_{P\leq p\leq 2P}\frac{a_{p}}{p^{s}}\quad\text{with $|a_{p}|\leq 1$.} |  |

Let 𝒯 ⊂ [− T, T] \mathcal{T}\subset[-T,T] be a sequence of well-spaced points such that | P ⁡ ( 1 + i ​ t) | ≥ V − 1 |P(1+it)|\geq V^{-1} for every t ∈ 𝒯 t\in\mathcal{T}. Then

 | | 𝒯 | ≪ T 2 ​ log ⁡ V log ⁡ P ​ V 2 ​ exp ⁡ ( 2 ​ log ⁡ T log ⁡ P ​ log ⁡ log ⁡ T). |\mathcal{T}|\ll T^{2\frac{\log V}{\log P}}V^{2}\exp\left(2\frac{\log T}{\log P}\log\log T\right). |  |

###### Proof.

Let k = ⌈ log ⁡ T / log ⁡ P ⌉ k=\lceil\log T/\log P\rceil and

 | P ​ ( s) k =: ∑ P k ≤ n ≤ ( 2 ​ P) k b ⁡ ( n) ​ n − s. P(s)^{k}=:\sum_{P^{k}\leq n\leq(2P)^{k}}b(n)n^{-s}. |  |

Notice that

 | ∑ P k ≤ n ≤ ( 2 ​ P) k ( b ⁡ ( n) n) 2 ≤ ∑ n ( ∑ p 1 ​ ⋯ ​ p k = n P ≤ p j ≤ 2 ​ P 1 p 1 ​ ⋯ ​ p k) 2 ≤ 1 P k ​ ∑ p 1 ​ ⋯ ​ p k = q 1 ​ ⋯ ​ q k P ≤ p j, q j ≤ 2 ​ P 1 p 1 ​ ⋯ ​ p k ≤ 1 P k ​ k! ​ ( ∑ P ≤ p ≤ 2 ​ P 1 p) k. \begin{split}&\sum_{P^{k}\leq n\leq(2P)^{k}}\left(\frac{b(n)}{n}\right)^{2}\leq\sum_{n}\left(\sum_{\begin{subarray}{c}p_{1}\dotsm p_{k}=n\\ P\leq p_{j}\leq 2P\end{subarray}}\frac{1}{p_{1}\dotsm p_{k}}\right)^{2}\\ &\leq\frac{1}{P^{k}}\sum_{\begin{subarray}{c}p_{1}\dotsm p_{k}=q_{1}\dotsm q_{k}\\ P\leq p_{j},q_{j}\leq 2P\end{subarray}}\frac{1}{p_{1}\dotsm p_{k}}\leq\frac{1}{P^{k}}k!\Big(\sum_{P\leq p\leq 2P}\frac{1}{p}\Big)^{k}.\end{split} |  |

Hence by the previous lemma and Chebyschev’s inequality

 | | 𝒯 | ≪ V 2 ​ k ⋅ ( T + ( 2 ​ P) k) ​ log ⁡ ( 2 ​ P) k ​ 1 P k ​ k! ​ ( ∑ P ≤ p ≤ 2 ​ P 1 p) k ≪ T 2 ​ log ⁡ V log ⁡ P ​ V 2 ​ 5 k ​ k!. \begin{split}|\mathcal{T}|&\ll V^{2k}\cdot(T+(2P)^{k})\log(2P)^{k}\frac{1}{P^{k}}k!\Big(\sum_{P\leq p\leq 2P}\frac{1}{p}\Big)^{k}\\ &\ll T^{2\frac{\log V}{\log P}}V^{2}5^{k}k!.\end{split} |  |

∎

For sparse sets 𝒯 \mathcal{T} one can use work of Halász to improve on the bound given for ∑ t ∈ 𝒯 | A ⁡ ( i ​ t) | 2 \sum_{t\in\mathcal{T}}|A(it)|^{2} in Lemma 7. We will actually need two versions of Halász’s inequality. The first, stated below, works for arbitrary Dirichlet polynomials supported on integers. The second, stated in Lemma 11 requires the Dirichlet polynomial to be supported on the primes, and is stronger in certain situations. Accordingly we call the first Lemma a “Halász inequality for the integers” and the second a “Halász inequality for the primes”.

###### Lemma 9 (Halász inequality for integers).

Let A ⁡ ( s) = ∑ n ≤ N a n ​ n − i ​ t A(s)=\sum_{n\leq N}a_{n}n^{-it} and let 𝒯 \mathcal{T} be a sequence of well-spaced points. Then

 | ∑ t ∈ 𝒯 | A ⁡ ( i ​ t) | 2 ≪ ( N + | 𝒯 | ​ T) ​ log ⁡ 2 ​ T ​ ∑ n ≤ N | a n | 2 \sum_{t\in\mathcal{T}}|A(it)|^{2}\ll(N+|\mathcal{T}|\sqrt{T})\log 2T\sum_{n\leq N}|a_{n}|^{2} |  |

###### Proof.

See [20, Theorem 9.6]. ∎

Let us now explain why we need a separate “Halász inequality for the primes”. In all the mean and large value theorems presented so far, the term N ​ ∑ n ≤ N | a n | 2 N\sum_{n\leq N}|a_{n}|^{2} reflects the largest possible value of | A ⁡ ( i ​ t) | 2 |A(it)|^{2}. However, when n n is supported on a thin sets such as primes, such a bound loses a logarithmic factor compared to the expected maximum (even when there is no log ⁡ 2 ​ T \log 2T or log ⁡ 2 ​ N \log 2N present). Our “Halász inequality for the primes” recovers this loss when 𝒯 \mathcal{T} is very small, which is enough for us. The proof relies on the duality principle, which we state below.

###### Lemma 10 (Duality principle).

Let 𝒳 = ( x m ​ n) \mathcal{X}=(x_{mn}) be a complex matrix and D ≥ 0 D\geq 0. The following two statements are equivalent:

- •

For any complex numbers a n a_{n}

 | ∑ m | ∑ n a n ​ x m ​ n | 2 ≤ D ​ ∑ n | a n | 2; \sum_{m}\left|\sum_{n}a_{n}x_{mn}\right|^{2}\leq D\sum_{n}|a_{n}|^{2}; |  |

- •

For any complex numbers b m b_{m}

 | ∑ n | ∑ m b m ​ x m ​ n | 2 ≤ D ​ ∑ m | b m | 2. \sum_{n}\left|\sum_{m}b_{m}x_{mn}\right|^{2}\leq D\sum_{m}|b_{m}|^{2}. |  |

###### Proof.

See [32, Chapter 7, Theorem 6, p. 134] ∎

###### Lemma 11 (Halász inequality for primes).

Let P ⁡ ( s) = ∑ P ≤ p ≤ 2 ​ P a p ​ p − s P(s)=\sum_{P\leq p\leq 2P}a_{p}p^{-s} be a Dirichlet polynomial whose coefficients are supported on the primes and let 𝒯 ⊂ [− T, T] \mathcal{T}\subset[-T,T] be a sequence of well-spaced points. Then

 | ∑ t ∈ 𝒯 | P ⁡ ( i ​ t) | 2 ≪ ( P + | 𝒯 | ​ P ​ exp ⁡ ( − log ⁡ P ( log ⁡ T) 2 / 3 + ε) ​ ( log ⁡ T) 2) ⋅ ∑ P ≤ p ≤ 2 ​ P | a p | 2 log ⁡ P. \sum_{t\in\mathcal{T}}|P(it)|^{2}\ll\left(P+|\mathcal{T}|P\exp\left(-\frac{\log P}{(\log T)^{2/3+\varepsilon}}\right)(\log T)^{2}\right)\cdot\sum_{P\leq p\leq 2P}\frac{|a_{p}|^{2}}{\log P}. |  |

###### Proof.

By the duality principle (Lemma 10) applied to ( p i ​ t) P ≤ p ≤ 2 ​ P, t ∈ 𝒯 (p^{it})_{P\leq p\leq 2P,t\in\mathcal{T}} it is enough to prove that

 | ∑ P ≤ p ≤ 2 ​ P log ⁡ p ​ | ∑ t ∈ 𝒯 η t ​ p i ​ t | 2 ≪ ( P + | 𝒯 | ​ P ​ exp ⁡ ( − log ⁡ P ( log ⁡ T) 2 / 3 + ε) ​ ( log ⁡ T) 2) ⋅ ∑ t ∈ 𝒯 | η t | 2 \sum_{P\leq p\leq 2P}\log p\left|\sum_{t\in\mathcal{T}}\eta_{t}p^{it}\right|^{2}\ll\left(P+|\mathcal{T}|P\exp\left(-\frac{\log P}{(\log T)^{2/3+\varepsilon}}\right)(\log T)^{2}\right)\cdot\sum_{t\in\mathcal{T}}|\eta_{t}|^{2} |  |

for any complex numbers η t \eta_{t}. Opening the square, we see that

 | ∑ P ≤ p ≤ 2 ​ P log ⁡ p ​ | ∑ t ∈ 𝒯 η t ​ p i ​ t | 2 \displaystyle\sum_{P\leq p\leq 2P}\log p\Big|\sum_{t\in\mathcal{T}}\eta_{t}p^{it}\Big|^{2} | ≤ ∑ p k log ⁡ p ​ | ∑ t ∈ 𝒯 η t ​ p k ​ i ​ t | 2 ​ f ​ ( p k P) \displaystyle\leq\sum_{p^{k}}\log p\Big|\sum_{t\in\mathcal{T}}\eta_{t}p^{kit}\Big|^{2}f\Big(\frac{p^{k}}{P}\Big) |  |

 |  | ≤ ∑ t, t ′ ∈ 𝒯 | η t ​ η t ′ | ​ | ∑ p k log ⁡ p ⋅ p k ​ i ​ ( t − t ′) ​ f ​ ( p k P) | \displaystyle\leq\sum_{t,t^{\prime}\in\mathcal{T}}|\eta_{t}\eta_{t^{\prime}}|\Big|\sum_{p^{k}}\log p\cdot p^{ki(t-t^{\prime})}f\Big(\frac{p^{k}}{P}\Big)\Big| |  |

where f ⁡ ( x) f(x) is a smooth compactly supported function such that f ⁡ ( x) = 1 f(x)=1 for 1 ≤ x ≤ 2 1\leq x\leq 2 and f f decays to zero outside of the interval [1, 2] [1,2]. Let f ~ \widetilde{f} denote the Mellin transform of f f. Then f ~ ( x + i y) ≪ A, B ( 1 + | y |) − B \widetilde{f}(x+iy)\ll_{A,B}(1+|y|)^{-B} uniformly in | x | ≤ A |x|\leq A. In addition,

(15) |  | ∑ n Λ ⁡ ( n) ​ n i ​ t \displaystyle\sum_{n}\Lambda(n)n^{it} | f ( n P) = − 1 2 ​ π ​ i ∫ 2 − i ​ ∞ 2 + i ​ ∞ f ~ ( s) ζ ′ ζ ( s − i t) P s s d s \displaystyle f\Big(\frac{n}{P}\Big)=-\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}\widetilde{f}(s)\frac{\zeta^{\prime}}{\zeta}(s-it)\frac{P^{s}}{s}ds |  |

We truncate the integral at | t | = T |t|=T, making a negligible error of O A ​ ( T − A) O_{A}(T^{-A}). In the remaining integral, we shift the contour to σ = 1 − c ( log T) − 2 / 3 + ε \sigma=1-c(\log T)^{-2/3+\varepsilon}, staying in the zero-free region of the ζ \zeta -function, and use the following bound there (see [19, formula (1.52)])

 | ζ ′ ζ ​ ( σ + i ​ t) = ∑ ϱ = β + i ​ γ | t − γ | < 1 1 σ + i ​ t − ϱ + O ⁡ ( log ⁡ ( | t | + 2)) ≪ ( log ⁡ T) 1 + 2 / 3 + ε \frac{\zeta^{\prime}}{\zeta}(\sigma+it)=\sum_{\begin{subarray}{c}\varrho=\beta+i\gamma\\ |t-\gamma|<1\end{subarray}}\frac{1}{\sigma+it-\varrho}+O(\log(|t|+2))\ll(\log T)^{1+2/3+\varepsilon} |  |

One readily checks this bound by noticing that there are O ⁡ ( log ⁡ T) O(\log T) zeros in the sum and they are ≫ ( log T) − 2 / 3 + ε \gg(\log T)^{-2/3+\varepsilon} away from the contour. It follows that ( 15) is equal to

 |  | f ~ ​ ( 1 + i ​ t) 1 + i ​ t ⋅ P 1 + i ​ t + O ⁡ ( P ​ exp ⁡ ( − log ⁡ P ( log ⁡ T) 2 / 3 + ε) ​ ( log ⁡ T) 2) \displaystyle\frac{\widetilde{f}(1+it)}{1+it}\cdot P^{1+it}+O\left(P\exp\left(-\frac{\log P}{(\log T)^{2/3+\varepsilon}}\right)(\log T)^{2}\right) |  |

Combining the above observations and using the inequality | η t ​ η t ′ | ≤ | η t | 2 + | η t ′ | 2 |\eta_{t}\eta_{t^{\prime}}|\leq|\eta_{t}|^{2}+|\eta_{t^{\prime}}|^{2} we obtain

 | ∑ P ≤ p ≤ 2 ​ P log ⁡ p ​ | ∑ t ∈ 𝒯 η t ​ p i ​ t | 2 ≪ ∑ t, t ′ ∈ 𝒯 | η t ​ η t ′ | ​ | ∑ p k log ⁡ p ⋅ p k ​ i ​ ( t − t ′) ​ f ​ ( p k P) | ≪ ∑ t, t ′ ∈ 𝒯 ( | η t | 2 + | η t ′ | 2) ​ ( | f ~ ​ ( 1 + i ⁡ ( t − t ′)) 1 + i ⁡ ( t − t ′) | ⋅ P + P ​ exp ⁡ ( − log ⁡ P ( log ⁡ T) 2 / 3 + ε) ​ ( log ⁡ T) 2) ≪ ( P + | 𝒯 | ​ P ​ exp ⁡ ( − log ⁡ P ( log ⁡ T) 2 / 3 + ε) ​ ( log ⁡ T) 2) ⋅ ∑ t ∈ 𝒯 | η t | 2 \begin{split}&\sum_{P\leq p\leq 2P}\log p\left|\sum_{t\in\mathcal{T}}\eta_{t}p^{it}\right|^{2}\\ &\ll\sum_{t,t^{\prime}\in\mathcal{T}}|\eta_{t}\eta_{t^{\prime}}|\Big|\sum_{p^{k}}\log p\cdot p^{ki(t-t^{\prime})}f\Big(\frac{p^{k}}{P}\Big)\Big|\\ &\ll\sum_{t,t^{\prime}\in\mathcal{T}}(|\eta_{t}|^{2}+|\eta_{t^{\prime}}|^{2})\left(\left|\frac{\widetilde{f}(1+i(t-t^{\prime}))}{1+i(t-t^{\prime})}\right|\cdot P+P\exp\left(-\frac{\log P}{(\log T)^{2/3+\varepsilon}}\right)(\log T)^{2}\right)\\ &\ll\Big(P+|\mathcal{T}|P\exp\left(-\frac{\log P}{(\log T)^{2/3+\varepsilon}}\right)(\log T)^{2}\Big)\cdot\sum_{t\in\mathcal{T}}|\eta_{t}|^{2}\end{split} |  |

since ∑ t ∈ 𝒯 | f ~ ​ ( 1 − i ⁡ ( t − t ′)) | = O ⁡ ( 1) \sum_{t\in\mathcal{T}}|\widetilde{f}(1-i(t-t^{\prime}))|=O(1). ∎

###### Remark.

On the Riemann Hypothesis one can replace P exp ( − log P / ( log T) 2 / 3 + ε) ( log T) 2 P\exp(-\log P/(\log T)^{2/3+\varepsilon})(\log T)^{2} in the above lemma by P 1 / 2 ​ log ⁡ P ​ log ⁡ T P^{1/2}\log P\log T.

## 5. Decomposition of Dirichlet polynomials

In this section we prove a technical version of the Buchstab decomposition ( 9). We are grateful to Terry Tao for pointing out that our “Buchstab decomposition” is a variant of Ramaré’s identity [8, Section 17.3].

###### Lemma 12.

Let H ≥ 1 H\geq 1 and Q ≥ P ≥ 1 Q\geq P\geq 1. Let a m, b m a_{m},b_{m} and c p c_{p} be bounded sequences such that a m ​ p = b m ​ c p a_{mp}=b_{m}c_{p} whenever p ∤ m p\nmid m and P ≤ p ≤ Q P\leq p\leq Q. Let

 | Q v, H ​ ( s) \displaystyle Q_{v,H}(s) | = ∑ P ≤ p ≤ Q e v / H ≤ p ≤ e ( v + 1) / H c p p s and \displaystyle=\sum_{\begin{subarray}{c}P\leq p\leq Q\\ e^{v/H}\leq p\leq e^{(v+1)/H}\end{subarray}}\frac{c_{p}}{p^{s}}\quad\text{and} |  |

 | R v, H ​ ( s) \displaystyle R_{v,H}(s) | = ∑ X e − v / H ≤ m ≤ 2 X e − v / H b m m s ⋅ 1 #{ P ≤ q ≤ Q: q | m, q ∈ ℙ } + 1 \displaystyle=\sum_{\begin{subarray}{c}Xe^{-v/H}\leq m\leq 2Xe^{-v/H}\end{subarray}}\frac{b_{m}}{m^{s}}\cdot\frac{1}{\#\{P\leq q\leq Q:q|m,q\in\mathbb{P}\}+1} |  |

and let 𝒯 ⊆ [− T, T] \mathcal{T}\subseteq[-T,T]. Then,

 | ∫ 𝒯 \displaystyle\int_{\mathcal{T}} | | ∑ X ≤ n ≤ 2 ​ X a n n 1 + i ​ t | 2 ​ 𝑑 t ≪ H ​ log ⁡ ( Q P) × ∑ j ∈ ℐ ∫ 𝒯 | Q j, H ​ ( 1 + i ​ t) ​ R j, H ​ ( 1 + i ​ t) | 2 ​ 𝑑 t \displaystyle\Big|\sum_{\begin{subarray}{c}X\leq n\leq 2X\end{subarray}}\frac{a_{n}}{n^{1+it}}\Big|^{2}dt\ll H\log\Big(\frac{Q}{P}\Big)\times\sum_{j\in\mathcal{I}}\int_{\mathcal{T}}\Big|Q_{j,H}(1+it)R_{j,H}(1+it)|^{2}dt |  |

 |  | + T + X X ​ ( 1 H + 1 P + ∑ X ≤ n ≤ 2 ​ X ( n, ∏ P ≤ p ≤ Q p) = 1 | a n | 2 n) \displaystyle+\frac{T+X}{X}\Bigg(\frac{1}{H}+\frac{1}{P}+\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ (n,\prod_{P\leq p\leq Q}p)=1\end{subarray}}\frac{|a_{n}|^{2}}{n}\Bigg) |  |

where ℐ \mathcal{I} is the interval ⌊ H ​ log ⁡ P ⌋ ≤ j ≤ H ​ log ⁡ Q \lfloor H\log P\rfloor\leq j\leq H\log Q.

###### Proof.

Let us write s = 1 + i ​ t s=1+it and notice that

(16) |  | ∑ X ≤ n ≤ 2 ​ X a n n s = ∑ P ≤ p ≤ Q \displaystyle\sum_{\begin{subarray}{c}X\leq n\leq 2X\end{subarray}}\frac{a_{n}}{n^{s}}=\sum_{P\leq p\leq Q} | ∑ X / p ≤ m ≤ 2 ​ X / p a p ​ m ( p ​ m) s ⋅ 1 #{ P ≤ q ≤ Q: q | m, q ∈ ℙ } + 𝟏 ( p, m) = 1 + ∑ X ≤ n ≤ 2 ​ X ( n, 𝒫) = 1 a n n s \displaystyle\sum_{\begin{subarray}{c}X/p\leq m\leq 2X/p\end{subarray}}\frac{a_{pm}}{(pm)^{s}}\cdot\frac{1}{\#\{P\leq q\leq Q:q|m,q\in\mathbb{P}\}+\mathbf{1}_{(p,m)=1}}+\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ (n,\mathcal{P})=1\end{subarray}}\frac{a_{n}}{n^{s}} |  |

where 𝒫 = ∏ P ≤ p ≤ Q p \mathcal{P}=\prod_{P\leq p\leq Q}p and 𝟏 ( p, m) = 1 \mathbf{1}_{(p,m)=1} is the indicator function of ( p, m) = 1 (p,m)=1. Notice that when p ∤ m p\nmid m, we can replace a p ​ m a_{pm} by b m ​ c p b_{m}c_{p}. Let also ω ( n; P, Q) = #{ P ≤ p ≤ Q: p | n } \omega(n;P,Q)=\#\{P\leq p\leq Q:p|n\}. This allows us to rewrite the first summand as

 | ∑ P ≤ p ≤ Q \displaystyle\sum_{P\leq p\leq Q} | c p p s ​ ∑ X / p ≤ m ≤ 2 ​ X / p b m m s ⋅ 1 ω ⁡ ( m, P, Q) + 1 \displaystyle\frac{c_{p}}{p^{s}}\sum_{\begin{subarray}{c}X/p\leq m\leq 2X/p\end{subarray}}\frac{b_{m}}{m^{s}}\cdot\frac{1}{\omega(m;P,Q)+1} |  |

 |  | + ∑ P ≤ p ≤ Q ∑ X / p ≤ m ≤ 2 ​ X / p p | m ( a p ​ m ω ⁡ ( m, P, Q) ⋅ 1 ( p ​ m) s − b m ​ c p ( p ​ m) s ⋅ 1 ω ⁡ ( m, P, Q) + 1). \displaystyle+\sum_{P\leq p\leq Q}\sum_{\begin{subarray}{c}X/p\leq m\leq 2X/p\\ p\mid m\end{subarray}}\Big(\frac{a_{pm}}{\omega(m;P,Q)}\cdot\frac{1}{(pm)^{s}}-\frac{b_{m}c_{p}}{(pm)^{s}}\cdot\frac{1}{\omega(m;P,Q)+1}\Big). |  |

We split the first sum further into dyadic ranges getting that it is

 | ∑ j ∈ ℐ ∑ e j / H ≤ p < e ( j + 1) / H P ≤ p ≤ Q c p p s ​ ∑ X e − ( j + 1) / H ≤ m ≤ 2 X e − j / H X ≤ m ​ p ≤ 2 ​ X b m m s ⋅ 1 ω ⁡ ( m, P, Q) + 1 \sum_{j\in\mathcal{I}}\ \sum_{\begin{subarray}{c}e^{j/H}\leq p<e^{(j+1)/H}\\ P\leq p\leq Q\end{subarray}}\frac{c_{p}}{p^{s}}\ \sum_{\begin{subarray}{c}Xe^{-(j+1)/H}\leq m\leq 2Xe^{-j/H}\\ X\leq mp\leq 2X\end{subarray}}\frac{b_{m}}{m^{s}}\cdot\frac{1}{\omega(m;P,Q)+1} |  |

We remove the condition X ≤ m ​ p ≤ 2 ​ X X\leq mp\leq 2X overcounting at most by the integers m ​ p mp in the ranges [X e − 1 / H, X] [Xe^{-1/H},X] and [2 ​ X, 2 ​ X ​ e 1 / H] [2X,2Xe^{1/H}]. Similarly, removing numbers with X e − ( j + 1) / H ≤ m ≤ X e − j / H Xe^{-(j+1)/H}\leq m\leq Xe^{-j/H} we undercount at most by integers m ​ p mp in the range [X e − 1 / H, X e 1 / H] [Xe^{-1/H},Xe^{1/H}]. Therefore we can, for some bounded d m d_{m}, rewrite ( 16) as

 | ∑ j ∈ ℐ \displaystyle\sum_{j\in\mathcal{I}} | Q j, H ​ ( s) ​ R j, H ​ ( s) + ∑ X e − 1 / H ≤ m ≤ X e 1 / H d m m s + ∑ 2 ​ X ≤ m ≤ 2 ​ X ​ e 1 / H d m m s \displaystyle Q_{j,H}(s)R_{j,H}(s)+\sum_{\begin{subarray}{c}Xe^{-1/H}\leq m\leq Xe^{1/H}\end{subarray}}\frac{d_{m}}{m^{s}}+\sum_{\begin{subarray}{c}2X\leq m\leq 2Xe^{1/H}\end{subarray}}\frac{d_{m}}{m^{s}} |  |

 |  | + ∑ P ≤ p ≤ Q ∑ X / p 2 ≤ m ≤ 2 ​ X / p 2 ( a p 2 ​ m ω ⁡ ( m ​ p, P, Q) ⋅ 1 ( p 2 ​ m) s − c p ​ b p ​ m ω ⁡ ( m ​ p, P, Q) + 1 ⋅ 1 ( p 2 ​ m) s) + ∑ X ≤ n ≤ 2 ​ X ( n, 𝒫) = 1 a n n s \displaystyle+\sum_{P\leq p\leq Q}\sum_{\begin{subarray}{c}X/p^{2}\leq m\leq 2X/p^{2}\end{subarray}}\Big(\frac{a_{p^{2}m}}{\omega(mp;P,Q)}\cdot\frac{1}{(p^{2}m)^{s}}-\frac{c_{p}b_{pm}}{\omega(mp;P,Q)+1}\cdot\frac{1}{(p^{2}m)^{s}}\Big)+\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ (n,\mathcal{P})=1\end{subarray}}\frac{a_{n}}{n^{s}} |  |

We square this, integrate over 𝒯 \mathcal{T} and then apply Cauchy-Schwarz on the first sum over j j and the mean-value theorem (Lemma 6) on the remaining sums. This gives the result since it is easily seen that the later mean-values are bounded by the stated quantities. ∎

## 6. Moment computation

In this section we prove a lemma which allows us to compute the second moment of the Dirichlet polynomial in ( 11). Let us first introduce some relevant notation. Let Y 1, Y 2 ≥ 1 Y_{1},Y_{2}\geq 1, and consider,

 | Q ⁡ ( s) = ∑ Y 1 ≤ p ≤ 2 ​ Y 1 c p p s and A ⁡ ( s) = ∑ X / Y 2 ≤ m ≤ 2 ​ X / Y 2 a m m s Q(s)=\sum_{Y_{1}\leq p\leq 2Y_{1}}\frac{c_{p}}{p^{s}}\quad\text{and}\quad A(s)=\sum_{\begin{subarray}{c}X/Y_{2}\leq m\leq 2X/Y_{2}\end{subarray}}\frac{a_{m}}{m^{s}} |  |

with coefficients | a m |, | c p | ≤ 1 |a_{m}|,|c_{p}|\leq 1.

###### Lemma 13.

Let ℓ = ⌈ log ⁡ Y 2 log ⁡ Y 1 ⌉ \ell=\lceil\frac{\log Y_{2}}{\log Y_{1}}\rceil. Then

 | ∫ − T T | Q ( 1 + i t) ℓ ⋅ A ( 1 + i t) | 2 d t ≪ ( T X + 2 ℓ Y 1) ⋅ ( ℓ + 1)! 2 \int_{-T}^{T}|Q(1+it)^{\ell}\cdot A(1+it)|^{2}dt\ll\Big(\frac{T}{X}+2^{\ell}Y_{1}\Big)\cdot(\ell+1)!^{2} |  |

###### Proof.

The coefficients of the Dirichlet polynomial Q ​ ( s) ℓ ​ A ​ ( s) Q(s)^{\ell}A(s) are supported on the interval

 | [Y 1 ℓ ⋅ X / Y 2, ( 2 ​ Y 1) ℓ ⋅ 2 ​ X / Y 2] ⊆ [X, 2 ℓ + 1 ​ Y 1 ​ X] [Y_{1}^{\ell}\cdot X/Y_{2},(2Y_{1})^{\ell}\cdot 2X/Y_{2}]\subseteq[X,2^{\ell+1}Y_{1}X] |  |

Using the mean-value theorem for Dirichlet polynomials (Lemma 6) we see that

 | ∫ − T T | Q ​ ( 1 + i ​ t) ℓ ⋅ A ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t ≪ ( T + 2 ℓ ​ Y 1 ​ X) ​ ∑ X ≤ n ≤ 2 ℓ + 1 ​ Y 1 ​ X 1 n 2 ⋅ ( ∑ n = m ​ p 1 ​ … ​ p ℓ Y 1 ≤ p 1, …, p ℓ ≤ 2 ​ Y 1 X / Y 2 ≤ m ≤ 2 ​ X / Y 2 1) 2. \int_{-T}^{T}|Q(1+it)^{\ell}\cdot A(1+it)|^{2}dt\ll(T+2^{\ell}Y_{1}X)\sum_{X\leq n\leq 2^{\ell+1}Y_{1}X}\frac{1}{n^{2}}\cdot\Bigg(\sum_{\begin{subarray}{c}n=mp_{1}\ldots p_{\ell}\\ Y_{1}\leq p_{1},\ldots,p_{\ell}\leq 2Y_{1}\\ X/Y_{2}\leq m\leq 2X/Y_{2}\end{subarray}}1\Bigg)^{2}. |  |

Here

 | ∑ n = m ​ p 1 ​ … ​ p ℓ Y 1 ≤ p 1, …, p ℓ ≤ 2 ​ Y 1 X / Y 2 ≤ m ≤ 2 ​ X / Y 2 1 ≤ ℓ! ⋅ ∑ n = m ​ r p | r ⟹ Y 1 ≤ p ≤ 2 ​ Y 1 1 =: ℓ! ⋅ g ⁡ ( n), \sum_{\begin{subarray}{c}n=mp_{1}\ldots p_{\ell}\\ Y_{1}\leq p_{1},\ldots,p_{\ell}\leq 2Y_{1}\\ X/Y_{2}\leq m\leq 2X/Y_{2}\end{subarray}}1\leq\ell!\cdot\sum_{\begin{subarray}{c}n=mr\\ p\mid r\implies Y_{1}\leq p\leq 2Y_{1}\end{subarray}}1=:\ell!\cdot g(n), |  |

say, where g g is multiplicative and

 | g ⁡ ( p k) = { ( k + 1) if Y 1 ≤ p ≤ 2 ​ Y 1; 1 otherwise. g(p^{k})=\begin{cases}(k+1)&\text{if $Y_{1}\leq p\leq 2Y_{1}$;}\\ 1&\text{otherwise.}\end{cases} |  |

With this notation

(17) |  | ∫ − T T | Q ( 1 + i t) ℓ ⋅ A ( 1 + i t) | 2 ≪ ( T + 2 ℓ Y 1 X) ℓ! 2 ∑ X ≤ n ≤ 2 ℓ + 1 ​ Y 1 ​ X g ​ ( n) 2 n 2. \int_{-T}^{T}|Q(1+it)^{\ell}\cdot A(1+it)|^{2}\ll(T+2^{\ell}Y_{1}X)\ell!^{2}\sum_{X\leq n\leq 2^{\ell+1}Y_{1}X}\frac{g(n)^{2}}{n^{2}}. |  |

By Shiu’s bound [36, Theorem 1] for sums of positive-valued multiplicative functions we have, for any Y ≥ 2 Y\geq 2,

(18) |  | ∑ Y ≤ n ≤ 2 ​ Y g ​ ( n) 2 ≪ Y ​ ∏ p ≤ Y ( 1 + | g ⁡ ( p) | 2 − 1 p) ≪ Y. \sum_{Y\leq n\leq 2Y}g(n)^{2}\ll Y\prod_{p\leq Y}\left(1+\frac{|g(p)|^{2}-1}{p}\right)\ll Y. |  |

The claim follows by splitting the sum over n n in ( 17) into sums over dyadic intervals and applying ( 18) to each of them. ∎

## 7. Parseval bound

The following lemma shows that the behavior of a multiplicative function in almost all very short intervals can be approximated by its behavior on a long interval if the mean square of the corresponding Dirichlet polynomial is small. This is in the spirit of previous work on primes in almost all intervals, see for instance [14, Lemma 9.3].

###### Lemma 14.

Let | a m | ≤ 1 |a_{m}|\leq 1. Assume 1 ≤ h 1 ≤ h 2 = X / ( log ⁡ X) 1 / 5 1\leq h_{1}\leq h_{2}=X/(\log X)^{1/5}. Consider, for X ≤ x ≤ 2 ​ X X\leq x\leq 2X,

 | S j ​ ( x) = ∑ x ≤ m ≤ x + h j a m and write A ⁡ ( s):= ∑ X ≤ m ≤ 4 ​ X a m m s. S_{j}(x)=\sum_{\begin{subarray}{c}x\leq m\leq x+h_{j}\end{subarray}}a_{m}\quad\text{and write}\quad A(s):=\sum_{\begin{subarray}{c}X\leq m\leq 4X\end{subarray}}\frac{a_{m}}{m^{s}}. |  |

Then

 | 1 X ​ ∫ X 2 ​ X | 1 h 1 ​ S 1 ​ ( x) − 1 h 2 ​ S 2 ​ ( x) | 2 ​ 𝑑 x ≪ 1 ( log ⁡ X) 2 / 15 + ∫ 1 + i ​ ( log ⁡ X) 1 / 15 1 + i ​ X / h 1 | A ⁡ ( s) | 2 ​ | d s | + max T ≥ X / h 1 ⁡ X / h 1 T ​ ∫ 1 + i ​ T 1 + i ​ 2 ​ T | A ⁡ ( s) | 2 ​ | d s |. \begin{split}&\frac{1}{X}\int_{X}^{2X}\left|\frac{1}{h_{1}}S_{1}(x)-\frac{1}{h_{2}}S_{2}(x)\right|^{2}dx\\ &\ll\frac{1}{(\log X)^{2/15}}+\int_{1+i(\log X)^{1/15}}^{1+iX/h_{1}}\left|A(s)\right|^{2}|ds|+\max_{T\geq X/h_{1}}\frac{X/h_{1}}{T}\int_{1+iT}^{1+i2T}\left|A(s)\right|^{2}|ds|.\end{split} |  |

###### Proof.

By Perron’s formula

 | S j ​ ( x) = 1 2 ​ π ​ i ​ ∫ 1 − i ​ ∞ 1 + i ​ ∞ A ⁡ ( s) ​ ( x + h j) s − x s s ​ d s. \begin{split}S_{j}(x)&=\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}A(s)\frac{(x+h_{j})^{s}-x^{s}}{s}ds.\end{split} |  |

Let us split the integral in S j ​ ( x) S_{j}(x) into two parts U j ​ ( x) U_{j}(x) and V j ​ ( x) V_{j}(x) according to whether | t | ≤ T 0:= ( log ⁡ X) 1 / 15 |t|\leq T_{0}:=(\log X)^{1/15} or not. In U j ​ ( x) U_{j}(x) we write

 | ( x + h j) s − x s s = x s ​ ( 1 + h j x) s − 1 s = x s ​ ( h j x + O ⁡ ( T 0 ​ ( h j X) 2)), \frac{(x+h_{j})^{s}-x^{s}}{s}=x^{s}\frac{\left(1+\frac{h_{j}}{x}\right)^{s}-1}{s}=x^{s}\left(\frac{h_{j}}{x}+O\left(T_{0}\left(\frac{h_{j}}{X}\right)^{2}\right)\right), |  |

and get

 | U j ( x) = h j x ⋅ 1 2 ​ π ​ i ∫ 1 − i ​ T 0 1 + i ​ T 0 A ( s) x s d s + O ( T 0 2 ⋅ x ( h j X) 2), U_{j}(x)=\frac{h_{j}}{x}\cdot\frac{1}{2\pi i}\int_{1-iT_{0}}^{1+iT_{0}}A(s)x^{s}ds+O\left(T_{0}^{2}\cdot x\left(\frac{h_{j}}{X}\right)^{2}\right), |  |

so that

 | 1 h 1 ​ U 1 ​ ( x) − 1 h 2 ​ U 2 ​ ( x) ≪ T 0 2 ​ x ​ h 2 X 2 ≪ 1 ( log ⁡ X) 1 / 15. \frac{1}{h_{1}}U_{1}(x)-\frac{1}{h_{2}}U_{2}(x)\ll T_{0}^{2}x\frac{h_{2}}{X^{2}}\ll\frac{1}{(\log X)^{1/15}}. |  |

Hence it is enough to consider, for j = 1, 2 j=1,2,

 | 1 X ​ ∫ X 2 ​ X ( | V j ​ ( x) | h j) 2 ​ d x ≪ 1 h j 2 ​ X ​ ∫ X 2 ​ X | ∫ 1 + i ​ T 0 1 + i ​ ∞ A ⁡ ( s) ​ ( x + h j) s − x s s ​ d s | 2 ​ d x. \begin{split}&\frac{1}{X}\int_{X}^{2X}\left(\frac{|V_{j}(x)|}{h_{j}}\right)^{2}dx\ll\frac{1}{h_{j}^{2}X}\int_{X}^{2X}\left|\int_{1+iT_{0}}^{1+i\infty}A(s)\frac{(x+h_{j})^{s}-x^{s}}{s}ds\right|^{2}dx.\end{split} |  |

We would like to add a smoothing, take out a factor x s x^{s}, expand the square, exchange the order of integration and integrate over x x. However, the term ( x + h j) s (x+h_{j})^{s} prevents us from doing this and we overcome this problem in a similar way to [35, Page 25]. We write

 | ( x + h j) s − x s s = 1 2 ​ h j ​ ( ∫ h j 3 ​ h j ( x + w) s − x s s ​ d w − ∫ h j 3 ​ h j ( x + w) s − ( x + h j) s s ​ d w) = x 2 ​ h j ​ ∫ h j / x 3 ​ h j / x x s ​ ( 1 + u) s − 1 s ​ d u − x + h j 2 ​ h j ​ ∫ 0 2 ​ h j / ( x + h j) ( x + h j) s ​ ( 1 + u) s − 1 s ​ d u. \begin{split}&\frac{(x+h_{j})^{s}-x^{s}}{s}=\frac{1}{2h_{j}}\left(\int_{h_{j}}^{3h_{j}}\frac{(x+w)^{s}-x^{s}}{s}dw-\int_{h_{j}}^{3h_{j}}\frac{(x+w)^{s}-(x+h_{j})^{s}}{s}dw\right)\\ &=\frac{x}{2h_{j}}\int_{h_{j}/x}^{3h_{j}/x}x^{s}\frac{(1+u)^{s}-1}{s}du-\frac{x+h_{j}}{2h_{j}}\int_{0}^{2h_{j}/(x+h_{j})}(x+h_{j})^{s}\frac{(1+u)^{s}-1}{s}du.\end{split} |  |

where we have substituted w = x ⋅ u w=x\cdot u in the first integral and w = h j + ( x + h j) ​ u w=h_{j}+(x+h_{j})u in the second integral. Let us only study the first summand, the second one being handled completely similarly. Thus we assume that

 | 1 X ​ ∫ X 2 ​ X ( | V j ​ ( x) | h j) 2 ​ 𝑑 x ≪ X h j 4 ​ ∫ X 2 ​ X | ∫ h j / x 3 ​ h j / x ∫ 1 + i ​ T 0 1 + i ​ ∞ A ⁡ ( s) ​ x s ​ ( 1 + u) s − 1 s ​ 𝑑 s ​ 𝑑 u | 2 ​ 𝑑 x ≪ 1 h j 3 ​ ∫ h j / ( 2 ​ X) 3 ​ h j / X ∫ X 2 ​ X | ∫ 1 + i ​ T 0 1 + i ​ ∞ A ⁡ ( s) ​ x s ​ ( 1 + u) s − 1 s ​ 𝑑 s | 2 ​ 𝑑 x ​ 𝑑 u ≪ 1 h j 2 ​ X ​ ∫ X 2 ​ X | ∫ 1 + i ​ T 0 1 + i ​ ∞ A ⁡ ( s) ​ x s ​ ( 1 + u) s − 1 s ​ 𝑑 s | 2 ​ 𝑑 x \begin{split}\frac{1}{X}\int_{X}^{2X}\left(\frac{|V_{j}(x)|}{h_{j}}\right)^{2}dx&\ll\frac{X}{h_{j}^{4}}\int_{X}^{2X}\left|\int_{h_{j}/x}^{3h_{j}/x}\int_{1+iT_{0}}^{1+i\infty}A(s)x^{s}\frac{(1+u)^{s}-1}{s}dsdu\right|^{2}dx\\ &\ll\frac{1}{h_{j}^{3}}\int_{h_{j}/(2X)}^{3h_{j}/X}\int_{X}^{2X}\left|\int_{1+iT_{0}}^{1+i\infty}A(s)x^{s}\frac{(1+u)^{s}-1}{s}ds\right|^{2}dxdu\\ &\ll\frac{1}{h_{j}^{2}X}\int_{X}^{2X}\left|\int_{1+iT_{0}}^{1+i\infty}A(s)x^{s}\frac{(1+u)^{s}-1}{s}ds\right|^{2}dx\end{split} |  |

for some u ≪ h j / X u\ll h_{j}/X.

Let us introduce a smooth function g ⁡ ( x) g(x) supported on [1 / 2, 4] [1/2,4] and equal to 1 1 on [1, 2] [1,2]. We obtain

 |  | 1 X ​ ∫ X 2 ​ X ( | V j ​ ( x) | h j) 2 ​ 𝑑 x ≪ 1 h j 2 ​ X ​ ∫ g ⁡ ( x X) ​ | ∫ 1 + i ​ T 0 1 + i ​ ∞ A ⁡ ( s) ​ x s ​ ( 1 + u) s − 1 s ​ 𝑑 s | 2 ​ 𝑑 x \displaystyle\frac{1}{X}\int_{X}^{2X}\left(\frac{|V_{j}(x)|}{h_{j}}\right)^{2}dx\ll\frac{1}{h_{j}^{2}X}\int g\Big(\frac{x}{X}\Big)\left|\int_{1+iT_{0}}^{1+i\infty}A(s)x^{s}\frac{(1+u)^{s}-1}{s}ds\right|^{2}dx |  |

 |  | ≤ 1 h j 2 ​ X ​ ∫ 1 + i ​ T 0 1 + i ​ ∞ ∫ 1 + i ​ T 0 1 + i ​ ∞ | A ⁡ ( s 1) ​ A ​ ( s 2) ​ ( 1 + u) s 1 − 1 s 1 ​ ( 1 + u) s 2 − 1 s 2 | ​ | ∫ g ⁡ ( x X) ​ x s 1 + s 2 ¯ ​ 𝑑 x | ​ | d ​ s 1 ​ d ​ s 2 | \displaystyle\leq\frac{1}{h_{j}^{2}X}\int_{1+iT_{0}}^{1+i\infty}\int_{1+iT_{0}}^{1+i\infty}\left|A(s_{1})A(s_{2})\frac{(1+u)^{s_{1}}-1}{s_{1}}\frac{(1+u)^{s_{2}}-1}{s_{2}}\right|\left|\int g\Big(\frac{x}{X}\Big)x^{s_{1}+\overline{s_{2}}}dx\right||ds_{1}ds_{2}| |  |

 |  | ≪ 1 h j 2 ​ X ​ ∫ 1 + i ​ T 0 1 + i ​ ∞ ∫ 1 + i ​ T 0 1 + i ​ ∞ | A ⁡ ( s 1) ​ A ​ ( s 2) ​ | min ⁡ { h j X, 1 | t 1 | } ​ min ​ { h j X, 1 | t 2 | } ​ X 3 | t 1 − t 2 | 2 + 1 | ​ d ​ s 1 ​ d ​ s 2 | \displaystyle\ll\frac{1}{h_{j}^{2}X}\int_{1+iT_{0}}^{1+i\infty}\int_{1+iT_{0}}^{1+i\infty}|A(s_{1})A(s_{2})|\min\left\{\frac{h_{j}}{X},\frac{1}{|t_{1}|}\right\}\min\left\{\frac{h_{j}}{X},\frac{1}{|t_{2}|}\right\}\frac{X^{3}}{|t_{1}-t_{2}|^{2}+1}|ds_{1}ds_{2}| |  |

 |  | ≪ X 2 h j 2 ​ ∫ 1 + i ​ T 0 1 + i ​ ∞ ∫ 1 + i ​ T 0 1 + i ​ ∞ | A ⁡ ( s 1) | 2 ​ min ​ { ( h j / X) 2, | t 1 | − 2 } + | A ⁡ ( s 2) | 2 ​ min ​ { ( h j / X) 2, | t 2 | − 2 } | t 1 − t 2 | 2 + 1 ​ | d ​ s 1 ​ d ​ s 2 | \displaystyle\ll\frac{X^{2}}{h_{j}^{2}}\int_{1+iT_{0}}^{1+i\infty}\int_{1+iT_{0}}^{1+i\infty}\frac{|A(s_{1})|^{2}\min\{(h_{j}/X)^{2},|t_{1}|^{-2}\}+|A(s_{2})|^{2}\min\{(h_{j}/X)^{2},|t_{2}|^{-2}\}}{|t_{1}-t_{2}|^{2}+1}|ds_{1}ds_{2}| |  |

 |  | ≪ ∫ 1 + i ​ T 0 1 + i ​ X / h j | A ⁡ ( s) | 2 ​ | 𝑑 s | + X 2 h j 2 ​ ∫ 1 + i ​ X / h j 1 + i ​ ∞ | A ⁡ ( s) | 2 | t | 2 ​ | 𝑑 s |. \displaystyle\ll\int_{1+iT_{0}}^{1+iX/h_{j}}|A(s)|^{2}|ds|+\frac{X^{2}}{h_{j}^{2}}\int_{1+iX/h_{j}}^{1+i\infty}\frac{|A(s)|^{2}}{|t|^{2}}|ds|. |  |

The second summand is

(19) |  | ≪ X 2 h j 2 ∫ 1 + i ​ X / ( 2 ​ h j) 1 + i ​ ∞ 1 T 3 ∫ 1 + i ​ T 1 + i ​ 2 ​ T | A ( s) | 2 | d s | d T ≪ X 2 h j 2 ⋅ 1 X / h j max T ≥ X / ( 2 ​ h j) 1 T ∫ 1 + i ​ T 1 + i ​ 2 ​ T | A ( s) | 2 | d s | \ll\frac{X^{2}}{h_{j}^{2}}\int_{1+iX/(2h_{j})}^{1+i\infty}\frac{1}{T^{3}}\int_{1+iT}^{1+i2T}|A(s)|^{2}|ds|dT\ll\frac{X^{2}}{h_{j}^{2}}\cdot\frac{1}{X/h_{j}}\max_{T\geq X/(2h_{j})}\frac{1}{T}\int_{1+iT}^{1+i2T}|A(s)|^{2}|ds| |  |

so that

 | 1 X ​ ∫ X 2 ​ X ( | V j ​ ( x) | h j) 2 ​ d x ≪ ∫ 1 + i ​ T 0 1 + i ​ X / h j | A ⁡ ( s) | 2 ​ | d s | + X h j ​ max T ≥ X / h j ​ 1 T ​ ∫ 1 + i ​ T 1 + i ​ 2 ​ T | A ⁡ ( s) | 2 ​ | d s |. \begin{split}&\frac{1}{X}\int_{X}^{2X}\left(\frac{|V_{j}(x)|}{h_{j}}\right)^{2}dx\ll\int_{1+iT_{0}}^{1+iX/h_{j}}|A(s)|^{2}|ds|+\frac{X}{h_{j}}\max_{T\geq X/h_{j}}\frac{1}{T}\int_{1+iT}^{1+i2T}|A(s)|^{2}|ds|.\end{split} |  |

Since h 2 ≥ h 1 h_{2}\geq h_{1} the expression on the right hand side with j = 2 j=2 is always smaller than the same expression with j = 1 j=1, and the claim follows. ∎

## 8. The main proposition

By Lemma 14, Theorem 3 will essentially follow from the following proposition.

###### Proposition 1.

Let f: ℕ → [− 1, 1] f:\mathbb{N}\rightarrow[-1,1] be a multiplicative function. Let 𝒮 \mathcal{S} be a set of integers as defined in Section 2. Let

 | F ⁡ ( s) = ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) n s. F(s)=\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{s}}. |  |

Then, for any T T,

 | ∫ ( log ⁡ X) 1 / 15 T | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t ≪ ( T X / Q 1 + 1) ​ ( ( log ⁡ Q 1) 1 / 3 P 1 1 / 6 − η + 1 ( log ⁡ X) 1 / 50). \int_{(\log X)^{1/15}}^{T}\left|F(1+it)\right|^{2}dt\ll\left(\frac{T}{X/Q_{1}}+1\right)\left(\frac{(\log Q_{1})^{1/3}}{P_{1}^{1/6-\eta}}+\frac{1}{(\log X)^{1/50}}\right). |  |

###### Remark.

The “trivial bound” for ∫ 0 T | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t \int_{0}^{T}|F(1+it)|^{2}dt, obtained by applying a standard mean-value theorem (Lemma 6), is T / X + 1 T/X+1.

###### Proof.

Since the mean value theorem gives the bound O ⁡ ( T X + 1) O(\frac{T}{X}+1), we can assume T ≤ X T\leq X.

Pick a sequence α j \alpha_{j} for 1 ≤ j ≤ J 1\leq j\leq J with

(20) |  | α j = 1 4 − η ⁡ ( 1 + 1 2 ​ j), \alpha_{j}=\frac{1}{4}-\eta\left(1+\frac{1}{2j}\right), |  |

where η ∈ ( 0, 1 / 6) \eta\in(0,1/6) is such that ( 2) and ( 3) hold. Notice that

 | 1 4 − 3 2 ​ η = α 1 ≤ α 2 ≤ … ≤ α J ≤ 1 4 − η. \frac{1}{4}-\frac{3}{2}\eta=\alpha_{1}\leq\alpha_{2}\leq\dotsc\leq\alpha_{J}\leq\frac{1}{4}-\eta. |  |

We now split into several cases. Let

 | Q v, H j ​ ( s):= ∑ P j ≤ q ≤ Q j e v / H j ≤ q ≤ e ( v + 1) / H j f ⁡ ( q) q s, where H j:= j 2 ​ P 1 1 / 6 − η ( log ⁡ Q 1) 1 / 3. Q_{v,H_{j}}(s):=\sum_{\begin{subarray}{c}P_{j}\leq q\leq Q_{j}\\ e^{v/H_{j}}\leq q\leq e^{(v+1)/H_{j}}\end{subarray}}\frac{f(q)}{q^{s}},\quad\text{where}\quad H_{j}:=j^{2}\frac{P_{1}^{1/6-\eta}}{(\log Q_{1})^{1/3}}. |  |

Notice that this can be non-zero only when

 | v ∈ ℐ j:= { v: ⌊ H j ​ log ⁡ P j ⌋ ≤ v ≤ H j ​ log ⁡ Q j } v\in\mathcal{I}_{j}:=\{v:\lfloor H_{j}\log P_{j}\rfloor\leq v\leq H_{j}\log Q_{j}\} |  |

We write

 | [T 0, T] = ⋃ j = 1 J 𝒯 j ∪ 𝒰, T 0 = ( log ⁡ X) 1 / 15 [T_{0},T]=\bigcup_{j=1}^{J}\mathcal{T}_{j}\cup\mathcal{U}\ ,\ T_{0}=(\log X)^{1/15} |  |

as a disjoint union where t ∈ 𝒯 j t\in\mathcal{T}_{j} when j j is the smallest index such that

(21) |  | for all v ∈ ℐ j: | Q v, H j ( 1 + i t) | ≤ e − α j v / H j \text{for all }v\in\mathcal{I}_{j}:|Q_{v,H_{j}}(1+it)|\leq e^{-\alpha_{j}v/H_{j}} |  |

and t ∈ 𝒰 t\in\mathcal{U} if this does not hold for any j j.

Let us first consider the integrals over the sets 𝒯 j \mathcal{T}_{j}. Let

 | R v, H j ( s) = ∑ X e − v / H j ≤ m ≤ 2 X e − v / H j m ∈ 𝒮 j f ⁡ ( m) m s ⋅ 1 #{ P j ≤ p ≤ Q j: p | m } + 1 R_{v,H_{j}}(s)=\sum_{\begin{subarray}{c}Xe^{-v/H_{j}}\leq m\leq 2Xe^{-v/H_{j}}\\ m\in\mathcal{S}_{j}\end{subarray}}\frac{f(m)}{m^{s}}\cdot\frac{1}{\#\{P_{j}\leq p\leq Q_{j}:p|m\}+1} |  |

where 𝒮 j \mathcal{S}_{j} is the set of those integers which have at least one prime factor in every interval [P i, Q i] [P_{i},Q_{i}] with i ≠ j i\neq j and i ≤ J i\leq J (and possibly but not necessarily some prime factors in [P j, Q j] [P_{j},Q_{j}]). Using Lemma 12 with H = H j H=H_{j}, P = P j, Q = Q j P=P_{j},Q=Q_{j} and a m = f ⁡ ( m) ​ 𝟏 𝒮 a_{m}=f(m)\mathbf{1}_{\mathcal{S}}, c p = f ⁡ ( p) c_{p}=f(p), b m = f ⁡ ( m) ​ 𝟏 𝒮 j b_{m}=f(m)\mathbf{1}_{\mathcal{S}_{j}} (where 𝟏 A \mathbf{1}_{A} is the indicator function of the set A A), we see that

 | ∫ 𝒯 j | F ( 1 + i t) | 2 d t ≪ H j ⋅ log Q j ∑ v ∈ ℐ j ∫ 𝒯 j | Q v, H j ( 1 + i t) R v, H j ( 1 + i t) | 2 d t + 1 H j + 1 P j. \displaystyle\int_{\mathcal{T}_{j}}|F(1+it)|^{2}dt\ll H_{j}\cdot\log Q_{j}\sum_{v\in\mathcal{I}_{j}}\int_{\mathcal{T}_{j}}|Q_{v,H_{j}}(1+it)R_{v,H_{j}}(1+it)|^{2}dt+\frac{1}{H_{j}}+\frac{1}{P_{j}}. |  |

Here the second and third terms contribute in total to integrals over all 𝒯 j \mathcal{T}_{j}

 | ≪ ∑ j = 1 J ( 1 H j + 1 P j) ≪ ( log ⁡ Q 1) 1 / 3 P 1 1 / 6 − η. \ll\sum_{j=1}^{J}\left(\frac{1}{H_{j}}+\frac{1}{P_{j}}\right)\ll\frac{(\log Q_{1})^{1/3}}{P_{1}^{1/6-\eta}}. |  |

since P j ≥ P 1 j 2 P_{j}\geq P_{1}^{j^{2}} by ( 3). We can thus concentrate, for 1 ≤ j ≤ J 1\leq j\leq J, on bounding

(22) |  | E j:= H j ​ log ⁡ Q j ⋅ ∑ v ∈ ℐ j ∫ 𝒯 j | Q v, H j ​ ( 1 + i ​ t) ​ R v, H j ​ ( 1 + i ​ t) | 2 ​ 𝑑 t. \displaystyle E_{j}:=H_{j}\log Q_{j}\cdot\sum_{v\in\mathcal{I}_{j}}\int_{\mathcal{T}_{j}}|Q_{v,H_{j}}(1+it)R_{v,H_{j}}(1+it)|^{2}dt. |  |

By the definition of the set 𝒯 j \mathcal{T}_{j} we have | Q v, H j ( 1 + i t) | ≤ e − α j v / H j |Q_{v,H_{j}}(1+it)|\leq e^{-\alpha_{j}v/H_{j}} for t ∈ 𝒯 j t\in\mathcal{T}_{j}. Therefore, for 1 ≤ j ≤ J 1\leq j\leq J,

(23) |  | E j ≪ H j log Q j ⋅ ∑ v ∈ ℐ j e − 2 α j v / H j ∫ 𝒯 j | R v, H j ( 1 + i t) | 2 d t. E_{j}\ll H_{j}\log Q_{j}\cdot\sum_{v\in\mathcal{I}_{j}}e^{-2\alpha_{j}v/H_{j}}\int_{\mathcal{T}_{j}}|R_{v,H_{j}}(1+it)|^{2}dt. |  |

Recalling that [T 0, T] = 𝒯 1 ∪ 𝒯 2 ∪ … ∪ 𝒯 J ∪ 𝒰 [T_{0},T]=\mathcal{T}_{1}\cup\mathcal{T}_{2}\cup\ldots\cup\mathcal{T}_{J}\cup\mathcal{U} (with T 0 = ( log ⁡ X) 1 / 15 T_{0}=(\log X)^{1/15}) we see that

(24) |  | ∫ T 0 T | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t ≪ E 1 + E 2 + … + E J + ∫ 𝒰 | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t \int_{T_{0}}^{T}|F(1+it)|^{2}dt\ll E_{1}+E_{2}+\ldots+E_{J}+\int_{\mathcal{U}}|F(1+it)|^{2}dt |  |

We will now proceed as follows: In section 8.1 we bound E 1 E_{1}, in section 8.2 we bound E i E_{i} with 2 ≤ i ≤ J 2\leq i\leq J, and finally in section 8.3 we obtain a bound for ∫ 𝒰 | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t \int_{\mathcal{U}}|F(1+it)|^{2}dt.

### 8.1. Bounding E 1 E_{1}

If j = 1 j=1, then by the mean-value theorem (Lemma 6), we get

 | E 1 \displaystyle E_{1} | ≪ H 1 log Q 1 ⋅ ∑ v ∈ ℐ 1 e − 2 α 1 v / H 1 ⋅ ( T + X e v / H 1) 1 X / e v / H 1 \displaystyle\ll H_{1}\log Q_{1}\cdot\sum_{v\in\mathcal{I}_{1}}e^{-2\alpha_{1}v/H_{1}}\cdot\Big(T+\frac{X}{e^{v/H_{1}}}\Big)\frac{1}{X/e^{v/H_{1}}} |  |

 |  | ≪ H 1 ​ log ⁡ Q 1 ⋅ P 1 − 2 ​ α 1 ​ 1 1 − e − 2 α 1 / H 1 ⋅ ( T X / Q 1 + 1) \displaystyle\ll H_{1}\log Q_{1}\cdot P_{1}^{-2\alpha_{1}}\frac{1}{1-e^{-2\alpha_{1}/H_{1}}}\cdot\Big(\frac{T}{X/Q_{1}}+1\Big) |  |

 |  | ≪ H 1 2 log Q 1 ⋅ P 1 − 1 / 2 + 3 η ( T X / Q 1 + 1) ≪ ( T X / Q 1 + 1) ( log ⁡ Q 1) 1 / 3 P 1 1 / 6 − η \displaystyle\ll H_{1}^{2}\log Q_{1}\cdot P_{1}^{-1/2+3\eta}\Big(\frac{T}{X/Q_{1}}+1\Big)\ll\Big(\frac{T}{X/Q_{1}}+1\Big)\frac{(\log Q_{1})^{1/3}}{P_{1}^{1/6-\eta}} |  |

by the choice of H 1 H_{1}.

### 8.2. Bounding E j E_{j} with 2 ≤ j ≤ J 2\leq j\leq J

Now suppose that 2 ≤ j ≤ J 2\leq j\leq J. In this case we split further

 | 𝒯 j = ⋃ r ∈ ℐ j − 1 𝒯 j, r, \mathcal{T}_{j}=\bigcup_{r\in\mathcal{I}_{j-1}}\mathcal{T}_{j,r}, |  |

where

 | 𝒯 j, r = { t ∈ 𝒯 j: | Q r, H j − 1 ( 1 + i t) | > e − α j − 1 r / H j − 1 } \mathcal{T}_{j,r}=\{t\in\mathcal{T}_{j}\colon|Q_{r,H_{j-1}}(1+it)|>e^{-\alpha_{j-1}r/H_{j-1}}\} |  |

Note that this is indeed a splitting, since, by the definition of 𝒯 j \mathcal{T}_{j}, for any t ∈ 𝒯 j t\in\mathcal{T}_{j} there will be an index r ∈ ℐ j − 1 r\in\mathcal{I}_{j-1} such that | Q r, H j − 1 ( 1 + i t) | > e − α j − 1 r / H j − 1 |Q_{r,H_{j-1}}(1+it)|>e^{-\alpha_{j-1}r/H_{j-1}}. Therefore, for some v = v ⁡ ( j) ∈ ℐ j v=v(j)\in\mathcal{I}_{j} and r = r ⁡ ( j) ∈ ℐ j − 1 r=r(j)\in\mathcal{I}_{j-1},

(25) |  | E j ≪ H j log Q j ⋅ #ℐ j ⋅ #ℐ j − 1 ⋅ e − 2 α j v / H j × ∫ 𝒯 j, r | R v, H j ( 1 + i t) | 2 d t E_{j}\ll H_{j}\log Q_{j}\cdot\#\mathcal{I}_{j}\cdot\#\mathcal{I}_{j-1}\cdot e^{-2\alpha_{j}v/H_{j}}\times\int_{\mathcal{T}_{j,r}}|R_{v,H_{j}}(1+it)|^{2}dt |  |

On 𝒯 j, r \mathcal{T}_{j,r} we have | Q r, H j − 1 ( 1 + i t) | > e − α j − 1 r / H j − 1 |Q_{r,H_{j-1}}(1+it)|>e^{-\alpha_{j-1}r/H_{j-1}}. Therefore, for any ℓ j, r ≥ 1 \ell_{j,r}\geq 1, multiplying by the term ( | Q r, H j − 1 ​ ( 1 + i ​ t) | ​ e α j − 1 ​ r / H j − 1) 2 ​ ℓ j, r ≥ 1 (|Q_{r,H_{j-1}}(1+it)|e^{\alpha_{j-1}r/H_{j-1}})^{2\ell_{j,r}}\geq 1, we can bound this further as

 | E j ≪ \displaystyle E_{j}\ll | ( H j log Q j) 3 ⋅ e − 2 α j v / H j × \displaystyle(H_{j}\log Q_{j})^{3}\cdot e^{-2\alpha_{j}v/H_{j}}\times |  |

 |  | × exp ⁡ ( 2 ​ ℓ j, r ⋅ α j − 1 ​ r / H j − 1) ​ ∫ 𝒯 j, r | Q r, H j − 1 ​ ( 1 + i ​ t) ℓ j, r ​ R v, H j ​ ( 1 + i ​ t) | 2 ​ 𝑑 t. \displaystyle\times\exp\Big(2\ell_{j,r}\cdot\alpha_{j-1}r/H_{j-1}\Big)\int_{\mathcal{T}_{j,r}}|Q_{r,H_{j-1}}(1+it)^{\ell_{j,r}}R_{v,H_{j}}(1+it)|^{2}dt. |  |

Choosing

 | ℓ j, r = ⌈ v / H j r / H j − 1 ⌉ ≤ H j − 1 r ⋅ v H j + 1, \ell_{j,r}=\left\lceil\frac{v/H_{j}}{r/H_{j-1}}\right\rceil\leq\frac{H_{j-1}}{r}\cdot\frac{v}{H_{j}}+1, |  |

we get

 | E j \displaystyle E_{j} | ≪ H j 3 ​ ( log ⁡ Q j) 3 ⋅ exp ⁡ ( 2 ​ v ​ ( α j − 1 − α j) / H j + 2 ​ α j − 1 ​ r / H j − 1) \displaystyle\ll H_{j}^{3}(\log Q_{j})^{3}\cdot\exp\Big(2v(\alpha_{j-1}-\alpha_{j})/H_{j}+2\alpha_{j-1}r/H_{j-1}\Big) |  |

 |  | ⋅ ∫ − T T | Q r, H j − 1 ​ ( 1 + i ​ t) ℓ j, r ​ R v, H j ​ ( 1 + i ​ t) | 2 ​ 𝑑 t. \displaystyle\quad\cdot\int_{-T}^{T}|Q_{r,H_{j-1}}(1+it)^{\ell_{j,r}}R_{v,H_{j}}(1+it)|^{2}dt. |  |

Now we are in the position to use Lemma 13 which gives

 | ∫ − T T | Q r, H j − 1 ​ ( 1 + i ​ t) ℓ j, r ​ R v, H j ​ ( 1 + i ​ t) | 2 ​ 𝑑 t \displaystyle\int_{-T}^{T}|Q_{r,H_{j-1}}(1+it)^{\ell_{j,r}}R_{v,H_{j}}(1+it)|^{2}dt | ≪ ( T X + 2 ℓ j, r e r / H j − 1) ⋅ ( ℓ j, r + 1)! 2 \displaystyle\ll\left(\frac{T}{X}+2^{\ell_{j,r}}e^{r/H_{j-1}}\right)\cdot(\ell_{j,r}+1)!^{2} |  |

 |  | ≪ ( T X + Q j − 1) ​ exp ⁡ ( 2 ​ ℓ j, r ​ log ⁡ ℓ j, r) \displaystyle\ll\left(\frac{T}{X}+Q_{j-1}\right)\exp\left(2\ell_{j,r}\log\ell_{j,r}\right) |  |

Here by the mean value theorem and the definition of ℓ j, r \ell_{j,r}

 | ℓ j, r ​ log ⁡ ℓ j, r ≤ v / H j r / H j − 1 ​ log ⁡ v / H j r / H j − 1 + log ⁡ log ⁡ Q j + 1 ≤ v H j ⋅ log ⁡ log ⁡ Q j log ⁡ P j − 1 − 1 + log ⁡ log ⁡ Q j + 1, \begin{split}\ell_{j,r}\log\ell_{j,r}&\leq\frac{v/H_{j}}{r/H_{j-1}}\log\frac{v/H_{j}}{r/H_{j-1}}+\log\log Q_{j}+1\\ &\leq\frac{v}{H_{j}}\cdot\frac{\log\log Q_{j}}{\log P_{j-1}-1}+\log\log Q_{j}+1,\end{split} |  |

so that

 |  | ∫ − T T | Q r, H j − 1 ​ ( 1 + i ​ t) ℓ j, r ​ R v, H j ​ ( 1 + i ​ t) | 2 ​ 𝑑 t \displaystyle\int_{-T}^{T}|Q_{r,H_{j-1}}(1+it)^{\ell_{j,r}}R_{v,H_{j}}(1+it)|^{2}dt |  |

 |  | ≪ ( T X + 1) ​ Q j − 1 ​ ( log ⁡ Q j) 2 ​ exp ⁡ ( v H j ⋅ 2 ​ log ⁡ log ​ Q j log ⁡ P j − 1 − 1) \displaystyle\ll\left(\frac{T}{X}+1\right)Q_{j-1}(\log Q_{j})^{2}\exp\left(\frac{v}{H_{j}}\cdot\frac{2\log\log Q_{j}}{\log P_{j-1}-1}\right) |  |

 |  | ≪ ( T X + 1) ​ Q j − 1 ​ ( log ⁡ Q j) 2 ​ exp ⁡ ( η 2 ​ j 2 ⋅ v H j) \displaystyle\ll\left(\frac{T}{X}+1\right)Q_{j-1}(\log Q_{j})^{2}\exp\left(\frac{\eta}{2j^{2}}\cdot\frac{v}{H_{j}}\right) |  |

by ( 2). Note that ( 2) also implies

 | log ⁡ log ⁡ Q j ≤ 1 24 ​ log ⁡ P j − 1 ≤ log ⁡ Q j − 1 1 / 24 ⟹ log ⁡ Q j ≤ Q j − 1 1 / 24, \log\log Q_{j}\leq\frac{1}{24}\log P_{j-1}\leq\log Q_{j-1}^{1/24}\implies\log Q_{j}\leq Q_{j-1}^{1/24}, |  |

so that

 | H j 3 ​ ( log ⁡ Q j) 5 ​ Q j − 1 ​ exp ⁡ ( 2 ​ α j − 1 ​ r / H j − 1) ≪ H j 3 ​ ( log ⁡ Q j) 5 ​ Q j − 1 2 ≪ H j 3 ​ Q j − 1 5 / 2 ≪ j 6 ​ P 1 1 / 2 ​ Q j − 1 5 / 2 ≪ j 6 ​ Q j − 1 3. \begin{split}H_{j}^{3}(\log Q_{j})^{5}Q_{j-1}\exp(2\alpha_{j-1}r/H_{j-1})&\ll H_{j}^{3}(\log Q_{j})^{5}Q_{j-1}^{2}\\ &\ll H_{j}^{3}Q_{j-1}^{5/2}\ll j^{6}P_{1}^{1/2}Q_{j-1}^{5/2}\ll j^{6}Q_{j-1}^{3}.\end{split} |  |

Therefore we end up with the bound

 | E j \displaystyle E_{j} | ≪ ( T X + 1) ​ j 6 ​ Q j − 1 3 ​ exp ⁡ ( 2 ​ v H j ​ ( α j − 1 − α j + η 4 ​ j 2)) \displaystyle\ll\left(\frac{T}{X}+1\right)j^{6}Q_{j-1}^{3}\exp\left(\frac{2v}{H_{j}}\left(\alpha_{j-1}-\alpha_{j}+\frac{\eta}{4j^{2}}\right)\right) |  |

 |  | ≪ ( T X + 1) ​ j 6 ​ Q j − 1 3 ​ exp ⁡ ( − η 2 ​ j 2 ​ log ⁡ P j) \displaystyle\ll\left(\frac{T}{X}+1\right)j^{6}Q_{j-1}^{3}\exp\left(-\frac{\eta}{2j^{2}}\log P_{j}\right) |  |

 |  | ≪ ( T X + 1) ​ 1 j 2 ​ Q j − 1 ≪ ( T X + 1) ​ 1 j 2 ​ P 1 \displaystyle\ll\left(\frac{T}{X}+1\right)\frac{1}{j^{2}Q_{j-1}}\ll\Big(\frac{T}{X}+1\Big)\frac{1}{j^{2}P_{1}} |  |

by ( 20) and ( 3).

### 8.3. Bounding ∫ 𝒰 | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t \int_{\mathcal{U}}|F(1+it)|^{2}dt

Let us now bound the integral

 | ∫ 𝒰 | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t. \int_{\mathcal{U}}|F(1+it)|^{2}dt. |  |

We again apply Lemma 12, this time with a m = b m = f ⁡ ( m) ​ 𝟏 𝒮 ​ ( m) a_{m}=b_{m}=f(m)\mathbf{1}_{\mathcal{S}}(m), c p = f ⁡ ( p) c_{p}=f(p) and P = exp ⁡ ( ( log ⁡ X) 1 − 1 / 48), Q = exp ⁡ ( log ⁡ X / ( log ⁡ log ⁡ X)) P=\exp((\log X)^{1-1/48}),Q=\exp(\log X/(\log\log X)) and H = ( log ⁡ X) 1 / 48 H=(\log X)^{1/48} to see that, for some v ∈ [⌊ H ​ log ⁡ P ⌋, H ​ log ⁡ Q] v\in[\lfloor H\log P\rfloor,H\log Q], the integral is bounded by

 | H 2 ​ ( log ⁡ X) 2 ​ ∫ 𝒰 | Q v, H ​ ( 1 + i ​ t) ​ R v, H ​ ( 1 + i ​ t) | 2 ​ 𝑑 t + ( T X + 1) ​ ( 1 H + 1 P + log ⁡ P log ⁡ Q), H^{2}(\log X)^{2}\int_{\mathcal{U}}|Q_{v,H}(1+it)R_{v,H}(1+it)|^{2}dt+\left(\frac{T}{X}+1\right)\left(\frac{1}{H}+\frac{1}{P}+\frac{\log P}{\log Q}\right), |  |

where

 | Q v, H ​ ( s) = ∑ e v / H ≤ p ≤ e ( v + 1) / H f ⁡ ( p) p s Q_{v,H}(s)=\sum_{e^{v/H}\leq p\leq e^{(v+1)/H}}\frac{f(p)}{p^{s}} |  |

and

 | R v, H ( s) = ∑ X e − v / H ≤ m ≤ 2 X e − v / H m ∈ 𝒮 f ⁡ ( m) m s ⋅ 1 #{ p ∈ [P, Q]: p ∣ m } + 1. R_{v,H}(s)=\sum_{\begin{subarray}{c}Xe^{-v/H}\leq m\leq 2Xe^{-v/H}\\ m\in\mathcal{S}\end{subarray}}\frac{f(m)}{m^{s}}\cdot\frac{1}{\#\{p\in[P,Q]\colon p\mid m\}+1}. |  |

We then find a well-spaced set 𝒯 ⊆ 𝒰 \mathcal{T}\subseteq\mathcal{U} such that

 | ∫ 𝒰 | Q v, H ​ ( 1 + i ​ t) ​ R v, H ​ ( 1 + i ​ t) | 2 ​ 𝑑 t ≤ 2 ​ ∑ t ∈ 𝒯 | Q v, H ​ ( 1 + i ​ t) | 2 ⋅ | R v, H ​ ( 1 + i ​ t) | 2. \int_{\mathcal{U}}|Q_{v,H}(1+it)R_{v,H}(1+it)|^{2}dt\leq 2\sum_{t\in\mathcal{T}}|Q_{v,H}(1+it)|^{2}\cdot|R_{v,H}(1+it)|^{2}. |  |

By definition of J J and ( 2), we know that Q J ≤ exp ⁡ ( ( log ⁡ X) 1 / 2) Q_{J}\leq\exp((\log X)^{1/2}) and

 | log ⁡ P J ≥ 4 ​ j 2 η ⋅ log ⁡ log ⁡ Q J + 1 ≥ 4 ​ j 2 η ⋅ log ⁡ ( log ⁡ X) 1 / 2 ⟹ P J ≥ ( log ⁡ X) 2 / η. \log P_{J}\geq\frac{4j^{2}}{\eta}\cdot\log\log Q_{J+1}\geq\frac{4j^{2}}{\eta}\cdot\log(\log X)^{1/2}\implies P_{J}\geq(\log X)^{2/\eta}. |  |

Now, by definition of 𝒰 \mathcal{U}, for each t ∈ 𝒯 t\in\mathcal{T} there is v ∈ ℐ J v\in\mathcal{I}_{J} such that | Q v, H J ( s) | > e − α J v / H J |Q_{v,H_{J}}(s)|>e^{-\alpha_{J}v/H_{J}}. Applying Lemma 8 to Q v, H J ​ ( s) Q_{v,H_{J}}(s) for every v ∈ ℐ J v\in\mathcal{I}_{J} we get

 | | 𝒯 | ≪ | ℐ J | ⋅ T 2 ​ α J + o ⁡ ( 1) ⋅ T η ⋅ X o ⁡ ( 1) ≪ T 1 / 2 − η ⋅ X o ⁡ ( 1). |\mathcal{T}|\ll|\mathcal{I}_{J}|\cdot T^{2\alpha_{J}+o(1)}\cdot T^{\eta}\cdot X^{o(1)}\ll T^{1/2-\eta}\cdot X^{o(1)}. |  |

Let

 | 𝒯 L = { t ∈ 𝒯: | Q v, H ​ ( 1 + i ​ t) | ≥ ( log ⁡ X) − 100 } \mathcal{T}_{L}=\{t\in\mathcal{T}:|Q_{v,H}(1+it)|\geq(\log X)^{-100}\} |  |

and

 | 𝒯 S = { t ∈ 𝒯: | Q v, H ​ ( 1 + i ​ t) | < ( log ⁡ X) − 100 }. \mathcal{T}_{S}=\{t\in\mathcal{T}:|Q_{v,H}(1+it)|<(\log X)^{-100}\}. |  |

By Lemma 9,

 |  | ∑ t ∈ 𝒯 S | Q v, H ​ ( 1 + i ​ t) ​ R v, H ​ ( 1 + i ​ t) | 2 ​ d ​ t ≪ ( log ⁡ X) − 200 ⋅ ∑ t ∈ 𝒯 | R v, H ​ ( 1 + i ​ t) | 2 \displaystyle\sum_{t\in\mathcal{T}_{S}}|Q_{v,H}(1+it)R_{v,H}(1+it)|^{2}dt\ll(\log X)^{-200}\cdot\sum_{t\in\mathcal{T}}|R_{v,H}(1+it)|^{2} |  |

 |  | ≪ ( log X) − 200 ⋅ ( X e − v / H + | 𝒯 | T 1 / 2) log ( 2 T) 1 X e − v / H ≪ ( log X) − 199, \displaystyle\ll(\log X)^{-200}\cdot\Big(Xe^{-v/H}+|\mathcal{T}|T^{1/2}\Big)\log(2T)\frac{1}{Xe^{-v/H}}\ll(\log X)^{-199}, |  |

and thus we can concentrate on the integral over 𝒯 L \mathcal{T}_{L}.

By Lemma 8, we have

 | | 𝒯 L | ≪ exp ⁡ ( 2 ​ log ⁡ ( log ⁡ X) 100 v / H ​ log ⁡ T + 2 ​ log ⁡ ( log ⁡ X) 100 + 2 ​ log ⁡ T v / H ​ log ⁡ log ⁡ T) ≪ exp ⁡ ( ( log ⁡ X) 1 + o ⁡ ( 1) log ⁡ P) ≪ exp ⁡ ( ( log ⁡ X) 1 / 48 + o ⁡ ( 1)), \begin{split}|\mathcal{T}_{L}|&\ll\exp\left(2\frac{\log(\log X)^{100}}{v/H}\log T+2\log(\log X)^{100}+2\frac{\log T}{v/H}\log\log T\right)\\ &\ll\exp\left(\frac{(\log X)^{1+o(1)}}{\log P}\right)\ll\exp((\log X)^{1/48+o(1)}),\end{split} |  |

and by Lemmas 3 and 5 (since 2 J ≪ ( log ⁡ X) o ⁡ ( 1) 2^{J}\ll(\log X)^{o(1)}),

 | max ( log ⁡ X) 1 / 15 ≤ | u | ≤ 2 ​ T 1 + ε | R v, H ( 1 + i u) | ≪ ( log X) − 1 / 16 + o ( 1) ⋅ log ⁡ Q log ⁡ P \max_{(\log X)^{1/15}\leq|u|\leq 2T^{1+\varepsilon}}|R_{v,H}(1+iu)|\ll(\log X)^{-1/16+o(1)}\cdot\frac{\log Q}{\log P} |  |

Thus by Lemma 11, and the Halász bound above,

 | ∑ t ∈ 𝒯 L | R v, H ​ ( 1 + i ​ t) | 2 ⋅ | Q v, H ​ ( 1 + i ​ t) | 2 ≪ ( log X) − 1 / 8 + o ( 1) ( log ⁡ Q log ⁡ P) 2 ( e v / H + | 𝒯 L | ⋅ e v / H ⋅ exp ( − ( log X) 1 / 5)) ⋅ ∑ e v / H ≤ r ≤ e ( v + 1) / H r ∈ ℙ 1 r 2 ​ log ⁡ r ≪ ( log X) − 1 / 8 + o ( 1) ( log ⁡ Q log ⁡ P) 2 H v ∑ e v / H ≤ r ≤ e ( v + 1) / H r ∈ ℙ 1 r ≪ ( log X) − 1 / 8 + o ( 1) ( log ⁡ Q) 2 ( log ⁡ P) 4 1 H, \begin{split}&\sum_{t\in\mathcal{T}_{L}}|R_{v,H}(1+it)|^{2}\cdot|Q_{v,H}(1+it)|^{2}\\ &\ll(\log X)^{-1/8+o(1)}\left(\frac{\log Q}{\log P}\right)^{2}\Big(e^{v/H}+|\mathcal{T}_{L}|\cdot e^{v/H}\cdot\exp(-(\log X)^{1/5})\Big)\cdot\sum_{\begin{subarray}{c}e^{v/H}\leq r\leq e^{(v+1)/H}\\ r\in\mathbb{P}\end{subarray}}\frac{1}{r^{2}\log r}\\ &\ll(\log X)^{-1/8+o(1)}\left(\frac{\log Q}{\log P}\right)^{2}\frac{H}{v}\sum_{\begin{subarray}{c}e^{v/H}\leq r\leq e^{(v+1)/H}\\ r\in\mathbb{P}\end{subarray}}\frac{1}{r}\ll(\log X)^{-1/8+o(1)}\frac{(\log Q)^{2}}{(\log P)^{4}}\frac{1}{H},\end{split} |  |

where the additional gain comes from the sum over r ∈ ℙ r\in\mathbb{P} saving us an additional 1 / v ≪ 1 / ( H ​ log ⁡ P) 1/v\ll 1/(H\log P) (since we are looking at primes in a short interval). Combining the above estimates, we get the bound

 | ∫ t ∈ 𝒰 | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t ≪ H ( log X) 2 ( log X) − 1 / 8 + o ( 1) ( log ⁡ Q) 2 ( log ⁡ P) 4 + ( T X + 1) ( 1 H + log ⁡ P log ⁡ Q) ≪ ( T X + 1) ( log X) − 1 / 48 + o ( 1). \begin{split}\int_{t\in\mathcal{U}}|F(1+it)|^{2}dt&\ll H(\log X)^{2}(\log X)^{-1/8+o(1)}\frac{(\log Q)^{2}}{(\log P)^{4}}+\left(\frac{T}{X}+1\right)\left(\frac{1}{H}+\frac{\log P}{\log Q}\right)\\ &\ll\left(\frac{T}{X}+1\right)(\log X)^{-1/48+o(1)}.\end{split} |  |

### 8.4. Conclusion

Collecting all the bounds and refering to ( 24) we get

 | ∫ T 0 T | F ⁡ ( 1 + i ​ t) | 2 ​ 𝑑 t ≪ ( T X / Q 1 + 1) ​ ( log ⁡ Q 1) 1 / 3 P 1 1 / 6 − η + ( T X + 1) ​ ( ∑ 2 ≤ j ≤ J − 1 1 j 2 ​ P 1 + 1 ( log ⁡ X) 1 / 48 + o ⁡ ( 1)) ≪ ( T X / Q 1 + 1) ​ ( ( log ⁡ Q 1) 1 / 3 P 1 1 / 6 − η + 1 ( log ⁡ X) 1 / 50) \begin{split}&\int_{T_{0}}^{T}|F(1+it)|^{2}dt\\ &\ll\left(\frac{T}{X/Q_{1}}+1\right)\frac{(\log Q_{1})^{1/3}}{P_{1}^{1/6-\eta}}+\left(\frac{T}{X}+1\right)\left(\sum_{2\leq j\leq J-1}\frac{1}{j^{2}P_{1}}+\frac{1}{(\log X)^{1/48+o(1)}}\right)\\ &\ll\left(\frac{T}{X/Q_{1}}+1\right)\left(\frac{(\log Q_{1})^{1/3}}{P_{1}^{1/6-\eta}}+\frac{1}{(\log X)^{1/50}}\right)\end{split} |  |

which is the desired bound. ∎

## 9. Proofs of Theorems 1 and 3

###### Proof of Theorem 3.

Combining Lemma 14 with Proposition 1 it follows that

 | 1 X ​ ∫ X 2 ​ X | 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 f ⁡ ( n) − 1 h 2 ​ ∑ x ≤ n ≤ x + h 2 n ∈ 𝒮 f ⁡ ( n) | 2 ​ 𝑑 x ≪ ( log ⁡ h) 1 / 3 P 1 1 / 6 − η + 1 ( log ⁡ X) 1 / 50, \frac{1}{X}\int_{X}^{2X}\left|\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}f(n)-\frac{1}{h_{2}}\sum_{\begin{subarray}{c}x\leq n\leq x+h_{2}\\ n\in\mathcal{S}\end{subarray}}f(n)\right|^{2}dx\ll\frac{(\log h)^{1/3}}{P_{1}^{1/6-\eta}}+\frac{1}{(\log X)^{1/50}}, |  |

when Q 1 ≤ h ≤ h 2 = X ( log ⁡ X) 1 / 5 Q_{1}\leq h\leq h_{2}=\frac{X}{(\log X)^{1/5}}. Using Lemma 4 together with Lemma 5 we have, for any X ≤ x ≤ 2 ​ X X\leq x\leq 2X,

(26) |  | 1 h 2 ∑ x ≤ n ≤ x + h 2 n ∈ 𝒮 f ( n) = 1 X ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ( n) + O ( ( log X) − 1 / 20 + o ( 1)), \frac{1}{h_{2}}\sum_{\begin{subarray}{c}x\leq n\leq x+h_{2}\\ n\in\mathcal{S}\end{subarray}}f(n)=\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}f(n)+O((\log X)^{-1/20+o(1)}), |  |

and the claim follows in case h ≤ h 2 h\leq h_{2}. In case h > h 2 h>h_{2}, the claim follows immediately from ( 26). ∎

###### Proof of Theorem 1.

Let us start by separating the contribution of n ∉ 𝒮 n\not\in\mathcal{S}, where 𝒮 \mathcal{S} is a set satisfying the conditions in Theorem 3. We get

 | | 1 h ​ ∑ x ≤ n ≤ x + h f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) | ≤ | 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) | + 1 h ​ ∑ x ≤ n ≤ x + h n ∉ 𝒮 1 + 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∉ 𝒮 1. \begin{split}&\Bigg|\frac{1}{h}\sum_{x\leq n\leq x+h}f(n)-\frac{1}{X}\sum_{X\leq n\leq 2X}f(n)\Bigg|\\ &\leq\left|\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}f(n)-\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}f(n)\right|+\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\not\in\mathcal{S}\end{subarray}}1+\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\not\in\mathcal{S}\end{subarray}}1.\end{split} |  |

Let us write

 | 1 h ​ ∑ x ≤ n ≤ x + h n ∉ 𝒮 1 = 1 + O ⁡ ( 1 / h) − 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 1 = 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∉ 𝒮 1 + 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 1 + O ⁡ ( 1 / h) − 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 1, \begin{split}&\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\not\in\mathcal{S}\end{subarray}}1=1+O(1/h)-\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}1\\ &=\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\not\in\mathcal{S}\end{subarray}}1+\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}1+O(1/h)-\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}1,\end{split} |  |

so that

 | | 1 h ​ ∑ x ≤ n ≤ x + h f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) | ≤ | 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 f ⁡ ( n) | + | 1 h ​ ∑ x ≤ n ≤ x + h n ∈ 𝒮 1 − 1 X ​ ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 1 | + 2 X ​ ∑ X ≤ n ≤ 2 ​ X n ∉ 𝒮 1 + O ⁡ ( 1 / h). \begin{split}&\Bigg|\frac{1}{h}\sum_{x\leq n\leq x+h}f(n)-\frac{1}{X}\sum_{X\leq n\leq 2X}f(n)\Bigg|\\ &\leq\left|\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}f(n)-\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}f(n)\right|+\left|\frac{1}{h}\sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}1-\frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}1\right|+\frac{2}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\not\in\mathcal{S}\end{subarray}}1+O(1/h).\end{split} |  |

Theorem 3 applied to f ⁡ ( n) f(n) and to 1 1 implies that the first and second terms are both at most δ / 100 \delta/100 with at most

(27) |  | ≪ X ​ ( log ⁡ h) 1 / 3 P 1 1 / 6 − η ​ δ 2 + X ( log ⁡ X) 1 / 50 ​ δ 2 \ll\frac{X(\log h)^{1/3}}{P_{1}^{1/6-\eta}\delta^{2}}+\frac{X}{(\log X)^{1/50}\delta^{2}} |  |

exceptions.

By the fundamental lemma of the sieve, for all large enough X X,

 | ∑ X ≤ n ≤ 2 ​ X n ∉ 𝒮 1 ≤ ( 1 + 1 100) ​ X ​ ∑ j ≤ J ∏ P j ≤ p ≤ Q j ( 1 − 1 p) ≤ ( 1 + 1 100) ​ X ​ ∑ j ≤ J log ⁡ P j log ⁡ Q j \displaystyle\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\not\in\mathcal{S}\end{subarray}}1\leq\left(1+\frac{1}{100}\right)X\sum_{j\leq J}\prod_{P_{j}\leq p\leq Q_{j}}\Big(1-\frac{1}{p}\Big)\leq\left(1+\frac{1}{100}\right)X\sum_{j\leq J}\frac{\log P_{j}}{\log Q_{j}} |  |

Hence we get that

(28) |  | | 1 h ​ ∑ x ≤ n ≤ x + h f ⁡ ( n) − 1 X ​ ∑ X ≤ n ≤ 2 ​ X f ⁡ ( n) | ≤ δ / 50 + ( 2 + 1 50) ​ ∑ j log ⁡ P j log ⁡ Q j \Bigg|\frac{1}{h}\sum_{x\leq n\leq x+h}f(n)-\frac{1}{X}\sum_{X\leq n\leq 2X}f(n)\Bigg|\leq\delta/50+\left(2+\frac{1}{50}\right)\sum_{j}\frac{\log P_{j}}{\log Q_{j}} |  |

with at most ( 27) exceptions.

To deduce Theorem 1 we pick an appropriate sequence of intervals [P j, Q j] [P_{j},Q_{j}]. In case h ≤ exp ⁡ ( ( log ⁡ X) 1 / 2) h\leq\exp((\log X)^{1/2}), we choose η = 1 / 150 \eta=1/150, Q 1 = h, P 1 = max ⁡ { h δ / 4, ( log ⁡ h) 40 / η } Q_{1}=h,P_{1}=\max\{h^{\delta/4},(\log h)^{40/\eta}\} and P j P_{j} and Q j Q_{j} as in ( 4). With this choice the expression in ( 28) is at most δ + 20000 ​ log ⁡ log ⁡ h log ⁡ h \delta+20000\frac{\log\log h}{\log h} and the number of exceptions is as claimed.

In case h > exp ⁡ ( ( log ⁡ X) 1 / 2) h>\exp((\log X)^{1/2}), we choose η = 1 / 150, Q 1 = exp ⁡ ( ( log ⁡ X) 1 / 2), P 1 = Q 1 δ / 4 \eta=1/150,Q_{1}=\exp((\log X)^{1/2}),P_{1}=Q_{1}^{\delta/4} and P j P_{j} and Q j Q_{j} as in ( 4). This is a valid choice since we can assume δ ≥ ( log X) − 1 / 100 \delta\geq(\log X)^{-1/100}, so that P 1 ≥ ( log ⁡ Q 1) 40 / η P_{1}\geq(\log Q_{1})^{40/\eta}. With this choice the expression in ( 28) is at most δ \delta and the number of exceptions is as claimed.

∎

## 10. Proof of Theorems 4 and 2

Let η ξ, v ​ ( x) \eta_{\xi,v}(x) be a smoothing of the indicator function of [1 − v, 1 + v] [1-v,1+v] which decays on the segments [1 − ξ − v, 1 − v] [1-\xi-v,1-v] and [1 + v, 1 + ξ + v] [1+v,1+\xi+v]. Precisely, let

 | η ξ, v ​ ( x) = { 1 if ​ 1 − v ≤ x ≤ 1 + v ( 1 + v + ξ − x) / ξ if ​ 1 + v ≤ x ≤ 1 + ξ + v ( x + v + ξ − 1) / ξ if ​ 1 − ξ − v ≤ x ≤ 1 − v 0 otherwise. \eta_{\xi,v}(x)=\begin{cases}1&\text{ if }1-v\leq x\leq 1+v\\ (1+v+\xi-x)/\xi&\text{ if }1+v\leq x\leq 1+\xi+v\\ (x+v+\xi-1)/\xi&\text{ if }1-\xi-v\leq x\leq 1-v\\ 0&\text{ otherwise}.\end{cases} |  |

We find that

 | η ^ ξ, v ​ ( s) \displaystyle\widehat{\eta}_{\xi,v}(s) | : = − ∫ 0 ∞ t s d η ξ, v ( t) = − ∫ 1 − v − ξ 1 − v t s ξ d t + ∫ 1 + v 1 + v + ξ t s ξ d t \displaystyle:=-\int_{0}^{\infty}t^{s}d\eta_{\xi,v}(t)=-\int_{1-v-\xi}^{1-v}\frac{t^{s}}{\xi}dt+\int_{1+v}^{1+v+\xi}\frac{t^{s}}{\xi}dt |  |

 |  | = ( 1 + ξ + v) s + 1 − ( 1 + v) s + 1 ξ ⁡ ( s + 1) − ( 1 − v) s + 1 − ( 1 − ξ − v) s + 1 ξ ⁡ ( s + 1). \displaystyle=\frac{(1+\xi+v)^{s+1}-(1+v)^{s+1}}{\xi(s+1)}-\frac{(1-v)^{s+1}-(1-\xi-v)^{s+1}}{\xi(s+1)}. |  |

Therefore by Mellin inversion,

(29) |  | η ξ, v ​ ( x) = 1 2 ​ π ​ i ​ ∫ 1 − i ​ ∞ 1 + i ​ ∞ x − s s ⋅ η ^ ξ, v ​ ( s) ​ 𝑑 s. \eta_{\xi,v}(x)=\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}\frac{x^{-s}}{s}\cdot\widehat{\eta}_{\xi,v}(s)ds. |  |

We are now ready to prove Theorem 4.

###### Proof of Theorem 4.

Let h 1 = h ​ x h_{1}=h\sqrt{x} and h 2 = x ( log x) − 1 / 5 h_{2}=x(\log x)^{-1/5}. Let v j = h j / x v_{j}=h_{j}/x and ξ j = δ ​ h j / x \xi_{j}=\delta h_{j}/x for some small δ \delta to be chosen later. Let also η j ​ ( x):= η ξ j, v j ​ ( x) \eta_{j}(x):=\eta_{\xi_{j},v_{j}}(x) for j = 1, 2 j=1,2. Consider,

 | S j = ∑ x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) ​ η j ​ ( n 1 ​ n 2 x). \displaystyle S_{j}=\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})\eta_{j}\Big(\frac{n_{1}n_{2}}{x}\Big). |  |

Using ( 29), we see that S j S_{j} equals

 | 1 2 ​ π ​ i ​ ∫ 1 − i ​ ∞ 1 + i ​ ∞ M 1 ​ ( s) ​ M 2 ​ ( s) ​ x s ⋅ ( 1 + ξ j + v j) s + 1 − ( 1 + v j) s + 1 − ( 1 − v j) s + 1 + ( 1 − ξ j − v j) s + 1 ξ j ⋅ s ⁡ ( s + 1) ​ 𝑑 s \displaystyle\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}M_{1}(s)M_{2}(s)x^{s}\cdot\frac{(1+\xi_{j}+v_{j})^{s+1}-(1+v_{j})^{s+1}-(1-v_{j})^{s+1}+(1-\xi_{j}-v_{j})^{s+1}}{\xi_{j}\cdot s(s+1)}ds |  |

where

 | M 1 ​ ( s):= ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ⁡ ( n) n s and M 2 ​ ( s):= ∑ x / 2 ≤ n ≤ 2 ​ x n ∈ 𝒮 f ⁡ ( n) n s M_{1}(s):=\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{s}}\quad\text{and}\quad M_{2}(s):=\sum_{\begin{subarray}{c}\sqrt{x}/2\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}\frac{f(n)}{n^{s}} |  |

As in the proof of Lemma 14 we split the integral in S j S_{j} into two parts U j U_{j} and V j V_{j} according to whether | t | ≤ T 0:= ( log ⁡ x) 1 / 12 |t|\leq T_{0}:=(\log x)^{1/12} or not. In U j U_{j}, we expand each term in the following way, ( 1 + w) 1 + s = 1 + w ⁡ ( 1 + s) + w 2 2 ​ s ​ ( 1 + s) + O ⁡ ( | w | 3 ​ | s | ​ | s + 1 | ​ | s − 1 |) (1+w)^{1+s}=1+w(1+s)+\frac{w^{2}}{2}s(1+s)+O(|w|^{3}|s||s+1||s-1|) (for | w | ≤ 1 / 2 |w|\leq 1/2 and ℜ ⁡ s = 1 \Re s=1). This gives,

 |  | x s ⋅ ( 1 + ξ j + v j) s + 1 − ( 1 + v j) s + 1 − ( 1 − v j) s + 1 + ( 1 − ξ j − v j) s + 1 ξ j ​ s ​ ( s + 1) \displaystyle x^{s}\cdot\frac{(1+\xi_{j}+v_{j})^{s+1}-(1+v_{j})^{s+1}-(1-v_{j})^{s+1}+(1-\xi_{j}-v_{j})^{s+1}}{\xi_{j}s(s+1)} |  |

 |  | = ( ξ j + 2 ​ v j) ​ x s + O ⁡ ( x ⁡ ( 1 + | s |) ​ ( ξ j 3 + v j 3) / ξ j) = ( 2 + δ) ⋅ h j x ⋅ x s + O ⁡ ( x ⋅ T 0 ​ ( h j / x) 2 / δ). \displaystyle=(\xi_{j}+2v_{j})x^{s}+O(x(1+|s|)(\xi_{j}^{3}+v_{j}^{3})/\xi_{j})=(2+\delta)\cdot\frac{h_{j}}{x}\cdot x^{s}+O(x\cdot T_{0}(h_{j}/x)^{2}/\delta). |  |

so that

 | | 1 h 1 ​ U 1 − 1 h 2 ​ U 2 | ≪ T 0 2 δ ⋅ h 2 x ≪ ( log ⁡ x) 1 / 6 − 1 / 5 δ ≪ ( log x) − 1 / 30 δ. \Big|\frac{1}{h_{1}}U_{1}-\frac{1}{h_{2}}U_{2}\Big|\ll\frac{T_{0}^{2}}{\delta}\cdot\frac{h_{2}}{x}\ll\frac{(\log x)^{1/6-1/5}}{\delta}\ll\frac{(\log x)^{-1/30}}{\delta}. |  |

On the other hand, to bound V j V_{j}, we notice that (on ℜ ⁡ s = 1 \Re s=1),

 | | η ^ j ​ ( s) | | s | = | ∫ 0 ∞ t s − 1 ​ η ​ ( t) ​ 𝑑 t | ≪ h j x ​ and ​ | η ^ j ​ ( s) | | s | ≪ 1 | s | ​ ξ ​ | s + 1 | ≪ x δ ​ h j ⋅ 1 1 + | s | 2. \frac{|\widehat{\eta}_{j}(s)|}{|s|}=\Big|\int_{0}^{\infty}t^{s-1}\eta(t)dt\Big|\ll\frac{h_{j}}{x}\text{ and }\frac{|\widehat{\eta}_{j}(s)|}{|s|}\ll\frac{1}{|s|\xi|s+1|}\ll\frac{x}{\delta h_{j}}\cdot\frac{1}{1+|s|^{2}}. |  |

Therefore splitting the integral V j V_{j} at height x / h j x/h_{j}, we get

 | | 1 h 1 ​ V 1 − 1 h 2 ​ V 2 | \displaystyle\Big|\frac{1}{h_{1}}V_{1}-\frac{1}{h_{2}}V_{2}\Big| | ≤ 1 δ ​ ∑ j = 1 2 ( ∫ 1 + i ​ T 0 1 + i ​ x / h j | M 1 ​ ( s) ​ M 2 ​ ( s) | ​ | 𝑑 s | + x h j ​ max T > x / h j ​ 1 T ​ ∫ 1 + i ​ T 1 + 2 ​ i ​ T | M 1 ​ ( s) ​ M 2 ​ ( s) | ​ | 𝑑 s |). \displaystyle\leq\frac{1}{\delta}\sum_{j=1}^{2}\Big(\int_{1+iT_{0}}^{1+ix/h_{j}}|M_{1}(s)M_{2}(s)||ds|+\frac{x}{h_{j}}\max_{T>x/h_{j}}\frac{1}{T}\int_{1+iT}^{1+2iT}|M_{1}(s)M_{2}(s)||ds|\Big). |  |

similarly to ( 19). Using Cauchy-Schwarz inequality and Proposition 1 we thus get the following bound (recall that h 1 = h ​ x, h 2 = x / ( log ⁡ x) 1 / 5 h_{1}=h\sqrt{x},h_{2}=x/(\log x)^{1/5} and h ≥ Q 1 h\geq Q_{1} by assumptions):

 | | 1 h 1 ​ V 1 − 1 h 2 ​ V 2 | ≪ ( log ⁡ Q 1) 1 / 3 δ ​ P 1 1 / 6 − η + 1 δ ​ ( log ⁡ X) 1 / 50. \Big|\frac{1}{h_{1}}V_{1}-\frac{1}{h_{2}}V_{2}\Big|\ll\frac{(\log Q_{1})^{1/3}}{\delta P_{1}^{1/6-\eta}}+\frac{1}{\delta(\log X)^{1/50}}. |  |

We now choose δ = max ( ( log Q 1) 1 / 6 / P 1 1 / 12 − η / 2, ( log X) − 1 / 100) \delta=\max((\log Q_{1})^{1/6}/P_{1}^{1/12-\eta/2},(\log X)^{-1/100}) and notice that

 | 1 h j ​ ∑ x ≤ n 1 ≤ 2 ​ x x + h j ≤ n 1 ​ n 2 ≤ x + δ ​ h j 1 ≪ δ. \frac{1}{h_{j}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ x+h_{j}\leq n_{1}n_{2}\leq x+\delta h_{j}\end{subarray}}1\ll\delta. |  |

Therefore

(30) |  | 1 h 1 ​ ∑ x ≤ n 1 ≤ 2 ​ x x − h 1 ≤ n 1 ​ n 2 ≤ x + h 1 n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) = 1 h 2 ∑ x ≤ n 1 ≤ 2 ​ x x − h 2 ≤ n 1 ​ n 2 ≤ x + h 2 n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) + + O ⁡ ( ( log ⁡ Q 1) 1 / 6 P 1 1 / 12 − η / 2 + 1 ( log ⁡ X) 1 / 100). \begin{split}\frac{1}{h_{1}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ x-h_{1}\leq n_{1}n_{2}\leq x+h_{1}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})=\frac{1}{h_{2}}&\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ x-h_{2}\leq n_{1}n_{2}\leq x+h_{2}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})+\\ &+O\Big(\frac{(\log Q_{1})^{1/6}}{P_{1}^{1/12-\eta/2}}+\frac{1}{(\log X)^{1/100}}\Big).\end{split} |  |

Finally,

 | ∑ x − h 2 ≤ n 1 ​ n 2 ≤ x + h 2 x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) \displaystyle\sum_{\begin{subarray}{c}x-h_{2}\leq n_{1}n_{2}\leq x+h_{2}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2}) | = ∑ x ≤ n 1 ≤ 2 ​ x n 1 ∈ 𝒮 f ⁡ ( n 1) ​ ∑ ( x − h 2) / n 1 ≤ n 2 ≤ ( x + h 2) / n 1 n 2 ∈ 𝒮 f ⁡ ( n 2). \displaystyle=\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1}\in\mathcal{S}\end{subarray}}f(n_{1})\sum_{\begin{subarray}{c}(x-h_{2})/n_{1}\leq n_{2}\leq(x+h_{2})/n_{1}\\ n_{2}\in\mathcal{S}\end{subarray}}f(n_{2}). |  |

and [( x − h 2) / n 1, ( x + h 2) / n 1] [(x-h_{2})/n_{1},(x+h_{2})/n_{1}] is an interval of length ≍ x / ( log ⁡ x) 1 / 5 \asymp\sqrt{x}/(\log x)^{1/5} around ≍ x \asymp\sqrt{x}. Using Lemma 4 and Lemma 5, we get

 | 1 h 2 / n 1 ∑ ( x − h 2) / n 1 ≤ n 2 ≤ ( x + h 2) / n 1 n 2 ∈ 𝒮 f ( n 2) = 2 x ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ( n) + O ( ( log x) − 1 / 20 + o ( 1)), \frac{1}{h_{2}/n_{1}}\sum_{\begin{subarray}{c}(x-h_{2})/n_{1}\leq n_{2}\leq(x+h_{2})/n_{1}\\ n_{2}\in\mathcal{S}\end{subarray}}f(n_{2})=\frac{2}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}f(n)+O((\log x)^{-1/20+o(1)}), |  |

so that

 | 1 h 2 ​ ∑ x ≤ n 1 ≤ 2 ​ x x − h 2 ≤ n 1 ​ n 2 ≤ x + h 2 n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) = 2 x ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ( n) ∑ x ≤ n 1 ≤ 2 ​ x n 1 ∈ 𝒮 f ⁡ ( n 1) n 1 + O ( ( log x) − 1 / 20 + o ( 1)) = 2 log 2 ⋅ ( 1 x ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ( n)) 2 + O ( ( log x) − 1 / 20 + o ( 1)) \begin{split}\frac{1}{h_{2}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ x-h_{2}\leq n_{1}n_{2}\leq x+h_{2}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})&=\frac{2}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}f(n)\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1}\in\mathcal{S}\end{subarray}}\frac{f(n_{1})}{n_{1}}+O((\log x)^{-1/20+o(1)})\\ &=2\log 2\cdot\Big(\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}f(n)\Big)^{2}+O((\log x)^{-1/20+o(1)})\end{split} |  |

by partial summation and Lemmas 4 and 5. The claim follows by combining this with ( 30). ∎

###### Proof of Theorem 2.

We can assume that h ≤ exp ⁡ ( ( log ⁡ x) 1 / 2) h\leq\exp((\log x)^{1/2}) since the claim for longer intervals follows by splitting the sum on the left hand side into sums over intervals of length x ​ exp ⁡ ( ( log ⁡ x) 1 / 2) \sqrt{x}\exp((\log x)^{1/2}).

We take η = 1 / 12 \eta=1/12, Q 1 = h Q_{1}=h, and P 1 = ( log ⁡ h) 40 / η = ( log ⁡ h) 480 P_{1}=(\log h)^{40/\eta}=(\log h)^{480} and for j ≥ 2 j\geq 2, the intervals [P j, Q j] [P_{j},Q_{j}] as in ( 4). Arguing as in the proof of Theorem 1, and noticing that

 | ( ∑ x ≤ n ≤ 2 ​ x 1) 2 = ∑ x ≤ n 1, n 2 ≤ 2 ​ x 1 = ( ∑ x ≤ n ≤ 2 ​ x, n ∈ 𝒮 1) 2 + ∑ x ≤ n 1, n 2 ≤ 2 ​ x n 1 ∉ 𝒮 ​ or ​ n 2 ∉ 𝒮 1, \left(\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}1\right)^{2}=\sum_{\sqrt{x}\leq n_{1},n_{2}\leq 2\sqrt{x}}1=\left(\sum_{\sqrt{x}\leq n\leq 2\sqrt{x},n\in\mathcal{S}}1\right)^{2}+\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1},n_{2}\leq 2\sqrt{x}\\ n_{1}\not\in\mathcal{S}\text{ or }n_{2}\not\in\mathcal{S}\end{subarray}}1, |  |

we obtain

 | | 1 h ​ x ​ log ⁡ 2 ​ ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x f ⁡ ( n 1) ​ f ​ ( n 2) − ( 1 x ​ ∑ x ≤ n ≤ 2 ​ x f ⁡ ( n)) 2 | ≤ | 1 h ​ x ​ log ⁡ 2 ​ ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 f ⁡ ( n 1) ​ f ​ ( n 2) − ( 1 x ​ ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 f ⁡ ( n)) 2 | + | 1 h ​ x ​ log ⁡ 2 ​ ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 1 − ( 1 x ​ ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 1) 2 | + 2 x ​ ∑ x ≤ n 1, n 2 ≤ 2 ​ x n 1 ∉ 𝒮 ​ or ​ n 2 ∉ 𝒮 1 + O ⁡ ( 1 / h). \begin{split}&\left|\frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\end{subarray}}f(n_{1})f(n_{2})-\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}f(n)\Big)^{2}\right|\\ &\leq\left|\frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}f(n_{1})f(n_{2})-\Big(\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}f(n)\Big)^{2}\right|\\ &\quad+\left|\frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\end{subarray}}1-\Big(\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\end{subarray}}1\Big)^{2}\right|+\frac{2}{x}\sum_{\begin{subarray}{c}\sqrt{x}\leq n_{1},n_{2}\leq 2\sqrt{x}\\ n_{1}\not\in\mathcal{S}\text{ or }n_{2}\not\in\mathcal{S}\end{subarray}}1+O(1/h).\end{split} |  |

Now we apply Theorem 4 to the first two terms and use the fundamental lemma of the sieve to get that

 | 1 x ​ ∑ x ≤ n ≤ 2 ​ x n ∉ 𝒮 1 ≪ ∑ j log ⁡ P j log ⁡ Q j ≪ log ⁡ P 1 log ⁡ Q 1 ≪ log ⁡ log ⁡ h log ⁡ h. \frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\notin\mathcal{S}\end{subarray}}1\ll\sum_{j}\frac{\log P_{j}}{\log Q_{j}}\ll\frac{\log P_{1}}{\log Q_{1}}\ll\frac{\log\log h}{\log h}. |  |

It follows that

 | 1 h ​ x ​ log ⁡ 2 \displaystyle\frac{1}{h\sqrt{x}\log 2} | ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x f ⁡ ( n 1) ​ f ​ ( n 2) = ( 1 x ​ ∑ x ≤ n ≤ 2 ​ x f ⁡ ( n)) 2 + \displaystyle\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\end{subarray}}f(n_{1})f(n_{2})=\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}f(n)\Big)^{2}+ |  |

 |  | + O ( ( log ⁡ h) 1 / 6 + ε P 1 1 / 12 − η / 2 + log ⁡ log ⁡ h log ⁡ h + ( log x) − 1 / 100), \displaystyle+O\Big(\frac{(\log h)^{1/6+\varepsilon}}{P_{1}^{1/12-\eta/2}}+\frac{\log\log h}{\log h}+(\log x)^{-1/100}\Big), |  |

and the claim follows recalling our choices of η \eta and P 1 P_{1}. ∎

## 11. Proofs of the corollaries

### 11.1. Smooth numbers

###### Proof of Corollary 6.

Follows immediately from Theorem 1 by taking f f to be the multiplicative function such that f ⁡ ( p ν) = 1 f(p^{\nu})=1 for p ≤ x 1 / u p\leq x^{1/u} and f ⁡ ( p ν) = 0 f(p^{\nu})=0 otherwise ∎

###### Proof of Corollary 1.

The qualitative statement in Corollary 1 would follow immediately from Theorem 2 together with the Cauchy-Schwarz inequality through the same choice of f f as in the previous proof. However, to get a better value for C ⁡ ( ε) C(\varepsilon), we prove the result using Theeorem 4 with an appropriate choice of 𝒮 \mathcal{S}.

Let δ \delta be a small positive constant, η ∈ ( 0, 1 / 6) \eta\in(0,1/6), and h h be fixed but large in terms of δ \delta and η \eta. Choose P 1 = h 1 − δ, Q 1 = h P_{1}=h^{1-\delta},Q_{1}=h, and for j ≥ 2 j\geq 2 choose

(31) |  | P j = exp ⁡ ( ( j / δ) 4 ​ j ​ ( log ⁡ h) j) and Q j = exp ⁡ ( ( j / δ) 4 ​ j + 2 ​ ( log ⁡ h) j). P_{j}=\exp((j/\delta)^{4j}(\log h)^{j})\quad\text{and}\quad Q_{j}=\exp((j/\delta)^{4j+2}(\log h)^{j}). |  |

This choice satisfies conditions ( 2) and ( 3), provided that h h is fixed but large enough in terms of δ \delta and η \eta.

Notice that with the same choice of f f as above, Theorem 4 implies that

 | 1 h ​ x ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 n 1, n 2 x ε -smooth 1 ≫ ( 1 x ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 n x ε -smooth 1) 2 + O ( ( log ⁡ Q 1) 1 / 6 P 1 1 / 12 − η + ( log x) − 1 / 100). \displaystyle\frac{1}{h\sqrt{x}}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\\ n_{1},n_{2}\text{ }x^{\varepsilon}\text{-smooth}\end{subarray}}1\gg\Big(\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\\ n\text{ }x^{\varepsilon}\text{-smooth}\end{subarray}}1\Big)^{2}+O\Big(\frac{(\log Q_{1})^{1/6}}{P_{1}^{1/12-\eta}}+(\log x)^{-1/100}\Big). |  |

The fundamental lemma of the sieve shows that for any j ≤ J j\leq J, we have

 | ∑ x ≤ n ≤ 2 ​ x p | n ⟹ p ∉ [P j, Q j] n ​ x ε -smooth 1 ≤ ( 1 + δ 2) ​ ρ ​ ( 1 / ( 2 ​ ε)) ​ x ⋅ log ⁡ P j log ⁡ Q j. \sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ p\mid n\implies p\not\in[P_{j},Q_{j}]\\ n\text{ $x^{\varepsilon}$-smooth}\end{subarray}}1\leq(1+\delta^{2})\rho(1/(2\varepsilon))\sqrt{x}\cdot\frac{\log P_{j}}{\log Q_{j}}. |  |

provided that x x is large enough, so that

 | 1 x ​ ∑ x ≤ n ≤ 2 ​ x n ∈ 𝒮 n x ε -smooth 1 ≥ 1 x ​ ∑ x ≤ n ≤ 2 ​ x n x ε -smooth 1 − 1 x ​ ∑ j = 1 J ∑ x ≤ n ≤ 2 ​ x p | n ⟹ p ∉ [P j, Q j] n ​ x ε -smooth 1 ≥ ρ ⁡ ( 1 / ( 2 ​ ε)) ​ ( 1 + o ⁡ ( 1)) − ∑ j = 1 J ( 1 + δ 2) ​ ρ ​ ( 1 / ( 2 ​ ε)) ⋅ log ⁡ P j log ⁡ Q j ≥ ρ ⁡ ( 1 / ( 2 ​ ε)) ​ ( 1 + o ⁡ ( 1) − ( 1 + δ 2) ​ ( 1 − δ) − ∑ j = 2 J δ 2 j 2) ≥ δ / 2 ⋅ ρ ⁡ ( 1 / ( 2 ​ ε)). \begin{split}\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\in\mathcal{S}\\ n\text{ }x^{\varepsilon}\text{-smooth}\end{subarray}}1&\geq\frac{1}{\sqrt{x}}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ n\text{ }x^{\varepsilon}\text{-smooth}\end{subarray}}1-\frac{1}{\sqrt{x}}\sum_{j=1}^{J}\sum_{\begin{subarray}{c}\sqrt{x}\leq n\leq 2\sqrt{x}\\ p\mid n\implies p\not\in[P_{j},Q_{j}]\\ n\text{ $x^{\varepsilon}$-smooth}\end{subarray}}1\\ &\geq\rho(1/(2\varepsilon))(1+o(1))-\sum_{j=1}^{J}(1+\delta^{2})\rho(1/(2\varepsilon))\cdot\frac{\log P_{j}}{\log Q_{j}}\\ &\geq\rho(1/(2\varepsilon))\left(1+o(1)-(1+\delta^{2})(1-\delta)-\sum_{j=2}^{J}\frac{\delta^{2}}{j^{2}}\right)\\ &\geq\delta/2\cdot\rho(1/(2\varepsilon)).\end{split} |  |

Hence

 | 1 h ​ x ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x n 1, n 2 ∈ 𝒮 n 1, n 2 x ε -smooth 1 ≫ δ 2 ρ ( 1 / ( 2 ε)) 2 + O ( h − ( 1 − δ) / 12 + 1 / 1000 + ( log x) − 1 / 100). \displaystyle\frac{1}{h\sqrt{x}}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\\ n_{1},n_{2}\in\mathcal{S}\\ n_{1},n_{2}\text{ }x^{\varepsilon}\text{-smooth}\end{subarray}}1\gg\delta^{2}\rho(1/(2\varepsilon))^{2}+O\Big(h^{-(1-\delta)/12+1/1000}+(\log x)^{-1/100}\Big). |  |

Therefore for any small enough δ > 0 \delta>0, and all x x large enough, the left-hand side is

 | ≫ δ 2 ρ ( 1 / ε) 1.01 + O ( h − 1 / 12 + 2 δ + 1 / 1000 + ( log x) − 1 / 100) \gg\delta^{2}\rho(1/\varepsilon)^{1.01}+O\Big(h^{-1/12+2\delta+1/1000}+(\log x)^{-1/100}\Big) |  |

It follows that the lower bound is positive if h = ρ ​ ( 1 / ε) − 13 h=\rho(1/\varepsilon)^{-13} and δ, ε \delta,\varepsilon are taken small enough. We conclude by using the Cauchy-Schwarz inequality, noting that

 | x ≪ ( ∑ x ≤ n ≤ x + C ​ x n ​ x ε -smooth 1) 1 / 2 ​ ( ∑ x ≤ n ≤ x + C ​ x ( ∑ n 1 ​ n 2 = n 1) 2) 1 / 2 ≪ ( ∑ x ≤ n ≤ x + C ​ x n ​ x ε -smooth 1) 1 / 2 ​ ( x ​ ( log ⁡ x) 4) 1 / 2 \begin{split}\sqrt{x}&\ll\left(\sum_{\begin{subarray}{c}x\leq n\leq x+C\sqrt{x}\\ n\text{ $x^{\varepsilon}$-smooth}\end{subarray}}1\right)^{1/2}\left(\sum_{x\leq n\leq x+C\sqrt{x}}\left(\sum_{n_{1}n_{2}=n}1\right)^{2}\right)^{1/2}\\ &\ll\left(\sum_{\begin{subarray}{c}x\leq n\leq x+C\sqrt{x}\\ n\text{ $x^{\varepsilon}$-smooth}\end{subarray}}1\right)^{1/2}\left(\sqrt{x}(\log x)^{4}\right)^{1/2}\end{split} |  |

and the claim follows. ∎

### 11.2. Signs of multiplicative functions

###### Proof of Corollary 4.

First notice that the condition that f ⁡ ( n) ≠ 0 f(n)\neq 0 for a positive proportion of n n is equivalent to ∑ p, f ⁡ ( p) = 0 1 p < ∞ \sum_{p,f(p)=0}\frac{1}{p}<\infty, and also that we can assume without loss of generality that f ⁡ ( n) ∈ { − 1, 0, 1 } f(n)\in\{-1,0,1\}. The qualitative statement in Corollary 4 would follow from Theorem 1 using a slightly simpler variant of the argument below. However, to get a better bound for the size of the exceptional set, we prove the result using Theeorem 3 with an appropriate choice of 𝒮 \mathcal{S}.

Let us choose P j P_{j} and Q j Q_{j} and thus 𝒮 \mathcal{S} as in the proof of Corollary 1 in previous subsection, with δ \delta small but fixed. By ( 13) together with Lemma 5,

 | 1 X ∑ X ≤ n ≤ 2 ​ X n ∈ 𝒮 g ( n) = 1 X ∑ n ≤ X n ∈ 𝒮 g ( n) + O ( ( log X) − 1 / 20 + o ( 1)). \frac{1}{X}\sum_{\begin{subarray}{c}X\leq n\leq 2X\\ n\in\mathcal{S}\end{subarray}}g(n)=\frac{1}{X}\sum_{\begin{subarray}{c}n\leq X\\ n\in\mathcal{S}\end{subarray}}g(n)+O((\log X)^{-1/20+o(1)}). |  |

for g = f g=f and g = | f | g=|f|. Let p 0 ν p_{0}^{\nu} be the smallest prime power for which f ⁡ ( p 0 ν) = − 1 f(p_{0}^{\nu})=-1. Now

 | ∑ n ≤ X n ∈ 𝒮 | f ⁡ ( n) | − f ⁡ ( n) ≥ ∑ n ≤ X / p 0 ν n ∈ 𝒮, p 0 ∤ n | f ⁡ ( n) | − f ⁡ ( n) + | f ⁡ ( p 0 ν ​ n) | − f ⁡ ( p 0 ν ​ n) = 2 ​ ∑ n ≤ X / p 0 ν n ∈ 𝒮, p 0 ∤ n | f ⁡ ( n) | ≫ X \sum_{\begin{subarray}{c}n\leq X\\ n\in\mathcal{S}\end{subarray}}|f(n)|-f(n)\geq\sum_{\begin{subarray}{c}n\leq X/p_{0}^{\nu}\\ n\in\mathcal{S},p_{0}\nmid n\end{subarray}}|f(n)|-f(n)+|f(p_{0}^{\nu}n)|-f(p_{0}^{\nu}n)=2\sum_{\begin{subarray}{c}n\leq X/p_{0}^{\nu}\\ n\in\mathcal{S},p_{0}\nmid n\end{subarray}}|f(n)|\gg X |  |

by the fundamental lemma of sieve, similarly to the proof of Corollary 1.

Applying Theorem 3 to f ⁡ ( n) f(n) and | f ⁡ ( n) | |f(n)| we obtain that

 | ∑ x ≤ n ≤ x + h n ∈ 𝒮 | f ⁡ ( n) | − f ⁡ ( n) ≫ h \sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}|f(n)|-f(n)\gg h |  |

for all but at most

(32) |  | ≪ ( log ⁡ h) 1 / 3 h ( 1 − ε) ​ ( 1 / 6 − η) + 1 ( log ⁡ X) 1 / 50 \ll\frac{(\log h)^{1/3}}{h^{(1-\varepsilon)(1/6-\eta)}}+\frac{1}{(\log X)^{1/50}} |  |

integers x ∈ [X, 2 ​ X] x\in[X,2X]. Hence f ⁡ ( n) f(n) is negative in almost all short intervals. Similarly we can show that

 | ∑ x ≤ n ≤ x + h n ∈ 𝒮 | f ⁡ ( n) | + f ⁡ ( n) ≫ h \sum_{\begin{subarray}{c}x\leq n\leq x+h\\ n\in\mathcal{S}\end{subarray}}|f(n)|+f(n)\gg h |  |

for all but at most ( 32) exceptional integers x ∈ [X, 2 ​ X] x\in[X,2X]. Hence f ⁡ ( n) f(n) must be positive in almost all short intervals, and the claim follows. We actually get that the number of exceptions is ≪ X / h 1 / 6 − ε + ( log X) − 1 / 50 \ll X/h^{1/6-\varepsilon}+(\log X)^{-1/50} for any ε > 0 \varepsilon>0. ∎

It is worth remarking that when ∑ f ⁡ ( p) < 0 1 / p < ∞ \sum_{f(p)<0}1/p<\infty, one can work out directly the number of sign changes of f f up to x x. For example for non-vanishing completely multiplicative f f such that ∑ f ⁡ ( p) < 0 1 / p < ∞ \sum_{f(p)<0}1/p<\infty, the number of sign changes up to x x is asymptotically

 | x ⋅ ( 1 2 − 1 2 ∏ p: f ⁡ ( p) < 0 ( 1 − 4 p + 1)). x\cdot\Big(\frac{1}{2}-\frac{1}{2}\prod_{p\colon f(p)<0}\Big(1-\frac{4}{p+1}\Big)\Big). |  |

Such formulas were pointed out to us by Andrew Granville and Greg Martin, and essentially the formula in general case as well as its proof can be found from a paper by Lucht and Tuttas [26].

###### Proof of Corollary 3.

Follows immediately from the proof of Corollary 4. ∎

###### Proof of Corollary 2.

By Corollary 3, there is a positive proportion δ \delta of integers n n such that f ⁡ ( n) ​ f ​ ( n + 1) ≤ 0 f(n)f(n+1)\leq 0. Hence

 | ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + 1) ≤ ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + 1) > 0 1 ≤ ( 1 − δ) ​ x. \sum_{n\leq x}f(n)f(n+1)\leq\sum_{\begin{subarray}{c}n\leq x\\ f(n)f(n+1)>0\end{subarray}}1\leq(1-\delta)x. |  |

On the other hand,

 | f ⁡ ( n) ​ f ​ ( n + 1) ​ f ​ ( 2 ​ n) ​ f ​ ( 2 ​ n + 1) 2 ​ f ​ ( 2 ​ ( n + 1)) = ( f ⁡ ( 2) ​ f ​ ( n) ​ f ​ ( n + 1) ​ f ​ ( 2 ​ n + 1)) 2 ≥ 0, f(n)f(n+1)f(2n)f(2n+1)^{2}f(2(n+1))=(f(2)f(n)f(n+1)f(2n+1))^{2}\geq 0, |  |

so that one of f ⁡ ( n) ​ f ​ ( n + 1) f(n)f(n+1), f ⁡ ( 2 ​ n) ​ f ​ ( 2 ​ n + 1) f(2n)f(2n+1) and f ⁡ ( 2 ​ n + 1) ​ f ​ ( 2 ​ n + 2) f(2n+1)f(2n+2) must be non-negative, so that

 | ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + 1) ≥ ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + 1) < 0 ( − 1) ≥ − ( 1 − δ) ​ x. \sum_{n\leq x}f(n)f(n+1)\geq\sum_{\begin{subarray}{c}n\leq x\\ f(n)f(n+1)<0\end{subarray}}(-1)\geq-(1-\delta)x. |  |

Hence

(33) |  | | ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + 1) | ≤ ( 1 − δ) ​ x. \left|\sum_{n\leq x}f(n)f(n+1)\right|\leq(1-\delta)x. |  |

For h ≥ 2 h\geq 2,

 | | ∑ n ≤ x f ⁡ ( n) ​ f ​ ( n + h) | ≤ | ∑ n ≤ x h ∤ n f ⁡ ( n) ​ f ​ ( n + h) | + | ∑ n ≤ x h | n f ⁡ ( n) ​ f ​ ( n + h) | ≤ ( 1 − 1 h) ​ x + 1 + | f ⁡ ( h) | ​ | ∑ n ≤ x / h f ⁡ ( n) ​ f ​ ( n + 1) | ≤ ( 1 − 1 h) ​ x + 1 + ( 1 − δ) ​ x h < ( 1 − δ ⁡ ( h)) ​ x \begin{split}\left|\sum_{n\leq x}f(n)f(n+h)\right|&\leq\left|\sum_{\begin{subarray}{c}n\leq x\\ h\nmid n\end{subarray}}f(n)f(n+h)\right|+\left|\sum_{\begin{subarray}{c}n\leq x\\ h\mid n\end{subarray}}f(n)f(n+h)\right|\\ &\leq\left(1-\frac{1}{h}\right)x+1+|f(h)|\left|\sum_{n\leq x/h}f(n)f(n+1)\right|\\ &\leq\left(1-\frac{1}{h}\right)x+1+(1-\delta)\frac{x}{h}<(1-\delta(h))x\end{split} |  |

by ( 33). ∎

###### Proof of Corollary 5.

Without loss of generality we can assume that f ⁡ ( n) ∈ { − 1, 0, 1 } f(n)\in\{-1,0,1\}. Theorem 2 implies that for any multiplicative function g: ℕ → [− 1, 1] g:\mathbb{N}\rightarrow[-1,1],

(34) |  | 1 h ​ x ​ log ⁡ 2 ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x g ( n 1) g ( n 2) = ( 1 x ∑ x ≤ n ≤ 2 ​ x g ( n)) 2 + O ( ( log h) − 1 / 100). \frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\end{subarray}}g(n_{1})g(n_{2})=\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}g(n)\Big)^{2}+O((\log h)^{-1/100}). |  |

Let us study, for a given f f,

 | S ± = 1 h ​ x ​ log ⁡ 2 ​ ∑ x ≤ n 1 ​ n 2 ≤ x + h ​ x x ≤ n 1 ≤ 2 ​ x ( | f ⁡ ( n 1) ​ f ​ ( n 2) | ± f ⁡ ( n 1) ​ f ​ ( n 2)). S^{\pm}=\frac{1}{h\sqrt{x}\log 2}\sum_{\begin{subarray}{c}x\leq n_{1}n_{2}\leq x+h\sqrt{x}\\ \sqrt{x}\leq n_{1}\leq 2\sqrt{x}\end{subarray}}(|f(n_{1})f(n_{2})|\pm f(n_{1})f(n_{2})). |  |

We will show that S + > 0 S^{+}>0 and S − > 0 S^{-}>0. First of these implies that there is n ∈ [x, x + h ​ x] n\in[x,x+h\sqrt{x}] such that f ⁡ ( n) > 0 f(n)>0 (since f f is assumed to be completely multiplicative) whereas the second one implies that there is n ∈ [x, x + h ​ x] n\in[x,x+h\sqrt{x}] such that f ⁡ ( n) < 0 f(n)<0.

By ( 34)

 | S ± = ( 1 x ∑ x ≤ n ≤ 2 ​ x | f ( n) |) 2 ± ( 1 x ∑ x ≤ n ≤ 2 ​ x f ( n)) 2 + O ( ( log h) − 1 / 100). S^{\pm}=\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}|f(n)|\Big)^{2}\pm\Big(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}f(n)\Big)^{2}+O((\log h)^{-1/100}). |  |

Here the first square is ≫ 1 \gg 1 by assumption that f f is non-vanishing for positive proportion of n n, so that immediately S + ≫ 1 S^{+}\gg 1. On the other hand

 | S − = ( 1 x ∑ x ≤ n ≤ 2 ​ x ( | f ( n) | + f ( n))) ⋅ ( 1 x ∑ x ≤ n ≤ 2 ​ x ( | f ( n) | − f ( n))) + O ( ( log h) − 1 / 100). S^{-}=\left(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}(|f(n)|+f(n))\right)\cdot\left(\frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}(|f(n)|-f(n))\right)+O((\log h)^{-1/100}). |  |

Arguing as in beginning of proof of Corollary 4,

 | 1 x ​ ∑ x ≤ n ≤ 2 ​ x ( | f ⁡ ( n) | ± f ⁡ ( n)) ≫ 1, \frac{1}{\sqrt{x}}\sum_{\sqrt{x}\leq n\leq 2\sqrt{x}}(|f(n)|\pm f(n))\gg 1, |  |

so that also S − ≫ 1 S^{-}\gg 1 and the claim follows. ∎

It is worth noticing that the case ∑ p: f ⁡ ( p) < 0 1 p < ∞ \sum_{\begin{subarray}{c}p\colon f(p)<0\end{subarray}}\frac{1}{p}<\infty is easier than the general case — actually it follows from work of Kowalski, Robert and Wu [22] on 𝔅 \mathfrak{B} -free numbers in short intervals that f f has a sign change in all intervals [x, x + x θ] [x,x+x^{\theta}] for any θ > 7 / 17 \theta>7/17.

## Acknowledgements

The authors would like to thank Andrew Granville for many useful discussions on the topic. They would also like to thank the anonymous referee and Joni Teräväinen for careful reading of the manuscript. The first author was supported by the Academy of Finland grants no. 137883 and 138522.

## References

- [1] A. Balog. On the distribution of integers having no large prime factor. Astérisque, (147-148):27–31, 343, 1987. Journées arithmétiques de Besançon (Besançon, 1985).
- [2] J. Cassaigne, S. Ferenczi, C. Mauduit, J. Rivat, and A. Sárközy. On finite pseudorandom binary sequences. III. The Liouville function. I. Acta Arith., 87(4):367–390, 1999.
- [3] E. S. Croot, III. On the oscillations of multiplicative functions taking values ± 1 \pm 1. J. Number Theory, 98(1):184–194, 2003.
- [4] E. S. Croot, III. Smooth numbers in short intervals. Int. J. Number Theory, 3(1):159–169, 2007.
- [5] P. D. T. A. Elliott. On the correlation of multiplicative functions. Notas Soc. Mat. Chile, 11(1):1–11, 1992.
- [6] P. D. T. A. Elliott. Duality in analytic number theory, volume 122 of Cambridge Tracts in Mathematics. Cambridge University Press, Cambridge, 1997.
- [7] C. Elsholtz and D. S. Gunderson. Congruence properties of multiplicative functions on sumsets and monochromatic solutions of linear equations. Funct. Approx. Comment. Math., 52(2):263–281, 2015.
- [8] J. Friedlander and H. Iwaniec. Opera de cribro, volume 57 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2010.
- [9] J. B. Friedlander and A. Granville. Smoothing “smooth” numbers. Philos. Trans. Roy. Soc. London Ser. A, 345(1676):339–347, 1993.
- [10] A. Ghosh and P. Sarnak. Real zeros of holomorphic Hecke cusp forms. J. Eur. Math. Soc. (JEMS), 14(2):465–487, 2012.
- [11] A. Granville. Smooth numbers: computational number theory and beyond. In Algorithmic number theory: lattices, number fields, curves and cryptography, volume 44 of Math. Sci. Res. Inst. Publ., pages 267–323. Cambridge Univ. Press, Cambridge, 2008.
- [12] A. Granville and K. Soundararajan. Decay of mean values of multiplicative functions. Canad. J. Math., 55(6):1191–1230, 2003.
- [13] J. Hafner. On smooth numbers in short intervals under the Riemann hypothesis. pre-print, 1993.
- [14] G. Harman. Prime-detecting Sieves, volume 33 of London Mathematical Society Monographs (New Series). Princeton University Press, Princeton, 2007.
- [15] G. Harman, J. Pintz, and D. Wolke. A note on the Möbius and Liouville functions. Studia Sci. Math. Hungar., 20(1-4):295–299, 1985.
- [16] A. Harper. Sharp conditional bounds for moments of the zeta function. Preprint, available at `http://arxiv.org`as arXiv:1305.4618 [math.NT].
- [17] A. Hildebrand. Math. Reviews, review no. 95d:11099.
- [18] A. Hildebrand. Multiplicative functions at consecutive integers. Math. Proc. Cambridge Philos. Soc., 100(2):229–236, 1986.
- [19] A. Ivić. The Riemann Zeta-Function. Theory and Applications. Dover Publications, New York, 2003, reprint of the 1985 original.
- [20] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, Rhode Island, 2004.
- [21] M. Jutila. Zero-density estimates for L L -functions. Acta Arith., 32(1):55–62, 1977.
- [22] E. Kowalski, O. Robert, and J. Wu. Small gaps in coefficients of L L -functions and 𝔅 \mathfrak{B} -free numbers in short intervals. Rev. Mat. Iberoam., 23(1):281–326, 2007.
- [23] Y.-K. Lau, J.Y. Liu, and J. Wu. Coefficients of symmetric square L L -functions. Sci. China Math., 53(9):2317–2328, 2010.
- [24] H. W. Lenstra, Jr. Elliptic curves and number-theoretic algorithms. In Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Berkeley, Calif., 1986), pages 99–120. Amer. Math. Soc., Providence, RI, 1987.
- [25] S. Lester, K. Matomäki, and M. Radziwiłł. Small scale distribution of zeros and mass of modular forms. Preprint, available at `http://arxiv.org`as arXiv:1501.01292 [math.NT].
- [26] L. Lucht and F. Tuttas. Aufeinanderfolgende Elemente in multiplikativen Zahlenmengen. Monatsh. Math., 87(1):15–19, 1979.
- [27] K. Matomäki. A note on smooth numbers in short intervals. Int. J. Number Theory, 6(5):1113–1116, 2010.
- [28] K. Matomäki. Another note on smooth numbers in short intervals. Int. J. Number Theory, to appear, available at `http://users.utu.fi/ksmato/papers/Smoothshorts2.pdf`.
- [29] K. Matomäki and M. Radziwiłł. A note on the Liouville function in short intervals. Preprint, available at `http://arxiv.org`as arXiv:1502.02374 [math.NT].
- [30] K. Matomäki and M. Radziwiłł. Sign changes of Hecke eigenvalues. Geom. Funct. Anal., to appear, Preprint available at `http://arxiv.org`as arXiv:1405.7671v1 [math.NT].
- [31] K. Matomäki, M. Radziwiłł, and T. Tao. An averaged form of Chowla’s conjecture. Algebra & Number theory, to appear, available at `http://arxiv.org`as arXiv:1503.05121 [math.NT].
- [32] H. L. Montgomery. Ten lectures on the interface between analytic number theory and harmonic analysis, volume 84 of CBMS Regional Conference Series in Mathematics. Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994.
- [33] M. Radziwiłł and K. Soundararajan. Moments and distribution of central L L -values of quadratic twists of elliptic curves. Invent. Math, to appear, available at `http://arxiv.org`as arXiv:1403.7067 [math.NT].
- [34] K. Ramachandra. Some problems of analytic number theory. Acta Arith., 31(4):313–324, 1976.
- [35] B. Saffari and R. C. Vaughan. On the fractional parts of x / n x/n and related sequences II. Ann. Inst. Fourier, 27:1–30, 1977.
- [36] P. Shiu. A Brun-Titchmarsh theorem for multiplicative functions. J. Reine Angew. Math., 313:161–170, 1980.
- [37] K. Soundararajan. Smooth numbers in short intervals. Preprint, available at `http://arxiv.org`as arXiv:1009.1591v1 [math.NT].
- [38] G. Tenenbaum. Introduction to analytic and probabilistic number theory, volume 46 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 1995. Translated from the second French edition (1995) by C. B. Thomas.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:ksmato@utu.fi
[4]: mailto:maksym.radziwill@gmail.com
