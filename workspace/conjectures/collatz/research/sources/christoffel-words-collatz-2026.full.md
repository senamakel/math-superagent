<!-- source: https://arxiv.org/html/2607.24844v1 | converted from HTML -->

Christoffel Words as Extremal Structures in Collatz Dynamics

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2607.24844v1 [math.DS] 24 Jul 2026

# Christoffel Words as Extremal Structures in Collatz Dynamics

Carlos Fernández Thanks: Departamento de Matemáticas, University of Oviedo, E-33007 Oviedo, Spain.
carlos@uniovi.es Santiago Ibáñez Thanks: Departamento de Matemáticas, University of Oviedo, E-33007 Oviedo, Spain.
mesa@uniovi.es

July 2026

###### Abstract

We study the combinatorial structure of parity sequences associated with the accelerated Collatz map with the goal of identifying extremal configurations and relating them to the existence of periodic orbits. To each finite sequence of an orbit, we associate a binary word whose ones encode the odd iterates, and we introduce a functional C ⁡ ( d) C(d) on such words which provides an explicit expression for the iterates and characterizes possible periodic cycles. We define a natural rotation action on binary words, compatible with the cyclic structure of periodic orbits, and consider the functional C min ​ ( d) C_{\min}(d) as a canonical representative of each rotation class. In this setting, we formulate and solve a discrete optimization problem on the set of binary words of fixed length and prescribed density.

We prove that Christoffel words are, up to rotation, the unique maximizers of C min ​ ( d) C_{\min}(d) on D N, r D_{N,r}, the set of binary words of length N N with exactly r r ones, thereby establishing a direct connection between the dynamics of the Collatz problem and the classical theory of balanced words. As a consequence, we obtain restrictions on the possible existence of nontrivial cycles and derive explicit bounds for the minimum element of an orbit in terms of its length and the proportion of odd iterates. These results show that the combinatorial structure of parity sequences imposes strong constraints on Collatz dynamics and suggest that extremal configurations are governed by classical objects from the combinatorics on words, exhibiting a pronounced structural rigidity.

## 1 Introduction

The Collatz problem, despite its elementary formulation, conceals a rich combinatorial structure. In this paper we take a parity - sequence viewpoint and relate the binary words that encode Collatz orbits to classical objects such as Christoffel words, which also appear in optimal scheduling, digital geometry, and Sturmian sequences.

Let

 | ϕ ⁡ ( x) = { x / 2, x ≡ 0 ( mod 2), ( 3 ​ x + 1) / 2, x ≡ 1 ( mod 2), \phi(x)=\begin{cases}x/2,&x\equiv 0\pmod{2},\\ (3x+1)/2,&x\equiv 1\pmod{2},\end{cases} |  | (1) |

be defined on the set of positive integers. The Collatz conjecture asserts that for every x ∈ ℕ x\in\mathbb{N} there exists N ≥ 0 N\geq 0 such that ϕ N ​ ( x) = 1 \phi^{N}(x)=1. A classical approach to this problem is to study the possible existence of periodic orbits other than the trivial 2-cycle 1 ↔ 2 1\leftrightarrow 2. Terras [1] showed that ϕ N ​ ( x) \phi^{N}(x) can be expressed explicitly in terms of the parity sequence ( d 1, …, d N) (d_{1},\dots,d_{N}), where d i ∈ { 0, 1 } d_{i}\in\{0,1\} records the parity of the ( i − 1) (i-1) -th iterate: d i = 0 d_{i}=0 if ϕ i − 1 ​ ( x) \phi^{i-1}(x) is even, and d i = 1 d_{i}=1 if it is odd. This encoding links the study of the dynamics to the combinatorial analysis of binary words.

The dynamics of the Collatz map has been the subject of extensive investigation since the pioneering work of L. Collatz in the 1930s. Early contributions by Terras and Everett studied stopping times and structural properties of the iteration [1, 2], while Lagarias provided a systematic account of the problem and its variants [3, 4]. More recent advances include density bounds, probabilistic models, and almost-everywhere results; see, for instance, [7, 8, 9, 10].

From a combinatorial viewpoint, it is natural to encode orbits by binary words associated with the parity of the iterates. This perspective has been developed explicitly in recent work on parity vectors: Rajab [11] introduces characteristic numbers associated with parity vectors that share a similar flavour with the functional C ⁡ ( d) C(d) studied here, while Rozier [12] analyzes order relations on binary words that are closely related to the local transformations we use in Section 5. This places the problem in the framework of combinatorics on words and symbolic dynamics, where classical objects such as Sturmian and Christoffel words naturally appear [13, 5].

On the other hand, the analysis of nontrivial cycles has led to the introduction of functionals associated with parity sequences, which allow one to formulate the existence of periodic orbits in terms of precise arithmetic conditions. Such ideas are already implicit in the work of Terras [1] and have been further developed from different points of view; see, for instance, [3, 11].

Problems of this type, involving discrete optimization over binary words of fixed length and density, have been extensively studied in combinatorics on words, where Christoffel words and, more generally, Sturmian words appear as extremal configurations characterized by optimal balance and regularity properties [5, 14, 13]. Up to the recent contribution [15], a paper we discovered only after our work was completed, and to the best of our knowledge, this connection has not been systematically developed in the specific context of the Collatz problem. However, the explicit form of the functionals associated with parity sequences—in particular, their exponential dependence on the distribution of symbols—justifies the optimization problems that give rise to these structures.

In this context, the present work lies at the intersection of the arithmetic dynamics of the Collatz map and the combinatorics on words. We introduce a functional C ⁡ ( d) C(d) associated with parity sequences, define a rotation-invariant version C min ​ ( d) C_{\min}(d), and prove that Christoffel words are, up to rotation, the unique maximizers of C min ​ ( d) C_{\min}(d) on D N, r D_{N,r}, the set of binary words of length N N with exactly r r ones. As a consequence, we derive explicit restrictions on the existence of nontrivial periodic orbits, including the bound

 | x ≤ 1 2 N / r − 3 x\leq\frac{1}{2^{N/r}-3} |  |

(valid for N / r > log 2 ⁡ 3 N/r>\log_{2}3, which is a necessary condition for the existence of a periodic orbit) on the minimum element, x x, of a cycle of length N N with r r odd iterates, and show that no nontrivial cycle can satisfy N ≥ 2 ​ r N\geq 2r.

The paper is organized as follows. In Section 2 we introduce parity sequences and the functional C ⁡ ( d) C(d). Section 3 studies the rotation action and defines C min ​ ( d) C_{\min}(d). Christoffel words are recalled in Section 4. Local transformations and the induced partial order are analyzed in Section 5, and the combinatorial structure of minimizers is developed in Section 6. The main maximization theorem is proved in Section 7, and its consequences for Collatz dynamics are derived in Section 8.

## 2 Parity sequences

Let 𝒟 N = { 0, 1 } N \mathcal{D}_{N}=\{0,1\}^{N} denote the set of binary words of length N N. Given 0 ≤ r ≤ N 0\leq r\leq N, we define the subset

 | 𝒟 N, r = { d = ( d 1, …, d N) ∈ 𝒟 N: ∑ j = 1 N d j = r }, \mathcal{D}_{N,r}=\left\{d=(d_{1},\dots,d_{N})\in\mathcal{D}_{N}:\sum_{j=1}^{N}d_{j}=r\right\}, |  |

that is, the set of all binary words of length N N with exactly r r ones.

Given x ∈ ℕ x\in\mathbb{N}, consider the orbit x, ϕ ⁡ ( x), ϕ 2 ​ ( x), …, ϕ N − 1 ​ ( x) x,\phi(x),\phi^{2}(x),\dots,\phi^{N-1}(x), with ϕ \phi as given in ( 1). We associate to it the binary word d = ( d 1, …, d N) d=(d_{1},\dots,d_{N}) defined by

 | d i = δ 1 ​ ( 2) ​ ( ϕ i − 1 ​ ( x)) ∈ { 0, 1 }, d_{i}=\delta_{1(2)}\!\left(\phi^{i-1}(x)\right)\in\{0,1\}, |  |

where δ 1 ​ ( 2) ​ ( n) = 0 \delta_{1(2)}(n)=0, if n n is even, and 1 1, if it is odd. In this way, each initial sequence of length N N of a Collatz orbit determines a binary word in 𝒟 N, r 0 ​ ( d) \mathcal{D}_{N,r_{0}(d)}.

For each i = 0, …, N i=0,\dots,N, we define

 | r i ​ ( d) = ∑ j = i + 1 N d j, r_{i}(d)=\sum_{j=i+1}^{N}d_{j}, |  |

with the convention r N ​ ( d) = 0 r_{N}(d)=0. Thus r 0 ​ ( d) = r r_{0}(d)=r is the total number of ones in d d, and r i ​ ( d) r_{i}(d) counts the ones strictly to the right of position i i.

Following the classical formula of Terras [1], the N N -th iterate of ϕ \phi satisfies

 | ϕ N ​ ( x) = 3 r 0 ​ ( d) 2 N ​ x + ∑ i = 1 N 3 r i ​ ( d) 2 N − i + 1 ​ d i. \phi^{N}(x)=\frac{3^{r_{0}(d)}}{2^{N}}\,x+\sum_{i=1}^{N}\frac{3^{r_{i}(d)}}{2^{N-i+1}}\,d_{i}. |  | (2) |

If x x belongs to a periodic orbit of period N N, then ϕ N ​ ( x) = x \phi^{N}(x)=x, and ( 2) gives

 | x = C ⁡ ( d) 2 N − 3 r 0 ​ ( d), x=\frac{C(d)}{2^{N}-3^{r_{0}(d)}}, |  | (3) |

where

 | C ⁡ ( d) = ∑ i = 1 N 2 i − 1 ​ 3 r i ​ ( d) ​ d i. C(d)=\sum_{i=1}^{N}2^{i-1}\,3^{r_{i}(d)}\,d_{i}. |  | (4) |

This representation of the iterates in terms of the parity sequence appears already in [1] and has been used extensively in the subsequent literature to translate dynamical properties of the Collatz map into arithmetic and combinatorial conditions on binary words; see also [3, 11].

The quantity r i ​ ( d) r_{i}(d) admits a natural combinatorial interpretation: it counts the number of ones strictly to the right of position i i, that is,

 | r i ​ ( d) = #⁡ { j ∈ I ⁡ ( d): j > i }, r_{i}(d)=\#\{\,j\in I(d):j>i\,\}, |  |

where I ⁡ ( d) = { i ∈ { 1, …, N }: d i = 1 } I(d)=\{\,i\in\{1,\dots,N\}:d_{i}=1\,\} is the set of positions of the ones in d d. In particular, r i ​ ( d) r_{i}(d) can be interpreted as the number of odd iterates remaining after step i i, so that the functional C ⁡ ( d) C(d) depends on the distribution of the ones in d d in a global, rather than local, manner.

## 3 Rotations

Suppose that the binary word d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} arises from a periodic orbit of ϕ \phi of period N N. Since the choice of base point along the orbit is not canonical, it is natural to introduce an action on 𝒟 N, r \mathcal{D}_{N,r} that models this change of reference. We define the *rotation operator*τ: 𝒟 N → 𝒟 N \tau:\mathcal{D}_{N}\to\mathcal{D}_{N} by

 | τ ⁡ ( d 1, d 2, …, d N) = ( d 2, d 3, …, d N, d 1), \tau(d_{1},d_{2},\dots,d_{N})=(d_{2},d_{3},\dots,d_{N},d_{1}), |  |

and denote by τ j \tau^{j} its j j -th iterate, with τ 0 = id \tau^{0}=\mathrm{id}. The map τ \tau is a bijection of order dividing N N, so in particular τ N = id \tau^{N}=\mathrm{id}, and it defines an action of the cyclic group ℤ / N ​ ℤ \mathbb{Z}/N\mathbb{Z} on 𝒟 N, r \mathcal{D}_{N,r}.

If x x belongs to a periodic orbit of period N N with associated parity word d d, then choosing a different base point along the orbit yields the word τ j ​ ( d) \tau^{j}(d) for some j ∈ { 0, …, N − 1 } j\in\{0,\dots,N-1\}. Consequently, the words associated with a given cycle form a single orbit under the action of τ \tau, and any quantity intended to describe intrinsic properties of the cycle must be invariant under this action.

The functional C ⁡ ( d) C(d) defined in ( 4), however, depends on the choice of base point. It is therefore natural to pass to the rotation-invariant quantity

 | C min ​ ( d) = min 0 ≤ j ≤ N − 1 ⁡ C ⁡ ( τ j ​ ( d)), C_{\min}(d)=\min_{0\leq j\leq N-1}C(\tau^{j}(d)), |  | (5) |

which is well defined on rotation classes and provides a canonical representative of the equivalence class of d d under τ \tau.

###### Remark 3.1.

From a dynamical viewpoint, C min ​ ( d) C_{\min}(d) corresponds to choosing the base point in the orbit for which the numerator C ⁡ ( d) C(d) in the expression

 | x = C ⁡ ( d) 2 N − 3 r x=\frac{C(d)}{2^{N}-3^{r}} |  |

is minimized. Note that 2 N ≠ 3 r 2^{N}\neq 3^{r} for all N, r ∈ ℕ N,r\in\mathbb{N} with r ≥ 1 r\geq 1, since log 2 ⁡ 3 \log_{2}3 is irrational, so the denominator is always nonzero. This is a standard procedure in the study of the Collatz problem, where quantities associated with parity vectors depend on the choice of base point and it is natural to consider extremal representatives to obtain well-defined invariants; see, for example, [1, 3].

Now, observe that the expression x = C ⁡ ( d) 2 N − 3 r x=\frac{C(d)}{2^{N}-3^{r}} can be considered for any binary word d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r}, regardless of whether it actually comes from a periodic orbit of the Collatz map. In particular, if the corresponding value of x x is not a positive integer, we must conclude that there is no periodic Collatz orbit whose parity pattern is encoded by d d.

On the other hand, it is clear that C C induces an order on 𝒟 N, r \mathcal{D}_{N,r}. The question we ask is therefore the following: does there exist a pair ( N, r) (N,r) for which

 | max d ∈ 𝒟 N, r ⁡ C min ​ ( d) < 2 N − 3 r ​? \max_{d\in\mathcal{D}_{N,r}}C_{\min}(d)<2^{N}-3^{r}? |  |

In other words, we seek to characterize those pairs ( N, r) (N,r) for which the quotient

 | C min ​ ( d) 2 N − 3 r \frac{C_{\min}(d)}{2^{N}-3^{r}} |  |

is always strictly less than one for every d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r}, and hence no periodic orbit with that parity structure can exist.

From a combinatorial viewpoint, the problem consists in studying the behaviour of C min ​ ( d) C_{\min}(d) over 𝒟 N, r \mathcal{D}_{N,r}. This leads to a discrete optimization problem: for fixed N N and r r, determine which binary words in 𝒟 N, r \mathcal{D}_{N,r} maximize C min ​ ( d) C_{\min}(d). The density r / N r/N plays a particularly relevant role, as it can be interpreted as the slope associated with the word, in the sense of the theory of Sturmian and Christoffel words [13, 5].

## 4 Christoffel words

The Christoffel word of parameters ( N, r) (N,r) can be defined by means of several equivalent conventions. In this work we adopt the following.

###### Definition 4.1.

Let N ≥ 1 N\geq 1 and 0 ≤ r ≤ N 0\leq r\leq N. The *Christoffel word*of parameters ( N, r) (N,r) is the binary word d N, r chr = ( d 1, …, d N) ∈ 𝒟 N, r d^{\mathrm{chr}}_{N,r}=(d_{1},\dots,d_{N})\in\mathcal{D}_{N,r} defined by

 | d i = ⌈ i ​ r N ⌉ − ⌈ ( i − 1) ​ r N ⌉, i = 1, …, N. d_{i}=\left\lceil\frac{i\,r}{N}\right\rceil-\left\lceil\frac{(i-1)\,r}{N}\right\rceil,\qquad i=1,\dots,N. |  | (6) |

This definition is equivalent, up to a rotation (and, in some cases, an elementary reflection), to the more standard definition based on the floor function; see [13]. We adopt ( 6) because it is well suited to the analysis of the positions of the ones carried out in Sections 6 and 7.

These words provide a balanced distribution of the ones along the word, characterized by optimal regularity properties with respect to the density r / N r/N. More precisely, Christoffel words are the unique balanced words of given length and density, up to rotation [5]. Recall that a binary word is *balanced*if for any two factors or subsequences of the same length, the numbers of ones differ by at most one. They constitute a classical object in combinatorics on words and symbolic dynamics; see [5, 13, 14] for systematic accounts.

In the context of the Collatz problem, where the dynamics can be encoded by parity vectors [1, 11], it is natural to expect that such balanced structures play a relevant role in the study of functionals such as C ⁡ ( d) C(d). Since C ⁡ ( d) C(d) depends on the distribution of the ones in a non-local manner, optimal configurations must avoid local concentrations of ones, favouring distributions that are as uniform as possible. This leads naturally to Christoffel words as the candidates to maximize C min ​ ( d) C_{\min}(d) within each class 𝒟 N, r \mathcal{D}_{N,r}.

The main result of this paper, proved in Section 7, confirms this expectation: Christoffel words are, up to rotation, the unique maximizers of C min ​ ( d) C_{\min}(d) on 𝒟 N, r \mathcal{D}_{N,r}.

## 5 Local transformations

We now study the behaviour of C ⁡ ( d) C(d) under local transformations of the binary word. We begin with a preliminary result.

###### Proposition 5.1.

Let d 1 ∈ 𝒟 N 1 d_{1}\in\mathcal{D}_{N_{1}} and d 2 ∈ 𝒟 N 2 d_{2}\in\mathcal{D}_{N_{2}}. Then

 | C ⁡ ( [d 1, d 2]) = 3 r 0 ​ ( d 2) ​ C ​ ( d 1) + 2 N 1 ​ C ​ ( d 2). C([d_{1},d_{2}])=3^{r_{0}(d_{2})}\,C(d_{1})+2^{N_{1}}\,C(d_{2}). |  | (7) |

###### Proof.

Let d = [d 1, d 2] d=[d_{1},d_{2}] be the concatenation of both words. Separating the sum defining C ⁡ ( d) C(d) into the contributions of d 1 d_{1} and d 2 d_{2}, we obtain

 | C ⁡ ( d) = ∑ i = 1 N 1 2 i − 1 ​ 3 r i ​ ( d) ​ d i + ∑ i = N 1 + 1 N 1 + N 2 2 i − 1 ​ 3 r i ​ ( d) ​ d i. C(d)=\sum_{i=1}^{N_{1}}2^{i-1}3^{r_{i}(d)}\,d_{i}+\sum_{i=N_{1}+1}^{N_{1}+N_{2}}2^{i-1}3^{r_{i}(d)}\,d_{i}. |  |

For i ≤ N 1 i\leq N_{1} we have

 | r i ​ ( d) = r i ​ ( d 1) + r 0 ​ ( d 2), r_{i}(d)=r_{i}(d_{1})+r_{0}(d_{2}), |  |

while for i > N 1 i>N_{1}, writing j = i − N 1 j=i-N_{1}, we have

 | r i ​ ( d) = r j ​ ( d 2). r_{i}(d)=r_{j}(d_{2}). |  |

Substituting into the expression above gives

 | ∑ i = 1 N 1 2 i − 1 ​ 3 r i ​ ( d) ​ d i = 3 r 0 ​ ( d 2) ​ ∑ i = 1 N 1 2 i − 1 ​ 3 r i ​ ( d 1) ​ d i = 3 r 0 ​ ( d 2) ​ C ​ ( d 1), \sum_{i=1}^{N_{1}}2^{i-1}3^{r_{i}(d)}\,d_{i}=3^{r_{0}(d_{2})}\sum_{i=1}^{N_{1}}2^{i-1}3^{r_{i}(d_{1})}\,d_{i}=3^{r_{0}(d_{2})}\,C(d_{1}), |  |

and

 | ∑ i = N 1 + 1 N 1 + N 2 2 i − 1 ​ 3 r i ​ ( d) ​ d i = 2 N 1 ​ ∑ j = 1 N 2 2 j − 1 ​ 3 r j ​ ( d 2) ​ d j = 2 N 1 ​ C ​ ( d 2). \sum_{i=N_{1}+1}^{N_{1}+N_{2}}2^{i-1}3^{r_{i}(d)}\,d_{i}=2^{N_{1}}\sum_{j=1}^{N_{2}}2^{j-1}3^{r_{j}(d_{2})}\,d_{j}=2^{N_{1}}\,C(d_{2}). |  |

Therefore C ⁡ ( [d 1, d 2]) = 3 r 0 ​ ( d 2) ​ C ​ ( d 1) + 2 N 1 ​ C ​ ( d 2) C([d_{1},d_{2}])=3^{r_{0}(d_{2})}\,C(d_{1})+2^{N_{1}}\,C(d_{2}). ∎

The concatenation formula ( 7) allows us to compare words that differ only in the order of appearance of certain symbols, and will be used to establish an order under local transpositions.

###### Proposition 5.2.

Let d 1 ∈ 𝒟 N 1 d_{1}\in\mathcal{D}_{N_{1}}, d 2 ∈ 𝒟 N 2 d_{2}\in\mathcal{D}_{N_{2}}, and let

 | d = [d 1, 1, 0, d 2], d ′ = [d 1, 0, 1, d 2]. d=[d_{1},1,0,d_{2}],\qquad d^{\prime}=[d_{1},0,1,d_{2}]. |  |

Then C ⁡ ( d) < C ⁡ ( d ′) C(d)<C(d^{\prime}).

###### Proof.

Applying the concatenation formula ( 7), we have

 | C ⁡ ( [d 1, 1, 0, d 2]) = 3 r 0 ​ ( d 2) ​ C ​ ( [d 1, 1, 0]) + 2 N 1 + 2 ​ C ​ ( d 2), C([d_{1},1,0,d_{2}])=3^{r_{0}(d_{2})}\,C([d_{1},1,0])+2^{N_{1}+2}\,C(d_{2}), |  |

and analogously

 | C ⁡ ( [d 1, 0, 1, d 2]) = 3 r 0 ​ ( d 2) ​ C ​ ( [d 1, 0, 1]) + 2 N 1 + 2 ​ C ​ ( d 2). C([d_{1},0,1,d_{2}])=3^{r_{0}(d_{2})}\,C([d_{1},0,1])+2^{N_{1}+2}\,C(d_{2}). |  |

It therefore suffices to compare C ⁡ ( [d 1, 1, 0]) C([d_{1},1,0]) and C ⁡ ( [d 1, 0, 1]) C([d_{1},0,1]). Applying ( 7) again,

 | C ⁡ ( [d 1, 1, 0]) = 3 ​ C ​ ( d 1) + 2 N 1 ​ C ​ ( [1, 0]), C ⁡ ( [d 1, 0, 1]) = 3 ​ C ​ ( d 1) + 2 N 1 ​ C ​ ( [0, 1]). C([d_{1},1,0])=3\,C(d_{1})+2^{N_{1}}\,C([1,0]),\qquad C([d_{1},0,1])=3\,C(d_{1})+2^{N_{1}}\,C([0,1]). |  |

Since C ⁡ ( [1, 0]) = 1 C([1,0])=1 and C ⁡ ( [0, 1]) = 2 C([0,1])=2, we obtain

 | C ⁡ ( [d 1, 0, 1]) − C ⁡ ( [d 1, 1, 0]) = 2 N 1 > 0. C([d_{1},0,1])-C([d_{1},1,0])=2^{N_{1}}>0. |  |

Multiplying by 3 r 0 ​ ( d 2) > 0 3^{r_{0}(d_{2})}>0 gives

 | C ⁡ ( d ′) − C ⁡ ( d) = 2 N 1 ​ 3 r 0 ​ ( d 2) > 0, C(d^{\prime})-C(d)=2^{N_{1}}\,3^{r_{0}(d_{2})}>0, |  |

which completes the proof. ∎

Proposition 5.2 shows that moving a one to the right increases the value of C C. Consequently, configurations that minimize the functional tend to concentrate the ones in earlier positions. Moreover, it induces a partial order on the set of binary words compatible with the distribution of the ones, in the spirit of recent work on parity vectors [12].

This local behaviour is consistent with the global structure of Christoffel words, which distribute the ones in a balanced manner and therefore appear as natural candidates to maximize C min ​ ( d) C_{\min}(d) over 𝒟 N, r \mathcal{D}_{N,r}.

This partial order will be the key tool in Section 6, where we show that any word in 𝒟 N, r \mathcal{D}_{N,r} can be connected to the Christoffel word by a finite sequence of 10 → 01 10\to 01 transpositions.

## 6 Combinatorial structure

It is natural to study the average position of the ones in a binary word. For d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} we define

 | μ ⁡ ( d) = 1 N ​ ∑ j = 1 N j ​ d j. \mu(d)=\frac{1}{N}\sum_{j=1}^{N}j\,d_{j}. |  | (8) |

The quantity μ ⁡ ( d) \mu(d) measures the mean position of the ones in d d. Minimizing μ \mu is therefore equivalent to concentrating the ones as far to the left as possible. The key observation connecting μ \mu to the functional C C is that the rotation minimizing μ \mu within a rotation class is precisely the one that places the ones furthest to the left, and this will turn out to be the rotation for which C C is smallest; working with μ \mu is more tractable because it depends linearly on the positions of the ones, whereas C C depends on them exponentially.

Rather than restricting to a single rotation class, we consider the minimization of μ \mu over the full set 𝒟 N, r \mathcal{D}_{N,r}. This relaxation allows us to work in a simpler framework, decoupling the analysis from the rotation action and revealing the underlying combinatorial structure.

Given d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r}, there exists a rotation d c = τ j ​ ( d) d^{c}=\tau^{j}(d) such that

 | μ ⁡ ( d c) = min 0 ≤ j < N ⁡ μ ⁡ ( τ j ​ ( d)). \mu(d^{c})=\min_{0\leq j<N}\mu(\tau^{j}(d)). |  | (9) |

The idea is to show that, starting from d c d^{c} and applying 10 → 01 10\to 01 transpositions, we can reach the Christoffel word d N, r chr d^{\mathrm{chr}}_{N,r}. We begin with the following lemma.

###### Lemma 6.1.

Let d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} and let d c = τ j ​ ( d) d^{c}=\tau^{j}(d) be a rotation of d d such that

 | μ ⁡ ( d c) = min 0 ≤ j < N ⁡ μ ⁡ ( τ j ​ ( d)). \mu(d^{c})=\min_{0\leq j<N}\mu(\tau^{j}(d)). |  |

Then

 | 1 N − k ∑ j = k + 1 N d j c ≤ r N, k = 0, …, N − 1. \frac{1}{N-k}\sum_{j=k+1}^{N}d_{j}^{c}\leq\frac{r}{N},\qquad k=0,\dots,N-1. |  | (10) |

###### Proof.

We first observe that the condition ( 10) is equivalent, for k ≥ 1 k\geq 1, to

 | 1 k ​ ∑ j = 1 k d j c ≥ r N. \frac{1}{k}\sum_{j=1}^{k}d_{j}^{c}\geq\frac{r}{N}. |  |

Suppose for contradiction that there exists k 0 ∈ { 1, …, N − 1 } k_{0}\in\{1,\dots,N-1\} such that

 | 1 N − k 0 ​ ∑ j = k 0 + 1 N d j c > r N, \frac{1}{N-k_{0}}\sum_{j=k_{0}+1}^{N}d_{j}^{c}>\frac{r}{N}, |  |

and let

 | τ k 0 ​ ( d c) = ( d k 0 + 1 c, …, d N c, d 1 c, …, d k 0 c). \tau^{k_{0}}(d^{c})=\left(d_{k_{0}+1}^{c},\dots,d_{N}^{c},d_{1}^{c},\dots,d_{k_{0}}^{c}\right). |  |

Then

 | μ ⁡ ( τ k 0 ​ ( d c)) \displaystyle\mu(\tau^{k_{0}}(d^{c})) | = 1 N ​ ∑ j = k 0 + 1 N ( j − k 0) ​ d j c + 1 N ​ ∑ j = 1 k 0 ( N − k 0 + j) ​ d j c \displaystyle=\frac{1}{N}\sum_{j=k_{0}+1}^{N}(j-k_{0})\,d_{j}^{c}+\frac{1}{N}\sum_{j=1}^{k_{0}}(N-k_{0}+j)\,d_{j}^{c} |  |

 |  | = μ ⁡ ( d c) − k 0 N ​ ∑ j = k 0 + 1 N d j c + N − k 0 N ​ ∑ j = 1 k 0 d j c. \displaystyle=\mu(d^{c})-\frac{k_{0}}{N}\sum_{j=k_{0}+1}^{N}d_{j}^{c}+\frac{N-k_{0}}{N}\sum_{j=1}^{k_{0}}d_{j}^{c}. |  |

By hypothesis,

 | ∑ j = k 0 + 1 N d j c > r N ​ ( N − k 0), \sum_{j=k_{0}+1}^{N}d_{j}^{c}>\frac{r}{N}(N-k_{0}), |  |

and since ∑ j = 1 N d j c = r \sum_{j=1}^{N}d_{j}^{c}=r, we deduce that

 | ∑ j = 1 k 0 d j c < r N ​ k 0. \sum_{j=1}^{k_{0}}d_{j}^{c}<\frac{r}{N}\,k_{0}. |  |

Substituting gives

 | μ ⁡ ( τ k 0 ​ ( d c)) < μ ⁡ ( d c), \mu(\tau^{k_{0}}(d^{c}))<\mu(d^{c}), |  |

contradicting the minimality of d c d^{c}. ∎

The inequality ( 10) can be interpreted as a balance condition: no tail of the word has a density of ones exceeding the global density r / N r/N. This is a characteristic property of optimal configurations.

###### Lemma 6.2.

Let i 1 chr < ⋯ < i r chr i_{1}^{\mathrm{chr}}<\cdots<i_{r}^{\mathrm{chr}} denote the positions of the ones in d N, r chr d^{\mathrm{chr}}_{N,r}. Then

 | i j chr = ⌊ ( j − 1) ​ N r ⌋ + 1, j = 1, …, r. i_{j}^{\mathrm{chr}}=\left\lfloor\frac{(j-1)N}{r}\right\rfloor+1,\qquad j=1,\dots,r. |  | (11) |

###### Proof.

By definition,

 | i k chr = min ⁡ { i: ⌈ i ​ r N ⌉ = k }. i_{k}^{\mathrm{chr}}=\min\left\{i:\left\lceil\frac{ir}{N}\right\rceil=k\right\}. |  |

Since ⌈ i ​ r N ⌉ = k \left\lceil\frac{ir}{N}\right\rceil=k is equivalent to

 | k − 1 < i ​ r N ≤ k, k-1<\frac{ir}{N}\leq k, |  |

the position i k chr i_{k}^{\mathrm{chr}} is given by the smallest integer satisfying

 | i > ( k − 1) ​ N r. i>\frac{(k-1)N}{r}. |  |

Therefore

 | i k chr = 1 + ⌊ ( k − 1) ​ N r ⌋. i_{k}^{\mathrm{chr}}=1+\left\lfloor\frac{(k-1)N}{r}\right\rfloor. |  |

∎

###### Theorem 6.3 (Position comparison).

Let d c d^{c} be a rotation of d d minimizing μ \mu among all rotations of d d, and let d N, r chr d^{\mathrm{chr}}_{N,r} be the Christoffel word in 𝒟 N, r \mathcal{D}_{N,r}. Denote by i k c i_{k}^{c} and i k chr i_{k}^{\mathrm{chr}}, for k = 1, …, r k=1,\dots,r, the positions of the k k -th one in d c d^{c} and d N, r chr d^{\mathrm{chr}}_{N,r}, respectively. Then

 | i k c ≤ i k chr, k = 1, …, r. i_{k}^{c}\leq i_{k}^{\mathrm{chr}},\qquad k=1,\dots,r. |  | (12) |

###### Proof.

Let d c = ( d 1 c, …, d N c) ∈ 𝒟 N, r d^{c}=(d_{1}^{c},\ldots,d_{N}^{c})\in\mathcal{D}_{N,r} be a rotation minimizing μ \mu. By Lemma 6.1,

 | 1 N − m ∑ j = m + 1 N d j c ≤ r N, m = 0, …, N − 1. \frac{1}{N-m}\sum_{j=m+1}^{N}d_{j}^{c}\leq\frac{r}{N},\qquad m=0,\ldots,N-1. |  |

Taking m = i k c − 1 m=i_{k}^{c}-1, and observing that ( d i k c c, …, d N c) (d_{i_{k}^{c}}^{c},\ldots,d_{N}^{c}) contains exactly r − k + 1 r-k+1 ones, we obtain

 | r − k + 1 N − i k c + 1 ≤ r N. \frac{r-k+1}{N-i_{k}^{c}+1}\leq\frac{r}{N}. |  |

Hence,

 | N ⁡ ( r − k + 1) ≤ r ⁡ ( N − i k c + 1), N(r-k+1)\leq r(N-i_{k}^{c}+1), |  |

which yields

Since i k c i_{k}^{c} is an integer,

 | i k c ≤ 1 + ⌊ ( k − 1) ​ N r ⌋. i_{k}^{c}\leq 1+\left\lfloor\frac{(k-1)N}{r}\right\rfloor. |  |

Combining this with Lemma 6.2, we conclude ( 12). ∎

Inequality ( 12) expresses that the ones in d c d^{c} are, in a precise sense, shifted to the left relative to those of the Christoffel word. This comparison is consistent with the optimal balance of Christoffel words and will allow us to connect d c d^{c} to d N, r chr d^{\mathrm{chr}}_{N,r} by a chain of Proposition 5.2 transpositions.

###### Theorem 6.4 (Connection by transpositions).

The word d c d^{c} can be transformed into d N, r chr d^{\mathrm{chr}}_{N,r} by a finite sequence of 10 → 01 10\to 01 transpositions.

###### Proof.

We proceed by induction, constructing a sequence of words d 0, d 1, …, d r − 1 d^{0},d^{1},\dots,d^{r-1} with d 0 = d c d^{0}=d^{c}.

The last one in d 0 d^{0} occupies the position i r c i_{r}^{c}. By Theorem 6.3 i r c ≤ i r chr i_{r}^{c}\leq i_{r}^{\mathrm{chr}}. Therefore, we can move that last one at position i r chr i_{r}^{\mathrm{chr}} to get d 1 d^{1} by a sequence of i r chr − i r c i_{r}^{\mathrm{chr}}-i_{r}^{c} transpositions.

Assume that in the word d k d^{k} the last k k ones already occupy their correct positions, that is, they appear at positions i r − k + 1 chr, …, i r chr i_{r-k+1}^{\mathrm{chr}},\dots,i_{r}^{\mathrm{chr}}. The remaining r − k r-k ones to the left occupy their original positions, those of the first r − k r-k ones in d c d^{c}. So, there is a one in d k d^{k} at position i r − k c i_{r-k}^{c}.

By Theorem 6.3, i r − k c ≤ i r − k chr i_{r-k}^{c}\leq i_{r-k}^{\mathrm{chr}}. Moreover, between positions i r − k c i_{r-k}^{c} and i r − k chr i_{r-k}^{\mathrm{chr}} there are no ones already fixed, since those occupy positions i r − k + 1 chr, …, i r chr i_{r-k+1}^{\mathrm{chr}},\dots,i_{r}^{\mathrm{chr}}, all strictly to the right of i r − k chr i_{r-k}^{\mathrm{chr}}. Therefore it is possible to move the one at position i r − k c i_{r-k}^{c} to position i r − k chr i_{r-k}^{\mathrm{chr}} by a finite sequence of 10 → 01 10\to 01 transpositions, each of which moves it one step to the right without altering any other one. Define d k + 1 d^{k+1} as the word obtained after these transpositions.

Iterating for k = 1, …, r − 1 k=1,\dots,r-1, we obtain d r − 1 = d N, r chr d^{r-1}=d^{\mathrm{chr}}_{N,r}, which completes the induction. ∎

Theorem 6.4 shows that d N, r chr d^{\mathrm{chr}}_{N,r} can be reached from d c d^{c} by local transformations that progressively redistribute the ones in a more balanced way. This reveals the compatibility between the partial order induced by 10 → 01 10\to 01 transpositions and the structure of Christoffel words.

## 7 Main result

Before establishing the main result, we analyze the behaviour of the functional C C on Christoffel words as the length increases with the number of ones fixed. This controls the growth of C C and will be essential in the final comparison.

###### Proposition 7.1.

For the Christoffel word d N, r chr d_{N,r}^{\mathrm{chr}} of length N N with r r ones, defined by ( 6), we have

 | C ⁡ ( d N, r chr) < C ⁡ ( d N + 1, r chr) < 2 ​ C ​ ( d N, r chr). C(d_{N,r}^{\mathrm{chr}})<C(d_{N+1,r}^{\mathrm{chr}})<2\,C(d_{N,r}^{\mathrm{chr}}). |  | (13) |

###### Proof.

Let c k ​ ( N) = ⌈ k ​ r / N ⌉ c_{k}(N)=\left\lceil kr/N\right\rceil. Then, the characters of the word d N, r chr d_{N,r}^{\mathrm{chr}} can be written as d k = c k ​ ( N) − c k − 1 ​ ( N) d_{k}=c_{k}(N)-c_{k-1}(N), and the ones appear exactly at the indices where c k ​ ( N) c_{k}(N) increments. Denoting these indices by

 | k 1 ​ ( N) < ⋯ < k r ​ ( N), k_{1}(N)<\cdots<k_{r}(N), |  |

we have

 | C ⁡ ( d N, r chr) = ∑ j = 1 r 2 k j ​ ( N) − 1 ​ 3 r − j. C(d_{N,r}^{\mathrm{chr}})=\sum_{j=1}^{r}2^{k_{j}(N)-1}\,3^{r-j}. |  |

We define the indices k j ​ ( N + 1) k_{j}(N+1) analogously. Since k ​ r / ( N + 1) < k ​ r / N kr/(N+1)<kr/N, we have c k ​ ( N + 1) ≤ c k ​ ( N) c_{k}(N+1)\leq c_{k}(N). Both sequences are non-decreasing, take integer values in { 0, …, r } \{0,\dots,r\}, and can increase by at most one; therefore the positions of the increments shift to the right as N N increases to N + 1 N+1 [13, 5]. Consequently,

 | k j ​ ( N) ≤ k j ​ ( N + 1), k_{j}(N)\leq k_{j}(N+1), |  |

with strict inequality for at least one j j, which gives

 | C ⁡ ( d N + 1, r chr) > C ⁡ ( d N, r chr). C(d_{N+1,r}^{\mathrm{chr}})>C(d_{N,r}^{\mathrm{chr}}). |  |

On the other hand, we claim that c k ​ ( N + 1) ≥ c k − 1 ​ ( N) c_{k}(N+1)\geq c_{k-1}(N), which implies k j ​ ( N + 1) ≤ k j ​ ( N) + 1 k_{j}(N+1)\leq k_{j}(N)+1. Indeed, k ​ r N + 1 ≥ ( k − 1) ​ r N \frac{kr}{N+1}\geq\frac{(k-1)r}{N} is equivalent to k ​ N ≥ ( k − 1) ​ ( N + 1) kN\geq(k-1)(N+1), that is, to N + 1 ≥ k N+1\geq k, which holds for all k ≤ N + 1 k\leq N+1. Therefore each increment position shifts by at most one, so

 | C ⁡ ( d N + 1, r chr) ≤ ∑ j = 1 r 2 k j ​ ( N) ​ 3 r − j = 2 ​ C ​ ( d N, r chr). ∎ C(d_{N+1,r}^{\mathrm{chr}})\leq\sum_{j=1}^{r}2^{k_{j}(N)}\,3^{r-j}=2\,C(d_{N,r}^{\mathrm{chr}}).\qed |  |

Proposition 7.1 shows that C C grows in a controlled manner as the length increases; the following corollary translates this into a monotonicity property of the quantity characterizing cycles.

###### Corollary 7.2.

Assume 2 N > 3 r 2^{N}>3^{r}, which holds whenever N / r > log 2 ⁡ 3 N/r>\log_{2}3. Then

 | C ⁡ ( d N + 1, r chr) 2 N + 1 − 3 r < C ⁡ ( d N, r chr) 2 N − 3 r. \frac{C(d_{N+1,r}^{\mathrm{chr}})}{2^{N+1}-3^{r}}<\frac{C(d_{N,r}^{\mathrm{chr}})}{2^{N}-3^{r}}. |  | (14) |

###### Proof.

From Proposition 7.1, C ⁡ ( d N + 1, r chr) < 2 ​ C ​ ( d N, r chr) C(d_{N+1,r}^{\mathrm{chr}})<2\,C(d_{N,r}^{\mathrm{chr}}), so

 | C ⁡ ( d N + 1, r chr) 2 N + 1 − 3 r < 2 ​ C ​ ( d N, r chr) 2 N + 1 − 3 r. \frac{C(d_{N+1,r}^{\mathrm{chr}})}{2^{N+1}-3^{r}}<\frac{2\,C(d_{N,r}^{\mathrm{chr}})}{2^{N+1}-3^{r}}. |  |

Since 2 ​ ( 2 N − 3 r) = 2 N + 1 − 2 ⋅ 3 r < 2 N + 1 − 3 r 2(2^{N}-3^{r})=2^{N+1}-2\cdot 3^{r}<2^{N+1}-3^{r} and 2 N > 3 r 2^{N}>3^{r} by hypothesis, it follows that

 | 2 2 N + 1 − 3 r < 1 2 N − 3 r. \frac{2}{2^{N+1}-3^{r}}<\frac{1}{2^{N}-3^{r}}. |  |

Multiplying by C ⁡ ( d N, r chr) > 0 C(d_{N,r}^{\mathrm{chr}})>0 and combining with the previous inequality yields ( 14). ∎

Corollary 7.2 shows that as the length increases with the number of odd iterates fixed, the quantity associated with the possible existence of cycles decreases strictly. In particular, longer configurations are progressively less favourable for the existence of cycles.

We are now in a position to establish the main result of the paper.

###### Theorem 7.3 (Main theorem).

For every N ≥ 1 N\geq 1 and 0 ≤ r ≤ N 0\leq r\leq N,

 | max d ∈ 𝒟 N, r ⁡ C min ​ ( d) = C ⁡ ( d N, r chr), \max_{d\in\mathcal{D}_{N,r}}C_{\min}(d)=C(d^{\mathrm{chr}}_{N,r}), |  | (15) |

where d N, r chr d^{\mathrm{chr}}_{N,r} is the Christoffel word of length N N with r r ones. Moreover, the maximum is attained uniquely, up to rotation, at d = d N, r chr d=d^{\mathrm{chr}}_{N,r}.

###### Proof.

Let d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} and let d c d^{c} be the rotation of d d minimizing μ \mu among all rotations, as in ( 9). By definition of C min C_{\min} and the fact that d c d^{c} is one of the rotations over which the minimum is taken,

 | C min ​ ( d) ≤ C ⁡ ( d c). C_{\min}(d)\leq C(d^{c}). |  |

By Theorem 6.4, d c d^{c} can be transformed into d N, r chr d^{\mathrm{chr}}_{N,r} by a finite sequence of 10 → 01 10\to 01 transpositions. By Proposition 5.2, each such transposition strictly increases the value of C C. Therefore

 | C ⁡ ( d c) ≤ C ⁡ ( d N, r chr), C(d^{c})\leq C(d^{\mathrm{chr}}_{N,r}), |  |

with equality if and only if the sequence of transpositions is empty, that is, if and only if d c = d N, r chr d^{c}=d^{\mathrm{chr}}_{N,r}. Combining both inequalities,

 | C min ​ ( d) ≤ C ⁡ ( d N, r chr), ∀ d ∈ 𝒟 N, r ⟹ max d ∈ 𝒟 N, r ⁡ C min ​ ( d) ≤ C ⁡ ( d chr) C_{\min}(d)\leq C(d^{\mathrm{chr}}_{N,r}),\quad\forall d\in\mathcal{D}_{N,r}\Longrightarrow\max_{d\in\mathcal{D}_{N,r}}C_{\min}(d)\leq C(d^{\mathrm{chr}}) |  |

It is now easy to see that the Christoffel word d N, r chr d^{\mathrm{chr}}_{N,r} is the rotation that minimizes μ \mu within its rotation class, that is

 | ( d N, r chr) c = d N, r chr, (d^{\mathrm{chr}}_{N,r})^{c}=d^{\mathrm{chr}}_{N,r}, |  |

and this follows directly from the previous lemmas.

Moreover, by Theorem 6.3 and Proposition 5.2 we know that there exists, for any μ \mu -minimizing rotation d c d^{c}, a finite sequence of 10 → 01 10\to 01 transpositions transforming d c d^{c} into d N, r chr d^{\mathrm{chr}}_{N,r}, each of which strictly increases C C. In our particular case, starting from ( d N, r chr) c = d N, r chr (d^{\mathrm{chr}}_{N,r})^{c}=d^{\mathrm{chr}}_{N,r}, this sequence of transpositions is empty, so there is no way to obtain a rotation of d N, r chr d^{\mathrm{chr}}_{N,r} with a strictly smaller value of C C. Consequently,

 | C min ​ ( d N, r chr) = min 0 ≤ j < N ⁡ C ⁡ ( τ j ​ ( d N, r chr)) = C ⁡ ( d N, r chr), C_{\min}\bigl(d^{\mathrm{chr}}_{N,r}\bigr)=\min_{0\leq j<N}C\bigl(\tau^{j}(d^{\mathrm{chr}}_{N,r})\bigr)=C\bigl(d^{\mathrm{chr}}_{N,r}\bigr), |  |

which shows that the upper bound C ⁡ ( d N, r chr) C(d^{\mathrm{chr}}_{N,r}) is actually attained. ∎

Theorem 7.3 shows that Christoffel words are not only combinatorially balanced, but also constitute the unique extremal configurations for the functional C min C_{\min}. This establishes a direct link between the dynamics of the Collatz problem and classical structures in combinatorics on words, showing that optimal configurations are governed by balanced distributions of the ones. To the best of our knowledge, this is the first result identifying Christoffel words as extremal configurations for a functional arising directly from Collatz dynamics.

## 8 Bounds

In this section we use the optimization results obtained previously to derive arithmetic restrictions on the possible existence of periodic cycles. In particular, we show that the proportion between even and odd iterates imposes very rigid constraints on the dynamics.

###### Theorem 8.1.

Let d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} be the parity word associated with a periodic orbit of the Collatz map. Then:

1. 1.

If N = 2 ​ r N=2r, the only periodic orbit with this proportion of even and odd iterates is the trivial one.

2. 2.

There is no periodic orbit with N > 2 ​ r N>2r.

###### Proof.

1. 1.

Case N = 2 ​ r N=2r. The Christoffel word in this case is d 2 ​ r, r chr = [10] r d_{2r,r}^{\mathrm{chr}}=[10]^{r}, and a direct computation gives

 | C ⁡ ( d 2 ​ r, r chr) = ∑ i = 1 r 2 2 ​ i − 2 ​ 3 r − i = 3 r 4 ​ ∑ i = 1 r ( 4 3) i = 4 r − 3 r. C(d_{2r,r}^{\mathrm{chr}})=\sum_{i=1}^{r}2^{2i-2}\,3^{r-i}=\frac{3^{r}}{4}\sum_{i=1}^{r}\left(\frac{4}{3}\right)^{i}=4^{r}-3^{r}. |  |

By Theorem 7.3, C min ​ ( d) ≤ C ⁡ ( d 2 ​ r, r chr) = 4 r − 3 r C_{\min}(d)\leq C(d_{2r,r}^{\mathrm{chr}})=4^{r}-3^{r} for every d ∈ 𝒟 2 ​ r, r d\in\mathcal{D}_{2r,r}. Using ( 3) with 2 N − 3 r = 4 r − 3 r 2^{N}-3^{r}=4^{r}-3^{r},

 | x = C min ​ ( d) 4 r − 3 r ≤ 4 r − 3 r 4 r − 3 r = 1. x=\frac{C_{\min}(d)}{4^{r}-3^{r}}\leq\frac{4^{r}-3^{r}}{4^{r}-3^{r}}=1. |  |

Since x ∈ ℕ x\in\mathbb{N} and x ≥ 1 x\geq 1, we conclude x = 1 x=1, which corresponds to the trivial cycle. By Theorem 7.3, equality holds if and only if d d is a rotation of [10] r [10]^{r}, confirming that the trivial cycle is the only one.

2. 2.

Case N > 2 ​ r N>2r. Write N = 2 ​ r + n 0 N=2r+n_{0} with n 0 > 0 n_{0}>0. Applying Corollary 7.2 repeatedly and noting that 2 N > 3 r 2^{N}>3^{r} for all steps since N / r > 2 > log 2 ⁡ 3 N/r>2>\log_{2}3,

 | C ⁡ ( d N, r chr) 2 N − 3 r < ⋯ < C ⁡ ( d 2 ​ r, r chr) 4 r − 3 r = 1. \frac{C(d_{N,r}^{\mathrm{chr}})}{2^{N}-3^{r}}<\cdots<\frac{C(d_{2r,r}^{\mathrm{chr}})}{4^{r}-3^{r}}=1. |  |

By Theorem 7.3, C min ​ ( d) ≤ C ⁡ ( d N, r chr) C_{\min}(d)\leq C(d_{N,r}^{\mathrm{chr}}), so

 | x = C min ​ ( d) 2 N − 3 r ≤ C ⁡ ( d N, r chr) 2 N − 3 r < 1, x=\frac{C_{\min}(d)}{2^{N}-3^{r}}\leq\frac{C(d_{N,r}^{\mathrm{chr}})}{2^{N}-3^{r}}<1, |  |

contradicting x ∈ ℕ x\in\mathbb{N} with x ≥ 1 x\geq 1.

∎

Theorem 8.1 shows that the density of odd iterates in a periodic orbit is strongly constrained. The bound N ≤ 2 ​ r N\leq 2r is known in the literature [3]; what is new here is that it follows directly from the extremality of Christoffel words established in Theorem 7.3. Together with the necessary condition

 | N r > log ⁡ 3 log ⁡ 2 ≈ 1.585, \frac{N}{r}>\frac{\log 3}{\log 2}\approx 1.585, |  |

this gives the sharp bound on the slope:

 | log ⁡ 3 log ⁡ 2 < N r ≤ 2. \frac{\log 3}{\log 2}<\frac{N}{r}\leq 2. |  | (16) |

To obtain an explicit bound on x x in terms of N / r N/r, we need to explicitly estimate C ⁡ ( d N, r chr) C(d_{N,r}^{\mathrm{chr}}). This requires knowing the positions of the ones, which is given by Lemma 6.2. The estimate in Theorem 8.2 will be sharp when the floor function in ( 11) is close to the continuous value ( j − 1) ​ N / r (j-1)N/r, which occurs precisely for Christoffel words.

###### Theorem 8.2.

Let d ∈ 𝒟 N, r d\in\mathcal{D}_{N,r} be the parity word associated with a periodic orbit of the Collatz map, with N / r > log 2 ⁡ 3 N/r>\log_{2}3. Then there exists an element x x of the orbit satisfying

 | x ≤ 1 2 N / r − 3. x\leq\frac{1}{2^{N/r}-3}. |  | (17) |

###### Proof.

By Theorem 7.3 and ( 3),

 | x = C min ​ ( d) 2 N − 3 r ≤ C ⁡ ( d N, r chr) 2 N − 3 r. x=\frac{C_{\min}(d)}{2^{N}-3^{r}}\leq\frac{C(d_{N,r}^{\mathrm{chr}})}{2^{N}-3^{r}}. |  | (18) |

Using Lemma 6.2 and ( 4),

 | C ⁡ ( d N, r chr) = ∑ j = 1 r 2 i j chr − 1 ​ 3 r − j = ∑ j = 1 r 2 ⌊ ( j − 1) ​ N / r ⌋ ​ 3 r − j. C(d_{N,r}^{\mathrm{chr}})=\sum_{j=1}^{r}2^{i_{j}^{\mathrm{chr}}-1}\,3^{r-j}=\sum_{j=1}^{r}2^{\left\lfloor(j-1)N/r\right\rfloor}\,3^{r-j}. |  |

Since ⌊ ( j − 1) ​ N / r ⌋ ≤ ( j − 1) ​ N / r \left\lfloor(j-1)N/r\right\rfloor\leq(j-1)N/r, we have 2 ⌊ ( j − 1) ​ N / r ⌋ ≤ 2 ( j − 1) ​ N / r 2^{\left\lfloor(j-1)N/r\right\rfloor}\leq 2^{(j-1)N/r}, and therefore

 | C ⁡ ( d N, r chr) ≤ ∑ j = 1 r 2 ( j − 1) ​ N / r ​ 3 r − j = 3 r − 1 ​ ∑ j = 1 r ( 2 N / r 3) j − 1. C(d_{N,r}^{\mathrm{chr}})\leq\sum_{j=1}^{r}2^{(j-1)N/r}\,3^{r-j}=3^{r-1}\sum_{j=1}^{r}\left(\frac{2^{N/r}}{3}\right)^{j-1}. |  |

This is a geometric series with ratio q = 2 N / r / 3 > 1 q=2^{N/r}/3>1 (since N / r > log 2 ⁡ 3 N/r>\log_{2}3), giving

 | C ⁡ ( d N, r chr) ≤ 3 r − 1 ​ ∑ j = 1 r q j − 1 = 3 r − 1 ​ q r − 1 q − 1 = 3 r − 1 ​ 2 N / 3 r − 1 2 N / r / 3 − 1 = 2 N − 3 r 2 N / r − 3. C(d_{N,r}^{\mathrm{chr}})\leq 3^{r-1}\sum_{j=1}^{r}q^{j-1}=3^{r-1}\frac{q^{r}-1}{q-1}=3^{r-1}\frac{2^{N}/3^{r}-1}{2^{N/r}/3-1}=\frac{2^{N}-3^{r}}{2^{N/r}-3}. |  |

Using this bound in ( 18) we get ( 17). ∎

The bound ( 17) translates the combinatorial structure of parity sequences into an explicit arithmetic constraint on the minimum element of a periodic orbit. Since r ↦ 2 N / r r\mapsto 2^{N/r} is decreasing in r r, the bound ( 17) is largest when r r is largest, that is, when r r takes its maximum admissible value

 | r 0 = ⌊ N ​ log ⁡ 2 log ⁡ 3 ⌋. r_{0}=\left\lfloor N\,\frac{\log 2}{\log 3}\right\rfloor. |  |

###### Corollary 8.3.

For every N ≥ 1 N\geq 1, the minimum element of any periodic orbit of length N N satisfies

 | x ≤ 1 2 N / r 0 − 3, r 0 = ⌊ N ​ log ⁡ 2 log ⁡ 3 ⌋, x\leq\frac{1}{2^{N/r_{0}}-3},\qquad r_{0}=\left\lfloor N\,\frac{\log 2}{\log 3}\right\rfloor, |  | (19) |

a bound depending only on N N.

###### Proof.

Apply Theorem 8.2 with r = r 0 r=r_{0}, noting that r ↦ ( 2 N / r − 3) − 1 r\mapsto(2^{N/r}-3)^{-1} is decreasing since r ↦ 2 N / r r\mapsto 2^{N/r} is decreasing, so the bound is maximized at the largest admissible r r, which is r 0 r_{0}. ∎

Bound ( 19) is particularly useful for computational searches, as it provides an a priori upper bound on the minimum element of any cycle of length N N, independently of the number of odd iterates. Table 1 lists the values of this universal bound for a selection of periods N ≤ 485 N\leq 485.

Table 1: Universal bound ( 19) on the minimum element of any periodic orbit of length N N, for selected values of N N. Here r 0 = ⌊ N ​ log ⁡ 2 / log ⁡ 3 ⌋ r_{0}=\lfloor N\log 2/\log 3\rfloor is the worst-case number of odd iterates. The non-monotone behaviour of the bound is a consequence of the irregular approximation of log 2 ⁡ 3 \log_{2}3 by rationals. The last two rows correspond to values of N N for which r 0 / N r_{0}/N is an exceptionally good rational approximation of log ⁡ 2 / log ⁡ 3 \log 2/\log 3, producing very large bounds and illustrating the divergence of the universal bound as N / r 0 → log 2 ⁡ 3 + N/r_{0}\to\log_{2}3^{+}.

N N | r 0 r_{0} | N / r 0 N/r_{0} | 1 2 N / r 0 − 3 \dfrac{1}{2^{N/r_{0}}-3} |

10 | 6 | 1.6667 1.6667 | 5.721 5.721 |

20 | 12 | 1.6667 1.6667 | 5.721 5.721 |

30 | 18 | 1.6667 1.6667 | 5.721 5.721 |

40 | 25 | 1.6000 1.6000 | 31.814 31.814 |

50 | 31 | 1.6129 1.6129 | 17.045 17.045 |

60 | 37 | 1.6216 1.6216 | 12.952 12.952 |

70 | 44 | 1.5909 1.5909 | 80.703 80.703 |

80 | 50 | 1.6000 1.6000 | 31.814 31.814 |

90 | 56 | 1.6071 1.6071 | 21.515 21.515 |

100 | 63 | 1.5873 1.5873 | 205.426 205.426 |

150 | 94 | 1.5957 1.5957 | 44.435 44.435 |

200 | 126 | 1.5873 1.5873 | 205.426 205.426 |

306 | 193 | 1.5855 1.5855 | 907.656 907.656 |

485 | 306 | 1.5850 1.5850 | 99780.791 99780.791 |

## 9 Discussion

The results obtained allow us to reinterpret the problem of the existence of nontrivial cycles of the Collatz map in purely combinatorial terms, reducing it to the study of binary words of fixed length and prescribed density.

The main theorem shows that, within each class 𝒟 N, r \mathcal{D}_{N,r}, the Christoffel word d N, r chr d^{\mathrm{chr}}_{N,r} is the unique maximizer, up to rotation, of C min ​ ( d) C_{\min}(d). This establishes a direct connection between Collatz dynamics and the classical theory of balanced words, where Christoffel words appear as extremal configurations characterized by an optimal distribution of symbols. From this perspective, the existence of periodic cycles is constrained by

 | x = C min ​ ( d) 2 N − 3 r ≤ C ⁡ ( d N, r chr) 2 N − 3 r, x=\frac{C_{\min}(d)}{2^{N}-3^{r}}\leq\frac{C(d^{\mathrm{chr}}_{N,r})}{2^{N}-3^{r}}, |  |

which reduces the analysis essentially to understanding the behaviour of Christoffel words.

As a first consequence, no cycle can satisfy N > 2 ​ r N>2r, and the critical case N = 2 ​ r N=2r corresponds exclusively to the trivial cycle. As noted in Section 8, the bound N ≤ 2 ​ r N\leq 2r is known in the literature [3]; the contribution of the present work is to derive it as a direct consequence of the extremality of Christoffel words, placing it within a broader combinatorial framework. Combined with the necessary condition N / r > log 2 ⁡ 3 N/r>\log_{2}3, this gives the sharp constraint ( 16) on the admissible slopes.

The explicit bound

 | x ≤ 1 2 N / r − 3 x\leq\frac{1}{2^{N/r}-3} |  |

provides a direct relation between the length of the orbit and the size of its minimum element, giving effective control over the possible candidates for cycles in terms of the parameters ( N, r) (N,r). The worst case occurs when r ≈ N ​ log ⁡ 2 / log ⁡ 3 r\approx N\log 2/\log 3, which coincides with the critical slope arising naturally in heuristic models of the Collatz problem [3, 10], and leads to the universal bound of Corollary 8.3.

From a conceptual point of view, these results show that the combinatorial structure of parity sequences imposes strong restrictions on the possible existence of cycles. In particular, the compatibility between the partial order induced by 10 → 01 10\to 01 transpositions and the structure of Christoffel words suggests that extremal configurations exhibit a pronounced structural rigidity: any word that is not a rotation of a Christoffel word is strictly suboptimal for C min C_{\min}, and therefore cannot correspond to a cycle with parameters close to the critical values.

Several directions remain open. First, the bound ( 17) could potentially be sharpened by a more precise analysis of the gap between ⌊ ( j − 1) ​ N / r ⌋ \left\lfloor(j-1)N/r\right\rfloor and ( j − 1) ​ N / r (j-1)N/r, which depends on the continued fraction expansion of r / N r/N. Second, the role of Sturmian words — the aperiodic analogues of Christoffel words, corresponding to irrational slopes — in the study of unbounded orbits deserves further investigation: if the density of odd iterates along an orbit converges to an irrational value, the associated parity sequence approaches a Sturmian word, and the extremal properties of such sequences may impose constraints on the growth of the orbit. Third, the framework developed here could be extended to variants of the Collatz map, such as the a ​ x + b ax+b family, or to other discrete dynamical systems with symbolic structure admitting a similar functional C ⁡ ( d) C(d).

After this work was completed, we became aware of the recent article by Kevin Knight [15], which studies rational Collatz cycles and identifies upper Christoffel words in that setting. Although both works highlight the role of Christoffel words in Collatz dynamics, they address different but complementary questions.

Knight considers the case of rational Collatz cycles with odd denominators, showing that upper Christoffel words parametrize the high cycles of prescribed length and odd density, and proving that none of these high cycles can consist entirely of integers. By contrast, we study the classical accelerated Collatz map on 𝐍 \mathbf{N} and formulate a discrete optimization problem for the rotation-invariant functional C min C_{\min} on the space D N, r D_{N,r} of parity words.

Our Theorem 7.3 proves that, for every admissible pair ( N, r) (N,r), the corresponding Christoffel word is the unique maximizer of C min C_{\min} up to rotation. Theorem 8.1 then translates this extremal property into explicit bounds on the existence and size of integer cycles. Together with Knight’s non-integrality result for rational high cycles, our results show that, whenever N r ∈ ( log 2 ⁡ 3, 2] \frac{N}{r}\in\left(\log_{2}3,2\right], the unique extremal parity pattern cannot correspond to an entirely integer cycle. Consequently, any hypothetical integer cycle must arise from a strictly suboptimal parity pattern, to which our upper bounds impose additional constraints.

## References

- [1] R. Terras, A stopping time problem on the positive integers, Acta Arithmetica, 30 (1976), 241–252.
- [2] C. J. Everett, Iteration of the number-theoretic function f ⁡ ( 2 ​ n) = n f(2n)=n, f ⁡ ( 2 ​ n + 1) = 3 ​ n + 2 f(2n+1)=3n+2, Advances in Mathematics, 25 (1977), 42–45.
- [3] J. C. Lagarias, The 3 ​ x + 1 3x+1 problem and its generalizations, American Mathematical Monthly, 92 (1985), 3–23.
- [4] J. C. Lagarias (ed.), The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem, American Mathematical Society, 2010.
- [5] J.-P. Allouche, J. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge University Press, 2003.
- [6] G. Wirsching, The Dynamical System Generated by the 3 ​ n + 1 3n+1 Function, Springer, 1998.
- [7] D. Applegate, J. C. Lagarias, Density bounds for the 3 ​ x + 1 3x+1 problem, Experimental Mathematics, 12 (2003), 403–414.
- [8] I. Krasikov, J. C. Lagarias, Bounds for the 3 ​ x + 1 3x+1 problem using difference inequalities, Acta Arithmetica, 109 (2003), 237–258.
- [9] T. Tao, Almost all Collatz orbits attain almost bounded values, arXiv:1909.03562 [math.NT], 2019.
- [10] A. Kontorovich, J. C. Lagarias, Stochastic models for the 3 ​ x + 1 3x+1 problem, Experimental Mathematics, 19 (2010), 1–19.
- [11] R. Rajab, Characteristic numbers and characteristic equations of parity vectors of Collatz sequences, arXiv:2209.03730 (2022), [https://arxiv.org/abs/2209.03730][3].
- [12] O. Rozier, Paradoxical behavior in Collatz sequences, arXiv:2502.00948 (2025), [https://arxiv.org/abs/2502.00948][4].
- [13] M. Lothaire, Algebraic Combinatorics on Words, Cambridge University Press, 2002.
- [14] J. Berstel, A. De Luca, Sturmian words, Lyndon words and trees, Theoretical Computer Science, 178 (2002), 171–203
- [15] K. Knight, Collatz high dycles do not exist, Disrrete Mathematics, 349 (2026) 114812.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/pdf/2209.03730
[4]: https://arxiv.org/pdf/2502.00948
