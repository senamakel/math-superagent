<!-- source: https://ir.cwi.nl/pub/6822/6822D.pdf | converted from PDF -->

stichting

mathematisch

centrum

AFDELING  ZUIVERE  WISKUNDE
(DEPARTMENT  OF  PUR~  MATHEMATICS)

H.A.  WILBRINK  & A.E.  BROUWER
 zw  121/78

A (57,14, 1)  STRONGLY  REGULAR  GRAPH  DOES  NOT  EXIST
 ~
MC

DECEMBER

2e boerhaavestraat  49  amsterdam

Punted  a.:t  t;he.  Ma.:the.ma.:Uc.ai.  Ce.nvz.e.,  49,  2e.  BoeJr..haave1>:tJta.a;t,  Am.6t;e/l.dam.

The.  Ma.:the.ma.:Uc.ai.  Ce.ntlr.e.,  6ounde.d  t;he.  11-t;h  06  Fe.b1tu.a1ty  1946,  ,if,  a.  non-
p1to6U  .ln6.tA..:ti.Ltion  cum.lng  a.:t  t;he.  p1tomotion  06  pUILe.  ma.:the.ma.:UC6  a.nd  .l.t6
a.ppUc.a.:Uon6.  It;  ,if,  .6pon601te.d  by  t;he.  Ne.the/t£.a.nd6  Gove.Jtnme.nt  fuough  t;he.
Ne.theJll.a.nd.6  OJtga.n.lza.:Uon  601t  t;he.  Advruic.e.me.nt  06  PU/Le.  Re1>e.a.1tc.h  (Z.W.0).

AMS(MOS)  subject  classification  scheme  (1970):  05B30

A  (57,14,1)  strongly  regular  graph  does  not  exist

by

H.A.  Wilbrink  &  A.E.  Brouwer

ABSTRACT

We  show  that  a  strongly.regular  graph  with  parameters

n  =  57,  k  =  14,  A=  1,  µ  =  4

(  (0,1)-eigenvalues:  1*14,  38*2,  18*(-5);
(1,-1)-eigenvalues:  1*28,  38*(-5),  18*9)  does  not  exist.

KEY  WORDS  8,  PHRASES:  Strongly  regular  graph.

I •  TWO  LEMMAS

LEMMA  I.  Let  G be  a  strongZy  reguZar  graph  with  parameters  n,k,A,µ.  Let  H be
an  induced  subgraph  with  N points,  M edges  and  degree  sequence  d 1, ••• ,dN.
Then
 (kN- 2M)  - (AM+  µ((~)  - M)  - I (~i))  ~  n  - N
i=l

and  equaZity  hoZds  iff exactiy  (kN- 2M)  - (n- N)  points  in  G\H  are  adjacent
to  preciseZy  two  points  of H,  whiZe  the  remaining  points  in  G\H  are  adjacent
to  preciseZy  one  point  of H.

PROOF.  Let  there  be  x.  points  in  G\H  adjacent  to  i  points  of  H.  We  have
1.
Ix.
1.  =  n- N,

I  ix.
1.  = kN- 2M,

N  N  d
( (  )  )  \  (  2i). =  AM+µ  2  - M  - l
i=l

LEMMA  2.  Let  G be  a  strongZy  reguZar  graph  with  parameters  n,k,A,µ.  Lets

D

be  the  smaZZest  eigenvaZue  of the  (O,l)-adjacency  matrix  of G,  i.e.,  the
negative  root  of the  equation  x 2  +  (µ-A)x  +  µ-k  =  O.  Then  if Sis  a  cocZique
in  G we  have

V  :=  ISi  ~ n• (-s)
k-s

and  equaZity  holds  iff each  point  outside  Sis  adjacent  to  exactZy

K  k  •  V
:=  n- V

points  in  s.  In  this  case  we  find  a  2 - (V ,K, µ)  design  with  point  set  Sand

bZocks  B  =  {y  E  s  I y  adjacent  to  z}  for  z  E  G\S.
z

PROOF.  Let  there  be  x.  points  in  G\S  adjacent  to  i  points  of  S.  We  have
1.
 2

I  x.  =  n- V,
i

I  ix.  =  k  •  V,
i

I  i  V
(2)xi  =  µ.  (2),

so  that
 2  k 2v2
l(i-K)xi=µV(V-l)+kV-n-V  ~  0.

kV  d  .  1 · -i=  •  (  • Writing  x  =  -V- an  simp  iLying  using  O  <  V  <  n)  we  see  that  this  inequal--n
ity  is  equivalent  with

2  n-1
x  +  (µ  • k  - k+1 )x  +  µ-k  ::;:;  0

which  is  exactly  the  desired  inequality  (- note  that  the  largest  possible  V

corresponds  to  the  smallest  possible  x,  and  that  the  middle  coefficient

equals  µ-;\  since  n  =  1 + k + k(k-1-A) /µ).  D

2.  THE  NONEXISTENCE  OF  (57,14,1)

Let  G be  a  strongly  regular  graph  with  parameters  n  =  57,  k  =  14  and

;\  =  1.  Then  JJ  =  4  and  the  smallest  eigenvalue  of  the  (0,1)-adjacency  matrix
of  G is  s  =  -5.  By  Lemma  2  a  coclique  in  G can  have  at  most  15  points.  We
first  derive  a  contradiction  under  the  assumption  that  G contains  a  coclique

of  size  15,  and  then  under  the  opposite  assumption.

2.1.  G has  a  15-coclique

Let  S  be  a  15-coclique  in  G.  If  we  identify  a  point  z  not  in  S  with

the  set  B  =  {y  ES  I  y  ~  z}  (where~  denotes  adjacency)  then  the  points  of
z
Gare  the  points  and  blocks  of  a  2- (15,5,4)  design  (S,B).  Choose  a  block

B0 ,  and  investigate  the  intersection  numbers

Obviously,  since  A,JJ  ::;:;  4  we  have  x 5  =  1,  i.e.,  there  are  no  repeated

blocks.

Since  A=  I,  each  edge  is  in  a  unique  triangle,  and  each  point  is

incident  with  7  triangles.  Of  the  seven  triangles  inc.ident  with  B0 ,  five
contain a point  of  S  and  two  consist  of  blocks  only.  But  if  a  triangle
consists  of  three  blocks,  these  blocks  must  be  mutually  disjoint,  because
\=I.  This  proves  x0  ~ 4.

We  have  the  equations

XO+  XI  +  x2  +  X3  +  X4  =  41  ,

xi  +  2x2  +  3x3  +  4x4  =  5 • I 3  =  65,

x2  +  3x3  +  6x4  =  (5). 3  =  30.
2

Consequently,
 3

Since  x0  ~  4  it  follows  that  x4  =  0  and  thus  x0 + x3  =  6.  But  this  soon  leads

to  a  contradiction:

Let  B0 ,B 1,B 2  and  B0 ,B3 ,B4  be  two  triangles  containing  B0 .  Since  inter-
sections  of  size  4  do  not  occur  we  may
B0 :  11111  00000  00000

B1:  00000  Ill II  00000

B2:  00000  00000  111  11

B3:  00000  11100  11000

B4 :  00000  00011  00111

B5 :  <3*1>  00000  <2*1>

B6 :  <3*1>  <2*1>  00000
B:  <3*1>  000 ..  00 ...
 suppose  !B3nB 1 I  =  3,  and  then

IB4 nB2 !  =  3.

Let  B1,B5 ,B 7  be  another  triangle  contain-

ing  B1.  W.l.o.g.  !B5 nB0 1  =  3.

Let  B2 ,B6 ,B8  be  another  triangle  contain-

ing  B2 .  W.l.o.g.  IB6 nB0 1  =  3.
Finally,  let  B3 ,B,B'  be  another  triangle

containing  B3 .  W.l.o.g.  IBnB0 1  =  3.

Since  x3 ::;  2  and  B5  r- B6 ,  B  must  coincide  with  either  B5  or  B6 .  But  then  B

and  B0  have  at  least  five  common  neighbours:  B1  or  B2 ,  B3 ,  and  the  three
points  in  B  n  B0 .  Contradiction,  for\,µ::;  4.

2.2.  G does  not  contain  a  15-coclique

LEMMA.  G  does  not  contain  a  regular  subgraph  H with  6  points  and  valency  3

( i. e . .,  K3 , 3  or  the  prism) .

PROOF.  Apply  Lemma  I  with  N =  6,  M =  9,  di=  •••  =  d6  =  3.

We  find  66-15  ~ 51.  Since  equality  holds,  exactly  15,points  outside  Hare

connected  with  two  points  in  H.  If  z  is  a  point  in  G\H  adjacent  to  two
points  of  H,  then  let  H  be  the  graph  induced  by  G  on  Hu  {z}.  Again  apply
z
 4

Lenm1a  1,  now  with  N =  7,  M =  11,  di=  2,  d2  =  d3  =  d4  =  d5  =  3,  d6  =  d7  =  4.

We  find  76-26  ~ 50.  Since  equality  holds  again,  no  point  in  G\(Hu{z})  is
adjacent  to  three  points  in  Hu  {z}.  It  follows  that  if  Sis  the  set  of  15
points  adjacent  to  two  points  in  H,  then  Sis  a  15-coclique.

Contradiction.  D

In  the  previous  section  we  considered  Gas  a  2- (15,5,4)  design;  now

we  shall  consider  Gas  a  GD[4,3,2;14]  group  divisible  design:  Let  00  be  some
fixed  point,  r  :=  r( 00 )  the  set  of  its  neighbours  and  6  the  set  of  its  non-

neighbours.  Then  lrl  =  14  and  161  =  42.  G  induces  on  r  a  regular  graph  with

valency  A=  I,  so  that  we  find  seven  disjoint  pairs  in  r,  the  groups.  For

each  point  z  E  6  we  find  a  block  B  =  {x  Er  I x  ~ z}  of  sizeµ=  4.  One
z
verifies  inm1ediately  that  r  with  these  groups  and  blocks  is  a  group  divisible

design  GD[4,3,2;14]  (in  HANANI's  notation).

(A)  Let  T  be  the  union  of  -two  groups  in  r.  The  set  R  of  the  six  points  in  6-
not  joined  to  any  point  of Tis  a  6-coclique.

PROOF.  For  u  ER,  let  x.  :=  x.(u)  :=  #{z  E  6  I  z  ~  u  and  lr(z)nTI  =  i}.  Then
l.  l.

and
 x  +  2x  = µ • I T I  =  I 6
I  2

so  that  x2-x0  =  6.  Suppose  that  u,v  ER  and  u  ~  v.  Then  x0  ~  I,  so  x2  ~  7

and  hence  both  u  and  v  have  at  least  7  neighbours  in  the  set  (of  size  12)
of  points  with  two  neighbours  in  T.  But  then  they  must  have  at  least  two

conm1on  neighbours.  Contradiction  with  A=  I.  D

(B)  Let  U =  U(B)  be  the  union  of  the  three  groups  that  do  not  intersect  B.

Let  x.  :=  x.(U)  :=  #{z  E  6  I  lr(z)nUI  =  i}.  Then
l.  l.

x0  +  x 1  +  x2  +  x3  =  161  =  42,

x 1  +  2x2  +  3x3  =  IUl•(k-2)  =  72,

x2  +  3x3  =  12•(µ-1)  =  36,

so  that  x0+x3  =  6.

Let  y.  :=  y.(B)  :=  #{z  E  6  I  z  ~Band  lr(z)nU(B) I  =  i}.  Then
l.  l.

Yo+  YI+  Y2  +  y3  =  k-µ  =  10

and

From  (A)  it  follows  that  y0  =  y 1  =  0  and  hence  y 2  =  6,  y3  =  4.  We  can  iden-
tify  these  four  neighbours  of  B  intersecting  U  in  three  points:  they  are

the  blocks  B  where  p  EN  and
p  p BB  is  a  triangle.
p
[For:  suppose  B  intersects  U
p  in  less  than  three  points.  Then  there  is  a

second  group  {r,s}  intersecting  both  Band  B  •  Of  courser  EB  n  B  is
p  p
impossible  since  A=  I,  so  we  would  haver  EB  ands  EB  •  But  now  we  find
p
a  prism  on  the  set  {B,B  ,p,r,s, 00 }.  Contradiction.]
p  7
There  are  42  blocks,  but  only  (4)  =  35  sets  of  4  groups.  Therefore,
there  must  be  two  blocks,  say  B'  and  B",  intersecting  the  same  four  groups
(i.e.,  U =  U(B')  =  U(B")).  Now  x0 (U)  ~ 2  and  x3 (U)  ~ y3  =  4,  so

x3 (U)  =  y3 (B')  =  y3 (B")  =  4:  the  four  blocks  intersecting  U  in  three  points
are  common  neighbours  of  B'  and  B",  so  B'  n  B"  =  </>  sinceµ=  4.

But  for  p  E  B'  the  block  B'
p  intersects  f\U  only  in  the  point  p,  i.e.,

B'  :/:  B"  for  p  E  BI,  q  E  B".  Contradiction.
p  q

Hence  no  graph  G  exists.
 Vanl!llse,  781208
 5

ONTVANGGJ  1 8 JAU.  1979
