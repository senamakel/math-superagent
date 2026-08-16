<!-- source: http://ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf | converted from PDF -->

The 12-Element Case of Frankl’s Conjecture

Vuˇckovi´c, Bojan and ˇZivkovi´c, Miodrag

Abstract: According to Frankl’s conjecture, for each union-
closed family F of subsets of ﬁnite set X, there exists an element
contained in at least half members of F . We give a computer
assisted proof that Frankl’s conjecture is true if |X| ≤ 12.

Index Terms: extremal sets, union-closed family, Frankl’s
conjecture
 1. INTRODUCTION
D ENOTE by 2
A the family of all subsets of A, and
by [n] the set {1, . . . , n}. We say that a family F is
uniform if all the sets within F have an equal number of
elements. Denote by (A
k) the uniform family of all subsets
of A with k elements. Non-empty collection of sets F is
union-closed if for an arbitrary two sets A, B ∈ F is also
A ∪ B ∈ F . For an arbitrary family A ⊆ 2
[n] let A denote
the closure of A, the minimum union-closed family in 2
[n]

containing A. Let Fα = {S ∈ F | α ∈ S}. If F and G are
any two collections of sets, let F ⊎ G denote {S ∪ T | S ∈
F, T ∈ G}.
According to the longstanding Frankl’s conjecture (1979),
if F is a union-closed family, then there is an element in ∪ F
which is contained in at least half elements of F. Following
Markovi´c [1] we say that the union-closed family F is
Frankl’s if it satisﬁes Frankl’s conjecture. Let n = | ∪ F|.
Gao and Yu [11] proved that Frankl’s conjecture is satisﬁed
for any union-closed family with n ≤ 8, Morris [4] proved
it for 9 elements, Markovi´c [1] improved the bound to 10,
and by now the best obtained result in this manner is by
Boˇsnjak and Markovi´c [2], stating that family is Frankl’s if
n ≤ 11. More on the results related to Frankl’s conjecture
can be found in recent survey by Bruhn and Schaudt [3].
The main tools of our approach are the following deﬁni-
tion and lemma (see [1], [2]).

Deﬁnition 1. Let X = ∪ F. A function w that assigns
a real nonnegative values to elements of X, such that
there exists an element x ∈ X with w(x) > 0, is called
weight function. The weight of a set S ⊆ X is deﬁned by
w(S) = ∑
a∈S w(a). The number t(w) = 1
2 w(X) is the
target weight.

Lemma 1. A family F is Frankl’s if and only if there is a
weight function w : X → R, deﬁned on the set X = ∪ F,
such that ∑

S∈F w(S) ≥ t(w)|F|

Manuscript received September 8, 2016. Supported by the Serbian
Ministry of Education, Science and Technological Development, project
III44006 and by the grant no. 174021.
Bojan Vuˇckovi´c is with the Matematiˇcki institut SANU, Kneza Mihaila 36,
11001 Beograd, p.p. 367, Serbia (e-mail: vuckochess@gmail.com).
Miodrag ˇZivkovi´c is with the Matematiˇcki fakultet, Studentski trg 16, 11000
Beograd, Serbia (e-mail: ezivkovm@matf.bg.ac.rs).
 It is usually possible to restrict a function w by assigning
rational or even integer values to all the elements of family,
like we do in this paper. In order to simplify implementation
of the previous Lemma, it is convenient to introduce shares
of elements, sets and families.

Deﬁnition 2. Let F be a union-closed family of sets, and
let w be a weight function on F. The share s(L) of the
set L ⊆ ∪ F is the difference s(L) = w(L) − t(w). The
share of an arbitrary family A ⊆ F is deﬁned by s(A) =∑
A∈A s(A).

By reformulating Lemma 1, we obtain

Corrolary 1. An arbitrary union-closed family F is Frankl’s
if and only if there exists a weight function w, such that
s(F) ≥ 0.

Proof. The proof follows from the equality

s(F) = ∑

S∈F s(S) = ∑

S∈F(w(S) − t(w))

= ∑

S∈F w(S) − t(w)|F|

Denote by Sn the set of all permutation on [n], and for ϕ ∈
Sn set ϕ(A) as {ϕ(x) | x ∈ A}. The families A, B ⊆ 2
[n]

are equivalent, denoted by A ∼ B, if there exists ϕ ∈ Sn,
such that B = {ϕ(A) | A ∈ A}.

Example 1.

A = {{4, 5, 6}, {2, 4, 6}, {3, 4, 5, 6}},

B = {{1, 2, 3}, {1, 2, 4}, {1, 2, 3, 5}}

For ϕ : {2, 3, 4, 5, 6} → [5] given by

ϕ : ( 2 3 4 5 6
4 5 1 3 2
 ) ,

B is equal to {ϕ(A) | A ∈ A}, and hence A ∼ B.

2. FC FAMILIES

Vaughan [6] introduced the concept of Frankl-complete
families, or FC families.

Deﬁnition 3. Family G is an FC family if for any union-
closed family Fcontaining subfamily G′ ∼ G, there exists
an element x ∈ ∪ G′ appearing in at least half of the sets
of F.

Poonen [5] showed which conditions family G needs to
satisfy to be an F C-family.

The ﬁrst two claims of the following theorem are proved
in [9], the third and fourth in [4], and the last one is from [7].

Theorem 1. The following families are FC:
1) singleton {1}
2) dublet {1, 2}
3) an arbitrary three-subset subfamily of ([5]
3 )

4) an arbitrary four-subset subfamily of (
[6]
3 )

5) an arbitrary four-subset subfamily of (
[7]
3 )

Following Boˇsnjak and Markovi´c [1], [2], for K ∩ S = ∅,
let CK,S = K ⊎ 2
S denote the hypercube with the base K
and the upper set S. We use the following consequence of
Corrolary 1.

Corrolary 2. Let F be a union-closed family, and let S ⊆∪ F, K = ∪ F \S. If there exists a weight function w, such
that ∑
L⊆K s(CL,S ∩ F) ≥ 0, then F is Frankl’s.

Deﬁnition 4. The family G is k-FC family if an arbitrary
union-closed family F ⊆ 2
[k] containing G′ ∼ G as a
subfamily is Frankl’s.

3. RESULTS FOR |X| = 12

Denote by Q(F) and R(F, i) the following statements:

Q(F) : F does not contain a family equivalent
to some FC family from Theorem 1, (1)

R(F, i) : F does not contain a family equivalent
to some Fj, j < i, from Table I. (2)

Deﬁnition 5. Let i ∈ {1, . . . , 33}. We say that F is Fi-
correct family if it satisﬁes the following conditions:
1) F is a union-closed,
2) ∪ F = [12],
3) Fi ⊆ F,
4) Q(F),
5) R(F, i).

Denote by Si = ∪ Fi and ri = |Si|. We may assume
that Si = [ri]. The set of hypercubes CK,Si = K ⊎ 2Si,
K ⊆ [12] \ Si, partitions the family 2
[12]. Let CK,Si be an
arbitrary hypercube, corresponding to the base K ⊆ [12]\Si.
We say that family G is (Fi, k)-correct if G = CK,Si ∩ F,
where k = |K| and F is Fi-correct. It is obvious that, for
an (Fi, k)-correct family G, the following statements hold:
1) G is union-closed,
2) G ⊎ Fi = G,
3) Q(G),
4) R(G, i).
We say that G is (Fi, k)-closed if it satisﬁes the ﬁrst two of
the above conditions.
Denote by 1A(x) the indicator function (equal to 1 if x ∈ A,
and equal to 0 otherwise), and by d l
i,k

d l
i,k = min{s(G) | G is (Fi, k)-correct family,
|K| = k, 1G(K) = l} (3)

Note that the weights of all the elements from K, given in
Table I, have the same values. Hence d l
i,k has the same value
 for all bases K satisfying |K| = k. Instead of considering
all the 2
12−ri hypercubes, it is enough to consider only
2(13 − ri) cases, corresponding to 0 ≤ |K| ≤ 12 − ri,
and 1Fi(K) ∈ {0, 1}.
Next, we propose a pseudo-code that can be used to ﬁnd
the smallest values of d l
i,k for every i ∈ {1, . . . , 33}, k ∈
{0, . . . , 12 − ri} and l ∈ {0, 1}, where the weights of the
elements of ∪ F assigned by function w are given in the
ith row of Table I. We prove later the correctness of the
algorithm, and consequently, our main result.
The following simple brute force algorithm for computing
d l
i,k would do the desired calculations.

Algorithm 1.
Input: families Fi, 1 ≤ i ≤ 33.
Output: values d0
i,k and d
1
i,k, for every i ∈ {1, . . . , 33} and
k ∈ {0, . . . , 12 − ri}.

for all i ∈ {1, . . . , 33}
for all k ∈ {0, . . . , 12 − ri}
set d 0
i,k ← ∞, d 1
i,k ← ∞
set K ← {ri + 1, . . . , ri + k}
for all families G ∈ {K} ⊎ 2
[ri]

if G is (Fi, k)-correct

d1G (K)
i,k ← min {
s(G), d1G (K)
i,k }

return d0
i,k and d1
i,k
The problem with the above algorithm is that the inner-
most loop examines 2
2
ri families. Even for small values
of ri, for example ri = 6, the number of families we
need to check is 2
64, which is too much, even for powerful
computers. However, it is possible to reduce the number
of the cases by considering only (Fi, k)-correct families
obtained from a family containing only sets with negative
value of share. Denote by Ni,k the following family

Ni,k = {A ∈ CK,Si | |K| = k, s(A) < 0} (4)
= {N1, . . . , Np} (5)

where s(N1) ≤ s(N2) ≤ · · · ≤ s(Np). Since K ⊆ N for
every N ∈ Ni,k, we have that N1 = K, when p ≥ 1. Also,
since weight of every element shown in Table I is positive,
we have that for every A ⊂ B is s(A) < s(B). Furthermore,
for every i ≥ 1 there does not exist j, i < j ≤ p such that
Nj ⊂ Ni.
In the case when Ni,k is empty (the only such case is i = 25,
k = 9), the lower bounds are non-negative, and they are
easily obtained:
 d 1
i,|K| = s({K} ⊎ Fi)

d 0
i,|K| = s(K ∪ Si)

Let |N | = p. Subfamilies of N can be indexed by vectors

a = (a1, . . . , ap) ∈ {0, 1}
p (6)

Denote by

Na,i,k = {Nj | Nj ∈ Ni,k, 1 ≤ j ≤ p, aj = 1}. (7)

and by Ga the minimal (Fi, k)-closed family containing
Na,i,k, that is Ga = N a,i,k ⊎ Fi (8)

TABLE I
12-FC FAMILIES AND THE CORRESPONDING WEIGHT FUNCTIONS USED IN THE PROOF OF LEMMA 4. EACH FAMILY CONTAINS ALSO AN EMPTY SET.

i Fi 1 2 3 4 5 6 7 8 − 12 t(w)
1 {1, 2, 3},{1, 2, 4},{1, 2, 3, 5} 24 24 18 18 12 2 2 2 55
2 {1, 2, 3},{1, 4, 5, 6},{2, 4, 5, 6},{3, 4, 5, 6} 24 24 24 10 10 10 2 2 57
3 {1, 2, 3},{1, 2, 3, 4},{1, 2, 3, 5},{4, 5, 6} 6 6 6 9 9 6 1 1 24
4 {1, 2, 3},{1, 4, 5} 11 7 7 7 7 1 1 1 23
5 {1, 2, 3},{1, 4, 5, 6},{2, 4, 5, 6} 6 6 4 4 4 4 1 1 17

6 {1, 2, 3},{1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 3, 6},
{1, 2, 3, 7} 8 8 8 8 8 8 8 2 33

7 {1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 4, 5},{1, 2, 3, 6},
{1, 2, 4, 6},{1, 2, 5, 6} 5 5 4 4 4 4 1 1 16

8 {1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 3, 6},{1, 2, 3, 7} 8 8 8 6 6 6 6 2 29
9 {1, 2, 3},{1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 3, 6} 10 10 10 8 8 8 2 2 33
10 {1, 2, 3},{1, 2, 3, 4},{1, 2, 3, 5},{4, 6, 7} 3 3 3 3 3 3 3 1 13
11 {1, 2, 3},{1, 2, 3, 4},{4, 5, 6} 8 8 8 14 6 6 2 2 31
12 {1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 3, 6} 10 10 10 8 8 8 2 2 33
13 {1, 2, 3},{1, 2, 4, 5},{1, 3, 4, 5} 12 12 12 8 8 2 2 2 33
14 {1, 2, 3},{1, 4, 5, 6, 7},{2, 4, 5, 6, 7},{3, 4, 5, 6, 7} 3 3 3 3 3 3 3 1 13
15 {1, 2, 3},{1, 4, 5, 6},{1, 2, 4, 5, 6} 7 7 4 4 4 4 1 1 18
16 {1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 4, 5} 9 9 8 8 8 2 2 2 28
17 {1, 2, 3},{4, 5, 6} 3 3 3 3 3 3 1 1 12
18 {1, 2, 3},{1, 2, 4} 4 4 4 4 1 1 1 1 12
19 {1, 2, 3},{1, 2, 4, 5, 6},{1, 3, 4, 5, 6} 8 8 8 6 6 6 2 2 27
20 {1, 2, 3},{1, 4, 5, 6} 6 6 6 4 4 4 2 2 21
21 {1, 2, 3},{1, 2, 3, 4},{1, 2, 3, 5} 3 3 3 3 3 1 1 1 11
22 {1, 2, 3},{1, 2, 4, 5} 10 10 8 6 6 2 2 2 27
23 {1, 2, 3},{1, 2, 4, 5, 6} 4 4 4 2 2 2 1 1 12
24 {1, 2, 3},{4, 5, 6, 7} 3 3 3 2 2 2 2 1 11
25 {1, 2, 3} 3 3 3 1 1 1 1 1 9
26 {1, 2, 3, 4},{1, 2, 3, 5},{1, 2, 3, 4, 6} 6 6 6 6 6 4 2 2 23
27 {1, 2, 3, 4},{1, 2, 3, 4, 5},{1, 2, 3, 4, 6} 2 2 2 2 2 2 1 1 9
28 {1, 2, 3, 4},{1, 2, 3, 5} 3 3 3 2 2 1 1 1 10
29 {1, 2, 3, 4, 5},{1, 2, 3, 4, 6} 3 3 3 3 3 3 1 1 12
30 {1, 2, 3, 4},{1, 2, 3, 4, 5} 3 3 3 3 3 1 1 1 11
31 {1, 2, 3, 4},{1, 2, 5, 6} 3 3 3 3 3 3 1 1 12
32 {1, 2, 3, 4} 5 5 5 5 2 2 2 2 18
33 {1, 2, 3, 4, 5} 4 4 4 4 4 2 2 2 17

Hence, the more efﬁcient version of the algorithm would
examine only (Fi, k)-closed families Ga.

Algorithm 2.
Input: families Fi, 1 ≤ i ≤ 33.
Output: values d
0
i,k and d
1
i,k, for every i ∈ {1, . . . , 33} and
k ∈ {0, . . . , 12 − ri}.

for all i ∈ {1, . . . , 33} do
for all k ∈ {0, . . . , 12 − ri} do
set d 0
i,k ← ∞, d 1
i,k ← ∞
set K ← {ri + 1, . . . , ri + k}
for all a ∈ {0, 1}
p do
set Ga ← N a,i,k ⊎ Fi
if Q(Ga) and R(Ga, i) then

d1Ga (K)
i,k ← min {
s(Ga), d1Ga (K)
i,k }

return d0
i,k and d1
i,k

Even this algorithm, though more efﬁcient than the pre-
vious one, is to demanding. It is possible to further reduce
the number of calculations with backtracking algorithm. We
now introduce some notation that makes it easier to explain
the steps of the backtracking algorithm.
Let a be a vector given by (6) and

b = (a1, . . . , at), 1 ≤ t ≤ p (9)
 Denote by v(b):

v(b) = s(Gb) + ∑

t<i≤p
Ni /∈Gb
 s(Ni). (10)

Let a and b be vectors given by (6) and (9), respectively.
We now present the backtracking algorithm, that discards
large quantity of families that have a share greater than d
l
i,k.

Algorithm 3 (backtracking()).
Input: family Fi, family Ni,k, integer k, vector b =
(a1, . . . , at)

set Gb ← Nb ⊎ Fi
if Q(Gb) and R(Gb, i) then

if v(b) < d1Gb (K)
i,k then

set d1Gb (K)
i,k ← min {
s(Gb), d1Gb (K)
i,k }

if t < |Ni,k| then
backtracking(Fi, Ni,k, k, (a1, . . . , at, 1))
if Nt+1 /∈ Gb then
backtracking(Fi, Ni,k, k, (a1, . . . , at, 0))

The following algorithm can be used to call backtracking
algorithm for each i ∈ {1, . . . , 33}, thus calculating the
values dl
i,k.

Algorithm 4.
Input: families Fi, 1 ≤ i ≤ 33.
Output: values d0
i,k and d1
i,k, for every
i ∈ {1, 2, . . . , 33} and k ∈ {0, 1, . . . , 12 − ri}.

for all i ∈ {1, . . . , 33} do
for all k ∈ {0, . . . , 12 − ri} do
set d 0
i,k ← ∞, d 1
i,k ← ∞
set K ← {ri + 1, . . . , ri + k}
calculate Ni,k
backtracking(Fi, Ni,k, k, b = (1))
if k > 0 then
backtracking(Fi, Ni,k, k, b = (0))
return d0
i,k and d1
i,k
Lemma 2. Using the Algorithm 4 we obtain the values
of d
0
i,k and d1
i,k for every i ∈ {1, 2, . . . 33} and k ∈
{0, 1, . . . 12 − ri}.

Proof. Let a and b be vectors given by (6) and (9). Let
Ga and Gb be families given by (8), obtained from the
vectors a and b, respectively. We have the following simple
observations
1) Gb ⊆ Ga,
2) if Q(Ga) then Q(Gb),
3) if R(Ga, i) then R(Gb, i),
4) v(b) ≤ s(Ga), thus if v(b) ≥ d l
i,k then s(Ga) ≥ d l
i,k.
Hence, when Gb contains as a subfamily some F C-family
or Fj, for some j < i, or when v(b) ≥ d l
i,k, then all the
vectors a, having b as a preﬁx, can be skipped. Let i ∈
{1, . . . , 33} and let F contain Fi, as a subfamily. Let G be
an (Fi, k)-correct family such that s(G) = d
1G (K)
i,k , where
k ∈ {0, . . . , ri}. Let a ∈ {0, 1}
p be the vector corresponding
to the sets from Ni,k that are included in G. We prove that
the value of d
1G (K)
i,k can be obtained by the backtracking
algorithm. Let l = |Na,i,k|.
We proceed by induction on l. Obviously, for l = 0 the
value of d
1G (K)
i,k is obtained. Thus, we may assume that l ≥
1 and that for every 0 ≤ j < l, the family induced by
the vector (a1, . . . , aj) with d
1G (K)
i,k can be reached by the
backtracking algorithm. Let H = G ∩ Ni,k, and let m be
the largest number, such that Nm ∈ H, 1 ≤ m ≤ l and
G − Nm ̸= G. Furthermore, let n be the largest number,
such that 1 ≤ n < m, Nn ∈ G, and in case such Nn does
not exists, let n = 0. By the induction hypothesis, family
Gb = N b,i,k ⊎ Fi, where b = (a1, . . . , an), can be reached.
Since value of v(b) from (10) is smaller or equal to d
1G (K)
i,k
the backtracking algorithm will continue with recursive calls,
all the way to the a = (a1, . . . , am), thus the values of dl
i,k
for l = 0, 1 are obtained.

Example 2. Let i = 32, then F32 = {{1, 2, 3, 4}}, Si =∪ F32 = [4], ri = |Si| = 4. The weights are w(1) = w(2) =
w(3) = w(4) = 5, and w(x) = 2 for all x > 4; t(w) = 18.
When k = 0, then the base of the hypercube is K = ∅, and
in case when k = 1 the base of the hypercube is K = {5}.
In both cases sets with negative share are

N = {∅, {1}, {2}, {3}, {4}, {1, 3}, {2, 3}, {1, 2}, {1, 4},

{2, 4}, {3, 4}, {1, 2, 4}, {1, 2, 3}, {1, 3, 4}, {2, 3, 4}} .
 The values d 1
32,0 = −16 and d 0
32,1 = 4 are calculated after
the sequence of recursive calls listed in Tables II and III,
respectively.
 TABLE III
THE SEQUENCE OF RECURSIVE CALLS, k = 1, EXAMPLE 2.

a Na,i,k backtracking?
K ∈ Ga
1 {{5}} yes, Ga contains FC family {{5}}
K /∈ Ga
01 {{1, 5}} yes, Ga contains FC family {{1, 5}}

The values of d l
i,k, given in the Table IV, are obtained
with program written in Java programming language im-
plementing the Algorithm 4. It takes about ﬁve minutes to
calculate all these values, on 64-bit Acer laptop with Intel’s
i7 processor, on 2.4 GHz, with 16 GB of RAM. The largest
number of recursive calls for some of the cases is 34437982
for (i, k) = (14, 2). Note that values of (i, k, l) are left out
from the Table IV when:

• 1 ≤ i ≤ 33, k = 0, l = 0.
This is done because an empty set is implicitly included
in all of the considered families;

• 1 ≤ i ≤ 33, k ∈ {1, 2}, l = 1.
According to Theorem 1, any family containing a
singleton or doublet is Frankl’s.

• i ≥ 18, k = 3, l = 1.
Ga contains a family equivalent to F17 =
{{1, 2, 3}, {4, 5, 6}}, the ﬁrst 3-set is K, and the
second one is an element of Fj, 18 ≤ j ≤ 24.

• i ≥ 25, k = 3, l = 1.
Ga ⊇ K ∼ F25 = {{1, 2, 3}}.

• i = 25, k = 4, l = 1.
Ga ⊇ F25 ∪ {K} = {{1, 2, 3}, {4, 5, 6, 7}} ∼ F24.

• i = 33, k = 4, l = 1.
Ga ⊇ K = {{1, 2, 3, 4}} ∼ F32.

Lemma 3. Suppose A, B and C are three different three-
member sets. Then at least one of the following three
statements is true:

1) The union of some two of the sets A, B and C is a
ﬁve-element set.
2) There are two pairs of disjoint sets among A, B, C.
3) The family {A, B, C} is FC.

Proof. Since the size of the intersection of two different
three-member sets is 0, 1 or 2, we have the following
possibilities:

1) The intersection of some two of the sets is one-element
set. Then the size of their union is ﬁve, and the ﬁrst
statement is true.
2) Neither of the two-set intersections is one-element set.
a) Some two of the three sets A, B, C are disjoint.
Assume that A ∩ B = ∅. Then |C ∩ A| = 0 or
|C ∩ B| = 0 (otherwise, it would be |C ∩ A| =
|C ∩ B| = 2, implying |C| ≥ 4), and the second
statement is true.

b) Intersection of any two of the sets A, B and C
is a nonempty set. Then |A ∩ B| = |A ∩ C| =
|B ∩C| = 2. Let |A∩B ∩C| = q. The case q = 0
is impossible. If q = 1, then |A ∪ B ∪ C| = 4,
and if q = 2, then |A ∪ B ∪ C| = 5. In both
cases the family {A, B, C} is FC by Theorem 1,
hence the third statement is true.

Lemma 4. The families Fi listed in Table I are 12-FC,
1 ≤ i ≤ 33.

Proof. Let the values of d
l
i,k, 0 ≤ k ≤ 12 − ri, l ∈ {0, 1},
given in the Table IV, be the smallest values of share of
all the families that contain family equivalent to Fi as a
subset, and do not contain as a subset a family equivalent to
some FC family from Theorem 1 or Fj, for any 1 ≤ j < i.
Let Kk = {K|K ⊆ X \ Si, |K| = k}. We have that |Kk| =(12−ri
k ). CK,Si ∩F ̸= ∅ for |K| = 0 and |K| = 12−ri, since
Si ∈ F and X = [12] ∈ F , and in both cases |Kk| = 1. Let
Wi denote smaller of the two values of the share bounds
(when F contains, and when it does not contain a set K) of
the upper hypercube, that is Wi = min{d 0
i,12−ri , d 1
i,12−ri }.
Case i = 7, 8 or 17 ≤ i ≤ 33:
From Table I could be seen that d l
i,k < 0, and
hence s(CK,Si ∩ F ) < 0 is possible only when
k = 0. But, for all such i, the negative share of the
lowest hypercube is compensated by the share of
the uppermost hypercube: s(F) ≥ d 1
i,0 + Wi ≥ 0.
Case 1 ≤ i ≤ 6 or 9 ≤ i ≤ 16:
d l
i,k < 0 is possible only if k ∈ {0, 3}. We have
12 − ri ∈ {5, 6, 7}. Let

mi = { 3, if 12 − ri = 5
4, if 12 − ri ∈ {6, 7}.

If |K3| ≥ mi, then the family K3 ⊂ F is FC
by Theorem 1. Otherwise, if |K3| ≤ mi − 2, then
s(F) ≥ di,0 +Wi +(mi −2)d
1
i,3 ≥ 0 (see Table V).
In the remaining case |K3| = mi − 1 the inequality
s(F) ≥ 0 is also true; indeed, from Lemma 3 and
Table V it follows that:

• 12 − ri = 7: s(F) ≥ d 1
i,0 + (mi − 1)d 1
i,3 +
min{d 1
i,5, 2d 1
i,6} + Wi ≥ 0

• 12 − ri = 6: s(F) ≥ d 1
i,0 + (mi − 1)d 1
i,3 +
d 1
i,5 + d 1
i,6 ≥ 0

• 12−ri = 5: s(F) ≥ d 1
i,0+(mi−1)d 1
i,3+d 1
i,5 ≥
0

Theorem 2. If F is a union-closed family, X = ∪ F and
|X| = 12, then F is Frankl’s.

Proof. Suppose F is not Frankl’s. Then F does not contain
a singleton, nor does F contain a doublet. From Lemma 4
it follows that F does not contain

• a subfamily equivalent to F25 = [3],

• a subfamily equivalent to F32 = [4],

• a subfamily equivalent to F33 = [5].
 TABLE V
CALCULATIONS ACCOMPANYING THE PROOF OF LEMMA 4. b ∈ {0, 1},
i IS THE NUMBER OF ROW IN TABLE IV WITH d1
i,3 < 0, mi ∈ {3, 4},
ri = | ∪ Fi|.

|K| 0 3 5 6 7
i \b 1 1 1 1 1 0 mi ri s(F) ≥
1 60 -36 30 58 86 55 4 5 37
2 30 -40 56 96 4 6 62
3 6 -15 15 30 4 6 6
4 -3 -6 6 12 18 23 4 5 3
5 2 -2 20 29 4 6 45
6 60 -18 140 3 7 164
9 30 -23 56 96 4 6 113
10 -9 -4 24 3 7 7
11 -17 -5 26 38 4 6 32
12 27 -7 49 87 4 6 142
13 3 -1 23 45 64 33 4 5 56
14 6 -9 32 3 7 20
15 3 -5 14 24 4 6 26
16 -2 -10 24 48 64 28 4 5 20

Thus, all sets in F (except the set ∅) have 6 or more
elements. Let the weight function w be such that w(x) = 1
for all x ∈ X. Then t(w) = 6, s(∅) + s(X) = 0, and for
all non empty sets A ∈ F we have s(A) ≥ 0. Therefore,
s(F) ≥ 0, and F is Frankl’s, which is a contradiction, thus
proving the theorem statement.

If there exists a counterexample F to Frankl’s conjecture,
when ∪ F < 12, then it would be possible to construct
(see [2]) a counterexample F ′, when ∪ F ′ = 12. Therefore,
if F is a union-closed family, X = ∪ F and |X| ≤ 12, then
F is Frankl’s.
Lo Faro [8] and later Roberts and Simpson [10] proved
that if minimal counterexample, in terms of | ∪ F|, has
m elements than any counterexample has at least 4m − 1
sets. As a direct consequence of this statement we have the
following corollary.

Corrolary 3. Frankl’s conjecture is satisﬁed for any union
closed family with at most 50 sets.

4. CONCLUSION

Implementing technique presented in this paper on fami-
lies having 13 or more elements is probably a difﬁcult task.
The main problem is that, when ∪ F has only one more
element, the number of families that should be considered
grows exponentially. That, even with very efﬁcient algo-
rithm, demands too many calculations.

5. ACKNOWLEDGEMENT

We thank the referees for many useful suggestions that
helped us improve the article.

REFERENCES

[1] P. Markovi´c, An Attempt at Frankl’s Conjecture, Publ. Math. Inst.
81(95) (2007), pp. 29–43.
[2] I. Boˇsnjak, P. Markovi´c, The 11-element case of Frankl’s conjecture,
The Electronic J. Combin. 15 (2008) #R88.
[3] H. Bruhn, O. Schaudt, The Journey of the Union-Closed Sets Con-
jecture, Graphs and Combinatorics 31 (2015), pp. 2043–2074.

[4] R. Morris, FC-families and improved bounds for Frankl’s conjecture,
European J. Combin. 27(2006), no. 2, pp. 269–282.
[5] B. Poonen, Union-Closed Families, J. Combin. Theory Ser. A 59
(1992), no. 2, pp. 253–268.
[6] T. P. Vaughan, Families implying the Frankl conjecture, Europ. J.
Combin. 23 (2002), pp. 851–860.
[7] F. Mari´c, M. ˇZivkovi´c, B. Vuˇckovi´c, Formalizing Frankls Conjec-
ture: FC-Families, Intelligent Computer Mathematics, Volume 7362
(2012), pp 248-263.
[8] G. Lo Faro, Union-closed sets conjecture: Improved bounds, J.
Combin. Math. Combin. Comput. 16 (1994), pp. 97–102.
[9] D. G. Sarvate and J. C. Renaud, On the union-closed sets conjecture,
Ars Combin. 27 (1989), pp. 149–154.
[10] I. Roberts , J. Simpson, A note on the union-closed sets conjecture,
Australas. J. Combin. 47 (2010), pp. 265–267.
[11] W. Gao and H. Yu, Note on the union-closed sets conjecture, Ars
Combin. 49 (1998), pp. 280–288.
 TABLE II
THE SEQUENCE OF RECURSIVE CALLS, EXAMPLE 2.

a Na backtracking?
K ∈ Ga
1 {∅} no
11 {∅, {1}} yes, Ga contains FC family {{1}}
101 {∅, {2}} yes, Ga contains FC family {{2}}
1001 {∅, {3}} yes, Ga contains FC family {{3}}
10001 {∅, {4}} yes, Ga contains FC family {{4}}
100001 {∅, {1, 3}} yes, Ga contains FC family {{1, 3}}
1000001 {∅, {2, 3}} yes, Ga contains FC family {{2, 3}}
10000001 {∅, {1, 2}} yes, Ga contains FC family {{1, 2}}
100000001 {∅, {1, 4}} yes, Ga contains FC family {{1, 4}}
1000000001 {∅, {2, 4}} yes, Ga contains FC family {{2, 4}}
10000000001 {∅, {3, 4}} yes, Ga contains FC family {{3, 4}}
100000000001 {∅, {1, 2, 4}} yes, Ga contains {{1, 2, 4}} equivalent to F25
1000000000001 {∅, {1, 2, 3}} yes, Ga contains {{1, 2, 3}} equivalent to F25
10000000000001 {∅, {1, 3, 4}} yes, Ga contains {{1, 3, 4}} equivalent to F25
100000000000001 {∅, {2, 3, 4}} yes, Ga contains {{2, 3, 4}} equivalent to F25
100000000000000 {∅} no, t = |N |, d 1
33,0 = s(Ga) = −16

TABLE IV
LOWER BOUNDS d l
i,k ON HYPERCUBE SHARES IN LEMMA 4, 1 ≤ i ≤ 33, 0 ≤ k ≤ 12 − | ∪ Fi|, l ∈ {0, 1}.

|K| 0 1 2 3 4 5 6 7 8 9
i \l 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 12 − ri ri
1 60 38 15 −36 13 0 43 30 51 58 53 86 55 7 5
2 30 47 45 −40 11 8 53 56 55 96 57 6 6
3 6 19 12 −15 6 0 20 15 23 30 24 6 6
4 −3 12 3 −6 1 0 19 6 21 12 22 18 23 7 5
5 2 12 9 −2 4 5 15 20 16 29 17 6 6
6 60 25 1 −18 9 52 31 140 33 5 7
7 22 11 8 7 4 26 14 53 15 80 16 6 6
8 58 18 7 15 6 77 27 155 29 5 7
9 30 14 3 −23 1 8 28 56 31 96 33 6 6
10 −9 6 0 −4 1 9 12 24 13 5 7
11 −17 8 16 −5 9 8 27 26 29 38 31 6 6
12 27 14 12 −7 1 3 28 49 31 87 33 6 6
13 3 19 18 −1 20 1 26 23 29 45 31 64 33 7 5
14 6 3 6 −9 1 9 12 32 13 5 7
15 3 8 11 −5 7 0 13 14 17 24 18 6 6
16 −2 10 4 −10 12 0 20 24 24 48 26 64 28 7 5
17 −12 2 6 0 0 0 8 8 11 12 12 6 6
18 −8 4 4 1 0 8 6 9 14 10 19 11 24 12 8 4
19 −1 16 13 14 0 19 19 25 41 27 6 6
20 −18 2 1 0 3 16 17 19 27 21 6 6
21 −7 5 3 0 0 7 9 9 20 10 27 11 7 5
22 −8 15 12 2 1 17 14 23 31 25 43 27 7 5
23 −4 3 4 2 2 10 10 11 18 12 6 6
24 −10 4 3 0 3 10 10 11 5 7
25 −9 1 2 3 1 0 4 3 6 5 7 7 8 9 9 9 3
26 0 8 5 2 8 19 43 21 65 23 6 6
27 −7 0 0 0 1 6 16 8 24 9 6 6
28 −5 1 0 1 4 3 8 7 15 9 22 10 7 5
29 0 5 3 6 6 0 7 10 18 12 6 6
30 −6 3 3 0 1 3 3 6 9 8 14 10 7 5
31 −6 7 2 6 6 10 5 11 12 12 6 6
32 −16 4 6 1 0 5 0 8 7 13 12 16 16 18 8 4
33 −14 5 5 6 5 1 8 9 14 14 17 7 5
