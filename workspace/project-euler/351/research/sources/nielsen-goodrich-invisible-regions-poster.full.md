<!-- source: https://minds.wisconsin.edu/bitstreams/416db04c-caa1-4cad-ac54-13e576d6940a/download | converted from PDF -->

ARBITRARILY LARGE REGIONS OF INVISIBLE
INTEGER LATTICE POINTS
STUDENT RESEARCHERS: Jasmine Nielsen & Austin Goodrich FACULTY MENTOR: Aba Mbirika

REFERENCES

[1] Cesáro, E. Question 75 (Solution). Mathesis 3 (1883), 224-
225.
[2] Mbirika, Aba. Hidden trees in the forest: On lattice points and
prime labeling of graphs. (unpublished), 2012.
[3] Problem Number 47. Project Euler. An online resource for a
series of challenging mathematical problems.
 ACKNOWLEDGMENTS

• UWEC Mathematics Department

• University of Wisconsin - Eau Claire Ofﬁce
of Research and Sponsored Programs

• Poster created with LATEX

FUTURE RESEARCH

More investigation will be done to ﬁnd the closest H 4
(x,y) and H 2
(x,y,z). Also, determining a theorem for
the minimal required prime factors of an arbitrary H n
(x,y) appears to be fairly reasonable. When using
the Chinese Remainder Theorem to determine various H n
(x,y) different permutations of the same n × n
matrix yield different results. We conjecture that the closest hidden forests can be obtained in this way.

INTRODUCTION

Consider the integer lattice in the plane (i.e., all
the points (x, y) such that x and y are integer val-
ues). Imagine for a moment that each integer lat-
tice point is an inﬁnitely thin tree. Which trees
can you see from the origin? Surely on the x-axis,
one can only see the points (1, 0) to the right and
(−1, 0) to the left. But all other “trees” behind
these two points are obscured from view. For ex-
ample, (2, 0) cannot be seen because (1, 0) is block-
ing it. See the diagram to the right, where the blue
vertices are examples of three points which are not
visible since they are obscured from view by a vis-
ible point (denoted by a tree). A natural question
to ask is, what fraction of integer lattice points are
visible from the origin? It turns out that this is a
well-known question with an answer involving a
value that is ubiquitous in mathematics, namely,
the Riemann-zeta function ζ(s) evaluated at s = 2.
Phrased in equivalent terms, the probability that a
 randomly selected lattice point is visible from the
origin is ; that is, approximately 60%. This clas-
sic result was proven in 1883 by Cesáro [1]. So
what can be said about the 40% of invisible lat-
tice points? Are there arbitrarily large patches of
invisible lattice points? Yes.

BACKGROUND

Deﬁnition: A point (x, y) in the integer lattice Z
2

is invisible from the origin if gcd(x, y) > 1.

Theorem: The fraction of pairs (x, y) in the integer
lattice Z
2 such that gcd(x, y) = 1 is ζ(2)
−1 which
equals 6/π2 ≈ .607927. Hence approximately 40%
of Z
2 is invisible.

ζ(s) = ∑∞
n=1 1/(ns)
ζ(2) = ∑∞
n=1 1/(n2) = π2/6 ≈ 1.644934
ζ(3) = ∑∞
n=1 1/(n3) ≈ 1.202057
Deﬁnition: Let n ∈ N. Then n = p
k1
1 p
k2
2 . . . p
kα(n)
α(n)
by the unique factorization theorem, where α(n)
is the number of distinct prime factors dividing n.
Deﬁne the prime set of n to be Pr(n) = {pi}
α(n)
i=1 .
 Deﬁnition: An n × n forest with bottom-left cor-
ner (x, y) in the quadrant Z
+ × Z
+ is denoted
F n
(x,y). If F n
(x,y) is not visible from the origin, then
we call F n
(x,y) a hidden forest and denote it by H n
(x,y).

Theorem: For every n ∈ N, there exists disjoint
sets A1 and A2 each containing n consecutive natural
numbers such that gcd(a1, a2) > 1 whenever ai ∈ Ai.
Hence an n × n hidden forest exists for each n ∈ N.

Deﬁnition: An n × n × n forest with the bottom-
left corner (x, y, z) in the quadrant Z
+ × Z
+ × Z
+

is denoted as F n
(x,y,z) and if hidden then denoted
H n
(x,y,z).
 RESULTS

2 × 2 : For H 2
(x,y) consider the four points (x, y),
(x, y + 1), (x + 1, y), and (x + 1, y + 1). Then
α(x + i) ≥ 2 and α(y + j) ≥ 2 for i, j ∈ {0, 1}.
In particular, we need at least 4 distinct prime fac-
tors p1, . . . , p4 such that:

p1, p2 ∈ Pr(x) p1, p3 ∈ Pr(y)

p3, p4 ∈ Pr(x + 1) p2, p4 ∈ Pr(y + 1)

3 × 3 : For H 3
(x,y) there are three distinct cases.
Optimal Case: x ∈ 2Z, y ∈ 2Z. Let p1 = 2. Then

p1, p2 ∈ Pr(x) p1, p3 ∈ Pr(y)

p3, p4, p5 ∈ Pr(x + 1) p2, p4, p6 ∈ Pr(y + 1)

p1, p6 ∈ Pr(x + 2) p1, p5 ∈ Pr(y + 2)
 4 × 4 : For H 4
(x,y) there are multiple distinct cases.
Optimal Case: 3|x, 3|y, x ∈ 2Z, y ∈ 2Z. Let p1 = 2,
and p2 = 3. Then

p1, p2, p3 ∈ Pr(x) p1, p2, p4 ∈ Pr(y)

p4, p5, p6, p7 ∈ Pr(x + 1) p3, p5, p8, p10 ∈ Pr(y + 1)

p1, p8, p9 ∈ Pr(x + 2) p1, p6, p11 ∈ Pr(y + 2)

p2, p10, p11 ∈ Pr(x + 3) p2, p7, p9 ∈ Pr(y + 3)

2×2×2 : We applied the Chinese Remainder The-
orem to locate H 2
(x,y,z) with x = x0 + 1, y = y0 + 1,
and z = z0 + 1. The eight corner points have coor-
dinates (x0 + i, y0 + j, z0 + k) where 1 ≤ i, j, k ≤ 2.
In the diagram below, the prime numbers corre-
spond to each gcd(x0 + i, y0 + j, z0 + k).
