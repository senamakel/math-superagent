<!-- source: https://cgasa.sbu.ac.ir/article_85730_9c926c8729189f4e871a4fed07a012e5.pdf | converted from PDF -->

Volume 11, Special Issue Dedicated to Professor George A. Grätzer,

July 2019, 197-205.

Frankl’s Conjecture for a subclass of
semimodular lattices

Vinayak Joshi
∗ and B.N. Waphare

This article is dedicated to Prof. George A. Grätzer

Abstract. In this paper, we prove Frankl’s Conjecture for an upper semi-
modular lattice L such that |J(L) \ A(L)| ≤ 3, where J(L) and A(L) are the
set of join-irreducible elements and the set of atoms respectively. It is known
that the class of planar lattices is contained in the class of dismantlable lat-
tices and the class of dismantlable lattices is contained in the class of lattices
having breadth at most two. We provide a very short proof of the Conjecture
for the class of lattices having breadth at most two. This generalizes the
results of Joshi, Waphare and Kavishwar [9, Theorem 2.4] as well as Czédli
and Schmidt [6, Theorem 1].

1 Introduction

In 1979, Peter Frankl conjectured the following, known as the Union-Closed
Sets Conjecture or Frankl’s Conjecture.

* Corresponding author
Keywords: Union-Closed Sets Conjecture, Frankl’s Conjecture, semimodular lattice, ad-
junct operation.
Mathematics Subject Classiﬁcation[2010]: 06A07, Secondary: 05D05.
Received: 3 July 2018, Accepted: 1 November 2018.
ISSN: Print 2345-5853, Online 2345-5861.
© Shahid Beheshti University
 197

198 V. Joshi and B.N. Waphare

Union-Closed Sets Conjecture 1.1. Let F be a collection of subsets of
a ﬁnite set X such that F ∪ G ∈ F holds for all F, G ∈ F, that is, F is a
union-closed family. If |F| ≥ 2 then there is an element x in X such that at
least |F| /2 members F ∈ F satisfy x ∈ F .

Poonen [10] formulated the Conjecture in the language of lattice theory
and is equivalent to the Union-Closed Sets Conjecture.

Frankl’s Conjecture 1.2 (Poonen [10], Stanley [13]). In every ﬁnite lattice
L with |L| ≥ 2, there is a nonzero join-irreducible element j (that is j =
a ∨ b ⇒ j = a or j = b) such that |{x ∈ L : j ≤ x}| ≤ |L| /2.

Many partial results have been obtained by using lattice theoretic meth-
ods which solve the conjecture for special classes of lattices; see Abe [2], Abe
and Nakano [3] and Czédli and Schmidt [6]. Recently, Henning Bruhn and
Oliver Schaudt [5] wrote a nice survey on the journey of the Union-Closed
Sets Conjecture which lists around 50 articles related to this Conjecture.
However, it is unknown whether Frankl’s Conjecture is true for upper semi-
modular lattices and this case is supposed to be the diﬃcult one in the
lattice theoretic version of the Conjecture. Czédli and Schmidt [6] proved
this conjecture for large semimodular lattices.
Czédli and Schmidt [6] proved the Conjecture for planar upper semi-
modular lattice. In [4], Baker et al. proved that every planar lattice is
dismantlable. Rival [11] proved that a dismantlable lattice is of breadth at
most two.
Now, we provide the most trivial proof of the result which states that
every lattice of breadth two satisﬁes the Conjecture. In fact, this extends the
result of Joshi et al. [9, Theorem 2.4] which states that every dismantlable
lattice satisﬁes Frankl’s Conjecture. Note that in a lattice L, if 1 = j1 ∨ j2
for some j1, j2 ∈ J(L), then L is not necessarily of breadth two. Recently,
statement (A) of Theorem 1.3 is proved in [1, Corollary 1.11]. Here we
provide a diﬀerent proof of statement (A). In fact, we prove:

Theorem 1.3. Let L be a ﬁnite lattice with |L| ≥ 2.
(A) If the greatest element 1 of L is join-irreducible or is the join of two
join-irreducibles, then L satisﬁes Frankl’s Conjecture.
(B) If L is semimodular and |J(L) \ A(L)| ≤ 3, then L satisﬁes Frankl’s
Conjecture again.

Frankl’s Conjecture for a subclass of semimodular lattices 199

We feel that the method adopted to prove this result is eﬀective for the
case |J(L) \ A(L)| ≤ 3 and is diﬃcult to extend for the general case.
Throughout this paper, all lattices are assumed to be ﬁnite. For unde-
ﬁned notions and terminology, the reader is referred to Grätzer [7].

2 Frankl’s Conjecture

Now, we begin with the necessary deﬁnitions and terminology.

Deﬁnition 2.1. Let L be a lattice. By a ≺ b, we mean there is no c such
that a < c < b. An element a is an upper cover (a lower cover ) of b if b ≺ a
(a ≺ b). A lower cover of a is denoted by a−. A nonzero element p of L is
an atom if 0 ≺ p. Dually, an element d of L is a dual atom if d ≺ 1. The set
of atoms in L is denoted by A(L).
As usual, J(L) stands for the set of nonzero join-irreducible elements of
L. So an element x ∈ L belongs to J(L) if and only if it has the unique lower
cover, denoted by x−. Dually, the set of nonzero meet-irreducible elements
is denoted by M (L).
A lattice L is said to be large, if |L| > 5 · 2m−3, where m = |J(L)|.
We deﬁne x′ = ⋁{j− : x ≥ j ∈ J(L)} for x > 0. It is called the derivation
of x. On the other hand, if x > 0 then we can deﬁne the meet of all lower
covers of x. We write x+ for it.
Note that in a ﬁnite lattice L, every nonzero element is a join of join-
irreducible elements of L. We say that a set U ⊆ J(L) is an irredundant set
of x, if x = ⋁ U and x > ⋁(U \ {a}) for a ∈ U .
The breadth of a lattice L is the least positive integer m such that any
n⋁

i=1 xi, xi ∈ L, n ≥ m, is always a join of m of the xi’s.

Lemma 2.2 (Stern [14, Corollary 6.5.3, p.254]). In an upper semimodular
lattice L, x+ ≤ x′ for every nonzero x ∈ L.

Proof of Theorem 1.3. (A) If the greatest element 1 is join-irreducible
then nothing to prove.
Now, assume that 1 = j1 ∨ j2 be an irredundant representation, j1, j2 ∈
J(L). If |[j1)| ≤ |L|/2 then nothing to prove. Suppose |[j1)| > |L|/2. Then
|L \ [j1)| < |L|/2. Clearly, [j2) \ {1} ⫋ L \ [j1), as j−
1 , the unique lower cover

200 V. Joshi and B.N. Waphare

of j1, is in L \ [j1) but j−
1 /∈ [j2). This proves that |[j2)| ≤ |L|/2. This proves
that every lattice of at most breadth two satisﬁes the conjecture.

(B): Now, assume that L is a upper semimodular lattice with |J(L)\A(L)| ≤
3.
 We consider the following two cases.
Case I: Suppose there is an irredundant representation of 1 that contains
an atom, say, p. Let U be an irredundant set of 1 such that p ∈ U . Then
1′ = ⋁
{j−
i : ji ∈ J(L) \ A(L)}, because p− = 0 for p in A(L). Clearly,
1′ ≤ 1. If 1′ = 1, then 1 = 1′ = ⋁{j−
i : ji ∈ J(L) \ A(L)} ≤ ⋁{ji : ji ∈

J(L) \ A(L)}. Hence 1 = ⋁(J(L) \ A(L)
), a contradiction to the fact that

U is an irredundant set of 1 containing an atom p. Hence 1′ < 1. Therefore
there is j ∈ J(L) such that j ̸≤ 1′. Let x ∈ L such that j ≤ x ≤ 1. By
Lemma 2.2, we have x+ ≤ x′. Therefore j ̸≤ x+, otherwise j ≤ x+ ≤ x′ ≤ 1′,
a contradiction. But then there is y(x) such that y(x) ≺ x and j ∨ y(x) = x.
This deﬁnes a 1-1 correspondence from [j) to L \ [j). Hence |[j)| ≤ |L \ [j)|.
In this case we are done.

Case II: Suppose no irredundant representation of 1 contains an atom.
Let U be an irredundant set of 1 and p ̸∈ U for every p ∈ A(L). By the
assumption |J(L) \ A(L)| ≤ 3 and by part (A), we have only possibility
U = {j1, j2, j3}, where jk ∈ J(L) \ A(L), k = 1, 2, 3.

Subcase II(a): Let U = {j1, j2, j3} = J(L) \ A(L). Then 1 = j1 ∨ j2 ∨ j3,
as p ̸∈ U for any p ∈ A(L).

Without loss of generality, choose j1 ∈ J(L) \ A(L) and let Ux be some
irredundant set of x. Note that an element may have more than one irre-
dundant sets.
We prove that for every x ∈ [j1), if at least one irredundant set Ux of x
contains some atom p ∈ L such that p < j1 or j1 ∈ Ux, then we are through.
For this, assume that x ∈ [j1) with Ux be its irredundant set such that Ux
contains either an atom p < j1 or j1. In case p ∈ Ux, put y(x) = ⋁(Ux \{p}).
Then x = p ∨ y(x) ≤ j1 ∨ y(x) ≤ x. Thus x = j1 ∨ y(x) in either the case.
This proves that x ↦→ y(x) is a 1-1 correspondence from [j1) to L\[j1). Thus
in this case, j1 is the required join-irreducible element, and we are done.

Frankl’s Conjecture for a subclass of semimodular lattices 201

Now, assume that there is some x with x ∈ [j1) and no irredundant set
Ux of x contains j1 or an atom p with p < j1.
Let Ux be any irredundant set of x with the above property.
Further, if both of j2 and j3 are in Ux, then j1 ≤ x =⋁(Ux \{j2, j3})∨j2 ∨j3. This gives 1 = j1 ∨j2 ∨j3 ≤ ⋁(Ux \{j2, j3})∨j2 ∨j3.
Note that (Ux \ {j2, j3}) ⊆ A(L), as J(L) \ A(L) = {j1, j2, j3}. Then 1 has
an irredundant representation which contains at least one atom, a contra-
diction.
Thus without loss of generality, assume that j2 ∈ Ux and j3 /∈ Ux. In
this case, j1 ≤ x = ⋁(Ux \ {j2}) ∨ j2. But again, 1 = j1 ∨ j2 ∨ j3 ≤⋁(Ux \{j2})∨j2 ∨j3. Since j1, j3 /∈ Ux, we have Ux \{j2} ⊆ A(L). Therefore
1 has an irredundant representation which contains at least one atom, again
a contradiction.
Hence j1, j2, j3 ̸∈ Ux. Then x = q1 ∨ · · · ∨ qm for qi ∈ A(L) and for some
m ∈ N. Since j1 ≤ x, we have 1 = j1∨j2∨j3 ≤ x∨j2∨j3 ≤ j2∨j3∨q1∨· · ·∨qm,
again a contradiction to the fact that 1 has an irredundant representation
which contains an atom. Thus we are done in this case also.
This completes the proof.

Essentially, Czédli and Schmidt [6] proved:

Lemma 2.3. If L is a large semimodular lattice, then |J(L) \ A(L)| ≤ 1.

As an immediate consequence of Theorem 1.3 and Lemma 2.3, we have
the following result of Czédli and Schmidt [6].

Corollary 2.4. Let L be a large semimodular lattice. Then L satisﬁes
Frankl’s Conjecture.

Now, we need the following deﬁnition of an adjunct operation to prove
that Frankl’s Conjecture is true for adjunct of lattices.

Deﬁnition 2.5 (Thakare et al. [15]). If L1 and L2 are two disjoint ﬁnite
lattices and (a, b) is a pair of elements in L1 such that a < b and a ̸≺ b.
Deﬁne the partial order ≤ on L = L1 ∪ L2 with respect to the pair (a, b) as
follows. For x, y ∈ L, we say x ≤ y in L if either x, y ∈ L1 and x ≤ y in L1;
or x, y ∈ L2 and x ≤ y in L2; or x ∈ L1, y ∈ L2 and x ≤ a in L1; or
x ∈ L2, y ∈ L1 and b ≤ y in L1.

202 V. Joshi and B.N. Waphare

It is easy to see that L is a lattice containing L1 and L2 as sublattices.
The procedure of obtaining L in this way is called an adjunct operation of
L2 to L1. The pair (a, b) is called an adjunct pair and L is an adjunct of
L2 to L1 with respect to the adjunct pair (a, b) and we write L = L1]b
aL2.

We place the Hasse diagrams of L1, L2 side by side in such a way that
the greatest element 1L2 of L2 is at the lower position than b and the least
element 0L2 of L2 is at the higher position than a. Then add the coverings
1L2 ≺ b and a ≺ 0L2, as shown in Figure 1, to obtain the Hasse diagram of
L = L1]b
aL2.
 a

b

L1 L2

0L2

1L2
 a

b

L1]b
aL2
 0L2

1L2

Figure 1: Adjunct of two lattices L1 and L2

Note that the adjunct operation preserves all the covering relations of
the individual lattices L1 and L2. Also if x, y ∈ L2, then a ≺ 0L2 ≤ x ∧ y.
Hence x ∧ y ̸= 0 in L = L1]b
aL2. Moreover, J(L) ⊆ J(L1) ∪ J(L2) and if
b ∈ J(L1) then b ̸∈ J(L).

Deﬁnition 2.6. Let P and Q be disjoint posets. Let P ∪ Q be the union
with the inherited order on P and Q such that p < q for all p ∈ P and
q ∈ Q. Then it forms a poset called the linear sum of P and Q denoted by
P ⊕ Q.

Theorem 2.7. Let L1 be a lattice satisfying Frankl’s Conjecture with two
incomparable join-irreducible elements j1, j2 ∈ J(L1), that is, |[ji)| ≤ |L1|/2

Frankl’s Conjecture for a subclass of semimodular lattices 203

for i = 1, 2. Then L = L1]b
aL2 as well as L = L2 ⊕ L1 satisﬁes Frankl’s
Conjecture for any lattice L2.

Proof. Let L = L1]b
aL2 with (a, b) as an adjunct pair. By the assumption,
there exist two incomparable join-irreducible elements j1, j2 of L1 such that
|[ji)| ≤ |L1|/2 for i = 1, 2.
Without loss of generality, assume that j2 = a. Then j1 and j2 are
incomparable join-irreducible elements of L also and x ̸∈ [j1) for every x ∈
L2. In this case, |[j1)| ≤ |L|/2 and we are through.
Now, if j1 = b or j2 = b, then j1 or j2 is not in J(L). Without loss
of generality, assume that j2 = b. Then clearly j1 ∈ J(L) and j1 ̸≤ a, as
j1, j2 are incomparable. By the deﬁnition of an adjunct, we have x ̸∈ [j1) for
every x ∈ L2. Therefore |[j1)| ≤ |L|/2. Thus L = L1]b
aL2 satisﬁes Frankl’s
Conjecture.
Clearly, L = L2 ⊕ L1 satisﬁes Frankl’s Conjecture for any lattice L2.

Theorem 2 of [12] states that Frankl’s Conjecture is true for the class of
lattices satisfying the dual covering property, a more general class than the
class of lower semimodular lattices. A careful observation of the proof reveals
that, a stronger version of theorem is true. For the sake of completeness, we
provide the proof of it.

Theorem 2.8 ( [12]). Let L be a lattice with the greatest element 1 as a join-
reducible element and satisﬁes the dual covering property. Then L satisﬁes
Frankl’s Conjecture with two incomparable elements j1, j2 ∈ J(L), that is,
|[ji)| ≤ |L|/2 for i = 1, 2.

Proof. Since 1 is a join-reducible element, there are at least two dual atoms,
say d1, d2. Hence there are two join-irreducible elements such that ji ≤ di
for i = 1, 2 and jk ̸≤ di for i ̸= k. Clearly, j1, j2 are incomparable. From the
proof of Theorem 2 of [12], it is clear that these join-irreducible elements
j1, j2 serves the purpose.

In view of Theorem 2.7 and Theorem 2.8, we have the following corollary.

Corollary 2.9. Let L1 be a lattice satisfying the dual covering property with
1 as a join-reducible element. Then L = L1]b
aL2 satisﬁes Frankl’s Conjecture
for any lattice L2 with (a, b) as an adjunct pair.

204 V. Joshi and B.N. Waphare

Acknowledgement

The ﬁrst author is ﬁnancial supported by DST(SERB) via MATRICS
PROJECT ﬁle number MTR/2017/000251.

References

[1] Abdollahi, A., Woodroofe, R., and Zaimi, G., Frankl’s Conjecture for subgroup lat-
tices, Electron. J. Combin. 24(3) (2017), P3.25.

[2] Abe, T., Strong semimodular lattices and Frankl’s Conjecture, Algebra Universalis
44 (2000), 379-382.

[3] Abe, T. and Nakano, B., Lower semimodular types of lattices: Frankl’s Conjecture
holds for lower quasi-modular lattices, Graphs Combin. 16 (2000), 1-16.

[4] Baker, K.A., Fishburn, P.C., and Roberts, F.S., Partial orders of dimension 2,
Networks 2 (1972), 11-28.

[5] Bruhn, H. and Schaudt, O., The journey of the Union-Closed Sets Conjecture,
Graphs Combin. 31 (2015), 2043-2074.

[6] Czédli, G. and Schmidt, E.T., Frankl’s conjecture for large semimodular and pla-
nar semimodular lattices, Acta Univ. Palack. Olomuc. Fac. Rerum Natur. Math. 47
(2008), 47-53.

[7] Grätzer, G., “General Lattice Theory”, Birkhäuser, 1998.

[8] Hunh, A.P., Schwach distributive Verbdnde-I, Acta Sci. Math. (Szeged) 33 (1972),
297-305.

[9] Joshi, V., Waphare, B.N., and Kavishwar, S.P., A proof of Frankl’s Union-Closed
Sets Conjecture for dismantlable lattices, Algebra Universalis 76 (2016), 351-354.

[10] Poonen, B., Union-closed families, J. Combin. Theory Ser. A. 59 (1992), 253-268.

[11] Rival, I., Combinatorial inequalities for semimodular lattices of breadth two, Algebra
Universalis 6 (1976), 303-311.

[12] Shewale, R.S., Joshi, V., and Kharat, V.S., Frankl’s conjecture and the dual covering
property, Graphs Combin. 25(1) (2009), 115-121.

[13] Stanley, R.P., “Enumerative Combinatorics”, Vol I. Wadsworth & Brooks/Cole Ad-
vanced Books & Software, 1986.

[14] Stern, M., “Semimodular Lattices”, Encyclopedia of Mathematics and its Applica-
tions, Cambridge University Press, 1999.

Frankl’s Conjecture for a subclass of semimodular lattices 205

[15] Thakare, N.K., Pawar, M.M., and Waphare, B.N., A structure theorem for disman-
tlable lattices and enumeration, Period. Math. Hungar. 45(1-2) (2002), 147-160.

Vinayak Joshi, Department of Mathematics, Savitribai Phule Pune University, Pune-411007,

India.

Email: vvjoshi@unipune.ac.in; vinayakjoshi111@yahoo.com

B.N. Waphare, Department of Mathematics, Savitribai Phule Pune University, Pune-411007,

India.

Email: bnwaphare@unipune.ac.in; waphare@yahoo.com
