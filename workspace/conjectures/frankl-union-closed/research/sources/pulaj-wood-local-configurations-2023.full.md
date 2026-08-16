<!-- source: https://arxiv.org/pdf/2301.01331 | converted from PDF -->

arXiv:2301.01331v2  [math.CO]  14 Oct 2024
Local Conﬁgurations in Union-Closed Families

Jonad Pulaj and Kenan Wood∗

Abstract

The Frankl or Union-Closed Sets conjecture states that for any ﬁnite union-
closed family of sets F containing some nonempty set, there is some element i
in the ground set U (F) := ⋃S∈F S of F such that i is in at least half of the
sets in F. In this work, we ﬁnd new values and bounds for the least integer
F C(k, n) such that any union-closed family containing F C(k, n) distinct k-sets
of an n-set X satisﬁes Frankl’s conjecture with an element of X. Additionally,
we answer an older question of Vaughan regarding symmetry in union-closed
families and we give a proof of a recent question posed by Ellis, Ivan and Leader.
Finally, we introduce novel local conﬁguration criteria through a generalization
of Poonen’s Theorem to prove the conjecture for many, previously unknown
classes of families.

1 Introduction

Frankl’s or the Union-Closed Sets conjecture is an open, well-known problem in ex-
tremal set theory. A ﬁnite family of ﬁnite sets F is union-closed if for every A, B ∈ F ,
it follows that A ∪ B ∈ F . Frankl’s conjecture states that for any union-closed family
F containing some nonempty set, there is some element i in the ground set, or uni-
verse, of F deﬁned as U(F ) := ⋃
S∈F S such that i is in at least half of the sets in
F . Of the well-known techniques to tackle Frankl’s conjecture, this work is concerned
with the approach of local conﬁgurations [2], a method that aims to prove the con-
jecture for any union-closed family F satisfying some local conditions with respect
to some ﬁxed ground set X ⊆ U(F ). We believe recent developments [11, 12], in-
cluding the work presented here, provide a new impetus into this line of research and
its implications for Frankl’s conjecture. In addition, some questions related to local
conﬁgurations may be of independent interest since they are not implied by Frankl’s
conjecture.

∗Department of Mathematics and Computer Science, Davidson College, Davidson, NC 28036,
{jopulaj, kewood}@davidson.edu
 1

The genesis of local conﬁgurations began with the well-known observations that
any union-closed family containing a 1-set or a 2-set satisﬁes Frankl’s conjecture with
an element from the 1-set or 2-set (where a k-set is a set with k elements). Poonen
[10] provided a complete characterization of families A such that every union-closed
family containing A satisﬁes Frankl’s conjecture with an element from U(A). Such
families A are called Frankl-Complete (FC). Families A that are not FC, are called
Non-FC. As a consequence he showed that there is a union-closed family F containing
a 3-set A such that every element of A is in strictly less than half the sets of F ;
that is, {A} is Non-FC. Using Poonen’s Theorem and machine-assisted techniques,
Morris [9] and Vaughan [13] were able to characterize many FC-families on at most six
elements. More recently, Pulaj [11] exhibited the ﬁrst eﬃcient algorithm to completely
characterize FC-families on at most 10-elements.
For a positive integer k, we deﬁne [k] = {1, . . . , k} and let P([k]) denote the
power set of [k]. For 3 ≤ k < n, deﬁne F C(k, n) to be the least integer m such
that any A ⊆ P([n]) containing m distinct k-sets is FC. Morris [9] proved that
F C(3, n) ≥ ⌊n/2⌋ + 1 for all n ≥ 4 and conjectured that equality holds. Pulaj
[12] then proved Morris’s conjecture showing F C(3, n) = ⌊n/2⌋ + 1 for all n ≥ 4.
Morris also proved that F C(4, 5) = 5 and 7 ≤ F C(4, 6) ≤ 8, while Mari´c, Vuˇckovi´c
and ˇZivkovi´c [8] provided a complete classiﬁcation of all FC-families on six elements,
showing F C(4, 6) = 7.
Our main contributions in this work are as follows. First, we algorithmically show:

• F C(4, 7) = 10, F C(4, 8) = 12, F C(5, 7) = 14, F C(6, 8) = 26;

• F C(4, 9) ≥ 14, F C(4, 10) ≥ 16, F C(5, 8) ≥ 21, F C(5, 9) ≥ 31, F C(5, 10) ≥
44, F C(6, 9) ≥ 42, F C(6, 10) ≥ 71, F C(7, 10) ≥ 85.

We also prove the following new upper bounds for general n, which follow from the
above exact characterizations of small F C(k, n) computations.

• F C(4, n) ≤ 1 + ⌈ 11
1680 · n(n − 1)(n − 2)(n − 3)⌉ for n > 8;

• F C(5, n) ≤ 1 + ⌈ 13
2520 · n(n − 1)(n − 2)(n − 3)(n − 4)⌉ for n > 7;

• F C(6, n) ≤ 1 + ⌈ 5
4032 · n(n − 1)(n − 2)(n − 3)(n − 4)(n − 5)⌉ for n > 8.

As a consequence, we obtain F C(4, 9) ≤ 21, F C(5, 8) ≤ 36, and F C(6, 9) ≤ 76. In
contrast to previous works [11, 12, 3] where exact integer programming is used for
veriﬁcation of computational results, in our current work we use a SMT (Satisﬁability
Modulo Theory) solver for veriﬁcation as suggested in [8]. Tools like SMTCoq [4] pave
the way for further veriﬁcation in interactive theorem provers.
Second, we answer a question of Vaughan [13] in the positive that simpliﬁes Poo-
nen’s characterization of FC-families according to the symmetry of a given family, in
particular, its automorphism group. For families A and B, deﬁne A ⊎ B := {A ∪ B :
A ∈ A, B ∈ B}. For an element i, let Ai := {A ∈ A : i ∈ A}. We explicitly state
Poonen’s Theorem below.
 2

Theorem 1.1 (Poonen). Let A be a union-closed family of sets with ∅ ∈ A and
U(A) = [n]. Then the following are equivalent:

1. A is an FC-family. That is, for all union-closed F ⊇ A, there is some i ∈ U(A)
such that |Fi| ≥ |F |/2.

2. There exists some c ∈ Rn
≥0 satisfying ∑
i∈[n] ci = 1 such that for any union-closed
B ⊆ P([n]) with A ⊎ B = B, we have
∑

i∈[n] ci|Bi| ≥ |B|/2.

The set of all c allowed in (2) is a polyhedron denoted P A. In 2002, Vaughan [13]
asked whether or not P A ̸= ∅ implies there is some c ∈ P A such that ci = cj whenever
there is an automorphism of A mapping i to j. We prove that this implication does,
indeed, hold.
Third, we highlight the utility of FC-families by answering in the positive the
following recently posed question by Ellis, Ivan and Leader [5]. Let n ≥ 4 and choose
some R ⊂ Zn with |R| = 3. Does the union-closed family generated by all translates
of R × {0} or {0} × R by elements of Zn × Zn necessarily satisfy Frankl’s conjecture?
Finally, we prove a useful generalization of Poonen’s Theorem that constructs
a new type of local conﬁguration. Given a Non-FC family A, our theorem gives a
method of restricting the possible union-closed families F ⊇ A such that |Fi| < |F |/2
for all i ∈ U(A) by considering only the structure of A. To our knowledge, this is
the ﬁrst result that allows us to prove that a large collection of union-closed families
that contain a Non-FC family satisfy Frankl’s conjecture. We are able to obtain very
strong results about union-closed families containing a small Non-FC family such as
{∅, {1, 2, 3}} or {∅, {1, 2, 3, 4}}. We obtain similar results on families of 4-sets, 5-
sets, 6-sets, and 7-sets using an adaptation of Pulaj’s algorithm together with the
algorithm used for the above computations on F C(k, n).
The rest of this paper is organized as follows. In Section 2, we give many new val-
ues and bounds for F C(k, n), along with an interesting structural conjecture. Section
3 settles an older question of Vaughan, and Section 4 settles a more recent question
of Ellis, Ivan and Leader. Section 5 proves a generalization of Poonen’s Theorem
and introduces a new kind of local conﬁguration, which we use to prove Frankl’s
conjecture for many new previously unknown classes of families. Finally, concluding
remarks may be found in Section 6.

2 FC-values and FC-bounds

In this section, we give many new values and bounds implying Frankl-Completeness
and conjecture a striking structural pattern regarding maximal Non-FC families.

3

Deﬁnition 2.1. Two families of sets A and B are isomorphic, written A ∼= B,
provided there is some bijection φ : U(A) → U(B) such that B = {φ(S) : S ∈ A}.
The map φ is called an isomorphism.

We now introduce our main tool for determining exact values of F C(k, n), Al-
gorithm 1. The method getNonIsomorphicFamilies(n, k, m) returns a set of rep-
resentatives from each isomorphism class of families A of m distinct k-sets with
U(A) = [n]. The method isFC(F ) uses Pulaj’s algorithm [11] to return true if F is
FC, and false otherwise.

Algorithm 1: getNFC(n, k, m)
Input: Positive integers n, k, m where n ≥ k ≥ 3
Output: A set of all pair-wise nonisomorphic Non-FC families of m distinct
k-sets with universe [n]

1 if km < n or m > (n
k) then

2 return ∅

3

4 NFC ← ∅

5 FC ← ∅

6

7 if k(m − 1) < n then

8 for F ∈ getNonIsomorphicFamilies(n, k, m) do

9 if not isFC(F ) then

10 NFC ← NFC ∪ {F }

11 return NFC

12

13 J ← {i ∈ Z | max{k, n − k} ≤ i ≤ n}

14 for F ∈ ⋃
i∈J getNFC(i, k, m − 1) do

15 for S ⊆ [n] such that |S| = k and U(F ∪ {S}) = [n] do

16 if ∀A ∈ NFC ∪ FC : F ∪ {S} ̸∼= A then

17 if F ∪ {S} contains a proper FC-family then

18 continue

19 if isFC(F ∪ {S}) then

20 FC ← FC ∪ {F ∪ {S}}

21 else

22 NFC ← NFC ∪ {F ∪ {S}}

23 return NFC

Algorithm 1 is a recursive algorithm designed to determine all isomorphism classes

4

of Non-FC families of m distinct k-sets with universe [n], while disregarding families
containing a proper FC-family. The isomorphism checks in line 16 are performed by
computing a canonical form
1 of the family F such that any family isomorphic to F
has an identical canonical form, checking if that canonical form has been computed
before, and if not, storing its canonical form. The proper FC-containment check in
line 17 is computed in a similar fashion by computing the canonical form of subfamilies
of F with one fewer member-set. In our implementation, we manually start at the
bottom of the call stack to avoid recomputation.
Additionally, for the purpose of ensuring the correctness of each isFC() com-
putation, we use the SMT solver Z3 [1] within the SMT python library, pySMT [6].
For verifying Non-FC families, we check the infeasibility of the terminating set of
constraints produced by the isFC() algorithm. For FC families, (using Pulaj’s no-
tation) we check the infeasibility of the linear integer system deﬁning X(A, c), where
c is the vector in Z
n found by the algorithm that is proposed to satisfy X(A, c) = ∅.

Lemma 2.1. Algorithm 1 correctly ﬁnds a desired collection of Non-FC families.

Proof. For termination, notice that in each recursive call, we must have n ≥ k >
0. Also, the m argument is decreased by 1 at every call, so if Algorithm 1 did
not terminate, km ≥ n at every iteration; however, m must be zero at some point
assuming no termination. This is a contradiction because n > 0. Therefore Algorithm
1 terminates.
For correctness, observe that the theorem is true if either km < n or k(m − 1) < n
or m > (
n
k). We ﬁrst prove the following claim.

Claim: Let J = {i ∈ Z | max{k, n − k} ≤ i ≤ n}. Assume getNFC(i, k, m − 1) is
correct for all i ∈ J. Then getNFC(n, k, m) is correct.

Proof of claim. We may assume k(m − 1) ≥ n and m ≤ (
n
k). Consider the execu-
tion of getNFC(n, k, m). Observe that anytime a family is added to NFC, we always
ﬁrst verify that it is Non-FC. Hence every family in NFC is Non-FC. Suppose F
is a Non-FC family with universe [n] containing m distinct k-sets. Let S ∈ F ; let
F ′ = F − {S} with i := |U(F )|. Since S ∈ F , we know |S| = k, so that n − k ≤ i and
k ≤ i ≤ n (because m ≥ 2). Hence i ∈ J, which implies that getNFC(n, k, m) iterates
through all families in getNFC(i, k, m − 1). By assumption, one of these families, say
G′, is isomorphic to F ′. Since there is an isomorphism φ : U(F ′) → U(G′), the family
G := G′ ∪ {φ(S ∩ U(F ′)) ∪ (S − U(F ′))} is isomorphic to F . Also G is added to NFC
since F ∼= G is Non-FC, as desired. Thus getNFC(n, k, m) is correct.

We proceed by induction on n. Note that n ≥ k, so the base case is n = k. If
m = 1, the the result follows by inspecting lines 7-11 in Algorithm 1. If m ≥ 2, then
m > (
n
k) = 1, so getNFC(n, k, m) correctly returns.

1We use SageMath’s canonical label() method within the IncidenceStructure class.

5

For the induction step on n, suppose n ≥ k + 1 and getNFC(n
′, k, m
′) is correct
for all k ≤ n
′ < n and m
′. Then getNFC(i, k, m − 1) correctly returns for all i ∈
J −{n}. To show getNFC(n, k, m) correctly returns, we use induction on m. If m = 1,
then certainly getNFC(n, k, m) is correct. Suppose m ≥ 2 and getNFC(n, k, m − 1)
correctly returns. This shows that getNFC(i, k, m − 1) is correct for all i ∈ J. Hence
the theorem follows from the above claim.

Using Algorithm 1, which can be easily extended to determine the exact value of
F C(k, n) for small values of k and n, we have determined the following.2

Theorem 2.2. F C(4, 7) = 10.

Theorem 2.3. F C(4, 8) = 12.

Theorem 2.4. F C(5, 7) = 14.

Theorem 2.5. F C(6, 8) = 26.

The system used to verify all of our results (including those in Section 5) has an
Intel Xeon Processor E5-2620 v4 with 16 cores, each running at 2.1GHz; the system
has 128GB of memory and two NUMA nodes. Theorems 2.2, 2.4, 2.5 have been
veriﬁed within at most a couple hours, but Theorem 2.3 took us more than 26 days
to verify.
Let (S
k) be the set of all k-subsets of a set S. Deﬁne a strict total order <, called
the lexicographic order, on the set ([n]
k ) by A < B if min(A∆B) ∈ A. In this order,
for ﬁxed n and k and for any S ∈ ([n]
k )
, deﬁne [S] := {A ∈ ([n]
k ) | A ≤ S}. Let
{Sn,k
i }i≥1 = ([n]
k ), where Sn,k
i < Sn,k
j for all 1 ≤ i < j. If n and k are clear, we simply
write Si instead of Sn,k
i .
The following conjecture seems to be very promising based oﬀ of our experimental
results.

Conjecture 1. For ﬁxed n > k ≥ 3, if [Sm] is an FC-family for some positive integer
m and has universe size n, then F C(k, n) ≤ m.

This conjecture has been veriﬁed for all n > k ≥ 3 such that F C(k, n) is known
(it is trivial for k = 3 and any n ≥ 4); there is always a maximum Non-FC family of
the form [Sm] for some m. If the conjecture is true, then we could easily ﬁnd all exact
values of F C(k, n) for n ≤ 10; all we would need to do in that case is to ﬁnd an integer
m such that [Sm] is FC and [Sm−1] is Non-FC, giving us a result of F C(k, n) = m.
It can be shown using the above method that the following FC lower bounds are
also exact values, assuming Conjecture 1. Most of these have been veriﬁed to be tight
bounds within pySMT, except lower bounds of F C(k, 10).

2All code used in this paper can be accessed here: https://github.com/KenanWood/Local-
Conﬁgurations-in-Union-Closed-Families
 6

k\n 4 5 6 7 8 9 10
3 3 3 4 4 5 5 6
4 5 7 10 12 14 16
5 14 21 31 44
6 26 42 71
7 85

Table 1: FC-values

Theorem 2.6. F C(4, 9) ≥ 14, F C(4, 10) ≥ 16, F C(5, 8) ≥ 21, F C(5, 9) ≥ 31,
F C(5, 10) ≥ 44, F C(6, 9) ≥ 42, F C(6, 10) ≥ 71, F C(7, 10) ≥ 85. The remaining
values of F C(k, n) for 5 ≤ k < n ≤ 10 are undeﬁned.

Proof. For each pair (k, n) ∈ {(4, 9), (4, 10), (5, 8), (5, 9), (5, 10), (6, 9), (6, 10), (7, 10)},
the family [Sn,k
m−1] as deﬁned above is Non-FC, where m is the proposed lower bound.
For the remaining pairs (k, n) when 5 ≤ k < n ≤ 10, we can easily show that the
family ([n]
k ) is Non-FC.

Assuming Conjecture 1 is true, Table 1 shows a complete classiﬁcation of FC-
values for (k, n) ∈ {3, . . . , 7} × {4, . . . , 10}, where no entry at (k, n) indicates that
F C(k, n) is undeﬁned.
To ﬁnd upper bounds of F C(k, n), we generalize and tighten a result of Morris
[9]. Morris showed that F C(4, n) ≤ 7
360 n
4, though without an explicit proof. The
following theorem improves and generalizes this bound, which yields improved explicit
upper bounds on F C(k, n) for 4 ≤ k ≤ 6.

Theorem 2.7. If m0 = F C(k, n0) ≤ (n0
k ), then

F C(k, n) ≤ 1 + ⌈ (m0 − 1)
n0 · · · (n0 − k + 1) · n · · · (n − k + 1)⌉ ≤ (
n
k
)

for all n > n0.

Proof. Suppose m0 = F C(k, n0) ≤ (n0
k ). Let n > n0 and m := 1+⌈
(m0 − 1) · (n0−k)!
n0! · n!
(n−k)! ⌉
,

noting that m = 1 + ⌈ (m0−1)
n0···(n0−k+1) · n · · · (n − k + 1)⌉
. Since n > n0, we know

(n0−k)!
n0! · n!
(n−k)! > 1. This implies

m ≤ ⌈
1 + ((n0
k
 ) − 1) · (n0 − k)!
n0! · n!
(n − k)!
 ⌉

= ⌈
1 + (n0
k
 ) · (n0 − k)!
n0! · n!
(n − k)! − (n0 − k)!
n0! · n!
(n − k)!
 ⌉

≤ ⌈ n0!
k!(n0 − k)! · (n0 − k)!
n0! · n!
(n − k)!
 ⌉

= (n
k
)
.
 7

Next, let A be a family of m distinct k-sets with a universe of size at most n. Deﬁne
A0 := A; for i ≥ 0, recursively deﬁne Ai+1 := Ai if |U(Ai)| < n − i, and otherwise,
Ai+1 := Ai − Ai
x, where x ∈ U(Ai) minimizes |Ai
x|. It follows that |U(Ai)| ≤ n − i
for all i ≥ 0 by induction. Since F C(k, n0) = m0, it suﬃces to prove |An−n0| ≥ m0.
To this end, for any i ≥ 0, the pigeonhole principle shows that there is some
x ∈ U(Ai) such that |Ai
x| ≤ k|Ai|
|U (Ai)| . If |U(Ai)| = n − i, then

|Ai+1| ≥ |Ai| − k|Ai|
|U(Ai)|

= |Ai| (
1 − k
n − i
)

= |Ai| (n − i − k
n − i
 ) .

Otherwise, |Ai+1| = |Ai| by construction, so that the inequality still holds since
n−i−k
n−i < 1. In writing
 |An−n0| = |A0| ·
 n−n0−1∏

i=0
 |Ai+1|
|Ai| ,

we obtain

|An−n0| ≥ m ·
 n−n0−1∏

i=0
 (n − i − k
n − i
 )

≥ (1 + (m0 − 1) · (n0 − k)!
n0! · n!
(n − k)!
 ) · ((n − k)!
n! · n0!
(n0 − k)!
 )

> m0 − 1,

so that |An−n0| ≥ m0. Thus A ⊇ An−n0 is an FC-family and the result follows.

Corollary 2.7.1. The following bounds hold:

• F C(4, n) ≤ 1 + ⌈ 11
1680 · n(n − 1)(n − 2)(n − 3)⌉ for n > 8;

• F C(5, n) ≤ 1 + ⌈ 13
2520 · n(n − 1)(n − 2)(n − 3)(n − 4)⌉ for n > 7;

• F C(6, n) ≤ 1 + ⌈ 5
4032 · n(n − 1)(n − 2)(n − 3)(n − 4)(n − 5)⌉ for n > 8.

Proof. This is an immediate consequence of Theorem 2.7 along with Theorems 2.3,
2.4, and 2.5.

Corollary 2.7.2. F C(4, 9) ≤ 21, F C(5, 8) ≤ 36, and F C(6, 9) ≤ 76.

Proof. This is an immediate consequence of Corollary 2.7.1.

8

3 Symmetry in FC-families

In this section, we answer two previously unsolved questions regarding symmetry in
union-closed families with respect to local conﬁgurations.
Given a union-closed family A containing ∅ with U(A) = [n], let B(A) be the set
of all union-closed B ⊆ P([n]) such that A ⊎ B = B. Recall that P A = {c ∈ Rn
≥0 :∑

i∈[n] ci = 1 ∧ ∀B ∈ B(A), ∑

i∈[n] ci|Bi| ≥ |B|/2}. Then By Poonen’s Theorem 1.1,
A is FC if and only if P A ̸= ∅. As outlined in our introduction, the following is a
generalization of Vaughan’s [13] question.

Question 1. Given a union-closed family A containing ∅, if P A is nonempty, then
is there always some c ∈ P A such that ci = cj whenever there is an automorphism of
A that maps i to j?

We prove that the answer is yes in the following theorem. First, let Aut(A) denote
the set of all automorphisms of A and note that Aut(A) is a group under function
composition.

Theorem 3.1. Let A be a union-closed family containing ∅. If P A is nonempty, then
there is some c ∈ P A such that ci = cj whenever there is an automorphism of A that
maps i to j.

Proof. Without loss of generality, assume U(A) = [n]. Suppose x ∈ P A. For any
φ ∈ Aut(A), we ﬁrst show that (xφ(i))i∈[n] ∈ P A; it suﬃces to show that for any B ∈
B(A), we have ∑

i∈[n] xφ(i)|Bi| ≥ |B|/2. Consider the image φ(B) = {φ(S) : S ∈ B}.
If A
′ ∈ A and B′ ∈ φ(B), then there are A ∈ A and B ∈ B such that A
′ = φ(A)
and B′ = φ(B); the ﬁrst holds since φ−1 ∈ Aut(A), so that A = φ−1(A
′) ∈ A, and
the second is by construction of φ(B); this shows A
′ ∪ B′ = φ(A ∪ B) ∈ φ(B), which
implies φ(B) ∈ B(A). Since x ∈ P A, then ∑

i∈[n] xi|φ(B)i| ≥ |φ(B)|/2. Since φ is a
bijection, ∑

i∈[n] xφ(i)|φ(B)φ(i)| ≥ |φ(B)|/2, which shows ∑

i∈[n] xφ(i)|Bi| ≥ |B|/2. Thus
(xφ(i))i∈[n] ∈ P A for any φ ∈ Aut(A).
Consider the convex combination of elements of P A,

c = 1
| Aut(A)| · ∑

φ∈Aut(A)(xφ(i))i∈[n]

= 1
| Aut(A)| ·
 

 ∑

φ∈Aut(A) xφ(i)




i∈[n]
 .

For each i ∈ [n], let si = ∑

φ∈Aut(A) xφ(i).

9

Then we obtain c = 1
| Aut(A)| · (si)i∈[n].

For any φ0 ∈ Aut(A), every automorphism in Aut(A) can be written as a unique
left composition with φ0; that is, Aut(A) = {φ ◦ φ0 : φ ∈ Aut(A)}. Then, for every
i, j ∈ [n] such that there is some automorphism φ0 ∈ Aut(A) mapping i to j, we
know si = ∑

φ∈Aut(A) x[φ◦φ0](i) = ∑

φ∈Aut(A) xφ(j) = sj,

so that ci = cj as well. Since c is a convex combination of points in a polyhedron,
c ∈ P A.

An important case of Theorem 3.1 is for transitive families, where a family A is
said to be transitive if for any two elements i, j ∈ U(A), there is an automorphism
of A mapping i to j. In particular, let A be a transitive union-closed family with
universe [n]. Then Theorem 3.1 implies that A is FC if and only if (1/n)i∈[n] ∈ P A.
We also remark a computational consequence of this theorem as follows. Note that
the dimension of P A is at most n − 1, and equality holds most of the time. However,
through Theorem 3.1, P A is nonempty if and only if the polyhedron obtained by
adding the constraints from Theorem 3.1 is also nonempty. But this constructed
polyhedron has dimension at most |[n]/ Aut(A)| − 1, where X/G denotes the set of
orbits of elements in X under the group action of G. It follows that for families of
sets A where the number of distinct automorphism orbits is small (highly symmetric
families), determining if some c ∈ P A exists becomes much more computationally
eﬃcient.

4 A Result on Transitive Families of 3-sets

In an Abelian group (G, +), if R ⊆ G and g ∈ G, we deﬁne the translation of R by g
in G as the set g + R := {g + r : r ∈ R}.

The set of all translations (by some element g ∈ G) of R in G is denoted T (R). Given
a family A, the union-closure of A, or the family generated by A, is deﬁned as the
union-closed family ⟨A⟩ := {⋃
S∈A′ S : A′ ⊆ A}; note that ⟨A⟩ contains ∅.
The authors of [5] pose the following open question related to small sets in union-
closed families.

Question 2. Given some 3-set R ⊂ Zn, does the union-closed family generated by
A = T (R × {0}) ∪ T ({0} × R) ⊆ Z
2
n necessarily satisfy Frankl’s conjecture?

The authors remark that this family is transitive; that is, for any x, y ∈ Z
2
n, there
is an automorphism φ ∈ Aut(A) such that φ(x) = y.

10

Let A be a family of sets. Let d(x) = |Ax| be the degree of x in A. The family
A is regular if d(x) = d(y) for all x, y ∈ U(A), in which case the degree of A is the
common degree.

Lemma 4.1. Let A be a regular family of 3-sets with degree k ≥ 2 and universe of
size n ≥ 4. Then A is FC.

Proof. Since ∑

i∈U (A) d(i) = ∑
A∈A |A|, we obtain kn = 3m, so that m = kn/3 ≥
2n/3, where m = |A|. This implies that m ≥ ⌈2n/3⌉ ≥ ⌊n/2⌋ + 1 = F C(3, n),
showing that A is FC.

Theorem 4.2. Let R ⊂ Zn be a 3-set, where n ≥ 4. Then the family A = T (R ×
{0}) ∪ T ({0} × R) ⊆ Z
2
n is FC, and thus, ⟨A⟩ satisﬁes Frankl’s conjecture.

Proof. It is clear that A is a regular family of 3-sets with degree at least two. Fur-
thermore, |U(A)| ≥ 4. The result follows from Lemma 4.1.

5 A Generalization of Poonen’s Theorem and FC-
families

In this section, we give a generalization of Poonen’s Theorem that allows us to prove
that a large class of union-closed families containing a potentially Non-FC family A
satisﬁes Frankl’s conjecture with an element from U(A). To our knowledge, this is
the ﬁrst result that allows us to obtain any signiﬁcant information about union-closed
families containing a Non-FC family.
For ﬁxed n, given a family F with [n] ⊆ U(F ) and a set T ⊆ U(F ) \ [n], let
F T,n = {S ∩ [n] : S ∈ F , S \ [n] = T }; if n is clear, we simply write F T . For utility,
observe that if F is union-closed containing A with U(A) = [n] and ∅ ∈ A, then for
any T ⊆ U(F ) \ [n], the family F T is union-closed and A ⊎ F T = F T . This shows
that condition 1 of Theorem 5.1 is not vacuously true. Note that when B consists of
all union-closed families B ⊆ P([n]) such that A ⊎ B = B, the statement of Theorem
5.1 reduces precisely to Poonen’s Theorem.

Theorem 5.1. Let A be a union-closed family containing ∅ with U(A) = [n]. Let B
be a set of union-closed subfamilies of P([n]) such that for all B ∈ B, it follows that
A ⊎ B = B. Assume A ∈ B. Then the following are equivalent:

1. For any union-closed F ⊇ A where for any T ⊆ U(F ) \ [n], it follows that F T is
empty or P([n]) or a family in B, there is some i ∈ [n] such that |Fi| ≥ |F |/2.

2. There is some c ∈ Rn
≥0 where ∑
i∈[n] ci = 1 and ∑

i∈[n] ci|Bi| ≥ |B|/2 for all
B ∈ B.

Proof. The proof follows that of Poonen’s Theorem exactly, except instead of using
all union-closed families B such that A ⊎ B = B, we only use the families B ∈ B.

11

Below we present a special case of Theorem 5.1 that is easier to work with than the
previous theorem. In particular, it allows for a simple extension of Pulaj’s algorithm
to determine if a family of sets A satisﬁes condition 1 below.

Theorem 5.2. Let A be a union-closed family containing ∅ with U(A) = [n]. Let
V ⊆ P([n]) with A ⊆ V. The following are equivalent:

1. For any union-closed family F ⊇ A where for each T ⊆ U(F ), it follows that
F T is equal to P([n]) or a subfamily of V, there is some i ∈ [n] such that
|Fi| ≥ |F |/2.

2. There is some c ∈ Rn
≥0 where ∑
i∈[n] ci = 1 and ∑

i∈[n] ci|Bi| ≥ |B|/2 for all
union-closed B ⊆ V such that A ⊎ B = B.

Proof. This is a consequence of Theorem 5.1, by choosing B to be the set of all
union-closed B ⊆ V such that A ⊎ B = B, noting that ∅ and A are families in B.

For brevity, any family A with U(A) = [n] together with a family V ⊆ P([n])
with A ⊆ V is said to be V-FC if ⟨A⟩ and V satisfy Theorem 5.2. That is, A is V-FC
if for any union-closed family F ⊇ A where for each T ⊆ U(F ), it follows that F T is
equal to P([n]) or a subfamily of V, there is some i ∈ [n] such that |Fi| ≥ |F |/2.
Since most interesting cases are when V is union-closed, our implementation as-
sumes that V is union-closed. This has the advantage of simply restricting the vari-
ables in the integer program IP (A, c) to only the ones indexed by sets in V instead of
all sets in P([n]), using Pulaj’s [11] notation IP (A, c). We cannot make this simple
restriction if V is not union-closed because the union-closure inequalities in IP (A, c)
require the variable indices to be closed under union. Alternatively, we could simply
add the constraints xS = 0 for all S ∈ P([n]) \ V. In either case, it is clear that mak-
ing either of the above restrictions on the integer program IP (A, c) yields a correct
algorithm for determining if A is V-FC. We implement this algorithm in Gurobi [7],
and verify the results using pySMT in an analogous way to the F C(k, n) results in
Section 2.
A natural candidate for a family V that will obtain strong results is V = {S ∈
P([n]) : |S| ̸= 1}. Through experimentation with Pulaj’s isFC() algorithm, which
iteratively ﬁnds the most restrictive inequalities in Poonen’s Theorem, we ﬁnd the
following. For most families A in which we are able to determine isFC(A) on our
system, the most restrictive inequalities in Poonen’s Theorem are the ones induced by
families of the form B = A⊎P([n]\{i}) for i ∈ [n]. In fact, Morris [9] conjectured that
these are the only inequalities needed. However, Pulaj [11] disproved his conjecture.
Still, it is reasonable to expect that removing these inequalities (by restricting V as
above) will yield many new strong results about Non-FC families. In the following
corollaries, we show that setting V = {S ∈ P([n]) : |S| ̸= 1} does indeed produce
striking new information about small Non-FC families.

Corollary 5.2.1. Let A = ⟨{{1, 2, 3}}⟩ and V = P([3]) \ {{1}}. Then A is V-FC.

12

Corollary 5.2.2. Let A = ⟨{{1, 2, 3, 4}}⟩ and V = {S ∈ P([4]) : |S| ̸= 1}. Then A
is V-FC.

Corollary 5.2.3. Let A = ⟨{{1, 2, 3, 4, 5}, {1, 2, 3, 4, 6}, {1, 2, 3, 5, 6}}⟩ and V = {S ∈
P([6]) : |S| ̸= 1}. Then A is V-FC. However, if A = ⟨{{1, 2, 3, 4, 5}, {1, 2, 3, 4, 6}}⟩
with the same V, then A is not V-FC.

Let F CV(k, n) be the minimal m such that any family A ⊆ P([n]) containing at
least m distinct k-sets and has U(A) = [n] is V-FC. When V = {S ∈ P([6]) : |S| ̸= 1},
Corollary 5.2.3 implies F CV(5, 6) = 3, which is a signiﬁcant improvement on FC-
families since F C(5, 6) is not even deﬁned. To determine F CV(k, n), we may simply
adapt Algorithm 1, or for our purposes since the cases are suﬃciently small, we simply
run a brute-force check of all desired non-isomorphic families. To this end, we obtain
the following.

Corollary 5.2.4. Let V = {S ∈ P([7]) : |S| ̸= 1}. Then F CV(5, 7) = 5 and
F CV(6, 7) = 7.

6 Conclusion

In this work, we answer two previously unsolved questions. One is an older question
of Vaughan that shows the dimension of Poonen’s polyhedron P A can be reduced
from |U(A)| to the number of orbits of Aut(A) through a projection, which shrinks
the search space and reduces computational work. We also answer a question of
Ellis, Ivan and Leader related to union-closed families generated by 3-sets. Our so-
lution highlights the continual importance of FC-families in that they provide simple
solutions to diﬃcult problems related to the Union-Closed Sets conjecture. Further-
more, we ﬁnd and verify many new values of F C(k, n) for k ≥ 4, of which only two
were previously known. These computations lead to three new general upper bounds
on F C(4, n), F C(5, n), F C(6, n). Additionally, an insightful pattern emerges in the
maximum Non-FC families through executions of Algorithm 1 (see Conjecture 1),
suggesting that Non-FC families have signiﬁcantly more structure than previously
thought. Finally, we introduce a new class of local conﬁgurations, a kind of “partial
Frankl-Completeness,” by generalizing Poonen’s theorem. We use an adaptation of
Pulaj’s algorithm to obtain strong new results in this direction.
We believe several directions merit further attention, including Conjecture 1 and
Theorem 5.1. In particular, what are the limits of Theorem 5.1 and V-FC families?
FC-families were very useful for proving that Frankl’s conjecture holds for all union-
closed families F with |U(F )| ≤ 12, so these newfound restrictions may be suﬃcient
to prove Frankl’s conjecture for larger ground sets U(F ), such as when |U(F )| equals
13 or 14. How far can the results about V-FC families be taken in relation to FC-
families? Aﬃrmative answers to these questions would be a signiﬁcant step towards
a deeper understanding of local conﬁgurations.

13

References

[1] Nikolaj Bjørner and Leonardo de Moura. Z3: An Eﬃcient SMT Solver. Tools and
Algorithms for the Construction and Analysis of Systems, 4963:337–340, 2008.

[2] Henning Bruhn and Oliver Schaudt. The Journey of the Union-Closed Sets
Conjecture. Graph. Comb., 31(6):2043–2074, Nov 2015.

[3] Leon Eiﬂer, Ambros Gleixner, and Jonad Pulaj. A Safe Computational Frame-
work for Integer Programming Applied to Chv´atal’s Conjecture. ACM Trans.
Math. Softw., 48(2), May 2022.

[4] Burak Ekici, Alain Mebsout, Cesare Tinelli, Chantal Keller, Guy Katz, Andrew
Reynolds, and Clark W. Barrett. SMTCoq: Plug-In for Integrating SMT Solvers
into Coq. In Rupak Majumdar and Viktor Kuncak, editors, Computer Aided Ver-
iﬁcation - 29th International Conference, CAV 2017, Heidelberg, Germany, July
24-28, 2017, Proceedings, Part II, volume 10427 of Lecture Notes in Computer
Science, pages 126–133. Springer, 2017.

[5] David Ellis, Maria-Romina Ivan, and Imre Leader. Small Sets in Union-Closed
Families. Electronic Journal of Combinatorics, 2023.

[6] Marco Gario, Andrea Micheli, and Bruno Kessler. PySMT: a Solver-Agnostic
Library for Fast Prototyping of SMT-Based Algorithms. 2015.

[7] Gurobi Optimization, LLC. Gurobi Optimizer Reference Manual, 2022.

[8] Mari´c, Vuˇckovi´c, and ˇZivkovi´c. Fully Automatic, Veriﬁed Classiﬁcation of all
Frankl-Complete (FC(6)) Set Families. arXiv preprint arXiv:1902.08765, 2019.

[9] Robert Morris. FC-families and improved bounds for Frankl’s conjecture. Euro-
pean Journal of Combinatorics, 27(2):269–282, 2006.

[10] Bjorn Poonen. Union-Closed Families. Journal of Combinatorial Theory, Series
A, 59(2):253–268, 1992.

[11] Jonad Pulaj. Cutting Planes for Families Implying Frankl’s Conjecture. Mathe-
matics of Computation, 89(322):829–857, 2019.

[12] Jonad Pulaj. Characterizing 3-Sets in Union-Closed Families. Experimental
Mathematics, pages 1–12, 2021.

[13] Theresa P. Vaughan. A Note on the Union-Closed Sets Conjecture. Journal of
Combinatorial Mathematics and Combinatorial Computing, 45:97–110, 2002.

14
