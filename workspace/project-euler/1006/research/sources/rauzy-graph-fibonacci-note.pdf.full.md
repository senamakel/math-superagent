<!-- source: https://ar5iv.labs.arxiv.org/html/2210.08629 | converted from HTML -->

[2210.08629] A Note On ℓ -Rauzy Graphs for the Infinite Fibonacci Word

# A Note On ℓ \ell -Rauzy Graphs for the Infinite Fibonacci Word

Rajavel Praveen M and Rama R
Department of Mathematics
Indian Institute of Technology Madras, Chennai - 600036, India
kingspearpraveen@gmail.com, ramar@iitm.ac.in

###### Abstract

The ℓ \ell -Rauzy graph of order k k for any infinite word is a directed graph in which an arc ( v 1, v 2) (v_{1},v_{2}) is formed if the concatenation of the word v 1 v_{1} and the suffix of v 2 v_{2} of length k − ℓ k-\ell is a subword of the infinite word. In this paper, we consider one of the important aperiodic recurrent words, the infinite Fibonacci word for discussion. We prove a few basic properties of the ℓ \ell -Rauzy graph of the infinite Fibonacci word. We also prove that the ℓ \ell -Rauzy graphs for the infinite Fibonacci word are strongly connected.

Keywords— Infinite words, Infinite Fibonacci word, Rauzy graphs, ℓ \ell -Rauzy graphs

## 1 Introduction

Theory of word representable graphs have main applications in Combinatorics, Graph theory, Computer science and Algebra [5, 8, 17]. This theory was first introduced by S. V. Kitaev and studied in detail [15] by the motivation of Perkins semigroup in [16]. A detailed survey is made by S. V. Kitaev and A. V. Pyatkin in [19]. Fundamental properties of word representable graphs are discussed in [15, 18].

A de Bruijn graph of order m m, is a directed graph with the vertex set Σ k \Sigma^{k} and u ​ v uv forms an arc iff u 2 u 3 ⋯ u k = v 1 v 2 ⋯ v k − 1 u_{2}u_{3}\cdots u_{k}=v_{1}v_{2}\cdots v_{k-1}. There are many interesting results like “For a de Bruijn graph of order k k whose | Σ | = 2 |\Sigma|=2 with 2 k 2^{k} vertices, there exists 2 2 k − 1 − k 2^{2^{k-1}-k} different Hamiltonian cycles” [12]. Finding Hamiltonian cycle in a graph is a difficult computational problem, where de Bruijn graph made it easier and it is widely applied in genome assembly [22].

In [23], Gerard Rauzy introduced a new graph by adding some more conditions to de Bruijn graph, called as Rauzy graph. The graph is defined with vertex set Σ k ∩ L ⁡ ( denote ​ Σ k ∩ L ​ by ​ L ​ ( k)) \Sigma^{k}\cap L(\text{denote}\Sigma^{k}\cap L\text{ by }L(k)) and an ordered pair ( u, v) (u,v) of vertices form an arc iff u 2 u 3 ⋯ u k = v 1 v 2 ⋯ v k − 1 u_{2}u_{3}\cdots u_{k}=v_{1}v_{2}\cdots v_{k-1} and u ​ v k ∈ L ⁡ ( k + 1) uv_{k}\in L(k+1). Here, L L denotes the factorial language, and Σ k \Sigma^{k} is the set of all words of length k k from the alphabet Σ \Sigma. Rauzy graphs are broadly used in finding the complexity of words of finite lengths. Arnoux and Rauzy in 1991, investigated the sequences with complexity 2 ​ n + 1 2n+1. And G. Rote in [24], went one step further to Arnoux and Rauzy by constructing the sequences with complexity 2 ​ n 2n using Rauzy graphs. Then Ali Aberkane in [2], approached similarly the intermediate case of complexity between n + 1 n+1 and 2 ​ n 2n.

In [13], Frid obtained a description of Rauzy graphs for a wide family of sequences. The author proved that to find the structure of Rauzy graphs for arbitrarily long lengths, it is sufficient to find a fixed number of Rauzy graphs for length bounded by a constant. In [3], Ali Aberkane studies the infinite words whose l ​ i ​ m ​ p ⁡ ( n) n = 1 lim\frac{p(n)}{n}=1, with the help of Rauzy graphs. Salimov in [26], proved that for a given sequence of strongly connected graphs with maximal in and out degrees equal to s s, an uniformly recurrent infinite word on Σ \Sigma, | Σ | = s |\Sigma|=s can be constructed. In the sequence of its Rauzy graphs, there is a subsequence of graphs isomorphic to the stretchings of graphs of the given sequence. In [4], Balková et al. proves that the factor frequency of infinite words whose language is closed under reversal does not exceed 2 ​ Δ ​ C ​ ( n) + 1 2\Delta C(n)+1.

Later in [21], we introduced a variant of Rauzy graph in which the vertex set is same as the Rauzy graph but any two vertices ( u, v) (u,v) form an arc iff u ⁡ [| u | 2 + 1, | u |] = v ⁡ [1, | v | 2] u[\frac{|u|}{2}+1,|u|]=v[1,\frac{|v|}{2}] i.e, half the length of the vertices are matched instead of | u | − 1 |u|-1 to form an arc. The idea of sharing half the length of vertex was motivated by the encoding procedure of vertices and edges in to DNA strand, proposed by Adleman in [1]. Some interesting structural properties of half range Rauzy graphs were studied in [21].

In this paper, we generalize the sharing length ℓ \ell of suffix/prefix in vertices to form an arc i.e., ( u, v) (u,v) forms an arc iff u ⁡ [| u | − ℓ + 1, | u |] = v ⁡ [1, ℓ] u[|u|-\ell+1,|u|]=v[1,\ell] and call it as ℓ − \ell- Rauzy graph. This is the generalization of Rauzy graphs and half range Rauzy graphs.

In [24], G. Rote proved that Rauzy graphs of any recurrent word are strongly connected. But, the ℓ \ell -Rauzy graph of any recurrent word need not be connected. For example, the 1 1 -Rauzy graph of order 4 4 for an infinite periodic word x ​ x ​ x ​ … xxx\ldots is not connected, where x x is a primitive word with alphabet size 2 2 and the length of x x is atleast 4. Also, the 2 2 -Rauzy graph of order 4 4 for the Thue-Morse word (an aperiodic recurrent infinite word) is not connected. We observe that the ℓ \ell -Rauzy graphs of the infinite Fibonacci word are strongly connected. So, we are interested in proving that the ℓ \ell -Rauzy graph of any order k ( ∈ N) k(\in N) for the well known infinite Fibonacci word is strongly connected.

Fibonacci word is one of the most studied infinite word in combinatorics on words as it has many combinatorial properties. Fibonacci words are defined by one of the simplest morphisms ϕ: 0 → 01 \phi:0\to 01, and 1 → 0 1\to 0. Fibonacci word is a Sturmian word whose subword complexity, σ ⁡ ( k) = k + 1 \sigma(k)=k+1. The subword complexity of the Fibonacci word is minimum among all aperiodic recurrent words. Fibonacci words are used to prove optimality of several results such as text algorithms and periodicity of infinite words. The finite Fibonacci words are considered as important as the Fibonacci numbers because of their applications.

In [10], Chuan uses Zeckendorf representation to obtain the locations of those subwords whose lengths are Fibonacci numbers ≥ 2 \geq 2. Later in [11], Chuan obtain the locations of any finite subword of the Infinite Fibonacci word. In [25], Rytter also obtains the location of any finite subword of the Infinite Fibonacci word in a different approach. The locations of any finite subword of the Infinite Fibonacci word can also be known by using the software Walnut. For more details about the Walnut software, one may refer [14]. Locations of the subwords plays a vital role in proving that the ℓ \ell -Rauzy graph of order k k for the infinite Fibonacci word is strongly connected for any k k and 1 ≤ ℓ ≤ k − 1 1\leq\ell\leq k-1.

## 2 Preliminaries

In this section, we present few basic and necessary definitions, for more details one can refer [20, 6, 9, 7]. A non empty collection of symbols is an alphabet Σ \Sigma. A sequence of finite or infinite symbols from Σ \Sigma forms a word. Length of a word w w is the number of letters in w w, denoted by l ⁡ ( w) l(w) and Σ ∗ \Sigma^{*} is the set of all finite words and Σ n \Sigma^{n} is the set of all words over Σ \Sigma of length n n. A word u u is a factor of w = w 1 ​ w 2 ​ … w=w_{1}w_{2}\ldots, if u = w i ​ w i + 1 ​ … ​ w i + k − 1 u=w_{i}w_{i+1}\ldots w_{i+k-1}, and is denoted by w ⁡ [i; k] w[i;k] for some i, k ∈ ℕ i,k\in\mathbbmss{N}. Here, w i w_{i} denotes the symbol in the i i th position of w w, and w ⁡ [i; k] w[i;k] is the word that starts at position i i and has length k k. Any factor u u is a prefix(suffix) of w w if w = u ​ x ​ ( w = x ​ u) w=ux(w=xu), x ∈ Σ ∗ x\in\Sigma^{*}.

A set L ⊆ Σ ∗ L\subseteq\Sigma^{*} is said to be a factorial language if it contains all the subwords of its words. Let L ⁡ ( k) = L ∩ Σ k L(k)=L\cap\Sigma^{k}, L w L_{w} be the set of all factors of w w and L w ​ ( k) L_{w}(k) be the set of all factors of w w of length k k.

Let g n g_{n} be the n n th Fibonacci word, where

 | g 0 = 1, g 1 = 0, g n = g n − 1 ​ g n − 2, n ≥ 2. g_{0}=1,~g_{1}=0,~g_{n}=g_{n-1}g_{n-2},~n\geq 2. |  |

The words g n g_{n} are referred to as the finite Fibonacci words. Let F n F_{n} be the n n th Fibonacci number, where | g n | = F n |g_{n}|=F_{n}. The limit f = lim n → ∞ g n f=\lim\limits_{n\to\infty}g_{n} is called the infinite Fibonacci word. The infinite Fibonacci word is given by

 | f = 010010100100101001010 ​ … f=010010100100101001010\ldots |  |

whose n n th letter is 1 ( r e s p., 0) 1~(resp.,~0) if ⌊ ( n + 1) τ ⌋ − ⌊ n τ ⌋ = 0 ( r e s p., 1), \lfloor(n+1)\tau\rfloor-\lfloor n\tau\rfloor=0~(resp.,~1), where τ = 5 − 1 2, n ≥ 1 \tau=\frac{\sqrt{5}-1}{2},n\geq 1 and the complement of infinite Fibonacci word is f c = 101101011011010110101 ​ … f^{c}=101101011011010110101\ldots.

A directed graph G G is an ordered pair ( V ⁡ ( G), E ⁡ ( G)) (V(G),E(G)) consisting of non empty set V ⁡ ( G) V(G) of vertices, a set E ⁡ ( G) E(G), disjoint from V ⁡ ( G) V(G), of arcs. In a graph G G, indegree (resp., outdegree) of a vertex u u is the number of arcs entering (resp., leaving) u u and denoted by d ​ e ​ g i ​ n ​ ( u) deg_{in}(u) (resp., d ​ e ​ g o ​ u ​ t ​ ( u) deg_{out}(u)). A vertex u u is isolated iff d ​ e ​ g i ​ n ​ ( u) = 0 = d ​ e ​ g o ​ u ​ t ​ ( u) deg_{in}(u)=0=deg_{out}(u).

A directed graph is said to be connected (weakly) if there is a path between any two vertices in its underlying undirected graph. A directed graph is said to be strongly connected if it has a path from each vertex to every other vertex. A loop (or self-loop) is an edge from a vertex to itself. Simple directed graphs are directed graphs that have no loops and no multiple arcs.

###### Definition 1.

A de Bruijn graph of order k > 1 k>1 is a directed graph whose vertex set is Σ k \Sigma^{k} and an arc u ​ v uv is formed iff

 | u ⁡ [2, k] = v ⁡ [1, k − 1] u[2,k]=v[1,k-1] |  |

Some more conditions on de Bruijn graph were imposed by Rauzy and defined a graph in the following way:

###### Definition 2.

A Rauzy graph of order k k for a factorial language L L is a directed graph ( V, E) (V,E) where V = L ⁡ ( k) V=L(k) and ( u, v) ∈ E (u,v)\in E iff

 | u 2 u 3 ⋯ u k = v 1 v 2 ⋯ v k − 1 a n d u 1 u 2 ⋯ u k v k ∈ L ( k + 1). u_{2}u_{3}\cdots u_{k}=v_{1}v_{2}\cdots v_{k-1}\hskip 18.49988ptand\hskip 18.49988ptu_{1}u_{2}\cdots u_{k}v_{k}\in L(k+1). |  |

A Rauzy graph of order k k for an infinite word w w is the Rauzy graph of order k k for the language of subwords of w w. We denote a Rauzy graph of order k k for a factorial language L L (for an infinite word w w) by R L ​ ( k) R_{L}(k) (correspondingly, R w ​ ( k) R_{w}(k)).

Later, a new graph is defined from Rauzy graph by sharing the suffix of preceding vertex with the prefix of succeeding vertex by half the length of its vertices [21].

###### Definition 3.

An ‘Half range Rauzy graph’(or and HRR-graph in short) of order k > 1 k>1, for a factorial language L L is a directed graph ( V, E) (V,E), where V = L ⁡ ( k) V=L(k) and arc set is defined as follows:

1. 1.

For an even k k, ( u, v) ∈ E (u,v)\in E iff

u k 2 + 1 u k 2 + 2 ⋯ u k = v 1 v 2 ⋯ v k 2 a n d u 1 u 2 ⋯ u k v k 2 + 1 ⋯ v k ∈ L ( 3 ​ k 2). u_{\frac{k}{2}+1}u_{\frac{k}{2}+2}\cdots u_{k}=v_{1}v_{2}\cdots v_{\frac{k}{2}}~and~u_{1}u_{2}\cdots u_{k}v_{\frac{k}{2}+1}\cdots v_{k}\in L(\frac{3k}{2}).

2. 2.

For an odd k k, there are two types of graphs, ( u, v) ∈ E (u,v)\in E iff

Type I: u k + 1 2 ⋯ u k = v 1 ⋯ v k + 1 2 a n d u 1 u 2 ⋯ u k v k + 3 2 ⋯ v k ∈ L ( 3 ​ k − 1 2) u_{\frac{k+1}{2}}\cdots u_{k}=v_{1}\cdots v_{\frac{k+1}{2}}~~and~~u_{1}u_{2}\cdots u_{k}v_{\frac{k+3}{2}}\cdots v_{k}\in L(\frac{3k-1}{2})

Type II: u k + 3 2 ⋯ u k = v 1 ⋯ v k − 1 2 a n d u 1 u 2 ⋯ u k v k + 1 2 ⋯ v k ∈ L ( 3 ​ k + 1 2) u_{\frac{k+3}{2}}\cdots u_{k}=v_{1}\cdots v_{\frac{k-1}{2}}~~and~~u_{1}u_{2}\cdots u_{k}v_{\frac{k+1}{2}}\cdots v_{k}\in L(\frac{3k+1}{2})

denoted by, ℍ ​ ℝ L ​ ( k, ∗) = { ℍ ​ ℝ L ​ ( k) i ​ f ​ k ​ i ​ s ​ e ​ v ​ e ​ n ℍ ​ ℝ L ​ ( k, I) i ​ f ​ k ​ i ​ s ​ o ​ d ​ d ​ a ​ n ​ d ​ T ​ y ​ p ​ e ​ I ℍ ​ ℝ L ​ ( k, I ​ I) i ​ f ​ k ​ i ​ s ​ o ​ d ​ d ​ a ​ n ​ d ​ T ​ y ​ p ​ e ​ I ​ I \mathbbmss{HR}_{L}(k,*)=\begin{cases}\mathbbmss{HR}_{L}(k)&if~k~is~even\\ \mathbbmss{HR}_{L}(k,I)&if~k~is~odd~and~Type~I\\ \mathbbmss{HR}_{L}(k,II)&if~k~is~odd~and~Type~II\end{cases}

If the underlying language is set of all factors of a given word w w, then ℍ ​ ℝ L ​ ( k, ∗) \mathbbmss{HR}_{L}(k,*) is simply represented as ℍ ​ ℝ w ​ ( k, ∗) \mathbbmss{HR}_{w}(k,*).

## 3 The ℓ \ell -Rauzy graph

Though, we were motivated by Adleman in [1], by matching half the length of DNA strands, the sharing length of suffix and prefix among the vertices made a difference in Rauzy graph and HRR (which is shown in [21]). Now, we are interested in the question “what if, we match an arbitrary length 1 ≤ ℓ ≤ k − 1 1\leq\ell\leq k-1 of suffix/prefix word among the vertices in a graph to form an arc?” On answering this question, a new graph ℓ − \ell- Rauzy graph is defined as follows and its properties are studied.

###### Definition 4.

An ℓ \ell -Rauzy graph of order k k for a factorial language L L is a directed graph ( V, E) (V,E) where V = L ⁡ ( k) V=L(k) and any two vertices u, v u,v forms an edge i.e. ( u, v) ∈ E (u,v)\in E iff

 | u k − ℓ + 1 u k − ℓ + 2 ⋯ u k = v 1 v 2 ⋯ v ℓ a n d u 1 u 2 ⋯ u k v ℓ + 1 v ℓ + 2 ⋯ v k ∈ L ( 2 k − ℓ) u_{k-\ell+1}u_{k-\ell+2}\cdots u_{k}=v_{1}v_{2}\cdots v_{\ell}~and~u_{1}u_{2}\cdots u_{k}v_{\ell+1}v_{\ell+2}\cdots v_{k}\in L(2k-\ell) |  |

is denoted by ℓ \ell - ℝ L ​ ( k) \mathbbmss{R}_{L}(k).

An ℓ \ell -Rauzy graph of order k k for an infinite word w w is the ℓ − \ell- Rauzy graph of order k k for the language of subwords of w w and denoted by ℓ \ell - ℝ w ​ ( k) \mathbbmss{R}_{w}(k).

###### Example 1.

The ℓ \ell -Rauzy graphs of order 4 4 for the word w = 010010010 ​ … w=010010010\ldots are directed graphs with vertex set V 1 = { v 1 = 0100, v 2 = 1001, v 3 = 0010 } V_{1}=\{v_{1}=0100,~v_{2}=1001,~v_{3}=0010\}, and the arc set varies for various ℓ \ell. The graph of ℓ \ell - R w ​ ( 4) R_{w}(4) is shown in Figure 1.

[image: Refer to caption] Figure 1: ℓ \ell -Rauzy graphs of order 4 for the word w w

###### Example 2.

ℓ \ell -Rauzy graphs of order 4 4 for the infinite Fibonacci word f f are directed graphs with vertex set V 2 = { u 1 = 0100, u 2 = 1001, u 3 = 0010, u 4 = 1010 } V_{2}=\{u_{1}=0100,~u_{2}=1001,~u_{3}=0010,~u_{4}=1010\}. For various ℓ \ell, graphs of ℓ \ell - R w ​ ( 4) R_{w}(4) are shown in Figure 2.

[image: Refer to caption] Figure 2: ℓ \ell -Rauzy graphs of order 4 for the infinite Fibonacci word f f

###### Example 3.

The 2 2 - Rauzy graph of order 4 4 for Thue-Morse infinite word T T is a directed graph with vertex set V 3 = { v 1 ′ = 0110, v 2 ′ = 1101, v 3 ′ = 1010, v 4 ′ = 0100, v 5 ′ = 1001, v 6 ′ = 0011, v 7 ′ = 1100, v 8 ′ = 0010, v 9 ′ = 0101, v 10 ′ = 1011 } V_{3}=\{v^{\prime}_{1}=0110,~v^{\prime}_{2}=1101,~v^{\prime}_{3}=1010,~v^{\prime}_{4}=0100,~v^{\prime}_{5}=1001,~v^{\prime}_{6}=0011,~v^{\prime}_{7}=1100,~v^{\prime}_{8}=0010,~v^{\prime}_{9}=0101,~v^{\prime}_{10}=1011\}. The graph 2 2 - R T ​ ( 4) R_{T}(4) is shown in Figure 3.

[image: Refer to caption] Figure 3: 2 2 -Rauzy graph of order 4 for the Thue-Morse infinite word T T

## 4 Properties of ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) for the Infinite Fibonacci word

In this section, we discuss a few basic properties of ℓ \ell -Rauzy graph for the infinite Fibonacci word.

By definition of ℓ \ell -Rauzy graph of order k k, the set of vertices is the set of all subwords of length k k in the factorial language L f ​ ( k) L_{f}(k) of infinite Fibonacci word f f. The subword complexity of fibonacci infinite word is well known and there are n + 1 n+1 number of subwords of length n n. Therefore, the number of vertices in ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) is given by

 | | V ⁡ ( ℓ ​ - ​ ℝ w ​ ( k)) | = k + 1. |V(\ell\text{-}\mathbbmss{R}_{w}(k))|=k+1. |  |

By definition of ℓ \ell -Rauzy graph for order k k, the set of arcs is the set of all subwords of length 2 ​ k − ℓ 2k-\ell in the factorial language L f ​ ( 2 ​ k − ℓ) L_{f}(2k-\ell) of infinite Fibonacci word f f. As there are 2 ​ k − ℓ + 1 2k-\ell+1 subwords of length 2 ​ k − ℓ 2k-\ell, the number of arcs in ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) is given by

 | | E ⁡ ( ℓ ​ - ​ ℝ f ​ ( k)) | = 2 ​ k − ℓ + 1. |E(\ell\text{-}\mathbbmss{R}_{f}(k))|=2k-\ell+1. |  |

The following proposition ensures that none of the vertices of ℓ \ell -Rauzy graph for the infinite Fibonacci word is isolated.

###### Proposition 1.

For each vertex v v in ℓ \ell -Rauzy graph for the infinite Fibonacci word, d ​ e ​ g i ​ n ​ ( v) ≥ 1 deg_{in}(v)\geq 1 and d ​ e ​ g o ​ u ​ t ​ ( v) ≥ 1 deg_{out}(v)\geq 1.

###### Proof.

Let v v be a word x i x i + 1 ⋯ x i + k − 1 x_{i}x_{i+1}\cdots x_{i+k-1} of length k k. As the infinite Fibonacci word is recurrent, there exist a

 | u = { x i − k + ℓ x i − k + ℓ + 1 ⋯ x i − 1 x i x i + 1 ⋯ x i + ℓ − 1 for i > k − ℓ x j − k + ℓ x j − k + ℓ + 1 ⋯ x j − 1 x j x j + 1 ⋯ x j + ℓ − 1 for i ≤ k − ℓ u=\begin{cases}x_{i-k+\ell}x_{i-k+\ell+1}\cdots x_{i-1}x_{i}x_{i+1}\cdots x_{i+\ell-1}&\text{for $i>k-\ell$}\\ x_{j-k+\ell}x_{j-k+\ell+1}\cdots x_{j-1}x_{j}x_{j+1}\cdots x_{j+\ell-1}&\text{for $i\leq k-\ell$}\end{cases} |  |

where x i x i + 1 ⋯ x i + k − 1 = x j x j + 1 ⋯ x j + k − 1 x_{i}x_{i+1}\cdots x_{i+k-1}=x_{j}x_{j+1}\cdots x_{j+k-1}, for some j > i + k − ℓ j>i+k-\ell and

 | u ′ = x i + ℓ ⋯ x i + k − 1 x i + k x i + k + 1 ⋯ x i + k + ℓ − 1 u^{\prime}=x_{i+\ell}\cdots x_{i+k-1}x_{i+k}x_{i+k+1}\cdots x_{i+k+\ell-1} |  |

such that ( u, v), ( v, u ′) ∈ E ⁡ ( ℓ CLOSE (u,v),(v,u^{\prime})\in E(\ell - OPEN ℝ w ​ ( k)) \mathbbmss{R}_{w}(k)). Hence d ​ e ​ g i ​ n ​ ( v) ≥ 1 deg_{in}(v)\geq 1 and d ​ e ​ g o ​ u ​ t ​ ( v) ≥ 1 deg_{out}(v)\geq 1. ∎

For given k k and ℓ \ell, the indegree and outdegree of any vertex in ℓ \ell - R f ​ ( k) R_{f}(k) can be known explicitly. Let k = F n + 1 − 1 k=F_{n+1}-1 and F n − 1 ≤ k − ℓ ≤ F n F_{n-1}\leq k-\ell\leq F_{n}. In ℓ \ell - R f ​ ( F n + 1 − 1) R_{f}(F_{n+1}-1), any vertex v j v_{j} that forms an arc with v i v_{i} is given by

 | v i → { v i + ( k − ℓ) for ​ 1 ≤ i ≤ F n + 1 − ( k − ℓ) v i + ( k − ℓ) − F n + 1 for ​ F n + 1 − ( k − ℓ) + 1 ≤ i ≤ F n + 1 v i + ( k − ℓ) − F n for ​ F n − ( k − ℓ) + 1 ≤ i ≤ F n v_{i}\rightarrow\begin{cases}v_{i+(k-\ell)}&\text{for}1\leq i\leq F_{n+1}-(k-\ell)\\ v_{i+(k-\ell)-F_{n+1}}&\text{for}F_{n+1}-(k-\ell)+1\leq i\leq F_{n+1}\\ v_{i+(k-\ell)-F_{n}}&\text{for}F_{n}-(k-\ell)+1\leq i\leq F_{n}\end{cases} |  |

The total number of arcs listed above are ( F n + 1 − ( k − ℓ)) + ( k − ℓ) + ( k − ℓ) = F n + 1 + ( k − ℓ) = 2 ​ k − ℓ + 1 (F_{n+1}-(k-\ell))+(k-\ell)+(k-\ell)=F_{n+1}+(k-\ell)=2k-\ell+1. The indegree and outdegree of any vertex can be known from the Figure 4.

For gievn k = F n + 1 − 1 k=F_{n+1}-1, k − ℓ < F n − 1 k-\ell<F_{n-1} and 2 ​ ( k − ℓ) < F n 2(k-\ell)<F_{n}, there exist no vertex v i v_{i} in the graph ℓ \ell - R f ​ ( F n + 1 − 1) R_{f}(F_{n+1}-1) such that d ​ e ​ g i ​ n ​ ( v i) = 2 = d ​ e ​ g o ​ u ​ t ​ ( v i) deg_{in}(v_{i})=2=deg_{out}(v_{i}).

[image: Refer to caption] Figure 4: Indegree and out degree of any vertex v i v_{i}

The ℓ \ell -Rauzy graph of order k k for the infinite Fibonacci word f f is isomorphic to the ℓ \ell -Rauzy graph of order k k for the complement of infinite Fibonacci word f c f^{c}. It is proved in the following proposition.

###### Proposition 2.

Let w = f w=f and w ′ = f c w^{\prime}=f^{c}. Then ℓ \ell - ℝ w ​ ( k) ≃ ℓ \mathbbmss{R}_{w}(k)\simeq\ell - ℝ w ′ ​ ( k), ∀ k ∈ ℕ \mathbbmss{R}_{w^{\prime}}(k),~\forall~k\in\mathbbmss{N}, 1 ≤ ℓ ≤ k − 1 1\leq\ell\leq k-1.

###### Proof.

If x ∈ V ⁡ ( ℓ CLOSE x\in V(\ell - OPEN ℝ w ​ ( k)) \mathbbmss{R}_{w}(k)) then x c ∈ ℓ x^{c}\in\ell - ℝ w ′ ​ ( k) \mathbbmss{R}_{w^{\prime}}(k). A morphism ϕ: ℓ \phi:\ell - ℝ w ​ ( k) → ℓ \mathbbmss{R}_{w}(k)\rightarrow\ell - ℝ w ′ ​ ( k) \mathbbmss{R}_{w^{\prime}}(k) is given by ϕ ⁡ ( x) = x c \phi(x)=x^{c}, where x ∈ V ⁡ ( ℓ CLOSE x\in V(\ell - OPEN ℝ w ​ ( k)) \mathbbmss{R}_{w}(k)). Also, the arcs ( u, v) ∈ E ⁡ ( ℓ CLOSE (u,v)\in E(\ell - OPEN ℝ w ​ ( k)) ⇔ ( u c, v c) ∈ E ⁡ ( ℓ CLOSE \mathbbmss{R}_{w}(k))\Leftrightarrow(u^{c},v^{c})\in E(\ell - OPEN ℝ w ′ ​ ( k)) \mathbbmss{R}_{w^{\prime}}(k)). Hence, ϕ \phi is an isomorphism and ℓ \ell - ℝ w ​ ( k) ≃ ℓ \mathbbmss{R}_{w}(k)\simeq\ell - ℝ w ′ ​ ( k) ​ ∀ k ∈ ℕ \mathbbmss{R}_{w^{\prime}}(k)~\forall~k\in\mathbbmss{N}. ∎

Any two ℓ \ell -Rauzy graphs for the infinite Fibonacci word are not isomorphic to each other, is proved in the following theorem.

###### Theorem 1.

The ℓ \ell - ℝ f ​ ( k 1) \mathbbmss{R}_{f}(k_{1}) is not isomorphic to ℓ ′ \ell^{\prime} - ℝ f ​ ( k 2) \mathbbmss{R}_{f}(k_{2}) for any k 1 ≠ k 2 k_{1}\neq k_{2} or ℓ ≠ ℓ ′ \ell\neq\ell^{\prime}.

###### Proof.

The ℓ \ell -Rauzy graph of infinite Fibonacci word ℓ \ell - ℝ f ​ ( k 1) \mathbbmss{R}_{f}(k_{1}) has | V 1 | = k 1 + 1 |V_{1}|=k_{1}+1 and | E 1 | = 2 ​ k 1 − ℓ + 1 |E_{1}|=2k_{1}-\ell+1 where as ℓ ′ \ell^{\prime} - ℝ f ​ ( k 2) \mathbbmss{R}_{f}(k_{2}) has | V 2 | = k 2 + 1 |V_{2}|=k_{2}+1 and | E 2 | = 2 ​ k 2 − ℓ ′ + 1 |E_{2}|=2k_{2}-\ell^{\prime}+1.

In the case 1 1: k 1 ≠ k 2 k_{1}\neq k_{2}, as the cardinality of vertex set of ℓ \ell - ℝ f ​ ( k 1) \mathbbmss{R}_{f}(k_{1}) is different from ℓ ′ \ell^{\prime} - ℝ f ​ ( k 2) \mathbbmss{R}_{f}(k_{2}), they are not isomorphic graphs.

In the case 2 2: k 1 = k 2 k_{1}=k_{2}, the cardinality of arc set of ℓ \ell - ℝ f ​ ( k 1) \mathbbmss{R}_{f}(k_{1}) is different from ℓ ′ \ell^{\prime} - ℝ f ​ ( k 2) \mathbbmss{R}_{f}(k_{2}), and so they are not isomorphic graphs.∎

We show that there exist a non-trivial bijection between the ℓ \ell -Rauzy graph and Rauzy graph of order k k for the infinite Fibonacci word f f, but not an isomorphism.

###### Theorem 2.

There exist a mapping ψ: ℓ \psi:\ell - ℝ f ​ ( k) → ℝ f ​ ( k) \mathbbmss{R}_{f}(k)\to\mathbbmss{R}_{f}(k) such that ψ \psi is a bijection.

###### Proof.

Let ψ: ℓ \psi:\ell - ℝ f ​ ( k) → ℝ f ​ ( k) \mathbbmss{R}_{f}(k)\to\mathbbmss{R}_{f}(k) be a mapping. By definition, V ⁡ ( ℓ CLOSE V(\ell - OPEN ℝ f ​ ( k)) = V ⁡ ( ℝ f ​ ( k)) = F ⁡ ( k) \mathbbmss{R}_{f}(k))=V(\mathbbmss{R}_{f}(k))=F(k). Each arc e ∈ E ⁡ ( ℓ CLOSE e\in E(\ell - OPEN ℝ f ​ ( k)) \mathbbmss{R}_{f}(k)) is a word of length 2 ​ k − ℓ 2k-\ell and each path v i v i + 1 ⋯ v i + k − ℓ v_{i}v_{i+1}\cdots v_{i+k-\ell} or e ′ i e ′ i + 1 ⋯ e ′ ( i − 1) + k − ℓ e^{\prime}_{i}e^{\prime}_{i+1}\cdots e^{\prime}_{(i-1)+k-\ell} in ℝ f ​ ( k) \mathbbmss{R}_{f}(k) is a word of length ( k + 1 + 1 + ⋯ + 1 ⏟ ( k − ℓ) ​ t ​ i ​ m ​ e ​ s) = 2 ​ k − ℓ (k+\underbrace{1+1+\cdots+1}_{(k-\ell)~times})=2k-\ell. Now, we map each arc e = v i ​ v i + k − ℓ e=v_{i}v_{i+k-\ell} in ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) to the path v i v i + 1 ⋯ v ( i − 1) + k − ℓ v i + k − ℓ v_{i}v_{i+1}\cdots v_{(i-1)+k-\ell}v_{i+k-\ell} or e ′ i e ′ i + 1 ⋯ e ′ ( i − 1) + k − ℓ e^{\prime}_{i}e^{\prime}_{i+1}\cdots e^{\prime}_{(i-1)+k-\ell}. The mapping ψ \psi is a bijection because E ⁡ ( ℓ CLOSE E(\ell - OPEN ℝ f ​ ( k)) = { P f ​ ( k − ℓ) } \mathbbmss{R}_{f}(k))=\{P_{f}(k-\ell)\}, where P f ​ ( k − ℓ) P_{f}(k-\ell) is the path of length ( k − ℓ) (k-\ell) in infinite Fibonacci word. ∎

In the above theorem, ψ \psi becomes an isomorphism only if it is a bijection mapping between the arc sets of ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) and ℝ f ​ ( k) \mathbbmss{R}_{f}(k). Here, we have given a bijection between the arc set of ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) and the { P f ​ ( k 2) } \{P_{f}(\frac{k}{2})\} i.e., the set of all paths of length ( k − ℓ) (k-\ell) in ℝ f ​ ( k) \mathbbmss{R}_{f}(k).

## 5 Main result

In this section, we prove that the ℓ \ell -Rauzy graph of order k k for the infinite Fibonacci word is strongly connected for any k, ℓ ∈ ℕ, 1 ≤ ℓ ≤ k − 1 k,\ell\in\mathbbmss{N},~1\leq\ell\leq k-1.

###### Theorem 3.

For a given k > 1, 1 ≤ ℓ ≤ k − 1 k>1,~1\leq\ell\leq k-1 and k, ℓ ∈ ℕ ~k,~\ell\in\mathbbmss{N}, the ℓ \ell -Rauzy graph of infinite Fibonacci word f f of order k k, i.e., ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) is strongly connected.

###### Proof.

For a given k > 1, 1 ≤ ℓ ≤ k − 1 k>1,~1\leq\ell\leq k-1 and k, ℓ ∈ ℕ ~k,~\ell\in\mathbbmss{N}, the distinct subwords of length k k in infinite Fibonacci word f f is the set of all vertices in ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k). It is well known that the number of subwords of Fibonacci infinite word of length k k is k + 1 k+1. Let the vertices of ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) be v 1, v 2, ⋯, v k, v k + 1 v_{1},~v_{2},\cdots,~v_{k},~v_{k+1}.

For a given k k, F n ≤ k ≤ F n + 1 F_{n}\leq k\leq F_{n+1}. From proposition 2.7 2.7 in [11], the first occurrences of k + 1 k+1 distinct factors of length k k are given by

 | v j = { f ⁡ [j; k] if ​ 1 ≤ j ≤ F n f ⁡ [j + F n + 1 − ( k + 1); k] if ​ F n + 1 ≤ j ≤ k + 1 v_{j}=\begin{cases}f[j;~k]&\text{if~~}1\leq j\leq F_{n}\\ f[j+F_{n+1}-(k+1);~k]&\text{if~~}F_{n}+1\leq j\leq k+1\end{cases} |  |

From corollary 3.6 3.6 and proposition 3.9 3.9 in [11], all the locations of v j v_{j} are given by

 | l ​ o ​ c. ( v j) = { { t ​ F n − 1 + ⌊ ( t + 1) ​ τ ⌋ ​ F n − 2 + j } if ​ 1 ≤ j ≤ F n + 1 − k − 1 { t ​ F n + ⌊ ( t + 1) ​ τ ⌋ ​ F n − 1 + j } if ​ F n + 1 − k ≤ j ≤ F n { t ​ F n + 1 + ⌊ ( t + 1) ​ τ ⌋ ​ F n + j + F n + 1 − ( k + 1) } if ​ F n + 1 ≤ j ≤ k + 1 loc.(v_{j})=\begin{cases}\{tF_{n-1}+\lfloor(t+1)\tau\rfloor F_{n-2}+j\}&\text{if~~}1\leq j\leq F_{n+1}-k-1\\ \{tF_{n}+\lfloor(t+1)\tau\rfloor F_{n-1}+j\}&\text{if~~}F_{n+1}-k\leq j\leq F_{n}\\ \{tF_{n+1}+\lfloor(t+1)\tau\rfloor F_{n}+j+F_{n+1}-(k+1)\}&\text{if~~}F_{n+1}\leq j\leq k+1\end{cases} |  |

where t ≥ 0 t\geq 0 in each of those sets. We see that locations of v j v_{j} for any j j is of the form

 | b ​ t + c ⁡ ⌊ ( t + 1) ​ τ ⌋ + d bt+c\lfloor(t+1)\tau\rfloor+d |  |

where b, c ∈ { F n − 2, F n − 1, F n, F n + 1 } b,~c\in\{F_{n-2},~F_{n-1},~F_{n},~F_{n+1}\} and d = j d=j or j + F n + 1 − ( k + 1) j+F_{n+1}-(k+1).

Let us consider the path ( s ​ a ​ y ​ P 1) (say~P_{1}) that starts from the subword of length k k, located in the first position of infinite Fibonacci word. By the definition of ℓ \ell -Rauzy graphs, the path P 1 P_{1} is given by

 | f ⁡ [1; k] → f ⁡ [1 + ( k − ℓ); k] → f ⁡ [1 + 2 ​ ( k − ℓ); k] → ⋯ → f ⁡ [1 + m ⁡ ( k − ℓ); k] → ⋯ f[1;k]\rightarrow f[1+(k-\ell);k]\rightarrow f[1+2(k-\ell);k]\rightarrow\cdots\rightarrow f[1+m(k-\ell);k]\rightarrow\cdots |  |

In path P 1 P_{1}, it is clear that any subword of the form f ⁡ [1 + m ⁡ ( k − ℓ); k] f[1+m(k-\ell);k] is reachable from f ⁡ [1; k] f[1;k] or v 1 v_{1}. If atleast one location of each vertex is of the form 1 + m ⁡ ( k − ℓ) 1+m(k-\ell), then every vertex is reachable from v 1 v_{1}.

The integer solutions to the equation

 | 1 + m ⁡ ( k − ℓ) = b ​ t + c ⁡ ⌊ ( t + 1) ​ τ ⌋ + d ​ for each 1 ≤ j ≤ k + 1 1+m(k-\ell)=bt+c\lfloor(t+1)\tau\rfloor+d\text{~~~~~~for each $1\leq j\leq k+1$} |  |

guarantee that atleast one location of each vertex is of the form 1 + m ⁡ ( k − ℓ) 1+m(k-\ell). Let x 1 = m, x 2 = t, x 3 = ⌊ ( t + 1) ​ τ ⌋ x_{1}=m,~x_{2}=t,~x_{3}=\lfloor(t+1)\tau\rfloor be the variables. The equation can be rewritten as

 | a ​ x 1 − b ​ x 2 − c ​ x 3 = d ′. ax_{1}-bx_{2}-cx_{3}=d^{\prime}. |  |

For each 1 ≤ j ≤ k + 1 1\leq j\leq k+1, the linear Diophantine equation a ​ x 1 − b ​ x 2 − c ​ x 3 = d ′ ax_{1}-bx_{2}-cx_{3}=d^{\prime} has infinite integer solutions ⇔ \iff g. c. d ( a, b, c) | d ′ g.c.d(a,b,c)|d^{\prime}.

It is well known that any two consecutive Fibonacci numbers are coprime, g. c. d ⁡ ( b, c) = 1 g.c.d(b,c)=1 for any 1 ≤ j ≤ k + 1 1\leq j\leq k+1, and so g. c. d ⁡ ( a, b, c) = 1 g.c.d(a,b,c)=1 that divides d ′ d^{\prime} always.

Now, it is clear that the equation a ​ x 1 − b ​ x 2 − c ​ x 3 = d ′ ax_{1}-bx_{2}-cx_{3}=d^{\prime} has infinite integer solutions for any 1 ≤ j ≤ k + 1 1\leq j\leq k+1. Thus, every vertex is reachable from v 1 v_{1} in the path P 1 P_{1}. As every vertex is located infinitely many times in the path P 1 P_{1}, the vertex v 1 v_{1} is reachable from any other vertex. Hence, ℓ \ell - ℝ f ​ ( k) \mathbbmss{R}_{f}(k) is strongly connected. ∎

However, the ℓ \ell -Rauzy graph of order k k for any recurrent word need not be connected. Figure 3 shows that the 2 2 -Rauzy graph of order 4 4 for the Thue-Morse word (aperiodic recurrent infinite word) is not connected.

## References

- [1] Adleman, L. M.: Molecular Computation of solutions to Combinatorial Problems. Science 266 (5187), 1021–1024, (1994)
- [2] Ali Aberkane: Exemples Suites de complexitié inférieure à 2 ​ n 2n. Bulletin of Belgium Mathematical Society 8 (2), 161–180 (2001)
- [3] Ali Aberkane: Words whose complexity satisfies lim p ⁡ ( n) n = 1 \frac{p(n)}{n}=1. Theoretical computer science 307 (1), 31–46 (2003)
- [4] L’ubomíra Balková and Edita pelantová: A note on symmetries in the Rauzy graph and factor frequencies. Theoretical Computer Science 410 (27-29), 2779–2783 (2009)
- [5] Beigel, R., Eppstein, D.: 3-Coloring in Time O(1.3289n). Journal of Algorithms 54 (2), 168–204 (2005)
- [6] Berthe, V., Rigo, M.(Editors): Combinatorics, Automata and Number theory. In series: Encyclopedia of Mathematics and its Applications, First edition. Cambridge University press, New york (2010)
- [7] Bondy, A., Murthy, M. R.: Graph Theory. Springer, India (2008)
- [8] Cerny, J.: Coloring Circle Graphs. Electronics Notes in Discrete Mathematics 29, 457–461 (2007)
- [9] Chartand, G., Lesniak, L., Zhang, P.: Graphs and Digraphs. Sixth edition. CRC press, 2016.
- [10] Chuan, W.: Subwords of golden sequence and the Fibonacci words. In: G. E. Bergum, A. N. Philippou, A. F. Horadam (Eds.), Applications of Fibonacci numbers 6, 73–84 (1996)
- [11] Chuan, W., Hui-Ling Ho: Locating factors of the infinite Fibonacci word, Theoretical Computer Science 349, 429–442 (2005)
- [12] De Bruijn, N. G.: A Combinatorial problem. In: Proceedings of Koninklijke Nederlandse Akademie van Wetenschappen, vol. 49, pp. 758–764 (1946)
- [13] Frid, A. E.: On factor graphs of D0L words. Discrete Applied Mathematics 114, 121–130 (2001)
- [14] Jeffrey Shallit: The Logical Approach to Automatic Sequences: Exploring Combinatorics on Words with Walnut, Cambridge University Press, (2022)
- [15] Kitaev, S., Pyatkin, A.: On Representable Graphs. Journal of Automata, Languages and Combinatorics 13 (1), 45–54 (2008)
- [16] Kitaev, S., Seif, S.: Word Problem of the Perkins Semigroup via Directed Acyclic Graphs. Order 25 (3), 177–194 (2008)
- [17] Kitaev, S., Lozin, V.: Words and Graphs. Springer, (2015)
- [18] Kitaev, S., Salimov, P., Severs, C., and Ulfarsson, H.: Word-representability and line graphs. Open Journal of Discrete Mathematics 1 (2), 96–101 (2011)
- [19] Kitaev, S. V., Pyatkin, A. V.: Word-Representable Graphs: a Survey. Journal of Applied and Industrial Mathematics 12 (2), 278–296 (2018)
- [20] Lothaire, M.: Algebraic combinatorics on words. In series: Encyclopedia of Mathematics and its Applications 90, Cambridge university press, (2002)
- [21] Mahalingam, K., Praveen, R., Rama, R.: On special Variant of Rauzy Graphs. Romanian Journal of Information and Technology 21 (3), 256–266 (2018)
- [22] Phillip E C Compeau, Pavel A Pevzner, and Glenn Tesler: How to apply de Bruijn graphs to genome assembly. Nature Biotechnology 29, 987–991 (2011)
- [23] Rauzy, G.: Suites à termes dans un alphabet fini. Seminar on Number Theory 25, 1–16, University of Bordeaux, Talence (1983)
- [24] Rote, G.: Sequences with subword complexity 2n. Journal of Number Theory 46, 196–213 (1993)
- [25] Rytter, W.: The structure of subword graph and suffix trees of Fibonacci words, Theoretical Computer Science 363, 211–223 (2006)
- [26] Salimov, P. V.: On Rauzy graph sequences of Infinite words. Journal of Applied and Industrial Mathematics 4 (1), 127–135 (2010)

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2210.08628
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2210.08629
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2210.08629
[7]: https://arxiv.org/pdf/2210.08629
[8]: /html/2210.08632
