<!-- source: https://arxiv.org/html/2401.17502v2 | converted from HTML -->

The Period of Ducci Cycles on Z 2 l for Tuples of Length 2 k

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2401.17502v2 [math.NT] 29 Aug 2024

# The Period of Ducci Cycles on ℤ 2 l \mathbb{Z}_{2^{l}} for Tuples of Length 2 k 2^{k}

Mark L. Lewis Address: Department of Mathematical Sciences
Kent State University
Kent, OH 44242 Email address: [lewis@math.kent.edu][3] and Shannon M. Tefft Address: Department of Mathematical Sciences
Kent State University
Kent, OH 44242 Email address: [stefft@kent.edu][4]

Date: August 2024

###### Abstract.

Let the Ducci function D: ℤ m n → ℤ m n D:\mathbb{Z}_{m}^{n}\to\mathbb{Z}_{m}^{n} be defined as

 | D ⁡ ( x 1, x 2, …, x n) = ( x 1 + x 2 ​ mod ​ m, x 2 + x 3 ​ mod ​ m, …, x n + x 1 ​ mod ​ m) D(x_{1},x_{2},...,x_{n})=(x_{1}+x_{2}\;\text{mod}\;m,x_{2}+x_{3}\;\text{mod}\;m,...,x_{n}+x_{1}\;\text{mod}\;m) |  |

and let the Ducci sequence of 𝐮 \mathbf{u} be the sequence { D α ​ ( 𝐮) } α = 0 ∞ \{D^{\alpha}(\mathbf{u})\}_{\alpha=0}^{\infty}. In this paper, we will provide another proof that for n = 2 k n=2^{k} and m = 2 l m=2^{l}, that all Ducci sequences will end in ( 0, 0, …, 0) (0,0,...,0) and additionally prove that this will happen in at most 2 k − 1 ​ ( l + 1) 2^{k-1}(l+1) iterations of D D.

###### Key words and phrases:

Ducci sequence, modular arithmetic, length, period, n n -Number Game

###### 1991 Mathematics Subject Classification

20D60, 11B83, 11B50

## 1. Introduction

Consider a function D: ℤ m n → ℤ m n D:\mathbb{Z}_{m}^{n}\to\mathbb{Z}_{m}^{n}, which we define as

 | D ⁡ ( x 1, x 2, …, x n) = ( x 1 + x 2 ​ mod ​ m, x 2 + x 3 ​ mod ​ m, …, x n + x 1 ​ mod ​ m). D(x_{1},x_{2},...,x_{n})=(x_{1}+x_{2}\;\text{mod}\;m,x_{2}+x_{3}\;\text{mod}\;m,...,x_{n}+x_{1}\;\text{mod}\;m). |  |

Like [2, 10, 12], we call D D the Ducci function and for a given tuple 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n}, we say that the Ducci sequence of 𝐮 \mathbf{u} is the sequence { D α ​ ( 𝐮) } α = 0 ∞ \{D^{\alpha}(\mathbf{u})\}_{\alpha=0}^{\infty}.

Looking at an example, consider ( 3, 1, 3) ∈ ℤ 4 3 (3,1,3)\in\mathbb{Z}_{4}^{3} and the first few terms in its Ducci sequence: ( 3, 1, 3), ( 0, 0, 2), ( 0, 2, 2), ( 2, 0, 2), ( 2, 2, 0), ( 0, 2, 2) (3,1,3),(0,0,2),(0,2,2),(2,0,2),(2,2,0),(0,2,2). One can see that if you continue the Ducci sequence, it cycles through the tuples ( 0, 2, 2), ( 2, 0, 2), (0,2,2),(2,0,2), ( 2, 2, 0) (2,2,0). We say that these three tuples are the Ducci cycle of the Ducci sequence of ( 3, 1, 3) (3,1,3). More specifically, we say that the Ducci cycle of a tuple 𝐮 \mathbf{u} is the set { 𝐯 ∣ ∃ α ∈ ℤ + ∪ { 0 }, β ∈ ℤ + ∋ 𝐯 = D α + β ( 𝐮) = D α ( 𝐮) } \{\mathbf{v}\mid\exists\alpha\in\mathbb{Z}^{+}\cup\{0\},\beta\in\mathbb{Z}^{+}\ni\mathbf{v}=D^{\alpha+\beta}(\mathbf{u})=D^{\alpha}(\mathbf{u})\}, a term [2, 7, 14] also uses. We define 𝐋𝐞𝐧 ⁡ ( 𝐮) \mathbf{Len(u)} to be the smallest α \alpha that can be found to satisfy the equation 𝐯 = D α + β ​ ( 𝐮) = D α ​ ( 𝐮) \mathbf{v}=D^{\alpha+\beta}(\mathbf{u})=D^{\alpha}(\mathbf{u}) from our definition for some β ∈ ℤ +, 𝐯 ∈ ℤ m n \beta\in\mathbb{Z}^{+},\mathbf{v}\in\mathbb{Z}_{m}^{n}. We also define 𝐏𝐞𝐫 ⁡ ( 𝐮) \mathbf{Per(u)} to be the smallest β \beta that satisfies the same equation. We obtain the notations of L ​ e ​ n ​ ( 𝐮) Len(\mathbf{u}) and P ​ e ​ r ​ ( 𝐮) Per(\mathbf{u}) from Definition 1 of [2], with [3, 6, 10] being some other sources that call this the period. Notice that P ​ e ​ r ​ ( 𝐮) Per(\mathbf{u}) is also the number of distinct tuples in the Ducci cycle of 𝐮 \mathbf{u}. If a tuple 𝐯 ∈ ℤ m n \mathbf{v}\in\mathbb{Z}_{m}^{n} is in the Ducci cycle of the Ducci sequence for some tuple 𝐮 \mathbf{u}, we may simply say that 𝐯 \mathbf{v} is in a Ducci cycle. Because ℤ m n \mathbb{Z}_{m}^{n} is finite, every Ducci sequence enters a cycle.

Define K ⁡ ( ℤ m n) K(\mathbb{Z}_{m}^{n}) to be the set of all tuples in ℤ m n \mathbb{Z}_{m}^{n} that are in the Ducci cycle for the Ducci sequence of some 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n},which is given in Definition 4 of [2]. The following theorem about K ⁡ ( ℤ m n) K(\mathbb{Z}_{m}^{n}) is stated on page 6001 of [2] but we will provide a proof of it in Section 3:

###### Theorem 1.

K ⁡ ( ℤ m n) K(\mathbb{Z}_{m}^{n}) is a subgroup of ℤ m n \mathbb{Z}_{m}^{n}.

If for a tuple 𝐮 \mathbf{u} there exists a tuple 𝐯 \mathbf{v} such that D ⁡ ( 𝐯) = 𝐮 D(\mathbf{v})=\mathbf{u}, we say that 𝐯 \mathbf{v} is a predecessor of 𝐮 \mathbf{u}. We believe page 259 of [14] is the first time this term is used, then later by [2, 12].

It is not always the case that the Ducci sequence ends in a cycle containing more than one tuple. Notice that the Ducci cycle of ( 0, 0, …, 0) (0,0,...,0) consists only of itself and that it satisfies P ​ e ​ r ​ ( 𝐮) = 1 Per(\mathbf{u})=1. In addition to this, ( 0, 0, …, 0) (0,0,...,0) is the only tuple that satisfies D ⁡ ( 𝐮) = 𝐮 D(\mathbf{u})=\mathbf{u}, which we believe is first noted in Remark 5 of [6] and then again by [2]. This means that only ( 0, 0, …, 0) (0,0,...,0) and tuples whose Ducci cycle are { ( 0, 0,.., 0) } \{(0,0,..,0)\} have a period of 1 1. We say that a Ducci sequence vanishes when its cycle is { ( 0, 0, …, 0) } \{(0,0,...,0)\}, a term first used by [6] on page 117 and also by [2, 12].

An important Ducci sequence is the one corresponding to ( 0, 0, …, 0, 1) ∈ ℤ m n (0,0,...,0,1)\in\mathbb{Z}_{m}^{n}. We call the Ducci sequence of this tuple the basic Ducci sequence of ℤ m n \mathbb{Z}_{m}^{n}, like [10] first uses on page 302, as well as [2, 9, 12]. In a similar way to particularly [2] in Definition 5 and to [10, 12], we denote L m ​ ( n) = L ​ e ​ n ​ ( 0, 0, …, 0, 1) L_{m}(n)=Len(0,0,...,0,1) and P m ​ ( n) = P ​ e ​ r ​ ( 0, 0, …, 0, 1) P_{m}(n)=Per(0,0,...,0,1). These are significant because Lemma 1 in [2] tells us that for every 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n}, L m ​ ( n) ≥ L ​ e ​ n ​ ( 𝐮) L_{m}(n)\geq Len(\mathbf{u}) and P ​ e ​ r ​ ( 𝐮) | P m ​ ( n) Per(\mathbf{u})|P_{m}(n). Page 858 of [3] also uses the notation of P m ​ ( n) P_{m}(n) to mean the maximal period for a Ducci sequence on ℤ m n \mathbb{Z}_{m}^{n}.

In this paper, we focus on the case where m = 2 l m=2^{l} and n = 2 k n=2^{k} for integers k, l ≥ 1 k,l\geq 1. It is first proven in (I) on page 103 of [19] that all Ducci sequences in ℤ 2 l 2 k \mathbb{Z}_{2^{l}}^{2^{k}} vanish. Theorem 2.3 of [9] also provides a proof of this. However, we would like to establish a value for L m ​ ( n) L_{m}(n) in this case. Our main goal is to prove the following theorem:

###### Theorem 2.

Let n = 2 k n=2^{k}, m = 2 l m=2^{l} for integers l, k ≥ 1 l,k\geq 1. Then L m ​ ( n) = ( l + 1) ​ 2 k − 1 L_{m}(n)=(l+1)2^{k-1} and P m ​ ( n) = 1 P_{m}(n)=1.

As part of his proof, [19] finds that D l ∗ 2 k ​ ( 𝐮) = ( 0, 0, …, 0) D^{l*2^{k}}(\mathbf{u})=(0,0,...,0) for every tuple 𝐮 ∈ ℤ 2 l 2 k \mathbf{u}\in\mathbb{Z}_{2^{l}}^{2^{k}}, however, neither [19] nor [9] find a value for L 2 l ​ ( 2 k) L_{2^{l}}(2^{k}).

It is worth noting that as a result of all Ducci sequences vanishing, we gain the following corollary:

###### Corollary 3.

K ⁡ ( ℤ 2 l 2 k) K(\mathbb{Z}_{2^{l}}^{2^{k}}) is the trivial subgroup.

The work in this paper was done while the second author was a Ph.D. student at Kent State University under the advisement of the first author and will appear as part of the second author’s dissertation.

## 2. Background

There are many different versions of the Ducci function. The first and most common Ducci function is D ¯: ( ℤ + ∪ { 0 }) n → ( ℤ + ∪ { 0 }) n \bar{D}:(\mathbb{Z}^{+}\cup\{0\})^{n}\to(\mathbb{Z}^{+}\cup\{0\})^{n} being defined as D ¯ ​ ( x 1, x 2, …, x n) = ( | x 1 − x 2 |, | x 2 − x 3 |, …, | x n − x 1 |) \bar{D}(x_{1},x_{2},...,x_{n})=(|x_{1}-x_{2}|,|x_{2}-x_{3}|,...,|x_{n}-x_{1}|), with [10, 11, 12, 14] being a few examples, or similarly defined on ℤ n \mathbb{Z}^{n} like in [2]. Other sources, such as [5, 7, 18], define it on ℝ n \mathbb{R}^{n}. Note that if 𝐮 ∈ ℤ n \mathbf{u}\in\mathbb{Z}^{n}, then D ¯ ​ ( 𝐮) ∈ ( ℤ + ∪ { 0 }) n \bar{D}(\mathbf{u})\in(\mathbb{Z}^{+}\cup\{0\})^{n}. Therefore, for simplicity, we will refer to the Ducci case on ( ℤ + ∪ { 0 }) n (\mathbb{Z}^{+}\cup\{0\})^{n} or ℤ n \mathbb{Z}^{n} as the Ducci case on ℤ n \mathbb{Z}^{n}.

For both Ducci on ℤ n \mathbb{Z}^{n} and Ducci on ℝ n \mathbb{R}^{n}, it has been proven that all Ducci sequences enter a cycle. Some examples of sources that explain why this happens on ℤ n \mathbb{Z}^{n} are [6, 10, 12, 14] and [18] proves it for ℝ n \mathbb{R}^{n} in Theorem 2. For Ducci on ℤ n \mathbb{Z}^{n}, when looking at the tuples in a Ducci cycle, all of the entries belong to { 0, c } \{0,c\} for some c ∈ ℤ + c\in\mathbb{Z}^{+}, which is proved in Lemma 3 of [14] and then again later by [16]. Because D ¯ ​ ( λ ​ 𝐮) = λ ​ D ¯ ​ ( 𝐮) \bar{D}(\lambda\mathbf{u})=\lambda\bar{D}(\mathbf{u}) when λ ∈ ℤ \lambda\in\mathbb{Z} and 𝐮 ∈ ℤ n \mathbf{u}\in\mathbb{Z}^{n}, this means that for this case, one only needs to worry about when Ducci is defined on ℤ 2 \mathbb{Z}_{2} when examining Ducci cycles and periods, something that [2, 10, 12, 14] all talk about. For the ℝ n \mathbb{R}^{n} case, [18] proves a similar result in Theorem 1: if the Ducci sequence reaches a limit point, then all of the entries in the tuple belong to { 0, c } \{0,c\} for some c ∈ ℝ c\in\mathbb{R}.

It has been proven that the Ducci sequence will eventually vanish for all tuples in ℤ n \mathbb{Z}^{n} if and only if if n n is a power of 2 2. According to [4, 7], [8] is the first to provide a proof of this with other papers, like [12, 14], also citing [8] for a proof of this fact. [8] is also the first paper published that talks about Ducci sequences. Unfortunately, we are unable to find a copy of [8]; a review of the paper can be found at [17]. Many different proofs for the fact that all Ducci sequences vanish have been made since [8], with [10, 11, 15, 16] being a few. As discussed in the introduction, this conclusion can be extended to m = 2 l m=2^{l} where l ≥ 1 l\geq 1. Our ultimate goal is to establish how long we can expect it to take for a sequence to reach ( 0, 0, …, 0) (0,0,...,0).

For the Ducci case on ℤ 2 n \mathbb{Z}_{2}^{n}, there have been a few sources that look at the maximum value of the length of a Ducci sequence, L 2 ​ ( n) L_{2}(n), for a variety of values for n n. The first source is [10] on page 303 who found that for odd n n, L 2 ​ ( n) = 1 L_{2}(n)=1. The next example is the specific case where n = 2 k 1 + 2 k 2 n=2^{k_{1}}+2^{k_{2}} for k 1 > k 2 ≥ 0 k_{1}>k_{2}\geq 0 by [12] in Theorem 6, who finds L 2 ​ ( n) = 2 k 2 L_{2}(n)=2^{k_{2}}. Theorem 4 of [1] then extends this to all even n n, finding that if n = 2 k ​ n 1 n=2^{k}n_{1} where n 1 n_{1} is odd, then L 2 ​ ( n) = 2 k L_{2}(n)=2^{k}. This supports the case where l = 1 l=1 for Theorem 2.

Returning to our Ducci case, [19] is the first paper to look at Ducci sequences on ℤ m n \mathbb{Z}_{m}^{n}, followed by [2, 3, 9].

We start by discussing more about our example of the Ducci cycle of ( 3, 1, 3) (3,1,3) to provide a better visualization of what Ducci sequences in ℤ m n \mathbb{Z}_{m}^{n} look like. We can do this by creating a transition graph that maps all of the Ducci sequences of ℤ 4 3 \mathbb{Z}_{4}^{3} and direct our focus to the connected component containing ( 3, 1, 3) (3,1,3), which can be found in Figure 1.

( 0, 2, 2) (0,2,2) ( 0, 0, 2) (0,0,2) ( 3, 1, 3) (3,1,3) ( 1, 3, 1) (1,3,1) ( 2, 2, 0) (2,2,0) ( 0, 2, 0) (0,2,0) ( 3, 1, 1) (3,1,1) ( 1, 3, 3) (1,3,3) ( 2, 0, 2) (2,0,2) ( 2, 0, 0) (2,0,0) ( 1, 1, 3) (1,1,3) ( 3, 3, 1) (3,3,1)

Figure 1. Transition Graph for ℤ 4 3 \mathbb{Z}_{4}^{3}

Using our definitions from before, one can see L ​ e ​ n ​ ( 3, 1, 3) = 2 Len(3,1,3)=2, L ​ e ​ n ​ ( 0, 0, 2) = 1 Len(0,0,2)=1, and L ​ e ​ n ​ ( 0, 2, 2) = 0 Len(0,2,2)=0. Although ( 1, 3, 1) (1,3,1) is not in the Ducci sequence of ( 3, 1, 3) (3,1,3), we can see that the Ducci sequences of ( 3, 1, 3) (3,1,3) and ( 1, 3, 1) (1,3,1) have the same Ducci cycle, as well as every other tuple, in this connected component. In addition to this, all of these tuples have period 3 3.

Notice that ( 0, 0, 2) (0,0,2) has two predecessors, ( 3, 1, 3) (3,1,3) and ( 1, 3, 1) (1,3,1). But not all tuples have predecessors; both ( 3, 1, 3) (3,1,3) and ( 1, 3, 1) (1,3,1) are examples of this.

We also present the transition graph for ℤ 4 2 \mathbb{Z}_{4}^{2} to give an example where all Ducci sequences vanish in Figure 2.

( 0, 0) (0,0) ( 1, 3) (1,3) ( 3, 1) (3,1) ( 2, 2) (2,2) ( 0, 2) (0,2) ( 2, 0 CLOSE (2,0 ( 3, 3) (3,3) ( 0, 3) (0,3) ( 3, 0) (3,0) ( 1, 2) (1,2) ( 2, 1) (2,1) ( 1, 1) (1,1) ( 0, 1) (0,1) ( 1, 0) (1,0) ( 2, 3) (2,3) ( 3, 2) (3,2)

Figure 2. Transition graph for ℤ 4 2 \mathbb{Z}_{4}^{2}

For this graph, all tuples in ℤ 4 2 \mathbb{Z}_{4}^{2} are part of the same component. Here, we can see that L 2 ​ ( 4) = 3 L_{2}(4)=3, but not all tuples without predecessors have this length. For example, ( 2, 3) (2,3) and ( 1, 3) (1,3) both do not have predecessors, but L ​ e ​ n ​ ( 2, 3) = 3 Len(2,3)=3 and L ​ e ​ n ​ ( 1, 3) = 1 Len(1,3)=1.
Notice that all tuples in ℤ 4 2 \mathbb{Z}_{4}^{2} that have a predecessor have exactly four predecessors. This is not a coincidence, in fact,

###### Theorem 4.

Let n n be even. If a tuple 𝐮 = ( x 1, x 2, …, x n) ∈ ℤ m n \mathbf{u}=(x_{1},x_{2},...,x_{n})\in\mathbb{Z}_{m}^{n} has a predecessor ( y 1, y 2, …, y n) (y_{1},y_{2},...,y_{n}), then ( y 1 + z, y 2 − z, …, y n − 1 + z, y n − z) (y_{1}+z,y_{2}-z,...,y_{n-1}+z,y_{n}-z) is also a predecessor of 𝐮 \mathbf{u} where z ∈ ℤ m z\in\mathbb{Z}_{m}. Moreover, if a tuple 𝐮 \mathbf{u} has a predecessor, it has exactly m m predecessors.

###### Proof.

Let x i, y i ∈ ℤ m x_{i},y_{i}\in\mathbb{Z}_{m}. Clearly, if ( y 1, y 2, …, y n) (y_{1},y_{2},...,y_{n}) is a predecessor to ( x 1, x 2, …, x n) (x_{1},x_{2},...,x_{n}), then so is ( y 1 + z, y 2 − z, …, y n − z) (y_{1}+z,y_{2}-z,...,y_{n}-z) if z ∈ ℤ m z\in\mathbb{Z}_{m}. This gives us at least m predecessors to ( x 1, x 2, …, x n) (x_{1},x_{2},...,x_{n}), each beginning with a different element in ℤ m \mathbb{Z}_{m}.

We now confirm that these are all the predecessors of ( x 1, x 2, …, x n) (x_{1},x_{2},...,x_{n}). If we consider two tuples that are predecessors to ( x 1, x 2, …, x n) (x_{1},x_{2},...,x_{n}) that both begin with the same element, say ( y 1, y 2, …, y n) (y_{1},y_{2},...,y_{n}) and ( y 1, y 2 ′, …, y n ′) (y_{1},y_{2}^{\prime},...,y_{n}^{\prime}), then we have the relations

 | y 1 + y 2 ≡ x 1 ​ mod ​ m y_{1}+y_{2}\equiv x_{1}\;\text{mod}\;m |  |

and

 | y 1 + y 2 ′ ≡ x 1 ​ mod ​ m, y_{1}+y_{2}^{\prime}\equiv x_{1}\;\text{mod}\;m, |  |

which gives us y 2 = y 2 ′ y_{2}=y_{2}^{\prime}. We can repeat this to see y i = y i ′ y_{i}=y_{i}^{\prime} for every i, 1 ≤ i ≤ n i,1\leq i\leq n and to see that ( x 1, x 2, …, x n) (x_{1},x_{2},...,x_{n}) only has one unique predecessor beginning with y 1 y_{1}, so it has exactly m m predecessors. ∎

Let’s now draw our attention back to D D specifically. Because

 | D ⁡ ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) = D ⁡ ( x 1 + x 1 ′, x 2 + x 2 ′, …, x n + x n ′) D((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}))=D(x_{1}+x_{1}^{\prime},x_{2}+x_{2}^{\prime},...,x_{n}+x_{n}^{\prime}) |  |

 | = ( x 1 + x 2 + x 1 ′ + x 2 ′, x 2 + x 3 + x 2 ′ + x 3 ′, …, x n + x 1 + x n ′ + x 1 ′) =(x_{1}+x_{2}+x_{1}^{\prime}+x_{2}^{\prime},x_{2}+x_{3}+x_{2}^{\prime}+x_{3}^{\prime},...,x_{n}+x_{1}+x_{n}^{\prime}+x_{1}^{\prime}) |  |

 | = ( x 1 + x 2, x 2 + x 3, …, x n + x 1) + ( x 1 ′ + x 2 ′, x 2 ′ + x 3 ′, …, x n ′ + x 1 ′) =(x_{1}+x_{2},x_{2}+x_{3},...,x_{n}+x_{1})+(x_{1}^{\prime}+x_{2}^{\prime},x_{2}^{\prime}+x_{3}^{\prime},...,x_{n}^{\prime}+x_{1}^{\prime}) |  |

 | = D ⁡ ( x 1, x 2, …, x n) + D ⁡ ( x 1 ′, x 2 ′, …, x n ′), =D(x_{1},x_{2},...,x_{n})+D(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}), |  |

it is true that D ∈ E ​ n ​ d ​ ( ℤ m n) D\in End(\mathbb{Z}_{m}^{n}). Notice also that it remains true that D ⁡ ( λ ​ 𝐮) = λ ​ D ​ ( 𝐮) D(\lambda\mathbf{u})=\lambda D(\mathbf{u}) when λ ∈ ℤ m \lambda\in\mathbb{Z}_{m} and 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n}. Since this means D α ​ ( λ ​ 𝐮) = λ ​ D α ​ ( 𝐮) D^{\alpha}(\lambda\mathbf{u})=\lambda D^{\alpha}(\mathbf{u}) for α ∈ ℤ + \alpha\in\mathbb{Z}^{+}, the Ducci sequence for λ ​ 𝐮 \lambda\mathbf{u} is { λ ​ D α ​ ( 𝐮) } α = 0 ∞ \{\lambda D^{\alpha}(\mathbf{u})\}_{\alpha=0}^{\infty} and if 𝐮 ∈ K ⁡ ( ℤ m n) \mathbf{u}\in K(\mathbb{Z}_{m}^{n}), then so is λ ​ 𝐮 \lambda\mathbf{u}.
Define H: ℤ m n → ℤ m n H:\mathbb{Z}_{m}^{n}\to\mathbb{Z}_{m}^{n} as

 | H ⁡ ( x 1, x 2, …, x n) = ( x 2, x 3, …, x n, x 1). H(x_{1},x_{2},...,x_{n})=(x_{2},x_{3},...,x_{n},x_{1}). |  |

We also have that H ∈ E ​ n ​ d ​ ( ℤ m n) H\in End(\mathbb{Z}_{m}^{n}) and D = I + H D=I+H where I I is the identity endomorphism. Note that

 | H ( D ( x 1, x 2,.., x n)) = H ( x 1 + x 2, x 2 + x 3, …, x n + x 1) H(D(x_{1},x_{2},..,x_{n}))=H(x_{1}+x_{2},x_{2}+x_{3},...,x_{n}+x_{1}) |  |

 | = ( x 2 + x 3, x 3 + x 4, …, x n + x 1, x 2 + x 1) =(x_{2}+x_{3},x_{3}+x_{4},...,x_{n}+x_{1},x_{2}+x_{1}) |  |

 | = D ( x 2, x 3,.., x n, x 1) =D(x_{2},x_{3},..,x_{n},x_{1}) |  |

 | = D ⁡ ( H ⁡ ( x 1, x 2, …, x n)), =D(H(x_{1},x_{2},...,x_{n})), |  |

and therefore H, D H,D commute. This means that if { D α ​ ( 𝐮) } α = 0 ∞ \{D^{\alpha}(\mathbf{u})\}_{\alpha=0}^{\infty} is the Ducci sequence for 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n}, then { H β ​ ( D α ​ ( 𝐮)) } α = 0 ∞ \{H^{\beta}(D^{\alpha}(\mathbf{u}))\}_{\alpha=0}^{\infty} is the Ducci sequence for H β ​ ( 𝐮) H^{\beta}(\mathbf{u}) when 0 ≤ β ≤ n − 1 0\leq\beta\leq n-1. Consequently, if 𝐮 ∈ K ⁡ ( ℤ m n) \mathbf{u}\in K(\mathbb{Z}_{m}^{n}), then so is H β ​ ( 𝐮) H^{\beta}(\mathbf{u}).

## 3. Findings on Ducci for n, m n,m Arbitrary

We can now prove Theorem 1 from Section 1. Note that this theorem is stated as a fact in [2], but a proof is provided here for completeness.

###### Proof of Theorem 1.

We start by showing that

 | D α ​ ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) = D α ​ ( x 1, x 2, …, x n) + D α ​ ( x 1 ′, x 2 ′, …, x n ′) D^{\alpha}((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}))=D^{\alpha}(x_{1},x_{2},...,x_{n})+D^{\alpha}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}) |  |

by induction for α ∈ ℤ + {\alpha}\in\mathbb{Z}^{+}. This is true for α = 1 {\alpha}=1 because D D is an endomorphism.

Assume that it is true for α − 1 \alpha-1, then

 | D α ​ ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) = D ⁡ ( D α − 1 ​ ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) CLOSE. D^{\alpha}((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}))=D(D^{\alpha-1}((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime})). |  |

By induction, we have

 | D ⁡ ( D α − 1 ​ ( x 1, x 2, …, x n) + D α − 1 ​ ( x 1 ′, x 2 ′, …, x n ′)) D(D^{\alpha-1}(x_{1},x_{2},...,x_{n})+D^{\alpha-1}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime})) |  |

and

 | D ⁡ ( D α − 1 ​ ( x 1, x 2, …, x n)) + D ⁡ ( D α − 1 ​ ( x 1 ′, x 2 ′, …, x n ′)), D(D^{\alpha-1}(x_{1},x_{2},...,x_{n}))+D(D^{\alpha-1}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime})), |  |

which equals D α ​ ( x 1, x 2, …, x n) + D α ​ ( x 1 ′, x 2 ′, …, x n ′) D^{\alpha}(x_{1},x_{2},...,x_{n})+D^{\alpha}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}).

Now suppose that ( x 1, x 2, …, x n), ( x 1 ′, x 2 ′, …, x n ′) ∈ K ⁡ ( ℤ m n) (x_{1},x_{2},...,x_{n}),(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime})\in K(\mathbb{Z}_{m}^{n}). If d = P m ​ ( n) d=P_{m}(n), then D d ​ ( x 1, x 2, …, x n) = ( x 1, x 2, …, x n) D^{d}(x_{1},x_{2},...,x_{n})=(x_{1},x_{2},...,x_{n}) and D d ​ ( x 1 ′, x 2 ′, …, x n ′) = ( x 1 ′, x 2 ′, …, x n ′) D^{d}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime})=(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}). Therefore,

 | D d ​ ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) = D d ​ ( x 1, x 2, …, x n) + D d ​ ( x 1 ′, x 2 ′, …, x n ′), D^{d}((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}))=D^{d}(x_{1},x_{2},...,x_{n})+D^{d}(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}), |  |

which equals ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′) (x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}) and thus

 | ( ( x 1, x 2, …, x n) + ( x 1 ′, x 2 ′, …, x n ′)) ∈ K ⁡ ( ℤ m n). ((x_{1},x_{2},...,x_{n})+(x_{1}^{\prime},x_{2}^{\prime},...,x_{n}^{\prime}))\in K(\mathbb{Z}_{m}^{n}). |  |

It follows then that K ⁡ ( ℤ m n) ≤ ℤ m n K(\mathbb{Z}_{m}^{n})\leq\mathbb{Z}_{m}^{n}. ∎

When examining a Ducci sequence, it is useful to be able to know what D r ​ ( 𝐮) D^{r}(\mathbf{u}) is given 𝐮 ∈ ℤ m n \mathbf{u}\in\mathbb{Z}_{m}^{n}. To do this, define a r, s, r, s ∈ ℤ a_{r,s},r,s\in\mathbb{Z}, r ≥ 0, 1 ≤ s ≤ n r\geq 0,1\leq s\leq n so that D r ​ ( 0, 0, …, 0, 1) = ( a r, n, a r, n − 1, …, a r, 1) D^{r}(0,0,...,0,1)=(a_{r,n},a_{r,n-1},...,a_{r,1}). Now, any tuple ( x 1, x 2, …, x n) ∈ ℤ m n (x_{1},x_{2},...,x_{n})\in\mathbb{Z}_{m}^{n} can be written as

 | ( x 1, x 2, …, x n) = ∑ s = 1 n x s H − s ( 0, 0,.., 0, 1), (x_{1},x_{2},...,x_{n})=\sum_{s=1}^{n}x_{s}H^{-s}(0,0,..,0,1), |  |

which gives

 | D r ​ ( x 1, x 2, …, x n) = ∑ s = 1 n x s ​ H − s ​ ( a r, n, a r, n − 1, …, a r, 1) D^{r}(x_{1},x_{2},...,x_{n})=\sum_{s=1}^{n}x_{s}H^{-s}(a_{r,n},a_{r,n-1},...,a_{r,1}) |  |

or

 | ∑ s = 1 n x s ​ ( a r, s, a r, s − 1, …, a r, s + 1). \sum_{s=1}^{n}x_{s}(a_{r,s},a_{r,s-1},...,a_{r,s+1}). |  |

Using this, we can now define a r, s a_{r,s} as the coefficient on x s − i + 1 x_{s-i+1} in the i i th coordinate of D r ​ ( x 1, x 2, …, x n) D^{r}(x_{1},x_{2},...,x_{n}), with

 | a 0, s = { 0 s ≠ 1 1 s = 1. a_{0,s}=\begin{cases}0&s\neq 1\\ 1&s=1\end{cases}. |  |

We now aim to prove a few more observations about a r, s a_{r,s}.

###### Theorem 5.

Let r ≥ 1 r\geq 1, 1 ≤ s ≤ n 1\leq s\leq n

1. (1)

a r, s = a r − 1, s + a r − 1, s − 1 a_{r,s}=a_{r-1,s}+a_{r-1,s-1}.

2. (2)

For r < n r<n, a r, s = ( r s − 1) a_{r,s}=\displaystyle{\binom{r}{s-1}}.

3. (3)

a r + t, s = ∑ i = 1 n a t, i ​ a r, s − i + 1 a_{r+t,s}=\displaystyle{\sum_{i=1}^{n}a_{t,i}a_{r,s-i+1}} where t ≥ 1 t\geq 1.

###### Proof.

(1): Letting i = 1 i=1, we only need to show a r, s a_{r,s} as the coefficient on x s x_{s} in the first entry of D r ​ ( x 1, x 2, …, x n) D^{r}(x_{1},x_{2},...,x_{n}). Note that by how a r, s a_{r,s} is defined, D r ​ ( x 1, x 2, …, x n) D^{r}(x_{1},x_{2},...,x_{n}) is

 | D ⁡ ( ( ∑ s = 1 n x s ​ H − s ​ ( a r − 1, n, a r − 1, n − 1, …, a r − 1, 1)) CLOSE. D((\sum_{s=1}^{n}x_{s}H^{-s}(a_{r-1,n},a_{r-1,n-1},...,a_{r-1,1})). |  |

The first entry of this tuple is

 | ( a r − 1, 1 + a r − 1, n) ​ x 1 + ( a r − 1, 2 + a r − 1, 1) ​ x 2 + ⋯ + ( a r, n + a r, n − 1) ​ x n. (a_{r-1,1}+a_{r-1,n})x_{1}+(a_{r-1,2}+a_{r-1,1})x_{2}+\cdots+(a_{r,n}+a_{r,n-1})x_{n}. |  |

By definition, a r, s a_{r,s} is the coefficient on x s x_{s} in the first entry, which the above tells us is also a r − 1, s + a r − 1, s − 1 a_{r-1,s}+a_{r-1,s-1} and (1) follows.

We prove (2) and (3) by induction.

(2): Basis Step 𝐫 = 𝟎 \mathbf{r=0}: This follows from (1) and

 | a 0, s = { 0 s ≠ 1 1 s = 1. a_{0,s}=\begin{cases}0&s\neq 1\\ 1&s=1\end{cases}. |  |

Inductive Step: Note that if s − 1 > r s-1>r, we use the convention that

 | a r, s = ( r s − 1) = 0. a_{r,s}=\binom{r}{s-1}=0. |  |

Assume a r − 1, s = ( r − 1 s − 1) a_{r-1,s}=\displaystyle{\binom{r-1}{s-1}} when r < n r<n. By (1), we have that for 1 < s ≤ n 1<s\leq n,

 | a r, s = a r − 1, s + a r − 1, s − 1, a_{r,s}=a_{r-1,s}+a_{r-1,s-1}, |  |

which by induction is

 | ( r − 1 s − 1) + ( r − 1 s − 2) \binom{r-1}{s-1}+\binom{r-1}{s-2} |  |

or

 | ( r s − 1). \binom{r}{s-1}. |  |

For s = 1 s=1, we have

 | a r, 1 = a r − 1, 1 + a r − 1, n. a_{r,1}=a_{r-1,1}+a_{r-1,n}. |  |

By induction, this is

 | ( r − 1 0) + ( r − 1 n − 1) \binom{r-1}{0}+\binom{r-1}{n-1} |  |

which is 1 1 or ( r 0) \displaystyle{\binom{r}{0}} as long as r < n r<n.

(3): We prove this via induction on t t.

Basis Steps 𝐭 = 𝟏, 𝟐 \mathbf{t=1,2}: Calculating a r, s a_{r,s} in terms of a r − 1, i a_{r-1,i} terms,

 | a r, s = a r − 1, s + a r − 1, s − 1, a_{r,s}=a_{r-1,s}+a_{r-1,s-1}, |  |

or breaking it down further in terms of a r − 2, i a_{r-2,i},

 | a r, s = a r − 2, s + 2 ​ a r − 2, s − 1 + a r − 2, s − 2. a_{r,s}=a_{r-2,s}+2a_{r-2,s-1}+a_{r-2,s-2}. |  |

This is a 2, 1 ​ a r − 2, s + a 2, 2 ​ a r − 2, s − 1 + a 2, 3 ​ a r − 2, s − 2 a_{2,1}a_{r-2,s}+a_{2,2}a_{r-2,s-1}+a_{2,3}a_{r-2,s-2} and the basis case follows.

Inductive Step: Assume that for t ′ < t t^{\prime}<t, a r + t ′, s = ∑ i = 1 n a t ′, i ​ a r, s − i + 1 a_{r+t^{\prime},s}=\displaystyle{\sum_{i=1}^{n}a_{t^{\prime},i}a_{r,s-i+1}}. Then calculating a r + t, s a_{r+t,s}, we have

 | a r + t, s = ∑ i = 1 n a t − 1, i ​ a r + 1, s − i + 1. a_{r+t,s}=\sum_{i=1}^{n}a_{t-1,i}a_{r+1,s-i+1}\,. |  |

Breaking down a r, s − i + 1 a_{r,s-i+1}, this is

 | ∑ i = 1 n a t − 1, i ​ ( a r, s − i + 1 + a r, s − i). \sum_{i=1}^{n}a_{t-1,i}(a_{r,s-i+1}+a_{r,s-i})\,. |  |

Distributing a t − 1, i a_{t-1,i} and breaking the sum up, this is

 | ∑ i = 1 n a t − 1, i ​ a r, s − i + 1 + ∑ i = 1 n a t − 1, i ​ a r, s − i. \sum_{i=1}^{n}a_{t-1,i}a_{r,s-i+1}+\sum_{i=1}^{n}a_{t-1,i}a_{r,s-i}\,. |  | (3.1) |

Note that for the sum ∑ i = 1 n a t − 1, i ​ a r, s − i \displaystyle{\sum_{i=1}^{n}a_{t-1,i}a_{r,s-i}} from Expression ( 3.1), we have

 | ∑ i = 1 n a t − 1, i ​ a r, s − i = ∑ i = 2 n + 1 a t − 1, i − 1 ​ a r, s − i + 1. \sum_{i=1}^{n}a_{t-1,i}a_{r,s-i}=\sum_{i=2}^{n+1}a_{t-1,i-1}a_{r,s-i+1}\,. |  |

Because the s s coordinate of a r, s a_{r,s} is reduced modulo n n, this is

 | ∑ i = 1 n a t − 1, i − 1 ​ a r, s − i + 1. \sum_{i=1}^{n}a_{t-1,i-1}a_{r,s-i+1}\,. |  |

Therefore, Expression ( 3.1) is equal to

 | ∑ i = 1 n ( a t − 1, i + a t − 1, i − 1) ​ a r, s − i + 1 \sum_{i=1}^{n}(a_{t-1,i}+a_{t-1,i-1})a_{r,s-i+1} |  |

or

 | ∑ i = 1 n a t, i ​ a r, s − i + 1. \sum_{i=1}^{n}a_{t,i}a_{r,s-i+1}\,. |  |

(3) follows from here. ∎

We now prove some other useful facts about the a r, s a_{r,s} coefficients that we will need later.

###### Corollary 6.

 | a n, 1 = { ( n s − 1) s ≠ 1 2 s = 1. a_{n,1}=\begin{cases}\displaystyle{\binom{n}{s-1}}&s\neq 1\\ 2&s=1\end{cases}. |  |

###### Proof.

Let s > 1 s>1. Then a n, s = a n − 1, s + a n − 1, s − 1 a_{n,s}=a_{n-1,s}+a_{n-1,s-1} gives us

 | a n, s = ( n − 1 s − 1) + ( n − 1 s − 2) a_{n,s}=\binom{n-1}{s-1}+\binom{n-1}{s-2} |  |

or ( n s − 1) \displaystyle{\binom{n}{s-1}} by Theorem 5

For s = 1 s=1, a n, 1 = a n − 1, 1 + a n − 1, n a_{n,1}=a_{n-1,1}+a_{n-1,n} gives us

 | ( n − 1 0) + ( n − 1 n − 1) \binom{n-1}{0}+\binom{n-1}{n-1} |  |

or 2 2 by Theorem 5. ∎

We have one last lemma about the a r, s a_{r,s} that is true for all n, m n,m:

###### Lemma 7.

For r ≥ 0 r\geq 0,

 | a r, s = a r, r − s + 2. a_{r,s}=a_{r,r-s+2}\,. |  |

###### Proof.

We work by induction on r r.

Basis Step: We take advantage of Theorem 5 to see that when r < n r<n,

 | a r, s = ( r s − 1) = ( r r − s + 1) = a r, r − s + 2. a_{r,s}=\binom{r}{s-1}=\binom{r}{r-s+1}=a_{r,r-s+2}\,. |  |

Inductive Step: Suppose that the theorem is true for r − 1 r-1. Then we have

 | a r − 1, s = a r − 1, r − s + 1 a_{r-1,s}=a_{r-1,r-s+1} |  |

and

 | a r − 1, s − 1 = a r − 1, r − s + 2. a_{r-1,s-1}=a_{r-1,r-s+2}\,. |  |

Then because a r, s = a r − 1, s + a r − 1, s − 1 a_{r,s}=a_{r-1,s}+a_{r-1,s-1},

 | a r, s = a r − 1, r − s + 1 + a r − 1, r − s + 2, a_{r,s}=a_{r-1,r-s+1}+a_{r-1,r-s+2}, |  |

which equals a r, r − s + 2 a_{r,r-s+2}. ∎

## 4. All Tuples Vanish in ℤ 2 l 2 k \mathbb{Z}_{2^{l}}^{2^{k}}

Recall that it is our main goal to prove that for m = 2 l, n = 2 k m=2^{l},n=2^{k}, then L m ​ ( n) = ( l + 1) ​ 2 k − 1 L_{m}(n)=(l+1)2^{k-1}. In order to do this, we first aim to prove a number of lemmas, starting with a few lemmas that explore the value of certain binomial coefficients. We believe that Lemmas 8 - 10, and 12 are known but we are including the following proofs for the sake of completeness. Throughout these proofs, we rely on the well known fact that ( 2 j t) \displaystyle{\binom{2^{j}}{t}} is even when t ≠ 1, 2 j t\neq 1,2^{j}, a proof of which can be found in Theorem 3 of [13].

###### Lemma 8.

When j ≥ 2 j\geq 2

 | ( 2 j 2 j − 1) ≡ 2 ​ mod ​ 4. \binom{2^{j}}{2^{j-1}}\equiv 2\;\text{mod}\;4. |  |

###### Proof.

By the Chu-Vandermonde identity [9], ( 2 j 2 j − 1) \displaystyle{\binom{2^{j}}{2^{j-1}}} is

 | ∑ i = 0 2 j − 1 ( 2 j − 1 i) 2 = ( 2 j − 1 0) 2 + ( 2 j − 1 2 j − 1) 2 + ∑ i = 1 2 j − 1 − 1 ( 2 j − 1 i) 2, \sum_{i=0}^{2^{j-1}}\binom{2^{j-1}}{i}^{2}=\binom{2^{j-1}}{0}^{2}+\binom{2^{j-1}}{2^{j-1}}^{2}+\sum_{i=1}^{2^{j-1}-1}\binom{2^{j-1}}{i}^{2}, |  |

which is congruent to 2 ​ mod ​ 4. 2\;\text{mod}\;4. ∎

For the other binomial coefficients ( 2 j t) \displaystyle{\binom{2^{j}}{t}}, we have the following lemma:

###### Lemma 9.

When t ≠ 0, 2 j − 1, 2 j t\neq 0,2^{j-1},2^{j} and j ≥ 2 j\geq 2, then

 | ( 2 j t) ≡ 0 ​ mod ​ 4. \binom{2^{j}}{t}\equiv 0\;\text{mod}\;4. |  |

###### Proof.

First to address the cases when t ∈ { 0, 2 j − 1, 2 j } t\in\{0,2^{j-1},2^{j}\}, we know ( 2 j 0) = ( 2 j 2 j) = 1 \displaystyle{\binom{2^{j}}{0}=\binom{2^{j}}{2^{j}}=1} and ( 2 j 2 j − 1) ≡ 2 ​ mod ​ 4 \displaystyle{\binom{2^{j}}{2^{j-1}}}\equiv 2\;\text{mod}\;4. We prove the rest of the lemma by induction on j j.

Basis Step 𝐣 = 𝟐 \mathbf{j=2}:

 | ( 4 1) = ( 4 3) = 4. \binom{4}{1}=\binom{4}{3}=4. |  |

Inductive Step: Assume that ( 2 j − 1 t) ≡ 0 ​ mod ​ 4 \displaystyle{\binom{2^{j-1}}{t}}\equiv 0\;\text{mod}\;4 when t ≠ 0, 2 j − 2, 2 j − 1 t\neq 0,2^{j-2},2^{j-1}. We start with when 0 < t < 2 j − 2 0<t<2^{j-2} and use the Chu-Vandermonde identity to see that ( 2 j t) \displaystyle{\binom{2^{j}}{t}} is

 | ∑ i = 0 t ( 2 j − 1 i) ​ ( 2 j − 1 t − i) = ( 2 j − 1 0) ​ ( 2 j − 1 t) + ( 2 j − 1 t) ​ ( 2 j − 1 0) + ∑ i = 1 t − 1 ( 2 j − 1 i) ​ ( 2 j − 1 t − i), \sum_{i=0}^{t}\binom{2^{j-1}}{i}\binom{2^{j-1}}{t-i}=\binom{2^{j-1}}{0}\binom{2^{j-1}}{t}+\binom{2^{j-1}}{t}\binom{2^{j-1}}{0}+\sum_{i=1}^{t-1}\binom{2^{j-1}}{i}\binom{2^{j-1}}{t-i}, |  |

which is congruent to 0 ​ mod ​ 4 0\;\text{mod}\;4 by induction. Next we take 2 j − 2 < t < 2 j − 1 2^{j-2}<t<2^{j-1}; calculating ( 2 j t) \displaystyle{\binom{2^{j}}{t}} yields

 | ( 2 j − 1 0) ​ ( 2 j − 1 t) + ( 2 j − 1 t) ​ ( 2 j − 1 0) + ( 2 j − 1 2 j − 2) ​ ( 2 j − 1 t − 2 j − 2) \binom{2^{j-1}}{0}\binom{2^{j-1}}{t}+\binom{2^{j-1}}{t}\binom{2^{j-1}}{0}+\binom{2^{j-1}}{2^{j-2}}\binom{2^{j-1}}{t-2^{j-2}} |  |

 | + ( 2 j − 1 t − 2 j − 2) ​ ( 2 j − 1 2 j − 2) + ∑ i = 1 i ≠ 2 j − 2, t − 2 j − 2 t − 1 ( 2 j − 1 i) ​ ( 2 j − 1 t − i), +\binom{2^{j-1}}{t-2^{j-2}}\binom{2^{j-1}}{2^{j-2}}+\sum_{\begin{subarray}{c}i=1\\ i\neq 2^{j-2},t-2^{j-2}\end{subarray}}^{t-1}\binom{2^{j-1}}{i}\binom{2^{j-1}}{t-i}, |  |

which by induction is congruent to 0 ​ mod ​ 4 0\;\text{mod}\;4. Now if we take t = 2 j − 2 t=2^{j-2}, then ( 2 j 2 j − 2) \displaystyle{\binom{2^{j}}{2^{j-2}}} is

 | ( 2 j − 1 0) ​ ( 2 j − 1 2 j − 2) + ( 2 j − 1 2 j − 2) ​ ( 2 j − 1 0) + ∑ i = 1 2 j − 2 − 1 ( 2 j − 1 i) ​ ( 2 j − 1 t − i), \binom{2^{j-1}}{0}\binom{2^{j-1}}{2^{j-2}}+\binom{2^{j-1}}{2^{j-2}}\binom{2^{j-1}}{0}+\sum_{i=1}^{2^{j-2}-1}\binom{2^{j-1}}{i}\binom{2^{j-1}}{t-i}, |  |

which is equivalent to 0 ​ mod ​ 4 0\;\text{mod}\;4 by Lemma 8 and induction.

Now suppose that 2 j − 1 < t < 2 j 2^{j-1}<t<2^{j}. Then 0 < 2 j − t < 2 j − 1 0<2^{j}-t<2^{j-1}, so

 | ( 2 j t) = ( 2 j 2 j − t) ≡ 0 ​ mod ​ 4 \binom{2^{j}}{t}=\binom{2^{j}}{2^{j}-t}\equiv 0\;\text{mod}\;4 |  |

and the lemma follows.

∎

We still need to know more about the value of ( 2 j 2 j − 1) \displaystyle{\binom{2^{j}}{2^{j-1}}} so we prove the following lemma:

###### Lemma 10.

For j ≥ 2 j\geq 2,

 | ( 2 j 2 j − 1) ≡ 6 ​ mod ​ 8. \binom{2^{j}}{2^{j-1}}\equiv 6\;\text{mod}\;8. |  |

###### Proof.

Basis Step 𝐣 = 𝟐: \mathbf{j=2}:

 | ( 4 2) = 6. \binom{4}{2}=6. |  |

Inductive Step: Assume ( 2 j − 1 2 j − 2) ≡ 6 ​ mod ​ 8 \displaystyle{\binom{2^{j-1}}{2^{j-2}}}\equiv 6\;\text{mod}\;8. By the Chu-Vandermonde Identity, ( 2 j 2 j − 1) \displaystyle{\binom{2^{j}}{2^{j-1}}} is

 | ∑ i = 0 2 j − 1 ( 2 j − 1 i) 2 = ( 2 j − 1 0) 2 + ( 2 j − 1 2 j − 1) 2 + ( 2 j − 1 2 j − 2) 2 + ∑ i = 1 i ≠ 2 j − 2 2 j − 1 − 1 ( 2 j − 1 i) 2, \sum_{i=0}^{2^{j-1}}\binom{2^{j-1}}{i}^{2}=\binom{2^{j-1}}{0}^{2}+\binom{2^{j-1}}{2^{j-1}}^{2}+\binom{2^{j-1}}{2^{j-2}}^{2}+\sum_{\begin{subarray}{c}i=1\\ i\neq 2^{j-2}\end{subarray}}^{2^{j-1}-1}\binom{2^{j-1}}{i}^{2}, |  |

which by induction and Lemma 9 is ≡ 6 ​ mod ​ 8 \equiv 6\;\text{mod}\;8. ∎

Lemma 11 follows from Lucas’s Theorem, which can be found in many books, including [10]:

###### Lemma 11.

( 2 j − 1 t) \displaystyle{\binom{2^{j}-1}{t}} is odd for every 0 ≤ t ≤ 2 j − 1 0\leq t\leq 2^{j}-1.

To be more specific about ( 2 j − 1 2 j − 1) \displaystyle{\binom{2^{j}-1}{2^{j-1}}}, we have the following lemma:

###### Lemma 12.

For j ≥ 2 j\geq 2,

 | ( 2 j − 1 2 j − 1) ≡ 3 ​ mod ​ 4. \binom{2^{j}-1}{2^{j-1}}\equiv 3\;\text{mod}\;4. |  |

###### Proof.

We prove this via induction.

Basis Step j = 2 j=2:

 | ( 3 2) = 3. \binom{3}{2}=3. |  |

Inductive Step: Assume that ( 2 j − 1 − 1 2 j − 2) ≡ 3 ​ mod ​ 4 \displaystyle{\binom{2^{j-1}-1}{2^{j-2}}}\equiv 3\;\text{mod}\;4. By the Chu-Vandermonde Identity,

 | ( 2 j − 1 2 j − 1) = ∑ i = 0 2 j − 1 ( 2 j − 1 i) ​ ( 2 j − 1 − 1 2 j − 1 − i) \binom{2^{j}-1}{2^{j-1}}=\sum_{i=0}^{2^{j-1}}\binom{2^{j-1}}{i}\binom{2^{j-1}-1}{2^{j-1}-i} |  |

or

 | ( 2 j − 1 0) ​ ( 2 j − 1 − 1 2 j − 1) + ( 2 j − 1 2 j − 1) ​ ( 2 j − 1 − 1 0) + ( 2 j − 1 2 j − 2) ​ ( 2 j − 1 − 1 2 j − 2) \ \binom{2^{j-1}}{0}\binom{2^{j-1}-1}{2^{j-1}}+\binom{2^{j-1}}{2^{j-1}}\binom{2^{j-1}-1}{0}+\binom{2^{j-1}}{2^{j-2}}\binom{2^{j-1}-1}{2^{j-2}} |  |

 | + ∑ i = 1 i ≠ 2 j − 2 2 j − 1 − 1 ( 2 j − 1 i) ( 2 j − 1 − 1 2 j − 1 − i). +\sum_{\begin{subarray}{c}i=1\\ i\neq 2^{j-2}\end{subarray}}^{2^{j-1}-1}\binom{2^{j-1}}{i}\binom{2^{j-1}-1}{2^{j-1}-i}. |  |

This is equivalent to 1 + ( 2 ∗ 3) ​ mod ​ 4 ≡ 3 ​ mod ​ 4. 1+(2*3)\;\text{mod}\;4\equiv 3\;\text{mod}\;4. ∎

We now direct our attention back to the a r, s a_{r,s} coefficients and examine what happens at certain values of r r. We first note that for n = 2 k n=2^{k}, a r, s + 2 k − 1 = a r, s − 2 k − 1 a_{r,s+2^{k-1}}=a_{r,s-2^{k-1}}.

###### Lemma 13.

Let l ≥ 1 l\geq 1 and n = 2 k n=2^{k}. Then for every 1 ≤ s ≤ 2 k 1\leq s\leq 2^{k},

 | a l ​ 2 k − 1, s + a l ​ 2 k − 1, s − 2 k − 1 ≡ 0 ​ mod ​ 2 l. a_{l2^{k-1},s}+a_{l2^{k-1},s-2^{k-1}}\equiv 0\;\text{mod}\;2^{l}. |  |

###### Proof.

We prove this by induction on l l. Because of how long the subscripts on the a r, s a_{r,s} coefficients will end up being in the next few proofs, we will be defining a few functions to represent certain coefficients. Let f ⁡ ( γ, δ) = a γ ​ 2 k − 1, δ f(\gamma,\delta)=a_{\gamma 2^{k-1},\delta}. In terms of f f, we want to show

 | f ⁡ ( l, s) + f ⁡ ( l, s − 2 k − 1) ≡ 0 ​ mod ​ 2 l. f(l,s)+f(l,s-2^{k-1})\equiv 0\;\text{mod}\;2^{l}. |  |

Basis Step 𝐥 = 𝟏 \mathbf{l=1}: It suffices to show f ⁡ ( 1, s) + f ⁡ ( 1, s − 2 k − 1) ≡ 0 ​ mod ​ 2 f(1,s)+f(1,s-2^{k-1})\equiv 0\;\text{mod}\;2. Then for s ≠ 1, 2 k − 1 + 1 s\neq 1,2^{k-1}+1,

 | f ⁡ ( 1, s) + f ⁡ ( 1, s − 2 k − 1) = ( 2 k − 1 s − 1) + ( 2 k − 1 s − 2 k − 1 − 1) ≡ 0 ​ mod ​ 2 f(1,s)+f(1,s-2^{k-1})=\binom{2^{k-1}}{s-1}+\binom{2^{k-1}}{s-2^{k-1}-1}\equiv 0\;\text{mod}\;2 |  |

because both of these binomial coefficients are even. For s = 1, 2 k − 1 + 1 s=1,2^{k-1}+1,

 | f ⁡ ( 1, 1) + f ⁡ ( 1, 1 + 2 k − 1) = ( 2 k − 1 0) + ( 2 k − 1 2 k − 1) ≡ 0 ​ mod ​ 2 f(1,1)+f(1,1+2^{k-1})=\binom{2^{k-1}}{0}+\binom{2^{k-1}}{2^{k-1}}\equiv 0\;\text{mod}\;2 |  |

and the basis case follows.

Inductive Step: Assume f ⁡ ( l − 1, s) + f ⁡ ( l − 1, s − 2 k − 1) ≡ 0 ​ mod ​ 2 l − 1 f(l-1,s)+f(l-1,s-2^{k-1})\equiv 0\;\text{mod}\;2^{l-1}, then

 | f ⁡ ( l, s) + f ⁡ ( l, s − 2 k − 1) f(l,s)+f(l,s-2^{k-1}) |  |

is

 | ∑ i = 1 2 k [f ⁡ ( l − 1, i) ​ f ​ ( 1, s − i + 1) + f ⁡ ( l − 1, i) ​ f ​ ( 1, s − 2 k − 1 − i + 1)]. \sum_{i=1}^{2^{k}}[f(l-1,i)f(1,s-i+1)+f(l-1,i)f(1,s-2^{k-1}-i+1)]. |  |

We now break this up into the following two sums:

 | ∑ i = 1 2 k − 1 [f ⁡ ( l − 1, i) ​ f ​ ( 1, s − i + 1) + f ⁡ ( l − 1, i) ​ f ​ ( 1, s − 2 k − 1 − i + 1)] \sum_{i=1}^{2^{k-1}}[f(l-1,i)f(1,s-i+1)+f(l-1,i)f(1,s-2^{k-1}-i+1)] |  |

 | + ∑ i = 2 k − 1 + 1 2 k [f ( l − 1, i) f ( 1, s − i + 1) + f ( l − 1, i) f ( 1, s − 2 k − 1 − i + 1)]. +\sum_{i=2^{k-1}+1}^{2^{k}}[f(l-1,i)f(1,s-i+1)+f(l-1,i)f(1,s-2^{k-1}-i+1)]. |  |

Changing the indices of the second sum to match the first, this is

 | ∑ i = 1 2 k − 1 [f ⁡ ( l − 1, i) ​ f ​ ( 1, s − i + 1) + f ⁡ ( l − 1, i) ​ f ​ ( 1, s − 2 k − 1 − i + 1)] \sum_{i=1}^{2^{k-1}}[f(l-1,i)f(1,s-i+1)+f(l-1,i)f(1,s-2^{k-1}-i+1)] |  |

 | + ∑ i = 1 2 k − 1 [f ( l − 1, i − 2 k − 1) f ( 1, s − i + 2 k − 1 + 1) + f ( l − 1, i − 2 k − 1) f ( 1, s − i + 1)], +\sum_{i=1}^{2^{k-1}}[f(l-1,i-2^{k-1})f(1,s-i+2^{k-1}+1)+f(l-1,i-2^{k-1})f(1,s-i+1)], |  |

which can be factored into

 | ∑ i = 1 2 k − 1 [f ⁡ ( 1, s − i + 1) + f ⁡ ( 1, s − i + 2 k − 1 + 1)] ​ [f ⁡ ( l − 1, i) + f ⁡ ( l − 1, i − 2 k − 1)]. \sum_{i=1}^{2^{k-1}}[f(1,s-i+1)+f(1,s-i+2^{k-1}+1)][f(l-1,i)+f(l-1,i-2^{k-1})]. |  | (4.1) |

By induction, since f ⁡ ( l − 1, i) + f ⁡ ( l − 1, i − 2 k − 1) ≡ 0 ​ mod ​ 2 l − 1 f(l-1,i)+f(l-1,i-2^{k-1})\equiv 0\;\text{mod}\;2^{l-1}, the addend in the sum from ( 4.1) is congruent to 0 ​ mod ​ 2 l 0\;\text{mod}\;2^{l} if both f ⁡ ( 1, s − i + 1) f(1,s-i+1) and f ⁡ ( 1, s − i + 2 k − 1 + 1) f(1,s-i+2^{k-1}+1) are even. The only times this does not happen is when i = s i=s and i = s + 2 k − 1 i=s+2^{k-1}. In both cases, the addend in the sum of ( 4.1) is

 | [f ⁡ ( 1, 1) + f ⁡ ( 1, 2 k − 1 + 1)] ​ [f ⁡ ( l − 1, 1) + f ⁡ ( l − 1, 2 k − 1 + 1)]. [f(1,1)+f(1,2^{k-1}+1)][f(l-1,1)+f(l-1,2^{k-1}+1)]. |  |

This is

 | 2 ​ [f ⁡ ( l − 1, 1) + f ⁡ ( l − 1, 2 k − 1 + 1)], 2[f(l-1,1)+f(l-1,2^{k-1}+1)], |  |

which is equivalent to 0 ​ mod ​ 2 l 0\;\text{mod}\;2^{l} by induction. Therefore, ( 4.1) is ≡ 0 ​ mod ​ 2 l \equiv 0\;\text{mod}\;2^{l} and the lemma follows. ∎

We have one last lemma to prove before Theorem 2. We are once more interested in a sum of two specific a r, s a_{r,s} coefficients.

###### Lemma 14.

Let n = 2 k n=2^{k}. For l ≥ 3 l\geq 3,

 | a ( l − 1) ​ 2 k − 1, l ​ 2 k − 2 + 1 + a ( l − 1) ​ 2 k − 1, l ​ 2 k − 2 − 2 k − 1 + 1 ≡ 0 ​ mod ​ 2 l. a_{(l-1)2^{k-1},l2^{k-2}+1}+a_{(l-1)2^{k-1},l2^{k-2}-2^{k-1}+1}\equiv 0\;\text{mod}\;2^{l}. |  |

###### Proof.

Let g ⁡ ( γ, ϵ, δ) = a γ ​ 2 k − 1, ϵ ​ 2 k − 2 + δ g(\gamma,\epsilon,\delta)=a_{\gamma 2^{k-1},\epsilon 2^{k-2}+\delta}. Written in terms of g g, we want to show

 | g ⁡ ( l − 1, l, 1) + g ⁡ ( l − 1, l, 2 k − 1 + 1) ≡ 0 ​ mod ​ 2 l. g(l-1,l,1)+g(l-1,l,2^{k-1}+1)\equiv 0\;\text{mod}\;2^{l}. |  |

Calculating g ⁡ ( l − 1, l, 1) + g ⁡ ( l − 1, l, 2 k − 1 + 1) g(l-1,l,1)+g(l-1,l,2^{k-1}+1), we have

 | ∑ i = 1 2 k [f ⁡ ( 1, i) ​ g ​ ( l − 2, l, 2 − i) + f ⁡ ( 1, i) ​ g ​ ( l − 2, l, 2 k − 1 + 2 − i)]. \sum_{i=1}^{2^{k}}[f(1,i)g(l-2,l,2-i)+f(1,i)g(l-2,l,2^{k-1}+2-i)]. |  |

Like in the proof of Lemma 13, we break the sum up and adjust the indices to give

 | ∑ i = 1 2 k − 1 [f ⁡ ( 1, i) ​ g ​ ( l − 2, l, 2 − i) + f ⁡ ( 1, i) ​ g ​ ( l − 2, l, 2 k − 1 + 2 − i)] \sum_{i=1}^{2^{k-1}}[f(1,i)g(l-2,l,2-i)+f(1,i)g(l-2,l,2^{k-1}+2-i)] |  |

 | + ∑ i = 1 2 k − 1 [f ( 1, i − 2 k − 1) g ( l − 2, l, 2 k − 1 + 2 − i) + f ( 1, i − 2 k − 1) g ( l − 2, l, 2 − i)]. +\sum_{i=1}^{2^{k-1}}[f(1,i-2^{k-1})g(l-2,l,2^{k-1}+2-i)+f(1,i-2^{k-1})g(l-2,l,2-i)]. |  |

Factoring yields

 | ∑ i = 1 2 k − 1 [f ⁡ ( 1, i) + f ⁡ ( 1, i − 2 k − 1)] ​ [g ⁡ ( l − 2, l, 2 − i) + g ⁡ ( l − 2, l, 2 k − 1 + 2 − i)]. \sum_{i=1}^{2^{k-1}}[f(1,i)+f(1,i-2^{k-1})][g(l-2,l,2-i)+g(l-2,l,2^{k-1}+2-i)]. |  | (4.2) |

Note that by Lemma 13, g ⁡ ( l − 2, l, 2 − i) + g ⁡ ( l − 2, l, 2 k − 1 + 2 − i) ≡ 0 ​ mod ​ 2 l − 2 g(l-2,l,2-i)+g(l-2,l,2^{k-1}+2-i)\equiv 0\;\text{mod}\;2^{l-2}. Consequently, if f ⁡ ( 1, i) + f ⁡ ( 1, i − 2 k − 1) ≡ 0 ​ mod ​ 4 f(1,i)+f(1,i-2^{k-1})\equiv 0\;\text{mod}\;4, then the whole addend in the sum of ( 4.2) is congruent to 0 ​ mod ​ 2 l 0\;\text{mod}\;2^{l}.

Note that if i ≠ 1, 2 k − 2 + 1, 2 k − 1 + 1, 2 k − 1 + 2 k − 2 + 1 i\neq 1,2^{k-2}+1,2^{k-1}+1,2^{k-1}+2^{k-2}+1, then both f ⁡ ( 1, i) f(1,i) and f ⁡ ( 1, i − 2 k − 1) f(1,i-2^{k-1}) are equivalent to 0 ​ mod ​ 4 0\;\text{mod}\;4. So reducing modulo 2 l 2^{l}, Expression ( 4.2) is

 | [f ⁡ ( 1, 1) + f ⁡ ( 1, 2 k − 1 + 1)] ​ [g ⁡ ( l − 2, l, 1) ​ g ​ ( l − 2, l, 2 k − 1 + 1)] [f(1,1)+f(1,2^{k-1}+1)][g(l-2,l,1)g(l-2,l,2^{k-1}+1)] |  |

 | + [f ⁡ ( 1, 2 k − 1 + 1) + f ⁡ ( 1, 1)] ​ [g ⁡ ( l − 2, l, 2 k − 1 + 1) + g ⁡ ( l − 2, l, 1)] +[f(1,2^{k-1}+1)+f(1,1)][g(l-2,l,2^{k-1}+1)+g(l-2,l,1)] |  |

 | + [g ⁡ ( 1, 1, 1) + g ⁡ ( 1, 1, 2 k − 1 + 1)] ​ [g ⁡ ( l − 2, l − 1, 1) + g ⁡ ( l − 2, l − 1, 2 k − 1 + 1)] +[g(1,1,1)+g(1,1,2^{k-1}+1)][g(l-2,l-1,1)+g(l-2,l-1,2^{k-1}+1)] |  |

 | + [g ⁡ ( 1, 1, 2 k − 1 + 1) + g ⁡ ( 1, 1, 1)] ​ [g ⁡ ( l − 2, l − 1, 2 k − 1 + 1) + g ⁡ ( l − 2, l − 1, 1)], +[g(1,1,2^{k-1}+1)+g(1,1,1)][g(l-2,l-1,2^{k-1}+1)+g(l-2,l-1,1)], |  |

which is congruent to 0 ​ mod ​ 2 l 0\;\text{mod}\;2^{l} by Lemma 13 when l − 2 ≥ 1 l-2\geq 1.

∎

We now have all the tools we will use to prove our main theorem.

###### Proof of Theorem 2.

We once more note that in (I) on page 103 of [19] and in Theorem 2.3 of [9], it is proved that all tuples vanish in ℤ 2 l 2 k \mathbb{Z}_{2^{l}}^{2^{k}} for l, k ∈ ℤ + l,k\in\mathbb{Z}^{+}. We also provide a proof of this because to prove that L 2 l ​ ( 2 k) = ( l + 1) ​ 2 k − 1 L_{2^{l}}(2^{k})=(l+1)2^{k-1}, we will show D ( l + 1) ​ 2 k − 1 ​ ( 0, 0, …, 0, 1) = ( 0, 0, …, 0) D^{(l+1)2^{k-1}}(0,0,...,0,1)=(0,0,...,0), which will give us that P 2 l ​ ( 2 k) = 1 P_{2^{l}}(2^{k})=1 and all tuples in ℤ 2 l 2 k \mathbb{Z}_{2^{l}}^{2^{k}} vanish.

We prove this via induction on l l with two basis cases. However, we will often need to use theorems that rely on k ≥ 2 k\geq 2 in our proof, so we first prove our theorem for k = 1 k=1 or that L 2 l ​ ( 2) = l + 1 L_{2^{l}}(2)=l+1 and that P 2 l ​ ( 2) = 1 P_{2^{l}}(2)=1 for every l > 0 l>0.

Basis Step 𝐤 = 𝟏 \mathbf{k=1}: Notice that D α ​ ( 0, 1) = ( 2 α − 1, 2 α − 1) D^{\alpha}(0,1)=(2^{\alpha-1},2^{\alpha-1}). This means that D l + 1 ​ ( 0, 1) = ( 0, 0) D^{l+1}(0,1)=(0,0) and that P 2 l ​ ( 2) = 1 P_{2^{l}}(2)=1. Since we also have that

 | D l ​ ( 0, 1) = ( 2 l − 1, 2 l − 1) ≢ ( 0, 0) ​ mod ​ 2 l, D^{l}(0,1)=(2^{l-1},2^{l-1})\not\equiv(0,0)\;\text{mod}\;2^{l}, |  |

L 2 l ​ ( 2) = l + 1 L_{2^{l}}(2)=l+1 follows.

For the rest of the proof, we assume n = 2 k n=2^{k}, k ≥ 1 k\geq 1.

Basis Step 𝐥 = 𝟏 \mathbf{l=1}: We first prove f ⁡ ( 2, s) ≡ 0 ​ mod ​ 2 f(2,s)\equiv 0\;\text{mod}\;2 for all 1 ≤ s ≤ n 1\leq s\leq n. Recall that f ⁡ ( 2, 1) = 2 f(2,1)=2 and for s ≠ 1 s\neq 1, f ⁡ ( 2, s) = ( 2 k s − 1) ≡ 0 ​ mod ​ 2 f(2,s)=\displaystyle{\binom{2^{k}}{s-1}}\equiv 0\;\text{mod}\;2 which gives us P 2 ​ ( 2 k) = 1 P_{2}(2^{k})=1. Note also that for r < 2 k r<2^{k}, a r, 1 = 1 ≢ 0 ​ mod ​ 2 a_{r,1}=1\not\equiv 0\;\text{mod}\;2. Therefore, this is the first time we have that a r, s ≡ 0 ​ mod ​ 2 a_{r,s}\equiv 0\;\text{mod}\;2 for all s s, so L 2 ​ ( 2 k) = 2 k L_{2}(2^{k})=2^{k}.

Basis Step 𝐥 = 𝟐 \mathbf{l=2}: It suffices to show that L 4 ​ ( 2 k) = 3 ∗ 2 k − 1 L_{4}(2^{k})=3*2^{k-1} and P 4 ​ ( 2 k) = 1 P_{4}(2^{k})=1. We begin by showing that f ⁡ ( 3, s) ≡ 0 ​ mod ​ 4 f(3,s)\equiv 0\;\text{mod}\;4 for every s. Start by noting

 | f ⁡ ( 3, s) = ∑ i = 1 2 k f ⁡ ( 1, i) ​ f ​ ( 2, s − i + 1) f(3,s)=\sum_{i=1}^{2^{k}}f(1,i)f(2,s-i+1) |  |

and then separate the terms where i = 1, 2 k − 1 + 1 i=1,2^{k-1}+1 to produce

 | f ⁡ ( 1, 2 k − 1 + 1) ​ f ​ ( 2, s − 2 k − 1) + f ⁡ ( 1, 1) ​ f ​ ( 2, s) + ∑ i = 2 i ≠ 2 k − 1 + 1 f ⁡ ( 1, i) ​ f ​ ( 2, s − i + 1). f(1,2^{k-1}+1)f(2,s-2^{k-1})+f(1,1)f(2,s)+\sum_{\begin{subarray}{c}i=2\\ i\neq 2^{k-1}+1\end{subarray}}f(1,i)f(2,s-i+1). |  | (4.3) |

We do this because f ⁡ ( 1, i) ≡ 0 ​ mod ​ 2 f(1,i)\equiv 0\;\text{mod}\;2 for i ≠ 1, 2 k − 1 + 1 i\neq 1,2^{k-1}+1 and f ⁡ ( 2, s − i + 1) ≡ 0 ​ mod ​ 2 f(2,s-i+1)\equiv 0\;\text{mod}\;2 as shown in our first basis case. So now Expression ( 4.3) is equivalent to

 | f ⁡ ( 2, s − 2 k − 1) + f ⁡ ( 2, s) ​ mod ​ 4, f(2,s-2^{k-1})+f(2,s)\;\text{mod}\;4, |  | (4.4) |

which, because of Lemma 13, is congruent to 0 ​ mod ​ 4 0\;\text{mod}\;4. Therefore we have that P 4 ​ ( 2 k) = 1 P_{4}(2^{k})=1 and L 4 ​ ( 2 k) ≤ 3 ∗ 2 k − 1 L_{4}(2^{k})\leq 3*2^{k-1}. So we now need to show that there exists s s such that a 3 ∗ 2 k − 1 − 1, s ≢ 0 ​ mod ​ 4 a_{3*2^{k-1}-1,s}\not\equiv 0\;\text{mod}\;4. Define h ⁡ ( γ, δ) = a γ ​ 2 k − 1 − 1, δ h(\gamma,\delta)=a_{\gamma 2^{k-1}-1,\delta} Calculating h ⁡ ( 3, s) h(3,s) for general s s, we have

 | h ⁡ ( 3, s) = ∑ i = 1 2 k f ⁡ ( 1, i) ​ h ​ ( 2, s − i + 1). h(3,s)=\sum_{i=1}^{2^{k}}f(1,i)h(2,s-i+1). |  |

We now separate the terms where i i is 1, 2 k − 2 + 1 1,2^{k-2}+1 or 2 k − 1 + 1 2^{k-1}+1, which gives

 | f ⁡ ( 1, 1) ​ h ​ ( 2, s) + f ⁡ ( 1, 2 k − 1 + 1) ​ h ​ ( 2, s − 2 k − 1) + g ⁡ ( 1, 1, 1) ​ h ​ ( 2, s − 2 k − 2) f(1,1)h(2,s)+f(1,2^{k-1}+1)h(2,s-2^{k-1})+g(1,1,1)h(2,s-2^{k-2}) |  | (4.5) |

 | + ∑ i ∈ J f ( 1, i) h ( 2, s − i + 1) +\sum_{i\in J}f(1,i)h(2,s-i+1) |  |

where J = { 2 ≤ i ≤ 2 k | i ≠ 2 k − 1, 2 k − 2 + 1 } J=\{2\leq i\leq 2^{k}\;|\;i\neq 2^{k-1},2^{k-2}+1\}. We do this so the sum over J J is congruent to 0 ​ mod ​ 4 0\;\text{mod}\;4 by Lemma 9. If we also take s = 1 s=1, Expression ( 4.5) is congruent to

 | f ⁡ ( 1, 1) ​ h ​ ( 2, 1) + f ⁡ ( 1, 2 k − 1 + 1) ​ h ​ ( 2, 2 k − 1 + 1) + g ⁡ ( 1, 1, 1) ​ h ​ ( 2, 2 k − 2 k − 2 + 1) ​ mod ​ 4, f(1,1)h(2,1)+f(1,2^{k-1}+1)h(2,2^{k-1}+1)+g(1,1,1)h(2,2^{k}-2^{k-2}+1)\;\text{mod}\;4, |  |

which is equivalent to 1 + h ⁡ ( 2, 2 k − 1 + 1) + 2 ​ mod ​ 4 1+h(2,2^{k-1}+1)+2\;\text{mod}\;4 because g ⁡ ( 1, 1, 1) ≡ 2 ​ mod ​ 4 g(1,1,1)\equiv 2\;\text{mod}\;4 and h ⁡ ( 2, 2 k − 2 k − 2 + 1) h(2,2^{k}-2^{k-2}+1) is odd. From Lemma 12, this is congruent to 2 ​ mod ​ 4 2\;\text{mod}\;4 and h ⁡ ( 3, 1) ≢ 0 ​ mod ​ 4 h(3,1)\not\equiv 0\;\text{mod}\;4, so L 4 ​ ( 2 k) = 3 ∗ 2 k − 1 L_{4}(2^{k})=3*2^{k-1}.

Inductive Step: Assume that L 2 l − 1 ​ ( 2 k) = l ​ 2 k − 1 L_{2^{l-1}}(2^{k})=l2^{k-1} and P 2 l − 1 ​ ( 2 k) = 1 P_{2^{l-1}}(2^{k})=1. This implies that f ⁡ ( l, s) ≡ 0 ​ mod ​ 2 l − 1 f(l,s)\equiv 0\;\text{mod}\;2^{l-1} for every s s. Calculating f ⁡ ( l + 1, s) f(l+1,s), we get

 | f ⁡ ( l + 1, s) = ∑ i = 1 2 k f ⁡ ( l, i) ​ f ​ ( 1, s − i + 1). f(l+1,s)=\sum_{i=1}^{2^{k}}f(l,i)f(1,s-i+1). |  |

If we separate out the terms where s − i + 1 = 1, 2 k − 1 + 1 s-i+1=1,2^{k-1}+1, this becomes

 | f ⁡ ( l, s) ​ f ​ ( 1, 1) + f ⁡ ( l, s − 2 k − 1) ​ f ​ ( 1, 2 k − 1 + 1) + ∑ i ∈ J f ⁡ ( l, i) ​ f ​ ( 1, s − i + 1) f(l,s)f(1,1)+f(l,s-2^{k-1})f(1,2^{k-1}+1)+\sum_{i\in J}f(l,i)f(1,s-i+1) |  | (4.6) |

where J = { 1 ≤ i ≤ 2 k | i ≠ s, s − 2 k − 1 } J=\{1\leq i\leq 2^{k}\;|\;i\neq s,s-2^{k-1}\}. We do this so the sum over J J is equivalent to 0 ​ mod ​ 2 l 0\;\text{mod}\;2^{l} by induction and because f ⁡ ( 1, s − i + 1) f(1,s-i+1) is even over J J. Therefore, Expression ( 4.6) is equivalent to

 | f ⁡ ( l, s) + f ⁡ ( l, s − 2 k − 1) ​ mod ​ 2 l, f(l,s)+f(l,s-2^{k-1})\;\text{mod}\;2^{l}, |  |

which by Lemma 13 is ≡ 0 ​ mod ​ 2 l \equiv 0\;\text{mod}\;2^{l}. This gives us that P m ​ ( n) = 1 P_{m}(n)=1 and

 | L m ​ ( n) ≤ ( l + 1) ​ 2 k − 1. L_{m}(n)\leq(l+1)2^{k-1}. |  |

Now showing L m ​ ( n) > ( l + 1) ​ 2 k − 1 − 1 L_{m}(n)>(l+1)2^{k-1}-1 will prove the rest of the theorem. Note that because P m ​ ( n) = 1 P_{m}(n)=1, it suffices to show that there exists s s such that

 | h ⁡ ( l + 1, s) ≢ 0 ​ mod ​ 2 l. h(l+1,s)\not\equiv 0\;\text{mod}\;2^{l}. |  |

We start by breaking down h ⁡ ( l + 1, s) h(l+1,s) as follows:

 | h ⁡ ( l + 1, s) = ∑ i = 1 2 k f ⁡ ( l, i) ​ h ​ ( 1, s − i + 1). h(l+1,s)=\sum_{i=1}^{2^{k}}f(l,i)h(1,s-i+1). |  | (4.7) |

Because a r, s = a r, r − s + 2 a_{r,s}=a_{r,r-s+2} by Lemma 7, most coefficients have another coefficient that it is equal to. The case where they do not is when s ≡ r − s + 2 ​ mod ​ 2 k s\equiv r-s+2\;\text{mod}\;2^{k}. For our case then, h ⁡ ( l, i) h(l,i) is not equal to another coefficient when

 | i = l ​ 2 k − 1 − i + 2 i=l2^{k-1}-i+2 |  |

and

 | i = l ​ 2 k − 1 − i + 2 k + 2. i=l2^{k-1}-i+2^{k}+2. |  |

Solving for i i, this is when i = l ​ 2 k − 2 + 1 i=l2^{k-2}+1 and i = l ​ 2 k − 2 + 2 k − 1 + 1. i=l2^{k-2}+2^{k-1}+1. We will separate these out from our sum so, using Equation ( 4.7), we can view h ⁡ ( l + 1, s) h(l+1,s) like

 | g ⁡ ( l, l, 1) ​ h ​ ( 1, s − l ​ 2 k − 2) + g ⁡ ( l, l, 2 k − 1 + 1) ​ h ​ ( 1, s − l ​ 2 k − 2 − 2 k − 1) g(l,l,1)h(1,s-l2^{k-2})+g(l,l,2^{k-1}+1)h(1,s-l2^{k-2}-2^{k-1}) |  |

 | + ∑ i ∈ M [f ( l, i) h ( 1, s − i + 1) + g ( l, 2 l, 2 − i) h ( 1, s − l 2 k − 1 + i − 1) +\sum_{i\in M}[f(l,i)h(1,s-i+1)+g(l,2l,2-i)h(1,s-l2^{k-1}+i-1) |  |

where M M is defined to preserve equality. We now take s = l ​ 2 k − 2 + 1 s=l2^{k-2}+1, so h ⁡ ( l + 1, l ​ 2 k − 2 + 1) h(l+1,l2^{k-2}+1) is

 | g ⁡ ( l, l, 1) ​ h ​ ( 1, 1) + g ⁡ ( l, l, 2 k − 1 + 1) ​ h ​ ( 1, 2 k − 1 + 1) g(l,l,1)h(1,1)+g(l,l,2^{k-1}+1)h(1,2^{k-1}+1) |  | (4.8) |

 | + ∑ i ∈ M [f ( l, i) h ( 1, l 2 k − 2 + 2 − i) + g ( l, l, 2 − i) h ( 1, l 2 k − 2 − l 2 k − 1 + i)]. +\sum_{i\in M}[f(l,i)h(1,l2^{k-2}+2-i)+g(l,l,2-i)h(1,l2^{k-2}-l2^{k-1}+i)]. |  |

Taking a look at each piece of ( 4.8), g ⁡ ( l, l, 2 k − 1 + 1) ​ h ​ ( 1, 2 k − 1 + 1) = 0 g(l,l,2^{k-1}+1)h(1,2^{k-1}+1)=0 because h ⁡ ( 1, 2 k − 1 + 1) = 0 h(1,2^{k-1}+1)=0. For the sum in ( 4.8), this is equal to

 | ∑ i ∈ M f ⁡ ( l, i) ​ [h ⁡ ( 1, l ​ 2 k − 2 + 2 − i) + h ⁡ ( 1, l ​ 2 k − 2 − l ​ 2 k − 1 + i)], \sum_{i\in M}f(l,i)[h(1,l2^{k-2}+2-i)+h(1,l2^{k-2}-l2^{k-1}+i)], |  |

because f ⁡ ( l, i) = g ⁡ ( l, l, 2 − i) f(l,i)=g(l,l,2-i). Since h ⁡ ( 1, s) h(1,s) is odd for all s s by Lemma 11,

 | h ⁡ ( 1, l ​ 2 k − 2 − i + 2) + h ⁡ ( 1, l ​ 2 k − 2 − l ​ 2 k − 1 + i) h(1,l2^{k-2}-i+2)+h(1,l2^{k-2}-l2^{k-1}+i) |  |

is even. We know f ⁡ ( l, i) ≡ 0 ​ mod ​ 2 l − 1 f(l,i)\equiv 0\;\text{mod}\;2^{l-1}, so the whole sum is ≡ 0 ​ mod ​ 2 l \equiv 0\;\text{mod}\;2^{l}. Therefore, reducing Expression ( 4.8) modulo 2 l 2^{l}, we conclude that

 | g ⁡ ( l + 1, l, 1) ≡ g ⁡ ( l, l, 1) ​ mod ​ 2 l. g(l+1,l,1)\equiv g(l,l,1)\;\text{mod}\;2^{l}. |  |

So if we can prove that g ⁡ ( l, l, 1) ≢ 0 ​ mod ​ 2 l g(l,l,1)\not\equiv 0\;\text{mod}\;2^{l}, then the theorem will follow. Since we already know that g ⁡ ( l, l, 1) ≡ 0 ​ mod ​ 2 l − 1 g(l,l,1)\equiv 0\;\text{mod}\;2^{l-1}, we need to prove the following claim:

Claim: g ⁡ ( l, l, 1) ≡ 2 l − 1 ​ mod ​ 2 l g(l,l,1)\equiv 2^{l-1}\;\text{mod}\;2^{l} for l ≥ 2 l\geq 2.

We prove this claim via induction l l.

Basis Step l = 2 \mathit{l=2}: g ⁡ ( 2, 2, 1) ≡ 2 ​ mod ​ 4 g(2,2,1)\equiv 2\;\text{mod}\;4 by Lemma 8 and the basis case follows.

Inductive Step: Assume now that g ⁡ ( l − 1, l − 1, 1) ≡ 2 l − 2 ​ mod ​ 2 l − 1 g(l-1,l-1,1)\equiv 2^{l-2}\;\text{mod}\;2^{l-1}, then g ⁡ ( l, l, 1) g(l,l,1) is

 | ∑ i = 1 2 k f ⁡ ( l − 1, i) ​ g ​ ( 1, l, 2 − i). \sum_{i=1}^{2^{k}}f(l-1,i)g(1,l,2-i). |  |

Let J ∗ = { 1 ≤ i ≤ 2 k | i ≠ ( l − 1) 2 k − 2 + 1, l 2 k − 2 + 1, l 2 k − 2 − 2 k − 1 + 1 } J^{*}=\{1\leq i\leq 2^{k}\;|\;i\neq(l-1)2^{k-2}+1,l2^{k-2}+1,l2^{k-2}-2^{k-1}+1\} and separate all terms not in J ∗ J^{*} to see this is

 | g ⁡ ( l − 1, l − 1, 1) ​ g ​ ( 1, 1, 1) + g ⁡ ( l − 1, l, 1) ​ f ​ ( 1, 1) + g ⁡ ( l − 1, l, 2 k − 1 + 1) ​ g ​ ( 1, 2, 1) g(l-1,l-1,1)g(1,1,1)+g(l-1,l,1)f(1,1)+g(l-1,l,2^{k-1}+1)g(1,2,1) |  | (4.9) |

 | + ∑ i ∈ J ∗ f ( l − 1, i) g ( 1, l, 2 − i) +\sum_{i\in J^{*}}f(l-1,i)g(1,l,2-i) |  |

Once more, we separate this sum over J ∗ J^{*} because it is ≡ 0 ​ mod ​ 2 l \equiv 0\;\text{mod}\;2^{l} because

 | f ⁡ ( l − 1, i) ≡ 0 ​ mod ​ 2 l − 2 f(l-1,i)\equiv 0\;\text{mod}\;2^{l-2} |  |

and g ⁡ ( 1, l, 2 − i) ≡ 0 ​ mod ​ 4 g(1,l,2-i)\equiv 0\;\text{mod}\;4 by Lemma 9. Looking at the remaining pieces from ( 4.9), g ⁡ ( l − 1, l − 1, 1) ​ g ​ ( 1, 1, 1) ≡ 2 l − 1 ​ mod ​ 2 l g(l-1,l-1,1)g(1,1,1)\equiv 2^{l-1}\;\text{mod}\;2^{l} by induction and Lemma 8. Next,

 | g ⁡ ( l − 1, l, 1) ​ f ​ ( 1, 1) + g ⁡ ( l − 1, l, 2 k − 1 + 1) ​ g ​ ( 1, 2, 1) = g ⁡ ( l − 1, l, 1) + g ⁡ ( l − 1, l, 2 k − 1 + 1) g(l-1,l,1)f(1,1)+g(l-1,l,2^{k-1}+1)g(1,2,1)=g(l-1,l,1)+g(l-1,l,2^{k-1}+1) |  |

which by Lemma 14 is ≡ 0 ​ mod ​ 2 l \equiv 0\;\text{mod}\;2^{l}. The claim follows.

Therefore, g ⁡ ( l + 1, l, 1) ≡ 2 l − 1 ​ mod ​ 2 l g(l+1,l,1)\equiv 2^{l-1}\;\text{mod}\;2^{l} and L m ​ ( n) > ( l + 1) ​ 2 k − 1 − 1 L_{m}(n)>(l+1)2^{k-1}-1. Hence, L m ​ ( n) = ( l + 1) ​ 2 k − 1 L_{m}(n)=(l+1)2^{k-1}. ∎

## References

- [1] Breuer, F. (1998). A Note on a Paper by Glaser and Schöffl. The Fibonacci Quarterly, 36(5), 463-466.
- [2] Breuer, F. (1999). Ducci Sequences Over Abelian Groups. Communications in Algebra, 27(12), 5999-6013.
- [3] Breuer, F. (2010). Ducci Sequences and Cyclotomic Fields. Journal of Difference Equations and Applications, 16(7), 847-862.
- [4] Brown, R. & Merzel, J. (2003). Limiting Behavior in Ducci Sequences. Periodica Mathematica Hungarica, 47(1-2), 45-50.
- [5] Brown, R. & Merzel, J. (2007). The Length of Ducci’s Four Number Game Rocky Mountain Journal of Mathematics, 37(1), 45-65.
- [6] Burmester, M., Forcade, R., & Jacobs, E. (1978) CIrcles of Numbers. Glasgow Mathematical Journal, 19, 115-119.
- [7] Chamberland, M. (2003). Unbounded Ducci Sequences. Journal of Difference Equations and Applications, 9(10), 887-895.
- [8] Ciamberlini, C. & Marengoni, A. (1937). Su una interessante curiosita numerica. Periodiche di Matematiche, 17, 25-30.
- [9] Dular, B. (2020). Cycles of Sums of Integers. Fibonacci Quarterly, 58(2), 126-139.
- [10] Ehrlich, A. (1990). Periods in Ducci’s n n -Number Game of Differences. Fibonacci Quarterly, 28(4), 302-305.
- [11] Freedman, B (1948). The Four Number Game. Scripta Mathematica, 14, 35-47.
- [12] Glaser, H. & Schöffl, G. (1995). Ducci Sequences and Pascal’s Triangle. Fibonacci Quarterly, 33(4), 313-324.
- [13] Fine, N.J. (1947). Binomial Coefficients Modulo a Prime. The American Mathematical Monthly, 54(10.1), 589-592.
- [14] Ludington Furno, A (1981). Cycles of differences of integers. Journal of Number Theory, 13(2), 255-261.
- [15] Miller, R. (1978). A Game with n Numbers. The American Mathematical Monthly, 85(3), 183-185.
- [16] Pompili, F. (1996). Evolution of Finite Sequences of Integers… The Mathematical Gazette, 80(488), 322-332.
- [17] Rothe-Ille, H. [Review of Su una interessante curiosita numerica, by Ciamberlini, C. & Marengoni, A.]. Retrieved from https://zbmath.org/63.0112.08.
- [18] Misiurewicz, M., & Schinzel, A. (1988). On n n Numbers in a Circle. Hardy Ramanujan Journal, 11, 30-39.
- [19] Wong, F.B. (1982). Ducci Processes. The Fibonacci Quarterly, 20(2), 97-105.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:lewis@math.kent.edu
[4]: mailto:stefft@kent.edu
