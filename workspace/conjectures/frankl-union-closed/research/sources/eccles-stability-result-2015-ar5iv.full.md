<!-- source: https://ar5iv.labs.arxiv.org/html/1311.2298 | converted from HTML -->

[1311.2298] A stability result for the union-closed size problem

# A stability result for the union-closed size problem

Tom Eccles Thanks: Department of Pure Mathematics and Mathematical Statistics, Wilberforce Road, Cambridge CB3 0WB, UK; +44 (0)1223 765921; te227@cam.ac.uk Thanks: This research was supported by EPSRC

August 8, 2026

###### Abstract

A family of sets is called union-closed if whenever A A and B B are sets of the family, so is A ∪ B A\cup B. The long-standing union-closed conjecture states that if a family of subsets of [n] [n] is union-closed, some element appears in at least half the sets of the family. A natural weakening is that the union-closed conjecture holds for large families; that is, families consisting of at least p 0 ​ 2 n p_{0}2^{n} sets for some constant p 0 p_{0}. The first result in this direction appears in a recent paper of Balla, Bollobás and Eccles [1], who showed that union-closed families of at least 2 3 ​ 2 n \frac{2}{3}2^{n} sets satisfy the conjecture — they proved this by determining the minimum possible average size of a set in a union-closed family of given size. However, the methods used in that paper cannot prove a better constant than 2 3 \frac{2}{3}. Here, we provide a stability result for the main theorem of [1], and as a consequence we prove the union-closed conjecture for families of at least ( 2 3 − c) ​ 2 n (\frac{2}{3}-c)2^{n} sets, for a positive constant c c.

## 1 Introduction

We shall be concerned with finite families of finite sets; as often, we shall assume that such a family is a subset of 𝒫 ⁡ ( n) = 𝒫 ⁡ ( [n]) \mathcal{P}(n)=\mathcal{P}([n]) for some n n, where 𝒫 \mathcal{P} denotes the powerset and [n] = { 1, …, n } [n]=\{1,\dots,n\}. For 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n), we call 𝒜 \mathcal{A}*union-closed*if for any two elements A A and B B of 𝒜 \mathcal{A} the set A ∪ B A\cup B is also in 𝒜 \mathcal{A}. For i ∈ ℕ i\in\mathbb{N}, the *degree of i i in 𝒜 \mathcal{A}*, denoted deg 𝒜 ​ ( i) \mathrm{deg}_{\mathcal{A}}(i), is simply

 | | { A ∈ 𝒜: i ∈ A } |. |\{A\in\mathcal{A}:i\in A\}|. |  |

The *union-closed conjecture*, often attributed to Frankl [4], states that if 𝒜 \mathcal{A} is a union-closed family other than { ∅ } \{\emptyset\} then there is some i i with deg 𝒜 ​ ( i) ≥ | 𝒜 | / 2 \mathrm{deg}_{\mathcal{A}}(i)\geq|\mathcal{A}|/2.

A related problem is the *union-closed size problem*, which asks how small the sets of a union-closed family can be. For a finite family 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n), we define the *total size*of 𝒜 \mathcal{A} to be

 | ‖ 𝒜 ‖ = ∑ A ∈ 𝒜 | A |. ||\mathcal{A}||=\sum_{A\in\mathcal{A}}|A|. |  |

Then the union-closed size problem asks what is the value of

 | f ⁡ ( m) = min ⁡ ‖ 𝒜 ‖, f(m)=\min||\mathcal{A}||, |  |

where the minimum runs over union-closed families which consist of m m sets. This problem was first addressed by Reimer [8] in 2003, who proved that

 | f ⁡ ( m) ≥ m 2 ​ log 2 ​ m. f(m)\geq\frac{m}{2}\log_{2}m. |  |

Recently, Balla, Bollobás and Eccles [1] settled the union-closed size problem entirely, determining the exact value of f ⁡ ( m) f(m) for all m m. We denote by ℐ ⁡ ( m) \mathcal{I}(m) the initial segment of the colex order on ℕ ( < ∞) \mathbb{N}^{(<\infty)} of length m m; this order shall be defined fully in Section 2.

###### Theorem 1.1.

Let m m be a positive integer, and let n n be the unique integer with 2 n − 1 < m ≤ 2 n 2^{n-1}<m\leq 2^{n}. Set m ′ = 2 n − m m^{\prime}=2^{n}-m. Then

 | f ⁡ ( m) = ‖ 𝒫 ⁡ ( n) ‖ − | | ℐ ⁡ ( m ′) | | − m ′. f(m)=||\mathcal{P}(n)||-||\mathcal{I}(m^{\prime})||-m^{\prime}. |  |

In particular, if 𝒜 \mathcal{A} is a counterexample to the union-closed conjecture in 𝒫 ⁡ ( n) \mathcal{P}(n) with | 𝒜 | = m |\mathcal{A}|=m then f ⁡ ( m) < n ​ m / 2 f(m)<nm/2, and so

 | ‖ ℐ ⁡ ( m ′) ‖ + m ′ > n ​ 2 n / 2 − n ​ m / 2 = n ​ m ′ / 2. ||\mathcal{I}(m^{\prime})||+m^{\prime}>n2^{n}/2-nm/2=nm^{\prime}/2. |  |

The extremal family 𝒜 \mathcal{A} for the first part of the theorem has 𝒫 ⁡ ( n) ∖ 𝒜 = { B ∪ { n }: B ∈ ℐ ⁡ ( m ′) } \mathcal{P}(n)\setminus\mathcal{A}=\{B\cup\{n\}:B\in\mathcal{I}(m^{\prime})\}. Through bounding ‖ ℐ ⁡ ( m ′) ‖ ||\mathcal{I}(m^{\prime})||, this result is sufficient to prove the union-closed conjecture if | 𝒜 | |\mathcal{A}| is large — in fact the following bound is given in [1].

###### Corollary 1.2.

The union-closed conjecture holds for all union-closed families 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) with | 𝒜 | ≥ 2 3 ​ 2 n |\mathcal{A}|\geq\frac{2}{3}2^{n}.

However, this is as far as one can go considering only averaging arguments — if m < 2 3 ​ 2 n m<\frac{2}{3}2^{n}, then f ⁡ ( m) < m ​ n / 2 f(m)<mn/2. From this, one might reasonably assume that the constant 2 3 \frac{2}{3} in Corollary 1.2 is hard to improve to any constant 2 3 − ϵ \frac{2}{3}-\epsilon. But in the extremal examples for f ⁡ ( m) f(m), the family 𝒜 \mathcal{A} is very asymmetric — indeed, there is a single element which is in every set of 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{P}(n)\setminus\mathcal{A} — and so 𝒜 \mathcal{A} is in a sense far away from being a counterexample to the union-closed conjecture. In this paper, we prove a stability result for the union-closed size problem for union-closed families 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) with | 𝒜 | ≥ 2 n − 1 |\mathcal{A}|\geq 2^{n-1}. Roughly speaking, we show that if ‖ 𝒜 ‖ ||\mathcal{A}|| is close to the maximum possible then 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{P}(n)\setminus\mathcal{A} has an element of high degree — this result is Theorem 3.1. This enables us to extend Theorem 1.1.

###### Theorem 1.3.

There is a positive constant c 1 c_{1} such that if 𝒜 \mathcal{A} is a counterexample to the union-closed conjecture in 𝒫 ⁡ ( n) \mathcal{P}(n), and ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A} with | ℬ | = m |\mathcal{B}|=m, then

 | ‖ ℐ ⁡ ( m) ‖ > m ⁡ ( n / 2 − 1 + c 1). ||\mathcal{I}(m)||>m(n/2-1+c_{1}). |  |

Using simple bounds on ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)||, this extends slightly the range where we can prove the union-closed conjecture.

###### Corollary 1.4.

There is a positive constant c 2 c_{2} such that the union-closed conjecture holds for all union-closed familes 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) with | 𝒜 | ≥ 2 n ​ ( 2 / 3 − c 2) |\mathcal{A}|\geq 2^{n}(2/3-c_{2}).

In fact, we shall prove these theorems with bounds of c 1 ≥ 1 / 24 c_{1}\geq 1/24 and c 2 ≥ 1 / 104 c_{2}\geq 1/104.

The rest of the paper is organised as follows. In Section 2, we define the concepts needed in the proofs of our main theorems — in particular down-compressions and simply rooted families, which shall be at the heart of our argument. In Section 3 we state Theorem 3.1, our stability result for Theorem 1.1. In Section 4, we prove Theorem 3.1, and use it to prove Theorem 1.3. In Section 5 we bound ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)||, proving Corollary 1.4 from Theorem 1.3. In Section 6 we prove a slightly stronger form of Theorem 3.1, which improves the constants c 1 c_{1} and c 2 c_{2} a little — this is left out of the main proof for the sake of clarity.

## 2 Definitions

In this section, we recall some concepts used by Reimer [8] and Balla, Bollobás and Eccles [1] in their work on the union-closed size problem. Central to both of those papers are *compressions*. Up- and down-compressions are by now standard; see for example Bollobás and Leader [2]. For a family ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) and i ∈ [n] i\in[n], we define the *down-compression of ℬ \mathcal{B} in direction i i*, denoted d i ​ ( ℬ) d_{i}(\mathcal{B}), by defining

 | d ( i, ℬ) ( B) = { B − i: i ∈ B, B − i ∉ ℬ B: otherwise, d_{(i,\mathcal{B})}(B)=\begin{cases}B-i:i\in B,\,B-i\notin\mathcal{B}\\ B:\mathrm{otherwise,}\end{cases} |  |

and d i ​ ( ℬ) = { d ( i, ℬ) ​ ( B): B ∈ ℬ } d_{i}(\mathcal{B})=\{d_{(i,\mathcal{B})}(B):B\in\mathcal{B}\}. A down-compression of a family ℬ \mathcal{B} is equivalent to an up-compression on its complement in 𝒫 ⁡ ( n) \mathcal{P}(n), in that

 | 𝒫 ⁡ ( n) ∖ d i ​ ( ℬ) = u i ​ ( 𝒫 ⁡ ( n) ∖ ℬ), \mathcal{P}(n)\setminus d_{i}(\mathcal{B})=u_{i}(\mathcal{P}(n)\setminus\mathcal{B}), |  | (1) |

where u i u_{i} is the up-compression in direction i i, defined analogously to d i d_{i}. Also, for ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) we define d ⁡ ( ℬ) d(\mathcal{B}) to be d n ​ … ​ d 1 ​ ( ℬ) d_{n}\dots d_{1}(\mathcal{B}), the compression obtained by applying the compressions d i d_{i} to ℬ \mathcal{B} for 1 ≤ i ≤ n 1\leq i\leq n, starting with d 1 d_{1}.

For B ∈ ℬ B\in\mathcal{B} we define d ℬ ​ ( B) d_{\mathcal{B}}(B) to be the image of B B under the down-compression d ℬ d_{\mathcal{B}}; that is, letting ℬ i \mathcal{B}_{i} = d i ​ … ​ d 1 ​ ( ℬ) d_{i}\dots d_{1}(\mathcal{B}), we define

 | d ℬ ​ ( B) = d ( n, ℬ n − 1) ​ … ​ d ( 2, ℬ 1) ​ d ( 1, ℬ) ​ ( B); d_{\mathcal{B}}(B)=d_{(n,\mathcal{B}_{n-1})}\dots d_{(2,\mathcal{B}_{1})}d_{(1,\mathcal{B})}(B); |  |

so d ℬ ​ ( B) d_{\mathcal{B}}(B) is the set we get by following B B through the compressions d i d_{i}. Similarly, we shall often want to consider the family ℬ \mathcal{B} after some of the compressions d i d_{i} have been applied; to this end we define D k ​ ( ℬ) = d k ​ … ​ d 1 ​ ( ℬ) D_{k}(\mathcal{B})=d_{k}\dots d_{1}(\mathcal{B}), the family after compressing in directions i i for 1 ≤ i ≤ k 1\leq i\leq k, and for B ∈ ℬ B\in\mathcal{B} we define D ( ℬ, k) ​ ( B) = d ( k, ℬ k − 1) ​ … ​ d ( 1, ℬ) ​ ( B) D_{(\mathcal{B},k)}(B)=d_{(k,\mathcal{B}_{k-1})}\dots d_{(1,\mathcal{B})}(B), the image of the set B B in D k ​ ( ℬ) D_{k}(\mathcal{B}).

Following the approach of [1], we shall view the complement of a union-closed family as a simply rooted family — this perspective is crucial for our proof of Theorem 1.3. We call a family ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n)*simply rooted*if for every ∅ ≠ B ∈ ℬ \emptyset\neq B\in\mathcal{B}, there is some b ∈ B b\in B with [{ b }, B] ⊆ ℬ [\{b\},B]\subseteq\mathcal{B}. The following simple observation was made in [1].

###### Observation 2.1.

Let 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n), and ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A}. Then ℬ \mathcal{B} is a simply rooted family if and only if 𝒜 \mathcal{A} is a union-closed family.

###### Proof.

The family 𝒜 \mathcal{A} is union-closed exactly when for every B ∉ 𝒜 B\notin\mathcal{A} we have

 | ⋃ B ′ ⊆ B, B ′ ∈ 𝒜 B ′ ≠ B, \bigcup_{B^{\prime}\subseteq B,\,B^{\prime}\in\mathcal{A}}B^{\prime}\neq B, |  |

which is in turn true exactly when [{ b }, B] ⊆ ℬ [\{b\},B]\subseteq\mathcal{B} for some b ∈ B b\in B. ∎

Finally, we recall the colex order on ℕ ( < ∞) \mathbb{N}^{(<\infty)}, the collection of finite sets of positive integers, and some of its standard properties. Given A A and B B sets in ℕ ( < ∞) \mathbb{N}^{(<\infty)}, we define the colex order < < by

 | A < B ⇔ max ⁡ ( A ​ △ ​ B) ∈ B. A<B\iff\max(A\triangle B)\in B. |  |

This is a linear order on ℕ ( < ∞) \mathbb{N}^{(<\infty)}. We write ℐ ⁡ ( m) \mathcal{I}(m) for the initial segment of this order of length m m; so, for example, ℐ ⁡ ( 9) = { ∅, 1, 2, 12, 3, 13, 23, 123, 4 } \mathcal{I}(9)=\{\emptyset,1,2,12,3,13,23,123,4\}, where we write 13 13 for the set { 1, 3 } \{1,3\}. Also, a family of sets 𝒟 \mathcal{D} is called a *down-set*if for every A ∈ 𝒟 A\in\mathcal{D} we have 𝒫 ⁡ ( A) ⊆ 𝒟 \mathcal{P}(A)\subseteq\mathcal{D}. The following result is a well-known consequence of the fundamental theorem of Kruskal [7] and Katona [6].

###### Lemma 2.2.

If 𝒟 \mathcal{D} is a down-set, then ‖ 𝒟 ‖ ≤ ‖ ℐ ⁡ ( | 𝒟 |) ‖ ||\mathcal{D}||\leq||\mathcal{I}(|\mathcal{D}|)||. ∎

The other fact which we shall need about initial segments of colex is the following lemma, which is a simple corollary of Lemma 2.2 – see for example [1].

###### Lemma 2.3.

Let m 1 m_{1} and m 2 m_{2} be positive integers. Then

 | ‖ ℐ ⁡ ( m 1) ‖ + ‖ ℐ ⁡ ( m 2) ‖ ≤ | | ℐ ⁡ ( m 1 + m 2) | | − min ⁡ ( m 1, m 2). ||\mathcal{I}(m_{1})||+||\mathcal{I}(m_{2})||\leq||\mathcal{I}(m_{1}+m_{2})||-\min(m_{1},m_{2}). |  |

This can be proved for m 1 ≥ m 2 m_{1}\geq m_{2} by applying Lemma 2.2 to the down-set ℐ ⁡ ( m 1) ∪ { A + N: A ∈ ℐ ⁡ ( m 2) } \mathcal{I}(m_{1})\cup\{A+N:A\in\mathcal{I}(m_{2})\}, for a sufficiently large integer N N. ∎

## 3 Stability for sizes of simply rooted families

For a simply rooted family ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n), a set B ∈ ℬ B\in\mathcal{B} and an element i ∈ [n] i\in[n], we say that B B is *ℬ \mathcal{B} -rooted at i i*if i ∈ B i\in B and the cube [{ i }, B] [\{i\},B] is contained in ℬ \mathcal{B}. Then for a set S ⊆ [n] S\subseteq[n], we define ℬ S \mathcal{B}_{S} to be those sets of ℬ \mathcal{B} which are ℬ \mathcal{B} -rooted at some i ∈ S i\in S.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family. By Observation 2.1 the family 𝒫 ⁡ ( n) ∖ ℬ \mathcal{P}(n)\setminus\mathcal{B} is union-closed, and so Theorem 1.1 gives us

 | ‖ ℬ ‖ = ‖ 𝒫 ⁡ ( n) ‖ − ‖ 𝒜 ‖ ≤ ‖ 𝒫 ⁡ ( n) ‖ − f ⁡ ( | 𝒜 |) = | | ℐ ⁡ ( | ℬ |) | | + | ℬ |. ||\mathcal{B}||=||\mathcal{P}(n)||-||\mathcal{A}||\leq||\mathcal{P}(n)||-f(|\mathcal{A}|)=||\mathcal{I}(|\mathcal{B}|)||+|\mathcal{B}|. |  | (2) |

For any m m, the family ℬ = { B + n: B ∈ ℐ ⁡ ( m) } \mathcal{B}=\{B+n:B\in\mathcal{I}(m)\} makes this inequality tight for n = ⌈ l ​ o ​ g 2 ​ ( m) ⌉ + 1 n=\lceil log_{2}(m)\rceil+1 — every set in this family is ℬ \mathcal{B} -rooted at n n. In fact, up to isomorphism this is the only simply rooted family of m m sets for which equality holds; this is a consequence of the uniqueness of extremal families for f ⁡ ( m) f(m), which was proved in [1]. In particular, if ‖ ℬ ‖ = ‖ ℐ ⁡ ( | ℬ |) ‖ + | ℬ | ||\mathcal{B}||=||\mathcal{I}(|\mathcal{B}|)||+|\mathcal{B}| then ℬ { i } = ℬ \mathcal{B}_{\{i\}}=\mathcal{B} for some i ∈ [n] i\in[n]. The following result extends this, showing that if ‖ ℬ ‖ ||\mathcal{B}|| is close to ‖ ℐ ⁡ ( m) ‖ + m ||\mathcal{I}(m)||+m then | ℬ { i } | |\mathcal{B}_{\{i\}}| is large for some i i.

###### Theorem 3.1.

Let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n) with | ℬ | = m |\mathcal{B}|=m, and p ∈ [0, 1] p\in[0,1]. Suppose that | ℬ { i } | ≤ p ​ m |\mathcal{B}_{\{i\}}|\leq pm for all i ∈ [n] i\in[n]. Then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n. ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{2}(1/12-p^{2}/12)/2^{n}. |  |

Theorem 3.1 provides a stability result for Theorem 1.1 for union-closed families 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) with | 𝒜 | ≥ 2 n − 1 |\mathcal{A}|\geq 2^{n-1}. Indeed, let 𝒜 \mathcal{A} be such a family and set ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A} with | ℬ | = m |\mathcal{B}|=m. Since ℬ \mathcal{B} is a simply rooted family by Observation 2.1, if | ℬ { i } | ≤ p ​ m |\mathcal{B}_{\{i\}}|\leq pm for all i i we have

 | ‖ 𝒜 ‖ \displaystyle||\mathcal{A}|| | = ‖ 𝒫 ⁡ ( n) ‖ − ‖ ℬ ‖ \displaystyle=||\mathcal{P}(n)||-||\mathcal{B}|| |  |

 |  | ≥ | | 𝒫 ⁡ ( n) | | − ‖ ℐ ⁡ ( m) ‖ − m + m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n \displaystyle\geq||\mathcal{P}(n)||-||\mathcal{I}(m)||-m+m^{2}(1/12-p^{2}/12)/2^{n} |  |

 |  | = f ⁡ ( | 𝒜 |) + m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n. \displaystyle=f(|\mathcal{A}|)+m^{2}(1/12-p^{2}/12)/2^{n}. |  |

Hence if ‖ 𝒜 ‖ ||\mathcal{A}|| is close to f ⁡ ( | 𝒜 |) f(|\mathcal{A}|), some element of [n] [n] appears in nearly all the sets of ℬ \mathcal{B}.

## 4 Proofs of main theorems

Now we turn to the proofs of Theorems 3.1 and 1.3. First we give two definitions we shall need in the proof of Theorem 3.1. For a finite set B B, let δ ​ B = { B − i: i ∈ B } \delta B=\{B-i:i\in B\} be the *shadow of B B*. Given a simply rooted family ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n), we call a set B ∈ ℬ B\in\mathcal{B} a *bad set of ℬ \mathcal{B}*if either δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B} or d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. We call a set B ∈ ℬ B\in\mathcal{B} that is not bad a *good set of ℬ \mathcal{B}*.

We now sketch the proof of Theorem 3.1. In Lemmas 4.3 and 4.4 we shall show that if ℬ \mathcal{B} has many bad sets then ‖ ℬ ‖ ||\mathcal{B}|| is much less than ‖ ℐ ⁡ ( m) ‖ + m ||\mathcal{I}(m)||+m; as a result, it is enough to show that a simply rooted family satisfying the condition of Theorem 3.1 has many bad sets. Given such a simply rooted family ℬ \mathcal{B}, we shall then write ℬ \mathcal{B} as ℬ S ∪ ℬ T \mathcal{B}_{S}\cup\mathcal{B}_{T}, where S ∪ T S\cup T is a partition of [n] [n]. Since no ℬ { i } \mathcal{B}_{\{i\}} is too large, we can do this so both ℬ S \mathcal{B}_{S} and ℬ T \mathcal{B}_{T} are fairly large. If their intersection | ℬ S ∩ ℬ T | |\mathcal{B}_{S}\cap\mathcal{B}_{T}| is large, then we conclude that ℬ \mathcal{B} has many bad sets, since all the sets of ℬ S ∩ ℬ T \mathcal{B}_{S}\cap\mathcal{B}_{T} are ℬ \mathcal{B} -rooted at two elements of [n] [n], and so are bad sets of ℬ \mathcal{B}. If, on the other hand, | ℬ S ∩ ℬ T | |\mathcal{B}_{S}\cap\mathcal{B}_{T}| is small, we shall show in Corollary 4.10 that ℬ \mathcal{B} still has many bad sets. We prove this by considering the down-sets d ⁡ ( ℬ S) d(\mathcal{B}_{S}) and d ⁡ ( ℬ T) d(\mathcal{B}_{T}); since these are large down-sets in 𝒫 ⁡ ( n) \mathcal{P}(n), they have a large intersection, and in Lemma 4.9 we shall show that sets in this intersection correspond to sets in either ℬ S ∩ ℬ T \mathcal{B}_{S}\cap\mathcal{B}_{T} or bad sets of ℬ \mathcal{B}.

### 4.1 Applying down-compressions to simply rooted families

In Lemma 4.3, we shall show that if ℬ \mathcal{B} has many sets with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B then ‖ ℬ ‖ ||\mathcal{B}|| is small. In order to prove this lemma, we first recall some results of Reimer [8] on union-closed families, restating them in terms of simply rooted families.

###### Lemma 4.1.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family. Then

1. 1.

d ⁡ ( ℬ) d(\mathcal{B}) is a down-set,

2. 2.

for 1 ≤ k ≤ n 1\leq k\leq n, D k ​ ( ℬ) D_{k}(\mathcal{B}) is a simply rooted family. ∎

We now prove some further basic properties of down-compressions on simply rooted families.

###### Lemma 4.2.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family. Then

1. 1.

for B ∈ ℬ B\in\mathcal{B} and 1 ≤ k ≤ n 1\leq k\leq n, if D ( ℬ, k) ​ ( B) ≠ B D_{(\mathcal{B},k)}(B)\neq B then 𝒫 ⁡ ( D ( ℬ, k) ​ ( B)) ⊆ D k ​ ( ℬ) \mathcal{P}(D_{(\mathcal{B},k)}(B))\subseteq D_{k}(\mathcal{B}),

2. 2.

for B ∈ ℬ B\in\mathcal{B}, | B ∖ d ℬ ​ ( B) | ≤ 1 |B\setminus d_{\mathcal{B}}(B)|\leq 1.

###### Proof.

Suppose that D ( ℬ, j) ​ ( B) ≠ B D_{(\mathcal{B},j)}(B)\neq B for some j ∈ [n] j\in[n]; otherwise both parts of the lemma hold for the set B B. Let ℓ \ell be minimal with D ( ℬ, ℓ) ​ ( B) ≠ B D_{(\mathcal{B},\ell)}(B)\neq B. Then D ( ℬ, ℓ) ​ ( B) = B − ℓ D_{(\mathcal{B},\ell)}(B)=B-\ell, and B − ℓ ∉ D ℓ − 1 ​ ( ℬ) B-\ell\notin D_{\ell-1}(\mathcal{B}). Also, by Part 2 of Lemma 4.1, D ℓ − 1 ​ ( ℬ) D_{\ell-1}(\mathcal{B}) is simply rooted, and so there is some i ∈ B i\in B such that [{ i }, B] ⊆ D ℓ − 1 ​ ( ℬ) [\{i\},B]\subseteq D_{\ell-1}(\mathcal{B}) — and since B − ℓ ∉ D ℓ − 1 ​ ( ℬ) B-\ell\notin D_{\ell-1}(\mathcal{B}), we must have i = ℓ i=\ell. Hence 𝒫 ⁡ ( B − ℓ) ⊆ D ℓ ​ ( ℬ) \mathcal{P}(B-\ell)\subseteq D_{\ell}(\mathcal{B}), since if a family ℱ \mathcal{F} contains S + ℓ S+\ell for some set S S then d ℓ ​ ( ℱ) d_{\ell}(\mathcal{F}) contains S S.

Now, 𝒫 ⁡ ( B − ℓ) \mathcal{P}(B-\ell) is a down-set which is contained in D ℓ ​ ( ℬ) D_{\ell}(\mathcal{B}), and so any down-compression of the family D ℓ ​ ( ℬ) D_{\ell}(\mathcal{B}) fixes every set in 𝒫 ⁡ ( B − ℓ) \mathcal{P}(B-\ell). For Part 1 of the lemma, if D ( ℬ, k) ​ ( B) ≠ B D_{(\mathcal{B},k)}(B)\neq B for some k ∈ [n] k\in[n], k ≥ ℓ k\geq\ell, and so D k ​ ( ℬ) = d k ​ … ​ d l + 1 ​ ( D l ​ ( ℬ)) D_{k}(\mathcal{B})=d_{k}\dots d_{l+1}(D_{l}(\mathcal{B})). Hence we have D ( ℬ, k) ​ ( B) = B − ℓ D_{(\mathcal{B},k)}(B)=B-\ell and

 | 𝒫 ⁡ ( D ( ℬ, k) ​ ( B)) = 𝒫 ⁡ ( B − ℓ) ⊆ D k ​ ( ℬ), \mathcal{P}(D_{(\mathcal{B},k)}(B))=\mathcal{P}(B-\ell)\subseteq D_{k}(\mathcal{B}), |  |

so Part 1 holds. For Part 2, we have d ℬ ​ ( B) = D ( ℬ, ℓ) ​ ( B) = B − ℓ d_{\mathcal{B}}(B)=D_{(\mathcal{B},\ell)}(B)=B-\ell, so | B ∖ d ℬ ​ ( B) | = 1 |B\setminus d_{\mathcal{B}}(B)|=1. ∎

From Lemmas 4.1 and 4.2, we immediately get a bound on the total size of a simply rooted family.

###### Lemma 4.3.

Let ℬ \mathcal{B} be a simply rooted family, let | ℬ | = m |\mathcal{B}|=m, and let m ′ m^{\prime} be the number of sets B ∈ ℬ B\in\mathcal{B} with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m ′. ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{\prime}. |  |

###### Proof.

Note that

 | ‖ ℬ ‖ = ‖ d ⁡ ( ℬ) ‖ + ∑ B ∈ ℬ | B ∖ d ℬ ​ ( B) |. ||\mathcal{B}||=||d(\mathcal{B})||+\sum_{B\in\mathcal{B}}|B\setminus d_{\mathcal{B}}(B)|. |  |

By Part 1 of Lemma 4.1, d ⁡ ( ℬ) d(\mathcal{B}) is a down-set, and so by Lemma 2.2 ‖ d ⁡ ( ℬ) ‖ ||d(\mathcal{B})|| is at most ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)||. Also, by Part 2 of Lemma 4.2, ∑ B ∈ ℬ | B ∖ d ℬ ​ ( B) | \sum_{B\in\mathcal{B}}|B\setminus d_{\mathcal{B}}(B)| is exactly m − m ′ m-m^{\prime}, and so the result follows. ∎

Note that if ℬ \mathcal{B} is a simply rooted family and B ∈ ℬ B\in\mathcal{B}, | δ ​ B ∖ ℬ | ≤ 1 |\delta B\setminus\mathcal{B}|\leq 1. We shall now show that if there are many B ∈ ℬ B\in\mathcal{B} with the entire shadow of B B contained in ℬ \mathcal{B} then Theorem 3.1 holds.

###### Lemma 4.4.

Let ℬ \mathcal{B} be a simply rooted family of size m m, and set m ′ m^{\prime} to be the number of sets B ∈ ℬ B\in\mathcal{B} with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}. Then

 | ‖ ℬ ‖ ≤ ‖ I ⁡ ( m) ‖ + m − m ′. ||\mathcal{B}||\leq||I(m)||+m-m^{\prime}. |  |

We shall deduce this from a more general result. For ℬ \mathcal{B} a finite family of finite sets, we define the *deficiency of ℬ \mathcal{B}*, denoted def ⁡ ( ℬ) \mathrm{def}(\mathcal{B}), to be the number of sets in the shadows of sets B ∈ ℬ B\in\mathcal{B} that are missing from ℬ \mathcal{B} — that is,

 | def ⁡ ( ℬ) = ∑ B ∈ ℬ | δ ⁡ ( B) ∖ ℬ |. \mathrm{def}(\mathcal{B})=\sum_{B\in\mathcal{B}}|\delta(B)\setminus\mathcal{B}|. |  |

Then we have the following lemma concerning the total size of a family of given size and deficiency.

###### Lemma 4.5.

Suppose that ℬ \mathcal{B} is a finite family of finite sets in 𝒫 ⁡ ( n) \mathcal{P}(n), with | ℬ | = m |\mathcal{B}|=m. Then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + def ⁡ ( ℬ). ||\mathcal{B}||\leq||\mathcal{I}(m)||+\mathrm{def}(\mathcal{B}). |  |

We note that Lemma 4.4 is immediate from this lemma, since if ℬ \mathcal{B} is a simply rooted family then for each B B we have | δ ​ B ∖ ℬ | ≤ 1 |\delta B\setminus\mathcal{B}|\leq 1, and there are m ′ m^{\prime} sets B ∈ ℬ B\in\mathcal{B} with | δ ​ B ∖ ℬ | = 0 |\delta B\setminus\mathcal{B}|=0, so def ⁡ ( ℬ) = m − m ′ \mathrm{def}(\mathcal{B})=m-m^{\prime}.

###### Proof.

We apply induction on n n. For n = 1 n=1 the result is easily checked. If n > 1 n>1, we define families of sets ℬ n + \mathcal{B}_{n}^{+} and ℬ n − \mathcal{B}_{n}^{-} by

 | ℬ n + \displaystyle\mathcal{B}^{+}_{n} | = { B ∈ 𝒫 ⁡ ( n − 1): B + n ∈ ℬ }, and \displaystyle=\{B\in\mathcal{P}(n-1):B+n\in\mathcal{B}\},\,\textrm{and} |  |

 | ℬ n − \displaystyle\mathcal{B}^{-}_{n} | = { B ∈ 𝒫 ⁡ ( n − 1): B ∈ ℬ }, \displaystyle=\{B\in\mathcal{P}(n-1):B\in\mathcal{B}\}, |  |

so that | ℬ | = | ℬ n + | + | ℬ n − | |\mathcal{B}|=|\mathcal{B}_{n}^{+}|+|\mathcal{B}_{n}^{-}|, and ‖ ℬ ‖ = ‖ ℬ n + ‖ + ‖ ℬ n − ‖ + | ℬ n + | ||\mathcal{B}||=||\mathcal{B}_{n}^{+}||+||\mathcal{B}_{n}^{-}||+|\mathcal{B}_{n}^{+}|. We define m n + = | ℬ n + | m_{n}^{+}=|\mathcal{B}_{n}^{+}|, and m n − = | ℬ n − | m_{n}^{-}=|\mathcal{B}_{n}^{-}|. Now we count pairs ( B, i) (B,i) such that B ∈ ℬ B\in\mathcal{B}, i ∈ B i\in B and B − i ∉ ℬ B-i\notin\mathcal{B} — these are the pairs which contribute to def ⁡ ( ℬ) \mathrm{def}(\mathcal{B}). We obtain

 | def ⁡ ( ℬ) = \displaystyle\mathrm{def}(\mathcal{B})= | | { B ∈ ℬ, i ∈ [n]: i ≠ n, n ∈ B, B − i ∉ ℬ } | + \displaystyle|\{B\in\mathcal{B},\,i\in[n]:i\neq n,\,n\in B,\,B-i\notin\mathcal{B}\}|+ |  |

 |  | | { B ∈ ℬ, i ∈ [n]: i ≠ n, n ∉ B, B − i ∉ ℬ } | + \displaystyle|\{B\in\mathcal{B},\,i\in[n]:i\neq n,\,n\notin B,\,B-i\notin\mathcal{B}\}|+ |  |

 |  | | { B ∈ ℬ: n ∈ B, B − n ∉ ℬ } | \displaystyle|\{B\in\mathcal{B}:n\in B,\,B-n\notin\mathcal{B}\}| |  |

 |  | = def ⁡ ( ℬ n +) + def ⁡ ( ℬ n −) + | ℬ n + ∖ ℬ n − |. \displaystyle=\mathrm{def}(\mathcal{B}_{n}^{+})+\mathrm{def}(\mathcal{B}_{n}^{-})+|\mathcal{B}_{n}^{+}\setminus\mathcal{B}_{n}^{-}|. |  |

By the induction hypothesis and Lemma 2.3,

 | ‖ ℬ ‖ \displaystyle||\mathcal{B}|| | = ‖ ℬ n + ‖ + ‖ ℬ n − ‖ + | ℬ n + | \displaystyle=||\mathcal{B}_{n}^{+}||+||\mathcal{B}_{n}^{-}||+|\mathcal{B}_{n}^{+}| |  |

 |  | ≤ ‖ ℐ ⁡ ( m n, +) ‖ + | | ℐ ⁡ ( m n, −) | | + m n, + + def ⁡ ( ℬ n +) + def ⁡ ( ℬ n −) \displaystyle\leq||\mathcal{I}(m_{n,+})||+||\mathcal{I}(m_{n,-})||+m_{n,+}+\mathrm{def}(\mathcal{B}_{n}^{+})+\mathrm{def}(\mathcal{B}_{n}^{-}) |  |

 |  | ≤ ‖ ℐ ⁡ ( m) ‖ − min ⁡ ( m n, +, m n, −) + m n, + + def ⁡ ( ℬ) − | ℬ n + ∖ ℬ n − |. \displaystyle\leq||\mathcal{I}(m)||-\min(m_{n,+},m_{n,-})+m_{n,+}+\mathrm{def}(\mathcal{B})-|\mathcal{B}_{n}^{+}\setminus\mathcal{B}_{n}^{-}|. |  |

If m n, + ≤ m n, − m_{n,+}\leq m_{n,-} then ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + def ⁡ ( ℬ) ||\mathcal{B}||\leq||\mathcal{I}(m)||+\mathrm{def}(\mathcal{B}), and so we are done. If not, then since | ℬ n + ∖ ℬ n − | ≥ m n, + − m n, − |\mathcal{B}_{n}^{+}\setminus\mathcal{B}_{n}^{-}|\geq m_{n,+}-m_{n,-} we have

 | ‖ ℬ ‖ \displaystyle||\mathcal{B}|| | ≤ ‖ ℐ ⁡ ( m) ‖ − m n, − + m n, + + def ⁡ ( ℬ) − ( m n, + − m n, −) \displaystyle\leq||\mathcal{I}(m)||-m_{n,-}+m_{n,+}+\mathrm{def}(\mathcal{B})-(m_{n,+}-m_{n,-}) |  |

 |  | = ‖ ℐ ⁡ ( m) ‖ + def ⁡ ( ℬ), \displaystyle=||\mathcal{I}(m)||+\mathrm{def}(\mathcal{B}), |  |

and so we are also done. ∎

###### Remark.

For positive integers k k and m m, there is a family ℬ \mathcal{B} with | ℬ | = m |\mathcal{B}|=m and def ⁡ ( ℬ) = k ​ m \mathrm{def}(\mathcal{B})=km so that the inequality in Lemma 4.5 is tight — we can take ℬ = { A ∪ { N, …, N + k − 1 }: A ∈ ℐ ⁡ ( m) } \mathcal{B}=\{A\cup\{N,\dots,N+k-1\}:A\in\mathcal{I}(m)\}, for N N a sufficiently large integer. For general | ℬ | |\mathcal{B}| and def ⁡ ( ℬ) \mathrm{def}(\mathcal{B}), there is not always a family ℬ \mathcal{B} so that the inequality is tight; for example if | ℬ | = 2 |\mathcal{B}|=2 and def ⁡ ( ℬ) = 3 \mathrm{def}(\mathcal{B})=3, then in fact ‖ ℬ ‖ ≤ 3 = ‖ ℐ ⁡ ( 2) ‖ + 2 ||\mathcal{B}||\leq 3=||\mathcal{I}(2)||+2.

Together, Lemmas 4.3 and 4.4 show that if ℬ \mathcal{B} has many bad sets then ‖ ℬ ‖ ||\mathcal{B}|| is small. Indeed, if ℬ \mathcal{B} has b b bad sets then either at least b / 2 b/2 sets of ℬ \mathcal{B} have δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, or at least b / 2 b/2 have d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. By Lemma 4.4 in the first case, and Lemma 4.3 in the second,

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( | ℬ |) ‖ + | ℬ | − b / 2. ||\mathcal{B}||\leq||\mathcal{I}(|\mathcal{B}|)||+|\mathcal{B}|-b/2. |  |

Our aim now is to give a lower bound on the number of bad sets of ℬ \mathcal{B}. To do this, we shall focus on how the down-compression d ℬ d_{\mathcal{B}} affects the sets of a simply rooted family ℬ \mathcal{B}.

###### Lemma 4.6.

Let ℬ \mathcal{B} be a simply rooted family, and let B ∈ ℬ B\in\mathcal{B} with B − b ∉ ℬ B-b\notin\mathcal{B} for some b ∈ B b\in B. Then d ℬ ​ ( B) ∈ { B, B − b } d_{\mathcal{B}}(B)\in\{B,B-b\}.

###### Proof.

Since ℬ \mathcal{B} is a simply rooted family, for some a ∈ B a\in B we have [{ a }, B] ⊆ ℬ [\{a\},B]\subseteq\mathcal{B}. But B − b ∉ ℬ B-b\notin\mathcal{B}, and so a = b a=b. We now consider D b − 1 ​ ( ℬ) D_{b-1}(\mathcal{B}), the family obtained by applying the compressions d 1, …, d b − 1 d_{1},\dots,d_{b-1} to ℬ \mathcal{B}, starting with d 1 d_{1}. We note that the cube [{ b }, B] [\{b\},B] is fixed when we apply any down-compression d i d_{i} with i ≠ b i\neq b to ℬ \mathcal{B}; indeed, if A ∈ [{ b }, B] A\in[\{b\},B] then A − i ∈ [{ b }, B] A-i\in[\{b\},B], so d ( ℬ, i) ​ ( A) = A d_{(\mathcal{B},i)}(A)=A. Hence we have [{ b }, B] ⊆ D b − 1 ​ ( ℬ) [\{b\},B]\subseteq D_{b-1}(\mathcal{B}).

We now consider two cases. If B − b ∈ D b − 1 ​ ( ℬ) B-b\in D_{b-1}(\mathcal{B}) then it is D ( ℬ, b − 1) ​ ( B ′) D_{(\mathcal{B},b-1)}(B^{\prime}) for some B ′ ∈ ℬ B^{\prime}\in\mathcal{B}. Hence D ( ℬ, b − 1) ​ ( B ′) ≠ B ′ D_{(\mathcal{B},b-1)}(B^{\prime})\neq B^{\prime}, and so by Part 1 of Lemma 4.2 we have 𝒫 ⁡ ( B − b) ⊆ D b − 1 ​ ( ℬ) \mathcal{P}(B-b)\subseteq D_{b-1}(\mathcal{B}). Since [{ b }, B] ⊆ D b − 1 ​ ( B) [\{b\},B]\subseteq D_{b-1}(B), we then have 𝒫 ​ ( B) ⊆ D b − 1 ​ ( ℬ) \mathcal{P}(B)\subseteq D_{b-1}(\mathcal{B}) and so d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. On the other hand, if B − b ∉ D b − 1 ​ ( ℬ) B-b\notin D_{b-1}(\mathcal{B}) then D ( ℬ, b) ​ ( B) = B − b D_{(\mathcal{B},b)}(B)=B-b, and by Part 2 of Lemma 4.2 we have d ℬ ​ ( B) = B − b d_{\mathcal{B}}(B)=B-b. ∎

In the next lemma, we show that if ℬ ′ ⊆ ℬ \mathcal{B}^{\prime}\subseteq\mathcal{B} are simply rooted families, then sets in ℬ ′ \mathcal{B}^{\prime} which are fixed by d ℬ ′ d_{\mathcal{B}^{\prime}} are also fixed by d ℬ d_{\mathcal{B}}.

###### Lemma 4.7.

Let ℬ ′ ⊆ ℬ \mathcal{B}^{\prime}\subseteq\mathcal{B} be simply rooted families, and let B ∈ ℬ ′ B\in\mathcal{B}^{\prime} with d ℬ ′ ​ ( B) = B d_{\mathcal{B}^{\prime}}(B)=B. Then d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B.

###### Proof.

By induction on k k, it is easy to show that for all 1 ≤ k ≤ n 1\leq k\leq n we have D k ​ ( ℬ ′) ⊆ D k ​ ( ℬ) D_{k}(\mathcal{B}^{\prime})\subseteq D_{k}(\mathcal{B}). Indeed, if ℱ ′ ⊆ ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}^{\prime}\subseteq\mathcal{F}\subseteq\mathcal{P}(n), then for any i ∈ [n] i\in[n] we have d i ​ ( ℱ ′) ⊆ d i ​ ( ℱ) d_{i}(\mathcal{F}^{\prime})\subseteq d_{i}(\mathcal{F}). Since d ℬ ′ ​ ( B) = B d_{\mathcal{B}^{\prime}}(B)=B, for all k ∈ B k\in B we must have B − k ∈ D k − 1 ​ ( ℬ ′) B-k\in D_{k-1}(\mathcal{B}^{\prime}), and so also B − k ∈ D k − 1 ​ ( ℬ) B-k\in D_{k-1}(\mathcal{B}). This is exactly the condition we need to guarantee d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. ∎

From the previous lemmas, we can read out a result on how the good sets of ℬ \mathcal{B} behave under down-compressions d ℬ ′ d_{\mathcal{B}^{\prime}} for simply rooted families ℬ ′ ⊆ ℬ \mathcal{B}^{\prime}\subseteq\mathcal{B}.

###### Lemma 4.8.

Let ℬ ′ ⊆ ℬ \mathcal{B}^{\prime}\subseteq\mathcal{B} be simply rooted families, with B ∈ ℬ ′ B\in\mathcal{B}^{\prime} a good set of ℬ \mathcal{B}. Then d ℬ ​ ( B) = d ℬ ′ ​ ( B) d_{\mathcal{B}}(B)=d_{\mathcal{B}^{\prime}}(B).

###### Proof.

Since B B is a good set of ℬ \mathcal{B}, for some b ∈ B b\in B we have B − b ∉ ℬ B-b\notin\mathcal{B}, and by Part 2 of Lemma 4.2 we have d ℬ ​ ( B) = B − a d_{\mathcal{B}}(B)=B-a for some a ∈ B a\in B. So by Lemma 4.7, d ℬ ′ ​ ( B) ≠ B d_{\mathcal{B}^{\prime}}(B)\neq B, and so d ℬ ′ ​ ( B) = B − c d_{\mathcal{B}^{\prime}}(B)=B-c for some c ∈ B c\in B. But by Lemma 4.6, a = c = b a=c=b, and the result holds. ∎

### 4.2 Unions of simply rooted families

Now we are in a position to prove a lemma about simply rooted families ℬ \mathcal{B} which can be decomposed as the union of two other simply rooted families ℬ 1 ∪ ℬ 2 \mathcal{B}_{1}\cup\mathcal{B}_{2}. Specifically, we show that if ℬ 1 \mathcal{B}_{1} and ℬ 2 \mathcal{B}_{2} have small intersection, but the down-sets d ⁡ ( ℬ 1) d(\mathcal{B}_{1}) and d ⁡ ( ℬ 2) d(\mathcal{B}_{2}) have large intersection, then ℬ \mathcal{B} has many bad sets.

###### Lemma 4.9.

Let ℬ \mathcal{B}, ℬ 1 \mathcal{B}_{1} and ℬ 2 \mathcal{B}_{2} be simply rooted families, with ℬ 1 ∪ ℬ 2 = ℬ \mathcal{B}_{1}\cup\mathcal{B}_{2}=\mathcal{B}. Let b b be the number of bad sets of ℬ \mathcal{B}. Then

 | | d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) | ≤ b + | ℬ 1 ∩ ℬ 2 |. |d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2})|\leq b+|\mathcal{B}_{1}\cap\mathcal{B}_{2}|. |  |

###### Proof.

Let B B be a set in d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2}). Then B = d ℬ 1 ​ ( B 1) = d ℬ 2 ​ ( B 2) B=d_{\mathcal{B}_{1}}(B_{1})=d_{\mathcal{B}_{2}}(B_{2}), for some B 1 ∈ ℬ 1 B_{1}\in\mathcal{B}_{1} and B 2 ∈ ℬ 2 B_{2}\in\mathcal{B}_{2}. If both B 1 B_{1} and B 2 B_{2} are good sets of ℬ \mathcal{B} then, applying Lemma 4.8,

 | d ℬ ​ ( B 1) = d ℬ 1 ​ ( B 1) = d ℬ 2 ​ ( B 2) = d ℬ ​ ( B 2). d_{\mathcal{B}}(B_{1})=d_{\mathcal{B}_{1}}(B_{1})=d_{\mathcal{B}_{2}}(B_{2})=d_{\mathcal{B}}(B_{2}). |  |

But d ℬ: ℬ → d ⁡ ( ℬ) d_{\mathcal{B}}:\mathcal{B}\to d(\mathcal{B}) is injective, and so B 1 = B 2 ∈ ℬ 1 ∩ ℬ 2 B_{1}=B_{2}\in\mathcal{B}_{1}\cap\mathcal{B}_{2}. On the other hand, if B 1 B_{1} and B 2 B_{2} are not both good sets of ℬ \mathcal{B}, B B is the d ℬ 1 d_{\mathcal{B}_{1}} image of a bad set of ℬ \mathcal{B} in ℬ 1 \mathcal{B}_{1}, or the d ℬ 2 d_{\mathcal{B}_{2}} image of a bad set of ℬ \mathcal{B} in ℬ 2 \mathcal{B}_{2}. Hence the number of sets in d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2}) is at most the number of good sets of ℬ \mathcal{B} in ℬ 1 ∩ ℬ 2 \mathcal{B}_{1}\cap\mathcal{B}_{2}, plus the number of bad sets of ℬ \mathcal{B} in ℬ 1 \mathcal{B}_{1}, plus the number of bad sets of ℬ \mathcal{B} in ℬ 2 \mathcal{B}_{2} — which is precisely b + | ℬ 1 ∩ ℬ 2 | b+|\mathcal{B}_{1}\cap\mathcal{B}_{2}|.∎

This result has an immediate corollary using Harris’s Lemma [5], which states that down-sets in the cube are positively correlated. Precisely, if 𝒟 1 \mathcal{D}_{1} and 𝒟 2 \mathcal{D}_{2} are down-sets in 𝒫 ⁡ ( n) \mathcal{P}(n), then | 𝒟 1 ∩ 𝒟 2 | ≥ 2 − n ​ | 𝒟 1 | ​ | 𝒟 2 | |\mathcal{D}_{1}\cap\mathcal{D}_{2}|\geq 2^{-n}|\mathcal{D}_{1}||\mathcal{D}_{2}|. Applying this to the down-sets d ⁡ ( ℬ 1) d(\mathcal{B}_{1}) and d ⁡ ( ℬ 2) d(\mathcal{B}_{2}), and using the fact that | d ⁡ ( ℬ i) | = | ℬ i | |d(\mathcal{B}_{i})|=|\mathcal{B}_{i}| for i = 1 i=1 and 2 2, we get the following result.

###### Corollary 4.10.

Let ℬ \mathcal{B}, ℬ 1 \mathcal{B}_{1} and ℬ 2 \mathcal{B}_{2} be simply rooted families, with ℬ 1 ∪ ℬ 2 = ℬ \mathcal{B}_{1}\cup\mathcal{B}_{2}=\mathcal{B}. Let b b be the number of bad sets of ℬ \mathcal{B}. Then

 | 2 − n ​ | ℬ 1 | ​ | ℬ 2 | ≤ b + | ℬ 1 ∩ ℬ 2 |. 2^{-n}|\mathcal{B}_{1}||\mathcal{B}_{2}|\leq b+|\mathcal{B}_{1}\cap\mathcal{B}_{2}|. |  |

∎

Next we shall choose simply rooted families ℬ 1 \mathcal{B}_{1} and ℬ 2 \mathcal{B}_{2} to which we can apply this result to give a lower bound on the number of bad sets in ℬ \mathcal{B}. Recall that for a set S ⊆ [n] S\subseteq[n] and a simply rooted family ℬ \mathcal{B}, ℬ S \mathcal{B}_{S} is the family consisting those elements of B B which are ℬ \mathcal{B} -rooted at some element of S S. We note that ℬ S \mathcal{B}_{S} is a simply rooted family; if B B is ℬ \mathcal{B} -rooted at s ∈ S s\in S, every set of [{ s }, B] [\{s\},B] is ℬ \mathcal{B} -rooted at s s and hence is in ℬ S \mathcal{B}_{S}, so B B is ℬ S \mathcal{B}_{S} -rooted at s s. We restate Corollary 4.10 for these simply rooted families.

###### Lemma 4.11.

Let ( S, T) (S,T) be a partition of [n] [n] into two disjoint sets, and let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n). Let b 1 b_{1} be the number of sets B ∈ ℬ ∖ ( ℬ S ∩ ℬ T) B\in\mathcal{B}\setminus(\mathcal{B}_{S}\cap\mathcal{B}_{T}) with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, let b 2 = | ℬ S ∩ ℬ T | b_{2}=|\mathcal{B}_{S}\cap\mathcal{B}_{T}|, and let b 3 b_{3} be the number of sets B ∈ ℬ B\in\mathcal{B} with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Then

 | 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + 2 ​ b 2 + b 3. 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+2b_{2}+b_{3}. |  |

###### Proof.

Note that since ℬ \mathcal{B} is a simply rooted family, ℬ S \mathcal{B}_{S} and ℬ T \mathcal{B}_{T} are simply rooted families and ℬ S ∪ ℬ T = ℬ \mathcal{B}_{S}\cup\mathcal{B}_{T}=\mathcal{B}. Also, there are at most b 1 + b 3 b_{1}+b_{3} bad sets of ℬ \mathcal{B} not in ℬ S ∩ ℬ T \mathcal{B}_{S}\cap\mathcal{B}_{T}, and at most b 2 b_{2} in ℬ S ∩ ℬ T \mathcal{B}_{S}\cap\mathcal{B}_{T}. Hence the total number of bad sets of ℬ \mathcal{B} is at most b 1 + b 2 + b 3 b_{1}+b_{2}+b_{3}, and so by Corollary 4.10 we have

 | 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + b 2 + b 3 + | ℬ S ∩ ℬ T | = b 1 + 2 ​ b 2 + b 3, 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+b_{2}+b_{3}+|\mathcal{B}_{S}\cap\mathcal{B}_{T}|=b_{1}+2b_{2}+b_{3}, |  |

as required. ∎

We note that in fact every set in ℬ S ∩ ℬ T \mathcal{B}_{S}\cap\mathcal{B}_{T} is bad — indeed, any set B B which is ℬ \mathcal{B} -rooted at two distinct integers has δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}. Hence this result gives us a lower bound on the number of bad sets in ℬ \mathcal{B}.

To use Lemma 4.11 to prove Theorem 3.1, we shall pick S S and T T to make | ℬ S | ​ | ℬ T | |\mathcal{B}_{S}||\mathcal{B}_{T}| large. In general, we cannot do well; if, for example, m ≤ 2 n − 1 m\leq 2^{n-1} and ℬ \mathcal{B} is { B + n: B ∈ ℐ ⁡ ( m) } \{B+n:B\in\mathcal{I}(m)\}, then for any partition [n] = S ∪ T [n]=S\cup T one of ℬ S \mathcal{B}_{S} and ℬ T \mathcal{B}_{T} is empty — which is as we expect, because this family has no bad sets. However, if ℬ { i } \mathcal{B}_{\{i\}} — that is, the family of sets of ℬ \mathcal{B} which are ℬ \mathcal{B} -rooted at i i — is not too large for any i i, we can easily choose S S and T T to make | ℬ S | ​ | ℬ T | |\mathcal{B}_{S}||\mathcal{B}_{T}| large.

###### Lemma 4.12.

Let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n) with | ℬ | = m |\mathcal{B}|=m. Suppose that no i ∈ [n] i\in[n] has | ℬ { i } | > p ​ m |\mathcal{B}_{\{i\}}|>pm. Then there exists a partition [n] = S ∪ T [n]=S\cup T such that

 | | ℬ S | ​ | ℬ T | ≥ m 2 ​ ( 1 / 4 − p 2 / 4). |\mathcal{B}_{S}||\mathcal{B}_{T}|\geq m^{2}(1/4-p^{2}/4). |  |

###### Proof.

Take the partition [n] = S ∪ T [n]=S\cup T where the smaller of | ℬ S | |\mathcal{B}_{S}| and | ℬ T | |\mathcal{B}_{T}| is as large as possible — without loss of generality | ℬ S | ≤ | ℬ T | |\mathcal{B}_{S}|\leq|\mathcal{B}_{T}|. If | ℬ S | < m ⁡ ( 1 / 2 − p / 2) |\mathcal{B}_{S}|<m(1/2-p/2), we can move an element t t of T T to S S such that min ⁡ ( ℬ S, ℬ T) \min(\mathcal{B}_{S},\mathcal{B}_{T}) increases, a contradiction. Since | ℬ S | + | ℬ T | ≥ m |\mathcal{B}_{S}|+|\mathcal{B}_{T}|\geq m, | ℬ S | ​ | ℬ T | ≥ ( m / 2 − p / 2) ​ ( m / 2 + p / 2) = m 2 ​ ( 1 / 4 − p 2 / 4) |\mathcal{B}_{S}||\mathcal{B}_{T}|\geq(m/2-p/2)(m/2+p/2)=m^{2}(1/4-p^{2}/4). ∎

We are now ready to prove Theorem 3.1. Let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n) with | ℬ | = m |\mathcal{B}|=m, such that no i ∈ [n] i\in[n] has | ℬ { i } | > p ​ m |\mathcal{B}_{\{i\}}|>pm. By Lemma 4.12, there exists a partition [n] = S ∪ T [n]=S\cup T such that | ℬ S | ​ | ℬ T | ≥ m 2 ​ ( 1 / 4 − p 2 / 4) |\mathcal{B}_{S}||\mathcal{B}_{T}|\geq m^{2}(1/4-p^{2}/4). We let b 1 b_{1} be the number of sets B ∈ ℬ ∖ ( ℬ S ∩ ℬ T) B\in\mathcal{B}\setminus(\mathcal{B}_{S}\cap\mathcal{B}_{T}) with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, b 2 = | ℬ S ∩ ℬ T | b_{2}=|\mathcal{B}_{S}\cap\mathcal{B}_{T}|, and b 3 b_{3} be the number of sets B ∈ ℬ B\in\mathcal{B} with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Then from Lemma 4.11 we have

 | 2 − n ​ m 2 ​ ( 1 / 4 − p 2 / 4) ≤ 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + 2 ​ b 2 + b 3, 2^{-n}m^{2}(1/4-p^{2}/4)\leq 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+2b_{2}+b_{3}, |  |

and so either b 1 + b 2 ≥ m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n b_{1}+b_{2}\geq m^{2}(1/12-p^{2}/12)/2^{n} or b 3 ≥ m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n b_{3}\geq m^{2}(1/12-p^{2}/12)/2^{n}. In the first case, since b 1 + b 2 b_{1}+b_{2} is the number of sets in ℬ \mathcal{B} with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, by Lemma 4.4 we have ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{2}(1/12-p^{2}/12)/2^{n}. In the second case, from Lemma 4.3 we also have ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m 2 ​ ( 1 / 12 − p 2 / 12) / 2 n ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{2}(1/12-p^{2}/12)/2^{n}, as required. ∎

### 4.3 Proof of Theorem 1.3

We now prove Theorem 1.3 from Theorem 3.1, giving us a tighter restriction than Theorem 1.1 on (hypothetical) counterexamples to the union-closed conjecture. Let 𝒜 \mathcal{A} be such a counterexample, with ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A} and | ℬ | = m |\mathcal{B}|=m. Our task is to show that ‖ ℐ ⁡ ( m) ‖ > m ⁡ ( n / 2 − 1 + c 1) ||\mathcal{I}(m)||>m(n/2-1+c_{1}), for some universal constant c 1 c_{1}. If ‖ ℬ { i } ‖ ||\mathcal{B}_{\{i\}}|| is small for all i i, we shall prove this using Theorem 3.1, since if 𝒜 \mathcal{A} is a counterexample to the union-closed conjecture we have m ​ n / 2 ≤ ‖ ℬ { i } ‖ mn/2\leq||\mathcal{B}_{\{i\}}||. To complete the proof of Theorem 1.3, we shall show that if | ℬ { i } | |\mathcal{B}_{\{i\}}| is large for some i i then ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)|| is large. For this, we use the following simple observation.

###### Lemma 4.13.

Let 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) be a counterexample to the union-closed conjecture, let ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A}, and let p ∈ [0, 1 / 2] p\in[0,1/2]. If some element of [n] [n] is in m ⁡ ( 1 / 2 + p) m(1/2+p) sets of ℬ \mathcal{B} then

 | ‖ ℐ ⁡ ( m) ‖ > m ⁡ ( n / 2 − 1 + p). ||\mathcal{I}(m)||>m(n/2-1+p). |  |

###### Proof.

From Equation ( 2), we have ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m ||\mathcal{B}||\leq||\mathcal{I}(m)||+m. Here, since every element of [n] [n] is in more than m / 2 m/2 sets of ℬ \mathcal{B}, we must also have ‖ ℬ ‖ > ( n − 1) ​ m / 2 + m ⁡ ( 1 / 2 + p) ||\mathcal{B}||>(n-1)m/2+m(1/2+p), and the result follows. ∎

Now we can show that if many sets of ℬ \mathcal{B} are ℬ \mathcal{B} -rooted at the same i ∈ [n] i\in[n] then Theorem 1.3 holds. We shall use Lemma 4.13, and also Theorem 19 of [1], which we state in a slightly different form.

###### Theorem 4.14.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family with | ℬ | = m |\mathcal{B}|=m. Suppose the largest down-set contained in ℬ \mathcal{B} is 𝒟 \mathcal{D}. Then ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − | 𝒟 | ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-|\mathcal{D}|.∎

In fact, this theorem is an immediate consequence of Lemma 4.4, since every B ∈ 𝒟 B\in\mathcal{D} has δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}.

###### Lemma 4.15.

Suppose that 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) is a counterexample to the union-closed conjecture, let ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A}, and let p ∈ [0, 1] p\in[0,1]. If | ℬ { i } | ≥ 3 ​ p ​ m |\mathcal{B}_{\{i\}}|\geq 3pm for some i ∈ [n] i\in[n], then

 | ‖ ℐ ⁡ ( m) ‖ > m ⁡ ( n / 2 − 1 + p). ||\mathcal{I}(m)||>m(n/2-1+p). |  |

###### Proof.

We may assume i = n i=n. We define

 | ℬ n + \displaystyle\mathcal{B}^{+}_{n} | = { B ⊆ 𝒫 ⁡ ( n − 1): B + n ∈ ℬ }, \displaystyle=\{B\subseteq\mathcal{P}(n-1):B+n\in\mathcal{B}\}, |  |

 | ℬ n − \displaystyle\mathcal{B}^{-}_{n} | = { B ⊆ 𝒫 ⁡ ( n − 1): B ∈ ℬ }. \displaystyle=\{B\subseteq\mathcal{P}(n-1):B\in\mathcal{B}\}. |  |

Also, define m n, + = | ℬ n + | m_{n,+}=|\mathcal{B}^{+}_{n}|, and m n, − = | ℬ n − | m_{n,-}=|\mathcal{B}^{-}_{n}|. Since 𝒜 \mathcal{A} is a counterexample to the union-closed conjecture, m n, + > m n, − m_{n,+}>m_{n,-}. If m n, + > m ⁡ ( 1 / 2 + p) m_{n,+}>m(1/2+p), we are done by Lemma 4.13, so we may assume that m n, + ≤ m ⁡ ( 1 / 2 + p) m_{n,+}\leq m(1/2+p), and hence m n, + − m n, − ≤ 2 ​ p ​ m m_{n,+}-m_{n,-}\leq 2pm. Then, setting D + D_{+} to be the largest down-set contained in ℬ n + \mathcal{B}_{n}^{+}, we have { B − n: [{ n }, B] ⊆ ℬ } ⊆ 𝒟 + \{B-n:[\{n\},B]\subseteq\mathcal{B}\}\subseteq\mathcal{D}_{+}, and so | 𝒟 + | ≥ 3 ​ p ​ m ≥ m n, + − m n, − + p ​ m |\mathcal{D}_{+}|\geq 3pm\geq m_{n,+}-m_{n,-}+pm. Applying Theorem 4.14 to ℬ n + \mathcal{B}^{+}_{n} now gives us

 | ‖ ℬ ‖ \displaystyle||\mathcal{B}|| | = ‖ ℬ n + ‖ + ‖ ℬ n − ‖ + m n, + \displaystyle=||\mathcal{B}^{+}_{n}||+||\mathcal{B}^{-}_{n}||+m_{n,+} |  |

 |  | ≤ ‖ ℐ ⁡ ( m n, +) ​ ‖ + m n, + − | 𝒟 + | + ‖ ​ ℐ ​ ( m n, −) ‖ + m n, − + m n, + \displaystyle\leq||\mathcal{I}(m_{n,+})||+m_{n,+}-|\mathcal{D}_{+}|+||\mathcal{I}(m_{n,-})||+m_{n,-}+m_{n,+} |  |

 |  | = | | ℐ ⁡ ( m n, +) | ​ | + ‖ ℐ ⁡ ( m n, −) ‖ + m + m n, + − | ​ 𝒟 + | \displaystyle=||\mathcal{I}(m_{n,+})||+||\mathcal{I}(m_{n,-})||+m+m_{n,+}-|\mathcal{D}_{+}| |  |

 |  | ≤ ‖ ℐ ⁡ ( m n, +) ‖ + | | ℐ ⁡ ( m n, −) | | + m + m n, − − p ​ m. \displaystyle\leq||\mathcal{I}(m_{n,+})||+||\mathcal{I}(m_{n,-})||+m+m_{n,-}-pm. |  |

Now, since m n, + > m n, − m_{n,+}>m_{n,-}, by Lemma 2.3 we have ‖ ℐ ⁡ ( m n, +) ‖ + ‖ ℐ ⁡ ( m n, −) ‖ + m n, − ≤ ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m_{n,+})||+||\mathcal{I}(m_{n,-})||+m_{n,-}\leq||\mathcal{I}(m)||, and hence

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − p ​ m. ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-pm. |  |

Since ℬ \mathcal{B} is the complement of a counterexample to the union-closed conjecture, we also have ‖ ℬ ‖ > m ​ n / 2 ||\mathcal{B}||>mn/2, and the result follows. ∎

Putting Theorem 3.1 and Lemma 4.15 together, we can prove Theorem 1.3. Indeed, suppose there is a counterexample 𝒜 \mathcal{A} to the union-closed conjecture in 𝒫 ⁡ ( n) \mathcal{P}(n), and let ℬ \mathcal{B} be 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{P}(n)\setminus\mathcal{A} with | ℬ | = m |\mathcal{B}|=m. Suppose that ‖ ℐ ⁡ ( m) ‖ = m ⁡ ( n / 2 − 1 + p) ||\mathcal{I}(m)||=m(n/2-1+p). Then by Lemma 4.15 we have | ℬ { i } | ≤ 3 ​ p ​ m |\mathcal{B}_{\{i\}}|\leq 3pm for every i ∈ [n] i\in[n]. The family ℬ \mathcal{B} is the complement of a union-closed family, and so is simply rooted, so by Theorem 3.1 we have

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m 2 ​ ( 1 / 12 − 9 ​ p 2 / 12) / 2 n. ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{2}(1/12-9p^{2}/12)/2^{n}. |  |

However, ‖ ℬ ‖ > m ​ n / 2 ||\mathcal{B}||>mn/2, since ℬ \mathcal{B} is the complement of a counterexample to the union-closed conjecture. Hence

 | ‖ ℐ ⁡ ( m) ‖ = m ⁡ ( n / 2 − 1 + p) > m ⁡ ( n / 2 − 1 + m ⁡ ( 1 − 9 ​ p 2) 12 ⋅ 2 n). ||\mathcal{I}(m)||=m(n/2-1+p)>m\left(n/2-1+\frac{m(1-9p^{2})}{12\cdot 2^{n}}\right). |  |

Now, 𝒫 ⁡ ( n) ∖ ℬ \mathcal{P}(n)\setminus\mathcal{B} is a counterexample to the union-closed conjecture, so by Corollary 1.2 we have m ≥ 2 n / 3 m\geq 2^{n}/3, and so

 | p ​ m > m ⁡ ( 1 / 36 − 9 ​ p 2 / 36), pm>m(1/36-9p^{2}/36), |  |

and

 | 36 ​ p + 9 ​ p 2 > 1. 36p+9p^{2}>1. |  |

This is false for all 0 ≤ p ≤ 1 / 37 0\leq p\leq 1/37, and so we have that

 | ‖ ℐ ⁡ ( m) ‖ > m ⁡ ( n / 2 − 1 + 1 / 37), ||\mathcal{I}(m)||>m(n/2-1+1/37), |  |

proving Theorem 1.3 with a bound of c 1 ≥ 1 / 37 c_{1}\geq 1/37. ∎

## 5 Bounding ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)||

In this section we bound ‖ ℐ ⁡ ( m) ‖ ||\mathcal{I}(m)||, enabling us to prove Corollary 1.4. We will use a result of Czédli, Maróti and Schmidt [3], which states that for a positive integer r r we have ‖ ℐ ⁡ ( m) ‖ > m ​ r / 2 ||\mathcal{I}(m)||>mr/2 if and only if m > 2 r + 2 / 3 m>2^{r+2}/3. Here, we shall want a more precise bound for general m m.

###### Lemma 5.1.

Let r r and m m be positive integers with r ≥ 1 r\geq 1 and 2 r / 3 ≤ m ≤ 2 r + 1 / 3 2^{r}/3\leq m\leq 2^{r+1}/3, and write m = 2 r / 3 + m ′ m=2^{r}/3+m^{\prime}. Then

 | ‖ ℐ ⁡ ( m) ‖ ≤ m ⁡ ( r / 2 − 1) + 3 ​ m ′ / 2. ||\mathcal{I}(m)||\leq m(r/2-1)+3m^{\prime}/2. |  |

###### Proof.

We prove this by induction on r r — we deduce the assertion for r r from those for r − 1 r-1 and r − 2 r-2. For r = 1 r=1 or 2 2 the result is easy to check. For r ≥ 3 r\geq 3, first suppose that m ≥ 2 r − 1 m\geq 2^{r-1}. Since m ≤ 2 r + 1 / 3 m\leq 2^{r+1}/3, we have

 | ‖ ℐ ⁡ ( m) ‖ ≤ m ⁡ ( r / 2 − 1 / 2) = m ⁡ ( r / 2 − 1) + m / 2. \displaystyle||\mathcal{I}(m)||\leq m(r/2-1/2)=m(r/2-1)+m/2. |  |

Also, m ′ ≥ m / 3 m^{\prime}\geq m/3, so the result follows. Otherwise, write m = 2 r − 2 + k m=2^{r-2}+k, where 2 r − 2 / 3 ≤ k < 2 r − 2 2^{r-2}/3\leq k<2^{r-2}. If k ≥ 2 r − 1 / 3 k\geq 2^{r-1}/3, we set k = 2 r − 1 / 3 + k ′ k=2^{r-1}/3+k^{\prime} and use the induction hypothesis;

 | ‖ ℐ ⁡ ( m) ‖ \displaystyle||\mathcal{I}(m)|| | = ( r / 2 − 1) ​ 2 r − 2 + k + ‖ ℐ ⁡ ( k) ‖ \displaystyle=(r/2-1)2^{r-2}+k+||\mathcal{I}(k)|| |  |

 |  | ≤ ( r / 2 − 1) ​ 2 r − 2 + k + k ⁡ ( r / 2 − 3 / 2) + 3 ​ k ′ / 2 \displaystyle\leq(r/2-1)2^{r-2}+k+k(r/2-3/2)+3k^{\prime}/2 |  |

 |  | = ( r / 2 − 1) ​ m − k / 2 + 3 ​ ( k − 2 r − 1 / 3) / 2, \displaystyle=(r/2-1)m-k/2+3(k-2^{r-1}/3)/2, |  |

while m ′ = k − 2 r − 2 / 3 m^{\prime}=k-2^{r-2}/3. Hence we need that for all 2 r − 2 / 3 ≤ k < 2 r − 2 2^{r-2}/3\leq k<2^{r-2},

 | 3 / 2 ​ ( k − 2 r − 2 / 3) ≤ k / 2 + 3 ​ ( k − 2 r − 1 / 3) / 2, 3/2(k-2^{r-2}/3)\leq k/2+3(k-2^{r-1}/3)/2, |  |

which does indeed hold. Finally, if k < 2 r − 1 / 3 k<2^{r-1}/3 we have k = 2 r − 2 / 3 + m ′ k=2^{r-2}/3+m^{\prime}, and by the induction hypothesis we have

 | ‖ ℐ ⁡ ( m) ‖ \displaystyle||\mathcal{I}(m)|| | = ( r / 2 − 1) ​ 2 r − 2 + k + ‖ ℐ ⁡ ( k) ‖ \displaystyle=(r/2-1)2^{r-2}+k+||\mathcal{I}(k)|| |  |

 |  | ≤ ( r / 2 − 1) ​ 2 r − 2 + k + k ⁡ ( r / 2 − 2) + 3 ​ m ′ / 2 \displaystyle\leq(r/2-1)2^{r-2}+k+k(r/2-2)+3m^{\prime}/2 |  |

 |  | = ( r / 2 − 1) ​ m + 3 ​ m ′ / 2, \displaystyle=(r/2-1)m+3m^{\prime}/2, |  |

as required. ∎

In fact, we have equality in Lemma 5.1 whenever m m is of the form 2 a + 2 a − 2 + ⋯ + 2 a − 2 ​ j + 2 a − 2 ​ j − 1 2^{a}+2^{a-2}+\dots+2^{a-2j}+2^{a-2j-1} for some integers a a and j j with a > 0 a>0, j ≥ 0 j\geq 0 and a − 2 ​ j − 1 > 0 a-2j-1>0. We can now prove Corollary 1.4. If 𝒜 \mathcal{A} is a counterexample to the union-closed conjecture in 𝒫 ⁡ ( n) \mathcal{P}(n), and ℬ = 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{B}=\mathcal{P}(n)\setminus\mathcal{A} with | ℬ | = m |\mathcal{B}|=m, then write m = 2 n / 3 + m ′ m=2^{n}/3+m^{\prime}. Then from Theorem 1.3 and Lemma 5.1 we have

 | m ⁡ ( n / 2 − 1) + 3 ​ m ′ / 2 \displaystyle m(n/2-1)+3m^{\prime}/2 | ≥ ‖ ℐ ⁡ ( m) ‖ \displaystyle\geq||\mathcal{I}(m)|| |  |

 |  | ≥ m ⁡ ( n / 2 − 1 + 1 / 37), \displaystyle\geq m(n/2-1+1/37), |  |

and so 3 ​ m ′ / 2 ≥ ( 2 n / 3 + m ′) / 37 3m^{\prime}/2\geq(2^{n}/3+m^{\prime})/37, which rearranges to m ′ ≥ 2 327 ​ 2 n m^{\prime}\geq\frac{2}{327}2^{n}, and Corollary 1.4 follows with a bound of c 2 ≥ 2 327 c_{2}\geq\frac{2}{327}.∎

## 6 Improving the constants

In this section, we give a modification to the arguments in Section 4 which improves the constants in our main theorems. To do this, we give stronger versions of Lemmas 4.9 and 4.11. For a triple of simply rooted families ℬ \mathcal{B}, ℬ 1 \mathcal{B}_{1}, ℬ 2 \mathcal{B}_{2} with ℬ = ℬ 1 ∪ ℬ 2 \mathcal{B}=\mathcal{B}_{1}\cup\mathcal{B}_{2},

 | Z ( ℬ, ℬ 1, ℬ 2) = { B ∈ ℬ 1 ∩ ℬ 2: d ℬ ( B), d ℬ 1 ( B) and d ℬ 2 ( B) are all distinct }. Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2})=\{B\in\mathcal{B}_{1}\cap\mathcal{B}_{2}:d_{\mathcal{B}}(B),\,d_{\mathcal{B}_{1}}(B)\textrm{ and }d_{\mathcal{B}_{2}}(B)\textrm{ are all distinct}\}. |  |

The definition of Z ⁡ ( ℬ, ℬ 1, ℬ 2) Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2}) is motivated by the proof of Lemma 4.9. The sets in Z ⁡ ( ℬ, ℬ 1, ℬ 2) Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2}) are those sets B B for which d ℬ 1 ​ ( B) d_{\mathcal{B}_{1}}(B) and d ℬ 2 ​ ( B) d_{\mathcal{B}_{2}}(B) may be distinct sets of d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2}), so if we can bound | Z ⁡ ( ℬ, ℬ 1, ℬ 2) | |Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2})| we can improve our bound on | d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) | |d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2})|.

###### Lemma 6.1.

Let ℬ \mathcal{B}, ℬ 1 \mathcal{B}_{1} and ℬ 2 \mathcal{B}_{2} be simply rooted families, with ℬ 1 ∪ ℬ 2 = ℬ \mathcal{B}_{1}\cup\mathcal{B}_{2}=\mathcal{B}. Let b b be the number of bad sets of ℬ \mathcal{B}. If every set B ∈ ℬ 1 ∩ ℬ 2 B\in\mathcal{B}_{1}\cap\mathcal{B}_{2} has δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, then

 | | d ⁡ ( ℬ 1) ∩ d ⁡ ( ℬ 2) | ≤ b + | Z ⁡ ( ℬ, ℬ 1, ℬ 2) |. |d(\mathcal{B}_{1})\cap d(\mathcal{B}_{2})|\leq b+|Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2})|. |  |

###### Proof.

The proof is similar to that of Lemma 4.9. Letting 𝒟 i = d ⁡ ( ℬ i) \mathcal{D}_{i}=d(\mathcal{B}_{i}), consider an element S S of 𝒟 1 ∩ 𝒟 2 \mathcal{D}_{1}\cap\mathcal{D}_{2}. Then S = d ℬ 1 ​ ( B 1) = d ℬ 2 ​ ( B 2) S=d_{\mathcal{B}_{1}}(B_{1})=d_{\mathcal{B}_{2}}(B_{2}) for some B 1 ∈ ℬ 1 B_{1}\in\mathcal{B}_{1} and B 2 ∈ ℬ 2 B_{2}\in\mathcal{B}_{2}. We now define a function f: 𝒟 1 ∩ 𝒟 2 → ℬ f:\mathcal{D}_{1}\cap\mathcal{D}_{2}\to\mathcal{B}. If B 1 = B 2 B_{1}=B_{2}, then we set f ⁡ ( S) = B 1 f(S)=B_{1} — note that since B 1 ∈ ℬ 1 ∩ ℬ 2 B_{1}\in\mathcal{B}_{1}\cap\mathcal{B}_{2}, δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B} and so B 1 B_{1} is a bad set of ℬ \mathcal{B}. Otherwise, since d ℬ d_{\mathcal{B}} is injective, for i = 1 i=1 or 2 2 we have d ℬ i ​ ( B i) ≠ d ℬ ​ ( B i) d_{\mathcal{B}_{i}}(B_{i})\neq d_{\mathcal{B}}(B_{i}). In this case, we define f ⁡ ( S) = B i f(S)=B_{i} — note that since d ℬ i ​ ( B i) ≠ d ℬ ​ ( B i) d_{\mathcal{B}_{i}}(B_{i})\neq d_{\mathcal{B}}(B_{i}), by Lemma 4.8 the set B i B_{i} is a bad set of ℬ \mathcal{B}. So f ⁡ ( S) f(S) is a bad set of ℬ \mathcal{B} for all S ∈ 𝒟 1 ∩ 𝒟 2 S\in\mathcal{D}_{1}\cap\mathcal{D}_{2}. Also, for S ≠ T ∈ 𝒟 1 ∩ 𝒟 2 S\neq T\in\mathcal{D}_{1}\cap\mathcal{D}_{2}, if f ⁡ ( S) = f ⁡ ( T) = B f(S)=f(T)=B then

 | S = d ℬ i ​ ( B) ≠ d ℬ ​ ( B) ≠ d ℬ j ​ ( B) = T, S=d_{\mathcal{B}_{i}}(B)\neq d_{\mathcal{B}}(B)\neq d_{\mathcal{B}_{j}}(B)=T, |  |

where { i, j } = { 1, 2 } \{i,j\}=\{1,2\}. In particular B ∈ Z ⁡ ( ℬ, ℬ 1, ℬ 2) B\in Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2}), and there is no U ∈ 𝒟 1 ∩ 𝒟 2 U\in\mathcal{D}_{1}\cap\mathcal{D}_{2} with S ≠ U ≠ T S\neq U\neq T and f ⁡ ( U) = B f(U)=B. Hence the size of the image of f f is at least | 𝒟 1 ∩ 𝒟 2 | − | Z ⁡ ( ℬ, ℬ 1, ℬ 2) | |\mathcal{D}_{1}\cap\mathcal{D}_{2}|-|Z(\mathcal{B},\mathcal{B}_{1},\mathcal{B}_{2})|, and since every set in the image is a bad set of ℬ \mathcal{B} the result follows. ∎

We can now prove a stronger form of Lemma 4.11, using Lemma 6.1 and making sure we do not overcount the bad sets of ℬ \mathcal{B}. For a family of sets ℬ \mathcal{B} we define

 | Y ⁡ ( ℬ) = { B ∈ ℬ: δ ​ B ⊆ ℬ ​ and ​ d ℬ ​ ( B) = B }. Y(\mathcal{B})=\{B\in\mathcal{B}:\delta B\subseteq\mathcal{B}\textrm{ and }d_{\mathcal{B}}(B)=B\}. |  |

The sets in Y ⁡ ( ℬ) Y(\mathcal{B}) are those that satisfy both criteria for a set to be bad; we have often overcounted the number of bad sets of ℬ \mathcal{B} by | Y ⁡ ( ℬ) | |Y(\mathcal{B})|.

###### Lemma 6.2.

Let ( S, T) (S,T) be a partition of [n] [n] into two disjoint sets, and ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n). Let b 1 b_{1} be the number of sets B ∈ ℬ ∖ ( ℬ S ∩ ℬ T) B\in\mathcal{B}\setminus(\mathcal{B}_{S}\cap\mathcal{B}_{T}) with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, b 2 = | ℬ S ∩ ℬ T | b_{2}=|\mathcal{B}_{S}\cap\mathcal{B}_{T}|, and b 3 b_{3} be the number of sets B ∈ ℬ B\in\mathcal{B} with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Then

 | 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + b 2 + b 3 + | Z ⁡ ( ℬ, ℬ S, ℬ T) | − | Y ⁡ ( ℬ) |. 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+b_{2}+b_{3}+|Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T})|-|Y(\mathcal{B})|. |  |

###### Proof.

The proof is identical to that of Lemma 4.11 — letting b b be the number of bad sets of ℬ \mathcal{B}, by Harris’s Lemma and Lemma 6.1 we have

 | 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b + | Z ⁡ ( ℬ, ℬ S, ℬ T) |, 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b+|Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T})|, |  |

and b = b 1 + b 2 + b 3 − | Y ⁡ ( ℬ) | b=b_{1}+b_{2}+b_{3}-|Y(\mathcal{B})|. ∎

We shall show that in fact | Y ⁡ ( ℬ) | ≥ | Z ⁡ ( ℬ, ℬ S, ℬ T) | |Y(\mathcal{B})|\geq|Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T})|, improving our bound on the number of bad sets of ℬ \mathcal{B}. For this, we shall use the key lemma of Reimer [8] on up-compressions of union-closed families. For a family 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n), a set A ∈ 𝒜 A\in\mathcal{A} and an element i ∈ [n] i\in[n], we define

 | u ( i, 𝒜) ( A) = { A + i: i ∉ A, A + i ∉ 𝒜 A: otherwise. u_{(i,\mathcal{A})}(A)=\begin{cases}A+i:i\notin A,\,A+i\notin\mathcal{A}\\ A:\mathrm{otherwise.}\end{cases} |  |

Then u ⁡ ( 𝒜) u(\mathcal{A}), u 𝒜 ​ ( A) u_{\mathcal{A}}(A), u i ​ ( 𝒜) u_{i}(\mathcal{A}), U i ​ ( 𝒜) U_{i}(\mathcal{A}) and U ( 𝒜, i) ​ ( A) U_{(\mathcal{A},i)}(A) are defined analagously to in the case of down-compressions. In particular, u ⁡ ( 𝒜) = u 1 ​ … ​ u n ​ ( 𝒜) u(\mathcal{A})=u_{1}\dots u_{n}(\mathcal{A}), and u 𝒜 ​ ( A) u_{\mathcal{A}}(A) is the image of the set A A in u ⁡ ( 𝒜) u(\mathcal{A}) under the sequence of up-compressions u 1 ​ … ​ u n u_{1}\dots u_{n}.

###### Lemma 6.3.

If 𝒜 \mathcal{A} is a union-closed family, and A 1 ≠ A 2 A_{1}\neq A_{2} are sets in 𝒜 \mathcal{A}, the cubes [A 1, u 𝒜 ​ ( A 1)] [A_{1},u_{\mathcal{A}}(A_{1})] and [A 2, u 𝒜 ​ ( A 2)] [A_{2},u_{\mathcal{A}}(A_{2})] are disjoint.∎

We make a simple observation about the relationship between sets of a simply rooted family which lose an element under the down-compression d ℬ d_{\mathcal{B}}, and the sets of the union-closed family 𝒫 ⁡ ( n) ∖ ℬ \mathcal{P}(n)\setminus\mathcal{B}.

###### Lemma 6.4.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family, let 𝒜 = 𝒫 ⁡ ( n) ∖ ℬ \mathcal{A}=\mathcal{P}(n)\setminus\mathcal{B}, and let B ∈ ℬ B\in\mathcal{B}. If d ℬ ​ ( B) ≠ B d_{\mathcal{B}}(B)\neq B then for some 1 ≤ k ≤ n 1\leq k\leq n and some A ∈ 𝒜 A\in\mathcal{A} we have U ( 𝒜, k) ​ ( A) = B U_{(\mathcal{A},k)}(A)=B.

###### Proof.

Let k k be minimal with D ( ℬ, k) ​ ( B) ≠ B D_{(\mathcal{B},k)}(B)\neq B. Then D ( ℬ, k) ​ ( B) = B − k D_{(\mathcal{B},k)}(B)=B-k, and B − k ∉ D k − 1 ​ ( B) B-k\notin D_{k-1}(B). Hence B − k ∈ 𝒫 ⁡ ( n) ∖ D k − 1 ​ ( B) = U k − 1 ​ ( 𝒜) B-k\in\mathcal{P}(n)\setminus D_{k-1}(B)=U_{k-1}(\mathcal{A}), and so B − k = U ( 𝒜, k − 1) ​ ( A) B-k=U_{(\mathcal{A},k-1)}(A) for some A ∈ 𝒜 A\in\mathcal{A}, and B = U ( 𝒜, k) ​ ( A) B=U_{(\mathcal{A},k)}(A). ∎

For a simply rooted family ℬ \mathcal{B}, and a set B ∈ ℬ B\in\mathcal{B}, let R ℬ ​ ( B) = { r ∈ [n]: [{ r }, B] ⊆ ℬ } R_{\mathcal{B}}(B)=\{r\in[n]:[\{r\},B]\subseteq\mathcal{B}\} be the set of roots of B B in ℬ \mathcal{B}. We now prove that if B B is in some cube [A, U 𝒜 ​ ( A)] [A,U_{\mathcal{A}}(A)], we must have A = B ∖ R ℬ ​ ( B) A=B\setminus R_{\mathcal{B}}(B).

###### Lemma 6.5.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family, and let B ∈ ℬ B\in\mathcal{B}. Let 𝒜 = 𝒫 ⁡ ( n) ∖ ℬ \mathcal{A}=\mathcal{P}(n)\setminus\mathcal{B}. If B B is in the cube [A, U 𝒜 ​ ( A)] [A,U_{\mathcal{A}}(A)] for some A ∈ 𝒜 A\in\mathcal{A}, then A = B ∖ R ℬ ​ ( B) A=B\setminus R_{\mathcal{B}}(B).

###### Proof.

Let R = R ℬ ​ ( B) R=R_{\mathcal{B}}(B). First we observe that B ∖ R ∈ 𝒜 B\setminus R\in\mathcal{A}. Indeed, suppose B ∖ R ∈ ℬ B\setminus R\in\mathcal{B}; then it is ℬ \mathcal{B} -rooted at some b ∈ B ∖ R b\in B\setminus R. But then we have { B ′ ⊆ B: B ′ ∩ R ≠ ∅ } ⊆ ℬ \{B^{\prime}\subseteq B:B^{\prime}\cap R\neq\emptyset\}\subseteq\mathcal{B}, and { B ′ ⊆ B ∖ R: b ∈ B ′ } ⊆ ℬ \{B^{\prime}\subseteq B\setminus R:b\in B^{\prime}\}\subseteq\mathcal{B}. Hence B B is ℬ \mathcal{B} -rooted at b b, and so b ∈ R b\in R, a contradiction as b ∈ B ∖ R b\in B\setminus R.

Now, since B ∈ [A, U 𝒜 ​ ( A)] B\in[A,U_{\mathcal{A}}(A)], we have A ⊆ B A\subseteq B. However, { B ′ ⊆ B: B ′ ∩ R ≠ ∅ } \{B^{\prime}\subseteq B:B^{\prime}\cap R\neq\emptyset\} is contained in the family ℬ \mathcal{B}, and hence we have A ⊆ B ∖ R A\subseteq B\setminus R. In particular, B ∖ R ∈ [A, B] ⊆ [A, U 𝒜 ​ ( A)] B\setminus R\in[A,B]\subseteq[A,U_{\mathcal{A}}(A)]. Hence the cubes [A, U 𝒜 ​ ( A)] [A,U_{\mathcal{A}}(A)] and [B ∖ R, U 𝒜 ​ ( B ∖ R)] [B\setminus R,U_{\mathcal{A}}(B\setminus R)] intersect, and so from Theorem 6.3 we have A = B ∖ R A=B\setminus R. ∎

Using the last two lemmas, it is immediate that if a set B ∈ ℬ B\in\mathcal{B} loses an element r r under the down-compression d ℬ d_{\mathcal{B}}, then B B is ℬ \mathcal{B} -rooted at r r.

###### Lemma 6.6.

Let ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) be a simply rooted family, and let B ∈ ℬ B\in\mathcal{B}. Then d ℬ ​ ( B) ∈ { B } ∪ { B − r: r ∈ R ℬ ​ ( B) } d_{\mathcal{B}}(B)\in\{B\}\cup\{B-r:r\in R_{\mathcal{B}}(B)\}.

###### Proof.

Let 𝒜 = 𝒫 ⁡ ( n) ∖ ℬ \mathcal{A}=\mathcal{P}(n)\setminus\mathcal{B}. Suppose d ℬ ​ ( B) ≠ B d_{\mathcal{B}}(B)\neq B — then by Lemma 4.2, d ℬ ​ ( B) = B − b d_{\mathcal{B}}(B)=B-b for some b ∈ B b\in B. Also, by Lemma 6.4 we have that for some k k and some A ∈ 𝒜 A\in\mathcal{A} we have U ( 𝒜, k) ​ ( A) = B U_{(\mathcal{A},k)}(A)=B. In particular, B ∈ [A, u 𝒜 ​ ( A)] B\in[A,u_{\mathcal{A}}(A)], and so A = B ∖ R ℬ ​ ( B) A=B\setminus R_{\mathcal{B}}(B). Since d ℬ ​ ( B) ∈ [A, B] d_{\mathcal{B}}(B)\in[A,B], we then have b ∈ B ∖ A = R ℬ ​ ( B) b\in B\setminus A=R_{\mathcal{B}}(B), as required. ∎

In the special case where B − b ∉ ℬ B-b\notin\mathcal{B} for some b ∈ B b\in B, we must have R ℬ ​ ( B) = { b } R_{\mathcal{B}}(B)=\{b\}, and so Lemma 4.6 is a special case of Lemma 6.6. We read out the following corollary on the number of roots of sets in Z ⁡ ( ℬ, ℬ S, ℬ T) Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T}).

###### Corollary 6.7.

Let ℬ \mathcal{B} be a simply rooted family, S ∪ T S\cup T a partition of [n] [n], and B ∈ Z ⁡ ( ℬ, ℬ S, ℬ T) B\in Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T}). Then | R ℬ ​ ( B) | ≥ 2 |R_{\mathcal{B}}(B)|\geq 2. If d ℬ ​ ( B) ≠ B d_{\mathcal{B}}(B)\neq B, then | R ℬ ​ ( B) | ≥ 3 |R_{\mathcal{B}}(B)|\geq 3.

###### Proof.

By Lemma 6.6 the sets d ℬ S ​ ( B) d_{\mathcal{B}_{S}}(B), d ℬ T ​ ( B) d_{\mathcal{B}_{T}}(B) and d ℬ ​ ( B) d_{\mathcal{B}}(B) are all elements of { B } ∪ { B − r: r ∈ R ℬ ​ ( B) } \{B\}\cup\{B-r:r\in R_{\mathcal{B}}(B)\}. But B ∈ Z ⁡ ( ℬ, ℬ S, ℬ T) B\in Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T}), so these sets are all distinct, and in particular, | R ℬ ​ ( B) | ≥ 2 |R_{\mathcal{B}}(B)|\geq 2. If d ℬ ​ ( B) ≠ B d_{\mathcal{B}}(B)\neq B, then by Lemma 4.7 we also have d ℬ 1 ​ ( B) ≠ B ≠ d ℬ 2 ​ ( B) d_{\mathcal{B}_{1}}(B)\neq B\neq d_{\mathcal{B}_{2}}(B), so the sets d ℬ 1 ​ ( B) d_{\mathcal{B}_{1}}(B), d ℬ 2 ​ ( B) d_{\mathcal{B}_{2}}(B) and d ℬ ​ ( B) d_{\mathcal{B}}(B) are distinct elements of { B − r: r ∈ R ℬ ​ ( B) } \{B-r:r\in R_{\mathcal{B}}(B)\} and | R ℬ ​ ( B) | ≥ 3 |R_{\mathcal{B}}(B)|\geq 3.∎

Now we shall prove that | Y ⁡ ( ℬ) | ≥ | Z ⁡ ( ℬ, ℬ S, ℬ T) | |Y(\mathcal{B})|\geq|Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T})|. For a finite set B B we define the *2 2 nd shadow of B B*to be δ 2 ​ B = { B ′ ⊆ B: | B ′ | = | B | − 2 } \delta_{2}B=\{B^{\prime}\subseteq B:|B^{\prime}|=|B|-2\}.

###### Lemma 6.8.

Let ℬ \mathcal{B} be a simply rooted family, and S ∪ T S\cup T a partition of [n] [n]. Then | Y ⁡ ( ℬ) | ≥ | Z ⁡ ( ℬ, ℬ S, ℬ T) | |Y(\mathcal{B})|\geq|Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T})|.

###### Proof.

We write Z = Z ⁡ ( ℬ, ℬ S, ℬ T) Z=Z(\mathcal{B},\mathcal{B}_{S},\mathcal{B}_{T}), and Y = Y ⁡ ( ℬ) Y=Y(\mathcal{B}). Let 𝒜 \mathcal{A} be 𝒫 ⁡ ( n) ∖ ℬ \mathcal{P}(n)\setminus\mathcal{B}; 𝒜 \mathcal{A} is a union-closed family, since ℬ \mathcal{B} is simply rooted. If a set B ∈ Z B\in Z is not in a cube [A, u 𝒜 ​ ( A)] [A,u_{\mathcal{A}}(A)] for some A ∈ 𝒜 A\in\mathcal{A}, then B B is also in Y Y. Indeed, δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B} because all sets in Z Z are ℬ \mathcal{B} -rooted at two distinct elements of [n] [n]. d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B follows from Lemma 6.4; otherwise we must have B = U ( 𝒜, k) ​ ( A) B=U_{(\mathcal{A},k)}(A) for some A ∈ 𝒜 A\in\mathcal{A} and 1 ≤ k ≤ n 1\leq k\leq n, so B ∈ [A, u 𝒜 ​ ( A)] B\in[A,u_{\mathcal{A}}(A)], a contradiction. Hence it is enough to show that for every cube C = [A, u 𝒜 ​ ( A)] C=[A,u_{\mathcal{A}}(A)],

 | | C ∩ Y | ≥ | C ∩ Z |, |C\cap Y|\geq|C\cap Z|, |  |

since by Theorem 6.3 these cubes are disjoint for different A A. We shall now show this for the cube C C. If C ∩ Z ⊆ C ∩ Y C\cap Z\subseteq C\cap Y, we are done. Otherwise, let B ∈ ( C ∩ Z) ∖ Y B\in(C\cap Z)\setminus Y. Since B ∈ Z B\in Z, B B has at least two roots in ℬ \mathcal{B} by Corollary 6.7, so δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}. Then since B ∉ Y B\notin Y, d ℬ ​ ( B) ≠ B d_{\mathcal{B}}(B)\neq B, and B B has at least 3 3 roots in ℬ \mathcal{B} by Corollary 6.7. Hence δ 2 ​ ( B) ⊆ ℬ \delta_{2}(B)\subseteq\mathcal{B}, and so | u 𝒜 ​ ( A) ∖ A | ≥ | B ∖ A | ≥ 3 |u_{\mathcal{A}}(A)\setminus A|\geq|B\setminus A|\geq 3. We define r = | u 𝒜 ​ ( A) ∖ A | r=|u_{\mathcal{A}}(A)\setminus A|.

We now count the sets of C ∖ Y C\setminus Y. Note that by Lemma 6.3, C C contains no set of 𝒜 \mathcal{A} other than A A. In C C, there are r + 1 r+1 sets which are U ( 𝒜, k) ​ ( A) U_{(\mathcal{A},k)}(A) for some 0 ≤ k ≤ n 0\leq k\leq n, one of size i i for each i i with | A | ≤ i ≤ | u 𝒜 ​ ( A) | |A|\leq i\leq|u_{\mathcal{A}}(A)|. All other sets B ∈ C B\in C are in ℬ \mathcal{B}, and have d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Also, every set B B in C C of size at least | A | + 2 |A|+2 has δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}. Indeed, if i ∈ B ∩ A i\in B\cap A, B − i ∈ C ∖ { A } ⊆ ℬ B-i\in C\setminus\{A\}\subseteq\mathcal{B}. If i ∈ B ∖ A i\in B\setminus A, then ( B − i) ∪ A = B (B-i)\cup A=B, and 𝒜 \mathcal{A} is union-closed, so B − i ∈ ℬ B-i\in\mathcal{B}.

Hence | C ∩ Y | = 2 r − 2 ​ r |C\cap Y|=2^{r}-2r — the elements of C ∖ Y C\setminus Y are precisely the r + 1 r+1 sets of C C of size | A | |A| or | A | + 1 |A|+1, together with one set of size i i for each i i with | A | + 2 ≤ i ≤ | A | + r |A|+2\leq i\leq|A|+r. To bound | C ∩ Z | |C\cap Z|, we note that A A is not in Z Z, and nor is A + i A+i for any i ∈ ( u 𝒜 ​ ( A) ∖ A) i\in(u_{\mathcal{A}}(A)\setminus A), since A + i A+i has only one ℬ \mathcal{B} -root. Also, if A + i + j A+i+j is in Z Z, for i ≠ j i\neq j both in u 𝒜 ​ ( A) ∖ A u_{\mathcal{A}}(A)\setminus A, then since A + i + j A+i+j is not ℬ \mathcal{B} -rooted at any element in A A by Corollary 6.7 we must have { d ℬ ​ ( A + i + j), d ℬ S ​ ( A + i + j), d ℬ T ​ ( A + i + j) } = { A + i + j, A + i, A + j } \{d_{\mathcal{B}}(A+i+j),d_{\mathcal{B}_{S}}(A+i+j),d_{\mathcal{B}_{T}}(A+i+j)\}=\{A+i+j,A+i,A+j\}.

However, we must have d ℬ ​ ( A + i + j) = A + i + j d_{\mathcal{B}}(A+i+j)=A+i+j; otherwise by Lemma 4.7 d ℬ S ​ ( A + i + j) ≠ A + i + j ≠ d ℬ T ​ ( A + i + j) d_{\mathcal{B}_{S}}(A+i+j)\neq A+i+j\neq d_{\mathcal{B}_{T}}(A+i+j), a contradiction. So { d ℬ S ​ ( A + i + j), d ℬ T ​ ( A + i + j) } = { A + i, A + j } \{d_{\mathcal{B}_{S}}(A+i+j),d_{\mathcal{B}_{T}}(A+i+j)\}=\{A+i,A+j\}. Without loss of generality, d ℬ S ​ ( A + i + j) = A + i d_{\mathcal{B}_{S}}(A+i+j)=A+i. Then by Lemma 6.6 we have j ∈ R ℬ S ​ ( A + i + j) j\in R_{\mathcal{B}_{S}}(A+i+j), and so j ∈ S j\in S. Similarly, i ∈ T i\in T.

Now, suppose A + i + k ∈ Z A+i+k\in Z for some k ≠ j k\neq j. Then, as before, { d ℬ S ​ ( A + i + k), d ℬ T ​ ( A + i + k) } = { A + i, A + k } \{d_{\mathcal{B}_{S}}(A+i+k),d_{\mathcal{B}_{T}}(A+i+k)\}=\{A+i,A+k\}, and since i ∈ T i\in T we must have k ∈ S k\in S and d ℬ S ​ ( A + i + k) = A + i d_{\mathcal{B}_{S}}(A+i+k)=A+i, contradicting the injectivity of d ℬ S d_{\mathcal{B}_{S}}. Hence each element of u 𝒜 ​ ( A) ∖ A u_{\mathcal{A}}(A)\setminus A appears in at most one of size | A | + 2 |A|+2 in C ∩ Z C\cap Z. So C ∩ Z C\cap Z does not contain A A, nor any of the r r sets of size | A | + 1 |A|+1 in C C, and contains at most ⌊ r / 2 ⌋ \lfloor r/2\rfloor of the ( r 2) \binom{r}{2} sets of size | A | + 2 |A|+2 in C C. So the total number of sets in C ∩ Z C\cap Z is at most 2 r − 1 − r − ( r 2) + ⌊ r / 2 ⌋ 2^{r}-1-r-\binom{r}{2}+\lfloor r/2\rfloor. It is easy to see that for r ≥ 3 r\geq 3 this is at most 2 r − 2 ​ r 2^{r}-2r, with equality when r = 3 r=3. Hence | Y | ≥ | Z | |Y|\geq|Z|, as required.∎

Combining Lemmas 6.2 and 6.8, we get the following lemma.

###### Lemma 6.9.

Let ( S, T) (S,T) be a partition of [n] [n] into two disjoint sets. Also, let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n). Let b 1 b_{1} be the number of sets B ∈ ℬ ∖ ( ℬ S ∩ ℬ T) B\in\mathcal{B}\setminus(\mathcal{B}_{S}\cap\mathcal{B}_{T}) with δ ​ B ⊆ ℬ \delta B\subseteq\mathcal{B}, let b 2 = | ℬ S ∩ ℬ T | b_{2}=|\mathcal{B}_{S}\cap\mathcal{B}_{T}|, and let b 3 b_{3} be the number of sets B ∈ ℬ B\in\mathcal{B} with d ℬ ​ ( B) = B d_{\mathcal{B}}(B)=B. Then

 | 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + b 2 + b 3. 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+b_{2}+b_{3}. |  |

∎

This result is a stronger version Lemma 4.11, and using it instead of that lemma improves the constant in Theorem 3.1, giving the following result.

###### Theorem 6.10.

Let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n) with | ℬ | = m |\mathcal{B}|=m, and let p ∈ [0, 1] p\in[0,1]. Suppose that no i ∈ [n] i\in[n] has | ℬ { i } | ≥ p ​ m |\mathcal{B}_{\{i\}}|\geq pm. Then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m − m 2 ​ ( 1 / 8 − p 2 / 8) / 2 n. ||\mathcal{B}||\leq||\mathcal{I}(m)||+m-m^{2}(1/8-p^{2}/8)/2^{n}. |  |

###### Proof.

Indeed, by Lemma 4.12 we can choose a partition [n] = S ∪ T [n]=S\cup T so that | ℬ S | ​ | ℬ T | ≥ m 2 ​ ( 1 / 2 − p 2 / 4) |\mathcal{B}_{S}||\mathcal{B}_{T}|\geq m^{2}(1/2-p^{2}/4). Then we have

 | 2 − n ​ m 2 ​ ( 1 / 2 − p 2 / 4) ≤ 2 − n ​ | ℬ S | ​ | ℬ T | ≤ b 1 + b 2 + b 3, 2^{-n}m^{2}(1/2-p^{2}/4)\leq 2^{-n}|\mathcal{B}_{S}||\mathcal{B}_{T}|\leq b_{1}+b_{2}+b_{3}, |  |

and so either b 1 + b 2 b_{1}+b_{2} or b 3 b_{3} is at least m 2 ​ ( 1 / 8 − p 2 / 8) / 2 n m^{2}(1/8-p^{2}/8)/2^{n}. Applying Lemma 4.4 in the first case or Lemma 4.3 in the second, we get Theorem 6.10.∎

This in turn improves the constants in Theorem 1.3 and Corollary 1.4. We also note another minor change to the proof of Theorem 1.3 — at the end of the proof, we use the fact that a counterexample to the union-closed conjecture in 𝒫 ⁡ ( n) \mathcal{P}(n) has fewer than 2 3 ​ 2 n \frac{2}{3}2^{n} elements. Since we now have a better bound, we can use this instead to improve the argument slightly. Applying these improvements together improves our bound in Theorem 1.3 to c 1 ≥ 0.04218 ​ … > 1 / 24 c_{1}\geq 0.04218\ldots>1/24 and in Corollary 1.4 to c 2 ≥ 0.009646 ​ … > 1 / 104 c_{2}\geq 0.009646\ldots>1/104 — that is, the union-closed conjecture holds for families in 𝒫 ⁡ ( n) \mathcal{P}(n) with at least ( 2 3 − 1 104) ​ 2 n (\frac{2}{3}-\frac{1}{104})2^{n} elements.

## 7 Further Work

Theorem 6.10 is a stability result for the total sizes of simply rooted families, which in turn provides a stability result for the union-closed size problem in the case of large union-closed families; if 𝒜 ⊆ 𝒫 ⁡ ( n) \mathcal{A}\subseteq\mathcal{P}(n) is union-closed, with | 𝒜 | ≥ 2 n − 1 |\mathcal{A}|\geq 2^{n-1} and ‖ 𝒜 ‖ ||\mathcal{A}|| is close to the minimum possible, then 𝒫 ⁡ ( n) ∖ 𝒜 \mathcal{P}(n)\setminus\mathcal{A} has an element of high degree. However, we have no stability result for the union-closed size problem in general. It was proved in [1] that there is a unique uinon-closed family ℱ m \mathcal{F}_{m} with | ℱ m | = m |\mathcal{F}_{m}|=m and ‖ ℱ m ‖ = f ⁡ ( m) ||\mathcal{F}_{m}||=f(m), but if 𝒜 \mathcal{A} is a union-closed family of m m sets with ‖ 𝒜 ‖ ||\mathcal{A}|| close to ‖ ℱ m ‖ ||\mathcal{F}_{m}|| in a large powerset, we have no result (or even conjecture) which states that 𝒜 \mathcal{A} is in some sense similar to ℱ m \mathcal{F}_{m}.

Another direction would be to improve our stability results for the sizes of simply rooted families. For example, it was conjectured in [1] that if ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) is a simply rooted family then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + max i ∈ [n] ⁡ deg ℬ ​ ( i). ||\mathcal{B}||\leq||\mathcal{I}(m)||+\max_{i\in[n]}\mathrm{deg}_{\mathcal{B}}(i). |  | (3) |

This remains open, but we conjecture a stronger result still; that we can replace the maximum of the degrees d ℬ ​ ( i) d_{\mathcal{B}}(i) with the largest number of elements of ℬ \mathcal{B} rooted at a single element of [n] [n]:

###### Conjecture 1.

Let ℬ \mathcal{B} be a simply rooted family in 𝒫 ⁡ ( n) \mathcal{P}(n) then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + max i ∈ [n] ⁡ | ℬ { i } |. ||\mathcal{B}||\leq||\mathcal{I}(m)||+\max_{i\in[n]}|\mathcal{B}_{\{i\}}|. |  |

Even if these conjectures do not hold, it seems likely that some version of Theorem 3.1 which does not depend on n n is true. To be precise, we conjecture that there are some positive constants ϵ \epsilon and δ \delta such that if ℬ ⊆ 𝒫 ⁡ ( n) \mathcal{B}\subseteq\mathcal{P}(n) is a simply rooted family of m m sets, and | ℬ { i } | ≤ ϵ ​ m |\mathcal{B}_{\{i\}}|\leq\epsilon m for all i ∈ [n] i\in[n], then

 | ‖ ℬ ‖ ≤ ‖ ℐ ⁡ ( m) ‖ + m ⁡ ( 1 − δ). ||\mathcal{B}||\leq||\mathcal{I}(m)||+m(1-\delta). |  |

## 8 Acknowledgements

The author would like to thank Béla Bollobás for his helpful comments on earlier versions of this paper.

## References

- [1] I. Balla, B. Bollobás, T. Eccles, On union-closed families of sets, J. Combin. Theory Ser. A, to appear.
- [2] B. Bollobás, I. Leader, Compressions and isoperimetric inequalities, J. Combin. Theory Ser. A 56 (1991), 47–62.
- [3] G. Czédli, M. Maróti and E.T. Schmidt, On the scope of averaging for Frankl’s conjecture, Order 26 (2009), 31–48.
- [4] D. Duffus, in Graphs and Order (I. Rival, Ed.), Dordrecht/Boston, Reidel (1985), p.525.
- [5] T.E. Harris, A lower bound for the critical probability in a certain percolation process, Math. Proc. Cambridge Philos. Soc. 26 (1960), 13-�20.
- [6] G.O.H. Katona, A theorem on finite sets, in Theory of Graphs (P. Erdős and G.O.H. Katona, Eds.), Akadémiai Kiadó, Budapest, 1968, 187–207.
- [7] J.B. Kruskal, The number of simplices in a complex, in Mathematical Optimization Techniques, Univ. of California Press, Berkeley, 1963, 251–278.
- [8] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003), 89–93.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1311.2297
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1311.2298
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1311.2298
[7]: https://arxiv.org/pdf/1311.2298
[8]: /html/1311.2299
