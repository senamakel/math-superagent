<!-- source: https://arxiv.org/html/2507.10351v2 | converted from HTML -->

Leaf to leaf path lengths in trees of given degree sequence

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2507.10351v2 [math.CO] 24 Jul 2025

# Leaf to leaf path lengths in trees of given degree sequence

Dieter Rautenbach Johannes Scherer Florian Werner

###### Abstract

For a tree T T, let l ​ p ​ ( T) lp(T) be the number of different lengths of leaf to leaf paths in T T. For a degree sequence s s of a tree, let rad ⁡ ( s) {\rm rad}(s) be the minimum radius of a tree with degree sequence s s. Recently, Di Braccio, Katsamaktsis, Ma, Malekshahian, and Zhao provided a lower bound on l ​ p ​ ( T) lp(T) in terms of the number of leaves and the maximum degree of T T, answering a related question posed by Narins, Pokrovskiy, and Szabó. Here we show l ​ p ​ ( T) ≥ rad ⁡ ( s) − log 2 ⁡ ( rad ⁡ ( s)) lp(T)\geq{\rm rad}(s)-\log_{2}\left({\rm rad}(s)\right) for a tree T T with no vertex of degree 2 2 and degree sequence s s, and discuss possible improvements and variants.
Keywords: leaf to leaf path length

Institute of Optimization and Operations Research, Ulm University, Ulm, Germany
{ \{ dieter.rautenbach,johannes-1.scherer,florian.werner } \} @uni-ulm.de

## 1 Introduction

Let T T be a tree. A vertex of degree at most 1 1 in T T is a leaf of T T. A path in T T between leaves of T T is a leaf to leaf path in T T. Let l ​ p ​ ( T) lp(T) denote the number of different lengths of leaf to leaf paths in T T. Let rad ⁡ ( T) {\rm rad}(T) and diam ⁡ ( T) {\rm diam}(T) denote the radius and the diameter of T T, respectively.

For the construction of a counterexample to a conjecture of Erdős, Faudree, Gyárfás, and Schelp [2] concerning cycle lengths, Narins, Pokrovskiy, and Szabó [3] constructed trees with vertices of degrees 1 1 and 3 3 only that avoid leaf to leaf paths of certain lengths. Answering one of the related questions posed by Narins et al. in [3], Di Braccio et al. [1] proved the following.

###### Theorem 1 (Di Braccio et al. [1]).

If T T is a tree of maximum degree Δ \Delta at least 3 3 with ℓ \ell leaves, then

 | l ​ p ​ ( T) ≥ log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ). lp(T)\geq\log_{\Delta-1}((\Delta-2)\ell). |  |

Our goal is to generalize Theorem 1 in such a way that the lower bound on l ​ p ​ ( T) lp(T) depends on the degree sequence or the diameter of the tree T T. Recall that, for an integer n n at least 2 2, a sequence s = ( d 1, …, d n) s=(d_{1},\ldots,d_{n}) of n n positive integers is the degree sequence of some tree if and only if d 1 + ⋯ + d n = 2 ​ ( n − 1) d_{1}+\cdots+d_{n}=2(n-1). Typically, for a given degree sequence s = ( d 1, …, d n) s=(d_{1},\ldots,d_{n}) of some tree, there are many non-isomorphic trees with degree sequence s s. Let

 | rad ⁡ ( s) {\rm rad}(s) |  |

denote the minimum radius of a tree with degree sequence s s.

We pose the following conjecture.

###### Conjecture 2.

If s s is the degree sequence of a tree T T with no vertex of degree 2 2, then

 | l ​ p ​ ( T) ≥ rad ⁡ ( s) − O ⁡ ( 1). lp(T)\geq{\rm rad}(s)-O(1). |  |

Let Δ \Delta and h h be integers at least 3 3. If T Δ, h T_{\Delta,h} is the tree with vertices of degrees 1 1 and Δ \Delta only in which every leaf has distance h h from some fixed root vertex r r, then T Δ, h T_{\Delta,h} has ℓ = Δ ​ ( Δ − 1) h − 1 \ell=\Delta(\Delta-1)^{h-1} leaves. As observed by Di Braccio et al. [1], the trees T Δ, h T_{\Delta,h} show that Theorem 1 is essentially tight, because

 | l ​ p ​ ( T Δ, h) = | { 0, 2, …, 2 ​ h } | = h + 1 = ⌈ log Δ − 1 ⁡ ( ( Δ − 2) ​ ℓ) ⌉. lp(T_{\Delta,h})=|\{0,2,\ldots,2h\}|=h+1=\left\lceil\log_{\Delta-1}((\Delta-2)\ell)\right\rceil. |  |

It is easy to see that rad ⁡ ( s Δ, h) = h {\rm rad}(s_{\Delta,h})=h for the degree sequence s Δ, h s_{\Delta,h} of T Δ, h T_{\Delta,h}, which means that Conjecture 2 would be best possible up to the additive constant.

If s = ( d 1, …, d n) s=(d_{1},\ldots,d_{n}) is a given degree sequence of some tree with ordered entries d 1 ≥ … ≥ d n d_{1}\geq\ldots\geq d_{n}, then it is easy to see using simple exchange arguments that rad ⁡ ( s) {\rm rad}(s) can be determined efficiently by a simple greedy construction

- •

creating a 0 0 th layer L 0 L_{0} containing a center vertex r r of maximum degree d 1 d_{1},

- •

creating a 1st layer L 1 L_{1} attaching to r r exactly d 1 d_{1} neighbors of the largest possible degrees d 2, …, d 1 + d 1, d_{2},\ldots,d_{1+d_{1}},

- •

creating a 2nd layer L 2 L_{2} attaching ∑ u ∈ L 1 ( d T ​ ( u) − 1) = ( d 2 − 1) + ⋯ + ( d 1 + d 1 − 1) \sum\limits_{u\in L_{1}}(d_{T}(u)-1)=(d_{2}-1)+\cdots+(d_{1+d_{1}}-1) vertices of the largest possible degrees d 2 + d 1, …, d 1 + d 1 + ( d 2 − 1) + ⋯ + ( d 1 + d 1 − 1) d_{2+d_{1}},\ldots,d_{1+d_{1}+(d_{2}-1)+\cdots+(d_{1+d_{1}}-1)} to the neighbors of r r,

- •

and so forth.

The constructed tree has its vertices in layers L 0, L 1, …, L rad ⁡ ( s) L_{0},L_{1},\ldots,L_{{\rm rad}(s)}, each containing all vertices at a certain distance from the root vertex and this distance increases monotonically with the corresponding vertex degree. The number of vertices in each layer depends on the degrees of the vertices in the preceding layer. All leaves of the constructed tree have distance rad ⁡ ( s) {\rm rad}(s) or rad ⁡ ( s) − 1 {\rm rad}(s)-1 from r r.

If s s contains only entries 1 1 and Δ ≥ 3 \Delta\geq 3, then rad ⁡ ( s) {\rm rad}(s) is essentially log Δ − 1 ⁡ ( ℓ) \log_{\Delta-1}(\ell), where ℓ \ell is the number of 1 1 entries in s s, that is, Conjecture 2 generalizes Theorem 1 in the desired way. Our main result establishes Conjecture 2 up to a term of smaller order.

###### Theorem 3.

If s s is the degree sequence of some tree T T with no vertex of degree 2 2, then

 | l ​ p ​ ( T) ≥ rad ⁡ ( s) − log 2 ⁡ ( rad ⁡ ( s)). lp(T)\geq{\rm rad}(s)-\log_{2}\left({\rm rad}(s)\right). |  |

## 2 Proof of Theorem 3

For the proof of Theorem 3, it is convenient to consider rooted trees. For notational clarity, we consider rooted trees ( T, r) (T,r) as so-called out-trees, where all edges of T T are directed away from the root r r. If T T has degree sequence ( d 1, d 2, …, d n) (d_{1},d_{2},\ldots,d_{n}), where d 1 d_{1} is the degree of r r, then the rooted tree ( T, r) (T,r) has out-degree sequence ( d 1 +, d 2 +, …, d n +) = ( d 1, d 2 − 1, …, d n − 1) (d_{1}^{+},d_{2}^{+},\ldots,d_{n}^{+})=(d_{1},d_{2}-1,\ldots,d_{n}-1). In fact, a sequence s + = ( d 1 +, …, d n +) s^{+}=(d_{1}^{+},\ldots,d_{n}^{+}) of non-negative integers is the out-degree sequence of some rooted (out-)tree ( T, r) (T,r) if and only if d 1 + + ⋯ + d n + = n − 1 d_{1}^{+}+\cdots+d_{n}^{+}=n-1. A leaf in a rooted tree is a vertex without children. The depth of a vertex in a rooted tree is the distance from the root to that vertex and the height of a rooted tree is the maximum depth of a vertex. For a rooted tree ( T, r) (T,r) and a vertex u u in T T, the rooted subtree ( T u, u) (T_{u},u) of ( T, r) (T,r) at u u contains u u as its root as well as all descendants of u u in ( T, r) (T,r).

For an out-degree sequence s + s^{+} of some rooted tree, let

 | h ⁡ ( s +) {\rm h}(s^{+}) |  |

denote the minimum height of a rooted (out-)tree with out-degree sequence s + s^{+}. Given s + s^{+}, it is easy to see that h ⁡ ( s +) {\rm h}(s^{+}) can be determined efficiently by a similar greedy construction as explained above for rad ⁡ ( s) {\rm rad}(s). Furthermore, it is easy to see that

 | h ⁡ ( d 1, d 2 − 1, …, d n − 1) = rad ⁡ ( d 1, d 2, …, d n) \displaystyle{\rm h}(d_{1},d_{2}-1,\ldots,d_{n}-1)={\rm rad}(d_{1},d_{2},\ldots,d_{n}) |  | (1) |

for every degree sequence s = ( d 1, d 2, …, d n) s=(d_{1},d_{2},\ldots,d_{n}) with ordered entries d 1 ≥ … ≥ d n d_{1}\geq\ldots\geq d_{n}.

For a rooted tree ( T, r) (T,r), let l ​ p ​ ( T, r) = l ​ p ​ ( T) lp(T,r)=lp(T), where T T is the underlying undirected tree, that is, we ignore the orientations for the paths lengths counted by l ​ p ​ ( T, r) lp(T,r).

###### Lemma 4.

If ( T, r) (T,r) is a rooted tree with leaves of k k different depths, then l ​ p ​ ( T, r) ≥ k lp(T,r)\geq k.

###### Proof.

Since the statement is trivial for k = 1 k=1, we may assume k ≥ 2 k\geq 2. Let u 1, …, u k u_{1},\ldots,u_{k} be leaves of different depths in ( T, r) (T,r). Let v v be the lowest common ancestor of u 1, …, u k u_{1},\ldots,u_{k} in ( T, r) (T,r). Since k ≥ 2 k\geq 2, the vertex v v has at least 2 2 children. Let w w be a child of v v such that some u i u_{i} is in V ⁡ ( T w) V(T_{w}). Let

 | A \displaystyle A | = \displaystyle= | { dist T ​ ( v, u i): i ∈ [k] ​ and ​ u i ∈ V ⁡ ( T w) } ​ and \displaystyle\Big\{{\rm dist}_{T}(v,u_{i}):i\in[k]\mbox{ and }u_{i}\in V(T_{w})\Big\}\mbox{ and } |  |

 | B \displaystyle B | = \displaystyle= | { dist T ​ ( v, u i): i ∈ [k] ​ and ​ u i ∈ V ⁡ ( T v) ∖ V ⁡ ( T w) }. \displaystyle\Big\{{\rm dist}_{T}(v,u_{i}):i\in[k]\mbox{ and }u_{i}\in V(T_{v})\setminus V(T_{w})\Big\}. |  |

Clearly, the sets A A and B B are non-empty and | A ∪ B | = k |A\cup B|=k. Let A = { a 1, …, a c } A=\{a_{1},\ldots,a_{c}\} with a 1 < … < a c a_{1}<\ldots<a_{c} and B = { b 1, …, b d } B=\{b_{1},\ldots,b_{d}\} with b 1 < … < b d b_{1}<\ldots<b_{d}. Considering leaf to leaf paths over v v as well as one trivial leaf to leaf path of length 0 0, we obtain l ​ p ​ ( T, r) ≥ | A + B | + 1 lp(T,r)\geq|A+B|+1. Since A + B A+B contains at least c + d − 1 = k − 1 c+d-1=k-1 distinct sums

 | a 1 + b 1 < a 1 + b 2 < … < a 1 + b d < a 2 + b d < … < a c + b d, a_{1}+b_{1}<a_{1}+b_{2}<\ldots<a_{1}+b_{d}<a_{2}+b_{d}<\ldots<a_{c}+b_{d}, |  |

the statement follows. ∎

Let s + = ( d 1 +, …, d n +) s^{+}=(d_{1}^{+},\ldots,d_{n}^{+}) be the out-degree sequence of some rooted tree ( T, r) (T,r). Let ℓ \ell be the number of 0 0 entries of s + s^{+}, which equals the number of leaves of ( T, r) (T,r). For some k ∈ [ℓ] k\in[\ell], let

 | h ⁡ ( s +, k) h(s^{+},k) |  |

be the minimum height of a rooted tree ( T ^, r ^) (\hat{T},\hat{r}) with out-degree sequence s ^ + \hat{s}^{+} such that

- •

( T ^, r ^) (\hat{T},\hat{r}) has at least k k leaves and

- •

s ^ + \hat{s}^{+} is a subsequence of s + s^{+}, that is, the sequence s ^ + \hat{s}^{+} arises from s + s^{+} by removing entries.

###### Lemma 5.

Given s + s^{+} and k k as above.

1. (i)

h ⁡ ( s +, k) h(s^{+},k) is well-defined and increases monotonically in k k.

2. (ii)

h ⁡ ( s +, k) h(s^{+},k) can be determined efficiently.

3. (iii)

h ⁡ ( s +, k) ≤ h ⁡ ( s +, ⌈ k 2 ⌉) + 1 h(s^{+},k)\leq h\left(s^{+},\left\lceil\frac{k}{2}\right\rceil\right)+1.

###### Proof.

(i) Since ( T, r) (T,r) has ℓ \ell leaves and ℓ ≥ k \ell\geq k, the rooted tree ( T, r) (T,r) is a feasible choice for ( T ^, r ^) (\hat{T},\hat{r}), which implies that h ⁡ ( s +, k) h(s^{+},k) is well-defined. The monotonicity follows immediately from the definition.

(ii) We may assume that d 1 + ≥ … ≥ d n + d_{1}^{+}\geq\ldots\geq d_{n}^{+}. The definition of h ⁡ ( s +, k) h(s^{+},k) and simple exchange arguments imply that the non-zero entries of s ^ + \hat{s}^{+} can be chosen as an initial segment of s + s^{+}. More precisely, there is some p ∈ [n] p\in[n] with

 | s ^ + = ( d 1 +, …, d p +, 0, …, 0 ⏟ ≥ k). \hat{s}^{+}=(d_{1}^{+},\ldots,d_{p}^{+},\underbrace{0,\ldots,0}_{\geq k}). |  |

Since s ^ + \hat{s}^{+} is the out-degree sequence of some rooted tree, the number of 0 0 entries in s ^ + \hat{s}^{+} is exactly d 1 + + ⋯ + d p + − ( p − 1) d_{1}^{+}+\cdots+d_{p}^{+}-(p-1), which implies that p p can be chosen within [n] [n] as the smallest value for which d 1 + + ⋯ + d p + − ( p − 1) ≥ k d_{1}^{+}+\cdots+d_{p}^{+}-(p-1)\geq k. In particular, this choice implies that d p + ≥ 2 d_{p}^{+}\geq 2, that is, the sequence s ^ + \hat{s}^{+} contains no 1 1 entry. Clearly, for this specific choice of s ^ + \hat{s}^{+}, we have h ⁡ ( s +, k) = h ⁡ ( s ^ +) h(s^{+},k)=h(\hat{s}^{+}), which completes the proof of (ii).

(iii) We exploit the above observations. Again, let d 1 + ≥ … ≥ d n + d_{1}^{+}\geq\ldots\geq d_{n}^{+}. Let p, q ∈ [n] p,q\in[n] be smallest such that

 | d 1 + + ⋯ + d p + − ( p − 1) \displaystyle d_{1}^{+}+\cdots+d_{p}^{+}-(p-1) | ≥ \displaystyle\geq | k ​ and \displaystyle k\mbox{ and } |  |

 | k ′:= d 1 + + ⋯ + d q + − ( q − 1) \displaystyle k^{\prime}:=d_{1}^{+}+\cdots+d_{q}^{+}-(q-1) | ≥ \displaystyle\geq | ⌈ k 2 ⌉. \displaystyle\left\lceil\frac{k}{2}\right\rceil. |  |

Clearly, we have p ≥ q p\geq q and d p + ≥ 2 d^{+}_{p}\geq 2.

If k ′ ≥ k k^{\prime}\geq k, then

 | h ⁡ ( s +, k) = h ⁡ ( d 1 +, …, d q +, 0, …, 0 ⏟ = k ′ ≥ k) = h ⁡ ( s +, ⌈ k 2 ⌉). h(s^{+},k)=h(d_{1}^{+},\ldots,d_{q}^{+},\underbrace{0,\ldots,0}_{=k^{\prime}\geq k})=h\left(s^{+},\left\lceil\frac{k}{2}\right\rceil\right). |  |

Now, let k ′ < k k^{\prime}<k. If k ′ < p − q k^{\prime}<p-q, then

 | d 1 + + ⋯ + d q + k ′ + − ( q + k ′ − 1) \displaystyle d_{1}^{+}+\cdots+d_{q+k^{\prime}}^{+}-(q+k^{\prime}-1) | = \displaystyle= | d 1 + + ⋯ + d q + − ( q − 1) + ( d q + 1 + − 1) ⏟ ≥ 1 + ⋯ + ( d q + k ′ + − 1) ⏟ ≥ 1 ≥ 2 ​ k ′ ≥ k, \displaystyle d_{1}^{+}+\cdots+d_{q}^{+}-(q-1)+\underbrace{(d_{q+1}^{+}-1)}_{\geq 1}+\cdots+\underbrace{(d_{q+k^{\prime}}^{+}-1)}_{\geq 1}\geq 2k^{\prime}\geq k, |  |

contradicting the choice of p p. Hence, we obtain k ′ ≥ p − q k^{\prime}\geq p-q. Let ( T ^ ′, r ^) (\hat{T}^{\prime},\hat{r}) be a rooted tree of height h ⁡ ( s +, ⌈ k 2 ⌉) h\left(s^{+},\left\lceil\frac{k}{2}\right\rceil\right) with k ′ k^{\prime} leaves and out-degree sequence

 | ( d 1 +, …, d q +, 0, …, 0 ⏟ = k ′ ≥ ⌈ k / 2 ⌉). (d_{1}^{+},\ldots,d_{q}^{+},\underbrace{0,\ldots,0}_{=k^{\prime}\geq\lceil k/2\rceil}). |  |

If ( T ^, r ^) (\hat{T},\hat{r}) arises from ( T ^ ′, r ^) (\hat{T}^{\prime},\hat{r}) by selecting p − q p-q leaves of ( T ^ ′, r ^) (\hat{T}^{\prime},\hat{r}) and attaching to these leaves d q + 1 +, …, d p + d_{q+1}^{+},\ldots,d_{p}^{+} new leaves, respectively, then ( T ^, r ^) (\hat{T},\hat{r}) is of height at most h ⁡ ( s +, ⌈ k 2 ⌉) + 1 h\left(s^{+},\left\lceil\frac{k}{2}\right\rceil\right)+1, has k ′ + d q + 1 + + ⋯ + d p + − ( p − q) ≥ k k^{\prime}+d_{q+1}^{+}+\cdots+d_{p}^{+}-(p-q)\geq k leaves and out-degree sequence ( d 1 +, …, d p +, 0, …, 0) (d_{1}^{+},\ldots,d_{p}^{+},0,\ldots,0), which implies h ⁡ ( s +, k) ≤ h ⁡ ( s +, ⌈ k 2 ⌉) + 1 h(s^{+},k)\leq h\left(s^{+},\left\lceil\frac{k}{2}\right\rceil\right)+1. ∎

###### Lemma 6.

If ( T, r) (T,r) is a rooted tree with out-degree sequence s + s^{+} and U = { u 1, …, u k } U=\{u_{1},\ldots,u_{k}\} is a set of k k leaves of ( T, r) (T,r) that are all of equal depth, then there are leaf to leaf paths between vertices in U U of at least h ⁡ ( s +, k) + 1 h(s^{+},k)+1 different lengths. In particular, l ​ p ​ ( T, r) ≥ h ⁡ ( s +, k) + 1 lp(T,r)\geq h(s^{+},k)+1.

###### Proof.

The proof is by induction on k k. For k = 1 k=1, the trivial leaf to leaf path u 1 u_{1} of length 0 0 implies l ​ p ​ ( T, r) = 1 lp(T,r)=1. Since h ⁡ ( s +, 1) = 0 h(s^{+},1)=0, we have the desired inequality. Now, let k ≥ 2 k\geq 2. Let v v be the lowest common ancestor of u 1, …, u k u_{1},\ldots,u_{k}. Since k ≥ 2 k\geq 2, the vertex v v is not a leaf. Let d = d T + ​ ( v) d=d_{T}^{+}(v) and let w 1, …, w d w_{1},\ldots,w_{d} be the children of v v. For i ∈ [d] i\in[d], let ( T i, w i) (T_{i},w_{i}) be the rooted subtree of ( T, r) (T,r) at w i w_{i}, let s i + s_{i}^{+} be the out-degree sequence of ( T i, w i) (T_{i},w_{i}), let U i = { u 1, …, u k } ∩ V ⁡ ( T i) U_{i}=\{u_{1},\ldots,u_{k}\}\cap V(T_{i}), and let k i = | U i | k_{i}=|U_{i}|. Clearly, we have k 1 + ⋯ + k d = k k_{1}+\cdots+k_{d}=k and k i < k k_{i}<k for every i ∈ [d] i\in[d]. By reordering the children of v v, we may assume that k 1, …, k d ′ ≥ 1 k_{1},\ldots,k_{d^{\prime}}\geq 1 and k d ′ + 1 = … = k d = 0 k_{d^{\prime}+1}=\ldots=k_{d}=0 for some d ′ ∈ [d] ∖ { 1 } d^{\prime}\in[d]\setminus\{1\}.

If, for every i ∈ [d ′] i\in[d^{\prime}], the rooted tree ( T ^ i, w i) (\hat{T}_{i},w_{i}) of height h ⁡ ( s i +, k i) h(s_{i}^{+},k_{i}) has at least k i k_{i} leaves and an out-degree sequence that is a subsequence of s i + s_{i}^{+}, then the rooted tree ( T ^, v) (\hat{T},v) that arises

- •

from the disjoint union of v v, ( T ^ 1, w 1), …, ( T ^ d ′, w d ′) (\hat{T}_{1},w_{1}),\ldots,(\hat{T}_{d^{\prime}},w_{d^{\prime}}), and a set X X of d − d ′ d-d^{\prime} further vertices

- •

by adding the oriented edges ( v, w 1), …, ( v, w d ′) (v,w_{1}),\ldots,(v,w_{d^{\prime}}) as well as the oriented edges from v v to each element of X X

has height max ⁡ { h ⁡ ( s i +, k i): i ∈ [d ′] } + 1, \max\Big\{h(s_{i}^{+},k_{i}):i\in[d^{\prime}]\Big\}+1, at least k k leaves, and an out-degree sequence that is a subsequence of s + s^{+}. This implies

 | h ⁡ ( s +, k) ≤ max ⁡ { h ⁡ ( s i +, k i): i ∈ [d ′] } + 1. h(s^{+},k)\leq\max\Big\{h(s_{i}^{+},k_{i}):i\in[d^{\prime}]\Big\}+1. |  |

By symmetry, we may assume that h ⁡ ( s +, k) ≤ h ⁡ ( s 1 +, k 1) + 1 h(s^{+},k)\leq h(s_{1}^{+},k_{1})+1. By induction, the rooted tree ( T 1, w 1) (T_{1},w_{1}) contains leaf to leaf paths between the vertices in U 1 U_{1} of h ⁡ ( s 1 +, k 1) + 1 h(s_{1}^{+},k_{1})+1 different lengths. Since all leaves in U U have the same depth in ( T, r) (T,r), a leaf to leaf path between a vertex in U 1 U_{1} and a vertex in U 2 U_{2} is strictly longer than each of these paths, and we obtain leaf to leaf paths between vertices in U U of at least h ⁡ ( s 1 +, k 1) + 2 ≥ h ⁡ ( s +, k) + 1 h(s_{1}^{+},k_{1})+2\geq h(s^{+},k)+1 different lengths, which completes the proof. ∎

We are now in a position to prove Theorem 3.

###### Proof of Theorem 3.

Let s s and T T be as in the statement. Let s = ( d 1, …, d n) s=(d_{1},\ldots,d_{n}) with d 1 ≥ … ≥ d n d_{1}\geq\ldots\geq d_{n}. Rooting T T at a vertex r r of degree d 1 d_{1} yields a rooted tree ( T, r) (T,r) with out-degree sequence s + = ( d 1, d 2 − 1, …, d n − 1) s^{+}=(d_{1},d_{2}-1,\ldots,d_{n}-1). Let h = h ⁡ ( s +) h=h(s^{+}). By ( 1), it suffices to show l ​ p ​ ( T, r) ≥ h − log 2 ⁡ ( h) lp(T,r)\geq h-\log_{2}(h). Since s s has no 2 2 entry, the sequence s + s^{+} has no 1 1 entry, which easily implies h ⁡ ( s +) = h ⁡ ( s +, ℓ) h(s^{+})=h(s^{+},\ell). Let the number of 0 0 entries in s + s^{+} be ℓ \ell, that is, the tree T T and the rooted tree ( T, r) (T,r) both have exactly ℓ \ell leaves.

If ( T, r) (T,r) has leaves of h + 1 h+1 different depths, then Lemma 4 implies l ​ p ​ ( T, r) ≥ h + 1 lp(T,r)\geq h+1. Hence, we may assume that ( T, r) (T,r) has leaves of at most h h different depths only. By the pigeonhole principle, this implies that ( T, r) (T,r) has k ≥ ℓ h k\geq\frac{\ell}{h} leaves that are all of equal depth and Lemma 6 implies l ​ p ​ ( T, r) ≥ h ⁡ ( s +, k) + 1 lp(T,r)\geq h(s^{+},k)+1. For p = ⌊ log 2 ⁡ ( ℓ k) ⌋ p=\left\lfloor\log_{2}\left(\frac{\ell}{k}\right)\right\rfloor, we obtain ⌈ ℓ 2 ⌉ ≤ 2 p ​ k ≤ ℓ \left\lceil\frac{\ell}{2}\right\rceil\leq 2^{p}k\leq\ell, and Lemma 5 (i) and (iii) imply

 | h = h ⁡ ( s +) = h ⁡ ( s +, ℓ) ≤ ( i ​ i ​ i) h ⁡ ( s +, ⌈ ℓ 2 ⌉) + 1 ≤ ( i) h ⁡ ( s +, 2 p ​ k) + 1 ≤ ( i ​ i ​ i) h ⁡ ( s +, k) + p + 1 h=h(s^{+})=h(s^{+},\ell)\stackrel{{\scriptstyle(iii)}}{{\leq}}h\left(s^{+},\left\lceil\frac{\ell}{2}\right\rceil\right)+1\stackrel{{\scriptstyle(i)}}{{\leq}}h\left(s^{+},2^{p}k\right)+1\stackrel{{\scriptstyle(iii)}}{{\leq}}h(s^{+},k)+p+1 |  |

and, hence,

 | l ​ p ​ ( T, r) ≥ h ⁡ ( s +, k) + 1 ≥ h − p ≥ h − log 2 ⁡ ( ℓ k) ≥ h − log 2 ⁡ ( h), lp(T,r)\geq h(s^{+},k)+1\geq h-p\geq h-\log_{2}\left(\frac{\ell}{k}\right)\geq h-\log_{2}(h), |  |

which completes the proof. ∎

## 3 Conclusion

While it is natural to exclude vertices of degree 2 2 in this context, there is a version of Conjecture 2 including them: If s = ( d 1, …, d n) s=(d_{1},\ldots,d_{n}) is the degree sequence of a tree T T and s ′ = ( d 1, …, d n ′) s^{\prime}=(d_{1},\ldots,d_{n^{\prime}}) arises from s s by removing all entries equal to 2 2, then s ′ s^{\prime} is still the degree sequence of a tree and we conjecture l ​ p ​ ( T) ≥ rad ⁡ ( s ′) − O ⁡ ( 1). lp(T)\geq{\rm rad}(s^{\prime})-O(1). Next to Conjecture 2, we pose the problem to determine f ⁡ ( D) = inf { l ​ p ​ ( T): T ∈ 𝒯 ⁡ ( D) }, f(D)=\inf\{lp(T):T\in{\cal T}(D)\}, where 𝒯 ⁡ ( D) {\cal T}(D) is the set of all trees T T with no vertex of degree 2 2 and diameter diam ⁡ ( T) {\rm diam}(T) equal to D D. Results in [1] imply l ​ p ​ ( T) ≥ diam ​ ( T) 2 / 3 3 lp(T)\geq\frac{{\rm diam}(T)^{2/3}}{3} for a tree T T with no vertex of degree 2 2, which implies f ⁡ ( D) ≥ D 2 / 3 3 f(D)\geq\frac{D^{2/3}}{3}. We believe f ⁡ ( D) = o ⁡ ( D) f(D)=o(D).

We conclude with an observation related to Kraft’s inequality: If T T is a rooted binary tree with ℓ \ell leaves and 𝒲 {\cal W} is the multiset of all ( ℓ 2) {\ell\choose 2} path lengths of non-trivial leaf to leaf paths in T T, then a simple inductive argument shows ∑ w ∈ 𝒲 2 − w ≤ ℓ − 1 4 \sum\limits_{w\in{\cal W}}2^{-w}\leq\frac{\ell-1}{4} with equality if and only if T T is a full binary tree.

## References

- [1] F. Di Braccio, K. Katsamaktsis, J. Ma, A. Malekshahian, and Z. Zhao. Leaf-to-leaf paths and cycles in degree-critical graphs, arXiv:2504.11656.
- [2] P. Erdős, R. J. Faudree, A. Gyárfás, and R. H. Schelp. Cycles in graphs without proper subgraphs of minimum degree 3 3. Ars Combinatorica 25 (1988) 195-201.
- [3] L. Narins, A. Pokrovskiy, and T. Szabó. Graphs without proper subgraphs of minimum degree 3 3 and short cycles. Combinatorica 37 (2017) 495-519.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
