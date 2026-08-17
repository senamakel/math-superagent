<!-- source: https://arxiv.org/pdf/2309.01704 | converted from PDF -->

arXiv:2309.01704v3  [math.CO]  9 Sep 2023
A Note on the Union-closed Sets Conjecture

Mohammad Javad Moghaddas Mehr

Email: m.moghadas11235@gmail.com

September 4, 2023

Abstract
Let M be a non-zero binary matrix with distinct rows where the rows
are closed under certain logical operators. In this article, we investigate the
existence of columns containing an equal or greater number of ones than zeros.
Speciﬁcally, the existence of such columns when the rows of the matrix are
closed under material conditional leads us to a weaker version of the Union-
Closed Set Conjecture.

Keywords: union-closed sets conjecture, binary matrix, logical operators, material
conditional

1 Introduction

For an integer, n ∈ N, we deﬁne the set [n] as {k ∈ N | k ≤ n}. A family F ⊆ 2[n] is
called union-closed if A, B ∈ F implies that A ∪ B ∈ F . In 1979, P´eter Frankl [4] posed
a seemingly straightforward conjecture that, over four decades later, still stands as an
unsolved puzzle despite substantial eﬀorts and progress dedicated to its understanding.
The conjecture states as follows.

Conjecture 1.1. For every non-empty ﬁnite union-closed family of sets, there exists an
element that belongs to at least half of the sets in the family.

Eﬀorts to understand the conjecture have led to notable breakthroughs. We recom-
mend the survey paper by Bruhn and Schaudt [2] for details. Vuckovic and Zivkovic [9]
demonstrated the conjecture’s validity for any union-closed family F ⊆ 2[n] where n ≤ 12.
Roberts and Simpson [7] established that if q is the minimum cardinality of ⋃ F taken
over all counterexamples F , then any counterexample F has cardinality at least 4q − 1.

1

In 2017, Ilan Karpas [6] showed that there exists some absolute constant c > 0 such
that for any union-closed family F ⊆ 2[n], if |F| ≥ ( 1
2 − c
) 2n, then there is an element
i ∈ [n] that appears in at least half of the sets in F.

Recently, Gilmer [5] established the ﬁrst constant lower bound for the conjecture, as-
serting the existence of an element that belongs to at least 0.01 of the sets in the family.
Gilmer claimed that his method could enhance the lower bound to (3 − √
5) /2 ≈ 0.38. A
few days later, three preprints were published and veriﬁed his claim [1, 3, 8].

In this note, we explore binary matrices whose rows are closed under diﬀerent logical
operators. To do so, we need some fundamental deﬁnitions.

Deﬁnition 1.1. Let A = (aij) and B = (bij) be two binary matrices of size n × m,

1. Let ¬A := (¬aij).

2. Let A ∗ B := (aij ∗ bij) for binary operator ”∗”.

Let M = (mij) be a matrix. We denote Mi− and M−j as the rows and columns of M,
respectively. From this perspective, we can restate Conjecture 1.1 as follows.

Conjecture 1.2. Let M = (mij) be a non-zero binary matrix of size n × m with distinct
rows. If for any arbitrary pair of rows Mi− and Mj− we have Mi− ∨ Mj− as a row of M,
then there exists a column M−k that contains at least n/2 ones.

Finally in Section 7 we will establish a weaker version of Conjecture 1.2 by proving the
following theorem.

Theorem 1.1. Let M = (mij) be a non-zero binary matrix of size n × m with distinct
rows. If for any arbitrary pair of rows Mi− and Mj− we have ¬Mi− ∨ Mj− as a row of
M, then there exists a column M−k that contains at least n/2 ones.

Let M be the set of all binary matrices, and denote N be the set of all ﬁnite subsets of
natural numbers. Deﬁne ψ : M → N as follows

ψ(Mn×m) =
 { n∑

i=1 mij | j ∈ [m]

}
 .

Example 1.1. Let A be a family of sets as follows

A = {∅, {1}, {1, 2}, {2, 3, 4}, {1, 2, 3, 4}}

which is union-closed.
 2 of 11

The matrix representation of A will be

A =
 







0 0 0 0
1 0 0 0
1 1 0 0
0 1 1 1
1 1 1 1










then ψ(A) = {2, 3}, so max(ψ(A)) ≥ 5/2. Thus, Conjecture 1.2 holds in this case.

If Conjecture 1.2 holds for matrix A, then any row and column permutation of A also
satisﬁes the Conjecture’s conditions.

Deﬁnition 1.2. Matrix A is equivalent to matrix B, denoted as A ∼ B, if B can be
obtained from A through row and column permutations.

We refer to the pair (M, ∗) as a space, where M = (mij) is a non-zero binary matrix of
size n × m, such that its rows are closed under ”*” operator. This operator can be either
binary or unary.

2 Negation (¬)

In this section, we will prove our ﬁrst lemma, which serves as a useful tool and provides
valuable insights for dealing with other cases.

Negation Lemma 2.1. For every space (Mn×m, ¬) we have max(ψ(M )) ≥ n/2.

Proof. Without loss of generality, assume that M−j ̸= 0 for each j ∈ [m]. Deﬁne two sets
K and L as follows
 K := {Mi− | mi1 = 1}

L := {Mi− | mi1 = 0}.

If L = ∅ there is nothing to prove, so let L ̸= ∅. Deﬁne matrix K such that its rows
come from K while preserving their order in M. We deﬁne matrix L from L in the same
manner, then
 M ∼
 (K
L
 )
 .

For any row Kt− there is exactly one row Ls− such that Kt− = ¬Ls−, and vice versa.

3 of 11

This establishes a mutual correspondence between the rows of K and the rows of L, thus

K ∼ ¬L

which forces M to have an even number of rows and an equal number of ones and zeros
in each column. So n = 2k for some k ∈ N, then ψ(M ) = {k}. Thus

max(ψ(M )) = k.
 ■

3 Alternative denial (↑) and Joint denial (↓)

In this section, we will utilize Lemma 2.1 to explore the properties of two binary oper-
ators, Alternative Denial and Joint Denial.

Proposition 3.1. For every space (Mn×m, ↑) we have max(ψ(M )) ≥ n/2.

Proof. Since rows of M are closed under ”↑”, then for an arbitrary Mi− we have

Mi− ↑ Mi− = ¬Mi−

which means rows of M are closed under ”¬”. By applying the Lemma 2.1, we can
conclude max(ψ(M )) ≥ n/2. ■

Proposition 3.2. For every space (Mn×m, ↓) we have max(ψ(M )) ≥ n/2.

Proof. Since rows of M are closed under ”↓”, then for an arbitrary Mi− we have

Mi− ↓ Mi− = ¬Mi−

which means rows of M are closed under ”¬”. By applying the Lemma 2.1, we can
conclude max(ψ(M )) ≥ n/2. ■

4 Abjunction (̸→) and Conjunction (∧)

In this section, we provide two examples to demonstrate that when rows are closed
under Abjunction or Conjunction, it does not guarantee the existence of a column with
an equal or greater number of ones than zeros.

4 of 11

Example 4.1. Let A be the binary matrix

A(n+1)×n =
 (In×n
01×n
)

then for n > 1
 max(ψ(A)) = 1 < (n + 1)/2

but the rows of matrix A are closed under abjunction and conjunction.

For an arbitrary k ∈ N, there exists a matrix A such that its rows are closed under
conjunction and max(ψ(A)) = k + 1.

Example 4.2. Let A be the binary matrix

A(n+2)×(n+1) =
 





 Jk×1
0(n−k)×1 In

1
0 02×n
 






so max(ψ(A)) = k + 1. For instance, for k = 2

A7×6 =
 












 1
1
0
0
0
 1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1
0 0 0 0 0 0
0 0 0 0 0
 













thus
 max(ψ(M )) = 3 < 7/2.

5 Biconditional (↔) and Exclusive or (̸↔)

In this section, we will explore two logical operators that form an additive group on
rows of a binary matrix.

Proposition 5.1. For every space (Mn×m, ↔) we have max(ψ(M )) ≥ n/2.

Proof. Deﬁne matrices K and L, as in the proof of the Lemma 2.1, so

5 of 11

M ∼
 (K
L
 )
 .

Deﬁne the function g as follows
 g : L → K

g(Lt−) = L1− + Lt−.

If g(A) = g(B) then L1− + A = L1− + B. Since {Mi−}i∈[n] is an additive group, then
A = B. So g is injective, and as a result,

|L| ≤ |K|.

Thus
 max(ψ(M )) ≥ (|K| + |L|)/2

= n/2.
 ■

Proposition 5.2. For every space (Mn×m, ̸↔) we have max(ψ(M )) ≥ n/2.

Proof. Deﬁne matrices K and L, as in the proof of the Lemma 2.1 , so

M ∼
 (K
L
 )
 .

Deﬁne the function g as follows
 g : L → K

g(Lt−) = K1− + Lt−.

If g(A) = g(B) then K1− + A = K1− + B. Since {Mi−}i∈[n] is an additive group, then
A = B. So g is injective, and as a result,

|L| ≤ |K|.

Thus
 max(ψ(M )) ≥ (|K| + |L|)/2

= n/2.
 ■

6 of 11

6 Topology (∪, ∩)

If F ⊆ 2[n] is a family of sets that is closed under ”∪” and ”∩”, it implies that we may
deﬁne a topology on ⋃ F . However, being closed under ”∪” and ”∩” doesn’t guarantee
that ∅ ∈ F . Nevertheless, if ⋂ F ̸= ∅, then there exists an a ∈ ⋃ F such that it belongs
to each member of F .

Theorem 6.1. Let (X, τ ) be a ﬁnite topological space, then there exists an x0 ∈ X that
appears in at least half of the members of τ .

Proof. Without loss of generality, assume X = [n] for some n ∈ N. Let X be a family
of members of τ with the minimum cardinality among the members of τ , excluding the
empty set. We select the smallest set B ∈ X according to the lexicographic order. It is
guaranteed that for A ∈ τ , we have either B ⊆ A or B ∩ A = ∅. Deﬁne sets K and L as
follows
 K = {A ∈ τ | B ⊆ A}

L = {A ∈ τ | B ∩ A = ∅}.

If L = ∅, there is nothing to prove, so let L ̸= ∅. Deﬁne the function g as follows

g : L → K

g(A) = B ∪ A.

If g(A) = g(C), then A ∪ B = C ∪ B. Since B has an empty intersection with A and C,
then A = C. So g is injective, and as a result, |L| ≤ |K|, thus members of B appear in at
least half of the members of τ . ■

Corollary 6.1. Let M be a non-zero binary matrix of size n × m, where its rows are
closed under ”∧” and ”∨”, then max(ψ(M )) ≥ n
2 .

7 Material Conditional (→)

In this section, we will establish our main result. Before proceeding, we need some tools
that will help us move forward more easily.

Let Mn×m be a non-zero binary matrix. We deﬁne ̃Mn×m = ¬M. If rows of M are
closed under the binary operator ”*”, then rows of ̃M would also be closed under the
binary operator ”̃∗” deﬁned as follows
 7 of 11

̃∗( ̃A, ̃B) := ¬ ∗ (A, B)

where ̃A, ̃B ∈ { ̃Mi−}i∈[n] and A, B ∈ {Mi−}i∈[n].

Example 7.1. Let (Mn×m, ∗) be a non-zero space such that for A, B ∈ {Mi−}i∈[n],
∗(A, B) = ¬A ∨ B. Then for ̃A, ̃B ∈ { ̃Mi−}i∈[n]

̃∗( ̃A, ̃B) = ¬ ∗ (A, B) = ¬(¬A ∨ B) = ¬ ̃A ∧ ̃B.

Deﬁnition 7.1. Let F be a non-empty ﬁnite family of sets. A basis for the family F is
a disjoint collection B = {Bi}i∈γ of members of F such that for every member A in F ,
there exists an index set α ⊆ γ such that A = ⋃
i∈α Bi.

Deﬁnition 7.2. Let Mn×m be a non-zero binary matrix. A basis for the matrix M is a
collection V = {vi}i∈γ of rows of M , where vt and vk are orthogonal for t ̸= k, such that
for every row A of M , there exists an index set α ⊆ γ such that A = ⋁i∈α vi.

Proposition 7.1. Let F be a ﬁnite family of sets. If F has a basis, then it is unique.

Proof. Suppose F has two diﬀerent bases B = {Bi}i∈γ and C = {Ci}i∈λ. Without loss of
generality, let Ct ∈ C such that Ct /∈ B, so

Ct = ⋃

j∈α Bj,

where Bj ̸= Ct and
 Bj = ⋃

i∈βj Ci

where Ci ̸= Ct. Then
 Ct = ⋃

j∈α
 ⋃

i∈βj Ci = ⋃

i∈∪j∈αβj Ci

where Ci ̸= Ct. So Ct is represented by other members of C , which is a contradiction. ■

Proposition 7.2. Let F be a non-empty ﬁnite family of sets such that for A, D ∈ F ,
A − D ∈ F and A ∩ D ∈ F . Then F has a unique basis B = {Bi}i∈γ, where for every
A ∈ F there is a unique index set α ⊆ γ such that A = ⋃
i∈α Bi. So A is uniquely
determined by members of B.

Proof. We construct B inductively. Start with F0 = F . In each step, let Fi+1 be obtained
from Fi by removing an element C that can be expressed as the union of other elements
of Fi. This process terminates in less than |F | steps. Let B = {Bi}i∈γ, which is obtained
from the last step, so the members of F can be represented as the union of members of
B.
 8 of 11

Assume there is a distinct pair Bt, Bk ∈ B such that Bt ∩ Bk ̸= ∅. Without loss of
generality, we can assume Bt − Bk ̸= ∅. Deﬁne A1 = Bt − Bk and A2 = Bt ∩ Bk, obviously
A1 and A2 are proper subsets of Bt and A1, A2 ∈ F , hence they can be represented by
members of B, so A1 = ⋃i∈α Bi, A2 = ⋃
i∈β Bi where Bi ̸= Bt for i ∈ α ∪ β. Thus

Bt = A1 ∪ A2 = ⋃

i∈α∪β Bi

where Bi ̸= Bt. So Bt is represented by members of B which is a contradiction, so diﬀerent
members of B have empty intersection.

It remains to show that every A ∈ F is uniquely determined by members of B = {Bi}i∈γ.
Assume A = ⋃i∈α Bi and A = ⋃
j∈β Bj where α, β ⊆ γ and α ̸= β. Let Bk ∈ {Bi}i∈α thus
Bk ⊆ ⋃j∈β Bj so there is Bt ∈ {Bj}j∈β such that Bk ∩ Bt ̸= ∅ which is a contradiction. So
A is uniquely determined by members of B. ■

Corollary 7.1. Let Mn×m be a non-zero binary matrix such that for A, B ∈ {Mi−}i∈[n],
A ∧ ¬B ∈ {Mi−}i∈[n] and A ∧ B ∈ {Mi−}i∈[n]. Then M has a unique basis V = {vi}i∈γ,
where for every A ∈ {Mi−}i∈[n] there is a unique index set α ⊆ γ such that A = ⋁i∈α vi.
So A is uniquely determined by members of V.

In the following proposition, we will demonstrate the necessary conditions for the matrix
̃M , corresponding to the space (Mn×m, →), to have a basis.

Proposition 7.3. Let (Mn×m, →) be a non-zero space. Then

1. For ̃A, ̃B ∈ { ̃Mi−}i∈[n] we have ̃A ∧ ¬ ̃B ∈ { ̃Mi−}i∈[n].

2. For ̃A, ̃B ∈ { ̃Mi−}i∈[n] we have ̃A ∧ ̃B ∈ { ̃Mi−}i∈[n].

Proof. We conclude (1) from Example 7.1.
(2) Let ̃A, ̃B ∈ { ̃Mi−}i∈[n]. By (1) ̃A ∧ ¬( ̃A ∧ ¬ ̃B) ∈ { ̃Mi−}i∈[n]. Since

̃A ∧ ¬( ̃A ∧ ¬ ̃B) = ̃A ∧ (¬ ̃A ∨ ̃B)

= ̃A ∧ ̃B

then ̃A ∧ ̃B ∈ { ̃Mi−}i∈[n]. ■

Remark 7.1. Let (Mn×m, →) be a non-zero space. Then ̃M has a basis V = {vi}i∈γ by
Proposition 7.3 and Corollary 7.1.
 9 of 11

Remark 7.2. Suppose M = (mij) be a non-zero binary matrix of size n × m and k ∈ [m].
Clearly ∑n
i=1 mik ≥ n/2 if and only if ∑n
i=1 ̃mik ≤ n/2.

Theorem 7.1. For every space (M, →) we have max(ψ(M )) ≥ n/2.

Proof. Let V = {vi}i∈γ be a basis for ̃M . We deﬁne sets K and L as follows

K := { ̃Mi−| for ̃Mi− = ⋁

i∈α vi, where 1 ∈ α}

L := { ̃Mj−| for ̃Mj− = ⋁

j∈β vj, where 1 /∈ β}.

Clearly K and L are well deﬁned, due to the unique representation of rows of ̃M by
members of V. Deﬁne matrix K where its rows come from K while preserving their order
in ̃M .
We deﬁne matrix L from L in the same manner, then

̃M ∼
 (K
L
 )
 .

Deﬁne function g as follows
 g : K → L

g( ̃Mk−) = ̃Mk− ∧ ¬v1.

Since vt ∧ vk = 0 for any two distinct members vt, vk ∈ V and every row of ̃M has a unique
representation, we conclude that g is an injective function. So |K| ≤ |L| which means v1
appears in equal or less than half of rows of ̃M . Thus, there is a column ̃M−t ∈ { ̃M−j}j∈[m]
such that ∑n
i=1 ̃mit ≤ n/2. So by Remark 7.2

n∑

i=1 mit ≥ n/2

which implies that
 max(ψ(M )) ≥ n/2.
 ■

We end this paper by mentioning that Theorem 7.1 provides a weaker version of Con-
jecture 1.2. To see this, consider a binary matrix M where ¬A ∨ B ∈ {Mi−}i∈[n] for
A, B ∈ {Mi−}i∈[n]. By Proposition 7.3, we also know that ¬A ∧ ¬B ∈ { ̃Mi−}i∈[n]. So we
can conclude that A ∨ B ∈ {Mi−}i∈[n].
 10 of 11

References

[1] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for the union-
closed sets conjecture. arXiv:2211.11731, 2022.

[2] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets conjecture.
Graphs and Combinatorics, 31:2043–2074, 2015.

[3] Zachary Chase and Shachar Lovett. Approximate union closed conjecture.
arXiv:2211.11689, 2022.

[4] P. Frankl. Extremal set systems. Handbook of Combinatorics, 2:1293–1329, 1995.

[5] Justin Gilmer. A constant lower bound for the union-closed sets conjecture.
arXiv:2211.09055, 2022.

[6] Ilan Karpas. Two results on union-closed families. arXiv:1708.01434, 2017.

[7] Ian Roberts and Jamie Simpson. A note on the union-closed sets conjecture. Aus-
tralasian Journal of Combinatorics, 47:265–267, 2010.

[8] Will Sawin. An improved lower bound for the union-closed set conjecture.
arXiv:2211.11504, 2022.

[9] Bojan Vuckovic and Miodrag Zivkovic. The 12-element case of frankl’s conjecture.
IPSI BgD Transactions on Internet Research, 13:65–71, 01 2017.

11 of 11
