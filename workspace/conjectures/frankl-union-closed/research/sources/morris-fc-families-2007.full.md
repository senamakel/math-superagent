<!-- source: https://arxiv.org/pdf/math/0702348 | converted from PDF -->

arXiv:math/0702348v1  [math.CO]  13 Feb 2007FC-FAMILIES, AND IMPROVED BOUNDS FOR
FRANKL’S CONJECTURE

ROBERT MORRIS

Abstract. A family of sets A is said to be union-closed if {A∪B :
A, B ∈ A} ⊂ A. Frankl’s conjecture states that given any ﬁnite
union-closed family of sets, not all empty, there exists an element
contained in at least half of the sets. Here we prove that the con-
jecture holds for families containing three 3-subsets of a 5-set, four
3-subsets of a 6-set, or eight 4-subsets of a 6-set, extending work of
Poonen and Vaughan. As an application we prove the conjecture in
the case that the largest set has at most nine elements, extending
a result of Gao and Yu. We also pose several open questions.

1. Introduction

A family of sets A is called union-closed if A ∪ B ∈ A for every pair
of sets A, B ∈ A. The Union-Closed Sets Conjecture, which is also
known as Frankl’s Conjecture, and is generally attributed to P. Frankl
in 1979 (see [1], [2]), is as follows.

The Union-Closed Sets Conjecture. If A is a ﬁnite union-closed
family of sets, not all empty, then there exists an element belonging to
at least half of the sets of A.

By Corollary 1 of [4] we may assume that the sets of A are ﬁnite,
so, writing P(n) for the power set of {1, . . . , n}, let A ⊂ P(n) and
|A| = m.
Very little progress has been made on this simple-sounding problem.
David Reimer [5] recently proved that the average set-size in a union-

closed family is at least 1
2 log2(m), but this gives only weak bounds
on the number of appearances of the most common element. We shall
continue a route into the problem initiated by Poonen [4], and contin-
ued by Vaughan [7], [8], [9], and also by Gao and Yu [3]. The approach
is motivated by the following simple observations. First, let A be a
union-closed family of sets, and suppose that A contains a one-element

The author was supported during this research by a Van Vleet Memorial Doctoral
Fellowship. 1

2 ROBERT MORRIS

set {x}. Then clearly x is in at least half the sets of A. Similarly, if
A contains a two-element set {x, y}, then at least one of x and y is
contained in at least half the sets of A (consider the four sub-families
containing both, exactly one, and neither of the pair x and y).
Following Vaughan [7], call B an F C(k)-family if it is a union-closed
family of sets containing ∅ and whose largest set has k elements, and
it has the property that given any union-closed family A ⊇ B, one of
the k elements of (the largest set in) B is in at least half the sets of A.
Call a family F C if it is F C(k) for some k, and call an F C(k)-family
proper if it contains no strictly smaller F C-family. By the observations
above, {∅, {x}} is an F C(1)-family, and {∅, {x, y}} is an F C(2)-family.
However, a single 3-element set is not an F C(3)-family (an example
showing this was given in [6]), so there are no proper F C(3)-families.
Poonen studied these families, and gave necessary and suﬃcient con-
ditions for a family to be F C (see Poonen’s Theorem, below). He used
his result to show that the conjecture holds for any family which con-
tains three of the 3-subsets of a 4-set, and deduced that the conjecture
holds if n ⩽ 7 or m ⩽ 28. Gao and Yu [3] later improved these bounds
to n ⩽ 8 and m ⩽ 32. Vaughan [7], [8], [9] studied F C(k)-families
for small values of k, and showed that the conjecture holds for any
family which contains all ﬁve of the 4-subsets of a 5-set, or ten of
the 4-subsets of a 6-set, or three 3-subsets of a 7-set with a common
element. Given a set system S ⊂ P(n), we deﬁne the family gener-
ated by S to be the smallest union-closed family containing S ∪ ∅, i.e.
{A ∈ P(n) : A = A1∪. . .∪Ar, where Ai ∈ S∪∅ for 1 ⩽ i ⩽ r}. Since
determining exactly which families are F C seems to be complicated for
k ⩾ 5, we shall concentrate on a slightly simpler question: how many
k-sets in [n] = {1, . . . , n} necessarily generate an F C-family? To this
end, write F C(k, n) for the minimal m such that any m of the k-sets
in [n] generate an F C-family.
As noted above, Poonen [4] showed that F C(3, 4) = 3, and Vaughan [7]
showed that F C(4, 5) ⩽ 5 and F C(4, 6) ⩽ 10. In this paper we shall
improve on the results of Vaughan, by determining exactly which fam-
ilies are F C(5), and ﬁnding new examples of F C(6)-families. In par-
ticular, we shall show that F C(3, 5) = 3, F C(4, 5) = 5, F C(3, 6) = 4
and 7 ⩽ F C(4, 6) ⩽ 8. In other words, we shall prove that the conjec-
ture holds for any union-closed family which contains any three of the
3-subsets of some 5-set, four of the 3-subsets of some 6-set, or eight of
the 4-subsets of some 6-set. As an application of our results, we shall
prove the conjecture in the cases n ⩽ 9 and m ⩽ 36, improving the
bounds of Gao and Yu. We shall also prove a conjecture of Vaughan [7]

FC-FAMILIES AND FRANKL’S CONJECTURE 3

on union-closed families with many 2-sets, and discuss the asymptotics
of F C(k, n) as n → ∞.
In this paper we shall prove the following theorems. The ﬁrst deter-
mines exactly which families are F C(5).

Theorem 1. A sub-family of P(5) is a proper F C(5)-family if, and
only if it is generated by one of the following set systems (under some
permutation of {1, 2, 3, 4, 5}).

(a) Any three of the 3-subsets,
(b) {1, 2, 3}, {1, 2, 4} and {1, 3, 4, 5},
(c) {1, 2, 3}, {1, 4, 5} and {2, 3, 4, 5},
(d) {1, 2, 3}, {1, 4, 5}, {1, 2, 3, 4}, {1, 2, 3, 5}, {1, 2, 4, 5} and {1, 3, 4, 5},
(e) {1, 2, 3}, {1, 2, 4, 5}, {1, 3, 4, 5} and {2, 3, 4, 5},
(f ) All ﬁve 4-sets.

In particular F C(3, 5) = 3 and F C(4, 5) = 5.

The next gives some new examples of F C(6)-families.

Theorem 2. F C(3, 6) = 4 and 7 ⩽ F C(4, 6) ⩽ 8.

As an application of our results, we prove the following theorem.

Theorem 3. The Union-Closed Sets Conjecture holds in the case n =
9.
 We shall also prove the following theorem on union-closed families,
conjectured by Vaughan [7], and proved by her in the cases n = 5, 6
and 7, which will be useful in proving the above results.

Theorem 4. If A is a union-closed family in P(n) and contains at

least (n − 1
2
 ) + 1 of the 2-sets, then

|{A ∈ A : |A| = n − k}| ⩾ |{A ∈ A : |A| = k}|

for every 0 ⩽ k ⩽ ⌊n
2
 ⌋.

The rest of the paper is organised as follows. In Section 2 we shall
describe the tools we shall use to prove our main theorems; in Section 3
we shall prove Theorem 4; in Section 4 we shall prove Theorems 1 and
2; in Section 5 we shall prove Theorem 3; in Section 6 we shall discuss
the asymptotics of F C(k, n); and in Section 7 we shall discuss some of
our questions and conjectures relating to this work.

4 ROBERT MORRIS

2. Our method of approach

Our main tool in ﬁnding F C-families will be the following theorem
of Poonen [4].

Poonen’s Theorem. If B is a union-closed family containing ∅ whose
largest set has n elements, say {1, . . . , n}, then the following are equiv-
alent:
(a) B is an F C(n)-family
(b) There exist non-negative real numbers c1, . . . , cn summing to 1
such that for every union-closed family A ⊂ P(n) such that
A ⊎ B ⊆ A, n∑

i=1 ci|Ai| ⩾ |A|
2

where A ⊎ B = {A ∪ B : A ∈ A, B ∈ B} and Ai = {A ∈ A : i ∈
A}.

It will be convenient to allow the ci to be integers, and to deﬁne

K(A) = ∑

A∈A
 (∑

i∈A ci − ∑

i /∈A ci
)
 = 2
 n∑

i=1
 ∑

A∈A (ciI[i ∈ A]) − |A|
 n∑

i=1 ci,

where I[S] as usual denotes the indicator function of the event S. Write

Ni for ∑

{A∈A:|A|=i}
 


∑

j∈A cj − ∑

j /∈A cj


, the contribution of the i-sets to

K(A), and notice that condition 2 of the theorem holds for a given

family A if and only if K(A) =
 n∑

i=0 Ni ⩾ 0. Whenever possible, we

shall choose the ci to be integers, but the reader should be aware that
when proving that no such ci exist (for certain families), we shall revert
to real numbers summing to one. It will always be clear which situation
we are in, and we trust this will not cause any confusion. We shall write
c = 1 if ci = 1 for all i, and ni for the number of i-sets in A.
Our proof will also use the following lemmas of Vaughan [7], and the
trivial observation below.

Lemma A. Suppose that A and B are union-closed families in P(n)
such that A ⊎ B ⊂ A, and that there are exactly r k-sets which are in

B but not A. Suppose also that r = (ak
k
 ) + ( ak−1
k − 1
) + . . . + (
at
t
 )

with ak > . . . > at ⩾ t ⩾ 1.

FC-FAMILIES AND FRANKL’S CONJECTURE 5

Then for each 1 ⩽ j ⩽ k, the number of j-sets in A is bounded above
by dj(n, k, r), where

dj(n, k, r) = (n
j
 ) − (
ak
j
 ) − ( ak−1
j − 1
) − . . . − ( at
t − k + j
)

Lemma B. Let t(i) = |{A ∈ A : i ∈ A, |A| = 2}|. If t(i) ⩾ k + 1 for
all i ∈ [n], then A contains all of the (n − k)-sets in P(n).

Remark 1. Note that in general if tj(i) = |{A ∈ A : i ∈ A, |A| = j}|

and tj(i) ⩾ (
n − 1
j − 1
) − (n − k − 1
j − 1
 ) + 1 for some j and all i ∈ [n], then

A contains all of the (n − k)-sets in P(n), since for any (n − k)-set K
and any i ∈ K there exists a j-set L such that i ∈ L ⊂ K.

Observation 5. If A and B are union-closed families with A ⊎B ⊆ A,
and ∅ ∈ A, then B ⊆ A.

3. Proof of Theorem 4

Proof. The cases k = 0 and k = n
2 are trivial, so ﬁx 1 ⩽ k ⩽ ⌊ n − 1
2
 ⌋

and suppose that the theorem fails for k (i.e. A contains at least(
n − 1
2
 )+ 1 of the 2-sets and more k-sets than (n−k)-sets). Note that

we may assume that A is generated by its 2-sets and its k-sets, since the
addition of other sets can only increase the number of (n−k)-sets. Con-
sider the graph G with [n] as the vertices and ij ∈ E(G) ⇔ {i, j} ∈ A
(so subgraphs of G with no isolated vertices correspond to sets in A),
and note that if each vertex of G has degree at least k + 1 then we are
done by Lemma B.

Claim: Suppose either more than one element has degree at most k, or
exactly one element has this property and in the induced subgraph on
the other n − 1 vertices some vertex has degree at most k. Then n is

odd, k = n − 1
2 and G contains an induced copy of Kn−2.

Proof of claim. We must be missing at least n − 1 − k edges from the
ﬁrst vertex, and at least n − 2 − k diﬀerent edges from the second
vertex. However, at most n − 2 edges are missing from G, thus n − 2 ⩾

(n − 1 − k) + (n − 2 − k), and so k ⩾ n − 1
2 . It follows that k = n − 1
2 ,
hence n is odd, and equality holds everywhere, so all missing edges are
incident with one of these two vertices. □

6 ROBERT MORRIS

First assume that the assumptions of the claim fail to hold. Thus
we may assume that exactly one vertex has degree at most k. Let
this element be u, suppose u lies in exactly r of the 2-sets in A (so

1 ⩽ r ⩽ k ⩽ ⌊n − 1
2
 ⌋). Note also that, by Lemma B, A contains all of

the (n − k)-sets and all of the (n − k − 1)-sets in P([n] − u).
Consider which of the (n − k)-sets in P(n) may be missing from A.
Such a set must contain u by the comment above, and cannot contain
any element of Γ(u) = {v : {u, v} ∈ A}, as then it would be the union
of some (n − k − 1)-set in P([n] − u) with some pair {u, v} ∈ A. So

there are at most (n − r − 1
n − k − 1
) such sets.

Now observe that any k-set which contains u but no neighbour of u

is not generated by the 2-sets of A. There are (n − r − 1
k − 1
 ) such sets.

Since (n − r − 1
n − k − 1
) ⩽ (
n − r − 1
k − 1
 ) when r ⩾ 1, we must have some

of these sets in A as generating sets. However, if such a k-set A ∈ A,
then every (n − k)-set containing A and n − 2k diﬀerent elements of
P([n] − u − Γ(u)) is also in A, by taking the union of A with some
(n − k − 1)-set in P([n] − u − Γ(u)) containing A \ u. Moreover each
of these (n − k)-sets was counted as missing from A above.

In this way, each of these k-sets generates (
n − k − r
n − 2k
 ) new (n − k)-

sets, and each (n−k)-set is generated by (n − k − 1
k − 1
 ) of the k-sets. But

now simply observe that (
n − k − r
n − 2k
 ) = (
n − k − r
k − r
 ) ⩽ (
n − k − 1
k − 1
 )

when r ⩾ 1, and it is clear that the number of missing (n − k)-sets
must be no greater than the number of missing k-sets.

We are left to deal with the (easier) case that n is odd, k = n − 1
2 and
G contains an induced copy of Kn−2. Let the remaining two vertices
be u and v and let d(u) ⩽ d(v). We may assume that the assumptions

of the claim hold, and that e(G) = (
n − 1
2
 ) + 1.

Suppose ﬁrst that uv ∈ E(G). Then u and v must be missing n − 1
2
and n − 3
2 edges respectively, and the only (n − k)-set which may be

missing from A is [n] − Γ(u). However, if A contains all the k-sets then
it contains this set as well, so we are done.

FC-FAMILIES AND FRANKL’S CONJECTURE 7

So assume uv /∈ E(G), and that each of u and v is missing n − 1
2
edges. Then the only (n − k)-sets which may be missing are [n] − Γ(u)
and [n] − Γ(v). As before if either of these is actually in A then we
are done. But if A contains any k-set which is a subset of one of these
(n − k)-sets and contains both u and v, then A must also contain that
(n − k)-set, and since there are at least two such k-sets when n ⩾ 7,
and the remaining cases are trivial, we are done. □

4. F C(k)-families for small values of k

First let us consider the case k = 5. In [7], Vaughan showed that a 5-
set with all its 4-subsets, and a 5-set with four of its 4-subsets and four
of its 3-subsets are F C(5)-families, using Poonen’s Theorem with c = 1.
By using diﬀerent values of ci and a (fairly simple-minded) computer
program, we have been able to show much more, characterising exactly
the F C(5)-families.

Proof of Theorem 1. First we show that the given families are F C, us-
ing Poonen’s Theorem. The required inequalities, K(A) ⩾ 0 for all
A ⊂ P(5) such that A ⊎ B ⊆ A, follow by a tedious case analysis (ei-
ther by hand or by computer) once the correct values of ci have been
identiﬁed. The search is narrowed by considering only solutions to the
ﬁve inequalities given by A = B ⊎ P([5] \ {i}) for i = 1, . . . , 5.
The following are examples of c’s which work:
(1) If the three 3-sets are contained in some 4-set then let c = 1 (this
is Corollary 4 of [4]). If the 3-sets cover [5] then there are three cases
to consider:
1. {1, 2, 3}, {1, 2, 4}, {1, 2, 5}: c = (3, 3, 2, 2, 2) will do;
2. {1, 2, 3}, {1, 2, 4}, {1, 3, 5}: c = (6, 5, 5, 3, 3) works;
3. {1, 2, 3}, {1, 2, 4}, {3, 4, 5}: c = (2, 2, 2, 2, 1) is an example.

(It is easy to see that all other possibilities are just permutations of
one of these three.)
For the rest of the set systems listed in Theorem 1, suitable values of
c are
(2) c = (24, 22, 19, 19, 4)
(3) c = (4, 3, 3, 3, 3)
(4) c = (4, 3, 3, 3, 3)
(5) c = (14, 14, 14, 9, 9)
(6) c = 1 (This is Theorem 4.2 of [7].)

8 ROBERT MORRIS

Now we show that these are the only proper F C(5)-families (up to
permutations of {1, 2, 3, 4, 5}). It suﬃces to show that the following
families are not F C.
1. {1, 2, 3}, {1, 4, 5}, {1, 2, 3, 4}, {1, 2, 3, 5} and {1, 2, 4, 5}
2. {1, 2, 3}, {1, 2, 4}, {1, 2, 3, 4}, {1, 2, 3, 5} and {1, 2, 4, 5}
3. {1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 5}, {1, 2, 4, 5} and {1, 3, 4, 5}
In each case we show that no values of ci simultaneously satisfy the
inequalities given by K(A) ⩾ 0, with A = B⊎P([5]−j) for j = 1, . . . , 5.
The result then follows by Poonen’s Theorem.
1. Noting that c1 + c2 + c3 + c4 + c5 = 1, the ﬁve inequalities reduce
to
 c1 ⩽ 1
4 (1)

4c1 − 12c2 + 2c3 ⩾ −1 (2)
9c1 + 5c2 + 5c3 ⩾ 4 (3)
c1 + c2 ⩾ 3c3 (4)

From (1) and (2) we have c2 ⩽ c3 + 1
6 and from (1) and (3) we have

c2 + c3 ⩾ 7
20 . But now, since 7
20 ⩽ c2 + c3 ⩽ 7c3 + 1
6 ⇒ c3 ⩾ 11
70, 3c3 ⩽

c1 + c2 ⩽ 2c3 + 5
12 ⇒ c3 ⩽ 5
34 and 5
34 < 11
70 , we have a contradiction.
2. Form the inequalities as before, and noting the symmetries in B,
let x = c1 + c2, y = c3 + c4 and z = c5 + c6. Adding inequalities and
making the substitution z = 1 − x − y gives

x ⩽ y (5)
2x ⩾ 3y (6)
16x + 14y ⩾ 13 (7)

But (5) and (6) ⇒ x = y = 0, so again we have a contradiction.
3. Again noting the symmetries we let x = c1 and y = c2 + c3, and
reduce as before to get
 − 6x + y ⩾ −1 (8)
4x − 5y ⩾ −1 (9)
9x + 7y ⩾ 5 (10)

But (8) and (9) ⇒ x ⩽ 3
13 and y ⩽ 5
13, so 9x + 7y ⩽ 62
13 < 5,

contradicting (10). □

FC-FAMILIES AND FRANKL’S CONJECTURE 9

We next consider F C(6)-families. Vaughan [7] proved that any ten
4-sets, or any eight 4-sets together with six 5-sets, generate an F C-
family. Theorem 2 improves these results, and also gives the exact
number of 3-sets in {1, . . . , 6} which are guaranteed to generate an
F C-family.

Proof of the ﬁrst half of Theorem 2. The upper bound again follows by
computer-based case analysis. If any three of the 3-sets do not cover all
six elements then we are done by Theorem 1. Hence each element of [6]
must lie in at least (and so exactly) two of the 3-sets. If some pair of 3-
sets intersect in two elements then the 3-sets must be {1, 2, 3}, {1, 2, 4},
{3, 5, 6} and {4, 5, 6} (under some permutation of {1, 2, 3, 4, 5}). Oth-
erwise the sets are {1, 2, 3}, {1, 4, 5}, {2, 4, 6} and {3, 5, 6}. In either
case condition 2 of Poonen’s Theorem is satisﬁed by c = 1.
The lower bound follows by applying the method of Theorem 1 to the
family generated by {1, 2, 3}, {1, 2, 4}, and {3, 5, 6}. Let x = c1 + c2,
y = c3 and z = c4, and get
 y + z ⩾ x
4y + z ⩽ 1
x ⩾ 3z
x + 2y + z ⩾ 1

Now, from the ﬁrst and third equations we get y ⩾ 2z, and so by

the second, z ⩽ 1
9 . Hence x + 2y + z ⩽ 3y + 2z ⩽ 3 (1 − z
4
 ) + 2z =

3
4 + 5z
4 < 1, a contradiction. □

Unfortunately from now on the case analysis involved in proving
upper bounds on F C(k, n) becomes too lengthy to be performed by
our computer program, so for the second half of Theorem 2 we need to
be a little more clever.

Proof of the second half of Theorem 2. Let B be generated by eight 4-
sets, and note that each element of [6] = {1, 2, 3, 4, 5, 6} must be con-
tained in at least four of the 4-sets, else we are done by Theorem 4.2
of [7]. We shall show that in all but a few special cases the result fol-
lows by Poonen’s Theorem with c = 1, and then deal with those cases
separately.
Recall that ni denotes the number of i-sets in A. In all cases we may
assume that n1 ⩽ 5, and by Theorem 4 we may assume that n2 ⩽ 10
when c = 1. Also recall Lemma A and observe that a trivial calculation
(as in [7]) gives us d2(6, 4, r) ⩽ 10 − r for all 1 ⩽ r ⩽ 10.

10 ROBERT MORRIS

Suppose ﬁrst that the eight 4-sets generate at least 5 of the 5-sets,

and let c = 1, so K(A) =
 3∑

i=1 i (n3+i − n3−i). Then n5 ⩾ n1, since if

A is missing at least two of the 5-sets in B then by Lemma A n1 ⩽
d1(6, 5, 2) = 0, if A is missing exactly one of the 5-sets in B then
n1 ⩽ d1(6, 5, 1) = 1, and if A contains all of the 5-sets in B then
n5 ⩾ 5 ⩾ n1 by assumption. Also, since d2(6, 4, r) ⩽ 10 − r for all
1 ⩽ r ⩽ 8, Theorem 4 and Lemma A give us n4 − n2 ⩾ −2.
Now, if ∅ /∈ A then K(A) ⩾ 0 , so assume that ∅ ∈ A. Then n5 ⩾ 5
and n4 ⩾ 8, and so if K(A) < 0, we must have n1 = n5 = 5. But the
1-sets now generate at least one new 4-set, so n4 ⩾ 9 and n2 = 10. We
are done if each 5-set in [6] contains at most three 4-sets of B, since
then n4 ⩾ 10, so assume some four of the 4-sets lie in {1, 2, 3, 4, 5}.
Also note that since n5 = 5, at least seven of the 4-sets in B contain i,
where [6] \ {i} is the missing 5-set.

Claim 1: If at least seven of the 4-sets contain 1, no other element
is contained in more than six, and four of the 4-sets are contained
in {1, 2, 3, 4, 5}, then the conditions of Poonen’s Theorem hold with
c = (11, 9, 9, 9, 9, 9).

Proof of claim. The values of ci were chosen by considering P([6] \
{i}) ⊎ B for i = 2, . . . , 6, assuming c2 = . . . = c6 and minimising c1.
Let A ⊂ P(5) such that A ⊎ B ⊆ A, and note that we still have that A
contains at least n1 of the 5-sets and n2 − 2 of the 4-sets of B. Recall
that Ni denotes the contribution to K(A) of the i-sets in A, and note
that N3 ⩾ −20.
Consider ﬁrst the case ∅ /∈ A. Then N6 + N0 = +56, since we may
assume [6] ∈ A. Also N4 + N2 ⩾ −44, since 2-sets contribute at least
−20, and all but at most one of the 4-sets in B contributes 20, the other
contributing 16. Suppose {2, 3, 4, 5, 6} /∈ A. Then we have N3 ⩾ −8,
and N5 + N1 ⩾ 0, so K(A) ⩾ 0. If {2, 3, 4, 5, 6} ∈ A then N5 + N1 ⩾ 34
(assuming n1 ⩽ 5), so since N3 ⩾ −20, K(A) ⩾ 0 still holds.
So assume now that ∅ ∈ A, so n4 ⩾ 8 and n5 ⩾ 5 by Observation 5.
First note that if n1 ⩽ 3 then N5+N1 ⩾ 76, N4+N3+N2 ⩾ −64 and we
are done. So assume n1 ⩾ 4 and again suppose that {2, 3, 4, 5, 6} /∈ A.
If n1 = 4 then N5 +N1 ⩾ 38, N3 ⩾ −8 and so if K(A) < 0 then n2 = 10
and n4 = 8. But this is impossible since any four 1-sets and ten 2-sets
clearly generate either {2, 3, 4, 5, 6} or a 4-set not in B. If n1 = 5, then
since {2, 3, 4, 5, 6} /∈ A, the only possibilities for A are P([6] \ {i}) ⊎ B
and P([6] \ {i}) ⊎ B ⊎ {1, i}, where i ∈ {2, 3, 4, 5, 6} (we may assume no
extra 3-sets containing 1 are added to A, since these increase K(A)).

FC-FAMILIES AND FRANKL’S CONJECTURE 11

We chose c so that K(A) ⩾ 0 in the former case, and the latter gives
a higher value of K(A), since new 4-sets are generated.
Hence we may assume that {2, 3, 4, 5, 6} ∈ A, and so n5 = 6. If
n1 ⩽ 4 we get N5 + N1 ⩾ 72 and are done as before, so assume also
that n1 = 5. If {1} /∈ A we get N5 + N1 = 34 and n4 ⩾ 12, but n2 ⩾
13 ⇒ n4 = 15, so we are done. But if {1} ∈ A we get N5 + N1 = 38,
N3 ⩾ −8 and N4 + N2 ⩾ −24 (since n4 ⩾ 9), so again K(A) ⩾ 0, and
the proof of claim 1 is complete. □

So from now on we may assume that B contains at most four 5-sets.
But since any two 4-sets in a 5-set generate that 5-set (so a missing 5-
set implies four missing 4-sets), and each 4-set is contained in only two
5-sets of [6], eight 4-sets in [6] must generate at least four 5-sets. Hence
B contains exactly four 5-sets. But now we can reduce the problem to
a single family, for suppose wlog that {1, 3, 4, 5, 6} and {2, 3, 4, 5, 6}
are the 5-sets missing from B. Then B must contain all 4-sets which
contain both 1 and 2, one containing 1 and not 2, and one containing
2 and not 1. These last two sets must have intersection 2, as otherwise
we would have ﬁve 4-sets in {1, 2, 3, 4, 5}, and by symmetry we may
take any pair with this property.
It follows that the proof of the upper bound is completed by the
following claim.

Claim 2: If B is generated by the sets {1, 2, 3, 4}, {1, 2, 3, 5}, {1, 2, 3, 6},
{1, 2, 4, 5}, {1, 2, 4, 6}, {1, 2, 5, 6}, {1, 3, 4, 5} and {2, 3, 4, 6}, A ⊂ P(5),
A ⊎ B ⊂ A and c = (8, 8, 7, 7, 7, 7), then K(A) ⩾ 0.

Proof of claim. As in Claim 1, the values of ci were chosen by looking
at P([6] \ {i}) ⊎ B for 1 ⩽ i ⩽ 6, letting c3 = . . . = c6 and minimising
c1 + c2. Our approach follows the same lines as the proof of claim 1.
Note ﬁrst that if n1 = 5, either {1, 3, 4, 5, 6} ∈ A or {2, 3, 4, 5, 6} ∈ A,
so n5 ⩾ 5 and as before A still contains at least n2 − 2 of the 4-sets
and n1 of the 5-sets of B.
Consider ﬁrst the case ∅ /∈ A. We have N6 + N0 = 44, N5 + N1 ⩾ 0,
N4 + N2 ⩾ −36 (since 2-sets contribute at least −16, and six of the
4-sets in B contribute 16, the other two contributing 14), and N3 ⩾ −4,
so K(A) ⩾ 0.
So we may assume that ∅ ∈ A, so n4 ⩾ 8 and n5 ⩾ 4 by Obser-
vation 5. If n5 = 4, then {5}, {6} /∈ A and n2 ⩽ 8, since the only
2-sets containing 5 or 6 which can be in A are {1, 5} and {2, 6}. Hence
N5 + N1 ⩾ 4 and N4 + N2 ⩾ (16 ×6) + (14 ×2) −16 −(14 ×6) −12 = 12.
We still have N3 ⩾ −4, so K(A) ⩾ 0.

12 ROBERT MORRIS

Suppose next that n5 = 5, and {1, 3, 4, 5, 6} ∈ A, say. If n1 ⩽ 3 then
N5 + N3 + N1 ⩾ 54 and we are done. If n1 = 4 then N5 + N3 + N1 ⩾
26, so n2 = 10 and n4 = 8, which is impossible. Hence n1 = 5,
and {5} /∈ A, so the only possibilities for A are P([6] − 5) ⊎ B and
P([6] − 5) ⊎ B ⊎ {1, 5} (since {2, 3, 4, 5, 6} /∈ A, and we may assume
no extra sets with non-negative contribution to K(A) are added). But
these both give K(A) ⩾ 0, so we are done with this case also.
So we may assume that n5 = 6. Now if n1 ⩽ 4 then N5 + N3 + N1 ⩾
52, and so we are done. But if n1 = 5 then N5 + N3 + N1 ⩾ 24 and
n4 ⩾ 10, since no 5-set in [6] contains more than three 4-sets of B, so
N4 + N2 ⩾ −12, and the claim follows. □

For the lower bound consider the set system S = {{1, 2, i, j} :
{i, j} ⊂ {3, 4, 5, 6}} and let B be generated by S. We apply the usual
method. Let x = c1 + c2 and y = c3 + c4 + c5 + c6, and add the
inequalities to get
 38x + 46y ⩾ 43
92x + 67y ⩾ 78

which imply that x ⩽ 1
4 and x ⩾ 11
25 respectively. But 1
4 < 11
25, so we

have a contradiction. This implies that F C(4, 6) ⩾ 7. □

We shall also use the following two simple results in Section 5.

Lemma 6. F C(3, 7) ⩽ 6.

Proof. Consider any six 3-sets in {1, 2, 3, 4, 5, 6, 7}. Some element is
contained in at most two of them, so we have at least four 3-sets com-
posed solely of the other six elements. The result now follows by The-
orem 2. □

Lemma 7. F C(4, 7) ⩽ 18.

Proof. Suppose we have eighteen 4-sets in {1, 2, 3, 4, 5, 6, 7}. Then some
element must be contained in no more than ten of them, so we have
at least eight 4-sets contained in a 6-set, and the result follows by
Theorem 2. □

5. The case n = 9 of the conjecture

We now provide an application of the above results by proving the
Union-Closed Sets Conjecture in the case that the size of the largest
set is at most nine. This improves the previous known bound by one.
The idea of the proof is to show that if the family contains none of the

FC-FAMILIES AND FRANKL’S CONJECTURE 13

above F C-families, then either the average size of a set is at least 1
2 , or
the family contains very few sets. We shall need the following results
for the proof. The ﬁrst two were proved by Gao and Yu [3], the third
by Poonen [4].

Theorem C. If m ⩽ 32 then the UC-Sets Conjecture holds for A.

Theorem D. If n ⩽ 8 then the UC-Sets Conjecture holds for A.

Lemma E. We may assume that A contains at least two (n − 1)-sets.

Lemma 8. One 3-set and thirteen 4-sets in [9] generate either at least
two 7-sets, at least three 6-sets, or an F C-family.

Proof. Suppose only at most one 7-set and two 6-sets are generated.
Partition the 4-sets according to the size of their intersection with the
3-set. If we have more than six 4-sets with intersection 2, then we get
at least four distinct 2-sets by removing the elements of our 3-set from
them (by Theorem 1 (5)), which generate either at least two 4-sets or
three 3-sets, a contradiction. But we can have at most three 4-sets
with intersection 3, at most two with intersection 1 and at most one
with intersection 0. □

Lemma 9. Five 3-sets in [9] generate either an F C-family or a 7-set.

Proof. Assume not and choose three of the 3-sets in such a way as
to maximise the size of their union. Let this maximum be t. By
Theorem 1, t ⩾ 6.

Case 1: t = 9. The addition of any other 3-set forms a 7-set so we are
done.

Case 2: t = 8. Suppose without loss that the 3-sets are {1, 2, 3},
{4, 5, 6} and {6, 7, 8}. Then by Theorem 2 we must add a 3-set which
intersects {1, 2, 3}, and the only (type of) 3-set which does so and
whose addition does not create a 7-set is {1, 4, 5}. Now, consider the
possible intersections of the ﬁfth 3-set with {1, 2, 3, 4, 5}. By Theorem 1
it cannot have order 3; by Theorem 2 if it has order 2 then we have a
7-set; if it has order 1 we clearly have a 7-set, so the ﬁfth 3-set must
be contained in {6, 7, 8, 9}. But then it must contain 9, so we have the
7-set {1, 4, 5, 6, 7, 8, 9}.

Case 3: t = 6. Each of the other 3-sets can contain at most one of
these six elements (if two we’d be able to form a 7-set, if three we’d
have an F C-family by Theorem 2), so by maximality no two of the
chosen 3-sets intersect in two elements. Hence wlog the chosen 3-sets

14 ROBERT MORRIS

are {1, 2, 3}, {1, 4, 5} and {2, 4, 6}. At least one of the remaining sets
must be of the form {i, 7, 8} say, with i ∈ {1, 2, 3, 4, 5, 6}, but then we
have a 7-set. □

Proof of Theorem 3. Suppose A is a union-closed family in P(9) for
which the conjecture fails, and observe that by Theorem D we may
assume that [9] ∈ A. Also note that we may assume that n1 = n2 = 0,
since every 1- and 2-set forms an F C-family. We are trying to show
K(A) ⩾ 0 for c = 1, so an r-set contributes 2r − 9 to K(A). We shall
consider the contribution of the (non-empty) sets in the 7-sets of [9].

Notice that there are (9
7

) = 36 of them, and that the contribution of

[9], ∅ and the 8-sets of A is at least +14.
Consider a single 7-set of [9], not necessarily in A. If the 7-set itself is

in A then it contributes +5 to K(A), but each r-subset lies in (
9 − r
7 − r
)

diﬀerent 7-sets, so we must divide its contribution by this number.
Summing over all 7-sets will then give us the total contribution of the
3-, 4-, 5-, 6- and 7-sets to K(A). Hence 6-sets contribute +1, 5-sets

+ 1
6, 4-sets − 1
10 and 3-sets −1
5 .
We need a lower bound on the contribution of a given 7-set’s non-
empty subsets. Let ri denote the number of i-sets in this 7-set, and
divide into cases as follows:

Case 1: The 7-set is in A. Then the contribution is at least 5− r4
10 − r3
5 ⩾

5 − 17
10 − 5
5 = 23
10 , by Lemmas 6 and 7.

Case 2: The largest subset in A has six elements. Then the contribu-
tion of the subsets is at least 0, since r4 ⩽ 7 and r3 ⩽ 3 by Theorem 2,
so we may assume that either r3 = 2 and r4 = 7, or r3 = 3. But then
r5 ⩾ 1, so we may assume that r3 = 3 and r4 ⩾ 6. But now r5 ⩾ 2 and
we are done.

Case 3: The largest subset in A has ﬁve elements. Then it follows from
Theorem 1 that the worst case is r3 = 2, r4 = 3, which gives a total

contribution of −16
30 .

Case 4: The largest subset in A has fewer than ﬁve elements. Then

r3 ⩽ 2 and r4 ⩽ 1, so the contribution is at least −1
2 .
Claim: If A contains a 7-set then K(A) ⩾ 0.

FC-FAMILIES AND FRANKL’S CONJECTURE 15

Proof of claim. First note that if n8 ⩾ 3 then we are done, since then

K(A) ⩾ 21 − (36 × −16
30 ) > 0, so assume that n8 = 2. Suppose

that n7 ⩾ 2. Then K(A) ⩾ 14 + 4.6 − (34 × −16
30 ) > 0, so assume

that n7 = 1 and observe that if K(A) < 0 then at least 31 of the

7-sets contain no 6- or 7-set, since 14 + 2.3 − (30 × −16
30 ) > 0. Hence

n3 ⩽ (31 × 2) + (4 × 3) + 5
15 < 6 since each 3-set appears in 15 diﬀerent

7-sets, and n4 ⩽ (31 × 4) + (4 × 7) + 17
10 < 17, since each 4-set appears

in 10 diﬀerent 7-sets. It follows that the total contribution to K(A)
of all except the 5- and 6-sets is at least 14 + 5 − 16 − 15 = −12, so
assume that the 5- and 6-sets contribute at most +11. Note also that∑

i̸=5,6 ni ⩽ 26.

Now, from above if n3 = 0 then K(A) > 0, so by Lemma 8, either
n6 ⩾ 3, or n4 ⩽ 12. In the former case we get n5 + n6 ⩽ 5, so m ⩽ 31
and we are done by Theorem C. In the latter case the 5- and 6-sets can
contribute at most +7 and ∑

i̸=5,6 ni ⩽ 22, which gives m ⩽ 29 and we

are again done. □

So we may assume that n7 = 0, and by Lemma 9 we have n3 ⩽ 4.
Now, let p = |{7-sets with r4 ⩽ 3}| and q = |{7-sets with r4 = 4}|.

Then Theorem 1 and the observations above imply that 16
30 p+ 13
30 q > 14

if K(A) < 0. But then 10n4 ⩽ 3p+4q+7(36−p−q) = 252−(4p+3q) ⩽
252 − 105 + q
4 ⩽ 156, so n4 ⩽ 15.

Hence the total contribution to K(A) of all except the 5- and 6-sets
is at least 14 − 15 − 12 = −13, so we may assume that the 5- and 6-sets
contribute at most +12, and we have ∑

i̸=5,6 ni ⩽ 23. The result now

follows exactly as before, using Lemma 8 and Theorem C: n3 ⩾ 1 so
either n6 ⩾ 3, in which case n5 + n6 ⩽ 6 and m ⩽ 29; or n4 ⩽ 12, in
which case n5 + n6 ⩽ 9, and m ⩽ 29. □

Although our method does not seem to easily extend to larger val-
ues of n (at least, not without ﬁrst improving our upper bounds on
F C(k, n)), it does give a short proof of Theorem D.

Alternative proof of Theorem D. Suppose A is a counter-example and
let b = maxA∈A|A|. Since n1 = n2 = 0, we may assume that b ⩾ 7.

16 ROBERT MORRIS

Case 1: b = 7. By Lemma 6 we have n3 ⩽ 5, and by Lemma E

n6 ⩾ 2, so the average set size is at least 34
9 > 7
2 and we are done.
Case 2: b = 8. Apply the method of the proof of Theorem 3. There

are (
8
6
) = 28 6-sets, each contributing at least −1
5 to K(A) (two 3-

sets in a 4-set). But now K(A) ⩾ (2 × 3) − 28
5 > 0, so again we are
done. □

We also get the following improvement without doing any extra work.

Theorem 10. The Union-Closed Sets Conjecture holds in the case
m ⩽ 36.

Proof. Follow the exact method of [3] and [4], replacing the bound
n ⩾ 9 with n ⩾ 10. □

Problem 1. Can we improve Theorem 5 further? A useful step would
be (using the notation of [3]) to get good lower bounds on Sr in terms
of S1, given a condition limiting the average size of the sets in A.

Problem 2. Can we generalise or improve Lemmas 8 and 9? In par-
ticular, how many k-sets in [n] do we need to guarantee either an F C-
family or an r-set?

6. General bounds on F C(k, n)

We have found some values of F C(k, n) for small k and n, but if
we hope to use our method to solve the conjecture we shall need good
asymptotic bounds. Good upper bounds seem hard to prove, but by
Proposition 1.4 of [3] the function is at least deﬁned for any k for
suﬃciently large n. We give the following short proof of the result.

Theorem 11. For any k ⩾ 1 and n ⩾ 2k − 2, the family B generated

by all the k-sets in [n] is an F C-family, and hence F C(k, n) ⩽ (
n
k
)
.

Proof. The result follows by Poonen’s Theorem, and the following claim.

Claim: If A ⊂ P(n) and A ⊎ B ⊆ A, then nn−r ⩾ nr for all r ⩽ ⌊n
2
 ⌋
.

Proof of claim. Note that B ⊃ {B ∈ P(n) : |B| ⩾ k}. So if an r-set A
is in A, then all those (n − r)-sets in P(n) that contain A are also in

A. Hence each r-set in A generates ( n − r
n − 2r
) (n − r)-sets. Conversely

FC-FAMILIES AND FRANKL’S CONJECTURE 17

each (n − r)-set in A is generated by at most (
n − r
r
 ) = ( n − r
n − 2r
)

r-sets, so we are done. □

Now let c = 1, so K(A) ⩾ 0 for families satisfying the conditions of
the claim. The result follows by Poonen’s Theorem. □

Remark 2. This result is almost certainly not best possible, but as
yet we have been unable to improve it. The usual lower bound method

gives that B is not F C if (n−2)(
n − 2
k − 2
) < 2
 k−3∑

i=0
 (n − 2
i
 ), which holds

if and only if k ⩾ n
2 + ( 1
2√2 + o(1)) √n log n.

We have the following bounds on F C(k, n) (the ﬁrst upper bound,

F C(3, n) ⩽ 2n
3 , is due to Vaughan [9]). The proofs of the lower bounds
are not diﬃcult but lengthy, so we omit them, giving only the main
ideas.

Theorem 12.

(a) ⌊ n
2
 ⌋ + 1 ⩽ F C(3, n) ⩽ 2n
3 ,

(b) ( 6
25 + o(1)) n
2 ⩽ F C(4, n) ⩽ 7
360n
4,

(c) ckn
k−2 ⩽ F C(k, n) ⩽ ex(n, K (k)
2k−2) ⩽ (
n
k
) with ck > 0 con-

stant.

Sketch of proof. The upper bounds are easily obtained by showing that
any family in P(n) with the given number of k-sets contains one of the
families we (or Vaughan) have already shown to be F C. For the lower
bounds, ﬁrst let

B(n, k, r) = {B ∈ P(n) : |B| = k and for some 0 ⩽ i ⩽ r − 1, either {4i + 1,

4i + 2, 4i + 3} or {4i + 1, 4i + 2, 4i + 4} is the initial segment of B}.

The bounds are obtained by applying the method of the proofs of
Theorems 1 and 2, using the families P([n] \ {i}) for 1 ⩽ i ⩽ n, to
(1) B = B(n, 3, r), if n = 4r or 4r + 1, or
B = B(n, 3, r) ∪ {4r − 1, 4r + 1, 4r + 2} if n = 4r + 2 or 4r + 3.

(2) B = B(n, 4, r), where r = ⌊(1
5 − ε) n
⌋ for some ε > 0.

(3) B = B(n, k, c′
kn) for some suﬃciently small c′
k > 0. □

18 ROBERT MORRIS

7. Questions and Conjectures

Several avenues for further research spring readily to mind. For
example, given our experience so far we might hope to show that in
Poonen’s Theorem it is suﬃcient to consider only the families P([n] \
{i}) for 1 ⩽ i ⩽ n. Unfortunately it is not true that these families give
exactly the permissible values of c, as the following example shows.

Counter-example 1. Let B = {{1, 2, 3}, {1, 2, 4}, {3, 4, 5}}, and let
c = (9, 7, 12, 12, 8). Then K(A) ⩾ 0 for A = P([5] \ {i}) ⊎ B for each
i, but K(A) < 0 for P({2, 3, 4, 5}) ⊎ {1, 2} ⊎ B.

However, it is still possible that the following question has an aﬃr-
mative answer.

Question 1. Do the inequalities K(A) ⩾ 0 given by the families P([n]\
{i}) for 1 ⩽ i ⩽ n permit some solution c only when one is possible for
all A ⊂ P(n) such that A ⊎ B ⊆ A?

In any case we are still inclined to believe the following conjectures,
the ﬁrst of which was suggested (though not speciﬁcally conjectured)
in [9].

Conjecture 1. F C(3, n) = ⌊ n
2
 ⌋ + 1 for all n ⩾ 4.

Conjecture 2. F C(k, n) = Θ(n
k−2) for all k ⩾ 2.

A ﬁnal conjecture is suggested simply on the basis that it seems
plausible, and is true for the F C-families we have discovered so far.

Conjecture 3. Suppose a union-closed family B has minimal gener-
ating family S, and let B′ be generated by (S \ {B}) ∪ {B ∪ {i}} for
some set B ∈ S. If B is not F C, then B′ is not F C either.

References

[1] D. Duﬀus, page 525 of Graphs and Order, I. Rival (Ed.), Reidel, Dor-
drecht/Boston 1985.
[2] P. Frankl in Extremal Set Systems, Chapter 24 of the Handbook of Combina-
torics, MIT Press & North-Holland, 1995.
[3] W. Gao and H. Yu, Note on the union-closed sets conjecture, Ars Comb., 49
(1998), 280–288.
[4] B. Poonen, Union Closed Families, J. Combin. Theory Ser. A, 59 (1992), 253–
268.
[5] D. Reimer, An average set size theorem, Combin. Probab. Comput., 12 (2003),
89–93.
[6] D.G. Sarvate and J.-C. Renaud, Improved bounds for the union-closed sets
conjecture, Ars Comb., 29 (1990), 181–185.

FC-FAMILIES AND FRANKL’S CONJECTURE 19

[7] T.P. Vaughan, Families implying the Frankl conjecture, Europ. J. Combina-
torics, 23 (2002), 851–860
[8] T.P. Vaughan, A Note on the Union Closed Sets Conjecture, J. Comb. Maths.
and Comb. Comp., 45 (2003), 95–108.
[9] T.P. Vaughan, Three-sets in union closed families, J. Comb. Maths. and Comb.
Comp., to appear.

Department of Mathematical Sciences, The University of Memphis,
Memphis, TN 38152
E-mail address: rdmorrs1@memphis.edu
