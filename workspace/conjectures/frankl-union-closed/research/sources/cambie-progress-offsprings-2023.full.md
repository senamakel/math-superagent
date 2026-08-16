<!-- source: https://arxiv.org/html/2306.12351 | converted from HTML -->

Progress on the union-closed conjecture and offsprings in winter 2022-2023

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2306.12351v1 [math.CO] 21 Jun 2023

# Progress on the union-closed conjecture and offsprings in winter 2022-2023

Stijn Cambie Thanks: Extremal Combinatorics and Probability Group (ECOPRO), Institute for Basic Science (IBS), Daejeon, South Korea, supported by the Institute for Basic Science (IBS-R029-C4), E-mail: stijn.cambie@hotmail.com

Mathematicians had little idea whether the easy-to-state union-closed conjecture was true or false even after 40 40 years. However, last winter saw a surge of interest in the conjecture and its variants, initiated by the contribution of a researcher at Google. Justin Gilmer made a significant breakthrough by discovering a first constant lower bound for the proportion of the most common element in a union-closed family.

## 1 Introduction of the Union-Closed conjecture

The union-closed conjecture is due to Peter Frankl 1 1 1 See also https://en.wikipedia.org/wiki/P\%C3\%A9ter_Frankl and https://www.nrc.nl/nieuws/2023/01/20/na-wiskundige-opwinding-op-sociale-media-is-het-probleem-van-de-kleurige-knikkers-bijna-opgelost-2-a4154586., who constructed the elegant statement in 1979 1979 after observing many implications of the statement. Before fully stating it, we need to define crucial concepts from set theory.

The ground set is generally denoted with [n] = { 1, 2, …, n } [n]=\{1,2,\ldots,n\}, where n ∈ ℕ n\in\mathbb{N} is a finite number. A subset A ⊆ [n] A\subseteq[n] is nothing more than a set containing integers between 1 1 and n n, e.g., A = { 2, 4, 6 } ⊂ [7] A=\{2,4,6\}\subset[7].

A family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is a collection of subsets of [n] [n]. Here 2 [n] 2^{[n]} contains all 2 n 2^{n} possible subsets of [n] [n], which includes the empty set ∅ \emptyset as well.

A family ℱ \mathcal{F} is called union-closed if for every A, B ∈ ℱ A,B\in\mathcal{F}, the union A ∪ B A\cup B belongs to ℱ \mathcal{F}. This can be written as ℱ = ℱ ∪ ℱ \mathcal{F}=\mathcal{F}\cup\mathcal{F}, where the latter equals exactly { A ∪ B ∣ A, B ∈ ℱ }. \{A\cup B\mid A,B\in\mathcal{F}\}. An example of such a family is presented in Figure 1. An other example, for every m ∈ ℕ m\in\mathbb{N}, is the family ℱ m = { A ∣ A ⊆ [m] ∨ A = [k] ​ for some ​ m + 1 ≤ k ≤ m 2 } \mathcal{F}_{m}=\{A\mid A\subseteq[m]\vee A=[k]\mbox{ for some }m+1\leq k\leq m^{2}\} which consists of the 2 m 2^{m} subsets of [m] [m], as well as m 2 − m m^{2}-m intervals consisting of the first k k natural numbers.

{ 1, 2 } \{1,2\} { 1, 2, 3 } \{1,2,3\} { 1, 2, 3, 4 } \{1,2,3,4\} { 1, 3 } \{1,3\} { 2 } \{2\} { 1 } \{1\} { 2, 3 } \{2,3\} Figure 1: Example of union-closed family

The Union-closed conjecture can now be formally stated as follows.

###### Conjecture 1 (Union-closed conjecture).

If ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\} is a union-closed family with ground set [n] [n], then there exists an element i ∈ [n] i\in[n] such that at least half of the sets in ℱ \mathcal{F} contain i i.

Considering our previous example ℱ m \mathcal{F}_{m} for large m m, one can verify that it might be that only a small fraction of the elements of the ground set are abundant (belong to at least half of the sets) and their average proportion of sets to which they belong can tend to zero. Note that this conjecture would be (arguably) false when taking an infinite ground set ℕ, \mathbb{N}, e.g. by considering the (union-closed) family of finite subsets of ℕ \mathbb{N}.

This conjecture can also be formulated in many different ways. For example, one can consider bitstrings in { 0, 1 } n \{0,1\}^{n} with the element-wise O ​ R OR -operation. For instance, when n = 4 n=4 and ℱ = { 0011, 1100, 1111 } \mathcal{F}=\{0011,1100,1111\}, we note that 0011 + 1100 = 1111 0011+1100=1111. This family is closed under the O ​ R OR -operation, which corresponds to being union-closed in the initial formulation.

Taking the complements of the set, one obtains the Intersection-closed sets conjecture, which states that an intersection-closed family has an element in its ground set appearing in at most half of the sets. In [3, Sec. 3], one can also find a lattice-, graph-, and Salzborn-formulation.

On November 17, 2022, Justin Gilmer [10], a researcher at Google working in machine learning, made a breakthrough by proving a first constant fraction for Conjecture 1. Soon thereafter, as fast as a few days, his result made others put improvements and related results on the preprint server Arxiv. In this note, we summarize the contributions and progress that was made in the winter of 2022–2023. We explain the main ideas of Gilmer’s approach (Section 2), mention the forthcoming extensions of his method (Sections 3 and 4), as well as an unsuccessful attempt (Section 5) and discuss other work related to the Union-closed conjecture (Section 6).

## 2 The observations and key elements in the proof by Gilmer

A first elementary observation by Gilmer is that one can always prove a statement by proving the contrapositive of that statement. Since the statement of the union-closed conjecture is that simple already, it might be no one considered that before. The contraposition of Conjecture 1 can be stated as follows. If a non-empty family ℱ \mathcal{F} has no element appearing in at least half of the sets of ℱ \mathcal{F}, then ℱ \mathcal{F} is not a union-closed family. By remarking that A ∪ A = A A\cup A=A for every set A A, one knows that ℱ ⊆ ℱ ∪ ℱ, \mathcal{F}\subseteq\mathcal{F}\cup\mathcal{F}, and thus | ℱ ∪ ℱ | > | ℱ | \lvert\mathcal{F}\cup\mathcal{F}\rvert>\lvert\mathcal{F}\rvert whenever ℱ \mathcal{F} is not a union-closed family. While posing related questions and studying counterexamples to variants of Conjecture 1 similar to the ones in [8], Gilmer noted that the entropy of a family might play a role. 2 2 2 More details on his journey/ thought process can be found in https://www.youtube.com/watch?v=AZaP0EwjR_I&t The entropy H ⁡ ( X) H(X) of a discrete random variable X X equals the Shannon entropy of its probability distribution. The latter can be purely presented with a formula. If each possible outcome x x belongs to a (finite) set A A, and has probability p x, p_{x}, then

 | H ( X) = − ∑ x ∈ A p x log 2 p x. H(X)=-\sum_{x\in A}p_{x}\log_{2}p_{x}. |  |

When sampling uniformly at random from ℱ \mathcal{F}, the entropy will equal log 2 ⁡ | ℱ | \log_{2}{\lvert\mathcal{F}\rvert} and no higher entropy is possible. If one can sample from ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F} in such a way that the entropy is larger than log 2 ⁡ | ℱ |, \log_{2}{\lvert\mathcal{F}\rvert}, then one can conclude that | ℱ ∪ ℱ | > | ℱ |. \lvert\mathcal{F}\cup\mathcal{F}\rvert>\lvert\mathcal{F}\rvert. This is exactly the core of Gilmer’s approach.

More precisely, he proved the following statement.

###### Theorem 2.

Let A A and B B denote independent and identically distributed random variables that sample from a common distribution over subsets of [n] [n]. Assume that for all i ∈ [n] i\in[n], ℙ [i ∈ A] ≤ 0.01 \,\mathbb{P}[i\in A]\leq 0.01. Then H ⁡ ( A ∪ B) ≥ 1.26 ​ H ​ ( A) H(A\cup B)\geq 1.26H(A).

As a corollary, by taking the uniform distribution over the subsets of [n] [n], one knows that if ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} is a family for which every element is contained in no more than 1 % 1\% of the sets, then | ℱ ∪ ℱ | ≥ | ℱ | 1.26 \lvert\mathcal{F}\cup\mathcal{F}\rvert\geq\lvert\mathcal{F}\rvert^{1.26}. 3 3 3 As a corollary of later work by Sawin, this is at least | ℱ | 1.74 \lvert\mathcal{F}\rvert^{1.74} This implies that whenever | ℱ | ≥ 2 \lvert\mathcal{F}\rvert\geq 2, either | ℱ ∪ ℱ | > | ℱ | \lvert\mathcal{F}\cup\mathcal{F}\rvert>\lvert\mathcal{F}\rvert (and so the family is not union-closed) or there is an element appearing in at least a 0.01 0.01 fraction of the sets in ℱ. \mathcal{F}. From this, one can conclude that Conjecture 1 is true for a half replaced by 0.01. 0.01.

###### example 3.

Let ℱ = { { 1 }, { 2 } } \mathcal{F}=\{\{1\},\{2\}\} and thus ℱ ∪ ℱ = { { 1 }, { 2 }, { 1, 2 } }. \mathcal{F}\cup\mathcal{F}=\{\{1\},\{2\},\{1,2\}\}. Let A A and B B be i.i.d. random variables that output a set of ℱ \mathcal{F} uniformly at random. Then ℙ ⁡ ( A = { 1 }) = ℙ ⁡ ( A = { 2 }) \,\mathbb{P}(A=\{1\})=\,\mathbb{P}(A=\{2\}) and analogously for B B, which implies

 | ℙ ⁡ ( A ∪ B = { 1 }) = ℙ ⁡ ( A ∪ B = { 2 }) = 1 4 ​ and ​ ℙ ​ ( A ∪ B = { 1, 2 }) = 1 2. \,\mathbb{P}(A\cup B=\{1\})=\,\mathbb{P}(A\cup B=\{2\})=\frac{1}{4}\mbox{ and }\,\mathbb{P}(A\cup B=\{1,2\})=\frac{1}{2}. |  |

Now H ⁡ ( A) = 2 ⋅ 1 2 ​ log 2 ​ 2 = 1 H(A)=2\cdot\frac{1}{2}\log_{2}2=1 and H ⁡ ( A ∪ B) = 2 ⋅ 1 4 ​ log 2 ​ 4 + 1 2 ​ log ⁡ 2 = 3 2 ( < log 2 ⁡ 3). H(A\cup B)=2\cdot\frac{1}{4}\log_{2}4+\frac{1}{2}\log 2=\frac{3}{2}(<\log_{2}3). Since log 2 ⁡ ( 2) < H ⁡ ( A ∪ B), \log_{2}(2)<H(A\cup B), we conclude that it is impossible that A ∪ B A\cup B takes values in a family with only 2 2 elements and thus | ℱ ∪ ℱ | > | ℱ |, \lvert\mathcal{F}\cup\mathcal{F}\rvert>\lvert\mathcal{F}\rvert, i.e. Gilmer’s method verifies that ℱ \mathcal{F} is not union-closed.

###### example 4.

Let ℱ = ( [3] ≤ 2) \mathcal{F}=\binom{[3]}{\leq 2} and thus ℱ ∪ ℱ = 2 [3]. \mathcal{F}\cup\mathcal{F}=2^{[3]}. Note that | ℱ | = 7 \lvert\mathcal{F}\rvert=7 and every 1 ≤ i ≤ 3 1\leq i\leq 3 appears in exactly 3 3 sets and thus in a 3 7 \frac{3}{7} fraction. Let A, B A,B be i.i.d. random variables that output a set of ℱ \mathcal{F} uniformly at random. Then

 | ℙ ⁡ ( A ∪ B = ∅) \displaystyle\,\mathbb{P}(A\cup B=\emptyset) | = 1 49 \displaystyle=\frac{1}{49} |  |

 | ℙ ⁡ ( | A ∪ B | = 1) \displaystyle\,\mathbb{P}(\lvert A\cup B\rvert=1) | = 3 49 \displaystyle=\frac{3}{49} |  |

 | ℙ ⁡ ( | A ∪ B | = 2) \displaystyle\,\mathbb{P}(\lvert A\cup B\rvert=2) | = 9 49 \displaystyle=\frac{9}{49} |  |

 | ℙ ⁡ ( A ∪ B = [3]) \displaystyle\,\mathbb{P}(A\cup B=[3]) | = 12 49 \displaystyle=\frac{12}{49} |  |

Now

 | H ⁡ ( A) = \displaystyle H(A)= | 7 ⁤ 1 7 ​ log 2 ⁡ ( 7) = log 2 ⁡ ( 7) \displaystyle 7\frac{1}{7}\log_{2}(7)=\log_{2}(7) |  |

 | ∼ \displaystyle\sim | 2.81 \displaystyle 2.81 |  |

 | H ⁡ ( A ∪ B) = \displaystyle H(A\cup B)= | 1 49 ​ log 2 ⁡ ( 49) + 3 ⁤ 3 49 ​ log 2 ⁡ ( 49 / 3) \displaystyle\frac{1}{49}\log_{2}(49)+3\frac{3}{49}\log_{2}(49/3) |  |

 |  | + 3 ⁤ 9 49 ​ log 2 ⁡ ( 49 / 9) + 12 49 ​ log 2 ⁡ ( 49 / 12) \displaystyle+3\frac{9}{49}\log_{2}(49/9)+\frac{12}{49}\log_{2}(49/12) |  |

 | ∼ \displaystyle\sim | 2.70 \displaystyle 2.70 |  |

and thus H ⁡ ( A) > H ⁡ ( A ∪ B) H(A)>H(A\cup B). We conclude that this is an example for which Gilmer’s method does not provide evidence that the family is not union-closed, even while the maximum fraction of occurence of an element is 3 7. \frac{3}{7}.

Note: Analogously, when ℱ = ( [5] ≤ 3) \mathcal{F}=\binom{[5]}{\leq 3}, one can verify that H ⁡ ( A) = log 2 ⁡ ( 26) ∼ 4.7 H(A)=\log_{2}(26)\sim 4.7 and H ⁡ ( A ∪ B) ∼ 4.54. H(A\cup B)\sim 4.54. Every element appears in a 11 26 \frac{11}{26} fraction in this case.

## 3 Quick refinement of Gilmer’s idea

The binary entropy function h ⁡ ( p) = − ( p ​ log 2 ​ p + ( 1 − p) ​ log 2 ⁡ ( 1 − p)) h(p)=-(p\log_{2}p+(1-p)\log_{2}(1-p)) plays a role in the computations in the work of Gilmer. Noting that h ⁡ ( p) ≤ h ⁡ ( 2 ​ p − p 2) h(p)\leq h(2p-p^{2}) whenever p ≤ ψ:= 3 − 5 2 p\leq\psi:=\frac{3-\sqrt{5}}{2}, Gilmer claimed that his ideas could be extended to prove a fraction equal to ψ. \psi. The authors of [1, 5, 18, 15] quickly implemented this approach. All four of these papers essentially reduced Conjecture 1 for the constant ψ \psi to the following key lemma, an inequality in one variable.

###### Lemma 5.

Let ϕ = 5 + 1 2 \phi=\frac{\sqrt{5}+1}{2} and 0 ≤ x ≤ 1, 0\leq x\leq 1, then h ⁡ ( x 2) ≥ ϕ ​ x ​ h ​ ( x). h(x^{2})\geq\phi xh(x).

The validity of this lemma was established in two different ways by [1] and Sawin [18]. The former used accurate computer calculations and applied interval arithmetic on three intervals, while the latter utilized a purely calculus-based approach. Thanks to some communication between the authors of [1] and [5], in [5] a reference to the formal proof of [1] was added. In [15] the lemma was split in two parts without formal proof, but both can be verified easily.

A short and more elegant proof for Lemma 5 was given later by Boppana [2], even while the proof itself would originate from 1989 1989. This proof relies on the following extension of the classical Rolle’s theorem, which follows from observations in e.g. [12].

###### Theorem 6.

Let f f be a differentiable function on a interval I I. Let m ⁡ ( f) m(f) be the sum of multiplicities of the roots of f f in I I. Then m ⁡ ( f ′) ≥ m ⁡ ( f) − 1. m(f^{\prime})\geq m(f)-1.

By iterating the theorem three times, one finds m ⁡ ( f) ≤ m ⁡ ( f ′′′) + 3 m(f)\leq m(f^{\prime\prime\prime})+3. Applying this result on the function f ⁡ ( x) = h ⁡ ( x 2) − ϕ ​ x ​ h ​ ( x) f(x)=h(x^{2})-\phi xh(x) and counting the multiplicities of the roots 0, 1 ϕ 0,\frac{1}{\phi} and 1 1 of f f, the conclusion that f f is nonnegative on [0, 1] [0,1] follows quickly. Once Lemma 5 is derived, the proof for Conjecture 1 for constant ψ \psi (instead of 0.5 0.5) is rather short in each of the papers [1, 5, 15, 18], indicated e.g. by the total length of the paper by Chase and Lovett [5]. Their work has three steps. First, they extended the analytic claim (Lemma 5) to the two-variate function f ⁡ ( x, y):= h ⁡ ( x ​ y) h ⁡ ( x) ​ y + h ⁡ ( y) ​ x f(x,y):=\frac{h(xy)}{h(x)y+h(y)x}. Next they prove a strengthened inequality between the entropy of A ∪ B A\cup B and the one of A A and B B, for random variables A A and B B (not necessarily identical) on { 0, 1 } n \{0,1\}^{n} for which every bit is 1 1 with a bounded probability. Finally, they finish the proof of their slightly more general statement that holds for approximate union-closed families. The latter being families for which the union of two random drawn sets belong to the family with a high probability.

One example which certifies the sharpness of their proof can be derived from ℱ 1 + ℱ 2 = { A ∣ A ∈ ℱ 1 ∨ A ∈ ℱ 2 } \mathcal{F}_{1}+\mathcal{F}_{2}=\{A\mid A\in\mathcal{F}_{1}\vee A\in\mathcal{F}_{2}\} where ℱ 1 = ( [n] ψ ​ n + n 2 / 3) \mathcal{F}_{1}=\binom{[n]}{\psi n+n^{2/3}} and ℱ 2 = ( [n] ≥ ( 1 − ψ) ​ n) \mathcal{F}_{2}=\binom{[n]}{\geq(1-\psi)n}. For this, one need to note that | ℱ 1 | >> | ℱ 2 | \lvert\mathcal{F}_{1}\rvert>>\lvert\mathcal{F}_{2}\rvert and that the union of two (iid uniform sampled) random sets from ℱ 1 \mathcal{F}_{1} belongs with very high probability to ℱ 2. \mathcal{F}_{2}. The expected size of the union is slightly larger (with an additional term of the order n 2 / 3 n^{2/3}, i.e. Θ ⁡ ( n 2 / 3) \Theta(n^{2/3})) than n − ( 1 − ψ) 2 ​ n = ( 1 − ψ) ​ n n-(1-\psi)^{2}n=(1-\psi)n, and since the variance on the size is O ⁡ ( n 1 / 2) O(n^{1/2}), the union almost surely belongs to ℱ 2 \mathcal{F}_{2} as well. The conclusion is still valid when replacing the term n 2 / 3 n^{2/3} by any function g ⁡ ( n) g(n) for which n >> g ⁡ ( n) >> n 1 / 2. n>>g(n)>>n^{1/2}.

ℱ 1 \mathcal{F}_{1} ℱ 2 \mathcal{F}_{2} Figure 2: An approximate union-closed family whose elements appear in at most a ψ + o ⁡ ( 1) \psi+o(1) fraction.

In a different direction, in his paper, Gilmer included some ideas for a full resolution of Conjecture 1, but some of these directions were immediately proven not to hold by Sawin and Ellis [18, 7].

## 4 Further refinements and extensions related to Gilmer’s work

Sawin [18] gave a suggestion to improve the bound further, which given the sharpness of the form for union-closed families may be considered surprising. Hereby the essence is in a question purely stated in terms of probability distributions. His suggestion was worked out by Yu [20] and Cambie [4]. Yu [20] considered the approach in a slightly more general form initially and made a lower bound computable by restricting to the suggestion of Sawin and applying [1, Lem. 5] and the Krein-Milman theorem [13] to bound the support (number of values with nonzero probability) of a joint distribution by 4 4. A numerical computation then yield a bound equal to (roughly) 0.38234. 0.38234. In parallel, Cambie [4] found an upper bound for Sawin’s approach which indicates that the improvement is way smaller than expected and one would hope for. The construction is a discrete probability distribution with only two values having nonzero probability, with the values determined by a system of equations involving the entropy function. Additionally he proved that this value is sharp, by first reducing the support to 3 3 elements, where one of the elements equals 1. 1. Finally, the conclusion is derived from the combination of 3 3 -dimensional plots, a numerical minimization problem and a more precise solution for the case where the support has exactly two elements, one of which equals 1 1.

Finally, building upon the work of [5], Yuster [21] considered families that are almost k k -union-closed, meaning that the union of k k independent uniform random sets from ℱ \mathcal{F} belongs to ℱ \mathcal{F} with high probability. He conjectured a tight version for the minimum frequency (the proportion of sets containing the element) of some element in such families, with the threshold for this frequency being the unique real root in [0, 1] [0,1] of ( 1 − x) k = x (1-x)^{k}=x, denoted by ψ k \psi_{k}. To understand the sharpness of his conjecture and the intuition behind the choice of ψ k \psi_{k}, consider the union of ℱ 1 = ( [n] ψ k ​ n + ​ n 2 / 3) \mathcal{F}_{1}=\binom{[n]}{\psi_{k}n^{+}n^{2/3}} and ℱ 2 = ( [n] ≥ ( 1 − ψ k) ​ n) \mathcal{F}_{2}=\binom{[n]}{\geq(1-\psi_{k})n}. If at least one set from ℱ 2 \mathcal{F}_{2} is included among the k k sets drawn, the union is guaranteed to belong to ℱ 2 \mathcal{F}_{2}. If all k k sets belong to ℱ 1 \mathcal{F}_{1}, the expected size of the union is n − ( 1 − ψ k) k ​ n + Θ ⁡ ( n 2 / 3) n-(1-\psi_{k})^{k}n+\Theta(n^{2/3}), and since the variance is O ⁡ ( n 1 / 2) O(n^{1/2}), the union almost surely belongs to ℱ 2 \mathcal{F}_{2} as well. The conjecture is proven to be true for k ≤ 4 k\leq 4, while for larger values of k k a weaker bound is established.

## 5 The final Eureka moment, not yet

When Scandone [19] uploaded a preprint claiming the full resolution of the union-closed conjecture, there arose initially excitement. However, upon closer examination it became clear that Scandone’s proposed solution had several issues, including a significant flaw that requires revising the underlying construction. This was communicated to Scandone by Terence Tao, and the details of this issue are briefly explained later in this section.

Nevertheless, Scandone’s underlying idea holds potential and is worth mentioning for the valuable intuition it provides for Gilmer’s approach. Let ℱ \mathcal{F} be a family which is not union-closed, so ℱ ∪ ℱ ≠ ℱ \mathcal{F}\cup\mathcal{F}\not=\mathcal{F}. A random variable taking values in ℱ \mathcal{F} has entropy at most log 2 ⁡ | ℱ | \log_{2}\lvert\mathcal{F}\rvert and equality occurs only for uniform sampling from ℱ. \mathcal{F}. By considering various examples, e.g. ℱ = { { 1 }, { 2 } } \mathcal{F}=\{\{1\},\{2\}\}, the reader can verify that there is no strategy to choose two random variables A, B A,B which sample sets from ℱ \mathcal{F}, such that A ∪ B A\cup B samples uniformly random from ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F}. On the other hand, if for every set A ∈ ℱ A\in\mathcal{F} the probability of obtaining it is almost equal to the original probability and a few other sets from ( ℱ ∪ ℱ) \ ℱ (\mathcal{F}\cup\mathcal{F})\backslash\mathcal{F} happen with a small probability, the entropy can increase. The reason for this is that the derivative of h h (plotted in Figure 3) is a continuously decreasing function on the interval ( 0, 1) (0,1), with h ′ ​ ( 0) = + ∞ h^{\prime}(0)=+\infty. To provide a more explicit explanation of Scandone’s idea, we describe his proposed construction in detail.

Let A, B A,B be independent random variables that take any set of ℱ \mathcal{F} uniformly at random. Define a 𝒫 ⁡ ( [n]) \mathcal{P}([n]) -valued random variable A δ A^{\delta} (depending on δ \delta) through the relation

 | Pr [A δ = X] = ( 1 − δ) Pr [A = X] + δ Pr [A ∪ B = X] for every X ⊆ [n]. \operatorname{Pr}[A^{\delta}=X]=(1-\delta)\operatorname{Pr}[A=X]+\delta\operatorname{Pr}[A\cup B=X]\mbox{ for every }X\subseteq[n]. |  |

For every X ∈ ℱ X\in\mathcal{F}, Pr [A δ = X] ≥ ( 1 − δ) Pr [A = X] \operatorname{Pr}[A^{\delta}=X]\geq(1-\delta)\operatorname{Pr}[A=X] and thus for δ \delta sufficiently small, we have h ( Pr [A δ = X]) − h ( Pr [A = X]) ≳ δ / | ℱ | h ′ ( 1 / | ℱ |). h(\operatorname{Pr}[A^{\delta}=X])-h(\operatorname{Pr}[A=X])\gtrsim\delta/\lvert\mathcal{F}\rvert h^{\prime}(1/\lvert\mathcal{F}\rvert). 4 4 4 To be precise, we assume | ℱ | ≥ 3 \lvert\mathcal{F}\rvert\geq 3 and 2 | ℱ | + δ < 1. \frac{2}{\lvert\mathcal{F}\rvert}+\delta<1. On the other hand, for X ∈ ( ℱ ∪ ℱ) \ ℱ X\in(\mathcal{F}\cup\mathcal{F})\backslash\mathcal{F}, let the probability p:= Pr [A ∪ B = X] p:=\operatorname{Pr}[A\cup B=X]. We have that h ⁡ ( δ ​ p) ∼ − δ ​ p ​ ( log ⁡ δ + log ⁡ p − 1) h(\delta p)\sim-\delta p(\log\delta+\log p-1). By choosing δ \delta to be sufficiently small such that − log ⁡ δ -\log\delta is much greater than 1 p ​ h ′ ​ ( 1 / | ℱ |) \frac{1}{p}h^{\prime}(1/\lvert\mathcal{F}\rvert), we can ensure that H ⁡ ( A δ) > H ⁡ ( A) H(A^{\delta})>H(A) holds.

0.2 0.2 0.4 0.4 0.6 0.6 0.8 0.8 1 1 0.5 0.5 1 1 x x h ⁡ ( x) h(x) Figure 3: Plot of the binary entropy function h h

Equivalently, the variable A δ A^{\delta} can be obtained by considering, in addition to A A and B B, a Bernoulli random variable of parameter δ \delta, Z δ Z_{\delta}, which determines whether we take A ∪ B A\cup B or only A A. The flaw in the argument is that, in the process of revealing all the digits of A δ A^{\delta} (computed using the chain rule for the entropy), the indeterminacy provided by Z δ Z_{\delta} (and the consequent improvement of the bounds) is lost after the first step. More precisely, there is step in the computations in which a conditional probability distribution has been erroneously replaced by its expected value, and this produces the aforementioned flaw in the argument. The comment of Tao can be rephrased as follows, “the idea of modifying the union operation by Gilmer is promising, but a single global bit Z δ Z_{\delta} is not sufficient to do the job, and a more involved construction is needed”.

## 6 A better understanding by progress in a different direction

In this final section, we conclude with the essence of a recent paper and two preprints on the union-closed conjecture, which consider different aspects and angles of attack on Conjecture 1.

While Frankl’s conjecture is about the existence of one abundant element (element that appears in at least half of the sets) in the family, it is also natural to wonder if there are more abundant elements, assuming that all sets in the family are sufficiently large. The following conjecture by Cui and Hu [6] would imply Conjecture 1.

###### Conjecture 7.

If ℱ \mathcal{F} is a finite union-closed family of sets whose smallest set is of size at least 2 2, then there are at least two elements such that each belong to more than half of the sets of ℱ \mathcal{F}.

At the end of 2022 2022, the three authors of [11] considered this different direction and proved that Conjecture [6] is not true when replacing 2 2 by a larger integer. They proved (among other results) that there are families all of whose sets have size at least k k, where k k can be arbitrary large, which do only have 2 2 abundant elements. The main construction is the family 𝒫 4 12 \mathcal{P}^{12}_{4}. The family 𝒫 4 12 \mathcal{P}^{12}_{4} consists of all subsets S S of { 0, 1, …, 11 } \{0,1,\dots,11\} of size at least 4 4 such that either { 0, 1 } ⊂ S \{0,1\}\subset S, or 0 ∈ S 0\in S and S ⊆ { 0, 2, …, 10 } S\subseteq\{0,2,\dots,10\}, or 1 ∈ S 1\in S and S ⊆ { 1, 3, …, 11 } S\subseteq\{1,3,\dots,11\}. The reader can verify that | 𝒫 4 12 | = ( 2 10 − 11) + 2 ⋅ 16 = 1045 \lvert\mathcal{P}^{12}_{4}\rvert=(2^{10}-11)+2\cdot 16=1045, while every element 2 ≤ i ≤ 11 2\leq i\leq 11 only appears 2 9 − 1 + 11 = 522 2^{9}-1+11=522 times. One way to increase the size of sets in families with non-abundant elements is to duplicate an element within the sets. However, this creates blocks of size at least 2 2. A block is defined by Poonen [16] as a maximum set of elements that all belong to the exact same sets of a family. Poonen also noted that to prove Conjecture 1, it is sufficient to focus on families for which no block is a singleton. Due to this, it is interesting to note that the construction of the family 𝒫 4 12 \mathcal{P}^{12}_{4} in [11] can be extended to such families.Let k ≥ 3 k\geq 3 be a fixed integer and let n n be a sufficiently large even integer as a function of k k ( n ≥ 10 ​ k n\geq 10k works). Let E n = { i ∈ [n] ∣ i ≡ 0 ( mod 2) } E_{n}=\{i\in[n]\mid i\equiv 0\pmod{2}\} and O n = { i ∈ [n] ∣ i ≡ 1 ( mod 2) } O_{n}=\{i\in[n]\mid i\equiv 1\pmod{2}\} be the set of even and odd integers in [n] [n] respectively. Consider the family 𝒫 k n \mathcal{P}^{n}_{k} consisting of subsets S S of [n] [n] of size at least k k, such that either

- •

{ 1, 2 } ⊂ S \{1,2\}\subset S,

- •

S ⊂ E n S\subset E_{n} and 2 ∈ S 2\in S, or

- •

S ⊂ O n S\subset O_{n} and 1 ∈ S 1\in S.

It is clear that 1 1 and 2 2 are abundant elements. Now the other elements appear all equally often (by symmetry) and by a small bijection and counting argument, we conclude that these elements are not abundant whenever

 | ( n − 3 k − 3) < 2 ​ ( n / 2 − 2 ≥ k − 1). \binom{n-3}{k-3}<2\binom{n/2-2}{\geq k-1}. |  |

Since this is the case for n n sufficiently large, the conclusion is clear.

Another result related with union-closed families and the smallest set size, was published early 2023 2023. Ellis, Ivan and Leader [9] proved that for every k ∈ ℕ k\in\mathbb{N}, there exists a union-closed family in which the (unique) smallest set has size k k, but where each element of this set has frequency ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k. (1+o(1))\frac{\log k}{2k}. As such, proving that focusing on the smallest set cannot work in the strongest possible sense. They also proposed the problem of verifying the union-closed conjecture for a family for which they were unable to verify the statement. The latter was verified by Pulaj and Wood [17]. They also proved new bounds on the least number m m (given k k and n n) such that every union-closed family ℱ \mathcal{F} containing any 𝒜 ⊆ ( [n] k) \mathcal{A}\subseteq\binom{[n]}{k} with | 𝒜 | = m \lvert\mathcal{A}\rvert=m as a subfamily, satisfies Conjecture 1.

We can conclude that despite the progress that originates from the breakthrough of Justin Gilmer, the exact version of Conjecture 1 is still not proven. Mathematicians are still thinking about other directions or modifications of the strategy and hope to resolve Conjecture 1 in the future. Taking into account that the improvement by taking combinations suggested by Sawin [18] turned out to be tinier than expected and hoped for, as illustrated by the example in [4], it seems that the focus should go towards essential new ideas. In particular, the union-closed conjecture might be a distraction of a more general behaviour that | ℱ ∪ ℱ | > | ℱ | c \lvert\mathcal{F}\cup\mathcal{F}\rvert>\lvert\mathcal{F}\rvert^{c} for some c ⁡ ( ε) > 1 c(\varepsilon)>1 when every element of [n] [n] appears in less than a 1 2 − ε \frac{1}{2}-\varepsilon fraction of the sets in ℱ. \mathcal{F}. 5 5 5 communicated by Zachary Chase

Note added: In June 2023, Liu [14] improved the constant slightly with a different method of coupling.

## Acknowledgements

We thank Zachary Chase, Justin Gilmer, Raffaele Scandone and Lei Yu for internal communication while writing this manuscript.

## References

- [1] R. Alweiss, B. Huang, and M. Sellke. Improved Lower Bound for the Union-Closed Sets Conjecture. arXiv e-prints, page arXiv:2211.11731, Nov. 2022.
- [2] R. B. Boppana. A Useful Inequality for the Binary Entropy Function. arXiv e-prints, page arXiv:2301.09664, Jan. 2023.
- [3] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture. Graphs Combin., 31(6):2043–2074, 2015.
- [4] S. Cambie. Better bounds for the union-closed sets conjecture using the entropy approach. arXiv e-prints, page arXiv:2212.12500, Dec. 2022.
- [5] Z. Chase and S. Lovett. Approximate union closed conjecture. arXiv e-prints, page arXiv:2211.11689, Nov. 2022.
- [6] Z. Cui and Z. Hu. Two stronger versions of the union-closed sets conjecture. Adv. Math. (China), 50(6):829–851, 2021.
- [7] D. Ellis. Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture. arXiv e-prints, page arXiv:2211.12401, Nov. 2022.
- [8] D. Ellis. Union-closed families with small average overlap densities. Electron. J. Combin., 29(1):Paper No. 1.11, 5, 2022.
- [9] D. Ellis, I. Leader, and M.-R. Ivan. Small Sets in Union-Closed Families. Electron. J. Combin., 30(1):Paper No. 1.8–, 2023.
- [10] J. Gilmer. A constant lower bound for the union-closed sets conjecture. arXiv e-prints, page arXiv:2211.09055, Nov. 2022.
- [11] A. Kabela, M. Polák, and J. Teska. The number of abundant elements in union-closed families without small sets. arXiv e-prints, page arXiv:2212.09279, Dec. 2022.
- [12] V. P. Kostov. On arrangements of real roots of a real polynomial and its derivatives. Serdica Math. J., 29(1):65–74, 2003.
- [13] M. Krein and D. Milman. On extreme points of regular convex sets. Studia Math., 9:133–138, 1940.
- [14] J. Liu. Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling. arXiv e-prints, page arXiv:2306.08824, June 2023.
- [15] L. Pebody. Extension of a Method of Gilmer. arXiv e-prints, page arXiv:2211.13139, Nov. 2022.
- [16] B. Poonen. Union-closed families. J. Combin. Theory Ser. A, 59(2):253–268, 1992.
- [17] J. Pulaj and K. Wood. Local Configurations in Union-Closed Families. arXiv e-prints, page arXiv:2301.01331, Jan. 2023.
- [18] W. Sawin. An improved lower bound for the union-closed set conjecture. arXiv e-prints, page arXiv:2211.11504, Nov. 2022.
- [19] R. Scandone. A proof of the union-closed sets conjecture. arXiv e-prints, page arXiv:2302.03484, Feb. 2023.
- [20] L. Yu. Dimension-Free Bounds for the Union-Closed Sets Conjecture. arXiv e-prints, page arXiv:2212.00658, Dec. 2022.
- [21] R. Yuster. Almost k k -union closed set systems. arXiv e-prints, page arXiv:2302.12276, Feb. 2023.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
