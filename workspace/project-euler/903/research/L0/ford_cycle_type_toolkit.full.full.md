<!-- source: https://ar5iv.labs.arxiv.org/html/2104.12019 | converted from HTML -->

[2104.12019] 1Introduction

###### Abstract

We provide a standard reference for fundamental distributional results about the cycle type of a random permutation σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}, emphasizing methods which are combinatorial or probabilistic in nature and adaptable to other situations. Many of our techniques are borrowed from methods used to prove analogous theorems about the prime factorization of random integers. Included here are results about the proportion of permutations σ \sigma having a given number of cycles with lengths from a given set, the distribution of the smallest and largest cycle, and the distribution of the sizes of fixed sets of σ \sigma.

† † daj-author-details: title = Cycle Type of Random Permutations:
a Toolkit, author = Kevin Ford, plaintextauthor = Kevin Ford, keywords = random permutations, cycle type, , † † daj-editor-details: year=2022, number=9, received=10 May 2021, revised=18 February 2022, published=8 September 2022, doi=10.19086/da.38090,

## 1 Introduction

The theory of the cycle type of random permutations of the symmetric group 𝒮 n \mathcal{S}_{n} is very active, with many applications in combinatorics, group theory and number theory. A selection of applications includes

- •

the distribution of orders of permutations (the least common multiple of cycle lengths) [1, 7, 10, 13, 22, 23, 24, 25, 26, 27, 28, 38, 50, 57, 61, 62, 63] and [40, Sec. 6];

- •

invariable generation of the symmetric group [16, 18, 53, 67] and other classical groups [59];

- •

the distribution of fixed sets (divisors) of permutations [14, 17, 18, 19, 33, 53, 73];

- •

permutations contained in transitive subgroups [12, 19, 45];

- •

irreducibility of polynomials over the rationals [8, 9];

- •

permutation groups containing elements with a single cycle that is not a fixed point (Jordan groups) [45, 37] and [69, Ch. 10];

- •

polynomial factorization in finite fields [3, 8, 68].

The main purpose of this paper is provide a standard reference for fundamental distributional results about cycle types, which heretofore have been scattered across many papers with widely varying strength and generality. We showcase methods which are both *general*and *combinatorial*. While many of the results stated here are weaker than existing results in the literature, they are far more general, have significantly shorter proofs and are more adaptable to new situations. This paper is an expanded version of portions of the author’s lecture notes on permutations prepared for the course “Anatomy of integers and random permutations”.

Our methods are borrowed from the theory of numbers, particularly the theory of sieves and the theory of averages of multiplicative functions (see [48, Part 3, Part 4] for uses in number theory). As positive integers factor uniquely into a product of prime numbers, and permutations factor uniquely into a product of cycles, the connection between the distributions of the two objects, prime factors and cycles, is not surprising. The first explicit mention of such a connection, however, is the paper of Knuth and Trabb Pardo [46] in 1976. On the other hand, there are significant differences in the structure of the two objects which explains why there is no simple *transference principle*between statements about prime factorizations and the corresponding statement about the cycle structure of permutations. Deeper inspection, however, reveals that the *distribution*of the two factorizations have many common features, and for much the same underlying reasons.

Let σ \sigma denote a random permutation from the symmetric group 𝒮 n \mathcal{S}_{n}, each permutation being equally likely 1 1 1 Random permutations sampled from certain other distributions have been studied, e.g. [4], but we will not discuss these here.. We denote by ℙ n \mathbb{P}_{n} and 𝔼 n {\mathbb{E}}\,_{n} the probability and expectation with respect to a uniform random σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}. Often, the subscript n n will be omitted if it is clear from the context. We denote the type (or cycle type) of σ \sigma by

 | ( C 1 ​ ( σ), C 2 ​ ( σ), …, C n ​ ( σ)), (C_{1}(\sigma),C_{2}(\sigma),\ldots,C_{n}(\sigma)), |  |

where C j ​ ( σ) C_{j}(\sigma) is the number of cycles of length j j in σ \sigma. More generally, for any subset I I of [n] = { 1, …, n } [n]=\{1,\ldots,n\}, we let C I ​ ( σ) C_{I}(\sigma) be the number of cycles whose lengths lie in the set I I. For brevity, we write C ⁡ ( σ) C(\sigma) for the total number of cycles in σ \sigma. The principal problems considered in this paper are

- (a)

What is the distribution of C j ​ ( σ) C_{j}(\sigma) for each j j?

- (b)

What is the distribution of C I ​ ( σ) C_{I}(\sigma) for each I I?

- (c)

What is the joint distribution of C I 1 ​ ( σ), …, C I k ​ ( σ) C_{I_{1}}(\sigma),\ldots,C_{I_{k}}(\sigma) for disjoint sets I 1, …, I k ⊆ [n] I_{1},\ldots,I_{k}\subseteq[n]?

- (d)

What is the distribution of C I ​ ( σ) C_{I}(\sigma) conditional on C ⁡ ( σ) = k C(\sigma)=k?

Most of the analysis of these problems in the literature utilizes recurrence relations, properties of Stirling numbers, or complex analytic methods starting with the exponential generating function of Gruder [41, Satz 2] for permutations having only cycle sizes from a set I I. See, e.g. [29] for a general analytic theory.

###### Theorem 1.1 (Gruder).

For complex x x and y y with | x | < 1 |x|<1, and subset I ⊆ ℕ I\subseteq{\mathbb{N}} we have

 | ∑ k ∑ n ℙ n ​ ( C I ​ ( σ) = k, C [n] ∖ I ​ ( σ) = 0) ​ x n ​ y k = exp ⁡ { y ​ ∑ m ∈ I x m m }. \sum_{k}\sum_{n}\mathbb{P}_{n}\big(C_{I}(\sigma)=k,C_{[n]\setminus I}(\sigma)=0\big)x^{n}y^{k}=\exp\bigg\{y\sum_{m\in I}\frac{x^{m}}{m}\bigg\}. |  | (1) |

Moreover, when I I is finite the above identity holds for every complex x x.

While some existing distribution theorems are very strong, in particular the recent results of Manstavičius and Petuchovas [55, 56, 65, 66], the methods are highly specialized and not easily adaptable to the solution of related problems. By contrast, we eschew recurrences and generating functions (for the most part) in favor of direct arguments. We focus on *quantitative*results, that is, with a specific rate of convergence, as well as results that are *uniform*in j, I j,I and the sets I j I_{j}.

Underlying our analysis is the *Poisson model*of permutations, which suggests that C j ​ ( σ) C_{j}(\sigma) is approximately Poisson with parameter 1 / j 1/j, and that C 1 ​ ( σ), C 2 ​ ( σ), … C_{1}(\sigma),C_{2}(\sigma),\ldots are nearly independent. This is already hinted at in Cauchy’s classical formula:

###### Theorem 1.2 (Cauchy).

If m 1 + 2 ​ m 2 + ⋯ + n ​ m n = n m_{1}+2m_{2}+\cdots+nm_{n}=n, then

 | ℙ n ​ ( C 1 ​ ( σ) = m 1, …, C n ​ ( σ) = m n) = ∏ j = 1 n ( 1 / j) m j m j!. \mathbb{P}_{n}\big(C_{1}(\sigma)=m_{1},\ldots,C_{n}(\sigma)=m_{n}\big)=\prod_{j=1}^{n}\frac{(1/j)^{m_{j}}}{m_{j}!}. |  |

If X 1, X 2, …, X k X_{1},X_{2},\ldots,X_{k} are independent Poisson random variables with parameters λ 1, …, λ k \lambda_{1},\ldots,\lambda_{k}, respectively, then the sum X 1 + ⋯ + X k X_{1}+\cdots+X_{k} is Poisson with parameter λ 1 + ⋯ + λ k \lambda_{1}+\cdots+\lambda_{k}. Thus, for subsets I I of [n] [n] we should expect that C I ​ ( σ) C_{I}(\sigma) will be roughly Poisson with parameter

 | H ⁡ ( I):= ∑ j ∈ I 1 j. H(I):=\sum_{j\in I}\frac{1}{j}. |  |

In the important special case I = { 1, …, n } I=\{1,\ldots,n\} we set

 | H n = ∑ i = 1 n 1 i. H_{n}=\sum_{i=1}^{n}\frac{1}{i}. |  |

The Poisson model has limitations, however, particularly if I I contains many large elements. For example the events “ C j ​ ( σ) ⩾ 1 C_{j}(\sigma)\geqslant 1 ”, n / 2 < j ⩽ n n/2<j\leqslant n, are clearly disjoint. Also, if I = { 2, …, n } I=\{2,\ldots,n\}, then ℙ ⁡ ( C I ​ ( σ) = 0) = 1 / n! \mathbb{P}(C_{I}(\sigma)=0)=1/n! whereas the Poisson model predicts a probability of about e − H ⁡ ( I) ≈ 1 / n \mathrm{e}^{-H(I)}\approx 1/n. In general, permutations lacking large cycles are much rarer than would be predicted by the Poisson model, these being analogous to integers lacking large prime factors. We will take up this subject again later, e.g. Theorem 1.16. On the other hand, we shall see that the Poisson model is very accurate for small j j, and is reasonably accurate for large j j on average near the center of the distribution.

In the remainder of the introductory section, we describe a number of results, most of which will be proved in subsequent sections.

### 1.1 Notational conventions.

We adopt the standard Bachman-Landau, Hardy, and Vinogradov notations: f = O ⁡ ( g) f=O(g) and f ≪ g f\ll g mean that there is a positive constant C C so that | f | ⩽ C ​ g |f|\leqslant Cg throughout the domain of f f. The constant C C is independent of any parameters, unless specified by subscripts, e.g. f ⁡ ( x) = O ε ​ ( x ε) f(x)=O_{\varepsilon}(x^{\varepsilon}). Also, f ⁡ ( x) ∼ g ⁡ ( x) f(x)\sim g(x) as x → ∞ x\to\infty means lim x → ∞ f ⁡ ( x) / g ⁡ ( x) = 1 \lim_{x\to\infty}f(x)/g(x)=1 and f ⁡ ( x) = o ⁡ ( g ⁡ ( x)) f(x)=o(g(x)) means that lim x → ∞ f ⁡ ( x) / g ⁡ ( x) = 0 \lim_{x\to\infty}f(x)/g(x)=0.

For σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}, the notation β | σ \beta|\sigma means that β \beta is a *divisor*of the permutation σ \sigma, i.e. a product of some subset of the cycles of σ \sigma. | β | |\beta| is the size (length) of β \beta.

𝟙 ​ ( S) \mathbbm{1}(S) is the indicator function of statement S S; 𝟙 ​ ( S) = { 1 S ​ is true 0 S ​ is false. \displaystyle\mathbbm{1}(S)=\begin{cases}1&S\text{ is true}\\ 0&S\text{ is false}.\end{cases}

### 1.2 Binomial moments.

A great deal of our analysis ultimately relies on estimates for joint binomial moments of the quantities C I ​ ( σ) C_{I}(\sigma). Recall that if X X is Poisson with parameter λ \lambda, then for any non-negative integer m m,

 | 𝔼 ​ ( X m) = ∑ k = 0 ∞ ( k m) ​ e − λ ​ λ k k! = λ m m!. {\mathbb{E}}\,\binom{X}{m}=\sum_{k=0}^{\infty}\binom{k}{m}\mathrm{e}^{-\lambda}\frac{\lambda^{k}}{k!}=\frac{\lambda^{m}}{m!}. |  |

We establish an analog for joint binomial moments of the statistics C I j ​ ( σ) C_{I_{j}}(\sigma) for disjoint I 1, …, I k I_{1},\ldots,I_{k}.

###### Theorem 1.3.

Let I 1, I 2, …, I k I_{1},I_{2},\ldots,I_{k} be disjoint, nonempty subsets of [n] [n], and let m 1, …, m k m_{1},\ldots,m_{k} be non-negative integers. Then

 | 𝔼 ( C I 1 ​ ( σ) m 1) ⋯ ( C I k ​ ( σ) m k) ⩽ ∏ j = 1 k H ​ ( I j) m j m j!, {\mathbb{E}}\,\binom{C_{I_{1}}(\sigma)}{m_{1}}\cdots\binom{C_{I_{k}}(\sigma)}{m_{k}}\leqslant\prod_{j=1}^{k}\frac{H(I_{j})^{m_{j}}}{m_{j}!}, |  |

with equality if and only if ∑ j = 1 k m j ​ max ⁡ ( I j) ⩽ n \sum_{j=1}^{k}m_{j}\max(I_{j})\leqslant n.

In the special case k = 1 k=1, I 1 = [m] I_{1}=[m] and m 1 = 1 m_{1}=1 we have

 | 𝔼 ​ C [m] ​ ( σ) = H m = log ⁡ m + γ + O ⁡ ( 1 / m). {\mathbb{E}}\,C_{[m]}(\sigma)=H_{m}=\log m+\gamma+O(1/m). |  | (2) |

Theorem 1.3 will be proved in Section 3, where we will also give short deductions of Theorems 1.1 and 1.2 from Theorem 1.3.

### 1.3 Local limit theorems

We begin with an exact evaluation of the local limit laws for C j ​ ( σ) C_{j}(\sigma), due to Goncharov [39].

###### Theorem 1.4 (Goncharov).

For any n ∈ ℕ n\in{\mathbb{N}}, 1 ⩽ j ⩽ n 1\leqslant j\leqslant n and 0 ⩽ m ⩽ n / j 0\leqslant m\leqslant n/j, we have

 | ℙ ( C j ( σ) = m) = ( 1 / j) m m! ∑ h = 0 ⌊ n / j ⌋ − m ( − 1 / j) h h!, ( 1 ⩽ j ⩽ n, 0 ⩽ m ⩽ n / j). \mathbb{P}\left(C_{j}(\sigma)=m\right)=\frac{(1/j)^{m}}{m!}\sum_{h=0}^{{\left\lfloor{n/j}\right\rfloor}-m}\frac{(-1/j)^{h}}{h!},\quad(1\leqslant j\leqslant n,0\leqslant m\leqslant n/j). |  |

A special case is the very classical *derangement problem*, posed in 1708 by Pierre Raymond de Montmort. Taking j = 1 j=1 we have the exact formula for derangements

 | ℙ ⁡ ( C 1 ​ ( σ) = 0) = ∑ j = 0 n ( − 1) j j!. \mathbb{P}(C_{1}(\sigma)=0)=\sum_{j=0}^{n}\frac{(-1)^{j}}{j!}. |  |

Observe that if j, m j,m vary with n n such that m ​ j ⩽ n mj\leqslant n and that either j → ∞ j\to\infty or n j − m → ∞ \frac{n}{j}-m\to\infty then

 | lim n → ∞ ℙ n ​ ( C j ​ ( σ) = m) e − 1 / j ( 1 / j) m / m! = 1. \lim_{n\to\infty}\frac{\mathbb{P}_{n}\left(C_{j}(\sigma)=m\right)}{\mathrm{e}^{-1/j}(1/j)^{m}/{m!}}=1. |  |

This establishes the Poisson distribution of C j ​ ( σ) C_{j}(\sigma) in this range.

Theorem 1.4 can be thought of as a permutation analog of Landau’s [51, p. 211] classical theorem in number theory, which states that number of integers n ⩽ x n\leqslant x having exactly k k distinct prime factors is asymptotic to

 | x log ⁡ x ​ ( log ⁡ log ⁡ x) k − 1 ( k − 1)! \frac{x}{\log x}\;\frac{(\log\log x)^{k-1}}{(k-1)!} |  |

as x → ∞ x\to\infty.

Here we derive a very general local limit law. In such generality, we only obtain an upper bound for the probability of the expected order. Lower bounds are also possible, as are asymptotic formulae, when working with small cycle lengths; see Theorem 1.19 below. The behavior of ℙ ​ ( C I ​ ( σ) = 0) \mathbb{P}(C_{I}(\sigma)=0) when I = { m + 1, …, n } I=\{m+1,\ldots,n\} is very different from the Poisson model prediction and will be dealt with separately.

###### Theorem 1.5.

Let I 1, …, I r I_{1},\ldots,I_{r} be arbitrary disjoint, nonempty subsets of [n] [n] and m 1, …, m r ⩾ 0 m_{1},\ldots,m_{r}\geqslant 0. Then

 | ℙ ⁡ ( C I 1 ​ ( σ) = m 1, …, C I r ​ ( σ) = m r) ⩽ e H n n ​ ∏ j = 1 r ( H ​ ( I j) m j m j! ​ e − H ⁡ ( I j)) ⋅ ( ε + m 1 H ⁡ ( I 1) + ⋯ + m r H ⁡ ( I r)), \mathbb{P}\big(C_{I_{1}}(\sigma)=m_{1},\ldots,C_{I_{r}}(\sigma)=m_{r}\big)\leqslant\frac{\mathrm{e}^{H_{n}}}{n}\,\prod_{j=1}^{r}\Bigg(\frac{H(I_{j})^{m_{j}}}{m_{j}!}\mathrm{e}^{-H(I_{j})}\Bigg)\cdot\left(\varepsilon+\frac{m_{1}}{H(I_{1})}+\cdots+\frac{m_{r}}{H(I_{r})}\right), |  |

where ε = 0 \varepsilon=0 if [n] = I 1 ∪ ⋯ ∪ I r [n]=I_{1}\cup\cdots\cup I_{r} and ε = 1 \varepsilon=1 otherwise.

The analog of Theorem 1.5 for prime factors of a random integer n ⩽ x n\leqslant x was proved by the author [32]. We note that H n ⩽ log ⁡ n + 1 H_{n}\leqslant\log n+1 for all n n, thus the factor e H n / n \mathrm{e}^{H_{n}}/n is bounded. Consequently, whenever r r is bounded and m j = O ⁡ ( H ⁡ ( I j)) m_{j}=O(H(I_{j})) for each j j, the right side is

 | O ⁡ ( ℙ ⁡ ( Y 1 = m 1, …, Y r = m r)), O\big(\mathbb{P}(Y_{1}=m_{1},\ldots,Y_{r}=m_{r})\big), |  |

where for each i i, Y i Y_{i} is Poisson with parameter H ⁡ ( I i) H(I_{i}), and Y 1, …, Y r Y_{1},\ldots,Y_{r} are independent. Thus, Theorem 1.5 gives an upper bound for counts of cycle lengths in sets I 1, …, I r I_{1},\ldots,I_{r} of the expected order (up to a constant factor) according to the Poisson model. As a special case of one set I 1 = I I_{1}=I, we obtain:

###### Corollary 1.6.

For any I ⊂ [n] I\subset[n] and m ⩾ 0 m\geqslant 0,

 | ℙ ⁡ ( C I ​ ( σ) = m) ⩽ e H n − H ⁡ ( I) n ⋅ H ​ ( I) m m! ​ ( 𝟙 ​ ( I ≠ [n]) + m H ⁡ ( I)). \mathbb{P}\left(C_{I}(\sigma)=m\right)\leqslant\frac{\mathrm{e}^{H_{n}-H(I)}}{n}\cdot\frac{H(I)^{m}}{m!}\Bigg(\mathbbm{1}(I\neq[n])+\frac{m}{H(I)}\Bigg). |  |

In particular,

 | ℙ ⁡ ( C I ​ ( σ) = 0) ⩽ e H n − H ⁡ ( I) n = e γ − H ⁡ ( I) ​ ( 1 + O ⁡ ( 1 / n)). \mathbb{P}(C_{I}(\sigma)=0)\leqslant\frac{\mathrm{e}^{H_{n}-H(I)}}{n}=\mathrm{e}^{\gamma-H(I)}(1+O(1/n)). |  |

The first estimate is asymptotically sharp in the case I = [n] I=[n] and m = o ⁡ ( log ⁡ n) m=o(\log n) as n → ∞ n\to\infty; see ( 3) below for a corresponding lower bound.

A slight improvement of the final estimate, namely ℙ ⁡ ( C I ​ ( σ) = 0) ⩽ e γ − H ⁡ ( I) \mathbb{P}(C_{I}(\sigma)=0)\leqslant\mathrm{e}^{\gamma-H(I)}, is given in [37] using different methods.

Theorem 1.5 becomes less accurate when m j m_{j} is much larger than H ⁡ ( I j) H(I_{j}), however it still gives roughly the right rate of decay; e.g. when I = [n] I=[n] and k = n k=n, ℙ ⁡ ( C ⁡ ( σ) = n) = 1 / n! \mathbb{P}(C(\sigma)=n)=1/n! while the right side is O ⁡ ( H n n − 1 / n!) O(H_{n}^{n-1}/n!).

Corollary 1.6 is a permutation analog of the Hardy-Ramanujan [43] inequality

 | #⁡ { n ⩽ x: n ​ has exactly ​ k ​ distinct prime factors } ⩽ C 1 ​ x log ⁡ x ​ ( log ⁡ log ⁡ x + C 2) k − 1 ( k − 1)!, \#\{n\leqslant x:n\text{ has exactly }k\text{ distinct prime factors}\}\leqslant C_{1}\frac{x}{\log x}\;\frac{(\log\log x+C_{2})^{k-1}}{(k-1)!}, |  |

where C 1, C 2 C_{1},C_{2} are certain absolute constants.

Theorem 1.5 is a useful tool for showing that cycle counts cannot vary too much from their means. Specifically, the local statistics obey the same tail bounds as the Poisson distribution, cf. Lemma 2.4.

###### Theorem 1.7.

Let I I be a nonempty subset of [n] [n]. For 0 ⩽ λ ⩽ 1 0\leqslant\lambda\leqslant 1 we have

 | ℙ ⁡ ( C I ​ ( σ) ⩽ λ ​ H ​ ( I)) ⩽ 2 ​ e 1 − Q ⁡ ( λ) ​ H ​ ( I), \mathbb{P}\big(C_{I}(\sigma)\leqslant\lambda H(I)\big)\leqslant 2\mathrm{e}^{1-Q(\lambda)H(I)}, |  |

where

 | Q ⁡ ( λ) = λ ​ log ⁡ λ − λ + 1 ⩾ 0. Q(\lambda)=\lambda\log\lambda-\lambda+1\geqslant 0. |  |

For λ ⩾ 1 \lambda\geqslant 1 we have

 | ℙ ⁡ ( C I ​ ( σ) ⩾ λ ​ H ​ ( I) + 1) ⩽ 2 ​ e 1 − Q ⁡ ( λ) ​ H ​ ( I). \mathbb{P}\big(C_{I}(\sigma)\geqslant\lambda H(I)+1\big)\leqslant 2\mathrm{e}^{1-Q(\lambda)H(I)}. |  |

Lastly, when 0 ⩽ ψ ⩽ H ⁡ ( I) 0\leqslant\psi\leqslant\sqrt{H(I)},

 | ℙ ⁡ ( | C I ​ ( σ) − H ⁡ ( I) | ⩾ ψ ​ H ⁡ ( I)) ⩽ 20 ​ e − 1 3 ​ ψ 2. \mathbb{P}\left(|C_{I}(\sigma)-H(I)|\geqslant\psi\sqrt{H(I)}\right)\leqslant 20\mathrm{e}^{-\frac{1}{3}\psi^{2}}. |  |

The function Q Q is non-negative and satisfies Q ⁡ ( x) ≈ 1 2 ​ ( x − 1) 2 Q(x)\approx\frac{1}{2}(x-1)^{2} for x x near 1 1; see also the inequality ( 11) below.

When λ \lambda is close to 1, we can be much more precise, showing a Central Limit Theorem for C I ​ ( σ) C_{I}(\sigma); see Theorem 1.21 below.

Specializing to cycle lengths in a single interval I = [a, b] ∩ ℕ I=[a,b]\cap{\mathbb{N}}, and using that H ⁡ ( I) ≈ log ⁡ ( b / a) H(I)\approx\log(b/a), we obtain the following very useful estimates.

###### Theorem 1.8.

Let a, b a,b be real numbers with 1 ⩽ a < b ⩽ n 1\leqslant a<b\leqslant n and set I = [a, b] ∩ ℕ I=[a,b]\cap{\mathbb{N}}. Uniformly for 0 ⩽ λ ⩽ 1 0\leqslant\lambda\leqslant 1, we have

 | ℙ ⁡ ( C I ​ ( σ) ⩽ λ ​ log ⁡ ( b / a)) = O ⁡ ( ( b / a) − Q ⁡ ( λ)). \mathbb{P}\left(C_{I}(\sigma)\leqslant\lambda\log(b/a)\right)=O\left((b/a)^{-Q(\lambda)}\right). |  |

Let λ 0 > 1 \lambda_{0}>1. Uniformly for 1 ⩽ λ ⩽ λ 0 1\leqslant\lambda\leqslant\lambda_{0},

 | ℙ ⁡ ( C I ​ ( σ) ⩾ λ ​ log ⁡ ( b / a)) = O λ 0 ​ ( ( b / a) − Q ⁡ ( λ)). \mathbb{P}\left(C_{I}(\sigma)\geqslant\lambda\log(b/a)\right)=O_{\lambda_{0}}\left((b/a)^{-Q(\lambda)}\right). |  |

In particular, uniformly for 0 ⩽ ψ ⩽ log ⁡ ( b / a) 0\leqslant\psi\leqslant\sqrt{\log(b/a)},

 | ℙ ⁡ ( | C I ​ ( σ) − log ⁡ ( b / a) | ⩾ ψ ​ log ⁡ ( b / a)) = O ⁡ ( e − 1 3 ​ ψ 2). \mathbb{P}\left(|C_{I}(\sigma)-\log(b/a)|\geqslant\psi\sqrt{\log(b/a)}\right)=O\big(\mathrm{e}^{-\frac{1}{3}\psi^{2}}\big). |  |

In particular, taking I = [n] I=[n], we see that C ⁡ ( σ) C(\sigma) usually does not vary more that a constant times log ⁡ n \sqrt{\log n} from its mean H n H_{n}.

Theorems 1.6 and 1.7 are not very accurate when H ⁡ ( I) < 1 H(I)<1, especially in the case m = 1 m=1. In this case, we expect that C I ​ ( σ) C_{I}(\sigma) will rarely be much more than 1. The next Theorem gives an improved upper bound in this case.

###### Theorem 1.9.

If I I is a nonempty susbet of [n] [n], and k ⩾ 0 k\geqslant 0, then

 | ℙ ⁡ ( C I ​ ( σ) ⩾ k) ⩽ H ​ ( I) k k!. \mathbb{P}\left(C_{I}(\sigma)\geqslant k\right)\leqslant\frac{H(I)^{k}}{k!}. |  |

The proof is very short and we include it here. By Theorem 1.3,

 | ℙ ⁡ ( C I ​ ( σ) ⩾ k) ⩽ 𝔼 ​ ( C I ​ ( σ) k) ⩽ H ​ ( I) k k!. \mathbb{P}(C_{I}(\sigma)\geqslant k)\leqslant{\mathbb{E}}\,\binom{C_{I}(\sigma)}{k}\leqslant\frac{H(I)^{k}}{k!}. |  |

###### Corollary 1.10.

Let 2 ⩽ ℓ ⩽ n 2\leqslant\ell\leqslant n. The probability that a random permutation σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} has two cycles of the same length j j for some j ⩾ ℓ j\geqslant\ell, is at most 1 2 ​ ( ℓ − 1) \frac{1}{2(\ell-1)}.

Again, the proof is very short: By Theorem 1.9, ℙ ⁡ ( C j ​ ( σ) ⩾ 2) ⩽ 1 2 ​ j 2 \mathbb{P}(C_{j}(\sigma)\geqslant 2)\leqslant\frac{1}{2j^{2}}. Summing over j ⩾ ℓ j\geqslant\ell we find that

 | ℙ ⁡ ( C j ​ ( σ) ⩾ 2 ​ for some ​ j ⩾ ℓ) ⩽ ∑ j = ℓ ∞ 1 2 ​ j 2 ⩽ 1 2 ​ ∑ j = ℓ ∞ 1 j ⁡ ( j − 1) = 1 2 ​ ( ℓ − 1). \mathbb{P}(C_{j}(\sigma)\geqslant 2\text{ for some }j\geqslant\ell)\leqslant\sum_{j=\ell}^{\infty}\frac{1}{2j^{2}}\leqslant\frac{1}{2}\sum_{j=\ell}^{\infty}\frac{1}{j(j-1)}=\frac{1}{2(\ell-1)}. |  |

Next, we take a first look at the *random sequence*C [m] ​ ( σ) C_{[m]}(\sigma) ( 1 ⩽ m ⩽ n) (1\leqslant m\leqslant n) for σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}. As long as m m is not too small, it is relatively easy to deduce from Theorem 1.8 that C [m] ​ ( σ) C_{[m]}(\sigma) is *uniformly*close to log ⁡ m \log m for most σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}.

###### Theorem 1.11.

Let 2 ⩽ ξ ⩽ n 2\leqslant\xi\leqslant n. With probability 1 − O ⁡ ( 1 / ( log ⁡ ξ) 1 / 3) 1-O(1/(\log\xi)^{1/3}), we have

 | | C [m] − log ⁡ m | < 2 ​ log ⁡ m ​ log ⁡ log ​ m ( ξ ⩽ m ⩽ n). |C_{[m]}-\log m|<2\sqrt{\log m\log\log m}\quad(\xi\leqslant m\leqslant n). |  |

Our proof is based on the analogous proof for the normal distribution of prime factors of integers given in [42, Ch. 1]. When m m is bounded, C [m] ​ ( σ) C_{[m]}(\sigma) has a discrete distribution which is approximately Poisson with parameter H m H_{m}. Slightly better bounds than those in Theorem 1.11 are attainable, based on ideas stemming from the Law of the Iterated Logarithm from probability theory. Essentially one can replace the factor log ⁡ log ⁡ m \log\log m with log ⁡ log ⁡ log ⁡ m \log\log\log m. See e.g., [54] for a specific statement; see also [42, Theorem 11] for the analogous statement and proof for prime factors of integers.

Theorem 1.11 also tells us about the normal behavior of D j ​ ( σ) D_{j}(\sigma), the length of the j j -th smallest cycle of σ \sigma (note that D j ​ ( σ) = D j + 1 ​ ( σ) D_{j}(\sigma)=D_{j+1}(\sigma) for some j j when σ \sigma has cycles of the same length). Since a typical permutation σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} has about log ⁡ m \log m cycles of length ⩽ m \leqslant m, we expect that D j ​ ( n) ≈ e j D_{j}(n)\approx\mathrm{e}^{j}.

###### Theorem 1.12.

Let 1 ⩽ θ ⩽ log ⁡ n 1\leqslant\theta\leqslant\log n. With probability 1 − O ( θ − 1 / 3) 1-O(\theta^{-1/3}), we have

 | | log ⁡ D j ​ ( σ) − j | < 3 ​ j ​ log ⁡ j ( θ ⩽ j ⩽ C ⁡ ( σ)). |\log D_{j}(\sigma)-j|<3\sqrt{j\log j}\qquad(\theta\leqslant j\leqslant C(\sigma)). |  |

We conclude this subsection with a sharp lower bound for ℙ ⁡ ( C ⁡ ( σ) = k) \mathbb{P}(C(\sigma)=k). This estimate is not new, but will be needed in section 5.

###### Theorem 1.13.

We have

 | ℙ ⁡ ( C ⁡ ( σ) = k) ⩾ H n k − 1 n ⁡ ( k − 1)! ​ ( 1 − k − 1 log ⁡ n) ( 1 ⩽ k < log ⁡ n). \mathbb{P}(C(\sigma)=k)\geqslant\frac{H_{n}^{k-1}}{n(k-1)!}\left(1-\frac{k-1}{\log n}\right)\qquad(1\leqslant k<\log n). |  | (3) |

For each fixed A > 1 A>1, there is a constant c ⁡ ( A) > 0 c(A)>0 such that for large enough n n (depending on A A),

 | ℙ ⁡ ( C ⁡ ( σ) = k) ⩾ c ⁡ ( A) ​ H n k − 1 ( k − 1)! ​ e − H n ( 1 ⩽ k ⩽ A ​ log ⁡ n). \mathbb{P}(C(\sigma)=k)\geqslant c(A)\frac{H_{n}^{k-1}}{(k-1)!}\mathrm{e}^{-H_{n}}\qquad(1\leqslant k\leqslant A\log n). |  |

In particular, taking Corollary 1.6 and ( 3) together establishes the asymptotic

 | ℙ ( C ( σ) = k) ∼ H n k − 1 n ⁡ ( k − 1)! ( k = o ( log n), n → ∞), \mathbb{P}(C(\sigma)=k)\sim\frac{H_{n}^{k-1}}{n(k-1)!}\qquad(k=o(\log n),n\to\infty), |  | (4) |

recovering a result of Moser and Wyman [60] (the authors utilized generating functions and contour integration). We note that ( 4) differs from the prediction of the Poisson model by a factor

 | 1 n ​ e H n ∼ e γ ( n → ∞). \frac{1}{n}\mathrm{e}^{H_{n}}\sim\mathrm{e}^{\gamma}\qquad(n\to\infty). |  |

Theorem 1.4, Theorem 1.5, Theorem 1.7, Theorem 1.8, Theorem 1.11, Theorem 1.12 and Theorem 1.13 will be proved in section 4.

### 1.4 Conditioning on the total number of cycles

If we restrict attention to permutations with k k total cycles, we may obtain analogous theorems about the distribution of C I ​ ( σ) C_{I}(\sigma). We focus on the “normal” case when k = O ⁡ ( log ⁡ n) k=O(\log n) and prove an analog of Theorem 1.7. We expect that C I ​ ( σ) C_{I}(\sigma) will have roughly a binomial distribution with parameter p = H ⁡ ( I) / H n p=H(I)/H_{n}, since if X, Y X,Y are independent Poisson random variables with parameters λ 1, λ 2 \lambda_{1},\lambda_{2}, respectively, then

 | ℙ ⁡ ( X = ℓ | X + Y = k) = ( k l) ​ ( λ 1 λ 1 + λ 2) ℓ ​ ( λ 2 λ 1 + λ 2) k − ℓ. \displaystyle\mathbb{P}(X=\ell|X+Y=k)=\binom{k}{l}\left(\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{\ell}\left(\frac{\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right)^{k-\ell}. |  |

Without loss of generality, we may assume that H ⁡ ( I) ⩽ 1 2 ​ H n H(I)\leqslant\frac{1}{2}H_{n}, else replace I I by [n] ∖ I [n]\setminus I.

###### Theorem 1.14.

Fix A > 1 A>1. Let I I be a nonempty, proper subset of [n] [n] with H ⁡ ( I) ⩽ 1 2 ​ H n H(I)\leqslant\frac{1}{2}H_{n}, suppose 2 ⩽ k ⩽ A ​ log ⁡ n 2\leqslant k\leqslant A\log n, and define let p = H ⁡ ( I) / H n ⩽ 1 2 p=H(I)/H_{n}\leqslant\frac{1}{2}. For any 0 ⩽ ψ ⩽ p ​ ( 1 − p) ​ ( k − 1) 0\leqslant\psi\leqslant\sqrt{p(1-p)(k-1)} we have

 | ℙ ⁡ ( | C I ​ ( σ) − p ⁡ ( k − 1) | ⩾ ψ ​ p ​ ( 1 − p) ​ ( k − 1) | C ⁡ ( σ) = k) = O A ​ ( e − 1 3 ​ ψ 2), \mathbb{P}\Big(|C_{I}(\sigma)-p(k-1)|\geqslant\psi\sqrt{p(1-p)(k-1)}\;\Big|\;C(\sigma)=k\Big)=O_{A}\left(\mathrm{e}^{-\frac{1}{3}\psi^{2}}\right), |  |

the implied constant depending only on A A.

Theorem 1.14 will be proved in section 5. We also mention here work of Mező and Wang [58], who found an asymptotic for the number of permutations with exactly k k cycles and all cycles having length > m >m, for fixed k k and m m with n → ∞ n\to\infty.

### 1.5 Permutations without small cycles.

Sharp bounds on ℙ ​ ( C [m] ​ ( σ) = 0) \mathbb{P}(C_{[m]}(\sigma)=0) are a key to establishing the Poisson model. The model predicts that ℙ ​ ( C [m] ​ ( σ) = 0) \mathbb{P}(C_{[m]}(\sigma)=0) should be about e − H m \mathrm{e}^{-H_{m}}, and Corollary 1.6 contains an upper bound close to this. This cannot be expected to hold for large m m, for example ℙ ⁡ ( C [m] ​ ( σ) = 0) = 1 / n \mathbb{P}(C_{[m]}(\sigma)=0)=1/n if m ⩾ n / 2 m\geqslant n/2 since a permutation lacking cycles of length at most m m must be a single n n -cycle. In fact, when n / m n/m is small, there is an asymptotic formula ℙ ⁡ ( C [m] ​ ( σ) = 0) ∼ ω ⁡ ( n / m) / m \mathbb{P}(C_{[m]}(\sigma)=0)\sim\omega(n/m)/m ( n → ∞ n\to\infty, m → ∞ m\to\infty) where ω \omega is Buchstab’s function and ω ⁡ ( u) → e − γ \omega(u)\to\mathrm{e}^{-\gamma} as u → ∞ u\to\infty [40, Theorem 5]. This is analogous to the problem of counting integers n ⩽ x n\leqslant x with no prime factor ⩽ x 1 / u \leqslant x^{1/u} (see [70, Ch. III.6]).

Our focus is to prove that ℙ ​ ( C [m] ​ ( σ) = 0) \mathbb{P}(C_{[m]}(\sigma)=0) is very close to e − H m \mathrm{e}^{-H_{m}} when n / m n/m is large.

###### Theorem 1.15.

Let 1 ⩽ m ⩽ n 1\leqslant m\leqslant n. Then

 | ℙ ⁡ ( C [m] ​ ( σ) = 0) = e − H m ​ ( 1 + O ⁡ ( e − g ⁡ ( n / m))), \mathbb{P}(C_{[m]}(\sigma)=0)=\mathrm{e}^{-H_{m}}\left(1+O(\mathrm{e}^{-g(n/m)})\right), |  |

where g ⁡ ( x) = 0 g(x)=0 for 1 ⩽ x ⩽ 20 1\leqslant x\leqslant 20 and for x > 20 x>20,

 | g ⁡ ( x) = x ​ log ⁡ x − x ​ log ⁡ log ​ log ⁡ x + O ⁡ ( x). g(x)=x\log x-x\log\log\log x+O(x). |  |

Theorem 1.15 will be proved in section 6.

Historically, the relation lim n → ∞ ℙ ⁡ ( C [m] ​ ( σ) = 0) → e − H m \lim_{n\to\infty}\mathbb{P}(C_{[m]}(\sigma)=0)\to\mathrm{e}^{-H_{m}}, for m m fixed, is due to Gruder [41]. Exact asymptotics for ℙ ⁡ ( C [m] ​ ( σ) = 0) − e − H m \mathbb{P}(C_{[m]}(\sigma)=0)-\mathrm{e}^{-H_{m}} have been obtained by Petuchovas [65, 66], using generating functions ( 1) and a lengthy argument based on contour integration. Our method is much simpler and is based on sieve methods in number theory.

### 1.6 Permutations without large cycles

The distribution of permutations without large cycles is very different from that predicted by the Poisson model. If σ \sigma has no large cycles, the fact that the cycle lengths must sum to n n implies that σ \sigma must contain a very large number of smaller cycles, and this is a much rarer event. We define

 | ν ⁡ ( n, m) = ℙ ⁡ ( C { m + 1, …, n } ​ ( σ) = 0). \nu(n,m)=\mathbb{P}(C_{\{m+1,\ldots,n\}}(\sigma)=0). |  |

###### Theorem 1.16.

For 1 ⩽ m ⩽ n 1\leqslant m\leqslant n we have

 | ν ⁡ ( n, m) ⩽ e − u ​ log ⁡ u + u − 1, u = n / m. \nu(n,m)\leqslant\mathrm{e}^{-u\log u+u-1},\qquad u=n/m. |  |

This bound is reasonably sharp throughout the range 1 ⩽ m ⩽ n 1\leqslant m\leqslant n. For example, when m = 1 m=1, Stirling’s formula implies

 | ν ⁡ ( 1, m) = 1 n! ∼ e − n ​ log ⁡ n + n 2 ​ π ​ n ( n → ∞). \nu(1,m)=\frac{1}{n!}\sim\frac{\mathrm{e}^{-n\log n+n}}{\sqrt{2\pi n}}\qquad(n\to\infty). |  |

When m = 2 m=2, Chowla, Herstein and Moore [13] showed an asymptotic for ν ⁡ ( 2, m) \nu(2,m) which implies that

 | ν ⁡ ( 2, m) = e − ( n / 2) ​ log ⁡ ( n / 2) + O ⁡ ( n). \nu(2,m)=\mathrm{e}^{-(n/2)\log(n/2)+O(n)}. |  |

At the opposite extreme, when n / m = u n/m=u is bounded, then ν ⁡ ( n, m) ∼ ρ ⁡ ( u) \nu(n,m)\sim\rho(u) as n → ∞ n\to\infty by Goncharov [39], where ρ \rho is the Dickman function [15], the unique continuous solution of the differential-delay equation

 | ρ ( u) = 1 ( 0 ⩽ u ⩽ 1); u ρ ′ ( u) = − ρ ( u − 1) ( u > 1). \rho(u)=1\;\;\;(0\leqslant u\leqslant 1);\qquad u\rho^{\prime}(u)=-\rho(u-1)\quad(u>1). |  | (5) |

de Bruijn [11] found a precise asymptotic for ρ ⁡ ( u) \rho(u) as u → ∞ u\to\infty. In particular

 | ρ ⁡ ( u) = e − u ​ log ⁡ u − u ​ log ⁡ log ⁡ ( 3 ​ u) + O ⁡ ( u). \rho(u)=\mathrm{e}^{-u\log u-u\log\log(3u)+O(u)}. |  |

See also [70], Ch. III.5.4.

Using complex analytic methods starting from ( 1), Manstavičius and Petuchovas [55] found more precise asymptotics for ν ⁡ ( n, m) \nu(n,m) throughout the range 1 ⩽ m ⩽ n 1\leqslant m\leqslant n. Their methods are motivated by the analogous problem of counting integers lacking large prime factors, see [70, Ch. III.5]. Our next result, which has a very short proof, provides an asymptotic in large range of n, m n,m.

###### Theorem 1.17.

For all n ⩾ m ⩾ 1 n\geqslant m\geqslant 1 we have

 | ρ ⁡ ( n m) ⩽ ν ⁡ ( n, m) ⩽ ρ ⁡ ( n + 1 m + 1). \rho\left(\frac{n}{m}\right)\leqslant\nu(n,m)\leqslant\rho\left(\frac{n+1}{m+1}\right). |  | (6) |

Theorems 1.16 and 1.17 will be proved in section 7.

We have

 | ρ ( u − v) = ρ ( u) e O ⁡ ( v ​ log ⁡ u) ( u ⩾ 2, 0 ⩽ v ⩽ 1). \rho(u-v)=\rho(u)\mathrm{e}^{O(v\log u)}\qquad(u\geqslant 2,0\leqslant v\leqslant 1). |  | (7) |

This follows from strong asymptotics for ρ ⁡ ( u) \rho(u), e.g. [70, Theorem III.5.13]. We give a short, direct deduction of ( 7) in the Appendix. Since n m − n + 1 m + 1 ⩽ n m 2 \frac{n}{m}-\frac{n+1}{m+1}\leqslant\frac{n}{m^{2}} we deduce the following.

###### Corollary 1.18.

We have

 | ν ( n, m) ∼ ρ ( n / m) ( m ⩽ n = o ( m 2 / log m), m → ∞). \nu(n,m)\sim\rho(n/m)\qquad(m\leqslant n=o(m^{2}/\log m),m\to\infty). |  |

Corollary 1.18 recovers Theorem 4 of [55]. When n ≫ m 2 / log ⁡ m n\gg m^{2}/\log m, ν ⁡ ( n, m) ≁ ρ ⁡ ( n / m) \nu(n,m)\not\sim\rho(n/m), the asymptotic having a different shape; see [65, Theorem 2.4]. Thus, the range of n n in Theorem 1.18 is best possible.

When n / 2 ⩽ m ⩽ n n/2\leqslant m\leqslant n, σ \sigma has at most one cycle of length k ∈ ( m, n] k\in(m,n], thus

 | ν ⁡ ( n, m) = 1 − ∑ m < k ⩽ n 𝔼 ​ C k ​ ( σ) = 1 − ( H n − H m). \nu(n,m)=1-\sum_{m<k\leqslant n}{\mathbb{E}}\,C_{k}(\sigma)=1-(H_{n}-H_{m}). |  | (8) |

In particular, when m = 50, n = 100 m=50,n=100, this helps to solve the “100 prisoners problem” [35]: There are 100 prisoners, numbered to 100. The numbers from 1 to 100 are placed in 100 unmarked boxes. Each prisoner is allowed to open 50 of the boxes, and no communication between prisoners is allowed. If every prisoner finds his own number then they all go free. Although it appears hopeless, there is a strategy that will work about 31% of the time. If the boxes are labeled 1,…,100 on the outside, the mapping from external label to internal number is a permutation of [100] [100]. With probability 1 − H 100 + H 50 ≈ 0.31 1-H_{100}+H_{50}\approx 0.31, the permutation contains no cycles of length more than 50. In this case, if every prisoner follows the cycle starting with his own number (first opens the box labeled on the outside with his number, then opens the box number that he finds in the first box, etc), he’ll find his number inside one of the boxes after no more than 50 openings.

The limiting relation lim n → ∞ ν ⁡ ( n, ⌊ n / u ⌋) = ρ ⁡ ( u) \lim_{n\to\infty}\nu(n,{\left\lfloor{n/u}\right\rfloor})=\rho(u) was first proved by Knuth and Trabb Pardo [46], 46 years after Dickman [15] showed the analogous statement for prime factors. The joint distribution of the lengths of the r r largest cycles of σ \sigma, with r ⩾ 1 r\geqslant 1 fixed, has also received considerable attention (see, e.g., [3, 52, 71]), but we will not discuss it here. We also mention the survey paper [49, Section 3.10,3.11], which has more extensive historical information about work on the distribution of the smallest and largest cycles.

### 1.7 Poisson approximation of small cycle lengths

Let 1 ⩽ k ⩽ n 1\leqslant k\leqslant n and consider the problem of modeling

 | 𝒞 k = ( C 1 ​ ( σ), …, C k ​ ( σ)) \mathcal{C}_{k}=(C_{1}(\sigma),\ldots,C_{k}(\sigma)) |  |

by the random vector

 | 𝒵 k = ( Z 1, …, Z k), \mathcal{Z}_{k}=(Z_{1},\ldots,Z_{k}), |  |

where Z 1, …, Z k Z_{1},\ldots,Z_{k} are independent Poisson random variables with parameters 1, 1 2, …, 1 k 1,\frac{1}{2},\ldots,\frac{1}{k}, respectively. We especially desire a good approximation when k k is large, as opposed to bounded (ref. Theorem 1.5). We express our results in terms of the Total Variational Distance d T ​ V ​ ( X, Y) d_{TV}(X,Y) between two random variables X X and Y Y taking values in a discrete space Ω \Omega, defined by

 | d T ​ V ​ ( X, Y):= sup U ⊂ Ω ℙ ⁡ ( X ∈ U) − ℙ ⁡ ( Y ∈ U). d_{TV}(X,Y):=\sup_{U\subset\Omega}\mathbb{P}(X\in U)-\mathbb{P}(Y\in U). |  | (9) |

###### Theorem 1.19.

Let 1 ⩽ k ⩽ n 1\leqslant k\leqslant n. Then

 | d T ​ V ​ ( 𝒞 k, 𝒵 k) ⩽ e − f ⁡ ( n / k), d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k})\leqslant\mathrm{e}^{-f(n/k)}, |  |

where f ⁡ ( x) = 0 f(x)=0 for x ⩽ 20 x\leqslant 20 and for x ⩾ 20 x\geqslant 20 we have

 | f ⁡ ( x) = x ​ log ⁡ x − x ​ log ⁡ log ​ log ⁡ x + O ⁡ ( x). f(x)=x\log x-x\log\log\log x+O(x). |  |

Theorem 1.19 will be proved in section 8.

Theorem 1.19 is slightly weaker than the main theorem of Arratia and Tavaré [5], which states that d T ​ V ​ ( 𝒞 k, 𝒵 k) ⩽ e − ( n / k) ​ log ⁡ ( n / k) + O ⁡ ( n / k) d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k})\leqslant\mathrm{e}^{-(n/k)\log(n/k)+O(n/k)}. Sharper bounds are known, and are expressed in terms of the Dickman and Buchstab functions (see [55, 65]). Our proof is significantly shorter than either of these treatments.

We immediately obtain the following corollary, by grouping together integers into sets.

###### Theorem 1.20.

Let I 1, …, I m I_{1},\ldots,I_{m} be disjoint subsets of [k] [k], with k ⩽ n k\leqslant n. Then, for any set 𝒥 ⊆ ℕ 0 m \mathcal{J}\subseteq{\mathbb{N}}_{0}^{m},

 | ℙ ⁡ ( ( C I 1 ​ ( σ), …, C I m ​ ( σ)) ∈ 𝒥) = ℙ ⁡ ( ( Y 1, …, Y m) ∈ 𝒥) + O ⁡ ( e − f ⁡ ( n / k)), \mathbb{P}\Big((C_{I_{1}}(\sigma),\ldots,C_{I_{m}}(\sigma))\in\mathcal{J}\Big)=\mathbb{P}\Big((Y_{1},\ldots,Y_{m})\in\mathcal{J}\Big)+O(\mathrm{e}^{-f(n/k)}), |  |

where for each i i, Y i Y_{i} is Poisson with parameter H ⁡ ( I i) H(I_{i}), and Y 1, …, Y m Y_{1},\ldots,Y_{m} are independent.

### 1.8 Central Limit Theorems

Combining Theorem 1.20 with the Central Limit Theorem for Poisson variables (Theorem 9.1 below) establishes a Central Limit Theorem for the count of cycles whose lengths lie in an arbitrary set I ⊂ [n] I\subset[n].

###### Theorem 1.21.

Let I ⊂ [n] I\subset[n] with H ⁡ ( I) ⩾ 3 H(I)\geqslant 3. Uniformly for all I I and any real w w,

 | ℙ ⁡ ( C I ​ ( σ) ⩽ H ⁡ ( I) + w ​ H ⁡ ( I)) = Φ ⁡ ( w) + O ⁡ ( log ⁡ H ⁡ ( I) H ⁡ ( I)), Φ ⁡ ( w) = 1 2 ​ π ​ ∫ − ∞ w e − 1 2 ​ t 2 ​ 𝑑 t. \mathbb{P}\left(C_{I}(\sigma)\leqslant H(I)+w\sqrt{H(I)}\right)=\Phi(w)+O\left(\frac{\log H(I)}{\sqrt{H(I)}}\right),\quad\;\;\Phi(w)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{w}\mathrm{e}^{-\frac{1}{2}t^{2}}\,dt. |  |

The special case I = [n] I=[n] was established by Goncharov [39], without a specific rate of convergence. Goncharov analyzed carefully the asymptotics of the Stirling number of the first kind, s ⁡ ( n, m) s(n,m), the absolute value of which counts the number of permutations σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} with C ⁡ ( σ) = m C(\sigma)=m. Since H n = log ⁡ n + O ⁡ ( 1) H_{n}=\log n+O(1) and Φ \Phi has bounded derivative, we quickly arrive at the following.

###### Theorem 1.22.

Let n ⩾ 100 n\geqslant 100 and w w be real. Then

 | P ⁡ ( C ⁡ ( σ) ⩽ log ⁡ n + w ​ log ⁡ n) = Φ ⁡ ( w) + O ⁡ ( log ⁡ log ⁡ n log ⁡ n). P\left(C(\sigma)\leqslant\log n+w\sqrt{\log n}\right)=\Phi(w)+O\left(\frac{\log\log n}{\sqrt{\log n}}\right). |  |

The big- O O term in Theorem 1.21 cannot be made smaller than 1 / H ⁡ ( I) 1/\sqrt{H(I)} since C I ​ ( σ) C_{I}(\sigma) is integer valued, and thus the left side is constant in intervals of w w of length 1 / H ⁡ ( I) 1/\sqrt{H(I)}, while Φ ′ ​ ( w) ≫ 1 \Phi^{\prime}(w)\gg 1 if w w is bounded. We remark that when H ⁡ ( I) H(I) is bounded, C I ​ ( σ) C_{I}(\sigma) is expected to have Poisson distribution with small parameter, and this cannot be approximated by a Gaussian.

We also derive that the j j -th smallest cycle of σ \sigma, denoted D j ​ ( σ) D_{j}(\sigma) (with ties allowed), also obeys the Gaussian law, refining Theorem 1.12.

###### Theorem 1.23.

Uniformly for j j in the range

 | 1 ⩽ j ⩽ log ⁡ n − ( log ⁡ n) ​ log ⁡ log ​ n 1\leqslant j\leqslant\log n-\sqrt{(\log n)\log\log n} |  |

and for any real w w,

 | ℙ ⁡ ( log ⁡ D j ​ ( σ) ⩽ j + w ​ j) = Φ ⁡ ( w) + O ⁡ ( log ⁡ ( 2 ​ j) j). \mathbb{P}\Big(\log D_{j}(\sigma)\leqslant j+w\sqrt{j}\Big)=\Phi(w)+O\left(\frac{\log(2j)}{\sqrt{j}}\right). |  |

The analogous statement for the j j -th smallest prime factor of an integer, without a rate of convergence, was proved by Galambos [36].

Theorems 1.21 and 1.23 will be proved in section 9.

### 1.9 Fixed sets and divisors of permutations

A *fixed set*of a permutation σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} is a subset of [n] [n] fixed by σ \sigma. A fixed set corresponds to a product of some subset of the cycles in σ \sigma (we include both the empty set and the whole set [n] [n] as fixed sets). These play the same role for permutations as divisors do for integers. The existence of fixed sets of a particular size has applications to various questions in combinatorial group theory, such as generation of 𝒮 n \mathcal{S}_{n} by random permutations and the distribution of transitive subgroups of 𝒮 n \mathcal{S}_{n}. See e.g. [12, 14, 16, 17, 18, 19, 33, 53, 67, 73].

We begin with a simple result about 2 C ⁡ ( σ) 2^{C(\sigma)}, which counts the number of fixed sets of σ \sigma, equivalently, the number of divisors of σ \sigma.

###### Theorem 1.24.

𝔼 ​ 2 C ⁡ ( σ) = n + 1 {\mathbb{E}}\,2^{C(\sigma)}=n+1.

By contrast, we know that C ⁡ ( σ) ∼ log ⁡ n C(\sigma)\sim\log n for most σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} (for example, from Theorem 1.22), and therefore for most σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n}, 2 C ⁡ ( σ) ≈ 2 log ⁡ n = n log ⁡ 2 2^{C(\sigma)}\approx 2^{\log n}=n^{\log 2}, much smaller than n n.

A basic problem is to estimate i ⁡ ( n, k) i(n,k), the probability that σ ∈ 𝒮 n \sigma\in\mathcal{S}_{n} fixes some set of size k k. Equivalently, what is the probability that the cycle decomposition of σ \sigma contains disjoint cycles with lengths summing to k k? Evidently, i ⁡ ( n, k) = i ⁡ ( n, n − k) i(n,k)=i(n,n-k), thus it suffices to bound i ⁡ ( n, k) i(n,k) for k ⩽ n / 2 k\leqslant n/2. Sharpening earlier bounds due to Diaconis, Fulman and Guralnick [14], Łuczak and Pyber [53] and by Pemantle, Peres, and Rivin [67, Theorem 1.7], the author with Eberhard and Green [17] proved that

 | 1 k ℰ ​ ( 1 + log ⁡ k) 3 / 2 ≪ i ⁡ ( n, k) ≪ 1 k ℰ ​ ( 1 + log ⁡ k) 3 / 2, ℰ = 1 − 1 + log ⁡ log ⁡ 2 log ⁡ 2 = 0.08607 ​ …, \frac{1}{k^{\mathcal{E}}(1+\log k)^{3/2}}\ll i(n,k)\ll\frac{1}{k^{\mathcal{E}}(1+\log k)^{3/2}},\quad\mathcal{E}=1-\frac{1+\log\log 2}{\log 2}=0.08607\ldots, |  | (10) |

uniformly for 1 ⩽ k ⩽ n / 2. 1\leqslant k\leqslant n/2. A full asymptotic is not known.

This is the permutation analog of counting integers with a divisor in a given interval, see e.g. [30, 31], and is related to the Erdős multiplication table problem ( [20, 21]), that of estimating the number, A ⁡ ( N) A(N), of *distinct*products of the form a ​ b ab with a ⩽ N a\leqslant N, b ⩽ N b\leqslant N. The full proof of ( 10) is rather complicated. However, using the tools we have developed in this paper, we can quickly obtain an upper bound which is close to optimal.

###### Theorem 1.25.

Uniformly for 1 ⩽ k ⩽ n / 2 1\leqslant k\leqslant n/2 we have

 | i ⁡ ( n, k) ≪ 1 k ℰ. i(n,k)\ll\frac{1}{k^{\mathcal{E}}}. |  |

## 2 Preliminaries

The following standard bounds are stated without proof.

###### Lemma 2.1.

The harmonic sums H n H_{n} satisfy

(i) log ⁡ n ⩽ H n ⩽ 1 + log ⁡ n \log n\leqslant H_{n}\leqslant 1+\log n;

(ii) H n = log ⁡ n + γ + O ⁡ ( 1 / n) H_{n}=\log n+\gamma+O(1/n), where γ = 0.57721566 ​ … \gamma=0.57721566\ldots is Euler’s constant.

###### Lemma 2.2 (Stirling’s formula).

We have n! ⩾ ( n / e) n n!\geqslant(n/\mathrm{e})^{n} and the asymptotic

 | n! = 2 ​ π ​ n ​ ( n / e) n ​ ( 1 + O ⁡ ( 1 / n)) ( n ⩾ 1). n!=\sqrt{2\pi n}(n/\mathrm{e})^{n}(1+O(1/n))\qquad(n\geqslant 1). |  |

###### Lemma 2.3 (Inclusion-exclusion).

Let a a be a non-negative integer. For 0 ⩽ m ⩽ k 0\leqslant m\leqslant k,

 | 𝟙 ​ ( a = m) \displaystyle\mathbbm{1}(a=m) | = ∑ r = m ∞ ( − 1) r − m ​ ( r m) ​ ( a r) \displaystyle=\sum_{r=m}^{\infty}(-1)^{r-m}\binom{r}{m}\binom{a}{r} |  |

 |  | = ∑ r = m k ( − 1) r − m ​ ( r m) ​ ( a r) + ( − 1) k + 1 − m ​ ( a m) ​ ( a − m − 1 k − m), \displaystyle=\sum_{r=m}^{k}(-1)^{r-m}\binom{r}{m}\binom{a}{r}+(-1)^{k+1-m}\binom{a}{m}\binom{a-m-1}{k-m}, |  |

where the final term is at most ( a k + 1) ​ ( k + 1 m) \binom{a}{k+1}\binom{k+1}{m} in absolute value.

The final claim comes from the inequality ( a − m − 1 k − m) ⩽ ( a − m k − m + 1) \binom{a-m-1}{k-m}\leqslant\binom{a-m}{k-m+1}.

###### Lemma 2.4 (Poisson tails; see Norton [64, Section 4]).

Let X X be Poisson with parameter λ \lambda. Then

 | ℙ ⁡ ( X ⩽ α ​ λ) \displaystyle\mathbb{P}(X\leqslant\alpha\lambda) | ⩽ min ( 1, 1 ( 1 − α) ​ α ​ λ) e − Q ⁡ ( α) ​ λ ( 0 ⩽ α ⩽ 1), \displaystyle\leqslant\min\bigg(1,\frac{1}{(1-\alpha)\sqrt{\alpha\lambda}}\bigg)\mathrm{e}^{-Q(\alpha)\lambda}\quad(0\leqslant\alpha\leqslant 1), |  |

 | ℙ ⁡ ( X ⩾ α ​ λ) \displaystyle\mathbb{P}(X\geqslant\alpha\lambda) | ⩽ min ( 1, 1 α − 1 α 2 ​ π ​ λ) e − Q ⁡ ( α) ​ λ ( α ⩾ 1), \displaystyle\leqslant\min\bigg(1,\frac{1}{\alpha-1}\sqrt{\frac{\alpha}{2\pi\lambda}}\bigg)\mathrm{e}^{-Q(\alpha)\lambda}\quad(\alpha\geqslant 1), |  |

where Q ⁡ ( x) = ∫ 1 x log ⁡ t ​ 𝑑 t = x ​ log ​ x − x + 1. Q(x)=\int_{1}^{x}\log t\,dt=x\log x-x+1. Furthermore,

 | x 2 3 ⩽ Q ⁡ ( 1 + x) ⩽ x 2 ( | x | ⩽ 1) \frac{x^{2}}{3}\leqslant Q(1+x)\leqslant x^{2}\quad(|x|\leqslant 1) |  | (11) |

and, when 0 < x 1 ⩽ x 2 ⩽ 1 0<x_{1}\leqslant x_{2}\leqslant 1 we have

 | Q ⁡ ( x 1) − Q ⁡ ( x 2) ⩽ ( − log ⁡ x 1) ​ ( x 2 − x 1). Q(x_{1})-Q(x_{2})\leqslant(-\log x_{1})(x_{2}-x_{1}). |  | (12) |

## 3 Binomial moments

We begin by proving a special case of Theorem 1.3, where each set I j I_{j} is a singleton. This is Theorem 7 in [72].

###### Lemma 3.1.

Let m 1, …, m n m_{1},\ldots,m_{n} be non-negative integers with m 1 + 2 ​ m 2 + ⋯ + n ​ m n ⩽ n m_{1}+2m_{2}+\cdots+nm_{n}\leqslant n. Then

 | 𝔼 ​ ∏ j = 1 n ( C j ​ ( σ) m j) = ∏ j = 1 n ( 1 / j) m j m j!. {\mathbb{E}}\,\prod_{j=1}^{n}\binom{C_{j}(\sigma)}{m_{j}}=\prod_{j=1}^{n}\frac{(1/j)^{m_{j}}}{m_{j}!}. |  |

If m 1 + 2 ​ m 2 + ⋯ + n ​ m n > n m_{1}+2m_{2}+\cdots+nm_{n}>n, then the left side is zero.

###### Proof.

The second assertion is obvious, since the only way for the product on the left to be positive is for the sum of the cycle lengths to exceed n n. Now assume that m 1 + 2 ​ m 2 + ⋯ + n ​ m n ⩽ n m_{1}+2m_{2}+\cdots+nm_{n}\leqslant n. The number of ways of choosing from [n] [n] a disjoint collection of m 1 m_{1} 1 − 1- element sets, m 2 m_{2} 2 − 2- element sets, … \ldots, m n m_{n} n − n- element sets is equal to

 | ( n 1 ⋯ 1 ⏟ m 1 2 ⋯ 2 ⏟ m 2 ⋯ n ⋯ n ⏟ m n t) ​ 1 m 1! ⋯ m n! = n! / t! ∏ j = 1 n ( j!) m j ​ m j!, \binom{n}{\underbrace{1\cdots 1}_{m_{1}}\underbrace{2\cdots 2}_{m_{2}}\cdots\underbrace{n\cdots n}_{m_{n}}\,t}\frac{1}{m_{1}!\cdots m_{n}!}=\frac{n!/t!}{\prod_{j=1}^{n}(j!)^{m_{j}}m_{j}!}, |  |

where t = n − ( m 1 + 2 ​ m 2 + ⋯ + n ​ m n) t=n-(m_{1}+2m_{2}+\cdots+nm_{n}). A k k -element set may be arranged into a cycle in ( k − 1)! (k-1)! ways. Thus, the number of ways to arrange the elements of these sets into cycles is ( 0!) m 1 ( 1!) m 2 ⋯ ( n − 1)! m k (0!)^{m_{1}}(1!)^{m_{2}}\cdots(n-1)!^{m_{k}}. Finally, the t t elements not used in any of these cycles may be permuted in t! t! ways. ∎

This special case suffices to prove Theorems 1.1 and 1.2.

###### Proof of Theorem 1.2 (Cauchy’s Theorem).

Apply Lemma 3.1, noting that ( C j ​ ( σ) m j) ≠ 0 \binom{C_{j}(\sigma)}{m_{j}}\neq 0 for all j j if and only if C j ​ ( σ) = m j C_{j}(\sigma)=m_{j} for every j j. ∎

###### Proof of Theorem 1.1.

Using Cauchy’s formula, we have

 | ∑ n, k ℙ n ​ ( C I ​ ( σ) = k, C [n] ∖ I ​ ( σ) = 0) ​ x n ​ y k \displaystyle\sum_{n,k}\mathbb{P}_{n}\big(C_{I}(\sigma)=k,C_{[n]\setminus I}(\sigma)=0\big)x^{n}y^{k} | = ∑ n, k x n ​ y k ​ ∑ ∑ i ∈ I a i = k ∑ i ∈ I i ​ a i = n ∏ i ∈ I ( 1 / i) a i a i! \displaystyle=\sum_{n,k}x^{n}y^{k}\sum_{\begin{subarray}{c}\sum_{i\in I}a_{i}=k\\ \sum_{i\in I}ia_{i}=n\end{subarray}}\prod_{i\in I}\frac{(1/i)^{a_{i}}}{a_{i}!} |  |

 |  | = ∑ a i ⩾ 0: i ∈ I x ∑ i ​ a i ​ y ∑ a i ​ ( 1 / i) a i ∏ a i! \displaystyle=\sum_{a_{i}\geqslant 0:i\in I}\frac{x^{\sum ia_{i}}y^{\sum a_{i}}(1/i)^{a_{i}}}{\prod a_{i}!} |  |

 |  | = exp ⁡ { y ​ ∑ i ∈ I x i i }. ∎ \displaystyle=\exp\bigg\{y\sum_{i\in I}\frac{x^{i}}{i}\bigg\}.\qed |  |

###### Proof of Theorem 1.3.

Consider a set A A of size C I j ​ ( σ) C_{I_{j}}(\sigma), and partition A A into subsets A r A_{r}, where | A r | = C r ​ ( σ) |A_{r}|=C_{r}(\sigma) for r ∈ I j r\in I_{j}. Then

 | ∏ j = 1 k ( C I j ​ ( σ) m j) = ∑ ( 13) ∏ j = 1 k ∏ r ∈ I j ( C r ​ ( σ) m j, r), \prod_{j=1}^{k}\binom{C_{I_{j}}(\sigma)}{m_{j}}=\sum_{\eqref{cycles-sets-2}}\;\prod_{j=1}^{k}\prod_{r\in I_{j}}\binom{C_{r}(\sigma)}{m_{j,r}}, |  |

where the summation is over tuples ( m j, r) 1 ⩽ j ⩽ k, r ∈ I j (m_{j,r})_{1\leqslant j\leqslant k,r\in I_{j}} satisfying the system

 | ∑ r ∈ I j m j, r = m j ( 1 ⩽ j ⩽ k). \sum_{r\in I_{j}}m_{j,r}=m_{j}\quad(1\leqslant j\leqslant k). |  | (13) |

Thus,

 | 𝔼 ​ ∏ j = 1 k ( C I j ​ ( σ) m j) = ∑ ( 13) 𝔼 ​ ∏ j = 1 k ∏ r ∈ I j ( C r ​ ( σ) m j, r). {\mathbb{E}}\,\prod_{j=1}^{k}\binom{C_{I_{j}}(\sigma)}{m_{j}}=\sum_{\eqref{cycles-sets-2}}{\mathbb{E}}\,\prod_{j=1}^{k}\prod_{r\in I_{j}}\binom{C_{r}(\sigma)}{m_{j,r}}. |  | (14) |

Using Lemma 3.1, the expectation on the right side of ( 14) equals

 | ∏ j = 1 k ∏ r ∈ I j ( 1 / r) m r, j m r, j! \prod_{j=1}^{k}\prod_{r\in I_{j}}\frac{(1/r)^{m_{r,j}}}{m_{r,j}!} |  |

provided that

 | ∑ j = 1 k ∑ r ∈ I j r ​ m r, j ⩽ n, \sum_{j=1}^{k}\sum_{r\in I_{j}}rm_{r,j}\leqslant n, |  | (15) |

and is zero otherwise.

If ∑ j = 1 k m j ​ max ⁡ ( I j) ⩽ n \sum_{j=1}^{k}m_{j}\max(I_{j})\leqslant n, then ( 15) will always be satisfied as long as ( 13) holds, and therefore

 | 𝔼 ​ ∏ j = 1 k ( C I j ​ ( σ) m j) = ∏ j = 1 k ∑ ( 13) ∏ r ∈ I j ( 1 / r) m r, j m r, j! = ∏ j = 1 k H ​ ( I j) m j m j!, {\mathbb{E}}\,\prod_{j=1}^{k}\binom{C_{I_{j}}(\sigma)}{m_{j}}=\prod_{j=1}^{k}\sum_{\eqref{cycles-sets-2}}\prod_{r\in I_{j}}\frac{(1/r)^{m_{r,j}}}{m_{r,j}!}=\prod_{j=1}^{k}\frac{H(I_{j})^{m_{j}}}{m_{j}!}, |  |

as claimed. On the other hand, if ∑ j = 1 k m j ​ max ⁡ ( I j) > n \sum_{j=1}^{k}m_{j}\max(I_{j})>n, then there is some choice of the parameters ( m j, r) (m_{j,r}) satisfying ( 13) but violating ( 15), and the left side is strictly less than the right side. Specifically, we may take m j, max ⁡ I j = m j m_{j,\max I_{j}}=m_{j} for each j j and m j, r = 0 m_{j,r}=0 otherwise. ∎

## 4 Local limit theorems

###### Proof of Goncharov’s local limit theorem, Theorem 1.4.

By Lemma 2.3 and Lemma 3.1, we obtain

 | ℙ ​ ( C j ​ ( σ) = m) \displaystyle\mathbb{P}\big(C_{j}(\sigma)=m\big) | = 𝔼 ​ ∑ r = m ∞ ( − 1) r − m ​ ( r m) ​ ( C j ​ ( σ) r) = ( − 1) m ​ ∑ r = m ⌊ n / j ⌋ ( r m) ​ ( − 1 / j) r r!. \displaystyle={\mathbb{E}}\,\sum_{r=m}^{\infty}(-1)^{r-m}\binom{r}{m}\binom{C_{j}(\sigma)}{r}=(-1)^{m}\sum_{r=m}^{{\left\lfloor{n/j}\right\rfloor}}\binom{r}{m}\frac{(-1/j)^{r}}{r!}. |  |

The desired equality follows by setting r = h + m r=h+m. ∎

While Theorem 1.4 provides a exact formula for the local statistic ℙ ​ ( C j ​ ( σ) = m) \mathbb{P}(C_{j}(\sigma)=m), an analogous formula for ℙ ​ ( C I ​ ( σ) = m) \mathbb{P}(C_{I}(\sigma)=m) with an arbitrary set I I will necessarily be far more complicated. However, borrowing ideas from the theory of averages of multiplicative functions in number theory, we give a relatively sharp upper bound for this quantity, and more generally for the joint probability of C I j ​ ( σ) = m j C_{I_{j}}(\sigma)=m_{j} for j = 1, …, k j=1,\ldots,k.

We begin with a rather complicated identity for the joint distribution of the quantities C I i C_{I_{i}}.

###### Lemma 4.1.

Let I 1, …, I r I_{1},\ldots,I_{r} be disjoint subsets of [n] [n] and m 1, …, m r m_{1},\ldots,m_{r} be non-negative integers. Denote I 0 = [n] ∖ ( I 1 ∪ ⋯ ∪ I r) I_{0}=[n]\setminus(I_{1}\cup\cdots\cup I_{r}). Let 𝒯 \mathcal{T} be the set of indices i i with m i > 0 m_{i}>0, together with the number 0 if I 0 I_{0} is nonempty. Then

 | ℙ ⁡ ( C I j ​ ( σ) = m j ​ ( 1 ⩽ j ⩽ r)) = 1 n ​ ∑ t ∈ 𝒯 ∑ h ∈ I t ∑ b 1, …, b n ⩾ 0 b 1 + 2 ​ b 2 + ⋯ + n ​ b n = n − h ∑ i ∈ I j b i = m j − 𝟙 ​ ( t = j), ( 1 ⩽ j ⩽ r) ∏ i = 1 n ( 1 / i) b i b i!. \mathbb{P}\big(C_{I_{j}}(\sigma)=m_{j}\;(1\leqslant j\leqslant r)\big)=\frac{1}{n}\sum_{t\in\mathcal{T}}\sum_{h\in I_{t}}\sum_{\begin{subarray}{c}b_{1},\dots,b_{n}\geqslant 0\\ b_{1}+2b_{2}+\cdots+nb_{n}=n-h\\ \sum_{i\in I_{j}}b_{i}=m_{j}-\mathbbm{1}(t=j),\ (1\leqslant j\leqslant r)\end{subarray}}\prod_{i=1}^{n}\frac{(1/i)^{b_{i}}}{b_{i}!}. |  |

###### Proof.

Evidently

 | n #{ σ ∈ 𝒮 n: C I 1 ( σ) = m 1, …, C I r ( σ) = m r } = ∑ σ ∈ 𝒮 n C I j ​ ( σ) = m j ​ ( 1 ⩽ j ⩽ r) ∑ α | σ α ​ a cycle | α |. n\#\{\sigma\in\mathcal{S}_{n}:C_{I_{1}}(\sigma)=m_{1},\ldots,C_{I_{r}}(\sigma)=m_{r}\}=\sum_{\begin{subarray}{c}\sigma\in\mathcal{S}_{n}\\ C_{I_{j}}(\sigma)=m_{j}\;(1\leqslant j\leqslant r)\end{subarray}}\;\;\sum_{\begin{subarray}{c}\alpha|\sigma\\ \alpha\text{ a cycle}\end{subarray}}|\alpha|. |  |

Write σ = α ​ β \sigma=\alpha\beta and let h = | α | h=|\alpha|. Thus, for some t ∈ 𝒯 t\in\mathcal{T}, we have | α | = h ∈ I t |\alpha|=h\in I_{t} and

 | ( C I 1 ​ ( β), …, C I r ​ ( β)) = ( m 1 − 𝟙 ​ ( t = 1), …, m r − 𝟙 ​ ( t = r)). (C_{I_{1}}(\beta),\ldots,C_{I_{r}}(\beta))=(m_{1}-\mathbbm{1}(t=1),\ldots,m_{r}-\mathbbm{1}(t=r)). |  |

It is permissible to think of β ∈ 𝒮 n − h \beta\in\mathcal{S}_{n-h} and thus

 | n #{ σ ∈ 𝒮 n: C I 1 ( σ) = m 1, …, C I r ( σ) = m r } \displaystyle n\#\{\sigma\in\mathcal{S}_{n}:C_{I_{1}}(\sigma)=m_{1},\ldots,C_{I_{r}}(\sigma)=m_{r}\} | = ∑ t ∈ 𝒯 ∑ h ∈ I t ∑ α ∈ 𝒮 n, | α | = h α ​ a cycle h ​ ∑ β ∈ 𝒮 n − h C I i ​ ( β) = m i − 𝟙 ​ ( t = i), ( 1 ⩽ i ⩽ r) 1 \displaystyle=\sum_{t\in\mathcal{T}}\sum_{h\in I_{t}}\;\sum_{\begin{subarray}{c}\alpha\in\mathcal{S}_{n},|\alpha|=h\\ \alpha\text{ a cycle}\end{subarray}}h\sum_{\begin{subarray}{c}\beta\in\mathcal{S}_{n-h}\\ C_{I_{i}}(\beta)=m_{i}-\mathbbm{1}(t=i),(1\leqslant i\leqslant r)\end{subarray}}1 |  |

 |  | = ∑ t ∈ 𝒯 ∑ h ∈ I t n! ( n − h)! ​ ∑ β ∈ 𝒮 n − h C I i ​ ( β) = m i − 𝟙 ​ ( t = i), ( 1 ⩽ i ⩽ r) 1. \displaystyle=\sum_{t\in\mathcal{T}}\sum_{h\in I_{t}}\frac{n!}{(n-h)!}\sum_{\begin{subarray}{c}\beta\in\mathcal{S}_{n-h}\\ C_{I_{i}}(\beta)=m_{i}-\mathbbm{1}(t=i),(1\leqslant i\leqslant r)\end{subarray}}1. |  |

Now subdivide the sum according the cycle type ( b 1, …, b n) (b_{1},\ldots,b_{n}) of the permutation β \beta, use Cauchy’s formula (Thm. 1.2) to count such permutations for each type, and divide by n n. The desired identity follows. ∎

###### Proof of Theorem 1.5.

The right side in Lemma 4.1 is at most

 | 1 n ​ ∑ t ∈ 𝒯 ∑ b 1, …, b n ⩾ 0 ∑ i ∈ I j b i = m j − 𝟙 ​ ( t = j) ​ ( 1 ⩽ j ⩽ r) ∏ i ( 1 / i) b i b i!:= Y n, \frac{1}{n}\sum_{t\in\mathcal{T}}\sum_{\begin{subarray}{c}b_{1},\dots,b_{n}\geqslant 0\\ \sum_{i\in I_{j}}b_{i}=m_{j}-\mathbbm{1}(t=j)\;(1\leqslant j\leqslant r)\end{subarray}}\prod_{i}\frac{(1/i)^{b_{i}}}{b_{i}!}:=\frac{Y}{n}, |  |

say. By the multinomial theorem,

 | Y \displaystyle Y | = ∑ t ∈ 𝒯 ∑ b i ⩾ 0 ​ ( i ∈ I 1 ∪ ⋯ ∪ I r) ∑ i ∈ I j b i = m j − 𝟙 ​ ( t = j) ​ ( 1 ⩽ j ⩽ r) 1 ∏ i ∈ I 1 ∪ ⋯ ∪ I r b i! ​ i b i ​ ∑ b i ⩾ 0 ​ ( i ∈ I 0) 1 ∏ i ∈ I 0 b i! ​ i b i \displaystyle=\sum_{t\in\mathcal{T}}\sum_{\begin{subarray}{c}b_{i}\geqslant 0\;(i\in I_{1}\cup\cdots\cup I_{r})\\ \sum_{i\in I_{j}}b_{i}=m_{j}-\mathbbm{1}(t=j)\;(1\leqslant j\leqslant r)\end{subarray}}\frac{1}{\prod_{i\in I_{1}\cup\cdots\cup I_{r}}b_{i}!i^{b_{i}}}\sum_{b_{i}\geqslant 0\;(i\in I_{0})}\frac{1}{\prod_{i\in I_{0}}b_{i}!i^{b_{i}}} |  |

 |  | = ∑ t ∈ 𝒯 m t H ⁡ ( I t) ​ ∏ j = 1 r H ​ ( I j) m j m j! ​ e H ⁡ ( I 0). \displaystyle=\sum_{t\in\mathcal{T}}\frac{m_{t}}{H(I_{t})}\prod_{j=1}^{r}\frac{H(I_{j})^{m_{j}}}{m_{j}!}\mathrm{e}^{H(I_{0})}. |  |

The claimed bound now follows from H ⁡ ( I 0) = H n − H ⁡ ( I 1) − ⋯ − H ⁡ ( I r) H(I_{0})=H_{n}-H(I_{1})-\cdots-H(I_{r}). ∎

Later, we will sharpen the conclusion when r = 1 r=1, I 1 = [k] I_{1}=[k], m 1 = 0 m_{1}=0 (permutations lacking small cycles) and when r = 1 r=1, I 1 = { k + 1, …, n } I_{1}=\{k+1,\ldots,n\} and m 1 = 0 m_{1}=0 (permutations lacking large cycles).

###### Proof of Theorem 1.7.

For brevity, let H = H ⁡ ( I) H=H(I). For the first inequality, apply Corollary 1.6 for all m ⩽ λ ​ H m\leqslant\lambda H, using H n ⩽ log ⁡ n + 1 H_{n}\leqslant\log n+1, followed by an application of Lemma 2.4. This gives

 | ℙ ⁡ ( C I ​ ( σ) ⩽ λ ​ H) ⩽ 2 ​ ∑ m ⩽ λ ​ H e 1 − H ​ H m m! ⩽ 2 ​ e 1 − Q ⁡ ( λ) ​ H. \mathbb{P}(C_{I}(\sigma)\leqslant\lambda H)\leqslant 2\sum_{m\leqslant\lambda H}\mathrm{e}^{1-H}\frac{H^{m}}{m!}\leqslant 2\mathrm{e}^{1-Q(\lambda)H}. |  |

The second inequality is similar. We have

 | ℙ ⁡ ( C I ​ ( σ) ⩾ λ ​ H + 1) \displaystyle\mathbb{P}(C_{I}(\sigma)\geqslant\lambda H+1) | ⩽ ∑ m ⩾ λ ​ H + 1 e 1 − H ​ ( H m m! + H m − 1 ( m − 1)!) \displaystyle\leqslant\sum_{m\geqslant\lambda H+1}\mathrm{e}^{1-H}\bigg(\frac{H^{m}}{m!}+\frac{H^{m-1}}{(m-1)!}\bigg) |  |

 |  | ⩽ 2 ​ ∑ m ⩾ λ ​ H e 1 − H ​ H m m! ⩽ 2 ​ e 1 − Q ⁡ ( λ) ​ H. \displaystyle\leqslant 2\sum_{m\geqslant\lambda H}\mathrm{e}^{1-H}\frac{H^{m}}{m!}\leqslant 2\mathrm{e}^{1-Q(\lambda)H}. |  |

The third assertion is trivial if ψ ⩽ 1 \psi\leqslant 1, thus we may assume that ψ > 1 \psi>1, and in particular that H > 1 H>1. Define λ ± \lambda^{\pm} by

 | λ − ​ H = H − ψ ​ H, λ + ​ H + 1 = H + ψ ​ H. \lambda^{-}H=H-\psi\sqrt{H},\qquad\lambda^{+}H+1=H+\psi\sqrt{H}. |  |

In particular, 0 ⩽ λ − ⩽ 1 ⩽ λ + ⩽ 2 0\leqslant\lambda^{-}\leqslant 1\leqslant\lambda^{+}\leqslant 2. Apply the first inequality in Theorem 1.7 with λ = λ − \lambda=\lambda^{-} and the second inequality in Theorem 1.7 with λ = λ + \lambda=\lambda^{+}, obtaining

 | ℙ ⁡ ( | C I ​ ( σ) − H | ⩾ ψ ​ H) ⩽ 2 ​ e 1 − Q ⁡ ( λ −) ​ H + 2 ​ e 1 − Q ⁡ ( λ +) ​ H. \mathbb{P}\left(|C_{I}(\sigma)-H|\geqslant\psi\sqrt{H}\right)\leqslant 2\mathrm{e}^{1-Q(\lambda^{-})H}+2\mathrm{e}^{1-Q(\lambda^{+})H}. |  |

By ( 11),

 | Q ⁡ ( λ −) = Q ⁡ ( 1 − ψ H 1 / 2) ⩾ ψ 2 3 ​ H Q(\lambda^{-})=Q\left(1-\frac{\psi}{H^{1/2}}\right)\geqslant\frac{\psi^{2}}{3H} |  |

and

 | Q ⁡ ( λ +) = Q ⁡ ( 1 − ψ H 1 / 2 + 1 H) ⩾ 1 3 ​ H ​ ( ψ − 1 / H) 2 ⩾ ψ 2 − 2 3 ​ H Q(\lambda^{+})=Q\left(1-\frac{\psi}{H^{1/2}}+\frac{1}{H}\right)\geqslant\frac{1}{3H}(\psi-1/\sqrt{H})^{2}\geqslant\frac{\psi^{2}-2}{3H} |  |

and the third assertion follows, since 2 ​ e + 2 ​ e 5 / 3 ⩽ 20 2\mathrm{e}+2\mathrm{e}^{5/3}\leqslant 20. ∎

###### Proof of Theorem 1.8.

Let I = [a, b] ∩ ℕ I=[a,b]\cap{\mathbb{N}}, H = H ⁡ ( I) H=H(I) and let K K be a sufficiently large constant. The conclusions are trivial when b / a ⩽ K b/a\leqslant K, henceforth we assume that b / a > K b/a>K. By ( 11), the assertions are also trivial when

 | 1 − 1 log ⁡ ( b / a) ⩽ λ ⩽ 1 + 1 log ⁡ ( b / a), 1-\frac{1}{\sqrt{\log(b/a)}}\leqslant\lambda\leqslant 1+\frac{1}{\sqrt{\log(b/a)}}, |  |

and henceforth we assume that

 | | λ − 1 | > 1 log ⁡ ( b / a). |\lambda-1|>\frac{1}{\sqrt{\log(b/a)}}. |  | (16) |

By Lemma 2.1,

 | H = log ⁡ ( b / a) + O ⁡ ( 1). H=\log(b/a)+O(1). |  | (17) |

As the first assertion follows from Theorem 1.7 if λ = 0 \lambda=0, we may assume that λ > 0 \lambda>0.

Firstly, suppose that 0 < λ ⩽ 1 0<\lambda\leqslant 1 and that ( 16) holds. If we define λ ′ \lambda^{\prime} by

 | λ ​ log ⁡ ( b / a) = λ ′ ​ H, \lambda\log(b/a)=\lambda^{\prime}H, |  |

then λ ′ ⩽ 1 \lambda^{\prime}\leqslant 1, and thus by Theorem 1.7,

 | ℙ ⁡ ( C I ​ ( σ) ⩽ λ ​ log ⁡ ( b / a)) = ℙ ⁡ ( C I ​ ( σ) ⩽ λ ′ ​ H) ⩽ 2 ​ e 1 − Q ⁡ ( λ ′) ​ H. \mathbb{P}\left(C_{I}(\sigma)\leqslant\lambda\log(b/a)\right)=\mathbb{P}(C_{I}(\sigma)\leqslant\lambda^{\prime}H)\leqslant 2\mathrm{e}^{1-Q(\lambda^{\prime})H}. |  |

By ( 17),

 | | λ − λ ′ | ≪ min ⁡ ( λ, λ ′) log ⁡ ( b / a) |\lambda-\lambda^{\prime}|\ll\frac{\min(\lambda,\lambda^{\prime})}{\log(b/a)} |  |

and hence ( 12) implies that

 | Q ⁡ ( λ) − Q ⁡ ( λ ′) ≪ ( − log ⁡ min ⁡ ( λ, λ ′)) ​ min ⁡ ( λ, λ ′) log ⁡ ( b / a) ≪ 1 log ⁡ ( b / a) ≪ 1 H Q(\lambda)-Q(\lambda^{\prime})\ll(-\log\min(\lambda,\lambda^{\prime}))\frac{\min(\lambda,\lambda^{\prime})}{\log(b/a)}\ll\frac{1}{\log(b/a)}\ll\frac{1}{H} |  |

and the first assertion follows.

The proof of the second bound is similar. Suppose that 1 ⩽ λ ⩽ λ 0 1\leqslant\lambda\leqslant\lambda_{0} and ( 16) holds. If we define λ ′ \lambda^{\prime} by

 | λ ​ log ⁡ ( b / a) = λ ′ ​ H + 1, \lambda\log(b/a)=\lambda^{\prime}H+1, |  |

then 1 ⩽ λ ′ ⩽ 2 ​ λ 0 1\leqslant\lambda^{\prime}\leqslant 2\lambda_{0} if K K is large enough. Theorem 1.7 then implies that

 | ℙ ⁡ ( C I ​ ( σ) ⩾ λ ​ log ⁡ ( b / a)) = ℙ ⁡ ( C I ​ ( σ) ⩾ λ ′ ​ H + 1) ⩽ 2 ​ e 1 − Q ⁡ ( λ ′) ​ H. \mathbb{P}\left(C_{I}(\sigma)\geqslant\lambda\log(b/a)\right)=\mathbb{P}(C_{I}(\sigma)\geqslant\lambda^{\prime}H+1)\leqslant 2\mathrm{e}^{1-Q(\lambda^{\prime})H}. |  |

By ( 17), | λ − λ ′ | ≪ λ 0 1 log ⁡ ( b / a) ≪ 1 / H |\lambda-\lambda^{\prime}|\ll_{\lambda_{0}}\frac{1}{\log(b/a)}\ll 1/H. Since Q ′ ​ ( x) ⩽ log ⁡ ( 2 ​ λ 0) Q^{\prime}(x)\leqslant\log(2\lambda_{0}) for 1 ⩽ x ⩽ 2 ​ λ 0 1\leqslant x\leqslant 2\lambda_{0}, we have

 | | Q ( λ) − Q ( λ ′) | ≪ λ 0 1 / H |Q(\lambda)-Q(\lambda^{\prime})|\ll_{\lambda_{0}}1/H |  |

and the second assertion follows.

The final estimate follows from the first two, with λ 0 = 2 \lambda_{0}=2, and the bound ( 11) for Q ⁡ ( u) Q(u). ∎

###### Proof of Theorem 1.11.

We may assume that ψ \psi is sufficiently large. Let

 | k 1 = ⌊ log ⁡ ξ ⌋ + 1, k 2 = ⌊ log ⁡ n ⌋, k_{1}={\left\lfloor{\log\xi}\right\rfloor}+1,\qquad k_{2}={\left\lfloor{\log n}\right\rfloor}, |  |

and for k 1 ⩽ k ⩽ k 2 k_{1}\leqslant k\leqslant k_{2}, let t k = e k t_{k}=\mathrm{e}^{k}. Put t k 1 − 1 = ξ t_{k_{1}-1}=\xi and t k 2 + 1 = n t_{k_{2}+1}=n. For brevity, write C ⁡ ( σ, t):= ∑ j ⩽ t C j ​ ( σ) C(\sigma;t):=\sum_{j\leqslant t}C_{j}(\sigma). For each k k, k 1 − 1 ⩽ k ⩽ k 2 + 1 k_{1}-1\leqslant k\leqslant k_{2}+1, let N k ​ ( x) N_{k}(x) be the probability that

 | | C ⁡ ( σ, t k) − log ⁡ t k | ⩾ 2 ​ ( k − 1) ​ log ⁡ ( k − 1) − 1. |C(\sigma;t_{k})-\log t_{k}|\geqslant 2\sqrt{(k-1)\log(k-1)}-1. |  | (18) |

As log ⁡ t k = k + O ⁡ ( 1) \log t_{k}=k+O(1) for all t k t_{k} (including the endpoints),

 | 2 ​ ( k − 1) ​ log ⁡ ( k − 1) − 1 = ψ ​ log ⁡ t k, ψ = 2 ​ log ⁡ k + O ⁡ ( 1 / k). 2\sqrt{(k-1)\log(k-1)}-1=\psi\sqrt{\log t_{k}},\quad\psi=2\sqrt{\log k}+O(1/\sqrt{k}). |  |

Since k k is sufficiently large, for all k ⩾ k 1 k\geqslant k_{1} we have ψ ⩽ log ⁡ t k \psi\leqslant\sqrt{\log t_{k}}. By the third part of Theorem 1.8,

 | N k ​ ( x) ≪ e − 1 3 ​ ψ 2 ≪ 1 k 4 / 3. N_{k}(x)\ll\mathrm{e}^{-\frac{1}{3}\psi^{2}}\ll\frac{1}{k^{4/3}}. |  |

Summing over k k, we see that the probability that ( 18) holds for some k k is bounded by O ⁡ ( 1 / ( log ⁡ ξ) 1 / 3) O(1/(\log\xi)^{1/3}). Now suppose that ( 18) fails for every k k with k 1 − 1 ⩽ k ⩽ k 2 + 1 k_{1}-1\leqslant k\leqslant k_{2}+1. Let ξ ⩽ t ⩽ x \xi\leqslant t\leqslant x and suppose that t k ⩽ t ⩽ t k + 1 t_{k}\leqslant t\leqslant t_{k+1}. Evidently,

 | C ⁡ ( σ, t k) ⩽ C ⁡ ( σ, t) ⩽ C ⁡ ( σ, t k + 1). C(\sigma;t_{k})\leqslant C(\sigma;t)\leqslant C(\sigma;t_{k+1}). |  |

Since log ⁡ t k ⩾ k \log t_{k}\geqslant k and log ⁡ t k + 1 ⩽ k + 1 \log t_{k+1}\leqslant k+1, k ⩽ log ⁡ t ⩽ k + 1 k\leqslant\log t\leqslant k+1. By the failure of ( 18) at every k k,

 | C ⁡ ( σ, t) ⩾ log ⁡ t k − 2 ​ ( k − 1) ​ log ⁡ ( k − 1) + 1 ⩾ log ⁡ t − 2 ​ log ⁡ t ​ log ⁡ log ​ t C(\sigma;t)\geqslant\log t_{k}-2\sqrt{(k-1)\log(k-1)}+1\geqslant\log t-2\sqrt{\log t\log\log t} |  |

and

 | C ⁡ ( σ, t) ⩽ log ⁡ t k + 1 + 2 ​ k ​ log ⁡ k − 1 ⩽ log ⁡ t + 2 ​ log ⁡ t ​ log ⁡ log ​ t. ∎ C(\sigma;t)\leqslant\log t_{k+1}+2\sqrt{k\log k}-1\leqslant\log t+2\sqrt{\log t\log\log t}.\qed |  |

###### Proof of Theorem 1.12.

We may suppose that θ ⩾ θ 0 \theta\geqslant\theta_{0}, where θ 0 \theta_{0} is a sufficiently large, absolute constant, for otherwise the conclusion of the Corollary is trivial if the implied constant is large enough. Let ξ = ⌊ e ( 2 / 3) ​ θ ⌋ \xi={\left\lfloor{\mathrm{e}^{(2/3)\theta}}\right\rfloor}. By Theorem 1.11, with probability 1 − O ⁡ ( 1 / θ 1 / 3) 1-O(1/\theta^{1/3}), we have

 | | C [m] ​ ( σ) − log ⁡ m | < 2 ​ log ⁡ m ​ log ⁡ log ​ m ( ξ ⩽ m ⩽ n). |C_{[m]}(\sigma)-\log m|<2\sqrt{\log m\log\log m}\qquad(\xi\leqslant m\leqslant n). |  | (19) |

Also, by Corollary 1.10, with probability 1 − O ⁡ ( 1 / ξ) 1-O(1/\xi) all the cycles of σ \sigma of length ⩾ ξ \geqslant\xi have distinct lengths. Now suppose that σ \sigma is a permutation satisfying ( 19), and such that the cycles of σ \sigma with lengths ⩾ ξ \geqslant\xi have distinct lengths. We suppose that θ 0 \theta_{0} is so large that the right side of the inequality in ( 19) is at most 1 2 ​ log ⁡ m \frac{1}{2}\log m for every m ⩾ ξ m\geqslant\xi. In particular,

 | C [ξ] ​ ( σ) < 3 2 ​ log ⁡ ξ ⩽ θ, C_{[\xi]}(\sigma)<\frac{3}{2}\log\xi\leqslant\theta, |  |

that is, D θ ​ ( σ) > ξ D_{\theta}(\sigma)>\xi. Thus, we may apply ( 19) with m = D j ​ ( σ) m=D_{j}(\sigma) for all θ ⩽ j ⩽ C ⁡ ( σ) \theta\leqslant j\leqslant C(\sigma). As the cycle lengths ⩾ ξ \geqslant\xi are distinct, we have j = C [m] ​ ( σ) > 1 2 ​ log ⁡ D j ​ ( σ) j=C_{[m]}(\sigma)>\frac{1}{2}\log D_{j}(\sigma) and hence

 | | j − log ⁡ D j ​ ( σ) | < 2 ​ log ⁡ D j ​ ( σ) ​ log ⁡ log ⁡ D j ​ ( σ) < 2 ​ 2 ​ j ​ log ⁡ ( 2 ​ j) < 3 ​ j ​ log ⁡ j |j-\log D_{j}(\sigma)|<2\sqrt{\log D_{j}(\sigma)\log\log D_{j}(\sigma)}<2\sqrt{2j\log(2j)}<3\sqrt{j\log j} |  |

provided that θ 0 \theta_{0} is large enough (and hence j j is large enough). ∎

###### Proof of Theorem 1.13.

If k = 1 k=1, ℙ ⁡ ( C ⁡ ( σ) = 1) = 1 / n \mathbb{P}(C(\sigma)=1)=1/n. Now suppose k ⩾ 2 k\geqslant 2. We begin with Lemma 4.1, which implies that

 | n ⋅ ℙ ⁡ ( C ⁡ ( σ) = k) = ∑ b 1, …, b n ⩾ 0 b 1 + 2 ​ b 2 + ⋯ ⩽ n b 1 + ⋯ + b n = k − 1 1 ∏ i ⩽ n b i! ​ i b i. n\cdot\mathbb{P}(C(\sigma)=k)=\sum_{\begin{subarray}{c}b_{1},\ldots,b_{n}\geqslant 0\\ b_{1}+2b_{2}+\cdots\leqslant n\\ b_{1}+\cdots+b_{n}=k-1\end{subarray}}\frac{1}{\prod_{i\leqslant n}b_{i}!i^{b_{i}}}. |  | (20) |

We restrict the summations to b i = 0 ​ ( i > m) b_{i}=0\;\;(i>m) for some parameter m ∈ [1, n] m\in[1,n] to be chosen later. Using

 | 𝟙 ​ ( b 1 + 2 ​ b 2 + ⋯ + m ​ b m ⩽ n) ⩾ n − ( b 1 + 2 ​ b 2 + ⋯ + m ​ b m) n \mathbbm{1}(b_{1}+2b_{2}+\cdots+mb_{m}\leqslant n)\geqslant\frac{n-(b_{1}+2b_{2}+\cdots+mb_{m})}{n} |  |

and the multinomial theorem,

 | n ⋅ ℙ ⁡ ( C ⁡ ( σ) = k) \displaystyle n\cdot\mathbb{P}(C(\sigma)=k) | ⩾ 1 n ​ ∑ b 1, …, b m ⩾ 0 b 1 + ⋯ + b m = k − 1 n − ( b 1 + 2 ​ b 2 + ⋯ + m ​ b m) ∏ i ⩽ m b i! ​ i b i \displaystyle\geqslant\frac{1}{n}\sum_{\begin{subarray}{c}b_{1},\ldots,b_{m}\geqslant 0\\ b_{1}+\cdots+b_{m}=k-1\end{subarray}}\frac{n-(b_{1}+2b_{2}+\cdots+mb_{m})}{\prod_{i\leqslant m}b_{i}!i^{b_{i}}} |  |

 |  | = H m k − 1 ( k − 1)! − m n ⋅ H m k − 2 ( k − 2)! \displaystyle=\frac{H_{m}^{k-1}}{(k-1)!}-\frac{m}{n}\cdot\frac{H_{m}^{k-2}}{(k-2)!} |  |

 |  | = H m k − 1 ( k − 1)! ​ ( 1 − m ⁡ ( k − 1) n ​ H m). \displaystyle=\frac{H_{m}^{k-1}}{(k-1)!}\bigg(1-\frac{m(k-1)}{nH_{m}}\bigg). |  |

When 1 ⩽ k ⩽ log ⁡ n 1\leqslant k\leqslant\log n, we take m = n m=n and note that H m = H n ⩾ log ⁡ n H_{m}=H_{n}\geqslant\log n. This proves ( 3).

To obtain the 2nd part of Theorem 1.13, we fix A ⩾ 2 A\geqslant 2 and take m = n / ( 2 ​ A) m=n/(2A). We have H m = H n + O ⁡ ( log ⁡ A) H_{m}=H_{n}+O(\log A) and k ⩽ A ​ log ⁡ n ⩽ A ​ H n k\leqslant A\log n\leqslant AH_{n}. Hence, for n n large enough,

 | ℙ ⁡ ( C ⁡ ( σ) = k) ⩾ H m k − 1 3 ​ n ​ ( k − 1)! ⩾ c ⁡ ( A) ​ H n k − 1 ( k − 1)! ​ e − H n \mathbb{P}(C(\sigma)=k)\geqslant\frac{H_{m}^{k-1}}{3n(k-1)!}\geqslant c(A)\frac{H_{n}^{k-1}}{(k-1)!}\mathrm{e}^{-H_{n}} |  |

for some positive c ⁡ ( A) c(A). ∎

## 5 Conditioning on the total number of cycles

We will use an explicit Chernoff bound for tails of the binomial distribution. Denote by Bin ⁡ ( k, p) \Bin(k,p) a binomial random variable corresponding to k k trials, and parameter p ∈ [0, 1] p\in[0,1].

###### Lemma 5.1 ( [2, Lemma 4.7.2]).

If 0 < p < 1 0<p<1 and β ⩽ p \beta\leqslant p then we have

 | ℙ ⁡ ( Bin ⁡ ( n, p) ⩽ β ​ n) ⩽ exp ⁡ { − n ⁡ ( β ​ log ​ β p + ( 1 − β) ​ log ​ 1 − β 1 − p) } ⩽ exp ⁡ { − ( p − β) 2 ​ n 3 ​ p ​ ( 1 − p) }. \mathbb{P}(\Bin(n,p)\leqslant\beta n)\leqslant\exp\left\{-n\left(\beta\log\frac{\beta}{p}+(1-\beta)\log\frac{1-\beta}{1-p}\right)\right\}\leqslant\exp\bigg\{-\frac{(p-\beta)^{2}n}{3p(1-p)}\bigg\}. |  |

Replacing p p with 1 − p 1-p we also have for β ⩾ p \beta\geqslant p,

 | ℙ ⁡ ( Bin ⁡ ( n, p) ⩾ β ​ n) ⩽ exp ⁡ { − ( p − β) 2 ​ n 3 ​ p ​ ( 1 − p) }. \mathbb{P}(\Bin(n,p)\geqslant\beta n)\leqslant\exp\bigg\{-\frac{(p-\beta)^{2}n}{3p(1-p)}\bigg\}. |  |

###### Proof of Theorem 1.14.

Apply Theorem 1.5 with two sets: I I and [n] ∖ I [n]\setminus I. Here ε = 0 \varepsilon=0. Divide the right side in Theorem 1.5 by ℙ ⁡ ( C ⁡ ( σ) = k) \mathbb{P}(C(\sigma)=k), where a lower bound is given in Theorem 1.13. Set p = H ⁡ ( I) / H n p=H(I)/H_{n}. Then, for 0 ⩽ h ⩽ k 0\leqslant h\leqslant k,

 | ℙ ⁡ ( C I ​ ( σ) = h | C ⁡ ( σ) = k) \displaystyle\mathbb{P}\Big(C_{I}(\sigma)=h|C(\sigma)=k\Big) | = ℙ ⁡ ( C I ​ ( σ) = h ∧ C [n] ∖ I ​ ( σ) = k − h) ℙ ⁡ ( C ⁡ ( σ) = k) \displaystyle=\frac{\mathbb{P}(C_{I}(\sigma)=h\,\land\,C_{[n]\setminus I}(\sigma)=k-h)}{\mathbb{P}(C(\sigma)=k)} |  |

 |  | ≪ A ℙ ( Bin ( k − 1, p) = h − 1) + ℙ ( Bin ( k − 1, p) = h), \displaystyle\ll_{A}\mathbb{P}\big(\Bin(k-1,p)=h-1\big)+\mathbb{P}\big(\Bin(k-1,p)=h\big), |  |

Set β − = p − ψ ​ p ⁡ ( 1 − p) / ( k − 1) \beta^{-}=p-\psi\sqrt{p(1-p)/(k-1)}. By Lemma 5.1,

 | ℙ ( C I ( σ) ⩽ β − ( k − 1) | C ( σ) = k) ≪ A ℙ ( Bin ( k − 1, p) ⩽ β − ( k − 1)) ≪ A e − 1 3 ​ ψ 2. \mathbb{P}\Big(C_{I}(\sigma)\leqslant\beta^{-}(k-1)\;\;\big|\;\;C(\sigma)=k\big)\ll_{A}\mathbb{P}\Big(\Bin(k-1,p)\leqslant\beta^{-}(k-1)\Big)\ll_{A}\mathrm{e}^{-\frac{1}{3}\psi^{2}}. |  |

Let β + = p + ψ ​ p ⁡ ( 1 − p) / ( k − 1) − 1 k − 1 \beta^{+}=p+\psi\sqrt{p(1-p)/(k-1)}-\frac{1}{k-1}. Since 0 ⩽ ψ ⩽ p ​ ( 1 − p) ​ ( k − 1) 0\leqslant\psi\leqslant\sqrt{p(1-p)(k-1)},

 | ℙ ⁡ ( C I ​ ( σ) ⩾ β + ​ ( k − 1) + 1 | C ⁡ ( σ) = k) \displaystyle\mathbb{P}\Big(C_{I}(\sigma)\geqslant\beta^{+}(k-1)+1\;\;\big|\;\;C(\sigma)=k\Big) | ≪ A ℙ ( Bin ( k − 1, p) ⩾ β + ( k − 1)) \displaystyle\ll_{A}\mathbb{P}\Big(\Bin(k-1,p)\geqslant\beta^{+}(k-1)\Big) |  |

 |  | ≪ A exp { − ( ψ ​ p ⁡ ( 1 − p) − 1 / k − 1) 2 3 ​ p ​ ( 1 − p) } \displaystyle\ll_{A}\exp\bigg\{-\frac{(\psi\sqrt{p(1-p)}-1/\sqrt{k-1})^{2}}{3p(1-p)}\bigg\} |  |

 |  | ≪ A e − 1 3 ​ ψ 2. \displaystyle\ll_{A}\mathrm{e}^{-\frac{1}{3}\psi^{2}}. |  |

This completes the proof. ∎

## 6 Permutations without small cycles

###### Proof of Theorem 1.15.

Our proof is based on the Brun-Hooley sieve [34] from number theory. Let K ⩾ e 10 K\geqslant\mathrm{e}^{10} be fixed and sufficiently large and let u = n / m u=n/m. If u ⩽ K u\leqslant K, then Corollary 1.6 implies that ℙ ⁡ ( C [m] ​ ( σ) = 0) ≪ 1 / m \mathbb{P}(C_{[m]}(\sigma)=0)\ll 1/m and the conclusion follows. Now assume that u > K u>K and let

 | D = log ⁡ u, D=\log u, |  |

so that D ⩾ 10 D\geqslant 10. Partition [m] [m] into intervals I j = [z j, z j − 1) ∩ ℕ I_{j}=[z_{j},z_{j-1})\cap{\mathbb{N}}, where z j = m / D j z_{j}=m/D^{j}, 0 ⩽ j ⩽ ⌈ log ⁡ m log ⁡ D ⌉ = t 0\leqslant j\leqslant{\left\lceil\frac{\log m}{\log D}\right\rceil}=t. Let k 1, …, k t k_{1},\ldots,k_{t} be positive, even integers, subject to

 | k j ⩾ 10 ​ log ⁡ D ⁡ ( 1 ⩽ j ⩽ t), ∑ j = 1 t ( k j + 1) ​ m D j − 1 ⩽ n. k_{j}\geqslant 10\log D\;\;(1\leqslant j\leqslant t),\qquad\sum_{j=1}^{t}\frac{(k_{j}+1)m}{D^{j-1}}\leqslant n. |  | (21) |

With σ \sigma fixed, let

 | x j = 𝟙 ​ ( C I j ​ ( σ) = 0), y j = ∑ r = 0 k j ( − 1) r ​ ( C I j ​ ( σ) r). x_{j}=\mathbbm{1}(C_{I_{j}}(\sigma)=0),\quad y_{j}=\sum_{r=0}^{k_{j}}(-1)^{r}\binom{C_{I_{j}}(\sigma)}{r}. |  |

By Lemma 2.3, we have

 | 0 ⩽ y j − x j = ( C I j ​ ( σ) − 1 k j) ⩽ ( C I j ​ ( σ) k j + 1). 0\leqslant y_{j}-x_{j}=\binom{C_{I_{j}}(\sigma)-1}{k_{j}}\leqslant\binom{C_{I_{j}}(\sigma)}{k_{j}+1}. |  |

Using the elementary inequality

 | x 1 ⋯ x t ⩾ y 1 ⋯ y t − ∑ ℓ = 1 t ( y ℓ − x ℓ) ∏ j = 1 j ≠ ℓ t y j, x_{1}\cdots x_{t}\geqslant y_{1}\cdots y_{t}-\sum_{\ell=1}^{t}(y_{\ell}-x_{\ell})\prod_{\begin{subarray}{c}j=1\\ j\neq\ell\end{subarray}}^{t}y_{j}, |  |

together with ℙ ( C [m] ( σ) = 0) = 𝔼 x 1 ⋯ x t \mathbb{P}(C_{[m]}(\sigma)=0)={\mathbb{E}}\,x_{1}\cdots x_{t}, we thus obtain

 | M − E ⩽ ℙ ⁡ ( C [m] ​ ( σ) = 0) ⩽ M, M-E\leqslant\mathbb{P}(C_{[m]}(\sigma)=0)\leqslant M, |  | (22) |

where

 | M = 𝔼 y 1 ⋯ y t, E = 𝔼 ∑ ℓ = 1 t ( C I ℓ ​ ( σ) k ℓ + 1) ∏ j ≠ ℓ y j. M={\mathbb{E}}\,y_{1}\cdots y_{t},\qquad E={\mathbb{E}}\,\sum_{\ell=1}^{t}\binom{C_{I_{\ell}}(\sigma)}{k_{\ell}+1}\prod_{j\neq\ell}y_{j}. |  |

The condition ( 21) implies that

 | ∑ j ( k j + 1) ​ max ⁡ I j ⩽ n. \sum_{j}(k_{j}+1)\max I_{j}\leqslant n. |  | (23) |

Thus, by Theorem 1.3,

 | M \displaystyle M | = ∑ r 1, …, r t 0 ⩽ r j ⩽ k j ​ ( 1 ⩽ j ⩽ t) ( − 1) r 1 + ⋯ + r t 𝔼 ( C I 1 ​ ( σ) r 1) ⋯ ( C I t ​ ( σ) r t) \displaystyle=\sum_{\begin{subarray}{c}r_{1},\ldots,r_{t}\\ 0\leqslant r_{j}\leqslant k_{j}(1\leqslant j\leqslant t)\end{subarray}}(-1)^{r_{1}+\cdots+r_{t}}{\mathbb{E}}\,\binom{C_{I_{1}}(\sigma)}{r_{1}}\cdots\binom{C_{I_{t}}(\sigma)}{r_{t}} |  |

 |  | = ∑ r 1, …, r t 0 ⩽ r j ⩽ k j ​ ( 1 ⩽ j ⩽ t) ( − 1) r 1 + ⋯ + r t ​ ∏ j = 1 t H ⁡ ( I j) r j! = ∏ j = 1 t ( ∑ r j = 0 k j ( − H ⁡ ( I j)) r j r j!). \displaystyle=\sum_{\begin{subarray}{c}r_{1},\ldots,r_{t}\\ 0\leqslant r_{j}\leqslant k_{j}(1\leqslant j\leqslant t)\end{subarray}}(-1)^{r_{1}+\cdots+r_{t}}\prod_{j=1}^{t}\frac{H(I_{j})}{r_{j}!}=\prod_{j=1}^{t}\Bigg(\sum_{r_{j}=0}^{k_{j}}\frac{(-H(I_{j}))^{r_{j}}}{r_{j}!}\Bigg). |  |

Since H ⁡ ( I j) = log ⁡ D + O ⁡ ( 1) H(I_{j})=\log D+O(1) for every j j, and recalling ( 21), we have

 | ∑ r j = 0 k j ( − H ⁡ ( I j)) r j r j! \displaystyle\sum_{r_{j}=0}^{k_{j}}\frac{(-H(I_{j}))^{r_{j}}}{r_{j}!} | = e − H ⁡ ( I j) + O ⁡ ( H ​ ( I j) k j + 1 ( k j + 1)!) \displaystyle=\mathrm{e}^{-H(I_{j})}+O\left(\frac{H(I_{j})^{k_{j}+1}}{(k_{j}+1)!}\right) |  |

 |  | = e − H ⁡ ( I j) ​ ( 1 + O ⁡ ( D ​ ( log ⁡ D + O ⁡ ( 1)) k j + 1 ( k j + 1)!)) \displaystyle=\mathrm{e}^{-H(I_{j})}\bigg(1+O\left(\frac{D(\log D+O(1))^{k_{j}+1}}{(k_{j}+1)!}\right)\bigg) |  |

 |  | = e − H ⁡ ( I j) ​ exp ⁡ [O ⁡ ( D ​ ( log ⁡ D + O ⁡ ( 1)) k j + 1 ( k j + 1)!)]. \displaystyle=\mathrm{e}^{-H(I_{j})}\exp\Bigg[O\left(\frac{D(\log D+O(1))^{k_{j}+1}}{(k_{j}+1)!}\right)\Bigg]. |  | (24) |

Hence, the main term satisfies

 | M = e − H m ​ exp ⁡ [O ⁡ ( ∑ j = 1 t D ​ ( log ⁡ D + O ⁡ ( 1)) k j + 1 ( k j + 1)!)]. M=\mathrm{e}^{-H_{m}}\exp\left[O\left(\sum_{j=1}^{t}\frac{D(\log D+O(1))^{k_{j}+1}}{(k_{j}+1)!}\right)\right]. |  | (25) |

Similarly, using ( 23), the error term satisfies

 | E \displaystyle E | = ∑ ℓ = 1 t ∑ r j ​ ( j ≠ ℓ) OPEN 0 ⩽ r j ⩽ k j ​ ( j ≠ ℓ)) ( − 1) ∑ j ≠ ℓ r j ​ 𝔼 ​ ( C I ℓ ​ ( σ) k ℓ + 1) ​ ∏ j ≠ ℓ ( C I j ​ ( σ) r j) \displaystyle=\sum_{\ell=1}^{t}\sum_{\begin{subarray}{c}r_{j}(j\neq\ell)\\ 0\leqslant r_{j}\leqslant k_{j}(j\neq\ell))\end{subarray}}(-1)^{\sum_{j\neq\ell}r_{j}}{\mathbb{E}}\,\binom{C_{I_{\ell}}(\sigma)}{k_{\ell}+1}\prod_{j\neq\ell}\binom{C_{I_{j}}(\sigma)}{r_{j}} |  |

 |  | = ∑ ℓ = 1 t H ​ ( I ℓ) k ℓ + 1 ( k ℓ + 1)! ​ ∏ j ≠ ℓ ( ∑ r j = 0 k j ( − H ⁡ ( I j)) r j r j!). \displaystyle=\sum_{\ell=1}^{t}\frac{H(I_{\ell})^{k_{\ell}+1}}{(k_{\ell}+1)!}\prod_{j\neq\ell}\Bigg(\sum_{r_{j}=0}^{k_{j}}\frac{(-H(I_{j}))^{r_{j}}}{r_{j}!}\Bigg). |  |

Hence, by ( 24),

 | E = ∑ ℓ = 1 t e H ⁡ ( I ℓ) ​ ( log ⁡ D + O ⁡ ( 1)) k ℓ + 1 ( k ℓ + 1)! ​ e − H m ​ exp ⁡ [O ⁡ ( ∑ j = 1 t D ​ ( log ⁡ D + O ⁡ ( 1)) k j + 1 ( k j + 1)!)]. E=\sum_{\ell=1}^{t}\frac{\mathrm{e}^{H(I_{\ell})}(\log D+O(1))^{k_{\ell}+1}}{(k_{\ell}+1)!}\mathrm{e}^{-H_{m}}\exp\left[O\left(\sum_{j=1}^{t}\frac{D(\log D+O(1))^{k_{j}+1}}{(k_{j}+1)!}\right)\right]. |  | (26) |

We now take

 | k j = k 1 + 2 ​ ( j − 1) ( j ⩾ 1), k 1 = 2 ​ ⌊ D − 1 D ⋅ u 2 ⌋ − 6, k_{j}=k_{1}+2(j-1)\quad(j\geqslant 1),\;\;k_{1}=2{\left\lfloor{\frac{D-1}{D}\cdot\frac{u}{2}}\right\rfloor}-6, |  |

and readily verify that the conditions ( 21) hold if K K is large enough. Thus, by Stirling’s formula,

 | ∑ j = 1 t D ​ ( log ⁡ D + O ⁡ ( 1)) k j + 1 ( k j + 1)! \displaystyle\sum_{j=1}^{t}\frac{D(\log D+O(1))^{k_{j}+1}}{(k_{j}+1)!} | ≪ D ​ ( log ⁡ D + O ⁡ ( 1)) k 1 + 1 ( k 1 + 1)! \displaystyle\ll\frac{D(\log D+O(1))^{k_{1}+1}}{(k_{1}+1)!} |  |

 |  | ⩽ e − u ​ log ⁡ u + u ​ log ⁡ log ​ log ⁡ u + O ⁡ ( u) \displaystyle\leqslant\mathrm{e}^{-u\log u+u\log\log\log u+O(u)} |  |

and likewise

 | ∑ ℓ = 1 t e H ⁡ ( I ℓ) ​ ( log ⁡ D + O ⁡ ( 1)) k ℓ + 1 ( k ℓ + 1)! ⩽ e − u ​ log ⁡ u + u ​ log ⁡ log ​ log ⁡ u + O ⁡ ( u). \sum_{\ell=1}^{t}\frac{\mathrm{e}^{H(I_{\ell})}(\log D+O(1))^{k_{\ell}+1}}{(k_{\ell}+1)!}\leqslant\mathrm{e}^{-u\log u+u\log\log\log u+O(u)}. |  |

Inserting these last two bounds into ( 25) and ( 26), and recalling ( 22), the proof is complete. ∎

## 7 Permutations without large cycles

The traditional approach to the problem of estimating the probability that a random permutation has no cycle of size > m >m is via generating functions, e.g. Theorem 1. The sharpest results depend on a lengthy complex-analytic argument, see [55, 65].

###### Proof of Theorem 1.16.

Let w ⩾ 1 w\geqslant 1. If σ \sigma has no cycles of length > m >m, then ∑ j = 1 m j ​ C j ​ ( σ) = n \sum_{j=1}^{m}jC_{j}(\sigma)=n and hence

 | ν ⁡ ( n, m) ⩽ 𝔼 ​ w C 1 ​ ( σ) + 2 ​ C 2 ​ ( σ) + ⋯ + m ​ C m ​ ( σ) − n. \nu(n,m)\leqslant{\mathbb{E}}\,w^{C_{1}(\sigma)+2C_{2}(\sigma)+\cdots+mC_{m}(\sigma)-n}. |  |

For 1 ⩽ j ⩽ m 1\leqslant j\leqslant m, write w j = 1 + ( w j − 1) w^{j}=1+(w^{j}-1). By the binomial theorem and Lemma 3.1,

 | ν ⁡ ( n, m) \displaystyle\nu(n,m) | ⩽ w − n ​ 𝔼 ​ ∏ j = 1 m ( ∑ k j = 0 ∞ ( w j − 1) k j ​ ( C j ​ ( σ) k j)) \displaystyle\leqslant w^{-n}{\mathbb{E}}\,\prod_{j=1}^{m}\Bigg(\sum_{k_{j}=0}^{\infty}(w^{j}-1)^{k_{j}}\binom{C_{j}(\sigma)}{k_{j}}\Bigg) |  |

 |  | = w − n ∑ k 1, …, k m ⩾ 0 ( w − 1) k 1 ⋯ ( w m − 1) k m 𝔼 ( C 1 ​ ( σ) k 1) ⋯ ( C m ​ ( σ) k m) \displaystyle=w^{-n}\sum_{k_{1},\ldots,k_{m}\geqslant 0}(w-1)^{k_{1}}\cdots(w^{m}-1)^{k_{m}}{\mathbb{E}}\,\binom{C_{1}(\sigma)}{k_{1}}\cdots\binom{C_{m}(\sigma)}{k_{m}} |  |

 |  | ⩽ w − n ∑ k 1, …, k m ⩾ 0 ( w − 1) k 1 ⋯ ( w m − 1) k m ∏ j = 1 m ( 1 / j) k j k j! \displaystyle\leqslant w^{-n}\sum_{k_{1},\ldots,k_{m}\geqslant 0}(w-1)^{k_{1}}\cdots(w^{m}-1)^{k_{m}}\prod_{j=1}^{m}\frac{(1/j)^{k_{j}}}{k_{j}!} |  |

 |  | = w − n exp { w − 1 1 + w 2 − 1 2 + ⋯ w m − 1 m }. \displaystyle=w^{-n}\exp\Bigg\{\frac{w-1}{1}+\frac{w^{2}-1}{2}+\cdots\frac{w^{m}-1}{m}\Bigg\}. |  |

A good all-purpose choice is w = u 1 / m w=u^{1/m}, where u = n / m u=n/m. The mean value theorem implies that

 | w j = u j / m ⩽ 1 + ( u − 1) ​ j / m ( 1 ⩽ j ⩽ m) w^{j}=u^{j/m}\leqslant 1+(u-1)j/m\qquad(1\leqslant j\leqslant m) |  |

and hence

 | w − 1 + w 2 − 1 2 + ⋯ + w m − 1 m ⩽ ∑ j = 1 m ( u − 1) ​ j / m j = u − 1. w-1+\frac{w^{2}-1}{2}+\cdots+\frac{w^{m}-1}{m}\leqslant\sum_{j=1}^{m}\frac{(u-1)j/m}{j}=u-1. |  | (27) |

We conclude that

 | ν ( n, m) ⩽ u − n / m e u − 1 = e − u ​ log ⁡ u + u − 1. ∎ \nu(n,m)\leqslant u^{-n/m}\mathrm{e}^{u-1}=\mathrm{e}^{-u\log u+u-1}.\qed |  |

For the proof of Theorem 1.17, we need only very basic facts about the Dickman function ρ ⁡ ( u) \rho(u), namely that it is positive and decreasing. These facts follow quickly from the definition plus the relation

 | v ​ ρ ​ ( v) = ∫ v − 1 v ρ ⁡ ( u) ​ 𝑑 u ( v ⩾ 1) v\rho(v)=\int_{v-1}^{v}\rho(u)\,du\qquad(v\geqslant 1) |  | (28) |

obtained by integrating ( 5) from u = 1 u=1 to u = v u=v.

###### Proof of Theorem 1.17.

When m ⩽ n ⩽ 2 ​ m m\leqslant n\leqslant 2m, the desired bounds ( 6) follow from ( 8), the fact that ρ ⁡ ( u) = 1 − log ⁡ u \rho(u)=1-\log u for 1 ⩽ u ⩽ 2 1\leqslant u\leqslant 2 and the easy inequalities

 | log ⁡ ( n + 1 m + 1) = ∫ m + 1 n + 1 d ​ t t ⩽ H n − H m ⩽ ∫ n m d ​ t t = log ⁡ ( n m). \log\left(\frac{n+1}{m+1}\right)=\int_{m+1}^{n+1}\frac{dt}{t}\leqslant H_{n}-H_{m}\leqslant\int_{n}^{m}\frac{dt}{t}=\log\left(\frac{n}{m}\right). |  |

For larger n n, we fix m m and argue by induction. For 1 ⩽ ℓ ⩽ m 1\leqslant\ell\leqslant m, there are ( n ℓ) ⁡ ( ℓ − 1)! \binom{n}{\ell}(\ell-1)! ways to form an ℓ − \ell- cycle from [n] [n]. Hence

 | ν ⁡ ( n, m) = 1 n! ​ ∑ σ ∈ 𝒮 n C ( m, n] ​ ( σ) = 0 1 n ​ ∑ τ | σ τ ​ a cycle | τ | \displaystyle\nu(n,m)=\frac{1}{n!}\!\!\sum_{\begin{subarray}{c}\sigma\in\mathcal{S}_{n}\\ C_{(m,n]}(\sigma)=0\end{subarray}}\frac{1}{n}\sum_{\begin{subarray}{c}\tau|\sigma\\ \tau\text{ a cycle}\end{subarray}}|\tau| | = 1 n ⋅ n! ​ ∑ ℓ = 1 m ℓ ​ ( n ℓ) ​ ( ℓ − 1)! ​ ( n − ℓ)! ​ ν ​ ( n − ℓ, m) \displaystyle=\frac{1}{n\cdot n!}\sum_{\ell=1}^{m}\ell\binom{n}{\ell}(\ell-1)!(n-\ell)!\nu(n-\ell,m) |  |

 |  | = 1 n ​ ∑ k = n − m n − 1 ν ⁡ ( k, m). \displaystyle=\frac{1}{n}\sum_{k=n-m}^{n-1}\nu(k,m). |  |

Now fix m ⩾ 1 m\geqslant 1, let N ⩾ 2 ​ m + 1 N\geqslant 2m+1 and assume that ( 6) holds when m ⩽ n ⩽ N − 1 m\leqslant n\leqslant N-1. Using ( 28) and the monotonicity of ρ \rho,

 | ν ⁡ ( N, m) = 1 N ​ ∑ k = N − m N − 1 ν ⁡ ( k, m) \displaystyle\nu(N,m)=\frac{1}{N}\sum_{k=N-m}^{N-1}\nu(k,m) | ⩾ 1 N ​ ∑ k = N − m N − 1 ρ ⁡ ( k / m) > 1 N ​ ∑ k = N − m N − 1 ∫ k k + 1 ρ ⁡ ( t / m) ​ 𝑑 t \displaystyle\geqslant\frac{1}{N}\sum_{k=N-m}^{N-1}\rho(k/m)>\frac{1}{N}\sum_{k=N-m}^{N-1}\int_{k}^{k+1}\rho(t/m)\,dt |  |

 |  | = 1 N ​ ∫ N − m N ρ ⁡ ( v / m) ​ 𝑑 v = 1 N / m ​ ∫ N / m − 1 N / m ρ ⁡ ( v) ​ 𝑑 v = ρ ⁡ ( N / m) \displaystyle=\frac{1}{N}\int_{N-m}^{N}\rho(v/m)\,dv=\frac{1}{N/m}\int_{N/m-1}^{N/m}\rho(v)\,dv=\rho(N/m) |  |

and

 | ν ⁡ ( N, m) ⩽ 1 N ​ ∑ k = N − m N − 1 ρ ⁡ ( k + 1 m + 1) \displaystyle\nu(N,m)\leqslant\frac{1}{N}\sum_{k=N-m}^{N-1}\rho\left(\frac{k+1}{m+1}\right) | ⩽ 1 N ​ ∑ k = N − m N − 1 ∫ k − 1 k ρ ⁡ ( t + 1 m + 1) ​ 𝑑 t \displaystyle\leqslant\frac{1}{N}\sum_{k=N-m}^{N-1}\int_{k-1}^{k}\rho\left(\frac{t+1}{m+1}\right)\,dt |  |

 |  | = m + 1 N ​ ∫ N − m m + 1 N m + 1 ρ ⁡ ( v) ​ 𝑑 v \displaystyle=\frac{m+1}{N}\int_{\frac{N-m}{m+1}}^{\frac{N}{m+1}}\,\rho(v)\,dv |  |

 |  | = m + 1 N ​ ∫ N − m m + 1 N + 1 m + 1 ρ ⁡ ( v) ​ 𝑑 v − m + 1 N ​ ∫ N m + 1 N + 1 m + 1 ρ ⁡ ( v) ​ 𝑑 v \displaystyle=\frac{m+1}{N}\int_{\frac{N-m}{m+1}}^{\frac{N+1}{m+1}}\,\rho(v)\,dv-\frac{m+1}{N}\int_{\frac{N}{m+1}}^{\frac{N+1}{m+1}}\,\rho(v)\,dv |  |

 |  | = N + 1 N ​ ρ ​ ( N + 1 m + 1) − m + 1 N ​ ∫ N m + 1 N + 1 m + 1 ρ ⁡ ( v) ​ 𝑑 v. \displaystyle=\frac{N+1}{N}\rho\left(\frac{N+1}{m+1}\right)-\frac{m+1}{N}\int_{\frac{N}{m+1}}^{\frac{N+1}{m+1}}\,\rho(v)\,dv. |  |

The final integral on the right side is ⩾ 1 m + 1 ​ ρ ​ ( N + 1 m + 1) \geqslant\frac{1}{m+1}\rho\left(\frac{N+1}{m+1}\right) and thus ν ⁡ ( N, m) ⩽ ρ ⁡ ( N + 1 m + 1) \nu(N,m)\leqslant\rho\left(\frac{N+1}{m+1}\right). The claimed bounds ( 6) now follow by induction on n n. ∎

## 8 Poisson approximation of small cycle lengths

In this section, we prove Theorem 1.19, which shows that C j ​ ( σ) C_{j}(\sigma) is approximately Poisson with parameter 1 / j 1/j, uniformly for small j j.

We begin by relating d T ​ V ​ ( 𝒞 k, 𝒵 k) d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k}) to ℙ ​ ( C [m] ​ ( σ) = 0) \mathbb{P}(C_{[m]}(\sigma)=0) using a variant of a special case of [6, eq. (33)]. Define U ⁡ ( n, m) = ℙ n ​ ( C [m] ​ ( σ) = 0) U(n,m)=\mathbb{P}_{n}(C_{[m]}(\sigma)=0) for n ⩾ 0 n\geqslant 0 and U ⁡ ( n, m) = 0 U(n,m)=0 for n < 0 n<0.

###### Lemma 8.1.

We have

 | d T ​ V ​ ( 𝒞 k, 𝒵 k) = ∑ 𝐡 ∈ ℕ 0 k ∏ j = 1 k ( 1 / j) h j h j! ​ max ⁡ ( 0, e − H k − U ⁡ ( n ′, k)), d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k})=\sum_{\mathbf{h}\in{\mathbb{N}}_{0}^{k}}\;\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}\max\Big(0,\mathrm{e}^{-H_{k}}-U(n^{\prime},k)\Big), |  |

where n ′ = n ′ ​ ( 𝐡) = n − ∑ j = 1 k j ​ h j n^{\prime}=n^{\prime}(\mathbf{h})=n-\sum_{j=1}^{k}jh_{j}.

###### Proof.

We begin with the easy identity

 | d T ​ V ​ ( 𝒞 k, 𝒵 k) = ∑ 𝐡 ∈ ℕ 0 k max ⁡ ( 0, ℙ ⁡ ( 𝒵 k = 𝐡) − ℙ ⁡ ( 𝒞 k = 𝐡)). d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k})=\sum_{\mathbf{h}\in{\mathbb{N}}_{0}^{k}}\max\Big(0,\mathbb{P}(\mathcal{Z}_{k}=\mathbf{h})-\mathbb{P}(\mathcal{C}_{k}=\mathbf{h})\Big). |  |

Clearly,

 | ℙ ⁡ ( 𝒵 k = 𝐡) = e − H k ​ ∏ j = 1 k ( 1 / j) h j h j!. \mathbb{P}(\mathcal{Z}_{k}=\mathbf{h})=\mathrm{e}^{-H_{k}}\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}. |  |

Now fix 𝐡 \mathbf{h}, write g = h 1 + 2 ​ h 2 + ⋯ + k ​ h k g=h_{1}+2h_{2}+\cdots+kh_{k} and consider ℙ ⁡ ( 𝒞 k = 𝐡) \mathbb{P}(\mathcal{C}_{k}=\mathbf{h}). If g > n g>n, then ℙ ⁡ ( 𝒞 k = 𝐡) = 0 \mathbb{P}(\mathcal{C}_{k}=\mathbf{h})=0. Now suppose that g ⩽ n g\leqslant n. Write σ = σ 1 ​ σ 2 \sigma=\sigma_{1}\sigma_{2}, where σ 1 \sigma_{1} is the product of the cycles of length at most k k and permutes a subset I I of [n] [n] of size g g, and σ 2 \sigma_{2} is the product of the cycles of length greater than k k and permutes [n] ∖ I [n]\setminus I of size n ′ = n − g n^{\prime}=n-g. By Cauchy’s formula (Theorem 1.2), applied to σ 1 \sigma_{1}, it follows that

 | ℙ ⁡ ( 𝒞 k = 𝐡) = U ⁡ ( n ′, k) ​ ∏ j = 1 k ( 1 / j) h j h j!, \mathbb{P}(\mathcal{C}_{k}=\mathbf{h})=U(n^{\prime},k)\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}, |  |

and the lemma follows. ∎

###### Proof of Theorem 1.19.

We may assume that k ⩽ n / 100 k\leqslant n/100. We will use Lemma 8.1 and estimate the contribution to d T ​ V ​ ( 𝒞 k, 𝒵 k) d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k}) from the tuples 𝐡 = ( h 1, ⋯, h k) ∈ ℕ 0 k \mathbf{h}=(h_{1},\cdots,h_{k})\in{\mathbb{N}}_{0}^{k}. The main idea of the proof is to separately consider those vectors which constitute rare events (many h j h_{j} large): specifically, let

 | ℋ 1 \displaystyle\mathcal{H}_{1} | = { 𝐡 ∈ ℕ 0 k: h 1 + 2 ​ h 2 + ⋯ + k ​ h k ⩽ n − 50 ​ k }, \displaystyle=\{\mathbf{h}\in{\mathbb{N}}_{0}^{k}:h_{1}+2h_{2}+\cdots+kh_{k}\leqslant n-50k\}, |  |

 | ℋ 2 \displaystyle\mathcal{H}_{2} | = { 𝐡 ∈ ℕ 0 k: h 1 + 2 ​ h 2 + ⋯ + k ​ h k > n − 50 ​ k }. \displaystyle=\{\mathbf{h}\in{\mathbb{N}}_{0}^{k}:h_{1}+2h_{2}+\cdots+kh_{k}>n-50k\}. |  |

First, consider 𝐡 ∈ ℋ 1 \mathbf{h}\in\mathcal{H}_{1} and let n ′ = n − ( h 1 + 2 ​ h 2 + ⋯ + k ​ h k) ⩾ 50 ​ k n^{\prime}=n-(h_{1}+2h_{2}+\cdots+kh_{k})\geqslant 50k. By Theorem 1.15,

 | U ⁡ ( n ′, k) = e − H k ​ ( 1 + O ⁡ ( e − g ⁡ ( n ′ / k))), U(n^{\prime},k)=\mathrm{e}^{-H_{k}}\left(1+O(\mathrm{e}^{-g(n^{\prime}/k)})\right), |  |

where g ⁡ ( x) = − x ​ log ⁡ x + x ​ log ⁡ log ​ log ⁡ x + O ⁡ ( x) g(x)=-x\log x+x\log\log\log x+O(x) when x ⩾ 50 x\geqslant 50. It follows that

 | ∑ 𝐡 ∈ ℋ 1 ∏ j = 1 k ( 1 / j) h j h j! ​ | e − H k − U ⁡ ( n ′, k) | ≪ e − H k ​ ∑ 𝐡 ∈ ℋ 1 e − g ⁡ ( n ′ / k) ​ ∏ j = 1 k ( 1 / j) h j h j!. \sum_{\mathbf{h}\in\mathcal{H}_{1}}\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}\Big|\mathrm{e}^{-H_{k}}-U(n^{\prime},k)\Big|\ll\mathrm{e}^{-H_{k}}\sum_{\begin{subarray}{c}\mathbf{h}\in\mathcal{H}_{1}\end{subarray}}\mathrm{e}^{-g(n^{\prime}/k)}\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}. |  |

For 𝐡 ∈ ℋ 2 \mathbf{h}\in\mathcal{H}_{2}, we use a trivial bound

 | max ⁡ ( 0, e − H k − U ⁡ ( n ′, k)) ⩽ e − H k ⩽ 1 / k. \max\Big(0,\mathrm{e}^{-H_{k}}-U(n^{\prime},k)\Big)\leqslant\mathrm{e}^{-H_{k}}\leqslant 1/k. |  |

We conclude that

 | ∑ 𝐡 ∈ ℕ 0 k ∏ j = 1 k ( 1 / j) h j h j! ​ max ⁡ ( 0, e − H k − U ⁡ ( n ′, k)) ≪ 1 k ​ ∑ 50 ⩽ r ⩽ n / k + 1 e − g ⁡ ( r) ​ ∑ 𝐡 ∈ ℕ 0 k n ′ < r ​ k ∏ j = 1 k ( 1 / j) h j h j!. \sum_{\mathbf{h}\in{\mathbb{N}}_{0}^{k}}\;\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}\max\Big(0,\mathrm{e}^{-H_{k}}-U(n^{\prime},k)\Big)\ll\frac{1}{k}\sum_{50\leqslant r\leqslant n/k+1}\mathrm{e}^{-g(r)}\sum_{\begin{subarray}{c}\mathbf{h}\in{\mathbb{N}}_{0}^{k}\\ n^{\prime}<rk\end{subarray}}\;\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}. |  | (29) |

As in the proof of Theorem 1.16, we invoke the method of parameters, also known as the tilting method (this is commonly used in Chernoff inequalities; see Section 0.5 in [42] for number theoretic applications). For any real number w ⩾ 1 w\geqslant 1 we have

 | ∑ 𝐡 ∈ ℕ 0 k n ′ < r ​ k ∏ j = 1 k ( 1 / j) h j h j! \displaystyle\sum_{\begin{subarray}{c}\mathbf{h}\in{\mathbb{N}}_{0}^{k}\\ n^{\prime}<rk\end{subarray}}\;\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!} | ⩽ ∑ 𝐡 ∈ ℕ 0 k w h 1 + 2 ​ h 2 + ⋯ + k ​ h k − n + r ​ k ​ ∏ j = 1 k ( 1 / j) h j h j! \displaystyle\leqslant\sum_{\mathbf{h}\in{\mathbb{N}}_{0}^{k}}w^{h_{1}+2h_{2}+\cdots+kh_{k}-n+rk}\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!} |  |

 |  | = w − n + r ​ k ​ exp ⁡ { w + 1 2 ​ w 2 + ⋯ + 1 k ​ w k }. \displaystyle=w^{-n+rk}\exp\left\{w+\frac{1}{2}w^{2}+\cdots+\frac{1}{k}w^{k}\right\}. |  |

Take w = ( u − r + 2) 1 / k w=(u-r+2)^{1/k} where u = n k u=\frac{n}{k}. By the argument in ( 27),

 | w + 1 2 ​ w 2 + ⋯ + 1 k ​ w k ⩽ H k + u − r + 1 ⩽ log ⁡ k + u − r + 2. w+\frac{1}{2}w^{2}+\cdots+\frac{1}{k}w^{k}\leqslant H_{k}+u-r+1\leqslant\log k+u-r+2. |  |

It follows that

 | ∑ 𝐡 ∈ ℕ 0 k n ′ < r ​ k ∏ j = 1 k ( 1 / j) h j h j! ⩽ k ​ exp ⁡ { − ( u − r) ​ log ⁡ ( u − r + 2) + ( u − r + 2) }. \sum_{\begin{subarray}{c}\mathbf{h}\in{\mathbb{N}}_{0}^{k}\\ n^{\prime}<rk\end{subarray}}\;\prod_{j=1}^{k}\frac{(1/j)^{h_{j}}}{h_{j}!}\leqslant k\exp\big\{-(u-r)\log(u-r+2)+(u-r+2)\big\}. |  |

Inserting this into ( 29), we find that

 | d T ​ V ​ ( 𝒞 k, 𝒵 k) \displaystyle d_{TV}(\mathcal{C}_{k},\mathcal{Z}_{k}) | ≪ e u ​ log ⁡ log ⁡ log ​ u + O ⁡ ( u) ​ ∑ 50 ⩽ r ⩽ u + 1 e − r ​ log ⁡ r − ( u − r) ​ log ⁡ ( u − r + 2) \displaystyle\ll\mathrm{e}^{u\log\log\log u+O(u)}\sum_{50\leqslant r\leqslant u+1}\mathrm{e}^{-r\log r-(u-r)\log(u-r+2)} |  |

 |  | ≪ e u ​ log ⁡ log ⁡ log ​ u + O ⁡ ( u) ​ ∑ 50 ⩽ r ⩽ u + 1 1 r! ​ ( u + 2 − r)! \displaystyle\ll\mathrm{e}^{u\log\log\log u+O(u)}\sum_{50\leqslant r\leqslant u+1}\frac{1}{r!(u+2-r)!} |  |

 |  | ≪ e − u ​ log ⁡ u + u ​ log ⁡ log ​ log ⁡ u + O ⁡ ( u). ∎ \displaystyle\ll\mathrm{e}^{-u\log u+u\log\log\log u+O(u)}.\qed |  |

## 9 Central Limit Theorems

A principal tool is the fact that, as λ → ∞ \lambda\to\infty, the Poisson random variable with parameter λ \lambda approaches a Gaussian distribution with mean λ \lambda and variance λ \lambda. The following is a special case of the Central Limit Theorem with Berry-Esseen type rate of convergence. For completeness, we give a short proof in the Appendix using only Stirling’s formula and Euler summation.

###### Lemma 9.1 (Poisson CLT).

Let λ ⩾ 1 \lambda\geqslant 1, and let X X be Poisson with parameter λ \lambda. Uniformly for real λ ⩾ 1 \lambda\geqslant 1 and real z z, we have

 | ℙ ( X ⩽ λ + z λ) = Φ ( z) + O ( λ − 1 / 2), Φ ( z) = 1 2 ​ π ∫ − ∞ z e − 1 2 ​ t 2 d t. \mathbb{P}\left(X\leqslant\lambda+z\sqrt{\lambda}\right)=\Phi(z)+O\left(\lambda^{-1/2}\right),\qquad\Phi(z)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z}\mathrm{e}^{-\frac{1}{2}t^{2}}\,dt. |  |

###### Proof of Theorem 1.21.

Let H = H ⁡ ( I) H=H(I). We may assume that H ⩾ 100 H\geqslant 100, the assertion being trivial otherwise. If | w | ⩾ 3 ​ log ⁡ H |w|\geqslant\sqrt{3\log H} then the result follows from Theorem 1.7, since the left side is thus O ⁡ ( 1 / H) = Φ ⁡ ( w) + O ⁡ ( 1 / H) O(1/H)=\Phi(w)+O(1/H) if w ⩽ − 3 ​ log ⁡ H w\leqslant-\sqrt{3\log H} and is 1 − O ⁡ ( 1 / H) = Φ ⁡ ( w) + O ⁡ ( 1 / H) 1-O(1/H)=\Phi(w)+O(1/H) if w ⩾ 3 ​ log ⁡ H w\geqslant\sqrt{3\log H}. Suppose now that | w | < 3 ​ log ⁡ H |w|<\sqrt{3\log H}, let

 | A = H + w ​ H, m = ⌈ n log ⁡ H ⌉, J = I ∩ [m]. A=H+w\sqrt{H},\qquad m={\left\lceil\frac{n}{\log H}\right\rceil},\qquad J=I\cap[m]. |  |

Because

 | H ⁡ ( I ∖ J) = ∑ m < k ⩽ n k ∈ I 1 k ⩽ H ⁡ ( ( m, n] ∩ ℕ) ⩽ log ⁡ log ⁡ H + O ⁡ ( 1) H(I\setminus J)=\sum_{\begin{subarray}{c}m<k\leqslant n\\ k\in I\end{subarray}}\frac{1}{k}\leqslant H((m,n]\cap{\mathbb{N}})\leqslant\log\log H+O(1) |  |

we have H ⁡ ( J) = H + O ⁡ ( log ⁡ log ⁡ H) H(J)=H+O(\log\log H). Thus,

 | A = H ⁡ ( J) + w ′ ​ H ⁡ ( J), w ′ = w + O ⁡ ( log ⁡ log ⁡ H H). A=H(J)+w^{\prime}\sqrt{H(J)},\quad w^{\prime}=w+O\left(\frac{\log\log H}{\sqrt{H}}\right). |  |

Let Y Y be a Poisson random variable with parameter H ⁡ ( J) H(J). Thus, by Theorem 1.20 and Lemma 9.1,

 | ℙ ⁡ ( C I ​ ( σ) ⩽ A) \displaystyle\mathbb{P}(C_{I}(\sigma)\leqslant A) | ⩽ ℙ ⁡ ( C J ​ ( σ) ⩽ A) \displaystyle\leqslant\mathbb{P}(C_{J}(\sigma)\leqslant A) |  |

 |  | = ℙ ( Y ⩽ A) + O ( e − n / m) \displaystyle=\mathbb{P}(Y\leqslant A)+O(\mathrm{e}^{-n/m}) |  |

 |  | = Φ ( w ′) + O ( H ( J) − 1 / 2 + e − n / m) \displaystyle=\Phi(w^{\prime})+O\left(H(J)^{-1/2}+\mathrm{e}^{-n/m}\right) |  |

 |  | = Φ ⁡ ( w ′) + O ⁡ ( 1 H) \displaystyle=\Phi(w^{\prime})+O\left(\frac{1}{\sqrt{H}}\right) |  |

 |  | = Φ ⁡ ( w) + O ⁡ ( log ⁡ log ⁡ H H). \displaystyle=\Phi(w)+O\left(\frac{\log\log H}{\sqrt{H}}\right). |  |

We also have

 | A − log ⁡ H = H ⁡ ( J) + w ′′ ​ H ⁡ ( J), w ′′ = w + O ⁡ ( log ⁡ H H) A-\log H=H(J)+w^{\prime\prime}\sqrt{H(J)},\quad w^{\prime\prime}=w+O\left(\frac{\log H}{\sqrt{H}}\right) |  |

and it follows that

 | ℙ ⁡ ( C I ​ ( σ) ⩽ A) \displaystyle\mathbb{P}(C_{I}(\sigma)\leqslant A) | ⩾ ℙ ⁡ ( C J ​ ( σ) ⩽ A − log ⁡ H ​ and ​ C I ∖ J ​ ( σ) ⩽ log ⁡ H) \displaystyle\geqslant\mathbb{P}\left(C_{J}(\sigma)\leqslant A-\log H\text{ and }C_{I\setminus J}(\sigma)\leqslant\log H\right) |  |

 |  | = ℙ ⁡ ( C J ​ ( σ) ⩽ A − log ⁡ H), \displaystyle=\mathbb{P}\left(C_{J}(\sigma)\leqslant A-\log H\right), |  |

since min ⁡ ( I ∖ J) ⩾ n / log ⁡ H \min(I\setminus J)\geqslant n/\log H implies that C I ∖ J ​ ( σ) ⩽ log ⁡ H C_{I\setminus J}(\sigma)\leqslant\log H always. Hence, by Theorem 1.20 and Lemma 9.1,

 | ℙ ⁡ ( C I ​ ( σ) ⩽ A) \displaystyle\mathbb{P}(C_{I}(\sigma)\leqslant A) | ⩾ Φ ⁡ ( w ′′) + O ⁡ ( 1 / H) \displaystyle\geqslant\Phi(w^{\prime\prime})+O(1/\sqrt{H}) |  |

 |  | = Φ ⁡ ( w) + O ⁡ ( log ⁡ H H). \displaystyle=\Phi(w)+O\left(\frac{\log H}{\sqrt{H}}\right). |  |

The theorem follows by combining the upper and lower bounds for ℙ ⁡ ( C I ​ ( σ) ⩽ A) \mathbb{P}(C_{I}(\sigma)\leqslant A). ∎

###### Proof of Theorem 1.23.

We may assume that j ⩾ 10 j\geqslant 10 and that n n is sufficiently large, the statement being trivial otherwise. We may also assume that | w | ⩽ log ⁡ j |w|\leqslant\sqrt{\log j}, since the statement for w w outside this range follows from the monotonicity of ℙ ⁡ ( log ⁡ D j ​ ( σ) ⩽ j + w ​ j) \mathbb{P}(\log D_{j}(\sigma)\leqslant j+w\sqrt{j}), as a function of w w, the statement for the two points w = ± log ⁡ j w=\pm\sqrt{\log j} and the fact that Φ ⁡ ( − log ⁡ j) ≪ 1 / j 1 / 2 \Phi(-\sqrt{\log j})\ll 1/j^{1/2} and Φ ⁡ ( log ⁡ j) = 1 − O ⁡ ( 1 / j 1 / 2) \Phi(\sqrt{\log j})=1-O(1/j^{1/2}).

Let k = ⌊ e j + w ​ j ⌋ k={\left\lfloor{\mathrm{e}^{j+w\sqrt{j}}}\right\rfloor}, so by hypothesis,

 | log ⁡ k ⩽ j + j ​ log ⁡ j ⩽ j + ( log ⁡ n) ​ log ⁡ log ​ n ⩽ log ⁡ n. \log k\leqslant j+\sqrt{j\log j}\leqslant j+\sqrt{(\log n)\log\log n}\leqslant\log n. |  |

Then D j ​ ( σ) ⩽ k D_{j}(\sigma)\leqslant k is equivalent to C [k] ​ ( σ) ⩾ j C_{[k]}(\sigma)\geqslant j. As H k = log ⁡ k + O ⁡ ( 1) H_{k}=\log k+O(1) and H k = j + O ⁡ ( | w | + 1) \sqrt{H_{k}}=\sqrt{j}+O(|w|+1), we have

 | j − 1 = H k − u ​ H k, where u = w + O ⁡ ( w 2 + 1 j). j-1=H_{k}-u\sqrt{H_{k}},\quad\text{where}\quad u=w+O\left(\frac{w^{2}+1}{\sqrt{j}}\right). |  |

By Theorem 1.21,

 | ℙ ⁡ ( D j ​ ( σ) ⩽ k) \displaystyle\mathbb{P}(D_{j}(\sigma)\leqslant k) | = ℙ ⁡ ( C [k] ​ ( σ) ⩾ j) = 1 − ℙ ⁡ ( C [k] ​ ( σ) ⩽ j − 1) \displaystyle=\mathbb{P}(C_{[k]}(\sigma)\geqslant j)=1-\mathbb{P}(C_{[k]}(\sigma)\leqslant j-1) |  |

 |  | = 1 − Φ ⁡ ( u) + O ⁡ ( log ⁡ H k H k) \displaystyle=1-\Phi(u)+O\left(\frac{\log H_{k}}{\sqrt{H_{k}}}\right) |  |

 |  | = Φ ⁡ ( u) + O ⁡ ( log ⁡ ( 2 ​ j) j). \displaystyle=\Phi(u)+O\left(\frac{\log(2j)}{\sqrt{j}}\right). |  |

Also,

 | Φ ⁡ ( u) = Φ ⁡ ( w) + O ⁡ ( w 2 + 1 j) = Φ ⁡ ( w) + O ⁡ ( log ⁡ ( 2 ​ j) j) \Phi(u)=\Phi(w)+O\left(\frac{w^{2}+1}{\sqrt{j}}\right)=\Phi(w)+O\left(\frac{\log(2j)}{\sqrt{j}}\right) |  |

and the proof is complete. ∎

## 10 Fixed sets and divisors of permutations

###### Proof of Theorem 1.24.

Evidently, 2 C ⁡ ( σ) 2^{C(\sigma)} equals the number of divisors β | σ \beta|\sigma. The permutation β \beta fixes a set I I. Summing over I I we see that

 | 𝔼 ​ 2 C ⁡ ( σ) \displaystyle{\mathbb{E}}\,2^{C(\sigma)} | = 1 n! ∑ σ ∈ 𝒮 n ∑ β | σ 1 = 1 n! ∑ I ⊆ [n] ∑ σ ∈ 𝒮 n σ fixes I 1 \displaystyle=\frac{1}{n!}\sum_{\sigma\in\mathcal{S}_{n}}\sum_{\beta|\sigma}1=\frac{1}{n!}\sum_{I\subseteq[n]}\sum_{\begin{subarray}{c}\sigma\in\mathcal{S}_{n}\\ \sigma\text{ fixes }I\end{subarray}}1 |  |

 |  | = 1 n! ​ ∑ I ⊆ [n] ( n − | I |)! ​ | I |! \displaystyle=\frac{1}{n!}\sum_{I\subseteq[n]}(n-|I|)!|I|! |  |

 |  | = 1 n! ​ ∑ j = 0 n ( n − j)! ​ j! ​ ( n j) = ∑ j = 0 n 1 = n + 1. ∎ \displaystyle=\frac{1}{n!}\sum_{j=0}^{n}(n-j)!j!\binom{n}{j}=\sum_{j=0}^{n}1=n+1.\qed |  |

###### Proof of Theorem 1.25.

The statement is trivial for 1 ⩽ k ⩽ 100 1\leqslant k\leqslant 100, thus we may assume that k > 100 k>100. Let r 0 = H k log ⁡ 2 r_{0}=\frac{H_{k}}{\log 2}, so that r 0 = log ⁡ k log ⁡ 2 + O ⁡ ( 1) r_{0}=\frac{\log k}{\log 2}+O(1). By Theorem 1.8,

 | ℙ ⁡ ( C [k] ​ ( σ) ⩾ r 0) ≪ k − Q ⁡ ( 1 / log ⁡ 2) = k − ℰ. \mathbb{P}(C_{[k]}(\sigma)\geqslant r_{0})\ll k^{-Q(1/\log 2)}=k^{-\mathcal{E}}. |  |

If σ \sigma has a fixed set of size k k, then σ \sigma factors as σ = α ​ β \sigma=\alpha\beta, where | α | = k |\alpha|=k and | β | = n − k |\beta|=n-k. Hence, if C [k] ​ ( σ) < r 0 C_{[k]}(\sigma)<r_{0}, then for some non-negative integers j, h j,h with j + h < r 0 j+h<r_{0} we have

 | C ⁡ ( α) = j, C [k] ​ ( β) = h. C(\alpha)=j,\qquad C_{[k]}(\beta)=h. |  | (30) |

With j, h j,h fixed the number of pairs α, β \alpha,\beta with ( 30) is at most

 | ( n k) ​ k! ​ ℙ k ​ ( C ⁡ ( α) = j) ​ ( n − k)! ​ ℙ n − k ​ ( C [k] ​ ( β) = h) ≪ n! ​ H k j + h ​ e − 2 ​ H k j! ​ h!, \binom{n}{k}k!\mathbb{P}_{k}(C(\alpha)=j)(n-k)!\;\mathbb{P}_{n-k}(C_{[k]}(\beta)=h)\ll n!\frac{H_{k}^{j+h}\mathrm{e}^{-2H_{k}}}{j!h!}, |  |

upon invoking Lemma 1.5. Summing first over all j, h j,h with h + j = r h+j=r using the binomial theorem, and then over r < r 0 r<r_{0} we see that the probability that C [k] ​ ( σ) < r 0 C_{[k]}(\sigma)<r_{0} and σ \sigma factors as σ = α ​ β \sigma=\alpha\beta with | α | = k |\alpha|=k is bounded above by

 | ≪ e − 2 ​ H k ​ ∑ r < r 0 ( 2 ​ H k) r r! ≪ k − Q ⁡ ( 1 2 ​ log ⁡ 2) = k − ℰ, \ll\mathrm{e}^{-2H_{k}}\sum_{r<r_{0}}\frac{(2H_{k})^{r}}{r!}\ll k^{-Q(\frac{1}{2\log 2})}=k^{-\mathcal{E}}, |  |

upon invoking Lemma 2.4. ∎

## Appendix

In this appendix, we proof Lemma 9.1 and ( 7).

###### Proof of Lemma 9.1.

We give a short, direct proof using Stirling’s formula and Euler summation. Let h ∗ = 3 ​ log ⁡ ( 1 + λ) h^{*}=3\sqrt{\log(1+\lambda)}. We may assume that λ \lambda is sufficiently large. By Proposition 2.4 and the crude bounds for Q ⁡ ( x) Q(x) given in ( 11), we have

 | ℙ ⁡ ( | X − λ | > h ∗ ​ λ) ⩽ 2 ​ e − 3 ​ log ⁡ ( 1 + λ) = 2 ( 1 + λ) 3. \mathbb{P}(|X-\lambda|>h^{*}\sqrt{\lambda})\leqslant 2\mathrm{e}^{-3\log(1+\lambda)}=\frac{2}{(1+\lambda)^{3}}. |  |

Likewise,

 | ∫ | t | > h ∗ e − 1 2 ​ t 2 ​ 𝑑 t ≪ 1 ( 1 + λ) 3. \int\limits_{|t|>h^{*}}\mathrm{e}^{-\frac{1}{2}t^{2}}\,dt\ll\frac{1}{(1+\lambda)^{3}}. |  | (31) |

Consequently, we may assume that | z | ⩽ h ∗ |z|\leqslant h^{*}, and deduce

 | ℙ ⁡ ( X ⩽ λ + z ​ λ) = e − λ ​ ∑ λ − h ∗ ​ λ ⩽ k ⩽ λ + z ​ λ λ k k! + O ⁡ ( 1 λ 3). \mathbb{P}\left(X\leqslant\lambda+z\sqrt{\lambda}\right)=\mathrm{e}^{-\lambda}\sum_{\lambda-h^{*}\sqrt{\lambda}\leqslant k\leqslant\lambda+z\sqrt{\lambda}}\frac{\lambda^{k}}{k!}+O\left(\frac{1}{\lambda^{3}}\right). |  |

For | k − λ | ⩽ h ∗ ​ λ |k-\lambda|\leqslant h^{*}\sqrt{\lambda}, Stirling’s formula implies that

 | k! = ( k e) k ​ 2 ​ π ​ λ ​ ( 1 + O ⁡ ( | k − λ | + 1 λ)). k!=\left(\frac{k}{\mathrm{e}}\right)^{k}\sqrt{2\pi\lambda}\left(1+O\left(\frac{|k-\lambda|+1}{\lambda}\right)\right). |  |

Write k = λ + u k=\lambda+u. Then, for | u | ⩽ h ∗ ​ λ |u|\leqslant h^{*}\sqrt{\lambda}, we have

 | e − λ ​ λ k k! \displaystyle\mathrm{e}^{-\lambda}\frac{\lambda^{k}}{k!} | = 1 + O ⁡ ( | u | + 1 λ) 2 ​ π ​ λ ​ e − λ ​ ( e ​ λ λ + u) λ + u = 1 + O ⁡ ( | u | + 1 λ) 2 ​ π ​ λ ​ e u ( 1 + u / λ) λ + u \displaystyle=\frac{1+O\left(\frac{|u|+1}{\lambda}\right)}{\sqrt{2\pi\lambda}}\mathrm{e}^{-\lambda}\left(\frac{\mathrm{e}\lambda}{\lambda+u}\right)^{\lambda+u}=\frac{1+O\left(\frac{|u|+1}{\lambda}\right)}{\sqrt{2\pi\lambda}}\frac{\mathrm{e}^{u}}{(1+u/\lambda)^{\lambda+u}} |  |

 |  | = 1 + O ⁡ ( | u | + 1 λ) 2 ​ π ​ λ ​ exp ⁡ { u − ( λ + u) ​ ( u λ − 1 2 ​ ( u λ) 2 + O ⁡ ( ( u λ) 3)) } \displaystyle=\frac{1+O\left(\frac{|u|+1}{\lambda}\right)}{\sqrt{2\pi\lambda}}\exp\left\{u-(\lambda+u)\left(\frac{u}{\lambda}-\frac{1}{2}\left(\frac{u}{\lambda}\right)^{2}+O\left(\left(\frac{u}{\lambda}\right)^{3}\right)\right)\right\} |  |

 |  | = ( 1 + O ⁡ ( 1 + | u | λ + | u | 3 λ 2)) ​ e − u 2 2 ​ λ 2 ​ π ​ λ. \displaystyle=\left(1+O\left(\frac{1+|u|}{\lambda}+\frac{|u|^{3}}{\lambda^{2}}\right)\right)\frac{\mathrm{e}^{-\frac{u^{2}}{2\lambda}}}{\sqrt{2\pi\lambda}}. |  |

It follows that

 | e − λ ​ ∑ λ − h ∗ ​ λ ⩽ k ⩽ λ + z ​ λ λ k k! = M + E, \mathrm{e}^{-\lambda}\sum_{\lambda-h^{*}\sqrt{\lambda}\leqslant k\leqslant\lambda+z\sqrt{\lambda}}\frac{\lambda^{k}}{k!}=M+E, |  |

where

 | M = 1 2 ​ π ​ λ ​ ∑ λ − h ∗ ​ λ ⩽ k ⩽ λ + z ​ λ e − ( k − λ) 2 2 ​ λ M=\frac{1}{\sqrt{2\pi\lambda}}\sum_{\lambda-h^{*}\sqrt{\lambda}\leqslant k\leqslant\lambda+z\sqrt{\lambda}}\mathrm{e}^{-\frac{(k-\lambda)^{2}}{2\lambda}} |  |

and

 | E \displaystyle E | ≪ 1 λ ​ ∑ k ( 1 + | k − λ | λ + | k − λ | 3 λ 2) ​ e − | k − λ | 2 2 ​ λ \displaystyle\ll\frac{1}{\sqrt{\lambda}}\sum_{k}\left(\frac{1+|k-\lambda|}{\lambda}+\frac{|k-\lambda|^{3}}{\lambda^{2}}\right)\mathrm{e}^{-\frac{|k-\lambda|^{2}}{2\lambda}} |  |

 |  | ≪ ∑ a = 1 ∞ ( a + a 3 λ) e − ( a − 1) 2 / 2 ≪ 1 λ. \displaystyle\ll\sum_{a=1}^{\infty}\left(\frac{a+a^{3}}{\sqrt{\lambda}}\right)\mathrm{e}^{-(a-1)^{2}/2}\ll\frac{1}{\sqrt{\lambda}}. |  |

By Euler summation, and writing { t } = t − ⌊ t ⌋ \{t\}=t-{\left\lfloor{t}\right\rfloor},

 | M = 1 2 ​ π ​ λ ​ [∫ λ − h ∗ ​ λ λ + z ​ λ e − ( t − λ) 2 2 ​ λ ​ 𝑑 t − ∫ λ − h ∗ ​ λ λ + z ​ λ { t } ​ ( t − λ λ) ​ e − ( t − λ) 2 2 ​ λ ​ 𝑑 t + O ⁡ ( 1)]. M=\frac{1}{\sqrt{2\pi\lambda}}\Bigg[\int_{\lambda-h^{*}\sqrt{\lambda}}^{\lambda+z\sqrt{\lambda}}\mathrm{e}^{-\frac{(t-\lambda)^{2}}{2\lambda}}\,dt-\int_{\lambda-h^{*}\sqrt{\lambda}}^{\lambda+z\sqrt{\lambda}}\{t\}\left(\frac{t-\lambda}{\lambda}\right)\mathrm{e}^{-\frac{(t-\lambda)^{2}}{2\lambda}}\,dt+O(1)\Bigg]. |  |

The integral involving { t } \{t\} is O ⁡ ( 1) O(1). The first integral equals, by ( 31),

 | λ ∫ − h ∗ z e − 1 2 ​ u 2 d u = λ ∫ − ∞ z e − 1 2 ​ u 2 d u + O ( λ − 5 / 2), \sqrt{\lambda}\int_{-h^{*}}^{z}\mathrm{e}^{-\frac{1}{2}u^{2}}\,du=\sqrt{\lambda}\int_{-\infty}^{z}\mathrm{e}^{-\frac{1}{2}u^{2}}\,du+O(\lambda^{-5/2}), |  |

and hence

 | M = 1 2 ​ π ​ ∫ − ∞ z e − 1 2 ​ u 2 ​ 𝑑 u + O ⁡ ( 1 λ) = Φ ⁡ ( z) + O ⁡ ( 1 λ). ∎ M=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z}\mathrm{e}^{-\frac{1}{2}u^{2}}\,du+O\left(\frac{1}{\sqrt{\lambda}}\right)=\Phi(z)+O\left(\frac{1}{\sqrt{\lambda}}\right).\qed |  |

###### Proof of ( 7).

It suffices to show that

 | − ρ ′ ​ ( u) ρ ⁡ ( u) ≪ 1 + log ⁡ u ( u > 1). -\frac{\rho^{\prime}(u)}{\rho(u)}\ll 1+\log u\qquad(u>1). |  | (32) |

From ( 5) and ( 28),

 | − ρ ′ ​ ( u) ρ ⁡ ( u) = ρ ⁡ ( u − 1) ∫ u − 1 u ρ ⁡ ( v) ​ 𝑑 v. -\frac{\rho^{\prime}(u)}{\rho(u)}=\frac{\rho(u-1)}{\int_{u-1}^{u}\rho(v)\,dv}. |  | (33) |

Let B k = max 1 < v ⩽ k / 2 ( − ρ ′ ( v) / ρ ( v)) B_{k}=\max_{1<v\leqslant k/2}(-\rho^{\prime}(v)/\rho(v)). We have

 | B 4 = max 1 < v ⩽ 2 ⁡ 1 / v 1 − log ⁡ v = 1 2 ​ ( 1 − log ⁡ 2) = 1.629 ​ …. B_{4}=\max_{1<v\leqslant 2}\frac{1/v}{1-\log v}=\frac{1}{2(1-\log 2)}=1.629\ldots. |  |

If k ⩾ 4 k\geqslant 4 and k / 2 < u ⩽ ( k + 1) / 2 k/2<u\leqslant(k+1)/2 then the denominator on the right side of ( 33) is at least

 | ∫ u − 1 u − 1 / 2 ρ ⁡ ( v) ​ 𝑑 v ⩾ ρ ⁡ ( u − 1) ​ ∫ u − 1 u − 1 / 2 e − B k ​ ( v − u + 1) ​ 𝑑 v = ρ ⁡ ( u − 1) ​ ( 1 − e − 1 2 ​ B k) B k. \int_{u-1}^{u-1/2}\rho(v)\,dv\geqslant\rho(u-1)\int_{u-1}^{u-1/2}\mathrm{e}^{-B_{k}(v-u+1)}\,dv=\frac{\rho(u-1)(1-\mathrm{e}^{-\frac{1}{2}B_{k}})}{B_{k}}. |  |

Using that e − 1 2 ​ B k ⩽ e − 1 2 ​ B 4 < 1 / 2 \mathrm{e}^{-\frac{1}{2}B_{k}}\leqslant\mathrm{e}^{-\frac{1}{2}B_{4}}<1/2, we infer that

 | B k + 1 ⩽ B k 1 − e − 1 2 ​ B k ⩽ B k ​ ( 1 + 2 ​ e − 1 2 ​ B k). B_{k+1}\leqslant\frac{B_{k}}{1-\mathrm{e}^{-\frac{1}{2}B_{k}}}\leqslant B_{k}\left(1+2\mathrm{e}^{-\frac{1}{2}B_{k}}\right). |  |

The function x ( 1 + 2 e − x / 2) x(1+2\mathrm{e}^{-x/2}) is increasing for x ⩾ 0 x\geqslant 0, hence if C C is large and B k ⩽ C ​ log ⁡ k B_{k}\leqslant C\log k then

 | B k + 1 ⩽ ( C ​ log ⁡ k) ​ ( 1 + 2 / k C / 2) ⩽ C ​ log ⁡ ( k + 1). B_{k+1}\leqslant(C\log k)(1+2/k^{C/2})\leqslant C\log(k+1). |  |

Therefore, B k ≪ log ⁡ k B_{k}\ll\log k and ( 32) follows. ∎

Somewhat stronger local bounds on ρ ⁡ ( u) \rho(u), also proved by elementary methods, can be found in section 2 of [44].

## Acknowledgments

The author thanks Sean Eberhard and Ben Green for helpful comments on an early draft, and thanks Dimitris Koukoulopoulos for showing him the lower bound argument in Theorem 1.18. The author also thanks the anonymous referee for carefully reading the paper and making many helpful suggestions.

## References

- [1] H. Acan, C. Burnette, S. Eberhard, E. Schmutz and J. Thomas. *Permutations with equal orders*, Combin. Probab. Comput. 30 (2021), no. 5, 800–810.
- [2] R. B. Ash. *Information theory*. Corrected reprint of the 1965 original. Dover Publications, Inc., New York, 1990. xii+339 pp.
- [3] R. Arratia, A. D. Barbour, and S. Tavaré. On random polynomials over finite fields, Math. Proc. Cambridge Philos. Soc., 114 (1993), pp. 347–368.
- [4] R. Arratia, A. D. Barbour, and S. Tavaré. Logarithmic Combinatorial Structures: A Probabilistic Approach, EMS Monogr. Math., EMS Publishing House, Zürich, 2003.
- [5] R. Arratia and S. Tavaré. The cycle structure of random permutations. Ann. Probab. 20(3) (1992), 1567–1591.
- [6] R. Arratia and S. Tavaré. *Independent process approximations for random combinatorial structures.*Adv. Math. 104 (1994), no. 1, 90–154.
- [7] J. Bamberg, S.P. Glasby, S. Harper, and C. E. Praeger. *Permutations with orders coprime to a given integer.*Electronic J. Combinatorics 27, 1, (2020), 14 pp.
- [8] L. Bary-Soroker and G. Kozma.*Irreducible polynomials of bounded height.*Duke Math. J. 169 (2020), no. 4, 579–598.
- [9] L. Bary-Soroker, G. Kozma and D. Koukoulopoulos. Irreducibility of random polynomials: general measures. preprint. arXiv:2007.14567.
- [10] R. Beals, C. R. Leedham-Green, A. C. Niemeyer, C. E. Praeger, and Á. Seress. *Permutations with restricted cycle structure and an algorithmic application.*Combin. Probab. Comput. 11, (5), (2002), 447–464.
- [11] N. G. de Bruijn. *The asymptotic behaviour of a function occurring in the theory of primes*. J. Indian Math. Soc. (N.S.) 15 (1951), 25–32.
- [12] P. J. Cameron and W. M. Kantor. Random permutations: some group-theoretic aspects. Combin. Probab. Comput., 2(3):257–262, 1993.
- [13] S. Chowla, I. N. Herstein, and W. K. Moore. On recursions connected with symmetric groups. I. Canad. J. Math., 3:328–334, 1951.
- [14] P. Diaconis, J. Fulman, and R. Guralnick. On fixed points of permutations. J. Algebraic Combin., 28(1):189–218, 2008.
- [15] K. Dickman. *On the Frequency of Numbers Containing Prime Factors of a Certain Relative Magnitude*. Arkiv för Mat., Astron. och Fys. 22A, 1–14, 1930.
- [16] J. Dixon. *Random sets which invariably generate the symmetric group*, Discrete Math. 105 (1992), 25–39.
- [17] S. Eberhard, K. Ford, and B. Green. Permutations fixing a k k -set. Int. Math. Res. Not. IMRN, (21):6713–6731, 2016.
- [18] S. Eberhard, K. Ford, and B. Green. *Invariable generation of the symmetric group.*Duke Math. J. 166 (2017), no. 8, 1573-1590.
- [19] S. Eberhard, K. Ford and D. Koukoulopoulos, *Permutations contained in transitive subgroups*, Discrete Analysis 2016: 12, 34 pages.
- [20] P. Erdős. Some remarks on number theory. Riveon Lematematika, 9:45–48, 1955. (Hebrew. English summary).
- [21] P. Erdős. An asymptotic inequality in the theory of numbers. Vestnik Leningrad. Univ., 15(13):41–49, 1960. (Russian).
- [22] P. Erdős and P. Turán. *On some problems of a statistical group-theory. I.*Z. Wahrscheinlichkeitstheorie und Verw. Gebiete 4 (1965), 175–186.
- [23] P. Erdős and P. Turán. *On some problems of a statistical group-theory. II*, Acta Math. Acad. Sci. Hungar. 18 (1967), 151–163;
- [24] P. Erdős and P. Turán. *On some problems of a statistical group-theory. III*, Acta Math. Acad. Sci. Hungar. 18 (1967), 309–320;
- [25] P. Erdős and P. Turán. *On some problems of a statistical group-theory. IV*, Acta Math. Acad. Sci. Hungar. 19 (1968), 413–435.
- [26] P. Erdős and P. Turán. *On some problems of a statistical group-theory. V*, Period. Math. Hungar. 1 (1971), no. 1, 5–13.
- [27] P. Erdős and P. Turán. *On some problems of a statistical group-theory. VI*, J. Indian Math. Soc. 34 (1971), no. 3-4, 175–192.
- [28] P. Erdős and P. Turán. *On some problems of a statistical group-theory. VII*, Period. Math. Hungar. 2 (1972), 149–163.
- [29] P. Flajolet and R. Sedgewick. *Analytic combinatorics*. Cambridge University Press, Cambridge, 2009. xiv+810 pp.
- [30] K. Ford. The distribution of integers with a divisor in a given interval. Ann. of Math. (2), 168(2):367–433, 2008.
- [31] K. Ford. Integers with a divisor in ( y, 2 ​ y] (y,2y]. In Anatomy of integers, volume 46 of CRM Proc. Lecture Notes, pages 65–80. Amer. Math. Soc., Providence, RI, 2008.
- [32] K. Ford. Joint Poisson distribution of prime factors in sets, Math. Proc. Cambridge Phil. Soc., to appear.
- [33] K. Ford, B. Green and D. Koukoulopoulos. *Equal sums in random sets and the concentration of divisors.*preprint, arXiv:1908.00378
- [34] K. Ford and H. Halberstam. The Brun-Hooley sieve. J. Number Theory, 81(2):335–350, 2000.
- [35] A. Gál and P. B. Miltersen, *The cell probe complexity of succinct data structures*, Proceedings 30th International Colloquium on Automata, Languages and Programming (ICALP), (2003), 332-344.
- [36] J. Galambos. *The sequences of prime divisors of integers.*Acta Arith. 31 (1976), no. 3, 213–218.
- [37] S. P. Glasby, C. E. Praeger and W. R. Unger. *Most permutations power to a cycle of small prime length*, Proc. Edinb. Math. Soc. (2) 64 (2021), no. 2, 234–246.
- [38] W. M. Y. Goh and E. Schmutz. *The expected order of a random permutation.*Bull. London Math. Soc. 23 (1991), no. 1, 34–42.
- [39] V. Gontcharoff. Du domaine de l’analyse combinatoire. Bull. Acad. Sci. URSS Sér. Math. [Izvestia Akad. Nauk SSSR], 8:3–48, 1944. (Russian). English translation: V. Gonĉarov, On the field of combinatory analysis. Amer. Math. Soc. Transl. (2) 19, 1962, 1–46.
- [40] A. Granville. Cycle lengths in a permutation are typically Poisson. Electron. J. Combin., 13(1):Research Paper 107, 23, 2006.
- [41] O. Gruder. *Zur Theorie der Zerlegung von Permutationen in Zyklen.*(German). Ark. Mat. 2 (1952), 385–414.
- [42] R. R. Hall and G. Tenenbaum. Divisors, volume 90 of Cambridge Tracts in Mathematics. Cambridge University Press, Cambridge, 1988.
- [43] G. H. Hardy and S. Ramanujan. *The normal number of prime factors of a number n n*, Quart. J. Math. Oxford 48, 76–92.
- [44] A. Hildebrand. *On the number of positive integers ⩽ x \leqslant x and free of prime factors > y >y*. J. Number Theory 22 (1986), no. 3, 289–307.
- [45] C. Jordan. *Sur la limite de transitivité des groupes non alternés*, Bull. Soc. Math. France 1 (1872/73), 40–71. (French)
- [46] D. E. Knuth and L. Trabb Pardo. *Analysis of a simple factorization algorithm*. Theoret. Comput. Sci. 3 (1976/77), no. 3, 321–348.
- [47] V. P. Kolchin and V. P. Chistyakov. *On the cyclic structure of random permutations.*(Russian) Mat. Zametki 18 (1975), no. 6, 929–938.
- [48] D. Koukoulopoulos. *The distribution of prime numbers*, Amer. Math. Soc., Graduate Studies in Math. 203, 2019.
- [49] J. Lagarias. *Euler’s constant: Euler’s work and modern developments*. Bull. Amer. Math. Soc. (N.S.) 50 (2013), no. 4, 527–628.
- [50] E. Landau. *Über die Maximalordnung der Permutationen gegebenen Grades [On the maximal order of permutations of given degree]*, Arch. Math. Phys. Ser. 3, vol. 5, 1903. (German)
- [51] E. Landau. *Handbuch der Lehre von der Verteilung der Primzahlen*, Chelsea, 1951. Reprint of the 1909 original. (German)
- [52] S. P. Lloyd and L. A. Shepp. *Ordered cycle lengths in a random permutation*, Trans. Amer. Math. Soc. 121 (1966), 340–357.
- [53] T. Łuczak and L. Pyber. On random generation of the symmetric group. Combin. Probab. Comput., 2(4):505–512, 1993.
- [54] E. Manstavičius. Iterated logarithm laws and the cycle lengths of a random permutation. In Mathematics and computer science. III, Trends Math., pages 39–47. Birkhäuser, Basel, 2004.
- [55] E. Manstavičius and R. Petuchovas. *Local probabilities for random permutations without long cycles.*Electron. J. Combin. 23 (2016), no. 1, Paper 1.58, 25 pp.
- [56] E. Manstavičius and R. Petuchovas. *Local probabilities and total variation distance for random permutations.*Ramanujan J. 43 (2017), no. 3, 679–696.
- [57] J.-P. Massias, *Majoration explicite de l’ordre maximum d’un élément du groupe symétrique*, Ann. Fac. Sci. Toulouse Math. (5) 6 (1984), no. 3-4, pp. 269–281. (French)
- [58] I. Mező and C. Wang. *Some limit theorems with respect to constrained permutations and partitions.*Monatsh. Math. 182 (2017), no. 1, 155–164.
- [59] E. McKemmie. *Invariable generation of finite classical groups*, J. Algebra 585 (2021), 592–615.
- [60] L. Moser and M. Wyman. *Asymptotic development of the Stirling numbers of the first kind.*J. London Math. Soc. 33 (1958), 133–146.
- [61] J.-L. Nicolas. *Sur l’ordre maximum d’un élément dans le groupe S n S_{n} des permutations*, Acta Arithmetica 14 (1968), 315–332. (French)
- [62] A. C. Niemeyer and C. E. Praeger. *On the frequency of permutations containing a long cycle.*J. Algebra 300 (2006), no. 1, 289–304.
- [63] A. C. Niemeyer and C. E. Praeger. *On the proportion of permutations of order a multiple of the degree.*J. London Math. Soc. (2) 76 (2007), no. 3, 622–632.
- [64] K. K. Norton. *On the number of restricted prime factors of an integer*, Illinois J. Math. 20, 681–705.
- [65] R. Petuchovas. Asymptotic analysis of the cyclic structure of permutations. PhD thesis, Vilnius University, 2016. arXiv:1611.02934.
- [66] R. Petuchovas. Asymptotic estimates for the number of permutations without short cycles. Australas. J. Combin., 72:1–18, 2018.
- [67] R. Pemantle, Y. Peres, and I. Rivin. Four random permutations conjugated by an adversary generate 𝒮 n \mathcal{S}_{n} with high probability. Random Structures Algorithms, 49(3):409–428, 2016.
- [68] Z. Rudnick. *On locally repeated values of arithmetic functions over 𝔽 q ​ [T] \mathbb{F}_{q}[T].*With an appendix by Ron Peled. Q. J. Math. 70 (2019), no. 2, 451–472.
- [69] A. Seress. *Permutation group algorithms.*Cambridge Tracts in Mathematics, 152. Cambridge University Press, Cambridge, 2003.
- [70] G. Tenenbaum. Introduction to analytic and probabilistic number theory, volume 163 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, third edition, 2015. English. Translated from the 2008 French edition by Patrick D. F. Ion.
- [71] A. Vershik and A. Schmidt, *Limit measures that arise in the asymptotics of symmetric groups, I.*Theoret. Veroyatn. i Prim. 22 (1977), 72–88. (Russian)
- [72] G. A. Watterson, *The sampling theory of selectively neutral alleles.*Advances in Appl. Probability 6 (1974), 463–488.
- [73] A. Weingartner. *On the degrees of polynomial divisors over finite fields.*Math. Proc. Cambridge Philos. Soc. 161 (2016), no. 3, 469–487.

† † daj-authors: † † daj-authorinfo: Kevin Ford
Department of Mathematics
University of Illinois at Urbana-Champaign
1409 West Green Street
Urbana, IL 61801, USA
ford@math.uiuc.edu
[https://faculty.math.illinois.edu/~ford/][1]

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: https://faculty.math.illinois.edu/~ford/
[2]: /html/2104.12018
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/2104.12019
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2104.12019
[8]: https://arxiv.org/abs/2104.12019
[9]: /html/2104.12020
