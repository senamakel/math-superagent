<!-- source: https://ir.cwi.nl/pub/1721/1721D.pdf | converted from PDF -->

COMBINATORICA  COMBINATORICA 8 (1) (1988) 57-61

Akademiai Kiad6 - Springer-Verlag

A  REMARK  ON  PARTIAL  LINEAR  SPACES  OF
GIRTH  5  WITH  AN  APPLICATION  TO  STRONGLY
REGULAR  GRAPHS

A.  E.  BROUWER  and  A.  NEUMAIER

Received April 10. 1984

We  derive  a  lower bound on  the  number of points of a  partial linear space of girth  5.  As
an application,  certain  strongly  regular graphs  with µ=2  are  ruled out by  observing  that the first
subconstituents are partial linear spaces.

1. Partial linear spaces of girth 5

A partial linear space consists  of a set of points and a  set of lines  (subsets  of
the point set) such that any two lines  have at most one point in  common.  Collinear
points  are  called  adjacent  or  neighbours.  The  girth  of a  partial linear space  is  the
length  of a shortest circuit.
In view  of the  application  to  strongly  regular graphs  we  shall  use  k  for  the
number of points and  A.  for  the valency  (of the pointgraph) of a  partial linear space.

Theorem.  A  connected partial linear space  with girth at least 5 and more  than  one line
(lines possibly  of varying  size)  in  which  every point has  A.  neighbours,  contains  k ~

~}.(..1.+3)/2 points.

Proof.  Let L be a line of size /.  Denote by T the set of points at distance at least two
from  L.  Then  JTl=k-l(A.+2-l),  and  /§:..1.  since  a  line  of size  A.+1  would  be
a  component.  Let  x;  be  the  number  of points  in  T  having  exactly  i  neighbours  at
distance one from L. We have

(i)  Z X1  =  k-/(..1.+2-l),
i

(ii)  Zix1~l(A.+t-l)(t-1),
i

Hence

0  :::§  Z (i-(A.+2-l))2x1  =  2 Z (2i)x1-(2A.+3-21)4' ix1+(A.+2-l)2 Z X1  ~

J.  '  '  '

:::§  l(l- 1)(). + 1-!)2-/{l-1)(..1.+ 1- l)(2..1. + 3-21) +  (..1. +2- l)2(k- l(A.+2-l)),

AMS subject classification (1980):  05 B 30.

58  A.  BROUWER,  A.  NEUMAIER

whence  k(A.+2-1)2 ~l(A.+2-l)((A.+2)(A.+1-/)+ 1)

which can be  written as

k ~ _!_ 2().  3)  (2 + 2)(A.-l)(2/-3-A.)
- 2  +  +  2(A.+2-l)

It follows  that ifthere is a line  of size  l  with  /~0.+3)/2 then  k~d(A.+3)/2 (with
strict inequality unless  1=2  or  l=(A.+3)/2).
If l is  relatively small then we can improve on estimate (ii).  Let m be the size
of the longest line intersecting L. We have

(ii)'  Zixi~l(l+l-1)(2+1-m).
i

Hence, evaluating  0:§2' (i-/)(i-/- l)xi  we  find
i

k ;:;;:  (A.  l)2 -/A.- 2/(m-l)(A.+1-l)
- +  l+l

It follows that if the longest line in our partial linear space has length at most (J,.+ 1)/2
(putting  m:§/:§(}.+ 1)/2)  then  k ~ 0. + 1)(2 +2)/2=A.(A. +3)/2+ 1.
In case  the  longest line  has length  (A.+2)/2,  we  have  to  estimate somewhat
more carefully.  If there is  a  line L  of length  /:§A./2  such that each line  intersecting
L has length at most )./2 then  k~A.2/2+2A.+ I.  This shows  that for smaller k there
are many lines  of size  A./2+1 ;  in fact too many.
Write  IMl=l +sM  for  each  line  M.  Considering  the  lines  M  distinct from
L passing through a  point  xEL  we see  that x is at distance  two from  Z sM(A.-sM)
points  in  T.  But  Z sM=2+1-l,  so  Z sM(A.-sM)=A.(J,.+1-/)-(A.+l-/)2+
+  Z  sMsN~(l-1)(A.+1-l)+(nx-1)(2(A.+1-l)-nx)  where  nx=Z 1  is  the
M>'N  M
number of lines intersecting L  in the point x.
Let  nx = 1  for  j  points of L, so that  nx ~ 2  for  the remaining  /- j  points
of L. Then

(ii)"  Z ix1  ~ /(l-1)(2+1-/) +2(/ -j)(1-l).

In  particular,  for  l=A./2+1  we  find,  evaluating  0-:§Z (i-J)(i-l+I)xi.  that

k  ~ ~ ;.2+2+ 1 + 4(1-21(1-j);

On  the other hand, if for  some  jEN  each line  of size  /=A./2+1  intersects  at least

~ + 1 . others  ~f this  s.ize  th~n considering  j(j + 1)  lines  of size  I intersecting  such
Imes  mte~sectmg a  give~ hne  L  we  find  ITl=k-/2~j(j+l)(/-l)/2=Aj(j+l)/4.
This  shows  that  if the  linear  space  contains  lines  of size  I= Aj2 +I  then

k  ~ max  min{ 2
1 A.2 +3A.-3-j 4/-S  _!_A.j(j+l)+.!.;,,2+A.+1}
O;;>j:;;l  I  '  4  4  .

STRONGLY  REGULAR  GRAPHS  59

Hence,  for  A.=2, 4, 6, 8,  10  we  find  k"§:5, 15, 27, 46, 67  respectively,  and
in  general  putting  j=f Yil  we  find  k>J..() .. +3)/2  for  ).>6.  This  proves  the
theorem.  II

Remark.  Equality  holds  in  the  theorem  iff  J..=2  and  k=5.  (This  partial  linear
space exists -it is a pentagon.) For: if there is a line of sizd./2+ I then k>).(J..+3)/2
unless  A.=2  or  A.=6.  But if  A.=6  and  k=27  one  sees  that  each  line  of size  4
intersects exactly three others and that each point in  Thas three or four  neighbours
at distance one of L  (where  1=4) - hence lines  of size 4 do  not intersect in  T and
ITf "§:18,  k"§:34,  contradiction.
Hence there are no lines  of size  )./2 +I, but each  line of size at most (A.+ 1)/2
intersects a  longer  line,  so  there are  lines  of size  (A.+3)/2  or  )..  In  the  former  case
(l=() .. +3)/2)  wemaysuppose  A.>3.  Weseethat  j=l,  i.e.,eachlineofsize(J..+3)/2
intersects  only  lines  of size  (J..+1)/2.  Let there  be  a  lines  of size  (A+3)/2.  Then
there are  (A.-a)(A.+3)/2  points  not in  one  of these  lines,  and  a(J.-l)(J..+3)/4 in-
cidences of such points with (A.+ 1 )/2-lines. But each point is in at most two (A.+ I )/2-
lines,  so  (J.-a)(A.+3)"§:a(A.-l)(A.+3)/4  and  a:§3.  If  a"§:l  then  we  find  a  line
Lwith  l=(A.+1)/2  intersectingonlyonelineofsize  (A.+3)/2,  i.e., with  j=l.  From

o~z(i-/-1)2x;  onefinds  /;§I,  contradiction.
Hence there are no lines of size  (). +3)/2  and all lines have size 2 or )..
If some  point is  only  in  lines  of size  2 then it has  A.  neighbours  and  ).().-I)
:::ioints  at distance 2 so that  k"§:A.2 +1.  On the other hand, if  A.>2  and each  point
is in a line of size )., then let L  be a line of size A. Each of its .A.  neighbours is  in a line
of length  A.,  and  these  lines  cannot  intersect,  so  ITl"§:A.(A.-1)  and  k"§:A.(A.+1).
This proves our claim.

Remark.  We  do  not  know  the  right  order  of magnitude  of the  lower  bound.  The
Theorem gives  something of order  A.2/2  - on  the  other hand,  the  Moore graphs  of
diameter two are examples with  k=J .. 2+1.  For small A. we  have:

A.=  2,  k  =  5,  the pentagon.

A.  =  3,  k  =  10,  the Petersen graph.

A.=  4,  k =  15:

There is a  unique partial linear space  on  15 points with 10 lines  of size 3 and
girth  5.  Its  point-graph  is  distance  regular  with  parameters  i(4, 2,  1;  l, l, 4).  It is
obtained  from  the  generalised  quadrangle  GQ(2, 2)  by  deleting  a  parallel  class  of
lines. It is  the line graph of the Petersen graph.
Now  these  three examples  are  regular:  all  lines  have  the  same  size.  But  for
regular  partial  linear  spaces  these  same  methods  yield  stronger  bounds:  we  have
k"§:A.(A.-1+2)+1  if all  lines  have  size!. If ).;§/(/-1) this  can  be  strengthened  to

k "§:  12(.A.-21+3)+  /(/~ l)3

(In  case  A.=/(/-1),  equality  would  mean  that we  have  a  strongly  regular  graph
with  µ = 1  and  discriminant  (/-1) ¥5,  hence  equality  occurs  only  for  I= 2.  In
general equality means that we  have a  strongly regular graph withµ= 1 in the first

60  A.  BROUWER,  A.  NEUMAll!R

case and a  distance regular graph  of diameter  at m?st  three .in  the  ~econd case  -
the  linegraph  of a  system  satisfying  one  bound  with  equality,  satisfies  the  o.ther
with equality. This yields very strong conditions on the parameters, and only finitely
many examples are known.)  .  .  .  h
An  infinite  family  of regular  examples  is  provided  by  the  mc1de~ce grap  s
of finite projective planes: they have  k=2(,1.2-.A.+ I),  fc:ir  .A.=q+ 1,  q a  pm~1epo~r.
Concerning  irregular  examples,  there  are  precisely  two  others  with  .?i.-3,
k=lO  namely
 and

For  A.=2,  k=5  and  .A.=4,  k= 15  there  are  no irregular examples.  There  are  no
examples with  .?i.=5,  k=2l.

2.  Strongly regular graphs with  µ = 2

Let G be  a  graph such that two  nonadjacent vertices have at !Ilost two  com-
mon neighbours.  Let  x  be  a  fixed  vertex,  and  H=I'(x)  the  graph  mduc~d on  the
neighbours of x. Then each edge  of His contained in a  unique maximal chque, and
points and  maximal  cliques  of H  form  a  partial  linear  space  ?f .girth  at  least. five.
Now if G is  moreover regular of valency k and each edge 1s m  exactly A. triang-
les  then  by  the  Theorem,  either  k~J.(,1.+3)/2  or  I'(x)  is  a  disjoint  union  of lines
of size  ,1. + 1.  It  follows  that  (A.+ l)!k  and  that  G  itself is  a  partial  linear  space.
In particular, this holds for strongly regular graphs with parameters v, k, .A., µ
(as defined, e.g.,  in [2])  where  µ=2.  Thus:

Corollary.  A strongly regular graph with  11=2  and  k<.?i.(A.+3)/2  is a partial quad-
rangle; in particular it satisfies the divisibility condition (.A.+ l)lk.

This Corollary rules  out infinitely many feasible sets of parameters of strongly
regular graphs that just escape the claw bound ([2],  Theorem 4.7 (iii)).  For example,
if  µ=2  and the smallest eigenvalue is  -4 then its  multiplicity is  24.?i.+210/(A.+6)
so  that  A.E {O,  I, 4, 8, 9, 15, 24, 29, 36, 64, 99, 204}.  The  claw  bound  rules  out  the
parameter sets  with  A.~24. The Corollary implies that also  .li.E {8,  9,  15}  is impos-
sible,  thus  leaving  the  parameter  sets  (v, k, A.)=(56,  10, 0), (99, 14, 1), (300, 26, 4).
(The  first  one  corresponds  to  the  Gewirtz  graph  [I],  the  other  two  are unknown.)
An  infinite  series  of  ruled  out  parameter  sets  is  e.g.  (v, k, .A.)=
=(t 2(6t+11)(3t+2), 6t 2+10t-2,5t-2),  admissible  for  t=sl, 2, 4  or  6  (mod 7)
but excluded by the corollary for  t~2.
Looking at the table we found one parameter set that just escaped the  bound,
namely  (v,  k, A.)=(1944, 67,  10).  But also  this  one  is  easily  ruled  out.  Returning
to  t~e proo~ of the  theorem  in the special case  k=67, .A.= 10  we see  that  there  are
no Imes  of size 7, 8 or 9 and that each line of length 6 intersects at least 4  and hence
exactly 4 other lin~s of size 6. If there is a line of size 6 then there are at least  1 +4+
+ 12= 1_7  . such  Imes,  together  containing  at  least  (2+4/2). 17 =68  points  a
contradict10n.  '

STRONGLY  REGULAR  GRAPHS  61

Hence  there  are  only lines  of size  2 or  10  and  k ~ A.2 +1=101
tradiction.  '  again a  con-

Clearly  our  result  can  also  be  applied  to  other  distance  regular  graphs,  but
we have no examples at present.

Table of "feasible" parameters for strongly regular graphs
with  v :§2000  and µ=2  but not with the parameters of a net

v  k  A,  r  s  f  g  existence

4  2  0  0  -2  2  1  4-cycle (unique)
16  5  0  1  -3  10  5  Clebsch  graph (unique)
56  10  0  2  -4  35  20  Gewirtz graph (unique)
85  14  3  4  -3  34  50  ?
99  14  1  3  -4  54  44  ?
243  22  1  4  -5  132  110  Berlekamp-Seidel-van Lint graph
300  26  4  6  -4  117  182  ?
352  26  0  4  -6  208  143  ?
456  35  10  11  -3  95  360  Ruled out by the claw bound
630  37  4  7  -5  259  370  ?
704  37  0  5  -7  407  296  ?
736  42  8  10  -4  207  528  Ruled out in this  note
875  46  9  11  -4  230  644  Ruled  out in this  note
1176  50  4  8  -6  500  675  ?
1276  50  0  6  -8  725  550  ?
1625  58  3  8  -7  754  870  ?
1944  67  10  13  -5  536  1407  Ruled out in  this  note
1961  70  15  17  -4  370  1590  Ruled  out in this  note

(Herek, r,  s are the eigenvalues of the graph,  with  multiplicities 1,/, g.)

References

[ 1]  A.  GEWIRTZ, The uniqueness of g(2, 2,  10,  56),  Trans. New York Acad. Sci., 31(1969),656-675.
[2]  A.  NEUMAIER,  Strongly  regular  graphs  with  smallest  eigenvalue  -M, Archiv der Mathematik,
33 (19i9), 392-400.

A. E.  Brouwer

Mathematical Centre
Kruislaan 413, Amsterdam
The Netherlands
 A.  Neumaier

Jnstitutfiir Angewandte Mathematik
Universitiit Freiburg,
D-7800 Freiburg, BRD
