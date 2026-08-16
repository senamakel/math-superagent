<!-- source: https://arxiv.org/html/1508.05718 | converted from HTML -->

The Union-Closed Sets Conjecture for Small Families

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1508.05718v2 [math.CO] 25 Aug 2015

# The Union-Closed Sets Conjecture for Small Families

Jens Maßberg Note: Institut für Optimierung und Operations Research, University of Ulm, jens.massberg@uni-ulm.de

###### Abstract

We prove that the union-closed sets conjecture is true for separating union-closed families 𝒜 \mathcal{A} with | 𝒜 | ≤ 2 ​ ( m + m log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m)) |\mathcal{A}|\leq 2\left(m+\frac{m}{\log_{2}(m)-\log_{2}\log_{2}(m)}\right) where m m denotes the number of elements in 𝒜 \mathcal{A}.

Keywords: union-closed sets, Frankl’s conjecture

## 1 Introduction

A family 𝒜 \mathcal{A} of sets is said to be *union-closed*if for any two member sets A, B ∈ 𝒜 A,B\in\mathcal{A} their union A ∪ B A\cup B is also a member of 𝒜 \mathcal{A}.

A well-known conjecture is the *Union-Closed Sets Conjecture*which is also called *Frankl’s conjecture*:

###### Conjecture 1.1.

Any finite non-empty union-closed family of sets has an element that is contained in at least half of its member sets.

There are many papers considering this conjecture. So it is known to be true if 𝒜 \mathcal{A} has at most 12 elements [8] or at most 50 member sets [4, 7] or if the number of member sets is large compared to the number m m of elements, that is | 𝒜 | ≥ 2 3 ​ 2 m |\mathcal{A}|\geq\frac{2}{3}2^{m} [1]. Nevertheless, the conjecture is still far from being proved or disproved. A good survey on the current state of this conjecture is given by Bruhn and Schaudt [2].

In this paper we consider the case that the number of member-sets is small compared to the number of elements. But first we recall some basic definitions and results. Let 𝒜 \mathcal{A} be a union-closed set. We call U ⁡ ( 𝒜) = ⋃ A ∈ 𝒜 A U(\mathcal{A})=\bigcup_{A\in\mathcal{A}}A the *universe*of 𝒜 \mathcal{A}. For an element x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}) the cardinality of | { A ∈ 𝒜: x ∈ A } | |\{A\in\mathcal{A}:\,x\in A\}| is called the *frequency*of x x. Thus the union-closed sets conjecture states that there exists an element x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}) of frequency at least 1 2 ​ | 𝒜 | \frac{1}{2}|\mathcal{A}|.

A family 𝒜 \mathcal{A} is called *separating*if for any two distinct elements x, y ∈ U ⁡ ( 𝒜) x,y\in U(\mathcal{A}) there exists a set A ∈ 𝒜 A\in\mathcal{A} that contains exactly one of the elements x x and y y. We can restrict ourselves to separating union-closed families: If there exist elements x x and y y such that each member set A ∈ 𝒜 A\in\mathcal{A} that contains x x also contains y y, then we can delete x x from each such set and obtain a new family of the same cardinality that is still union-closed. Falgas-Ravry showed that there are some sets in 𝒜 \mathcal{A} satisfying certain conditions which help us to analyze small separating union-closed families:

###### Theorem 1.2 (Falgas-Ravry [3]).

Let 𝒜 \mathcal{A} be a separating union-closed family and let x 1, …, x m x_{1},\ldots,x_{m} be the elements of U ⁡ ( 𝒜) U(\mathcal{A}) labeled in order of increasing frequency. Then there exist sets X 0, …, X m ∈ 𝒜 X_{0},\ldots,X_{m}\in\mathcal{A} such that

 | x i ∉ X i ∀ i ∈ { 1, …, m } x_{i}\notin X_{i}\quad\forall i\in\{1,\ldots,m\} |  | (1) |

and

 | { x i + 1, …, x m } ⊂ X i ∀ i ∈ { 0, …, m } \{x_{i+1},\ldots,x_{m}\}\subset X_{i}\quad\forall i\in\{0,\ldots,m\} |  | (2) |

###### Proof.

As 𝒜 \mathcal{A} is separating, for any 1 ≤ i < j ≤ m 1\leq i<j\leq m there exists a set X i ​ j ∈ 𝒜 X_{ij}\in\mathcal{A} such that x i ∉ X i ​ j x_{i}\notin X_{ij} and x j ∈ X i ​ j x_{j}\in X_{ij}. For all 1 ≤ i ≤ m − 1 1\leq i\leq m-1 let X i = ⋃ j = i + 1 m X i ​ j X_{i}=\bigcup_{j=i+1}^{m}X_{ij} and set X 0 = U ⁡ ( 𝒜) X_{0}=U(\mathcal{A}). ∎

The previous theorem directly implies that the conjecture is satisfied for small families:

###### Lemma 1.3.

Any separating family on m m elements with at most 2 ​ m 2m member sets satisfies the Union-Closed Sets Conjecture.

###### Proof.

Consider the sets X 0, …, X m − 1 X_{0},\ldots,X_{m-1} constructed in Theorem 1.2 and observe that the most frequent element x m x_{m} is contained in all these sets. As these sets are pairwise different, x m x_{m} is contained in at least m m of all member sets of 𝒜 \mathcal{A}. ∎

In this paper we show that the Union-Closed Sets Conjecture is also satisfied for families that contain (slightly) more then 2 ​ m 2m member sets. Considering such families is motivated by a result of Hu (see also [2]):

###### Theorem 1.4 (Hu [5]).

Suppose there is a c > 2 c>2 so that any separating union-closed family 𝒜 ′ \mathcal{A}^{\prime} with | 𝒜 ′ | ≤ c ​ | U ⁡ ( 𝒜 ′) | |\mathcal{A}^{\prime}|\leq c|U(\mathcal{A}^{\prime})| satisfies the Union-Closed Sets Conjecture. Then, for every union-closed family 𝒜 \mathcal{A}, there is an element x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}) of frequency

 | | { A ∈ 𝒜: x ∈ A } | ≥ c − 2 2 ​ ( c − 1) ​ | 𝒜 |. |\{A\in\mathcal{A}:\,x\in A\}|\geq\frac{c-2}{2(c-1)}|\mathcal{A}|. |  | (3) |

Therefore, if the Union-Closed Sets Conjecture is satisfied for ’small’ families, then for any union-closed family there exists an element that appears with a frequency at least a constant fraction of the number of member sets. In this paper we push the bound over 2 ​ m 2m, but for increasing m m it still converges slowly towards 2 ​ m 2m.

## 2 Frankl’s Conjecture for Small Families

Combining and extending the idea of the proof of Theorem 1.2 and an argument of Knill [6] we get the main result of this paper.

###### Theorem 2.1.

The Union-Closed Sets Conjecture is true for separating union-closed families 𝒜 \mathcal{A} with a universe containing m m elements satisfying

 | | 𝒜 | ≤ 2 ​ ( m + m log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m)). |\mathcal{A}|\leq 2\left(m+\frac{m}{\log_{2}(m)-\log_{2}\log_{2}(m)}\right). |  |

###### Proof.

Let 𝒜 \mathcal{A} be a separating union-closed family, let the elements x 1, …, x m x_{1},\ldots,x_{m} of U ⁡ ( 𝒜) U(\mathcal{A}) be labeled in order of increasing frequency and set n = | 𝒜 | n=|\mathcal{A}|. Assume that each element appears in at most m + c m+c member sets. We compute an upper bound on the size of n n.

For i ∈ { 1, …, m } i\in\{1,\ldots,m\} we set

 | M i = ⋃ A ∈ 𝒜: x i ∉ A A M_{i}=\bigcup_{A\in\mathcal{A}:x_{i}\notin A}A |  | (4) |

to be the union of all sets containing x i x_{i} and we set M 0 = U M_{0}=U. If the sets X i X_{i}, i ∈ { 0, …, m } i\in\{0,\ldots,m\}, are chosen as in Theorem 1.2, then we have X i ⊂ M i X_{i}\subset M_{i} for all i ∈ { 0, …, m − 1 } i\in\{0,\ldots,m-1\} and thus

 | { x i + 1, …, x m } ⊆ M i. \{x_{i+1},\ldots,x_{m}\}\subseteq M_{i}. |  | (5) |

Let U ~ = { x i: ∃ A ∈ 𝒜 ​ with ​ max x j ∈ A ​ j } \tilde{U}=\{x_{i}:\,\exists A\in\mathcal{A}\text{ with }\max_{x_{j}\in A}j\} be the set of all x i x_{i} which are the elements with the highest index in some set A A.

For x i ∈ U ~ x_{i}\in\tilde{U} we set

 | A i = ⋃ A ∈ 𝒜: i = max ⁡ { j: x j ∈ A } A. A_{i}=\bigcup_{A\in\mathcal{A}:\,i=\max\{j:\,x_{j}\in A\}}A. |  | (6) |

By definition x i ∈ A i x_{i}\in A_{i}. Now consider j > i j>i. As x j ∉ A i x_{j}\notin A_{i} we have A i ⊂ M j A_{i}\subset M_{j}. Together with ( 5) we have

 | x i ∈ M j ∀ x i ∈ U ~, j ∈ { 0, …, m − 1 }, i ≠ j. x_{i}\in M_{j}\quad\forall x_{i}\in\tilde{U},j\in\{0,\ldots,m-1\},i\neq j. |  | (7) |

Observe that every non-empty member set of 𝒜 \mathcal{A} touches U ~ \tilde{U}. Following an argument of Knill [6] let U ^ ⊆ U ~ \hat{U}\subseteq\tilde{U} be minimal such that every non-empty set of 𝒜 \mathcal{A} touches U ^ \hat{U}. Then for all x i ∈ U ^ x_{i}\in\hat{U} there exists a set A ∈ 𝒜 A\in\mathcal{A} with U ^ ∩ A = { x i } \hat{U}\cap A=\{x_{i}\}; if not, U ^ ∖ { x i } \hat{U}\setminus\{x_{i}\} still touches every member set of 𝒜 \mathcal{A} contradicting the minimality of U ^ \hat{U}. Therefore as 𝒜 \mathcal{A} is union-closed, for each B ⊆ U ^ B\subseteq\hat{U} there exists a set P B ∈ 𝒜 P_{B}\in\mathcal{A} with P B ∩ U ^ = B P_{B}\cap\hat{U}=B. Let 𝒫 = { P B: B ⊆ U ^ } \mathcal{P}=\{P_{B}:\,B\subseteq\hat{U}\}. The sets in 𝒫 \mathcal{P} are pairwise disjoint and each element x i ∈ U ^ x_{i}\in\hat{U} is contained in exactly half of the sets. Setting k = | U ^ | k=|\hat{U}|, we conclude that there are 2 k 2^{k} sets in 𝒫 \mathcal{P} containing in total k ​ 2 k − 1 k2^{k-1} elements from U ^ \hat{U}.

Note, that 𝒫 \mathcal{P} might contain the sets M i M_{i} for x i ∈ U ^ x_{i}\in\hat{U} and one additional set M j M_{j} with U ^ ⊂ M j \hat{U}\subset M_{j}. But then { M 0, …, M m − 1 } \{M_{0},\ldots,M_{m-1}\} contains m − k m-k sets that are not in 𝒫 \mathcal{P} and each of these sets contains all elements of U ^ \hat{U}.

Before we compute an upper bound for the number of elements in 𝒜 \mathcal{A} we summarize the previous observations:

- •

Each of the k k elements in U ^ \hat{U} appears in at most m + c m+c member sets,

- •

the 2 k 2^{k} sets in 𝒫 \mathcal{P} contain in total k ​ 2 k − 1 k2^{k-1} copies of elements of U ^ \hat{U},

- •

there are m − k m-k additional member sets, each containing all elements of U ^ \hat{U} and

- •

all remaining member sets contain at least one element of U ^ \hat{U}.

We conclude:

 | n \displaystyle n | ≤ \displaystyle\leq | k ⁡ ( m + c) + ( 2 k − k ​ 2 k − 1) + ( m − k) ​ ( 1 − k) \displaystyle k(m+c)+(2^{k}-k2^{k-1})+(m-k)(1-k) |  | (8) |

 |  | = \displaystyle= | m + k ​ c + ( 2 − k) ​ 2 k − 1 + k 2 − k. \displaystyle m+kc+(2-k)2^{k-1}+k^{2}-k. |  | (9) |

Suppose the Union-Closed Sets Conjecture is wrong, that is, n > 2 ​ ( m + c) n>2(m+c) or n 2 − m > c \frac{n}{2}-m>c. Then

 | n \displaystyle n | ≤ \displaystyle\leq | m + k ⁡ ( n 2 − m) + ( 2 − k) ​ 2 k − 1 + k 2 − k \displaystyle m+k(\frac{n}{2}-m)+(2-k)2^{k-1}+k^{2}-k |  | (10) |

or

 | n \displaystyle n | ≥ \displaystyle\geq | 2 ​ ( k − 1) ​ m + ( k − 2) ​ 2 k − 1 + k − k 2 k − 2 \displaystyle 2\frac{(k-1)m+(k-2)2^{k-1}+k-k^{2}}{k-2} |  | (11) |

 |  | ≥ \displaystyle\geq | 2 ​ ( m + 2 k − 1 + m k − 2 − k − 3). \displaystyle 2\left(m+2^{k-1}+\frac{m}{k-2}-k-3\right). |  | (12) |

We conclude that the conjecture is true for all n n satisfying

 | n ≤ 2 ​ ( m + min k ∈ ℕ ⁡ ( 2 k − 1 + m k − 2 − k − 3)). n\leq 2\left(m+\min_{k\in\mathbb{N}}\left(2^{k-1}+\frac{m}{k-2}-k-3\right)\right). |  | (13) |

The function f m ​ ( k):= 2 k − 1 + m k − 2 − k − 3 f_{m}(k):=2^{k-1}+\frac{m}{k-2}-k-3 is convex. Živković et al. [8] showed that the Union-Closed Sets Conjecture is satisfied for m ≤ 12 m\leq 12 so we can assume that m ≥ 13 m\geq 13. In this case the minimum of f m ​ ( k) f_{m}(k) is obtained in the interval [5, log 2 ⁡ ( m)] [5,\log_{2}(m)] and we get

 | f m ​ ( k) \displaystyle f_{m}(k) | = \displaystyle= | max ⁡ { 2 k − 1, m k − 2 } + ( min ⁡ { 2 k − 1, m k − 2 } − 3 − k) \displaystyle\max\left\{2^{k-1},\frac{m}{k-2}\right\}+\left(\min\left\{2^{k-1},\frac{m}{k-2}\right\}-3-k\right) |  | (14) |

 |  | ≥ \displaystyle\geq | max ⁡ { 2 k − 1, m k − 2 } \displaystyle\max\left\{2^{k-1},\frac{m}{k-2}\right\} |  | (15) |

 |  | ≥ \displaystyle\geq | min k ′ ⁡ ( max ⁡ { 2 k ′ − 1, m k ′ − 2 }) \displaystyle\min_{k^{\prime}}\left(\max\left\{2^{k^{\prime}-1},\frac{m}{k^{\prime}-2}\right\}\right) |  | (16) |

 |  | ≥ \displaystyle\geq | max k ′ ⁡ ( min ⁡ { 2 k ′ − 1, m k ′ − 2 }). \displaystyle\max_{k^{\prime}}\left(\min\left\{2^{k^{\prime}-1},\frac{m}{k^{\prime}-2}\right\}\right). |  | (17) |

The last inequality is due to the fact that 2 k − 1 2^{k-1} is increasing in k k while m k − 2 \frac{m}{k-2} is decreasing in k k.

Setting k ′ = log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m) + 2 k^{\prime}=\log_{2}(m)-\log_{2}\log_{2}(m)+2 we get

 | log 2 ⁡ ( m k ′ − 2) \displaystyle\log_{2}\left(\frac{m}{k^{\prime}-2}\right) | = \displaystyle= | log 2 ⁡ ( m) − log 2 ⁡ ( log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m)) \displaystyle\log_{2}(m)-\log_{2}\left(\log_{2}(m)-\log_{2}\log_{2}(m)\right) |  |

 |  | = \displaystyle= | log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m) − log 2 ⁡ ( 1 − log 2 ⁡ log 2 ⁡ ( m) log 2 ⁡ ( m)) \displaystyle\log_{2}(m)-\log_{2}\log_{2}(m)-\log_{2}\left(1-\frac{\log_{2}\log_{2}(m)}{\log_{2}(m)}\right) |  |

 |  | ≤ \displaystyle\leq | log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m) + 1 \displaystyle\log_{2}(m)-\log_{2}\log_{2}(m)+1 |  |

 |  | = \displaystyle= | log 2 ⁡ ( 2 k ′). \displaystyle\log_{2}(2^{k^{\prime}}). |  |

Inserting this result in ( 17) and ( 13) we finally obtain that the Union-Closed Sets Conjecture is true for all n n satisfying

 | n ≤ 2 ​ ( m + m log 2 ⁡ ( m) − log 2 ⁡ log 2 ⁡ ( m)). n\leq 2\left(m+\frac{m}{\log_{2}(m)-\log_{2}\log_{2}(m)}\right). |  | (18) |

∎

## 3 Acknowledgement

The author thanks Henning Bruhn-Fujimoto for pointing him to the union-closed sets conjecture.

## References

- [1] I. Balla, B. Bollobás, and T. Eccles. Union-closed families of sets. J. Combin. Theory (Series A), 120:531–544, 2013.
- [2] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture. Graphs and Combinatorics, 2015. DOI: 10.1007/s00373-014-1515-0.
- [3] V. Falgas-Ravry. Minimal weight in union-closed families. Electron. J. Comb., 19(P95), 2011.
- [4] G. Lo Faro. Union-closed sets conjecture: Improved bounds. J. Combin. Math. Combin. Comput., 16:97–102, 1994.
- [5] Y. Hu. Master’s thesis (in preperation).
- [6] E. Knill. Graph generated union-closed families of sets, 1994. arXiv:math/9409215v1 [math.CO].
- [7] I. Roberts and J. Simpson. A note on the union-closed sets conjecture. Australas. J. Combin., 47:265–267, 2010.
- [8] M. Živković and B. Vučković. The 12-element case of Frankls conjecture. (submitted, 2012).

*


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
