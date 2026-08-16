<!-- source: https://arxiv.org/pdf/2412.18740 | converted from PDF -->

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED
UNION-CLOSED FAMILIES OF SETS

CORY H. COLBERT

1Department of Mathematics, Washington and Lee University, Lexington, VA, USA

Abstract. The union-closed sets conjecture (sometimes referred to as Frankl’s conjecture) states
that every finite, nontrivial union-closed family of sets has an element that is in at least half of its
members. Although the conjecture is known to be false in the infinite setting, we show that many
interesting results can still be recovered by imposing suitable chain conditions and considering
carefully chosen elements called optimal elements. We use these elements to show that the union-
closed conjecture holds for both finite and infinite union-closed families such that the cardinality
of any chain of sets is at most three. We also show that the conjecture holds for all nontrivial
topological spaces satisfying the descending chain condition on its open sets. Notably, none of
those arguments depend on the cardinality of the underlying family or its universe. Finally, we
provide an interesting class of families that satisfy the conclusion of the conjecture but are not
necessarily union-closed.
 1. Introduction

A family of sets F is union-closed if for all A, B ∈ F, we have A ∪ B ∈ F. The union-closed sets
conjecture (sometimes referred to as Frankl’s conjecture, in honor of P. Frankl) says that if F ̸= {∅}
is a finite nonempty union-closed family of sets, then there exists an element that is in at least half
of the sets in F. Such an element in a union-closed family is called an abundant element. Despite
over four decades of research, the conjecture has so far resisted proof and remains unresolved.
Much progress has been made, however. Recall that if F is a family of sets, then the universe of F
is defined as UF := ∪F ∈F F. In [4], Boˇsnjak and Markovi´c show that the conjecture holds if F is union-
closed and |UF | ≤ 11. In particular, any counterexample must have |UF | ≥ 12. Studying potential
counterexamples further, Roberts and Simpson proved that if q = |UF | is minimal among all union-
closed counterexamples F to the conjecture, then |F| ≥ 4q − 1. Consequently, any counterexample
to the conjecture must have |F| ≥ 47 ([13], Corollary 5). In [3], Balla, Bollob´as and Eccles show
that if |F| ≥ 2
3 · 2|UF |, then F has an abundant element. In 2022, Gilmer [9] made a stunning
breakthrough by showing that if F is union-closed, then there exists an element that is in at least
1% of the members of F. Gilmer’s result, which uses ideas from information theory and Shannon
entropy, was the first result to show that there exists an element that is in a constant proportion c
of the members of a union-closed family. Gilmer’s work resulted in significant research activity to
improve the constant proportion c. The bound was initially improved to c = 3−
√5
2 ≈ 0.38197 by

E-mail address: ccolbert@wlu.edu.
Key words and phrases. posets, combinatorics, union-closed families, descending chain condition, ascending chain
condition.
 1arXiv:2412.18740v3  [math.CO]  2 Dec 2025
2 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

Alweiss, Huang, and Sellke [1]; Chase and Lovett [8]; and Sawin [14]. In ([14], Section 2), Sawin
showed that the original bound was not sharp, and both Cambie [6] and Yu [16] improved the
bound to c ≈ 0.38234. Liu [10] further improved the bound to c ≈ 0.38271.
1 In [7], Cambie provides
an excellent survey of Gilmer’s method and entropic techniques. Another excellent exposition by
Bruhn and Schaudt in [5] summarizes numerous other strategies, approaches, and results toward
understanding the conjecture.
Although the conjecture is typically stated in the context of finite families, it is natural to wonder
what happens in the infinite case. In this setting, if F is a family of sets, then an element x ∈ UF will
be abundant if there exists an injective set map from the collection sets that do not contain x into the
collection of sets that do. In the most general setting the conjecture does indeed fail, with a classic
counterexample being F = {N \ {1, . . . , i} : i ∈ N} ∪ {N} (see [12], p.2). In this example, the reader
will notice that every positive integer only belongs to a finite number of sets in F, so no positive
integer can be abundant. Another interesting observation can be made concerning F as well. Recall
that if S is a collection of sets, ordered with respect to inclusion, then S has the descending chain
condition (see Definition 2.1) if every descending chain A1 ⊇ A2 ⊇ A3 . . . of sets in S terminates.
That is, there exists n ∈ N such that An = Am for all m ≥ n. The reader will notice that the family
(F, ⊆) defined above fails the descending chain condition: N ⊋ N \ {1} ⊋ N \ {1, 2} ⊋ . . . , thus
leaving open the possibility for investigation into the case where one imposes chain conditions. It
is a central focus of this paper to study how the two basic chain conditions – the descending chain
condition and its dual ascending chain condition – affect union-closed families, and what can be said
about such families in the context of the union-closed conjecture.
In this paper, we study general union-closed families with a particular focus on the partial order
(F, ⊆). If x ∈ UF , we define Fx = {A ∈ F : x ∈ A}, N (F) = {Fx : x ∈ UF }, and we say x is
optimal in F is Fx is maximal in (N (F), ⊆). Optimal elements are worth studying because they
could provide promising places to look for abundant elements in many casual circumstances. As
seen in the above example, union-closed families need not have optimal elements. However, as our
first result shows, if (F, ⊆) satisfies the descending chain condition and is nontrivial, then optimal
elements always exist:

Lemma. If (F, ⊆) satisfies DCC, then (N (F), ⊆) satisfies ACC. Consequently, if (F, ⊆) satisfies
DCC and Fa ∈ N (F), then there exists an optimal b ∈ UF such that Fa ⊆ Fb.

In section 3, we show numerous applications of optimal elements. First, we turn our attention
to generalized union-closed families F such that the length of the longest chain of sets in (F, ⊆) is
two (we define the length of a nonempty finite chain C to be |C| − 1). Specifically, we prove the
following:

Theorem. Every nontrivial union-closed family of dimension at most two has an abundant element.

This result extends a result of Tian [15] to the infinite case (height-three posets correspond to
dimension-two posets herein), and its proof shows that every optimal element in such a family
is abundant. Although optimal elements need not be abundant in general (see Example 3.19),
such examples only exist in dimension three or higher. Moreover, even in some more complicated

1The author wishes to thank S. Cambie for providing helpful comments regarding the status of improved values
of c.

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 3

examples in dimension three, such as Example 3.20, optimal elements can still be abundant. As a
final application of optimal elements, we show that they can be used to prove that certain topological
spaces have abundant elements. Specifically, we show:

Theorem. Let (X, τ ) be a topological space satisfying the descending chain condition on its open
sets and such that τ ̸= {∅}. Then X has an abundant element of τ.

In the last section, we show that abundant elements can exist in many interesting families of sets
that are not necessarily union-closed. Let α > 0 be a cardinal number. An α-tent T is a poset
(T , ≤) of dimension one with α minimal nodes and a single greatest node. In the context of families
of sets, we say a family of sets T is an α-tent if (T , ⊆) is an α-tent. If F and G are families of
sets, we say F dominates G if for all A ∈ F there exists B ∈ G such that A ⊇ B. Finally, we define
F ∗ := F \ {∅}. We prove the following result:

Theorem. Let T be a union-closed α-tent for some α > 1 and let F be a family of sets. Let
F ∗ := F \ {∅}. If F ∗ dominates T , then F ∪ T has an abundant element.

2. Basic Definitions and Notation

Definition 2.1. If (X, ≤) is a poset and x ∈ X, define the down-set of x as x
↓ := {y ∈ X : y ≤ x}
and the up-set of x as x
↑ := {y ∈ X : y ≥ x}. A chain is a subset C ⊆ X such that for all x, y ∈ C,
we have x ≤ y or y ≤ x. The length ℓ(C) of a finite nonempty chain C is defined as ℓ(C) = |C| − 1.
We define the dimension 2 of X to be dim X := sup{ℓ(C) : C is a chain in X}. If x ∈ X, we define
the height of x to be htX x := dim x↓ and the coheight of x to be cohtX x := dim x↑. If x, y ∈ X,
then y covers x in X if x < y and for all z ∈ X, if x ≤ z ≤ y, we have x = z or z = y. If y covers
x in X, we will write x <c y. An element x ∈ X is maximal (resp. minimal ) in X if for all y ∈ X,
x ≤ y (resp. y ≤ x) implies x = y. The set of maximal elements (resp. minimal elements) is denoted
max X (resp. min X). Finally, a poset (X, ≤) satisfies the descending chain condition (DCC) (resp.
ascending chain condition (ACC)) if every nonempty subset of X has a minimal (resp. maximal)
element.

Definition 2.2. A family of sets F is a subset of some power set. The universe UF of F is
defined as UF := ∪A∈F A and F is nontrivial if F is nonempty and UF ̸= ∅. If x ∈ UF , we define
Fx := {A ∈ F : x ∈ A}, and we define F c
x := F \ Fx. We define N (F) = {Fx : x ∈ UF }. A family F
is separating if the map x → Fx is injective and it is union-closed if the union of any two members of
F is still in F. A family is countably union-closed if it is closed under countable unions of members
in the family. An element x ∈ UF is abundant in (not necessarily union-closed) F if there exists
an injective set map F c
x ↪→ Fx. An element x ∈ UF is optimal in F if Fx is a maximal element of
(N (F), ⊆).

Remark 2.3. If F is a family of sets, min F (resp. max F) will take its meaning from Definition
2.1 applied to (F, ⊆). Note also that if F is nonempty and (F, ⊆) satisfies DCC, then min F is
nonempty. A similar statement holds if (F, ⊆) satisfies ACC.

2The author’s training is in commutative algebra where the dimension of (Spec R, ⊆) is defined this way, inspired
by Krull dimension for commutative rings.

4 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

3. Chain Conditions and Optimal Elements

In the search for abundant elements, it is most natural to look at elements x corresponding to sets
Fx of maximal cardinality. However, this presents some issues. In the infinite case, for instance, it can
happen that Fx ⊊ Fy yet |Fx| = |Fy|. As will be discussed in Remark 3.12, this particular situation
makes generalizing to the infinite case somewhat subtle. Moreover, if Fx has maximal cardinality
in N (F), it is unclear what structural implications exist in (F, ⊆) as a result. In other words,
cardinality alone will not be sufficient to distinguish the elements of N (F) in an immediately useful
way. As we show in this section, optimal elements have the advantage of providing some structural
insights into (F, ⊆) when F is assumed to be union-closed and of low dimension. Most importantly,
they allow us to provide arguments establishing abundance in low dimension that do not depend
on cardinality. Although determining when optimal elements exist is a subtle matter in the most
general case, Lemma 3.3 provides a useful criterion which will suit our purposes herein.

3.1. The union-closed hypothesis and ACC. If F is union-closed, then F contains all finite
unions of members of F, and if F is also finite, then it follows that UF ∈ F. However, if F is not
finite, then it is not necessarily the case that UF ∈ F. Consider, for instance, F := {[n] : n ∈ N},
where [n] = {1, . . . , n}. Then F is union-closed, but UF = ∪n∈N[n] = N /∈ F. In other words, if
one wishes to conduct a study of general union-closed families, one must consider whether to relax
Definition 2.2 to allow for unions over infinite indexing sets. As the next lemma shows, however,
if (F, ⊆) satisfies the ascending chain condition, then no information is lost by using the “finite
version” of the union-closed hypothesis.

Lemma 3.1. If (F, ⊆) is a family of sets that satisfies ACC, then F is closed under finite unions of
sets if and only if F is closed under arbitrary unions of sets.

Proof. Suppose F is closed under finite unions of sets. Let {Ai}i∈I be a collection of sets in F
indexed by some nonempty set I. Let B := {∪i∈F Ai : F is a finite, nonempty subset of I}. Since I
is nonempty, so is B. Moreover, since F is closed under finite unions, we have B ⊆ F so that (B, ⊆)
satisfies ACC as well. By the ACC hypothesis, (B, ⊆) has a maximal element B. Relabeling elements
of I if necessary, assume B = A1 ∪ . . . ∪ AN for some N ∈ N. If x ∈ ∪i∈I Ai \ B, then there is i ∈ I
such that x ∈ Ai \ (A1 ∪ . . . ∪ AN ). So B ⊊ Ai ∪ (A1 ∪ . . . ∪ AN ) ∈ B, which contradicts B being a
maximal element of (B, ⊆). So ∪i∈I Ai ⊆ B and hence is B. The other direction is immediate. □

Remark 3.2. As an immediate corollary, if F is a nonempty family of sets that satisfies ACC and
is union-closed, then UF is the greatest element of (F, ⊆). In particular, if x ∈ UF , the subfamily
F c
x is also union-closed and hence has a greatest element if it is nonempty.

3.2. Optimal elements and DCC. As mentioned in the introduction, if F = {N\[i] : i ∈ N}∪{N},
then (F, ⊆) has no abundant elements and also fails DCC. In addition to failing DCC, one may
also notice that F1 ⊊ F2 ⊊ F3 ⊊ . . . , so no Fa is maximal in (N (F), ⊆). Hence F has no
optimal elements as in Definition 2.2. Interestingly, (F, ⊆) not having the descending chain condition
resulted in (N (F), ⊆) not having the ascending chain condition. As the next result shows, this is
no coincidence for countably union-closed families:

Lemma 3.3. Suppose F is a countably union-closed family of sets. If (F, ⊆) satisfies DCC, then
(N (F), ⊆) satisfies ACC. Consequently, if (F, ⊆) satisfies DCC and a ∈ UF , then there exists an
optimal b ∈ UF such that Fa ⊆ Fb.

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 5

Proof. Let UF be the universe of F and suppose (N (F), ⊆) does not satisfy ACC. Then there
exist x1, x2, x3, . . . ∈ UF such that Fx1 ⊊ Fx2 ⊊ Fx3 ⊊ . . . is a non-terminating ascending chain in
(N (F), ⊆). Let X1 ∈ Fx1 and for each i > 1, let Xi ∈ Fxi \ Fxi−1 . Observe that xi ∈ Xi for all
i ≥ 1, and if 1 ≤ i′ < i, then xi′ /∈ Xi. Having chosen Xi for all i ≥ 1, let Ej := ∪∞
j=iXj. Since F is
countably union-closed, Ej ∈ F for all j ≥ 1. Moreover, E1 ⊋ E2 ⊋ E3 ⊋ . . . is a non-terminating
descending chain in (F, ⊆) because xi ∈ Ei \ Ei+1 for all i ≥ 1. So (F, ⊆) does not satisfy DCC.
For the second part, simply observe that F ↑
a is a nonempty subset of N (F). Since (F, ⊆) satisfies
DCC, (N (F), ⊆) satisfies ACC, so (F ↑
a , ⊆) has a maximal element. □

Remark 3.4. The converse is false. For example, (P(N), ⊆) does not satisfy DCC yet Fm is maximal
in (N (P(N)), ⊆) for all m ∈ N because if Fm ⊆ Fm′, then {m} ∈ Fm′ =⇒ m
′ = m.

As an immediate consequence, we have the following:

Corollary 3.5. If (F, ⊆) is a finite-dimensional, nontrivial, union-closed family, then F is closed
under arbitrary unions and has an optimal element.

Proof. If (F, ⊆) is finite-dimensional, then it is both ACC and DCC. By Lemma 3.1, it is closed
under arbitrary unions (hence countable unions). So it has an optimal element by Lemma 3.3. □

3.3. Covert elements. A classical result towards the union-closed conjecture states that if {x} ∈ F
for some x, then x is abundant in F. One proves this result by considering the injective map
A → A ∪ {x} which is well-defined by hypothesis. Interestingly, it can still happen that the map is
well-defined even though {x} /∈ F. Consider the following example.

Example 3.6. In the following figure, the reader will observe that {3} /∈ F, yet the map A → A∪{3}
from F c
3 ↪→ F3 is well-defined.
 {1, 2, 3, 4}

{1, 2, 4} {2, 3, 4}

{1, 2} {2, 4}

{1, 2, 3}

In this case, we refer to x = 3 as a covert element. More precisely, we say x is covert if {x} /∈ F
yet the map A → A ∪ {x} is well-defined. As the next result shows, if one wishes to show that x
is covert, then under mild conditions, it suffices to check that the map A → A ∪ {x} is well-defined
along the “bottom row” (i.e. minimal nodes) of F c
x. In the case of Example 3.6, for instance, this
amounts to checking along min F c
3 = {{1, 2}, {2, 4}}.

Lemma 3.7. Suppose F is union-closed, (F, ⊆) satisfies DCC, and x ∈ UF . If there exists A ∈ F c
x
such that A ∪ {x} /∈ F, then there exists B ∈ min F c
x such that B ∪ {x} /∈ F. Consequently, if
A ∪ {x} ∈ Fx for all A ∈ min F c
x, then x is abundant in F.

Proof. Let A = {A ∈ F c
x : A ∪ {x} /∈ F}. Since A ̸= ∅, it has a minimal element B because (F, ⊆)
satisfies DCC. We claim B ∈ min F c
x. Assume the contrary. Then there exists B′ ∈ F c
x such that
B′ ⊊ B. Since B′ ∈ F c
x and B′ /∈ A , we have B′ ∪ {x} ∈ F. Note B = B ∪ B′. Hence,

B ∪ {x} = (B ∪ B′) ∪ {x} = B ∪ (B′ ∪ {x}) ∈ F,

6 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

where the last assertion holds because F is union-closed. But this contradicts B ∈ A . Therefore,
B ∈ min F c
x. For the second part, if A ∪ {x} ∈ Fx for all A ∈ min F c
x, then by what we have justh
shown, it follows that A ∪ {x} ∈ Fx for all A ∈ F c
x. So the map A → A ∪ {x} is well-defined and of
course injective. □

Example 3.8. If F is a union-closed family and B ∈ F, recall B is a basis set in F if for all
X, Y ∈ F, whenever B = X ∪ Y, then B = X or B = Y (e.g., see Section 2 of [5]). Indeed,
sets in min F (see Remark 2.3) are necessarily basis sets in F, and if (F, ⊆) satisfies DCC and
X ∈ F, then there exists M ∈ (min F) ∩ X ↓ (see Definition 2.1). Basis sets need not exist in
general, however. Such examples are necessarily infinite. As a straightforward example, consider
F = {A ⊆ N : A is infinite}. Then F is certainly union-closed. If A ∈ F, let x1 < x2 be the two
smallest elements of A. Then A1 = A \ {x1} and A2 = A \ {x2} are both in F and A = A1 ∪ A2. So A
is not a basis set. Although this example has no basis elements, every positive integer is nevertheless
abundant in F. In fact, if x ∈ N, then F c
x is in bijection with Fx via the classical map A → A ∪ {x}
even though {x} /∈ F. In other words, although Lemma 3.7 does not apply in this case, every integer
is nevertheless covert. Notably, every element is also optimal in F even though (F, ⊆) does not
satisfy DCC: indeed, if a, b ∈ N are distinct, then N \ {b} ∈ Fa \ Fb. So (N (F), ⊆) is an antichain
(just as in Remark 3.4) and each Fa is maximal.

3.4. The separating condition. Let F be a union-closed family. Establish an equivalence relation
∼ on UF as x ∼ y if and only if Fx = Fy. Let V = UF / ∼ with map [·] : UF → V defined as x → [x].
If A ∈ F, then [A] = {[a] : a ∈ A} and we may define S := {[A] : A ∈ F}. Then S is a family of
sets with universe US = V. Note that S is separating: if S[x] = S[y] and A ∈ Fx, then [x] ∈ [A] so
[A] ∈ S[x] = S[y]. Hence [y] ∈ [A] so [y] = [a
′] for some a
′ ∈ A. Thus Fy = Fa′ and since A ∈ Fa′,
we have A ∈ Fy. So Fx ⊆ Fy and a similar argument gives Fy ⊆ Fx. So [x] = [y]. In addition, [·]
induces a poset isomorphism of (F, ⊆) with (S, ⊆). That [·] preserves order and is surjective is clear,
so all that remains to show is that it is an order embedding. Indeed, if [A] ⊆ [B] and a ∈ A, then
[a] = [b] for some b ∈ B so Fa = Fb hence B ∈ Fa =⇒ a ∈ B. So A ⊆ B.
Let {Xi : i ∈ I} ⊆ F be a nonempty collection of sets in F. We claim [∪i∈I Xi] = ∪i∈I [Xi] and
[∩i∈I Xi] = ∩i∈I [Xi]. The first assertion is clear. For the second assertion, if [x] ∈ ∩i∈I [Xi], then
for all i ∈ I, there exists xi ∈ Xi such that [x] = [xi]. Fix i0 ∈ I. Then [xi0 ] = [xi] for all i ∈ I.
So Fxi0 = Fxi for all i ∈ I. Since Xi ∈ Fxi, we have Xi ∈ Fxi0 so that xi0 ∈ Xi. So xi0 ∈ ∩i∈I Xi.
That is, [x] = [xi0 ] ∈ [∩i∈I Xi]. That [∩i∈I Xi] ⊆ ∩i∈I [Xi] is straightforward. In particular, if F is
union-closed (resp. intersection-closed), then S is union-closed (resp. intersection-closed).
Lastly, we claim [·] preserves abundance and optimality. First, note that for all x ∈ UF we have
x ∈ A ⇐⇒ [x] ∈ [A]. So [Fx] = S[x] and [F c
x] = S c
[x]. Suppose [x] is abundant in S. Then there
exists an injective map ψ : S c
[x] ↪→ S[x]. Then φ : F c
x → Fx defined as φ(A) := [ψ([A])]
−1 is an
injective map from F c
x into Fx; recall that although [·] is not invertible as a map from UF onto V,
it is invertible as an induced map from F onto S. So x is abundant in F. A similar argument shows
that if x is abundant in F, then [x] is abundant in S. If Fx is maximal in N (F) and S[x] ⊆ S[y],
then
 Fx = [
S[x]]−1 ⊆ [
S[y]]−1 = Fy =⇒ Fx = Fy =⇒ [x] = [y].

So S[x] is maximal in N (S), and [x] is optimal in S. As before, a similar argument shows the
converse.

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 7

In summary, taking a union-closed family F and reducing to S as above replaces F with a
separating union-closed family S whose structure is indistinguishable from F from the point-of-view
of order.

3.5. Union-closed families of dimension at most two. In this section, we show that every
union-closed family of dimension at most two – whether it is infinite or not – has an abundant
element. In fact, we show that every optimal element is abundant in such families. Notably, none
of our arguments in this section depend on the cardinality of the family or the size of its universe.

Proposition 3.9. If F is a nontrivial union-closed family of dimension at most one, then every
element in UF is abundant in F.

Proof. If F is zero dimensional, then F = {UF } is a point and the assertion is clear (see Remark
3.2). Assume dim F = 1 and let x ∈ UF . Then F c
x is union-closed, and since x ∈ UF , either F c
x = ∅
or it is nonempty and satisfies dim F c
x < dim F. In the former case, Fx = F and we are done. In
the latter case, dim F c
x = 0 which means that F c
x is a point, so there is certainly an injective map
F c
x ↪→ Fx. □

Remark 3.10. The proof of the previous proposition shows that if dim F ≤ 1, then every element
in UF belongs to all but at most one member of F.

Lemma 3.11. Let F be a separating union-closed family, let x ∈ UF , and let Ix = ∩F ∈Fx F. If x is
optimal, then Ix = {x}. Consequently, if x is optimal and A ∈ F c
x is such that A ∪ X = UF for all
X ∈ Fx, then UF = A ∪ {x}.

Proof. Note x ∈ Ix by definition. Let y ∈ Ix. Then y ∈ F for all F ∈ Fx, so Fx ⊆ Fy hence Fx = Fy
by optimality. Since F is separating, we have y = x. For the second part, if A ∪ X = UF for all
X ∈ Fx, then UF \ A ⊆ ∩X∈FxX = Ix = {x}. If UF \ A = ∅, then UF = A since A ⊆ UF , a
contradiction because x /∈ A. So UF = A ∪ {x}. □

Remark 3.12. If F is finite, separating, and nonempty, then one can forego the notion of optimality
as we have defined it and simply focus on studying an Fx of maximal cardinality. An alternative
argument, for instance, is to assume Fx has maximal cardinality and suppose y ∈ Ix. Then Fx ⊆ Fy,
but by the separating condition, Fx ⊊ Fy, so |Fx| < |Fy|, a contradiction. This argument does not
quite work in the general case, however. Optimality provides a very simple modification to this
argument that generalizes to the infinite case (as seen above).

Recall from Definition 2.1 that if A, B ∈ F are members, then A ⊂c B (i.e., B “covers” A) if
A ⊊ B and for all C ∈ F if A ⊆ C ⊆ B, then A = C or C = B.

Definition 3.13. If F is a family of sets and x ∈ UF and A ∈ F, then B is an x-cover of A if
B ∈ Fx and A ⊂c B.

Lemma 3.14. If F is a union-closed family of sets and x ∈ UF , then every member of Fx covers at
most one member of F c
x. Consequently, if for all A ∈ F c
x there exists an x-cover B of A, then after
choosing a fixed x-cover BA of each such A, the map A → BA is an injection from F c
x into Fx.

Proof. If B ∈ Fx covers A1 ̸= A2 ∈ F c
x, then we claim A1 and A2 are incomparable. For otherwise,
A1 ⊊ A2 ⊂c B without loss of generality, and that contradicts B being a cover of A1. So A1 ⊊
A1 ∪ A2 ⊆ B and A1 ⊂c B =⇒ A1 ∪ A2 = B, a contradiction since x /∈ A1 ∪ A2. □

8 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

Remark 3.15. The union-closed hypothesis cannot be dropped. Consider F = {{1}, {2}, {3}, {1, 2, 3}}.
Then {1, 2, 3} is a 3-cover of both {1} and {2}. Moreover, it is not necessarily the case that if B is
an x-cover of A, then B = A ∪ {x}. For instance, take F = {{1}, {1, 2, 3}}. Then F is union-closed
and {1, 2, 3} is a 2-cover of {1}.

Lemma 3.14 provides a slightly different argument to the following well-known result:

Corollary 3.16. If F is a union-closed family and {x} ∈ F for some x ∈ UF , then x is abundant
in F.

Proof. If A ∈ F c
x, then A ⊂c A ∪ {x}. □

Theorem 3.17. Every union-closed family of dimension two has an abundant element.

Proof. We may assume by the work of Section 3.4 that F is separating. Since every nontrivial,
finite-dimensional, union-closed family has an optimal element, there exists x ∈ UF that is optimal
in F. We claim x is abundant in F. By Lemma 3.14, we need only show that every element of F c
x
has an x-cover. To that end, let A ∈ F c
x. If UF covers A we are done, so assume UF does not cover
A. If A ∪ X = UF for all X ∈ Fx, then by Lemma 3.11 we have UF = A ∪ {x}. So A ⊂c UF ,
a contradiction. Therefore, there exists X ∈ Fx such that A ∪ X ̸= UF . Set B = A ∪ X. Then
A ⊊ B ⊊ UF . Since dim F = 2, we must have ht A = 0 and ht B = 1 (see Definition 2.1). Hence
A ⊂c B. □

Example 3.18. The proof of Theorem 3.17 shows that if F is union-closed and separating of
dimension two, then every optimal element in F is abundant. To see an example of how the result
distinguishes among different possible choices of abundant elements for a given family, consider the
following example:
 {1, 2, 3, 4}

{1, 2, 3} {2, 3, 4}

{1, 2} {2, 3} {3, 4}

Note that in this example, F1 ⊊ F2, and so x = 1 is not optimal, although it is abundant since it
resides in exactly half of the members of F. On the other hand, x = 2 is optimal and is clearly the
“better” choice, residing in all but one of the sets in F.

Example 3.19. Optimal elements need not be abundant in higher dimensions. Consider, for in-
stance, the following union-closed example of dimension three:

{1, 2, 3}

{1, 2} {2, 3} {1, 3}

{2} {3}

∅

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 9

Notice that x = 1 is optimal but not abundant. This example is minimal in every immediate
sense of the word. If F is a separating union-closed family of sets containing an element x ∈ UF
that is optimal in F yet not abundant in F, then we claim |Fx| ≥ 3. To see why, first note that
UF ∈ Fx. Since F ̸= {UF }, and x is optimal in F, we must have Fx ̸= {UF }. So there exists Q ∈ F
such that x ∈ Q and Q ̸= UF . Since x is not abundant, Q ̸= {x} by Corollary 3.16. So there is
y ∈ Q \ {x}. Optimality and the separating condition imply that Fx ̸⊆ Fy. So there is Q′ ∈ Fx such
that y /∈ Q
′. Since y ∈ Q, we have Q
′ ̸= Q, and of course Q
′ ̸= UF because y /∈ Q
′. So |Fx| ≥ 3.
Since x is not abundant, |F c
x| ≥ 4. So |F| ≥ 7. Any set with at least 7 subsets must have at least 3
elements. So |UF | ≥ 3. And the proof of Theorem 3.17 shows that dim F ≥ 3.

Example 3.20. The next example demonstrates the limits to the x-cover approach that allowed us
to prove Theorem 3.17:
 {1, 2, 3, 4, 5}

{1, 2, 3, 5} {1, 2, 3, 4} {2, 3, 4, 5}{1, 3, 4, 5}{1, 2, 4, 5}

{1, 2, 3}{1, 2, 5} {1, 4, 5} {3, 4, 5}{2, 3, 4}

{1, 2} {1, 5} {3, 4}{2, 3} {4, 5}

In this union-closed example of dimension three, every element in UF = [5] is optimal (and indeed
abundant), yet for all x ∈ UF , there exists A ∈ F c
x that has no x-cover. For example, if x = 1, then
A = {3, 4} is not covered by any member of F1.

3.6. Topological spaces. All topological spaces are union-closed by definition, so it is natural to
wonder if the the union-closed sets conjecture can be proved for topological spaces. Although it is
known to be true for finite topological spaces ([11], Theorem 6.1), left open is the infinite case. As
the next theorem indicates, if (X, τ ) is a (possibly infinite) topological space, all one needs is for
(τ, ⊆) to satisfy the descending chain condition to guarantee the existence of an abundant element.
Recall a topological space (X, τ ) is an Alexandroff topology if the arbitrary intersection of open sets
is open.

Theorem 3.21. Let (X, τ ) be a topological space satisfying the descending chain condition on its
open sets and such that τ ̸= {∅}. Then X has an abundant element of τ.

Proof. By the work of Section 3.4, it suffices to assume (X, τ ) is T0 (i.e., τ is separating). We claim
(X, τ ) is Alexandroff. By ([2], p.1), it suffices to show that for all a ∈ X, there exists a smallest
neighborhood Ua of a. Let N (a) be the set of all neighborhoods of a. Then N (a) is nonempty and
hence has a minimal element Ua since (τ, ⊆) satisfies the descending chain condition. If U ∈ N (a),
then Ua ∩ U ∈ N (a) and Ua ∩ U ⊆ Ua. By minimality, Ua ∩ U = Ua, so Ua ⊆ U. Since U was
arbitrary, we have that Ua is the least element of N (a). Since τ ̸= {∅}, we have Uτ ̸= ∅, so by
Lemma 3.3, there exists an element x ∈ X that is optimal in τ. Since (X, τ ) is Alexandroff, we must

10 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

have I τ
x = ∩U ∈τx U ∈ τ. By Lemma 3.14, Ix = {x}. So {x} ∈ τ, and by Corollary 3.16, x is abundant
in τ. □

As mentioned above, Theorem 3.21 recovers the result of Mehr ([11], Theorem 6.1) in the finite
case:

Corollary 3.22. If (X, τ ) is a finite topological space, and τ ̸= {∅}, then X has an abundant
element of τ.

Proof. Finite topological spaces satisfy DCC on their open sets, so the result follows by Theorem
3.21. □

Example 3.23. The descending chain condition hypothesis cannot be dropped. For instance, let
X = N and let Fi = {n ∈ N : n ≥ i}. Let τ = {Fi : i ∈ N} ∪ {∅}. Then τ is infinite, yet for all
m ∈ X, τm is finite. So no m ∈ X is abundant.

Example 3.24. Although the DCC hypothesis cannot be dropped, some topologies that fail DCC
still have abundant elements. Consider X = R and τ = {(−∞, x) : x ∈ R}∪{R, ∅}. Then (τ, ⊆) does
not satisfy the descending chain condition, yet we claim every element in R is abundant. Indeed, if
a ∈ R, then τa is in one-to-one correspondence with the interval (a, +∞). So |τa| = |R| = |τ |.

4. Dominating Families and α-Tents

The union-closed hypothesis is not always necessary to prove the existence of an abundant element
in a family of sets. In this section, we show that if F is any family of sets that dominates a union-
closed α-tent T (i.e., α minimal nodes and a single greatest node), then F ∪ T has an abundant
element.

Definition 4.1. If F and G are families of sets, F dominates G if for all A ∈ F, there exists B ∈ G
such that A ⊇ B.

Definition 4.2. If α is a positive cardinal, an α-tent is the one-dimensional poset with α minimal
nodes and a single greatest node.

Theorem 4.3. Let T be a union-closed α-tent for some α > 1 and let F be a family of sets. Let
F ∗ := F \ {∅}. If F ∗ dominates T , then F ∪ T has an abundant element.

Proof. Let G := F ∗ ∪ T and consider (G, ⊆). First, we claim min G = min T (the latter of which is
the set of α minimal nodes of T ). Suppose A ∈ min T , and suppose X ∈ G is such that X ⊆ A.
If X ∈ T , then X = A and hence A ∈ min G. If X ∈ F ∗, then by domination there exists X ′ ∈ T
such that A ⊇ X ⊇ X ′. Since A ∈ min T , we have A = X ′. So A = X still. Hence A ∈ min G.
Likewise, if A ∈ min G, then since dim T = 1, there exists X ∈ min T such that A ⊇ X. So A = X
and hence A ∈ min T . Therefore, min T = min G. Consider M := {|M ↑| : M ∈ min T }, where each
M ↑ is taken in (G, ⊆).
Suppose max M exists and equals |M ↑| for some M ∈ min T . Since α > 1, no set in min T is
empty. Let x ∈ M. If x is in each minimal node of T , then x is in every nonempty member of F ∪ T
and we are done. Otherwise, by Lemma 3.10, there exists exactly one minimal node N such that
x /∈ N. In particular, if G ∈ Gc
x, then we must have G ⊇ N. Moreover, since x ∈ UT (i.e., the greatest
node of T ), it follows that Gc
x ⊆ N ↑ \ {UT }. Now |N ↑ \ {UT }| ≤ |M ↑ \ {UT }| because of our choice

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 11

of M ↑ and the fact that UT ∈ M ↑ ∩ N ↑. Let φ1 : N ↑ \ {UT } ↪→ M ↑ \ {UT } be an injective set map.
Then φ1 restricts to an injective map Gc
x ↪→ Gx. If F ∗ = F, we are done. Otherwise, ∅ ∈ F and we
may extend φ1 to φ2 : Gc
x ∪ {∅} → Gx by setting φ2(∅) = UT . Then φ2 is injective because φ1 is and
UT /∈ im φ1 .
Now suppose max M does not exist. We claim every element of UT is abundant in F ∪ T . Let
x ∈ UT and assume without loss of generality that there is N ∈ min T such that x /∈ N. Again by
Lemma 3.10, such N is unique. Since max M does not exist, there exists M ∈ min T such that
|M ↑| > |N ↑|. Since M ̸= N we have x ∈ M. Now apply the argument from the previous paragraph
to M and N. □

Corollary 4.4. If (G, ⊆) is a DCC union-closed family of nonempty sets such that there exists a
height-one member of G that exceeds every height-zero member of G, then the family G ∪ {∅} has
an abundant element.

Proof. Let α = | min G|. Note that α > 0. If α = 1, then G has a unique minimal nonempty member
M, and if x ∈ M, then x is in every member of G. Thus, (G ∪ {∅})c
x = {∅}, and it follows that x is
abundant in G ∪ {∅}.
Suppose α > 1. Let H be a height-one element as in the hypothesis, and let M ̸= N be any two
height-zero elements of G. Then M ⊊ M ∪ N ∈ G, and since M ∪ N ⊆ H, we have M ∪ N = H
because ht H = 1. Therefore, the set T := {H} ∪ min G is a union-closed α-tent.
Let F = G ∪ {∅}. Then F ∗ = G since every member of G is nonempty, and F ∗ dominates T
because every member of G contains an element of min G by the DCC hypothesis. By Theorem 4.3,
F ∪ T = (G ∪ {∅}) ∪ T = G ∪ {∅} has an abundant element. □

Example 4.5. A key feature of Theorem 4.3 is that it does not require that F be union-closed. As
an example, let M be any collection of proper subsets of R such that the union of any two is exactly
R (for example, M could consist of all sets of the form R \ {t} for t ∈ R). Note that every set in M
is nonempty. For each M ∈ M, let FM be any collection of subsets of C such that for all A ∈ FM ,
we have M ⊆ A. Let F = (∪M ∈MFM ) ∪ {∅}. Then T := {R} ∪ M is a union-closed α-tent, where
α = |M|, and F ∗ dominates T by definition of F. By Theorem 4.3, there exists a real number that
is in at least half of the sets in F ∪ T (we know a real number can be chosen since the proof of 4.3
picks an abundant element from UT = R).

Example 4.6. The proof of Theorem 4.3 occasionally pairs ∅ with UT in order to get the desired
injective map. Sometimes this is necessary under the current strategy. Consider, for instance, the
following family of sets:
 {1, 3} {1, 2} {2, 4}

{1} {2}

∅

Notice that if F = {∅, {1, 3}, {2, 4}}, then F ∗ dominates a 2-tent T = {{1}, {2}, {1, 2}}. An
inspection of the figure shows that x = 1 is abundant, and the argument in the proof of 4.3 allows
one to create a map by sending {2} → {1}, and {2, 4} → {1, 3}, while ∅ starts off unassigned since

12 CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS

it is not in F ∗ ∪ T . However, UT was also left open for assignment in the argument, and so we may
send ∅ → UT to get the full injective map.

5. Acknowledgments

The author wishes to thank Washington & Lee University for its support through the Lenfest
Summer Research Grant. The author also wishes to thank the referee for their helpful remarks.

6. Declarations

6.1. Ethical Approval. Not applicable. This study does not involve human or animal subjects.

6.2. Funding. This study was partially supported by the Lenfest Summer Research Grant at Wash-
ington and Lee University. The Lenfest Grant is an internally awarded grant.

6.3. Availability of Data and Materials. Not applicable.

References

[1] Alweiss, R., Huang, B., Sellke, M.: Improved lower bound for frankl’s union-closed sets conjec-
ture. The Electronic Journal of Combinatorics 31 (2024) 2
[2] Arenas, F.G.: Alexandroff spaces. Acta Mathematica Universitatis Comenianae. New Series
68(1), 17–25 (1999) 9
[3] Balla, I., Bollob´as, B., Eccles, T.: Union-closed families of sets. J. Combin. Theory (Series A)
120, 531–544 (2013) 1
[4] Boˇsnjak, I., Markovi´c, P.: The 11-element case of frankl’s conjecture. Europ. J. Combin. 15
(2008) 1
[5] Bruhn, H., Schaudt, O.: The journey of the union-closed sets conjecture. Graphs and Combi-
natorics 31, 2043–2074 (2015) 2, 6
[6] Cambie, S.: Better bounds for the union-closed sets conjecture using the entropy approach
(2022). https://arxiv.org/abs/2212.12500 2
[7] Cambie, S.: Progress on the union-closed conjecture and offsprings in winter 2022-2023 (2023).
https://arxiv.org/abs/2306.12351 2
[8] Chase, Z., Lovett, S.: Approximate union closed conjecture (2022). https://arxiv.org/abs/
2211.11689 2
[9] Gilmer, J.: A constant lower bound for the union-closed sets conjecture (2022). https://arxiv.
org/abs/2211.09055 1
[10] Liu, J.: Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally
IID Coupling (2023). https://arxiv.org/abs/2306.08824 2
[11] Mehr, M.: A Note on the Union-closed Sets Conjecture (2023). https://arxiv.org/abs/2309.
01704 9, 10
[12] Poonen, B.: Union-closed families. Journal of Combinatorial Theory, Series A 59(2), 253–268
(1992) https://doi.org/10.1016/0097-3165(92)90068-6 2
[13] Roberts, I., Simpson, J.: A note on the union-closed sets conjecture. Australas. J. Combin. 47,
265–267 (2010) 1
[14] Sawin, W.: An improved lower bound for the union-closed set conjecture (2023). https://
arxiv.org/abs/2211.11504 2

CHAIN CONDITIONS AND OPTIMAL ELEMENTS IN GENERALIZED UNION-CLOSED FAMILIES OF SETS 13

[15] Tian, C.: Union-closed Sets Conjecture Holds for Height No More Than 3 and Height No Less
Than N − 1 (2022). https://arxiv.org/abs/2112.06659 2
[16] Yu, L.: Dimension-free bounds for the union-closed sets conjecture. Entropy 25(5), 767 (2023)
https://doi.org/10.3390/e25050767 2
