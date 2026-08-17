<!-- source: https://arxiv.org/html/2212.09279v2 | converted from HTML -->

The number of abundant elements in union-closed families without small sets

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2212.09279v2 [math.CO] 30 May 2023

# The number of abundant elements in union-closed families without small sets Thanks: The work of the first and third author was supported by project 20-09525S of the Czech Science Foundation. All authors are affiliated with the Faculty of Applied Sciences, University of West Bohemia, Czech Republic. E-mails: kabela@kma.zcu.cz, polakmi@students.zcu.cz, teska@kma.zcu.cz.

Adam Kabela Michal Polák Jakub Teska

###### Abstract

We let ℱ \mathcal{F} be a finite family of sets closed under taking unions and ∅ ∉ ℱ \emptyset\not\in\mathcal{F}, and call an element *abundant*if it belongs to more than half of the sets of ℱ \mathcal{F}. In this notation, the classical Frankl’s conjecture (1979) asserts that ℱ \mathcal{F} has an abundant element. As possible strengthenings, Poonen (1992) conjectured that if ℱ \mathcal{F} has precisely one abundant element, then this element belongs to each set of ℱ \mathcal{F}, and Cui and Hu (2019) investigated whether ℱ \mathcal{F} has at least k k abundant elements if a smallest set of ℱ \mathcal{F} is of size at least k k. Cui and Hu conjectured that this holds for k = 2 k=2 and asked whether this also holds for the cases k = 3 k=3 and k > n 2 k>\frac{n}{2} where n n is the size of the largest set of ℱ \mathcal{F}.

We show that ℱ \mathcal{F} has at least k k abundant elements if k ≥ n − 3 k\geq n-3, and that ℱ \mathcal{F} has at least k − 1 k-1 abundant elements if k = n − 4 k=n-4, and we construct a union-closed family with precisely k − 1 k-1 abundant elements for every k k and n n satisfying n − 4 ≥ k ≥ 3 n-4\geq k\geq 3 and n ≥ 9 n\geq 9 (and for k = 3 k=3 and n = 8 n=8). We also note that ℱ \mathcal{F} always has at least min ⁡ { n, 2 ​ k − n + 1 } \min\{n,2k-n+1\} abundant elements. On the other hand, we construct a union-closed family with precisely two abundant elements for every k k and n n satisfying n ≥ max ⁡ { 3, 5 ​ k − 4 } n\geq\max\{3,5k-4\}. Lastly, we show that Cui and Hu’s conjecture for k = 2 k=2 stands between Frankl’s conjecture and Poonen’s conjecture.

## 1 Introduction

We recall that a collection of sets is a *family*if all sets are distinct, and a family ℱ \mathcal{F} of sets is *union-closed*if for every pair of sets A A and B B from ℱ \mathcal{F}, their union A ∪ B A\cup B also belongs to ℱ \mathcal{F}. For families which do not contain the empty set, the classical union-closed sets conjecture states the following.

###### Conjecture 1.

If ℱ \mathcal{F} is a finite union-closed family of sets such that ∅ ∉ ℱ \emptyset\not\in\mathcal{F}, then some element belongs to more than half of the sets of ℱ \mathcal{F}.

The conjecture is associated with Frankl and its origins go back to 1970s [11, 2]. An engaging historical review and numerous related results can be found in the survey paper of Bruhn and Schaudt [4]. Notably, Conjecture 1 is also investigated in equivalent formulations concerning lattices, independent sets in bipartite graphs, and basis sets in union-closed families (for instance, see [4, 15, 5, 19]).

Conjecture 1 remains wide open despite the amount of research on the topic and the recent breakthrough result of Gilmer [10] instantly followed by [1, 7, 14, 16] and [6] which proved the statement of Conjecture 1 in weaker forms with the half replaced by a smaller constant.

In particular, it is even non-trivial to show that Conjecture 1 is true for small families, and there is a sequel of papers [15, 9, 12, 3, 18] showing that Conjecture 1 holds for union-closed families whose largest set is of size at most 7, 9, 10, 11, 12, respectively. The proofs of the partial results use the fact that Conjecture 1 is true for families which contain a set of size 1 1 or 2 2 (first shown in [17]). Hence, the proofs can essentially consider families which contain no set of size 1 1 and 2 2, and with more involved arguments also reduce the number of possible sets of size 3 3 and 4 4 (for instance, see [13]). This motivates the present study of families whose smallest set is of size at least k k.

On the other hand, it seems that we are far from disproving Conjecture 1 since there are stronger conjectures which are still open. As remarked by Poonen [15], it seems that union-closed families usually contain many elements satisfying the statement of Conjecture 1. Considering families with only one such element, Poonen [15] stated the following conjectures.

###### Conjecture 2.

Let ℱ \mathcal{F} be a finite union-closed family of sets such that ∅ ∉ ℱ \emptyset\not\in\mathcal{F}. If precisely one element belongs to more than half of the sets of ℱ \mathcal{F}, then this element belongs to each set of ℱ \mathcal{F}.

Given a family ℱ \mathcal{F} of sets, we say that elements a a and b b are *twins*if each set A A of ℱ \mathcal{F} satisfies that | A ∩ { a, b } | ≠ 1 |A\cap\{a,b\}|\neq 1, and we say that ℱ \mathcal{F} is *twin-free*if ℱ \mathcal{F} contains no twins.

###### Conjecture 3.

Let ℱ \mathcal{F} be a finite union-closed twin-free family of sets such that ∅ ∉ ℱ \emptyset\not\in\mathcal{F}, and let M M be the largest set of ℱ \mathcal{F}. If precisely one element belongs to more than half of the sets of ℱ \mathcal{F}, then ℱ \mathcal{F} is precisely the family consisting of all sets of 2 M 2^{M} which contain this element.

It appears that Conjectures 2 and 3 are still open and little is known in terms of partial results. The phenomenon of many elements satisfying the statement of Conjecture 1 is also addressed in a recent work of Cui and Hu [8]. As a possible strengthening of Conjecture 1, Cui and Hu investigated whether a finite union-closed family of sets has at least k k such elements if its smallest set is of size at least k k. In particular, the case k = 1 k=1 is precisely Conjecture 1, and they asked whether it holds for the cases k = 3 k=3 and k > n 2 k>\frac{n}{2} (where n n is the size of the largest set), and conjectured that it holds for the case k = 2 k=2.

###### Conjecture 4.

If ℱ \mathcal{F} is a finite union-closed family of sets whose smallest set is of size at least 2 2, then there are at least two elements such that each belongs to more than half of the sets of ℱ \mathcal{F}.

In the present paper, we show that if a smallest set is large, then many elements satisfy the statement of Conjecture 1 as follows.

###### Theorem 5.

Let ℱ \mathcal{F} be a union-closed family of sets and k k and n n be the sizes of its smallest and largest set, respectively. Let f f be the number of elements x x such that x x belongs to more than half of the sets of ℱ \mathcal{F}. The following statements are satisfied.

1. (1)

If k ≥ n − 3 k\geq n-3 then f ≥ k f\geq k.

2. (2)

If k = n − 4 k=n-4 then f ≥ k − 1 f\geq k-1.

3. (3)

f ≥ min ⁡ { n, 2 ​ k − n + 1 } f\geq\min\{n,2k-n+1\}.

The proof of Theorem 5 is given in Section 2. We complement the result of Theorem 5 by constructing families whose smallest set is of size k k, but fewer than k k elements satisfy the statement of Conjecture 1. In particular, we show that the difference of k k and f f can be arbitrarily large. The properties of the present constructions are summarized as follows.

###### Theorem 6.

We say that a union-closed family ℱ \mathcal{F} of sets is an ( f, k, n) (f,k,n) -construction if there are precisely f f elements each of which belongs to more than half of the sets of ℱ \mathcal{F} and k k and n n are the sizes of a smallest and the largest set of ℱ \mathcal{F}, respectively. The following statements are satisfied.

1. (1)

There is a ( 2, 3, 8) (2,3,8) -construction, ( 3, 4, 9) (3,4,9) -construction, ( 4, 5, 9) (4,5,9) -construction and ( 5, 6, 10) (5,6,10) -construction. The constructions are twin-free.

2. (2)

There is a twin-free ( 2, k, n) (2,k,n) -construction for every k k and n n which satisfy ∑ i = k − 1 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i) > ( n − 3 k − 3) + ( ⌊ n 2 ⌋ − 2 k − 2). {\sum_{i=k-1}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}>\binom{n-3}{k-3}+\binom{\lfloor\frac{n}{2}\rfloor-2}{k-2}}. This inequality holds for every k k and large enough n n.

3. (3)

There is a ( 2, k, n) (2,k,n) -construction for every k k and n n satisfying n ≥ max ⁡ { 3, 5 ​ k − 4 } {n\geq\max\{3,5k-4\}}. Furthermore, n ≥ max ⁡ { 3, 5 ​ k − 8 } n\geq\max\{3,5k-8\} suffices for even k k.

4. (4)

There is a ( k − 1, k, n) (k-1,k,n) -construction for every k k and n n satisfying n − 4 ≥ k ≥ 3 n-4\geq k\geq 3 and n ≥ 9 n\geq 9.

The proof of Theorem 6 and details on the constructions are given in Section 3. Regarding the bounds shown in Theorem 5, we note that the inequality f ≥ k f\geq k in statement (1) it tight (this is easy to see), and the inequality f ≥ k − 1 f\geq k-1 in statement (2) is also tight (this follows from item (4) of Theorem 6), and there likely is an ample room for improvement of statement (3) of Theorem 5.

In particular, statements (1) of Theorem 5 and (4) of Theorem 6 resolve the questions of [8] for every k k greater than 2 2. We leave the case k = 2 k=2 open and show that it stands between Conjectures 1 and 2 as follows.

###### Proposition 7.

Each of the following implications holds.

1. (1)

Conjecture 3 implies Conjecture 2.

2. (2)

Conjecture 2 implies Conjecture 4.

3. (3)

Conjecture 4 implies Conjecture 1.

The proof of Proposition 7 is given in Section 4. We should say that there is a minor difference between the present formulations of Conjectures 1, 2, 3 and 4 and formulations of these conjectures in the literature. For the sake of completeness, we recall the common formulations in Section 4 and show that each is equivalent to the respective present formulation.

This minor difference is that Conjectures 1, 2, 3 and 4 are commonly formulated for union-closed families possibly containing the empty set and consider elements which belong to at least half of the sets (with a non-strict inequality). In particular, the investigation of [8] concerns the size of a smallest non-empty set, and the original formulations in [15] state that the considered element belongs to all non-empty sets. However, it seems more natural to state the conjectures in the present form for union-closed families which do not contain the empty set, and accordingly we say that an element is *abundant*for a family ℱ \mathcal{F} if it belongs to more than half of the sets of ℱ \mathcal{F} (we use a strict inequality).

We also note that the results of Theorems 5 and 6 trivially translate to the original setting of [8]. In particular, if ℱ \mathcal{F} is a union-closed family such that ∅ ∈ ℱ \emptyset\in\mathcal{F}, then we apply Theorem 5 to the family ℱ ∖ ∅ \mathcal{F}\setminus\emptyset and obtain f f elements which belong to more than half of the sets of ℱ ∖ ∅ \mathcal{F}\setminus\emptyset, and we conclude that each belongs to at least half of the sets of ℱ \mathcal{F}. Furthermore, for each of the triples ( f, k, n) (f,k,n) considered in Theorem 6 distinct from ( 4, 5, 9) (4,5,9), we present an ( f, k, n) (f,k,n) -construction such that each of the remaining n − f n-f elements belongs to strictly less than half of its sets. Hence, the constructions are slightly stronger than needed, and thus relevant in the present setting and also in the original setting of [8]. (For the ( 4, 5, 9) (4,5,9) triple, we can simply add the empty set to the ( 4, 5, 9) (4,5,9) -construction used and conclude that 5 5 elements belong to strictly less than half of the sets of the modified construction.)

## 2 Sufficient conditions for many abundant elements

In the present section, we prove Theorem 5. We note that statement (3) of Theorem 5 is shown by a simple averaging argument and statements (1) and (2) are shown by slightly more involved double counting arguments. For the sake of simplicity, we view the families from a dual perspective in the proofs of statements (1) and (2). We start by showing statement (3).

###### Proof of Theorem 5.

We show statement (3). Clearly, if k = n k=n then f = n ≥ min ⁡ { n, 2 ​ k − n + 1 } f=n\geq\min\{n,2k-n+1\} as desired. Hence, we can assume that k ≤ n − 1 k\leq n-1 and we need to show that f ≥ 2 ​ k − n + 1 f\geq 2k-n+1. We let m m be the number of sets in family ℱ \mathcal{F} and s = ∑ A ∈ ℱ | A | s=\sum_{A\in\mathcal{F}}|A|. We note that s > k ​ m s>km (since k ≤ n − 1 k\leq n-1). On the other hand, we observe that f ​ m + ( n − f) ​ m 2 ≥ s fm+(n-f)\frac{m}{2}\geq s (since n − f n-f elements belong to at most half of the sets of ℱ \mathcal{F}). We combine the inequalities and get n + f 2 > k \frac{n+f}{2}>k, and it follows that f ≥ 2 ​ k − n + 1 f\geq 2k-n+1.

Next, we show statement (1). For the sake of a contradiction, we suppose that there is a union-closed family ℱ \mathcal{F} whose largest set, say M M, is of size n n and smallest set is of size k k so that n ≤ k + 3 n\leq k+3, and that there are at least n − k + 1 n-k+1 elements of M M such that each of these elements belongs to at most 1 2 ​ | ℱ | \frac{1}{2}|\mathcal{F}| sets of ℱ \mathcal{F} (where | ℱ | |\mathcal{F}| is the number of sets in ℱ \mathcal{F}). We consider a set of precisely n − k + 1 n-k+1 such elements, and we let X X denote this set and let d = n − k d=n-k.

We consider the dual family 𝒟 \mathcal{D} defined as follows. A set A A belongs to 𝒟 \mathcal{D} if and only if the set M ∖ A M\setminus A belongs to ℱ \mathcal{F}. The definition yields that | 𝒟 | = | ℱ | |\mathcal{D}|=|\mathcal{F}| and ∅ ∈ 𝒟 \emptyset\in\mathcal{D} and a largest set of 𝒟 \mathcal{D} is of size d d and each element of X X belongs to at least 1 2 ​ | 𝒟 | \frac{1}{2}|\mathcal{D}| sets of 𝒟 \mathcal{D}. Furthermore, we observe that 𝒟 \mathcal{D} is closed under taking intersections (since ℱ \mathcal{F} is union-closed).

For each set A A of 𝒟 \mathcal{D}, we define its *rank*as r ⁡ ( A) = | A ∩ X | r(A)=|A\cap X|. By the assumption on the elements of X X, we note that the sum of ranks taken over all sets of 𝒟 \mathcal{D} is at least d + 1 2 ​ | 𝒟 | \frac{d+1}{2}|\mathcal{D}| (since | X | = d + 1 |X|=d+1). In other words, the average rank is bounded from below as follows.

 | ∑ A ∈ 𝒟 r ⁡ ( A) | 𝒟 | ≥ d + 1 2 \frac{\sum_{A\in\mathcal{D}}r(A)}{|\mathcal{D}|}\geq\frac{d+1}{2} |  | (1) |

We note that r ⁡ ( A) ≤ d r(A)\leq d for every A A. For every i i of { 0, 1, …, d } \{0,1,\dots,d\}, we let r i r_{i} denote the number of sets of 𝒟 \mathcal{D} whose rank is equal to i i. Now, we can rewrite inequality ( 1) and obtain the following.

 | ∑ i = 0 d i ⋅ r i ∑ i = 0 d r i ≥ d + 1 2 \frac{\sum_{i=0}^{d}i\cdot r_{i}}{\sum_{i=0}^{d}r_{i}}\geq\frac{d+1}{2} |  | (2) |

We use inequality ( 2) and the fact that r 0 ≥ 1 r_{0}\geq 1, and we observe the following.

- •

d ≥ 2 d\geq 2.

- •

If d = 2 d=2 then r 2 ≥ 3 r_{2}\geq 3.

- •

If d = 3 d=3 then r 3 ≥ 2 r_{3}\geq 2.

On the other hand, we note that r d ≤ d + 1 r_{d}\leq d+1 (since ( d + 1 d) = d + 1 \binom{d+1}{d}=d+1). If r d = d + 1 r_{d}=d+1, then we observe that r 1 = d + 1 r_{1}=d+1 (since 𝒟 \mathcal{D} contains all possible sets of rank d d and 𝒟 \mathcal{D} is intersection-closed), and we use that d ≤ 3 d\leq 3 and obtain a contradiction with inequality ( 2).

Hence, we can assume that d = 3 d=3 and 2 ≤ r 3 ≤ 3 2\leq r_{3}\leq 3, and we discuss two cases. For the case that r 3 = 2 r_{3}=2, inequality ( 2) implies that r 1 = 0 r_{1}=0. We consider the two sets of rank 3 3 in 𝒟 \mathcal{D} and let I I denote their intersection (and note that | I | = r ⁡ ( I) = 2 |I|=r(I)=2). We observe that every set of positive rank in 𝒟 \mathcal{D} contains I I as a subset (since r 1 = 0 r_{1}=0 and 𝒟 \mathcal{D} is intersection-closed). It follows that some element of X X belongs to only one set of 𝒟 \mathcal{D}, a contradiction. For the case that r 3 = 3 r_{3}=3, we observe that r 1 = 1 r_{1}=1 (inequality ( 2) implies that r 1 ≤ 1 r_{1}\leq 1, and r 1 ≥ 1 r_{1}\geq 1 follows since 𝒟 \mathcal{D} is intersection-closed), and we let x x denote the element of X X which belongs to the set of rank 1 1. We observe that x x belongs to each of the three sets of rank 3 3 in 𝒟 \mathcal{D} (since { x } \{x\} is the only set of rank 1 1 and 𝒟 \mathcal{D} is intersection-closed), and it follows that x x also belongs every set of rank 2 2 in 𝒟 \mathcal{D}. Finally, we consider the elements of X ∖ { x } X\setminus\{x\} and count their occurrences, and we conclude that some element of X ∖ { x } X\setminus\{x\} belongs to less than 1 2 ​ | 𝒟 | \frac{1}{2}|\mathcal{D}| sets of 𝒟 \mathcal{D}, a contradiction.

Lastly, we show statement (2). Similarly to the proof of item (1), we define the dual family 𝒟 \mathcal{D}; and we note that in the setting of item (2) a largest set of 𝒟 \mathcal{D} has size 4 4. For the sake of a contradiction, we suppose that there are at least 6 6 elements each of which belongs to at least 1 2 ​ | 𝒟 | \frac{1}{2}|\mathcal{D}| sets of 𝒟 \mathcal{D}.

In addition, we say that an element a a is *dominated*by an element b b if b b belongs to every set of 𝒟 \mathcal{D} containing a a and a ≠ b a\neq b. We show the following.

###### Claim 1.

If set { a } \{a\} does not belong to 𝒟 \mathcal{D}, then element a a is dominated.

###### Proof of Claim 1.

For the sake of a contradiction, we suppose that { a } \{a\} does not belong to 𝒟 \mathcal{D}, but a a is not dominated by any element. In particular, we have that a a belongs to some set of 𝒟 \mathcal{D} (otherwise a a is dominated by every element). We let A A be a smallest set of 𝒟 \mathcal{D} containing a a, and we note that | A | ≥ 2 |A|\geq 2. Since a a is not dominated, we observe that 𝒟 \mathcal{D} contains a set B B such that a a belongs to B B and A A is not a subset of B B. We note that a a belongs to A ∩ B A\cap B, and A ∩ B A\cap B belongs to 𝒟 \mathcal{D} (since 𝒟 \mathcal{D} is intersection-closed). We conclude that A ∩ B A\cap B is smaller than A A, which contradicts the choice of A A. ∎

We let H H denote the set of all elements which belong to at least 1 2 ​ | 𝒟 | \frac{1}{2}|\mathcal{D}| sets of 𝒟 \mathcal{D}. We call a set X X a *crew*if X ⊆ H X\subseteq H and | X | = 6 |X|=6. For every set A A of 𝒟 \mathcal{D}, we let r ⁡ ( X, A) = | A ∩ X | r(X,A)=|A\cap X|. Furthermore, we let r i ​ ( X) r_{i}(X) denote the number of sets A A of 𝒟 \mathcal{D} such that r ⁡ ( X, A) = i r(X,A)=i. We say that a set A A is *relevant*for X X if A A belongs to 𝒟 \mathcal{D} and r ⁡ ( X, A) = 4 r(X,A)=4 and | A ∩ { a, b } | ∈ { 0, 2 } |A\cap\{a,b\}|\in\{0,2\} for every pair of elements a, b a,b of X X such that a a is dominated by b b. We let ℛ ⁡ ( X) \mathcal{R}(X) be the family of all relevant sets for X X, and we show the following.

###### Claim 2.

For every crew X X, we have | ℛ ⁡ ( X) | ≥ r 2 ​ ( X) + 2 ​ r 1 ​ ( X) + 3 |\mathcal{R}(X)|\geq r_{2}(X)+2r_{1}(X)+3.

###### Proof of Claim 2.

We consider an arbitrary crew X X. The definition of X X yields that

 | ∑ A ∈ 𝒟 r ⁡ ( X, A) ≥ 6 ⋅ 1 2 ​ | 𝒟 | = 3 ​ | 𝒟 |. \sum_{A\in\mathcal{D}}r(X,A)\geq 6\cdot\frac{1}{2}|\mathcal{D}|=3|\mathcal{D}|. |  |

In addition, we define w ⁡ ( X) = ∑ A ∈ 𝒟 r ⁡ ( X, A) − 3 ​ | 𝒟 | w(X)=\sum_{A\in\mathcal{D}}r(X,A)-3|\mathcal{D}| and note that w ⁡ ( X) w(X) is non-negative. In other words, we consider the elements of X X which occur in more than half of the sets of 𝒟 \mathcal{D} and let w ⁡ ( X) w(X) account for the total number of these additional occurrences. We observe that

 | w ⁡ ( X) = ∑ A ∈ 𝒟 r ⁡ ( X, A) − 3 ​ | 𝒟 | = ∑ A ∈ 𝒟 ( r ⁡ ( X, A) − 3) = ∑ i = 0 4 ( i − 3) ​ r i ​ ( X) = r 4 ​ ( X) − r 2 ​ ( X) − 2 ​ r 1 ​ ( X) − 3 ​ r 0 ​ ( X) \begin{split}w(X)&=\sum_{A\in\mathcal{D}}r(X,A)-3|\mathcal{D}|=\sum_{A\in\mathcal{D}}\left(r(X,A)-3\right)=\sum_{i=0}^{4}(i-3)r_{i}(X)\\ &=r_{4}(X)-r_{2}(X)-2r_{1}(X)-3r_{0}(X)\end{split} |  |

where the third equality follows from the fact that a largest set of 𝒟 \mathcal{D} is of size 4 4. We use that r 0 ​ ( X) ≥ 1 r_{0}(X)\geq 1 and obtain

 | r 4 ​ ( X) − w ⁡ ( X) ≥ r 2 ​ ( X) + 2 ​ r 1 ​ ( X) + 3. r_{4}(X)-w(X)\geq r_{2}(X)+2r_{1}(X)+3. |  |

It remains to show that | ℛ ⁡ ( X) | ≥ r 4 ​ ( X) − w ⁡ ( X) |\mathcal{R}(X)|\geq r_{4}(X)-w(X). We rewrite the inequality as w ⁡ ( X) ≥ r 4 ​ ( X) − | ℛ ⁡ ( X) | w(X)\geq r_{4}(X)-|\mathcal{R}(X)| and note that the right-hand side accounts for the number of sets A A of 𝒟 \mathcal{D} such that r ⁡ ( X, A) = 4 r(X,A)=4 and A A does not belong to ℛ ⁡ ( X) \mathcal{R}(X). It suffices to show that each such set contributes at least 1 1 to w ⁡ ( X) w(X). To this end, we consider an arbitrary set A A of 𝒟 ∖ ℛ ⁡ ( X) \mathcal{D}\setminus\mathcal{R}(X) satisfying r ⁡ ( X, A) = 4 r(X,A)=4. The definition of ℛ ⁡ ( X) \mathcal{R}(X) implies that there is pair of elements a, b a,b of X X such that a a is dominated by b b and | A ∩ { a, b } | = 1 |A\cap\{a,b\}|=1. We observe that b b belongs to A A (since A A belongs to 𝒟 \mathcal{D} and a a is dominated by b b). Furthermore, the facts that a a belongs to X X and a a is dominated by b b yield that at least 1 2 ​ | 𝒟 | \frac{1}{2}|\mathcal{D}| sets of 𝒟 \mathcal{D} contain { a, b } \{a,b\} as a subset. Thus, we can say that A A contributes at least 1 1 to w ⁡ ( X) w(X) (since A A contains b b but not a a). It follows that w ⁡ ( X) ≥ r 4 ​ ( X) − | ℛ ⁡ ( X) | w(X)\geq r_{4}(X)-|\mathcal{R}(X)|, which concludes the proof of the claim. ∎

As the last claim, we show the following.

###### Claim 3.

H H contains at least four elements e e such that { e } \{e\} does not belong to 𝒟 \mathcal{D}.

###### Proof of Claim 3.

We consider an arbitrary crew X X. We note that r 4 ​ ( X) ≤ 15 r_{4}(X)\leq 15 (since | X | = 6 |X|=6 and a largest set of 𝒟 \mathcal{D} has size 4 4). However if r 4 ​ ( X) = 15 r_{4}(X)=15, then the intersection-closed property implies that r 2 ​ ( X) ≥ 15 r_{2}(X)\geq 15, and we use the fact that r 4 ​ ( X) ≥ | ℛ ⁡ ( X) | r_{4}(X)\geq|\mathcal{R}(X)| and obtain a contradiction with Claim 2.

Hence, we can assume that r 4 ​ ( X) ≤ 14 r_{4}(X)\leq 14, and thus r 1 ​ ( X) ≤ 5 r_{1}(X)\leq 5 by Claim 2. In particular, there is an element a a of X X such that { a } \{a\} does not belong to 𝒟 \mathcal{D}. By Claim 1, element a a is dominated, and we let b b be an element dominating a a. Clearly, b b belongs to H H, and we consider a crew X ′ X^{\prime} containing a a and b b. We use the definition of ℛ ⁡ ( X ′) \mathcal{R}(X^{\prime}) and observe that ℛ ⁡ ( X ′) ≤ 7 \mathcal{R}(X^{\prime})\leq 7. Consequently, Claim 2 yields that r 1 ​ ( X ′) ≤ 2 r_{1}(X^{\prime})\leq 2, and thus X ′ X^{\prime} contains at most two elements e e such that { e } \{e\} belongs to 𝒟 \mathcal{D}. The desired statement follows. ∎

With Claims 1, 2 and 3 on hand, we conclude the proof as follows. Claim 3 gives an element a a of H H such that the set { a } \{a\} does not belong to 𝒟 \mathcal{D}. By Claim 1, there is an element b b dominating a a, and we note that b b also belongs to H H. We consider the set A A of all elements of H H which are dominated by b b, and we discuss two cases based on | A | |A|.

For the case that | A | ≥ 3 |A|\geq 3, we consider a crew X X such that b b belongs to X X and | A ∩ X | ≥ 3 |A\cap X|\geq 3. We observe that each relevant set contains an element of A ∩ X A\cap X (since | X | = 6 |X|=6 and | A ∩ X | ≥ 3 |A\cap X|\geq 3), and hence each relevant set contains b b, and thus it contains all elements of A ∩ X A\cap X. The fact that | ( A ∩ X) ∪ { b } | ≥ 4 |(A\cap X)\cup\{b\}|\geq 4 implies that | ℛ ⁡ ( X) | ≤ 1 |\mathcal{R}(X)|\leq 1, and we obtain a contradiction with Claim 2.

For the case that | A | ≤ 2 |A|\leq 2, we use that | A ∪ { b } | ≤ 3 |A\cup\{b\}|\leq 3 and Claim 3 guarantees that there is an element a ′ a^{\prime} of H ∖ ( A ∪ { b }) H\setminus(A\cup\{b\}) such that the set { a ′ } \{a^{\prime}\} does not belong to 𝒟 \mathcal{D}. In addition, we use Claim 1 and consider an element b ′ b^{\prime} dominating a ′ a^{\prime}, and we observe that b ′ b^{\prime} is distinct from a a and b b (since a ′ a^{\prime} is not dominated by b b). It follows that a, b, a ′ a,b,a^{\prime} and b ′ b^{\prime} are four distinct elements of H H, and we consider a crew X X which contains these four elements. We note that the only possible relevant sets are { a, b, a ′, b ′ } \{a,b,a^{\prime},b^{\prime}\} and X ∖ { a, b } X\setminus\{a,b\} and X ∖ { a ′, b ′ } X\setminus\{a^{\prime},b^{\prime}\}. We conclude that | ℛ ⁡ ( X) | ≤ 3 |\mathcal{R}(X)|\leq 3 (and if | ℛ ⁡ ( X) | = 3 |\mathcal{R}(X)|=3 then r 2 ​ ( X) ≥ 3 r_{2}(X)\geq 3), and a contradiction with Claim 2 follows. ∎

## 3 Families with few abundant elements

In the present section, we construct various union-closed families of sets and we use the families for proving Theorem 6.

We let 𝒫 3 8 \mathcal{P}^{8}_{3} be the family of sets constructed as follows. We let 𝒜 \mathcal{A} denote the family consisting of all sets A A such that A ⊆ { 0, 1, …, 7 } A\subseteq\{0,1,\dots,7\} and { 0, 1 } ⊂ A \{0,1\}\subset A and | A | ≥ 3 |A|\geq 3. We let ℰ = { { 0, 2, 4 }, { 0, 2, 6 }, { 0, 4, 6 }, { 0, 2, 4, 6 } } \mathcal{E}=\{\{0,2,4\},\{0,2,6\},\{0,4,6\},\{0,2,4,6\}\} and 𝒪 = { { 1; 3; 5 }; { 1; 3; 7 }; { 1; 5; 7 }; { 1; 3; 5; 7 } } \mathcal{O}=\{\{1\mathchar 59\penalty\hskip 0.0pt3\mathchar 59\penalty\hskip 0.0pt5\}\mathchar 59\penalty\hskip 0.0pt\{1\mathchar 59\penalty\hskip 0.0pt3\mathchar 59\penalty\hskip 0.0pt7\}\mathchar 59\penalty\hskip 0.0pt\{1\mathchar 59\penalty\hskip 0.0pt5\mathchar 59\penalty\hskip 0.0pt7\}\mathchar 59\penalty\hskip 0.0pt\{1\mathchar 59\penalty\hskip 0.0pt3\mathchar 59\penalty\hskip 0.0pt5\mathchar 59\penalty\hskip 0.0pt7\}\}, and we let 𝒫 3 8 = 𝒜 ∪ ℰ ∪ 𝒪 \mathcal{P}^{8}_{3}=\mathcal{A}\cup\mathcal{E}\cup\mathcal{O}.

Also, we extend 𝒫 3 8 \mathcal{P}^{8}_{3} by adding element 8 8 to every set, and we let 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} denote the resulting family.

Next, we construct family 𝒬 5 9 \mathcal{Q}^{9}_{5} as follows. We let ℬ \mathcal{B} denote the family consisting of all sets B B such that B ⊆ { 0, 1, …, 8 } B\subseteq\{0,1,\dots,8\} and { 0, 1, …, 5 } ⊆ B \{0,1,\dots,5\}\subseteq B. We let 𝒞 \mathcal{C} denote the family consisting of all sets C C such that C ⊆ { 0, 1, 2, 3, 6, 7, 8 } C\subseteq\{0,1,2,3,6,7,8\} and { 0, 1, 2 } ⊂ C \{0,1,2\}\subset C and | C | ≥ 5 |C|\geq 5. We let 𝒟 = { { 0, 1, 3, 4, 5 }, { 0, 2, 3, 4, 5 }, { 1, 2, 3, 4, 5 } } \mathcal{D}=\{\{0,1,3,4,5\},\{0,2,3,4,5\},\{1,2,3,4,5\}\} and 𝒬 5 9 = ℬ ∪ 𝒞 ∪ 𝒟 \mathcal{Q}^{9}_{5}=\mathcal{B}\cup\mathcal{C}\cup\mathcal{D}.

Lastly, we construct family ℛ 6 10 \mathcal{R}^{10}_{6}. We let ℱ \mathcal{F} denote the family consisting of all sets F F such that F ⊆ { 0, 1, …, 9 } F\subseteq\{0,1,\dots,9\} and { 0, 1, …, 4 } ⊂ F \{0,1,\dots,4\}\subset F and | F | ≥ 6 |F|\geq 6. For every i i of { 0, 1, …, 4 } \{0,1,\dots,4\}, we let G i G_{i} be the set depicted in Figure 1 and 𝒢 i \mathcal{G}_{i} be the family consisting of G i G_{i} and all subsets G i ′ G^{\prime}_{i} of G i G_{i} such that | G i ′ | = 6 |G^{\prime}_{i}|=6 and | G i ′ ∩ { 0, 1, …, 4 } | = 4 |G^{\prime}_{i}\cap\{0,1,\dots,4\}|=4. For instance, 𝒢 0 = { { 1, 2, 3, 4, 7, 8 }, { 1, 2, 3, 4, 7, 9 }, { 1, 2, 3, 4, 8, 9 }, { 1, 2, 3, 4, 7, 8, 9 } } \mathcal{G}_{0}=\{\{1,2,3,4,7,8\},\{1,2,3,4,7,9\},\{1,2,3,4,8,9\},\{1,2,3,4,7,8,9\}\} We let ℛ 6 10 = ℱ ∪ 𝒢 0 ∪ 𝒢 1 ∪ ⋯ ∪ 𝒢 4 \mathcal{R}^{10}_{6}=\mathcal{F}\cup\mathcal{G}_{0}\cup\mathcal{G}_{1}\cup\dots\cup\mathcal{G}_{4}.

Figure 1: Sets G 0, G 1, …, G 4 G_{0},G_{1},\dots,G_{4} viewed as subsets of { 0, 1, …, 9 } \{0,1,\dots,9\}. For instance, G 0 = { 1, 2, 3, 4, 7, 8, 9 } G_{0}=\{1,2,3,4,7,8,9\}.

We show relevant properties of the constructions as follows.

###### Proposition 8.

Let 𝒫 3 8 \mathcal{P}^{8}_{3}, 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}, 𝒬 5 9 \mathcal{Q}^{9}_{5} and ℛ 6 10 \mathcal{R}^{10}_{6} be the families of sets defined above. Each of the families is twin-free and the following statements are satisfied.

1. (1)

𝒫 3 8 \mathcal{P}^{8}_{3} is a ( 2, 3, 8) (2,3,8) -construction and 0 0 and 1 1 are abundant.

2. (2)

𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} is a ( 3, 4, 9) (3,4,9) -construction and 0, 1 0,1 and 8 8 are abundant.

3. (3)

𝒬 5 9 \mathcal{Q}^{9}_{5} is a ( 4, 5, 9) (4,5,9) -construction and 0, 1, 2 0,1,2 and 3 3 are abundant.

4. (4)

ℛ 6 10 \mathcal{R}^{10}_{6} is a ( 5, 6, 10) (5,6,10) -construction and 0, 1, 2, 3 0,1,2,3 and 4 4 are abundant.

Furthermore, each non-abundant element for 𝒫 3 8 \mathcal{P}^{8}_{3} belongs to strictly less than half of the sets, and similarly for 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} and ℛ 6 10 \mathcal{R}^{10}_{6}.

###### Proof.

For each of the families 𝒫 3 8 \mathcal{P}^{8}_{3}, 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}, 𝒬 5 9 \mathcal{Q}^{9}_{5} and ℛ 6 10 \mathcal{R}^{10}_{6}, we note that the subscript and superscript correspond to the sizes of its smallest and largest set, respectively. We observe that each of the families is twin-free. It remains to count the occurrences of elements and show that the families are union-closed.

We show statement (1). We note that | 𝒫 3 8 | = | 𝒜 | + | ℰ | + | 𝒪 | = 63 + 4 + 4 = 71 |\mathcal{P}^{8}_{3}|=|\mathcal{A}|+|\mathcal{E}|+|\mathcal{O}|=63+4+4=71. Also, we observe that each of elements 0, 1 0,1 belongs to 67 67 sets of 𝒫 3 8 \mathcal{P}^{8}_{3} (it belongs to all sets of 𝒜 \mathcal{A} and 4 4 sets of ℰ ∪ 𝒪 \mathcal{E}\cup\mathcal{O}), and each of elements 2, 3, …, 7 2,3,\dots,7 belongs to 35 35 sets of 𝒫 3 8 \mathcal{P}^{8}_{3} (it belongs to 32 32 sets of 𝒜 \mathcal{A} and 3 3 sets of ℰ ∪ 𝒪 \mathcal{E}\cup\mathcal{O}). Thus, elements 0 0 and 1 1 are abundant for 𝒫 3 8 \mathcal{P}^{8}_{3} and each of elements 2, 3, …, 7 2,3,\dots,7 belongs to strictly less than half of the sets of 𝒫 3 8 \mathcal{P}^{8}_{3}.

In order to show that 𝒫 3 8 \mathcal{P}^{8}_{3} is union-closed, we consider arbitrary sets X X and Y Y of 𝒫 3 8 \mathcal{P}^{8}_{3} and show that the set X ∪ Y X\cup Y belongs to 𝒫 3 8 \mathcal{P}^{8}_{3}. We discuss three cases. For the case that 1 1 does not belong to X ∪ Y X\cup Y, we note that X X and Y Y belong to ℰ \mathcal{E}. The definition of ℰ \mathcal{E} yields that the set X ∪ Y X\cup Y belongs to ℰ \mathcal{E}, and hence X ∪ Y X\cup Y belongs to 𝒫 3 8 \mathcal{P}^{8}_{3}. For the case that 0 0 does not belong to X ∪ Y X\cup Y, the conclusion follows similarly from the definition of 𝒪 \mathcal{O}. Thus, we can assume that 0 0 and 1 1 belong to X ∪ Y X\cup Y. Since | X | ≥ 3 |X|\geq 3 and | Y | ≥ 3 |Y|\geq 3, we have | X ∪ Y | ≥ 3 |X\cup Y|\geq 3. By the definition of 𝒜 \mathcal{A}, the set X ∪ Y X\cup Y belongs to 𝒜 \mathcal{A}, and thus to 𝒫 3 8 \mathcal{P}^{8}_{3}.

We proceed with statement (2). We use the properties of 𝒫 3 8 \mathcal{P}^{8}_{3} and note that 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} is also union-closed, and each of elements 0, 1 0,1 belongs to 67 67 sets of 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}, and each of elements 2, 3, …, 7 2,3,\dots,7 belongs to 35 35 sets of 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}, and element 8 8 belongs to all 71 71 sets of 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}. Thus, elements 0, 1 0,1 and 8 8 are abundant for 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} and each of elements 2, 3, …, 7 2,3,\dots,7 belongs to strictly less than half of the sets of 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}.

Next, we show statement (3). We note that | 𝒬 5 9 | = | ℬ | + | 𝒞 | + | 𝒟 | = 8 + 11 + 3 = 22 |\mathcal{Q}^{9}_{5}|=|\mathcal{B}|+|\mathcal{C}|+|\mathcal{D}|=8+11+3=22. We observe that each of elements 0, 1, 2 0,1,2 belongs to 21 21 sets, and element 3 3 belongs to 18 18 sets, and each of elements 4, 5, …, 8 4,5,\dots,8 belongs to 11 11 sets (since no set from 𝒞 \mathcal{C} contains 4 4 or 5 5, and each of elements 6, 7 6,7 and 8 8 belongs to 4 4 sets from ℬ \mathcal{B} and 7 7 sets from 𝒞 \mathcal{C} and no set from 𝒟 \mathcal{D}).

We consider arbitrary sets X X and Y Y of 𝒬 5 9 \mathcal{Q}^{9}_{5} and discuss two cases. For the case that both X X and Y Y belong to 𝒞 \mathcal{C}, we note that X ∪ Y X\cup Y belongs to 𝒞 \mathcal{C} (this follows from the definition of 𝒞 \mathcal{C}), and thus X ∪ Y X\cup Y belongs to 𝒬 5 9 \mathcal{Q}^{9}_{5}. For the case that at least one of X X and Y Y belongs to ℬ ∪ 𝒟 \mathcal{B}\cup\mathcal{D}, we observe that { 0, 1, …, 5 } \{0,1,\dots,5\} is a subset of X ∪ Y X\cup Y if X ≠ Y X\neq Y. It follows that X ∪ Y X\cup Y belongs to ℬ \mathcal{B}, and thus to 𝒬 5 9 \mathcal{Q}^{9}_{5}.

Lastly, we show statement (4). We note that | ℛ 6 10 | = | ℱ | + | 𝒢 0 | + ⋯ + | 𝒢 4 | = 31 + 5 ⋅ 4 = 51 |\mathcal{R}^{10}_{6}|=|\mathcal{F}|+|\mathcal{G}_{0}|+\dots+|\mathcal{G}_{4}|=31+5\cdot 4=51, and each of elements 0, 1, …, 4 0,1,\dots,4 belongs to 47 47 sets ( 31 31 sets of ℱ \mathcal{F} and 16 16 sets of 𝒢 0 ∪ ⋯ ∪ 𝒢 4 \mathcal{G}_{0}\cup\dots\cup\mathcal{G}_{4}), and each of elements 5, 6, …, 9 5,6,\dots,9 belongs to 25 25 sets ( 16 16 sets of ℱ \mathcal{F} and 9 9 sets of 𝒢 0 ∪ ⋯ ∪ 𝒢 4 \mathcal{G}_{0}\cup\dots\cup\mathcal{G}_{4}).

We consider arbitrary sets X X and Y Y of ℛ 6 10 \mathcal{R}^{10}_{6}. We use that each set of ℛ 6 10 \mathcal{R}^{10}_{6} contains at least four elements of { 0, 1, …, 4 } \{0,1,\dots,4\} and discuss two cases. For the case that the set X ∪ Y X\cup Y contains { 0, 1, …, 4 } \{0,1,\dots,4\} as a subset, we note that X ∪ Y X\cup Y belongs to ℱ \mathcal{F}, and thus to ℛ 6 10 \mathcal{R}^{10}_{6}. Otherwise, we note that X ∪ Y X\cup Y contains all but one element of { 0, 1, …, 4 } \{0,1,\dots,4\}, and we let i i be this element. It follows that X X and Y Y belong to 𝒢 i \mathcal{G}_{i}, and hence X ∪ Y X\cup Y belongs to 𝒢 i \mathcal{G}_{i}, and thus to ℛ 6 10 \mathcal{R}^{10}_{6}. ∎

With Proposition 8 on hand, we consider families 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}} and 𝒬 5 9 \mathcal{Q}^{9}_{5} and simple extensions of families 𝒫 3 8 \mathcal{P}^{8}_{3} and ℛ 6 10 \mathcal{R}^{10}_{6} and prove Theorem 6.

###### Proof of Theorem 6.

For statement (1), we consider families 𝒫 3 8 \mathcal{P}^{8}_{3}, 𝒫 4 9 ¯ \overline{\mathcal{P}^{9}_{4}}, 𝒬 5 9 \mathcal{Q}^{9}_{5} and ℛ 6 10 \mathcal{R}^{10}_{6} and note that they have the desired properties by Proposition 8.

In order to show statement (2), we consider a simple extension 𝒫 k n \mathcal{P}^{n}_{k} of the construction of 𝒫 3 8 \mathcal{P}^{8}_{3}. Given integers n n and k k such that n ≥ k ≥ 3 n\geq k\geq 3, we let 𝒜 \mathcal{A} be the family consisting of all sets A A such that A ⊆ { 0, 1, …, n − 1 } A\subseteq\{0,1,\dots,n-1\} and { 0, 1 } ⊂ A \{0,1\}\subset A and | A | ≥ k |A|\geq k, and let ℰ \mathcal{E} be the family consisting of all sets E E such that E ⊆ { 0, 2, …, 2 ​ ⌊ n 2 ⌋ − 2 } E\subseteq\{0,2,\dots,2\lfloor\frac{n}{2}\rfloor-2\} and 0 ∈ E 0\in E and | E | ≥ k |E|\geq k, and let 𝒪 \mathcal{O} be the family consisting of all sets O O such that O ⊆ { 1, 3, …, 2 ​ ⌊ n 2 ⌋ − 1 } O\subseteq\{1,3,\dots,2\lfloor\frac{n}{2}\rfloor-1\} and 1 ∈ O 1\in O and | O | ≥ k |O|\geq k, and we let 𝒫 k n = 𝒜 ∪ ℰ ∪ 𝒪 \mathcal{P}^{n}_{k}=\mathcal{A}\cup\mathcal{E}\cup\mathcal{O}. In particular, | ℰ | = | 𝒪 | |\mathcal{E}|=|\mathcal{O}| for every n n and k k, and if n n is odd, then element n − 1 n-1 belongs to no set from ℰ ∪ 𝒪 \mathcal{E}\cup\mathcal{O}.

We observe that 𝒫 k n \mathcal{P}^{n}_{k} is twin-free, and the fact that 𝒫 k n \mathcal{P}^{n}_{k} is union-closed follows by a very similar argument as for the family 𝒫 3 8 \mathcal{P}^{8}_{3}. We also note that elements 0 0 and 1 1 are abundant for 𝒫 k n \mathcal{P}^{n}_{k} since | 𝒜 | + | ℰ | > | 𝒪 | |\mathcal{A}|+|\mathcal{E}|>|\mathcal{O}| and | 𝒜 | + | 𝒪 | > | ℰ | |\mathcal{A}|+|\mathcal{O}|>|\mathcal{E}|.

Finally, we use the assumption that k k and n n satisfy the inequality

 | ∑ i = k − 1 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i) > ( n − 3 k − 3) + ( ⌊ n 2 ⌋ − 2 k − 2), {\sum_{i=k-1}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}>\binom{n-3}{k-3}+\binom{\lfloor\frac{n}{2}\rfloor-2}{k-2}}, |  |

and we show that each of elements 2, 3, …, n − 1 2,3,\dots,n-1 belongs to strictly less than half of the sets of 𝒫 k n \mathcal{P}^{n}_{k}. In particular, we note that each of elements 2, 3, …, n − 2 2,3,\dots,n-2 belongs to the same number of sets of 𝒫 k n \mathcal{P}^{n}_{k}, and element n − 1 n-1 does not belong to a greater number of sets. Hence, it suffices to consider just element 2 2 and show that it belongs to strictly less than half of the sets of 𝒫 k n \mathcal{P}^{n}_{k}. We let 𝒜 2 \mathcal{A}_{2} be the family of all sets of 𝒜 \mathcal{A} which contain element 2 2 and let 𝒜 0 = 𝒜 ∖ 𝒜 2 \mathcal{A}_{0}=\mathcal{A}\setminus\mathcal{A}_{2}. Instead of enumerating | 𝒜 2 | |\mathcal{A}_{2}| and | 𝒜 0 | |\mathcal{A}_{0}|, we enumerate the quantity a = | 𝒜 2 | − | 𝒜 0 | a=|\mathcal{A}_{2}|-|\mathcal{A}_{0}|. To this end, we consider an arbitrary set A A of 𝒜 0 \mathcal{A}_{0} and observe that the set A ∪ { 2 } A\cup\{2\} always belongs to 𝒜 \mathcal{A}, and similarly we consider a set A A of 𝒜 2 \mathcal{A}_{2} and observe that the set A ∖ { 2 } A\setminus\{2\} belongs to 𝒜 \mathcal{A} if and only if | A | > k |A|>k. These two observations imply that a a is equal to the number of sets of size k k which belong to 𝒜 2 \mathcal{A}_{2}, that is, a = ( n − 3 k − 3) a=\binom{n-3}{k-3}. We use a similar reasoning for the sets of ℰ \mathcal{E}. We let e e be equal to the number of sets of ℰ \mathcal{E} containing element 2 2 minus the number of the remaining sets of ℰ \mathcal{E}, and we observe that e = ( ⌊ n 2 ⌋ − 2 k − 2) e=\binom{\lfloor\frac{n}{2}\rfloor-2}{k-2}. Lastly, we enumerate the number of sets in 𝒪 \mathcal{O}. We use that a smallest set in 𝒪 \mathcal{O} is of size k k and the largest set is of size ⌊ n 2 ⌋ \lfloor\frac{n}{2}\rfloor and each set contains element 0 0, and hence we note that

 | | 𝒪 | = ∑ i = k − 1 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i). |\mathcal{O}|=\sum_{i=k-1}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}. |  |

We conclude that | 𝒪 | > a + e |\mathcal{O}|>a+e, and thus element 2 2 belongs to strictly less than half of the sets of 𝒫 k n \mathcal{P}^{n}_{k}.

Finally, we show that for every fixed k k, we can choose n n large enough so that

 | ∑ i = k − 1 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i) > ( n − 3 k − 3) + ( ⌊ n 2 ⌋ − 2 k − 2). {\sum_{i=k-1}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}>\binom{n-3}{k-3}+\binom{\lfloor\frac{n}{2}\rfloor-2}{k-2}}. |  |

In particular if k − 1 ≤ 1 2 ​ ( ⌊ n 2 ⌋ − 1) k-1\leq\frac{1}{2}\left(\lfloor\frac{n}{2}\rfloor-1\right), then it is easy to see that the left-hand side can be bounded by an exponential function as

 | ∑ i = k − 1 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i) ≥ 1 2 ​ ∑ i = 0 ⌊ n 2 ⌋ − 1 ( ⌊ n 2 ⌋ − 1 i) = 1 2 ⋅ 2 ⌊ n 2 ⌋ − 1 = 2 ⌊ n 2 ⌋ − 2. \sum_{i=k-1}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}\geq\frac{1}{2}\sum_{i=0}^{\lfloor\frac{n}{2}\rfloor-1}\binom{\lfloor\frac{n}{2}\rfloor-1}{i}=\frac{1}{2}\cdot 2^{\lfloor\frac{n}{2}\rfloor-1}=2^{\lfloor\frac{n}{2}\rfloor-2}. |  |

For the right-hand side, we note that the first term is bounded by a polynomial as

 | ( n − 3 k − 3) = n − 3 k − 3 ⋅ n − 4 k − 4 ⋅ ⋯ ⋅ n − k − 1 1 < ( n − 3) k − 3, \binom{n-3}{k-3}=\frac{n-3}{k-3}\cdot\frac{n-4}{k-4}\cdot\dots\cdot\frac{n-k-1}{1}<(n-3)^{k-3}, |  |

and similarly the second term is bounded as

 | ( ⌊ n 2 ⌋ − 2 k − 2) < ( ⌊ n 2 ⌋ − 2) k − 2. \binom{\lfloor\frac{n}{2}\rfloor-2}{k-2}<\left(\lfloor\frac{n}{2}\rfloor-2\right)^{k-2}. |  |

For every k k and large enough n n, we clearly have that

 | 2 ⌊ n 2 ⌋ − 2 > ( n − 3) k − 3 + ( ⌊ n 2 ⌋ − 2) k − 2, 2^{\lfloor\frac{n}{2}\rfloor-2}>(n-3)^{k-3}+\left(\lfloor\frac{n}{2}\rfloor-2\right)^{k-2}, |  |

and the desired inequality follows.

Next, we show statement (3). We consider integers k k and n n which satisfy that n ≥ max ⁡ { 3, k + 8 ​ ⌈ k 2 ⌉ − 8 } {n\geq\max\{3,k+8\left\lceil\frac{k}{2}\right\rceil-8\}}, and we note that the term k + 8 ​ ⌈ k 2 ⌉ − 8 k+8\left\lceil\frac{k}{2}\right\rceil-8 is equal to 5 ​ k − 8 5k-8 for even k k, and it is equal to 5 ​ k − 4 5k-4 for odd k k as desired.

For 0 ≤ k ≤ 3 0\leq k\leq 3, we consider the following simple families and observe that each family is a ( 2, k, n) (2,k,n) -construction.

- •

We consider { ∅, { 0 }, { 1 }, { 0, 1 }, { 0, 1, …, n − 1 } } \{\emptyset,\{0\},\{1\},\{0,1\},\{0,1,\dots,n-1\}\} for k = 0 k=0.

- •

Similarly, { { 0 }, { 1 }, { 0, 1 }, { 0, 1, …, n − 1 } } \{\{0\},\{1\},\{0,1\},\{0,1,\dots,n-1\}\} for k = 1 k=1.

- •

We consider { { 0, 1 }, { 0, 1, …, n − 1 } } \{\{0,1\},\{0,1,\dots,n-1\}\} for k = 2 k=2.

- •

For k = 3 k=3, we consider the family obtained from 𝒫 3 8 \mathcal{P}^{8}_{3} by adding n − 8 n-8 new elements, say 8, 9, …, n − 1 8,9,\dots,n-1, to each set which contains element 2 2.

Hence, we can assume that k ≥ 4 k\geq 4 and n ≥ k + 8 ​ ⌈ k 2 ⌉ − 8 n\geq k+8\left\lceil\frac{k}{2}\right\rceil-8, and we produce a ( 2, k, n) (2,k,n) -construction by extending the family 𝒫 4 12 \mathcal{P}^{12}_{4}. To this end, we consider sets of additional elements A 2, A 3, …, A 11 A_{2},A_{3},\dots,A_{11} such that A 2, A 3, …, A 11 A_{2},A_{3},\dots,A_{11} are pairwise disjoint and each is disjoint with { 0, 1, …, 11 } \{0,1,\dots,11\}, and | A i | = ⌈ k − 4 2 ⌉ |A_{i}|=\left\lceil\frac{k-4}{2}\right\rceil for every i i of { 2, 3, …, 9 } \{2,3,\dots,9\}, and | A 10 | = ⌊ k − 4 2 ⌋ |A_{10}|=\left\lfloor\frac{k-4}{2}\right\rfloor and | A 11 | = n − 12 − ∑ i = 2 10 | A i | |A_{11}|=n-12-\sum_{i=2}^{10}|A_{i}|. We extend 𝒫 4 12 \mathcal{P}^{12}_{4} as follows. For every i i of { 2, 3, …, 11 } \{2,3,\dots,11\} in sequence, we add all elements of A i A_{i} to every set containing i i. We let 𝒫 + \mathcal{P}^{+} denote the resulting family.

Clearly, the largest set of 𝒫 + \mathcal{P}^{+} is { 0, 1, …, 11 } ∪ A 2 ∪ A 3 ∪ ⋯ ∪ A 11 \{0,1,\dots,11\}\cup A_{2}\cup A_{3}\cup\dots\cup A_{11} and its size is 12 + | A 2 | + | A 3 | + ⋯ + | A 11 | 12+|A_{2}|+|A_{3}|+\dots+|A_{11}| which is equal to n n. In order to determine the size of a smallest set of 𝒫 + \mathcal{P}^{+}, we first note the following.

 | | A 11 | \displaystyle|A_{11}| | = n − 12 − ∑ i = 2 10 | A i | = n − 12 − 8 ​ ⌈ k − 4 2 ⌉ − ⌊ k − 4 2 ⌋ \displaystyle=n-12-\sum_{i=2}^{10}|A_{i}|=n-12-8\left\lceil\frac{k-4}{2}\right\rceil-\left\lfloor\frac{k-4}{2}\right\rfloor |  |

 |  | = n − k − 7 ​ ⌈ k 2 ⌉ + 6 ≥ k + 8 ​ ⌈ k 2 ⌉ − 8 − k − 7 ​ ⌈ k 2 ⌉ + 6 \displaystyle=n-k-7\left\lceil\frac{k}{2}\right\rceil+6\geq k+8\left\lceil\frac{k}{2}\right\rceil-8-k-7\left\lceil\frac{k}{2}\right\rceil+6 |  |

 |  | ≥ ⌈ k − 4 2 ⌉ \displaystyle\geq\left\lceil\frac{k-4}{2}\right\rceil |  |

Hence, | A 11 | ≥ | A i | |A_{11}|\geq|A_{i}| for every i i of { 2, 3, …, 10 } \{2,3,\dots,10\}, and it follows that a smallest set of 𝒫 + \mathcal{P}^{+} is, for instance, the set { 0, 1, 2, 10 } ∪ A 2 ∪ A 10 \{0,1,2,10\}\cup A_{2}\cup A_{10} and its size is 4 + ⌈ k − 4 2 ⌉ + ⌊ k − 4 2 ⌋ 4+\lceil\frac{k-4}{2}\rceil+\lfloor\frac{k-4}{2}\rfloor which is equal to k k.

We use the properties of 𝒫 4 12 \mathcal{P}^{12}_{4} and observe that 𝒫 + \mathcal{P}^{+} is union-closed. We conclude that 𝒫 + \mathcal{P}^{+} is a ( 2, k, n) (2,k,n) -construction, and 0 0 and 1 1 are the only abundant elements for 𝒫 + \mathcal{P}^{+}, and each non-abundant element belongs to strictly less than half of the sets of 𝒫 + \mathcal{P}^{+}.

Lastly, we show statement (4). We let k k and n n be arbitrary integers such that n − 4 ≥ k ≥ 3 n-4\geq k\geq 3 and n ≥ 9 n\geq 9 and we produce a ( k − 1, k, n) (k-1,k,n) -construction. We discuss three cases.

For the case that n = 9 n=9 and k = 5 k=5, we just consider family 𝒬 5 9 \mathcal{Q}^{9}_{5} and use item (3) of Proposition 8.

For the case that k = n − 4 k=n-4 and n ≥ 10 n\geq 10, we consider family ℛ 6 10 \mathcal{R}^{10}_{6} and its properties given item (4) of Proposition 8, and we extend the family as follows. We take n − 10 n-10 new elements, say 10, 11, …, n − 1 10,11,\dots,n-1, and augment every set of ℛ 6 10 \mathcal{R}^{10}_{6} by adding all these elements, and we let ℛ k n ¯ \overline{\mathcal{R}^{n}_{k}} denote the resulting family. We note that ℛ k n ¯ \overline{\mathcal{R}^{n}_{k}} is union-closed and its smallest set is of size k k and largest set of size n n and precisely k − 1 k-1 elements are abundant for ℛ k n ¯ \overline{\mathcal{R}^{n}_{k}} as desired. Furthermore, each of elements 5, 6, …, 9 5,6,\dots,9 belongs to strictly less than half of the sets of ℛ k n ¯ \overline{\mathcal{R}^{n}_{k}}.

For the case that n − 5 ≥ k ≥ 3 n-5\geq k\geq 3 and n ≥ 9 n\geq 9, we use item (1) of Proposition 8 and we extend family 𝒫 3 8 \mathcal{P}^{8}_{3} as follows. We choose a non-abundant element, say 2 2, and we augment every set of 𝒫 3 8 \mathcal{P}^{8}_{3} containing 2 2 by adding elements 8, 9, …, n − 1 8,9,\dots,n-1 (which is n − 8 n-8 new elements), and augment every other set by adding elements 8, 9, …, k + 4 8,9,\dots,k+4 (which is k − 3 k-3 elements), and we let 𝒫 + \mathcal{P}^{+} denote the resulting family. We observe that 𝒫 + \mathcal{P}^{+} is union-closed and the abundant elements for 𝒫 + \mathcal{P}^{+} are 0, 1 0,1 and 8, 9, …, k + 4 8,9,\dots,k+4. We conclude that 𝒫 + \mathcal{P}^{+} is a ( k − 1, k, n) (k-1,k,n) -construction and each non-abundant element for 𝒫 + \mathcal{P}^{+} belongs to strictly less than half of the sets of 𝒫 + \mathcal{P}^{+}. ∎

In relation to statement (3) of Theorem 6, we remark that a simpler ( 2, k, n) (2,k,n) -construction can be obtained by extending the family 𝒫 3 8 \mathcal{P}^{8}_{3} (instead of 𝒫 4 12 \mathcal{P}^{12}_{4}) and considering a slightly worse bound of n ≥ max ⁡ { 3, 6 ​ k − 10 } n\geq\max\{3,6k-10\}.

## 4 Relations among conjectures

In the present section, we show Proposition 7. For the sake of completeness, we also recall the common formulations of the conjectures and show that they are equivalent to the formulations stated in Section 1. Following [4, 15, 8], the formulations are recalled in Conjectures A, B, C and D.

###### Conjecture A.

If ℱ \mathcal{F} is a finite union-closed family of sets such that ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}, then some element belongs to at least half of the sets of ℱ \mathcal{F}.

###### Conjecture B.

Let ℱ \mathcal{F} be a finite union-closed family of sets. If precisely one element belongs to at least half of the sets of ℱ \mathcal{F}, then this element belongs to each non-empty set of ℱ \mathcal{F}.

###### Conjecture C.

Let ℱ \mathcal{F} be a finite union-closed family of sets and let M M be the largest set of ℱ \mathcal{F}. For every pair of elements a, b a,b of M M, let ℱ \mathcal{F} contain a set A A such that | A ∩ { a, b } | = 1 |A\cap\{a,b\}|=1. Let x x be the only element which belongs to at least half of the sets of ℱ \mathcal{F}. If | M | ≥ 2 |M|\geq 2, then ℱ \mathcal{F} consists of the empty set and precisely all sets of 2 M 2^{M} containing x x. If | M | = 1 |M|=1 then ℱ = { { x } } \mathcal{F}=\{\{x\}\} or ℱ = { ∅, { x } } \mathcal{F}=\{\emptyset,\{x\}\}.

###### Conjecture D.

If ℱ \mathcal{F} is a finite union-closed family of sets such that ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\} and a smallest non-empty set of ℱ \mathcal{F} is of size at least 2 2, then there are at least two elements such that each belongs to a least half of the sets of ℱ \mathcal{F}.

We show that the formulations of the conjectures are equivalent as follows.

###### Proposition 9.

Each of the following equivalences holds.

1. (1)

Conjectures 1 and A are equivalent.

2. (2)

Conjectures 2 and B are equivalent.

3. (3)

Conjectures 3 and C are equivalent.

4. (4)

Conjectures 4 and D are equivalent.

Proving Propositions 7 and 9, we note that the arguments actually show the desired implications and equivalences also with the additional constraint that the largest set is of size at most n n. For a possible reference in further research, we prove the relations of Propositions 7 and 9 in the stronger form with this additional constraint as follows.

###### Proposition 10.

Let n n be a positive integer. For the sake of brewity, we say that a conjecture works for n n if the conjecture is true under the additional constraint that the largest set of ℱ \mathcal{F} is of size at most n n. The following statements all hold.

1. (1)

If Conjecture 3 works for n n, then Conjecture 2 works for n n.

2. (2)

If Conjecture 2 works for n n, then Conjecture 4 works for n n.

3. (3)

If Conjecture 4 works for n n, then Conjecture 1 works for n n.

4. (4)

Conjecture 1 works for n n if and only if Conjecture A works for n n.

5. (5)

Conjecture 2 works for n n if and only if Conjecture B works for n n.

6. (6)

Conjecture 3 works for n n if and only if Conjecture C works for n n.

7. (7)

Conjecture 4 works for n n if and only if Conjecture D works for n n.

We observe that it suffices to show Proposition 10 since Proposition 10 implies Propositions 7 and 9; for instance, statement (1) of Proposition 7 is implied as follows. Conjecture 3 is assumed to be true, that is, Conjecture 3 works for every positive integer n n, and we use Proposition 10 and obtain that Conjecture 2 works for every positive integer n n, and thus, Conjecture 2 is true as desired.

In the remainder of this section, we prove Proposition 10.

###### Proof of Proposition 10.

For the sake of brewity, we let M ⁡ ( ℱ) M(\mathcal{F}) denote the largest set of a finite union-closed family ℱ \mathcal{F}. We let n n be an arbitrary positive integer, and we fix n n and show statements (1), (2), …, (7).

We start by showing statement (1), that is, we assume that Conjecture 3 works for n n and show that Conjecture 2 works for n n. In relation to Conjecture 2, we let ℱ 0 \mathcal{F}_{0} be an arbitrary union-closed family of sets such that | M ⁡ ( ℱ 0) | ≤ n |M(\mathcal{F}_{0})|\leq n and ∅ ∉ ℱ 0 \emptyset\not\in\mathcal{F}_{0} and precisely one element is abundant for ℱ 0 \mathcal{F}_{0}, and we let x x denote this element. Now, we reduce ℱ 0 \mathcal{F}_{0} to a twin-free family as follows. If there is a pair of twins in ℱ 0 \mathcal{F}_{0}, then we choose one of them, say b b, and remove b b from every set of ℱ 0 \mathcal{F}_{0}. We consider the modified family of sets, and we apply such removals in sequence until there are no twins in the resulting family, and we let ℱ \mathcal{F} denote this family. We observe that ℱ \mathcal{F} is a union-closed family of sets and | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ∅ ∉ ℱ \emptyset\not\in\mathcal{F}. Furthermore, the natural bijection between sets of ℱ 0 \mathcal{F}_{0} and sets of ℱ \mathcal{F} yields that x x is the only abundant element for ℱ \mathcal{F}. We note that ℱ \mathcal{F} satisfies the hypothesis of Conjecture 3. Since Conjecture 3 is assumed to work for n n, we get that ℱ \mathcal{F} is precisely the family of all sets of 2 M ⁡ ( ℱ) 2^{M(\mathcal{F})} containing x x. It follows that x x belongs to every set of the original family ℱ 0 \mathcal{F}_{0}, and thus ℱ 0 \mathcal{F}_{0} satisfies Conjecture 2. This concludes the proof of statement (1).

In order to show statement (2), we show the contrapositive statement, that is, we show that if Conjecture 4 does not work for n n, then Conjecture 2 does not work for n n. To this end, we consider a family ℱ \mathcal{F} which witnesses that Conjecture 4 does not work for n n. In particular, family ℱ \mathcal{F} is union-closed and its largest set is of size at most n n, and smallest set is of size at least 2 2, and at most one element is abundant for ℱ \mathcal{F}. We discuss two cases.

First, we suppose that precisely one element is abundant for ℱ \mathcal{F}, and we let x x be this element. We note that if x x does not belong to all sets of ℱ \mathcal{F}, then ℱ \mathcal{F} also witnesses that Conjecture 2 does not work for n n, and the desired statement follows. Hence, we can assume that x x belongs to every set of ℱ \mathcal{F}. We let S S be a smallest set of ℱ \mathcal{F}, and let ℱ ′ \mathcal{F}^{\prime} be the family obtained from ℱ \mathcal{F} by replacing S S with the set S ∖ { x } S\setminus\{x\}. We use the fact that ℱ \mathcal{F} is union-closed and observe that ℱ ′ \mathcal{F}^{\prime} is also union-closed (since for every pair of distinct sets A, B A,B of ℱ ′ \mathcal{F}^{\prime}, the set A ∪ B A\cup B contains x x and | A ∪ B | > | S | |A\cup B|>|S|). In addition, we note that | M ⁡ ( ℱ ′) | ≤ n |M(\mathcal{F}^{\prime})|\leq n and ∅ ∉ ℱ ′ \emptyset\not\in\mathcal{F}^{\prime} and x x is the only abundant element for ℱ ′ \mathcal{F}^{\prime}, but x x does not belong to each set of ℱ ′ \mathcal{F}^{\prime}. Thus, family ℱ ′ \mathcal{F}^{\prime} witnesses that Conjecture 2 does not work for n n.

Second, we suppose that no element is abundant for ℱ \mathcal{F}. We choose an element y y of M ⁡ ( ℱ) M(\mathcal{F}) and modify ℱ \mathcal{F} as follows. For every set A A of ℱ \mathcal{F} such that the set A ∪ { y } A\cup\{y\} does not belong to ℱ \mathcal{F}, we remove A A from ℱ \mathcal{F} and add A ∪ { y } A\cup\{y\} to ℱ \mathcal{F}, and we let ℱ + \mathcal{F}^{+} denote the resulting family. Clearly, | M ⁡ ( ℱ +) | ≤ n |M(\mathcal{F}^{+})|\leq n, and we observe that ℱ + \mathcal{F}^{+} is union-closed. Furthermore, we use the natural bijection between sets of ℱ \mathcal{F} and sets of ℱ + \mathcal{F}^{+} and note that | ℱ | = | ℱ + | |\mathcal{F}|=|\mathcal{F}^{+}| and that for every element of M ⁡ ( ℱ) ∖ { y } M(\mathcal{F})\setminus\{y\}, the number of its occurrences in ℱ \mathcal{F} is equal to the number of occurrences in ℱ + \mathcal{F}^{+}. We let c c be the number of occurrences of y y in ℱ + \mathcal{F}^{+} and we observe that c ≥ 1 2 ​ | ℱ + | c\geq\frac{1}{2}|\mathcal{F}^{+}|. We discuss three cases based on c c.

For the case that c = 1 2 ​ | ℱ + | c=\frac{1}{2}|\mathcal{F}^{+}|, we use the fact that a smallest set of ℱ + \mathcal{F}^{+} is of size at least 2 2 and consider the family ℱ ′ \mathcal{F}^{\prime} obtained from ℱ + \mathcal{F}^{+} by adding the set { y } \{y\}. We observe that ℱ ′ \mathcal{F}^{\prime} is union-closed and conclude that ℱ ′ \mathcal{F}^{\prime} witnesses that Conjecture 2 does not work for n n.

For the case that | ℱ + | > c > 1 2 ​ | ℱ + | |\mathcal{F}^{+}|>c>\frac{1}{2}|\mathcal{F}^{+}|, we note that family ℱ + \mathcal{F}^{+} witnesses that Conjecture 2 does not work for n n.

For the case that c = | ℱ + | c=|\mathcal{F}^{+}|, we let S S be a smallest set of ℱ + \mathcal{F}^{+} and we modify ℱ + \mathcal{F}^{+} as follows. We use the fact that | S | ≥ 2 |S|\geq 2 and let ℱ ′ \mathcal{F}^{\prime} be the family obtained from ℱ + \mathcal{F}^{+} by replacing S S with S ∖ { y } S\setminus\{y\}. We observe that ℱ ′ \mathcal{F}^{\prime} is union-closed. Thus, ℱ ′ \mathcal{F}^{\prime} witnesses that Conjecture 2 does not work for n n which concludes the proof of statement (2).

In order to show statement (3), we let ℱ \mathcal{F} be a union-closed family of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ∅ ∉ ℱ \emptyset\not\in\mathcal{F}, and we discuss two cases.

For the case that a smallest set of ℱ \mathcal{F} is of size at least 2 2, we use that Conjecture 4 is assumed to work for n n and conclude that some element is abundant for ℱ \mathcal{F}, and thus ℱ \mathcal{F} satisfies Conjecture 1.

For the case that a smallest set of ℱ \mathcal{F} is of size 1 1, we use a simple idea of [17] as follows. We let { x } \{x\} be a smallest set of ℱ \mathcal{F} and show that x x is abundant for ℱ \mathcal{F}. We consider a set A A of ℱ \mathcal{F} such that x x does not belong to A A, and we note that the set A ∪ { x } A\cup\{x\} belongs to ℱ \mathcal{F} (since ℱ \mathcal{F} is union-closed). For each such set A A, the set A ∪ { x } A\cup\{x\} is unique and distinct from { x } \{x\}, and hence the number of sets containing x x is greater than the number of sets not containing x x. Thus, x x is abundant for ℱ \mathcal{F}, and ℱ \mathcal{F} satisfies Conjecture 1.

For statement (4), we need to show two implications. First, we show that if Conjecture 1 works for n n, then Conjecture A works for n n. We let ℱ \mathcal{F} be a union-closed family of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}. We let ℱ ′ = ℱ ∖ ∅ \mathcal{F}^{\prime}=\mathcal{F}\setminus\emptyset and we use that Conjecture 1 is assumed to work for n n and note that ℱ ′ \mathcal{F}^{\prime} has an abundant element, and we let x x be this element and c c be the number of sets of ℱ ′ \mathcal{F}^{\prime} containing x x. In particular, c > 1 2 ​ | ℱ ′ | c>\frac{1}{2}|\mathcal{F}^{\prime}| and we use the fact that c c and | ℱ ′ | |\mathcal{F}^{\prime}| are integers and obtain 2 ​ c ≥ | ℱ ′ | + 1 ≥ | ℱ | 2c\geq|\mathcal{F}^{\prime}|+1\geq|\mathcal{F}|. Hence, c ≥ 1 2 ​ | ℱ | c\geq\frac{1}{2}|\mathcal{F}| and it follows that x x belongs to at least half of the sets of ℱ \mathcal{F}.

Second, we show that if Conjecture A works for n n, then Conjecture 1 works for n n. We let ℱ \mathcal{F} be a union-closed family of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ∅ ∉ ℱ \emptyset\not\in\mathcal{F}. We let ℱ ′ = ℱ ∪ ∅ \mathcal{F}^{\prime}=\mathcal{F}\cup\emptyset and use that Conjecture A is assumed to work for n n. We conclude some element belongs to at least half of the sets of ℱ ′ \mathcal{F}^{\prime}, and thus this element belongs to more than half of the sets of ℱ \mathcal{F}.

In order to prove statement (5), we first show that if Conjecture 2 works for n n, then Conjecture B works for n n. To this end, we consider a union-closed family ℱ \mathcal{F} of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and such that precisely one element of M ⁡ ( ℱ) M(\mathcal{F}) belongs to at least half of the sets of ℱ \mathcal{F}; and we let x x be this element. We let ℱ ′ = ℱ ∖ ∅ \mathcal{F}^{\prime}=\mathcal{F}\setminus\emptyset (possibly ℱ ′ = ℱ \mathcal{F}^{\prime}=\mathcal{F} if ∅ ∉ ℱ \emptyset\not\in\mathcal{F}). We consider an arbitrary element a a of M ⁡ ( ℱ ′) ∖ { x } M(\mathcal{F}^{\prime})\setminus\{x\} and show that a a is not abundant for ℱ ′ \mathcal{F}^{\prime}. We let c c be the number of occurrences of a a in ℱ ′ \mathcal{F}^{\prime} and note that c < 1 2 ​ | ℱ | c<\frac{1}{2}|\mathcal{F}|, and hence 2 ​ c ≤ | ℱ | − 1 ≤ | ℱ ′ | 2c\leq|\mathcal{F}|-1\leq|\mathcal{F}^{\prime}|, and thus c ≤ 1 2 ​ | ℱ ′ | c\leq\frac{1}{2}|\mathcal{F}^{\prime}| as desired. On the other hand since Conjecture 2 is assumed to work for n n, we can use statements (2) and (3) of Proposition 10 and obtain that Conjecture 1 works for n n, and this yields that ℱ ′ \mathcal{F}^{\prime} has at least one abundant element. It follows that x x is the only abundant element for ℱ ′ \mathcal{F}^{\prime}. We use that Conjecture 2 works for n n and conclude that x x belongs to each set of ℱ ′ \mathcal{F}^{\prime}, and thus x x belongs to each non-empty set of ℱ \mathcal{F}.

Now, we show that if Conjecture B works for n n, then Conjecture 2 works for n n. We let ℱ \mathcal{F} be a union-closed family of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ∅ ∉ ℱ \emptyset\not\in\mathcal{F} and let x x be the only abundant element for ℱ \mathcal{F}. We let ℱ ′ = ℱ ∪ ∅ \mathcal{F}^{\prime}=\mathcal{F}\cup\emptyset and note that x x is the only element which belongs to at least half of the sets of ℱ ′ \mathcal{F}^{\prime}. We conclude that x x belongs of each non-empty set of ℱ ′ \mathcal{F}^{\prime}, and thus to every set of ℱ \mathcal{F}.

In order to prove the first implication of statement (6), we consider a union-closed family ℱ \mathcal{F} which satisfies the following.

- •

| M ⁡ ( ℱ) | ≤ n. |M(\mathcal{F})|\leq n.

- •

There are no twins in ℱ \mathcal{F}.

- •

Precisely one element of M ⁡ ( ℱ) M(\mathcal{F}) belongs to at least half of the sets of ℱ \mathcal{F}, and we let x x be this element.

Clearly, the desired statement holds if | M ⁡ ( ℱ) | ≤ 1 |M(\mathcal{F})|\leq 1. Hence, we can assume that | M ⁡ ( ℱ) | ≥ 2 |M(\mathcal{F})|\geq 2. We let ℱ ′ = ℱ ∖ ∅ \mathcal{F}^{\prime}=\mathcal{F}\setminus\emptyset, and we note that ℱ ′ \mathcal{F}^{\prime} has no twins and | M ⁡ ( ℱ ′) | ≤ n |M(\mathcal{F}^{\prime})|\leq n. We use a similar argument as in the proof of (5) and obtain that x x is the only abundant element for ℱ ′ \mathcal{F}^{\prime}. Since Conjecture 3 works for n n, we get that ℱ ′ \mathcal{F}^{\prime} consists of precisely all sets of 2 M ⁡ ( ℱ ′) 2^{M(\mathcal{F}^{\prime})} containing x x. Finally, we use that ℱ ′ = ℱ ∖ ∅ \mathcal{F}^{\prime}=\mathcal{F}\setminus\emptyset and | M ⁡ ( ℱ) | ≥ 2 |M(\mathcal{F})|\geq 2 and that precisely one element of M ⁡ ( ℱ) M(\mathcal{F}) belongs to at least half of the sets of ℱ \mathcal{F}, and we conclude that ℱ \mathcal{F} consists of the empty set and precisely all sets of 2 M ⁡ ( ℱ) 2^{M(\mathcal{F})} containing x x.

For the reverse implication, we let ℱ \mathcal{F} be a union-closed family of sets such that | M ⁡ ( ℱ) | ≤ n |M(\mathcal{F})|\leq n and ∅ ∉ ℱ \emptyset\not\in\mathcal{F} and such that there are no twins in ℱ \mathcal{F} and precisely one element is abundant for ℱ \mathcal{F}; and we let x x be this element. Clearly, if | M ⁡ ( ℱ) | ≤ 1 |M(\mathcal{F})|\leq 1 then ℱ \mathcal{F} satisfies Conjecture 3. Hence, we can assume that | M ⁡ ( ℱ) | ≥ 2 |M(\mathcal{F})|\geq 2. We let ℱ ′ = ℱ ∪ ∅ \mathcal{F}^{\prime}=\mathcal{F}\cup\emptyset and note that x x is the only element which belongs to at least half of the sets of ℱ ′ \mathcal{F}^{\prime}. Thus, ℱ ′ \mathcal{F}^{\prime} consists of the empty set and precisely all sets of 2 M ⁡ ( ℱ ′) 2^{M(\mathcal{F}^{\prime})} containing x x. It follows that ℱ \mathcal{F} consists of precisely all sets of 2 M ⁡ ( ℱ) 2^{M(\mathcal{F})} containing x x.

Finally, we show statement (7). The proof is similar to the proof of (4). We let ℱ \mathcal{F} be a union-closed family of sets whose largest set is of size at most n n and smallest non-empty set is of size at least 2 2. We let ℱ ′ = ℱ ∖ ∅ \mathcal{F}^{\prime}=\mathcal{F}\setminus\emptyset and use that Conjecture 4 is assumed to work for n n. If follows that at least two elements of M ⁡ ( ℱ ′) M(\mathcal{F}^{\prime}) belong to more than half of the sets of ℱ ′ \mathcal{F}^{\prime}, and thus belong to at least half of the sets of ℱ \mathcal{F}.

For the reverse implication, we let ℱ \mathcal{F} be a union-closed family of sets whose largest set is of size at most n n and smallest set is of size at least 2 2. We consider the family ℱ ∪ ∅ \mathcal{F}\cup\emptyset and use a similar argument, and we conclude that at least two elements are abundant for ℱ \mathcal{F}. ∎

## Acknowledgement

We thank Stijn Cambie for his suggestion on extending the constructions 𝒫 3 8 \mathcal{P}^{8}_{3} and 𝒫 4 12 \mathcal{P}^{12}_{4} to 𝒫 k n \mathcal{P}^{n}_{k}.

## References

- [1] R. Alweiss, B. Huang and M. Sellke: Improved Lower Bound for the Union-Closed Sets Conjecture, arXiv:2211.11731 (2022).
- [2] I. Balla, B. Bollobás and T. Eccles: Union-closed families of sets, Journal of Combinatorial Theory, Series A 120 (2013), 531–544.
- [3] I. Bošnjak and P. Marković: The 11 11 -element case of Frankl’s conjecture, European Journal of Combinatorics 15 (2008), R88.
- [4] H. Bruhn and O. Schaudt: The journey of the union-closed sets conjecture, Graphs and Combinatorics 31 (2015), 2043–2074.
- [5] H. Bruhn, P. Charbit, O. Schaudt and J. A. Telle: The graph formulation of the union-closed sets conjecture, European Journal of Combinatorics 43 (2015), 210–219.
- [6] S. Cambie: Better bounds for the union-closed sets conjecture using the entropy approach, arXiv:2212.12500 (2022).
- [7] Z. Chase and S. Lovett: Approximate union closed conjecture, arXiv:2211.11689 (2022).
- [8] Z. Cui and Z. Hu: Two stronger versions of the union-closed sets conjecture, arXiv:1711.04276 (2019).
- [9] G. Lo Faro: Union-closed sets conjecture: improved bounds, Journal of Combinatorial Mathematics and Combinatorial Computing 16 (1994), 97–102.
- [10] J. Gilmer: A constant lower bound for the union-closed sets conjecture, arXiv:2211.09055 (2022).
- [11] P. Frankl: Extremal set systems, Handbook of combinatorics, Elsevier (1995), 1293–1329.
- [12] P. Marković: An attempt at Frankl’s conjecture, Publications de l’Institut Mathématique 81 (2007), 29–43.
- [13] R. Morris: FC-families and improved bounds for Frankl’s conjecture, European Journal of Combinatorics 27 (2006), 269–282.
- [14] L. Pebody: Extension of a Method of Gilmer, arXiv:2211.13139 (2022).
- [15] B. Poonen: Union-closed families, Journal of Combinatorial Theory, Series A 59 (1992), 253–268.
- [16] W. Sawin: An improved lower bound for the union-closed set conjecture, arXiv:2211.11504 (2022).
- [17] D. G. Sarvate and J.-C. Renaud: On the union-closed sets conjecture, Ars Combinatorica 27 (1989), 149–154.
- [18] B. Vučković and M. Živković: The 12 12 -element case of Frankl’s conjecture, IPSI BgD Transactions on Internet Research 13 (2017), 65–71.
- [19] P. Wójcik: Union-closed families of sets, Discrete Mathematics 199 (1999), 173–182.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
