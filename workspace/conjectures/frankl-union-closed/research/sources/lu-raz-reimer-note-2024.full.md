<!-- source: https://arxiv.org/pdf/2405.10639 | converted from PDF -->

Note on the union-closed sets conjecture and Reimer’s
average set size theorem

Kengbo Lu
∗, Abigail Raz
†

May 31, 2024

Abstract

The Union-Closed Sets Conjecture, often attributed to P´eter Frankl in 1979, re-
mains an open problem in discrete mathematics. It posits that for any finite family of
sets S ̸= {∅}, if the union of any two sets in the family is also in the family, then there
must exist an element that belongs to at least half of the member sets. We will refer
to the italicized portion as the abundance condition. In 2001, David Reimer proved
that the average set size of a union-closed family S must be at least 1
2 log2 |S|. When
proving this result, he showed that a family being union-closed implies that the family
satisfies certain conditions, which we will refer to as the Reimer’s conditions. There-
fore, as seen in the context of Tim Gowers’ polymath project on the Union-Closed Sets
Conjecture, it is natural to ask if all families that satisfy Reimer’s conditions meet the
abundance condition. A minimal counterexample to this question was offered by Raz
in 2017. In this paper, we will discuss a general method to construct infinitely many
such counterexamples with any fixed lower bound on the size of the member sets. Fur-
thermore, we will discuss some properties related to these counterexamples, especially
those focusing on how far these counterexamples are from being union-closed.

1 Introduction

The Union-Closed Sets Conjecture, stated below, often attributed to P´eter Frankl in 1979,
remains an open problem in extremal combinatorics.

Conjecture 1. For any finite family of sets S ̸= {∅}, if the union of any two sets in the
family is also in the family, then there must exist an element that belongs to at least half of
the sets.

There are also multiple equivalent graph theoretic formulations and a lattice formulation
for this conjecture [3] [11]. An important early partial result was provided by Knill in 1994,
who proved that in any non-trivial union-closed family with n member sets, there exists
an element that appears in at least n−1
log2 n of the sets [6]. Since then, many other partial

∗kengbo.lu@cooper.edu
†abigail.raz@cooper.edu
 1arXiv:2405.10639v2  [math.CO]  30 May 2024
results have been proven. For example, the conjecture holds for families with singletons or
doubletons [12], and it also holds for families whose largest member set size is no more than
11 [2]. In 2022, Gilmer provided the first constant lower bound - there exists an element that
appears in at least 0.01n sets in every union-closed family [4]. Shortly after, multiple groups
improve the constant lower bound to around 0.38 [8, 1, 13, 14]. The best constant lower
bound currently is approximately 0.38271, proven by Liu [7] by building upon the arguments
of Yu [14], Sawin [13], and Gilmer[4].
Gilmer’s groundbreaking constant lower bound is in some sense derived with an averaging
argument together with the use of entropy. Prior to this, many partial results were derived
from using averaging arguments, most notably including Reimer’s result that the average set
size of a union-closed family S must be at least 1
2 log2 |S| [10]. To do this, Reimer introduced
a set of necessary conditions, given in Definition 2, and showed that any family satisfying
these conditions has average set size at least 1
2 log2 |S|. In this paper we further comment on
families satisfying Definition 2. Below we introduce some necessary notation and definitions.

Notation 1.

1. [n] := {1, . . . , n}.

2. Given A ⊆ B ⊆ [n], [A, B] := {C : A ⊆ C ⊆ B}.

3. Let cl(S) denote the union closure of the family S; that is, A ∈ cl(S) if and only if
there exists some subset T ⊆ S such that A = ⋃
B∈T B.

Definition 1.

1. A family of sets satisfies the abundance condition if there exists an element that belongs
to at least half of the sets.

2. Let P([n]) be the power set of [n]; that is, P([n]) is the set of all subsets of [n], then
F ⊆ P([n]) is a filter if i ∈ [n] and F ∈ F implies F ∪ {i} ∈ F.

Definition 2. S ⊆ P([n]) satisfies Reimer’s conditions if there exists a filter F ⊆ P([n])
and a bijection from S to F, A → FA such that:

1. A ⊆ FA (subset condition);

2. if A, B ∈ S and A ̸= B then [A, FA] ∩ [B, FB] = ∅ (non-interference condition).

Lemma 1. (Lemma 1.3 in [10]) If S is a non-trivial union-closed family of sets, then it
satisfies Reimer’s conditions.

As a part of Tim Gowers’ polymath project on the union-closed sets conjecture in 2016,
the following conjecture, a strengthening of the union-closed sets conjecture, was posed [5].

Conjecture 2. Any family that satisfies Reimer’s conditions satisfies the abundance condi-
tion.

Raz disproved this conjecture by constructing one such counterexample; that is, a family
S that satisfies Reimer’s conditions but not the abundance condition [9]. In her counterex-
ample, n = 8 and |S| = 11. She also proved that there is no counterexample with n < 8 or
|S| < 11.
 2

2 Observations

This section includes observations on some necessary properties for a family to be a coun-
terexample of Conjecture 2. Observations 1, 2, 4, 5 are proven in [9].

Observation 1. (Note 6 in [9]) We may assume F must contain all sets in P([n]) of size at
least n − 1.

Observation 2. (Fact 5 in [9]) If S satisfies the Reimer’s conditions and every member of
F has size at least n − 1, then there exists an element satisfying the abundance condition.

Observation 3. The set in S that is mapped to [n] ∈ F must be [n] itself.

Proof. Assume a set A ∈ P([n]), A ̸= [n] is mapped to [n]. There must be an element
k ∈ [n] such that k /∈ A. Let FB be the set in F of size n − 1 such that k /∈ FB. Then
FB ∈ [A, [n]] ∩ [B, FB], contradicting the non-interference condition.

Observation 4. If n is even, then we need at least 2 sets of size less than n − 1 in F to
possibly construct a counterexample to Conjecture 2. If n is odd, we need at least 3 sets of
size less than n − 1.

In the following discussion, we will focus on the smaller case in which n is even. By the non-
interference condition and Observation 4, there must be at least two sets of size n − 2 in F.
We further restrict to only consider families where the two necessary sets of size n − 2 in F
are the only sets in F that are of size less than n − 1. Moreover, we assume that the elements
that are missing in these two sets are disjoint. These assumptions specify a specific form of
filter F = {F0, F1, F2, . . . , Fn, Fn+1, Fn+2}, where F0 = [n], F1 = [n] \ {1}, F2 = [n] \ {2}, . . .,
Fn = [n] \ {n}, Fn+1 = [n] \ {1, 2}, Fn+2 = [n] \ {3, 4}. Let S = {S0, S1, . . . , Sn+2}, where Si
is mapped to Fi for i = 0, 1, . . . , n + 2.

Observation 5. (Note 8 [9]) Sn+1 ̸= ∅ and Sn+2 ̸= ∅

Before the next observation, we provide an equivalent formulation for the non-interference
condition. This formulation is particularly important in the proof of Observation 6.

Lemma 2. Let p and q be arbitrary elements in 0, 1, . . . , n + 2. [Sp, Fp] ∩ [Sq, Fq] = ∅ if and
only if there exists i ∈ [n] such that at least one of the following is true:

1. i ∈ Sp and i /∈ Fq

2. i ∈ Sq and i /∈ Fp

In the case of both p, q ∈ [n], this is the same as saying at least one of q ∈ Sp and p ∈ Sq is
true.

Proof. First we show the forward direction using a contrapositive argument. For the sake of
contradiction, assume that neither of the two statements are true. This implies Sp ⊆ Fq and
Sq ⊆ Fp, thus Sp ∪ Sq ∈ [Sp, Fp] ∩ [Sq, Fq], so [Sp, Fp] ∩ [Sq, Fq] ̸= ∅.
For the other direction, assume without loss of generality that there is some i such that
i ∈ Sp, and i /∈ Fq. Then for all P ∈ [Sp, Fp], we have i ∈ P . For all Q ∈ [Sq, Fq], we have
i /∈ Q. Therefore [Sp, Fp] ∩ [Sq, Fq] = ∅.
 3

Observation 6. Let x be the smallest set size in S, then n ≥ 4x + 4.

Proof. Let p be an arbitrary element in [n]. Because [Sp, Fp] ∩ [Sq, Fq] = ∅ for all q ∈ [n] \ {p}
by the non-interference condition, the sum of |Sp| and the number of appearances of element
p in all other Sq must be at least n − 1. Therefore, after accounting for double counting,
we have ∑
p∈[n] |Sp| ≥ n(n−1)
2 . Moreover, because [S1, F1] ∩ [Sn+1, Fn+1] = ∅, we have 2 ∈ S1.
Because [S2, F2] ∩ [Sn+1, Fn+1] = ∅, we have 1 ∈ S2. Because either one of 2 ∈ S1 and
1 ∈ S2 is necessary and sufficient for [S1, F1] ∩ [S2, F2] = ∅, the simultaneous existence
of 2 ∈ S1 and 1 ∈ S2 is not accounted in the previous argument of ∑
p∈[n] |Sp| ≥ n(n−1)
2 .
Similarly, from [S3, F3] ∩ [Sn+2, Fn+2] = ∅ and [S4, F4] ∩ [Sn+2, Fn+2] = ∅, we have 4 ∈ S3
and 3 ∈ S4. Therefore, we have ∑

p∈[n] |Sp| ≥ n(n−1)
2 + 2. To fail the abundance condition,
∑

k∈{0,1,...,n+2} |Sk| ≤ n( n
2 + 1) as |S| = n + 3 and n is even. Because |S0| = n by observation
3 and |Sn+1| ≥ x and |Sn+2| ≥ x, we have ∑
p∈[n] |Sp| ≤ n( n
2 + 1) − n − 2x. Solving for

inequality n( n
2 + 1) − n − 2x ≥ n(n−1)
2 + 2, we have n ≥ 4x + 4.

Observation 7. If there is a counterexample with such form of filter and satisfy n = 4x + 4,
then each element in [n] belongs to exactly n
2 + 1 sets in S.

Proof. This is a direct result of observation 6 . In this case, the minimum and maximum
value of ∑

p∈[n] |Sp| is equal. Therefore, we are required to maximize ∑
p∈{0,...,n+2} |Sp| without
satisfying the abundance condition.

3 Construction

Counterexamples with such form of filter and satisfy n = 4x + 4 indeed exist. Raz offered
a specific counterexample for x = 1. This section offers a way to construct such counterex-
amples for any x ≥ 2. The non-interference condition and the specific forms of Fn+1 and
Fn+2 provide certain restrictions on S1, S2, S3, and S4. After constructing these sets, We
then filled in the other sets with the help of the observations above. The final construction
is given below.
S0 = [n]
S1 = {2, n
2 + 1, . . . , n}
S2 = {1, 3, . . . , n
2 , n}
S3 = {1, 4, . . . , n
2 + 2}
S4 = {1, 3, n
2 + 3, . . . , n}
Sk1 = {1, 4, k1 + 1, . . . , n
2 + k1 − 2}, 5 ≤ k1 ≤ n
4 + 2
Sk2 = {1, 4, k2 + 1, . . . , n
2 + k2 − 3}, n
4 + 3 ≤ k2 ≤ n
2
S n
2 +2 = {2, 4, n
2 + 3, . . . , n − 1}
S n
2 +3 = {2, 3, n
2 + 4, . . . , n}
Sk3 = {2, 3, 5, . . . , k3 − n
2 + 1, k3 + 1, . . . , n}, n
2 + 4 ≤ k3 ≤ 3n
4
S 3n
4 +1 = {2, 3, 5, . . . , n
4 + 3, 3n
4 + 2, . . . , n − 1}
Sk4 = {2, 3, 5, . . . , k4 − n
2 + 2, k4 + 1, . . . , n}, 3n
4 + 2 ≤ k4 ≤ n − 1
Sn = {3, 5, . . . , n
2 + 2, 3n
4 + 1}
Sn+1 = { 3n
4 + 2, . . . , n}
 4

Sn+2 = {1, 5, . . . , n
4 + 2}
It can be checked by hand that the following hold.

1. The minimum set size of S in this construction is n
4 − 1, which is achieved by Sn+1 and
Sn+2

2. Reimer’s conditions are satisfied.

3. Each element in [n] appears in exactly n
2 + 1 member sets of S.

The verification of non-interference condition is included in the appendix.

4 Properties

The family S created under the above construction is not union-closed. In other words,
S ̸= cl(S). When x = 2, |S|
|cl(S)| = 15
133 ≈ 0.1128. When x = 3, |S|
|cl(S)| = 19
233 ≈ 0.0815. When

x = 4, |S|
|cl(S)| = 23
354 ≈ 0.0650. Unless explicitly specified, the discussion in this section only
applies to the type of counterexamples constructed in the previous section.

Theorem 1. If S is a family satisfying the construction given in Section 3, then |cl(S)| =
Θ(n2).

Proof. First we show |cl(S)| = O(n2). Define four families Sk1, Sk2, Sk3, Sk4 as

Sk1 ={Sk1:5 ≤ k1 ≤ n
4 + 2}

Sk2 ={Sk2: n
4 + 3 ≤ k2 ≤ n
2 }

Sk3 ={Sk3: n
2 + 4 ≤ k3 ≤ 3n
4 }

Sk4 ={Sk4: 3n
4 + 2 ≤ k4 ≤ n − 1}

Note that there are only 11 other sets in S. Therefore, proving |cl(Sk1 ∪ Sk2 ∪ Sk3 ∪ Sk4)| =
O(n2) is sufficient to show |cl(S)| = O(n2). To begin with, we have
cl(Sk1) = {{1, 4, k1a, . . . , k1b} : 6 ≤ k1a ≤ n
4 + 3, n
2 + 3 ≤ k1b ≤ 3n
4 , k1b − k1a ≥ n
2 − 3}
cl(Sk2) = {{1, 4, k2a, . . . , k2b} : n
4 + 4 ≤ k2a ≤ n
2 + 1, 3n
4 ≤ k2b ≤ n − 3, k2b − k2a ≥ n
2 − 4}
cl(Sk3) = {{2, 3, 5, . . . , k3a, k3b, . . . , n} : 5 ≤ k3a ≤ n
4 + 1, n
2 + 5 ≤ k3b ≤ 3n
4 + 1, k3b − k3a ≤ n
2 }
cl(Sk4) = {{2, 3, 5, . . . , k4a, k4b, . . . , n} : n
4 +4 ≤ k4a ≤ n
2 +1, 3n
4 +3 ≤ k4b ≤ n, k4b−k4a ≤ n
2 −1}
Because cl(Sk1 ∪ Sk2) = cl(cl(Sk1) ∪ cl(Sk2)), we have
cl(Sk1 ∪ Sk2) ⊂ {{1, 4, k5a, . . . , k5b} : 6 ≤ k5a ≤ n
2 + 1, n
2 + 3 ≤ k5b ≤ n − 3, k5b − k5a ≥ n
2 − 4}
Similarly, we have
cl(Sk3 ∪ Sk4) ⊂ {{2, 3, 5, . . . , k6a, k6b, . . . , n} : 5 ≤ k6a ≤ n
2 + 1, n
2 + 5 ≤ k6b ≤ n, k6b − k6a ≤ n
2 }
Then
cl(Sk1 ∪ Sk2 ∪ Sk3 ∪ Sk4) ⊂ C = {{1, . . . , k8a, k7a, . . . , k7b, k8b, . . . , n} : 5 ≤ k8a < k7a ≤
n
2 + 1, n
2 + 3 ≤ k7b < k8b ≤ n, k7b − k7a ≥ n
2 − 4, k8b − k8a ≤ n
2 }
From the inequalities constraints, we have k7b ≥ k7a+ n
2 −4 and k8b ≤ k8a+ n
2 < k7a+ n
2 . There-
fore, the sets in C can be partitioned to two different types. The first type contains the sets
where there is no gap between k7b and k8b; that is, they are of the form {1, . . . , k8a, k7a, . . . , n}.

5

The number of these sets is O(n
2), as each of k8a and k7a have linear in n choices. For the
sets where the gap between k7b and k8b does exist, for any fixed k7a, there are at most 6
choices for the pair (k7b, k8b) due to the two inequalities above. Therefore, the number of
sets that belong to the second type is also O(n2). Thus |C| = O(n
2). From the description
of cl(Sk1) above, we can obtain that cl(Sk1) = Ω(n
2) and thus cl(S) = Θ(n
2).

Corollary 1. limx→∞ |S|
|cl(S)| = 0.

Proof. This follows directly from |S| = Θ(n) and |cl(S)| = Θ(n2).

5 Conjectures

Conjecture 3. For x ≥ 5, |cl(S)| = 23
32n2 + 35
8 n − 21.

This conjecture has been verified for x = 5, 6, . . . , 12. Links to the scripts used in this
verificaiton can be found in the appendix.
 6

6 Appendix

There are two codes linked below. generator.cpp generates families and filters with the con-
struction given in this paper. The program asks for x, the minimum set size, as input. The
program outputs a file where each row corresponds to a set. The set elements are represented
in binary. For example, when n = 8, {1, 3, 4, 7, 8} will be represented as “1 0 1 1 0 0 1 1”
and {2, 4} will be represented as “0 1 0 1 0 0 0 0”. When a row ends with “S”, the set is in
the family. The set immediately after it, ending with “F”, is its correspond set in the filter.
The sets are in the same order as seen in the construction section previously.
uclosure.cpp accepts an input file in the same format as the output file from “generator.cpp”;
that is, families and filters are represented in binary, and each set in the family is followed
immediately by its corresponding set in the filter. The program then checks if the non-
interference condition is violated, and if there is any element satisfying the abundance con-
dition. The program also generates the closure of the family. It counts the size of the closure
and the numbers of sets in the closure of each specific size.

References

[1] R. Alweiss, B. Huang, and M. Sellke, Improved Lower Bound for Frankl’s Union-
Closed Sets Conjecture, 2022, arXiv: 2211.11731 [math.CO]

[2] I. Boˇsnjak and P. Markovi´c, The 11-element case of Frankl’s conjecture, The
Electronic Journal of Combinatorics, 15.1 (2008)

[3] H. Bruhn, P. Charbit, and J. A. Telle, The graph formulation of the union-closed
sets conjecture, The Seventh European Conference on Combinatorics, Graph Theory and
Applications, (2013), pp. 73–78.

[4] J. Gilmer, A constant lower bound for the union-closed sets conjecture, 2002, arXiv:
2211.09055 [math.CO]

[5] T. Gowers, FUNC1 - strengthenings, variants, potential counterexamples, Jan. 2016.

[6] E. Knill, Graph generated union-closed families of sets, 1994, arXiv: math/9409215
[math.CO]

[7] J. Liu, Improving the Lower Bound for the Union-closed Sets Conjecture via Condi-
tionally IID Coupling, 2023, arXiv: 2306.08824 [cs.IT]

[8] L. Pebody, Extension of a Method of Gilmer, 2022, arXiv: 2211.13139 [math.CO]

[9] A. Raz, Note on the Union-Closed Sets Conjecture, Electronic Journal of Combina-
torics, 24 (Apr. 2017).

[10] D. Reimer, An Average Set Size Theorem, Combinatorics, Probability and Computing,
12.1 (2003), pp. 89–93.
 7

[11] I. Rival, Graphs and order: The role of graphs in the theory of ordered sets and its
applications, Reidel, 1985.

[12] D. G. Sarvate and J. C. Renaud, On the Union-Closed Sets Conjecture, Ars Com-
binatoria, 27 (1989), pp. 149–154.

[13] W. Sawin, An improved lower bound for the union-closed set conjecture, 2023, arXiv:
2211.11504 [math.CO]

[14] L. Yu, Dimension-Free Bounds for the Union-Closed Sets Conjecture, Entropy, 25.5
(2023)
 8
