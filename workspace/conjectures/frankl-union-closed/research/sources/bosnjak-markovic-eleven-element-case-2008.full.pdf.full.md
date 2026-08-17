<!-- source: https://people.dmi.uns.ac.rs/~markovicp/papers/2008-Frankl11.pdf | converted from PDF -->

The 11-element case of Frankl’s conjecture

Ivica Boˇsnjak and Petar Markovi´c ∗

Department of Mathematics and Informatics
University of Novi Sad, Serbia
ivb@im.ns.ac.yu
pera@im.ns.ac.yu

Submitted: Jan 24, 2007; Accepted: Jun 27, 2008; Published: Jul 6, 2008
Mathematics Subject Classiﬁcations: primary 05D05, secondary 05A05

Abstract

In 1979, P. Frankl conjectured that in a ﬁnite union-closed family F of ﬁnite
sets, F ̸= {∅}, there has to be an element that belongs to at least half of the sets in
F. We prove this when | ⋃ F| ≤ 11.

1 Introduction

Frankl’s conjecture [9], sometimes also called the union-closed sets conjecture is one of the
most celebrated open problems in combinatorics. In [10] it is referred to as ‘diabolical’,
presumably since it has an elementary, even trivial statement, but seems to be quite
diﬃcult. In its original statement, the conjecture is that in a ﬁnite union-closed family
F of ﬁnite sets, F ̸= {∅} there has to be an element that belongs to at least half of the
sets in F . Several equivalents have been found, in various areas of mathematics, the most
popular of which is probably the lattice-theoretic one (see [10], Chapter 3, Problem 39a).
Recently there have been quite a few new partial results concerning the original version
of the problem, (see for instance [2], [3], [6], [7], [11, 12, 13]). Many of these papers are
using the idea introduced ﬁrst in [8], Theorem 1. This is a way for rapid veriﬁcation of
the conjecture for a large class of union-closed families using a weight function. We use a
similar approach, introduced in [6]. The main diﬀerence is that Theorem 1 of [8] gives a
necessary and suﬃcient condition for a subfamily F ′ to force that an element of ⋃ F ′ is
in at least half of the sets of F for any F ⊇ F ′ (such F ′ are called F C families in [11]),
while our (easier) Lemma 2.1 gives a necessary and suﬃcient condition for F to satisfy
Frankl’s Conjecture. We are able to use our approach to prove that any counterexample
F to Frankl’s Conjecture must satisfy | ⋃ F | ≥ 12.

∗The second author was supported by the grant no. 144011G of the Ministry of Science and Environ-
ment of Serbia.

the electronic journal of combinatorics 15 (2008), #R88 1

In Section 2 we prove lemmas we will need later on, and which are true in any union-
closed family. Many of these are proved elsewhere, and some were left to the reader
to verify in the papers where they appeared. Our goal was to have every step in our
proof veriﬁable, so we (re-)proved the lemmas of the second kind. Section 3 consists of
lemmas in the setting | ⋃ F | = 11, culminating with Theorem 3.1, which claims that all
union-closed families F with | ⋃ F | = 11 satisfy Frankl’s conjecture. Clearly, if there
was a counterexample with | ⋃ F| < 11, we could easily construct a counterexample with
| ⋃ F| = 11 by ‘copying’ one element into an appropriate number of ‘copies’ which appear
in sets whenever the ‘original’ one does. Therefore, we prove that all union-closed families
with | ⋃ F | ≤ 11 satisfy Frankl’s conjecture.

2 Initial Results

Throughout this paper F will denote a ﬁnite family of ﬁnite sets closed under unions and
X will denote the union of F . We will call F Frankl’s if X = ⋃ F contains an element
which is in at least one half of the sets from F.

Deﬁnition 2.1. We call any function w : X → {x ∈ R|x ≥ 0}, such that w(a) > 0 for
some a ∈ X, a weight function. The weight w(S), for S ⊆ X is equal to ∑

x∈S w(x). The

number 0.5w(X) will be called the target weight and denoted by t(w).

Lemma 2.1. F is Frankl’s if and only if there is a weight function w assigned to elements
of X = ⋃ F such that ∑

S∈F w(S) ≥ t(w)|F|.

Proof. (=⇒) Let a be an element of at least half of the sets in F. Take the weight function
w such that w(a) = 1 and w(x) = 0 for x ̸= a. Then t(w) = 0.5, and the inequality is
obviously satisﬁed.
(⇐=) Assume that F is not Frankl’s. Let na(F ) be the number of occurrences of the
element a in sets from F . We take an arbitrary weight function w. Then
∑

S∈F w(S) = ∑

S∈F
 ∑

a∈S w(a) = ∑

a∈X w(a)na(F) <

∑

a∈X w(a) |F|
2 = t(w)|F|.

Lemma 2.2. If F contains a one-element set, or a two-element set, then it is Frankl’s.

Proof. Easy exercise for the reader, and also found in several of the papers in the bibli-
ography.

the electronic journal of combinatorics 15 (2008), #R88 2

Deﬁnition 2.2. For S, K ⊆ X, S ∩ K = ∅ we call any interval in the Boolean lattice
P(X) of the form [K, K ∪ S] an S-hypercube. We can partition a hypercube into levels,
where a set is on level k if and only if k is the cardinality of its intersection with S. We
denote level k of a hypercube C by Ck. Also, for x ∈ S we deﬁne the auxiliary hypercubes
Cx and C¬x to be the S \ {x}-hypercubes with bottom sets K ∪ {x} and K, respectively.
Let F be a union-closed family of sets and w a weight function. The deﬁcit of a set
L ⊆ X with w(L) < t(w) is d(L) = t(w) − w(L). The surplus of a set L ⊆ X with
w(L) > t(w) is s(L) = w(L) − t(w). Let C be an S-hypercube. The deﬁcit of C is deﬁned
to be d(C) = ∑

L∈C∩F
w(L)<t(w) d(L), while s(C) = ∑

L∈C∩F
w(L)>t(w) s(L) is the surplus of C. Analogously we

deﬁne d(Ck) and s(Ck).

It is an obvious consequence of Lemma 2.1 that if for some weight function w the
sum of surpluses of the sets in F which have weights greater than t(w) is greater than or
equal to the sum of deﬁcits of the sets in F which have weights less than t(w), then F is
Frankl’s. In particular, if for every S-hypercube C, s(C) ≥ d(C), then F is Frankl’s. In
all the S-hypercubes we will consider, we will have S ∈ F . Hence, if the hypercube has
a nonempty intersection with F , then the top set of that hypercube is in F .
Let F be a union-closed family of sets and C an S-hypercube for some S ⊆ X. By
pk(C) we will denote the number of sets on level k in the hypercube C which belong to F .
When C is obvious we will just write pk.

Lemma 2.3. Let F be a union-closed family of sets and C an S-hypercube for some
S ⊆ X, |S| = m. If k < l < m, suppose that for every set from level l of C which is in
F, at most u of its subsets from level k could be in F , and for every set from level l of C
which is not in F, at most v of its subsets from level k could be in F . Then
(m − k
l − k
 )pk ≤ upl + v((m
l
 ) − pl). (1)

Proof. Consider a bipartite graph G whose set of vertices is A ∪ B, where A contains all
l-level sets of C, and B contains those k-level sets of C which are in F. Every vertex from
A is connected by an edge to all its subsets from B. Since the degree of every vertex from
B is (
m−k
l−k ), this graph has (
m−k
l−k )pk edges. On the other hand, for all sets from A which
are not in F, their degree is not more than v, and the degree of those A-sets which are in
F is not greater than u. From these facts we conclude
(m − k
l − k
 )pk ≤ upl + v((m
l
 ) − pl).

In the special case when l = k + 1 and the number of level k-subsets in F is not
limited, we have u = k + 1 and v = 1, so

(m − k)pk ≤ kpk+1 + ( m
k + 1
). (2)

Inequality (2) is equivalent to Lemma 3.4. (b) from [11].

the electronic journal of combinatorics 15 (2008), #R88 3

Proposition 2.1. Assume that F contains three diﬀerent three-element sets which are
all subsets of the same four-element set. Then F is Frankl’s.

Proof. This was proved in [8], Corollary 4.

Proposition 2.2. Suppose that F contains three three-element sets which all contain the
same two elements. Then F is Frankl’s.

Proof. See [12], Section 3 and [6], Proposition 2.2.

The following proposition can be found in [7], with the sketch of a proof.

Proposition 2.3. [7] Let {a, b, c, d, e} ⊆ X, {a, b, c}, {a, b, d}, {c, d, e} ∈ F . Then F is
Frankl’s.

Proof. Assume that F is not Frankl’s. As suggested in [7], we choose the weight function
w such that w(a) = w(b) = w(c) = w(d) = 2, w(e) = 1, and w(x) = 0 for all other
x ∈ X. Consider an arbitrary {a, b, c, d, e}-hypercube C with bottom set K. Let us
consider C1 ∪ C4. Here K ∪ {a} ∈ F implies K ∪ {a, c, d, e} ∈ F, K ∪ {b} ∈ F implies
K ∪ {b, c, d, e} ∈ F , K ∪ {e} ∈ F implies K ∪ {a, b, c, e} ∈ F and K ∪ {a, b, d, e} ∈ F. This
means that d(C1) > s(C4) only if K ∪{c}, K ∪{d} ∈ F (and, therefore K ∪{a, b, c, d} ∈ F ),
K ∪ {a, b, c, e}, K ∪ {a, b, d, e} /∈ F , and in this case d(C1) = s(C4) + 1.5. On levels 2 and
3 we have the following situation: If p1(Ce) = 3 then p2(Ce) ≥ 3 and if p1(Ce) = 4
then p2(Ce) = 6. This means d(C e
1) ≤ s(Ce
2) + 3. Also, if K ∈ F, since K ∪ {a, b, c},
K ∪ {a, b, d} ∈ F, and p2(C¬e) ≥ 4 implies p3(C¬e) ≥ 3, we have d(C ¬e
2 ) ≤ s(C¬e
3 ) − 1.5.
On the other hand, if K /∈ F, then d(C ¬e
2 ) ≤ s(C¬e
3 ) + 0.5, the equality being achieved
only when K ∪ {c, d} is the only set from C ¬e
2 in F, and p3(C¬e) = 0. The levels 0 and 5
of C produce a surplus of 4.5 when K /∈ F and cancel each other when K ∈ F.
The analysis from above guarantees that when K /∈ F , then s(C) < d(C) only if
d(C1) = s(C4) + 1.5 and d(C¬e
2 ) = s(C¬e
3 ) + 0.5. The ﬁrst requires K ∪ {c} ∈ F , and the
second requires p3(C¬e) = 0. These two requirements are incompatible in any union-closed
system F which contains {a, b, c}. So we may assume K ∈ F . We will discuss three cases.

1. K ∪ {a, b, c, e}, K ∪ {a, b, d, e} /∈ F. This means p1(Ce) = 0 and we have d(C1) ≤
s(C4) + 1.5, d(Ce
1) ≤ s(Ce
2) − 0.5 and d(C¬e
2 ) ≤ s(C¬e
3 ) − 1.5. Finally, this gives
d(C) ≤ s(C) − 0.5.

2. K ∪ {a, b, c, e} ∈ F , K ∪ {a, b, d, e} /∈ F . This means p1(Ce) ≤ 1 and we have
d(C1) ≤ s(C4) − 1, d(Ce
1) ≤ s(Ce
2) + 1 and d(C¬e
2 ) ≤ s(C¬e
3 ) − 1.5. Finally, this gives
d(C) ≤ s(C) − 1.5.

3. K ∪ {a, b, c, e}, K ∪ {a, b, d, e} ∈ F . If s(C) < d(C), then K ∪ {c}, K ∪ {d}, K ∪ {e}
must be in F . Now we analyze the sets in C in a diﬀerent way. K ∪ {c}, K ∪ {d} and
K ∪ {e} cancel out with K ∪ {a, b, c, e}, K ∪ {a, b, d, e} and K ∪ {a, b, c, d}. K ∪ {c, e}
and K ∪ {d, e} cancel out with K ∪ {a, b, c} and K ∪ {a, b, d}. As K ∪ {e} ∈ F ,
d(C¬e
2 ) ≤ s(Ce
2). Since K ∪ {a} ∈ F implies K ∪ {a, c, d}, K ∪ {a, c, d, e} ∈ F , and

the electronic journal of combinatorics 15 (2008), #R88 4

K ∪ {a, e} ∈ F implies K ∪ {a, c, d, e} ∈ F, sets K ∪ {a} and K ∪ {a, e} cancel out
with K ∪ {a, c, d} and K ∪ {a, c, d, e}. Similarly, K ∪ {b} and K ∪ {b, e} cancel out
with K ∪ {b, c, d} and K ∪ {b, c, d, e}. This gives d(C) ≤ s(C).

Theorem 2.1. [7] Assume that F contains three diﬀerent three-element sets which are
all subsets of the same ﬁve-element set. Then F is Frankl’s.

Proof. There are four possible cases:

1. F contains three three-element subsets of a four-element set. This case is considered
in Proposition 2.1.

2. F contains three three-element sets which all contain the same two elements. The
statement holds by Proposition 2.2.

3. F contains three three-element sets whose union is a ﬁve-element set and whose
intersection is a one-element set. This case is solved in [12].

4. The intersection of the three three-element sets is ∅. This case is investigated in
Proposition 2.3.

3 Results for |X| = 11

All the proofs in this Section follow a similar pattern: we assume that certain sets are in
F and F is not Frankl’s. Therefore, F contains no one- or two-element sets, and no case
considered in the previous Lemmas occurs. Moreover, when considering the situation in
a certain hypercube C, unless otherwise stated, we are trying to prove that s(C) ≥ d(C)
and assuming the opposite.

Lemma 3.1. If |X| = 11 and F contains two three-element sets with a two-element
intersection, then F is Frankl’s.

Proof. Let {a, b, c} and {a, b, d} be the two sets in F. We consider the weight function
w, with w(a) = w(b) = 8, w(c) = w(d) = 6 and w(x) = 1 for x ∈ X − {a, b, c, d}. We
have t(w) = 17.5. Let C be an {a, b, c, d}-hypercube with bottom set K. We consider the
cases:

1. |K| = 0. Only four sets in this hypercube are in F (according to Proposition 2.1),
so s(C) = d(C) + 2.

2. |K| = 1. In such hypercubes p0 = p1 = 0, so the only sets which might have a deﬁcit
are on level 2. The surplus of the top set K ∪ {a, b, c, d} is 11.5, and d(C2) ≥ 12
implies p2 ≥ 4. This means that p3 ≥ 3, and s(C) ≥ 24 > d(C).

3. |K| = 2. Here d(C2) ≤ 9.5. If we consider the number of level 1 sets, we have
subcases:

the electronic journal of combinatorics 15 (2008), #R88 5

(a) p1 = 0. Then s(C) ≥ 12.5 > 9.5 ≥ d(C).

(b) p1=1. That level 1 set implies that at least one of the sets K ∪ {a, b, c} and
K ∪ {a, b, d} is in F (each has the surplus 6.5). Therefore, as the deﬁcit of a
level 1 set is at most 9.5, s(C) ≥ 19 ≥ d(C).

(c) p1 = 2. This implies that both of the sets K ∪ {a, b, c} and K ∪ {a, b, d} are in
F , so s(C) ≥ 25.5. Here d(C1) ≤ 19, and this means that s(C) ≥ d(C) provided
that d(C2) ≤ 6.5. But, d(C2) > 6.5 implies p2 ≥ 4 which implies p3 ≥ 3, so
s(C) ≥ 30 > 28.5 = 19 + 9.5 ≥ d(C1) + d(C2) = d(C).

(d) p1 ≥ 3. Then these level 1 sets form three three-element sets with a common
two-element intersection. Then F is Frankl’s by Proposition 2.2.

4. |K| = 3. If K /∈ F, the surplus of the top set is 13.5. The sets producing a deﬁcit
are on level 1 (two with deﬁcit 8.5 and two with deﬁcit 6.5) and on level 2 (four with
deﬁcit 0.5 and one with deﬁcit 2.5). Thus, p1 ≥ 2, which implies that K ∪ {a, b, c}
and K ∪ {a, b, d} are both in F . So, s(C) ≥ 28.5, and therefore p1 = 4. But then,
C \ {K} ⊆ F, so s(C) = 41 > 34.5 = d(C).

If K ∈ F we would like to prove that d(C) ≤ s(C) + 8. The equality is achieved
when C ⊆ F , which happens exactly when p1 = 4. We consider the remaining
cases for p1. The deﬁcit of K is 14.5, while d(C2) ≤ 4.5. On the other hand,
s(C4) + s(K ∪ {a, b, c}) + s(K ∪ {a, b, d}) = 28.5, so s(C) + 8 ≥ 36.5. This means that
d(C1) ≥ 18, so p1 = 3. We have, up to a trivial equivalence, two subcases: Either
K ∪ {a} /∈ F , or K ∪ {c} /∈ F. In the ﬁrst subcase, p3 ≥ 3 and s(C) + 8 ≥ 42.
Since d(C0) + d(C1) = 38, we need d(C2) = 4.5, so p2 ≥ 5. But, this would imply
p3 = 4 and s(C) + 8 ≥ 47.5 > d(C). In the second subcase, we are guaranteed
that K ∪ {a, b} ∈ F, so s(C) + 8 ≥ 38. Also, if K ∪ {c, d} ∈ F, then p3 = 4, and
the desired inequality trivially holds. The remaining case is when d(C2) ≤ 2, so
d(C) ≤ 38 ≤ s(C) + 8.

5. |K| = 4. In this case and all others when |K| ≥ 4 we only need to consider the case
K ∈ F (so K, K ∪ {a, b, c}, K ∪ {a, b, d}, K ∪ {a, b, c, d} ∈ F ), as otherwise we just
imitate the proof for |K| = 3, and the numbers work even better. We have that
s(C) ≥ 31.5 and d(C) ≥ 13.5. Therefore, d(C1) + d(C2) > 18. Hence, p1 ≥ 3 and this
means that either K ∪ {a, b} ∈ F , or p3 ≥ 3. So, we now have s(C) ≥ 34 and either
p1 = 4 (in which case C ⊆ F and the inequality s(C) ≥ d(C) holds), or the only set
with deﬁcit which is not in F is one of the sets K ∪ {a}, K ∪ {b}. In the second
case, we are forced to have p3 ≥ 3 and s(C) > 35.5 = d(C).

6. When |K| = 5, K ∈ F, we will prove that s(C) ≥ d(C) + 8.5. We have s(C) ≥ 34.5
and d(C) + 8.5 ≥ 21. Again, the only sets with a deﬁcit are the level 1 sets and
K ∪ {c, d}, and their weights guarantee that p1 ≥ 3 (when p1 = 2 only s(C) =
d(C) + 8.5 is reachable). p1 ≥ 3 means that p2 ≥ 3, and s(C2) ≥ 3, so s(C) ≥ 37.5.
Therefore, K ∪ {c}, K ∪ {d} ∈ F . In this case, we are forced to have p3 ≥ 3 and
s(C) ≥ 46 > 43.5 ≥ d(C) + 8.5.

the electronic journal of combinatorics 15 (2008), #R88 6

7. 6 ≤ |K| ≤ 7 and K ∈ F are dealt with analogously to the case |K| = 5, K ∈ F. In
both situations we obtain that the ‘worst’ case is when

C ∩ F = {K, K ∪ {c}, K ∪ {d}, K ∪ {c, d},
K ∪ {a, b, c}, K ∪ {a, b, d}, K ∪ {a, b, c, d}}.

In case |K| = 6 this implies that s(C) ≥ d(C) + 15.5 and in the case |K| = 7 this
implies that s(C) ≥ d(C) + 22.5.

8. |K| = 7 and K /∈ F . We know that the top set is in F, and if no other set is in F, we
have s(C) = d(C)+17.5. If p1 ≤ 2, then p1 ≤ p3, and therefore d(C) = d(C1) ≤ s(C3).
This means that we always have s(C) ≥ d(C) + 17.5.

We have proved that the top and bottom hypercube together have the surplus by at least
19.5 greater than the deﬁcit. Thus, there are at least 3 of the ‘bad’ hypercubes with
|K| = 3, K ∈ F , in which s(C) ≥ d(C) − 8. Consider the family of bottom sets of these
hypercubes G ⊆ F . According to Theorem 2.1, ⋃ G is either a 6-set or a 7-set. If ⋃ G is
a 6-set, then there are two of the bottom sets whose union is a 5-set. Therefore we have
a hypercube with |K| = 6 for which s(C) ≥ d(C) + 15.5, and a hypercube with |K| = 5
for which s(C) ≥ d(C) + 8.5. The total surplus from the four ‘good’ hypercubes (the top
one, the bottom one and the two we just established) is by at least 43.5 greater than the
deﬁcit. If ⋃ G is a 7-set, then the diﬀerence between the total surplus and the total deﬁcit
of ‘good’ hypercubes is greater than 41.5 (we have that K ∈ F in the top hypercube, and
also in at least two other ones with |K| ≥ 5).
This means that |G| ≥ 6. Also, since no 5-set contains more than two 3-sets in F, we
get that any 6-set can contain at most four 3-sets in F . We now know that the union of
any six 3-sets in G is X − {a, b, c, d}, and the surplus of the top and bottom hypercube
must be by at least 24.5 greater than the deﬁcit. An easy pigeon-hole argument shows
that there must be at least four elements in X − {a, b, c, d} which are ‘covered’ by at most
three out of any six 3-sets in G, so the union of the remaining three (or more) must be a
6-set. This 6-set is in F, so we get four hypercubes with |K| = 6 and K ∈ F for which
s(C) ≥ d(C) + 15.5. The total surplus of these four hypercubes, and the top and the
bottom one, is by at least 86.5 greater than its total deﬁcit. This means that |G| ≥ 11.
But Theorem 2.1 and our inequality (1) imply |G| ≤ 7.

Lemma 3.2. If |X| = 11 and F contains three four-element subsets of a ﬁve-element set,
then F is Frankl’s.

Proof. We suppose F is not Frankl’s, so we may assume that F contains no one- or two-
element sets. Let {a, b, c, d}, {a, b, c, e}, {a, b, d, e} ∈ F. We consider the weight function
w, with w(a) = w(b) = w(c) = w(d) = w(e) = 4, and w(x) = 1 for x ∈ X − {a, b, c, d, e}.
Then t(w) = 13. Let C be an {a, b, c, d, e}-hypercube with bottom set K. We consider
several cases, depending on |K|:

the electronic journal of combinatorics 15 (2008), #R88 7

1. |K| = 0. We know that d(∅) = 13 and according to Theorem 2.1, p3 ≤ 2, hence
d(C) ≤ 15. On the other hand, s(C) = s(C4) + s(C5) ≥ 16.

2. |K| = 1. In such hypercubes the top set has the surplus 8, d(C) = d(C2), but
according to Lemma 3.1, p2 ≤ 2, so d(C) ≤ 8.

3. |K| = 2. According to Lemma 3.1, p1 ≤ 1, so d(C1) ≤ 7, while the surplus of the top
set is 9. Also, d(C) = d(C1) + d(C2), d(C2) = 3p2, and s(C4) = 5p4. The inequality
2p4 ≥ p2 follows by an easy case analysis. If p2 ≤ 5, then d(C2) − s(C4) ≤ 2 which
gives s(C) ≥ d(C). If p2 ≥ 6, from inequality (2) we get 3p2 ≤ 2p3 + 10 and p3 ≥ 4.
Thus we have s(C) − d(C) = s(C4) − d(C2) + s(C5) − d(C1) + s(C3) ≥ −5 + 2 + 4 = 1.

4. |K| = 3. If K /∈ F, the surplus of the top set is 10, the surplus of a level 4 set
is equal to the deﬁcit of a level 1 set (both 6), and the surplus of a level 3 set is
equal to the deﬁcit of a level 2 set (both 2). If p1 > p4, then p1 = 4 and p4 = 3.
Now we have p3 ≥ 4, which together with (2) gives p2 ≤ p3 + 2. Clearly, in this
case s(C) ≥ d(C). If p1 ≤ p4, using p2 ≤ p3 + 3 (which is a consequence of (2)), we
conclude that s(C) ≥ d(C) + 4 holds.

If K ∈ F, such hypercubes may have a deﬁcit. We can see from the previous case
that d(C) ≤ s(C) + 10 and there are examples of hypercubes in which equality holds.

5. |K| = 4. The surplus of the top set is 11, the deﬁcit of the bottom set is 9. If there
are at least one set on levels lower than 3, then s(C4) = 7p4 ≥ 5p1 + 1 = d(C2) + 1.
As the deﬁcit of a level 2 set is 1, inequality (2) implies d(C2) ≤ s(C3) + 3. This
implies s(C) ≥ d(C).

6. |K| = 5. We will only examine the case K ∈ F and try to prove s(C) ≥ d(C) + 20.
In this situation, s(C4) + s(C5) ≥ 36. K has the deﬁcit 8; levels 1 and 3 have equal
deﬁcit/surplus, and level 2 sets have weight t(w). From p1 ≤ p3 + 2 follows that
d(C1) − s(C3) ≤ 8 and s(C) ≥ d(C) + 20.

7. |K| = 6. The surplus of the top set is 13. If K /∈ F, d(C1) = 3p1 ≤ 9p4 = s(C4), so
s(C) ≥ d(C) + 13. If K ∈ F, then using similar arguments as in the case |K| = 5,
we can prove s(C) ≥ d(C) + 28.

We have proved that in the top hypercube s(C) ≥ d(C)+13 holds. Thus, there are at least
two of the ‘bad’ hypercubes with |K| = 3, K ∈ F , in which s(C) ≥ d(C) − 10. Consider
the family of bottom sets of these hypercubes G ⊆ F. Lemma 3.1 guarantees |G| ≤ 4. If
|G| = 2 then, according to Lemma 3.1, 5 ≤ | ⋃ G| ≤ 6 and ⋃ G ∈ F is the bottom set of
a hypercube C. In both cases, s(C) ≥ d(C) + 20. If |G| ≥ 3, then the surplus of the top
hypercube is by at least 28 greater than its deﬁcit, and there will be a hypercube C with
|K| = 5 and s(C) ≥ d(C) + 20. Thus F is Frankl’s.

Lemma 3.3. Let |X| = 11 and F contains three four-element sets which all contain the
same three elements. Then F is Frankl’s.

the electronic journal of combinatorics 15 (2008), #R88 8

Proof. Let {a, b, c, d}, {a, b, c, e, }, {a, b, c, f } ∈ F . The weight function we choose is
w(x) = 3 for x ∈ {a, b, c, d, e, f } and w(x) = 1 for all other x ∈ X. The target weight
is 11.5. We consider an {a, b, c, d, e, f }-hypercube C with bottom set K. Again we have
several possible cases depending on |K|.

1. |K| = 0. Here p4 ≥ 3 and p5 ≥ 3, so s(C) ≥ 18.5, while d(∅) = 11.5. Lemma 3.1
implies p3 ≤ 4, so d(C3) ≤ 10. If p3 ≥ 3 then we must have that any two level 3 sets
intersect (according to Lemma 3.1), so p3 = 4 implies p5 = 6 and s(C) > d(C). The
worst case is p3 = 3 when s(C) + 0.5 ≥ d(C).

2. |K| = 1. Then the surplus of the top set of C is 7.5 and p0 = p1 = 0. Since
p3 ≤ p4 + 5 (according to (2)), d(C3) = 1.5p3 ≤ 1.5p4 + 7.5 = s(C4) + 7.5. By Lemma
3.1, the intersection of any two level 2 sets is K, so p2 ≤ 3. Hence, p2 ≤ p5 and
d(C2) = 4.5p2 ≤ 4.5p5 = s(C5), so d(C) ≤ s(C).

3. |K| = 2. Then K /∈ F, and by Lemma 3.1, p1 ≤ 1. The surplus of the top set is 8.5.
By Lemma 3.2 and Turan’s Theorem, each level k set which is in F can contain at
most k2
4 level 2 sets which are in F. From Lemma 2.3 we conclude 3p2 ≤ p4 + 15 and
p3 ≤ p4 + 5. The second inequality implies d(C3) ≤ s(C4) + 2.5, so p1 = 1 or p2 ≥ 2.
Both imply p5 ≥ 2, so s(C5) + s(C6) ≥ 19.5, d(C1) + d(C2) > 17 and d(C2) ≥ 11.

If p5 = 2, then p2 ≤ 5 (otherwise all three level 5 sets containing {a, b, c} would be
in F ). Let K ∪{a, b, c, d, e} /∈ F. Then all level 2 sets in F are in C f
1 , and d(C2) ≥ 11
implies p2 = p1(Cf ) ≥ 4, so p3(Cf ) ≥ 4. Therefore, p4 ≥ 4, and p3 ≤ p4 + 5 implies
d(C3) ≤ s(C4) − 5.5. Now, d(C1) + d(C2) > 25, so p2 ≥ 6, which is a contradiction.

If p5 ≥ 3, then s(C) − d(C3) ≥ 22.5. Therefore, p2 ≥ 5 and p4 ≥ 1 (at least one of
the level 4 sets containing {a, b, c} must be in F when p2 > 3). Let p4 = 3l + s,
0 ≤ s ≤ 2. Then p3 ≤ 3l + s + 5, while 3p2 ≤ p4 + 15 implies p2 ≤ l + 5. Therefore,
d(C2)+d(C3)−s(C4) ≤ 20−2.5l−2s ≤ 18. On the other hand, s(C5)+s(C6)−d(C1) ≥
18.5, so s(C) ≥ d(C).

4. |K| = 3 and K /∈ F . There are four cases depending on p1.

(a) p1 ≤ 3. Then p4 ≥ p1 and d(C1) − s(C4) = 5.5p1 − 3.5p4 ≤ 6. The surplus
of the top set is 9.5, which means that d(C2) = 2.5p2 > 3.5, so p2 ≥ 2. This
implies p5 ≥ 2, and as s(C5) = 6.5p5 ≥ 13, we have p2 ≥ 7. Now p5 ≥ 3, and
d(C2) > 23. This gives p2 ≥ 10. From inequality (2) we get 2p2 ≤ p3 + 10. Now
we have p3 ≥ 10, and from s(C3) = 0.5p3, we obtain p2 ≤ 12. Now it is easy to
verify that p5 = 6 and s(C) ≥ d(C).

(b) p1 = 4. From d(C1) = 22, p4 ≥ 3 and p5 ≥ 3 we conclude d(C2) > 17.5 and
p2 ≥ 8. If one considers the level 2 sets which have one-element intersection
with {a, b, c}, and the remaining ones, it is easy to see that at least 4 in any
of those groups produce a level 4 set not containing {a, b, c}, so p4 ≥ 4. This
gives p2 ≥ 9 and (by Lemma 2.3) p3 ≥ 8. Now s(C) ≥ 47, which gives p2 ≥ 11.
Now for at most one x ∈ {a, b, c, d, e, f }, p2(C¬x) ≤ 6, and the top set of C ¬x is
not in F. So, p5 ≥ 5 which implies s(C) ≥ d(C).

the electronic journal of combinatorics 15 (2008), #R88 9

(c) p1 = 5. Let K ∪ {x} be the level 1 set not in F . Then all ﬁve level 4 sets not
containing x are in F and at least one of the sets K ∪{a, b, c, d}, K ∪{a, b, c, e},
K ∪ {a, b, c, f } which contains x is in F . So p4 ≥ 6, p3 ≥ 10 and p5 ≥ 3 holds.
This means that s(C) ≥ 55, which gives p2 ≥ 12. Now it is easy to verify p5 = 6
which implies s(C) ≥ d(C).

(d) p1 = 6. Then all the sets from C except K are in F.

If K ∈ F then, clearly, s(C) + 8.5 ≥ d(C).

5. |K| = 4. If K /∈ F , we can imitate the proof for |K| = 3. If K ∈ F , 2p2 ≤ p3 + 10
implies d(C2) − s(C3) ≤ 7.5. s(C4) + s(C5) + s(C6) ≥ 46.5, while d(C0) + d(C1) ≤ 34.5,
so s(C) ≤ d(C).

6. |K| = 5. Here 2p2 ≤ p3 + 10 implies d(C2) − s(C3) ≤ 2.5. If K ∈ F , then s(C4) +
s(C5) + s(C6) ≥ 53.5 and d(C0) + d(C1) ≤ 27.5. This gives s(C) ≥ d(C) + 23.5. If
K /∈ F it is easy to see that if d(C) > 0, then p5 > 0, and (quite straightforwardly)
d(C) ≤ s(C5). The ‘worst’ case is d(C) = 0 when s(C) ≥ d(C) + 11.5.

We have proved that, except for the bottom hypercube with possible deﬁcit 0.5, ‘bad’
hypercubes can appear only at level 3 and there d(C) ≤ s(C) + 8.5. According to Lemma
3.1, there can be at most two of them. If there is only one, its extra deﬁcit is covered
by the top hypercube. If there are two of them, according to Lemma 3.1, in the top
hypercube it holds K ∈ F , so the top hypercube satisﬁes s(C) ≥ d(C) + 23.5 and easily
makes up for all extra deﬁcit.

Lemma 3.4. Let |X| = 11 and F contains two four-element subsets of a ﬁve element
set. Than F is Frankl’s.

Proof. Let {a, b, c, d}, {a, b, c, e} ∈ F. We choose the weight function such that w(a) =
w(b) = w(c) = w(d) = w(e) = 4 and w(x) = 1 for all other x ∈ X, so t(w) = 13. Again
we observe an {a, b, c, d, e}-hypercube C with bottom set K and consider cases:

1. |K| = 0. Here d(∅) = 13 and by Lemma 3.1, p3 ≤ 2 and d(C3) ≤ 2. On the other
hand, s(C) ≥ 13, so s(C) + 2 ≥ d(C).

2. |K| = 1. Here d(C) = d(C2) = 4p2. By Lemma 3.1, p2 ≤ 2 and d(C) ≤ 8. The
surplus of the top set is 8, so s(C) ≥ d(C).

3. |K| = 2. Lemma 3.1 gives p1 ≤ 1. By Lemma 3.3 every element from {a, b, c, d, e}
can appear in at most two level 2 sets from F. This implies p2 ≤ 5. Also, from
Lemma 3.2 and Lemma 2.3 we get d(C2) = 3p2 ≤ p3 + 10 = s(C3) + 10. If p4 ≥ 2,
then s(C4) + s(C5) ≥ 19 > 17 ≥ d(C1) + d(C2) − s(C3). If p4 = 1 then F ∩ C2 ⊆ Cd
1
or F ∩ C2 ⊆ Ce
1. Either way, p2 ≤ 2 because d (or e) can be in at most two level
2 sets, so s(C) ≥ 14 > 13 ≥ d(C). Finally, if p4 = 0 then p1 = 0 and p2 ≤ 1, so
s(C) ≥ 9 > 3 ≥ d(C).

the electronic journal of combinatorics 15 (2008), #R88 10

4. |K| = 3. Let K /∈ F. From Lemma 3.3 it follows p1 ≤ 2, and this implies p1 ≤ p4
and d(C1) = 6p1 ≤ 6p4 = s(C4). By inequality (2) we get 3p2 ≤ 2p3 + 10. Therefore,
d(C2) − s(C3) = 2p2 − 2p3 ≤ 6, while the surplus of the top set is 10. When K ∈ F
we will prove that d(C) ≤ s(C) + 4. If p1 < 2, according to above observations, we
have s(C) ≥ d(C). So we may assume p1 = 2. If p2 ≥ 5 it follows from 3p2 ≤ 2p3 +10
that p2 ≤ p3 + 2. If p2 = 3 then p3 ≥ 1. Finally, when p2 = 4, either for an element
x ∈ {a, b, c, d, e}, p1(Cx) ≥ 3, and therefore p3 ≥ p2(Cx) ≥ 3 holds, or for any
element x ∈ {a, b, c, d, e} such that K ∪ {x} ∈ F, p2(C¬x) ≥ 2, so the unions of these
sets in F ∩ C¬x
2 with K ∪ {x} give p3 ≥ p2(Cx) ≥ 2. In all cases for p2, the inequality
p2 ≤ p3 + 2 holds. Then d(C2) ≤ s(C3) + 4 and d(C0) + d(C1) ≤ s(C4) + s(C5), which
gives s(C) + 4 ≥ d(C).

5. 4 ≤ |K| ≤ 5 (we only consider the ‘harder’ case |K| = 4). From 3p2 ≤ 2p3 + 10 we
conclude p2 ≤ p3 + 3 and d(C2) = p2 ≤ 3p3 + 3 = s(C3) + 3. Since the surplus of the
top set is 11, either K ∈ F, or p1 ≥ 2. Either way, p4 ≥ 2, and s(C4) + s(C5) ≥ 25.
Therefore, d(C1) > 13, so p1 ≥ 3. But, in this case, p3 ≥ 1, so d(C2) ≤ s(C3) + 1.
This implies d(C1) > 15 and p1 ≥ 4. Now p3 ≥ 4 and d(C2) ≤ s(C3) − 5. This implies
d(C1) > 21 and p1 = 5, but then C \ {K} ⊆ F and s(C) ≥ d(C) + 16.

6. |K| = 6. If K /∈ F , we will prove that s(C) ≥ d(C) + 13. The surplus of the top
set is 13, while d(C) = d(C1) = 3p1. But, if p1 ≤ 2, then p1 ≤ p4 and if p1 > 2,
then p4 ≥ 2. In both cases, s(C4) = 9p4 ≥ 3p1 = d(C1). If K ∈ F , we will prove
that s(C) ≥ d(C) + 19. We have s(C4) + s(C5) ≥ 31 and d(C0) + 19 = 26. Therefore,
p1 ≥ 2, and hence p2 ≥ 1. Now s(C) ≥ 32 and p1 ≥ 3. We have p1 ≤ p3 + 2, so
d(C1) − s(C3) = 3p1 − 5p3 ≤ 6 − 2p3 ≤ 4 and the claim follows.

We have the bottom hypercube with d(C) ≤ s(C) + 2 and the top hypercube with
d(C) ≤ s(C) − 13. The only other hypercubes with d(C) > s(C) are those with |K| = 3,
K ∈ F (d(C) ≤ s(C) + 4). According to Lemma 3.1, we can have at most four such
hypercubes in F. However, from the extra surplus in the top hypercube we conclude we
have at least three such ‘bad’ hypercubes in F . By Lemma 3.1, this means that the union
of their bottom sets must be X − {a, b, c, d, e}. Therefore, in the top hypercube, K ∈ F
and d(C) ≤ s(C) − 19. This cannot be ‘covered’ by the extra deﬁcits of the bottom and
‘bad’ hypercubes.

Lemma 3.5. Let |X| = 11 and F contain two intersecting three-element sets. Then F
is Frankl’s.

Proof. Let {a, b, c}, {a, d, e} ∈ F. The weight function we choose is w(a) = 8, w(b) =
w(c) = w(d) = w(e) = 4 and w(x) = 1 for all other x ∈ X. The target weight t(w) = 15.
We consider an {a, b, c, d, e}-hypercube C with bottom set K. As usual, we consider
possible values of |K|:

1. |K| = 1. Here, p0 = p1 = 0 and according to Lemma 3.1, p2 ≤ 2. Also, Lemma
3.4 implies that p3 ≤ 2, and if p3 = 2, then p2(Ca) ≥ 1, so d(C3) ≤ 2. Since

the electronic journal of combinatorics 15 (2008), #R88 11

p2 ≤ 2, p2 ≤ p3(Ca) + p2(Ca). Therefore, d(C2) ≤ 6p2 ≤ 2p3(Ca) + 2p2(Ca) + 8 ≤
s(C3) + s(C4) + 8 = s(C) − 2.

2. |K| = 2. Then K /∈ F , by Lemma 3.1, p1 ≤ 1, while by Lemma 3.4, p2 ≤ 2. The
surplus of the top set is 11 and d(C3) ≤ 4. If d(C1) < 9, then d(C1) ≤ s(C3). This
means that d(C2) > 7, so p2 = 2 and d(C2) = 10. But, p2 = 2 implies p4 ≥ 1, and
s(C4) + s(C5) ≥ 14 ≥ d(C2) + d(C3), so s(C) ≥ d(C).

Let us now assume that p1 = 1 and d(C1) = 9. This means that p4 ≥ 1, p3 ≥ 1,
s(C4) ≥ 7 and s(C3) ≥ 3. Therefore s(C) ≥ 21, so p2 = 2 and d(C2) = 10. But then
K ∪ {b, c, d, e} ∈ F, according to Lemma 3.4. Therefore, s(C) ≥ 24 > d(C).

3. |K| = 3. We have p1 ≤ 1, according to Lemma 3.4. The subfamily of C

C′ = {K, K ∪ {a}, K ∪ {b, c}, K ∪ {d, e}, K ∪ {a, b, c},
K ∪ {a, d, e}, K ∪ {b, c, d, e}, K ∪ {a, b, c, d, e}}

has s(C′ ∩ F) ≥ d(C′ ∩ F). Let q2 = |C2 ∩ (C¬a \ C′) ∩ F|. If q2 = 0, then d((C \
C′) ∩ F ) = 8p1(C¬a
1 ) ≤ 8p3(Ca) ≤ s((C \ C′) ∩ F). If q2 > 0, then q2 ≤ p3(Ca) − 1
or q2 = p3(Ca) = 4. Hence, d((C \ C ′) ∩ F ) ≤ 4q2 + 8 ≤ 8p3(Ca) ≤ s((C \ C′) ∩ F ).
Either way, s(C) = s((C \ C ′) ∩ F) + s(C′ ∩ F ) ≥ d((C \ C ′) ∩ F ) + d(C′ ∩ F ) = d(C).

4. 4 ≤ |K| ≤ 5. We will consider only the case |K| = 4. Analogously to the case
|K| = 3, we deﬁne the subfamily C ′ ⊆ C and see easily that s(C ′ ∩F ) ≥ d(C′ ∩F )+4.
We have only eight sets with a deﬁcit in C \ C ′, and can divide them among four
groups of the form K ∪ {b}, K ∪ {b, d}, K ∪ {a, b, d, e}. The total deﬁcit of such a
group is by at most 1 greater than the surplus. Therefore, s(C) ≥ d(C).

5. |K| = 6 and |K| = 0. For |K| = 0, according to Lemma 3.1, d(C) ≤ s(C) + 4.
But, considering that the weight of a set in the top hypercube is by 2 greater than
of the corresponding set in the hypercube with |K| = 4, if |C ∩ F | ≥ 2 in the top
hypercube, the proof for |K| = 4 implies that s(C) ≥ d(C) + 4 for |K| = 6. If
|C ∩ F| = 1 in the top hypercube, then C ∩ F = {X}, so s(C) ≥ d(C) + 4, again.

Lemma 3.6. Let |X| = 11 and F contain two three-element sets. Then F is Frankl’s.

Proof. Let {a, b, c}, {d, e, f } ∈ F. The weight function we choose is w(x) = 2.5 for
x ∈ {a, b, c, d, e, f } and w(x) = 1 for all other x ∈ X. The target weight is 10. We
consider an {a, b, c, d, e, f }-hypercube C with bottom set K. We will prove that the only
hypercube with d(C) − s(C) > 0 is the bottom one, and that this diﬀerence will be covered
by the extra surplus in the top hypercube.

1. |K| = 0. Since p3 = 2, d(C) − s(C) ≤ 10 + 2.5p3 − 5 ≤ 10.

2. |K| = 1. We have p0 = p1 = p2 = 0. According to Lemma 3.4, p3 ≤ 4, and therefore
s(C) ≥ s(C6) = 6 ≥ 1.5p3 = d(C).

the electronic journal of combinatorics 15 (2008), #R88 12

3. |K| = 2. From Lemma 3.5 we get p1 = 0, from Lemma 3.4 we get p2 ≤ 3, while
d(C3) = 0.5p3. All sets in C3 ∪ C5, except K ∪ {a, b, c} and K ∪ {d, e, f }, can
be divided into six groups of the form K ∪ {a, b, d}, K ∪ {a, b, e}, K ∪ {a, b, f },
K ∪{a, b, d, e, f }. The total deﬁcit of such a group is not greater than the surplus, so
we have d(C3)−s(C5) ≤ 1. The surplus of the top set is 7. This gives d(C2) = 3p2 > 6
and p2 = 3. By Lemma 3.4 this forces p4 ≥ 3, which means s(C) ≥ d(C).

4. |K| = 3. If p4 + p5 = 0, then d(C) ≤ d(K) = 7 < 8 ≤ s(C). So we may assume
p4 + p5 > 0. From Lemma 3.4 we conclude p1 ≤ 1. Also, we can notice that
s(C3) = 0.5p3 ≥ p0. Let Q = {Y ∈ C2 : |Y ∩ {a, b, c}| = 1}, R = C2 \ Q, q2 = |Q ∩ F |
and r2 = |R ∩ F|. Since r2 ≤ p5, s(C5) − 2r2 = 5.5p5 − 2r2 ≥ 3.5p5. Consider the
bipartite graph G = (V, E) where V = {a, b, c, d, e, f } and xy ∈ E iﬀ K ∪{x, y} ∈ Q.
Let m = |{x ∈ {a, b, c} : dG(x) > 0}| and n = |{x ∈ {d, e, f } : dG(x) > 0}|. Then
q2 ≤ mn ≤ m + n + (m
2 ) + (
n
2) − 1 ≤ p4 + p5 − 1. Now s(C) − d(C) ≥ s(C6) + s(C5) +
3p4 + p0 − 2q2 − 2r2 − 4.5p1 − 7p0 ≥ 8 + 3 − 4.5 − 6p0 + 3.5p5 + 3(p4 − 1) − 2q2 ≥
0.5 + 2(p5 + p4 − 1 − q2) ≥ 0.

5. |K| = 4. Here s(C3) = 1.5p3 ≥ 3p0, so s(C6) + s(C3) − d(C0) ≥ 9 − 3p0 ≥ 6. Since
p1 ≤ p4, s(C4) − d(C1) = 4p4 − 3.5p1 ≥ 0. Since d(C2) = p2, we have p2 ≥ 7. But
now, using a similar argument with q2 and r2 as above, we get p5 ≥ 2, which implies
15 ≥ p2 = d(C2) > 19, a contradiction.

6. |K| = 5. Since p1 ≤ p4 and s(C3) = 2.5p3 ≥ 5p0, we get s(C) − d(C) ≥ 10 + 7.5p5 +
5p4 + 5p0 − 5p1 − 5p0 ≥ 10.

Lemma 3.7. Let |X| = 11 and F contain a four-element set and one of its three-element
subsets. Then F is Frankl’s.

Proof. Let {a, b, c}, {a, b, c, d} ∈ F . The weight function will be w(a) = w(b) = w(c) = 3,
w(d) = 2 and w(x) = 1 for all other x ∈ X. The target weight is 9. Let C be an
{a, b, c, d, }-hypercube with bottom set K. We consider the cases:

1. |K| = 1. Here d(C) = 0.

2. |K| = 2. By Lemma 3.4 we get p2 ≤ 2, which gives s(C) ≥ s(C4) ≥ 4 ≥ 2p2 ≥ d(C).

3. |K| = 3. Here K /∈ F, d(C2) = d(Cd
1 ) ≤ 3, and Lemma 3.4 implies p1 ≤ 1. The
surplus of the top set is 5, so p1 = 1 and p1(Cd) ≥ 2. But, this means p3 ≥ 1 and
s(C) ≥ 7 ≥ d(C).

4. 4 ≤ |K| ≤ 6. We may assume that |K| = 4. Here d(C) = d(C0) + d(C1). As the
surplus of the top set is 6, and p1 ≥ 2 implies K ∪ {a, b, c} ∈ F , we may assume
K ∈ F. We now have s(C) ≥ 10, and d(C1) > 5. Therefore, p1 ≥ 3. When
p1 = 4, C ⊆ F, and d(C) < s(C). When p1 = 3 and K ∪ {d} /∈ F, then s(C2) = 3
and s(C) ≥ 13 > d(C). Finally, if p1 = 3 and K ∪ {d} ∈ F, then s(C3) ≥ 7 and
s(C) ≥ 13 > d(C).

the electronic journal of combinatorics 15 (2008), #R88 13

5. |K| = 0 and |K| = 7. The total deﬁcit of the two hypercubes is at most d(∅) +
d(X \ {a, b, c, d}) = s(X) + s({a, b, c, d}).

Lemma 3.8. Let |X| = 11 and F contain a three-element set and a four-element set
which do not intersect. Then F is Frankl’s.

Proof. Let {a, b, c}, {d, e, f, g} ∈ F. The weight function will be w(x) = 2 for x ∈
{a, b, c, d, e, f, g} and w(x) = 1 for all other x ∈ X. The target weight is 9. Let C be an
{a, b, c, d, e, f, g}-hypercube with bottom set K. We will prove that the only hypercube
with d(C) − s(C) > 0 is the bottom one, and that this diﬀerence will be covered by the
extra surplus in the top hypercube. The cases are:

1. |K| = 0. Here we will prove d(C) ≤ s(C) + 8. By Lemmas 3.7 and 3.4, any level
4 set in F diﬀerent from {d, e, f, g} has a two-element intersection with {d, e, f, g}.
However, by Lemma 3.4 there can be at most one such set of the type {x, y, d, e}
in F , and it implies that {a, b, c, d, e} ∈ F. Therefore, p4 ≤ p5 + 1. So d(C) =
d(C0) + d(C3) + d(C4) = 9 + 3 + p4 ≤ p5 + 13 = s(C5) + s(C7) + 8 ≤ s(C) + 8.

2. |K| = 1. According to Lemmas 3.7 and 3.4, every level 3 set in F has either a
two-element intersection with {a, b, c} (we denote their number by q3), or a two-
element intersection with {d, e, f, g} (we denote their number by r3). According to
Lemma 3.4, at most one of the sets K ∪ {a, b, x}, x ∈ {d, e, f, g}, could be in F
(and it implies K ∪ {a, b, d, e, f, g} ∈ F), hence q3 ≤ p6. Similarly, at most one of
the sets K ∪ {d, e, x}, x ∈ {a, b, c}, could be in F, which implies r3 ≤ p5. Therefore,
d(C) = d(C3) = 2p3 = 2q3 + 2r3 ≤ 4p6 + 2p5 ≤ s(C).

3. |K| = 2. We have d(C) = d(C2) + d(C3) = 3p2 + p3. We deﬁne q3 and r3 similarly
as in the case |K| = 1, while s3 is the number of level 3 sets in F which have no
intersection with {a, b, c}. Similarly as in the previous case, {d, e, f, g}, {a, b, c} ∈ F
imply that q3 + 4s3 ≤ 4p6 and r3 ≤ 3p5. Therefore, s(C) − s(C4) − d(C3) ≥ 7 + 5p6 +
3p5 − q3 − r3 − s3 − 1 ≥ 6. Lemma 3.4 implies that the union of any two level 2 sets
is a level 4 set, so d(C2) > 6 implies p2 = 3 ≤ p4, and d(C2) − s(C4) ≤ 6.

4. |K| = 3. Here d(C) = d(C1) + d(C2) = 4p1 + 2p2. Let q2, r2, s2 denote the
number of level 2 sets in F whose intersection with {a, b, c} has 0, 1 and 2 elements,
respectively. We have r2 ≤ 12, while {d, e, f, g}, {a, b, c} ∈ F imply 4q2 + r2 ≤ 4p5,
r2 ≤ 3p4 and s2 ≤ p6. Hence, d(C2) = 2q2 + 2r2 + 2s2 ≤ 2p4 + 4p5 + 6p6 + 1
3 r2 ≤
s(C4) + s(C5) + s(C6) + 4. On the other hand, Lemma 3.4 implies p1 ≤ 1, so
d(C1) ≤ s(C7) − 4.

5. |K| = 4. Note that the sets K, K ∪ {a, b, c}, K ∪ {d, e, f, g}, and X have total
surplus by at least 8 greater that the deﬁcit (when all are in F ). We will prove
that the deﬁcit of the remaining sets in C is not greater than the surplus. Denote
by p′ the number of level 3 sets in F diﬀerent from K ∪ {a, b, c} and by p′ the
number of level 4 sets in F diﬀerent from K ∪ {d, e, f, g}. Deﬁne q2, r2 and s2
as above, let q1 be the number of level 1 sets in F which have empty intersection

the electronic journal of combinatorics 15 (2008), #R88 14

with {a, b, c} and r1 = p1 − q1. Let Cx be the {d, e, f, g}-hypercube with bottom
set K ∪ {x}, x ∈ {a, b, c}. Clearly, p1(Cx) ≤ p2(Cx) + 1, and if Cx ∩ F ̸= ∅, then
d(Cx) = 3p0(Cx) + p1(Cx) ≤ 3 + p2(Cx) + 1 ≤ s(Cx). Note that the top set of
Cx is a level 5 set of C which contains {d, e, f, g}, while in the proof of q2 ≤ p5
in the previous case we used the level 5 sets which contain {a, b, c}, so we have
3r1 + r2 + q2 ≤ p′ + 5p5. We also have that q1 ≤ p′ and s2 ≤ p6. Therefore,
d(C1) + d(C2) ≤ p′ + 3p′ + 5p5 + 7p6.

Lemma 3.9. Let |X| = 11 and F contain a three-element set. Then F is Frankl’s.

Proof. Let {a, b, c} ∈ F. The weight function will be w(a) = w(b) = w(c) = 4 and
w(x) = 1 for all other x ∈ X. The target weight is 10. Let C be an {a, b, c}-hypercube
with bottom set K. There are several possible cases:

1. |K| = 1 or |K| = 2. In these hypercubes d(C) = 0.

2. |K| = 3. By Lemmas 3.6 and 3.4, d(C) = 3p1 ≤ 3 < s(C3).

3. |K| = 4. By Lemma 3.8, d(C) = 2p1 ≤ 6 = s(C3).

4. 5 ≤ |K| ≤ 7. We will only examine the case |K| = 5. Obviously, p1 ≤ p2 + 1, so
d(C) = 5p0 + p1 ≤ 3p2 + 7p3 = s(C).

5. |K| = 0 or |K| = 8. The ﬁrst hypercube has d(C) = s(C) + 8 and the second one
d(C) = 2p0 ≤ 10p3 − 8 ≤ s(C) − 8.

Lemma 3.10. Let |X| = 11 and F contain a ﬁve-element set and one of its four-element
subsets. Then F is Frankl’s.

Proof. Let {a, b, c, d}, {a, b, c, d, e} ∈ F. The weight function will be w(a) = w(b) =
w(c) = w(d) = w(e) = 2 and w(x) = 1 for all other x ∈ X. The target weight is 8. Let C
be an {a, b, c, d, e}-hypercube with bottom set K. We consider the following cases:

1. |K| = 1. According to Lemma 3.4, d(C) = d(C3) = p3 ≤ 2 < 3 = s(C5).

2. |K| = 2. According to Lemma 3.4, d(C) = d(C2) = 2p2 ≤ 4 = s(C5).

3. |K| = 3. According to Lemma 3.4, d(C) = d(C1) + d(C2) = 3p1 + p2 ≤ p2 + 3. Since
s(C5) = 5, we have d(C2) > 2 and p2 > 2. Now, p2 = p1(Ce), or K ∪ {a, b, c, d} ∈ F ,
either way p4 ≥ 1. From inequality (2) we get 3p2 ≤ 2p3+10, which gives p2 ≤ p3+3.
Combining the above results, we get d(C) ≤ p2 + 3 ≤ p3 + 3p4 + 5p5 = s(C).

4. |K| = 4 or |K| = 5. We will only consider the case |K| = 4. In this hypercube
p0 ≤ p4 and p1 ≤ p3 + 2, so d(C) = 4p0 + 2p1 ≤ 4p4 + 2p3 + 4 ≤ s(C) − 2.

5. |K| = 0 or |K| = 6. The ﬁrst hypercube has d(C) = s(C) + 8 and the second one
d(C) = 2p0 ≤ 10p5 − 8 ≤ s(C) − 8.

the electronic journal of combinatorics 15 (2008), #R88 15

Lemma 3.11. Let |X| = 11 and F contain a four-element set. Then F is Frankl’s.

Proof. Let {a, b, c, d} ∈ F. The weight function will be w(a) = w(b) = w(c) = w(d) = 2.5
and w(x) = 1 for all other x ∈ X. The target weight is t(w) = 8.5. Let C be an
{a, b, c, d}-hypercube with bottom set K. We will consider the following cases:

1. |K| = 1. Here d(C) = 0.

2. |K| = 2. According to Lemma 3.4, d(C) = d(C2) = 1.5p2 ≤ 3 < s(C4).

3. |K| = 3. Lemma 3.4 implies d(C) − s(C4) = 3p1 + 0.5p2 − 4.5 ≤ 0.5p2 − 1.5, so
p2 > 3. Hence, p3 ≥ 3 and s(C3) ≥ 6 > d(C) − s(C4).

4. |K| = 4. Lemma 3.10 implies that p1 = 0 or p0 = 0. If p1 = 0 then d(C) = d(C0) ≤
s(C4). If p0 = 0, since s(C4) = 5.5 and d(C1) = 2p1, it must be p1 ≥ 3. This implies
p2 ≥ 3, p3 ≥ 1 and s(C) ≥ 10 > 6 ≥ d(C).

5. |K| = 5 or |K| = 6. We will only consider the case |K| = 5. There s(C4) = 6.5,
which implies d(C) > 6.5 which holds only if K ∈ F and p1 = 4. But then C ⊆ F
and d(C) ≤ s(C).

6. |K| = 0 and |K| = 7. The ﬁrst hypercube has d(C) = s(C) + 7 and the second one
d(C) = 1.5p0 ≤ 8.5p5 − 7 ≤ s(C) − 7.

Theorem 3.1. If |X| = 11 then F is Frankl’s.

Proof. If there are no ﬁve element sets in F then for every A ∈ F it holds |A| > |X|
2
and F is clearly Frankl’s. Let {a, b, c, d, e} ∈ F. The weight function we choose is
w(a) = w(b) = w(c) = w(d) = w(e) = 2 and w(x) = 1 for all other x ∈ X. The target
weight is 8. Let C be an {a, b, c, d, e}-hypercube with bottom set K. There are several
cases we need to consider.

1. |K| = 1 or |K| = 2. Here d(C) = 0.

2. |K| = 3. Here d(C) − s(C5) = d(C2) − 5 = p2 − 5, so p2 ≥ 6. Hence, p3 ≥ 2 and
p4 ≥ 1, which gives s(C) ≥ 10 ≥ p2 = d(C).

3. |K| = 4. Here d(C) − s(C5) = d(C1) − 6 = 2p1 − 6, so p1 ≥ 4. Hence, p3 ≥ 4 and
p4 ≥ 1, which gives s(C) ≥ 18 > d(C).

4. |K| = 5. Here d(C) − s(C5) = d(C0) + d(C1) − 7 = 3 + p1 − 7, so p1 = 5. Hence,
C ⊆ F, which gives s(C) ≥ d(C).

5. |K| = 0 and |K| = 7. The ﬁrst hypercube has d(C) = s(C) + 6 and the second one
d(C) = 2p0 ≤ 8p5 − 6 ≤ s(C) − 6.

Acknowledgements

The authors wish to thank Professor Theresa P. Vaughan for many useful comments.

the electronic journal of combinatorics 15 (2008), #R88 16

References

[1] W. Gao and H. Yu, Note on the Union-Closed Sets Conjecture. Ars Combin. 49
(1998), pp. 280-288.

[2] K. Henry and M. S. Roddy, A Notion of Reducibility for Union-Closed Families of
Sets. (in preparation)

[3] R. T. Johnson and T. P. Vaughan, On Union-Closed Families, I. J. Combin. Theory
Ser. A 84 (1998), no. 2, pp. 242-249.

[4] G. Lo Faro, A Note on the Union-Closed Sets Conjecture. J. Austral. Math. Soc. Ser
A 57 (1994), no. 2, pp. 230-236.

[5] G. Lo Faro, Union-Closed Sets Conjecture: Improved Bounds. J. Combin. Math.
Combin. Comp. 16 (1994), pp. 97-102.

[6] P. Markovi´c An Attempt at Frankl’s Conjecture. Proceedings of the Novi Sad Algebraic
Conference 2005 (NSAC’05), a special issue of Publ. Math. Inst. (Beograd) (N. S.)
81(95) (2007), pp. 29-43.

[7] R. Morris FC-families and Improved Bound for Frankl’s Conjecture. European J.
Combin. 27 (2006), no. 2, pp. 269-282.

[8] B. Poonen, Union-Closed Families. J. Combin. Theory Ser. A 59 (1992), no. 2, pp.
253-268.

[9] I. Rival (ed.), Graphs and Order. NATO Advanced Science Institute Series C: Math-
ematical and Physical Sciences, 147 D. Reidel Publishing Co., Dordrecht-Boston,
Mass. (1985), p. 525.

[10] R. P. Stanley, Enumerative Combinatorics, Vol. I. The Wadsworth and Brooks/Cole
Mathematics Series The Wadsworth and Brooks/Cole Advanced Books and Software,
Monterey, Calif. (1986).

[11] T. P. Vaughan, Families Implying the Frankl Conjecture. European J. Combin. 23
(2002), no. 7, pp. 851-860.

[12] T. P. Vaughan, A Note on the Union-Closed Sets Conjecture. J. Combin. Math.
Combin. Comput. 45 (2003), pp. 95-108.

[13] T. P. Vaughan, Three-sets in a Union-Closed Family. J. Combin. Math. Combin.
Comput. 49 (2004), pp. 73-84.

the electronic journal of combinatorics 15 (2008), #R88 17
