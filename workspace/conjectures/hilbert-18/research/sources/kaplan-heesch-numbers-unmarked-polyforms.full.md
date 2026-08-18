<!-- source: https://arxiv.org/pdf/2105.09438 | converted from PDF -->

Heesch Numbers of Unmarked Polyforms

Craig S. Kaplan
School of Computer Science, University of Waterloo, Ontario, Canada; csk@uwaterloo.ca

Abstract

A shape’s Heesch number is the number of layers of copies of the shape that can be placed around it without gaps or
overlaps. Experimentation and exhaustive searching have turned up examples of shapes with ﬁnite Heesch numbers
up to six, but nothing higher. The computational problem of classifying simple families of shapes by Heesch number
can provide more experimental data to fuel our understanding of this topic. I present a technique for computing
Heesch numbers of non-tiling polyforms using a SAT solver, and the results of exhaustive computation of Heesch
numbers up to 19-ominoes, 17-hexes, and 24-iamonds.

1 Introduction

Tiling theory is the branch of mathematics concerned with the properties of shapes that can cover the plane
with no gaps or overlaps. It is a topic rich with deep results and open problems. Of course, tiling theory must
occasionally venture into the study of shapes that do not tile the plane, so that we might understand those that
do more completely.
If a shape tiles the plane, then it must be possible to surround the shape by congruent copies of itself,
leaving no part of its boundary exposed. A circle clearly cannot tile the plane, because neighbouring circles
can cover at most a ﬁnite number of points on its boundary. A regular pentagon also cannot be surrounded
by copies of itself: its vertices will always remain exposed.
However, the converse is not true: there exist shapes that can be fully surrounded by copies of themselves,
but for which no such surround can be extended to a tiling. For example, there are 108 heptominoes (shapes
formed by gluing together seven squares), of which four, shown in Figure 1, are known not to tile the plane.
One of them contains an internal hole and can be discarded immediately. As it happens, the other three can
all be surrounded. In the middle two cases, the shape and its surrounding copies are simply connected. On
the right, the surrounding tiles leave behind an internal hole, and no alternative surround can eliminate that
hole.There is no a priori reason why a given non-tiling shape might not be surroundable by two, three, or
more layers of copies of itself. The illustrations in Figure 1 provide lower bounds for the numbers of layers

Figure 1: The four non-tiling heptominoes. The shape on the left has a hole and cannot be
surrounded. The other three can be fully surrounded by copies, but in the rightmost shape the
copies will necessarily enclose a hole.
 1arXiv:2105.09438v1  [cs.CG]  20 May 2021
Figure 2: A 23-omino that can be surrounded by two layers of copies of itself, but not more.

for these shapes; that they also represent upper bounds must be proven by enumerating all possible surrounds,
and showing that none of them may be further surrounded. Other shapes might permit more layers. For
example, the 23-omino shown in Figure 2, due to Fontaine [3], can be surrounded by two layers but not more.
How far can this process be extended?
A shape’s Heesch number is the number of times it can be surrounded with complete layers of congruent
copies of itself (I will oﬀer a precise deﬁnition in the next section). If the shape tiles the plane, its Heesch
number is deﬁned to be inﬁnity. Heesch’s problem asks which positive integers are Heesch numbers; that is,
for which 𝑛 > 0 does there exist a shape with Heesch number 𝑛?
Very little is known about the solution to Heesch’s problem. Writing in 1987, Grünbaum and Shephard
were not aware of any examples with ﬁnite Heesch number greater than 1 [5, Section 3.8]. After that, a few
isolated examples were found with Heesch numbers up to 4 [7]. Mann and Thomas performed a systematic
computer search of marked polyforms (polyominoes, polyhexes, and polyiamonds, with edges decorated with
geometric matching conditions), yielding new examples and pushing the record to 5 [8]. In 2021 Bašić ﬁnally
broke this record, demonstrating a ﬁgure with Heesch number 6 [1].
The study of Heesch numbers can shed light on some of the deepest problems in tiling theory. In
particular, the tiling problem asks, for a given set of shapes, whether they admit at least one tiling of the
plane. The tiling problem is known to be undecidable for general sets of shapes [2], but its status is open for
a set consisting of a single shape 𝑆. If there were an upper bound 𝑁 on ﬁnite Heesch numbers, then the tiling
problem would be decidable, at least when there are only ﬁnitely many ways that two copies of 𝑆 may be
adjacent [4]. The algorithm would involve trying the ﬁnitely many ways of surrounding 𝑆 with 𝑁 + 1 layers
of copies of itself. If you succeed, then you have exceeded the maximum ﬁnite Heesch number and 𝑆 must
tile the plane. If you fail, then 𝑆 evidently does not tile. To that end, more experimental data revealing which
Heesch numbers are possible, even for limited classes of shapes, could be useful in understanding whether
such an upper bound might exist.
In this article I report on a complete enumeration of Heesch numbers of unmarked polyforms, up to

2

19-ominoes, 17-hexes, and 24-iamonds. This enumeration comprises approximately 4.16 billion non-tilers,
extracted from enumerations of all free polyforms of those sizes. Respecting a slight diﬀerence of opinion
among researchers, I compute two variations of Heesch numbers: one where tiles may form holes in the
outermost layer, and one where a shape and all its surrounding layers must be simply connected. This
enumeration does not shatter the existing records for Heesch numbers, but it does provide a store of new
examples of shapes with non-trivial Heesch numbers. Some, like a 9-omino with Heesch number 2 (Figure 7)
and a 7-hex with Heesch number 3 (Figure 8), are interesting because of the complex behaviour exhibited by
relatively simple shapes. The enumeration also uncovered seven new examples with Heesch number 4.
Apart from the tabulation and speciﬁc examples, the other main contribution of this work lies in the use
of a SAT solver to compute Heesch numbers. Because polyominoes, polyhexes, and polyiamonds are subsets
of ambient regular tilings of the plane, it is possible to reduce the geometric problem of surroundability to the
logical problem of satisﬁability of Boolean formulas. A SAT solver can optimize its search of the exponential
space of possible solutions, avoiding the risk of “backtracking hell”. This formulation leads to a very reliable
algorithm, whose performance degrades only on the rare shapes that actually have high Heesch numbers.

2 Mathematical background

Although Heesch’s problem grew out of tiling theory, most of the language, techniques, and results of tiling
theory are not needed within the scope of this article and will be omitted. Readers interested in the topic
should consult Grünbaum and Shephard’s book [5], which remains the standard reference. In this section I
will formalize the deﬁnition of a shape’s Heesch number and review marked and unmarked polyforms.

2.1 Heesch numbers

Let 𝐶 and 𝑆 be simple shapes in the plane, i.e., topological discs. We say that 𝐶 can be surrounded by 𝑆 if
there exists a set of shapes {𝑆1, . . . , 𝑆𝑛} with the following properties:

1. Each 𝑆𝑖 is congruent to 𝑆 via a rigid motion in the plane;

2. The shapes in the set {𝐶, 𝑆1, . . . , 𝑆𝑛} have pairwise disjoint interiors;

3. The boundary of each 𝑆𝑖 shares at least one point with the boundary of 𝐶.

4. The boundary of 𝐶 lies entirely within the interior of the union of 𝐶 and all the 𝑆𝑖.

The second condition forces the shapes not to overlap, except on their boundaries. The third condition
forces every 𝑆𝑖 to be useful in covering the boundary of 𝐶. The fourth condition ensures that 𝐶 is completely
surrounded.
If, furthermore, the union of 𝐶 and the 𝑆𝑖 is simply connected, we say that 𝐶 can be surrounded by 𝑆
without holes. In tiling theory, a ﬁnite union of non-overlapping shapes whose union is a topological disc is
also known as a patch, a term I will use here. On the other hand, I will use the more general term packing
when shapes are known to be non-overlapping but when their union may or may not contain holes.
We formalize the notion of layers by deﬁning the coronas of 𝑆. We deﬁne the 0-corona of 𝑆 to be
the singleton set {𝑆}. Setting 𝐶 = 𝑆 above, if 𝑆 can be surrounded by itself then the tiles that make up
that surround are one possible 1-corona of 𝑆. In general, if we have a nested sequence of 𝑘-coronas for
𝑘 = 0, . . . , 𝑛 − 1, all without holes, and the patch created from the union of all of these coronas can itself be
surrounded by 𝑆, then the copies of 𝑆 making up the surround constitute an 𝑛-corona.
The Heesch number of a shape 𝑆 is the largest 𝑛 for which 𝑆 has an 𝑛-corona. If 𝑆 tiles the plane, then
by deﬁnition it is possible to build an 𝑛-corona for every positive integer 𝑛, and we deﬁne its Heesch number
to be inﬁnity. If we wish to be concise, we will simply say that 𝑆 has 𝐻 = 𝑛.

3

The deﬁnitions above require that for a shape to have Heesch number 𝑛, each 𝑘-corona for 𝑘 = 1, . . . , 𝑛−1
surround its predecessor without holes. But it leaves the status of the outermost corona ambiguous. Most
researchers require that a shape’s 𝑛-corona be hole-free in order to regard the shape as having 𝐻 = 𝑛, but some
permit the 𝑛-corona to have holes. In this article I will remain neutral on this point, and report separate results
with and without holes in the outer corona. To that end, I will say that a shape has 𝐻𝑐 = 𝑛1 and 𝐻ℎ = 𝑛2
to distinguish its Heesch numbers when holes are or are not permitted in the outer corona, respectively. In
any case, we must always have either 𝐻𝑐 = 𝐻ℎ or 𝐻𝑐 = 𝐻ℎ − 1, so this diﬀerence of opinion cannot aﬀect
results too dramatically. (Note that permitting a hole in the outermost corona raises the alarming possibility
that the hole could be ﬁlled with additional tiles, forcing us to consider the validity of a subsequent corona
made from multiple disjoint pieces!)

2.2 Polyforms

A polyform is a shape constructed by gluing together multiple copies of some simple polygonal building
block along their edges. Usually we require that the assembly be edge-to-edge: no vertex of one copy of
the building block may lie in the interior of the edge of another copy. The most famous polyforms are the
polyominoes, constructed from glued-together squares. We speak more speciﬁcally of 𝑛-ominoes as unions
of 𝑛 squares, so that, for example, the 4-ominoes (or tetrominoes) are the familiar Tetris pieces. In this
article I will also consider polyhexes and polyiamonds, formed from unions of regular hexagons and unions
of equilateral triangles, respectively, and refer more precisely to 𝑛-hexes and 𝑛-iamonds as needed.
Simple polyforms are an attractive domain in which to compute Heesch numbers. They can be explored
exhaustively by enumerating the ﬁnite number of distinct 𝑛-forms for each successive 𝑛. The edge-to-
edge constraint often reduces a continuous geometric problem to a combinatorial one, and in the technique
presented here, even the combinatorial structure will be distilled into a problem in Boolean satisﬁability.
Still, polyforms can expose many of the core behaviours of shapes more generally. Conceivably one could
establish an upper bound on Heesch numbers of, say, polyominoes, while leaving Heesch’s problem open
more generally; but in the meantime, these calculations can yield a trove of interesting data.
In a marked polyform, the edges of a polyform are assigned symbolic labels, and a binary relation over
labels determines which pairs of edges may be placed side-by-side in neighbouring copies of the polyform.
A simple system of labels involves marking some edges with a “bump”, some with a corresponding “nick”,
and leaving all others ﬂat. Flat edges can only meet other ﬂat edges, and bumps must be adjacent to nicks.
Mann and Thomas computed Heesch numbers of simple polyforms with markings of this form [8]. They
began with a small family of low-order polyominoes, polyhexes, and polyiamonds, enumerated all possible
assignments of bumps and nicks to their edges, and computed the Heesch numbers of the resulting shapes
using a recursive search with backtracking. Their search yielded a number of examples with Heesch numbers
up to 5. However, the majority of their eﬀorts produced inconclusive results: they either failed to produce a
ﬁnite Heesch number in the time allotted to each shape, or terminated the computation at ﬁve coronas. The
main reason for this deﬁciency is that they did not have an eﬀective procedure for ﬁrst computing whether
a marked polyform tiles the plane. Most of their inconclusive results are likely to be shapes with Heesch
numbers that are inﬁnite, rather than high-but-ﬁnite.
To my knowledge, no previous work has sought to compute Heesch numbers of unmarked polyforms.
Myers tabulated information about polyominoes, polyhexes, and polyiamonds that tile the plane [9]. He
determined whether polyforms tiled in progressively more intricate ways, measuring the isohedral number of
tilers (roughly speaking, the number of copies of the tile that must be glued together to produce a patch that
tiles in a relatively simple way). Each of his tables includes a single column labelled “non-tilers”. This article
sorts that columns into multiple bins organized by Heesch number, eﬀectively tabulating the progressively
more intricate ways in which polyforms do not tile. Myers’s software is remarkably eﬃcient, requiring on
average a fraction of a millisecond on modern hardware to classify a given polyform. I use his software to

4

produce initial lists of non-tilers for Heesch number computation, thereby avoiding the needless construction
of coronas for shapes that have inﬁnitely many of them.

3 Computing Heesch numbers with a SAT solver

In this section I show how to reduce the problem of computing a polyform’s Heesch number to evaluating
the satisﬁability of a sequence of Boolean formulas. At a high level, each formula encodes whether a given
polyform has Heesch number at least 𝑛 (with slight variations depending on whether to allow holes). I check
the satisﬁability of these formulas for increasing values of 𝑛 until I ﬁnd one that is unsatisﬁable, indicating
the non-existence of a corona of a given level.
Every formula will be expressed in conjunctive normal form (CNF) as a conjunction of clauses, each
of which is a disjunction of variables or their negations. That is, each clause ORs together any number of
Boolean variables or their negations, and the entire formula is an AND of clauses. I use the standard operators
∨ for OR, ∧ for AND, and ¬ for NOT. I will also allow clauses to be written using an implication operator
with a single variable on the left, converting 𝑃 → 𝑄 to ¬𝑃 ∨ 𝑄 as needed.
To simplify the exposition, I will limit the development here exclusively to polyominoes. In the next
section I will describe the modiﬁcations that are necessary to support polyhexes and polyiamonds.

3.1 Developing the base formula

Because our shapes will always meet edge-to-edge, we can assume that they will occupy cells in a conceptually
inﬁnite grid of squares, indexed by (𝑥, 𝑦) pairs of integer coordinates. For a given cell 𝑝 = (𝑥, 𝑦), we deﬁne
𝑁8( 𝑝), the 8-neighbourhood of 𝑝, to be the set of cells horizontally, vertically, or diagonally adjacent to
𝑝. Now let 𝑆 be an 𝑚-omino whose Heesch number we wish to compute. We describe 𝑆 as a set of cells
{(𝑥1, 𝑦1), . . . , (𝑥𝑚, 𝑦𝑚)}, translated so that (0, 0) ∈ 𝑆. We will also make use of the halo of 𝑆, written
Halo(𝑆), the set of grid cells 𝑝 for which 𝑝 ∉ 𝑆 but 𝑁8( 𝑝) ∩ 𝑆 ≠ œ. That is, Halo(𝑆) consists of a ring of
cells around the boundary of 𝑆.
Ignoring symmetry, a polyomino has eight distinct rotated and reﬂected orientations, which can be
represented by 2 × 2 matrices with entries in {−1, 0, 1}. We must also track translations of polyominoes by
integer vectors (Δ𝑥, Δ𝑦). Any possible transformed copy of 𝑆 can therefore be identiﬁed with six (usually
small) integers that deﬁne an aﬃne transformation 𝑇. Two transformed shapes 𝑇1(𝑆) and 𝑇2(𝑆) are adjacent if
they occupy neighbouring cells but do not overlap; that is, 𝑇1(𝑆) ∩ 𝑇2(𝑆) = œ, but 𝑇1(𝑆) ∩ Halo(𝑇2(𝑆)) ≠ œ.
For a ﬁxed 𝑆, I will also refer to 𝑇1 and 𝑇2 as adjacent in this context.
We are particularly interested in ﬁnite sets of transformations T𝑘, containing every possible 𝑇 for which
𝑇 (𝑆) might be part of a 𝑘-corona of 𝑆. We can deﬁne these sets recursively by setting T0 to be a singleton
set containing the identity transformation, and each subsequent T𝑘 to be every transformation 𝑇 adjacent to
some 𝑇 ′ ∈ T𝑘−1. Every 𝑘-corona of 𝑆, if one exists, must consist of copies of 𝑆 transformed by a subset of T𝑘.
We are now ready to deﬁne two classes of Boolean variables: cell variables and shape variables. For
every 𝑝 = (𝑥, 𝑦) in the grid, the cell variable 𝑐 𝑝 is true if and only if 𝑝 is covered by a transformed copy of
𝑆. For every aﬃne transformation 𝑇 and every integer 𝑘 ≥ 0, the shape variable 𝑠𝑇 ,𝑘 is true if and only if
the transformed shape 𝑇 (𝑆) is used as part of the 𝑘-corona in a packing of copies of 𝑆.
Given an integer 𝑛 > 0, we can at last write down a Boolean formula 𝐹𝑛 whose satisﬁability implies that
𝑆 has an 𝑛-corona. 𝐹𝑛 is the conjunction of a large number of clauses, belonging to seven distinct classes.
The clauses are listed in full in Figure 3, along with intuitive explanations of their meanings. Informally, we
see that the 0-corona is activated by ﬁat, which in turn demands that its halo cells all be occupied by adjacent
shapes. Additional clauses force those adjacent shapes to belong to the 1-corona, and to be pairwise disjoint.
A similar process plays out in each subsequent corona before the last one: shapes in the corona tag their
halo cells, thereby recruiting new neighbours to surround them. The shapes in the outermost corona are left

5

partially exposed to empty space.
The formula 𝐹𝑛 can be given to a SAT solver, a program that consumes a Boolean formula and determines
whether any assignment of true or false to its variables makes the entire formula true. If the solver reports
that 𝐹𝑛 is satisﬁable, then the coronas of 𝑆 can be read directly from the true variables 𝑠𝑇 ,𝑘 in the satisfying
assignment. I iteratively construct and check 𝐹𝑛 for each 𝑛 ≥ 1 in turn; an unsatisﬁable 𝐹𝑛 implies that 𝑆 has
Heesch number 𝑛 − 1. Unfortunately, 𝐹𝑛 does not contain a strict superset of the clauses of 𝐹𝑛−1, and must
be constructed starting from scratch.

3.2 Suppressing holes

If 𝐹𝑛 is satisﬁable, then the subset of shapes out to the (𝑛 − 1)-corona will be a simply connected patch: every
shape’s halo must be ﬁlled, and so no pockets of empty space can be left behind. However, there is nothing
to prohibit holes from forming between shapes in the 𝑛-corona. Thus the algorithm above can compute only
whether 𝑆 has 𝐻ℎ = 𝑛. If we wish to compute the hole-free Heesch number 𝐻𝑐, then we must suppress all
holes in the outermost corona.
Most such holes that might arise are relatively simple, and can be suppressed easily. These are holes
that are completely enclosed by a pair of adjacent shapes in the 𝑛-corona (Figure 4, centre). I precompute
all pairs of transforms 𝑇1, 𝑇2 ∈ T𝑛 for which 𝑇1 is adjacent to 𝑇2 but 𝑇1 ∪ 𝑇2 is not simply connected. When
constructing 𝐹𝑛, I treat such adjacencies as illegal, and add clauses of the form 𝑠𝑇1,𝑛 → ¬𝑠𝑇2,𝑛 to prevent
them.
However, it is also possible for the 𝑛-corona to contain a hole enclosed by three or more diﬀerent copies
of 𝑆 (Figure 4, right). It would be prohibitive to precompute and suppress all possible holes formed by subsets
of T𝑛. Fortunately, such holes are exceedingly rare and can be eliminated one at a time as they arise, using a
standard trick from discrete optimization. If I am trying to compute a shape’s hole-free Heesch number, and
𝐹𝑛 is reported as satisﬁable, I “draw” the implied packing by assigning symbolic colours to the grid cells in a
2D image, with colours that index the transformed copies of 𝑆. A simple algorithm such as ﬂood ﬁlling can
then search the packing for holes. If none are found, then 𝑆 has 𝐻𝑐 ≥ 𝑛 and the algorithm proceeds to testing
𝐹𝑛+1. If a hole is found, its boundary will be made up of cells belonging to shapes transformed by some set
{𝑇1, . . . , 𝑇𝑚} ⊂ T𝑛. I add a clause ¬𝑠𝑇1,𝑛 ∨ . . . ∨ ¬𝑠𝑇𝑚,𝑛, designed to prevent this precise hole, and re-run the
SAT solver. By repeating his process, eventually we will either ﬁnd a hole-free solution, or the solver will
report the enriched 𝐹𝑛 as unsatisﬁable, implying that 𝑆 has 𝐻𝑐 < 𝑛. Unfortunately, verifying that a patch is
simply connected is necessary and potentially expensive; after initial preprocessing, it is the only part of the
process that relies on the actual geometry of the problem rather than its reduction to Boolean logic. I am not
aware of an eﬀective way to design 𝐹𝑛 to force the 𝑛-corona to be simply connected at the outset.

4 General polyforms

The geometry of polyominoes makes them easy to work with computationally, and simpliﬁes the development
of the previous section. All the geometric computations above can be represented quite compactly in software.
If we assume that we will not enumerate beyond 23-ominoes (already an ambitious goal!), and that Heesch
numbers will not exceed 5, then any conceivable set of coronas will ﬁt inside a 256 × 256 grid, meaning that
a cell coordinate can ﬁt in a single signed byte. By the same token, a transformation can easily ﬁt in 32 bits:
at a minimum, we require eight bits each for the coordinates of the translation, and three more to select a
combination of rotation and reﬂection. Furthermore, any copy of a shape 𝑆 can be represented implicitly via
its transformation, meaning that construction of 𝐹𝑛 can be carried out entirely with 32-bit integers, regardless
of the size of 𝑆. It is only when checking whether a patch is simply connected that I resort to instantiating a
large grid and drawing copies of 𝑆 in it.
The SAT reduction above can be adapted to other classes of polyforms, provided that they are expressible

6

Clause and quantiﬁers Explanation
𝑠𝐼 ,0 The 0-corona is always used.

𝑠𝑇 ,𝑘 → 𝑐 𝑝
For all 0 ≤ 𝑘 ≤ 𝑛
For all 𝑇 ∈ T𝑘
For all 𝑝 ∈ 𝑇 (𝑆)
 If a copy of 𝑆 is used, then its cells are used.

𝑐 𝑝 → 𝑠𝑇1,𝑘1 ∨ . . . ∨ 𝑠𝑇𝑚,𝑘𝑚
For all 0 ≤ 𝑘𝑖 ≤ 𝑛
For all 𝑇𝑖 ∈ T𝑘𝑖
Where 𝑝 ∈ 𝑇𝑖 (𝑆)
 If a cell is used, then some copy of 𝑆 must use it.

𝑠𝑇 ,𝑘 → 𝑐𝑞
For all 0 ≤ 𝑘 ≤ 𝑛 − 1
For all 𝑇 ∈ T𝑘
For all 𝑞 ∈ Halo(𝑇 (𝑆))
 If a copy of 𝑆 is used in an interior corona (a 𝑘-
corona for 𝑘 < 𝑛), then that copy’s halo cells must
be used.

𝑠𝑇1,𝑘1 → ¬𝑠𝑇2,𝑘2
For all 0 ≤ 𝑘1, 𝑘2 ≤ 𝑛
For all 𝑇1 ∈ T𝑘1 and 𝑇2 ∈ T𝑘2
Where (𝑇1, 𝑘1) ≠ (𝑇2, 𝑘2)
And 𝑇1(𝑆) ∩ 𝑇2(𝑆) ≠ œ
 Used copies of 𝑆 cannot overlap.

𝑠𝑇 ,𝑘 → 𝑠𝑇1,𝑘−1 ∨ . . . ∨ 𝑠𝑇𝑚,𝑘−1
For all 1 ≤ 𝑘 ≤ 𝑛
For all 𝑇𝑖 ∈ T𝑘−1
Where 𝑇𝑖 is adjacent to 𝑇
 If a copy of 𝑆 is used in a 𝑘-corona, it must be
adjacent to a copy in a (𝑘 − 1)-corona

𝑠𝑇1,𝑘 → ¬𝑠𝑇2,𝑚
For all 2 ≤ 𝑘 ≤ 𝑛
Where 𝑇1 ∈ T𝑘
For all 0 ≤ 𝑚 ≤ 𝑘 − 2
For all 𝑇2 ∈ T𝑚
Where 𝑇2 is adjacent to 𝑇1
 If a copy of 𝑆 is used in a 𝑘-corona, it cannot be
adjacent to a copy in an 𝑚-corona for 𝑚 < 𝑘 − 1.

Figure 3: The clauses that make up the Boolean formula 𝐹𝑛, which is satisﬁable if a shape 𝑆 has
an 𝑛-corona.
 7

Figure 4: A non-tiling 13-omino (left) that demonstrates the problem of detecting holes in the
outermost corona. The middle illustration shows a 1-corona where two adjacent shapes enclose
holes (one is indicated by an arrow). These holes can be suppressed by including a clause forbidding
the two shapes from both being used. On the right, the 2-corona includes a hole bounded by three
copies of the shape. Such holes are diﬃcult to prevent, and are explicitly forbidden after the fact if
they are found.

Figure 5: The basis on the left allows every cell in an inﬁnite hexagonal tiling to be assigned a
unique pair of integer coordinates.

as subsets of a ﬁxed ambient tiling. That easily encompasses the regular tilings by hexagons and equilateral
triangles, giving us polyhexes and polyiamonds. It rules out, for example, shapes formed from edge-to-edge
assemblies of isosceles right triangles, sometimes known as polyabolos or polytans. Of course, even with
polyhexes and polyiamonds we would like to keep the representation of shapes and transformations simple,
compact, and discrete. The solution is to express all coordinates relative to non-standard basis vectors. This
trick is fairly common when working with hexagonal grids in software, but I will summarize the approach
here.

4.1 Polyhexes

The cells in a hexagonal grid can be assigned integer coordinates in a basis with vectors ®𝑣 = (1, 0) and
®𝑤 = ( 1
2 , √3
2 ), connecting a hexagon centre to the centres of two of its neighbours. The basis is illustrated in
Figure 5, together with a portion of a grid labelled with coordinate pairs.
A hexomino has a maximum of 12 distinct orientations, six direct and six reﬂected. They are generated

8

Figure 6: Polyiamonds can be represented eﬃciently using a sparse subset of the hexagonal grid.
The conceptual tiling on the left is spread out to the coloured cells in the hexagonal tiling on the
right.

by a transformation 𝐴 that rotates by 60◦ about the origin, and a transformation 𝐵 that reﬂects across the ®𝑣
axis. Working in the basis { ®𝑢, ®𝑣}, these transformations have simple representations as matrices with integer
entries:
 𝐴 = [0 −1
1 1
 ] , 𝐵 = [1 1
0 −1
]

The products 𝐴𝑖 𝐵 𝑗 for 𝑖 = 0, . . . , 5 and 𝑗 = 0, 1 yield matrices for all 12 orientations which, like their
square counterparts, all have entries in {−1, 0, 1}. These can be combined with translations by vectors with
integer coordinates to represent all possible transformations of a polyhex.
To construct the halo of a polyhex 𝑆, we must consider every cell in the 6-neighbourhood (and not the
8-neighbourhood) of a given cell. These six neighbours can easily be found by oﬀsetting the coordinates of a
cell by the six coordinate pairs in the ring around (0, 0) in Figure 5. The revised deﬁnition of Halo(𝑆) also
aﬀects the deﬁnition of adjacency, and by extension a number of the clauses that make up 𝐹𝑛.
When suppressing holes, verifying that a packing of polyhexes is simply connected also depends on the
distinct topology of the hexagonal grid. It is still possible to draw the packing directly into a square image
using the cells’ integer coordinates and to use a ﬂood ﬁll to detect holes. But unlike the square case, after
ﬁlling an empty grid cell the algorithm must walk recursively to the empty cells in its 6-neighbourhood.

4.2 Polyiamonds

Polyiamonds are slightly more complicated than polyominoes or polyhexes, in that there are two possible
orientations for cells in the inﬁnite tiling by equilateral triangles. So, for example, translations cannot simply
bring any triangle into correspondence with any other—they must respect orientation. I build a somewhat
exotic sparse integer representation of the triangular grid that harnesses the hexagonal representation described
above.
Figure 6 shows part of a triangular grid on the left, with upward-pointing black triangles and downward-
pointing grey triangles. The illustration on the right shows how triangles are assigned coordinates in the
hexagonal grid. Every black triangle has coordinates that are divisible by 3; every grey triangle has coordinates
that are congruent to 1 modulo 3. Other hexagonal cells are simply left unused.
Like a polyhex, a polyiamond has a maximum of twelve orientations. Six of these correspond to
automorphisms of the black triangle at (0, 0) in Figure 6, and can be found among the orientation matrices

9

Table 1: Heesch numbers of 𝑛-ominoes with no holes in the outer corona

𝑛 non-tilers 𝐻𝑐 = 0 𝐻𝑐 = 1 𝐻𝑐 = 2 𝐻𝑐 = 3
7 3 1 2
8 20 6 14
9 198 75 122 1
10 1390 747 642 1
11 9474 5807 3628 39
12 35488 28572 6906 10
13 178448 149687 28694 67
14 696371 635951 60362 58
15 2721544 2598257 123262 25
16 10683110 10397466 285578 66
17 41334494 40695200 639162 130 2
18 155723774 154744331 979375 68
19 596182769 593856697 2325874 198

for hexominoes. The other six combine one of these six transformations with a transformation that swaps
black and grey triangles, for example an application of 𝐵 above followed by a translation by (1, −2). Any
transformation of a polyiamond can be represented by a choice of orientation together with a translation by a
vector whose coordinates are divisible by 3.
Neighbourhoods must also be reconsidered in this model. When computing haloes we must take into
account the 12-neighbourhood of each cell in a polyiamond 𝑆, consisting of all cells that share an edge or a
vertex with the given cell. In Figure 6, the 12-neighbourhood of (0, 0) consists of every other black and grey
triangle shown, together with one more at (−2, 4). The 12-neighbourhood is ﬁne when computing haloes
and determining adjacency, but not when checking a packing for holes. In that case, a ﬂood ﬁll algorithm
should move from a given cell only to the three neighbours with which it shares an edge.

5 Implementation and results

I have implemented the data structures and algorithms described here as three separate C++ programs, for
the three diﬀerent polyform types. Each program reads a sequence of polyforms in plain text format, and
produces a text report with the values of 𝐻𝑐 and 𝐻ℎ for the input shapes. A command line option causes
the programs to include, for each shape, the set of transformations that make up the coronas in the packings
found by the SAT solver. A separate Python script can read the shape description and transformations and
draw the coronas that realize the shape’s computed Heesch number.
The programs are unable to determine whether a shape tiles the plane, and must be given known non-
tilers as input. I use software written by Joseph Myers [9] to enumerate free polyforms (which are unique up
to rotation and reﬂection) and discard the shapes that tile. I then use a separate program to convert from the
representation Myers uses in his output (a boundary word made up of unit steps from an alphabet of evenly
spaced directions) to an area-based representation (coordinates of cells that make up a polyform).
I use the open-source CryptoMiniSat library [10] as my SAT solver. The library is easy to conﬁgure,
has a simple C++ API, and performs well in practice.
A SAT solver imposes a small amount of overhead on running time, because of the need to translate
problems from their geometric origins into Boolean formulas. However, the beneﬁts of the solver more than

10

Table 2: Heesch numbers of 𝑛-ominoes with holes permitted in the outer corona

𝑛 non-tilers 𝐻ℎ = 0 𝐻ℎ = 1 𝐻ℎ = 2 𝐻ℎ = 3
7 3 0 3
8 20 0 19 1
9 198 36 157 5
10 1390 355 1020 15
11 9474 2820 6544 109 1
12 35488 17409 18038 41
13 178448 100180 78048 219 1
14 696371 485807 210362 202
15 2721544 2185656 535724 164
16 10683110 9300840 1381965 305
17 41334494 37932265 3401701 525 3
18 155723774 148955184 6768266 324
19 596182769 580412188 15769814 767

Table 3: Heesch numbers of 𝑛-hexes with no holes in the outer corona

𝑛 non-tilers 𝐻𝑐 = 0 𝐻𝑐 = 1 𝐻𝑐 = 2 𝐻𝑐 = 3 𝐻𝑐 = 4
6 4 3 1
7 37 5 25 6 1
8 381 70 264 44 3
9 2717 825 1822 67 3
10 18760 8248 10234 265 13
11 116439 67644 47940 817 37 1
12 565943 431882 133484 567 10
13 3033697 2565727 466159 1783 27 1
14 14835067 13676416 1156793 1836 22
15 72633658 69871458 2758485 3534 179 2
16 356923880 350337478 6581529 4818 54 1
17 1746833634 1731652467 15167876 13129 161 1

11

Table 4: Heesch numbers of 𝑛-hexes with holes permitted in the outer corona

𝑛 non-tilers 𝐻ℎ = 0 𝐻ℎ = 1 𝐻ℎ = 2 𝐻ℎ = 3 𝐻ℎ = 4
6 4 3 1
7 37 4 19 12 2
8 381 37 253 84 7
9 2717 434 2091 185 7
10 18760 4332 13766 632 29 1
11 116439 38621 75783 1956 73 6
12 565943 286656 277601 1652 32 2
13 3033697 1895666 1132994 4985 50 2
14 14835067 11201813 3627594 5614 46
15 72633658 61761205 10862327 9802 322 2
16 356923880 325357916 31551809 13997 156 2
17 1746833634 1660634503 86167750 30811 569 1

Table 5: Heesch numbers of 𝑛-iamonds with no holes in the outer corona

𝑛 non-tilers 𝐻𝑐 = 0 𝐻𝑐 = 1 𝐻𝑐 = 2 𝐻𝑐 = 3 𝐻𝑐 = 4
7 1 1
8 0
9 20 11 9
10 103 44 55 3 1
11 594 236 346 11 1
12 1192 826 364 1 1
13 6290 4360 1884 24 2
14 18099 14949 3141 8
15 54808 48108 6661 39
16 159048 148881 10153 13 1
17 502366 474738 27544 83 1
18 1374593 1341460 33100 33
19 4076218 4001470 74689 57 2
20 11378831 11282686 96091 51 2 1
21 32674779 32505745 168959 73 2
22 93006494 92740453 265977 62 2
23 264720498 264216706 503651 140 1
24 748062099 747476118 585571 384 26

12

Table 6: Heesch numbers of 𝑛-iamonds with holes permitted in the outer corona

𝑛 non-tilers 𝐻ℎ = 0 𝐻ℎ = 1 𝐻ℎ = 2 𝐻ℎ = 3 𝐻ℎ = 4
7 1 1
8 0
9 20 7 13
10 103 33 59 10 1
11 594 117 446 30 1
12 1192 495 692 4 1
13 6290 2639 3598 51 2
14 18099 10328 7745 25
15 54808 36965 17748 91 4
16 159048 124954 34058 35 1
17 502366 414119 88072 173 2
18 1374593 1239971 134541 80 1
19 4076218 3776105 299954 157 2
20 11378831 10921532 457157 139 2 1
21 32674779 31831654 842947 174 4
22 93006494 91551851 1454494 147 2
23 264720498 262051399 2668753 343 3
24 748062099 744472222 3589353 425 99

compensate for this added cost. Human intuition is easily seduced by the structure of a geometric problem,
and that intuition colours the choice of algorithm used in solving the problem. Sometimes the resulting
algorithms are perfectly ﬁne. But here, a “natural” approach—walk around the boundary of a shape, gluing
on neighbours, and backtrack when no legal option exists for continuing—can get stuck in “backtracking
hell”. An unavoidable dead end may lurk far out along the boundary of a shape, with exponentially many (or
more!) conﬁgurations of neighbours to be explored along the way, all of which will be rejected. The earlier
work of Mann and Thomas [8] attempts to surround in a ﬁxed order, and they report a number of cases where
their algorithm times out. A SAT solver has no particular opinion on the geometric structure of the problem
domain. Its input is an undiﬀerentiated collection of clauses, and it will take advantage of any opportunity it
can ﬁnd to narrow the search space, regardless of order or locality.
I have not attempted to gather full information about the running times of these programs. On a single
core of a 40-CPU cluster node with 2.2 GHz Intel Xeon processors, I can compute the Heesch numbers of
all 1390 non-tiling 10-ominoes in about 220 seconds, on average about 0.16 seconds per shape. I have also
sampled the running times on batches of the much larger 17-hexes, and the average per-shape computation
time is comparable. Unsurprisingly, the computation time appears to increase exponentially for shapes with
higher Heesch numbers. For example, shapes with Heesch number 4 might require 30 seconds to a minute of
computation time. But because such shapes become progressively more rare as the Heesch number increases,
the overall eﬀect on computation time is negligible.
Tables 1–6 list Heesch numbers for all the non-tiling polyforms I tested, up to 19-ominoes, 17-hexes,
and 24-iamonds. For values of 𝑛 smaller than those shown in the tables, no non-tilers exist. Permitting holes
in the outermost corona oﬀers shapes more freedom to form coronas. As a result, the rows of the 𝐻ℎ tables
are weighted slightly more to the right than the corresponding rows of the 𝐻𝑐 tables.
Of course, a few highlights deserve to be shared. I am particularly interested in the smallest polyforms

13

Figure 7: The smallest polyominoes with Heesch numbers 2 and 3, with and without holes in the
outermost corona. The 11-omino has a single square hole on the right side of the packing.

14

Figure 8: The smallest polyhexes with 𝐻𝑐 = 1, 2, 3, 4.

15

Figure 9: The smallest polyiamonds with 𝐻𝑐 = 1, 2, 3, 4.

16

that exhibit each successive Heesch number. Figure 1 already shows the smallest polyominoes with 𝐻𝑐 = 1
and 𝐻ℎ = 1. Figure 7 shows the smallest polyominoes with Heesch numbers 2 and 3, both with and without
holes. In Figures 8 and 9, I show the smallest polyhexes and polyiamonds with hole-free Heesch numbers 1
through 4. In all cases, my search did not produce any shapes with Heesch numbers higher than the ones
shown.

6 Conclusions

In this article I have demonstrated the eﬀectiveness of recasting the computation of Heesch numbers within
the framework of Boolean satisﬁability. I used a software implementation of this idea to compute Heesch
numbers for a few billion unmarked polyominoes, polyhexes, and polyiamonds. The search did not yield any
shapes that break previous records for Heesch numbers, but provides a lot of data that can be used to deepen
our understanding of this intriguing open problem in tiling theory.
The most obvious avenue for future work is to continue the enumeration to larger polyforms. However,
I am reluctant to do so without signiﬁcant performance improvements or insights on narrowing the set of
polyforms to process. For example, there are more than twice as many 18-hexes as all the Heesch numbers I
have computed so far: over 8.5 billion of them. If they require an average of 0.15 seconds each to process, I
estimate that a 120-core cluster would have to run full-tilt for four months to compute them all.
It would be interesting to reformulate the approach presented here using binary integer programming [6]
instead of Boolean satisﬁability. Some families of clauses might be expressed much more compactly this
way. With satisﬁability, if transformed shapes 𝑇1(𝑆), . . . , 𝑇𝑚(𝑆) all overlap at some cell, then (𝑚
2 ) clauses
of the form 𝑠𝑇𝑖 ,𝑘𝑖 → ¬𝑠𝑇𝑗 ,𝑘 𝑗 are required to rule out all possible overlaps. In binary integer programming,
the shape variables would be assigned the integers 0 or 1, and all overlaps at this cell could be prevented
with the single inequality 𝑠𝑇1,𝑘1 + . . . + 𝑠𝑇𝑚,𝑘𝑚 ≤ 1. However, it is unclear whether this change would boost
performance.
Part of the goal of assembling a large corpus of data is to mine it for patterns. I do not believe that
the tables in this article betray any obvious patterns in the sizes of polyforms that produce certain Heesch
numbers. The general upward trend in each column could be a simple consequence of the exponential growth
in the number of shapes being classiﬁed, and even then the numbers jump around erratically. But there
may be some insight to be gleaned from examinations of the shapes themselves. Mann and Thomas refer to
“forced grouping”, in which tiles in a patch tend to cluster together into larger units [8]. I have observed this
phenomenon in many of my results as well—see for example the 11-hex patch in Figure 8. Forced grouping
may inspire strategies for “amplifying” the Heesch number of a large shape by ﬁnding a way to decompose
it into smaller congruent pieces.
Perhaps the most promising way forward is to consider other families of shapes. The techniques in this
article could easily be extended to handle marked polyforms, simply by prohibiting adjacencies that are not
compatible with the markings. However, it would be crucial to apply markings to polyforms that tile the
plane. Markings can only lower an unmarked shape’s Heesch number, making it pointless to add markings
to any of the polyforms presented here. It would therefore become necessary to check explicitly that a set
of markings prevents a polyform from tiling, whether based on combinatorial imbalance or a more complex
computation. Of course, it would be interesting to explore the use of a SAT solver (or integer programming)
to check whether a shape tiles the plane.
It may also be possible to extend this work to polyforms that are not subsets of an ambient grid, like
the polyabolos mentioned previously, or shapes constructed from unions of Penrose rhombs. In that case we
would likely have to do away with haloes and cell variables, and use computational geometry to test whether
two copies of a shape are disconnected, adjacent, or overlapping. The lack of a grid to organize the plane
would incur a heavy cost, but the greater potential for disorder may pack higher Heesch numbers into smaller

17

shapes.

Acknowledgments

Acknowledgments withheld during peer review.

References

[1] Bojan Bašić. A ﬁgure with Heesch number 6: Pushing a two-decade-old boundary. The Mathematical
Intelligencer, pages 1–4, 2021.

[2] Robert Berger. The undecidability of the domino problem. Number 66 in Memoirs of the American
Mathematical Society. American Mathematical Soc., 1966.

[3] Anne Fontaine. An inﬁnite number of plane ﬁgures with heesch number two. Journal of
Combinatorial Theory, Series A, 57(1):151–156, 1991.

[4] Chaim Goodman-Strauss. Open questions in tiling. https://strauss.hosted.uark.edu/papers/survey.pdf,
2000. Accessed: May 14th, 2021.

[5] Branko Grünbaum and G.C. Shephard. Tilings and Patterns. Dover, second edition, 2016.

[6] LLC Gurobi Optimization. Gurobi optimizer reference manual, 2021.

[7] Casey Mann. Heesch’s tiling problem. The American Mathematical Monthly, 111(6):509–517, 2004.

[8] Casey Mann and B. Charles Thomas. Heesch numbers of edge-marked polyforms. Experimental
Mathematics, 25(3):281–294, 2016.

[9] Joesph Myers. Polyomino, polyhex and polyiamond tiling.
https://www.polyomino.org.uk/mathematics/polyform-tiling/, 2019. Accessed: May 14th, 2021.

[10] Mate Soos, Karsten Nohl, and Claude Castelluccia. Extending SAT solvers to cryptographic problems.
In Oliver Kullmann, editor, Theory and Applications of Satisﬁability Testing - SAT 2009, 12th
International Conference, SAT 2009, Swansea, UK, June 30 - July 3, 2009. Proceedings, volume 5584
of Lecture Notes in Computer Science, pages 244–257. Springer, 2009.

18
