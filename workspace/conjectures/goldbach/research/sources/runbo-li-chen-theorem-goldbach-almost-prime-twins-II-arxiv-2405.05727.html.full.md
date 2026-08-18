<!-- source: https://arxiv.org/html/2405.05727v4 | converted from HTML -->

On Chen’s theorem, Goldbach’s conjecture and almost prime twins II

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-SA 4.0][2]

arXiv:2405.05727v4 [math.NT] 31 May 2025

# On Chen’s theorem, Goldbach’s conjecture and almost prime twins II

Runbo Li Address: International Curriculum Center, The High School Affiliated to Renmin University of China, Beijing, China Email address: [runbo.li.carey@gmail.com][3]

###### Abstract.

Let N N denote a sufficiently large even integer and x x denote a sufficiently large integer, we define D 1, 2 ​ ( N) D_{1,2}(N) as the number of primes p p that such that N − p N-p has at most 2 prime factors. In this paper, we show that D 1, 2 ​ ( N) ⩾ 1.9728 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 D_{1,2}(N)\geqslant 1.9728\frac{C(N)N}{(\log N)^{2}}, which is rather near to the asymptotic constant 2 2 in Hardy–Littlewood conjecture for Goldbach’s conjecture. We also get similar results on twin prime problem and additive representations of integers. The proof combines various techniques in sieve methods, such as weighted sieve, Chen’s switching principle, new distribution levels proved by Lichtman and Pascadi, Chen’s double sieve and Harman’s sieve.

###### Key words and phrases:

Chen’s theorem, Sieve, Distribution level

###### 2020 Mathematics Subject Classification

11N35, 11N36, 11P32

## 1. Introduction

One of the most famous open problem in number theory is the Goldbach’s conjecture, which states that any even integers can be written as the sum of two primes. Since the original conjecture is so hard, mathematicians try to consider the problem of writing a large even integer as a sum of a prime and a number with few prime factors. Let N N denote a sufficiently large even integer, p p denote a prime, and P r P_{r} denote an integer with at most r r prime factors counted with multiplicity. We define

 | D 1, 2 ( N) = | { p: p ⩽ N, N − p = P 2 } |. D_{1,2}(N)=\left|\left\{p:p\leqslant N,N-p=P_{2}\right\}\right|. |  | (1) |

In 1973 Chen [5] established his remarkable Chen’s theorem:

 | D 1, 2 ​ ( N) ⩾ 0.67 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, D_{1,2}(N)\geqslant 0.67\frac{C(N)N}{(\log N)^{2}}, |  | (2) |

where

 | C ⁡ ( N) = ∏ p | N p > 2 p − 1 p − 2 ​ ∏ p > 2 ( 1 − 1 ( p − 1) 2). C(N)=\prod_{\begin{subarray}{c}p\mid N\\ p>2\end{subarray}}\frac{p-1}{p-2}\prod_{p>2}\left(1-\frac{1}{(p-1)^{2}}\right). |  | (3) |

Chen’s constant 0.67 was improved successively to

 | 0.689, 0.7544, 0.81, 0.8285, 0.836, 0.867, 0.899 0.689,\ 0.7544,\ 0.81,\ 0.8285,\ 0.836,\ 0.867,\ 0.899 |  |

by Halberstam and Richert [11] [10], Chen [7] [6], Cai and Lu [4], Wu [21], Cai [2] and Wu [22] respectively. Chen [8] announced a better constant 0.9, but this work has not been published.

In our 2024 preprint [13], we increase this constant to 1.733 1.733, which almost doubles Wu’s 0.899 0.899. In the proof we use the distribution levels of Lichtman (see [15], and [16] for an earlier development of this kind of results) and complicated techniques in sieves. In this paper, by modifying the parameters used in [13] and inserting more advanced techniques, we obtain the following sharper result.

###### Theorem 1.1.

 | D 1, 2 ​ ( N) ⩾ 1.9728 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. D_{1,2}(N)\geqslant 1.9728\frac{C(N)N}{(\log N)^{2}}. |  |

Our new constant 1.9728 1.9728 gives a 13.8 % 13.8\% improvement over our previous result 1.733 1.733 and a 119 % 119\% refinement of Wu’s prior record 0.899 0.899. An important meaning of our new constant is that it is very close to the conjectured asymptotic constant 2 2 for D 1, 1 ​ ( N) D_{1,1}(N), the number of primes p p such that N − p N-p is also a prime.

Furthermore, for two relatively prime square-free positive integers a, b a,b, let M M denote a sufficiently large integer that is relatively prime to both a a and b b, a, b < M ε a,b<M^{\varepsilon} and let M M be even if a a and b b are both odd. Let R a, b ​ ( M) R_{a,b}(M) denote the number of primes p p such that a ​ p ap and M − a ​ p M-ap are both square-free, b | ( M − a ​ p) b\mid(M-ap), and M − a ​ p b = P 2 \frac{M-ap}{b}=P_{2}. In 1976, Ross [[19], Chapter 3] established that

 | R a, b ​ ( M) ⩾ 0.608 ​ C ⁡ ( a ​ b ​ M) ​ M a ​ b ​ ( log ⁡ M) 2, R_{a,b}(M)\geqslant 0.608\frac{C(abM)M}{ab(\log M)^{2}}, |  | (4) |

and in [13] the constant 0.608 0.608 was improved successively to 1.733 1.733 by essentially the same process. Now by using the new sieve process and methods in [14], we have the following sharper.

###### Theorem 1.2.

 | R a, b ​ ( M) ⩾ 1.9728 ​ C ⁡ ( a ​ b ​ M) ​ M a ​ b ​ ( log ⁡ M) 2. R_{a,b}(M)\geqslant 1.9728\frac{C(abM)M}{ab(\log M)^{2}}. |  |

Another famous problem in number theory is the twin prime problem, which states that there are infinitely many prime pairs differ by 2 2. Again, mathematicians consider the problem that there are infinitely many prime p p such that p + 2 p+2 has few prime factors. For the twin prime problem, let x x denote a sufficiently large integer and define

 | π 1, 2 ( x) = | { p: p ⩽ x, p + 2 = P 2 } |. \pi_{1,2}(x)=\left|\left\{p:p\leqslant x,p+2=P_{2}\right\}\right|. |  | (5) |

In 1973 Chen [5] showed simultaneously that

 | π 1, 2 ​ ( x) ⩾ 0.335 ​ C 2 ​ x ( log ⁡ x) 2, \pi_{1,2}(x)\geqslant 0.335\frac{C_{2}x}{(\log x)^{2}}, |  | (6) |

where

 | C 2 = 2 ​ ∏ p > 2 ( 1 − 1 ( p − 1) 2), C_{2}=2\prod_{p>2}\left(1-\frac{1}{(p-1)^{2}}\right), |  | (7) |

and the constant 0.608 was improved successively to

 | 0.3445, 0.3772, 0.405, 0.71, 1.015, 1.05, 1.0974, 1.104, 1.123, 1.13 0.3445,\ 0.3772,\ 0.405,\ 0.71,\ 1.015,\ 1.05,\ 1.0974,\ 1.104,\ 1.123,\ 1.13 |  |

by Halberstam [10], Chen [7] [6], Fouvry and Grupp [9], Liu [17], Wu [20], Cai [1], Wu [21], Cai [2] and Cai [3] respectively.

In [13] we increase this constant to 1.238 1.238 by similar methods. Recently, Pascadi [18] got a powerful new distribution level for primes, which is quite helpful in improving the lower bound for π 1, 2 ​ ( x) \pi_{1,2}(x). Using his new distribution results together with sieve inputs in [13], we get the following sharper.

###### Theorem 1.3.

 | π 1, 2 ​ ( x) ⩾ 1.2759 ​ C 2 ​ x ( log ⁡ x) 2. \pi_{1,2}(x)\geqslant 1.2759\frac{C_{2}x}{(\log x)^{2}}. |  |

## 2. New distribution levels

In this section we put A, B > 0 A,B>0, θ 0 = 0 \theta_{0}=0, θ 1 = 7 32 \theta_{1}=\frac{7}{32} from Kim–Sarnak [12], and we define the functions ϑ α ​ ( t 1) \boldsymbol{\vartheta}_{\alpha}(t_{1}) and ϑ α ​ ( t 1, t 2, t 3) \boldsymbol{\vartheta}_{\alpha}(t_{1},t_{2},t_{3}) with α = 0 ​ or ​ 1 \alpha=0\text{ or }1 similar to those in [15], but with θ = θ α \theta=\theta_{\alpha} here for ϑ α \boldsymbol{\vartheta}_{\alpha}. We consider the analogous set of well–factorable vectors 𝐃 r w ​ e ​ l ​ l \mathbf{D}_{r}^{well}:

 | 𝐃 r w ​ e ​ l ​ l ( D) = { ( D 1, …, D r): D 1 ⋯ D m − 1 D m 2 < D for all m ⩽ r }. \mathbf{D}_{r}^{well}(D)=\left\{\left(D_{1},\ldots,D_{r}\right):D_{1}\cdots D_{m-1}D_{m}^{2}<D\ \text{for all }m\leqslant r\right\}. |  | (8) |

We shall first state the distribution results for Theorem 1.1, which were proved in [15]. We remark that the maximum possible distribution level here is 19101 32000 ≈ 0.5969 \frac{19101}{32000}\approx 0.5969. The first one is used when Chen’s switching principle is not used, and the second one is used when Chen’s switching principle is used.

###### Lemma 2.1.

Let ( D 1, …, D r) ∈ 𝐃 r well ​ ( D) \left(D_{1},\ldots,D_{r}\right)\in\mathbf{D}_{r}^{\text{well}}(D) and write D = N ϑ, D i = N t i D=N^{\boldsymbol{\vartheta}},D_{i}=N^{t_{i}} for i ⩽ r i\leqslant r. If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon, then

 | ∑ b = p 1 ⋯ p r D i < p i ⩽ D i 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( p r) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( N, q, N) − π ⁡ ( N) φ ⁡ ( q)) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}\cdots p_{r}\\ D_{i}<p_{i}\leqslant D_{i}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(p_{r}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(N;q,N)-\frac{\pi(N)}{\varphi(q)}\right)\ll\frac{N}{(\log N)^{A}}. |  | (i) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4} and r ⩾ 3 r\geqslant 3, then (i) holds if ϑ ⩽ ϑ 1 ​ ( t 1, t 2, t 3) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-\varepsilon.

If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon and r = 2 r=2, then

 | ∑ b = p 1 ​ p 2 D 1 < p 1 ⩽ D 1 1 + ε 9 D 2 < p 2 ⩽ D 2 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( N u) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( N, q, N) − π ⁡ ( N) φ ⁡ ( q)) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}p_{2}\\ D_{1}<p_{1}\leqslant D_{1}^{1+\varepsilon^{9}}\\ D_{2}<p_{2}\leqslant D_{2}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(N^{u}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(N;q,N)-\frac{\pi(N)}{\varphi(q)}\right)\ll\frac{N}{(\log N)^{A}}. |  | (ii) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4}, then (ii) holds if ϑ ⩽ ϑ 1 ​ ( t 1, t 2, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},t_{2},u)-\varepsilon.

If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon and r = 1 r=1, then

 | ∑ b = p 1 D 1 < p 1 ⩽ D 1 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( N u) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( N, q, N) − π ⁡ ( N) φ ⁡ ( q)) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}\\ D_{1}<p_{1}\leqslant D_{1}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(N^{u}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(N;q,N)-\frac{\pi(N)}{\varphi(q)}\right)\ll\frac{N}{(\log N)^{A}}. |  | (iii) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4}, then (iii) holds if ϑ ⩽ ϑ 1 ​ ( t 1, u, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},u,u)-\varepsilon.

If r = 0 r=0 and u = 1 500 u=\frac{1}{500}, this simplifies as

 | ∑ q ⩽ N 19101 32000 q | P ⁡ ( N 1 / 500) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( N, q, N) − π ⁡ ( N) φ ⁡ ( q)) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}q\leqslant N^{\frac{19101}{32000}}\\ q\mid P\left(N^{1/500}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(N;q,N)-\frac{\pi(N)}{\varphi(q)}\right)\ll\frac{N}{(\log N)^{A}}. |  |

###### Lemma 2.2.

Let ( D 1, …, D r) ∈ 𝐃 r well ​ ( D) \left(D_{1},\ldots,D_{r}\right)\in\mathbf{D}_{r}^{\text{well}}(D) and write D = N ϑ, D i = N t i D=N^{\boldsymbol{\vartheta}},D_{i}=N^{t_{i}} for i ⩽ r i\leqslant r. Let ε > 0 \varepsilon>0 and real numbers ε 1, …, ε k ⩾ ε \varepsilon_{1},\ldots,\varepsilon_{k}\geqslant\varepsilon such that ∑ i ⩽ k ε i = 1 \sum_{i\leqslant k}\varepsilon_{i}=1, and let Δ = 1 + ( log ⁡ N) − B \Delta=1+(\log N)^{-B}. If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon, then

 | ∑ b = p 1 ′ ⋯ p r ′ D i < p i ′ ⩽ D i 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( p r ′) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ N ( mod q) N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, N) = 1 N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}\cdots p_{r}^{\prime}\\ D_{i}<p_{i}^{\prime}\leqslant D_{i}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(p_{r}^{\prime}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv N(\bmod q)\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},N)=1\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{N}{(\log N)^{A}}. |  | (i) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4} and r ⩾ 3 r\geqslant 3, then (i) holds if ϑ ⩽ ϑ 1 ​ ( t 1, t 2, t 3) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-\varepsilon.

If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon and r = 2 r=2, then

 | ∑ b = p 1 ′ ​ p 2 ′ D 1 < p 1 ′ ⩽ D 1 1 + ε 9 D 2 < p 2 ′ ⩽ D 2 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( N u) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ N ( mod q) N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, N) = 1 N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}p_{2}^{\prime}\\ D_{1}<p_{1}^{\prime}\leqslant D_{1}^{1+\varepsilon^{9}}\\ D_{2}<p_{2}^{\prime}\leqslant D_{2}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(N^{u}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv N(\bmod q)\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},N)=1\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{N}{(\log N)^{A}}. |  | (ii) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4}, then (ii) holds if ϑ ⩽ ϑ 1 ​ ( t 1, t 2, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},t_{2},u)-\varepsilon.

If ϑ ⩽ ϑ 1 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1})-\varepsilon and r = 1 r=1, then

 | ∑ b = p 1 ′ D 1 < p 1 ′ ⩽ D 1 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( N u) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ N ( mod q) N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, N) = 1 N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}\\ D_{1}<p_{1}^{\prime}\leqslant D_{1}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(N^{u}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv N(\bmod q)\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},N)=1\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{N}{(\log N)^{A}}. |  | (iii) |

Moreover if t 1 ⩽ 1 − θ 1 4 t_{1}\leqslant\frac{1-\theta_{1}}{4}, then (iii) holds if ϑ ⩽ ϑ 1 ​ ( t 1, u, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{1}(t_{1},u,u)-\varepsilon.

If r = 0 r=0 and u = 1 500 u=\frac{1}{500}, this simplifies as

 | ∑ q ⩽ N 19101 32000 q | P ⁡ ( N 1 / 500) ( q, N) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ N ( mod q) N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, N) = 1 N ε i / Δ < p i ⩽ N ε i ​ ∀ i ⩽ k 1) ≪ N ( log ⁡ N) A. \sum_{\begin{subarray}{c}q\leqslant N^{\frac{19101}{32000}}\\ q\mid P\left(N^{1/500}\right)\\ (q,N)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv N(\bmod q)\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},N)=1\\ N^{\varepsilon_{i}}/\Delta<p_{i}\leqslant N^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{N}{(\log N)^{A}}. |  |

Next we shall state the distribution results for Theorem 1.3, which were proved in [18]. We remark that the maximum possible distribution level here is 2497 4000 = 0.62425 \frac{2497}{4000}=0.62425. The first one is used when Chen’s switching principle is not used, and the second one is used when Chen’s switching principle is used.

###### Lemma 2.3.

Let ( D 1, …, D r) ∈ 𝐃 r well ​ ( D) \left(D_{1},\ldots,D_{r}\right)\in\mathbf{D}_{r}^{\text{well}}(D) and write D = x ϑ, D i = x t i D=x^{\boldsymbol{\vartheta}},D_{i}=x^{t_{i}} for i ⩽ r i\leqslant r. If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon, then

 | ∑ b = p 1 ⋯ p r D i < p i ⩽ D i 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( p r) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( x, q, − 2) − π ⁡ ( x) φ ⁡ ( q)) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}\cdots p_{r}\\ D_{i}<p_{i}\leqslant D_{i}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(p_{r}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(x;q,-2)-\frac{\pi(x)}{\varphi(q)}\right)\ll\frac{x}{(\log x)^{A}}. |  | (i) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}} and r ⩾ 3 r\geqslant 3, then (i) holds if ϑ ⩽ ϑ 0 ​ ( t 1, t 2, t 3) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-\varepsilon.

If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon and r = 2 r=2, then

 | ∑ b = p 1 ​ p 2 D 1 < p 1 ⩽ D 1 1 + ε 9 D 2 < p 2 ⩽ D 2 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( x u) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( x, q, − 2) − π ⁡ ( x) φ ⁡ ( q)) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}p_{2}\\ D_{1}<p_{1}\leqslant D_{1}^{1+\varepsilon^{9}}\\ D_{2}<p_{2}\leqslant D_{2}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(x^{u}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(x;q,-2)-\frac{\pi(x)}{\varphi(q)}\right)\ll\frac{x}{(\log x)^{A}}. |  | (ii) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}}, then (ii) holds if ϑ ⩽ ϑ 0 ​ ( t 1, t 2, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},t_{2},u)-\varepsilon.

If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon and r = 1 r=1, then

 | ∑ b = p 1 D 1 < p 1 ⩽ D 1 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( x u) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( x, q, − 2) − π ⁡ ( x) φ ⁡ ( q)) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}\\ D_{1}<p_{1}\leqslant D_{1}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(x^{u}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(x;q,-2)-\frac{\pi(x)}{\varphi(q)}\right)\ll\frac{x}{(\log x)^{A}}. |  | (iii) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}}, then (iii) holds if ϑ ⩽ ϑ 0 ​ ( t 1, u, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},u,u)-\varepsilon.

If r = 0 r=0 and u = 1 500 u=\frac{1}{500}, this simplifies as

 | ∑ q ⩽ x 2497 4000 q | P ⁡ ( x 1 / 500) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( π ⁡ ( x, q, − 2) − π ⁡ ( x) φ ⁡ ( q)) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}q\leqslant x^{\frac{2497}{4000}}\\ q\mid P\left(x^{1/500}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\pi(x;q,-2)-\frac{\pi(x)}{\varphi(q)}\right)\ll\frac{x}{(\log x)^{A}}. |  |

###### Lemma 2.4.

Let ( D 1, …, D r) ∈ 𝐃 r well ​ ( D) \left(D_{1},\ldots,D_{r}\right)\in\mathbf{D}_{r}^{\text{well}}(D) and write D = x ϑ, D i = x t i D=x^{\boldsymbol{\vartheta}},D_{i}=x^{t_{i}} for i ⩽ r i\leqslant r. Let ε > 0 \varepsilon>0 and real numbers ε 1, …, ε k ⩾ ε \varepsilon_{1},\ldots,\varepsilon_{k}\geqslant\varepsilon such that ∑ i ⩽ k ε i = 1 \sum_{i\leqslant k}\varepsilon_{i}=1, and let Δ = 1 + ( log ⁡ x) − B \Delta=1+(\log x)^{-B}. If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon, then

 | ∑ b = p 1 ′ ⋯ p r ′ D i < p i ′ ⩽ D i 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( p r ′) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ 2 ( mod q) x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, 2) = 1 x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}\cdots p_{r}^{\prime}\\ D_{i}<p_{i}^{\prime}\leqslant D_{i}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(p_{r}^{\prime}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv 2(\bmod q)\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},2)=1\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{x}{(\log x)^{A}}. |  | (i) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}} and r ⩾ 3 r\geqslant 3, then (i) holds if ϑ ⩽ ϑ 0 ​ ( t 1, t 2, t 3) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-\varepsilon.

If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon and r = 2 r=2, then

 | ∑ b = p 1 ′ ​ p 2 ′ D 1 < p 1 ′ ⩽ D 1 1 + ε 9 D 2 < p 2 ′ ⩽ D 2 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( x u) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ 2 ( mod q) x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, 2) = 1 x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}p_{2}^{\prime}\\ D_{1}<p_{1}^{\prime}\leqslant D_{1}^{1+\varepsilon^{9}}\\ D_{2}<p_{2}^{\prime}\leqslant D_{2}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(x^{u}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv 2(\bmod q)\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},2)=1\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{x}{(\log x)^{A}}. |  | (ii) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}}, then (ii) holds if ϑ ⩽ ϑ 0 ​ ( t 1, t 2, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},t_{2},u)-\varepsilon.

If ϑ ⩽ ϑ 0 ​ ( t 1) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1})-\varepsilon and r = 1 r=1, then

 | ∑ b = p 1 ′ D 1 < p 1 ′ ⩽ D 1 1 + ε 9 ∑ q = b ​ c ⩽ D c | P ⁡ ( x u) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ 2 ( mod q) x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, 2) = 1 x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}b=p_{1}^{\prime}\\ D_{1}<p_{1}^{\prime}\leqslant D_{1}^{1+\varepsilon^{9}}\end{subarray}}\sum_{\begin{subarray}{c}q=bc\leqslant D\\ c\mid P\left(x^{u}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv 2(\bmod q)\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},2)=1\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{x}{(\log x)^{A}}. |  | (iii) |

Moreover if t 1 ⩽ 1 − θ 0 4 − 3 ​ θ 0 t_{1}\leqslant\frac{1-\theta_{0}}{4-3\theta_{0}}, then (iii) holds if ϑ ⩽ ϑ 0 ​ ( t 1, u, u) − ε \boldsymbol{\vartheta}\leqslant\boldsymbol{\vartheta}_{0}(t_{1},u,u)-\varepsilon.

If r = 0 r=0 and u = 1 500 u=\frac{1}{500}, this simplifies as

 | ∑ q ⩽ x 2497 4000 q | P ⁡ ( x 1 / 500) ( q, 2) = 1 λ ~ ± ​ ( q) ​ ( ∑ p 1 ⋯ p k ≡ 2 ( mod q) x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1 − 1 φ ⁡ ( q) ​ ∑ ( p 1 ⋯ p k, 2) = 1 x ε i / Δ < p i ⩽ x ε i ​ ∀ i ⩽ k 1) ≪ x ( log ⁡ x) A. \sum_{\begin{subarray}{c}q\leqslant x^{\frac{2497}{4000}}\\ q\mid P\left(x^{1/500}\right)\\ (q,2)=1\end{subarray}}\widetilde{\lambda}^{\pm}(q)\left(\sum_{\begin{subarray}{c}p_{1}\cdots p_{k}\equiv 2(\bmod q)\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1-\frac{1}{\varphi(q)}\sum_{\begin{subarray}{c}(p_{1}\cdots p_{k},2)=1\\ x^{\varepsilon_{i}}/\Delta<p_{i}\leqslant x^{\varepsilon_{i}}\ \forall i\leqslant k\end{subarray}}1\right)\ll\frac{x}{(\log x)^{A}}. |  |

## 3. Weighted sieve method

Let 𝒜 \mathcal{A} and ℬ \mathcal{B} denote finite sets of positive integers, 𝒫 \mathcal{P} denote an infinite set of primes and z ⩾ 2 z\geqslant 2. Put

 | 𝒜 = { N − p: p ⩽ N }, ℬ = { p + 2: p ⩽ x }, \mathcal{A}=\left\{N-p:p\leqslant N\right\},\quad\mathcal{B}=\left\{p+2:p\leqslant x\right\}, |  |

 | 𝒫 = { p: ( p, 2) = 1 }, 𝒫 ( q) = { p: p ∈ 𝒫, ( p, q) = 1 }, \mathcal{P}=\{p:(p,2)=1\},\quad\mathcal{P}(q)=\{p:p\in\mathcal{P},(p,q)=1\}, |  |

 | P ( z) = ∏ p ∈ 𝒫 p < z p, 𝒜 d = { a: a ∈ 𝒜, a ≡ 0 ( mod d) }, S ( 𝒜; 𝒫, z) = ∑ a ∈ 𝒜 ( a, P ⁡ ( z)) = 1 1. P(z)=\prod_{\begin{subarray}{c}p\in\mathcal{P}\\ p<z\end{subarray}}p,\quad\mathcal{A}_{d}=\{a:a\in\mathcal{A},a\equiv 0(\bmod d)\},\quad S(\mathcal{A};\mathcal{P},z)=\sum_{\begin{subarray}{c}a\in\mathcal{A}\\ (a,P(z))=1\end{subarray}}1. |  |

###### Lemma 3.1.

We have

 | 4 ​ D 1, 2 ​ ( N) ⩾ \displaystyle 4D_{1,2}(N)\geqslant | 3 ​ S ​ ( 𝒜, 𝒫 ⁡ ( N), N 1 11.49) + S ⁡ ( 𝒜, 𝒫 ⁡ ( N), N 1 6.18) \displaystyle\ 3S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{11.49}}\right)+S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{6.18}}\right) |  |

 |  | − 2 ∑ N 1 11.49 ⩽ p < N 25 128 ( p, N) = 1 S ( 𝒜 p; 𝒫 ( N), N 1 11.49) \displaystyle-2\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p<N^{\frac{25}{128}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | − ∑ N 25 128 ⩽ p < N 1 4 ( p, N) = 1 S ( 𝒜 p; 𝒫 ( N), N 1 11.49) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{25}{128}}\leqslant p<N^{\frac{1}{4}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | − ∑ N 1 4 ⩽ p < N 57 224 ( p, N) = 1 S ( 𝒜 p; 𝒫 ( N), N 1 11.49) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{4}}\leqslant p<N^{\frac{57}{224}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | − ∑ N 57 224 ⩽ p < N 1 3 ( p, N) = 1 S ( 𝒜 p; 𝒫 ( N), N 1 11.49) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{57}{224}}\leqslant p<N^{\frac{1}{3}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | − ∑ N 25 128 ⩽ p < N 1 2 − 3 11.49 ( p, N) = 1 S ( 𝒜 p; 𝒫 ( N), N 1 11.49) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{25}{128}}\leqslant p<N^{\frac{1}{2}-\frac{3}{11.49}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | + ∑ N 1 11.49 ⩽ p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 11.49) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | + ∑ N 1 11.49 ⩽ p 2 < N 1 6.18 ⩽ p 1 < N 25 128 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 11.49) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{2}<N^{\frac{1}{6.18}}\leqslant p_{1}<N^{\frac{25}{128}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | + ∑ N 1 11.49 ⩽ p 2 < N 1 6.18 < N 25 128 ⩽ p 1 < N 1 2 − 3 11.49 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 11.49) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{2}<N^{\frac{1}{6.18}}<N^{\frac{25}{128}}\leqslant p_{1}<N^{\frac{1}{2}-\frac{3}{11.49}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{11.49}}\right) |  |

 |  | − 2 ∑ N 1 2 − 3 11.49 ⩽ p 1 < p 2 < ( N p 1) 1 2 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N p 1), p 2) \displaystyle-2\sum_{\begin{subarray}{c}N^{\frac{1}{2}-\frac{3}{11.49}}\leqslant p_{1}<p_{2}<(\frac{N}{p_{1}})^{\frac{1}{2}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(Np_{1}),p_{2}\right) |  |

 |  | − ∑ N 1 11.49 ⩽ p 1 < N 1 3 ⩽ p 2 < ( N p 1) 1 2 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N p 1), p 2) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{1}<N^{\frac{1}{3}}\leqslant p_{2}<(\frac{N}{p_{1}})^{\frac{1}{2}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(Np_{1}),p_{2}\right) |  |

 |  | − ∑ N 1 6.18 ⩽ p 1 < N 1 2 − 3 11.49 ⩽ p 2 < ( N p 1) 1 2 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N p 1), ( N p 1 ​ p 2) 1 2) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{6.18}}\leqslant p_{1}<N^{\frac{1}{2}-\frac{3}{11.49}}\leqslant p_{2}<(\frac{N}{p_{1}})^{\frac{1}{2}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(Np_{1}),\left(\frac{N}{p_{1}p_{2}}\right)^{\frac{1}{2}}\right) |  |

 |  | − ∑ N 1 11.49 ⩽ p 4 < p 3 < p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2 ​ p 3 ​ p 4, N) = 1 S ( 𝒜 p 1 ​ p 2 ​ p 3 ​ p 4; 𝒫 ( N), p 3) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{4}<p_{3}<p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2}p_{3}p_{4},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(N),p_{3}\right) |  |

 |  | − ∑ N 1 11.49 ⩽ p 1 < p 2 < p 3 < N 1 6.18 ⩽ p 4 < N 1 2 − 2 11.49 ​ p 3 − 1 ( p 1 ​ p 2 ​ p 3 ​ p 4, N) = 1 S ( 𝒜 p 1 ​ p 2 ​ p 3 ​ p 4; 𝒫 ( N), p 2) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{1}<p_{2}<p_{3}<N^{\frac{1}{6.18}}\leqslant p_{4}<N^{\frac{1}{2}-\frac{2}{11.49}}p_{3}^{-1}\\ (p_{1}p_{2}p_{3}p_{4},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(N),p_{2}\right) |  |

 |  | + O ⁡ ( N 10.49 11.49) \displaystyle+O\left(N^{\frac{10.49}{11.49}}\right) |  |

 | = \displaystyle= | 3 ​ S 1 + S 2 − 2 ​ S 3 − S 4 − S 5 − S 6 − S 7 + S 8 + S 9 \displaystyle\ 3S_{1}+S_{2}-2S_{3}-S_{4}-S_{5}-S_{6}-S_{7}+S_{8}+S_{9} |  |

 |  | + S 10 − 2 ​ S 11 − S 12 − S 13 − S 14 − S 15 + O ⁡ ( N 10.49 11.49). \displaystyle+S_{10}-2S_{11}-S_{12}-S_{13}-S_{14}-S_{15}+O\left(N^{\frac{10.49}{11.49}}\right). |  |

###### Proof.

Taking κ 1 = 1 11.49 \kappa_{1}=\frac{1}{11.49} and κ 2 = 1 6.18 \kappa_{2}=\frac{1}{6.18} in [[22], Lemma 2.2], we get Lemma 3.1. ∎

###### Lemma 3.2.

We have

 | 4 ​ π 1, 2 ​ ( x) ⩾ \displaystyle 4\pi_{1,2}(x)\geqslant | 3 ​ S ​ ( ℬ, 𝒫, x 1 12) + S ⁡ ( ℬ, 𝒫, x 1 7.2) \displaystyle\ 3S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{12}}\right)+S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{7.2}}\right) |  |

 |  | + ∑ x 1 12 ⩽ p 2 < p 1 < x 1 7.2 S ( ℬ p 1 ​ p 2; 𝒫, x 1 12) \displaystyle+\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{2}<p_{1}<x^{\frac{1}{7.2}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | + ∑ x 1 12 ⩽ p 2 < x 1 7.2 ⩽ p 1 < x 1 4 S ( ℬ p 1 ​ p 2; 𝒫, x 1 12) \displaystyle+\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{2}<x^{\frac{1}{7.2}}\leqslant p_{1}<x^{\frac{1}{4}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | + ∑ x 1 12 ⩽ p 2 < x 1 7.2 < x 1 4 ⩽ p 1 < min ⁡ ( x 2 7, x 17 42 ​ p 2 − 1) S ( ℬ p 1 ​ p 2; 𝒫, x 1 12) \displaystyle+\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{2}<x^{\frac{1}{7.2}}<x^{\frac{1}{4}}\leqslant p_{1}<\min(x^{\frac{2}{7}},x^{\frac{17}{42}}p_{2}^{-1})\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | − 2 ∑ x 1 12 ⩽ p < x 1 4 S ( ℬ p; 𝒫, x 1 12) − 2 ∑ x 1 4 ⩽ p < x 2 7 − ε S ( ℬ p; 𝒫, x 1 12) \displaystyle-2\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p<x^{\frac{1}{4}}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right)-2\sum_{\begin{subarray}{c}x^{\frac{1}{4}}\leqslant p<x^{\frac{2}{7}-\varepsilon}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | − ∑ x 2 7 − ε ⩽ p < x 2 7 S ( ℬ p; 𝒫, x 1 12) − ∑ x 2 7 − ε ⩽ p < x 29 100 S ( ℬ p; 𝒫, x 1 12) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{2}{7}-\varepsilon}\leqslant p<x^{\frac{2}{7}}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right)-\sum_{\begin{subarray}{c}x^{\frac{2}{7}-\varepsilon}\leqslant p<x^{\frac{29}{100}}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | − ∑ x 29 100 ⩽ p < x 1 3 − ε S ( ℬ p; 𝒫, x 1 12) − ∑ x 1 3 − ε ⩽ p < x 1 3 S ( ℬ p; 𝒫, x 1 12) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{29}{100}}\leqslant p<x^{\frac{1}{3}-\varepsilon}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right)-\sum_{\begin{subarray}{c}x^{\frac{1}{3}-\varepsilon}\leqslant p<x^{\frac{1}{3}}\end{subarray}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{12}}\right) |  |

 |  | − ∑ x 1 12 ⩽ p 1 < x 1 3 ⩽ p 2 < ( x p 1) 1 2 S ( ℬ p 1 ​ p 2; 𝒫 ( p 1), p 2) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{1}<x^{\frac{1}{3}}\leqslant p_{2}<(\frac{x}{p_{1}})^{\frac{1}{2}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P}(p_{1}),p_{2}\right) |  |

 |  | − ∑ x 1 7.2 ⩽ p 1 < x 2 7 ⩽ p 2 < ( x p 1) 1 2 S ( ℬ p 1 ​ p 2; 𝒫 ( p 1), ( x p 1 ​ p 2) 1 2) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{1}{7.2}}\leqslant p_{1}<x^{\frac{2}{7}}\leqslant p_{2}<(\frac{x}{p_{1}})^{\frac{1}{2}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P}(p_{1}),\left(\frac{x}{p_{1}p_{2}}\right)^{\frac{1}{2}}\right) |  |

 |  | − 2 ∑ x 2 7 ⩽ p 1 < p 2 < ( x p 1) 1 2 S ( ℬ p 1 ​ p 2; 𝒫 ( p 1), p 2) \displaystyle-2\sum_{\begin{subarray}{c}x^{\frac{2}{7}}\leqslant p_{1}<p_{2}<(\frac{x}{p_{1}})^{\frac{1}{2}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P}(p_{1}),p_{2}\right) |  |

 |  | − ∑ x 1 12 ⩽ p 4 < p 3 < p 2 < p 1 < x 1 7.2 S ( ℬ p 1 ​ p 2 ​ p 3 ​ p 4; 𝒫 ( p 1), p 3) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{4}<p_{3}<p_{2}<p_{1}<x^{\frac{1}{7.2}}\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(p_{1}),p_{3}\right) |  |

 |  | − ∑ x 1 12 ⩽ p 1 < p 2 < p 3 < x 1 7.2 < p 4 < min ⁡ ( x 2 7, x 17 42 ​ p 3 − 1) S ( ℬ p 1 ​ p 2 ​ p 3 ​ p 4; 𝒫 ( p 1), p 2) \displaystyle-\sum_{\begin{subarray}{c}x^{\frac{1}{12}}\leqslant p_{1}<p_{2}<p_{3}<x^{\frac{1}{7.2}}<p_{4}<\min\left(x^{\frac{2}{7}},x^{\frac{17}{42}}p_{3}^{-1}\right)\end{subarray}}S\left(\mathcal{B}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(p_{1}),p_{2}\right) |  |

 |  | + O ⁡ ( x 11 12) \displaystyle+O\left(x^{\frac{11}{12}}\right) |  |

 | = \displaystyle= | 3 ​ S 1 ′ + S 2 ′ + S 3 ′ + S 4 ′ + S 5 ′ − 2 ​ S 6 ′ − 2 ​ S 7 ′ − S 8 ′ − S 9 ′ \displaystyle\ 3S^{\prime}_{1}+S^{\prime}_{2}+S^{\prime}_{3}+S^{\prime}_{4}+S^{\prime}_{5}-2S^{\prime}_{6}-2S^{\prime}_{7}-S^{\prime}_{8}-S^{\prime}_{9} |  |

 |  | − S 10 ′ − S 11 ′ − S 12 ′ − S 13 ′ − 2 ​ S 14 ′ − S 15 ′ − S 16 ′ + O ⁡ ( x 11 12). \displaystyle-S^{\prime}_{10}-S^{\prime}_{11}-S^{\prime}_{12}-S^{\prime}_{13}-2S^{\prime}_{14}-S^{\prime}_{15}-S^{\prime}_{16}+O\left(x^{\frac{11}{12}}\right). |  |

###### Proof.

This is [[3], Lemma 3.2] and [[13], Lemma 3.2]. ∎

## 4. Proof of Theorem 1.1

In this section, sets 𝒜 \mathcal{A} and 𝒫 \mathcal{P} are defined respectively. Let γ \gamma denotes the Euler’s constant, F ⁡ ( s) F(s) and f ⁡ ( s) f(s) are determined by the following differential-difference equation

 | { F ( s) = 2 ​ e γ s, f ( s) = 0, 0 < s ⩽ 2, ( s F ( s)) ′ = f ( s − 1), ( s f ( s)) ′ = F ( s − 1), s ⩾ 2, \displaystyle\begin{cases}F(s)=\frac{2e^{\gamma}}{s},\quad f(s)=0,\quad&0<s\leqslant 2,\\ (sF(s))^{\prime}=f(s-1),\quad(sf(s))^{\prime}=F(s-1),\quad&s\geqslant 2,\end{cases} |  |

and let ω ⁡ ( u) \omega(u) denotes the Buchstab function determined by the following differential-difference equation

 | { ω ⁡ ( u) = 1 u, 1 ⩽ u ⩽ 2, ( u ​ ω ​ ( u)) ′ = ω ⁡ ( u − 1), u ⩾ 2. \displaystyle\begin{cases}\omega(u)=\frac{1}{u},&\quad 1\leqslant u\leqslant 2,\\ (u\omega(u))^{\prime}=\omega(u-1),&\quad u\geqslant 2.\end{cases} |  |

We first consider S 1 S_{1} and S 2 S_{2}. By Buchstab’s identity, we have

 | S 1 = S ⁡ ( 𝒜, 𝒫 ⁡ ( N), N 1 11.49) = \displaystyle S_{1}=S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{11.49}}\right)= | S ⁡ ( 𝒜, 𝒫 ⁡ ( N), N 1 500) − ∑ N 1 500 ⩽ p < N 1 11.49 ( p, N) = 1 S ⁡ ( 𝒜 p, 𝒫 ⁡ ( N), N 1 500) \displaystyle\ S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{500}}\right)-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p<N^{\frac{1}{11.49}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | + ∑ N 1 500 ⩽ p 2 < p 1 < N 1 11.49 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 500) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p_{2}<p_{1}<N^{\frac{1}{11.49}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | − ∑ N 1 500 ⩽ p 3 < p 2 < p 1 < N 1 11.49 ( p 1 ​ p 2 ​ p 3, N) = 1 S ( 𝒜 p 1 ​ p 2 ​ p 3; 𝒫 ( N), p 3) \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p_{3}<p_{2}<p_{1}<N^{\frac{1}{11.49}}\\ (p_{1}p_{2}p_{3},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}};\mathcal{P}(N),p_{3}\right) |  | (9) |

and

 | S 2 = S ⁡ ( 𝒜, 𝒫 ⁡ ( N), N 1 6.18) = \displaystyle S_{2}=S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{6.18}}\right)= | S ⁡ ( 𝒜, 𝒫 ⁡ ( N), N 1 500) − ∑ N 1 500 ⩽ p < N 1 6.18 ( p, N) = 1 S ⁡ ( 𝒜 p, 𝒫 ⁡ ( N), N 1 500) \displaystyle\ S\left(\mathcal{A};\mathcal{P}(N),N^{\frac{1}{500}}\right)-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p<N^{\frac{1}{6.18}}\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | + ∑ N 1 500 ⩽ p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 500) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | − ∑ N 1 500 ⩽ p 3 < p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2 ​ p 3, N) = 1 S ( 𝒜 p 1 ​ p 2 ​ p 3; 𝒫 ( N), p 3). \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p_{3}<p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2}p_{3},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}};\mathcal{P}(N),p_{3}\right). |  | (10) |

By Lemma 2.1, Iwaniec’s linear sieve method and arguments in [16], [15] and [13] we have

 | S 1 ⩾ \displaystyle S_{1}\geqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 500 ​ f ​ ( 500 ​ ϑ 1 500) − 500 ​ ∫ 1 500 1 11.49 F ⁡ ( 500 ​ ( ϑ 1 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(500f\left(500\boldsymbol{\vartheta}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{1}{11.49}}\frac{F(500(\boldsymbol{\vartheta}_{1}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt\right. |  |

 |  | + 500 ∫ 1 500 1 11.49 ∫ 1 500 t 1 f ⁡ ( 500 ​ ( ϑ 1 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{1}{11.49}}\int_{\frac{1}{500}}^{t_{1}}\frac{f(500(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 1 11.49 ∫ 1 500 t 1 ∫ 1 500 t 2 F ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.-\int_{\frac{1}{500}}^{\frac{1}{11.49}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  | (11) |

and

 | S 2 ⩾ \displaystyle S_{2}\geqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 500 ​ f ​ ( 500 ​ ϑ 1 500) − 500 ​ ∫ 1 500 1 6.18 F ⁡ ( 500 ​ ( ϑ 1 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(500f\left(500\boldsymbol{\vartheta}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{1}{6.18}}\frac{F(500(\boldsymbol{\vartheta}_{1}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt\right. |  |

 |  | + 500 ∫ 1 500 1 6.18 ∫ 1 500 t 1 f ⁡ ( 500 ​ ( ϑ 1 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{1}{6.18}}\int_{\frac{1}{500}}^{t_{1}}\frac{f(500(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 1 6.18 ∫ 1 500 t 1 ∫ 1 500 t 2 F ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\left.-\int_{\frac{1}{500}}^{\frac{1}{6.18}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}}, |  | (12) |

where ϑ 1 500 = 19101 32000 \boldsymbol{\vartheta}_{\frac{1}{500}}=\frac{19101}{32000}. By numerical calculations we get that

 | S 1 ⩾ 12.902021 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 S_{1}\geqslant 12.902021\frac{C(N)N}{(\log N)^{2}} |  | (13) |

and

 | S 2 ⩾ 6.533916 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. S_{2}\geqslant 6.533916\frac{C(N)N}{(\log N)^{2}}. |  | (14) |

For S 3 S_{3}, we can either use Buchstab’s identity and Lichtman’s method to estimate S 3 S_{3} with a better distribution level as in [15] or use Chen’s double sieve technique as in [22]. The first option leads to

 | ∑ p ( p, N) = 1 S ⁡ ( 𝒜 p, 𝒫 ⁡ ( N), N 1 11.49) = \displaystyle\sum_{\begin{subarray}{c}p\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{11.49}}\right)= | ∑ p ( p, N) = 1 S ⁡ ( 𝒜 p, 𝒫 ⁡ ( N), N 1 k) \displaystyle\ \sum_{\begin{subarray}{c}p\\ (p,N)=1\end{subarray}}S\left(\mathcal{A}_{p};\mathcal{P}(N),N^{\frac{1}{k}}\right) |  |

 |  | − ∑ p 1 N 1 k ⩽ p 2 < N 1 11.49 ( p 1 ​ p 2, N) = 1 S ( 𝒜 p 1 ​ p 2; 𝒫 ( N), N 1 k) \displaystyle-\sum_{\begin{subarray}{c}p_{1}\\ N^{\frac{1}{k}}\leqslant p_{2}<N^{\frac{1}{11.49}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(N),N^{\frac{1}{k}}\right) |  |

 |  | + ∑ p 1 N 1 k ⩽ p 3 < p 2 < N 1 11.49 ( p 1 ​ p 2 ​ p 3, N) = 1 S ( 𝒜 p 1 ​ p 2 ​ p 3; 𝒫 ( N), p 3) \displaystyle+\sum_{\begin{subarray}{c}p_{1}\\ N^{\frac{1}{k}}\leqslant p_{3}<p_{2}<N^{\frac{1}{11.49}}\\ (p_{1}p_{2}p_{3},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}};\mathcal{P}(N),p_{3}\right) |  | (15) |

for some k ⩾ 11.49 k\geqslant 11.49, while the second option creates a small saving on S 3 S_{3} itself. We can also use Chen’s double sieve on the first two sums on the right–hand side of (15) after applying Buchstab’s identity. We don’t know which of these options gives a smaller value, hence we take a minimum. By Lemma 2.1, Iwaniec’s linear sieve method and arguments in [16], [15] and [13] we have

 | S 3 ⩽ \displaystyle S_{3}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( ∫ 1 11.49 25 128 min ⁡ ( 11.49 ​ F ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1, 1 11.49, 1 11.49) − t 1)) t 1 CLOSE CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(\int_{\frac{1}{11.49}}^{\frac{25}{128}}\min\left(11.49\frac{F(11.49(\boldsymbol{\vartheta}_{1}(t_{1},\frac{1}{11.49},\frac{1}{11.49})-t_{1}))}{t_{1}}\right.\right. |  |

 |  | − 22.98 ​ e γ ​ H ​ ( 11.49 ​ ( 1 2 − t 1)) ( 11.49 ​ ( 1 2 − t 1)) ​ t 1, min 11.49 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 1 ​ ( t 1, 1 k, 1 k) − t 1)) t 1 CLOSE \displaystyle-\frac{22.98e^{\gamma}H(11.49(\frac{1}{2}-t_{1}))}{(11.49(\frac{1}{2}-t_{1}))t_{1}},\min_{11.49\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{1}(t_{1},\frac{1}{k},\frac{1}{k})-t_{1}))}{t_{1}}\right. |  |

 |  | − 2 ​ k ​ e γ ​ H ​ ( k ⁡ ( 1 2 − t 1)) ( k ⁡ ( 1 2 − t 1)) ​ t 1 − k ​ ∫ 1 k 1 11.49 f ⁡ ( k ⁡ ( ϑ 1 ​ ( t 1, t 2, 1 k) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 \displaystyle-\frac{2ke^{\gamma}H(k(\frac{1}{2}-t_{1}))}{(k(\frac{1}{2}-t_{1}))t_{1}}-k\int_{\frac{1}{k}}^{\frac{1}{11.49}}\frac{f(k(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{k})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2} |  |

 |  | − 2 k e γ ∫ 1 k 1 11.49 h ⁡ ( k ⁡ ( 1 2 − t 1 − t 2)) ( k ⁡ ( 1 2 − t 1 − t 2)) ​ t 1 ​ t 2 d t 2 \displaystyle-2ke^{\gamma}\int_{\frac{1}{k}}^{\frac{1}{11.49}}\frac{h(k(\frac{1}{2}-t_{1}-t_{2}))}{(k(\frac{1}{2}-t_{1}-t_{2}))t_{1}t_{2}}dt_{2} |  |

 |  | + ∫ 1 k 1 11.49 ∫ 1 k t 2 F ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2)) d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\left.+\int_{\frac{1}{k}}^{\frac{1}{11.49}}\int_{\frac{1}{k}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}\right)\right)dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 10.436523 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 10.436523\frac{C(N)N}{(\log N)^{2}}, |  | (16) |

where we choose k = 12.3 k=12.3 and H ​ ( s) = H 1 / 2 ​ ( s) H(s)=H_{1/2}(s) and h ​ ( s) = h 1 / 2 ​ ( s) h(s)=h_{1/2}(s) are defined as the same in [22]. We have used the following lower bounds of H ⁡ ( s) H(s) and h ⁡ ( s) h(s) for 2.0 ⩽ s ⩽ 4.9 2.0\leqslant s\leqslant 4.9. These values can be found at Tables 1 and 2 of [22]. We remark that we have H ϑ ​ ( s) ⩾ H 1 / 2 ​ ( s) H_{\boldsymbol{\vartheta}}(s)\geqslant H_{1/2}(s) and h ϑ ​ ( s) ⩾ h 1 / 2 ​ ( s) h_{\boldsymbol{\vartheta}}(s)\geqslant h_{1/2}(s) for ϑ > 1 2 \boldsymbol{\vartheta}>\frac{1}{2}.

 | H ⁡ ( s) ⩾ { 0.0223939, 2.0 < s ⩽ 2.2, 0.0217196, 2.2 < s ⩽ 2.3, 0.0202876, 2.3 < s ⩽ 2.4, 0.0181433, 2.4 < s ⩽ 2.5, 0.0158644, 2.5 < s ⩽ 2.6, 0.0129923, 2.6 < s ⩽ 2.7, 0.0100686, 2.7 < s ⩽ 2.8, 0.0078162, 2.8 < s ⩽ 2.9, 0.0072943, 2.9 < s ⩽ 3.0, 0.0061642, 3.0 < s ⩽ 3.1, 0.0052233, 3.1 < s ⩽ 3.2, 0.0044073, 3.2 < s ⩽ 3.3, 0.0036995, 3.3 < s ⩽ 3.4, 0.0030860, 3.4 < s ⩽ 3.5, { 0.0025551, 3.5 < s ⩽ 3.6, 0.0020972, 3.6 < s ⩽ 3.7, 0.0017038, 3.7 < s ⩽ 3.8, 0.0013680, 3.8 < s ⩽ 3.9, 0.0010835, 3.9 < s ⩽ 4.0, 0.0008451, 4.0 < s ⩽ 4.1, 0.0006482, 4.1 < s ⩽ 4.2, 0.0004882, 4.2 < s ⩽ 4.3, 0.0003602, 4.3 < s ⩽ 4.4, 0.0002592, 4.4 < s ⩽ 4.5, 0.0001803, 4.5 < s ⩽ 4.6, 0.0001187, 4.6 < s ⩽ 4.7, 0.0000702, 4.7 < s ⩽ 4.8, 0.0000313, 4.8 < s ⩽ 4.9, \displaystyle H(s)\geqslant\begin{cases}0.0223939,&\quad 2.0<s\leqslant 2.2,\\ 0.0217196,&\quad 2.2<s\leqslant 2.3,\\ 0.0202876,&\quad 2.3<s\leqslant 2.4,\\ 0.0181433,&\quad 2.4<s\leqslant 2.5,\\ 0.0158644,&\quad 2.5<s\leqslant 2.6,\\ 0.0129923,&\quad 2.6<s\leqslant 2.7,\\ 0.0100686,&\quad 2.7<s\leqslant 2.8,\\ 0.0078162,&\quad 2.8<s\leqslant 2.9,\\ 0.0072943,&\quad 2.9<s\leqslant 3.0,\\ 0.0061642,&\quad 3.0<s\leqslant 3.1,\\ 0.0052233,&\quad 3.1<s\leqslant 3.2,\\ 0.0044073,&\quad 3.2<s\leqslant 3.3,\\ 0.0036995,&\quad 3.3<s\leqslant 3.4,\\ 0.0030860,&\quad 3.4<s\leqslant 3.5,\\ \end{cases}\quad\begin{cases}0.0025551,&\quad 3.5<s\leqslant 3.6,\\ 0.0020972,&\quad 3.6<s\leqslant 3.7,\\ 0.0017038,&\quad 3.7<s\leqslant 3.8,\\ 0.0013680,&\quad 3.8<s\leqslant 3.9,\\ 0.0010835,&\quad 3.9<s\leqslant 4.0,\\ 0.0008451,&\quad 4.0<s\leqslant 4.1,\\ 0.0006482,&\quad 4.1<s\leqslant 4.2,\\ 0.0004882,&\quad 4.2<s\leqslant 4.3,\\ 0.0003602,&\quad 4.3<s\leqslant 4.4,\\ 0.0002592,&\quad 4.4<s\leqslant 4.5,\\ 0.0001803,&\quad 4.5<s\leqslant 4.6,\\ 0.0001187,&\quad 4.6<s\leqslant 4.7,\\ 0.0000702,&\quad 4.7<s\leqslant 4.8,\\ 0.0000313,&\quad 4.8<s\leqslant 4.9,\\ \end{cases} |  | (17) |

 | h ⁡ ( s) ⩾ { 0.0232385, s = 2.0, 0.0211041, 2.0 < s ⩽ 2.1, 0.0191556, 2.1 < s ⩽ 2.2, 0.0173631, 2.2 < s ⩽ 2.3, 0.0157035, 2.3 < s ⩽ 2.4, 0.0141585, 2.4 < s ⩽ 2.5, 0.0127132, 2.5 < s ⩽ 2.6, 0.0113556, 2.6 < s ⩽ 2.7, 0.0100756, 2.7 < s ⩽ 2.8, 0.0088648, 2.8 < s ⩽ 2.9, 0.0077612, 2.9 < s ⩽ 3.0, 0.0066236, 3.0 < s ⩽ 3.1, 0.0055818, 3.1 < s ⩽ 3.2, 0.0046164, 3.2 < s ⩽ 3.3, 0.0037529, 3.3 < s ⩽ 3.4, { 0.0030123, 3.4 < s ⩽ 3.5, 0.0023901, 3.5 < s ⩽ 3.6, 0.0018997, 3.6 < s ⩽ 3.7, 0.0015336, 3.7 < s ⩽ 3.8, 0.0012593, 3.8 < s ⩽ 3.9, 0.0010120, 3.9 < s ⩽ 4.0, 0.0008099, 4.0 < s ⩽ 4.1, 0.0006440, 4.1 < s ⩽ 4.2, 0.0005084, 4.2 < s ⩽ 4.3, 0.0003980, 4.3 < s ⩽ 4.4, 0.0003085, 4.4 < s ⩽ 4.5, 0.0002365, 4.5 < s ⩽ 4.6, 0.0001791, 4.6 < s ⩽ 4.7, 0.0001396, 4.7 < s ⩽ 4.8, 0.0000981, 4.8 < s ⩽ 4.9. \displaystyle h(s)\geqslant\begin{cases}0.0232385,&\quad s=2.0,\\ 0.0211041,&\quad 2.0<s\leqslant 2.1,\\ 0.0191556,&\quad 2.1<s\leqslant 2.2,\\ 0.0173631,&\quad 2.2<s\leqslant 2.3,\\ 0.0157035,&\quad 2.3<s\leqslant 2.4,\\ 0.0141585,&\quad 2.4<s\leqslant 2.5,\\ 0.0127132,&\quad 2.5<s\leqslant 2.6,\\ 0.0113556,&\quad 2.6<s\leqslant 2.7,\\ 0.0100756,&\quad 2.7<s\leqslant 2.8,\\ 0.0088648,&\quad 2.8<s\leqslant 2.9,\\ 0.0077612,&\quad 2.9<s\leqslant 3.0,\\ 0.0066236,&\quad 3.0<s\leqslant 3.1,\\ 0.0055818,&\quad 3.1<s\leqslant 3.2,\\ 0.0046164,&\quad 3.2<s\leqslant 3.3,\\ 0.0037529,&\quad 3.3<s\leqslant 3.4,\\ \end{cases}\quad\begin{cases}0.0030123,&\quad 3.4<s\leqslant 3.5,\\ 0.0023901,&\quad 3.5<s\leqslant 3.6,\\ 0.0018997,&\quad 3.6<s\leqslant 3.7,\\ 0.0015336,&\quad 3.7<s\leqslant 3.8,\\ 0.0012593,&\quad 3.8<s\leqslant 3.9,\\ 0.0010120,&\quad 3.9<s\leqslant 4.0,\\ 0.0008099,&\quad 4.0<s\leqslant 4.1,\\ 0.0006440,&\quad 4.1<s\leqslant 4.2,\\ 0.0005084,&\quad 4.2<s\leqslant 4.3,\\ 0.0003980,&\quad 4.3<s\leqslant 4.4,\\ 0.0003085,&\quad 4.4<s\leqslant 4.5,\\ 0.0002365,&\quad 4.5<s\leqslant 4.6,\\ 0.0001791,&\quad 4.6<s\leqslant 4.7,\\ 0.0001396,&\quad 4.7<s\leqslant 4.8,\\ 0.0000981,&\quad 4.8<s\leqslant 4.9.\\ \end{cases} |  | (18) |

Similarly, for S 4 S_{4}, S 5 S_{5} and S 7 S_{7} we have

 | S 4 ⩽ \displaystyle S_{4}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( ∫ 25 128 1 4 min ⁡ ( 11.49 ​ F ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1) − t 1)) t 1 − 22.98 ​ e γ ​ H ​ ( 11.49 ​ ( 1 2 − t 1)) ( 11.49 ​ ( 1 2 − t 1)) ​ t 1 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(\int_{\frac{25}{128}}^{\frac{1}{4}}\min\left(11.49\frac{F(11.49(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}}-\frac{22.98e^{\gamma}H(11.49(\frac{1}{2}-t_{1}))}{(11.49(\frac{1}{2}-t_{1}))t_{1}},\right.\right. |  |

 |  | min 11.49 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 1 ​ ( t 1) − t 1)) t 1 − 2 ​ k ​ e γ ​ H ​ ( k ⁡ ( 1 2 − t 1)) ( k ⁡ ( 1 2 − t 1)) ​ t 1 CLOSE \displaystyle\min_{11.49\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}}-\frac{2ke^{\gamma}H(k(\frac{1}{2}-t_{1}))}{(k(\frac{1}{2}-t_{1}))t_{1}}\right. |  |

 |  | − ∫ 1 k 1 11.49 f ⁡ ( ( ϑ 1 ​ ( t 1) − t 1 − t 2) t 2) t 1 ​ t 2 2 d t 2)) d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\left.-\ \int_{\frac{1}{k}}^{\frac{1}{11.49}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}-t_{2})}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}\right)\right)dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 3.311305 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 3.311305\frac{C(N)N}{(\log N)^{2}}, |  | (19) |

 | S 5 ⩽ \displaystyle S_{5}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( ∫ 1 4 57 224 min ⁡ ( 11.49 ​ F ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1) − t 1)) t 1 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(\int_{\frac{1}{4}}^{\frac{57}{224}}\min\left(11.49\frac{F(11.49(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}},\right.\right. |  |

 |  | OPEN OPEN min 11.49 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 1 ​ ( t 1) − t 1)) t 1 − ∫ 1 k 1 11.49 f ⁡ ( ( ϑ 1 ​ ( t 1) − t 1 − t 2) t 2) t 1 ​ t 2 2 ​ d ​ t 2)) ​ d ​ t 1) ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\min_{11.49\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}}-\int_{\frac{1}{k}}^{\frac{1}{11.49}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}-t_{2})}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}\right)\right)dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.272301 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 0.272301\frac{C(N)N}{(\log N)^{2}}, |  | (20) |

 | S 7 ⩽ \displaystyle S_{7}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( ∫ 25 128 1 2 − 3 11.49 min ⁡ ( 11.49 ​ F ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1) − t 1)) t 1 − 22.98 ​ e γ ​ H ​ ( 11.49 ​ ( 1 2 − t 1)) ( 11.49 ​ ( 1 2 − t 1)) ​ t 1 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(\int_{\frac{25}{128}}^{\frac{1}{2}-\frac{3}{11.49}}\min\left(11.49\frac{F(11.49(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}}-\frac{22.98e^{\gamma}H(11.49(\frac{1}{2}-t_{1}))}{(11.49(\frac{1}{2}-t_{1}))t_{1}},\right.\right. |  |

 |  | min 11.49 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 1 ​ ( t 1) − t 1)) t 1 − 2 ​ k ​ e γ ​ H ​ ( k ⁡ ( 1 2 − t 1)) ( k ⁡ ( 1 2 − t 1)) ​ t 1 CLOSE \displaystyle\min_{11.49\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}))}{t_{1}}-\frac{2ke^{\gamma}H(k(\frac{1}{2}-t_{1}))}{(k(\frac{1}{2}-t_{1}))t_{1}}\right. |  |

 |  | − ∫ 1 k 1 11.49 f ⁡ ( ( ϑ 1 ​ ( t 1) − t 1 − t 2) t 2) t 1 ​ t 2 2 d t 2)) d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\left.-\ \int_{\frac{1}{k}}^{\frac{1}{11.49}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1})-t_{1}-t_{2})}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}\right)\right)dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 2.659313 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 2.659313\frac{C(N)N}{(\log N)^{2}}. |  | (21) |

By the classical linear sieve, for S 6 S_{6} we have

 | S 6 ⩽ \displaystyle S_{6}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 11.49 ​ ∫ 57 224 1 3 F ​ ( 11.49 ​ ( 1 2 − t)) t ​ 𝑑 t) ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(11.49\int_{\frac{57}{224}}^{\frac{1}{3}}\frac{F(11.49(\frac{1}{2}-t))}{t}dt\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 5.259433 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 5.259433\frac{C(N)N}{(\log N)^{2}}. |  | (22) |

For S 8 S_{8} – S 10 S_{10} we can also use Chen’s double sieve to gain some savings. Using similar methods as above together with [[22], Propositions 4.2 and 4.3], we have

 | S 8 ⩾ \displaystyle S_{8}\geqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 11.49 ​ ∫ 1 11.49 1 6.18 ∫ 1 11.49 t 1 f ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1, t 2, 1 11.49) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 ​ d ​ t 1 CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(11.49\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\int_{\frac{1}{11.49}}^{t_{1}}\frac{f(11.49(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{11.49})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1}\right. |  |

 |  | + 11.49 ∫ 1 11.49 1 6.18 ∫ 1 11.49 t 1 2 ​ e γ ​ h ​ ( 11.49 ​ ( 1 2 − t 1 − t 2)) ( 11.49 ​ ( 1 2 − t 1 − t 2)) ​ t 1 ​ t 2 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.+\ 11.49\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\int_{\frac{1}{11.49}}^{t_{1}}\frac{2e^{\gamma}h(11.49(\frac{1}{2}-t_{1}-t_{2}))}{(11.49(\frac{1}{2}-t_{1}-t_{2}))t_{1}t_{2}}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 2.421452 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 2.421452\frac{C(N)N}{(\log N)^{2}}, |  | (23) |

 | S 9 ⩾ \displaystyle S_{9}\geqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 11.49 ​ ∫ 1 6.18 25 128 ∫ 1 11.49 1 6.18 f ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1, t 2, 1 11.49) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 ​ d ​ t 1 CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(11.49\int_{\frac{1}{6.18}}^{\frac{25}{128}}\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\frac{f(11.49(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{11.49})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1}\right. |  |

 |  | + 11.49 ∫ 1 6.18 1 2 − 2 6.18 ∫ 1 11.49 1 6.18 2 ​ e γ ​ h ​ ( 11.49 ​ ( 1 2 − t 1 − t 2)) ( 11.49 ​ ( 1 2 − t 1 − t 2)) ​ t 1 ​ t 2 d t 2 d t 1 \displaystyle+11.49\int_{\frac{1}{6.18}}^{\frac{1}{2}-\frac{2}{6.18}}\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\frac{2e^{\gamma}h(11.49(\frac{1}{2}-t_{1}-t_{2}))}{(11.49(\frac{1}{2}-t_{1}-t_{2}))t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | + 11.49 ∫ 1 2 − 2 6.18 25 128 ∫ 1 11.49 39 256 2 ​ e γ ​ h ​ ( 11.49 ​ ( 1 2 − t 1 − t 2)) ( 11.49 ​ ( 1 2 − t 1 − t 2)) ​ t 1 ​ t 2 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.+\ 11.49\int_{\frac{1}{2}-\frac{2}{6.18}}^{\frac{25}{128}}\int_{\frac{1}{11.49}}^{\frac{39}{256}}\frac{2e^{\gamma}h(11.49(\frac{1}{2}-t_{1}-t_{2}))}{(11.49(\frac{1}{2}-t_{1}-t_{2}))t_{1}t_{2}}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 1.382532 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 1.382532\frac{C(N)N}{(\log N)^{2}}, |  | (24) |

 | S 10 ⩾ \displaystyle S_{10}\geqslant | ( 1 + o ⁡ ( 1)) ​ 2 e γ ​ ( 11.49 ​ ∫ 25 128 1 2 − 3 11.49 ∫ 1 11.49 1 6.18 f ⁡ ( 11.49 ​ ( ϑ 1 ​ ( t 1, t 2, 1 11.49) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 ​ d ​ t 1 CLOSE \displaystyle\ (1+o(1))\frac{2}{e^{\gamma}}\left(11.49\int_{\frac{25}{128}}^{\frac{1}{2}-\frac{3}{11.49}}\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\frac{f(11.49(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{11.49})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1}\right. |  |

 |  | + 11.49 ∫ 25 128 1 2 − 3 11.49 ∫ 1 11.49 1.5 11.49 2 ​ e γ ​ h ​ ( 11.49 ​ ( 1 2 − t 1 − t 2)) ( 11.49 ​ ( 1 2 − t 1 − t 2)) ​ t 1 ​ t 2 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.+\ 11.49\int_{\frac{25}{128}}^{\frac{1}{2}-\frac{3}{11.49}}\int_{\frac{1}{11.49}}^{\frac{1.5}{11.49}}\frac{2e^{\gamma}h(11.49(\frac{1}{2}-t_{1}-t_{2}))}{(11.49(\frac{1}{2}-t_{1}-t_{2}))t_{1}t_{2}}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 0.960457 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 0.960457\frac{C(N)N}{(\log N)^{2}}. |  | (25) |

For the remaining terms, we can use Chen’s switching principle together with Lemma 2.2 to estimate them. Namely, for S 11 S_{11} we have

 | S 11 = ∑ N 1 2 − 3 11.49 ⩽ p 1 < p 2 < ( N p 1) 1 2 ( p 1 ​ p 2, N) = 1 S ⁡ ( 𝒜 p 1 ​ p 2, 𝒫 ⁡ ( N ​ p 1), p 2) = S ⁡ ( 𝒜 ′, 𝒫 ⁡ ( N), N 1 2), S_{11}=\sum_{\begin{subarray}{c}N^{\frac{1}{2}-\frac{3}{11.49}}\leqslant p_{1}<p_{2}<(\frac{N}{p_{1}})^{\frac{1}{2}}\\ (p_{1}p_{2},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}};\mathcal{P}(Np_{1}),p_{2}\right)=S\left(\mathcal{A}^{\prime};\mathcal{P}(N),N^{\frac{1}{2}}\right), |  | (26) |

where the set 𝒜 ′ \mathcal{A}^{\prime} is defined as

 | 𝒜 ′ = { N − p 1 p 2 m: N 1 2 − 3 11.49 ⩽ p 1 < p 2 < ( N / p 1) 1 2, p ′ ∣ m ⇒ p ′ > p 2 or p ′ = p 1 }. \mathcal{A}^{\prime}=\left\{N-p_{1}p_{2}m:N^{\frac{1}{2}-\frac{3}{11.49}}\leqslant p_{1}<p_{2}<(N/p_{1})^{\frac{1}{2}},\ p^{\prime}\mid m\Rightarrow p^{\prime}>p_{2}\text{ or }p^{\prime}=p_{1}\right\}. |  |

We note that each m m above must be a prime number or a P 2 P_{2} since 1 2 − 3 11.49 > 1 5 \frac{1}{2}-\frac{3}{11.49}>\frac{1}{5}. By Buchstab’s identity, we have

 | S 11 = S ⁡ ( 𝒜 ′, 𝒫 ⁡ ( N), N 1 2) ⩽ \displaystyle S_{11}=S\left(\mathcal{A}^{\prime};\mathcal{P}(N),N^{\frac{1}{2}}\right)\leqslant | S ⁡ ( 𝒜 ′, 𝒫 ⁡ ( N), N 25 128) \displaystyle\ S\left(\mathcal{A}^{\prime};\mathcal{P}(N),N^{\frac{25}{128}}\right) |  |

 | = \displaystyle= | S ⁡ ( 𝒜 ′, 𝒫 ⁡ ( N), N 1 500) − ∑ N 1 500 ⩽ p ′ < N 25 128 ( p ′, N) = 1 S ⁡ ( 𝒜 p ′ ′, 𝒫 ⁡ ( N), N 1 500) \displaystyle\ S\left(\mathcal{A}^{\prime};\mathcal{P}(N),N^{\frac{1}{500}}\right)-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p^{\prime}<N^{\frac{25}{128}}\\ (p^{\prime},N)=1\end{subarray}}S\left(\mathcal{A}^{\prime}_{p^{\prime}};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | + ∑ N 1 500 ⩽ p 2 ′ < p 1 ′ < N 25 128 ( p 1 ′ ​ p 2 ′, N) = 1 S ( 𝒜 p 1 ′ ​ p 2 ′ ′; 𝒫 ( N), N 1 500) \displaystyle+\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p^{\prime}_{2}<p^{\prime}_{1}<N^{\frac{25}{128}}\\ (p^{\prime}_{1}p^{\prime}_{2},N)=1\end{subarray}}S\left(\mathcal{A}^{\prime}_{p^{\prime}_{1}p^{\prime}_{2}};\mathcal{P}(N),N^{\frac{1}{500}}\right) |  |

 |  | − ∑ N 1 500 ⩽ p 3 ′ < p 2 ′ < p 1 ′ < N 25 128 ( p 1 ′ ​ p 2 ′ ​ p 3 ′, N) = 1 S ( 𝒜 p 1 ′ ​ p 2 ′ ​ p 3 ′ ′; 𝒫 ( N), p 3 ′). \displaystyle-\sum_{\begin{subarray}{c}N^{\frac{1}{500}}\leqslant p^{\prime}_{3}<p^{\prime}_{2}<p^{\prime}_{1}<N^{\frac{25}{128}}\\ (p^{\prime}_{1}p^{\prime}_{2}p^{\prime}_{3},N)=1\end{subarray}}S\left(\mathcal{A}^{\prime}_{p^{\prime}_{1}p^{\prime}_{2}p^{\prime}_{3}};\mathcal{P}(N),p^{\prime}_{3}\right). |  | (27) |

Then by Lemma 2.2, Iwaniec’s linear sieve method and arguments in [16], [15] and [13] we have

 | S 11 ⩽ \displaystyle S_{11}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 ​ C ​ ( N) ​ | 𝒜 ′ | e γ ​ log ⁡ N ​ ( 500 ​ F ​ ( 500 ​ ϑ 1 500) − 500 ​ ∫ 1 500 25 128 f ⁡ ( 500 ​ ( ϑ 1 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t CLOSE \displaystyle\ (1+o(1))\frac{2C(N)\left|\mathcal{A}^{\prime}\right|}{e^{\gamma}\log N}\left(500F\left(500\boldsymbol{\vartheta}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{25}{128}}\frac{f(500(\boldsymbol{\vartheta}_{1}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt\right. |  |

 |  | + 500 ∫ 1 500 25 128 ∫ 1 500 t 1 F ⁡ ( 500 ​ ( ϑ 1 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{25}{128}}\int_{\frac{1}{500}}^{t_{1}}\frac{F(500(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 25 128 ∫ 1 500 t 1 ∫ 1 500 t 2 f ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1) \displaystyle\left.-\int_{\frac{1}{500}}^{\frac{25}{128}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}\right) |  |

 | ⩽ \displaystyle\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 ​ G 1 e γ ​ ( ∫ 1 2 − 3 11.49 1 3 ∫ t 1 1 2 ​ ( 1 − t 1) ω ⁡ ( 1 − t 1 − t 2 t 2) t 1 ​ t 2 2 ​ d ​ t 2 ​ d ​ t 1) ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\ (1+o(1))\frac{2G_{1}}{e^{\gamma}}\left(\int_{\frac{1}{2}-\frac{3}{11.49}}^{\frac{1}{3}}\int_{t_{1}}^{\frac{1}{2}(1-t_{1})}\frac{\omega\left(\frac{1-t_{1}-t_{2}}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 1.30656 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 1.30656\frac{C(N)N}{(\log N)^{2}}, |  | (28) |

where

 | G 1 = \displaystyle G_{1}= | 500 ​ F ​ ( 500 ​ ϑ 1 500) − 500 ​ ∫ 1 500 25 128 f ⁡ ( 500 ​ ( ϑ 1 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t \displaystyle\ 500F\left(500\boldsymbol{\vartheta}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{25}{128}}\frac{f(500(\boldsymbol{\vartheta}_{1}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt |  |

 |  | + 500 ∫ 1 500 25 128 ∫ 1 500 t 1 F ⁡ ( 500 ​ ( ϑ 1 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{25}{128}}\int_{\frac{1}{500}}^{t_{1}}\frac{F(500(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 25 128 ∫ 1 500 t 1 ∫ 1 500 t 2 f ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1 \displaystyle-\int_{\frac{1}{500}}^{\frac{25}{128}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1} |  |

 | < \displaystyle< | 6.06932. \displaystyle\ 6.06932. |  | (29) |

Similarly, for S 12 S_{12} and S 13 S_{13} we have

 | S 12 ⩽ \displaystyle S_{12}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 ​ G 1 e γ ​ ( ∫ 1 11.49 1 3 ∫ 1 3 1 2 ​ ( 1 − t 1) ω ⁡ ( 1 − t 1 − t 2 t 2) t 1 ​ t 2 2 ​ d ​ t 2 ​ d ​ t 1) ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\ (1+o(1))\frac{2G_{1}}{e^{\gamma}}\left(\int_{\frac{1}{11.49}}^{\frac{1}{3}}\int_{\frac{1}{3}}^{\frac{1}{2}(1-t_{1})}\frac{\omega\left(\frac{1-t_{1}-t_{2}}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 3.912436 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 3.912436\frac{C(N)N}{(\log N)^{2}}, |  | (30) |

 | S 13 ⩽ \displaystyle S_{13}\leqslant | ( 1 + o ⁡ ( 1)) ​ 2 ​ G 1 e γ ​ ( ∫ 1 6.18 1 2 − 3 11.49 ∫ 1 2 − 3 11.49 1 2 ​ ( 1 − t 1) 1 t 1 ​ t 2 ​ ( 1 − t 1 − t 2) ​ d ​ t 2 ​ d ​ t 1) ​ C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\ (1+o(1))\frac{2G_{1}}{e^{\gamma}}\left(\int_{\frac{1}{6.18}}^{\frac{1}{2}-\frac{3}{11.49}}\int_{\frac{1}{2}-\frac{3}{11.49}}^{\frac{1}{2}(1-t_{1})}\frac{1}{t_{1}t_{2}(1-t_{1}-t_{2})}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 2.835087 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 2.835087\frac{C(N)N}{(\log N)^{2}}. |  | (31) |

For S 14 S_{14} and S 15 S_{15}, we shall use a device that has been used a lot in Harman’s sieve. Since p 3 > p 4 p_{3}>p_{4}, we have

 |  | ∑ N 1 11.49 ⩽ p 4 < p 3 < p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2 ​ p 3 ​ p 4, N) = 1 S ⁡ ( 𝒜 p 1 ​ p 2 ​ p 3 ​ p 4, 𝒫 ⁡ ( N), p 3) \displaystyle\sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{4}<p_{3}<p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2}p_{3}p_{4},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(N),p_{3}\right) |  |

 | ⩽ \displaystyle\leqslant | ∑ N 1 11.49 ⩽ p 4 < p 3 < p 2 < p 1 < N 1 6.18 ( p 1 ​ p 2 ​ p 3 ​ p 4, N) = 1 S ⁡ ( 𝒜 p 1 ​ p 2 ​ p 3 ​ p 4, 𝒫 ⁡ ( N), p 4). \displaystyle\ \sum_{\begin{subarray}{c}N^{\frac{1}{11.49}}\leqslant p_{4}<p_{3}<p_{2}<p_{1}<N^{\frac{1}{6.18}}\\ (p_{1}p_{2}p_{3}p_{4},N)=1\end{subarray}}S\left(\mathcal{A}_{p_{1}p_{2}p_{3}p_{4}};\mathcal{P}(N),p_{4}\right). |  | (32) |

Here we can apply Lemma 2.1 with r = 4 r=4 to handle part of the sum on the right–hand side of (32) if ( D 1, …, D 4) ∈ 𝐃 4 w ​ e ​ l ​ l ​ ( D) (D_{1},\ldots,D_{4})\in\mathbf{D}_{4}^{well}(D). We use the similar arguments as above to deal with other parts. Thus, we have

 | S 14 ⩽ \displaystyle S_{14}\leqslant | ( 1 + o ( 1)) ( ∫ 1 11.49 1 6.18 ∫ 1 11.49 t 1 ∫ 1 11.49 t 2 ∫ 1 11.49 t 3 ( Boole [( D 1, …, D 4) ∈ 𝐃 4 w ​ e ​ l ​ l ( D)] × \displaystyle\ (1+o(1))\left(\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\int_{\frac{1}{11.49}}^{t_{1}}\int_{\frac{1}{11.49}}^{t_{2}}\int_{\frac{1}{11.49}}^{t_{3}}\left(\texttt{Boole}[(D_{1},\ldots,D_{4})\in\mathbf{D}_{4}^{well}(D)]\times\right.\right. |  |

 |  | min ⁡ ( 2 e γ ​ F ⁡ ( ( ϑ 1 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3 − t 4) t 4) t 1 ​ t 2 ​ t 3 ​ t 4 2, 2 ​ G 1 e γ ​ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 3) t 1 ​ t 2 ​ t 3 2 ​ t 4) \displaystyle\qquad\qquad\qquad\min\left(\frac{2}{e^{\gamma}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3}-t_{4})}{t_{4}}\right)}{t_{1}t_{2}t_{3}t_{4}^{2}},\frac{2G_{1}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}t_{4}}\right) |  |

 |  | + Boole [( D 1, …, D 4) ∉ 𝐃 4 w ​ e ​ l ​ l ( D)] 2 ​ G 1 e γ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 3) t 1 ​ t 2 ​ t 3 2 ​ t 4) d t 4 d t 3 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\qquad\qquad\qquad+\ \texttt{Boole}[(D_{1},\ldots,D_{4})\notin\mathbf{D}_{4}^{well}(D)]\frac{2G_{1}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}t_{4}}\right)dt_{4}dt_{3}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.193502 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 0.193502\frac{C(N)N}{(\log N)^{2}}. |  | (33) |

Similarly, for S 15 S_{15} we have

 | S 15 ⩽ \displaystyle S_{15}\leqslant | ( 1 + o ( 1)) ( ∫ 1 11.49 1 6.18 ∫ t 1 1 6.18 ∫ t 2 1 6.18 ∫ 1 6.18 1 2 − 2 11.49 − t 3 ( Boole [( D 4, …, D 1) ∈ 𝐃 4 w ​ e ​ l ​ l ( D)] × \displaystyle\ (1+o(1))\left(\int_{\frac{1}{11.49}}^{\frac{1}{6.18}}\int_{t_{1}}^{\frac{1}{6.18}}\int_{t_{2}}^{\frac{1}{6.18}}\int_{\frac{1}{6.18}}^{\frac{1}{2}-\frac{2}{11.49}-t_{3}}\left(\texttt{Boole}[(D_{4},\ldots,D_{1})\in\mathbf{D}_{4}^{well}(D)]\times\right.\right. |  |

 |  | min ⁡ ( 2 e γ ​ F ⁡ ( ( ϑ 1 ​ ( t 4, t 3, t 2) − t 1 − t 2 − t 3 − t 4) t 1) t 1 2 ​ t 2 ​ t 3 ​ t 4, 2 ​ G 1 e γ ​ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 2) t 1 ​ t 2 2 ​ t 3 ​ t 4) \displaystyle\qquad\qquad\qquad\min\left(\frac{2}{e^{\gamma}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{1}(t_{4},t_{3},t_{2})-t_{1}-t_{2}-t_{3}-t_{4})}{t_{1}}\right)}{t_{1}^{2}t_{2}t_{3}t_{4}},\frac{2G_{1}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{2}}\right)}{t_{1}t_{2}^{2}t_{3}t_{4}}\right) |  |

 |  | + Boole [( D 4, …, D 1) ∉ 𝐃 4 w ​ e ​ l ​ l ( D)] 2 ​ G 1 e γ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 2) t 1 ​ t 2 2 ​ t 3 ​ t 4) d t 4 d t 3 d t 2 d t 1) C ⁡ ( N) ​ N ( log ⁡ N) 2 \displaystyle\left.\left.\qquad\qquad\qquad+\ \texttt{Boole}[(D_{4},\ldots,D_{1})\notin\mathbf{D}_{4}^{well}(D)]\frac{2G_{1}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{2}}\right)}{t_{1}t_{2}^{2}t_{3}t_{4}}\right)dt_{4}dt_{3}dt_{2}dt_{1}\right)\frac{C(N)N}{(\log N)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.183611 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. \displaystyle\ 0.183611\frac{C(N)N}{(\log N)^{2}}. |  | (34) |

Finally, by Lemma 3.1 and (9)–(34) we get

 | 4 ​ D 1, 2 ​ ( N) ⩾ \displaystyle 4D_{1,2}(N)\geqslant | ( 3 ​ S 1 + S 2 + S 8 + S 9 + S 10) \displaystyle\ (3S_{1}+S_{2}+S_{8}+S_{9}+S_{10}) |  |

 |  | − ( 2 ​ S 3 + S 4 + S 5 + S 6 + S 7 + 2 ​ S 11 + S 12 + S 13 + S 14 + S 15) \displaystyle-(2S_{3}+S_{4}+S_{5}+S_{6}+S_{7}+2S_{11}+S_{12}+S_{13}+S_{14}+S_{15}) |  |

 | ⩾ \displaystyle\geqslant | 7.8912 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2, \displaystyle\ 7.8912\frac{C(N)N}{(\log N)^{2}}, |  |

 | D 1, 2 ​ ( N) ⩾ 1.9728 ​ C ⁡ ( N) ​ N ( log ⁡ N) 2. D_{1,2}(N)\geqslant 1.9728\frac{C(N)N}{(\log N)^{2}}. |  |

Theorem 1.1 is proved. Since the detail of the proof of Theorem 1.2 is similar to those of Theorem 1.1 and Theorem 1.1 in [14] so we omit it in this paper.

## 5. Proof of Theorem 1.3

In this section, sets ℬ \mathcal{B} and 𝒫 \mathcal{P} are defined respectively. For S 1 ′ S^{\prime}_{1} and S 2 ′ S^{\prime}_{2}, by Buchstab’s identity, we have

 | S 1 ′ = S ⁡ ( ℬ, 𝒫, x 1 12) = \displaystyle S^{\prime}_{1}=S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{12}}\right)= | S ⁡ ( ℬ, 𝒫, x 1 500) − ∑ x 1 500 ⩽ p < x 1 12 S ⁡ ( ℬ p, 𝒫, x 1 500) \displaystyle\ S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{500}}\right)-\sum_{x^{\frac{1}{500}}\leqslant p<x^{\frac{1}{12}}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{500}}\right) |  |

 |  | + ∑ x 1 500 ⩽ p 2 < p 1 < x 1 12 S ( ℬ p 1 ​ p 2; 𝒫, x 1 500) \displaystyle+\sum_{x^{\frac{1}{500}}\leqslant p_{2}<p_{1}<x^{\frac{1}{12}}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P},x^{\frac{1}{500}}\right) |  |

 |  | − ∑ x 1 500 ⩽ p 3 < p 2 < p 1 < x 1 12 S ( ℬ p 1 ​ p 2 ​ p 3; 𝒫, p 3) \displaystyle-\sum_{x^{\frac{1}{500}}\leqslant p_{3}<p_{2}<p_{1}<x^{\frac{1}{12}}}S\left(\mathcal{B}_{p_{1}p_{2}p_{3}};\mathcal{P},p_{3}\right) |  | (35) |

and

 | S 2 ′ = S ⁡ ( ℬ, 𝒫, x 1 7.2) = \displaystyle S^{\prime}_{2}=S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{7.2}}\right)= | S ⁡ ( ℬ, 𝒫, x 1 500) − ∑ x 1 500 ⩽ p < x 1 7.2 S ⁡ ( ℬ p, 𝒫, x 1 500) \displaystyle\ S\left(\mathcal{B};\mathcal{P},x^{\frac{1}{500}}\right)-\sum_{x^{\frac{1}{500}}\leqslant p<x^{\frac{1}{7.2}}}S\left(\mathcal{B}_{p};\mathcal{P},x^{\frac{1}{500}}\right) |  |

 |  | + ∑ x 1 500 ⩽ p 2 < p 1 < x 1 7.2 S ( ℬ p 1 ​ p 2; 𝒫, x 1 500) \displaystyle+\sum_{x^{\frac{1}{500}}\leqslant p_{2}<p_{1}<x^{\frac{1}{7.2}}}S\left(\mathcal{B}_{p_{1}p_{2}};\mathcal{P},x^{\frac{1}{500}}\right) |  |

 |  | − ∑ x 1 500 ⩽ p 3 < p 2 < p 1 < x 1 7.2 S ( ℬ p 1 ​ p 2 ​ p 3; 𝒫, p 3). \displaystyle-\sum_{x^{\frac{1}{500}}\leqslant p_{3}<p_{2}<p_{1}<x^{\frac{1}{7.2}}}S\left(\mathcal{B}_{p_{1}p_{2}p_{3}};\mathcal{P},p_{3}\right). |  | (36) |

By Lemma 2.3, Iwaniec’s linear sieve method and arguments in [16], [15] and [13] we have

 | S 1 ′ ⩾ \displaystyle S^{\prime}_{1}\geqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( 500 ​ f ​ ( 500 ​ ϑ 1 500 ′) − 500 ​ ∫ 1 500 1 12 F ⁡ ( 500 ​ ( ϑ 0 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t CLOSE \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(500f\left(500\boldsymbol{\vartheta}^{\prime}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{1}{12}}\frac{F(500(\boldsymbol{\vartheta}_{0}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt\right. |  |

 |  | + 500 ∫ 1 500 1 12 ∫ 1 500 t 1 f ⁡ ( 500 ​ ( ϑ 0 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{1}{12}}\int_{\frac{1}{500}}^{t_{1}}\frac{f(500(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 1 12 ∫ 1 500 t 1 ∫ 1 500 t 2 F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.-\int_{\frac{1}{500}}^{\frac{1}{12}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 6.737439 ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\ 6.737439\frac{C_{2}x}{(\log x)^{2}} |  | (37) |

and

 | S 2 ′ ⩾ \displaystyle S^{\prime}_{2}\geqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( 500 ​ f ​ ( 500 ​ ϑ 1 500 ′) − 500 ​ ∫ 1 500 1 7.2 F ⁡ ( 500 ​ ( ϑ 0 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t CLOSE \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(500f\left(500\boldsymbol{\vartheta}^{\prime}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{1}{7.2}}\frac{F(500(\boldsymbol{\vartheta}_{0}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt\right. |  |

 |  | + 500 ∫ 1 500 1 7.2 ∫ 1 500 t 1 f ⁡ ( 500 ​ ( ϑ 0 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{1}{7.2}}\int_{\frac{1}{500}}^{t_{1}}\frac{f(500(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 1 7.2 ∫ 1 500 t 1 ∫ 1 500 t 2 F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.-\int_{\frac{1}{500}}^{\frac{1}{7.2}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 4.011646 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 4.011646\frac{C_{2}x}{(\log x)^{2}}, |  | (38) |

where ϑ 1 500 ′ = 2497 4000 \boldsymbol{\vartheta}^{\prime}_{\frac{1}{500}}=\frac{2497}{4000}. For S 3 ′ S^{\prime}_{3} – S 7 ′ S^{\prime}_{7}, by Lemma 2.3, Iwaniec’s linear sieve method and above discussion, we have

 | S 3 ′ ⩾ \displaystyle S^{\prime}_{3}\geqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( ∫ 1 12 1 7.2 ∫ 1 12 t 1 max ⁡ ( 12 ​ f ⁡ ( 12 ​ ( ϑ 0 ​ ( t 1, t 2, 1 12) − t 1 − t 2)) t 1 ​ t 2 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(\int_{\frac{1}{12}}^{\frac{1}{7.2}}\int_{\frac{1}{12}}^{t_{1}}\max\left(12\frac{f(12(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{12})-t_{1}-t_{2}))}{t_{1}t_{2}},\right.\right. |  |

 |  | max 12 ⩽ k ⩽ 500 ⁡ ( k ​ f ⁡ ( k ⁡ ( ϑ 0 ​ ( t 1, t 2, 1 k) − t 1 − t 2)) t 1 ​ t 2 CLOSE \displaystyle\max_{12\leqslant k\leqslant 500}\left(k\frac{f(k(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{k})-t_{1}-t_{2}))}{t_{1}t_{2}}\right. |  |

 |  | − ∫ 1 k 1 12 F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3)) d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\left.-\int_{\frac{1}{k}}^{\frac{1}{12}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}\right)\right)dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 0.875194 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 0.875194\frac{C_{2}x}{(\log x)^{2}}, |  | (39) |

 | S 4 ′ ⩾ \displaystyle S^{\prime}_{4}\geqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( ∫ 1 7.2 1 4 ∫ 1 12 1 7.2 max ⁡ ( 12 ​ f ⁡ ( 12 ​ ( ϑ 0 ​ ( t 1, t 2, 1 12) − t 1 − t 2)) t 1 ​ t 2 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(\int_{\frac{1}{7.2}}^{\frac{1}{4}}\int_{\frac{1}{12}}^{\frac{1}{7.2}}\max\left(12\frac{f(12(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{12})-t_{1}-t_{2}))}{t_{1}t_{2}},\right.\right. |  |

 |  | max 12 ⩽ k ⩽ 500 ⁡ ( k ​ f ⁡ ( k ⁡ ( ϑ 0 ​ ( t 1, t 2, 1 k) − t 1 − t 2)) t 1 ​ t 2 CLOSE \displaystyle\max_{12\leqslant k\leqslant 500}\left(k\frac{f(k(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{k})-t_{1}-t_{2}))}{t_{1}t_{2}}\right. |  |

 |  | − ∫ 1 k 1 12 F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3)) d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\left.-\int_{\frac{1}{k}}^{\frac{1}{12}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}\right)\right)dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 1.917212 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 1.917212\frac{C_{2}x}{(\log x)^{2}}, |  | (40) |

 | S 5 ′ ⩾ \displaystyle S^{\prime}_{5}\geqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( 12 ​ ∫ 1 12 1 7.2 ∫ 1 4 min ⁡ ( 2 7, 17 42 − t 1) f ⁡ ( 12 ​ ( ϑ 0 ​ ( t 2) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 ​ d ​ t 1) ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(12\int_{\frac{1}{12}}^{\frac{1}{7.2}}\int_{\frac{1}{4}}^{\min\left(\frac{2}{7},\frac{17}{42}-t_{1}\right)}\frac{f(12(\boldsymbol{\vartheta}_{0}(t_{2})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩾ \displaystyle\geqslant | 0.282826 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 0.282826\frac{C_{2}x}{(\log x)^{2}}, |  | (41) |

 | S 6 ′ ⩽ \displaystyle S^{\prime}_{6}\leqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( ∫ 1 12 1 4 min ⁡ ( 12 ​ F ⁡ ( 12 ​ ( ϑ 0 ​ ( t 1, 1 12, 1 12) − t 1)) t 1 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(\int_{\frac{1}{12}}^{\frac{1}{4}}\min\left(12\frac{F(12(\boldsymbol{\vartheta}_{0}(t_{1},\frac{1}{12},\frac{1}{12})-t_{1}))}{t_{1}},\right.\right. |  |

 |  | min 12 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 0 ​ ( t 1, 1 k, 1 k) − t 1)) t 1 − k ​ ∫ 1 k 1 12 f ⁡ ( k ⁡ ( ϑ 0 ​ ( t 1, t 2, 1 k) − t 1 − t 2)) t 1 ​ t 2 ​ d ​ t 2 CLOSE \displaystyle\min_{12\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{0}(t_{1},\frac{1}{k},\frac{1}{k})-t_{1}))}{t_{1}}-k\int_{\frac{1}{k}}^{\frac{1}{12}}\frac{f(k(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{k})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}\right. |  |

 |  | + ∫ 1 k 1 12 ∫ 1 k t 2 F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2)) d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\left.+\int_{\frac{1}{k}}^{\frac{1}{12}}\int_{\frac{1}{k}}^{t_{2}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}\right)\right)dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 7.410929 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 7.410929\frac{C_{2}x}{(\log x)^{2}}, |  | (42) |

 | S 7 ′ ⩽ \displaystyle S^{\prime}_{7}\leqslant | ( 1 + o ⁡ ( 1)) ​ 1 e γ ​ ( ∫ 1 4 2 7 min ⁡ ( 12 ​ F ⁡ ( 12 ​ ( ϑ 0 ​ ( t 1) − t 1)) t 1 CLOSE CLOSE, \displaystyle\ (1+o(1))\frac{1}{e^{\gamma}}\left(\int_{\frac{1}{4}}^{\frac{2}{7}}\min\left(12\frac{F(12(\boldsymbol{\vartheta}_{0}(t_{1})-t_{1}))}{t_{1}},\right.\right. |  |

 |  | OPEN OPEN min 12 ⩽ k ⩽ 500 ⁡ ( k ​ F ⁡ ( k ⁡ ( ϑ 0 ​ ( t 1) − t 1)) t 1 − ∫ 1 k 1 12 f ⁡ ( ( ϑ 0 ​ ( t 1) − t 1 − t 2) t 2) t 1 ​ t 2 2 ​ d ​ t 2)) ​ d ​ t 1) ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\min_{12\leqslant k\leqslant 500}\left(k\frac{F(k(\boldsymbol{\vartheta}_{0}(t_{1})-t_{1}))}{t_{1}}-\int_{\frac{1}{k}}^{\frac{1}{12}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1})-t_{1}-t_{2})}{t_{2}}\right)}{t_{1}t_{2}^{2}}dt_{2}\right)\right)dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.925271 ​ C 2 ​ x ( log ⁡ x) 2. \displaystyle\ 0.925271\frac{C_{2}x}{(\log x)^{2}}. |  | (43) |

For S 12 ′ S^{\prime}_{12} – S 16 ′ S^{\prime}_{16}, by Chen’s switching principle, Lemma 2.4 and above arguments on estimating S 11 S_{11} – S 15 S_{15} we have

 | S 12 ′ ⩽ \displaystyle S^{\prime}_{12}\leqslant | ( 1 + o ⁡ ( 1)) ​ G 2 e γ ​ ( ∫ 2 11 log ⁡ ( 2 − 3 t + 1) t ​ 𝑑 t) ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\ (1+o(1))\frac{G_{2}}{e^{\gamma}}\left(\int_{2}^{11}\frac{\log\left(2-\frac{3}{t+1}\right)}{t}dt\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 1.960955 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 1.960955\frac{C_{2}x}{(\log x)^{2}}, |  | (44) |

 | S 13 ′ ⩽ \displaystyle S^{\prime}_{13}\leqslant | ( 1 + o ⁡ ( 1)) ​ G 2 e γ ​ ( ∫ 2.5 6.2 log ⁡ ( 2.5 − 3.5 t + 1) t ​ 𝑑 t) ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\ (1+o(1))\frac{G_{2}}{e^{\gamma}}\left(\int_{2.5}^{6.2}\frac{\log\left(2.5-\frac{3.5}{t+1}\right)}{t}dt\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 1.699112 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 1.699112\frac{C_{2}x}{(\log x)^{2}}, |  | (45) |

 | S 14 ′ ⩽ \displaystyle S^{\prime}_{14}\leqslant | ( 1 + o ⁡ ( 1)) ​ G 2 e γ ​ ( ∫ 2 2.5 log ⁡ ( t − 1) t ​ 𝑑 t) ​ C 2 ​ x ( log ⁡ x) 2 \displaystyle\ (1+o(1))\frac{G_{2}}{e^{\gamma}}\left(\int_{2}^{2.5}\frac{\log(t-1)}{t}dt\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.152213 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 0.152213\frac{C_{2}x}{(\log x)^{2}}, |  | (46) |

 | S 15 ′ ⩽ \displaystyle S^{\prime}_{15}\leqslant | ( 1 + o ( 1)) ( ∫ 1 12 1 7.2 ∫ 1 12 t 1 ∫ 1 12 t 2 ∫ 1 12 t 3 ( Boole [( D 1, …, D 4) ∈ 𝐃 4 w ​ e ​ l ​ l ( D)] × \displaystyle\ (1+o(1))\left(\int_{\frac{1}{12}}^{\frac{1}{7.2}}\int_{\frac{1}{12}}^{t_{1}}\int_{\frac{1}{12}}^{t_{2}}\int_{\frac{1}{12}}^{t_{3}}\left(\texttt{Boole}[(D_{1},\ldots,D_{4})\in\mathbf{D}_{4}^{well}(D)]\times\right.\right. |  |

 |  | min ⁡ ( 1 e γ ​ F ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3 − t 4) t 4) t 1 ​ t 2 ​ t 3 ​ t 4 2, G 2 e γ ​ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 3) t 1 ​ t 2 ​ t 3 2 ​ t 4) \displaystyle\qquad\qquad\qquad\min\left(\frac{1}{e^{\gamma}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3}-t_{4})}{t_{4}}\right)}{t_{1}t_{2}t_{3}t_{4}^{2}},\frac{G_{2}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}t_{4}}\right) |  |

 |  | + Boole [( D 1, …, D 4) ∉ 𝐃 4 w ​ e ​ l ​ l ( D)] G 2 e γ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 3) t 1 ​ t 2 ​ t 3 2 ​ t 4) d t 4 d t 3 d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\qquad\qquad\qquad+\ \texttt{Boole}[(D_{1},\ldots,D_{4})\notin\mathbf{D}_{4}^{well}(D)]\frac{G_{2}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}t_{4}}\right)dt_{4}dt_{3}dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.031709 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 0.031709\frac{C_{2}x}{(\log x)^{2}}, |  | (47) |

 | S 16 ′ ⩽ \displaystyle S^{\prime}_{16}\leqslant | ( 1 + o ( 1)) ( ∫ 1 12 1 7.2 ∫ t 1 1 7.2 ∫ t 2 1 7.2 ∫ 1 7.2 min ⁡ ( 2 7, 17 42 − t 3) ( Boole [( D 4, …, D 1) ∈ 𝐃 4 w ​ e ​ l ​ l ( D)] × \displaystyle\ (1+o(1))\left(\int_{\frac{1}{12}}^{\frac{1}{7.2}}\int_{t_{1}}^{\frac{1}{7.2}}\int_{t_{2}}^{\frac{1}{7.2}}\int_{\frac{1}{7.2}}^{\min\left(\frac{2}{7},\frac{17}{42}-t_{3}\right)}\left(\texttt{Boole}[(D_{4},\ldots,D_{1})\in\mathbf{D}_{4}^{well}(D)]\times\right.\right. |  |

 |  | min ⁡ ( 1 e γ ​ F ⁡ ( ( ϑ 0 ​ ( t 4, t 3, t 2) − t 1 − t 2 − t 3 − t 4) t 1) t 1 2 ​ t 2 ​ t 3 ​ t 4, G 2 e γ ​ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 2) t 1 ​ t 2 2 ​ t 3 ​ t 4) \displaystyle\qquad\qquad\qquad\min\left(\frac{1}{e^{\gamma}}\frac{F\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{4},t_{3},t_{2})-t_{1}-t_{2}-t_{3}-t_{4})}{t_{1}}\right)}{t_{1}^{2}t_{2}t_{3}t_{4}},\frac{G_{2}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{2}}\right)}{t_{1}t_{2}^{2}t_{3}t_{4}}\right) |  |

 |  | + Boole [( D 4, …, D 1) ∉ 𝐃 4 w ​ e ​ l ​ l ( D)] G 2 e γ ω ⁡ ( 1 − t 1 − t 2 − t 3 − t 4 t 2) t 1 ​ t 2 2 ​ t 3 ​ t 4) d t 4 d t 3 d t 2 d t 1) C 2 ​ x ( log ⁡ x) 2 \displaystyle\left.\left.\qquad\qquad\qquad+\ \texttt{Boole}[(D_{4},\ldots,D_{1})\notin\mathbf{D}_{4}^{well}(D)]\frac{G_{2}}{e^{\gamma}}\frac{\omega\left(\frac{1-t_{1}-t_{2}-t_{3}-t_{4}}{t_{2}}\right)}{t_{1}t_{2}^{2}t_{3}t_{4}}\right)dt_{4}dt_{3}dt_{2}dt_{1}\right)\frac{C_{2}x}{(\log x)^{2}} |  |

 | ⩽ \displaystyle\leqslant | 0.245969 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ 0.245969\frac{C_{2}x}{(\log x)^{2}}, |  | (48) |

where

 | G 2 = \displaystyle G_{2}= | 500 ​ F ​ ( 500 ​ ϑ 1 500 ′) − 500 ​ ∫ 1 500 1 5 f ⁡ ( 500 ​ ( ϑ 0 ​ ( t, 1 500, 1 500) − t)) t ​ 𝑑 t \displaystyle\ 500F\left(500\boldsymbol{\vartheta}^{\prime}_{\frac{1}{500}}\right)-500\int_{\frac{1}{500}}^{\frac{1}{5}}\frac{f(500(\boldsymbol{\vartheta}_{0}(t,\frac{1}{500},\frac{1}{500})-t))}{t}dt |  |

 |  | + 500 ∫ 1 500 1 5 ∫ 1 500 t 1 F ⁡ ( 500 ​ ( ϑ 0 ​ ( t 1, t 2, 1 500) − t 1 − t 2)) t 1 ​ t 2 d t 2 d t 1 \displaystyle+500\int_{\frac{1}{500}}^{\frac{1}{5}}\int_{\frac{1}{500}}^{t_{1}}\frac{F(500(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},\frac{1}{500})-t_{1}-t_{2}))}{t_{1}t_{2}}dt_{2}dt_{1} |  |

 |  | − ∫ 1 500 1 5 ∫ 1 500 t 1 ∫ 1 500 t 2 f ⁡ ( ( ϑ 0 ​ ( t 1, t 2, t 3) − t 1 − t 2 − t 3) t 3) t 1 ​ t 2 ​ t 3 2 d t 3 d t 2 d t 1. \displaystyle-\int_{\frac{1}{500}}^{\frac{1}{5}}\int_{\frac{1}{500}}^{t_{1}}\int_{\frac{1}{500}}^{t_{2}}\frac{f\left(\frac{(\boldsymbol{\vartheta}_{0}(t_{1},t_{2},t_{3})-t_{1}-t_{2}-t_{3})}{t_{3}}\right)}{t_{1}t_{2}t_{3}^{2}}dt_{3}dt_{2}dt_{1}. |  |

 | < \displaystyle< | 5.81637. \displaystyle\ 5.81637. |  | (49) |

For the remaining terms, by the arguments in [3] and [22], we have

 | S 8 ′ ≪ \displaystyle S^{\prime}_{8}\ll | ε ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ \frac{\varepsilon C_{2}x}{(\log x)^{2}}, |  | (50) |

 | S 9 ′ ⩽ \displaystyle S^{\prime}_{9}\leqslant | ( 1 + o ⁡ ( 1)) ​ 12 e γ ​ ( ∫ ( 11 20 − 29 100) ​ 12 ( 4 7 − 2 7) ​ 12 F ⁡ ( t) 2 × 12 − t ​ 𝑑 t) ⩽ 0.111039 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ (1+o(1))\frac{12}{e^{\gamma}}\left(\int_{(\frac{11}{20}-\frac{29}{100})12}^{(\frac{4}{7}-\frac{2}{7})12}\frac{F(t)}{2\times 12-t}dt\right)\leqslant 0.111039\frac{C_{2}x}{(\log x)^{2}}, |  | (51) |

 | S 10 ′ ⩽ \displaystyle S^{\prime}_{10}\leqslant | ( 1 + o ⁡ ( 1)) ​ 12 e γ ​ ( ∫ ( 11 20 − 1 3) ​ 12 ( 11 20 − 29 100) ​ 12 F ⁡ ( t) 11 20 × 12 − t ​ 𝑑 t) ⩽ 1.169696 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle\ (1+o(1))\frac{12}{e^{\gamma}}\left(\int_{(\frac{11}{20}-\frac{1}{3})12}^{(\frac{11}{20}-\frac{29}{100})12}\frac{F(t)}{\frac{11}{20}\times 12-t}dt\right)\leqslant 1.169696\frac{C_{2}x}{(\log x)^{2}}, |  | (52) |

 | S 11 ′ ≪ \displaystyle S^{\prime}_{11}\ll | ε ​ C 2 ​ x ( log ⁡ x) 2. \displaystyle\ \frac{\varepsilon C_{2}x}{(\log x)^{2}}. |  | (53) |

Finally, by Lemma 3.2 and (35)–(53) we get

 | 4 ​ π 1, 2 ​ ( x) ⩾ \displaystyle 4\pi_{1,2}(x)\geqslant | ( 3 ​ S 1 ′ + S 2 ′ + S 3 ′ + S 4 ′ + S 5 ′) \displaystyle(3S^{\prime}_{1}+S^{\prime}_{2}+S^{\prime}_{3}+S^{\prime}_{4}+S^{\prime}_{5}) |  |

 |  | − ( 2 ​ S 6 ′ + 2 ​ S 7 ′ + S 8 ′ + S 9 ′ + S 10 ′ + S 11 ′ + S 12 ′ + S 13 ′ CLOSE \displaystyle-(2S^{\prime}_{6}+2S^{\prime}_{7}+S^{\prime}_{8}+S^{\prime}_{9}+S^{\prime}_{10}+S^{\prime}_{11}+S^{\prime}_{12}+S^{\prime}_{13} |  |

 |  | OPEN + 2 ​ S 14 ′ + S 15 ′ + S 16 ′ + S 17 ′ + S 18 ′ + S 19 ′) \displaystyle+2S^{\prime}_{14}+S^{\prime}_{15}+S^{\prime}_{16}+S^{\prime}_{17}+S^{\prime}_{18}+S^{\prime}_{19}) |  |

 | ⩾ \displaystyle\geqslant | 5.1036 ​ C 2 ​ x ( log ⁡ x) 2, \displaystyle 5.1036\frac{C_{2}x}{(\log x)^{2}}, |  |

 | π 1, 2 ​ ( x) ⩾ 1.2759 ​ C 2 ​ x ( log ⁡ x) 2. \pi_{1,2}(x)\geqslant 1.2759\frac{C_{2}x}{(\log x)^{2}}. |  |

Theorem 1.3 is proved.

## Acknowledgements

The author would like to thank Jiamin Li for some helpful discussions.

## References

- [1] Y. Cai. A remark on Chen’s theorem. Acta Arith., 102(4):339–352, 2002.
- [2] Y. Cai. On Chen’s theorem. II. J. Number Theory, 128(5):1336–1357, 2008.
- [3] Y. Cai. A remark on Chen’s theorem (II). Chinese Ann. Math. Ser. B, 29(6):687–698, 2008.
- [4] Y. Cai and M. Lu. On Chen’s theorem. In Analytic number theory (Beijing/Kyoto, 1999), volume 6 of Dev. Math., pages 99–119. Kluwer Acad. Publ., Dordrecht, 2002.
- [5] J. R. Chen. On the representation of a larger even integer as the sum of a prime and the product of at most two primes. Sci. Sinica, 16:157–176, 1973.
- [6] J. R. Chen. Further improvement on the constant in the proposition ‘1+2’: On the representation of a large even integer as the sum of a prime and the product of at most two primes (II). Sci. Sinica, pages 477–494(in Chinese), 1978.
- [7] J. R. Chen. On the representation of a large even integer as the sum of a prime and the product of at most two primes. II. Sci. Sinica, 21(4):421–430, 1978.
- [8] J. R. Chen. On some problems in prime number theory. In Séminaire de théorie des nombres, Paris 1979-80, pages 167–170. Birkhäuser, Boston, 1981.
- [9] E. Fouvry and F. Grupp. On the switching principle in sieve theory. J. Reine Angew. Math., 1986(370):101–126, 1986.
- [10] H. Halberstam. A proof of Chen’s theorem. In Journées Arithmétiques de Bordeaux (Conf., Univ. Bordeaux, 1974),, Astérisque, No. 24–25,, pages 281–293. ,, 1975.
- [11] H. Halberstam and H.-E. Richert. Sieve methods, volume No. 4. Academic Press [Harcourt Brace Jovanovich, Publishers], London-New York, 1974.
- [12] H. H. Kim. Functoriality for the exterior square of G ​ L 4 GL_{4} and the symmetric fourth of G ​ L 2 GL_{2}, with appendix 1 by D. Ramakrishnan and appendix 2 by H. H. Kim and P. Sarnak. J. Amer. Math. Soc., 16:139–183, 2003.
- [13] R. Li. On Chen’s theorem, Goldbach’s conjecture and almost prime twins. arXiv e-prints, page arXiv:2405.05727v3, 2024.
- [14] R. Li. Remarks on additive representations of natural numbers. arXiv e-prints, page arXiv:2309.03218v6, 2024.
- [15] J. D. Lichtman. Primes in arithmetic progressions to large moduli, and Goldbach beyond the square–root barrier. arXiv e-prints, page arXiv:2309.08522v1, 2023.
- [16] J. D. Lichtman. A modification of the linear sieve, and the count of twin primes. Algebra & Number Theory, 19:1–38, 2025.
- [17] H.-Q. Liu. On the prime twins problem. Sci. Sinica, 33(3):281–298, 1990.
- [18] A. Pascadi. On the exponents of distribution of primes and smooth numbers. arXiv e-prints, page arXiv:2505.00653v1, 2025.
- [19] P. M. Ross. On linear combinations of primes and numbers having at most two prime factors. Ph.D. Thesis, University of London, 1976.
- [20] J. Wu. Sur la suite des nombres premiers jumeaux. Acta Arith., 55(4):365–394, 1990.
- [21] J. Wu. Chen’s double sieve, Goldbach’s conjecture and the twin prime problem. Acta Arith., 114(3):215–273, 2004.
- [22] J. Wu. Chen’s double sieve, Goldbach’s conjecture and the twin prime problem. II. Acta Arith., 131(4):367–387, 2008.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:runbo.li.carey@gmail.com
