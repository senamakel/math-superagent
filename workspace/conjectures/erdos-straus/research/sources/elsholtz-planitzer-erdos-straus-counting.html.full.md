<!-- source: https://arxiv.org/html/1805.02945 | converted from HTML -->

The number of solutions of the Erdős-Straus Equation and sums of k unit fractions

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1805.02945v1 [math.NT] 08 May 2018

# The number of solutions of the Erdős-Straus Equation and sums of k k unit fractions

Christian Elsholtz C. Elsholtz Graz University of Technology, Institute of Analysis and Number Theory, Kopernikusgasse 24/II, 8010 Graz, Austria Email address: [elsholtz@math.tugraz.at][3] and Stefan Planitzer S. Planitzer Graz University of Technology, Institute of Analysis and Number Theory, Kopernikusgasse 24/II, 8010 Graz, Austria Email address: [planitzer@math.tugraz.at][4]

###### Abstract.

We prove new upper bounds for the number of representations of an arbitrary rational number as a sum of three unit fractions. In particular, for fixed m m there are at most 𝒪 ϵ ​ ( n 3 / 5 + ϵ) \mathcal{O}_{\epsilon}(n^{\nicefrac{{3}}{{5}}+\epsilon}) solutions of m n = 1 a 1 + 1 a 2 + 1 a 3 \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}}. This improves upon a result of Browning and Elsholtz (2011) and extends a result of Elsholtz and Tao (2013) who proved this when m = 4 m=4 and n n is a prime. Moreover there exists an algorithm finding all solutions in expected running time 𝒪 ϵ ​ ( n ϵ ​ ( n 3 m 2) 1 / 5) \mathcal{O}_{\epsilon}\left(n^{\epsilon}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right), for any ϵ > 0 \epsilon>0. We also improve a bound on the maximum number of representations of a rational number as a sum of k k unit fractions. Furthermore, we also improve lower bounds. In particular we prove that for given m ∈ ℕ m\in\mathbb{N} in every reduced residue class e mod f e\bmod f there exist infinitely many primes p p such that the number of solutions of the equation m p = 1 a 1 + 1 a 2 + 1 a 3 \frac{m}{p}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}} is ≫ f, m exp ( ( 5 ​ log ⁡ 2 12 ​ lcm ⁡ ( m, f) + o f, m ( 1)) log ⁡ p log ⁡ log ⁡ p) \gg_{f,m}\exp\left(\left(\frac{5\log 2}{12\lcm(m,f)}+o_{f,m}(1)\right)\frac{\log p}{\log\log p}\right). Previously the best known lower bound of this type was of order ( log ⁡ p) 0.549 (\log p)^{0.549}.

###### 2010 Mathematics Subject Classification

Primary: 11D68, Secondary: 11D72

## 1. Introduction

We consider the problem of finding upper bounds for the number of solutions in positive integers a 1 a_{1}, a 2 a_{2} and a 3 a_{3} of equations of the form

(1) |  | m n = 1 a 1 + 1 a 2 + 1 a 3 \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}} |  |

where m, n ∈ ℕ m,n\in\mathbb{N} are fixed. In the case when m = 4 m=4 we call equation ( 1) Erdős-Straus equation. The Erdős-Straus conjecture states that this equation has at least one solution for any n > 1 n>1 (see [9] and [16] *D11 for classical results concerning the Erdős-Straus equation and several related problems, as well as [13] for a survey of the work of Erdős on egyptian fractions). Also the more general equation

(2) |  | m n = ∑ i = 1 k 1 a i \frac{m}{n}=\sum_{i=1}^{k}\frac{1}{a_{i}} |  |

for m, n ∈ ℕ m,n\in\mathbb{N} fixed and a 1, …, a k ∈ ℕ a_{1},\ldots,a_{k}\in\mathbb{N} received some attention. Browning and Elsholtz [5] found upper bounds for the number of solutions of ( 2). For the special case m = n = 1 m=n=1 they were able to improve a result of Sándor [27] and proved that there are at most c 0 ( 5 / 24 + ϵ) ​ 2 k c_{0}^{(\nicefrac{{5}}{{24}}+\epsilon)2^{k}} representations of 1 1 as a sum of k k unit fractions, for any ϵ > 0 \epsilon>0 and sufficiently large k k. Here c 0 = lim n → ∞ u n 2 − n = 1.264 ​ … c_{0}=\lim_{n\rightarrow\infty}u_{n}^{2^{-n}}=1.264\ldots where u 1 = 1 u_{1}=1 and u n + 1 = u n ​ ( u n + 1) u_{n+1}=u_{n}(u_{n}+1). On the other hand Konyagin [21] proved a lower bound of order exp ⁡ ( exp ⁡ ( ( ( log ⁡ 2) ​ ( log ⁡ 3) 3 + o ⁡ ( 1)) ​ k log ⁡ k)) \exp\left(\exp\left(\left(\frac{(\log 2)(\log 3)}{3}+o(1)\right)\frac{k}{\log k}\right)\right) for the number of these representations with distinct denominators. While the Erdős-Straus conjecture is about representing certain rational numbers as a sum of just three unit fractions, Martin [24] worked on representations of positive rationals as sums of many unit fractions. In particular he proved that every positive rational number r r has a representation of the form r = ∑ s ∈ S 1 s r=\sum_{s\in S}\frac{1}{s}, where the set S S contains a positive proportion of the integers less than any sufficiently large real number x x.

Chen et.al. [7] dealt with representations of 1 1 as a sum of k k distinct unit fractions where the denominators satisfy certain restrictions (like all of them being odd). Several results on representations of rational numbers as a sum of unit fractions with restrictions on the denominators can be found in the work of Graham [14, 15, 13]. Elsholtz [12] proved a lower bound of similar order as the one of Konyagin for the number of representations of 1 1 as a sum of k k distinct unit fractions with odd denominators.

For sums of k k unit fractions we adopt the notation of [5] and define f k ​ ( m, n) f_{k}(m,n) to be the number of solutions ( a 1, a 2, …, a k) ∈ ℕ k (a_{1},a_{2},\ldots,a_{k})\in\mathbb{N}^{k} of equation ( 2) with a 1 ≤ a 2 ≤ … ≤ a k a_{1}\leq a_{2}\leq\ldots\leq a_{k}, i.e.

 | f k ( m, n) = | { ( a 1, a 2, …, a k) ∈ ℕ k: m n = 1 a 1 + 1 a 2 + ⋯ + 1 a k, a 1 ≤ a 2 … ≤ a k } |. f_{k}(m,n)=\left|\left\{(a_{1},a_{2},\ldots,a_{k})\in\mathbb{N}^{k}:\frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{k}},a_{1}\leq a_{2}\ldots\leq a_{k}\right\}\right|. |  |

Concerning equation ( 1) with m = 4 m=4 the results of Elsholtz and Tao [9] show that the number of solutions f 3 ​ ( 4, n) f_{3}(4,n) is related to some divisor questions and is on average a power of log ⁡ n \log n (at least when n n is prime). It even seems possible that for fixed m ∈ ℕ m\in\mathbb{N} and any ϵ > 0 \epsilon>0 the number of representations of m n \frac{m}{n} as a sum of k k unit fractions is bounded by 𝒪 k, ϵ ​ ( n ϵ) \mathcal{O}_{k,\epsilon}(n^{\epsilon}). More details on this are informally and heuristically discussed in Section 3. For general m m and n n the best known upper bound on the number of solutions of ( 1) is due to Browning and Elsholtz [5] *Theorem 2 who proved an upper bound of order 𝒪 ϵ ​ ( n ϵ ​ ( n m) 2 / 3) \mathcal{O}_{\epsilon}(n^{\epsilon}\left(\frac{n}{m}\right)^{\nicefrac{{2}}{{3}}}). In the case of the Erdős-Straus equation with n = p n=p prime Elsholtz and Tao [9] *Proposition 1.7 have improved this bound to 𝒪 ϵ ​ ( p 3 / 5 + ϵ) \mathcal{O}_{\epsilon}(p^{\nicefrac{{3}}{{5}}+\epsilon}). It is known that this type of question is easier to study, when the denominator is prime.

Our main result will be the following theorem which provides an upper bound on the number of solutions of equation ( 1).

###### Theorem 1.

For any m, n ∈ ℕ m,n\in\mathbb{N} and any ϵ > 0 \epsilon>0 there are at most 𝒪 ϵ ​ ( n ϵ ​ ( n 3 m 2) 1 / 5) \mathcal{O}_{\epsilon}\left(n^{\epsilon}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right) solutions of the equation

 | m n = 1 a 1 + 1 a 2 + 1 a 3 \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}} |  |

in positive integers a 1 a_{1}, a 2 a_{2} and a 3 a_{3}.

Note that this improves upon the bound of Browning and Elsholtz in the range m ≪ n 1 / 4 m\ll n^{\nicefrac{{1}}{{4}}}. As a corollary we get that the Elsholtz-Tao bound for the number of solutions of the Erdős-Straus equation is true for arbitrary denominators n ∈ ℕ n\in\mathbb{N}.

###### Corollary 1.

The Erdős-Straus equation

 | 4 n = 1 a 1 + 1 a 2 + 1 a 3 \frac{4}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}} |  |

has at most 𝒪 ϵ ​ ( n 3 / 5 + ϵ) \mathcal{O}_{\epsilon}(n^{\nicefrac{{3}}{{5}}+\epsilon}) solutions in positive integers a 1 a_{1}, a 2 a_{2} and a 3 a_{3}.

We also prove the following algorithmic version of Theorem 1 with a matching upper bound for the expected running time 1 1 1 For a definition of expected running time see the proof of this corollary at the end of section 5..

###### Corollary 2.

There exists an algorithm with an expected running time of order 𝒪 ϵ ​ ( n ϵ ​ ( n 3 m 2) 1 / 5) \mathcal{O}_{\epsilon}\left(n^{\epsilon}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right), for any ϵ > 0 \epsilon>0, which lists all representations of the rational number m n \frac{m}{n} as a sum of three unit fractions. Furthermore all representations of m n \frac{m}{n} as a sum of k > 3 k>3 unit fractions may be found in expected time 𝒪 ϵ, k ​ ( n 2 k − 3 ​ ( 8 / 5 + ϵ) − 1) \mathcal{O}_{\epsilon,k}\left(n^{2^{k-3}(\nicefrac{{8}}{{5}}+\epsilon)-1}\right), for any ϵ > 0 \epsilon>0.

For sums of k k unit fractions we will prove the following result.

###### Theorem 2.

We have

 | f 4 ( m, n) ≪ ϵ n ϵ ( n 4 / 3 m 2 / 3 + n 28 / 17 m 8 / 5) f_{4}(m,n)\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}\right) |  |

and for any k ≥ 5 k\geq 5

 | f k ( m, n) ≪ ϵ ( k n) ϵ ( k 4 / 3 ​ n 2 m) 28 / 17 ⋅ 2 k − 5. f_{k}(m,n)\ll_{\epsilon}(kn)^{\epsilon}\left(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\right)^{\nicefrac{{28}}{{17}}\cdot 2^{k-5}}. |  |

Keeping in mind that 28 17 = 1.64705 ​ … \frac{28}{17}=1.64705\ldots, Theorem 2 may be compared with the following bounds from [5] *Theorem 3:

 | f 4 ​ ( m, n) \displaystyle f_{4}(m,n) | ≪ ϵ n ϵ ( n 4 / 3 m 2 / 3 + ( n m) 5 / 3), \displaystyle\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\left(\frac{n}{m}\right)^{\nicefrac{{5}}{{3}}}\right), |  |

 | f k ​ ( m, n) \displaystyle f_{k}(m,n) | ≪ ϵ ( k n) ϵ ( k 4 / 3 ​ n 2 m) 5 / 3 ⋅ 2 k − 5, for k ≥ 5. \displaystyle\ll_{\epsilon}(kn)^{\epsilon}\left(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\right)^{\nicefrac{{5}}{{3}}\cdot 2^{k-5}}\text{, for }k\geq 5. |  |

A well studied special case of Theorem 2 concerns representations of 1 1 as a sum of k k unit fractions. Browning and Elsholtz [5] mention several related problems which are studied in the literature and can be improved using better upper bounds on f k ​ ( m, n) f_{k}(m,n). We summarize these results in the following corollary.

###### Corollary 3.

1. (1)

For any ϵ > 0 \epsilon>0 we have that

 | f k ( 1, 1) ≪ ϵ k 7 / 51 ⋅ 2 k − 1 + ϵ. f_{k}(1,1)\ll_{\epsilon}k^{\nicefrac{{7}}{{51}}\cdot 2^{k-1}+\epsilon}. |  |

2. (2)

Let u n u_{n} be the sequence recursively defined by u 0 = 1 u_{0}=1 and u n + 1 = u n ​ ( u n + 1) u_{n+1}=u_{n}(u_{n}+1) and set c 0 = lim n → ∞ u n 2 − n c_{0}=\lim_{n\rightarrow\infty}u_{n}^{2^{-n}}. Then for ϵ > 0 \epsilon>0 and k ≥ k ⁡ ( ϵ) k\geq k(\epsilon) we have

 | f k ​ ( 1, 1) < c 0 ( 7 / 17 + ϵ) ​ 2 k − 1. f_{k}(1,1)<c_{0}^{(\nicefrac{{7}}{{17}}+\epsilon)2^{k-1}}. |  |

3. (3)

For ϵ > 0 \epsilon>0 and k ≥ k ⁡ ( ϵ) k\geq k(\epsilon) the number S ⁡ ( k) S(k) of positive integer solutions of the equation

 | 1 = ∑ i = 1 k 1 a i + 1 ∏ i = 1 k a i 1=\sum_{i=1}^{k}\frac{1}{a_{i}}+\frac{1}{\prod_{i=1}^{k}a_{i}} |  |

is bounded from above by c 0 ( 7 / 17 + ϵ) ​ 2 k c_{0}^{(\nicefrac{{7}}{{17}}+\epsilon)2^{k}}.

###### Proof.

The first assertion is an immediate consequence of Theorem 2. For the proof of the second statement we refer the reader to the proof of Theorem 4 in [5]. The only change necessary is plugging in the bound from Theorem 2 instead of [5] *Theorem 3 for the last 5 5 lines of the proof which amounts to just exchanging one exponent. The last statement follows from the first one and the observation that S ⁡ ( k) ≤ f k + 1 ​ ( 1, 1) S(k)\leq f_{k+1}(1,1). ∎

We note that the number of solutions of the equation 1 = ∑ 1 = 1 k 1 a i + 1 ∏ i = 1 k a i 1=\sum_{1=1}^{k}\frac{1}{a_{i}}+\frac{1}{\prod_{i=1}^{k}a_{i}} has applications to problems considered in [4].

Finally we deal with lower bounds. In [9] *Theorem 1.8 it is shown that we have

 | f 3 ​ ( 4, n) ≥ exp ⁡ ( ( log ⁡ 3 + o ⁡ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n) f_{3}(4,n)\geq\exp\left((\log 3+o(1))\frac{\log n}{\log\log n}\right) |  |

for infinitely many n ∈ ℕ n\in\mathbb{N} and that

 | f 3 ​ ( 4, n) ≥ exp ⁡ ( ( log ⁡ 3 2 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n) f_{3}(4,n)\geq\exp\left(\left(\frac{\log 3}{2}+o(1)\right)\log\log n\right) |  |

for all integers n n in a subset of the positive integers with density 1 1. The following theorem gives an improvement of these bounds which also give a limitation on improving the upper bounds for the number of solution of the Erdős-Straus equation and in the general case. For comparison we note that log ⁡ 3 = 1.09861 ​ … \log 3=1.09861\ldots, log ⁡ 3 2 = 0.54930 ​ … \frac{\log 3}{2}=0.54930\ldots and log ⁡ 6 = 1.79175 ​ … \log 6=1.79175\ldots.

###### Theorem 3.

For given m ∈ ℕ m\in\mathbb{N} there are infinitely many n ∈ ℕ n\in\mathbb{N} such that

 | f 3 ​ ( m, n) ≥ exp ⁡ ( ( log ⁡ 6 + o m ​ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n). f_{3}(m,n)\geq\exp\left((\log 6+o_{m}(1))\frac{\log n}{\log\log n}\right). |  |

Furthermore, for given m ∈ ℕ m\in\mathbb{N}, there exists a subset ℳ 1 \mathcal{M}_{1} of the integers with density one, such that for any n ∈ ℳ 1 n\in\mathcal{M}_{1}

 | f 3 ​ ( m, n) \displaystyle f_{3}(m,n) | ≥ ( 1 φ ⁡ ( m) + o ⁡ ( 1)) ​ exp ⁡ ( ( log ⁡ 3 + o m ​ ( 1)) ​ log ⁡ log ⁡ n) ⋅ log ⁡ log ⁡ n \displaystyle\geq\left(\frac{1}{\varphi(m)}+o(1)\right)\exp\left((\log 3+o_{m}(1))\log\log n\right)\cdot\log\log n |  |

 |  | ≫ ( log ⁡ n) log ⁡ 3 + o m ​ ( 1). \displaystyle\gg(\log n)^{\log 3+o_{m}(1)}. |  |

For the special case m = 4 m=4 and for integers n n in a set ℳ 2 ⊂ ℕ \mathcal{M}_{2}\subset\mathbb{N} with density one, the last bound may be improved to

 | f 3 ​ ( 4, n) ≥ exp ⁡ ( ( log ⁡ 6 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n). f_{3}(4,n)\geq\exp\left((\log 6+o(1))\log\log n\right). |  |

###### Remark 1.

Previous proofs of lower bounds of similar type as the ones in Theorem 3 constructed solutions from factorizations of n n. We get our improvement from additionally taking into account factorizations of a lot of shifts of n n. Hence our proof also shows that there are many values a 1 a_{1} admitting many pairs ( a 2, a 3) (a_{2},a_{3}). Here ‘many’ means exp ⁡ ( ( C + o m ​ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n) \exp\left((C+o_{m}(1))\frac{\log n}{\log\log n}\right), where the constant C C depends on which of the three lower bounds in Theorem 3 we consider.

We may ask if a lower bound on f 3 ​ ( m, n) f_{3}(m,n) of the first type in Theorem 3 does not only hold for infinitely many positive integers n n but also for infinitely many prime denominators p p. In [9] there was no lower bound of this type, but it was proved that f 3 ​ ( 4, p) ≫ ( log ⁡ p) 0.549 f_{3}(4,p)\gg(\log p)^{0.549} for almost all primes. We note that this result implies, using Dirichlet’s theorem on primes, the following corollary.

###### Corollary 4.

For every reduced residue class e mod f e\bmod f, i.e. gcd ⁡ ( e, f) = 1 \gcd(e,f)=1, there are infinitely many primes p p such that f 3 ​ ( 4, p) ≫ ( log ⁡ p) 0.549 f_{3}(4,p)\gg(\log p)^{0.549}, and p ≡ e mod f p\equiv e\bmod f.

Here we improve this corollary considerably.

###### Theorem 4.

For every m ∈ ℕ m\in\mathbb{N} and every reduced residue class e mod f e\bmod f there are infinitely many primes p ≡ e mod f p\equiv e\bmod f such that

 | f 3 ( m, p) ≫ f, m exp ( ( 5 ​ log ⁡ 2 12 ​ lcm ⁡ ( m, f) + o f, m ( 1)) log ⁡ p log ⁡ log ⁡ p). f_{3}(m,p)\gg_{f,m}\exp\left(\left(\frac{5\log 2}{12\lcm(m,f)}+o_{f,m}(1)\right)\frac{\log p}{\log\log p}\right). |  |

Here o f, m ​ ( 1) o_{f,m}(1) denotes a quantity depending on f f and m m which goes to zero as p p tends to infinity.

Using results of Harman [19, 20] one might be able to improve the factor 5 12 \frac{5}{12} in the exponent to 0.4736 0.4736.

## 2. Notation

As usual ℕ \mathbb{N} denotes the set of positive integers and ℙ \mathbb{P} the set of primes in ℕ \mathbb{N}. We denote the greatest common divisor and the least common multiple of n n elements a i ∈ ℕ a_{i}\in\mathbb{N} by gcd ⁡ ( a 1, a 2, …, a n) \gcd(a_{1},a_{2},\ldots,a_{n}) and lcm ⁡ ( a 1, a 2, …, a n) \lcm(a_{1},a_{2},\ldots,a_{n}) or ( a 1, a 2, …, a n) (a_{1},a_{2},\ldots,a_{n}) and [a 1, a 2, …, a n] [a_{1},a_{2},\ldots,a_{n}] for short. For integers d, n ∈ ℕ d,n\in\mathbb{N} we write d | n d|n if d d divides n n. We use the symbols 𝒪 \mathcal{O}, o o, ≪ \ll and ≫ \gg within the contexts of the well known Landau and Vinogradov notations where dependence of the implied constant on certain variables is indicated by a subscript. For any prime p ∈ ℙ p\in\mathbb{P} we define the function ν p: ℕ → ℕ ∪ { 0 } \nu_{p}:\mathbb{N}\rightarrow\mathbb{N}\cup\{0\} to be the p p -adic valuation, i.e. ν p ​ ( n) = a \nu_{p}(n)=a if and only if p a p^{a} is the highest power of p p dividing n n. By τ ⁡ ( n) \tau(n) and ω ⁡ ( n) \omega(n), as usual, we denote the number of divisors and the number of distinct prime divisors of n n. By τ ⁡ ( n, m) \tau(n,m), we denote the number of divisors of n n coprime to m m and τ ⁡ ( n, k, m) \tau(n,k,m), ω ⁡ ( n, k, m) \omega(n,k,m) denote the number of divisors (resp. distinct prime divisors) of n n in the residue class k mod m k\bmod m, where ( k, m) = 1 (k,m)=1. Finally, for two coprime integers a a and b b we denote by ord a ⁡ ( b) \ord_{a}(b) the least positive integer l l, such that b l ≡ 1 mod a b^{l}\equiv 1\bmod a.

## 3. Heuristics on f k ​ ( m, n) f_{k}(m,n)

We now informally discuss why f 3 ​ ( m, n) = 𝒪 ϵ ​ ( n ϵ) f_{3}(m,n)=\mathcal{O}_{\epsilon}(n^{\epsilon}) can be expected. In fact, as far as we are aware, this was first observed by Roger Heath-Brown (private communication with the first author in 1994). Let us first recall (see e.g. [28] *p. 201: Theorem 3) that a fraction m n \frac{m}{n} with gcd ⁡ ( m, n) = 1 \gcd(m,n)=1 is a sum of two unit fractions 1 a 1 + 1 a 2 \frac{1}{a_{1}}+\frac{1}{a_{2}} if and only if there exist two distinct, positive and coprime divisors d 1 d_{1} and d 2 d_{2} of n n such that d 1 + d 2 ≡ 0 mod m d_{1}+d_{2}\equiv 0\bmod m. We may deduce an upper bound of 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) for the number of representations of m n \frac{m}{n} as a sum of two unit fractions. Indeed from

(3) |  | m n = 1 a 1 + 1 a 2, \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}, |  |

by setting d = ( a 1, a 2) d=(a_{1},a_{2}) and a i ′ = a i d a_{i}^{\prime}=\frac{a_{i}}{d} for i ∈ { 1, 2 } i\in\{1,2\}, we see that

 | m ​ a 1 ′ ​ a 2 ′ ​ d = n ⁡ ( a 1 ′ + a 2 ′). ma_{1}^{\prime}a_{2}^{\prime}d=n(a_{1}^{\prime}+a_{2}^{\prime}). |  |

This implies that a 1 ′, a 2 ′ a_{1}^{\prime},a_{2}^{\prime} are divisors of n n, d d divides n ⁡ ( a 1 ′ + a 2 ′) < 2 ​ n 2 n(a_{1}^{\prime}+a_{2}^{\prime})<2n^{2} and any solution ( a 1, a 2) (a_{1},a_{2}) of ( 3) uniquely corresponds to a triple ( a 1 ′, a 2 ′, d) (a_{1}^{\prime},a_{2}^{\prime},d). The number ∑ a 1 ′, a 2 ′ | n τ ⁡ ( n ⁡ ( a 1 ′ + a 2 ′)) \sum_{a_{1}^{\prime},a_{2}^{\prime}|n}\tau(n(a_{1}^{\prime}+a_{2}^{\prime})) of such triples is bounded by 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) (see Lemma A below).

Studying m n = 1 a 1 + 1 a 2 + 1 a 3 \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}} with a 1 ≤ a 2 ≤ a 3 a_{1}\leq a_{2}\leq a_{3} one observes that

 | 1 a 1 < m n ≤ 3 a 1 \frac{1}{a_{1}}<\frac{m}{n}\leq\frac{3}{a_{1}} |  |

from which n m < a 1 ≤ 3 ​ n m \frac{n}{m}<a_{1}\leq\frac{3n}{m} follows. In view of

(4) |  | m n − 1 a 1 = m ​ a 1 − n n ​ a 1 = 1 a 2 + 1 a 3 \frac{m}{n}-\frac{1}{a_{1}}=\frac{ma_{1}-n}{na_{1}}=\frac{1}{a_{2}}+\frac{1}{a_{3}} |  |

there are at most 𝒪 ⁡ ( n m) \mathcal{O}\left(\frac{n}{m}\right) choices for a 1 a_{1}, and for given a 1 a_{1} there are at most d ⁡ ( n ​ a 1) = 𝒪 ϵ ​ ( n ϵ) d(na_{1})=\mathcal{O}_{\epsilon}(n^{\epsilon}) divisors of n ​ a 1 na_{1}. This shows that f 3 ​ ( m, n) = 𝒪 ϵ ​ ( n 1 + ϵ m) f_{3}(m,n)=\mathcal{O}_{\epsilon}\left(\frac{n^{1+\epsilon}}{m}\right) is a trivial upper bound. The real question is for how many values of a 1 a_{1} there can be at least one solution. For increasing a 1 a_{1}, even if n ​ a 1 na_{1} contains many divisors, the congruence d 1 + d 2 ≡ 0 mod m ​ a 1 − n d_{1}+d_{2}\equiv 0\bmod ma_{1}-n should become, on average, more difficult to satisfy if m ​ a 1 − n ≫ n ϵ ma_{1}-n\gg n^{\epsilon}. Therefore we expect that the number of a 1 a_{1} contributing at least one solution is 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}), so that f 3 ​ ( m, n) = 𝒪 ϵ ​ ( n 2 ​ ϵ) f_{3}(m,n)=\mathcal{O}_{\epsilon}(n^{2\epsilon}). Moreover equation ( 4) implies that for any given a 1 a_{1}, the number of solutions is about d ~ ​ ( m, n, a 1) \tilde{d}(m,n,a_{1}). Here d ~ ​ ( m, n, a 1) \tilde{d}(m,n,a_{1}) counts the number of pairs of coprime divisors d 1, d 2 d_{1},d_{2} of n ​ a 1 na_{1}, with d 1 + d 2 ≡ 0 mod m ​ a 1 − n d_{1}+d_{2}\equiv 0\bmod ma_{1}-n. Therefore f 3 ​ ( m, n) f_{3}(m,n) should be approximately ∑ a 1 d ~ ​ ( m, n, a 1) \sum_{a_{1}}\tilde{d}(m,n,a_{1}).

Similarly a completely trivial upper bound on f 4 ​ ( m, n) f_{4}(m,n) is as follows. With a 1 ≤ a 2 ≤ a 3 ≤ a 4 a_{1}\leq a_{2}\leq a_{3}\leq a_{4} it follows that n m < a 1 ≤ 4 ​ n m \frac{n}{m}<a_{1}\leq\frac{4n}{m} and hence

 | m ​ a 1 − n n ​ a 1 = m n − 1 a 1 = 1 a 2 + 1 a 3 + 1 a 4 ≤ 3 a 2. \frac{ma_{1}-n}{na_{1}}=\frac{m}{n}-\frac{1}{a_{1}}=\frac{1}{a_{2}}+\frac{1}{a_{3}}+\frac{1}{a_{4}}\leq\frac{3}{a_{2}}. |  |

From those bounds we easily deduce that a 2 ≤ 12 ​ n 2 m a_{2}\leq\frac{12n^{2}}{m}. With

 | m n − 1 a 1 − 1 a 2 = m ​ a 1 ​ a 2 − n ​ a 2 − n ​ a 1 n ​ a 1 ​ a 2 = 1 a 3 + 1 a 3, \frac{m}{n}-\frac{1}{a_{1}}-\frac{1}{a_{2}}=\frac{ma_{1}a_{2}-na_{2}-na_{1}}{na_{1}a_{2}}=\frac{1}{a_{3}}+\frac{1}{a_{3}}, |  |

with similar arguments as above, we deduce that f 4 ​ ( m, n) = 𝒪 ϵ ​ ( n 3 + ϵ m 2) f_{4}(m,n)=\mathcal{O}_{\epsilon}\left(\frac{n^{3+\epsilon}}{m^{2}}\right). For fixed m m the fact that our bound on f 4 ​ ( m, n) f_{4}(m,n) in Theorem 2 below is better than 𝒪 ⁡ ( n 2) \mathcal{O}(n^{2}) shows that, for most pairs ( a 1, a 2) (a_{1},a_{2}) and moreover, for most choices of a 2 ∈ [n m, 12 ​ n 2 m] a_{2}\in\left[\frac{n}{m},\frac{12n^{2}}{m}\right] there is no solution of m n = 1 a 1 + 1 a 2 + 1 a 3 + 1 a 4 \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}}+\frac{1}{a_{4}}. Here again, as soon as m ​ a 1 ​ a 2 − n ​ a 2 − n ​ a 1 ≫ n ϵ ma_{1}a_{2}-na_{2}-na_{1}\gg n^{\epsilon} one should not expect to have two divisors d 1, d 2 d_{1},d_{2} of n ​ a 1 ​ a 2 na_{1}a_{2} such that d 1 + d 2 ≡ 0 mod m ​ a 1 ​ a 2 − n ​ a 2 − n ​ a 1 d_{1}+d_{2}\equiv 0\bmod ma_{1}a_{2}-na_{2}-na_{1}. From this reasoning, also f k ​ ( m, n) = 𝒪 ϵ, k ​ ( n ϵ) f_{k}(m,n)=\mathcal{O}_{\epsilon,k}(n^{\epsilon}), for k ≥ 4 k\geq 4 seems to us a reasonable expectation.

The papers [5] and [9] studied parametric solutions of the diophantine equation ( 1). The reason why the result in [9] is superior in the case of n n being a prime is that here a full parametric solution (e.g. [26]) is much easier to work with. However, in this manuscript we develop parametric solutions of ( 1) and ( 2) from scratch. Some simplified version of this has been used in [11] and [9] *Section 11, but there the focus was to generate solutions with many parameters. Here we need to do kind of the opposite, namely to show that every solution comes from a number of parametric families.

The method we introduce should theoretically work for any diophantine equation as it expresses a k k -tuple of integers in a standard form. In practice it might work favorably if there is some inhomogeneous part as in

 | n = a 1 ​ a 2 ​ a 3 − a 1 − a 2. n=a_{1}a_{2}a_{3}-a_{1}-a_{2}. |  |

For prime values of n n in equation ( 1) there are several discussions of parametric solutions in the literature, e.g. by Rosati [26] and Aigner [1], see also Mordell’s book [25] *Chapter 30. For composite values n n there is no satisfactory treatment in the literature, and Section 5 below may be the most detailed study to date.

## 4. Patterns and relative greatest common divisors

Consider a solution ( a 1, a 2, …, a k) ∈ ℕ k (a_{1},a_{2},\ldots,a_{k})\in\mathbb{N}^{k} with a 1 ≤ a 2 ≤ … ≤ a k a_{1}\leq a_{2}\leq\ldots\leq a_{k} of equation ( 2) and set n i = ( a i, n) n_{i}=(a_{i},n), a i = n i ​ t i a_{i}=n_{i}t_{i} for i ∈ { 1, 2, …, k } i\in\{1,2,\ldots,k\}. We can thus rewrite equation ( 2) as

(5) |  | m n = ∑ i = 1 k 1 n i ​ t i. \frac{m}{n}=\sum_{i=1}^{k}{\frac{1}{n_{i}t_{i}}}. |  |

Later, when working on upper bounds for the number of solutions of equation ( 5) for k ∈ { 3, 4 } k\in\{3,4\}, we will fix a choice of ( n 1, n 2, …, n k) ∈ ℕ k (n_{1},n_{2},\ldots,n_{k})\in\mathbb{N}^{k}. For given m, n ∈ ℕ m,n\in\mathbb{N} we call such a choice the *pattern*of a solution of this equation. Note that for solutions corresponding to a given pattern ( n 1, n 2, …, n k) (n_{1},n_{2},\ldots,n_{k}) we have that ( n n i, t i) = 1 \left(\frac{n}{n_{i}},t_{i}\right)=1 for all i ∈ { 1, 2, …, k } i\in\{1,2,\ldots,k\}. As n i | n n_{i}|n the number of distinct patterns is 𝒪 k ​ ( n ϵ) \mathcal{O}_{k}(n^{\epsilon}) only.

Also, when dealing with equations of type ( 5) for k ∈ { 3, 4 } k\in\{3,4\} we will make heavy use of the concept of relative greatest common divisors as described by Elsholtz in [10] (for some ad hoc definition see also [11]). Relative greatest common divisors are a useful tool when studying divisibility relations among the t i t_{i} in ( 5).

Let I = { 1, 2, …, k } I=\{1,2,\ldots,k\} be the index set. Then we define the relative greatest common divisors of the positive integers t 1, t 2, …, t k t_{1},t_{2},\ldots,t_{k} recursively as follows:

 | x I = gcd ⁡ ( t 1, t 2, …, t k) x_{I}=\gcd(t_{1},t_{2},\ldots,t_{k}) |  |

and for any { i 1, i 2, … ​ i | J | } = J ⊆ I \{i_{1},i_{2},\ldots i_{|J|}\}=J\subseteq I, J ≠ ∅ J\neq\emptyset we set

 | x J = gcd ⁡ ( t i 1, t i 2, …, t i | J |) ∏ J ′ ⊆ I J ⊊ J ′ x J ′. x_{J}=\frac{\gcd(t_{i_{1}},t_{i_{2}},\ldots,t_{i_{|J|}})}{\prod_{\begin{subarray}{c}J^{\prime}\subseteq I\\ J\subsetneq J^{\prime}\end{subarray}}x_{J^{\prime}}}. |  |

For k ∈ { 3, 4 } k\in\{3,4\} we will later identify the elements x J x_{J} with J ⊆ I J\subseteq I with the elements x i, x i ​ j x_{i},x_{ij} and x i ​ j ​ k x_{ijk} where { i, j, k } = { 1, 2, 3 } \{i,j,k\}=\{1,2,3\} in the case when k = 3 k=3 and with the elements x i, x i ​ j, x i ​ j ​ k x_{i},x_{ij},x_{ijk} and x i ​ j ​ k ​ l x_{ijkl} with { i, j, k, l } = { 1, 2, 3, 4 } \{i,j,k,l\}=\{1,2,3,4\} when k = 4 k=4. With the relative greatest common divisors defined as above we have that

 | t i = ∏ J ⊆ I i ∈ J x J. t_{i}=\prod_{\begin{subarray}{c}J\subseteq I\\ i\in J\end{subarray}}x_{J}. |  |

A further very useful property of relative greatest common divisors is that ( x J, x K) = 1 (x_{J},x_{K})=1 if J ⊈ K J\nsubseteq K and K ⊈ J K\nsubseteq J. We prove this property as the following lemma (see also [10] *p. 2).

###### Lemma 1.

Let t 1, t 2, …, t k ∈ ℕ t_{1},t_{2},\ldots,t_{k}\in\mathbb{N}, J, K ⊆ { 1, 2, …, k } J,K\subseteq\{1,2,\ldots,k\}, J, K ≠ ∅ J,K\neq\emptyset and define the corresponding relative greatest common divisors x J x_{J} and x K x_{K} as above. If J ⊈ K J\nsubseteq K and K ⊈ J K\nsubseteq J then ( x J, x K) = 1 (x_{J},x_{K})=1.

###### Proof.

By assumption J ⊈ K J\nsubseteq K and K ⊈ J K\nsubseteq J and thus we have that J ⊊ J ∪ K J\subsetneq J\cup K and K ⊊ J ∪ K K\subsetneq J\cup K. We suppose that d = ( x J, x K) > 1 d=(x_{J},x_{K})>1 and choose an arbitrary prime divisor p | d p|d. Set L = J ∪ K L=J\cup K, J = { j 1, j 2, …, j | J | } J=\{j_{1},j_{2},\ldots,j_{|J|}\}, K = { k 1, k 2, …, k | K | } K=\{k_{1},k_{2},\ldots,k_{|K|}\}, L = { l 1, l 2, …, l | L | } L=\{l_{1},l_{2},\ldots,l_{|L|}\} and write

 | x J \displaystyle x_{J} | = ( t j 1, t j 2, …, t j | J |) ( ∏ J ′ ⊆ I J ⊊ J ′ L ⊈ J ′ x J ′) ⋅ x L ⋅ ( ∏ J ′ ⊆ I L ⊊ J ′ x J ′) ​, \displaystyle=\frac{(t_{j_{1}},t_{j_{2}},\ldots,t_{j_{|J|}})}{\left(\prod_{\begin{subarray}{c}J^{\prime}\subseteq{I}\\ J\subsetneq J^{\prime}\\ L\nsubseteq J^{\prime}\end{subarray}}x_{J^{\prime}}\right)\cdot x_{L}\cdot\left(\prod_{\begin{subarray}{c}J^{\prime}\subseteq I\\ L\subsetneq J^{\prime}\end{subarray}}x_{J^{\prime}}\right)}\text{, } |  |

 | x K \displaystyle x_{K} | = ( t k 1, t k 2, …, t k | K |) ( ∏ K ′ ⊆ I K ⊊ K ′ L ⊈ K ′ x K ′) ⋅ x L ⋅ ( ∏ K ′ ⊆ I L ⊊ K ′ x K ′). \displaystyle=\frac{(t_{k_{1}},t_{k_{2}},\ldots,t_{k_{|K|}})}{\left(\prod_{\begin{subarray}{c}K^{\prime}\subseteq{I}\\ K\subsetneq K^{\prime}\\ L\nsubseteq K^{\prime}\end{subarray}}x_{K^{\prime}}\right)\cdot x_{L}\cdot\left(\prod_{\begin{subarray}{c}K^{\prime}\subseteq I\\ L\subsetneq K^{\prime}\end{subarray}}x_{K^{\prime}}\right)}. |  |

With x L = ( t l 1, t l 2, …, t l | L |) ∏ L ′ ⊆ I L ⊊ L ′ x L ′ x_{L}=\frac{(t_{l_{1}},t_{l_{2}},\ldots,t_{l_{|L|}})}{\prod_{\begin{subarray}{c}L^{\prime}\subseteq I\\ L\subsetneq L^{\prime}\end{subarray}}x_{L^{\prime}}} this simplifies to

(6) |  | x J = ( t j 1, t j 2, …, t j | J |) ( ∏ J ′ ⊆ I J ⊊ J ′ L ⊈ J ′ x J ′) ⋅ ( t l 1, t l 2, …, t l | L |) ​, ​ x K = ( t k 1, t k 2, …, t k | K |) ( ∏ K ′ ⊆ I K ⊊ K ′ L ⊈ K ′ x K ′) ⋅ ( t l 1, t l 2, …, t l | L |). x_{J}=\frac{(t_{j_{1}},t_{j_{2}},\ldots,t_{j_{|J|}})}{\left(\prod_{\begin{subarray}{c}J^{\prime}\subseteq{I}\\ J\subsetneq J^{\prime}\\ L\nsubseteq J^{\prime}\end{subarray}}x_{J^{\prime}}\right)\cdot(t_{l_{1}},t_{l_{2}},\ldots,t_{l_{|L|}})}\text{, }x_{K}=\frac{(t_{k_{1}},t_{k_{2}},\ldots,t_{k_{|K|}})}{\left(\prod_{\begin{subarray}{c}K^{\prime}\subseteq{I}\\ K\subsetneq K^{\prime}\\ L\nsubseteq K^{\prime}\end{subarray}}x_{K^{\prime}}\right)\cdot(t_{l_{1}},t_{l_{2}},\ldots,t_{l_{|L|}})}. |  |

Let p α p^{\alpha} be the highest power of p p dividing the greatest common divisor of the terms ( t j 1, t j 2, …, t j | J |) (t_{j_{1}},t_{j_{2}},\ldots,t_{j_{|J|}}) and ( t k 1, t k 1, …, t k | K |) (t_{k_{1}},t_{k_{1}},\ldots,t_{k_{|K|}}). Thus p α p^{\alpha} is also the highest power of p p such that

 | p α | ( ( t j 1, t j 2, …, t j | J |), ( t k 1, t k 1, …, t k | K |)) = ( t l 1, t l 2, …, t l | L |). p^{\alpha}|((t_{j_{1}},t_{j_{2}},\ldots,t_{j_{|J|}}),(t_{k_{1}},t_{k_{1}},\ldots,t_{k_{|K|}}))=(t_{l_{1}},t_{l_{2}},\ldots,t_{l_{|L|}}). |  |

By definition of the greatest common divisor, without loss of generality we may suppose that ν p ​ ( (,,,,,,,)) = α \nu_{p}((t_{j_{1}},t_{j_{2}},\ldots,t_{j_{|J|}}))=\alpha. From equation ( 6) we finally see that ν p ​ ( x J) = 0 \nu_{p}(x_{J})=0, a contradiction to p | d p|d. ∎

Relative greatest common divisors may be nicely visualized via Venn diagrams (especially when k ≤ 3 k\leq 3). We identify a positive integers with the multiset of its prime divisors, i.e. each prime p p dividing n n occurs with multiplicity ν p ​ ( n) \nu_{p}(n) in the multiset. Given the Venn diagram of the multisets corresponding to the integers t 1, …, t k t_{1},\ldots,t_{k}, each area of intersection in the diagram uniquely corresponds to a relative greatest common divisor x J x_{J}, J ⊆ { 1, …, k } J\subseteq\{1,\ldots,k\}. Figure 1 shows the situation for relative greatest common divisors of three positive integers t 1, t 2 t_{1},t_{2} and t 3 t_{3}.

Figure 1. A visualization of relative greatest common divisors using Venn diagrams. On the left hand side one sees the general case of three positive integers t 1, t 2 t_{1},t_{2} and t 3 t_{3} and on the right hand side the situation when t 1 = 90 t_{1}=90, t 2 = 126 t_{2}=126 and t 3 = 616 t_{3}=616. Empty sets correspond to empty products and we set the corresponding relative greatest common divisor to 1 1.

As mentioned in the beginning of this section relative greatest common divisors were systematically described in [10]. Nonetheless concepts of a similar type date back at least as far as Dedekind [8] who called the relative greatest common divisors of the integers t 1, …, t k t_{1},\ldots,t_{k} the cores (Kerne) of the system ( t 1, …, t k) (t_{1},\ldots,t_{k}). Dedekind described the construction of these cores explicitly for systems with three and four elements and developed some theory to describe the cores of systems with more than four elements.

Decompositions similar to relative greatest common divisors also occur when we look for generalizations of the formula

(7) |  | [t 1, t 2] = t 1 ​ t 2 ( t 1, t 2), [t_{1},t_{2}]=\frac{t_{1}t_{2}}{(t_{1},t_{2})}, |  |

where [t 1, t 2] [t_{1},t_{2}] denotes the least common multiple of the integers t 1 t_{1} and t 2 t_{2}. A generalization of formula ( 7) to least common multiples and greatest common divisors of k k integers t 1, …, t k t_{1},\ldots,t_{k} was found by V.-A. Lebesgue [22] *p. 350, who proved that

 | [t 1, t 2, …, t k] = ∏ 1 ≤ i ≤ k i ​ odd G i ∏ 1 ≤ j ≤ k j ​ even G j, [t_{1},t_{2},\ldots,t_{k}]=\frac{\prod_{\begin{subarray}{c}1\leq i\leq k\\ i\text{ odd}\end{subarray}}G_{i}}{\prod_{\begin{subarray}{c}1\leq j\leq k\\ j\text{ even}\end{subarray}}G_{j}}, |  |

where the variables G i G_{i} denote the product of the greatest common divisors of all choices of subsets of i i integers in the set { t 1, t 2, …, t k }. \{t_{1},t_{2},\ldots,t_{k}\}.

## 5. Sums of three unit fractions

In this section we deal with equation ( 5) for k = 3 k=3, i.e. with equations of the form

(8) |  | m n = 1 n 1 ​ t 1 + 1 n 2 ​ t 2 + 1 n 3 ​ t 3, \frac{m}{n}=\frac{1}{n_{1}t_{1}}+\frac{1}{n_{2}t_{2}}+\frac{1}{n_{3}t_{3}}, |  |

where n 1 ​ t 1 ≤ n 2 ​ t 2 ≤ n 3 ​ t 3 n_{1}t_{1}\leq n_{2}t_{2}\leq n_{3}t_{3}, n i | n n_{i}|n and ( n n i, t i) = 1 \left(\frac{n}{n_{i}},t_{i}\right)=1 for i ∈ { 1, 2, 3 } i\in\{1,2,3\}. In the following we use the concept of relative greatest common divisors introduced in the previous section to get a suitable parametrisation of the solutions of ( 8) corresponding to a fixed pattern ( n 1, n 2, n 3) ∈ ℕ 3 (n_{1},n_{2},n_{3})\in\mathbb{N}^{3}.

Writing the variables t i t_{i} in terms of relative greatest common divisors, equation ( 8) takes the form

(9) |  | m n = 1 n 1 ​ x 1 ​ x 12 ​ x 13 ​ x 123 + 1 n 2 ​ x 2 ​ x 12 ​ x 23 ​ x 123 + 1 n 3 ​ x 3 ​ x 13 ​ x 23 ​ x 123 \frac{m}{n}=\frac{1}{n_{1}x_{1}x_{12}x_{13}x_{123}}+\frac{1}{n_{2}x_{2}x_{12}x_{23}x_{123}}+\frac{1}{n_{3}x_{3}x_{13}x_{23}x_{123}} |  |

and multiplying out yields

(10) |  | m ​ x 1 ​ x 2 ​ x 3 ​ x 12 ​ x 13 ​ x 23 ​ x 123 = n n 1 ​ x 2 ​ x 3 ​ x 23 + n n 2 ​ x 1 ​ x 3 ​ x 13 + n n 3 ​ x 1 ​ x 2 ​ x 12. mx_{1}x_{2}x_{3}x_{12}x_{13}x_{23}x_{123}=\frac{n}{n_{1}}x_{2}x_{3}x_{23}+\frac{n}{n_{2}}x_{1}x_{3}x_{13}+\frac{n}{n_{3}}x_{1}x_{2}x_{12}. |  |

A first thing we observe is that we have x i = 1 x_{i}=1 for all i ∈ { 1, 2, 3 } i\in\{1,2,3\}. This follows from Lemma 1 and equation ( 10) together with the fact that x i | n n i x_{i}|\frac{n}{n_{i}} is possible only if x i = 1 x_{i}=1 by definition of n i n_{i}. We thus can work with the following simplified version of equation ( 10)

(11) |  | m ​ x 12 ​ x 13 ​ x 23 ​ x 123 = n n 1 ​ x 23 + n n 2 ​ x 13 + n n 3 ​ x 12. mx_{12}x_{13}x_{23}x_{123}=\frac{n}{n_{1}}x_{23}+\frac{n}{n_{2}}x_{13}+\frac{n}{n_{3}}x_{12}. |  |

Next we introduce the parameters d i ​ j d_{ij} which are defined as d i ​ j = ( n n i, n n j) d_{ij}=\left(\frac{n}{n_{i}},\frac{n}{n_{j}}\right). Again we have that ( x i ​ j, d i ​ j) = 1 (x_{ij},d_{ij})=1 by definition of the n i n_{i} and we note that for given m, n m,n and a fixed pattern ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) also the parameters d i ​ j d_{ij} are fixed.

In what follows we apply methods developed by Elsholtz and Tao [9] *Sections 2 and 3. The strategy is to derive a system of equations from ( 11) and to make use of divisor relations therein. With the observation of coprimality of d i ​ j d_{ij} and x i ​ j x_{ij}, and using divisibility relations implied by equation ( 11) we may define the following three positive integers

 | w = n n 1 ​ d 13 ​ x 23 + n n 3 ​ d 13 ​ x 12 x 13 ​, ​ y = n n 1 ​ d 12 ​ x 23 + n n 2 ​ d 12 ​ x 13 x 12 ​ and ​ z = n n 2 ​ d 23 ​ x 13 + n n 3 ​ d 23 ​ x 12 x 23. w=\frac{\frac{n}{n_{1}d_{13}}x_{23}+\frac{n}{n_{3}d_{13}}x_{12}}{x_{13}}\text{, }y=\frac{\frac{n}{n_{1}d_{12}}x_{23}+\frac{n}{n_{2}d_{12}}x_{13}}{x_{12}}\text{ and }z=\frac{\frac{n}{n_{2}d_{23}}x_{13}+\frac{n}{n_{3}d_{23}}x_{12}}{x_{23}}. |  |

Later we make use of the product of w w and z z which is given by

 | w ​ z \displaystyle wz | = n n 1 ​ d 13 ​ n n 2 ​ d 23 + x 12 x 13 ​ x 23 ​ ( n 2 n 1 ​ n 3 ​ d 13 ​ d 23 ​ x 23 + n 2 n 2 ​ n 3 ​ d 13 ​ d 23 ​ x 13 + n 2 n 3 2 ​ d 13 ​ d 23 ​ x 12) \displaystyle=\frac{n}{n_{1}d_{13}}\frac{n}{n_{2}d_{23}}+\frac{x_{12}}{x_{13}x_{23}}\left(\frac{n^{2}}{n_{1}n_{3}d_{13}d_{23}}x_{23}+\frac{n^{2}}{n_{2}n_{3}d_{13}d_{23}}x_{13}+\frac{n^{2}}{n_{3}^{2}d_{13}d_{23}}x_{12}\right) |  |

 |  | = n n 1 ​ d 13 ​ n n 2 ​ d 23 + n ​ x 12 n 3 ​ d 13 ​ d 23 ​ x 13 ​ x 23 ​ ( n n 1 ​ x 23 + n n 2 ​ x 13 + n n 3 ​ x 12) \displaystyle=\frac{n}{n_{1}d_{13}}\frac{n}{n_{2}d_{23}}+\frac{nx_{12}}{n_{3}d_{13}d_{23}x_{13}x_{23}}\left(\frac{n}{n_{1}}x_{23}+\frac{n}{n_{2}}x_{13}+\frac{n}{n_{3}}x_{12}\right) |  |

 |  | = n n 1 ​ d 13 ​ n n 2 ​ d 23 + n ​ m n 3 ​ d 13 ​ d 23 ​ x 12 2 ​ x 123, \displaystyle=\frac{n}{n_{1}d_{13}}\frac{n}{n_{2}d_{23}}+\frac{nm}{n_{3}d_{13}d_{23}}x_{12}^{2}x_{123}, |  |

where we used equation ( 11) to get the last equality. We collect the equations just derived in the following list

(12) |  | m ​ x 12 ​ x 13 ​ x 23 ​ x 123 \displaystyle mx_{12}x_{13}x_{23}x_{123} | = n n 1 ​ x 23 + n n 2 ​ x 13 + n n 3 ​ x 12 \displaystyle=\frac{n}{n_{1}}x_{23}+\frac{n}{n_{2}}x_{13}+\frac{n}{n_{3}}x_{12} |  |

(13) |  | y ​ x 12 \displaystyle yx_{12} | = n n 1 ​ d 12 ​ x 23 + n n 2 ​ d 12 ​ x 13 \displaystyle=\frac{n}{n_{1}d_{12}}x_{23}+\frac{n}{n_{2}d_{12}}x_{13} |  |

(14) |  | z ​ x 23 \displaystyle zx_{23} | = n n 2 ​ d 23 ​ x 13 + n n 3 ​ d 23 ​ x 12 \displaystyle=\frac{n}{n_{2}d_{23}}x_{13}+\frac{n}{n_{3}d_{23}}x_{12} |  |

(15) |  | m ​ x 13 ​ x 23 ​ x 123 \displaystyle mx_{13}x_{23}x_{123} | = d 12 ​ y + n n 3 \displaystyle=d_{12}y+\frac{n}{n_{3}} |  |

(16) |  | m ​ x 12 ​ x 13 ​ x 123 \displaystyle mx_{12}x_{13}x_{123} | = d 23 ​ z + n n 1 \displaystyle=d_{23}z+\frac{n}{n_{1}} |  |

(17) |  | w ​ z \displaystyle wz | = n n 1 ​ d 13 ​ n n 2 ​ d 23 + n ​ m n 3 ​ d 13 ​ d 23 ​ x 12 2 ​ x 123. \displaystyle=\frac{n}{n_{1}d_{13}}\frac{n}{n_{2}d_{23}}+\frac{nm}{n_{3}d_{13}d_{23}}x_{12}^{2}x_{123}. |  |

For proving Theorem 1 the classical divisor bound will play a crucial role. We will use it in the following form (see [18] *Theorem 315).

###### Lemma A.

Let d ⁡ ( n): ℕ → ℕ d(n):\mathbb{N}\rightarrow\mathbb{N} be the divisor function, i.e. d ⁡ ( n) = ∑ d | n 1 d(n)=\sum_{d|n}1. Then for every ϵ > 0 \epsilon>0 we have

 | d ( n) ≪ ϵ n ϵ. d(n)\ll_{\epsilon}n^{\epsilon}. |  |

We now have all the tools we need to prove Theorem 1.

###### Proof of Theorem 1.

Consider a solution of equation ( 8) for a fixed pattern ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}). By assumption we have n 1 ​ t 1 ≤ n 2 ​ t 2 ≤ n 3 ​ t 3 n_{1}t_{1}\leq n_{2}t_{2}\leq n_{3}t_{3} and using the parametrization of the t i t_{i} we introduced in equation ( 9) this implies

 | x 13 ≤ n 2 n 1 ​ x 23 ​ and ​ x 12 ≤ n 3 n 2 ​ x 13. x_{13}\leq\frac{n_{2}}{n_{1}}x_{23}\text{ and }x_{12}\leq\frac{n_{3}}{n_{2}}x_{13}. |  |

Using these inequalities in equations ( 13) and ( 14) yields

 | y ​ x 12 ≤ 2 ​ n n 1 ​ d 12 ​ x 23 ​ and ​ z ​ x 23 ≤ 2 ​ n n 2 ​ d 23 ​ x 13. yx_{12}\leq 2\frac{n}{n_{1}d_{12}}x_{23}\text{ and }zx_{23}\leq 2\frac{n}{n_{2}d_{23}}x_{13}. |  |

Dividing by x 23 x_{23} and x 13 x_{13} respectively and multiplying the last two inequalities we arrive at

 | y ​ x 12 x 23 ​ z ​ x 23 x 13 ≤ 4 ​ n 2 n 1 ​ n 2 ​ d 12 ​ d 23. \frac{yx_{12}}{x_{23}}\frac{zx_{23}}{x_{13}}\leq 4\frac{n^{2}}{n_{1}n_{2}d_{12}d_{23}}. |  |

We now intend to obtain a lower bound for n 1 ​ n 2 ​ d 12 ​ d 23 n_{1}n_{2}d_{12}d_{23}. Let n = ∏ p ∈ ℙ p ν p ​ ( n) n=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n)} be the prime factorization of n n. Then n 1 = ∏ p ∈ ℙ p ν p ​ ( n 1) n_{1}=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n_{1})} and n 2 = ∏ p ∈ ℙ p ν p ​ ( n 2) n_{2}=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n_{2})} where 0 ≤ ν p ​ ( n 1), ν p ​ ( n 2) ≤ ν p ​ ( n) 0\leq\nu_{p}(n_{1}),\nu_{p}(n_{2})\leq\nu_{p}(n) for all p ∈ ℙ p\in\mathbb{P}. Since

 | d 12 = ( n n 1, n n 2) = ∏ p ∈ ℙ p ν p ​ ( n) − max ⁡ ( ν p ​ ( n 1), ν p ​ ( n 2)) d_{12}=\left(\frac{n}{n_{1}},\frac{n}{n_{2}}\right)=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n)-\max(\nu_{p}(n_{1}),\nu_{p}(n_{2}))} |  |

we have

 | n 1 ​ n 2 ​ d 12 \displaystyle n_{1}n_{2}d_{12} | = ∏ p ∈ ℙ p ν p ​ ( n 1) + ν p ​ ( n 2) + ν p ​ ( n) − max ⁡ ( ν p ​ ( n 1), ν p ​ ( n 2)) \displaystyle=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n_{1})+\nu_{p}(n_{2})+\nu_{p}(n)-\max(\nu_{p}(n_{1}),\nu_{p}(n_{2}))} |  |

 |  | ≥ ∏ p ∈ ℙ p ν p ​ ( n 1) + ν p ​ ( n 2) + ν p ​ ( n) − ν p ​ ( n 1) − ν p ​ ( n 2) = n. \displaystyle\geq\prod_{p\in\mathbb{P}}p^{\nu_{p}(n_{1})+\nu_{p}(n_{2})+\nu_{p}(n)-\nu_{p}(n_{1})-\nu_{p}(n_{2})}=n. |  |

This shows that n 1 ​ n 2 ​ d 12 ​ d 23 ≥ n n_{1}n_{2}d_{12}d_{23}\geq n and thus

 | y ​ x 12 x 23 ​ z ​ x 23 x 13 ≪ n. \frac{yx_{12}}{x_{23}}\frac{zx_{23}}{x_{13}}\ll n. |  |

By assumption we have that n 1 ​ t 1 n_{1}t_{1} is the smallest denominator in equation ( 8). This implies that

 | m n ≤ 3 n 1 ​ t 1 ​ and thus ​ t 1 ≤ 3 ​ n m ​ n 1 ≪ n m. \frac{m}{n}\leq\frac{3}{n_{1}t_{1}}\text{ and thus }t_{1}\leq\frac{3n}{mn_{1}}\ll\frac{n}{m}. |  |

The bound in Theorem 1 can finally be derived from the following inequality

(18) |  | y ⋅ z ⋅ x 12 ​ x 13 ⋅ ( x 12 ​ x 123) 2 = y ​ x 12 x 23 ​ z ​ x 23 x 13 ​ ( x 12 ​ x 13 ​ x 123) 2 ≪ n 3 m 2. y\cdot z\cdot x_{12}x_{13}\cdot(x_{12}x_{123})^{2}=\frac{yx_{12}}{x_{23}}\frac{zx_{23}}{x_{13}}(x_{12}x_{13}x_{123})^{2}\ll\frac{n^{3}}{m^{2}}. |  |

This implies that at least one of the factors y y, z z, x 12 ​ x 13 x_{12}x_{13} and x 12 ​ x 123 x_{12}x_{123} is bounded by 𝒪 ⁡ ( ( n 3 m 2) 1 / 5) \mathcal{O}\left(\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right).

If this is the case for y y then by Lemma A and equation ( 15) we have at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the parameters x 13 x_{13}, x 23 x_{23} and x 123 x_{123} for every choice of y y. The parameter x 12 x_{12} is then uniquely determined by ( 12).

Similarly, if z z is the bounded parameter use Lemma A and equation ( 16) to see that there are at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the parameters x 12 x_{12}, x 13 x_{13} and x 123 x_{123} for every choice of z z. Again the remaining parameter x 23 x_{23} is uniquely determined by ( 12).

Suppose that x 12 ​ x 13 ≪ ( n 3 m 2) 1 / 5 x_{12}x_{13}\ll\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}. By Lemma A for every fixed choice of x 12 ​ x 13 x_{12}x_{13} we may choose the factors x 12 x_{12} and x 13 x_{13} in at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) ways. For each of those choices Lemma A and equation ( 14) imply that there are at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the parameter x 23 x_{23}. As before the remaining parameter x 123 x_{123} is then fixed by ( 12).

Finally we need to consider the case when x 12 ​ x 123 x_{12}x_{123} is the bounded factor. As in the previous case for any fixed choice of x 12 ​ x 123 x_{12}x_{123} we have at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the factors x 12 x_{12} and x 123 x_{123}. Since equation ( 8) has no solutions for m > 3 ​ n m>3n we have that m ≪ n m\ll n and using equation ( 17) we see that for any fixed choice of x 12 x_{12} and x 123 x_{123} we have at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the parameters w w and z z. With z z, x 12 x_{12} and x 123 x_{123} fixed, x 13 x_{13} is uniquely determined by ( 16). The last parameter x 23 x_{23} is again uniquely determined by ( 12).

In any case we have a bounded number of applications of the divisor bound from Lemma A, say it was applied at most l l times. Setting ϵ ~ = l ​ ϵ \tilde{\epsilon}=l\epsilon we hence have at most 𝒪 ϵ ~ ​ ( n ϵ ~ ​ ( n 3 m 2) 1 / 5) \mathcal{O}_{\tilde{\epsilon}}\left(n^{\tilde{\epsilon}}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right) choices for the parameters x 12 x_{12}, x 13 x_{13}, x 23 x_{23} and x 123 x_{123} which uniquely determine a solution of ( 8) if n 1 n_{1}, n 2 n_{2} and n 3 n_{3} are fixed. Note that this bound is independent of the concrete choice of the parameters n i n_{i} and again by Lemma A we have at most 𝒪 ϵ ​ ( n 3 ​ ϵ) \mathcal{O}_{\epsilon}(n^{3\epsilon}) choices for the pattern ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}). Theorem 1 now follows by redefining the choice of ϵ \epsilon. ∎

Finally we prove Corollary 2.

###### Proof of Corollary 2.

The proof of Theorem 1 suggests an algorithm for computing all decompositions of a rational number m n \frac{m}{n} as a sum of three unit fractions. The running time of this algorithm depends on the quality of algorithms used for integer factorization. In [23] a probabilistic algorithm is analyzed which finds all prime factors of a given integer in expected running time exp ⁡ ( ( 1 + o ⁡ ( 1)) ​ log ⁡ n ​ log ⁡ log ​ n) \exp((1+o(1))\sqrt{\log n\log\log n}) for n → ∞ n\rightarrow\infty, which is clearly 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}). Here the term probabilistic means that the algorithm is allowed to call a random number generator which outputs 0 0 or 1 1 each with probability 1 2 \frac{1}{2}. The term expected running time refers to averaging over the output of the random number generator only and not over the input n n. Hence the expected running time is also valid for each individual n n.

As a consequence, using an algorithm of this type, all decompositions of m n \frac{m}{n} as a sum of three unit fractions can be found by carrying out the following steps. Factorize the integer n n and compute all possible patterns ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}). For any of these 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) patterns it follows from the calculations in the proof of Theorem 1, that the implied constant in inequality ( 18) may be chosen as C:= ( 36 n 1 2 ​ d 23) C:=\left(\frac{36}{n_{1}^{2}d_{23}}\right). For all choices of integers y y, z z, x 12 ​ x 13 x_{12}x_{13} and x 12 ​ x 123 ∈ [1, C 1 / 5 ​ ( n 3 m 2) 1 / 5] x_{12}x_{123}\in\left[1,C^{\nicefrac{{1}}{{5}}}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right] we determine the integers x 12, x 13, x 23 x_{12},x_{13},x_{23} and x 123 x_{123} via factoring x 12 ​ x 13 x_{12}x_{13}, x 12 ​ x 123 x_{12}x_{123} and a small number of integers mentioned in formulae ( 12)-( 17). All in all this leads to an algorithm of expected running time 𝒪 ϵ ​ ( n ϵ ​ ( n 3 m 2) 1 / 5) \mathcal{O}_{\epsilon}\left(n^{\epsilon}\left(\frac{n^{3}}{m^{2}}\right)^{\nicefrac{{1}}{{5}}}\right).

As for representations of the form

(19) |  | m n = ∑ i = 1 k 1 a i \frac{m}{n}=\sum_{i=1}^{k}\frac{1}{a_{i}} |  |

with k > 3 k>3 we enumerate all possible choices for the denominators a i a_{i}, 1 ≤ i ≤ k − 3 1\leq i\leq k-3, and apply our algorithm for finding representations as sum of three unit fractions to determine all choices for the remaining three denominators, i.e. we solve

(20) |  | m n − ∑ i = 1 k − 3 1 a i = 1 a k − 2 + 1 a k − 1 + 1 a k. \frac{m}{n}-\sum_{i=1}^{k-3}\frac{1}{a_{i}}=\frac{1}{a_{k-2}}+\frac{1}{a_{k-1}}+\frac{1}{a_{k}}. |  |

We suppose the denominators a i a_{i} in equation ( 19) are given in increasing order and prove upper bounds for the size of a i a_{i}, 1 ≤ i ≤ k 1\leq i\leq k. In particular we use an induction argument to show that a i ≤ α i ​ n 2 i − 1 a_{i}\leq\alpha_{i}n^{2^{i-1}} where the finite sequence ( α i) 1 ≤ i ≤ k (\alpha_{i})_{1\leq i\leq k} is recursively defined by α 1 = k \alpha_{1}=k and α i = ( k − i + 1) ​ ∏ j < i α j \alpha_{i}=(k-i+1)\prod_{j<i}\alpha_{j} for 2 ≤ i ≤ k 2\leq i\leq k. For i = 1 i=1 this bound follows easily from the following inequality

 | m n = 1 a 1 + ⋯ + 1 a k ≤ k a 1 \frac{m}{n}=\frac{1}{a_{1}}+\cdots+\frac{1}{a_{k}}\leq\frac{k}{a_{1}} |  |

which leads to a 1 ≤ k ​ n m ≤ k ​ n a_{1}\leq\frac{kn}{m}\leq kn. If we suppose the bound holds for a i a_{i}, with a similar argument we get

 | m n − 1 a 1 − ⋯ − 1 a i = 1 a i + 1 + ⋯ + 1 a k ≤ ( k − i) a i + 1. \frac{m}{n}-\frac{1}{a_{1}}-\cdots-\frac{1}{a_{i}}=\frac{1}{a_{i+1}}+\cdots+\frac{1}{a_{k}}\leq\frac{(k-i)}{a_{i+1}}. |  |

The last inequality together with the induction hypothesis for j < i + 1 j<i+1 implies

 | a i + 1 ≤ ( k − i) ​ n ​ ∏ j < i + 1 a j m ​ ∏ j < i + 1 a j − n ​ ∑ j < i + 1 ∏ l < i + 1 l ≠ j a l ≤ ( k − i) ​ n ​ ∏ j < i + 1 a j ≤ α i + 1 ​ n 2 i. a_{i+1}\leq(k-i)\frac{n\prod_{j<i+1}a_{j}}{m\prod_{j<i+1}a_{j}-n\sum_{j<i+1}\prod_{\begin{subarray}{c}l<i+1\\ l\neq j\end{subarray}}a_{l}}\leq(k-i)n\prod_{j<i+1}a_{j}\leq\alpha_{i+1}n^{2^{i}}. |  |

By definition α i \alpha_{i} is a polynomial in k k of degree 2 i 2^{i} with leading coefficient 1 1. Furthermore the denominator of the rational number on the left hand side of equation ( 20) is of size at most n ∏ i = 1 k − 3 a i ≪ k n 2 k − 3 n\prod_{i=1}^{k-3}a_{i}\ll_{k}n^{2^{k-3}}. By the aforementioned result we can compute all decompositions as a sum of three unit fractions of this number in time 𝒪 ϵ, k ​ ( n 2 k − 3 ​ ( 3 / 5 + ϵ)) \mathcal{O}_{\epsilon,k}(n^{2^{k-3}(\nicefrac{{3}}{{5}}+\epsilon)}). We have to compute these representations for at most ∏ i = 1 k − 3 a i ≪ k n 2 k − 3 − 1 \prod_{i=1}^{k-3}a_{i}\ll_{k}n^{2^{k-3}-1} rational numbers which leads to an upper bound of

 | 𝒪 ϵ, k ​ ( n 2 k − 3 ​ ( 8 / 5 + ϵ) − 1) \mathcal{O}_{\epsilon,k}\left(n^{2^{k-3}(\nicefrac{{8}}{{5}}+\epsilon)-1}\right) |  |

for the running time. ∎

###### Remark 2.

The procedure for computing representations as a sum of k k unit fractions as described in the proof of Corollary 2 could lead to a speedup for calculations similar to those in [2]. In the calculations above the size of the numerator of the rational number on the left hand side of equation ( 20), which we denote by m ′ n ′ \frac{m^{\prime}}{n^{\prime}}, was not taken into account. We note that also the proof of the upper bound for f 3 ​ ( m, n) f_{3}(m,n) by Browning and Elsholtz [5] *Theorem 2 may be similarly turned into an algorithm of running time 𝒪 ϵ ​ ( n ϵ ​ ( n m) 2 / 3) \mathcal{O}_{\epsilon}\left(n^{\epsilon}\left(\frac{n}{m}\right)^{\nicefrac{{2}}{{3}}}\right). In practice one would check dynamically if m ′ ≪ ( n ′) 1 / 4 m^{\prime}\ll(n^{\prime})^{\nicefrac{{1}}{{4}}} before computing the representations as a sum of three unit fractions of m ′ n ′ \frac{m^{\prime}}{n^{\prime}}. If this is the case, the algorithm described in the first part of the proof of Corollary 2 should be applied, if m ′ ≫ ( n ′) 1 / 4 m^{\prime}\gg(n^{\prime})^{\nicefrac{{1}}{{4}}} the method of [5] should be used.

## 6. Sums of k k unit fractions

In this section we will prove Theorem 2. Browning and Elsholtz used an induction argument on their bound for the quantity f 3 ​ ( m, n) f_{3}(m,n) to get bounds for f k ​ ( m, n) f_{k}(m,n) for k ≥ 4 k\geq 4. Using their arguments directly on our result from Theorem 1 would lead to worse upper bounds than those of Browning and Elsholtz. The reason is that our bound for f 3 ​ ( m, n) f_{3}(m,n) is weaker than the one in [5] when m m is large.

As in [5] *Section 4 the proof of Theorem 2 will be based on the observation that from equation ( 5) it follows that

 | f k ​ ( m, n) ≤ ∑ n m < n 1 ​ t 1 ≤ k ​ n m f k − 1 ​ ( m ​ n 1 ​ t 1 − n, n 1 ​ t 1 ​ n), f_{k}(m,n)\leq\sum_{\frac{n}{m}<n_{1}t_{1}\leq\frac{kn}{m}}f_{k-1}(mn_{1}t_{1}-n,n_{1}t_{1}n), |  |

which, after introducing the parameter u = m ​ n 1 ​ t 1 − n u=mn_{1}t_{1}-n, becomes

(21) |  | f k ​ ( m, n) ≤ ∑ 0 < u ≤ ( k − 1) ​ n m | u + n f k − 1 ​ ( u, n ⁡ ( u + n) m). f_{k}(m,n)\leq\sum_{\begin{subarray}{c}0<u\leq(k-1)n\\ m|u+n\end{subarray}}f_{k-1}\left(u,\frac{n(u+n)}{m}\right). |  |

The improvement in Theorem 2 stems from extending the method of Browning and Elsholtz by applying the following new idea. In the case of k = 4 k=4 we do not consider the sum on the right hand side of ( 21) as a whole but we split the sum into two parts. In the first part we collect the values of u u where 0 < u ≤ n δ 0<u\leq n^{\delta} for some 0 < δ < 1 0<\delta<1 which will be chosen later. This sum will be small since it contains few summands.

The second part will consist of all summands where u > n δ u>n^{\delta}. This corresponds to n 1 ​ t 1 > n + n δ m n_{1}t_{1}>\frac{n+n^{\delta}}{m} which will force n 2 ​ t 2 n_{2}t_{2} and n 3 ​ t 3 n_{3}t_{3} to be small.

The following Lemma B is [5] *Theorem 2.

###### Lemma B.

For any ϵ > 0 \epsilon>0, we have

 | f 3 ( m, n) ≪ ϵ n ϵ ( n m) 2 3. f_{3}(m,n)\ll_{\epsilon}n^{\epsilon}\left(\frac{n}{m}\right)^{\frac{2}{3}}. |  |

In the proof of Theorem 2 below we make use of Lemma B rather than Theorem 1. Furthermore we will use a lifting procedure which was first used by Browning and Elsholtz [5] to lift upper bounds of the form

(22) |  | f 5 ( m, n) ≪ ϵ n ϵ ( n 2 m) c f_{5}(m,n)\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{c} |  |

to upper bounds for f k ​ ( m, n) f_{k}(m,n) for k > 5 k>5. For possible future use we write this procedure up in the following lemma and work through the original proof by Browning and Elsholtz with an arbitrary exponent c > 1 c>1 in ( 22).

###### Lemma C.

Suppose that there exists c > 1 c>1 such that

 | f 5 ( m, n) ≪ ϵ n ϵ ( n 2 m) c. f_{5}(m,n)\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{c}. |  |

Then for any k ≥ 5 k\geq 5 we have

 | f k ( m, n) ≪ ϵ ( k n) ϵ ( k 4 / 3 ​ n 2 m) c ​ 2 k − 5. f_{k}(m,n)\ll_{\epsilon}(kn)^{\epsilon}\left(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\right)^{c2^{k-5}}. |  |

###### Proof.

We will inductively show that for k ≥ 5 k\geq 5 there exists Θ k \Theta_{k} depending on k k such that we have

(23) |  | f k ( m, n) ≪ ϵ ( k n) ϵ ( k Θ k ​ n 2 m) c ​ 2 k − 5 f_{k}(m,n)\ll_{\epsilon}(kn)^{\epsilon}\left(\frac{k^{\Theta_{k}}n^{2}}{m}\right)^{c2^{k-5}} |  |

and we note that this is certainly true for k = 5 k=5 by assumption. The proof works in three steps.

1. Establish an upper bound where the implied constant is allowed to depend on k k.

For k ≥ 5 k\geq 5 we want to have a bound of the form

(24) |  | f k ( m, n) ≪ k, ϵ n ϵ ( n 2 m) c ​ 2 k − 5 f_{k}(m,n)\ll_{k,\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{c2^{k-5}} |  |

where the implied constant is allowed to depend on k k. An upper bound of this type may easily be achieved via ( 21). Indeed this bound holds true for k = 5 k=5 by assumption and assuming its existence for f k ​ ( m, n) f_{k}(m,n) we find for f k + 1 ​ ( m, n) f_{k+1}(m,n)

 | f k + 1 ​ ( m, n) \displaystyle f_{k+1}(m,n) | ≪ ∑ 0 < u ≤ k ​ n m | u + n f k ( u, n ⁡ ( u + n) m) ≪ k, ϵ n ϵ ( n 2 m) c ​ 2 k − 4 ∑ u = 1 ∞ 1 u c ​ 2 k − 5 \displaystyle\ll\sum_{\begin{subarray}{c}0<u\leq kn\\ m|u+n\end{subarray}}f_{k}\left(u,\frac{n(u+n)}{m}\right)\ll_{k,\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}\sum_{u=1}^{\infty}\frac{1}{u^{c2^{k-5}}} |  |

 |  | ≪ k, ϵ n ϵ ( n 2 m) c ​ 2 k − 4, \displaystyle\ll_{k,\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}, |  |

where we used that c > 1 c>1.

2. Use inequality ( 21) and split the sum into two parts.

For the upper bound where the implied constant is independent of k k we again suppose it to be true for f k ​ ( m, n) f_{k}(m,n) with k ≥ 5 k\geq 5 and inductively prove it to hold for f k + 1 ​ ( m, n) f_{k+1}(m,n). Using inequalities ( 21) and ( 23) we get

 | f k + 1 ​ ( m, n) \displaystyle f_{k+1}(m,n) | ≪ ∑ 0 < u ≤ k ​ n m | u + n f k ​ ( u, n ⁡ ( u + n) m) \displaystyle\ll\sum_{\begin{subarray}{c}0<u\leq kn\\ m|u+n\end{subarray}}f_{k}\left(u,\frac{n(u+n)}{m}\right) |  |

 |  | ≪ ∑ 0 < u ≤ ( L − 1) ​ n m | u + n f k ​ ( u, n ⁡ ( u + n) m) + ∑ ( L − 1) ​ n < u ≤ k ​ n m | u + n f k ​ ( u, n ⁡ ( u + n) m) \displaystyle\ll\sum_{\begin{subarray}{c}0<u\leq(L-1)n\\ m|u+n\end{subarray}}f_{k}\left(u,\frac{n(u+n)}{m}\right)+\sum_{\begin{subarray}{c}(L-1)n<u\leq kn\\ m|u+n\end{subarray}}f_{k}\left(u,\frac{n(u+n)}{m}\right) |  |

 |  | ≪ ( k n) ϵ k Θ k ​ c ​ 2 k − 5 ( n 2 m) c ​ 2 k − 4 × \displaystyle\ll(kn)^{\epsilon}k^{\Theta_{k}c2^{k-5}}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}\times |  |

 |  | ( ∑ 0 < u ≤ ( L − 1) ​ n 1 u c ​ 2 k − 5 ​ L c ​ 2 k − 4 + ∑ ( L − 1) ​ n < u ≤ k ​ n 1 u c ​ 2 k − 5 ​ ( k + 1) c ​ 2 k − 4). \displaystyle\left(\sum_{0<u\leq(L-1)n}\frac{1}{u^{c2^{k-5}}}L^{c2^{k-4}}+\sum_{(L-1)n<u\leq kn}\frac{1}{u^{c2^{k-5}}}(k+1)^{c2^{k-4}}\right). |  |

Since c ​ 2 k − 5 > 1 c2^{k-5}>1 the infinite sums over 1 u c ​ 2 k − 5 \frac{1}{u^{c2^{k-5}}} converge. For the first sum we use that the sum is bounded by a constant for the second sum we use the following more accurate bound

 | ∑ ( L − 1) ​ n < u ≤ k ​ n 1 u c ​ 2 k − 5 ≤ ∑ u = L ∞ 1 u c ​ 2 k − 5 ≪ ∫ L ∞ 1 u c ​ 2 k − 5 ​ 𝑑 u ≪ L 1 − c ​ 2 k − 5. \sum_{(L-1)n<u\leq kn}\frac{1}{u^{c2^{k-5}}}\leq\sum_{u=L}^{\infty}\frac{1}{u^{c2^{k-5}}}\ll\int_{L}^{\infty}\frac{1}{u^{c2^{k-5}}}\mathrm{d}u\ll L^{1-c2^{k-5}}. |  |

Together with the fact that ( a + b) α ≥ a α + b α (a+b)^{\alpha}\geq a^{\alpha}+b^{\alpha} for a, b > 0 a,b>0 and α > 1 \alpha>1 this shows that

 | f k + 1 \displaystyle f_{k+1} | ( m, n) \displaystyle(m,n) |  |

 |  | ≪ ϵ ( ( k + 1) n) ϵ ( k + 1) Θ k ​ c ​ 2 k − 5 ( n 2 m) c ​ 2 k − 4 ( L c ​ 2 k − 4 + ( k + 1 L 1 / 2 − ( c ​ 2 k − 4) − 1) c ​ 2 k − 4) \displaystyle\ll_{\epsilon}((k+1)n)^{\epsilon}(k+1)^{\Theta_{k}c2^{k-5}}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}\left(L^{c2^{k-4}}+\left(\frac{k+1}{L^{\nicefrac{{1}}{{2}}-(c2^{k-4})^{-1}}}\right)^{c2^{k-4}}\right) |  |

 |  | ≪ ϵ ( ( k + 1) n) ϵ ( k + 1) Θ k ​ c ​ 2 k − 5 ( n 2 m) c ​ 2 k − 4 ( L + k + 1 L 1 / 2 − ( c ​ 2 k − 4) − 1) c ​ 2 k − 4. \displaystyle\ll_{\epsilon}((k+1)n)^{\epsilon}(k+1)^{\Theta_{k}c2^{k-5}}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}\left(L+\frac{k+1}{L^{\nicefrac{{1}}{{2}}-(c2^{k-4})^{-1}}}\right)^{c2^{k-4}}. |  |

3. Optimizing for L L and determining an upper bound for Θ k \Theta_{k}.

By the bound we derived in step 1 we may suppose that k ≥ max ⁡ { log ⁡ ( 2 3 ​ ( c ​ ϵ) − 1) log ⁡ 2 + 4, ( 1 + 5 2) 1 / ϵ − 1 } k\geq\max\{\frac{\log(\frac{2}{3}(c\epsilon)^{-1})}{\log 2}+4,(\frac{1+\sqrt{5}}{2})^{\nicefrac{{1}}{{\epsilon}}}-1\}. With L = ( k + 1) 2 / 3 L=(k+1)^{\nicefrac{{2}}{{3}}} we get

 |  | f k + 1 ​ ( m, n) \displaystyle f_{k+1}(m,n) |  |

 |  | ≪ ϵ ( ( k + 1) n) ϵ ( k + 1) Θ k ​ c ​ 2 k − 5 ( n 2 m) c ​ 2 k − 4 ( k + 1) 2 / 3 ⋅ c ​ 2 k − 4 ( 1 + L ( c ​ 2 k − 4) − 1) c ​ 2 k − 4 \displaystyle\ll_{\epsilon}((k+1)n)^{\epsilon}(k+1)^{\Theta_{k}c2^{k-5}}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}(k+1)^{\nicefrac{{2}}{{3}}\cdot c2^{k-4}}\left(1+L^{(c2^{k-4})^{-1}}\right)^{c2^{k-4}} |  |

 |  | ≪ ϵ ( k + 1) ϵ ⁡ ( 1 + c ​ 2 k − 3) n ϵ ( k + 1) c ​ 2 k − 4 ​ ( Θ k / 2 + 2 / 3) ( n 2 m) c ​ 2 k − 4. \displaystyle\ll_{\epsilon}(k+1)^{\epsilon(1+c2^{k-3})}n^{\epsilon}(k+1)^{c2^{k-4}(\nicefrac{{\Theta_{k}}}{{2}}+\nicefrac{{2}}{{3}})}\left(\frac{n^{2}}{m}\right)^{c2^{k-4}}. |  |

With Θ k + 1 = Θ k 2 + 2 3 \Theta_{k+1}=\frac{\Theta_{k}}{2}+\frac{2}{3} and an appropriate choice of ϵ \epsilon this implies

 | f k + 1 ≪ ϵ ( ( k + 1) n) ϵ ( ( k + 1) Θ k + 1 ​ n 2 m) c ​ 2 ( k + 1) − 5 f_{k+1}\ll_{\epsilon}((k+1)n)^{\epsilon}\left(\frac{(k+1)^{\Theta_{k+1}}n^{2}}{m}\right)^{c2^{(k+1)-5}} |  |

Since for Θ 5 ≤ 4 3 \Theta_{5}\leq\frac{4}{3} the sequence recursively defined by Θ k + 1 = Θ k 2 + 2 3 \Theta_{k+1}=\frac{\Theta_{k}}{2}+\frac{2}{3} monotonically increases towards its limit 4 3 \frac{4}{3} we eventually get for any k ≥ 5 k\geq 5:

 | f k ( m, n) ≪ ϵ ( k n) ϵ ( k 4 / 3 ​ n 2 m) c ​ 2 k − 5. f_{k}(m,n)\ll_{\epsilon}(kn)^{\epsilon}\left(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\right)^{c2^{k-5}}. |  |

∎

###### Proof of Theorem 2.

In the following δ < 1 \delta<1 is a fixed constant to be chosen at the end of the proof. We start with proving bounds on f 4 ​ ( m, n) f_{4}(m,n) and we write f 4 ​ ( m, n) = f 4 ( 1) ​ ( m, n) + f 4 ( 2) ​ ( m, n) f_{4}(m,n)=f_{4}^{(1)}(m,n)+f_{4}^{(2)}(m,n). Here f 4 ( 1) ​ ( m, n) f_{4}^{(1)}(m,n) counts those solutions of equation ( 5) with n 1 ​ t 1 ≤ n + n δ m n_{1}t_{1}\leq\frac{n+n^{\delta}}{m} and f 4 ( 2) ​ ( m, n) f_{4}^{(2)}(m,n) those with n 1 ​ t 1 > n + n δ m n_{1}t_{1}>\frac{n+n^{\delta}}{m}. From ( 21) we have that

 | f 4 ​ ( m, n) \displaystyle f_{4}(m,n) | = f 4 ( 1) ​ ( m, n) + f 4 ( 2) ​ ( m, n) ≤ ∑ 0 < u ≤ n δ m | u + n f 3 ​ ( u, n ⁡ ( u + n) m) + f 4 ( 2) ​ ( m, n) \displaystyle=f_{4}^{(1)}(m,n)+f_{4}^{(2)}(m,n)\leq\sum_{\begin{subarray}{c}0<u\leq n^{\delta}\\ m|u+n\end{subarray}}f_{3}\left(u,\frac{n(u+n)}{m}\right)+f_{4}^{(2)}(m,n) |  |

 |  | = S 1 + f 4 ( 2) ​ ( m, n). \displaystyle=S_{1}+f_{4}^{(2)}(m,n). |  |

We use the following estimate (uniform in a ∈ ℤ a\in\mathbb{Z})

(25) |  | ∑ n ≤ x n ≡ a mod q n − Θ = x 1 − Θ ( 1 + Θ) ​ q + 𝒪 Θ ​ ( 1). \sum_{\begin{subarray}{c}n\leq x\\ n\equiv a\bmod q\end{subarray}}n^{-\Theta}=\frac{x^{1-\Theta}}{(1+\Theta)q}+\mathcal{O}_{\Theta}(1). |  |

To bound the sum S 1 S_{1} we use ( 25) and Lemma B to get

(26) |  | S 1 ≪ ϵ n ϵ ( n 2 m) 2 3 ∑ 0 < u ≤ n δ m | u + n 1 u 2 3 ≪ ϵ n ϵ ( n 2 m) 2 3 ( n δ 3 m + 1). S_{1}\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{\frac{2}{3}}\sum_{\begin{subarray}{c}0<u\leq n^{\delta}\\ m|u+n\end{subarray}}\frac{1}{u^{\frac{2}{3}}}\ll_{\epsilon}n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{\frac{2}{3}}\left(\frac{n^{\frac{\delta}{3}}}{m}+1\right). |  |

Next we prove that

 | f 4 ( 2) ( m, n) ≪ ϵ n ϵ n ( 12 − 4 ​ δ) / 5 m 8 / 5. f_{4}^{(2)}(m,n)\ll_{\epsilon}n^{\epsilon}\frac{n^{\nicefrac{{(12-4\delta)}}{{5}}}}{m^{\nicefrac{{8}}{{5}}}}. |  |

Since there are at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) distinct patterns ( n 1, n 2, n 3, n 4) (n_{1},n_{2},n_{3},n_{4}) it suffices to prove this bound for all solutions counted by f 4 ( 2) ​ ( m, n) f_{4}^{(2)}(m,n) corresponding to a fixed pattern. To get an upper bound for the contribution of f 4 ( 2) ​ ( m, n) f_{4}^{(2)}(m,n) we thus suppose that ( n 1, n 2, n 3, n 4) (n_{1},n_{2},n_{3},n_{4}) is fixed and note that the fact that 4 ​ n m ≥ n 1 ​ t 1 > n + n δ m \frac{4n}{m}\geq n_{1}t_{1}>\frac{n+n^{\delta}}{m} implies the following upper bound for n 2 ​ t 2 n_{2}t_{2}:

 | 3 n 2 ​ t 2 ≥ m ​ n 1 ​ t 1 − n n ​ n 1 ​ t 1 ≥ m ​ n δ 4 ​ n 2. \frac{3}{n_{2}t_{2}}\geq\frac{mn_{1}t_{1}-n}{nn_{1}t_{1}}\geq\frac{mn^{\delta}}{4n^{2}}. |  |

Therefore we have

(27) |  | n 2 ​ t 2 ≪ n 2 − δ m. n_{2}t_{2}\ll\frac{n^{2-\delta}}{m}. |  |

We use again relative greatest common divisors and write a representation of m n \frac{m}{n} as a sum of four unit fractions as

 | m n \displaystyle\frac{m}{n} | = 1 n 1 ​ x 1 ​ x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234 + 1 n 2 ​ x 2 ​ x 12 ​ x 23 ​ x 24 ​ x 123 ​ x 124 ​ x 234 ​ x 1234 \displaystyle=\frac{1}{n_{1}x_{1}x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234}}+\frac{1}{n_{2}x_{2}x_{12}x_{23}x_{24}x_{123}x_{124}x_{234}x_{1234}} |  |

 |  | + 1 n 3 ​ x 3 ​ x 13 ​ x 23 ​ x 34 ​ x 123 ​ x 134 ​ x 234 ​ x 1234 + 1 n 4 ​ x 4 ​ x 14 ​ x 24 ​ x 34 ​ x 124 ​ x 134 ​ x 234 ​ x 1234. \displaystyle+\frac{1}{n_{3}x_{3}x_{13}x_{23}x_{34}x_{123}x_{134}x_{234}x_{1234}}+\frac{1}{n_{4}x_{4}x_{14}x_{24}x_{34}x_{124}x_{134}x_{234}x_{1234}}. |  |

It is again easy to see that x 1 = x 2 = x 3 = x 4 = 1 x_{1}=x_{2}=x_{3}=x_{4}=1 and multiplying out the last equation yields

(28) |  | m x 12 ​ x 13 ​ x 14 ​ x 23 ​ x 24 ​ x 34 ​ x 123 ​ x 124 ​ x 134 ​ x 234 ​ x 1234 = n n 1 ​ x 23 ​ x 24 ​ x 34 ​ x 234 + n n 2 ​ x 13 ​ x 14 ​ x 34 ​ x 134 + n n 3 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ x 12 ​ x 13 ​ x 23 ​ x 123. \begin{split}m&x_{12}x_{13}x_{14}x_{23}x_{24}x_{34}x_{123}x_{124}x_{134}x_{234}x_{1234}\\ &=\frac{n}{n_{1}}x_{23}x_{24}x_{34}x_{234}+\frac{n}{n_{2}}x_{13}x_{14}x_{34}x_{134}+\frac{n}{n_{3}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}}x_{12}x_{13}x_{23}x_{123}.\end{split} |  |

From equation ( 28) we see that the quantity

 | z 34 = n n 3 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ x 12 ​ x 13 ​ x 23 ​ x 123 x 34 z_{34}=\frac{\frac{n}{n_{3}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}}x_{12}x_{13}x_{23}x_{123}}{x_{34}} |  |

is an integer and we use

(29) |  | z 34 ​ x 34 = n n 3 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ x 12 ​ x 13 ​ x 23 ​ x 123. z_{34}x_{34}=\frac{n}{n_{3}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}}x_{12}x_{13}x_{23}x_{123}. |  |

By ( 27) and 4 ​ n m ≥ n 1 ​ t 1 > n + n δ m \frac{4n}{m}\geq n_{1}t_{1}>\frac{n+n^{\delta}}{m} we have

(30) |  | ( t 1 ​ t 2) 4 = ( x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234) 4 ​ ( x 12 ​ x 23 ​ x 24 ​ x 123 ​ x 124 ​ x 234 ​ x 1234) 4 ≪ n 12 − 4 ​ δ m 8, (t_{1}t_{2})^{4}=(x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234})^{4}(x_{12}x_{23}x_{24}x_{123}x_{124}x_{234}x_{1234})^{4}\ll\frac{n^{12-4\delta}}{m^{8}}, |  |

and we write

(31) |  | ( x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234) 4 ​ ( x 12 ​ x 23 ​ x 24 ​ x 123 ​ x 124 ​ x 234 ​ x 1234) 4 = ( x 12 x 13 x 14 x 23 x 24 x 123 x 124 x 1234) ( x 12 x 13 x 23 x 24 x 123 x 124 x 134 x 234 x 1234) × ( x 12 x 14 x 23 x 24 x 123 x 124 x 134 x 234 x 1234) ( x 12 x 13 x 14 x 24 x 123 x 124 x 134 x 234 x 1234) × ( x 12 4 ​ x 13 ​ x 14 ​ x 23 ​ x 123 4 ​ x 124 4 ​ x 134 ​ x 234 ​ x 1234 4). \begin{split}&(x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234})^{4}(x_{12}x_{23}x_{24}x_{123}x_{124}x_{234}x_{1234})^{4}=\\ &(x_{12}x_{13}x_{14}x_{23}x_{24}x_{123}x_{124}x_{1234})(x_{12}x_{13}x_{23}x_{24}x_{123}x_{124}x_{134}x_{234}x_{1234})\times\\ &(x_{12}x_{14}x_{23}x_{24}x_{123}x_{124}x_{134}x_{234}x_{1234})(x_{12}x_{13}x_{14}x_{24}x_{123}x_{124}x_{134}x_{234}x_{1234})\times\\ &(x_{12}^{4}x_{13}x_{14}x_{23}x_{123}^{4}x_{124}^{4}x_{134}x_{234}x_{1234}^{4}).\end{split} |  |

We show that each of the five factors in brackets on the right hand side of the last equation corresponds to at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) solutions of ( 28), where ϵ \epsilon is an arbitrarily small positive number. First we note that all factors are of polynomial size in n n and by Lemma A, given one of these factors, we have 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for all the x i ​ j x_{ij}, x i ​ j ​ k x_{ijk} and x 1234 x_{1234} appearing as sub-factors.

Given positive integer constants C 0, C 1, C 2 C_{0},C_{1},C_{2} and C 3 C_{3} of size polynomial in n n, we count the number of integer solutions ( A, B) (A,B) of the equation

(32) |  | C 0 ​ A ​ B = C 1 ​ A + C 2 ​ B + C 3. C_{0}AB=C_{1}A+C_{2}B+C_{3}. |  |

Rewriting this equation in the form

 | ( C 0 ​ A − C 2) ​ ( C 0 ​ B − C 1) = C 0 ​ C 3 + C 1 ​ C 2 (C_{0}A-C_{2})(C_{0}B-C_{1})=C_{0}C_{3}+C_{1}C_{2} |  |

we see that the number of solutions ( A, B) (A,B) is bounded by 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}). For the second to the fifth factor on the right hand side of ( 31) exactly two parameters are missing to uniquely determine a solution of ( 28). All of these factors miss the parameter x 34 x_{34}. The second one additionally misses x 14 x_{14}, the third one x 13 x_{13}, the fourth one x 23 x_{23} and the last one x 24 x_{24}. In all of these cases equation ( 28) provides an instance of ( 32) where the variables A A and B B correspond to the two missing parameters (the term containing both missing parameters on the right hand side of ( 28) may be shifted to the left hand side).

In the first factor on the right hand side of ( 31) three parameters are missing. From equation ( 29) we see that we have at most 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) choices for the parameter x 34 x_{34}. To see the same bound for the parameters x 134 x_{134} and x 234 x_{234} we use again that equations of type ( 32) can be factorized.

Since by ( 30) at least one of the factors on the right hand side of ( 31) is 𝒪 ⁡ ( n ( 12 − 4 ​ δ) / 5 m 8 / 5) \mathcal{O}\left(\frac{n^{\nicefrac{{(12-4\delta)}}{{5}}}}{m^{\nicefrac{{8}}{{5}}}}\right) we have that

(33) |  | f 4 ( 2) ( m, n) ≪ ϵ n ϵ n ( 12 − 4 ​ δ) / 5 m 8 / 5. f_{4}^{(2)}(m,n)\ll_{\epsilon}n^{\epsilon}\frac{n^{\nicefrac{{(12-4\delta)}}{{5}}}}{m^{\nicefrac{{8}}{{5}}}}. |  |

Again we note that in the considerations above the divisor bound from Lemma A was applied a bounded number of times and the bound in ( 33) follows upon redefining the choice of ϵ \epsilon. Choosing δ = 16 17 \delta=\frac{16}{17} in ( 26) and ( 33) we get

(34) |  | f 4 ​ ( m, n) ≪ n ϵ ​ ( n 4 / 3 m 2 / 3 + n 28 / 17 m 8 / 5). f_{4}(m,n)\ll n^{\epsilon}\left(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}\right). |  |

To bound f 5 ​ ( m, n) f_{5}(m,n) we again use ( 21) and ( 25) and get

(35) |  | f 5 ​ ( m, n) ≪ n ϵ ​ ∑ 0 < u ≤ 4 ​ n m | u + n ( ( n 2 m) 4 / 3 ​ 1 u 2 / 3 + ( n 2 m) 28 / 17 ​ 1 u 8 / 5) ≪ n ϵ ​ ( n 2 m) 28 / 17. f_{5}(m,n)\ll n^{\epsilon}\sum_{\begin{subarray}{c}0<u\leq 4n\\ m|u+n\end{subarray}}\left(\left(\frac{n^{2}}{m}\right)^{\nicefrac{{4}}{{3}}}\frac{1}{u^{\nicefrac{{2}}{{3}}}}+\left(\frac{n^{2}}{m}\right)^{\nicefrac{{28}}{{17}}}\frac{1}{u^{\nicefrac{{8}}{{5}}}}\right)\ll n^{\epsilon}\left(\frac{n^{2}}{m}\right)^{\nicefrac{{28}}{{17}}}. |  |

Setting c = 28 17 c=\frac{28}{17} in Lemma C yields the bound in Theorem 2. ∎

## 7. Lower bounds

###### Proof of Theorem 3.

To prove the first bound we are going to extend an idea used in the proof of [5] *Theorem 1. As before we use highly composite denominators n ∈ ℕ n\in\mathbb{N}, but here we show that there are many values a 1 a_{1} with many corresponding pairs ( a 2, a 3) (a_{2},a_{3}) giving a solution of

 | m n = 1 a 1 + 1 a 2 + 1 a 3. \frac{m}{n}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}}. |  |

To prove our lower bound for f 3 ​ ( m, n) f_{3}(m,n) we consider the set

 | 𝒩 = { m ​ n ′: n ′ = ∏ i = 1 r p i }, \mathcal{N}=\left\{mn^{\prime}:n^{\prime}=\prod_{i=1}^{r}p_{i}\right\}, |  |

where p i p_{i} is the i i -th prime. In choosing the denominators n ∈ 𝒩 n\in\mathcal{N} we reduce the problem to finding many solutions of the equation

 | 1 n ′ = 1 a 1 + 1 a 2 + 1 a 3. \frac{1}{n^{\prime}}=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\frac{1}{a_{3}}. |  |

We set a 1 = n ′ + d a_{1}=n^{\prime}+d, where d d is any divisor of n ′ n^{\prime}, and are left with

 | 1 n ′ − 1 n ′ + d = 1 n ′ ​ ( n ′ d + 1) = 1 a 2 + 1 a 3. \frac{1}{n^{\prime}}-\frac{1}{n^{\prime}+d}=\frac{1}{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}=\frac{1}{a_{2}}+\frac{1}{a_{3}}. |  |

For two divisors d 1 d_{1} and d 2 d_{2} of n ′ n^{\prime} with ( d 1, d 2) = 1 (d_{1},d_{2})=1 we have

(36) |  | 1 n ′ ​ ( n ′ d + 1) = 1 n ′ ​ ( n ′ d + 1) d 1 ​ ( d 1 + d 2) + 1 n ′ ​ ( n ′ d + 1) d 2 ​ ( d 1 + d 2). \frac{1}{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}=\frac{1}{\frac{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}{d_{1}}(d_{1}+d_{2})}+\frac{1}{\frac{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}{d_{2}}(d_{1}+d_{2})}. |  |

We note that for two pairs of divisors d 1, d 2 d_{1},d_{2} and d 1 ′, d 2 ′ d_{1}^{\prime},d_{2}^{\prime} with ( d 1, d 2) = 1 (d_{1},d_{2})=1 and ( d 1 ′, d 2 ′) = 1 (d_{1}^{\prime},d_{2}^{\prime})=1 it follows that

 | n ′ ​ ( n ′ d + 1) d 1 ​ ( d 1 + d 2) = n ′ ​ ( n ′ d + 1) d 1 ′ ​ ( d 1 ′ + d 2 ′) ⇔ d 1 d 2 = d 1 ′ d 2 ′. \frac{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}{d_{1}}(d_{1}+d_{2})=\frac{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}{d_{1}^{\prime}}(d_{1}^{\prime}+d_{2}^{\prime})\Leftrightarrow\frac{d_{1}}{d_{2}}=\frac{d_{1}^{\prime}}{d_{2}^{\prime}}. |  |

Since d 1 d_{1} and d 2 d_{2} as well as d 1 ′ d_{1}^{\prime} and d 2 ′ d_{2}^{\prime} are coprime we get d 1 = d 1 ′ d_{1}=d_{1}^{\prime} and d 2 = d 2 ′ d_{2}=d_{2}^{\prime}. This implies that each pair ( d 1, d 2) (d_{1},d_{2}) with d 1 < d 2 d_{1}<d_{2} gives a unique solution of equation ( 36). Furthermore for any choice of d, d 1, d 2 d,d_{1},d_{2} it follows that

 | n ′ + d < n ′ ​ ( n ′ d + 1) d 1 ​ ( d 1 + d 2), n^{\prime}+d<\frac{n^{\prime}\left(\frac{n^{\prime}}{d}+1\right)}{d_{1}}(d_{1}+d_{2}), |  |

which altogether implies that by counting all possible choices for d, d 1, d 2 d,d_{1},d_{2} we get a lower bound for twice the value of f 3 ​ ( 1, n ′) f_{3}(1,n^{\prime}).

Choosing n ′ n^{\prime} as in the construction of the set 𝒩 \mathcal{N}, we have 2 ω ⁡ ( n ′) 2^{\omega(n^{\prime})} choices for the divisor d d and using the binomial theorem there are

 | ∑ i = 0 ω ⁡ ( n ′) ( ω ⁡ ( n ′) i) ​ ∑ j = 0 ω ⁡ ( n ′) − i ( ω ⁡ ( n ′) − i j) = ∑ i = 0 ω ⁡ ( n ′) ( ω ⁡ ( n ′) i) ​ 2 ω ⁡ ( n ′) − i = 3 ω ⁡ ( n ′) \sum_{i=0}^{\omega(n^{\prime})}\binom{\omega(n^{\prime})}{i}\sum_{j=0}^{\omega(n^{\prime})-i}\binom{\omega(n^{\prime})-i}{j}=\sum_{i=0}^{\omega(n^{\prime})}\binom{\omega(n^{\prime})}{i}2^{\omega(n^{\prime})-i}=3^{\omega(n^{\prime})} |  |

choices for the divisors d 1 d_{1} and d 2 d_{2}. As a consequence of the prime number theorem it is known that ω ⁡ ( n ′) ∼ log ⁡ n ′ log ⁡ log ⁡ n ′ \omega(n^{\prime})\sim\frac{\log n^{\prime}}{\log\log n^{\prime}} and hence, for n ∈ 𝒩 n\in\mathcal{N}

 | f 3 ​ ( m, n) = f 3 ​ ( 1, n ′) ≥ 1 2 ​ 2 ω ⁡ ( n ′) ​ 3 ω ⁡ ( n ′) \displaystyle f_{3}(m,n)=f_{3}(1,n^{\prime})\geq\frac{1}{2}2^{\omega(n^{\prime})}3^{\omega(n^{\prime})} | ≥ exp ⁡ ( ( log ⁡ 6 + o ⁡ ( 1)) ​ log ⁡ n ′ log ⁡ log ⁡ n ′) \displaystyle\geq\exp\left((\log 6+o(1))\frac{\log n^{\prime}}{\log\log n^{\prime}}\right) |  |

 |  | ≥ exp ⁡ ( ( log ⁡ 6 + o m ​ ( 1)) ​ log ⁡ n log ⁡ log ⁡ n). \displaystyle\geq\exp\left((\log 6+o_{m}(1))\frac{\log n}{\log\log n}\right). |  |

For the second bound we modify the idea used in the proof of [9] *Theorem 1.8. For fixed m ∈ ℕ m\in\mathbb{N}, as a consequence of the Turán-Kubilius inequality (see e.g. [29] *p. 434) we get that the set

 | ℳ 1 = ⋂ k ≤ m ( k, m) = 1 { n ∈ ℕ: ω ⁡ ( n, k, m) = ( 1 φ ⁡ ( m) + o ⁡ ( 1)) ​ log ⁡ log ⁡ n } \mathcal{M}_{1}=\bigcap_{\begin{subarray}{c}k\leq m\\ (k,m)=1\end{subarray}}\left\{n\in\mathbb{N}:\omega(n,k,m)=\left(\frac{1}{\varphi(m)}+o(1)\right)\log\log n\right\} |  |

is a set with density one, i.e. lim x → ∞ { n ∈ ℳ 1: n ≤ x } x = 1 \lim_{x\rightarrow\infty}\frac{\{n\in\mathcal{M}_{1}:n\leq x\}}{x}=1.

For any n ∈ ℳ 1 n\in\mathcal{M}_{1} we write m n = m ′ n ′ \frac{m}{n}=\frac{m^{\prime}}{n^{\prime}} with ( m ′, n ′) = 1 (m^{\prime},n^{\prime})=1 and note that ω ⁡ ( n, k, m) = ω ⁡ ( n ′, k, m) \omega(n,k,m)=\omega(n^{\prime},k,m) for all k k with ( k, m) = 1 (k,m)=1. By construction of the set ℳ 1 \mathcal{M}_{1} and since n ′ n^{\prime} is coprime to m ′ m^{\prime}, we find ( 1 φ ⁡ ( m) + o ⁡ ( 1)) ​ log ⁡ log ​ n \left(\frac{1}{\varphi(m)}+o(1)\right)\log\log n prime divisors p p of n ′ n^{\prime} in the residue class − n ′ mod m ′ -n^{\prime}\bmod m^{\prime}. For any of these prime divisors we have

 | m ′ n ′ − 1 n ′ + p m ′ = p n ′ ​ n ′ + p m ′ = 1 n ′ ​ n ′ / p + 1 m ′ \frac{m^{\prime}}{n^{\prime}}-\frac{1}{\frac{n^{\prime}+p}{m^{\prime}}}=\frac{p}{n^{\prime}\frac{n^{\prime}+p}{m^{\prime}}}=\frac{1}{n^{\prime}\frac{\nicefrac{{n^{\prime}}}{{p}}+1}{m^{\prime}}} |  |

where n ′ / p + 1 m ′ \frac{\nicefrac{{n^{\prime}}}{{p}}+1}{m^{\prime}} is an integer. Again, by construction of the set ℳ 1 \mathcal{M}_{1}, for the number of prime factors of n ′ n^{\prime} we have

 | ω ⁡ ( n ′) ≥ ω ⁡ ( n) − ω ⁡ ( m) = ( 1 + o m ​ ( 1)) ​ log ⁡ log ⁡ n. \omega(n^{\prime})\geq\omega(n)-\omega(m)=(1+o_{m}(1))\log\log n. |  |

For two coprime divisors d 1 d_{1} and d 2 d_{2} of n ′ n^{\prime} we construct decompositions of 1 n ′ ​ n ′ / p + 1 m ′ \frac{1}{n^{\prime}\frac{\nicefrac{{n^{\prime}}}{{p}}+1}{m^{\prime}}} as a sum of two unit fractions as in ( 36). As above we see that for any prime divisor p p of n ′ n^{\prime} in the residue class − n ′ mod m ′ -n^{\prime}\bmod m^{\prime} there are at least 3 ω ⁡ ( n ′) 3^{\omega(n^{\prime})} such decompositions and all of them are distinct.

Altogether this implies that for any n ∈ ℳ 1 n\in\mathcal{M}_{1}

 | f ⁡ ( m, n) \displaystyle f(m,n) | ≥ ( 1 φ ⁡ ( m) + o ⁡ ( 1)) ​ 3 ω ⁡ ( n ′) ⋅ log ⁡ log ⁡ n ≥ ( 1 φ ⁡ ( m) + o ⁡ ( 1)) ​ 3 ω ⁡ ( n / m) ⋅ log ⁡ log ⁡ n \displaystyle\geq\left(\frac{1}{\varphi(m)}+o(1)\right)3^{\omega(n^{\prime})}\cdot\log\log n\geq\left(\frac{1}{\varphi(m)}+o(1)\right)3^{\omega(\nicefrac{{n}}{{m}})}\cdot\log\log n |  |

 |  | ≥ exp ⁡ ( ( log ⁡ 3 + o m ​ ( 1)) ​ log ⁡ log ⁡ n) ⋅ log ⁡ log ⁡ n. \displaystyle\geq\exp((\log 3+o_{m}(1))\log\log n)\cdot\log\log n. |  |

Finally, we prove the improved lower bound on f 3 ​ ( 4, n) f_{3}(4,n). To do so, we set

 | ℳ 2 \displaystyle\mathcal{M}_{2} | = ( ⋂ i ∈ { 1, 3 } { n ∈ ℕ: τ ⁡ ( n, 4) 4 ≤ τ ⁡ ( n, i, 4) }) ∩ \displaystyle=\left(\bigcap_{i\in\{1,3\}}\{n\in\mathbb{N}:\frac{\tau(n,4)}{4}\leq\tau(n,i,4)\}\right)\cap |  |

 |  | ∩ { n ∈ ℕ: ω ⁡ ( n) = ( 1 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n } ∩ { n ∈ ℕ: τ ⁡ ( n) ≥ ( log ⁡ n) log ⁡ 2 + o ⁡ ( 1) }. \displaystyle\cap\{n\in\mathbb{N}:\omega(n)=(1+o(1))\log\log n\}\cap\{n\in\mathbb{N}:\tau(n)\geq(\log n)^{\log 2+o(1)}\}. |  |

The first two sets with i = 1 i=1 and i = 3 i=3 in the intersection in the definition of ℳ 2 \mathcal{M}_{2} have density 1 1 by [17] *Theorem 5. For the third and the fourth set this is true by the Turán-Kubilius inequality (again see e.g. [29] *p. 434). Hence the set ℳ 2 \mathcal{M}_{2} has density 1 1 and we investigate what happens for n n in a certain residue class modulo 4 4.

If n ≡ 0 mod 4 n\equiv 0\bmod 4, then 4 n = 1 n / 4 \frac{4}{n}=\frac{1}{\nicefrac{{n}}{{4}}} and for any divisor d d of n 4 \frac{n}{4} we have

 | 1 n 4 − 1 n 4 + d = 1 n 4 ​ ( n 4 ​ d + 1). \frac{1}{\frac{n}{4}}-\frac{1}{\frac{n}{4}+d}=\frac{1}{\frac{n}{4}\left(\frac{n}{4d}+1\right)}. |  |

Since ω ⁡ ( n 4) ≥ ω ⁡ ( n) − 1 \omega\left(\frac{n}{4}\right)\geq\omega(n)-1, with the same arguments as above, we conclude that the number of representations of 1 n / 4 ​ ( n / 4 ​ d + 1) \frac{1}{\nicefrac{{n}}{{4}}\left(\nicefrac{{n}}{{4d}}+1\right)} as a sum of two unit fractions is at least of order 3 ω ⁡ ( n / 4) = 3 ( 1 + o ⁡ ( 1)) ​ log ⁡ log ​ n 3^{\omega(\nicefrac{{n}}{{4}})}=3^{(1+o(1))\log\log n}. From τ ⁡ ( n) = ∏ p | n ( ν p ​ ( n) + 1) \tau(n)=\prod_{p|n}(\nu_{p}(n)+1) we easily deduce that τ ⁡ ( n 4) ≥ 1 3 ​ τ ​ ( n) \tau\left(\frac{n}{4}\right)\geq\frac{1}{3}\tau(n). Altogether we thus get

 | f 3 ​ ( 4, n) ≥ 1 3 ​ τ ​ ( n 4) ​ 3 ω ⁡ ( n / 4) ≥ exp ⁡ ( ( log ⁡ 6 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n). f_{3}(4,n)\geq\frac{1}{3}\tau\left(\frac{n}{4}\right)3^{\omega(\nicefrac{{n}}{{4}})}\geq\exp((\log 6+o(1))\log\log n). |  |

If n ≡ 2 mod 4 n\equiv 2\bmod 4, then n 2 \frac{n}{2} is odd and the same is true for all τ ⁡ ( n 2) = 1 2 ​ τ ​ ( n) \tau\left(\frac{n}{2}\right)=\frac{1}{2}\tau(n) divisors of n 2 \frac{n}{2}. We have 4 n = 2 n / 2 \frac{4}{n}=\frac{2}{\nicefrac{{n}}{{2}}} and for any divisor d d of n 2 \frac{n}{2}

 | 2 n 2 − 1 n / 2 + d 2 = 1 n 2 ​ ( n / 2 ​ d + 1 2). \frac{2}{\frac{n}{2}}-\frac{1}{\frac{\nicefrac{{n}}{{2}}+d}{2}}=\frac{1}{\frac{n}{2}\left(\frac{\nicefrac{{n}}{{2d}}+1}{2}\right)}. |  |

As above we get

 | f 3 ​ ( 4, n) ≥ τ ⁡ ( n 2) ​ 3 ω ⁡ ( n) − 1 ≥ exp ⁡ ( ( log ⁡ 6 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n). f_{3}(4,n)\geq\tau\left(\frac{n}{2}\right)3^{\omega(n)-1}\geq\exp((\log 6+o(1))\log\log n). |  |

Finally, if n ≡ r mod 4 n\equiv r\bmod 4 for r ∈ { 1, 3 } r\in\{1,3\}, we have τ ⁡ ( n, 4) = τ ⁡ ( n) \tau(n,4)=\tau(n) and by construction of the set ℳ 2 \mathcal{M}_{2}, we have more than τ ⁡ ( n) 4 \frac{\tau(n)}{4} divisors d d of n n in the residue class − r mod 4 -r\bmod 4. Again, for any of these divisors we have

 | 4 n − 1 n + d 4 = 1 n ⁡ ( n / d + 1 4). \frac{4}{n}-\frac{1}{\frac{n+d}{4}}=\frac{1}{n\left(\frac{\nicefrac{{n}}{{d}}+1}{4}\right)}. |  |

Applying the arguments used previously one more time, we find

 | f 3 ​ ( 4, n) ≥ τ ⁡ ( n) 4 ​ 3 ω ⁡ ( n) ≥ exp ⁡ ( ( log ⁡ 6 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n) f_{3}(4,n)\geq\frac{\tau(n)}{4}3^{\omega(n)}\geq\exp((\log 6+o(1))\log\log n) |  |

also in this case.

∎

###### Remark 3.

The difference in the constants in the exponential functions of the lower bounds on f ⁡ ( m, n) f(m,n) and f ⁡ ( 4, n) f(4,n) for sets of integers with density one in Theorem 3 is basically due to cancellation effects when dealing with general m m. In particular we deal with m n = m ′ n ′ \frac{m}{n}=\frac{m^{\prime}}{n^{\prime}}, where ( m ′, n ′) = 1 (m^{\prime},n^{\prime})=1, and we would need to have good control of the number of divisors of n ′ n^{\prime} in the residue class − n ′ mod m ′ -n^{\prime}\bmod m^{\prime} to get the log ⁡ 6 \log 6 exponent also in the general case. However, if we do not ask about a lower bound holding for a set of density one within the positive integers, but for a set of integers of density one within the set 𝒮 \mathcal{S} of positive integers coprime to a given m ∈ ℕ m\in\mathbb{N}, we may achieve the log ⁡ 6 \log 6 exponent. To do so we replace the set ℳ 1 \mathcal{M}_{1} with

 | ℳ 1 ′ \displaystyle\mathcal{M}_{1}^{\prime} | = ( ⋂ 1 ≤ i ≤ m ( i, m) = 1 { n ∈ ℕ: τ ⁡ ( n, i, m) = τ ⁡ ( n) φ ⁡ ( m) ​ ( 1 + o m ​ ( 1)) }) ∩ \displaystyle=\left(\bigcap_{\begin{subarray}{c}1\leq i\leq m\\ (i,m)=1\end{subarray}}\{n\in\mathbb{N}:\tau(n,i,m)=\frac{\tau(n)}{\varphi(m)}(1+o_{m}(1))\}\right)\cap |  |

 |  | ∩ { n ∈ ℕ: ω ⁡ ( n) = ( 1 + o ⁡ ( 1)) ​ log ⁡ log ⁡ n } ∩ { n ∈ ℕ: τ ⁡ ( n) ≥ ( log ⁡ n) log ⁡ 2 + o ⁡ ( 1) } ∩ 𝒮. \displaystyle\cap\{n\in\mathbb{N}:\omega(n)=(1+o(1))\log\log n\}\cap\{n\in\mathbb{N}:\tau(n)\geq(\log n)^{\log 2+o(1)}\}\cap\mathcal{S}. |  |

Now we may use results from [17] *Theorem 5 as well as Turán-Kubilius like previously and get that ℳ 1 ′ \mathcal{M}_{1}^{\prime} has density one in 𝒮 \mathcal{S}. Instead of constructing the first denominator via shifts in prime factors of n n we may use arbitrary divisors of n n in this case, which leads to the improvement mentioned above.

###### Proof of Theorem 4.

We consider solutions corresponding to the pattern ( 1, p, p) (1,p,p). In equation ( 1) we suppose that a 1 a_{1} is the denominator with ( a 1, p) = 1 (a_{1},p)=1 and we write a 1 = t 1 a_{1}=t_{1}, a 2 = p ​ t 2 a_{2}=pt_{2} and a 3 = p ​ t 3 a_{3}=pt_{3}. We use the parametrization via relative greatest common divisors of the t i t_{i} and applying Lemma 1 it is easy to see, that x 1 = x 2 = x 3 = 1 x_{1}=x_{2}=x_{3}=1 in this case. Hence we are looking for infinitely many primes p ≡ e mod f p\equiv e\bmod f such that for given m ∈ ℕ m\in\mathbb{N} the equation

(37) |  | m p = 1 x 12 ​ x 13 ​ x 123 + 1 p ​ x 12 ​ x 23 ​ x 123 + 1 p ​ x 13 ​ x 23 ​ x 123 \frac{m}{p}=\frac{1}{x_{12}x_{13}x_{123}}+\frac{1}{px_{12}x_{23}x_{123}}+\frac{1}{px_{13}x_{23}x_{123}} |  |

has many solutions. Multiplying equation ( 37) by the common denominator we get

 | m ​ x 12 ​ x 13 ​ x 23 ​ x 123 = p ​ x 23 + x 13 + x 12. mx_{12}x_{13}x_{23}x_{123}=px_{23}+x_{13}+x_{12}. |  |

Setting x 12 + x 13 = k ​ x 23 x_{12}+x_{13}=kx_{23}, M = lcm ⁡ ( m, f) M=\lcm(m,f) and x 12 = M m x_{12}=\frac{M}{m} we deduce that

 | M ⁡ ( k ​ x 23 − M m) ​ x 123 = p + k. M\left(kx_{23}-\frac{M}{m}\right)x_{123}=p+k. |  |

The residue class ( f − e) ≡ − e mod f (f-e)\equiv-e\bmod f splits into the residue classes ( f − e) + i ​ f mod M (f-e)+if\bmod M, for 0 ≤ i ≤ m ( m, f) − 1 0\leq i\leq\frac{m}{(m,f)}-1. Note, that gcd ⁡ ( f, m ( m, f)) = 1 \gcd\left(f,\frac{m}{(m,f)}\right)=1 hence the integers i ⋅ f i\cdot f for 0 ≤ i ≤ m ( m, f) − 1 0\leq i\leq\frac{m}{(m,f)}-1 are a full system of residues modulo m ( m, f) \frac{m}{(m,f)}. In particular there exists a 0 ≤ j ≤ m ( m, f) − 1 0\leq j\leq\frac{m}{(m,f)}-1 such that ( f − e) + j ​ f ≡ 1 mod m ( m, f) (f-e)+jf\equiv 1\bmod\frac{m}{(m,f)}. We set k = ( f − e) + j ​ f k=(f-e)+jf and with ( e, f) = 1 (e,f)=1 we altogether see that ( M, k) = 1 (M,k)=1.

Now let Q = ∏ i = 1 r q i Q=\prod_{i=1}^{r}q_{i} where q i q_{i} is the i i -th prime with q i ≡ − M m mod k q_{i}\equiv-\frac{M}{m}\bmod k and q i > M q_{i}>M. Note that gcd ⁡ ( M, Q) = 1 \gcd(M,Q)=1.

With r = ⌊ log ⁡ t φ ⁡ ( k) ​ C ​ log ⁡ log ​ t ⌋ r=\left\lfloor\frac{\log t}{\varphi(k)C\log\log t}\right\rfloor we find that Q Q is of order t 1 / C + o f, m ​ ( 1) t^{\nicefrac{{1}}{{C}}+o_{f,m}(1)}. We now use Linnik’s theorem on primes in arithmetic progressions. As the modulus is very smooth we can use an exponent of C = 12 5 + o ⁡ ( 1) C=\frac{12}{5}+o(1), due to Chang [6] *Corollary 11. Hence we may find a prime p p of order M C ​ t 1 + o f, m ​ ( 1) M^{C}t^{1+o_{f,m}(1)} with

 | p ≡ − k mod Q ​ M. p\equiv-k\bmod QM. |  |

This congruence implies that p + k p+k is divisible by the primes q 1, …, q r q_{1},\ldots,q_{r} and together with k = ( f − e) + j ​ f k=(f-e)+jf, we deduce that p ≡ e mod f p\equiv e\bmod f and p + k ≡ 0 mod M p+k\equiv 0\bmod M.

Let l ∈ ℕ 0 l\in\mathbb{N}_{0} and S S be a subset of size l ​ ord k ​ ( − M m) + 1 l\ord_{k}\left(-\frac{M}{m}\right)+1 of the prime factors of Q Q. Hence x 23 = ∏ q ∈ S q + M m k x_{23}=\frac{\prod_{q\in S}q+\frac{M}{m}}{k} is an integer and we set x 123 = p + k M ​ ∏ q ∈ S q x_{123}=\frac{p+k}{M\prod_{q\in S}q}. We observe that any of these choices leads to a different solution of ( 37). To see this we look at the denominator a 2 = p ​ x 12 ​ x 23 ​ x 123 a_{2}=px_{12}x_{23}x_{123} of the second fraction on the right hand side of this equation. Suppose that two sets S S and S ′ S^{\prime} would lead to the same denominator a 2 a_{2}. With x 12 = M m x_{12}=\frac{M}{m} this would imply the existence of x 23 ≠ x 23 ′ x_{23}\neq x_{23}^{\prime} such that

 | p ​ M m ​ x 23 ​ p + k M ⁡ ( k ​ x 23 − M m) = p ​ M m ​ x 23 ′ ​ p + k M ⁡ ( k ​ x 23 ′ − M m) p\frac{M}{m}x_{23}\frac{p+k}{M(kx_{23}-\frac{M}{m})}=p\frac{M}{m}x_{23}^{\prime}\frac{p+k}{M(kx_{23}^{\prime}-\frac{M}{m})} |  |

from which we derive that

 | x 23 x 23 ′ = k ​ x 23 − M m k ​ x 23 ′ − M m = ∏ q ∈ S q ∏ q ′ ∈ S ′ q ′. \frac{x_{23}}{x_{23}^{\prime}}=\frac{kx_{23}-\frac{M}{m}}{kx_{23}^{\prime}-\frac{M}{m}}=\frac{\prod_{q\in S}q}{\prod_{q^{\prime}\in S^{\prime}}q^{\prime}}. |  |

If q ∈ S q\in S would divide x 23 x_{23} then q q would also divide M m \frac{M}{m}, which is impossible by construction of Q Q. We hence have that ∏ q ∈ S q ∏ q ′ ∈ S ′ q ′ = 1 \frac{\prod_{q\in S}q}{\prod_{q^{\prime}\in S^{\prime}}q^{\prime}}=1 and thus S = S ′ S=S^{\prime}.

To count the number of solutions we get with the above construction, we make use of a formula which can be found in [3] *Theorem 1, for example, and which states

(38) |  | ∑ i ≥ 0 ( n i ​ u) = 1 u ​ ∑ j = 0 u − 1 ( 1 + ξ u j) n, \sum_{i\geq 0}\binom{n}{iu}=\frac{1}{u}\sum_{j=0}^{u-1}(1+\xi_{u}^{j})^{n}, |  |

where ξ u = exp ⁡ ( 2 ​ π ​ i u) \xi_{u}=\exp\left(\frac{2\pi i}{u}\right). Note that for the term corresponding to j = 0 j=0 in the sum on the right hand side of ( 38) we get 2 n 2^{n} while for all other j j we have | 1 + ξ u j | < 2 |1+\xi_{u}^{j}|<2. Hence we deduce

 | ∑ i ≥ 0 ( n i ​ u) = 2 n u ​ ( 1 + o u ​ ( 1)). \sum_{i\geq 0}\binom{n}{iu}=\frac{2^{n}}{u}(1+o_{u}(1)). |  |

The number of choices of the parameter x 23 x_{23} is

 | ∑ i ≥ 0 \displaystyle\sum_{i\geq 0} | ( r i ​ ord k ​ ( − M m) + 1) = ∑ i ≥ 0 ( r + 1 i ​ ord k ​ ( − M m)) − ∑ i ≥ 0 ( r i ​ ord k ​ ( − M m)) \displaystyle\binom{r}{i\ord_{k}\left(-\frac{M}{m}\right)+1}=\sum_{i\geq 0}\binom{r+1}{i\ord_{k}\left(-\frac{M}{m}\right)}-\sum_{i\geq 0}\binom{r}{i\ord_{k}\left(-\frac{M}{m}\right)} |  |

 |  | = 2 r + 1 ord k ⁡ ( − M m) ​ ( 1 + o f, m ​ ( 1)) − 2 r ord k ⁡ ( − M m) ​ ( 1 + o f, m ​ ( 1)) \displaystyle=\frac{2^{r+1}}{\ord_{k}\left(-\frac{M}{m}\right)}(1+o_{f,m}(1))-\frac{2^{r}}{\ord_{k}\left(-\frac{M}{m}\right)}(1+o_{f,m}(1)) |  |

 |  | = 2 r ord k ⁡ ( − M m) ​ ( 1 + o f, m ​ ( 1)). \displaystyle=\frac{2^{r}}{\ord_{k}\left(-\frac{M}{m}\right)}(1+o_{f,m}(1)). |  |

Plugging in r = ⌊ log ⁡ t φ ⁡ ( k) ​ C ​ log ⁡ log ​ t ⌋ r=\left\lfloor\frac{\log t}{\varphi(k)C\log\log t}\right\rfloor and using that p ≤ M C ​ t 1 + o f, m ​ ( 1) p\leq M^{C}t^{1+o_{f,m}(1)} we get a lower bound of

(39) |  | f 3 ​ ( m, p) \displaystyle f_{3}(m,p) | ≫ f, m exp ( ( log ⁡ 2 C ​ φ ​ ( k) + o f, m ( 1)) log ⁡ t log ⁡ log ⁡ t) \displaystyle\gg_{f,m}\exp\left(\left(\frac{\log 2}{C\varphi(k)}+o_{f,m}(1)\right)\frac{\log t}{\log\log t}\right) |  |

 |  | ≫ f, m exp ( ( 5 ​ log ⁡ 2 12 ​ lcm ⁡ ( m, f) + o f, m ( 1)) log ⁡ p log ⁡ log ⁡ p). \displaystyle\gg_{f,m}\exp\left(\left(\frac{5\log 2}{12\lcm(m,f)}+o_{f,m}(1)\right)\frac{\log p}{\log\log p}\right). |  |

∎

###### Remark 4.

The best known exponent for Linnik’s Theorem takes care of the worst case modulus and is 5 5 by work of Xylouris [30]. Chang’s result [6] *Corollary 11 considers smooth moduli (as in our situation) and allows for the better exponent 12 5 \frac{12}{5}. Harman investigated, in connection with constructing Carmichael numbers, what happens if one is allowed to avoid a small set of exceptional moduli. In this situation he improved the exponent to 1 0.4736 \frac{1}{0.4736} (see [20] *Theorem 1.2 and [19] for some more explanation). As in our situation we choose the modulus M M, and hence can avoid ”bad” factors, it seems possible that Theorem 4 can also be proved with a factor of 0.4736 0.4736 instead of 5 12 ≈ 0.4167 \frac{5}{12}\approx 0.4167 in the exponent of the lower bound on f 3 ​ ( m, p) f_{3}(m,p).

###### Remark 5.

If we consider the case m = 4 m=4, f = 4 f=4 and e ∈ { 1, 3 } e\in\{1,3\} in Theorem 4, we can explicitly compute k k in the first line of ( 39). We simply have k = 3 k=3 if e = 1 e=1 and k = 1 k=1 if e = 3 e=3 hence we arrive at the lower bounds

 | f 3 ​ ( 4, p) ≫ exp ⁡ ( ( 0.1444 + o ⁡ ( 1)) ​ log ⁡ p log ⁡ log ⁡ p) f_{3}(4,p)\gg\exp\left((0.1444+o(1))\frac{\log p}{\log\log p}\right) |  |

if e = 1 e=1 and

 | f 3 ​ ( 4, p) ≫ exp ⁡ ( ( 0.2888 + o ⁡ ( 1)) ​ log ⁡ p log ⁡ log ⁡ p) f_{3}(4,p)\gg\exp\left((0.2888+o(1))\frac{\log p}{\log\log p}\right) |  |

if e = 3 e=3.

## Acknowledgement

The authors acknowledge the support of the Austrian Science Fund (FWF): W1230. Furthermore we would like to thank Igor Shparlinski and Glyn Harman for drawing our attention to the papers [6] and [19, 20].

## References

- [1] A. Aigner (1964) Brüche als summe von stammbrüchen. J. Reine Angew. Math. 214/215, pp. 174–179. Cited by: §3.
- [2] R. Arce-Nazario, F. Castro, and R. Figueroa (2013) On the number of solutions of ∑ i = 1 11 1 x i = 1 \sum_{i=1}^{11}\frac{1}{x_{i}}=1 in distinct odd natural numbers. J. Number Theory 133 ( 6), pp. 2036–2046. Cited by: Remark 2.
- [3] A. T. Benjamin, B. Chen, and K. Kindred (2010) Sums of evenly spaced binomial coefficients. Math. Mag. 83 ( 5), pp. 370–373. Cited by: §7.
- [4] L. Brenton and R. Hill (1988) On the Diophantine equation 1 = ∑ 1 / n i + 1 / ∏ n i 1=\sum 1/n_{i}+1/\prod n_{i} and a class of homologically trivial complex surface singularities. Pacific J. Math. 133 ( 1), pp. 41–67. Cited by: §1.
- [5] T. D. Browning and C. Elsholtz (2011) The number of representations of rationals as a sum of unit fractions. Illinois J. Math. 55 ( 2), pp. 685–696. Cited by: §1, §1, §1, §1, §1, §1, §3, §6, §6, §6, §6, §7, Remark 2.
- [6] M.-C. Chang (2014) Short character sums for composite moduli. J. Anal. Math. 123, pp. 1–33. Cited by: §7, Acknowledgement, Remark 4.
- [7] Y.-G. Chen, C. Elsholtz, and L.-L. Jiang (2012) Egyptian fractions with restrictions. Acta Arith. 154 ( 2), pp. 109–123. Cited by: §1.
- [8] R. Dedekind Über zerlegungen von zahlen durch ihre größten gemeinsamen teiler. In in Gesammelte mathematische Werke, Zweiter Band (Fricke, R., Noether, E. and Ore, Ö., eds.), Friedr. Vieweg & Sohn Akt.-Ges., Braunschweig, 1931, pp. 103–147. Note: Available online at http://resolver.sub.uni-goettingen.de/purl?PPN235693928 Cited by: §4.
- [9] C. Elsholtz and T. Tao (2013) Counting the number of solutions to the Erdős-Straus equation on unit fractions. J. Aust. Math. Soc. 94 ( 1), pp. 50–105. Cited by: §1, §1, §1, §1, §3, §5, §7.
- [10] C. Elsholtz (1999) Sums of k k Unit Fractions. Shaker Verlag, Aachen. Note: Phd Thesis, Technische Universität Darmstadt (1998), 109 pages Cited by: §4, §4, §4.
- [11] C. Elsholtz (2001) Sums of k k unit fractions. Trans. Amer. Math. Soc. 353 ( 8), pp. 3209–3227. Cited by: §3, §4.
- [12] C. Elsholtz (2016) Egyptian fractions with odd denominators. Q. J. Math. 67 ( 3), pp. 425–430. Cited by: §1.
- [13] R. L. Graham Paul erd \h os and egyptian fractions. In in Erdős Centennial, Bolyai Soc. Math. Stud., 25, (Lovász, L., Ruzsa, I. Z. and Sós, V. T., eds.), János Bolyai Math. Soc., Budapest, 2013, pp. 289–309. Cited by: §1, §1.
- [14] R. L. Graham (1964) On finite sums of reciprocals of distinct n n th powers. Pacific J. Math. 14, pp. 85–92. Cited by: §1.
- [15] R. L. Graham (1964) On finite sums of unit fractions. Proc. London Math. Soc. (3) 14, pp. 193–207. Cited by: §1.
- [16] R. K. Guy (2010) Unsolved Problems in Number Theory. third edition edition, Springer-Verlag, New York. Cited by: §1.
- [17] R. R. Hall (1970) On the distribution of divisors of integers in residue classes ( mod ​ k) ({\rm mod}\,k). J. Number Theory 2, pp. 168–188. Cited by: §7, Remark 3.
- [18] G. H. Hardy and E. M. Wright (2008) An Introduction to the Theory of Numbers. sixth edition edition, Oxford University Press, Oxford. Cited by: §5.
- [19] G. Harman (2005) On the number of carmichael numbers up to x x. Bull. London Math. Soc. 37 ( 5), pp. 641–650. Cited by: §1, Acknowledgement, Remark 4.
- [20] G. Harman (2008) Watt’s mean value theorem and carmichael numbers. Int. J. Number Theory 4 ( 2), pp. 241–248. Cited by: §1, Acknowledgement, Remark 4.
- [21] S. V. Konyagin (2014) Double exponential lower bound for the number of representations of unity by Egyptian fractions. Math. Notes 95 ( 1-2), pp. 277–281. Note: Translation of Mat. Zametki 95 (2014), no. 2, 312–316 Cited by: §1.
- [22] V.-A. Lebesgue (1849) Extrait des exercises d’analyse numérique. Nouvelles annales de mathématiques 1 re 1^{\text{re}} série 8, pp. 347–353. Cited by: §4.
- [23] H. W. Lenstra, Jr. and C. Pomerance (1992) A rigorous time bound for factoring integers. J. Amer. Math. Soc. 5 ( 3), pp. 483–516. Cited by: §5.
- [24] G. Martin (1999) Dense egyptian fractions. Trans. Amer. Math. Soc. 351 ( 9), pp. 3641–3657. Cited by: §1.
- [25] L. J. Mordell (1969) Diophantine equations. Pure and Applied Mathematics, Vol. 30, Academic Press, London and New York. Cited by: §3.
- [26] L. A. Rosati (1954) Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}. Boll. Un. Mat. Ital. (3) 9, pp. 59–63. Cited by: §3, §3.
- [27] C. Sándor (2003) On the number of solutions of the Diophantine equation ∑ i = 1 n 1 x i = 1 \sum^{n}_{i=1}\frac{1}{x_{i}}=1. Period. Math. Hungar. 47 ( 1-2), pp. 215–219. Cited by: §1.
- [28] B. M. Stewart (1964) Theory of numbers. second edition edition, The Macmillan Company, New York, Collier-Macmillan Limited, London. Cited by: §3.
- [29] G. Tenenbaum (2008) Introduction à la théorie analytique et probabiliste des nombres. third edition edition, Éditions Belin, Paris. Cited by: §7, §7.
- [30] T. Xylouris (2011) Über die nullstellen der dirichletschen L L -funktionen und die kleinste primzahl in einer arithmetischen progression. Universität Bonn. Note: PhD thesis Cited by: Remark 4.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:elsholtz@math.tugraz.at
[4]: mailto:planitzer@math.tugraz.at
