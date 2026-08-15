<!-- source: https://ar5iv.labs.arxiv.org/html/1511.04315 | converted from HTML -->

[1511.04315] A growth model based on the arithmetic Z -game

# A growth model based on the arithmetic Z Z -game

Cristian Cobeli, Mihai Prunescu, Alexandru Zaharescu Address: Cristian Cobeli, Simion Stoilow, Institute of Mathematics of the Romanian Academy, 21 Calea Griviţei Street, 010702; P.O. Box 1-764, 014700, Bucharest, Romania Email address: [cristian.cobeli@imar.ro][1] Address: Mihai Prunescu, Simion Stoilow, Institute of Mathematics of the Romanian Academy, 21 Calea Griviţei Street, 010702; P.O. Box 1-764, 014700, Bucharest, Romania Email address: [mihai.prunescu@imar.ro][2] Address: Alexandru Zaharescu, Department of mathematics, University of Illinois, 1409 West Green Street, Urbana , IL 61801, USA, and Simion Stoilow, Institute of Mathematics of the Romanian Academy, 21 Calea Griviţei Street, 010702; P.O. Box 1-764, 014700, Bucharest, Romania Email address: [zaharesc@illinois.edu][3]

###### Abstract.

We present an evolutionary self-governing model based on the numerical atomic rule Z ⁡ ( a, b) = a ​ b / gcd ⁡ ( a, b) 2 Z(a,b)=ab/\gcd(a,b)^{2}, for a, b a,b positive integers. Starting with a sequence of numbers, the initial generation 𝒢 i ​ n {\mathcal{G}_{in}}, a new sequence is obtained by applying the Z Z -rule to any neighbor terms. Likewise, applying repeatedly the same procedure to the newest generation, an entire matrix T 𝒢 i ​ n T_{\mathcal{G}_{in}} is generated. Most often, this matrix, which is the recorder of the whole process, shows a fractal aspect and has intriguing properties.

If 𝒢 i ​ n {\mathcal{G}_{in}} is the sequence of positive integers, in the associated matrix remarkable are the distinguished geometrical figures called the Z Z -solitons and the sinuous evolution of the size of numbers on the western edge. We observe that T ℕ ∗ T_{\mathbb{N}^{*}} is close to the analogue free of solitons matrix generated from an initial generation in which each natural number is replaced by its largest divisor that is a product of distinct primes. We describe the shape and the properties of this new matrix.

N. J. A. Sloane raised a few interesting problems regarding the western edge of the matrix T ℕ ∗ T_{\mathbb{N}^{*}}. We solve one of them and present arguments for a precise conjecture on another.

###### Key words and phrases:

Absolute differences, cellular automata, growth model, recurrent sequences, self-similar processes, dynamic lattice systems, solitons.

###### 2010 Mathematics Subject Classification

Primary 37B15, Secondary 68Q80, 82C22, 82C20, 60G18.

## 1. Introduction Story

Many different mathematical models have been proposed to study an evolutionary self-governing system. In the last several decades, a particular attention was devoted to those that are based on simple generating rules that produce complex outcomes. Such an example is the growing model based on the numerical Z Z -rule introduced in [12]

 | Z ⁡ ( a, b) = a ​ b gcd ⁡ ( a, b) 2, a, b ∈ ℕ ∗, \begin{split}Z(a,b)=\frac{ab}{\gcd(a,b)^{2}}\,,\quad\text{ $a,b\in{\mathbb{N}^{*}}$,}\end{split} |  | (1.1) |

where ℕ ∗:= ℕ ∖ { 0 } {\mathbb{N}^{*}}:=\mathbb{N}\setminus\{0\}. The numbers are recorded in cells and, for simplicity, we keep the unidirectional development of future generations, composed of children Z ⁡ ( a, b) Z(a,b) born from parents a a and b b, which are neighbor cells in the previous generation.

For a plastic representation of the Z Z -rule ( 1.1), one can think that any cell containing a positive integer n n is a citadel composed of towers. There are as many towers in the citadel as prime factors n n has. Each tower is associated to a prime and the height of the tower corresponding to a prime p p that divides n n equals the power of p p in the factor decomposition of n n. In particular, the citadel of a cell containing the number 1 1 has no towers at all. Likewise, one may think that the citadel n n has towers associated to the primes that do not divide n n also, but these towers have zero height. Then, the Z Z -rule topples the towers of the neighbor citadels a a and b b creating a new citadel Z ⁡ ( a, b) Z(a,b) in the next generation. The towers of the new citadel have heights equal with the absolute difference of the heights of towers corresponding to the same prime in a a and b b and, if a prime divides only one of a a and b b, then this tower is reproduced unchanged in the new citadel.

The process starts with a sequence of numbers 𝒢 i ​ n {\mathcal{G}_{in}}, which may be finite or not, which are placed in a row of cells. This sequence is called the initial generation and the Z Z -rule is applied sequentially on each two consecutive terms of 𝒢 i ​ n {\mathcal{G}_{in}}. Whence, a new generation is born and its cells are placed in the following row. Usually, in graphic representations, we slightly shift to the right the new generation such that any new cell is placed in the middle under its parents. Repeating the process, we obtain a matrix T 𝒢 i ​ n T_{{\mathcal{G}_{in}}} with infinitely many rows if 𝒢 i ​ n {\mathcal{G}_{in}} is infinite. As the reproducing rule remains unchanged, the results depend only on the initial generations and we shall see that in this way a large variety of outcomes are produced.

The matrices of numbers T 𝒢 i ​ n T_{{\mathcal{G}_{in}}} have lots of features of which some are similar to the objects created by the abelian sandpile model proposed by Bak, Tang and Wiesenfeld [1]. The intensely studied model, also called the chip-firing game, was surveyed by Levine and Propp [27]. Our Z Z -model also captures features of other evolutionary systems such as the Ducci-type game [7], [9], [8], [6], [22], [5], [24], [2], the numerical ensembles created by median insertions, such as those related to Pascal triangle [19] [20], [34], [35], [36], [37], [12] or the Farey sequences [10], [11]. For many initial generations 𝒢 i ​ n {\mathcal{G}_{in}}, the matrices T 𝒢 i ​ n T_{{\mathcal{G}_{in}}} show complex self-similar structures, like those of some particular abelian sandpile states [28], [3], [4], [38] or the outcomes produced in the related rotor-router model [32], [25], [33].

A special feature of matrices T 𝒢 i ​ n T_{\mathcal{G}_{in}} is the fact that they can be localized. For any prime p p, the p p -tomography is the matrix of citadels of T 𝒢 i ​ n T_{\mathcal{G}_{in}} in which all towers, except the towers associated to p p, are deleted. Then T 𝒢 i ​ n T_{{\mathcal{G}_{in}}} is the superposition (the element-wise multiplication) of the p p -tomographies for all primes p p, since the evolution according to the Z Z -rule is independent to one another.

We have already proved in [13] that the Z Z -rule produces objects with a fractal aspect if 𝒢 i ​ n {\mathcal{G}_{in}} is the sequence of prime numbers or its localized slice, the sequence of zeros except one term that is equal to a prime p p. In this article we show that this also happens if the initial generation is the p p -spaced sequence 𝒜 p = { 𝔭 n } n ≥ 1 \mathcal{A}_{p}=\{\mathfrak{p}_{n}\}_{n\geq 1}, where

 | 𝔭 n = { p if p | n, 0 else, \begin{split}\mathfrak{p}_{n}=\begin{cases}p\quad&\text{if $p\mid n$,}\\ 0\quad&\text{else,}\end{cases}\end{split} |  | (1.2) |

or 𝒱 p = { 𝔮 n } n ≥ 1 \mathcal{V}_{p}=\{\mathfrak{q}_{n}\}_{n\geq 1}, the p p -section of positive integers,

 | 𝔮 n = { p v p ​ ( n) if p | n, 0 else, \begin{split}\mathfrak{q}_{n}=\begin{cases}p^{v_{p}(n)}\quad&\text{if $p\mid n$,}\\ 0\quad&\text{else,}\end{cases}\end{split} |  | (1.3) |

where v p ​ ( n) v_{p}(n) is the p p -valuation of n n, which is, the power of p p into the prime decomposition of n n. The classic Sierpinski fractal appears if p = 2 p=2 (a finite fragment is shown in Figure 3), while more complex self-similar patterns are typical for larger primes (see Figures 5 – 7). Always, in a graphical representation, we present only a triangular region of T 𝒢 i ​ n T_{\mathcal{G}_{in}}, the one composed by the cells born in future generations from the part of 𝒢 i ​ n {\mathcal{G}_{in}} shown on the first row.

 | 1 2 3 4 5 6 7 8 9 10 11 12 ⋯ 2 6 12 20 30 42 56 72 90 110 132 ⋯ 3 2 15 6 35 12 63 20 99 30 ⋯ 6 30 10 210 420 84 1260 1980 330 ⋯ 5 3 21 2 5 15 77 6 ⋯ 15 7 42 10 3 1155 462 ⋯ 105 6 105 30 385 10 ⋯ 70 70 14 462 154 ⋯ 1 5 33 3 ⋯ 5 165 11 ⋯ 33 15 ⋯ 55 ⋯ ⋯ \begin{array}[]{ccccccccccccccccccccccccc}\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}&\makebox[8.92514pt]{$$}\\ \textbf{1}&&2&&3&&4&&5&&6&&7&&8&&9&&10&&11&&12&&\cdots\\ &\textbf{2}&&6&&12&&20&&30&&42&&56&&72&&90&&110&&132&&\cdots&\\ &&\textbf{3}&&2&&15&&6&&35&&12&&63&&20&&99&&30&&\cdots&&\\ &&&\textbf{6}&&30&&10&&210&&420&&84&&1260&&1980&&330&&\cdots&&&\\ &&&&\textbf{5}&&3&&21&&2&&5&&15&&77&&6&&\cdots&&&&\\ &&&&&\textbf{15}&&7&&42&&10&&3&&1155&&462&&\cdots&&&&&\\ &&&&&&\textbf{105}&&6&&105&&30&&385&&10&&\cdots&&&&&&\\ &&&&&&&\textbf{70}&&70&&14&&462&&154&&\cdots&&&&&&&\\ &&&&&&&&\textbf{1}&&5&&33&&3&&\cdots&&&&&&&&\\ &&&&&&&&&\textbf{5}&&165&&11&&\cdots&&&&&&&&&\\ &&&&&&&&&&\textbf{33}&&15&&\cdots&&&&&&&&&&\\ &&&&&&&&&&&\textbf{55}&&\cdots&&&&&&&&&&&\\ &&&&&&&&&&&&{\boldsymbol{\cdots}}&&&&&&&&&&&&\\ \end{array} |  |

Figure 1. The matrix T ℕ ∗ T_{{\mathbb{N}^{*}}}. After the first generation, the rows are shifted to the right so that any child is placed in the middle, under its parents.

A fundamental problem raised by the Z Z -model concerns the shape and properties of the matrix grown from the first generation ℕ ∗ {\mathbb{N}^{*}}. Its north-west corner is shown in Figure 1. The p p -tomographies of T ℕ ∗ T_{\mathbb{N}^{*}} can be grown individually, by starting in the first row with the sequence 𝒱 p \mathcal{V}_{p}. Of particular interest are questions related to the geometrical figures propagated from the cell p g, g ≥ 2 p^{g},\ g\geq 2. For any prime p p and integer g ≥ 2 g\geq 2, we denote by 𝔖 ⁡ ( p, g) \mathfrak{S}(p,g) the collection of connected cells that starts from p g p^{g} and contains only powers of p p larger than two. We call these figures Z Z -solitons and present two of them in Figure 2. Unlike the set of cells containing powers of p p less than two, which forms a continuous texture all over the infinite matrix T ℕ ∗ T_{\mathbb{N}^{*}}, the solitons are larger and larger with the power g g, but finite.

[image: Refer to caption]

[image: Refer to caption]

Figure 2. The solitons 𝔖 ⁡ ( p, n) \mathfrak{S}(p,n) generated by the cells p 14 p^{14} with p = 13 p=13 and p = 17 p=17.
Code of colors for the cells containing the powers of p p from 0 0 to 14 14:

###### Conjecture 1.

Two distinct solitons 𝔖 ⁡ ( p, g 1) \mathfrak{S}(p,g_{1}), 𝔖 ⁡ ( p, g 2) \mathfrak{S}(p,g_{2}), neither overlap nor touch each other.

The characterization problem of the evolution of shape and size of the solitons for different p p and growing g g is the analog of the limiting shape problems studied in [21], [17], [25], [26], [18]. The solitons 𝔖 ⁡ ( 2, g) \mathfrak{S}(2,g) verify Conjecture 1, as follows from their complete description presented in Section 3. For odd primes, 𝔖 ⁡ ( p, g) \mathfrak{S}(p,g) are more complex, with an aspect of certain fringed parts of Sierpinski triangles. For a fixed prime p p, the series of solitons 𝔖 ⁡ ( p, g) \mathfrak{S}(p,g), as g g increases, offers an intriguing spectacle and their growth appears to be proportional, as in the analog case of the abelian sandpiles [31], [15], [16], [14].

Another zone of interest is the first column or the west edge of matrix T 𝒢 i ​ n T_{\mathcal{G}_{in}}. We denote this sequence by W 𝒢 i ​ n W_{\mathcal{G}_{in}}. The western edge can be viewed as the projection of 𝒢 i ​ n {\mathcal{G}_{in}} through the entire Z Z -process. Notice that the value of the m m -th citadel on W 𝒢 i ​ n W_{\mathcal{G}_{in}} is influenced by the values of all first m m citadels of 𝒢 i ​ n {\mathcal{G}_{in}} and by neither of the others. An example is the western frontier of the triangle in Figure 1:

 | W ℕ ∗: 1, 2, 3, 6, 5, 15, 105, 70, 1, 5, 33, 55, 65, 273, 1001, … \begin{split}W_{\mathbb{N}^{*}}:\ 1,2,3,6,5,15,105,70,1,5,33,55,65,273,1001,\dots{}\end{split} |  |

Various evidence obtained by computer verifications suggest that no square of any prime divides a term of this sequence. In other words, no soliton grows as large as to touch the western edge W ℕ ∗ W_{\mathbb{N}^{*}}. Corollary 2 shows that this is true for solitons 𝔖 ⁡ ( 2, g) \mathfrak{S}(2,g), g ≥ 2 g\geq 2.

At the exponents level, this is the counterpart of the Gilbreath’s Conjecture [23, A10], [30], which refers to the similar process that starts with the sequence of primes as 𝒢 i ​ n {\mathcal{G}_{in}} and grows the future generations with children born by taking the absolute difference of their parents. The Gilbreath’s Conjecture says that the west edge of the triangle composed of these rows of successive gaps of gaps, contains only ones.

Another example extending this widespread property [30] is the matrix that starts with the sequence of Sophie Germain primes † †\dagger † †\dagger † \dagger A positive integer p p is a Sophie Germain prime if p p and 2 ​ p + 1 2p+1 are primes at the same time. and is generated in the same way, listing successively the gaps from the previous row of gaps. For this matrix, John W. Layman [29, A080209] observed and conjectured that the left edge consists only of 1 1 s and 3 3 s.

In our multiplicative setting, we conjecture that the maximal power of any prime that appears in the decomposition of the numbers situated on the left edge of T ℕ ∗ T_{{\mathbb{N}^{*}}} is one.

###### Conjecture 2 (Section 9 [12]).

The left edge of the infinite triangle generated by the iterated application of the Z Z -rule to the set of positive integers contain only square free numbers.

The object of Sections 4 – 6 is to compare and analyze the similarities between T ℕ ∗ T_{\mathbb{N}^{*}} and an analogue matrix that has no solitons. The p p -tomographies of this new matrix are generated by sequence 𝒜 p \mathcal{A}_{p} and in Theorem 2 we show that these tomographies are eventually periodic for all p p. Furthermore, we observe the closeness of the citadels on the western side of the two matrices and in Theorem 3 we characterize the structure of the sinuous series of extreme values of the western edge of the matrix with no solitons.

Theorem 1 gives a complete characterization of the 2 2 -tomography of matrix T ℕ ∗ T_{\mathbb{N}^{*}}. In particular, it shows that there are no fours on the western edge of T ℕ ∗ T_{\mathbb{N}^{*}}, solving a problem raised by N. J. A. Sloane [29, A222313]. Our analysis in Sections 4 – 6 allows us to formulate the precise Conjecture 3 regarding another problem raised by Sloane [29, A222313], [13, Question 3].

## 2. Notations

Starting with a sequence of integers 𝒮 = { s 1, s 2, … } \mathcal{S}=\{s_{1},s_{2},\dots\}, we consider the matrix whose first row is 𝒮 \mathcal{S} and the following ones are generated with the Z Z -rule. We denote this matrix by T 𝒮 = ( t j, k) 1 ≤ j, k T_{\mathcal{S}}=(t_{j,k})_{1\leq j,k}, where t 1, 1 = s 1 t_{1,1}=s_{1}, t 1, 2 = s 2, … t_{1,2}=s_{2},\dots and

 | t j, k = Z ⁡ ( t j − 1, k, t j − 1, k + 1), for ​ 2 ≤ j, 1 ≤ k. t_{j,k}=Z(t_{j-1,k},t_{j-1,k+1}),\ \text{ for}\ 2\leq j,\ 1\leq k. |  |

If the initial sequence is a finite ordered set 𝒮 = { s 1, …, s K } \mathcal{S}=\{s_{1},\dots,s_{K}\}, we obtain the numerical triangle

 | T 𝒮 ( K) = { t j, k: 1 ≤ j ≤ K, 1 ≤ k ≤ K − j + 1 }, T_{\mathcal{S}}(K)=\big\{t_{j,k}\ \colon\ 1\leq j\leq K,\ 1\leq k\leq K-j+1\big\}, |  |

whose first row is t 1, 1 = s 1 t_{1,1}=s_{1}, t 1, 2 = s 2, …, t 1, K = s K t_{1,2}=s_{2},\dots,t_{1,K}=s_{K}, and following ones are generated recursively by

 | t j, k = Z ⁡ ( t j − 1, k, t j − 1, k + 1), for 2 ≤ j ≤ K and 1 ≤ k ≤ K − j + 1. t_{j,k}=Z(t_{j-1,k},t_{j-1,k+1}),\quad\text{for $2\leq j\leq K$ and $1\leq k\leq K-j+1$.} |  |

We say that t j, k = Z ⁡ ( t j − 1, k, t j − 1, k + 1) t_{j,k}=Z(t_{j-1,k},t_{j-1,k+1}), for j ≥ 2 j\geq 2, is the child of its parents t j − 1, k t_{j-1,k} and t j − 1, k + 1 t_{j-1,k+1} and in pictures we usually place the child in the middle, below its parents.

The j j -th row of the matrix is called the j j -th generation and we denote it by

 | G 𝒮 ​ ( j) = { t j, k: 1 ≤ k } and G 𝒮 ​ ( j, K) = { t j, k: 1 ≤ k ≤ K }, for j ≥ 1. G_{\mathcal{S}}(j)=\big\{t_{j,k}\ \colon\ 1\leq k\big\}\quad\text{and}\quad G_{\mathcal{S}}(j;K)=\big\{t_{j,k}\ \colon\ 1\leq k\leq K\big\}\,,\quad\text{for $j\geq 1$}\,. |  |

We denote the west-side of the triangle by

 | W 𝒮 = { t j, 1: 1 ≤ j } and W 𝒮 ​ ( K) = { t j, 1: 1 ≤ j ≤ K }. W_{\mathcal{S}}=\big\{t_{j,1}\ \colon\ 1\leq j\big\}\quad\text{and}\quad W_{\mathcal{S}}(K)=\big\{t_{j,1}\ \colon\ 1\leq j\leq K\big\}\,. |  |

The evolution at the exponents level is presented into the following tables:

 | v p ​ ( T 𝒮) = { v p ( t j, k): 1 ≤ j, k }, v p ​ ( T 𝒮 ​ ( K)) = { v p ( t j, k): 1 ≤ j ≤ K, 1 ≤ k ≤ K − j + 1 }. \begin{split}v_{p}(T_{\mathcal{S}})&=\big\{v_{p}(t_{j,k})\ \colon\ 1\leq j,k\big\},\\ v_{p}(T_{\mathcal{S}}(K))&=\big\{v_{p}(t_{j,k})\ \colon\ 1\leq j\leq K,\ 1\leq k\leq K-j+1\big\}.\end{split} |  |

Given an infinite matrix T 𝒮 T_{\mathcal{S}} or a bounded triangle T 𝒮 ​ ( K) T_{\mathcal{S}}(K), we denote their p p - tomography (also called the p p -slice or the p p -section) by

 | T 𝒮, p = { p v p ​ ( t j, k): 1 ≤ j, k }, T 𝒮, p ​ ( K) = { p v p ​ ( t j, k): 1 ≤ j ≤ K, 1 ≤ k ≤ K − j + 1 }. \begin{split}T_{\mathcal{S},p}&=\big\{p^{v_{p}(t_{j,k})}\ \colon\ 1\leq j,k\big\},\\ T_{\mathcal{S},p}(K)&=\big\{p^{v_{p}(t_{j,k})}\ \colon\ 1\leq j\leq K,\ 1\leq k\leq K-j+1\big\}.\end{split} |  |

Thus, the superposition of all p p -slices recovers the full matrix:

 | T 𝒮 = ∏ p T 𝒮, p and T 𝒮 ​ ( K) = ∏ p T 𝒮, p ​ ( K), \begin{split}T_{\mathcal{S}}=\prod_{p}T_{\mathcal{S},p}\quad\text{and}\quad T_{\mathcal{S}}(K)=\prod_{p}T_{\mathcal{S},p}(K),\end{split} |  |

where the product over all primes p p is taken component-wise.

For any positive integer n n, we denote by p ⁡ ( n) p(n) the largest square free number that divides n n, and by ℙ \mathbb{P} the sequence of these numbers:

 | p ( n) = ∏ p | n p, ℙ = { p ( n): n ∈ ℕ }. \begin{split}p(n)=\prod_{p|n}p,\qquad\mathbb{P}=\{p(n):n\in\mathbb{N}\}\,.\end{split} |  | (2.1) |

We denote by 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] the ring of meromorphic series of variable X X and coefficients in the field with two elements 𝔽 2 \mathbb{F}_{2} and by 𝔽 2 ​ [[X]] ∗ ⊂ 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]]^{*}\subset\mathbb{F}_{2}[[X]] the collection of series that are sums of monomials X k X^{k} with k ≥ 1 k\geq 1, only.

As usual, the number of distinct prime factors of n n is denoted by ω ⁡ ( n) \omega(n) and the notation for the multiplicative order of a a modulo p p is ind p ⁡ ( a) \operatorname{ind}_{p}(a).

## 3. The 2 2 -tomography of T ℕ ∗ T_{\mathbb{N}^{*}}

The real action on T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2} is on the exponents level and, to understand its result, we need to formalize it. Let ℕ + \mathbb{N}^{+} denote the collection of nonempty finite words over the infinite alphabet ℕ \mathbb{N}. We introduce the following sequence of words in ℕ + \mathbb{N}^{+}, defined recursively:

 | x 1 = 0, x n = x n − 1 + ⁣ + ( n − 1) + ⁣ + x n − 1, for n ≥ 2, x_{1}=0,\quad x_{n}=x_{n-1}\mathbin{+\mkern-10.0mu+}(n-1)\mathbin{+\mkern-10.0mu+}x_{n-1},\ \ \text{for $n\geq 2$}, |  |

where “ + ⁣ + \mathbin{+\mkern-10.0mu+} ” denotes the concatenation of integers. Note that x n x_{n} is the concatenation of 2 n − 1 2^{n}-1 integers. Since x n x_{n} is an initial sub-word of x n + 1 x_{n+1}, for all n ≥ 1 n\geq 1, there exists a limit sequence 𝐰 0: ℕ ∗ → ℕ \mathbf{w}_{0}:{\mathbb{N}^{*}}\rightarrow\mathbb{N}, whose first 2 n − 1 2^{n}-1 terms coincides with the letters of x n x_{n}, for n ≥ 1 n\geq 1. We write: 𝐰 0 = lim → ⁡ x n \mathbf{w}_{0}=\varinjlim x_{n}.

Similarly, starting with 1 1 instead of 0 0, we define the sequence of words

 | y 1 = 1, y n = y n − 1 + ⁣ + n + ⁣ + y n − 1, for n ≥ 2 y_{1}=1,\quad y_{n}=y_{n-1}\mathbin{+\mkern-10.0mu+}n\mathbin{+\mkern-10.0mu+}y_{n-1},\ \ \text{for $n\geq 2$} |  |

and obtain the limit sequence 𝐰 1 = lim → ⁡ y n \mathbf{w}_{1}=\varinjlim y_{n}, whose first 2 n − 1 2^{n}-1 terms coincides with the letters of y n y_{n}, for n ≥ 1 n\geq 1.

The first terms of 𝐰 0 \mathbf{w}_{0} and 𝐰 1 \mathbf{w}_{1} are:

 | 𝐰 0: 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4, … 𝐰 1: 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, … \begin{split}\mathbf{w}_{0}:&\ \ 0,1,0,2,0,1,0,3,0,1,0,2,0,1,0,4,\dots\\ \mathbf{w}_{1}:&\ \ 1,2,1,3,1,2,1,4,1,2,1,3,1,2,1,5,\dots\end{split} |  |

For a given sequence a: ℕ ∗ → ℕ a:{\mathbb{N}^{*}}\rightarrow\mathbb{N}, we denote by α ⁡ ( a) = { α n } n ≥ 1 \alpha(a)=\{\alpha_{n}\}_{n\geq 1} the sequence of absolute differences between consecutive terms:

 | α n = | a n + 1 − a n |, for ​ n ≥ 1 \alpha_{n}=|a_{n+1}-a_{n}|,\quad\text{for}\ n\geq 1 |  |

and by β ⁡ ( a) = { β n } n ≥ 1 \beta(a)=\{\beta_{n}\}_{n\geq 1} the bubbled sequence, defined by

 | β 2 ​ n − 1 = β 2 ​ n = a n, for ​ n ≥ 1. \beta_{2n-1}=\beta_{2n}=a_{n},\quad\text{for}\ n\geq 1\,. |  |

We use the same notations for the similar operations applied on words, where the action is on the the sequences of their letters. For example: α ⁡ ( x 2) = α ⁡ ( 010) = 11 \alpha(x_{2})=\alpha(010)=11 and β ⁡ ( y 2) = β ⁡ ( 121) = 112211 \beta(y_{2})=\beta(121)=112211.

[image: Refer to caption] Figure 3. The tomography of T ℕ ∗ ​ ( 129) T_{{\mathbb{N}^{*}}}(129) for p = 2 p=2. Notice that the larger solitons are further and further away from the western edge of T ℕ ∗ T_{{\mathbb{N}^{*}}}.
Code of colors for the cells containing the powers of 2 2 from 0, …, 7 0,\dots,7:

The next lemma shows how 𝐰 0 \mathbf{w}_{0} and 𝐰 1 \mathbf{w}_{1} relates to one another through these operations.

###### Lemma 1.

The following properties hold true:

1. (1)

𝐰 1 = 𝐰 0 + 1 \mathbf{w}_{1}=\mathbf{w}_{0}+1, with element-wise addition;

2. (2)

𝐰 0 = v 2 ​ ( ℕ ∗) \mathbf{w}_{0}=v_{2}({\mathbb{N}^{*}}), with term-wise application of the valuation v 2 v_{2};

3. (3)

𝐰 1 = v 2 ​ ( 2 ​ ℕ ∗) \mathbf{w}_{1}=v_{2}(2{\mathbb{N}^{*}});

4. (4)

α ⁡ ( 𝐰 0) = α ⁡ ( 𝐰 1) = β ⁡ ( 𝐰 1) \alpha(\mathbf{w}_{0})=\alpha(\mathbf{w}_{1})=\beta(\mathbf{w}_{1}).

###### Proof.

(1) The equality 𝐰 1 = 𝐰 0 + 1 \mathbf{w}_{1}=\mathbf{w}_{0}+1 follows directly from the definitions.

(2) We prove the equality by induction. The initial step: 𝐰 0 ​ ( 1) = 0 = v 2 ​ ( 1) \mathbf{w}_{0}(1)=0=v_{2}(1). Now, suppose that 𝐰 0 ​ ( n) = v 2 ​ ( n) \mathbf{w}_{0}(n)=v_{2}(n) for all n ∈ { 1, 2, …, 2 k − 1 } n\in\{1,2,\dots,2^{k}-1\}. Then v 2 ​ ( 2 k) = k v_{2}(2^{k})=k and v 2 ​ ( 2 k + m) = v 2 ​ ( m) v_{2}(2^{k}+m)=v_{2}(m), for all m ∈ { 1, 2, …, 2 k − 1 } m\in\{1,2,\dots,2^{k}-1\}, by the definition of the valuation. Using the definition of 𝐰 0 \mathbf{w}_{0}, this means that 𝐰 0 ​ ( n) = v 2 ​ ( n) \mathbf{w}_{0}(n)=v_{2}(n), for n ∈ { 1, 2, …, 2 k + 1 − 1 } n\in\{1,2,\dots,2^{k+1}-1\}, as needed.

(3) 𝐰 1 = v 2 ​ ( 2 ​ ℕ ∗) \mathbf{w}_{1}=v_{2}(2{\mathbb{N}^{*}}) follows from (1) and (2).

(4) The equality α ⁡ ( 𝐰 0) = α ⁡ ( 𝐰 1) \alpha(\mathbf{w}_{0})=\alpha(\mathbf{w}_{1}) also follows directly from (1) and the definition of α ⁡ ( ⋅) \alpha(\cdot). So it remains to prove that α ⁡ ( 𝐰 1) = β ⁡ ( 𝐰 1) \alpha(\mathbf{w}_{1})=\beta(\mathbf{w}_{1}). We proceed by induction.

The initial step: applying α ⁡ ( ⋅) \alpha(\cdot) to the finite sequence 1, 2, 1 1,2,1 (which are the letters of y 2 y_{2}, the beginning of 𝐰 1 \mathbf{w}_{1}), we get 1, 1 1,1, the beginning of β ⁡ ( 𝐰 1) \beta(\mathbf{w}_{1}) or, with the notation on words, α ⁡ ( y 2) = α ⁡ ( 121) = 11 = β ⁡ ( y 1) \alpha(y_{2})=\alpha(121)=11=\beta(y_{1}).

The induction step: suppose that α ⁡ ( y n) = β ⁡ ( y n − 1) \alpha(y_{n})=\beta(y_{n-1}). Then

 | α ⁡ ( y n + 1) = α ⁡ ( y n + ⁣ + ( n + 1) + ⁣ + y n) = β ⁡ ( y n − 1) + ⁣ + n + ⁣ + n + ⁣ + β ⁡ ( y n − 1) = β ⁡ ( y n), \begin{split}\alpha(y_{n+1})=\alpha(y_{n}\mathbin{+\mkern-10.0mu+}(n+1)\mathbin{+\mkern-10.0mu+}y_{n})=\beta(y_{n-1})\mathbin{+\mkern-10.0mu+}n\mathbin{+\mkern-10.0mu+}n\mathbin{+\mkern-10.0mu+}\beta(y_{n-1})=\beta(y_{n}),\end{split} |  |

since the last and the first letters of y n − 1 y_{n-1} are equal to 1 1. This completes the proof of the lemma. ∎

Thus, by Lemma 1 we see that the sequences of gaps between consecutive terms of 𝐰 0 \mathbf{w}_{0} and 𝐰 1 \mathbf{w}_{1} both coincide with the bubbled sequence

 | β ( 𝐰 1): 1, 1, 2, 2, 1, 1, 3, 3, 1, 1, 2, 2, 1, 1, 4, 4, 1, 1, 2, 2, 1, 1, 3, 3, 1, 1, 2, 2, 1, 1, 5, 5, … \begin{split}\beta(\mathbf{w}_{1}):1,1,2,2,1,1,3,3,1,1,2,2,1,1,4,4,1,1,2,2,1,1,3,3,1,1,2,2,1,1,5,5,\dots{}\end{split} |  |

With the above notations, we see that the sequence of exponents of 2 2 on the first row of T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2} coincides with 𝐰 0 \mathbf{w}_{0}. Then, by Lemma 1, it follows that the subsequent sequences of exponents of 2 2 on the following rows of T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2} are: α ⁡ ( 𝐰 0), α ( 2) ​ ( 𝐰 0), α ( 3) ​ ( 𝐰 0), … \alpha(\mathbf{w}_{0}),\alpha^{(2)}(\mathbf{w}_{0}),\alpha^{(3)}(\mathbf{w}_{0}),\dots In general, the m m th row of T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2} is

 | 2 α ( m − 1) ​ ( 𝐰 0) ​ ( 1), 2 α ( m − 1) ​ ( 𝐰 0) ​ ( 2), 2 α ( m − 1) ​ ( 𝐰 0) ​ ( 3), …, for m ≥ 1. \begin{split}2^{\alpha^{(m-1)}(\mathbf{w}_{0})(1)},\ 2^{\alpha^{(m-1)}(\mathbf{w}_{0})(2)},\ 2^{\alpha^{(m-1)}(\mathbf{w}_{0})(3)},\ \dots,\quad\text{for $m\geq 1$.}\end{split} |  |

Now we can describe the structure of the matrix of the exponents v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}), which corresponds explicitly to the explicit description of the 2 2 -tomography of T ℕ ∗ T_{\mathbb{N}^{*}}. Its initial cut-off triangle T ℕ ∗, 2 ​ ( 129) T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2}(129), composed of 129 129 rows, is shown in Figure 3. We see that, geometrically, it is part of an infinite Sierpinski triangle. Notice that the horizontal rows are grouped naturally in slices containing sequences of pairs of triangles. The couple of triangles in each pair is colored with the same color and the change of colors from a pair to another corresponds to the change of numbers in the sequence β ⁡ ( 𝐰 1) \beta(\mathbf{w}_{1}).

The sequence of slices { S k } k ≥ 0 \{S_{k}\}_{k\geq 0} in which v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}) is partitioned are larger and larger in size. The slice S 0 S_{0} is just the first row and it is exceptional. The next slice, S 1 S_{1}, is the second row. Then, for any k ≥ 2 k\geq 2, the slice S k S_{k} groups 2 k − 1 2^{k-1} rows, those from the ( 2 k − 1 + 1) (2^{k-1}+1) th till the 2 k 2^{k} th.

In any slice, the largest triangles formed by cells of the same color are the top rows of the Pascal arithmetic triangle modulo 2 2, with the odd entries replaced by a certain positive integer. Such a triangle depends on two parameters: the height h h and the weight t t, which is the value of the non-zero entries. We denote it by P 2 ​ ( h, t) P_{2}(h,t) (see the left triangle in Figure 4 for such an example).

Triangle P 2 ​ ( h, t) P_{2}(h,t) is generated as Pascal’s classic triangle, by starting from the top with a symbolic variable t t, which satisfies the rule t + t = 0 t+t=0. The same result is obtained if the top is placed somewhere in a row of zeros (see the matrix from the right-side of Figure 4).

 | 10 10 10 10 0 10 10 10 10 10 10 0 0 0 10 10 10 0 0 10 10 10 0 10 0 10 0 10 \begin{array}[]{ccccccccccccc}&&&&&&10&&&&&&\\ &&&&&10&&10&&&&&\\ &&&&10&&0&&10&&&&\\ &&&10&&10&&10&&10&&&\\ &&10&&0&&0&&0&&10&&\\ &10&&10&&0&&0&&10&&10&\\ 10&&0&&10&&0&&10&&0&&10\\ \end{array} |  |

 | ⋅ ⋅ ⋅ 0 0 0 0 t 0 0 0 0 ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ 0 0 0 t t 0 0 0 ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ 0 0 t 0 t 0 0 ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ 0 t t t t 0 ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ t 0 0 0 t ⋅ ⋅ ⋅ \begin{array}[]{ccccc ccccc c ccccc ccccc}\!\!\!\!\cdot\!\cdot\!\cdot&&0&&0&&0&&0&&t&&0&&0&&0&&0&&\ \,\!\!\!\!\cdot\!\cdot\!\cdot\\ &\!\!\!\!\cdot\!\cdot\!\cdot&&0&&0&&0&&t&&t&&0&&0&&0&&\!\!\!\!\cdot\!\cdot\!\cdot&\\ &&\!\!\!\!\cdot\!\cdot\!\cdot&&0&&0&&t&&0&&t&&0&&0&&\!\!\!\!\cdot\!\cdot\!\cdot&&\\ &&&\!\!\!\!\cdot\!\cdot\!\cdot&&0&&t&&t&&t&&t&&0&&\!\!\!\!\cdot\!\cdot\!\cdot&&&\\ &&&&\!\!\!\!\cdot\!\cdot\!\cdot&&t&&0&&0&&0&&t&&\!\!\!\!\cdot\!\cdot\!\cdot&&&&\\ \end{array} |  |

Figure 4. Left: The triangle P 2 ​ ( 7, 10) P_{2}(7,10) of height 7 7 and weight 10 10.
Right: A triangle P 2 ​ ( 5, t) P_{2}(5,t) generated by a single non-zero cell of weight t t placed in the center of a string of zeros of length at least 4 + 1 + 4 = 9 4+1+4=9.

###### Lemma 2.

Let h h be a positive integer and let t t be a formal variable. Let 𝐮 = { u k } k ≥ 1 \mathbf{u}=\{u_{k}\}_{k\geq 1} be a sequence of zeros, except one term u n = t u_{n}=t and suppose that n ≥ h n\geq h. Then, the matrix with rows 𝐮, α ⁡ ( 𝐮), α ( 2) ​ ( 𝐮) ​ …, α ( h − 1) ​ ( 𝐮) \mathbf{u},\alpha(\mathbf{u}),\alpha^{(2)}(\mathbf{u})\dots,\alpha^{(h-1)}(\mathbf{u}) contains triangle P 2 ​ ( h, t) P_{2}(h,t).

###### Proof.

It suffices to note that condition h ≤ n h\leq n ensures that the object that develops from u n = t u_{n}=t is not influenced by external obstacles and the operation of taking the absolute value of the difference acts on { 0, t } \{0,t\} exactly as the operation that grows a Pascal triangle with entries in 𝔽 2 \mathbb{F}_{2}.

∎

We summarize the complete description of v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}) (respectively T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2}) in the next theorem.

###### Theorem 1.

(1) Slice S 0 S_{0} of the matrix v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}) is sequence 𝐰 0 \mathbf{w}_{0}. The next rows of v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}) are grouped in slices S k S_{k}, such that, for any k ≥ 1 k\geq 1, slice S k S_{k} is formed by rows from the ( 2 k − 1 + 1) (2^{k-1}+1) th till the 2 k 2^{k} th. (2) The single row of S 1 S_{1} is sequence α ⁡ ( 𝐰 0) = β ⁡ ( 𝐰 1) \alpha(\mathbf{w}_{0})=\beta(\mathbf{w}_{1}). (3) For any k ≥ 1 k\geq 1, the collection of non-zero elements in slice S k S_{k} is the union of triangles P 2 ​ ( 2 k − 1, t) P_{2}(2^{k-1},t) and the sequence of their weights (from left to right) coincides with β ⁡ ( 𝐰 1) \beta(\mathbf{w}_{1}). The top vertices of these triangles are on the first row of the slice and their bases are adjacent and partition the bottom row.

###### Proof.

(1) follows by the definitions. (2) is proved in Lemma 1. (3) The proof is by induction. The initial step, k = 1 k=1, coincides with (2).

Suppose now that the stated description is valid for slice S k S_{k} and let as look on S k + 1 S_{k+1}. We begin with the first row of S k + 1 S_{k+1}. Here, the first 2 ⋅ 2 k − 1 − 1 2\cdot 2^{k-1}-1 cells are zeros, because, by the induction hypothesis, on the previous row, the first 2 ⋅ 2 k − 1 2\cdot 2^{k-1} cells where the adjacent bases of two triangles P 2 ​ ( 2 k − 1, 1) P_{2}(2^{k-1},1). The next element, the 2 ⋅ 2 k − 1 2\cdot 2^{k-1} th, is 1 = | 1 − 2 | 1=|1-2|, since on the previous slice, the weight of the second triangle was 1 1 and the weight of the third triangle is 2 2. Continuing in the same way, we see that the next non-zero cell on the first row of slice S k + 1 S_{k+1} is the 4 ⋅ 2 k − 1 4\cdot 2^{k-1} th and its value is equal with 1 = | 2 − 1 | 1=|2-1|. In this way we see that the non-zero cells on the first row of slice S k + 1 S_{k+1} are those obtained as absolute differences of the parent cells that are vertices of neighbor triangles P 2 ​ ( 2 k − 1, t) P_{2}(2^{k-1},t) with different weights from the previous slice. These are the 2 k 2^{k} th, the 2 ⋅ 2 k 2\cdot 2^{k} th, the 3 ⋅ 2 k 3\cdot 2^{k} th, and so on. Moreover, by the induction hypothesis, the values of integers occupying these cells are the integers in the sequence β ⁡ ( 𝐰 1) \beta(\mathbf{w}_{1}).

Now, using Lemma 2, we find that from each of these cells, grows a triangle P 2 ​ ( 2 k, t) P_{2}(2^{k},t). Moreover, the weights of these triangles coincides with the integers on the non-zero cells in the first row of S k + 1 S_{k+1}. Also, the size of the slice assures that the bases of these triangles are adjacent. This concludes the proof of the induction step and of the theorem. ∎

In particular, Theorem 1 describes the western edge of the matrix T ℕ ∗, 2 T_{{\mathbb{N}^{*}}\mkern-3.0mu,\mkern 1.0mu2}.

###### Corollary 1.

The 2 2 -valuation of the elements of the west sequence W ℕ ∗ W_{\mathbb{N}^{*}} are:

 | v 2 ​ ( t ⁡ ( m, 1)) = { 1, m = 2 k, k ≥ 1 0, else. \begin{split}v_{2}\big(t(m,1)\big)=\begin{cases}1,&\ m=2^{k},\ k\geq 1\\ 0,&\ \text{else.}\end{cases}\end{split} |  |

Also, Theorem 1 answers to a question of N. J. A. Sloane, who asks whether there is a proof that 4 4 cannot appear on the western edge of the matrix T ℕ ∗ T_{\mathbb{N}^{*}} [29, A222313].

###### Corollary 2.

There is no 4 4 on W ⁡ ( T ℕ ∗) W(T_{\mathbb{N}^{*}}).

## 4. The description of T ℙ T_{\mathbb{P}}

The powers of all primes in the decomposition of the terms in the sequence

 | ℙ = { 1, 2, 3, 2, 5, 6, 7, 2, 3, 10, 11, 6, 13, 14, 15, 2, 17, 6, 19, … } \mathbb{P}=\{1,2,3,2,5,6,7,2,3,10,11,6,13,14,15,2,17,6,19,\dots\} |  |

defined in ( 2.1) are equal to one. This allows us to employ operations in the the ring of meromorphic series 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] to understand the structure of the p p -tomographies of T ℙ T_{\mathbb{P}}. Thus the initial generation of any p p -tomography is sequence 𝒜 p = { 𝔭 n } n ≥ 1 \mathcal{A}_{p}=\{\mathfrak{p}_{n}\}_{n\geq 1} defined by ( 1.2). The superposition (component-wise multiplication) of the p p -tomographies for all p p gives the full description of matrix T ℙ T_{\mathbb{P}}.

For any prime p p, we look at matrix v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}). Always, the first row is filled with zeros except the cells in the arithmetic progression k ​ p kp, k ≥ 1 k\geq 1, which are equal to 1 1. Again, the prime p = 2 p=2 is exceptional. The second row of v 2 ​ ( T ℙ) v_{2}(T_{\mathbb{P}}) has all cells equal to 1 1 and from the third row on, matrix v 2 ​ ( T ℙ) v_{2}(T_{\mathbb{P}}) is filled with zeros only.

We show that if p p is odd, the rows can be grouped in periodic slices. The number of rows in such a slice is a period of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) and we denote by π p \pi_{p} the length of the smallest period. If p = 2 p=2, the periodic slices contain just one row, which repeats from the third on. If p p is odd, the first row of the first periodic slice is always the second row of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}).

One can check the small periods for some primes: π 2 = 1 \pi_{2}=1, π 3 = 3 \pi_{3}=3, π 5 = 15 \pi_{5}=15, π 7 = 7 \pi_{7}=7, π 31 = 31 \pi_{31}=31, π 127 = 127 \pi_{127}=127. As p p increases, the size of π p \pi_{p} becomes large: π 11 = 341 \pi_{11}=341, π 13 = 819 \pi_{13}=819, π 17 = 255 \pi_{17}=255, π 19 = 9709 \pi_{19}=9709. This fact produces the general aspect of randomness of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}), for p ≥ 11 p\geq 11. Also, in some areas this phenomenon is more pronounced than in others (see Figure 5).

[image: Refer to caption]

[image: Refer to caption]

Figure 5. The tomographies v p ​ ( T ℙ ​ ( 100)) v_{p}(T_{\mathbb{P}}(100)), for p = 13 p=13 and p = 19 p=19.

Any sequence 𝐞 = { e k } k ≥ 1 ⊂ { 0, 1 } ℕ \mathbf{e}=\{e_{k}\}_{k\geq 1}\subset\{0,1\}^{\mathbb{N}} can be identified uniquely with a series in 𝔽 2 ​ [[X]] ∗ \mathbb{F}_{2}[[X]]^{*}. We use this identifications for the rows of the matrix v p ​ ( T ℙ, p) v_{p}(T_{\mathbb{P},p}) and write

 | 𝐞 = { e k } k ≥ 1 ⟷ θ θ 𝐞 ​ ( X) = ∑ k ≥ 1 e k ​ X k. \begin{split}\mathbf{e}=\{e_{k}\}_{k\geq 1}\stackrel{{\scriptstyle\theta}}{{\longleftrightarrow}}\theta_{\mathbf{e}}(X)=\sum_{k\geq 1}e_{k}X^{k}\,.\end{split} |  |

The operation of passing from one generation to the next by applying the Z ⁡ ( ⋅, ⋅) Z(\cdot,\cdot) -rule ( 1.1) transfers on the side of the series to multiplication by 1 + X X \frac{1+X}{X}. This may produce a series in 𝔽 2 ​ [[X]] ∖ 𝔽 2 ​ [[X]] ∗ \mathbb{F}_{2}[[X]]\setminus\mathbb{F}_{2}[[X]]^{*} and we need to bring it back by dropping the meromorphic part and the constant term through the Δ \Delta operation:

 | Δ ⁡ ( S ⁡ ( X)):= ∑ k ≥ 1 c k ​ X k ∈ 𝔽 2 ​ [[X]], for S ⁡ ( X) = ∑ c k ​ X k ∈ 𝔽 2 ​ [[X]]. \begin{split}\Delta(S(X)):=\sum_{k\geq 1}c_{k}X^{k}\in\mathbb{F}_{2}[[X]]\,,\quad\text{for $S(X)=\sum c_{k}X^{k}\in\mathbb{F}_{2}[[X]]$}\,.\end{split} |  |

Then, to pass from the j j th generation to the ( j + m) (j+m) th, we have to multiply repeatedly m m times by 1 + X X \tfrac{1+X}{X}, so the general correspondence is

 | [image: [Uncaptioned image]] \begin{split}\mathchoice{\raisebox{0.0pt}{\resizebox{1162251}{447828}{\hbox{$\displaystyle\includegraphics[]{DiagramaComutativa.png}$}}}}{\raisebox{0.0pt}{\resizebox{1162251}{447828}{\hbox{$\textstyle\includegraphics[]{DiagramaComutativa.png}$}}}}{\raisebox{0.0pt}{\resizebox{813579}{313481}{\hbox{$\scriptstyle\includegraphics[]{DiagramaComutativa.png}$}}}}{\raisebox{0.0pt}{\resizebox{581128}{223915}{\hbox{$\scriptscriptstyle\includegraphics[]{DiagramaComutativa.png}$}}}}\end{split} |  | (4.1) |

where α \alpha is the absolute value of the differences (which, in this case, coincides with addition in 𝔽 2 \mathbb{F}_{2}), taken component wise.

Next we show that this association is well defined.

###### Proposition 1.

The above association between the rows of the matrix v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) and the series in 𝔽 2 ​ [[X]] ∗ \mathbb{F}_{2}[[X]]^{*} and the operation of passing from one generation to the next is well defined, and diagram ( 4.1) is commutative.

###### Proof.

Well defining is due to the correspondence between the absence of columns to the left of the first column of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}), so there is no influence from the left when α \alpha is applied, and from ignoring of the meromorphic and constant terms of the series using the dropping function Δ \Delta.

It remains to prove that diagram ( 4.1) is commutative by induction. The initial step: Suppose 𝐞 j = ( e 1, e 2, e 3, …) \mathbf{e}_{j}=(e_{1},e_{2},e_{3},\dots). Then, on the one hand, we have:

 | α ⁡ ( 𝐞 j) = 𝐞 j + 1 = ( e 1 + e 2, e 2 + e 3, e 3 + e 4 ​ …), θ 𝐞 j + 1 ​ ( X) = ∑ k ≥ 1 ( e k + e k + 1) ​ X k, \begin{split}\alpha(\mathbf{e}_{j})=\mathbf{e}_{j+1}&=(e_{1}+e_{2},e_{2}+e_{3},e_{3}+e_{4}\dots)\,,\\ \theta_{\mathbf{e}_{j+1}}(X)&=\sum_{k\geq 1}(e_{k}+e_{k+1})X^{k},\end{split} |  | (4.2) |

and on the other hand

 | θ 𝐞 j ​ ( X) = ∑ k ≥ 1 e k ​ X k, 1 + X X ⋅ ∑ k ≥ 1 e k ​ X k = e 1 + ∑ k ≥ 1 ( e k + e k + 1) ​ X k, Δ ⁡ ( e 1 + ∑ k ≥ 1 ( e k + e k + 1) ​ X k) = ∑ k ≥ 1 ( e k + e k + 1) ​ X k. \begin{split}\theta_{\mathbf{e}_{j}}(X)&=\sum_{k\geq 1}e_{k}X^{k},\\ \tfrac{1+X}{X}\cdot\sum_{k\geq 1}e_{k}X^{k}&=e_{1}+\sum_{k\geq 1}(e_{k}+e_{k+1})X^{k},\\ \Delta\Big(e_{1}+\sum_{k\geq 1}(e_{k}+e_{k+1})X^{k}\Big)&=\sum_{k\geq 1}(e_{k}+e_{k+1})X^{k}\,.\end{split} |  | (4.3) |

The outcomes of ( 4.2) and ( 4.3) are identical, so the initial step is completed.

The induction step follows by using the associative property of the composition of functions Δ \Delta and multiplication by 1 + X X \tfrac{1+X}{X} and the fact that Δ ( 2) = Δ \Delta^{(2)}=\Delta. This completes the proof of the proposition.

∎

Let us see the periodicity of the matrix v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) in two particular cases.

### 4.1. Periodicity of v 3 ​ ( T ℙ) v_{3}(T_{\mathbb{P}})

The first row of v 3 ​ ( T ℙ) v_{3}(T_{\mathbb{P}}) contains only zeros, except the cells with ones in the columns with ranks in the arithmetic progression { 3 ​ n } n ≥ 1 \{3n\}_{n\geq 1}. The series that corresponds to the second row is

 | Δ ⁡ ( 1 + X X ⋅ ∑ k ≥ 1 X 3 ​ k) = ( X 2 + X 3) ​ ∑ k ≥ 0 X 3 ​ k. \begin{split}\Delta\Big(\tfrac{1+X}{X}\cdot\sum_{k\geq 1}X^{3k}\Big)&=(X^{2}+X^{3})\sum_{k\geq 0}X^{3k}.\end{split} |  | (4.4) |

Then the series that corresponds to the 5 5 th row is

 | Δ ⁡ ( ( 1 + X X) 5 − 2 ​ ( X 2 + X 3) ​ ∑ k ≥ 0 X 3 ​ k) = Δ ⁡ ( ( 1 + X + X 2 + X 3) ​ ( 1 + X X) ​ ∑ k ≥ 0 X 3 ​ k) = Δ ⁡ ( 1 + X 4 X ⋅ ∑ k ≥ 0 X 3 ​ k) = ( X 2 + X 3) ​ ∑ k ≥ 0 X 3 ​ k. \begin{split}\Delta\Big(\left(\tfrac{1+X}{X}\right)^{5-2}(X^{2}+X^{3})\sum_{k\geq 0}X^{3k}\Big)&=\Delta\Big((1+X+X^{2}+X^{3})\left(\tfrac{1+X}{X}\right)\sum_{k\geq 0}X^{3k}\Big)\\ &=\Delta\Big(\tfrac{1+X^{4}}{X}\cdot\sum_{k\geq 0}X^{3k}\Big)\\ &=(X^{2}+X^{3})\sum_{k\geq 0}X^{3k}.\end{split} |  | (4.5) |

Comparing ( 4.4) and ( 4.5), we see that the 2 2 nd and the 5 5 th rows coincide. Therefore, the matrix v 3 ​ ( T ℙ) v_{3}(T_{\mathbb{P}}) is eventually periodic and 3 3 is the length of a period.

### 4.2. Periodicity of v 5 ​ ( T ℙ) v_{5}(T_{\mathbb{P}})

The series that corresponds to the second row of v 5 ​ ( T ℙ) v_{5}(T_{\mathbb{P}}) is

 | Δ ⁡ ( 1 + X X ⋅ ∑ k ≥ 1 X 5 ​ k) = ( X 4 + X 5) ​ ∑ k ≥ 0 X 5 ​ k. \begin{split}\Delta\Big(\tfrac{1+X}{X}\cdot\sum_{k\geq 1}X^{5k}\Big)&=(X^{4}+X^{5})\sum_{k\geq 0}X^{5k}.\end{split} |  | (4.6) |

We take advantage of the fact that 15 15 is a special number and all the binomial coefficients ( 15 k) \binom{15}{k}, 0 ≤ k ≤ 15 0\leq k\leq 15, are odd. Then

 | ( 1 + X X) 15 ​ ( X 4 + X 5) ​ ∑ k ≥ 0 X 5 ​ k = ( 1 + X + ⋯ + X 15) ⋅ 1 + X X 11 ⋅ ∑ k ≥ 0 X 5 ​ k = 1 + X 16 X 11 ⋅ ∑ k ≥ 0 X 5 ​ k. \begin{split}\left(\tfrac{1+X}{X}\right)^{15}(X^{4}+X^{5})\sum_{k\geq 0}X^{5k}&=(1+X+\cdots+X^{15})\cdot\tfrac{1+X}{X^{11}}\cdot\sum_{k\geq 0}X^{5k}\\ &=\tfrac{1+X^{16}}{X^{11}}\cdot\sum_{k\geq 0}X^{5k}.\end{split} |  |

Dropping the meromorphic and the constant term, we find that

 | Δ ⁡ ( ( 1 + X X) 15 ​ ( X 4 + X 5) ​ ∑ k ≥ 0 X 5 ​ k) = Δ ⁡ ( 1 + X 16 X 11 ⋅ ∑ k ≥ 0 X 5 ​ k) = ( X 4 + X 5) ​ ∑ k ≥ 0 X 5 ​ k, \begin{split}\Delta\Big(\left(\tfrac{1+X}{X}\right)^{15}(X^{4}+X^{5})\sum_{k\geq 0}X^{5k}\Big)&=\Delta\Big(\tfrac{1+X^{16}}{X^{11}}\cdot\sum_{k\geq 0}X^{5k}\Big)\\ &=(X^{4}+X^{5})\sum_{k\geq 0}X^{5k},\end{split} |  |

which, compared with ( 4.6) shows that the 2 2 nd row coincides with the 16 16 th. Thus the matrix v 5 ​ ( T ℙ) v_{5}(T_{\mathbb{P}}) is eventually periodic and 15 15 is the length of a period. One can check that there is no shorter period. For this, it suffices to calculate the terms from the first column of the matrix v 5 ​ ( T ℙ) v_{5}(T_{\mathbb{P}}). The first 16 16 of them are:

 | v 5 ​ ( W ℙ ​ ( 16)) = { 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1 ⏟ the west-period }. v_{5}(W_{\mathbb{P}}(16))=\{0,\underbrace{0,0,0,1,1,1,1,0,1,0,1,1,0,0,1}_{\text{the west-period }}\}\,. |  |

### 4.3. Periodicity of v p ​ ( T ℙ), p v_{p}(T_{\mathbb{P}}),\ p odd

For a general p p, we can also take advantage of the fact that there are integers M M for which all the binomial coefficients ( M k) \binom{M}{k}, 0 ≤ k ≤ M 0\leq k\leq M are odd. Such integers do exist, as follows from the next simple lemma.

###### Lemma 3.

For any integer n ≥ 1 n\geq 1, we have

 | v 2 ( u) = v 2 ( v), for 1 ≤ u, v ≤ 2 n − 1, with u + v = 2 n. \begin{split}v_{2}(u)=v_{2}(v),\ \text{for }1\leq u,v\leq 2^{n-1},\ \text{with }u+v=2^{n}.\end{split} |  |

Then, by Lemma 3 and the definition of the binomial coefficients , we see that

 | ( 2 n − 1 k) ≡ 1 ( mod 2), for 0 ≤ k ≤ n. \begin{split}\binom{2^{n}-1}{k}\equiv 1\pmod{2},\ \ \text{for }\ 0\leq k\leq n\,.\end{split} |  | (4.7) |

Another requirement for M M is to be divisible by p p. A minimal value of n n for which M = 2 n − 1 M=2^{n}-1 is divisible by p p is ind p ⁡ ( 2) \operatorname{ind}_{p}(2). (We denote by ind p ⁡ ( a) \operatorname{ind}_{p}(a) the smallest integer 1 ≤ n ≤ p − 1 1\leq n\leq p-1 for which a n ≡ 1 ( mod p) a^{n}\equiv 1\pmod{p}.)

Now let M = d ​ p M=dp for some integer d ≥ 1 d\geq 1. The series associated to the second row of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) is

 | S 2 ​ ( X) = ( X p − 1 + X p) ​ ∑ k ≥ 0 X p ​ k. \begin{split}S_{2}(X)=(X^{p-1}+X^{p})\sum_{k\geq 0}X^{pk}\,.\end{split} |  | (4.8) |

To get the series S M + 1 ​ ( X) S_{M+1}(X) corresponding to the ( M + 1) (M+1) th row, we have to multiply S 2 ​ ( X) S_{2}(X) by ( 1 + X) d ​ p X d ​ p \tfrac{(1+X)^{dp}}{X^{dp}}. First, let us see that

 | ( X p − 1 + X p) ​ ( 1 + X) d ​ p X d ​ p = 1 + X X d ​ p − p + 1 ​ ( 1 + X + ⋯ + X d ​ p) = 1 + X d ​ p + 1 X d ​ p − p + 1. \begin{split}(X^{p-1}+X^{p})\frac{(1+X)^{dp}}{X^{dp}}&=\frac{1+X}{X^{dp-p+1}}(1+X+\cdots+X^{dp})=\frac{1+X^{dp+1}}{X^{dp-p+1}}\,.\end{split} |  |

Then

 | S 2 ​ ( X) ⋅ ( 1 + X) d ​ p X d ​ p = 1 + X d ​ p + 1 X d ​ p − p + 1 ⋅ ∑ k ≥ 0 X p ​ k = ∑ k ≥ 0 X p ​ k − d ​ p + p − 1 + ∑ k ≥ 0 X p ​ k + p. \begin{split}S_{2}(X)\cdot\frac{(1+X)^{dp}}{X^{dp}}&=\frac{1+X^{dp+1}}{X^{dp-p+1}}\cdot\sum_{k\geq 0}X^{pk}\\ &=\sum_{k\geq 0}X^{pk-dp+p-1}+\sum_{k\geq 0}X^{pk+p}.\end{split} |  |

Here the meromorphic and constant terms occur only in the first sum. Dropping them, we arrive at

 | S M + 1 ​ ( X) = Δ ⁡ ( ∑ k ≥ 0 X p ​ k − d ​ p + p − 1 + ∑ k ≥ 0 X p ​ k + p) = S 2 ​ ( X). \begin{split}S_{M+1}(X)=\Delta\Big(\sum_{k\geq 0}X^{pk-dp+p-1}+\sum_{k\geq 0}X^{pk+p}\Big)=S_{2}(X)\,.\end{split} |  |

In conclusion, we have proved the following theorem.

###### Theorem 2.

For any prime p ≥ 3 p\geq 3, the rows of the matrix v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) are eventually periodic. The pre-period contains only the first row of the matrix and the length of the smallest period is a divisor of 2 ind p ⁡ ( 2) − 1 2^{\operatorname{ind}_{p}(2)}-1.

We remark that 2 ind p ⁡ ( 2) − 1 2^{\operatorname{ind}_{p}(2)}-1 is not always the size of the smallest period. For example, if p = 11 p=11, ind 11 ⁡ ( 2) = 10 \operatorname{ind}_{11}(2)=10 and 2 10 − 1 = 1023 = 3 ⋅ 11 ⋅ 31 2^{10}-1=1023=3\cdot 11\cdot 31, but the length of the smallest period is π 11 = 11 ⋅ 31 = 341 \pi_{11}=11\cdot 31=341. Also, if p = 13 p=13, ind 13 ⁡ ( 2) = 12 \operatorname{ind}_{13}(2)=12 and 2 12 − 1 = 4095 = 3 2 ⋅ 5 ⋅ 7 ⋅ 13 2^{12}-1=4095=3^{2}\cdot 5\cdot 7\cdot 13, but the length of the smallest period is π 13 = 3 2 ⋅ 7 ⋅ 13 = 819 \pi_{13}=3^{2}\cdot 7\cdot 13=819. As well, if p = 19 p=19, ind 19 ⁡ ( 2) = 18 \operatorname{ind}_{19}(2)=18 and 2 18 − 1 = 262143 = 3 3 ⋅ 7 ⋅ 19 ⋅ 73 2^{18}-1=262143=3^{3}\cdot 7\cdot 19\cdot 73. In this case, again, the length of the smallest period is shorter, π 19 = ( 2 18 − 1) / 3 3 = 9709 \pi_{19}=(2^{18}-1)/3^{3}=9709.

There are two classes of primes: the first one, for which the length of the period of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) is maximal (that is, 2 ind p ⁡ ( 2) − 1 2^{\operatorname{ind}_{p}(2)}-1) and the second one, for which the length of the period is strictly smaller than 2 ind p ⁡ ( 2) − 1 2^{\operatorname{ind}_{p}(2)}-1. We do not know if either one or both of these classes contain infinitely many primes.

The reason for the shorter periods in these cases are the arithmetic properties that produce favorable patterns in the series of binomial coefficients. Thus, writing the binomial coefficients ( H k) ( mod 2) \binom{H}{k}\pmod{2}, 0 ≤ k ≤ H 0\leq k\leq H, as concatenated letters of a word and the repeated letters as powers, for H = 341 H=341, they are:

 | 1 2 ​ 0 2 ​ 1 2 ​ 0 10 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 42 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 10 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 170 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 10 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 42 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 10 ​ 1 2 ​ 0 2 ​ 1 2 \begin{split}1^{2}0^{2}1^{2}0^{10}1^{2}0^{2}1^{2}0^{42}1^{2}0^{2}1^{2}0^{10}1^{2}0^{2}1^{2}0^{170}1^{2}0^{2}1^{2}0^{10}1^{2}0^{2}1^{2}0^{42}1^{2}0^{2}1^{2}0^{10}1^{2}0^{2}1^{2}\end{split} |  |

and for H = 819 H=819, they are:

 | 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 204 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 204 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 204 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4 ​ 0 12 ​ 1 4. \begin{split}1^{4}0^{12}1^{4}0^{12}1^{4}0^{12}1^{4}0^{204}1^{4}0^{12}1^{4}0^{12}1^{4}0^{12}1^{4}0^{204}1^{4}0^{12}1^{4}0^{12}1^{4}0^{12}1^{4}0^{204}1^{4}0^{12}1^{4}0^{12}1^{4}0^{12}1^{4}.\end{split} |  |

A related pattern appears if p = 19 p=19. In this case H = 9709 H=9709 and the word defined by the binomial coefficients is

 | ( A ​ B) 16 ​ 0 512 ​ ( A ​ B) 16 ​ 0 6638 ​ ( B ​ A) 16 ​ 0 512 ​ ( B ​ A) 16, \begin{split}(AB)^{16}0^{512}(AB)^{16}0^{6638}(BA)^{16}0^{512}(BA)^{16},\end{split} |  |

where A = 1 2 ​ 0 2 ​ 1 2 ​ 0 2 ​ 1 2 ​ 0 2 ​ 1 2 A=1^{2}0^{2}1^{2}0^{2}1^{2}0^{2}1^{2} and B = 0 18 B=0^{18}.

## 5. Extreme values on the West Side of W ℙ W_{\mathbb{P}}

Calculations using power series from 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] allows us to quickly find a particular element of matrix T ℙ T_{\mathbb{P}}. In particular, we can find the “extreme values” of W ℙ ​ ( m) W_{\mathbb{P}}(m), m ≥ 1 m\geq 1. They emerge on the m m th row of T ℙ T_{\mathbb{P}} in places where number m m, when written in base two, has either few or many ones, compared with the rank of rows in its neighborhood. One can notice this property in the augmented oscillations of both graphs in Figure 8. In the following, we present the concrete structure of the most pronounced extremes, the values of W ℙ ​ ( m) W_{\mathbb{P}}(m), with m m around powers of two. We have to consider only the influence of odd primes, since p = 2 p=2 is involved only on the first two rows of T ℙ T_{\mathbb{P}}.

### 5.1. The size of W ℙ ​ ( 2 g) W_{\mathbb{P}}(2^{g})

Let m = 2 g − 1 m=2^{g}-1. By ( 4.7) we know that ( m j) ≡ 1 ( mod 2) \binom{m}{j}\equiv 1\pmod{2}, for 0 ≤ j ≤ m 0\leq j\leq m. To find the series associated to the ( m + 1) (m+1) th row of the p p -topography of T ℙ T_{\mathbb{P}}, we have to multiply:

 | ( 1 + X X) m ​ ∑ k ≥ 1 X k ​ p = 1 X m ​ ( 1 + X + ⋯ + X m) ​ ∑ k ≥ 1 X k ​ p = ( X p − m + X p − m + 1 + ⋯ + X p) + ( X 2 ​ p − m + X 2 ​ p − m + 1 + ⋯ + X 2 ​ p) + + ( X 3 ​ p − m + X 3 ​ p − m + 1 + ⋯ + X 3 ​ p) + ⋯ \begin{split}\left(\tfrac{1+X}{X}\right)^{m}\sum_{k\geq 1}X^{kp}=&\tfrac{1}{X^{m}}(1+X+\cdots+X^{m})\sum_{k\geq 1}X^{kp}\\ =&(X^{p-m}+X^{p-m+1}+\cdots+X^{p})+(X^{2p-m}+X^{2p-m+1}+\cdots+X^{2p})+\\ &+(X^{3p-m}+X^{3p-m+1}+\cdots+X^{3p})+\cdots\end{split} |  | (5.1) |

Then, p p divides W ℙ ​ ( 2 g) W_{\mathbb{P}}(2^{g}) if and only if the coefficient of X X in series ( 5.1) is odd. We see that primes p ≥ m + 2 p\geq m+2 are not involved and p = m + 1 p=m+1 is impossible.

For any small primes 3 ≤ p ≤ m 3\leq p\leq m, denote by λ = λ ⁡ ( p, m) ≥ 1 \lambda=\lambda(p,m)\geq 1 the largest integer for which there exist integers 0 ≤ s 1, s 2, …, s λ ≤ m 0\leq s_{1},s_{2},\dots,s_{\lambda}\leq m, such that

 | 1 = p + s 1 − m, 1 = 2 ​ p + s 2 − m, ⋮ 1 = λ ​ p + s λ − m. \begin{split}1&=p+s_{1}-m,\\ 1&=2p+s_{2}-m,\\[-6.49994pt] &\ \,\vdots\\[-3.50006pt] 1&=\lambda p+s_{\lambda}-m.\\ \end{split} |  | (5.2) |

Note that λ ⁡ ( p, m) \lambda(p,m) exists and λ ⁡ ( p, m) ≤ ( m + 1) / p \lambda(p,m)\leq(m+1)/p. Then, monomial X X appears in the 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] series ( 5.1) if and only if λ ⁡ ( p, m) \lambda(p,m) is odd.

For example, if m = 15 m=15, by a simple investigation we find that λ ⁡ ( 7, 15) \lambda(7,15) is even and λ ⁡ ( p, 15) \lambda(p,15) is odd for p = 3, 5, 11, 13 p=3,5,11,13, so W ℙ ​ ( 16) = 3 ⋅ 5 ⋅ 11 ⋅ 13 = 2145 W_{\mathbb{P}}(16)=3\cdot 5\cdot 11\cdot 13=2145. In the same way, if m = 31 m=31, we see that λ ⁡ ( p, 31) \lambda(p,31) is even only for p = 3, 5, 7, 11, 13 p=3,5,7,11,13, so W ℙ ​ ( 32) = 17 ⋅ 19 ⋅ 23 ⋅ 29 ⋅ 31 = 6678671 W_{\mathbb{P}}(32)=17\cdot 19\cdot 23\cdot 29\cdot 31=6678671.

### 5.2. The maximum W ℙ ​ ( 2 g − 1) W_{\mathbb{P}}(2^{g}-1)

Let m = 2 g − 2 m=2^{g}-2 with g ≥ 2 g\geq 2. Then, in 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] we have

 | ( 1 + X) m = 1 + X 2 + X 4 + ⋯ + X m. \begin{split}(1+X)^{m}=1+X^{2}+X^{4}+\cdots+X^{m}\,.\end{split} |  |

Finding the series that corresponds to the ( 2 g − 1) (2^{g}-1) th row of T ℙ T_{\mathbb{P}} implicates the calculation:

 | ( 1 + X X) m ​ ∑ k ≥ 1 X k ​ p = 1 X m ​ ( 1 + X 2 + ⋯ + X m) ​ ∑ k ≥ 1 X k ​ p = ( X p − m + X p − m + 2 + ⋯ + X p) + ( X 2 ​ p − m + X 2 ​ p − m + 2 + ⋯ + X 2 ​ p) + + ( X 3 ​ p − m + X 3 ​ p − m + 2 + ⋯ + X 3 ​ p) + ⋯ \begin{split}\left(\tfrac{1+X}{X}\right)^{m}\sum_{k\geq 1}X^{kp}=&\tfrac{1}{X^{m}}(1+X^{2}+\cdots+X^{m})\sum_{k\geq 1}X^{kp}\\ =&(X^{p-m}+X^{p-m+2}+\cdots+X^{p})+(X^{2p-m}+X^{2p-m+2}+\cdots+X^{2p})+\\ &+(X^{3p-m}+X^{3p-m+2}+\cdots+X^{3p})+\cdots\end{split} |  | (5.3) |

Again, we have to look for terms whose power of X X is equal to one. In series ( 5.3), the terms corresponding to primes p ≥ m + 2 p\geq m+2 do not contribute to the coefficient of X X. Also, p p can not be equal to m m, because m m is even.

If 2 g − 1 2^{g}-1 is a Mersenne prime, then p = m + 1 p=m+1 is equal with this prime. Then X p − m = X X^{p-m}=X, so p p divides W ℙ ​ ( 2 g − 1) W_{\mathbb{P}}(2^{g}-1).

For the remaining primes 3 ≤ p < m 3\leq p<m, let μ = μ ⁡ ( p, m) \mu=\mu(p,m) be the the maximal number of equalities

 | 1 = p + t 1 − m, 1 = 2 ​ p + t 2 − m, ⋮ 1 = μ ​ p + t μ − m, \begin{split}1&=p+t_{1}-m,\\ 1&=2p+t_{2}-m,\\[-6.49994pt] &\ \,\vdots\\[-3.50006pt] 1&=\mu p+t_{\mu}-m,\end{split} |  | (5.4) |

where t 1, t 2, …, t μ t_{1},t_{2},\dots,t_{\mu} are even numbers that belong to { 0, 2, …, m } \{0,2,\dots,m\}. Notice that μ ⁡ ( p, m) ≤ ( m + 1) / p \mu(p,m)\leq(m+1)/p. Then monomial X X effectively appears in series ( 5.3) if and only if μ ⁡ ( p, m) ≡ 1 ( mod 2) \mu(p,m)\equiv 1\pmod{2}. Therefore p | W ℙ ​ ( 2 g − 1) p\mid W_{\mathbb{P}}(2^{g}-1) if and only if μ ⁡ ( p, m) \mu(p,m) is odd.

Examples: If m = 14 m=14, we find that μ ⁡ ( 3, 14) = 3 \mu(3,14)=3; μ ⁡ ( 5, 14) = 2 \mu(5,14)=2; and μ ⁡ ( 7, 14) = μ ⁡ ( 11, 14) = μ ⁡ ( 13, 14) = 1 \mu(7,14)=\mu(11,14)=\mu(13,14)=1, so W ℙ ​ ( 15) = 3 ⋅ 7 ⋅ 11 ⋅ 13 = 3003 W_{\mathbb{P}}(15)=3\cdot 7\cdot 11\cdot 13=3003.

If m = 30 m=30, p = m + 1 p=m+1 is a Mersenne prime. For the smaller primes, we find that μ ⁡ ( 3, 30) = 5 \mu(3,30)=5; μ ⁡ ( 5, 30) = 3 \mu(5,30)=3; μ ⁡ ( 7, 30) = 2 \mu(7,30)=2; and μ ⁡ ( 11, 30) = μ ⁡ ( 13, 30) = μ ⁡ ( 19, 30) = μ ⁡ ( 23, 30) = μ ⁡ ( 29, 30) = 1 \mu(11,30)=\mu(13,30)=\mu(19,30)=\mu(23,30)=\mu(29,30)=1. This implies that W ℙ ​ ( 31) = 3 ⋅ 5 ⋅ 11 ⋅ 13 ⋅ 17 ⋅ 19 ⋅ 23 ⋅ 29 ⋅ 31 = 14325749295 W_{\mathbb{P}}(31)=3\cdot 5\cdot 11\cdot 13\cdot 17\cdot 19\cdot 23\cdot 29\cdot 31=14325749295.

### 5.3. The minimum W ℙ ​ ( 2 g + 1) W_{\mathbb{P}}(2^{g}+1)

Let m = 2 g m=2^{g}. The smaller numbers on the west side of T ℙ T_{\mathbb{P}} appear on the rows of rank 2 g + 1 2^{g}+1. This is due to the fact that ( 1 + X) m = 1 + X m (1+X)^{m}=1+X^{m} in 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]], that is, the binomial ( 1 + X) m (1+X)^{m} has fewest possible terms. Then, the series that correspond to the ( 2 g + 1) (2^{g}+1) th row sums the terms of positive powers of X X from the following

 | ( 1 + X X) m ​ ∑ k ≥ 1 X k ​ p = 1 X m ​ ( 1 + X m) ​ ∑ k ≥ 1 X k ​ p = ( X p − m + X p) + ( X 2 ​ p − m + X 2 ​ p) + ( X 3 ​ p − m + X 3 ​ p) + ⋯ \begin{split}\left(\tfrac{1+X}{X}\right)^{m}\sum_{k\geq 1}X^{kp}=&\tfrac{1}{X^{m}}(1+X^{m})\sum_{k\geq 1}X^{kp}\\ =&(X^{p-m}+X^{p})+(X^{2p-m}+X^{2p})+(X^{3p-m}+X^{3p})+\cdots\end{split} |  | (5.5) |

For a given p ≥ 3 p\geq 3, on the right-hand side of ( 5.5) may appear a single monomial X X, and this happens whenever there exists an integer d ≥ 1 d\geq 1, such that d ​ p − m = 1 dp-m=1. This implies that the only prime divisors p p of W ℙ ​ ( 2 g + 1) W_{\mathbb{P}}(2^{g}+1) are those for which if p | ( m + 1) p\mid(m+1).

For example, W ℙ ​ ( 9) = 3 W_{\mathbb{P}}(9)=3; W ℙ ​ ( 17) = 17 W_{\mathbb{P}}(17)=17; W ℙ ​ ( 33) = 33 W_{\mathbb{P}}(33)=33 and W ℙ ​ ( 1025) = 5 ⋅ 41 = 205 W_{\mathbb{P}}(1025)=5\cdot 41=205 (because 1025 = 5 2 ⋅ 41 1025=5^{2}\cdot 41); W ℙ ​ ( 32769) = 3 ⋅ 11 ⋅ 331 = 10923 W_{\mathbb{P}}(32769)=3\cdot 11\cdot 331=10923 (because 32769 = 2 15 + 1 = 3 2 ⋅ 11 ⋅ 331 32769=2^{15}+1=3^{2}\cdot 11\cdot 331).

Other terms of sequence W ℙ W_{\mathbb{P}} may be calculated in the same way. A few more examples are listed in Table 1.

Table 1. The size of W ℙ ​ ( m) W_{\mathbb{P}}(m) for m m around 2 g 2^{g}

power m W ℙ ​ ( m) decomposition of ​ W ℙ ​ ( m) ω ​ ( W ℙ ​ ( m)) g = 6 62 3.49 ⋅ 10 9 23 ⋅ 31 ⋅ 37 ⋅ 41 ⋅ 53 ⋅ 61 6 63 2.79 ⋅ 10 18 3 ⋅ 7 ⋅ 11 ⋯ 59 ⋅ 61 13 64 4.36 ⋅ 10 16 3 ⋅ 7 ⋅ 11 ⋯ 59 ⋅ 61 12 65 65 5 ⋅ 13 2 66 2145 3 ⋅ 5 ⋅ 11 ⋅ 13 4 g = 7 126 2.42 ⋅ 10 21 3 ⋅ 5 ⋅ 7 ⋯ 109 ⋅ 113 14 127 7.87 ⋅ 10 39 3 ⋅ 5 ⋅ 7 ⋯ 113 ⋅ 127 24 128 1.45 ⋅ 10 34 5 ⋅ 11 ⋅ 13 ⋯ 113 ⋅ 127 20 129 129 3 ⋅ 43 2 130 8385 3 ⋅ 5 ⋅ 13 ⋅ 43 4 g = 8 254 6.86 ⋅ 10 28 103 ⋅ 107 ⋅ 127 ⋯ 233 ⋅ 241 13 255 4.20 ⋅ 10 76 3 ⋅ 19 ⋅ 37 ⋯ 241 ⋅ 251 37 256 1.17 ⋅ 10 72 3 ⋅ 5 ⋅ 11 ⋯ 241 ⋅ 251 37 257 257 257 1 258 33153 3 ⋅ 43 ⋅ 257 3 g = 9 510 5.17 ⋅ 10 92 3 ⋅ 11 ⋅ 19 ⋯ 461 ⋅ 509 42 511 4.35 ⋅ 10 168 3 ⋅ 5 ⋅ 7 ⋯ 503 ⋅ 509 74 512 8.03 ⋅ 10 147 7 ⋅ 13 ⋅ 29 ⋯ 503 ⋅ 509 63 513 57 3 ⋅ 19 2 514 14649 3 ⋅ 19 ⋅ 257 3 g = 10 1022 9.32 ⋅ 10 173 7 ⋅ 71 ⋅ 109 ⋯ 1013 ⋅ 1021 65 1023 2.53 ⋅ 10 344 3 ⋅ 7 ⋅ 11 ⋯ 1019 ⋅ 1021 132 1024 4.72 ⋅ 10 298 3 ⋅ 11 ⋅ 19 ⋯ 1019 ⋅ 1021 115 1025 205 5 ⋅ 41 2 1026 11685 3 ⋅ 5 ⋅ 19 ⋅ 41 4 \begin{array}[]{*5c}\hline\cr\hline\cr\text{power}&m&W_{\mathbb{P}}(m)&\text{decomposition of }W_{\mathbb{P}}(m)&\omega(W_{\mathbb{P}}(m))\\ \hline\cr\hbox{\multirowsetup$g=6$}&62&3.49\cdot 10^{9}&23\cdot 31\cdot 37\cdot 41\cdot 53\cdot 61&6\\ &63&2.79\cdot 10^{18}&3\cdot 7\cdot 11\cdots 59\cdot 61&13\\ &64&4.36\cdot 10^{16}&3\cdot 7\cdot 11\cdots 59\cdot 61&12\\ &65&65&5\cdot 13&2\\ &66&2145&3\cdot 5\cdot 11\cdot 13&4\\ \hline\cr\hbox{\multirowsetup$g=7$}&126&2.42\cdot 10^{21}&3\cdot 5\cdot 7\cdots 109\cdot 113&14\\ &127&7.87\cdot 10^{39}&3\cdot 5\cdot 7\cdots 113\cdot 127&24\\ &128&1.45\cdot 10^{34}&5\cdot 11\cdot 13\cdots 113\cdot 127&20\\ &129&129&3\cdot 43&2\\ &130&8385&3\cdot 5\cdot 13\cdot 43&4\\ \hline\cr\hbox{\multirowsetup$g=8$}&254&6.86\cdot 10^{28}&103\cdot 107\cdot 127\cdots 233\cdot 241&13\\ &255&4.20\cdot 10^{76}&3\cdot 19\cdot 37\cdots 241\cdot 251&37\\ &256&1.17\cdot 10^{72}&3\cdot 5\cdot 11\cdots 241\cdot 251&37\\ &257&257&257&1\\ &258&33153&3\cdot 43\cdot 257&3\\ \hline\cr\hbox{\multirowsetup$g=9$}&510&5.17\cdot 10^{92}&3\cdot 11\cdot 19\cdots 461\cdot 509&42\\ &511&4.35\cdot 10^{168}&3\cdot 5\cdot 7\cdots 503\cdot 509&74\\ &512&8.03\cdot 10^{147}&7\cdot 13\cdot 29\cdots 503\cdot 509&63\\ &513&57&3\cdot 19&2\\ &514&14649&3\cdot 19\cdot 257&3\\ \hline\cr\hbox{\multirowsetup$g=10$}&1022&9.32\cdot 10^{173}&7\cdot 71\cdot 109\cdots 1013\cdot 1021&65\\ &1023&2.53\cdot 10^{344}&3\cdot 7\cdot 11\cdots 1019\cdot 1021&132\\ &1024&4.72\cdot 10^{298}&3\cdot 11\cdot 19\cdots 1019\cdot 1021&115\\ &1025&205&5\cdot 41&2\\ &1026&11685&3\cdot 5\cdot 19\cdot 41&4\\ \hline\cr\hline\cr\end{array}

We collect the results from Sections 5.1 - 5.3 into the next theorem.

###### Theorem 3.

Let g ≥ 2 g\geq 2 and let λ = λ ⁡ ( p, 2 g − 1) \lambda=\lambda(p,2^{g}-1) and μ = μ ⁡ ( p, 2 g − 2) \mu=\mu(p,2^{g}-2) be the integers defined by ( 5.2) and ( 5.4). Then

 | W ℙ ( 2 g − 1) = ∏ 0 ≤ p ≤ 2 g − 3 μ ⁡ ( p, 2 g − 2) ​ odd p; W ℙ ( 2 g) = ∏ 0 ≤ p ≤ 2 g − 1 λ ⁡ ( p, 2 g − 1) ​ odd p; W ℙ ( 2 g + 1) = ∏ p | 2 g + 1 p. \begin{split}W_{\mathbb{P}}(2^{g}-1)=\prod_{\begin{subarray}{c}0\leq p\leq 2^{g}-3\\ \mu(p,2^{g}-2)\text{ odd}\end{subarray}}p;\quad W_{\mathbb{P}}(2^{g})=\prod_{\begin{subarray}{c}0\leq p\leq 2^{g}-1\\ \lambda(p,2^{g}-1)\text{ odd}\end{subarray}}p;\quad W_{\mathbb{P}}(2^{g}+1)=\prod_{p\mid 2^{g}+1}p\,.\ \ \end{split} |  |

###### Paradox Problem 1.

Explain why W ℙ ​ ( 2 g − 1) W_{\mathbb{P}}(2^{g}-1) is larger than W ℙ ​ ( 2 g) W_{\mathbb{P}}(2^{g}), even if in the definition of μ ⁡ ( p, m) \mu(p,m), in equalities ( 5.4), an extra parity restriction on numbers t j t_{j} is imposed (condition that is absent for the existence of numbers s j s_{j} in ( 5.2)).

Removing duplicates and ordering W ℙ W_{\mathbb{P}}, we obtain sequence

 | U ​ O ​ ( W ℙ): 1, 2, 3, 5, 11, 15, 17, 33, 35, 51, 57, 65, 91, 105, 129, 165, 195, 205, 221, 255,257,385,451,561, 861, 897, 969, 1615, … \begin{split}UO(W_{\mathbb{P}}):\ &1,2,3,5,11,15,17,33,35,51,57,65,91,105,129,165,195,205,221,\\ &255,257,385,451,561,861,897,969,1615,\dots\end{split} |  | (5.6) |

This is related and has terms close to those of the analogues sequence [29, A222313], [13, Question 3] obtained by starting with the initial generation ℕ ∗ {\mathbb{N}^{*}} instead of ℙ \mathbb{P}. A complete discussion based on the previous analysis might give a complete argument for the certainty of the ranks of terms in list ( 5.6).

## 6. The West-Side of T ℙ T_{\mathbb{P}} and T ℕ ∗ T_{\mathbb{N}^{*}}

By Theorem 2 it follows that sequence v p ​ ( W ℙ) v_{p}(W_{\mathbb{P}}), the west edge of the matrix v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}), is also periodic, for any odd prime and the pre-period contains only the first term of the sequence. We do not know whether there is a prime p p for which the length of the period of v p ​ ( W ℙ) v_{p}(W_{\mathbb{P}}) is strictly smaller than the length of the period of v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}). If there is such a prime, then it should be larger than 23 23.

Comparing the general aspect of the p p -tomographies of T ℕ ∗ T_{\mathbb{N}^{*}} and T ℙ T_{\mathbb{P}}, one can observe both similarities and significant differences. Thus, on the one hand, although there are more and more irregularities in v p ​ ( T ℙ) v_{p}(T_{\mathbb{P}}) as p p increases, it is still eventually periodic. On the other hand, a big noise grows under the cells with larger and larger powers of p p, if the initial generation is ℕ ∗ {\mathbb{N}^{*}}. The most noticeable difference is if p = 2 p=2, since v 2 ​ ( T ℙ) v_{2}(T_{\mathbb{P}}) has only zero-cells from the third row on, while v 2 ​ ( T ℕ ∗) v_{2}(T_{\mathbb{N}^{*}}) sprouts the triangles in Figure 3. For small powers of p = 3 p=3 and p = 5 p=5, the results are shown side by side in Figures 6 and 7.

Figure 6. The tomographies of T ℕ ∗ ​ ( 60) T_{{\mathbb{N}^{*}}}(60) (left) and T ℙ ​ ( 60) T_{\mathbb{P}}(60) (right), for p = 3 p=3.
Code of colors for the cells containing the powers of p p, from 0, 1, 2, 3 0,1,2,3:

Figure 7. The tomographies of T ℕ ∗ ​ ( 60) T_{{\mathbb{N}^{*}}}(60) (left) and T ℙ ​ ( 60) T_{\mathbb{P}}(60) (right) for p = 5 p=5.
Code of colors for the cells containing the powers of p p, from 0, 1, 2, 3 0,1,2,3:

Although the noise is transmitted till the west edge, it does not cover it completely. The beginning of sequences W ℕ ∗ W_{\mathbb{N}^{*}} and W ℙ W_{\mathbb{P}} are:

 | W ℕ ∗ ( 35) = { 1, 2, 3, 6, 5, 15, 105, 70, 1, 5, 33, 55, 65, 273, 1001, 1430, 17, 17, 969, 4845, 1785, 6545, 37145, 81719, 17, 1105, 3553, 969969, 672945, 81345, 955049953, 66786710, 33, 561, 385 } \begin{split}W_{{\mathbb{N}^{*}}}(35)=\{&1,2,3,6,5,15,105,70,1,5,33,55,65,273,1001,1430,17,17,\\ &969,4845,1785,6545,37145,81719,17,1105,3553,\\ &969969,672945,81345,955049953,66786710,33,561,385\}\end{split} |  |

and

 | W ℙ ( 35) = { 1, 2, 3, 3, 5, 15, 105, 35, 3, 15, 11, 165, 195, 91, 3003, 2145, 17, 51, 969, 1615, 1785, 19635, 37145, 245157, 255, 221, 53295, 4849845, 44863, 16269, 14325749295, 6678671, 33, 561, 385 }. \begin{split}W_{\mathbb{P}}(35)=\{&1,2,3,3,5,15,105,35,3,15,11,165,195,91,3003,2145,17,51,\\ &969,1615,1785,19635,37145,245157,255,221,53295,\\ &4849845,44863,16269,14325749295,6678671,33,561,385\}\,.\end{split} |  |

They are equal in 13 13 places, at terms of indices 1, 2, 3, 5, 6, 7, 17, 19, 21, 23, 33, 34, 35 1,2,3,5,6,7,17,19,21,23,33,34,35. As far as we can check, this semblance remains valid, suggesting a general behavior. Even in places where they differ, the terms are very close, both in size and in arithmetic structure. Compare Figures 9 and 8 to see more similarities of sequences W ℕ W_{\mathbb{N}} and W ℙ W_{\mathbb{P}}.

Figure 8. Comparison of the size and structure of the sequence W ℙ ​ ( m), m ≥ 1 W_{\mathbb{P}}(m),m\geq 1:
Left: the graph of log ⁡ ( W ℙ ​ ( m)) \log(W_{\mathbb{P}}(m)); Right: the graph of ω ​ ( W ℙ ​ ( m)) \omega(W_{\mathbb{P}}(m)).

Figure 9. Comparison of the size and structure of the sequence W ℕ ∗ ​ ( m), m ≥ 1 W_{{\mathbb{N}^{*}}}(m),m\geq 1:
Left: the graph of log ⁡ ( W ℕ ∗ ​ ( m)) \log(W_{{\mathbb{N}^{*}}}(m)); Right: the graph of ω ​ ( W ℕ ∗ ​ ( m)) \omega(W_{{\mathbb{N}^{*}}}(m)).

More precisely, the closeness between the two sequences can be measured by the surplus number of prime factors between W ℕ ∗ ​ ( m) W_{{\mathbb{N}^{*}}}(m) or W ℙ ​ ( m) W_{\mathbb{P}}(m) and their greatest common divisor, G ⁡ ( m):= gcd ⁡ ( W ℕ ∗ ​ ( m), W ℙ ​ ( m)) G(m):=\gcd(W_{{\mathbb{N}^{*}}}(m),W_{\mathbb{P}}(m)), m ≥ 1 m\geq 1. For this, the appropriate counting functions are

 | s ℕ ∗ ​ ( f, K) = #⁡ { 1 ≤ m ≤ K: ω ⁡ ( W ℕ ∗ ​ ( m) / G ⁡ ( m)) = f }, s ℙ ​ ( f, K) = #⁡ { 1 ≤ m ≤ K: ω ⁡ ( W ℙ ​ ( m) / G ⁡ ( m)) = f }. \begin{split}s_{\mathbb{N}^{*}}(f;K)&=\#\{1\leq m\leq K:\omega\big(W_{{\mathbb{N}^{*}}}(m)/G(m)\big)=f\}\,,\\ s_{\mathbb{P}}(f;K)&=\#\{1\leq m\leq K:\omega\big(W_{\mathbb{P}}(m)/G(m)\big)=f\}\,.\end{split} |  |

In Table 2 we counted the number of integers m m for which the surplus occurs. Notice that if m ≤ 1024 m\leq 1024, the largest surplus is 7 7. This is small when compared with the maximum values of ω ​ ( W ℕ ∗ ​ ( m)) \omega(W_{\mathbb{N}^{*}}(m)) and ω ​ ( W ℙ ​ ( m)) \omega(W_{\mathbb{P}}(m)) in this range, which are equal to ω ​ ( W ℕ ∗ ​ ( 1023)) = 130 \omega(W_{\mathbb{N}^{*}}(1023))=130 and ω ​ ( W ℙ ​ ( 1023)) = 132 \omega(W_{\mathbb{P}}(1023))=132.

Table 2. The surplus counting functions of W ℕ ∗ W_{\mathbb{N}^{*}} and W ℙ W_{\mathbb{P}}.

f 0 1 2 3 4 5 6 7 8 9 s ℕ ∗ ​ ( f, 1024) 391 311 183 77 41 14 5 2 0 0 s ℙ ​ ( f, 1024) 353 391 186 74 11 6 3 0 0 0 \begin{array}[]{ccccccccccc}\hline\cr\hline\cr f&0&1&2&3&4&5&6&7&8&9\\ \hline\cr s_{\mathbb{N}^{*}}(f;1024)&391&311&183&77&41&14&5&2&0&0\\ s_{\mathbb{P}}(f;1024)&353&391&186&74&11&6&3&0&0&0\\ \hline\cr\hline\cr\end{array}

Equality between W ℕ ∗ ​ ( m) W_{{\mathbb{N}^{*}}}(m) and W ℙ ​ ( m) W_{\mathbb{P}}(m) for m ≤ 1024 m\leq 1024 occurs 149 149 times. We also mention that even in a larger range, integers m m for which W ℕ ∗ ​ ( m) = W ℙ ​ ( m) W_{{\mathbb{N}^{*}}}(m)=W_{\mathbb{P}}(m) tend to appear in clusters, often grouping a varying number of consecutive numbers.

### 6.1. Primes dividing the maximal values of W ℕ ∗ ​ ( m) W_{\mathbb{N}^{*}}(m)

An intricate pattern of the sets of primes that divide the larger values of W ℕ ∗ ​ ( m) W_{\mathbb{N}^{*}}(m) around m = 2 g m=2^{g} develops as g g increases. Let us see a typical example, the case g = 8 g=8. To emphasize the presence or absence and the position of prime divisors in the list all primes ≤ m \leq m, we have listed them all, but in two distinguished ways. Thus W ℕ ∗ ​ ( m) W_{\mathbb{N}^{*}}(m) is the product of primes written in normal font, while the primes that do not divide W ℕ ∗ ​ ( m) W_{\mathbb{N}^{*}}(m) are shown in red color (in the electronic form) smaller font. Thus, we have:

 | W ℕ ∗ ​ ( 255): 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,179,181,191,193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251; W ℕ ∗ ​ ( 256): 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,179,181,191,193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, \begin{split}W_{\mathbb{N}^{*}}(255):\ &\mbox{{\color[rgb]{1,0,0}\footnotesize 2}},3,\mbox{{\color[rgb]{1,0,0}\footnotesize 5}},7,11,13,\mbox{{\color[rgb]{1,0,0}\footnotesize 17}},19,\mbox{{\color[rgb]{1,0,0}\footnotesize 23, 29, 31}},37,41,43,47,\mbox{{\color[rgb]{1,0,0}\footnotesize 53, 59, 61, 67, 71, 73, 79, 83}},\\ &89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,\\ &173,179,181,191,193,197,199,211,223,227,229,233,239,241,251;\\[5.59721pt] W_{\mathbb{N}^{*}}(256):\ &2,\mbox{{\color[rgb]{1,0,0}\footnotesize 3}},5,7,11,\mbox{{\color[rgb]{1,0,0}\footnotesize 13}},17,19,23,\mbox{{\color[rgb]{1,0,0}\footnotesize 29, 31, 37, 41}},43,47,\mbox{{\color[rgb]{1,0,0}\footnotesize 53, 59, 61}},67,71,73,79,83,\\ &\mbox{{\color[rgb]{1,0,0}\footnotesize 89, 97, 101, 103, 107, 109, 113, 127}},131,137,139,149,151,157,163,167,\\ &173,179,181,191,193,197,199,211,223,227,229,233,239,241,251\,,\end{split} |  |

so ω ​ ( W ℕ ∗ ​ ( 255)) = 40 \omega(W_{\mathbb{N}^{*}}(255))=40 and ω ​ ( W ℕ ∗ ​ ( 256)) = 37 \omega(W_{\mathbb{N}^{*}}(256))=37.

### 6.2. A problem of Sloane

N. J. A. Sloane [29, A222313], [13, Question 3] orders increasingly and eliminates duplicates from the terms of W ℕ ∗ W_{\mathbb{N}^{*}} and obtains sequence ‡ ‡\ddagger ‡ ‡\ddagger ‡ \ddagger Considering only the first five hundred terms, Sloane missed W ℕ ∗ ​ ( 1025) = 41 W_{\mathbb{N}^{*}}(1025)=41 and W ℕ ∗ ​ ( 513) = 57 W_{\mathbb{N}^{*}}(513)=57 from the list of terms of size smaller than 100 100.

 | U ​ O ​ ( W ℕ ∗): 1, 2, 3, 5, 6, 15, 17, 33, 41, 55, 57, 65, 70, 105, 129, 257,273,385,561,897, 969, 1001, … \begin{split}UO(W_{\mathbb{N}^{*}}):\ &1,2,3,5,6,15,17,33,41,55,57,65,70,105,129,\\ &257,273,385,561,897,969,1001,\dots\end{split} |  | (6.1) |

He asks if the first part of the list contains all numbers ≤ 100 \leq 100 that appear in this sequence. The numbers from ( 6.1) are obtained from the first 8200 8200 terms of W ℕ ∗ W_{\mathbb{N}^{*}}.

Examining the terms, we observed a general formula for a numbers that make a big jump in the beginning, during the process of ordering.

###### Conjecture 3.

For any integer g ≥ 0 g\geq 0, we have:

 | W ℕ ∗ ​ ( 2 g + 1) = { 2 g + 1, if 2 g + 1 is square free ( 2 g + 1) / D g, else, \begin{split}W_{\mathbb{N}^{*}}(2^{g}+1)=\begin{cases}2^{g}+1,&\text{ if\ \ $2^{g}+1$ is square free}\\ (2^{g}+1)/D_{g},&\text{ else,}\\ \end{cases}\end{split} |  |

where D g D_{g} is the largest square that divides 2 g + 1 2^{g}+1.

For small ranks, if g ≤ 13 g\leq 13, Conjecture 3 verifies, since 2 g + 1 2^{g}+1 is prime, for g = 1, 2, 4, 8 g=1,2,4,8, or a product of two distinct primes, for g = 5, 6, 7, 11, 12, 13 g=5,6,7,11,12,13, and W ℕ ∗ ​ ( 2 g + 1) = 2 g + 1 W_{\mathbb{N}^{*}}(2^{g}+1)=2^{g}+1 in these cases. For the remaining values, we have: W ℕ ∗ ​ ( 2 3 + 1) = W ℕ ∗ ​ ( 3 2) = 1 W_{\mathbb{N}^{*}}(2^{3}+1)=W_{\mathbb{N}^{*}}(3^{2})=1; W ℕ ∗ ​ ( 2 8 + 1) = W ℕ ∗ ​ ( 3 3 ⋅ 19) = 57 W_{\mathbb{N}^{*}}(2^{8}+1)=W_{\mathbb{N}^{*}}(3^{3}\cdot 19)=57; W ℕ ∗ ​ ( 2 10 + 1) = W ℕ ∗ ​ ( 5 2 ⋅ 41) = 41 W_{\mathbb{N}^{*}}(2^{10}+1)=W_{\mathbb{N}^{*}}(5^{2}\cdot 41)=41.

Verifying the decomposition of a few hundred more numbers of the form 2 g + 1 2^{g}+1 and assuming, confer the above discussion, that the smallest local minimums of W ℕ ∗ W_{\mathbb{N}^{*}} are attained at these ranks, we should expect a positive answer to Sloane’s question.

###### Paradox Problem 2.

Explain the peculiarity: why, given that the towers of the p p -tomographies are higher when starting with the initial generation ℕ ∗ {\mathbb{N}^{*}} instead of ℙ \mathbb{P}, more non-zero cells appear on the western edge in the second case. For example, counting only terms less than 1000 1000, we find 27 27 terms in O ​ U ​ ( W ℙ) OU(W_{\mathbb{P}}) and 21 21 terms in O ​ U ​ ( W ℕ ∗) OU(W_{\mathbb{N}^{*}}).

## Acknowledgement

All calculations and images presented in this work were made using the free open-source mathematical software system [39].

## References

- BTW’ [87] P. Bak, C. Tang, K. Wiesenfeld, *Self-organized criticality: an explanation of 1 / f 1/f noise*, Physical Review Letters 59 (1987), no. 4, 381–384.
- BGS’ [15] A. Balog, A. Granville, J. Solymosi, *Gaps between fractional parts and additive combinatorics*, Q. J. Math. (2015) doi: 10.1093/qmath/hav012, First published online: May 1, 2015.
- BR’ [02] Y. Le Borgne, D. Rossin, *On the identity of the sandpile group*, Discrete Math. 256 (2002), no. 3, 775–790.
- CPS’ [08] S. Caracciolo, G. Paoletti, A. Sportiello, *Explicit characterization of the identity configuration in an abelian sandpile model*, J. Phys. A 41 (2008), no. 49, 495003, 17 pp.
- CZZ’ [11] M. Caragiu, A. Zaharescu, M. Zaki, *On Ducci sequences with algebraic numbers*, Fibonacci Quart. 49 (2011), 34–40.
- CT’ [04] M. Chamberland, D. Thomas, *The N N -number Ducci game*, Section of Open Problems and Conjectures from J. Difference Equ. Appl. 10, no. 3 (2004), 339–342.
- CM’ [37] C. Ciamberlini, A. Marengoni, *Su una interessante curiosità numerica*, Periodico di Matematiche 17 (1937), 25–30.
- CGVZ’ [02] C. Cobeli, G. Groza, M. Vâjâitu, A. Zaharescu, *Generalization of a theorem of Steinhaus*, Colloq. Math 92 (2002), 257–266.
- CCZ’ [00] C. Cobeli, M. Crâşmaru, A. Zaharescu, *A cellular automaton on a torus*, Portugaliae Mathematica, 57, fasc. 3 (2000), 311–323.
- CZ’ [03] C. Cobeli, A. Zaharescu, *The Haros-Farey sequence at two hundred years*, Acta Univ. Apulensis Math. Inform. 5 (2003), 1–38.
- CZ’ [06] C. Cobeli, A. Zaharescu, *On the Farey fractions with denominators in arithmetic progression*, J. Integer Seq. 9 (2006), no. 3, Article 06.3.4, 26 pp.
- CZ’ [13] C. Cobeli, A. Zaharescu, *A promenade around Pascal triangle - number motives*, Bull. Math. Soc. Sci. Math. Roumanie 56 ( 104) (2013), no. 1, 73–98.
- CZ’ [14] C. Cobeli, A. Zaharescu, *A game with divisors and absolute differences of exponents*, J. Difference Equ. Appl. 20 (2014), no. 11, 1489–1501.
- DD’ [14] R. Dandekar, D. Dhar, *Proportionate growth in patterns formed in the rotor-router model*, J. Stat. Mech. Theory Exp. 2014, no. 11, P11030, 25 pp.
- DS’ [12] D. Dhar, T. Sadhu, *Pattern formation in fast-growing sandpiles*, Phys. Rev. E. 85 (2012), no. 2, 16 pp.
- DS’ [13] D. Dhar, T. Sadhu, *A sandpile model for proportionate growth*, J. Stat. Mech. Theory Exp. (2013), no. 11, P11006, 17 pp.
- FR’ [08] A. Fey-den Boer, F. Redig, *Limiting shapes for deterministic centrally seeded growth models*, J. Stat. Phys. 130 (2008), no. 3, 579–597.
- BR’ [11] A. Fey, H. Liu, *Limiting shapes for a non-abelian sandpile growth model and related cellular automata*, J. Cell. Autom. 6 (2011), no. 4-5, 353–383.
- Gra’ [92] A. Granville, *Zaphod Beeblebrox’s brain and the fifty-ninth row of Pascal’s triangle*, The American Mathematical Monthly 99 (1992) 318–331.
- Gra’ [97] A. Granville, *Arithmetic properties of binomial coefficients. I. Binomial coefficients modulo prime powers*, Organic mathematics (Burnaby, BC, 1995), 253–276. CMS Conf. Proc. 20, Amer. Math. Soc. Providence, RI, 1997.
- GQ’ [00] J. Gravner, J. Quastel, *Internal DLA and the Stefan problem*, Ann. Probab. 28 (2000), no. 4, 1528–1562.
- GVZ’ [05] G. Groza, M. Vâjâitu, A. Zaharescu, *Primitive arcs on elliptic curves*, Rev. Roumaine Math. Pures Appl. 50 (2005), 31–38.
- Guy’ [04] R. K. Guy, *Unsolved Problems in Number Theory*, Springer-Verlag, 3nd ed. 2004.
- HKSW’ [14] A. Haynes, H. Koivusalo, L. Sadun, J. Walton, *Gaps problems and frequencies of patches in cut and project sets*, http://arxiv.org/abs/1411.0578.
- LP’ [08] L. Levine, Y. Peres, *Spherical asymptotics for the rotor-router model in ℤ d \mathbb{Z}^{d}*, Indiana Univ. Math. J. 57 (2008), no. 1, 431–449.
- LPer’ [10] L. Levine, Y. Peres, *Scaling limits for internal aggregation models with multiple sources*, J. Anal. Math. 111 (2010), 151–219.
- LPro’ [10] L. Levine, J. Propp, *What is a sandpile?*, Notices Amer. Math. Soc. 57 (2010), no. 8, 976–979.
- LKG’ [90] S. H. Liu, T. Kaplan, L. J. Gray, *Geometry and dynamics of deterministic sand piles*, Phys. Rev. A (3) 42 (1990), no. 6, 3207–3212.
- [29] N. J. A. Sloane and OEIS foundation, *On-Line Encyclopedia of Integer Sequences*published electronically.
- Odl’ [93] A. M. Odlyzko, *Iterated absolute values of differences of consecutive primes*, Mathematics of Computation 61 (1993), 373–380.
- Ost’ [03] S. Ostojic, *Patterns formed by addition of grains to only one site of an abelian sandpile*, Physica A: Statistical Mechanics and its Applications 318, Issue 1 (2003), 187–199.
- PDK’ [96] V. B. Priezzhev, D. Dhar, A. Dhar, S. Krishnamurthy, *Eulerian walkers as a model of self-organized criticality*, Physical Review Letters, 77 (1996), 5079–5082.
- Pro’ [10] J. Propp, *Discrete analog computing with rotor-routers*, Chaos 20 (2010), no. 3, 037110, 10 pp.
- [34] M. Prunescu, *Recurrent two-dimensional sequences generated by homomorphisms of finite abelian p p -groups with periodic initial conditions*, Fractals 19 (2011), no. 4, 431–442.
- [35] M. Prunescu, *The Thue-Morse-Pascal double sequence and similar structures*, C. R. Math. Acad. Sci. Paris 349 (2011), no. 17-18, 939–942.
- Pru’ [12] M. Prunescu, *Sign-reductions, p p -adic valuations, binomial coefficients modulo p k p^{k} and triangular symmetries*, preprint 2012. [electronic version][4]
- Pru’ [13] M. Prunescu, *𝔽 p \mathbb{F}_{p} -affine recurrent n n -dimensional sequences over 𝔽 q \mathbb{F}_{q} are p p -automatic*, European J. Combin. 34 (2013), no. 2, 260–284.
- SD’ [10] T. Sadhu, D. Dhar, *Pattern formation in growing sandpiles with multiple sources or sinks*, J. Stat. Phys. 138 (2010), no. 4-5, 815–837.
- [39] W. Stein et al., *Sage Mathematics Software (Version 6.8)*, The Sage Development Team, 2015. [http://www.sagemath.org][5].

[◄][6][image: ar5iv homepage] [7]
[Feeling lucky?][8] [9]
[Conversion report][10]
[Report an issue][11]
[View original on arXiv][12] [►][13]


## Links

[1]: mailto:cristian.cobeli@imar.ro
[2]: mailto:mihai.prunescu@imar.ro
[3]: mailto:zaharesc@illinois.edu
[4]: https://www.academia.edu/3136109/Sign-reductions_p-adic_valuations_binomial_coefficients_modulo_p_k_and_triangular_symmetries
[5]: http://www.sagemath.org
[6]: /html/1511.04314
[7]: /
[8]: /feeling_lucky
[9]: /land_of_honey_and_milk
[10]: /log/1511.04315
[11]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1511.04315
[12]: https://arxiv.org/pdf/1511.04315
[13]: /html/1511.04316
