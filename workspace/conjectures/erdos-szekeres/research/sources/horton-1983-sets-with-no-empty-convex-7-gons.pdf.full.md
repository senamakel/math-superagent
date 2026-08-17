<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E7C17D71D9FA4A08B265441FBEB32D7/S0008439500065176a.pdf/sets-with-no-empty-convex-7-gons.pdf | converted from PDF -->

Canad. Math. Bull. Vol. 26 (4), 1983

SETS WITH NO EMPTY CONVEX 7-GONS

BY
J. D . HORTON *

ABSTRACT. Erdôs has defined g(n) as the smallest integer such
that any set of g(n) points in the plane, no three collinear, contains
the vertex set of a convex rc-gon whose interior contains no point of
this set. Arbitrarily large sets containing no empty convex 7-gon are
constructed, showing that g(rc) does not exist for n>l. Whether
g(6) exists is unknown.

Esther Klein raised the following combinatorial geometry problem [5]. For
n >3 , let f(n) be the smallest integer such that for any set of f(n) points in the
plane, no three collinear, contains the vertex set of a convex n-gon. Determine
f(n). It is easy to show that /(3)-= 3 and /(4) = 5. That /(5) = 9 was proved in

/2H-4 \
[4]. Erdôs and Szekeres [1], [2] determined that 2 n~ 2+ 1 </(n ) < „ + 1.
\ n — 2 J
Erdôs has raised a similar question. For n >3 , define g(n) to be the smallest
integer such that any set of g(n) points in the plane, no three collinear,
contains the vertex set of a convex n-gon whose interior contains no point of
the set. We call a n-gon, with no points of the set in its interior, empty. Again,
g(3) = 3 and g(4) = 5. Harborth [3] has proved that g(5) = 10. However, it is
not known whether g(6) exists. The main result of this note is that g(7), and
hence g(n) for all M>7 , does not exist.
We construct, for any k, a set of 2
k points with no empty convex 7-gon. Let
d\Ci2 ' ' '
 ak be the binary expansion of the integer i, 0<i<2
k. Note that
leading O's are not omitted. Let c — 2
k + 1, and define d(i) = X djC1 \ summing
from / = 1 to / = k. Let pt be the point (i, d(i)), and define Sk to be the set of
points {pi | i = 0, 1, . . ., 2
k - 1}. Observations:
(a) {pt | i <2 k_1 } = the left half of Sk = L.
(b) {pt | i>2 k-l } = the right half of Sk = R, which is a translate of L.
(c) [pt | i is even} = the bottom half of Sk = B.
(d) {pi ! i is odd} = the top half of Sk = T, which is a translate of B.
(e) L, R, B, and T are all scaled translates of each other. For example,
halving the first coordinate while multiplying the second coordinate by c,
takes B onto L.
(f) The 180° rotation of the plane about ((2k - l)/2, X c
l/2) takes T onto B.

Received by the editors August 31, 1982 and, in revised form, December 3, 1982.
* Research financially supported by NSERC grant no. A5376.
1980 Mathematics Subject Classification: 52A40.
Keywords: Combinatorial geometry, convex polygon.
©Canadian Mathematical Society 1983.  482

https://doi.org/10.4153/CMB-1983-077-8 Published online by Cambridge University Press

SETS WITH NO EMPTY CONVEX 7-GONS  483

(g) All points of T are above any line joining two points of B. The value of c
was chosen large enough to make this true. Similarly, all points of B are
below any line joining two points of T.
(h) If i and j both have the same last x digits in their binary expansions, and
h has a different sequence of x rightmost digits, then whether ph is above
or below the line joining pt and p] is determined by the sequences of the
last x digits.
Consider any empty convex n-gon A in Sk. We may assume A is contained
entirely in neither T nor B. Otherwise if A is contained in B, apply the linear
transformation that takes B onto L. A will be transformed into an empty
convex n-gon in L. Similarly, if A is contained in T, apply the linear
transformation that takes T onto L. Repeat this procedure until a transformed
image of A meets both T and B.
Next, consider how many points of A can be in B. Assume pt and p] are in
AC\B. By (g) above, no point ph of B with i<h<j, can be above the line
segment joining pt and pJ5 since otherwise no point of T could be in A. As well,
I claim that d(h)<d(i) and d(h)<d(j). Since ph is below the line joining pt
and Pj, clearly one of these statements is true. Assume d(h)<d(i), but
d(h)>d(j). Let x be the position of the right-most digit at which h and i differ
in their binary expansions; let y be the position of the right-most digit at which
h and / differ. In both cases, the number with the larger functional value must
have a 1 in the position, and the other number a 0. If x < y then p] must be
below the line joining pt and ph, by observation (h). But then ph is above the
line joining pt and pJ? a contradiction. Hence we can assume that y <x. In this
case, consider l = j — 2
k'
x. The right-most position in which the binary expan-
sions of J and j differ is x, where / has a 1 and / has a 0. On the other hand, J
and i must agree in the last k — x positions. By observation (h), pj is below the
line joining pt and pb But since j — i > j — h > 2k~y > 2 k" x = / — /, i < I < j. Then
Pi must be both above and below the line joining pt and p]5 a contradiction.
Similarly, d(j)<d(h)<d(i) leads to a contradiction. Therefore d(h)<d(i) and
d(h)<d(j).
If A DJB contained four points i<h<l<j, then d(h)<d(l) and d(l)<d(h).
Hence A H B cannot contain more than three points. By observation (f) above,
A HT cannot contain more than three points either. Hence A has no more
than 6 points.
Whether g(6) exists is still unknown, although the author believes that g(6)
does exist.
I wish to acknowledge D. Avis of McGill University who first mentioned this
problem to me, and with whom I had some interesting discussions.

REFERENCES

1. P. Erdôs and G. Szekeres, A combinatorial problem in geometry, Compositio Math. 2 (1935),
463-470.

https://doi.org/10.4153/CMB-1983-077-8 Published online by Cambridge University Press

484  J. D. HORTON

2. P. Erdôs and G. Szekeres, On some extremum problems in elementary geometry, Ann. Univ.
Sci. Budapest 3-4 (1960-1) 53-62.
3. H. Harborth, Konvexe Funfecke in ebenen Punktmenger, Elem. Math. 33 (1978) 116-118.
4. J. D. Kalbfleisch, J. G. Kalbfleisch, and R. G. Stanton, A combinatorial problem on convex
n-gons, Proc. Louisiana Conf. on Combinatorics Graph Theory, and Computing, Baton Rouge
(1970), 180-188.
5. Wm. Moser, Research Problems in Geometry, McGill University, (1981) #29 .

SCHOOL OF COMPUTER SCIENCE

UNIVERSITY OF NEW BRUNSWICK

FREDERICTON, NEW BRUNSWICK, E3B 5 A3

https://doi.org/10.4153/CMB-1983-077-8 Published online by Cambridge University Press
