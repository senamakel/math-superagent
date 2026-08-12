<!-- source: http://multimagie.com/Search.pdf | converted from PDF -->

A search for 3x3 magic squares having more than six
square integers among their nine distinct integers.
Draft v2, By Christian Boyer, France, September 16th 2004
cboyer@club-internet.fr
www.multimagie.com/indexengl.htm
  “Martin  LaBar,  in  The  College  Mathematics  Journal
[January 1984, p.69], asked if a 3x3 magic square exists with
nine distinct square numbers. (…) Neither such a square nor
a proof of impossibility has been found. (…) I here offer $100
to  the  first  person  to  construct  such  a  square.  If  it  exists,  its
numbers are sure to be monstrously large.”
Martin Gardner, 1996

Today,  eight  years  after  this  quotation,  nobody  has  succeeded  in  winning  the  $100  of  this
Gardner’s challenge.
However, it is possible to construct a 3x3 square with nine square integers and only one bad
magic sum. The smallest example is the following square, first found independently by Lee
Sallows  and  Michael  Schweitzer.  All  the  rows  and  columns,  but  only  one  of  the  two
diagonals, have the same magic sum.

127²  46²  58²
2²  113²  94²
74²  82²  97²
(fig. 1)

Our problem, here, is to get the maximum number of square integers in a fully magic square:
the eight lines of the squares of our study will always have the same magic sum.

Six square integers
Andrew  Bremner,  Department  of  Mathematics,  Arizona  State  University,  demonstrated  in
2001  that  all  the  sixteen  possible  configurations  of  magic  squares  including  six  square
integers are possible.

x  x  x       x  x    x  x  x       x                     x             x       x  x
x  x       x     x               x  x  x    x  x  x    x  x  x    x  x  x       x  x
x          x  x       x  x  x    x     x    x  x  x    x  x       x     x    x     x
6.I    6.II    6.III    6.IV    6.V    6.VI    6.VII    6.VIII

      x          x          x       x          x  x    x     x       x  x    x     x
x     x    x  x  x    x  x  x    x     x    x  x          x  x    x                x
x  x  x       x  x    x  x       x  x  x    x     x    x     x    x  x  x    x  x  x
6.IX    6.X    6.XI    6.XII    6.XIII    6.XIV    6.XV    6.XVI
 (fig. 2)

 - A search for 3x3 magic squares having more than six square integers, by Christian Boyer, © 2004, page 2/5 -

Numerous  examples  with  six  square  integers  are  easy  to  find,  for  each  configuration.  For
example,  here  is  the  “smallest”  possible  magic  square  with  six  square  integers,  “smallest”
meaning  that  it  is  using  the  smallest  magic  sum.  This  example  belongs  to  the  Bremner’s
configuration 6.XV. The central cell is equal to 145 = 5·29
  265  1²  13²
7²  145  241
11²  17²  5²
(fig. 3)

Here are the two smallest examples using a square integer in the central cell. These examples
belong  to  the  configurations  6.VII  and  6.XIV.  There  is  an  easy  correspondence  between
squares of these two configurations, as mentioned by Bremner: that’s why these two different
squares are in fact very similar, using the same square integers, having one identical diagonal.
  889  697  17²    5²  1561  17²
5²  25²  35²    889  25²  19²
31²  553  19²    31²  -311  35²
(fig. 4)

And when two magic squares 3x3 have the same central cell, then they have the same magic
sum. The magic sum of a magic square 3x3 always equals three times the central cell.

Seven square integers
Up to symmetry (rotation and reflection), there are eight ways of selecting seven entries from
a 3x3 square. These are as follows:

x  x  x    x  x  x    x  x  x    x  x  x    x  x  x    x  x       x  x  x    x  x  x
   x       x  x       x  x  x       x  x    x  x  x    x  x  x    x     x    x     x
x  x  x    x     x    x          x  x          x          x  x    x     x    x  x
7.I    7.II    7.III    7.IV    7.V    7.VI    7.VII    7.VIII
(fig. 5)

Two results are already known about these configurations:
•  Duncan Buell, Department of Computer Science and Engineering, University of South
Carolina, studied in 1998 the configuration 7.I, that he called the “magic hourglass”,
and  computed  that  there  is  no  solution  with  a  central  cell  <  25·1024.  A  direct
consequence:  if  a  magic  square  of  squares  exists,  then  its  central  cell  is  bigger  than
25·1024. Martin Gardner was right saying that ”if it exists, its numbers are sure to be
monstrously large.”
•  Lee  Sallows  and  Andrew  Bremner  had  separately  and  previously  found  the  only
known example having seven square integers, excluding its symmetries, rotations and
k² multiples. This example is of configuration 7.IV. The central cell is equal to 425² =
(5²·17)² = 180,625.
  373²  289²  565²
360721  425²  23²
205²  527²  222121
(fig. 6)

- A search for 3x3 magic squares having more than six square integers, by Christian Boyer, © 2004, page 3/5 -

The goal of our study is to try to find at least another example with seven square integers.

Of course excluding rotations, symmetries, or k² multiples of the figure 6.

Eight square integers
Up to symmetry (rotation and reflection), there are three ways of selecting eight entries from a
3x3 square. These are as follows:

x  x  x    x  x  x    x  x  x
x  x  x    x  x  x    x     x
x     x    x  x       x  x  x
8.I    8.II    8.III
(fig. 7)

Currently, no example with eight square integers is known (and no example with nine square
integers, Martin Gardner’s initial challenge).
Some words about the method used

A line going through the central cell C, and having two square integers around the central cell,
is an integer solution of the equation:  x² + y² = 2C.
Because  4k+3  prime  integers  cannot  be  sums  of  two  square  integers,  we  study  only  magic
squares  with  central  cells  which  are  products  of  4k+1  prime  integers.  All  the  7.x  and  8.x
configurations  need  two,  three  or  four  such  lines  through  the  centre,  meaning  at  least  (as  a
strict minimum) two, three or four solutions of the above equation.
Knowing  that  a  4k+1  prime  number  has  only  one  way  to  be  a  sum  of  two  square  numbers,
knowing that the product (a² + b²)(c² + d²) gives two different ways to be a sum of two square
numbers,
•  (ad + bc)² + (ac – bd)²
•  (ad – bc)² + (ac + bd)²
and using the fact that
•  2(a² + b²) = (a + b)² + (a – b)²
it is possible to demonstrate that:
D1.  For  configurations  7.I  to  7.VI,  and  8.I  to  8.II  where  the  central  cell  C  is  a
square C=c².
If c has n distinct factors which are 4k+1 prime integers, then there are:
(3n – 1)/2 different solutions of x² + y² = 2c², with x<y.

D2. For configurations 7.VII, 7.VIII, 8.III where the central cell C is not a square.
If C has n distinct factors which are 4k+1 prime integers, then there are:
2(n-1) different solutions of x² + y² = 2C, with x<y.

Even  if  distinct  factors  give  the  above  maximum  number  of  solutions,  it  is  interesting  for
variety purpose, to allow factors in common in the factorisation of the central cell: the only
known example with 7 squares (fig.6) has one time the factor 17, but twice the factor 5.

 - A search for 3x3 magic squares having more than six square integers, by Christian Boyer, © 2004, page 4/5 -

Research with a square integer in the central cell
We  first  limit  our  study to  magic  squares  having  a  square  integer in  the  central  cell:  all  the
configurations from 7.I to 7.VI, and 8.I, 8.II.
Disappointing  result,  done  by  computer:  the  magic  square  of  Fig  6  is  the  ONLY  magic
square  (excluding  its  rotations,  symmetries,  and  k²  multiples)  with  more  than  six  square
integers, if the central cell is one of the following square integer types:
  a)  (5i·p1·p2)² with 5 ≤ pj < 40,000 (→ central cell < 1.60x1021)
b)  (5i·p1·p2·p3)² with 5 ≤ pj < 1,500 (→ central cell < 6.92x1021)
c)  (5i·p1·p2·p3·p4)² with 5 ≤ pj < 300 (→ central cell < 3.39x1022)
d)  (5i·p1·p2·p3·p4·p5)² with 5 ≤ pj ≤ 101 (→ central cell < 6.90x10
22)
e)  (5i·p1·p2·p3·p4·p5·p6)² with 5 ≤ pj ≤ 53 (→ central cell < 3.07x1023)
f)  (5i·p1·p2·p3·p4·p5·p6·p7)² with 5 ≤ pj ≤ 37 (→ central cell < 5.63x1024)
g)  (5i·p1·p2·p3·p4·p5·p6·p7·p8)² with 5 ≤ pj ≤ 29 (→ central cell < 1.56x1026)
h)  (5i·p1·p2·p3·p4·p5·p6·p7·p8·p9·p10)² with 5 ≤ pj ≤ 17 (→ central cell < 2.54x10
27)
i)  (5i·p1·p2·p3)² with
5 ≤ p1 ≤ 101
5 ≤ p2 < 1,000
5 ≤ p3 < 10,000 (→ central cell < 6.30x1020)
j)  (5i·p1·p2·p3·p4)² with
5 ≤ p1 ≤ 101
5 ≤ p2 < 150
5 ≤ p3 < 300
5 ≤ p4 < 1,000 (→ central cell < 1.21x1022)
k)  (5i·13·17·29·37·p5·p6)² with
5 ≤ p5 ≤ 41
5 ≤ p6 < 1,000 (→ central cell < 5.87x1022)
l)  (5i0·(p1)i1·(p2)i2·(p3)i3)² with 5 ≤ pj < 200 (→ central cell < 2.14x1030)
m)  (p1·p2·p3)² with 5 ≤ pj < 3,000 (→ central cell < 6.85x1020)

0 ≤ i ≤ 2, and pj being a 4k+1 prime number {5, 13, 17, 29, 37, 41, 53, …}

From a) to k), I have in fact analyzed only (5²·p1· …)². And for l), only (5²·p1²·p2²·p3²)².
Because a magic square with x square entries keeps its x square entries when all the cells are
multiplied by the same square factor, our results includes automatically all the submultiples of
the square root of the central cell: if there is no magic square with central cells (5²·p1· …)²,
then  there  is  also  no  magic  square  with  central  cells  (5·p1·  …)²  and  (p1·  …)²  in  the  studied
intervals. And also, for example, the type a) includes automatically the simplest case (5i·p1)².

Research with a non-square integer in the central cell
We  now  study  the  magic  squares  that  do  not  have  a  square  integer  in  the  central  cell:
configurations 7.VII, 7.VIII, and 8.III.
Again a disappointing result, done by computer: there is NO magic square with more than
six square integers, if the central cell is one of the following integer types:
  n)  (5i·p1) with 5 ≤ pj < 40,000 (→ central cell < 1.25x108)
o)  (5i·p1·p2) with 5 ≤ pj < 40,000 (→ central cell < 5x1012)
p)  (5i·p1·p2·p3) with 5 ≤ pj < 4,000 (→ central cell < 1.98x1014)
q)  (5i·p1·p2·p3·p4) with 5 ≤ pj < 800 (→ central cell < 1.26x1015)

- A search for 3x3 magic squares having more than six square integers, by Christian Boyer, © 2004, page 5/5 -

 r)  (5i·p1·p2·p3·p4·p5) with 5 ≤ pj < 300 (→ central cell < 6.75x10
15)
s)  (5i·p1·p2·p3·p4·p5·p6) with 5 ≤ pj < 150 (→ central cell < 3.42x1016)
t)  (5i·p1·p2·p3·p4·p5·p6·p7) with 5 ≤ pj ≤ 101 (→ central cell < 3.35x1017)
u)  (5i·p1·p2·p3) with
5 ≤ p1 < 150
5 ≤ p2 < 1,500
5 ≤ p3 < 15,000 (→ central cell < 1.04x1013)
v)  (5i·p1·p2·p3·p4) with
5 ≤ p1 < 150
5 ≤ p2 < 250
5 ≤ p3 < 500
5 ≤ p4 < 1,500 (→ central cell < 7.72x1013)
w)  (5i·13·17·29·37·p5·p6) with
5 ≤ p5 ≤ 101
5 ≤ p6 < 1,500 (→ central cell < 1.12x1014)
x)  (p1·p2·p3) with 5 ≤ pj < 15,000 (→ central cell < 3.35 x1012)

0 ≤ i ≤ 5, and pj being a 4k+1 prime number {5, 13, 17, 29, 37, 41, 53, …}

I have in fact analyzed only (54·p1· …) and (55·p1· …) integers.
About  (54·p1·  …):  because  the  square  properties  of  a  magic  square  are  not  modified  by  a
square factor like 5², if there is no magic square with central cell (54·p1· …), then there is also
no magic square with central cells (5²·p1· …) and (p1· …) in the studied intervals.
About  (55·p1·  …):  because  the  square  properties  of  a  magic  square  are  not  modified  by  a
square factor like 5², if there is no magic square with central cell (55·p1· …), then there is also
no magic square with central cells (5
3·p1· …) and (5·p1· …) in the studied intervals.

Conclusion

Fig 6 shows, by the example, that it is possible to get seven square entries in a magic square.
It  is  very  strange  (and  really  disappointing…)  to  have  been  unable  to  find  at  least  another
example of such a square in our various and wide range of central cells.
It is so difficult to find at least another example with “only” seven squares that I think that a
complete  square  of  squares  -with  nine  square  integers-  cannot  exist.  But  it’s  only  a  feeling,
the eventual proof of the impossibility has not yet been found…

References

Christian Boyer, Some notes on the magic squares of squares problem, article in preparation
Andrew Bremner, On squares of squares, Acta Arithmetica 88 (1999), pp. 289-297
Andrew Bremner, On squares of squares II, Acta Arithmetica 99 (2001), pp. 289-308
Duncan Buell, A search for a magic hourglass (1999), preprint
Martin Gardner, The magic of 3x3, Quantum, vol 6 n3 (Jan.-Feb. 1996), pp. 24-26
Martin Gardner, The latest magic, Quantum, vol 6 n4 (March-April 1996), p. 60
Richard  Guy  and  Richard  Nowakowski,  Monthly  unsolved  problems  1969-1997,  American
Math. Monthly 104 (1997), pp. 969-973
Richard  Guy,  Problem  D15  –  Numbers  whose  sums  in  pairs  make  squares,  Unsolved
problems in number theory, third edition, Springer-Verlag, New York (2004), pp. 268-
271
