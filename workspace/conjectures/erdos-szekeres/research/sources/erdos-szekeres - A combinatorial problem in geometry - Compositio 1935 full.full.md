<!-- source: https://www.numdam.org/article/CM_1935__2__463_0.pdf | converted from PDF -->

COMPOSITIO MATHEMATICA

P. ERDÖS
G. SZEKERES
A combinatorial problem in geometry

Compositio Mathematica, tome 2 (1935), p. 463-470

<http://www.numdam.org/item?id=CM_1935__2__463_0>

© Foundation Compositio Mathematica, 1935, tous droits réservés.

L’accès aux archives de la revue « Compositio Mathematica » (http:
//http://www.compositio.nl/) implique l’accord avec les conditions gé-
nérales d’utilisation (http://www.numdam.org/conditions). Toute utili-
sation commerciale ou impression systématique est constitutive d’une
infraction pénale. Toute copie ou impression de ce ﬁchier doit conte-
nir la présente mention de copyright.

Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

A Combinatorial Problem in Geometry

by

P.  Erdös and G.  Szekeres

Manchester

INTRODUCTION.

Our present problem bas been suggested by Miss Esther Klein

in  connection with the following proposition.
From 5 points of the plane of which no three lie on the same

straight line it is always possible to select 4 points determining
a  convex  quadrilateral.
We present  E.  Klein’s  proof here  because  later  on  we  are

going to make use  qf it.  If the least convex polygon which en-

closes  the points is  a  quadrilateral or  a  pentagon the theorem

is trivial. Let therefore the enclosing polygon be a triangle A BC.
Then the two remaining points D and E are  inside A BC. Two

of the given points (say A and C) must lie on the same side of
the connecting straight line  DE. Then it  is  clear  that AEDC

is  a  convex  quadrilateral.
Miss Klein suggested the following more general problem. Can

we find for a given n a number N(n) such that f rom any set con-

taining at  least N points it  is possible to  select  ln  points forming
a  convex  polygon?
There are  two particular questions:  (1)  does the number N
corresponding to n exist?  (2) If so, how is the least N(n) deter-
mined as  a  function of n?  (We denote the least N by No (n ) . )
We give two proofs that the first question is to be answered

in the affirmative.  Both of them will  give definite  values  for
N(n) and  the  first  one  can  be generalised to  any number of
dimensions.  Thus  we  obtain  a  certain  preliminary  answer  to
the second question. But the answer is not final for we generally
get in this way a  number N which is  too large. Mr. E. Makai
proved that NO(5)
= 9, and from our second demonstration,  we
obtain N(5)
= 21  (from the  first a  number of the order 21000°).
Thus it  is  to be seen,  that our  estimate lies  pretty far from

464

the  true  limit  No( n).  It  is  notable  that  N (3) == 3 == 2 + l,
No (4) == 5 == 22+1, .LlVo(5) == 9 == 23 + 1.
We might conjecture therefore that No(n)
= 2 n-2 + 1,  but the
limits  given by our  proofs are  much larger.
It is desirable to extend the usual definition of convex polygon
to include the cases  where three or  more  consecutive points lie

on  a  straight line.
 FIRST  PROOF.

The  basis  of  the  first  proof is  a  combinatorial  theorem  of
Ramsey 1). In the introduction it was proved that from 5 points
it  is  always possible to  select  4  forming a  convex  quadrangle.
Now it  can  be easily proved by induction that n points deter-
mine a  convex polygon if and only if any 4 points of them form

a  convex quadrilateral.
Denote the given points by the numbers 1,  2, 3,  ..., N, then

any k-gon of the set of points is represented by a set of k of these
numbers, or  as  we  shall  say,  by a  k-combination.  Let us  now

suppose each n-gon to be concave, then from what we observed
above we  can  divide the  4-combinations into two classes  (i. e.
into  "convex" and  "concave"  quadrilaterals)  such that  every
5-combination shall contain at least one  "convex" combination
and each n-combination at  least  one  concave  one.  (We regard
one combination as  contained in another, if each element of the

first  is  also an  element of the second.)
From Ramsey’s theorem,  it follows that this is impossible for

a  sufficiently ˛arge N.
Ramsey’s theorem can  be stated  as  follows:
Let k, l, i be given positive integers, k &#x3E; 1;  l &#x3E;  i.  Suppose that

there  exist  two  classes,  ce  and f3,  of i-combinations  of m elements
such that each k-combination shall contain at least one combination
from  class  oc  und  each  l-combination  shall  contain  at  least  one
combination from class  {J.  Then for sufficiently great m   mi(k, l)
this is not possible. Ramsey enunciated his theorem in a slightly
different form.
In othei  words: if the members of ce  had been determined as
above  at  our  discretion  and  m &#x3E; mi(k, l),  then there  must  be

at  least  one  l-combination  with  every combination of order i
belonging to  class  oc.

1)  F.  P.  RAMSEY,  Collected papers.  On a  problem of formal logic,  82-111.

Recently SKOLEM also  proved Ramsey’s theorem [Fundamenta Math. 20 (1933),
254-261].
 465

We give here a new proof of Ramsey’s theorem, which differs

entirely from th e  previous ones  and gives for mi(k, l )  slightly
smaller limits.

a)  If i =  1,  the theorem holds for every k and l.  For if we

select out of m some determined elements (combinations of order 1 )

as  the  class  ce,  so  that  every k-gon (this shorter denomination

will  be  given to  the  combination of order k) must contain at

least one  of  the  oc  elements, there are  at  most (k-l) elenlents
which do not belong to the class (X.  Then there must be at least
(m-k+l) elements of  ce.  If  (m-k+l) &#x3E; l, then there must be

an  1-gon of the  ce  elements and thus

which  is  evidently false  for sufficiently great m.
Suppose then that i &#x3E;  1.

b)  The theorem is trivial, if k or 1 equals i.  If, for example,
k = i,  then it  is  sufficient to  choose m = l.
For k = 1  means that all i-gons aie  a combinations and thus

in  virtue of m = l there is  one  polygon (i. e.  the 1-gon formed

of all  the  ØlØments),  whose i-gons are  all  ce-combinations.
The argument for 1 = i runs  similarly.
c)  Suppose finally that k &#x3E;  i ;  and suppose that the theorem
holds  for  ( i -1)  and  every and l, further for i,  k, l
-  1  and

i, k - 1, l.  We shall prove that it will hold for i, k, l also and in
virtue  of  (a) and  (b) we  may say that the theorem is  proved
for all  i, k, l.
Suppose then that we  are  able to  carry  out  the division  of
the i-polygons mentioned above. Further let k’ be so great that

if in every 1-gon of k’ elements there is at least one P combination,
then  there  is  one (k-l)-gon all of whose i-gons are P combina-

tions. This choice of k’ is always possible in virtue of the induction-

hypothesis,  we  have only to  choose  k’ = mi(k-l, 1).
Similarly we choose l’ so great that if each k-gon of l’ elements
contains  at  least one  oc  combination,  then there is  one  (l-1 )-
gon  all  of  whose  i-gons  are  oc  combinations.
We then take m larger than k’  and l’;  and let

be an arbitrary k’ -gon of the first (n-1 ) elements. By hypothesis
each 1-gon contains  at  least one fl combination, hence owing to
the choice of k’, A contains one  (k -1 )-gon (a , a m ,
...,  a Mk-1)1  2  a  k-l
whose i-gons all belong to the class fl. Since in (a ml, ..., am , n)

30

466

there is at least one  ce  combination, it is clear that this must be

one of the i-gons

In just the same  way we  may prove by replacing the roles
of k and 1 by k’  and l’and of x  by fJ,  that if

is  an  arbitrary l’-gon of the first  (n-1) elements, then among
the i-gons

there  must be a fl combination.
Thus we can divide the (i-l)-gons of the first (n -1) elements
into  classes  oc’  and fl’ so that each k’ -gon A shall contain at least

one  oc’  combination B and each l’-gon A’ at least one fl’ com-
bination  B’.  But, by the induction-hypotheses this is impossible
for m &#x3E; mi-l(k’l’) + 1.
By following the induction,  it  is  easy to  obtain for mi(k, 1)
the following functional equation;

By this recurrence-formula and the initial values

obtained from  (a)  and  (b)  we  can  calculate  every mi(k, l ).
We obtain  e. g.  easily

The function  mentioned in  the  introduction has the form

Finally, for the special case  i = 2,  we give a graphotheoretic
formulation  of  Ramsey’s  theorem and present a  very simple
proof of it.
THEOREM :  I1t  an  arbitrary graph let  the maximum number of
independent  points 2 )  be k; if the number of points is N &#x3E; m(k, 1)
then there exists in our graph a complete graph 3) of order l.

2 )  Two points are  said to  be independent if they are not connected; k points

are  independent if every pair is  independent.

3)  A complete graph is  one  in  which every pair of points is  connected.

467

PROOF.  For 1 = 1,  the theorem is trivial for any k, since the
maximum number of independent points is k and if the number

of points is  (k+1 ), there must be an  edge (complete graph of
order  1).
Now suppose the theorem proved for (l-l) with any k.  Then
N-k  in
 depen dent
 .
at least - edges start from one  of the independent points.
k
Hence if

i. e.,

then,  out  of the  end points of these  edges we  may select,  in

virtue  of  our  induction  hypothesis,  a  complete graph whose
order is at least (l-l).  As the points of this graph are connected
with the  same  point, they form together a  complete graph of
order l.
 SECOND PROOF.

The foundation of the second proof of our  main theorem is
formed  partly  by  geometrical  and  partly  by  combinatorial

considerations.  We start  from  some  similar  problems and  we

shall  see,  that the numerical limits  are  more  accurate then in
the previous proof; they are  in  some  respects  exact.
Let us  consider the first  quarter of the plane, whose points
are  determined by coordinates  (x, y). We choose n points with
monotonously increasing abscissae 4).
THEOREM : It is  always possible to  choose  at  least  vin points
with  increasing  abscissae  and  either  monotonously increasing or

,jnonotonously  decreasing ordinates.  If two  ordinates  are  equal,
the  case  may equally be regarded as  increasing or  decreasing.
Let us  denote by f(n, n ) the minimum number of the points
out of which we can select n monotonously increasing or decreas-

ing ordinates.
We assert that

Let us select n monotonously increasing or decreasing points out

of the f(n, n). Let us replace the last point by one of the (2n-l)
new  points. Then we  shall  have once  more f(n, n) points,  out

4)  The same  problem was  considered independently by Richard Rado.

468

of which we  can  select as  before n monotonous points. Now we

replace the last point by one  of the new ones  and so  on.  Thus

we obtain 2n points each an endpoint of a monotonous set. Suppose
that among them (n+l) are end points of monotonously increas-

ing sets.  Then if  y l &#x3E; Yk for 1 &#x3E;  k we add Pl to the monotonously
increasing set of Pk and thus, with it, we shall have an increasing
set of (n+l) points.  If Yk &#x3E; Yt for every Jc  1, then the (n+1 )
decreasing  end-points  themselves  give the  monotonous  set  of
(n+1) members.  If  between the  2n  points there  are  at  least
(n+l) end-points of monotonous decreasing sets,  the proof will

run in just the same way.
But it may happen that, out of the 2n points, just n are  the

end-points of increasing sets,  and n the end-points of decreasing
sets. Then by the same reasoning, the end-points of the decreasing
sets necessarily increase. But after the last end-point P there is

no point, for its ordinate would be greater or smaller than that
of P. If it is greater, then together with the n end-points it forms

a monotonously increasing (n + 1 ) set and if it is smaller, with the

n  points belonging to  P,  it  forms  a  decreasing set  of  (n+l)
members. But by the same reasoning the last of the n increasing
end-points Q ought to be also an extreme one and that is evidently
impossible. Thus we may deduce by induction

Similarly let f(i, k)  denote  the  minimum number  of  points
out of which it is  impossible to  select  either i monotonously in-

creasing or  k monotonously decreasing points. We have then

The proof is  similar to  the previous one.

It is  not difficult to  see,  that this Iimit is  exact i. e.  we can

give  (i-l) (k-1)  points  such  that  it  is  impossible to  select

out of them the desired number of monotonously increasing or

decreasing  ordinates.
We solve  now  a  similar  problem:
P1, P2’ ...  are  given points  on  a  straight  line.  Let f 1 ( i, k)
denote  the  minimum  number  of  points  such  that  proceeding
from left  to  right we  shall  be able to  select  either i points so
that  the  distances  of  two  neighbouring points  monotonously
increase  or k points  so  that the  same  distances  monotonously
decrease.  We assert  that
 469

Let the point C bisect the distance A B  (A and B being the first
and the last points). If the total number of points is fI (i - l, k ) +

+ f1(i, k-1) - 1,  then either the number of points in the first

half  is  at least f,(i-1, k),  or  else there are  in the second half

at least f, (i, k - 1 ) points. If in the first half there are fi (i - 1, k)
points then either there are among them k points whose distances,
from left to right, monotonously decrease and then the equation
for  f 1 ( i, k)  is  fulfilled,  or there must be (i-1) points with in-
creasing distances. By adding the point B, we have i points with
monotonely increasing distances. If in the second interval there

are  fl(i, k-1)  points,  the proof runs  in  the  same  way.  (The

case,  in which two distances are the same,  may be classed into
either the increasing or the decreasing sets.)
It  is  possible to  prove that this  limit is  exact.  If the limits
fl(i-l, k)  and  fl(i, k-l)  are  exact  (i. e.  if  it  is  possible  to
give [fl(i-l, k) -lJ  points  so  that  there  are  no  (i -1 )  in-

creasing nor  k  decreasing distances)  then  the  limit fl(i, k)  is

exact  too.  For if  we  choose  e. g. [f, (i - 1, k) - 1 ] points in the

0 ... 1  interval,  and [f1(i, k-l) - 1]  points  in  the  2 ... 3

interval,  then  we  have [,fl (i, k) - 1 ]  points out of which it  is

equally impossible to select i points with monotonously increasing
and k points with decreasing distances.
We now tackle the problem of the convex n-gon. If there are

n given points, there is  always a  straight line which is  neither

parallel nor  perpendicular to  any join of two points. Let this

straight line be e. Now we regard the configuration A1A2A3A4
...

as convex, if the gradients of the lines A1A2, A2A3,
...  decrease
monotonously, and as concave if they increase monotonously. Let

f2(i, k) denote the minimum number of the points such that from
them we may pick out either i sided convex or k-sided concave
configurations. We assert  that

We  consider  the  first f2(i-l, k) points.  If out  of them there

can be taken a concave configuration of k points then the equation
for f2(i, k) is fulfilled. If not, then there is a convex configuration
of (i-1) points. The last point of this convex configuration we
replace by another  point.  Then  we  have  once  more  either k

concave  points  and  then the assertion holds, or  (i-1) convex

ones.  We go  on  replacing the  last  point, until  we  have made

use  of  all  points.  Thus  we  obtain f2(i, k-1) points,  each  of
which  is  an  end-point  of  a  convex  configuration  of  (i-1)

470

elements. Among them, there are either i convex points and then

our  assertion is  proved, or  (k - 1) concave  ones.  Let the first
of them be Al, the second A2’ Ai is the end-point of a  convex

configuration  of  (i-1) points.  Let the neighbour of A, in this

configuration be B. If the gradient of BA, is greater than that of
A1A2,  then  A2 together with the  (i-l) points form a  convex

configuration; if the gradient is  smaller, then L’ together with
A1A2...
.  form  a  concave  k-configuration.  This  proves  our

assertion.
The deduction of the recurrence  formula may start from the

statement:  f2(3, n) ==f2(n, 3) == n  (by  definition).  Thus  we

easily obtain

As before we  may easily prove that the limit given by (11)

is exact, i. e.  it is possible to give 2k-4) points such, that they1-2
contain  neither  convex  nor  concave points.
Since by connection of the first and last points, every set of k

convex or concave points determines a convex k-gon it is evident
2k --4) + i] points always contain a  convex  k-gon.that  k-2  + 1  points al ways contain  a  convex  -gon.
And  as  in  every  convex  (2k -1)  polygon there  is  always
either a convex or a concave configuration of k points, it is evident

that it  is  possible to give ( 2k-4 k 2) points,  so  that  out  of them

no  convex  (2k -1)  polygon can  be selected.  Thus the limit  is

also  estimated from below.
Professor D.  Kônig’s lemma 5)  of infinity also gives a  proof
of the theorem that if k is  a  definite number and n sufficiently
great, the n points always contain a convex k-gon. But we thus
obtain  a  pure  existence-proof,  which  allows  no  estimation  of
the number n.  The proof depends on  the statement that if M

is an infinite set of points we may select out of it another convex

infinite  set  of points.

(Received December 7th@  1934.)

5)  D.  KôxiG,  Ùber  eine  Schlußweise  aus  dem  Endlichen  ins  Unendliche

[Acta Szeged 3  (1927), 121-130].
