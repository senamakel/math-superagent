<!-- source: https://arxiv.org/pdf/2007.05480 | converted from PDF -->

arXiv:2007.05480v3  [math.NT]  8 Jan 2025
Additive and geometric transversality of fractal sets
in the integers

Daniel Glasscock Joel Moreira Florian K. Richter

January 9, 2025

Abstract

By juxtaposing ideas from fractal geometry and dynamical systems, Furstenberg pro-
posed a series of conjectures in the late 1960’s that explore the relationship between digit
expansions with respect to multiplicatively independent bases. In this work, we introduce
and study – in the discrete context of the integers – analogues of some of the notions and
results surrounding Furstenberg’s work. In particular, we deﬁne a new class of fractal
sets of integers that parallels the notion of ×r-invariant sets on the 1-torus and investi-
gate the additive and geometric independence between two such fractal sets when they
are structured with respect to multiplicatively independent bases. Our main results in
this direction parallel the works of Furstenberg, Hochman-Shmerkin, Shmerkin, Wu, and
Lindenstrauss-Meiri-Peres and include:
• a classiﬁcation of all subsets of the positive integers that are simultaneously ×r-
and ×s-invariant;
• integer analogues of two of Furstenberg’s transversality conjectures pertaining to the
dimensions of the intersection A ∩ B and the sumset A + B of ×r- and ×s-invariant
sets A and B when r and s are multiplicatively independent; and
• a description of the dimension of iterated sumsets A+A+· · ·+A for any ×r-invariant
set A.
We achieve these results by combining ideas from fractal geometry and ergodic theory
to build a bridge between the continuous and discrete regimes. For the transversality
results, we rely heavily on quantitative bounds on the Lq-dimensions of projections of
restricted digit Cantor measures obtained recently by Shmerkin. We end by outlining a
number of open questions and directions regarding fractal subsets of the integers.

Contents

1 Introduction 2
1.1 Preview of the main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 History and context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.3 Main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 Overview of the paper . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.5 Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2 Sums and intersections of multiplicatively invariant subsets of the reals 12
2.1 Fractal geometry of sets and measures in Euclidean space . . . . . . . . . . . . . . . . . . 12
2.2 Multiplicatively invariant sets and restricted digit Cantor sets . . . . . . . . . . . . . . . . 16
2.3 A uniform Frostman exponent projection theorem . . . . . . . . . . . . . . . . . . . . . . 17
2.4 Geometric transversality in the reals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.5 Additive transversality of sumsets in the reals . . . . . . . . . . . . . . . . . . . . . . . . 22
3 Discrete fractal geometry and multiplicatively invariant subsets of the integers 25
3.1 Notions of dimension for subsets of integers . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.2 Dimension regularity of multiplicatively invariant sets . . . . . . . . . . . . . . . . . . . . 28

1

3.3 Connections to symbolic dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.4 Connections to fractal geometry of the reals . . . . . . . . . . . . . . . . . . . . . . . . . 34
4 Transversality between multiplicatively invariant subsets of the integers 36
4.1 Sets which are simultaneously multiplicatively invariant . . . . . . . . . . . . . . . . . . . 36
4.2 Intersections of multiplicatively independent invariant sets . . . . . . . . . . . . . . . . . . 37
4.3 Sums of multiplicatively independent invariant sets . . . . . . . . . . . . . . . . . . . . . 39
4.4 An example that shows R-invariance does not suﬃce . . . . . . . . . . . . . . . . . . . . . 43
4.5 Iterated sums of a multiplicatively invariant set . . . . . . . . . . . . . . . . . . . . . . . 45
5 Open directions 46
5.1 Positive density for sumsets of full dimension . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.2 Small intersections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.3 Diﬀerence sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.4 Analogous results for other notions of discrete dimension . . . . . . . . . . . . . . . . . . . 48
5.5 Polynomial functions of multiplicatively invariant sets . . . . . . . . . . . . . . . . . . . . 49
5.6 Multiplicatively invariant sets in relation to other arithmetic sets in the integers . . . . . . 49
5.7 Transversality of multiplicatively invariant sets in the rs-adics . . . . . . . . . . . . . . . . 50

1. Introduction

Number theorists in the ﬁrst half of the 20th century were among the ﬁrst to consider the
degree to which base 2 and base 3 representations of real numbers are independent. An open
conjecture attributed to Mahler [MF] postulates, for example, that if (an)∞
n=1 ⊆ {0, 1} is
not eventually periodic, then at least one of the numbers ∑∞
n=1 an2−n and ∑∞
n=1 an3−n is
transcendental. In a diﬀerent vein, Cassels [Cas] and Schmidt [Sch], answering a question of
Steinhaus about Cantor’s middle thirds set C, proved that almost every number in C/2 (with
respect to the log 2/ log 3-dimensional Hausdorﬀ measure) is normal to every base which is
not a power of 3. More general questions along these lines – is almost every real number with
respect to any continuous ×3-invariant measure on [0, 1] normal to every base that is not a
power of 3 – remain open, despite considerable partial progress [Hos, Lin, HS2].
Studying the independence between diﬀerent representations of real numbers remains
an active area of research that brings together results and techniques from number theory,
ergodic theory, and geometric measure theory. Parallel investigations concerning represen-
tations of integers appear to be less developed but are no less natural or interesting. It is
the purpose of this paper to advance those investigations by demonstrating various forms of
independence between diﬀerent base representations in the non-negative integers. One of the
basic principles that underpin our results in this direction states the following:

If r and s are multiplicatively independent positive integers (meaning that the
quantity log(r)/ log(s) is irrational) and A and B are subsets of the non-negative
integers that are structured with respect to base-r and base-s representations, re-
spectively, then A and B lie in general position.

The following unresolved conjecture of Erd˝os [Erd] exempliﬁes this heuristic: for all n ⩾ 9, it
is impossible the express the number 2n in base 3 using only the digits 0 and 1; see [DW, Lag]
for some recent progress. Today, Erd˝os’ conjecture is understood as merely a special case of
a much broader conjecture that asserts that any inﬁnite set of natural numbers that has a
“simple” description in base r must have a “complex” description in base s (see Question 5.2
in Section 5.2 for more details). A related folklore conjecture in number theory [Inc] posits
that {0, 1, 82000} is exactly the set of non-negative integers that can be written in bases 2, 3,

4, and 5 using only the digits 0 and 1. A partial answer to this was given recently by Burrell
and Yu [BY], who proved that the set A of non-negative integers that can be written in bases
4 and 5 using only the digits 0 and 1 satisﬁes ∣
∣A ∩ [0, N ]
∣
∣ ⩽ CεN ε for all ε > 0.
In this paper, we aim to 1) introduce a family of multiplicatively structured “fractal”
subsets of the non-negative integers that naturally arise from digit restrictions, and 2) inves-
tigate the transversality, or independence, between members of that family that are structured
with respect to multiplicatively independent bases. Our investigation is strongly motivated
by the heuristic and conjectures mentioned above and by the recent resolutions of a pair of
Furstenberg’s conjectures concerning notions of geometric and additive transversality of frac-
tal subsets of the reals. Our results give integer parallels of those advancements in the reals,
generalize the aforementioned result of Burrell and Yu, and make progress toward Erd˝os’
conjecture.
Before recounting the relevant history and stating our main results in full generality, we
focus our attention on the special case of restricted digit Cantor sets in the non-negative
integers. Although restricted digit Cantor sets comprise only a small subclass of the sets that
we consider, most of our results are already novel and interesting for this class. In this sense,
the following section serves as a preview of our main results.

1.1. Preview of the main results

Let N = {1, 2, 3, . . .} and N0 = {0, 1, 2, . . .}. An integer base-r restricted digit Cantor set is
a set of non-negative integers whose base-r expansion includes only digits from a ﬁxed set
D ⊆ {0, 1, . . . , r − 1}, i.e., { n∑

i=0 airi ∣
∣
∣
∣
∣ n ∈ N0, a0, . . . , an ∈ D
}
 . (1.1)

The (mass) dimension of such a set A is dim A := log |D|/ log r, in the sense that |A∩[0, N )| =
N dim A+o(1). We discuss notions of dimension for more general subsets of the non-negative
integers in the next section and deﬁne them precisely in (1.12) and Deﬁnition 3.1. While
a number of arithmetic properties of integer restricted digit Cantor sets are well studied –
divisibility [BS], distribution in arithmetic progressions [EMS, Kon], number of prime factors
[KMS], character sums [BCS] – much less appears to be known about the relationship between
such sets when they are structured with respect to diﬀerent bases.
Let r and s be multiplicatively independent positive integers, and let A, B ⊆ N0 be base-r
and base-s restricted digit Cantor sets, respectively. Under these assumptions, our results
demonstrate that the sets A and B are transverse both in a geometric / probabilistic sense
and in an additive combinatorial sense. More precisely, the sets A and B are
• geometrically / probabilistically in general position, in the sense that neither A nor B
contains the other and in the sense that the size of A ∩ B is at most what is expected
if A and B were independent random sets;
• additive combinatorially disjoint, in the sense that the cardinality of the sumset A + B
is nearly as large as possible, and hence there are only very few coincidences amongst
the sums a + b for a ∈ A and b ∈ B.
Our main Theorems A and B address the ﬁrst point, while Theorem C addresses the sec-
ond. We move now to formulate corollaries of those theorems that clearly demonstrate these
notions of independence.
 3

To describe all of the elements of a non-trivial base-5 restricted digit Cantor set in base 17,
all 17 digits are required. The following corollary of Theorem A generalizes this observation by
showing that restricted digit Cantor structures with respect to multiplicatively independent
bases are mutually incompatible. It also provides an integer analogue of a well-known theorem
of Furstenberg; see Theorem 1.1 below.

Corollary of Theorem A. Under the assumptions on the sets A and B above, if A ⊆ B,
then either A = {0} or B = N0.

The ﬁner question about the size of the intersection A ∩ B is addressed in Theorem B.
For N ∈ N, deﬁne AN = A ∩ [0, N ) and BN = B ∩ [0, N ). The sets AN and BN would be
probabilistically independent if ∣
∣AN ∩ BN ∣
∣/N = ∣
∣AN ∣
∣
∣
∣BN ∣
∣/N 2. Examples show that the sets
A and B can be disjoint, even in the case that both A and B have a large set of allowed
digits, so the inequality ∣
∣AN ∩ BN ∣
∣

N ≪
 ∣
∣AN ∣
∣

N ·
 ∣
∣BN ∣
∣

N (1.2)

for all N large can be understood to demonstrate a type of asymptotic probabilistic transver-
sality between the sets A and B. (As explained in the next section, such an inequality can
also be interpreted as AN and BN being geometrically in general position.) Theorem B shows
that (1.2) holds up to a factor of N ε; the precise extent to which (1.2) holds remains open
and is addressed brieﬂy in Section 5.2.

Corollary of Theorem B. Under the assumptions on the sets A and B above, for all ε > 0
and all suﬃciently large N ,
• if dim A + dim B ⩾ 1, then
∣
∣AN ∩ BN ∣
∣

N ⩽ N ε ·
 ∣
∣AN ∣
∣

N ·
 ∣
∣BN ∣
∣

N ;

• if dim A + dim B < 1, then ∣
∣AN ∩ BN ∣
∣ ⩽ N ε.

As an example application, let C4,{0,1} and C5,{0,1} be the sets of non-negative integers
that have only digits 0 and 1 in their base 4 and 5 expansions, respectively. Since log 2/ log 4+
log 2/ log 5 < 1, it follows that ∣
∣C4,{0,1} ∩ C5,{0,1}∣
∣ = o(N ε), which recovers the theorem of
Burrell and Yu’s mentioned in the previous section.
If X and Y are ﬁnite sets of real numbers, then it is easy to check that

|X| + |Y | − 1 ⩽ |X + Y | ⩽ |X||Y |.

Equality holds on the left if and only if X and Y are arithmetic progressions of the same
step size. When |X + Y | is near this lower bound, inverse theorems in combinatorial number
theory (e.g. [TV, Ch. 5]) provide additive structural information on the sets X and Y . At
the other end of the spectrum, equality holds on the right if and only if none of the sums
x + y, with x ∈ X and y ∈ Y , coincide. In this case, the sets X and Y lie in general position
from an additive combinatorial point of view.
In this context, the inequality
∣
∣AN + BN ∣
∣ ≫ min (N, ∣
∣AN ∣
∣ · ∣
∣BN ∣
∣
) (1.3)

4

can be understood as demonstrating additive combinatorial transversality between the sets
AN and BN . Theorem C shows that (1.3) holds up to a factor of N ε; the extent to which
(1.3) holds is unknown and is discussed brieﬂy in Section 5.1.

Corollary of Theorem C. Under the assumptions on the sets A and B above, for all ε > 0
and all suﬃciently large N ,
∣
∣AN + BN ∣
∣ ⩾ min (N, ∣
∣AN ∣
∣ · ∣
∣BN ∣
∣
)∕
N ε.

Theorems A, B, and C are more general than the corollaries above might suggest. Indeed,
each result applies not only to restricted digit Cantor sets, but to a wider class of integer
fractal sets called multiplicatively invariant sets. Moreover, each set can be replaced by a
rounded image of itself under any aﬃne transformation of R. Finally, in Theorem C, the
sets A and B can be replaced by arbitrary subsets of A and B, and set cardinality can
be replaced with a notion of discrete Hausdorﬀ content. We will introduce multiplicatively
invariant sets in Section 1.3 and state our main results precisely there, after providing some
historical context and motivation for them in the next section.

1.2. History and context

In the language of fractal geometry and dynamical systems, Furstenberg [Fur1, Fur2] estab-
lished a number of conjectures and results that explore the relationship between multiplicative
structures with respect to diﬀerent bases in the real numbers. The notion of structure particu-
larly relevant to this work is that of multiplicative invariance: a set X ⊆ [0, 1] is ×r-invariant
if it is closed and TrX ⊆ X, where Tr : [0, 1] → [0, 1] denotes the map

Tr : x ↦→ rx mod 1.

We call a set X ⊆ [0, 1] multiplicatively invariant if it is ×r-invariant for some r ⩾ 2.
One of Furstenberg’s ﬁrst and most well-known results concerning multiplicatively invari-
ant sets is the following theorem, the measure-theoretic analogue of which is the ×2, ×3
conjecture, a central open problem in ergodic theory.

Theorem 1.1 ([Fur1, Theorem 4.2]). If X ⊆ [0, 1] is simultaneously ×2- and ×3-invariant,
then either X is ﬁnite or X = [0, 1].

The numbers 2 and 3 in Theorem 1.1 can be replaced by any pair of multiplicatively
independent positive integers r and s. Following Theorem 1.1, Furstenberg conjectured that
if X, Y ⊆ [0, 1] are ×r- and ×s-invariant, respectively, then X and Y are transverse in
more than one sense, some of which are made precise below. While some of Furstenberg’s
“transversality conjectures” remain open, two of them were resolved recently by Hochman and
Shmerkin [HS1], Shmerkin [Shm], and, independently, Wu [Wu]. Both of these conjectures
are particularly relevant to this work, so we will expound on them further now.
In Euclidean geometry, linear subspaces U, V ⊆ Rd are said to be in general position (or
transverse) if
 dim(U ∩ V ) = max (0, dim U + dim V − d
), and

dim(U + V ) = min ( dim U + dim V, d
).

5

By analogy, Furstenberg conjectured1 that if r and s are multiplicatively independent and X
and Y are ×r- and ×s-invariant subsets of [0, 1], then

dimH(X ∩ Y ) ⩽ max (0, dimH X + dimH Y − 1
), and (1.4)

dimH(X + Y ) = min ( dimH X + dimH Y, 1
), (1.5)

where dimH denotes the Hausdorﬀ dimension.
With no assumptions on the sets X, Y ⊆ [0, 1], it is not diﬃcult to ﬁnd examples for which
neither (1.4) nor (1.5) hold. Nevertheless, it is a consequence of Marstrand’s projection and
slicing theorems2 that for all Borel sets X and Y , the typical dilated sets λX and ηY are
transverse in the sense of (1.4) and (1.5).

Theorem 1.2 ([Mar, Theorems II and III]). Let X and Y be Borel subsets of [0, 1]. For
Lebesgue-a.e. λ, η, σ ∈ R,

dimH (λX ∩ (ηY + σ)
) ⩽ max (0, dimH(X × Y ) − 1
), and (1.6)

dimH (λX + ηY ) = min ( dimH(X × Y ), 1
). (1.7)

In this context, Furstenberg’s conjectures in (1.4) and (1.5) say that the multiplicative
invariance of the sets X and Y can be leveraged to change the result in Marstrand’s theorem
from concerning the typical sets λX ∩ (ηY + σ) and λX + ηY to concerning the speciﬁc ones
X ∩ Y and X + Y . In fact, Furstenberg conjectured that for ×r- and ×s-invariant sets X
and Y , the inequality in (1.6) and equality in (1.7) hold for all non-zero λ and η and all
σ. Hochman and Shmerkin resolved the sumset conjecture by proving a stronger result for
multiplicatively invariant measures, and several years later Shmerkin [Shm] and Wu [Wu]
independently resolved the intersection conjecture. (These works resolved both conjectures
for classes of attractors of iterated function systems, too.) Several more recent works oﬀer
new proofs of (1.4) and (1.5); see, for example, [Aus, Yu4, JR, GMR].

Theorem 1.3 ([Shm, Wu] and [HS1]). Let r and s be multiplicatively independent positive
integers, and let X, Y ⊆ [0, 1] be ×r- and ×s-invariant sets, respectively. For all λ, η ∈ R\{0}
and all σ ∈ R,
 dimM (λX ∩ (ηY + σ)
) ⩽ max (0, dimH X + dimH Y − 1
), and (1.8)

dimH (λX + ηY ) = min ( dimH X + dimH Y, 1
), (1.9)

where dimM denotes the upper Minkowski dimension.

The upper bound on the dimension of ﬁbers in (1.8) suﬃces to give the lower bound on
the dimension of sumsets necessary for (1.9), as was observed in [Fur3]; for elaboration on the
connection between the two, see the discussion following Conjecture 1.2 in [HS1]. Shmerkin’s
main result in [Shm], which concerns the decay of Lq norms of certain self-similar measures

1The intersection conjecture (1.4) is one of several conjectures stated in [Fur2]. The sumset conjecture
(1.5) does not, as far as we are aware, appear by Furstenberg in print, but it was known to have originated
with him.
2Marstrand’s slicing and projection theorems originally concerns orthogonal projections of subsets of the
plane and intersections with lines. Images of the Cartesian product X × Y under orthogonal projections are,
up to aﬃne transformations which preserve dimension, sumsets of the form λX + ηY , while intersections of
X × Y with lines are aﬃnely equivalent to sets of the form λX ∩ (ηY + σ). Also note that for suﬃciently
regular sets X and Y , dimH(X × Y ) = dimH X + dimH Y ; see, for example, [Mat, Corollary 8.11].

6

of dynamical origin, proves (1.8) by controlling the Frostman exponent of images of regular
measures under projections. We derive a number of our main theorems from Shmerkin’s
work, which we elaborate on further in Section 2.3.
In an eﬀort to better understand the role that the multiplicative independence between
the bases plays in the sumset theorem, it is natural to ask about the sum of sets that are all
structured with respect to the same base r. Taking X ⊆ [0, 1] to be those numbers that can
be written in decimal with only the digits 0, 1, and 2, we see that the equality in (1.5) need
not hold:
 log 5
log 10 = dimH(X + X) < 2 dimH X = 2 log 3
log 10 .

Nevertheless, it is a consequence of the following theorem of Lindenstrauss, Meiri, and Peres
that the dimension of the iterated sumset X+· · ·+X approaches 1 as the number of summands
increases.

Theorem 1.4 ([LMP, Corollary 1.2]). Let (Xi)∞
i=1 be a sequence of ×r-invariant subsets of
[0, 1]. If ∑∞
i=1 dimH Xi/| log dimH Xi| diverges, then

lim
n→∞ dimH (X1 + · · · + Xn) = 1.

This theorem demonstrates that the structure captured by multiplicative invariance sits
transversely to the additive structure captured by additive closure: because the sumset
X1 + · · · + Xn ﬁlls out the entire space (with respect to the Hausdorﬀ dimension), the sets
Xi are not contained in an additively closed set of dimension less than 1. Dimension growth
of iterated sumsets under weaker regularity conditions was studied recently in [FHY].

While there is a strong historical precedent for the study of ×r-invariant subsets of the
unit interval, less seems to be known in the integer and p-adic settings, despite the fact that
many of the same objects and questions can be naturally formulated there.
Furstenberg [Fur2], assuming a positive answer to one of his yet-unresolved transversality
conjectures in the reals, drew a connection between the real and integer regimes by showing
that given any ﬁnite word from the alphabet {0, . . . , 9}, the decimal expansion of the number
2n contains that word provided that n is suﬃciently large. This (conditionally) solves an
analogue of Erd˝os’ conjecture mentioned earlier.
The folklore conjecture mentioned in the second paragraph in Section 1 is proﬁtably
understood in terms of intersections of restricted digit Cantor sets and, as such, evokes the
real transversality conjecture of Furstenberg in (1.4). Burrell and Yu’s [BY] results toward a
resolution of this conjecture rely heavily on Yu’s work in [Yu4] on improvements to Shmerkin
and Wu’s resolution of Furstenberg’s intersection conjecture. Drawing on results in [Yu4],
Yu [Yu1] also shows that there are few solutions to the equation x + y = z in which the
variables come from diﬀerent integer restricted digit Cantor sets. Using projection theorems
and Newhouse’s gap lemma, Yu [Yu3] furthermore proves that there are inﬁnitely many sums
of powers of ﬁve that can be written as sums of powers of three and four.
The ﬁrst author proved in [Gla, Theorem 1.4] a discrete analogue of Marstrand’s projec-
tion theorem, building on the work of Lima and Moreira in [LM1]: for all A, B ⊆ Z satisfying

7

a necessary dimension condition 3 and for Lebesgue-a.e. (λ, η) ∈ R2,

dimM (
⌊λA + ηB⌋
) = min (dimM (A × B), 1
), (1.10)

where the upper mass dimension, dimM , is deﬁned in (1.12) below, ⌊ · ⌋ denotes the ﬂoor
function, and ⌊λA + ηB⌋ := {
⌊λa + ηb⌋ ∣
∣ a ∈ A, b ∈ B}
. It is reasonable to conjecture
by analogy that if A and B are restricted digit Cantor sets with respect to multiplicatively
independent bases, then (1.10) would hold for all non-zero λ, η ∈ R. We show that this is
indeed the case in Theorem C and its generalizations.

1.3. Main results

Our primary goals for this article are to introduce the study of multiplicatively invariant
subsets of the non-negative integers and to bring transversality results in the integers more
in line with those in the reals by giving full-ﬂedged analogues of Theorems 1.1, 1.3, and 1.4.
To that end, we begin by introducing an analogue of a ×r-invariant set for the integers.
Let r ∈ N, r ⩾ 2. Deﬁne Rr : N0 → N0 and Lr : N0 → N0 by

Rr : n ↦→ ⌊n/r⌋ and Lr : n ↦→ n − rk⌊n/rk⌋,

where k = ⌊log n/ log r⌋ when n ⩾ 1. The maps Rr and Lr are best understood using the
base-r representations of non-negative integers: if n = akrk + · · · + a1r + a0, ak ̸= 0, is the
base-r representation of n, then

Rr(n) = akrk−1 + · · · + a2r + a1 and Lr(n) = ak−1rk−1 + · · · + a1r + a0.

In other words, the map Rr “forgets” the least signiﬁcant digit (the right-most digit, hence
the letter R) while the map Lr “forgets” the most signiﬁcant digit (the left-most digit, hence
the letter L) in base r. For example, in base r = 10 we have R10(71393) = 7139 and
L10(71393) = 1393.

Deﬁnition 1.5. A set A ⊆ N0 is ×r-invariant if Rr(A) ⊆ A and Lr(A) ⊆ A. We call A ⊆ N0
multiplicatively invariant if it is ×r-invariant for some r ⩾ 2.

It may be helpful to note that a ×r-invariant set A need not satisfy rA ⊆ A and that there
are examples showing that the condition rA ⊆ A does not yield a natural integer analogue
of the notion of ×r-invariance on the unit interval; see Section 4.4.
There are many natural examples of ×r-invariant subsets of N0. Integer base-r restricted
digit Cantor sets, deﬁned in (1.1), are clearly ×r-invariant. More general examples arise
from symbolic subshifts of {0, 1, . . . , r − 1}N0. For any closed and left-shift-invariant set
Σ ⊆ {0, 1, . . . , r − 1}N0 , the corresponding language set is deﬁned by

L(Σ) = {w0w1 · · · wk ∣
∣ w0w1 · · · ∈ Σ, k ∈ N0}.

Any language set naturally embeds in two ways into the non-negative integers as
{
w0rk + · · · + wk−1r + wk ∣
∣ w0w1 · · · wk ∈ L(Σ)
}
,
{
wkrk + · · · + w1r + w0 ∣
∣ w0w1 · · · wk ∈ L(Σ)
},

3The condition is that the upper mass dimension of A × B is equal to the upper counting dimension of
A × B. The upper mass dimension is deﬁned in (1.12), while the upper counting dimension of A × B is equal
to lim supN→∞ maxz∈Z2 log ∣
∣(A × B) ∩ (z + {−N, . . . , N }
2)∣
∣
∕ log N .

8

yielding sets that are ×r-invariant. For more details, see Deﬁnition 3.9 and Proposition 3.10,
and for more such examples, see Examples 3.12. As yet another source of ×r-invariant subsets
of the non-negative integers, we note that if X is a ×r-invariant subset of [0, 1], then the set
⋃

k∈N0
 {⌊rkx⌋ ∣
∣ x ∈ X}

can be shown to be ×r-invariant; see Section 3.4 for more details.
Our ﬁrst result in the integer setting is an analogue of Theorem 1.1 that demonstrates that
there are no non-trivial examples of sets which exhibit structure simultaneously with respect
to multiplicatively independent bases. Theorem A is proved in Section 4.1 by expanding on
the well-known argument that all non-zero decimal digits appear as the most signiﬁcant digit
of 2n. We deﬁne [X]δ := {z ∈ R | ∃x ∈ X with |z − x| ⩽ δ} to be the δ-neighborhood of the
set X.

Theorem A. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant sets, respectively. If λ, η > 0, σ, τ ∈ R and δ > 0 are such that

λA + τ ⊆ [ηB + σ]
δ, (1.11)

then either A is ﬁnite or B = N0.

To measure the size of multiplicatively invariant subsets of N0 and their sumsets and
Cartesian products, we make use of two notions of dimension in the integers that parallel
the classical Minkowski and Hausdorﬀ dimensions from geometric measure theory. The dis-
crete analogue of the lower and upper Minkowski dimension are the lower and upper mass
dimension, deﬁned for A ⊆ Nd
0 as

dimM A = lim inf
N →∞ log |A ∩ [0, N )d|
log N = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim inf
N →∞
 ∣
∣A ∩ [0, N )d∣
∣

N γ > 0

}
 ,

dimM A = lim sup
N →∞
 log |A ∩ [0, N )d|
log N = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim sup
N →∞
 ∣
∣A ∩ [0, N )d∣
∣

N γ > 0

}
 . (1.12)

Whenever dimM A = dimM A, we say that the mass dimension of A exists and denote it by
dimM A. In analogy to the way in which the classical Hausdorﬀ dimension can be deﬁned
in terms of the unlimited Hausdorﬀ content (see Section 2.1), the lower and upper discrete
Hausdorﬀ dimension of A are deﬁned to be

dimH A = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim inf
N →∞ Hγ
⩾1(A ∩ [0, N )d)

N γ > 0

}
 ,

dimH A = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim sup
N →∞
 Hγ
⩾1(A ∩ [0, N )d)

N γ > 0

}
 ,

where the discrete γ-Hausdorﬀ content, Hγ
⩾1, is deﬁned in Deﬁnition 2.2. If these two quan-
tities agree then we say that the discrete Hausdorﬀ dimension of A, dimH A, exists and is
equal to this quantity.
The mass dimension and the upper discrete Hausdorﬀ dimension are systematically stud-
ied along with a host of other discrete dimensions in [BT2]. We discuss these notions of

9

dimension and the interplay between them at greater length in Section 3.1. For the current
discussion, it is helpful to know that

dimH ⩽ dimM ⩽ dimM and dimH ⩽ dimH ⩽ dimM ,

and that for any ×r-invariant set A ⊆ N0, both the mass dimension dimM A and the discrete
Hausdorﬀ dimension dimH A exist and coincide; see Proposition 3.6.
Our next main results in the integer setting demonstrate geometric and additive combi-
natorial transversality between ×r- and ×s-invariant subsets of integers. Thus, these results
parallel the results of Hochman and Shmerkin, Shmerkin, and Wu by verifying analogues of
Furstenberg’s intersection and sumset conjectures.
Let r and s be multiplicatively independent positive integers, and let A, B ⊆ N0 be ×r-
and ×s-invariant sets, respectively. Deﬁne γ = max (0, dimH A + dimH B − 1
). (In what
follows, recall the use of the ﬂoor notation ⌊ · ⌋ described just after (1.10) above.)

Theorem B. For all ε, λ, η > 0, σ, τ ∈ R, and suﬃciently large N ∈ N,
∣
∣⌊λ
(A ∩ [0, N )
) + τ ⌋ ∩ ⌊η(B ∩ [0, N )
) + σ⌋
∣
∣ ⩽ N γ+ε.

In particular, for all λ, η > 0 and σ, τ ∈ R,

dimM (⌊λA + τ ⌋ ∩ ⌊ηB + σ⌋
) ⩽ max (0, dimH A + dimH B − 1
).

The upper bound on the dimension of the set ⌊λA + τ ⌋ ∩ ⌊ηB + σ⌋ in Theorem B provides
an analogue in the integers to the result of Shmerkin and Wu in (1.8) in the reals. Theorem B
will be derived as a corollary of Theorem 4.3, a stronger result proved in Section 4.2 in which
we demonstrate that the upper bound on ∣
∣⌊λ(A∩ [0, N )
)+ τ ⌋∩ ⌊η(
B ∩ [0, N )
) + σ⌋
∣
∣ is uniform
over a compact set of scaling parameters.
Our next theorem gives an integer analogue of the result of Hochman and Shmerkin in
(1.9). We bound both the cardinality and the discrete Hausdorﬀ content of the set ⌊λA′+ηB′⌋
from below in terms of the cardinality and the discrete Hausdorﬀ content of the product set
A′ × B′, where A′ and B′ are arbitrary subsets of A and B. Note that dimH(A × B) =
dimH A + dimH B holds because A and B are multiplicatively invariant (see Corollary 3.8),
but this equality need not hold for arbitrary subsets A′ ⊆ A and B′ ⊆ B. Hence, the role
played by dimH A + dimH B in Theorem B is now played by dimH(A′ × B′) in this next result.

Theorem C. For all ε, λ, η > 0, γ ∈ [0, 1], suﬃciently large N and non-empty A′ ⊆ A∩[0, N ),
B′ ⊆ B ∩ [0, N ),
 ∣
∣⌊
λA
′ + ηB′⌋∣
∣ ⩾ |A′ × B′|
N γ+ε , and

Hγ
⩾1(⌊λA′ + ηB′⌋)

N γ ≫ε,λ,η,γ Hγ+γ+ε
⩾1 (A′ × B′)

N γ+γ+ε .

In particular, for all dim ∈ {dimM , dimM , dimH , dimH },

dim (⌊λA + ηB⌋
) = min (
1, dim(A × B)
),

and, if dimH A + dimH B ⩽ 1, then for all A′ ⊆ A, B′ ⊆ B,

dim (⌊λA
′ + ηB′⌋
) = dim (
A
′ × B′)
.

10

Just as with Theorem B, we derive Theorem C from a more general result, Theorem 4.6
proved in Section 4.3, which demonstrates that the inequalities in Theorem C hold uniformly
over the scaling parameters λ and η. Both Theorem B and Theorem C are proved by combing
the uniformity in Shmerkin’s main theorem in [Shm] with tools from ergodic theory in an
appropriate symbolic dynamic setting. It remains an interesting question whether there is
a direct way of deriving Theorem C from Theorem B, in analogy to the continuous setting
where it is known that upper bounds on the dimension of ﬁbers imply lower bounds on the
dimension of sumsets.
Our ﬁnal main result in the integer setting is an analogue of Theorem 1.4 concerning
the dimension of iterated sumsets of ×r-invariant sets. Our deduction of Theorem D from
Theorem 1.4 highlights the ﬂexibility of the machinery developed in this paper to transfer
results from the reals to the integers.

Theorem D. Let (Ai)∞
i=1 be a sequence of ×r-invariant subsets of N0. If ∑∞
i=1 dimH Ai/
| log dimH Ai| diverges, then
 lim
n→∞ dimH (A1 + · · · + An) = 1.

In the same way as in the continuous regime, this theorem demonstrates that the struc-
ture captured by ×r-invariance in N0 sits transversely to the additive structure captured by
additive closure. It also demonstrates the connection between ×r-invariant subsets of the in-
tegers and ×r-invariant subsets of [0, 1], and it will serve to emphasize the role multiplicative
independence plays in the other results in this section.

1.4. Overview of the paper

The paper is organized as follows. In Section 2, we derive the intersection and sumset
transversality results for multiplicatively invariant subsets of [0, 1] from the main result in
[Shm]. We begin Section 3 with the basic facts and results we need from discrete fractal
geometry in Section 3.1 and continue by connecting ×r-invariant subsets of N0 to symbolic
dynamics and multiplicatively invariant subsets of the reals. Section 3 lays the groundwork
for Section 4, where we prove our main results: Theorems A, B, C, and D. We construct
an example in Section 4.4 that demonstrates that Theorem C is not expected to hold under
weaker assumptions. Finally, we conclude the paper with Section 5 by outlining a number of
open problems and directions.
 1.5. Acknowledgements

The authors extend a debt of gratitude to Pablo Shmerkin and Mark Pollicott, whose insight-
ful questions led to improvements in early formulations of Theorem C, and to Sam Chow for
help with Section 5.5. We also thank Vicente Saavedra Araya who pointed out a mistake in
an earlier draft of this paper. The third author is supported by the Swiss National Science
Foundation under grant number TMSGI2-211214.

11

2. Sums and intersections of multiplicatively invariant
subsets of the reals

In this section, we prove that subsets of [0, 1] that are multiplicatively invariant with respect
to multiplicatively independent bases are both geometrically and additive combinatorially
transverse. Our theorems are derived from the main result of Shmerkin [Shm], but we give
particular care on emphasizing the “uniformity” in the parameters. While most of the results
in this section are already implicit in the literature, we spell out the full details to have the
precise statements we need, and we provide complete proofs for the beneﬁt of non-experts.
This is the only section in the paper in which we draw on classical fractal geometry, so
we begin by establishing the basic terminology and results.
The set of real numbers, R, is equipped with the usual Euclidean metric, and, for con-
venience, all product spaces in the work are endowed with the L1 (taxicab) metric. The
distance between x, y ∈ Rd is denoted by |x − y|, and the open ball centered at x with radius
δ is denoted B(x, δ). Throughout the paper, a measure refers to a non-negative-valued Radon
measure on Rd. The total mass of a measure µ is ∥µ∥ := µ(Rd), and its support is denoted
supp µ. The push-forward of µ under a map ϕ is denoted ϕµ, so that ϕµ(B) = µ(ϕ−1B) for
all measurable sets B.
Finally, given two positive-valued functions f and g, we write f ≪a1,...,ak g if there exists
a constant c > 0 depending only on the quantities a1, . . . , ak for which f (x) ⩽ cg(x) for all
x in the domain common to both f and g. We write f ≍a1,...,ak g if both f ≪a1,...,ak g and
f ≫a1,...,ak g.

2.1. Fractal geometry of sets and measures in Euclidean space

In this subsection, we give a terse summary of the necessary notation, terminology, and basic
results from traditional fractal geometry. The reader interested in learning more will ﬁnd
most of this material in Mattila [Mat, Ch. 4]. Throughout this subsection, ρ and γ are
positive real numbers and X ⊆ Rd is non-empty.

Deﬁnition 2.1.
• The set X is ρ-separated if for all distinct x1, x2 ∈ X, |x1 − x2| ⩾ ρ.
• The packing number of X (sometimes also called the metric entropy of X) at scale ρ is

N (X, ρ) = sup {|X0| ∣
∣ X0 ⊆ X is ρ-separated}.

• The upper Minkowski dimension of X is

dimM X = lim sup
ρ→0+ log N (X, ρ)
log ρ−1 .

The lower Minkowski dimension, dimM X, is deﬁned analogously with a limit inﬁmum
in place of the limit supremum. If the lower and upper Minkowski dimensions agree,
then that value is the Minkowski dimension of X, dimM X. It is easy to check that for
all ρ < 1, dimM X = lim supN →∞ log N (X, ρ−N )
∕ log ρN and similarly for dimM X.

Deﬁnition 2.2.
 12

• The discrete Hausdorﬀ content of X at scale ρ and dimension γ is

Hγ
⩾ρ(X) = inf
 {∑

i∈I δγ
i
 ∣
∣
∣
∣
∣ X ⊆ ⋃

i∈I Bi, Bi open ball of diameter δi ⩾ ρ
}
 .

• The unlimited Hausdorﬀ content at dimension γ of X is

Hγ
>0(X) = inf
 {∑

i∈I δγ
i
 ∣
∣
∣
∣
∣ X ⊆ ⋃

i∈I Bi, Bi open ball of diameter δi > 0

}
 .

• The Hausdorﬀ dimension of X is

dimH X = sup{γ ∈ R | Hγ
>0(X) > 0} = inf{γ ∈ R | Hγ
>0(X) = 0}.

Note that if X is compact, the index set I in the deﬁnitions of Hγ
⩾ρ(X) and Hγ
>0(X) may
be taken to be ﬁnite.

Remark 2.3. The discrete Hausdorﬀ content tends to the unlimited Hausdorﬀ content in
the limit as the scale tends to zero. More precisely, for X ⊆ Rd compact and γ ⩾ 0,

lim
ρ→0+ Hγ
⩾ρ(X) = Hγ
>0(X).

It follows that if limρ→0 Hγ
⩾ρ(X) > 0, then dimH X ⩾ γ. The proof is straightforward; see
[GMR, Lemma 2.4].

Recall the notation [X]δ for the δ-neighborhood of X:

[X]δ := {z ∈ Rd ∣
∣ ∃x ∈ X with |z − x| ⩽ δ}.

The Hausdorﬀ distance between two non-empty, compact sets X, Y ⊆ Rd is

dH (X, Y ) := inf {δ > 0 ∣
∣ X ⊆ [Y ]δ and Y ⊆ [X]δ}
.

By the Blaschke selection theorem, the set of all non-empty, compact subsets of Rd equipped
with the Hausdorﬀ distance is a complete metric space.

Lemma 2.4. Suppose X, Y ⊆ Rd are non-empty, compact and X ⊆ [Y ]δ. For all non-empty,
compact X ′ ⊆ X, there exists a non-empty, compact Y ′ ⊆ Y such that dH(X ′, Y ′) ⩽ δ.

Proof. Deﬁne Y ′ = Y ∩ [X ′]δ. By deﬁnition, the set Y ′ is compact and Y ′ ⊆ [X ′]δ. Since
X ′ ⊆ [Y ]δ, the set Y ′ is non-empty. To see that X ′ ⊆ [Y ′]δ, let x ∈ X ′. Since X ⊆ [Y ]δ,
there exists y ∈ Y such that |x − y| ⩽ δ. This implies that y ∈ Y ∩ [X ′]δ, which shows that
x ∈ [Y ∩ [X ′]δ]δ = [Y ′]δ, as was to be shown.

We proceed with a number of straightforward lemmas that describe how the packing
number and discrete Hausdorﬀ content behave as functions of the set and the scale. We
include full proofs for completeness.

Lemma 2.5. For all a, ρ > 0, all non-empty, compact sets X, Y ⊆ Rd satisfying X ⊆ [Y ]aρ,
and all γ ∈ [0, d],
 N (X, ρ) ≪a,d N (
Y, ρ
), (2.1)

Hγ
⩾ρ(X) ≪a,d Hγ
⩾ρ(Y ). (2.2)

13

Proof. Let X ′ ⊆ X be a maximal ρ-separated subset of X. Deﬁne a map π : X ′ → Y by
choosing for each point x ∈ X ′ a point πx ∈ Y such that |x − πx| ⩽ aρ. Deﬁne Y ′ = πX ′.
Since X ′ is ρ-separated, there are at most C = C(a, d) > 0 many points of X ′ in any
closed ball of radius (a + 1)ρ. It follows that the map π is at most C-to-1, and hence that
|Y ′| ≫a,d |X ′|. It also follows that there are at most C many points of Y ′ in any closed ball
of radius ρ. Therefore, the set Y ′ can be thinned to a set Y ′′ ⊆ Y ′ that is ρ-separated and
that satisﬁes |Y ′′| ≫a,d |Y ′|. Combining these observations,

N (X, ρ) = |X ′| ≪a,d |Y ′| ≪a,d |Y ′′| ⩽ N (Y, ρ
)

which veriﬁes (2.1).
To show (2.2), let {Bi}i∈I be a collection of open balls that covers Y and where Bi
has diameter ri ⩾ ρ and ∑i∈I rγ
i < 2Hγ
⩾ρ(Y ). It follows that X ⊆ ⋃i∈I [Bi]aρ and [Bi]aρ
is a ball of diameter ri + 2aρ ⩽ (2a + 1)ri. Therefore Hγ
⩾ρ(X) ⩽ ∑i∈I ((2a + 1)ri)γ ⩽
2(2a + 1)dHγ
⩾ρ(Y ).

Lemma 2.6. For all a, ρ > 0, all non-empty, compact X ⊆ Rd, and all γ ∈ [0, d],

N (
X, ρ) ≍a,d N (
X, aρ),

Hγ
⩾ρ(X) ≍a,d Hγ
⩾aρ(X).

Proof. Replacing ρ with aρ, we may assume without loss of generality in both statements
that 0 < a ⩽ 1.
Since 0 < a ⩽ 1, we have that N (X, ρ) ⩽ N (X, aρ
). To see the reverse inequality, let
X ′ ⊆ X be a maximal (aρ)-separated subset of X. Since the set X ′ intersects any ball of
diameter ρ in at most ≪a,d 1 many points, it may be thinned to an ρ-separated subset X ′′

of X ′ with cardinality |X ′′| ≫a,d |X ′|. Therefore, N (X, aρ) = |X ′| ≪a,d |X ′′| ⩽ N (X, ρ).
Since 0 < a ⩽ 1, we have that Hγ
⩾aρ(X) ⩽ Hγ
⩾ρ(
X). To see the reverse inequality, let X ⊆
∪iBi be an open cover of X by balls Bi with diam Bi ⩾ aρ and ∑i(diam Bi)γ ⩽ 2Hγ
⩾aρ(X).
Replace Bi with an open ball Ci with the same center and with diameter diam Bi/a. Since
Bi ⊆ Ci, we have that X ⊆ ∪iCi is an open cover of X by balls Ci with diam Ci ⩾ ρ.
Therefore,
 Hγ
⩾ρ(X) ⩽ ∑

i (diam Ci)
γ = a−γ ∑

i (diam Bi)
γ ⩽ 2a
−γHγ
⩾aρ(X),

as was to be shown.

Lemma 2.7. For all ρ > 0, all non-empty, compact X ⊆ Rd, all Lipschitz ϕ : Rd → Rk with
Lipschitz constant a > 0, and all γ ∈ [0, d],

N (ϕ(X), ρ) ≪a,d N (X, ρ),

Hγ
⩾ρ(ϕ(X)) ≪a,d Hγ
⩾ρ(X).

Proof. Let X ′ ⊆ X be such that ϕ(X ′) is a maximal ρ-separated subset of ϕ(X). Since ϕ
has Lipschitz constant a, the points of X ′ are ρ/a-separated. Thus, by Lemma 2.6,

N (ϕ(X), ρ) = |X ′| ⩽ N (X, ρ/a) ≪a,d N (X, ρ).

verifying the ﬁrst inequality.
 14

To see the second inequality, note that if B is an open ball in Rd, then the diameter of
ϕ(B) is bounded from above by a · diam B. Hence, there exists an open ball C ⊆ Rk with
diam B ⩽ diam C ⩽ max(a, 1) diam B and such that ϕ(B) ⊆ C.
If ∪iBi is a cover of X by open balls Bi with diam Bi ⩾ ρ then, ﬁnding for each Bi a ball
Ci as described above, we obtain a cover ∪iCi of the image set ϕ(X) by open balls Ci ⊆ Rk

with ρ ⩽ diam Ci ⩽ max(a, 1) diam Bi. It follows that

Hγ
⩾ρ(ϕ(X)) ⩽ max(a, 1)
γ Hγ
⩾ρ(X),

as was to be shown.

Deﬁnition 2.8. The real number γ is a Frostman exponent for a measure µ if there exists
a constant c > 0 such that for all balls B ⊆ Rd,

µ(
B) ⩽ c(diam B)
γ. (2.3)

If (2.3) holds only for balls B of diameter greater than / less than ρ, then γ is a Frostman
exponent at scales larger than / smaller than ρ, respectively.

The following lemmas are discrete versions of the well-known mass distribution principle
and Frostman’s lemma. This pair of results describes a close relationship between the discrete
Hausdorﬀ content of a set and the Frostman exponents of measures supported on that set.

Lemma 2.9 (cf. [BP, Lemma 1.2.8]). Let c, ρ > 0 and µ be a measure on Rd. If for all balls
B ⊆ Rd of diameter at least ρ we have µ(B) ⩽ c(diam B)γ, then Hγ
⩾ρ(supp µ) ⩾ ∥µ∥/c.

Proof. Let ε > 0, and let {Bi}i∈I be a cover of supp µ with balls Bi of diameter δi ⩾ ρ and
with ∑i∈I δγ
i ⩽ (1 + ε)Hγ
⩾ρ(supp µ). Then

∥µ∥ ⩽ µ
 (⋃

i Bi
)
 ⩽ ∑

i cδγ
i ⩽ c(1 + ε)Hγ
⩾ρ(supp µ).

The conclusion follows because ε > 0 was arbitrary.

Lemma 2.10. There exists a constant c > 0, depending only on the dimension d ∈ N, for
which the following holds. For all non-empty, compact X ⊆ [0, 1]d and all ρ, γ > 0 there
exists a measure µ supported on X with ∥µ∥ ⩾ Hγ
⩾ρ(X) and with the property that for all
balls B of diameter at least ρ, µ(B) ⩽ c(diam B)γ.

Proof. This requires only a small modiﬁcation to the proof of Frostman’s Lemma found in
[BP, Lemma 3.1.1]. By adjusting the constant c, it suﬃces to prove the lemma for ρ of
the form 2−k. Construct the 2-adic tree corresponding to the set X down to level k. More
precisely, the vertices of the tree at level ℓ are the closed, 2-adic cubes of the form
[ i1
2ℓ , i1 + 1
2ℓ
 ] × · · · × [ id
2ℓ , id + 1
2ℓ
 ] for some i1, . . . , id ∈ {0, . . . , 2
ℓ − 1}

that have non-empty intersection with the set X. Two vertices are adjacent in the tree if one
of the corresponding cubes contains the other. Associate to each leaf v (i.e. a vertex at level
k) of the tree an arbitrary point xv in X which belongs to the corresponding 2-adic cube.

15

Instead of deﬁning a measure µ on the space of inﬁnite paths through the tree as is done
in [BP], we deﬁne µ to be an atomic measure supported on the ﬁnite set S = {xv | v is a leaf}
that are associated to leaves of the tree.
Let E be the set of edges in the tree. We deﬁne an edge conductance (or capacity) function
c : E → [0, 1] as follows: an edge e connecting vertices on levels ℓ − 1 and ℓ is given an edge
conductance of c(e) = 2−ℓγ. Fix a maximal ﬂow f : E → [0, 1] from the root of the tree to
the leaves. This means that for every vertex v of the tree which is neither the root nor one
of the leafs, the sum of f (e) over all edges connecting v to a vertex at a higher level equals
the value of f on the (unique) edge connecting v to a vertex of a lower level. Moreover, f
is restricted by the conductance (so that f (e) ⩽ c(e) for all e ∈ E) and attains the highest
possible value (among all such ﬂows f ) of the sum over all edges connecting to a leaf. Deﬁne
the µ-mass of each point xv ∈ S to be equal to the value of f on the (unique) edge adjacent
to the leaf v.
Every 2-adic cube B with 2−k ⩽ diam B ⩽ 2−1 and with non-empty intersection with
X corresponds to an edge in the tree. By the choice of edge conductance and the fact that
the maximal ﬂow is a legal ﬂow, µ(B) ⩽ (diam B)γ. (Note that this inequality also holds for
B = [0, 1]d.) A 2-adic grid cover of X with cells of diameter at least 2−k corresponds to a
cut-set of the tree. By the MaxFlow-MinCut theorem, the measure µ has total mass equal to
the minimum cut, which is necessarily greater than Hγ
⩾2−k (X), concluding the proof of the
lemma.

2.2. Multiplicatively invariant sets and restricted digit Cantor sets

In this short subsection, we record some basic facts about multiplicatively invariant subsets
of [0, 1] and the subclass of restricted digit Cantor sets.

Deﬁnition 2.11. Let r ∈ N, r ⩾ 2, and X ⊆ [0, 1].
• The map Tr : [0, 1] → [0, 1] is deﬁned by Trx = {rx}, the fractional part of the real
number rx.
• The set X is ×r-invariant if it is closed and TrX ⊆ X.
• The set X is multiplicatively invariant if it is ×r-invariant for some r ⩾ 2.
We stress that, by our deﬁnition, all multiplicatively invariant sets are closed.

Multiplicatively invariant sets behave well in regards to dimension: their Hausdorﬀ and
Minkowski dimensions agree, and so by [Mat, Theorem 8.10] the dimension of a Cartesian
products of such sets is the sum of the dimensions of the factors.

Lemma 2.12. If X, Y ⊆ [0, 1] are multiplicatively invariant, then dimH X = dimM X and
dimH(X × Y ) = dimM(X × Y ) = dimH X + dimH Y .

Proof. The ﬁrst fact is proven in [Fur1, Proposition III.1]. The second follows immediately
from [Mat, Corollary 8.11] and the fact that dimH X = dimM X.

Restricted digit Cantor sets are important examples of multiplicatively invariant sets, and
the natural Bernoulli measures they support will play an important role in the theorems in
this section.

Deﬁnition 2.13.
 16

• The base-r restricted digit Cantor set with digits from D ⊆ {0, . . . , r − 1} is

Cr,D =
 { ∞∑

i=1
 di
ri
 ∣
∣
∣
∣
∣ (di)i∈N ⊆ D
}
 ,

the set of those real numbers in [0, 1] expressible in base-r using only digits from D.
• The base-r restricted digit Cantor measure with digits from D ⊆ {0, . . . , r − 1}, denoted
µr,D, is the (1/|D|)-Bernoulli measure on Cr,D, deﬁned as

µr,D
 ([ j
ri , j + 1
ri
 )) =
 {
|D|−i if [ j
ri , j+1
ri ) ∩ Cr,D ̸= ∅

0 otherwise .

• The dimension 4 of the measure µr,D is dim µr,D := log |D|/ log r. We also deﬁne the
dimension of a product of such measures to be the sum of the dimensions of the factors.

The dimensions of a product of restricted digit Cantor sets Cr,Dr × Cs,Ds and of its as-
sociated product measure µ := µr,Dr × µs,Ds coincide and are equal to log r/ log |Dr| +
log s/ log |Ds|. In fact, such a measure µ is highly regular, in the sense that for all balls
B ⊆ R2 of diameter 0 < δ < 1 centered at a point in the support of µ,

µ(B) ≍ δdim µ, (2.4)

where the asymptotic constants are independent of δ. This follows from the fact that such an
estimate holds for single restricted digit Cantor measures, an easy exercise left to the reader.
While multiplicatively invariant sets can be vastly more complicated than restricted digit
Cantor sets, the following lemma shows that the former can be approximated from above
(with respect to dimension) by the latter. The result is well known; for a proof, see [Wu,
Prop. 9.3].

Lemma 2.14. Let X ⊆ [0, 1] be multiplicatively invariant. For all ε > 0, there exists a
restricted digit Cantor set X ′ containing X such that dimH X ′ < dimH X + ε.

2.3. A uniform Frostman exponent projection theorem

For t ∈ R, denote by Πt : R2 → R the oblique projection Πt(x, y) = x + ty. The goal in
this subsection is to prove Theorem 2.15 below, which is a result about Frostman exponents
for oblique projections of products of restricted digit Cantor measures. This theorem follows
implicitly from the results in [Shm], but since the exact statement does not appear in the lit-
erature, we provide a complete proof. We stress the uniformity over the projection parameter
t, which will be crucial to our applications later.

Theorem 2.15. Let µ be the product of two restricted digit Cantor measures whose bases
are multiplicatively independent. For all compact I ⊆ R\{0} and all 0 < γ < min(dim µ, 1),

4There are many natural and useful ways to deﬁne the dimension of a measure. In this paper, we will need
only to consider the dimension of products of restricted digit Cantor measures, a class of measures for which
most notions of dimension coincide. Thus, we deﬁne “dim µ” for such measures µ in a highly specialized way
instead of giving a general deﬁnition of the symbol.
 17

there exists c > 0 such that for all ρ ∈ [0, 1],

sup
t∈I, x∈R Πtµ(
B(x, ρ)
) ⩽ cργ.

Let 2 ⩽ r < s be multiplicatively independent integers, Dr ⊆ {0, . . . , r − 1} and Ds ⊆
{0, . . . , s − 1} sets of digits, and Cr,Dr ⊆ [0, 1] and Cs,Ds ⊆ [0, 1] the base-r and base-s
restricted digit Cantor sets with allowed digits Dr and Ds, respectively. Let µr,Dr and µs,Ds
the restricted digit Cantor measures on Cr,Dr and Cs,Ds, respectively, and let µ = µr,Dr ×µs,Ds.
We will prove Theorem 2.15 for the measure µ by ﬁrst proving the following theorem,
which we derive from a careful application of Shermkin’s recent Lq-dimension projection
theorem [Shm, Theorem 1.11]. Denote by Pm the dyadic partition of R into intervals of
length 2−m, and denote by log the base-2 logarithm.

Theorem 2.16. For all q ∈ (1, ∞) and all compact I ⊆ R\{0},

lim
m→∞ sup
t∈I
 ∣
∣
∣
∣− log ∑Q∈Pm Πtµ(Q)q

(q − 1)m − min(dim µ, 1)
∣
∣
∣
∣ = 0.

Proof. It suﬃces to prove Theorem 2.16 for intervals I ⊆ (0, ∞). Indeed, note that the set
1 − Cs,Ds = Cs, ˜Ds is a base-s restricted digit Cantor set with digits from ˜Ds = s − 1 − Ds
whose associated restricted digit Cantor measure µs, ˜Ds is the image of the measure µs,Ds
under x ↦→ 1 − x. It follows that for t < 0, Πtµ is a translate of Π−t(µr,Dr ⊗ µs, ˜Ds), a measure
which satisﬁes the conclusion of the theorem. To prove the theorem for I ⊆ (0, ∞), it suﬃces
to prove it for every interval I of the form I = [ξ, ξs), where ξ > 0, since every compact
subset of (0, ∞) is contained in a ﬁnite union of intervals of this form.
Let ξ > 0 and λ = 1/r. Let T : [0, 1) → [0, 1) be the irrational rotation by β = log r/ log s,
T x = x + β mod 1. For t > 0, let St : R → R denote the multiplication by t. Let ∆r and ∆s
be the normalized counting measures on Dr and Ds, respectively, and for x ∈ [0, 1), deﬁne

∆(x) =
 {∆r if x ⩾ β
∆r ∗ Sξsx∆s if x < β .

Given x ∈ [0, 1) and n ∈ N, deﬁne µx,0 = δ0 and µx,n = µx,n−1 ∗ Sλn∆(T nx), where we denote
by Sλν the pushforward of the measure ν under Sλ. To each x ∈ X, we associate the measure

µx = ∞
∗
n=1 Sλn∆(T nx) = lim
n→∞ µx,n.

The tuple ([0, 1), T, ∆, λ) is an example of what Shmerkin calls a “pleasant model” ([Shm,
Deﬁnition 1.9]). As such, it follows from [Shm, Theorem 1.11] that for all q ∈ (1, ∞),

lim
m→∞ sup
x∈[0,1)
 ∣
∣
∣
∣− log ∑Q∈Pm µx(Q)q

(q − 1)m − min(α, 1)
∣
∣
∣
∣ = 0, (2.5)

where
 α = α(q) = 1
(q − 1) log λ
 ∫ 1

0 log ∥∆(x)∥
q
q dx

and ∥ν∥
q
q = ∑y∈R ν({y})q. To ﬁnish the proof of Theorem 2.16, we will show that for all
x ∈ [0, 1) and all q > 1, µx = Πξsxµ and α = dim µ.

18

To see that for each x ∈ [0, 1) the measure µx is equal to Πξsxµ, observe ﬁrst that

µx,n = µx,n−1 ∗ Sλn∆(T nx)

=
 {
µx,n−1 ∗ Sr−n∆r if {x + nβ} ⩾ β

µx,n−1 ∗ Sr−n (
∆r ∗ Sξs{x+nβ}∆s) if {x + nβ} < β . (2.6)

Note that
 r−ns{x+nβ} = s−nβs{x+nβ} = sxs−⌊x+nβ⌋.

Borrowing notation from Shmerkin, let n′(x) := ⌊x + nβ⌋; it is a function of both x and n.
Note that n′(x) can equivalently be described as the cardinality of the set {i ∈ {1, . . . , n} | {x+
iβ} < β}. Now (2.6) becomes

µx,n =
 {
µx,n−1 ∗ Sr−n∆r if {x + nβ} ⩾ β
µx,n−1 ∗ Sr−n∆r ∗ Ss−n′(x)ξsx∆s if {x + nβ} < β . (2.7)

Since convolution is commutative, the fact that the orbit {T x, . . . , T nx} visits [0, β) exactly
n′(x) times and (2.7) imply that

µx,n = ( n
∗
i=1 r−i∆r
) ∗ Sξsx (n′(x)
∗
i=1 Ss−i∆s
) .

Now for all x ∈ [0, 1),

lim
n→∞
 n
∗
i=1 Sr−i∆r = µr,Dr and lim
n→∞
 n′(x)
∗
i=1 Ss−i∆s = µs,Ds,

which proves that for every x ∈ [0, 1), µx = limn→∞ µx,n = µr,Dr ∗ Sξsxµs,Ds = Πξsxµ, as
claimed.
To ﬁnish the proof, it remains to show that the value α in (2.5) equals the dimension
of µ, which is dim µ = dim µr,Dr + dim µs,Ds = log |Dr|
log r + log |Ds|
log s . Note that for almost

every x < β, ∥∆(x)∥
q
q = ∑i∈Dr ∑j∈Ds ( 1
|Dr||Ds| )q = |Dr|1−q|Ds|1−q, and for all x ⩾ β,

∥∆(x)∥
q
q = ∑i∈Dr ( 1
|Dr| )q = |Dr|1−q. Therefore, by the deﬁnition of α,

α = 1
(q − 1) log λ
 ∫ 1

0 log ∥∆(x)∥
q
q dx

= 1
(1 − q) log r
 (∫ β

0 log ∥∆(x)∥
q
q dx + ∫ 1

β log ∥∆(x)∥
q
q dx)

= 1
log r
 (
β( log |Dr| + log |Ds|
) + (1 − β) log |Dr|
)

= log |Dr|
log r + log |Ds|
log s ,

as was to be shown.

Though we have not developed the terminology for it, the conclusion in Theorem 2.16
concerns the Lq-dimension of the images of µ under oblique projections. The following lemma
allows us to derive from Theorem 2.16 a statement concerning Frostman exponents of the

19

projected measures.

Lemma 2.17 (cf. [Shm, Lemma 1.7]). Let µ be a probability measure on R, q > 1, and
γ > 0. If for all m ⩾ M ,
 − log ∑Q∈Pm µ(Q)q

(q − 1)m ⩾ γ, (2.8)

then for all x ∈ R and all ρ < 2−M , µ(B(x, ρ)) ⩽ 2ρ(1−1/q)γ.

Proof. Note that the inequality in (2.8) rearranges to
∑

Q∈Pm µ(Q)
q ⩽ 2
−m(q−1)γ .

Thus, for all Q ∈ Pm,
 µ(Q)
q ⩽ ∑

Q∈Pm µ(Q)
q ⩽ 2
−m(q−1)γ .

This gives the desired inequality for those intervals that are elements of the partition Pm for
m ⩾ M . Any interval of length 2−(m+1) ⩽ ρ < 2−m is covered by at most two elements of
the partition Pm+1, giving the result.

We are now in a position to deduce Theorem 2.15 from Theorem 2.16 and Lemma 2.17.

Proof of Theorem 2.15. Let I ⊆ R\{0} be compact and 0 < γ < γ′ < min(dim µ, 1). Let
q > 1 be large enough so that (1 − 1/q)γ′ > γ. It follows from Theorem 2.16 that there exists
M ∈ N such that for all t ∈ I and all m ⩾ M ,

− log ∑Q∈Pm Πtµ(Q)q

(q − 1)m ⩾ γ′.

Let 0 < ρ0 < 2−M be small enough so that 2ρ
(1−1/q)γ′
0 < ργ
0. It follows from Lemma 2.17
that for all ρ < ρ0, all t ∈ I, and all x ∈ R,

Πtµ(B(x, ρ)
) ⩽ 2ρ(1−1/q)γ′ .

Since the Πtµ mass of any ball is at most 1, by setting c = ρ
−γ
0 , the conclusion of Theorem 2.15
holds for all ρ ∈ [0, 1].

2.4. Geometric transversality in the reals

Here we employ Theorem 2.15 to deduce upper bounds on the packing number of intersections
of multiplicatively invariant sets. The idea in the proof below is borrowed from [Shm, Lemma
1.8].

Theorem 2.18. Let r and s be multiplicatively independent positive integers, and let X, Y ⊆
[0, 1] be ×r- and ×s-invariant sets, respectively. Deﬁne γ = max(0, dim X + dim Y − 1). For

20

all compact I ⊆ R\{0} and ε > 0,

lim
ρ→0+ sup
t∈I
x∈R
 N ((X × Y ) ∩ Π
−1
t (B(x, ρ)
) , ρ
)

ρ−(γ+ε) = 0.

Proof. Let I ⊆ R\{0} be compact and ε > 0. According to Lemma 2.14, we can embed
X and Y into restricted digit Cantor sets of slightly higher dimension. Thus, there exists a
product of restricted digit Cantor measures µ of dimension dim µ < dimH X + dimH Y + ε/4
such that X × Y ⊆ supp µ.
From Theorem 2.15, we have that there exists ρ0 > 0 such that for all ρ < ρ0, all t ∈ I,
and all x ∈ R,
 Πtµ(B(x, 2ρ)) ⩽ ρmin(dim µ,1)−ε/4.

Let ρ < ρ0, t ∈ I, and x ∈ R. By (2.4) and the fact that ρ0 is suﬃciently small, every
ball of radius ρ centered at a point of supp µ has µ-mass greater than ρdim µ+ε/4. Therefore,

N ((supp µ) ∩ Π
−1
t (B(x, ρ)), 2ρ) · ρ
dim µ+ε/4 ⩽ µ(Π
−1
t (B(x, 2ρ))
) ⩽ ρmin(dim µ,1)−ε/4.

It follows now from the fact that X × Y ⊆ supp µ and Lemma 2.6 that

N ((X × Y ) ∩ Π
−1
t (B(x, ρ)), ρ) ⩽ N ((supp µ) ∩ Π
−1
t (B(x, ρ)), ρ)

≪ N (
(supp µ) ∩ Π
−1
t (B(x, ρ)), 2ρ)

⩽ ρmin(dim µ,1)−dim µ−ε/2

= ρ−(max(0,dim µ−1)+ε/2)

⩽ ρ−(γ+3ε/4).

The limit in the conclusion of the theorem follows.

The following corollary is formulated in a way that will make it convenient to apply in
the integer setting.

Corollary 2.19. Let r and s be multiplicatively independent positive integers, and let
X, Y ⊆ [0, 1] be ×r- and ×s-invariant sets, respectively. Deﬁne γ = max(0, dim X + dim Y −
1). For all compact I ⊆ R\{0} and all ε > 0,

lim
ρ→0+ sup
λ,η∈I
σ,τ ∈R
 N ([λX + τ ]
ρ ∩ [ηY + σ]
ρ, ρ)

ρ−(γ+ε) = 0.

Note that, taking ﬁxed λ, η, σ and τ = 0 this corollary recovers the Shermkin-Wu theorem
encapsulated in (1.8).

Proof. Let I ⊆ R\{0} be compact and ε > 0. Denote by π1 : (x, y) ↦→ x the ﬁrst coordinate
projection. The following facts are straightforward to verify:
• λ[X]ρ = [λX]|λ|ρ;
• [X + τ ]ρ = [X]ρ + τ ;
• [X]ρ ∩ ([ηY ]ρ + σ) = π1(
[X × Y ]ρ ∩ Π
−1
−η(σ)
), using that X × Y is equipped with the L1

metric;
 21

• if ϕ has Lipschitz constant L, then [X]ρ ∩ ϕ−1(σ) ⊆ [X ∩ ϕ−1B(σ, Lρ)]ρ.
Using these facts in order, we see that there exist c1, c2 > 1 depending only on I such that

[λX + τ ]ρ ∩ [ηY + σ]ρ ⊆ λ ([X]c1ρ ∩ ([ η
λ Y ]

c1ρ + σ − τ
λ
 )) + τ

= λπ1
 ([X × Y ]c1ρ ∩ Π
−1
−η/λ
 ( σ − τ
λ
 )) + τ

⊆ λπ1
 ([(X × Y ) ∩ Π
−1
−η/λB ( σ − τ
λ , c1c2ρ)]
c1c2ρ
)
 + τ.
 (2.9)

We have need for four more easily-veriﬁed facts:
• N (Z + τ, ρ) = N (Z, ρ);
• N (λZ, ρ) = N (Z, ρ/|λ|);
• N (π1(Z), ρ) ⩽ N (Z, ρ);
• N ([Z]δ, ρ) ⩽ δ/ρN (Z, ρ).
Applying N ( · , ρ) to both sides of (2.9) and using the preceding facts in order, we have that
there exists c3 > 1 depending only on I such that

N ([λX + τ ]
ρ ∩ [ηY + σ]
ρ, ρ) ⩽ c3N (
(X × Y ) ∩ Π
−1
−η/λB(
(σ − τ )/λ, c3ρ
), ρ/c3).

The conclusion of the corollary now follows from Theorem 2.18 by appealing to Lemma 2.6.

2.5. Additive transversality of sumsets in the reals

In this subsection, we use Theorem 2.18 to show that sets which are multiplicatively invariant
with respect to multiplicatively independent bases are transverse in an additive combinatorial
sense. The core ideas here appear in [Shm, Corollary 7.4], and we develop it in the context
of the discrete Hausdorﬀ dimension here.
The following lemma is a packing number analogue of the useful fact that if the ﬁbers of
a map X → Y between ﬁnite sets X and Y are uniformly bounded in cardinality, then the
image of the map must be large.

Lemma 2.20. Let ϕ : Rd → Rk, X ⊆ Rd be bounded, and ρ > 0. If W > 0 is such that for
all x ∈ Rk,
 N (
X ∩ ϕ
−1(
B(x, 2ρ)
) , ρ) ⩽ W,

then N (ϕ(X), ρ) ⩾ N (
X, ρ)/W .

Proof. Let X ′ be a ρ-separated subset of X of maximal cardinality so that |X ′| = N (X, ρ).
Since ϕ(X ′) is covered by N (ϕ(X ′), ρ)-many balls of radius 2ρ, the set X ′ is covered by
N (ϕ(X ′), ρ)-many pre-images of balls of radius 2ρ under ϕ. Thus, there exists x ∈ Rk such
that
 |X ′|
N (ϕ(X ′), ρ) ⩽ ∣
∣X ′ ∩ ϕ
−1(B(x, 2ρ))
∣
∣ ⩽ N (X ∩ ϕ
−1(B(x, 2ρ)), ρ) ⩽ W.

22

It follows that
 N (X, ρ)
W = |X ′|
W ⩽ N (ϕ(X ′), ρ) ⩽ N (ϕ(X), ρ),

as was to be shown.

Theorem 2.21. Let r and s be multiplicatively independent positive integers, and let X, Y ⊆
[0, 1] be ×r- and ×s-invariant sets, respectively. Deﬁne γ = max(0, dimH X + dimH Y − 1).
For all compact I ⊆ R\{0}, all ε > 0, all 0 ⩽ γ ⩽ 1, all suﬃciently small ρ > 0 (depending
on X, Y, I, ε, and γ), all compact, non-empty X ′ ⊆ X, Y ′ ⊆ Y , and all λ, η ∈ I,

N (λX ′ + ηY ′, ρ
) ⩾ N (X ′ × Y ′, ρ)

ρ−(γ+ε) , and (2.10)

Hγ
⩾ρ(λX ′ + ηY ′) ≫I,γ,ε Hγ+γ+ε
⩾ρ (X ′ × Y ′)
. (2.11)

Proof. It suﬃces by dilating, appealing to Lemma 2.6, and absorbing asymptotic constants
into the ρε term to prove the following: for all compact I ⊆ R\{0}, all ε > 0, all 0 ⩽ γ ⩽ 1,
all suﬃciently small ρ0 > 0 (depending on I, ε, and γ), all compact, non-empty X ′ ⊆ X,
Y ′ ⊆ Y , all t ∈ I, and all 0 < ρ < ρ0,

N (
Πt(X ′ × Y ′), ρ
) ⩾ N (X ′ × Y ′, ρ)

ρ−(γ+ε) , and (2.12)

Hγ
⩾ρ(Πt(X ′ × Y ′)
) ≫ ρ0Hγ+γ+ε
⩾ρ (
X ′ × Y ′), (2.13)

where, recall, Πt(x, y) = x + ty.
Let I ⊆ R\{0} be compact, ε > 0, and 0 ⩽ γ ⩽ 1. It follows by Theorem 2.18 (with ε/2
as ε) that for all suﬃciently small ρ > 0, all t ∈ I, and all x ∈ R,

N (
(X × Y ) ∩ Π
−1
t (B(x, 2ρ)), 2ρ) ⩽ (2ρ)
−(γ+ε/2).

Fix such a suﬃciently small 0 < ρ0 < 1, and ensure also that it is small enough so that ρ
−ε/2
0
is greater than the asymptotic constant appearing in Lemma 2.6 (with a = d = 2). It follows
that for all 0 < ρ < ρ0, all compact, non-empty X ′ ⊆ X, Y ′ ⊆ Y , all t ∈ I, and all x ∈ R,

N (
(X ′ × Y ′) ∩ Π
−1
t (B(x, 2ρ)), ρ) ⩽ ρ−(γ+ε). (2.14)

Now (2.12) follows immediately from Lemma 2.20 (with X ′ × Y ′ as X).
To show (2.13), let 0 < ρ < ρ0 and X ′ ⊆ X, Y ′ ⊆ Y be compact, non-empty. By
Lemma 2.10, there exists a measure ν supported on X ′ × Y ′ with ∥ν∥ ⩾ Hγ+γ+ε
⩾ρ (X ′ × Y ′)
and such that for all x ∈ R2 and all δ ⩾ ρ,

ν(B(x, δ/2)
) ⩽ c1δγ+γ+ε, (2.15)

where c1 > 1 is an absolute constant. Using the fact that supp ν ⊆ X ′ × Y ′ ⊆ X × Y , it
follows from (2.14) that for all 0 < δ < ρ0, all t ∈ I, and all x ∈ R,

N (supp ν ∩ Π
−1
t (B(x, δ/2)), δ/4
) ⩽ c2δ−(γ+ε), (2.16)

where c2 > 1 is an absolute constant.
The inequality in (2.16) implies that as long as δ < ρ0, the part of the support of ν
contained in any tube Π
−1
t (B(x, δ/2)) can be covered by c2δ−(γ+ε) many balls of diameter δ.

23

The inequality in (2.15) says that as long as δ ⩾ ρ, each of those balls has ν-measure at most
c1δγ+γ+ε. Therefore, we have that for all ρ ⩽ δ < ρ0, all t ∈ I, and all x ∈ R,

ν(
Π
−1
t (B(x, δ/2))
) ⩽ c1δγ+γ+εc2δ−(γ+ε) = c1c2δγ. (2.17)

We aim now to deduce (2.13) from (2.17). Let 0 < ρ < ρ0, and let ∪iBi be a cover of
Πt(X ′ × Y ′) by open balls of diameter at least ρ. If some ball Bi is such that diam Bi ⩾ ρ0,
then ∑i(diam Bi)γ ⩾ ργ
0 ⩾ ρ0. Otherwise, all balls in the cover have diameter less than ρ0,
and it follows then from (2.17) that

c1c2 ∑

i (diam Bi)
γ ⩾ ∥Πtν∥ = ∥ν∥ ⩾ Hγ+γ+ε
⩾ρ (X ′ × Y ′).

In either case, we have that
∑

i (diam Bi)
γ ⩾ min (ρ0, (c1c2)
−1Hγ+γ+ε
⩾ρ (X ′ × Y ′)
) ⩾ ρ0(c1c2)
−1Hγ+γ+ε
⩾ρ (X ′ × Y ′),

where the second inequality follows from the fact that both quantities in the minimum are
at most 1. Since the cover was arbitrary, we conclude the inequality in (2.13).

In the statement of the following corollary, it is useful to recall Lemma 2.12: all of the
notions of dimension for X, Y , and X × Y coincide, and dim(X × Y ) = dim X + dim Y .

Corollary 2.22. Let r and s be multiplicatively independent positive integers, and let
X, Y ⊆ [0, 1] be ×r- and ×s-invariant sets, respectively. For all dim ∈ {dimM , dimM , dimH},
for all compact subsets X ′ ⊆ X and Y ′ ⊆ Y , and for all λ, η ∈ R\{0},
• if dim X + dim Y ⩽ 1, then

dim (λX ′ + ηY ′) = dim (X ′ × Y ′)
; (2.18)

• if dim X + dim Y > 1, then

dim (λX ′ + ηY ′) ⩾ dim (X ′ × Y ′) − dim (X × Y ) + 1. (2.19)

Note that Corollary 2.22 extends the theorem of Hochman and Shmerkin encapsulated
by (1.9). Indeed, setting X ′ = X and Y ′ = Y , it follows from (2.18) and (2.19) that
dim (
λX + ηY ) ⩾ min (1, dim(X × Y )
). Using the fact that (x, y) ↦→ λx + ηy is Lipschitz,
the bounds in Lemma 2.7 immediately give the required upper bounds to yield equality in
(1.9).

Proof. Deﬁne γ = max(0, dimH(X × Y ) − 1), and let X ′ ⊆ X and Y ′ ⊆ Y . To show (2.18)
and (2.19), it suﬃces to show

dim (λX ′ + ηY ′) ⩾ dim (
X ′ × Y ′) − γ. (2.20)

Indeed, this is the lower bound in (2.19) and the upper bound derived from Lemma 2.7
combined with this lower bound gives the desired equality in (2.18).
Let dim ∈ {dimM , dimM , dimH} and λ, η ∈ (0, ∞). If dim(X ′ × Y ′) ⩽ γ, the conclusion
is immediate, so we can proceed under the assumption that dim(X ′ × Y ′) > γ.
Let ε > 0, and let γ = dim(X ′ × Y ′) − γ − 2ε. It follows from Theorem 2.21 that there

24

exists a small ρ0 > 0 such that for all 0 < ρ < ρ0,

N (λX ′ + ηY ′, ρ
)

ρ−γ ⩾ N (
X ′ × Y ′, ρ)

ρ−(γ+γ+ε) ,

Hγ
⩾ρ(λX ′ + ηY ′) ⩾ ρ0Hγ+γ+ε
⩾ρ (
X ′ × Y ′).

Consider the ﬁrst inequality if dim is the Minkowski dimension and the second inequality if
dim is the Hausdorﬀ dimension. Because γ + γ + ε = dim(A′ × B′) − ε, the limit inﬁmum (if
dim is a lower dimension) or limit supremum (if dim is an upper dimension) as N tends to
inﬁnity of the right hand side is positive. It follows that

dim (λX ′ + ηY ′) ⩾ dim (X ′ × Y ′) − γ − ε.

The inequality in (2.20) now follow from the fact that ε > 0 was arbitrary, concluding the
proof.

3. Discrete fractal geometry and multiplicatively invariant
subsets of the integers

In this section, we introduce the notation and terminology involved in the study of fractal
geometry in the positive integers and develop the basic results concerning multiplicatively
invariant subsets. To prove the results in this section and the transversality results in the
next, we relate ×r-invariant subsets of the integers to symbolic subshifts on r symbols and
to ×r-invariant subsets of [0, 1].

3.1. Notions of dimension for subsets of integers

To measure the size of subsets of N0, we will make use of the (upper and lower) mass
dimension and the (upper and lower) discrete Hausdorﬀ dimension, which were introduced in
Section 1.3, but which we recall for a more detailed discussion in this section. The upper and
lower mass dimensions and the upper Hausdorﬀ dimension are also treated systematically in
[BT2]; we will state the properties we require from these quantities with the aim of making
this presentation self-contained. These dimensions join a bevy of other natural notions of
dimension for subsets of the integers, integer lattices, and more general discrete sets; see
[Nau1, Nau2, BT1, IRUT, LM1].

Deﬁnition 3.1. Let A ⊆ Nd
0 be non-empty.
• The lower mass dimension of A is

dimM A = lim inf
N →∞ log ∣
∣A ∩ [0, N )d∣
∣

log N .

The upper mass dimension, dimM A, is deﬁned analogously with a limit supremum in
place of the limit inﬁmum. If dimM A = dimM A, then this value is the mass dimension
of A, dimM A.
• The lower discrete Hausdorﬀ dimension of A is

dimH A = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim inf
N →∞ Hγ
⩾1(
A ∩ [0, N )d)

N γ > 0

}
 .

25

The upper discrete Hausdorﬀ dimension, dimH A, is deﬁned analogously with a limit
supremum in place of the limit inﬁmum. If dimH A = dimH A, then this value is the
discrete Hausdorﬀ dimension of A, dimH A.

As the notation suggests, the mass and discrete Hausdorﬀ dimensions are deﬁned in
analogy to the Minkowski and Hausdorﬀ dimensions, respectively. The analogy becomes
clearer on noting that
 ∣
∣A ∩ [0, N )
d∣
∣ = N ( A ∩ [0, N )d

N , N −1) , (3.1)

Hγ
⩾1(
A ∩ [0, N )d)

N γ = Hγ
⩾N −1
 ( A ∩ [0, N )d

N
 ) , (3.2)

so that the mass and discrete Hausdorﬀ dimensions are capturing, in some sense, the Min-
kowski and Hausdorﬀ dimensions of the sequence of sets N ↦→ A/N in the unit cube.
As a word of caution, note that our terminology does not match exactly with the termi-
nology used in [BT2]. What we call the upper discrete Hausdorﬀ dimension is called dimL in
[BT2] (see Lemma 2.3 in that paper), while the discrete Hausdorﬀ dimension deﬁned in that
work does not appear in our work. Our choice of terminology is motivated by the connections
drawn in our work between the discrete and continuous notions of dimension.

Lemma 3.2. Let A, B ⊆ Nd
0, λ > 0, and σ ∈ Rd.
(I) For all dim ∈ {dimM , dimM , dimH , dimH }, dim A ∈ [0, d].
(II) For all dim ∈ {dimM , dimM , dimH , dimH }, dim A = dim (⌊λA + σ⌋
), where ⌊λA + σ⌋ =
{⌊λn + σ⌋ | n ∈ A}.
(III) For all dim ∈ {dimM , dimH }, dim(A ∪ B) = max ( dim A, dim B).
(IV) For all r ∈ N, r ⩾ 2,
 dimM A = lim inf
N →∞ log |A ∩ [0, rN )d|
N log r ,

and the analogous statement with dimM in place of dimM and limit supremum in place
of limit inﬁmum holds.
(V) For all r ∈ N, r ⩾ 2,

dimH A = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim inf
N →∞ Hγ
⩾1(A ∩ [0, rN )d)

rγN > 0

}
 ,

and the analogous statement with dimH in place of dimH and limit supremum in place
of limit inﬁmum holds.

Note that the sets in Examples 3.4 (ii) below show that the statement in (III) does not
hold for the lower mass and lower discrete Hausdorﬀ dimensions.

Proof. The statements in (I) through (IV) follow from straightforward calculations which are
left to the reader.
Both of the statements in (V) follow from (3.2) and the fact that for all γ ⩾ 0 and all
rK ⩽ N ⩽ rK+1,

Hγ
⩾1(A ∩ [0, rK )d)

rKγ ⩽ rγ Hγ
⩾1(A ∩ [0, N )d)

N γ ⩽ r2γ Hγ
⩾1(A ∩ [0, rK+1)d)

r(K+1)γ .

26

Indeed, this shows that the limit inﬁmum (resp. limit supremum) of the sequence N ↦→
Hγ
⩾1(A ∩ [0, rN )
)/rN γ is non-zero if and only if the limit inﬁmum (resp. limit supremum) of
the sequence N ↦→ Hγ
⩾1(
A ∩ [0, N )
)/N γ is non-zero.

Lemma 3.3. For all A ⊆ Nd
0,
 dimH A ⩽ dimM A ⩽ dimM A,

dimH A ⩽ dimH A ⩽ dimM A,

and no other comparisons are possible in general.

Proof. It is immediate from the deﬁnitions that dimM A ⩽ dimM A and dimH A ⩽ dimH A,
and the set in Examples 3.4 (i) below shows that neither of these inequalities are, in general,
equalities.
To see that dimH A ⩽ dimM A and that dimH A ⩽ dimM A, note that by covering A∩[0, N )d

by |A ∩ [0, N )d| many balls of diameter 1 it follows that

Hγ
⩾1(
A ∩ [0, N )d)

N γ ⩽ |A ∩ [0, N )d|
N γ .

If γ > dimM A (resp. γ > dimM A), then the limit inﬁmum (resp. limit supremum) of the
right hand side is zero, implying that γ ⩾ dimH A (resp. γ ⩾ dimH A). It follows that
dimH A ⩽ dimM A and dimH A ⩽ dimM A. The set in Examples 3.4 (iii) below shows that
neither of these inequalities are, in general, equalities.
To see that no other comparisons are possible, it suﬃces to show that there can in general
be no comparison between dimH and dimM . This is demonstrated by the sets in Examples 3.4
(i) and (iii) below.

The following examples are meant to illustrate the extent to which the mass and discrete
Hausdorﬀ dimensions relate for subsets of N0. These examples do not feature the type of
structures that we are concerned with in this work, so we leave some of the details to the
reader.

Examples 3.4.
(i) Let (xn)∞
n=0 ⊆ N0 be any sequence which satisﬁes limn→∞ log(xn+1 − xn)/ log xn+1 = 1,
and deﬁne
 A := {0} ∪
 ∞⋃

n=0
{x2n, x2n + 1, . . . , x2n+1}.

It is easy to check that dimM A = dimH A = 0 and that dimM A = dimH A = 1.
(ii) Let A be the set from (i). Put B = {0} ∪ (
N0\A
). Then dimM B = dimH B = 0 while
dimM B = dimH B = 1, and A + B = A ∪ B = N0.
(iii) Deﬁne
 A = {0, . . . , 16} ∪
 ∞⋃

n=2
 {2
n, . . . , 2
n + ⌊2
n−n/ log n⌋
}.

It is quick to check that the mass dimension of A exists and dimM A = 1. On the
other hand, by covering A with the intervals in its deﬁnition, it can be shown that the
discrete Hausdorﬀ dimension of A exists and dimH A = 0.

27

We conclude this section by proving some basic upper and lower bounds on the dimension
of product sets.

Lemma 3.5. For all non-empty A1, . . . , Ad ⊆ N0,

dimM (A1 × · · · × Ad) ⩽
 d∑

i=1 dimM Ai, (3.3)

dimH (A1 × · · · × Ad) ⩾
 d∑

i=1 dimH Ai. (3.4)

In particular, if dimH Ai = dimM Ai for each i ∈ {1, . . . , d}, then for all dim ∈ {dimM , dimM ,
dimH , dimH },
 dim (A1 × · · · × Ad) = dim A1 + · · · + dim Ad.

Proof. The inequality in (3.3) is immediate from the deﬁnition of upper mass dimension. To
prove the inequality in (3.4), deﬁne γi = dimH Ai and γ = ∑d
i=1 γi. Deﬁne A = A1 × · · · × Ad.
Let ε > 0 and N ∈ N. It follows by Lemma 2.10 that there exists a measure µi supported
on (Ai/N ) ∩ [0, 1) with ∥µi∥ ⩾ Hγi−ε
⩾N −1((Ai/N ) ∩ [0, 1)
) and such that for all balls B of
diameter at least N −1, µi(B) ⩽ c diam(B)γi−ε.
Consider the product measure µ = µ1 × · · · × µd; it is supported on the set A and has the
property that for all balls B of diameter at least N −1, µ(B) ⩽ cd diam(B)γ−dε. It follows by
Lemma 2.9 and (3.2) that

Hγ−dε
⩾1 (A ∩ [0, N )d)
N γ−dε = Hγ−dε
⩾N −1
 ( A
N ∩ [0, 1)
d)

⩾ c
−d d∏

i=1 Hγi−ε
⩾N −1(
(Ai/N ) ∩ [0, 1)
)

= c
−d d∏

i=1
 Hγi−ε
⩾1 (Ai ∩ [0, N ))
N γi−ε .

By the deﬁnition of the lower discrete Hausdorﬀ dimension, the limit inﬁmum as N tends to
inﬁnity of the right hand side of the previous inequality is positive, whereby dimH A ⩾ γ − dε.
The conclusion of the lemma follows since ε > 0 was arbitrary.

3.2. Dimension regularity of multiplicatively invariant sets

In this section, we prove that the mass and discrete Hausdorﬀ dimensions of a multiplicatively
invariant set (cf. Deﬁnition 1.5) exist and coincide. This is accomplished by adapting an
argument of Furstenberg [Fur1, Prop. III.1] from the continuous setting.

Proposition 3.6. If A ⊆ N0 is multiplicatively invariant (see Deﬁnition 1.5), then

dimH A = dimH A = dimM A = dimM A.

In particular, the mass and discrete Hausdorﬀ dimensions of A exist and coincide.

Before the proof, we introduce some notation that will be useful throughout this section

28

and the following ones. Fix r ∈ N, r ⩾ 2, and denote by Λr the alphabet {0, . . . , r − 1}. An
element w ∈ Λℓ
r is a word of length |w| = ℓ. The set of all ﬁnite words is Λ∗
r = ∪∞
ℓ=0Λℓ
r, and
the set of all inﬁnite words is ΛN0
r . The empty word is the sole element of the set Λ0
r. The
concatenation of the word w ∈ Λℓ
r with the word v ∈ Λk
r is denoted by juxtaposition: the word
wv is an element of Λℓ+k
r . We write wk for the word w concatenated with itself k many times.
Finally, we write w = w0 · · · wℓ−1 to indicate that the letters of w are w0, . . . , wℓ−1 ∈ Λr, in
that order.
For w = w0 · · · wℓ−1 ∈ Λℓ
r, deﬁne an element in N0 by

(w)r := w0rℓ−1 + w1rℓ−2 + · · · + wℓ−2r + wℓ−1.

The function ( · )r : Λ∗
r → N0 serves as the primary link between subsets of non-negative
integers and words. In the following subsection, we will use ( · )r to connect ×r-invariant
subsets of N0 with symbolic subshifts. Note that ( · )r is surjective, and is injective when
restricted to Λℓ
r for some ℓ ∈ N0.
As a ﬁnal ingredient before the proof of Proposition 3.6, we give an equivalent character-
ization of the lower discrete Hausdorﬀ dimension, dimH .

Lemma 3.7. For all A ⊆ N0,

dimH A = sup
 {

γ ⩾ 0
 ∣
∣
∣
∣
∣ lim inf
N →∞ Hγ,∗
⩾1 (A ∩ [0, rN )
)

rN γ > 0

}
 ,

where Hγ,∗
⩾1 (X) is deﬁned to be

min
 {
∑

i∈I rdiγ ∣
∣
∣
∣
∣ X ⊆ ⋃

i∈I
 ((w(i)0
di )r + [0, rdi )
), w(i) ∈ Λ
∗
r, di ∈ N0
}
 .

Proof. It suﬃces to show that for all ﬁnite X ⊆ N0, Hγ,∗
⩾1 (X) ≍ Hγ
⩾1(X), and then appeal to
Lemma 3.2 (V). That Hγ,∗
⩾1 (X) ⩾ Hγ
⩾1(X) follows immediately from the deﬁnitions. To show
that Hγ,∗
⩾1 (X) ≪ Hγ
⩾1(X), use the fact that any interval in N0 of length ℓ can be covered by
at most two intervals of the form (w0d)r + [0, rd), where d = ⌈logr ℓ⌉.

Proof of Proposition 3.6. Suppose A ⊆ N0 is ×r-invariant. Let γ > dimH A. We will show
that lim supM →∞ |A ∩ [0, rM )|/rM γ < ∞, from which it follows that dimM A ⩽ γ. Since
γ > dimH A is arbitrary, it will follow that dimM A ⩽ dimH A. It will follow then from
Lemma 3.3 that dimH A = dimH A = dimM A = dimM A, which will conclude the proof of the
lemma.
According to Lemma 3.7, there exists N ∈ N and a collection of intervals Bi = (w(i)0di)r +
[0, rdi), i ∈ I, that cover A ∩ [0, rN ) and for which ∑i∈I r(di−N )γ < 1. By prepending zeros
onto each w(i), we may assume that |w(i)| + di = N . Note that for all w ∈ ΛN
r , (w)r ∈ Bi if
and only if w = w(i)w′ for some w′ ∈ Λdi
r .
Let M ∈ N, M > N , and let n ∈ A ∩ [0, rM ). Write n = (w)r, where w ∈ ΛM
r (so that w
may have leading zeroes). Since A is Rr-invariant, RM −N
r (n) = (w1 · · · wN )r ∈ A ∩ [0, rN ).
Since A ∩ [0, rN ) ⊆ ∪iBi, there exists i1 ∈ I such that (w1 · · · wN )r ∈ Bi1. It follows that
w = w(i1)w′ for some w′ ∈ Λ
M −di1
r . Since A is Lr-invariant, applying Lr to n between 0
and |w(i1)|-many times (depending on how many initial zeroes there are in the word w(i1))
to n, we see that (w′)r ∈ A. Repeating the argument with (w′)r ∈ A, there exists i2 ∈ I

29

such that w′ = w(i2)w′′ for some w′′ ∈ Λ
M −di1 −di2
r . Repeating further, we see that there exist
i1, . . . , ik ∈ I such that w = w(i1) · · · w(ik)v, where v ∈ Λ<N
r .
Using the factorization of words w ∈ ΛM
r for which (w)r ∈ A described in the previous
paragraph and recalling that −|w(i)| = di − N , we see that
∣
∣A ∩ [0, 2M )
∣
∣

rM γ = ∑

w∈ΛM
r : (w)r∈A r−|w|γ

⩽
 

 ∑

v∈Λ<N
r
 r−|v|γ



 

1 + ∑

i1∈I r(di1 −N )γ + ∑

i1,i2∈I r(di1 −N +di2 −N )γ + · · ·
 



=
 

 ∑

v∈Λ<N
r
 r−|v|γ


 (
1 − ∑

i∈I r(di−N )γ)−1 .

Since the ﬁnal quantity is ﬁnite and independent of M , and since M > N was arbitrary, it
follows that lim supM →∞ |A ∩ [0, rM )|/rM γ < ∞, as was to be shown.

Corollary 3.8. If A1, . . . , Ad ⊆ N0 are multiplicatively invariant (with respect to any bases),
then for all dim ∈ {dimM , dimM , dimH , dimH },

dim (A1 × · · · × Ad) = dim A1 + · · · + dim Ad.

Proof. This follows immediately by combining Lemma 3.5 and Proposition 3.6.

3.3. Connections to symbolic dynamics

Throughout this subsection, we use σ to denote the left-shift on ΛN0
r , which is deﬁned by

σ : (wn)n∈N0 ↦→ (wn+1)n∈N0.

We endow Λr with the discrete topology and ΛN0
r with the product (or Tychonoﬀ) topology.
In the context of symbolic dynamics, any closed subset of ΛN0
r satisfying σ(Σ) ⊆ Σ is called
a subshift. The language set associated to a subshift Σ is the set of all the ﬁnite words,
including the empty word, appearing in the elements of Σ, i.e.,

L(Σ) = {
w0 · · · wℓ−1 ∣
∣ w = w0w1 · · · ∈ Σ, ℓ ∈ N0}
.

The language set of any subshift can be naturally embedded into the integers in two ways,
giving rise to the following deﬁnition.

Deﬁnition 3.9. The r-language sets associated to a subshift Σ ⊆ ΛN0
r are the sets AΣ, BΣ ⊆
N0 deﬁned by

AΣ = {(w0 · · · wℓ−1)r = w0rℓ−1 + w1rℓ−2 + · · · + wℓ−2r + wℓ−1 ∣
∣ w0 · · · wℓ−1 ∈ L(Σ)
},

BΣ = {(wℓ−1 · · · w0)r = wℓ−1rℓ−1 + wℓ−2rℓ−2 + · · · + w1r + w0 ∣
∣ w0 · · · wℓ−1 ∈ L(Σ)
},

where (w)r = 0 when w is the empty word.

The following proposition uses r-language sets to relate ×r-invariant sets with subshifts
of ΛN0
r . It is a generalization of some of the results in [LM1, Section 3], where subsets of

30

integers arising from shifts of ﬁnite type are deﬁned and studied.

Proposition 3.10. The r-language sets AΣ, BΣ ⊆ N0 corresponding to any non-empty sub-
shift Σ ⊆ ΛN0
r are ×r-invariant sets, and have discrete mass and Hausdorﬀ dimensions equal
to the normalized topological entropy of the symbolic subshift (Σ, σ), i.e.,

dimH AΣ = dimM AΣ = dimH BΣ = dimM BΣ = htop(Σ, σ)
log r . (3.5)

Moreover, for any ×r-invariant set B ⊆ N0, there exists a subshift Σ ⊆ ΛN0
r such that B
coincides with the r-language set BΣ associated to Σ.

Remark 3.11. The second part of Proposition 3.10 does not hold with AΣ in place of BΣ
in general. As an example, let k ∈ N and put B := {0, 1, 2, . . . , k} ⊆ N0. It is clear that for
any r ⩾ 2, the set B is a ×r-invariant set. However, note that for any subshift Σ, the set AΣ
is either {0} or inﬁnite, so we can not have that AΣ = B.

Proposition 3.10 shows that r-language sets 1) provide us with a natural way of producing
examples of ×r-invariant subsets of the non-negative integers; and 2) allow us to employ tools
and techniques from symbolic dynamics to study ×r-invariant sets. Before the proof, we give
some examples of ×r-invariant subsets of N0 arising this way.

Examples 3.12. In each of the examples below, the language of the subshift Σ used to
generate the r-language set AΣ is invariant under reversing words. Therefore, in each example,
BΣ = AΣ.
• The classical golden mean shift is the subshift of {0, 1}N0 consisting of all binary se-
quences with no two consecutive 1’s. This leads to a natural example of a ×2-invariant
set Agolden ⊆ N0 consisting of all integers whose binary digit expansion does not contain
two consecutive 1’s. Since the topological entropy of the golden mean shift is known
the equal log((1 + √5)/2) (cf. [LM2, Example 4.1.4]), it follows from Proposition 3.10
that the dimension of Agolden equals log((1 + √
5)/2)/ log 2. Integer sets corresponding
to the broader class of subshifts of ﬁnite type were also considered by Lima and Moreira
in [LM1].
• The even shift is the subshift of {0, 1}N0 consisting of all binary sequences so that
between any two 1’s there are an even number of 0’s. The corresponding ×2-invariant
set Aeven ⊆ N0 consists of all integers whose binary digit expansion has an even number
of 0’s between any two 1’s. Since the topological entropy of the golden mean shift
coincides with the topological entropy of the even shift (cf. [LM2, Example 4.1.6]), we
conclude that Aeven and Agolden have the same dimension.
• The prime gap shift is the subshift of {0, 1}N0 consisting of all binary sequences such
that there is a prime number of 0’s between any two 1’s. This corresponds to the
×2-invariant set Aprime ⊆ N0 of all those numbers written in binary in which there
is a prime number of 0’s between any two 1’s. For example, the ﬁrst 17 elements of
Aprime are: 0, 1, 2, 4, 8, 9, 16, 17, 18, 32, 34, 36, 64, 65, 68, 72, 73. The entropy of the prime
gap shift is approximately 0.30293, (cf. [LM2, Exercise 4.3.7]) which implies that the
dimension of Aprime is approximately 0.437.

Proof of Proposition 3.10. Let Σ ⊆ ΛN0
r be a subshift, and let AΣ and BΣ be the associated
r-language sets. We begin with the proof that the set AΣ is ×r-invariant. Note ﬁrst that
0 ∈ AΣ because the empty word is in L(Σ). Let n ∈ AΣ, n ⩾ 1. Because Σ is shift-invariant,

31

there exists a word w = w0 · · · wℓ−1 ∈ L(Σ) such that w0 ̸= 0 and (w)r = n. We see that

Rr(n) = (w0 · · · wℓ−2)r and Lr(n) = (w1 . . . wℓ−1)r.

Since L(Σ) is closed under preﬁxes, Rr(n) ∈ AΣ, and since Σ is shift-invariant, Lr(n) ∈ AΣ.
This shows that AΣ is ×r-invariant. The proof that BΣ is ×r-invariant is identical, only with
the order of letters reversed.
Next we will show (3.5). Since AΣ and BΣ are ×r-invariant, it follows from Proposition 3.6
that dimH AΣ = dimM AΣ and dimH BΣ = dimM BΣ. Therefore, it suﬃces to verify that
dimM AΣ = dimM BΣ = htop(Σ, T )/ log r.
Let Lℓ(Σ) denote the set of words of length ℓ appearing in the language set L(Σ), i.e.,

Lℓ(Σ) := {
w0w1 · · · wℓ−1 ∣
∣ w = w0w1 · · · ∈ Σ}.

It is well known (see, for instance, [Wal, Theorem 7.13 (i)]) that the topological entropy of
(Σ, σ) is given by
 htop(Σ, σ) = lim
ℓ→∞ 1
ℓ log |Lℓ(Σ)|, (3.6)

where the limit as ℓ → ∞ on the right hand side is known to exist. We claim that for all
ℓ ∈ N0,
 ∣
∣Lℓ(Σ)
∣
∣ ⩽ ∣
∣AΣ ∩ [0, rℓ)
∣
∣ ⩽ ∣
∣ ℓ⋃

k=0 Lk(Σ)
∣
∣. (3.7)

Indeed, the ﬁrst inequality follows immediately from the fact that ( · )r : Λℓ
r → [0, rℓ) is
injective. For the second inequality, associate to each n ∈ AΣ ∩ [0, rℓ) a word w ∈ L(Σ) such
that w0 ̸= 0 and (w)r = n. Since n < rℓ, |w| ⩽ ℓ. The second inequality follows then from
the fact that the association just described is bijective.
Using the fact that the limit in (3.6) exists, it is a short exercise to show that limℓ→∞
log ∣
∣ ∪ℓ
k=0 Lk(Σ)
∣
∣/ℓ exists and is equal to htop(Σ, σ). It follows from the inequalities in (3.7)
that dimM AΣ = htop(Σ, T )/ log r. The same argument shows that similarly dimM BΣ =
htop(Σ, T )/ log r, verifying the equality in (3.5).
Finally, suppose B ⊆ N0 is a ×r-invariant set. We will prove that there exists a subshift
Σ ⊆ ΛN0
r for which BΣ = B. Let Σ(ℓ) denote the set of all inﬁnite words w0w1 · · · ∈ ΛN0
r for
which (wℓ−1 · · · w0)r ∈ B, and deﬁne
 Σ := ⋂

ℓ∈N Σ(ℓ−1). (3.8)

Being an intersection of closed sets, Σ is closed. From Rr(B) ⊆ B, it follows that σ(Σ(ℓ)) ⊆
Σ(ℓ), whereby σ(Σ) ⊆ Σ. This proves that (Σ, σ) is a subshift. From the construction, it is
clear that BΣ ⊆ B.
On the other hand, if (wℓ−1 · · · w0)r ∈ B, then the inﬁnite word w0 · · · wℓ−100 · · · ∈ Σ. It
follows that (wℓ−1 · · · w0)r ∈ BΣ, showing that B = BΣ.

We note that the identiﬁcation of ×r-invariant subsets of N0 and subshifts of ΛN0
r given
by Proposition 3.10 is not bijective. The subshift Σ deﬁned in (3.8) can be shown to be the
largest such that BΣ = B, but in general there can be inﬁnitely many distinct subshifts Σ′

such that BΣ′ = B.
 32

As a corollary to Proposition 3.10 we obtain the following result, which plays an important
role in most of our main results.

Corollary 3.13. For any ×r-invariant A ⊆ N0, the set

A
′ := ⋂

k∈N0
 ⋂

ℓ∈N0 R
k
r Lℓ
r(A)

satisﬁes Rr(A′) = Lr(A′) = A′ (in particular, A′ is ×r-invariant) and dimH A′ = dimM A′ =
dimM A.

Proof. Note that A′ is the largest subset of A satisfying Rr(A′) = Lr(A′) = A′; in particular,
it is ×r-invariant. Therefore, to prove dimM A′ = dimM A, it suﬃces to ﬁnd a subset A′′ ⊆ A
satisfying Rr(A′′) = Lr(A′′) = A′′ and dimM A′′ = dimM A. Appealing to Proposition 3.6,
this would also prove that dimH A′ = dimM A. If dimM A = 0, then there is nothing to show,
so let us proceed under the assumption that dimM A > 0.
According to Proposition 3.10, we can ﬁnd a subshift Σ ⊆ ΛN0
r such that A coincides with
the r-language set BΣ associated to Σ. Let µ be an ergodic σ-invariant Borel probability
measure on Σ of maximal entropy (the existence of such a measure follows from, e.g. [Wal,
Theorem 8.2 + Theorem 8.7 (v)]). Let Σ′′ denote the support of µ, and observe that (Σ′′, σ)
is a subshift of (Σ, σ) with htop(Σ, σ) = htop(Σ′′, σ). Moreover, since µ is ergodic, almost
every point in Σ′′ has a dense orbit (by Birkhoﬀ’s ergodic theorem) and almost every point
is recurrent (by Poincar´e’s recurrence theorem). Therefore there exists a point x ∈ Σ′′ which
visits every non-empty open set in Σ′′ inﬁnitely often.
Let A′′ ⊆ N0 be the r-language set associated to Σ′′, i.e., A′′ = BΣ′′. Since Σ′′ ⊆ Σ, we have
A′′ ⊆ A. Also, by Proposition 3.10, dimM A = htop(Σ, σ)/ log r, dimM A′′ = htop(Σ′′, σ)/ log r,
and htop(Σ, σ) = htop(Σ′′, σ), which implies dimM A = dimM A′′. All that remains to be shown
is that Rr(A′′) = Lr(A′′) = A′′.
Since A′′ is an r-language set, it is ×r-invariant, so we already have the inclusions

Rr(A
′′) ⊆ A
′′ and Lr(A
′′) ⊆ A
′′.

To prove the reverse inclusions, let n ∈ A′′, and let w0 · · · wℓ−1 ∈ L(Σ′′) be such that n =
(wℓ−1 · · · w0)r ∈ A′′. Since the point x visits every open set of Σ′′ inﬁnitely often, the word
w0 · · · wℓ−1 appears in x inﬁnitely often. This implies that x cannot be equal to w0 · · · wℓ−10∞

and so there exists a non-zero letter u ∈ Λr and some k ∈ N0 such that the word w0 · · · wℓ−10ku
appears in x and hence in L(Σ′′). Now (u0kwℓ−1 · · · w0)r ∈ A′′ and Lr(u0kwℓ−1 · · · w0)r =
(wℓ−1 · · · w0)r = n, showing that A′′ ⊆ Lr(A′′).
Invoking again the fact that the word w0 · · · wℓ−1 appears inﬁnitely often in x, there must
exist a letter v ∈ Λr such that the word vw0 · · · wℓ−1 appears in x and hence belongs to L(Σ′′).
Now (wℓ−1 · · · w0v)r ∈ A′′ and Rr(wℓ−1 · · · w0v)r = n, showing that A′′ ⊆ Rr(A′′).

A well-known fact from geometric measure theory states that if X ⊆ [0, 1] is multiplica-
tively invariant and has Hausdorﬀ dimension 1 then X = [0, 1] (see [Fur2, discussion after
Conjecture 2]). The following corollary of Proposition 3.10 oﬀers a discrete analogue of this
result and may be of independent interest.

Corollary 3.14. If A ⊆ N0 is multiplicatively invariant and dimM A = 1, then A = N0.

33

Proof. Suppose A is ×r-invariant with dimM A = 1. It follows from Proposition 3.6 that
dimM A = 1. In view of Proposition 3.10, there exists a subshift Σ ⊆ ΛN0
r such that A = BΣ
and htop(Σ, σ) = log r. However, the only subshift of ΛN0
r with full entropy is the full shift.
Hence Σ = ΛN0
r , which implies A = BΣ = N0.

3.4. Connections to fractal geometry of the reals

The purpose of this subsection is to establish a connection between ×r-invariant subsets of
the non-negative integers and ×r-invariant subsets of [0, 1]. Recall that X ⊆ [0, 1] is called
×r-invariant if it is closed and TrX ⊆ X, where Tr : x ↦→ rx mod 1.
First, we remark that every ×r-invariant subset of [0, 1] can be “lifted” to a ×r-invariant
subset of N0. Indeed, if X ⊆ [0, 1] is ×r-invariant, then one can show that the set
{⌊rkx⌋ | x ∈ X, k ∈ N0}

is ×r-invariant. We will not make use of this fact, so we leave the details to the interested
reader. Of more importance to us is the converse direction, stated in the following proposition.
Recall from Section 2.1 the deﬁnition of Hausdorﬀ distance.

Proposition 3.15. For any ×r-invariant set A ⊆ N0, the sequence Xk := (A ∩ [0, rk))/rk

converges with respect to the Hausdorﬀ metric dH as k → ∞ to a ×r-invariant set X ⊆ [0, 1]
satisfying dimM X = dimM A.

We remark that by Lemma 2.12 and Proposition 3.6, the Minkowski and Hausdorﬀ di-
mensions of multiplicatively invariant sets in N0 and [0, 1] coincide. Thus, either dimension
can be used in the conclusion of Proposition 3.15. For the proof of the proposition, we will
need two technical lemmas.

Lemma 3.16. Let A ⊆ N0, and deﬁne Xk := (A ∩ [0, rk))/rk.
(I) If Rr(A) ⊆ A, then for any k, l ∈ N with l ⩾ k, we have Xl ⊆ [Xk]r−k .
(II) If Rr(A) ⊇ A, then for any k, l ∈ N with l ⩾ k, we have Xk ⊆ [Xl]r−k .
In particular, if Rr(A) = A then for all l ⩾ k, we have dH(Xl, Xk) ⩽ r−k.

Proof. It is helpful to note ﬁrst that for all n, l, k ∈ N with l ⩾ k,
∣
∣
∣
∣ n
rl − Rl−k
r (n)
rk
 ∣
∣
∣
∣ ⩽ 1
rk . (3.9)

This inequality follows easily from the fact that Rl−k
r (n) = ⌊n/rl−k⌋. For the proof of
part (I), let y ∈ Xl and write y = m/rl for some m ∈ A. Note that ˜m := Rl−k
r (m) belongs to
A ∩ [0, rk) because Rr(A) ⊆ A. Then, setting ˜y := ˜m/rk, we see that ˜y ∈ Xk and, by (3.9),
d(y, ˜y) ⩽ r−k. This proves Xl ⊆ [Xk]r−k .
Next, we prove part (II). For any x ∈ Xk we can ﬁnd n ∈ A ∩ [0, rk) such that x = n/rk.
Since A ⊆ Rl−k
r (A), there exists ˜n ∈ A ∩ [0, rl) such that

R
l−k
r (˜n) = n.

Now ˜x := ˜n/rl belongs to Xl and it follows from (3.9) that d(x, ˜x) ⩽ r−k. This proves
Xk ⊆ [Xl]r−k .
 34

Lemma 3.17. Suppose A ⊆ N0 satisﬁes Rr(A) ⊆ A, and deﬁne A′ := ⋂k∈N Rk
r (A). Also,
set Xk := (A ∩ [0, rk))/rk and X ′
k := (A′ ∩ [0, rk))/rk. Then limk→∞ dH(Xk, X ′
k) = 0.

Proof. Let ε > 0, and let m ∈ N such that 2r−m < ε. Since Rr(A) ⊆ A, we have

A ∩ [0, rm) ⊇ Rr(A) ∩ [0, rm) ⊇ R
2
r(A) ∩ [0, rm) ⊇ R
3
r(A) ∩ [0, rm) ⊇ . . . .

In particular, the sequence k ↦→ Rk
r (A) ∩ [0, rm) eventually stabilizes, which happens exactly
when Rk
r (A) ∩ [0, rm) = A′ ∩ [0, rm). It follows from (3.9) that

Xk ⊂ [ Rk−m
r (A) ∩ [0, rm)
rm
 ]
r−m .

Therefore, for large enough k, Xk ⊂ [X ′
m]r−m. On the other hand it is clear that X ′
k ⊂ Xk.
Finally, since from Lemma 3.16 we have that dH (X ′
k, X ′
m) < r−m, we conclude that X ′
k ⊂
Xk ⊂ [X ′
m]r−k ⊂ [X ′
k]2r−m, when it follows that dH (Xk, X ′
k) < ε.

Proof of Proposition 3.15. Deﬁne A′ := ⋂k∈N0 Rk
r (A) and X ′
k := (A′ ∩ [0, rk))/rk. In view
of Lemma 3.17, the sequence k ↦→ Xk converges with respect to the Hausdorﬀ metric if and
only if the sequence k ↦→ X ′
k converges. Since A′ = Rr(A′), it follows from Lemma 3.16 that

dH(X ′
k, X ′
l ) ⩽ r−k, for all k, l ∈ N with l ⩾ k.

This implies that k ↦→ X ′
k is a Cauchy sequence, and hence it is convergent (recall that by
the Blaschke selection theorem, the set of all non-empty, compact subsets of [0, 1] equipped
with the Hausdorﬀ distance is a complete metric space). Let X ′ = limk→∞ X ′
k, and note that
X ′ ⊆ X.
Next, let us show that X is ×r-invariant. Since Lr(A) ⊆ A, a simple computation shows
Tr(Xk) ⊆ Xk−1. Therefore, using X = limk→∞ Xk and the fact that Tr is continuous on
[0, 1)\{0, 1
r , . . . , r−1
r }, we get that for any closed set C ⊆ [0, 1)\{0, 1
r , . . . , r−1
r },

Tr(X ∩ C) = Tr( lim
k→∞
(Xk ∩ C)
)

= lim
k→∞ Tr(Xk ∩ C)

⊆ lim
k→∞ Tr(Xk)

⊆ lim
k→∞ Xk−1

= X.

It follows that Tr(X\{0, 1
r , . . . , r−1
r }) ⊆ X. Since 0 ∈ X, we obtain T ({0, 1
r , . . . , r−1
r }) ⊆ X,
and hence Tr(X) ⊆ X, as desired.
Finally, we must show dimM X = dimM A. As guaranteed by Corollary 3.13, dimM A =
dimM A′. By combining part (I) of Lemma 3.16 with Lemma 2.5, we see that

0 ⩽ lim inf
k→∞
 ( log N (Xk, r−k)

k log r − log N (X, r−k)

k log r
 )

= dimM A − lim sup
k→∞
 log N (X, r−k)

k log r ,
 (3.10)

where the equality follows from the fact that dimM A = limk→∞ 1
k log r log N (Xk, r−k) (cf.

35

equation (3.1)). On the other hand, using part (II) of Lemma 3.16, Lemma 2.5, and the fact
that dimM A′ = limk→∞ 1
k log r log N (X ′
k, r−k), we see

0 ⩽ lim inf
k→∞
 ( log N (
X ′, r−k)

k log r − log N (X ′
k, r−k)

k log r
 )

= lim inf
k→∞ log N (
X ′, r−k)

k log r − dimM A
′.
 (3.11)

Combining (3.10) and (3.11) with the fact that X ′ ⊆ X, we see

dimM A
′ ⩽ lim inf
k→∞ log N (X ′, r−k)

k log r ⩽ lim sup
k→∞
 log N (
X, r−k)

k log r ⩽ dimM A.

Since dimM A = dimM A′ and X ′ ⊆ X, we conclude that dimM X exists and is equal to
dimM A.

4. Transversality between multiplicatively invariant subsets
of the integers

In this section, we prove our main results, Theorems A, B, C, and D. As in the other sections,
the positive integers r and s are ﬁxed, and the implicit constants appearing in asymptotic
notation may depend on r and s without further indication.

4.1. Sets which are simultaneously multiplicatively invariant

In this subsection we give a proof of Theorem A. We follow the notation and terminology
established in Section 3.2. We say that a non-negative integer n begins with the word w in
base s if there exists d ∈ N0 and n0 ∈ [0, sd) such that

n = (w)ssd + n0. (4.1)

If w = w0 · · · wℓ−1 and w0 ̸= 0, this means that the ℓ most signiﬁcant digits in the base-s
expansion of n are w0, w1, . . . , wℓ−1, in order.

Lemma 4.1. For all w ∈ Λℓ
s, there is an arc Iw ⊆ [0, 1) modulo 1 (meaning that Iw is an
interval when 0 and 1 are identiﬁed) with the property that for all x ⩾ (w)s, the integer ⌊x⌋
begins with w in base s if and only if {log x/ log s} ∈ Iw.

Proof. Let w ∈ Λℓ+1
s . It follows from (4.1) that a positive integer n begins with w in base s
if and only if there exists d ∈ N0 such that

(w)ssd ⩽ n < ((w)s + 1)sd.

Therefore, a positive real number x has the property that ⌊x⌋ begins with w in base s if and
only if there exists d ∈ N0 such that

(w)ssd ⩽ x < (
(w)s + 1)sd.

36

The previous inequality is equivalent to

log(w)s
log s + d ⩽ log x
log s < log (
(w)s + 1
)

log s + d. (4.2)

Let Iw be the modulo 1 arc from the fractional part of log(w)s/ log s to the fractional part
of log ((w)s + 1
)/ log s in the positive direction. We see that for all x ⩾ (w)s, the integer ⌊x⌋
begins with w in base s if and only if (4.2) holds, which happens if and only if { log x/ log s} ∈
Iw.
 Recall from Section 2.1 that [A]δ denotes the δ-neighborhood of A.

Lemma 4.2. Let r and s be multiplicatively independent positive integers, and let A ⊆ N0
be ×r invariant and inﬁnite. If λ, δ > 0, τ ∈ R, and B ⊆ N0 are such that λA + τ ⊆ [B]δ,
then for all w ∈ Λ∗
s, there exists an integer in B that begins with w in base s.

Proof. Let w ∈ Λ∗
s, and let Iw be the arc from Lemma 4.1. Let I ′
w be the middle 3rd
subinterval of Iw, and let ξ be the length of I ′
w. Deﬁne α = log r/ log s. Since α is irrational,
there exists K ∈ N such that the set {{iα} | i ∈ {0, . . . , K}
} is ξ-dense in [0, 1).
Since A is inﬁnite, there exists n ∈ A suﬃciently large (to be speciﬁed momentarily)
such that λn/sK + τ ⩾ (w)s + δ + λ. Since A is Rr-invariant, n, ⌊n/r⌋, . . . , ⌊n/rK⌋ are
all elements of A. Let i ∈ {0, . . . , K}. Since λA + τ ⊆ [B]δ, the real number λ⌊n/ri⌋ + τ
is within a distance δ of the set B. Therefore, there exists ti ∈ R, |ti| ⩽ λ + δ, such that
λn/ri + τ + ti ∈ B.
By the mean value theorem, ensuring that n is suﬃciently large, we see that for all
i ∈ {0, . . . , K}, ∣
∣
∣
∣
∣ log (
λn/ri + τ + ti)

log s − log (
λn/ri)

log s
 ∣
∣
∣
∣
∣ < ξ. (4.3)

It follows from the fact that log (λn/ri)/ log s = log(λn)/ log s − iα and from our choice of
K that there exists i ∈ {0, . . . , K} such that { log (λn/ri)/ log s} ∈ I ′
w. It follows from (4.3)
and the deﬁnition of ξ that { log (λn/ri + τ + ti)
/ log s} ∈ Iw. By our choice of n and the
fact that i ⩽ K, we have that λn/ri + τ + ti ⩾ (w)s. Therefore, Lemma 4.1 gives that
λn/ri + τ + ti, an integer in B, begins with the word w in base s, as was to be shown.

Proof of Theorem A. Let r and s be multiplicatively independent positive integers, and let
A, B ⊆ N0 be ×r- and ×s-invariant sets, respectively. Suppose λ, η > 0, σ, τ ∈ R and δ > 0
are such that λA + τ ⊆ [ηB + σ]
δ. We need to show that then either A is ﬁnite or B = N0.
Suppose A is inﬁnite; we will argue that B = N0. Since B is ×s-invariant, it suﬃces to
show that for all w ∈ Λ∗
s, there exists an integer in B that begins with w in base s.
Let w ∈ Λ∗
s. It follows from (1.11) that λ′A + τ ′ ⊆ [B]δ′, where λ′ = λ/η, τ ′ = (τ − σ)/η
and δ′ = δ/η. Since A is ×r-invariant and inﬁnite, Lemma 4.2 gives that some integer in B
begins with w ∈ Λ∗
s in base s, as was to be shown.

4.2. Intersections of multiplicatively independent invariant sets

In this subsection, we prove Theorem B, showing that ×r- and ×s-invariant sets are geomet-
rically transverse in the sense that the dimension of the intersection of one with any aﬃne
image of the other is small. In fact we prove the following stronger version.

37

Theorem 4.3. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant sets, respectively. Deﬁne γ = max (0, dimH A + dimH B − 1
).
For every compact set I ⊆ R\{0} and ε > 0,

lim
N →∞ sup
λ,η∈I
σ,τ ∈R
 ∣
∣
⌊λ(A ∩ [0, N )) + τ ⌋ ∩ ⌊η(B ∩ [0, N )) + σ⌋∣
∣

N γ+ε = 0. (4.4)

In particular, for all λ, η, σ, τ ∈ R,

dimM (⌊λA + τ ⌋ ∩ ⌊ηB + σ⌋
) ⩽ max (0, dimH A + dimH B − 1
). (4.5)

Proof. Let I ⊆ R\{0} be compact and ε > 0. Since ⌊λ(A∩[
0, N ))+τ ⌋ ⊆ [λ(A∩[
0, N ))+τ ]
1
and ⌊η(B ∩ [
0, N )) + σ⌋ ⊆ [η(B ∩ [
0, N )) + σ]
1, the cardinality in the numerator on the left
hand side of (4.4) is bounded from above by

N ([λ
(
A ∩ [
0, N )) + τ ]
1 ∩ [η(B ∩ [0, N )) + σ]
1, 1
),

which is quickly seen to be equal to

N
 ([

λ
 ( A ∩ [0, N )

N
 )
 + τ
N
 ]
N −1 ∩
 [
η
 ( B ∩ [0, N )

N
 )
 + σ
N
 ]
N −1 , N −1)
 . (4.6)

Deﬁne for every k, ℓ ∈ N the sets

Xk := A ∩ [0, rk)
rk and Yℓ := B ∩ [0, sℓ)
sℓ .

Deﬁne kN := ⌊log N/ log r⌋ + 1 and ℓN := ⌊log N/ log s⌋ + 1, and note that

N = rkN r{log N/ log r}−1 = sℓN s{log N/ log s}−1.

Since N ⩽ min(rkN , sℓN ), we have that A ∩ [0, N ) ⊆ A ∩ [0, rkN ) and B ∩ [0, N ) ⊆ B ∩ [0, sℓN ).
Therefore, the expression in (4.6) is bounded from above by

N ([λr1−{log N/ log r}XkN + τ /N ]
N −1 ∩ [ηs1−{log N/ log s}YℓN + σ/N ]
N −1, N −1).

Since I ⊆ R\{0} is compact, there exists t > 1 such that I ⊆ ±[t−1, t]. If λ and η belong
to I, then λr1−{log N/ log r} and ηs1−{log N/ log s} belong to J := ±[t−1, max(r, s)t]. Therefore,
to show (4.4), it suﬃces to prove

lim
N →∞ sup
λ,η∈J
σ,τ ∈R
 N ([λXkN + τ ]
N −1 ∩ [ηYℓN + σ]
N −1, N −1)

N γ+ε = 0. (4.7)

In view of Proposition 3.15, the limits X := limk→∞ Xk and Y := limℓ→∞ Yℓ exist
in the Hausdorﬀ metric. Moreover, X and Y are ×r- and ×s-invariant, respectively, and
dimH X = dimH A, dimH Y = dimH B. By Lemma 3.16, we have that dH (XkN , X) ⩽ N −1

and dH(YℓN , Y ) ⩽ N −1. Put a = max J, and note that for all λ, η ∈ J and σ, τ ∈ R,
[λXkN + τ ]
N −1 ∩ [
ηYℓN + σ]
N −1 ⊆ [λX + τ ]
aN −1 ∩ [ηY + σ]
aN −1. (4.8)

We can now manipulate the left hand side of (4.7) using (4.8), Lemma 2.6, and Corol-

38

lary 2.19 (with J as I), to get

lim sup
N →∞ sup
λ,η∈J
σ,τ ∈R
 N ([λXkN + τ ]
N −1 ∩ [ηYℓN + σ]
N −1, N −1)

N γ+ε

⩽ lim sup
N →∞ sup
λ,η∈J
σ,τ ∈R
 log N ([λX + τ ]
aN −1 ∩ [ηY + σ]
aN −1 , N −1)

N γ+ε

≪ lim
N →∞ sup
λ,η∈J
σ,τ ∈R
 N ([λX + τ ]
aN −1 ∩ [
ηY + σ]
aN −1, aN −1)

(aN )γ+ε = 0.

This veriﬁes (4.7) and concludes the proof of (4.4).
To show (4.5), let λ, η, σ, τ ∈ R. Put M = 3 max (
|λ|−1, |η|−1), and note that for all
N ⩾ max (
|σ|, |τ |
),
⌊λA + τ ⌋ ∩ ⌊ηB + σ⌋ ∩ [0, N ) ⊆ ⌊λ(
A ∩ [0, M N )) + τ ⌋ ∩ ⌊η(B ∩ [0, M N )) + σ⌋.

It follows from this containment and (4.4) that for all ε > 0,

1
M γ+ε lim
N →∞
 ∣
∣
⌊λA + τ ⌋ ∩ ⌊ηB + σ⌋ ∩ [0, N )∣
∣

N γ+ε = 0.

This proves (4.5) and concludes the proof of the theorem.

Remark 4.4. We note two modiﬁcations to the statement of Theorem 4.3 that can be proved
with minor corresponding modiﬁcations made to the proof. First, the initial interval [0, N )
can be replaced by an interval symmetric about the origin, (−N, N ). Though A and B
consist of positive integers, this is meaningful because the theorem allows for λ and/or η
to be negative. Second, using the ﬂoor function to round to the integer lattice is a mere
convenience: the result hold when the sets λX + τ and ηY + σ are rounded to any other
discrete subgroup (or translate of a discrete subgroup) of R.

4.3. Sums of multiplicatively independent invariant sets

In this subsection, we prove Theorem C, showing that sets which are multiplicatively invariant
with respect to multiplicatively independent bases are transverse in an additive combinatorial
sense. The results can be phrased in terms of the size (cardinality or Hausdorﬀ content) of
ﬁnite subsets of multiplicatively invariant sets. The upper bounds on the size of the sumsets
are contained in Lemma 4.5 and follow from general considerations. The diﬃculty in the main
results is in proving the lower bounds, which are handled in Theorem 4.6 and are derived
from their continuous counterparts in Theorem 2.21.

Lemma 4.5. For all ﬁnite, non-empty A′, B′ ⊆ N0, all λ, η > 0, and all 0 ⩽ γ ⩽ 1,
∣
∣
⌊λA
′ + ηB′⌋∣
∣ ⩽ ∣
∣A
′ × B′∣
∣, (4.9)

Hγ
⩾1(⌊λA
′ + ηB′⌋) ≪max(λ,η) Hγ
⩾1(A
′ × B′). (4.10)

Moreover, for all A, B ⊆ N0, all dim ∈ {dimM , dimM , dimH , dimH }, and all λ, η > 0,

dim (⌊λA + ηB⌋
) ⩽ min (
1, dim(A × B)
).

39

Proof. Let A′, B′ ⊆ N0 be ﬁnite, non-empty, let λ, η > 0, and let 0 ⩽ γ ⩽ 1. Denote by
ϕ : R2 → R the map ϕ(x, y) = λx + ηy; it is Lipschitz with Lipschitz constant max(λ, η).
Note that ϕ(A′ × B′) = λA′ + ηB′.
The upper bound in (4.9) follows from the fact that |⌊ϕ(A′ × B′)⌋| ⩽ |ϕ(A′ × B′)| ⩽
|A′ × B′|, while the upper bound in (4.10) follows from Lemma 2.5 and Lemma 2.7 via

Hγ
⩾1(⌊ϕ(A
′ × B′)⌋
) ≍ Hγ
⩾1(
ϕ(A
′ × B′)
) ≪max(λ,η) Hγ
⩾1(A
′ × B′).

To prove the dimension inequality for A, B ⊆ N0, note that there exists M ∈ N, depending
only on max(λ, η), such that for all N ∈ N,
⌊λA + ηB⌋ ∩ [0, N ) ⊆ ⌊λ(A ∩ [0, N M )) + η(B ∩ [0, N M ))
⌋. (4.11)

Let dim ∈ {dimM , dimM , dimH , dimH }, and let γ > dim(A × B). It follows from (4.9), (4.10),
and (4.11) that ∣
∣
⌊λA + ηB⌋ ∩ [0, N )
∣
∣

N γ ⩽ M γ ∣
∣
(A × B) ∩ [0, N M )2∣
∣

(N M )γ ,

Hγ
⩾1(⌊λA + ηB⌋ ∩ [0, N )
)

N γ ≪max(λ,η) M γ Hγ
⩾1((
A × B) ∩ [0, N M )2)

(N M )γ .

Considering the ﬁrst or second inequality (if dim is the discrete Minkowski or Hausdorﬀ
dimension, respectively), the limit inﬁmum or limit supremum (if dim is a lower or upper
dimension, respectively) of the quantity on the right hand side is equal to zero because
γ > dim(A × B). It follows that dim (⌊λA + ηB⌋
) ⩽ γ. This suﬃces for the conclusion of the
lemma since γ > dim(A × B) was arbitrary and since dim (⌊λA + ηB⌋
) is clearly bounded
from above by 1.

Theorem 4.6. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant sets, respectively. Deﬁne γ = max(0, dimH(A × B) − 1). For all
compact I ⊆ (0, ∞), all 0 ⩽ γ ⩽ 1, all ε > 0, all suﬃciently large N (depending on A, B, I,
γ, and ε), all non-empty A′ ⊆ A ∩ [0, N ) and B′ ⊆ B ∩ [0, N ), and all λ, η ∈ I,

∣
∣
⌊λA
′ + ηB′⌋∣
∣ ⩾
 ∣
∣A′ × B′∣
∣

N γ+ε , and (4.12)

Hγ
⩾1(⌊λA′ + ηB′⌋)

N γ ≫I,γ,ε Hγ+γ+ε
⩾1 (A′ × B′)

N γ+γ+ε . (4.13)

Proof. For all k, ℓ ∈ N, deﬁne the sets

Xk := A ∩ [0, rk)
rk and Yℓ := B ∩ [0, sℓ)
sℓ .

Let X = limk→∞ Xk and Y = limℓ→∞ Yℓ in the Hausdorﬀ metric; Proposition 3.15 gives that
these limits exist, that X and Y are ×r- and ×s-invariant subsets of [0, 1], respectively, and
that dimH X = dimH A and dimH Y = dimH B. For N ∈ N, deﬁne kN := ⌊log N/ log r⌋ + 1
and ℓN := ⌊log N/ log s⌋ + 1, and note that

N = rkN r{log N/ log r}−1 = sℓN s{log N/ log s}−1. (4.14)

40

By Lemma 3.16, we have that

dH (XkN , X) ⩽ N −1 and dH(YℓN , Y ) ⩽ N −1. (4.15)

Let I ⊆ (0, ∞) be compact, 0 ⩽ γ ⩽ 1, and ε > 0. Deﬁne J := [min I, rs max I]. Next we
invoke Theorem 2.21 with J in place of I and either ε/2 in place of ε (to prove (4.12)) or ε
as it is (to prove (4.13)). Let N be suﬃciently large, to be speciﬁed later, but in particular
so that ρ := 1/N is suﬃciently small for Theorem 2.21 to apply (with ε as either ε/2 or ε).
Let A′ ⊆ A ∩ [0, N ) and B′ ⊆ B ∩ [0, N ) be non-empty, and λ, η ∈ I. It follows from
(4.14) that N ⩽ min(rkN , sℓN ), whereby

A′

rkN ⊆ XkN and B′

skN ⊆ YkN .

Combining these facts with (4.15), it follows from Lemma 2.4 that there exist non-empty
compact sets X ′ ⊆ X and Y ′ ⊆ Y such that

dH
 (X ′, A′

rkN
 ) ⩽ N −1 and dH
 (Y ′, B′

sℓN
 ) ⩽ N −1. (4.16)

Deﬁne λ′ = rkN λ/N = r1−{log N/ log r}λ and η′ = sℓN η/N = s1−{log N/ log s}η. Note that
λ′, η′ ∈ J and that
 λ
′ A′

rkN + η′ B′

sℓN = λA′ + ηB′

N . (4.17)

Combining (4.16) and (4.17) with basic properties of the Hausdorﬀ distance, we see that

dH
 (λ
′X ′ + η′Y ′, λA′ + ηB′

N
 ) ⩽ 2rs max(I)N −1, and (4.18)

dH
 (X ′ × Y ′, A′

rkN × B′

sℓN
 ) ⩽ N −1. (4.19)

It follows from Lemma 2.7 and (4.19) that

N (X ′ × Y ′, N −1) ≍ N ( A′ × B′

N , N −1) = N (
A
′ × B′, 1
) = |A
′ × B′|, and (4.20)

Hγ+γ+ε
⩾N −1 (X ′ × Y ′) ≍ Hγ+γ+ε
⩾N −1
 ( A′ × B′

N
 ) = Hγ+γ+ε
⩾1 (A′ × B′)
N γ+γ+ε . (4.21)

Appealing to (4.18), Lemma 2.5, Theorem 2.21 (with ε/2 as ε), and (4.20), we see that

|⌊λA
′ + ηB′⌋| ≍ N (
λA
′ + ηB′, 1
) = N ( λA′ + ηB′

N , N −1)

≍I N (λ
′X ′ + η′Y ′, N −1) ⩾ N (X ′ × Y ′, N −1)

N γ+ε/2 ≍ |A′ × B′|
N γ+ε/2 .

Thus, there exists a constant C > 0 depending only on r, s, and I for which |⌊λA′ + ηB′⌋| ⩾
|A′ × B′|/(CN γ+ε/2). The inequality in (4.12) follows as long as N ε/2 > C.
Replacing cardinality and packing number with the γ-dimensional discrete Hausdorﬀ con-
tent and appealing to (4.18), Lemma 2.5, Theorem 2.21 (with ε as ε), and (4.21) in the same

41

way, we see that

Hγ
⩾1(⌊λA′ + ηB′⌋)

N γ ≍ Hγ
⩾1(
λA′ + ηB′)

N γ = Hγ
⩾N −1
 ( λA′ + ηB′

N
 )

≍I Hγ
⩾N −1(
λ′X ′ + η′Y ′) ≫I,γ,ε Hγ+γ+ε
⩾N −1 (X ′ × Y ′) ≍ Hγ+γ+ε
⩾1 (
A′ × B′)

N γ+γ+ε .

This is precisely the inequality in (4.13), completing the proof.

In the following corollary, note that it is a consequence of Corollary 3.8 that all four dis-
crete notions of dimension, dimM , dimM , dimH , dimH , coincide for multiplicatively invariant
sets A and B and their Cartesian product A × B. In particular,

dim(A × B) = dim A + dim B

for any dim ∈ {dimM , dimM , dimH , dimH }.

Corollary 4.7. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant sets, respectively. For all dim ∈ {dimM , dimM , dimH , dimH } and
λ, η ∈ (0, ∞),
 dim (⌊λA + ηB⌋
) = min (
1, dim(A × B)
). (4.22)

Moreover, for all A′ ⊆ A and B′ ⊆ B,
• if dim A + dim B ⩽ 1, then

dim (
⌊λA
′ + ηB′⌋
) = dim (A
′ × B′); (4.23)

• if dim A + dim B > 1, then

dim (⌊λA
′ + ηB′⌋
) ⩾ dim (A
′ × B′) − dim (
A × B) + 1. (4.24)

Proof. First, note that (4.22) is a consequence of (4.23) and (4.24). Indeed, setting A′ = A
and B′ = B, if dim A + dim B ⩽ 1 then (4.22) becomes (4.23), and if dim A + dim B > 1 then
(4.24) implies that dim (
⌊λA + ηB⌋
) ⩾ 1. Since any subset of N0 has dimension at most 1,
(4.22) follows in this case as well.
Deﬁne γ = max(0, dimH(A × B) − 1), and let A′ ⊆ A and B′ ⊆ B. To show (4.23) and
(4.24), it suﬃces to show
 dim (⌊λA
′ + ηB′⌋
) ⩾ dim (A
′ × B′) − γ. (4.25)

Indeed, this is the lower bound in (4.24), and the upper bound guaranteed by Lemma 4.5
combined with this lower bound gives the desired equality in (4.23).
Let dim ∈ {dimM , dimM , dimH , dimH } and λ, η ∈ (0, ∞). If dim(A′ × B′) = 0, the
conclusion is immediate, so we can proceed under the assumption that dim(A′ × B′) > 0.
There exists M ∈ N such that for all N ∈ N,
⌊λA
′ + ηB′⌋ ∩ [0, N ) ⊇ ⌊λ(A
′ ∩ [0, N/M )
) + η(B′ ∩ [0, N/M )
)⌋.

Let ε > 0, and let γ = dim(A′ × B′) − γ − 2ε. Let N be large enough that Theorem 4.6 holds
with N/M in place of N , and deﬁne A′′ = A′ ∩ [0, N/M ) and B′′ = B′ ∩ [0, N/M ). It follows

42

from Theorem 4.6 that
∣
∣
(λA′ + ηB′) ∩ [0, N )
∣
∣

N γ ⩾ |A′′ × B′′|
N γ(N/M )γ+ε = M γ+ε |(A′ × B′) ∩ [0, N/M )2|
N γ+γ+ε ,

Hγ
⩾1(⌊λA′ + ηB′⌋ ∩ [0, N )
)

N γ ≫λ,η,γ,ε Hγ+γ+ε
⩾1 (A′′ × B′′)
N γ(N/M )γ+ε

= M γ+ε Hγ+γ+ε
⩾1 ((A′ × B′) ∩ [0, N/M )2)
N γ+γ+ε .

Consider the ﬁrst inequality if dim is the discrete Minkowski dimension and the second
inequality if dim is the discrete Hausdorﬀ dimension. Because γ + γ + ε = dim(A′ × B′) − ε,
the limit inﬁmum (if dim is a lower dimension) or limit supremum (if dim is an upper
dimension) as N tends to inﬁnity of the right hand side is positive. It follows that

dim (
⌊λA
′ + ηB′⌋
) ⩾ γ.

The inequality in (4.25) now follow from the fact that γ = dim(A′ × B′) − γ − 2ε and ε > 0
was arbitrary, concluding the proof.

4.4. An example that shows R-invariance does not suﬃce

Fix 2 ⩽ r < s. In this section, we construct two sets A, B ⊆ N0 which satisfy the following
properties:
(I) the mass dimensions of A and B exist and dimM A = dimM B = 1/2;
(II) rA ⊆ A and sB ⊆ B;
(III) Rr(A) = A and Rs(B) = B; and
(IV) dimM (A + B) ⩽ 4/5.
This example demonstrates that neither R-invariance nor the invariance indicated in (II)
suﬃce to obtain the result in Corollary 4.7. This is in contrast to Theorem A, where the
conclusion holds under the weaker assumption that the sets A and B are Rr- and Rs-invariant,
respectively. We do not know whether L-invariance alone suﬃces in either Theorem A or
Corollary 4.7, but invariance under multiplication by r and s (in the sense of (II)) does
not suﬃce to reach the conclusions in either theorem: the set of squares is invariant under
multiplication by both 4 and 9 simultaneously, but has dimension equal to 1/2, while the
sets A and B above demonstrate that Corollary 4.7 does not hold under the assumption of
invariance under multiplication.
In what follows, the interval notation [a, b] is understood to mean [a, b]∩ N0. For i, j ∈ N0,
let
 Ii = [ri, ri + r(i+1)/2], Jj = [sj, sj + s(j+1)/2],

and then deﬁne
 A = {0} ∪ ⋃

i,ℓ⩾0 rℓIi, B = {0} ∪ ⋃

j,m⩾0 smJj.

First we will verify (I) by showing that the mass dimension of A exists and is equal to

43

1/2; the argument for B is the same. It is easy to see that for all N ⩾ 1,

IN −1 ⊆ A ∩ [1, rN ) ⊆ ⋃

i,ℓ⩾0
i+ℓ⩽N
 rℓIi,

from which it follows that

rN/2 ⩽ ∣
∣A ∩ [0, rN )
∣
∣ ⩽ (N + 1)
2(r(N +1)/2 + 1).

This shows that dimM A = dimM A = dimM A = 1/2.
It is clear from the deﬁnition of the sets A and B that (II) holds.
Next we will verify (III) by showing that Rr(A) = A; the same argument works to show
that Rs(B) = B. Since rA ⊆ A, we have that

A = Rr(rA) ⊆ Rr(A) = {0} ∪ ⋃

i,ℓ⩾0 Rr(rℓIi).

Since 0 ∈ A, we need only to verify that for all i, ℓ ⩾ 0, Rr(rℓIi) ⊆ A. If ℓ ⩾ 1, then
Rr(rℓIi) = rℓ−1Ii ⊆ A. If ℓ = 0 and i = 0, then we see Rr(I0) = {0} ⊆ A. If ℓ = 0 and i ⩾ 1,
then we see Rr(Ii) = [ri−1, ri−1 + r(i−1)/2] ⊆ Ii−1 ⊆ A. Thus, Rr(A) = A.
Finally we will verify (IV) by showing that for all N suﬃciently large,
∣
∣(A + B) ∩ [0, rN )
∣
∣ ⩽ 4N 4r4N/5. (4.26)

Let σ = log s/ log r. Because
 B ∩ [1, rN ) ⊆ ⋃

i,ℓ⩾0
σ(j+m)⩽N
 smJj,

we have that ∣
∣(A + B) ∩ [0, rN )
∣
∣ ⩽ 1 + ∑

i,j,ℓ,m |rℓIi + smJj|, (4.27)

where the sum is over all i, j, ℓ, m ⩾ 0 for which i + ℓ ⩽ N and σ(j + m) ⩽ N . We will
estimate this sum from above by splitting the sum indices into two sets depending on the
“type” of the pair (i, j), which we now deﬁne.
A pair (i, j) is of Type I if
 i + 1
2 + σ j + 1
2 ⩽ 4N
5 .

Using the trivial bound |C + D| ⩽ |C||D| for ﬁnite sets C, D ⊆ N0, we see that if i, j, ℓ, and
m are such that (i, j) is of Type I, then

|rℓIi + smJj| ⩽ |Ii||Jj| = r(i+1)/2s(j+1)/2 ⩽ r4N/5. (4.28)

A pair (i, j) is of Type II if it is not of Type I, that is, if

i + 1
2 + σ j + 1
2 > 4N
5 . (4.29)

Using the fact that σj ⩽ N and that N is suﬃciently large, we see from (4.29) that (i−1)/2 >

44

N/4. It follows then from the fact that i + ℓ ⩽ N that

ℓ + i + 1
2 < 4N
5 . (4.30)

Similarly, using that i ⩽ N and the fact that N is suﬃciently large, we see from (4.29) that
σ(j − 1)/2 > N/4. It follows from the fact that σ(j + m) ⩽ N that

σ (m + j + 1
2
 ) < 4N
5 . (4.31)

Now we are in a position to use the following fact: if C, D ⊆ N0 are contained in intervals of
length L, M , respectively, then C + D is contained in an interval of length L + M and hence
|C + D| ⩽ L + M + 1. If i, j, ℓ, and m are such that (i, j) is of Type II, then

|rℓIi + smJj| ⩽ rℓ+(i+1)/2 + sm+(j+1)/2 + 1.

Using (4.30) and (4.31), we have that

|rℓIi + smJj| ⩽ 3r4N/5. (4.32)

Finally, by splitting up the sum in (4.27) into tuples for which the pairs (i, j) are of Type
I or Type II, we see by combining (4.28) and (4.32) that the desired inequality in (4.26) holds.

4.5. Iterated sums of a multiplicatively invariant set

In this section, we will prove Theorem D. The strategy is to use tools from Section 3.4 to
derive Theorem D from the theorem of Lindenstrauss-Meiri-Peres, Theorem 1.4. Throughout
this section, r ⩾ 2 is ﬁxed and all of the asymptotic notation may implicitly depend on it.

Remark 4.8. There are some useful remarks to make before the proof. Let X1, X2, . . . ,
Xn ⊆ [0, 1] be ×r-invariant sets. The sumset X1 + · · · + Xn may be interpreted in R/Z or
in R. Denote temporarily by Wn the set X1 + · · · + Xn interpreted modulo 1 as a subset of
[0, 1] and by Yn the set X1 + · · · + Xn interpreted in R as a subset of [0, n]. Two facts of
particular relevance to us are: 1) set Wn is ×r-invariant, and 2) dimH Wn = dimH Yn. The
ﬁrst fact follows easily from the fact that multiplication by r is a group endomorphism of
(R/Z, +). (In contrast, note that the sumset of ×r-invariant subsets of N0 is not necessarily
×r-invariant: if A is the base-10 restricted digit Cantor set with allowed digits 0 and 5, then
A + A contains 10 but does not contain R10(10) = 1, for example). The second fact follows
immediately by writing Wn = ∪n−1
i=0 ((Yn ∩ [i, i + 1]) − i
) and using the translation-invariance
and ﬁnite (countable) stability under unions of the Hausdorﬀ dimension.

Proof of Theorem D. Recall that (Ai)∞
i=1 is a sequence of ×r-invariant subsets of N0. For
each i ∈ N, let A′
i be the set described in Corollary 3.13, and deﬁne Xi ⊆ [0, 1] to be the
Hausdorﬀ limit of the sequence (A′
i ∩ [0, rN )/rN )∞
N =1 as in Proposition 3.15. Since dimH Xi =
dimH A′
i = dimH Ai and ∑∞
i=1 dimH Ai/| log dimH Ai| diverges, we have that ∑∞
i=1 dimH Xi/
| log dimH Xi| diverges. It follows by Theorem 1.4 that

lim
n→∞ dimH (X1 + · · · + Xn) = 1. (4.33)

According to Remark 4.8, we can and will interpret the sum X1 + · · · + Xn to be in R.
We claim now that for all n ∈ N, the discrete Hausdorﬀ dimension of the set A′
1 + · · · + A′
n

45

exists and
 dimH (A
′
1 + · · · + A
′
n) = dimH (
X1 + · · · + Xn)
. (4.34)

Combined with (4.33), this suﬃces to conclude the proof of Theorem D since A′
i ⊆ Ai implies
that dimH (
A′
1 + · · · + A′
n) ⩽ dimH (A1 + · · · + An)
.
To show (4.34), let n ∈ N, and deﬁne k = ⌊log n/ log r⌋ + 1. Deﬁne Bn = A′
1 + · · · + A′
n
and Yn = X1 + · · · + Xn, where the sum deﬁning Yn is understood to be in R. Note that for
all N ⩾ k,
 n∑

i=1
 A′
i ∩ [0, rN −k)
rN ⊆ Bn ∩ [0, rN )
rN ⊆
 n∑

i=1
 A′
i ∩ [0, rN )
rN , (4.35)

where the sums indicate sumsets. The goal now is to compare the discrete Hausdorﬀ contents
of each of these sets at scale r−N .
By the deﬁnition of the set Xi, it follows from Lemma 3.16 that

dH
 (A′
i ∩ [0, rN )
rN , Xi
) ≪ r−N , (4.36)

which implies by Lemma 2.5 that for all γ ∈ [0, 1],

Hγ
⩾r−N
 ( n∑

i=1
 A′
i ∩ [0, rN )
rN
 )
 ≍n Hγ
⩾r−N (Yn). (4.37)

It also follows from (4.36) that

dH
 ( A′
i ∩ [0, rN −k)
rN , Xi
rk
 ) ≪n r−N ,

which implies by Lemma 2.5 that

Hγ
⩾r−N
 ( n∑

i=1
 A′
i ∩ [0, rN −k)
rN
 )
 ≍n Hγ
⩾r−N
 (Yn
rk
 ) . (4.38)

Combining (4.35) with (4.37) and (4.38), we see that

Hγ
⩾r−N
 ( Yn
rk
 ) ≪n Hγ
⩾r−N
 ( Bn ∩ [0, rN )
rN
 ) = Hγ
⩾1 (Bn ∩ [0, rN )
)

rN γ ≪n Hγ
⩾r−N (Yn).

Letting N tend to inﬁnity and noting that n, and hence k, are ﬁxed, these inequalities combine
with Remark 2.3, Lemma 3.2 (V), (4.33), and the fact that dimH(Yn/rk) = dimH Yn to prove
the equality in (4.34).
 5. Open directions

We collect in this section a number of interesting open questions concerning multiplicatively
invariant subsets of the non-negative integers. Though these questions and conjectures are
stated for arbitrary ×r-invariant subsets of N0, many are already open and interesting for
the special case of base-r restricted digit Cantor sets.

46

5.1. Positive density for sumsets of full dimension

In [Hoc, Problem 4.10], Hochman asks whether the sumset X + Y of a ×r- and a ×s-
invariant subset of [0, 1] satisfying dimH X + dimH Y > 1 has positive Lebesgue measure. We
remark that a projection theorem of Marstrand [Mar, Theorem I] implies that λX + ηY has
positive Lebesgue measure for a.e. (λ, η) ∈ R2, suggesting a possible aﬃrmative answer. In
[Gla, Theorem 1.4], a version of Marstrand’s projection theorem for subsets of the integers
was obtained, with Lebesgue measure replaced by the notion of upper natural density.5 It
therefore makes sense to consider the following integer analogue of Hochman’s question.

Question 5.1. Let r, s ∈ N be multiplicatively independent, and let A, B ⊆ N0 be ×r- and
×s-invariant, respectively. If dimM A+dimM B > 1, then does the sumset A+B have positive
upper natural density?
 5.2. Small intersections

While Question 5.1 considers the sum A + B when sum of the dimensions is larger than 1, it
is also natural to ask about the intersection A ∩ B when the sum of the dimensions is below
1. A special case of a conjecture posed by Furstenberg in [Fur2] asserts that if r, s ∈ N are
multiplicatively independent and X, Y ⊆ [0, 1] are ×r- and ×s-invariant, respectively, then

dim X + dim Y < 1 =⇒ X ∩ Y ⊆ Q.

Furstenberg showed that an aﬃrmative answer to this question implies that any large enough
power of 2 contains every digit (in base 10), which is a variant of the conjecture of Erd˝os
[Erd] mentioned in the introduction.
The following question is inspired by Furstenberg’s conjecture.

Question 5.2. Let r, s ∈ N be multiplicatively independent, and let A, B ⊆ N0 be ×r- and
×s-invariant, respectively. Is it true that

dim A + dim B < 1 =⇒ A ∩ B is ﬁnite?

A special case of this question is formulated in [Yu2, Conjecture 6.2]. If the answer to
Question 5.2 is positive, then Erd˝os’ conjecture holds (this can be seen by taking r = 2,
s = 3, A to be the powers of 2, and B to be a restricted digit Cantor set). A weaker version
of this statement was established by Lagarias [Lag].
One can formulate a natural quantitative strengthening of Question 5.2 as follows. Given
n, r, k ∈ N, let dr,k(n) be the number of subwords of (n)r of length at most k. Then the
answer to Question 5.2 is positive if one can show that

lim sup
k→∞ lim inf
n→∞
 ( log dr,k(n)
k log r + log ds,k(n)
k log s
 ) = 1. (5.1)

In fact, it suﬃces to prove that the expression in (5.1) is greater than or equal to 1. Indeed, by
considering n to be a power of r, for any k ∈ N, lim inf n→∞ log dr,k(n)/k log r = log 2k/k log r,
whereby the expression in (5.1) is at most 1. We believe the limit in (5.1) as k tends to inﬁnity
exists, but this would not be necessary to imply a positive answer to Question 5.2.

5Given a set E ⊆ Z, its upper natural density is deﬁned by ¯d(E) := lim supN→∞ |E ∩{−N, . . . , N }|/(2N +1).

47

5.3. Diﬀerence sets

For closed subsets X, Y ⊆ [0, 1], working with the diﬀerence set X − Y is no harder than
working with the sumset X + Y . In particular, proving that

dimM (X − Y ) = min ( dimM X + dimM Y, 1
)

in Eq. (1.9) requires no additional work. The story changes in the setting of the non-negative
integers, where diﬀerence sets are much more cumbersome to handle, ultimately because the
ﬁbers of the map (a, b) ↦→ a − b are not compact. This observation explains why our main
results in the integer setting only deal with sumsets λA + ηB with λ and η both positive,
and it naturally leads us to the following question.

Question 5.3. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant, respectively. Is it true that

dimM(A − B) = min ( dimM A + dimM B, 1
)?

The methods used in Section 4.3 allow us to establish the lower bound dimM (A − B) ⩾
min(dimM A + dimM B, 1). However, the upper bound dimM (A − B) ⩽ min(dimM A +
dimM B, 1), which is straightforward for sums, remains open for diﬀerences.
There are many natural variants and extensions of Question 5.3: one can replace A − B
with a more general expression ⌊λA + ηB⌋ for any non-zero real numbers λ, η, or one can
replace dimM with dimH. One can ask about combinations of the form ⌊λA′ + ηB′⌋ for
arbitrary subsets A′ and B′ of A and B, or one can look only at the positive portion (A−B)∩N
of the diﬀerence set. Our methods provide an outline for obtaining lower bounds, but upper
bounds seem to require a new strategy.

5.4. Analogous results for other notions of discrete dimension

The upper Banach dimension (or upper counting dimension, cf. [LM1] and [Gla]) of a set
A ⊆ N0 is
 dim
∗ A := lim sup
N −M →∞
 log ∣
∣A ∩ [M, N ]
∣
∣

log(N − M ) .

In general, we only have the inequality dim
∗ A ⩾ dimM A, but if A ⊆ N0 is ×r-invariant, then
it can be shown that dimM A = dimH A = dim
∗ A.

Question 5.4. Let r and s be multiplicatively independent positive integers, and let A, B ⊆
N0 be ×r- and ×s-invariant, respectively. Is it true that

dim
∗(A + B) = min ( dim∗ A + dim
∗ B, 1
), and / or

dim
∗(A ∩ B) ⩽ max ( dim
∗ A + dim∗ B − 1, 0
).

Note that the lower bound dim∗(A + B) ⩾ min ( dim∗ A + dim
∗ B, 1
) follows from The-
orem C using the fact that dim∗ ⩾ dimM .
There are several other ways to deﬁne natural notions of dimensions for subsets of N0.
Barlow and Taylor [BT2] deﬁne, for example, a discrete notion of packing dimension. The
main results in this article suggest possible analogues for their discrete packing dimension.

48

5.5. Polynomial functions of multiplicatively invariant sets

The dimension of the sumset of aﬃne images of multiplicatively invariant sets A and B is
described in Theorem C. It is natural to ask about the extent to which the results in that
theorem might hold for the sumset of images of A and B under other functions.
In this subsection, for n ∈ N, denote by A(n) the set of nth-powers of elements of A:
A(n) := {an | a ∈ A}. The following question is a (special case of a) natural polynomial
extension of Theorem C.

Question 5.5. Let n, m ∈ N, let r, s ∈ N be multiplicatively independent, and let A, B ⊆ N0
be ×r- and ×s-invariant, respectively. Is it true that

dimM (A
(n) + B(m)) = min ( 1
n dimM A + 1
m dimM B , 1
)? (5.2)

When A = B = N0, an aﬃrmative answer to Question 5.5 follows from basic facts in
number theory. It is easy to see that for any A ⊆ N0 for which the Minkowski dimension
exists, the set A(n) has dimension dimM A(n) = dimM A/n (however it is not true in general
that A(n) is ×r-invariant when A is). Thus, for arbitrary sets A and B that satisfy a natural
dimension condition (see footnote 3), it follows from the discrete version of Marstrand’s
projection theorem in (1.10) that dimM (
⌊λA(n) + ηB(m)⌋
) is equal to the right hand side of
(5.2) for Lebesgue almost every λ, η > 0.
We cannot rule out the possibility that (5.2) holds when n, m ⩾ 2 for arbitrary sets A
and B for which the Minkowski dimensions exist. When A = B and n = m = 2, equality in
(5.2) is an inﬁnitary version of a conjecture attributed to Ruzsa; see [CG, Conjecture 5].

5.6. Multiplicatively invariant sets in relation to other arithmetic sets in
the integers

In this paper, we are concerned with transversality between ×r- and ×s-invariant sets when-
ever r and s are multiplicatively independent. In principle, it makes sense to inquire about
transversality (or independence) between any two sets which are structured in diﬀerent ways.
To keep the discussion short, we restrict to inﬁnite arithmetic progressions (or congruence
classes), the set of perfect squares, and the set of primes.

Question 5.6. Let A ⊆ N0 be a ×r-invariant set, and let P be an inﬁnite arithmetic
progression. Is it true that dimM(A ∩ P ) is either 0 or dimM(A)?

The answer is yes for restricted digit Cantor sets. In fact, it is proved in [EMS] that such
sets satisfy “good equidistribution properties” in residue classes.
More generally, one could ask about the sum or the intersection of a ×r-invariant set and
the image of an arbitrary polynomial with integer coeﬃcients, for instance the set of perfect
squares, S = {n2 | n ∈ N0}. Note that dimM S = 1/2.

Question 5.7. Let A ⊆ N0 be a ×r-invariant set. Is is true that

dimM (A + S) = min ( dimM A + 1/2, 1
)

and/or
 dimM (
A ∩ S) ⩽ max ( dimM A − 1/2, 0
)?

49

Note that the ﬁrst expression in this question is a special case of the equality in Ques-
tion 5.5. In a similar vein, one can ask about intersections with the set of prime numbers, P.
Note that dimM P = 1.

Question 5.8. Let A ⊆ N0 be a ×r-invariant set. Is is true that dimM(A ∩ P) is either 0 or
dimM(A)?

Maynard showed in [May] that the answer to Question 5.8 is positive when A is a restricted
digit Cantor set where the number of restricted digits is small enough with respect to the
base. In fact, he obtains a Prime Number Theorem in such sets, which is stronger than
simply dimM(A ∩ P) = dimM A. Question 5.8 is open for general restricted digit Cantor sets,
and may be very diﬃcult in general. The methods in this paper do not appear to shed new
light on this line of inquiry.

5.7. Transversality of multiplicatively invariant sets in the rs-adics

The rs-adics is a non-Archimedean regime in which it is easy to ask questions analogous to
those asked in this work. Furstenberg proved in [Fur2, Theorem 3] an analogue of Theorem 1.1
in the rs-adics.
Following Furstenberg, note that the maps Rr and Rs, with domains extended to Z,
are uniformly continuous with respect to the rs-adic metric on Z, and therefore extend to
continuous transformations of the set of rs-adic integers, Zrs. As a compact metric space,
there is a natural Hausdorﬀ dimension to measure the size of subsets of Zrs. Let us call a set
X ⊆ Zrs ×r-invariant if it is closed and RrX ⊆ X.

Question 5.9. Let r and s be multiplicatively independent positive integers, and let X, Y ⊆
Zrs be ×r- and ×s-invariant sets, respectively. Is it true that

dimH (X + Y ) = min ( dimH X + dimH Y, dimH Zrs), and / or

dimH (
X ∩ Y ) ⩽ max ( dimH X + dimH Y − dimH Zrs, 0
)?

The upper bound on dimH (X ∩ Y ) in the previous question was conjectured by Fursten-
berg in [Fur2, Conjecture 3]. A positive answer to these questions would bring transversality
results in the rs-adics in line with those in the real and integer settings.

References

[Aus] Tim Austin. A new dynamical proof of the Shmerkin-Wu theorem. J. Mod. Dyn.,
18:1–11, 2022.

[BCS] William D. Banks, Alessandro Conﬂitti, and Igor E. Shparlinski. Character sums over
integers with restricted g-ary digits. Illinois J. Math., 46(3):819–836, 2002.

[BP] Christopher J. Bishop and Yuval Peres. Fractals in probability and analysis, volume
162 of Cambridge Studies in Advanced Mathematics. Cambridge University Press,
Cambridge, 2017.

[BS] William D. Banks and Igor E. Shparlinski. Arithmetic properties of numbers with
restricted digits. Acta Arith., 112(4):313–332, 2004.

50

[BT1] Martin T. Barlow and Samuel J. Taylor. Fractional dimension of sets in discrete spaces.
J. Phys. A, 22(13):2621–2628, 1989. With a reply by Jan Naudts.

[BT2] Martin T. Barlow and Samuel J. Taylor. Deﬁning fractal subsets of Zd. Proc. London
Math. Soc. (3), 64(1):125–152, 1992.

[BY] Stuart A. Burrell and Han Yu. Digit expansions of numbers in diﬀerent bases. arXiv
e-prints, arXiv:1905.00832, May 2019.

[Cas] John William Scott Cassels. On a problem of Steinhaus about normal numbers. Colloq.
Math., 7:95–101, 1959.

[CG] Javier Cilleruelo and Andrew Granville. Lattice points on circles, squares in arithmetic
progressions and sumsets of squares. In Additive combinatorics, volume 43 of CRM
Proc. Lecture Notes, 241–262. Amer. Math. Soc., Providence, RI, 2007.

[DW] Taylor Dupuy and David E. Weirich. Bits of 3n in binary, Wieferich primes and a
conjecture of Erd˝os. J. Number Theory, 158:268–280, 2016.

[EMS] Paul Erd˝os, Christian Mauduit, and Andr´as S´ark¨ozy. On arithmetic properties of
integers with missing digits. I. Distribution in residue classes. J. Number Theory,
70(2):99–120, 1998.

[Erd] Paul Erd˝os. Some unconventional problems in number theory. Math. Mag., 52(2):67–
70, 1979.

[FHY] Jonathan M. Fraser, Douglas C. Howroyd, and Han Yu. Dimension growth for iterated
sumsets. Math. Z., 293(3-4):1015–1042, 2019.

[Fur1] Harry Furstenberg. Disjointness in ergodic theory, minimal sets, and a problem in
Diophantine approximation. Math. Systems Theory, 1:1–49, 1967.

[Fur2] Harry Furstenberg. Intersections of Cantor sets and transversality of semigroups.
41–59, 1970.

[Fur3] Hillel Furstenberg. Ergodic fractal measures and dimension conservation. Ergodic
Theory and Dynamical Systems, 28(2):405–422, 2008.

[Gla] Daniel Glasscock. Marstrand-type theorems for the counting and mass dimensions in
Zd. Combin. Probab. Comput., 25(5):700–743, 2016.

[GMR] Daniel Glasscock, Joel Moreira, and Florian K. Richter. A combinatorial proof of a
sumset conjecture of Furstenberg. arXiv e-prints, arXiv:2107.10605, 2021.

[Hoc] Michael Hochman. Dimension theory of self-similar sets and measures. In Proceedings of
the International Congress of Mathematicians—Rio de Janeiro 2018. Vol. III. Invited
lectures, 1949–1972. World Sci. Publ., Hackensack, NJ, 2018.

[Hos] Bernard Host. Nombres normaux, entropie, translations. Israel J. Math., 91(1-3):419–
428, 1995.

[HS1] Michael Hochman and Pablo Shmerkin. Local entropy averages and projections of
fractal measures. Ann. of Math. (2), 175(3):1001–1059, 2012.

51

[HS2] Michael Hochman and Pablo Shmerkin. Equidistribution from fractal measures. In-
vent. Math., 202(1):427–479, 2015.

[Inc] OEIS Foundation Inc. The On-Line Encyclopedia of Integer Sequences.
http://oeis.org/A146025, 2020.

[IRUT] Alexander Iosevich, Michael Rudnev, and Ignacio Uriarte-Tuero. Theory of dimen-
sion for large discrete sets and applications. Math. Model. Nat. Phenom., 9(5):148–169,
2014.

[JR] Thomas Jordan and Ariel Rapaport. Dimension of ergodic measures projected onto
self-similar sets with overlaps. Proc. Lond. Math. Soc. (3), 122(2):191–206, 2021.

[KMS] Sergei Konyagin, Christian Mauduit, and Andr´as S´ark¨ozy. On the number of prime
factors of integers characterized by digit properties. Period. Math. Hungar., 40(1):37–
52, 2000.

[Kon] Sergei Konyagin. Arithmetic properties of integers with missing digits: distribution in
residue classes. Period. Math. Hungar., 42(1-2):145–162, 2001.

[Lag] Jeﬀrey C. Lagarias. Ternary expansions of powers of 2. J. Lond. Math. Soc. (2),
79(3):562–588, 2009.

[Lin] Elon Lindenstrauss. p-adic foliation and equidistribution. Israel J. Math., 122:29–42,
2001.

[LM1] Yuri Lima and Carlos Gustavo Moreira. A Marstrand theorem for subsets of integers.
Combinatorics, Probability and Computing, 23:116–134, 1 2014.

[LM2] Douglas Lind and Brian Marcus. An introduction to symbolic dynamics and coding.
Cambridge University Press, Cambridge, 1995.

[LMP] Elon Lindenstrauss, David Meiri, and Yuval Peres. Entropy of convolutions on the
circle. Ann. of Math. (2), 149(3):871–904, 1999.

[Mar] John M. Marstrand. Some fundamental geometrical properties of plane sets of frac-
tional dimensions. Proc. London Math. Soc. (3), 4:257–302, 1954.

[Mat] Pertti Mattila. Geometry of sets and measures in Euclidean spaces, volume 44 of
Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge,
1995. Fractals and rectiﬁability.

[May] James Maynard. Primes with restricted digits. Invent. Math., 217(1):127–218, 2019.

[MF] Michel Mend`es France. Sur les d´ecimales des nombres alg´ebriques r´eels. In Seminar
on Number Theory, 1979–1980 (French), Exp. No. 28, 7. Univ. Bordeaux I, Talence,
1980.

[Nau1] Jan Naudts. Dimension of discrete fractal spaces. J. Phys. A, 21(2):447–452, 1988.

[Nau2] Jan Naudts. Reply to a paper by Martin T. Barlow and Samuel J. Taylor. J. Phys.
A, 22(13):2627–2628, 1989.
 52

[Sch] Wolfgang M. Schmidt. On normal numbers. Paciﬁc J. Math., 10:661–672, 1960.

[Shm] Pablo Shmerkin. On Furstenberg’s intersection conjecture, self-similar measures, and
the Lq norms of convolutions. Ann. of Math. (2), 189(2):319–391, 2019.

[TV] Terence Tao and Van Vu. Additive combinatorics, volume 105 of Cambridge Studies in
Advanced Mathematics. Cambridge University Press, Cambridge, 2006.

[Wal] Peter Walters. An introduction to ergodic theory, volume 79 of Graduate Texts in
Mathematics. Springer-Verlag, New York-Berlin, 1982.

[Wu] Meng Wu. A proof of Furstenberg’s conjecture on the intersections of ×p- and ×q-
invariant sets. Ann. of Math. (2), 189(3):707–751, 2019.

[Yu1] Han Yu. A higher dimensional version of Furstenberg’s intersection problem and ad-
ditive properties of numbers with restricted digits. arXiv e-prints, arXiv:2004.05926,
April 2020.

[Yu2] Han Yu. Additive properties of numbers with restricted digits. arXiv e-prints,
arXiv:2004.05926, April 2020.

[Yu3] Han Yu. Fractal projections with an application in number theory. arXiv e-prints,
arXiv:2004.05924, April 2020.

[Yu4] Han Yu. An improvement on Furstenberg’s intersection problem. Trans. Amer. Math.
Soc., 374(9):6583–6610, 2021.

Daniel Glasscock
University of Massachusetts Lowell
daniel glasscock@uml.edu

Joel Moreira
University of Warwick
joel.moreira@warwick.ac.uk

Florian K. Richter
´Ecole Polytechnique F´ed´erale de Lausanne (EPFL)
f.richter@epfl.ch
 53
