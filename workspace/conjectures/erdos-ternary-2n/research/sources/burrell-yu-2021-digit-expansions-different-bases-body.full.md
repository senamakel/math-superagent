<!-- source: https://arxiv.org/html/1905.00832v3 | converted from HTML -->

Digit expansions of numbers in different bases

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1905.00832v3 [math.NT] 23 Apr 2021

# Digit expansions of numbers in different bases

Stuart A. Burrell Address: Stuart A. Burrell
School of Mathematics & Statistics
University of St Andrews
St Andrews
KY16 9SS
UK Current address: Email address: [sb235@st-andrews.ac.uk][3] and Han Yu Address: Han Yu
Department of Pure Mathematics and Mathematical Statistics
University of Cambridge
CB3 0WB
UK Current address: Email address: [hy351@maths.cam.ac.uk][4]

Date: August 11, 2026

###### Abstract.

A folklore conjecture in number theory states that the only integers whose expansions in base 3, 4 3,4 and 5 5 contain solely binary digits are 0, 1 0,1 and 82000 82000. In this paper, we present the first progress on this conjecture. Furthermore, we investigate the density of the integers containing only binary digits in their base 3 3 or 4 4 expansion, whereon an exciting transition in behaviour is observed. Our methods shed light on the reasons for this, and relate to several well-known questions, such as Graham’s problem and a related conjecture of Pomerance. Finally, we generalise this setting and prove that the set of numbers in [0, 1] [0,1] who do not contain some digit in their b b -expansion for all b ≥ 3 b\geq 3 has zero Hausdorff dimension.

###### Key words and phrases:

digit expansion, Graham’s problem, Schanuel’s conjecture

###### 2010 Mathematics Subject Classification

Primary: 11K55, 28A50, 28A80, 28D05, 37C45.

## 1. Introduction and Statement of Results

The expansion of numbers in various bases gives rise to a number of notorious problems. Of these, the most famous is the Erdős ternary problem [4], which conjectures that there are only finitely many integers n n such that the ternary expansion of 2 n 2^{n} does not contain the digit 1 1, see [3, 10] for some recent developments. Other important related works include [25]. In this field, an intriguing folklore conjecture concerning the integer sequence [16] states the following.

###### Conjecture 1.1.

0, 1, 82000 0,1,82000 are the only integers whose base 3, 4 3,4 and 5 5 expansions contain solely the digits 0, 1 0,1.

As well as attracting specialist audiences, this problem has been popularised in [13] and, so far, numerical computations have not found any counter-examples up to 2 65520 2^{65520}. To our knowledge, the following is the first progress on this conjecture.

###### Theorem 1.2.

For each ϵ > 0 \epsilon>0, there is a constant C ϵ > 0 C_{\epsilon}>0 such that

 | #⁡ { k ∈ [1, n]: the base 4 and 5 expansions of k contain only the digits 0, 1 } ≤ C ϵ ​ n ϵ. \#\{k\in[1,n]:\text{ the base $4$ and $5$ expansions of $k$ contain only the digits $0,1$}\}\leq C_{\epsilon}n^{\epsilon}. |  |

Of course, the base 3 3 requirement may immediately be added to correspond directly with the conjecture.

###### Corollary 1.3.

For each ϵ > 0 \epsilon>0, there is a constant C ϵ > 0 C_{\epsilon}>0 such that

 | #⁡ { k ∈ [1, n]: the base 3, 4 and 5 expansions of k contain only the digits 0, 1 } ≤ C ϵ ​ n ϵ. \#\{k\in[1,n]:\text{ the base $3,4$ and $5$ expansions of $k$ contain only the digits $0,1$}\}\leq C_{\epsilon}n^{\epsilon}. |  |

Our methods may be used to show other similar results in a range of contexts. For example, one can show that an O ⁡ ( n ϵ) O(n^{\epsilon}) estimate holds if we consider the set of numbers whose base 3 3 and 7 7 expansions contain only binary digits. Numerical computations indicate that the largest such number which is smaller than 7 3841 7^{3841} is between 7 43 7^{43} and 7 44 7^{44}. Other candidates for the application of our arguments include the integer sequences [17, 18, 19, 20] from the OEIS [14].

One may also consider those integers whose base 3 3 and 4 4 expansions contain only binary digits. This corresponds to the integer sequence [15], denoted 𝒮 \mathcal{S}, defined by

 | 𝒮 ⁡ ( n):= #⁡ { k ∈ [4 n, 4 n + 1 − 1]: the expansions of k contains only 0, 1 in bases 3, 4 }. \mathcal{S}(n):=\#\{k\in[4^{n},4^{n+1}-1]:\text{ the expansions of $k$ contains only $0,1$ in bases $3,4$}\}. |  |

The first few terms of this sequence are 2, 1, 0, 3, 6, 3, 0, 5, 12 2,1,0,3,6,3,0,5,12 and 11 11. Numerical analysis of 𝒮 \mathcal{S}, see Figure 1, suggests that

 | lim sup n → ∞ log ⁡ 𝒮 ⁡ ( n) n ​ log ⁡ 4 = log ⁡ 2 log ⁡ 3 − 1 2. \limsup_{n\to\infty}\frac{\log\mathcal{S}(n)}{n\log 4}=\frac{\log 2}{\log 3}-\frac{1}{2}. |  |

In stark contrast to the setting of Theorem 1.2, there appear to be infinitely many n n such that 𝒮 ⁡ ( n) > 0 \mathcal{S}(n)>0, and the proof of Theorem 1.2 sheds some light on why the base 5 5 requirement induces such a dramatic transition. In addition, one may wonder if there are infinitely many n n with 𝒮 ⁡ ( n) = 0 \mathcal{S}(n)=0, and our next result, Theorem 1.4, confirms this fact.

###### Theorem 1.4.

For each ϵ > 0 \epsilon>0, there is a constant C ϵ > 0 C_{\epsilon}>0 such that

 | 𝒮 ⁡ ( n) ≤ C ϵ ​ 4 n ⁡ ( log ⁡ 2 / log ⁡ 3 − 0.5 + ϵ). \mathcal{S}(n)\leq C_{\epsilon}4^{n(\log 2/\log 3-0.5+\epsilon)}. |  |

Moreover,

 | lim inf n → ∞ #⁡ { n ∈ ℕ: 𝒮 ⁡ ( n) ∩ [3 n, 3 n + 1] = ∅ } n ≥ log ( 2.25) / log 9 ≈ 0.36907, \liminf\limits_{n\rightarrow\infty}\frac{\#\{n\in\mathbb{N}:\mathcal{S}(n)\cap[3^{n},3^{n+1}]=\emptyset\}}{n}\geq\log(2.25)/\log 9\approx 0.36907, |  |

and if n n is such that 9 { n ​ log ⁡ 4 / log ⁡ 9 } ∈ ( 1.5, 2.25) ∪ ( 4.5, 6.75) 9^{\{n\log 4/\log 9\}}\in(1.5,2.25)\cup(4.5,6.75), then n ∈ { n ∈ ℕ: 𝒮 ⁡ ( n) ∩ [3 n, 3 n + 1] = ∅ }. n\in\{n\in\mathbb{N}:\mathcal{S}(n)\cap[3^{n},3^{n+1}]=\emptyset\}.

From the proof of this theorem it may be deduced that the converse of the last statement does not hold, a fact further discussed in Section 6.

Figure 1. A plot of log ⁡ 𝒮 ⁡ ( n) / log ⁡ 4 n \log\mathcal{S}(n)/\log 4^{n} for n ∈ { 1, …, 118 } n\in\{1,\dots,118\}. The horizontal line is { y = log 2 / log 3 − 0.5 } \{y=\log 2/\log 3-0.5\} and the lower dots indicate where 𝒮 ⁡ ( n) = 0 \mathcal{S}(n)=0. According to this data, the density of 0 0 in this range is approximately 0.4576271. 0.4576271.

The third focus of this paper concerns a generalisation of the above setting, by introducing the notion of *digit-special*numbers. We say real number x ≥ 0 x\geq 0 is digit-special if the expansion of x x in base b b does not contain at least one digit from 0, 1, …, b − 1 0,1,\dots,b-1 for all b ≥ 3 b\geq 3. Our work in this broader direction relies on Schanuel’s conjecture [1], which we state below for convenience.

###### Conjecture 1.5 (Schanuel).

Let x 1, …, x n x_{1},\dots,x_{n} be ℚ \mathbb{Q} -linearly independent complex numbers, the transcendence degree of ℚ ⁡ ( x 1, …, x n, e x 1, …, e x n) \mathbb{Q}(x_{1},\dots,x_{n},e^{x_{1}},\dots,e^{x_{n}}) is at least n. n.

Our primary result on digit-special numbers is the following, which, as an initial contribution, we hope will provoke further investigations into this rich topic.

###### Theorem 1.6.

Assume Schanuel’s conjecture. For each ϵ > 0 \epsilon>0, there is a constant C ϵ > 0 C_{\epsilon}>0 such that for all N ≥ 1 N\geq 1, the number of digit-special integers smaller than N N is at most C ϵ ​ N ϵ. C_{\epsilon}N^{\epsilon}. In addition, the Hausdorff dimension of the set of digit special numbers intersecting [0, 1] [0,1] is zero.

These results also find connections to a famous question asked by Graham and a related conjecture of Pomerance.

###### Question 1.7 (Graham’s $ 1000 \$1000 problem 1 1 1 According to [21], Graham offers $ 1000 \$1000 to the first person with a solution.).

Are there infinitely many integers n ≥ 1 n\geq 1 such that the binomial coefficient ( 2 ​ n n) \binom{2n}{n} is coprime with 105 = 3 × 5 × 7 ​? 105=3\times 5\times 7?

This problem is currently open but has seen significant attention. Notably, in 1975, Erdős, Graham, Ruzsa and Straus showed the following result.

###### Theorem 1.8 (Two prime factor theorem [5]).

Let p, q p,q be integers greater than 1 1. If A, B A,B are two positive integers satisfying

 | A p − 1 + B q − 1 ≥ 1, \frac{A}{p-1}+\frac{B}{q-1}\geq 1, |  |

then there exist infinitely many integers whose base p p expansion contains only digits ≤ A \leq A and base q q expansion contains only digits ≤ B. \leq B.

Later it will be clear that the following condition seems to be more canonical for this type of problem:

 | log ⁡ ( A + 1) log ⁡ p + log ⁡ ( B + 1) log ⁡ q ≥ 1, \frac{\log(A+1)}{\log p}+\frac{\log(B+1)}{\log q}\geq 1, |  |

although we have not yet proved an analogous result with this condition. The connection between prime factors of binomial coefficients and digit expansions is due to Kummer [9], who proved that a prime number does not divide ( 2 ​ n n) \binom{2n}{n} if and only if the p p -ary expansion of n n contains only digits less than or equal to ( p − 1) / 2 (p-1)/2. Thus by the two prime factor theorem of Erdős, Graham, Ruzsa and Straus we see that for any two different odd prime numbers p, q, p,q, there are infinitely many integers n n such that ( 2 ​ n n) \binom{2n}{n} is coprime with p p and q q.

In approaching Graham’s problem, it is natural to first consider alternative or related forms. In [23, Section 4], Pomerance gave a heuristic argument that leads to the following conjecture.

###### Conjecture 1.9.

Let N N be an integer. Denote G ⁡ ( N) G(N) to be the number of positive integers n ≤ N n\leq N such that ( 2 ​ n n) \binom{2n}{n} is coprime with 105 105. Then

 | N 0.025 ≤ G ⁡ ( N) ≤ N 0.026 N^{0.025}\leq G(N)\leq N^{0.026} |  |

for all large enough N. N.

Moreover, in [23, page 639] Pomerance asks

 | “…why would the base- p p expansion of n n have nothing to do with the base- q q |  |

 | expansion when p p and q q are different primes?" |  |

We partially answer this question and Conjecture 1.9 in Theorem 1.10, the proof of which may be found in Section 6. For now, this theorem is dependent upon Schanuel’s conjecture, due to the important consequence that

 | 1, log ⁡ 3 / log ⁡ 5, log ⁡ 3 / log ⁡ 7 1,\log 3/\log 5,\log 3/\log 7 |  |

are then ℚ \mathbb{Q} -linearly independent.

###### Theorem 1.10.

Let N N be an integer and G ⁡ ( N) G(N) denote the number of positive integers n ≤ N n\leq N such that ( 2 ​ n n) \binom{2n}{n} is coprime with any choice of three different prime numbers. Then we have

 | G ⁡ ( N) ≤ N 0.073 G(N)\leq N^{0.073} |  |

for all large enough N. N. Furthermore, assuming Schanuel’s conjecture, we have

 | G ⁡ ( N) ≤ N 0.026 G(N)\leq N^{0.026} |  |

for all large enough N. N.

It is likely that one can prove the necessary ℚ \mathbb{Q} -linear independence directly without having to prove the more general Schanuel’s conjecture. We are able to make some progress along these lines and in Section 3 show the following.

###### Theorem 1.11.

The triple

 | 1, log ⁡ 3 / log ⁡ 5, log ⁡ 3 / log ⁡ n 1,\log 3/\log 5,\log 3/\log n |  |

is ℚ \mathbb{Q} -linearly independent for at least one n ∈ { 7, 11, 13 } n\in\{7,11,13\}.

###### Remark 1.12.

Theorem 1.11 may easily be generalized to show that for each choice of three primes numbers p 1, p 2, p 3 ≥ 7, p_{1},p_{2},p_{3}\geq 7, at least one of them, say, n n, is such that

 | 1, log ⁡ 3 / log ⁡ 5, log ⁡ 3 / log ⁡ n 1,\log 3/\log 5,\log 3/\log n |  |

are ℚ \mathbb{Q} -linearly independent.

There are yet more interesting stories in this direction and we postpone further discussion until Section 6.

## 2. Preliminaries

In this section we introduce the required definitions and results from existing literature.

### 2.1. Densities of integer sequences

The notion of density describes the size of subsets of ℕ \mathbb{N}. Let W ⊂ ℕ W\subset\mathbb{N} be a sequence of natural numbers and define

 | #n ​ W = #⁡ { i ∈ [1, n]: i ∈ W }. \#_{n}W=\#\{i\in[1,n]:i\in W\}. |  |

Then, the upper natural density of W W is

 | d ¯ ​ ( W) = lim sup n → ∞ #n ​ W n, \overline{d}(W)=\limsup_{n\to\infty}\frac{\#_{n}W}{n}, |  |

and the lower natural density is given by

 | d ¯ ​ ( W) = lim inf n → ∞ #n ​ W n. \underline{d}(W)=\liminf_{n\to\infty}\frac{\#_{n}W}{n}. |  |

If these two numbers coincide we call the common value, denoted d ⁡ ( W) d(W), the natural density of W W.

### 2.2. Dimensions

Dimension is another standard way of quantifying the size of a set. There are numerous notions, but our focus is the Hausdorff and box dimensions. For an in-depth introduction, see [6, Chapters 2,3] and [12, Chapters 4,5].

#### 2.2.1. Hausdorff dimension

For all δ > 0 \delta>0 and s > 0 s>0, define the δ \delta -approximate s s -dimensional Hausdorff measure of a set F ⊆ ℝ n F\subseteq\mathbb{R}^{n} by

 | ℋ δ s ( F) = inf { ∑ i = 1 ∞ diam ( U i) s: ⋃ i U i ⊃ F, diam ( U i) ≤ δ }, \mathcal{H}^{s}_{\delta}(F)=\inf\left\{\sum_{i=1}^{\infty}\mathrm{diam}(U_{i})^{s}:\bigcup_{i}U_{i}\supset F,\mathrm{diam}(U_{i})\leq\delta\right\}, |  |

and the s s -dimensional Hausdorff measure of F F by

 | ℋ s ​ ( F) = lim δ → 0 ℋ δ s ​ ( F). \mathcal{H}^{s}(F)=\lim_{\delta\to 0}\mathcal{H}^{s}_{\delta}(F). |  |

The Hausdorff dimension of F F, denoted dim H F \dim_{\mathrm{H}}F, is then given by

 | dim H F = inf { s ≥ 0: ℋ s ​ ( F) = 0 } = sup { s ≥ 0: ℋ s ​ ( F) = ∞ }. \dim_{\mathrm{H}}F=\inf\{s\geq 0:\mathcal{H}^{s}(F)=0\}=\sup\{s\geq 0:\mathcal{H}^{s}(F)=\infty\}. |  |

#### 2.2.2. Box dimensions

Let N ⁡ ( F, r) N(F,r) denote the smallest number of cubes of side length r > 0 r>0 required to cover F ∈ ℝ n F\in\mathbb{R}^{n}. The upper box dimension of a bounded set F F is

 | dim ¯ B ​ F = lim sup r → 0 ( − log ⁡ N ⁡ ( F, r) log ⁡ r), \overline{\dim}_{\mathrm{B}}F=\limsup_{r\to 0}\left(-\frac{\log N(F,r)}{\log r}\right), |  |

and the lower box dimension of F F is

 | dim ¯ B ​ F = lim inf r → 0 ( − log ⁡ N ⁡ ( F, r) log ⁡ r). \underline{\dim}_{\mathrm{B}}F=\liminf_{r\to 0}\left(-\frac{\log N(F,r)}{\log r}\right). |  |

If dim ¯ B ​ F = dim ¯ B ​ F \underline{\dim}_{\textup{B}}F=\overline{\dim}_{\textup{B}}F, then we call the common value, denoted dim B F \dim_{\textup{B}}F, the box dimension of F F. It is easy to see that for all F ⊆ ℝ n F\subseteq\mathbb{R}^{n},

 | dim H F ≤ dim ¯ B ​ F ≤ dim ¯ B ​ F. \dim_{\textup{H}}F\leq\underline{\dim}_{\textup{B}}F\leq\overline{\dim}_{\textup{B}}F. |  |

### 2.3. Invariant sets

Given an integer k ≥ 2 k\geq 2, let A k A_{k} denote an arbitrary closed × k mod 1 \times k\mod 1 invariant subset of [0, 1] [0,1]. That is to say, a ∈ A k a\in A_{k} implies { k ​ a } ∈ A k \{ka\}\in A_{k} for all a ∈ A k a\in A_{k}, where { x } \{x\} is the fractional part of x x. We say that A k A_{k} is strictly invariant if a ∈ A k a\in A_{k} if and only if { k ​ a } ∈ A k \{ka\}\in A_{k}. For each closed × k mod 1 \times k\mod 1 invariant set A k A_{k}, it is known that dim H A k = dim ¯ B ​ A k \dim_{\mathrm{H}}A_{k}=\overline{\dim}_{\mathrm{B}}A_{k} [8, Theorem 5.1]. In particular, for any integers k, l ≥ 2 k,l\geq 2, and closed × k, l mod 1 \times k,l\mod 1 invariant sets A k, A l A_{k},A_{l}, we have dim H A k × A l = dim ¯ B ​ A k × A l. \dim_{\mathrm{H}}A_{k}\times A_{l}=\overline{\dim}_{\mathrm{B}}A_{k}\times A_{l}.

### 2.4. Equidistribution

Let T T be a compact metric space and μ ∈ 𝒫 ⁡ ( T) \mu\in\mathcal{P}(T) be a Borel probability measure. Let X = { x n } n ≥ 1 X=\{x_{n}\}_{n\geq 1} be a sequence in T. T. We say that X X equidistributes in T T with respect to μ \mu if for each closed metric ball B ⊂ T B\subset T,

 | lim N → ∞ 1 N ​ ∑ n = 1 N 𝟙 B ​ ( x n) = μ ⁡ ( B). \lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^{N}\mathbbm{1}_{B}(x_{n})=\mu(B). |  |

Suppose that X ′ = { x i k } k ≥ 1 X^{\prime}=\{x_{i_{k}}\}_{k\geq 1} is a subsequence of X X such that { i k } k ≥ 1 \{i_{k}\}_{k\geq 1} has positive upper natural density ρ > 0 \rho>0. X ′ X^{\prime} might not be equidistributed, but we may still consider the μ \mu measure of its closure in T T in some special cases. For example, it is not too hard to show that if T T is the n n -dimensional torus and μ \mu denotes Lebesgue measure, then μ ⁡ ( X ′ ¯) ≥ ρ \mu(\overline{X^{\prime}})\geq\rho.

### 2.5. Dipole directions

Let A ⊂ ℝ n A\subset\mathbb{R}^{n} be compact and consider

 | D D ( A) = { ( x − y) / | x − y |: x, y ∈ A, | x − y | > 0.001 } ⊂ S n − 1. DD(A)=\{(x-y)/|x-y|:x,y\in A,|x-y|>0.001\}\subset S^{n-1}. |  |

From [27, Section 4.3], we know that dim ¯ B ​ A ≥ 0.5 ​ dim ¯ B ​ D ​ D ​ ( A) \overline{\dim}_{\mathrm{B}}A\geq 0.5\overline{\dim}_{\mathrm{B}}DD(A). Moreover, if x ∈ ℝ n x\in\mathbb{R}^{n} is a fixed point, then

 | D D ( A, x) = { ( x − y) / | x − y |: y ∈ A, | x − y | > 0.001 } ⊂ S n − 1 DD(A,x)=\{(x-y)/|x-y|:y\in A,|x-y|>0.001\}\subset S^{n-1} |  |

has dimension dim ¯ B ​ D ​ D ​ ( A, x) ≤ dim ¯ B ​ A. \overline{\dim}_{\mathrm{B}}DD(A,x)\leq\overline{\dim}_{\mathrm{B}}A.

### 2.6. Intersections of invariant sets

2 2 2 As a side note, we mention that the result we discuss here actually partially resolves the quoted question of Pomerance in Section 1.

The methods we use in this paper rely heavily on the following result from [27], which is a uniform and higher dimensional version of a deep result concerning the Furstenberg problem [7] proven in [24] and [26].

Let k ≥ 2 k\geq 2 be an integer and A p 1, …, A p k A_{p_{1}},\dots,A_{p_{k}} be closed invariant subsets of [0, 1] [0,1] with respect to × p 1 mod 1, × p 2 mod 1, …, × p k mod 1 \times p_{1}\mod 1,\times p_{2}\mod 1,\dots,\times p_{k}\mod 1, respectively. Assume that log ⁡ p 1 / log ⁡ p i \log p_{1}/\log p_{i} for i ∈ { 2, …, k } i\in\{2,\dots,k\} are irrational numbers which are linearly independent over ℚ \mathbb{Q}. If

 | ∑ i = 1 k dim H A p i < k − 1, \sum_{i=1}^{k}\dim_{\mathrm{H}}A_{p_{i}}<k-1, |  |

then for each 2 ​ k 2k -tuple u 1, …, u k, v 1, …, v k u_{1},\dots,u_{k},v_{1},\dots,v_{k} of non-zero real numbers we have

 | dim ¯ B ∩ i = 1 k ( u i A p i + v i) = 0 \overline{\dim}_{\mathrm{B}}\cap_{i=1}^{k}(u_{i}A_{p_{i}}+v_{i})=0 |  |

by [27]. Moreover, for δ > 0 \delta>0, if δ < | u i | < δ − 1 \delta<|u_{i}|<\delta^{-1} for each i ∈ { 1, …, k } i\in\{1,\dots,k\}, then for each ϵ > 0 \epsilon>0 there is an integer N ϵ > 0 N_{\epsilon}>0 such that

 | N ( ∩ i = 1 k ( u i A p i + v i), 2 − N) ≤ N ϵ N(\cap_{i=1}^{k}(u_{i}A_{p_{i}}+v_{i}),2^{-N})\leq N^{\epsilon} |  |

for all N ≥ N ϵ N\geq N_{\epsilon}, where N ⁡ ( …) N(\dots) denotes the box covering number (see Section 2.2.2 for details). Note that the choice of N ϵ N_{\epsilon} does not depend on u i, v i u_{i},v_{i}. For most of the results in this paper, we do not need the full strength of the above result. In fact, our main results (Theorems 1.2, 1.4) only rely on the case k = 2. k=2. In this case, the above result is [27, Corollary 1.2]. Alternatively, one can apply [24, Theorem 1.11, Lemma 1.8]. For k ≥ 3, k\geq 3, results in [24] cannot be used here. Nonetheless, the result follows by modifying the proof of [27, Theorem 10.1] as described in the discussions found in [27, Section 12.1].

## 3. Schanuel’s conjecture and proof of Theorem 1.11

In this section, we use Schanuel’s conjecture to show ℚ \mathbb{Q} -linealy independence among ratios of integer logarithms.

###### Lemma 3.1.

Assume Schanuel’s conjecture. Let k ≥ 3 k\geq 3 be an integer. If p 1, …, p k p_{1},\dots,p_{k} are integers such that

 | p 1 n 1 ​ … ​ p k n k = 1 ( n i ∈ ℤ) p^{n_{1}}_{1}\dots p^{n_{k}}_{k}=1\,\,\,\,\,\,(n_{i}\in\mathbb{Z}) |  |

implies n 1 = ⋯ = n k = 0 n_{1}=\dots=n_{k}=0, then

 | 1, log ⁡ p 1 log ⁡ p 2, …, log ⁡ p 1 log ⁡ p k 1,\frac{\log p_{1}}{\log p_{2}},\dots,\frac{\log p_{1}}{\log p_{k}} |  |

are ℚ \mathbb{Q} -linearly independent.

###### Remark 3.2.

For k = 2 k=2, the conclusion of Lemma 3.1 holds without requiring Schanuel’s conjecture.

###### Proof.

The required ℚ \mathbb{Q} -linearly independence follows if

 | Λ ′ = ( ∏ i = 1 k log ⁡ p i log ⁡ p 1, …, ∏ i = 1 k log ⁡ p i log ⁡ p k) \Lambda^{\prime}=\left(\frac{\prod_{i=1}^{k}\log p_{i}}{\log p_{1}},\dots,\frac{\prod_{i=1}^{k}\log p_{i}}{\log p_{k}}\right) |  |

are ℚ \mathbb{Q} -linearly independent. Considering Conjecture 1.5 in the case when e x 1, …, e x k e^{x_{1}},\dots,e^{x_{k}} are integers, the conjecture reduces to saying that x 1, …, x k x_{1},\dots,x_{k} are algebraically independent over ℚ. \mathbb{Q}. We want to apply this conclusion with x 1 = log ⁡ p 1, …, x k = log ⁡ p k. x_{1}=\log p_{1},\dots,x_{k}=\log p_{k}. Now if if 1, log ⁡ p 1, …, log ⁡ p k 1,\log p_{1},\dots,\log p_{k} are ℚ \mathbb{Q} -linearly independent, then we meet the conditions of Conjecture 1.5 and can apply the aforementioned conclusion. This says that log ⁡ p 1, …, log ⁡ p k \log p_{1},\dots,\log p_{k} are algebraically independent. Suppose that Λ ′ \Lambda^{\prime} is not ℚ \mathbb{Q} -linear independent, then we have

 | ∑ j = 1 k c j ​ log ⁡ p j = c ​ ∏ i = 1 k log ⁡ p i \sum_{j=1}^{k}c_{j}\log p_{j}=c\prod_{i=1}^{k}\log p_{i} |  |

for some integers c 1, …, c k c_{1},\dots,c_{k} and c. c. This contradicts the algebraic independence of log ⁡ p 1, \log p_{1}, …, \dots, log ⁡ p k. \log p_{k}. This implies that Λ ′ \Lambda^{\prime} is indeed ℚ \mathbb{Q} -linearly independent if 1, log ⁡ p 1, …, log ⁡ p k 1,\log p_{1},\dots,\log p_{k} are ℚ \mathbb{Q} -linearly independent. ∎

To prove Theorem 1.11, first recall [11, Theorem 1, Chapter 2].

###### Theorem 3.3 (Six Exponentials Theorem).

Let ( x 1, x 2, x 3) (x_{1},x_{2},x_{3}) and ( y 1, y 2) (y_{1},y_{2}) be a ℚ \mathbb{Q} -linearly independent triple and pair of complex numbers, respectively. There exists a pair ( i, j) ∈ { 1, 2, 3 } × { 1, 2 } (i,j)\in\{1,2,3\}\times\{1,2\} such that

 | e x i ​ y j e^{x_{i}y_{j}} |  |

is transcendental over ℚ. \mathbb{Q}.

###### Proof of Theorem 1.11.

Applying Theorem 3.3 with

 | ( x 1, x 2, x 3) = ( log ⁡ 7 / log ⁡ 5, log ⁡ 11 / log ⁡ 5, log ⁡ 13 / log ⁡ 5) (x_{1},x_{2},x_{3})=(\log 7/\log 5,\log 11/\log 5,\log 13/\log 5) |  |

and

 | ( y 1, y 2) = ( log ⁡ 3, log ⁡ 5), (y_{1},y_{2})=(\log 3,\log 5), |  |

we see that at least one of

 | exp ( log 3 log 7 / log 5), exp ( log 3 log 11 / log 5), exp ( log 3 log 13 / log 5). \exp(\log 3\log 7/\log 5),\exp(\log 3\log 11/\log 5),\exp(\log 3\log 13/\log 5). |  |

is not algebraic over ℚ. \mathbb{Q}. Suppose now that a, b, c ≥ 2 a,b,c\geq 2 are integers, log ⁡ b / log ⁡ a ∉ ℚ \log b/\log a\notin\mathbb{Q} and exp ⁡ ( log ⁡ a ​ log ⁡ b / log ⁡ c) \exp(\log a\log b/\log c) is not algebraic over ℚ. \mathbb{Q}. Then integer solutions ( k 1, k 2, k 3) (k_{1},k_{2},k_{3}) to the following equation

 | k 1 ​ log ⁡ a ​ log ​ b + k 2 ​ log ​ a ​ log ​ c + k 3 ​ log ​ b ​ log ​ c = 0 k_{1}\log a\log b+k_{2}\log a\log c+k_{3}\log b\log c=0 |  |

must have k 1 = 0 k_{1}=0, for otherwise

 | log ⁡ a ​ log ⁡ b log ⁡ c + k 2 k 1 ​ log ⁡ a + k 3 k 1 ​ log ⁡ b = 0 \frac{\log a\log b}{\log c}+\frac{k_{2}}{k_{1}}\log a+\frac{k_{3}}{k_{1}}\log b=0 |  |

and so exp ⁡ ( log ⁡ a ​ log ⁡ b / log ⁡ c) = a k 2 / k 1 ​ b k 3 / k 1 \exp(\log a\log b/\log c)=a^{k_{2}/k_{1}}b^{k_{3}/k_{1}} which is algebraic. However, if k 1 = 0, k_{1}=0, then k 2 = k 3 = 0 k_{2}=k_{3}=0 or else log ⁡ b / log ⁡ a ∈ ℚ. \log b/\log a\in\mathbb{Q}. Hence

 | 1, log ⁡ a log ⁡ c, log ⁡ a log ⁡ b 1,\frac{\log a}{\log c},\frac{\log a}{\log b} |  |

are ℚ \mathbb{Q} -linearly independent. Therefore, Theorem 3.3 implies that at least one of the triples

 | ( 3, 5, 7), ( 3, 5, 11), ( 3, 5, 13), (3,5,7),(3,5,11),(3,5,13), |  |

say ( a, b, c) (a,b,c), is such that

 | 1, log ⁡ a log ⁡ b, log ⁡ a log ⁡ c 1,\frac{\log a}{\log b},\frac{\log a}{\log c} |  |

is ℚ \mathbb{Q} -linearly independent. This proves Theorem 1.11.∎

## 4. Digit-special numbers

It is natural to begin with the more general case of digit-special numbers, and then specialise to the settings of Theorem 1.2 and Theorem 1.4. As such, in this section we present the proof of Theorem 1.6, beginning with two lemmas that develop the majority of the new machinery required. In what follows, we say that p 1, …, p k p_{1},\dots,p_{k} are strongly multiplicatively independent if

 | 1, log ⁡ p 1 / log ⁡ p 2, …, log ⁡ p 1 / log ⁡ p k 1,\log p_{1}/\log p_{2},\dots,\log p_{1}/\log p_{k} |  |

are linearly independent over the field of rational numbers. From Lemma 3.1 and assuming Schanuel’s conjecture, this is the case when

 | 1, log ⁡ p 1, …, log ⁡ p k 1,\log p_{1},\dots,\log p_{k} |  |

are ℚ \mathbb{Q} -linearly independent. For k = 2, k=2, the condition is simply saying that log ⁡ p 1 / log ⁡ p 2 ∉ ℚ. \log p_{1}/\log p_{2}\notin\mathbb{Q}.

###### Lemma 4.1.

Let k ≥ 2 k\geq 2 be an integer and p 1, …, p k p_{1},\dots,p_{k} be strongly multiplicatively independent integers and for each i ∈ { 1, …, k } i\in\{1,\dots,k\} let a i ∈ { 0, …, p i − 1 } a_{i}\in\{0,\dots,p_{i}-1\}. If

 | ∑ i = 1 k log ⁡ ( p i − 1) log ⁡ p i < k − 1, \sum_{i=1}^{k}\frac{\log(p_{i}-1)}{\log p_{i}}<k-1, |  |

then the set of numbers in [0, 1] [0,1] whose p i p_{i} -ary expansion does not contain the digit a i a_{i} for all i ∈ { 1, …, k } i\in\{1,\dots,k\} has Hausdorff dimension zero.

### 4.1. Proof of Lemma 4.1

Let p ∈ ℕ p\in\mathbb{N} and a ∈ { 0, …, p − 1 }. a\in\{0,\dots,p-1\}. Define

 | A p ( a) = { x ∈ [0, 1]: the p -ary expansion of n does not contain the digit a } ¯, A_{p}(a)=\overline{\{x\in[0,1]:\text{the $p$-ary expansion of $n$ does not contain the digit $a$}\}}, |  |

adopting the convention that whenever possible a number x x should be written with a terminating digit expansion. A simple calculation shows dim ¯ B ​ A p ​ ( a) = log ⁡ ( p − 1) / log ⁡ p \overline{\dim}_{\mathrm{B}}A_{p}(a)=\log(p-1)/\log p, (see [2, Section 1.3], [6, Chapter 4] for further details). Hence, if ∑ i = 1 k log ⁡ ( p i − 1) / log ⁡ p i < k − 1 \sum_{i=1}^{k}\log(p_{i}-1)/\log p_{i}<k-1, then

 | dim H A p 1 ​ ( a 1) ∩ ⋯ ∩ A p k ​ ( a k) = dim B A p 1 ​ ( a 1) ∩ ⋯ ∩ A p k ​ ( a k) = 0 \dim_{\mathrm{H}}A_{p_{1}}(a_{1})\cap\dots\cap A_{p_{k}}(a_{k})=\dim_{\mathrm{B}}A_{p_{1}}(a_{1})\cap\dots\cap A_{p_{k}}(a_{k})=0 |  |

by Section 2. □ \square

###### Lemma 4.2.

Let k ≥ 2 k\geq 2 and p 1, …, p k p_{1},\dots,p_{k} be strongly multiplicatively independent numbers and for each i ∈ { 1, …, k }, i\in\{1,\dots,k\}, let a i ∈ { 0, …, p i − 1 }. a_{i}\in\{0,\dots,p_{i}-1\}. If

 | ∑ i = 1 k log ⁡ ( p i − 1) / log ⁡ p i < k − 1, \sum_{i=1}^{k}\log(p_{i}-1)/\log p_{i}<k-1, |  |

then for each ϵ > 0 \epsilon>0 there exists a constant C > 0 C>0 such that for each N ≥ 1 N\geq 1,

 | #⁡ { m ∈ { 0, …, N }: the p i -ary expansion of m does not contain a i for all i = 1, …, k } ≤ C ​ N ϵ. \#\{m\in\{0,\dots,N\}:\textnormal{the $p_{i}$-ary expansion of $m$ does not contain $a_{i}$ for all $i=1,\dots,k$}\}\leq CN^{\epsilon}. |  |

Moreover, for

 | A ⁡ ( a 1, …, a k) = { m ∈ ℕ: the p i -ary expansion of m does not contain a i for all i = 1, …, k }, A(a_{1},\dots,a_{k})=\{m\in\mathbb{N}:\textnormal{the $p_{i}$-ary expansion of $m$ does not contain $a_{i}$ for all $i=1,\dots,k$}\}, |  |

we have

 | d ¯ ​ ( { n ∈ ℕ: A ⁡ ( a 1, …, a k) ∩ [p 1 n, p 1 n + 1] ≠ ∅ }) = 0. \overline{d}\left(\{n\in\mathbb{N}:A(a_{1},\dots,a_{k})\cap[p_{1}^{n},p_{1}^{n+1}]\neq\emptyset\}\right)=0. |  |

### 4.2. Proof of Lemma 4.2

Let p ∈ ℕ p\in\mathbb{N} and for each a ∈ { 0, …,, p − 1 } a\in\{0,\dots,,p-1\} define

 | A p ​ ( a) = { n ∈ ℕ: the p -ary expansion of n does not contain the digit a }. A_{p}(a)=\{n\in\mathbb{N}:\text{the $p$-ary expansion of $n$ does not contain the digit $a$}\}. |  |

Let k ∈ ℕ k\in\mathbb{N}, p 1 < ⋯ < p k p_{1}<\dots<p_{k} be strongly multiplicatively independent integers and ( a 1, …, a k) (a_{1},\dots,a_{k}) be an arbitrary k k -tuple with a i ∈ { 0, …, p i − 1 } a_{i}\in\{0,\dots,p_{i}-1\} for each i ∈ { 1, …, k } i\in\{1,\dots,k\}. For brevity, we assume a 1 = a 2 = ⋯ = a k = 0 a_{1}=a_{2}=\dots=a_{k}=0 and note that all the other cases can be treated similarly. Thus, henceforth we write A p i A_{p_{i}} for A p i ​ ( 0) A_{p_{i}}(0). Define

 | K = A p 1 × ⋯ × A p k ⊂ ℕ k. K=A_{p_{1}}\times\dots\times A_{p_{k}}\subset\mathbb{N}^{k}. |  |

We are interested in the intersection l K = K ∩ l l_{K}=K\cap l, where l l is the diagonal line

 | l = { ( n, …, n): n ∈ ℕ }. l=\{(n,\dots,n):n\in\mathbb{N}\}. |  |

First, for each ( n, …, n) ∈ l K (n,\dots,n)\in l_{K} we wish to find a suitable way to renormalize it. To do this, we define the vector (in what follows, {. } \{.\} is the fractional part function),

 | a n = n / p 1 m ​ ( 1, p 2 { m ​ log ⁡ p 1 / log ⁡ p 2 }, …, p k { m ​ log ⁡ p 1 / log ⁡ p k }). \textbf{a}_{n}=n/p_{1}^{m}\left(1,p_{2}^{\{m\log p_{1}/\log p_{2}\}},\dots,p_{k}^{\{m\log p_{1}/\log p_{k}\}}\right). |  |

By construction, a n \textbf{a}_{n} is contained in

 | A p 1 / p 1 m × A p 2 / p 2 m 2 × … ​ A p k / p k m k ⊂ [1, p 1] × [1, p 1 ​ p 2] × ⋯ × [1, p 1 ​ p k] A_{p_{1}}/p_{1}^{m}\times A_{p_{2}}/p_{2}^{m_{2}}\times\dots A_{p_{k}}/p_{k}^{m_{k}}\subset[1,p_{1}]\times[1,p_{1}p_{2}]\times\dots\times[1,p_{1}p_{k}] |  |

for suitable integers m 2, m 3, …, m k. m_{2},m_{3},\dots,m_{k}. For each i ∈ { 1, …, k } i\in\{1,\dots,k\}, we see that

 | A p i / p i m i ⊂ { x ∈ [1, p 1 ​ p i]: The p i -ary expansion of x does not have digit 0 } ¯:= B p i. A_{p_{i}}/p_{i}^{m_{i}}\subset\overline{\{x\in[1,p_{1}p_{i}]:\text{The $p_{i}$-ary expansion of $x$ does not have digit $0$}\}}:=B_{p_{i}}. |  |

Observe that B p i B_{p_{i}} is a subset of a scaled version of a closed × p i mod 1 \times p_{i}\mod 1 invariant set with Hausdorff dimension log ⁡ ( p i − 1) / log ⁡ p i \log(p_{i}-1)/\log p_{i}. Indeed for each i, i,, we first consider the following set

 | B ′ p i = { x ∈ [0, 1]: The p i -ary expansion of x does not have digit 0 } ¯. B^{\prime}_{p_{i}}=\overline{\{x\in[0,1]:\text{The $p_{i}$-ary expansion of $x$ does not have digit $0$}\}}. |  |

To see how B p i ′ B^{\prime}_{p_{i}} is × p i mod 1 \times p_{i}\mod 1 invariant, consider the following construction, which closely mirrors the construction of the middle-third Cantor set. We start with the unit interval [0, 1] [0,1], then decompose it equally into p p pieces, each with length 1 / p. 1/p. We now cut out the first interval, [0, 1 / p). [0,1/p). Then, inside each interval [j / p, ( j + 1) / p), j ∈ { 1, 2, …, p − 1 } [j/p,(j+1)/p),j\in\{1,2,\dots,p-1\} we cut out the first 1 / p 1/p portion, that is, [j / p, j / p + 1 / p 2). [j/p,j/p+1/p^{2}). In this way, we obtain a decreasing sequence of compact sets which converge to B p i ′. B^{\prime}_{p_{i}}. Clearly, this set B p i ′ B^{\prime}_{p_{i}} is closed and × p i mod 1 \times p_{i}\mod 1 invariant. After constructing the set B p i ′, B^{\prime}_{p_{i}}, we consider the scaled set p i k i ​ B p i ′, p^{k_{i}}_{i}B^{\prime}_{p_{i}}, where k i k_{i} is the smallest integer with p i k i > p 1 ​ p i. p_{i}^{k_{i}}>p_{1}p_{i}. For each integer j ∈ { 1, …, p i k i }, j\in\{1,\dots,p^{k_{i}}_{i}\}, the set p i k i ​ B p i ′ ∩ ( j, j + 1) ¯ \overline{p^{k_{i}}_{i}B^{\prime}_{p_{i}}\cap(j,j+1)} is empty, or else it is the translated set B p i ′ + j. B^{\prime}_{p_{i}}+j.

As n n varies in [p 1 m, p 1 m + 1) [p^{m}_{1},p^{m+1}_{1}), the vectors a n \textbf{a}_{n} are contained in a line through the origin with direction vector

 | ( 1, p 2 { m ​ log ⁡ p 1 / log ⁡ p 2 }, …, p k { m ​ log ⁡ p 1 / log ⁡ p k }). (1,p_{2}^{\{m\log p_{1}/\log p_{2}\}},\dots,p_{k}^{\{m\log p_{1}/\log p_{k}\}}). |  |

Denoting this line as l m l_{m}, we see that all values of a n \textbf{a}_{n} (if they exist) must be contained in

 | l m ∩ ( B p 1 × ⋯ × B p k). l_{m}\cap(B_{p_{1}}\times\dots\times B_{p_{k}}). |  |

Consider the intervals [n, n + 1] [n,n+1] for n ∈ { p 1 m, …, p 1 m + 1 − 1 }. n\in\{p^{m}_{1},\dots,p^{m+1}_{1}-1\}. Thus, any a n \textbf{a}_{n} (if it exists) must have a first coordinate in the interval [n / p 1 m, ( n + 1) / p 1 m]. [n/p^{m}_{1},(n+1)/p^{m}_{1}]. We decompose l m l_{m} into closed line segments of equal length and disjoint interiors according to the first coordinate, i.e. the components have a first coordinate of form [j / p 1 m, ( j + 1) / p 1 m] [j/p^{m}_{1},(j+1)/p^{m}_{1}] for integers j. j. We denote this collection of line segments ℐ m \mathcal{I}_{m}, and wish to estimate the length of those line segments. We know the length of the projection of the first coordinate, say, d > 0. d>0. We also know the direction vector of the line l m l_{m}, say 𝐭 = ( t 1, t 2, …, t k). \mathbf{t}=(t_{1},t_{2},\dots,t_{k}). Then, the length of the line segments will be equal to

 | t 1 2 + ⋯ + t k 2 | t 1 | ​ d. \frac{\sqrt{t^{2}_{1}+\dots+t^{2}_{k}}}{|t_{1}|}d. |  |

Together with (Direction), we see that the length we want to compute is in the range

 | [p 1 − m, p 1 − m ​ 1 + p 2 2 + … ​ p k 2]. \left[p^{-m}_{1},p_{1}^{-m}\sqrt{1+p^{2}_{2}+\dots p^{2}_{k}}\right]. |  |

By Section 2, we see that for each ϵ > 0 \epsilon>0, there is an integer N ϵ > 0 N_{\epsilon}>0 such that for each m ≥ N ϵ m\geq N_{\epsilon}, the number of elements in ℐ m \mathcal{I}_{m} intersecting B p 1 × ⋯ × B p k B_{p_{1}}\times\dots\times B_{p_{k}} is smaller than p 1 ϵ ​ m. p^{\epsilon m}_{1}. Therefore, for m ≥ N ϵ m\geq N_{\epsilon}, the number of points ( n, …, n) (n,\dots,n) on l K l_{K} with n ∈ [p 1 m, p 1 m + 1) n\in[p^{m}_{1},p^{m+1}_{1}) is at most p 1 ϵ ​ m. p_{1}^{\epsilon m}. Thus, there is a constant C > 0 C>0 such that for all N ≥ 1, N\geq 1,

 | #​ A p 1 ​ ( 0) ∩ ⋯ ∩ A p k ​ ( 0) ∩ [1, N] ≤ C ​ N ϵ. \#A_{p_{1}}(0)\cap\dots\cap A_{p_{k}}(0)\cap[1,N]\leq CN^{\epsilon}. |  |

This concludes the first part. For the second, we utilise Section 2.4.

Suppose that a n \textbf{a}_{n} exists for some n ∈ [p 1 m, p 1 m + 1) n\in[p^{m}_{1},p^{m+1}_{1}) for all m ∈ ℳ ⊆ ℕ m\in\mathcal{M}\subseteq\mathbb{N}, where d ¯ ​ ( ℳ) > 0 \overline{d}(\mathcal{M})>0. This implies that

 | { ( 1, p 2 { m ​ log ⁡ p 1 / log ⁡ p 2 }, …, p k { m ​ log ⁡ p 1 / log ⁡ p k }) } m ∈ ℳ ¯ \overline{\{(1,p_{2}^{\{m\log p_{1}/\log p_{2}\}},\dots,p_{k}^{\{m\log p_{1}/\log p_{k}\}})\}_{m\in\mathcal{M}}} |  |

has positive Lebesgue measure, forcing

 | B p 1 × ⋯ × B p k B_{p_{1}}\times\dots\times B_{p_{k}} |  |

to have dimension at least k − 1 k-1, by Section 2.5. This is a contradiction and concludes the proof of the second part. □ \square

### 4.3. Proof of Theorem 1.6

Let p 1, p 2, ⋯ = 3, 4, 5, … p_{1},p_{2},\dots=3,4,5,\dots be the list of prime numbers greater than two together with 4 4. Under Schanuel’s conjecture and Lemma 3.1, we see that p 1, … p_{1},\dots are strongly multiplicatively independent. Observe that for each i ≥ 1, i\geq 1,

 | log ⁡ ( p i − 1) log ⁡ p i = 1 + 1 log ⁡ p i ​ log ⁡ ( 1 − p i − 1) ≤ 1 − 1 p i ​ log ⁡ p i. \frac{\log(p_{i}-1)}{\log p_{i}}=1+\frac{1}{\log p_{i}}\log(1-p_{i}^{-1})\leq 1-\frac{1}{p_{i}\log p_{i}}. |  |

It may be easily numerically computed that the following convergent sum

 | C = ∑ i ≥ 1 1 p i ​ log ⁡ p i ≈ 1.09561. C=\sum_{i\geq 1}\frac{1}{p_{i}\log p_{i}}\approx 1.09561. |  |

and, in fact

 | C > ∑ i = 1 26 1 p i ​ log ⁡ p i ≥ 1.00112 > 1. C>\sum_{i=1}^{26}\frac{1}{p_{i}\log p_{i}}\geq 1.00112>1. |  |

Note that p 26 = 101 p_{26}=101, the 26 26 -th prime number. Next, we apply Lemma 4.2 with k = 26 k=26 and a collection a 1, …, a k a_{1},\dots,a_{k} chosen arbitrarily. Fix a small number ϵ > 0 \epsilon>0, for each such collection of a 1, …, a k a_{1},\dots,a_{k}, there is a constant C a 1, …, a k C_{a_{1},\dots,a_{k}} such that among the first N N integers, all but at most C a 1, …, a k ​ N ϵ C_{a_{1},\dots,a_{k}}N^{\epsilon} many of them contain a i a_{i} in their p i p_{i} -ary expansion for at least one i ∈ { 1, …, k }. i\in\{1,\dots,k\}. There are finitely many choices of the tuple a 1, …, a k a_{1},\dots,a_{k}, and thus setting

 | C:= ∑ a 1, …, a k C a 1, …, a k < ∞ C:=\sum_{a_{1},\dots,a_{k}}C_{a_{1},\dots,a_{k}}<\infty |  |

completes the first part of the proof. For numbers in ( 0, 1) (0,1) we may argue similarly and apply Lemma 4.1. □ \square

## 5. Numbers with only binary digits in different bases

In this Section we prove Theorem 1.2 and Theorem 1.4.

### 5.1. Proof of Theorem 1.2

We utilise the general strategy found in the proof of Lemma 4.2. Note that, for a base b b, the set A b A_{b} of numbers in [0, 1] [0,1] whose b b -ary expansion contain only the digits 0, 1 0,1 has Hausdorff dimension log ⁡ 2 / log ⁡ b \log 2/\log b. Thus, Theorem 1.2 follows by a direct modification of the proof of Lemma 4.2 (with k = 2 k=2 in the statement) together with the fact that

 | log ⁡ 2 log ⁡ 4 + log ⁡ 2 log ⁡ 5 ≈ 0.930677 < 1. \frac{\log 2}{\log 4}+\frac{\log 2}{\log 5}\approx 0.930677<1. |  |

□ \square

### 5.2. Proof of Theorem 1.4

First, observe

 | log ⁡ 2 log ⁡ 3 + log ⁡ 2 log ⁡ 4 > 1 = 2 − 1. \frac{\log 2}{\log 3}+\frac{\log 2}{\log 4}>1=2-1. |  |

Hence, we may not proceed as before by utilising the method of Lemma 4.2.

By a result in [26] and [24], for any line l l not parallel with the coordinate axes, the intersection l ∩ A 4 × A 3 l\cap A_{4}\times A_{3} has dimension at most log ⁡ 2 / log ⁡ 3 + log ⁡ 2 / log ⁡ 4 − 1 \log 2/\log 3+\log 2/\log 4-1. This is the reason for the exponent that appeared in Theorem 1.4. By [27, Lemma 11.1], there is an integer M > 0 M>0 and closed × 3 M mod 1 \times 3^{M}\mod 1 invariant sets A 3 ′, A 3 ′′ ⊂ [0, 1] A^{\prime}_{3},A^{\prime\prime}_{3}\subset[0,1] with

 | A 3 ⊂ A 3 ′ + A 3 ′′, A_{3}\subset A^{\prime}_{3}+A^{\prime\prime}_{3}, |  |

 | | dim H A 3 ′ − 0.49 | < 0.0001, |\dim_{\mathrm{H}}A^{\prime}_{3}-0.49|<0.0001, |  |

and

 | dim H A 3 ′ + dim H A 3 ′′ ≤ log ⁡ 2 / log ⁡ 3 + 0.0001. \dim_{\mathrm{H}}A^{\prime}_{3}+\dim_{\mathrm{H}}A^{\prime\prime}_{3}\leq\log 2/\log 3+0.0001. |  |

By applying the argument in the proof of Lemma 4.2, for each integer n ≥ 1 n\geq 1, we may map { x = y } ∩ { x ∈ [4 n, 4 ( n + 1)] } \{x=y\}\cap\{x\in[4^{n},4^{(n+1)}]\} to a line passing through the origin with slope 9 { n ​ log ⁡ 4 / log ⁡ 9 } 9^{{\{n\log 4/\log 9\}}}. Denote this line l n. l_{n}. We wish to estimate how large l n ∩ A 4 × A 3 ∩ { x ∈ [1, 9] } l_{n}\cap A_{4}\times A_{3}\cap\{x\in[1,9]\} can be. Considering l n ∩ A 4 × ( A 3 ′ + A 3 ′′) l_{n}\cap A_{4}\times(A^{\prime}_{3}+A^{\prime\prime}_{3}), we note this can be written as

 | ⋃ t ∈ A 3 ′′ ( ( l n − ( 0, t)) ∩ A 4 × A 3 ′) + t. \bigcup_{t\in A^{\prime\prime}_{3}}((l_{n}-(0,t))\cap A_{4}\times A^{\prime}_{3})+t. |  |

In general, ( l n − ( 0, t)) ∩ A 4 × A 3 ′ (l_{n}-(0,t))\cap A_{4}\times A^{\prime}_{3} is small for each individual t t, however, since there are uncountably many elements in A 3 ′′ A^{\prime\prime}_{3}, we cannot say anything about the union. However, in our discrete case we may bypass this issue.

Our aim is to decompose A 3 A_{3} in such a way that we can utilise the uniform small dimension result discussed in Section 2. Let m, r m,r be two integers with m ≥ 2 m\geq 2 and r ∈ { 0, …, m − 1 } r\in\{0,\dots,m-1\}. Denote A 3 ​ ( m, r) A_{3}(m,r) to be the subset of A 3 A_{3} consisting those numbers whose ternary expansion may only have the digit 1 1 in the ( k ​ m + r) (km+r) -th positions for all integers k ≥ 0 k\geq 0. We then observe

 | A 3 = ∑ r = 0 m − 1 A 3 ​ ( m, r) A_{3}=\sum_{r=0}^{m-1}A_{3}(m,r) |  |

as a sumset. Choosing an integer s < m − 1 s<m-1 such that

 | A 3 ′ = ∑ r = 0 s A 3 ​ ( m, r) A_{3}^{\prime}=\sum_{r=0}^{s}A_{3}(m,r) |  |

and

 | A 3 ′′ = ∑ r = s + 1 m − 1 A 3 ​ ( m, r) A_{3}^{\prime\prime}=\sum_{r=s+1}^{m-1}A_{3}(m,r) |  |

yields A 3 = A 3 ′ + A 3 ′′. A_{3}=A_{3}^{\prime}+A_{3}^{\prime\prime}. By choosing m m to be suitably large as well as s s we may force

 | 0.49 < dim H A 3 ′ < 0.5. 0.49<\dim_{\mathrm{H}}A_{3}^{\prime}<0.5. |  |

Hence dim H A 3 ′ + dim H A 4 < 1 \dim_{\mathrm{H}}A_{3}^{\prime}+\dim_{\mathrm{H}}A_{4}<1 and A 3 ′ A_{3}^{\prime} is × 3 m mod 1 \times 3^{m}\mod 1 invariant.

Recall that we wish to investigate l n ∩ 4 ​ A 4 × 27 ​ A 3 l_{n}\cap 4A_{4}\times 27A_{3}. In particular, we wish to count the number of points in l n ∩ 4 ​ A 4 × 27 ​ A 3 l_{n}\cap 4A_{4}\times 27A_{3} whose x x coordinate is of form k / 4 n, k ∈ { 4 n, …, 4 n + 1 − 1 }. k/4^{n},k\in\{4^{n},\dots,4^{n+1}-1\}. If a ∈ l n ∩ 4 ​ A 4 × 27 ​ A 3 a\in l_{n}\cap 4A_{4}\times 27A_{3}, then there is a t ∈ 27 ​ A 3 ′′ t\in 27A^{\prime\prime}_{3} such that ( a − ( 0, t)) ∈ 4 ​ A 4 × 27 ​ A 3 ′ (a-(0,t))\in 4A_{4}\times 27A_{3}^{\prime}. It is easy to check that we only need to consider those t t with a terminating ternary expansion of at most [( n + 1) ​ log ⁡ 4 / log ⁡ 3] [(n+1)\log 4/\log 3] many digits in total.

Let ϵ > 0 \epsilon>0 be a small number. There exists an integer N ϵ N_{\epsilon} such that we may apply Section 2. Assume that n ≥ N ϵ n\geq N_{\epsilon}. For each t t as above, we see that ( l n − ( 0, t)) ∩ 4 ​ A 4 × 27 ​ A 3 (l_{n}-(0,t))\cap 4A_{4}\times 27A_{3} can be covered by at most 4 n ​ ϵ 4^{n\epsilon} balls of radius 4 − n 4^{-n}. Moreover, there is a constant C C (depending only on m m) such that there are no more than C ​ 4 n ⁡ ( log ⁡ 2 / log ⁡ 3 − 0.49) C4^{n(\log 2/\log 3-0.49)} many such t t to be considered. Hence, l n ∩ 4 ​ A 4 × 27 ​ A 3 l_{n}\cap 4A_{4}\times 27A_{3} can be covered by at most C ​ 4 n ⁡ ( log ⁡ 2 / log ⁡ 3 − 0.49 + ϵ) C4^{n(\log 2/\log 3-0.49+\epsilon)} many balls of radius 4 − n. 4^{-n}. This implies that among all integers in [4 n, 4 n + 1), [4^{n},4^{n+1}), there are no more than C ​ 4 n ⁡ ( log ⁡ 2 / log ⁡ 3 − 0.49 + ϵ) C4^{n(\log 2/\log 3-0.49+\epsilon)} many of them with base 3 3 and 4 4 expansions containing only binary digits. We can replace 0.49 0.49 to be any number smaller than 0.5 0.5 (by choosing m m to be large enough), concluding the proof of first part of Theorem 1.4.

Figure 2. The two solid lines have slopes 1 1 and 9 9. The four dashed lines have slopes 1.5, 2.25, 4.5 1.5,2.25,4.5 and 6.25. 6.25.

For the second part, note that l n l_{n} is a line passing through the origin with slope 9 { n ​ log ⁡ 4 / log ⁡ 9 } 9^{\{n\log 4/\log 9\}}. As n n varies through the natural numbers, 9 { n ​ log ⁡ 4 / log ⁡ 9 } 9^{\{n\log 4/\log 9\}} will take values in [1, 9]. [1,9]. Figure 2 illustrates that there are regions of slopes such that the lines passing through the origin with those slopes cannot intersect

 | ( 4 ​ A 4 ∩ [1, 4]) × ( 27 ​ A 3 ∩ [1, 27]). (4A_{4}\cap[1,4])\times(27A_{3}\cap[1,27]). |  |

For example, if

 | 9 { n ​ log ⁡ 4 / log ⁡ 9 } ∈ ( 1.5, 2.25) ∪ ( 4.5, 6.25), 9^{\{n\log 4/\log 9\}}\in(1.5,2.25)\cup(4.5,6.25), |  |

then

 | l n ∩ ( 4 ​ A 4 ∩ [1, 4]) × ( 27 ​ A 3 ∩ [1, 27]) = ∅. l_{n}\cap(4A_{4}\cap[1,4])\times(27A_{3}\cap[1,27])=\emptyset. |  |

Since the slopes equidistribute across [1, 9] [1,9], directly computing the proportion of such regions in [1, 9] [1,9] shows the above intersection is empty for at least a 0.36907 0.36907 portion of ℕ \mathbb{N}. □ \square

## 6. Discussion, Conjectures and Open Problems

In this section we provide some broad insights into the above topics to help future work. Divided into three subsections, the first deals our numerical analysis on digit special numbers, the second with binary expansions in base 3 3 and 4 4, and the last with related open problems.

### 6.1. Digit-special numbers

We have computed the approximate number of digit special numbers lower than 3 36 3^{36}. In order to check whether n ∈ ℕ n\in\mathbb{N} is special, it suffices to check its base g g expansion for 3 ≤ g ≤ b 3\leq g\leq b and g g either a prime number or 4 4, where b b is the largest prime such that b b ≤ n b^{b}\leq n. In the following, we denote this collection of bases B n B_{n}. If we choose a digit for each base g g, then the amount of numbers whose base g g expansion misses the chosen digit in each base for all g ∈ B n g\in B_{n} is O ⁡ ( n s + ϵ) O(n^{s+\epsilon}), where

 | s = max ⁡ { 0, ∑ g ∈ B n log ⁡ ( g − 1) log ⁡ g − ( #​ B n − 1) }. s=\max\left\{0,\sum_{g\in B_{n}}\frac{\log(g-1)}{\log g}-(\#B_{n}-1)\right\}. |  |

To understand this choice of s s we direct the reader to the hypotheses of Lemma 4.2 and the decomposition method found at the beginning of the proof of Theorem 1.4. As there are ∏ g ∈ B n g \prod_{g\in B_{n}}g many choices of different possible combinations of missing digits, a very rough estimate for the amount of special-numbers less than n n is

 | Est ​ ( n) = n s ​ ∏ g ∈ B n g. \text{Est}(n)=n^{s}\prod_{g\in B_{n}}g. |  |

Letting

 | Real ​ ( n) = #⁡ { i ≤ n: i is digit special }, \text{Real}(n)=\#\{i\leq n:\text{$i$ is digit special}\}, |  |

in Figure 3 we compare Est ​ ( n) \text{Est}(n) with the actual data, by plotting G ⁡ ( n) = log ⁡ Est ​ ( n) / log ⁡ n G(n)=\log\text{Est}(n)/\log n and R ⁡ ( n) = log ⁡ Real ​ ( n) / log ⁡ n R(n)=\log\text{Real}(n)/\log n. Specifically, it is worth observing that the estimates appear to become quite precise for n ≥ 31 n\geq 31.

[image: Refer to caption] Figure 3. This is a plot of R ⁡ ( 3 n), G ⁡ ( 3 n) R(3^{n}),G(3^{n}) for 8 ≤ n ≤ 36 8\leq n\leq 36. Corollary 1.6 implies that the R R points will eventually drop near to 0 0.

Although these estimates are somewhat crude, they approximate the true values surprisingly well for large n n. In order to establish the theoretical reasons for this, further quantitive information on the constant C C appearing in Lemma 4.2 is required.

The overarching message of our analysis is that digit-special numbers are exceptionally rare. Thus, we conclude this part of the discussion with the following two conjectures, which constitute a strengthening of Theorem 1.6.

###### Conjecture 6.1.

There are finitely many digit-special integers.

###### Conjecture 6.2.

Digit-special numbers in ( 0, 1) (0,1) are rational.

### 6.2. Binary digit expansions in base 3 3 and 4 4.

Next, we will discuss some further conjectures and questions relating to the sequence [16] on numbers with only binary digits in their base 3 3 and 4 4 expansions. For [16], it would be interesting to compute the exact density of the appearance of 0 0. Recall that in Theorem 1.4 we showed that 0 0 must appear at a lower density of at least 0.36907 0.36907. In addition, Figure 1 suggests that for the non-zero terms it seems likely the exponent log ⁡ 2 / log ⁡ 3 − 0.5 \log 2/\log 3-0.5 is essentially sharp. The following questions makes this precise.

###### Question 6.3.

For each ϵ > 0, \epsilon>0, are there infinitely many integers n ∈ ℕ n\in\mathbb{N} such that 𝒮 ⁡ ( n) ≥ 4 n ⁡ ( log ⁡ 2 / log ⁡ 3 − 0.5 − ϵ) \mathcal{S}(n)\geq 4^{n(\log 2/\log 3-0.5-\epsilon)}?

It is already interesting to see whether 𝒮 ⁡ ( n) > 0 \mathcal{S}(n)>0 for infinitely many n. n. Unfortunately, Theorem 1.8 cannot help us to find an answer, since in the statement of the theorem we must have A = B = 1 A=B=1, but then

 | 1 2 + 1 3 < 1. \frac{1}{2}+\frac{1}{3}<1. |  |

On the other hand, if we were to consider numbers containing { 0, 1, 2 } \{0,1,2\} in their base 4 4 expansion, then we would find infinitely many, since

 | 1 2 + 2 3 > 1. \frac{1}{2}+\frac{2}{3}>1. |  |

###### Question 6.4.

What is the lower density of { n ∈ ℕ: 𝒮 ⁡ ( n) = 0 } \{n\in\mathbb{N}:\mathcal{S}(n)=0\}?

In relation to Question 6.4, note that for the last part of Theorem 1.4, we were required to identify the proportion of slopes in Figure 2 avoiding a cantor-like set. The estimate given is based on just the largest interval of such slopes. In fact, there are smaller gaps that we did not point out, as illustrated in Figure 4, which is a zoomed-in picture of Figure 2. Including these further regions in the calculation yields a small improvement of approximately 0.0115 0.0115 to the lower density estimate. Thus, the heart of Question 6.4 is to compute the sum of the lengths of all such gaps.

Figure 4. Zoomed-in version of Figure 2, the lines have slops 1, 1.2, 16 / 13, 1.5. 1,1.2,16/13,1.5.

As a final question, note that thus far we have separately discussed integers and numbers in ( 0, 1). (0,1). However, the similarity in the methods used suggests a potential connection, which we describe in the following conjecture.

###### Conjecture 6.5.

Let p 1, …, p k p_{1},\dots,p_{k} be strongly multiplicatively independent integers. For each i ∈ { 1, …, k } i\in\{1,\dots,k\} and D i ⊂ { 0, …, p i − 1 } D_{i}\subset\{0,\dots,p_{i}-1\}, define

 | A p i ​ ( D i) = { x ∈ ( 0, 1): the p -ary expansion of x does not have a digit in D i } A_{p_{i}}(D_{i})=\{x\in(0,1):\text{the $p$-ary expansion of $x$ does not have a digit in $D_{i}$}\} |  |

and

 | A ~ p i ​ ( D i) = { x ∈ ℕ: the p -ary expansion of x does not have a digit in D i }. \tilde{A}_{p_{i}}(D_{i})=\{x\in\mathbb{N}:\text{the $p$-ary expansion of $x$ does not have a digit in $D_{i}$}\}. |  |

Furthermore, let A = ∩ i = 1 k A p i ( D i). A=\cap_{i=1}^{k}A_{p_{i}}(D_{i}). If

 | ∑ i ∈ { 1, …, k } dim H A p i = s ∈ ( k − 1, k), \sum_{i\in\{1,\dots,k\}}\dim_{\mathrm{H}}A_{p_{i}}=s\in(k-1,k), |  |

then there exist constants c c and C C such that

 | c ​ N s − ( k − 1) ≤ #​ A ∩ [1, N] ≤ C ​ N s − ( k − 1) cN^{s-(k-1)}\leq\#A\cap[1,N]\leq CN^{s-(k-1)} |  |

for all integers N. N. If s < k − 1 s<k-1, then A A is finite.

We will see shortly that under Schanuel’s conjecture, the above conjecture may resolve Graham’s problem.

### 6.3. A return to binomial coefficients

Unless otherwise mentioned, Schanuel’s conjecture is assumed for the discussions in this subsection. A number of problems related to the prime factors of binomial coefficients ( 2 ​ n n) \binom{2n}{n} have been discussed, but the alert reader may notice that we actually have not explicitly proved Theorem 1.10. However, one can easily modify the proof of Theorem 1.4 to show Theorem 1.10 with just a few key observations. First, notice that 3, 5, 7 3,5,7 satisfy the condition on p 1, p 2, p 3 p_{1},p_{2},p_{3} in the result of Section 2 and that

(6.1) |  | log ⁡ 2 log ⁡ 3 + log ⁡ 3 log ⁡ 5 + log ⁡ 4 log ⁡ 7 − 2 ≈ 0.0259 < 0.026. \frac{\log 2}{\log 3}+\frac{\log 3}{\log 5}+\frac{\log 4}{\log 7}-2\approx 0.0259<0.026. |  |

Without using Schanuel’s conjecture, we can use Theorem 1.11 to find an integer n ∈ { 7, 11, 13 } n\in\{7,11,13\} such that 1, log ⁡ 3 / log ⁡ 5, log ⁡ 3 / log ⁡ n 1,\log 3/\log 5,\log 3/\log n are ℚ \mathbb{Q} -linearly independent. The worst upper bound occurs when n = 13 n=13,

 | log ⁡ 2 log ⁡ 3 + log ⁡ 3 log ⁡ 5 + log ⁡ 7 log ⁡ 13 − 2 ≈ 0.0722 < 0.073. \frac{\log 2}{\log 3}+\frac{\log 3}{\log 5}+\frac{\log 7}{\log 13}-2\approx 0.0722<0.073. |  |

Under Schanuel’s conjecture, however, we may set n = 7 n=7 and perform a decomposition as discussed in the proof of Theorem 1.4 together with ( 6.1) to deduce Theorem 1.10.

Now let us put Conjecture 6.5 into play. Together with the computations above, we see that Conjecture 6.5 would imply Conjecture 1.9 and thus answer the Graham’s $ 1000 \$1000 problem.

Finally, we note how our methods also provide information on natural generalisations of Graham’s problem. For example, one may consider 1155 = 3 × 5 × 7 × 11 1155=3\times 5\times 7\times 11 in place of 105, 105, see [22] for some numerical computations. It is conjectured that the only integers n n such that ( 2 ​ n n) \binom{2n}{n} is coprime with 1155 1155 are 0, 1, 3160 0,1,3160, motivated by the fact there are no other examples smaller than 10 10000. 10^{10000}. Observing that

 | log ⁡ 2 log ⁡ 3 + log ⁡ 3 log ⁡ 5 + log ⁡ 4 log ⁡ 7 + log ⁡ 6 log ⁡ 11 < 3, \frac{\log 2}{\log 3}+\frac{\log 3}{\log 5}+\frac{\log 4}{\log 7}+\frac{\log 6}{\log 11}<3, |  |

the proof of Theorem 1.2 may be generalised to yield the following.

###### Theorem 6.6.

Assume Schanuel’s conjecture. Let N N be an integer. Denote G ⁡ ( N) G(N) to be the number of positive integers n ≤ N n\leq N such that ( 2 ​ n n) \binom{2n}{n} is coprime with 1155 1155. Then for all ϵ > 0, \epsilon>0, we have

 | G ⁡ ( N) ≤ N ϵ G(N)\leq N^{\epsilon} |  |

for all large enough N. N.

### 6.4. Strongly multiplicative independence

If k ≥ 3 k\geq 3, we have seen that Schanuel’s conjecture implies some integers p 1, p 2, …, p k p_{1},p_{2},\dots,p_{k} are strongly multiplicatively independent if they are multiplicatively independent. In other words, if

 | 1, log ⁡ p 1, …, log ⁡ p k 1,\log p_{1},\dots,\log p_{k} |  |

are ℚ \mathbb{Q} -linearly independent. Without assuming Schanuel’s conjecture, we saw that at least one of the triples ( 3, 5, 7), ( 3, 5, 11), ( 3, 5, 13) (3,5,7),(3,5,11),(3,5,13) are strongly multiplicatively independent. Thus there exists at least one strongly multiplicatively independent integer triple.

If one wishes to consider strong multiplicative independence of quadruples, the situation is far more complex and the proof of Theorem 1.11 cannot be directly generalized. It is unknown whether such quadruples exist, although, under Schanuel’s conjecture, one would expect there to be multitudes.

## 7. Acknowledgement

The authors would like to thank Douglas Howroyd for many useful discussions and help with the numerical computations used to create Figure 3. The authors also want to thank Carlo Sanna for bringing us the connection between Graham’s problem and results in an early version of this manuscript. SAB was supported by a *Carnegie Trust PhD Scholarship*(PHD060287) and HY was financially supported by the University of St Andrews, the University of Cambridge and the Corpus Christi College, Cambridge. HY has received funding from the European Research Council (ERC) under the European UnionÕs Horizon 2020 research and innovation programme (grant agreement No. 803711).

## References

- [1] J. Ax, *On Schanuel’s Conjectures*, Annals of Mathematics, 93 (2), (1971).
- [2] C. Bishop and Y. Peres, *Fractals in Probability and Analysis*, Cambridge University Press, (2017).
- [3] T. Dupuy and D. Weirich, *Bits of 3 n 3^{n} in binary, Wieferich primes and a conjecture of Erdős*, Journal of Number theory, 158, (2016), 268-280.
- [4] P. Erdős, *Some Unconventional Problems in Number Theory*, Mathematics Magazine, 52 (2), (1979), 67-70.
- [5] P. Erdős, R. Graham, I. Ruzsa and E. Straus, *On the Prime Factors of ( 2 ​ n n) \binom{2n}{n}*, Mathematics of Computation, 29 (129), (1975), 83-92.
- [6] K.J. Falconer, *Fractal geometry: Mathematical foundations and applications, second edition*, John Wiley and Sons, Ltd, (2005).
- [7] H. Furstenberg, *Intersections of Cantor sets and transversality of semigroups*, Problems in Analysis, Princeton University Press, (1970), 41-59.
- [8] H. Furstenberg. *Ergodic fractal measures and dimension conservation*, Ergodic Theory Dynamical Systems, 28, (2008), 405–422.
- [9] E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocit"atsgesetzen*, Journal für die reine und angewandte Mathematik. 44, (1852), 93-146.
- [10] J. Lagarias, *Ternary expansions of powers of 2 2*, Journal of the London Mathematical Society, 79, (2009), 562-588.
- [11] S. Lang, *Introduction to transcendental numbers*, Addison-Wesley Publishing Co., (1966).
- [12] P. Mattila, *Geometry of sets and measures in Euclidean spaces: Fractals and rectifiability*, Cambridge Studies in Advanced Mathematics, Cambridge University Press, (1999).
- [13] Numberphile, *Why 82,000 is an extraordinary number*, Youtube video: URL: [https://www.youtube.com/watch?v=LNS1fabDkeA][5], (2015).
- [14] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/][6].
- [15] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A230360][7].
- [16] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A146025][8].
- [17] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A146026][9].
- [18] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A146027][10].
- [19] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A146028][11].
- [20] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A146029][12].
- [21] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A030979][13].
- [22] N. J. A. Sloane, *The On-Line Encyclopedia of Integer Sequences,*URL: [http://oeis.org/A151750][14].
- [23] C. Pomerance, *Divisors of the middle binomial coefficient*, *American Mathematical Monthly*, 122 (7), (2015), 636-644.
- [24] P. Shmerkin, *On Furstenberg’s intersection conjecture, self-similar measures, and the L q L^{q} norms of convolutions*, Annals of Mathematics, 189 (2), (2019).
- [25] C. Stewart, *On the representation of an integer in two different bases*, J. Reine Angew. Math., 319, (1980), 63-72.
- [26] M. Wu, *A proof of Furstenberg’s conjecture on the intersections of × p \times p and × q \times q -invariant sets*, Annals of Mathematics, 189 (3), 707-751, (2019).
- [27] H. Yu, *Discrepancies of irrational rotations, binary expansions of powers of 3 and an improvement on Furstenberg’s slicing problem*, preprint, arxiv: 1811.11073, (2018).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:sb235@st-andrews.ac.uk
[4]: mailto:hy351@maths.cam.ac.uk
[5]: https://www.youtube.com/watch?v=LNS1fabDkeA
[6]: http://oeis.org/
[7]: http://oeis.org/A230360
[8]: http://oeis.org/A146025
[9]: http://oeis.org/A146026
[10]: http://oeis.org/A146027
[11]: http://oeis.org/A146028
[12]: http://oeis.org/A146029
[13]: http://oeis.org/A030979
[14]: http://oeis.org/A151750
