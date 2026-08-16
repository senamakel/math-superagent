<!-- source: https://arxiv.org/pdf/1702.05947 | converted from PDF -->

arXiv:1702.05947v2  [math.CO]  4 Jun 2018
Cutting Planes for Families Implying Frankl’s
Conjecture

Jonad Pulaj ∗1,2

1Department of Computer Science, Mathematics and Physics, Faculty of Science and
Technology, The University of the West Indies, Cave Hill, St. Michael, Barbados
2Dept. of Mathematical Optimization, Zuse Institute Berlin (ZIB) Takustr. 7, 14195
Berlin, Germany
jonad.pulaj@cavehill.uwi.edu

Abstract

We ﬁnd previously unknown families of sets which ensure Frankl’s
conjecture holds for all families that contain them using an algorithmic
framework. The conjecture states that for any nonempty union-closed
(UC) family there exists an element of the ground set in at least half the
sets of the considered UC family. Poonen’s Theorem characterizes the ex-
istence of weights which determine whether a given UC family implies the
conjecture for all UC families which contain it. We design a cutting-plane
method that computes the explicit weights which imply the existence con-
ditions of Poonen’s Theorem. This method enables us to answer several
open questions regarding structural properties of UC families, including
the construction of a counterexample to a conjecture of Morris from 2006.

Keywords: Frankl’s conjecture, union-closed families, integer programming,
cutting-plane method, extremal combinatorics.

1 Introduction

Frankl’s (union-closed sets) conjecture is a celebrated unsolved problem in com-
binatorics that was recently brought to the attention of a wider audience as
a polymath project led by Timothy Gowers [12]. A nonempty ﬁnite family of
distinct ﬁnite sets F is union-closed (UC) if and only if for every A, B ∈ F
it follows that A ∪ B ∈ F. Frankl’s conjecture states that for any UC family
F ̸= {∅} there exists an element in the union of sets of F that is present in at
least half the sets of F . The problem appears to have little structure—perhaps
the very reason why a proof or disproof remains elusive.
In this paper we focus on a well-established method employed to attack the
problem referred to as local conﬁgurations in Bruhn and Schaudt [5], namely
UC families that imply the conjecture for all UC families which contain them.

∗The work for this article has been (partly) conducted within the Research Campus
MODAL funded by the German Federal Ministry of Education and Research (BMBF grant
number 05M14ZAM).
 1

In other words, these particular UC families always have an element in their sets
that is frequent enough to imply the conjecture for all UC families that contain
them. In this regard, given a UC family A, Poonen’s Theorem [17] characterizes
the necessity of the implication by the existence of weights on the elements of A
that obey certain inequalities. Following Vaughan [19], we say that a UC family
of sets A with a largest (cardinality-wise) set A is Frankl-Complete (FC), if and
only if for every UC family F ⊇ A there exists i ∈ A that is contained in at
least half the sets of F . A UC family A with a largest (cardinality-wise) set
A is Non–Frankl-Complete (Non–FC), if and only if there exists a UC family
F ⊇ A such that each i ∈ A is in less than half the sets of F . Non–FC-families
are particularly useful in characterizing minimal FC-families, i.e., FC-families
that do not contain smaller FC-families, and also other objects of interests
deﬁned in Morris [16], which help shed light into structural properties of the
conjecture. In addition, Non–FC-families yield natural candidates for possible
counterexamples.
However, on a more positive note, the pressing relevance of FC and Non–FC-
families is evident in existing literature: These objects are at the heart of ar-
guments that yield improved bounds for the problem, as seen in Poonen [17],
Gao and Yu [10], Morris [16], Marković [15], Bošnjak and Marković [3], and
ﬁnally Vučković and Živković [22] which features the current best bound of
n ≤ 12, where n is the cardinality of the largest set in a UC family. In other
words, Frankl’s conjecture holds for all UC families whose largest set has at
most twelve elements. Furthermore, FC-families are used in Bruhn et al. [4] to
prove that Frankl’s conjecture holds for subcubic bipartite graphs. Therefore
characterizing a considerable number of previously unknown FC and Non–FC-
families—the fundamental contribution of this work which consequently helps
settle several open questions of interest—is a clear step toward a better under-
standing of Frankl’s conjecture.
Characterizing exactly which UC families are FC and Non–FC is surprisingly
diﬃcult, as evinced by the relative dearth of known FC-families despite the
past twenty-ﬁve years of research on the matter. For a positive integer r an
r-set (or r-subset) is a set (or subset) of cardinality r. Previous researchers
use special structures and stronger than necessary conditions to determine a
number of FC-families. In particular, Poonen [17] proves that any UC family
which contains three 3-subsets of a 4-set satisﬁes the conjecture. Vaughan [19],
[20], [21] proves that the conjecture holds for any UC family which contains a
5-set and all of its 4-subsets, or ten of the 4-subsets of a 6-set, or three 3-subsets
of a 7-set with a common element. Furthermore, using a heuristic procedure
implemented in a computer algebra system, Vaughan identiﬁes potential weight
systems for candidate FC-families and then proves through tedious and technical
case analysis that a few more UC families are FC. Still, several FC-families
Vaughan discovers are not minimal, in the sense that they contain smaller FC-
families as shown by subsequent research or results in this paper. Morris [16]
is able to characterize new FC-families on six elements and with the help of a
computer program exactly characterizes all minimal FC-families on 5 elements.
Given a family of sets S, we say that S generates (or is a generator of) F ,
denoted by ⟨S⟩ := F , if and only if F is a UC family that contains S, and
there exists no UC family ̃F ⊂ F such that S ⊆ ̃F . A generator of a UC
family F is minimal if it does not contain a smaller generator of F . Johnson

2

and Vaughan [13] show that each UC family has a unique minimal generator.
In this paper, we are mainly interested in minimal generators of minimal FC-
families. Hence from now on, to improve readability, we simply refer to minimal
generators of FC-families. In order to facilitate the combinatorial analysis of
FC-families, Morris [16] introduces the following notion. Let F C(k, n) denote
the smallest m such that any m of the k-sets in {1, 2, . . . , n} generate an FC-
family. As proven in Gao and Yu [10], F C(k, n) is always deﬁned for suﬃciently
large n in relation to k. Consequently, Morris [16] shows that F C(3, 5) = 3,
F C(4, 5) = 5, F C(3, 6) = 4, 7 ≤ F C(4, 6) ≤ 8, F C(3, 7) ≤ 6 and F C(4, 7) ≤
18. Such characterizations further facilitate the search for better bounds (or
possible counterexamples). Finally, Marić, Živković, and Vučković [14] formalize
a combinatorial search in the interactive theorem prover Isabelle/HOL and show
that all families containing four 3-subsets of a 7-set are FC-families. Although
not explicitly mentioned in their paper, their result implies that F C(3, 7) =
4 by the lower bound on the number of 3-sets of Morris [16]. In summary,
previous research has yielded less than two dozen exact characterizations of
minimal generators of FC-families, with roughly a dozen more characterizations
of general FC-families. In light of the above, our main contributions in this paper
are the following:

• We design a general computational framework that is able to precisely
characterize FC or Non–FC-families by using exact integer programming
and other redundant veriﬁcation routines, thus providing an algorithmic
road-map for settling open questions in Morris [16] and Vaughan [20], [21].

• In particular we construct an explicit counterexample to a conjecture of
Morris [16] about the structure of generators for Non–FC-families. Fur-
thermore we answer in the negative two related questions of Vaughan [20]
and Morris [16] regarding a simpliﬁed method for proving the existence of
weights that yield FC-families.

• In the Appendix we feature over one hundred previously unknown mini-
mal nonisomorphic (under permutations of the ground set) generators of
FC-families. We ﬁnd the ﬁrst known exact characterizations of minimal
generators of FC-families on 8 ≤ n ≤ 10.

The connection between Frankl’s conjecture and mathematical programming is
well-established in Pulaj, Raymond and Theis [18], where the authors derive
the equivalence of the problem with an integer program and investigate related
conjectures. Furthermore, given an UC family A, Poonen’s Theorem yields a
constructive proof to determine if A is FC or Non–FC in the form of a fractional
polytope with a potentially exponential number of constraints. In general, this
makes it diﬃcult to explicitly state the conditions which determine whether a
given UC family is FC. To overcome this, we design a cutting-plane method
that computes the explicit weights which imply Poonen’s existence conditions.
In particular, this paves the way toward automated discovery of FC-families by
computational integer programming, especially when coupled (as we do in this
work) with an exact rational solver [7] and other veriﬁcation routines such as the
recent work of Cheung, Gleixner and Steﬀy [11]. Our current implementation
1

1Final computations are rechecked with CPLEX 12.6.3 [8], Gurobi 6.5.2 [1], and exact SCIP

3

in SCIP 3.2.1 [9] allows us to characterize any FC-family up to 10 elements
tested so far.

2 Poonen’s Theorem

In this paper we are only interested in ﬁnite families of ﬁnite sets, which we will
simply refer to as families of sets. First we will need the following deﬁnitions.
For two families of sets A and B, let A ⊎ B := {A ∪ B | A ∈ A, B ∈ B}. Let
[n] := {1, 2, . . . , n} and let P([n]) denote the power set of [n]. Let F be a family
of sets and denote by U (F ) the union of all sets in F . For i ∈ U (F ) deﬁne
Fi := {F ∈ F | i ∈ F }. Poonen’s theorem [17] is central to all approaches for
classifying FC-families. In the following to simplify notation we assume w.l.o.g.
that U (A) = [n].

Theorem 1 (Poonen 1992). Let A be a UC family such that ∅ ∈ A. The
following statements are equivalent:

1. For every UC family F ⊇ A, there exists i ∈ [n] such that |Fi| ≥ |F |/2.

2. There exist nonnegative real numbers c1, . . . , cn with ∑
i∈[n] ci = 1 such
that for every UC family B ⊆ P([n]) with B ⊎ A = B, the following in-
equality holds
 ∑

i∈[n] ci|Bi| ≥ |B|/2. (1)

It is important to note that Poonen’s Theorem still holds if ∅ ̸∈ A. In this
case the condition B⊎A = B becomes B⊎A ⊆ B. This is an equivalent condition
we ﬁnd in Vaughan [19], [20], [21]. For a ﬁxed UC family A such that ∅ ∈ A,
the second statement in Theorem 1 can be seen as a polyhedron deﬁned as the
following:

P A :=
 



y ∈ Rn
 ∑i∈[n] yi = 1;

∑i∈[n] yi|Bi| ≥ |B|/2 ∀ UC B ⊆ P([n]) : B ⊎ A = B;

yi ≥ 0 ∀i ∈ [n];
 




Furthermore since the coeﬃcients (and the right-hand side vector) are all ratio-
nal, if P A is nonempty, we can safely assume (via Fourier-Motzkin elimination)
that it contains a rational vector. This is a very well-known result (for more
details see the excellent exposition of Aigner and Ziegler [2, pp.66]) which we
formally state as follows for completeness and reference.

Proposition 1. Let P be a nonempty rational polyhedron. Then P contains a
rational vector.

[7]. For n ≥ 8, we use CPLEX 12.6.3 [8], then recheck the results with the rest of the solvers. In
addition, the branch and bound tree of exact SCIP [7] is veriﬁed with VIPR [6]. Our implemen-
tation is freely available at https://github.com/JoniPulaj/cutting-planes-UC-families

4

We can use the simplex or interior point methods to ﬁnd a feasible point
of P A, or show that one does not exist via Farkas’ Lemma. Suppose P A is
nonempty. Then we can scale any rational vector contained in P A and arrive at
an integer vector. In particular, for reasons that we outline in Section 5, we want
to choose a rational vector such that the ℓ1 norm of the resulting integer vector
is as small as possible. This explains the objective function of the following
integer program. Let I A denote the following integer program:

min ∑

i∈[n] zi

s.t. ∑

i∈[n] zi|Bi| ≥ (|B|/2) ∑

i∈[n] zi ∀B ⊆ P([n]) : B ⊎ A = B

∑

i∈[n] zi ≥ 1

zi ∈ Z≥0 ∀i ∈ [n]

A feasible solution of I A is a vector ¯z ∈ Z
n
≥0 such that ¯z satisﬁes all the given
inequalities of I A.

Proposition 2. Let A be a UC family such that ∅ ∈ A. Then P A is nonempty
if and only if there exists a feasible solution of I A.

Proof. Suppose P A is nonempty and let ¯y ∈ P A. From Proposition 1 we can
safely assume that ¯y ∈ Qn
≥0, i.e., ¯y = (¯y1 = a1
b1 , ¯y2 = a2
b2 , . . . , ¯yn = an
bn ) such that
bi ≥ 1 for all i ∈ [n]. Let g ∈ Z≥0 such that g = lcm(b1, b2, . . . , bn), and let
¯zi ∈ Z≥0 such that ¯zi = g ¯yi for all i ∈ [n]. Deﬁne ¯z := (¯z1, ¯z2, . . . , ¯zn). It follows
that ¯z ∈ Z
n
≥0 is a feasible solution of I A.
For the other direction, suppose the vector ¯z ∈ Z
n
≥0 is a feasible solution of
I A. Let ¯z = (¯z1, ¯z2, . . . , ¯zn). Deﬁne ¯yi := ¯zi/(
∑
i∈[n] ¯zi) for all i ∈ [n] and
¯y := (¯y1, ¯y2, . . . , ¯yn). It follows that ¯y ∈ P A.

We need the following corollary of Poonen’s Theorem, a version of which is
already noted in Morris [16]. We formalize it again here for clarity and reference.

Corollary 1. Let A be a UC family such that ∅ ∈ A. The following statements
are equivalent:

1. For every UC family F ⊇ A, there exists i ∈ [n] such that |Fi| ≥ |F |/2.

2. There exist ci ∈ Q≥0 for all i ∈ [n] with ∑i∈[n] ci = 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑S∈B (∑i∈S ci − ∑
i /∈S ci) ≥ 0
holds.
 5

Proof. Fix a UC family B ⊆ P([n]) with B ⊎ A = B. Then the following holds,

∑

S∈B
 (∑

i∈S ci − ∑

i /∈S ci
)
 = 2 ∑

S∈B
 ∑

i∈S ci − ∑

S∈B
 (∑

i /∈S ci + ∑

i∈S ci
)

= 2 ∑

S∈B
 ∑

i∈S ci − ∑

S∈B
 ∑

i∈[n] ci

= 2 ∑

i∈[n] ci|Bi| − |B| ∑

i∈[n] ci ≥ 0

⇐⇒ ∑

i∈[n] ci|Bi| ≥ |B|/2.

Since the above holds for every UC family B ⊆ P([n]) with B ⊎ A = B, the
desired result follows from Poonen’s Theorem.

Proposition 2 shows that if P A is nonempty we can simply scale a rational
vector contained in it and arrive at an integer vector. Then the proof of the
previous corollary implies the following.

Corollary 2. Let A be a UC family such that ∅ ∈ A. The following statements
are equivalent:

1. For every UC family F ⊇ A, there exists i ∈ [n] such that |Fi| ≥ |F |/2.

2. There exist ci ∈ Z≥0 for all i ∈ [n] with ∑
i∈[n] ci ≥ 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑S∈B (∑i∈S ci − ∑
i /∈S ci) ≥ 0
holds.

Proof. It is suﬃcient to follow the proof of Corollary 1 with ci ∈ Z≥0 for all
i ∈ [n] such that ∑i∈[n] ci ≥ 1. Then we arrive at the following

2 ∑

i∈[n] ci|Bi| − |B| ∑

i∈[n] ci ≥ 0.

The desired result is implied from Proposition 2 and Poonen’s Theorem.

From now on, we can base relevant arguments (when convenient) on real,
rational or integer vectors.

Corollary 3. Let A be a UC family such that ∅ ∈ A. The following statements
are equivalent:

1. A is an FC-family.

2. There exist ci ∈ R≥0 for all i ∈ [n] with ∑
i∈[n] ci = 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑

i∈[n] ci|Bi| ≥ |B|/2 holds.

3. There exist ci ∈ Q≥0 for all i ∈ [n] with ∑i∈[n] ci = 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑S∈B (∑i∈S ci − ∑
i /∈S ci) ≥ 0
holds.
 6

4. There exist ci ∈ Z≥0 for all i ∈ [n] with ∑i∈[n] ci ≥ 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑
S∈B (∑
i∈S ci − ∑

i /∈S ci) ≥ 0
holds.

5. There exist ci ∈ Z≥0 for all i ∈ [n] with ∑i∈[n] ci ≥ 1, such that for every
UC family B ⊆ P([n]) with B ⊎ A = B, ∑i∈[n] ci|Bi| ≥ (|B|/2) ∑i∈[n] ci
holds.

Proof. (1) ⇐⇒ (2) from Poonen’s Theorem. (1) ⇐⇒ (3) from Corollary 1.
(1) ⇐⇒ (4) from Corollary 2. (2) ⇐⇒ (5) from Proposition 2.

In the next proposition, we show that for FC or Non–FC-families we can
always assume (when convenient) that the empty set is present.

Proposition 3. Let A be a UC family such that ∅ ∈ A. Then A is an FC-family
if and only if A \ {∅} is an FC-family.

Proof. Let A be a UC family such that ∅ ∈ A. Deﬁne ̃A := A \ {∅}.
Suppose A is an FC-family. Then for each UC family F ⊇ A there exists
i ∈ U (A) such that |Fi| ≥ |F |/2. Hence F \{∅} also satisﬁes Frankl’s conjecture.
It follows that ̃A is an FC-family.
For the other direction, suppose ̃A is an FC-family and let F be a UC family
such that F ⊇ A. Then F ⊇ ̃A. Therefore there exists i ∈ U ( ̃A) such that
|Fi| ≥ |F |/2. Since U ( ̃A) = U (A), it follows that A is an FC-family.

2.1 A Cutting-Plane Method for Poonen’s Theorem

As mentioned in the introduction, the main obstacle in using Poonen’s Theorem
to characterize FC-families is the potentially exponential number of constraints
in P A or (equivalently) I A. Therefore, our main goal in the rest of this section
is to precisely deﬁne a method for starting with a small subset of the constraints
that deﬁne P A or I A and then generate more constraints as needed. First we
deﬁne a set of integer vectors contained in a polyhedron that determines, when
the set is empty, that a given rational vector satisﬁes the second condition of
Poonen’s Theorem (this is Proposition 4). Then we show that the set above
is nonempty if and only if a given rational vector does not satisfy the second
condition of Poonen’s Theorem (this is Theorem 2). Finally, this gives rise to
an algorithm that determines whether a given A is FC or Non–FC.
Corollary 3 combined with the integer programming approach to UC families
in in Pulaj, Raymond and Theis [18], provides the background of our method.
Fix a UC family A such that ∅ ∈ A. As previously, we may assume U (A) = [n].
Let c ∈ Z
n
≥0 such that ∑
i∈[n] ci ≥ 1. With every set S ∈ P([n]), we associate a
variable xS, i.e, a component of a vector x ∈ R2
n indexed by S. Given a family
of sets F ⊆ P([n]), let X F ∈ R2
n denote the incidence vector of F deﬁned
(component-wise) as
 X F
S := { 1 if S ∈ F,
0 if S ̸∈ F.

Hence every family of sets F ⊆ P([n]) corresponds to a unique zero-one vector
in R2
n and vice versa. Let X(A, c) denote the set of integer vectors contained

7

in the polyhedron deﬁned by the following inequalities:

xS + xT ≤ 1 + xS∪T ∀S ∈ P([n]), ∀T ∈ P([n]) (2)

∑

S∈P([n])
 (∑

i∈S ci − ∑

i /∈S ci
)
 xS + 1 ≤ 0 (3)

xS ≤ xA∪S ∀S ∈ P([n]), ∀A ∈ A (4)
0 ≤ xS ≤ 1 ∀S ∈ P([n]) (5)

Suppose X(A, c) is nonempty and let ¯x ∈ X(A, c). Then ¯x = X B for some
family of sets B such that B ⊆ P([n]). Inequalities (2) ensure that the chosen
family B is UC, and we denote them as UC inequalities. Inequalities (4) ensure
that B ⊎ A = B, and we denote them as Fixed-Set (FS) inequalities. We denote
Inequality (3) as the Weight Vector (WV) inequality and we explain it in the
next proposition.

Proposition 4. Let A be a UC family such that ∅ ∈ A, and let c ∈ Z
n
≥0 such
that ∑
i∈[n] ci ≥ 1. If X(A, c) = ∅, then A is an FC-family.

Proof. Suppose that X(A, c) = ∅. Let Y (A, c) be deﬁned as the set of integer
vectors contained in the polyhedron deﬁned by Inequalities (2), (4) and (5).
For any UC family B ⊆ P([n]) such that B ⊎ A = B, we arrive at X B ∈ Y (A, c).
Therefore if X(A, c) = ∅ this implies there exists no UC family B ⊆ P([n]) with
B ⊎ A = B such that:
 ∑

S∈B
 (∑

i∈S ci − ∑

i /∈S ci
)
 ≤ −1.

Since ci ∈ Z≥0 for all i ∈ [n], this implies that for each UC family B ⊆ P([n])
with B ⊎ A = B, the following inequality holds:

∑

S∈B
 (
∑

i∈S ci − ∑

i /∈S ci
)
 ≥ 0.

Corollary 3 implies that each UC family F such that F ⊇ A, satisﬁes Frankl’s
conjecture.

A natural candidate for checking whether X(A, c) is empty (or not), for
some A and c, is a standard branch and bound algorithm. Hence we deﬁne an
appropriate integer program related to X(A, c) and solve it in a general purpose
integer programming solver as speciﬁed in the introduction. However in order
to prove that a “candidate" UC family is an FC-family, we need a vector c which
yields an empty X(A, c), if such a vector exists. Thus we turn our attention to
the relation between X(A, c) and P A, for a given A and c. First we need the
following basic deﬁnition.

Deﬁnition 1. A valid inequality πT x ≥ π0 for a set X ⊆ Rn is violated by a
vector ¯x ∈ Rn if and only if πT ¯x < π0.

Given c ∈ Z
n
≥0 such that ∑i∈[n] ci ≥ 1, we deﬁne ¯y as c normalized by its
ℓ1 norm. Thus ¯y = c/ ∑
i∈[n] ci. By deﬁnition we arrive at ¯y ∈ Qn
≥0 such that
∑i∈[n] ¯yi = 1.
 8

Theorem 2. Let A be a UC family such that ∅ ∈ A and let c ∈ Z
n
≥0 such
that ∑
i∈[n] ci ≥ 1. Then X(A, c) is nonempty if and only if there exists a valid
inequality of P A that is violated by ¯y.

Proof. Suppose X(A, c) is nonempty. Hence there exists ¯x ∈ X(A, c) such that
¯x = X B for some B ⊆ P([n]). B is a UC family since the corresponding UC
inequalities are satisﬁed. Furthermore, for each B ∈ B and for each A ∈ A, it
follows that A ∪ B ∈ B since all the corresponding FS inequalities are satisﬁed.
Hence we see that B ⊎ A = B. Therefore B yields the coeﬃcients (and the
right-hand side scalar) of the following valid inequality for P A,
∑

i∈[n] yi|Bi| ≥ |B|/2.

Since X B ∈ X(A, c) implies the WV inequality is satisﬁed, we arrive at the
following, ∑

S∈B
 (∑

i∈S ci − ∑

i /∈S ci
)
 ≤ −1.

Combining the above with the proof of Corollary 2 we arrive at the following
inequality, 2 ∑

i∈[n] ci|Bi| − |B| ∑

i∈[n] ci ≤ −1.

Adding |B| ∑
i∈[n] ci to both sides of the above and dividing by 2 ∑
i∈[n] ci, we
arrive at ∑

i∈[n]
 ci∑i∈[n] ci |Bi| ≤ −1
2 ∑
i∈[n] ci + |B|
2

and because −1
2 ∑
i∈[n] ci < 0, and ci∑

i∈[n] ci = ¯yi for each i ∈ [n], it follows that

∑

i∈[n] ¯yi|Bi| < |B|/2.

For the other direction, suppose X(A, c) = ∅. Following the proof of Propo-
sition 4 we see that for each B ⊆ P([n]) such that B ⊎ A = B, the following
inequality holds: ∑

S∈B
 (
∑

i∈S ci − ∑

i /∈S ci
)
 ≥ 0.

Hence, Corollary 3 implies that ¯y ∈ P A.

We determined that a nonempty X(A, c) implies a violated inequality for
P A. However for a given A and c, there may be many such violated inequalities.
This leads to the notion of a maximally violated inequality, which we deﬁne
below. This notion is based on the intuition that a maximally violated inequality
is “farthest" away from P A, and hence adding it to a subset of the constraints
of P A should get us “closest" to P A.
2

2Indeed, from a computational perspective, for all the tested UC families in this paper,
using this notion for the objective function of IP (A, c) leads to the fewest number of iterations
of Algorithm 1, where we use IP (A, c) instead of X(A, c).

9

Deﬁnition 2. Let A, B ⊆ P([n]), be UC families such B ⊎ A = B and ∅ ∈ A. A
valid inequality ∑i∈[n] yi|Bi| ≥ |B|/2 for P A is maximally violated by a vector
¯y ∈ Qn
≥0 such that ∑i∈[n] ¯yi = 1 if and only if for each violated valid inequality
∑i∈[n] yi|Di| ≥ |D|/2 such that D ⊆ P([n]) is a UC family and D ⊎ A = D, the
following inequalities (|B|/2 − ∑i∈[n] ¯yi|Bi|) ≥ (|D|/2 − ∑i∈[n] ¯yi|Di|) > 0 hold.

Let A be a UC family such that ∅ ∈ A. Furthermore, let c ∈ Z
n
≥0 such that∑i∈[n] ci ≥ 1. Denote by IP (A, c) the following integer program:

max ∑

i∈[n] ci
 

 ∑

S∈P([n]) xS − 2 ∑

S∈P([n]):i∈S xS




s.t. x ∈ X(A, c)

An integer vector ¯x ∈ R2
n is a feasible solution of IP (A, c) if and only if ¯x = X B

for some UC family B ⊆ P([n]) such that B ⊎ A = B and X B satisﬁes the WV
inequality. IP (A, c) is infeasible if and only if there exists no feasible solution
of IP (A, c). X B is an optimal solution of IP (A, c) if and only if X B is a feasible
solution of IP (A, c), and for any other feasible solution X D of IP (A, c), we
arrive at ∑

S∈B
 ∑

i∈[n] ci − 2 ∑

S∈B
 ∑

i∈S ci ≥ ∑

S∈D
 ∑

i∈[n] ci − 2 ∑

S∈D
 ∑

i∈S ci.

Theorem 3. Let A be a UC family such that ∅ ∈ A, and let c ∈ Z
n
≥0 such that
∑i∈[n] ci ≥ 1. Suppose X B is an optimal solution of IP (A, c). Then the valid
inequality ∑
i∈[n] yi|Bi| ≥ |B|/2 for P A is maximally violated by ¯y.

Proof. Suppose X B is an optimal solution of IP (A, c). Then the following
inequality holds: ∑

S∈B
 (∑

i∈S ci − ∑

i /∈S ci
)
 ≤ −1.

Following the proof of Corollary 2 we arrive the following:
∑

S∈B
 ∑

i∈[n] ci − 2 ∑

S∈B
 ∑

i∈S ci ≥ 1.

Suppose X D is a feasible solution of IP (A, c). Then the following holds:
∑

S∈B
 ∑

i∈[n] ci − 2 ∑

S∈B
 ∑

i∈S ci ≥ ∑

S∈D
 ∑

i∈[n] ci − 2 ∑

S∈D
 ∑

i∈S ci ≥ 1.

Rewriting the inequalities above as in the proof of Corollary 2 combined with
the proof of Theorem 2 we arrive at

|B|
2 − ∑

i∈[n]
 ci∑
i∈[n] ci |Bi| ≥ |D|
2 − ∑

i∈[n]
 ci∑i∈[n] ci |Di| ≥ 1
2 ∑
i∈[n] ci .

Finally, this implies that the following holds:

(|B|/2 − ∑

i∈[n] ¯yi|Bi|) ≥ (|D|/2 − ∑

i∈[n] ¯yi|Di|) > 0.

10

Given a UC family A, the following algorithm ﬁnds a rational vector that
satisﬁes the second condition of Poonen’s Theorem, or an infeasible subset of the
constraints that deﬁne P A. The former proves that A is FC, whereas the latter
proves that A is Non–FC. Using Proposition 2 with appropriate adjustments in
the algorithm below we may search for an infeasible subset of the constraints
that deﬁne I A instead of P A. Furthermore, we may use IP (A, c) instead of
X(A, c). For a given vector ¯y ∈ Qn
≥0 such that ¯y = ( a1
b1 , a2
b2 , . . . , an
bn ), we safely
assume that bi ≥ 1 for all i ∈ [n].

Algorithm 1: Cutting planes for FC-families
Input : A UC family A such that U (A) = [n] and ∅ ∈ A
Output: A is an FC-family, or A is a Non–FC-family

1 H ← (∑i∈[n] yi = 1, yi ≥ 0 ∀i ∈ [n]
)

2 while ∃ ¯y ∈ H such that ¯y = ( a1
b1 , a2
b2 , . . . , an
bn ) ∈ Qn
≥0 do

3 g ← lcm(b1, b2, . . . , bn)

4 c ← g ¯y

5 if ∃ X B ∈ X(A, c) then

6 H ← H ∩ (∑
i∈[n] yi|Bi| ≥ |B|/2)

7 else

8 return A is an FC-family

9 return A is a Non–FC-family

Theorem 4. Let A be a UC family such that U (A) = [n] and ∅ ∈ A. Then
Algorithm 1 correctly determines if A is an FC-family or Non–FC-family.

Proof. It is clear Algorithm 1 ﬁnitely terminates. Furthermore, if H is nonempty,
then by Proposition 1 it contains a rational vector. Let A be a UC family such
that U (A) = [n] and ∅ ∈ A. Suppose A is an FC-family. By the deﬁnition of
an FC-family and by Poonen’s Theorem there exist ci ≥ 0 for all i ∈ [n], such
that ∑i∈[n] ci = 1, which satisfy all Inequalities (1). Therefore P A is nonempty
and consequently H is nonempty. This implies that at some iteration of Algo-
rithm 1, by Theorem 2 we arrive at ¯y ∈ P A, otherwise Algorithm 1 determines
an infeasible system of constraints that deﬁnes H and we arrive at a contra-
diction. Suppose A is a Non–FC-family. By the deﬁnition of a Non–FC-family
and Poonen’s Theorem, this implies there exist no ci ≥ 0 for all i ∈ [n] with∑i∈[n] ci = 1 that satisfy all Inequalities (1). By Theorem 2 during all the
iterations of Algorithm 1 we have that ¯y ̸∈ P A, otherwise we arrive at a con-
tradiction. Therefore Algorithm 1 terminates when it determines a system of
constraints that deﬁne H such that H = ∅, which implies that P A = ∅.

Algorithm 1 becomes our main tool for determining whether certain UC
families are FC or Non–FC. This in turn allows us to answer other questions
of interest. In the next section we narrow our focus on valid inequalities for
IP (A, c). Our interest in these is mainly practical, since solving IP (A, c) in a
general purpose integer programming solver is how we determine if X(A, c) is
empty or not.
 11

3 Valid Inequalities for X(A, c)

From the perspective of computational integer programming, valid inequalities
may be considered eﬀective if—among other things—they lead to a smaller
branch and bound tree. For all the results that we feature in this paper, adding
a subset of the following inequalities to the root node of a given instance of
IP (A, c) signiﬁcantly reduces the size of the resulting branch and bound tree.
This is particularly important in the implementation of Algorithm 1 which fea-
tures IP (A, c). Since the algorithm may iterate many times, speeding up the
solution process of IP (A, c) becomes crucial. Once Algorithm 1 determines
whether a given A is an FC or Non–FC-family, separate rounds of veriﬁcations
take place in a number of diﬀerent solvers as mentioned in the introduction. If
the given family A is FC, then automated veriﬁcations are carried out in an
exact rational solver [7] and VIPR [6] which do not make use of the following
inequalities, thus allowing for, if necessary, a straightforward check of the input
ﬁles.
3

In the next deﬁnition, we may assume that U (S) = U (F ) = U (A) = [n], for
some positive integer n.

Deﬁnition 3. A family of sets S generates F with a UC family A, denoted by
⟨S⟩A := F , if and only if F is a UC family that contains S such that F ⊎A = F ,
and there exists no UC family ̃F ⊂ F such that ̃F contains S and ̃F ⊎ A = ̃F .

As in the previous Section, for all UC families A that are “candidate" FC-
families in the following propositions and deﬁnition, we assume that U (A) = [n],
for some integer n ≥ 1.

Proposition 5 (FC inequalities). Let A be a UC family such that ∅ ∈ A, and
let c ∈ Z
n
≥0 such that ∑
i∈[n] ci ≥ 1. Let S ∈ A, and let U, T ∈ P([n]) such that
S ∪ U = F and S ∪ T = F . Then the following

xT + xU − xT ∪U − xF ≤ 0,

is valid for X(A, c).

Proof. Suppose there exists an integer vector in X(A, c) which yields a UC
family F such that the following inequality holds (for some S ∈ A and U, T ∈
P([n]) as above) xT + xU − xT ∪U − xF ≥ 1.

This implies that the number of variables which equal one with positive coeﬃ-
cients is greater than the number of variables with negative coeﬃcients which
equal one. But if either xT or xU are one then xF is one (if both are one then
xT ∪U is one) and we arrive at a contradiction.

In the following deﬁnition the role of a considered UC family A is taken into
account in the listed conditions. In the ﬁrst condition the role of A is implicit

3This is important because it means that the interested reader does not need to rely on the
implementation of Algorithm 1, and in particular the generation of FC-chain inequalities, in
order to computationally reproduce the results featured in this paper. To check that a given A
is FC, a reader simply needs the correct weight vector and a solver of choice. For a Non–FC-
family, the reader needs the UC families which yield the infeasible system of inequalities and
the Farkas duals.
 12

in the existence of a FS inequality, whereas in the second condition the role of
A is implicit in generating the desired family, as discussed at the beginning of
this section.

Deﬁnition 4 (FC-chain). Let A be a UC family such that ∅ ∈ A, and let
c ∈ Z
n
≥0 such that ∑
i∈[n] ci ≥ 1. Let S, S′ ⊂ P([n]), S ∩ S′ = ∅. Given
Bi ∈ S, Bj ∈ S′, we say Bi, Bj form an FC-chain which we denote by Bi −→ Bj,
if and only if there exist tuples (Bi, Bk), (Bk, Bl), (Bl, Bm), . . . , (Bp, Bj), where
{Bk, Bl, . . . , Bp} ⊂ P([n]), such that for any tuple (Bq, Br) in the FC-chain, at
least one of the following conditions holds:

1. There exists A ∈ A such that A ∪ Bq = Br, and therefore xBq ≤ xBr is a
valid FS inequality for X(A, c).

2. There exists S ∈ ⟨S⟩A such that xBq +xS ≤ 1+xBr is a valid UC inequality
for X(A, c).

The following proposition follows directly from the deﬁnition above.

Proposition 6 (FC-chain inequalities). Let A be a UC family such that ∅ ∈ A,
and let c ∈ Z
n
≥0 such that ∑i∈[n] ci ≥ 1. Let S, S′ ⊂ P([n]), S ∩ S′ = ∅.
For any T ⊆ S deﬁne U(T ) := {S′ ∈ S′ | ∃ S ∈ T : S −→ S′}. Suppose that
|T | ≤ |U(T )| for all T ⊆ S. Then the inequality
∑

S∈S xS − ∑

S∈S ′ xS ≤ 0,

is valid for X(A, c).

Proof. Suppose there exists an integer vector in X(A, c) which yields a UC
family F such that the following inequality holds (for some S, S′ ⊂ P([n]), as
above) ∑

S∈S∩F xS − ∑

S∈S ′∩F xS ≥ 1.

It is clear that S ∩ F ̸= ∅, otherwise we arrive at a contradiction. Therefore
the inequality implies that the number of variables xS which equal one, for all
S ∈ S ∩ F is greater than the number of variables xS which equal one, for all
S ∈ S′ ∩ F. Let T ⊆ S ∩ F, and for all S ∈ T , let xS = 1. |T | ≤ |U(T )|
holds by hypothesis. Furthermore by the deﬁnition of an FC-chain for each
T , S′ ⊂ P([n]) such that T ∩ S′ = ∅, for all S′ ∈ U(T ) we conclude that
xS′ = 1. Thus we arrive at a contradiction.

Observe that FC-chain inequalities generalize FC-inequalities. We will use
them in the appendix to explicitly exhibit the branch and bound tree of the
counterexample in the next section. In particular, this implies that our coun-
terexample requires no trust from the reader, in the sense that its veriﬁcation
can be separated from the complex optimization process that produced it.

4 Generators for Non–FC-families

In this section we exhibit a counterexample to a conjecture of Morris [16] about
generators for Non-FC-families.
 13

Deﬁnition 5 (regular). Let S be a family of sets such that U (S) = [n]. Suppose
S is a minimal generator for a UC family F , such that F is a Non–FC-family.
Then S is regular if and only if for any A ∈ S, A ̸= ∅, and any i ∈ [n], the UC
family ⟨(S \ {A}) ∪ {A ∪ {i}}⟩ is Non–FC.

Conjecture 1 (Morris 2006). Let S be a family of sets such that U (S) = [n],
for n ≥ 3. Suppose S is a minimal generator for a UC family F , such that F
is a Non–FC-family. Then S is regular.

Morris [16] checked the conjecture for all known families at the time, and
therefore considered it plausible. In some sense, Conjecture 1 perfectly illus-
trates our general lack of knowledge about UC families since—as a number of
other related questions—it has eluded an answer for a relatively long time. The
obstacle—in this case and others to follow—is the lack of a method for ex-
actly characterizing FC-families, a gap in knowledge which we correct with our
framework.

4.1 A Counterexample for Structures in Non–FC-families

Our counterexample on six elements is minimal, in the sense that Morris [16]
completely characterizes FC-families on 5 elements.
Let S := {∅, {4, 5, 6} , {1, 3, 4} , {1, 2, 5, 6} , {1, 2, 3, 4}} ⊂ P([6]). Furthermore,
let T := {{1, 2, 4, 5, 6} , {1, 3, 4, 5, 6} , {1, 2, 3, 4, 5, 6}} ⊂ P([6]). Hence it follows
that ⟨S⟩ = S ∪ T . It is straightforward to check that S is a minimal generator
for S ∪ T . We will show that ⟨S⟩ is a Non–FC-family. There is a stronger
connection between the structure of inequalities featured in the proof below
and questions of Vaughan [20] and Morris [16] we answer later in this work.
In Section 5 we explicitly describe the structure of UC families from which the
inequalities below are derived in relation to the questions of interest.

Proposition 7. ⟨S⟩ is a Non–FC-family.

Proof. Algorithm 1 determines an infeasible system of constraints which yields
the result. We display an irreducible infeasible subset of the given system. We
identify columns with zero one entries for each S ∈ P([6]). The six matrices
featured below represent UC families. The top row keeps track of the number of
sets in each family. In addition to rechecking with an exact rational solver [7] and
other solvers, we check that each matrix is UC via simple external subroutines
and ﬁnally by hand. Furthermore, let F ⊂ P([6]) be a family represented by one
of the matrices below. By inspection we see that F ⊎ ⟨S⟩ = F . In each matrix,
we color columns which correspond to sets in S, T , red and blue, respectively.
Each matrix yields an Inequality (1) from Poonen’s Theorem (multiplied by
two) featured below it. The following system of constraints is infeasible in
nonnegative yi for all 1 ≤ i ≤ 6. For each row we display the Farkas dual values
in square brackets. This yields a certiﬁcate of infeasibility via a straightforward
application of Farkas’ Lemma. For convenience we state the lemma in the
appendix.
[−7190] : y1 + y2 + y3 + y4 + y5 + y6 = 1.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1
c3 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1
c4 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1
c5 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 1 1 0 0 1 1
c6 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 1
14

[30] : 22y1 + 46y2 + 50y3 + 50y4 + 46y5 + 46y6 ≥ 43.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
c3 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1
c4 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 1 0 1 1 1 1
c5 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 1 1 0 0 1 1
c6 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 1

[9] : 46y1 + 14y2 + 42y3 + 42y4 + 42y5 + 42y6 ≥ 39.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1
c3 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1
c4 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 1
c5 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 0 0 1 1
c6 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1

[44] : 52y1 + 46y2 + 52y3 + 28y4 + 52y5 + 52y6 ≥ 46.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
c3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1
c4 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 1
c5 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1
c6 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1

[21] : 48y1 + 40y2 + 16y3 + 48y4 + 40y5 + 40y6 ≥ 40.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
c3 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1
c4 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1
c5 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1
c6 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1

[32] : 44y1 + 44y2 + 42y3 + 48y4 + 20y5 + 52y6 ≥ 42.

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42
c1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
c2 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
c3 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1
c4 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1
c5 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1
c6 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1

[32] : 44y1 + 44y2 + 42y3 + 48y4 + 52y5 + 20y6 ≥ 42.

15

We are now ready to show that S is not regular, and thus give a counterex-
ample to Conjecture 1.

Proposition 8. Let S′ := {∅, {4, 5, 6} , {1, 3, 4} , {1, 2, 5, 6} , {1, 2, 3, 4, 5}}.
Then ⟨S′⟩ is an FC-family.

Proof. Let c ∈ Z
6
≥0 such that c = (16, 8, 12, 20, 17, 15). Then IP (⟨S′⟩, c) is
infeasible 4.

Corollary 4. S is a counterexample to Conjecture 1.

Proof. We show that S is not regular. We observe that U (S) = [6] and S is a
minimal generator for ⟨S⟩. Furthermore from Proposition 7 it follows that ⟨S⟩
is a Non–FC-family. However S′ = (S \ {1, 2, 3, 4}) ∪ {{1, 2, 3, 4} ∪ {5}} and
Proposition 8 implies that ⟨S′⟩ is an FC-family.

5 Relaxation Questions

In this section, we brieﬂy address the practical behavior of Algorithm 1, as it
sheds light on open questions of interests in Vaughan [20] and Morris [16]. As
a result, we exhibit a counterexample to the questions of Morris and Vaughan.
Our current implementation features I A and IP (A, c) in order to avoid pos-
sible numerical trouble by minimizing the sum of the zi, in addition to select-
ing the “sharpest cut" whenever we solve IP (A, c). Yet, without witnessing
ﬁrst-hand computations for ﬁxed UC families A such that U (A) = [n] and
6 ≤ n ≤ 10, Algorithm 1 may appear fraught with theoretical dangers.
5 How-
ever, in practice our method is well-behaved in the described range, and is
consequently the currently best available technique for the exact determination
of FC-families.
Furthermore, our implementation mostly conﬁrms the heuristic intuition of
Vaughan and Morris as will be made explicit in the next paragraphs. Thus in
the tested range, Algorithm 1 mostly iterates n times. However, in some cases
it iterates more than n (but less than 2n) times6. Among the latter we ﬁnd
counterexamples to open questions of interest which we feature below.
As mentioned in the introduction, Vaughan [20] implements a heuristic that
guides the search for a potential weight system. Given a UC family A, ∅ ∈ A,
the heuristic focuses only on UC families B with B ⊎ A = B, where B =
P([n] \ {j}) ⊎ A for all j ∈ [n]. If there exists a solution to the system of linear
equations ∑
i∈[n] yi|Bi| = |B|/2 in nonnegative yi, with ∑i∈[n] yi ≤ 1, then
the considered UC family A becomes a candidate FC-family. All of Vaughan’s
candidate FC-families in [20] are identiﬁed as above, followed by tedious case
analysis that spans several pages for the proof that the given family is FC. We
precisely state Vaughan’s question as follows:

4In the appendix we explicitly show the infeasibility of IP (⟨S ′⟩, c) by making use of FC-
chain inequalities and displaying irreducible infeasible subsets of constraints for the two leaf
nodes of the resulting branch and bound tree.
5 IP (A, c) is a binary program with an exponential number of variables and constraints in
n. Furthermore the number of iterations of Algorithm 1 could be exponential in n.
6The runtimes vary roughly from a few seconds for 6 ≤ n ≤ 7 and a few minutes for
8 ≤ n ≤ 9, to a few hours for n = 10. Furthermore veriﬁcation with exact SCIP [7] takes
longer, as does testing a non-minimal FC-family. Computations were carried out on machines
with 2.40 GHz quad-core processors and 16 GB of RAM.

16

Question 1 (Vaughan 2003). Let A be a UC family such that U (A) = [n] and
∅ ∈ A. Consider UC families B ⊆ P([n]) such that B = P([n] \ {j}) ⊎ A for
all j ∈ [n]. Suppose the linear system of equations ∑

i∈[n] yi|Bi| = |B|/2 for
all B as above has a solution in nonnegative reals yi for all i ∈ [n], such that∑i∈[n] yi ≤ 1. Does this imply that P A is nonempty?

Given a UC family A, ∅ ∈ A, Morris [16] also focuses on B as above, searching
instead for integer vectors contained in the polyhedron deﬁned by the inequal-
ities derived from the n given B and zi ≥ 0 for all i ∈ [n] with ∑i∈[n] zi ≥ 1.
The idea is that the n given inequalities could capture information of interest
without needing the rest of the possible inequalities. Morris shows that this
holds in a number of cases, but is it true in general? More precisely, we state it
as the following question:

Question 2 (Morris 2006). Let A be a UC family such that U (A) = [n] and
∅ ∈ A. Consider UC families B ⊆ P([n]) such that B = P([n] \ {j}) ⊎ A for all
j ∈ [n]. Denote by Z(A) the set of integer vectors contained in the polyhedron
deﬁned by ∑i∈[n] zi ≥ 1, ∑
S∈B (∑i∈S zi − ∑
i /∈S zi) ≥ 0 for all B as above,
and 0 ≤ zi for all i ∈ [n]. Suppose Z(A) is nonempty. Does this imply that
there exists a feasible solution of I A?

Given a set A that yields a positive answer to Question 1, we can scale the
resulting vector y and (after arbitrarily increasing some entries if necessary)
arrive, following the proof of Corollary 2, at a vector z that gives a positive
answer to Question 2.

Observation 1. A positive answer to Question 1 for a given A implies a pos-
itive answer to Question 2 for the same A.

Thus, considering the above, we can explicitly describe the structure associ-
ated with the Non–FC-family that leads to the counterexample in Corollary 4.
As above, it suﬃces to consider B ⊆ P([n]) such that B = P([n] \ {j}) ⊎ A
for all j ∈ [n], where A is our given UC family. This greatly simpliﬁes the
tedious task of checking that the algorithm’s output is correct. Once the family
is constructed according the given B, it becomes straightforward to check that
the necessary conditions for correctness are met.
Given that the empty set does not make a diﬀerence in determining whether
a UC family A is FC or Non–FC, as we saw in Proposition 3, we may think
the condition ∅ ∈ A in the questions of Vaughan and Morris can be relaxed.
If this were the case, the structure of the considered B with ∅ ̸∈ A is again
simpliﬁed, since the cardinality of the new family is at most the cardinality
of the original one. Unfortunately, as we shall see, this is not the case. Still,
in the next proposition, we show that a nonempty Z(A) implies that a set of
integer vectors contained in a polyhedron arising from “smaller" structures is
also nonempty.

Proposition 9. Let A be a UC family such that U (A) = [n] and ∅ ∈ A.
Suppose Z(A) is nonempty. Consider G ⊆ P([n]) such that G = (P([n] \ {j}) ⊎
A) \ P([n] \ {j}) for all j ∈ [n]. Then the set of integer vectors contained in the
polyhedron deﬁned by ∑
i∈[n] zi ≥ 1, ∑S∈G (∑
i∈S zi − ∑i /∈S zi) ≥ 0 for all G
as above, and 0 ≤ zi for all i ∈ [n], is nonempty.

17

Proof. Let A be a UC family such that U (A) = [n] and ∅ ∈ A. Furthermore,
let B ⊆ P([n]) such that B = P([n] \ {1}) ⊎ A. Since ∅ ∈ A, it follows that
P([n] \ {1}) ⊂ B. Deﬁne D := P([n] \ {1}), G := B \ D. Suppose that Z(A)
is nonempty and z ∈ Z(A). Deﬁne ¯z as z normalized by its ℓ1 norm. Thus
we arrive at ¯zi ∈ Q≥0 for all i ∈ [n] and ∑
i∈[n] ¯zi = 1. Following the proof of
Corollary 1 we arrive at
∑

i∈[n] 2¯zi|Bi| ≥ |B| ⇐⇒ ∑

i∈[n] 2¯zi|Gi| + ∑

i∈[n]\{1} 2¯zi|Di| ≥ |G| + |D|

=⇒ ∑

i∈[n] 2¯zi|Gi| ≥ |G|.

In the last implication we use ∑
i∈[n]\{1} ¯zi ≤ 1, with ¯zi ≥ 0 for all i ∈ [n] \ {1}.
Furthermore, D = P([n] \ {1}) implies that |Di| = 2n−2 for all i ∈ [n] \ {1} and
therefore ∑

i∈[n]\{1} 2¯zi|Di| = |D| ∑

i∈[n]\{1} ¯zi ≤ |D|.

Since the same argument applies to B = P([n] \ {j}) ⊎ A for all j ∈ [n], the
desired result follows.

As we shall see next, a nonempty Z(A \ {∅}) does not necessarily imply a
nonempty Z(A).

Proposition 10. Let A be a UC family such that U (A) = [n] and ∅ ∈ A. A
nonempty Z(A \ {∅}) does not necessarily imply a nonempty Z(A).

Proof. Let S := {∅, {1, 2, 3} , {1, 4, 5} , {1, 2, 3, 4} , {1, 2, 3, 5} , {1, 2, 4, 5}} ⊂ P([5])
and let ̃S := S \ {∅}. Let A := ⟨S⟩ and ̃A := ⟨ ̃S⟩. Morris [16] proved that Z(A)
is empty. We show that Z( ̃A) is nonempty. Observe that if we write each set in
̃A as a column of an n × m binary matrix M , we have more entries with ones
than zeros. We conclude similarly for B ⊆ P([n]) such that B = P([n] \ {j}) ⊎ ̃A
for all j ∈ [n]. Hence, the (component-wise) all one vector is contained in
Z( ̃A).

Corollary 5. The reverse implication in Proposition 9 does not necessarily
hold.

Proof. Follows directly from the proof of Proposition 10 where we exhibit an
A such that ∅ ∈ A and Z(A) is empty. Then for each j ∈ [n] we see that the
binary matrix that represents G = (P([n] \ {j}) ⊎ A) \ P([n] \ {j}) has more
entries with ones than zeros.

Finally, we give a negative answer to Morris’ question, and also Vaughan’s
question.
 18

Let S := {∅, {2, 3, 4, 6, 7} , {1, 2, 3, 4} , {1, 3, 4, 6} , {5, 6, 7} , {3, 4, 7}} ⊂ P([7]).
Furthermore, deﬁne D := ⟨S⟩.

Proposition 11. Z(D) is nonempty.

Proof. We simply write down the relevant inequalities and exhibit a vector in
Z(D). The order of display matches j in B = P([7] \ {j}) ⊎ D for each j ∈ [7].

−52z1 + 4z2 + 12z3 + 12z4 + 4z6 ≥ 0
+6z1 − 54z2 + 10z3 + 10z4 + 2z6 + 2z7 ≥ 0
+6z1 + 2z2 − 42z3 + 22z4 + 2z6 + 10z7 ≥ 0
+6z1 + 2z2 + 22z3 − 42z4 + 2z6 + 10z7 ≥ 0
−48z5 + 16z6 + 16z7 ≥ 0
+5z1 + 1z2 + 7z3 + 7z4 + 13z5 − 41z6 + 15z7 ≥ 0
+12z3 + 12z4 + 12z5 + 12z6 − 36z7 ≥ 0

The vector (7, 5, 12, 12, 10, 14, 16) ∈ Z
7
≥0 is contained in Z(D).

Proposition 12. D is a Non–FC-family.

Proof. Using Algorithm 1 we exhibit a system of linear inequalities that is in-
feasible and the result follows from Corollary 3. As a certiﬁcate of infeasibility
we display Farkas dual values in square brackets before each inequality. Struc-
turally, we see that the only diﬀerence between the UC families that generated
this system of linear inequalities and the previous one are the red inequalities. In
contrast to the other inequalities, the red one here is derived from the following
UC family: (P([7] \ {3} \ {4}) ⊎ D) ∪ {{1, 3, 4} , {1, 3, 4, 5}}.

[1] : z1 + z2 + z3 + z4 + z5 + z6 + z7 ≥ 1
[19] : −52z1 + 4z2 + 12z3 + 12z4 + 4z6 ≥ 0
[2] : +6z1 − 54z2 + 10z3 + 10z4 + 2z6 + 2z7 ≥ 0
[109] : +8z1 − 8z3 − 8z4 + 8z7 ≥ 0
[16] : −48z5 + 16z6 + 16z7 ≥ 0
[20] : +5z1 + 1z2 + 7z3 + 7z4 + 13z5 − 41z6 + 15z7 ≥ 0
[40] : +12z3 + 12z4 + 12z5 + 12z6 − 36z7 ≥ 0

Corollary 6. Let A be a UC family such that U (A) = [n] and ∅ ∈ A. A
nonempty Z(A) does not necessarily imply that there exists a feasible solution
of I A.

Proof. From Proposition 11 combined with Proposition 12, followed by Corol-
lary 3.

Corollary 7. Let A be a UC family such that U (A) = [n] and ∅ ∈ A. A solution
to the system of equations from Question 1 in y ∈ Rn
≥0 such that ∑i∈[n] yi ≤ 1
does not necessarily imply that P A is nonempty.

Proof. Considering D as above with Observation 1 and the proof of Corollary 6
yields the desired result. Alternatively in the appendix we show that, given D,
there exists a solution to the system of equations from Question 1 in y ∈ Rn
≥0
such that ∑i∈[n] yi ≤ 1. This coupled with Proposition 12 and Corollary 3,
yields the result again.
 19

Conclusion

In this work we design a cutting-plane algorithm that determines if a given UC
family necessarily implies Frankl’s conjecture for all families that contain it.
By employing exact rational integer programming and highly redundant veriﬁ-
cation routines, we classify more previously unknown miminal non-isomorphic
FC-families than the total output of the past twenty-ﬁve years of research on
the topic. The eﬀects of safely automating the discovery of FC-families allow us
to answer several open questions of Morris [16] and Vaughan [20]. In particular,
the counterexamples we exhibit to settle open questions of interest require no
trust from the reader, in the sense that they are independent of the complex
optimization processeses that led to them, and can be checked by hand. Fur-
thermore, our framework can be used to improve several other results in the
following ways:

• Since Algorithm 1 determines exactly whether a given UC family A if FC
or Non–FC for 6 ≤ n ≤ 10, lower bounds for previously unknown F C(k, n)
in this range become trivial to obtain. Furthermore when coupled with
a computer algebra system or graph isomorphism software to obtain the
isomorphism types of generators, upper or exact bounds for previously
unknown F C(k, n) are obtained in the aforementioned range.

• The approach of Morris [16] for the classiﬁcation of FC-families on ﬁve
elements lends itself well to being generalized within our framework. The
number of minimal non-isomorphic generators for FC-families seems to
quickly grow for n ≥ 6, but we believe a complete classiﬁcation for n = 6
is possible with routine work.

• Proving the 3-sets conjecture of Morris [16], by recovering the arguments
of Vaughan [21] through a classiﬁcation of F C(3, n) for 7 ≤ n ≤ 9 and
using Morris’s lower bound on 3-sets, is within reach.

Acknowledgements

The author would like to thank Martin Grötschel, Ralf Borndörfer, Felipe Ser-
rano and Axel Werner for fruitful discussions, and Ambros Gleixner and Stephen
Maher for their helpful suggestions about SCIP and exact SCIP.

References

[1] Gurobi Optimizer Reference Manual. http://www.gurobi.com. Accessed:
2017-07-17.

[2] Martin Aigner, Günter M Ziegler, and Alﬁo Quarteroni. Proofs from the
Book, volume 274. Springer, 2010.

[3] Ivica Bošnjak and Petar Markovic. The 11-element case of Frankl’s conjec-
ture. The Electronic Journal of Combinatorics, 15(1):R88, 2008.

20

[4] Henning Bruhn, Pierre Charbit, Oliver Schaudt, and Jan Arne Telle. The
graph formulation of the union-closed sets conjecture. European Journal of
Combinatorics, 43:210–219, 2015.

[5] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets
conjecture. Graphs and Combinatorics, 31(6):2043–2074, 2015.

[6] Kevin KH Cheung, Ambros Gleixner, and Daniel E Steﬀy. Verifying In-
teger Programming Results. In International Conference on Integer Pro-
gramming and Combinatorial Optimization, pages 148–160. Springer, 2017.

[7] William Cook, Thorsten Koch, Daniel E Steﬀy, and Kati Wolter. A hybrid
branch-and-bound approach for exact rational mixed-integer programming.
Mathematical Programming Computation, 5(3):305–344, 2013.

[8] IBM ILOG CPLEX. V12. 1: User’s Manual for CPLEX. International
Business Machines Corporation, 46(53):157, 2009.

[9] Gerald Gamrath, Tobias Fischer, Tristan Gally, Ambros M. Gleixner, Gre-
gor Hendel, Thorsten Koch, Stephen J. Maher, Matthias Miltenberger,
Benjamin Müller, Marc E. Pfetsch, Christian Puchert, Daniel Rehfeldt,
Sebastian Schenker, Robert Schwarz, Felipe Serrano, Yuji Shinano, Stefan
Vigerske, Dieter Weninger, Michael Winkler, Jonas T. Witt, and Jakob
Witzig. The SCIP Optimization Suite 3.2. Technical Report 15-60, ZIB,
Takustr.7, 14195 Berlin, 2016.

[10] Weidong Gao and Hongquan Yu. Note on the Union-Closed Sets Conjec-
ture. Ars Comb., 49, 1998.

[11] Ambros M Gleixner. Exact and fast algorithms for mixed-integer nonlinear
programming. Dissertation, Technische Universität Berlin, 2015.

[12] Timothy Gowers. Polymath11–func4. https://gowers.wordpress.com.
Accessed: 2017-07-17.

[13] Robert T Johnson and Theresa P Vaughan. On union-closed families, I.
Journal of Combinatorial Theory, Series A, 84(2):242–249, 1998.

[14] Filip Marić, Miodrag Živković, and Bojan Vučković. Formalizing Frankl’s
conjecture: FC-families. In International Conference on Intelligent Com-
puter Mathematics, pages 248–263. Springer, 2012.

[15] Petar Markovic. An attempt at Frankl’s conjecture. Publications de
l’Institut Mathématique. Nouvelle Série, 81(95):29–43, 2007.

[16] Robert Morris. FC-families and improved bounds for Frankl’s conjecture.
European Journal of Combinatorics, 27(2):269–282, 2006.

[17] Bjorn Poonen. Union-closed families. Journal of Combinatorial Theory,
Series A, 59(2):253–268, 1992.

[18] Jonad Pulaj, Annie Raymond, and Dirk Theis. New Conjectures for Union-
Closed Families. arXiv preprint arXiv:1512.00083, 2015.

21

[19] Theresa P Vaughan. Families implying the Frankl conjecture. European
Journal of Combinatorics, 23(7):851–860, 2002.

[20] Theresa P Vaughan. A note on the union-closed sets conjecture. Journal
of Combinatorial Mathematics and Combinatorial Computing, 45:97–110,
2003.

[21] Theresa P Vaughan. Three-sets in a union-closed family. Journal of Com-
binatorial Mathematics and Combinatorial Computing, 49:73–84, 2004.

[22] Bojan Vuckovic and Miodrag Zivkovic. The 12 element case of Frankl’s
conjecture. preprint, 2012.

A Appendix

To check the claims of infeasibility for the linear systems in this paper it is
suﬃcient to ensure that the vector of values exhibited in square brackets before
each row corresponds to the vector y in the theorem below.

Theorem 5 (Farkas’ Lemma). Let A1 ∈ Rm1×n, A2 ∈ Rm2×n and A3 ∈
Rm3×n. Also let b1 ∈ Rm1, b2 ∈ Rm2 and b3 ∈ Rm3. Then the following system
of linear equalities and inequalities in x ∈ Rn :

A1x = b1
A2x ≤ b2
A3x ≥ b3
x ≥ 0

is infeasible if and only if there exist y1 ∈ Rm1 , y2 ∈ Rm2, y3 ∈ Rm3 such that:

b⊤
1 y1 + b⊤
2 y2 + b⊤
3 y3 > 0

A
⊤
1 y1 + A
⊤
2 y2 + A
⊤
3 y3 ≤ 0

y2 ≤ 0
y3 ≥ 0

Proof of Proposition 8. We identify sets in P([6]) with the columns in the ma-
trix below. For each column, the number on the top row represents its corre-
sponding variable index in IP (⟨S′⟩, c). Column c corresponds to a weight vector
for the elements in [n]. The columns representing families of sets S′ and T are
colored red and blue, respectively. As previously, ⟨S′⟩ = S′ ∪ T .

c 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
16 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
8 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
12 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
20 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0
17 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
15 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0

22

32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0
1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0

We prove that IP (⟨S′⟩, c) with some added valid FC and FC-chain inequali-
ties is infeasible by branching on x0 and showing that the linear relaxations
of the two subproblems are infeasible. We denote an explicit FC-chain by
Bi S
−→ Bk U
−→ . . . Bp T
−→ Bj, where S, U, T satisfy either condition listed in Deﬁni-
tion 4. When needed we specify which type of inequalities form an FC-chain by
SUC , U UC , T UC for UC inequalities, and SF S, U F S, T F S for FS inequalites. We
show infeasibility by explicitly exhibiting Farkas dual values (shown in square
brackets) for each row of some irreducible infeasible subset of constraints. It
suﬃces to show the infeasibilty of the following system (trivial inequalities not
shown):

1. [44] : x0 = 1.

2. UC inequalites:

[−2] : x11 + x45 − x9 ≤ 1, [−3] : x13 + x59 − x9 ≤ 1,

[−2] : x14 + x43 − x10 ≤ 1, [−1] : x22 + x61 − x20 ≤ 1,

[−3] : x23 + x60 − x20 ≤ 1, [−1] : x35 + x45 − x33 ≤ 1,

[−3] : x35 + x62 − x34 ≤ 1, [−6] : x37 + x59 − x33 ≤ 1,

[−1] : x38 + x43 − x34 ≤ 1, [−3] : x38 + x45 − x36 ≤ 1,

[−1] : x38 + x61 − x36 ≤ 1, [−1] : x39 + x44 − x36 ≤ 1,

[−2] : x42 + x55 − x34 ≤ 1, [−2] : x53 + x43 − x33 ≤ 1,

[−5] : x54 + x43 − x34 ≤ 1, [−3] : x44 + x55 − x36 ≤ 1,

[−4] : x47 + x49 − x33 ≤ 1.

3. FS inequalities:

[0] : x47 − x1 ≤ 0, [−6] : x63 − x1 ≤ 0, [−14] : x63 − x8 ≤ 0,

[−1] : x7 − x4 ≤ 0, [−16] : x55 − x4 ≤ 0, [−12] : x63 − x12 ≤ 0,

[−3] : x14 − x2 ≤ 0, [−24] : x46 − x2 ≤ 0, [−12] : x47 − x3 ≤ 0,

[−21] : x61 − x17 ≤ 0, [−19] : x62 − x18 ≤ 0, [−4] : x63 − x19 ≤ 0,

[−24] : x31 − x24 ≤ 0, [−1] : x37 − x32 ≤ 0, [−4] : x38 − x32 ≤ 0,

[−23] : x39 − x32 ≤ 0, [−16] : x47 − x40 ≤ 0, [−11] : x55 − x48 ≤ 0,

[−8] : x63 − x56 ≤ 0.

4. FC inequalities:

[−2] : x15 + x53 − x1 − x5 ≤ 0, [−7] : x15 + x57 − x1 − x9 ≤ 0,

[−9] : x58 + x15 − x8 − x10 ≤ 0, [−2] : x15 + x59 − x1 − x11 ≤ 0,

[−7] : x45 + x23 − x1 − x5 ≤ 0, [−5] : x60 + x23 − x20 − x16 ≤ 0,

[−1] : x61 + x23 − x21 − x16 ≤ 0, [−5] : x45 + x27 − x1 − x9 ≤ 0,

23

[−3] : x27 + x61 − x25 − x16 ≤ 0, [0] : x43 + x29 − x1 − x9 ≤ 0,

[−5] : x54 + x29 − x20 − x16 ≤ 0, [−6] : x29 + x59 − x16 − x25 ≤ 0,

[−4] : x43 + x30 − x10 − x8 ≤ 0, [−2] : x53 + x30 − x16 − x20 ≤ 0,

[−7] : x59 + x30 − x16 − x26 ≤ 0, [−4] : x31 + x60 − x16 − x28 ≤ 0,

[−1] : x43 + x45 − x8 − x41 ≤ 0, [−1] : x43 + x62 − x8 − x42 ≤ 0,

[−3] : x47 + x62 − x8 − x46 ≤ 0, [−3] : x51 + x62 − x16 − x50 ≤ 0,

[−7] : x7 + x54 − x4 − x6 ≤ 0, [−9] : x51 + x53 − x48 − x49 ≤ 0.

5. WV inequality:

[−0.5] : 88x0 + 58x1 + 54x2 + 24x3 + 48x4 + 18x5 + 14x6 − 16x7 + 64x8
+34x9 + 30x10 + 24x12 − 6x13 − 10x14 − 40x15 + 72x16 + 42x17
+38x18 + 8x19 + 32x20 + 2x21 − 2x22 − 32x23 + 48x24 + 18x25
+14x26 − 16x27 + 8x28 − 22x29 − 26x30 − 56x31 + 56x32 + 26x33
+22x34 − 8x35 + 16x36 − 14x37 − 18x38 − 48x39 + 32x40 + 2x41
−2x42 − 32x43 − 8x44 − 38x45 − 42x46 − 72x47 + 40x48
+10x49 + 6x50 − 24x51 − 30x53 − 34x54 − 64x55 + 16x56 − 14x57
−18x58 − 48x59 − 24x60 − 54x61 − 58x62 − 88x63 ≤ −1.

Furthermore we show that the following system of constraints is infeasible (triv-
ial ones not shown):

1. [−186.5] : x0 = 0

2. FS inequalities:

[−7.5] : x1 − x0 ≤ 0, [−10] : x6 − x0 ≤ 0, [−8.5] : x11 − x0 ≤ 0,

[0] : x19 − x0 ≤ 0, [−8.5] : x23 − x0 ≤ 0, [−4] : x35 − x0 ≤ 0,

[−7] : x37 − x0 ≤ 0, [−9] : x38 − x0 ≤ 0, [−24] : x39 − x0 ≤ 0,

[−2.5] : x41 − x0 ≤ 0, [−16] : x44 − x0 ≤ 0, [−21] : x46 − x0 ≤ 0,

[−15] : x47 − x0 ≤ 0, [−6] : x50 − x0 ≤ 0, [−19] : x55 − x0 ≤ 0,

[−5.5] : x56 − x0 ≤ 0, [−17] : x59 − x0 ≤ 0, [−16] : x61 − x0 ≤ 0,

[−11] : x62 − x0 ≤ 0, [−23] : x63 − x0 ≤ 0, [−12] : x13 − x12 ≤ 0,

[−12.5] : x14 − x2 ≤ 0, [−12.5] : x22 − x18 ≤ 0, [−6.5] : x62 − x18 ≤ 0,

[−1] : x42 − x40 ≤ 0, [−7] : x51 − x48 ≤ 0, [−7.5] : x43 − x8 ≤ 0,

[−5.5] : x29 − x17 ≤ 0, [−5.5] : x61 − x9 ≤ 0, [0] : x63 − x56 ≤ 0.

3. FC inequalities:

[−7.5] : x15 + x45 − x1 − x13 ≤ 0, [−9] : x15 + x53 − x1 − x5 ≤ 0,

[−3.5] : x15 + x57 − x1 − x9 ≤ 0, [−7.5] : x23 + x62 − x16 − x22 ≤ 0,

[−8] : x27 + x45 − x1 − x9 ≤ 0, [−8.5] : x31 + x43 − x1 − x11 ≤ 0,

[−1] : x31 + x53 − x16 − x21 ≤ 0, [−3.5] : x45 + x57 − x8 − x41 ≤ 0,

[−9] : x55 + x58 − x16 − x50 ≤ 0, [−17] : x7 + x54 − x4 − x6 ≤ 0,

[−5] : x51 + x53 − x48 − x49 ≤ 0.
 24

4. FC-chain inequalities (it is straightforward to check that the explicit chains,
where we identify sets with their respective column numbers, work as re-
quired by Proposition 6):

[−1.5] : x29 + x47 + x61 + x63 − x8 − x13 − x17 − x56 ≤ 0,

(29 19
F S
−−−→ 17), (63 8
F S
−−→ 8), (47 8
F S
−−→ 8), (61 56
F S
−−−→ 56), (63 56
F S
−−−→ 56),

(47 29
U C
−−−→ 13), (61 19
F S
−−−→ 17).

[−4] : x29 + x61 + x62 − x16 − x17 − x28 ≤ 0,

(29 16
F S
−−−→ 16), (61 19
F S
−−−→ 17), (62 19
F S
−−−→ 18 16
F S
−−−→ 16),

(29 62
U C
−−−→ 28).

[−7.5] : x30 + x31 + x47 + x63 − x8 − x14 − x16 − x24 ≤ 0,

(63 8
F S
−−→ 8), (47 8
F S
−−→ 8), (63 16
F S
−−−→ 16), (47 30
U C
−−−→ 14), (30 16
F S
−−−→ 16),

(30 56
F S
−−−→ 24), (31 16
F S
−−−→ 16), (31 56
F S
−−−→ 24).

[−4] : x30 + x31 + x55 − x19 − x22 − x24 ≤ 0,

(30 56
F S
−−−→ 24), (31 56
F S
−−−→ 24), (31 19
F S
−−−→ 19), (55 30
U C
−−−→ 22), (55 19
F S
−−−→ 19).

[−7] : x30 + x31 + x59 − x16 − x24 − x26 ≤ 0,

(30 56
F S
−−−→ 24), (31 56
F S
−−−→ 24), (31 16
F S
−−−→ 16), (30 16
F S
−−−→ 16),

(59 16
F S
−−−→ 16), (59 30
U C
−−−→ 26).

[0] : x47 + x54 + x63 − x8 − x16 − x38 ≤ 0,

(63 8
F S
−−→ 8), (63 16
F S
−−−→ 16), (47 8
F S
−−→ 8), (54 16
F S
−−−→ 16), (54 47
U C
−−−→ 38).

[−12] : x47 + x60 + x63 − x8 − x44 − x56 ≤ 0.

(47 8
F S
−−→ 8), (63 8
F S
−−→ 8), (63 56
F S
−−−→ 56), (60 56
F S
−−−→ 56), (60 47
U C
−−−→ 44).

5. WV inequality:

[−0.5] : 58x1 + 54x2 + 24x3 + 48x4 + 18x5 + 14x6 − 16x7 + 64x8
+34x9 + 30x10 + 24x12 − 6x13 − 10x14 − 40x15 + 72x16 + 42x17
+38x18 + 8x19 + 32x20 + 2x21 − 2x22 − 32x23 + 48x24 + 18x25
+14x26 − 16x27 + 8x28 − 22x29 − 26x30 − 56x31 + 56x32 + 26x33
+22x34 − 8x35 + 16x36 − 14x37 − 18x38 − 48x39 + 32x40 + 2x41
−2x42 − 32x43 − 8x44 − 38x45 − 42x46 − 72x47 + 40x48
+10x49 + 6x50 − 24x51 − 30x53 − 34x54 − 64x55 + 16x56 − 14x57
−18x58 − 48x59 − 24x60 − 54x61 − 58x62 − 88x63 ≤ −1.

Another proof of Corollary 7. Next, we explicitly answer Vaughan’s question in
the negative. Given ⟨S⟩, we show that there exists a nonnegative solution to the
system of equations in Question 1 such that ∑
i∈[n] yi ≤ 1, where S is deﬁned as
in the counterexample to Morris’s question. Furthermore the order of display
of equations is the same as previously.
25

24y1 + 80y2 + 88y3 + 88y4 + 76y5 + 80y6 + 76y7 = 76
80y1 + 20y2 + 84y3 + 84y4 + 74y5 + 76y6 + 76y7 = 74
92y1 + 88y2 + 44y3 + 108y4 + 86y5 + 88y6 + 96y7 = 86
92y1 + 88y2 + 108y3 + 44y4 + 86y5 + 88y6 + 96y7 = 86
80y1 + 80y2 + 80y3 + 80y4 + 32y5 + 96y6 + 96y7 = 80
92y1 + 88y2 + 94y3 + 94y4 + 100y5 + 46y6 + 102y7 = 87
92y1 + 92y2 + 104y3 + 104y4 + 104y5 + 104y6 + 56y7 = 92

Let ¯y1 = 28304
309701 ,¯y2 = 60251
738922 , ¯y3 = 94175
606582 , ¯y4 = 94175
606582 , ¯y5 = 63417
493048 , ¯y6 = 158373
872233 ,
¯y7 = 95228
462227 . Then ¯y ∈ Q7
≥0 such that ¯y = (¯y1, ¯y2, . . . , ¯y7) is a solution to the
system of linear equations above such that the following holds,

∑

i∈[7] ¯yi = 6896010572642828356716603827169373
6898390222382701705240892810504568 < 1.

26

Previously unknown minimal nonisomorphic generators for FC-families on [6]
1256, 3456, 456, 236 1 ↦→ 7, 2 ↦→ 15, 3 ↦→ 15, 4 ↦→ 11, 5 ↦→ 14, 6 ↦→ 20
12456, 2346, 456, 356 1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 6, 6 ↦→ 7
12345, 1356, 456, 356 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 5, 6 ↦→ 5
12345, 2346, 456, 236 1 ↦→ 2, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 3, 5 ↦→ 4, 6 ↦→ 5
12345, 2346, 456, 236 1 ↦→ 2, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 3, 5 ↦→ 4, 6 ↦→ 5
12346, 1256, 456, 356 1 ↦→ 4, 2 ↦→ 4, 3 ↦→ 7, 4 ↦→ 7, 5 ↦→ 9, 6 ↦→ 10
12356, 1345, 456, 236 1 ↦→ 8, 2 ↦→ 12, 3 ↦→ 16, 4 ↦→ 15, 5 ↦→ 17, 6 ↦→ 20
12356, 1234, 456, 356 1 ↦→ 8, 2 ↦→ 8, 3 ↦→ 24, 4 ↦→ 24, 5 ↦→ 27, 6 ↦→ 29
12456, 1356, 456, 326 1 ↦→ 45, 2 ↦→ 71, 3 ↦→ 77, 4 ↦→ 59, 5 ↦→ 74, 6 ↦→ 103
136, 2456, 3456, 456, 123 1 ↦→ 6, 2 ↦→ 5, 3 ↦→ 7, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 6
136, 1256, 3456, 456, 123 1 ↦→ 2, 2 ↦→ 1, 3 ↦→ 2, 4 ↦→ 1, 5 ↦→ 1, 6 ↦→ 2
2346, 3456, 2456, 2356, 1234 1 ↦→ 2, 2 ↦→ 5, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 4, 6 ↦→ 5
3456, 2456, 2356, 1346, 1246, 1234 1 ↦→ 3, 2 ↦→ 4, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 3, 6 ↦→ 4
3456, 2456, 2356, 1346, 1245, 1234 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 2, 5 ↦→ 2, 6 ↦→ 2
3456, 2456, 1456, 1236, 1235, 1234 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 1, 5 ↦→ 1, 6 ↦→ 1
3456, 2456, 1356, 1246, 1235, 1234 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 1, 5 ↦→ 1, 6 ↦→ 1
3456, 2456, 2356, 2346, 1456, 1356 1 ↦→ 8, 2 ↦→ 14, 3 ↦→ 15, 4 ↦→ 15, 5 ↦→ 16, 6 ↦→ 19
3456, 2456, 2356, 2346, 1456, 1236 1 ↦→ 3, 2 ↦→ 4, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 4, 6 ↦→ 5
3456, 2456, 2356, 1456, 1356, 1234 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 1, 5 ↦→ 1, 6 ↦→ 1
3456, 2456, 2356, 1456, 1346, 1245 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 3
3456, 2456, 2356, 1456, 1346, 1235 1 ↦→ 5, 2 ↦→ 4, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 6, 6 ↦→ 6
3456, 2456, 2356, 1456, 1236, 1235 1 ↦→ 2, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 2, 5 ↦→ 3, 6 ↦→ 3
3456, 2456, 2356, 1456, 1236, 1234 1 ↦→ 4, 2 ↦→ 5, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 4, 6 ↦→ 5
3456, 2456, 2356, 1346, 1345, 1246 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 3
3456, 2456, 2356, 1346, 1246, 1235 1 ↦→ 3, 2 ↦→ 4, 3 ↦→ 4, 4 ↦→ 3, 5 ↦→ 4, 6 ↦→ 4
12346, 3456, 2456, 2356, 1456, 1356, 1256 1 ↦→ 5, 2 ↦→ 5, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 6, 6 ↦→ 7
1236, 3456, 2456, 2356, 1456, 1356, 1246 2 ↦→ 2, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 4
1456, 3456, 2456, 2356, 1346, 1246, 1236 2 ↦→ 3, 2 ↦→ 2, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 4
1256, 3456, 2456, 2356, 1456, 1346, 1236 2 ↦→ 2, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 4
2356, 2456, 345, 13456, 12346 2 ↦→ 3, 2 ↦→ 8, 3 ↦→ 12, 4 ↦→ 12, 5 ↦→ 13, 6 ↦→ 9
1234, 1256, 246, 23456, 13456 2 ↦→ 9, 2 ↦→ 12, 3 ↦→ 7, 4 ↦→ 11, 5 ↦→ 7, 6 ↦→ 11
1236, 2456, 125, 23456, 13456 2 ↦→ 32, 2 ↦→ 34, 3 ↦→ 19, 4 ↦→ 16, 5 ↦→ 32, 6 ↦→ 25
1246, 1256, 123, 23456, 13456 2 ↦→ 7, 2 ↦→ 7, 3 ↦→ 6, 4 ↦→ 3, 5 ↦→ 4, 6 ↦→ 5

Table 1: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 27

Previously unknown minimal nonisomorphic generators for FC-families on [7]
3457, 567, 467, 123 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 3, 4 ↦→ 5, 5 ↦→ 5, 6 ↦→ 6, 7 ↦→ 7
2467, 567, 347, 126 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 1, 4 ↦→ 2, 5 ↦→ 2, 6 ↦→ 3, 7 ↦→ 3
357, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 6, 4 ↦→ 2, 5 ↦→ 5, 6 ↦→ 5, 7 ↦→ 7
356, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 4, 4 ↦→ 1, 5 ↦→ 3, 6 ↦→ 4, 7 ↦→ 3
257, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 1, 5 ↦→ 2, 6 ↦→ 2, 7 ↦→ 3
256, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 2, 4 ↦→ 1, 5 ↦→ 3, 6 ↦→ 4, 7 ↦→ 3
346, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 4, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 4, 7 ↦→ 2
245, 367, 4567, 1237 1 ↦→ 2, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 2, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 4
246, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 4, 7 ↦→ 1
235, 367, 4567, 1237 1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 1, 5 ↦→ 3, 6 ↦→ 4, 7 ↦→ 1
234, 367, 4567, 1237 1 ↦→ 2, 2 ↦→ 4, 3 ↦→ 7, 4 ↦→ 5, 5 ↦→ 5, 6 ↦→ 5, 7 ↦→ 4
12456, 34567, 267, 127 1 ↦→ 78, 2 ↦→ 105, 3 ↦→ 16, 4 ↦→ 27, 5 ↦→ 27, 6 ↦→ 84, 7 ↦→ 103
12456, 34567, 267, 257 1 ↦→ 1, 2 ↦→ 9, 3 ↦→ 1, 4 ↦→ 2, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 9
3467, 4567, 2367, 2345, 1357 1 ↦→ 20, 2 ↦→ 36, 3 ↦→ 52, 4 ↦→ 45, 5 ↦→ 46, 6 ↦→ 39, 7 ↦→ 49
3456, 4567, 2367, 1357, 1247 1 ↦→ 15, 2 ↦→ 15, 3 ↦→ 20, 4 ↦→ 18, 5 ↦→ 19, 6 ↦→ 19, 7 ↦→ 23
3456, 4567, 2367, 1357, 1246 1 ↦→ 17, 2 ↦→ 16, 3 ↦→ 22, 4 ↦→ 19, 5 ↦→ 21, 6 ↦→ 24, 7 ↦→ 22
2347, 4567, 3567, 1267, 1245 1 ↦→ 69, 2 ↦→ 91, 3 ↦→ 71, 4 ↦→ 93, 5 ↦→ 87, 6 ↦→ 81, 7 ↦→ 103
2346, 4567, 3567, 2347, 1267 1 ↦→ 6, 2 ↦→ 13, 3 ↦→ 14, 4 ↦→ 14, 5 ↦→ 9, 6 ↦→ 16, 7 ↦→ 16
2345, 4567, 3567, 1247, 1236 1 ↦→ 24, 2 ↦→ 32, 3 ↦→ 33, 4 ↦→ 33, 5 ↦→ 32, 6 ↦→ 31, 7 ↦→ 31
2345, 4567, 2367, 1357, 1247 1 ↦→ 3, 2 ↦→ 4, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 4, 6 ↦→ 3, 7 ↦→ 4
2345, 4567, 2367, 1357, 1246 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 2, 5 ↦→ 2, 6 ↦→ 2, 7 ↦→ 2
1356, 4567, 2367, 2345, 1357 1 ↦→ 5, 2 ↦→ 6, 3 ↦→ 9, 4 ↦→ 6, 5 ↦→ 9, 6 ↦→ 8, 7 ↦→ 8
12456, 13457, 23457, 12367, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 11, 2 ↦→ 12, 3 ↦→ 11, 4 ↦→ 13, 5 ↦→ 13, 6 ↦→ 14, 7 ↦→ 15

12345, 13457, 23457, 12367, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 12, 2 ↦→ 12, 3 ↦→ 13, 4 ↦→ 13, 5 ↦→ 13, 6 ↦→ 12, 7 ↦→ 15

12345, 23456, 23457, 12367, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 8, 7 ↦→ 8

12345, 13456, 23457, 12367, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 6, 5 ↦→ 6, 6 ↦→ 7, 7 ↦→ 7

23456, 12457, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 8, 5 ↦→ 8, 6 ↦→ 8, 7 ↦→ 8

12356, 12457, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 8, 2 ↦→ 8, 3 ↦→ 8, 4 ↦→ 8, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 10

23456, 14567, 13567, 13467, 13457,
13456, 12567, 12467, 12457, 12456,
12367, 12357, 12356, 12347
 1 ↦→ 14, 2 ↦→ 12, 3 ↦→ 12, 4 ↦→ 11, 5 ↦→ 12, 6 ↦→ 12, 7 ↦→ 11

23456, 14567, 13567, 13467, 13457,
13456, 12567, 12467, 12457, 12456,
12367, 12357, 12346, 12345 1 ↦→ 7, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 6, 5 ↦→ 6, 6 ↦→ 6, 7 ↦→ 5

Table 2: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 28

Previously unknown minimal nonisomorphic generators for FC-families on [7]
23456, 12357, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 7, 2 ↦→ 10, 3 ↦→ 10, 4 ↦→ 10, 5 ↦→ 11, 6 ↦→ 11, 7 ↦→ 12

12456, 12357, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 9, 2 ↦→ 9, 3 ↦→ 8, 4 ↦→ 9, 5 ↦→ 10, 6 ↦→ 10, 7 ↦→ 11

12346, 12357, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 12, 2 ↦→ 12, 3 ↦→ 13, 4 ↦→ 13, 5 ↦→ 12, 6 ↦→ 13, 7 ↦→ 15

13456, 23456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 7

12456, 23456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 7

12356, 23456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 7, 2 ↦→ 7, 3 ↦→ 8, 4 ↦→ 8, 5 ↦→ 8, 6 ↦→ 9, 7 ↦→ 9

12345, 23456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 8, 4 ↦→ 9, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 9

12356, 12456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 6, 5 ↦→ 6, 6 ↦→ 7, 7 ↦→ 7

12345, 12456, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 7

12346, 12356, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 6, 5 ↦→ 6, 6 ↦→ 7, 7 ↦→ 7

12345, 12356, 13457, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 9, 2 ↦→ 9, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 10, 6 ↦→ 10, 7 ↦→ 10

23456, 12347, 12357, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 5, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 8

13456, 12347, 12357, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 7, 4 ↦→ 7, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 8

12356, 12347, 12357, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567 1 ↦→ 6, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 6, 5 ↦→ 7, 6 ↦→ 7, 7 ↦→ 8

12345, 12347, 12357, 23457, 12467,
13467, 23467, 12567, 13567, 23567,
14567, 24567, 34567
 1 ↦→ 11, 2 ↦→ 12, 3 ↦→ 12, 4 ↦→ 12, 5 ↦→ 12, 6 ↦→ 11, 7 ↦→ 14

Table 3: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 29

Previously unknown minimal nonisomorphic generators for FC-families on [7]
34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12367, 12347 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 8, 6 ↦→ 9, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12367, 12346 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 8, 6 ↦→ 9, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12367, 12345 1 ↦→ 3, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 4, 6 ↦→ 4, 7 ↦→ 4

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12357, 12347 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 9, 6 ↦→ 8, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12357, 12346 1 ↦→ 3, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 4, 5 ↦→ 4, 6 ↦→ 4, 7 ↦→ 4

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12357, 12345 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 9, 6 ↦→ 8, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12347, 12346 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 8, 6 ↦→ 9, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12347, 12345 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 9, 6 ↦→ 8, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12457, 12346, 12345 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 8

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 13456,
12347, 12346, 12345 1 ↦→ 7, 2 ↦→ 7, 3 ↦→ 9, 4 ↦→ 9, 5 ↦→ 8, 6 ↦→ 8, 7 ↦→ 8

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 12457,
12456, 12347, 12346 1 ↦→ 8, 2 ↦→ 9, 3 ↦→ 9, 4 ↦→ 10, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13467, 12457,
12456, 12347, 12345 1 ↦→ 8, 2 ↦→ 9, 3 ↦→ 9, 4 ↦→ 10, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13456, 12567,
12456, 12367, 12357 1 ↦→ 7, 2 ↦→ 8, 3 ↦→ 8, 4 ↦→ 7, 5 ↦→ 9, 6 ↦→ 9, 7 ↦→ 8

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13456, 12567,
12456, 12367, 12356 1 ↦→ 7, 2 ↦→ 9, 3 ↦→ 9, 4 ↦→ 8, 5 ↦→ 10, 6 ↦→ 10, 7 ↦→ 9

34567, 24567, 23567, 23467, 23457,
23456, 14567, 13567, 13456, 12567,
12456, 12356, 12347 1 ↦→ 6, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 7, 5 ↦→ 8, 6 ↦→ 8, 7 ↦→ 7

Table 4: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 30

Previously-unknown minimal nonisomorphic generators for FC-families on [8]
678, 578, 346, 125 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 1, 5 ↦→ 2, 6 ↦→ 2, 7 ↦→ 2, 8 ↦→ 2
678, 458, 237, 135 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 2, 4 ↦→ 1, 5 ↦→ 2, 6 ↦→ 1, 7 ↦→ 2, 8 ↦→ 2
1578, 678, 458, 237 1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 4, 6 ↦→ 4, 7 ↦→ 6, 8 ↦→ 6
1567, 678, 458, 237 1 ↦→ 1, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 2, 5 ↦→ 3, 6 ↦→ 3, 7 ↦→ 4, 8 ↦→ 4
1457, 678, 458, 237 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 2, 5 ↦→ 2, 6 ↦→ 2, 7 ↦→ 3, 8 ↦→ 3
45678, 1246, 678, 578, 346 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 4, 4 ↦→ 5, 5 ↦→ 3, 6 ↦→ 7, 7 ↦→ 5, 8 ↦→ 5
35678, 2357, 678, 458, 123 1 ↦→ 18, 2 ↦→ 25, 3 ↦→ 30, 4 ↦→ 28, 5 ↦→ 40, 6 ↦→ 27, 7 ↦→ 37, 8 ↦→ 44
35678, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 3, 3 ↦→ 5, 4 ↦→ 4, 5 ↦→ 5, 6 ↦→ 4, 7 ↦→ 6, 8 ↦→ 6
35678, 1246, 678, 578, 346 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 4, 6 ↦→ 8, 7 ↦→ 6, 8 ↦→ 6
34678, 2357, 678, 458, 123 1 ↦→ 8, 2 ↦→ 12, 3 ↦→ 15, 4 ↦→ 16, 5 ↦→ 19, 6 ↦→ 13, 7 ↦→ 18, 8 ↦→ 22
34578, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 5, 3 ↦→ 7, 4 ↦→ 5, 5 ↦→ 5, 6 ↦→ 5, 7 ↦→ 9, 8 ↦→ 8
34578, 1246, 678, 578, 346 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 4, 4 ↦→ 5, 5 ↦→ 3, 6 ↦→ 7, 7 ↦→ 5, 8 ↦→ 5
34568, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 4, 3 ↦→ 6, 4 ↦→ 5, 5 ↦→ 5, 6 ↦→ 6, 7 ↦→ 8, 8 ↦→ 8
25678, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 5, 3 ↦→ 6, 4 ↦→ 5, 5 ↦→ 6, 6 ↦→ 5, 7 ↦→ 8, 8 ↦→ 8
25678, 1246, 678, 578, 346 1 ↦→ 4, 2 ↦→ 8, 3 ↦→ 11, 4 ↦→ 13, 5 ↦→ 10, 6 ↦→ 20, 7 ↦→ 15, 8 ↦→ 15
24678, 1246, 678, 578, 346 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 4, 4 ↦→ 5, 5 ↦→ 3, 6 ↦→ 7, 7 ↦→ 5, 8 ↦→ 5
24578, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 7, 3 ↦→ 7, 4 ↦→ 6, 5 ↦→ 6, 6 ↦→ 7, 7 ↦→ 11, 8 ↦→ 10
24578, 1246, 678, 578, 346 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 2, 4 ↦→ 3, 5 ↦→ 2, 6 ↦→ 4, 7 ↦→ 3, 8 ↦→ 3
24568, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 4, 5 ↦→ 4, 6 ↦→ 5, 7 ↦→ 8, 8 ↦→ 7
23678, 1246, 678, 578, 346 1 ↦→ 2, 2 ↦→ 2, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 4, 6 ↦→ 8, 7 ↦→ 6, 8 ↦→ 6
23567, 1345, 678, 458, 237 1 ↦→ 2, 2 ↦→ 4, 3 ↦→ 5, 4 ↦→ 4, 5 ↦→ 5, 6 ↦→ 5, 7 ↦→ 7, 8 ↦→ 7
3456, 1458, 2378, 4678,
2347, 2458 1 ↦→ 2, 2 ↦→ 5, 3 ↦→ 5, 4 ↦→ 6, 5 ↦→ 4, 6 ↦→ 4, 7 ↦→ 5, 8 ↦→ 6
2356, 1568, 3468, 2478,
1268, 1248 1 ↦→ 7, 2 ↦→ 9, 3 ↦→ 6, 4 ↦→ 7, 5 ↦→ 5, 6 ↦→ 9, 7 ↦→ 3, 8 ↦→ 10
1357, 1356, 1348, 1346,
1345, 1278, 1268 1 ↦→ 54, 2 ↦→ 26, 3 ↦→ 42, 4 ↦→ 31, 5 ↦→ 30, 6 ↦→ 38, 7 ↦→ 31, 8 ↦→ 36
1346, 1345, 1278, 1268,
1267, 1258, 1257, 1256 1 ↦→ 7, 2 ↦→ 6, 3 ↦→ 2, 4 ↦→ 2, 5 ↦→ 5, 6 ↦→ 5, 7 ↦→ 4, 8 ↦→ 4
345678, 245678, 235678, 234678,
234578, 234568, 234567, 145678,
135678, 134678, 134578, 134568,
134567, 125678, 124678, 124578,
124568, 124567, 123678, 123578,
123568, 123567, 123478, 123468,
123467, 123456
 1 ↦→ 28, 2 ↦→ 28, 3 ↦→ 28, 4 ↦→ 28, 5 ↦→ 28, 6 ↦→ 30, 7 ↦→ 29, 8 ↦→ 29

345678, 245678, 235678, 234678,
234578, 234568, 234567, 145678,
135678, 134678, 134578, 134568,
134567, 125678, 124678, 124578,
124568, 124567, 123678, 123578,
123568, 123567, 123478, 123468,
123457, 123456
 1 ↦→ 27, 2 ↦→ 27, 3 ↦→ 27, 4 ↦→ 27, 5 ↦→ 28, 6 ↦→ 28, 7 ↦→ 28, 8 ↦→ 28

Table 5: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 31

Previously-unknown minimal nonisomorphic generators for FC-families on [9]
369, 789, 456, 123 1 ↦→ 1, 2 ↦→ 1, 3 ↦→ 2, 4 ↦→ 1, 5 ↦→ 1, 6 ↦→ 2, 7 ↦→ 1, 8 ↦→ 1, 9 ↦→ 2
348, 569, 789, 1268 1 ↦→ 4, 2 ↦→ 4, 3 ↦→ 8, 4 ↦→ 8, 5 ↦→ 9, 6 ↦→ 11, 7 ↦→ 11, 8 ↦→ 17, 9 ↦→ 16
148, 159, 6789, 2345 1 ↦→ 4, 2 ↦→ 1, 3 ↦→ 1, 4 ↦→ 3, 5 ↦→ 3, 6 ↦→ 1, 7 ↦→ 1, 8 ↦→ 3, 9 ↦→ 3
589, 129, 6789, 3459 1 ↦→ 18, 2 ↦→ 18, 3 ↦→ 10, 4 ↦→ 10, 5 ↦→ 25, 6 ↦→ 10, 7 ↦→ 10, 8 ↦→ 25, 9 ↦→ 36
489, 159, 2345, 5679 1 ↦→ 20, 2 ↦→ 8, 3 ↦→ 8, 4 ↦→ 23, 5 ↦→ 28, 6 ↦→ 10, 7 ↦→ 10, 8 ↦→ 19, 9 ↦→ 34
5689, 578, 129, 6789, 3459 1 ↦→ 3, 2 ↦→ 3, 3 ↦→ 2, 4 ↦→ 2, 5 ↦→ 6, 6 ↦→ 3, 7 ↦→ 5, 8 ↦→ 6, 9 ↦→ 6
5679, 128, 129, 6789, 3459 1 ↦→ 16, 2 ↦→ 16, 3 ↦→ 3, 4 ↦→ 3, 5 ↦→ 6, 6 ↦→ 7, 7 ↦→ 7, 8 ↦→ 15, 9 ↦→ 17
5678, 278, 129, 6789, 3459 1 ↦→ 52, 2 ↦→ 81, 3 ↦→ 16, 4 ↦→ 16, 5 ↦→ 32, 6 ↦→ 35, 7 ↦→ 58, 8 ↦→ 58, 9 ↦→ 75
4789, 578, 129, 6789, 3459 1 ↦→ 49, 2 ↦→ 49, 3 ↦→ 34, 4 ↦→ 60, 5 ↦→ 80, 6 ↦→ 36, 7 ↦→ 79, 8 ↦→ 79, 9 ↦→ 98
4789, 489, 159, 6789, 2345 1 ↦→ 20, 2 ↦→ 8, 3 ↦→ 8, 4 ↦→ 26, 5 ↦→ 24, 6 ↦→ 11, 7 ↦→ 17, 8 ↦→ 26, 9 ↦→ 36
4689, 578, 129, 6789, 3459 1 ↦→ 17, 2 ↦→ 17, 3 ↦→ 12, 4 ↦→ 21, 5 ↦→ 30, 6 ↦→ 19, 7 ↦→ 28, 8 ↦→ 33, 9 ↦→ 35
4689, 478, 159, 6789, 2345 1 ↦→ 12, 2 ↦→ 6, 3 ↦→ 6, 4 ↦→ 24, 5 ↦→ 15, 6 ↦→ 14, 7 ↦→ 21, 8 ↦→ 25, 9 ↦→ 21
4679, 158, 159, 6789, 2345 1 ↦→ 18, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 6, 5 ↦→ 19, 6 ↦→ 7, 7 ↦→ 7, 8 ↦→ 16, 9 ↦→ 17
4678, 578, 159, 6789, 2345 1 ↦→ 9, 2 ↦→ 3, 3 ↦→ 3, 4 ↦→ 6, 5 ↦→ 16, 6 ↦→ 6, 7 ↦→ 11, 8 ↦→ 11, 9 ↦→ 12
4589, 589, 159, 6789, 2345 1 ↦→ 5, 2 ↦→ 2, 3 ↦→ 2, 4 ↦→ 4, 5 ↦→ 8, 6 ↦→ 2, 7 ↦→ 2, 8 ↦→ 6, 9 ↦→ 8

Table 6: Frankl’s conjecture holds for all UC families which contain the following
subfamilies

Previously-unknown minimal nonisomorphic generators for FC-families on [10]
123, 124, 356, 678, 79(10) 1 ↦→ 6, 2 ↦→ 6, 3 ↦→ 8, 4 ↦→ 4, 5 ↦→ 5, 6 ↦→ 7, 7 ↦→ 5, 8 ↦→ 4, 9 ↦→ 2, 10 ↦→ 2
123, 124, 356, 678, 3489(10) 1 ↦→ 7, 2 ↦→ 7, 3 ↦→ 5, 4 ↦→ 5, 5 ↦→ 5, 6 ↦→ 6, 7 ↦→ 3, 8 ↦→ 3, 9 ↦→ 1, 10 ↦→ 1

Table 7: Frankl’s conjecture holds for all UC families which contain the following
subfamilies
 32
