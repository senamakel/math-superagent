<!-- source: https://web.archive.org/web/2023/https://digitalcommons.memphis.edu/cgi/viewcontent.cgi?article=1134&context=speccoll-faudreerj | converted from PDF -->

University of Memphis University of Memphis
University of Memphis Digital Commons University of Memphis Digital Commons

Ralph J. Faudree

6-21-2021

The Number of Cycle Lengths in Graphs of Given Minimum The Number of Cycle Lengths in Graphs of Given Minimum
Degree and Girth Degree and Girth

Follow this and additional works at: https://digitalcommons.memphis.edu/speccoll-faudreerj

Recommended Citation Recommended Citation
"The Number of Cycle Lengths in Graphs of Given Minimum Degree and Girth" (2021). Ralph J. Faudree.
135.
https://digitalcommons.memphis.edu/speccoll-faudreerj/135

This Text is brought to you for free and open access by University of Memphis Digital Commons. It has been
accepted for inclusion in Ralph J. Faudree by an authorized administrator of University of Memphis Digital
Commons. For more information, please contact khggerty@memphis.edu.
 DISCRETE  MATHEMATICS

ELSEVIER  Discrete Mathematics 200 (1999)  55~50

The  number  of  cycle  lengths  in  graphs  of  given  minimum
degree  and  girth

P.  Erd6s  a,  R.J.  Faudree  b'l,  C.C.  Rousseau  u,  R.H.  Schelp  h'*,2

a  Mathematics  Institute,  Hungarian  Academy  of  Science,  Budapest,  Hungary
b  Department  of  Mathematical  Sciences,  University  of  Memphis,  WinfieM  Dunn  Bldg.,  RM.  373.
Memphis.  TN  38152,  USA

Received 23 July 1997;  revised 15 January 1998;  accepted 2 February 1998

De.cation

The  latter  three  authors  dedicate  this  article  to  the  memory  of  the  late  Paul  Erdb's,  their  longtime
friend,  mentor,  and  frequent  collaborator.  The  results  of  this  paper  were  started  several  years  ago  during
one  of  the  many  Erdds  visits  to  Memphis.  We  feel  both  honored  and  privileged  to  have  had  the
opportunity  to  learn  from  and  work  with  him  over  the  last  23 years.

Abstract
 This  paper determines lower bounds on the number of different cycle lengths in  a  graph of
given minimum degree k  and girth  g.  The  most general result  gives a  lower bound of ck  ~.
@  1999  Elsevier  Science  B.V.  All  rights reserved

Keywords"  Cycle lengths;  Girth;  Minimum degree;  Predecessor

I.  Introduction

A  graph G  of minimum degree k,  contains at  least k-1  cycles of different lengths.
One  need only  consider the  end vertex x  of a  longest path in  the  graph and form the

cycles determined by  the path segments from x  to  the  k-1  neighbors of x  at  greatest

distance along the  path.  Clearly,  k-1  is  best possible as  shown by  the  graphs K~+l
and Kk,  k.  The  problem suggested by  these comments is  of  more  interest if  G  has  a
minimum girth  requirement.

Let  n(g,d)  denote the  minimum number of different cycle lengths in  a  graph with
girth at least g  and minimum degree at least d.  The  objective of this paper is  to prove

*  Corresponding author. E-mail:  schelpr@msci.memphis.edu.
1 This work was partially supported by ONR  Research Grant N00014-94-J-1085.
2 This work was partially supported by NSF  Grant DMS-9400530.

0012-365X/99/$-see  front matter (~)  1999  Elsevier  Science  B.V.  All  rights reserved
PII:  S0012-365X(98)00324-0

56  P.  Erdds  et al./ Discrete Mathematics 200 (1999)  5540

for  appropriate  constants  c~,  c2,  and  c3  that
(1)  n(S,k)>~(k  2 +  k-  2)/4,
(2)  n(9,k)>~clk  3,
(3)  n(7,  k)>~c2k  s/2, and  more  generally  that
(4)  n(4t-  1,k)>~c3k  t/2 for  t~>2.
The  lower  bound  given  in  (l)  is  the  correct  order  of  magnitude  of  n(5,k).  The  lower
bound  in  (4)  is  likely  to  be  far  from  the  truth.  In  fact,  the  best-known  upper  bound  is

n(g,k)<<,k  ~  which  is  weak  in  that  it  comes  from  the  upper  bound  given  by  Erd6s  and
Sachs  [2]  on  the  minimum  order  of  a  k-regular  graph  of  girth  9.

2.  Results

Theorem  1.  (i)  n(5,k)<~k  2 -  k  if  k-1  is  a  prime power, (ii)  n(5,k)>~(k  2 ˜  k  -  2)/4
for  all  k>~2,  (iii)  n(5,k)  =  O(k2).

Proof.  Suppose  k-1  =q  where  q  is  a  prime  power.  Let  G  be  the  bipartite  graph
obtained  from  the  projective  plane  of  order  q  by  taking  one  part  to  be  'points'  and
the  other  to  be  'lines'  of  the  projective  plane,  and  letting  adjacency  in  G  correspond
to  incidence  in  the  projective  plane.  Then  G  is  regular  of  degree  q  +  1  and  satisfies
g(G)>4.  At  most,  G  has  cycles  6,8,  10  .....  2(q  2  +q  +  1),  so  the  number  of  different
cycle  lengths  does  not  exceed  q2  +  q.  This  example  shows  that  n(5,k)<~k  2 -  k  for
k  =q  +  1.  In  view  of  well-known  facts  about  the  gap  between  successive  primes,  it
follows  that  n(5,k)~<(1  +  o(1))k  2,  k  ~  oc.
To  prove  the  lower  bound  consider  a  path  P=(xo,xl,...,xn)  in  G  of  maximum
length  where  g(G)~>5  and  fi(G)>~k.  Thus  all  neighbors  of  x0  are  on  the  path,  and
since  6(G)>~  k  the  neighbors  N(xo) of  x0  constitute  a  set  containing  at  least  k  elements.
Let
 N(xo) ~_  {xt,xi:,xi3  ..... xi~}  with  1  <i2  <  "'"  <ik.

Note  that  xi2  i,xi3-1 ..... xi,-i  are  each  end  vertices  of  a  maximum  length  path  in  G,
that  is  (X(i_I,Xi_2,...  ,Xo,Xi,,Xxi+l  .....  Xn)  is  a  maximum  length  path  for  2  <<,j<~k.
Since  G  contains  no  cycle  C3  with  3  vertices,

{xo,  x,,_  ,,  x,3-1  .....  _,  }  n  {x,,  x 2,  x,3  .....  }  =  O.

A  lower  bound  can  be  given  for  U)=  2 N(xi,-1  ),  where  N(xi,_  1)  is  the  set  of  neighbors
of  xi~_  l,  all  of  which  lie  on  the  path  P.  Clearly  for  l ¢  t,  IN(x#_1  )NN(xi,_  l)]  ~<  1,
otherwise,  if  Zl  and  z2  are  distinct  members  of  this  intersection,  G  contains  the  cy-
cle  C4  =  (xi;  -  a, Zl,  xi, _  l, z2, xi,-  1  ).  Thus  ]N(xi~_  l ) U N(xi,_  i )l  1>  k  +  (k-  1  )  =  2k-  1  for  all
l  ¢  t  so  that  ]  Uf=  2  N(xi,_,  )1  ~>  k  +  (k-  1  )  +  (k  -  2)  +-..  +  2  =  (k-  1  )(k  +  2)/2.
For  convenience,  a  neighbor  xr  of  xi,-1  will  be  called  a  forward  neighbor  on  P
if  r>iy_l  and  a  backward neighbor  on  P  when  r<ij-  1.  Thus  of  the  at  least

P.  Erdds  et  al./Discrete  Mathematics  200  (1999)  55~0  57

(k-1)(k+2)/2  neighbors of  some xi~-l  in  [,J;=zN(X#_l)  at  least one-half are  for-
ward neighbors or  at least one-half are backward neighbors. If  one-half of (k-  1 )(k +
2)/2  are  forward neighbors, then each such neighbor x~  c  N(xi,_l)  gives the  cycle
(xo,xt  .....  Xij-l,X,-,X~-I  .....  X#,Xo)  of  length r  +  1  in  G.  But  each of  these at  least
(k-1)(k  +  2)/4  neighbors have a different index r  so that G  contains (k-1)(k  +  2)/4
different cycle lengths. Likewise, if there are (k-1)(k +  2)/4  backward neighbors, then
each such neighbor xr  E  N(xi~_  l  )  gives a cycle (xo,  x  l  .....  x~,  x!j_  t,  x#,  xo  )  of length r +  3.
Again  a  different index for each backward neighbor provides at least (k-1)(k  +  2)/4
different cycle lengths.
In  view  of the bounds obtained above one has n(5, k)=  O(k2).  []

In  each of the remaining theorems it  will  be  shown that n(t,k)>~ck  ftt)  for  some
appropriate f(t)  and constant c.  Since  c  can be chosen small and k  is integral, it  will
suffice to prove each of these inequalities  for all  k ~>k0,  k0 fixed. Thus, in  the proofs
which follow it  will  be  assumed (without mention) that it  is  enough to  prove  each
theorem for all  k  larger than some fixed k0.

Theorem 2.  There  ex&ts  a  constant  c~,  such  that  n(9,k)>~clk  3.

Proof.  Consider a  longest path P=(xO,Xl  .....  Xn)  in  a  graph G  with  g(G)>~9  and
fi(G)>~k.  Let  N(xo)D_  {Xl,Xi~,xi2  .....  xi~}.  As  noted earlier each of xo,xi,-i  .....  xi~-i
are the  end vertices of a  longest path. Choose an  end vertex which has its  Lk/2jth
neighbor along its longest path as close as possible. For convenience, assume x0 is that
end vertex with longest path P  and let F  =  {x0:1  ~<j  ~<  [k/2J }  be the set of those closest
neighbors. As  a consequence of this choice for each xij E  F-{xl  }  the element x//_  i  has
at least Lk/2j forward neighbors along P.  Denote this set of forward neighbors by E/for
all such i/. Since  g(G)>6,  it is clear that F#  NFi,  =0  for all j~t,  2~<j,  t~<  [k/2J. Thus
if F/- ={x,  1:  xicFij  -  {x#}},  each pair F#-NF/,  =0  for all  j#t,  2<~j,  t<~[k/2  1.

It  clearly follows that IF#-]  >t  Lk/2j -  1 and ]  U~22  J F/~-]  >~  ( Lk/ZJ  -  1 )2.
In  order  to  obtain the  lower  bound of  the  theorem a  lower  bound estimate is
first  needed for  ]0)~22JN(F/~-)I  where  N(A)is  defined as  the  set  {y:  yxEE(G)

for  some xEA}.  Note  if  Xr,  X~EFi~-,  xr:/:xs,  then N(x,.)AN(xs)=O.  If  not,  say

z  E  N(xr  )  N  N(xs  ),  then (xij-  i,  x~+  l,  x~,  z,  x~.,  x,.+  l,  x  b-  1 )  is  a  (76  in  G,  contradicting the
girth requirement.  Therefore IN(F/- )1 ~>k(  Lk/2J -  1).
Consider F/-  and  F/-  with  j  ¢  t.  Surely,  if  F/,- N N(F/7)  ¢  ~  then  each vertex

y  E  Fi-NN(Fi~-)  has no  neighbor in  N(F/-),  otherwise G  would contain either a  C3
or a  C7.  More generally it  is true that for each y  E  F/-,  IN(y)A  N(F/-)1 ~<  1. If this is

not the case then let z:/:w  be  elements of N(y)NN(FiT)  with x,., x~  EF/~  such that

x~z,  X,.w  E  E(G).  But  then either Xr  ¢  Xs  and (xi~-  l  x~+  i,  xr,  z,  y,  w,  xs,  xs+l,  xij-  I  )  is  a  C8
in  G,  or x~  =x~  and (Xr,Z,y,W,  Xr)  is a  Ca  in  G,  both of which are impossible.
Hence,

[N(F#)  A  N(F/,-)[  ~<  min{IF/~  [,  IF/,- I}

58  P.  Erdds  et  al./Discrete Mathematics 200  (1999)  55~50

and
 IN(F~.-  )  o  N(~-)I/>  IN(F~.-  )[  +  IN(Fi-)I  -  rain{  If(I,  IF£1}

It  follows  that

L,~/2J  U  N(F6-  )
j=2
 for  all  j  ¢  t.

Lk/2A
~>  ~-~'  N(Fi;)I-  ~  min{  IF/(I,  IF~,-  I  }  •

j  =  2  2<~j<t<~  [k/2/

Since  IN(Fi~)I  -  mlFi~-  [  >>.(k  -  m)IFi~-  ]  >>.(k  -  m)([k/2]  -  1),  the  difference

Lk/2J  y~  IN(F()I  -  ~  min{lF(I,  IF~.  I}

j  =  2  2<~j<t<~  [k/2]

>~  (  [k/ZJ  -  1  )(k  -  Lk/ZJ  +  1  )(  Lk/2J  -  1  )  >1  ck  3

II  j-k/2j  N(F~2)I  >ck  3. I  Therefore  I  ~j  =  2 with  c  ~  g.

The  final  step  in  the  proof  is  to  partition  U}~22  N(~-)  into  sets  Al,  A2,  A3  as

follows:  forxr  CN(~/)  andx,  EF,/with  x,.  x~  EE(G)  place  (1)Xr  inA1  ifr>s,  (2)x,.
in  A2  if  ij<r<s,  and  (3)xr  in  A3  if  r<ij  -  1.  But  each  of  the  elements  in  a  fixed
Ai,  1  ~<i  ~<  3,  give  cycles  of  different  lengths.  For  xr  E  A  i  the  cycle

(X0,XI  .....  Xi/--  l ,Xs+  l ,Xs+  2 .....  Xr,Xs,Xs--  I .....  X(i,Xo  )

is  a  cycle  of  length  r+l;  forx~cA2  the  cycle  (xo,xl  .....  xii-l,Xs+l,X~,X~,Xr-i  .....  xij,xo)
is  a  cycle  of  length  r+3;  and  for  x~  EA3  the  cycle  (x0,xl  .....  xr,xs,x~+l,x#_l,xij,Xo)  is
a  cycle  of  length  r  +  5.  Therefore,  since  one  of  Ai,  A2,  A3  has  cardinality  at  least
ck3/3,  the  proof  is  complete.  []

Theorem  3.  There  exists  a  constant  c2  such  that  n(7,k)>~c2k  5/2.

ProoL  The  proof  of  this  result  is  similar  to  that  of  the  proof  given  of  Theorem  2
so  results  obtained  there  will  be  used.  The  proof  begins  the  same  except  that  G  is
a  graph  with  9(G)>~7.  Let  P=(xo,xl  .....  xn)  again  be  a  longest  path,  and  let  F,  Fij
and  F/j-  (1  <~j  <<.  Lk/2J  )  be  as  defined  in  Theorem  2  except  that  both  F/j  and  F/-  are
restricted  to  exactly  [k/2J  forward  neighbors  and  Lk/2J  -  1  predecessors  of  these  forward
neighbors,  respectively.  Observe  that  each  y  C  Fi7  can  have  at  most  one  neighbor

in  F/i  ,-  for  any  t¢j.  Also  each  y  E  F/-  has  at  most  one  neighbor  in  U}k/21J=  ~,  and
no  neighbor  in  F.  Thus  each  y  E  Fi-  has  at  least  k-  Lk/2j  new  neighbors  in  L3

where  L3=G  -({Xo}  uFu(U)k__/2~  F/j)  u(U}~TF/~)).  Setting  L2=  U~k__'/22  ]  F/~  recall
that  IL21  =  (/k/2/  -  1)  2  so  that  there  are  at  least  ([k/2j  -  1)  2  rk/2]  edges  from  L2
to  L3.
The  next  step  of  the  proof  is  to  apply  a  theorem  of  deCaen  and  Sz6kely  [  1  ]  to  obtain
an  estimate  on  [L3[  in  the  bipartite  graph  with  L2  and  L3  as  parts,  deCaen  and  Sz6kely

P.  Erdrs  et  al./Discrete  Mathematics  200  (1999)  55~50  59

[1]  proved that a bipartite graph with no C4  and no C6  and parts of order r  and s  with
(x/~<r<s)  has at most c*r2/3s  2/3  edges, c*  a  constant.
Since  the bipartite graph given above with parts L2  and L3  (IL31  >~IL21)  has at least
( Lk/2J  -  1 )2 [k/2~  edges, it  follows that ( [k/2J  -  1 )2 [k/2~  <~  c*  IL2  ]2/3  IL312/3. Therefore
since IL21  =  (  Lk/2J -  1)2,  IL3I ~>  c,k5/2,  c'  an  appropriate constant.
The  proof is  completed as  in  the  final  step of  the proof of  Theorem 2,  the  only
difference is  that L3  replaces the  set  [-J)*--/7  N(~)  given  there. As  done before L3
is  partitioned into  sets A1,A2,  and A3  with  each pair  of  elements in  Ai  determining
a  pair  of cycles of different length. Since  the largest of these three sets has at  least
1L31/3  >>.(c'k5/2)/3  elements, G  contains at least (c'k5/2)/3  different length cycles.  []

Theorem 4.  There  ex&ts  a  constant  ¢3  such  that  n(4t-  1,k)>/c3k  t/2  for  t>~2.

Proof.  Suppose  g(G)~>4t-  1 and 6(G)>~k.  Let P~o  -(x0,xl ..... x,)  be a path of max-
imum length in  G.  As  before if  {xi~  =Xl,Xi2  ....  x/k}  C_N(xo)  then each of the vertices
xi,-1  =xo,xi2-1  ..... xik-i  are end vertices of a  path of maximum length. In  fact, each
of these maximum length paths are simply a reordering of the vertices of P~0.  Relative
to the path P~o  each Xgj_  1 is  a  predecessor of x#.  For convenience x/j_  i  will  be called
a  Pxo-predecessor of xij.  More  generally, if  x  is  an  end vertex of a  maximum length
path and x  is  adjacent to xr  then xr-1  will  be called a Pz-predecessor of Xr  (assuming
Xr-l  precedes x~  as one moves along the path from x).  For  t>~2  it  is  clear that the
sets N(xi2-1),N(xi3-1)  ..... N(xik-l  )  are pairwise disjoint,  otherwise G  would contain
a  cycle on at most six vertices. Therefore,  [  U;=2N(xij_l  )1. >~(k-1)k.
Let  x  be  an  end  vertex  of  a  longest path P  and  let  N*(x)={y:  yEN(x)  and
yx  is  not  an  edge of P}.  Set  I(l)=N(x0),  PI(1)=  {y:  y  is  a  Pxo-predecessor of
z  E  N*(xo)},   (2)  =  Ux e too)N(x)  and PI(2)  ---  {y:  y  is a Px-predecessor of z E  N*(x),
x  EPI(1)}.  More  generally  if  I(j-  1)  and  PI(j-  1)  are  defined  let  I(j)=

Ux  E  PI(j--  I  )  N  (x  )  and PI  (j  )  =  {y:  y  is  a  Px-predecessor of z  E  N*  (x  ),x  E  PI  (j  -  1)}.
As  noted above li(2)]  ~>(k-1)k  when t~>2.  In  a  similar fashion since the girth of G  is
at least 4t-1,  [I(j)[  >>,(k-l)J-lk  when j<~t.  One  should observe that, with respect to
the original path P~0  with end vertex x0,  a vertex y  E  PI(i),  i  <~j,  may be a predecessor
or  successor of some z  E  N(x)  where x  E  PI(i  -  1).  This depends on how the original
path P  is reordered in  the i  steps which determine PI(i).
Along  the original path P~0  select a  vertex z  El(t)  which is  at the greatest distance
from x0.  Next,  select z'  E  Pl(t  -  1 )  such that z'z  E  E(G).  But  z'  is then the end vertex
of a  longest path Pz,  and this path does not include the edge zz'.  Thus, form the cycle
C  =Pz  +  zz'  and notice from the  choice of z  that the  sets PI(t)  and I(t)  are  both
subsets of the vertex set of C.  Also  [PI(t)l  =  II(t)[  >~(k-1)t-lk.  But  as the vertex set
of the cycle contains the independent set Pl(t  -  1)  and all  its neighbors (the members
of I(t)),  there are at least (k-1)t-2k(k-2)>~(k-2)  t  chords in  C.  Here  a chord refers
to  any noncycle edge connecting a  pair of vertices of the cycle. Also  the length of a
chord will  refer to the shortest distance between the endvertices of the chord along the
cycle.

60  P.  Erdds  et al./Discrete Mathematics 200 (1999)  55~50

Surely  different  length  chords  in  C  determine  different  length  cycles.  Thus,  one  has
determined  the  desired  c3k  t/2  different  length  cycles,  if  there  are  at  least  (k-  2)  t/2

chords  of  C  of  different  length.  Since  one  can  then  assume  no  such  set  of  different
length  chords  exists,  it  follows  that  from  the  (k  -  2)  t  chords  of  C,  at  least  (k  -  2)  t/2

are  of  the  same  length.  Further  from  these  (k-  2)  t/2  of  the  same  length,  assume  that

s  of  them,  say  el,e2  .....  es  are  pairwise  noncrossing  in  C  and  ordered  in  a  clockwise

fashion.  In  addition,  it  can  be  assumed  that  at  least  one-half  of  the  remaining  chords
of  the  same  length  cross  the  odd  indexed  chords  el,e3  .....  e2[.,./2]-1.

Set  l  =  2rs/2  ]  -1.  Of  the  ½((k-2)  t/2  -s)  chords  of  the  same  length  which  cross  one

of  el,e3  .....  e/,  assume  rt  of  them  cross  ei  for  i=  1,2  .....  I.  Let  C=(yl,y2  .....  y,,)
and  assume  that  the  length  of  chord  ei  from  vertex  yr  to  yt  is  measured  along
the  segment  (yr,  yr+i  .....  yt)  of  the  cycle  with  crossing  chord  f=(ys,  yu)  where

r<s<t<u.  Note  that  the  cycle  (yl,y2  .....  Yr,  yt,  yt  l  .....  y~.,y,,,yu+~  .....  yn)  skips

vertices  Y,-+l,yr+2  .....  Ys-l,yt+l,yt+2  .....  yu-i  of  C,  so  is  of  length  n  -  (s  -  1  -
r)  -  (u  -  1  -  t).  If  m=s  -  1  -  r  +  u  -  1  -  t,  a  resulting  cycle  obtained  from  C
by  skipping  m  such  vertices  is  denoted  C(m).  It  is  clear  that  each  of  the  ri  chords

which  cross  chord  ei  cross  no  other  odd  indexed  chord  and  each  skips  a  different
number  of  vertices  of  C.  Therefore,  let  m(1,i)<m(2,  i)<  ...  <m(ri,  i)  be  the  num-

bers  of  vertices  skipped  by  the  ri  chords  crossing  ei.  Thus  one  obtains  the  follow-

ing  cycles;  C(m(1,  1)),  C(m(2,  1))  .....  C(m(rl,  1)),  C(m(rl,  1)  +  m(1,2)),  C(m(rl,  1)  +
m(2,2))  .....  C(m(rl,1)  +  m(r2,2)),C(m(rl,1)  ÷  m(r2,2)  +  m(1,3)),C(m(rl,1)  +

m(r2,  1)  +  m(2,3))  .....  C(m(rl,  1)  +  m(r2,2)  +  m(r3,3))  .....  C(m(rl,  1)  +  m(r2,2)  +

•  ..  +  m(rt-l,l  -  1)  +  m(1,  I))  .....  C(m(ri,1)  +  m(r2,2)  +  ...  +  m(rz,  l)).  This  gives

l((k-  2)  t/2-  s)  different  cycle  lengths.  But  if  each  of  the  chords  el,e2  .....  e/  skips  u

vertices  of  C,  by  skipping  one  or  more  of  these  chords  as  one  traces  around  C,  cycles  of
length  ICI-ju,  j  =  1,2  .....  l  are  obtained.  Thus  it  follows  that  there  are  at  least  ½((k-

2)  t/2  -  s)  +  l  cycles  of  different  lengths  in  G  which  is  at  least  c3k  t/2  for  an  appropriate
constant  c3.  []

It  is  likely  that  neither  the  lower  bounds  of  Theorems  2-4  nor  the  general  upper
bound  given  is  close  to  the  truth.  Precise  bounds  will  likely  be  difficult  to  obtain.

References

[1]  D.  de  Caen,  L.A.  Szrkely,  The  maximum  size  of  4-  and  6-cycle  free  bipartite  graphs  on  n  vertices,  in:
G.  Halfisz,  L.  Lov~isz,  D.  Mikl6s,  T.  Sz6nyi  (Eds.),  Graphs,  Sets  and  Numbers,  Proc.  Conf.  Dedicated
to  A.  Hajnal  and  V.T.  S6s,  Budapest  1991,  Coll.  Math.  Soc.  Jfinos  Bolyai,  vol.  60,  1992,  pp.  135-142.
[2]  P.  Erdrs,  H.  Sachs,  Regulfire  Graphen  gegebener  Taillenweite  mit  minimaler  Knotenzahl,  Wiss.  Z.  Univ.
Halle,  Math.  Nat.  R.  12  (1993)  251-258.
