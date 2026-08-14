<!-- source: https://people.uwec.edu/mbirika/paper_lattice_point_visibility.pdf | converted from PDF -->

inv lve

a journal of mathematics

msp

New methods to ﬁnd patches of
invisible integer lattice points

Austin Goodrich, aBa Mbirika and Jasmine Nielsen

2021 vol. 14, no. 2

msp
 INVOLVE 14:2 (2021)

https://doi.org/10.2140/involve.2021.14.283

New methods to ﬁnd patches of
invisible integer lattice points

Austin Goodrich, aBa Mbirika and Jasmine Nielsen

(Communicated by Stephan Garcia)

It is a surprising fact that the proportion of integer lattice points visible from the
origin is exactly 6/π 2, or approximately 60%. Hence, approximately 40% of the
integer lattice is hidden from the origin. Since 1971, many have studied a variety
of problems involving lattice-point visibility, in particular, searching for patterns
in that 40% of the lattice composed of invisible points. One such pattern is a
square patch, an n×n grid of n2 invisible points, which we call a hidden forest.
It is known that there exist arbitrarily large hidden forests in the integer lattice.
However, the methods up to now involve the Chinese remainder theorem (CRT)
on the rows and columns of matrices with prime number entries, and they have
only been able to locate hidden forests very far from the origin. For example,
using this method the closest known 4×4 hidden forest is over 3 quintillion, or
3×1018, units away from the origin. We introduce the concept of quasiprime
matrices and utilize a variety of computational and theoretical techniques to ﬁnd
some of the closest known hidden forests to date. Using these new techniques,
we ﬁnd a 4×4 hidden forest that is merely 184 million units away from the origin.
We conjecture that every hidden forest can be found via the CRT-algorithm on a
quasiprime matrix.
 1. Introduction

Imagine the plane R2 as a forest in which each nonorigin lattice point in Z2 is a
tree and each tree is inﬁnitely thin yet also opaque. In this scenario, we say that a
tree is hidden if some other tree lies in our line of sight from the origin.
Consider the four lines of sight denoted by the dashed line segments emanating
from the origin in Figure 1, left. In these four lines of sight in the ﬁrst quadrant,
exactly four trees are visible — one per each line of sight. These visible trees are
located at the black bullet points. Obscured by them are three other trees at the
white bullet points, which are not visible from the origin. The tree at (2, 6) is

MSC2020: primary 11P21; secondary 11Y99.
Keywords: lattice-point visibility, Chinese remainder theorem, number theory.

283

284 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

1 2 3 4 5 6

1

2

3

4

5

6 (2,6)
 (3,4)
 (6,3)

(5,1)
(2,1)

(1,3)
 (4,2) (10,7)
(4,3)

(3,2)

(7,5)
 (20,14) (21,14)

(20,15) (21,15)

Figure 1. Four visible trees (left), and a 2×2 hidden forest (right).

obscured by the visible tree at (1, 3), while the tree at (6, 3) is obscured by the
tree at (4, 2), which in turn is obscured by the visible tree at (2, 1). The question
of the visibility (or invisibility) of a lattice point from the origin can be recast in
a number-theoretic setting, where it turns out that the only visible points are the
points (x, y) such that gcd(x, y) = 1. A proof for this visibility criterion is given
in Proposition 2.1.
It is well known that approximately 60% of the integer lattice is visible from the
origin (see Proposition 2.4). So a natural question to ask about the approximately
40% of the integer lattice which is hidden from view is the following:

Are there arbitrarily large square patches of invisible lattice points?

The answer to this question is yes, and in this paper we focus on invisible n×n square
patches, which we call hidden forests. An example of a 2×2 hidden forest is given
in Figure 1, right. In this ﬁgure we note the speciﬁc four visible trees that obscure
this hidden forest.
Lattice-point visibility is a well-studied subject that arises in a variety of areas
such as number theory, integer optimization, and even theoretical physics (see
[Brass et al. 2005, Chapter 10.4] for a brief survey). Herzog and Stewart [1971]
studied patterns of both visible and invisible lattice points; one such invisible pattern
they explored is the one we call a hidden forest. Schumer [1990] also examined
hidden forests. He used the Chinese remainder theorem (in a form similar to
our Theorem 3.4) and gave an example of a 3×3 hidden forest very far from the
origin and questioned whether a closer one could be found. He then noted that
ﬁnding a 4×4 forest would require solving systems of linear congruence equations
modulo the product of the ﬁrst 16 primes, the so-called 16th primorial which is
approximately 32 quintillion, and declared, “Such a project is beyond the courage
of this author!” In this paper we not only undertake this task of ﬁnding closer
4×4 hidden forests, but also introduce a variety of theoretical and computational

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 285

techniques to aid in ﬁnding the closest known n×n hidden forests for n ≥ 4, a task
which has not yet been done to date. The paper is broken down as follows:
In Section 2, we give a brief overview of lattice-point visibility and provide a
detailed proof of the well-known result that the probability of two randomly selected
integers being relatively prime is 6/π 2.
In Section 3, we give the known method of ﬁnding hidden forests in Section 3A.
Given n ∈ N and a prime matrix Pn, there exists an n×n hidden forest H n
(x,y) in the
ﬁrst quadrant with bottom-left corner (x, y) that is found by applying the Chinese
remainder theorem to the rows and columns of Pn. We denote this process by the
term CRT-algorithm. In Section 3B, we elaborate on the relationship between a
prime matrix Pn and its hidden forest H n
(x,y) with the introduction of an object
called a gcd-matrix. In Section 3C, we apply this method to ﬁnd hidden forests
H n
(x,y) for n = 2, 3, 4.
In Section 4, we introduce the concept of a quasiprime matrix QPM and the
QP-algorithm in Section 4A and deﬁne the method of strings of strongly composite
integers in Section 4B. In Section 4C, we explore the notion of an optimal gcd-matrix
by considering the minimal number of prime factors required in a quasiprime matrix
to produce an n×n hidden forest. With these three tools and some computational
programming techniques, we then use the CRT-algorithm on quasiprime matrices
to ﬁnd n×n hidden forests. The resulting hidden forests turn out to be much closer
to the origin than those found by the traditional method (given in Section 3).
In Section 5, we combine the techniques detailed in the previous section to ﬁnd
the closest known (to date) 5×5 hidden forest.
In Section 6, we give a selection of open problems.

2. Density of visible lattice points in Z2

As mentioned in the introduction, a criterion for the visibility of an integer lattice
point can be recast in the number-theoretic setting as the following proposition
shows.

Proposition 2.1. Let (x, y) ∈ Z2 \ {(0, 0)}. Then (x, y) is visible if and only if
gcd(x, y) = 1.

Proof. Let (x, y) be a nonorigin point in Z2. Suppose d = gcd(x, y). If d > 1 then
(x/d, y/d) lies strictly between the points (0, 0) and (x, y), and hence (x, y) is not
visible. Thus (x, y) visible implies that gcd(x, y) = 1.
Conversely, assume that d = 1 and suppose by way of contradiction that (x, y)
is not visible from the origin. Then there is a point (x0, y0) ∈ Z2 such that we have
(x, y) = (cx0, cy0) for some integer c > 1. That is, c divides both x and y. But
d = 1 is the greatest common divisor of x and y, contradicting that c > 1. Thus if
gcd(x, y) = 1 then (x, y) is visible. □

286 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

Now that we have a simple criterion for an integer lattice point’s visibility, it is
natural to inquire what fraction of integer lattice points are visible from the origin.
That is, we ask:
 What is the density of visible lattice points in Z2?

Let T (n) equal the total number of integer lattice points in an n×n square centered
at the origin, and let V (n) equal the number of these points visible from the origin.
Then it sufﬁces to compute the limit of V (n)/T (n) as n approaches inﬁnity. It turns
out this limit is 6/π 2. Proofs of this famous result are well known with the earliest
proofs given in the late 19th century (see references in Remark 2.2). Many modern
solutions involve the Möbius inversion formula and Euler’s totient function. In
Proposition 2.4, we provide an alternative proof that is essentially an application of
Euler’s famous product formula and utilizes the number-theoretic criterion for the
visibility of a lattice point given in Proposition 2.1.

Remark 2.2 (historical background to the problem). The historical record of the
original authorship of the result in Proposition 2.4 is inaccurately described on a
number of occasions in the literature. Originally, the question on the probability
of two random integers being coprime was raised by Cesàro [1881]. Two years
later, Cesáro [1883] and Sylvester [1883] independently proved the result. Earlier
Dirichlet [1849] proved a slightly weaker form of the result. The generalization to
k coprime integers with k > 2 was presented again by Cesàro [1884]. This result
was also proven independently by Lehmer [1900].

Remark 2.3. Since there is no uniform distribution on the natural numbers, it is
somewhat imprecise to speak about the probability that two integers chosen at
random are relatively prime. However, if we consider the uniform distribution on
the set {1, 2, . . . , n} and take the limit as n approaches inﬁnity, then it is within this
context that we make any probability statements in Proposition 2.4.

Proposition 2.4. The density of integer lattice points that are visible from the origin
is 6/π 2, or approximately 60%.

Proof. It sufﬁces to show that a lattice point chosen at random has a probability of
6/π 2 of being visible from the origin. Let x and y be randomly selected integers.
Recall that (x, y) is visible if and only if gcd(x, y) = 1 by Proposition 2.1. Hence
it sufﬁces to compute the probability that no prime divides both x and y. The
probability that x is divisible by the prime p is 1/ p. Similarly y is divisible by p
with probability 1/ p. By mutual independence, the probability that both x and y
are divisible by p is 1/ p2. Hence, the probability that both integers x and y are not
divisible by p is 1 − 1/ p2. For distinct primes, these divisibility events are mutually

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 287

independent; thus the probability that no prime divides both x and y is

∏

p
 (
1 − 1
p2
 ).

To calculate this inﬁnite product, it is helpful to consider the Riemann zeta function

ζ (s) = ∑

n≥1
 1
ns = 1
1s + 1
2s + 1
3s + · · ·

for s > 1. A result of Euler connects this inﬁnite sum with an inﬁnite product
of inﬁnite sums over the primes. The essence of Euler’s proof is his use of the
fundamental theorem of arithmetic to observe that the sum ζ (s) can be written as

∑

n≥1
 1
ns = ∏

p
 (
1 + 1
ps + 1
p2s + 1
p3s + · · ·
). (1)

To prove (1), Euler observed that since each n in the denominator on the left-hand
side is of the form n = pαi1
i1 pαi2
i2 · · · pαik
ik for some k by the fundamental theorem of
arithmetic, by multiplying out the product on the right-hand side, each term 1/ns on
the left-hand side appears exactly once, as a product of the appropriate powers of
the primes in n. And since each multiplicand on the right-hand side is a geometric
series of the form 1/(1 − 1/ ps), Equation (1) becomes

∑

n≥1
 1
ns = ∏

p
 1
1 − 1/ ps .

Setting s = 2 and taking reciprocals, we get

ζ (2)
−1 = 1
∑
n≥1 1/n2 = ∏

p
 (
1 − 1
p2
 )
,

where the right-hand side is the probability value we seek, and the left-hand side
is the reciprocal of the well-known evaluation of the Riemann zeta function at
s = 2, namely ζ (2) = π 2/6 (the solution to the famous Basel problem).1 Hence the
fraction of lattice points (x, y) visible from the origin is 6/π 2 (or approximately
60%), as desired. □

1The Basel problem asks for the exact sum of the reciprocals of the squares of the positive integers.
There are a variety of proofs of this result. The details of 14 different proofs are given in [Chapman
2003], and [Moreno 2015] compiles a comprehensive list of 85 references from Euler to the present
that address the Basel problem.

288 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

3. The traditional method to ﬁnd hidden forests

In the previous section we showed that approximately 60% of the integer lattice
is visible, and hence approximately 40% lies hidden from view. In this section,
we ﬁnd arbitrarily large patches of hidden square regions in Z2 using the known
method. This technique is what we call the CRT-algorithm, since it is mainly an
application of the Chinese remainder theorem (CRT). The strategy is to ﬁnd two
sets of n consecutive integers

X = {x1, x2, . . . , xn} and Y = {y1, y2, . . . , yn}

such that X ∩ Y = ∅ and gcd(xi , y j ) > 1 for all 1 ≤ i, j ≤ n. Then it is clear that
the n2 points in the set {(xi , y j ) | 1 ≤ i, j ≤ n} yield the desired hidden square
region. To this end, we ﬁrst establish some necessary preliminary deﬁnitions.

Deﬁnition 3.1 (hidden forest). An n×n hidden forest in Z2 is a square patch of
n2 adjacent invisible integer lattice points. We denote this hidden forest by the
symbol H n
(x,y), where (x, y) is the closest corner lattice point of the square to the
origin. By the remark below, this closest corner point is well-deﬁned.

Remark 3.2. Observe that the points (x, ±1) and (±1, y) are visible for all x, y ∈ Z
by Proposition 2.1. Hence no nontrivial (that is, n > 1) hidden forest H n
(x,y) will
contain any points on the x- or y-axes. Hence we conclude that any H n
(x,y) for n > 1
is completely contained in the interior of one of the four quadrants.

Deﬁnition 3.3 (prime matrix). Let { p1, p2, . . . , pn2} be the set of the ﬁrst n2 primes.
Construct an n×n matrix with these primes by ﬁlling row i with p(i−1)n+1 through
p(i−1)n+n for each 1 ≤ i ≤ n to yield











 p1 p2 · · · p j · · · pn
pn+1 pn+2 · · · pn+ j · · · p2n
p2n+1 p2n+2 · · · p2n+ j · · · p3n
... ... ... ...
p(i−1)n+1 p(i−1)n+2 · · · p(i−1)n+ j · · · p(i−1)n+n
... ... ... ...
p(n−1)n+1 p(n−1)n+2 · · · p(n−1)n+ j · · · pn2
 










 .

Note that the prime p(i−1)n+ j , boxed for visual ease, is located in row i and column j
of the matrix. We call this n×n matrix a prime matrix and denote it by Pn.

3A. The CRT-algorithm. The following theorem is the primary tool used in the
CRT-algorithm to ﬁnd hidden forests of arbitrary size.

Theorem 3.4. For each n ∈ N, there exist two sets of n consecutive numbers X =
{x1, x2, . . . , xn} and Y = {y1, y2, . . . , yn} such that X ∩ Y = ∅ and gcd(xi , y j ) > 1
for all 1 ≤ i, j ≤ n.

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 289

Proof. Fix n ∈ N. Consider the prime matrix Pn. Let Ri and C j be the product of
the entries in row i and column j, respectively, so we have

Ri =
 n∏

k=1 p(i−1)n+k and C j =
 n−1∏

k=0 pkn+ j .

Since they share no primes in common, the row products R1, R2, . . . , Rn are pair-
wise relatively prime. Similarly, the column products C1, C2, . . . , Cn are pairwise
relatively prime. Consider the pair of systems of linear congruences




x + 1 ≡ 0 (mod R1),
x + 2 ≡ 0 (mod R2),
...
x + n ≡ 0 (mod Rn),
 



y + 1 ≡ 0 (mod C1),
y + 2 ≡ 0 (mod C2),
...
y + n ≡ 0 (mod Cn).

Observe that R1 · R2 · · · Rn = C1 · C2 · · · Cn = ∏n2
i=1 pi , which we denote by M.
By the Chinese remainder theorem, there exist solutions x0 and y0 to the left and
right systems, respectively, such that x0 and y0 are unique modulo M. Deﬁne the
set X = {x0 + 1, x0 + 2, . . . , x0 + n} and the set Y = {y0 + 1, y0 + 2, . . . , y0 + n}.
We claim that none of the integers in X are pairwise relatively prime to any of the
integers in Y. For an arbitrary x0 + i ∈ X and y0 + j ∈ Y, these two elements by
construction are multiples of Ri and C j , respectively. Hence the prime that lies
in the intersection of row i and column j in the matrix, namely p(i−1)n+ j , divides
gcd(x0 + i, y0 + j). Thus gcd(x0 + i, y0 + j) > 1 as desired.
Observe that for n ≥ 2 the sets X and Y are necessarily disjoint. Otherwise if
X ∩ Y ̸= ∅ then some element a ∈ X is relatively prime to some element a ± 1 ∈ Y
since gcd(a, a ± 1) = 1, contradicting gcd(x0 + i, y0 + j) > 1 for all 1 ≤ i, j ≤ n.
For the trivial case when n = 1, the algorithm above yields X = Y = {2}. So set
Y = {4}, and hence X ∩ Y = ∅. □

Algorithm (CRT-algorithm to construct a hidden forest H n
(x,y)).

(1) Fix a value n ∈ N.

(2) Construct the prime matrix Pn.

(3) Apply Theorem 3.4 to Pn to yield sets X and Y.

(4) Construct the hidden forest H n
(x,y) from X and Y.

3B. The gcd-grid and gcd-matrix yielded by prime matrices. By Theorem 3.4, the
prime matrix Pn yields the hidden forest H n
(x,y) composed of the n2 points (xi , y j ),
where xi = x0 + i ∈ X and y j = y0 + j ∈ Y for 1 ≤ i, j ≤ n. The forest H n
(x,y) is
shown in Figure 2. For each H n
(x,y) we can write a corresponding n×n array of
numbers called the gcd-grid where gi, j = gcd(xi , y j ) for 1 ≤ i, j ≤ n. The gcd-grid
is shown in Figure 2.

290 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

... ... ... ... ... ...

... ... ... ... ... ...
· · · · · ·

· · · · · ·

· · · · · ·

· · · · · ·

· · · · · ·

(x1, y1)

(x1, y2)

(x1, y j )

(x1, yn)
 (x2, y1) (xi , y1) (xn, y1)

(xi , y j )

(xi , yn)
 (xn, y j )

(xn, yn)
 ... ... ... ... ... ...

... ... ... ... ... ...
· · · · · ·

· · · · · ·

· · · · · ·

· · · · · ·

· · · · · ·

g1,1

g1,2

g1, j

g1,n
 g2,1 gi,1 gn,1

gi, j

gi,n
 gn, j

gn,n

Figure 2. The hidden forest H n
(x,y) (left) and the gcd-grid of H n
(x,y) (right).

We may also consider the gcd-grid as a matrix if we collapse the grid structure
and place the n2 gcd-values into a matrix in the same locations that they appear in
the gcd-grid:
 GcdPn =
 








g1,n g2,n · · · gi,n · · · gn,n
... ... ... ...
g1, j g2, j · · · gi, j · · · gn, j
... ... ... ...
g1,2 g2,2 · · · gi,2 · · · gn,2
g1,1 g2,1 · · · gi,1 · · · gn,1









 .

We call this matrix arising from the gcd-grid the gcd-matrix corresponding to Pn
and denote it by GcdPn . If we denote the prime p(i−1)n+ j in row i and column j of
matrix Pn by pi, j , then the prime matrix given in Deﬁnition 3.3 can be written as

Pn =
 








 p1,1 p1,2 · · · p1, j · · · p1,n
p2,1 p2,2 · · · p2, j · · · p2,n
... ... ... ...
pi,1 pi,2 · · · pi, j · · · pi,n
... ... ... ...
pn,1 pn,2 · · · pn, j · · · pn,n









 .

Remark 3.5. The (i, j)-entry of Pn is pi, j . However, the (i, j)-entry of GcdPn is
not gi, j . In fact, the entry gi, j is in row n − ( j − 1) and column i of GcdPn .

Comparing the locations of the entries gi, j and pi, j of the matrices GcdPn and Pn,
respectively, as the values i and j vary, we observe that the subscripts of the entries
in one matrix are a rotation of the subscripts of the entries in the other. In particular,
the following proposition describes the relationship between the matrices GcdPn
and Pn via a third matrix which we call ˜GcdPn .

Proposition 3.6. Let Pn be a prime matrix. A rotation by 90◦ counterclockwise of
the entries in Pn gives a corresponding matrix, which we denote by ˜GcdPn , and the
(i, j)-entry in ˜GcdPn divides the (i, j)-entry in the gcd-matrix GcdPn .

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 291

Proof. The rotational relationship between Pn and ˜GcdPn is given by a simple
matrix calculation. If we let ADn be the antidiagonal matrix — that is, a matrix with
ones in the antidiagonal and zeroes elsewhere, then ˜GcdPn = (Pn · ADn)T, where T
denotes the transpose of a matrix. In particular, multiplying Pn on the right by ADn
reverses the columns of Pn, and then transposing this result yields ˜GcdPn as desired.
After this rotation on Pn is performed, the entry pi, j of ˜GcdPn is then located in
row n − ( j − 1) and column i. In this same location in GcdPn is gi, j . Below we
give an illustration of this process:

Pn =
 








 p1,1 p1,2 · · · p1, j · · · p1,n
p2,1 p2,2 · · · p2, j · · · p2,n
... ... ... ...
pi,1 pi,2 · · · pi, j · · · pi,n
... ... ... ...
pn,1 pn,2 · · · pn, j · · · pn,n










⟲
90◦ left↦−−−−→ ˜GcdPn =
 








 p1,n p2,n · · · pi,n · · · pn,n
... ... ... ...
p1, j p2, j · · · pi, j · · · pn, j
... ... ... ...
p1,2 p2,2 · · · pi,2 · · · pn,2
p1,1 p2,1 · · · pi,1 · · · pn,1









 .

In the proof of Theorem 3.4, we observed that by construction the prime pi, j
divides the value gcd(x0 +i, y0 + j) = gi, j . Hence, the (i, j)-entry in ˜GcdPn divides
the (i, j)-entry in GcdPn . □

Remark 3.7. The rotational relationship between Pn and ˜GcdPn proves to be very
important in Section 4 when we perform the reverse rotation. Starting from a
gcd-matrix, a clockwise rotation will help us produce a quasiprime matrix, crucial
for ﬁnding closer hidden forests.

3C. An application: the n = 2, 3, 4 cases.

Example 3.8. In the 2×2 case, using Theorem 3.4, we set n = 2 and the prime
matrix is
 P2 = (2 3
5 7
) .

The row products are R1 = 6 and R2 = 35, while the column products are C1 = 10
and C2 = 21. Hence the corresponding linear congruences we need to solve are

x + 1 ≡ 0 (mod 6), y + 1 ≡ 0 (mod 10),

x + 2 ≡ 0 (mod 35), y + 2 ≡ 0 (mod 21).

By the CRT-algorithm, the left and right systems have the unique solutions x0 =
173 (mod 210) and y0 = 19 (mod 210), respectively. Set X = {174, 175} and
Y = {20, 21}. Then X ∩ Y = ∅ and gcd(xi , y j ) > 1 for all 1 ≤ i, j ≤ 2. Thus

292 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

there is a hidden forest H 2
(174,20) of four trees at (174, 20), (174, 21), (175, 20),
and (175, 21). Below we give the hidden forest on the left and its corresponding
gcd-grid on the right:

(174,20)

(174,21)
 (175,20)

(175,21)
 gcd(174, 20) = 2

gcd(174, 21) = 3
 5 = gcd(175, 20)

7 = gcd(175, 21)

Then by Proposition 3.6, we have the following map from P2 to ˜GcdP2:

P2 = (2 3
5 7
) ⟲
90◦ left↦−−−−→ ˜GcdP2 = (
3 7
2 5
) .

In this example, the ˜GcdP2 coincides with the gcd-matrix GcdP2, and so the (i, j)-
entry of ˜GcdP2 divides the (i, j)-entry of GcdP2 as Proposition 3.6 guarantees. This
is an effect of the so-called law of small numbers, since we see in the cases of
larger n to follow that this coincidence does not occur.

Example 3.9. In the 3×3 case, using Theorem 3.4, we set n = 3 and the prime
matrix is
 P3 =
 

 2 3 5
7 11 13
17 19 23



 .

The CRT-algorithm gives the solutions x0 = 119,740,619 and y0 = 121,379,047,
which are both unique modulo 223,092,870. Hence the nine coordinates (xi , y j ) of
H 3
(119740620,121379048) have the following values and respective prime factorizations:

x1 = 119,740,620 = 22·3·5·1,995,677, y1 = 121,379,048 = 23·7·17·59·2161,

x2 = 119,740,621 = 7·11·13·37·53·61, y2 = 121,379,049 = 32·11·19·173·373,

x3 = 119,740,622 = 2·17·19·23·8059, y3 = 121,379,050 = 2·52·13·23
2·353.

It is readily veriﬁed that the corresponding 3×3 hidden forest has the following
gcd-grid:
 2
2

3

2·5
 7
 11

13
 2·17

19

2·23

For example, the top-right node corresponds to the (x3, y3)-coordinate, and it is
labeled by the value gcd(x3, y3) = 2 · 23 since x3 = 2 · 17 · 19 · 23 · 8059 and
y3 = 2 · 52 · 13 · 232 · 353. And by Proposition 3.6, we have the following map from

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 293

P3 to ˜GcdP3:
 P3 =
 

 2 3 5
7 11 13
17 19 23



 ⟲
90◦ left↦−−−−→ ˜GcdP3 =
 


5 13 23
3 11 19
2 7 17



 .

Observe that, as expected, the (i, j)-entry of ˜GcdP divides the (i, j)-entry of the
gcd-matrix
 GcdP3 =
 


2·5 13 2·23
3 11 19
22 7 2·17



 .

Example 3.10. In the 4×4 case, the CRT-algorithm on the prime matrix gives the
solution x0 = 2,847,617,195,518,191,809,

y0 = 1,160,906,121,308,397,397.

The absurdly large solution values in Examples 3.9 and 3.10 reveal that the
CRT-algorithm applied to prime matrices is hardly useful for ﬁnding n×n hidden
forests which are close to the origin for cases even as small as n = 3 and n = 4.
For instance, we prove later that the closest H 3
(x,y) is at x = 1274 and y = 1308.
Furthermore, we reveal that there is an H 4
(x,y) at x = 134,043 and y = 184,785,885.
The x-value of the H 4
(x,y) which the CRT-algorithm on a prime matrix yields is
2.12441×1013 times larger than this x-value, 134,043, of the H 4
(x,y) which we
found.

Remark 3.11. It turns out that the number 134,043 is a very interesting integer; it is
the smallest positive integer n such that the numbers in the set {n, n +1, n +2, n +3}
have exactly four prime factors each.2 We later use this value to calculate the closest
known H 4
(x,y), bearing the smallest x-value, in Example 4.8.

4. New methods to ﬁnd closer hidden forests

The previous section detailed the well-known method of using the CRT-algorithm on
prime matrices to ﬁnd arbitrarily large hidden forests. The main problem with that
method is that for n ≥ 3 the locations of these H n
(x,y) are substantially further away
from the origin and thus progressively harder to compute. The aim of this section
is to introduce two concepts, namely quasiprime matrices and strings of strongly
composite integers, to help ﬁnd substantially closer H n
(x,y). In this section we give
the closest H n
(x,y) for n = 2, 3 and the closest known (to date) H n
(x,y) for n = 4.

2This is known as Problem 47 on the website https://projecteuler.net/about started in 2001 by
Colin Hughes [Somers 2011]. Project Euler gives a series of challenging computational problems
that require more than just mathematical insights to solve. Nayuki Minase’s very simple solution via
Mathematica to Problem 47 is given in Section 4B.

294 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

(20,14) (21,14)

(20,15) (21,15)
(14,20) (15,20)

(14,21) (15,21)

(20,-15) (21,-15)

(20,-14) (21,-14)

(14,-21) (15,-21)

(14,-20) (15,-20)

(-21,14) (-20,14)

(-21,15) (-20,15)
(-15,20) (-14,20)

(-15,21) (-14,21)

(-21,-15) (-20,-15)

(-21,-14) (-20,-14)

(-15,-21) (-14,-21)

(-15,-20) (-14,-20)

Figure 3. Eight copies of the closest 2×2 hidden forest.

Deﬁnition 4.1 (the closest n×n). A hidden forest H n
(x,y) is said to have distance d
from the origin where d is given by

d(x, y) = √x 2 + y2.

We say that H n
(x,y)is the closest n×n hidden forest if it has the minimum distance d
of all hidden n×n forests.

Note that Remark 3.2 guarantees that the closest corner point (x, y) of H n
(x,y) is
well-deﬁned up to quadrant selection.

Convention 4.2. In searching for the closest hidden forest it sufﬁces to search
only half of quadrant I. As seen in Figure 3, any H n
(x,y) has seven copies that are
reﬂectional symmetries, which are the same distance from the origin. We choose to
focus only on H n
(a,b) in quadrant I such that (a, b) lies above the diagonal y = x
(that is, a < b). Note that H n
(a,a) can never exist if n > 1 since gcd(a, a + 1) = 1
and hence (a, a + 1) is a visible point.

4A. Quasiprime matrices and the QP-algorithm. In Proposition 3.6, we begin
with a prime matrix Pn and observe that a 90◦ counterclockwise rotation of Pn yields
˜GcdPn , which relates very closely to the gcd-matrix GcdPn of the corresponding
H n
(x,y) (in particular, recall that the (i, j)-entry of ˜GcdPn divides the (i, j)-entry
of GcdPn ). Now suppose instead that we start with an H n
(x,y) and its associated
gcd-matrix, which we denote by GcdM . If we rotate this matrix 90◦ clockwise, then
we get some matrix M that is not necessarily a prime matrix. Furthermore, applying

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 295

the CRT-algorithm on M may not even be possible (see Example 4.5). But from M,
can we ﬁnd a matrix ̃M such that the (i, j)-entry of ̃M divides the (i, j)-entry of
M and applying the CRT-algorithm on ̃M gives the original H n
(x,y) from which we
started? Based on much computational evidence, the answer appears to be yes. The
matrix ̃M is what we call a quasiprime matrix QPM to be deﬁned in Deﬁnition 4.6,
but a formal proof still awaits. For now, we proceed to give very substantial support
that this conjecture holds for all H n
(x,y) (see Question 1).
To ﬁnd M, we use the matrix equality in Proposition 3.6 and solve for M:

GcdM = (M · ADn)T =⇒ (GcdM )T = M · ADn

=⇒ M = (GcdM )T · ADn, (2)

where (2) follows since an antidiagonal matrix with all ones in its nonzero entries
is its own inverse. Below we give an illustration of this process:

GcdM =
 








g1,n g2,n · · · gi,n · · · gn,n
... ... ... ...
g1, j g2, j · · · gi, j · · · gn, j
... ... ... ...
g1,2 g2,2 · · · gi,2 · · · gn,2
g1,1 g2,1 · · · gi,1 · · · gn,1










⟳
90◦ right↦−−−−→ M =
 








g1,1 g1,2 · · · g1, j · · · g1,n
g2,1 g2,2 · · · g2, j · · · g2,n
... ... ... ...
gi,1 gi,2 · · · gi, j · · · gi,n
... ... ... ...
gn,1 gn,2 · · · gn, j · · · gn,n









 .

In the case of n = 2, we see that M is a prime matrix (see Example 4.3). However
in the case of n = 3, the matrix M can have repeated prime number entries and
hence is not a prime matrix (see Example 4.5). And in the case of n ≥ 4, the matrix
can have both repeated primes and composite number entries, and hence is not a
prime matrix (see Example 4.8). In these n ≥ 3 cases, we construct a quasiprime
version of M which we denote by QPM. And an application of the CRT-algorithm
on QPM yields the H n
(x,y) that has the original gcd-matrix corresponding to H n
(x,y).
Before we present an algorithm on how to produce QPM from M, we give two
motivating examples in the n = 2 and n = 3 cases.

Example 4.3 (the closest 2×2). By examining a small grid of points in quadrant I
of Z2, it is easy to notice that the closest H 2
(x,y) occurs at x = 14 and y = 20. Below
we give H 2
(14,20) and to its right the gcd-grid corresponding to the four nodes:

(14,20)

(14,21)
 (15,20)

(15,21)
 2

7
 5

3

296 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

By (2), we can retrieve a matrix M from the gcd-grid above as follows:

GcdM = (
7 3
2 5
) ⟳
90◦ right↦−−−−→ M = (2 7
5 3
) .

Applying the CRT-algorithm to this matrix M, we get x0 = 13 and y0 = 19 as desired.
Hence at the distance of d ≈ 24.4131 we have the closest hidden forest H 2
(14,20).

Remark 4.4. Alternate permutations of the same primes in the gcd-grid, and con-
sequently the matrix M, may produce different solutions under the CRT-algorithm.
This means that for each unique set of n2 primes in the matrix Pn, the CRT-algorithm
can yield up to n2 factorial (not necessarily distinct) H n
(x,y). Compare the previous
example with Example 3.8. Both examples use the same set of primes {2, 3, 5, 7}
but yield drastically different H 2
(x,y).

Example 4.5 (the closest 3×3). At the distance of d ≈ 1825.91 we ﬁnd the closest
hidden forest H 3
(1274,1308). Though others have cited H 3
(1274,1308) as a hidden forest
[Herzog and Stewart 1971; Weisstein], none of these sources have asserted that it
is the closest. For the n = 3 case, the problem of ﬁnding the closest hidden forest
is computationally tractable via exhaustive means. In fact, we wrote Java code,3

which exhaustively checked the square region with lower-left endpoint (0, 0) and
upper-right endpoint (1308, 1308), ﬁnally conﬁrming that this is the closest 3×3
hidden forest. Below we give the hidden forest H 3
(1274,1308) and its corresponding
gcd-grid:
 (1274, 1308)

(1274, 1309)

(1274, 1310)
 (1275, 1308)

(1275, 1309)

(1275, 1310)
 (1276, 1308)

(1276, 1309)

(1276, 1310)
 2

7

2
 3
 17

5
 2
2

11

2

By (2), we can retrieve a matrix M from the gcd-grid above as follows:

GcdM =
 

2 5 2
7 17 11
2 3 22


 ⟳
90◦ right↦−−−−→ M =
 

 2 7 2
3 17 5
22 11 2


 .

Incidentally, the M given here is very similar to the one given in [Herzog and
Stewart 1971], but neither of these matrices can possibly produce the correct H 3
(x,y)
because the Chinese remainder theorem simply cannot work on such matrices. For
example, since the products of row 1 and row 3 of M each have a factor of 4, any
solution x0 to the three row equations would also have to satisfy x + 1 ≡ 0 (mod 4)

3See the online supplement for the Java code.

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 297

and x + 3 ≡ 0 (mod 4), but the existence of such an x0 is absurd. However, this
problem is resolved by introducing the concept of a quasiprime matrix.

Deﬁnition 4.6. Given a matrix M arising from a GcdM via (2), we produce a
quasiprime matrix QPM deﬁned by the QP-algorithm given below.

Algorithm (QP-algorithm to construct a quasiprime matrix QPM).

(1) Construct matrix M arising from a GcdM via (2).

(2) Let { pi }
s
i=1 be the union of the sets of all primes appearing in the prime
factorizations of each entry of M.

(3) For a ﬁxed pi with 1 ≤ i ≤ s, locate the entry in M which contains pk
i for
k ≥ 1 such that k is largest. If there is more than one entry which contains pk
i ,
then choose exactly one.

(4) Place the selected pk
i in QPM in the same location where it appears in M. Place
the value 1 in QPM in every location where a p j
i appears in M for each j ≤ k.

(5) Repeat the previous two steps for each pi with 1 ≤ i ≤ s.

Example 4.7 (the closest 3×3 via a quasiprime matrix). From the matrix M in
Example 4.5, we can produce the quasiprime matrix as follows using the QP-
algorithm:
 M =
 

 2 7 2
3 17 5
22 11 2


 QP
algorithm↦−−−−→ QPM =
 

 1 7 1
3 17 5
22 11 1


 .

By use of the CRT-algorithm on QPM, we solve the system of linear congruences

x + 1 ≡ 0 (mod 7), y + 1 ≡ 0 (mod 22 · 3),

x + 2 ≡ 0 (mod 3 · 5 · 17), y + 2 ≡ 0 (mod 7 · 11 · 17),

x + 3 ≡ 0 (mod 22 · 11), y + 3 ≡ 0 (mod 5),

which has solutions x0 = 1273 and y0 = 1307. Hence the QPM yields the closest
3×3 hidden forest H 3
(1274,1308).

4B. Computer-heavy approach: strings of strongly composite integers. Another
technique we implement that proves very powerful in ﬁnding hidden forests involves
using strings of consecutive integers each with several prime factors. In Section 5,
we ﬁnd that combining the technique below with a clever computational use of
quasiprime matrices yields the closest known n×n hidden forests for n ≥ 4.
Schumer [1990] proved that there exist strings of n consecutive integers each
divisible by at least k distinct primes, which he calls strings of strongly composite in-
tegers. The proof uses the Chinese remainder theorem, and hence, like Theorem 3.4,
it produces very large numbers for n ≥ 3. However, there is an efﬁcient way to ﬁnd

298 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

the smallest set of n consecutive integers each with at least k prime factors each
(ignoring multiplicity). We can then use these values as our x-values in our hunt
for closer hidden forests for n ≥ 4.
The following Mathematica code, which is Nayuki Minase’s solution to Project
Euler Problem 47, easily produces the very ﬁrst number n in a sequence of four
consecutive integers each with four prime factors (ignoring multiplicity):

Has4PrimeFactors[n_] := Length[FactorInteger[n]] == 4
i = 2;
While[! (Has4PrimeFactors[i] && Has4PrimeFactors[i + 1] &&
Has4PrimeFactors[i + 2] && Has4PrimeFactors[i + 3]), i++]
i

The value that it yields is 134,043. This number and the next three consecutive
integers have the prime factorizations

134,043 = 3 · 7 · 13 · 491,

134,044 = 22 · 23 · 31 · 47,

134,045 = 5 · 17 · 19 · 83,

134,046 = 2 · 3
2 · 11 · 677.

Example 4.8 (the closest 4×4 to date with the smallest x-value). Using the four
values 134,043 to 134,046 as the x-values of 4×4 hidden forest we seek, we
exhaustively searched for the very ﬁrst set of four consecutive integers such that all
four values share at least one prime factor with each of the four values 134,043 to
134,046. After running for only two minutes,4 the Java program which we wrote
outputs the value 184,785,885. This number and the next three consecutive integers
have the prime factorizations

184,785,885 = 32 · 5 · 31
2 · 4273,

184,785,886 = 2 · 17 · 491 · 11,069,

184,785,887 = 11 · 13 · 19 · 23 · 2957,

184,785,888 = 25 · 3 · 7 · 83 · 3313.

Using these four numbers as the y-values of our H 4
(x,y) and the four values 134,043 to
134,046 as the x-values, we get a hidden forest H 4
(134043,184785885) with the following
gcd-grid:

4The run times for the Java code are based on the code running on the Blugold Supercomputing
Cluster of UWEC, while the run times for the Mathematica code are based on the code running on a
standard ofﬁce computer.

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 299

3

491

13

3·7
 31

2

23

2
2
 5
 17

19

83
 3
2

2

11

2·3

By (2), we retrieve a matrix M from the gcd-grid above as follows:

GcdM =
 




3·7 22 83 2·3
13 23 19 11
491 2 17 2
3 31 5 32
 



 ⟳
90◦ right↦−−−−→ M =
 




 3 491 13 3·7
31 2 23 22

5 17 19 83
32 2 11 2·3




 .

Applying the QP-algorithm to M, we get the quasiprime matrix

QPM =
 




 1 491 13 7
31 1 23 22

5 17 19 83
32 1 11 1
 



 .

Then applying the CRT-algorithm to QPM indeed yields the forest H 4
(134043,184785885)
as desired.

Remark 4.9. The hidden forest H 4
(134043,184785885) is distance d ≈ 1.84786×108

from the origin. In comparison recall Example 3.10, where we used the only known
method to date in the literature (that is, the prime matrix P4 and Theorem 3.4).
Using that traditional method we found the hidden forest H 4
(x1,y1) with

x1 = 2,847,617,195,518,191,810,

y1 = 1,160,906,121,308,397,398

at a distance d ≈ 3.07516×1018, which is 1.66418×1010 times farther than the
hidden forest which we found in Example 4.8! The matrix P4 and its associated
gcd-grid of our closer hidden forest H 4
(134043,184785885) are as follows:

P4 =
 




 2 3 5 7
11 13 17 19
23 29 31 37
41 43 47 53




 Theorem 3.4
CRT−algorithm↦−−−−−−−→
 2

3

2·5

7
 11

13

17

19
 2·23

29

22 ·31

37
 41

3·43

47

53

300 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

year distance of H 4
(x,y) proof/method given?

Pighizzini and Shallit 2002 2.30574×108 no
Baake and Grimm 2013 1.90265×107 no
Goodrich, Mbirika, and Nielsen 2014 1.84786×108 yes

Table 1. Distances of the three closest known 4×4 hidden forests
in the literature. (We discovered this forest in 2014; however, it is
in this paper in which we give its existence and proof.)

Hence the gcd-matrix of this 4×4 hidden forest is

GcdM =
 




 7 19 37 53
2·5 17 22 ·31 47
3 13 29 3·43
2 11 2·23 41
 



 .

Remark 4.10. Other researchers have found 4×4 hidden forests of distances rela-
tively close to the one shown in Remark 4.9. Pighizzini and Shallit [2002] addressed
the issue of ﬁnding the closest n×n hidden forests. For a positive integer n,
they deﬁne a function S(n), which is the least positive integer r such that there
exists m ∈ {0, 1, . . . , r } with gcd(r − i, m − j) > 1 for 0 ≤ i, j < n. This is
equivalent to ﬁnding the closest n×n hidden forest. They were only successful
in ﬁnding this value for n = 1, 2, 3, but for n = 4 they were able to give bounds
450000 < S(4) ≤ 172379781 by ﬁnding a hidden forest H 4
(x,y) with x = 172,379,778
and y = 153,132,342. An even closer 4×4 hidden forest was later revealed in
[Baake and Grimm 2013, p. 422]. The forest they ﬁnd has bottom left corner
x = 13,458,288 and y = 13,449,225; however, no proof or justiﬁcation of how this
was found is given. Moreover, they give no assertion regarding whether this is the
closest known 4×4 hidden forest. Table 1 gives the distances of the three closest
known 4×4 hidden forests in the literature.

4C. Computer-free approach: minimum prime factors in an optimal gcd-matrix.
The concept of an “optimal” gcd-matrix for a hidden n×n forest H n
(x,y) depends
on n and is based on the minimal number of prime factors required in the gcd-grid
of H n
(x,y). We ﬁnd that minimizing the number of primes used in the gcd-matrix
while simultaneously maximizing the number of locations in the gcd-grid where a
prime can be used again leads to a closer H n
(x,y) than the traditional method given
in Section 3.
Observe that the gcd-matrix of the H 4
x,y in Remark 4.9 is hardly optimal in
the sense that if the corner entries were all multiples of 3, then we immediately
get the four corners “hidden for free”, as in the forest in Example 4.8 — that is,

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 301

2×3

p3

2

3
 p1
p2

p5

p9
 2
 p4

2

p8
 3

p6

p7

3

Figure 4

the values x1, x4, y1 and y4 would all be divisible by 3 and hence none of the
four points (x1, y1), (x4, y1), (x1, y4), or (x4, y4) would be visible. An optimal
situation is to have one corner, for example, the bottom-left coordinate (x1, y1), be
divisible by both 2 and 3. Then we would have a forest where the gcd of each of
the 16 coordinates (xi , y j ) with 1 ≤ i, j ≤ 4 are divisible by 2, 3, and the nine other
primes p1, . . . , p9 as in Figure 4.
This leads one to consider a different type of gcd-matrix that does not give the
exact gcd gi, j (recall Figure 2, right) for each coordinate (xi , x j ) (recall Figure 2,
left) of H n
(x,y). But on the other hand, this new matrix would simply give the
smallest prime divisor of the gcd for each coordinate. We make this more precise in
Deﬁnition 4.12. But ﬁrst we need to recall the following number-theoretic function.

Deﬁnition 4.11. The prime counting function π : R → N counts the number of
primes less than or equal to a given real number.

Deﬁnition 4.12. Construct an optimal gcd-matrix as follows. Let one of the four
corner entries of the n×n matrix contain the product of the ﬁrst kn := π(n−1) primes
(where π is the prime counting function) if n ≥ 3, and set k2 = 1. Without loss of
generality, choose the bottom-left corner for this value. Denote these ﬁrst kn primes
as q1, q2, . . . , qkn . For each qi with 1 ≤ i ≤ kn, any entry in the matrix that is a mul-
tiple of qi rows to the right of the bottom-left corner and/or a multiple of qi columns
above the bottom-left corner must be ﬁlled with the value qi . If more than one prime
ﬁts this criteria for a speciﬁc matrix entry, then simply multiply the primes in that
entry together. In the remaining unﬁlled entries, place one prime in each entry from
the set of the next smallest primes larger than the prime qkn . Denote this set of primes
by { p1, p2, . . .}. We denote this optimal gcd-matrix by the symbol opt-GcdM .

Example 4.13. An optimal 4×4 gcd-matrix is

opt-GcdM =
 




 3 p9 p8 3
2 p5 2 p7
p3 p2 p4 p6
2×3 p1 2 3
 



 ,

where the entries p1, . . . , p9 are the nine smallest prime numbers other than 2 or 3.
Observe that the locations of the primes 2 and 3 correspond exactly to their location

302 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

12 11 p85 p84 p83 p82 p81 p80 p79 p78 p77 p76 11
11 2, 5 p65 2 p64 2 5 2 p63 2 p62 2, 5 p75
10 3 p57 p56 3 p55 p54 3 p53 p52 3 p61 p74
9 2 p45 2 p44 2 p43 2 p42 2 p51 2 p73
8 7 p37 p36 p35 p34 p33 p32 7 p41 p50 p60 p72
7 2, 3 p25 2 3 2 p24 2, 3 p31 2 3 2 p71
6 5 p21 p20 p19 p18 5 p23 p30 p40 p49 5 p70
5 2 p13 2 p12 2 p17 2 p29 2 p48 2 p69
4 3 p9 p8 3 p11 p16 3 p28 p39 3 p59 p68
3 2 p5 2 p7 2 p15 2 p27 2 p47 2 p67
2 p3 p2 p4 p6 p10 p14 p22 p26 p38 p46 p58 p66
1 • p1 2 3 2 5 2, 3 7 2 3 2, 5 11

3 2 4 4 8 4 12 8 12 8 20
 n kn •-value

2 1 2
3 1 2
4 2 2×3
5 2 2×3
6 3 2×3×5
7 3 2×3×5
8 4 2×3×5×7
9 4 2×3×5×7
10 4 2×3×5×7
11 4 2×3×5×7
12 5 2×3×5×7×11

Figure 5. An optimal gcd-grid with bottom left corner having the
product of kn primes.

in the gcd-grid in Figure 4. The manner in which the p1 through p9 are distributed
in this particular matrix is the n = 4 case that arises from the grid in Figure 5.

The grid in Figure 5 shows us the minimum number of primes and their relative
locations in a candidate for an optimal gcd-matrix for an n×n hidden forest. In this
grid, we choose the bottom-left corner (denoted with the symbol •) to contain the
product of powers of the ﬁrst kn primes where kn is the value given in Deﬁnition 4.12.
In the far-left column, each entry refers to the size n of the corresponding n×n
grid. In the bottom row, in each box we give the number of additional primes that
are needed to go from an n×n grid to an (n+1)×(n+1) grid. For example, for
n = 5, we need a minimum k5 + 3 + 2 + 4 + 4 = 15 distinct primes in the optimal
gcd-matrix for an H 5
(x,y). Indeed in Section 5, we see that this minimum is achieved.

Example 4.14. If n = 4 then k4 = 2, and hence we place 2×3 in a corner location.
This is because the 4×4 portion of the grid in Figure 5 says that we need a minimum
of nine primes, not counting the primes 2 and 3, which are placed in the locations
where they appear in the grid. Hence an optimal gcd-matrix might be

opt-GcdM =
 




 3 29 31 3
2 19 2 23
7 11 13 17
2×3 5 2 3
 



 .

In the boxed entries in the matrix above, we place the nine smallest primes larger
than 3 where the grid in Figure 5 places p1, . . . , p9.
Observe that the forest H 4
(134043,184785885) found in Example 4.8 is the closest
known 4×4 forest and is attained by cleverly using the method of strings of strongly

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 303

composite integers, that is, using computer computation to ﬁnd the smallest four
consecutive values x1, . . . , x4 which each have at least four primes factors each,
and then using computer computation again to compute the next set of four values
y1, . . . , y4, each of which is not relatively prime to all four x-values. However,
the QPM associated to this closest forest is not optimal in the sense that it uses ten
primes (not including 2 and 3), whereas an optimal QPM uses at most nine primes
(not including 2 and 3).
Note that much computer assistance was required to generate H 4
(134043,184785885);
however, no computer assistance whatsoever is required to create the optimal gcd-
matrix, opt-GcdM . From the matrix opt-GcdM in this example, we produce the
quasiprime matrix as follows using the QP-algorithm:

opt-GcdM =
 




 3 29 31 3
2 19 2 23
7 11 13 17
2×3 5 2 3
 



 QP
algorithm↦−−−−−→ QPM =
 





1 29 31 1
1 19 1 23
7 11 13 17
6 5 1 1
 



 .

Applying the CRT-algorithm on QPM, we then get the forest H 4
(x,y) with

x = 153,630,616,137, y = 116,380,988,514

and the following prime factorizations of the 16 coordinates (xi , y j ) for all 1 ≤
i, j ≤ 4:
 x1 = 153,630,616,137 = 3 · 29 · 31 · 229 · 248,749,

y1 = 116,380,988,514 = 2 · 33 · 7 · 37 · 8,321,249,

x2 = 153,630,616,138 = 2 · 19 · 23 · 1723 · 102,019,

y2 = 116,380,988,515 = 5 · 11 · 19 · 29 · 47 · 101 · 809,

x3 = 153,630,616,139 = 7 · 11 · 13 · 17 · 9,028,067,

y3 = 116,380,988,516 = 22 · 13 · 31 · 72,196,643,

x4 = 153,630,616,140 = 22 · 33 · 5 · 103 · 2,762,147,

y4 = 116,380,988,517 = 3 · 17 · 23 · 883 · 112,363.

In Table 2 we summarize the distances of the 4×4 hidden forests found by the
traditional method versus the two new methods given in this paper.
So we can easily see that the two new methods produce substantially closer
hidden forests than the traditional methods. However, we ﬁnd that merging the
method of strings of composite integers with the method of the optimal matrix is an
even better idea. And that is precisely what we do in the 5×5 case in the following
section.

304 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

method distance location

traditional approach CRT-algorithm 3.07516×1018 Example 3.10
computer-heavy approach with QP-algorithm 1.84786×108 Example 4.8
computer-free approach with QP-algorithm 1.92735×1011 Example 4.14

Table 2. Distances of the 4×4 hidden forests found by the tradi-
tional method versus the two new methods given in this paper.

5. An application: the closest known 5×5 hidden forest

We employ a combination of the techniques from both strings of strongly composite
integers and an optimal quasiprime matrix to ﬁnd the closest known 5×5 hidden
forest to date. We ﬁrst calculate a length-5 analogue of the Project Euler Problem 47
(recall the footnote given in Remark 3.11). By slightly altering Minase’s solution
(see Section 4B), we ﬁnd the smallest set of ﬁve consecutive integers each with at
least ﬁve prime factors. Mathematica completed this computation in 36 minutes.
These ﬁve integers and their prime factorizations are

x1 = 129,963,314 = 2 · 13 · 37 · 53 · 2549,

x2 = 129,963,315 = 3 · 5 · 31 · 269 · 1039,

x3 = 129,963,316 = 22 · 7 · 97 · 109 · 439,

x4 = 129,963,317 = 11
2 · 17 · 23 · 41 · 67,

x5 = 129,963,318 = 2 · 3 · 89 · 199 · 1223.

In Example 4.8, it took the Java code only 2 minutes to ﬁnd the smallest four
consecutive values which are each not relatively prime to the four values 134,043
through 134,046. However in this n = 5 case, it is not as simple. After the Java
code ran continuously for four days,5 it had checked up to the y-value of 500 billion
and still did not ﬁnd an H 5
(x,y) with the x-values x1, . . . , x5 given earlier. So we
approached this problem from a more theoretical perspective instead.
Consider the list of ﬁve consecutive integers x1, . . . , x5. Observe that x1, x3,
and x5 are divisible by 2 and that x2 and x5 are divisible by 3. Hence a hidden 5×5
forest bearing these x-values would be “optimal” if the corresponding ﬁve y-values
(which we denote y1, . . . , y5) have the property that y1, y3, and y5 are divisible by 2
and that y2 and y5 are divisible by 3. The beneﬁt of this optimal situation is that
12 of the 25 coordinates will automatically have gcd(xi , y j ) > 1 and hence these
12 points are hidden. In the following matrices, we represent each of these 12 points
with the symbol • in the gcd-matrix GcdM on the left, and to its right we give the
90◦ clockwise rotation matrix M from which we construct a quasiprime matrix:

5Recall the footnote regarding computation times in Example 4.8.

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 305

GcdM =
 y5 →
y4 →
y3 →
y2 →
y1 →
 






 • • • d5 •
a2 b3 c2 d4 e1
• b2 • d3 •
a1 • c1 d2 •

• b1 • d1 •
 







↑ ↑ ↑ ↑ ↑
x1 x2 x3 x4 x5
 ⟳
90◦ right↦−−−−→ M =
 y1 y2 y3 y4 y5
↓ ↓ ↓ ↓ ↓
x1 →
x2 →
x3 →
x4 →
x5 →
 










 • a1 • a2 •
b1 • b2 b3 •

• c1 • c3 •
d1 d2 d3 d4 d5
• • • e1 •
 











Since we know that x5 and y5 are both divisible by 2 and 3 in this optimal case,
we place a 6 in this entry, and the QPM matrix has the abstract form

QPM =
 






 1 a1 1 a2 1
b1 1 b2 b3 1
1 c1 1 c2 1
d1 d2 d3 d4 d5
1 1 1 e1 6
 





 , (3)

where

x1 = 2 · 13 · 37 · 53 · 2549 =⇒ a1, a2 ∈ {13, 37, 53, 2549},

x2 = 3 · 5 · 31 · 269 · 1039 =⇒ b1, b2, b3 ∈ {5, 31, 269, 1039},

x3 = 22 · 7 · 97 · 109 · 439 =⇒ c1, c2 ∈ {7, 97, 109, 439},

x4 = 11
2 · 17 · 23 · 41 · 67 =⇒ d1, d2, d3, d4, d5 ∈ {11, 17, 23, 41, 67},

x5 = 2 · 3 · 89 · 199 · 1223 =⇒ e1 ∈ {89, 199, 1223}.

Observation 5.1. Consider the QPM matrix in (3). Then the following hold:

(1) There are 1,244,160 distinct ways to produce a quasiprime matrix QPM.

(2) Applying the CRT-algorithm to any of the QPM yields the same solution values
x1, . . . , x5 as the x-values of the hidden forest H 5
(x1,y1). In particular, this
unique x1-value is 129,963,314.

(3) The y-value solutions have the property that y1, y3, y5 ∈ 2Z and y2, y5 ∈ 3Z.

Proof. (1) There are P(4, 2) = 4!/(4 − 2)! = 12 possible 2-permutations of a
4-element set. So since a1 and a2 must be distinct elements of {13, 37, 53, 2549},
the ordered tuple (ai )
2
i=1 can be chosen in 12 ways. Applying a similar argument
to count the possible (bi )3
i=1, (ci )
2
i=1, (di )
5
i=1, and the (e1), we see that the ordered
tuple (bi )
3
i=1 can be chosen in 12 ways, the (ci )
2
i=1 in 12 ways, the (di )
5
i=1 in 120
ways, and (e1) in 3 ways. Thus there are 1,244,160 distinct ways to produce a
quasiprime matrix QPM, which proves (1).

306 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

(2) Unfortunately, we only proved this by computational exhaustion using Mathe-
matica. See part (a) of Question 1.

(3) Consider an arbitrary QPM. Suppose y0 is a solution to the ﬁve linear congru-
ences y + k ≡ 0 (mod Ck), where Ck equals the product of the column entries of
QPM for 1 ≤ k ≤ 5. Setting yk = y0 + k, we observe that y5 ≡ 0 (mod 6 · d5), and
thus y5 ≡ 0 (mod 2) and y5 ≡ 0 (mod 3). Hence y5 ∈ 2Z ∩ 3Z. Since y5 ∈ 2Z, it
follows that y3 = y5 −2 implies y3 ∈ 2Z, and y1 = y5 −4 implies y1 ∈ 2Z. Moreover
since y5 ∈ 3Z, it follows that y2 = y5 − 3 implies y2 ∈ 3Z. Thus (3) holds. □

We wrote a program in Mathematica which applies the CRT-algorithm to each
of the possible 1,244,160 matrices. Four minutes later, the program yields that the
smallest y-value solution is given by the quasiprime matrix

QPM =
 






 1 37 1 13 1
31 1 5 269 1
1 109 1 7 1
67 17 41 23 11
1 1 1 89 6
 





 . (4)

This y-value and the next four consecutive integers have the following prime
factorizations (with commas omitted in the factorizations for readability):

y1 = 2,546,641,254,872,348 = 2
2 · 31 · 67 · 461 · 664921471,

y2 = 2,546,641,254,872,349 = 3
2 · 17 · 37 · 109 · 8681 · 475421,

y3 = 2,546,641,254,872,350 = 2 · 52 · 41 · 11113 · 111784759,

y4 = 2,546,641,254,872,351 = 7
2 · 13 · 23 · 73 · 89 · 269 · 271 · 367,

y5 = 2,546,641,254,872,352 = 2
5 · 3 · 11 · 2411592097417.

Comparing the x1, . . . , x5 with the y1, . . . , y5 we see that gcd(xi , y j ) > 1 for all
indices 1 ≤ i, j ≤ 5 and in fact H 5
(x1,y1) has the following gcd-matrix GcdM and
corresponding matrix M:

GcdM =
 






 2 3 22 11 2·3
13 269 7 23 89
2 5 2 41 2
37 3 109 17 3
2 31 22 67 2
 





 ⟳
90◦ right↦−−−−→ M =
 






 2 37 2 13 2
31 3 5 269 3
22 109 2 7 22

67 17 41 23 11
2 3 2 89 2·3







 .

Remark 5.2. If we apply the QP-algorithm to the M above, then we are forced
to place a 22 in either the (3, 1)- or (3, 5)-entry of QPM, and consequently the 6
in the (5, 5) entry becomes a 3. Hence this new QPM differs from the quasiprime
matrix in (4). However, applying the CRT-algorithm to this new QPM gives the
same hidden forest as expected.

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 307

Remark 5.3. The forest H 5
(x,y) with

x = 129,963,314, y = 2,546,641,254,872,348

is at a distance d ≈ 2.54664×1015 from the origin. Using the only known method
until now (that is, Theorem 3.4), we get a forest H 5
(x,y) with

x = 251,080,644,933,696,940,130,615,676,720,763,950,

y = 108,580,359,501,475,197,963,484,708,875,960,338.

This forest is at a distance d ≈ 2.73553×1035 from the origin, and hence is
1.07417×1020 times farther than the forest we reveal in this paper! We have
not found a computationally tractable method to ﬁnd the closest 5×5 hidden forest,
nor do we believe that anyone else has. So for the time being, the H 5
(x,y) we present
in this paper is the closest 5×5 hidden forest to date.

6. Open problems

There are many avenues for further research motivated from the work in this present
paper. In this section, we give some open problems identiﬁed during our research
process.

Question 1. Is it true that for every hidden forest H n
(x,y), there exists a quasiprime
matrix QPM in Matn(Z) such that the CRT-algorithm applied to QPM yields H n
(x,y)?
Related to this question are the following subquestions:

(a) Why do all 1,244,160 distinct quasiprime matrices in matrix (3) yield exactly
the same x-value solution under the CRT-algorithm?

(b) Do all distinct quasiprime matrices produce unique solutions?

(c) Can one code a computationally efﬁcient method to search for the closest
H n
(x,y) for n ≥ 4?

Question 2. Higher-dimensional analogues of patches of invisible points can be
found. Observe that our proof of Proposition 2.4 can easily be extended to higher
dimensions by setting the value s (in the proof) to the appropriate dimension. That
is, the probability that (x1, x2, . . . , xs) is visible in Zs is 1/ζ (s). In Example 6.1, we
ﬁnd a hidden 2×2×2 forest using a 3-dimensional analogue of the CRT-algorithm,
and we see that the forest found by this method is very far from the origin. Can
we generalize the quasiprime matrix to these higher-dimensional settings and ﬁnd
closer hidden n-dimensional forests?

Example 6.1. In Figure 6, we give an example of a hidden 2×2×2 forest with
corner point (x1, y1, z1) at x1 = 9,126,194, y1 = 8,286,564, and z1 = 8,822,099.

308 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

(x2, y1, z2) (x2, y2, z2)

(x2, y1, z1) (x2, y2, z1)

(x1, y1, z2) (x1, y2, z2)

(x1, y1, z1) (x1, y2, z1)

Figure 6. A 2×2×2 hidden forest.

To ﬁnd this 3-dimensional hidden forest, we considered a 3-dimensional version
of the prime matrix as a cube whose corners contain the ﬁrst eight prime numbers.
Then to each face of the cube, we multiplied the four numbers in each corner as the
following image illustrates:

2 7

11 19

1713

3 5 3
 2

13
 11
 17
 19

7

5
 2 7

19

5

1713

3
 11

11
 11

front

back
 left right top

bottom

Solving the three systems of congruences
{x+1 ≡ 0 (mod back),
x+2 ≡ 0 (mod front),
 {y+1 ≡ 0 (mod left),
y+2 ≡ 0 (mod right),
 {z+1 ≡ 0 (mod bottom),
z+2 ≡ 0 (mod top)

yields the three simultaneous solutions x0 = 9,126,193, y0 = 8,286,563, and
z0 = 8,822,098. Then the following values x1, y1, z1, x2, y2, and z2 have the prime
factorizations

x1 = 2 · 7 · 11 · 19 · 3119, y1 = 22 · 3 · 11
2 · 13 · 439, z1 = 11 · 13 · 17 · 19 · 191,

x2 = 3 · 5 · 13 · 17 · 2753, y2 = 5 · 7 · 17 · 19 · 733, z2 = 2
2 · 3 · 5
2 · 7 · 4201.

It is readily veriﬁed from these factorizations that each of the eight tuples of
coordinates (xi , y j , zk) for 1 ≤ i, j, k ≤ 2 have the property gcd(xi , y j , zk) > 1.
Hence this 3-dimensional forest is indeed hidden from the origin.

Question 3. What can be said about hidden forests in the Z[i]×Z[i] lattice? What
is meant by the coordinate values (x, y) ∈ Z[i]×Z[i] being relatively prime? Recall
that if R is a Euclidean domain (as is the case for the ring Z[i] of Gaussian integers),
then greatest common divisors can be computed using the Euclidean algorithm. Can
we apply methods in this paper to the visibility of points in the lattice Z[i]×Z[i]?

NEW METHODS TO FIND PATCHES OF INVISIBLE INTEGER LATTICE POINTS 309

Question 4. Recently, the notion of lattice-point visibility was generalized to
include all curves through the origin given by power functions of the form f (x) =
ax b, where a ∈ Q and b ∈ N, by Goins, Harris, Kubik, and Mbirika [Goins et al.
2018]. In this generalized setting, forests invisible from the origin are called
b-invisible forests. Can we apply the techniques detailed in Section 4 to ﬁnd the
closest b-invisible n×n forests?

Acknowledgments

We thank Stephan Garcia of Pomona College who introduced Mbirika to the concept
of these hidden forests at the AIM-NSF research workshop, REUF4, at ICERM
in June 2012. We also thank the Ofﬁce of Research and Sponsored Programs at
the University of Wisconsin-Eau Claire (UWEC) who funded this project from
Fall 2013 through Summer 2014. We gratefully thank Zane Toman who helped us
with his Java coding guidance in 2014. Moreover, we are indebted to Mbirika’s
current research student Lily Leith who updated the Java code in 2021 to the user-
friendly version found in the online supplement. Lastly, we appreciate the use of the
computing resources of the Blugold Supercomputing Cluster of UWEC. Without
access to its unending hard work and processing power, the immense calculations
that we needed probably would not have been possible to complete within our
lifetime.
 References

[Baake and Grimm 2013] M. Baake and U. Grimm, Aperiodic order, vol. 1: A mathematical invitation,
Encyclopedia of Mathematics and its Applications 149, Cambridge University Press, 2013. MR Zbl

[Brass et al. 2005] P. Brass, W. Moser, and J. Pach, Research problems in discrete geometry, Springer,
2005. MR Zbl

[Cesàro 1881] E. Cesàro, “Question proposée 75”, Mathesis 1 (1881), 184.

[Cesàro 1883] E. Cesàro, “Question 75 (solution)”, Mathesis 3 (1883), 224–225.

[Cesàro 1884] E. Cesàro, “Probabilité de certains faits arithméthiques”, Mathesis 4 (1884), 50–151.

[Chapman 2003] R. Chapman, “Evaluating ζ (2)”, preprint, 2003, http://empslocal.ex.ac.uk/
people/staﬀ/rjchapma/etc/zeta2.pdf.

[Dirichlet 1849] P. G. L. Dirichlet, “Über die Bestimmung der mittleren Werte in der Zahlentheorie”,
Abhandl. Kgl. Preuss. Akad. Wiss. Berlin 1849 (1849), 63–83.

[Goins et al. 2018] E. H. Goins, P. E. Harris, B. Kubik, and A. Mbirika, “Lattice point visibility on
generalized lines of sight”, Amer. Math. Monthly 125:7 (2018), 593–601. MR Zbl

[Herzog and Stewart 1971] F. Herzog and B. M. Stewart, “Patterns of visible and nonvisible lattice
points”, Amer. Math. Monthly 78 (1971), 487–496. MR Zbl

[Lehmer 1900] D. N. Lehmer, “Asymptotic Evaluation of Certain Totient Sums”, Amer. J. Math. 22:4
(1900), 293–335. MR Zbl

[Moreno 2015] S. G. Moreno, “A one-sentence and truly elementary proof of the basel problem”,
preprint, 2015. arXiv

310 AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN

[Pighizzini and Shallit 2002] G. Pighizzini and J. Shallit, “Unary language operations, state com-
plexity and Jacobsthal’s function”, Internat. J. Found. Comput. Sci. 13:1 (2002), 145–159. MR
Zbl

[Schumer 1990] P. Schumer, “Strings of strongly composite integers and invisible lattice points”,
College Math. J. 21:1 (1990), 37–40. MR Zbl

[Somers 2011] J. Somers, “How I failed, failed, and ﬁnally succeeded at learning how to code”, The
Atlantic (June 3 2011).

[Sylvester 1883] J. Sylvester, “Sur le nombre de fractions ordinaires inégales qu’on peut exprimer en
se servant de chiffres qui n’excède pas un nombre donné”, C. R. Acad. Sci. Paris 96 (1883), 409–413.
Zbl

[Weisstein] E. W. Weisstein, “Visible point”, http://mathworld.wolfram.com/VisiblePoint.html.
From MathWorld.

Received: 2020-07-27 Revised: 2020-11-14 Accepted: 2020-11-14

awgoodie@gmail.com University of Wisconsin, Eau Claire, WI, United States

mbirika@uwec.edu Department of Mathematics, University of Wisconsin,
Eau Claire, WI, United States

jasminemlnielsen@gmail.com University of Wisconsin, Eau Claire, WI, United States

mathematical sciences publishers msp

involve
msp.org/involve

INVOLVE YOUR STUDENTS IN RESEARCH
Involve showcases and encourages high-quality mathematical research involving students from all
academic levels. The editorial board consists of mathematical scientists committed to nurturing
student participation in research. Bridging the gap between the extremes of purely undergraduate
research journals and mainstream research journals, Involve provides a venue to mathematicians
wishing to encourage the creative involvement of students.

MANAGING EDITOR
Kenneth S. Berenhaut Wake Forest University, USA

BOARD OF EDITORS

Colin Adams Williams College, USA
Arthur T. Benjamin Harvey Mudd College, USA
Martin Bohner Missouri U of Science and Technology, USA
Amarjit S. Budhiraja U of N Carolina, Chapel Hill, USA
Pietro Cerone La Trobe University, Australia
Scott Chapman Sam Houston State University, USA
Joshua N. Cooper University of South Carolina, USA
Jem N. Corcoran University of Colorado, USA
Toka Diagana University of Alabama in Huntsville, USA
Michael Dorff Brigham Young University, USA
Sever S. Dragomir Victoria University, Australia
Joel Foisy SUNY Potsdam, USA
Errin W. Fulp Wake Forest University, USA
Joseph Gallian University of Minnesota Duluth, USA
Stephan R. Garcia Pomona College, USA
Anant Godbole East Tennessee State University, USA
Ron Gould Emory University, USA
Sat Gupta U of North Carolina, Greensboro, USA
Jim Haglund University of Pennsylvania, USA
Johnny Henderson Baylor University, USA
Glenn H. Hurlbert Virginia Commonwealth University, USA
Charles R. Johnson College of William and Mary, USA
K. B. Kulasekera Clemson University, USA
Gerry Ladas University of Rhode Island, USA
David Larson Texas A&M University, USA
Suzanne Lenhart University of Tennessee, USA
Chi-Kwong Li College of William and Mary, USA
 Robert B. Lund Clemson University, USA
Gaven J. Martin Massey University, New Zealand
Mary Meyer Colorado State University, USA
Frank Morgan Williams College, USA
Mohammad Sal Moslehian Ferdowsi University of Mashhad, Iran
Zuhair Nashed University of Central Florida, USA
Ken Ono Univ. of Virginia, Charlottesville
Yuval Peres Microsoft Research, USA
Y.-F. S. Pétermann Université de Genève, Switzerland
Jonathon Peterson Purdue University, USA
Robert J. Plemmons Wake Forest University, USA
Carl B. Pomerance Dartmouth College, USA
Vadim Ponomarenko San Diego State University, USA
Bjorn Poonen UC Berkeley, USA
Józeph H. Przytycki George Washington University, USA
Richard Rebarber University of Nebraska, USA
Robert W. Robinson University of Georgia, USA
Javier Rojo Oregon State University, USA
Filip Saidak U of North Carolina, Greensboro, USA
Hari Mohan Srivastava University of Victoria, Canada
Andrew J. Sterge Honorary Editor
Ann Trenk Wellesley College, USA
Ravi Vakil Stanford University, USA
Antonia Vecchio Consiglio Nazionale delle Ricerche, Italy
John C. Wierman Johns Hopkins University, USA
Michael E. Zieve University of Michigan, USA

PRODUCTION
Silvio Levy, Scientiﬁc Editor
 Cover: Alex Scorpan

See inside back cover or msp.org/involve for submission instructions. The subscription price for 2021 is US $205/year for the electronic
version, and $275/year (+$35, if shipping outside the US) for print and electronic. Subscriptions, requests for back issues and changes of
subscriber address should be sent to MSP.

Involve (ISSN 1944-4184 electronic, 1944-4176 printed) at Mathematical Sciences Publishers, 798 Evans Hall #3840, c/o University of
California, Berkeley, CA 94720-3840, is published continuously online. Periodical rate postage paid at Berkeley, CA 94704, and additional
mailing ofﬁces.
 Involve peer review and production are managed by EditFLOW® from Mathematical Sciences Publishers.

PUBLISHED BY
mathematical sciences publishers
nonproﬁt scientiﬁc publishing
http://msp.org/
© 2021 Mathematical Sciences Publishers
 inv lve

a journal of mathematics

involve

2021 vol. 14 no. 2
 181Some remarks on generalized recursive polynomials
LUKE WILJANEN AND AKLILU ZELEKE 195When winning sets have full dimension
PEDRO BIRINDIBA AND KATRIN GELFERT 209Wave-packet propagation in a ﬁnite topological insulator and the
spectral localizer index
JONATHAN MICHALA, ALEXANDER PIERSON, TERRY A.
LORING AND ALEXANDER B. WATSON 241The mathematics of tie knots
ELIZABETH DENNE, CORINNE JOIREMAN AND ALLISON
YOUNG 271Zeros of complex random polynomials spanned by Bergman
polynomials
MARIANELA LANDI, KAYLA JOHNSON, GARRETT
MOSELEY AND AARON YEAGER 283New methods to ﬁnd patches of invisible integer lattice points
AUSTIN GOODRICH, ABA MBIRIKA AND JASMINE NIELSEN 311Properties of certain sparse circulant determinants
DUSTY E. GRUNDMEIER AND SAMUEL M. KIM 327On cyclic and nontransitive probabilities
PAVLE VUKSANOVIC AND A. J. HILDEBRAND 349Two families of hypercyclic nonconvolution operators
ALEXANDER MYERS, MUHAMMADYUSUF ODINAEV AND
DAVID WALMSLEYinvolve2021vol.14,no.2
