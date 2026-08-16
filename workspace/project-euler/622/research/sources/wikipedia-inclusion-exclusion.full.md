<!-- source: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle | converted from HTML -->

Inclusion–exclusion principle - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Counting technique in combinatorics

[1] [Venn diagram][2] showing the union of sets A and B as everything not in white

In [combinatorics][3], the **inclusion–exclusion principle**(commonly referred to as **PIE**) is a counting technique which generalizes the familiar method of obtaining the number of elements in the [union][4] of two [finite sets][5]; symbolically expressed as | A ∪ B | = | A | + | B | − | A ∩ B | {\displaystyle |A\cup B|=|A|+|B|-|A\cap B|}[image: {\displaystyle |A\cup B|=|A|+|B|-|A\cap B|}] where A and B are two finite sets and |*S*| indicates the [cardinality][6] of a set S (which may be considered as the number of elements of the set, if the set is [finite][5]). The formula expresses the fact that the sum of the sizes of the two sets may be too large since some elements may be counted twice. The double-counted elements are those in the [intersection][7] of the two sets and the count is corrected by subtracting the size of the intersection.

The inclusion-exclusion principle, being a generalization of the two-set case, is perhaps more clearly seen in the case of three sets, which for the sets A, B and C is given by | A ∪ B ∪ C | = | A | + | B | + | C | − | A ∩ B | − | A ∩ C | − | B ∩ C | + | A ∩ B ∩ C | {\displaystyle |A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|}[image: {\displaystyle |A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|}] This formula can be verified by counting how many times each region in the [Venn diagram][2] figure is included in the right-hand side of the formula. In this case, when removing the contributions of over-counted elements, the number of elements in the mutual intersection of the three sets has been subtracted too often, so must be added back in to get the correct total.

[8] Inclusion–exclusion illustrated by a Venn diagram for three sets

Generalizing the results of these examples gives the principle of inclusion–exclusion. To find the cardinality of the union of n sets:

1. Include the cardinalities of the sets.
2. Exclude the cardinalities of the pairwise intersections.
3. Include the cardinalities of the triple-wise intersections.
4. Exclude the cardinalities of the quadruple-wise intersections.
5. Include the cardinalities of the quintuple-wise intersections.
6. Continue, until the cardinality of the n -tuple-wise intersection is included (if n is odd) or excluded ( n even).

The name comes from the idea that the principle is based on over-generous *inclusion*, followed by compensating *exclusion*. This concept is attributed to [Abraham de Moivre][9] (1718), [1] although it first appears in a paper of [Daniel da Silva][10] (1854) [2] and later in a paper by [J. J. Sylvester][11] (1883). [3] Sometimes the principle is referred to as the formula of Da Silva or Sylvester, due to these publications. The principle can be viewed as an example of the [sieve method][12] extensively used in [number theory][13] and is sometimes referred to as the *sieve formula*. [4]

As finite probabilities are computed as counts relative to the cardinality of the [probability space][14], the formulas for the principle of inclusion–exclusion remain valid when the cardinalities of the sets are replaced by finite probabilities. More generally, both versions of the principle can be put under the common umbrella of [measure theory][15].

In a very abstract setting, the principle of inclusion–exclusion can be expressed as the calculation of the inverse of a certain matrix. [5] This inverse has a special structure, making the principle an extremely valuable technique in combinatorics and related areas of mathematics. As [Gian-Carlo Rota][16] put it: [6]

"One of the most useful principles of enumeration in discrete probability and combinatorial theory is the celebrated principle of inclusion–exclusion. When skillfully applied, this principle has yielded the solution to many a combinatorial problem."

## Formula

[[edit][17]]

In its general formula, the principle of inclusion–exclusion states that for finite sets 1</sub>, ..., ''A<sub>n</sub>''"}},"i":0}}]}'>*A*1, ..., *A n*, one has the identity

\\left|\\bigcup_{i=1}^n A_i\\right| = \\sum_{i=1}^n |A_i| - \\sum_{1 \\leqslant i < j \\leqslant n} |A_i\\cap A_j| + \\sum_{1 \\leqslant i < j < k \\leqslant n} |A_i \\cap A_j\\cap A_k| - \\cdots + (-1)^{n+1} \\left|A_1\\cap\\cdots\\cap A_n\\right|.</math>"},"3":{"wt":"{{EquationRef|1}}"}},"i":0}}]}'>

| ⋃ i = 1 n A i | = ∑ i = 1 n | A i | − ∑ 1 ⩽ i < j ⩽ n | A i ∩ A j | + ∑ 1 ⩽ i < j < k ⩽ n | A i ∩ A j ∩ A k | − ⋯ + ( − 1) n + 1 | A 1 ∩ ⋯ ∩ A n |. {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{i=1}^{n}|A_{i}|-\sum _{1\leqslant i<j\leqslant n}|A_{i}\cap A_{j}|+\sum _{1\leqslant i<j<k\leqslant n}|A_{i}\cap A_{j}\cap A_{k}|-\cdots +(-1)^{n+1}\left|A_{1}\cap \cdots \cap A_{n}\right|.}[image: {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{i=1}^{n}|A_{i}|-\sum _{1\leqslant i<j\leqslant n}|A_{i}\cap A_{j}|+\sum _{1\leqslant i<j<k\leqslant n}|A_{i}\cap A_{j}\cap A_{k}|-\cdots +(-1)^{n+1}\left|A_{1}\cap \cdots \cap A_{n}\right|.}] |  | 1 |

[18] Each term of the inclusion–exclusion formula gradually corrects the count until finally each portion of the [Venn diagram][2] is counted exactly once.

This can be compactly written as | ⋃ i = 1 n A i | = ∑ k = 1 n ( − 1) k + 1 ( ∑ 1 ⩽ i 1 < ⋯ < i k ⩽ n | A i 1 ∩ ⋯ ∩ A i k |) {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{k=1}^{n}(-1)^{k+1}\left(\sum _{1\leqslant i_{1}<\cdots <i_{k}\leqslant n}\left|A_{i_{1}}\cap \cdots \cap A_{i_{k}}\right|\right)}[image: {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{k=1}^{n}(-1)^{k+1}\left(\sum _{1\leqslant i_{1}<\cdots <i_{k}\leqslant n}\left|A_{i_{1}}\cap \cdots \cap A_{i_{k}}\right|\right)}] or | ⋃ i = 1 n A i | = ∑ ∅ ≠ J ⊆ { 1, …, n } ( − 1) | J | + 1 | ⋂ j ∈ J A j |. {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{\emptyset \neq J\subseteq \{1,\ldots ,n\}}(-1)^{|J|+1}\left|\bigcap _{j\in J}A_{j}\right|.}[image: {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{\emptyset \neq J\subseteq \{1,\ldots ,n\}}(-1)^{|J|+1}\left|\bigcap _{j\in J}A_{j}\right|.}]

In words, to count the number of elements in a finite union of finite sets, first sum the cardinalities of the individual sets, then subtract the number of elements that appear in at least two sets, then add back the number of elements that appear in at least three sets, then subtract the number of elements that appear in at least four sets, and so on. This process always ends since there can be no elements that appear in more than the number of sets in the union. (For example, if n = 4, {\displaystyle n=4,}[image: {\displaystyle n=4,}] there can be no elements that appear in more than 4 {\displaystyle 4}[image: {\displaystyle 4}] sets; equivalently, there can be no elements that appear in at least 5 {\displaystyle 5}[image: {\displaystyle 5}] sets.)

In applications it is common to see the principle expressed in its complementary form. That is, letting S be a finite [universal set][19] containing all of the i</sub>''"}},"i":0}}]}'>*A i*and letting A i ¯ {\displaystyle {\overline {A_{i}}}}[image: {\displaystyle {\overline {A_{i}}}}] denote the complement of i</sub>''"}},"i":0}}]}'>*A i*in S, by [De Morgan's laws][20] we have | ⋂ i = 1 n A i ¯ | = | S − ⋃ i = 1 n A i | = | S | − ∑ i = 1 n | A i | + ∑ 1 ⩽ i < j ⩽ n | A i ∩ A j | − ⋯ + ( − 1) n | A 1 ∩ ⋯ ∩ A n |. {\displaystyle \left|\bigcap _{i=1}^{n}{\overline {A_{i}}}\right|=\left|S-\bigcup _{i=1}^{n}A_{i}\right|=|S|-\sum _{i=1}^{n}|A_{i}|+\sum _{1\leqslant i<j\leqslant n}|A_{i}\cap A_{j}|-\cdots +(-1)^{n}|A_{1}\cap \cdots \cap A_{n}|.}[image: {\displaystyle \left|\bigcap _{i=1}^{n}{\overline {A_{i}}}\right|=\left|S-\bigcup _{i=1}^{n}A_{i}\right|=|S|-\sum _{i=1}^{n}|A_{i}|+\sum _{1\leqslant i<j\leqslant n}|A_{i}\cap A_{j}|-\cdots +(-1)^{n}|A_{1}\cap \cdots \cap A_{n}|.}]

As another variant of the statement, let 1</sub>, ..., ''P<sub>n</sub>''"}},"i":0}}]}'>*P*1, ..., *P n*be a list of properties that elements of a set S may or may not have, then the principle of inclusion–exclusion provides a way to calculate the number of elements of S that have none of the properties. Just let i</sub>''"}},"i":0}}]}'>*A i*be the subset of elements of S which have the property i</sub>''"}},"i":0}}]}'>*P i*and use the principle in its complementary form. This variant is due to [J. J. Sylvester][11]. [1]

Notice that if you take into account only the first *m<n*sums on the right (in the general form of the principle), then you will get an overestimate if *m*is odd and an underestimate if *m*is even.

## Examples

[[edit][21]]

### Counting derangements

[[edit][22]]

A more complex example is the following.

Suppose there is a deck of n cards numbered from 1 to n. Suppose a card numbered m is in the correct position if it is the m th card in the deck. How many ways, W, can the cards be shuffled with at least 1 card being in the correct position?

Begin by defining set ''m''</sub>"}},"i":0}}]}'>*A**m*, which is all of the orderings of cards with the m th card correct. Then the number of orders, W, with *at least*one card being in the correct position, m, is W = | ⋃ m = 1 n A m |. {\displaystyle W=\left|\bigcup _{m=1}^{n}A_{m}\right|.}[image: {\displaystyle W=\left|\bigcup _{m=1}^{n}A_{m}\right|.}]

Apply the principle of inclusion–exclusion, W = ∑ m 1 = 1 n | A m 1 | − ∑ 1 ⩽ m 1 < m 2 ⩽ n | A m 1 ∩ A m 2 | + ⋯ + ( − 1) p − 1 ∑ 1 ⩽ m 1 < ⋯ < m p ⩽ n | A m 1 ∩ ⋯ ∩ A m p | + ⋯ {\displaystyle W=\sum _{m_{1}=1}^{n}\left|A_{m_{1}}\right|-\sum _{1\leqslant m_{1}<m_{2}\leqslant n}\left|A_{m_{1}}\cap A_{m_{2}}\right|+\cdots +(-1)^{p-1}\sum _{1\leqslant m_{1}<\cdots <m_{p}\leqslant n}\left|A_{m_{1}}\cap \cdots \cap A_{m_{p}}\right|+\cdots }[image: {\displaystyle W=\sum _{m_{1}=1}^{n}\left|A_{m_{1}}\right|-\sum _{1\leqslant m_{1}<m_{2}\leqslant n}\left|A_{m_{1}}\cap A_{m_{2}}\right|+\cdots +(-1)^{p-1}\sum _{1\leqslant m_{1}<\cdots <m_{p}\leqslant n}\left|A_{m_{1}}\cap \cdots \cap A_{m_{p}}\right|+\cdots }]

Each value A m 1 ∩ ⋯ ∩ A m p {\displaystyle A_{m_{1}}\cap \cdots \cap A_{m_{p}}}[image: {\displaystyle A_{m_{1}}\cap \cdots \cap A_{m_{p}}}] represents the set of shuffles having at least p values 1</sub>,&nbsp;...,&nbsp;''m<sub>p</sub>''"}},"i":0}}]}'>*m*1,...,*m p*in the correct position. Note that the number of shuffles with at least p values correct only depends on p, not on the particular values of m {\displaystyle m}[image: {\displaystyle m}]. For example, the number of shuffles having the 1st, 3rd, and 17th cards in the correct position is the same as the number of shuffles having the 2nd, 5th, and 13th cards in the correct positions. It only matters that of the n cards, 3 were chosen to be in the correct position. Thus there are ( n p) {\textstyle {n \choose p}}[image: {\textstyle {n \choose p}}] equal terms in the p th summation (see [combination][23]).

W = ( n 1) | A 1 | − ( n 2) | A 1 ∩ A 2 | + ⋯ + ( − 1) p − 1 ( n p) | A 1 ∩ ⋯ ∩ A p | + ⋯ {\displaystyle W={n \choose 1}|A_{1}|-{n \choose 2}|A_{1}\cap A_{2}|+\cdots +(-1)^{p-1}{n \choose p}|A_{1}\cap \cdots \cap A_{p}|+\cdots }[image: {\displaystyle W={n \choose 1}|A_{1}|-{n \choose 2}|A_{1}\cap A_{2}|+\cdots +(-1)^{p-1}{n \choose p}|A_{1}\cap \cdots \cap A_{p}|+\cdots }]

| A 1 ∩ ⋯ ∩ A p | {\displaystyle |A_{1}\cap \cdots \cap A_{p}|}[image: {\displaystyle |A_{1}\cap \cdots \cap A_{p}|}] is the number of orderings having p elements in the correct position, which is equal to the number of ways of ordering the remaining *n*−*p*elements, or (*n*−*p*)!. Thus we finally get: W = ( n 1) ( n − 1)! − ( n 2) ( n − 2)! + ⋯ + ( − 1) p − 1 ( n p) ( n − p)! + ⋯ = ∑ p = 1 n ( − 1) p − 1 ( n p) ( n − p)! = ∑ p = 1 n ( − 1) p − 1 n! p! ( n − p)! ( n − p)! = ∑ p = 1 n ( − 1) p − 1 n! p! {\displaystyle {\begin{aligned}W&={n \choose 1}(n-1)!-{n \choose 2}(n-2)!+\cdots +(-1)^{p-1}{n \choose p}(n-p)!+\cdots \\&=\sum _{p=1}^{n}(-1)^{p-1}{n \choose p}(n-p)!\\&=\sum _{p=1}^{n}(-1)^{p-1}{\frac {n!}{p!(n-p)!}}(n-p)!\\&=\sum _{p=1}^{n}(-1)^{p-1}{\frac {n!}{p!}}\end{aligned}}}[image: {\displaystyle {\begin{aligned}W&={n \choose 1}(n-1)!-{n \choose 2}(n-2)!+\cdots +(-1)^{p-1}{n \choose p}(n-p)!+\cdots \\&=\sum _{p=1}^{n}(-1)^{p-1}{n \choose p}(n-p)!\\&=\sum _{p=1}^{n}(-1)^{p-1}{\frac {n!}{p!(n-p)!}}(n-p)!\\&=\sum _{p=1}^{n}(-1)^{p-1}{\frac {n!}{p!}}\end{aligned}}}]

A permutation where *no*card is in the correct position is called a [derangement][24]. Taking *n*! to be the total number of permutations, the probability Q that a random shuffle produces a derangement is given by Q = 1 − W n! = ∑ p = 0 n ( − 1) p p!, {\displaystyle Q=1-{\frac {W}{n!}}=\sum _{p=0}^{n}{\frac {(-1)^{p}}{p!}},}[image: {\displaystyle Q=1-{\frac {W}{n!}}=\sum _{p=0}^{n}{\frac {(-1)^{p}}{p!}},}] a truncation to *n*+ 1 terms of the [Taylor expansion][25] of −1</sup>"}},"i":0}}]}'>*e*−1. Thus the probability of guessing an order for a shuffled deck of cards and being incorrect about every card is approximately −1</sup>"}},"i":0}}]}'>*e*−1 or 37%.

## A special case

[[edit][26]]

The situation that appears in the derangement example above occurs often enough to merit special attention. [7] Namely, when the size of the intersection sets appearing in the formulas for the principle of inclusion–exclusion depend only on the number of sets in the intersections and not on which sets appear. More formally, if the intersection A J:= ⋂ j ∈ J A j {\displaystyle A_{J}:=\bigcap _{j\in J}A_{j}}[image: {\displaystyle A_{J}:=\bigcap _{j\in J}A_{j}}] has the same cardinality, say k</sub>'' = {{abs|''A<sub>J</sub>''}}"}},"i":0}}]}'>*α k*= |*A J*|, for every k -element subset J of {1,...,*n*}, then | ⋃ i = 1 n A i | = ∑ k = 1 n ( − 1) k − 1 ( n k) α k. {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}\alpha _{k}.}[image: {\displaystyle \left|\bigcup _{i=1}^{n}A_{i}\right|=\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}\alpha _{k}.}]

Or, in the complementary form, where the universal set S has cardinality 0</sub>"}},"i":0}}]}'>*α*0, | S ∖ ⋃ i = 1 n A i | = α 0 − ∑ k = 1 n ( − 1) k − 1 ( n k) α k = ∑ k = 0 n ( − 1) k ( n k) α k. {\displaystyle {\begin{aligned}\left|S\smallsetminus \bigcup _{i=1}^{n}A_{i}\right|&=\alpha _{0}-\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}\alpha _{k}\\&=\sum _{k=0}^{n}(-1)^{k}{\binom {n}{k}}\alpha _{k}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}\left|S\smallsetminus \bigcup _{i=1}^{n}A_{i}\right|&=\alpha _{0}-\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}\alpha _{k}\\&=\sum _{k=0}^{n}(-1)^{k}{\binom {n}{k}}\alpha _{k}.\end{aligned}}}]

## Formula generalization

[[edit][27]]

Given a [family (repeats allowed) of subsets][28] 1</sub>, ''A''<sub>2</sub>, ..., ''A''<sub>''n''</sub>"}},"i":0}}]}'>*A*1, *A*2, ..., *A**n*of a universal set S, the principle of inclusion–exclusion calculates the number of elements of S in none of these subsets. A generalization of this concept would calculate the number of elements of S which appear in exactly some fixed m of these sets.

Let [</nowiki>''n''<nowiki>]</nowiki> = {{mset|1, 2, ..., ''n''}}"}},"i":0}}]}'>*N*= [*n*] = {1, 2, ..., *n*}. If we define A ∅ = S {\displaystyle A_{\emptyset }=S}[image: {\displaystyle A_{\emptyset }=S}], then the principle of inclusion–exclusion can be written as, using the notation of the previous section; the number of elements of S contained in none of the ''i''</sub>"}},"i":0}}]}'>*A**i*is: ∑ J ⊆ [n] ( − 1) | J | | A J |. {\displaystyle \sum _{J\subseteq [n]}(-1)^{|J|}|A_{J}|.}[image: {\displaystyle \sum _{J\subseteq [n]}(-1)^{|J|}|A_{J}|.}]

If I is a fixed subset of the [index set][29] N, then the number of elements which belong to ''i''</sub>"}},"i":0}}]}'>*A**i*for all i in I and for no other values is: [8] ∑ J ⊇ I ( − 1) | J | − | I | | A J |. {\displaystyle \sum _{J\supseteq I}(-1)^{|J|-|I|}|A_{J}|.}[image: {\displaystyle \sum _{J\supseteq I}(-1)^{|J|-|I|}|A_{J}|.}]

Define the sets B k = A I ∪ { k } for k ∈ N ∖ I. {\displaystyle B_{k}=A_{I\cup \{k\}}{\text{ for }}k\in N\smallsetminus I.}[image: {\displaystyle B_{k}=A_{I\cup \{k\}}{\text{ for }}k\in N\smallsetminus I.}]

We seek the number of elements in none of the ''k''</sub>"}},"i":0}}]}'>*B**k*which, by the principle of inclusion–exclusion (with B ∅ = A I {\displaystyle B_{\emptyset }=A_{I}}[image: {\displaystyle B_{\emptyset }=A_{I}}]), is ∑ K ⊆ N ∖ I ( − 1) | K | | B K |. {\displaystyle \sum _{K\subseteq N\smallsetminus I}(-1)^{|K|}|B_{K}|.}[image: {\displaystyle \sum _{K\subseteq N\smallsetminus I}(-1)^{|K|}|B_{K}|.}]

The correspondence *K*↔ *J*= *I*∪ *K*between subsets of *N*\*I*and subsets of N containing I is a bijection and if J and K correspond under this map then ''K''</sub> = ''A''<sub>''J''</sub>"}},"i":0}}]}'>*B**K*= *A**J*, showing that the result is valid.

## In probability

[[edit][30]]

In [probability][31], for events 1</sub>, ..., ''A''<sub>''n''</sub>"}},"i":0}}]}'>*A*1, ..., *A**n*in a [probability space][14] ( Ω, F, P) {\displaystyle (\Omega ,{\mathcal {F}},\mathbb {P} )}[image: {\displaystyle (\Omega ,{\mathcal {F}},\mathbb {P} )}], the inclusion–exclusion principle becomes for *n*= 2 P ( A 1 ∪ A 2) = P ( A 1) + P ( A 2) − P ( A 1 ∩ A 2), {\displaystyle \mathbb {P} (A_{1}\cup A_{2})=\mathbb {P} (A_{1})+\mathbb {P} (A_{2})-\mathbb {P} (A_{1}\cap A_{2}),}[image: {\displaystyle \mathbb {P} (A_{1}\cup A_{2})=\mathbb {P} (A_{1})+\mathbb {P} (A_{2})-\mathbb {P} (A_{1}\cap A_{2}),}] for *n*= 3 P ( A 1 ∪ A 2 ∪ A 3) = P ( A 1) + P ( A 2) + P ( A 3) − P ( A 1 ∩ A 2) − P ( A 1 ∩ A 3) − P ( A 2 ∩ A 3) + P ( A 1 ∩ A 2 ∩ A 3) {\displaystyle \mathbb {P} (A_{1}\cup A_{2}\cup A_{3})=\mathbb {P} (A_{1})+\mathbb {P} (A_{2})+\mathbb {P} (A_{3})-\mathbb {P} (A_{1}\cap A_{2})-\mathbb {P} (A_{1}\cap A_{3})-\mathbb {P} (A_{2}\cap A_{3})+\mathbb {P} (A_{1}\cap A_{2}\cap A_{3})}[image: {\displaystyle \mathbb {P} (A_{1}\cup A_{2}\cup A_{3})=\mathbb {P} (A_{1})+\mathbb {P} (A_{2})+\mathbb {P} (A_{3})-\mathbb {P} (A_{1}\cap A_{2})-\mathbb {P} (A_{1}\cap A_{3})-\mathbb {P} (A_{2}\cap A_{3})+\mathbb {P} (A_{1}\cap A_{2}\cap A_{3})}] and in general P ( ⋃ i = 1 n A i) = ∑ i = 1 n P ( A i) − ∑ i < j P ( A i ∩ A j) + ∑ i < j < k P ( A i ∩ A j ∩ A k) + ⋯ + ( − 1) n − 1 P ( ⋂ i = 1 n A i), {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{i=1}^{n}\mathbb {P} (A_{i})-\sum _{i<j}\mathbb {P} (A_{i}\cap A_{j})+\sum _{i<j<k}\mathbb {P} (A_{i}\cap A_{j}\cap A_{k})+\cdots +(-1)^{n-1}\mathbb {P} \left(\bigcap _{i=1}^{n}A_{i}\right),}[image: {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{i=1}^{n}\mathbb {P} (A_{i})-\sum _{i<j}\mathbb {P} (A_{i}\cap A_{j})+\sum _{i<j<k}\mathbb {P} (A_{i}\cap A_{j}\cap A_{k})+\cdots +(-1)^{n-1}\mathbb {P} \left(\bigcap _{i=1}^{n}A_{i}\right),}] which can be written in closed form as P ( ⋃ i = 1 n A i) = ∑ k = 1 n ( ( − 1) k − 1 ∑ I ⊆ { 1, …, n } | I | = k P ( A I)), {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}\left((-1)^{k-1}\sum _{I\subseteq \{1,\ldots ,n\} \atop |I|=k}\mathbb {P} (A_{I})\right),}[image: {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}\left((-1)^{k-1}\sum _{I\subseteq \{1,\ldots ,n\} \atop |I|=k}\mathbb {P} (A_{I})\right),}] where the last sum runs over all subsets I of the indices 1, ..., *n*which contain exactly k elements, and A I:= ⋂ i ∈ I A i {\displaystyle A_{I}:=\bigcap _{i\in I}A_{i}}[image: {\displaystyle A_{I}:=\bigcap _{i\in I}A_{i}}] denotes the intersection of all those i</sub>''"}},"i":0}}]}'>*A i*with index in I.

According to the [Bonferroni inequalities][32], the sum of the first terms in the formula is alternately an upper bound and a lower bound for the [LHS][33]. This can be used in cases where the full formula is too cumbersome.

For a general [measure space][34] (*S*, Σ, *μ*) and [measurable][35] subsets 1</sub>, ..., ''A''<sub>''n''</sub>"}},"i":0}}]}'>*A*1, ..., *A**n*of [finite measure][36], the above identities also hold when the probability measure P {\displaystyle \mathbb {P} }[image: {\displaystyle \mathbb {P} }] is replaced by the measure μ.

### Special case

[[edit][37]]

If, in the probabilistic version of the inclusion–exclusion principle, the probability of the intersection ''I''</sub>"}},"i":0}}]}'>*A**I*only depends on the cardinality of I, meaning that for every k in {1,...,*n*} there is an k</sub>''"}},"i":0}}]}'>*a k*such that a k = P ( A I) for every I ⊂ { 1, …, n } with | I | = k, {\displaystyle a_{k}=\mathbb {P} (A_{I}){\text{ for every }}I\subset \{1,\ldots ,n\}{\text{ with }}|I|=k,}[image: {\displaystyle a_{k}=\mathbb {P} (A_{I}){\text{ for every }}I\subset \{1,\ldots ,n\}{\text{ with }}|I|=k,}] then the above formula simplifies to P ( ⋃ i = 1 n A i) = ∑ k = 1 n ( − 1) k − 1 ( n k) a k {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}a_{k}}[image: {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}(-1)^{k-1}{\binom {n}{k}}a_{k}}] due to the combinatorial interpretation of the [binomial coefficient][38] ( n k) {\textstyle {\binom {n}{k}}}[image: {\textstyle {\binom {n}{k}}}]. For example, if the events A i {\displaystyle A_{i}}[image: {\displaystyle A_{i}}] are [independent and identically distributed][39], then P ( A i) = p {\displaystyle \mathbb {P} (A_{i})=p}[image: {\displaystyle \mathbb {P} (A_{i})=p}] for all i, and we have a k = p k {\displaystyle a_{k}=p^{k}}[image: {\displaystyle a_{k}=p^{k}}], in which case the expression above simplifies to P ( ⋃ i = 1 n A i) = 1 − ( 1 − p) n. {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=1-(1-p)^{n}.}[image: {\displaystyle \mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=1-(1-p)^{n}.}]

(This result can also be derived more simply by considering the intersection of the complements of the events A i {\displaystyle A_{i}}[image: {\displaystyle A_{i}}].)

An analogous simplification is possible in the case of a general measure space ( S, Σ, μ) {\displaystyle (S,\Sigma ,\mu )}[image: {\displaystyle (S,\Sigma ,\mu )}] and measurable subsets A 1, …, A n {\displaystyle A_{1},\dots ,A_{n}}[image: {\displaystyle A_{1},\dots ,A_{n}}] of finite measure.

There is another formula used in [point processes][40]. Let S {\displaystyle S}[image: {\displaystyle S}] be a finite set and P {\displaystyle P}[image: {\displaystyle P}] be a random subset of S {\displaystyle S}[image: {\displaystyle S}]. Let A {\displaystyle A}[image: {\displaystyle A}] be any subset of S {\displaystyle S}[image: {\displaystyle S}], then P ( P = A) = P ( P ⊃ A) − ∑ j 1 ∈ S ∖ A P ( P ⊃ A ∪ j 1) = + ∑ j 1, j 2 ∈ S ∖ A j 1 ≠ j 2 P ( P ⊃ A ∪ j 1, j 2) + … = + ( − 1) | S | − | A | P ( P ⊃ S) = ∑ A ⊂ J ⊂ S ( − 1) | J | − | A | P ( P ⊃ J). {\displaystyle {\begin{aligned}\mathbb {P} (P=A)&=\mathbb {P} (P\supset A)-\sum _{j_{1}\in S\setminus A}\mathbb {P} (P\supset A\cup {j_{1}})\\&{\hphantom {=}}+\sum _{j_{1},j_{2}\in S\setminus A \atop j_{1}\neq j_{2}}\mathbb {P} (P\supset A\cup {j_{1},j_{2}})+\dots \\&{\hphantom {=}}+(-1)^{|S|-|A|}\mathbb {P} (P\supset S)\\&=\sum _{A\subset J\subset S}(-1)^{|J|-|A|}\mathbb {P} (P\supset J).\end{aligned}}}[image: {\displaystyle {\begin{aligned}\mathbb {P} (P=A)&=\mathbb {P} (P\supset A)-\sum _{j_{1}\in S\setminus A}\mathbb {P} (P\supset A\cup {j_{1}})\\&{\hphantom {=}}+\sum _{j_{1},j_{2}\in S\setminus A \atop j_{1}\neq j_{2}}\mathbb {P} (P\supset A\cup {j_{1},j_{2}})+\dots \\&{\hphantom {=}}+(-1)^{|S|-|A|}\mathbb {P} (P\supset S)\\&=\sum _{A\subset J\subset S}(-1)^{|J|-|A|}\mathbb {P} (P\supset J).\end{aligned}}}]

## Other formulas

[[edit][41]]

The principle is sometimes stated in the form [9] that says that if g ( A) = ∑ S ⊆ A f ( S) {\displaystyle g(A)=\sum _{S\subseteq A}f(S)}[image: {\displaystyle g(A)=\sum _{S\subseteq A}f(S)}] then

f(A)=\\sum_{S \\subseteq A}(-1)^{|A|-|S|}g(S) </math>"},"3":{"wt":"{{EquationRef|2}}"}},"i":0}}]}'>

f ( A) = ∑ S ⊆ A ( − 1) | A | − | S | g ( S) {\displaystyle f(A)=\sum _{S\subseteq A}(-1)^{|A|-|S|}g(S)}[image: {\displaystyle f(A)=\sum _{S\subseteq A}(-1)^{|A|-|S|}g(S)}] |  | 2 |

The combinatorial and the probabilistic version of the inclusion–exclusion principle are instances of (**2**).

\\underline{m} = \\{1,2,\\ldots,m\\}</math>, <math>f(\\underline{m}) = 0</math>, and\n<math display=\"block\">f(S)=\\left|\\bigcap_{i \\in \\underline{m} \\smallsetminus S} A_i \\smallsetminus \\bigcup_{i \\in S} A_i\\right| \\text{ and } f(S) = \\mathbb{P} \\left(\\bigcap_{i \\in \\underline{m} \\smallsetminus S} A_i \\smallsetminus \\bigcup_{i \\in S} A_i\\right)</math>\nrespectively for all [[set (mathematics)|sets]] <math>S</math> with <math>S \\subsetneq \\underline{m}</math>. Then we obtain\n<math display=\"block\">g(A)=\\left|\\bigcap_{i \\in \\underline{m} \\smallsetminus A} A_i\\right|, \\quad g(\\underline{m}) = \\left|\\bigcup_{i \\in \\underline{m}} A_i \\right| \\text{ and } g(A) = \\mathbb{P} \\left( \\bigcap_{i \\in \\underline{m} \\smallsetminus A} A_i \\right),~~ g(\\underline{m}) = \\mathbb{P} \\left(\\bigcup_{i \\in \\underline{m}} A_i\\right)</math>\nrespectively for all sets <math>A</math> with <math>A \\subsetneq \\underline{m}</math>. This is because [[element (mathematics)|elements]] <math>a</math> of <math display=\"inline\">\\bigcap_{i \\in \\underline{m} \\smallsetminus A} A_i</math> can be [[element (mathematics)#notation|contained]] in other <math>A_i</math> (<math>A_i</math> with <math>i \\in A</math>) as well, and the {{nowrap|<math display=\"inline\">\\bigcap \\smallsetminus \\bigcup</math>-formula}} runs exactly through all possible extensions of the sets <math>\\{A_i \\mid i \\in \\underline{m} \\smallsetminus A\\}</math> with other <math>A_i</math>, counting <math>a</math> only for the set that matches the membership behavior of <math>a</math>, if <math>S</math> runs through all [[subset]]s of <math>A</math> (as in the definition of <math>g(A)</math>).\n\nSince <math>f(\\underline{m}) = 0</math>, we obtain from ({{EquationNote|2}}) with <math>A = \\underline{m}</math> that\n<math display=\"block\">\\sum_{\\underline{m} \\supseteq T \\supsetneq \\varnothing}(-1)^{|T|-1} g(\\underline{m} \\smallsetminus T) = \\sum_{\\varnothing \\subseteq S \\subsetneq \\underline{m}}(-1)^{m-|S|-1} g(S) = g(\\underline{m})</math>\nand by interchanging sides, the combinatorial and the probabilistic version of the inclusion–exclusion principle follow."}},"i":0}}]}'>

**Proof**

Take m _ = { 1, 2, …, m } {\displaystyle {\underline {m}}=\{1,2,\ldots ,m\}}[image: {\displaystyle {\underline {m}}=\{1,2,\ldots ,m\}}], f ( m _) = 0 {\displaystyle f({\underline {m}})=0}[image: {\displaystyle f({\underline {m}})=0}], and f ( S) = | ⋂ i ∈ m _ ∖ S A i ∖ ⋃ i ∈ S A i | and f ( S) = P ( ⋂ i ∈ m _ ∖ S A i ∖ ⋃ i ∈ S A i) {\displaystyle f(S)=\left|\bigcap _{i\in {\underline {m}}\smallsetminus S}A_{i}\smallsetminus \bigcup _{i\in S}A_{i}\right|{\text{ and }}f(S)=\mathbb {P} \left(\bigcap _{i\in {\underline {m}}\smallsetminus S}A_{i}\smallsetminus \bigcup _{i\in S}A_{i}\right)}[image: {\displaystyle f(S)=\left|\bigcap _{i\in {\underline {m}}\smallsetminus S}A_{i}\smallsetminus \bigcup _{i\in S}A_{i}\right|{\text{ and }}f(S)=\mathbb {P} \left(\bigcap _{i\in {\underline {m}}\smallsetminus S}A_{i}\smallsetminus \bigcup _{i\in S}A_{i}\right)}] respectively for all [sets][42] S {\displaystyle S}[image: {\displaystyle S}] with S ⊊ m _ {\displaystyle S\subsetneq {\underline {m}}}[image: {\displaystyle S\subsetneq {\underline {m}}}]. Then we obtain g ( A) = | ⋂ i ∈ m _ ∖ A A i |, g ( m _) = | ⋃ i ∈ m _ A i | and g ( A) = P ( ⋂ i ∈ m _ ∖ A A i), g ( m _) = P ( ⋃ i ∈ m _ A i) {\displaystyle g(A)=\left|\bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}\right|,\quad g({\underline {m}})=\left|\bigcup _{i\in {\underline {m}}}A_{i}\right|{\text{ and }}g(A)=\mathbb {P} \left(\bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}\right),~~g({\underline {m}})=\mathbb {P} \left(\bigcup _{i\in {\underline {m}}}A_{i}\right)}[image: {\displaystyle g(A)=\left|\bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}\right|,\quad g({\underline {m}})=\left|\bigcup _{i\in {\underline {m}}}A_{i}\right|{\text{ and }}g(A)=\mathbb {P} \left(\bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}\right),~~g({\underline {m}})=\mathbb {P} \left(\bigcup _{i\in {\underline {m}}}A_{i}\right)}] respectively for all sets A {\displaystyle A}[image: {\displaystyle A}] with A ⊊ m _ {\displaystyle A\subsetneq {\underline {m}}}[image: {\displaystyle A\subsetneq {\underline {m}}}]. This is because [elements][43] a {\displaystyle a}[image: {\displaystyle a}] of ⋂ i ∈ m _ ∖ A A i {\textstyle \bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}}[image: {\textstyle \bigcap _{i\in {\underline {m}}\smallsetminus A}A_{i}}] can be [contained][44] in other A i {\displaystyle A_{i}}[image: {\displaystyle A_{i}}] ( A i {\displaystyle A_{i}}[image: {\displaystyle A_{i}}] with i ∈ A {\displaystyle i\in A}[image: {\displaystyle i\in A}]) as well, and the ⋂ ∖ ⋃ {\textstyle \bigcap \smallsetminus \bigcup }[image: {\textstyle \bigcap \smallsetminus \bigcup }] -formula runs exactly through all possible extensions of the sets { A i ∣ i ∈ m _ ∖ A } {\displaystyle \{A_{i}\mid i\in {\underline {m}}\smallsetminus A\}}[image: {\displaystyle \{A_{i}\mid i\in {\underline {m}}\smallsetminus A\}}] with other A i {\displaystyle A_{i}}[image: {\displaystyle A_{i}}], counting a {\displaystyle a}[image: {\displaystyle a}] only for the set that matches the membership behavior of a {\displaystyle a}[image: {\displaystyle a}], if S {\displaystyle S}[image: {\displaystyle S}] runs through all [subsets][45] of A {\displaystyle A}[image: {\displaystyle A}] (as in the definition of g ( A) {\displaystyle g(A)}[image: {\displaystyle g(A)}]).

Since f ( m _) = 0 {\displaystyle f({\underline {m}})=0}[image: {\displaystyle f({\underline {m}})=0}], we obtain from (**2**) with A = m _ {\displaystyle A={\underline {m}}}[image: {\displaystyle A={\underline {m}}}] that ∑ m _ ⊇ T ⊋ ∅ ( − 1) | T | − 1 g ( m _ ∖ T) = ∑ ∅ ⊆ S ⊊ m _ ( − 1) m − | S | − 1 g ( S) = g ( m _) {\displaystyle \sum _{{\underline {m}}\supseteq T\supsetneq \varnothing }(-1)^{|T|-1}g({\underline {m}}\smallsetminus T)=\sum _{\varnothing \subseteq S\subsetneq {\underline {m}}}(-1)^{m-|S|-1}g(S)=g({\underline {m}})}[image: {\displaystyle \sum _{{\underline {m}}\supseteq T\supsetneq \varnothing }(-1)^{|T|-1}g({\underline {m}}\smallsetminus T)=\sum _{\varnothing \subseteq S\subsetneq {\underline {m}}}(-1)^{m-|S|-1}g(S)=g({\underline {m}})}] and by interchanging sides, the combinatorial and the probabilistic version of the inclusion–exclusion principle follow.

If one sees a number n {\displaystyle n}[image: {\displaystyle n}] as a set of its prime factors, then (**2**) is a generalization of [Möbius inversion formula][46] for [square-free][47] [natural numbers][48]. Therefore, (**2**) is seen as the Möbius inversion formula for the [incidence algebra][49] of the [partially ordered set][50] of all subsets of A.

For a generalization of the full version of Möbius inversion formula, (**2**) must be generalized to [multisets][51]. For multisets instead of sets, (**2**) becomes

f(A) = \\sum_{S\\subseteq A}\\mu(A - S) g(S) </math>"},"3":{"wt":"{{EquationRef|3}}"}},"i":0}}]}'>

f ( A) = ∑ S ⊆ A μ ( A − S) g ( S) {\displaystyle f(A)=\sum _{S\subseteq A}\mu (A-S)g(S)}[image: {\displaystyle f(A)=\sum _{S\subseteq A}\mu (A-S)g(S)}] |  | 3 |

where A − S {\displaystyle A-S}[image: {\displaystyle A-S}] is the multiset for which ( A − S) ⊎ S = A {\displaystyle (A-S)\uplus S=A}[image: {\displaystyle (A-S)\uplus S=A}], and

- *μ*(*S*) = 1 if S is a set (i.e. a multiset without double elements) of [even][52] [cardinality][6].
- *μ*(*S*) = −1 if S is a set (i.e. a multiset without double elements) of odd cardinality.
- *μ*(*S*) = 0 if S is a proper multiset (i.e. S has double elements).

Notice that μ ( A − S) {\displaystyle \mu (A-S)}[image: {\displaystyle \mu (A-S)}] is just the ( − 1) | A | − | S | {\displaystyle (-1)^{|A|-|S|}}[image: {\displaystyle (-1)^{|A|-|S|}}] of (**2**) in case A − S {\displaystyle A-S}[image: {\displaystyle A-S}] is a set.

g(S)=\\sum_{T\\subseteq S}f(T)</math>\non the right hand side of ({{EquationNote|3}}). Notice that <math>f(A)</math> appears once on both sides of ({{EquationNote|3}}). So we must show that for all <math>T</math> with <math>T\\subsetneq A</math>, the terms <math>f(T)</math> cancel out on the right hand side of ({{EquationNote|3}}). For that purpose, take a fixed <math>T</math> such that <math>T\\subsetneq A</math> and take an arbitrary fixed <math>a \\in A</math> such that <math>a \\notin T</math>.\n\nNotice that <math>A - S</math> must be a set for each [[Positive number|positive]] or [[negative number|negative]] appearance of <math>f(T)</math> on the right hand side of ({{EquationNote|3}}) that is obtained by way of the multiset <math>S</math> such that <math>T \\subseteq S \\subseteq A</math>. Now each appearance of <math>f(T)</math> on the right hand side of ({{EquationNote|3}}) that is obtained by way of <math>S</math> such that <math>A - S</math> is a set that contains <math>a</math> cancels out with the one that is obtained by way of the corresponding <math>S</math> such that <math>A - S</math> is a set that does not contain <math>a</math>. This gives the desired result."}},"i":0}}]}'>

**Proof of (**3**)**

Substitute g ( S) = ∑ T ⊆ S f ( T) {\displaystyle g(S)=\sum _{T\subseteq S}f(T)}[image: {\displaystyle g(S)=\sum _{T\subseteq S}f(T)}] on the right hand side of (**3**). Notice that f ( A) {\displaystyle f(A)}[image: {\displaystyle f(A)}] appears once on both sides of (**3**). So we must show that for all T {\displaystyle T}[image: {\displaystyle T}] with T ⊊ A {\displaystyle T\subsetneq A}[image: {\displaystyle T\subsetneq A}], the terms f ( T) {\displaystyle f(T)}[image: {\displaystyle f(T)}] cancel out on the right hand side of (**3**). For that purpose, take a fixed T {\displaystyle T}[image: {\displaystyle T}] such that T ⊊ A {\displaystyle T\subsetneq A}[image: {\displaystyle T\subsetneq A}] and take an arbitrary fixed a ∈ A {\displaystyle a\in A}[image: {\displaystyle a\in A}] such that a ∉ T {\displaystyle a\notin T}[image: {\displaystyle a\notin T}].

Notice that A − S {\displaystyle A-S}[image: {\displaystyle A-S}] must be a set for each [positive][53] or [negative][54] appearance of f ( T) {\displaystyle f(T)}[image: {\displaystyle f(T)}] on the right hand side of (**3**) that is obtained by way of the multiset S {\displaystyle S}[image: {\displaystyle S}] such that T ⊆ S ⊆ A {\displaystyle T\subseteq S\subseteq A}[image: {\displaystyle T\subseteq S\subseteq A}]. Now each appearance of f ( T) {\displaystyle f(T)}[image: {\displaystyle f(T)}] on the right hand side of (**3**) that is obtained by way of S {\displaystyle S}[image: {\displaystyle S}] such that A − S {\displaystyle A-S}[image: {\displaystyle A-S}] is a set that contains a {\displaystyle a}[image: {\displaystyle a}] cancels out with the one that is obtained by way of the corresponding S {\displaystyle S}[image: {\displaystyle S}] such that A − S {\displaystyle A-S}[image: {\displaystyle A-S}] is a set that does not contain a {\displaystyle a}[image: {\displaystyle a}]. This gives the desired result.

## Applications

[[edit][55]]

The inclusion–exclusion principle is widely used and only a few of its applications can be mentioned here.

### Counting derangements

[[edit][56]]

Main article: [Derangement][24]

A well-known application of the inclusion–exclusion principle is to the combinatorial problem of counting all [derangements][24] of a finite set. A *derangement*of a set A is a [bijection][57] from A into itself that has no fixed points. Via the inclusion–exclusion principle one can show that if the cardinality of A is n, then the number of derangements is [*n*! /*e*] where [*x*] denotes the [nearest integer][58] to x; a detailed proof is available [here][59] and also see the examples section above.

The first occurrence of the problem of counting the number of derangements is in an early book on games of chance: *Essai d'analyse sur les jeux de hazard*by P. R. de Montmort (1678 – 1719) and was known as either "Montmort's problem" or by the name he gave it, "*problème des rencontres*". [10] The problem is also known as the *hatcheck problem*.

The number of derangements is also known as the [subfactorial][60] of n, written !*n*. It follows that if all bijections are assigned the same probability then the probability that a random bijection is a derangement quickly approaches 1/*e*as n grows.

### Counting intersections

[[edit][61]]

The principle of inclusion–exclusion, combined with [De Morgan's law][62], can be used to count the cardinality of the intersection of sets as well. Let A k ¯ {\displaystyle {\overline {A_{k}}}}[image: {\displaystyle {\overline {A_{k}}}}] represent the complement of k</sub>''"}},"i":0}}]}'>*A k*with respect to some universal set A such that A k ⊆ A {\displaystyle A_{k}\subseteq A}[image: {\displaystyle A_{k}\subseteq A}] for each k. Then we have ⋂ i = 1 n A i = ⋃ i = 1 n A i ¯ ¯ {\displaystyle \bigcap _{i=1}^{n}A_{i}={\overline {\bigcup _{i=1}^{n}{\overline {A_{i}}}}}}[image: {\displaystyle \bigcap _{i=1}^{n}A_{i}={\overline {\bigcup _{i=1}^{n}{\overline {A_{i}}}}}}] thereby turning the problem of finding an intersection into the problem of finding a union.

### Graph coloring

[[edit][63]]

The inclusion exclusion principle forms the basis of algorithms for a number of NP-hard graph partitioning problems, such as [graph coloring][64]. [11]

A well known application of the principle is the construction of the [chromatic polynomial][65] of a graph. [12]

### Bipartite graph perfect matchings

[[edit][66]]

The number of [perfect matchings][67] of a [bipartite graph][68] can be calculated using the principle. [13]

### Number of onto functions

[[edit][69]]

Given finite sets A and B, how many [surjective functions][70] (onto functions) are there from A to B? [Without any loss of generality][71] we may take *A*= {1, ..., *k*} and *B*= {1, ..., *n*}, since only the cardinalities of the sets matter. By using S as the set of all [functions][72] from A to B, and defining, for each i in B, the property i</sub>''"}},"i":0}}]}'>*P i*as "the function misses the element i in B " ( i is not in the [image][73] of the function), the principle of inclusion – exclusion gives the number of onto functions between A and B as: [14] ∑ j = 0 n ( n j) ( − 1) j ( n − j) k. {\displaystyle \sum _{j=0}^{n}{\binom {n}{j}}(-1)^{j}(n-j)^{k}.}[image: {\displaystyle \sum _{j=0}^{n}{\binom {n}{j}}(-1)^{j}(n-j)^{k}.}]

### Permutations with forbidden positions

[[edit][74]]

A [permutation][75] of the set *S*= {1, ..., *n*} where each element of S is restricted to not being in certain positions (here the permutation is considered as an ordering of the elements of S) is called a *permutation with forbidden positions*. For example, with *S*= {1,2,3,4}, the permutations with the restriction that the element 1 can not be in positions 1 or 3, and the element 2 can not be in position 4 are: 2134, 2143, 3124, 4123, 2341, 2431, 3241, 3421, 4231 and 4321. By letting i</sub>''"}},"i":0}}]}'>*A i*be the set of positions that the element i is not allowed to be in, and the property ''i''</sub>"}},"i":0}}]}'>*P**i*to be the property that a permutation puts element i into a position in i</sub>''"}},"i":0}}]}'>*A i*, the principle of inclusion–exclusion can be used to count the number of permutations which satisfy all the restrictions. [15]

In the given example, there are 12 = 2(3!) permutations with property 1</sub>"}},"i":0}}]}'>*P*1, 6 = 3! permutations with property 2</sub>"}},"i":0}}]}'>*P*2, and no permutations have properties 3</sub>"}},"i":0}}]}'>*P*3 or 4</sub>"}},"i":0}}]}'>*P*4 as there are no restrictions for these two elements. The number of permutations satisfying the restrictions is thus: 4! − ( 12 + 6 + 0 + 0) + ( 4) = 24 − 18 + 4 = 10. {\displaystyle 4!-(12+6+0+0)+(4)=24-18+4=10.}[image: {\displaystyle 4!-(12+6+0+0)+(4)=24-18+4=10.}]

The final 4 in this computation is the number of permutations having both properties 1</sub>"}},"i":0}}]}'>*P*1 and 2</sub>"}},"i":0}}]}'>*P*2. There are no other non-zero contributions to the formula.

### Stirling numbers of the second kind

[[edit][76]]

Main article: [Stirling numbers of the second kind][77]

The [Stirling numbers of the second kind][77], *S*(*n*,*k*) count the number of [partitions][78] of a set of n elements into k non-empty subsets (indistinguishable *boxes*). An explicit formula for them can be obtained by applying the principle of inclusion–exclusion to a very closely related problem, namely, counting the number of partitions of an n -set into k non-empty but distinguishable boxes ( [ordered][79] non-empty subsets). Using the universal set consisting of all partitions of the n -set into k (possibly empty) distinguishable boxes, 1</sub>, ''A''<sub>2</sub>, ..., ''A<sub>k</sub>''"}},"i":0}}]}'>*A*1, *A*2, ..., *A k*, and the properties i</sub>''"}},"i":0}}]}'>*P i*meaning that the partition has box i</sub>''"}},"i":0}}]}'>*A i*empty, the principle of inclusion–exclusion gives an answer for the related result. Dividing by *k*! to remove the artificial ordering gives the Stirling number of the second kind: [16] S ( n, k) = 1 k! ∑ t = 0 k ( − 1) t ( k t) ( k − t) n. {\displaystyle S(n,k)={\frac {1}{k!}}\sum _{t=0}^{k}(-1)^{t}{\binom {k}{t}}(k-t)^{n}.}[image: {\displaystyle S(n,k)={\frac {1}{k!}}\sum _{t=0}^{k}(-1)^{t}{\binom {k}{t}}(k-t)^{n}.}]

### Rook polynomials

[[edit][80]]

Main article: [Rook polynomial][81]

A [rook polynomial][81] is the [generating function][82] of the number of ways to place non-attacking [rooks][83] on a *board B*that looks like a subset of the squares of a [checkerboard][84]; that is, no two rooks may be in the same row or column. The board B is any subset of the squares of a rectangular board with n rows and m columns; we think of it as the squares in which one is allowed to put a rook. The [coefficient][85], k</sub>''(''B'')"}},"i":0}}]}'>*r k*(*B*) of k</sup>''"}},"i":0}}]}'>*x k*in the rook polynomial B</sub>''(''x'')"}},"i":0}}]}'>*R B*(*x*) is the number of ways k rooks, none of which attacks another, can be arranged in the squares of B. For any board B, there is a complementary board B ′ {\displaystyle B'}[image: {\displaystyle B'}] consisting of the squares of the rectangular board that are not in B. This complementary board also has a rook polynomial R B ′ ( x) {\displaystyle R_{B'}(x)}[image: {\displaystyle R_{B'}(x)}] with coefficients r k ( B ′). {\displaystyle r_{k}(B').}[image: {\displaystyle r_{k}(B').}]

It is sometimes convenient to be able to calculate the highest coefficient of a rook polynomial in terms of the coefficients of the rook polynomial of the complementary board. Without loss of generality we can assume that *n*≤ *m*, so this coefficient is n</sub>''(''B'')"}},"i":0}}]}'>*r n*(*B*). The number of ways to place n non-attacking rooks on the complete *n*× *m*"checkerboard" (without regard as to whether the rooks are placed in the squares of the board B) is given by the [falling factorial][86]: ( m) n = m ( m − 1) ( m − 2) ⋯ ( m − n + 1). {\displaystyle (m)_{n}=m(m-1)(m-2)\cdots (m-n+1).}[image: {\displaystyle (m)_{n}=m(m-1)(m-2)\cdots (m-n+1).}]

Letting ''i''</sub>"}},"i":0}}]}'>*P**i*be the property that an assignment of n non-attacking rooks on the complete board has a rook in column i which is not in a square of the board B, then by the principle of inclusion–exclusion we have: [17] r n ( B) = ∑ t = 0 n ( − 1) t ( m − t) n − t r t ( B ′). {\displaystyle r_{n}(B)=\sum _{t=0}^{n}(-1)^{t}(m-t)_{n-t}\ r_{t}(B').}[image: {\displaystyle r_{n}(B)=\sum _{t=0}^{n}(-1)^{t}(m-t)_{n-t}\ r_{t}(B').}]

### Euler's phi function

[[edit][87]]

Main article: [Euler's totient function][88]

Euler's totient or phi function, *φ*(*n*) is an [arithmetic function][89] that counts the number of positive integers less than or equal to n that are [relatively prime][90] to n. That is, if n is a [positive integer][91], then *φ*(*n*) is the number of integers k in the range 1 ≤ *k*≤ *n*which have no common factor with n other than 1. The principle of inclusion–exclusion is used to obtain a formula for *φ*(*n*). Let S be the set {1, ..., *n*} and define the property i</sub>''"}},"i":0}}]}'>*P i*to be that a number in S is divisible by the prime number i</sub>''"}},"i":0}}]}'>*p i*, for 1 ≤ *i*≤ *r*, where the [prime factorization][92] of n = p 1 a 1 p 2 a 2 ⋯ p r a r. {\displaystyle n=p_{1}^{a_{1}}p_{2}^{a_{2}}\cdots p_{r}^{a_{r}}.}[image: {\displaystyle n=p_{1}^{a_{1}}p_{2}^{a_{2}}\cdots p_{r}^{a_{r}}.}]

Then, [18] φ ( n) = n − ∑ i = 1 r n p i + ∑ 1 ⩽ i < j ⩽ r n p i p j − ⋯ = n ∏ i = 1 r ( 1 − 1 p i). {\displaystyle \varphi (n)=n-\sum _{i=1}^{r}{\frac {n}{p_{i}}}+\sum _{1\leqslant i<j\leqslant r}{\frac {n}{p_{i}p_{j}}}-\cdots =n\prod _{i=1}^{r}\left(1-{\frac {1}{p_{i}}}\right).}[image: {\displaystyle \varphi (n)=n-\sum _{i=1}^{r}{\frac {n}{p_{i}}}+\sum _{1\leqslant i<j\leqslant r}{\frac {n}{p_{i}p_{j}}}-\cdots =n\prod _{i=1}^{r}\left(1-{\frac {1}{p_{i}}}\right).}]

### Dirichlet hyperbola method

[[edit][93]]

Main article: [Dirichlet hyperbola method][94]

[95] An example of the Dirichlet hyperbola method with *n*= 10, *a*≈ 2.7, and *b*≈ 3.7.

The [Dirichlet hyperbola method][94] re-expresses a sum of a [multiplicative function][96] f ( n) {\displaystyle f(n)}[image: {\displaystyle f(n)}] by selecting a suitable [Dirichlet convolution][97] f = g ∗ h {\displaystyle f=g\ast h}[image: {\displaystyle f=g\ast h}], recognizing that the sum F ( n) = ∑ k = 1 n f ( k) = ∑ k = 1 n ∑ x y = k g ( x) h ( y) {\displaystyle F(n)=\sum _{k=1}^{n}f(k)=\sum _{k=1}^{n}\sum _{xy=k}^{}g(x)h(y)}[image: {\displaystyle F(n)=\sum _{k=1}^{n}f(k)=\sum _{k=1}^{n}\sum _{xy=k}^{}g(x)h(y)}] can be recast as a sum over the [lattice points][98] in a region bounded by x ≥ 1 {\displaystyle x\geq 1}[image: {\displaystyle x\geq 1}], y ≥ 1 {\displaystyle y\geq 1}[image: {\displaystyle y\geq 1}], and x y ≤ n {\displaystyle xy\leq n}[image: {\displaystyle xy\leq n}], splitting this region into two overlapping subregions, and finally using the inclusion–exclusion principle to conclude that F ( n) = ∑ k = 1 n f ( k) = ∑ k = 1 n ∑ x y = k g ( x) h ( y) = ∑ x = 1 a ∑ y = 1 n / x g ( x) h ( y) + ∑ y = 1 b ∑ x = 1 n / y g ( x) h ( y) − ∑ x = 1 a ∑ y = 1 b g ( x) h ( y). {\displaystyle F(n)=\sum _{k=1}^{n}f(k)=\sum _{k=1}^{n}\sum _{xy=k}^{}g(x)h(y)=\sum _{x=1}^{a}\sum _{y=1}^{n/x}g(x)h(y)+\sum _{y=1}^{b}\sum _{x=1}^{n/y}g(x)h(y)-\sum _{x=1}^{a}\sum _{y=1}^{b}g(x)h(y).}[image: {\displaystyle F(n)=\sum _{k=1}^{n}f(k)=\sum _{k=1}^{n}\sum _{xy=k}^{}g(x)h(y)=\sum _{x=1}^{a}\sum _{y=1}^{n/x}g(x)h(y)+\sum _{y=1}^{b}\sum _{x=1}^{n/y}g(x)h(y)-\sum _{x=1}^{a}\sum _{y=1}^{b}g(x)h(y).}]

## Diluted inclusion–exclusion principle

[[edit][99]]

See also: [Bonferroni inequalities][100]

In many cases where the principle could give an exact formula (in particular, counting [prime numbers][101] using the [sieve of Eratosthenes][102]), the formula arising does not offer useful content because the number of terms in it is excessive. If each term individually can be estimated accurately, the accumulation of errors may imply that the inclusion–exclusion formula is not directly applicable. In [number theory][13], this difficulty was addressed by [Viggo Brun][103]. After a slow start, his ideas were taken up by others, and a large variety of [sieve methods][12] developed. These for example may try to find upper bounds for the "sieved" sets, rather than an exact formula.

Let 1</sub>, ..., ''A''<sub>''n''</sub>"}},"i":0}}]}'>*A*1, ..., *A**n*be arbitrary sets and 1</sub>, ..., ''p''<sub>''n''</sub>"}},"i":0}}]}'>*p*1, ..., *p**n*real numbers in the closed [unit interval][104] [0, 1]. Then, for every even number k in {0, ..., *n*}, the [indicator functions][105] satisfy the inequality: [19] 1 A 1 ∪ ⋯ ∪ A n ≥ ∑ j = 1 k ( − 1) j − 1 ∑ 1 ≤ i 1 < ⋯ < i j ≤ n p i 1 … p i j 1 A i 1 ∩ ⋯ ∩ A i j. {\displaystyle \mathbf {1} _{A_{1}\cup \cdots \cup A_{n}}\geq \sum _{j=1}^{k}(-1)^{j-1}\sum _{1\leq i_{1}<\cdots <i_{j}\leq n}p_{i_{1}}\dots p_{i_{j}}\,\mathbf {1} _{A_{i_{1}}\cap \cdots \cap A_{i_{j}}}.}[image: {\displaystyle \mathbf {1} _{A_{1}\cup \cdots \cup A_{n}}\geq \sum _{j=1}^{k}(-1)^{j-1}\sum _{1\leq i_{1}<\cdots <i_{j}\leq n}p_{i_{1}}\dots p_{i_{j}}\,\mathbf {1} _{A_{i_{1}}\cap \cdots \cap A_{i_{j}}}.}]

## Proof of main statement

[[edit][106]]

Choose an element contained in the union of all sets and let A 1, A 2, …, A t {\displaystyle A_{1},A_{2},\dots ,A_{t}}[image: {\displaystyle A_{1},A_{2},\dots ,A_{t}}] be the individual sets containing it. (Note that *t*> 0.) Since the element is counted precisely once by the left-hand side of equation (**1**), we need to show that it is counted precisely once by the right-hand side. On the right-hand side, the only non-zero contributions occur when all the subsets in a particular term contain the chosen element, that is, all the subsets are selected from A 1, A 2, …, A t {\displaystyle A_{1},A_{2},\dots ,A_{t}}[image: {\displaystyle A_{1},A_{2},\dots ,A_{t}}]. The contribution is one for each of these sets (plus or minus depending on the term) and therefore is just the (signed) number of these subsets used in the term. We then have: | { A i ∣ 1 ⩽ i ⩽ t } | − | { A i ∩ A j ∣ 1 ⩽ i < j ⩽ t } | + ⋯ + ( − 1) t + 1 | { A 1 ∩ A 2 ∩ ⋯ ∩ A t } | = ( t 1) − ( t 2) + ⋯ + ( − 1) t + 1 ( t t). {\displaystyle {\begin{aligned}|\{A_{i}\mid 1\leqslant i\leqslant t\}|&-|\{A_{i}\cap A_{j}\mid 1\leqslant i<j\leqslant t\}|+\cdots +(-1)^{t+1}|\{A_{1}\cap A_{2}\cap \cdots \cap A_{t}\}|={\binom {t}{1}}-{\binom {t}{2}}+\cdots +(-1)^{t+1}{\binom {t}{t}}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}|\{A_{i}\mid 1\leqslant i\leqslant t\}|&-|\{A_{i}\cap A_{j}\mid 1\leqslant i<j\leqslant t\}|+\cdots +(-1)^{t+1}|\{A_{1}\cap A_{2}\cap \cdots \cap A_{t}\}|={\binom {t}{1}}-{\binom {t}{2}}+\cdots +(-1)^{t+1}{\binom {t}{t}}.\end{aligned}}}]

By the [binomial theorem][107], 0 = ( 1 − 1) t = ( t 0) − ( t 1) + ( t 2) − ⋯ + ( − 1) t ( t t). {\displaystyle 0=(1-1)^{t}={\binom {t}{0}}-{\binom {t}{1}}+{\binom {t}{2}}-\cdots +(-1)^{t}{\binom {t}{t}}.}[image: {\displaystyle 0=(1-1)^{t}={\binom {t}{0}}-{\binom {t}{1}}+{\binom {t}{2}}-\cdots +(-1)^{t}{\binom {t}{t}}.}]

Using the fact that ( t 0) = 1 {\displaystyle {\binom {t}{0}}=1}[image: {\displaystyle {\binom {t}{0}}=1}] and rearranging terms, we have 1 = ( t 1) − ( t 2) + ⋯ + ( − 1) t + 1 ( t t), {\displaystyle 1={\binom {t}{1}}-{\binom {t}{2}}+\cdots +(-1)^{t+1}{\binom {t}{t}},}[image: {\displaystyle 1={\binom {t}{1}}-{\binom {t}{2}}+\cdots +(-1)^{t+1}{\binom {t}{t}},}] and so, the chosen element is counted only once by the right-hand side of equation (**1**).

### Algebraic proof

[[edit][108]]

An algebraic proof can be obtained using [indicator functions][105] (also known as characteristic functions). The indicator function of a subset S of a set X is the function 1 S: X → { 0, 1 } 1 S ( x) = { 1 x ∈ S 0 x ∉ S {\displaystyle {\begin{aligned}&\mathbf {1} _{S}:X\to \{0,1\}\\&\mathbf {1} _{S}(x)={\begin{cases}1&x\in S\\0&x\notin S\end{cases}}\end{aligned}}}[image: {\displaystyle {\begin{aligned}&\mathbf {1} _{S}:X\to \{0,1\}\\&\mathbf {1} _{S}(x)={\begin{cases}1&x\in S\\0&x\notin S\end{cases}}\end{aligned}}}]

If A {\displaystyle A}[image: {\displaystyle A}] and B {\displaystyle B}[image: {\displaystyle B}] are two subsets of X {\displaystyle X}[image: {\displaystyle X}], then 1 A ⋅ 1 B = 1 A ∩ B. {\displaystyle \mathbf {1} _{A}\cdot \mathbf {1} _{B}=\mathbf {1} _{A\cap B}.}[image: {\displaystyle \mathbf {1} _{A}\cdot \mathbf {1} _{B}=\mathbf {1} _{A\cap B}.}]

Let A denote the union ⋃ i = 1 n A i {\textstyle \bigcup _{i=1}^{n}A_{i}}[image: {\textstyle \bigcup _{i=1}^{n}A_{i}}] of the sets 1</sub>, ..., ''A<sub>n</sub>''"}},"i":0}}]}'>*A*1, ..., *A n*. To prove the inclusion–exclusion principle in general, we first verify the identity

\\mathbf{1}_A =\\sum_{k=1}^n (-1)^{k-1} \\sum_{I\\subset\\{1,\\ldots,n\\} \\atop|I| = k} \\mathbf{1}_{A_I}</math>"},"3":{"wt":"{{EquationRef|4}}"}},"i":0}}]}'>

1 A = ∑ k = 1 n ( − 1) k − 1 ∑ I ⊂ { 1, …, n } | I | = k 1 A I {\displaystyle \mathbf {1} _{A}=\sum _{k=1}^{n}(-1)^{k-1}\sum _{I\subset \{1,\ldots ,n\} \atop |I|=k}\mathbf {1} _{A_{I}}}[image: {\displaystyle \mathbf {1} _{A}=\sum _{k=1}^{n}(-1)^{k-1}\sum _{I\subset \{1,\ldots ,n\} \atop |I|=k}\mathbf {1} _{A_{I}}}] |  | 4 |

for indicator functions, where: A I = ⋂ i ∈ I A i. {\displaystyle A_{I}=\bigcap _{i\in I}A_{i}.}[image: {\displaystyle A_{I}=\bigcap _{i\in I}A_{i}.}]

The following function ( 1 A − 1 A 1) ( 1 A − 1 A 2) ⋯ ( 1 A − 1 A n) = 0, {\displaystyle \left(\mathbf {1} _{A}-\mathbf {1} _{A_{1}}\right)\left(\mathbf {1} _{A}-\mathbf {1} _{A_{2}}\right)\cdots \left(\mathbf {1} _{A}-\mathbf {1} _{A_{n}}\right)=0,}[image: {\displaystyle \left(\mathbf {1} _{A}-\mathbf {1} _{A_{1}}\right)\left(\mathbf {1} _{A}-\mathbf {1} _{A_{2}}\right)\cdots \left(\mathbf {1} _{A}-\mathbf {1} _{A_{n}}\right)=0,}] is identically zero because: if x is not in A, then all factors are 0 − 0 = 0; and otherwise, if x does belong to some m</sub>''"}},"i":0}}]}'>*A m*, then the corresponding m th factor is 1 − 1 = 0. By expanding the product on the left-hand side, equation (**4**) follows.

To prove the inclusion–exclusion principle for the cardinality of sets, sum the equation (**4**) over all x in the union of 1</sub>, ..., ''A<sub>n</sub>''"}},"i":0}}]}'>*A*1, ..., *A n*. To derive the version used in probability, take the [expectation][109] in (**4**). In general, [integrate][110] the equation (**4**) with respect to μ. Always use linearity in these derivations.

## See also

[[edit][111]]

- [Boole's inequality][112] – Inequality applying to probability spaces
- [Combinatorial principles][113] – Methods used in combinatorics
- [Maximum-minimums identity][114] – Relates the maximum element of a set of numbers and the minima of its non-empty subsets
- [Necklace problem][115]
- [Pigeonhole principle][116] – Theorem in combinatorics
- [Schuette–Nesbitt formula][117]

## Notes

[[edit][118]]

1. 1 2 Roberts & Tesman 2009, pg. 405
2. ↑ Mazur 2010, pg. 94
3. ↑ van Lint & Wilson 1992, pg. 77
4. ↑ van Lint & Wilson 1992, pg. 77
5. ↑ Stanley 1986, pg. 64
6. ↑ Rota 1964, p. 340.
7. ↑ Brualdi 2010, pp. 167–8
8. ↑ Cameron 1994, pg. 78
9. ↑ Graham, Grötschel & Lovász 1995, pg. 1049
10. ↑ van Lint & Wilson 1992, pp. 77-8
11. ↑ Björklund, Husfeldt & Koivisto 2009
12. ↑ Gross 2008, pp. 211–13
13. ↑ Gross 2008, pp. 208–10
14. ↑ Mazur 2010, pp.84-5, 90
15. ↑ Brualdi 2010, pp. 177–81
16. ↑ Brualdi 2010, pp. 282 – 7
17. ↑ Roberts & Tesman 2009, pp.419–20
18. ↑ van Lint & Wilson 1992, pg. 73
19. ↑ ( Fernández, Fröhlich & Alan D. 1992, Proposition 12.6)

## References

[[edit][119]]

- Allenby, R.B.J.T.; Slomson, Alan (2010), **[How to Count: An Introduction to Combinatorics][120], Discrete Mathematics and Its Applications (2 ed.), CRC Press, pp. 51– 60, [ISBN][121] [978-1-4200-8260-9][122]
- Björklund, A.; Husfeldt, T.; Koivisto, M. (2009), "Set partitioning via inclusion–exclusion", *[SIAM Journal on Computing][123]*, **39**(2): 546– 563, [doi][124]: [10.1137/070683933][125]
- [Brualdi, Richard A.][126] (2010), *Introductory Combinatorics*(5th ed.), Prentice–Hall, [ISBN][121] [978-0-13-602040-0][127]
- [Cameron, Peter J.][128] (1994), *Combinatorics: Topics, Techniques, Algorithms*, Cambridge University Press, [ISBN][121] [0-521-45761-0][129]
- Fernández, Roberto; [Fröhlich, Jürg][130]; [Alan D., Sokal][131] (1992), *Random Walks, Critical Phenomena, and Triviality in Quantum Field Theory*, Texts an Monographs in Physics, Berlin: [Springer-Verlag][132], pp. xviii+444, [ISBN][121] [3-540-54358-9][133], [MR][134] [1219313][135], [Zbl][136] [0761.60061][137]
- [Graham, R.L.][138]; [Grötschel, M.][139]; [Lovász, L.][140] (1995), *Hand Book of Combinatorics (volume-2)*, MIT Press – North Holland, [ISBN][121] [978-0-262-07171-0][141]
- Gross, Jonathan L. (2008), *Combinatorial Methods with Computer Applications*, Chapman&Hall/CRC, [ISBN][121] [978-1-58488-743-0][142]
- ["Inclusion-and-exclusion principle"][143], *[Encyclopedia of Mathematics][144]*, EMS Press, 2001 [1994]
- Mazur, David R. (2010), *Combinatorics A Guided Tour*, The Mathematical Association of America, [ISBN][121] [978-0-88385-762-5][145]
- [Roberts, Fred S.][146]; Tesman, Barry (2009), *Applied Combinatorics*(2nd ed.), CRC Press, [ISBN][121] [978-1-4200-9982-9][147]
- [Rota, Gian-Carlo][16] (1964), "On the foundations of combinatorial theory I. Theory of Möbius functions", *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete*, **2**(4): 340– 368, [doi][124]: [10.1007/BF00531932][148], [S2CID][149] [121334025][150]
- [Stanley, Richard P.][151] (1986), *Enumerative Combinatorics Volume I*, Wadsworth & Brooks/Cole, [ISBN][121] [0-534-06546-5][152]
- [van Lint, J.H.][153]; [Wilson, R.M.][154] (1992), *A Course in Combinatorics*, Cambridge University Press, [ISBN][121] [0-521-42260-4][155]

*This article incorporates material from principle of inclusion–exclusion on [PlanetMath][156], which is licensed under the [Creative Commons Attribution/Share-Alike License][157].*

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Inclusion–exclusion_principle&oldid=1369587686][158] "

[Categories][159]:

- [Enumerative combinatorics][160]
- [Probability theory][161]
- [Mathematical principles][162]
- [Abraham de Moivre][163]

Hidden categories:

- [Articles with short description][164]
- [Short description matches Wikidata][165]
- [Articles containing French-language text][166]
- [Wikipedia articles incorporating text from PlanetMath][167]
- [Articles containing proofs][168]

Search

Inclusion–exclusion principle

32 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Венов_дијаграм.svg
[2]: https://en.wikipedia.org/wiki/Venn_diagram
[3]: https://en.wikipedia.org/wiki/Combinatorics
[4]: https://en.wikipedia.org/wiki/Union_(set_theory)
[5]: https://en.wikipedia.org/wiki/Finite_set
[6]: https://en.wikipedia.org/wiki/Cardinality
[7]: https://en.wikipedia.org/wiki/Intersection_(set_theory)
[8]: https://en.wikipedia.org/wiki/File:Inclusion-exclusion.svg
[9]: https://en.wikipedia.org/wiki/Abraham_de_Moivre
[10]: https://en.wikipedia.org/wiki/Daniel_da_Silva_(mathematician)
[11]: https://en.wikipedia.org/wiki/J._J._Sylvester
[12]: https://en.wikipedia.org/wiki/Sieve_theory
[13]: https://en.wikipedia.org/wiki/Number_theory
[14]: https://en.wikipedia.org/wiki/Probability_space
[15]: https://en.wikipedia.org/wiki/Measure_theory
[16]: https://en.wikipedia.org/wiki/Gian-Carlo_Rota
[17]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=1
[18]: https://en.wikipedia.org/wiki/File:Inclusion-exclusion-3sets.png
[19]: https://en.wikipedia.org/wiki/Universal_set
[20]: https://en.wikipedia.org/wiki/De_Morgan's_laws
[21]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=2
[22]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=3
[23]: https://en.wikipedia.org/wiki/Combination
[24]: https://en.wikipedia.org/wiki/Derangement
[25]: https://en.wikipedia.org/wiki/Taylor_series
[26]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=4
[27]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=5
[28]: https://en.wikipedia.org/wiki/Family_of_sets
[29]: https://en.wikipedia.org/wiki/Index_set
[30]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=6
[31]: https://en.wikipedia.org/wiki/Probability
[32]: https://en.wikipedia.org/wiki/Boole's_inequality#Bonferroni_inequalities
[33]: https://en.wikipedia.org/wiki/Sides_of_an_equation
[34]: https://en.wikipedia.org/wiki/Measure_space
[35]: https://en.wikipedia.org/wiki/Measurable
[36]: https://en.wikipedia.org/wiki/Finite_measure
[37]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=7
[38]: https://en.wikipedia.org/wiki/Binomial_coefficient
[39]: https://en.wikipedia.org/wiki/Independent_and_identically_distributed
[40]: https://en.wikipedia.org/wiki/Point_process_notation
[41]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=8
[42]: https://en.wikipedia.org/wiki/Set_(mathematics)
[43]: https://en.wikipedia.org/wiki/Element_(mathematics)
[44]: https://en.wikipedia.org/wiki/Element_(mathematics)#notation
[45]: https://en.wikipedia.org/wiki/Subset
[46]: https://en.wikipedia.org/wiki/Möbius_inversion_formula
[47]: https://en.wikipedia.org/wiki/Square-free_integer
[48]: https://en.wikipedia.org/wiki/Natural_number
[49]: https://en.wikipedia.org/wiki/Incidence_algebra
[50]: https://en.wikipedia.org/wiki/Partially_ordered_set
[51]: https://en.wikipedia.org/wiki/Multiset
[52]: https://en.wikipedia.org/wiki/Even_and_odd_numbers
[53]: https://en.wikipedia.org/wiki/Positive_number
[54]: https://en.wikipedia.org/wiki/Negative_number
[55]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=9
[56]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=10
[57]: https://en.wikipedia.org/wiki/Bijection
[58]: https://en.wikipedia.org/wiki/Nearest_integer_function
[59]: https://en.wikipedia.org/wiki/Random_permutation_statistics#Number_of_permutations_that_are_derangements
[60]: https://en.wikipedia.org/wiki/Subfactorial
[61]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=11
[62]: https://en.wikipedia.org/wiki/De_Morgan's_law
[63]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=12
[64]: https://en.wikipedia.org/wiki/Graph_coloring
[65]: https://en.wikipedia.org/wiki/Chromatic_polynomial
[66]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=13
[67]: https://en.wikipedia.org/wiki/Perfect_matching
[68]: https://en.wikipedia.org/wiki/Bipartite_graph
[69]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=14
[70]: https://en.wikipedia.org/wiki/Surjective_function
[71]: https://en.wikipedia.org/wiki/Without_any_loss_of_generality
[72]: https://en.wikipedia.org/wiki/Function_(mathematics)
[73]: https://en.wikipedia.org/wiki/Image_(mathematics)
[74]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=15
[75]: https://en.wikipedia.org/wiki/Permutation
[76]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=16
[77]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
[78]: https://en.wikipedia.org/wiki/Partition_of_a_set
[79]: https://en.wikipedia.org/wiki/Ordered_set
[80]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=17
[81]: https://en.wikipedia.org/wiki/Rook_polynomial
[82]: https://en.wikipedia.org/wiki/Generating_polynomial
[83]: https://en.wikipedia.org/wiki/Rook_(chess)
[84]: https://en.wikipedia.org/wiki/Checkerboard
[85]: https://en.wikipedia.org/wiki/Coefficient
[86]: https://en.wikipedia.org/wiki/Falling_factorial
[87]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=18
[88]: https://en.wikipedia.org/wiki/Euler's_totient_function
[89]: https://en.wikipedia.org/wiki/Arithmetic_function
[90]: https://en.wikipedia.org/wiki/Relatively_prime
[91]: https://en.wikipedia.org/wiki/Positive_integer
[92]: https://en.wikipedia.org/wiki/Prime_factorization
[93]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=19
[94]: https://en.wikipedia.org/wiki/Dirichlet_hyperbola_method
[95]: https://en.wikipedia.org/wiki/File:Dirichlet_hyperbola_example_4.svg
[96]: https://en.wikipedia.org/wiki/Multiplicative_function
[97]: https://en.wikipedia.org/wiki/Dirichlet_convolution
[98]: https://en.wikipedia.org/wiki/Lattice_points
[99]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=20
[100]: https://en.wikipedia.org/wiki/Bonferroni_inequalities
[101]: https://en.wikipedia.org/wiki/Prime_number
[102]: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
[103]: https://en.wikipedia.org/wiki/Viggo_Brun
[104]: https://en.wikipedia.org/wiki/Unit_interval
[105]: https://en.wikipedia.org/wiki/Indicator_function
[106]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=21
[107]: https://en.wikipedia.org/wiki/Binomial_theorem
[108]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=22
[109]: https://en.wikipedia.org/wiki/Expected_value
[110]: https://en.wikipedia.org/wiki/Lebesgue_integral
[111]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=23
[112]: https://en.wikipedia.org/wiki/Boole's_inequality
[113]: https://en.wikipedia.org/wiki/Combinatorial_principles
[114]: https://en.wikipedia.org/wiki/Maximum-minimums_identity
[115]: https://en.wikipedia.org/wiki/Necklace_problem
[116]: https://en.wikipedia.org/wiki/Pigeonhole_principle
[117]: https://en.wikipedia.org/wiki/Schuette–Nesbitt_formula
[118]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=24
[119]: /w/index.php?title=Inclusion%E2%80%93exclusion_principle&amp;action=edit&amp;section=25
[120]: http://www.crcpress.com/product/isbn/9781420082609
[121]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[122]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-4200-8260-9
[123]: https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing
[124]: https://en.wikipedia.org/wiki/Doi_(identifier)
[125]: https://doi.org/10.1137%2F070683933
[126]: https://en.wikipedia.org/wiki/Richard_A._Brualdi
[127]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-602040-0
[128]: https://en.wikipedia.org/wiki/Peter_Cameron_(mathematician)
[129]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-45761-0
[130]: https://en.wikipedia.org/wiki/Jürg_Fröhlich
[131]: https://en.wikipedia.org/wiki/Alan_Sokal
[132]: https://en.wikipedia.org/wiki/Springer-Verlag
[133]: https://en.wikipedia.org/wiki/Special:BookSources/3-540-54358-9
[134]: https://en.wikipedia.org/wiki/MR_(identifier)
[135]: https://mathscinet.ams.org/mathscinet-getitem?mr=1219313
[136]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[137]: https://zbmath.org/?format=complete&amp;q=an:0761.60061
[138]: https://en.wikipedia.org/wiki/Ronald_Graham
[139]: https://en.wikipedia.org/wiki/Martin_Grötschel
[140]: https://en.wikipedia.org/wiki/László_Lovász
[141]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-07171-0
[142]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-58488-743-0
[143]: https://www.encyclopediaofmath.org/index.php?title=Inclusion-and-exclusion_principle
[144]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[145]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-88385-762-5
[146]: https://en.wikipedia.org/wiki/Fred_S._Roberts
[147]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-4200-9982-9
[148]: https://doi.org/10.1007%2FBF00531932
[149]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[150]: https://api.semanticscholar.org/CorpusID:121334025
[151]: https://en.wikipedia.org/wiki/Richard_P._Stanley
[152]: https://en.wikipedia.org/wiki/Special:BookSources/0-534-06546-5
[153]: https://en.wikipedia.org/wiki/J._H._van_Lint
[154]: https://en.wikipedia.org/wiki/R._M._Wilson
[155]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-42260-4
[156]: https://en.wikipedia.org/wiki/PlanetMath
[157]: https://en.wikipedia.org/wiki/Wikipedia:CC-BY-SA
[158]: https://en.wikipedia.org/w/index.php?title=Inclusion–exclusion_principle&amp;oldid=1369587686
[159]: /wiki/Help:Category
[160]: /wiki/Category:Enumerative_combinatorics
[161]: /wiki/Category:Probability_theory
[162]: /wiki/Category:Mathematical_principles
[163]: /wiki/Category:Abraham_de_Moivre
[164]: /wiki/Category:Articles_with_short_description
[165]: /wiki/Category:Short_description_matches_Wikidata
[166]: /wiki/Category:Articles_containing_French-language_text
[167]: /wiki/Category:Wikipedia_articles_incorporating_text_from_PlanetMath
[168]: /wiki/Category:Articles_containing_proofs
