<!-- source: https://arxiv.org/pdf/0710.4607 | converted from PDF -->

arXiv:0710.4607v4  [math.AG]  12 Jun 2008
GALOIS GROUPS OF SCHUBERT PROBLEMS
VIA HOMOTOPY COMPUTATION

ANTON LEYKIN AND FRANK SOTTILE

Abstract. Numerical homotopy continuation of solutions to polynomial equations is
the foundation for numerical algebraic geometry, whose development has been driven by
applications of mathematics. We use numerical homotopy continuation to investigate the
problem in pure mathematics of determining Galois groups in the Schubert calculus. For
example, we show by direct computation that the Galois group of the Schubert problem
of 3-planes in C8 meeting 15 ﬁxed 5-planes non-trivially is the full symmetric group S6006.

Introduction

Numerical homotopy continuation [26] gives a method to ﬁnd all solutions to a system
of polynomials with ﬁnitely many solutions. Current parallel implementations [18] can
solve systems with over 40 million solutions [19]. The emerging ﬁeld of numerical algebraic
geometry [25, 26] uses numerical homotopy continuation as a foundation for algorithms
to study algebraic varieties. While numerical algebraic geometry was developed for ap-
plications of mathematics, we apply it in pure mathematics, computing Galois groups of
enumerative-geometric problems from the Schubert calculus, called Schubert problems.
Along with [2], this is one of the ﬁrst applications of numerical algebraic geometry to a
problem in pure mathematics.
Jordan introduced Galois groups of enumerative problems in 1870 [11] and Harris laid
their modern foundations in 1979 [8], showing that the algebraic Galois group is equal
to a geometric monodromy group. Byrnes [4, Section 5] used Harris’s theory to prove
that the general problem of placing poles with static output feedback in linear systems
theory was not solvable by radicals. He used numerical homotopy continuation to show
that a particular Galois group arising in pole placement was the full symmetric group, S5.
Underlying this calculation was a Schubert problem. Vakil [32] applied his geometric
Littlewood-Richardson rule [31] to study Galois groups of Schubert problems and showed
that many Schubert problems have Galois group containing the alternating group.
A Schubert problem is simple if it involves no more than two Schubert conditions of
codimension more than 1. Simple Schubert problems are natural to study [28, 29] and
among all Schubert problems on a given Grassmannian, they have the largest intersection
numbers, so they are the most challenging for direct computation. They may also be
formulated as complete intersections, which is a restriction imposed by our software.

2000 Mathematics Subject Classiﬁcation. 14N15, 65H20.
Key words and phrases. Polynomial homotopy continuation, Schubert problem, Galois group.
Leykin and Sottile supported by the Institute for Mathematics and its Applications and Sottile by
NSF grants CAREER DMS-0538734 and DMS-0701050.
1

2 ANTON LEYKIN AND FRANK SOTTILE

Numerical Theorem. The Galois group of the Schubert problem of 3-planes in C8

meeting 15 ﬁxed 5-planes non-trivially is the full symmetric group S6006.

This is a numerical theorem, as our software does not certify its output. We have
computed Galois groups of scores of other simple Schubert problems, including one on
the Grassmannian of 4-planes in C8 having 8580 solutions and ones on Grassmannians of
3-planes in C8 and in C9 having 10329 and 17589 solutions, respectively. In every case, we
ﬁnd that the Galois group is the full symmetric group. Table 2 in Section 3.2 records some
of these calculations. Based on this evidence, we conjecture that every simple Schubert
problem on a Grassmannian has Galois group equal to the full symmetric group.
Not all Schubert problems have Galois group equal to the full symmetric group. Using
an idea of Derksen, Vakil [32] gives some Schubert problems on Grassmannians whose
Galois group is not the full symmetric group and Ruﬀo, et. al. [21] give one on a particu-
larly small ﬂag manifold. None of these examples can be studied with our software, which
requires the Schubert problem to have a formulation as a complete intersection.
Our software has two implementations in Maple which use homotopy continuation to
compute elements in the Galois groups and either Maple or GAP [6] to determine if these
elements generate the full symmetric group. For the continuation, both implementations
use PHCpack [33] through its Maple interface PHCmaple [17] and the second may also
call Bertini [1]. The advantages of Bertini are that it can use arbitrary precision and it
gives an independent veriﬁcation of our results.
Numerical techniques give insight into some mathematical properties that are far be-
yond the reach of other methods. For example, Billey and Vakil [3] studied Galois groups
of Schubert problems using symbolic methods. The largest problem that they treated
(showing its Galois group is the full symmetric group) had 9 solutions on the Grassman-
nian of 2-planes in C6, and they stated that the Schubert problem on this Grassmannian
having 14 solutions was computationally infeasible.
The largest simple Schubert problem which we have solved symbolically has 91 solu-
tions [21, §5.3]. In contrast, numerical methods allow us to solve Schubert problems with
as many as 17589 solutions. These examples actually underestimate the gap between
the computational possibilities of symbolic and numeric methods, because they were per-
formed on serial machines.
Current and (likely) future increases in computer power will come from multiple core
and distributed computing. This is a break with the past, when improvements in compu-
tational power came from increasing the clock speed of single-processor units. Symbolic
algorithms have limited potential in this regime, as Gr¨obner basis computation appears to
be intrinsically serial and thus can not be eﬃciently parallelized. In contrast, numerical
homotopy continuation is easily parallelized, since its atomic tasks are independent. Thus
methods based on numerical continuation will reap the beneﬁts of future parallel archi-
tectures. In addition, numerical algorithms typically require less memory than symbolic
algorithms. In particular, the sizes of ﬁnal and intermediate expressions in Gr¨obner basis
computation not only may be large, but also are unpredictable. For these reasons, we feel
that the future of computing in algebraic geometry lies in numerical algorithms.

GALOIS GROUPS OF SCHUBERT PROBLEMS 3

This paper is structured as follows. In Section 1, we describe the basic geometry of
Schubert problems and Harris’s theory of Galois groups. In Section 2, we explain the use
of homotopy continuation for simple Schubert problems. We present our software and
algorithms and discuss our results in Section 3, which include the computation described
in the Numerical Theorem. We describe future work in Section 4.

1. Galois group computation of Schubert problems

The Schubert calculus [14] is a method to compute the number of solutions to Schu-
bert problems, which are a class of geometric problems involving linear subspaces. The
prototypical Schubert problem is the classical problem of four lines: How many lines in
space meet four given lines? To answer this, note that three lines ℓ1, ℓ2, ℓ3 lie on a unique
doubly-ruled hyperboloid, depicted in Figure 1. These three lines lie in one ruling, while

ℓ1
 ℓ2

ℓ3

ℓ4
 m1

m2

p ✑
✑
✑
✑
✑
✑✑✸

Figure 1. The two lines meeting four lines in space.

the second ruling consists of the lines meeting the given three lines. The fourth line ℓ4
meets the hyperboloid in two points. Through each of these points there is a line in the
second ruling, and these are the two lines m1 and m2 meeting our four given lines.
The Galois group of this Schubert problem is the group of permutations which are
obtained by following the solutions over loops in the space of lines ℓ1, . . . , ℓ4. Rotating
ℓ4 about the point p gives a loop which interchanges the two solution lines m1 and m2,
showing that the Galois group is S2, the full symmetric group on two letters.

1.1. Schubert problems in the Grassmannian. A typical Schubert problem asks for
the linear subspaces of a ﬁxed dimension (k-planes) in Cn that have speciﬁed positions
(incidence conditions) with respect to some ﬁxed, but otherwise general, linear subspaces.
Each incidence condition deﬁnes a set of k-planes, called a Schubert variety, and the
solutions to the Schubert problem are the points of intersection of the corresponding
Schubert varieties. We describe this class of problems.

4 ANTON LEYKIN AND FRANK SOTTILE

The Grassmannian G(k, n) is the set of k-planes in Cn. This is a complex manifold of
dimension k(n−k). The problem of four lines involves the four-dimensional Grassmannian
G(2, 4) as a line in (projective) 3-space corresponds to a 2-plane in C4. The set of lines m
meeting a ﬁxed line ℓ corresponds to the set of 2-planes M of C4 whose intersection with
a ﬁxed 2-plane L is at least one-dimensional, and this set of lines m is a Schubert variety.
The problem of four lines asks for the points common to four such Schubert varieties, one
for each of the given lines ℓ1—ℓ4 in projective 3-space.
The speciﬁed positions of k-planes in Schubert problems are in reference to ﬂags in Cn.
A ﬂag F• is a sequence of linear subspaces

F• : F1 ⊂ F2 ⊂ · · · ⊂ Fn−1 ⊂ Fn = Cn ,

where i = dim Fi. The possible positions are encoded by partitions. A partition λ is a
weakly decreasing sequence of integers

λ : (n−k) ≥ λ1 ≥ λ2 ≥ · · · ≥ λk ≥ 0 .

Give a partition λ and a ﬂag F•, the Schubert (sub)variety YλF• of G(k, n) is

(1.1) YλF• := {E ∈ G(k, n) | dim E ∩ Fn−k+i−λi ≥ i, i = 1, . . . , k} .

This has codimension |λ| := λ1 + · · · + λk in G(k, n). When λ = □ := (1, 0, . . . , 0),

Y□F• = {E ∈ G(k, n) | dim E ∩ Fn−k ≥ 1} ,

as the other conditions are redundant. We call □ a simple Schubert condition and Y□F•
a simple Schubert variety. It depends only upon Fn−k, so we also write Y□Fn−k. All four
Schubert varieties in the problem of four lines are simple.
A Schubert problem is a list (λ1, . . . , λm) of partitions with |λ1| + · · · + |λm| = k(n−k).
By Kleiman’s Transversality Theorem [13], if F 1
• , . . . , F m
• are general, then the intersection

(1.2) Yλ1F 1
• ∩ Yλ2F 2
• ∩ · · · ∩ YλmF m
•

is transverse and consists of ﬁnitely many k-planes. The number d(λ1, . . . , λm) of k-
planes may be computed using the algorithms in the Schubert calculus (see [14] or [5] or
the Introduction to [9]). The problem of four lines is an instance of the Schubert problem
(□, □, □, □) in G(2, 4) and our analysis shows that d(□, □, □, □) = 2.
We study Schubert problems in which all except possibly two Schubert conditions are
simple. A simple Schubert problem on G(k, n) is one of the form
(λ, µ, □, . . . , □
︸ ︷︷ ︸
k(n−k)−|λ|−|µ|

) ,

where λ, µ are not necessarily equal to □. We speak of the simple Schubert problem (λ, µ)
on G(k, n) (the k(n − k) − |λ| − |µ| simple conditions □ are understood).
The primary reason for limiting our study to simple Schubert problems in this paper
is that these are Schubert problems that are complete intersections, and the oﬀ-the-shelf
software that we use restricts us to complete intersections.

GALOIS GROUPS OF SCHUBERT PROBLEMS 5

1.2. Galois groups of Schubert problems. According to Harris [8], Jordan [11] showed
how intrinsic structures of some enumerative problems could be understood in terms of
Galois theory. Harris took the opposite approach—computing Galois groups of enumer-
ative problems to expose the intrinsic structure of an enumerative problem. He showed
that many enumerative problems have Galois group equal to the full symmetric group,
demonstrating that these problems had no underlying structures.
Harris’ theory relating Galois groups to monodromy groups begins with a map f : U →
V of degree d between irreducible complex algebraic varieties U and V . The function ﬁeld
C(U) of U is a degree d extension of the function ﬁeld C(V ) of V . These ﬁelds may be
embedded into the ﬁeld K of germs of meromorphic functions on a disc around a regular
value v ∈ V of f . If L ⊂ K is the normalization in K of the extension C(U)/C(V ), then
the Galois group G = Gal(L/C(V )) acts faithfully on the d points f −1(v), and this gives
an embedding G ֒→ Sd, where Sd is the symmetric group of the ﬁber f −1(v).
Replacing U and V by Zariski open subsets if necessary, we may assume that the map
f : U → V is a degree d covering. A loop in V based at v has d lifts to U, one for each
point in the ﬁber f −1(v). Associating a point in the ﬁber f −1(v) to the endpoint of the
corresponding lift gives a permutation in Sd. This deﬁnes the usual permutation action
of the fundamental group of V on the ﬁber f −1(v). The monodromy group of the map
f : U → V is the image of the fundamental group of V in Sd.

Proposition 1.1 (Harris [8]). For a map f : U → V as above, the monodromy group
equals the Galois group.

Given a Schubert problem (λ1, . . . , λm) on G(k, n), let V be the space of m-tuples
(F 1
• , . . . , F m
• ) of ﬂags, a product of ﬂag manifolds. Deﬁne U to be the incidence variety

(1.3) U := {(H, F 1
• , . . . , F m
• ) ∈ G(k, n) × V | H ∈ YλiF i
• for i = 1, . . . , m} .

The ﬁber of U over a point H ∈ G(k, n) is a product of the Schubert subvarieties

{F i
• | H ∈ YλiF i
•} i = 1, . . . , m

of the ﬂag manifold. Each of these is irreducible, and so U is irreducible. Let f : U → V
be the other projection. Given v = (F 1
• , . . . , F m
• ) ∈ V , the ﬁber f −1(v) is the intersec-
tion (1.2). When v is general, this has d = d(λ1, . . . , λm) points, so that the map f has
degree d. The Galois group of the Schubert problem is the Galois group of the extension
C(U)/C(V ). By Proposition 1.1, this is the monodromy group of the map f : U → V .

The point of this paper is that these monodromy groups may be computed using nu-
merical homotopy continuation. For this, we ﬁrst compute the points in a single ﬁber
f −1(v). Then, given a loop ϕ : [0, 1] → V based at v (ϕ(0) = ϕ(1) = v), we numerically
follow the points in the ﬁbers f −1(ϕ(t)) as t runs from 0 to 1. This computes the lifts of ϕ
and thus the associated monodromy permutation. Computing suﬃciently many of these
monodromy permutations will enable us to recover the Galois group. While this gives the
idea behind our method, we postpone more details until Section 3.1.

6 ANTON LEYKIN AND FRANK SOTTILE

2. Homotopy continuation of simple Schubert problems

Homotopy continuation is a numerical method to compute all solutions to a system
of polynomials given the solutions to a similar system. We use it to ﬁnd all solutions
to a simple Schubert problem and to compute elements of the monodromy group. We
ﬁrst describe the method of numerical homotopy continuation, then discuss polynomial
formulations of Schubert problems, and ﬁnally explain the Pieri homotopy algorithm [9,
10] to ﬁnd all solutions to simple Schubert problems.

2.1. Homotopy continuation of polynomial systems. Suppose that we want to ﬁnd
all solutions to a 0-dimensional target system of polynomial equations

(2.1) f1(x1, . . . , xn) = f2(x1, . . . , xn) = · · · = fN (x1, . . . , xn) = 0 ,

written as F (x) = 0. Numerical homotopy continuation ﬁnds these solutions if we have a
homotopy, which is a system H(x, t) of polynomials in n+1 variables such that
(1) The systems H(x, 1) = 0 and F (x) = 0 both have the same solutions;
(2) We know all solutions to the start system H(x, 0) = 0;
(3) The components of the variety deﬁned by H(x, t) = 0 include curves whose pro-
jection to C (via the second coordinate t) is dominant; and
(4) The solutions to the system H(x, t) = 0, where t ∈ [0, 1), occur at smooth points
of curves from (3) in the variety H(x, t) = 0.
Given this, we restrict the variety H(x, t) = 0 to t ∈ [0, 1] and obtain ﬁnitely many
real arcs in Cn × [0, 1] which connect (possibly singular) solutions of the target system
H(x, 1) = 0 to solutions of the start system H(x, 0) = 0. We then numerically trace each
arc from t = 0 to t = 1, obtaining all isolated solutions to the target system.
The homotopy is optimal if every solution at t = 0 is connected to a unique solution
at t = 1 along an arc. This is illustrated in Figure 2. For simple Schubert problems, the

0 1
 t

optimal 0 1
not optimal
 t
 0 1
not optimal
 t

Figure 2. Optimal and non-optimal homotopies

Pieri homotopy algorithm is optimal.

Remark 2.1. Homotopy continuation software often constructs a homotopy as follows.
Let F (x) be the target system (2.1) and suppose we have solutions to a start system G(x).

GALOIS GROUPS OF SCHUBERT PROBLEMS 7

Then for a number γ ∈ C with |γ| = 1 deﬁne the linear homotopy

H(x, t) := γtF (x) + (1 − t)G(x) .

Then H(x, t) satisﬁes the deﬁnition of a homotopy for all but ﬁnitely many γ. The
software detects the probability 0 event that H(x, t) does not satisfy the deﬁnition when
it encounters a singularity, and then it recreates the homotopy with a diﬀerent number γ.

Path following algorithms use predictor-corrector methods, which are conceptually sim-
ple for square systems, where the number of equations equals the number of variables.
Given a point (x
(0), t
(0)) on an arc such that t
(0) ∈ [0, 1), the n × n matrix

Hx := ( ∂Hi
∂xj
 )n

i,j=1

is regular at (x
(0), t
(0)), which follows from the deﬁnition of the homotopy. Let Ht :=
(∂H1/∂t, . . . , ∂Hn/∂t)T . Given ∆t, we set

∆x := −∆t Hx(x
(0), t
(0))−1 Ht(x
(0), t
(0)) .

For t
(1) = t
(0) + ∆t, the point (x
′, t
(1)) = (x
(0) + ∆x, t
(1)) is an approximation to the
point (x
(1), t
(1)) on the same arc. This constitutes a ﬁrst order predictor step. A cor-
rector step uses the multivariate Newton method for the system H(x, t
(1)) = 0, reﬁning
the approximate solution x
′ to a solution x
(1). In practice, the points x
(0) and x
(1) are
numerical (approximate) solutions, and both the prediction and correction steps require
that det Hx ̸= 0 at every point where the computation of the Jacobian matrix Hx is done.
When the system is not square, additional strategies must be employed to enable the
path following. Fortunately, simple Schubert problems are exactly the class of Schubert
problems for which we have an optimal square homotopy (the Pieri homotopy).
Cheater homotopies [20] are optimal homotopies constructed from families of polynomial
systems. For example, given a Schubert problem (λ1, . . . , λm), let V be the space of all
m-tuples (F 1
• , . . . , F m
• ) of ﬂags. The total space of the Schubert problem

U := {(H, F 1
• , . . . , F m
• ) ∈ G(k, n) × V | H ∈ YλiF i
• for i = 1, . . . , m}

is deﬁned by equations (see Section 2.2) depending upon the point (F 1
• , . . . , F m
• ) ∈ V . If
ϕ : C → V is an embedding of C into V in which ϕ(0) and ϕ(1) are general m-tuples of
ﬂags and we write ϕ(t) = (F 1
• (t), . . . , F m
• (t)), then

ϕ∗U = {(H, F 1
• (t), . . . , F m
• (t)) | H ∈ YλiF i
•(t) for i = 1, . . . , m} .

This is deﬁned by a system H(x, t) = 0, which gives an optimal homotopy. We use
this particular cheater homotopy to compute permutations in monodromy groups, called
monodromy permutations. We give more details in Section 3.1.
There, we describe the Pieri homotopy algorithm, which is a cheater homotopy where
only one ﬂag in ϕ(t) actually moves and the others remain ﬁxed. The moving ﬂag is in
general position when t = 1, but in a particular special position when t = 0, so that
the Schubert problem becomes a union of other Schubert problems (whose solutions were
previously computed and thus are known).

8 ANTON LEYKIN AND FRANK SOTTILE

2.2. Equations for Schubert problems. Polynomial homotopy continuation methods
require that our geometric problems are modeled by a system of polynomial equations.
For eﬃciency, the number of variables should be minimized. We describe equations for
Schubert varieties and then model Schubert problems by systems of equations which
minimize the number of variables, stated in Proposition 2.2 below.
Represent a k-plane in Cn as the row space of a k by n matrix E with full rank and
a ﬂag by an invertible n by n matrix F• of constants, where the i-dimensional subspace
in the ﬂag is the row space of the ﬁrst i rows Fi of the matrix. The condition from (1.1)
that dim E ∩ Fn−k+i−λi ≥ i is

(2.2) rank [ E
Fn−k+i−λi
] ≤ n − λi ,

which is given by the vanishing of the determinants of all n+1−λi by n+1−λi submatrices
of the n+i−λi by n matrix in (2.2). When λi = 0 the condition (2.2) is empty.
Write E(E, F•, λ) for the system consisting of these ∑
i (n+i−λi
n+1−λi)( n
n+1−λi) equations.
The codimension |λ| equals the number of equations only when λ = □. In that case,
E(E, F•, □) consists of the single equation

(2.3) det [ E
Fn−k
] = 0 .

Since any two ﬂags in general position are conjugate under a linear transformation, we
always assume that two ﬂags in (1.2) are ﬁxed. Let the ﬂag F• be deﬁned by setting Fi to
be the span of en, en−1, . . . , en+1−i, where e1, . . . , en form the standard basis for Cn. The
Schubert variety YλF• has an open subset isomorphic to Ck(n−k)−|λ| consisting of k-planes
that are the row space of an echelon matrix of the form






0 · · · 0 1 ∗ · · · ∗ 0 ∗ · · · ∗ 0 ∗ · · · ∗
0 · · · 0 0 0 · · · 0 1 ∗ · · · ∗ 0 ∗ · · · ∗
. . . . . . .

0 · · · 0 0 0 · · · 0 0 0 · · · 0 1 ∗ · · · ∗






where 1 + λk, 2 + λk−1, . . . , k + λ1 are the columns with 1s and ∗ represents some number.
To further reduce the number of variables, let the ﬂag F ′
• be deﬁned by setting F ′
i to
be the span of e1, . . . , ei. The skew Schubert variety [30] (or Richardson variety),

Yλ,µ := YλF• ∩ YµF ′
•
has an open subset parameterized by matrices of the form

Eλ,µ :=
 

 0 1 ∗ · · · · · · · · · ∗ 0 · · · 0. . . . . . . ∗ · · · · · · · · · ∗ . . . .
0 · · · 0 1 ∗ · · · · · · · · · ∗ 0
 



whose entries ai,j are 



 1 if j = i + λk+1−i ,
∗ if i + λk+1−i < j ≤ n − k + i − µi ,
0 otherwise .

GALOIS GROUPS OF SCHUBERT PROBLEMS 9

This parameterization is one-to-one if the product of the rightmost entries is non-zero,

0 ̸=
 k∏

i=1 ai, n−k+i−µi .

On the left below is E□,□ in G(2, 4) and on the right is E210,110 in G(3, 7).

(2.4) [1 x 0 0
0 0 1 y
] 

1 a b c 0 0 0
0 0 1 d e 0 0
0 0 0 0 1 f g




Given a Schubert problem λ, µ, ν1, . . . , νm, we will always take two of the ﬂags to be
these coordinate ﬂags F• and F ′
•, and consider intersections of the form

Yλ,µ ∩ Yν1F 1
• ∩ · · · ∩ YνmF m
• ,

where the ﬂags F 1
• , . . . , F m
• are general. By Kleiman’s transversality theorem, all intersec-
tions will lie in the subset of Yλ,µ that is parameterized by matrices from Eλ,µ, and thus
are solutions to the system of equations given by

E(Eλ,µ, F 1
• , ν1), . . . , E(Eλ,µ, F m
• , νm) .

This system is not necessarily square unless it is a simple Schubert problem. Since the
homotopy continuation software we use is for square systems of polynomials, we restrict
ourselves to simple Schubert problems. Write G for the n−k by n matrix Fn−k. Then
E(Eλ,µ, F•, □) is a single equation (2.3) that depends only on G.

Proposition 2.2. A simple Schubert problem (λ, µ) on G(k, n) is given by m := k(n −
k) − |λ| − |µ| matrices G1, . . . , Gm each of size n−k by n, and the solutions are modeled
by the system of equations

(2.5) det [Eλ,µ
G1
 ] = det [
Eλ,µ
G2
 ] = · · · = det [
Eλ,µ
Gm
 ] = 0 .

For example, the simple Schubert problem □, □ on G(2, 4) is modeled by

(2.6) det
 




 1 x 0 0
0 0 1 y
g11 g12 g13 g14
g21 g22 g23 g24




 = det
 




 1 x 0 0
0 0 1 y
g′
11 g′
12 g′
13 g′
14
g′
21 g′
22 g′
23 g′
24




 = 0 ,

where G1 = (gij) and G2 = (g′
ij) are matrices of constants.

2.3. Pieri homotopy algorithm. We describe the simpliﬁed version of the Pieri ho-
motopy algorithm [9, 10] that we use. The Pieri homotopy algorithm ﬁnds all solutions
to those Schubert problems where all except possibly two partitions consist of a single
part, (a, 0, . . . , 0). It is based on subtle geometric degenerations constructed in [27]. Both
the algorithm and the degenerations enjoy a dramatic simpliﬁcation for simple Schubert
problems. The degenerations for these simple Schubert problems were introduced by
Schubert [22, 23].

10 ANTON LEYKIN AND FRANK SOTTILE

Example 2.3. Consider the simple Schubert problem (λ, µ) = (210, 110) in G(3, 7). Begin
with local coordinates (2.4) for E210,110

E := E210,110 =
 

1 a b c 0 0 0
0 0 1 d e 0 0
0 0 0 0 1 f g




There are four columns, 1, 2, 3, and 6 not of the form n+i−k−µi. Let G be a general
4-plane represented by a matrix in which these columns form a identity matrix

(2.7) G :=
 





1 0 0 ∗ ∗ 0 ∗
0 1 0 ∗ ∗ 0 ∗
0 0 1 ∗ ∗ 0 ∗
0 0 0 ∗ ∗ 1 ∗




 .

Let G(t) be this matrix with each entry ∗ scaled by t. Then

(2.8) det [ E
G(t)
] = ceg + t(∗c + · · · + ∗cef ) + t
2(∗ + · · · + ∗bef ) + t
3(∗f + ∗af ) ,

where each ∗ again represents a ﬁxed number.
When t = 0, the expression (2.8) becomes ceg. Let us investigate the consequences of
ceg = 0. If we set c = 0 in E210,110, we get E210,210 and if we set g = 0, we get E210,111,

E210,210 =
 

1 a b 0 0 0 0
0 0 1 d e 0 0
0 0 0 0 1 f g


 E210,111 =
 

1 a b c 0 0 0
0 0 1 d e 0 0
0 0 0 0 1 f 0



 .

(If e = 0, then the row operation R1 ← R1 − cR2 gives a matrix with c = 0, which lies in
E210,210.) This computation in local coordinates shows that

Y210,110 ∩ Y□G(0) = Y210,210 ∪ Y210,110 .

Now suppose that we have general 4 by 7 matrices G1, . . . , G6, G7, and we wish to solve
the instance of the simple Schubert problem (210, 110):

(2.9) det [ E
G1
] = · · · = det [ E
G6
] = det [ E
G7
] = 0 ,

where G7 is the matrix (2.7). Replacing G7 by G(t) gives a homotopy of 7 equations in the
coordinates a, . . . , g where 6 equations are ﬁxed (2.9) and one depends on t (2.8). When
t = 0, the latter becomes ceg = 0 and the system splits into subsystems on E210,210 and
E210,111 involving the matrices G1, . . . , G6. Numerical continuation along this homotopy
uses solutions to these smaller problems to obtain solutions to the system (2.9).

Write λ ⋖ ν if the components of the vector ν − λ are either 0 or 1, with exactly one 1.
For example, 110 ⋖ 210 and 110 ⋖ 111. Given partitions λ, µ, deﬁne the (n−k)-plane

Gµ := {ei | i ̸∈ {n−k+j−µj , for j = 1, . . . , k}} .

GALOIS GROUPS OF SCHUBERT PROBLEMS 11

Then if the non-zero entries of the matrix Eλ,µ are ai,j, we have

(2.10) det [Eλ,µ
Gµ
 ] =
 k∏

i=1 ai,n−k+i−µi ,

which is the product of the rightmost non-zero entries in the rows of Eλ,µ. This determi-
nant deﬁnes the charts Eλ,ν for µ ⋖ ν. A child problem for the simple Schubert problem
(λ, µ) is one of the form (λ, ν) with µ ⋖ ν.
The Pieri homotopy algorithm ﬁnds all solutions to a simple Schubert problem (λ, µ)
with ﬁxed (but general) (n−k)-planes G1, . . . , Gm where m + |λ| + |µ| = k(n−k). We
assume that we are given all solutions to all child problems (λ, ν) with µ ⋖ ν and the
(n−k)-planes are G1, . . . , Gm−1. If we let Gm(t) be a 1-parameter family of (n−k)-planes
with Gm(1) = Gm and Gm(0) = Gµ, then we obtain a homotopy

det [
Eλ,µ
G1
 ] = · · · = det [ Eλ,µ
Gm−1
] = det [ Eλ,µ
Gm(t)
] = 0 .

When t = 0 this is the disjunction of child problems and when t = 1, it is the problem we
wish to solve.
This method recursively ﬁnds solutions to parent problems given solutions to their
child problems. The depth of this recursion equals the dimension of the skew Schubert
variety corresponding to the simple Schubert problem we wish to solve, i.e., the number
of variables in the corresponding equations. The base case of this recursion is when
|λ| + |µ| = k(n−k), for then Eλ,µ is empty unless λi + µk+1−i = n−k for i = 1, . . . , k, and
in that case, Eλ,µ gives the k-plane spanned by {ei+λi | i = 1, . . . , k}.
These homotopies are optimal. This is because they only follow solutions to the given
Schubert problem and because the number d(λ, µ) of solutions to a simple Schubert prob-
lem satisﬁes the same recursion as the number of paths that are followed. Namely, if
|λ| + |µ| = k(n−k) then d(λ, µ) = 0 unless λi + µk+1−i = n−k for i − 1, . . . , k, and then
it equals 1. If |λ| + |µ| < k(n−k), then

d(λ, µ) = ∑

µ⋖ν d(λ, ν) .

Remark 2.4. We do not quite use the homotopy we just described, as the equations
involving t will in general have degree in t at least the minimum of k and n−k. Instead,
we use the convex combination of the equations

(2.11) γt det [
Eλ,µ
Gm
 ] + (1 − t) det [Eλ,µ
Gµ
 ] = 0 .

Here, γ ∈ C has norm 1, |γ| = 1. This has degree 1 in the homotopy parameter t.
Doing this, the intermediate solutions will not necessarily be solutions to the Schubert
problem, so we need to argue that this homotopy will remain optimal. For this, we appeal
a little to the geometry of the Grassmannian. The equations we use deﬁne hyperplane
sections of the Grassmannian in its Pl¨ucker embedding, and the number of solutions d(λ, µ)
to the Schubert problem turns out to be the degree of the variety Yλ,µ. Thus, replacing
a family of hyperplanes deﬁned by Schubert conditions (as in the Pieri homotopy) by

12 ANTON LEYKIN AND FRANK SOTTILE

an arbitrary pencil of hyperplanes (2.11) will still give an optimal homotopy between
solutions to the child problems and solutions to the parent problem.

3. Description of software

We divide the computation of the Galois group of a Schubert problem into three tasks.
(1) Compute the solutions of a general instance of the problem, called a master set.
(2) Use cheater homotopies to compute monodromy permutations of the master set.
(3) Determine the group generated by the monodromy permutations.
The ﬁrst task may be accomplished by the brute-force application of a polynomial
system solver. This is, however, ineﬃcient. In Table 1, we compare the number of
solutions to simple Schubert problems with λ = µ = □ to the number of homotopy paths
followed in polyhedral homotopies (as in the black-box solver of PHCpack). This is the
volume of the associated Newton polytope and was computed with Polymake [7]. This

k, n 2,6 2,7 2,8 2,9 2,10 2,11 3,6 3,7 3,8 4,6 4,7 5,7
solutions 14 42 132 429 1430 4862 42 462 6006 14 462 42
paths 18 67 248 919 3426 12843 130 3004 74645 42 7156 364
Table 1. Ineﬃciency of polyhedral homotopy for simple Schubert problems

shows that the Pieri homotopy algorithm is an eﬃcient alternative.
Subsection 3.1 discusses the second task.
The theory for the third task is beyond the scope of this paper. Based on preliminary
computations, we conjectured that the Galois group is always the full symmetric group,
and therefore we only check this. The fastest routine we have found to accomplish this is
the isNaturalSymmetricGroup function of GAP [6].
In Section 3.2, we discuss implementations of our algorithm. Implementations and
documentation of our computations are available at our website [16].

3.1. Computing monodromy permutations. Suppose that we have a master set of
solutions to the simple Schubert problem (λ, µ) on G(k, n), which is modeled by the system
of equations

(3.1) det [
Eλ,µ
G1
 ] = det [Eλ,µ
G2
 ] = · · · = det [Eλ,µ
Gm
 ] = 0 ,

where G1, . . . , Gm are ﬁxed (n−k)-planes. We follow these solutions along loops in the
space of m-tuples of (n−k)-planes to compute monodromy permutations.
The oﬀ-the-shelf homotopy continuation software we use requires that the equations are
linear in the homotopy parameter t, and so we follow piece-wise linear loops. For these,
we ﬁx all of the Gi except Gm, and exploit the linearity of the determinant in the row
vectors g1, . . . , gn−k of Gm. If g′
i is a vector not in Gm and we replace the row gi by the
convex combination (1 − t)gi + tg′
i, obtaining the pencil of planes Gm(t), then

det [ Eλ,µ
Gm(t)
] = (1 − t) det [
Eλ,µ
Gm
 ] + t det [ Eλ,µ
Gm(1)
]

= (1 − t)F (g1, . . . , gm) + tF (g1, . . . , g′
i, . . . , gm) .

GALOIS GROUPS OF SCHUBERT PROBLEMS 13

Replacing the equation in (3.1) involving Gm with this equation gives a linear homotopy
between the system (3.1) and one with Gm(1) in place of Gm.
Given a diﬀerent (n−k)-plane G′
m spanned by g′
1, . . . , g′
n−k, we use these vectors to
generate loops along which we can compute monodromy permutations. Suppose for il-
lustration that n−k = 3 and the vectors are [a, b, c] for Gm and [a
′, b
′, c′] for G′
m. The
diﬀerent pencils that we may create correspond to the edges of a cube.

[a
′, b
′, c′]
✟✟
✟ ❍❍
❍
[a
′, b
′, c] [a, b
′, c′][a
′, b, c′]

✟✟ ✟✟
 ❍❍
❍❍

❍
❍❍
❍
 ✟
✟✟
✟

[a
′, b, c] [a, b, c′][a, b
′, c]

❍
❍❍ ✟
✟✟

[a, b, c]

Our software oﬀers 3 strategies to generate loops.
• long loop goes from a vertex of the cube to its opposite and back,

[a, b, c] → [a
′, b, c] → [a
′, b
′, c] → [a
′, b
′, c′] →
→ [a, b
′, c′] → [a, b, c′] → [a, b, c] .

• short loop uses only a square,

[a, b, c] → [a
′, b, c] → [a
′, b
′, c] → [a, b
′, c] → [a, b, c] .

• half loop makes use of just one edge,

[a, b, c] 1
→ [a
′, b, c] γ
→ [a, b, c] ,

where the second homotopy is modiﬁed via a random number γ ∈ C,

Hγ := (1 − t)F (a
′, b, c) + γtF (a, b, c) .

While we do not oﬀer a proof that these loops will suﬃce to ﬁnd all non-trivial permu-
tations, we remark that they do suﬃce in the examples we considered.

Example 3.1. Suppose that we have the simple Schubert problem (□, □) on G(2, 4) as
given by (2.6) with

G1 = [ −55 − 8i 17 + 15i 40 + 99i −17 − 38i
−67 + 25i −82 − 55i −99 − 80i −21 − 85i

]

G2 = [ 66 + 53i −73 − 14i 85 + 5i 67 + 16i
−53 − 85i 36 − 25i 2 + 81i −58 + 35i

] .

Its solutions m1 and m2 are

m1 := [1 −0.23714 − .0028980i 0 0
0 0 1 −.51680 − .10520i

]

m2 := [1 .97009 + 1.2705i 0 0
0 0 1 .44336 + .38248i

]

14 ANTON LEYKIN AND FRANK SOTTILE

The short loop strategy with

G′ = [ 33 − 84i 21 − i 59 + 94i −94 + 89i
−15 − 19i 29i 79 + 51i 89 + 3i
 ]

creates a non-trivial monodromy permutation. The paths followed during the homotopies
are drawn in Figure 3, where the large circles are the values taken at the endpoints of the
diﬀerent homotopies.
 1

i

m1
 m2

First coordinate in position 1, 2
 −1
 i

2i

m1
 m2

Second coordinate in position 2, 4

Figure 3. Paths tracked in Example 3.1.

3.2. Implementation. We have two Maple implementations of our algorithms using the
package PHCmaple [17] to interface with PHCpack [33], which performs the numerical
polynomial homotopy continuation. PHCmaple produced the graphic of Figure 3. The
second implementation may alternatively call Bertini [1].
Our prototype implementation was carried out entirely in Maple to take advantage of
Maple packages to generate the equations and to manage the monodromy group, while
using the black-box solver in PHCpack to compute the master sets of solutions. The largest
problem this implementation could treat was the simple Schubert problem (210, 200) on
G(3, 7)—it showed that the Galois group is the full symmetric group S91. Previously, the
largest Schubert problem whose Galois group that was proven to be the full symmetric
group was the simple Schubert problem (20, 10) on G(2, 6) with 9 solutions [3].
Our second implementation also uses Maple and either PHCpack or Bertini. However,
it relies on the Pieri homotopy algorithm to compute master sets of solutions and GAP
to manage the monodromy groups, removing the two main computational bottlenecks
of the prototype. The largest problems this implementation has treated are (2100, □)
in G(4, 8) with 8580 solutions, (210, 210) in G(3, 8) with 10329 solutions and (210, 200)

GALOIS GROUPS OF SCHUBERT PROBLEMS 15

on G(3, 9) with 17589 solutions. It showed that all of these have Galois group equal to
the full symmetric group. The computation for the problem (□, □) on G(3, 8) with 6006
solutions is the basis of the Numerical Theorem.
We computed Galois groups of the simple Schubert problems (□, □) on all small Grass-
mannians, using the short loops strategy. They were run on several diﬀerent computers,
including an AMD Athlon 64 Dual Core Processor 4600+ with CPU clock speed of 2400
MHz and 1 GB of memory whose timings (using PHCpack) are reported in Table 2. These

k, n 2,4 2,5 2,6 2,7 2,8 2,9 2,10
solutions 2 5 14 42 132 429 1430
time 12s 27s 19s 51s 4.2m 20.5m 2.6h
permutations 4 6 5 6 7 4 7

k, n 3,5 3,6 3,7 3,8 3,9 4,6 4,7 4,8
solutions 5 42 462 6006 17589 14 462 8580
time 12s 35s 17.9m 18.6h 78.2h 15s 23.5m 44.5h
permutations 4 4 5 6 7 5 5 7
s := seconds, m := minutes, h := hours
Table 2. Timings of Galois group computation

reported times are not CPU times, but actual elapsed (wall clock) time, and so may ex-
ceed CPU time by 10 to 20 %. We also record the number of permutations we needed to
compute. The entry in G(3, 9) is the Schubert problem (210, 200) and the entry in G(4, 8)
is the Schubert problem (2100, □).
We ran some of these computations in Bertini. It was unable to compute examples in
more than 10 variables, and was markedly slower for the largest computations it com-
pleted, on G(2, 8), G(3, 7), and G(4, 7). On the other hand, Bertini provided an inde-
pendent veriﬁcation that the Galois groups were indeed the full symmetric groups. We
remark that Bertini is new software and its eﬃciency will likely improve.

4. Conclusions and Future work

This paper demonstrates the feasibility of homotopy continuation as tool to study the
Galois groups of enumerative problems. It also implicitly provides several challenges to
the numerical homotopy community. Perhaps the most serious is the current lack of
certiﬁability of computations in numerical homotopy software. While numerical methods
will increasingly outperform symbolic algorithms in algebraic geometry, they are currently
inferior in that their results do not come with certiﬁcation. Certiﬁcates for numerical com-
putations do exist in theory, for example in Shub and Smale’s [24] alpha-theory, and there
is a need for their implementation. In fact, even more reliable numerical techniques, such
as the interval step control proposed in [12], are sidestepped by homotopy continuation
software developers mostly due to the perceived complexity of implementation and the
expected slower performance in comparison with heuristic methods. Robust, oﬀ-the-shelf
software to handle polynomial systems that are not complete intersections is also needed
to deal with ideals in algebraic geometry, which are typically not complete intersections.

16 ANTON LEYKIN AND FRANK SOTTILE

Two further theoretical problems are not addressed in this paper. While the sampling
of the fundamental group of the base space provided by the loop-generating heuristics of
subsection 3.1 is suﬃcient to generate the Galois group in the examples we considered,
a better understanding of the topology of a complement of an algebraic variety in a
Grassmannian is needed to prove that this sampling is always suﬃcient. Second, we do
not know how to certify that the computed set of permutations generates the whole Galois
group, if it is not the full symmetric group.
The tools that we use could be applied more systematically to other problems in enu-
merative geometry. To this end, we plan a comprehensive project exploring the limit of
computability of Galois groups of Schubert problems along several fronts. This will involve
the software and algorithms described here—perhaps also incorporating HOM4PS [15].
We will also write parallel software implementing algorithms to compute Galois groups
of Schubert problems that are not compete intersections, as well as pushing the limits of
the symbolic methods of Billey and Vakil [3] and of Vakil’s combinatorial algorithm [32].
This will be a large and distributed computation as in [21] which should give a catalog of
the Galois groups of several tens of thousands of Schubert problems.

References

[1] Daniel J. Bates, Jonathan D. Hauenstein, Andrew J. Sommese, and Charles W. Wampler, Bertini:
Software for numerical algebraic geometry, Available at http://www.nd.edu/˜sommese/bertini.
[2] Daniel J. Bates, Chris Peterson, Andrew J. Sommese, and Charles W. Wampler, Numerical compu-
tation of the genus of an irreducible curve within an algebraic set, Preprint, 2007.
[3] S. Billey and R. Vakil, Intersections of Schubert varieties and other permutation array schemes,
Algorithms in Algebraic Geometry (A. Dickenstein, F.-O. Schreyer, and A. J. Sommese, eds.), IMA
Volumes in Mathematics and its Applications, vol. 146, Springer New York, 2007, pp. 21–54.
[4] C. I. Byrnes, Pole assignment by output feedback, Three Decades of Mathematical Systems Theory
(H. Nijmeijer and J. M. Schumacher, eds.), Lecture Notes in Control and Inform. Sci., vol. 135,
Springer-Verlag, Berlin, 1989, pp. 31–78.
[5] Wm. Fulton, Young tableaux, Cambridge University Press, Cambridge, 1997, With applications to
representation theory and geometry.
[6] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.4.9, 2006.
[7] Ewgenij Gawrilow and Michael Joswig, polymake: a framework for analyzing convex polytopes,
Polytopes—combinatorics and computation (Oberwolfach, 1997), DMV Sem., vol. 29, Birkh¨auser,
Basel, 2000, pp. 43–73.
[8] J. Harris, Galois groups of enumerative problems, Duke Math. J. 46 (1979), 685–724.
[9] B. Huber, F. Sottile, and B. Sturmfels, Numerical Schubert calculus, J. Symb. Comp. 26 (1998),
no. 6, 767–788.
[10] B. Huber and J. Verschelde, Pieri homotopies for problems in enumerative geometry applied to pole
placement in linear systems control, SIAM J. Control Optim. 38 (2000), no. 4, 1265–1287 (electronic).
[11] C. Jordan (ed.), Trait´e des substitutions, Gauthier-Villars, Paris, 1870.
[12] R. Baker Kearfott and Zhaoyun Xing, An interval step control for continuation methods, SIAM J.
Numer. Anal. 31 (1994), no. 3, 892–914.
[13] S. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
[14] S. Kleiman and D. Laksov, Schubert calculus, Amer. Math. Monthly 79 (1972), 1061–1082.
[15] T. Lee, T.Y. Li, and C. Tsai, Hom4ps-2.0: A software package for solving poly-
nomial systems by the polyhedral homotopy continuation method, Available at
http://www.math.msu.edu/˜li/Software.htm, 2007.

GALOIS GROUPS OF SCHUBERT PROBLEMS 17

[16] A. Leykin and F. Sottile, Galois groups of Schubert problems, 2007,
www.math.tamu.edu/~sottile/stories/Galois.
[17] A. Leykin and J. Verschelde, Interfacing with the numerical homotopy algorithms in PHCpack, Pro-
ceedings of ICMS 2006 (Nobuki Takayama and Andres Iglesias, eds.), 2006, pp. 354–360.
[18] A. Leykin, J. Verschelde, and Z. Yang, Parallel homotopy algorithms to solve polynomial systems,
Proceedings of ICMS 2006 (Nobuki Takayama and Andres Iglesias, eds.), 2006, pp. 225–234.
[19] T.-Y. Li, personal communication.
[20] T. Y. Li, Tim Sauer, and J. A. Yorke, The cheater’s homotopy: an eﬃcient procedure for solving
systems of polynomial equations, SIAM J. Numer. Anal. 26 (1989), no. 5, 1241–1251.
[21] J. Ruﬀo, Y. Sivan, E. Soprunova, and F. Sottile, Experimentation and conjectures in the real Schubert
calculus for ﬂag manifolds, Experiment. Math. 15 (2006), no. 2, 199–221.
[22] H. Schubert, Anzahl-Bestimmungen f¨ur lineare R¨aume beliebiger Dimension, Acta. Math. 8 (1886),
97–118.
[23] , Los¨ung des Charakteritiken-Problems f¨ur lineare R¨aume beliebiger Dimension, Mittheil.
Math. Ges. Hamburg (1886), 135–155, (dated 1885).
[24] M. Shub and S. Smale, Complexity of B´ezout’s Theorem I: Geometric Aspects, J. the American
Mathematical Society 6 (1993), no. 2, 459–501.
[25] A. Sommese, J. Verschelde, and C. Wampler, Introduction to numerical algebraic geometry, Graduate
School on Systems of Polynomial Equations: From Algebraic Geometry to Industrial Applications.
14-25 July 2003, Buenos Aires, Argentina (A. Dickenstein and I. Emiris, eds.), INRIA, 2003, A
revised collection of the course notes is scheduled to be published by Springer–Verlag, pp. 229–247.
[26] A. Sommese and C. Wampler, The numerical solution of systems of polynomials, World Scientiﬁc
Publishing Co. Pte. Ltd., Hackensack, NJ, 2005, Arising in engineering and science.
[27] F. Sottile, Pieri’s formula via explicit rational equivalence, Canad. J. Math. 49 (1997), no. 6, 1281–
1298.
[28] , Some real and unreal enumerative geometry for ﬂag manifolds, Michigan Math. J. 48 (2000),
573–592, Dedicated to William Fulton on the occasion of his 60th birthday.
[29] , Elementary transversality in the Schubert calculus in any characteristic, Michigan Math. J.
51 (2003), no. 3, 651–666.
[30] Richard P. Stanley, Some combinatorial aspects of the Schubert calculus, Combinatoire et
repr´esentation du groupe sym´etrique (Actes Table Ronde CNRS, Univ. Louis-Pasteur Strasbourg,
Strasbourg, 1976), Springer, Berlin, 1977, pp. 217–251. Lecture Notes in Math., Vol. 579.
[31] R. Vakil, A geometric Littlewood-Richardson rule, Ann. of Math. (2) 164 (2006), no. 2, 371–421,
Appendix A written with A. Knutson.
[32] , Schubert induction, Ann. of Math. (2) 164 (2006), no. 2, 489–512.
[33] J. Verschelde, Algorithm 795: PHCpack: A general-purpose solver for polynomial systems by ho-
motopy continuation, ACM Trans. Math. Softw. 25 (1999), no. 2, 251–276, Software available at
http://www.math.uic.edu/~jan.

Institute for Mathematics and its Applications, University of Minnesota, Minneapolis,
MN 55455, USA
E-mail address: leykin@ima.umn.edu
URL: http://www.ima.umn.edu/~leykin/

Department of Mathematics, Texas A&M University, College Station, Texas 77843,
USA
E-mail address: sottile@math.tamu.edu
URL: http://www.math.tamu.edu/~sottile/
