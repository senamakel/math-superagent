<!-- source: https://zenodo.org/records/20800102/files/frankl-conjecture-audit.pdf?download=1 | converted from PDF -->

AUDITING TWO CLAIMED PROOFS OF FRANKL’S
CONJECTURE
AND STRUCTURAL REDUCTIONS FOR MINIMAL
COUNTEREXAMPLES

NELSON DANIEL SPENCE

Abstract. We audit two proposed proof mechanisms for Frankl’s union-
closed sets conjecture and give explicit finite counterexamples to their
central claims. First, a 5 × 4 binary matrix has distinct rows, distinct
columns, and no all-zero column; the recursive algorithm A2 of Abdu-
rakhmanov returns True on this matrix, although every column contains
only two ones and hence no column is heavy. This refutes the Heavy
Column Theorem in the form used by a subsequent claimed proof of
Frankl’s conjecture. Second, the intersection-closed family

{∅, {1}, {2}, {3}}

violates the recursive upper bound asserted in Schrader’s discarding-set
argument.
We then record structural reductions for a counterexample having the
minimum possible number of member sets. Such a counterexample has
odd cardinality 2k + 1. Moreover, deleting any member whose removal
preserves union-closure exposes an element outside that member with
frequency exactly k. Thus every removable member omits a maximum-
frequency element. In the dual lattice formulation we prove a further
deletion lemma: every two meet-irreducible elements have a common tight
join-irreducible below them, where tight means that the corresponding
principal filter has size k + 1. Consequently, if there are exactly three
tight coordinates, every meet-irreducible is incident with at least two
of them, and each of the three two-element incidence patterns occurs.
None of the results below resolves Frankl’s conjecture.

1. Introduction

A finite family F of finite sets is union-closed if

A, B ∈ F =⇒ A ∪ B ∈ F.

For an element x of the ground set, write

dF (x) = ∣
∣{A ∈ F : x ∈ A}
∣
∣.

2020 Mathematics Subject Classification. 05D05, 05B20, 06A07, 06B05.
Key words and phrases. Frankl’s conjecture, union-closed sets, minimal counterexample,
binary matrix, proof audit.
Project Navi, nelson@projectnavi.ai. Preprint, June 22, 2026. This paper does not
claim a proof of Frankl’s conjecture. Licensed under CC BY 4.0.
1

2 NELSON DANIEL SPENCE

Frankl’s conjecture is the following.

Conjecture 1.1 (Frankl). If F ̸= {∅} is a finite union-closed family, then
some element x satisfies
 dF (x) ≥ |F|
2 .

The conjecture, originating with Frankl [6], remains open despite sub-
stantial partial progress; see the survey of Bruhn and Schaudt [5], the
entropy breakthrough of Gilmer [7], and subsequent improvements such
as [3]. Its elementary formulation has also generated many claimed proofs.
Two recent examples are an algorithmic heavy-column approach of Abdu-
rakhmanov [2, 1] and a family of inequalities for intersection-closed systems
proposed by Schrader [11].
The purpose of this note is fourfold.
(i) We exhibit a small explicit counterexample to the heavy-column
implication used in [1].
(ii) We exhibit a four-member intersection-closed family on which the
main recursive bound of [11] fails.
(iii) We derive an odd-cardinality reduction for minimum counterexamples
and a tight-frequency witness for every removable member.
(iv) In the lattice formulation, we strengthen the common-lower-bound
condition for pairs of meet-irreducibles by forcing the common join-
irreducible to be tight.
The distinction between an audit and a disproof of Frankl’s conjecture
is important. The counterexamples below refute proof mechanisms, not
the conjecture. In particular, the matrix in Section 3 is not closed under
componentwise disjunction.
 2. Preliminaries

Let M be an m × n binary matrix. A column is heavy if it contains at
least ⌈m/2⌉ ones. Equivalently, the number of ones is at least the number of
zeros.
The incidence matrix of a union-closed family has one row per member
and one column per ground-set element. Union-closure is then closure of the
row set under componentwise disjunction. A heavy column is precisely an
element occurring in at least half the members.
We shall also use the following deletion notion.

Definition 2.1. A member A ∈ F is removable if F \ {A} is union-closed.
It is admissibly removable if, in addition, F \ {A} still contains a nonempty
member.

If ∅ ∈ F, then (F, ⊆) is a finite lattice: the join is set union, and the
meet of A, B ∈ F is the union of all members of F contained in A ∩ B. In
this normalized setting, a nonleast member is removable if and only if it is
join-irreducible.

AUDITING TWO CLAIMED PROOFS OF FRANKL’S CONJECTURE 3

3. A counterexample to the Heavy Column Theorem

3.1. The recursive predicate. We restate the behavior of Algorithm A2
used in [2, 1]. For a column i, let M 0
i and M 1
i denote the row submatrices
on which column i is respectively 0 and 1. Let M 0−
i and M 1−
i be obtained
by deleting column i.
The recursive predicate A2(M ) is evaluated as follows.

(A1) If M has one row and more than one column, return True.
(A2) If M has one column, return True exactly when that column has at
least as many ones as zeros.
(A3) Process the columns in order. For column i:
(a) if |M 0
i | = 1, return True;
(b) for each nonempty K ∈ {M 0−
i , M 1−
i }, return False if every
column of K has more zeros than ones;
(c) recursively evaluate every such K, returning False if any recur-
sive call returns False.
(A4) If no earlier return occurs, return True.

The claimed Heavy Column Theorem states that, for a binary matrix with
distinct rows, distinct columns, and no all-zero column,

A2(M ) = True =⇒ M has a heavy column.

3.2. The explicit matrix.

Proposition 3.1. Let
 M =
 






0 0 0 0
0 0 1 1
0 1 0 1
1 0 1 0
1 1 0 0







 .

Then M has distinct rows, distinct columns, and no all-zero column. Every
column has exactly two ones, so M has no heavy column. Nevertheless,

A2(M ) = True.

Proof. The structural hypotheses are immediate. Since M has five rows, a
heavy column must contain at least three ones; each column of M contains
exactly two.
At the top-level call, the zero and one fibers, after deleting the processed
column, are as follows. Row strings are written without separators.

i M 0−
i M 1−
i
1 {000, 011, 101} {010, 100}
2 {000, 011, 110} {001, 100}
3 {000, 011, 110} {001, 100}
4 {000, 101, 110} {001, 010}.

4 NELSON DANIEL SPENCE

Every displayed child has a column with at least as many ones as zeros, so
the immediate all-light test never returns False.
It remains to check the recursive calls. There are only six child types.

Rows Reason A2 returns True

{000, 011, 101} For each of the first two columns, the
children are {00, 11} and a one-row matrix;
these return True. The third column has a
unique zero.
{000, 011, 110} The first-column children are {00, 11} and a
one-row matrix; both return True. The
second column has a unique zero.
{000, 101, 110} The first column has a unique zero.
{010, 100} The first column has a unique zero.
{001, 100} The first column has a unique zero.
{001, 010} Its first column is all zero, producing the
child {01, 10}, which returns True; its
second column then has a unique zero.

The two-row matrix {00, 11} and the two-row matrix {01, 10} each return
True immediately from a column with a unique zero. A one-row matrix
with two columns returns True by the first base case. Consequently every
recursive child in the top-level computation returns True, and the top-level
loop terminates with True. □

Corollary 3.2. The Heavy Column Theorem quoted and applied in [1] is
false as stated. Therefore the claimed proof of Frankl’s conjecture in that
manuscript does not follow from its stated premises.

Remark 3.3. The row set of M is not closed under componentwise disjunction.
Thus Proposition 3.1 does not show that an appropriately strengthened
theorem restricted to disjunction-closed row sets is false. Such a strengthened
statement would contain essentially the unresolved combinatorial content,
and it requires an independent proof.

The example is also minimal in its number of rows.

Proposition 3.4. No matrix with fewer than five rows satisfies the hypotheses
of the Heavy Column Theorem, has no heavy column, and is accepted by A2.

Proof. For one or two rows, every nonzero column is heavy. Now let m ∈ {3, 4}
and suppose there is no heavy column. Every nonzero column then has exactly
one 1. Since columns are distinct, two columns cannot place their unique 1
in the same row.
Process any column i. Its one-fiber has one row, and after deleting column
i that row is all zero. If at least two columns are present, this one-row all-zero
child triggers the all-light test and A2 returns False. With only one column,
distinctness of all m ≥ 3 rows is impossible. Hence no such matrix exists. □

AUDITING TWO CLAIMED PROOFS OF FRANKL’S CONJECTURE 5

4. A counterexample to a discarding-set upper bound

Schrader [11] works in the dual, intersection-closed formulation. Let
N = [n], let F ⊆ 2N be intersection-closed, and write

Fi = {A ∈ F : i ∈ A},

with the ground set ordered so that |F1| ≥ · · · ≥ |Fn|. A set A ⊆ [i − 1] is
called discarding at level i when A ∈ F but A ∪ {i} /∈ F; let Di denote the
collection of such sets.
For a discarding set having no “root” in the terminology of [11], the excluded
collection is H A
i = {A ∪ {i} ∪ X : X ⊆ {i + 1, . . . , n}}.

The recursive quantity is initialized by t0 = 2n−1 and defined by

ti = ti−1 − ∑

A∈Di |H A
i |.

Theorem 5.1 of [11] asserts, among other things, that

ti ≥ |Fi| (1 ≤ i ≤ n).

Proposition 4.1. The asserted inequality ti ≥ |Fi| fails for the intersection-
closed family F = {∅, {1}, {2}, {3}}

on N = [3].

Proof. Each element has frequency one, so the required order |F1| ≥ |F2| ≥
|F3| is satisfied. We have t0 = 23−1 = 4 and D1 = ∅, hence t1 = 4.
At level 2, the only discarding set is {1}. It has no root, and

H {1}
2 = {{1, 2}, {1, 2, 3}}.

Thus t2 = 4 − 2 = 2.
At level 3, the discarding sets are {1} and {2}. Again they have no roots,
and H {1}
3 = {{1, 3}}, H {2}
3 = {{2, 3}}.

Therefore t3 = 2 − 1 − 1 = 0,

whereas |F3| = 1. Hence t3 ̸≥ |F3|. □

Remark 4.2 (Location of the accounting failure). The excluded collections
in the preceding example are pairwise disjoint, so disjointness is not the
missing property. The issue is that ti−1 is merely a numerical upper bound
inherited from a previous coordinate. To subtract |H A
i |, one must know that
the newly excluded sets lie inside a common candidate universe represented
by that bound. Disjointness from previously excluded sets does not establish
this containment. In the example, {2, 3} ∈ H {2}
3 was never among the four
subsets containing element 1 from which t0 was initialized.

6 NELSON DANIEL SPENCE

5. Reproducibility

The ancillary file verify_counterexamples.py contains a direct imple-
mentation of Algorithm A2 as restated in Section 3. It verifies the matrix in
Proposition 3.1, emits the complete recursive trace on request, reproduces
the discarding-set calculation in Proposition 4.1, and exhaustively checks the
row-minimality assertion of Proposition 3.4. The script uses only the Python
standard library. The mathematical arguments in the paper do not depend
on trusting a search heuristic or numerical approximation.

6. Minimum-cardinality counterexamples

We now turn from auditing to a constructive reduction. Assume for
contradiction that Frankl’s conjecture is false, and choose a counterexample
F with the minimum possible number of members. Write m = |F|.

Lemma 6.1. Every inclusion-minimal nonempty member A ∈ F is remov-
able.

Proof. Suppose B, C ∈ F \ {A} and B ∪ C = A. Then B, C ⊆ A. By
inclusion-minimality of the nonempty set A, each of B and C is either empty
or equal to A. Since A has been removed, both must be empty, which gives
B ∪ C = ∅ ̸= A. Therefore no union of two remaining members is A, and
deleting A preserves union-closure. □

Proposition 6.2 (A normalized minimum counterexample). If a minimum-
cardinality counterexample exists, then one exists with the same number of
members and with ∅ as a member.

Proof. If ∅ ∈ F, there is nothing to prove. Otherwise choose an inclusion-
minimal member A and set

G = (F \ {A}) ∪ {∅}.

By Lemma 6.1, G is union-closed. Every element frequency in G is no larger
than its frequency in F, so G remains a counterexample. It has the same
number of members. □

Theorem 6.3 (Odd-cardinality reduction). A minimum-cardinality coun-
terexample has odd cardinality.

Proof. Suppose m = 2k. Choose an inclusion-minimal nonempty member A.
By Lemma 6.1, the family F ′ = F \ {A}

is union-closed. It remains nontrivial, since a family with at most one
nonempty member cannot be a counterexample. By minimality of F , Frankl’s
conjecture holds for F ′, so some element x belongs to at least
⌈ 2k − 1
2
 ⌉ = k

AUDITING TWO CLAIMED PROOFS OF FRANKL’S CONJECTURE 7

members of F ′. It then belongs to at least k = m/2 members of F, contra-
dicting that F is a counterexample. □

Henceforth write |F| = 2k + 1.
Every element has frequency at most k.

Theorem 6.4 (Tight witness for deletion). Let A ∈ F be admissibly remov-
able. Then there exists an element xA /∈ A such that

dF (xA) = k.

Proof. The family F ′ = F \ {A} is a smaller nontrivial union-closed family,
so by the minimality of F it has an element xA with

dF ′(xA) ≥ |F ′|
2 = k.

Since F is a counterexample of size 2k + 1, every element has frequency at
most k in F. Thus dF ′(xA) = dF (xA) = k.
The equality of the two frequencies implies xA /∈ A. □

Definition 6.5. An element x is tight if dF (x) = k. Let

T = T (F) = {x : dF (x) = k}

denote the set of tight elements.

Corollary 6.6. The set T is nonempty, and every admissibly removable
member A satisfies T ⊈ A.
In particular, every inclusion-minimal nonempty member omits a tight ele-
ment.

Proof. Apply Theorem 6.4 to any inclusion-minimal nonempty member. The
same theorem gives the assertion for every admissibly removable member. □

Norton and Sarvate proved the stronger known fact that a minimum-
cardinality counterexample has at least three tight elements [10]. Theorem 6.4
is useful because it attaches a tight witness to every deletion, rather than
merely asserting that tight elements exist.

6.1. Lattice interpretation. Let L = (F, ⊆). A nonleast member A is
removable exactly when it is join-irreducible. Thus Corollary 6.6 gives an
incidence restriction between join-irreducible members and tight ground-set
elements: no join-irreducible member contains all of T .
There is also a complementary restriction in the intersection-closed lattice
formulation. Bouchard proved that in a minimum-size lattice counterexample,
every meet-irreducible lies above a join-irreducible whose principal filter
has cardinality (|L| + 1)/2 [4, Theorem 2.12]. Under the canonical set

8 NELSON DANIEL SPENCE

representation, these are precisely the tight coordinates on the intersection-
closed side.
We now strengthen the pairwise common-lower-bound conclusion of [4,
Corollary 2.11]. Let L be a minimum-size lattice counterexample. By
Theorem 6.3, write |L| = 2k + 1.
A join-irreducible j of L is called lattice-tight if

|(↑j)L| = k + 1.

Every join-irreducible has a principal filter of size at least k + 1.

Theorem 6.7 (Tight common lower bound). For any two distinct meet-
irreducible elements m1, m2 of L, there exists a lattice-tight join-irreducible j
such that j ≤ m1 and j ≤ m2.

Proof. Assume to the contrary that no lattice-tight join-irreducible lies below
both m1 and m2. Set ̂L = L \ {m1, m2}.

The subposet ̂L is a lattice because a set of meet-irreducible elements may
be deleted from a finite lattice [4, Theorem 1.4]. We show that every join-
irreducible ̂j of ̂L satisfies |(↑̂j)̂L| ≥ k.

Since |̂L| = 2k − 1, this would make ̂L a smaller counterexample.
First suppose that ̂j is already join-irreducible in L. If it is lattice-tight,
at most one of m1, m2 lies in (↑̂j)L by the contrary assumption, and hence
its filter in ̂L has size at least k. If it is not lattice-tight, then its filter in L
has size at least k + 2, so deleting two elements again leaves at least k.
It remains to consider a join-irreducible ̂j of ̂L that is join-reducible in L.
At least one deleted element, say m, lower covers ̂j in L; write m′ for the
other deleted meet-irreducible. Because m is meet-irreducible, ̂j is its unique
upper cover.
If m is join-irreducible, then it is doubly irreducible. By [4, Lemma 2.5],
m is lattice-tight. The contrary assumption gives m ≰ m′. Consequently
m′ /∈ (↑̂j)L, while m lies strictly below ̂j. Since

(↑m)L = {m} ˙∪ (↑̂j)L,

we obtain |(↑̂j)̂L| = |(↑̂j)L| = k.
Suppose instead that m is join-reducible. If none of the lower covers of m
is m′, then two distinct lower covers of m remain in ̂L. Their join in L is m,
and their join in ̂L is therefore ̂j, because every element strictly above the
meet-irreducible m lies above its unique upper cover ̂j. This contradicts the
join-irreducibility of ̂j in ̂L. Hence m′ lower covers m.

AUDITING TWO CLAIMED PROOFS OF FRANKL’S CONJECTURE 9

If m′ were join-reducible, two distinct lower covers of m′ would remain in
̂L and, by the same argument applied along the chain

m
′ < m < ̂j,

their join in ̂L would be ̂j, again a contradiction. Thus m′ is join-irreducible;
the least element is not meet-irreducible in a minimum counterexample [4,
Corollary 2.2], so there is no exceptional zero case. Hence m′ is doubly
irreducible and therefore lattice-tight by [4, Lemma 2.5]. But m′ ≤ m
and m′ ≤ m′, so m′ is a lattice-tight join-irreducible below both deleted
meet-irreducibles, contrary to the assumption.
Thus every join-irreducible of ̂L has a principal filter of size at least
k > |̂L|/2. This makes ̂L a smaller counterexample, contradicting the
minimality of L. □

7. The active exact-three frontier

The smallest numerically possible tight set has three members. On the
lattice side, suppose that the complete set of lattice-tight join-irreducibles is

J0 = {a, b, c}.

For each meet-irreducible m, define its tight trace

S(m) = {j ∈ J0 : j ≤ m}.

Corollary 7.1 (Exact-three incidence structure). Every meet-irreducible m
satisfies |S(m)| ≥ 2. Moreover, each of the traces

{a, b}, {a, c}, {b, c}

occurs for at least one meet-irreducible.

Proof. Theorem 6.7 implies that the traces of any two meet-irreducibles
intersect. Suppose S(m) = {a} for some meet-irreducible m. Then every
other meet-irreducible has a in its tight trace, so a lies below every meet-
irreducible of L. In a finite lattice, the meet of all meet-irreducible elements
is the least element [8, Section I.3]. This would give a ≤ 0L, a contradiction.
Thus every tight trace has size at least two.
For each a ∈ J0, some meet-irreducible does not lie above a; otherwise a
would again lie below the meet of all meet-irreducibles. A tight trace omitting
a has at least two members and is contained in J0 \ {a}, so it equals J0 \ {a}.
Repeating this for a, b, c yields all three displayed traces. □

Complementing the original union-closed family converts a union-side
tight element of frequency k into an intersection-side coordinate of frequency
k + 1 = (|L| + 1)/2. Thus Corollary 7.1 is the dual counterpart of the
deletion-witness restriction from Theorem 6.4, but it is strictly stronger than
the previously known assertion that every meet-irreducible has at least one
tight coordinate below it.

10 NELSON DANIEL SPENCE

The exact-three case is therefore reduced to a rigid triangle of tight inci-
dences: every meet-irreducible has trace in
{{a, b}, {a, c}, {b, c}, {a, b, c}
}
,

and all three two-element traces occur. The remaining task is to use the
lattice order beyond this incidence shadow. Two concrete possibilities are to
derive the 2-transversal configuration excluded for minimal counterexamples
by Hachimori and Kashiwabara [9], or to construct a larger deletion set whose
losses are absorbed by the slack of non-tight principal filters. Neither finishing
step is proved here.
 8. Conclusion

Two proposed proof mechanisms for Frankl’s conjecture fail on very small
explicit objects. The 5 × 4 matrix of Proposition 3.1 refutes the stated
implication from acceptance by A2 to a heavy column. The four-member
family of Proposition 4.1 refutes a recursive discarding-set upper bound even
though the excluded collections are pairwise disjoint.
The minimum-counterexample route remains viable. A smallest counterex-
ample must have odd size 2k + 1, and every admissible one-member deletion
exposes a tight element of frequency k outside the deleted member. On the
lattice side, every pair of meet-irreducibles has a common tight join-irreducible
below it. In the exact-three case, every meet-irreducible is therefore incident
with at least two tight coordinates, and all three two-coordinate traces oc-
cur. This reduces the remaining exact-three problem to exploiting the order
structure behind a rigid triangular incidence pattern. The conjecture itself
remains unresolved.
 References

1. Jamolidin K. Abdurakhmanov, An algorithmic proof of frankl’s union-closed sets
conjecture, HAL preprint hal-05482771, version 1, 2026, HAL: hal-05482771v1.
2. , On the existence of heavy columns in binary matrices with distinct rows, 2026,
arXiv:2601.18450.
3. Ryan Alweiss, Brice Huang, and Mark Sellke, Improved lower bound for frankl’s union-
closed sets conjecture, The Electronic Journal of Combinatorics 31 (2024), no. 3, Paper
No. P3.35.
4. Christopher Bouchard, On the lattice formulation of the union-closed sets conjecture,
2025, arXiv:2503.00277.
5. Henning Bruhn and Oliver Schaudt, The journey of the union-closed sets conjecture,
Graphs and Combinatorics 31 (2015), no. 6, 2043–2074.
6. Peter Frankl, Extremal set systems, Handbook of Combinatorics (Ronald L. Graham,
Martin Grötschel, and László Lovász, eds.), Elsevier, 1995, pp. 1293–1329.
7. Justin Gilmer, A constant lower bound for the union-closed sets conjecture, 2022,
arXiv:2211.09055.
8. George Grätzer, Lattice theory: Foundation, Birkhäuser, 2011.
9. Masahiro Hachimori and Kenji Kashiwabara, Several minimality concepts related to
frankl’s conjecture, Graphs and Combinatorics 40 (2024), 130.
10. R. M. Norton and D. G. Sarvate, A note on the union-closed sets conjecture, Journal
of the Australian Mathematical Society. Series A 55 (1993), no. 3, 411–413.

AUDITING TWO CLAIMED PROOFS OF FRANKL’S CONJECTURE 11

11. Rainer Schrader, A class of inequalities for intersection-closed set systems, 2025,
arXiv:2501.03302.
