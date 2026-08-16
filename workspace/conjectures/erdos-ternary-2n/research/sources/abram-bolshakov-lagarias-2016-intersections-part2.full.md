<!-- source: https://arxiv.org/pdf/1508.05967 | converted from PDF -->

arXiv:1508.05967v2  [math.NT]  15 Dec 2015
INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF
3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES

WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

ABSTRACT. This paper studies the structure of ﬁnite intersections of general multiplica-
tive translates C(M1, M2, . . . , Mn) = 1
M1 Σ3,¯2 ∩· · ·∩ 1
Mn Σ3,¯2 for integers 1 ≤ M1 <
M2 < · · · < Mn, in which Σ3,¯2 denotes the 3-adic Cantor set (of 3-adic integers whose
expansions omit the digit 2), which has Hausdorff dimension log3 2 ≈ 0.630929. This
study was motivated by questions concerning the discrete dynamical system on the 3-adic
integers Z3 given by multiplication by 2. The exceptional set E(Z3) is deﬁned to be the
set of all elements of Z3 whose forward orbits under this action intersect the 3-adic Cantor
set Σ3,¯2 inﬁnitely many times. It is conjectured that it has Hausdorff dimension 0. An
earlier paper showed that upper bounds on the Hausdorff dimension of the exceptional set
can be extracted from knowing Hausdorff dimensions of sets of the kind above, in cases
where all Mi are powers of 2. These intersection sets were shown to be fractals whose
points have 3-adic expansions describable by labeled paths in a ﬁnite automaton, whose
Hausdorff dimension is exactly computable and is of the form log3(β) where β is a real
algebraic integer. It gave algorithms for determination of the automaton, and computed
examples showing that the dependence of the automaton and the value β on the parame-
ters (M1, . . . , Mn) is complicated. The present paper studies two new inﬁnite families of
examples, illustrating interesting behavior of the automata and of the Hausdorff dimension
of the associated fractals. One family has associated automata whose directed graph has a
nested sequence of strongly connected components of arbitrarily large depth. The second
family leads to an improved upper bound for the Hausdorff dimension of the exceptional
set E(Z3) of log3 φ ≈ 0.438018, where φ denotes the Golden ratio.

CONTENTS

1. Introduction 2
1.1. Exceptional set conjecture and nesting constants 4
1.2. Statistics of ternary digits and n-digit Hausdorff dimension constant 5
1.3. Roadmap 6
2. Results 6
2.1. The inﬁnite family Pk = (20k−11)3 6
2.2. The inﬁnite family Qk = (2k0k−11)3 8
2.3. The n-digit Hausdorff dimension constants αn. 8
2.4. Notation 9
3. Symbolic dynamics, path sets and p-adic path set fractals 9
3.1. Symbolic dynamics, graphs and ﬁnite automata 9
3.2. p-Adic path sets, soﬁc shifts and p-adic path set fractals 10
3.3. p-Adic symbolic dynamics and graph directed constructions 11
3.4. Interleaving operation on path sets 11

Date: December 5, 2015.
The ﬁrst author received support from an NSF Graduate Research Fellowship. The third author received
support from NSF grants DMS-1101373 and DMS-1401224.

1

2 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

4. The inﬁnite family Pk = 2 · 3k + 1 = (20k−11)3 14
4.1. The Family Pk = (20k−11)3 = 2 · 3k + 1: Path set structure. 14
4.2. The Family Pk = (20k−11)3 = 2 · 3k + 1: Hausdorff dimension. 22
4.3. Hausdorff dimension bounds for C(1, Pk1, ..., Pkn ) 23
5. The inﬁnite family Qk = 32k − 3k + 1 = (2k0k−11)3 24
5.1. The Family Qk = (2k0k−11)3 = 32k − 3k + 1: Path set structure 24
5.2. The family Qk = (2k0k−11)3 = 32k − 3k + 1: Hausdorff dimension 27
6. Bounds on Hausdorff dimensions by numbers of ternary digits 27
6.1. Upper Bound on Γ via n-digit constants αn: Proof of Theorem 2.5. 27
6.2. Exact bound for α2 28
7. Block number and intermittency of ternary expansions 29
8. Appendix A: Review of results for families Lk = (1k)3 and Nk = (10k−11)3. 30
9. Appendix B: Relation of families Pk = (20k−11)3 and Lk+1 = (1k+1)3 31
References 32

1. INTRODUCTION

Let the 3-adic Cantor set Σ3 := Σ3,¯2 be the subset of all 3-adic integers whose 3-
adic expansions consist of digits 0 and 1 only. This set is a well-known fractal having
Hausdorff dimension dimH (Σ3) = log3 2 ≈ 0.630929. By a multiplicative translate of
such a Cantor set we mean a multiplicatively rescaled set rΣ3 = {rx : x ∈ Σ3}, where we
restrict to r = p
q ∈ Q× being a rational number that is 3-integral, meaning that r ∈ Z3, or
equivalently ord3(r) ≥ 0. For example the multiplicative translate Σ3,¯1 = 2Σ3,¯2, which
allows only 3-adic digits 0 and 2, has the symbol structure of its digits matching that of
ternary expansions of the usual middle-third Cantor set on [0, 1].
This paper considers sets given as ﬁnite intersections of such multiplicative translates:

C(r1, r2, · · · , rN ) :=
 N⋂

i=1
 1
ri Σ3. (1.1)

These sets are fractals and this paper considers the problems of determining their internal
structure and of obtaining bounds on their Hausdorff dimension. The dependence of the
Hausdorff dimension of the sets C(r1, . . . , rn) on the parameters (r1, r2, . . . , rn) turns out
to be complicated and fascinating.
In Part I [3], two of the authors presented a method for exactly computing the Hausdorff
dimension of individual sets C(r1, . . . , rn). This method is suited for computer experimen-
tation. The method is based on the fact all such sets have a special property: the 3-adic
expansions of members of such a set are characterizable by the set of all inﬁnite paths in
a ﬁxed labeled directed graph (ﬁnite automaton) that emanate from a ﬁxed initial vertex,
where the edge labels are 3-adic digits. We term sets of this kind, characterized by a ﬁnite
automaton, 3-adic path set fractals. Two of the authors studied the p-adic version of this
concept in [2], and showed their Hausdorff dimensions are explicitly computable in terms
of properties of the associated ﬁnite automaton. p-adic path set fractals in turn are geomet-
ric realizations of objects in symbolic dynamics called path sets. Forgetting the geometric
data associated to a p-adic path set fractal Y , that is, thinking of the 3-adic digits as an
alphabet with no additional structure, recovers an underlying path set X which is the set of
all inﬁnite strings of digits from {0, 1, . . . , p−1} corresponding to elements of Y . The path
set underlying the 3-adic path set fractal C(r1, . . . , rn) is denoted X(r1, . . . , rn), and will

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES3

play a role in the results of this paper. The papers [2], [3] gave between them algorithms
to effectively compute X(r1, . . . , rn) when given (r1, r2, ..., rn). Section 3 reviews basic
results on path sets and p-adic path set fractals; a general theory of path sets was previously
developed by two of the authors in [1].
This paper is concerned with the case C(1, M ) for M a positive integer. The Hausdorff
dimension dimH (C(1, M )) has a clear dependence on certain simple properties of the
ternary expansion (M )3 of M . For example Part I observed:

(i) dimH (C(1, M )) = 0 whenever the last ternary digit of (M )3 is a 2, i.e. M ≡
2 (mod 3).
(ii) dimH (C(1, 3M )) = dimH (C(1, M )). In consequence, all trailing zeros in the
base 3 expansion of M may be cancelled off without changing the Hausdorff di-
mension.

However the dependence on M seems anything but simple when examined more closely.
It appears that arithmetic properties of M inﬂuence both the structure of the underlying
automata and the Hausdorff dimension in extremely complex ways. Part I treated in detail
two inﬁnite families of M whose ternary expansion (M )3 had a particularly simple form,
where an exact answer for the Hausdorff dimension could be obtained.

(1) M = Lk = (1k)3, that is Lk = 1
2 (3k − 1). It obtained a Hausdorff dimension
formula for each k ≥ 1 and deduced that dimH (C(1, Lk)) → 0 as n → ∞ ([3,
Theorem 5.2]).
(2) M = Nk = (10k−11)3, that is Nk = 3k + 1. It showed for each k ≥ 1 that
dimH (C(1, Nk)) = log3 φ ≈ 0.438018, where φ = 1+√5
2 ([3, Theorem 5.5]).

The automata associated to the second of these families displayed considerable complexity.
The automaton associated to Nk had a number of states growing exponentially with k and
was strongly connected; it is remarkable that its Perron eigenvalue could be computed
exactly. Salient facts on these families are collected in Appendix A (Section 8) for easy
reference.
This paper continues the study of the sets C(1, M ) for various integers M ≥ 1. We
obtain results for two new inﬁnite families of M having ternary expansions (M )3 of a reg-
ular form, Pk = 2 · 3k + 1 = (20k−11)3 and Qk = 32k − 3k + 1 = (2k0k−11)3; they are
stated in Section 2. When compared to the families treated in Part I, these families reveal
additional complexity in the structure of the associated automata and the behavior of the
Hausdorff dimension. In particular the automata associated to one of these families are
not strongly connected; they are reducible and have arbitrarily large numbers of strongly
connected components. We bound the Hausdorff dimension of such C(1, M ) through esti-
mation of the Perron eigenvalue of the adjacency matrix of these automata. To estimate the
Hausdorff dimension of one family, we make use of an operation on path sets termed inter-
leaving, that we introduce in Section 3.4. The structure of the automata was ﬁrst guessed
from computer experiments and then proved. In addition to studying these two families the
paper presents further results from computer experiments to test the relation of Hausdorff
dimension to particular patterns in the ternary expansion of M .
The original motivation for studying questions of this kind arose from a problem of
Erd˝os [8]. This problem was generalized to a question over the 3-adic integers by the
third author ([12]), who proposed a weaker version of the Erd˝os problem, the Exceptional
set conjecture, explained below, which asserts that a certain set has Hausdorff dimension
0. The results of this paper yield new information about the Exceptional set conjecture
without resolving it, see Section 1.2.

4 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

1.1. Exceptional set conjecture and nesting constants. Erd˝os [8] conjectured that for
every n ≥ 9, the ternary expansion of 2n does not omit the digit 2. A weak version of this
conjecture asserts that there are only ﬁnitely many n such that the ternary expansion of 2n

does not omit the digit 2. Both versions of this conjecture are open and appear difﬁcult.
In [12] the third author proposed a 3-adic generalization of this problem, as follows. Let
Z3 denote the 3-adic integers, and let a 3-adic integer α have 3-adic expansion

(α)3 := a0 + a1 · 3 + a2 · 32 + · · · , with all ai ∈ {0, 1, 2}.

It introduced the following notion.

Deﬁnition 1.1. The 3-adic exceptional set E(Z3) is given by

E(Z3) := {λ ∈ Z3 : for inﬁnitely many n ≥ 0 the expansion (2nλ)3 omits the digit 2}.

This deﬁnition is less stringent than the Erd˝os problem in allowing variation of the new
parameter λ. The weak version of Erd˝os's conjecture above is equivalent to the assertion
that 1 /∈ E(Z3).
That paper proposed the following conjecture [12, Conjecture 1.7].

Conjecture 1.2. (Exceptional Set Conjecture) The 3-adic exceptional set E(Z3) has Haus-
dorff dimension zero, i.e. dimH (E(Z3)) = 0. (1.2)

Clearly 0 ∈ E(Z3), and our state of ignorance is such that we do not know whether
E(Z3) = {0} or not. In [12] the Exceptional Set Conjecture was approached by introduc-
ing the sets

E (k)(Z3) := {λ ∈ Z3 : at least k values of (2nλ)3 omit the digit 2}, (1.3)

which yield the containment relation

E(Z3) ⊆
 ∞⋂

k=1 E (k)(Z3). (1.4)

That paper obtained the upper bound

dimH (E(Z3)) ≤ dimH (E (2)(Z3)) ≤ 1
2 .

The sets E (k)(Z3) form a nested family

Σ3,¯2 = E (1)(Z3) ⊇ E (2)(Z3) ⊇ E (3)(Z3) ⊇ · · · ,

and are themselves expressed in terms of intersection sets (1.1) as

E (k)(Z3) = ⋃

0≤m1<...<mk C(2m1, . . . , 2mk ). (1.5)

This connection motivated the study made in [3] of the more general sets C(M1, ..., Mk).

Deﬁnition 1.3. The (dyadic) nesting constant Γ is given by

Γ := lim
k→∞ dimH (E (k)(Z3)). (1.6)

The containment relation (1.4) implies that the nesting constant upper bounds to the
Hausdorff dimension of the exceptional set,

dimH (E(Z3)) ≤ Γ. (1.7)

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES5

The third author raised the question in [12] whether Γ = 0, which if true would imply the
Exceptional Set Conjecture. This question is currently unanswered.
Part I [3, Section 1.2] approached the problem of obtaining improved upper bounds for
Γ by introducing a relaxed upper bound Γ⋆, called there the generalized nesting constant,
obtained by replacing C(2m1, . . . , 2mk ) with C(1, M1, ..., Mk−1) in the deﬁnition above.
That paper showed Γ ≤ Γ⋆ ≤ 1
2 , and also established the lower bound

Γ⋆ ≥ 1
2 log3 φ ≈ 0.21909.

It follows that one cannot resolve whether Γ = 0 or not using the relaxation Γ⋆.

1.2. Statistics of ternary digits and n-digit Hausdorff dimension constant. A focus
of this work was to shed light on the Exceptional set conjecture, by gathering evidence
whether there might exist simple statistics of the ternary expansion (M )3 of a single integer
M which will predict that the Hausdorff dimension dimH (C(1, M )) must go to 0 as the
value of the statistic goes to inﬁnity.
In this paper we resolve this question for the statistic d3(M ) that counts the number of
nonzero digits in the ternary expansion of the positive integer (M )3. This value coincides
with the number of nonzero digits in the 3-adic expansion of M ; note that a 3-adic integer
α has a ﬁnite number of non-zero digits if and only if it is a non-negative integer α ∈ N.

Deﬁnition 1.4. The n-digit Hausdorff dimension constant αn is given by

αn := sup
M≥1
{dimH (C(1, M )) : The expansion (M )3 has at least n nonzero ternary digits}.

By deﬁnition the αn form a nonincreasing sequence of nonnegative numbers, so that
the limit Γ⋆⋆ := lim
n→∞ αn

exists. Known results in number theory, detailed in Section 6, imply that the number of
nonzero ternary digits of 2n diverges as n goes to inﬁnity. Thus, we obtain an upper bound
on the dyadic nesting constant

Γ ≤ Γ⋆⋆ = lim
n→∞ αn = inf
n αn. (1.8)

One of the inﬁnite families studied in this paper has d3(Mk) → ∞ as k → ∞ and using it
we show
 Γ⋆⋆ = inf
n αn = log3
 ( 1 + √
5
2
 )
 ≈ 0.438018. (1.9)

In particular by (1.7) we obtain an improved upper bound for the Hausdorff dimension of
the exceptional set

dimH (E(Z3)) ≤ Γ ≤ Γ⋆⋆ ≤ log3
 ( 1 + √
5
2
 )
 ≈ 0.438018. (1.10)

In the opposite direction (1.9) establishes that the statistic d3(M ) does not have the prop-
erty that the Hausdorff dimension must go to 0 as the statistic d3(M ) → ∞.
The ﬁnal section of the paper empirically studies the Hausdorff dimension of C(1, M )
with respect to two other simple statistics of the ternary expansion (M )3: the block number
b3(M ) and intermittency s3(M ); these satisfy b3(M ) ≤ s3(M ). These are deﬁned in
Section 7.

6 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

1.3. Roadmap. Section 2 states the main results. Section 3 reviews properties of p-adic
path sets and their symbolic dynamics, drawing on [1] and [2]. Intersections of multi-
plicative translates of 3-adic Cantor sets are a special case of these constructions. Section
3.4 introduces an interleaving operation on path sets and analyzes its effect on Hausdorff
dimension. Section 4 studies the sets C(1, Pk) for the inﬁnite family Pk, analyzes the
structure of their associated automata, and proves Theorems 2.1-2.2, and additional re-
sults. Section 5 studies the structure of C(1, Qk) for the inﬁnite family Qk, and proves
Theorems 2.3-2.4. Section 6 deals with results on the quantities αn and proves Theo-
rems 2.5-2.6. Section 7 presents empirical results on Hausdorff dimensions of C(1, M )
for M having speciﬁed statistics of their ternary expansions (M )3.
Appendix A (Section 8) describes results for two inﬁnite families C(1, Lk) and C(1, Nk)
treated in Part I [3]. Appendix B (Section 9) relates Hausdorff dimensions of C(1, Pk) to
those of C(1, Lk+1).

Acknowledgments. We thank Yusheng Luo for an important observation on the structure
of the automata for the sets Pk, incorporated in Deﬁnition 4.3 and Proposition 4.4. W.
A. thanks the University of Michigan, where much of this work was carried out. W. A.
and A. B. would also like to thank Ridgeview Classical Schools, which facilitated their
collaboration. W.A. was partially supported by an NSF graduate fellowship. J. L. was
supported by NSF grants DMS-1101373 and DMS-1401224. Some work of J.L. on the
paper was done at ICERM, where he received support from the Clay Foundation as a Clay
Senior Scholar. He thanks ICERM for support and good working conditions.

2. RESULTS

The main results of this paper consist of determination of presentations of the 3-adic
path sets X(1, Pk) and X(1, Qk) associated to members of two inﬁnite families C(1, Pk)
and C(1, Qk) given below, with estimates of their Hausdorff dimensions, along with exper-
imental results for dimH (C(1, M )) for certain other M presented in Section 7.

2.1. The inﬁnite family Pk = (20k−11)3. We study the path set structure of families of
integers having few nonzero ternary digits. The only inﬁnite families of numbers having
exactly two nonzero ternary digits and dimH (C(1, N )) > 0 are Nk = 3k + 1 = (10k−11)3
and Pk = (20k−11)3 = 2 · 3k + 1. The family Nk was studied in Part I and here we study
the family Pk.
We directly compute the Hausdorff dimensions of the ﬁrst few sets C(1, Pk) using the
algorithms of Part I to be the following.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES7

Path Set Pk Vertices Perron eigenvalue Hausdorff dim
C(1, P1) 7 4 1.618033 0.438018
C(1, P2) 19 8 1.465571 0.347934
C(1, P3) 55 16 1.380278 0.293358
C(1, P4) 163 32 1.324718 0.255960
C(1, P5) 487 64 1.370957 0.287191
C(1, P6) 1459 128 1.388728 0.298913
C(1, P7) 4375 256 1.392067 0.301010
C(1, P8) 13123 512 1.387961 0.298408

TABLE 2.1. Hausdorff dimension of C(1, Pk) (to six decimal places)

The ﬁrst thing to observe from this data is the non-monotonic behavior of the Hausdorff
dimension as a function of k; the second observation is the possibility that the dimensions
are bounded away from zero. Our results below explain both these features. We also
observe that dimH (C(1, Pk)) = dimH (C(1, Lk+1)) for 1 ≤ k ≤ 4 but equality does
not hold for k = 5. In an Appendix B (Section 9) we show that dimH (C(1, Pk)) ≥
dimH (C(1, Lk+1)) holds in general.
Our ﬁrst result determines properties of a presentation of the path set X(1, Pk). The
resulting directed graphs are shown to be reducible, having a complicated structure with
nested strongly connected components.

Theorem 2.1. (Path set presentation for family Pk)
(1) For Pk = 2 · 3k + 1 = (20k−11)3, the path set X(1, Pk) underlying C(1, Pk) has a
path set presentation (Gk, v0) that has exactly 2k+1 vertices.
(2) The graph Gk is a nested sequence of 1 + ⌊k/2⌋ distinct strongly connected compo-
nents.
(3) The underlying graph G = Gk for Gk has an automorphism of order 2 and is a
connected double cover of its quotient graph Hk.

The structure of Gk is that of a “Matryoshka doll" with a single set of nested components
at each level. The non-monotonicity of the Hausdorff dimension as a function of k can be
related to the existence of multiple strongly connected components in the graphs Gk. The
non-monotonicity occurs because of a switch in which strongly connected component has
the largest topological entropy. We discuss this issue further in Section 4.2, see Remark
4.6.
Regarding the behavior of the Hausdorff dimension as k → ∞, we establish the follow-
ing result.

Theorem 2.2. (Hausdorff dimension bounds for family Pk = 2 · 3k + 1)
(1) The Hausdorff dimension of C(1, Pk) satisﬁes the asymptotic lower bound

lim inf
k→∞ dimH (C(1, Pk)) ≥ 1
8 log3(2).

(2) Furthermore, for all k ≥ 1,

dimH (C(1, Pk)) ≥ 1
13 log3(2).

The lower bounds in Theorem 2.2 are obtained by further inspection of the graph asso-
ciated to C(1, Pk). We also have an upper bound

dimH (C(1, Pk)) ≤ log3 φ.

8 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

which follows from Theorem 6.2 below.
In Section 4.3 we obtain additional results on intersection of sets in the inﬁnite family
Pk above. We show that the Hausdorff dimensions of arbitrarily large intersections are
always positive. However this is no longer true if we allow intersections of sets from the
inﬁnite family Pk with those of the inﬁnite family Nk = (10k−11)3 treated in [3, Sect. 4]
and reviewed in Appendix A (Section 8), which also consists of numbers having exactly
two nonzero ternary digits. For example, it is easy to show that for each k ≥ 1,

C(1, Nk, Pk) = {0},

so that dimH (C(1, Nk, Pk)) = 0.

2.2. The inﬁnite family Qk = (2k0k−11)3. We next study an inﬁnite family of integers
whose number of nonzero ternary digits grows without bound: Qk = (2k0k−11)3 =
32k − 3k + 1. The example Q2 having a large Hausdorff dimension was found by computer
search, and led to study of this family.

Theorem 2.3. (Path set presentation for family Qk)
(1) For Qk = 32k − 3k + 1 = (2k0k−11)3, the path set X(1, Qk) underlying C(1, Qk)
has a path set presentation (Gk, v0) that has exactly 4k vertices and 6 · 4k−1 edges.
(2) The underlying graph Gk is strongly connected.

Though the number of nonzero ternary digits of Qk grows without bound, the Hausdorff
dimension of C(1, Qk) is constant independent of k.

Theorem 2.4. (Hausdorff dimensions for family Qk = 32k − 3k + 1) For all k ≥ 2 the
Hausdorff dimension of C(1, Qk) satisﬁes

dimH (C(1, Qk)) = log3 φ ≈ 0.438018,

where φ = 1+√5
2 .

This result is established by showing that the path set X(1, Qk) is given by an interleav-
ing construction from the path set X(1, Q1), that is X(1, Qk) = X(1, 7)
(∗k), as deﬁned in
Section 3.4.

2.3. The n-digit Hausdorff dimension constants αn. It is a known fact that the number
of nonzero ternary digits in (2n)3 goes to inﬁnity as n → ∞, i.e. for each k ≥ 2 there are
only ﬁnitely many n with (2n)3 having at most k nonzero ternary digits. Using this fact
we easily deduce the following consequence.

Theorem 2.5. The nesting constant Γ satisﬁes

Γ ≤ lim
n→∞ αn. (2.1)

In particular dimH (E(Z3)) ≤ Γ∗∗ = lim
n→∞ αn.

It follows that individual values αn give upper bounds on Γ.

Theorem 2.6. We have for all k ≥ 2 that

αk = log3 φ ≈ 0.438018,

where φ = 1+√5
2 is the golden ratio. This value is attained by C(1, Qk) for

Qk := (2k0k−11)3.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES9

In particular this result yields an improved upper bound on the nesting constant

Γ ≤ log3 φ,

and on the Hausdorff dimension of the Exceptional set. It also gives

Γ⋆⋆ = log3 φ ≈ 0.438018.

We prove Theorem 2.6 in Section 6.2.
Using the known bound for the generalized dyadic nesting constant Γ⋆ ≤ α2 established
in Part I [3, (1.16)] we obtain the following corollary.

Corollary 2.7. We have Γ∗ ≤ log3 φ ≈ 0.438018,

in which φ = 1+√5
2 is the golden ratio.

2.4. Notation. The notation (m)3 means either the base 3 expansion of the positive inte-
ger m, or else the 3-adic expansion of (m)3. In the 3-adic case this expansion is to be read
right to left, so that it is compatible with the ternary expansion. That is, α = ∑∞
j=0 aj3j

will be written (· · · a2a1a0)3.

3. SYMBOLIC DYNAMICS, PATH SETS AND p-ADIC PATH SET FRACTALS

3.1. Symbolic dynamics, graphs and ﬁnite automata. The constructions of this paper
are based on the fact that the points in intersections of multiplicative translates of 3-adic
Cantor sets have 3-adic expansions that are describable in terms of allowable paths gener-
ated by ﬁnite directed labeled graphs. We use symbolic dynamics on certain closed subsets
of the one-sided shift space Σ = A
N with ﬁxed symbol alphabet A, which for our ap-
plication will be specialized to A = {0, 1, 2}. A basic reference for directed graphs and
symbolic dynamics, which we follow, is Lind and Marcus [14].
By a graph we mean a ﬁnite directed graph, allowing loops and multiple edges. A
labeled graph is a graph assigning labels to each directed edge; these labels are drawn from
a ﬁnite symbol alphabet. A labeled directed graph can be interpreted as a ﬁnite automaton
in the sense of automata theory. In our applications to 3-adic digit sets, the labels are drawn
from the alphabet A = {0, 1, 2}. In a directed graph, a vertex is a source if all directed
edges touching that vertex are outgoing; it is a sink if all directed edges touching that edge
are incoming. A vertex is essential if it is neither a source nor a sink; and is called stranded
otherwise. A graph is essential if all of its vertices are essential. A graph G is strongly
connected if for each two vertices i, j there is a directed path from i to j. We let SC(G)
denote the set of strongly connected component subgraphs of G.
We use some basic facts from the Perron-Frobenius theory of nonnegative matrices.
The Perron eigenvalue ([14, Deﬁnition 4.4.2]) of a nonnegative real matrix A ̸= 0 is the
largest real eigenvalue β ≥ 0 of A. A nonnegative matrix is irreducible if for each row
and column (i, j) some power A
m has (i, j)-th entry nonzero. A nonnegative matrix A is
primitive if some power A
k for an integer k ≥ 1 has all entries positive; primitivity implies
irreducibility but not vice versa. The Perron-Frobenius Theorem [14, Theorem 4.2.3] for
an irreducible nonnegative matrix A states that:

(1) The Perron eigenvalue β is geometrically and algebraically simple, and has an
everywhere positive eigenvector v.
(2) All other eigenvalues µ have |µ| ≤ β, so that β = σ(A), the spectral radius of A.
(3) Any other everywhere positive eigenvector must be a positive multiple of v.

10 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

For a general nonnegative real matrix A ̸= 0, the Perron eigenvalue need not be simple,
but it still equals the spectral radius σ(A) and it has at least one everywhere nonnegative
eigenvector.
We apply this theory to adjacency matrices of graphs. A (vertex-vertex) adjacency
matrix A = AG of the directed graph G has entry aij counting the number of directed
edges from vertex i to vertex j. The adjacency matrix is irreducible if and only if the
associated graph is strongly connected, and we also call the graph irreducible in this case.
Here primitivity of the adjacency matrix of a directed graph G is equivalent to the graph
being strongly connected and aperiodic, i. e. the greatest common divisor of its (directed)
cycle lengths is 1. For an adjacency matrix of a graph containing at least one directed
cycle, its Perron eigenvalue is necessarily a real algebraic integer β ≥ 1 (see Lind [13] for
a characterization of these numbers).

3.2. p-Adic path sets, soﬁc shifts and p-adic path set fractals. Our basic objects are
special cases of the following deﬁnition. A pointed graph is a pair (G, v) consisting of a
directed labeled graph G = (G, E) and a marked vertex v of G. Here G is a (directed)
graph and E is an assignment of labels (e, ℓ) = (v1, v2, ℓ) to the edges of G, where every
edge gets a single label, and no two triples are the same (but multiple edges and loops are
permitted otherwise).

Deﬁnition 3.1. Given a pointed graph (G, v) its associated path set P = XG(v) ⊂ A
N

is the set of all inﬁnite one-sided symbol sequences (x0, x1, x2, ...) ∈ A
N, giving the
successive labels of all one-sided inﬁnite walks in G issuing from the distinguished vertex
v. Many different (G, v) may give the same path set P, and we call any such (G, v) a
presentation of P.

An important class of presentations have the following extra property. We say that a di-
rected labeled graph G = (G, v) is right-resolving if for each vertex of G all directed edges
outward have distinct labels. (In automata theory G is called a deterministic automaton.)
One can show that every path set has a right-resolving presentation.
Note that the labeled graph G without a marked vertex determines a one-sided soﬁc shift
in the sense of symbolic dynamics, as deﬁned in [1]. This soﬁc shift comprises the set
union of the path sets at all vertices of G. Path sets are closed sets in the shift topology, but
are in general non-invariant under the one-sided shift operator. Those path sets P that are
invariant are exactly the one-sided soﬁc shifts [1, Theorem 1.4].
We study the path set concept in symbolic dynamics in [1]. The collection of path sets
P = XG(v) in a given alphabet is closed under ﬁnite union and intersection ([1, Theorem
1.2]). The symbolic dynamics analogue of Hausdorff dimension is topological entropy.
The topological entropy of a path set Htop(P) is given by

Htop(P) := lim sup
n→∞ 1
n log Nn(P),

where Nn(P) counts the number of distinct blocks of symbols of lengh n appearing in
elements of P. The topological entropy is easy to compute given a right-resolving presen-
tation. By [1, Theorem 1.13], it is
 Htop(P) = log β (3.1)

where β is the Perron eigenvalue of the adjacency matrix A = AG of the underlying
directed graph G of G, e.g. the spectral radius of A.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES11

3.3. p-Adic symbolic dynamics and graph directed constructions. We now suppose
A = {0, 1, 2, ..., p − 1}. We can view the elements of a path set P on this alphabet
geometrically as describing the digits in the 3-adic expansion of a 3-adic integer. This is
done using a map φ : A
N → Zp from symbol sequences into Zp. We call the resulting
image set K = φ(P) a p-adic path set fractal. Such sets are studied in [2], where they
are related to graph-directed fractal constructions. The class of p-adic path set fractals
is closed under the Minkowski sum and p-adic addition and multiplication by rational
numbers r ∈ Q that lie in Zp ([2, Theorems 1.2-1.4]).
It is possible to compute the Hausdorff dimension of a p-adic path set fractal directly
from a suitable presentation of the underlying path set P = XG(v). We will use the
following result.

Proposition 3.2. Let p be a prime, and K a set of p-adic integers whose allowable p-adic
expansions are described by the symbolic dynamics of a p-adic path set XK on symbols
A = {0, 1, 2, · · · , p−1}. Let (G, v) be a presentation of this path set that is right-resolving.
(1) The map φp : Zp → [0, 1] taking α = ∑∞
k=0 akpk ∈ Zp to the real number with
base p expansion φp(α) := ∑∞
k=0 ak
pk+1 is a continuous map, and the image of K under this
map, K ′ := φp(K) ⊂ [0, 1], is a graph-directed fractal in the sense of Mauldin-Williams.
(2) The Hausdorff dimension of the p-adic path set fractal K is

dimH (K) = dimH (K ′) = logp β, (3.2)

where β is the spectral radius of the adjacency matrix A of G.

Proof. These results are proved in [2, Section 2]. □

In this paper we treat the case p = 3 with A = {0, 1, 2}. The 3-adic Cantor set is a
3-adic path set fractal, so these general properties above guarantee that the intersection of
a ﬁnite number of multiplicative translates of 3-adic Cantor sets will itself be a 3-adic path
set fractal K, generated from an underlying path set.
To do calculations with such sets we will need algorithms for converting presentations
of a given p-adic path set to presentations of new p-adic path sets derived by the operations
above. We refer the reader to [2] for the p-adic arithmetic operations, and to [1] for union
and intersection. A further useful operation called interleaving will be developed in the
next subsection; this operation is sometimes useful in computing Hausdorff dimension.

3.4. Interleaving operation on path sets. Let P = XG(v) ⊂ A
N be a path set, and let
n be a positive integer. In the paper [1] the ﬁrst and third authors studied a decimation
operation on path sets. Given j ≥ 0 and m ≥ 1, deﬁne the decimation map ψj,m : A
N →
A
N by ψj,m(a0a1a2 · · · ) := (aj aj+maj+2m · · · ).
The decimation operation extracts the digits of the path set in a speciﬁed inﬁnite arithmetic
progression of indices. We set

ψj,m(P) := {ψj,m(x) : x ∈ P}.

Here [1, Theorem 1.5] proved that if P is a path set, then for each ﬁxed (j, m) with j ≥
0, m ≥ 1 the sets ψj,m(P) are path sets.
Here we consider a kind of inverse operator to decimation, which we term interleaving.

Deﬁnition 3.3. Let n ≥ 1 be given. The n-interleaving of a closed set X ⊂ A
N (not
necessarily a path set) is

X (∗n) := {(xi)
∞
i=0 ∈ A
N : (xj, xj+n, xj+2n, · · · ) ∈ X for all 0 ≤ j ≤ n − 1}.

12 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

We will show that the interleaving P (∗n) is itself a path set, and that its topological
entropy is the same as that of P.

Proposition 3.4. (1) For any n ≥ 1 and any path set P, the n-interleaving set P (∗n) is a
path set.
(2) There is an algorithm taking n and a path set presentation G of P and giving a path
set presentation H of P (∗n). If G has k verticies and m edges, then H has kn verticies and
mkn−1 edges.

Proof. It sufﬁces to prove (2). Suppose P = XG(v0), and that the vertices of G are
v0, v1, . . . , vk−1, so that G has k vertices. Let lj be the label of vertex vj for each 0 ≤ j ≤
k − 1. If the lj do not all have the same number of digits, append 0′s to the left of labels
as necessary to ensure that the labels l0, . . . , lj are distinct and have the same number of
digits.
The vertex set of H will be V = {vi1,i2,...,in |0 ≤ ij ≤ k − 1 for all j}, so that H will
have kn vertices. The vertex vi1,i2,...,in will have label l = li1 ⋆ li2 ⋆ · · · ⋆ lin , that is, the
concatenation of the labels of vi1 , vi2 , . . . , vin . Since the labels lj are all distinct and have
the same number of digits, the vertex labels in H as deﬁned will also be distinct.
Now for each edge labeled a from vi to vj in G, construct an edge labeled a from
vi1,i2,...,in−1,i to vj,i1,i2,...,in−1 for all 0 ≤ i1, i2, . . . , in−1 ≤ k − 1. Thus, for each
edge of G, H will have kn−1 corresponding edges, so that if G has m edges, then H has
mkn−1 edges. H is evidently right-resolving or strongly connected if G is right-resolving
or strongly connected, respectively. For simplicity, we will assume from here that G is
right-resolving. We can do this since if G is not right-resolving, we can perform the right-
resolving construction of [1, Section 3] to obtain a right-resolving presentation of P, and
proceed with this presentation in place of G.
We claim that P (∗n) = XH(v0,0,...,0). First we will show that P n ⊆ XH(v0,0,...,0).
Suppose (xt)
∞
t=0 ∈ P n. Then there must be elements

(x0,t)
∞
t=0, (x1,t)
∞
t=0, . . . , (xn−1,t)
∞
t=0 ∈ P

such that xj,t = xnt+j for all 0 ≤ j ≤ n − 1 and 0 ≤ t < ∞. Since G is right-resolving,
each of these elements of P corresponds to a unique inﬁnite vertex path v0, vij,0 , vij,1 , . . .
in G. We can traverse an initial path in the pointed graph H(v0,0,0,...,0) with labels
x0, x1, . . . , xn−1, since there are edges with each of these labels emanating from v0 in G.
This path takes us to the vertex vin−1,0,in−2,0,...,i0,0 . Since there is a vertex labeled xn+j
emenating fom vertex vij,0 and going to vij,1 for all 0 ≤ j ≤ n − 1, we can extend our path
to a path labeled x0, x1, . . . , x2n−1 beginning at v0,0,...,0 and ending at vin−1,1,in−2,1,...,i0,1 .
Inductively, assume we have constructed a path with labels x0, x1, . . . , xrn−1 in H
originating at v0,0,...,0 and terminating at vin−1,r−1,in−2,r−1,...,i0,r−1 . Then since there is
an edge in G labeled xrn+j from vj,r−1 to vj,r, we can extend our path to a path labeled
x0, x1, . . . , x(r+1)n−1 terminating at vin−1,r ,in−2,r,...,i0,r . Thus, there is an inﬁnite path in
H originating at v0,0,...,0 with label (x0, x1, x2, . . .), so (xi)
∞
i=0 ∈ XH(v0,0,...,0), hence
P n ⊆ XH(v0,0,...,0).
Now to show XH(v0,0,...,0) ⊆ P n: Suppose (xi)
∞
i=0 is an element of XH(v0,0,...,0).
Then there is a vertex path v0,0,...,0; vi0,0,...,0; vi1,i0,0,...,0; . . . ; vin−1,in−2;...,i0 ; . . . in H
which can be traversed by edges labeled x0, x1, . . .. Notice that the ﬁrst coordinate of
a vertex must be the last coordinate of the vertex that follows after n − 1 steps. Since the
initial vertex is v0,0,...,0, we know that for each 0 ≤ j ≤ n − 1, there is an edge in G
labeled xj from v0 to vij . For any j < ∞, an edge in H labeled xj from vi1,i2,...,in to
vin+1,i1,i2,...,in−1 corresponds to an edge in G labeled xj fom vin to vin+1. Following our

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES13

path in H for n − 1 more steps gets us to a vertex whose last coordinate is in+1, so the edge
in H labeled xn+j emanating from this vertex corresponds to an edge in G labeled xn+j
emanating from vin+1 . Thus, for each 0 ≤ j ≤ n − 1, the labels (xj, xj+nxj+2n, . . .) are
the labels of an inﬁnite path in G originating at v0, so (xi)
∞
i=0 ∈ P n, hence XH(v0,0,...,0) ⊆
P n, as desired. □

Remark 3.5. (1) The presentation H of P (∗n) given in the proof above is right-resolving
(resp. strongly connected) if and only if the presentation G of P used in its construction is
right-resolving (resp. strongly connected).
(2) The operation of interleaving can be extended to interleave several different sets

I(X1, X2, ..., Xm) := {x ∈ A
N : ψj,m(x) ∈ Xi for 0 ≤ j ≤ m − 1.}

One can show that if each Xi = Pi is a path set then I(P1, P2, · · · , Pn) is a path set.

We next show that the n-interleaving operation P (∗n) has the nice feature that it pre-
serves topological entropy. Following [1] we deﬁne the path topological entropy Hp(P)
of a path set P by
 Hp(P) := lim sup
k→∞
 1
k log N I
k (P), (3.3)

where N I
k (P) is the number of initial blocks of length k from P, then [1, Theorem 1.11]
shows that Hp(P) = Htop(P), (3.4)

and that the lim sup's are obtained as limits.

Proposition 3.6. If P is a path set, then

Htop(P (∗n)) = Htop(P). (3.5)

Proof. Using (3.4), it sufﬁces to show that P and P (∗n) have the same path entropy. But
we can see directly from the deﬁnition of P (∗n) that N I
nk(P (∗n)) = (N I
k (P))
n, since an
initial path of length nk in P (∗n) corresponds to n (not necessarily distinct) initial paths of
length k in P. Thus,
 Hp(P (∗n)) = lim
k→∞ 1
k log N I
k (P (∗n))

= lim
k→∞ 1
nk log N I
nk(P (∗n))

= lim
k→∞ 1
nk log[(N I
k (P))
n]

= lim
k→∞ 1
k log N I
k (P) = Hp(P),

as desired. □

If A = {0, 1, . . . , p − 1}, let φ : AN → Zp be the map of Section 3.3, which maps the
path set P to the corresponding p-adic path set fractal K = φ(P). We have the following
Corollary.

Corollary 3.7. If P is a path set on the alphabet A = {0, 1, 2, . . . , p − 1}, then the p-adic
path set fractals K = φ(P) and K ′ = φ(P (∗n)) have the same Hausdorff dimension.

Proof. This follows immediately from (3.1), Proposition 3.6, and Proposition 3.2. □

14 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

Remark 3.8. (1) Corollary 3.7 is useful in computing Hausdorff dimensions of path sets
in our examples. Let P = X(1, 4) be the Golden Mean Shift, which is also the path set
underlying the 3-adic path set fractal C(1, 4). An element of C(1, Nk) = C(1, (10k−11)3)
is any 3-adic integer consisting of 0's and 1's and for which no 1 is followed k digits later
by another 1. Recognizing this property allows us to see for Nk = (10k−11)3 = 3k +1 that
the path set X(1, Nk) underlying C(1, Nk) is just P (∗k). Corollary 3.7 provides another
proof of a result in part I ([3, Theorem 5.5]) asserting that dimH (C(1, Nk)) = log3 φ, since
this now follows from the basic computation dimH (C(1, 4)) = log3 φ. One may compare
this argument to the proof given in [3, Theorem 5.5]. Let G be the presentation of C(1, 4)
given by Algorithm A of [3]. The algorithm of Proposition 3.4 applied to k and G and
Algorithm A of [3] give isomorphic graph presentations of C(1, Nk).
(2) In Section 5 below, we will prove Theorem 2.4, which states that

dimH (C(1, Qk)) = log3 φ,

by a similar argument.

4. THE INFINITE FAMILY Pk = 2 · 3k + 1 = (20k−11)3

We obtain a relatively complete description of the path set structure for the family Pk =
2 · 3k + 1 = (20k−11)3. As a preliminary we review results for the inﬁnite families Lk and
Nk studied in part I ([3, Section 4]).

4.1. The Family Pk = (20k−11)3 = 2·3k +1: Path set structure. We study the structure
of a path set presentation of the 3-adic expansions of elements in C(1, Pk). The following
example gives a path set presentation for P2 = 19.

Example 4.1. A path set presentation of the path set X(1, 19) associated to C(1, 19), with
19 = (201)3, is shown in Figure 4.1. The vertex labeled 0 is the marked initial vertex.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES15

0
 1

10

100

22

20
 21

2

0

1
 10

1

1
 1 0

0
 0

1
 0

FIGURE 4.1. Path set presentation of X(1, 19). The marked vertex is 0.

The graph in Figure 4.1 has adjacency matrix

A =
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
 1 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 1 0 1 0
0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 0
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
 ,

which has Perron eigenvalue β ≈ 1.465571, so

dimH (C(1, 19)) = log3 β ≈ 0.347934.

An important feature of the graph in Figure 4.1 is that it is reducible with two strongly
connected components, one component being the 2 nodes in the middle, and the other the
ring of 6 nodes around the outside. The (oriented) dependency graph of the strongly con-
nected components is a tree with 2 nodes. The Perron eigenvalue β of the graph above is

16 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

associated with the outer strongly connected component with 6 nodes. The inner compo-
nent has topological entropy 0.

We describe the path set presentation in general. The vertex labels of the presentation
will be described using the following deﬁnition.

Deﬁnition 4.1. Classify the labels of the vertices in the graph Gk as numbers m with
0 ≤ m ≤ 3k whose ﬁnite 3-adic expansions (read right to left) are of types (S1) and (S2)
given by:
(S1) The expansion (X)3, written with exactly k digits, omits the digit 1.
(S2) The 3-adic expansion of m contains a single digit 1, and has the form (X10j)3
for some 0 ≤ j ≤ k, with (X10j)3 written with exactly k digits, plus m = 3k =
(10k)3.

Note that an (S2) label has initial 3-adic digits consisting of a string of zeros, followed
by a 1.

Proposition 4.2. For Pk = 2 · 3k + 1 the path set X(1, Pk) associated to C(1, Pk) has a
presentation (Gk, v0) with the following properties.
(1) The vertices vm have labels m consisting of those 0 ≤ m ≤ 3k whose 3-adic
expansion (m)3 is one of the two types (S1) and (S2) above.
(2) The underlying directed graph G of Gk has exactly 2k+1 vertices.
(3) The reﬂection map R(m) = 3k − m which acts on vertex labels of the underlying
directed graph Gk is an automorphism of Gk. Given any path from (0)3 to vertex m, there
is a directed path from vertex (10k)3 to vertex 3k − m of the same length, visiting the set of
reﬂected vertices of the original path, and having all the edge labels reversed (exchanging
0 and 1).

Proof. The presentation found in this theorem will be that given by the construction of
Algorithm A in part I [3].
From the proof of Theorem 9.1 we know that a vertex with label m = 3k is reachable
by a directed path from vertex m = 0 and vice-versa.
We prove the proposition by showing, in order:
(G1) The vertices of G reachable from v0 have labels 0 ≤ m ≤ 3k which are a subset
of the labels (S1) and (S2).
(G2) The set of vertex labels m satisfying (S1) or (S2) are exchanged under the reﬂec-
tion map R(m) = 3k − m. The set of all possible m satisfying (S1), respectively
(S2), each have cardinality 2k.
(G3) Each path emanating from vertex m = 0 corresponds to a unique path emanating
from vertex m = 3k with the new path having reﬂected vertex labels and reversed
edge labels, and vice versa.
(G4) The set of all reachable vertices is invariant under the reﬂection map.
(G5) All vertices with labels of type (S1) are reachable.
(G6) The reﬂection map on vertices induces a graph automorphism of G of order 2 with
no ﬁxed points. Thus G is a double cover of the resulting quotient graph H.
To establish (G1) we proceed by induction on the length n of a shortest path to a given
vertex. The base case m = 0 is an (S1) label. Following a single 0 edge changes a vertex
label (Xs)3 (with s = 0, 1,) to (0X)3, which maps (S1) labels to (S1) labels and maps
(S2) labels to (S2) labels, except the case d = 1 is mapped to an (S1) label. Following a
single 1 edge with vertex label (Xs)3 (here s = 0, 2) maps labels having s = 0 to (2X)3,
which preserves the property of being an (S1) label or an (S2) label. For the case s = 2,

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES17

which must be an (S1) label, rewrite (Xs)3 = (Y 02j)3 for some j ≥ 1, which is converted
to (2Y 10j−1)3, which is an (S2) label. The extreme case (Xs) = (2k)2 is converted to
m = 3k, in (S2). This completes the induction step.
(G2) There are clearly 2k elements in (S1). The reﬂection map R acts on elements m
of (S1) with m > 0 by replacing each 0 by 2 and vice versa, except that the smallest 2 is
converted to a 1, and this is an element of (S2). The remaining element m = 0 exchanges
with m = 3k which is in (S2). Conversely elements of (S2) are mapped into elements of
(S1), for m < 3k an expression 10j is converted to 02j, and for m = 3k is sent to m = 0.
Since the reﬂection map is an involution, it is one to one, so the (S2) labels have the same
cardinality 2k as (S1) labels.
(G3) This assertion is proved by induction on the length of the path. It is vacuously true
at step 0. For the induction step we must check that the vertices m and 2k − m have the
same number of exit edges, and that the available exit edges have reversed labels in the
second case. We must also check that following an edge in the two cases leads to a pair of
reﬂected vertex labels m′ and 3k − m′. There are several cases.

Case (1) If m = (X20ℓ)3 for ℓ > 0 of type (S1), then 3k − m = ( ¯X10ℓ)3 is of type (S2).
Both allow 0, 1 exit edges. A 0 exit edge from m goes to m′ = (0X02ℓ−1)3, and a
1 exit edge for 3k − m goes to (2 ¯X10ℓ−1)3 = 3k − m′. A 1 exit edge from m goes
to m′′ = (2X20ℓ−1)3, and a 0 exit edge for 3k−m goes to (0 ¯X10ℓ−1) = 3k−m′′.
Case (2) If m = (X02ℓ)3 for ℓ > 0 of type (S1), then 3k − m = ( ¯X20ℓ−11)3 is of type
(S2). Here m allows only a 1 exit edge, while 3k − m allows only a 0 exit edge.
Under the allowed 1 exit edge m goes to m′ = (2X10ℓ−1)3 of type (S2). Under
the allowed 0 exit edge 3k − m goes to (0 ¯X20ℓ−1)3 = 3k − m′ of type (S1).

For the two further cases where m is of type (S2), reverse the above. This completes the
induction step.
(G4) By (G3) if a vertex labeled m is reachable from (0)3, then its reﬂected vertex
3k − m is reachable from vertex 3k. But vertex 3k is reachable from (0)3 so 3k − m is
reachable from (0)3 as well.
(G5) We may assume that the (S1) vertex m ̸= 0, so it has the form 0r02r10r2 · · · 2rj ,
in which all ri > 0 except possibly r0 and rj , and r0 + r1 + · · · + rj = k. Now
it may be realized following a directed path from (0)3 having successive edge labels
1rj , 0rj−1 , 1rj−2, · · · , 0r0. This path is legal, because all intermediate words in the path
have initial 3-adic digit 0 so both edges labeled 0 and 1 exit from that vertex. (The intial
word has k initial zeros, and each step can decrement the number of leading zeros by at
most 1).
(G6) One ﬁrst checks that each label m in (S1) ending in 0 corresponds under reﬂection
to a label 3k − m in (S2) ending in 0 and vice versa (since 3 divides m). Each label in
(S1) ending in 2 corresponds under reﬂection to a label in (S2) ending in 1; the (S1) label
permits only a single exit edge with label 1 and the corresponding (S2) label has a single
exit edge labeled 0. Thus at each vertex the reﬂection automorphism (at the level of vertex
labels) preserves the number of edges and reverses their edge labels. This establishes (G6).
Moreover the graph G is a double cover of the quotient graph H under the automorphism
R (which has no ﬁxed points). □

Our next object is to show that the underlying graph Gk of the path set X(1, Nk) has at
least ⌈ k+1
2 ⌉ nested connected components, a number which is unbounded as k → ∞. We
establish this using the following notion of depth to vertices of Gk.

18 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

Deﬁnition 4.3. (1) First we classify the labels of the vertices in graph Gk as being of types
(T1) and (T2) as follows:
(T1) The k-th 3-adic digit of m is 0 or 1, so m = (0X)3 or m = (1X)3, with X
containing k − 1 digits, but excluding the label m = 3k = (10k)3.
(T2) The k-th 3-adic digit of m is 2, i.e. m = (2X)3, as above, in addition including
the label m = 3k = (10k)3.
One may check that there are 2k elements in each set, and that the reﬂection operation
R(m) = 3k − m sends (T2) labels to (T1) labels and vice versa.

(2) The depth of a (T1) label is the number of blocks of consecutive 2's appearing in
its 3-adic expansion. The depth of a (T2) label m is the depth of its reﬂected label R(m),
which is of type (T1).

Thus m = 0 and m = 3k are assigned depth 0. Furthermore all the vertices in the path
of length 2k + 2 studied in the proof of Theorem 9.1 are assigned depth 0, and they are the
complete set of depth 0 vertices.
The following proposition will establish that this notion of depth stratiﬁes the strongly
connected components, by showing depth is nondecreasing along each directed edge.

Proposition 4.4. For Pk = 2 · 3k + 1 the path set X(1, Pk) has presentation (Gk, v0) with
the following properties.
(1) Each step along an edge in the graph Gk leaves the same or increases the depth of
a vertex.
(2) For 0 ≤ j ≤ ⌊k/2⌋ there are exactly 2( k+1
2j+1) vertices in Gk of depth exactly j.
(3) For each 0 ≤ j ≤ ⌊ k
2 ⌋, the vertices of depth j form a strongly connected component
of the underlying directed graph Gk. Thus, Gk has a sequence of 1 + ⌊k/2⌋ strongly
connected components, which are nested in a chain.

Proof. The presentation found in this theorem will be that given by the construction of
Algorithm A in part I [3]. Some of the notation below only makes sense for k > 3. We
will restrict to these cases, as the result follows for k = 1, 2, 3 by direct inspection. The
reversal operation exchanges type (T1) and type (T2) labels. For this to work the top 3-adic
digit (the k-th digit) must be used, because this is the only digit always reversed under the
reﬂection map or with 2 changed to 1; there is one exception, which is m = 0 and m = 3k,
where we assigned them to (T1) and (T2) directly. The key point is: a label m and its
reversal are always at the same level. For the two exceptions m = 0 and m = 3k this fact
had to be checked directly.
(1) It sufﬁces to check the effect of traversing a single edge in Gk. The assertion holds
for cases m = 0 and m = 3k because they both exit to level 0 vertices. By the proof
of (G3) in Proposition 4.2, if label m goes to m′ by edge labeled s, then 3k − m goes to
3k − m′ by an edge labeled ¯s. Now the depths of m and 3k − m are the same, as are those
of m′ and 3k − m′, so it sufﬁces to check the effect of following an edge from a vertex of
type (T1). We treat cases.
(i) Suppose m = (0X0)3 of type (T1) has depth d, thus X contains d blocks of
consecutive 2's. Following a 0 edge goes to m′ = (00X)3, also (T1) of depth d.
(ii) Suppose m = (0X0)3 of type (T1) has depth d, thus it has d blocks of consecutive
2's. Following a 1 edge goes to m′ = (20X)3, now (T2), of depth same as 3k−m′.
Now X = X ′20ℓ with ℓ ≥ 0 or X = 0ℓ. In the ﬁrst case 3k − m′ = (02 ¯X ′10ℓ)3
If X ′ = 0X ′′0, then it has d − 1 blocks of 2′s, but its reversal ¯X has d blocks.
If X ′ = 2X ′′0 then it has d − 1 blocks of 2′s, as does its reversal, but the 02 at

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES19

front creates another block. If X ′ = 0X ′2 then it has d blocks of 2's, as does its
reversal. Finally if X ′ = 2X ′2 then it has d blocks of 2's, its reversal has d − 1
blocks, but the 02 at front creats another blocks. In all cases the depth cannot
decrease.
(iii) Suppose m = (0X02ℓ)3 with ℓ > 0 of type (T1) has depth d. Now can only
follow a 1 edge, go to m′ = (20X10ℓ−1)3 is of type (T2). This has same depth as
3k − m′ = (02 ¯X20ℓ−1)3. Now X has d − 1 blocks of 2's. If it is of form 0X ′′0
then reversal increases number of blocks of 2's in it by 1, compensating exactly
for the lost 2 block at the right end of the label, so the depth is still d. If of form
2X ′′0 or 0X ′′2 then reversal leaves d − 1 blocks of 2's but get one extra block
from either 2 before or after, so the depth is still d. If of form 2X ′′2 then reversal
leaves d − 2 blocks of 2's but now gain two extra blocks from the 2 before and
after, so the depth is still d.

In all cases of a type (T1) vertex a step leaves depth the same or increases it by 1.
(2) Let k be ﬁxed. The result is true for j = 0 by the construction in Theorem 9.1, where
there are 2k + 2 = 2(
k+1
1 ) vertices of depth 0, and this component is strongly connected.
For j ≥ 1 it sufﬁces to count the number of labels of type (T1) at depth j and then
double it. For j ≥ 1 the number of labels of type (T 1) at depth j consist of all labels
of form (0k1 2ℓ10k22ℓ2 · · · 0kj 2ℓj 0kj+1 X)3 with ﬁnal block X = ∅ (set kj+2 = 0) or
X = (10kj+2−1) (the latter requires kj+2 ≥ 1). Since labels have length k the exponents
necessarily satisfy

k1 + · · · + kj+1 + kj+2 + ℓ1 + · · · + ℓj = k, ki, ℓi > 0 for 1 ≤ i ≤ j; kj+1, kj+2 ≥ 0.

There are ( k
2j) solutions of depth j type (T 1) with X not containing a 1; this follows since
there are k symblols in a label and we mark the ﬁnal elements of each 0ki and 2ki with
an asterisk for 1 ≤ i ≤ j to uniquely determine a depth j label with X = ∅. There are( k
2j+1) solutions of depth j type (T 1) with X containing a 1; here we add an additional
asterisk marking the 1, which unqiuely speciﬁes the label, so we have the number of ways
of inserting 2j + 1 asterisks. Thus the number of (T 1) labels of depth j is ( k+1
2j+1)
, and (2)
follows.
(3) First, we show that it is possible to reach a vertex of each depth 0 ≤ j ≤ ⌊k/2⌋.
Starting from m = 0 following paths with labels (10)
j for 1 ≤ j ≤ ⌊k/2⌋, one arrives at
vertices m2j := ((02)
j0k−2j)3, and m2j is a type (T1) label of depth j. These are legal
paths since all the intermediate vertex mj labels (for 1 ≤ j ≤ m − 1) have initial 3-adic
digit 0. We have produced a path with vertices of depth 0, 1, 2, ..., ⌊k/2⌋, which guarantees
the existence of at least one sequence of distinct strongly connected components of length
1 + ⌊k/2⌋ which are nested in a chain.
Next, we show that the subgraph of Gk consisting of those vertices of depth j is strongly
connected for each 0 ≤ j ≤ ⌊k/2⌋. At depth d = 0, beginning at the vertext labeled 0 and
traversing a path with label 1k+10k+1 gives a loop at the 0-vertex that passes through each
other vertex of depth 0, so the subgraph of depth 0 vertices is strongly connected.. Below,
we restrict attention to depths d ≥ 1, and some statements below only apply in those cases.
Recall also that we are restricting attention to k > 3, as smaller cases can be checked by
hand.
We need to show, ﬁrstly, that from any vertex it is always possible to traverse an edge
that leaves the depth unchanged. By the proof of (G3) in Proposition 4.2 and the discussion
in the ﬁrst paragraph of (1) above, it sufﬁces to verify this for vertices of type (T1). Let m
be the label of a vertex of depth d and type (T1). Then either m = (0X0)3, in which case

20 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

we may follow an edge labeled 0 to arrive at a vertex labeled (00X)3 that also has depth d,
or else m = (0X02l)3 for some l > 0. In the latter case, we may follow an edge labeled
1 to a vertex labeled (20X10l−1)3, and the discussion in (iii) above shows that this vertex
also has depth d. In any case, we can always traverse an edge that will leave the depth
unchanged.
Among depth d labels, the minimal such label is mmin = ((20)
d−12)3. In order to
show that the set of depth d vertices is a strongly connected subgraph of Gk, it sufﬁces
to show that it is always possible, beginning at any vertex of depth d, to traverse paths
both forwards to mmin and backwards to the same vertex (that is, contrary to the ordinary
direction that arrows are traversed; this will show that there is a path forwards from mmin
to the desired vertex). This will follow if we can show that:

(A) For any depth d vertex with non-minimal label m, it is always possible to follow a
path, staying at depth d, to another vertex with label m′ < m.
(B) For any depth d vertex, it is possible to follow edges backwards until we reach a
vertex where each block of 2's has length exactly 1.
(C) For any depth d vertex with a label where each block of 2's has length exactly 1, it is
possible to reach mmin by going backwards.

(A) Suppose now we are at a depth d vertex with label m of type (T1). Then either m
is of the form (0X0)3, or else m is of the form (0X02l)3 for some l > 0. If m = (0X0)3,
then we may traverse an edge labeled 0 to arrive at an edge labeled m′ = (0X)3 < m, and
m′ is also at depth d. Now suppose instead that m = (0X02l)3. Then we must traverse
next an edge labeled 1 to the vertex with label m′ = (20X10l−1)3 > m. By the argument
of (iii) above, this vertex also has depth d. From here, we may traverse l consecutive edges
labeled 0 to arrive at a vertex labeled m′′ = (20X)3, whose depth is also d. If the right-
most digit of X is not a 2, we may continue to traverse edges labeled 0 until we arrive at
a vertex m′′′ = (20Y )3 where the right-most digit of Y is a 2, and the length |Y | ≤ |X|,
or else at the vertex m(4) = (2)3 if X is the empty string. In the latter case, we are at
depth d = 1 and m(4) = (2)3 = mmin is already the minimal label. Suppose we are in
the former case, and we have arrived at m′′′ = (20Y )3. But for any l ≥ 1, we necessarily
have m′′′ = (20Y )3 ≤ (X02l)3 = m, with equality if and only if X = Y , l = 1,
and m = m′ = (20)
d−12 = mmin. Thus, in any case, we may always traverse a path,
remaining at depth d, to arrive at a vertex whose label is less than m.
What if our initial vertex is of type (T2)? Then, m is either of the form 10k, in which
case, we simply follow edges labeled 1 until we reach the vertex labeled 0, or we have
something of the form 2X, where X has k − 1 digits. In this case, if X terminates in 10l,
we can immediately follow a vertex 0, without dropping depths, to m′ of form (T 1), where
of course m′ < m. Otherwise, we have 2Y 20l, where we follow l + 1 edges of label 1;
the ﬁrst l bring us to 2Z2, and the (l + 1)st edge takes us to a (T2) vertex that terminates
in 10n, which is a case already covered.
This proves (A).
To see (B), we will devise an algorithm (call it Algorithm (B)).

(i) If we are at 2X10l then we follow a vertex labeled 1 backwards to vertex X02l+1.
(This does not drop depth, as a block of consecutive 2's necessarily transforms into
another block of consecutive 2's).
(ii) If we are at 0lX, where l > 1, or we are at 0lY 10n, where l > 0, we follow a vertex
labelled 0 to 0l−1X or 0l−1Y 10n+1.
(iii) If we are at 02X, and X omits the digit 1, we follow an edge labeled 0 back to 2X1.
Notice that this avoids dropping depth.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES21

(iv) If we are 2X, where X omits the digit 1, we follow an edge labeled 1 back to X0.

The crux is step (iii); following the notation of that step, we will then be at 2X1, with
no 0s after the 1. We then apply case (i), reaching X02. Any other 2's that appeared in the
block at the far left will be transformed into 0's on the far right by the application of step
(iv), while the other blocks will merely be shifted.
Thereby, by repeated application of this algorithm, all of the blocks will be transformed
into single-digit blocks after at most k iterations. This concludes (B). For an illustration at
depth 2, see the column labeled “Step (B)" in Table 4.1.
Finally, for (C), notice that, for the type of vertex we are interested in, repeated applica-
tion of Algorithm (B) simply "scrolls through" the label, with the blocks of 2's shifting left,
always preserving the same cyclic order, with the same gaps of 0's between them (unless
a 1 is present) between them. In the case of the illustration of Table 4.1, see the column
labeled “Step (C)-1" of that table.
So, for (C), apply Algorithm (B) until we are at 0lX2 where l > 1 (if this is strictly im-
possible, then simply "scroll" until we are at (02)
k/2, and at this depth, that is the minimal
vertex). Then, break the pattern and go to 0lX21. Then, continue to apply Algorithm (B)
until we return to a vertex where all of the blocks of 2's have length 1.
Essentially, we will generate a long block of 2's instead of the block of 0's we currently
have, which won't have such a large gap; see the column labele d “Step (C)-2" in Table 4.1.
One such procedure transforms a block of 0's of arbitrary length into a block of length
1. Repeat this procedure untill all of the blocks of 0's (except for 1) have length 1, and
then use Algorithm (B) until we reach the minimal vertex. This completes (3). Continuing
with our simple example, see the column labeled “Step (C)-3" in Table 4.1.
Step (B) Step (C)-1 Step (C)-2 Step (C)-3
22022022 0020002 0020002 0002020
20220220 0200020 0200021 0020200
02202200 2000201 2000210 0202000
22002201 0002002 0002022 2020001
20022002 0020020 0020220 0200002
00220020 0200200 0202200 2000021
02200200 2002001 2022001 0000202
22002001 0020002 0220002
20020002 2200021
00200020 2000202
0002020

TABLE 4.1. Example of algorithm for proof of Proposition 4.3(3).
 □

Remark 4.5. (1) Proposition 4.4 counts the number of vertices at each depth, giving a re-
cursion to compute them. Table 4.2 below gives values for 1 ≤ k ≤ 9.

22 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

Depth= 0 1 2 3 4
P1 = 7 4
P2 = 19 6 2
P3 = 55 8 8
P4 = 163 10 20 2
P5 = 487 12 40 12
P6 = 1459 14 70 42 2
P7 = 4375 16 112 112 16
P8 = 13123 18 168 252 72 2
P9 = 39367 20 240 504 240 20

TABLE 4.2. Number of vertices at given depth in graph Gk for X(1, Pk).

(2) Proposition 4.4 says that the graph X(1, Pk) has a “Matryoshka doll" structure of a
single set of nested strongly connected components, one at each depth 0 ≤ j ≤ ⌊k/2⌋.
(3) The proof of Proposition 4.4 exploits repeatedly the symmetry of the graph Gk
exhibited by the partitioning of vertices into types (T1) and (T2).

4.2. The Family Pk = (20k−11)3 = 2 · 3k + 1: Hausdorff dimension. Data on the
Hausdorff dimensions of the ﬁrst few of the sets C(1, Pk) were obtained by computer
calculation of the maximum eigenvalue of the adjacency matrix of the graph X(1, Pk)
and presented in Section 3.1. The data contained oscillations and other features which we
discuss in Remark 4.6 below.
We now lower bound the Hausdorff dimension of C(1, Pk) as k → ∞. Theorem 2.2
gives both an asymptotic limiting result and a lower bound because it may be that the
Hausdorff dimensions continue to oscillate for large k.

Proof of Theorem 2.2. Let a = ⌊ k
4 ⌋ and let b ∈ {0, 1, 2, 3} be congruent to k mod 4, so
that k = 4a + b. Let S ⊂ A
N = {0, 1, 2}N be given by

S = {(1100)
a0b((1x00)
a0b(1000)
a−11000b)
∞ ∈ A
N|x ∈ {0, 1} may vary}. (4.1)

What we will show is that S ⊂ X(1, Pk). Since elements of S, after the ﬁxed initial string
(1100)
a0b, consists of symbol sequences of length 2k − 1 with 2k − 1 − a ﬁxed digits and
a digits which may be either 0 or 1, it follows that

Htop(S) = a
2k − 1 log3(2) = ⌊ k
4 ⌋
2k − 1 log3(2).

The two inequalities of the theorem, that

lim inf
k→∞ dimH C(1, Pk) ≥ 1
8 log3(2),

and, for all k,
 dimH (C(1, Pk)) ≥ 1
13 log3(2),

then will follow immediately.
To prove that S ⊂ X(1, Pk), we will trace out paths on the graph presentation of
C(1, Pk) given by Algorithm A of [3] whose edge labels give the elements of S. First,
note that if we begin with an edge labeled 1 from the 0-vertex, we arrive at the vertex with
label 20k−1. This means that our next k − 1 vertices may be either 0 or 1 freely. Each
edge 0 appends a 0 to the front of the vertex label and removes the last digit, and each
edge 1 appends a 2 to the front of the vertex label and removes the last digit. From these

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES23

observations, we see that there is in fact a sequence of edges with label (1100)
a0b, and
having traversed these edges we arrive at a vertex labeled 0b(0022)
a. Call this vertex v.
We will now show that we may traverse a sequence of edges with label
(1x00)
a0b(1000)
a−11000b initiating at v for x = 0 and x = 1, and that such a path also
terminates at v. The result will follow. Now since the label of v ends in 2, the only out
edge is indeed labeled 1, and this takes us to a vertex labeled 20b(0022)
a−1010. The next
edge label x may then be either 0 of 1, terminating in a vertex labeled [2x]20b(0022)
a−101,
where [2x] is a digit given by the product of 2 and x. From this vertex we may traverse two
subsequent edges each labeled 0, and the target vertex is 00[2x]20b(0022)
a−1. It is easy to
see that we may repeat this process, traversing edges labeled (1x00) a times and ultimately
terminating at a vertex labeled (00[2x]2)
a0b. Traversing then b edges labeled 0 gets us to
the vertex labeled 0b(00[2x]2)
a. We may then traverse edges labeled (1000)
a−11000b to
arrive back at the vertex v labeled 0b(0022)
a. This completes the proof. □

Remark 4.6. We speculate on the behavior of the Hausdorff dimension function C(1, Pk)
as a function of k. We believe the following might be true.

(1) Fixing level j and varying k the topological entropy of the strongly connected
component at depth j stay at value 0 until k ≥ 2j − 2, then increas monotonically
to a maximum and then decrease monotonically thereafter.
(2) The “champion" depth j with maximal topological entropy is a nondecreasing
function of k.

Speculations (1) and (2) are suggested by analogy with the behavior of the number of
vertices at depth j as a function of k, given in Table 4.1, which have both these properties.

4.3. Hausdorff dimension bounds for C(1, Pk1, ..., Pkn ). The path set structures of the
members of the inﬁnite family Pk are compatible with each other, as a function of k, so
that the associated C(1, Pk1 , ..., Pkn ) all have positive Hausdorff dimension. We relate
these Hausdorff dimensions to those of the inﬁnite family Lk = (1k)3 = 1
2 (3k+1 − 1)
treated by the ﬁrst and third authors in [3] and reviewed in Appendix A (Section 8).

Theorem 4.7. For the family Pk = 2 · 3k + 1 = (20k−11)3, and 0 ≤ k1 < . . . <
kn, the graph G presenting the path set X(1, Pk1 , ..., Pkn ) underlying C(1, Pk1, . . . , Pkn )
contains a double covering of the underlying directed graph G(1kn +2)3 presenting the path
set X(1, Lkn+1) underlying C(1, Lkn+1). Consequently

dimH (C(1, Pk1 , . . . , Pkn )) ≥ dimH (C(1, Lkn+2)). (4.2)

Proof. The graphs under consideration are the graphs given by Algorithm A of [3]. Since
the underlying graph Gk of the path set presentation (Gk, v0) of the path set X(1, Pk)
contains a double covering of the underlying graph G
′
k+1 of the path set presentation of
X(1, Lk+1), and
 G(1k1 +2)3 ⋆ · · · ⋆ G(1kn +2)3 ∼= G(1kn +2)3 ,

the proposition follows from Theorem 9.1 in Appendix B.
Note that this directed graph covering is not a covering at the level of path sets, because
the path labels on the two graphs differ. □

Theorem 4.7 shows that there exist an arbitrarily large number of different values Mj,
each having a 2 in their ternary expansion, such that dimH (C(1, M1, M2, ..., Mn)) > 0.

24 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

5. THE INFINITE FAMILY Qk = 32k − 3k + 1 = (2k0k−11)3

Let Qk = 32k − 3k + 1 = (2k0k−11)3. We will prove Theorem 2.3, which describes
the structure of a graph presentation Gk of C(1, Qk). We then use this description to prove
Theorem 2.4, which computes the Hausdorff dimension of C(1, Qk).

5.1. The Family Qk = (2k0k−11)3 = 32k − 3k + 1: Path set structure. First, let us give
an example. The following example gives a path set presentation for Q2 = 73.

Example 5.1. A path set presentation of X(1, 73), with 73 = (2201)3, is shown in Fig-
ure 5.1. The vertex labeled 0 is the marked initial vertex.
The graph in Figure 5.1 has adjacency matrix

A =
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







 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
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







 ,

which has Perron eigenvalue β = 1+√
5
2 , so

dimH (C(1, 73)) = log3
 ( 1 + √
5
2
 )
 ≈ 0.438108.

We describe the path set presentation in general. Theorem 2.3 will follow easily from
the following result, which makes use of the concepts developed in Section 3.4.

Proposition 5.1. Let P = X(1, 7) be the path set underlying C(1, 7), and let Q =
X(1, Qk) be the path set underlying C(1, Qk). Then Q is the interleaved path set

Q = P (∗k). (5.1)

Proof. For convenience, we recall that P = XG(0) for the graph G in Figure 5.1. This is
the graph given by the Algorithm A of [3].
Let (H, v0) be the graph presentation of Q given by the same algorithm. An element
of P may begin with either a 0 or a 1, while an element (xi)
∞
i=0 of Q may begin with
any sequence x0x1 · · · xk−1 of 0's and 1's, since Qk terminates in 0k−11. Thus, the initial
k-blocks of Q are precisely the same as the initial k-blocks of the interleaved path set
P (∗k).
To show that Q = P (∗k) we just need to check that for each 0 ≤ j ≤ k − 1, the
admissible strings xj xj+kxj+2k · · · of j (modk) digits of elements of Q are precisely
the elements of P. We proceed by induction on j ≥ 0, the observation above complet-
ing the base case j = 0. Inductively, assume none of the digits xr for r ≡ l (modk)

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES25

0

220

1012
 1022
 1100
 110
 11

1

22

1020
 102
 1001

100
 10

221

1000
 0

1

1
 0

1
 1
 1
 0
 0

1
 0

0

0 11
 0

0
 010

1

1
 0

1

FIGURE 5.1 Path set presentation of X(1, 73). The marked vertex is 0.

with l < j can restrict the admissible values for the digits xj+nk for n ≥ 0. We mean

26 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

0
 12
 10

0

1

1

1 0

0

FIGURE 5.2. Path set presentation of X(1, 7). The marked vertex is 0.

here that whether xr = 0 or xr = 1 has no effect on the last digit of the vertex la-
bel in H arrived at from a path labeled x0x1 · · · xj+nk originating at v0. The base case,
j = 0, is satisﬁed trivially. Then we can without loss of generality assume xi = 0 for
all 0 ≤ i < j. For now, we will also assume that xr = 0 for all r ̸≡ j (modk).
This assumption is not as restrictive as it seems since, as we will show, the j (modk)
digits do not effect the available choices for digits of other modular classes. Now since
Qk = 2k0k−11, whether xj is 0 or 1 has no effect on the digits xj+1, xj+2, . . . , xj+k−1.
If xj = 0, then xj+k may also be either 0 or 1. If xj+mk is 0 for all m < n, then
also xj+nk may be either 0 or 1, and those xr for r < j + nk, r ̸≡ j (modk) are un-
restricted. On the other hand, suppose there is an n ≥ 0 such that xj+mk = 0 for all
m < n and xj+nk = 1. Again, the labels xr for r < j + (n + 1)k, r ̸≡ j (modk) are
unrestricted. However, xj+(n+1)k must now be a 1. Now the label of the vertex we are at,
having traversed the path labeled x0x1 · · · xj+(n+1)k from v0, has label 102k−1. Thus the
digits xj+(n+1)k+1, xj+(n+1)k+2, · · · xj+(n+3)k−1 are unrestricted. However, if the digit
xj+(n+2)k is a 1, then the vertex at the end of the path labeled x0x1 · · · xj+(n+2)k has label
102k−1, so the vertices after xj+(n+2)k are restricted or unrestricted in precisely the same
way as those after xj+(n+1)k. If on the other hand xj+(n+2)k = 0, then the terminal vertex
has label 10k−2. Thus, the label of the vertex after j + (n + 3)k − 1 steps in this case
is 1, hence in this case xj+(n+3)k must be 0. The resulting terminal vertex label is 0. In
either case, the digits, xj+(n+3)k+1, xj+(n+3)k+2, xj+(n+4)k−1 are unrestricted. For the
(j + (n + 4)k)th step we either begin at vertex 0 or at vertex 10k−1, which cases have
already been considered.
Thus, we have shown that the digits xj+nk place no restrictions on any digits from
the other modular classes, and, furthermore, we have described the restrictions that xj+nk
place on xj+mk for m > n. Inspecting this description shows that the admissible digits
xjxj+kxj+2k are precisely the edge labels of the inﬁnite walks in G originating at the
vertex 0 in Figure 5.1. These are precisely the elements of P, so Q = P (∗k). □

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES27

Let G be the graph of Figure 5.1. The presentation for Qk given by Proposition 3.4
applied to k and G is isomorphic to that given by Algorithm A of [3]. We are now ready to
prove Theorem 2.3.

Proof of Theorem 2.3. Let (Gk, v0) be the presentation of Q = X(1, Qk) constructed by
applying the algorithm of Proposition 3.4 to the presentation G of X(1, 7). Since the graph
G used in this construction has 4 vertices and 6 edges, it follows by Proposition 3.4 that Gk
has 4k vertices and 6 · 4k−1 edges. Moreover, since G is strongly connected, so is Gk, by
Remark 3.5. This proves the theorem. □

5.2. The family Qk = (2k0k−11)3 = 32k − 3k + 1: Hausdorff dimension. We have
shown that X(1, Qk) = X(1, 7)
(∗k), (5.2)

is given by an interleaving construction. Using the results of Section 3.4, it is now a simple
matter to prove Theorem 2.4.

Proof of Theorem 2.4. We are trying to show that

dimH (C(1, Qk)) = log3 φ.

The result follows by Proposition 5.1 and by application of the interleaving result given in
Corollary 3.7, since dimH (C(1, 7)) = log3 φ,

as is easily computed, and Corollary 3.7 shows that the interleaving operation (·)
(∗k) pre-
serves the topological entropy of the input path set. □

6. BOUNDS ON HAUSDORFF DIMENSIONS BY NUMBERS OF TERNARY DIGITS

We study properties of the Hausdorff dimension constants αn.

6.1. Upper Bound on Γ via n-digit constants αn: Proof of Theorem 2.5. It is known
that the number of nonzero ternary digits in (2n)3 goes to inﬁnity as n → ∞, i.e. for each
k ≥ 2 there are only ﬁnitely many n with (2n)3 having at most k nonzero ternary digits.
This result was ﬁrst established in 1971 by Senge and Straus, see [19]. In 1980 Colin L.
Stewart [21, Theorem 1] obtained a quantitative reﬁnement of such bounds. We obtain as
a special case of his result the following quantitative version of the rate of growth of the
number of nonzero digits.

Theorem 6.1. (C. L. Stewart) For each k ≥ 1, there are only ﬁnitely many n such that the
base 3 expansion of 2n (equivalently the 3-adic expansion (2n)3) has at most k nonzero
digits. More precisely, if n3(n) denotes the sum of the base 3 digits of n, then for m ≥ 25,

n3(2m) > log m
log log m + c − 3,

where c > 0 is an effectively computable constant.

Proof. The result follows from [21, Theorem 1], taking for bases a = 2, b = 3, and digits
α = β = 0. Using Stewart's notation, La,α(2m) = 2, so that La,α,b,β(2m) − 2 counts the
number of nonzero ternary digits n3(2m) of 2m. □

We can now prove Theorem 2.5.

28 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

Proof of Theorem 2.5. For each n ≥ 1 we have

Γ ≤ dimH (E (n+1)
1 ).

We also have the inclusions

E (n+1)
1 = ⋃

0≤m1<...<mk C(1, 2m1, . . . , 2mn) ⊂
 ∞⋃

m=n C(1, 2m), (6.1)

which yields
 dimH (E (n+1)
1 ) ≤ sup
m≥n
 ( dimH (C(1, 2m))
).

Consequently we have
 Γ ≤ sup
m≥n
 ( dimH (C(1, 2m))
). (6.2)

However Theorem 6.1 implies that all (2m)3 for m ≥ n contain at least

k = k(n) := ⌊ log n
log log n + c
 ⌋ − 3

nonzero ternary digits. In particular

E (n+1)
1 ⊂
 ∞⋃

m=n C(1, 2m) ⊂ ⋃

{M: n3(M)≥k(n)} C(1, M ).

By defnition of αk it follows that

dimH (E (n+1)
1 ) ≤ αk(n).

Since k(n) → ∞ as n → ∞, we obtain

Γ = lim
n→∞ dimH (E (n+1)
1 ) ≤ lim
k→∞ αk,

as asserted. □

6.2. Exact bound for α2. We obtain a complete determination of α2.

Theorem 6.2. For all M ≥ 1 with M ≡ 1 (mod 3), one has

dimH (C(1, M )) ≤ log3 φ ≈ 0.438018.

where φ = 1+√5
2 is the golden ratio. Thus α2 = log3 φ ≈ 0.438018

Proof. We may write M = (mnmn−1 . . . mk0k−11)3 for some 1 ≤ k ≤ n < ∞ since
M is an integer, M ≡ 1 (mod3). Our strategy will be to construct an injective map
f : C(1, M ) → C(1, Nk), where recall that Nk = (10k−11)3, and by [3, Theorem 1.8],
dimH (C(1, Nk)) = log3(φ). Let (G, v0) and (Hk, w0) be the right-resolving, connected,
essential presentations of C(1, M ) and C(1, Nk), respectively, constructed by Algorithm A
of [3]. The injective map f induces for each l an injective map from the set of paths of
length l in G originating at v0 to the set of paths of length l in Hk originating at w0, since
there is a bijective correspondence between elements of C(1, M ) or C(1, Nk) and inﬁnite
paths in G or Hk, respectively, originating at the distinguished vertex. Thus, following [1,
Deﬁnition 1.10] and [2, Theorem 1.1], this will establish the result.
To deﬁne the map f : C(1, M ) → C(1, Nk), we will need some notation. Let α =
. . . a2a1a0 be a generic element of C(1, M ). α corresponds to a vertex path . . . v2v1v0 of
G such that there is an edge labeled ai from vertex vi to vertex vi+1. We call the digit ai

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES29

restricted if the out-degree of vi is 1, and we call ai unrestricted if the out-degree of vi is
2. We call ai restricting if ai+k is restricted, and otherwise we call ai non-restricting.
If the digit ai of α is unrestricted, then it is possible to ﬁnd an element
α
′ = . . . ai+k−1ai+k−2 . . . ai+1(1 − ai)ai−1 . . . a2a1a0 ∈ C(1, M ). That is, changing ai
to 1 − ai does not require us to make any other changes until the i + k-th digit. Then
for all such α
′ the vertex v′
i+k of the corresponding vertex path on G is the same. If ai
is not only unrestricted but also restricting, then if this vertex v′
i+k has out-degree 1, we
call ai unconditionally restricting, and if v′
i+k has out-degree 2, we call ai conditionally
restricting. Thus, a conditionally restricting digit can be changed to become unrestricting,
while an unconditionally restricting digit remains restricting when changed.
Tautologically, a conditionally restricting digit ai becomes unrestricting when replaced
by 1 − ai, but we can also see that an unrestricted, unrestricting digit ai becomes condi-
tionally restricting when replaced by 1 − ai, since this necessarily changes the carry digit
at the (i + k)-th step. Thus, these types of digits come in pairs.
Now we are ready to construct the map f : C(1, M ) → C(1, Nk), digit-by-digit, for
α ∈ C(1, M ):

f (α)i =
 



0 if ai is restricted or unrestricting;
ai if ai is unrestricted and unconditionally restricting;
1 if ai is unrestricted and conditionally restricting. (6.3)

Though f (α) is clearly an element of Σ3, we need to check ﬁrst that it is really an
element of C(1, Nk). To see this, note that if f (α)i = 1, then ai was restricting, so
ai+k is restricted, thus f (α)i+k = 0. So a digit 1 of f (α) is always followed, k digits
later, by a digit 0. Since C(1, Nk) can be described as the Z/2Z-shift of ﬁnite type with
forbidden block set {10k−11}, and this block does not occur in f (α), we are assured that
f (α) ∈ C(1, Nk).
It remains only to check that f is injective. Suppose α = . . . a2a1a0, β = . . . b2b1b0 ∈
C(1, M ) are distinct. Then there is a j such that aj = 1 − bj and ai = bi for all 0 ≤
i < j. Let . . . v2v1v0 and . . . w2w1w0 be the vertex paths of G corresponding to α and
β, respectively. Then we must have vi = wi for 0 ≤ i ≤ j, and vj = wj must have
out-degree 2. Thus, the digits aj of α and bj of β are unrestricted. But by the discussion
above, if aj is conditionally restricting then bj is unrestricting, in which case f (α)j = 1 ̸=
0 = f (β)j, and vice versa, or else aj and bj are both unconditionally restricting, in which
case f (α)j = aj ̸= bj = f (β)j. In any case, we see that f (α) ̸= f (β), so f is injective,
establishing the result. □

7. BLOCK NUMBER AND INTERMITTENCY OF TERNARY EXPANSIONS

The examples given so far show that the dependence of dimH (C(1, M )) for a posi-
tive integer M is complicated function, being driven by the structure of the underlying
automata, whose construction includes aspects of both number theory and dynamical sys-
tems. One may ask whether the Hausdorff dimension might go to zero as a function of
some statistic easily computable from the ternary expansion (M )3. Earlier results of this
paper show that the statistic d3(M ) does not have this property.
We now present empirical results for two other interesting statistics of (M )3:
(1) The block number b3(M ) counts the number of blocks of consecutive nonzero
digits in the ternary expansion (M )3.
(2) The intermittency s3(M ) counts the number of distinct blocks of consecutive
matching digits in the ternary expansion (M )3.

30 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

We clearly have b3(M ) ≤ s3(M ). As examples,

b3((2121011)3) = 2; b3((2101)3) = 2,

while s3((2121011)3) = 6; s3((2101)3) = 4.

The statistic b3(M ) might be relevant to controlling the Hausdoff dimension since blocks
of zeros at the end of the number have a simple effect on the associated automaton.
Table 7.1 below presents data on Hausdorff dimensions for a few numbers M taking the
smallest values for s3(M ), computed using the algorithm in Part I to six decimal places.
The table also provides the number of vertices in the associated ﬁnite directed graph.

Path Set C(1, M ) (M )3 s3(M ) Vertices Perron eigenvalue Hausdorff dim
C(1, 10) 101 3 4 1.618033 0.438018
C(1, 16) 121 3 5 1.324718 0.255960
C(1, 19) 201 3 8 1.465571 0.347934
C(1, 73) 2201 3 16 1.618033 0.438018
C(1, 34) 1021 4 8 1.324718 0.255960
C(1, 46) 1201 4 10 1.112776 0.097266
C(1, 61) 2021 4 14 1.570147 0.410672
C(1, 64) 2101 4 14 1.357193 0.278004
C(1, 70) 2121 4 14 1.360632 0.280308
C(1, 91) 10101 5 9 1.465571 0.347934
C(1, 97) 10121 5 16 1.380277 0.293356
C(1, 100) 10201 5 17 1.354948 0.276497
C(1, 142) 12021 5 20 1.276393 0.222133
C(1, 145) 12101 5 21 1.000000 0.000000
C(1, 151) 12121 5 20 1.227525 0.186599
C(1, 172) 20101 5 22 1.288329 0.230606
C(1, 178) 20121 5 25 1.345528 0.270148
C(1, 181) 20201 5 22 1.324718 0.255960
C(1, 196) 21021 5 24 1.383785 0.295666
C(1, 208) 21201 5 25 1.290893 0.232415

TABLE 7.1. Hausdorff dimension of C(1, M ) by intermittency

This extremely limited data set exhibits a small decrease in Hausdorff dimensions as the
statistic s3(M ) increases. It leaves open the possibility that one might have dimH (C(1, M )) →
0 as b3(M ) → ∞, noting that b3(M ) ≤ s3(M ). Further numerical experimentation seems
warranted to get a better idea whether such an assertion might be true.
Regarding potential applicability of information on these statistics to the Exceptional
set conjecture, we must point out that it is not currently known whether b3(2n) → ∞
holds as n → ∞ or whether s3(2n) → ∞ holds as n → ∞.

8. APPENDIX A: REVIEW OF RESULTS FOR FAMILIES Lk = (1k)3 AND
Nk = (10k−11)3.

We review two results proved in [3, Section 4]. The ﬁrst is for the family Lk = 1
2 (3k −
1) = (1k)3, for k ≥ 1, given as [3, Theorem 5.2].

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES31

Theorem 8.1. (Inﬁnite Family Lk = 1
2 (3k − 1))
(1) Let Lk = 1
2 (3k − 1) = (1k)3. The path set presentation (G, v) for the path set
X(1, Lk) underlying C(1, Lk) has exactly k vertices and is strongly connected.
(2) For every k ≥ 1,

dimH (C(1, Lk)) = dimH C(1, (1k)3) = log3 βk,

where βk is the unique real root greater than 1 of λ
k − λ
k−1 − 1 = 0.
(3) For all k ≥ 3 there holds

dimH (
C(1, Lk)
) = log3 k
k + O ( log log(k)
k
 ) .

The Hausdorff dimension dimH(C(1, Lk)) is positive but approaches 0 as k → ∞. We
present data in Table 8.1 below.
Path set Lk Vertices Perron eigenvalue Hausdorff dim
C(1, L1) 1 1 2.000000 0.630929
C(1, L2) 4 2 1.618033 0.438018
C(1, L3) 13 3 1.465571 0.347934
C(1, L4) 40 4 1.380278 0.293358
C(1, L5) 121 5 1.324718 0.255960
C(1, L6) 364 6 1.285199 0.228392
C(1, L7) 1093 7 1.255423 0.207052
C(1, L8) 3280 8 1.232055 0.189948
C(1, L9) 9841 9 1.213150 0.175877

TABLE 8.1. Hausdorff dimensions of C(1, Lk) (to six decimal places)

We also recall results on the family Nk = 3k + 1 = (10k−11)3, which consists of
numbers with exactly two nonzero ternary digits, with s3(Nk) = 2, given as [3, Theorem
5.5].

Theorem 8.2. (Inﬁnite Family Nk = 3k + 1)
(1) Let Nk = 3k + 1 = (10k−11)3. The path set presentation (G, v) for the path set
X(1, Nk) underlying C(1, Nk) has exactly 2k vertices and is strongly connected.
(2) For every integer k ≥ 1, there holds

dimH (C(1, Nk)) = dimH C(1, (10k−11)3) = log3
 ( 1 + √
5
2
 ) ≈ 0.438018.

Here the Hausdorff dimension is constant as k → ∞.

9. APPENDIX B: RELATION OF FAMILIES Pk = (20k−11)3 AND Lk+1 = (1k+1)3

We observe a relation between the Hausdorff dimensions of C(1, Pk) and C(1, Lk+1).
For 1 ≤ k ≤ 4, the Hausdorff dimension of C(1, (20k−11)3) equals that of C(1, (1k+1)3).
For general k we obtain an inequality.

Theorem 9.1. The Hausdorff dimensions of C(1, Pk) and C(1, Lk+1) are related by

dimH (C(1, Pk)) ≥ dimH (C(1, Lk+1)). (9.1)

Proof. The marked vertex v0 with label (0)3 of the path set presentation G(20k−11)3 associ-
ated to C(1, (20k−11)3) has two exit edges, one a self-loop with edge labeled 0, the second

32 WILLIAM C. ABRAM, ARTEM BOLSHAKOV, AND JEFFREY C. LAGARIAS

an exit edge labeled 1 to the vertex labeled (20k−1)3. From this vertex, there is an edge
labeled 1 to the vertex labeled (220k−2)3. This continues for k − 2 more steps into a vertex
labeled (2k)3, from which there is an out-edge labeled 1 to a vertex labeled (10k)3. There
is a self-loop labeled 1 at the (10k)3-vertex, and a path of length k + 1 through vertices
(10k−j)3, for 1 ≤ j ≤ k, all with edge label 0, then back to the 0-vertex. Considering only
the edges given above, this comprises a subgraph H of G(20k−11)3 having 2k + 2 edges
that is strongly connected, and consists of a closed path starting and ending at 0 of length
2k + 2 plus two self-loops, at vertices m = 0 and m = 3k. (The case k = 2 is pictured in
Example 4.1, where the subgraph of G(201)3 under consideration is the six outer vertices in
the graph in Figure 4.1.) Upon inspection we see that the graph H is a double-covering of
the graph G(1k+1)3 associated to C(1, Lk+1) given by Algorithm A of [3]. This implies the
bound (9.1). □

Remark 9.2. For 1 ≤ k ≤ 4, equality holds in Proposition 9.1 because the subgraph
of G(20k−11)3 constructed in the proof is the strongly connected component with great-
est topological entropy in these cases. This is not true for almost all larger k. Theorem
8.1 says dimH (C(1, Lk)) → 0 as n → ∞. On the other hand Theorem 2.2 says that
dimH (C(1, Lk)) is bounded away from 0 as k → ∞.

REFERENCES

[1] W. Abram and J. C. Lagarias, Path sets in one-sided symbolic dynamics, Advances in Applied Mathematics,
56 (2014), pp. 109-134.
[2] W. Abram and J. C. Lagarias, p-Adic path set fractals and arithmetic, Journal of Fractal Geometry, 1 (2014),
no.1, 45-81.
[3] W. Abram and J. C. Lagarias, Intersections of multiplicative translates of 3-adic Cantor sets, Journal of
Fractal Geometry, 1 (2014), no.4, 349–390.
[4] R.L. Adler and B. Marcus, Topological entropy and equivalence of dynamical systems, Memoirs of the
American Mathematical Society, Volume 20, No. 219, AMS: Providence, RI 1979.
[5] J.P. Alloche and J. O. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge Uni-
versity Press: Cambridge 2003.
[6] M. Boyle and D. Handelman, The spectrum of nonnegative matrices via symbolic dynamics, Ann. Math. 133
(1991), no. 2, 249–316.
[7] G. Edgar, Measure, topology and fractal geometry, Second Edition Springer-Verlag: New York 2008.
[8] P. Erd˝os, Some unconventional problems in number theory, Math. Mag. 52 (1979), 67-70.
[9] E. de Faria and C. Tresser, On Sloane's persistence problem, arXiv:1307.1188, July 2013.
[10] E. de Faria and C. Tresser, Equidistribution of digits in powers and Diophantine approximations,
arXiv:1307.1505, 5 July 2013.
[11] A. Katok and B. Hasselblatt, Introduction to the Modern Theory of Dynamical Systems (Cambridge Univer-
sity Press, New York, 1995).
[12] J.C. Lagarias, Ternary expansions of powers of 2, J. London Math. Soc.(2) 79 (2009), 562-588.
[13] D. Lind, The entropies of topological Markov shifts and a related class of algebraic integers, Ergod. Th.
Dyn. Sys. 4 (1984), no. 2, 283–300.
[14] D. Lind and B. Marcus, An Introduction to Symbolic Dynamics and Coding, (Cambridge University Press,
New York, 1995).
[15] K. Mahler, Lectures on diophantine approximations, Part I. g-adic numbers and Roth's theorem , Prepared
from notes of R. P. Bambah, University of Notre Dame Press, Notre Dame IN 1961.
[16] R. D. Mauldin and M. Urba´nski, Graph directed Markov systems. Geometry and dynamics of limit sets,
Cambridge Tracts in Mathematics No. 148, Cambridge Univ. Press: Cambridge 2003.
[17] R. D. Mauldin and S. C. Williams, On the Hausdorff dimension of some graphs, Trans. Amer. Math. Soc.
298 (1986), no. 2, 793–803.
[18] R.D. Mauldin and S.C. Williams, Hausdorff Dimension of Graph Directed Constructions, Transactions of
the American Mathematical Society, 309, No. 2 (1988) , 811-829.
[19] H. G. Senge and E. Straus, P.V. numbers and sets of multiplicity, Periodica Math. Hung. 3 (1973), 93–100.

INTERSECTIONS OF MULTIPLICATIVE TRANSLATES OF 3-ADIC CANTOR SETS II: TWO INFINITE FAMILIES33

[20] J.G. Simonsen, On the Computabillity of the Topological Entropy of Subshifts, Discrete Mathematics and
Theoretical Computer Science, 8 (2006), 83-96.
[21] C. L. Stewart, On the Representation of an Integer in two Different Bases, J. Reine Angew. Math., 319
(1980), 63–72.
[22] B. Weiss, Subshifts of ﬁnite type and soﬁc systems, Monatshefte für Math. 77 (1973), 462–474.
[23] S. Williams, A soﬁc system which is not spectrally of ﬁnite type, Ergod. Th. Dyn. Sys. 8 (1988), 483–490.

DEPARTMENT OF MATHEMATICS, HILLSDALE COLLEGE, HILLSDALE, MI 49242-1205, USA
E-mail address: wabram@hillsdale.edu

COLLEGE OF THE SCHOOL OF NATURAL SCIENCES AND MATHEMATICS, UNIVERSITY OF TEXAS

AT DALLAS, RICHARDSON, TX 75080-3021, USA
E-mail address: atb130030@utdallas.edu

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF MICHIGAN, ANN ARBOR, MI 48109-1043,USA
E-mail address: lagarias@umich.edu
