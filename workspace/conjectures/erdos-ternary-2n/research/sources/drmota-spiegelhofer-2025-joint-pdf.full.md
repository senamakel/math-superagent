<!-- source: https://arxiv.org/html/2501.00850v1 | converted from HTML -->

The joint distribution of binary and ternary digits sums

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2501.00850v1 [math.NT] 01 Jan 2025

# The joint distribution of binary and ternary digits sums Thanks: 1 This research was supported by the Austrian Science Foundation FWF, grant P36137-N, by the FWF–ANR joint projects ArithRand (grant numbers I4945-N and ANR-20-CE91-0006) and SymDynAr (grant numbers I6750 and ANR-23-CE40-0024-01). Thanks: ∗ Institute of Discrete Mathematics and Geometry, Technische Universität Wien, Wiedner Hauptstraße 8-10/113, A-1040 Wien, Austria Thanks: ∗∗ Department Mathematics and Information Technology, Montanuniversität Leoben, Austria

Michael Drmota ∗ and Lukas Spiegelhofer ∗∗

Date: August 11, 2026

###### Abstract.

We consider the sum-of-digits functions s 2 s_{2} and s 3 s_{3} in bases 2 2 and 3 3. These functions just return the minimal numbers of powers of two (resp. three) needed in order to represent a nonnegative integer as their sum. A result of the second author states that there are infinitely many *collisions*of s 2 s_{2} and s 3 s_{3}, that is, positive integers n n such that

 | s 2 ​ ( n) = s 3 ​ ( n). s_{2}(n)=s_{3}(n). |  |

This resolved a long-standing folklore conjecture.

In the present paper, we prove a strong generalization of this statement, stating that ( s 2 ​ ( n), s 3 ​ ( n)) (s_{2}(n),s_{3}(n)) attains almost all values in ℕ 2 \mathbb{N}^{2}, in the sense of asymptotic density. In particular, this yields *generalized collisions*: for any pair ( a, b) (a,b) of positive integers, the equation

 | a ​ s 2 ​ ( n) = b ​ s 3 ​ ( n) a\hskip 0.5pts_{2}(n)=b\hskip 0.5pts_{3}(n) |  |

admits infinitely many solutions in n n.

###### 1991 Mathematics Subject Classification

Primary: 11A63, Secondary: 11N60

## 1. Introduction and main result

The number 𝗌 q ​ ( n) \mathsf{s}_{q}(n), for natural numbers q ≥ 2 q\geq 2 and n n, is the sum of the base- q q digits of n n. Since the base- q q expansion of n n can be found by the greedy algorithm, it is the *lexicographically largest*representation of n n as sum of powers of q q. Using this, it is not difficult to show that 𝗌 q ​ ( n) \mathsf{s}_{q}(n) is the minimal number of powers of q q needed to represent n n as their sum:

 | 𝗌 q ( n) = min { k ≥ 0: there exist d 0, …, d k − 1 ∈ ℕ such that n = q d 0 + ⋯ + q d k − 1 }. \mathsf{s}_{q}(n)=\min\bigl\{k\geq 0:\mbox{there exist }d_{0},\ldots,d_{k-1}\in\mathbb{N}\mbox{ such that }n=q^{d_{0}}+\cdots+q^{d_{k-1}}\bigr\}. |  |

In the easiest case, the values of 𝗌 2 ​ ( n) \mathsf{s}_{2}(n), as n n varies in [2 λ, 2 λ + 1) [2^{\lambda},2^{\lambda+1}), are distributed according to a binomial distribution with parameters ( 1 / 2, λ) (1/2,\lambda). It is not surprising that in general, the values of 𝗌 q ​ ( n) \mathsf{s}_{q}(n) are asymptotically normally distributed [10, 18]. For example, the sum-of-digits function can be modeled by a sum of i.i.d. random variables on { 0, …, q − 1 } \{0,\ldots,q-1\} [9], from which the statement follows.

In the present paper, we consider the sum-of-digits function with respect to different bases p p and q q simultaneously. The corresponding normal distributions concentrate around values that are many standard deviations apart [6, 27]. Finding integers n n such that 𝗌 2 ​ ( n) − 𝗌 3 ​ ( n) \mathsf{s}_{2}(n)-\mathsf{s}_{3}(n) is small may therefore be expected to be a non-trivial problem.

Towards the end of the last century, the first author received a hand-written letter from A. Hildebrand, in which the following question was asked.

(1.1) |  | Are there infinitely many positive integers n n such that 𝗌 2 ​ ( n) = 𝗌 3 ​ ( n) \mathsf{s}_{2}(n)=\mathsf{s}_{3}(n)?  |  |

A natural number n n such that 𝗌 p ​ ( n) = 𝗌 q ​ ( n) \mathsf{s}_{p}(n)=\mathsf{s}_{q}(n) will be called *collision*of 𝗌 p \mathsf{s}_{p} and 𝗌 q \mathsf{s}_{q}, or ( p, q) (p,q) -collision, in this paper.

The first author [9] proved a statement on the joint distribution of 𝗌 2 ​ ( n) \mathsf{s}_{2}(n) and 𝗌 3 ​ ( n) \mathsf{s}_{3}(n), using among others Baker’s theorem on linear forms of logarithms. A corollary of the main result (Corollary 2 [9] states the following.

###### Corollary.

Let p, q > 1 p,q>1 be coprime integers. As N → ∞ N\rightarrow\infty, we have

 | 1 N #{ n < N: 𝗌 p ​ ( n) − ( p − 1) ​ log p ⁡ ( N) / 2 ( p 2 − 1) ​ log p ⁡ ( N) / 12 < y 1, 𝗌 q ​ ( n) − ( q − 1) ​ log q ⁡ ( N) / 2 ( q 2 − 1) ​ log q ⁡ ( N) / 12 < y 2 } → Φ ( y 1) Φ ( y 2). \frac{1}{N}\#\biggl\{n<N:\frac{\mathsf{s}_{p}(n)-(p-1)\log_{p}(N)/2}{\sqrt{(p^{2}-1)\log_{p}(N)/12}}<y_{1},\,\frac{\mathsf{s}_{q}(n)-(q-1)\log_{q}(N)/2}{\sqrt{(q^{2}-1)\log_{q}(N)/12}}<y_{2}\biggr\}\rightarrow\Phi(y_{1})\Phi(y_{2}). |  |

The statement of a *local version*of this result [9, Theorem 4] is at the core of our main theorem (Theorem 1.1 below).

###### Theorem (Drmota 2001).

Let p, q > 1 p,q>1 be coprime integers, and d = gcd ⁡ ( p − 1, q − 1) d=\gcd(p-1,q-1). As N → ∞ N\rightarrow\infty, we have uniformly for all integers k 1, k 2 ≥ 0 k_{1},k_{2}\geq 0 such that k 1 ≡ k 2 mod d k_{1}\equiv k_{2}\bmod d,

 |  | 1 N #{ n < N: 𝗌 p ( n) = k 1, 𝗌 q ( n) = k 2 } \displaystyle\frac{1}{N}\#\bigl\{n<N:\mathsf{s}_{p}(n)=k_{1},\mathsf{s}_{q}(n)=k_{2}\bigr\} |  |

 |  | = d ​ 1 2 ​ π ​ ( p 2 − 1) ​ log p ⁡ ( N) / 12 ​ exp ⁡ ( − ( k ℓ − ( p − 1) ​ log p ⁡ ( N) / 2) 2 2 ​ ( p 2 − 1) ​ log p ⁡ ( N) / 12) \displaystyle=d\frac{1}{\sqrt{2\pi(p^{2}-1)\log_{p}(N)/12}}\exp\biggl(-\frac{(k_{\ell}-(p-1)\log_{p}(N)/2)^{2}}{2(p^{2}-1)\log_{p}(N)/12}\biggr) |  |

 |  | × 1 2 ​ π ​ ( q 2 − 1) ​ log q ⁡ ( N) / 12 ​ exp ⁡ ( − ( k ℓ − ( q − 1) ​ log q ⁡ ( N) / 2) 2 2 ​ ( q 2 − 1) ​ log q ⁡ ( N) / 12) + o ⁡ ( ( log ⁡ N) − 1). \displaystyle\times\frac{1}{\sqrt{2\pi(q^{2}-1)\log_{q}(N)/12}}\exp\biggl(-\frac{(k_{\ell}-(q-1)\log_{q}(N)/2)^{2}}{2(q^{2}-1)\log_{q}(N)/12}\biggr)+o\bigl((\log N)^{-1}\bigr). |  |

Concerning similar values of 𝗌 2 \mathsf{s}_{2} and 𝗌 3 \mathsf{s}_{3}, Deshouillers, Habsieger, Laishram, and Landreau [6] write

“[…] it seems to be unknown whether there are infinitely many integers n n for which 𝗌 2 ​ ( n) = 𝗌 3 ​ ( n) \mathsf{s}_{2}(n)=\mathsf{s}_{3}(n) or even for which | 𝗌 2 ​ ( n) − 𝗌 3 ​ ( n) | \lvert\mathsf{s}_{2}(n)-\mathsf{s}_{3}(n)\rvert is significantly small.”

They prove the following theorem.

###### Theorem.

For sufficiently large N N, we have

 | #⁡ { n ≤ N: | 𝗌 3 ​ ( n) − 𝗌 2 ​ ( n) | ≤ 0.1457205 ​ log ⁡ n } > N 0.970359. \#\bigl\{n\leq N:\lvert\mathsf{s}_{3}(n)-\mathsf{s}_{2}(n)\rvert\leq 0.1457205\log n\bigr\}>N^{0.970359}. |  |

The result is nontrivial since 𝗌 3 ​ ( n) − 𝗌 2 ​ ( n) \mathsf{s}_{3}(n)-\mathsf{s}_{2}(n) usually has a value around c ​ log ⁡ n c\log n, where

 | c = 1 log ⁡ 3 − 1 log ⁡ 4 = 0.1888 ​ …. c=\frac{1}{\log 3}-\frac{1}{\log 4}=0.1888\ldots. |  |

Thus, they obtain in fact infinitely many n n such that | 𝗌 2 ​ ( n) − 𝗌 3 ​ ( n) | \lvert\mathsf{s}_{2}(n)-\mathsf{s}_{3}(n)\rvert is “significantly small”.

A partial refinement was given by La Bretèche, Stoll, and Tenenbaum [3]. They proved in particular that for all multiplicatively independent integers p, q ≥ 2 p,q\geq 2, the set

(1.2) |  | { 𝗌 p ​ ( n) / 𝗌 q ​ ( n): n ≥ 1 } \bigl\{\mathsf{s}_{p}(n)/\mathsf{s}_{q}(n):n\geq 1\} |  |

is dense in ℝ + \mathbb{R}^{+}.

The article [6] was the starting point of the paper [27] by the second author. Applying a rarefaction by some power of three, we aligned the expected values of 𝗌 2 \mathsf{s}_{2} and 𝗌 3 \mathsf{s}_{3}. The existence of infinitely many ( 2, 3) (2,3) -collisions was then established by means of a suitable *pre-selection of shifts*(see the three proof steps on page 482 of [27]).

###### Theorem (Spiegelhofer 2023).

There are infinitely many positive integers n n such that 𝗌 2 ​ ( n) = 𝗌 3 ​ ( n) \mathsf{s}_{2}(n)=\mathsf{s}_{3}(n).

The main theorem of the present paper yields this result, as well as the local theorem by Drmota stated above, and the special case ( p, q) = ( 2, 3) (p,q)=(2,3) of the La Bretèche–Stoll–Tenenbaum result as corollaries.

###### Theorem 1.1.

Suppose that 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, where c 2 > 0 c_{2}>0. Then, we have uniformly for K K in this range and for all integers k 1, k 2 ≥ 0 k_{1},k_{2}\geq 0, as N → ∞ N\to\infty,

 | 1 N #{ n < N | s 2 ( 3 K n) = k 1, s 3 ( n) = k 2 } \displaystyle\frac{1}{N}\#\left\{n<N\left|s_{2}(3^{K}n)=k_{1},s_{3}(n)=k_{2}\right.\right\} |  |

 | = 1 2 ​ π ​ 1 4 ​ log 2 ⁡ ( N ​ 3 K) ​ exp ⁡ ( − ( k 1 − 1 2 ​ log 2 ⁡ ( N ​ 3 K)) 2 1 2 ​ log 2 ⁡ ( N ​ 3 K)) \displaystyle\quad=\frac{1}{\sqrt{2\pi\frac{1}{4}\log_{2}(N\,3^{K})}}\exp\left(-\frac{\left(k_{1}-\frac{1}{2}\log_{2}(N\,3^{K})\right)^{2}}{\frac{1}{2}\log_{2}(N\,3^{K})}\right) |  |

 | × 1 2 ​ π ​ 2 3 ​ log 3 ​ N ​ exp ⁡ ( − ( k 2 − log 3 ⁡ N) 2 4 3 ​ log 3 ​ N) \displaystyle\qquad\times\frac{1}{\sqrt{2\pi\frac{2}{3}\log_{3}N}}\exp\left(-\frac{\left(k_{2}-\log_{3}N\right)^{2}}{\frac{4}{3}\log_{3}N}\right) |  |

 | + o ⁡ ( ( log ⁡ N) − 1). \displaystyle\quad+o\left((\log N)^{-1}\right). |  |

An analogous statement holds with reversed roles of 2 2 and 3 3: in this case, rarefaction by 2 K 2^{K} with s 3 ​ ( 2 K ​ n) s_{3}(2^{K}n) for even n n and s 3 ​ ( 2 K ​ n + 1) s_{3}(2^{K}n+1) for odd n n is used.

Combining the two parts of this theorem, we obtain the following corollary.

###### Theorem 1.2.

For every δ > 0 \delta>0 there exists K 0 > 0 K_{0}>0 such that for every pair of integers ( k 1, k 2) (k_{1},k_{2}) with

 | k 1 ≥ K 0, k 2 ≥ K 0, k 1 ≥ δ ​ k 2, k 2 ≥ δ ​ k 1, k_{1}\geq K_{0},\ k_{2}\geq K_{0},\ k_{1}\geq\delta k_{2},\ k_{2}\geq\delta k_{1}, |  |

there exists a non-negative integer n n satisfying

 | 𝗌 2 ​ ( n) = k 1 and 𝗌 3 ​ ( n) = k 2. \mathsf{s}_{2}(n)=k_{1}\quad\mbox{and}\quad\mathsf{s}_{3}(n)=k_{2}. |  |

This result means that the pairs ( 𝗌 2 ​ ( n), 𝗌 3 ​ ( n)) (\mathsf{s}_{2}(n),\mathsf{s}_{3}(n)) range over almost all possible pairs ( k 1, k 2) (k_{1},k_{2}). Actually this result is best possible, in the light of the following result by Senge and Straus [22]: for every pair ( k 1, k 2) (k_{1},k_{2}) of positive integers there are at most finitely many non-negative integers n n such that 𝗌 2 ​ ( n) = k 1 \mathsf{s}_{2}(n)=k_{1} and 𝗌 3 ​ ( n) = k 2 \mathsf{s}_{3}(n)=k_{2}.

Specializing further, Theorem 1.2 immediately yields the following result.

###### Corollary 1.1.

Assume that a, b ≥ 1 a,b\geq 1 are integers. There exist infinitely many natural numbers n n such that

(1.3) |  | a ​ 𝗌 2 ​ ( n) = b ​ 𝗌 3 ​ ( n). a\hskip 0.75pt\mathsf{s}_{2}(n)=b\hskip 0.75pt\mathsf{s}_{3}(n). |  |

### 1.1. Further directions

#### 1.1.1. Catalan numbers, and n! n! in base 12 12.

By Legendre’s identity (valid for primes p p) we have

(1.4) |  | ( p − 1) ​ ∑ 1 ≤ k ≤ n ν p ​ ( k) = n − 𝗌 p ​ ( n), (p-1)\sum_{1\leq k\leq n}\nu_{p}(k)=n-\mathsf{s}_{p}(n), |  |

and we see that the p p -valuation of factorials, and hence combinatorial counting sequences formed by products of factorials, is intimately tied to the sum-of-digits function in base p p. For example, there is a direct connection between ( 2, 3) (2,3) -collisions and the base- 12 12 expansion of n! n! [4, 5, 8]. By ( 1.4), the integer n ≥ 0 n\geq 0 is a collision if and only if

 | ν 2 ​ ( n!) = n − 𝗌 2 ​ ( n) = 2 ​ n − 𝗌 3 ​ ( n) 2 = 2 ​ ν 3 ​ ( n!). \nu_{2}(n!)=n-\mathsf{s}_{2}(n)=2\hskip 0.75pt\frac{n-\mathsf{s}_{3}(n)}{2}=2\hskip 0.75pt\nu_{3}(n!). |  |

This is the case if and only if n! n! is *exactly divisible by*some power of 2 2 ⋅ 3 1 = 12 2^{2}\cdot 3^{1}=12, in symbols, 12 k ∣ ∣ n! 12^{k}\mid\hskip-0.8pt\mid n! for some k k, where

 | 12 k ∣ ∣ m ⟺ 12 k ∣ m and gcd ( 12, m / 12 k) = 1. 12^{k}\mid\hskip-0.8pt\mid m\quad\Longleftrightarrow\quad 12^{k}\mid m\quad\textsf{and}\quad\gcd(12,m/12^{k})=1. |  |

In this case, and in this case only, the *last significant base- 12 12 digit*ℓ 12 ​ ( n!) \ell_{12}(n!) of n! n! is an element of { 1, 5, 7, 11 } \{1,5,7,11\}. Summarizing, we have the equivalences

(1.5) |  | 𝗌 2 ​ ( n) = 𝗌 3 ​ ( n) if and only if ν 2 ​ ( n!) = 2 ​ ν 3 ​ ( n!) if and only if 12 k ∣ ∣ n! for some k if and only if ℓ 12 ​ ( n!) ∈ { 1, 5, 7, 11 }. \begin{array}[]{ll}\mathsf{s}_{2}(n)=\mathsf{s}_{3}(n)&\mbox{{if and only if}}\\[8.53581pt] \nu_{2}(n!)=2\hskip 0.75pt\nu_{3}(n!)&\mbox{{if and only if}}\\[8.53581pt] 12^{k}\mid\hskip-0.8pt\mid n!\mbox{ for some }k&\mbox{{if and only if}}\\[8.53581pt] \ell_{12}(n!)\in\{1,5,7,11\}.\end{array} |  |

Together with J.-M. Deshouillers and P. Jelinek [7], second author proved that ℓ 12 ​ ( n!) \ell_{12}(n!) attains each digit in { 1, …, 11 } \{1,\ldots,11\} infinitely many times, thus refining the theorem on the infinitude of ( 2, 3) (2,3) -collisions.

A related question concerns the 2 2 -and 3 3 -valuations of *Catalan numbers*[11, 17],

 | C n = 1 n + 1 ​ ( 2 ​ n n). C_{n}=\frac{1}{n+1}\binom{2n}{n}. |  |

###### Conjecture 1.1.

Assume that a, b ≥ 1 a,b\geq 1 are integers. There exist infinitely many positive integers n n such that

(1.6) |  | a ​ ν 2 ​ ( C n) = b ​ ν 3 ​ ( C n). a\hskip 0.75pt\nu_{2}\bigl(C_{n}\bigr)=b\hskip 0.75pt\nu_{3}\bigl(C_{n}\bigr). |  |

If gcd ⁡ ( a, b) = 1 \gcd(a,b)=1, this states that C n C_{n} is exactly divisible by some power of 2 b ​ 3 a 2^{b}3^{a} infinitely often.

More generally, in the spirit of our main theorem (Theorem 1.1), we could ask whether ( ν 2 ​ ( C n), ν 3 ​ ( C n)) (\nu_{2}(C_{n}),\nu_{3}(C_{n})) attains all values in the set

 | { ( k 1, k 2) ∈ ℕ 2: | k 1 + i k 2 | > K, ε < arg ( k 1 + i k 2) < π / 2 − ε }, \bigl\{(k_{1},k_{2})\in\mathbb{N}^{2}:\lvert k_{1}+ik_{2}\rvert>K,\varepsilon<\arg(k_{1}+ik_{2})<\pi/2-\varepsilon\bigr\}, |  |

where ε > 0 \varepsilon>0, and K = K ⁡ ( ε) K=K(\varepsilon) is large enough. We leave this as another open problem.

#### 1.1.2.

Collisions in different bases. P. Jelinek (private communication) announced a proof of the existence of infinitely many collisions with respect to any pair ( p, q) (p,q) of coprime bases p, q ≥ 2 p,q\geq 2. As a possible extension, we could again ask for corresponding statements concerning the prime factorization of Catalan numbers.

Collisions in more than two bases — 𝗌 p ​ ( n) = 𝗌 q ​ ( n) = 𝗌 r ​ ( n) \mathsf{s}_{p}(n)=\mathsf{s}_{q}(n)=\mathsf{s}_{r}(n) — are in general certainly very difficult to handle. For example, it follows from work in progress by Jelinek that there exist infinitely many such collisions for some triples of bases, but it is not so clear what happens in the general case. If two of the three bases are much larger than the third, we would need to reduce significantly the sum of digits in two bases synchronously in order to obtain a collision. Currently we do not see a way to achieve this. In this context, it might be of interest to recall an ergodic conjecture [16] by Furstenberg, concerning *multiplicatively independent*integer bases p, q ≥ 2 p,q\geq 2: let dim H ( A) \dim_{H}(A) be the Hausdorff dimension of a set A ⊆ [0, 1] A\subseteq[0,1], and define

 | O a ​ ( x) ≔ { a k ​ x mod 1: k ∈ ℕ } O_{a}(x)\coloneqq\bigl\{a^{k}x\bmod 1:k\in\mathbb{N}\bigr\} |  |

Then

(1.7) |  | dim H ( O p ​ ( x) ¯) + dim H ( O q ​ ( x) ¯) ≥ 1 \dim_{H}\bigl(\overline{O_{p}(x)}\bigr)+\dim_{H}\bigl(\overline{O_{q}(x)}\bigr)\geq 1 |  |

for all irrational x ∈ [0, 1] x\in[0,1]. In other words, the base- p p and base- q q expansions of an irrational number cannot be “simple” at the same time (see Shmerkin [23] and Wu [32] for partial solutions of this conjecture, and Adamczewski–Faverjon [1] for solutions of several problems concerning the joint representation of a number in two bases).

### 1.2. Auxiliary results

Theorem 1.1 (and consequently Theorem 1.2) follows directly from the following two propositions (see Section 2).

###### Proposition 1.1.

Suppose that c 2 > 0 c_{2}>0 is a real number. There exists c > 0 c>0 such that uniformly for all integers K ≥ 0 K\geq 0 satisfying 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, and all real t 1 t_{1} and t 2 t_{2},

 | S 1 ( i) = ∑ n < N, n ≡ i mod 2 e ⁡ ( t 1 ​ 𝗌 2 ​ ( 3 K ​ n) + t 2 ​ 𝗌 3 ​ ( n)) ≪ N ​ exp ⁡ ( − c ​ log ⁡ N ​ ‖ t 1 ‖ 2) S_{1}^{(i)}=\sum_{n<N,\,n\equiv i\bmod 2}e\left(t_{1}\mathsf{s}_{2}(3^{K}n)+t_{2}\mathsf{s}_{3}(n)\right)\ll N\,\exp\left(-c\log N\|t_{1}\|^{2}\right) |  |

and

 | S 2 ( i) = ∑ n < N, n ≡ i mod 2 e ⁡ ( t 1 ​ 𝗌 2 ​ ( n) + t 2 ​ 𝗌 3 ​ ( 2 K ​ n + r)) ≪ N ​ exp ⁡ ( − c ​ log ⁡ N ​ ‖ 2 ​ t 2 ‖ 2). S_{2}^{(i)}=\sum_{n<N,\,n\equiv i\bmod 2}e\left(t_{1}\mathsf{s}_{2}(n)+t_{2}\mathsf{s}_{3}(2^{K}n+r)\right)\ll N\,\exp\left(-c\log N\|2t_{2}\|^{2}\right). |  |

for i, r ∈ { 0, 1 } i,r\in\{0,1\}.

###### Remark 1.1.

We will prove in detail only the first of these formulas, while the proof of the second is analogous. These two statements correspond to the adjusting the expected values of 𝗌 2 \mathsf{s}_{2} and 𝗌 3 \mathsf{s}_{3} in opposite directions, thus allowing for 𝗌 2 ​ ( n) / 𝗌 3 ​ ( n) \mathsf{s}_{2}(n)/\mathsf{s}_{3}(n) to be “large” and “small”, respectively.

###### Proposition 1.2.

Suppose that c 2 > 0 c_{2}>0 is a real number. Then we have uniformly for all integers K ≥ 0 K\geq 0 satisfying 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, and all real t 1 t_{1} and t 2 t_{2}

 | S 1 ( i) \displaystyle S_{1}^{(i)} | = ∑ n < N ​ n ≡ i mod 2 e ⁡ ( t 1 ​ s 2 ​ ( 3 K ​ n) + t 2 ​ s 3 ​ ( n)) = N 2 ​ e ​ ( t 1 2 ​ log 2 ⁡ ( 3 K ​ N) + t 2 ​ log 3 ⁡ ( N)) \displaystyle=\sum_{n<N\,n\equiv i\bmod 2}e\left(t_{1}s_{2}(3^{K}n)+t_{2}s_{3}(n)\right)=\frac{N}{2}\,e\left(\frac{t_{1}}{2}\log_{2}(3^{K}N)+t_{2}\log_{3}(N)\right) |  |

 |  | × exp ⁡ ( − π 2 2 ​ t 1 2 ​ log 2 ⁡ ( 3 K ​ N) − 4 ​ π 2 3 ​ t 2 2 ​ log 3 ⁡ ( N)) + o ⁡ ( N) \displaystyle\times\exp\left(-\frac{\pi^{2}}{2}t_{1}^{2}\log_{2}(3^{K}N)-\frac{4\pi^{2}}{3}t_{2}^{2}\log_{3}(N)\right)+o(N) |  |

and

 | S 2 ( i) \displaystyle S_{2}^{(i)} | = ∑ n < N ​ n ≡ i mod 2 e ⁡ ( t 1 ​ s 2 ​ ( n) + t 2 ​ s 3 ​ ( 2 K ​ n)) = N 2 ​ e ​ ( t 1 2 ​ log 2 ⁡ ( N) + t 2 ​ log 3 ⁡ ( 2 K ​ N)) \displaystyle=\sum_{n<N\,n\equiv i\bmod 2}e\left(t_{1}s_{2}(n)+t_{2}s_{3}(2^{K}n)\right)=\frac{N}{2}\,e\left(\frac{t_{1}}{2}\log_{2}(N)+t_{2}\log_{3}(2^{K}N)\right) |  |

 |  | × exp ⁡ ( − π 2 2 ​ t 1 2 ​ log 2 ⁡ ( N) − 4 ​ π 2 3 ​ t 2 2 ​ log 3 ⁡ ( 2 K ​ N + r)) + o ⁡ ( N) \displaystyle\times\exp\left(-\frac{\pi^{2}}{2}t_{1}^{2}\log_{2}(N)-\frac{4\pi^{2}}{3}t_{2}^{2}\log_{3}(2^{K}N+r)\right)+o(N) |  |

for i, r ∈ { 0, 1 } i,r\in\{0,1\}.

### 1.3. Plan of the paper.

We will prove first that Propositions 1.1 and 1.2 imply the main theorems. In a short section we collect some Diophantine properties that will be then used in the subsequent two sections that are concerned with the proofs of Propositions 1.1 and 1.2.

###### Notation 1.1.

The symbol log \log denotes the natural logarithm, and log a = 1 log ⁡ a ​ log \log_{a}=\frac{1}{\log a}\log is the logarithm in base a > 1 a>1. We use Landau notation, employing the symbols 𝒪 \mathcal{O}, ≪ \ll, and o o. The symbol f ⁡ ( n) ≍ g ⁡ ( n) f(n)\asymp g(n) abbreviates the statement ( f ⁡ ( n) ≪ g ⁡ ( n) CLOSE \bigl(f(n)\ll g(n) and OPEN g ⁡ ( n) ≪ f ⁡ ( n)) g(n)\ll f(n)\bigr), while f ⁡ ( n) ∼ g ⁡ ( n) f(n)\sim g(n) means that f ⁡ ( n) / g ⁡ ( n) f(n)/g(n) converges to 1 1 as n → ∞ n\rightarrow\infty. We also use the exponential e ⁡ ( x) = exp ⁡ ( 2 ​ π ​ ix) \e(x)=\exp(2\pi ix). For M ≥ 0 M\geq 0, the statement “ a a is M M -close to b b ” means | a − b | ≤ M \lvert a-b\rvert\leq M.

## 2. Propositions 1.1 and 1.2 imply Theorems 1.1 and 1.2

.

We set S 1 ( i) = S 1 ( i) ​ ( t 1, t 2) S_{1}^{(i)}=S_{1}^{(i)}(t_{1},t_{2}) as in Propositions 1.1 and 1.2. Then we have

 | #{ n < N: s 2 ( 3 K n) = k 1, s 3 ( n) = k 2 } = ∬ [− 1 / 2, 1 / 2] 2 ( S 1 ( 0) ( t 1, t 2) + S 1 ( 1) ( t 1, t 2)) e ( − t 1 k 1 − t 2 k 2) d t 1 d t 2. \#\{n<N:s_{2}(3^{K}n)=k_{1},\ s_{3}(n)=k_{2}\}=\iint_{[-1/2,1/2]^{2}}\left(S_{1}^{(0)}(t_{1},t_{2})+S_{1}^{(1)}(t_{1},t_{2})\right)e(-t_{1}k_{1}-t_{2}k_{2})\,dt_{1}\,dt_{2}. |  |

Futhermore we set

 | C L ( 0) = [− L log ⁡ N, L log ⁡ N] 2, C L ( 1) = [− L log ⁡ N, L log ⁡ N] × ( [− 1 2, − 1 2 + L log ⁡ N] ∪ [1 2 − L log ⁡ N, 1 2]) C_{L}^{(0)}=\left[-\frac{L}{\sqrt{\log N}},\frac{L}{\sqrt{\log N}}\right]^{2},\quad C_{L}^{(1)}=\left[-\frac{L}{\sqrt{\log N}},\frac{L}{\sqrt{\log N}}\right]\times\left(\left[-\frac{1}{2},-\frac{1}{2}+\frac{L}{\sqrt{\log N}}\right]\cup\left[\frac{1}{2}-\frac{L}{\sqrt{\log N}},\frac{1}{2}\right]\right) |  |

and

 | A L = [− 1 2, 1 2] 2 ∖ ( C L ( 0) ∪ C L ( 1)). A_{L}=\left[-\frac{1}{2},\frac{1}{2}\right]^{2}\setminus(C_{L}^{(0)}\cup C_{L}^{(1)}). |  |

By Proposition 1.1 it directly follows that.

 | I 1 = ∬ A L | S 1 ( i) ​ ( t 1, t 2) | ​ d ​ t 1 ​ d ​ t 2 ≪ N ​ e − c ​ L 2 log ⁡ N. I_{1}=\iint_{A_{L}}|S_{1}^{(i)}(t_{1},t_{2})|\,dt_{1}\,dt_{2}\ll N\frac{e^{-cL^{2}}}{\log N}. |  |

Next we apply Propositions 1.2 and observe that for every ε > 0 \varepsilon>0 there exists N 0 = N 0 ​ ( ε) N_{0}=N_{0}(\varepsilon) such that

 | | S 1 ( i) ​ ( t 1, t 2) − N 2 ​ e ​ ( t 1 2 ​ log 2 ⁡ ( 3 K ​ N) + t 2 ​ log 3 ⁡ ( N)) ​ exp ⁡ ( − π 2 2 ​ t 1 2 ​ log 2 ⁡ ( 3 K ​ N) − 4 ​ π 2 3 ​ t 2 2 ​ log 3 ⁡ ( N)) | ≤ ε ​ N \left|S_{1}^{(i)}(t_{1},t_{2})-\frac{N}{2}\,e\left(\frac{t_{1}}{2}\log_{2}(3^{K}N)+t_{2}\log_{3}(N)\right)\exp\left(-\frac{\pi^{2}}{2}t_{1}^{2}\log_{2}(3^{K}N)-\frac{4\pi^{2}}{3}t_{2}^{2}\log_{3}(N)\right)\right|\leq\varepsilon N |  |

for all N ≥ N 0 N\geq N_{0} and (uniformly) for all real t 1, t 2 t_{1},t_{2} and i ∈ { 0, 1 } i\in\{0,1\}. In order to calculate the integral

 | I 2 = ∬ C L ( 0) ∪ C L ( 1) ( S 1 ( 0) ​ ( t 1, t 2) + S 1 ( 1) ​ ( t 1, t 2)) ​ e ​ ( − t 1 ​ k 1 − t 2 ​ k 2) ​ d ​ t 1 ​ d ​ t 2 I_{2}=\iint_{C_{L}^{(0)}\cup C_{L}^{(1)}}\left(S_{1}^{(0)}(t_{1},t_{2})+S_{1}^{(1)}(t_{1},t_{2})\right)e(-t_{1}k_{1}-t_{2}k_{2})\,dt_{1}\,dt_{2} |  |

we observe that (due to the fact that s 3 ​ ( n) ≡ n mod 2 s_{3}(n)\equiv n\bmod 2) we have the relation S 1 ( i) ​ ( t 1, t 2 + 1 / 2) = ( − 1) i ​ S 1 ( i) ​ ( t 1, t 2) S_{1}^{(i)}(t_{1},t_{2}+1/2)=(-1)^{i}S_{1}^{(i)}(t_{1},t_{2}) and consequently

 | ∬ C L ( 1) S 1 ( i) ​ ( t 1, t 2) ​ e ​ ( − t 1 ​ k 1 − t 2 ​ k 2) ​ d ​ t 1 ​ d ​ t 2 \displaystyle\iint_{C_{L}^{(1)}}S_{1}^{(i)}(t_{1},t_{2})e(-t_{1}k_{1}-t_{2}k_{2})\,dt_{1}\,dt_{2} | = ∬ C L ( 0) S 1 ( i) ​ ( t 1, t 2 + 1 / 2) ​ e ​ ( − t 1 ​ k 1 − ( t 2 + 1 / 2) ​ k 2) ​ d ​ t 1 ​ d ​ t 2 \displaystyle=\iint_{C_{L}^{(0)}}S_{1}^{(i)}(t_{1},t_{2}+1/2)e(-t_{1}k_{1}-(t_{2}+1/2)k_{2})\,dt_{1}\,dt_{2} |  |

 |  | = ( − 1) ​ i + k 2 ​ ∬ C L ( 0) S 1 ( i) ​ ( t 1, t 2) ​ e ​ ( − t 1 ​ k 1 − t 2 ​ k 2) ​ d ​ t 1 ​ d ​ t 2 \displaystyle=(-1){i+k_{2}}\iint_{C_{L}^{(0)}}S_{1}^{(i)}(t_{1},t_{2})e(-t_{1}k_{1}-t_{2}k_{2})\,dt_{1}\,dt_{2} |  |

Thus

 | I 2 = 2 ​ ∬ C L ( 0) S 1 ( k 2 mod 2) ​ ( t 1, t 2) ​ e ​ ( − t 1 ​ k 1 − t 2 ​ k 2) ​ d ​ t 1 ​ d ​ t 2. I_{2}=2\iint_{C_{L}^{(0)}}S_{1}^{(k_{2}\bmod 2)}(t_{1},t_{2})e(-t_{1}k_{1}-t_{2}k_{2})\,dt_{1}\,dt_{2}. |  |

Next we use the simple formula

 | ∫ | t | ≤ C e i ​ A ​ t − t 2 2 ​ B ​ 𝑑 t = 2 ​ π B ​ e − A 2 2 ​ B + O ⁡ ( 1 B ​ C ​ e − C 2 ​ B 2) \int_{|t|\leq C}e^{iAt-\frac{t^{2}}{2}B}\,dt=\sqrt{\frac{2\pi}{B}}e^{-\frac{A^{2}}{2B}}+O\left(\frac{1}{BC}e^{-\frac{C^{2}B}{2}}\right) |  |

and Propostion 1.2 and obtain

 | I 2 \displaystyle I_{2} | = N 2 3 ​ π ​ log 2 ⁡ ( 3 K ​ N) ​ log 3 ⁡ ( N CLOSE ​ exp ⁡ ( − 2 ​ Δ 1 2 log 2 ⁡ ( 3 K ​ N) − 3 ​ Δ 2 2 4 ​ log 3 ​ ( N)) \displaystyle=\frac{N}{\sqrt{\frac{2}{3}\pi\log_{2}(3^{K}N)\log_{3}(N}}\exp\left(-\frac{2\Delta_{1}^{2}}{\log_{2}(3^{K}N)}-\frac{3\Delta_{2}^{2}}{4\log_{3}(N)}\right) |  |

 |  | + O ⁡ ( N L ​ log ⁡ N ​ e − c ​ L 2) + O ⁡ ( N ​ L 2 ​ ε log ⁡ N) \displaystyle+O\left(\frac{N}{L\log N}e^{-cL^{2}}\right)+O\left(N\frac{L^{2}\varepsilon}{\log N}\right) |  |

for some constant c > 0 c>0, where

 | Δ 1 = k 1 − 1 2 ​ log 2 ⁡ ( 3 K ​ N) and Δ 2 = k 2 − log 3 ⁡ ( N). \Delta_{1}=k_{1}-\frac{1}{2}\log_{2}(3^{K}N)\quad\mbox{and}\quad\Delta_{2}=k_{2}-\log_{3}(N). |  |

Finally we can choose

 | L = ⌊ ( 1 / c) ​ log ⁡ ( 1 / ε) ⌋ L=\lfloor\sqrt{(1/c)\log(1/\varepsilon)}\rfloor |  |

so that the error term sums up to

 | O ⁡ ( N log ⁡ N ​ ε ​ log ⁡ ( 1 / ε)) O\left(\frac{N}{\log N}\varepsilon\log(1/\varepsilon)\right) |  |

for N ≥ N 0 ​ ( ε) N\geq N_{0}(\varepsilon). This proves the first part of Theorem 1.1.

The proof of the second part is very similar. The only difference is that we use s 3 ​ ( 2 K ​ n) s_{3}(2^{K}n) to cover even k 2 k_{2} and s 3 ​ ( 2 K ​ n + 1) s_{3}(2^{K}n+1) to cover odd k 2 k_{2}.

For the proof of Theorem+ 1.2 we fix δ > 0 \delta>0 and set

 | c 2 = 1 log ⁡ 3 ​ ( 2 ​ log ⁡ 2 δ ​ log ⁡ 3 − 1). c_{2}=\frac{1}{\log 3}\left(\frac{2\log 2}{\delta\log 3}-1\right). |  |

With this parameter we apply Theorem 1.1 and now choose N 0 N_{0} large enough such that the error term o ⁡ ( ( log ⁡ N) − 1) o((\log N)^{-1}) in Theorem 1.1 is negligible for all N ≥ N 0 N\geq N_{0} compared to the main term

 | T:= N 2 ​ π ​ 1 4 ​ log 2 ⁡ ( N ​ 3 K) ​ exp ⁡ ( − Δ 1 2 1 2 ​ log 2 ⁡ ( N ​ 3 K)) ​ 1 2 ​ π ​ 2 3 ​ log 3 ​ N ​ exp ⁡ ( − Δ 2 2 4 3 ​ log 3 ​ N) T:=\frac{N}{\sqrt{2\pi\frac{1}{4}\log_{2}(N\,3^{K})}}\exp\left(-\frac{\Delta_{1}^{2}}{\frac{1}{2}\log_{2}(N\,3^{K})}\right)\frac{1}{\sqrt{2\pi\frac{2}{3}\log_{3}N}}\exp\left(-\frac{\Delta_{2}^{2}}{\frac{4}{3}\log_{3}N}\right) |  |

when | Δ 1 | ≤ 1 + log ⁡ 3 2 ​ log ⁡ 2 |\Delta_{1}|\leq 1+\frac{\log 3}{2\log 2} and | Δ 2 | ≤ 1 |\Delta_{2}|\leq 1. Furthermore we can assume that the main term T T is greater than 1 1.

Now assume that ( k 1, k 2) (k_{1},k_{2}) is a pair of positive integers satisfying

 | log ⁡ 3 2 ​ log ⁡ 2 ≤ k 1 k 2 ≤ 1 δ \frac{\log 3}{2\log 2}\leq\frac{k_{1}}{k_{2}}\leq\frac{1}{\delta} |  |

and

 | max ⁡ { k 1, k 2 } ≥ K 0:= log ⁡ N 0 δ ​ log ⁡ 3 + 1. \max\{k_{1},k_{2}\}\geq K_{0}:=\frac{\log N_{0}}{\delta\log 3}+1. |  |

We then choose N ≥ N 0 N\geq N_{0} and 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N such that

 | | Δ 1 | = | k 1 − log 3 ⁡ N | ≤ 1 and | Δ 2 | = | k 2 − 1 2 ​ log 2 ⁡ ( 3 K ​ N) | ≤ 1 + log ⁡ 3 2 ​ log ⁡ 2. |\Delta_{1}|=|k_{1}-\log_{3}N|\leq 1\quad\mbox{and}\quad|\Delta_{2}|=\left|k_{2}-\frac{1}{2}\log_{2}(3^{K}N)\right|\leq 1+\frac{\log 3}{2\log 2}. |  |

With this choice Theorem 1.1 shows that

 | #{ n < N: s 2 ( 3 K n) = k 1, s 3 ( n) = k 2 } = T ( 1 + o ( 1)) > 1. \#\{n<N:s_{2}(3^{K}n)=k_{1},\ s_{3}(n)=k_{2}\}=T(1+o(1))>1. |  |

This proves Theorem 1.2 in the case k 1 / k 2 ≥ log ⁡ 3 / ( 2 ​ log ⁡ 2) k_{1}/k_{2}\geq\log 3/(2\log 2). The other case runs along the same lines.

## 3. Diophantine Properties

The first property (Lemma 3.2, compare also with [9, 13]) follows from Baker’s theorem on linear forms of logarithms (see [31]).

###### Lemma 3.1.

Let α 1, α 2, …, α n \alpha_{1},\alpha_{2},\ldots,\alpha_{n} be non-zero algebraic numbers and b 1, b 2, …, b n b_{1},b_{2},\ldots,b_{n} integers such that

 | α 1 b 1 ⋯ α n b n ≠ 1 \alpha_{1}^{b_{1}}\cdots\alpha_{n}^{b_{n}}\neq 1 |  |

and let A 1, A 2, …, A n ≥ e A_{1},A_{2},\ldots,A_{n}\geq e real numbers with log ⁡ A j ≥ h ⁡ ( α j) \log A_{j}\geq h(\alpha_{j}), where h ⁡ ( ⋅) h(\cdot) denotes the absolute logarithmic height. Set d = [𝐐 ( α 1 …, α n): 𝐐] d=[{\bf Q}(\alpha_{1}\ldots,\alpha_{n}):{\bf Q}]. Then

 | | α 1 b 1 ⋯ α n b n − 1 | ≥ exp ( − U), \left|\alpha_{1}^{b_{1}}\cdots\alpha_{n}^{b_{n}}-1\right|\geq\exp\left(-U\right), |  |

where

 | U = 2 6 ​ n + 32 n 3 ​ n + 6 d n + 2 ( 1 + log d) ( log B + log d) log A 1 ⋯ log A n U=2^{6n+32}n^{3n+6}d^{n+2}(1+\log d)(\log B+\log d)\log A_{1}\cdots\log A_{n} |  |

and

 | B = max ⁡ { 2, | b 1 |, | b 2 |, …, | b n | }. B=\max\{2,|b_{1}|,|b_{2}|,\ldots,|b_{n}|\}. |  |

###### Lemma 3.2.

Let q 1, q 2 > 1 q_{1},q_{2}>1 be coprime integers and m 1, m 2 m_{1},m_{2} integers such that m 1 ≢ 0 mod q 1 m_{1}\not\equiv 0\bmod q_{1} and m 2 ≢ 0 mod q 2 m_{2}\not\equiv 0\bmod q_{2}. Then there exists a constant C > 0 C>0 such that for all positive integers k 0, k 1, k 2 > 1 k_{0},k_{1},k_{2}>1

 | | m 1 ​ q 2 k 0 q 1 k 1 + m 2 q 2 k 2 | ≥ max ( | m 1 | ​ q 2 k 0 q 1 k 1, | m 2 | q 2 k 2) ⋅ e − C log q 1 log q 2 log ( max ( k 1, k 0 + k 2)) ⋅ log ( max ( | m 1 |, | m 2 |)). \left|\frac{m_{1}q_{2}^{k_{0}}}{q_{1}^{k_{1}}}+\frac{m_{2}}{q_{2}^{k_{2}}}\right|\geq\max\left(\frac{|m_{1}|q_{2}^{k_{0}}}{q_{1}^{k_{1}}},\frac{|m_{2}|}{q_{2}^{k_{2}}}\right)\cdot e^{-C\log q_{1}\log q_{2}\log\left(\max(k_{1},k_{0}+k_{2})\right)\cdot\log(\max\left(|m_{1}|,|m_{2}|\right))}. |  |

###### Proof.

Since q 1, q 2 > 1 q_{1},q_{2}>1 are coprime integers and m 1 ≢ 0 mod q 1 m_{1}\not\equiv 0\bmod q_{1}, m 2 ≢ 0 mod q 2 m_{2}\not\equiv 0\bmod q_{2} we surely have m 1 ​ q 1 − k 1 ​ q 2 k 0 + m 2 ​ q 2 − k 2 ≠ 0 m_{1}q_{1}^{-k_{1}}q_{2}^{k_{0}}+m_{2}q_{2}^{-k_{2}}\neq 0. So can apply Lemma 3.1 for n = 3 n=3, α 1 = q 1 \alpha_{1}=q_{1}, α 2 = q 2 \alpha_{2}=q_{2}, α 3 = − m 2 / m 1 \alpha_{3}=-m_{2}/m_{1}, b 1 = k 1 b_{1}=k_{1}, b 2 = − k 2 b_{2}=-k_{2}, b 3 = 1 b_{3}=1 and directly obtain

 | | m 1 ​ q 2 k 0 q 1 k 1 + m 2 q 2 k 2 | \displaystyle\left|\frac{m_{1}q_{2}^{k_{0}}}{q_{1}^{k_{1}}}+\frac{m_{2}}{q_{2}^{k_{2}}}\right| | = | m 1 | ⋅ q 1 − k 1 ​ q 2 k 0 ⋅ | − q 1 k 1 ​ q 2 − k 0 − k 2 ​ m 2 m 1 − 1 | \displaystyle=|m_{1}|\cdot q_{1}^{-k_{1}}q_{2}^{k_{0}}\cdot\left|-q_{1}^{k_{1}}q_{2}^{-k_{0}-k_{2}}\frac{m_{2}}{m_{1}}-1\right| |  |

 |  | ≥ | m 1 | q 1 − k 1 q 2 k 0 e − C log q 1 log q 2 log ( max ( k 1, k 0 + k 2)) ⋅ log max ( | m 1 |, | m 2 |). \displaystyle\geq|m_{1}|q_{1}^{-k_{1}}q_{2}^{k_{0}}e^{-C\log q_{1}\log q_{2}\log\left(\max(k_{1},k_{0}+k_{2})\right)\cdot\log\max\left(|m_{1}|,|m_{2}|\right)}. |  |

In the same way we get the lower bound

 | | m 1 ​ q 2 k 0 q 1 k 1 + m 2 q 2 k 2 | ≥ | m 2 | q 2 − k 2 e − C log q 1 log q 2 log ( max ( k 1, k 0 + k 2)) ⋅ log max ( | m 1 |, | m 2 |) \left|\frac{m_{1}q_{2}^{k_{0}}}{q_{1}^{k_{1}}}+\frac{m_{2}}{q_{2}^{k_{2}}}\right|\geq|m_{2}|q_{2}^{-k_{2}}e^{-C\log q_{1}\log q_{2}\log\left(\max(k_{1},k_{0}+k_{2})\right)\cdot\log\max\left(|m_{1}|,|m_{2}|\right)} |  |

which completes the proof of the lemma. ∎

The second one follows from the p p -adic version of the subspace theorem by Schlickewei [15, Theorem 1.8].

###### Lemma 3.3.

Let r ≥ n ≥ 2 r\geq n\geq 2, C > 0 C>0, δ > 0 \delta>0 and S = { ∞, p 1, …, p t } S=\{\infty,p_{1},\ldots,p_{t}\}, where p 1, …, p t p_{1},\ldots,p_{t} are distinct prime numbers. Further, let L 1, ∞, …, L r, ∞ L_{1,\infty},\ldots,L_{r,\infty} be linear forms in X 1, …, X n X_{1},\ldots,X_{n} with algebraic coefficients in ℂ \mathbb{C} in general position, and for 1 ≤ j ≤ t 1\leq j\leq t, let L 1, p j, …, L r, p j L_{1,p_{j}},\ldots,L_{r,p_{j}} be linear forms in X 1, …, X n X_{1},\ldots,X_{n} with algebraic coefficients in ℚ ¯ p j \overline{\mathbb{Q}}_{p_{j}} in general position.

Then all integer solutions 𝐱 = ( x 1, …, x n) {\bf x}=(x_{1},\ldots,x_{n}) with gcd ⁡ ( x 1, …, x n) = 1 {\rm gcd}(x_{1},\ldots,x_{n})=1 of the inequality

(3.1) |  | ∏ p ∈ S | L 1, p ( 𝐱) ⋯ L r, p ( 𝐱) | p ≤ C ∥ 𝐱 ∥ ∞ r − n − δ \prod_{p\in S}\left|L_{1,p}({\bf x})\cdots L_{r,p}({\bf x})\right|_{p}\leq C\|{\bf x}\|_{\infty}^{r-n-\delta} |  |

are contained in the union of finitely many linear subspaces of ℚ n {\mathbb{Q}}^{n}.

The following two properties are corollaries of Lemma 3.3.

###### Lemma 3.4.

Suppose that q 1, q 2 q_{1},q_{2} are different prime numbers, that h 1, …, h d h_{1},\ldots,h_{d} are d ≥ 1 d\geq 1 integers not divisible by q 2 q_{2} and H H an integer not divisible by q 1 q_{1} such that

 | gcd ⁡ ( h 1, …, h d, H) = 1. {\rm gcd}(h_{1},\ldots,h_{d},H)=1. |  |

Then for every δ > 0 \delta>0 there exists M 0 M_{0} such that we have uniformly for all integer exponents k k, m 1, …, m d m_{1},\ldots,m_{d}, m m with k ≥ 0 k\geq 0, m 1 > m 2 > ⋯ > m d = 0 m_{1}>m_{2}>\cdots>m_{d}=0 and m ≥ max ⁡ ( m 1, M 0) m\geq\max(m_{1},M_{0}) the inequality

(3.2) |  | | q 1 k ​ ( q 2 m 1 ​ h 1 + ⋯ + q 2 m d ​ h d) − q 2 m ​ H | ≫ max ⁡ ( q 1 k ​ q 2 m 1, q 2 m ​ | H |) 1 − δ | h 1 h 2 ⋯ h d H |, \left|q_{1}^{k}\left(q_{2}^{m_{1}}h_{1}+\cdots+q_{2}^{m_{d}}h_{d}\right)-q_{2}^{m}H\right|\gg\frac{\max(q_{1}^{k}q_{2}^{m_{1}},q_{2}^{m}|H|)^{1-\delta}}{|h_{1}h_{2}\cdots h_{d}\,H|}, |  |

where the implicit constant depends just on δ \delta and d d.

###### Proof.

We apply Lemma 3.3 with r = d + 2 r=d+2, n = d + 1 n=d+1, C = 1 C=1, δ \delta, and the set S S that consists of ∞ \infty and of the primes q 1 q_{1} and q 2 q_{2}. For p ∈ S p\in S we set

 | L j, p = X j, ( 1 ≤ j ≤ d + 1), L d + 2, p = X 1 + X 2 + ⋯ + X d + 1, L_{j,p}=X_{j},\ (1\leq j\leq d+1),\ L_{d+2,p}=X_{1}+X_{2}+\cdots+X_{d+1}, |  |

that are obviously in general position. Hence for all coprime integer tuples 𝐱 = ( x 1, x 2, … ​ x d + 1) {\bf x}=(x_{1},x_{2},\ldots x_{d+1}) we either have

(3.3) |  | ∏ p ∈ S | ( x 1 + x 2 + ⋯ + x d + 1) x 1 x 2 ⋯ x d + 1 | p ≥ ∥ 𝐱 ∥ ∞ 1 − δ \prod_{p\in S}\left|(x_{1}+x_{2}+\cdots+x_{d+1})x_{1}x_{2}\cdots x_{d+1}\right|_{p}\geq\|{\bf x}\|_{\infty}^{1-\delta} |  |

or they are contained in finitely many linear subspaces of ℚ d + 1 {\mathbb{Q}}^{d+1}.

We now set

 | x j = q 1 k ​ q 2 m j ​ h j ​ ( 1 ≤ j ≤ d), x d + 1 = q 2 m ​ H. x_{j}=q_{1}^{k}q_{2}^{m_{j}}h_{j}\ (1\leq j\leq d),\ x_{d+1}=q_{2}^{m}H. |  |

Clearly we have

 | ‖ 𝐱 ‖ ∞ ≥ max ⁡ ( q 1 k ​ q 2 m 1, q 2 m ​ | H |). \|{\bf x}\|_{\infty}\geq\max\left(q_{1}^{k}q_{2}^{m_{1}},q_{2}^{m}|H|\right). |  |

By assumption m d = 0 m_{d}=0 and h d h_{d} is not divisible by q 2 q_{2}. Furthermore H H is not divisible by q 1 q_{1}. Consequently we have

 | gcd ⁡ ( q 1 k ​ q 2 m 1 ​ h 1, …, q 1 k ​ q 2 m d ​ h d, q 2 m ​ H) = gcd ⁡ ( h 1, …, h d, H) = 1. {\rm gcd}\left(q_{1}^{k}q_{2}^{m_{1}}h_{1},\ldots,q_{1}^{k}q_{2}^{m_{d}}h_{d},q_{2}^{m}H\right)={\rm gcd}\left(h_{1},\ldots,h_{d},H\right)=1. |  |

Suppose now that c 1 x 1 + ⋯ c d x d + c d + 1 x d + 1 = 0 c_{1}x_{1}+\cdots c_{d}x_{d}+c_{d+1}x_{d+1}=0 is one (of finitely many) equations for the exceptional rational subspaces, that is, we can assume that the coefficients c j c_{j} are integers and not all of them are zero. Actually, since all x j x_{j} are non-zero we can assume that at least two coefficients c j c_{j} are non-zero. In particular this implies that at least one of the coefficients c 1, …, c d c_{1},\ldots,c_{d} is non-zero.

Suppose first that d = 1 d=1. Then c 1 ≠ 0 c_{1}\neq 0 and m 1 = 0 m_{1}=0 and by considering the equation

 | c 1 ​ q 1 k ​ h 1 + c 2 ​ q 2 m ​ H = 0 c_{1}q_{1}^{k}h_{1}+c_{2}q_{2}^{m}H=0 |  |

modulo q 2 m q_{2}^{m} we get

 | c 1 ≡ 0 mod q 2 m. c_{1}\equiv 0\bmod q_{2}^{m}. |  |

If M 0 M_{0} is chosen large enough such that this relation is impossible for m ≥ M 0 m\geq M_{0} then there are no points of this form on one of the finitely many subspaces.

Next assume that d > 1 d>1 and that c d ≠ 0 c_{d}\neq 0. Here we consider the equation

 | c 1 ​ q 1 k ​ q 2 m 1 ​ h 1 + ⋯ + c d ​ q 1 k ​ q 2 m d ​ h d + c d + 1 ​ q 2 m ​ H = 0 c_{1}q_{1}^{k}q_{2}^{m_{1}}h_{1}+\cdots+c_{d}q_{1}^{k}q_{2}^{m_{d}}h_{d}+c_{d+1}q_{2}^{m}H=0 |  |

modulo q 2 m d − 1 q_{2}^{m_{d-1}}. Since m ≥ m 1 > ⋯ > m d − 1 > 0 m\geq m_{1}>\cdots>m_{d-1}>0, h d h_{d} is not divisibly by q 2 q_{2}, and q 1 q_{1} and q 2 q_{2} are different prime numbers it follows that

 | c d ≡ 0 mod q 2 m d − 1. c_{d}\equiv 0\bmod q_{2}^{m_{d-1}}. |  |

If m d − 1 m_{d-1} is sufficiently large this is certainly impossible.

Similarly as above, if c d = 0 c_{d}=0 but c d − 1 ≠ 0 c_{d-1}\neq 0 we get

 | c d − 1 ​ q 2 m d − 1 ≡ 0 mod q 2 m d − 2 or c d − 1 ≡ 0 mod q 2 m d − 2 − m d − 1. c_{d-1}q_{2}^{m_{d-1}}\equiv 0\bmod q_{2}^{m_{d-2}}\quad\mbox{or}\quad c_{d-1}\equiv 0\bmod q_{2}^{m_{d-2}-m_{d-1}}. |  |

Again this is impossible if m d − 2 − m d − 1 m_{d-2}-m_{d-1} is sufficiently large.

In this way we proceed further and observe that there exists a constant C > 0 C>0 (depending on δ \delta) such that ( x 1, …, x d, x d + 1) (x_{1},\ldots,x_{d},x_{d+1}) is not contained in any of the exceptional subspaces provided that m d − 1 ≥ C m_{d-1}\geq C, m d − 2 − m d − 1 ≥ C m_{d-2}-m_{d-1}\geq C, … \ldots, and m 2 − m 1 ≥ C m_{2}-m_{1}\geq C. In all these cases the inequality ( 3.3) is satisfied.

By definition we have

 | ∏ p ∈ S | q 1 ℓ 1 + ⋯ + ℓ d q 2 m 1 + ⋯ m d + m | p = 1 \prod_{p\in S}|q_{1}^{\ell_{1}+\cdots+\ell_{d}}q_{2}^{m_{1}+\cdots m_{d}+m}|_{p}=1 |  |

so that

 | ∏ p ∈ S | x 1 ⋯ x d + 1 | p = ∏ p ∈ S | h 1 ⋯ h d H | p ≤ | h 1 ⋯ h d H |. \prod_{p\in S}|x_{1}\cdots x_{d+1}|_{p}=\prod_{p\in S}|h_{1}\cdots h_{d}\,H|_{p}\leq|h_{1}\cdots h_{d}\,H|. |  |

Furthermore with | x 1 + ⋯ + x d + 1 | p ≤ 1 |x_{1}+\cdots+x_{d+1}|_{p}\leq 1 for p ≠ ∞ p\neq\infty it follows that ( 3.3) implies

 | | x 1 + ⋯ + x d + 1 | | h 1 ⋯ h d H | \displaystyle|x_{1}+\cdots+x_{d+1}|\,|h_{1}\cdots h_{d}\,H| | ≥ ∏ p ∈ S ∖ { ∞ } | x 1 + ⋯ x d + 1 | p | x 1 | p ⋯ | x d + 1 | p \displaystyle\geq\prod_{p\in S\setminus\{\infty\}}|x_{1}+\cdots x_{d+1}|_{p}|x_{1}|_{p}\cdots|x_{d+1}|_{p} |  |

 |  | ≥ max ⁡ ( | x 1 |, … ​ | x d + 1 |) 1 − δ \displaystyle\geq\max(|x_{1}|,\ldots|x_{d+1}|)^{1-\delta} |  |

 |  | ≥ max ⁡ ( q 1 k ​ q 2 m 1, q 2 m ​ | H |) 1 − δ \displaystyle\geq\max\left(q_{1}^{k}q_{2}^{m_{1}},q_{2}^{m}|H|\right)^{1-\delta} |  |

which is precisely ( 3.2).

Now suppose that m d − 1 ≤ C m_{d-1}\leq C. Then we put the terms

 | q 1 k ​ q 2 m d − 1 ​ h d − 1 + q 1 k ​ h d = q 1 k ​ ( q 2 m d − 1 ​ h d − 1 + h d) q_{1}^{k}q_{2}^{m_{d-1}}h_{d-1}+q_{1}^{k}h_{d}=q_{1}^{k}\left(q_{2}^{m_{d-1}}h_{d-1}+h_{d}\right) |  |

together and apply inductively the lemma for the case d − 1 d-1. Since q 2 m d − 1 ≤ q 2 C q_{2}^{m_{d-1}}\leq q_{2}^{C} is bounded we have

 | | q 2 m d − 1 ​ h d − 1 + h d | ≪ | h d − 1 ​ h d |. \left|q_{2}^{m_{d-1}}h_{d-1}+h_{d}\right|\ll|h_{d-1}h_{d}|. |  |

Thus, ( 3.2) follows by induction.

Similarly, if m d − 2 − m d − 1 ≥ C m_{d-2}-m_{d-1}\geq C then we group together the terms

 | q 1 k ​ q 2 m d − 2 ​ h d − 2 + q 1 k ​ q 2 m d − 1 ​ h d − 1 = q 1 k ​ q 2 m d − 1 ​ ( q 2 m d − 2 − m d − 1 ​ h d − 2 + h d − 1) q_{1}^{k}q_{2}^{m_{d-2}}h_{d-2}+q_{1}^{k}q_{2}^{m_{d-1}}h_{d-1}=q_{1}^{k}q_{2}^{m_{d-1}}\left(q_{2}^{m_{d-2}-m_{d-1}}h_{d-2}+h_{d-1}\right) |  |

and proceed in the same way. The remaining cases can be handled, too. However, we have to take care of the maximum max ⁡ ( q 1 k ​ q 2 m 1, q 2 m ​ | H |) \max(q_{1}^{k}q_{2}^{m_{1}},q_{2}^{m}|H|) if we group together

 | q 1 k ​ q 2 m 1 ​ h 1 + q 1 k ​ q 2 m 2 ​ h 2 = q 1 k ​ q 2 m 2 ​ ( q 2 m 1 − m 2 ​ h 1 + h 2). q_{1}^{k}q_{2}^{m_{1}}h_{1}+q_{1}^{k}q_{2}^{m_{2}}h_{2}=q_{1}^{k}q_{2}^{m_{2}}\left(q_{2}^{m_{1}-m_{2}}h_{1}+h_{2}\right). |  |

Since m 1 − m 2 ≤ C m_{1}-m_{2}\leq C we get

 | q 1 k ​ q 2 m 2 ≥ 1 q 2 C ​ q 1 k ​ q 2 m 1. q_{1}^{k}q_{2}^{m_{2}}\geq\frac{1}{q_{2}^{C}}q_{1}^{k}q_{2}^{m_{1}}. |  |

Thus, we can proceed by induction in all cases.

Summing up, we either get ( 3.2) directly or we reduce it to the case d − 1 d-1. Since the case d = 1 d=1 always holds (provided that m m is sufficiently large) the proof of the lemma is finished. ∎

###### Lemma 3.5.

Suppose that q 1, q 2 q_{1},q_{2} are different prime numbers, that h 1, …, h d 1 h_{1},\ldots,h_{d_{1}} are d 1 ≥ 1 d_{1}\geq 1 integers not divisible by q 2 q_{2}, r 1, …, r d 2 r_{1},\ldots,r_{d_{2}} are d 2 ≥ 1 d_{2}\geq 1 integers not divisible by q 1 q_{1} and H H an integer not divisible by q 1 ​ q 2 q_{1}q_{2} such that

 | gcd ⁡ ( h 1, …, h d 1, r 1, …, r d 2, H) = 1. {\rm gcd}(h_{1},\ldots,h_{d_{1}},r_{1},\ldots,r_{d_{2}},H)=1. |  |

Then for every δ > 0 \delta>0 there exists M 0 M_{0} such that we have uniformly for all integer exponents k k, m 1, …, m d 1 m_{1},\ldots,m_{d_{1}}, M M, n 1, …, n d 2 n_{1},\ldots,n_{d_{2}}, N N with k ≥ 0 k\geq 0, m 1 > m 2 > ⋯ > m d 1 = 0 m_{1}>m_{2}>\cdots>m_{d_{1}}=0, M ≥ max ⁡ ( m 1, M 0) M\geq\max(m_{1},M_{0}), n 1 > n 2 > ⋯ > n d 2 = 0 n_{1}>n_{2}>\cdots>n_{d_{2}}=0, and N ≥ max ⁡ ( n 1, M 0) N\geq\max(n_{1},M_{0}) the inequality

 |  | | q 1 k ​ ( q 2 m 1 ​ h 1 + ⋯ + q 2 m d 1 ​ h d 1) + q 1 n 1 ​ r 1 + ⋯ + q 1 n d 2 ​ r d 2 − q 1 N ​ q 2 M ​ H | \displaystyle\left|q_{1}^{k}\left(q_{2}^{m_{1}}h_{1}+\cdots+q_{2}^{m_{d_{1}}}h_{d_{1}}\right)+q_{1}^{n_{1}}r_{1}+\cdots+q_{1}^{n_{d_{2}}}r_{d_{2}}-q_{1}^{N}q_{2}^{M}H\right| |  |

(3.4) |  |  | ≫ max ⁡ ( q 1 k ​ q 2 m 1, q 1 n 1, q 1 N ​ q 2 M ​ | H |) 1 − δ | h 1 h 2 ⋯ h d 1 r 1 r 2 ⋯ r d 2 H |, \displaystyle\gg\frac{\max(q_{1}^{k}q_{2}^{m_{1}},q_{1}^{n_{1}},q_{1}^{N}q_{2}^{M}|H|)^{1-\delta}}{|h_{1}h_{2}\cdots h_{d_{1}}r_{1}r_{2}\cdots r_{d_{2}}\,H|}, |  |

where the implicit constant depends just on δ \delta, d 1 d_{1}, and d 2 d_{2}.

###### Proof.

The proof of Lemma 3.5 is a direct extension of the proof of Lemma 3.4. ∎

## 4. Proof of Proposition 1.1

For an integer M ≥ 1 M\geq 1, let L ⁡ ( M) L(M) denote the length of the longest block of 0 0 s or 1 1 s in the binary expansion of M M. The following lemma states that almost all powers of 3 3 only have short runs of 0 0 s or 1 1 s, where also multiplication by a factor M M is taken into account. This inconspicious lemma is in fact the key to the proof of Proposition 1.1, as it enables us to eliminate binary digits of powers of 3 3 with indices lying in an interval (Corollary 4.1 below).

###### Lemma 4.1.

Assume that 0 ≤ η ≤ 1 0\leq\eta\leq 1. Then

(4.1) |  | sup 1 ≤ M < 2 η ​ K L ⁡ ( M ​ 3 K) ≤ η ​ K + o ⁡ ( K) \sup_{1\leq M<2^{\eta K}}L\bigl(M3^{K}\bigr)\leq\eta K+o(K) |  |

as K → ∞ K\rightarrow\infty. In particular,

- (1.)

the longest 0 0 -or 1 1 -blocks in the binary expansion of 3 K 3^{K} have length o ⁡ ( K) o(K) as K → ∞ K\to\infty.

- (2.)

For given ε > 0 \varepsilon>0 and η > 0 \eta>0, all sufficiently large K K satisfy

 | sup 1 ≤ M < 2 η ​ K L ⁡ ( M ​ 3 K) ≤ ( 1 + ε) ​ η ​ K. \sup_{1\leq M<2^{\eta K}}L\bigl(M3^{K}\bigr)\leq(1+\varepsilon)\eta K. |  |

###### Proof.

The proof is an application of Schlickewei’s p p -adic subspace theorem. Suppose that the binary expansion of M ​ 3 K M3^{K} has a 0 0 -block of length L L. Then M ​ 3 K M3^{K} can be represented as

 | M ​ 3 K = a + 2 k + L ​ b, M3^{K}=a+2^{k+L}b, |  |

where 0 < a ≤ 2 k 0<a\leq 2^{k} and 0 < b ≤ M ​ 3 K ​ 2 − k − L 0<b\leq M3^{K}2^{-k-L}. Hence,

 | | M ​ 3 K − 2 k + L ​ b | ≤ 2 k. |M3^{K}-2^{k+L}b|\leq 2^{k}. |  |

On the other hand we have (by a direct application of the p p -adic subspace theorem, see below)

(4.2) |  | | M ​ 3 K − 2 k + L ​ b | ≥ max ⁡ ( 3 K, 2 k + L ​ b) 1 − δ M ​ b ≥ ( 2 k + L ​ b) 1 − δ M ​ b |M3^{K}-2^{k+L}b|\geq\frac{\max(3^{K},2^{k+L}b)^{1-\delta}}{Mb}\geq\frac{(2^{k+L}b)^{1-\delta}}{Mb} |  |

or we have

 | c 1 ​ M ​ 3 K + c 2 ​ 2 k + L ​ b = 0 c_{1}M3^{K}+c_{2}2^{k+L}b=0 |  |

for one (or several) of finitely many integer pairs ( c 1, c 2) ≠ ( 0, 0) (c_{1},c_{2})\neq(0,0) that depend on δ \delta. However, by considering such an equation modulo 2 k + L 2^{k+L} it follows that

 | c 1 ≡ 0 mod 2 k + L c_{1}\equiv 0\bmod 2^{k+L} |  |

which is impossible if k + L k+L is sufficiently large.

Thus, if k + L k+L is sufficiently large we certainly have ( 4.2). Consequently we have

 | 2 k ≥ ( 2 k + L ​ b) 1 − δ M ​ b 2^{k}\geq\frac{(2^{k+L}b)^{1-\delta}}{Mb} |  |

or

 | 2 L ≤ M 1 1 − δ ​ ( 2 k ​ b) δ 1 − δ. 2^{L}\leq M^{\frac{1}{1-\delta}}(2^{k}b)^{\frac{\delta}{1-\delta}}. |  |

Since 2 k ​ b ≤ M ​ 3 K 2^{k}b\leq M3^{K} and M ≤ 2 K ​ η M\leq 2^{K\eta} it also follows that

 | L ≤ ( η 1 − δ + ( η ​ log ⁡ 2 + log ⁡ 3) ​ δ 1 − δ) ​ K. L\leq\biggl(\frac{\eta}{1-\delta}+\frac{(\eta\log 2+\log 3)\delta}{1-\delta}\biggr)K. |  |

Since δ > 0 \delta>0 can be chosen arbitrarily small it follows that L ≤ 2 ​ η ​ K + o ⁡ ( K) L\leq 2\eta K+o(K), as proposed. ∎

From Lemma 4.1 we derive the following corollary, similar in spirit to the “odd elimination lemma” in the manuscript [28] by the second author. To this end, let us introduce the convenient notation

(4.3) |  | n I ≔ ∑ a ≤ j < b δ j ​ ( n) ​ 2 j − a, n^{I}\coloneqq\sum_{a\leq j<b}\delta_{j}(n)2^{j-a}, |  |

for n ∈ ℕ n\in\mathbb{N} and an interval I = [a, b) I=[a,b) in ℕ \mathbb{N}, where δ j ​ ( n) \delta_{j}(n) is the base- 2 2 digit of n n at index n n.

###### Corollary 4.1 (Odd elimination).

Assume that ε, η > 0 \varepsilon,\eta>0, and assume that d d and k k are positive integers. For all K ≥ K 𝟢 ​ ( η, ε, k) K\geq K_{\mathsf{0}}(\eta,\varepsilon,k), the following statement holds.

For all nonnegative integers a, b a,b such that

 | ε ​ K ≤ a < b ≤ a + η ​ K, \varepsilon K\leq a<b\leq a+\eta K, |  |

and all ω ∈ { 0, …, 2 b − a − 1 } \omega\in\{0,\ldots,2^{b-a}-1\}, there exists A ∈ d + k ​ ℕ A\in d+k\mathbb{N} such that 0 < A ≤ 4 ​ k 2 ​ 2 2 ​ η ​ K + ε ​ K 0<A\leq 4k^{2}2^{2\eta K+\varepsilon K} and

 | ( A ​ 3 K) [a, b) = ω. \bigl(A3^{K}\bigr)^{[a,b)}=\omega. |  |

The idea of proof of this statement is the following. First, we choose a factor M ≥ 1 M\geq 1, by Dirichlet’s approximation theorem, such that M ​ 3 K M3^{K} does not have binary digits in the interval [a − m, b) [a-m,b), where m m is a small margin coming from the modulus k k. Due to Lemma 4.1 it is not possible that “too many” digits below a − m a-m are eliminated by such a multiplication. Therefore there exist binary digits equal to 0 0 and 1 1 not too far below the cleared interval of digits of M ​ 3 K M3^{K}. This will enable us to find a factor A A in a prescribed residue class: we will r require 2 ∤ A 2\nmid A in order to allow for uniform distribution of the lowest digits in base 2 2 (see ( 4.23) for details).

###### Proof of Corollary 4.1.

Choose m ≥ 1 m\geq 1 in such a way that 2 m − 1 ≤ k < 2 m 2^{m-1}\leq k<2^{m}. Let η ≥ 0 \eta\geq 0, and set κ ≔ b − a + m \kappa\coloneqq b-a+m. By Dirichlet’s approximation theorem we may choose an integer C = C ⁡ ( K) ∈ { 1, …, 2 κ } C=C(K)\in\{1,\ldots,2^{\kappa}\} in such a way that

 | ∥ C ​ 3 K ​ 2 − b ∥ < 2 − κ. \lVert C3^{K}2^{-b}\rVert<2^{-\kappa}. |  |

That is, the digits of C ​ 3 K C3^{K} with indices in the interval [a − m, b) [a-m,b) are all equal to 𝟶 \mathtt{0}, or all equal to 𝟷 \mathtt{1}. We need to find another integer A A lying in a prescribed residue class, having the sharper property that all the digits in the smaller interval [a, b) [a,b) are *equal*to 𝟶 \mathtt{0} (or any other digit combination on [a, b) [a,b). At this point, Schlickewei’s p p -adic subspace theorem enters in an essential way. Lemma 4.1 yields

 | L ⁡ ( C ​ 3 K) ≤ κ + o ⁡ ( K), L\bigl(C3^{K}\bigr)\leq\kappa+o(K), |  |

and we choose K K large enough (depending on η, ε, k \eta,\varepsilon,k), such that L ⁡ ( C ​ 3 K) < b − a + ε ​ K L\bigl(C3^{K}\bigr)<b-a+\varepsilon K and ε ​ K ≥ m \varepsilon K\geq m. Assume for a moment that ( C 2 K) [a − m, b) = 0 (C2^{K})^{[a-m,b)}=0. Since a ≥ ε ​ K a\geq\varepsilon K, there exists a maximal position c ∈ { 0, …, a − m − 1 } c\in\{0,\ldots,a-m-1\} such that δ c ​ ( C ​ 3 K) = 1 \delta_{c}(C3^{K})=1. (It follows that δ c + 1 ​ ( C ​ 3 K) = 0 \delta_{c+1}(C3^{K})=0). We “shift” this appearance of the digit 𝟷 \mathtt{1} by a − m − c < ε ​ K a-m-c<\varepsilon K places, to the position a − m a-m. Setting B = 2 a − m − c ​ C B=2^{a-m-c}C, we obtain

 | ( B 3 K) [a − m, b) = 2 a − m. (B3^{K})^{[a-m,b)}=2^{a-m}. |  |

For any given M ≥ 0 M\geq 0, the block of digits of r ​ k ​ B ​ 3 k + M rkB3^{k}+M with indices in the interval [a, b) [a,b) changes step by step, as r r is varied. More precisely, since we chose 2 m − 1 ≤ k < 2 m 2^{m-1}\leq k<2^{m}, this block attains each value once or twice, cycling through all 2 b − a 2^{b-a} possibilities. *In particular*, we may choose r < 2 b − a + 1 r<2^{b-a+1} in such a way that

 | ( r ​ k ​ B ​ 3 K + d ​ 3 K) [a, b) = ω \bigl(rkB3^{K}+d3^{K}\bigr)^{[a,b)}=\omega |  |

(where we can assume without loss of generality that 0 ≤ d < k 0\leq d<k). We set A ≔ r ​ k ​ B + d ∈ d + k ​ ℕ A\coloneqq rkB+d\in d+k\mathbb{N}. Collecting the estimates, we have C ≤ 2 ​ k ​ 2 η ​ K C\leq 2k2^{\eta K}, B ≤ 2 ε ​ K ​ C B\leq 2^{\varepsilon K}C, r + 1 ≤ 2 η ​ K + 1 r+1\leq 2^{\eta K+1}, and therefore A ≤ 4 ​ k 2 ​ 2 2 ​ η ​ K + ε ​ K A\leq 4k^{2}2^{2\eta K+\varepsilon K}.

In the case that ( C 2 K) [a − m, b) = 2 κ − 1 (C2^{K})^{[a-m,b)}=2^{\kappa}-1, we choose the maximal position c ∈ { 0, …, a − m − 1 } c\in\{0,\ldots,a-m-1\} such that δ c ​ ( C ​ 3 K) = 0 \delta_{c}(C3^{K})=0 (and δ c + 1 ​ ( C ​ 3 K) = 1 \delta_{c+1}(C3^{K})=1). As r r runs, the digits of r ​ k ​ B ​ 3 K rkB3^{K} in [a, b) [a,b) cycle through all possibilities *in the opposite direction*, and we obtain the conclusion in a completely analogous way. ∎

###### Proof of Proposition 1.1.

Assume that N ≥ 1 N\geq 1, and choose ν ≥ 0 \nu\geq 0 in such a way that

(4.4) |  | 2 ν ≤ N < 2 ν + 1. 2^{\nu}\leq N<2^{\nu+1}. |  |

In the digit elimation procedure below we will use a parameter

(4.5) |  | R = 2 m, where m = ⌊ ν / 10 ⌋. R=2^{m},\quad\mbox{where}\quad m=\lfloor\nu/10\rfloor. |  |

The parameter R R will be used in van der Corput’s inequality; its binary length is a fraction ∼ 1 / 10 \sim 1/10 of the binary length of N N.

Applying van der Corput’s inequality. Let us first introduce an additional factor detecting whether n n is even or odd. Using Iverson bracket notation for convenience, We have

 | S 𝟣 ( i) = 1 N ∑ 0 ≤ n < N e ( t 1 𝗌 2 ( n3 K) + t 2 𝗌 3 ( n)) [[n ≡ i mod 2]], S_{\mathsf{1}}^{(i)}=\frac{1}{N}\sum_{0\leq n<N}\e\Bigl(t_{1}\mathsf{s}_{2}\bigl(n3^{K}\bigr)+t_{2}\mathsf{s}_{3}(n)\Bigr)\bigl[\hskip-3.00003pt\bigl[n\equiv i\bmod 2\bigr]\hskip-3.00003pt\bigr], |  |

therefore an application of van der Corput’s inequality yields

(4.6) |  | | S 1 ( i) | 2 ≪ 1 R ∑ 1 ≤ r < R 2 | r M 𝟢 ( i) + E 𝟢, \bigl\lvert S_{1}^{(i)}\bigr\rvert^{2}\ll\frac{1}{R}\sum_{\begin{subarray}{c}1\leq r<R\\ 2\mid r\end{subarray}}M_{\mathsf{0}}^{(i)}+E_{\mathsf{0}}, |  |

where

(4.7) |  | M 𝟢 ( i) ≔ 1 N ∑ n < N e ( t 1 𝗌 2 ( n3 K) − t 1 𝗌 2 ( ( n + r) 3 K) + t 2 𝗌 3 ( n) − t 2 𝗌 3 ( n + r)) [[n ≡ i mod 2]] M_{\mathsf{0}}^{(i)}\coloneqq\frac{1}{N}\sum_{n<N}\e\Bigl(t_{1}\mathsf{s}_{2}\bigl(n3^{K}\bigr)-t_{1}\mathsf{s}_{2}\bigl((n+r)3^{K}\bigr)+t_{2}\mathsf{s}_{3}(n)-t_{2}\mathsf{s}_{3}(n+r)\Bigr)\bigl[\hskip-3.00003pt\bigl[n\equiv i\bmod 2\bigr]\hskip-3.00003pt\bigr] |  |

and

(4.8) |  | E 𝟢 ≔ 1 R + R N. E_{\mathsf{0}}\coloneqq\frac{1}{R}+\frac{R}{N}. |  |

We introduce a new parameter λ 3 \lambda_{3} to be chosen in a moment (see ( 4.13) below), and apply the “carry lemma” [12, 19, 20, 21, 24] in order to replace 𝗌 3 \mathsf{s}_{3} by a 3 λ 3 3^{\lambda_{3}} -periodic term. Setting

(4.9) |  | E 𝟣 ≔ R 3 λ 3, E_{\mathsf{1}}\coloneqq\frac{R}{3^{\lambda_{3}}}, |  |

we obtain

(4.10) |  | M 𝟢 ( i) = 1 N ​ ∑ 0 ≤ n < N n ≡ i mod 2 e ⁡ ( t 1 ​ 𝗌 2 ​ ( n3 K) − t 1 ​ 𝗌 2 ​ ( ( n + r) ​ 3 K) + t 2 ​ 𝗌 3 [0, λ 3) ​ ( n) − t 2 ​ 𝗌 3 [0, λ 3) ​ ( n + r)) + 𝒪 ⁡ ( E 𝟣). M_{\mathsf{0}}^{(i)}=\frac{1}{N}\sum_{\begin{subarray}{c}0\leq n<N\\ n\equiv i\bmod 2\end{subarray}}\e\Bigl(t_{1}\mathsf{s}_{2}\bigl(n3^{K}\bigr)-t_{1}\mathsf{s}_{2}\bigl((n+r)3^{K}\bigr)+t_{2}\mathsf{s}^{[0,\lambda_{3})}_{3}(n)-t_{2}\mathsf{s}^{[0,\lambda_{3})}_{3}(n+r)\Bigr)+\mathcal{O}(E_{\mathsf{1}}). |  |

Writing n = n 𝟣 ​ 3 λ 3 + n 𝟢 n=n_{\mathsf{1}}3^{\lambda_{3}}+n_{\mathsf{0}}, where 0 ≤ n 𝟢 < 3 λ 3 0\leq n_{\mathsf{0}}<3^{\lambda_{3}}, we obtain

(4.11) |  | M 𝟢 ≪ ∑ 0 ≤ n 0 < 3 λ 3 | M 𝟤 ( n 0) | + 𝒪 ( E 𝟣), M_{\mathsf{0}}\ll\sum_{0\leq n_{0}<3^{\lambda_{3}}}\bigl\lvert M_{\mathsf{2}}(n_{0})\bigr\rvert+\mathcal{O}(E_{\mathsf{1}}), |  |

where

(4.12) |  | M 𝟤 ​ ( n 0) \displaystyle M_{\mathsf{2}}(n_{0}) | ≔ 1 N ​ ∑ 0 ≤ n < N n ≡ i mod 2 n ≡ n 𝟢 mod 3 λ 3 e ⁡ ( t 1 ​ 𝗌 2 ​ ( n3 K) − t 1 ​ 𝗌 2 ​ ( n3 K + r3 K)). \displaystyle\coloneqq\frac{1}{N}\sum_{\begin{subarray}{c}0\leq n<N\\ n\equiv i\bmod 2\\ n\equiv n_{\mathsf{0}}\bmod 3^{\lambda_{3}}\end{subarray}}\e\Bigl(t_{1}\mathsf{s}_{2}\bigl(n3^{K}\bigr)-t_{1}\mathsf{s}_{2}\bigl(n3^{K}+r3^{K}\bigr)\Bigr). |  |

Note that the 3 λ 3 3^{\lambda_{3}} -periodic terms 𝗌 3 [0, λ 3) \mathsf{s}^{[0,\lambda_{3})}_{3} have vanished.

We distinguish between the cases “ K K small” and “ K K large”. For this, we choose parameters c 1, R, λ 3 c_{1},R,\lambda_{3} in such a way that

(4.13) |  | c 1 = min ⁡ { c 2, 1 10 ​ log ⁡ 2 log ⁡ 3 }, R ≍ N 1 / 10, 3 λ 3 ≍ N 1 / 5. c_{1}=\min\biggl\{c_{2},\frac{1}{10}\frac{\log 2}{\log 3}\biggr\},\quad R\asymp N^{1/10},\quad 3^{\lambda_{3}}\asymp N^{1/5}. |  |

We consider, respectively, the cases

 | { K < c 1 ​ log 2 ​ N, and c 1 ​ log 2 ​ N ≤ K < c 2 ​ log 2 ​ N. \begin{cases}K<c_{1}\log_{2}N,&\mbox{and}\\ c_{1}\log_{2}N\leq K<c_{2}\log_{2}N.\end{cases} |  |

Let us start with the easier case.

### 4.1. Small values of K K

Note that our choice of λ 3 \lambda_{3} implies that 3 K ≤ N 1 / 10 3^{K}\leq N^{1/10}. Choose

(4.14) |  | λ 2 = ⌊ 3 ​ ν / 10 ⌋, \lambda_{2}=\lfloor 3\nu/10\rfloor, |  |

such that

(4.15) |  | R ​ 3 K 2 λ 2 ≪ N 1 / 10. \frac{R3^{K}}{2^{\lambda_{2}}}\ll N^{1/10}. |  |

Similarly to ( 4.10), we have

 | M 𝟤 ​ ( n 0) = 1 2 λ 2 ​ 3 λ 3 ​ ∑ 0 ≤ n < 2 λ 2 e ⁡ ( t 1 ​ 𝗌 [0, λ 2) ​ ( n) − t 1 ​ 𝗌 2 [0, λ 2) ​ ( n + r3 K)) + E 𝟤, \displaystyle M_{\mathsf{2}}(n_{0})=\frac{1}{2^{\lambda_{2}}3^{\lambda_{3}}}\sum_{0\leq n<2^{\lambda_{2}}}\e\Bigl(t_{1}\mathsf{s}^{[0,\lambda_{2})}(n)-t_{1}\mathsf{s}^{[0,\lambda_{2})}_{2}\bigl(n+r3^{K}\bigr)\Bigr)+E_{\mathsf{2}}, |  |

where

(4.16) |  | E 𝟤 ≔ R ​ 3 K ​ ( 1 2 λ 2 ​ 1 3 λ 3 + 1 N). E_{\mathsf{2}}\coloneqq{R3^{K}}\biggl(\frac{1}{2^{\lambda_{2}}}\frac{1}{3^{\lambda_{3}}}+\frac{1}{N}\biggr). |  |

For this, we just note that the lowest λ 2 \lambda_{2} binary digits of n ​ 3 K n3^{K} attain each value in a periodic fashion, as n n runs through i ​ 3 λ 3 + 2 ⋅ 3 λ 3 ​ ℤ i3^{\lambda_{3}}+2\cdot 3^{\lambda_{3}}\mathbb{Z}. Excluding R ​ 3 K R3^{K} digit combinations, the estimate follows. Next, we replace 𝗌 [0, λ 2) \mathsf{s}^{[0,\lambda_{2})} by 𝗌 \mathsf{s} again, reusing the fact that only a proportion ≪ R ​ 3 K / 2 λ 2 \ll R3^{K}/2^{\lambda_{2}} of integers n n satisfy

 | 𝗌 ⁡ ( n) − 𝗌 ⁡ ( n + r ​ 3 K) ≠ 𝗌 [0, λ 2) ​ ( n) − 𝗌 [0, λ 2) ​ ( n + r ​ 3 K). \mathsf{s}(n)-\mathsf{s}\bigl(n+r3^{K}\bigr)\neq\mathsf{s}^{[0,\lambda_{2})}(n)-\mathsf{s}^{[0,\lambda_{2})}\bigl(n+r3^{K}\bigr). |  |

As this error is swallowed by E 𝟤 E_{\mathsf{2}}, we obtain

(4.17) |  | | S 𝟣 ( i) | 2 ≪ 1 R ∑ 1 ≤ r ≤ R | γ r ​ 3 K ( t 1) | + E 𝟢 + E 𝟣 + E 𝟤, \bigl\lvert S_{\mathsf{1}}^{(i)}\bigr\rvert^{2}\ll\frac{1}{R}\sum_{1\leq r\leq R}\bigl\lvert\gamma_{r3^{K}}(t_{1})\bigr\rvert+E_{\mathsf{0}}+E_{\mathsf{1}}+E_{\mathsf{2}}, |  |

where

(4.18) |  | γ t ​ ( ϑ) ≔ lim M → ∞ 1 M ​ ∑ 0 ≤ n < M e ⁡ ( t 1 ​ 𝗌 ​ ( n) − t 1 ​ 𝗌 ​ ( n + t)). \gamma_{t}(\vartheta)\coloneqq\lim_{M\rightarrow\infty}\frac{1}{M}\sum_{0\leq n<M}\e\Bigl(t_{1}\mathsf{s}(n)-t_{1}\mathsf{s}\bigl(n+t\bigr)\Bigr). |  |

We recall a result from the paper [26] by the second author, which was also used in [29].

###### Lemma 4.2 ( [26, Lemma 2.7]).

Assume that t ≥ 1 t\geq 1 has at least M ′ = 2 ​ M + 1 M^{\prime}=2M+1 blocks of 𝟷 \mathtt{1} s. Then

 | | γ t ​ ( ϑ) | ≤ ( 1 − ∥ ϑ ∥ 2 2) M ≤ exp ⁡ ( − M ​ ∥ ϑ ∥ 2 2). \left\lvert\gamma_{t}(\vartheta)\right\rvert\leq\biggl(1-\frac{\lVert\vartheta\rVert^{2}}{2}\biggr)^{M}\leq\exp\biggl(-\frac{M\lVert\vartheta\rVert^{2}}{2}\biggr). |  |

In order to guarantee that r ​ 3 K r3^{K} has sufficiently many blocks of 𝟷 \mathtt{1} s, we apply Lemma 4.1. We assume that

(4.19) |  | R < 2 η ​ K. R<2^{\eta K}. |  |

For each ε > 0 \varepsilon>0, and K ≥ K 0 ​ ( η, ε) K\geq K_{0}(\eta,\varepsilon), the lemma implies

 | L ⁡ ( r ​ 3 K) ≤ ( 1 + ε) ​ η ​ K. L\bigl(r3^{K}\bigr)\leq(1+\varepsilon)\eta K. |  |

In particular, as K → ∞ K\rightarrow\infty, and ( 4.19) is satisfied, the number of maximal blocks of 𝟷 \mathtt{1} s in r ​ 3 K r3^{K} is ≫ K ​ η \gg K\eta.

By Lemma 4.2 it follows that there exists a constant c c (depending on η \eta) such that

 | | S 𝟣 ( i) | 2 ≪ exp ( − c K ∥ t 1 ∥ 2) + E 𝟢 + E 𝟣 + E 𝟤. \bigl\lvert S_{\mathsf{1}}^{(i)}\bigr\rvert^{2}\ll\exp\biggl(-cK\lVert t_{1}\rVert^{2}\biggr)+E_{\mathsf{0}}+E_{\mathsf{1}}+E_{\mathsf{2}}. |  |

Collecting the error terms, we see tht the proposition is proved for the case of “small K K ”.

### 4.2. Large values of K K

In order to handle the second case, we will use the odd elimination lemma (Corollary 4.1), based on Schlickewei’s p p -adic subspace theorem in an essential way.

Iterating van der Corput. Applying Cauchy-Schwarz and van der Corput alternatingly, we arrive at the following statement [28].

###### Lemma 4.3.

Let Q ≥ 1 Q\geq 1 be an integer. Assume that J J is a finite nonempty interval in ℤ \mathbb{Z}, and g: J → { z ∈ ℂ: | z | = 1 } g:J\rightarrow\{z\in\mathbb{C}:\lvert z\rvert=1\}. For all integers 𝔪 0, …, 𝔪 Q − 1 ≥ 1 \mathfrak{m}_{0},\ldots,\mathfrak{m}_{Q-1}\geq 1 and R ≥ 1 R\geq 1, we have

(4.20) |  | | 1 | J | ∑ n ∈ J g ( n) | 2 Q \displaystyle\Biggl\lvert\frac{1}{\lvert J\rvert}\sum_{n\in J}g(n)\Biggr\rvert^{2^{Q}} | ≪ 1 R Q ∑ r ∈ { 1, …, R − 1 } Q | K ( r 0 𝔪 0, …, r Q − 1 𝔪 Q − 1) | \displaystyle\ll\frac{1}{R^{Q}}\sum_{r\in\{1,\ldots,R-1\}^{Q}}\bigl\lvert K\bigl(r_{0}\mathfrak{m}_{0},\ldots,r_{Q-1}\mathfrak{m}_{Q-1}\bigr)\bigr\rvert |  |

 |  | + ( 𝔪 0 + ⋯ + 𝔪 Q − 1) ​ R | J | + 1 R, \displaystyle+\frac{\bigl(\mathfrak{m}_{0}+\cdots+\mathfrak{m}_{Q-1}\bigr)R}{\lvert J\rvert}+\frac{1}{R}, |  |

where

 | K ⁡ ( t 0, …, t Q − 1) ≔ 1 | J | ​ ∑ n ∈ J ∏ ε ∈ { 0, 1 } Q 𝒞 | ε | ​ g ​ ( n + ∑ 0 ≤ ℓ < Q ε ℓ ​ t ℓ), K\bigl(t_{0},\ldots,t_{Q-1}\bigr)\coloneqq\frac{1}{\lvert J\rvert}\sum_{n\in J}\prod_{\varepsilon\in\{0,1\}^{Q}}\mathcal{C}^{\lvert\varepsilon\rvert}g\Biggl(n+\sum_{0\leq\ell<Q}\varepsilon_{\ell}t_{\ell}\Biggr), |  |

and 𝒞 \mathcal{C} is pointwise complex conjugation. The implied constant depends only on Q Q.

Each factor 𝔪 ℓ \mathfrak{m}_{\ell} is responsible for the “elimination of digits” in a short interval, and also in a small margin just below the interval. Recall that m m is the binary length of R R 4.5. We double this value in order to obtain a useful *double margin*, and we define

(4.21) |  | a ℓ = λ 2 − ℓ ​ κ b ℓ = a ℓ − m c ℓ = a ℓ − 2 ​ m, I ℓ = [a ℓ, a ℓ − 1), I ℓ ′ = [b ℓ, a ℓ − 1), I ℓ ′′ = [c ℓ, a ℓ − 1). \begin{array}[]{rlrlrl}a_{\ell}&=\lambda_{2}-\ell\kappa&b_{\ell}&=a_{\ell}-m&c_{\ell}&=a_{\ell}-2m,\\ I_{\ell}&=[a_{\ell},a_{\ell-1}),&I^{\prime}_{\ell}&=[b_{\ell},a_{\ell-1}),&I^{\prime\prime}_{\ell}&=[c_{\ell},a_{\ell-1}).\end{array} |  |

The interval of digits we want to remove in step ℓ \ell (where 1 ≤ ℓ ≤ Q 1\leq\ell\leq Q, and Q Q is yet to be defined) is I ℓ I_{\ell}. In order to achieve this, we *clear*the binary digits of 3 K 𝟣 3^{K_{\mathsf{1}}} in the larger interval I ℓ ′′ I^{\prime\prime}_{\ell} of length κ + 2 ​ m \kappa+2m, multiplying this value by some odd integer produced by Corollary 4.1. Multiplying this new value by any number in r ℓ ∈ { 0, …, R − 1 } r_{\ell}\in\{0,\ldots,R-1\}, we still have only 𝟶 \mathtt{0} s in the slightly smaller interval I ℓ ′ I^{\prime}_{\ell} of length κ + m \kappa+m. Consequently, *in most cases*, the quantity r ℓ ​ 𝔪 ℓ ​ 3 K 𝟣 r_{\ell}\mathfrak{m}_{\ell}3^{K_{\mathsf{1}}} can be added to an integer n n without changing the digits in I ℓ I_{\ell}. Namely, this happens precisely when not all of the digits of n n on the upper part [b ℓ, a ℓ) [b_{\ell},a_{\ell}) of the margin are equal to 𝟷 \mathtt{1}, and thus carry propagation is interrupted. Set

 | g ⁡ ( n) = e ⁡ ( t 1 ​ 𝗌 2 [0, λ 2) ​ ( n3 K 𝟣 + n 𝟢 ​ 3 K)). g(n)=\e\bigl(t_{1}\mathsf{s}_{2}^{[0,\lambda_{2})}\bigl(n3^{K_{\mathsf{1}}}+n_{\mathsf{0}}3^{K}\bigr)\bigr). |  |

Lemma 4.3 implies

(4.22) |  | 1 | J ⁡ ( n 0) | | M 𝟤 ( n 0) | 2 Q \displaystyle\frac{1}{\lvert J(n_{0})\rvert}\bigl\lvert M_{\mathsf{2}}(n_{0})\bigr\rvert^{2^{Q}} | ≤ 1 R Q − 1 ∑ r 1, …, r Q ∈ { 1, …, R − 1 } | M 𝟥 ( r 0 3 K, r 1 𝔪 1 3 K 𝟣, …, r Q 𝔪 Q 3 K 𝟣; n 𝟢 3 K) | \displaystyle\leq\frac{1}{R^{Q-1}}\sum_{r_{1},\ldots,r_{Q}\in\{1,\ldots,R-1\}}\bigl\lvert M_{\mathsf{3}}\bigl(r_{0}3^{K},r_{1}\mathfrak{m}_{1}3^{K_{\mathsf{1}}},\ldots,r_{Q}\mathfrak{m}_{Q}3^{K_{\mathsf{1}}};n_{\mathsf{0}}3^{K}\bigr)\bigr\rvert |  |

 |  | + ( 𝔪 1 + ⋯ + 𝔪 Q) ​ R | J | + 1 R, \displaystyle+\frac{\bigl(\mathfrak{m}_{1}+\cdots+\mathfrak{m}_{Q}\bigr)R}{\lvert J\rvert}+\frac{1}{R}, |  |

where M 𝟥 M_{\mathsf{3}} is the iterated correlation

(4.23) |  | M 𝟥 ​ ( t 0, …, t Q, a) ≔ 1 | J ⁡ ( n 𝟢) | ​ ∑ n 𝟣 ∈ J ⁡ ( n 𝟢) ∏ ε ∈ { 0, 1 } Q + 1 e ⁡ ( ( − 1) | ε | ​ t 1 ​ s 2 [0, λ 2) ​ ( n 𝟣 ​ 3 K 𝟣 + ∑ 0 ≤ ℓ ≤ Q ε ℓ ​ t ℓ + a)). \displaystyle M_{\mathsf{3}}(t_{0},\ldots,t_{Q};a)\coloneqq\frac{1}{\lvert J(n_{\mathsf{0}})\rvert}\sum_{n_{\mathsf{1}}\in J(n_{\mathsf{0}})}\prod_{\varepsilon\in\{0,1\}^{Q+1}}\e\Biggl((-1)^{\lvert\varepsilon\rvert}t_{1}s_{2}^{[0,\lambda_{2})}\biggl(n_{\mathsf{1}}3^{K_{\mathsf{1}}}+\sum_{0\leq\ell\leq Q}\varepsilon_{\ell}t_{\ell}+a\Biggr)\Biggr). |  |

In the next few paragraphs, we will choose the parameters 𝔪 ℓ \mathfrak{m}_{\ell} suitably in order to discard intervals of digits, one interval for each ℓ ∈ { 1, …, Q } \ell\in\{1,\ldots,Q\}.

Preparing digit elimination. We begin with the observation that the binary digits of n 𝟣 ↦ n 𝟣 ​ 3 K 𝟣 n_{\mathsf{1}}\mapsto n_{\mathsf{1}}3^{K_{\mathsf{1}}} with indices in [b ℓ, a ℓ) [b_{\ell},a_{\ell}) attain all combinations in a uniform manner. This will be needed in order to bound the number of cases where for some ℓ \ell, carry propagation from the upper half [b ℓ, a ℓ) [b_{\ell},a_{\ell}) of the margin into the interval I ℓ I_{\ell} happens. This is our first use of Corollary 4.1. Assume that ε, η > 0 \varepsilon,\eta>0. We suppose in the following that x, y, K 𝟣 x,y,K_{\mathsf{1}} are integers satisfying

(4.24) |  | K 𝟣 \displaystyle K_{\mathsf{1}} | ≥ K 𝟢 ​ ( η, ε, 1), \displaystyle\geq K_{\mathsf{0}}(\eta,\varepsilon,1), |  |

 | ε ​ K 𝟣 \displaystyle\varepsilon K_{\mathsf{1}} | ≤ x ≤ y ≤ x + η ​ K 𝟣. \displaystyle\leq x\leq y\leq x+\eta K_{\mathsf{1}}. |  |

By the corollary,

(4.25) |  | ( A ​ 3 K 𝟣) [x, y) = 1 for some A ≪ 2 ( 2 ​ η + ε) ​ K 𝟣. \bigl(A3^{K_{\mathsf{1}}}\bigr)^{[x,y)}=1\quad\mbox{for some}\quad A\ll 2^{(2\eta+\varepsilon)K_{\mathsf{1}}}. |  |

That is, the digits of A ​ 3 K 𝟣 A3^{K_{\mathsf{1}}} are zero on ( x, y) (x,y), and the digit at index x x equals 𝟷 \mathtt{1}. It follows that for each b b,

 | n 𝟣𝟣 ↦ ( ( n 𝟣𝟣 ​ A + n 𝟣𝟢) ​ 3 K 𝟣 + b) ( x, y) n_{\mathsf{11}}\mapsto\bigl((n_{\mathsf{11}}A+n_{\mathsf{10}})3^{K_{\mathsf{1}}}+b\bigr)^{(x,y)} |  |

attains each value once or twice in a row, running through all possibilities. Using the decomposition n 𝟣 = n 𝟣𝟣 ​ A + n 𝟣𝟢 n_{\mathsf{1}}=n_{\mathsf{11}}A+n_{\mathsf{10}}, we obtain, for any ω ∈ { 0, …, 2 y − x − 1 } \omega\in\{0,\ldots,2^{y-x}-1\},

 | | { n 𝟣 ∈ J ( n 𝟢): ( n 𝟣 3 K 𝟣 + b) [x, y) = ω } | ≪ E 𝟥 \bigl\lvert\bigl\{n_{\mathsf{1}}\in J(n_{\mathsf{0}}):\bigl(n_{\mathsf{1}}3^{K_{\mathsf{1}}}+b\bigr)^{[x,y)}=\omega\bigr\}\bigr\rvert\ll E_{\mathsf{3}} |  |

with some absolute implicit constant, where

(4.26) |  | E 𝟥 ≔ | J ⁡ ( n 𝟢) | 2 y − x + A. E_{\mathsf{3}}\coloneqq\frac{\lvert J(n_{\mathsf{0}})\rvert}{2^{y-x}}+A. |  |

Recall that in our application, the role of interval [x, y) [x,y) will be played by the upper part [b ℓ, a ℓ) [b_{\ell},a_{\ell}) of the margin. *For all*( ε 0, …, ε Q) ∈ { 0, 1 } Q + 1 (\varepsilon_{0},\ldots,\varepsilon_{Q})\in\{0,1\}^{Q+1}, the digits of

(4.27) |  | ℒ ⁡ ( ε 0, …, ε Q) ≔ n 𝟣 ​ 3 K 𝟣 + ε 0 ​ r 𝟢 + ∑ 1 ≤ ℓ ≤ Q ε ℓ ​ r ℓ ​ 𝔪 ℓ ​ 3 K 𝟣 + n 𝟢 ​ 3 K \mathcal{L}(\varepsilon_{0},\ldots,\varepsilon_{Q})\coloneqq n_{\mathsf{1}}3^{K_{\mathsf{1}}}+\varepsilon_{0}r_{\mathsf{0}}+\sum_{1\leq\ell\leq Q}\varepsilon_{\ell}r_{\ell}\mathfrak{m}_{\ell}3^{K_{\mathsf{1}}}+n_{\mathsf{0}}3^{K} |  |

with indices in [b ℓ, a ℓ) [b_{\ell},a_{\ell}) should not be identical to 𝟷 \mathtt{1}. That is, ω = 2 y − x − 1 \omega=2^{y-x}-1 has to be excluded. The error term E 𝟥 E_{\mathsf{3}} has to be multiplied by a factor Q ​ 2 Q + 1 Q2^{Q+1}, since we want to avoid carry overflow *simultaneously*for all 1 ≤ ℓ ≤ Q 1\leq\ell\leq Q and ε ∈ { 0, 1 } Q + 1 \varepsilon\in\{0,1\}^{Q+1}.

Consequently, for all ℓ ∈ { 1, …, Q } \ell\in\{1,\ldots,Q\} and all choices ε k ∈ { 0, 1 } \varepsilon_{k}\in\{0,1\} for k ∈ { 0, …, Q } ∖ { ℓ } k\in\{0,\ldots,Q\}\setminus\{\ell\}, the integers

(4.28) |  | ℒ ⁡ ( ε 0, …, ε ℓ − 1, 0, ε ℓ + 1, …, ε Q) and ℒ ⁡ ( ε 0, …, ε ℓ − 1, 1, ε ℓ + 1, …, ε Q) \mathcal{L}\bigl(\varepsilon_{0},\ldots,\varepsilon_{\ell-1},0,\varepsilon_{\ell+1},\ldots,\varepsilon_{Q}\bigr)\quad\mbox{and}\quad\mathcal{L}\bigl(\varepsilon_{0},\ldots,\varepsilon_{\ell-1},1,\varepsilon_{\ell+1},\ldots,\varepsilon_{Q}\bigr) |  |

have the same digits in [a ℓ, a ℓ − 1) [a_{\ell},a_{\ell-1}) for all but 𝒪 ⁡ ( E 𝟦) \mathcal{O}(E_{\mathsf{4}}) integers n 𝟣 ∈ J ⁡ ( n 𝟢) n_{\mathsf{1}}\in J(n_{\mathsf{0}}), where

(4.29) |  | E 𝟦 ≔ N 3 λ 3 ​ 2 y − x + A. E_{\mathsf{4}}\coloneqq\frac{N}{3^{\lambda_{3}}2^{y-x}}+A. |  |

The implied constant may depend on Q Q.

Discarding digits block by block. Assume that c 2 > 0 c_{2}>0, and consider the requirement c 1 ​ log 2 ​ N ≤ K ≤ c 2 ​ log 2 ​ N c_{1}\log_{2}N\leq K\leq c_{2}\log_{2}N. In step ℓ \ell, where 1 ≤ ℓ ≤ Q 1\leq\ell\leq Q, we want to remove the interval [a ℓ, a ℓ − 1) [a_{\ell},a_{\ell-1}) (see ( 4.21)). For simplicity, we assume that its length κ \kappa is a fixed fraction of the binary length ν \nu of N N:

(4.30) |  | κ ∼ ν / 10. \kappa\sim\nu/10. |  |

After the removal of I 1, …, I Q I_{1},\ldots,I_{Q}, only the interval [0, μ) [0,\mu) of digits will be left, where

(4.31) |  | μ = λ 2 − Q ​ κ \mu=\lambda_{2}-Q\kappa |  |

should satisfy

 | 2 ​ κ ≤ μ < 3 ​ κ. 2\kappa\leq\mu<3\kappa. |  |

Clearly, this implies

(4.32) |  | Q ≍ ( 1 + c 2) − 1. Q\asymp(1+c_{2})^{-1}. |  |

As for the size of the margins, we note that m = κ = log 2 ⁡ R m=\kappa=\log_{2}R. By ( 4.31), the intervals

 | I ℓ ′′ = [a ℓ − 2 m, a ℓ − 1), I^{\prime\prime}_{\ell}=\bigl[a_{\ell}-2m,a_{\ell-1}\bigr), |  |

where a ℓ = λ 2 − ℓ ​ κ a_{\ell}=\lambda_{2}-\ell\kappa as in ( 4.21), are well separated from 0 0. In particular, there are enough digits below our intervals to be eliminated in order to apply Corollary 4.1. Suppose that K 𝟣 ≥ K 𝟢 ​ ( η, ε, 2) K_{\mathsf{1}}\geq K_{\mathsf{0}}(\eta,\varepsilon,2) as stated in the corollary. (The parameter 2 2 handles the even/odd restriction on n n.) We obtain *odd factors*𝔪 1, …, 𝔪 Q \mathfrak{m}_{1},\ldots,\mathfrak{m}_{Q},

 | 𝔪 ℓ ≪ 2 ( 2 ​ η + ε) ​ K 𝟣, \mathfrak{m}_{\ell}\ll 2^{(2\eta+\varepsilon)K_{\mathsf{1}}}, |  |

such that ( 𝔪 ℓ ​ 3 K 𝟣) [x, y) = 0 \bigl(\mathfrak{m}_{\ell}3^{K_{\mathsf{1}}}\bigr)^{[x,y)}=0, where [x, y) = I ℓ ′′ [x,y)=I^{\prime\prime}_{\ell}.

Introducing the error E 𝟦 E_{\mathsf{4}} defined in ( 4.29) takes care of the integers n 𝟣 ∈ J ⁡ ( n 𝟢) n_{\mathsf{1}}\in J(n_{\mathsf{0}}) that are exceptional for *some*index 1 ≤ ℓ ≤ Q 1\leq\ell\leq Q and *some*choice ( ε 0, …, ε Q) ∈ { 0, 1 } Q + 1 (\varepsilon_{0},\ldots,\varepsilon_{Q})\in\{0,1\}^{Q+1}. For the remaining n 𝟣 n_{\mathsf{1}}, we consider the product on the right hand side of ( 4.23). In a way analogous to [14, 25] we may discard the digits with indices outside [0, μ) [0,\mu). That is, we (1) exclude the critical indices n 𝟣 n_{\mathsf{1}}, (2) apply the digit-cancelling argument implemented in the cited papers, and (3) reinsert the missing indices again. Up to an error term E 𝟦 E_{\mathsf{4}}, this leads to an expression

(4.33) |  |  | M 𝟦 ​ ( t 0, …, t Q, a) ≔ 1 | J ⁡ ( n 𝟢) | ​ ∑ n 𝟣 ∈ J ⁡ ( n 𝟢) ∏ ε ∈ { 0, 1 } Q + 1 e ⁡ ( ( − 1) | ε | ​ t 1 ​ s 2 [0, μ) ​ ( n 𝟣 ​ 3 K 𝟣 + ∑ 0 ≤ ℓ ≤ Q ε ℓ ​ t ℓ + a)), \displaystyle M_{\mathsf{4}}(t_{0},\ldots,t_{Q};a)\coloneqq\frac{1}{\lvert J(n_{\mathsf{0}})\rvert}\sum_{n_{\mathsf{1}}\in J(n_{\mathsf{0}})}\prod_{\varepsilon\in\{0,1\}^{Q+1}}\e\Biggl((-1)^{\lvert\varepsilon\rvert}t_{1}s_{2}^{[0,\mu)}\biggl(n_{\mathsf{1}}3^{K_{\mathsf{1}}}+\sum_{0\leq\ell\leq Q}\varepsilon_{\ell}t_{\ell}+a\Biggr)\Biggr), |  |

 |  | where t 0 = r 𝟢 ​ 3 K, t ℓ = r ℓ ​ 𝔪 ℓ ​ 3 K 𝟣 for 1 ≤ ℓ ≤ Q, and a = n 𝟢 ​ 3 K. \displaystyle\mbox{where\quad$t_{0}=r_{\mathsf{0}}3^{K}$, \quad$t_{\ell}=r_{\ell}\mathfrak{m}_{\ell}3^{K_{\mathsf{1}}}$ for $1\leq\ell\leq Q$,\quad and \quad$a=n_{\mathsf{0}}3^{K}$.} |  |

At this point, the main work has already been done. The remaining sum over n 𝟣 n_{\mathsf{1}} is long enough to traverse all digit combinations on [0, μ) [0,\mu) in a uniform manner, but by construction, the sums over r ℓ r_{\ell} are too short. In order to transform the higher order correlations into a Gowers norm, we shorten our interval of digits once more. This leaves only [0, ρ) [0,\rho), where ρ = ν / 6 \rho=\nu/6 (recall that μ ≥ 2 ​ κ = ν / 5 \mu\geq 2\kappa=\nu/5).

Removing the last interval of digits. Let the odd positive integer 𝔪 Q + 1 < 2 μ \mathfrak{m}_{Q+1}<2^{\mu} be chosen in such a way that

(4.34) |  | 𝔪 Q + 1 ​ 3 K 𝟣 ≡ 1 mod 2 μ. \mathfrak{m}_{Q+1}3^{K_{\mathsf{1}}}\equiv 1\bmod 2^{\mu}. |  |

Let ρ ′ \rho^{\prime} be an integers such that 0 ≤ ρ ′ ≤ ρ 0\leq\rho^{\prime}\leq\rho. We apply van der Corput’s inequality one last time in order to eliminate the digits in [ρ, μ) [\rho,\mu). This yields

(4.35) |  |  | | M 𝟦 ( t 0, …, t Q; a) | 2 ≤ | J ⁡ ( n 𝟢) | + 2 μ + ρ ′ | J ⁡ ( n 𝟢) | ​ 2 ρ ′ ∑ 0 ≤ | r Q + 1 | < 2 ρ ′ ( 1 − | r Q + 1 | 2 ρ ′) \displaystyle\bigl\lvert M_{\mathsf{4}}(t_{0},\ldots,t_{Q};a)\bigr\rvert^{2}\leq\frac{\lvert J(n_{\mathsf{0}})\rvert+2^{\mu+\rho^{\prime}}}{\lvert J(n_{\mathsf{0}})\rvert 2^{\rho^{\prime}}}\sum_{0\leq\lvert r_{Q+1}\rvert<2^{\rho^{\prime}}}\biggl(1-\frac{\lvert r_{Q+1}\rvert}{2^{\rho^{\prime}}}\biggr) |  |

 |  | × ∑ n 𝟣, n 𝟣 + r Q + 1 ​ 𝔪 Q + 1 ∈ J ⁡ ( n 𝟢) M 𝟧 ​ ( t 0, …, t Q + 1, σ, 3 K 𝟣, a), \displaystyle\times\sum_{n_{\mathsf{1}},n_{\mathsf{1}}+r_{Q+1}\mathfrak{m}_{Q+1}\in J(n_{\mathsf{0}})}M_{\mathsf{5}}(t_{0},\ldots,t_{Q+1};\sigma,3^{K_{\mathsf{1}}},a), |  |

where

(4.36) |  |  | M 𝟧 ​ ( t 0, …, t Q + 1, σ, x, a) ≔ 1 | J ⁡ ( n 𝟢) | ​ ∑ n 𝟣 ∈ J ⁡ ( n 𝟢) ∏ ε ∈ { 0, 1 } Q + 2 e ⁡ ( ( − 1) | ε | ​ t 1 ​ s 2 [0, σ) ​ ( n 𝟣 ​ x + ∑ 0 ≤ ℓ ≤ Q + 1 ε ℓ ​ t ℓ + a)), \displaystyle M_{\mathsf{5}}(t_{0},\ldots,t_{Q+1};\sigma,x,a)\coloneqq\frac{1}{\lvert J(n_{\mathsf{0}})\rvert}\sum_{n_{\mathsf{1}}\in J(n_{\mathsf{0}})}\prod_{\varepsilon\in\{0,1\}^{Q+2}}\e\Biggl((-1)^{\lvert\varepsilon\rvert}{t_{1}}s_{2}^{[0,\sigma)}\biggl(n_{\mathsf{1}}x+\sum_{0\leq\ell\leq Q+1}\varepsilon_{\ell}t_{\ell}+a\Biggr)\Biggr), |  |

 |  | and σ = μ, x = 3 K 𝟣, t 0 = r 𝟢 ​ 3 K, t ℓ = r ℓ ​ 𝔪 ℓ ​ 3 K 𝟣 for 1 ≤ ℓ ≤ Q + 1, and a = n 𝟢 ​ 3 K. \displaystyle\mbox{and\quad$\sigma=\mu$,\quad$x=3^{K_{\mathsf{1}}}$, \quad$t_{0}=r_{\mathsf{0}}3^{K}$, \quad$t_{\ell}=r_{\ell}\mathfrak{m}_{\ell}3^{K_{\mathsf{1}}}$ for $1\leq\ell\leq Q+1$, and \quad$a=n_{\mathsf{0}}3^{K}$.} |  |

Note that ( 4.34) implies

 | ( r Q + 1 ​ 𝔪 Q + 1 ​ 3 K 𝟣) [ρ ′, μ) = 0. \bigl(r_{Q+1}\mathfrak{m}_{Q+1}3^{K_{\mathsf{1}}}\bigr)^{[\rho^{\prime},\mu)}=0. |  |

Consequently, for any shift s s and any interval I I of length 2 ρ 2^{\rho}, there are at most 2 ρ ′ 2^{\rho^{\prime}} integers n 𝟣 ∈ I n_{\mathsf{1}}\in I such that

 | ( n 𝟣 ​ 3 K 𝟣 + s) [ρ, μ) ≠ ( ( n 𝟣 + r Q + 1 ​ 𝔪 Q + 1) ​ 3 K 𝟣 + s) [ρ, μ) \bigl(n_{\mathsf{1}}3^{K_{\mathsf{1}}}+s\bigr)^{[\rho,\mu)}\neq\bigl((n_{\mathsf{1}}+r_{Q+1}\mathfrak{m}_{Q+1})3^{K_{\mathsf{1}}}+s\bigr)^{[\rho,\mu)} |  |

(the critical values being those where all digits of n 𝟣 ​ 3 K 𝟣 + s n_{\mathsf{1}}3^{K_{\mathsf{1}}}+s in [ρ ′, ρ) [\rho^{\prime},\rho) are equal to 𝟷 \mathtt{1}). Therefore, excluding 𝒪 ⁡ ( E 𝟦 ′) \mathcal{O}(E_{\mathsf{4}}^{\prime}) integers n 𝟣 ∈ J ⁡ ( n 𝟢) n_{\mathsf{1}}\in J(n_{\mathsf{0}}), where

 | E 𝟦 ′ = 2 ρ ′ ​ ⌈ | J ⁡ ( n 𝟢) | 2 ρ ⌉ ≤ 2 ρ ′ − ρ ​ | J ⁡ ( n 𝟢) | + 2 ρ ′, E_{\mathsf{4}}^{\prime}=2^{\rho^{\prime}}\biggl\lceil\frac{\lvert J(n_{\mathsf{0}})\rvert}{2^{\rho}}\biggr\rceil\leq 2^{\rho^{\prime}-\rho}\lvert J(n_{\mathsf{0}})\rvert+2^{\rho^{\prime}}, |  |

we may replace [0, μ) [0,\mu) by [0, ρ) [0,\rho) in the definition of M 𝟧 M_{\mathsf{5}}. Note once again that the implied constant may depend on Q Q.

The next step consists in replacing the sum over multiples of 3 K 𝟣 3^{K_{\mathsf{1}}} by a full sum, exploiting the fact that the sum over n 𝟣 n_{\mathsf{1}} is long enough, and 3 K 𝟣 3^{K_{\mathsf{1}}} is odd. Also, we may remove the factors t ℓ t_{\ell}, for 0 ≤ ℓ ≤ Q 0\leq\ell\leq Q, using R = 2 m | 2 ρ R=2^{m}\mid 2^{\rho}. Introducing a negligible error term coming from the decomposition of J ⁡ ( n 𝟢) J(n_{\mathsf{0}}) into intervals of length 2 ρ 2^{\rho} (the last interval might contribute an error), we arrive at the expression

(4.37) |  |  | M 𝟨 ( t 0, …, t Q; a) ≔ 1 2 ρ ′ ∑ r Q + 1 < 2 ρ ′ 1 2 ( Q + 1) ​ ρ ∑ r 0, …, r Q + 1 < 2 ρ | M 𝟧 ( t 0, …, t Q, t Q + 1; ρ, 1, 0) |, \displaystyle M_{\mathsf{6}}(t_{0},\ldots,t_{Q};a)\coloneqq\frac{1}{2^{\rho^{\prime}}}\sum_{r_{Q+1}<2^{\rho^{\prime}}}\frac{1}{2^{(Q+1)\rho}}\sum_{r_{0},\ldots,r_{Q+1}<2^{\rho}}\Biggl\lvert M_{\mathsf{5}}(t_{0},\ldots,t_{Q},t_{Q+1};\rho,1,0)\Biggr\rvert, |  |

 |  | where t 0 = ⋯ = t Q = 1, t Q + 1 = 𝔪 Q + 1 ​ 3 K 𝟣. \displaystyle\mbox{where\quad$t_{0}=\cdots=t_{Q}=1$, \quad$t_{Q+1}=\mathfrak{m}_{Q+1}3^{K_{\mathsf{1}}}$.} |  |

We have almost arrived at a Gowers norm. In order to handle the summation over r Q + 1 r_{Q+1}, which is shorter than 2 ρ 2^{\rho} by construction, we use a standard trick reminiscent of the “ 17 17 camels puzzle” [30]. We extend the sum to { 0, …, 2 ρ − 1 } \{0,\ldots,2^{\rho}-1\} (thus inserting terms representing the 18 18 th camel), noting that each summand is nonnegative. Applying the the Cauchy–Schwarz inequality, we insert another variable r Q + 2 r_{Q+2} ranging over { 0, …, 2 ρ − 1 } \{0,\ldots,2^{\rho}-1\}, and discard the absolute value again (this is also applied in our papers [25, 14]). The expression M 𝟨 M_{\mathsf{6}} is replaced by a Gowers- ( Q + 3) (Q+3) -norm on ℤ / 2 ρ ​ ℤ \mathbb{Z}/2^{\rho}\mathbb{Z}, where an additional factor ( 2 ρ − ρ ′) 2 \bigl(2^{\rho-\rho^{\prime}}\bigr)^{2} arising from our extension of a summation range is present. Having arrived at a full Gowers norm, we can use available techniques in order to arrive at a nontrivial estimate. More precisely, extending the method devised in [14, Chapter 5.2] for the *Zeckendorf sum-of-digits function*, we arrive at the following statement.

###### Proposition 4.1.

Let q ≥ 2 q\geq 2 and Q ≥ 1 Q\geq 1 be integers, and ϑ ∈ ℤ \vartheta\in\mathbb{Z}. There exists a constant c > 0 c>0 such that

(4.38) |  | 1 q ( Q + 1) ​ μ ​ ∑ 0 ≤ n < q μ ∑ r ∈ { 0, …, q μ − 1 } Q ∏ ε ∈ { 0, 1 } Q e ⁡ ( ( − 1) | ε | ​ ϑ ​ s q ​ ( n + ε ⋅ r)) ≪ q − c ​ μ ​ ∥ ( q − 1) ​ ϑ ∥ 2 \frac{1}{q^{(Q+1)\mu}}\sum_{0\leq n<q^{\mu}}\sum_{r\in\{0,\ldots,q^{\mu}-1\}^{Q}}\prod_{\varepsilon\in\{0,1\}^{Q}}\e\biggl((-1)^{\lvert\varepsilon\rvert}\vartheta s_{q}\bigl(n+\varepsilon\cdot r\bigr)\biggr)\ll q^{-c\mu\lVert(q-1)\vartheta\rVert^{2}} |  |

as μ → ∞ \mu\rightarrow\infty.

A full proof of this statement is given in a manuscript by Jelinek (in preparation). Provided that ρ ′ \rho^{\prime} is close enough to ρ \rho, the gain coming from this estimate is strictly bigger than the contribution ( 2 ρ − ρ ′) 2 (2^{\rho-\rho^{\prime}})^{2} of the artificially added terms. Thus, “the additional camel can be returned”, leaving us with a nontrivial estimate of the original sum.

We have to take care of the fact that ∥ ϑ ∥ \lVert\vartheta\rVert may be very small, yielding only a small gain in the Gowers norm. Correspondingly, our additional margin ρ − ρ ′ \rho-\rho^{\prime} has to be very small too. This issue has been dealt with in our paper [14] with Müllner, see pages 80–81, and only amounts to decreasing the constant c c in the expression N − c ​ ∥ ϑ ∥ 2 N^{-c\lVert\vartheta\rVert^{2}} by some factor.

∎

## 5. Proof of Proposition 1.2

The proof of Proposition 1.2 relies mainly on the following lemma.

###### Lemma 5.1.

Suppose that 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, where c 2 > 0 c_{2}>0. Set N 1 = ⌊ log 2 ⁡ ( 3 K ​ N) ⌋ N_{1}=\lfloor\log_{2}(3^{K}N)\rfloor and N 2 = ⌊ log 3 ⁡ N ⌋ N_{2}=\lfloor\log_{3}N\rfloor let λ > 0, η > 0 \lambda>0,\eta>0 be an arbitrary constant and let d 1 d_{1}, d 2 d_{2} be positive integers. Then for integers

(5.1) |  | N 1 η ≤ k 1 < k 2 < ⋯ < k d 1 ≤ N 1 − N 1 η N_{1}^{\eta}\leq k_{1}<k_{2}<\cdots<k_{d_{1}}\leq N_{1}-N_{1}^{\eta} |  |

and

(5.2) |  | N 2 η ≤ ℓ 1 < ℓ 2 < ⋯ < ℓ d 2 ≤ N 2 − N 2 η N_{2}^{\eta}\leq\ell_{1}<\ell_{2}<\cdots<\ell_{d_{2}}\leq N_{2}-N_{2}^{\eta} |  |

we have for i ∈ { 0, 1 } i\in\{0,1\}, as N → ∞ N\to\infty

 |  | 2 N #{ n < N, n ≡ i mod 2: ε 2, k j 1 ( 3 K n) = b j 1, 1 ≤ j 1 ≤ d 1, ε 3, ℓ j 2 ( n) = c j 2, 1 ≤ j 2 ≤ d 2 } \displaystyle\frac{2}{N}\#\left\{n<N,\,n\equiv i\bmod 2\,:\,\varepsilon_{2,k_{j_{1}}}(3^{K}n)=b_{j_{1}},\,1\leq j_{1}\leq d_{1},\,\varepsilon_{3,\ell_{j_{2}}}(n)=c_{j_{2}},\,1\leq j_{2}\leq d_{2}\right\} |  |

(5.3) |  |  | = 1 2 d 1 ​ 3 d 2 + O ⁡ ( ( log ⁡ N) − λ) \displaystyle=\frac{1}{2^{d_{1}}3^{d_{2}}}+O\left((\log N)^{-\lambda}\right) |  |

and (for r ∈ { 0, 1 } r\in\{0,1\})

 |  | 2 N #{ n < N n ≡ i mod 2: ε 2, k j 1 ( n) = b j 1, 1 ≤ j 1 ≤ d 1, ε 3, ℓ j 2 ( 2 K n + r) = c j 2, 1 ≤ j 2 ≤ d 2 } \displaystyle\frac{2}{N}\#\left\{n<N\,n\equiv i\bmod 2\,:\,\varepsilon_{2,k_{j_{1}}}(n)=b_{j_{1}},\,1\leq j_{1}\leq d_{1},\,\varepsilon_{3,\ell_{j_{2}}}(2^{K}n+r)=c_{j_{2}},\,1\leq j_{2}\leq d_{2}\right\} |  |

(5.4) |  |  | = 1 2 d 1 ​ 3 d 2 + O ⁡ ( ( log ⁡ N) − λ) \displaystyle=\frac{1}{2^{d_{1}}3^{d_{2}}}+O\left((\log N)^{-\lambda}\right) |  |

uniformly for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, b j 1 ∈ { 0, 1 } b_{j_{1}}\in\{0,1\}, c j 2 ∈ { 0, 1, 2 } c_{j_{2}}\in\{0,1,2\} and k j 1 k_{j_{1}}, ℓ i \ell_{i} in the given ranges, where the implicit constant of the error term may depend on h 1 h_{1}, h 2 h_{2}, and on λ \lambda.

We will prove this lemma in Section 5.2 with the help of exponential sum estimates provided in Section 5.1.

The proof of Proposition 1.2 is then given in Section 5.3.

### 5.1. Exponential Sums

The essential part of the proof of Lemma 5.1 are upper bounds for exponential sums of the form

(5.5) |  | S = ∑ n < N, n ≡ i mod 2 e ⁡ ( ( 3 K ​ ∑ j 1 = 1 d 1 h j 1 ​ 2 − k j 1 − 1 + ∑ j 2 = 1 d 2 r j 2 ​ 3 − ℓ j 2 − 1) ​ n), S=\sum_{n<N,\ n\equiv i\bmod 2}e\left(\left(3^{K}\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}-1}+\sum_{j_{2}=1}^{d_{2}}r_{j_{2}}3^{-\ell_{j_{2}}-1}\right)n\right), |  |

where h j 1 h_{j_{1}} are integers not divisible by 2 2, and r j 2 r_{j_{2}} are integers not divisible by 3 3 and h j 1 h_{j_{1}} and r j 2 r_{j_{2}} are absolutely upper bounded by ( log ⁡ N) λ 0 (\log N)^{\lambda_{0}} for some λ 0 > 0 \lambda_{0}>0. For the sake of shortness we only prove the relation ( 5.3). The corresponding relation ( 5.4) can be proved in the same way by interchanging the rôles of 2 2 and 3 3.

Clearly we have

(5.6) |  | | ∑ n < N, n ≡ i mod 2 e ⁡ ( α ​ n) | ≤ 1 2 ​ ‖ 2 ​ α ‖. \left|\sum_{n<N,\,n\equiv i\bmod 2}e(\alpha n)\right|\leq\frac{1}{2\|2\alpha\|}. |  |

Hence we have to find lower bounds for ‖ 2 ​ α ‖ \|2\alpha\|, where

 | α = 3 K ​ ∑ j 1 = 1 d 1 h j 1 ​ 2 − k j 1 − 1 + ∑ j 2 = 1 d 2 r j 2 ​ 3 − m j 2 − 1. \alpha=3^{K}\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}-1}+\sum_{j_{2}=1}^{d_{2}}r_{j_{2}}3^{-m_{j_{2}}-1}. |  |

Actually, we will prove that (uniformly under the above mentioned assumptions)

(5.7) |  | ‖ 2 ​ α ‖ ≫ ( log ⁡ N) λ N \|2\alpha\|\gg\frac{(\log N)^{\lambda}}{N} |  |

for any given constant λ > 0 \lambda>0. This implies then the following property.

###### Lemma 5.2.

Suppose that 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, where c 2 > 0 c_{2}>0. Set N 1 = ⌊ log 2 ⁡ ( 3 K ​ N) ⌋ N_{1}=\lfloor\log_{2}(3^{K}N)\rfloor and N 2 = ⌊ log 3 ⁡ N ⌋ N_{2}=\lfloor\log_{3}N\rfloor let λ 0 > 0, λ > 0 \lambda_{0}>0,\lambda>0 be arbitrary constants and let d 1 d_{1}, d 2 d_{2} be positive integers. Then for integers

 | N 1 η ≤ k 1 < k 2 < ⋯ < k d 1 ≤ N 1 − N 1 η, N_{1}^{\eta}\leq k_{1}<k_{2}<\cdots<k_{d_{1}}\leq N_{1}-N_{1}^{\eta}, |  |

 | N 2 η ≤ ℓ 1 < ℓ 2 < ⋯ < ℓ d 2 ≤ N 2 − N 2 η N_{2}^{\eta}\leq\ell_{1}<\ell_{2}<\cdots<\ell_{d_{2}}\leq N_{2}-N_{2}^{\eta} |  |

and for odd integers h 1, …, h d 2 h_{1},\ldots,h_{d_{2}} and integers r 1, …, r d 2 r_{1},\ldots,r_{d_{2}} that are not divisible by 3 3 with

 | max 1 ≤ j 1 ≤ d 1 ⁡ | k j 1 | ≤ ( log ⁡ N) 2 ​ λ 0 and max 1 ≤ j 2 ≤ d 2 | r j 2 | ≤ ( log ⁡ N) 2 ​ λ 0 \max_{1\leq j_{1}\leq d_{1}}|k_{j_{1}}|\leq(\log N)^{2\lambda_{0}}\quad\mbox{and}\quad\max_{1\leq j_{2}\leq d_{2}}|r_{j_{2}}|\leq(\log N)^{2\lambda_{0}} |  |

we have the uniform upper bouund

(5.8) |  | max ⁡ | S | ≪ N ​ ( log ⁡ N) − λ, \max|S|\ll N(\log N)^{-\lambda}, |  |

where S S denotes the exponential sum ( 5.5).

We will distinguish between several cases.

#### 5.1.1. d 1 = 0 d_{1}=0

In this case α \alpha simplifies to

 | α = ∑ j 2 = 1 d 2 r j 2 ​ 3 − ℓ j 2 − 1. \alpha=\sum_{j_{2}=1}^{d_{2}}r_{j_{2}}3^{-\ell_{j_{2}}-1}. |  |

By assumption ( 5.2) we have N 2 η ≤ ℓ j 2 ≤ N 2 − N 2 η N_{2}^{\eta}\leq\ell_{j_{2}}\leq N_{2}-N_{2}^{\eta}, | r j 2 | ≤ ( log ⁡ N) λ |r_{j_{2}}|\leq(\log N)^{\lambda} and r j 2 r_{j_{2}} is not divisible by 3 3, 1 ≤ j 2 ≤ d 2 1\leq j_{2}\leq d_{2}. Consequently

 | ‖ 2 ​ α ‖ = 2 ​ | α | = | 2 ​ ∑ j 2 = 1 d 2 r i ​ 3 − ℓ i − 1 | ≥ 2 3 ℓ d 2 + 1 ≫ e c ​ ( log ⁡ N) η N ≫ ( log ⁡ N) λ N \|2\alpha\|=2|\alpha|=\left|2\sum_{j_{2}=1}^{d_{2}}r_{i}3^{-\ell_{i}-1}\right|\geq\frac{2}{3^{\ell_{d_{2}}+1}}\gg\frac{e^{c(\log N)^{\eta}}}{N}\gg\frac{(\log N)^{\lambda}}{N} |  |

for some constant c > 0 c>0.

#### 5.1.2. d 2 = 0 d_{2}=0

Here we have

 | α = 3 K ​ ∑ j 1 = 1 d 1 h j 1 ​ 2 − k j 1 − 1, \alpha=3^{K}\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}-1}, |  |

where N 1 η ≤ k j 1 ≤ N 1 − N 1 η N_{1}^{\eta}\leq k_{j_{1}}\leq N_{1}-N_{1}^{\eta}, | h j 1 | ≤ ( log ⁡ N) λ |h_{j_{1}}|\leq(\log N)^{\lambda} and h j 1 h_{j_{1}} is not divisible by 2 2. Recall that N 1 = ⌊ log 2 ⁡ ( 3 K ​ N) ⌋ N_{1}=\lfloor\log_{2}(3^{K}N)\rfloor. Let H H denote the nearest integer to α \alpha, that is,

 | ‖ 2 ​ α ‖ = | 2 ​ α − H |. \|2\alpha\|=|2\alpha-H|. |  |

In a first step we assume that H = 0 H=0. Here we can argue similiarly as in the previous case:

 | ‖ 2 ​ α ‖ = 2 ​ | α | = 3 K ​ | ∑ j 1 = 1 d 1 h j 1 ​ 2 − k j 1 | ≥ 3 K 2 k d 1 ≫ 3 K ​ e c ​ ( log ⁡ N) η 3 K ​ N ≫ ( log ⁡ N) λ N \|2\alpha\|=2|\alpha|=3^{K}\left|\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}}\right|\geq\frac{3^{K}}{2^{k_{d_{1}}}}\gg\frac{3^{K}e^{c(\log N)^{\eta}}}{3^{K}N}\gg\frac{(\log N)^{\lambda}}{N} |  |

and we are done.

Next suppose that H ≠ 0 H\neq 0. Since ‖ 2 ​ α ‖ ≤ 1 \|2\alpha\|\leq 1 it follows that

 | | H | ≤ 1 + 3 K ​ ( log ⁡ N) λ ​ 2 − k 1. |H|\leq 1+3^{K}(\log N)^{\lambda}2^{-k_{1}}. |  |

Set H = 3 L ​ H ′ H=3^{L}H^{\prime} with ( 3, H ′) = 1 (3,H^{\prime})=1. Since | H | ≤ 3 K |H|\leq 3^{K} it follows that L ≤ K L\leq K. Furthermore set

 | D \displaystyle D | = gcd ⁡ ( 3 K − L ​ h 1 ​ 2 k d 1 − k 1, 3 K − L ​ h 2 ​ 2 k d 1 − 1 − k 1, …, 3 K − L ​ h d 1, H ′ ​ 2 k d 1 + 1) \displaystyle={\rm gcd}\left(3^{K-L}h_{1}2^{k_{d_{1}}-k_{1}},3^{K-L}h_{2}2^{k_{d_{1}-1}-k_{1}},\ldots,3^{K-L}h_{d_{1}},H^{\prime}2^{k_{d_{1}}+1}\right) |  |

 |  | = gcd ⁡ ( h 1, h 2, …, h d 1, H ′). \displaystyle={\rm gcd}\left(h_{1},h_{2},\ldots,h_{d_{1}},H^{\prime}\right). |  |

Note that H ′ H^{\prime} is not divisible by 3 3 and h d h_{d} not by 2 2. Thus, the last equality holds. We also set

 | h j 1 ′ = h j 1 / D and H ′′ = H ′ / D. h_{j_{1}}^{\prime}=h_{j_{1}}/D\quad\mbox{and}\quad H^{\prime\prime}=H^{\prime}/D. |  |

Then we have

 | ‖ 2 ​ α ‖ = D ​ 3 L 2 k d 1 ​ | 3 K − L ​ h 1 ′ ​ 2 k d 1 − k 1 + 3 K − L ​ h 2 ′ ​ 2 k d 1 − 1 − k 1 + ⋯ + 3 K − L ​ h d 1 ′ − H ′′ ​ 2 k d 1 + 1 |. \|2\alpha\|=\frac{D3^{L}}{2^{k_{d_{1}}}}\left|3^{K-L}h_{1}^{\prime}2^{k_{d_{1}}-k_{1}}+3^{K-L}h_{2}^{\prime}2^{k_{d_{1}-1}-k_{1}}+\cdots+3^{K-L}h_{d_{1}}^{\prime}-H^{\prime\prime}2^{k_{d_{1}}+1}\right|. |  |

At this level we can apply Lemma 3.4 and we obtain

 | ‖ α ‖ \displaystyle\|\alpha\| | ≫ D ​ 3 L 2 k d 1 + 1 ​ ( 3 K − L ​ 2 k d 1 − k 1) 1 − δ | h 1 ′ ⋯ h d 1 ′ H ′′ | \displaystyle\gg\frac{D3^{L}}{2^{k_{d_{1}}+1}}\frac{\left(3^{K-L}2^{k_{d_{1}}-k_{1}}\right)^{1-\delta}}{|h_{1}^{\prime}\cdots h_{d_{1}}^{\prime}\,H^{\prime\prime}|} |  |

 |  | ≫ D ​ 3 L 2 k d 1 + 1 ​ ( 3 K − L ​ 2 k d 1 − k 1) 1 − δ ( log ⁡ N) d 1 ​ λ ​ 3 K − L / ( D ​ 2 k 1) \displaystyle\gg\frac{D3^{L}}{2^{k_{d_{1}}+1}}\frac{\left(3^{K-L}2^{k_{d_{1}}-k_{1}}\right)^{1-\delta}}{(\log N)^{d_{1}\lambda}3^{K-L}/(D2^{k_{1}})} |  |

 |  | ≫ 3 L ( 3 K − L ​ 2 k d 1 − k 1) δ \displaystyle\gg\frac{3^{L}}{\left(3^{K-L}2^{k_{d_{1}}-k_{1}}\right)^{\delta}} |  |

 |  | ≫ 1 ( 3 K ​ 2 k d 1 − k 1) δ. \displaystyle\gg\frac{1}{\left(3^{K}2^{k_{d_{1}}-k_{1}}\right)^{\delta}}. |  |

Since

 | 3 K ​ 2 k d 1 − k 1 ≤ 3 2 ​ K ​ N ≤ N 1 + 2 ​ c 2 3^{K}2^{k_{d_{1}}-k_{1}}\leq 3^{2K}N\leq N^{1+2c_{2}} |  |

we, thus, obtain

 | ‖ 2 ​ α ‖ ≫ N − δ ⁡ ( 1 + 2 ​ c 2). \|2\alpha\|\gg N^{-\delta(1+2c_{2})}. |  |

Hence by choosing δ = ( 1 + 2 ​ c 2) / 2 \delta=(1+2c_{2})/2 we get a proper lower bound N − 1 / 2 ≫ ( log N) λ / N N^{-1/2}\gg(\log N)^{\lambda}/N.

#### 5.1.3. d 1 > 0 d_{1}>0 and d 2 > 0 d_{2}>0

As in the previous case let H H be the nearest integer to 2 ​ α 2\alpha, that is, ‖ 2 ​ α ‖ = | 2 ​ α − H | \|2\alpha\|=|2\alpha-H|.

First we consider the case H = 0 H=0. Here we have

 | ‖ α ‖ = | 3 K ​ ∑ j 1 = 1 d 1 h j 1 ​ 2 − k j 1 + 2 ​ ∑ j 2 = 1 d 2 r i ​ 3 − m i − 1 | \|\alpha\|=\left|3^{K}\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}}+2\sum_{j_{2}=1}^{d_{2}}r_{i}3^{-m_{i}-1}\right| |  |

In this case we proceed precisely as in the paper [9], where we apply Lemma 3.2 appropriately.

Without loss of generality we can assume that h j 1 ≠ 0 h_{j_{1}}\neq 0 and r j 2 ≠ 0 r_{j_{2}}\neq 0 (for all j j and i i). Otherwise we reduce d 1 d_{1} and d 2 d_{2} accordingly.

We set δ = η / ( d 1 + d 2) \delta=\eta/(d_{1}+d_{2}). Clearly there exists 0 ≤ k ≤ d 1 + d 2 − 1 0\leq k\leq d_{1}+d_{2}-1 such that

 | h j 1 + 1 − h j 1 ∉ [( log ⁡ N) k ​ δ, ( log ⁡ N) ( k + 1) ​ δ) ( 1 ≤ j 1 < d 1) h_{j_{1}+1}-h_{j_{1}}\not\in\left[(\log N)^{k\delta},(\log N)^{(k+1)\delta}\right)\quad(1\leq j_{1}<d_{1}) |  |

and

 | r j 2 + 1 − r j 2 ∉ [( log ⁡ N) k ​ δ, ( log ⁡ N) ( k + 1) ​ δ) ( 1 ≤ j 2 < d 2). r_{j_{2}+1}-r_{j_{2}}\not\in\left[(\log N)^{k\delta},(\log N)^{(k+1)\delta}\right)\quad(1\leq j_{2}<d_{2}). |  |

We first suppose that

 | h j 1 + 1 − h j 1 ≤ ( log ⁡ N) k ​ δ ( 1 ≤ j 1 < d 1) and r i + 1 − r j 2 ≤ ( log ⁡ N) k ​ δ ( 1 ≤ j 2 < d 2). h_{j_{1}+1}-h_{j_{1}}\leq(\log N)^{k\delta}\quad(1\leq j_{1}<d_{1})\quad\mbox{and}\quad r_{i+1}-r_{j_{2}}\leq(\log N)^{k\delta}\quad(1\leq j_{2}<d_{2}). |  |

Then we can represent α \alpha as

 | α = a ​ 3 K ​ 2 − k d 2 − 1 + b ​ 3 − ℓ d 2 − 1, \alpha=a3^{K}2^{-k_{d_{2}}-1}+b3^{-\ell_{d_{2}}-1}, |  |

where

 | a = ∑ j 1 = 1 d 1 h j 1 ​ 2 k d 1 − k j and b = ∑ j 2 = 1 d 2 r j 2 ​ 2 ℓ d 2 − ℓ j 2 a=\sum_{j_{1}=1}^{d_{1}}h_{j_{1}}2^{k_{d_{1}}-k_{j}}\quad\mbox{and}\quad b=\sum_{j_{2}=1}^{d_{2}}r_{j_{2}}2^{\ell_{d_{2}}-\ell_{j_{2}}} |  |

satisfy

 | log ⁡ | a | ≪ ( log ⁡ N) k ​ δ and log | b | ≪ ( log ⁡ N) k ​ δ. \log|a|\ll(\log N)^{k\delta}\quad\mbox{and}\quad\log|b|\ll(\log N)^{k\delta}. |  |

By a direct application of Lemma 3.2 we obtain

 | 2 ​ | α | = | a ​ 3 K ​ 2 − k d 1 + 2 ​ b ​ 3 − ℓ d 2 − 1 | ≥ max ⁡ ( | a ​ 3 K ​ 2 − k d 1 |, | 2 ​ b ​ 3 − ℓ d 2 − 1 |) ​ e − C ′ ​ log ⁡ log ⁡ N ​ ( log ⁡ N) k ​ δ 2|\alpha|=\left|a3^{K}2^{-k_{d_{1}}}+2b3^{-\ell_{d_{2}}-1}\right|\geq\max\left(\left|a3^{K}2^{-k_{d_{1}}}\right|,\left|2b3^{-\ell_{d_{2}}-1}\right|\right)e^{-C^{\prime}\log\log N(\log N)^{k\delta}} |  |

for some constant C ′ > 0 C^{\prime}>0. Clearly this implies

 | | 2 ​ α | ≫ e c ​ ( log ⁡ N) η N ​ e − C ′ ​ log ⁡ log ⁡ N ​ ( log ⁡ N) k ​ δ ≫ e c ′ ​ ( log ⁡ N) η N ≫ ( log ⁡ N) λ N |2\alpha|\gg\frac{e^{c(\log N)^{\eta}}}{N}e^{-C^{\prime}\log\log N(\log N)^{k\delta}}\gg\frac{e^{c^{\prime}(\log N)^{\eta}}}{N}\gg\frac{(\log N)^{\lambda}}{N} |  |

for some constants c > 0, c ′ > 0 c>0,c^{\prime}>0.

In general we assume that for some s 1 ≤ d 1 s_{1}\leq d_{1} and s 2 ≤ d 2 s_{2}\leq d_{2}

 | h j 1 + 1 − h j ≤ ( log ⁡ N) k ​ δ ( 1 ≤ j 1 < s 1) and r j 2 + 1 − r i ≤ ( log ⁡ N) k ​ δ ( 1 ≤ j 2 < s 2) h_{j_{1}+1}-h_{j}\leq(\log N)^{k\delta}\quad(1\leq j_{1}<s_{1})\quad\mbox{and}\quad r_{j_{2}+1}-r_{i}\leq(\log N)^{k\delta}\quad(1\leq j_{2}<s_{2}) |  |

but

 | h s 1 + 1 − h s 1 > ( log ⁡ N) ( k + 1) ​ δ and r s 2 + 1 − r s 2 > ( log ⁡ N) ( k + 1) ​ δ. h_{s_{1}+1}-h_{s_{1}}>(\log N)^{(k+1)\delta}\quad\mbox{and}\quad r_{s_{2}+1}-r_{s_{2}}>(\log N)^{(k+1)\delta}. |  |

Here we set

 | a = ∑ j 1 = 1 s 1 h j 1 ​ 2 k s 1 − k j 1 and b = ∑ j 2 = 1 s 2 r j 2 ​ 2 ℓ s 2 − ℓ j 2 a=\sum_{j_{1}=1}^{s_{1}}h_{j_{1}}2^{k_{s_{1}}-k_{j_{1}}}\quad\mbox{and}\quad b=\sum_{j_{2}=1}^{s_{2}}r_{j_{2}}2^{\ell_{s_{2}}-\ell_{j_{2}}} |  |

and use the upper bounds

 | ∑ j 1 = s 1 + 1 d 1 h j 1 ​ 2 − k j 1 − 1 ≪ ( log ⁡ N) 2 ​ λ 0 ​ 2 − k s 1 − ( log ⁡ N) ( k + 1) ​ δ and ∑ j 2 = s 2 + 1 d 2 r j 2 ​ 3 − ℓ j 2 − 1 ≪ ( log ⁡ N) 2 ​ λ 0 ​ 3 − ℓ s 2 − ( log ⁡ N) ( k + 1) ​ δ \sum_{j_{1}=s_{1}+1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}-1}\ll(\log N)^{2\lambda_{0}}2^{-k_{s_{1}}-(\log N)^{(k+1)\delta}}\quad\mbox{and}\quad\sum_{j_{2}=s_{2}+1}^{d_{2}}r_{j_{2}}3^{-\ell_{j_{2}}-1}\ll(\log N)^{2\lambda_{0}}3^{-\ell_{s_{2}}-(\log N)^{(k+1)\delta}} |  |

to obtain the lower bound for

 | | 2 ​ α | \displaystyle|2\alpha| | ≥ | a ​ 3 K ​ 2 − k s 1 + 2 ​ b ​ 3 − ℓ s 2 − 1 | − | 3 K ​ ∑ j 1 = s 1 + 1 d 1 h j 1 ​ 2 − k j 1 | − | 2 ​ ∑ j 2 = s 2 + 1 d 2 r j 2 ​ 3 − ℓ j 2 − 1 | \displaystyle\geq\left|a3^{K}2^{-k_{s_{1}}}+2b3^{-\ell_{s_{2}}-1}\right|-\left|3^{K}\sum_{j_{1}=s_{1}+1}^{d_{1}}h_{j_{1}}2^{-k_{j_{1}}}\right|-\left|2\sum_{j_{2}=s_{2}+1}^{d_{2}}r_{j_{2}}3^{-\ell_{j_{2}}-1}\right| |  |

 |  | ≥ max ⁡ ( | a ​ 3 K ​ 2 − k s 1 |, | 2 ​ b ​ 3 − ℓ s 2 − 1 |) ​ e − C ′ ​ log ⁡ log ⁡ N ​ ( log ⁡ N) k ​ δ \displaystyle\geq\max\left(\left|a3^{K}2^{-k_{s_{1}}}\right|,\left|2b3^{-\ell_{s_{2}}-1}\right|\right)e^{-C^{\prime}\log\log N(\log N)^{k\delta}} |  |

 |  | − O ⁡ ( max ⁡ ( | 3 K ​ 2 − k s 1 |, | 2 3 − ℓ s 2 − 1 |) ​ ( log ⁡ N) 2 ​ λ 0 ​ e − c ​ ( log ⁡ N) ( k + 1) ​ δ) \displaystyle-O\left(\max\left(\left|3^{K}2^{-k_{s_{1}}}\right|,\left|2\,3^{-\ell_{s_{2}}-1}\right|\right)(\log N)^{2\lambda_{0}}e^{-c(\log N)^{(k+1)\delta}}\right) |  |

 |  | ≫ max ⁡ ( | a ​ 3 K ​ 2 − k s 1 |, | 2 ​ b ​ 3 − ℓ s 2 − 1 |) ​ e − C ′ ​ log ⁡ log ⁡ N ​ ( log ⁡ N) k ​ δ \displaystyle\gg\max\left(\left|a3^{K}2^{-k_{s_{1}}}\right|,\left|2b3^{-\ell_{s_{2}}-1}\right|\right)e^{-C^{\prime}\log\log N(\log N)^{k\delta}} |  |

 |  | ≫ e c ′ ​ ( log ⁡ N) η N ≫ ( log ⁡ N) λ N. \displaystyle\gg\frac{e^{c^{\prime}(\log N)^{\eta}}}{N}\gg\frac{(\log N)^{\lambda}}{N}. |  |

This completes the case H = 0 H=0.

In the case H ≠ 0 H\neq 0 we proceed very similiarly to the case d 2 = 0 d_{2}=0. Since ‖ 2 ​ α ‖ ≤ 1 \|2\alpha\|\leq 1 we certainly have the upper bound

 | | H | ≤ 1 + ( log ⁡ N) λ ​ 3 K 2 k 1 |H|\leq 1+(\log N)^{\lambda}\frac{3^{K}}{2^{k_{1}}} |  |

We now reduce the general case to the coprime one and apply Lemma 3.5.

This completes the proof of Lemma 5.2.

### 5.2. Proof of Lemma 5.1

We follow [2] and [9]. Let f b, q, Δ ​ ( x) f_{b,q,\Delta}(x) be defined by

 | f b, q, Δ ( x):= 1 Δ ∫ − Δ / 2 Δ / 2 𝟏 [b q, b + 1 q] ( { x + z }) d z, f_{b,q,\Delta}(x):=\frac{1}{\Delta}\int_{-\Delta/2}^{\Delta/2}{\bf 1}_{[\frac{b}{q},\frac{b+1}{q}]}(\{x+z\})\,dz, |  |

where 𝟏 A {\bf 1}_{A} denotes the characteristic function of the set A A and { x } = x − [x] \{x\}=x-[x] the fractional part of x x. The Fourier coefficients of the Fourier series f b, q, Δ ​ ( x) = ∑ m ∈ 𝐙 d m, b, q, Δ ​ e ​ ( m ​ x) f_{b,q,\Delta}(x)=\sum_{m\in{\bf Z}}d_{m,b,q,\Delta}e(mx) are given by

 | d 0, b, q, Δ = 1 q d_{0,b,q,\Delta}=\frac{1}{q} |  |

and for m ≠ 0 m\neq 0 by

 | d m, b, q, Δ = e ⁡ ( − m ​ b q) − e ⁡ ( − m ⁡ ( b + 1) q) 2 ​ π ​ i ​ m ⋅ e ⁡ ( m ​ Δ 2) − e ⁡ ( − m ​ Δ 2) 2 ​ π ​ i ​ m ​ Δ. d_{m,b,q,\Delta}=\frac{e\left(-\frac{mb}{q}\right)-e\left(-\frac{m(b+1)}{q}\right)}{2\pi im}\cdot\frac{e\left(\frac{m\Delta}{2}\right)-e\left(-\frac{m\Delta}{2}\right)}{2\pi im\Delta}. |  |

Note that d m, b, q, Δ = 0 d_{m,b,q,\Delta}=0 if m ≠ 0 m\neq 0 and m ≡ 0 mod q m\equiv 0\bmod q and that

 | | d m, b, q, Δ | ≤ min ⁡ ( 1 π ​ | m |, 1 Δ ​ π ​ m 2). |d_{m,b,q,\Delta}|\leq\min\left(\frac{1}{\pi|m|},\frac{1}{\Delta\pi m^{2}}\right). |  |

By definition we have 0 ≤ f b, q, Δ ​ ( x) ≤ 1 0\leq f_{b,q,\Delta}(x)\leq 1 and

 | f b, q, Δ ​ ( x) = { 1 if ​ x ∈ [b q + Δ, b + 1 q − Δ], 0 if ​ x ∈ [0, 1] ∖ [b q − Δ, b + 1 q + Δ]. f_{b,q,\Delta}(x)=\left\{\begin{array}[]{cl}1&\mbox{if }x\in\left[\frac{b}{q}+\Delta,\frac{b+1}{q}-\Delta\right],\\ 0&\mbox{if }x\in[0,1]\setminus\left[\frac{b}{q}-\Delta,\frac{b+1}{q}+\Delta\right].\end{array}\right. |  |

So if we set

 | t ⁡ ( y 1, y 2):= ∏ j 1 = 1 d 1 f b j 1, 2, Δ ​ ( y 1 2 k j 1 + 1) ​ ∏ j 2 = 1 d 2 f c j 2, 3, Δ ​ ( y 2 3 ℓ j 2 + 1) t(y_{1},y_{2}):=\prod_{j_{1}=1}^{d_{1}}f_{b_{j_{1}},2,\Delta}\left(\frac{y_{1}}{2^{k_{j_{1}}+1}}\right)\prod_{j_{2}=1}^{d_{2}}f_{c_{j_{2}},3,\Delta}\left(\frac{y_{2}}{3^{\ell_{j_{2}}+1}}\right) |  |

then we get for Δ < 1 / 12 \Delta<1/12

 | | #{ n < N, n ≡ i mod 2 | ε 2, k j 1 ( 3 K n) = b j 1, 1 ≤ j 1 ≤ d 1, ε 3, ℓ j 2 ( n) = c j 2, 1 ≤ j 2 ≤ d 2 } − ∑ n < N, n ≡ i mod 2 t ( 3 K n, n) | \displaystyle\left|\#\left\{n<N,\,n\equiv i\bmod 2\,|\,\varepsilon_{2,k_{j_{1}}}(3^{K}n)=b_{j_{1}},\ 1\leq j_{1}\leq d_{1},\ \varepsilon_{3,\ell_{j_{2}}}(n)=c_{j_{2}},\ 1\leq j_{2}\leq d_{2}\right\}-\sum_{n<N,\,n\equiv i\bmod 2}t(3^{K}n,n)\right| |  |

 | ≤ ∑ j 1 = 1 d 1 #{ n < N | { 3 K ​ n 2 k j 1 + 1 } ∈ U b j 1, 2, Δ } + ∑ j 2 = 1 d 2 #{ n < N | { n 3 ℓ j 2 + 1 } ∈ U c j 2, 3, Δ } \displaystyle\quad\leq\sum_{j_{1}=1}^{d_{1}}\#\left\{n<N\left|\left\{\frac{3^{K}n}{2^{k_{j_{1}}+1}}\right\}\in U_{b_{j_{1}},2,\Delta}\right.\right\}+\sum_{j_{2}=1}^{d_{2}}\#\left\{n<N\left|\left\{\frac{n}{3^{\ell_{j_{2}}+1}}\right\}\in U_{c_{j_{2}},3,\Delta}\right.\right\} |  |

 | ≪ Δ ​ N + N ​ ∑ j 1 = 1 d 1 D 1 ​ ( k j 1) + N ​ ∑ j 2 = 1 d 2 D 2 ​ ( ℓ j 2) \displaystyle\quad\ll\Delta N+N\sum_{j_{1}=1}^{d_{1}}D_{1}(k_{j_{1}})+N\sum_{j_{2}=1}^{d_{2}}D_{2}(\ell_{j_{2}}) |  |

where

 | U b, q, Δ:= [0, Δ] ∪ ⋃ b = 1 q − 1 [b q − Δ, b q + Δ] ∪ [1 − Δ, 1]. U_{b,q,\Delta}:=[0,\Delta]\cup\bigcup_{b=1}^{q-1}\left[\frac{b}{q}-\Delta,\frac{b}{q}+\Delta\right]\cup[1-\Delta,1]. |  |

and D 1 ​ ( k j 1) D_{1}(k_{j_{1}}) and D 2 ​ ( ℓ j 2) D_{2}(\ell_{j_{2}}), respectively, denote the discrepancies of the sequences ( 3 K n 2 − k j 1 − 1 mod 1: n < N) (3^{K}n2^{-k_{j_{1}}-1}\bmod 1:n<N) and ( n 3 − ℓ j 2 − 1 mod 1: n < N) (n3^{-\ell_{j_{2}}-1}\bmod 1:n<N). The discrepancies D 1 ​ ( k j 1) D_{1}(k_{j_{1}}) and D 2 ​ ( ℓ j 2) D_{2}(\ell_{j_{2}}) that can be bounded with the help of the Erdős-Turan inequality and exponential sum estimates.

For D 2 ​ ( ℓ j 2) D_{2}(\ell_{j_{2}}) we directly obtain

 | D 2 ​ ( ℓ j 2) \displaystyle D_{2}(\ell_{j_{2}}) | ≪ 1 H + ∑ h = 1 H 1 h ​ | 1 N ​ ∑ n < N e ⁡ ( h ​ n ​ 3 − ℓ j 2 − 1) | \displaystyle\ll\frac{1}{H}+\sum_{h=1}^{H}\frac{1}{h}\left|\frac{1}{N}\sum_{n<N}e\left(hn3^{-\ell_{j_{2}}-1}\right)\right| |  |

 |  | ≪ 1 H + log ⁡ H ​ 3 ℓ j 2 N ≪ ( log ⁡ N) − λ \displaystyle\ll\frac{1}{H}+\log H\frac{3^{\ell_{j_{2}}}}{N}\ll(\log N)^{-\lambda} |  |

by using the estimate ( 5.6), setting H = ( log ⁡ N) λ 0 H=(\log N)^{\lambda_{0}} (for some λ 0 ≥ λ \lambda_{0}\geq\lambda) and applying the bound ℓ j 2 ≤ N 2 − N 2 η \ell_{j_{2}}\leq N_{2}-N_{2}^{\eta}.

For D 1 ​ ( k j 1) D_{1}(k_{j_{1}}) we have to be slightly more careful but we can use the bounds provided in Section 5.1.2 (note that λ \lambda is replaced by λ + 1 \lambda+1):

 | ∑ n < N e ⁡ ( h ​ 3 K ​ n ​ 2 − k j 1 − 1) ≪ N ​ ( log ⁡ N) − λ − 1 \sum_{n<N}e\left(h3^{K}n2^{-k_{j_{1}}-1}\right)\ll N(\log N)^{-\lambda-1} |  |

Obviously this leads to

 | D 1 ​ ( k j 1) \displaystyle D_{1}(k_{j_{1}}) | ≪ 1 H + ∑ h = 1 H 1 h ​ | 1 N ​ ∑ n < N e ⁡ ( h ​ 3 K ​ n ​ 2 − k j 1 − 1) | \displaystyle\ll\frac{1}{H}+\sum_{h=1}^{H}\frac{1}{h}\left|\frac{1}{N}\sum_{n<N}e\left(h3^{K}n2^{-k_{j_{1}}-1}\right)\right| |  |

 |  | ≪ 1 H + log ⁡ H ​ ( log ⁡ N) − λ − 1 ≪ ( log ⁡ N) − λ. \displaystyle\ll\frac{1}{H}+\log H(\log N)^{-\lambda-1}\ll(\log N)^{-\lambda}. |  |

Summing up, by setting Δ = ( log ⁡ N) − λ 0 \Delta=(\log N)^{-\lambda_{0}} for some λ 0 ≥ λ \lambda_{0}\geq\lambda we get

 | | #{ n < N | ε 2, k j 1 ( 3 K n) = b j 1, 1 ≤ j 1 ≤ d 1, ε 3, ℓ j 2 ( n) = c j 2, 1 ≤ j 2 ≤ d 2 } − ∑ n < N t ( 3 K n, n) | \displaystyle\left|\#\left\{n<N\,|\,\varepsilon_{2,k_{j_{1}}}(3^{K}n)=b_{j_{1}},\ 1\leq j_{1}\leq d_{1},\ \varepsilon_{3,\ell_{j_{2}}}(n)=c_{j_{2}},\ 1\leq j_{2}\leq d_{2}\right\}-\sum_{n<N}t(3^{K}n,n)\right| |  |

 | ≪ N ​ ( log ⁡ N) − λ. \displaystyle\quad\ll N(\log N)^{-\lambda}. |  |

For convenience, let 𝐡 = ( h 1, …, h d 1) {\bf h}=(h_{1},\ldots,h_{d_{1}}) and 𝐫 = ( r 1, …, r d 2) {\bf r}=(r_{1},\ldots,r_{d_{2}}) denote d 1 d_{1} - and d 2 d_{2} -dimensional integer vectors and 𝐯 = ( 2 − k 1 − 1, …, 2 − k d 1 − 1) {\bf v}=\left(2^{-k_{1}-1},\ldots,2^{-k_{d_{1}}-1}\right), 𝐰 = ( 3 − ℓ 1 − 1, …, 3 − ℓ d 2 − 1) {\bf w}=\left(3^{-\ell_{1}-1},\ldots,3^{-\ell_{d_{2}}-1}\right). Furthermore set

 | T 𝐡, 𝐫:= ∏ j 1 = 1 d 1 d h j 1, b j 1, 2, Δ ​ ∏ j 2 = 1 d 2 d r j 2, c j 2, 3, Δ. T_{{\bf h},{\bf r}}:=\prod_{j_{1}=1}^{d_{1}}d_{h_{j_{1}},b_{j_{1}},2,\Delta}\prod_{j_{2}=1}^{d_{2}}d_{r_{j_{2}},c_{j_{2}},3,\Delta}. |  |

Then t ⁡ ( y 1, y 2) t(y_{1},y_{2}) has the Fourier series expansion

 | t ⁡ ( y 1, y 2) = ∑ 𝐡, 𝐫 T 𝐡, 𝐫 ​ e ​ ( 𝐡 ⋅ 𝐯 ​ y 1 + 𝐫 ⋅ 𝐰 ​ y 2). t(y_{1},y_{2})=\sum_{{\bf h},{\bf r}}T_{{\bf h},{\bf r}}e\left({\bf h}\cdot{\bf v}\,y_{1}+{\bf r}\cdot{\bf w}\,y_{2}\right). |  |

Thus, we are led to consider the sums

(5.9) |  | ∑ n < N, n ≡ i mod 2 t ⁡ ( 3 K ​ n, n) = ∑ 𝐡, 𝐫 T 𝐡, 𝐫 ​ ∑ n < N e ⁡ ( ( 3 K ​ 𝐡 ⋅ 𝐯 + 𝐫 ⋅ 𝐰) ​ n) \sum_{n<N,\,n\equiv i\bmod 2}t(3^{K}n,n)=\sum_{{\bf h},{\bf r}}T_{{\bf h},{\bf r}}\sum_{n<N}e\left(\left(3^{K}{\bf h}\cdot{\bf v}+{\bf r}\cdot{\bf w}\right)n\right) |  |

If 𝐡 = 𝐫 = 𝟎 {\bf h}={\bf r}={\bf 0} then

 | T 𝟎, 𝟎 ​ ∑ n < N, n ≡ i mod 2 e ⁡ ( 0) = N / 2 + O ⁡ ( 1) 2 d 1 ​ 3 d 2 T_{{\bf 0},{\bf 0}}\sum_{n<N,\,n\equiv i\bmod 2}e\left(0\right)=\frac{N/2+O(1)}{2^{d_{1}}3^{d_{2}}} |  |

which provides the leading term. Furthermore, we have (for Δ = ( log ⁡ N) λ 0 \Delta=(\log N)^{\lambda_{0}}) the estimate

 | ∑ ( 𝐡, 𝐫) ≠ ( 𝟎, 𝟎) | T 𝐡, 𝐫 | ≪ ( 2 + 2 ​ log ⁡ ( 1 / Δ)) d 1 + d 2 ≪ ( log ⁡ log ⁡ N) d 1 + d 2 \sum_{({\bf h},{\bf r})\neq({\bf 0},{\bf 0})}|T_{{\bf h},{\bf r}}|\ll(2+2\log(1/\Delta))^{d_{1}+d_{2}}\ll(\log\log N)^{d_{1}+d_{2}} |  |

and

 | ∑ ‖ ( 𝐡, 𝐫) ‖ ≥ ( log ⁡ N) 2 ​ λ 0 | T 𝐡, 𝐫 | ≪ ( log ⁡ N) − λ 0. \sum_{\|({\bf h},{\bf r})\|\geq(\log N)^{2\lambda_{0}}}|T_{{\bf h},{\bf r}}|\ll(\log N)^{-\lambda_{0}}. |  |

Thus,

 | ∑ n < N, n ≡ i mod 2 t ⁡ ( 3 K ​ n, n) = N / 2 + O ⁡ ( 1) 2 d 1 ​ 3 d 2 + O ⁡ ( ( log ⁡ log ⁡ N) d 1 + d 2 ​ ( log ⁡ N) − λ) + O ⁡ ( ( log ⁡ N) − λ 0) \sum_{n<N,\,n\equiv i\bmod 2}t(3^{K}n,n)=\frac{N/2+O(1)}{2^{d_{1}}3^{d_{2}}}+O\left((\log\log N)^{d_{1}+d_{2}}(\log N)^{-\lambda}\right)+O\left((\log N)^{-\lambda_{0}}\right) |  |

This completes the proof of Lemma 5.1.

### 5.3. Completion of the proof of Proposition 1.2

We finally show that Lemma 5.1 implies Proposition 1.2 (again we follows [9]).

The idea is to compare the distribution of ( s 2 ​ ( 3 K ​ n), s 3 ​ ( n)) (s_{2}(3^{K}n),s_{3}(n)), n < N n<N, n ≡ i mod 2 n\equiv i\bmod 2, with the distribution of independent pairs of sums of iid random variables. Let Z 2, j Z_{2,j} be iid random variables that are uniformly distribution on { 0, 1 } \{0,1\} and Z 3, j Z_{3,j} iid random variables on { 0, 1, 2 } \{0,1,2\} that are also independent of Z 2, j Z_{2,j}. Then we consider the pair of random variables

 | S 2 ​ ( 3 K ​ N) = ∑ j = 0 N 1 Z 2, j and S 3 ​ ( N) = ∑ j = 0 N 2 Z 3, j S_{2}(3^{K}N)=\sum_{j=0}^{N_{1}}Z_{2,j}\quad\mbox{and}\quad S_{3}(N)=\sum_{j=0}^{N_{2}}Z_{3,j} |  |

and also the trucated versions

 | S ~ 2 ​ ( 3 K ​ N) = ∑ N 1 η ≤ j ≤ N 1 − N 1 η Z 2, j and S ~ 3 ​ ( N) = ∑ N 2 η ≤ j ≤ N 2 − N 2 η Z 3, j, \tilde{S}_{2}(3^{K}N)=\sum_{N_{1}^{\eta}\leq j\leq N_{1}-N_{1}^{\eta}}Z_{2,j}\quad\mbox{and}\quad\tilde{S}_{3}(N)=\sum_{N_{2}^{\eta}\leq j\leq N_{2}-N_{2}^{\eta}}Z_{3,j}, |  |

Recall that N 1 = ⌊ log 2 ⁡ ( 3 K ​ N) ⌋ N_{1}=\lfloor\log_{2}(3^{K}N)\rfloor and N 2 = ⌊ log 3 ⁡ N ⌋ N_{2}=\lfloor\log_{3}N\rfloor and that 0 < η < 1 2 0<\eta<\frac{1}{2}. We also set

 | N ~ 1 = | { j: N 1 η ≤ j ≤ N 1 − N 1 η } | = N 1 − 2 ​ N 1 η + O ⁡ ( 1) \tilde{N}_{1}=|\{j:N_{1}^{\eta}\leq j\leq N_{1}-N_{1}^{\eta}\}|=N_{1}-2N_{1}^{\eta}+O(1) |  |

and

 | N ~ 2 = | { j: N 2 η ≤ j ≤ N 2 − N 2 η } | = N 2 − 2 ​ N 2 η + O ⁡ ( 1). \tilde{N}_{2}=|\{j:N_{2}^{\eta}\leq j\leq N_{2}-N_{2}^{\eta}\}|=N_{2}-2N_{2}^{\eta}+O(1). |  |

Clearly

 | | S 2 ​ ( 3 K ​ N) − S ~ 2 ​ ( 3 K ​ N) | ≪ ( log ⁡ N) η and | S 3 ​ ( N) − S ~ 3 ​ ( K ​ N) | ≪ ( log ⁡ N) η. \left|S_{2}(3^{K}N)-\tilde{S}_{2}(3^{K}N)\right|\ll(\log N)^{\eta}\quad\mbox{and}\quad\left|S_{3}(N)-\tilde{S}_{3}(KN)\right|\ll(\log N)^{\eta}. |  |

The normalized versions

 | ( Y 1, 3 K ​ N, Y 2, N) = ( S 2 ​ ( 3 K ​ N) − 1 2 ​ N 1 1 4 ​ log 2 ⁡ ( 3 K ​ N), S 3 ​ ( N) − N 2 2 3 ​ log 3 ​ ( N)) (Y_{1,3^{K}N},Y_{2,N})=\left(\frac{S_{2}(3^{K}N)-\frac{1}{2}N_{1}}{\sqrt{\frac{1}{4}\log_{2}(3^{K}N)}},\frac{S_{3}(N)-N_{2}}{\sqrt{\frac{2}{3}\log_{3}(N)}}\right) |  |

and

 | ( Y ~ 1, 3 K ​ N, Y ~ 2, N) = ( S ~ 2 ​ ( 3 K ​ N) − 1 2 ​ N ~ 1 1 4 ​ log 2 ⁡ ( 3 K ​ N), S ~ 3 ​ ( N) − N ~ 2 2 3 ​ log 3 ​ ( N)) (\tilde{Y}_{1,3^{K}N},\tilde{Y}_{2,N})=\left(\frac{\tilde{S}_{2}(3^{K}N)-\frac{1}{2}\tilde{N}_{1}}{\sqrt{\frac{1}{4}\log_{2}(3^{K}N)}},\frac{\tilde{S}_{3}(N)-\tilde{N}_{2}}{\sqrt{\frac{2}{3}\log_{3}(N)}}\right) |  |

converge then to the two-dimensional normal distribution N ⁡ ( 𝟎, 𝐈) N({\bf 0},{\bf I}), where 𝐈 {\bf I} denotes the identity matrix. In particular the characteristic functions converge:

 | lim N → ∞ 𝔼 ( e i ​ t 1 ​ Y 1, 3 K ​ N + i ​ t 2 ​ Y 2, N) → e − t 1 2 / 2 − t 2 2 / 2 \lim_{N\to\infty}\mathbb{E}\left(e^{it_{1}Y_{1,3^{K}N}+it_{2}Y_{2,N}}\right)\to e^{-t_{1}^{2}/2-t_{2}^{2}/2} |  |

and

 | lim N → ∞ 𝔼 ( e i ​ t 1 ​ Y ~ 1, 3 K ​ N + i ​ t 2 ​ Y ~ 2, N) → e − t 1 2 / 2 − t 2 2 / 2. \lim_{N\to\infty}\mathbb{E}\left(e^{it_{1}\tilde{Y}_{1,3^{K}N}+it_{2}\tilde{Y}_{2,N}}\right)\to e^{-t_{1}^{2}/2-t_{2}^{2}/2}. |  |

Note that the convergence is uniform for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N. Furthermore, we have convergence of all (joint) moments:

(5.10) |  | lim N → ∞ 𝔼 ⁡ [Y ~ 1, 3 K ​ N d 1 ​ Y ~ 2, N d 2] → μ d 1 ​ μ d 2, \lim_{N\to\infty}\mathbb{E}\left[\tilde{Y}_{1,3^{K}N}^{d_{1}}\tilde{Y}_{2,N}^{d_{2}}\right]\to\mu_{d_{1}}\mu_{d_{2}}, |  |

where μ d = ( d − 1)!! \mu_{d}=(d-1)!! for even d d and μ d = 0 \mu_{d}=0 for odd d d denote the moments of the standard normal distribution. Again the convergence is uniform for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N. These are standard exercises for sums of independent random variables.

Next let D 2, j, K, N D_{2,j,K,N} denote the (random) j j -th digit in the binary expansion of 3 K ​ n 3^{K}n and D 3, j, N D_{3,j,N} the (random) j j -th digit in the ternary expansion of n n (again) if n < N n<N with n ≡ i mod 2 n\equiv i\bmod 2 is chosen uniformly at random. Then the sum-of-digits functions

 | s 2 ​ ( 3 K ​ n) = ∑ j = 0 N 1 D 2, j, K, N and s 3 ​ ( n) = ∑ j = 0 N 2 D 3, j, N s_{2}(3^{K}n)=\sum_{j=0}^{N_{1}}D_{2,j,K,N}\quad\mbox{and}\quad s_{3}(n)=\sum_{j=0}^{N_{2}}D_{3,j,N} |  |

model the random pair ( s 2 ​ ( 3 K ​ N), s 3 ​ ( n)) (s_{2}(3^{K}N),s_{3}(n)) if n < N n<N with n ≡ i mod 2 n\equiv i\bmod 2 is chosen uniformly at random. Again we also consider the truncated versions

 | s ~ 2 ​ ( 3 K ​ n) = ∑ N 1 η ≤ j ≤ N 1 − N 1 η D 2, j, K, N and s ~ 3 ​ ( n) = ∑ N 2 ≤ j ≤ N 2 − N 2 η D 3, j, N. \tilde{s}_{2}(3^{K}n)=\sum_{N_{1}^{\eta}\leq j\leq N_{1}-N_{1}^{\eta}}D_{2,j,K,N}\quad\mbox{and}\quad\tilde{s}_{3}(n)=\sum_{N_{2}\leq j\leq N_{2}-N_{2}^{\eta}}D_{3,j,N}. |  |

and the normalized versions:

 | ( X 1, 3 K ​ N, X 2, N) = ( s 2 ​ ( 3 K ​ N) − 1 2 ​ N 1 1 4 ​ log 2 ⁡ ( 3 K ​ N), s 3 ​ ( N) − N 2 2 3 ​ log 3 ​ ( N)) (X_{1,3^{K}N},X_{2,N})=\left(\frac{s_{2}(3^{K}N)-\frac{1}{2}N_{1}}{\sqrt{\frac{1}{4}\log_{2}(3^{K}N)}},\frac{s_{3}(N)-N_{2}}{\sqrt{\frac{2}{3}\log_{3}(N)}}\right) |  |

and

 | ( X ~ 1, 3 K ​ N, X ~ 2, N) = ( s ~ 2 ​ ( 3 K ​ N) − 1 2 ​ N ~ 1 1 4 ​ log 2 ⁡ ( 3 K ​ N), s ~ 3 ​ ( N) − N ~ 2 2 3 ​ log 3 ​ ( N)). (\tilde{X}_{1,3^{K}N},\tilde{X}_{2,N})=\left(\frac{\tilde{s}_{2}(3^{K}N)-\frac{1}{2}\tilde{N}_{1}}{\sqrt{\frac{1}{4}\log_{2}(3^{K}N)}},\frac{\tilde{s}_{3}(N)-\tilde{N}_{2}}{\sqrt{\frac{2}{3}\log_{3}(N)}}\right). |  |

###### Lemma 5.3.

For every pair of non-negative integers d 1, d 2 d_{1},d_{2} and i ∈ { 0, 1 } i\in\{0,1\} we have

 | lim N → ∞ 2 N ​ ∑ n < N, n ≡ i mod 2 ( s ~ 2 ​ ( 3 K ​ n) − 1 2 ​ N ~ 1 1 4 ​ log 2 ⁡ ( 3 K ​ N)) d 1 ​ ( s ~ 3 ​ ( n) − N ~ 2 2 3 ​ log 3 ​ ( N)) d 2 = μ d 1 ​ μ d 2 \lim_{N\to\infty}\frac{2}{N}\sum_{n<N,\,n\equiv i\bmod 2}\left(\frac{\tilde{s}_{2}(3^{K}n)-\frac{1}{2}\tilde{N}_{1}}{\sqrt{\frac{1}{4}\log_{2}(3^{K}N)}}\right)^{d_{1}}\left(\frac{\tilde{s}_{3}(n)-\tilde{N}_{2}}{\sqrt{\frac{2}{3}\log_{3}(N)}}\right)^{d_{2}}=\mu_{d_{1}}\mu_{d_{2}} |  |

uniformly for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N.

###### Proof.

We rewrite the sum-of-digits function

 | s ~ 2 ​ ( 3 K ​ n) \displaystyle\tilde{s}_{2}(3^{K}n) | = ∑ N 1 η ≤ j ≤ N 1 − N 1 η ε 2, j ​ ( 3 K ​ n) = ∑ N 1 η ≤ j ≤ N 1 − N 1 η D 2, j, K, N, \displaystyle=\sum_{N_{1}^{\eta}\leq j\leq N_{1}-N_{1}^{\eta}}\varepsilon_{2,j}(3^{K}n)=\sum_{N_{1}^{\eta}\leq j\leq N_{1}-N_{1}^{\eta}}D_{2,j,K,N}, |  |

 | s ~ 3 ​ ( n) \displaystyle\tilde{s}_{3}(n) | = ∑ N 2 η ≤ j ≤ N 2 − N 2 η ε 3, j ​ ( 3 K ​ n) = ∑ N 2 η ≤ j ≤ N 2 − N 2 η D 3, j, N \displaystyle=\sum_{N_{2}^{\eta}\leq j\leq N_{2}-N_{2}^{\eta}}\varepsilon_{3,j}(3^{K}n)=\sum_{N_{2}^{\eta}\leq j\leq N_{2}-N_{2}^{\eta}}D_{3,j,N} |  |

and expand the moments

 | 2 N ​ ∑ n < N, n ≡ i mod 2 ( s ~ 2 ​ ( 3 K ​ n) − 1 2 ​ N ~ 1) d 1 ​ ( s ~ 3 ​ ( n) − N ~ 2) d 2 \frac{2}{N}\sum_{n<N,\,n\equiv i\bmod 2}\left(\tilde{s}_{2}(3^{K}n)-\frac{1}{2}\tilde{N}_{1}\right)^{d_{1}}\left(\tilde{s}_{3}(n)-\tilde{N}_{2}\right)^{d_{2}} |  |

in OPEN N ~ 1 d 1 ​ N ~ 2 d 2 = O ⁡ ( ( log ⁡ N) d 1 + d 2)) \tilde{N}_{1}^{d_{1}}\tilde{N}_{2}^{d_{2}}=O((\log N)^{d_{1}+d_{2}})) terms of

 | 2 N #{ n < N, n ≡ i mod 2: ε 2, k j 1 ( 3 K n) = b j 1, 1 ≤ j 1 ≤ d 1 ′, ε 3, ℓ j 2 ( n) = c j 2, 1 ≤ j 2 ≤ d 2 ′ }. \frac{2}{N}\#\left\{n<N,\,n\equiv i\bmod 2\,:\,\varepsilon_{2,k_{j_{1}}}(3^{K}n)=b_{j_{1}},\,1\leq j_{1}\leq d_{1}^{\prime},\,\varepsilon_{3,\ell_{j_{2}}}(n)=c_{j_{2}},\,1\leq j_{2}\leq d_{2}^{\prime}\right\}. |  |

with 0 ≤ d 1 ′ ≤ d 1 0\leq d_{1}^{\prime}\leq d_{1}, 0 ≤ d 2 ′ ≤ d 2 0\leq d_{2}^{\prime}\leq d_{2} and powers of N ~ 1 \tilde{N}_{1} and N ~ 2 \tilde{N}_{2}. By Lemma 5.1 we can replace these numbers by 2 − d 1 ′ ​ 3 − d 2 ′ + O ⁡ ( ( log ⁡ N) − λ) 2^{-d_{1}^{\prime}}3^{-d_{2}^{\prime}}+O((\log N)^{-\lambda}) uniformly for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N, where we choose λ > 2 ​ ( d 1 + d 2) \lambda>2(d_{1}+d_{2}). Clearly the resulting sum equals

 | 𝔼 ⁡ [( S ~ 2 ​ ( 3 K ​ N) − 1 2 ​ N ~ 1) d 1 ​ ( S ~ 3 ​ ( N) − N ~ 2) d 2] + O ⁡ ( ( log ⁡ N) 2 ​ ( d 1 + d 2) − λ). \mathbb{E}\left[\left(\tilde{S}_{2}(3^{K}N)-\frac{1}{2}\tilde{N}_{1}\right)^{d_{1}}\left(\tilde{S}_{3}(N)-\tilde{N}_{2}\right)^{d_{2}}\right]+O\left((\log N)^{2(d_{1}+d_{2})-\lambda}\right). |  |

Finally by dividing the resulting equation by

 | ( 1 4 ​ log 2 ⁡ ( 3 K ​ N)) d 1 2 ​ ( 2 3 ​ log 3 ⁡ ( N)) d 2 2 \left(\frac{1}{4}\log_{2}(3^{K}N)\right)^{\frac{d_{1}}{2}}\left(\frac{2}{3}\log_{3}(N)\right)^{\frac{d_{2}}{2}} |  |

and by using the relation ( 5.10) we complete the proof of the lemma. ∎

Lemma 5.3 directly implies that the truncated and normalized pair of random variables

 | ( X ~ 1, 3 K ​ N, X ~ 2, N) (\tilde{X}_{1,3^{K}N},\tilde{X}_{2,N}) |  |

converges weakly to the 2 2 -dimensional normal distribution N ⁡ ( 𝟎, 𝐈) N({\bf 0},{\bf I}). Since η < 1 2 \eta<\frac{1}{2} the same holds for the untruncated pair

 | ( X 1, 3 K ​ N, X 2, N). (X_{1,3^{K}N},X_{2,N}). |  |

Hence, we also have for the characteristic function

(5.11) |  | lim N → ∞ 𝔼 ( e i ​ t 1 ​ X 1, 3 K ​ N + i ​ t 2 ​ X 2, N) → e − t 1 2 / 2 − t 2 2 / 2. \lim_{N\to\infty}\mathbb{E}\left(e^{it_{1}X_{1,3^{K}N}+it_{2}X_{2,N}}\right)\to e^{-t_{1}^{2}/2-t_{2}^{2}/2}. |  |

More precisely by using the Taylor expansion for e i ​ t e^{it} convergence of moments and in particular the uniformity for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N can be directly transformed in uniform convergence for the characteristic function. Thus, ( 5.11) holds uniformly for 0 ≤ K ≤ c 2 ​ log ⁡ N 0\leq K\leq c_{2}\log N

By rewriting ( 5.11) in terms of the sum-of-digits functions this is precisely (the first part of) Proposition 1.2.

As mentioned already several times, the second part of Proposition 1.2 follows very similarly. This completes the proof of Proposition 1.2.

## References

- [1] B. Adamczewski and C. Faverjon, Mahler’s method in several variables and finite automata, 2020. Preprint, [https://arxiv.org/abs/2012.08283][3].
- [2] N. L. Bassily and I. Kátai, Distribution of the values of q q -additive functions on polynomial sequences, Acta Math. Hungar., 68 (1995), pp. 353–361. [https://doi.org/10.1007/BF01874349][4].
- [3] R. de la Bretèche, T. Stoll, and G. Tenenbaum, Somme des chiffres et changement de base, Ann. Inst. Fourier, 69 (2019), pp. 2507–2518. [https://doi.org/10.5802/aif.3300][5].
- [4] J.-M. Deshouillers, A footnote to the least non zero digit of n n! in base 12 12, Unif. Distrib. Theory, 7 (2012), pp. 71–73. [https://doi.org/][6].
- [5], Yet another footnote to the least non zero digit of n! n! in base 12, Unif. Distrib. Theory, 11 (2016), pp. 163–167. [https://doi.org/10.1515/udt-2016-0018][7].
- [6] J.-M. Deshouillers, L. Habsieger, S. Laishram, and B. Landreau, Sums of the digits in bases 2 2 and 3 3, in Number theory — Diophantine problems, uniform distribution and applications, Springer, 2017, pp. 211–217. [https://doi.org/10.1007/978-3-319-55357-3_9][8].
- [7] J.-M. Deshouillers, P. Jelinek, and L. Spiegelhofer, Binary-ternary collisions and the last significant digit of n! n! in base 12, 2024. Preprint, [https://arxiv.org/abs/2412.09124][9].
- [8] J.-M. Deshouillers and I. Z. Ruzsa, The least nonzero digit of n! n! in base 12, Publ. Math. Debrecen, 79 (2011), pp. 395–400. [https://doi.org/10.5486/PMD.2011.5169][10].
- [9] M. Drmota, The joint distribution of q q -additive functions, Acta Arith., 100 (2001), pp. 17–39. [https://doi.org/10.4064/aa100-1-2][11].
- [10] M. Drmota and J. Gajdosik, The distribution of the sum-of-digits function, J. Théor. Nombres Bordeaux, 10 (1998), pp. 17–32. [https://doi.org/10.5802/jtnb.216][12].
- [11] M. Drmota and C. Krattenthaler, A joint central limit theorem for the sum-of-digits function, and asymptotic divisibility of Catalan-like sequences, Proc. Am. Math. Soc., 147 (2019), pp. 4123–4133. [https://doi.org/10.1090/proc/14349][13].
- [12] M. Drmota, C. Mauduit, and J. Rivat, Normality along squares, J. Eur. Math. Soc. (JEMS), 21 (2019), pp. 507–548. [https://doi.org/10.4171/JEMS/843][14].
- [13] M. Drmota, C. Mauduit, and J. Rivat, Prime numbers in two bases, Duke Math. J., 169 (2020), pp. 1809–1876. [https://doi.org/10.1215/00127094-2019-0083][15].
- [14] M. Drmota, C. Müllner, and L. Spiegelhofer, Primes as sums of Fibonacci numbers, 2022. 135 pages. Accepted for publication in Mem. Amer. Math. Soc., see [https://www.ams.org/cgi-bin/mstrack/accepted_papers/memo][16].
- [15] J.-H. Evertse, The Subspace Theorem of W. M. Schmidt, in Diophantine approximation and abelian varieties. Introductory lectures. Papers of the conference, held in Soesterberg, Netherlands, April 12-16, 1992, Berlin: Springer-Verlag, 1993, pp. 31–50.
- [16] H. Furstenberg, Intersections of Cantor sets and transversality of semi-groups. Probl. Analysis, Sympos. in Honor of Salomon Bochner, Princeton Univ. 1969, 41-59 (1970)., 1970.
- [17] M. Z. Garaev, F. Luca, and I. E. Shparlinski, Catalan and Apéry numbers in residue classes, J. Combin. Theory Ser. A, 113 (2006), pp. 851–865. [https://doi.org/10.1016/j.jcta.2005.08.003][17].
- [18] I. Kátai, Distribution of q q -additive function, in Probability theory and applications, vol. 80 of Math. Appl., Kluwer Acad. Publ., Dordrecht, 1992, pp. 309–318.
- [19] C. Mauduit and J. Rivat, La somme des chiffres des carrés, Acta Math., 203 (2009), pp. 107–148. [https://doi.org/10.1007/s11511-009-0040-0][18].
- [20], Sur un problème de Gelfond: la somme des chiffres des nombres premiers, Ann. of Math. (2), 171 (2010), pp. 1591–1646. [https://doi.org/10.4007/annals.2010.171.1591][19].
- [21] C. Müllner and L. Spiegelhofer, Normality of the Thue–Morse sequence along Piatetski-Shapiro sequences, II, Israel J. Math., 220 (2017), pp. 691–738. [https://doi.org/10.1007/s11856-017-1531-x][20].
- [22] H. G. Senge and E. G. Straus, PV-numbers and sets of multiplicity, Period. Math. Hung., 3 (1973), pp. 93–100. [https://doi.org/10.1007/BF02018464][21].
- [23] P. Shmerkin, On Furstenberg’s intersection conjecture, self-similar measures, and the L q L^{q} norms of convolutions, Ann. Math. (2), 189 (2019), pp. 319–391. [https://doi.org/10.4007/annals.2019.189.2.1][22].
- [24] L. Spiegelhofer, Normality of the Thue-Morse sequence along Piatetski-Shapiro sequences, Q. J. Math., 66 (2015), pp. 1127–1138. [https://doi.org/10.1093/qmath/hav029][23].
- [25], The level of distribution of the Thue–Morse sequence, Compos. Math., 156 (2020), pp. 2560–2587. [https://doi.org/10.1112/s0010437x20007563][24].
- [26], A lower bound for Cusick’s conjecture on the digits of n + t n+t, Math. Proc. Cambridge Philos. Soc., 172 (2022), pp. 139–161. [https://doi.org/10.1017/S0305004121000153][25]
- [27], Collisions of digit sums in bases 2 and 3, Israel J. Math., 258 (2023), pp. 475–502. [https://doi.org/10.1007/s11856-023-2478-8][26].
- [28], Thue–Morse along the sequence of cubes, 2023. Preprint, [https://arxiv.org/abs/2308.09498][27].
- [29] L. Spiegelhofer and M. Wallner, The binary digits of n + t n+t, Ann. Sc. Norm. Super. Pisa, Cl. Sci. (5), 24 (2023), pp. 1–31. [https://doi.org/10.2422/2036-2145.202105_069][28].
- [30] P. K. Stockmeyer, Of camels, inheritance, and unit fractions, Math Horiz., 21 (2013), pp. 8–11.
- [31] M. Waldschmidt, Minorations de combinaisons linéaires de logarithmes de nombres algébriques, Canad. J. Math., 45 (1993), pp. 176–224. [https://doi.org/10.4153/CJM-1993-010-1][29].
- [32] M. Wu, A proof of Furstenberg’s conjecture on the intersections of × p \times p - and × q \times q -invariant sets, Ann. Math. (2), 189 (2019), pp. 707–751. [https://doi.org/10.4007/annals.2019.189.3.2][30].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/pdf/2012.08283
[4]: https://doi.org/10.1007/BF01874349
[5]: https://doi.org/10.5802/aif.3300
[6]: https://doi.org/
[7]: https://doi.org/10.1515/udt-2016-0018
[8]: https://doi.org/10.1007/978-3-319-55357-3_9
[9]: https://arxiv.org/pdf/2412.09124
[10]: https://doi.org/10.5486/PMD.2011.5169
[11]: https://doi.org/10.4064/aa100-1-2
[12]: https://doi.org/10.5802/jtnb.216
[13]: https://doi.org/10.1090/proc/14349
[14]: https://doi.org/10.4171/JEMS/843
[15]: https://doi.org/10.1215/00127094-2019-0083
[16]: https://www.ams.org/cgi-bin/mstrack/accepted_papers/memo
[17]: https://doi.org/10.1016/j.jcta.2005.08.003
[18]: https://doi.org/10.1007/s11511-009-0040-0
[19]: https://doi.org/10.4007/annals.2010.171.1591
[20]: https://doi.org/10.1007/s11856-017-1531-x
[21]: https://doi.org/10.1007/BF02018464
[22]: https://doi.org/10.4007/annals.2019.189.2.1
[23]: https://doi.org/10.1093/qmath/hav029
[24]: https://doi.org/10.1112/s0010437x20007563
[25]: https://doi.org/10.1017/S0305004121000153
[26]: https://doi.org/10.1007/s11856-023-2478-8
[27]: https://arxiv.org/pdf/2308.09498
[28]: https://doi.org/10.2422/2036-2145.202105_069
[29]: https://doi.org/10.4153/CJM-1993-010-1
[30]: https://doi.org/10.4007/annals.2019.189.3.2
