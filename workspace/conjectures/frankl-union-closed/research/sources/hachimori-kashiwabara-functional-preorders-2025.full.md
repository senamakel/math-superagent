<!-- source: https://arxiv.org/pdf/2511.19833 | converted from PDF -->

Average-Rare Order Ideals in Functional Preorders

Masahiro Hachimori ∗

Kenji Kashiwabara†

Abstract

We prove that for the preorder induced by a function f : V → V , the family of all order
ideals is average-rare, that is, its normalized degree sum (NDS) is nonpositive. As a base
case in our reduction, we establish the same result for functional partial orders (or rooted
forests). We also propose a conjecture related to Frankl’s Conjecture. All proofs have
been formally verified in the proof assistant Lean 4.

1 Introduction

In this paper, all the sets, set families, partially ordered sets, and preordered sets are finite.
Frankl’s Conjecture [6] is a longstanding open problem in extremal set theory. The
conjecture states that a union-closed family that contains the ground set V and the empty set
must contain an abundant element, that is, an element that appears in at least half of the sets
of the family.
For a set family F ⊆ 2V , we define the degree deg(u) of an element u ∈ V to be the
number of sets containing u. Equivalently, the conjecture states that a union-closed family
that contains the ground set V and the empty set must contain an element u with

deg(u)
|F| ≥ 1/2.

Progress on the conjecture has been steady but partial. Reimer [13] obtained a general lower
bound via combinatorial averaging. The conjecture is settled for small families by Bošnjak and
P. Marković [2], Vučković and Živković [16], and Roberts and Simpson [14].
Bruhn and Schaudt [3] provide an excellent survey. More recently, Gilmer [7] introduced an
entropy-based approach and showed a positive constant lower bound, and this was sharpened
to 3−
√5
2 by several authors [1, 4, 5, 11, 12, 15, 17] as conjectured in [7]. The authors [8] gave a
systematic study of minimality concepts related to the conjecture.

The conjecture is usually phrased for union-closed families as above, but we work with
the dual, intersection-closed form. In the intersection-closed form, the conjecture states that
any intersection-closed family of sets that contains the ground set V and the empty set must
contain a rare element, that is, an element that appears in at most half of the sets of the

∗Institute of Systems and Information Engineering, University of Tsukuba, Email:hachi@sk.tsukuba.ac.jp
†Corresponding author, Graduate School of Arts and Sciences, The University of Tokyo, Email:
cashiwa@g.ecc.u-tokyo.ac.jp
 1arXiv:2511.19833v1  [math.CO]  25 Nov 2025
family. Equivalently, the conjecture states that any intersection-closed finite family of sets that
contains the ground set V and the empty set contains an element u such that

deg(u)
|F| ≤ 1/2.

The equivalence of the conjecture is straightforward by considering the family of complements
{V − F | F ∈ F}.
Let us consider the average value of deg(u)/|F| over all u ∈ V . If this average value is at
most 1/2, we say F is average-rare. More precisely, F is average-rare if
∑u∈V deg(u)/|F|
|V | ≤ 1
2 .

If F is average-rare, then the existence of a rare element is deduced. Hence, the average-rarity
is a stronger property than the existence of a rare element.
Since we have ∑

u∈V deg(u) = ∑

F ∈F |F |

by a double-counting argument, to be average-rare is equivalent to

2 ∑

F ∈F |F | ≤ |F||V |.

We define the normalized degree sum by

NDS(F) := 2 ∑

F ∈F|F | − |F| |V |.

By this, NDS(F) ≤ 0 if and only if F is average-rare. This NDS is a useful tool in studying
average-rarity. Previously, the authors used NDS in showing the average-rarity of “ideal families”
in [9]. (The “ideal families” in [9] are not families of order ideals, unlike in this paper.)

Frankl’s conjecture is usually phrased for union-closed families, but in this paper we work
with the dual and state it for intersection-closed families. This is because we intend to work
within the framework of the closure systems.

Definition 1.1. A closure system is a family of sets that is closed under intersection and
contains the ground set.

Frankl’s conjecture can be equivalently stated as follows: every closure system on a finite
set that contains the empty set as a member has a rare element.
Closure systems can be represented using rooted sets. Rooted sets provide a convenient
combinatorial encoding of closure systems.

Definition 1.2. A rooted set is a pair (A, r) consisting of a set A ⊆ V and a root r /∈ A. We
call A the stem. A collection of rooted sets is called a family of rooted sets.

It is better to note that in many contexts a rooted set is defined in such a way that r is
included in A (that is, (A ∪ {r}, r) is called a rooted set in such contexts), but in this paper
we exclude the root r from the stem A.
The following lemma is well-known. The proof is straightforward.

2

Lemma 1.3. For a family of rooted sets {(Ai, ri)} on a finite set V ,
{ F ⊆ V ∣
∣ Ai ⊆ F ⇒ ri ∈ F for all i ∈ I}

is a closure system. Conversely, every closure system admits a representation by a family of
rooted sets.

The rooted set (Ai, ri) here means that a set F of the closure system containing Ai must
also contain ri. The lemma above states that a closure system is defined by constraints of this
type.
Note that a closure system can be represented by different families of rooted sets. When a
family A of rooted sets represents a closure system F, we say A generates F.
If in a generating family of rooted sets every stem has size 1, such as ({w}, v), then the
constraints for the closure system are of the type that a set F containing an element w must
contain v. This equivalently means that such a generating family of rooted sets defines a
preorder on V : define a binary relation by v ⋖ w if and only if ({w}, v) is in the generating
family of rooted sets, and take the reflexive-transitive closure of this relation defines a preorder
on V . (A preorder is a partial order without requiring antisymmetry (i.e., x ≤ y and y ≤ x
do not imply x = y).) Further, the closure system defined by such a family of rooted sets
corresponds to the family of order ideals of the preordered set as follows.

Definition 1.4. For a preordered set (V, ≤), I ⊆ V is an order ideal if x ∈ I and y ≤ x implies
y ∈ I. The family of order ideals I(V, ≤) is

I(V, ≤) := { I ⊆ V | x ∈ I, y ≤ x ⇒ y ∈ I }.

Note that both the empty set ∅ and the whole set V always belong to I(V, ≤).

Lemma 1.5. For a preordered set, the family of order ideals is a closure system. Moreover,
the following are equivalent: being representable as a family of order ideals, and being generated
by a family of rooted sets all of whose stems are singletons.

Proof. That it is a closure system follows from the fact that the family of all order ideals is
closed under intersection and contains the whole set.
If a closure system is represented as the family of order ideals of a preorder, then using
the cover relation x ⋖ y one obtains a generating family of rooted sets by taking {({y}, x)}.
Conversely, if a closure system is represented by a family of rooted sets with singleton stems, one
forms a binary relation by directing each rooted pair ({y}, x) as x ≤ y; its reflexive–transitive
closure is a preorder whose order ideals are exactly the given closure system.

In this paper, we focus on functional preorders, preorders arising from a function f : V → V .
Given a function f , we define a preorder as the reflexive-transitive closure of the covering
relations v ⋖ f (v) for each v ∈ V with f (v) ̸= v. Equivalently, a preorder is defined such that
the family of order ideals is generated by the family { ({f (v)}, v) : v ∈ V, f (v) ̸= v }. Our
Main Theorem (Theorem 2.8) shows that the order-ideal family I(V, ≤) of such a preorder
is always average-rare. The proof reduces to the Secondary Main Theorem (Theorem 2.9),
which handles the special case where the preorder is a rooted forest (a partial order where each
element has at most one cover). All arguments have been formally verified in Lean 4, which
can be found in our repository [10].
 3

The rest of this paper is structured as follows. Section 2 introduces functional preorders
and states the Main Theorem. Section 3 outlines the reduction to rooted forests, and Section 4
provides the inductive proof of the Secondary Main Theorem. Section 5 summarizes the formal
verification, and Section 6 discusses a conjectural extension related to Frankl’s Conjecture.

2 Functional Preorders and the Main Theorem

Let V be a finite set and let f : V → V be a function on V .

Definition 2.1. Set v ⋖ w ⇔ f (v) = w for f (v) ̸= v. The reflexive–transitive closure defines
a preorder ≤. We call (V, ≤) the functional preorder induced by f .

Lemma 2.2. For any v, w ∈ V ,

v ≤ w ⇔ ∃k ≥ 0 : f k(v) = w,

where f k denotes the k-fold composition of f (with f 0 the identity).

Write v ∼ w when v ≤ w and w ≤ v; this defines an equivalence relation on V . If we define
a digraph, the functional graph of f , on V such that an arc is defined from v to w if f (v) = w
(v ̸= w), then the equivalence classes are the strongly connected components of the functional
graph of f .

Definition 2.3. In a preorder, an element u ∈ V is maximal if u ≤ v implies v ≤ u.

Lemma 2.4. In a functional preorder, the elements of any equivalence class of size ≥ 2 are
maximal elements.

Proof. Let u be an element of an equivalence class of size ≥ 2 and not maximal. Since u is non-
maximal, there exist v and u′ with f (u′) = v and u′ ∼ u but v ≰ u′. On the other hand, there
exists w ∈ V such that w ̸= u′ and w ∼ u′, i.e., w ≤ u′ and u′ ≤ w. That means f k(u′) = w
for some k > 1 by Lemma 2.2. Then, f k−1(v) = w since f k(u′) = (f k−1 ◦ f )(u′) = f k−1(v).
This means v ≤ w, and therefore v ≤ u′, which contradicts v ≰ u′.

Note that the equivalence class of a maximal element u is a singleton in a functional
preorder induced by f if and only if f (u) = u.
In a preorder, the condition that there is no pair of distinct elements u and v with u ∼ v is
equivalent to the condition that the preorder satisfies antisymmetry. In other words, a preorder
is a partial order if every equivalence class is a singleton. A partially ordered set is called a
poset. A functional preorder is a functional partial order if it is a partial order. In a functional
partial order induced by f , the maximal elements are those u with f (u) = u.

The following three examples show preorders (partial orders) that are functional and not
functional, respectively. These are illustrative examples that indicate functionality is needed
for the average-rarity as in our main theorem.

Example 2.5 (A two-element chain). Let V = {a, b} with f (a) = b and f (b) = b. This
induces an order relation a < b. The order ideals of the preorder (in fact, partial order) ≤
induced by f are I(V, ≤) = {∅, {a}, {a, b}},

and NDS(I(V, ≤)) = 2 · (0 + 1 + 2) − 3 · 2 = 0, so the family is average-rare.

4

Example 2.6 (The case of a preorder). Let V = {a, b, c} with f (a) = b, f (b) = c, and f (c) = b.
Then a preorder is induced by f such that a < b, a < c, and b ∼ c. The order ideals of the
preorder are I(V, ≤) = {∅, {a}, {a, b, c}},

and NDS(I(V, ≤)) = 2 · (0 + 1 + 3) − 3 · 3 = −1 < 0, so the family is average-rare.

Example 2.7 (A non-functional rooted-set family). Take V = {a, b, c} and rooted sets ({b}, a),
({c}, a). This determines preorder (in fact, partial order) ≤ induced by the two covering
relations a ⋖ b and a ⋖ c. The resulting ideal family is

I(V, ≤) = {∅, {a}, {a, b}, {a, c}, {a, b, c}}

giving NDS(I(V, ≤)) = 2 · (0 + 1 + 2 + 2 + 3) − 5 · 3 = 1 > 0, hence it is not average-rare. This
is not functional because the element a has two distinct covers, b and c.

The following is our main theorem.

Theorem 2.8 (Main Theorem). For any finite set V and function f : V → V , the order-ideal
family I(V, ≤) of the induced functional preorder satisfies

NDS
(I(V, ≤)
) ≤ 0.

We prove the Main Theorem (Theorem 2.8) by reducing to the following Secondary Main
Theorem (Theorem 2.9).

Theorem 2.9 (Secondary Main Theorem). Let (V, ≤) be a functional partial order. Then

NDS
(I(V, ≤)
) ≤ 0.

The reduction of the Main Theorem to the Secondary Main Theorem is given in Section 3,
and the Secondary Main Theorem will be proved in Section 4.
We say a poset is a rooted forest if its Hasse diagram is acyclic and each connected
component has a unique maximal element, where the unique maximal element is the root of
the component. Here, we remark that a poset is functional if and only if it is a rooted forest,
as shown in the following lemma. Hence, the Secondary Main Theorem can be equivalently
stated that the family of order ideals of a rooted forest is average-rare.

Lemma 2.10. A partial order on a finite set is functional if and only if it is a rooted forest,
i.e., its Hasse diagram is acyclic (as an undirected graph) and each connected component has a
unique maximal element.

Proof. Consider the Hasse diagram of the poset as a directed graph by orienting each edge of
the Hasse diagram from the lower vertex to the upper vertex. By this, the Hasse diagram of a
poset will be an acyclic digraph (i.e., a digraph with no directed cycles).
Suppose first that (V, ≤) is functional. Then every element has at most one outgoing edge
in its Hasse diagram. If the Hasse diagram contains a (undirected) cycle, then, each vertex
on the cycle has exactly one outgoing edge to another vertex on the cycle, forming a strongly
connected component of size at least two. This contradicts the antisymmetry of the partial
order. Hence, the Hasse diagram is acyclic as an undirected graph.

5

Moreover, in a finite acyclic digraph, each connected component must contain a sink, a
vertex of out-degree zero. Such a vertex is a maximal element of that component. If there are
two distinct maximal elements in the same component, there is an undirected path connecting
the two vertices on the Hasse diagram. Then, a minimal element among the vertices of the
path is found on an internal vertex of the path, since the end vertices are maximal elements
and cannot be minimal. This minimal element must have two outgoing edges, contradicting
the functionality. Thus, each connected component has a unique maximal element.
Conversely, assume that the Hasse diagram is acyclic as an undirected graph and that each
connected component has a unique maximal element r. Acyclicity implies that each component
is a finite tree. In each tree, from every vertex there exists a path to r going upward, since r
is the unique maximal element in the component. Since there exists only one path between
two vertices in a tree, this shows that each vertex has at most one outgoing edge in the Hasse
diagram. Therefore, the partial order is functional. This proves the equivalence.

If the Hasse diagram of a poset (V, ≤) has two or more connected components, then the
poset can be expressed as a disjoint union (C1, ≤1) + (C2, ≤2) with V = C1 ⊔ C2, where ≤1
and ≤2 are the restrictions of the order relation ≤ to C1 and C2, respectively. (The disjoint
union (C1, ≤1) + (C2, ≤2) is the poset on V = C1 ⊔ C2 with the order relation ≤ such that
x ≤ y if x, y ∈ C1 and x ≤1 y, or if x, y ∈ C2 and x ≤2 y.)

3 Reduction to Secondary Main Theorem

In this section, we reduce the proof of the Main Theorem (Theorem 2.8) to that of the Secondary
Main Theorem (Theorem 2.9).

Lemma 3.1. For any maximal element u of a preordered set (V, ≤), u is a rare element in
I(V, ≤).

Proof. Let U be the equivalence class containing u. Define a map

Φ : { I ∈ I(V, ≤) | u ∈ I } −→ { J ∈ I(V, ≤) | u /∈ J }

by Φ(I) := I \ U.

Here, Φ(I) is an order ideal not containing u by maximality of u, and if Φ(I1) = Φ(I2) then
I1 = I2, since every element of U appears in the same ideals simultaneously. This implies
that Φ is injective, and hence, the number of ideals containing u is at most the number not
containing u. Therefore, degI(u) ≤ 1
2 |I(V, ≤)|, i.e., u is rare.

Definition 3.2. Given a set family F on V , two elements u, v ∈ V are parallel in F if

{F ∈ F | u ∈ F } = {F ∈ F | v ∈ F }.

We say v, different from u, is a parallel partner of u if u and v are parallel.

The following lemma is straightforward.

Lemma 3.3. For the family of order ideals I(V, ≤) for any preorder, u ∼ v (i.e., both u ≤ v
and u ≥ v) if and only if u and v are parallel in I(V, ≤).

6

In the reduction, we use the following operator to the family of order ideals of the functional
preorder.

Definition 3.4. For x ∈ V and a family F ⊆ 2V , we define the traced family at x by

tracex(F) := { F \ {x} | F ∈ F }.

The following is the key lemma in the reduction.

Lemma 3.5. If u has a parallel partner in F, the trace map

Φu : F → traceu(F)

defined by F ↦→ F \ {u} is injective

Proof. Assume I1 \ {u} = I2 \ {u}. If I1 ̸= I2 they differ only by u. But then their memberships
of the parallel partner v would also differ, contradicting parallelism. Hence I1 = I2.

This implies that, if u has a parallel partner, then tracing preserves the number of sets and
all degrees except that of u. This is the key property to show the following lemma.

Lemma 3.6. Let (V, ≤) be a functional preorder and let u lie in an equivalence class of size at
least 2. Write V ′ := V \ {u}. Then:

(i) there is a function g : V ′ → V ′ such that the preorder ≤′ on V ′ induced by g has
I(V ′, ≤′) = traceu(I(V, ≤)) (the preorder ≤′ is functional induced by g), and

(ii) NDS
(I(V, ≤)
) ≤ NDS
(I(V ′, ≤
′)).

Remark that (i) of the lemma states that (V ′, ≤′) is a functional preorder.

Proof.

(i) Let the preordered set (V, ≤) be induced by f : V → V , and let g : V ′ → V ′ be defined
by g(x) = f (x) when f (x) ̸= u and g(x) = f 2(x) when f (x) = u. It can be easily verified
that the preordered set (V ′, ≤′) induced by this g is a restriction of (V, ≤) on V ′. This g
is a required function. Indeed, if I ∈ I(V, ≤), then it is easy to see that I \ {u} is an
order ideal in I(V ′, ≤′). On the other hand, if I ′ ∈ I(V ′, ≤′), then by letting

I =
 {
I ′ ∪ {u} if f (u) ∈ I ′,
I ′ otherwise.

I is an order ideal in I(V, ≤) and I \ {u} = I ′. Hence, I(V ′, ≤′) = traceu(I(V, ≤)).

(ii) By Lemma 3.5, the trace map

Φu : I(V, ≤) → I(V ′, ≤
′), I ↦→ I \ {u}

is injective when u has a parallel partner. Therefore |I(V, ≤)| = |I(V ′, ≤′)|.

Since I(V ′, ≤′) is the result of removing u from all ideals in I(V, ≤), we have
∑

I∈I(V,≤) |I| = ∑

I ′∈I(V ′,≤′) |I ′| + deg(u),

7

and we have |V | = |V ′| + 1. Hence,

NDS(I(V, ≤)) = 2 · ∑

I∈I(V,≤) |I| − |I(V, ≤)| |V |

= 2
 

 ∑

I ′∈I(V ′,≤′) |I ′| + deg(u)


 − |I(V ′, ≤
′)| (|V ′| + 1)

=
 

2 · ∑

I ′∈I(V ′,≤′) |I ′| − |I(V ′, ≤
′)| |V ′|



 + 2 deg(u) − |I(V, ≤)|

= NDS(I(V ′, ≤
′)) + 2 deg(u) − |I(V, ≤)|.

By Lemma 2.4, u is a maximal element of (V, ≤), and by Lemma 3.1, u is rare in I(V, ≤).
The rarity of u gives 2 deg(u) ≤ |I(V, ≤)|, and substituting this into the above expression
yields NDS(I(V, ≤)) ≤ NDS(I(V ′, ≤
′)),

as desired.

Proof of the Main Theorem from the Secondary Main Theorem.
With Lemma 3.6 in hand, repeatedly tracing out nontrivial equivalence classes reduces the
size of each equivalence class to one. This reduces the Main Theorem (Theorem 2.8) to the
Secondary Main Theorem (Theorem 2.9) since a preorder such that each equivalence class is a
singleton is a partial order.

What remains is the proof of the Secondary Main Theorem (Theorem 2.9), which is given
in Section 4.

4 Proof of the Secondary Main Theorem

We now prove the Secondary Main Theorem (Theorem 2.9), namely, NDS
(I(V, ≤)) ≤ 0 for
every rooted-forest poset (V, ≤). The argument proceeds by induction on the number of
vertices n = |V |, using four technical lemmas.
For the following lemma, note that a connected rooted-forest poset, i.e., a rooted-forest
poset such that the Hasse diagram is connected, has a unique maximal element by Lemma 2.10.

Lemma 4.1. Let (V, ≤) be a connected rooted-forest poset. Let the unique maximal element
be x, and denote V ′ := V \ {x}. Then (V ′, ≤′) is a functional poset, where ≤′ is a partial order
restricting the order relation ≤ to V ′, and

NDS
(I(V, ≤)
) = NDS(I(V ′, ≤
′)
) + (|V | − |I(V, ≤)| + 1).

8

Proof. Since (V, ≤) is a connected rooted forest, there is a function f : V → V that induces
the partial order, with f (x) = x for the unique maximal element x.
Let g : V ′ → V ′ be defined by

g(v) =
 {
f (v) if f (v) ̸= x,
v if f (v) = x.

Then it is easily verified that the order relation induced by g is exactly the order relation ≤′

that restricts the order relation induced by g on V ′ = V \ {x}. Hence (V ′, ≤′) is a functional
poset.

Since the only difference of (V, ≤) and (V ′, ≤′) is the element x, the number of order ideals
not containing x is the same. The only order ideal containing x is the whole V in I(V, ≤) since
x is the unique maximal element in (V, ≤). Therefore, we have

|I(V, ≤)| = |I(V ′, ≤
′)| + 1, ∑

I∈I(V,≤)|I| = ∑

I ′∈I(V ′,≤′)
|I ′| + |V |.

Let n := |V |, n′ := |V ′| = n − 1, m′ := |I(V ′, ≤′)|, m := |I(V, ≤)| = m′ + 1, and

S′ := ∑

I ′∈I(V ′,≤′)
|I ′|, S := ∑

I∈I(V,≤)|I| = S′ + n.

Then
 NDS(I(V, ≤)) − NDS(I(V ′, ≤
′)) = (2(S′ + n) − (m
′ + 1)n) − (2S′ − m′n′)

= 2n − (m′ + 1)n + m
′n′

= n − m′(n − n′) = n − m
′

= |V | − |I(V ′, ≤
′)| = |V | − (|I(V, ≤)| − 1)

= |V | − |I(V, ≤)| + 1.

Rearranging yields the stated identity.

Lemma 4.2. For any finite poset (V, ≤), |I(V, ≤)| ≥ |V | + 1.

Proof. Let Iv = {u ∈ V : u ≤ v}, i.e., the principal ideal of v. The injection v ↦→ Iv gives |V |
mutually distinct non-empty ideals by antisymmetry. Adding the empty ideal completes the
bound.

Lemma 4.3. For set families F1, F2 (on a common finite ground set U ),
∑

A∈F1
 ∑

B∈F2|A ∪ B| = |F2| ∑

A∈F1|A| + |F1| ∑

B∈F2|B| − ∑

A∈F1
 ∑

B∈F2|A ∩ B|.

Proof. For each A ⊆ U and B ⊆ U we have the identity |A∪B| = |A|+|B|−|A∩B|. Summing
over all ordered pairs (A, B) ∈ F1 × F2,
 9

∑

A∈F1
 ∑

B∈F2|A ∪ B| = ∑

A∈F1
 ∑

B∈F2
(|A| + |B| − |A ∩ B|
)

= ∑

A∈F1
 ∑

B∈F2|A| + ∑

A∈F1
 ∑

B∈F2|B| − ∑

A∈F1
 ∑

B∈F2|A ∩ B|

= |F2| ∑

A∈F1|A| + |F1| ∑

B∈F2|B| − ∑

A∈F1
 ∑

B∈F2|A ∩ B|.

Lemma 4.4. If a poset (V, ≤) decomposes as a disjoint union of two non-empty posets,
(V, ≤) = (C1, ≤1) + (C2, ≤2), then

NDS
(I(V, ≤)
) = |I(C2, ≤2)| NDS
(I(C1, ≤1)
) + |I(C1, ≤1)| NDS
(I(C2, ≤2)).

Proof. Since (C1, ≤1) and C2, ≤2) are disjoint, an order ideal I of (V, ≤) is decomposed as
I = I1 ⊔ I2 with I1 ∈ I(C1, ≤1) and I2 ∈ I(C2, ≤2). Hence,

|I(V, ≤)| = |I(C1, ≤1)| · |I(C2, ≤2)|.

The statement follows from Lemma 4.3.

Proof of the Secondary Main Theorem (Theorem 2.9).
The proof is by induction on n = |V |.
When n = 1, I = {∅, V } and NDS(I) = 0.
When n ≥ 2, assume the theorem is true for all rooted forests with fewer than n vertices.

- If (V, ≤) is disconnected, then it can be expressed by a disjoint union as (V, ≤) = (C1, ≤1)
+ (C2, ≤2) with V = C1 ⊔ C2, and each (Ci, ≤i) has non-positive NDS by the induction
hypothesis. Hence NDS(I(V, ≤)) is non-positive by Lemma 4.4 and the non-positivity of
NDS(I(C1, ≤1)) and NDS(I(C2, ≤2)).

- If (V, ≤) is connected, let x be the unique maximal element. Let V ′ = V \ {x} and ≤′

be the restriction of ≤ to V ′. By Lemma 4.1, Lemma 4.2, and the induction hypothesis,
we have
 NDS(I(V, ≤)) = NDS(I(V ′, ≤
′)) + (|V | − |I(V, ≤)| + 1)

≤ NDS(I(V ′, ≤
′)) ≤ 0.

10

5 Lean 4 Formalization

The validity of all theorems and lemmas in this paper is machine-checked in the proof assistant
Lean 4. Using proof assistants offers several advantages. First, they ensure the rigor of the
proofs, as every inference is validated by Lean’s kernel, eliminating overlooked edge cases and
computational errors. They also ensure reproducibility. The proof scripts are plain text and
can be replayed by anyone to obtain a formal verification. Moreover, the codes used for the
proofs can be reused by others, as the relevant definitions and lemmas are incorporated into
the community library mathlib4, thereby accelerating future work on Frankl-type problems.
We briefly describe the formalized code used in our proofs. The Lean code snippets below
are simplified for readability and exposition. For the complete and precise formalization, please
refer to the source code in the repository https://github.com/kashiwabarakenji/avg-rare.

SetFamily

structure SetFamily where
ground : Finset α
sets : Finset α → Prop

Structure SetFamily provides a family of subsets of a finite ground set. SetFamily.sets
is the predicate that determines whether a given subset is in the family.

Normalized Degree Sum (NDS)

def NDS (F : SetFamily α) : Int :=
2 * F.totalHyperedgeSize - F.numHyperedges * F.ground.card

The above code is the definition of the normalized degree sum (NDS):

NDS(F) := 2 ∑

F ∈F |F | − |F| · |V |.

NDS measures the average-rarity of elements in a set family. When NDS ≤ 0, the family is
average-rare. F.ground.card means the cardinality of the ground set. Int represents the set
of all integers. In the above, NDS returns an integer value.

FuncSetup

structure FuncSetup (α : Type) where
ground : Finset α
f : ground → ground

Structure FuncSetup provides the assumption for our problem, including the ground set
and the function f : V → V on the ground set. It induces the preorder FuncSetup.le on the
ground set.
 11

Order Ideal

def isOrderIdealOn (S: FuncSetup α) (le : α → α → Prop) (I : Finset α) : Prop :=
I ⊆ S.ground ∧
∀x, x ∈ I → ∀y, y ∈ S.ground → S.le y x → y ∈ I

This is the condition of the order ideal

I ⊆ V ∧ (∀x ∈ I, ∀y ∈ V, y ≤ x ⇒ y ∈ I).

FuncSetup.idealFamily is the set of all order ideals defined using isOrderIdealOn.

Main Theorem

theorem main_nds_nonpos {α : Type}
(S : FuncSetup α) :
(S.idealFamily).NDS ≤ 0 := by
apply Reduction.main_nds_nonpos_of_secondary
intro T hT
have hT’ : isPoset T := by
dsimp [isPoset]
dsimp [has_le_antisymm]
exact T.antisymm_of_isPoset hT
exact secondary_main_theorem T hT’

This is the Main Theorem of our paper: for any function f : V → V , the induced order ideal
family I is always average-rare: NDS(I(V, ≤)) ≤ 0.

(S:FuncSetup α) is the assumption of the statement, placed before the colon.
(S.idealFamily).NDS <= 0 is the conclusion of the statement. The codes followed by
“:=” are the proof of the statement. Proof codes consist of tactics in Lean 4. Theorem
theorem main_nds_nonpos_of_secondary in the repository is the reduction theorem for prov-
ing the Main Theorem from the Secondary Main Theorem.

Secondary Main Theorem

theorem secondary_main_theorem {α : Type}
(S : FuncSetup α) (hpos : isPoset S) :
(S.idealFamily).NDS ≤ 0

Assumption isPoset S means that the order relation of S is a partial order. This statement is
the Secondary Main Theorem: for any functional poset (rooted forest poset), the induced order
ideal family is always average-rare. This assumption is stronger than that of the Main Theorem.
The Secondary Main Theorem is also used as a lemma for proving the Main Theorem.

During the formalization, we made extensive use of AI-assisted tools, notably ChatGPT 5
(for brainstorming tactics and diagnosing type errors), Lean Copilot (for interactive tactic
completion), and GitHub Copilot (for boilerplate suggestions). These tools drastically reduced
the development time, from what would have taken months by hand to only a few weeks,

12

while correctness is uncompromised since all suggested fragments are checked by Lean’s kernel.
Our experience shows that recent AI tools have made Lean 4 formalization of advanced
combinatorial mathematics practically feasible. Without them, the scale of the present project
would likely have been out of reach. We therefore regard this as evidence that AI-assisted
proof development is becoming an essential methodology in formal mathematics.

6 Conclusion and Future Directions

In this paper, we have proved that every functional preorder, a preorder generated by a
function f : V → V , induces a family of order ideals that is average-rare. Average-rarity is a
stronger condition than the existence of a rare element. The existence of a rare element in the
order-ideal family of a preordered set in general can be shown rather easily (Lemma 3.1). That
is, Frankl’s conjecture holds for the order-ideal family of any preordered set. On the other
hand, average-rarity does not hold for the order-ideal family of any preordered set, as observed
in Example 2.7. In this paper we confirmed the average-rarity for the order-ideal family of a
functional preordered set (Main Theorem (Theorem 2.8)). This includes the case for functional
posets, equivalently, for rooted-forest posets (Secondary Main Theorem (Theorem 2.9)).
The order-ideal family of a preordered set is equivalently rephrased as an intersection-closed
family represented by rooted sets such that the stems are singletons (Lemma 1.5). Further,
if the preorder is functional, then each element is a root of at most one rooted set in the
representation. Extending this approach, a natural next step toward broader cases is to consider
rooted sets with stems of larger size. We have the following conjecture.

Conjecture 6.1. Let C be an intersection-closed family on a finite ground set V that contains
∅ and admits a rooted-set representation in which every element of V is the root of at most
one rooted set. Then C is average-rare.

In this setting of the conjecture, the existence of a rare element, that is, Frankl’s conjecture
for this case, is still an open problem. A positive answer to the conjecture would confirm
Frankl’s conjecture for this special case. Under the condition of the conjecture, if there exists
an element such that it is the root of no rooted set, then such an element is easily shown to be
rare. Hence, it is enough to consider the case in which each element is the root of exactly one
rooted set if one aims to verify Frankl’s conjecture for this case.

References

[1] R. Alweiss, B. Huang, and M. Sellke, Improved lower bound for Frankl’s union-closed sets
conjecture. Electron. J. Combin. 31 (2024), P3.35. doi:10.37236/12232

[2] I. Bošnjak, P. Marković, The 11-element case of Frankl’s conjecture, Electron. J. Combin.
15 (2008), R88. doi:10.37236/812

[3] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture. Graphs
Combin. 31, 2059–2084 (2015). doi:10.1007/s00373-014-1515-0

[4] S. Cambie, Better bounds for the union-closed sets conjecture using the entropy approach
(2022). arXiv:2212.12500
 13

[5] Z. Chase and S. Lovett. Approximate union-closed conjecture (2022). arXiv:2211.11689

[6] P. Frankl. Extremal set systems. In R. L. Graham, M. Grötschel, and L. Lovász (eds.),
Handbook of Combinatorics, vol. 1, pp. 1293–1329. Elsevier, 1995.

[7] J. Gilmer. A constant lower bound for the union-closed sets conjecture (2022). arXiv:
2211.09055

[8] M. Hachimori and K. Kashiwabara. Several minimality concepts related to Frankl’s
conjecture. Graphs Combin. 40 (6), Article 130 (2024). doi:10.1007/s00373-024-02834-0

[9] M. Hachimori and K. Kashiwabara. On the averaging problem of ideal families related to
Frankl’s conjecture with formal proof by Lean 4 (2025). arXiv:2504.13454

[10] K. Kashiwabara. avg-rare: Lean 4 formalization. GitHub repository (2025). https:
//github.com/kashiwabarakenji/avg-rare

[11] J. Liu, Improving the lower bound for the union-closed sets conjecture via conditionally
IID coupling, 58th Annual Conference on Information Sciences and Systems (CISS), IEEE,
2024, pp.7-12. doi:10.1109/CISS59072.2024.10480167

[12] L. Pebody, Extension of a method of Gilmer (2022). arXiv:2211.13139

[13] D. Reimer. An average set size theorem. Combin. Probab. Comput. 12 (1), 89–93 (2003).
doi:10.1017/S0963548302005230

[14] I. T. Roberts, J. Simpson, A note on the union-closed sets conjecture. Australas. J. Combin.
47 (2010), 265-267.

[15] W. Sawin. An improved lower bound for the union-closed set conjecture (2022, rev. 2023).
arXiv:2211.11504

[16] B. Vučković, M. Živković. The 12-element case of Frankl’s conjecture. IPSI Transactions
on Internet Research 13 (2017), 65–71.

[17] L. Yu, Dimension-free bounds for the union-closed sets conjecture. Entropy 25 (2023), 767.
doi:10.3390/e25050767
 14
