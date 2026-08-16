<!-- source: https://arxiv.org/pdf/2408.11213 | converted from PDF -->

On supratopologies, normalized families
and Frankl’s conjecture

Andr´e Carvalho∗ and Ant´onio Machiavelo†

CMUP, Faculdade de Ciˆencias da Universidade do Porto
Rua do Campo Alegre
4169-007, Porto, Portugal

September 18, 2025

Abstract

We introduce some generalized topological concepts to deal with union-closed fam-
ilies, and show that one can reduce the proof of Frankl’s conjecture to some families of
so-called supratopological spaces. We prove some results on the structure of normal-
ized families, presenting a new way of reducing such a family to a smaller one using
dual families. Applying our reduction method, we prove a refinement of a conjecture
originally proposed by Poonen. Finally, we show that Frankl’s Conjecture holds for the
class of families obtained from successively applying the reduction process to a power
set.

1 Introduction

Let F be a finite family of sets. In this context, by “family of sets” we mean a set consisting
of sets. We say that F is union-closed if, for any F, G ∈ F, we have that F ∪ G ∈ F. We
define the universe of a family F as the union of all its member-sets, and denote it by U (F).
Of course, F ⊆ P(U (F)), and if F is union-closed, then U (F) ∈ F.
Any bijection between two finite sets, U → V , induces a bijection P(U ) → P(V ), that,
of course, preserves unions, and therefore union-closed families, as well as all the properties
about them that are pertinent in this paper. Thus, we will only be interested in families

∗andrecruzcarvalho@gmail.com
†ajmachia@fc.up.pt
 1arXiv:2408.11213v2  [math.CO]  17 Sep 2025
modulo the equivalence relation induced by bijections on the respective universes. We will
then call two families isomorphic if such a bijection exists, and, as usual, we will say that a
family is “such and such” up to bijection, meaning up to a bijection between their universes.
For S ⊆ U (F), we define FS = {F ∈ F ∶ F ∩ S ≠ ∅} and F¬S = {F ∈ F ∶ F ∩ S = ∅}.
For a ∈ U (F), we denote F{a} by Fa, and similarly F¬{a} by F¬a.
The so called Frankl’s conjecture, also named the union-closed sets conjecture has been
attracting the curiosity of many for a long time (see [5]), mostly due to its apparently simple
statement.

Conjecture 1.1 (Frankl conjecture). If a finite family of sets F ≠ ∅, {∅} is union-closed,
then there is an element of its universe that belongs to at least half the sets of the family,
i.e.
 ∃ a ∈ U (F) ∶ ∣Fa∣ ≥ ∣F∣
2 .

The origin of Frankl’s conjecture is not completely clear. According to [3] it was well
known by the mid-1970s as a “folklore conjecture”, but it is usually attributed to P´eter
Frankl, as he stated it in terms of intersection-closed set families in 1979. The first such
attribution seems to have being done by Dwight Duffus, in 1985, in [9].
The problem has been studied from several viewpoints and some interesting formulations
have been obtained. For example, the conjecture admits a lattice-theoretical version, which
has been proved firstly for modular lattices [1] by Abe and Nakano, and later for lower
semimodular lattices by Reinhold [21]; it also admits a graph-theoretical version which is
trivially true for non-bipartite graphs and it was proved to hold for the classes of chordal
bipartite graphs, subcubic bipartite graphs, bipartite series-parallel graphs and bipartitioned
circular interval graphs in [4]; and there is also a very interesting, yet seemingly unfruitful
formulation, known as the Salzborn formulation, described in [25]. Compression techniques
have been attempted, yielding some partial results. They were introduced in this context by
Reimer in [20], and later further explored in [22] and [3]. The concept of Frankl’s Complete
families, or FC-families, introduced by Sarvate and Renaud [23], and later formalized by
Poonen [19], has also been studied by some ([17] and [24], for example). A more direct
approach on the properties a hypothetical counterexample of minimal size was taken by Lo
Faro in [10] and [11], with some interesting results.
A very thorough survey on the topic by Bruhn and Schaudt, [5], is suggested to the
interested reader, as well as the Master thesis of the first author [7].
Recently, a breakthrough by Gilmer [12] provided the first known constant lower bound
on the frequency of the most frequent element in union-closed families. This was later
improved, and the current best bound is of 0.38234 [6, 26].

2

In this paper, we will focus on the study of normalized union-closed families. These con-
stitute an interesting subclass of union-closed families, that are, in some sense, the smallest
possible separating families for a given universe. They are particularly relevant because the
above mentioned Salzborn formulation of Frankl’s conjecture only refers to normalized union-
closed families, as opposed to Frankl’s conjecture that concerns all union-closed families of
sets.
We will study normalized families, proving some of their properties, and detailing their
construction. The main result of this paper is a reduction technique that can be applied to
any normalized family to produce a smaller one. Denoting by F ⊖ S the set {F \ S ∶ F ∈ F},
where F is a family of sets and S ⊆ U (F), our result can be stated as:

Theorem 4.11. Let N be a n-normalized family and let M be any minimal non-empty set
of N . Then the family N ′ = (N \ {M }) ⊖ {aN } is (n − 1)-normalized, for some aN ∈ N .

Poonen, in [19] made the following refinement of Frankl’s conjecture:

Conjecture 5.1. Let F be a union-closed family of sets. Unless F is a power set, it contains
an element that appears in strictly more than half of the sets.

We use the reduction introduced by Theorem 4.11 to prove that this statement can be
weakened in the following way.

Conjecture 5.2. Let F be a union-closed family such that the most frequent element
belongs to exactly half the sets in F. Then F must be a power set.

Note that this conjecture only concerns families sharply satisfying the conclusion of Frankl’s
conjecture, apparently making no claim on the original conjecture. However, we show that:

Theorem 5.3. Conjectures 5.1 and 5.2 are equivalent.

Naturally, the non-trivial part is proving that Conjecture 5.2 implies the Frankl conjecture.
Finally, using the reduction of the statement of Theorem 4.11, we introduce a reduction
technique for arbitrary families, and use it to prove that Frankl’s conjecture holds for a
certain class of families obtained from successively reducing a power set, families that we
call descendents of the original family.

Theorem 5.5. If a family is a descendent of a power set, then it satisfies the Frankl Con-
jecture.
 3

The paper is organized as follows. In Section 2, we present some preliminary notions
and structural results on union-closed families and on Frankl’s conjecture, and show that
the statement of Frankl’s conjecture can be generalized in a natural way: if true, then one
can guarantee the existence of a subset of size k being in at least 1
2k of the sets of a union-
closed family. In Section 3, we show the relevance of some generalized topological concepts,
namely supratopologies, for the study of union-closed families, introducing some separation
axioms and prove that Frankl’s conjecture can be reduced to families satisfying some of those
axioms. In Section 4, we start by presenting the already known relation between union-closed
and normalized families in detail, combining the ideas from [25] and [14]. We then prove
Theorem 4.11, establishing a natural way to reduce a normalized family to a smaller one,
which looks non-trivial when seen in the original, non-normalized, context. Finally, we
present some properties of normalized families obtained through this reduction and some
of its connections to Frankl’s conjecture, including the weakening of Poonen conjecture,
in Section 5, and we prove that all families descending from power sets satisfy the Frankl
conjecture.

2 Preliminaries and an equivalent formulation

Let F be a family of sets. As usual, a set F ∈ F is said to be irreducible in F if, for all
G, H ∈ F, we have F = G ∪ H ⟹ G = F or H = F . The set of all irreducible non-empty
sets in a family F is denoted by J(F). Given a family G ⊆ P(U ), we denote by ⟨G⟩ the
smallest union-closed family in P(U ) that contains G, which is the family whose elements
are all possible finite unions of elements of G, the empty set included, as it is the union of
an empty family. When F = ⟨G⟩, we say that G is a generating family for F. Of course, F
is generated by its irreducible sets.
The family F is said to separating if, for every two distinct elements a, b ∈ U (F), there
is a set O ∈ F such that ∣O ∩ {a, b}∣ = 1, i.e. Fa ≠ Fb. A family is called normalized if it
is a separating union-closed family such that ∅ ∈ F and ∣F∣ = ∣U (F)∣ + 1. We will call it
n-normalized to mean that ∣U (F)∣ = n. Setting [n] = {1, 2, . . . , n}, a simple example of an
n-normalized family is given by the n-staircase family {∅, [1], . . . , [n]}. Another example
is the family {∅} ∪ {[n] \ {a} ∶ a ∈ {2, 3, . . . , n}} ∪ {[n]}.
We write U¬a instead of U (F¬a) when the family involved is clear, which is thus the set
of all elements belonging to some set of F that does not contain a. The following results
show that normalized families are the smallest possible families that are both separating and
union-closed.
 4

Lemma 2.1. A family F is separating if and only if U¬a ≠ U¬b, for all a ≠ b ∈ U (F).

Proof. Suppose F is separating and let a ≠ b ∈ U (F). Without loss of generality, there is a
set O ∈ F such that a ∈ O and b /∈ O. Then, a ∈ O ⊆ U¬b and a /∈ U¬a. Hence, U¬a ≠ U¬b.
Conversely, if F is not separating, there are a ≠ b ∈ U (F) such that Fa = Fb. Thus,
F¬a = F¬b, and therefore U¬a = U¬b.

Proposition 2.2. A separating union-closed family of sets F with a universe with n elements
has at least n sets. If, moreover, F is normalized, then there is a ∈ U (F) such that U¬a = ∅,
i.e. a belongs to every non-empty set in F.

Proof. Since F is union-closed, then U (F) ∈ F and U¬a ∈ F, for all a ∈ U (F) such that
Fa ≠ F. Also, from the fact that F is separating, it follows that there can only be at most
one a ∈ U (F) such that Fa = F and so, by the previous proposition, we have that F has at
least n sets, and at least n + 1 in case there is no element belonging to all sets.
When F is normalized, since we require that ∅ ∈ F, if there was no element belonging to
every non-empty set in F, then there would be at least n + 2 elements in F, by the argument
in the last paragraph.

We now present a generalization of the concept of separation in union-closed families,
which we call independence: we can think of it as a form of a weak separation between
elements and sets. Independent families will have a relevant role later in this paper.

Definition 2.3. A family F of sets is called independent if, for all a ∈ U (F) and for all
S ⊆ U (F) \ {a}, one of the following conditions holds:

• there is a set O ∈ F¬a such that O ∩ S ≠ ∅;

• there is a set O ∈ Fa such that O ∩ S = ∅.

We say that a family is dependent if it is not independent.

It is easy to see by the definition, that independent families are in particular separating,
by just taking ∣S∣ = 1. We now present a characterization of independence that will become
useful in Section 4.

Lemma 2.4. A family F of sets is dependent if and only if there exist a ∈ U (F) and
S ⊆ U (F) \ {a} such that Fa = ⋃
b∈S Fb.
 5

Proof. Let F be a dependent family of sets. Then there exist a ∈ U (F) and S ⊆ U (F)\{a}
such that, given any set O ∈ F, we have that a ∈ O if and only if O ∩ S ≠ ∅. So, for
O ∈ Fa, we have that O ∩ S ≠ ∅, thus we may take some element b ∈ O ∩ S to conclude
that O ∈ Fb. Therefore, Fa ⊆ ⋃b∈S Fb. Now, if O ∈ Fb for some b ∈ S, that means that
b ∈ O ∩ S, and so, in particular, O ∩ S ≠ ∅, from which it follows that a ∈ O. This shows
that ⋃b∈S Fb ⊆ Fa.
Conversely, suppose there exists a ∈ U (F) and S ⊆ U (F)\{a} such that Fa = ⋃b∈S Fb.
Let O ∈ F. If a ∈ O, then there exists b ∈ S such that O ∈ Fb, from which it follows
that O ∩ S ≠ ∅; if a /∈ O, then, for all b ∈ S, O /∈ Fb, and so O ∩ S = ∅. Hence, F is
dependent.

Proposition 2.5. To prove Frankl’s conjecture, it suffices to show it holds for independent
families.

Proof. Let F be a dependent union-closed family of sets. Then, by the previous proposition,
there are a ∈ U (F) and S ⊆ U (F) \ {a} such that Fa = ⋃
b∈S Fb. If we consider the family

F ′ = F ⊖ {a}, we have that ∣F ′∣ = ∣F∣, because if that was not the case, then there would
be sets O, O ∪ {a} ∈ F such that a /∈ O. But then, O ∪ {a} ∈ Fa implies that there is some
b ∈ S belonging to O, and so, O ∈ Fb ⊆ Fa, a contradiction. Hence, if Frankl’s conjecture
holds for F ′, then it holds for F. The family F ′ might not be independent, but if that is the
case we continue this process, which will eventually stop in an independent family, as the
cardinality of the universe decreases in each iteration.

As mentioned in the introduction, some different formulations of the union-closed sets
conjecture arose in different branches of mathematics. Out of those different formulations,
one that seems very surprising and also, so far, surprisingly unfruitful is the Salzborn for-
mulation that only refers to normalized families, a very restrict subclass of union-closed
families.

Conjecture 2.6 (Salzborn formulation). If a finite family of sets F is normalized, then
there is an irreducible set of size at least ∣F∣
2 , i.e.

∃ I ∈ J(F) ∶ ∣I∣ ≥ ∣F∣
2 .

Y. Jiang proposed, in [13] (the link is no longer available), the following generalization
of the Frankl conjecture:
 6

Conjecture 2.7. Let F be a union-closed family of sets such that n = ∣U (F)∣. Then, for
any positive integer k ≤ n, there exists at least one set S ⊆ U (F) of size k that is contained
in at least 2
−k∣F∣ of the sets in F.

This conjecture is, in principle, not easier to prove, but it might be useful in finding
eventual counterexamples to the problem. It turns out that it is, in fact, equivalent to
Frankl’s conjecture. The equivalence is not hard to see, but since we have not found it
stated in the literature, we include it here.

Proposition 2.8. Let F be a union-closed family of sets with n = ∣U (F)∣. If the union-
closed sets conjecture holds, then for any positive integer k ≤ n there are sets Sk ⊆ U (F)
such that ∣Sk∣ = k, Sk ⊆ Sk+1, and such that Sk is contained in at least 2−k∣F∣ of the sets in
F. In particular, in that case, Conjecture 2.7 also holds.

Proof. We proceed by induction on k. The case k = 1 is trivial, since in this case Conjec-
ture 2.7 reduces to the union-closed sets conjecture. Now, assume that we have some set
Sk ⊆ U (F) such that Sk is contained in at least 2−k∣F∣ of the sets in F and consider the
family G = {F ∈ F ∶ Sk ⊆ F }. We know that ∣G∣ ≥ 2
−k∣F∣, and it is clear that G is union-
closed. Now, take the family G ⊖Sk = {G\Sk ∶ G ∈ G}. This new family is still union-closed:
if A, B ∈ G ⊖ Sk, then (A ∪ Sk) ∪ (B ∪ Sk) = (A ∪ B) ∪ Sk ∈ G, and A ∪ B ∈ G ⊖ Sk.
Also, clearly, ∣G ⊖ Sk∣ = ∣G∣. Since we assume the union-closed sets conjecture is valid,
we know there exists an element x ∈ U (G ⊖ Sk) ⊆ U (F) \ Sk such that x is in at least
∣G⊖Sk∣
2 = ∣G∣
2 ≥ 2−(k+1)∣F∣ sets. Now just take Sk+1 = Sk ∪ {x}. We have ∣Sk+1∣ = k + 1, and

Sk+1 is contained in at least 2−(k+1)∣F∣ of the sets in F.

3 Generalized topologies and Frankl’s conjecture

A set X together with a union-closed family F ⊆ P(X) was named a supratopological space
when X ∈ F in [16]; a generalized topological space if ∅ ∈ F in [8]; and a strong generalized
topological space, e.g. in [18], when ∅, X ∈ F. Many topological notions can readily be
extended to this more general setting. For example, and this will be relevant later, calling
the elements of F open sets, and their complements closed sets, the interior of a subset A ⊆ X
is, as usual, the biggest open set contained in A, i.e. the set A◦ = ⋃{O ∈ F ∶ O ⊆ A}, which
is open, as F is union-closed. Note that, trivially, A
◦◦ = A
◦. Similarly, the closure of A is
the smallest closed set containing A, which is ¯A = ⋂{C closed ∶ A ⊆ C} = X \ (X \ A)◦.
In this setting, the union-closed sets conjecture has the following reformulation.

7

Conjecture 1.1 (Frankl’s conjecture, topological reformulation). If (X, F) is a finite supratopo-
logical space, then there is a point that belongs to at least half the open sets.

Note that, in this context, Fx is the set of all neighborhoods of x, and one can also state
the Frankl conjecture as: there is a point whose neighborhoods consist of at least half of all
open sets.
There are several separation axioms that are quite pertinent for our purposes, specially
axioms between T0 and T1, that we will shortly recall from [2], to which we join the axiom
that we introduced above, in Definition 2.3, and we separate as an axiom a condition in the
definition of TDD from [2]. Those axioms originated in the context of topological spaces, but
they carry over to supratopological spaces without changes. However, there are relations
among them that no longer hold, as we will point out. In particular, some do not remain
between T0 and T1.
To state the axioms, it is convenient to denote the closure of {x} by ¯x, for any given point
x ∈ X of a supratopological space, and we will call the shadow 1 of x to the set ˙x = ¯x \{x}.
It is easy to see that, with our notations, ¯x = {y ∈ X ∶ Fy ⊆ Fx} = X \ U¬x. Also, following
[2], given two subsets, A and B, of a supratopological space X, we say that A is weakly
separated from B, which we denote by A ⟝ B, if there is an open set O of X such that
A ⊆ O and B ∩ O = ∅. When dealing with a singular set, we will often write x for {x}. It
is easy to see that ¯x = {y ∈ X ∶ y /⟝ x}.
In [2], the set ˆx = {y ∈ X ∶ x /⟝ y} is called the kernel of x, and ⌢
x = ˆx \{x} the shell of
x. It is easy to see that ˆx = {y ∈ X ∶ Fx ⊆ Fy} = {y ∈ X ∶ x /∈ U¬y}, the set of all elements
y that dominate x, in the language of [5].
We prefer the name “supratopological” because it directly suggests that the family of
open sets is union-closed, but, from now on, to simplify matters and because it really
does not make much difference, we assume that a supratopological space always contains the
empty set.

Definition 3.1 (Separation Axioms). A supratopological space (X, F) is

• T0 if, for any x ≠ y ∈ X, either x ⟝ y or y ⟝ x, which is equivalent to Fx ≠ Fy.

• TI if F is independent, as specified above in Definition 2.3. Of course, TI ⊆ T0.

• TUD if ˙x is a union of disjoint closed sets, for all x ∈ X. This is equivalent to require
that, for all x ∈ X, U¬x ∪ {x} is a intersection of open sets whose pairwise union is X.

1In [2] this set is denoted by [x]′ and called the derived set of x.

8

• TD if ˙x is closed, for all x ∈ X. This is equivalent to demand that, for all x ∈ X, there
is O ∈ F such that O ∪ {x} ∈ F, which turns out to be equivalent to U¬x ∪ {x} ∈ F.
Clearly, TD ⊆ TUD.

• TiD if, for all x ≠ y ∈ X, ˙x ∩ ˙y = ∅, which is equivalent to {x, y} ∪ U¬x ∪ U¬y = X.

• TDD = TD ∩ TiD.

• TF if, for all x ∈ X and finite S ⊆ X \ {x}, either x ⟝ S or S ⟝ x.

• TFF if, for any pair of finite disjoint sets S1, S2 ⊆ X, either S1 ⟝ S2 or S2 ⟝ S1. Of
course, TFF ⊆ TF.

• TY if, for all x ≠ y ∈ X, one has ∣¯x∩ ¯y∣ ≤ 1. This is equivalent to either U¬x ∪U¬y = X,
or U¬x ∪ U¬y = X \ {z} for some z ∈ X, for each pair x ≠ y.

• TYS if, for all x ≠ y ∈ X, one has ¯x ∩ ¯y ∈ {∅, {x}, {y}}. This is equivalent to
U¬x ∪ U¬y ∈ {X, X \ {x}, X \ {y}}. It is clear that TYS ⊆ TY ∩ TiD.

• T1 if, for all x ≠ y ∈ X, one has Fx \ Fy ≠ ∅. This is equivalent to {x} is closed, for
all x ∈ X, or U¬x = X \ {x}. It immediately follows that T1 ⊆ TYS.

Examples:

• The indiscrete supratopology on X, given by F = {∅, X}, is not T0 when ∣X∣ ≥ 2, but
it is TiD when ∣X∣ = 2, and thus TiD /⊆ T0.

• Let us denote by (X
k ) the set of all subsets of the set X with k elements, and by ( X
≥k)
the set of all such subsets with at least k elements, which is a union-closed family.
Note that ⟨(X
k )⟩ = ( X
≥k) ∪ {∅}. The supratopological space given by ([4], ⟨([4]
2 )⟩) is a
finite non-discrete T1 space, something that cannot exist in the topological case.

• The n-staircase family {∅, [1], . . . , [n]} is TD but not T1.

• The space X = [4] with the supratopology given by F = ⟨{1, 2}, {3, 4}⟩ is TiD but not
TUD.

• For n ≥ 3, the family {∅} ∪ {[n] \ {a} ∶ a ∈ {2, 3, . . . , n}} ∪ {[n]} is TUD but not TD.

• The space X = [5] with the supratopology given by

F = {∅, {1, 2, 3}, {1, 4, 5}, {1, 2, 3, 4, 5}}

is TUD but not T0.
 9

• The space X = [3] with the supratopology given by F = {∅, {1, 2}, {1, 3}, {1, 2, 3}} is
TYS but not TI.

• The space X = [4] with the supratopology given by the family

F = {∅, {1, 2}, {2, 3}, {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {1, 2, 3, 4}}

is TDD but not TF.

Remarks:

• The notion of T0 corresponds exactly what it is called “separating” in the union-closed
literature, as we did in the previous section. One can now give a topological proof of
Lemma 2.1: when (X, F) is T0, the map X → F given by x ↦ X \ ¯x is injective.

• If X is not T0, then there exist x ≠ y ∈ X such that ¯x = ¯y, and hence {x, y} ⊆ ¯x ∩ ¯y.
This shows that TY ⊆ T0.

• We will see below that TD ⊆ TI ⊆ T0.

• TDD = TiD ∩ TD, by definition, and TDD = TiD ∩ TI, by Proposition 3.6 below.

• T1 /⊆ TFF: the space X = [4] with F = ⟨(
[4]
3 )⟩ is T1 but not TFF.

• TiD ∩ T0 ⊆ TYS.

• For topological spaces, one has the following relations (see [2]):

T1 ⊊ TDD ⊊ TD ⊊ TUD ⊊ T0;

T1 ⊊ TFF ⊊ TY ⊊ TF ⊊ TUD;

T1 ⊊ TDD ⊊ TYS ⊊ TY.

Some of these do not hold for supratopological spaces, as they depend on the fact
that the intersection of open sets is still open, which is not required to hold in a
supratopological space. One can see that in this case the relations are as depicted in
Figure 1, where all inclusions are straightforward by the definitions involved, except:

– (1) holds when ∅ /∈ F, which we assumed to be the case in supratopological
spaces.

– (2) and (3) follow easily from the fact that in a TF space all points are either open
or closed, which can be proved in an analogous way as Proposition 3.7 below.

10

T0

TI TUD

TD

TY TiD TF

TYS TDD TFF

T1

(4)
 (3)

(2)

(1)

Figure 1: Hasse diagram for the separation axioms in supratopological spaces

– (4) is the content of Proposition 3.4 below.

We leave to the reader the verification that the examples given above show that there
are no extra line segments in the diagram, as well as to verify that all inclusions are
indeed strict.

It is well known that it suffices to verify Frankl’s conjecture for T0 families. In fact, it is
easy to see that one can suppose the union-closed family to have, for every a ∈ U (F), an
a-problematic set, which is a set O ∈ F such that O ∪ {a} ∈ F. The paper by Lo Faro [10]
can be used as a reference for this result. This means:

Proposition 3.2. To prove the Frankl conjecture, it suffices to do it for TD supratopological
spaces.

We can go even further and assume F has at least 3 a-problematic sets for each a ∈ U (F)
(cf. [7, Corollary 3.1.11]):

Theorem 3.3. It suffices to prove the Frankl Conjecture for families F having at least three
a-problematic sets for each a ∈ U (F).

Proof. Suppose that the Frankl Conjecture does not hold, and let F be a minimal coun-
terexample to the conjecture with respect to the number of sets and with minimal universe
size among the counterexamples with ∣F∣ sets. Let a ∈ U (F) and

Πa = {O ∈ F¬a ∣ O ∪ {a} ∈ F}

11

be the subfamily of a-problematic sets of F. By minimality of F, we know that Frankl’s
Conjecture holds for F ′ = F ⊖ {a}, and so, ∣F ′∣ = ∣F∣ − ∣Πa∣ < ∣F∣ and Πa ≠ ∅. This
implies that U¬a ∈ Πa, as, taking O ∈ Πa, we have that U¬a ∪ {a} = U¬a ∪ (O ∪ {a}) ∈ F.
Let b ∈ U (F ′) be an element belonging to at least ∣F ′∣
2 sets of F ′, i.e., such that

∣F ′
b∣ ≥ ∣F∣ − ∣Πa∣
2 . (1)

As the element b belongs to at least half the sets in F ′ and F¬a ⊆ F ′ is a subfamily such
that ∣F¬a∣ ≥ ∣F ′∣
2 , b must belong to U¬a ∈ Πa. In particular, ∣(Πa)b∣ ≥ 1.
Since F is a counterexample to Frankl’s Conjecture, we have that

∣F ′
b∣ + ∣(Πa)b∣ = ∣Fb∣ < ∣F∣
2 . (2)

Combining (1) and (2), we get that

∣F∣ − ∣Πa∣
2 + ∣(Πa)b∣ < ∣F∣
2 ,

and so ∣Πa∣ > 2∣(Πa)b∣ ≥ 2.

Notice that the existence of an a-problematic set for each a ∈ U (F) implies separation,
since for a, b ∈ U (F), taking O, O ∪ {a} ∈ F, if b ∈ O, then O separates a from b; if not
then O ∪ {a} does. That is, TD ⊆ T0. The concept of independence lies somewhere between
T0 and TD, as we will now see, and which provides an alternative way to obtain the result
in Proposition 2.5.

Proposition 3.4. Every TD union-closed family is independent, i.e. TD ⊆ TI.

Proof. Suppose that F is dependent. In view of Lemma 2.4, there are a ∈ U (F) and
S ⊆ U (F) \ {a} such that Fa = ⋃
b∈S Fb. This means that F has no a-problematic sets, since,

if there was an a-problematic set O, then there would be some b ∈ S belonging to O ∪ {a},
which means that b ∈ O and that contradicts the fact that Fb ⊆ Fa. Therefore, F is not a
TD family.

It is proved in [11, Corollary 2] that, if F is a minimal counterexample to the Frankl
Conjecture, then, for all z ∈ U (F), 1 ≤ ∣ˆz∣ ≤ 2, i.e. ∣ ⌢
z∣ ≤ 1. This implies that F satisfies the
axiom TiD: given x, y ∈ U (F), we have that for every element z ∈ U (F) \ {x, y}, it cannot
happen that both x and y belong to ⌢
z, thus z ∈ U¬x ∪U¬y, and so {x, y}∪U¬x ∪U¬y = U (F).
This shows:
 12

Proposition 3.5. It suffices to prove the Frankl conjecture for TiD families

As noted above, the condition TiD is not sufficient for a family to be TDD. However, the
following holds.

Proposition 3.6. Let X be a set endowed with a supratopology F. If (X, F) satisfies TiD
and TI, then (X, F) is TDD.

Proof. Let (X, F) be TI supratopological space satisfying TiD, and x ∈ X. We want to prove
that U¬x ∪ {x} ∈ F. If U¬x = X \ {x}, we are done since X ∈ F. If not, then ˙x ≠ ∅. Notice
that, if y ∈ ˙x, then any open set containing y must also contain x, since y /∈ U¬x. That is,
⋃y∈ ˙x Fy ⊆ Fx. Since (X, F) is TI, the previous inclusion has to be strict, and hence there
must exist some S ∈ Fx disjoint from ˙x = X \ (U¬x ∪ {x}), which implies that S ⊆ U¬x ∪ {x}.
But then U¬x ∪ {x} = S ∪ U¬x ∈ F.

We finish this section by showing that the separation axiom TFF is strong enough to
imply Frankl’s conjecture.

Lemma 3.7. Let (X, F) be a supratopological space. Then (X, F) is TFF if and only if
every S ⊆ X is either open or closed.

Proof. Assume that (X, F) is TFF and let S ⊆ X. Then, there must be O ∈ F such that
S ⊆ O and (X \ S) ∩ O = ∅, and so S = O, in which case S is open; or X \ S ⊆ O and
S ∩ O = ∅, and so O = X \ S, in which case S is closed.
Now, assume that every S ⊆ X is either open or closed, and let S1, S2 ⊆ X be disjoint. If
S1 is open, then taking O = S1 in the definition of TFF, we get that S1 ⊆ O and O ∩ S2 = ∅.
If, on the other hand, S1 is closed, then taking O = X \ S1, we obtain that S1 ∩ O = ∅ and
S2 ⊆ O, so (X, F) is TFF.

Proposition 3.8. Let F be a finite TFF union-closed family of sets. Then the Frankl
Conjecture holds for F.

Proof. It follows from Lemma 3.7 that, for a TFF union-closed family F ⊆ P([n]), we have
that ∣F∣ ≥ 2n−1, and so Frankl’s Conjecture holds by [15].

4 Dual and normalized families

The notion of dual family was introduced in [14], and a similar notion was used in [25] to
prove the equivalence between the usual formulation of Frankl’s conjecture and the Salzborn

13

formulation. The main difference between those two notions is that, in [14], the sets of the
notion presented in [25] are replaced by their indexes, and the empty set is not included.
Also, the definition in [14] uses a minimal generating set, while the definition in [25] uses any
generating set. We use the notion introduced in [14], with some small variations. We will
describe the construction of the dual of a given family, illustrate it with examples, and give
some of its basic properties. We then give some structural results on normalized families,
and highlight their relation with Frankl’s conjecture.
Consider an indexed subfamily H = {H1, . . . , Hs} of distinct non-empty sets in P([m])
with U (H) = [m]. For each j ∈ [m], set

Hιj = {i ∈ [s] ∶ j ∈ Hi} ∈ P([s]),

i.e., Hιj is the set of indices of sets in H to which j belongs, and put

Hι = {Hι1, . . . , Hιm}.

Moreover, for any A ⊆ [m], set

HιA = {i ∈ [s] ∶ A ∩ Hi ≠ ∅} = ⋃

j∈A Hιj .

Note that HιA∪B = HιA ∪ HιB . Also, note that

Hιι = H, since j ∈ Hιιi ⟺ i ∈ Hιj ⟺ j ∈ Hi. (3)

The choice of indices for the sets in H is irrelevant, as a different choice just induces a
permutation of elements on the subsets of P([m]), and one simply obtains an isomorphic
family.
Now, given any subset L of P([m]), we define L
∗ as the union-closed family generated
by Hι, where H = L \ {∅} is indexed in some way. From what was noted above, L∗ = {HιA ∶
A ⊆ [m]}. The special cases L = F and L = J(F) will be particularly relevant. The family
F ∗ is called the dual family of F.

Remark 4.1. Note that F ιA is the set consisting of the indices of the sets in FA, and thus,
in particular, ∣F ιA∣ = ∣FA∣.

It is clear from the definitions that ∣U (L
∗)∣ = ∣L∣ − εL, , where

εL = {0, if ∅ /∈ L,
1, otherwise.

14

and that L
∗ is separating.
The next proposition gives a procedure to build examples of normalized families, and,
in fact, as we will see below, this procedure yields all normalized families. The result is
equivalent to one contained in [25, Lemma 2.2], but the context is a bit different, and so we
provide a complete proof which underlies its topological nature.

Proposition 4.2. Let F be a union-closed family, and G be a generating subfamily. Then
∣G∗∣ = ∣F∣ + 1 − εF . In particular, we have that F ∗ is a normalized family.

Proof. Set U = U (F) = [m], and G \ {∅} = {H1, . . . , Hs}. As pointed out above, G∗ =
{HιA ∶ A ⊆ [m]}, and therefore G∗ = {HιU \A ∶ A ⊆ [m]}. Now, HιU \A = HιU \B is equivalent
to saying that ∀i ∈ [s] (U \ A) ∩ Hi ≠ ∅ ⟺ (U \ B) ∩ Hi ≠ ∅,

which, of course, is the same as

∀i ∈ [s] (U \ A) ∩ Hi = ∅ ⟺ (U \ B) ∩ Hi = ∅,

or ∀i ∈ [s] Hi ⊆ A ⟺ Hi ⊆ B.

But this is equivalent to A◦ = B◦, since G is a generating family for F. It follows from
this that G∗ = {HιU \A◦ ∶ A ⊆ [m]} = {HιU \O ∶ O ∈ F ∪ {∅}}, and that the elements of
this last set are distinct, which proves first the claim. The second one is now very easy to
establish.

Example 4.3. Suppose we want to construct a 6-normalized family. To do so, we need
a union-closed family with 7 sets (or only 6, if the the empty set is excluded). Take, for
example: F = P([3])\{{1}} = {∅, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

One has F ι1 = {3, 4, 6}, F ι2 = {1, 3, 5, 6} and F ι3 = {2, 4, 5, 6}. Now, we simply build

F ∗ = ⟨{3, 4, 6}, {1, 3, 5, 6}, {2, 4, 5, 6}⟩

= {∅, {3, 4, 6}, {1, 3, 5, 6}, {2, 4, 5, 6}, {1, 3, 4, 5, 6}, {2, 3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}},

which is 6-normalized.

The following technical lemma gives us two properties that will be useful later on.

Lemma 4.4. Let F be a union-closed family and G be a generating subfamily. We have the
following:
 15

1. if F is independent, then J(G∗) = Gι, ∣J(G∗)∣ = ∣U (F)∣ and J(F ∗)∗ = F.

2. if F is normalized, then Gι is union-closed.

Proof. Let F be an independent union-closed family and put U (F) = [m]. Clearly, in G∗

only the sets in Gι may be irreducible. Let G \ {∅} = {H1, . . . , Hs}. If Hιc = Hιa ∪ Hιb,
for some a, b, c ∈ [m], then, since G is generating, it would follow that Fc = Fa ∪ Fb, which
contradicts independence by Proposition 2.4. This shows that J(G∗) = Gι.
Also, since F is independent (in particular, separating), the sets Hιj are all distinct, and
so we have that ∣J(G∗)∣ = ∣Gι∣ = m. Now, from what was proven in the last paragraph, we
know that J(F ∗) = (F \ {∅})
ι and so J(F ∗)
∗ = ((F \ {∅})ι)∗ = ⟨(F \ {∅})ιι⟩ = F. This
completes the proof of the first claim.
Finally, let F be an n-normalized family. Then, by the previous lemma, ∣G∗∣ = n + 1 =
∣U (F)∣ + 1 = ∣Gι∣ + 1, since F is separating. This means that G∗ = Gι ∪ {∅}, and thus Gι

is union-closed.

We can use this lemma to show that there is, up to bijection, only one independent
normalized family, while by definition all normalized families are separating. This implies
that the concept of independence is stronger than the concept of separation, i.e. T0 /⊂ TI.

Proposition 4.5. The only independent n-normalized family is the staircase family N =
{∅, [1], . . . , [n]}, up to bijection.

Proof. It is easy to see that the staircase family is independent for every n ∈ N. Now let
N be an independent n-normalized family of sets. By the previous lemma, it follows that
J(N ∗) is union-closed and all its sets are, of course, irreducible. Let X, Y ∈ J(N ∗). Then,
X ∪ Y ∈ J(N ∗) is an irreducible set, and so either Y ⊆ X or X ⊆ Y . Therefore J(N ∗) is
a chain. Now, the previous lemma also implies that N = J(N ∗)
∗. But it is easily seen that
the dual of a chain is still a chain, and that there is only one separating chain of sets with a
given universe, up to bijection.

The next two propositions show that any n-normalized family can be obtained as the
dual of an independent family.

Proposition 4.6. Let N be a normalized family. Then N = J(N )
∗∗.

Proof. Let N be an n-normalized family and set H = J(N ) = {H1, . . . , Hs}. We have
J(N )
∗ = ⟨Hι1, . . . , Hιn⟩ . From Proposition 4.2 it follows that ∣J(N )
∗∣ = ∣N ∣ = n + 1, since
here N contains the empty set. Hence J(N )
∗ = {∅, Hι1, . . . , Hιn}. But then

J(N )
∗∗ = ⟨Hιι1, . . . , Hιιn⟩ = ⟨H1, . . . , Hn⟩ = N ,

16

by (3). This proves the claim.

Proposition 4.7. If N be a normalized family of sets, then J(N )∗ is independent. It
follows that any normalized family is the dual of an independent family.

Proof. In view of the previous Proposition, is enough to show that L = J(N )∗ is indepen-
dent. Assume this is false, so that, from Lemma 2.4, and using the notations in the previous
proof, there would exist a ∈ [s] and S ⊆ [s] \ {a} such that

La = ⋃

b∈S Lb. (4)

But Hιj ∈ La ⟺ a ∈ Hιj ⟺ j ∈ Ha, and so one sees that (4) is equivalent to
Ha = ⋃
b∈S Hb, which contradicts the fact that the Hi are irreducible.

Example 4.8. Let N be the following 7-normalized family:

N = {∅, {1, 4, 6, 7}, {2, 5, 6, 7}, {3, 4, 5, 6}, [7] \ {3}, [7] \ {2}, [7] \ {1}, [7]}.

We have that J(N ) = {{1, 4, 6, 7}, {2, 5, 6, 7}, {3, 4, 5, 6}}. Let us compute J(N )
∗∗ and see
that it coincides with N , as Proposition 4.6 claims. To start with,

J(N )
∗ = ⟨{{1}, {2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {1, 2}}⟩

= {∅, {1}, {2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {1, 2}}.

It follows that J(N )
∗∗ = ⟨∅, {1, 4, 6, 7}, {2, 5, 6, 7}, {3, 4, 5, 6}⟩ = N .

It is now very easy to show that the original form of the union-closed sets conjecture
and its Salzborn formulation are equivalent. We state this result in a from that explicitly
exhibits the families involved in the equivalence.

Theorem 4.9 (Salzborn Formulation, [25]). If N is a normalized family and the indepen-
dent family J(N )
∗ satisfies the union-closed sets conjecture, then N satisfies the Salzborn
formulation of the conjecture. If F is an independent union-closed family such that F ∗ sat-
isfies the Salzborn formulation of the conjecture, then F = J(F ∗)∗ satisfies the union-closed
sets conjecture.

Proof. Let N be an n-normalized family, and J(N ) = {I1, . . . , Is}. We saw in the proof
of Proposition 4.6 that J(N )
∗ = J(N )
ι ∪ {∅}. The hypothesis that this set satisfies the
union-closed sets conjecture entails that there is an element a ∈ U (J(N )∗) in at least half
the sets of J(N )∗. Now, by the definition of J(N )ι, we have that a ∈ J(N )ιj ⟺ j ∈ Ia.

17

Therefore, if we have a in at least n
2 sets of J(N )
∗, we have ∣Ia∣ ≥ n
2 , and so N satisfies the
Salzborn formulation of the union-closed sets conjecture.
To prove the second statement, let F be an independent union-closed family. We know by
Lemma 4.4 that F = J(F ∗)∗. By Proposition 4.2, F ∗ is normalized, and so, by Lemma 4.4,
J(F ∗)
ι is union-closed. Therefore, every set in F = J(F ∗)∗ is of the form J(F ∗)ιj . Now, if
F ∗ satisfies the Salzborn condition, then, there exists I ∈ J(F ∗) with ∣I∣ ≥ 1
2∣F ∗∣, and thus
∣I∣ ≥ 1
2∣F∣, by Proposition 4.2. Let i be the index of I in J(F ∗) used when one constructs
J(F ∗)
∗ = F. Then, since k ∈ I ⟺ i ∈ J(F ∗)
ιk, it follows that i belongs to at least half
of the sets in F.

We saw in Proposition 2.2 that, in a normalized family, there is an element in all of its
non-empty sets, which must be unique since the family is, by definition, separating.

Definition 4.10. Given a normalized family N , we will denote by aN the unique element
belonging to all of its non-empty sets.

We are now ready to present one of the main results of this paper, which introduces a
reduction process for normalized families.

Theorem 4.11. Let N be a n-normalized family and let M be any minimal non-empty set
of N . Then the family N ′ = (N \ {M }) ⊖ {aN } is (n − 1)-normalized.

Proof. Note that if {aN } ∈ N , then M = {aN }, and N ′ = N ⊖ {aN }. We claim that
the family N ′ is (n − 1)-normalized. It is clear that N ′ is union closed, ∅ ∈ N ′, and
∣N ′∣ = ∣N ∣ − 1. It remains to show that ∣U (N ′)∣ = ∣U (N )∣ − 1 and that N ′ is separating.
In case {aN } ∈ N , it is clear that ∣U (N ′)∣ = ∣U (N )∣ − 1. Also, for x, y ∈ U (N ′), if
N ∈ N is such that x ∈ N , y /∈ N , then for N ′ = N \ {aN } ∈ N ′ it is still true that x ∈ N ′,
y /∈ N ′.
Let us now deal with the case {aN } /∈ N , which implies ∣M ∣ ≥ 2. Clearly ∣U (N ′)∣ ≤ n−1.
Now, ∣U (N ′)∣ < n − 1 would imply the existence of an element in M not in any other set of
N \ {M }, thus M = U (N ), and N = {∅, M }, but then ∣M ∣ = 1, a contradiction. Therefore,
∣U (N ′)∣ = n − 1.
Finally, let x, y ∈ U (N ′) = U (N ) \ {aN }. Since N is separating, there exists N ∈ N
such that ∣N ∩ {x, y}∣ = 1. It is, of course, still true that N ′ = N \ {aN } separates x
from y. If N ′ ≠ M \ {aN }, we are done. It remains to consider the case where M is the
only set that separates x from y in N . In this case, there cannot be any set ∅ ≠ L ∈ N
such that {x, y} /⊆ L, otherwise L ∪ M would also separate x and y, and by the minimality
of M , M ∪ L ≠ M . So, except for M , all other sets of N must contain {x, y}. Without

18

loss of generality, we may assume that x ∈ M . It follows that x belongs to all sets of N ,
contradicting the uniqueness of the element aN .

Corollary 4.12. For every normalized family N there are distinct elements ai ∈ U (N ) with
frequency at least i, for all 1 ≤ i ≤ n.

Proof. Follows directly from the Proposition 2.2 by applying Theorem 4.11 repeatedly.

Notice that in the reduction from N to N ′ we remove a minimal set. To preserve closure
under union we can only remove irreducible elements of the family. While it may be possible
to weaken the condition of minimality, it can not be replaced with irreducibility, in general,
as the next example shows.

Example 4.13. Take the normalized family

N = {∅, {5, 7}, {3, 6, 7}, {3, 5, 6, 7}, {2, 4, 5, 6, 7}, [7] \ {2}, [7] \ {1}, [7]}.

Then using the irreducible set M = [7] \ {2} one gets

N ′ = {∅, {5}, {3, 6}, {3, 5, 6}, {2, 4, 5, 6}, [6] \ {1}, [6]}

which is not separating, as no set separates 2 from 4.

Given an n-normalized family N , we can decompose it as N = Sλ0 ∪ Sλ1 ∪ . . . ∪ Sλs, with
λ0 < λ1 < ⋯ < λs, where Sℓ is the set of all subsets of N with ℓ elements. We set ki = ∣Sλi∣.
Since ∅ ∈ N , one has that λ0 = 0 and k0 = 1. Note that ∣S1∣ ≤ 1. We have the following
corollary by applying Proposition 2.2 to all possible reductions.

Corollary 4.14. Let N be an n-normalized family. Then, using the notations such defined,

there are ki elements with frequency at least n −
 i−1
∑
j=0 kj, for all 0 ≤ i ≤ s.

Proof. Let M1 and M2 be two minimal sets of N , and set N ′
i = (N \ {Mi}) ⊖ {aN }, for
i = 1, 2. If aN ′
1 = aN ′
2, then this element, which is distinct from aN , would be in all sets of
N , contradicting the uniqueness of aN . The claim follows easily from this, by reducing N
by successively removing sets of minimal length.

Using the reduction process introduced in Theorem 4.11 for normalized families, one can
introduce a reduction process for arbitrary union-closed families as follows. Given such a
family F, we will call F↓ = J((F ∗)′)∗ a child of F. It depends on the minimal set chosen
to be removed from F ∗ to form (F ∗)
′, and different choices may lead to non-isomorphic

19

families, but we do not include it in the notation, which would become a bit too heavy.
However, please keep in mind that there may several distinct children of a family, and F↓
just denotes one of them. Naturally, F is called a parent of F↓. Children of the same parent
are referred as siblings, and a family obtained by successive reductions from a given family
of sets is called a descendent of that family.
Note that it follows from the results seen above that ∣F↓∣ = ∣F∣ − 1, when F contains
the empty set, which will assume from now on. As usual, we define, F↓↓ = (F↓)↓, etc., and
F↓k = (F↓(k−1))↓, which again may depend on various choices of minimal sets, not conveyed
by the notation. One has ∣F↓k∣ = ∣F∣ − k. The families F↓k, for k ∈ N, are the descendents
of the family F. It follows from Proposition 4.7 that, for any family, all its descendents are
independent.
The relation between the family F and a family F↓ seems rather mysterious, in the sense
that they may have different universes, and even when the universe is the same the relation
between them does not seem to be evident.

Example 4.15. Consider again the union-closed family F of Example 4.3,

F = {∅, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

There is only one minimal set in F ∗, namely {3, 4, 6}. It yields:

(F ∗)′ = {∅, {1, 3, 5}, {2, 4, 5}, {1, 3, 4, 5}, {2, 3, 4, 5}{1, 2, 3, 4, 5}}.

Then J((F ∗)
′) = {{1, 3, 5}, {2, 4, 5}, {1, 3, 4, 5}, {2, 3, 4, 5}}, and thus

F↓ = J((F ∗)
′)∗ = {∅, {1, 3}, {2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}},

which looks quite different from the original family.

We can picture the two parallel reduction processes in the following commutative diagram
(the left dashed up arrow commutes with the others when F is an independent family):

J((F ∗)
′)
∗

F F↓ F↓↓ F↓k

F ∗ (F ∗)′ (F ∗)
′′ (F ∗)(k)

(F↓)
∗

□↓

□
∗
 □
′
 □∗◦J (5)

20

where the down arrows in the middle are given by the “taking the dual” operator, □∗; the
right arrows on the second row are given by the reduction operator □
′; the right arrows
on the first row by the reduction operator □↓ = □
∗ ◦ J ◦ □
′ ◦ □∗; and the up arrows in
the middle by the □
∗ ◦ J operator. Note that, by Theorem 4.11 and Proposition 4.6, we
have that (F↓k)
∗ = (F ∗)
(k) (i.e. the upper arrow followed by the down arrow is the identity
operator, Id, or □
∗ ◦ □
∗ ◦ J = Id, for normalized families). From Lemma 4.4 it follows that,
for independent families, □
∗ ◦ J ◦ □∗ = Id, i.e. the down arrow followed by the up arrow is
the identity, for independent families.

Remark 4.16. If F↓k satisfies the Frankl conjecture and has an odd number of sets, then
F↓(k+1) also satisfies the conjecture. If F↓k has an even number of sets and strictly satisfies
the Frankl conjecture, meaning that there is an element in strictly more than half the sets,
then F↓(k+1) also strictly satisfies the conjecture.

Remark 4.17. Given a normalized family N , the irreducibles of N ′ = (N \ {M }) ⊖ {aN }
that do not belong to set J(N ) ⊖ {aN } have cardinality bigger that ∣M ∣.

5 Refinement of a conjecture of Poonen and descen-
dents of power sets

It is easy to see that, for any given n-normalized family N , there is always at least one family
M such that N = M′, namely the family M = {N ∪ {n + 1} ∶ N ∈ N } ∪ {∅}. Note that M
is also normalized. Now, if F is an independent family, then take M such that M′ = F ∗,
and T = J(M)∗, which is an independent family as seen in the proof of Proposition 4.7.
Then T ∗ = M, by Proposition 4.6, and thus T↓ = J((T ∗)
′)∗ = J(M ′)
∗ = J(F ∗)
∗ = F, by
Lemma 4.4. This shows that, given any independent family F there is always a family T
such that F = T↓. We will refer to this family T as the trivial parent of F. In other words,
the operator □
′ is surjective on normalized families, while the operator □↓ is surjective on
independent families. It is clear that if an independent family satisfies the Frankl conjecture,
so does its trivial parent.
Poonen conjectured in [19] that every union-closed family is either a power set or has an
element in strictly more than half the sets.

Conjecture 5.1. Let F be a union-closed family of sets. Unless F is a power set, it contains
an element that appears in strictly more than half of the sets

We propose the following seemingly weaker version of Poonen conjecture.

21

Conjecture 5.2. Let F be a union-closed family such that the most frequent element
belongs to exactly half the sets in F. Then F must be a power set.

We can now prove that these two conjectures are in fact equivalent. The advantage of
this new statement is that it only concerns families sharply satisfying Frankl’s conjecture,
apparently making no claim on the original conjecture: naturally, the non-trivial part is
proving that Conjecture 5.2 implies Frankl’s conjecture.

Theorem 5.3. Conjectures 5.1 and 5.2 are equivalent.

Proof. Clearly Conjecture 5.1 implies Conjecture 5.2. We will prove that Conjecture 5.2
implies Conjecture 1.1. This is enough since Conjecture 5.2 together with Conjecture 1.1
implies Conjecture 5.1. Assume that Conjecture 5.2 holds while Frankl’s conjecture does not.
By Theorem 4.9 there would be a family F such that F ∗ is an n-normalized counterexample
to the Salzborn formulation of the conjecture. Put λ = max{∣I∣ ∶ I ∈ J(F)}, and choose a
set I ∈ J(F) such that ∣I∣ = λ. Obviously, ∣I∣ < n+1
2 . If we consider n − 2λ + 1 successive
trivial parents of F we obtain a family T such that T = I ∪ {n + 1, . . . , 2n − 2λ + 1} is a
maximal element of J(T ) and ∣T ∣
∣T ∣ = n−λ+1
2n−2λ+2 = 1
2. By Proposition 4.6, T = J(T )∗∗. But,
as seen in Proposition 4.7, J(T )∗ is an independent family, and therefore, by Lemma 4.4
applied to F = G = J(T )
∗, we have that T ∈ J(T ) = J(J(T ∗)∗) = (J(T )∗)ι. Hence, the
largest set (J(T )∗)
ιj , for j ∈ U (J(T )
∗), is T with cardinal n − λ + 1. Hence, the most
frequent element in J(T )
∗ has frequency n − λ + 1. Using Proposition 4.2, we see that
∣J(T )
∗∣ = ∣(J(T )∗)
∗∣ = ∣T ∣ = 2n − 2λ + 2. By the hypothesis, we deduce that J(T )
∗ is a
power set, but that is absurd since, by construction, T = (J(T )
∗)∗ has a singleton.

We now prove the Frankl conjecture for families that are descendents of power set families.
To do so, we start with a technical lemma.

Lemma 5.4. Let n ≥ 6 be an integer and 2 ≤ k ≤ n
2 . Then

2
k+1 − 1 ≤
 k−1
∑

s=0 (n
s).

Proof. For k = 2 we have that 2
k+1 − 1 = 7 and ∑k−1
i=0 (
n
i) = n + 1 ≥ 7. For k = 3, we have

that 2k+1 − 1 = 15 and ∑k−1
s=0 (
n
s) = n2+n+2
2 , which is greater than 15 if n ≥ 6.
Now assume that k ≥ 4. Since the sum of each row of Pascal’s triangle is half of the sum
of the next row, and the triangle is symmetrical, we have that

2
k+1 − 1 ≤ 2
k+1 =
 k+1
∑

s=0 (k + 1
s ) ≤
 ⌊ k+2
2 ⌋
∑

s=0 (
k + 2
s ) ≤
 k−1
∑

s=0 (k + 2
s ) ≤
 k−1
∑

s=0 (n
s).

22

Theorem 5.5. If a family F is a descendent of a power set, then it satisfies the Frankl
Conjecture.

Proof. We may assume that n ≥ 6 by [11, Theorem 10].
Suppose F = P([n]), for some n, and build its correspondent normalized family N = F ∗.
Then we have ∣N ∣ = 2n, ∣U (N )∣ = 2n − 1, ∣J(N )∣ = n, and ∣I∣ = 2
n−1 for every I ∈ J(N ).
In fact, N has (n
k) distinct sets of size 2
n − 2
k, for every k = 0, 1, . . . , n, which correspond to
the sets containing the indices of the sets in FF , for F ∈ F with ∣F ∣ = k. Indeed, it is easy
to see that FF ≠ FG whenever F ≠ G, and that for every F ∈ F with ∣F ∣ = k one has

∣FF ∣ = 2
n−k k
∑

i=1 (
k
i ) = 2
n−k(2
k − 1) = 2
n − 2n−k.

We will prove that the normalized families obtained in successive reductions satisfy the
Salzborn formulation of the conjecture. This suffices in view of Propositions 4.6 and 4.7,
and Theorem 4.9.
Consider the subfamilies Nk ⊆ N defined by Nk = {N ∈ N ∶ ∣N ∣ = 2
n − 2n−k}. With this
notation, we have that J(N ) = N1. Let N (i)
k the subfamily obtained by the sets descending
from the sets in Nk after i □
′ reductions. The sets in N (i)
k have 2
n − 2
n−k − i elements, and,
clearly, while doing the successive reductions, when the last set descending from a set in
Nk is removed, then all sets descending from a set in Nk+1 are irreducible, as they are then
minimal.
We apply the reduction process by removing all sets descending from N1, then all sets
descending from N2, and so on.
Put J(N ) = {∅, I1, . . . , In}, where Ii is a set containing the indexes of sets in F having
the element i ∈ U (F). Assume, without loss of generality, that the removed minimal set is
I1. When we do so, n − 1 sets of N ′
2, with size 2n − 2n−2 − 1, become irreducible, namely
the sets coming from the sets I1 ∪ Ii, for 2 ≤ i ≤ n. This happens because {1, i} ∈ F, which
implies that the only irreducible sets of N containing the index of {1, i} are Ii and I1, and
hence I1 ∪ Ii cannot be written as union of sets not involving I1. At this instance, we thus
have irreducible sets of size 2
n − 2
n−2 − 1. When we do the ℓ-th reduction, we must have
irreducible sets with at least 2n − 2
n−2 − ℓ elements, because every set that is then irreducible
belongs to N (ℓ)
k for some k ≥ 2. Since

2
n − 2n−2 − ℓ ≥ 2
n − ℓ
2 ⟺ ℓ ≤ 2n−1,

23

we have the conjecture verified up until N (2
n−1).
After doing 2n−1 reductions, our smallest irreducible elements are sets descending from
N n+1
2 , if n is odd (since the 2n−1 removed sets are precisely all sets from N1 ∪ ⋯ ∪ N n−1
2 ), or
sets descending from N n
2 , if n is even (since the 2n−1 removed sets are precisely all sets from
N1 ∪ ⋯ ∪ N n
2 −1 together with half the sets from N n
2 ). Hence, it suffices to prove that, when
removing sets coming from Nk with k ≥ n
2 , we always have irreducible sets of size greater
than half the respective universe.
Let k ≥ n
2 . When we remove the i-th set coming from Nk (this corresponds to the
(∑k−1
r=1 (
n
r) + i)-th reduction in total), the size of the remaining elements, if any, coming from

Nk is 2
n − 2n−k − ∑k−1
r=1 (
n
r) − i. If there are no remaining sets coming from Nk, then the
sets coming from Nk+1 are now irreducible, and larger. The total number of sets in N is
2
n − ∑k−1
r=1 (
n
r) − i. We have that

2
n − 2n−k −
 k−1
∑

r=1 (n
r) − i ≥ 2
n −
 k−1
∑
r=1 (
n
r) − i

2 ⟺ 2
n−1 − 2n−k −
 k−1
∑
r=1 (
n
r)

2 ≥ i
2

⟺ i ≤ 2n − 2n−k+1 −
 k−1
∑

r=1 (n
r). (6)

We know that i ≤ (
n
k), since that is total number of sets in Nk, so it suffices to prove that

(n
k) ≤ 2
n − 2n−k+1 −
 k−1
∑

r=1 (
n
r).

We have that
 (
n
k) ≤ 2
n − 2n−k+1 −
 k−1
∑

r=1 (n
r) ⟺ 2
n−k+1 ≤ 2
n −
 k
∑

r=1 (
n
r)

⟺ 2
n−k+1 − 1 ≤ 2
n −
 k
∑

r=0 (
n
r)

⟺ 2
n−k+1 − 1 ≤
 n
∑

r=k+1 (
n
r)

⟺ 2
n−k+1 − 1 ≤
 n−k−1
∑

r=0 (n
r).

If k ≤ n − 2, this follows from Lemma 5.4. The only case missing is the case k = n − 1.
Replacing k by n − 1 in (6), we get that i ≤ n − 2, so we can remove the first n − 2 sets of
Nn−1. Since Nn−1 has n sets, when one of the two last sets is removed, then the universe (of
the set in Nn) becomes irreducible and the conjecture is satisfied.

24

6 Future work

There are some things that we believe might be interesting to do using the construction
of families using the reductions introduced in this paper. The first big question would be
classifying the families which descend from power sets. It would also be interesting to uncover
some relations between relatives. For example, could it be proved that if a descendent from
a certain family satisfies the Frankl Conjecture, then all its siblings do? If all children from
a certain parent satisfy the conjecture, then so does the parent? If one parent satisfies the
conjecture, then does every parent satisfy it too? If every parent of a family satisfies the
conjecture, then so does that family?
Also, beyond the results presented in this paper, is it possible to further reduce the space
of families for which it suffices to prove the conjecture? In particular, can it be reduced
the T1 families? Or to some class of supratopological spaces smaller than TD or TiD spaces,
e.g. TDD spaces? Since we have proven that the conjecture holds for TFF spaces, and it is
enough to prove it for TD spaces, what can it be said about TF spaces?

Acknowledgements

The authors were partially supported by CMUP, member of LASI, which is financed by
national funds through the FCT — Funda¸c˜ao para a Ciˆencia e a Tecnologia, I.P., under the
projects with reference UIDB/00144/2020 and UIDP/00144/2020.

References

[1] T. Abe and B. Nakano. Frankl’s conjecture is true for modular lattices. Graphs and
Combinatorics, 14:305–311, 1998.

[2] C. E. Aull and W. J. Thron. Separation axioms between T0 and T1. Indagationes
Mathematicae (Proceedings), 65:26–37, 1962.

[3] I. Balla, B. Bollob´as, and T. Eccles. Union-closed families of sets. Journal of Combi-
natorial Theory, Series A, 120:531–544, 2013.

[4] H. Bruhn, P. Charbit, O. Schaudt, and J. A. Telle. The graph formulation of the
union-closed sets conjecture. European Journal of Combinatorics, 43:210–219, 2015.

[5] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture. Graphs and
Combinatorics, 31:2043–2074, 2015.
 25

[6] S. Cambie. Better bounds for the union-closed sets conjecture using the entropy ap-
proach. Preprint, arXiv:2212.12500, 2022.

[7] A. Carvalho. Frankl Conjecture. Master’s thesis, University of Porto, 2016.

[8] ´A. Cs´asz´ar. Generalized topology, generalized continuity. Acta Mathematica Hungarica,
96(4):351–357, 2002.

[9] Dwight Duffus. Open problem session. In Ivan Rival, editor, Graphs and Order: The
Role of Graphs in the Theory of Ordered Sets and Its Applications, volume 147 of
NATO ASI series. Series C: Mathematical and Physical Sciences, page 525. D. Reidel
Publishing Company, 1985.

[10] G. Lo Faro. A note on the union-closed sets conjecture. Journal of the Australian
Mathematical Society, Series A, 57:230–236, 1994.

[11] G. Lo Faro. Union-closed sets conjecture: improved bounds. Journal of Combinatorial
Mathematics and Combinatorial Computing, 16:97–102, 1994.

[12] J. Gilmer. A constant lower bound for the union-closed sets conjecture. Preprint,
arXiv:2211.09055, 2022.

[13] Y. Jiang. A generalization of the union-closed set conjecture. http://math.stanford.
edu/~jyj/Union_closed_set_conj.pdf. [online: accessed 2009].

[14] R. T. Johnson and T. P. Vaughan. On union-closed families, I. Journal of Combinatorial
Theory, Series A, 84(242-249), 1998.

[15] Ilan Karpas. Two results on union-closed families. Preprint, arXiv:1708.01434v1, 2017.

[16] A. S. Mashhour, A. A. Allam, F. S. Mahmoud, and F. H. Khedr. On supratopological
spaces. Indian Journal of Pure and Applied Mathematics, 14(4):502–510, 1983.

[17] R. Morris. FC-families, and improved bounds for Frankl’s conjecture. European Journal
of Combinatorics, 27:269–282, 2006.

[18] V. Pankajam and D. Sivaraj. Some separation axioms in generalized topological spaces.
Boletim da Sociedade Paranaense de Matem´atica, 31(1):29–42, 2013.

[19] B. Poonen. Union-closed families. Journal of Combinatorial Theory, Series A, 59:253–
269, 1992.
 26

[20] D. Reimer. An average set size theorem. Combinatorics, Probability and Computing,
12:89–93, 2003.

[21] J. Reinhold. Frankl’s conjecture is true for lower semimodular lattices. Graphs and
Combinatorics, 16:115–116, 2000.

[22] E. Rodaro. Union-closed vs upward-closed families of finite sets. Preprint,
arXiv:1208.5371v2, 2012.

[23] D.G. Sarvate and J-C. Renaud. Improved bounds for the union-closed sets conjecture.
Ars Combinatoria, 29:181–185, 1990.

[24] T. P. Vaughan. Families implying the Frankl conjecture. European Journal of Combi-
natorics, 23:851–860, 2002.

[25] P. W´ojcik. Union-closed families of sets. Discrete Mathematics, 199:173–182, 1999.

[26] L. Yu. Dimension-free bounds for the union-closed sets conjecture. Entropy, 25(5):767,
2023.
 27
