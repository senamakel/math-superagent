<!-- source: https://ar5iv.labs.arxiv.org/html/1508.05967 | converted from HTML -->

[1508.05967] Intersections of multiplicative translates of 3 -adic Cantor sets II: Two infinite families

# Intersections of multiplicative translates of
3 3 -adic Cantor sets II: Two infinite families Thanks: The first author received support from an NSF Graduate Research Fellowship. The third author received support from NSF grants DMS-1101373 and DMS-1401224.

William C. Abram , Artem Bolshakov and Jeffrey C. Lagarias Address: Department of Mathematics, Hillsdale College, Hillsdale, MI 49242-1205, USA Email address: [wabram@hillsdale.edu][1] Address: College of the School of Natural Sciences and Mathematics, University of Texas
at Dallas, Richardson, TX 75080-3021, USA Email address: [atb130030@utdallas.edu][2] Address: Department of Mathematics, University of Michigan, Ann Arbor, MI 48109-1043,USA Email address: [lagarias@umich.edu][3]

Date: December 5, 2015

###### Abstract.

This paper studies the structure of finite intersections of general multiplicative translates 𝒞 ⁡ ( M 1, M 2, …, M n) = 1 M 1 ​ Σ 3, 2 ¯ ∩ ⋯ ∩ 1 M n ​ Σ 3, 2 ¯ {{\mathcal{C}}}(M_{1},M_{2},\ldots,M_{n})=\frac{1}{M_{1}}\Sigma_{3,\bar{2}}\cap\cdots\cap\frac{1}{M_{n}}\Sigma_{3,\bar{2}} for integers 1 ≤ M 1 < M 2 < ⋯ < M n 1\leq M_{1}<M_{2}<\cdots<M_{n}, in which Σ 3, 2 ¯ \Sigma_{3,\bar{2}} denotes the 3 3 -adic Cantor set (of 3 3 -adic integers whose expansions omit the digit 2 2), which has Hausdorff dimension log 3 ⁡ 2 ≈ 0.630929 \log_{3}2\approx 0.630929. This study was motivated by questions concerning the discrete dynamical system on the 3 3 -adic integers ℤ 3 {\mathbb{Z}}_{3} given by multiplication by 2 2. The exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is defined to be the set of all elements of ℤ 3 \mathbb{Z}_{3} whose forward orbits under this action intersect the 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} infinitely many times. It is conjectured that it has Hausdorff dimension 0 0. An earlier paper showed that upper bounds on the Hausdorff dimension of the exceptional set can be extracted from knowing Hausdorff dimensions of sets of the kind above, in cases where all M i M_{i} are powers of 2 2. These intersection sets were shown to be fractals whose points have 3 3 -adic expansions describable by labeled paths in a finite automaton, whose Hausdorff dimension is exactly computable and is of the form log 3 ⁡ ( β) \log_{3}(\beta) where β \beta is a real algebraic integer. It gave algorithms for determination of the automaton, and computed examples showing that the dependence of the automaton and the value β \beta on the parameters ( M 1, …, M n) (M_{1},\ldots,M_{n}) is complicated. The present paper studies two new infinite families of examples, illustrating interesting behavior of the automata and of the Hausdorff dimension of the associated fractals. One family has associated automata whose directed graph has a nested sequence of strongly connected components of arbitrarily large depth. The second family leads to an improved upper bound for the Hausdorff dimension of the exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) of log 3 ⁡ ϕ ≈ 0.438018 \log_{3}\phi\approx 0.438018, where ϕ \phi denotes the Golden ratio.

## 1. Introduction

Let the 3 3 -adic Cantor set Σ 3:= Σ 3, 2 ¯ \Sigma_{3}:=\Sigma_{3,\bar{2}} be the subset of all 3 3 -adic integers whose 3 3 -adic expansions consist of digits 0 0 and 1 1 only. This set is a well-known fractal having Hausdorff dimension dim H ( Σ 3) = log 3 ⁡ 2 ≈ 0.630929 \dim_{H}(\Sigma_{3})=\log_{3}2\approx 0.630929. By a multiplicative translate of such a Cantor set we mean a multiplicatively rescaled set r ​ Σ 3 = { r ​ x: x ∈ Σ 3 } r\Sigma_{3}=\{rx:x\in\Sigma_{3}\}, where we restrict to r = p q ∈ ℚ × r=\frac{p}{q}\in{\mathbb{Q}}^{\times} being a rational number that is 3 3 -integral, meaning that r ∈ ℤ 3 r\in{\mathbb{Z}}_{3}, or equivalently o ​ r ​ d 3 ​ ( r) ≥ 0 ord_{3}(r)\geq 0. For example the multiplicative translate Σ 3, 1 ¯ = 2 ​ Σ 3, 2 ¯ \Sigma_{3,\bar{1}}=2\Sigma_{3,\bar{2}}, which allows only 3 3 -adic digits 0 0 and 2 2, has the symbol structure of its digits matching that of ternary expansions of the usual middle-third Cantor set on [0, 1] [0,1].

This paper considers sets given as finite intersections of such multiplicative translates:

 | 𝒞 ⁡ ( r 1, r 2, ⋯, r N):= ⋂ i = 1 N 1 r i ​ Σ 3. {\mathcal{C}}(r_{1},r_{2},\cdots,r_{N}):=\bigcap_{i=1}^{N}\frac{1}{r_{i}}\Sigma_{3}. |  | (1.1) |

These sets are fractals and this paper considers the problems of determining their internal structure and of obtaining bounds on their Hausdorff dimension. The dependence of the Hausdorff dimension of the sets 𝒞 ⁡ ( r 1, …, r n) {\mathcal{C}}(r_{1},\ldots,r_{n}) on the parameters ( r 1, r 2, …, r n) (r_{1},r_{2},\ldots,r_{n}) turns out to be complicated and fascinating.

In Part I [3], two of the authors presented a method for exactly computing the Hausdorff dimension of individual sets 𝒞 ⁡ ( r 1, …, r n) {\mathcal{C}}(r_{1},\ldots,r_{n}). This method is suited for computer experimentation. The method is based on the fact all such sets have a special property: the 3 3 -adic expansions of members of such a set are characterizable by the set of all infinite paths in a fixed labeled directed graph (finite automaton) that emanate from a fixed initial vertex, where the edge labels are 3 3 -adic digits. We term sets of this kind, characterized by a finite automaton, 3 3 -adic path set fractals. Two of the authors studied the p p -adic version of this concept in [2], and showed their Hausdorff dimensions are explicitly computable in terms of properties of the associated finite automaton. p p -adic path set fractals in turn are geometric realizations of objects in symbolic dynamics called path sets. Forgetting the geometric data associated to a p p -adic path set fractal Y Y, that is, thinking of the 3 3 -adic digits as an alphabet with no additional structure, recovers an underlying path set X X which is the set of all infinite strings of digits from { 0, 1, …, p − 1 } \{0,1,\ldots,p-1\} corresponding to elements of Y Y. The path set underlying the 3 3 -adic path set fractal 𝒞 ⁡ ( r 1, …, r n) {\mathcal{C}}(r_{1},\ldots,r_{n}) is denoted X ⁡ ( r 1, …, r n) X(r_{1},\ldots,r_{n}), and will play a role in the results of this paper. The papers [2], [3] gave between them algorithms to effectively compute X ⁡ ( r 1, …, r n) X(r_{1},\ldots,r_{n}) when given ( r 1, r 2, …, r n) (r_{1},r_{2},...,r_{n}). Section 3 reviews basic results on path sets and p p -adic path set fractals; a general theory of path sets was previously developed by two of the authors in [1].

This paper is concerned with the case 𝒞 ⁡ ( 1, M) {\mathcal{C}}(1,M) for M M a positive integer. The Hausdorff dimension dim H ( 𝒞 ⁡ ( 1, M)) \dim_{H}({\mathcal{C}}(1,M)) has a clear dependence on certain simple properties of the ternary expansion ( M) 3 (M)_{3} of M M. For example Part I observed:

1. (i)

dim H ( C ⁡ ( 1, M)) = 0 \dim_{H}(C(1,M))=0 whenever the last ternary digit of ( M) 3 (M)_{3} is a 2 2, i.e. M ≡ 2 ( mod 3) M\equiv 2\,(\bmod\,3).

2. (ii)

dim H ( C ⁡ ( 1, 3 ​ M)) = dim H ( 𝒞 ⁡ ( 1, M)). \dim_{H}(C(1,3M))=\dim_{H}({\mathcal{C}}(1,M)). In consequence, all trailing zeros in the base 3 3 expansion of M M may be cancelled off without changing the Hausdorff dimension.

However the dependence on M M seems anything but simple when examined more closely. It appears that arithmetic properties of M M influence both the structure of the underlying automata and the Hausdorff dimension in extremely complex ways. Part I treated in detail two infinite families of M M whose ternary expansion ( M) 3 (M)_{3} had a particularly simple form, where an exact answer for the Hausdorff dimension could be obtained.

1. (1)

M = L k = ( 1 k) 3, M=L_{k}=(1^{k})_{3}, that is L k = 1 2 ​ ( 3 k − 1) L_{k}=\frac{1}{2}(3^{k}-1). It obtained a Hausdorff dimension formula for each k ≥ 1 k\geq 1 and deduced that dim H ( C ⁡ ( 1, L k)) → 0 \dim_{H}(C(1,L_{k}))\to 0 as n → ∞ n\to\infty ( [3, Theorem 5.2]).

2. (2)

M = N k = ( 10 k − 1 ​ 1) 3 M=N_{k}=(10^{k-1}1)_{3}, that is N k = 3 k + 1 N_{k}=3^{k}+1. It showed for each k ≥ 1 k\geq 1 that dim H ( 𝒞 ⁡ ( 1, N k)) = log 3 ⁡ ϕ ≈ 0.438018, \dim_{H}({\mathcal{C}}(1,N_{k}))=\log_{3}\phi\approx 0.438018, where ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} ( [3, Theorem 5.5]).

The automata associated to the second of these families displayed considerable complexity. The automaton associated to N k N_{k} had a number of states growing exponentially with k k and was strongly connected; it is remarkable that its Perron eigenvalue could be computed exactly. Salient facts on these families are collected in Appendix A (Section 8) for easy reference.

This paper continues the study of the sets 𝒞 ⁡ ( 1, M) {{\mathcal{C}}}(1,M) for various integers M ≥ 1 M\geq 1. We obtain results for two new infinite families of M M having ternary expansions ( M) 3 (M)_{3} of a regular form, P k = 2 ⋅ 3 k + 1 = ( 20 k − 1 ​ 1) 3 P_{k}=2\cdot 3^{k}+1=(20^{k-1}1)_{3} and Q k = 3 2 ​ k − 3 k + 1 = ( 2 k ​ 0 k − 1 ​ 1) 3 Q_{k}=3^{2k}-3^{k}+1=(2^{k}0^{k-1}1)_{3}; they are stated in Section 2. When compared to the families treated in Part I, these families reveal additional complexity in the structure of the associated automata and the behavior of the Hausdorff dimension. In particular the automata associated to one of these families are not strongly connected; they are reducible and have arbitrarily large numbers of strongly connected components. We bound the Hausdorff dimension of such 𝒞 ⁡ ( 1, M) {\mathcal{C}}(1,M) through estimation of the Perron eigenvalue of the adjacency matrix of these automata. To estimate the Hausdorff dimension of one family, we make use of an operation on path sets termed interleaving, that we introduce in Section 3.4. The structure of the automata was first guessed from computer experiments and then proved. In addition to studying these two families the paper presents further results from computer experiments to test the relation of Hausdorff dimension to particular patterns in the ternary expansion of M M.

The original motivation for studying questions of this kind arose from a problem of Erdős [8]. This problem was generalized to a question over the 3 3 -adic integers by the third author ( [12]), who proposed a weaker version of the Erdős problem, the Exceptional set conjecture, explained below, which asserts that a certain set has Hausdorff dimension 0 0. The results of this paper yield new information about the Exceptional set conjecture without resolving it, see Section 1.2.

### 1.1. Exceptional set conjecture and nesting constants

Erdős [8] conjectured that for every n ≥ 9 n\geq 9, the ternary expansion of 2 n 2^{n} does not omit the digit 2 2. A weak version of this conjecture asserts that there are only finitely many n n such that the ternary expansion of 2 n 2^{n} does not omit the digit 2 2. Both versions of this conjecture are open and appear difficult.

In [12] the third author proposed a 3 3 -adic generalization of this problem, as follows. Let ℤ 3 \mathbb{Z}_{3} denote the 3 3 -adic integers, and let a 3 3 -adic integer α \alpha have 3 3 -adic expansion

 | ( α) 3:= a 0 + a 1 ⋅ 3 + a 2 ⋅ 3 2 + ⋯, with all ​ a i ∈ { 0, 1, 2 }. (\alpha)_{3}:=a_{0}+a_{1}\cdot 3+a_{2}\cdot 3^{2}+\cdots,~~\mbox{with all}~~a_{i}\in\{0,1,2\}. |  |

It introduced the following notion.

###### Definition 1.1.

The 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is given by

 | ℰ ⁡ ( ℤ 3):= { λ ∈ ℤ 3: for infinitely many n ≥ 0 the expansion ( 2 n ​ λ) 3 omits the digit 2 }. \mathcal{E}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{for infinitely many $n\geq 0$ the expansion $(2^{n}\lambda)_{3}$ omits the digit $2$}\}. |  |

This definition is less stringent than the Erdős problem in allowing variation of the new parameter λ \lambda. The weak version of Erdős’s conjecture above is equivalent to the assertion that 1 ∉ ℰ ⁡ ( ℤ 3) 1\notin\mathcal{E}(\mathbb{Z}_{3}).

That paper proposed the following conjecture [12, Conjecture 1.7].

###### Conjecture 1.2.

(Exceptional Set Conjecture) The 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) has Hausdorff dimension zero, i.e.

 | dim H ( ℰ ⁡ ( ℤ 3)) = 0. \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))=0. |  | (1.2) |

Clearly 0 ∈ ℰ ⁡ ( ℤ 3) 0\in\mathcal{E}(\mathbb{Z}_{3}), and our state of ignorance is such that we do not know whether ℰ ⁡ ( ℤ 3) = { 0 } \mathcal{E}(\mathbb{Z}_{3})=\{0\} or not. In [12] the Exceptional Set Conjecture was approached by introducing the sets

 | ℰ ( k) ​ ( ℤ 3):= { λ ∈ ℤ 3: at least k values of ( 2 n ​ λ) 3 omit the digit 2 }, \mathcal{E}^{(k)}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{at least $k$ values of $(2^{n}\lambda)_{3}$ omit the digit 2}\}, |  | (1.3) |

which yield the containment relation

 | ℰ ⁡ ( ℤ 3) ⊆ ⋂ k = 1 ∞ ℰ ( k) ​ ( ℤ 3). \mathcal{E}(\mathbb{Z}_{3})\subseteq\bigcap_{k=1}^{\infty}\mathcal{E}^{(k)}(\mathbb{Z}_{3}). |  | (1.4) |

That paper obtained the upper bound

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ dim H ( ℰ ( 2) ​ ( ℤ 3)) ≤ 1 2. \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))\leq\dim_{H}(\mathcal{E}^{(2)}(\mathbb{Z}_{3}))\leq\frac{1}{2}. |  |

The sets ℰ ( k) ​ ( ℤ 3) \mathcal{E}^{(k)}(\mathbb{Z}_{3}) form a nested family

 | Σ 3, 2 ¯ = ℰ ( 1) ​ ( ℤ 3) ⊇ ℰ ( 2) ​ ( ℤ 3) ⊇ ℰ ( 3) ​ ( ℤ 3) ⊇ ⋯, \Sigma_{3,\bar{2}}=\mathcal{E}^{(1)}(\mathbb{Z}_{3})\supseteq\mathcal{E}^{(2)}(\mathbb{Z}_{3})\supseteq\mathcal{E}^{(3)}(\mathbb{Z}_{3})\supseteq\cdots, |  |

and are themselves expressed in terms of intersection sets ( 1.1) as

 | ℰ ( k) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < … < m k 𝒞 ⁡ ( 2 m 1, …, 2 m k). \mathcal{E}^{(k)}(\mathbb{Z}_{3})=\bigcup_{0\leq m_{1}<\ldots<m_{k}}{{\mathcal{C}}}(2^{m_{1}},\ldots,2^{m_{k}}). |  | (1.5) |

This connection motivated the study made in [3] of the more general sets C ⁡ ( M 1, …, M k) C(M_{1},...,M_{k}).

###### Definition 1.3.

The (dyadic) nesting constant Γ \Gamma is given by

 | Γ:= lim k → ∞ dim H ( ℰ ( k) ​ ( ℤ 3)). \Gamma:=\lim_{k\to\infty}\dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3})). |  | (1.6) |

The containment relation ( 1.4) implies that the nesting constant upper bounds to the Hausdorff dimension of the exceptional set,

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ Γ. \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))\leq\Gamma. |  | (1.7) |

The third author raised the question in [12] whether Γ = 0 \Gamma=0, which if true would imply the Exceptional Set Conjecture. This question is currently unanswered.

Part I [3, Section 1.2] approached the problem of obtaining improved upper bounds for Γ \Gamma by introducing a relaxed upper bound Γ ⋆ \Gamma_{\star}, called there the generalized nesting constant, obtained by replacing 𝒞 ⁡ ( 2 m 1, …, 2 m k) {{\mathcal{C}}}(2^{m_{1}},\ldots,2^{m_{k}}) with 𝒞 ⁡ ( 1, M 1, …, M k − 1) {{\mathcal{C}}}(1,M_{1},...,M_{k-1}) in the definition above. That paper showed Γ ≤ Γ ⋆ ≤ 1 2 \Gamma\leq\Gamma_{\star}\leq\frac{1}{2}, and also established the lower bound

 | Γ ⋆ ≥ 1 2 ​ log 3 ​ ϕ ≈ 0.21909. \Gamma_{\star}\geq\frac{1}{2}\log_{3}\phi\approx 0.21909. |  |

It follows that one cannot resolve whether Γ = 0 \Gamma=0 or not using the relaxation Γ ⋆. \Gamma_{\star}.

### 1.2. Statistics of ternary digits and n n -digit Hausdorff dimension constant

A focus of this work was to shed light on the Exceptional set conjecture, by gathering evidence whether there might exist simple statistics of the ternary expansion ( M) 3 (M)_{3} of a single integer M M which will predict that the Hausdorff dimension dim H ( 𝒞 ⁡ ( 1, M)) \dim_{H}({\mathcal{C}}(1,M)) must go to 0 0 as the value of the statistic goes to infinity.

In this paper we resolve this question for the statistic d 3 ​ ( M) {d}_{3}(M) that counts the number of nonzero digits in the ternary expansion of the positive integer ( M) 3 (M)_{3}. This value coincides with the number of nonzero digits in the 3 3 -adic expansion of M M; note that a 3 3 -adic integer α \alpha has a finite number of non-zero digits if and only if it is a non-negative integer α ∈ ℕ \alpha\in{\mathbb{N}}.

###### Definition 1.4.

The n n -digit Hausdorff dimension constant α n {\alpha}_{n} is given by

 | α n:= sup M ≥ 1 { dim H ( 𝒞 ⁡ ( 1, M)): The expansion ( M) 3 has at least n nonzero ternary digits }. {\alpha}_{n}:=\sup_{M\geq 1}\{\dim_{H}({{\mathcal{C}}}(1,M)):\mbox{The expansion $(M)_{3}$ has at least $n$ nonzero ternary digits}\}. |  |

By definition the α n {\alpha}_{n} form a nonincreasing sequence of nonnegative numbers, so that the limit

 | Γ ⋆ ⁣ ⋆:= lim n → ∞ α n \Gamma_{\star\star}:=\lim_{n\to\infty}{\alpha}_{n} |  |

exists. Known results in number theory, detailed in Section 6, imply that the number of nonzero ternary digits of 2 n 2^{n} diverges as n n goes to infinity. Thus, we obtain an upper bound on the dyadic nesting constant

 | Γ ≤ Γ ⋆ ⁣ ⋆ = lim n → ∞ α n = inf n α n. \Gamma\leq\Gamma_{\star\star}=\lim_{n\to\infty}{\alpha}_{n}=\inf_{n}{\alpha}_{n}. |  | (1.8) |

One of the infinite families studied in this paper has d 3 ​ ( M k) → ∞ d_{3}(M_{k})\to\infty as k → ∞ k\to\infty and using it we show

 | Γ ⋆ ⁣ ⋆ = inf n α n = log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \Gamma_{\star\star}=\inf_{n}{\alpha}_{n}=\log_{3}\left(\frac{1+\sqrt{5}}{2}\right)\approx 0.438018. |  | (1.9) |

In particular by ( 1.7) we obtain an improved upper bound for the Hausdorff dimension of the exceptional set

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ Γ ≤ Γ ⋆ ⁣ ⋆ ≤ log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \dim_{H}(\mathcal{E}({\mathbb{Z}}_{3}))\leq\Gamma\leq\Gamma_{\star\star}\leq\log_{3}\left(\frac{1+\sqrt{5}}{2}\right)\approx 0.438018. |  | (1.10) |

In the opposite direction ( 1.9) establishes that the statistic d 3 ​ ( M) {d}_{3}(M) does not have the property that the Hausdorff dimension must go to 0 0 as the statistic d 3 ​ ( M) → ∞ {d}_{3}(M)\to\infty.

The final section of the paper empirically studies the Hausdorff dimension of 𝒞 ⁡ ( 1, M) {{\mathcal{C}}}(1,M) with respect to two other simple statistics of the ternary expansion ( M) 3 (M)_{3}: the block number b 3 ​ ( M) {b}_{3}(M) and intermittency s 3 ​ ( M) {s}_{3}(M); these satisfy b 3 ​ ( M) ≤ s 3 ​ ( M) {b}_{3}(M)\leq{s}_{3}(M). These are defined in Section 7.

### 1.3. Roadmap

Section 2 states the main results. Section 3 reviews properties of p p -adic path sets and their symbolic dynamics, drawing on [1] and [2]. Intersections of multiplicative translates of 3 3 -adic Cantor sets are a special case of these constructions. Section 3.4 introduces an interleaving operation on path sets and analyzes its effect on Hausdorff dimension. Section 4 studies the sets 𝒞 ⁡ ( 1, P k) {{\mathcal{C}}}(1,P_{k}) for the infinite family P k P_{k}, analyzes the structure of their associated automata, and proves Theorems 2.1 - 2.2, and additional results. Section 5 studies the structure of 𝒞 ⁡ ( 1, Q k) {{\mathcal{C}}}(1,Q_{k}) for the infinite family Q k Q_{k}, and proves Theorems 2.3 - 2.4. Section 6 deals with results on the quantities α n {\alpha}_{n} and proves Theorems 2.5 - 2.6. Section 7 presents empirical results on Hausdorff dimensions of C ⁡ ( 1, M) C(1,M) for M M having specified statistics of their ternary expansions ( M) 3 (M)_{3}.
Appendix A (Section 8) describes results for two infinite families 𝒞 ⁡ ( 1, L k) {{\mathcal{C}}}(1,L_{k}) and 𝒞 ⁡ ( 1, N k) {{\mathcal{C}}}(1,N_{k}) treated in Part I [3]. Appendix B (Section 9) relates Hausdorff dimensions of 𝒞 ⁡ ( 1, P k) {{\mathcal{C}}}(1,P_{k}) to those of 𝒞 ⁡ ( 1, L k + 1) {{\mathcal{C}}}(1,L_{k+1}).

Acknowledgments. We thank Yusheng Luo for an important observation on the structure of the automata for the sets P k P_{k}, incorporated in Definition 4.3 and Proposition 4.4. W. A. thanks the University of Michigan, where much of this work was carried out. W. A. and A. B. would also like to thank Ridgeview Classical Schools, which facilitated their collaboration. W.A. was partially supported by an NSF graduate fellowship. J. L. was supported by NSF grants DMS-1101373 and DMS-1401224. Some work of J.L. on the paper was done at ICERM, where he received support from the Clay Foundation as a Clay Senior Scholar. He thanks ICERM for support and good working conditions.

## 2. Results

The main results of this paper consist of determination of presentations of the 3 3 -adic path sets X ⁡ ( 1, P k) X(1,P_{k}) and X ⁡ ( 1, Q k) X(1,Q_{k}) associated to members of two infinite families 𝒞 ⁡ ( 1, P k) {\mathcal{C}}(1,P_{k}) and 𝒞 ⁡ ( 1, Q k) {\mathcal{C}}(1,Q_{k}) given below, with estimates of their Hausdorff dimensions, along with experimental results for dim H ( 𝒞 ⁡ ( 1, M)) \dim_{H}({{\mathcal{C}}}(1,M)) for certain other M M presented in Section 7.

### 2.1. The infinite family P k = ( 20 k − 1 ​ 1) 3 P_{k}=(20^{k-1}1)_{3}

We study the path set structure of families of integers having few nonzero ternary digits. The only infinite families of numbers having exactly two nonzero ternary digits and dim H ( 𝒞 ⁡ ( 1, N)) > 0 \dim_{H}({{\mathcal{C}}}(1,N))>0 are N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3} and P k = ( 20 k − 1 ​ 1) 3 = 2 ⋅ 3 k + 1 P_{k}=(20^{k-1}1)_{3}=2\cdot 3^{k}+1. The family N k N_{k} was studied in Part I and here we study the family P k P_{k}.

We directly compute the Hausdorff dimensions of the first few sets 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) using the algorithms of Part I to be the following.

Path Set | P k P_{k} | Vertices | Perron eigenvalue | Hausdorff dim |

𝒞 ⁡ ( 1, P 1) \mathcal{C}(1,P_{1}) | 7 | 4 | 1.618033 1.618033 | 0.438018 0.438018 |

𝒞 ⁡ ( 1, P 2) \mathcal{C}(1,P_{2}) | 19 | 8 | 1.465571 1.465571 | 0.347934 0.347934 |

𝒞 ⁡ ( 1, P 3) \mathcal{C}(1,P_{3}) | 55 | 16 | 1.380278 1.380278 | 0.293358 0.293358 |

𝒞 ⁡ ( 1, P 4) \mathcal{C}(1,P_{4}) | 163 | 32 | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1, P 5) \mathcal{C}(1,P_{5}) | 487 | 64 | 1.370957 1.370957 | 0.287191 0.287191 |

𝒞 ⁡ ( 1, P 6) \mathcal{C}(1,P_{6}) | 1459 | 128 | 1.388728 1.388728 | 0.298913 0.298913 |

𝒞 ⁡ ( 1, P 7) \mathcal{C}(1,P_{7}) | 4375 | 256 | 1.392067 1.392067 | 0.301010 0.301010 |

𝒞 ⁡ ( 1, P 8) \mathcal{C}(1,P_{8}) | 13123 | 512 | 1.387961 1.387961 | 0.298408 0.298408 |

TABLE 2.1. Hausdorff dimension of 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) (to six decimal places)

The first thing to observe from this data is the non-monotonic behavior of the Hausdorff dimension as a function of k k; the second observation is the possibility that the dimensions are bounded away from zero. Our results below explain both these features. We also observe that dim H ( 𝒞 ⁡ ( 1, P k)) = dim H ( 𝒞 ⁡ ( 1, L k + 1)) \dim_{H}(\mathcal{C}(1,P_{k}))=\dim_{H}(\mathcal{C}(1,L_{k+1})) for 1 ≤ k ≤ 4 1\leq k\leq 4 but equality does not hold for k = 5 k=5. In an Appendix B (Section 9) we show that dim H ( 𝒞 ⁡ ( 1, P k)) ≥ dim H ( 𝒞 ⁡ ( 1, L k + 1)) \dim_{H}(\mathcal{C}(1,P_{k}))\geq\dim_{H}(\mathcal{C}(1,L_{k+1})) holds in general.

Our first result determines properties of a presentation of the path set X ⁡ ( 1, P k) X(1,P_{k}). The resulting directed graphs are shown to be reducible, having a complicated structure with nested strongly connected components.

###### Theorem 2.1.

(Path set presentation for family P k P_{k})

(1) For P k = 2 ⋅ 3 k + 1 = ( 20 k − 1 ​ 1) 3 P_{k}=2\cdot 3^{k}+1=(20^{k-1}1)_{3}, the path set X ⁡ ( 1, P k) X(1,P_{k}) underlying 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) has a path set presentation ( 𝒢 k, v 0) ({\mathcal{G}}_{k},v_{0}) that has exactly 2 k + 1 2^{k+1} vertices.

(2) The graph 𝒢 k {\mathcal{G}}_{k} is a nested sequence of 1 + ⌊ k / 2 ⌋ 1+\lfloor k/2\rfloor distinct strongly connected components.

(3) The underlying graph G = G k G=G_{k} for 𝒢 k {\mathcal{G}}_{k} has an automorphism of order 2 2 and is a connected double cover of its quotient graph H k H_{k}.

The structure of G k G_{k} is that of a “Matryoshka doll" with a single set of nested components at each level. The non-monotonicity of the Hausdorff dimension as a function of k k can be related to the existence of multiple strongly connected components in the graphs G k G_{k}. The non-monotonicity occurs because of a switch in which strongly connected component has the largest topological entropy. We discuss this issue further in Section 4.2, see Remark 4.6.

Regarding the behavior of the Hausdorff dimension as k → ∞ k\to\infty, we establish the following result.

###### Theorem 2.2.

(Hausdorff dimension bounds for family P k = 2 ⋅ 3 k + 1 P_{k}=2\cdot 3^{k}+1)

(1) The Hausdorff dimension of 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) satisfies the asymptotic lower bound

 | lim inf k → ∞ dim H ( 𝒞 ⁡ ( 1, P k)) ≥ 1 8 ​ log 3 ⁡ ( 2). \liminf_{k\to\infty}\dim_{H}(\mathcal{C}(1,P_{k}))\geq\frac{1}{8}\log_{3}(2). |  |

(2) Furthermore, for all k ≥ 1 k\geq 1,

 | dim H ( 𝒞 ⁡ ( 1, P k)) ≥ 1 13 ​ log 3 ⁡ ( 2). \dim_{H}(\mathcal{C}(1,P_{k}))\geq\frac{1}{13}\log_{3}(2). |  |

The lower bounds in Theorem 2.2 are obtained by further inspection of the graph associated to 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}). We also have an upper bound

 | dim H ( 𝒞 ⁡ ( 1, P k)) ≤ log 3 ⁡ ϕ. \dim_{H}(\mathcal{C}(1,P_{k}))\leq\log_{3}\phi. |  |

which follows from Theorem 6.2 below.

In Section 4.3 we obtain additional results on intersection of sets in the infinite family P k P_{k} above. We show that the Hausdorff dimensions of arbitrarily large intersections are always positive. However this is no longer true if we allow intersections of sets from the infinite family P k P_{k} with those of the infinite family N k = ( 10 k − 1 ​ 1) 3 N_{k}=(10^{k-1}1)_{3} treated in [3, Sect. 4] and reviewed in Appendix A (Section 8), which also consists of numbers having exactly two nonzero ternary digits. For example, it is easy to show that for each k ≥ 1 k\geq 1,

 | 𝒞 ⁡ ( 1, N k, P k) = { 0 }, \mathcal{C}(1,N_{k},P_{k})=\{0\}, |  |

so that dim H ( 𝒞 ⁡ ( 1, N k, P k)) = 0 \dim_{H}(\mathcal{C}(1,N_{k},P_{k}))=0.

### 2.2. The infinite family Q k = ( 2 k ​ 0 k − 1 ​ 1) 3 Q_{k}=(2^{k}0^{k-1}1)_{3}

We next study an infinite family of integers whose number of nonzero ternary digits grows without bound: Q k = ( 2 k ​ 0 k − 1 ​ 1) 3 = 3 2 ​ k − 3 k + 1 Q_{k}=(2^{k}0^{k-1}1)_{3}=3^{2k}-3^{k}+1. The example Q 2 Q_{2} having a large Hausdorff dimension was found by computer search, and led to study of this family.

###### Theorem 2.3.

(Path set presentation for family Q k Q_{k})

(1) For Q k = 3 2 ​ k − 3 k + 1 = ( 2 k ​ 0 k − 1 ​ 1) 3 Q_{k}=3^{2k}-3^{k}+1=(2^{k}0^{k-1}1)_{3}, the path set X ⁡ ( 1, Q k) X(1,Q_{k}) underlying 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}) has a path set presentation ( 𝒢 k, v 0) (\mathcal{G}_{k},v_{0}) that has exactly 4 k 4^{k} vertices and 6 ⋅ 4 k − 1 6\cdot 4^{k-1} edges.

(2) The underlying graph 𝒢 k \mathcal{G}_{k} is strongly connected.

Though the number of nonzero ternary digits of Q k Q_{k} grows without bound, the Hausdorff dimension of 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}) is constant independent of k k.

###### Theorem 2.4.

(Hausdorff dimensions for family Q k = 3 2 ​ k − 3 k + 1 Q_{k}=3^{2k}-3^{k}+1) For all k ≥ 2 k\geq 2 the Hausdorff dimension of 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}) satisfies

 | dim H ( 𝒞 ⁡ ( 1, Q k)) = log 3 ⁡ ϕ ≈ 0.438018, \dim_{H}(\mathcal{C}(1,Q_{k}))=\log_{3}\phi\approx 0.438018, |  |

where ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2}.

This result is established by showing that the path set X ⁡ ( 1, Q k) X(1,Q_{k}) is given by an interleaving construction from the path set X ⁡ ( 1, Q 1) X(1,Q_{1}), that is X ( 1, Q k) = X ( 1, 7) ( ∗ k), X(1,Q_{k})=X(1,7)^{(\ast k)}, as defined in Section 3.4.

### 2.3. The n n -digit Hausdorff dimension constants α n {\alpha}_{n}.

It is a known fact that the number of nonzero ternary digits in ( 2 n) 3 (2^{n})_{3} goes to infinity as n → ∞ n\to\infty, i.e. for each k ≥ 2 k\geq 2 there are only finitely many n n with ( 2 n) 3 (2^{n})_{3} having at most k k nonzero ternary digits. Using this fact we easily deduce the following consequence.

###### Theorem 2.5.

The nesting constant Γ \Gamma satisfies

 | Γ ≤ lim n → ∞ α n. \Gamma\leq\lim_{n\to\infty}{\alpha}_{n}. |  | (2.1) |

In particular

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ Γ ∗ ⁣ ∗ = lim n → ∞ α n. \dim_{H}(\mathcal{E}({\mathbb{Z}}_{3}))\leq\Gamma_{**}=\lim_{n\to\infty}{\alpha}_{n}. |  |

It follows that individual values α n {\alpha}_{n} give upper bounds on Γ \Gamma.

###### Theorem 2.6.

We have for all k ≥ 2 k\geq 2 that

 | α k = log 3 ⁡ ϕ ≈ 0.438018, {\alpha}_{k}=\log_{3}\phi\approx 0.438018, |  |

where ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} is the golden ratio. This value is attained by 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}) for

 | Q k:= ( 2 k ​ 0 k − 1 ​ 1) 3. Q_{k}:=(2^{k}0^{k-1}1)_{3}. |  |

In particular this result yields an improved upper bound on the nesting constant

 | Γ ≤ log 3 ⁡ ϕ, \Gamma\leq\log_{3}\phi, |  |

and on the Hausdorff dimension of the Exceptional set. It also gives

 | Γ ⋆ ⁣ ⋆ = log 3 ⁡ ϕ ≈ 0.438018. \Gamma_{\star\star}=\log_{3}\phi\approx 0.438018. |  |

We prove Theorem 2.6 in Section 6.2.

Using the known bound for the generalized dyadic nesting constant Γ ⋆ ≤ α 2 \Gamma_{\star}\leq{\alpha}_{2} established in Part I [3, (1.16)] we obtain the following corollary.

###### Corollary 2.7.

We have

 | Γ ∗ ≤ log 3 ⁡ ϕ ≈ 0.438018, \Gamma_{\ast}\leq\log_{3}\phi\approx 0.438018, |  |

in which ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} is the golden ratio.

### 2.4. Notation

The notation ( m) 3 (m)_{3} means either the base 3 3 expansion of the positive integer m m, or else the 3 3 -adic expansion of ( m) 3 (m)_{3}. In the 3 3 -adic case this expansion is to be read right to left, so that it is compatible with the ternary expansion. That is, α = ∑ j = 0 ∞ a j ​ 3 j \alpha=\sum_{j=0}^{\infty}a_{j}3^{j} will be written ( ⋯ a 2 a 1 a 0) 3 (\cdots a_{2}a_{1}a_{0})_{3}.

## 3. Symbolic dynamics, path sets and p p -adic path set fractals

### 3.1. Symbolic dynamics, graphs and finite automata

The constructions of this paper are based on the fact that the points in intersections of multiplicative translates of 3 3 -adic Cantor sets have 3 3 -adic expansions that are describable in terms of allowable paths generated by finite directed labeled graphs. We use symbolic dynamics on certain closed subsets of the one-sided shift space Σ = 𝒜 ℕ \Sigma={\mathcal{A}}^{{\mathbb{N}}} with fixed symbol alphabet 𝒜 {\mathcal{A}}, which for our application will be specialized to 𝒜 = { 0, 1, 2 } {\mathcal{A}}=\{0,1,2\}. A basic reference for directed graphs and symbolic dynamics, which we follow, is Lind and Marcus [14].

By a graph we mean a finite directed graph, allowing loops and multiple edges. A labeled graph is a graph assigning labels to each directed edge; these labels are drawn from a finite symbol alphabet. A labeled directed graph can be interpreted as a finite automaton in the sense of automata theory. In our applications to 3 3 -adic digit sets, the labels are drawn from the alphabet 𝒜 = { 0, 1, 2 }. {\mathcal{A}}=\{0,1,2\}. In a directed graph, a vertex is a source if all directed edges touching that vertex are outgoing; it is a sink if all directed edges touching that edge are incoming. A vertex is essential if it is neither a source nor a sink; and is called stranded otherwise. A graph is *essential*if all of its vertices are essential. A graph G G is strongly connected if for each two vertices i, j i,j there is a directed path from i i to j j. We let S ​ C ​ ( G) SC(G) denote the set of strongly connected component subgraphs of G G.

We use some basic facts from the Perron-Frobenius theory of nonnegative matrices. The Perron eigenvalue ( [14, Definition 4.4.2]) of a nonnegative real matrix 𝐀 ≠ 0 \mathbf{A}\neq 0 is the largest real eigenvalue β ≥ 0 \beta\geq 0 of 𝐀 \mathbf{A}. A nonnegative matrix is irreducible if for each row and column ( i, j) (i,j) some power 𝐀 m {\bf A}^{m} has ( i, j) (i,j) -th entry nonzero. A nonnegative matrix 𝐀 {\bf A} is primitive if some power 𝐀 k {\bf A}^{k} for an integer k ≥ 1 k\geq 1 has all entries positive; primitivity implies irreducibility but not vice versa. The Perron-Frobenius Theorem [14, Theorem 4.2.3] for an irreducible nonnegative matrix 𝐀 {\bf A} states that:

1. (1)

The Perron eigenvalue β \beta is geometrically and algebraically simple, and has an everywhere positive eigenvector 𝐯. {\bf v}.

2. (2)

All other eigenvalues μ \mu have | μ | ≤ β |\mu|\leq\beta, so that β = σ ⁡ ( 𝐀) \beta=\sigma({\bf A}), the spectral radius of 𝐀 {\bf A}.

3. (3)

Any other everywhere positive eigenvector must be a positive multiple of 𝐯 {\bf v}.

For a general nonnegative real matrix 𝐀 ≠ 0 \mathbf{A}\neq 0, the Perron eigenvalue need not be simple, but it still equals the spectral radius σ ⁡ ( 𝐀) \sigma(\bf{A}) and it has at least one everywhere nonnegative eigenvector.

We apply this theory to adjacency matrices of graphs. A (vertex-vertex) adjacency matrix 𝐀 = 𝐀 G {\bf A}={\bf A}_{G} of the directed graph G G has entry a i ​ j a_{ij} counting the number of directed edges from vertex i i to vertex j j. The adjacency matrix is irreducible if and only if the associated graph is strongly connected, and we also call the graph irreducible in this case. Here primitivity of the adjacency matrix of a directed graph G G is equivalent to the graph being strongly connected and aperiodic, i. e. the greatest common divisor of its (directed) cycle lengths is 1 1. For an adjacency matrix of a graph containing at least one directed cycle, its Perron eigenvalue is necessarily a real algebraic integer β ≥ 1 \beta\geq 1 (see Lind [13] for a characterization of these numbers).

### 3.2. p p -Adic path sets, sofic shifts and p p -adic path set fractals

Our basic objects are special cases of the following definition. A pointed graph is a pair ( 𝒢, v) ({\mathcal{G}},v) consisting of a directed labeled graph 𝒢 = ( G, ℰ) {\mathcal{G}}=(G,\mathcal{E}) and a marked vertex v v of 𝒢 {\mathcal{G}}. Here G G is a (directed) graph and ℰ \mathcal{E} is an assignment of labels ( e, ℓ) = ( v 1, v 2, ℓ) (e,\ell)=(v_{1},v_{2},\ell) to the edges of G G, where every edge gets a single label, and no two triples are the same (but multiple edges and loops are permitted otherwise).

###### Definition 3.1.

Given a pointed graph ( 𝒢, v) ({\mathcal{G}},v) its associated *path set*𝒫 = X 𝒢 ​ ( v) ⊂ 𝒜 ℕ {\mathcal{P}}=X_{\mathcal{G}}(v)\subset{\mathcal{A}}^{{\mathbb{N}}} is the set of all infinite one-sided symbol sequences ( x 0, x 1, x 2, …) ∈ 𝒜 ℕ (x_{0},x_{1},x_{2},...)\in{\mathcal{A}}^{{\mathbb{N}}}, giving the successive labels of all one-sided infinite walks in 𝒢 \mathcal{G} issuing from the distinguished vertex v v. Many different ( 𝒢, v) (\mathcal{G},v) may give the same path set 𝒫 {\mathcal{P}}, and we call any such ( 𝒢, v) (\mathcal{G},v) a *presentation*of 𝒫 {\mathcal{P}}.

An important class of presentations have the following extra property. We say that a directed labeled graph 𝒢 = ( G, v) {\mathcal{G}}=(G,v) is right-resolving if for each vertex of 𝒢 {\mathcal{G}} all directed edges outward have distinct labels. (In automata theory 𝒢 {\mathcal{G}} is called a deterministic automaton.) One can show that every path set has a right-resolving presentation.

Note that the labeled graph 𝒢 {\mathcal{G}} without a marked vertex determines a one-sided sofic shift in the sense of symbolic dynamics, as defined in [1]. This sofic shift comprises the set union of the path sets at all vertices of 𝒢 {\mathcal{G}}. Path sets are closed sets in the shift topology, but are in general non-invariant under the one-sided shift operator. Those path sets 𝒫 {\mathcal{P}} that are invariant are exactly the one-sided sofic shifts [1, Theorem 1.4].

We study the path set concept in symbolic dynamics in [1]. The collection of path sets 𝒫 = X 𝒢 ​ ( v) \mathcal{P}=X_{{\mathcal{G}}}(v) in a given alphabet is closed under finite union and intersection ( [1, Theorem 1.2]). The symbolic dynamics analogue of Hausdorff dimension is topological entropy. The topological entropy of a path set H t ​ o ​ p ​ ( 𝒫) H_{top}(\mathcal{P}) is given by

 | H t ​ o ​ p ​ ( 𝒫):= lim sup n → ∞ 1 n ​ log ⁡ N n ​ ( 𝒫), H_{top}(\mathcal{P}):=\limsup_{n\to\infty}\frac{1}{n}\log N_{n}(\mathcal{P}), |  |

where N n ​ ( 𝒫) N_{n}(\mathcal{P}) counts the number of distinct blocks of symbols of lengh n n appearing in elements of 𝒫 \mathcal{P}. The topological entropy is easy to compute given a right-resolving presentation. By [1, Theorem 1.13], it is

 | H t ​ o ​ p ​ ( 𝒫) = log ⁡ β H_{top}(\mathcal{P})=\log\beta |  | (3.1) |

where β \beta is the Perron eigenvalue of the adjacency matrix 𝐀 = 𝐀 G {\bf A}={\bf A}_{G} of the underlying directed graph G G of 𝒢 {\mathcal{G}}, e.g. the spectral radius of 𝐀 {\bf A}.

### 3.3. p p -Adic symbolic dynamics and graph directed constructions

We now suppose 𝒜 = { 0, 1, 2, …, p − 1 } {\mathcal{A}}=\{0,1,2,...,p-1\}. We can view the elements of a path set 𝒫 \mathcal{P} on this alphabet geometrically as describing the digits in the 3 3 -adic expansion of a 3 3 -adic integer. This is done using a map ϕ: 𝒜 ℕ → ℤ p \phi:{\mathcal{A}}^{{\mathbb{N}}}\to{\mathbb{Z}}_{p} from symbol sequences into ℤ p {\mathbb{Z}}_{p}. We call the resulting image set K = ϕ ⁡ ( 𝒫) K=\phi(\mathcal{P}) a *p p -adic path set fractal*. Such sets are studied in [2], where they are related to graph-directed fractal constructions. The class of p p -adic path set fractals is closed under the Minkowski sum and p p -adic addition and multiplication by rational numbers r ∈ ℚ r\in{\mathbb{Q}} that lie in ℤ p {\mathbb{Z}}_{p} ( [2, Theorems 1.2-1.4]).

It is possible to compute the Hausdorff dimension of a p p -adic path set fractal directly from a suitable presentation of the underlying path set 𝒫 = X 𝒢 ​ ( v) \mathcal{P}=X_{{\mathcal{G}}}(v). We will use the following result.

###### Proposition 3.2.

Let p p be a prime, and K K a set of p p -adic integers whose allowable p p -adic expansions are described by the symbolic dynamics of a p p -adic path set X K X_{K} on symbols 𝒜 = { 0, 1, 2, ⋯, p − 1 } \mathcal{A}=\{0,1,2,\cdots,p-1\}. Let ( 𝒢, v) (\mathcal{G},v) be a presentation of this path set that is right-resolving.

(1) The map ϕ p: ℤ p → [0, 1] \phi_{p}:\mathbb{Z}_{p}\rightarrow[0,1] taking α = ∑ k = 0 ∞ a k ​ p k ∈ ℤ p \alpha=\sum_{k=0}^{\infty}{a_{k}p^{k}}\in\mathbb{Z}_{p} to the real number with base p p expansion ϕ p ​ ( α):= ∑ k = 0 ∞ a k p k + 1 \phi_{p}(\alpha):=\sum_{k=0}^{\infty}\frac{a_{k}}{p^{k+1}} is a continuous map, and the image of K K under this map, K ′:= ϕ p ​ ( K) ⊂ [0, 1] K^{\prime}:=\phi_{p}(K)\subset[0,1], is a graph-directed fractal in the sense of Mauldin-Williams.

(2) The Hausdorff dimension of the p p -adic path set fractal K K is

 | dim H ( K) = dim H ( K ′) = log p ⁡ β, \dim_{H}(K)=\dim_{H}(K^{\prime})=\log_{p}\beta, |  | (3.2) |

where β \beta is the spectral radius of the adjacency matrix 𝐀 {\bf A} of G G.

###### Proof.

These results are proved in [2, Section 2]. ∎

In this paper we treat the case p = 3 p=3 with 𝒜 = { 0, 1, 2 } {\mathcal{A}}=\{0,1,2\}. The 3 3 -adic Cantor set is a 3 3 -adic path set fractal, so these general properties above guarantee that the intersection of a finite number of multiplicative translates of 3 3 -adic Cantor sets will itself be a 3 3 -adic path set fractal K K, generated from an underlying path set.

To do calculations with such sets we will need algorithms for converting presentations of a given p p -adic path set to presentations of new p p -adic path sets derived by the operations above. We refer the reader to [2] for the p p -adic arithmetic operations, and to [1] for union and intersection. A further useful operation called interleaving will be developed in the next subsection; this operation is sometimes useful in computing Hausdorff dimension.

### 3.4. Interleaving operation on path sets

Let 𝒫 = X 𝒢 ​ ( v) ⊂ 𝒜 ℕ \mathcal{P}=X_{\mathcal{G}}(v)\subset\mathcal{A}^{\mathbb{N}} be a path set, and let n n be a positive integer. In the paper [1] the first and third authors studied a decimation operation on path sets. Given j ≥ 0 j\geq 0 and m ≥ 1 m\geq 1, define the decimation map ψ j, m: 𝒜 ℕ → 𝒜 ℕ \psi_{j,m}:{\mathcal{A}}^{{\mathbb{N}}}\to{\mathcal{A}}^{{\mathbb{N}}} by

 | ψ j, m ( a 0 a 1 a 2 ⋯):= ( a j a j + m a j + 2 ​ m ⋯). \psi_{j,m}(a_{0}a_{1}a_{2}\cdots):=(a_{j}a_{j+m}a_{j+2m}\cdots). |  |

The decimation operation extracts the digits of the path set in a specified infinite arithmetic progression of indices. We set

 | ψ j, m ​ ( 𝒫):= { ψ j, m ​ ( x): x ∈ 𝒫 }. \psi_{j,m}({\mathcal{P}}):=\{\psi_{j,m}(x):x\in{\mathcal{P}}\}. |  |

Here [1, Theorem 1.5] proved that if 𝒫 {\mathcal{P}} is a path set, then for each fixed ( j, m) (j,m) with j ≥ 0, m ≥ 1 j\geq 0,m\geq 1 the sets ψ j, m ​ ( 𝒫) \psi_{j,m}({\mathcal{P}}) are path sets.

Here we consider a kind of inverse operator to decimation, which we term interleaving.

###### Definition 3.3.

Let n ≥ 1 n\geq 1 be given. The n n -interleaving of a closed set 𝒳 ⊂ 𝒜 ℕ \mathcal{X}\subset{\mathcal{A}}^{{\mathbb{N}}} (not necessarily a path set) is

 | 𝒳 ( ∗ n):= { ( x i) i = 0 ∞ ∈ 𝒜 ℕ: ( x j, x j + n, x j + 2 ​ n, ⋯) ∈ 𝒳 for all 0 ≤ j ≤ n − 1 }. \mathcal{X}^{(*n)}:=\{(x_{i})_{i=0}^{\infty}\in\mathcal{A}^{\mathbb{N}}\,:\,(x_{j},x_{j+n},x_{j+2n},\cdots)\in\mathcal{X}\text{ for all }0\leq j\leq n-1\}. |  |

We will show that the interleaving 𝒫 ( ∗ n) \mathcal{P}^{(*n)} is itself a path set, and that its topological entropy is the same as that of 𝒫 \mathcal{P}.

###### Proposition 3.4.

(1) For any n ≥ 1 n\geq 1 and any path set 𝒫 \mathcal{P}, the n n -interleaving set 𝒫 ( ∗ n) \mathcal{P}^{(*n)} is a path set.

(2) There is an algorithm taking n n and a path set presentation 𝒢 \mathcal{G} of 𝒫 \mathcal{P} and giving a path set presentation ℋ \mathcal{H} of 𝒫 ( ∗ n) \mathcal{P}^{(*n)}. If 𝒢 \mathcal{G} has k k verticies and m m edges, then ℋ \mathcal{H} has k n k^{n} verticies and m ​ k n − 1 mk^{n-1} edges.

###### Proof.

It suffices to prove (2). Suppose 𝒫 = X 𝒢 ​ ( v 0) \mathcal{P}=X_{\mathcal{G}}(v_{0}), and that the vertices of 𝒢 \mathcal{G} are v 0, v 1, …, v k − 1 v_{0},v_{1},\ldots,v_{k-1}, so that 𝒢 \mathcal{G} has k k vertices. Let l j l_{j} be the label of vertex v j v_{j} for each 0 ≤ j ≤ k − 1 0\leq j\leq k-1. If the l j l_{j} do not all have the same number of digits, append 0 ′ ​ s 0^{\prime}s to the left of labels as necessary to ensure that the labels l 0, …, l j l_{0},\ldots,l_{j} are distinct and have the same number of digits.

The vertex set of ℋ \mathcal{H} will be V = { v i 1, i 2, …, i n | 0 ≤ i j ≤ k − 1 ​ for all j } V=\{v_{i_{1},i_{2},\ldots,i_{n}}|0\leq i_{j}\leq k-1\text{ for all j}\}, so that ℋ \mathcal{H} will have k n k^{n} vertices. The vertex v i 1, i 2, …, i n v_{i_{1},i_{2},\ldots,i_{n}} will have label l = l i 1 ⋆ l i 2 ⋆ ⋯ ⋆ l i n l=l_{i_{1}}\star l_{i_{2}}\star\cdots\star l_{i_{n}}, that is, the concatenation of the labels of v i 1, v i 2, …, v i n v_{i_{1}},v_{i_{2}},\ldots,v_{i_{n}}. Since the labels l j l_{j} are all distinct and have the same number of digits, the vertex labels in ℋ \mathcal{H} as defined will also be distinct.

Now for each edge labeled a a from v i v_{i} to v j v_{j} in 𝒢 \mathcal{G}, construct an edge labeled a a from v i 1, i 2, …, i n − 1, i v_{i_{1},i_{2},\ldots,i_{n-1},i} to v j, i 1, i 2, …, i n − 1 v_{j,i_{1},i_{2},\ldots,i_{n-1}} for all 0 ≤ i 1, i 2, …, i n − 1 ≤ k − 1 0\leq i_{1},i_{2},\ldots,i_{n-1}\leq k-1. Thus, for each edge of 𝒢 \mathcal{G}, ℋ \mathcal{H} will have k n − 1 k^{n-1} corresponding edges, so that if 𝒢 \mathcal{G} has m m edges, then ℋ \mathcal{H} has m ​ k n − 1 mk^{n-1} edges. ℋ \mathcal{H} is evidently right-resolving or strongly connected if 𝒢 \mathcal{G} is right-resolving or strongly connected, respectively. For simplicity, we will assume from here that 𝒢 \mathcal{G} is right-resolving. We can do this since if 𝒢 \mathcal{G} is not right-resolving, we can perform the right-resolving construction of [1, Section 3] to obtain a right-resolving presentation of 𝒫 \mathcal{P}, and proceed with this presentation in place of 𝒢 \mathcal{G}.

We claim that 𝒫 ( ∗ n) = X ℋ ( v 0, 0, …, 0) \mathcal{P}^{(*n)}=X_{\mathcal{H}}(v_{0,0,\ldots,0}). First we will show that 𝒫 n ⊆ X ℋ ​ ( v 0, 0, …, 0) \mathcal{P}^{n}\subseteq X_{\mathcal{H}}(v_{0,0,\ldots,0}). Suppose ( x t) t = 0 ∞ ∈ 𝒫 n (x_{t})_{t=0}^{\infty}\in\mathcal{P}^{n}. Then there must be elements

 | ( x 0, t) t = 0 ∞, ( x 1, t) t = 0 ∞, …, ( x n − 1, t) t = 0 ∞ ∈ 𝒫 (x_{0,t})_{t=0}^{\infty},(x_{1,t})_{t=0}^{\infty},\ldots,(x_{n-1,t})_{t=0}^{\infty}\in\mathcal{P} |  |

such that x j, t = x n ​ t + j x_{j,t}=x_{nt+j} for all 0 ≤ j ≤ n − 1 0\leq j\leq n-1 and 0 ≤ t < ∞ 0\leq t<\infty. Since 𝒢 \mathcal{G} is right-resolving, each of these elements of 𝒫 \mathcal{P} corresponds to a unique infinite vertex path v 0, v i j, 0, v i j, 1, … v_{0},v_{i_{j,0}},v_{i_{j,1}},\ldots in 𝒢 \mathcal{G}. We can traverse an initial path in the pointed graph ℋ ⁡ ( v 0, 0, 0, …, 0) \mathcal{H}(v_{0,0,0,\ldots,0}) with labels
x 0, x 1, …, x n − 1 x_{0},x_{1},\ldots,x_{n-1}, since there are edges with each of these labels emanating from v 0 v_{0} in 𝒢 \mathcal{G}. This path takes us to the vertex v i n − 1, 0, i n − 2, 0, …, i 0, 0 v_{i_{n-1,0},i_{n-2,0},\ldots,i_{0,0}}. Since there is a vertex labeled x n + j x_{n+j} emenating fom vertex v i j, 0 v_{i_{j,0}} and going to v i j, 1 v_{i_{j,1}} for all 0 ≤ j ≤ n − 1 0\leq j\leq n-1, we can extend our path to a path labeled x 0, x 1, …, x 2 ​ n − 1 x_{0},x_{1},\ldots,x_{2n-1} beginning at v 0, 0, …, 0 v_{0,0,\ldots,0} and ending at v i n − 1, 1, i n − 2, 1, …, i 0, 1 v_{i_{n-1,1},i_{n-2,1},\ldots,i_{0,1}}.

Inductively, assume we have constructed a path with labels x 0, x 1, …, x r ​ n − 1 x_{0},x_{1},\ldots,x_{rn-1} in ℋ \mathcal{H} originating at v 0, 0, …, 0 v_{0,0,\ldots,0} and terminating at v i n − 1, r − 1, i n − 2, r − 1, …, i 0, r − 1 v_{i_{n-1,r-1},i_{n-2,r-1},\ldots,i_{0,r-1}}. Then since there is an edge in 𝒢 \mathcal{G} labeled x r ​ n + j x_{rn+j} from v j, r − 1 v_{j,r-1} to v j, r v_{j,r}, we can extend our path to a path labeled x 0, x 1, …, x ( r + 1) ​ n − 1 x_{0},x_{1},\ldots,x_{(r+1)n-1} terminating at v i n − 1, r, i n − 2, r, …, i 0, r v_{i_{n-1,r},i_{n-2,r},\ldots,i_{0,r}}. Thus, there is an infinite path in ℋ \mathcal{H} originating at v 0, 0, …, 0 v_{0,0,\ldots,0} with label ( x 0, x 1, x 2, …) (x_{0},x_{1},x_{2},\ldots), so ( x i) i = 0 ∞ ∈ X ℋ ​ ( v 0, 0, …, 0) (x_{i})_{i=0}^{\infty}\in X_{\mathcal{H}}(v_{0,0,\ldots,0}), hence 𝒫 n ⊆ X ℋ ​ ( v 0, 0, …, 0) \mathcal{P}^{n}\subseteq X_{\mathcal{H}}(v_{0,0,\ldots,0}).

Now to show X ℋ ​ ( v 0, 0, …, 0) ⊆ 𝒫 n X_{\mathcal{H}}(v_{0,0,\ldots,0})\subseteq\mathcal{P}^{n}: Suppose ( x i) i = 0 ∞ (x_{i})_{i=0}^{\infty} is an element of X ℋ ​ ( v 0, 0, …, 0) X_{\mathcal{H}}(v_{0,0,\ldots,0}). Then there is a vertex path v 0, 0, …, 0; v i 0, 0, …, 0; v i 1, i 0, 0, …, 0; …; v i n − 1, i n − 2; …, i 0; … v_{0,0,\ldots,0};v_{i_{0},0,\ldots,0};v_{i_{1},i_{0},0,\ldots,0};\ldots;v_{i_{n-1},i_{n-2};\ldots,i_{0}};\ldots in ℋ \mathcal{H} which can be traversed by edges labeled x 0, x 1, … x_{0},x_{1},\ldots. Notice that the first coordinate of a vertex must be the last coordinate of the vertex that follows after n − 1 n-1 steps. Since the initial vertex is v 0, 0, …, 0 v_{0,0,\ldots,0}, we know that for each 0 ≤ j ≤ n − 1 0\leq j\leq n-1, there is an edge in 𝒢 \mathcal{G} labeled x j x_{j} from v 0 v_{0} to v i j v_{i_{j}}. For any j < ∞ j<\infty, an edge in ℋ \mathcal{H} labeled x j x_{j} from v i 1, i 2, …, i n v_{i_{1},i_{2},\ldots,i_{n}} to v i n + 1, i 1, i 2, …, i n − 1 v_{i_{n+1},i_{1},i_{2},\ldots,i_{n-1}} corresponds to an edge in 𝒢 \mathcal{G} labeled x j x_{j} fom v i n v_{i_{n}} to v i n + 1 v_{i_{n+1}}. Following our path in ℋ \mathcal{H} for n − 1 n-1 more steps gets us to a vertex whose last coordinate is i n + 1 i_{n+1}, so the edge in ℋ \mathcal{H} labeled x n + j x_{n+j} emanating from this vertex corresponds to an edge in 𝒢 \mathcal{G} labeled x n + j x_{n+j} emanating from v i n + 1 v_{i_{n+1}}. Thus, for each 0 ≤ j ≤ n − 1 0\leq j\leq n-1, the labels ( x j, x j + n ​ x j + 2 ​ n, …) (x_{j},x_{j+n}x_{j+2n},\ldots) are the labels of an infinite path in 𝒢 \mathcal{G} originating at v 0 v_{0}, so ( x i) i = 0 ∞ ∈ 𝒫 n (x_{i})_{i=0}^{\infty}\in\mathcal{P}^{n}, hence X ℋ ​ ( v 0, 0, …, 0) ⊆ 𝒫 n X_{\mathcal{H}}(v_{0,0,\ldots,0})\subseteq\mathcal{P}^{n}, as desired. ∎

###### Remark 3.5.

(1) The presentation ℋ \mathcal{H} of 𝒫 ( ∗ n) \mathcal{P}^{(*n)} given in the proof above is right-resolving (resp. strongly connected) if and only if the presentation 𝒢 \mathcal{G} of 𝒫 \mathcal{P} used in its construction is right-resolving (resp. strongly connected).

(2) The operation of interleaving can be extended to interleave several different sets

 | ℐ ( X 1, X 2, …, X m):= { x ∈ 𝒜 ℕ: ψ j, m ( x) ∈ X i for 0 ≤ j ≤ m − 1. } {\mathcal{I}}(X_{1},X_{2},...,X_{m}):=\{x\in{\mathcal{A}}^{{\mathbb{N}}}:\psi_{j,m}(x)\in X_{i}\quad\mbox{for}\quad 0\leq j\leq m-1.\} |  |

One can show that if each X i = 𝒫 i X_{i}={\mathcal{P}}_{i} is a path set then ℐ ⁡ ( 𝒫 1, 𝒫 2, ⋯, 𝒫 n) {\mathcal{I}}({\mathcal{P}}_{1},{\mathcal{P}}_{2},\cdots,{\mathcal{P}}_{n}) is a path set.

We next show that the n n -interleaving operation 𝒫 ( ∗ n) \mathcal{P}^{(*n)} has the nice feature that it preserves topological entropy. Following [1] we define the *path topological entropy*H p ​ ( 𝒫) H_{p}(\mathcal{P}) of a path set 𝒫 \mathcal{P} by

 | H p ​ ( 𝒫):= lim sup k → ∞ 1 k ​ log ⁡ N k I ​ ( 𝒫), H_{p}(\mathcal{P}):=\limsup_{k\rightarrow\infty}\frac{1}{k}\log N_{k}^{I}(\mathcal{P}), |  | (3.3) |

where N k I ​ ( 𝒫) N_{k}^{I}(\mathcal{P}) is the number of *initial*blocks of length k k from 𝒫 \mathcal{P}, then [1, Theorem 1.11] shows that

 | H p ​ ( 𝒫) = H t ​ o ​ p ​ ( 𝒫), H_{p}(\mathcal{P})=H_{top}(\mathcal{P}), |  | (3.4) |

and that the lim sup \limsup ’s are obtained as limits.

###### Proposition 3.6.

If 𝒫 \mathcal{P} is a path set, then

 | H t ​ o ​ p ( 𝒫 ( ∗ n)) = H t ​ o ​ p ( 𝒫). H_{top}(\mathcal{P}^{(*n)})=H_{top}(\mathcal{P}). |  | (3.5) |

###### Proof.

Using ( 3.4), it suffices to show that 𝒫 \mathcal{P} and 𝒫 ( ∗ n) \mathcal{P}^{(*n)} have the same path entropy. But we can see directly from the definition of 𝒫 ( ∗ n) \mathcal{P}^{(*n)} that N n ​ k I ( 𝒫 ( ∗ n)) = ( N k I ( 𝒫)) n N_{nk}^{I}(\mathcal{P}^{(*n)})=(N_{k}^{I}(\mathcal{P}))^{n}, since an initial path of length n ​ k nk in 𝒫 ( ∗ n) \mathcal{P}^{(*n)} corresponds to n n (not necessarily distinct) initial paths of length k k in 𝒫 \mathcal{P}. Thus,

 | H p ( 𝒫 ( ∗ n)) \displaystyle H_{p}(\mathcal{P}^{(*n)}) | = lim k → ∞ 1 k log N k I ( 𝒫 ( ∗ n)) \displaystyle=\lim_{k\rightarrow\infty}\frac{1}{k}\log N_{k}^{I}(\mathcal{P}^{(*n)}) |  |

 |  | = lim k → ∞ 1 n ​ k log N n ​ k I ( 𝒫 ( ∗ n)) \displaystyle=\lim_{k\rightarrow\infty}\frac{1}{nk}\log N_{nk}^{I}(\mathcal{P}^{(*n)}) |  |

 |  | = lim k → ∞ 1 n ​ k ​ log ⁡ [( N k I ​ ( 𝒫)) n] \displaystyle=\lim_{k\rightarrow\infty}\frac{1}{nk}\log[(N_{k}^{I}(\mathcal{P}))^{n}] |  |

 |  | = lim k → ∞ 1 k ​ log ⁡ N k I ​ ( 𝒫) = H p ​ ( 𝒫), \displaystyle=\lim_{k\rightarrow\infty}\frac{1}{k}\log N_{k}^{I}(\mathcal{P})=H_{p}(\mathcal{P}), |  |

as desired. ∎

If 𝒜 = { 0, 1, …, p − 1 } \mathcal{A}=\{0,1,\ldots,p-1\}, let ϕ: 𝔸 ℕ → ℤ p \phi:\mathbb{A}^{\mathbb{N}}\rightarrow\mathbb{Z}_{p} be the map of Section 3.3, which maps the path set 𝒫 \mathcal{P} to the corresponding p p -adic path set fractal K = ϕ ⁡ ( 𝒫) K=\phi(\mathcal{P}). We have the following Corollary.

###### Corollary 3.7.

If 𝒫 \mathcal{P} is a path set on the alphabet 𝒜 = { 0, 1, 2, …, p − 1 } \mathcal{A}=\{0,1,2,\ldots,p-1\}, then the p p -adic path set fractals K = ϕ ⁡ ( 𝒫) K=\phi(\mathcal{P}) and K ′ = ϕ ( 𝒫 ( ∗ n)) K^{\prime}=\phi(\mathcal{P}^{(*n)}) have the same Hausdorff dimension.

###### Proof.

This follows immediately from ( 3.1), Proposition 3.6, and Proposition 3.2. ∎

###### Remark 3.8.

(1) Corollary 3.7 is useful in computing Hausdorff dimensions of path sets in our examples. Let 𝒫 = X ⁡ ( 1, 4) \mathcal{P}=X(1,4) be the Golden Mean Shift, which is also the path set underlying the 3 3 -adic path set fractal 𝒞 ⁡ ( 1, 4) \mathcal{C}(1,4). An element of 𝒞 ⁡ ( 1, N k) = 𝒞 ⁡ ( 1, ( 10 k − 1 ​ 1) 3) \mathcal{C}(1,N_{k})=\mathcal{C}(1,(10^{k-1}1)_{3}) is any 3 3 -adic integer consisting of 0 0 ’s and 1 1 ’s and for which no 1 1 is followed k k digits later by another 1 1. Recognizing this property allows us to see for N k = ( 10 k − 1 ​ 1) 3 = 3 k + 1 N_{k}=(10^{k-1}1)_{3}=3^{k}+1 that the path set X ⁡ ( 1, N k) X(1,N_{k}) underlying 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) is just 𝒫 ( ∗ k) \mathcal{P}^{(*k)}. Corollary 3.7 provides another proof of a result in part I ( [3, Theorem 5.5]) asserting that dim H ( 𝒞 ⁡ ( 1, N k)) = log 3 ⁡ ϕ \dim_{H}(\mathcal{C}(1,N_{k}))=\log_{3}\phi, since this now follows from the basic computation dim H ( 𝒞 ⁡ ( 1, 4)) = log 3 ⁡ ϕ \dim_{H}(\mathcal{C}(1,4))=\log_{3}\phi. One may compare this argument to the proof given in [3, Theorem 5.5]. Let 𝒢 \mathcal{G} be the presentation of 𝒞 ⁡ ( 1, 4) \mathcal{C}(1,4) given by Algorithm A of [3]. The algorithm of Proposition 3.4 applied to k k and 𝒢 \mathcal{G} and Algorithm A of [3] give isomorphic graph presentations of 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}).

(2) In Section 5 below, we will prove Theorem 2.4, which states that

 | dim H ( 𝒞 ⁡ ( 1, Q k)) = log 3 ⁡ ϕ, \dim_{H}(\mathcal{C}(1,Q_{k}))=\log_{3}\phi, |  |

by a similar argument.

## 4. The infinite family P k = 2 ⋅ 3 k + 1 = ( 20 k − 1 ​ 1) 3 P_{k}=2\cdot 3^{k}+1=(20^{k-1}1)_{3}

We obtain a relatively complete description of the path set structure for the family P k = 2 ⋅ 3 k + 1 = ( 20 k − 1 ​ 1) 3 P_{k}=2\cdot 3^{k}+1=(20^{k-1}1)_{3}. As a preliminary we review results for the infinite families L k L_{k} and N k N_{k} studied in part I ( [3, Section 4]).

### 4.1. The Family P k = ( 20 k − 1 ​ 1) 3 = 2 ⋅ 3 k + 1 P_{k}=(20^{k-1}1)_{3}=2\cdot 3^{k}+1: Path set structure.

We study the structure of a path set presentation of the 3 3 -adic expansions of elements in 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}). The following example gives a path set presentation for P 2 = 19 P_{2}=19.

###### Example 4.1.

A path set presentation of the path set X ⁡ ( 1, 19) X(1,19) associated to 𝒞 ⁡ ( 1, 19) \mathcal{C}(1,19), with 19 = ( 201) 3 19=(201)_{3}, is shown in Figure 4.1. The vertex labeled 0 0 is the marked initial vertex.

-100,-165)(100,160) 20pt0 20pt1 n211n20 n201 n221 n1001 n100 n20 n00 n211 n10
FIGURE 4.1. Path set presentation of X ⁡ ( 1, 19) X(1,19). The marked vertex is 0 0.

The graph in Figure 4.1 has adjacency matrix

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎), \bf{A}=\left(\begin{array}[]{cccccccc}1&1&0&0&0&0&0&0\\ 0&0&1&1&0&0&0&0\\ 0&0&0&0&1&0&0&0\\ 0&0&0&0&0&1&0&0\\ 0&0&0&0&1&0&1&0\\ 0&0&0&1&0&0&0&0\\ 0&0&0&0&0&1&0&1\\ 1&0&0&0&0&0&0&0\\ \end{array}\right), |  |

which has Perron eigenvalue β ≈ 1.465571 \beta\approx 1.465571, so

 | dim H ( 𝒞 ⁡ ( 1, 19)) = log 3 ⁡ β ≈ 0.347934. \dim_{H}(\mathcal{C}(1,19))=\log_{3}\beta\approx 0.347934. |  |

An important feature of the graph in Figure 4.1 is that it is reducible with two strongly connected components, one component being the 2 2 nodes in the middle, and the other the ring of 6 6 nodes around the outside. The (oriented) dependency graph of the strongly connected components is a tree with 2 2 nodes. The Perron eigenvalue β \beta of the graph above is associated with the outer strongly connected component with 6 6 nodes. The inner component has topological entropy 0 0.

We describe the path set presentation in general. The vertex labels of the presentation will be described using the following definition.

###### Definition 4.1.

Classify the labels of the vertices in the graph G k G_{k} as numbers m m with 0 ≤ m ≤ 3 k 0\leq m\leq 3^{k} whose finite 3 3 -adic expansions (read right to left) are of types (S1) and (S2) given by:

1. (S1)

The expansion ( X) 3 (X)_{3}, written with exactly k k digits, omits the digit 1 1.

2. (S2)

The 3 3 -adic expansion of m m contains a single digit 1 1, and has the form ( X ​ 10 j) 3 (X10^{j})_{3} for some 0 ≤ j ≤ k 0\leq j\leq k, with ( X ​ 10 j) 3 (X10^{j})_{3} written with exactly k k digits, plus m = 3 k = ( 10 k) 3 m=3^{k}=(10^{k})_{3}.

Note that an (S2) label has initial 3 3 -adic digits consisting of a string of zeros, followed by a 1 1.

###### Proposition 4.2.

For P k = 2 ⋅ 3 k + 1 P_{k}=2\cdot 3^{k}+1 the path set X ⁡ ( 1, P k) X(1,P_{k}) associated to 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) has a presentation ( 𝒢 k, v 0) ({\mathcal{G}}_{k},v_{0}) with the following properties.

(1) The vertices v m v_{m} have labels m m consisting of those 0 ≤ m ≤ 3 k 0\leq m\leq 3^{k} whose 3 3 -adic expansion ( m) 3 (m)_{3} is one of the two types (S1) and (S2) above.

(2) The underlying directed graph G G of 𝒢 k {\mathcal{G}}_{k} has exactly 2 k + 1 2^{k+1} vertices.

(3) The reflection map R ⁡ ( m) = 3 k − m R(m)=3^{k}-m which acts on vertex labels of the underlying directed graph G k G_{k} is an automorphism of G k G_{k}. Given any path from ( 0) 3 (0)_{3} to vertex m m, there is a directed path from vertex ( 10 k) 3 (10^{k})_{3} to vertex 3 k − m 3^{k}-m of the same length, visiting the set of reflected vertices of the original path, and having all the edge labels reversed (exchanging 0 0 and 1 1).

###### Proof.

The presentation found in this theorem will be that given by the construction of Algorithm A in part I [3].

From the proof of Theorem 9.1 we know that a vertex with label m = 3 k m=3^{k} is reachable by a directed path from vertex m = 0 m=0 and vice-versa.

We prove the proposition by showing, in order:

1. (G1)

The vertices of G G reachable from v 0 v_{0} have labels 0 ≤ m ≤ 3 k 0\leq m\leq 3^{k} which are a subset of the labels (S1) and (S2).

2. (G2)

The set of vertex labels m m satisfying (S1) or (S2) are exchanged under the reflection map R ⁡ ( m) = 3 k − m R(m)=3^{k}-m. The set of all possible m m satisfying (S1), respectively (S2), each have cardinality 2 k 2^{k}.

3. (G3)

Each path emanating from vertex m = 0 m=0 corresponds to a unique path emanating from vertex m = 3 k m=3^{k} with the new path having reflected vertex labels and reversed edge labels, and vice versa.

4. (G4)

The set of all reachable vertices is invariant under the reflection map.

5. (G5)

All vertices with labels of type (S1) are reachable.

6. (G6)

The reflection map on vertices induces a graph automorphism of G G of order 2 2 with no fixed points. Thus G G is a double cover of the resulting quotient graph H H.

To establish (G1) we proceed by induction on the length n n of a shortest path to a given vertex. The base case m = 0 m=0 is an (S1) label. Following a single 0 0 edge changes a vertex label ( X ​ s) 3 (Xs)_{3} (with s = 0, 1, s=0,1,) to ( 0 ​ X) 3 (0X)_{3}, which maps (S1) labels to (S1) labels and maps (S2) labels to (S2) labels, except the case d = 1 d=1 is mapped to an (S1) label. Following a single 1 1 edge with vertex label ( X ​ s) 3 (Xs)_{3} (here s = 0, 2 s=0,2) maps labels having s = 0 s=0 to ( 2 ​ X) 3 (2X)_{3}, which preserves the property of being an (S1) label or an (S2) label. For the case s = 2 s=2, which must be an (S1) label, rewrite ( X ​ s) 3 = ( Y ​ 02 j) 3 (Xs)_{3}=(Y02^{j})_{3} for some j ≥ 1 j\geq 1, which is converted to ( 2 ​ Y ​ 10 j − 1) 3 (2Y10^{j-1})_{3}, which is an (S2) label. The extreme case ( X ​ s) = ( 2 k) 2 (Xs)=(2^{k})_{2} is converted to m = 3 k m=3^{k}, in (S2). This completes the induction step.

(G2) There are clearly 2 k 2^{k} elements in (S1). The reflection map R R acts on elements m m of (S1) with m > 0 m>0 by replacing each 0 0 by 2 2 and vice versa, except that the smallest 2 2 is converted to a 1 1, and this is an element of (S2). The remaining element m = 0 m=0 exchanges with m = 3 k m=3^{k} which is in (S2). Conversely elements of (S2) are mapped into elements of (S1), for m < 3 k m<3^{k} an expression 10 j 10^{j} is converted to 02 j 02^{j}, and for m = 3 k m=3^{k} is sent to m = 0 m=0. Since the reflection map is an involution, it is one to one, so the (S2) labels have the same cardinality 2 k 2^{k} as (S1) labels.

(G3) This assertion is proved by induction on the length of the path. It is vacuously true at step 0 0. For the induction step we must check that the vertices m m and 2 k − m 2^{k}-m have the same number of exit edges, and that the available exit edges have reversed labels in the second case. We must also check that following an edge in the two cases leads to a pair of reflected vertex labels m ′ m^{\prime} and 3 k − m ′ 3^{k}-m^{\prime}. There are several cases.

1. Case (1)

If m = ( X ​ 20 ℓ) 3 m=(X20^{\ell})_{3} for ℓ > 0 \ell>0 of type (S1), then 3 k − m = ( X ¯ ​ 10 ℓ) 3 3^{k}-m=(\bar{X}10^{\ell})_{3} is of type (S2). Both allow 0 0, 1 1 exit edges. A 0 0 exit edge from m m goes to m ′ = ( 0 ​ X ​ 02 ℓ − 1) 3 m^{\prime}=(0X02^{\ell-1})_{3}, and a 1 1 exit edge for 3 k − m 3^{k}-m goes to ( 2 ​ X ¯ ​ 10 ℓ − 1) 3 = 3 k − m ′ (2\bar{X}10^{\ell-1})_{3}=3^{k}-m^{\prime}. A 1 1 exit edge from m m goes to m ′′ = ( 2 ​ X ​ 20 ℓ − 1) 3 m^{\prime\prime}=(2X20^{\ell-1})_{3}, and a 0 0 exit edge for 3 k − m 3^{k}-m goes to ( 0 ​ X ¯ ​ 10 ℓ − 1) = 3 k − m ′′ (0\bar{X}10^{\ell-1})=3^{k}-m^{\prime\prime}.

2. Case (2)

If m = ( X ​ 02 ℓ) 3 m=(X02^{\ell})_{3} for ℓ > 0 \ell>0 of type (S1), then 3 k − m = ( X ¯ ​ 20 ℓ − 1 ​ 1) 3 3^{k}-m=(\bar{X}20^{\ell-1}1)_{3} is of type (S2). Here m m allows only a 1 1 exit edge, while 3 k − m 3^{k}-m allows only a 0 0 exit edge. Under the allowed 1 1 exit edge m m goes to m ′ = ( 2 ​ X ​ 10 ℓ − 1) 3 m^{\prime}=(2X10^{\ell-1})_{3} of type (S2). Under the allowed 0 0 exit edge 3 k − m 3^{k}-m goes to ( 0 ​ X ¯ ​ 20 ℓ − 1) 3 = 3 k − m ′ (0\bar{X}20^{\ell-1})_{3}=3^{k}-m^{\prime} of type (S1).

For the two further cases where m m is of type (S2), reverse the above. This completes the induction step.

(G4) By (G3) if a vertex labeled m m is reachable from ( 0) 3 (0)_{3}, then its reflected vertex 3 k − m 3^{k}-m is reachable from vertex 3 k 3^{k}. But vertex 3 k 3^{k} is reachable from ( 0) 3 (0)_{3} so 3 k − m 3^{k}-m is reachable from ( 0) 3 (0)_{3} as well.

(G5) We may assume that the (S1) vertex m ≠ 0 m\neq 0, so it has the form 0 r 0 2 r 1 0 r 2 ⋯ 2 r j 0^{r_{0}}2^{r_{1}}0^{r_{2}}\cdots 2^{r_{j}}, in which all r i > 0 r_{i}>0 except possibly r 0 r_{0} and r j r_{j}, and r 0 + r 1 + ⋯ + r j = k r_{0}+r_{1}+\cdots+r_{j}=k. Now it may be realized following a directed path from ( 0) 3 (0)_{3} having successive edge labels 1 r j, 0 r j − 1, 1 r j − 2, ⋯, 0 r 0 1^{r_{j}},0^{r_{j-1}},1^{r_{j-2}},\cdots,0^{r_{0}}. This path is legal, because all intermediate words in the path have initial 3 3 -adic digit 0 0 so both edges labeled 0 0 and 1 1 exit from that vertex. (The intial word has k k initial zeros, and each step can decrement the number of leading zeros by at most 1 1).

(G6) One first checks that each label m m in (S1) ending in 0 0 corresponds under reflection to a label 3 k − m 3^{k}-m in (S2) ending in 0 0 and vice versa (since 3 3 divides m m). Each label in (S1) ending in 2 2 corresponds under reflection to a label in (S2) ending in 1 1; the (S1) label permits only a single exit edge with label 1 1 and the corresponding (S2) label has a single exit edge labeled 0 0. Thus at each vertex the reflection automorphism (at the level of vertex labels) preserves the number of edges and reverses their edge labels. This establishes (G6). Moreover the graph G is a double cover of the quotient graph H H under the automorphism R R (which has no fixed points). ∎

Our next object is to show that the underlying graph G k G_{k} of the path set X ⁡ ( 1, N k) X(1,N_{k}) has at least ⌈ k + 1 2 ⌉ \lceil\frac{k+1}{2}\rceil nested connected components, a number which is unbounded as k → ∞ k\to\infty. We establish this using the following notion of depth to vertices of G k G_{k}.

###### Definition 4.3.

(1) First we classify the labels of the vertices in graph G k G_{k} as being of types (T1) and (T2) as follows:

1. (T1)

The k k -th 3 3 -adic digit of m m is 0 0 or 1 1, so m = ( 0 ​ X) 3 m=(0X)_{3} or m = ( 1 ​ X) 3 m=(1X)_{3}, with X X containing k − 1 k-1 digits, but excluding the label m = 3 k = ( 10 k) 3 m=3^{k}=(10^{k})_{3}.

2. (T2)

The k k -th 3 3 -adic digit of m m is 2 2, i.e. m = ( 2 ​ X) 3 m=(2X)_{3}, as above, in addition including the label m = 3 k = ( 10 k) 3 m=3^{k}=(10^{k})_{3}.

One may check that there are 2 k 2^{k} elements in each set, and that the reflection operation R ⁡ ( m) = 3 k − m R(m)=3^{k}-m sends (T2) labels to (T1) labels and vice versa.

(2) The depth of a (T1) label is the number of blocks of consecutive 2 2 ’s appearing in its 3 3 -adic expansion. The depth of a (T2) label m m is the depth of its reflected label R ⁡ ( m) R(m), which is of type (T1).

Thus m = 0 m=0 and m = 3 k m=3^{k} are assigned depth 0 0. Furthermore all the vertices in the path of length 2 ​ k + 2 2k+2 studied in the proof of Theorem 9.1 are assigned depth 0 0, and they are the complete set of depth 0 0 vertices.

The following proposition will establish that this notion of depth stratifies the strongly connected components, by showing depth is nondecreasing along each directed edge.

###### Proposition 4.4.

For P k = 2 ⋅ 3 k + 1 P_{k}=2\cdot 3^{k}+1 the path set X ⁡ ( 1, P k) X(1,P_{k}) has presentation ( 𝒢 k, v 0) ({\mathcal{G}}_{k},v_{0}) with the following properties.

(1) Each step along an edge in the graph G k G_{k} leaves the same or increases the depth of a vertex.

(2) For 0 ≤ j ≤ ⌊ k / 2 ⌋ 0\leq j\leq\lfloor k/2\rfloor there are exactly 2 ​ ( k + 1 2 ​ j + 1) 2{{k+1}\choose{2j+1}} vertices in 𝒢 k {\mathcal{G}}_{k} of depth exactly j j.

(3) For each 0 ≤ j ≤ ⌊ k 2 ⌋ 0\leq j\leq\lfloor\frac{k}{2}\rfloor, the vertices of depth j j form a strongly connected component of the underlying directed graph G k G_{k}. Thus, G k G_{k} has a sequence of 1 + ⌊ k / 2 ⌋ 1+\lfloor k/2\rfloor strongly connected components, which are nested in a chain.

###### Proof.

The presentation found in this theorem will be that given by the construction of Algorithm A in part I [3]. Some of the notation below only makes sense for k > 3 k>3. We will restrict to these cases, as the result follows for k = 1, 2, 3 k=1,2,3 by direct inspection. The reversal operation exchanges type (T1) and type (T2) labels. For this to work the top 3 3 -adic digit (the k k -th digit) must be used, because this is the only digit always reversed under the reflection map or with 2 2 changed to 1 1; there is one exception, which is m = 0 m=0 and m = 3 k m=3^{k}, where we assigned them to (T1) and (T2) directly. The key point is: a label m m and its reversal are always at the same level. For the two exceptions m = 0 m=0 and m = 3 k m=3^{k} this fact had to be checked directly.

(1) It suffices to check the effect of traversing a single edge in 𝒢 k {\mathcal{G}}_{k}. The assertion holds for cases m = 0 m=0 and m = 3 k m=3^{k} because they both exit to level 0 0 vertices. By the proof of (G3) in Proposition 4.2, if label m m goes to m ′ m^{\prime} by edge labeled s s, then 3 k − m 3^{k}-m goes to 3 k − m ′ 3^{k}-m^{\prime} by an edge labeled s ¯ \bar{s}. Now the depths of m m and 3 k − m 3^{k}-m are the same, as are those of m ′ m^{\prime} and 3 k − m ′ 3^{k}-m^{\prime}, so it suffices to check the effect of following an edge from a vertex of type (T1). We treat cases.

1. (i)

Suppose m = ( 0 ​ X ​ 0) 3 m=(0X0)_{3} of type (T1) has depth d d, thus X X contains d d blocks of consecutive 2 2 ’s. Following a 0 0 edge goes to m ′ = ( 00 ​ X) 3 m^{\prime}=(00X)_{3}, also (T1) of depth d d.

2. (ii)

Suppose m = ( 0 ​ X ​ 0) 3 m=(0X0)_{3} of type (T1) has depth d d, thus it has d d blocks of consecutive 2 2 ’s. Following a 1 1 edge goes to m ′ = ( 20 ​ X) 3 m^{\prime}=(20X)_{3}, now (T2), of depth same as 3 k − m ′ 3^{k}-m^{\prime}. Now X = X ′ ​ 20 ℓ X=X^{\prime}20^{\ell} with ℓ ≥ 0 \ell\geq 0 or X = 0 ℓ X=0^{\ell}. In the first case 3 k − m ′ = ( 02 ​ X ′ ¯ ​ 10 ℓ) 3 3^{k}-m^{\prime}=(02\bar{X^{\prime}}10^{\ell})_{3} If X ′ = 0 ​ X ′′ ​ 0 X^{\prime}=0X^{\prime\prime}0, then it has d − 1 d-1 blocks of 2 ′ ​ s 2^{\prime}s, but its reversal X ¯ \bar{X} has d d blocks. If X ′ = 2 ​ X ′′ ​ 0 X^{\prime}=2X^{\prime\prime}0 then it has d − 1 d-1 blocks of 2 ′ ​ s 2^{\prime}s, as does its reversal, but the 02 02 at front creates another block. If X ′ = 0 ​ X ′ ​ 2 X^{\prime}=0X^{\prime}2 then it has d d blocks of 2 2 ’s, as does its reversal. Finally if X ′ = 2 ​ X ′ ​ 2 X^{\prime}=2X^{\prime}2 then it has d d blocks of 2 2 ’s, its reversal has d − 1 d-1 blocks, but the 02 02 at front creats another blocks. In all cases the depth cannot decrease.

3. (iii)

Suppose m = ( 0 ​ X ​ 02 ℓ) 3 m=(0X02^{\ell})_{3} with ℓ > 0 \ell>0 of type (T1) has depth d d. Now can only follow a 1 1 edge, go to m ′ = ( 20 ​ X ​ 10 ℓ − 1) 3 m^{\prime}=(20X10^{\ell-1})_{3} is of type (T2). This has same depth as 3 k − m ′ = ( 02 ​ X ¯ ​ 20 ℓ − 1) 3 3^{k}-m^{\prime}=(02\bar{X}20^{\ell-1})_{3}. Now X X has d − 1 d-1 blocks of 2 2 ’s. If it is of form 0 ​ X ′′ ​ 0 0X^{\prime\prime}0 then reversal increases number of blocks of 2 2 ’s in it by 1 1, compensating exactly for the lost 2 2 block at the right end of the label, so the depth is still d d. If of form 2 ​ X ′′ ​ 0 2X^{\prime\prime}0 or 0 ​ X ′′ ​ 2 0X^{\prime\prime}2 then reversal leaves d − 1 d-1 blocks of 2 2 ’s but get one extra block from either 2 2 before or after, so the depth is still d d. If of form 2 ​ X ′′ ​ 2 2X^{\prime\prime}2 then reversal leaves d − 2 d-2 blocks of 2 2 ’s but now gain two extra blocks from the 2 2 before and after, so the depth is still d d.

In all cases of a type (T1) vertex a step leaves depth the same or increases it by 1 1.

(2) Let k k be fixed. The result is true for j = 0 j=0 by the construction in Theorem 9.1, where there are 2 ​ k + 2 = 2 ​ ( k + 1 1) 2k+2=2{{k+1}\choose{1}} vertices of depth 0 0, and this component is strongly connected.

For j ≥ 1 j\geq 1 it suffices to count the number of labels of type (T1) at depth j j and then double it. For j ≥ 1 j\geq 1 the number of labels of type ( T ​ 1) (T1) at depth j j consist of all labels of form ( 0 k 1 2 ℓ 1 0 k 2 2 ℓ 2 ⋯ 0 k j 2 ℓ j 0 k j + 1 X) 3 (0^{k_{1}}2^{\ell_{1}}0^{k_{2}}2^{\ell_{2}}\cdots 0^{k_{j}}2^{\ell_{j}}0^{k_{j+1}}X)_{3} with final block X = ∅ X=\emptyset (set k j + 2 = 0 k_{j+2}=0) or X = ( 10 k j + 2 − 1) X=(10^{k_{j+2}-1}) (the latter requires k j + 2 ≥ 1 k_{j+2}\geq 1). Since labels have length k k the exponents necessarily satisfy

 | k 1 + ⋯ + k j + 1 + k j + 2 + ℓ 1 + ⋯ + ℓ j = k, k i, ℓ i > 0 ​ for ​ 1 ≤ i ≤ j; k j + 1, k j + 2 ≥ 0. k_{1}+\cdots+k_{j+1}+k_{j+2}+\ell_{1}+\cdots+\ell_{j}=k,~~\,k_{i},\ell_{i}>0\,\mbox{for}\,1\leq i\leq j;k_{j+1},k_{j+2}\geq 0. |  |

There are ( k 2 ​ j) {{k}\choose{2j}} solutions of depth j j type ( T ​ 1) (T1) with X X not containing a 1 1; this follows since there are k k symblols in a label and we mark the final elements of each 0 k i 0^{k_{i}} and 2 k i 2^{k_{i}} with an asterisk for 1 ≤ i ≤ j 1\leq i\leq j to uniquely determine a depth j j label with X = ∅ X=\emptyset. There are ( k 2 ​ j + 1) {{k}\choose{2j+1}} solutions of depth j j type ( T ​ 1) (T1) with X X containing a 1 1; here we add an additional asterisk marking the 1 1, which unqiuely specifies the label, so we have the number of ways of inserting 2 ​ j + 1 2j+1 asterisks. Thus the number of ( T ​ 1) (T1) labels of depth j j is ( k + 1 2 ​ j + 1) {{k+1}\choose{2j+1}}, and (2) follows.

(3) First, we show that it is possible to reach a vertex of each depth 0 ≤ j ≤ ⌊ k / 2 ⌋ 0\leq j\leq\lfloor k/2\rfloor. Starting from m = 0 m=0 following paths with labels ( 10) j (10)^{j} for 1 ≤ j ≤ ⌊ k / 2 ⌋ 1\leq j\leq\lfloor k/2\rfloor, one arrives at vertices m 2 ​ j:= ( ( 02) j ​ 0 k − 2 ​ j) 3 m_{2j}:=((02)^{j}0^{k-2j})_{3}, and m 2 ​ j m_{2j} is a type (T1) label of depth j j. These are legal paths since all the intermediate vertex m j m_{j} labels (for 1 ≤ j ≤ m − 1 1\leq j\leq m-1) have initial 3 3 -adic digit 0 0. We have produced a path with vertices of depth 0, 1, 2, …, ⌊ k / 2 ⌋ 0,1,2,...,\lfloor k/2\rfloor, which guarantees the existence of at least one sequence of distinct strongly connected components of length 1 + ⌊ k / 2 ⌋ 1+\lfloor k/2\rfloor which are nested in a chain.

Next, we show that the subgraph of G k G_{k} consisting of those vertices of depth j j is strongly connected for each 0 ≤ j ≤ ⌊ k / 2 ⌋ 0\leq j\leq\lfloor k/2\rfloor. At depth d = 0 d=0, beginning at the vertext labeled 0 0 and traversing a path with label 1 k + 1 ​ 0 k + 1 1^{k+1}0^{k+1} gives a loop at the 0 0 -vertex that passes through each other vertex of depth 0 0, so the subgraph of depth 0 0 vertices is strongly connected.. Below, we restrict attention to depths d ≥ 1 d\geq 1, and some statements below only apply in those cases. Recall also that we are restricting attention to k > 3 k>3, as smaller cases can be checked by hand.

We need to show, firstly, that from any vertex it is always possible to traverse an edge that leaves the depth unchanged. By the proof of (G3) in Proposition 4.2 and the discussion in the first paragraph of (1) above, it suffices to verify this for vertices of type (T1). Let m m be the label of a vertex of depth d d and type (T1). Then either m = ( 0 ​ X ​ 0) 3 m=(0X0)_{3}, in which case we may follow an edge labeled 0 0 to arrive at a vertex labeled ( 00 ​ X) 3 (00X)_{3} that also has depth d d, or else m = ( 0 ​ X ​ 02 l) 3 m=(0X02^{l})_{3} for some l > 0 l>0. In the latter case, we may follow an edge labeled 1 1 to a vertex labeled ( 20 ​ X ​ 10 l − 1) 3 (20X10^{l-1})_{3}, and the discussion in (iii) above shows that this vertex also has depth d d. In any case, we can always traverse an edge that will leave the depth unchanged.

Among depth d d labels, the minimal such label is m m ​ i ​ n = ( ( 20) d − 1 ​ 2) 3 m_{min}=((20)^{d-1}2)_{3}. In order to show that the set of depth d d vertices is a strongly connected subgraph of 𝒢 k \mathcal{G}_{k}, it suffices to show that it is always possible, beginning at any vertex of depth d d, to traverse paths both *forwards*to m m ​ i ​ n m_{min} and *backwards*to the same vertex (that is, contrary to the ordinary direction that arrows are traversed; this will show that there is a path forwards from m m ​ i ​ n m_{min} to the desired vertex). This will follow if we can show that:

1. (A)

For any depth d d vertex with non-minimal label m m, it is always possible to follow a path, staying at depth d d, to another vertex with label m ′ < m m^{\prime}<m.

2. (B)

For any depth d d vertex, it is possible to follow edges b ​ a ​ c ​ k ​ w ​ a ​ r ​ d ​ s backwards until we reach a vertex where each block of 2 2 ’s has length exactly 1 1.

3. (C)

For any depth d d vertex with a label where each block of 2 2 ’s has length exactly 1 1, it is possible to reach m m ​ i ​ n m_{min} by going backwards.

(A) Suppose now we are at a depth d d vertex with label m m of type (T1). Then either m m is of the form ( 0 ​ X ​ 0) 3 (0X0)_{3}, or else m m is of the form ( 0 ​ X ​ 02 l) 3 (0X02^{l})_{3} for some l > 0 l>0. If m = ( 0 ​ X ​ 0) 3 m=(0X0)_{3}, then we may traverse an edge labeled 0 0 to arrive at an edge labeled m ′ = ( 0 ​ X) 3 < m m^{\prime}=(0X)_{3}<m, and m ′ m^{\prime} is also at depth d d. Now suppose instead that m = ( 0 ​ X ​ 02 l) 3 m=(0X02^{l})_{3}. Then we must traverse next an edge labeled 1 1 to the vertex with label m ′ = ( 20 ​ X ​ 10 l − 1) 3 > m m^{\prime}=(20X10^{l-1})_{3}>m. By the argument of (iii) above, this vertex also has depth d d. From here, we may traverse l l consecutive edges labeled 0 0 to arrive at a vertex labeled m ′′ = ( 20 ​ X) 3 m^{\prime\prime}=(20X)_{3}, whose depth is also d d. If the right-most digit of X X is not a 2 2, we may continue to traverse edges labeled 0 0 until we arrive at a vertex m ′′′ = ( 20 ​ Y) 3 m^{\prime\prime\prime}=(20Y)_{3} where the right-most digit of Y Y is a 2 2, and the length | Y | ≤ | X | |Y|\leq|X|, or else at the vertex m ( 4) = ( 2) 3 m^{(4)}=(2)_{3} if X X is the empty string. In the latter case, we are at depth d = 1 d=1 and m ( 4) = ( 2) 3 = m m ​ i ​ n m^{(4)}=(2)_{3}=m_{min} is already the minimal label. Suppose we are in the former case, and we have arrived at m ′′′ = ( 20 ​ Y) 3 m^{\prime\prime\prime}=(20Y)_{3}. But for any l ≥ 1 l\geq 1, we necessarily have m ′′′ = ( 20 ​ Y) 3 ≤ ( X ​ 02 l) 3 = m m^{\prime\prime\prime}=(20Y)_{3}\leq(X02^{l})_{3}=m, with equality if and only if X = Y X=Y, l = 1 l=1, and m = m ′ = ( 20) d − 1 ​ 2 = m m ​ i ​ n m=m^{\prime}=(20)^{d-1}2=m_{min}. Thus, in any case, we may always traverse a path, remaining at depth d d, to arrive at a vertex whose label is less than m m.

What if our initial vertex is of type (T2)? Then, m m is either of the form 10 k 10^{k}, in which case, we simply follow edges labeled 1 1 until we reach the vertex labeled 0 0, or we have something of the form 2 ​ X 2X, where X X has k − 1 k-1 digits. In this case, if X X terminates in 10 l 10^{l}, we can immediately follow a vertex 0 0, without dropping depths, to m ′ m^{\prime} of form ( T ​ 1) (T1), where of course m ′ < m m^{\prime}<m. Otherwise, we have 2 ​ Y ​ 20 l 2Y20^{l}, where we follow l + 1 l+1 edges of label 1 1; the first l l bring us to 2 ​ Z ​ 2 2Z2, and the ( l + 1) (l+1) st edge takes us to a (T2) vertex that terminates in 10 n 10^{n}, which is a case already covered.

This proves (A).

To see (B), we will devise an algorithm (call it Algorithm (B)).

1. (i)

If we are at 2 ​ X ​ 10 l 2X10^{l} then we follow a vertex labeled 1 backwards to vertex X ​ 02 l + 1 X02^{l+1}. (This does not drop depth, as a block of consecutive 2 2 ’s necessarily transforms into another block of consecutive 2 2 ’s).

2. (ii)

If we are at 0 l ​ X 0^{l}X, where l > 1 l>1, or we are at 0 l ​ Y ​ 10 n 0^{l}Y10^{n}, where l > 0 l>0, we follow a vertex labelled 0 0 to 0 l − 1 ​ X 0^{l-1}X or 0 l − 1 ​ Y ​ 10 n + 1 0^{l-1}Y10^{n+1}.

3. (iii)

If we are at 02 ​ X 02X, and X X omits the digit 1 1, we follow an edge labeled 0 0 back to 2 ​ X ​ 1 2X1. Notice that this avoids dropping depth.

4. (iv)

If we are 2 ​ X 2X, where X X omits the digit 1 1, we follow an edge labeled 1 1 back to X ​ 0 X0.

The crux is step (iii); following the notation of that step, we will then be at 2 ​ X ​ 1 2X1, with no 0 0 s after the 1 1. We then apply case (i), reaching X ​ 02 X02. Any other 2 2 ’s that appeared in the block at the far left will be transformed into 0 0 ’s on the far right by the application of step ( i ​ v) (iv), while the other blocks will merely be shifted.

Thereby, by repeated application of this algorithm, all of the blocks will be transformed into single-digit blocks after at most k k iterations. This concludes (B). For an illustration at depth 2, see the column labeled “Step (B)" in Table 4.1.

Finally, for (C), notice that, for the type of vertex we are interested in, repeated application of Algorithm (B) simply "scrolls through" the label, with the blocks of 2 2 ’s shifting left, always preserving the same cyclic order, with the same gaps of 0 0 ’s between them (unless a 1 1 is present) between them. In the case of the illustration of Table 4.1, see the column labeled “Step (C)-1" of that table.

So, for (C), apply Algorithm (B) until we are at 0 l ​ X ​ 2 0^{l}X2 where l > 1 l>1 (if this is strictly impossible, then simply "scroll" until we are at ( 02) k / 2 (02)^{k/2}, and at this depth, that is the minimal vertex). Then, break the pattern and go to 0 l ​ X ​ 21 0^{l}X21. Then, continue to apply Algorithm (B) until we return to a vertex where all of the blocks of 2 2 ’s have length 1 1.

Essentially, we will generate a long block of 2 2 ’s instead of the block of 0 0 ’s we currently have, which won’t have such a large gap; see the column labeled “Step (C)-2" in Table 4.1.

One such procedure transforms a block of 0 0 ’s of arbitrary length into a block of length 1 1.

Repeat this procedure untill all of the blocks of 0 0 ’s (except for 1) have length 1 1, and then use Algorithm (B) until we reach the minimal vertex. This completes (3). Continuing with our simple example, see the column labeled “Step (C)-3" in Table 4.1.

Step (B) | Step (C)-1 | Step (C)-2 | Step (C)-3 |

22022022 | 0020002 | 0020002 | 0002020 |

20220220 | 0200020 | 0200021 | 0020200 |

02202200 | 2000201 | 2000210 | 0202000 |

22002201 | 0002002 | 0002022 | 2020001 |

20022002 | 0020020 | 0020220 | 0200002 |

00220020 | 0200200 | 0202200 | 2000021 |

02200200 | 2002001 | 2022001 | 0000202 |

22002001 | 0020002 | 0220002 |  |

20020002 |  | 2200021 |  |

00200020 |  | 2000202 |  |

 |  | 0002020 |  |

TABLE 4.1. Example of algorithm for proof of Proposition 4.3(3).

∎

###### Remark 4.5.

(1) Proposition 4.4 counts the number of vertices at each depth, giving a recursion to compute them. Table 4.2 below gives values for 1 ≤ k ≤ 9 1\leq k\leq 9.

 | Depth= | 0 0 | 1 1 | 2 2 | 3 3 | 4 4 |

P 1 = 7 P_{1}=7 |  | 4 4 |  |  |  |  |

P 2 = 19 P_{2}=19 |  | 6 6 | 2 2 |  |  |  |

P 3 = 55 P_{3}=55 |  | 8 8 | 8 8 |  |  |  |

P 4 = 163 P_{4}=163 |  | 10 10 | 20 20 | 2 2 |  |  |

P 5 = 487 P_{5}=487 |  | 12 12 | 40 40 | 12 12 |  |  |

P 6 = 1459 P_{6}=1459 |  | 14 14 | 70 70 | 42 42 | 2 2 |  |

P 7 = 4375 P_{7}=4375 |  | 16 16 | 112 112 | 112 112 | 16 16 |  |

P 8 = 13123 P_{8}=13123 |  | 18 18 | 168 168 | 252 252 | 72 72 | 2 2 |

P 9 = 39367 P_{9}=39367 |  | 20 20 | 240 240 | 504 504 | 240 240 | 20 20 |

TABLE 4.2. Number of vertices at given depth in graph 𝒢 k {\mathcal{G}}_{k} for X ⁡ ( 1, P k) X(1,P_{k}).

(2) Proposition 4.4 says that the graph X ⁡ ( 1, P k) X(1,P_{k}) has a “Matryoshka doll" structure of a single set of nested strongly connected components, one at each depth 0 ≤ j ≤ ⌊ k / 2 ⌋ 0\leq j\leq\lfloor k/2\rfloor.

(3) The proof of Proposition 4.4 exploits repeatedly the symmetry of the graph G k G_{k} exhibited by the partitioning of vertices into types (T1) and (T2).

### 4.2. The Family P k = ( 20 k − 1 ​ 1) 3 = 2 ⋅ 3 k + 1 P_{k}=(20^{k-1}1)_{3}=2\cdot 3^{k}+1: Hausdorff dimension.

Data on the Hausdorff dimensions of the first few of the sets 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) were obtained by computer calculation of the maximum eigenvalue of the adjacency matrix of the graph X ⁡ ( 1, P k) X(1,P_{k}) and presented in Section 3.1. The data contained oscillations and other features which we discuss in Remark 4.6 below.

We now lower bound the Hausdorff dimension of 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) as k → ∞ k\to\infty. Theorem 2.2 gives both an asymptotic limiting result and a lower bound because it may be that the Hausdorff dimensions continue to oscillate for large k k.

###### Proof of Theorem 2.2.

Let a = ⌊ k 4 ⌋ a=\lfloor\frac{k}{4}\rfloor and let b ∈ { 0, 1, 2, 3 } b\in\{0,1,2,3\} be congruent to k k mod 4 4, so that k = 4 ​ a + b k=4a+b. Let S ⊂ 𝒜 ℕ = { 0, 1, 2 } ℕ S\subset\mathcal{A}^{\mathbb{N}}=\{0,1,2\}^{\mathbb{N}} be given by

 | S = { ( 1100) a ​ 0 b ​ ( ( 1 ​ x ​ 00) a ​ 0 b ​ ( 1000) a − 1 ​ 1000 b) ∞ ∈ 𝒜 ℕ | x ∈ { 0, 1 } ​ may vary }. S=\{(1100)^{a}0^{b}((1x00)^{a}0^{b}(1000)^{a-1}1000^{b})^{\infty}\in\mathcal{A}^{\mathbb{N}}|x\in\{0,1\}\text{ may vary}\}. |  | (4.1) |

What we will show is that S ⊂ X ⁡ ( 1, P k) S\subset X(1,P_{k}). Since elements of S S, after the fixed initial string ( 1100) a ​ 0 b (1100)^{a}0^{b}, consists of symbol sequences of length 2 ​ k − 1 2k-1 with 2 ​ k − 1 − a 2k-1-a fixed digits and a a digits which may be either 0 0 or 1 1, it follows that

 | H t ​ o ​ p ​ ( S) = a 2 ​ k − 1 ​ log 3 ⁡ ( 2) = ⌊ k 4 ⌋ 2 ​ k − 1 ​ log 3 ⁡ ( 2). H_{top}(S)=\frac{a}{2k-1}\log_{3}(2)=\frac{\lfloor\frac{k}{4}\rfloor}{2k-1}\log_{3}(2). |  |

The two inequalities of the theorem, that

 | lim inf k → ∞ dim H 𝒞 ⁡ ( 1, P k) ≥ 1 8 ​ log 3 ⁡ ( 2), \liminf_{k\to\infty}\dim_{H}\mathcal{C}(1,P_{k})\geq\frac{1}{8}\log_{3}(2), |  |

and, for all k k,

 | dim H ( 𝒞 ⁡ ( 1, P k)) ≥ 1 13 ​ log 3 ⁡ ( 2), \dim_{H}(\mathcal{C}(1,P_{k}))\geq\frac{1}{13}\log_{3}(2), |  |

then will follow immediately.

To prove that S ⊂ X ⁡ ( 1, P k) S\subset X(1,P_{k}), we will trace out paths on the graph presentation of 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) given by Algorithm A of [3] whose edge labels give the elements of S S. First, note that if we begin with an edge labeled 1 1 from the 0 0 -vertex, we arrive at the vertex with label 20 k − 1 20^{k-1}. This means that our next k − 1 k-1 vertices may be either 0 0 or 1 1 freely. Each edge 0 0 appends a 0 0 to the front of the vertex label and removes the last digit, and each edge 1 1 appends a 2 2 to the front of the vertex label and removes the last digit. From these observations, we see that there is in fact a sequence of edges with label ( 1100) a ​ 0 b (1100)^{a}0^{b}, and having traversed these edges we arrive at a vertex labeled 0 b ​ ( 0022) a 0^{b}(0022)^{a}. Call this vertex v v.

We will now show that we may traverse a sequence of edges with label
( 1 ​ x ​ 00) a ​ 0 b ​ ( 1000) a − 1 ​ 1000 b (1x00)^{a}0^{b}(1000)^{a-1}1000^{b} initiating at v v for x = 0 x=0 and x = 1 x=1, and that such a path also terminates at v v. The result will follow. Now since the label of v v ends in 2 2, the only out edge is indeed labeled 1 1, and this takes us to a vertex labeled 20 b ​ ( 0022) a − 1 ​ 010 20^{b}(0022)^{a-1}010. The next edge label x x may then be either 0 0 of 1 1, terminating in a vertex labeled [2 ​ x] ​ 20 b ​ ( 0022) a − 1 ​ 01 [2x]20^{b}(0022)^{a-1}01, where [2 ​ x] [2x] is a digit given by the product of 2 2 and x x. From this vertex we may traverse two subsequent edges each labeled 0 0, and the target vertex is 00 ​ [2 ​ x] ​ 20 b ​ ( 0022) a − 1 00[2x]20^{b}(0022)^{a-1}. It is easy to see that we may repeat this process, traversing edges labeled ( 1 ​ x ​ 00) (1x00) a a times and ultimately terminating at a vertex labeled ( 00 ​ [2 ​ x] ​ 2) a ​ 0 b (00[2x]2)^{a}0^{b}. Traversing then b b edges labeled 0 0 gets us to the vertex labeled 0 b ​ ( 00 ​ [2 ​ x] ​ 2) a 0^{b}(00[2x]2)^{a}. We may then traverse edges labeled ( 1000) a − 1 ​ 1000 b (1000)^{a-1}1000^{b} to arrive back at the vertex v v labeled 0 b ​ ( 0022) a 0^{b}(0022)^{a}. This completes the proof. ∎

###### Remark 4.6.

We speculate on the behavior of the Hausdorff dimension function 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) as a function of k k. We believe the following might be true.

1. (1)

Fixing level j j and varying k k the topological entropy of the strongly connected component at depth j j stay at value 0 0 until k ≥ 2 ​ j − 2 k\geq 2j-2, then increas monotonically to a maximum and then decrease monotonically thereafter.

2. (2)

The “champion" depth j j with maximal topological entropy is a nondecreasing function of k k.

Speculations (1) and (2) are suggested by analogy with the behavior of the number of vertices at depth j j as a function of k k, given in Table 4.1, which have both these properties.

### 4.3. Hausdorff dimension bounds for 𝒞 ⁡ ( 1, P k 1, …, P k n) \mathcal{C}(1,P_{k_{1}},...,P_{k_{n}})

The path set structures of the members of the infinite family P k P_{k} are compatible with each other, as a function of k k, so that the associated 𝒞 ⁡ ( 1, P k 1, …, P k n) \mathcal{C}(1,P_{k_{1}},...,P_{k_{n}}) all have positive Hausdorff dimension. We relate these Hausdorff dimensions to those of the infinite family L k = ( 1 k) 3 = 1 2 ​ ( 3 k + 1 − 1) L_{k}=(1^{k})_{3}=\frac{1}{2}(3^{k+1}-1) treated by the first and third authors in [3] and reviewed in Appendix A (Section 8).

###### Theorem 4.7.

For the family P k = 2 ⋅ 3 k + 1 = ( 20 k − 1 ​ 1) 3 P_{k}=2\cdot 3^{k}+1=(20^{k-1}1)_{3}, and 0 ≤ k 1 < … < k n 0\leq k_{1}<\ldots<k_{n}, the graph 𝒢 \mathcal{G} presenting the path set X ⁡ ( 1, P k 1, …, P k n) X(1,P_{k_{1}},...,P_{k_{n}}) underlying 𝒞 ⁡ ( 1, P k 1, …, P k n) \mathcal{C}(1,P_{k_{1}},\ldots,P_{k_{n}}) contains a double covering of the underlying directed graph G ( 1 k n + 2) 3 G_{(1^{k_{n}+2})_{3}} presenting the path set X ⁡ ( 1, L k n + 1) X(1,L_{k_{n}+1}) underlying 𝒞 ⁡ ( 1, L k n + 1) \mathcal{C}(1,L_{k_{n}+1}). Consequently

 | dim H ( 𝒞 ⁡ ( 1, P k 1, …, P k n)) ≥ dim H ( 𝒞 ⁡ ( 1, L k n + 2)). \dim_{H}(\mathcal{C}(1,P_{k_{1}},\ldots,P_{k_{n}}))\geq\dim_{H}(\mathcal{C}(1,L_{k_{n}+2})). |  | (4.2) |

###### Proof.

The graphs under consideration are the graphs given by Algorithm A of [3]. Since the underlying graph G k G_{k} of the path set presentation ( 𝒢 k, v 0) ({\mathcal{G}}_{k},v_{0}) of the path set X ⁡ ( 1, P k) X(1,P_{k}) contains a double covering of the underlying graph G k + 1 ′ G_{k+1}^{{}^{\prime}} of the path set presentation of X ⁡ ( 1, L k + 1) X(1,L_{k+1}), and

 | 𝒢 ( 1 k 1 + 2) 3 ⋆ ⋯ ⋆ 𝒢 ( 1 k n + 2) 3 ≅ 𝒢 ( 1 k n + 2) 3, \mathcal{G}_{(1^{k_{1}+2})_{3}}\star\cdots\star\mathcal{G}_{(1^{k_{n}+2})_{3}}\cong\mathcal{G}_{(1^{k_{n}+2})_{3}}, |  |

the proposition follows from Theorem 9.1 in Appendix B.

Note that this directed graph covering is not a covering at the level of path sets, because the path labels on the two graphs differ. ∎

Theorem 4.7 shows that there exist an arbitrarily large number of different values M j M_{j}, each having a 2 2 in their ternary expansion, such that dim H ( 𝒞 ⁡ ( 1, M 1, M 2, …, M n)) > 0 \dim_{H}(\mathcal{C}(1,M_{1},M_{2},...,M_{n}))>0.

## 5. The infinite family Q k = 3 2 ​ k − 3 k + 1 = ( 2 k ​ 0 k − 1 ​ 1) 3 Q_{k}=3^{2k}-3^{k}+1=(2^{k}0^{k-1}1)_{3}

Let Q k = 3 2 ​ k − 3 k + 1 = ( 2 k ​ 0 k − 1 ​ 1) 3 Q_{k}=3^{2k}-3^{k}+1=(2^{k}0^{k-1}1)_{3}. We will prove Theorem 2.3, which describes the structure of a graph presentation 𝒢 k \mathcal{G}_{k} of 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}). We then use this description to prove Theorem 2.4, which computes the Hausdorff dimension of 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}).

### 5.1. The Family Q k = ( 2 k ​ 0 k − 1 ​ 1) 3 = 3 2 ​ k − 3 k + 1 Q_{k}=(2^{k}0^{k-1}1)_{3}=3^{2k}-3^{k}+1: Path set structure

First, let us give an example. The following example gives a path set presentation for Q 2 = 73 Q_{2}=73.

###### Example 5.1.

A path set presentation of X ⁡ ( 1, 73) X(1,73), with 73 = ( 2201) 3 73=(2201)_{3}, is shown in Figure 5.1. The vertex labeled 0 0 is the marked initial vertex.

-250,-250)(250,250)

20pt0 n2201 n10121 n220 n10221 n11001 20pt1 n1100 n110 n10011 n10 n00 n1020 n10011 n10221 n1000 n100 n10 n2211 n220 n10001 n10201 n1000n10001
FIGURE 5.1 Path set presentation of X ⁡ ( 1, 73) X(1,73). The marked vertex is 0 0.

The graph in Figure 5.1 has adjacency matrix

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎), \bf{A}=\left(\begin{array}[]{cccccccccccccccc}1&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&1&1&0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&1&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&1&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&1&0&0&0&0&0&1&0&0&0&0&0\\ 0&0&0&0&0&1&0&0&0&0&0&1&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&1&1&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&1\\ 0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1\\ 0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0\\ 1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0\\ \end{array}\right), |  |

which has Perron eigenvalue β = 1 + 5 2 \beta=\frac{1+\sqrt{5}}{2}, so

 | dim H ( 𝒞 ⁡ ( 1, 73)) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438108. \dim_{H}(\mathcal{C}(1,73))=\log_{3}\left(\frac{1+\sqrt{5}}{2}\right)\approx 0.438108. |  |

We describe the path set presentation in general. Theorem 2.3 will follow easily from the following result, which makes use of the concepts developed in Section 3.4.

###### Proposition 5.1.

Let 𝒫 = X ⁡ ( 1, 7) \mathcal{P}=X(1,7) be the path set underlying 𝒞 ⁡ ( 1, 7) \mathcal{C}(1,7), and let 𝒬 = X ⁡ ( 1, Q k) \mathcal{Q}=X(1,Q_{k}) be the path set underlying 𝒞 ⁡ ( 1, Q k) \mathcal{C}(1,Q_{k}). Then 𝒬 \mathcal{Q} is the interleaved path set

 | 𝒬 = 𝒫 ( ∗ k). \mathcal{Q}=\mathcal{P}^{(*k)}. |  | (5.1) |

###### Proof.

For convenience, we recall that 𝒫 = X 𝒢 ​ ( 0) \mathcal{P}=X_{\mathcal{G}}(0) for the graph 𝒢 \mathcal{G} in Figure 5.1. This is the graph given by the Algorithm A of [3].

-80,-50)(80,150) 20pt0 20pt1 n21 n101 n10 n00
FIGURE 5.2. Path set presentation of X ⁡ ( 1, 7) X(1,7). The marked vertex is 0 0.

Let ( ℋ, v 0) (\mathcal{H},v_{0}) be the graph presentation of 𝒬 \mathcal{Q} given by the same algorithm. An element of 𝒫 \mathcal{P} may begin with either a 0 0 or a 1 1, while an element ( x i) i = 0 ∞ (x_{i})_{i=0}^{\infty} of 𝒬 \mathcal{Q} may begin with any sequence x 0 x 1 ⋯ x k − 1 x_{0}x_{1}\cdots x_{k-1} of 0 0 ’s and 1 1 ’s, since Q k Q_{k} terminates in 0 k − 1 ​ 1 0^{k-1}1. Thus, the initial k k -blocks of 𝒬 \mathcal{Q} are precisely the same as the initial k k -blocks of the interleaved path set 𝒫 ( ∗ k) \mathcal{P}^{(*k)}.

To show that 𝒬 = 𝒫 ( ∗ k) \mathcal{Q}=\mathcal{P}^{(*k)} we just need to check that for each 0 ≤ j ≤ k − 1 0\leq j\leq k-1, the admissible strings x j x j + k x j + 2 ​ k ⋯ x_{j}x_{j+k}x_{j+2k}\cdots of j ( mod k) j~(\bmod k) digits of elements of 𝒬 \mathcal{Q} are precisely the elements of 𝒫 \mathcal{P}. We proceed by induction on j ≥ 0 j\geq 0, the observation above completing the base case j = 0 j=0. Inductively, assume none of the digits x r x_{r} for r ≡ l ( mod k) r\equiv l~(\bmod k) with l < j l<j can restrict the admissible values for the digits x j + n ​ k x_{j+nk} for n ≥ 0 n\geq 0. We mean here that whether x r = 0 x_{r}=0 or x r = 1 x_{r}=1 has no effect on the last digit of the vertex label in ℋ \mathcal{H} arrived at from a path labeled x 0 x 1 ⋯ x j + n ​ k x_{0}x_{1}\cdots x_{j+nk} originating at v 0 v_{0}. The base case, j = 0 j=0, is satisfied trivially. Then we can without loss of generality assume x i = 0 x_{i}=0 for all 0 ≤ i < j 0\leq i<j. For now, we will also assume that x r = 0 x_{r}=0 for all r ≢ j ( mod k) r\not\equiv j~(\bmod k). This assumption is not as restrictive as it seems since, as we will show, the j ( mod k) j~(\bmod k) digits do not effect the available choices for digits of other modular classes. Now since Q k = 2 k ​ 0 k − 1 ​ 1 Q_{k}=2^{k}0^{k-1}1, whether x j x_{j} is 0 0 or 1 1 has no effect on the digits x j + 1, x j + 2, …, x j + k − 1 x_{j+1},x_{j+2},\ldots,x_{j+k-1}. If x j = 0 x_{j}=0, then x j + k x_{j+k} may also be either 0 0 or 1 1. If x j + m ​ k x_{j+mk} is 0 0 for all m < n m<n, then also x j + n ​ k x_{j+nk} may be either 0 0 or 1 1, and those x r x_{r} for r < j + n ​ k r<j+nk, r ≢ j ( mod k) r\not\equiv j~(\bmod k) are unrestricted. On the other hand, suppose there is an n ≥ 0 n\geq 0 such that x j + m ​ k = 0 x_{j+mk}=0 for all m < n m<n and x j + n ​ k = 1 x_{j+nk}=1. Again, the labels x r x_{r} for r < j + ( n + 1) ​ k r<j+(n+1)k, r ≢ j ( mod k) r\not\equiv j~(\bmod k) are unrestricted. However, x j + ( n + 1) ​ k x_{j+(n+1)k} must now be a 1 1. Now the label of the vertex we are at, having traversed the path labeled x 0 x 1 ⋯ x j + ( n + 1) ​ k x_{0}x_{1}\cdots x_{j+(n+1)k} from v 0 v_{0}, has label 10 2 ​ k − 1 10^{2k-1}. Thus the digits x j + ( n + 1) ​ k + 1, x j + ( n + 1) ​ k + 2, ⋯ x j + ( n + 3) ​ k − 1 x_{j+(n+1)k+1},x_{j+(n+1)k+2},\cdots x_{j+(n+3)k-1} are unrestricted. However, if the digit x j + ( n + 2) ​ k x_{j+(n+2)k} is a 1 1, then the vertex at the end of the path labeled x 0 x 1 ⋯ x j + ( n + 2) ​ k x_{0}x_{1}\cdots x_{j+(n+2)k} has label 10 2 ​ k − 1 10^{2k-1}, so the vertices after x j + ( n + 2) ​ k x_{j+(n+2)k} are restricted or unrestricted in precisely the same way as those after x j + ( n + 1) ​ k x_{j+(n+1)k}. If on the other hand x j + ( n + 2) ​ k = 0 x_{j+(n+2)k}=0, then the terminal vertex has label 10 k − 2 10^{k-2}. Thus, the label of the vertex after j + ( n + 3) ​ k − 1 j+(n+3)k-1 steps in this case is 1 1, hence in this case x j + ( n + 3) ​ k x_{j+(n+3)k} must be 0 0. The resulting terminal vertex label is 0 0. In either case, the digits, x j + ( n + 3) ​ k + 1, x j + ( n + 3) ​ k + 2, x j + ( n + 4) ​ k − 1 x_{j+(n+3)k+1},x_{j+(n+3)k+2},x_{j+(n+4)k-1} are unrestricted. For the ( j + ( n + 4) ​ k) (j+(n+4)k) th step we either begin at vertex 0 0 or at vertex 10 k − 1 10^{k-1}, which cases have already been considered.

Thus, we have shown that the digits x j + n ​ k x_{j+nk} place no restrictions on any digits from the other modular classes, and, furthermore, we have described the restrictions that x j + n ​ k x_{j+nk} place on x j + m ​ k x_{j+mk} for m > n m>n. Inspecting this description shows that the admissible digits x j ​ x j + k ​ x j + 2 ​ k x_{j}x_{j+k}x_{j+2k} are precisely the edge labels of the infinite walks in 𝒢 \mathcal{G} originating at the vertex 0 0 in Figure 5.1. These are precisely the elements of 𝒫 \mathcal{P}, so 𝒬 = 𝒫 ( ∗ k) \mathcal{Q}=\mathcal{P}^{(*k)}. ∎

Let 𝒢 \mathcal{G} be the graph of Figure 5.1. The presentation for Q k Q_{k} given by Proposition 3.4 applied to k k and 𝒢 \mathcal{G} is isomorphic to that given by Algorithm A of [3]. We are now ready to prove Theorem 2.3.

###### Proof of Theorem 2.3.

Let ( 𝒢 k, v 0) (\mathcal{G}_{k},v_{0}) be the presentation of 𝒬 = X ⁡ ( 1, Q k) \mathcal{Q}=X(1,Q_{k}) constructed by applying the algorithm of Proposition 3.4 to the presentation 𝒢 \mathcal{G} of X ⁡ ( 1, 7) X(1,7). Since the graph 𝒢 \mathcal{G} used in this construction has 4 4 vertices and 6 6 edges, it follows by Proposition 3.4 that 𝒢 k \mathcal{G}_{k} has 4 k 4^{k} vertices and 6 ⋅ 4 k − 1 6\cdot 4^{k-1} edges. Moreover, since 𝒢 \mathcal{G} is strongly connected, so is 𝒢 k \mathcal{G}_{k}, by Remark 3.5. This proves the theorem. ∎

### 5.2. The family Q k = ( 2 k ​ 0 k − 1 ​ 1) 3 = 3 2 ​ k − 3 k + 1 Q_{k}=(2^{k}0^{k-1}1)_{3}=3^{2k}-3^{k}+1: Hausdorff dimension

We have shown that

 | X ( 1, Q k) = X ( 1, 7) ( ∗ k), X(1,Q_{k})=X(1,7)^{(*k)}, |  | (5.2) |

is given by an interleaving construction. Using the results of Section 3.4, it is now a simple matter to prove Theorem 2.4.

###### Proof of Theorem 2.4.

We are trying to show that

 | dim H ( 𝒞 ⁡ ( 1, Q k)) = log 3 ⁡ ϕ. \dim_{H}(\mathcal{C}(1,Q_{k}))=\log_{3}\phi. |  |

The result follows by Proposition 5.1 and by application of the interleaving result given in Corollary 3.7, since

 | dim H ( 𝒞 ⁡ ( 1, 7)) = log 3 ⁡ ϕ, \dim_{H}(\mathcal{C}(1,7))=\log_{3}\phi, |  |

as is easily computed, and Corollary 3.7 shows that the interleaving operation ( ⋅) ( ∗ k) (\cdot)^{(*k)} preserves the topological entropy of the input path set. ∎

## 6. Bounds on Hausdorff dimensions by numbers of ternary digits

We study properties of the Hausdorff dimension constants α n \alpha_{n}.

### 6.1. Upper Bound on Γ \Gamma via n n -digit constants α n {\alpha}_{n}: Proof of Theorem 2.5.

It is known that the number of nonzero ternary digits in ( 2 n) 3 (2^{n})_{3} goes to infinity as n → ∞ n\to\infty, i.e. for each k ≥ 2 k\geq 2 there are only finitely many n n with ( 2 n) 3 (2^{n})_{3} having at most k k nonzero ternary digits. This result was first established in 1971 by Senge and Straus, see [19]. In 1980 Colin L. Stewart [21, Theorem 1] obtained a quantitative refinement of such bounds. We obtain as a special case of his result the following quantitative version of the rate of growth of the number of nonzero digits.

###### Theorem 6.1.

(C. L. Stewart) For each k ≥ 1 k\geq 1, there are only finitely many n n such that the base 3 3 expansion of 2 n 2^{n} (equivalently the 3 3 -adic expansion ( 2 n) 3 (2^{n})_{3}) has at most k k nonzero digits. More precisely, if n 3 ​ ( n) n_{3}(n) denotes the sum of the base 3 3 digits of n n, then for m ≥ 25 m\geq 25,

 | n 3 ​ ( 2 m) > log ⁡ m log ⁡ log ⁡ m + c − 3, n_{3}(2^{m})>\frac{\log m}{\log\log m+c}-3, |  |

where c > 0 c>0 is an effectively computable constant.

###### Proof.

The result follows from [21, Theorem 1], taking for bases a = 2 a=2, b = 3 b=3, and digits α = β = 0 \alpha=\beta=0. Using Stewart’s notation, L a, α ​ ( 2 m) = 2, L_{a,\alpha}(2^{m})=2, so that L a, α, b, β ​ ( 2 m) − 2 L_{a,\alpha,b,\beta}(2^{m})-2 counts the number of nonzero ternary digits n 3 ​ ( 2 m) n_{3}(2^{m}) of 2 m 2^{m}. ∎

We can now prove Theorem 2.5.

###### Proof of Theorem 2.5.

For each n ≥ 1 n\geq 1 we have

 | Γ ≤ dim H ( ℰ 1 ( n + 1)). \Gamma\leq\dim_{H}(\mathcal{E}_{1}^{(n+1)}). |  |

We also have the inclusions

 | ℰ 1 ( n + 1) = ⋃ 0 ≤ m 1 < … < m k 𝒞 ⁡ ( 1, 2 m 1, …, 2 m n) ⊂ ⋃ m = n ∞ 𝒞 ⁡ ( 1, 2 m), \mathcal{E}_{1}^{(n+1)}=\bigcup_{0\leq m_{1}<\ldots<m_{k}}\mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{n}})\subset\bigcup_{m=n}^{\infty}\mathcal{C}(1,2^{m}), |  | (6.1) |

which yields

 | dim H ( ℰ 1 ( n + 1)) ≤ sup m ≥ n ( dim H ( 𝒞 ⁡ ( 1, 2 m))). \dim_{H}(\mathcal{E}_{1}^{(n+1)})\leq\sup_{m\geq n}\Big(\dim_{H}(\mathcal{C}(1,2^{m}))\Big). |  |

Consequently we have

 | Γ ≤ sup m ≥ n ( dim H ( 𝒞 ⁡ ( 1, 2 m))). \Gamma\leq\sup_{m\geq n}\Big(\dim_{H}(\mathcal{C}(1,2^{m}))\Big). |  | (6.2) |

However Theorem 6.1 implies that all ( 2 m) 3 (2^{m})_{3} for m ≥ n m\geq n contain at least

 | k = k ⁡ ( n):= ⌊ log ⁡ n log ⁡ log ⁡ n + c ⌋ − 3 k=k(n):=\left\lfloor\frac{\log n}{\log\log n+c}\right\rfloor-3 |  |

nonzero ternary digits. In particular

 | ℰ 1 ( n + 1) ⊂ ⋃ m = n ∞ 𝒞 ( 1, 2 m) ⊂ ⋃ { M: n 3 ​ ( M) ≥ k ⁡ ( n) } 𝒞 ( 1, M). \mathcal{E}_{1}^{(n+1)}\subset\bigcup_{m=n}^{\infty}\mathcal{C}(1,2^{m})\subset\bigcup_{\{{M}:\,n_{3}(M)\geq k(n)\}}\mathcal{C}(1,M). |  |

By defnition of α k {\alpha}_{k} it follows that

 | dim H ( ℰ 1 ( n + 1)) ≤ α k ⁡ ( n). \dim_{H}(\mathcal{E}_{1}^{(n+1)})\leq{\alpha}_{k(n)}. |  |

Since k ⁡ ( n) → ∞ k(n)\to\infty as n → ∞ n\to\infty, we obtain

 | Γ = lim n → ∞ dim H ( ℰ 1 ( n + 1)) ≤ lim k → ∞ α k, \Gamma=\lim_{n\to\infty}\dim_{H}(\mathcal{E}_{1}^{(n+1)})\leq\lim_{k\to\infty}{\alpha}_{k}, |  |

as asserted. ∎

### 6.2. Exact bound for α 2 {\alpha}_{2}

We obtain a complete determination of α 2 {\alpha}_{2}.

###### Theorem 6.2.

For all M ≥ 1 M\geq 1 with M ≡ 1 ( mod 3) M\equiv\,1\,(\bmod\,3), one has

 | dim H ( 𝒞 ⁡ ( 1, M)) ≤ log 3 ⁡ ϕ ≈ 0.438018. \dim_{H}(\mathcal{C}(1,M))\leq\log_{3}\phi\approx 0.438018. |  |

where ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} is the golden ratio. Thus α 2 = log 3 ⁡ ϕ ≈ 0.438018 {\alpha}_{2}=\log_{3}\phi\approx 0.438018

###### Proof.

We may write M = ( m n ​ m n − 1 ​ … ​ m k ​ 0 k − 1 ​ 1) 3 M=(m_{n}m_{n-1}\ldots m_{k}0^{k-1}1)_{3} for some 1 ≤ k ≤ n < ∞ 1\leq k\leq n<\infty since M M is an integer, M ≡ 1 ( mod 3) M\equiv 1~(\bmod 3). Our strategy will be to construct an injective map f: 𝒞 ⁡ ( 1, M) → 𝒞 ⁡ ( 1, N k) f:\mathcal{C}(1,M)\rightarrow\mathcal{C}(1,N_{k}), where recall that N k = ( 10 k − 1 ​ 1) 3 N_{k}=(10^{k-1}1)_{3}, and by [3, Theorem 1.8], dim H ( 𝒞 ⁡ ( 1, N k)) = log 3 ⁡ ( ϕ) \dim_{H}(\mathcal{C}(1,N_{k}))=\log_{3}(\phi). Let ( 𝒢, v 0) (\mathcal{G},v_{0}) and ( ℋ k, w 0) (\mathcal{H}_{k},w_{0}) be the right-resolving, connected, essential presentations of 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) and 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}), respectively, constructed by Algorithm A of [3]. The injective map f f induces for each l l an injective map from the set of paths of length l l in 𝒢 \mathcal{G} originating at v 0 v_{0} to the set of paths of length l l in ℋ k \mathcal{H}_{k} originating at w 0 w_{0}, since there is a bijective correspondence between elements of 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) or 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) and infinite paths in 𝒢 \mathcal{G} or ℋ k \mathcal{H}_{k}, respectively, originating at the distinguished vertex. Thus, following [1, Definition 1.10] and [2, Theorem 1.1], this will establish the result.

To define the map f: 𝒞 ⁡ ( 1, M) → 𝒞 ⁡ ( 1, N k) f:\mathcal{C}(1,M)\rightarrow\mathcal{C}(1,N_{k}), we will need some notation. Let α = … ​ a 2 ​ a 1 ​ a 0 \alpha=\ldots a_{2}a_{1}a_{0} be a generic element of 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M). α \alpha corresponds to a vertex path … ​ v 2 ​ v 1 ​ v 0 \ldots v_{2}v_{1}v_{0} of 𝒢 \mathcal{G} such that there is an edge labeled a i a_{i} from vertex v i v_{i} to vertex v i + 1 v_{i+1}. We call the digit a i a_{i}*restricted*if the out-degree of v i v_{i} is 1 1, and we call a i a_{i}*unrestricted*if the out-degree of v i v_{i} is 2 2. We call a i a_{i}*restricting*if a i + k a_{i+k} is restricted, and otherwise we call a i a_{i}*non-restricting*.

If the digit a i a_{i} of α \alpha is unrestricted, then it is possible to find an element
α ′ = … ​ a i + k − 1 ​ a i + k − 2 ​ … ​ a i + 1 ​ ( 1 − a i) ​ a i − 1 ​ … ​ a 2 ​ a 1 ​ a 0 ∈ 𝒞 ⁡ ( 1, M) \alpha^{\prime}=\ldots a_{i+k-1}a_{i+k-2}\ldots a_{i+1}(1-a_{i})a_{i-1}\ldots a_{2}a_{1}a_{0}\in\mathcal{C}(1,M). That is, changing a i a_{i} to 1 − a i 1-a_{i} does not require us to make any other changes until the i + k i+k -th digit. Then for all such α ′ \alpha^{\prime} the vertex v i + k ′ v_{i+k}^{\prime} of the corresponding vertex path on 𝒢 \mathcal{G} is the same. If a i a_{i} is not only unrestricted but also restricting, then if this vertex v i + k ′ v_{i+k}^{\prime} has out-degree 1 1, we call a i a_{i}*unconditionally restricting*, and if v i + k ′ v_{i+k}^{\prime} has out-degree 2 2, we call a i a_{i}*conditionally restricting*. Thus, a conditionally restricting digit can be changed to become unrestricting, while an unconditionally restricting digit remains restricting when changed.

Tautologically, a conditionally restricting digit a i a_{i} becomes unrestricting when replaced by 1 − a i 1-a_{i}, but we can also see that an unrestricted, unrestricting digit a i a_{i} becomes conditionally restricting when replaced by 1 − a i 1-a_{i}, since this necessarily changes the carry digit at the ( i + k) (i+k) -th step. Thus, these types of digits come in pairs.

Now we are ready to construct the map f: 𝒞 ⁡ ( 1, M) → 𝒞 ⁡ ( 1, N k) f:\mathcal{C}(1,M)\rightarrow\mathcal{C}(1,N_{k}), digit-by-digit, for α ∈ 𝒞 ⁡ ( 1, M) \alpha\in\mathcal{C}(1,M):

 | f ​ ( α) i = { 0 if ​ a i ​ is restricted or unrestricting; a i if ​ a i ​ is unrestricted and unconditionally restricting; 1 if ​ a i ​ is unrestricted and conditionally restricting. f(\alpha)_{i}=\begin{cases}0&\text{if }a_{i}\text{ is restricted or unrestricting};\\ a_{i}&\text{if }a_{i}\text{ is unrestricted and unconditionally restricting};\\ 1&\text{if }a_{i}\text{ is unrestricted and conditionally restricting}.\\ \end{cases} |  | (6.3) |

Though f ⁡ ( α) f(\alpha) is clearly an element of Σ 3 \Sigma_{3}, we need to check first that it is really an element of 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}). To see this, note that if f ​ ( α) i = 1 f(\alpha)_{i}=1, then a i a_{i} was restricting, so a i + k a_{i+k} is restricted, thus f ​ ( α) i + k = 0 f(\alpha)_{i+k}=0. So a digit 1 1 of f ⁡ ( α) f(\alpha) is always followed, k k digits later, by a digit 0 0. Since 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) can be described as the ℤ / 2 ​ ℤ \mathbb{Z}/2\mathbb{Z} -shift of finite type with forbidden block set { 10 k − 1 ​ 1 } \{10^{k-1}1\}, and this block does not occur in f ⁡ ( α) f(\alpha), we are assured that f ⁡ ( α) ∈ 𝒞 ⁡ ( 1, N k) f(\alpha)\in\mathcal{C}(1,N_{k}).

It remains only to check that f f is injective. Suppose α = … ​ a 2 ​ a 1 ​ a 0, β = … ​ b 2 ​ b 1 ​ b 0 ∈ 𝒞 ⁡ ( 1, M) \alpha=\ldots a_{2}a_{1}a_{0},\beta=\ldots b_{2}b_{1}b_{0}\in\mathcal{C}(1,M) are distinct. Then there is a j j such that a j = 1 − b j a_{j}=1-b_{j} and a i = b i a_{i}=b_{i} for all 0 ≤ i < j 0\leq i<j. Let … ​ v 2 ​ v 1 ​ v 0 \ldots v_{2}v_{1}v_{0} and … ​ w 2 ​ w 1 ​ w 0 \ldots w_{2}w_{1}w_{0} be the vertex paths of 𝒢 \mathcal{G} corresponding to α \alpha and β \beta, respectively. Then we must have v i = w i v_{i}=w_{i} for 0 ≤ i ≤ j 0\leq i\leq j, and v j = w j v_{j}=w_{j} must have out-degree 2 2. Thus, the digits a j a_{j} of α \alpha and b j b_{j} of β \beta are unrestricted. But by the discussion above, if a j a_{j} is conditionally restricting then b j b_{j} is unrestricting, in which case f ​ ( α) j = 1 ≠ 0 = f ​ ( β) j f(\alpha)_{j}=1\neq 0=f(\beta)_{j}, and vice versa, or else a j a_{j} and b j b_{j} are both unconditionally restricting, in which case f ​ ( α) j = a j ≠ b j = f ​ ( β) j f(\alpha)_{j}=a_{j}\neq b_{j}=f(\beta)_{j}. In any case, we see that f ⁡ ( α) ≠ f ⁡ ( β) f(\alpha)\neq f(\beta), so f f is injective, establishing the result. ∎

## 7. Block number and intermittency of ternary expansions

The examples given so far show that the dependence of dim H ( 𝒞 ⁡ ( 1, M)) \dim_{H}({\mathcal{C}}(1,M)) for a positive integer M M is complicated function, being driven by the structure of the underlying automata, whose construction includes aspects of both number theory and dynamical systems. One may ask whether the Hausdorff dimension might go to zero as a function of some statistic easily computable from the ternary expansion ( M) 3 (M)_{3}. Earlier results of this paper show that the statistic d 3 ​ ( M) d_{3}(M) does not have this property.

We now present empirical results for two other interesting statistics of ( M) 3 (M)_{3}:

1. (1)

The block number b 3 ​ ( M) {b}_{3}(M) counts the number of blocks of consecutive nonzero digits in the ternary expansion ( M) 3 (M)_{3}.

2. (2)

The intermittency s 3 ​ ( M) {s}_{3}(M) counts the number of distinct blocks of consecutive matching digits in the ternary expansion ( M) 3 (M)_{3}.

We clearly have b 3 ​ ( M) ≤ s 3 ​ ( M) {b}_{3}(M)\leq{s}_{3}(M). As examples,

 | b 3 ​ ( ( 2121011) 3) = 2; b 3 ​ ( ( 2101) 3) = 2, {b}_{3}((2121011)_{3})=2;\quad{b}_{3}((2101)_{3})=2, |  |

while

 | s 3 ​ ( ( 2121011) 3) = 6; s 3 ​ ( ( 2101) 3) = 4. {s}_{3}((2121011)_{3})=6;\quad{s}_{3}((2101)_{3})=4. |  |

The statistic b 3 ​ ( M) {b}_{3}(M) might be relevant to controlling the Hausdoff dimension since blocks of zeros at the end of the number have a simple effect on the associated automaton.

Table 7.1 below presents data on Hausdorff dimensions for a few numbers M M taking the smallest values for s 3 ​ ( M) {s}_{3}(M), computed using the algorithm in Part I to six decimal places. The table also provides the number of vertices in the associated finite directed graph.

Path Set C ⁡ ( 1, M) C(1,M) | ( M) 3 (M)_{3} | s 3 ​ ( M) {s}_{3}(M) | Vertices | Perron eigenvalue | Hausdorff dim |

𝒞 ⁡ ( 1, 10) {\mathcal{C}}(1,10) | 101 101 | 3 3 | 4 4 | 1.618033 1.618033 | 0.438018 0.438018 |

𝒞 ⁡ ( 1, 16) {\mathcal{C}}(1,16) | 121 121 | 3 3 | 5 5 | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1, 19) {\mathcal{C}}(1,19) | 201 201 | 3 3 | 8 8 | 1.465571 1.465571 | 0.347934 0.347934 |

𝒞 ⁡ ( 1, 73) {\mathcal{C}}(1,73) | 2201 2201 | 3 3 | 16 16 | 1.618033 1.618033 | 0.438018 0.438018 |

𝒞 ⁡ ( 1, 34) {\mathcal{C}}(1,34) | 1021 1021 | 4 4 | 8 8 | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1, 46) {\mathcal{C}}(1,46) | 1201 1201 | 4 4 | 10 10 | 1.112776 1.112776 | 0.097266 0.097266 |

𝒞 ⁡ ( 1, 61) {\mathcal{C}}(1,61) | 2021 2021 | 4 4 | 14 14 | 1.570147 1.570147 | 0.410672 0.410672 |

𝒞 ⁡ ( 1, 64) {\mathcal{C}}(1,64) | 2101 2101 | 4 4 | 14 14 | 1.357193 1.357193 | 0.278004 0.278004 |

𝒞 ⁡ ( 1, 70) {\mathcal{C}}(1,70) | 2121 2121 | 4 4 | 14 14 | 1.360632 1.360632 | 0.280308 0.280308 |

𝒞 ⁡ ( 1, 91) {\mathcal{C}}(1,91) | 10101 10101 | 5 5 | 9 9 | 1.465571 1.465571 | 0.347934 0.347934 |

𝒞 ⁡ ( 1, 97) {\mathcal{C}}(1,97) | 10121 10121 | 5 5 | 16 16 | 1.380277 1.380277 | 0.293356 0.293356 |

𝒞 ⁡ ( 1,100) {\mathcal{C}}(1,100) | 10201 10201 | 5 5 | 17 17 | 1.354948 1.354948 | 0.276497 0.276497 |

𝒞 ⁡ ( 1,142) {\mathcal{C}}(1,142) | 12021 12021 | 5 5 | 20 20 | 1.276393 1.276393 | 0.222133 0.222133 |

𝒞 ⁡ ( 1,145) {\mathcal{C}}(1,145) | 12101 12101 | 5 5 | 21 21 | 1.000000 1.000000 | 0.000000 0.000000 |

𝒞 ⁡ ( 1,151) {\mathcal{C}}(1,151) | 12121 12121 | 5 5 | 20 20 | 1.227525 1.227525 | 0.186599 0.186599 |

𝒞 ⁡ ( 1,172) {\mathcal{C}}(1,172) | 20101 20101 | 5 5 | 22 22 | 1.288329 1.288329 | 0.230606 0.230606 |

𝒞 ⁡ ( 1,178) {\mathcal{C}}(1,178) | 20121 20121 | 5 5 | 25 25 | 1.345528 1.345528 | 0.270148 0.270148 |

𝒞 ⁡ ( 1,181) {\mathcal{C}}(1,181) | 20201 20201 | 5 5 | 22 22 | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1,196) {\mathcal{C}}(1,196) | 21021 21021 | 5 5 | 24 24 | 1.383785 1.383785 | 0.295666 0.295666 |

𝒞 ⁡ ( 1,208) {\mathcal{C}}(1,208) | 21201 21201 | 5 5 | 25 25 | 1.290893 1.290893 | 0.232415 0.232415 |

TABLE 7.1. Hausdorff dimension of 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) by intermittency

This extremely limited data set exhibits a small decrease in Hausdorff dimensions as the statistic s 3 ​ ( M) {s}_{3}(M) increases. It leaves open the possibility that one might have dim H ( 𝒞 ⁡ ( 1, M)) → 0 \dim_{H}(\mathcal{C}(1,M))\to 0 as b 3 ​ ( M) → ∞ {b}_{3}(M)\to\infty, noting that b 3 ​ ( M) ≤ s 3 ​ ( M) {b}_{3}(M)\leq{s}_{3}(M). Further numerical experimentation seems warranted to get a better idea whether such an assertion might be true.

Regarding potential applicability of information on these statistics to the Exceptional set conjecture, we must point out that it is not currently known whether b 3 ​ ( 2 n) → ∞ {b}_{3}(2^{n})\to\infty holds as n → ∞ n\to\infty or whether s 3 ​ ( 2 n) → ∞ {s}_{3}(2^{n})\to\infty holds as n → ∞. n\to\infty.

## 8. Appendix A: Review of results for families L k = ( 1 k) 3 L_{k}=(1^{k})_{3} and N k = ( 10 k − 1 ​ 1) 3 N_{k}=(10^{k-1}1)_{3}.

We review two results proved in [3, Section 4]. The first is for the family L k = 1 2 ​ ( 3 k − 1) = ( 1 k) 3 L_{k}=\frac{1}{2}(3^{k}-1)=(1^{k})_{3}, for k ≥ 1 k\geq 1, given as [3, Theorem 5.2].

###### Theorem 8.1.

(Infinite Family L k = 1 2 ​ ( 3 k − 1) L_{k}=\frac{1}{2}(3^{k}-1))

(1) Let L k = 1 2 ​ ( 3 k − 1) = ( 1 k) 3 L_{k}=\frac{1}{2}(3^{k}-1)=(1^{k})_{3}. The path set presentation ( 𝒢, v) ({\mathcal{G}},v) for the path set X ⁡ ( 1, L k) X(1,L_{k}) underlying 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) has exactly k k vertices and is strongly connected.

(2) For every k ≥ 1 k\geq 1,

 | dim H ( 𝒞 ⁡ ( 1, L k)) = dim H 𝒞 ⁡ ( 1, ( 1 k) 3) = log 3 ⁡ β k, \dim_{H}(\mathcal{C}(1,L_{k}))=\dim_{H}\mathcal{C}(1,(1^{k})_{3})=\log_{3}\beta_{k}, |  |

where β k \beta_{k} is the unique real root greater than 1 1 of λ k − λ k − 1 − 1 = 0 \lambda^{k}-\lambda^{k-1}-1=0.

(3) For all k ≥ 3 k\geq 3 there holds

 | dim H ( 𝒞 ⁡ ( 1, L k)) = log 3 ⁡ k k + O ⁡ ( log ⁡ log ⁡ ( k) k). \dim_{H}\Big(\mathcal{C}(1,L_{k})\Big)=\frac{\log_{3}k}{k}+O\left(\frac{\log\log(k)}{k}\right). |  |

The Hausdorff dimension dim H ( 𝒞 ⁡ ( 1, L k)) \dim_{H}(\mathcal{C}(1,L_{k})) is positive but approaches 0 0 as k → ∞ k\to\infty. We present data in Table 8.1 below.

Path set | L k L_{k} | Vertices | Perron eigenvalue | Hausdorff dim |

𝒞 ⁡ ( 1, L 1) \mathcal{C}(1,L_{1}) | 1 | 1 | 2.000000 2.000000 | 0.630929 0.630929 |

𝒞 ⁡ ( 1, L 2) \mathcal{C}(1,L_{2}) | 4 | 2 | 1.618033 1.618033 | 0.438018 0.438018 |

𝒞 ⁡ ( 1, L 3) \mathcal{C}(1,L_{3}) | 13 | 3 | 1.465571 1.465571 | 0.347934 0.347934 |

𝒞 ⁡ ( 1, L 4) \mathcal{C}(1,L_{4}) | 40 | 4 | 1.380278 1.380278 | 0.293358 0.293358 |

𝒞 ⁡ ( 1, L 5) \mathcal{C}(1,L_{5}) | 121 | 5 | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1, L 6) \mathcal{C}(1,L_{6}) | 364 | 6 | 1.285199 1.285199 | 0.228392 0.228392 |

𝒞 ⁡ ( 1, L 7) \mathcal{C}(1,L_{7}) | 1093 | 7 | 1.255423 1.255423 | 0.207052 0.207052 |

𝒞 ⁡ ( 1, L 8) \mathcal{C}(1,L_{8}) | 3280 | 8 | 1.232055 1.232055 | 0.189948 0.189948 |

𝒞 ⁡ ( 1, L 9) \mathcal{C}(1,L_{9}) | 9841 | 9 | 1.213150 1.213150 | 0.175877 0.175877 |

TABLE 8.1. Hausdorff dimensions of 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) (to six decimal places)

We also recall results on the family N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3}, which consists of numbers with exactly two nonzero ternary digits, with s 3 ​ ( N k) = 2 s_{3}(N_{k})=2, given as [3, Theorem 5.5].

###### Theorem 8.2.

(Infinite Family N k = 3 k + 1 N_{k}=3^{k}+1)

(1) Let N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3}. The path set presentation ( 𝒢, v) ({\mathcal{G}},v) for the path set X ⁡ ( 1, N k) X(1,N_{k}) underlying 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) has exactly 2 k 2^{k} vertices and is strongly connected.

(2) For every integer k ≥ 1 k\geq 1, there holds

 | dim H ( 𝒞 ⁡ ( 1, N k)) = dim H 𝒞 ⁡ ( 1, ( 10 k − 1 ​ 1) 3) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \dim_{H}(\mathcal{C}(1,N_{k}))=\dim_{H}\mathcal{C}(1,(10^{k-1}1)_{3})=\log_{3}\bigg(\frac{1+\sqrt{5}}{2}\bigg)\approx 0.438018. |  |

Here the Hausdorff dimension is constant as k → ∞ k\to\infty.

## 9. Appendix B: Relation of families P k = ( 20 k − 1 ​ 1) 3 P_{k}=(20^{k-1}1)_{3} and L k + 1 = ( 1 k + 1) 3 L_{k+1}=(1^{k+1})_{3}

We observe a relation between the Hausdorff dimensions of 𝒞 ⁡ ( 1, P k) {\mathcal{C}}(1,P_{k}) and 𝒞 ⁡ ( 1, L k + 1) {\mathcal{C}}(1,L_{k+1}). For 1 ≤ k ≤ 4 1\leq k\leq 4, the Hausdorff dimension of 𝒞 ⁡ ( 1, ( 20 k − 1 ​ 1) 3) \mathcal{C}(1,(20^{k-1}1)_{3}) equals that of 𝒞 ⁡ ( 1, ( 1 k + 1) 3) \mathcal{C}(1,(1^{k+1})_{3}). For general k k we obtain an inequality.

###### Theorem 9.1.

The Hausdorff dimensions of 𝒞 ⁡ ( 1, P k) \mathcal{C}(1,P_{k}) and 𝒞 ⁡ ( 1, L k + 1) \mathcal{C}(1,L_{k+1}) are related by

 | dim H ( 𝒞 ⁡ ( 1, P k)) ≥ dim H ( 𝒞 ⁡ ( 1, L k + 1)). \dim_{H}(\mathcal{C}(1,P_{k}))\geq\dim_{H}(\mathcal{C}(1,L_{k+1})). |  | (9.1) |

###### Proof.

The marked vertex v 0 v_{0} with label ( 0) 3 (0)_{3} of the path set presentation 𝒢 ( 20 k − 1 ​ 1) 3 \mathcal{G}_{(20^{k-1}1)_{3}} associated to 𝒞 ⁡ ( 1, ( 20 k − 1 ​ 1) 3) \mathcal{C}(1,(20^{k-1}1)_{3}) has two exit edges, one a self-loop with edge labeled 0 0, the second an exit edge labeled 1 1 to the vertex labeled ( 20 k − 1) 3 (20^{k-1})_{3}. From this vertex, there is an edge labeled 1 1 to the vertex labeled ( 220 k − 2) 3 (220^{k-2})_{3}. This continues for k − 2 k-2 more steps into a vertex labeled ( 2 k) 3 (2^{k})_{3}, from which there is an out-edge labeled 1 1 to a vertex labeled ( 10 k) 3 (10^{k})_{3}. There is a self-loop labeled 1 1 at the ( 10 k) 3 (10^{k})_{3} -vertex, and a path of length k + 1 k+1 through vertices ( 10 k − j) 3 (10^{k-j})_{3}, for 1 ≤ j ≤ k 1\leq j\leq k, all with edge label 0 0, then back to the 0 0 -vertex. Considering only the edges given above, this comprises a subgraph H H of 𝒢 ( 20 k − 1 ​ 1) 3 \mathcal{G}_{(20^{k-1}1)_{3}} having 2 ​ k + 2 2k+2 edges that is strongly connected, and consists of a closed path starting and ending at 0 0 of length 2 ​ k + 2 2k+2 plus two self-loops, at vertices m = 0 m=0 and m = 3 k m=3^{k}. (The case k = 2 k=2 is pictured in Example 4.1, where the subgraph of 𝒢 ( 201) 3 \mathcal{G}_{(201)_{3}} under consideration is the six outer vertices in the graph in Figure 4.1.) Upon inspection we see that the graph H H is a double-covering of the graph 𝒢 ( 1 k + 1) 3 \mathcal{G}_{(1^{k+1})_{3}} associated to 𝒞 ⁡ ( 1, L k + 1) \mathcal{C}(1,L_{k+1}) given by Algorithm A of [3]. This implies the bound ( 9.1). ∎

###### Remark 9.2.

For 1 ≤ k ≤ 4 1\leq k\leq 4, equality holds in Proposition 9.1 because the subgraph of 𝒢 ( 20 k − 1 ​ 1) 3 \mathcal{G}_{(20^{k-1}1)_{3}} constructed in the proof is the strongly connected component with greatest topological entropy in these cases. This is not true for almost all larger k k. Theorem 8.1 says dim H ( 𝒞 ⁡ ( 1, L k)) → 0 \dim_{H}(\mathcal{C}(1,L_{k}))\to 0 as n → ∞ n\to\infty. On the other hand Theorem 2.2 says that dim H ( 𝒞 ⁡ ( 1, L k)) \dim_{H}(\mathcal{C}(1,L_{k})) is bounded away from 0 0 as k → ∞ k\to\infty.

## References

- [1] W. Abram and J. C. Lagarias, *Path sets in one-sided symbolic dynamics,*Advances in Applied Mathematics, 56 (2014), pp. 109-134.
- [2] W. Abram and J. C. Lagarias, *p p -Adic path set fractals and arithmetic,*Journal of Fractal Geometry, 1 (2014), no.1, 45-81.
- [3] W. Abram and J. C. Lagarias, *Intersections of multiplicative translates of 3 3 -adic Cantor sets,*Journal of Fractal Geometry, 1 (2014), no.4, 349–390.
- [4] R.L. Adler and B. Marcus, Topological entropy and equivalence of dynamical systems, Memoirs of the American Mathematical Society, Volume 20, No. 219, AMS: Providence, RI 1979.
- [5] J.P. Alloche and J. O. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge University Press: Cambridge 2003.
- [6] M. Boyle and D. Handelman, *The spectrum of nonnegative matrices via symbolic dynamics*, Ann. Math. 133 (1991), no. 2, 249–316.
- [7] G. Edgar, *Measure, topology and fractal geometry, Second Edition*Springer-Verlag: New York 2008.
- [8] P. Erdős, *Some unconventional problems in number theory*, Math. Mag. 52 (1979), 67-70.
- [9] E. de Faria and C. Tresser, *On Sloane’s persistence problem,*arXiv:1307.1188, July 2013.
- [10] E. de Faria and C. Tresser, *Equidistribution of digits in powers and Diophantine approximations,*arXiv:1307.1505, 5 July 2013.
- [11] A. Katok and B. Hasselblatt, Introduction to the Modern Theory of Dynamical Systems (Cambridge University Press, New York, 1995).
- [12] J.C. Lagarias, *Ternary expansions of powers of 2*, J. London Math. Soc.(2) 79 (2009), 562-588.
- [13] D. Lind, *The entropies of topological Markov shifts and a related class of algebraic integers*, Ergod. Th. Dyn. Sys. 4 (1984), no. 2, 283–300.
- [14] D. Lind and B. Marcus, An Introduction to Symbolic Dynamics and Coding, (Cambridge University Press, New York, 1995).
- [15] K. Mahler, Lectures on diophantine approximations, Part I. g g -adic numbers and Roth’s theorem, Prepared from notes of R. P. Bambah, University of Notre Dame Press, Notre Dame IN 1961.
- [16] R. D. Mauldin and M. Urbański, *Graph directed Markov systems. Geometry and dynamics of limit sets,*Cambridge Tracts in Mathematics No. 148, Cambridge Univ. Press: Cambridge 2003.
- [17] R. D. Mauldin and S. C. Williams, *On the Hausdorff dimension of some graphs,*Trans. Amer. Math. Soc. 298 (1986), no. 2, 793–803.
- [18] R.D. Mauldin and S.C. Williams, *Hausdorff Dimension of Graph Directed Constructions*, Transactions of the American Mathematical Society, 309, No. 2 (1988) , 811-829.
- [19] H. G. Senge and E. Straus, *P.V. numbers and sets of multiplicity,*Periodica Math. Hung. 3 (1973), 93–100.
- [20] J.G. Simonsen, *On the Computabillity of the Topological Entropy of Subshifts*, Discrete Mathematics and Theoretical Computer Science, 8 (2006), 83-96.
- [21] C. L. Stewart, *On the Representation of an Integer in two Different Bases,*J. Reine Angew. Math., 319 (1980), 63–72.
- [22] B. Weiss, *Subshifts of finite type and sofic systems,*Monatshefte für Math. 77 (1973), 462–474.
- [23] S. Williams, *A sofic system which is not spectrally of finite type,*Ergod. Th. Dyn. Sys. 8 (1988), 483–490.

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: mailto:wabram@hillsdale.edu
[2]: mailto:atb130030@utdallas.edu
[3]: mailto:lagarias@umich.edu
[4]: /html/1508.05966
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/1508.05967
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1508.05967
[10]: https://arxiv.org/abs/1508.05967
[11]: /html/1508.05968
