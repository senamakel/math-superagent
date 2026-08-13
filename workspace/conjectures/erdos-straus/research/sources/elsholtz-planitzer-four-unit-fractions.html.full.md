<!-- source: https://arxiv.org/html/2012.05984 | converted from HTML -->

Sums of four and more unit fractionsand approximate parametrizations

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2012.05984v1 [math.NT] 10 Dec 2020

# Sums of four and more unit fractions
and approximate parametrizations

Christian Elsholtz C. Elsholtz Graz University of Technology, Institute of Analysis and Number Theory, Kopernikusgasse 24/II, 8010 Graz, Austria Email address: [elsholtz@math.tugraz.at][3] and Stefan Planitzer S. Planitzer Email address: [stefan.planitzer@gmail.com][4]

###### Abstract.

We prove new upper bounds on the number of representations of rational numbers m n \frac{m}{n} as a sum of 4 4 unit fractions, giving five different regions, depending on the size of m m in terms of n n. In particular, we improve the most relevant cases, when m m is small, and when m m is close to n n. The improvements stem from not only studying complete parametrizations of the set of solutions, but simplifying this set appropriately. Certain subsets of all parameters define the set of all solutions, up to applications of divisor functions, which has little impact on the upper bound of the number of solutions. These “approximate parametrizations” were the key point to enable computer programmes to filter through large number of equations and inequalities. Furthermore, this result leads to new upper bounds for the number of representations of rational numbers as sums of more than 4 4 unit fractions.

###### Key words and phrases:

unit fractions, Erdős-Straus equation, Diophantine equations

###### 2020 Mathematics Subject Classification

Primary: 11D68, Secondary: 11D72.

###### 2010 Mathematics Subject Classification

Primary: 11D68, Secondary: 11D72

## 1. Introduction

We consider the problem of representing an arbitrary positive rational number m n \frac{m}{n} as a sum of k k unit fractions. This leads to Diophantine equations of the form

(1) |  | m n = ∑ i = 1 k 1 a i. \frac{m}{n}=\sum_{i=1}^{k}\frac{1}{a_{i}}. |  |

This equation has been studied from a variety of different view points, we only mention results of Croot [3], Graham [8], Konyagin [11] and Martin [12].

In this paper we are interested in upper bounds for the number of solutions of ( 1) in ( a 1, …, a k) ∈ ℕ k (a_{1},\ldots,a_{k})\in\mathbb{N}^{k}, in particular for fixed m, n, k ∈ ℕ m,n,k\in\mathbb{N}, where we consider the a i a_{i} to be given in increasing order.

The most important special case of equation ( 1) is when m = 4 m=4 and k = 3 k=3 which is linked to the famous Erdős-Straus conjecture. This conjecture states that for any n ≥ 2 n\geq 2, the rational number 4 n \frac{4}{n} has a representation as a sum of three unit fractions (see [7]).

For a survey of recent results and for later use we borrow the following notation from [2]:

 | f k ( m, n) = | { ( a 1, …, a k) ∈ ℕ k: a 1 ≤ … ≤ a k, m n = ∑ i = 1 k 1 a i } |. f_{k}(m,n)=\bigg|\bigg\{(a_{1},\ldots,a_{k})\in\mathbb{N}^{k}:a_{1}\leq\ldots\leq a_{k},\frac{m}{n}=\sum_{i=1}^{k}\frac{1}{a_{i}}\bigg\}\bigg|. |  |

In case of the Erdős-Straus equation with n = p n=p prime, Elsholtz and Tao [5] proved that

(2) |  | f 3 ( 4, p) ≪ ε p 3 / 5 + ε. f_{3}(4,p)\ll_{\varepsilon}p^{\nicefrac{{3}}{{5}}+\varepsilon}. |  |

For general m, n ∈ ℕ m,n\in\mathbb{N} we have that

(3) |  | f 3 ( m, n) ≪ ε n ε ( n m) 2 / 3 (Browning and Elsholtz [2]) f_{3}(m,n)\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n}{m}\bigg)^{\nicefrac{{2}}{{3}}}\qquad\text{(Browning and Elsholtz~\cite[cite]{[\@@bibref{}{BrowningElsholtz}{}{}]})} |  |

and

(4) |  | f 3 ( m, n) ≪ ε n ε ( n 3 m 2) 1 / 5 (Elsholtz and Planitzer [4]). f_{3}(m,n)\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n^{3}}{m^{2}}\bigg)^{\nicefrac{{1}}{{5}}}\qquad\text{(Elsholtz and Planitzer~\cite[cite]{[\@@bibref{}{ElsholtzPlanitzer}{}{}]}).} |  |

Note that the upper bound in ( 4) is stronger than ( 3) if m ≪ n 1 / 4 m\ll n^{\nicefrac{{1}}{{4}}}. In particular the bound in ( 4) allows to deduce the Elsholtz-Tao exponent 3 / 5 3/5 in ( 2) for the Erdős-Straus equation also for general denominators n n.

Concerning sums of more than 3 3 unit fractions the following upper bounds were proved in [2]): for any ε > 0 \varepsilon>0

(5) |  | f 4 ( m, n) ≪ ε n ε { ( n m) 5 3 + n 4 3 m 2 3 }, f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\Big\{\Big(\frac{n}{m}\Big)^{\frac{5}{3}}+\frac{n^{\frac{4}{3}}}{m^{\frac{2}{3}}}\Big\}, |  |

and for k ≥ 5 k\geq 5

(6) |  | f k ( m, n) ≪ ε ( k n) ε ( k 4 3 ​ n 2 m) ( 5 / 3) ⋅ 2 k − 5. f_{k}(m,n)\ll_{\varepsilon}(kn)^{\varepsilon}\Big(\frac{k^{\frac{4}{3}}n^{2}}{m}\Big)^{(\nicefrac{{5}}{{3}})\cdot 2^{k-5}}. |  |

This was improved in [4]:

(7) |  | f 4 ( m, n) ≪ ε n ε ( n 4 / 3 m 2 / 3 + n 28 / 17 m 8 / 5) f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}\bigg) |  |

and

(8) |  | f k ( m, n) ≪ ε ( k n) ε ( k 4 / 3 ​ n 2 m) ( 28 / 17) ⋅ 2 k − 5, for k ≥ 5. f_{k}(m,n)\ll_{\varepsilon}(kn)^{\varepsilon}\bigg(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\bigg)^{(\nicefrac{{28}}{{17}})\cdot 2^{k-5}},\qquad\text{for }k\geq 5. |  |

In case of k = 3 k=3 the bounds in ( 2 – 4) were derived by analyzing suitable parametrizations of solutions of equation ( 1) together with an application of the classical divisor bound. The method of Elsholtz and Tao [5] leading to ( 2) is possibly the limit of that method, and the same seems to be true for the bound in ( 4) (at least for constant m m). However, we believe that these bounds are still quite far from the truth. Indeed, it was suggested by Heath-Brown to Elsholtz that even f 3 ​ ( m, n) = 𝒪 ε ​ ( n ε) f_{3}(m,n)=\mathcal{O}_{\varepsilon}(n^{\varepsilon}) appears possible, as n n tends to infinity. More generally, and somewhat stronger, we think that it is also quite possible that the following conjecture holds true.

###### Conjecture 1.

For k, m k,m fixed and n → ∞ n\rightarrow\infty we have

 | f k ​ ( m, n) ≪ exp ⁡ ( C m, k ​ log ⁡ n log ⁡ log ⁡ n), f_{k}(m,n)\ll\exp\bigg(C_{m,k}\frac{\log n}{\log\log n}\bigg), |  |

for a positive constant C m, k C_{m,k} depending only on m m and k k.

The bounds in ( 7) were derived via an application of a lifting procedure first introduced by Browning and Elsholtz [2]. The improvement in the bounds in ( 7) compared to the original bounds by Browning and Elsholtz comes from taking into account a small part of the information coming from parametrizations of solutions of ( 1) for k = 4 k=4 when lifting from k = 3 k=3.

In this paper, our goal is to prove better upper bounds in the k = 4 k=4 case *directly*by using suitable parametrizations of the solutions and not by lifting from the k = 3 k=3 case. The problem with this approach is, that we want to use a parametrization where the number of parameters increases exponentially with k k. The new method applied does not only use a suitable parametrization but in view of the increased complexity also has a computational part. In particular, we make heavy use of a computer algebra system to accomplish the following tasks:

- •

Find many defining sets. By this we mean subsets of the parameters such that once they are fixed, we have at most of order n ε n^{\varepsilon} choices for the remaining parameters.

- •

Find products of parameters which are small in terms of n n and such that the parameters appearing as factors may be partitioned into many defining sets.

Note that what we call “defining sets” above are approximate parametrizations in some sense. “Defining sets” are not in one-to-one correspondence with solutions of equation ( 1) as we would have with a full parametrization. Nonetheless, fixing integer values for all parameters in a “defining set” allows for very few (in our sense 𝒪 ε ​ ( n ε) \mathcal{O}_{\varepsilon}(n^{\varepsilon})) solutions for this equation instead of just a single one.

Our main result is the following.

###### Theorem 1.

For m, n ∈ ℕ m,n\in\mathbb{N} we have

 | f 4 ( m, n) ≪ ε n ε min { n 3 / 2 m 3 / 4, n 8 / 5 m }. f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\min\bigg\{\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}},\frac{n^{\nicefrac{{8}}{{5}}}}{m}\bigg\}. |  |

Together with the two bounds in ( 5) and ( 7) this gives:

###### Corollary 1.

For m, n ∈ ℕ m,n\in\mathbb{N} we have

 | f 4 ( m, n) ≪ ε n ε min { n 3 / 2 m 3 / 4, n 8 / 5 m, ( n 4 / 3 m 2 / 3 + n 28 / 17 m 8 / 5), ( ( n m) 5 3 + n 4 3 m 2 3) }. f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\min\bigg\{\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}},\frac{n^{\nicefrac{{8}}{{5}}}}{m},\bigg(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}\bigg),\bigg(\Big(\frac{n}{m}\Big)^{\frac{5}{3}}+\frac{n^{\frac{4}{3}}}{m^{\frac{2}{3}}}\bigg)\bigg\}. |  |

This new result shows that the analysis of the number sums of 4 and more unit fractions might be much more complicated than was previously known.

###### Remark 1.

In equation ( 1) one generally has that a 1 ≪ n, a 2 ≪ n 2, a 3 ≪ n 4 a_{1}\ll n,a_{2}\ll n^{2},a_{3}\ll n^{4}. Hence there are at most 𝒪 ⁡ ( n 7) {\mathcal{O}}(n^{7}) choices for a 1, a 2 a_{1},a_{2} and a 3 a_{3}, and then a 4 a_{4} is unique, if it exists. Hence f 4 ​ ( m, n) ≪ n 7 f_{4}(m,n)\ll n^{7} is a completely trivial upper bound. However, fixing only a 1 a_{1} and a 2 a_{2} one sees that the number of pairs ( a 3, a 4) (a_{3},a_{4}) is bounded by a divisor function, (for details see e.g. [4]). Hence f 4 ​ ( m, n) ≪ n 3 + ε f_{4}(m,n)\ll n^{3+\varepsilon} is still a trivial upper bound. The worst we would get from Theorem 1, when m m is small, would be an upper bound of order n 3 / 2 + ε n^{\nicefrac{{3}}{{2}}+\varepsilon}.

Furthermore, if we compare the two upper bounds on f 4 ​ ( m, n) f_{4}(m,n) in Theorem 1 with the previous bounds n ε ​ ( ( n 28 / 17 m 8 / 5 + n 4 3 m 2 3) CLOSE n^{\varepsilon}\Big(\Big(\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}+\frac{n^{\frac{4}{3}}}{m^{\frac{2}{3}}}\Big) in ( 7) and n ε ​ ( ( n m) 5 / 3 + n 4 / 3 m 2 / 3) n^{\varepsilon}\big(\big(\frac{n}{m}\big)^{\nicefrac{{5}}{{3}}}+\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}\big) in ( 5), we see that each of these four bounds is best in some cases, and when splitting the contributions of the two parts in 𝒪 ⁡ ( n 28 / 17 m 8 / 5 + n 4 / 3 m 2 / 3) \mathcal{O}\Bigl(\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}+\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}\Bigr), we see that there are even five different upper bounds involved:

To present these results in a uniform way we write exponents as α / 30345 \nicefrac{{\alpha}}{{30345}}, where 30345 30345 is the smallest integer avoiding further fractions in the boundaries below. For fractions m n \frac{m}{n} with m = n α / 30345 m=n^{\nicefrac{{\alpha}}{{30345}}}, where α \alpha is a real parameter in 0 ≤ α ≤ 30345 0\leq\alpha\leq 30345, the following holds, (omitting the n ε n^{\varepsilon} factor):

- •

0 ≤ α ≤ 5250 0\leq\alpha\leq 5250: the upper bound of order n 3 / 2 m 3 / 4 \frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}} from Theorem 1 is the sharpest one.

- •

5250 ≤ α ≤ 8925 5250\leq\alpha\leq 8925: the bound n 28 / 17 m 8 / 5 \frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}} from ( 7) gives the best bound.

- •

8925 ≤ α ≤ 10115 8925\leq\alpha\leq 10115: in this range the bound ( n m) 5 / 3 (\frac{n}{m})^{\nicefrac{{5}}{{3}}} from ( 5) yields the lowest upper bound. (Note that 10115 / 30345 = 1 / 3 10115/30345=1/3.)

- •

10115 ≤ α ≤ 10200 10115\leq\alpha\leq 10200. In this very small region the bound n 4 / 3 m 2 / 3 \frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}} from ( 5) gives the best bound.

- •

10200 ≤ α ≤ 24276 10200\leq\alpha\leq 24276. (Note that OPEN 24276 / 30345 = 4 / 5) 24276/30345=4/5). In this region the bound is also n 4 / 3 m 2 / 3 \frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}, but this time it comes from ( 5) and ( 7).

- •

24276 ≤ α ≤ 30345 24276\leq\alpha\leq 30345: the second bound in Theorem 1 which is of order n 8 / 5 m \frac{n^{\nicefrac{{8}}{{5}}}}{m} gives the best bound.

At the points of transition, i.e. α ∈ { 5250, 8925, 10115, 10200, 24276 } \alpha\in\{5250,8925,10115,10200,24276\}, in these inequalities the corresponding upper bounds are equally sharp.

We summarize this in the following corollary.

###### Corollary 2.

For m, n ∈ ℕ m,n\in\mathbb{N} we have

 | f 4 ( m, n) ≪ ε { n ε ​ n 3 / 2 m 3 / 4 if ​ m ≪ n 50 / 289, n ε ​ n 28 / 17 m 8 / 5 if ​ n 50 / 289 ≪ m ≪ n 5 / 17, n ε ​ ( n m) 5 / 3 if ​ n 5 / 17 ≪ m ≪ n 1 / 3, n ε ​ n 4 / 3 m 2 / 3 if ​ n 1 / 3 ≪ m ≪ n 4 / 5, n ε ​ n 8 / 5 m if ​ n 4 / 5 ≪ m ≪ n. f_{4}(m,n)\ll_{\varepsilon}\begin{cases}n^{\varepsilon}\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}}&\text{ if }m\ll n^{\nicefrac{{50}}{{289}}},\\ n^{\varepsilon}\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}&\text{ if }n^{\nicefrac{{50}}{{289}}}\ll m\ll n^{\nicefrac{{5}}{{17}}},\\ n^{\varepsilon}\Big(\frac{n}{m}\Big)^{\nicefrac{{5}}{{3}}}&\text{ if }n^{\nicefrac{{5}}{{17}}}\ll m\ll n^{\nicefrac{{1}}{{3}}},\\ n^{\varepsilon}\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}&\text{ if }n^{\nicefrac{{1}}{{3}}}\ll m\ll n^{\nicefrac{{4}}{{5}}},\\ n^{\varepsilon}\frac{n^{\nicefrac{{8}}{{5}}}}{m}&\text{ if }n^{\nicefrac{{4}}{{5}}}\ll m\ll n.\end{cases} |  |

[image: Refer to caption] Figure 1. The full range with 0 ≤ c = α / 30345 ≤ 1 0\leq c=\alpha/30345\leq 1.

Recall that the new bounds are the blue line (strongest on the left hand side), and beige, (strongest on the right hand side of the graph).

[image: Refer to caption] Figure 2. The region 0.24 ≤ c ≤ 0.35 0.24\leq c\leq 0.35 enlarged, to see the crossing of almost parallel lines.

###### Remark 2.

In the proof of Theorem 1 we give a method for constructing all representations of a rational number m n \frac{m}{n} as a sum of four unit fractions. Along the same lines as the proof of the corresponding result on sums of three unit fractions in [4], it can be shown that there exists an algorithm with expected running time of order

 | n ε ​ min ⁡ { n 3 / 2 m 3 / 4, n 8 / 5 m, ( n 4 / 3 m 2 / 3 + n 28 / 17 m 8 / 5), ( ( n m) 5 3 + n 4 3 m 2 3) } n^{\varepsilon}\min\bigg\{\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}},\frac{n^{\nicefrac{{8}}{{5}}}}{m},\bigg(\frac{n^{\nicefrac{{4}}{{3}}}}{m^{\nicefrac{{2}}{{3}}}}+\frac{n^{\nicefrac{{28}}{{17}}}}{m^{\nicefrac{{8}}{{5}}}}\bigg),\bigg(\Big(\frac{n}{m}\Big)^{\frac{5}{3}}+\frac{n^{\frac{4}{3}}}{m^{\frac{2}{3}}}\bigg)\bigg\} |  |

listing these solutions. In particular, we can decide within the same time constraints whether or not the rational number m n \frac{m}{n} has a representation of this form. A precise formulation of this result would make use of the complexity of factorizations. For details we refer to [4].

Again the bound on sums of four unit fractions can be lifted to upper bounds for k > 4 k>4.

###### Theorem 2.

For m, n ∈ ℕ m,n\in\mathbb{N} and k ≥ 5 k\geq 5 we have

 | f k ( m, n) ≪ ε ( k n) ε ( k 4 / 3 ​ n 2 m) ( 8 / 5) ⋅ 2 k − 5. f_{k}(m,n)\ll_{\varepsilon}(kn)^{\varepsilon}\bigg(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\bigg)^{(\nicefrac{{8}}{{5}})\cdot 2^{k-5}}. |  |

Note that the improvement in the upper bound in Theorem 2 concerns the constant 8 5 \frac{8}{5} in the exponent. If we compare the result with the bounds in ( 7), we see that, depending on k k, the difference in the corresponding exponents of n n is 4 85 ⋅ 2 k − 4 \frac{4}{85}\cdot 2^{k-4}.

The results in Theorem 2 immediately improve several upper bounds for the special case of representing 1 1 as a sum of unit fractions. Some of these results are mentioned in [2] with improved upper bounds in [4]. Here we just reformulate [4] *Corollary 3 by giving the improved upper bounds one gets by using Theorem 2. The proof is the same as in [4] and [2] after plugging in the new bound.

###### Corollary 3.

1. (1)

For any ε > 0 \varepsilon>0, we have that

 | f k ( 1, 1) ≪ ε k ( 2 / 15) ⋅ 2 k − 1 + ε. f_{k}(1,1)\ll_{\varepsilon}k^{(\nicefrac{{2}}{{15}})\cdot 2^{k-1}+\varepsilon}. |  |

2. (2)

Let ( u n) n ∈ ℕ (u_{n})_{n\in\mathbb{N}} be the sequence recursively defined by u 0 = 1 u_{0}=1 and u n + 1 = u n ​ ( u n + 1) u_{n+1}=u_{n}(u_{n}+1) and set c 0 = lim n → ∞ u n 2 − n c_{0}=\lim_{n\rightarrow\infty}u_{n}^{2^{-n}}. Then for ε > 0 \varepsilon>0 and k ≥ k ⁡ ( ε) k\geq k(\varepsilon) we have

 | f k ​ ( 1, 1) < c 0 ( 2 / 5 + ε) ​ 2 k − 1. f_{k}(1,1)<c_{0}^{(\nicefrac{{2}}{{5}}+\varepsilon)2^{k-1}}. |  |

3. (3)

For ε > 0 \varepsilon>0 and k ≥ k ⁡ ( ε) k\geq k(\varepsilon) the number of positive integer solutions of the equation

 | 1 = ∑ i = 1 k 1 a i + 1 ∏ i = 1 k a i 1=\sum_{i=1}^{k}\frac{1}{a_{i}}+\frac{1}{\prod_{i=1}^{k}a_{i}} |  |

is bounded from above by c 0 ( 2 / 5 + ε) ​ 2 k c_{0}^{(\nicefrac{{2}}{{5}}+\varepsilon)2^{k}}.

###### Remark 3.

The sequence u n u_{n}, starting with 1, 2, 6, 42, 1806, … 1,2,6,42,1806,\ldots is listed as A007018 in the online encyclopedia of integer seqeuences (OEIS), and is a shifted copy of the well known Sylvester sequence (A000058 of the OEIS): 2, 3, 7, 43, 1807, … 2,3,7,43,1807,\ldots It is known that the limit c 0 = lim n → ∞ u n 2 − n = 1.5979102 ​ … c_{0}=\lim_{n\rightarrow\infty}u_{n}^{2^{-n}}=1.5979102\ldots exists and is irrational, for details see [1] and [13]. Graham, Knuth and Patashnik [9, Exercise 4.37] sketch a proof of (in our notation) u n = ⌊ c 0 2 n − 1 2 ⌋ u_{n}=\lfloor c_{0}^{2^{n}}-\frac{1}{2}\rfloor. The existence of the limit can be proved directly, as it follows inductively that u n ≤ 2 2 n 2 u_{n}\leq\frac{2^{2^{n}}}{2}, so that the sequence q n:= ( u n) 1 / 2 n q_{n}:=(u_{n})^{1/2^{n}} is bounded from above by 2 2, and u n + 1 ≥ u n 2 u_{n+1}\geq u_{n}^{2} implies that ( u n + 1) 1 / 2 n + 1 ≥ ( u n) 1 / 2 n (u_{n+1})^{1/2^{n+1}}\geq(u_{n})^{1/2^{n}}, so that the sequence of the q n q_{n} is also monotonically increasing.

At the end of this introduction we want to comment on the most important aspects of the notation used in the following. The letters ℕ \mathbb{N} and ℙ \mathbb{P}, as usual, denote the sets of positive integers and positive primes. The function d ⁡ ( n) d(n) denotes the number of positive divisors of n n. By ν p ​ ( n) \nu_{p}(n), p ∈ ℙ p\in\mathbb{P}, we denote the p p -adic valuation of n n, i.e. the highest power of p p dividing n n. We use the symbols ≪ \ll and 𝒪 \mathcal{O} in the contexts of the well known Vinogradov- and Landau-notations. Dependencies of the implied constants on additional parameters will be indicated by a subscript.

## 2. Patterns and parameters

In this section, we introduce a method of parametrization for solutions of equation ( 1) which is based on what we will call relative greatest common divisors and patterns. This type of parametrization has been used before in connection with sums of unit fractions. Elsholtz first used relative greatest common divisors as described below in [6] while patterns played a role in proving results in [4]. For a more thorough introduction to this method and for some historical comments see [6] and [4].

We start by writing the denominators of the unit fractions on the right hand side of equation ( 1) as a i = n i ​ t i a_{i}=n_{i}t_{i}, where n i = gcd ⁡ ( a i, n) n_{i}=\gcd(a_{i},n). We note that by definition gcd ⁡ ( t i, n n i) = 1 \gcd\big(t_{i},\frac{n}{n_{i}}\big)=1 and for given ( a 1, …, a k) ∈ ℕ k (a_{1},\ldots,a_{k})\in\mathbb{N}^{k} we call ( n 1, …, n k) ∈ ℕ k (n_{1},\ldots,n_{k})\in\mathbb{N}^{k} the pattern of the solution. To bound the number of patterns for given n ∈ ℕ n\in\mathbb{N}, we make use of the classical divisor bound which was also one of the main ingredients in Elsholtz and Tao’s proof of an upper bound for f 3 ​ ( 4, p) f_{3}(4,p) in [5]. We will use it in the following form (see [10] *Theorem 315).

###### Lemma A (Classical divisor bound).

Let d ⁡ ( n) = ∑ d | n 1 d(n)=\sum_{d|n}1 be the number of positive divisors of an integer n n. Then for any ε > 0 \varepsilon>0, we have

 | d ( n) ≪ ε n ε. d(n)\ll_{\varepsilon}n^{\varepsilon}. |  |

When trying to find upper bounds on f 4 ​ ( m, n) f_{4}(m,n), we can consider the pattern of the solutions to be fixed, since the upper bound we will establish is independent of the pattern. Lemma A tells us, that we have at most 𝒪 ε ​ ( n ϵ) \mathcal{O}_{\varepsilon}(n^{\epsilon}) such patterns and when looking at the result in Theorem 1 we see that an additional factor of n ε n^{\varepsilon} does not change the upper bound there. Hence from now on we consider the pattern ( n 1, n 2, n 3, n 4) (n_{1},n_{2},n_{3},n_{4}) to be fixed.

Note that the trivial upper bound for the number of patterns would rather be of order n 4 ​ ε n^{4\varepsilon} and to get the above bound we need to redefine ε \varepsilon. Also below we will often apply the divisor bound several times in a row to conclude, that there are at most of order n ε n^{\varepsilon} choices for some parameters. In any such situation this upper bound is achieved after possibly redefining ε \varepsilon, and we will not explicitly state this henceforth.

Next we set I = { 1, …, k } I=\{1,\ldots,k\} to be the index set and write the factors t i t_{i} as a product of what we want to call relative greatest common divisors denoted by x J x_{J}, J = { i 1, …, i | J | } ⊂ I J=\{i_{1},\ldots,i_{|J|}\}\subset I. Here we recursively define these relative greatest common divisors x J x_{J} as follows:

 | x I = gcd ⁡ ( t 1, …, t k) ​ and ​ x J = gcd ⁡ ( t i 1, …, t i | J |) ∏ J ⊊ K x K ​ for ​ J ⊊ I. x_{I}=\gcd(t_{1},\ldots,t_{k})\text{ and }x_{J}=\frac{\gcd(t_{i_{1}},\ldots,t_{i_{|J|}})}{\prod_{J\subsetneq K}x_{K}}\text{ for }J\subsetneq I. |  |

With this definition, we have

 | t i = ∏ J ⊂ I i ∈ J x J ​ for ​ 1 ≤ i ≤ k t_{i}=\prod_{\begin{subarray}{c}J\subset I\\ i\in J\end{subarray}}x_{J}\text{ for }1\leq i\leq k |  |

and it is easy to see that

(9) |  | gcd ⁡ ( x J, x K) = 1 ​ whenever ​ J ⊈ K ​ and ​ K ⊈ J. \gcd(x_{J},x_{K})=1\text{ whenever }J\nsubseteq K\text{ and }K\nsubseteq J. |  |

See e.g. [4] for a short proof of the last statement.

To keep things readable, and since in the cases we use it no ambiguity will arise, below we will often resort to the following simplified notation. If J = { i 1, …, i | J | } J=\{i_{1},\ldots,i_{|J|}\} and the i j i_{j} are given in increasing order, then we write

 | x J = x i 1 ​ i 2 ​ … ​ i | J |. x_{J}=x_{i_{1}i_{2}\ldots i_{|J|}}. |  |

We now apply this parametrization and patterns in the special case of sums of 4 4 unit fractions, i.e. equation ( 1) with k = 4 k=4:

 | m n = 1 a 1 + ⋯ + 1 a 4, \frac{m}{n}=\frac{1}{a_{1}}+\cdots+\frac{1}{a_{4}}, |  |

where a 1 ≤ … ≤ a 4 a_{1}\leq\ldots\leq a_{4}. Let ( n 1, …, n 4) (n_{1},\ldots,n_{4}) be our fixed pattern and thus a i = n i ​ t i a_{i}=n_{i}t_{i} for 1 ≤ i ≤ 4 1\leq i\leq 4.

We use relative greatest common divisors and the fixed pattern to write

(10) |  | m n = 1 n 1 ​ x 1 ​ x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234 + 1 n 2 ​ x 2 ​ x 12 ​ x 23 ​ x 24 ​ x 123 ​ x 124 ​ x 234 ​ x 1234 + 1 n 3 ​ x 3 ​ x 13 ​ x 23 ​ x 34 ​ x 123 ​ x 134 ​ x 234 ​ x 1234 + 1 n 4 ​ x 4 ​ x 14 ​ x 24 ​ x 34 ​ x 124 ​ x 134 ​ x 234 ​ x 1234. \begin{split}\frac{m}{n}=&\frac{1}{n_{1}x_{1}x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234}}+\frac{1}{n_{2}x_{2}x_{12}x_{23}x_{24}x_{123}x_{124}x_{234}x_{1234}}+\\ &\frac{1}{n_{3}x_{3}x_{13}x_{23}x_{34}x_{123}x_{134}x_{234}x_{1234}}+\frac{1}{n_{4}x_{4}x_{14}x_{24}x_{34}x_{124}x_{134}x_{234}x_{1234}}.\end{split} |  |

Next we multiply the last equation by n n and the least common denominator of the unit fractions on the right hand side. Note that after doing so, the variable x i x_{i}, for 1 ≤ i ≤ 4 1\leq i\leq 4, appears in exactly three of the four summands on the right hand side and in the product on the left hand side. This means that also the fourth summand on the right hand side, of which x i x_{i} is not a factor, has to be divisible by x i x_{i}. This factor is of the form

 | n n i ​ ∏ J ⊂ I i ∉ J x J, \frac{n}{n_{i}}\prod_{\begin{subarray}{c}J\subset I\\ i\not\in J\end{subarray}}x_{J}, |  |

where we use the set-index notation for convenience. By ( 9), x i x_{i} is coprime to ∏ J ⊂ I i ∉ J x J \prod_{\begin{subarray}{c}J\subset I\\ i\not\in J\end{subarray}}x_{J}. Furthermore, by the definition of a pattern, we also have gcd ⁡ ( x i, n n i) = 1 \gcd\big(x_{i},\frac{n}{n_{i}}\big)=1, which leaves x i = 1 x_{i}=1 for 1 ≤ i ≤ 4 1\leq i\leq 4. With this simplification we get

(11) |  | m ​ x 12 ​ x 13 ​ x 14 ​ x 23 ​ x 24 ​ x 34 ​ x 123 ​ x 124 ​ x 134 ​ x 234 ​ x 1234 = n n 1 ​ x 23 ​ x 24 ​ x 34 ​ x 234 + n n 2 ​ x 13 ​ x 14 ​ x 34 ​ x 134 + n n 3 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ x 12 ​ x 13 ​ x 23 ​ x 123. \begin{split}mx_{12}x_{13}x_{14}x_{23}x_{24}x_{34}x_{123}x_{124}x_{134}x_{234}x_{1234}=&\frac{n}{n_{1}}x_{23}x_{24}x_{34}x_{234}+\frac{n}{n_{2}}x_{13}x_{14}x_{34}x_{134}+\\ &\frac{n}{n_{3}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}}x_{12}x_{13}x_{23}x_{123}.\end{split} |  |

We introduce the parameters d { i, j } = d i ​ j = gcd ⁡ ( n n i, n n j) d_{\{i,j\}}=d_{ij}=\gcd\big(\frac{n}{n_{i}},\frac{n}{n_{j}}\big) for 1 ≤ i < j ≤ 4 1\leq i<j\leq 4 and d { i, j, k } = d i ​ j ​ k = gcd ⁡ ( n n i, n n j, n n k) d_{\{i,j,k\}}=d_{ijk}=\gcd\big(\frac{n}{n_{i}},\frac{n}{n_{j}},\frac{n}{n_{k}}\big) for 1 ≤ i < j < k ≤ 4 1\leq i<j<k\leq 4 and we note that they are fixed by the pattern ( n 1, …, n 4) (n_{1},\ldots,n_{4}). Furthermore, again by definition of a pattern, we have that d i ​ j d_{ij} is coprime to all relative greatest common divisors with an i i or a j j in the index. The same holds true for d i ​ j ​ k d_{ijk} and relative greatest common divisors with an i i, j j or k k in the index.

In [2], [4] and [5] it turned out to be useful to consider divisibility relations in the equation corresponding to ( 11) in the three unit fractions case. We will also do this and define the following integer parameters:

(12) |  | z 23 = n n 2 ​ d 23 ​ x 13 ​ x 34 ​ x 134 + n n 3 ​ d 23 ​ x 12 ​ x 24 ​ x 124 x 23 z 34 = n n 3 ​ d 34 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ d 34 ​ x 13 ​ x 23 ​ x 123 x 34 \begin{split}z_{23}&=\frac{\frac{n}{n_{2}d_{23}}x_{13}x_{34}x_{134}+\frac{n}{n_{3}d_{23}}x_{12}x_{24}x_{124}}{x_{23}}\\ z_{34}&=\frac{\frac{n}{n_{3}d_{34}}x_{14}x_{24}x_{124}+\frac{n}{n_{4}d_{34}}x_{13}x_{23}x_{123}}{x_{34}}\end{split} |  |

(13) |  | z 123 = n n 1 ​ d 123 ​ x 23 ​ x 24 ​ x 34 ​ x 234 + n n 2 ​ d 123 ​ x 13 ​ x 14 ​ x 34 ​ x 134 + n n 3 ​ d 123 ​ x 12 ​ x 14 ​ x 24 ​ x 124 x 12 ​ x 13 ​ x 23 ​ x 123 z 134 = n n 1 ​ d 134 ​ x 23 ​ x 24 ​ x 34 ​ x 234 + n n 3 ​ d 134 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ d 134 ​ x 12 ​ x 13 ​ x 23 ​ x 123 x 13 ​ x 14 ​ x 34 ​ x 134 z 234 = n n 2 ​ d 234 ​ x 13 ​ x 14 ​ x 34 ​ x 134 + n n 3 ​ d 234 ​ x 12 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ d 234 ​ x 12 ​ x 13 ​ x 23 ​ x 123 x 23 ​ x 24 ​ x 34 ​ x 234. \begin{split}z_{123}&=\frac{\frac{n}{n_{1}d_{123}}x_{23}x_{24}x_{34}x_{234}+\frac{n}{n_{2}d_{123}}x_{13}x_{14}x_{34}x_{134}+\frac{n}{n_{3}d_{123}}x_{12}x_{14}x_{24}x_{124}}{x_{12}x_{13}x_{23}x_{123}}\\ z_{134}&=\frac{\frac{n}{n_{1}d_{134}}x_{23}x_{24}x_{34}x_{234}+\frac{n}{n_{3}d_{134}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}d_{134}}x_{12}x_{13}x_{23}x_{123}}{x_{13}x_{14}x_{34}x_{134}}\\ z_{234}&=\frac{\frac{n}{n_{2}d_{234}}x_{13}x_{14}x_{34}x_{134}+\frac{n}{n_{3}d_{234}}x_{12}x_{14}x_{24}x_{124}+\frac{n}{n_{4}d_{234}}x_{12}x_{13}x_{23}x_{123}}{x_{23}x_{24}x_{34}x_{234}}.\end{split} |  |

In the following we will only use the parameters z J z_{J} defined above. For a general definition of z J z_{J}, J ⊂ { 1, …, 4 } J\subset\{1,\ldots,4\}, 2 ≤ | J | ≤ 3 2\leq|J|\leq 3, see Section 6.

## 3. Defining sets for sums of four unit fractions

In this section, we will determine several defining sets for sums of four unit fractions. We define these sets in the following way.

###### Definition 1.

Let m, n ∈ ℕ m,n\in\mathbb{N}, ( n 1, …, n 4) ∈ ℕ 4 (n_{1},\ldots,n_{4})\in\mathbb{N}^{4} be a fixed pattern, I = { 1, …, 4 } I=\{1,\ldots,4\} and 𝒫 = 𝒳 ∪ 𝒵 \mathcal{P}=\mathcal{X}\cup\mathcal{Z}, where

(14) |  | 𝒳 = { x J: J ⊂ I, | J | ≥ 2 } and 𝒵 = { z J: J ⊂ I, 2 ≤ | J | ≤ 3 } \mathcal{X}=\big\{x_{J}:J\subset I,|J|\geq 2\big\}\text{ and }\mathcal{Z}=\{z_{J}:J\subset I,2\leq|J|\leq 3\} |  |

are the sets of parameters introduced in Section 2. We call a set S ⊂ P S\subset P a (four unit fractions) defining set, if assigning a positive integer value to every parameter in S S allows for at most 𝒪 ε ​ ( n ε) \mathcal{O}_{\varepsilon}(n^{\varepsilon}) positive integer assignments to variables in 𝒳 \ S \mathcal{X}\backslash S such that

 | m n = ∑ i = 1 4 1 n i ​ ∏ J ⊂ I i ∈ J | J | ≥ 2 x J. \frac{m}{n}=\sum_{i=1}^{4}\frac{1}{n_{i}\prod_{\begin{subarray}{c}J\subset I\\ i\in J\\ |J|\geq 2\end{subarray}}x_{J}}. |  |

Note that the idea behind the “defining sets” was already applied in [5] *Section 3 and [4] when dealing with sums of three unit fractions (in [4] actually also in the four unit fractions case, but to a very limited extent). Since the larger number of parameters in the four unit fractions case leads to a lot more possibilities for defining sets than we had when dealing with sums of three unit fractions, it seems impractical to determine these sets by hand. In Section 6, we describe how we computed many defining sets via a structured approach using a computer algebra system. Any of these new defining sets can easily be verified by hand. In particular, we will prove the following Lemma, which covers only the defining sets used to prove Theorem 1.

###### Lemma 1.

The following sets are four unit fractions defining sets:

1. (1)

{ z 23, z 234 } \{z_{23},z_{234}\},

2. (2)

{ z 234, x 23, x 24 } \{z_{234},x_{23},x_{24}\},

3. (3)

{ z 234, x 23, x 234 } \{z_{234},x_{23},x_{234}\},

4. (4)

{ z 34, x 12, x 123, x 124, x 1234 } \{z_{34},x_{12},x_{123},x_{124},x_{1234}\},

5. (5)

{ x 12, x 13, x 24, x 34, x 123, x 124, x 134, x 1234 } \{x_{12},x_{13},x_{24},x_{34},x_{123},x_{124},x_{134},x_{1234}\},

6. (6)

{ x 12, x 13, x 14, x 23, x 123, x 124, x 134, x 234, x 1234 } \{x_{12},x_{13},x_{14},x_{23},x_{123},x_{124},x_{134},x_{234},x_{1234}\}.

###### Proof.

With the help of equations ( 11 - 13) we derive the following set of equations:

(15) |  | m ​ x 14 ​ x 24 ​ x 34 ​ x 124 ​ x 134 ​ x 234 ​ x 1234 \displaystyle mx_{14}x_{24}x_{34}x_{124}x_{134}x_{234}x_{1234} | = d 123 ​ z 123 + n n 4, \displaystyle=d_{123}z_{123}+\frac{n}{n_{4}}, |  |

(16) |  | m ​ x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234 \displaystyle mx_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234} | = d 234 ​ z 234 + n n 1, \displaystyle=d_{234}z_{234}+\frac{n}{n_{1}}, |  |

(17) |  | z 23 ​ x 23 \displaystyle z_{23}x_{23} | = n n 2 ​ d 23 ​ x 13 ​ x 34 ​ x 134 + n n 3 ​ d 23 ​ x 12 ​ x 24 ​ x 124, \displaystyle=\frac{n}{n_{2}d_{23}}x_{13}x_{34}x_{134}+\frac{n}{n_{3}d_{23}}x_{12}x_{24}x_{124}, |  |

(18) |  | z 34 ​ x 34 \displaystyle z_{34}x_{34} | = n n 3 ​ d 34 ​ x 14 ​ x 24 ​ x 124 + n n 4 ​ d 34 ​ x 13 ​ x 23 ​ x 123, \displaystyle=\frac{n}{n_{3}d_{34}}x_{14}x_{24}x_{124}+\frac{n}{n_{4}d_{34}}x_{13}x_{23}x_{123}, |  |

(19) |  | z 234 ​ x 24 ​ x 34 ​ x 234 \displaystyle z_{234}x_{24}x_{34}x_{234} | = d 23 d 234 ​ x 14 ​ z 23 + n n 4 ​ d 234 ​ x 12 ​ x 13 ​ x 123, \displaystyle=\frac{d_{23}}{d_{234}}x_{14}z_{23}+\frac{n}{n_{4}d_{234}}x_{12}x_{13}x_{123}, |  |

(20) |  | z 234 ​ x 23 ​ x 24 ​ x 234 \displaystyle z_{234}x_{23}x_{24}x_{234} | = d 34 d 234 ​ x 12 ​ z 34 + n n 2 ​ d 234 ​ x 13 ​ x 14 ​ x 134, \displaystyle=\frac{d_{34}}{d_{234}}x_{12}z_{34}+\frac{n}{n_{2}d_{234}}x_{13}x_{14}x_{134}, |  |

(21) |  | z 134 ​ z 234 \displaystyle z_{134}z_{234} | = n 2 n 1 ​ n 2 ​ d 134 ​ d 234 + n 2 ​ d 34 d 134 ​ d 234 ​ z 34 ​ x 12 2 ​ x 123 ​ x 124 ​ x 1234. \displaystyle=\frac{n^{2}}{n_{1}n_{2}d_{134}d_{234}}+\frac{n^{2}d_{34}}{d_{134}d_{234}}z_{34}x_{12}^{2}x_{123}x_{124}x_{1234}. |  |

The method of proof will be as follows. We show that fixing positive integer values for the parameters in the sets in the statement of the lemma fixes the right hand side of at least one of the equations ( 15 – 21). From the divisor bound in Lemma A we may then deduce that we have at most of order n ϵ n^{\epsilon} choices for the variables on the left hand side of the corresponding equation. For any of these choices of new parameters we may then iterate the argument.

Here we note that the right hand sides of equations ( 15 – 21) are at most of polynomial sizes in n n. By definition, the parameters d J d_{J}, J ⊂ { 1, …, 4 } J\subset\{1,\ldots,4\}, 2 ≤ | J | ≤ 3 2\leq|J|\leq 3, are bounded from above by n n. If we have a look at the definition of the parameters in the set 𝒵 \mathcal{Z} in ( 14), we see that they are certainly of size at most polynomial in n n, if the same is true for the parameters in the set 𝒳 \mathcal{X}. To see that the relative greatest common divisors in 𝒳 \mathcal{X} are of size at most polynomial in n n, we use the fact that any of them is a factor of at least two of the denominators a i a_{i}, 1 ≤ i ≤ 4 1\leq i\leq 4. In particular, if we have m n = 1 a 1 + ⋯ + 1 a 4 \frac{m}{n}=\frac{1}{a_{1}}+\cdots+\frac{1}{a_{4}} with 0 < a 1 ≤ … ≤ a 4 0<a_{1}\leq\ldots\leq a_{4}, then

 | m n ≤ 4 a 1 ​ and ​ a 1 ≤ 4 ​ n m. \frac{m}{n}\leq\frac{4}{a_{1}}\text{ and }a_{1}\leq\frac{4n}{m}. |  |

With a similar argument we get

 | m n − 1 a 1 = m ​ a 1 − n n ​ a 1 ≤ 3 a 2 ​ and ​ a 2 ≤ 3 ​ n ​ a 1 ≤ 12 ​ n 2 m. \frac{m}{n}-\frac{1}{a_{1}}=\frac{ma_{1}-n}{na_{1}}\leq\frac{3}{a_{2}}\text{ and }a_{2}\leq 3na_{1}\leq\frac{12n^{2}}{m}. |  |

Finally we derive from the last two inequalities

 | m n − 1 a 1 − 1 a 2 = m ​ a 1 ​ a 2 − n ​ a 1 − n ​ a 2 n ​ a 1 ​ a 2 ≤ 2 a 3 ​ and ​ a 3 ≤ 2 ​ n ​ a 1 ​ a 2 ≤ 96 ​ n 4 m 2. \frac{m}{n}-\frac{1}{a_{1}}-\frac{1}{a_{2}}=\frac{ma_{1}a_{2}-na_{1}-na_{2}}{na_{1}a_{2}}\leq\frac{2}{a_{3}}\text{ and }a_{3}\leq 2na_{1}a_{2}\leq\frac{96n^{4}}{m^{2}}. |  |

We now go through all defining sets in the statement of the Lemma.

1. (1)

Once we fix positive integer values for z 23 z_{23} and z 234 z_{234}, we deduce from equation ( 16), that we have at most of order n ε n^{\varepsilon} may choices for all relative greatest common divisors with a ‘ 1 1 ’ in the index. Equation ( 19) then implies the same for the variables x 24 x_{24}, x 34 x_{34} and x 234 x_{234}. Finally, the missing variable x 23 x_{23} is uniquely determined by ( 11).

2. (2)

We now consider z 234 z_{234}, x 23 x_{23} and x 24 x_{24} to be fixed. Again we have at most of order n ε n^{\varepsilon} choices for all relative greatest common divisors with a ‘ 1 1 ’ in the index by ( 16). Now the same holds true for the parameters z 34 z_{34} and x 34 x_{34} by equation ( 18). Via equation ( 20) we deduce that we have at most of order n ε n^{\varepsilon} choices for the missing parameters x 23 x_{23}, x 24 x_{24} and x 234 x_{234}.

3. (3)

Having assigned positive integer values to the parameters z 234 z_{234}, x 23 x_{23} and x 234 x_{234}, we again use equation ( 19) to deduce, that we have at most of order n ε n^{\varepsilon} many choices for all parameters with a ‘1’ in the index. Now only assignments for the parameters x 24 x_{24} and x 34 x_{34} are missing.

To see that we also have at most of order n ε n^{\varepsilon} many choices for these two parameters, we will apply a method of factoring equation ( 11) which was already used by Browning and Elsholtz [2]. As two of the five terms of equation ( 11) contain the factor x 24 ​ x 34 x_{24}x_{34}, it may be rewritten in the form

 | C 1 ​ x 24 ​ x 34 = C 2 ​ x 24 + C 3 ​ x 34 + C 4 C_{1}x_{24}x_{34}=C_{2}x_{24}+C_{3}x_{34}+C_{4} |  |

and further

 | ( C 1 ​ x 24 − C 3) ​ ( C 1 ​ x 34 − C 2) = C 1 ​ C 4 + C 2 ​ C 3, (C_{1}x_{24}-C_{3})(C_{1}x_{34}-C_{2})=C_{1}C_{4}+C_{2}C_{3}, |  |

where the constants C i C_{i}, 1 ≤ i ≤ 4 1\leq i\leq 4, depend only on relative greatest common divisors x J x_{J} which are known. The last equation implies that also in this case, for the remaining parameters x 24 x_{24} and x 34 x_{34} we have at most of order n ε n^{\varepsilon} many choices.

4. (4)

In the case of z 34 z_{34}, x 12 x_{12}, x 123 x_{123}, x 124 x_{124} and x 1234 x_{1234} being fixed, we see that we have at most of order n ε n^{\varepsilon} choices for the parameters z 134 z_{134} and z 234 z_{234} by equation ( 21). From equations ( 15) and ( 16) we now see that we have at most of order n ε n^{\varepsilon} choices for x 13 x_{13}, x 14 x_{14}, x 24 x_{24}, x 34 x_{34}, x 134 x_{134}, and x 234 x_{234}. This last parameter, x 23 x_{23}, is finally uniquely determined by ( 11).

5. (5)

If all the parameters x 12 x_{12}, x 13 x_{13}, x 24 x_{24}, x 34 x_{34}, x 123 x_{123}, x 124 x_{124}, x 134 x_{134} and x 1234 x_{1234} are fixed, we see from equation ( 17) that we have of order n ε n^{\varepsilon} choices for the parameter x 23 x_{23}. Now only the parameters x 14 x_{14} and x 234 x_{234} are missing. At this point we again use that equation ( 11) factors. Indeed, we may rearrange this equation to take the form

 | C 1 ​ x 14 ​ x 234 = C 2 ​ x 14 + C 3 ​ x 234 + C 4, C_{1}x_{14}x_{234}=C_{2}x_{14}+C_{3}x_{234}+C_{4}, |  |

where C 1 C_{1}, C 2 C_{2}, C 3 C_{3} and C 4 C_{4} are integer constants. This equation factors as in point ( 3), which leads to at most 𝒪 ε ​ ( n ε) \mathcal{O}_{\varepsilon}(n^{\varepsilon}) choices for x 14 x_{14} and x 234 x_{234}.

6. (6)

We now deal with the case when x 12 x_{12}, x 13 x_{13}, x 14 x_{14}, x 23 x_{23}, x 123 x_{123}, x 124 x_{124}, x 134 x_{134}, x 234 x_{234} and x 1234 x_{1234} are all fixed. Note that only the two variables x 24 x_{24} and x 34 x_{34} are missing out. We already proved in point ( 3) that in this case we have at most of order n ε n^{\varepsilon} many choices for these two parameters.

∎

## 4. Upper bounds on sums of 4 unit fractions

In this section, we apply the parametrization introduced in Section 2 and defining sets from Section 3 together with ideas from [5] *Section 3 and [4] to prove Theorem 1. Recall, that with a fixed pattern all variables n i n_{i}, d i ​ j d_{ij} and d i ​ j ​ k d_{ijk} are fixed for 1 ≤ i, j, k ≤ 4 1\leq i,j,k\leq 4 and we have 𝒪 ϵ ​ ( n ϵ) \mathcal{O}_{\epsilon}(n^{\epsilon}) patterns altogether.

We now use the fact that the denominators a i = n i ​ t i a_{i}=n_{i}t_{i} are given in increasing order. The inequalities a 2 ≤ a 3 a_{2}\leq a_{3} and a 3 ≤ a 4 a_{3}\leq a_{4} may be rewritten as

 | x 12 ​ x 24 ​ x 124 ≤ n 3 n 2 ​ x 13 ​ x 34 ​ x 134, x 13 ​ x 23 ​ x 123 ≤ n 4 n 3 ​ x 14 ​ x 24 ​ x 124, x_{12}x_{24}x_{124}\leq\frac{n_{3}}{n_{2}}x_{13}x_{34}x_{134},\quad x_{13}x_{23}x_{123}\leq\frac{n_{4}}{n_{3}}x_{14}x_{24}x_{124}, |  |

by just plugging in the corresponding products of relative greatest common divisors for the t i t_{i}, 2 ≤ i ≤ 4 2\leq i\leq 4. Combining these last inequalities with three of the equations in ( 12) and ( 13) yields

(22) |  | z 23 ​ x 23 \displaystyle z_{23}x_{23} | ≤ 2 ​ n n 2 ​ d 23 ​ x 13 ​ x 34 ​ x 134, \displaystyle\leq\frac{2n}{n_{2}d_{23}}x_{13}x_{34}x_{134}, |  |

(23) |  | z 34 ​ x 34 \displaystyle z_{34}x_{34} | ≤ 2 ​ n n 3 ​ d 34 ​ x 14 ​ x 24 ​ x 124, \displaystyle\leq\frac{2n}{n_{3}d_{34}}x_{14}x_{24}x_{124}, |  |

(24) |  | z 234 ​ x 23 ​ x 24 ​ x 234 \displaystyle z_{234}x_{23}x_{24}x_{234} | ≤ 3 ​ n n 2 ​ d 234 ​ x 13 ​ x 14 ​ x 134. \displaystyle\leq\frac{3n}{n_{2}d_{234}}x_{13}x_{14}x_{134}. |  |

Furthermore, since the denominators a i a_{i} are given in ascending order, we deduce from m n = 1 n 1 ​ t 1 + 1 n 2 ​ t 2 + 1 n 3 ​ t 3 + 1 n 4 ​ t 4 \frac{m}{n}=\frac{1}{n_{1}t_{1}}+\frac{1}{n_{2}t_{2}}+\frac{1}{n_{3}t_{3}}+\frac{1}{n_{4}t_{4}} that m n ≤ 4 n 1 ​ t 1 \frac{m}{n}\leq\frac{4}{n_{1}t_{1}} and hence

(25) |  | t 1 = x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234 ≤ 4 ​ n n 1 ​ m. t_{1}=x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234}\leq\frac{4n}{n_{1}m}. |  |

We now prove the two upper bounds in Theorem 1 separately. We start with the upper bound of order n ε ​ ( n 3 / 2 m 3 / 4) n^{\varepsilon}\big(\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}}\big).

From inequalities ( 23 – 25) we deduce

(26) |  | ( z 234 ​ x 23 ​ x 234) 2 ​ ( z 34 ​ x 12 ​ x 123 ​ x 124 ​ x 1234) ​ ( x 12 ​ x 13 ​ x 24 ​ x 34 ​ x 123 ​ x 124 ​ x 134 ​ x 1234) ​ ( x 12 ​ x 123 ​ x 1234) = z 34 ​ x 34 x 14 ​ x 24 ​ x 124 ​ ( z 234 ​ x 23 ​ x 24 ​ x 234 x 13 ​ x 14 ​ x 134) 2 ​ ( x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234) 3 ≪ n 6 m 3 ​ n 1 3 ​ n 2 2 ​ n 3 ​ d 34 ​ d 234 2 ≪ n 6 m 3. \begin{split}&(z_{234}x_{23}x_{234})^{2}(z_{34}x_{12}x_{123}x_{124}x_{1234})(x_{12}x_{13}x_{24}x_{34}x_{123}x_{124}x_{134}x_{1234})(x_{12}x_{123}x_{1234})=\\ &\frac{z_{34}x_{34}}{x_{14}x_{24}x_{124}}\bigg(\frac{z_{234}x_{23}x_{24}x_{234}}{x_{13}x_{14}x_{134}}\bigg)^{2}(x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234})^{3}\ll\frac{n^{6}}{m^{3}n_{1}^{3}n_{2}^{2}n_{3}d_{34}d_{234}^{2}}\ll\frac{n^{6}}{m^{3}}.\end{split} |  |

Note that any of the factors in parentheses on the left hand side of this inequality, except for the factor ( x 12 ​ x 123 ​ x 1234) (x_{12}x_{123}x_{1234}) is a product of parameters constituting one of the defining sets in Lemma 1. After distributing the exceptional factor among the others, we see that we have 4 4 factors left and that at least one of them is bounded in size by 𝒪 ⁡ ( n 3 / 2 m 3 / 4) \mathcal{O}\big(\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}}\big). Once the bounded factor is fixed we have at most of order n ε n^{\varepsilon} many choices for the corresponding defining set and thus an upper bound of order 𝒪 ⁡ ( n ε ​ n 3 / 2 m 3 / 4) \mathcal{O}\big(n^{\varepsilon}\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}}\big) for the number of choices for all parameters.

Finally, to prove the upper bound of order n ε ​ ( n 8 / 5 m) n^{\varepsilon}\big(\frac{n^{\nicefrac{{8}}{{5}}}}{m}\big), from inequalities ( 22 - 25) we derive

(27) |  | ( z 23 z 234) ( z 234 x 23 x 24) ( z 34 x 12 x 123 x 124 x 1234) ( x 12 x 13 x 14 x 23 x 123 x 124 x 134 x 234 x 1234) 2 × ( x 12 2 x 123 2 x 124 x 1234 2) = z 23 ​ x 23 x 13 ​ x 34 ​ x 134 z 34 ​ x 34 x 14 ​ x 24 ​ x 124 ( z 234 ​ x 23 ​ x 24 ​ x 234 x 13 ​ x 14 ​ x 134) 2 × ( x 12 ​ x 13 ​ x 14 ​ x 123 ​ x 124 ​ x 134 ​ x 1234) 5 ≪ n 9 m 5 ​ n 1 5 ​ n 2 3 ​ n 3 ​ d 23 ​ d 34 ​ d 234 2 ≪ n 8 m 5. \begin{split}&(z_{23}z_{234})(z_{234}x_{23}x_{24})(z_{34}x_{12}x_{123}x_{124}x_{1234})(x_{12}x_{13}x_{14}x_{23}x_{123}x_{124}x_{134}x_{234}x_{1234})^{2}\times\\ &(x_{12}^{2}x_{123}^{2}x_{124}x_{1234}^{2})=\frac{z_{23}x_{23}}{x_{13}x_{34}x_{134}}\frac{z_{34}x_{34}}{x_{14}x_{24}x_{124}}\left(\frac{z_{234}x_{23}x_{24}x_{234}}{x_{13}x_{14}x_{134}}\right)^{2}\times\\ &(x_{12}x_{13}x_{14}x_{123}x_{124}x_{134}x_{1234})^{5}\ll\frac{n^{9}}{m^{5}n_{1}^{5}n_{2}^{3}n_{3}d_{23}d_{34}d_{234}^{2}}\ll\frac{n^{8}}{m^{5}}.\end{split} |  |

For the last inequality we note that by definition we have d 23 = ∏ p ∈ ℙ p ν p ​ ( n) − max ⁡ { ν p ​ ( n 2), ν p ​ ( n 3) } d_{23}=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n)-\max\{\nu_{p}(n_{2}),\nu_{p}(n_{3})\}}, where ν p \nu_{p} denotes the p p -adic valuation. Hence,

 | n 2 ​ n 3 ​ d 23 = ∏ p ∈ ℙ p ν p ​ ( n 2) + ν p ​ ( n 3) + ν p ​ ( n) − max ⁡ { ν p ​ ( n 2), ν p ​ ( n 3) } ≥ ∏ p ∈ ℙ p ν p ​ ( n) = n. n_{2}n_{3}d_{23}=\prod_{p\in\mathbb{P}}p^{\nu_{p}(n_{2})+\nu_{p}(n_{3})+\nu_{p}(n)-\max\{\nu_{p}(n_{2}),\nu_{p}(n_{3})\}}\geq\prod_{p\in\mathbb{P}}p^{\nu_{p}(n)}=n. |  |

By Lemma 1 any of the factors in parentheses on the very left hand side of ( 27), with exception of the factor ( x 12 2 ​ x 123 2 ​ x 124 ​ x 1234 2) (x_{12}^{2}x_{123}^{2}x_{124}x_{1234}^{2}), is a product of parameters forming a defining set. Hence, if we fix any of these factors, by Lemma A we have at most 𝒪 ε ​ ( n ε) \mathcal{O}_{\varepsilon}(n^{\varepsilon}) choices for the corresponding defining set, and thus also at most 𝒪 ε ​ ( n ε) \mathcal{O}_{\varepsilon}(n^{\varepsilon}) choices for all relative greatest common divisors. After distributing the variables of the exceptional factor among the other ones, we conclude that at least one of the remaining factors is bounded from above by 𝒪 ⁡ ( n 8 / 5 m) \mathcal{O}\big(\frac{n^{\nicefrac{{8}}{{5}}}}{m}\big) which gives an upper bound of 𝒪 ε ​ ( n ε ​ n 8 / 5 m) \mathcal{O}_{\varepsilon}\big(n^{\varepsilon}\frac{n^{\nicefrac{{8}}{{5}}}}{m}\big) for the number of solutions of ( 10) altogether.

It may seem a bit mysterious how the equations ( 26) and ( 27) were found. In Section 6, we describe how we used a computer programme to list many suitable inequalities of this type based on a precomputed list of defining sets. From a list of given inequalities we have chosen the best ones we found.

## 5. Upper bounds on sums of k ≥ 5 k\geq 5 unit fractions

In this section, we prove Theorem 2. We do so by applying a lifting method by Browning and Elsholtz [2] to the result in Theorem 1.

We first derive the bound on f 5 ​ ( m, n) f_{5}(m,n) by summing our upper bound from Theorem 1 over several choices of the smallest denominator a 1 a_{1} in the decomposition. Here, we will only consider the bound f 4 ( m, n) ≪ ε n ε n 8 / 5 m f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\frac{n^{\nicefrac{{8}}{{5}}}}{m}. The reason for this is, that summing over the bound f 4 ( m, n) ≪ ε n ε n 3 / 2 m 3 / 4 f_{4}(m,n)\ll_{\varepsilon}n^{\varepsilon}\frac{n^{\nicefrac{{3}}{{2}}}}{m^{\nicefrac{{3}}{{4}}}} leads to worse upper bounds for f 5 ​ ( m, n) f_{5}(m,n) because the exponent of m m is too small.

In particular, for given a 1 ∈ ℕ a_{1}\in\mathbb{N}, we consider decompositions of m n − 1 a 1 = m ​ a 1 − n n ​ a 1 \frac{m}{n}-\frac{1}{a_{1}}=\frac{ma_{1}-n}{na_{1}} as a sum of four unit fractions. We set m ​ a 1 − n = u ma_{1}-n=u, and with the trivial bounds

 | n m < a 1 ≤ 5 ​ n m, \frac{n}{m}<a_{1}\leq\frac{5n}{m}, |  |

we have

 | f 5 ​ ( m, n) \displaystyle f_{5}(m,n) | ≤ ∑ 0 < u ≤ 4 ​ n f 4 ( u, n u + n m) ≪ ε n ε ∑ 0 < u ≤ 4 ​ n ( n ​ u + n m) 8 / 5 u \displaystyle\leq\sum_{0<u\leq 4n}f_{4}\bigg(u,n\frac{u+n}{m}\bigg)\ll_{\varepsilon}n^{\varepsilon}\sum_{0<u\leq 4n}\frac{\big(n\frac{u+n}{m}\big)^{\nicefrac{{8}}{{5}}}}{u} |  |

 |  | ≪ ε n ε ( n 2 m) 8 / 5 ∑ 0 < u ≤ 4 ​ n 1 u ≪ ε n ε ( n 2 m) 8 / 5. \displaystyle\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n^{2}}{m}\bigg)^{\nicefrac{{8}}{{5}}}\sum_{0<u\leq 4n}\frac{1}{u}\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n^{2}}{m}\bigg)^{\nicefrac{{8}}{{5}}}. |  |

We next use [4] *Lemma C which summarizes the procedure used in [2] *Section 4 to lift this upper bound on f 5 ​ ( m, n) f_{5}(m,n) to f k ​ ( m, n) f_{k}(m,n) for k > 5 k>5. We give this result here as the following Lemma B.

###### Lemma B.

Suppose that there exists c > 1 c>1 such that

 | f 5 ( m, n) ≪ ε n ε ( n 2 m) c. f_{5}(m,n)\ll_{\varepsilon}n^{\varepsilon}\bigg(\frac{n^{2}}{m}\bigg)^{c}. |  |

Then for any k ≥ 5 k\geq 5 we have

 | f k ( m, n) ≪ ε ( k n) ε ( k 4 / 3 ​ n 2 m) c ​ 2 k − 5. f_{k}(m,n)\ll_{\varepsilon}(kn)^{\varepsilon}\bigg(\frac{k^{\nicefrac{{4}}{{3}}}n^{2}}{m}\bigg)^{c2^{k-5}}. |  |

Lemma B together with our bound on f 5 ​ ( m, n) f_{5}(m,n) above proves Theorem 2.

## 6. Computational aspects

Here, we describe how we found the proof of Theorem 1. To find inequalities of the type ( 26) and ( 27) we used a computer algebra system. As stated earlier there are two stages at which computational aspects came into play, the first of which was finding many defining sets. Here we used 96 96 equations of type ( 15 - 21). For subsets S i S_{i}, 0 ≤ i ≤ l 0\leq i\leq l of the set { x J: J ⊂ { 1, 2, 3, 4 }, | J | ≥ 2 } ∪ { z J: J ⊂ { 1, 2, 3, 4 }, 2 ≤ | J | ≤ 3 } \{x_{J}:J\subset\{1,2,3,4\},|J|\geq 2\}\cup\{z_{J}:J\subset\{1,2,3,4\},2\leq|J|\leq 3\} any of these equations is of the form

(28) |  | c 0 ​ ∏ p J ∈ S 0 p J = ∑ i = 1 l c i ​ ∏ p J ∈ S i p J, c_{0}\prod_{p_{J}\in S_{0}}p_{J}=\sum_{i=1}^{l}c_{i}\prod_{p_{J}\in S_{i}}p_{J}, |  |

where the c i c_{i}, 0 ≤ i ≤ l 0\leq i\leq l, are constants depending at most on m m and the pattern ( n 1, …, n 4) (n_{1},\ldots,n_{4}). In particular, Lemma A tells us, that once we fix the parameters in the sets S 1, …, S l S_{1},\ldots,S_{l}, we have at most of order n ε n^{\varepsilon} choices for the parameters in the set S 0 S_{0}.

For a given subset S S of parameters we can now go through our 96 96 equations and check whether for one of these

(29) |  | ⋃ i = 1 l S i ⊂ S. \bigcup_{i=1}^{l}S_{i}\subset S. |  |

If this is the case we add the parameters in S 0 \ S S_{0}\backslash S to S S and repeat the process.

If at some point equation ( 29) does not yield any new parameters for any of the 96 96 equations we stop the process. If the set of parameters we obtained in this fashion is the set of all parameters then the original set S S was a defining set.

It remains to discuss which equations of the form ( 28) our program used to find defining sets. We set I = { 1, …, 4 } I=\{1,\ldots,4\} and we consider the following 8 8 types of equations.

1. (1)

The first type of equation arises from considering two of the relative greatest common divisors unknown. In this case equation ( 11) may be rearranged such that it factors in one of the following forms:

 | ( C 1 ​ x J − C 3) ​ ( C 1 ​ x K − C 2) \displaystyle(C_{1}x_{J}-C_{3})(C_{1}x_{K}-C_{2}) | = C 1 ​ C 4 + C 2 ​ C 3 \displaystyle=C_{1}C_{4}+C_{2}C_{3} |  |

 | x J ​ ( C 5 + C 6 ​ x K) \displaystyle x_{J}(C_{5}+C_{6}x_{K}) | = C 7, \displaystyle=C_{7}, |  |

where J, K ⊂ I J,K\subset I. This leads to 55 55 equations.

2. (2)

Next, for 1 ≤ i < j ≤ 4 1\leq i<j\leq 4 and { k, l } = I \ { i, j } \{k,l\}=I\backslash\{i,j\}, we define the integer parameters z i ​ j z_{ij} in ( 12) in a general way:

 | z i ​ j = n n i ​ d i ​ j ​ ∏ i ∉ J, j ∈ J x J + n n j ​ d i ​ j ​ ∏ i ∈ J, j ∉ J x J x i ​ j ​ x k ​ l. z_{ij}=\frac{\frac{n}{n_{i}d_{ij}}\prod_{i\not\in J,j\in J}x_{J}+\frac{n}{n_{j}d_{ij}}\prod_{i\in J,j\not\in J}x_{J}}{x_{ij}x_{kl}}. |  |

From this equation we see that fixing the parameters in the set

 | { x J: J ⊂ { 1, 2, 3, 4 }, ( i ∈ J ∧ j ∉ J) ∨ ( i ∉ J ∧ j ∈ J), J ≠ { k, l } } \big\{x_{J}:J\subset\{1,2,3,4\},(i\in J\wedge j\not\in J)\vee(i\not\in J\wedge j\in J),J\neq\{k,l\}\big\} |  |

leads to at most of order n ε n^{\varepsilon} choices for z i ​ j z_{ij} and x i ​ j x_{ij} and, after multiplying with the denominator on the right hand side, to 6 6 equations of type ( 28).

3. (3)

In addition to the equations corresponding to the parameters z 123 z_{123}, z 134 z_{134} and z 234 z_{234} in ( 13), we used

 | z 124 = n n 1 ​ d 124 ​ x 23 ​ x 24 ​ x 34 ​ x 234 + n n 2 ​ d 124 ​ x 13 ​ x 14 ​ x 34 ​ x 134 + n n 4 ​ d 124 ​ x 12 ​ x 13 ​ x 23 ​ x 123 x 12 ​ x 14 ​ x 24 ​ x 124. z_{124}=\frac{\frac{n}{n_{1}d_{124}}x_{23}x_{24}x_{34}x_{234}+\frac{n}{n_{2}d_{124}}x_{13}x_{14}x_{34}x_{134}+\frac{n}{n_{4}d_{124}}x_{12}x_{13}x_{23}x_{123}}{x_{12}x_{14}x_{24}x_{124}}. |  |

To get an equation of the form ( 28) we multiply with the denominator on the right hand side.

4. (4)

Using the definition of z i ​ j ​ k z_{ijk}, z i ​ j z_{ij}, z i ​ k z_{ik} and z j ​ k z_{jk} and setting l l to be the single element in I \ { i, j, k } I\backslash\{i,j,k\}, we have

 | z i ​ j ​ k ​ x i ​ j ​ x i ​ k ​ x j ​ k ​ x i ​ j ​ k \displaystyle z_{ijk}x_{ij}x_{ik}x_{jk}x_{ijk} | = d i ​ j d i ​ j ​ k ​ z i ​ j ​ x k ​ l + n n k ​ d i ​ j ​ k ​ x i ​ j ​ x i ​ l ​ x j ​ l ​ x i ​ j ​ l \displaystyle=\frac{d_{ij}}{d_{ijk}}z_{ij}x_{kl}+\frac{n}{n_{k}d_{ijk}}x_{ij}x_{il}x_{jl}x_{ijl} |  |

 |  | = d i ​ k d i ​ j ​ k ​ z i ​ k ​ x j ​ l + n n j ​ d i ​ j ​ k ​ x i ​ k ​ x i ​ l ​ x k ​ l ​ x i ​ k ​ l \displaystyle=\frac{d_{ik}}{d_{ijk}}z_{ik}x_{jl}+\frac{n}{n_{j}d_{ijk}}x_{ik}x_{il}x_{kl}x_{ikl} |  |

 |  | = d j ​ k d i ​ j ​ k ​ z j ​ k ​ x i ​ l + n n i ​ d i ​ j ​ k ​ x j ​ k ​ x j ​ l ​ x k ​ l ​ x j ​ k ​ l. \displaystyle=\frac{d_{jk}}{d_{ijk}}z_{jk}x_{il}+\frac{n}{n_{i}d_{ijk}}x_{jk}x_{jl}x_{kl}x_{jkl}. |  |

This leads to twelve equations of type ( 28).

5. (5)

By definition of the parameters z i ​ j ​ k z_{ijk} we may write down the general form of equations ( 15) and ( 16):

 | m ​ ∏ J ⊂ I l ∈ J x J = d i ​ j ​ k ​ z i ​ j ​ k + n n l, m\prod_{\begin{subarray}{c}J\subset I\\ l\in J\end{subarray}}x_{J}=d_{ijk}z_{ijk}+\frac{n}{n_{l}}, |  |

where l l is the single element in the set I \ { i, j, k } I\backslash\{i,j,k\}. This leads to 4 4 equations and we get that fixing the parameter z i ​ j ​ k z_{ijk} leads to at most of order n ε n^{\varepsilon} choices for the parameters in the set

 | { x J: J ⊂ I, l ∈ J }. \big\{x_{J}:J\subset I,l\in J\big\}. |  |

6. (6)

Using just the definition of the z i ​ j z_{ij}, we derive 6 6 equations of the following form:

 | m ​ ∏ J ⊂ I J ≠ { i, j } x J = d i ​ j ​ x k ​ l ​ z i ​ j + n n k ​ ∏ J ⊂ I k ∉ J J ≠ { i, j } x J + n n l ​ ∏ J ⊂ I l ∉ J J ≠ { i, j } x J, m\prod_{\begin{subarray}{c}J\subset I\\ J\neq\{i,j\}\end{subarray}}x_{J}=d_{ij}x_{kl}z_{ij}+\frac{n}{n_{k}}\prod_{\begin{subarray}{c}J\subset I\\ k\not\in J\\ J\neq\{i,j\}\end{subarray}}x_{J}+\frac{n}{n_{l}}\prod_{\begin{subarray}{c}J\subset I\\ l\not\in J\\ J\neq\{i,j\}\end{subarray}}x_{J}, |  |

where { k, l } = I \ { i, j } \{k,l\}=I\backslash\{i,j\}. Hence, once we fix the parameters z i ​ j z_{ij}, x k ​ l x_{kl} and those in the set

 | { x J: J ⊂ I, k ∉ J, J ≠ { i, j } } ∪ { x J: J ⊂ I, l ∉ J, J ≠ { i, j } }, \big\{x_{J}:J\subset I,k\not\in J,J\neq\{i,j\}\big\}\cup\big\{x_{J}:J\subset I,l\not\in J,J\neq\{i,j\}\big\}, |  |

we have at most of order n ε n^{\varepsilon} choices for all the remaining relative greatest common divisors with the exception of x i ​ j x_{ij}.

7. (7)

Let { i, j } \{i,j\} and { k, l } \{k,l\} be a partition of I I. Again, just using the definition of z i ​ j z_{ij} and z k ​ l z_{kl}, we derive from ( 11):

 | m ​ ∏ J ⊂ I J ∉ { { i, j }, { k, l } } x J = d i ​ j ​ z i ​ j + d k ​ l ​ z k ​ l. m\prod_{\begin{subarray}{c}J\subset I\\ J\not\in\{\{i,j\},\{k,l\}\}\end{subarray}}x_{J}=d_{ij}z_{ij}+d_{kl}z_{kl}. |  |

Thus, once we fix the parameter z i ​ j z_{ij} and z k ​ l z_{kl} we have at most of order n ε n^{\varepsilon} choices for all relative greatest common divisors except x i ​ j x_{ij} and x k ​ l x_{kl}. We have 3 3 equations of this type.

8. (8)

Finally let J 1, J 2 ⊂ I J_{1},J_{2}\subset I with J 1 ≠ J 2 J_{1}\neq J_{2}, | J 1 | = | J 2 | = 3 |J_{1}|=|J_{2}|=3 and J 1 ∩ J 2 = { i, j } J_{1}\cap J_{2}=\{i,j\}, { k, l } = I \ { i, j } \{k,l\}=I\backslash\{i,j\}. Then by multiplying z J 1 z_{J_{1}} and z J 2 z_{J_{2}} we get 6 6 equations of the form

 | z J 1 ​ z J 2 = n 2 n k ​ n l ​ d J 1 ​ d J 2 + n 2 ​ d { i, j } d J 1 ​ d J 2 ​ z { i, j } ​ x { k, l } 2 ​ x { i, k, l } ​ x { j, k, l } ​ x 1234. z_{J_{1}}z_{J_{2}}=\frac{n^{2}}{n_{k}n_{l}d_{J_{1}}d_{J_{2}}}+\frac{n^{2}d_{\{i,j\}}}{d_{J_{1}}d_{J_{2}}}z_{\{i,j\}}x_{\{k,l\}}^{2}x_{\{i,k,l\}}x_{\{j,k,l\}}x_{1234}. |  |

Thus, if we fix z { i, j } z_{\{i,j\}}, x { k, l } x_{\{k,l\}}, x { i, k, l } x_{\{i,k,l\}}, x { j, k, l } x_{\{j,k,l\}} and x 1234 x_{1234}, we have at most of order n ε n^{\varepsilon} choices for the parameters z J 1 z_{J_{1}} and z J 2 z_{J_{2}}.

Next we need to multiplicatively combine inequalities of type ( 22 - 24) in such a way, that the exponent of n n on the (larger) right hand side is small and the set of relative greatest common divisors making up for the (smaller) left hand side may be split into many defining sets. In addition to inequalities ( 22 - 24) in our computer search we took into account the following seven inequalities:

 | z 12 ​ x 12 \displaystyle z_{12}x_{12} | ≤ 2 ​ n n 1 ​ d 12 x 23 x 24 x 234 z 123 x 12 x 13 x 123, \displaystyle\leq\frac{2n}{n_{1}d_{12}}x_{23}x_{24}x_{234}\qquad z_{123}x_{12}x_{13}x_{123}, |  | ≤ 3 ​ n n 1 ​ d 123 ​ x 24 ​ x 34 ​ x 234, \displaystyle\leq\frac{3n}{n_{1}d_{123}}x_{24}x_{34}x_{234}, |  |

 | z 13 ​ x 13 \displaystyle z_{13}x_{13} | ≤ 2 ​ n n 1 ​ d 13 x 23 x 34 x 234 z 124 x 12 x 14 x 124, \displaystyle\leq\frac{2n}{n_{1}d_{13}}x_{23}x_{34}x_{234}\qquad z_{124}x_{12}x_{14}x_{124}, |  | ≤ 3 ​ n n 1 ​ d 124 ​ x 23 ​ x 34 ​ x 234, \displaystyle\leq\frac{3n}{n_{1}d_{124}}x_{23}x_{34}x_{234}, |  |

 | z 14 ​ x 14 \displaystyle z_{14}x_{14} | ≤ 2 ​ n n 1 ​ d 14 x 23 x 34 x 234 z 134 x 13 x 14 x 134, \displaystyle\leq\frac{2n}{n_{1}d_{14}}x_{23}x_{34}x_{234}\qquad z_{134}x_{13}x_{14}x_{134}, |  | ≤ 3 ​ n n 1 ​ d 134 ​ x 23 ​ x 24 ​ x 234, \displaystyle\leq\frac{3n}{n_{1}d_{134}}x_{23}x_{24}x_{234}, |  |

 | z 24 ​ x 24 \displaystyle z_{24}x_{24} | ≤ 2 ​ n n 2 ​ d 24 ​ x 14 ​ x 34 ​ x 134. \displaystyle\leq\frac{2n}{n_{2}d_{24}}x_{14}x_{34}x_{134}. |  |

After multiplying any number of such inequalities up, we divide by the product of all relative greatest common divisors on the right hand side. To clear the resulting denominator on the new left hand side we use inequality ( 25) together with the inequalities t 2 ≤ 12 ​ n 2 n 2 ​ m t_{2}\leq\frac{12n^{2}}{n_{2}m} and t 3 ≤ 96 ​ n 4 n 3 ​ m 2 t_{3}\leq\frac{96n^{4}}{n_{3}m^{2}}, which we derived in the proof of Lemma 1. Note that apart from clearing denominators we can add any number of these three inequalities to our previously selected ones.

Furthermore, we took into account that n i ​ n j ​ d i ​ j ≥ n n_{i}n_{j}d_{ij}\geq n and n i ​ n j ​ n k ​ d i ​ j ​ k ≥ n n_{i}n_{j}n_{k}d_{ijk}\geq n for all 1 ≤ i, j, k ≤ 4 1\leq i,j,k\leq 4. This may lead to a further reduction in size in terms of n n on the right hand side of inequalities constructed as above. However, we cannot prove that our computer search covered all possible defining sets and all relevant combinations of inequalities. Hence, it may well be that the exponent in Theorem 1 can be improved by conducting a more complete search.

*Acknowledgements.*The authors would like to thank the referee for comments on the manuscript and acknowledge the support of the Austrian Science Fund (FWF): W1230, I 4945-N and I 4406-N.

## References

- [1] A.V. Aho and N. Sloane (1973) Some doubly exponential sequences,. Fibonacci Quart 11, pp. 429–437. Cited by: Remark 3.
- [2] T. D. Browning and C. Elsholtz (2011) The number of representations of rationals as a sum of unit fractions. Illinois J. Math. 55 ( 2), pp. 685–696. Cited by: §1, §1, §1, §1, §2, item 3, §5, §5.
- [3] E.S. Croot (2003) On a coloring conjecture about unit fractions. Annals of Mathematics 157, pp. 545–556. Cited by: §1.
- [4] C. Elsholtz and S. Planitzer (2020) The number of solutions of the erd \h os-straus equation and sums of k k unit fractions. Proc. Roy. Soc. Edinburgh Sect. A 150 ( 3), pp. 1401–1427. Cited by: §1, §1, §2, §2, §2, §3, §4, §5, Remark 1, Remark 2, Remark 2.
- [5] C. Elsholtz and T. Tao (2013) Counting the number of solutions to the Erdős-Straus equation on unit fractions. J. Aust. Math. Soc. 94 ( 1), pp. 50–105. Cited by: §1, §1, §2, §2, §3, §4.
- [6] C. Elsholtz (2001) Sums of k k unit fractions. Trans. Amer. Math. Soc. 353 ( 8), pp. 3209–3227. Cited by: §2.
- [7] P. Erdős (1950) Az 1 x 1 + 1 x 2 + ⋯ + 1 x n = a b \frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}=\frac{a}{b} egyenlet egész számú megoldásairól (On a Diophantine equation, in Hungarian). Mat. Lapok 1, pp. 192–210. Cited by: §1.
- [8] R. L. Graham (1964) On finite sums of unit fractions. Proc. London Math. Soc. (3) 14, pp. 193–207. Cited by: §1.
- [9] R.L. Graham, D.E. Knuth, and O. Patashnik (1994) Concrete mathematics. Addison-Wesley, Reading, MA. Cited by: Remark 3.
- [10] G. H. Hardy and E. M. Wright (2008) An introduction to the theory of numbers. sixth edition edition, Oxford University Press, Oxford. Cited by: §2.
- [11] S. V. Konyagin (2014) Double exponential lower bound for the number of r epresentations of unity by Egyptian fractions. Math. Notes 95 ( 1-2), pp. 277–281. Note: Translation of Mat. Zametki 95 (2014), no . 2, 312–316 Cited by: §1.
- [12] G. Martin (1999) Dense egyptian fractions. Trans. Amer. Math. Soc. 351 ( 9), pp. 3641–3657. Cited by: §1.
- [13] S. Wagner and V. Ziegler () Irrationality of growth constants associated with polynomial recursions. arxiv 2004.09353, pp. . Cited by: Remark 3.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:elsholtz@math.tugraz.at
[4]: mailto:stefan.planitzer@gmail.com
