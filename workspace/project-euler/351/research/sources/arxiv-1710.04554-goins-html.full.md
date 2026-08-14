<!-- source: https://arxiv.org/html/1710.04554v1 | converted from HTML -->

Lattice Point Visibility on Generalized Lines of Sight

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1710.04554v1 [math.NT] 12 Oct 2017

# Lattice Point Visibility on Generalized Lines of Sight

Edray H. Goins, Pamela E. Harris, Bethany Kubik, and Aba Mbirika

Date: August 11, 2026

###### Abstract.

For a fixed b ∈ ℕ = { 1, 2, 3, … } b\in\mathbb{N}=\{1,2,3,\ldots\} we say that a point ( r, s) (r,s) in the integer lattice ℤ × ℤ \mathbb{Z}\times\mathbb{Z} is b b -visible from the origin if it lies on the graph of a power function f ⁡ ( x) = a ​ x b f(x)=ax^{b} with a ∈ ℚ a\in\mathbb{Q} and no other integer lattice point lies on this curve (i.e., line of sight) between ( 0, 0) (0,0) and ( r, s) (r,s). We prove that the proportion of b b -visible integer lattice points is given by 1 / ζ ⁡ ( b + 1) 1/\zeta(b+1), where ζ ⁡ ( s) \zeta(s) denotes the Riemann zeta function. We also show that even though the proportion of b b -visible lattice points approaches 1 1 as b b approaches infinity, there exist arbitrarily large rectangular arrays of b b -invisible lattice points for any fixed b b. This work specialized to b = 1 b=1 recovers original results from the classical lattice point visibility setting where the lines of sight are given by linear functions with rational slope through the origin.

###### Key words and phrases:

Riemann-zeta function, lattice point visibility, greatest common divisor, Chinese remainder theorem

###### 2010 Mathematics Subject Classification

Primary 11P21, 11M99

## 1. Introduction

A point ( r, s) (r,s) in the integer lattice ℤ × ℤ \mathbb{Z}\times\mathbb{Z} is said to be visible from the origin if it lies on a straight line through the origin ( 0, 0) (0,0) and no other lattice point lies on this line of sight between ( 0, 0) (0,0) and ( r, s) (r,s). Given this definition, it is natural to ask what proportion of lattice points are visible from the origin, which is equivalent to computing the probability that two integers are relatively prime. This problem was first addressed in the 1800s by numerous people including: Dirichlet, who proved a weaker form of the problem in 1849 [13]; Cesàro, who is often attributed as having posed this problem in 1881 [8]; and Sylvester, who along with Cesàro gave independent proofs of this result in 1883 [9, 26]. Cesàro proved that the probability that two randomly chosen integers in { 1, 2, …, n } \{1,2,\ldots,n\} are coprime is given by 1 / ζ ⁡ ( 2) 1/\zeta(2) as n n approaches infinity, where ζ ⁡ ( s) = ∑ n = 1 ∞ 1 / n s \zeta(s)=\sum_{n=1}^{\infty}1/n^{s} denotes the Riemann zeta function [8]. Thus, the proportion of visible integer lattice points is given by 1 / ζ ⁡ ( 2) = 6 / π 2 ≈.608 1/\zeta(2)=6/\pi^{2}\approx.608.

In 1971, Herzog and Stewart characterized patterns of visible (respectively, invisible) points within the approximately 60% (respectively, 40%) of the lattice containing visible (respectively, invisible) points [16] and their seminal work continues to motivate research in this area [2, 3, 10, 15, 17, 18, 19]. Additionally, it has been shown that the set of lattice points in the plane visible from the origin contains arbitrarily large square arrays of adjacent invisible lattice points [5, Theorem 5.29, p. 119]. This is connected to a celebrated result in number theory regarding the existence of two mutually pairwise coprime sets of consecutive integers. Since then, others have further studied properties of strings of consecutive composite numbers and their connection to integer lattice point visibility [12, 14, 25].

(1,10) (2,20) (3,30) (4,40) (5,50) (6,60) (1,2) (2,8) (3,18) (4,32) (6,72) 1 2 3 4 5 6 10 20 30 40 50 60 70 80[image: Refer to caption]

Figure 1. Lines of sight f ⁡ ( x) = 10 ​ x f(x)=10x and g ⁡ ( x) = 2 ​ x 2 g(x)=2x^{2} with visible and invisible points.

In this work, we fix b ∈ ℕ b\in\mathbb{N} and say that a point ( r, s) (r,s) in the integer lattice ℤ × ℤ \mathbb{Z}\times\mathbb{Z} is b b -visible from the origin if it lies on the graph of a power function f ⁡ ( x) = a ​ x b f(x)=ax^{b} with a ∈ ℚ a\in\mathbb{Q} and no other integer lattice point lies on this curve (i.e., line of sight) between ( 0, 0) (0,0) and ( r, s) (r,s). Hence, our work specialized to b = 1 b=1 recovers the classical setting of lattice point visibility whose lines of sight are given by linear functions f ⁡ ( x) = a ​ x f(x)=ax with a ∈ ℚ a\in\mathbb{Q}. We remark that throughout this work, following the wording introduced by Pólya, we often refer to lattice points as trees and collections of adjacent trees as forests [4, 24].

Figure 1 contains two examples of lines of sight on which we mark the lattice points that are visible with white nodes and those that are invisible with black nodes. Figure 2 marks the b b -invisible lattice points in the square [0, 50] × [0, 50] [0,50]\times[0,50] for b = 1, 2, 3, 4 b=1,2,3,4. Note that the number of b b -visible points increases substantially relative to a small growth in b b even in this small portion of the integer lattice. This observation, presented in Table 1, leads us naturally to our first result.

[image: Refer to caption] (a) b = 1 b=1

[image: Refer to caption] (b) b = 2 b=2

[image: Refer to caption] (c) b = 3 b=3

[image: Refer to caption] (d) b = 4 b=4

Figure 2. The b b -invisible lattice points in [0, 50] × [0, 50] [0,50]\times[0,50] when b = 1, 2, 3, 4 b=1,2,3,4. Table 1. Proportion of b b -visible and b b -invisible points for b = 1, 2, 3, 4 b=1,2,3,4 with all values approximated to 3 decimal places.

b b | ζ ⁡ ( b + 1) \zeta(b+1) | 1 ζ ⁡ ( b + 1) \frac{1}{\zeta(b+1)} | 1 − 1 ζ ⁡ ( b + 1) 1-\frac{1}{\zeta(b+1)} | Proportion of b b -invisible points in 50 × 50 50\times 50 grid |

1 | 1.644 | .608 | .392 | 953 / 2500 ≈.381 953/2500\approx\mathbf{.381} |

2 | 1.202 | .832 | .168 | 399 / 2500 ≈.160 {399}/{2500}\approx\mathbf{.160} |

3 | 1.082 | .924 | .076 | 166 / 2500 ≈.066 {166}/{2500}\approx\mathbf{.066} |

4 | 1.036 | .964 | .035 | 75 / 2500 ≈.030 {\phantom{0}75}/{2500}\approx\mathbf{.030} |

###### Theorem 1.

Fix an integer b ∈ ℕ b\in\mathbb{N}. Then the proportion of points ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} that are b b -visible is 1 ζ ⁡ ( b + 1) \displaystyle\frac{1}{\zeta(b+1)}.

Theorem 1 implies that the proportion of b b -visible lattice points approaches 1 1 as b b approaches infinity. However, as our next result shows, for any fixed b ∈ ℕ b\in\mathbb{N} there exist arbitrarily large b b -invisible rectangular forests, that is, rectangular arrays of adjacent b b -invisible integer lattice points.

###### Theorem 2.

Let b ∈ ℕ b\in\mathbb{N}. For any integers n, m > 0 n,m>0, there exists a lattice point ( r, s) (r,s) such that every point ( r + i, s + j) (r+i,s+j), where 0 ≤ i < n 0\leq i<n and 0 ≤ j < m 0\leq j<m, is b b -invisible from the origin.

Although we present a proof that arbitrarily large b b -invisible rectangular forests exist for all values b ∈ ℕ b\in\mathbb{N}, our work does not construct forests close to the origin. In the classical b = 1 b=1 case, the work of Herzog and Stewart used prime matrices and the Chinese remainder theorem to compute invisible square forests and they presented 2 × 2 2\times 2 and 3 × 3 3\times 3 invisible forests shown in Figure 3 [16].

(14,20) (14,21) (15,20) (15,21)

( 1274, 1308) (1274,1308) ( 1274, 1309) (1274,1309) ( 1274, 1310) (1274,1310) ( 1275, 1308) (1275,1308) ( 1275, 1309) (1275,1309) ( 1275, 1310) (1275,1310) ( 1276, 1308) (1276,1308) ( 1276, 1309) (1276,1309) ( 1276, 1310) (1276,1310)

Figure 3. The 2 × 2 2\times 2 and 3 × 3 3\times 3 invisible forests lying closest to the origin.

It is easily verified that every point ( r, s) (r,s) in the forests of Figure 3 satisfies the condition gcd ⁡ ( r, s) > 1 \gcd(r,s)>1. It turns out that, up to symmetry, these are the closest invisible square forests of size n = 2 n=2 and n = 3 n=3. In a brief remark, Wolfram claims to have found the closest 4 × 4 4\times 4 invisible forest, being located approximately 12 million units from the origin [27, p. 1093]. However, this has yet to be confirmed in the literature. Although to date, no one knows the closest n × n n\times n invisible square forests for n ≥ 5 n\geq 5, recently bounds have been given on where invisible square forests might exist in the integer lattice [17, 22]. Finding such bounds in our generalized setting remains an open problem.

Our paper is organized as follows. Section 2 contains the necessary definitions to make our approach precise. Section 3 provides a proof of Theorem 1. Section 4 gives a construction of arbitrarily large rectangular b b -invisible forests, thereby proving Theorem 2.

## 2. Background

The results presented in this paper are limited to the first quadrant of the plane, and, due to the symmetry of the plane, our results can be easily extended to apply to all of ℤ × ℤ \mathbb{Z}\times\mathbb{Z}.

###### Definition 1.

Fix b ∈ ℕ b\in\mathbb{N}. A point ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} is said to be b b -invisible if the following two conditions hold:

1. (1)

The point ( r, s) (r,s) lies on the graph of f ⁡ ( x) = a ​ x b f(x)=ax^{b} for some a ∈ ℚ a\in\mathbb{Q}. That is, s = a ​ r b s=ar^{b}.

2. (2)

There exists an integer k > 1 k>1 such that k k divides r r and k b k^{b} divides s s.

The point is said to be b b -visible if it satisfies Condition 1, but fails to satisfy Condition 2.

When we say that a point is b b -invisible or b b -visible, it is always with respect to the origin. If ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} is b b -invisible and Condition 1 is satisfied by the function f ⁡ ( x) = a ​ x b f(x)=ax^{b}, then ( − r, s) (-r,s), ( − r, − s) (-r,-s), and ( r, − s) (r,-s) are b b -invisible under the functions a ​ ( − x) b a(-x)^{b}, − a ​ ( − x) b -a(-x)^{b}, and − a ​ x b -ax^{b}, respectively, and likewise for b b -visible points. Thus in our study it suffices to determine the b b -visibility (meaning, whether the point is b b -visible or b b -invisible) of the lattice points in ℕ × ℕ \mathbb{N}\times\mathbb{N}.

To speak about the b b -visibility of a lattice point in this new setting, we develop a generalization of the greatest common divisor.

###### Definition 2.

Fix b ∈ ℕ b\in\mathbb{N}. The generalized greatest common divisor of r r and s s with respect to b b is denoted gcd b \ggcd_{b} and is defined as

 | gcd b ⁡ ( r, s):= max ⁡ { k ∈ ℕ ∣ k ​ divides ​ r ​ and ​ k b ​ divides ​ s }. \ggcd_{b}(r,s):=\max\{k\in\mathbb{N}\mid k\textrm{ divides }r\textrm{ and }k^{b}\textrm{ divides }s\}. |  |

Observe that gcd b \ggcd_{b} coincides with the classical greatest common divisor when b b equals 1 1. Moreover, from the lattice point visibility language, the new generalized greatest common divisor implies that for a fixed b ∈ ℕ b\in\mathbb{N} the point ( r, s) (r,s) is b b -visible if there exists a function f ⁡ ( x) = a ​ x b f(x)=ax^{b} with a ∈ ℚ a\in\mathbb{Q} such that ( r, s) (r,s) is on the graph of f f and is the first integral point on the graph of f f from the origin. The following result gives a necessary and sufficient condition to determine b b -visibility.

###### Proposition 3.

A point ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} is b b -visible if and only if gcd b ⁡ ( r, s) = 1 \ggcd_{b}(r,s)=1.

###### Proof.

By Definition 1, a point ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} is b b -visible if s = a ​ r b s=ar^{b} for some a ∈ ℚ a\in\mathbb{Q} and there does not exist an integer k > 1 k>1 such that k k divides r r and k b k^{b} divides s s. Hence the largest positive integer that satisfies the visibility criterion is 1 1. Thus gcd b ⁡ ( r, s) = 1 \ggcd_{b}(r,s)=1.

For the other direction, suppose that gcd b ⁡ ( r, s) = 1 \ggcd_{b}(r,s)=1. Then k = 1 k=1 is the largest integer such that k k divides r r and k b k^{b} divides s s and the point ( r, s) (r,s) does not satisfy Condition 2 of Definition 1. Also, note that for every pair ( r, s) (r,s), there exists a unique a = s / r b ∈ ℚ a=s/r^{b}\in\mathbb{Q} such that s = a ​ r b s=ar^{b}. Hence ( r, s) (r,s) is b b -visible. ∎

Note that in the classical b = 1 b=1 setting of lattice point visibility, a point ( r, s) (r,s) is visible if and only if gcd ⁡ ( r, s) = 1 \gcd(r,s)=1. Hence, Proposition 3 generalizes the condition for a lattice point to be b b -visible via the generalized greatest common divisor gcd b \ggcd_{b} as stated in Definition 2. We also remark that the same integer lattice point can be b b -visible and b ′ b^{\prime} -invisible for distinct b b and b ′ b^{\prime}. We illustrate this in the following example.

###### Example 4.

In Figure 4 the dotted curve is f ⁡ ( x) = 7 ​ x f(x)=7x, the dashed curve is g ⁡ ( x) = x 2 g(x)=x^{2}, and the solid curve is h ⁡ ( x) = 1 7 ​ x 3 h(x)=\frac{1}{7}x^{3}. A white node denotes a visible point, while a black node denotes an invisible point. In particular, the white-black point at ( 7, 49) (7,49) is not 1-visible since gcd ⁡ ( 7, 49) = 7 \gcd(7,49)=7 and is not 2-visible since gcd 2 ⁡ ( 7, 49) = 7 \ggcd_{2}(7,49)=7. However it is 3-visible since gcd 3 ⁡ ( 7, 49) = 1 \ggcd_{3}(7,49)=1.

\circlerighthalfblack \circlerighthalfblack (1,7) (2,14) (3,21) (4,28) (5,35) (6,42) (8,56) (1,1) (2,4) (3,9) (4,16) (5,25) (6,36) (7,49) (8,64) 1 2 3 4 5 6 7 8 7 14 21 28 35 42 49 56 63 70[image: Refer to caption] Figure 4. Invisible and visible points under different lines of sights.

## 3. Proportion of b b -visible lattice points

The literature on lattice point visibility presents rigorous proofs of the b = 1 b=1 case of Theorem 1, in particular in Monthly articles by Casey and Sadler [7, Theorem 1] and Christopher [11, Theorem 1]. Other recent proofs (see [1, 6]) give illuminating plausibility arguments but are merely heuristic sketches as there is no uniform probability distribution on the natural numbers and these arguments gloss over this important fact. However, these proofs can be made rigorous by the methods presented by Pinsky [23]. Following an analogous method, we now present a proof of our result regarding the proportion of b b -visible points in the lattice, for b ≥ 1 b\geq 1.

###### Proof of Theorem 1.

Fix N, b ∈ ℕ N,b\in\mathbb{N}. Let [N]:= { 1, 2, …, N } [N]:=\{1,2,\ldots,N\}. Let r, s r,s be two numbers picked independently with uniform probability in [N] [N] and fix a prime p p in [N] [N]. By Proposition 3, a point ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} is b b -visible if and only if gcd b ⁡ ( r, s) = 1 \ggcd_{b}(r,s)=1. Let P N P_{N} denote the probability that p p divides r r and p b p^{b} divides s s. There are ⌊ N p ⌋ \left\lfloor{\frac{N}{p}}\right\rfloor integers in [N] [N] that are divisible by p p; namely p, 2 ​ p, …, ⌊ N p ⌋ ​ p p,2p,\ldots,\left\lfloor{\frac{N}{p}}\right\rfloor p. Thus the probability that p p divides r r is 1 N ​ ⌊ N p ⌋ \frac{1}{N}\left\lfloor{\frac{N}{p}}\right\rfloor. Similarly, the probability that p b p^{b} divides s s is 1 N ​ ⌊ N p b ⌋ \frac{1}{N}\left\lfloor{\frac{N}{p^{b}}}\right\rfloor. By mutual independence, the probability that p p divides r r and that p b p^{b} divides s s is P N = 1 N 2 ​ ⌊ N p ⌋ ​ ⌊ N p b ⌋ P_{N}=\frac{1}{N^{2}}\left\lfloor{\frac{N}{p}}\right\rfloor\left\lfloor{\frac{N}{p^{b}}}\right\rfloor. Therefore, the probability that p p does not divide r r or that p b p^{b} does not divide s s is 1 − P N 1-P_{N}. Since P N → 1 p b + 1 P_{N}\rightarrow\frac{1}{p^{b+1}} as N → ∞ N\rightarrow\infty, by multiplying over all of the primes we have that the probability that p p does not divide r r or that p b p^{b} does not divide s s given that p p is prime is

 | lim N → ∞ ∏ p ​ prime p ≤ N ( 1 − P N) = ∏ p ​ prime ( 1 − 1 p b + 1) = 1 ζ ⁡ ( b + 1), \displaystyle\lim_{N\rightarrow\infty}\prod_{\begin{subarray}{c}p\;\text{prime}\\ p\leq N\end{subarray}}\left(1-P_{N}\right)=\prod_{p\;\text{prime}}\left(1-\frac{1}{p^{b+1}}\right)=\frac{1}{\zeta(b+1)}, |  |

where ζ ⁡ ( s) = ∏ p ​ prime ( 1 − 1 / p s) − 1 \zeta(s)=\prod_{p\;\text{prime}}\left(1-1/p^{s}\right)^{-1}. ∎

## 4. Arbitrarily large b b -invisible forests

We exploit the Chinese remainder theorem to prove that arbitrarily large m × n m\times n arrays of adjacent b b -invisible integer lattice points in the plane exist for every b ∈ ℕ b\in\mathbb{N}. We call such arrays of points b b -invisible rectangular forests of size m × n m\times n.

###### Proof of Theorem 2.

It suffices to show that there exists a pair ( r, s) ∈ ℕ × ℕ (r,s)\in\mathbb{N}\times\mathbb{N} such that gcd b ⁡ ( r + i, s + j) ≠ 1 \ggcd_{b}(r+i,s+j)\neq 1 for all 0 ≤ i < n 0\leq i<n and 0 ≤ j < m 0\leq j<m. To obtain a pair ( r, s) (r,s), we first choose m ​ n mn distinct primes and label them p i, j p_{i,j} where 0 ≤ i < n 0\leq i<n and 0 ≤ j < m 0\leq j<m. Place the primes in a matrix as follows

 | P m × n = ( p 0, m − 1 p 1, m − 1 ⋯ p n − 1, m − 1 ⋰ p 0, 1 p 1, 1 ⋯ p n − 1, 1 p 0, 0 p 1, 0 ⋯ p n − 1, 0). P_{m\times n}=\begin{pmatrix}p_{0,m-1}&p_{1,m-1}&\cdots&p_{n-1,m-1}\\ \vdots&\vdots&\iddots&\vdots\\ p_{0,1}&p_{1,1}&\cdots&p_{n-1,1}\\ p_{0,0}&p_{1,0}&\cdots&p_{n-1,0}\end{pmatrix}. |  |

The choice of the nonstandard indexing of the entries in the matrix P m × n P_{m\times n} will become clear at the proof’s conclusion. Set C i = ∏ j = 0 m − 1 p i, j C_{i}=\prod_{j=0}^{m-1}p_{i,j} and R j = ∏ i = 0 n − 1 p i, j R_{j}=\prod_{i=0}^{n-1}p_{i,j} and consider the following systems of linear congruences:

 | { r + 0 ≡ 0 ( mod C 0) r + 1 ≡ 0 ( mod C 1) ⋮ r + ( n − 1) ≡ 0 ( mod C n − 1) and { s + 0 ≡ 0 ( mod R 0 b) s + 1 ≡ 0 ( mod R 1 b) ⋮ s + ( m − 1) ≡ 0 ( mod R m − 1 b). \begin{cases}\hskip 28.45274ptr+0&\equiv 0\pmod{C_{0}}\\ \hskip 28.45274ptr+1&\equiv 0\pmod{C_{1}}\\ &\hskip 2.84526pt\vdots\\ r+(n-1)&\equiv 0\pmod{C_{n-1}}\end{cases}\hskip 21.68121pt\mbox{and}\hskip 21.68121pt\begin{cases}\hskip 28.45274pts+0&\equiv 0\pmod{R_{0}^{b}}\\ \hskip 28.45274pts+1&\equiv 0\pmod{R_{1}^{b}}\\ &\hskip 2.84526pt\vdots\\ s+(m-1)&\equiv 0\pmod{R_{m-1}^{b}}.\end{cases} |  |

The integers in the set { C i } i = 0 n − 1 \{C_{i}\}_{i=0}^{n-1} are pairwise relatively prime. Thus, by the Chinese remainder theorem, there exists a unique solution r r. Similarly the integers in the set { R j } j = 0 m − 1 \{R_{j}\}_{j=0}^{m-1} are pairwise relatively prime and hence there is a unique solution s ( mod ∏ j = 0 m − 1 R j b) s\pmod{\prod_{j=0}^{m-1}R_{j}^{b}}.

For each 0 ≤ i < n 0\leq i<n and 0 ≤ j < m 0\leq j<m, we have by construction that C i C_{i} divides r + i r+i and R j b R_{j}^{b} divides s + j s+j, and thus p i, j p_{i,j} divides r + i r+i and p i, j b p_{i,j}^{b} divides s + j s+j. Hence p i, j p_{i,j} divides gcd b ⁡ ( r + i, s + j) \ggcd_{b}(r+i,s+j) and so gcd b ⁡ ( r + i, s + j) ≠ 1 \ggcd_{b}(r+i,s+j)\neq 1. Hence every point ( r + i, s + j) ∈ ℕ × ℕ (r+i,\,s+j)\in\mathbb{N}\times\mathbb{N} with 0 ≤ i < n 0\leq i<n and 0 ≤ j < m 0\leq j<m is b b -invisible, as desired. ∎

The proof of Theorem 2 constructs b b -invisible forests of any dimension. We illustrate this process below by constructing a 2 2 -invisible forest of size 2 × 3 2\times 3.

###### Example 5.

Consider the prime matrix

 | P 2 × 3 = ( 7 11 13 2 3 5). P_{2\times 3}=\left(\begin{array}[]{ccc}7&11&13\\ 2&3&5\end{array}\right). |  |

Using the technique described in Theorem 2, we compute the unique solution r 0 ( mod N) r_{0}\pmod{N} and s 0 ( mod N 2) s_{0}\pmod{N^{2}}, where N = 2 ⋅ 3 ⋅ 5 ⋅ 7 ⋅ 11 ⋅ 13 N=2\cdot 3\cdot 5\cdot 7\cdot 11\cdot 13, to the required system of linear congruences

 | r 0 = r + 0 \displaystyle r_{0}=r+0 | = 27818 = 2 ⋅ 7 ⋅ 1987 \displaystyle=27818=2\cdot 7\cdot 1987 |  |

 | r 1 = r + 1 \displaystyle r_{1}=r+1 | = 27819 = 3 2 ⋅ 11 ⋅ 281 \displaystyle=27819=3^{2}\cdot 11\cdot 281 |  |

 | r 2 = r + 2 \displaystyle r_{2}=r+2 | = 27820 = 2 2 ⋅ 5 ⋅ 13 ⋅ 107 \displaystyle=27820=2^{2}\cdot 5\cdot 13\cdot 107 |  |

 | s 0 = s + 0 \displaystyle s_{0}=s+0 | = 602202600 = 2 3 ⋅ 3 5 ⋅ 5 2 ⋅ 12391 \displaystyle=602202600=2^{3}\cdot 3^{5}\cdot 5^{2}\cdot 12391 |  |

 | s 1 = s + 1 \displaystyle s_{1}=s+1 | = 602202601 = 7 2 ⋅ 11 2 ⋅ 13 2 ⋅ 601. \displaystyle=602202601=7^{2}\cdot 11^{2}\cdot 13^{2}\cdot 601. |  |

The forest we have constructed is shown in Figure 5 with each corresponding value gcd 2 ⁡ ( r i, s j) \ggcd_{2}(r_{i},s_{j}) noted in red. One can easily verify that each of the six lattice points is 2 2 -invisible; indeed as the proof of Theorem 2 states, each prime p i, j p_{i,j} in the prime matrix P 2 × 3 P_{2\times 3} divides the corresponding point ( r i, s j) (r_{i},s_{j}).

( r 0, s 0) (r_{0},s_{0}) ( r 0, s 1) (r_{0},s_{1}) ( r 1, s 0) (r_{1},s_{0}) ( r 1, s 1) (r_{1},s_{1}) ( r 2, s 0) (r_{2},s_{0}) ( r 2, s 1) (r_{2},s_{1}) 2 2 7 7 3 2 3^{2} 11 11 2 ⋅ 5 2\cdot 5 13 13 Figure 5. A 2 2 -invisible forest of size 2 × 3 2\times 3.

Although Theorem 2 provides a way to find b b -invisible forests of an arbitrary size, it does not necessarily indicate which ones will be close to the origin. Finding the closest known invisible square forests (when b = 1 b=1) was explored by Goodrich, Mbirika, and Nielsen [15]. In fact, using techniques from [15], we find a closer hidden forest with ( r, s) = ( 440, 38024) (r,s)=(440,38024). An exhaustive computer implementation confirms that this is the closest 2 2 -invisible forest of size 2 × 3 2\times 3 in the first quadrant. We end by posing the following b b -visibility problem: For fixed values b, n, m ∈ ℕ b,n,m\in\mathbb{N}, find the nearest b b -invisible forest of dimension n × m n\times m.

ACKNOWLEDGMENTS. We thank Stephan Garcia for helpful references and for a conversation at REUF4 at ICERM in Summer 2012 which motivated the fourth author’s interest in lattice point visibility. We also thank the undergraduate UW-Eau Claire research students Austin Goodrich, Jasmine Nielsen, Michele Gebert, and Sara DeBrabander who studied lattice point visibility both in the classic and generalized cases with us.

## References

- [1] A. D. Abrams, M. J. Paris, The probability that ( a, b) = 1 (a,b)=1, *College Math. J.*23 (1992) 47, [http://dx.doi.org/10.2307/2686199][3].
- [2] S. D. Adhikari, Some questions regarding visibility of lattice integer points on ℝ d \mathbb{R}^{d}, in: D.R. Heath-Brown, B.Z. Moroz (Eds.), *Proceedings of the Session in Analytic Number Theory and Diophantine Equations*(Bonn, January-June 2002), *Bonner Math. Schriften*Vol. 360, Math. Inst. Univ. Bonn, Bonn (2003) 1–8.
- [3] S. D. Adhikari, A. Granville, Visibility in the plane, *J. of Number Theory*129 (2009) 2335–2345, [http://dx.doi.org/10.1016/j.int.2009.02.019][4].
- [4] T. T. Allen, Pólya’s orchard problem, *Amer. Math. Monthly*93 (1986) 98–104, [http://dx.doi.org/10.2307/2322700][5].
- [5] T. M. Apostol, *Introduction to Analytic Number Theory*. Springer-Verlag, New York-Heidelberg, 1976, [http://dx.doi.org/10.1007/978-3-662-28579-4][6].
- [6] T. M. Apostol, Lattice points, *Cubo Mat. Educ.*2 (2000) 157–173.
- [7] S. D. Casey, B. M. Sadler, Pi, the primes, periodicities, and probability, *Amer. Math. Monthly*120 (2013) 594–608, [http://dx.doi.org/10.4169/amer.math.monthly.120.07.594][7].
- [8] E. Cesàro, Question proposée 75. *Mathesis*1 (1881) 184.
- [9] —, Question 75 (Solution), *Mathesis*3 (1883) 224–225.
- [10] Y. Chen, L. Cheng, Visibility of lattice points, *Acta Arith.*107 (2003) 203–207, [http://dx.doi.org/10.4064/aa107-3-1][8].
- [11] J. Christopher, The asymptotic density of some k k -dimensional sets, *Amer. Math. Monthly*63 (1956) 399–401, [http://dx.doi.org/10.2307/2309400][9].
- [12] J. M. De Koninck, J. B. Friedlander, F. Luca, On strings of consecutive integers with a distinct number of prime factors, *Proc. Amer. Math. Soc.*137 (2009) 1585–1592, [http://dx.doi.org/10.1090/S0002-9939-08-09702-5][10].
- [13] P. G. L. Dirichlet, Über die Bestimmung der mittleren Werte in der Zahlentheorie, *Abhandl. Kgl. Preuß Akad. Wiss.*, Berlin (1849) 63–83.
- [14] R. B. Eggleton, J. S. Kimberly, J. A. MacDougall, Runs of integers with equally many distinct prime factors, *Bull. Inst. Comb. Appl.*64 (2012) 30–38.
- [15] A. Goodrich, A. Mbirika, J. Nielsen, New methods to find patches of invisible integer lattice points, Preprint available at [https://people.uwec.edu/mbirika/lattice_point_paper.pdf][11].
- [16] F. Herzog, B. M. Stewart, Patterns of Visible and Nonvisible Lattice Points, *Amer. Math. Monthly*78 (1971) 487–496, [http://dx.doi.org/10.2307/2317753][12].
- [17] S. Laishram, F. Luca, Rectangles of nonvisible lattice points, *J. Integer Seq.*18 (2015) Article 15.10.8, 11.
- [18] J. D. Laison, M. Schick, Seeing dots: visibility of lattice points, *Math. Mag.*80 (2007) 274–282.
- [19] N. Nicholson, R. Rachan, On weak lattice point visibility, *Involve*9 (2016) 411–414, [http://dx.doi.org/10.2140/involve.2016.9.411][13].
- [20] J. E. Nymann, On the probability that k k positive integers are relatively prime, *J. Number Theory*4 (1972) 469–473, [http://dx.doi.org/10.1016/0022-314X(72)90038-8][14].
- [21] J. E. Nymann, On the probability that k k positive integers are relatively prime II, *J. Number Theory*7 (1975) 406–412, [http://dx.doi.org/10.1016/0022-314X(75)90044-X][15].
- [22] G. Pighizzini, J. Shallit, Unary language operations, state complexity and Jacobsthal’s function, *Int. J. Found. Comput. Sci.*13 (2002) 145–159, [http://dx.doi.org/10.1142/S012905410200100X][16].
- [23] R. G. Pinsky, Problems from the Discrete to the Continuous, Springer International Publishing Switzerland, 2014, [http://dx.doi.org/10.1007/978-3-319-07965-3][17].
- [24] G. Pólya, Zahlentheoretisches und wahrscheinlichkeitstheoretisches über die sichtweite im walde, *Arch. Math. Phys. Ser.*2 27 (1918), 135–142.
- [25] P. Schumer, Strings of strongly composite integers and invisible lattice points, *College Math. J.*21 (1990) 37–40, [http://dx.doi.org/10.2307/2686720][18].
- [26] J. J. Sylvester, Sur le nombre de fractions ordinaires inégales qu’on peut exprimer en se servant de chiffres qui n’excèdent pas un nombre donné, *C. R. Acad. Sci. Paris*XCVI (1883) 409–413.
- [27] S. Wolfram, A New Kind of Science, Wolfram Media, Inc., Champaign, IL, 2002.

EDRAY HERBER GOINS grew up in South Los Angeles, California. He works in the field of number theory, as it pertains to the intersection of representation theory and algebraic geometry. He is currently the president of the National Association of Mathematics.
Department of Mathematics, Purdue University, West Lafayette IN 47906
egoins@purdue.edu

PAMELA E. HARRIS received her PhD degree in mathematics from the University of Wisconsin Milwaukee, held a postdoctoral position at the United Stated Military Academy, and is now an Assistant Professor of Mathematics at Williams College. Her research interests are in algebra and combinatorics, particularly as these subjects relate to the representation theory of Lie algebras. Her service commitments aim to increase the visibility of Latinx and Hispanic mathematicians via platforms such as [http://www.lathisms.org][19].
Department of Mathematics and Statistics, Williams College, Williamstown MA 01267
peh2@williams.edu

BETHANY KUBIK received her PhD from North Dakota State University, held a postdoctoral position at the United States Military Academy, and is now an Assistant Professor at University of Minnesota Duluth. Her research interests include homological algebra, factorization, and graph theory.
Department of Mathematics and Statistics, University of Minnesota Duluth, Duluth MN 55812
bakubik@d.umn.edu

ABA MBIRIKA received his PhD from University of Iowa, held a postdoctoral position at Bowdoin College, and very recently in Fall 2017 became an Associate Professor of Mathematics at University of Wisconsin-Eau Claire. His mathematical interests include combinatorial representation theory, complex reflection groups, lattice point visibility, and graph labelings. aBa (his preferred spelling) does not know how to drive, but he happily bikes even in the Wisconsin winters. His answer to the question “Where are you from?” is always Iowa because in his graduate school years there, Iowa City became his favorite place on Earth.
Department of Mathematics, University of Wisconsin-Eau Claire, Eau Claire WI 54701
mbirika@uwec.edu


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://dx.doi.org/10.2307/2686199
[4]: http://dx.doi.org/10.1016/j.int.2009.02.019
[5]: http://dx.doi.org/10.2307/2322700
[6]: http://dx.doi.org/10.1007/978-3-662-28579-4
[7]: http://dx.doi.org/10.4169/amer.math.monthly.120.07.594
[8]: http://dx.doi.org/10.4064/aa107-3-1
[9]: http://dx.doi.org/10.2307/2309400
[10]: http://dx.doi.org/10.1090/S0002-9939-08-09702-5
[11]: https://people.uwec.edu/mbirika/lattice_point_paper.pdf
[12]: http://dx.doi.org/10.2307/2317753
[13]: http://dx.doi.org/10.2140/involve.2016.9.411
[14]: http://dx.doi.org/10.1016/0022-314X(72)90038-8
[15]: http://dx.doi.org/10.1016/0022-314X(75)90044-X
[16]: http://dx.doi.org/10.1142/S012905410200100X
[17]: http://dx.doi.org/10.1007/978-3-319-07965-3
[18]: http://dx.doi.org/10.2307/2686720
[19]: http://www.lathisms.org
