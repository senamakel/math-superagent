<!-- source: https://www.igorballa.com/nov-30-UC.pdf | converted from PDF -->

Union-closed Families of Sets

Igor Balla, B´ela Bollob´as ∗†‡ and Tom Eccles §¶

November 30, 2011

Abstract

A family of sets is union-closed if it contains the union of any two of
its elements. Reimer [18] and Cz´edli [3] investigated the average size of an
element of a union-closed family consisting of m subsets of a ground set
with n elements. We determine the minimum average size precisely, ver-
ifying a conjecture of Cz´edli, Mar´oti and Schmidt [4]. As a consequence,
the union-closed conjecture holds if m ≥ 2
3 .2
n – in this case some element
of [n] is in at least half the sets of the family.

1 Introduction

Let A be a ﬁnite family of ﬁnite sets; as often, we shall assume that A is non-
empty and consists of subsets of [n] = {1, . . . , n}, i.e.

∅ ̸= A ⊂ P(n) = P([n]).

The degree of x ∈ [n] in A is

dA(x) = |{A ∈ A : x ∈ A}|.

Recall that A is an up-set (in P(n)) if B ∈ A whenever A ⊂ B, A ∈ A and
B ∈ P(n). A similar, but weaker property of A is that it is union-closed:
A ∪ B ∈ A whenever A, B ∈ A. As usual, we shall assume that the groundset
[n] is as small as possible: ⋃
A∈A A = [n]. Trivially, if A is an up-set then
dA(x) ≥ |A|/2 for every x ∈ [n]: indeed, A ↦→ A ∪ {x} is an injection from
{A ∈ A : x /∈ A} into {A ∈ A : x ∈ A}. Clearly, not every union-closed family

∗Department of Pure Mathematics and Mathematical Statistics, Wilberforce Road, Cam-
bridge CB3 0WB, UK
†Department of Mathematical Sciences, University of Memphis, Memphis TN 38152, USA
‡Research supported in part by NSF grants DMS-0906634, CNS-0721983 and CCF-
0728928, and ARO grant W911NF-06-1-0076
§Department of Pure Mathematics and Mathematical Statistics, Wilberforce Road, Cam-
bridge CB3 0WB, UK
¶Part of this research was done while the second and third authors were visiting the Theory
Group of Microsoft Research.
 1

has this property; e.g. if A = {[k] : 0 ≤ k ≤ n} then A is union-closed and
dA(n) = 1 = |A|/(n + 1). However, it seems that it may be true that

dA(x) ≥ |A|/2 for some x ∈ [n]. (1)

Indeed, the union-closed degree conjecture, or simply union-closed conjecture,
usually attributed to Frankl, says that this is the case: if A is a union-closed
family then some element is contained in at least half of the sets in A. (In
fact, the ﬁrst such attribution appeared in 1985 [5], but the conjecture was well
known by the mid-1970s as a ‘folklore conjecture’.)
Over the years, much work has been done on this conjecture, and yet, it has
only been proved when the size of the groundset [n] or the system A is very
restricted. Boˇsnjak and Markovi´c [2] settled it for n ≤ 11, improving on results
of Markovi´c [14], Morris [15], Gao and Yu [7], Poonen [17] and Lo Faro [12].
Roberts and Simpson [20] show that if q is the smallest n for which there is a
counterexample, then any counterexample A has |A| ≥ 4q − 1. Since q ≥ 12,
this implies the conjecture for |A| ≤ 46, improving bounds given by Lo Faro
[13] and Poonen [17].
In 2003 Reimer [18] considered the union-closed size problem, a problem
closely related to the union-closed degree conjecture: what is

f (m) = min ||A||,

where the minimum is over all union-closed families A of ﬁnite sets consisting
of m sets, and ||A|| is the total size of the sets in A,

||A|| = ∑

A∈A |A|.

Reimer [18] proved that f (m) ≥ m
2 log2 m. (2)

Clearly, equality holds whenever m = 2
k, since we may take A = P(k). In fact,
(2) is strict in every other case.
Recently, Cz´edli [3] studied a reﬁnement of the function f (m). For 0 ≤ m ≤
2n, let f (n, m) = min ||A||,

where the minimum is over all union-closed families A of subsets of [n] with
|A| = m. (The inequality m ≤ 2
n is not really a restriction, since if A is a
family of subsets on [n] then m ≤ 2n.)

Clearly, if ||A|| ≥ mn/2 and A ⊂ P(n) then (1) holds. Hence, setting

m0 = m0(n) = min{m
∗ : f (n, m) ≥ mn/2 if m ≥ m
∗},

the union-closed conjecture holds whenever |A| ≥ m0. A priori it is not clear
that m0 is smaller than 2
n (after all, it could be that Reimer’s inequality (2) is

2

close to best possible), but a moment’s thought tells us that this is the case. In
fact, Cz´edli [3] has proved that m0 is not too close to 2n: 2n − m0 ≥ ⌊2
n/2⌋.
From the other direction, Cz´edli, Mar´oti and Schmidt [4] showed that m0 ≥
2⌈2
n/3⌉. Our main aim in this paper is to determine f (n, m) precisely and give
the extremal families for all n and m, and so settle the union-closed size problem
completely. In particular, our result implies that m0 = 2⌈2
n/3⌉; a fortiori, the
union-closed conjecture holds for families in P(n) with at least 2
3 .2n elements.
This result was conjectured by Cz´edli, Mar´oti and Schmidt [4]; they also proved
that it does hold provided the union-closed conjecture holds.
The rest of this paper is organised as follows. In Section 2, we shall discuss
the initial segments of the colex order, enabling us to state our main theorem,
giving the value of f (n, m). Section 3 consists of the proof of the main theorem,
and in Section 4 we shall determine the structure of all extremal families. In
Section 5 we shall determine some quantitative bounds on f (n, m): our main
goal shall be to determine m0. In Section 6 we prove bounds for the sizes of a
restricted class of union-closed family. In Section 7 we prove a slightly stronger
result in the case when we have a hypothetical counterexample to the union-
closed conjecture. Finally, in Section 8, we conjecture a relationship between
the total size of union-closed family and the minimum degree of an element in
it.

2 The Main Result

Before stating our main theorem, let us recall the deﬁnition of the colex order on
ﬁnite sets of positive integers, and in particular the Kruskal–Katona theorem on
the cardinalities of shadows. The colex order on N(<∞), the collection of ﬁnite
sets of positive integers, is the linear order < on N(<∞) in which A < B if and
only if max(A△B) ∈ B. E.g., writing 124 for the set {1, 2, 4}, the colex order on
N(<∞) starts as follows: ∅ < 1 < 2 < 12 < 3 < 13 < 23 < 123 < 4 < 14 < 124.
It is immediate that < is indeed a linear order. We write I(m) for the initial
segment of length m of N(<∞) in the colex order, and Ik(m) for the initial
segment of length m of N(k) in the colex order. The fundamental theorem of
Kruskal [10] and Katona [9] states that if A ⊂ N(k) with |A| = m, then the lower
shadow of A is at least as large as the lower shadow of Ik(m); consequently,
|∂i(A)| ≥ |∂i(Ik(m))| for all A ⊂ N(k) with |A| = m and 0 ≤ i ≤ k. Let us state
an easy consequence of this Kruskal–Katona theorem as a lemma, since this is
the fact that we shall exploit.

Lemma 1. If D is a down-set, then ||D|| ≤ ||I(|D|)||. □

A consequence of this is a simple relationship between the total sizes of the
initial segments of the colex order.

Lemma 2. For all m1, m2 ≥ 1 we have

||I(m1 + m2)|| ≥ ||I(m1)|| + ||I(m2)|| + min(m1, m2). (3)

3

This follows (for m1 ≥ m2) by considering the down-set I(m1) ∪ {A ∪ {0} :
A ∈ I(m2)}, the total size of which is precisely the right hand side of (3).
Our main theorem, Theorem 3, giving the smallest average size of a set in
a union-closed family, was proved by Cz´edli, Mar´oti and Schmidt [4] under the
assumption that the union-closed conjecture holds; they also conjectured that
it holds unconditionally. As a by-product of our theorem, we ﬁnd that although
the function f (n, m) is a reﬁnement of f (m) it is, in fact, independent of n.
We need one more important ingredient before we can state our main result,
for which we give two deﬁnitions. First, for m < 2
n write m in the following
form: m = 2n−1 + 2
n−2 + ... + 2
k + m
′, where k and m
′ are integers, with
m′ ≤ 2k−1. Then deﬁne a family M(n, m) of subsets of P(n) by M(n, m) =
{B ∈ P(n) : B ∩ [k + 1, n] ̸= ∅} ∪ {B + k : B ∈ I(m
′)}. Here and elsewhere we
use the shorthand B + k for B ∪ {k}, and B − k for B \ {k}. Furthermore, for
m = 2
n we deﬁne M(n, m) = P(n).
Alternatively, we can deﬁne M(n, m) through another order on P(n). For
A, B ∈ P(n), let the mixed order to be a total order <M given by

A <M B ⇐⇒
 {max(A) > max(B) or
max(A) = max(B) and max(A△B) ∈ B.

Then M(n, m) is the initial segment of size m of the mixed order on P(n).
(On the set of all ﬁnite subsets of N the mixed order does not have a smallest
element, so does not have ﬁnite initial segments.)
It can easily be seen that for each n with 2
n ≥ m, the families P(n) \
M(n, 2
n − m) are identical. We deﬁne F(m) to be P(n) \ M(n, 2n − m) for any
n ≥ 2m. If k = ⌈log2(m)⌉, we can write F(m) = P(k − 1) ∪ {A + k : A ∈ U},
where U = P(k − 1) \ I(2
k − m) is an up-set contained in P(k − 1). Then we
shall prove the following result.

Theorem 3. For n, m ≥ 1 and 2
n ≥ m we have

f (n, m) = f (m) = ||F(m)||, (4)

i.e. if F ⊂ P(n) is a union-closed family and |F| = m then ||F|| ≥ ||F(m)||.
Equality holds when F = F(m).

3 Proof of Theorem 3

As in [18], we consider applying up-compressions to a union-closed family. To
perform an up-compression in direction i, we add i to any set A of A for which
A+i is not already in A. Formally, given a family A ⊂ P(n), an element i ∈ [n],
and a set A ∈ A, deﬁne

u(A,i)(A) =
 {A : A + i ∈ A,
A + i : A + i /∈ A.

4

Now, deﬁne the up-compression of A in direction i by

ui(A) = {u(A,i)(A) : A ∈ A}.

Also, deﬁne Ai by Ai = ui . . . u1(A); in particular, A0 = A. We then deﬁne
u(A) = An, and for A ∈ A deﬁne Ai = u(Ai−1,i) . . . u(A1,2)u(A,1)(A): this is the
“image of A” in Ai, so that Ai = {Ai : A ∈ A}. Also, occasionally we write
uA(A) for An.
We shall make use of a result of Reimer [18]; for the sake of completeness,
we prove it here.

Theorem 4. Let A ⊂ P(n). Then

(i) u(A) is an up-set;

(ii) if A is union-closed, the family Ai is union-closed for each 0 ≤ i ≤ n;

(iii) if A is union-closed, the cubes [A, uA(A)] and [B, uA(B)] are disjoint for
A and B distinct sets in A.

Proof. (i) This is well known and easily checked for any family A. In fact, all
that has to be shown is that if 1 ≤ i < j ≤ n then ui(Aj) = Aj.
(ii) It suﬃces to show that A1 = u1(A) is union-closed; then by induction
each Ai is union-closed also. Now, suppose A and B are sets in A1 – our task
to show A ∪ B is also in A1. If 1 ∈ A then either A or A − 1 is in A, and either
B or B − 1 is also in A. Hence either A ∪ B or A ∪ B − 1 is in A, as this family
is union-closed. In either case we have A ∪ B ∈ u1(A) = A1. If, on the other
hand, 1 /∈ A ∪ B, the sets A, B, A + 1 and B + 1 must all appear in A and A1.
Hence in A we have the sets A ∪ B and A ∪ B + 1, since A is union-closed. But
then these sets are in A1 also, so A ∪ B = u(A,1)(A ∪ B) ∈ A1.
(iii) In proving this assertion we may assume by symmetry that B ̸⊂ A. Now,
we claim that for all 0 ≤ i ≤ n, Ai ∪ B ∈ Ai. For i = 0 this is immediate from
A being union closed. Now, let 1 ≤ k ≤ n, and assume that Ak−1 ∪ B ∈ Ak−1.
To prove our claim, we consider three cases.
If k ∈ Ak−1 then Ak = Ak−1, and k ∈ Ak−1 ∪B. Hence Ak ∪B = Ak−1 ∪B ∈
Ak, as required.
If k /∈ Ak−1 but k ∈ Ak, then Ak−1 ∪ B ∈ Ak−1 is enough to guarantee
Ak ∪ B = Ak−1 ∪ B ∪ {k} ∈ Ak.
Finally, if k /∈ Ak then we have both Ak and Ak + k in Ak−1. Hence by the
induction hypothesis both Ak ∪ B and Ak ∪ B + k are in Ak−1 (although they
may be the same set). This is enough to guarantee Ak ∪ B ∈ Ak, as required.
Consequently, if B ̸⊂ A in A, then B ̸⊂ Ai for any i. Indeed, suppose B ⊂
Ai, and take i minimal such that this holds. Then we must have Ai−1 = Ai − i,
i ∈ B and Ai /∈ Ai−1. But then by the above we have Ai−1 ∪ B = Ai ∈ Ai−1, a
contradiction.
But if the cubes [A, uA(A)] and [B, uA(B)] intersect, then we have B ⊂ An.
Since we have shown this cannot happen, these cubes are disjoint.

5

Using this result, we can give the following suﬃcient condition for a union-
closed family to have the smallest possible total size. To state this result, for
A ∈ A we set rA(A) = |uA(A) \ A|: this is the total number of elements added
to A by our compressions.

Lemma 5. Suppose that A ⊂ P(n) is a union-closed family of m elements such
that the following hold:

(i) there exists an integer k so that for each A ∈ A, k ≤ rA(A) ≤ k + 1;

(ii) for each S ∈ P(n), there exists A ∈ A such that S ∈ [A, uA(A)];

(iii) ||u(A)|| is the minimal total size of an up-set with m elements in P(n).

Then f (n, m) = ||A||; that is, A has the smallest possible total size for a union-
closed family of m sets in P(n).

Proof. Let A
′ be another union-closed family of m elements in P(n) – our task
is to show that ||A
′|| ≥ ||A||. Note that from the second condition of the lemma,
together with Theorem 4, we have that ∑

A∈A′ 2
rA′ (A) ≤ ∑

A∈A 2
rA(A) = 2n.
Together with the ﬁrst condition, this implies that ∑

A∈A′ rA′(A) ≤ ∑

A∈A rA(A).
Also, the third condition of the lemma implies ||u(A
′)|| ≥ ||u(A)||. Hence we
have
 ||A
′|| = ||u(A
′)|| − ∑

A∈A′ rA′(A)

≥ ||u(A)|| − ∑

A∈A rA(A) = ||A||,

as required.

Lemma 6. Let A = F(m), viewed as a subset of P(n). Then A satisﬁes all
the conditions of Lemma 5.

Proof. Let k = ⌈log2(m)⌉, and write F(m) = P(k − 1) ∪ {A + k : A ∈ U}, where
U is an up-set contained in P(k − 1). For a set S ∈ A, it is easy to see that

uA(S) =
 {S ∪ [k, n] : k /∈ S, S /∈ U
S ∪ [k + 1, n] : otherwise .

Hence for each A ∈ A we have n − k + 1 ≤ rA(A) ≤ n − k, and so the ﬁrst
condition of Lemma 5 is satisﬁed.
For the second condition, consider S ∈ P(n). First, suppose k /∈ S. Then
let S = S1 ∪ S2, with S1 ⊂ [1, k − 1], S2 ⊂ [k + 1, n]. Now, S1 ∈ A, and uA(S1)
is either S1 ∪ [k + 1, n] or S1 ∪ [k, n]. In either case, S ∈ [S1, uA(S1)].
Next suppose k ∈ S. Let S = S1 ∪ S2 ∪ {k}, again with S1 ⊂ [1, k − 1],
S2 ⊂ [k + 1, n]. If S1 ∪ {k} ∈ A then uA(S1 ∪ {k}) = S1 ∪ [k + 1, n], and so S ⊂
[S1 ∪ {k}, uA(S1 ∪ {k})]. If S1 ∪ {k} /∈ A then S1 ∈ A and uA(S1) = S1 ∪ [k, n].
In this case we have S ∈ [S1, uA(S1)].
 6

For the third condition, note that u(A) = {S : [k, n] ⊂ S} ∪ {S ∪ [k + 1, n] :
S ∈ U}. Recalling that U is the complement of an initial segment of colex in
P(k − 1), let Dmax be the maximal set in this initial segment of colex. Then

P(n) \ u(A) = {B ∈ N(<∞) : B < Dmax ∪ [k + 1, n]} = I(2
n − m).

So ||P(n) \ u(A)|| is maximal over down-sets with 2
n − m elements, and hence
||u(A)|| is minimal over up-sets of P(n) with m elements.

Putting together Lemmas 5 and 6, we ﬁnd that f (n, m) = ||F(m)||, proving
Theorem 3.

4 Extremal examples for Theorem 3

In this section, we examine the proof of Theorem 3 to determine the extremal
families for f (m). The following lemma shows that in fact the conditions of
Lemma 5 are not only suﬃcient but also necessary for a union-closed family A
of m sets to have ||A|| = f (m).

Lemma 7. Suppose A ⊂ P(n) is a union-closed family with |A| = m and
||A|| = f (m). Then A satisﬁes the conditions of Lemma 5; that is

(i) there exists an integer k so that for each A ∈ A, k ≤ |uA(A) \ A| ≤ k + 1;

(ii) for each S ∈ P(n), there exists A ∈ A such that S ∈ [A, uA(A)];

(iii) ||u(A)|| is the minimal total size of an up-set with m elements in P(n).

Proof. Just as in the proof of Theorem 3, if we set A
′ = F(m) we have∑

A∈A rA(A) ≤ ∑

A∈A′ rA′(A), and ||u(A)|| ≥ ||u(A
′)||. If either of the ﬁrst
two conditions of the lemma fail to hold for A, then the ﬁrst of these inequali-
ties is strict. If the third fails to hold, then the second is strict. In either case,
||A
′|| > ||A||.

For a union-closed family A, we deﬁne g(A) to be the groundset of A; that
is g(A) = ⋃
A∈A A. Then, making use of Lemma 7, we can put the following
conditions on a union-closed family of extremal size:

Lemma 8. Suppose that A is union-closed, with |A| = m and ||A|| = f (m).
Let n0 = ⌈log2 m⌉. Then |g(A)| = n0, and there is a subset R ⊂ g(A) with
|R| = n0 − 1 such that P(R) ⊂ A. Let g(A) \ R = {x}. Then {A ⊂ P(R) :
A + x ∈ A} is an up-set in P(R) of size m − 2k−1, having the minimal possible
total size for such an up-set.

Proof. Suppose |g(A)| = n; then we may assume g(A) = [n]. View A as a
subset of P(n). Since A satisﬁes the ﬁrst condition of Lemma 7, there must be
some k such that for each A ∈ A we have k ≤ |uA(A)\A| ≤ k +1. Also, we must
have ⋃
A∈A[A, u(A)] = P(n); and hence we must have 2
k|A| ≤ 2n ≤ 2
k+1|A|.
Thus k = n − n0. However, [n] ∈ A, and uA([n]) = [n], and so 0 ∈ {k, k + 1},

7

giving n = n0 or n = n0 − 1. The latter is impossible, as m > 2
n0−1, so n = n0
and k = 0.
For the existence of the subset R, by the union-closed property it is enough
to show that A contains the empty set and all but at most 1 singleton. If
∅ /∈ A, then ∅ /∈ [A, uA(A)] for any A ∈ A, contradicting the second condition
of Lemma 7. Now, suppose some singleton {i} is not in A. Then from the second
condition of Lemma 7, there exists A ∈ A with {i} ∈ [A, uA(A)]. Thus A ⊂ {i},
and so A = ∅. If there are two such singletons i1 and i2, then {i1, i2} ⊂ uA(∅),
and so |uA(∅) \ ∅| ≥ 2. This contradicts the ﬁrst condition of Lemma 7, since
k = 0.
Now, taking [n] \ R = {x}, let S = {A ⊂ P(R) : A + x ∈ A}. If R1 ∈ S
and R1 ⊂ R2 with R2 ∈ P(R), then R2 \ R1 ∈ P(R), and hence R2 \ R1 ∈ A.
Thus (R1 + x) ∪ (R2 \ R1) = R2 + x ∈ A, and so R2 is also in S. Hence S is an
up-set in P(R). If S does not have minimal total size for an up-set of |S| sets in
P(R), then let S′ be another up-set of |S| sets in P(R) with ||S′|| < ||S||. Let
A
′ = P(R) ∪ {A + x : A ∈ S′}. Then A
′ is union-closed and |A′| = |A|, but
||A
′|| < ||A||, which is a contradiction.

In fact, this is enough to show that the extremal families F(m) are unique
up to isomorphism, since it is a consequence of the Kruskal-Katona Theorem
that the up-set in P(n) of m sets with smallest total size is unique.

5 Quantitative Bounds

An interesting implication of Theorem 3 is that ||A|| ≥ |A|n/2 if |A| is large
enough. Cz´edli, Mar´oti and Schmidt [4] proved that ||I(m)|| ≤ m(n/2 − 1)
exactly when m < 2
n/3. Since for m ≤ 2
n−1 we have ||M(m, n)|| = ||I(m)|| +
m, this will yield the union-closed conjecture for families A with at least 2
3 2
n

elements. We are able to give a somewhat simpler proof of this result, making
use of the following simple upper and lower bounds on ||I(m)||.

Lemma 9. For all positive integers m,

m(log2 m − 1)/2 < ||I(m)|| ≤ m(log2 m)/2. (5)

Equality in the upper bound of (5) is only achieved for m = 2
k.

Proof. We proceed by induction on m. For m = 1 we have equality in the upper
bound. For m ≥ 2, write m = k + ℓ, where k = 2
r is a power of 2 and ℓ < k.
If ℓ = 0, then I(m) = P(r), and we get equality in the upper bound of (5),
so we shall assume ℓ > 0. We note that I(m) consists of P(r), together with
{A ∪ {r + 1} : A ∈ I(ℓ)}. From this, we have

||I(m)|| = k(log2 k)/2 + ||I(ℓ)|| + ℓ.

Let us start with the upper bound of (5). By the induction hypothesis we have
that ||I(m)|| ≥ k(log2 k)/2 + ℓ((log2 ℓ)/2 + 1),

8

so it is enough to show that, for 0 < ℓ < k,

k(log2 k)/2 + ℓ((log2 ℓ)/2 + 1) < (k + ℓ)(log2(k + ℓ))/2.

This is equivalent to 22ℓkkℓ
ℓ < (k + ℓ)k+ℓ,

i.e.
 2
2ℓℓ
ℓ < ( k + ℓ
k
 )k (k + ℓ)ℓ. (6)

For ﬁxed ℓ > 0, the right hand side of (6) is increasing for k ≥ ℓ, and we have
equality when k = ℓ, so the upper bound of (5) holds with strict inequality for
all k > ℓ.
For the lower bound of (5), we proceed similarly. By the bound from the
induction hypothesis, that bound follows if

k(log2 k)/2 + ℓ((log2 ℓ)/2 + 1/2) > (k + ℓ)((log2(k + ℓ))/2 − 1/2),

i.e. 22ℓ+kkkℓℓ > (k + ℓ)
k+ℓ.

Writing ℓ = rk, this is equivalent to

2k(1+2r)kk+rkrrk > ((1 + r)k)(1+r)k,

which simpliﬁes to 2
1+2rrr > (1 + r)1+r. (7)

Since 0 ≤ r < 1, we have (1 + r)
1+r < 2
1+r ≤ 2
1+2rrr, so inequality (7) does
hold, implying the lower bound in (5).

Lemma 10. For m, n ≥ 1, the inequality ||I(m)|| ≤ m(n/2 − 1) holds exactly
when m ≤ ⌊2
n/3⌋.

Proof. We proceed by induction on n. Since the assertion is trivial for n ≤ 2,
in proving the induction step, we may assume that n ≥ 3. First, if m ≥ 2
n−1

then from Lemma 9 we have ||I(m)|| > m((log2 m)/2 − 1/2) ≥ m(n/2 − 1).
If m ≤ 2n−3, then again from Lemma 9 we have ||I(m)|| ≤ m((log2 m)/2) ≤
m(n/2−1). Hence, we may assume that m = 2
n−2+m′ for some 0 < m
′ < 2
n−2,
and so ||I(m)|| = 2
n−2(n − 2)/2 + ||I(m′)|| + m′.

From this we see that ||I(m)|| ≤ m(n/2−1) if and only if ||I(m
′)|| ≤ m
′(n/2−2).
(i) there exists an integer k so that for each A ∈ A, k ≤ |uA(A) \ A| ≤ k + 1;
(ii) for each S ∈ P(n), there exists A ∈ A such that S ∈ [A, uA(A)];
(iii) ||u(A)|| is the minimal total size of an up-set with m elements in P(n). By
the induction hypothesis, this is true if and only if m′ ≤ ⌊2n−2/3⌋, which is in
turn true if and only if m ≤ ⌊2
n/3⌋.

Corollary 11. If A ⊂ P(n) is a union-closed family with |A| > 2
3 2
n, then
||A|| ≥ |A|n/2, and in particular the union-closed conjecture holds for A.

This follows from Theorem 3 and Lemma 10.

9

6 Restricted union-closed families

In this section we prove results about the minimal total size of a union-closed
family in P(n) with certain restrictions, which are motivated by the fact that
the family F(m) is not “truly” in P(n) for n > ⌈log2(m)⌉, in the sense that no
element of F(m) contains n.

Theorem 12. Let fr(n, m) be deﬁned by

fr(n, m) = min(||A||),

where the minimum is taken over all union-closed families in P(n) which contain
[n]. Then
 fr(n, m) =
 {f (m) : m > 2
n−1

f (m − 1) + n : m ≤ 2
n−1.

The extremal examples are F(m) when m > 2
n−1 and F(m − 1) ∪ {[n]} when
m ≤ 2
n−1.

We shall prove this later, after having proved a result about families satis-
fying a diﬀerent restriction, that of point-separation.
We call a family A point-separating if for all i and j in [n] there is a set A ∈ A
with |A ∩ {i, j}| = 1. In studying UC-families, we may restrict our attention to
families F in P(n) which are point-separating and for which dF (i) ≥ 1 for each
1 ≤ i ≤ n; we call such families normal. Note that if A ⊂ P(n) is a normal
union-closed family, [n] = ⋃
A∈A A is a set of A.

Theorem 13. Let fp(n, m) be deﬁned by

fp(n, m) = min(||A||),

where the minimum is taken over all normal union-closed families in P(n). Let
Fp(n, k) be given by
 Fp(n, k) = F(k) ∪ {[i] : 1 ≤ i ≤ n}.

Then for any integers m and n with n + 1 ≤ m ≤ 2n there exists k such that
|Fp(n, k)| = m, and then we have

fp(n, m) = ||Fp(n, k)||.

In fact, we shall use Theorem 13 to prove Theorem 12. To prove Theorem
13, we shall again consider applying up-compressions to our family; in the case
where A is normal we can give some additional restrictions on the process.

Lemma 14. Suppose that A is a normal union-closed family in P(n). Then
there are distinct sets A0, A1, . . . , An in A such that |rA(A0)| = 0, and for
1 ≤ i ≤ n we have rA(Ai) ≤ i − 1.
 10

Proof. Without loss of generality, we may assume that dA(i) ≤ dA(j) if i ≤ j.
Now, for 1 ≤ i ≤ n let Ai = ⋃
i /∈A∈A A. Since A is union-closed, this is a
set of A. If j > i, then dA(j) ≥ dA(i). Since A is point-separating, i and j
cannot be in precisely the same sets, and so j ∈ Ai. Hence |Ai| ≥ n − i. Also,
|uA(Ai)| ≤ n − 1, since [n] ∈ A. Thus rA(Ai) ≤ (n − 1) − (n − i) = i − 1. To
show that the Ai are distinct, if i < j ∈ [n] then j ∈ Ai but j /∈ Aj. Setting
A0 = [n], we have A0, A1, . . . An as required.

Lemma 15. Let A be a normal union-closed family in P(n), and suppose
dA(i) ≤ dA(j) for i ≤ j. Then u(A) contains all sets in P(n) of size n − 1.

Proof. As in the proof of Lemma 14, we have sets Ai for 1 ≤ i ≤ n so that
i /∈ Ai, but j ∈ Ai for all j > i. Now, after applying ui−1 . . . u1 to A to reach
Ai−1 we have [n] − i = Ai ∪ [1, i − 1] ∈ Ai−1. The remaining compressions
un . . . ui do not aﬀect this set, as [n] ∈ A, and so [n] − i ∈ u(A).

Now, analogously to Lemma 5 we can give conditions under which a union-
closed point-separating family in P(n) with m sets is extremal.

Lemma 16. Suppose that A is a normal union-closed family of m sets in P(n),
and the following hold:

(i) Let ni = |{A ∈ A : rA(A) = i}|. Then there exist k, s ≥ 0 and r > 0 such
that
 ni =
 



2 : i = 0,
1 : 1 ≤ i ≤ k − 1,
r : i = k,
s : i = k + 1.

(ii) For every S ∈ P(n), there exists A ∈ A such that S ∈ [A, uA(A)].

(iii) ||u(A)|| is the smallest possible total size of an up-set of m sets in P(n)
containing [n]
(n−1).

Then fp(n, m) = ||A||; that is, A has the smallest possible total size for a normal
union-closed family in P(n).

Proof. If A
′ is another normal union-closed family with m sets in P(n), our task
is to show that ||A
′|| ≥ ||A||. We may assume that dA′(i) ≤ dA′(j) for i ≤ j. Let
n′
i = |{A ∈ A
′ : rA′(A) = i}|. Now, applying Lemma 14 to A
′, we have that for
0 ≤ j ≤ n there are at least j + 2 sets A of A
′ with r(A) ≤ j, and so ∑j
i=0 n′
i ≥
j + 2. Also, from the second condition of the lemma together with Theorem 4,
we have that ∑

A∈A′ 2rA′ (A) ≤ ∑

A∈A 2rA(A) = 2
n. Combining these conditions,
we must have ∑

A∈A′ rA′(A) ≤ ∑

A∈A rA(A). Also, applying Lemma 15, u(A
′)
is an up-set containing [n](n−1). Hence from the third condition of the lemma

11

we have ||u(A
′)|| ≥ ||u(A)||. Combining these inequalities, we have

||A
′|| = ||u(A
′)|| − ∑

A∈A′ rA′(A)

≥ ||u(A)|| − ∑

A∈A rA(A) = ||A||,

as required.

To ﬁnish the proof of Theorem 13, we now need to show that the family
Fp(n, m) satisﬁes these conditions.

Lemma 17. For all integers m and n with n+1 ≤ m ≤ 2
n, the family Fp(n, m)
satisﬁes the conditions of Lemma 16.

Proof. For some integer k, write m = 2
k−1 + m
′ with 0 < m
′ ≤ 2k−1. So, for U
an up-set of m
′ elements in P(k − 1) which minimises ||U||, we have

Fp(n, m) = P(k − 1) ∪ {A + k : A ∈ U} ∪ {[i] : k + 1 ≤ i ≤ n},

and this is a disjoint union. Then it can be shown that the following describes
u(A):
 uA(A) =
 




[n] : A = [n]
[n] − (i + 1) : A = [i], k ≤ i ≤ n − 1
A ∪ [k + 1, n] : A ∈ {A + k : A ∈ U} \ {[k]}
A ∪ [k + 1, n] : A ∈ {U}
A ∪ [k, n] : A ∈ P(n − 1) \ U.

Hence considering rA(A) for the various sets A ∈ A we have:

rA(A) =
 




0 : A = [n]
(n − 1) − i : A = [i], k ≤ i ≤ n − 1
n − k : A ∈ {k + U} \ {[k]}
n − k : A ∈ {U}
n − k + 1 : A ∈ P(n − 1) \ U,

and so
 ni =
 



2 : i = 0
1 : 1 ≤ i < n − k
2|U| : i = n − k
2
n−1 − |U| : i = n − k + 1
0 : i > n − k + 1.

This sequence satisﬁes Condition 1 of Lemma 16. For Condition 2, let S ∈ P(n);
we wish to ﬁnd A ∈ A with S ∈ [A, uA(A)]. We break this down into three
cases, depending on the intersection of S with [1, k]. Firstly, if [1, k] ⊂ S then

12

let i be minimal with i /∈ S. Then S ∈ [[i], uA([i])], as required. Secondly, if
k /∈ S, then write S = S1 ∪ S2, with S1 ⊂ [1, k − 1] and S2 ⊂ [k + 1, n]. Then
uA(S1) = S1 ∪ [k + 1, n], and so S ∈ [S1, uA(S1)]. Finally, if [1, k] ̸⊂ S and
k ∈ S, write S = S1 ∪ {k} ∪ S2, with S1 ⊂ [1, k − 1] and S2 ⊂ [k + 1, n]. If
S1 ∈ U, then uA(S1 + k) = (S1 + k) ∪ [k + 1, n], and S ∈ [S1 + k, uA(S1 + k)].
If S1 /∈ U, then u(S1) = S1 ∪ [k, n], and S ∈ [S1, uA(S1)].
For Condition 3, we have

u(A) = {A ∪ [k, n] : A ∈ P(n − 1)} ∪ {A ∪ [k + 1, n] : A ∈ U} ∪ [n](n−1).

The ﬁrst two terms in the union form an up-set in P(n) of m
′ sets of minimal
total size. It is an easy consequence of the Kruskal-Katona Theorem that the
union of this set with [n]
(n−1) gives an up-set of minimal total size containing
[n]
(n−1).

Putting together Lemmas 16 and 17, we have proved that every family
Fp(n, k) is extremal – that is, if |Fp(n, k)| = m then ||Fp(n, k)|| = fp(n, m).
To complete the proof of Theorem 13, it remains only to show that for n + 1 ≤
m ≤ 2
n there is some choice of k with |Fp(n, k)| = m. However, this is imme-
diate, since |Fp(n, k)| − |Fp(n, k − 1)| ≤ 1 for 1 ≤ k ≤ 2n, |Fp(n, 0)| = n, and
|Fp(n, 2n)| = 2
n.

6.1 Proof of Theorem 12

We now use Theorem 13 to prove Theorem 12. Let A be a union-closed family
in P(n), containing [n]. If |A| > 2n−1, then ||A|| ≥ f (m), so we are done. If
|A| ≤ 2n−1, we form an equivalence relation on [n] by setting

i ≡ j ⇐⇒ {A ∈ A : i ∈ A} = {A ∈ A : j ∈ A}.

Let the equivalence classes of this relation be C1, . . . Ck for some k ≤ n. Deﬁne
a family A
′ in P(k) by
 A ∈ A
′ ⇐⇒ ⋃

i∈A Ci ∈ A.

A
′ is a family in P(k) of m sets, and it is point-separating. We now split into
two cases. If m ≤ 2k−1 then for some m
′ < 2k−1 we have |Fp(k, m′)| = m, and
then ||A
′|| ≥ ||Fp(k, m′)|| ≥ f (m − 1) + k.

However, since every element of [n] appears in a set of A, ||A|| ≥ ||A′||+(n−k) ≥
f (m − 1) + n, as required.
On the other hand, if m > 2k−1 we write m = 2
k−1+m
′. Then every element
of [k] appears at least m
′ times in A
′, and so every element of [n] appears at
least m′ times in A. Hence we have

||A|| ≥ ||A′|| + (n − k)m
′

≥ f (m) + (n − k)m′.

13

Also, let F(m) \ F(m − 1) = {S}. Then since m = 2
k−1 + m
′, the set S is in
{k + A : A ∈ U}, for U an up-set of P(k − 1) with |U| = m
′. Hence we have
|S| ≥ k − log2(m
′), and so

||A|| ≥ f (m) + (n − k)m
′

= f (m − 1) + |S| + (n − k)m
′

≥ f (m − 1) + k − log2(m
′) + (n − k)m
′

= f (m − 1) + n + (n − k)(m′ − 1) − log2(m
′)

≥ f (m − 1) + n.

The last line follows since (n − k)(m′ − 1) − log2(m
′) ≥ 0 for all m′ ≥ 1 and
(n − k) ≥ 1. This completes the proof of Theorem 12.
Theorem 12 is enough to verify a conjecture of W´ojcik [26], which states
that the smallest average size for a union-closed family containing an n-set is
achieved by the family P(k) ∪ {[n]}, for either k = ⌊log2(n)⌋ or k = ⌈log2(n)⌉.
Given Theorem 12, to prove this result one only needs to minimise fr(n, m)/m
over m. To do so is a simple but tedious calculation, which we shall omit.

7 Union-closed and rooted families

We say a family B ⊂ P(n) rooted if for each B ∈ B there is an i ∈ B such
that {B′ : i ∈ B′ ⊂ B, |B′| = |B| − 1} ⊂ B. Also, we say that B ⊂ P(n) is
simply rooted if for each ∅ ̸= B ∈ B we have [{i}, B] ⊂ B for some i ∈ B. These
deﬁnitions is are motivated by the following simple observation.

Lemma 18. For a family A ⊂ P(n), A is union-closed if and only if B =
P(n) \ A is simply rooted.

Proof. The family A is union-closed if and only if ⋃
B′⊂B, B∈A B′ ̸= B whenever
B ∈ B. This is true precisely when for each B ∈ B there is an i ∈ B with
[{i}, B] ⊂ B.

Also, from the proof of Theorem 3 we can read out a slight strengthening
for union-closed families A with |A| ≥ 2
n−1.

Theorem 19. Let A ⊂ P(n), and B = P(n) \ A with |B| = m. Suppose the
largest down-set contained in B is D. Then ||A|| ≥ ||P(n)|| − ||I(m)|| − m + |D|.

Proof. Here, with u deﬁned as in the proof of Theorem 3, we have ||u(A)|| ≥
||P(n)|| − ||I(m)||, since u(A) is an up-set on 2n − m sets. Also, for every A ∈ A
we have [A, uA(A)] \ A ⊂ B \ D. Hence ∑A∈A |uA(A) \ A| ≤ |P(n) \ (A ∪ D)| =
m − |D|. Combining these inequalities,

||A|| = ||u(A)|| − ∑

A∈A |uA(A) \ A|

≥ ||P(n)|| − ||I(m)|| − m + |D|,

14

as required.

We use this to prove a slightly better bound on the total size of a hypothetical
counterexample to the union-closed conjecture. A corollary of Theorem 3 is the
following.

Corollary 20. Suppose that A ⊂ P(n) is a union-closed family which is a
counterexample to the union-closed conjecture; that is dA(i) < |A|/2 for each
i ∈ [n]. Let B = P(n) \ A, and m = |B|. Then ||I(m)|| > m(n/2 − 1).

This follows because we must have mn/2 < ||B|| ≤ ||M(n, m)|| ≤ ||I(m)|| +
m. In fact, we can prove the following slight strengthening of Corollary 20.

Lemma 21. Suppose that A ⊂ P(n) is a union-closed family which is a coun-
terexample to the union-closed conjecture. Let B = P(n) \ A, and m = |B|.
Then ||I(m)|| > m(n/2 − 1 + 1/n).

Proof. For each i ∈ [n], let Bi = {B ∈ B : [i, B] ⊂ B}, mi,+ = |{B ∈ B : i ∈ B}|,
and mi,− = m − mi,+. Also, let ||B|| = m(n/2 + r); since A is a counterexample
to the union-closed conjecture, r > 0. We relate r and mi,+ by

n∑

i=1(mi,+ − mi,−) =
 n∑

i=1(2mi,+ − m)

= 2||B|| − nm

= 2mr.

Also, since by Lemma 18 the family B is simply rooted, ∑n
i=1 |Bi| ≥ m. So we
have n∑

i=1 |Bi| − (mi,+ − mi,−) ≥ m(1 − 2r).

In particular, there is some j with |Bj| − mj,+ + mj,− ≥ m(1 − 2r)/n; without
loss of generality, we may assume j = n. Now, we deﬁne two families of sets

B+
n = {B ⊂ P(n − 1) : B + n ∈ B}

B−
n = {B ⊂ P(n − 1) : B ∈ B}

Then, setting D+ to be the largest down-set contained in B+
n , we have {B − n :
B ∈ Bn} ⊂ D+, and so |D+| ≥ |Bn| ≥ mn,+ − mn,− + m(1 − 2r)/n. This gives
us
 ||B|| = ||B+
n || + ||B−
n || + mn,+
≤ ||I(mn,+)|| + mn,+ − |D+| + ||I(mn,−)|| + mn,− + mn,+
≤ ||I(mn,+)|| + ||I(mn,−)|| + mn,− − m(1 − 2r)/n + m

≤ ||I(m)|| − m(1 − 2r)/n + m.

Where the last line follows from Lemma 2. Hence we have ||I(m)|| ≥ (n/2 +
r)m + m(1 − 2r)/n − m > m(n/2 − 1 + 1/n), as required.

15

Theorem 21 provides only a slight strengthening of our bound on the size of
a counterexample to the union-closed conjecture – approximately, it improves
|B| > 2
n/3 to |B| > 2n(1/3 + 2/9n) for P(n) \ B such a counterexample.

8 Conjectures on rooted families

By Theorem 3 and Lemma 18, if B is a simply rooted family in P(n) then

||B|| ≤ ||M(n, m)|| ≤ ||I(m)|| + m. (8)

We conjecture two strengthenings of this result. Firstly, we conjecture that (8)
holds for a family which has only the weaker property of being rooted. Also,
we note that the families M(n, m) for which equality is achieved in (8) are very
asymmetric; for m ≤ 2
n−1 every set in B contains n. This leads us to conjecture
the following strengthening of (8) for simply rooted or rooted families:

Conjecture 22. Suppose B is a rooted family in P(n). Then

||B|| ≤ ||I(|B|)|| + max
i∈[n] dB(i).

We note that the truth of this conjecture for simply rooted families would
show that if P(n)\B were a counterexample to the union-closed conjecture, then
we would have ||I(|B|)|| ≥ |B|(n − 1)/2, and so |B| ≥ (2/3)2
n. In particular,
Conjecture 22 implies that the union-closed conjecture holds for every family
A ⊂ P(n) with |A| > 2
n/3.

If [{i}, B] ⊂ B, we say that B is simply rooted at i. If all sets in B are simply
rooted at the same i, then Conjecture 22 reduces to a weaker form of Theorem
3. We can also prove Conjecture 22 in the case where each set B ∈ B is simply
rooted at one of two elements i and j in [n]. Indeed, in this case we let Bi, Bj and
Bij be the families {B ∈ B : j /∈ B}, {B ∈ B : i /∈ B} and {B ∈ B : {i, j} ⊂ B},
with sizes mi, mj and mij respectively. Since {B −i : B ∈ Bi}, {B −j : B ∈ Bj}
and {B \ {i, j} : B ∈ Bij} are all down-sets, we have

||B|| ≤ ||I(mi)|| + ||I(mj)|| + ||I(mij)|| + mi + mj + 2mij
≤ ||I(mi + mj)|| + max(mi, mj) + ||I(mij)|| + 2mij
≤ ||I(m)|| + max(mi, mj) + mij.

The last inequality uses the fact that mij ≤ mi + mj; indeed, we can re-
move either i or j from each set in Bij, while remaining in B. This is exactly
the statement of Conjecture 22 in this special case, as max(mi, mj) + mij =
max(dB(i), dB(j)).

References

[1] B. Bollob´as, Random Graphs, Second edition, Cambridge Studies in Ad-
vanced Mathematics 73, Cambridge University Press, Cambridge, 2001.
xviii+498 pp.
 16

[2] I. Boˇsnjak, P. Markovi´c, The 11-element case of Frankl’s conjecture, Elec-
tron. J. Combin. 15 (2008), Research Paper 88.

[3] G. Cz´edli, On averaging Frankl’s conjecture for large union-closed-sets, J.
Combin. Theory Ser. A 116 (2009), 724–729.

[4] G. Cz´edli, M. Mar´oti and E.T. Schmidt, On the scope of averaging for
Frankl’s conjecture, Order 26 (2009), 31–48.

[5] D. Duﬀus, in Graphs and Order (I. Rival, Ed.), Dordrecht/Boston, Reidel
(1985), p.525.

[6] M.H. El-Zahar, A graph-theoretic version of the union-closed sets conjec-
ture, J. Graph Theory 26 (1997), 155–163.

[7] W.D. Gao and H.Q. Yu, Note on the union-closed sets conjecture, Ars
Combin. 49 (1998), 280–288.

[8] R.T. Johnson and T.P. Vaughan, On union-closed families I, J. Combin.
Theory Ser. A 84 (1998), 242–249.

[9] G.O.H. Katona, A theorem on ﬁnite sets, in Theory of Graphs (P. Erd˝os
and G.O.H. Katona, Eds.), Akad´emiai Kiad´o, Budapest, 1968, pp. 187–207.

[10] J.B. Kruskal, The number of simplices in a complex, in Mathematical Opti-
mization Techniques, Univ. of California Press, Berkeley, 1963, pp. 251–278.

[11] L. Lov´asz, Combinatorial Problems and Exercises, Corrected reprint of the
1993 second edition, AMS Chelsea Publishing, Providence, RI, 2007. 642
pp.

[12] G. Lo Faro, A note on the union-closed sets conjecture, J. Austral. Math.
Soc. Ser. A 57 (1994), 230–236.

[13] G. Lo Faro, Union-closed sets conjecture: improved bounds, J. Combin.
Math. Combin. Comput. 16 (1994), 97–102.

[14] P. Markovi´c, An attempt at Frankl’s conjecture, Publ. Inst. Math. 81(95)
(2007), 29–43.

[15] R. Morris, FC-families and improved bounds for Frankl’s conjecture, Eu-
ropean J. Combin. 27 (2006), 269–282.

[16] R.M. Norton and D.G. Sarvate, A note of the union-closed sets conjecture,
J. Austral. Math. Soc. Ser. A 55 (1993), 411–413.

[17] B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992),
253–268.

[18] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12
(2003), 89–93,
 17

[19] J.-C. Renaud, Is the union-closed sets conjecture the best possible? J.
Austral. Math. Soc. Ser. A 51 (1991), 276–283.

[20] I. Roberts and J. Simpson, A note on the union-closed sets conjecture,
Australas. J. Combin. 47 (2010), 265–267,

[21] D.G. Sarvate and J.-C. Renaud, On the union-closed sets conjecture, Ars
Combin. 27 (1989), 149–153.

[22] D.G. Sarvate and J.-C. Renaud, Improved bounds for the union-closed sets
conjecture Ars Combin. 29 (1990), 181–185.

[23] T.P. Vaughan, Families implying the Frankl conjecture, European J. Com-
bin. 23 (2002), 851–860.

[24] T.P. Vaughan, A note on the union-closed sets conjecture, J. Combin.
Math. Combin. Comput. 45 (2003), 95–108.

[25] T.P. Vaughan, Three-sets in union-closed families, J. Combin. Math. Com-
bin. Comput. 49 (2004), 73–84.

[26] P. W´ojcik, Union-closed families of sets, Discrete Math. 199 (1999), 173–
182.
 18
