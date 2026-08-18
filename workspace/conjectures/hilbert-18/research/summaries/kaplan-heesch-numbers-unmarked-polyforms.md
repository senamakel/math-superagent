> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kaplan-heesch-numbers-unmarked-polyforms.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 37842 characters not shown — see `research/sources/kaplan-heesch-numbers-unmarked-polyforms.full.md`]*
