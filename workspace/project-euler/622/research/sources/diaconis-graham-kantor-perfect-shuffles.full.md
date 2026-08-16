<!-- source: https://pages.uoregon.edu/kantor/PAPERS/PerfectShuffles.pdf | converted from PDF -->

ADVANCES  IN  APPLIED  MATHEMATICS  4,  175- 196 ( 1983)

The  Mathematics  of  Perfect  Shuffles

PERSI  DIACONIS

Stanford  University,  Stanford  California  94305  and  Harvard  Universiv,  Cambridge,

Massachusetts  02138

R.  L.  GRAHAM

Bell  Laboratories,  Murray  Hill,  New  Jersey  07974  and  Stanford  University,  Stanford,

California  94305

WILLIAM  M.  KANTOR

University  of  Oregon,  Eugene,  Oregon  97403  and  Bell  Laboratories,  Murray  Hill,

New  Jersey  07974

There  are two  ways to perfectly  shuffle a deck of  2n  cards. Both  methods  cut  the
deck in  half  and  interlace  perfectly. The  out  shuffle 0  leaves the original  top  card  on
top.  The  in  shuffle I  leaves the original  top  card  second  from  the top.  Applications
to  the design  of computer  networks  and  card  tricks are  reviewed.  The  main  result  is
the determination  of the group  (I,  0)  generated  by the  two  shuffles, for all  n.  If 2 n
is not  a power  of 2, and  if 2n  *  12,24,  then  (I,  0)  has index  1,2,  or  4 in  the Weyl
group  B,  (the  group  of all  2”n!  signed n  x  n  permutation  matrices).  If  2n  =  2“,  then
(I,  0)  is isomorphic  to a semi-direct  product  of Zi  and  Z,.  When  2 n  =  24,  (I,  0)
is isomorphic  to a semi-direct  product  of 2-j’  and  M,,,  the Mathieu  group  of degree
12. When  2n  =  12,  (I,  0)  is  isomorphic  to  a  semi-direct  product  of  Zi  and  the
group  PGL(2,5)  of all  linear  fractional  transformations  over  GF(5).

1.  I~RODUCTI~N

There  are  two  ways  to  perfectly  shuffle  a  deck  of  2n  cards.  Both  cut  the
deck  in  half  and  interlace  perfectly.  The  in  shuffle  I  leaves  the  original  top
card  second  from  the  top.  The  out  shuffle  0  leaves  the  original  top  card  on
top.  Let  the  deck  be  labeled  (0,  1,.  . . ,  n  -  1, n,.  . . , 2n  -  1).  After  an  in
shuffle  the  order  is  (n,  0,  n  +  1,.  . . ,  2n  -  1, n  -  1).  After  an  out  shuffle,
the  order  is  (O,n,l,n+  l,...,  n  -  1,2n  -  1).  These  shuffles  have  been
used  by  gamblers  and  magicians  to  manipulate  cards.  A  historical  review,
175
 0196-8858/83  $7.50
Copyright  0  1983  by  Academic  Press,  Inc.
All  rights  of  reproduction  in  any  form  reserved.

176  DIACONIS,  GRAHAM,  AND  KANTOR

describing  “widely  known”  properties  of  the  shuffles,  is  in  Section  3.  This
section  also  describes  results  of  Levy  on  the  cycle  structure  of  the  shuffles,
and  results  concerning  decks  of  odd  size.
In  and  out  shuffles  appear  in  computer  science  as  a  way  of  connecting
processors  in  parallel  processing  machines.  One  widely  known  application  is
an  O(log  n)  FFT  algorithm.  Section  4  discusses these  applications  as well  as
some  new  results;  for  example,  an  array  of  2k  numbers  can  be  reversed  in  k
in  shuffles.  Section  5  discusses  some  related  permutations:  Levy’s  work  on
the  “milk  shuffle”  and  Morris’  work  on  generalized  perfect  shuffles.
The  main  result  of  this  paper  is  a  determination  of  the  group  generated
by  in  and  out  shuffles.  This  group  will  be  called  the  shuffle  group  and
denoted  (I,  0).  Both  of  the  generators  I  and  0  preserve  central  symmetry;
that  is,  cards  symmetrically  located  about  the  center  of  the  deck  (0  and
2n  -  1,  1 and  2n  -  2,  etc.)  are  sent  to  positions  symmetric  about  the  center.
Thus  (I,  0)  is  a  subgroup  of  the  centrally  symmetric  permutations.  This
group  is  isomorphic  to  the  Weyl  group  B,,  of  n  X  n  signed  permutation
matrices.  This  is  the  group  of  all  n  x  n  matrices  with  entries  0,  f  1, and  one
nonzero  entry  in  every  row  and  column.  Equivalently,  it  is  the  group  of  all
2”n!  symmetries  of  the  n-dimensional  generalization  of  the  octahedron,
whose  vertices  are  fe,,.  . . , f  e,,  where  e,,.  . . ,  e,  is  the  standard  basis  of
BP”  (see  Coxeter  [5]).  The  pairs  {ei,  -  ei}  correspond  to  the  pairs  of  card
positions  which  are  centrally  symmetric.
We  will  have  to  deal  with  three  homomorphisms  ofB,,.  If  g  E  B,,  then
sgn(g)  is  its  sign  as a  permutation  of  2n  cards,  and  sgn(g)  is  its  sign  as  a
permutation  of  n  centrally  symmetric  pairs;  and  g  +  sgn(g)g(g)  is  a
further  homomorphism  to  { f  l},  whose kernel  is  the  Weyl  group  0,.

THEOREM.  Let  (I,  0)  be  the  permutation  group  generated  by  in  and  out
shuffles  of  2n  cards.

(a)  If  n  =  2  (mod4)  an  n  >  6,  then  (I,  0)  is  isomorphic  to  B,  and d
I(Z,  0)l  =  n!2”.  If  n  =  6,  then  (I,  0)  is  a  semi-direct  product  of  Z,6  with

PGL(2,5).
(b)  If  n  =  1  (mod4)  and  n  >  5,  then  (I,  0)  is  the  kernel  of  s@  and
I(I,  0)l  =  n!2”-‘.

(c)  If  n  =  3  (mod4),  then  (I,  0)  is  isomorphic  to  D,,  and  I(I,  O)l  =
n-1
n!2  .

(4  If  n  =  0  (mod4),  n  >  12, and  n  not  a power  of  2,  then  (I,  0)  is  the
intersection  of  the  kernels  of  sgn  and  sz,  and  I( I,  O)l  =  n!2”-  2. If  2n  =  24,
then  (I,  0)  is  a  semi-direct  product  of  Zi’  with  the  Mathieu  group  M,,  of
degree  12.

(e)  If  2n  =  2k,  (I,  0)  . is  isomorphic  to  the  semi-direct  product  of  Z,k  by
Z,,  where  Z,  acts  by  a  cyclic  shift  and  I(I,  O)l  =  k  * 2k.

PERFECT  SHUFFLES  177

TABLE  I
Order  of  the  Group  (I,  0);  M  =  2”n  !

2n  2  4  6  8  10  12  14  16  18

I(I,O)(  2  2  .  22  M/2  3.  23  M/2  M/3!  M/2  4.  24  M/2

2n  20  22  24  26  28  30  32  34  36

I([*  O)l  M  M/2  M/(7!  .  2)  M/2  M  M/2  5  25  M/2  M

2n  38  40  42  44  46  48  50  52

I(I~O)l  M/2  M/4  M/2  M  M/2  M/4  M/2  M

The  theorem,  and  a  number  of  other  results  about  the  shuffle  group,  are
proved  in  Section  2.  A  list  of  the  order  of  the  shuffle  group  for  2n  =
2,4,.  . . ) 52,  appears  in  Table  I.  This  table  was  computed  using  a  stream-
lined  implementation  of  an  algorithm  of  Sims  [24]  developed  by  Eric
Hamilton  and  Donald  Knuth  at  Stanford  University.  The  numerical  evi-
dence  allowed  us  to  guess  at  the  theorem.  For  a  discussion  of  Sims’
algorithm  see Furst  et  al.  [7].
Finally,  we mention  the  connection  between  our  shuffles  (for  a deck  of  24
cards)  and  some  very  recent  work  of  Borcherds  et  al.  [2]  on  representations
of  the  Leech  lattice  in  hyperbolic  space.  Section  5  contains  further  discus-
sion.
 2.  PROOF  OF  THE  THEOREM

We  begin  by  establishing  a number  of  basic  properties  of  perfect  shuffles.
Lemma  1  gives  the  order  of  in  and  out  shuffles.  It  is  well  known:  see
Uspensky  and  Heaslet  [26,  pp.  244-2451,  Herstein  and  Kaplansky  [ll,
Chap.  3.41.

LEMMA  1.  The  order  of  the  in  shuffle  permutation  is  the  order  of  2
(mod2n  +  1).  The  order  of  the  out  shuffle  is  the  order  of  2  (mod2n  -  1).

Proof  The  order  of  an  in  shuffle  is  the  order  of  an  out  shuffle  with  a
deck  containing  2  more  cards,  so we only  prove  the  result  for  out  shuffles.  If
the  deck  is  labeled  0  1 ,  ,***,  2n  -  1,  then  after  one  out  shuffle  the  card
labeled  j  is  at  position  2j  (mod  2n  -  1) if j  <  2n  -  1. After  k  shuffles  it  is
in  position  2&j  (mod  2n  -  1). All  cards  will  be  in  their  original  positions  for
the  smallest  k  such  that  2k  =  1 (mod2n  -  1).  0

Remark.  A  pack  of  52  cards  requires  8  out  shuffles  or  52  in  shuffles  to
recycle.  Because  of  Fermat’s  theorem,  the  pack  will  always  recycle  after

178  DIACONIS,  GRAHAM,  AND  KANTOR

at  most  2n  -  2 out  shuffles,  although  fewer may  do.  A  famous  conjecture  of
Artin  asserts that  2 is  a primitive  root  (mod  p)  for  infinitely  many  primes  p.
If  this  is  true,  there  are  arbitrarily  large  n  such  that  2n  -  2  out  shuffles  are
required  to  recycle  2n  cards.

Lemma  2  gives  an  algorithm  for  bringing  the  top  card  to  any  position  by
a  sequence  of  in  and  out  shuffles.  The  result  was  first  given  by  Alex
Elmsley.  For  a  proof,  see Morris  [21,  Proposition  11.

LEMMA  2.  Let  the  positions  in  a  deck  of  2n  cara% be  labeled 0,  1, . . . ,
2n  -  1.  To bring  the top card to position k,  express k  in binary,  interpret  1 as
in and 0 as out, and perform  the indicated sequence of  in and out shuffles from

left  to right.

Lemmas  1 and  2  give  the  following  lower  bound  for  the  shuffle  group:

LEMMA  3.  The  order  of  the  shuffle  group  is  at  least  2n  X  order  of  2
(mod2n  -  1).

The  next  result  proves  part  (d)  of  the  theorem.  It  establishes  that  the
lower  bound  of  Lemma  3  is  achieved  for  decks  of  size  2’.  The  proof
provides  a simple  interpretation  of  in  and  out  shuffles  as maps  on  the  vector
space  Zf.

LEMMA  4.  For  2n  =  2k,  the  shuffle group  is  isomorphic to  a  semi-direct
product  of  Zt  by  zk.

Proof.  Label  the  cards  using  their  binary  expansions  (xt,.  . . , xk).  It  is
easy  to  check  that,  using  an  obvious  notation,

0:  (x+1  ,...,  xk)  +  (xz,x~,-,  xk,x,),
1:  (x~,x~,...,xk)-,(x~,x~,...,xk,x,)  withx,  =  1  -  x,.

The  permutations  Oj,  0  Q j  <  k,  form  a  cyclic  group  (0).  The  permuta-
tions  Bj  =  Oj-‘10-i  send  (x,,.  . . , xi,.  . . , xk)  into  (x,,.  . . , Xj,.  . .,  xk),  for
1  gjgk.MapZ,kintotheshufflegroupbysendinga=(a,,...,a,)~Z,k
into  l-l,“,,B,?~.  It  is  easy  to  see this  is  an  isomorphism.  The  image  group
intersects  the  cyclic  group  (0)  only  in  the  identity  and  their  product
contains  0  and  I.  The  action  of  Z,  on  Zt  is  a  cyclic  shift.  0
Both  in  and  out  shuffles  preserve  arrangements  with  “central  symmetry.”
We  now  turn  to  definitions  and  amplification  of  this  fact.  Throughout,
permutations  will  be  applied  on  the  right,  so xg  is  the  image  of  x  under  the
permutation  g.  S,, and  A,  denote  the  symmetric  and  alternating  groups  of
degree  n.  If  S  is  a  set  of  permutations,  then  (S)  denotes  the  group
generated  by  S.
 PERFECT  SHUFFLES  179

DEFINITIONS.  If  a  <  b,  then  [a,  b)  =  (x  E  Zla  d  x  <  b}.  A  permutation
g  E  S,,  has  central  symmetry  if  (i)g  +  (2n  -  1  -  i)g  =  2n  -  1  for  all
i  E  [0,  n).  The  subgroup  of  centrally  symmetric  permutations  is denoted  B,,.
It  is  natural  to  label  the  objects  being  permuted  as  0,  1, . . . , n  -  1, (n  -
l)‘,  . . . )  l’,  0’,  where  x  f)  x’  is  the  natural  pairing.  Let  X  =  {x,  x’}.  A  permu-
tation  g  E  B,, induces  a permutation  g  of  {X]x  E  [0,  n)}.  The  map  g  +  g  is  a
homomorphism  from  B,,  onto  S,,  with  kernel  equal  to  ((0,O’))  X  ((1,1’))
X  ...  x  ((n  -  l,(n  -  1)‘))  E  Z;.  Note  that  G(g)  =  sgn(g).

In  this  notation  the  shuffles  can  be  written

i
 x  +  2x
0:  and  x’  --) (2x)‘,  if  x  E  [0,  fn),

x  +  (2(n  -  x)  -  1)’  and  x’+2(n-x)-l,  ifxE[fn,n);

i
 x+2x+1
I:  and  x’  +  (2x  +  l)‘,  ifx  E  [O,(n  -  1)/2),

x  +  (2(n  -  x  -  1))’  and  x’  +  2(r1  -  x  -  l),  if x  E  [(rz  -  1)/2,  r~).

Let  G  =  (I,  0).  Let  c  be  the  image  of  G  in  S,, and  let  K  be  the  kernel  of
G  +  c.

LEMMA  5.  When n  =  12,  c  is isomorphic to  M,,  and K  is isomorphic to
Z;‘.

Proof:  The  group  c  is  generated  by  0  =  (i%@??sm%fl)  and  7  = ---------  --
(0137861025  11)(49).  A  computer  check  shows that  the  order  of  cis  95,040, _.
the  order  of  M,2.  Further,  G’ is  doubly  transitive;  indeed  g  is  an  1 l-cycle
fixing  0  and  Z moves  0,  so  G  is  transitive,  and  to  bring  symbols  labeled
(i,  j)  to  postions  (k,  I),  bring  i  to  0,  bring  j  to  the  appropriate  place  by
iterates  of  0,  and  then  bring  i  to  k.  Sims  [24]  showed  that  M,,  is  the  only
doubly  transitive  permutation  group  of  this  order.  The  result  for  K  follows
from  the  order  of  G  given  in  Table  I.  0

We  were  intrigued  by  the  appearance  of  M,,.  Table  II  lists  66  6-sets;
these  sets and  their  complements  in  [0,12)  form  the  design  S(5,6,12):  each
5-set  is in  exactly  one  of  the  132 6-sets.  Moreover,  Aut  S(5,6,12)  =  M,,.

Remark.  Lemmas  4  and  5  are  concerned  with  two  of  the  three  excep-
tional  situations  appearing  in  the  theorem.  The  third  situation  occurs  when
2n  =  12,  and  is  less interesting.  In  this  case, (X]X  E  [0,6)}  will  be  identified
with  GF(5)  u  {co}  as follows:

Then  0  sends  x  +  x  +  2  and  f  sends  x  +  2/x.  This  identifies  c  with
PGL(2,5).  Since  Z605  =  (O,O’),  the  transitivity  of  G  yields  that  /Kl  =  26. If
k  =  (2,2’)  and  I  =  (3,3’),  then  k -‘02k  and  I  -‘Z41  send  [0,6)  to  itself  and

180  DIACONIS,  GRAHAM,  AND  KANTOR

TABLE  II
A  Design  with  Automorphism  Group  M,,

1  5  711  0  4:  3  11  8  0  1  9  0  6  11  1  7  8

2  10  9  1  0  8  617025  011  12  9  7

I
435207  11  2  9  0  41040  1  2  4  5  9

8  6  10  4  0  9  145083  0  2  4  8  10  5

7  11  3  8  0  5  2  8  10  0  7  6  0  4  8  7  3  10

9  1  6  7  0  10  4  7  3  0  911  087963

5  211  9  0  3  896051  0  7  9  5  11  6

10  4  1  5  0  6  7  5  11  0  10  2  0  9  5  10  1  11

3  8  2  10  0  11  9  10  1  0  3  4  0  5  10  3  2  1

674301  532068  0  10  3  6  4  2

11  9  8  6  0  2  10  6  4  0  11  7  0  3  6  11  8  4

1  10  0  3  8  6

7  6  5  0  10  3  5  7  110  8  0:2  3  0  6  711

9  11  10  0  3  6  10  ‘9  2  3  7  0  4  6  011  9  1

5  13  0  611  354690  8  11  0  1  5  2

10  2  6  0  11  1L  6  10  8  11  5  0  7  1  0  2  10  4

3  4  11  0  1  2  11  3  7  1  10  0  920438

681024  169230  540867

11  7  2  0  4  8  211  5  4  6  0  10  8  0  7  11  9

1  9  4  0  8  7  4  1  10  8  11  0  370915

258079  823710  6  9  0  5  2  10

4  10  7  0  9  5  746920  11  5  0  10  4  3

8  3  9  0  5  10  9  811  5  4  0

induce  PGL(2,5)  there.  Consequently,  (I,  0)  is  a  semi-direct  product  as
asserted  in  the  theorem.  (N.B.  -  PGL(2,5)  =  S,.)

LEMMA  6.  (aJIJ  n  =  0  (mod  4),  then  G  is  in  the  kernels  of  the  homomor-
phisms  sgn  and  sgn.

(b)  If  n  =  1 (mod4),  then  G  is  in  the  kernel  of  &$.
(c)  Zf  n  =  3  (mod4),  then  G  is  in  the  kernel  of  sgn  . G.

Note  that  parity  considerations  give  no  restrictions  on  G  when  n  =  2
(mod4).  On  the  other  hand,  all  homomorphisms  of  B,  in  the  lemma  are
onto  {f  l},  so  that  the  orders  of  the  groups  given  in  the  theorem  are  upper
bounds.
 PERFECT  SHUFFLES  181

Proof.  It  suffices  to  prove  that  the  signs  of  Z, Z, 0,  and  Dare  as in  Table
III.  Since  the  case of  Z follows  from  that  of  0  by  replacing  n  by  n  +  1, we
only  need  to  consider  the  parity  of  0  and  ??.
In  order  to  deal  with  0,  we label  the  cards  0,  1,. . . , 2n  -  1,  so x0  =  2x
(mod  2n  -  1). Let  x  -C y.  We  need  to  decide  when  x0  >  y0.  Since  x0  =  2x
or  2x  -  (2n  -  1)  and  x  c  y,  the  inequality  x0  >  y0  holds  if  and  only  if
0  <  x  d  n  -  1,  n  <  y  <  2n  -  1,  and  2x  >  2y  -  (2n  -  1).  Thus,  for  each
x  E  [0,  n  -  1) we must  restrict  y  to  [n,  x  +  n).  The  number  of  pairs  (x,  y)
is  then  c::ix  =  y
0  .

Next,recallthata=%or2(n-x)-l.LetX<yandz>g.
There  are  two  ways this  can  happen:

(i)  x,  y  >  n/2,  in  which  case  2(n  -  x)  -  1  >  2(n  -  y)  -  1 holds,  or

(ii)  x  <  n/2,  y  2  n/2,  and  2x  >  2(n  -  y)  -  1, that  is,  x  +  y  >,  n.

Set  m  =  [(n  +  1)/2].  The  number  of  (js,  7)  in  (i)  is  (n 2  m).  The  number  in
(ii)  is  obtained  by  fixing  x  E  [0,  m),  and  then  letting  y  E  [n  -  x,  n).  Thus,
the  total  number  of  pairs  (x,  7)  is

If  n  is  even  this  is  2
(  1
T  ;  if  n  is  odd  it  is  (n  -  1)2/4.  It  is  now  straightfor-
ward  to  check  Table  III  and  then  deduce  Lemma  6.  0

Lemma  7  will  be  used  several  times.  The  simple  proof  is  omitted.

LEMMA  7.  Suppose  n  >,  3.  Form  a  graph  with  vertices  the  3-cycles  in  A,,.
Join  two  3-cycles  when  some  point  of  [0,  n)  is  displaced  by  both  of  them  (i.e.,
when  the  corresponding  3-sets  are  not  disjoint).  Let  H  be  a  subgroup  of  A,,
generated  by  a connected  set  of  3-cycles.  Zf  each point  of  [0,  n)  is  displaced  by  a
3-cycle  in  H,  then  H  =  A,.

We  now  begin  the  main  part  of  the  proof  of  the  theorem.  Some  further
notation  will  be  required.  If  g  and  h  are permutations,  and  in  cycle  notation

TABLE  III
(w(g),  w(g))  for  g  =  Z or  0

n (mod  4)

1

182  DIACONIS,  GRAHAM,  AND  KANTOR

his  se-(  . . . . x,y  ,...  )..e,  thenhs=g-‘hgis  me-( . . . . xg,yg  ,...  )....
Let  z be  the  element  of  S,,  interchanging  x  and  x’  for  all  x  E  [0,  n);  thus,  z
has  the  effect  of  reversing  the  order  of  the  deck.  Let  G*  consist  of  the
elements  of  G  sending  [0,  n)  to  itself.

LEMMA  8.  If  G*  2  A,  then  IK(  a  2”-‘.

Prooj  -  -.
By  Table  III,  at  least  one  of  the  permutations  I,  0  is  even.  Let
h  E  {I,  0}  with  6  even.  Let  f  E  G*  with  f  =  K,  and  set  k  =  f  -  ‘h.  Then
k  E  K  -  (z),  k  fixes  0  and  o_l, and  k-interchanges  certain  pairs  x,  x’.  Pick
any  g  E  G*  such  that  @  =  x,  G  =  0  for  some  such  pair  x,  x’,  and  such
that  z  =  r  whenever  yk  =  y.  Then  kg  =  (x)(x’)(OO’)  * . .  and  kkg  =
(OO’)(xx’).  Conjugating  by  elements  of  G*  produces  all  permutations
(aa’)(bb’).  Thus  pq  >  2”-‘.  0

The  argument  is  easiest  for  odd  n.  By  Table  I  we may  assume  that  n  >  3.

LEMMA  9.  The  theorem  ho&  if  n  is  odd.

Proof:  We  calculate  the  following  permutations:

IO-‘:  x  +  (n  -  1 -  x)’  (a cut  at  the  center);

I-,o:  2x*2x+  1,

I
 if  x  c  (n  -  1)/2

n  -  1 --,  (n  -  1)’  (pairwise  adjacent  transpositions);

1 2x  +  (n  -  2 -  2x)‘,  if  x  <  (n  -  1)/2,

I-‘O-IO-‘:  2x+l+(n-1-2x)‘,  if  x  <  (n  -  1)/2,

n-1+0;

2x  +  2x  +  2,  if  x  <  (n  -  1)/2,

b:=  (I-‘OIO-‘)2:  ;,: l-+-;;~‘l ,  if  0  <  x  <  (n  -  1)/2,
1 +  0’.

Then

b  =  (0,2,4  ,...,  n  -  3,  n  -  1, (n  -  2)‘,  (n  -  4)‘,.  . . )  l’)(O’,  2’,.  . . )  l),

c:=  b”-’  =  (0,1,2  ,...,  n  -  l)(O’,l’,...,  (PJ -  1)‘),

c2 =  (0,2,4  ,...,  n  -  3, n  -  1,1,3  )...)  n  -  4,  n  -  2)(0’,2’)...)  (Fr -  2)‘),

(cy’O=  (1,3,5  )...)  n  -  2,(n  -  1)‘,0,2  )...,  n  -  5,n  -  3)

x  (1’,3’)...)  (n  -  3)‘),

PERFECT  SHUFFLES  183

i):=  c-yc2)~-‘~  =  (0  , n  -  l,l)(O,  (n  -  l)‘,  l’),

UC -’  =  ((n  -  l)‘,  n  -  2,o)(n  -  l,(n  -  2)‘,0’),

w:=  (Dc-‘)l-‘o  =  (n  -  1 ) n  -  3,l)((n  -  l)‘,(n  -  3)‘,  1’).

Clearly,  c and  w belong  to  G*.  Restricting  G*  to  [0,  n)  it  is  easy to  check  the
connectedness  of  its  set of  3-cycles.  Thus,  Lemma  7  yields  that  G*  2  A,.  By
Lemma  8,  (K]  2  2”-‘.
If  n  =  3 (mod4),  then  Gcontains  A,,  and  the  odd  permutation  a,  so that
G  =  S,,.  Since  z  is  an  odd  element  of  S,,,  z  @ G  by  Lemma  6(c).  Thus
1 K  1 =  2” -  ‘,  completing  the  proof  in  this  case.
If  n  =  1 (mod4),  then  c  =  A,  by  Lemma  6(b).  Thus,  there  is  a  g  E  G*
with  g  =  1  Clearly,  g  is  even,  while  I  is  odd  by  Table  III.  Now  g1-  ’  is  odd
and  belongs  to  K.  Since  K  already  contains  all  permutations  of  the  form
(xx’)(  ~JJ’)  (see  the  proof  of  Lemma  8),  it  follows  that  ]K]  =  2”.  Then  G
consists  of  all  permutations  in  B,  that  map  to  even  permutations  of  S,.  0

The remainder  of  this  section  is  devoted  to  the proof  of  the  theorem  when  n  is
euen.  This  will  be  accomplished  in  a  sequence  of  lemmas.

Notation.  2n  =  2%  with  1) >  1 and  2) odd.  (The  manner  in  which  o  >  1
is  used  can  be  seen  in  Lemmas  10  and  12.)  Throughout  the  proof,  r  will
belong  to  [l,  k)  (except  that  r  E  [l,  k]  in  Lemma  11).

Lemma  10  determines  the  result  of  0  -  ‘I’.  In  the  language  of  cards,  the
effect  of  this  sequence  of  shuffles  is  to  reverse  the  top  2’  cards,  and  each
consecutive  group  of  2’  cards,  in  place.

LEMMA  10.  If  O~a<v  and  Og/.3<2’,  then  (2’a+/l)O-‘I’=
2’a  +  (Zr  -  1 -  /3)  and  (2’a  +  p)‘O-  ‘I’  =  (2’a  +  (2’  -  1 -  j3))‘.

Proof:  When  r  =  1,  this  states  that  2a  +  2a  +  1  (for  p  =  0)  and
2a  +  1 +  2a  (for  fi  =  1).  Assume  inductively  that  r  >  1  and  O-r+‘Ir-’
behaves  as  indicated.  We  must  distinguish  between  the  cases p  =  2y  and
p  =  2y  -  1.
If  /3 =  2y,  then  2’-‘a  +  (2r-1  -  1 -  y)  <  2’-‘u  Q  in,  and

(2'a  +  #qo-'o-  r+lIr-lI  =  @-la  +  y)o-r+lp~

=  {2'-'a  +  (2r-1  -  1 -  y)}l

=  2{2'-'a  +  (2r-1  -  1  -  y)>( +  1

=  2'a  +  2'  -  1 -  /3.

184  DIACONIS,  GRAHAM,  AND  KANTOR

Similarly,  if  j3  =  2y  -  1, then  2’a  +  /I  is  odd,  2’-‘(a  +  1) G  in,  and

(2’a  +  /3)0-‘O-‘+‘I’-‘I

=  n-

1
 2’a  +  P  +  1  ‘o-r+lIr-lI
2  )

=  {n  -  2’-‘(a  +  1)  +  (2’-’  -  y)}‘O-‘+‘I’-‘I

=  {n  -  2’-‘(a  +  1)  +  2’-’  -  1 -  (2’-’  -  y)}‘l

=  2n  -  2  -  2{n  -  2’-‘(a  +  1)  +  y  -  l}

=  2’(a  +  1)  -  2y

=  2’a  +  2’  -  1 -  j3.  0

Lemma  11  determines  the  result  of  I’0  - ‘.  In  the  language  of  cards,  the
effect  of  this  sequence  of  shuffles  can  be  described  as follows:  with  the  deck
on  the  table,  cut  off  the  top  n/2’-’  cards  and  place  them  on  the  table.  Cut
off  the  next  n/2’-’  cards  and  place  them  on  the  original  top  group.
Continue  cutting  off  packets  of  size  n/2’-‘,  placing  them  on  the  cards
already  cut  off,  until  there  are  no  more  cards  left.

LEMMA  11.  If  r  E  [l,  k]  and  x  E  ((i  -  l)(n/2’-‘)  -  1, i(n/2’-‘)  -  l]
with  1  <  i  Q  2’-‘,  then

xI’O--‘=
1
-x-l+  +2i  -  1))’

a&x’I’O-’  =  -X  -  1  +  -32i  -  1).

Proof:  The  proof  is  again  inductive.  If  r  =  1  the  lemma  states  that

xIO-’  =  {-x  -  1 +  n}’  for  x  E(-1,  n  -  11.

Let  r  3  2.  We  must  distinguish  between  the  cases  x  E  [0,  fn)  and
x  E  [in,  n).
Let  x  E  [0,  fn).  Then  XI  =  2x+  1 E  ((i-l)(n/2’-2)-1,  i(n/2’-2)-  11
and
 XII’  - ‘0  -  r+‘o-’  =  (  -  (2x  +  1)  -  1 +  -32’  -  1))‘0-1

1
(  [ z  -2x-2+”  1  I =  2r-2  (2’  - o]) .

PERFECT  SHUFFLES  185

Next,  let  x  E  [in,  n),  so  that  xl  =  (2n  -  2x  -  2)’  and

-i-+  +  1 d  -  (2x  +  1)  <  -  (i  -  1)s  +  1,

2n-in  2r-2  d  x’I  <  2n  -  (i  -  l)- 2r-2’

(2’-’  -  i)*  -  1 <  x’I  <  (2’-’  -  i  +  1)--11  -
2r-2  1.

Thus,
xII-‘+‘o’-‘o-’

=  -  (2n  -  2x  -  2)  -  1  +  -+{2(2r-1  -  i  +  1)  -  l}]O-’

=  t  [
n  -  +  -  (2n  -  2x  -  2)  +  L(2’  -  2i  +  I)])  ’
2r-2

=  t  -x-1+-  :  --&(2i  -  1))‘.  0

LEMMA  12.  Set  b  =  (IkOek  * I-‘O)-2.  Then  b  induces

(WA...,  2u  -  2)(2u  -  1,2u  -  3,..  .)  3,1)

on  [0,2u),  and  (x  +  2u)b  =  xb  +  2u  whenever  x,  x  +  2u  E  [0,  n).  In  pur-
titular,  b has  order  u.

Proof:  Recall  that  u  =  n/2k-‘.  Let  x  E  [(i  -  l)u,  iv).  By  Lemma  11

x’IkOek  =  -x  -  1  +  u(2i  -  1)  E  [(i  -  l)u,  iu).

If  x  is  even,  then
 x’IkOpk.  I-‘0  =  -x  +  u(2i  -  1).

If  x  is  odd,  then
 x’IkO  - k  .  I-‘0  =  -x  -  2  +  u(2i  -  1).

Thus,  x’I~O-~I’O  E  [(i  -  l)u,  iu)  unless  -x  +  u(2i  -  1) =  iv  and  x  is
even,  or  -x  -  2  +  u(2i  -  1)  =  (i  -  1)~  -  1 and  x  is  odd.  Excluding  these
cases, we find  that

xb -’  =  -  {-x  +  u(2i  -  1))  -  2  +  u(2i  -  1)  =  x  -  2  if  x  is  even,

xb  -I  =  -  {-x  -  2  +  u(2i  -  1))  +  u(2i  -  1)  =  x  +  2  ifx  isodd.

186  DIACONIS,  GRAHAM,  AND  KANTOR

Finally,  if  x  =  (i  -  1)~  is  even,  then

xb  -’  =  -  {-x  +  u(2i  -  1))  -  2  +  u(2i  +  1)  =  x  +  (2u  -  2)

while  if  x  =  iv  -  1 is  odd,  then

xb-’  =  -  {-x  -  2  +  u(2i  -  1))  +  u(2i  -  3)  =  x  -  (20  -  2).  0

LEMMA  13.  Set  c:  =  born’.  Then  c  induces  (0,1,2,.  . . , u  -  1)  on  [0,  u),
and  (x  +  u)c  =  xc  +  u  wherzeuer x,  x  +  u  E  [0,  n).

Proofi  Since  b  induces  (2iu,  2iu  +  2,.  . . ,  2iu  +  2u  -  2)  on  the  even
integers  in  [2iu,  2iu  +  2u),  c  acts  as indicated  on  [0,  in).  Also

((2iu  +  2u  -  l)‘,  (2iu  +  20  -  3)‘,.  . . ,  (2iu  +  3)‘,  (2iu  +  l)‘)O-’
=  (n-iv-u,n-iu-u+  l,...,n-iu-2,n-iu-  1).  0

Notation.

h(r):  =  O-1’  forr  E  [l,  k),

h:  =  b(l),

H  =  H(1):  =  (b,  c,  h)  withbandcasinLemmas  12and  13,

H(r):  =  (H(r  -  l),  h(r))  forr  E  (1,  k).

LEMMA  14.  If  g  E  H(r),  then

[0,2’u)g  =  [,0,2’u)  and  (x  +  2’u)g  =  xg  +  2’0

whenever  x,  x  +  2’  E  [0,  n).  In  particular,  H(r)  c  G*.

Proof.  This  follows  immediately  from  Lemmas  10,  12,  and  13.  0

LEMMA  15.  If  u  >  3,  then  H  induces  S,,  on  [0,2u).

Proof:  We  will  write  elements  of  H  as permutations  of  [0,2u).  Then

b  =  (0,2,4  ,...,  2u  -  2)(2u  -  1,.  . .)  3,  l),

c=(o,1,2  ,...)  u  -  l)(u,  0  +  1,.  . .)  2u  -  l),

h  =  (01)(23)...(u  -  3,u  -  2)(u  -  l,u)(u  +  l,u  +  2)...

X  (2~  -  4,2u  -  3)(2u  -  2,2u  -  1).

Note  that  h  is  an  odd  permutation  (of  [0,2u)).
We  will  exhibit  a  3-cycle.  We  have

hc2=(23)...  (u-  l,O)(l,u+2)(~+3,~+4)...

x  (2u  -  2,2u  -  l)(u,  0  +  1)

PERFECT  SHUFFLES

so that  (since  o  &  5)
 187

d:=  hh”  =  (0,  u  +  2,  u)(l,  2, -  1, B  +  1).

Then
 d’  =  (1,  u  +  3,  u  +  1)(2,0,  u  +  2),

e:=  ddc  =  (u  +  2,2,  u)(u  +  3,  u  -  1,  l),

f:=  eb  =  (u,4,  u  -  2)(u  +  5,  u  +  1,2u  -  l),

ef  =  (u  +  2,2,4)(u  +  3,  u  -  1, l),

e-‘ef=  (u  +  2,  u,4).

The  connectedness  of  the  set  of  3-cycles  in  H  is  easily  checked.  Thus,
Lemma  7  applies.  0

LEMMA  16.  If  r  <  k  -  1  and  H(r)  induces  at  least  A,,,  on  [0,2’u),  then
H(  r  +  1)  induces  at  least  A2,+lo  on  [0,2’+‘u).

Proof:  We  will  restrict  all  permutations  to  [0,2’+  ‘u).  By  hypothesis  and
Lemma  14,  H(r)  contains

t  =  (012)(2’u,2’u  +  1,2’u  +  2).

By  Lemma  10,  since  2%  =  2’(u  -  1) +  2’  we have

th(r+l)  =  (y+’  -  1,2’+1  -  2,3+1  -  3)(2’(u  -  1)  +  2’-  1,2’(u  -  1)

+2’  -  2,2’(  u  -  1)  +  2’  -  3)

(if  r  =  1, replace  2’(  u  -  1) +  2’  -  3 by  2( u  +  1) +  2’+’  -  1). Let  g  E  H(r)
fix  the  last  5  points  appearing  above  in  t”(‘+  ‘)  and  send  2’+  ’  -  1 to  2’+‘.
Then
 tw+  y  tw+  I’)-  ’  =  (y+  1,2’+  1 -  1,2r+  1 _  3).

Conjugating  by  elements  of  H(r),  and  by  h(r  +  l),  we  obtain  enough
3-cycles  to  deduce  the  connectedness  of  the  set  of  3-cycles  in  the  action  of
H(r  +  1) on  [0,2’+‘).  •I

LEMMA  17.  If  u  >  3,  then  G*  3  A,.

Proof.  This  follows  from  Lemmas  15  and  16  since  H(k  -  1) induces  at
least  A,,  on  [0, 2k-~u).  •I
LEMMA  18.  If  u  =  3 and  k  &  4,  then  G*  2  A,,.

188  DIACONIS,  GRAHAM,  AND  KANTOR

Proof:  Restricting  H(3)  to  [0,23  - 3),  we  obtain  the  subgroup  of  S,,
generated  by  the  permutations

b=  (024)(6810)(121416)(182022)(531)(1197)(171513)(2321  19);

c=(012)(345)(678)(91011)(121314)(151617)(181920)(212223);

h(1):  2x  @  2x  +  1;

h (2)  : (  4x4;r  ;$4;  :‘2;

8x  -  8x  +  7,
h(3).
 1

8x+  1  ++8x+6,
*  8x+2*8x+5,
8x  +  3  -  8x  +  4.

A  computer  calculation  shows that  these  generate  A,,  indeed  b,  c, and  h(3)
generate  A,.  (It  may  be  of  interest  to  observe  that  b,  c,  and  h(2)  generate
M,,  .) Now  Lemma  16  applies.  0
Completion  of  Proof:  We  may  assume  that  2n  is  not  a  power  of  2,  and
that  2n  *  12,24.  By  Lemmas  17,  18,  and  8,  G*  3  A,  and  llyl  2  2”-‘.
If  n  =  0  (mod4),  then,  by  Lemma  6(a),  c  =  A,  and  IGI  d  2”-‘IA,,l.  Thus,
(d)  holds.
If  n  =  2  (mod  4),  then,  by  Table  III,  c  =  S,.  Also  by  Table  III,  0  is  odd
while  0  is  even.  Let  g  E  G*  with  g  =  0.  Then  g0  -’  is  an  odd  element  of
K.  As  in  Lemma  9,  the  proof  of  Lemma  8  yields  that  llyl  =  2”,  as required.
0

3.  SOME  HISTORY  OF  THE  PERFECT  SHUFFLE

There  are  early  descriptions  of  the  perfect  shuffle  in  books  on  cheating  at
cards.  The  first  description  we  can  find  is  on  p.  91  of  the  anonymously
authored  “Whole  Art  and  Mystery  of  Modem  Gaming,”  Roberts,  London,
1726.  The  earliest  American  reference  to  perfect  shuffles  we can  locate  is  in
J.  H.  Green’s  book  “An  Exposure  of  the  Arts  and  Miseries  of  Gambling,”
James,  Cincinnati,  1843.  On  p.  195  he  described  a method  of  cheating  at  the
game  of  Faro  which  used  the  perfect  shuffle,  calling  it  “running  in  the
cards.”  Green  remarked  that  the  method  was a recent  invention.  The  perfect
shuffle  is  currently  called  the  Faro  shuffle  in  magic  circles.  It  is  still  widely
used  as a method  of  cheating  at  card  games  such  as gin  rummy  and  poker.
A  detailed  description  of  several  uses of  the  perfect  shuffle  for  cheating  at
Faro  can  be  found  in  the  anonymously  authored  book  “A  Grand  Expose  of
the  Science  of  Gambling”  Brady,  New  York,  1860.  An  illustrated  descrip-
tion  of  the  technique  is  on  pp.  204-205  of  J.  N.  Maskelyne’s  book  “Sharps
and  Flats,”  Longmans  Green  and  Co.,  London,  1894.

PERFECT  SHUFFLES  189

The  shuffle  was introduced  to  magicians  in  a brief  note  in  C.  T.  Jordan’s
classic  “Thirty  Card  Mysteries,”  published  by  the  author  in  Pengrove,
Calif.,  1919.  In  a  trick  called  the  Full  Hand,  on  pp.  17-  19,  he  used  the
principle  that  a  16  card  packet  out  shuffled  4  times  returned  to  its  original
order.  He  mentioned  that  5  out  shuffles  suffice  for  32  cards  and  that  T.
Nelson  Downs,  a  famous  American  manipulator,  could  do  similar  things
with  52  cards.
It  is  through  Downs  that  we have  any  record  of  a skillful  early  practioner
of  the  perfect  shuffle:  Fred  Black,  a  rancher  from  Thedford,  Nebraska.
Black  worked  out  the  mathematics  of  repeated  out  shuffles  of  52  cards  in
some  detail.  Downs  reported  meetings  with  Black  in  1924.  These  letters  are
reprinted  in  the  magic  journal,  The  Linking  Ring,  April  (1971),  53-83  and
May  (1971),  67-68;  72-73.  Dai  Vernon  knew  Black  and  said  that  he  used  to
practice  shuffling  on  horseback.  The  charts  Black  worked  out  depicting
some  of  the  group  structure  of  out  shuffles  appeared  first  in  Hugard  and
Braue’s  “Expert  Card  Technique,”  Chap.  16. These  charts  record  facts  like:
cards  18  and  35  repeatedly  interchange  during  repeated  out  shuffles;  the
deck  breaks  up  into  groups:  top,  bottom,  {18,35),  6 “belts”  of  8 cards  which
are  permuted  among  themselves,  etc.
The  modem  era  for  perfect  shuffles  in  magic  begins  in  1957  when  J.
Russell  Duck,  a  Pennsylvania  policeman,  published  the  basic  central  sym-
metry  principle,  calling  it  “stay-stack’,  in  the  first  issue  (Feb.  1957)  of  the
privately  published  journal  Curdiste.  At  about  the  same  time,  Alex  Elmsley,
a  computer  specialist  living  in  London,  began  to  publish  a  series  of  tricks
based  on  the  perfect  shuffle.  In  the  privately  published  card  magazine
Ibidem  (No.  11,  Sept.  1957),  he  established  the  binary  procedure  for
bringing  the  top  card  to  any  position  (Lemma  2).  In  a  series  of  articles  in
the  English  magic  journal  Pentugrum  11  (1957),  he  set  out  the  basic
mathematics  for  decks  of  general  size,  discovering  in  particular  the  impor-
tance  of  the  order  of  2 mod(2n  f  l),  and  the  connection  with  Fermat’s  little
theorem.
While  many  new  tricks  based  on  Faro  shuffles  have  appeared  in  the
magic  literature  in  recent  years,  few  new  properties  have  emerged.  (Our
theorem,  in  a  sense, explains  this.)  A  scholarly  manuscript  by  Ronald  Wohl,
a  Swiss chemist,  completed  in  the  early  1960s  has  recently  been  published,
in  part,  in  Ibidem,  No.  36.  In  two  books,  “Far0  Fantasy”  and  “More  Faro
Fantasy,”  Paul  Swinford  discovered  that  with  a deck  of  2k  cards,  the  shuffle
sequence  (in  Lemma  2)  that  brings  card  x  to  position  y  also  brings  the  card
at  y  to  position  x.  Swinford  (private  communication)  also  discovered  the
method  for  bringing  a card  at  x  to  position  y  for  2k  cards.  There  are  a large
number  of  recent  articles  on  the  Faro  shuffle.  Two  excellent  books  by
Edward  Marlo,  “The  Faro  Shuffle”  and  “Far0  Notes,”  Ireland  Magic
Company,  Chicago,  are  currently  sold  in  magic  shops.

190  DIACONIS,  GRAHAM,  AND  KANTOR

TABLE  IV
Cycle  and  Type  for  Out  Shuffles  of  64  Cards

cydc  nv

(0)  (0)

(1,2,48,16,32)  (000001)

(3,6,12,24,48,33)  (000011)

(5.10,20,40,17,34)  (000101)

(7.14,28,56,49,35)  (000  1 11)

(9.18,36)  (00  1)

(11,22,44,25,50,37)  (001011)

(13,26.52,41.19,38)  (001101)

(15.30,60,57,51,40’)  (001  11  1)

(21.44)  (011)

(23,46,29,58,43)  (010111)

(27,54,45)  (011)

(31,62,61,59,55,47)  (lQOOO0)

(63)  (1)

There  has  been  some  mathematical  work  on  perfect  shuffles.  P.  Levy
wrote  a  sequence  of  papers  on  them  in  1940-1950.  These  papers  (Levy
[ 13-  181) are  together  in  Vol.  6  of  Levy’s  collected  works.  Levy’s  motivation
for  working  on  these  shuffles  is  charmingly  described  in  his  autobiography
[19,  pp.  151-1531.  Since  Levy’s  work  seems  unknown,  a  brief  description  is
presented.  Throughout,  a deck  of  size 2n  is  assumed.  We  give  results  for  out
shuffles.  Levy  defined  the  type  of  a  cycle  in  the  cycle  decomposition  of  an
out  shuffle  as follows:  suppose  a  card  at  position  j,  goes  through  positions
j,,  j2,...,  j,,  in  successive out  shuffles.  The  type  of  the  cycle  (j,,  j,,  . . . , j,)  is
a  binary  vector  of  length  u  with  a  zero  in  the  i th  position  if  and  only  if
0  Q ji  G  n.  Table  IV  lists  the  cycle  and  type  decomposition  for  a  deck  of  64
cards.  Levy  proved  that  all  cycles  have  distinct  types.  When  n  =  2k  he
showed  that  all  types  occur  if  the  following  conventions  are  made:  two  types
that  differ  by  a  cyclic  shift  are  equivalent.  Call  a  type  imprimitiue  if  it  is
made  up  of  repetitions  of  a single  shorter  type.  (For  64  cards,  (0  0  0  0  0  0)
(0  0  1  0  0  1) (0  1  0  1  0  l)(l  1  0  1  1  0) (1  1  1  1  1  1) are imprimitive.)

PERFECT  SHUFFLES  191

Only  the  shorter  types  appear  for  an  imprimitive  type.  F.  Leighton  has
pointed  out  that  the  type  result  just  stated  is  equivalent  to  the  repre-
sentation  of  an  out  shuffle  as  a  shift  operating  on  Z,“,  as  in  the  proof  of
Lemma  4.
A  primitive  type  is  “born”  at  k,  if  it  occurs  in  a deck  of  k,  cards  and  for
no  smaller  deck.  Levy  showed  that  if  a  type  is  born  at  k,,  then  it  appears  in
a  deck  of  size  k  if  and  only  if  k  =  k,  +  2(k,  -  l)j,  j  =  0,  1,2,.  . .  .  For
example,  since  a  2-cycle  appears  for  the  first  time  with  k,  =  4  cards  it
follows  that  decks  of  size k  =  4  +  6j  have  2-cycles.  Levy  proved  that  for  a
fixed  k,  all  the  new  born  types  are  of  the  same  length  u.  This  u  is  the  order
of  2  (mod  k  -  1). Levy  gave  a number  of  other  results.
Golomb  [9]  considered  the  group  generated  by  out  shuffles  and  cuts.  He
showed  that  these  operations  generate  all  permutations.  He  also  gave  results
for  a  deck  of  size  2n  -  1. One  implication  of  his  results  is  that  in  and  out
shuffles  of  an  odd-sized  deck  generate  a very  small  group.  (Here,  in  and  out
shuffles  correspond  to  the  two  ways of  cutting  a  deck  into  two  parts  of  size
n  and  n  -  1. The  out  shuffle  leaves  the  top  card  on  top,  while  the  in  shuffle
leaves  the  bottom  card  on  bottom.)

THEOREM.  The  order  of  the  shuffle  group  for  a  deck  of  2n  -  1  cards  is
(2n  -  1) X  order  of  2  mod(2n  -  1).

Proof:  Let  c be  the  operation  of  cutting  the  top  card  to  the  bottom.  It  is
easy  to  see that  an  out  shuffle  followed  by  c is  the  same  as an  in  shuffle.  It
follows  that  (0,I)  =  (0,  c).  The  order  of  the  latter  group  was shown  to  be
(2n  -  1) X  order  of  2 (mod(2n  -  1))  by  Golomb.  0

In  fact,  if  the  cards  are  labeled  using  [0,2n  -  l),  then  x0  =  2x  (mod  2n
-  l),  xl  =  2x  +  1  (mod2n  -  l),  and  the  cut  c  is  given  by  xc  =  x  +  1
(mod  2n  -  1). The  order  of  (0,  c)  is  easily  found  using  the  identity  co  =  c2
observed  by  Golomb.  In  terms  of  0  and  I  =  Oc  this  asserts  that  I0  =

to-1  . ’  I-’  The  magical  properties  of  perfect  shuffles  of  odd-sized  decks  are
discussed  at  length  in  Gardner  [8,  Chap.  lo].

4.  APPLICATIONS  OF  PERFECT  SHUFFLES  TO  PARALLEL
PROCESSING  ALGORITHMS

Both  types  of  perfect  shuffles  and  their  combinations  have  been  applied
to  computer  algorithms.  Some  references  are  Stone  [25],  Schwartz  [23],  and
Chen  et  al.  [4].  For  a  simple  example,  due  to  Stone,  consider  computing  the
transpose  of  a  2”  X  2m  matrix.  Suppose  that  the  matrix  is  stored  in  a  22m
linear  array  in  row  major  order.  For  a  4  x  4  matrix  this  is

aooao1a02a03a10a11a12L113c120a21a22a23a333.  It  is  easy  to  verify  that

192  DIACONIS,  GRAHAM,  AND  KANTOR

after  m  out  shuffles  the  array  is  in  column  major  order,  and  so  transposed.
In  the  4  X  4  example  this  is  a  a  a  a  a  a  a  a  a  a  a  a  a 00  10  20  30  II  21  31  12  32  03  13  23  33’
Out  shuffles  are  performed  by  network  connection  patterns  like  the
example  in  Fig.  1 in  which  2  sets of  8  registers  are  connected.  Often  an  out
shuffle  connection  is  combined  with  an  array  of  simple  processors  (Fig.  2).
If  the  processors  P  take  two  input  numbers  and  output  their  sum  (Fig.  3)
then,  after  m  iterations  of  a  network  with  2”  registers,  all  registers  will
contain  the  sum  a,  +  a,  +  - . -  +  a2,,,  _ ,.  If  the  processors  output  other

0  0

1  4

2  1

3  5

4  2

5  6

6  3

7  7

FIGURE I

FIGURE 2

FIGURE 3

PERFECT  SHUFFLES  193

suitably chosen linear  combinations the result of m iterations is the  discrete
Fourier  transform  Zujwjk.  In  a  more  complex  application  the  processors
output  the  sorted  pair  (ai,  uj).  This  yields  an  algorithm  that  sorts  2”
numbers  in  0(  m2)  iterations.  See Brock  et al.  [3]  for  further  discussion.
It  should  be  emphasized  that  these  applications  mostly  amount  to  the
“out”  part  of  the  proof  of  Lemma  4.  Namely,  when  0  is  used  on  a  deck  of
size  2”  it  cyclically  shifts  the  digits  in  the  binary  expansion  of  each  integer
in  [0,2”).
As  a  simple  new  example,  we  mention  the  fact  that  an  array  of  2”
numbers  is  brought  into  reverse  order  by  m  in  shuffles.  Other  length  arrays
may  also  be  reversed;  for  length  52,  26  in  shuffles  suffice.  In  general,  an
array  of  length  2n  reverses  after  j  in  shuffles,  where  i  is  the  smallest
exponent  such  that  2j  =  -  l(mod2n  +  1).  In  shuffles  cannot  always  be
called  upon  to  reverse  an  array  of  length  2n.  For  example,  if  2n  =  2”  -  2,
the  order  of  2  (mod2n  +  1) is  m  and  2j  g  -  1 (mod2n  +  1)  for  any  j.  A
simple  corollary  of  the  main  theorem  is  that  an  array  of  length  2n  can  be
reversed  by  some  combination  of  in  and  out  shuffles  if  and  only  if  n  =  0,  1, or  2
(mod4).  Indeed,  if  z  denotes  the  permutation  reversing  the  position  of  2n
symbols,  sgn z  =  (-  l)“,  sgn Z  =  1, now  apply  Lemma  5  and  the  theorem.
As  an  example,  if  2n  =  10,  the  sequence  IO  0  IO  0  0  0  0  yields  z.  We  do
not  know  a  simple  algorithm  for  determining  a  minimal  length  sequence  for
general  n.
 5.  GENERALIZATIONS  AND  VARIATIONS

In  and  out  shuffles  are  related  to  the  so-called  “milk”  and  “Monge”
shuffles.  The  milk  shuffle  can  be  described  as  a  permutation  on  m  cards
labeled  0,  1, . . . , m  -  1  as  follows.  The  card  labeled  j  (and  initially  in
position  j)  is  moved  to  position  125’1, where  1x1 denotes  the  unique  y,
0  G  y  G  m,  such  that  y  =  f  x  (mod  2m  -  1).  Thus,  after  one  milk  shuffle,
the  deck  now  has  the  order  0,  m  -  1, 1, m  -  2,2,.  . . .  This  permutation  is
easily  performed  on  a  deck  of  cards.  Remove,  or  “milk,”  the  cards  at  top
and  bottom  simultaneously  and  place  them  on  the  table.  Then  milk  off  the
second  pair  from  the  top  and  bottom  and  place  them  on  top  of  the  first
removed  pair.  Continue  this  process  until  no  cards  remain.  Basic  properties
of  the  milk  shuffle  were  given  by  Levy  in  the  papers  cited  in  the  bibliog-
raphy.  Levy  [18]  showed  that  the  results  he  proved  for  milk  shuffles  had
easy  translations  into  corresponding  results  for  out  shuffles.  A  useful
connection  between  the  two  shuffles  is  the  following  observation  due  to
John  Conway.  The  permutation  of  the  pairs  3  in  an  out  shuffle  of  2m  cards
is just  a  milk  shuffle  of  the  m  symbols  X0,  Z,,  . . . ,  Tm _ ,.  The  inverse  of  the
milk  shuffle  was actually  analyzed  by  Monge  in  1773  (see Ball  and  Coxeter
[ 11). In  fact,  there  are  two  types  of  “Mange”  shuffles,  which  we will  call  the

194  DIACONIS,  GRAHAM,  AND  KANTOR

“up”  shuffle  and  the  “down”  shuffle.  For  the  up  shuffle,  successive  cards
are  removed  from  the  top  of  the  deck  and  placed  alternatively  on  the  top
and  the  bottom  of  the  new  stack  (with  the  second  card  being  placed  on  top
of  the  first).  For  the  down  shuffle,  the  same  procedure  is  followed  except
that  the  second  card  is  placed  below  the  first.  In  particular  the  order  of  a
milk  shuffle  of  m  cards  is  the  order  of  an  out  shuffle  of  2m  cards:  the  order
of  2 (mod  2m  -  1).  Symbolically,  for  a deck  of  m  cards,  the  up  shuffle  sends
a  card  originally  in  position  j  to  position  [m/2]  +  (-  l)‘[(i  +  1)/2].  Note
that  a  down  shuffle  is  actually  just  an  up  shuffle  followed  by  a  “reversal”
shuffle  z,  i.e.,  z(j)  =  m  -  1 -  j.  It  follows  from  what  we have  noted  that
the  group  (u,  d)  of  permutations  generated  by  up  and  down  shuffles  on  m --
cards  is  exactly  (I,  0)  acting  on  (pairs  of)  2m  cards.  In  particular,  since
(u,  d)  =  (u,  z),  it  follows  that  for  m  =  2  (mod  4)  (u,  z)  z  S,,, while  for
m  =  12,  (u,  z)  Z  M,*.  Borcherds  et  al.  [2]  have  used  this  fact  in  order  to
relate  two  different  bases  for  the  Leech  lattice.
Levy  also  mentioned  a  curious  connection  between  the  milk  shuffle  and
the  down  and  under  shuffle.  This  shuffle  successively  places  the  top  card  on
the  table,  the  next  card  under  the  deck,  the  next  card  on  (top  of  the  card
on)  the  table,  and  so on.  Let  E  be  the  set  of  integers  with  the  property  that
the  milk  shuffle  and  the  down  and  under  shuffle  have  the  same  cycle
structure  (and  in  particular  the  same  order).  Levy  showed  that  n  E  E  if  and
only  if  2n  -  1  divides  a  number  of  the  form  2’  +  1.  For  example,  a  milk
shuffle  with  5 cards  labeled  01234  gives  the  permutation

0  1  2  3  4
0  2  4  3  1.

A  down  and  under  shuffle  gives  the  permutation

0  1  2  3  4
0  4  1  3  2.

Both  permutations  have  one  3-cycle  and  two  fixed  points,  and  2n  -  1 =  9
which  divides  23 +  1. A.  M.  Odlyzko  has  shown  that  E  is  small  in  the  sense
of  density:  the  number  of  elements  in  E  smaller  than  x  is  asymptotic  to
C~/m3  x) ‘I3  for  an  explicit  constant  c.  The  down  and  under  shuffle  is
thoroughly  studied  under  the  name  of  the  Josephus  permutation  (see
Herstein  and  Kaplansky  [ 111). The  milk  shuffle  is  described  and  applied  in
early  books  on  card  cheating.  For  example,  the  anonymously  authored  book
“Whole  Art  and  Mystery  of  Modern  Gaming”  (London,  1726)  contains  a
description  of  several  methods  of  cheating  at  the  card  game  of  Faro  that
make  use of  milk  shuffles.
A  simple  way  to  achieve  an  inverse  in  or  out  shuffle  is  to  deal  a  deck  of
cards  into  two  face-up  piles  alternatively.  Place  one  pile  on  the  other,  and

PERFECT  SHUFFLES  195

turn  the  deck  face down.  This  suggests  a  generalized  perfect  out  shuffle:  for
a deck  consisting  of  a  .  b  cards,  deal  a  face-up  piles  and  gather  the  piles  so
that  the  original  top  card  remains  on  top.  This  shuffling  operation  arises
naturally  in  circuit  applications  such  as  the  final  shuffling  in  the
Cooley-Tukey  algorithms  for  the  discrete  Fourier  transform.  Davio  [6]
contains  a  nice  discussion  of  this  and  other  examples.  One  application
involves  the  noncommutativity  of  tensor  products.  If  the  permutation
matrix  of  the  generalized  out  shuffle  is  denoted  S,, b and  if  m,  and  m,  are
(r,,  c,)  and  (ra,  cO) matrices,  then  Davio  [6]  showed  that

Morris  and  Hartwig  [22]  have  determined  properties  of  generalized  out
shuffles  and  generalized  out  shuffles  and  cuts;  they  also  proved  a  special
case of  the  above  formula  (when  r,  =  c,  and  r0 =  c,,).  We  observe  that  it  is
also  possible  to  define  generalized  in  shuffles  by  picking  up  the  piles  in  the
opposite  order.  Both  generalized  in  and  out  shuffles  preserve  central  sym-
metry;  it  would  be  interesting  to  know  what  group  these  generate.  Going
further,  if  a  . b  cards  are  dealt  into  a  piles  with  b  cards  in  each  pile,  there
are  a!  possible  ways of  picking  up  the  piles,  and  this  leads  to  more  questions
of  the  same  sort.
 ACKNOWLEDGMENTS

This  paper  makes heavy use of computational  results generated  by Eric  Hamilton  in  a course
at  Stanford  taught  by  Don  Knuth.  The  calculations  leading  to  M,,  and  a crucial  computer
check required  in  the proof  of the main  theorem  were  carried  out  by Lyle  Ramshaw  at Xerox
PARC.  Rob  Calderbank  and  Neil  Sloane  provided  the  first  corroboration  that  for  n  =  12,
c  =  M,,.  A.  M.  Odlyzko  produced  the difficult  estimate  in  Section  5. We  thank  them  all  for
their  help.
 REFERENCES

1. W. W.  R. BALL  AND H.  M.  S.  COXETER, “Mathematical  Recreations  and  Essays,”  12th  ed.,
University  of Toronto  Press, Buffalo,  1974.
2.  R.  BORCHERDS, J.  H.  CONWAY, L.  QUEEN,  AND  N.  J.  A.  SLOANE, “A  Monster  Lie
Algebra?”  Technical  Report,  Bell  Laboratories,  Murray  Hill,  N.J.,  1982.
3.  H.  K.  BROCR, B.  J.  BROOKS, AND F.  SULLIVAN, Diamond,  a  sorting  method  for  vector
machines,  BIT  21(1981),  142-152.
4.  P.  Y.  CHEN, D.  H.  LAWRIE, P.  C.  YEW, AND D.  A.  PODERA, Interconnection  networks
using  shuffles, Computer,  December  (198 I),  55-64.
5.  H.  M.  S. COVETER, “Regular  Polytopes,”  Methuen,  London,  1948.
6.  M.  DA~IO,  Kronecker  products  and  shuffle  algebra,  IEEE  Trans.  Comput.  C-30  (1981)
116-125.

196  DIACONIS,  GRAHAM,  AND  KANTOR

7.  M.  FURST, J.  HOPCROR,  AND  E.  Luxs,  Polynomial-time  algorithms  for  permutation
groups,  in  “Proc.  21st FOCS,”  pp.  36-41,  1980.
8.  M.  GARDNER,  “Mathematical  Carnival,”  Knopf,  New  York,  1975.
9.  S. W.  GOLOMB, Permutations  by cutting  and  shuffling,  SIAM  Rev.  3  (1961),  293-297.
IO.  R.  E.  HARTWIG  AND  S. B.  MORRIS, The  universal  flip  matrix  and  the  generalized  Faro
shuffle,  Pacific  J.  Math.  58  (1975),  445-455.
Il.  I. N.  fhCXEIN  AND  I.  KAPLANSKY,  “Matters  Mathematical,”  Harper  &  Row,  New  York,
1974.
12.  D.  KLEITMAN,  F.  LEIGHTON,  M.  LEPLEY,  AND  G.  MILLER,  “New  Layouts  for  the
Shuffle-Exchange  Graph,”  Technical  report,  Applied  Mathematics  Department,  MIT.,
Cambridge,  Mass.,  1980.
13.  P. LEW,  Etude  dune  classe de permutations,  C.  R.  Acad.  Sci.  227  (1948),  422-423.
14.  P.  LEW,  Etude  dune  nouvelle  classe de  permutations,  C.  R.  Acad.  Sci.,  227  (1948),
578-579.
15.  P. LEW,  Sur  dew  classes de  permutations,  C.  R.  Acad.  Sci.  228  (1?49),  1089-1090.
16.  P. LEW,  Un  problem  de  la  theorie  des permutations,  in  “Conf.  Ecole  Polyt.,”  May  24,
1949.
17.  P. LEW,  Sur  une classe remarquable  de permutations,  Bull.  Acad.  Roy.  Belgique  2  (1949).
361-377.
18. P. LEW,  Sur  quelque  classes de permutations,  Compositio  Math.  8  (1950),  l-48.
19. P. LEW,  “Quelques  aspects de la  pensee d’un  mathematician,”  Blanchard,  Paris,  1970.
20.  S. B.  MORRIS, “Permutations  by Cutting  and  Shuffling-A  Generalization  to  Q-Dimen-
sions,”  Ph.D.  dissertation,  Department  of Mathematics,  Duke  University.  Published  under
the same title  by Micky  Hades, Box  476, Calgary,  Alberta,  Canada.
21.  S. B. MORRIS, The  basic mathematics  of the Fare  shuffle, Pi  Mu  Epsilon  J.  6  (1975),  85-92.
22.  S. B. Mows  AND  R. E. HARTWIG, The  generalized  Faro  shuffle, Discrete  Math.  15 (1976),
333-346.
23.  J.  T.  SCHWARTZ,  Ultracomputers,  ACM  Trans.  Program.  Language  Systems  2  (1980),
484-521.
24.  C.  C.  SIMS, Computational  methods  in  the  study  of  permutation  groups,  in  “Computa-
tional  Problems  in  Abstract  Algebra,”  Proc.  Conf.,  Oxford,  1967 (John  Leech,  Ed.),  pp.
169- 183, Pergamon,  Oxford,  1970.
25.  H.  S.  STONE,  Parallel  processing  with  the  perfect  shuffle,  IEEE  Trans.  Comput.  2  (1971),
153-161.
26.  J.  V.  USPENSKY  AND  M.  A.  HEASLET,  “Elementary  Number  Theory,”  McGraw-Hill,  New
York.  1939.
