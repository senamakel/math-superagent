<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p53/pdf/ | converted from PDF -->

Note on the union-closed sets conjecture

Abigail Raz

Department of Mathematics
Rutgers University
New Jersey, U.S.A.

ajr224@math.rutgers.edu

Submitted: Apr 29, 2017; Accepted: Aug 30, 2017; Published: Sep 8, 2017
Mathematics Subject Classiﬁcations: 05D05

Abstract

The union-closed sets conjecture states that if a ﬁnite family of sets A ̸= {∅} is
union-closed, then there is an element which belongs to at least half the sets in A.
In 2001, D. Reimer showed that the average set size of a union-closed family, A, is
at least 1
2 log2 |A|. In order to do so, he showed that all union-closed families satisfy
a particular condition, which in turn implies the preceding bound. Here, answering
a question raised in the context of T. Gowers’ polymath project on the union-closed
sets conjecture, we show that Reimer’s condition alone is not enough to imply that
there is an element in at least half the sets.

1 Introduction

Given the set [n] = {1, . . . , n} and a family A ⊆ 2
[n] we say A is union-closed if for
A, B ∈ A we have A ∪ B ∈ A. The union-closed sets conjecture, due to P. Frankl [3],
states that if A ⊆ 2
[n] is union-closed and A ̸= {∅} then there is some element of [n]
which belongs to at least half the sets in A. One method of approaching this conjecture is
to look at the average frequency of an element or, equivalently, the average set size. The
following theorem of D. Reimer [2] was thus motivated by and can be shown to follow
from, the union-closed sets conjecture.

Theorem 1. If A ⊆ 2
[n] and is union-closed, then
∑
A∈A |A|
|A| ⩾ log2 |A|
2 (1)

We will say that F ⊆ 2
[n] is a ﬁlter if G ⊇ F and F ∈ F implies G ∈ F. Additionally,
for A ⊆ B ⊆ [n] deﬁne [A, B] := {C : A ⊆ C ⊆ B}. In order to prove Theorem 1, Reimer
introduced the following criterion for a family A ⊆ 2
[n]:

the electronic journal of combinatorics 24(3) (2017), #P3.53 1

Deﬁnition 2. We say A ⊆ 2
[n] satisﬁes Condition 1 if there exists a ﬁlter F ⊆ 2
[n] and
a bijection A ↦→ FA from A to F satisfying:

1. A ⊆ FA for all A ∈ A

2. For distinct A, B ∈ A we have [A, FA] ∩ [B, FB] = ∅.

Reimer’s proof of Theorem 1 consists of two steps. He ﬁrst shows that every union-
closed family A satisﬁes Condition 1. He then shows that Condition 1 implies Theorem 1.
In 2016, T. Gowers began a polymath project focused on the union-closed sets con-
jecture. In the comments on the initial post I. Balla ﬁrst proposed:

Conjecture 3. Assume A ⊆ 2
[n] satisﬁes Condition 1. Then there is an element x ∈ [n]
in at least half the sets of A.

Gowers reiterates Conjecture 3 in his second post focused on strengthenings of the
union-closed sets conjecture. In the comments there is a discussion of a possible coun-
terexample, and it is stated that all families with ground set at most 5 and a random
sampling of families with ground set at most 12 have been conﬁrmed to satisfy Conjecture
3 [1].
The conjecture is certainly a natural one to consider: Reimer’s work has been perhaps
the most successful in ﬁnding a way to exploit the union-closed hypothesis, and one would
like to decide whether more can be gotten from his approach, particularly as ﬁnding a way
into the problem has proved so diﬃcult. The polymath project’s lack of recent progress,
after much initial enthusiasm, may be considered further evidence of this diﬃculty.
As Reimer showed that all union-closed families satisfy Condition 1, Conjecture 3 is
clearly a strengthening of the union-closed sets conjecture. The purpose of this note is to
show that Conjecture 3 is false.

2 Counterexample

In what follows we will always have A and F as in Deﬁnition 2.

Note 4. An equivalent way of stating the second part of Condition 1 is that at least one
of A \ FB or B \ FA is non-empty.

We will use the following notation:

• Ax = {A ∈ A : x ∈ A}

• A0 is the set for which FA0 = [n]

• Ai is the set for which FAi = [n] \ {i} for i ∈ [n]

• Bi,j is the set for which FBi,j = [n] \ {i, j} for i ̸= j ∈ [n]

Before giving the counterexample we will brieﬂy describe how we found it and indicate
why no smaller example is possible. The following observation was our starting point.

the electronic journal of combinatorics 24(3) (2017), #P3.53 2

Fact 5. Assume A satisﬁes Condition 1. If every set in F has size at least n − 1 then
there is an element in at least half of the sets of A.

Proof. Without loss of generality assume F = {[n]} ∪ {[n] \ {i} : i ∈ [k]}. Hence,
|F| = |A| = k + 1. By Note 4 we know that [k] ⊆ A0. Now we will view each Ai as
a vertex labelled i in a digraph, D, on vertex set [k], with (i, j) an edge exactly when
i ∈ Aj. Again by Note 4 we know that D must contain a tournament (an orientation
of Kn). Furthermore, the number of sets containing i is simply the out-degree of i plus
1 (since i ∈ A0). Since D has k vertices and contains a tournament it has maximum
out-degree at least k−1
2 . Hence there is always an element in at least k+1
2 members of
A.
 Assume n is the smallest integer such that there is a counterexample to Conjecture
3 on [n] and A is such a counterexample with corresponding ﬁlter F. We will use the
following three observations to show that n ⩾ 8, and then exhibit a counterexample when
n = 8.

Note 6. F must contain all sets of size n − 1.

Proof. Suppose instead that the elements of F of size n − 1 are [n] \ {i} for i ∈ [k] with
k < n. Since F is a ﬁlter we have {k + 1, . . . , n} ⊆ F for all F ∈ F, implying that the
condition in Note 4 is not aﬀected if we replace each X ∈ A ∪ F by X \ {k + 1, . . . , n}.
This produces a counterexample on a smaller set, contradicting the minimality of n.

Restrict A to A
′ := {Ai}n
i=0. If n is even then there exists x ∈ [n] with |A
′
x| ⩾ n+2
2 .
Hence we need at least two sets in A \ A
′. (If n is odd similar reasoning shows that there
must be at least three sets in A \ A′.)
In our example we will take n to be even and F to consist of [n] \ {1, 2} and [n] \ {3, 4}
along with all sets of size at least n − 1. Thus |F| = |A| = n + 3, A0 = [n], and we want
to arrange that |Ax| ⩽ n
2 + 1 for all x ∈ [n]. We will use the same digraph, D, as in the
proof of Fact 5 (with (i, j) an edge if and only if i ∈ Aj). Note that the Bi,j’s do not
directly aﬀect the digraph.

Note 7. The sum of the out-degrees in D must be at least n2−n
2 + 2.

Proof. Recall that by Note 4 D must contain a tournament. Additionally, by Note 4 if
Bi,j ∈ A then i ∈ Aj and j ∈ Ai. Thus we must have at least one additional out-degree
for every Bi,j.

Note 8. B1,2 and B3,4 must both be non-empty,

Proof. Without loss of generality 1 ∈ B3,4, since B1,2 and B3,4 must satisfy the condition
of Note 4. Additionally, if B1,2 = ∅ then to satisfy Note 4 all other sets in A must contain
1 or 2. However, A0 contains both 1 and 2, so one of 1 or 2 must appear in at least half
the sets, contradicting that A is a counterexample.

the electronic journal of combinatorics 24(3) (2017), #P3.53 3

By Note 8 we must have at least 2 vertices with out-degree no more than n
2 − 1. The
remaining out-degrees must still be no more than n
2 . Combining this with Note 7 we
have the inequality 2( n
2 − 1) + (n − 2)( n
2 ) ⩾ n2−n
2 + 2, i.e. n ⩾ 8. (If |A \ A′| > 2 then
we get even more “extra” degrees and the lower bound on n increases.) When n is odd
similar consideration gives n ⩾ 13; so, since our example does indeed use n = 8 it is of
the smallest possible size.

Counterexample 9. Here we will take our universe to be [8]. Our family A consists of
the following 11 sets:

• A0 = [8]

• A1 = {2, 4, 6, 7, 8}

• A2 = {1, 3, 5, 8}

• A3 = {1, 4, 7, 8}

• A4 = {2, 3, 5, 6}

• A5 = {1, 3, 7}

• A6 = {2, 3, 5}

• A7 = {2, 4, 6}

• A8 = {4, 5, 6, 7}

• B1,2 = {8}

• B3,4 = {1}

We (or our computers) can easily check that the requirement in Note 4 is satis-
ﬁed (a short maple script can be found at http://sites.math.rutgers.edu/~ajr224/
counterexample-check.txt.) and that each element appears in at most 5 sets. The
bijection between A and F is given explicitly in the appendix.

Acknowledgements

I would like to thank Jeﬀ Kahn for suggesting this problem.

References

[1] Timothy Gowers. Func1 - strengthenings, variants, potential counterexamples.
https://gowers.wordpress.com/2016/01/29/
func1-strengthenings-variants-potential-counterexamples, January
2016. [Online].

the electronic journal of combinatorics 24(3) (2017), #P3.53 4

[2] David Reimer. An average set size theorem. Combinatorics, Probability, and Com-
puting, 12(1):89–93, 2003.

[3] Ivan Rival, editor. Graphs and Order, volume 147 of Nato Science Series C:
Springer, 1st edition, 1985.

3 Appendix

Below is the complete bijection between A and F in our counterexample. All the sets are
represented by their indicator vectors:

A0 ↦→ FA0














1
1
1
1
1
1
1
1














 ↦→
 













1
1
1
1
1
1
1
1














 A1 ↦→ FA1














0
1
0
1
0
1
1
1














 ↦→
 













0
1
1
1
1
1
1
1














 A2 ↦→ FA2













1
0
1
0
1
0
0
1














 ↦→
 













1
0
1
1
1
1
1
1














 A3 ↦→ FA3














1
0
0
1
0
0
1
1














 ↦→
 













1
1
0
1
1
1
1
1














 A4 ↦→ FA4














0
1
1
0
1
1
0
0














 ↦→
 













1
1
1
0
1
1
1
1















A5 ↦→ FA5














1
0
1
0
0
0
1
0














 ↦→
 












1
1
1
1
0
1
1
1














 A6 ↦→ FA6














0
1
1
0
1
0
0
0














 ↦→
 













1
1
1
1
1
0
1
1














 A7 ↦→ FA7














0
1
0
1
0
1
0
0














 ↦→
 













1
1
1
1
1
1
0
1














 A8 ↦→ FA8













0
0
0
1
1
1
1
0














 ↦→
 












1
1
1
1
1
1
1
0














 B1,2 ↦→ FB1,2














0
0
0
0
0
0
0
1














 ↦→
 













0
0
1
1
1
1
1
1














 B3,4 ↦→ FB3,4














1
0
0
0
0
0
0
0














 ↦→
 













1
1
0
0
1
1
1
1















the electronic journal of combinatorics 24(3) (2017), #P3.53 5
