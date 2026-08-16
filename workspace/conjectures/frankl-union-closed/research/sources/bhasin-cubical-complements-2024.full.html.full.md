<!-- source: https://arxiv.org/html/2409.17050 | converted from HTML -->

A Cubical Perspective on Complements of Union-Closed Families of Sets

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2409.17050v1 [math.CO] 25 Sep 2024

# A Cubical Perspective on Complements of Union-Closed Families of Sets

Dhruv Bhasin Thanks: Department of Mathematics, Indian Institute of Science Education and Research, Pune
Email id: bhasin.dhruv@students.iiserpune.ac.in

###### Abstract

Complements of union-closed families of sets, over a finite ground set, are known as simply rooted families of sets. Cubical sets are widely studied topological objects having applications in computational homology. In this paper, we look at simply rooted families of sets from the perspective of cubical sets. That is, for every family ℱ \mathcal{F} of subsets of a finite set, we construct a natural cubical set X ⁡ ( ℱ) X(\mathcal{F}) (corresponding to it). We show that for every simply rooted family ℱ \mathcal{F}, containing the empty set, the cubical set X ⁡ ( ℱ) X(\mathcal{F}) is always acyclic (that is, it has trivial reduced cubical homology). As a consequence of this, using the Euler-Poincarè formula, we obtain a formula satisfied by all simply rooted families of sets which contain the empty set. We also provide an elementary proof of this formula.

## 1 Introduction

Intersection-closed structures are ubiquitous in all of mathematics. Collections of all subgroups of a group, subspaces of a vector space, subrings of a ring, independents sets of a graph are closed under intersections and the list goes on. In combinatorics, the dual concept of intersection-closed families of sets, namely union-closed families of sets is very widely studied. Most of this study is driven by the quest of solving the famous union-closed sets conjecture due to Frankl (see [11]). Let [n] = { 1, …, n } [n]=\{1,\dots,n\} and let 2 [n] 2^{[n]} denote its power set. A family of sets ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is said to be union-closed if for every A, B ∈ ℱ A,B\in\mathcal{F}, we have A ∪ B ∈ ℱ A\cup B\in\mathcal{F}. Frankl’s union-closed sets conjecture states that:

###### Conjecture 1.1.

(see [11]) Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a union-closed family of sets such that ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}. Then, there is an element i ∈ [n] i\in[n] such that i i is in at least half of the member sets of ℱ \mathcal{F}.

Conjecture 1.1 has been studied in various contexts. It has formulations in the languages of Lattice Theory ( [21]) and Graph Theory ( [4]). For a survey of the union-closed sets conjecture, we refer the reader to [5]. Recently, information theory based methods were used (in [12]) for proving the first constant lower bound for Conjecture 1.1. That is, in [12], the author showed that for every union-closed family of sets with at least two elements, there is an element in at least 1 % 1\% of the member sets of the family. Subsequently his ideas were improved to show that there is an element in at least 38.24 % 38.24\% many member sets of the family (see [1], [6], [7], [20], [22], [25]).

The relation between union-closed families of sets and simply rooted families was first made by Balla, Bollobás, Eccles (see [2]). In this paper, the authors investigated Conjecture 1.1 for large union-closed families of sets. That is, they showed that Conjecture 1.1 is true for all union-closed families of sets 𝒢 ⊆ 2 [n] \mathcal{G}\subseteq 2^{[n]} satisfying | 𝒢 | ≥ 2 3 ​ 2 n |\mathcal{G}|\geq\frac{2}{3}2^{n}. The authors then introduced and investigated simply rooted families for a slight strengthening of their result. In [10], the author further investigated simply rooted families to show that Conjecture 1.1 holds for union-closed families 𝒢 ⊆ 2 [n] \mathcal{G}\subseteq 2^{[n]} satisfying | 𝒢 | ≥ ( 2 3 − 1 104) ​ 2 n |\mathcal{G}|\geq(\frac{2}{3}-\frac{1}{104})2^{n}. In [19], the author studied simply rooted families using tools from Boolean analysis to show that there is a constant c > 0 c>0 such that Conjecture 1.1 holds for all union-closed families satisfying | ℱ | ≥ ( 1 2 − c) ​ 2 n |\mathcal{F}|\geq(\frac{1}{2}-c)2^{n}. In [23], the author showed that the equivalent version of Conjecture 1.1 for simply rooted families holds asymptotically.

Informally speaking, cubical sets are defined to be those subsets of the n n -dimensional euclidean space which are created by putting together cubes (of dimension at most n n) having vertices in the lattice ℤ n \mathbb{Z}^{n}. Cubical sets have been widely studied in various contexts and both from the theoretical and practical point of view (see for example: [3], [8], [9], [13], [15], [16], [17], [24]). In this paper, for every family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, we define a natural cubical set corresponding to it, denoted X ⁡ ( ℱ) ⊆ ℝ n X(\mathcal{F})\subseteq\mathbb{R}^{n}, which is formed by geometrically putting together the ‘cubes’ contained in ℱ \mathcal{F}. (For a formal definition, we refer the reader to Definition 2.6). To the best of our knowledge, the cubical set X ⁡ ( ℱ) X(\mathcal{F}) has not been studied in the literature.

We ask the question: what is the homology of X ⁡ ( ℱ) X(\mathcal{F}) when ℱ \mathcal{F} is simply rooted? Our main result is:

###### Theorem 1.1.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply rooted family of sets such that ∅ ∈ ℱ \emptyset\in\mathcal{F}. Then, X ⁡ ( ℱ) X(\mathcal{F}) is acyclic.

Using Theorem 1.1, and the Euler-Poincarè formula, we obtain

###### Corollary 1.2.

Let ℱ \mathcal{F} be a simply rooted family of sets such that ∅ ∈ ℱ \emptyset\in\mathcal{F}. Let 𝒞 k ( ℱ) = { [A, B]: A ⊆ B, [A, B] ⊆ ℱ, | B ∖ A | = k } \mathcal{C}_{k}(\mathcal{F})=\{[A,B]:A\subseteq B,[A,B]\subseteq\mathcal{F},|B\setminus A|=k\} where [A, B] = { C ∈ 2 [n]: A ⊆ C ⊆ B } [A,B]=\{C\in 2^{[n]}:A\subseteq C\subseteq B\}. Then,

 | ∑ k = 0 n ( − 1) k ​ | 𝒞 k ​ ( ℱ) | = 1. \sum_{k=0}^{n}(-1)^{k}|\mathcal{C}_{k}(\mathcal{F})|=1. |  | (1) |

We provide an elementary proof of Corollary 1.2 in Section 2.2 using Lemma 2.16. As depicted by Lemma 2.16, Equation 1, is the sum of 2 n 2^{n} equations each corresponding to a set A ∈ 2 [n] A\in 2^{[n]}.

While our results do not improve upon Conjecture 1.1, in this paper, we give a topological insight regarding simply rooted families of sets. Informally speaking, Theorem 1.1 says that simply rooted families, containing the empty set, are ‘simple in nature’ from the point of view of homology. We hope that studying simply rooted families further with this perspective will lead to more insights regarding them and in turn, regarding union-closed families of sets.

In Section 2.1, we define the basic terminology required for this work. In particular, we give the definition of the specific cubical set X ⁡ ( ℱ) X(\mathcal{F}) under consideration. We also give examples showing that one can not drop either assumption in Theorem 1.1. At the end of this section, we give the idea of our proof of Theorem 1.1. In Section 2.2, we prove some properties of simply-rooted families of sets needed for the proof of Theorem 1.1. Using these properties, we give an elementary proof of Corollary 1.2. In Section 2.3, we prove some preliminary Lemmas involving cubical sets needed for the proof of Theorem 1.1. In this section, we show that the cubical set we associate to a given family of sets behaves well with intersections of families of sets (Lemma 2.19). We also show that a particular class of cubical sets is always acyclic (Lemma 2.20), which will be needed for the proof of Theorem 1.1. Finally, in Section 3, we prove Theorem 1.1.

## 2 Cubical setting

### 2.1 Basic notions

Let [n] = { 1, …, n } [n]=\{1,\dots,n\} and 2 [n] 2^{[n]} be its power set. For A, B ∈ 2 [n] A,B\in 2^{[n]}, we denote [A, B] = { C ∈ 2 [n]: A ⊆ C ⊆ B } [A,B]=\{C\in 2^{[n]}:A\subseteq C\subseteq B\}. When A = { i } A=\{i\}, we use the shorter notation [i, B] [i,B] to mean [{ i }, B] [\{i\},B]. A family of sets ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is said to be union-closed if for every A, B ∈ ℱ, A ∪ B ∈ ℱ A,B\in\mathcal{F},A\cup B\in\mathcal{F}.

###### Definition 2.1.

(see [2]) A family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is said to be simply rooted if for every non-empty A ∈ ℱ A\in\mathcal{F}, there is an i ∈ A i\in A such that [i, A] ⊆ 2 [n] [i,A]\subseteq 2^{[n]}.

The following result relates union-closed families and simply rooted families of sets.

###### Proposition 2.2.

(see [2]) Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a family of sets. Then ℱ \mathcal{F} is union-closed if and only if 2 [n] ∖ ℱ 2^{[n]}\setminus\mathcal{F} is simply rooted.

In this paper, we will deal with simply rooted families of sets. Following [17], we define:

###### Definition 2.3.

(see [17]) A set A ⊆ ℝ n A\subseteq\mathbb{R}^{n} is called an elementary cube if A = I 1 × ⋯ × I n A=I_{1}\times\dots\times I_{n} where each I i = [a, b] I_{i}=[a,b] such that a, b ∈ ℤ a,b\in\mathbb{Z} and b − a ∈ { 0, 1 } b-a\in\{0,1\}. A set X ⊆ ℝ n X\subseteq\mathbb{R}^{n} is said to be a cubical set if it is the union of a finitely many elementary cubes.

###### Definition 2.4.

Given a family of sets ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, we define 𝒞 ⁡ ( ℱ) = { [A, B] ⊆ 2 [n]: [A, B] ⊆ ℱ } \mathcal{C}(\mathcal{F})=\{[A,B]\subseteq 2^{[n]}:[A,B]\subseteq\mathcal{F}\} to be the set of cubes of ℱ \mathcal{F}. We define 𝒞 k ​ ( ℱ) = { [A, B] ∈ 𝒞 ⁡ ( ℱ): | B ∖ A | = k } \mathcal{C}_{k}(\mathcal{F})=\{[A,B]\in\mathcal{C}(\mathcal{F}):|B\setminus A|=k\}.

###### Definition 2.5.

For a cube [A, B] ⊆ 2 [n] [A,B]\subseteq 2^{[n]}, with A ⊆ B A\subseteq B, we define I 1 × ⋯ × I n ⊆ ℝ n I_{1}\times\dots\times I_{n}\subseteq\mathbb{R}^{n} to be the geometric realization of [A, B] [A,B] where I i = { { 1 } ​ if ​ i ∈ A [0, 1] ​ if ​ i ∈ B ∖ A { 0 } ​ if ​ i ∈ B c I_{i}=\begin{cases}\{1\}\text{ if }i\in A\\ [0,1]\text{ if }i\in B\setminus A\\ \{0\}\text{ if }i\in B^{c}\end{cases}. We denote it by | [A, B] | |[A,B]|. If A ⊈ B A\nsubseteq B, we define its geometric realization to be the empty subspace of ℝ n \mathbb{R}^{n}.

###### Definition 2.6.

For a family of sets ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, we define the geometric realization of ℱ \mathcal{F} to be the cubical set

 | X ⁡ ( ℱ) = ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ) | [A, B] | ⊆ ℝ n. X(\mathcal{F})=\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F})}|[A,B]|\subseteq\mathbb{R}^{n}. |  |

[image: Refer to caption] (a) X ⁡ ( ℱ 1) X(\mathcal{F}_{1}).

[image: Refer to caption] (b) X ⁡ ( ℱ 2) X(\mathcal{F}_{2}).

[image: Refer to caption] (c) X ⁡ ( ℱ 3) X(\mathcal{F}_{3}).

Figure 1: This figure depicts X ⁡ ( ℱ) X(\mathcal{F}) for various families of sets ℱ \mathcal{F}.

###### Definition 2.7.

(see [17]) A cubical set X ⊆ ℝ n X\subseteq\mathbb{R}^{n} is said to be acyclic if

1. 1.

X X is non-empty and connected,

2. 2.

H i ​ ( X) H_{i}(X) is trivial for every i ≥ 1 i\geq 1, where H i ​ ( X) H_{i}(X) is i th i^{\text{th}} cubical homology group of X X.

###### Example 2.8.

In Figure 1, we demonstrate X ⁡ ( ℱ) X(\mathcal{F}) for various families of sets ℱ ⊆ 2 [3] \mathcal{F}\subseteq 2^{[3]}:

1. 1.

In Figure 1(a), we have ℱ 1 = { ∅, { 1 }, { 2 }, { 1, 3 }, { 2, 3 }, { 1, 2, 3 } } \mathcal{F}_{1}=\{\emptyset,\{1\},\{2\},\{1,3\},\{2,3\},\{1,2,3\}\} which is not a simply rooted family of sets. Note that X ⁡ ( ℱ 1) X(\mathcal{F}_{1}) is homeomorphic to the circle S 1 S^{1} in this case. This shows that the simply rooted condition is needed in Theorem 1.1.

2. 2.

In Figure 1(b), we have ℱ 2 = { { 1 }, { 2 }, { 3 }, { 1, 2 }, { 1, 3 }, { 2, 3 } } \mathcal{F}_{2}=\{\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\}\} which is a simply rooted family of sets. Note that in this case as well, X ⁡ ( ℱ 2) X(\mathcal{F}_{2}) is homeomorphic to S 1 S^{1}. This shows that the condition ∅ ∈ ℱ \emptyset\in\mathcal{F} is necessary in Theorem 1.1.

3. 3.

In Figure 1(c), we have ℱ 3 = { ∅, { 1 }, { 2 }, { 3 }, { 1, 3 } } \mathcal{F}_{3}=\{\emptyset,\{1\},\{2\},\{3\},\{1,3\}\} which is a simply rooted family of sets and satisfies ∅ ∈ ℱ 3 \emptyset\in\mathcal{F}_{3}. We note that X ⁡ ( ℱ 3) X(\mathcal{F}_{3}) is acyclic in this case.

We will use the following results from [17].

###### Theorem 2.9.

(see [17]) Assume X, Y ⊆ ℝ n X,Y\subseteq\mathbb{R}^{n} are cubical sets. If X, Y X,Y and X ∩ Y X\cap Y are acyclic, then X ∪ Y X\cup Y is acyclic.

###### Definition 2.10.

(see [17]) A cubical set X ⊆ ℝ n X\subseteq\mathbb{R}^{n} is star-shaped with respect to a point x ∈ ℝ n x\in\mathbb{R}^{n} if X X is the union of a finite number of elementary cubes each of which contains x x.

###### Proposition 2.11.

(see [17]) Every star-shaped set is acylic.

Theorem 2.9 is the main tool we use for the proof of Theorem 1.1. Our idea of proving Theorem 1.1 is: given a simply rooted family containing the empty set, say ℱ \mathcal{F}, and a set A ∈ ℱ A\in\mathcal{F} of maximum cardinality amongst the members of ℱ \mathcal{F}, we write X ⁡ ( ℱ) = X ⁡ ( ℱ ∖ { A }) ∪ X ⁡ ( ℱ A) X(\mathcal{F})=X(\mathcal{F}\setminus\{A\})\cup X(\mathcal{F}_{A}) (where ℱ A \mathcal{F}_{A} is defined in Definition 2.14). We assume that X ⁡ ( ℱ ∖ { A }) X(\mathcal{F}\setminus\{A\}) is acyclic by the induction hypothesis. We show that X ⁡ ( ℱ A) X(\mathcal{F}_{A}) is star-shaped and hence it is acyclic using Proposition 2.11. We show that the intersection of these two cubical sets is one among the class of cubical sets we show are acyclic in Lemma 2.20. Then, we are done using Theorem 2.9.

### 2.2 Some Properties of Simply-Rooted Families of Sets

In this section, we explore some properties of simply rooted families of sets. Using these properties, we give an elementary proof of Corollary 1.2. Using Corollary 1.2, we also give the Euler-characteristic of X ⁡ ( ℱ) X(\mathcal{F}) where ℱ \mathcal{F} is a simply rooted family of sets such that ∅ ∉ ℱ \emptyset\notin\mathcal{F}. We note here that among the results of this section, we will only need Proposition 2.15 for the proof of Theorem 1.1.

###### Definition 2.12.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply rooted family of sets. We define ϕ: ℱ → ( 2 [n] ∖ ℱ ∪ { ∅ }) \phi:\mathcal{F}\rightarrow(2^{[n]}\setminus\mathcal{F}\cup\{\emptyset\}) by

 | ϕ: A ↦ ⋃ B ∈ ( 2 [n] ∖ ℱ) ∩ [∅, A] B. \phi:A\mapsto\bigcup_{B\in(2^{[n]}\setminus\mathcal{F})\cap[\emptyset,A]}B. |  |

We note that ϕ \phi is well-defined because 2 [n] ∖ ℱ 2^{[n]}\setminus\mathcal{F} is union-closed.

###### Proposition 2.13.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply rooted family of sets. Let A ∈ ℱ A\in\mathcal{F} be a non-empty set. Then,

 | { i ∈ A: [i, A] ⊆ ℱ } = A ∖ ϕ ⁡ ( A). \{i\in A:[i,A]\subseteq\mathcal{F}\}=A\setminus\phi(A). |  |

###### Proof.

Let [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F}. Let B ∈ ( 2 [n] ∖ ℱ) ∩ [∅, A] B\in(2^{[n]}\setminus\mathcal{F})\cap[\emptyset,A]. Since [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F}, we see that i ∉ B i\notin B. Thus, we have i ∉ ϕ ⁡ ( A) i\notin\phi(A) and consequently, i ∈ A ∖ ϕ ⁡ ( A) i\in A\setminus\phi(A). We conclude that { i ∈ A: [i, A] ⊆ ℱ } ⊆ A ∖ ϕ ⁡ ( A) \{i\in A:[i,A]\subseteq\mathcal{F}\}\subseteq A\setminus\phi(A).

On the other hand, suppose that i ∈ A ∖ ϕ ⁡ ( A) i\in A\setminus\phi(A). Let B ∈ [i, A] B\in[i,A]. Suppose that B ∈ 2 [n] ∖ ℱ B\in 2^{[n]}\setminus\mathcal{F}. This means that B ⊆ ϕ ⁡ ( A) B\subseteq\phi(A) and hence, i ∈ ϕ ⁡ ( A) i\in\phi(A). This leads to a contradiction. Consequently, we obtain that B ∈ ℱ B\in\mathcal{F}. This allows us to conclude that { i ∈ A: [i, A] ⊆ ℱ } ⊇ A ∖ ϕ ⁡ ( A) \{i\in A:[i,A]\subseteq\mathcal{F}\}\supseteq A\setminus\phi(A). This completes the proof. ∎

###### Definition 2.14.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a family of sets. Let A ∈ ℱ A\in\mathcal{F}. We define ℱ A = { B ∈ ℱ: [B, A] ⊆ ℱ } \mathcal{F}_{A}=\{B\in\mathcal{F}:[B,A]\subseteq\mathcal{F}\}.

###### Proposition 2.15.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply rooted family of sets such that ϕ ∈ ℱ \phi\in\mathcal{F}. Let A ∈ ℱ A\in\mathcal{F} such that ϕ ⁡ ( A) ≠ ∅ \phi(A)\neq\emptyset. Then,

 | ℱ A = ⋃ [i, A] ⊆ ℱ [i, A]. \mathcal{F}_{A}=\bigcup_{[i,A]\subseteq\mathcal{F}}[i,A]. |  |

###### Proof.

It is obvious that ⋃ [i, A] ⊆ ℱ [i, A] ⊆ ℱ A \bigcup_{[i,A]\subseteq\mathcal{F}}[i,A]\subseteq\mathcal{F}_{A}. On the other hand, let C ∈ ℱ A C\in\mathcal{F}_{A}, that is, [C, A] ⊆ ℱ [C,A]\subseteq\mathcal{F}. We need to show that there is a j ∈ { i ∈ A: [i, A] ⊆ ℱ } j\in\{i\in A:[i,A]\subseteq\mathcal{F}\} such that j ∈ C j\in C. Suppose that, on the contrary, there is no such j j. By Proposition 2.13, this means that C ⊆ ϕ ⁡ ( A) C\subseteq\phi(A). Since, [C, A] ⊆ ℱ [C,A]\subseteq\mathcal{F}, we obtain that ϕ ⁡ ( A) ∈ ℱ \phi(A)\in\mathcal{F}, which is a contradiction. Thus, we obtain that ℱ A ⊆ ⋃ [i, A] ⊆ ℱ [i, A] \mathcal{F}_{A}\subseteq\bigcup_{[i,A]\subseteq\mathcal{F}}[i,A], as required. ∎

###### Lemma 2.16.

Let ℱ \mathcal{F} be a simply rooted family of sets such that ∅ ∈ ℱ \emptyset\in\mathcal{F}. Let A ∈ ℱ A\in\mathcal{F} be non-empty. Let 𝒞 k ​ ( ℱ, A) = { [C, D] ∈ 𝒞 k ​ ( ℱ): D = A } \mathcal{C}_{k}(\mathcal{F},A)=\{[C,D]\in\mathcal{C}_{k}(\mathcal{F}):D=A\}. Then, we have,

 | ∑ k = 0 | A | ( − 1) k ​ | 𝒞 k ​ ( ℱ, A) | = 0. \sum_{k=0}^{|A|}(-1)^{k}|\mathcal{C}_{k}(\mathcal{F},A)|=0. |  | (2) |

###### Proof.

We note that, by definition, the set 𝒞 k ​ ( ℱ, A) \mathcal{C}_{k}(\mathcal{F},A) is bijective to the set { B ∈ ℱ A: | B | = | A | − k } \{B\in\mathcal{F}_{A}:|B|=|A|-k\}. By Proposition 2.15 and Proposition 2.13, { B ∈ ℱ A: | B | = | A | − k } \{B\in\mathcal{F}_{A}:|B|=|A|-k\} consists all the subsets of A A, of size | A | − k |A|-k, that contain at least one element from A ∖ ϕ ⁡ ( A) A\setminus\phi(A). The number of such subsets is ( | A | | A | − k) − ( | ϕ ⁡ ( A) | | A | − k) \binom{|A|}{|A|-k}-\binom{|\phi(A)|}{|A|-k}. Consequently, we obtain:

 | ∑ k = 0 | A | ( − 1) k ​ | 𝒞 k ​ ( ℱ, A) | \displaystyle\sum_{k=0}^{|A|}(-1)^{k}|\mathcal{C}_{k}(\mathcal{F},A)| | = ∑ k = 0 | A | ( − 1) k ​ { ( | A | | A | − k) − ( | ϕ ⁡ ( A) | | A | − k) } \displaystyle=\sum_{k=0}^{|A|}(-1)^{k}\left\{\binom{|A|}{|A|-k}-\binom{|\phi(A)|}{|A|-k}\right\} |  |

 |  | = ∑ k = 0 | A | ( − 1) k ​ ( | A | | A | − k) − ∑ k = 0 | A | ( − 1) k ​ ( | ϕ ⁡ ( A) | | A | − k) \displaystyle=\sum_{k=0}^{|A|}(-1)^{k}\binom{|A|}{|A|-k}-\sum_{k=0}^{|A|}(-1)^{k}\binom{|\phi(A)|}{|A|-k} |  |

 |  | = ∑ k = 0 | A | ( − 1) k ​ ( | A | k) − ∑ t = 0 | ϕ ⁡ ( A) | ( − 1) t ​ ( | ϕ ⁡ ( A) | t) \displaystyle=\sum_{k=0}^{|A|}(-1)^{k}\binom{|A|}{k}-\sum_{t=0}^{|\phi(A)|}(-1)^{t}\binom{|\phi(A)|}{t} |  |

 |  | = 0. \displaystyle=0. |  |

∎

Proof of Corollary 1.2. Using Lemma 2.16, Corollary 1.2 follows by adding Equation 2 for every non-empty A ∈ 2 [n] A\in 2^{[n]} and adding 1 1 on both sides (corresponding to the empty set). □ \square

###### Corollary 2.17.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a non-empty simply rooted family of sets such that ∅ ∉ ℱ \emptyset\notin\mathcal{F}. For k ≥ 1 k\geq 1, let c k c_{k} be the number of sets A A of ℱ \mathcal{F}, of size k k, such that for every i ∈ A i\in A, [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F} and let c 0 = 1 c_{0}=1. Then, the Euler-characteristic of X ⁡ ( ℱ) X(\mathcal{F}) is given by

 | 1 − ∑ k = 0 n ( − 1) k ​ c k. 1-\sum_{k=0}^{n}(-1)^{k}c_{k}. |  |

###### Proof.

The result follows by using Corollary 1.2 on ℱ ∪ { ∅ } \mathcal{F}\cup\{\emptyset\} and noting that 𝒞 k ( ℱ) ⊆ 𝒞 k ( ℱ ∪ { ∅)) \mathcal{C}_{k}(\mathcal{F})\subseteq\mathcal{C}_{k}(\mathcal{F}\cup\{\emptyset)) and that 𝒞 k ( ℱ ∪ { ∅ }) ∖ 𝒞 k ( ℱ) = { A ∈ ℱ: | A | = k, [ϕ, A] ⊆ ℱ ∪ { ∅ } } \mathcal{C}_{k}(\mathcal{F}\cup\{\emptyset\})\setminus\mathcal{C}_{k}(\mathcal{F})=\{A\in\mathcal{F}:|A|=k,[\phi,A]\subseteq\mathcal{F}\cup\{\emptyset\}\}. ∎

### 2.3 Preliminary Lemmas

In this subsection we prove some preliminary results needed for the proof of Theorem 1.1.

###### Proposition 2.18.

Let ℱ, 𝒢 ⊆ 2 [n] \mathcal{F},\mathcal{G}\subseteq 2^{[n]} be family of sets. Then 𝒞 ⁡ ( ℱ) ∩ 𝒞 ⁡ ( 𝒢) = 𝒞 ⁡ ( ℱ ∩ 𝒢) \mathcal{C}(\mathcal{F})\cap\mathcal{C}(\mathcal{G})=\mathcal{C}(\mathcal{F}\cap\mathcal{G}).

###### Proof.

We note that

 | [A, B] ∈ 𝒞 ⁡ ( ℱ) ∩ 𝒞 ⁡ ( 𝒢) \displaystyle[A,B]\in\mathcal{C}(\mathcal{F})\cap\mathcal{C}(\mathcal{G}) | ⇔ [A, B] ⊆ ℱ ​ and ​ [A, B] ⊆ 𝒢 \displaystyle\Leftrightarrow[A,B]\subseteq\mathcal{F}\text{ and }[A,B]\subseteq\mathcal{G} |  |

 |  | ⇔ [A, B] ⊆ ℱ ∩ 𝒢 \displaystyle\Leftrightarrow[A,B]\subseteq\mathcal{F}\cap\mathcal{G} |  |

 |  | ⇔ [A, B] ∈ 𝒞 ⁡ ( ℱ ∩ 𝒢). \displaystyle\Leftrightarrow[A,B]\in\mathcal{C}(\mathcal{F}\cap\mathcal{G}). |  |

∎

The following lemma shows that geometric realization of families of sets behaves well with taking finite intersections.

###### Lemma 2.19.

Let ℱ, 𝒢 ⊆ 2 [n] \mathcal{F},\mathcal{G}\subseteq 2^{[n]} be family of sets. Then, X ⁡ ( ℱ) ∩ X ⁡ ( 𝒢) = X ⁡ ( ℱ ∩ 𝒢) X(\mathcal{F})\cap X(\mathcal{G})=X(\mathcal{F}\cap\mathcal{G}).

###### Proof.

We begin with [A, B], [C, D] ⊆ 2 [n] [A,B],[C,D]\subseteq 2^{[n]}. We note that [A, B] ∩ [C, D] = [A ∪ C, B ∩ D] [A,B]\cap[C,D]=[A\cup C,B\cap D]. This is because A ⊆ E ⊆ B A\subseteq E\subseteq B and C ⊆ E ⊆ D ⇔ A ∪ C ⊆ E ⊆ B ∩ D C\subseteq E\subseteq D\Leftrightarrow A\cup C\subseteq E\subseteq B\cap D. We first show that

 | | [A, B] | ∩ | [C, D] | = | [A ∪ C, B ∩ D] |. |[A,B]|\cap|[C,D]|=|[A\cup C,B\cap D]|. |  |

As in Definition 2.5, we let | [A, B] | = I 1 × ⋯ × I n ⊆ ℝ n |[A,B]|=I_{1}\times\dots\times I_{n}\subseteq\mathbb{R}^{n} and | [C, D] | = J 1 × ⋯ × J n ⊆ ℝ n |[C,D]|=J_{1}\times\dots\times J_{n}\subseteq\mathbb{R}^{n}. This means that

 | | [A, B] | ∩ | [C, D] | = ( I 1 ∩ J 1) × ⋯ × ( I n ∩ J n). |[A,B]|\cap|[C,D]|=(I_{1}\cap J_{1})\times\dots\times(I_{n}\cap J_{n}). |  |

We note that if i ∈ A ∖ D i\in A\setminus D then I i = { 1 } I_{i}=\{1\} and J i = { 0 } J_{i}=\{0\} by construction. This readily yields | [A, B] | ∩ | [C, D] | = | [A ∪ C, B ∩ D] | = ∅ |[A,B]|\cap|[C,D]|=|[A\cup C,B\cap D]|=\emptyset. On the other hand we assume that A ⊆ D A\subseteq D and C ⊆ B C\subseteq B (by symmetry).

Therefore, we have

 | I i ∩ J i = { 1 } \displaystyle I_{i}\cap J_{i}=\{1\} | ⇔ ( I i = { 1 } ​ and ​ J i = [0, 1]) ​ or ​ ( I i = [0, 1] ​ and ​ J i = { 1 }) \displaystyle\Leftrightarrow(I_{i}=\{1\}\text{ and }J_{i}=[0,1])\text{ or }(I_{i}=[0,1]\text{ and }J_{i}=\{1\}) |  |

 |  | or ​ ( I i = { 1 } ​ and ​ J i = { 1 }) \displaystyle\hskip 14.22636pt\text{ or }(I_{i}=\{1\}\text{ and }J_{i}=\{1\}) |  |

 |  | ⇔ i ∈ ( A ∩ D ∩ C c) ∪ ( B ∩ A c ∩ C) ∪ ( A ∩ C) \displaystyle\Leftrightarrow i\in(A\cap D\cap C^{c})\cup(B\cap A^{c}\cap C)\cup(A\cap C) |  |

 |  | ⇔ i ∈ ( A ∖ C) ∪ ( C ∖ A) ∪ ( A ∩ C) \displaystyle\Leftrightarrow i\in(A\setminus C)\cup(C\setminus A)\cup(A\cap C) |  |

 |  | ⇔ i ∈ A ∪ C. \displaystyle\Leftrightarrow i\in A\cup C. |  |

We also have

 | I i ∩ J i = { 0 } \displaystyle I_{i}\cap J_{i}=\{0\} | ⇔ ( I i = { 0 } ​ and ​ J i = [0, 1]) ​ or ​ ( I i = [0, 1] ​ and ​ J i = { 0 }) \displaystyle\Leftrightarrow(I_{i}=\{0\}\text{ and }J_{i}=[0,1])\text{ or }(I_{i}=[0,1]\text{ and }J_{i}=\{0\}) |  |

 |  | or ​ ( I i = { 0 } ​ and ​ J i = { 0 }) \displaystyle\hskip 14.22636pt\text{ or }(I_{i}=\{0\}\text{ and }J_{i}=\{0\}) |  |

 |  | ⇔ i ∈ ( B c ∩ D ∩ C c) ∪ ( B ∩ A c ∩ D c) ∪ ( B c ∩ D c) \displaystyle\Leftrightarrow i\in(B^{c}\cap D\cap C^{c})\cup(B\cap A^{c}\cap D^{c})\cup(B^{c}\cap D^{c}) |  |

 |  | ⇔ i ∈ ( D ∩ B c) ∪ ( B ∩ D c) ∪ ( B c ∩ D c) \displaystyle\Leftrightarrow i\in(D\cap B^{c})\cup(B\cap D^{c})\cup(B^{c}\cap D^{c}) |  |

 |  | ⇔ i ∈ ( B ∩ D) c. \displaystyle\Leftrightarrow i\in(B\cap D)^{c}. |  |

Finally, we have

 | I i ∩ J i = [0, 1] \displaystyle I_{i}\cap J_{i}=[0,1] | ⇔ ( I i = [0, 1]) ​ and ​ ( J i = [0, 1]) \displaystyle\Leftrightarrow(I_{i}=[0,1])\text{ and }(J_{i}=[0,1]) |  |

 |  | ⇔ i ∈ B ∩ A c ∩ D ∩ C c \displaystyle\Leftrightarrow i\in B\cap A^{c}\cap D\cap C^{c} |  |

 |  | ⇔ i ∈ B ∩ D ∖ ( A ∪ C). \displaystyle\Leftrightarrow i\in B\cap D\setminus(A\cup C). |  |

This means that ( I 1 ∩ J 1) × ⋯ × ( I n ∩ J n) = | [A ∪ C, B ∩ D] | (I_{1}\cap J_{1})\times\dots\times(I_{n}\cap J_{n})=|[A\cup C,B\cap D]| as required. We now come back to proving our original claim. Let ℱ, 𝒢 ⊆ 2 [n] \mathcal{F},\mathcal{G}\subseteq 2^{[n]} be family of sets. We have

 | X ⁡ ( ℱ) ∩ X ⁡ ( 𝒢) \displaystyle X(\mathcal{F})\cap X(\mathcal{G}) | = ( ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ) | [A, B] |) ∩ ( ⋃ [C, D] ∈ 𝒞 ⁡ ( 𝒢) | [C, D] |) \displaystyle=(\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F})}|[A,B]|)\cap(\bigcup_{[C,D]\in\mathcal{C}(\mathcal{G})}|[C,D]|) |  |

 |  | = ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ), [C, D] ∈ 𝒞 ⁡ ( 𝒢) | [A, B] | ∩ | [C, D] | \displaystyle=\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F}),[C,D]\in\mathcal{C}(\mathcal{G})}|[A,B]|\cap|[C,D]| |  |

 |  | = ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ), [C, D] ∈ 𝒞 ⁡ ( 𝒢) | [A ∪ C, B ∩ D] | \displaystyle=\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F}),[C,D]\in\mathcal{C}(\mathcal{G})}|[A\cup C,B\cap D]| |  | (3) |

 |  | ⊇ ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ) ∩ 𝒞 ⁡ ( 𝒢) | [A, B] | \displaystyle\supseteq\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F})\cap\mathcal{C}(\mathcal{G})}|[A,B]| |  |

 |  | = ⋃ [A, B] ∈ 𝒞 ⁡ ( ℱ ∩ 𝒢) | [A, B] | ( Using Proposition 2.18) \displaystyle=\bigcup_{[A,B]\in\mathcal{C}(\mathcal{F}\cap\mathcal{G})}|[A,B]|\hskip 76.82243pt(\text{Using Proposition\penalty\ \ref{prop:cubes-commute-intersection}}) |  |

 |  | = X ⁡ ( ℱ ∩ 𝒢). \displaystyle=X(\mathcal{F}\cap\mathcal{G}). |  |

On the other hand, we note that given [A, B] ∈ 𝒞 ⁡ ( ℱ) [A,B]\in\mathcal{C}(\mathcal{F}) and [C, D] ∈ 𝒞 ⁡ ( 𝒢) [C,D]\in\mathcal{C}(\mathcal{G}), we have [A ∪ C, B ∩ D] ∈ 𝒞 ⁡ ( ℱ ∩ 𝒢) [A\cup C,B\cap D]\in\mathcal{C}(\mathcal{F}\cap\mathcal{G}). This is because, [A, B] ⊆ ℱ ⇒ [A ∪ C, B ∩ D] ⊆ ℱ [A,B]\subseteq\mathcal{F}\Rightarrow[A\cup C,B\cap D]\subseteq\mathcal{F} and [C, D] ⊆ 𝒢 ⇒ [A ∪ C, B ∩ D] ⊆ 𝒢 [C,D]\subseteq\mathcal{G}\Rightarrow[A\cup C,B\cap D]\subseteq\mathcal{G}. Using Equation 3, we conclude that X ⁡ ( ℱ ∩ 𝒢) ⊆ X ⁡ ( ℱ ∩ 𝒢) X(\mathcal{F}\cap\mathcal{G})\subseteq X(\mathcal{F}\cap\mathcal{G}). This completes the proof. ∎

The following Lemma tells that a specific type of cubical sets are always acylic. We will encounter these cubical sets in the proof of Theorem 1.1.

###### Lemma 2.20.

Let n ≥ 2 n\geq 2 and k ≥ 1 k\geq 1 be integers such that k < n k<n. Then,

 | ⋃ i = 1 k ⋃ j ≠ i | [i, [n] ∖ { j }] | \bigcup_{i=1}^{k}\bigcup_{j\neq i}|[i,[n]\setminus\{j\}]| |  |

is acyclic.

###### Proof.

We prove this result by induction on n n. First of all, we note that for n = 2 n=2, we only need to check for the case when k = 1 k=1. The corresponding set is | { 1 } | |\{1\}| which is clearly acyclic. Suppose that the result is true for all n ≤ t n\leq t for some t ≥ 2 t\geq 2. Let n = t + 1 n=t+1. We now perform induction on k k. Note that if k = 1 k=1 then the corresponding cubical set is ⋃ j ≠ 1 | [1, [t + 1] ∖ { j }] | \bigcup_{j\neq 1}|[1,[t+1]\setminus\{j\}]|. This is a star-shaped cubical set and hence it is acyclic by using Proposition 2.11.

Suppose that the result is true for every k ≤ r k\leq r for some r r satisfying 1 ≤ r < t 1\leq r<t. Let us now consider k = r + 1 k=r+1. We have

 | ⋃ i = 1 r + 1 ⋃ j ≠ i | [i, [t + 1] ∖ { j }] | \displaystyle\bigcup_{i=1}^{r+1}\bigcup_{j\neq i}|[i,[t+1]\setminus\{j\}]| | = ( ⋃ i = 1 r ⋃ j ≠ i | [i, [t + 1] ∖ { j }] |) ∪ ⋃ j ≠ r + 1 | [r + 1, [t + 1] ∖ { j }] | \displaystyle=\bigg(\bigcup_{i=1}^{r}\bigcup_{j\neq i}|[i,[t+1]\setminus\{j\}]|\bigg)\cup\bigcup_{j\neq r+1}|[r+1,[t+1]\setminus\{j\}]| |  |

 |  | = X 1 ∪ X 2 \displaystyle=X_{1}\cup X_{2} |  |

where we put X 1 = ⋃ i = 1 t ⋃ j ≠ i | [i, [t + 1] ∖ { j }] | X_{1}=\bigcup_{i=1}^{t}\bigcup_{j\neq i}|[i,[t+1]\setminus\{j\}]| and X 2 = ⋃ j ≠ r + 1 | [r + 1, [t + 1] ∖ { j }] | X_{2}=\bigcup_{j\neq r+1}|[r+1,[t+1]\setminus\{j\}]|. We note that X 1 X_{1} is acyclic by the induction hypothesis. Since X 2 X_{2} is star-shaped, using Proposition 2.11, we conclude that X 2 X_{2} is acyclic. It is easy to see that X 1 = X ⁡ ( 𝒢) X_{1}=X(\mathcal{G}) where 𝒢 = { A ⊊ [t + 1]: A ∩ [r] ≠ ∅ } \mathcal{G}=\{A\subsetneq[t+1]:A\cap[r]\neq\emptyset\} and X 2 = X ⁡ ( ℋ) X_{2}=X(\mathcal{H}) where ℋ = { A ⊊ [t + 1]: r + 1 ∈ A } \mathcal{H}=\{A\subsetneq[t+1]:r+1\in A\}. This means that X 1 ∩ X 2 = X ⁡ ( 𝒢) ∩ X ⁡ ( ℋ) = X ⁡ ( 𝒢 ∩ ℋ) X_{1}\cap X_{2}=X(\mathcal{G})\cap X(\mathcal{H})=X(\mathcal{G}\cap\mathcal{H}) (using Lemma 2.19).

Now, we note that

 | 𝒢 ∩ ℋ = { A ⊊ [t + 1]: r + 1 ∈ A, A ∩ [r] ≠ ∅ }. \mathcal{G}\cap\mathcal{H}=\{A\subsetneq[t+1]:r+1\in A,A\cap[r]\neq\emptyset\}. |  |

Let 𝒦 = { A ⊊ [t]: A ∩ [r] ≠ ∅ } \mathcal{K}=\{A\subsetneq[t]:A\cap[r]\neq\emptyset\}. Clearly, X ⁡ ( 𝒢 ∩ ℋ) X(\mathcal{G}\cap\mathcal{H}) is homeomorphic to X ⁡ ( 𝒦) X(\mathcal{K}). We note that X ⁡ ( 𝒦) X(\mathcal{K}) is acyclic by the induction hypothesis. Hence, X ⁡ ( 𝒢 ∩ ℋ) X(\mathcal{G}\cap\mathcal{H}) is acyclic. Using Theorem 2.9, we see that X 1 ∪ X 2 = ⋃ i = 1 r + 1 ⋃ j ≠ i | [i, [t + 1] ∖ { j }] | X_{1}\cup X_{2}=\bigcup_{i=1}^{r+1}\bigcup_{j\neq i}|[i,[t+1]\setminus\{j\}]| is acylic. This completes the proof. ∎

We now come to our main result:

## 3 Proof of Theorem 1.1

We proceed by induction on n n. For n = 1 n=1, the only families are { ∅ } \{\emptyset\} and { ∅, { 1 } } \{\emptyset,\{1\}\}. The result is clearly true for these families. Suppose that the result is true for all n ≤ t n\leq t. Let n = t + 1 n=t+1. We now perform induction on m ⁡ ( ℱ) = max B ∈ ℱ ⁡ | B | m(\mathcal{F})=\max_{B\in\mathcal{F}}|B| where ℱ ⊆ 2 [t + 1] \mathcal{F}\subseteq 2^{[t+1]} is a simply rooted family of sets such that ∅ ∈ ℱ \emptyset\in\mathcal{F}. The result is easily seen to be true for all such ℱ \mathcal{F} satisfying m ⁡ ( ℱ) ≤ 1 m(\mathcal{F})\leq 1. Suppose that the result is true for all such ℱ \mathcal{F} satisfying m ⁡ ( ℱ) ≤ r m(\mathcal{F})\leq r for some r ≥ 1 r\geq 1. Let ℱ ⊆ 2 [t + 1] \mathcal{F}\subseteq 2^{[t+1]} be such a family with m ⁡ ( ℱ) = r + 1 m(\mathcal{F})=r+1. Let A A be a set of maximum size in ℱ \mathcal{F}. Since m ⁡ ( ℱ) = r + 1 m(\mathcal{F})=r+1, we note that | A | ≥ 2 |A|\geq 2. As in Definition 2.14, let ℱ A = { B ∈ ℱ: [B, A] ⊆ ℱ } \mathcal{F}_{A}=\{B\in\mathcal{F}:[B,A]\subseteq\mathcal{F}\}. First of all, if ℱ = ℱ A \mathcal{F}=\mathcal{F}_{A} then we are done since in this case, ∅ ∈ ℱ A \emptyset\in\mathcal{F}_{A} and consequently ℱ A \mathcal{F}_{A} is an elementary cube and hence it is acyclic using Proposition 2.11. So, we assume that ℱ ≠ ℱ A \mathcal{F}\neq\mathcal{F}_{A}. We note that ℱ = ( ℱ ∖ { A }) ∪ ℱ A \mathcal{F}=(\mathcal{F}\setminus\{A\})\cup\mathcal{F}_{A}. We also note that 𝒞 ⁡ ( ℱ) = 𝒞 ⁡ ( ℱ ∖ { A }) ∪ 𝒞 ⁡ ( ℱ A) \mathcal{C}(\mathcal{F})=\mathcal{C}(\mathcal{F}\setminus\{A\})\cup\mathcal{C}(\mathcal{F}_{A}). To see this, we begin with [C, D] ∈ 𝒞 ⁡ ( ℱ) [C,D]\in\mathcal{C}(\mathcal{F}). If D = A D=A then [C, D] ∈ 𝒞 ⁡ ( ℱ A) [C,D]\in\mathcal{C}(\mathcal{F}_{A}). On the other hand, if D ≠ A D\neq A, we have [C, D] ∈ 𝒞 ⁡ ( ℱ ∖ { A }) [C,D]\in\mathcal{C}(\mathcal{F}\setminus\{A\}) (because A A is of maximum cardinality). This allows us to conclude that 𝒞 ⁡ ( ℱ) ⊆ 𝒞 ⁡ ( ℱ ∖ { A }) ∪ 𝒞 ⁡ ( ℱ A) \mathcal{C}(\mathcal{F})\subseteq\mathcal{C}(\mathcal{F}\setminus\{A\})\cup\mathcal{C}(\mathcal{F}_{A}). On the other hand, 𝒞 ⁡ ( ℱ) ⊇ 𝒞 ⁡ ( ℱ ∖ { A }) ∪ 𝒞 ⁡ ( ℱ A) \mathcal{C}(\mathcal{F})\supseteq\mathcal{C}(\mathcal{F}\setminus\{A\})\cup\mathcal{C}(\mathcal{F}_{A}) is obviously true. This shows that 𝒞 ⁡ ( ℱ) = 𝒞 ⁡ ( ℱ ∖ { A }) ∪ 𝒞 ⁡ ( ℱ A) \mathcal{C}(\mathcal{F})=\mathcal{C}(\mathcal{F}\setminus\{A\})\cup\mathcal{C}(\mathcal{F}_{A}). Now,

 | X ⁡ ( ℱ ∖ { A }) ∪ X ⁡ ( ℱ A) \displaystyle X(\mathcal{F}\setminus\{A\})\cup X(\mathcal{F}_{A}) | = ( ⋃ [C, D] ∈ 𝒞 ⁡ ( ℱ ∖ { A } CLOSE | [C, D] |) ∪ ( ⋃ [C, D] ∈ 𝒞 ⁡ ( ℱ A) | [C, D] |) \displaystyle=\bigg(\bigcup_{[C,D]\in\mathcal{C}(\mathcal{F}\setminus\{A\}}|[C,D]|\bigg)\cup\bigg(\bigcup_{[C,D]\in\mathcal{C}(\mathcal{F}_{A})}|[C,D]|\bigg) |  |

 |  | = ⋃ [C, D] ∈ 𝒞 ⁡ ( ℱ ∖ { A }) ∪ 𝒞 ⁡ ( ℱ A) | [C, D] | \displaystyle=\bigcup_{[C,D]\in\mathcal{C}(\mathcal{F}\setminus\{A\})\cup\mathcal{C}(\mathcal{F}_{A})}|[C,D]| |  |

 |  | = ⋃ [C, D] ∈ 𝒞 ⁡ ( ℱ) | [C, D] | \displaystyle=\bigcup_{[C,D]\in\mathcal{C}(\mathcal{F})}|[C,D]| |  |

 |  | = X ⁡ ( ℱ). \displaystyle=X(\mathcal{F}). |  |

This shows that X ⁡ ( ℱ) = X ⁡ ( ℱ ∖ { A }) ∪ X ⁡ ( ℱ A) X(\mathcal{F})=X(\mathcal{F}\setminus\{A\})\cup X(\mathcal{F}_{A}). Now, we know that X ⁡ ( ℱ ∖ { A }) X(\mathcal{F}\setminus\{A\}) is acyclic by the induction hypothesis. Using Proposition 2.15, we have that ℱ A = ⋃ [i, A] ⊆ ℱ [i, A] \mathcal{F}_{A}=\bigcup_{[i,A]\subseteq\mathcal{F}}[i,A]. We note that { [i, A] ⊆ ℱ A } \{[i,A]\subseteq\mathcal{F}_{A}\} forms a maximal set of cubes of ℱ A \mathcal{F}_{A}. To see this, note that if [C, D] ⊆ ℱ [C,D]\subseteq\mathcal{F} then, since C ∈ ℱ A C\in\mathcal{F}_{A} there is an i ∈ A i\in A such that [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F} and C ∈ [i, A] C\in[i,A]. Since, D ⊆ A D\subseteq A, we obtain that [C, D] ⊆ [i, A] [C,D]\subseteq[i,A]. Thus, we obtain that X ⁡ ( ℱ A) = ⋃ [i, A] ⊆ ℱ | [i, A] | X(\mathcal{F}_{A})=\bigcup_{[i,A]\subseteq\mathcal{F}}|[i,A]| and hence, it is star-shaped. Using Proposition 2.11, we obtain that it is acyclic. Now, X ⁡ ( ℱ ∖ { A }) ∩ X ⁡ ( ℱ A) = X ⁡ ( ( ℱ ∖ { A }) ∩ ℱ A) = X ⁡ ( ℱ A ∖ { A }) X(\mathcal{F}\setminus\{A\})\cap X(\mathcal{F}_{A})=X((\mathcal{F}\setminus\{A\})\cap\mathcal{F}_{A})=X(\mathcal{F}_{A}\setminus\{A\}) using Lemma 2.19. Since | A | ≥ 2 |A|\geq 2, there exists an i i such that [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F} and hence, ℱ A ∖ { A } ≠ ∅ \mathcal{F}_{A}\setminus\{A\}\neq\emptyset. This shows that X ⁡ ( ℱ A ∖ { A }) ≠ ∅. X(\mathcal{F}_{A}\setminus\{A\})\neq\emptyset. Thus, if we can show that X ⁡ ( ℱ A ∖ { A }) X(\mathcal{F}_{A}\setminus\{A\}) is acyclic then we will be done using Theorem 2.9. We consider the following two cases:

Case 1: Suppose that for every i ∈ A i\in A, we have that [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F}. Since ∅ ∈ ℱ \emptyset\in\mathcal{F}, this clearly means that [∅, A] ∈ ℱ [\emptyset,A]\in\mathcal{F}. In this case X ⁡ ( ℱ ∖ { A }) = ⋃ i ∈ A | [∅, A ∖ { i }] | X(\mathcal{F}\setminus\{A\})=\bigcup_{i\in A}|[\emptyset,A\setminus\{i\}]| which is a star-shaped set and hence acyclic using Proposition 2.11.

Case 2: Suppose that there is an i ∈ A i\in A such that [i, A] ⊈ ℱ [i,A]\nsubseteq\mathcal{F}. Using ℱ A = ⋃ [i, A] ⊆ ℱ [i, A] \mathcal{F}_{A}=\bigcup_{[i,A]\subseteq\mathcal{F}}[i,A], we obtain that ℱ A ∖ { A } = ⋃ [i, A] ⊆ ℱ ⋃ j ≠ i, j ∈ A [i, A ∖ { j }] \mathcal{F}_{A}\setminus\{A\}=\bigcup_{[i,A]\subseteq\mathcal{F}}\bigcup_{j\neq i,j\in A}[i,A\setminus\{j\}]. Since, { [i, A ∖ { j }]: [i, A] ⊆ ℱ, j ∈ A, i ≠ j } \{[i,A\setminus\{j\}]:[i,A]\subseteq\mathcal{F},j\in A,i\neq j\} forms a maximal set of cubes of ℱ A ∖ { A } \mathcal{F}_{A}\setminus\{A\}, we obtain that X ⁡ ( ℱ A ∖ { A }) = ⋃ [i, A] ⊆ ℱ ⋃ j ≠ i, j ∈ A | [i, A ∖ { j }] | X(\mathcal{F}_{A}\setminus\{A\})=\bigcup_{[i,A]\subseteq\mathcal{F}}\bigcup_{j\neq i,j\in A}|[i,A\setminus\{j\}]|. Since, | { i ∈ A: [i, A] ⊆ ℱ } | < | A | |\{i\in A:[i,A]\subseteq\mathcal{F}\}|<|A|, using Lemma 2.20, it follows that X ⁡ ( ℱ A ∖ { A }) X(\mathcal{F}_{A}\setminus\{A\}) is acyclic.

This completes the proof.

## References

- [1] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for frankl’s union-closed sets conjecture. arXiv preprint arXiv:2211.11731, 2022.
- [2] Igor Balla, Béla Bollobás, and Tom Eccles. Union-closed families of sets. Journal of Combinatorial Theory, Series A, 120(3):531–544, 2013.
- [3] Hélène Barcelo, Curtis Greene, Abdul Salam Jarrah, and Volkmar Welker. Homology groups of cubical sets with connections. Applied Categorical Structures, 29:415–429, 2021.
- [4] Henning Bruhn, Pierre Charbit, Oliver Schaudt, and Jan Arne Telle. The graph formulation of the union-closed sets conjecture. European Journal of Combinatorics, 43:210–219, 2015.
- [5] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets conjecture. Graphs and Combinatorics, 31:2043–2074, 2015.
- [6] Stijn Cambie. Better bounds for the union-closed sets conjecture using the entropy approach. arXiv preprint arXiv:2212.12500, 2022.
- [7] Zachary Chase and Shachar Lovett. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689, 2022.
- [8] Seungho Choe and Sheela Ramanna. Cubical homology-based machine learning: An application in image classification. Axioms, 11(3):112, 2022.
- [9] Art M Duval, Caroline J Klivans, and Jeremy L Martin. Cellular spanning trees and laplacians of cubical complexes. Advances in Applied Mathematics, 46(1-4):247–274, 2011.
- [10] Tom Eccles. A stability result for the union-closed size problem. Combinatorics, Probability and Computing, 25(3):399–418, 2016.
- [11] P. Frankl. Extremal set systems. In Handbook of combinatorics, volume 2, pages 1293–1329. 1995.
- [12] Justin Gilmer. A constant lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.09055, 2022.
- [13] Frédéric Haglund and Daniel T Wise. A combination theorem for special cube complexes. Annals of mathematics, pages 1427–1482, 2012.
- [14] Allen Hatcher. Algebraic topology. Cambridge University Press, 2002.
- [15] Gabor Hetyei. Simplicial and cubical complexes: anologies and differences. PhD thesis, Massachusetts Institute of Technology, 1994.
- [16] Gábor Hetyei. On the stanley ring of cubical complex. Discrete & computational geometry, 14:305–330, 1995.
- [17] Tomasz Kaczynski, Konstantin Michael Mischaikow, and Marian Mrozek. Computational homology, volume 157. Springer, 2004.
- [18] Tomasz Kaczynski, Marian Mrozek, and Anik Trahan. Ideas from zariski topology in the study of cubical homology. Canadian Journal of Mathematics, 59(5):1008–1028, 2007.
- [19] Ilan Karpas. Two results on union-closed families. arXiv preprint arXiv:1708.01434, 2017.
- [20] Luke Pebody. Extension of a method of gilmer. arXiv preprint arXiv:2211.13139, 2022.
- [21] Bjorn Poonen. Union-closed families. Journal of Combinatorial Theory, Series A, 59(2):253–268, 1992.
- [22] Will Sawin. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504, 2022.
- [23] Luca Studer. An asymptotic version of frankl’s conjecture. The American Mathematical Monthly, 128(7):652–654, 2021.
- [24] Hubert Wagner, Chao Chen, and Erald Vuçini. Efficient computation of persistent homology for cubical data. In Topological methods in data analysis and visualization II: theory, algorithms, and applications, pages 91–106. Springer, 2011.
- [25] Lei Yu. Dimension-free bounds for the union-closed sets conjecture. Entropy, 25(5):767, 2023.

*


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
