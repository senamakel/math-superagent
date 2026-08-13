<!-- source: https://ir.cwi.nl/pub/1712/1712D.pdf | converted from PDF -->

ACT A  ARITHMETICA
XLVIII  (1987)

Equal  values  of  binary  forms  at  integral  points

by

J.-H.  EVERTSE * (Amsterdam),  K.  GvCRY * (Debrecen)
T.  N.  SHOREY  (Bombay)  and  R.  TuoEMAN  (Leiden)

1.  Equations  in  rational  integers.  Let  F(X,  Y)  be  an  irreducible  binary
form  of degree  n  ;;:::  3  with coefficients  in  Z  (the  ring  of rational integers)  and
m  a  non-zero  rational  integer.  In  1968,  Baker  [1]  gave  an  explicit  upper
bound  for  all  the  solutions  of  the  Thue  equation

(1)  F(x, y) = m  in  x,  yEZ

which  depends  only  on  m,  n  and  the  height  H (F)  of  F  (i.e.  the  maximal
absolute  value  of  the  coefficients  of F).  Here  the  irreducibility  of F  can  be
replaced  by  the  weaker  assumption  that  OJ (F) ;;:::  3  where  ro (F)  denotes  the
maximal  number  of  pairwise  non-proportional  linear  factors  of  F  in  its
factorisation  over  C  (see  e.g.  [10]  or  [20]).
After  Baker  had  proved  the  effective  version  of  Thue's  theorem  on
equation  (1),  Coates  [3],  [4]  showed  that  the  dependence  on  m  can  be
replaced  by dependence on the distinct  prime divisors  of m.  He proved that if
FeZ[X,  Y]  is  an  irreducible  binary  form  of degree  n ~ 3  and  if p 1 ,  ••• ,  Ps
are  distinct  prime  numbers,  then  all  solutions  of the  Thue--Mahler  equation

(2)  F (  )  v1  Vs
x, Y  =  P1  .. ·Ps  in

with  (x,  y) = 1  and  v1  ~ 0,  ... , vs  ;;:::  0,  in  absolute  values  are  less  than
a  bound  depending  only  on  n,  H(F),  s  and  maxp;.  As  a  consequence,  he
i
established  an  explicit  lower  bound  for  the  greatest  prime  factor  P(F(x, y))
of F(x,  y)  in  terms  of f!l'  =  max(Jxl,  IYI). These estimates of Coates  have  been
improved  and  generalised  by  others  (for  references  see  [2],  [10],  [21],  [14],
[20]).  In  1977,  Shorey,· van  der  Poorten,  Tijdeman and  Schinzel  [19]  proved
that  if FEZ[X,  Y]  is  any  binary  form  with  ro(F) ~ 3  then  for  all  pairs  x, y
with  (x, y)  =  1  and  F (x,  y)  =f:.  0,

* The research  was  partly done at the University  of Leiden in the academic year  1983/1984.

380  J.-H.  Evertse.  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman

(3)  P(P(x, y))  >  C 1  loglog(:1t"+2)

where  C 1  is  an effectively  computable  positive  number  depending  only  on  F.
Shorey  and  Tijdeman  [20,  Corollary  7.1]  derived  an  effective  upper
bound  for  the  solutions  of  the  equation

(4)  P(x, y) =  G(x, y)  in  x, yeZ with  P(x, y)  i=  0

where  F,  G  are  binary  forms  with  rational  integral  coefficients  such  that
deg P  >deg G  and  w(P) ~ 3.  Since  a  binary  form  may  be  a  constant,
equation  (4)  is  more  general  than  equation  (1).  Further  it  follows  from  the
arguments  of their  proof that  if  F,  GeZ[X, Y]  are  relatively  prime  binary
forms  with  (l)(F)  ~ 3.  then
P(  P(x, y)  )  "'  .  l
(P (x,  y),  G (x,  y))  .....,.  oo,  euect1ve y,

when  f!f.....,.  oo  subject  to  (x,  y)  =  1.
In  this  paper  we  shall  give  various further  generalisations  some of which
in  a  quantitative  form.  For  any  rational  number  a,  let  P(a)  denote  the
maximum  of the greatest  prime factors  of the numerator  and denominator of
a  (in  its  reduced  form),  but  P(O)  =  P(l) =  P( -1) =  1.

THEOREM  1.  Let P, GeZ[X, Y]  be relatively prime binary forms. Let  x
and y  be rational integers with (x, y)  =  1  and G (x,  y)  i=  0.  rf w (PG)  ~ 3,  then

( P(x, y))
P  G(x,y)  >C 2 loglog(¥+2).

If w(P) ~ 3,  then
 (  F(x, y)  )
P  (  G (  ))  >  C 3 log log ( .'¥' + 2).
F(x, y),  x,  y

Here .51'  =  max(lxl,  jyl)  and C2 ,  C3  are effectively computable positive numbers
depending only on the (constant and non-constant) irreducible factors of PG  in
Z[X,  Y].
The second  part of Theorem  1 has the following  immediate consequence.

COROLLARY  1.  Let F,  GE Z [X,  Y]  be relatively prime binary forms such
that  w(F) ~ 3.  Let  {p1 ,  ... ,  p1 )  be  d  set  of  prime  numbers.  Let
x, y, z, k 1 ,  ... ,  k1  be rational  integers with

zP (x, y)  =  G (x, y) p~1 ••• p~
1,

(x,  y)  =  1,  G(x, y)  i=  0,  (z,  P1  .. ·Pr)= 1.

Then  max(lxl,  lyl, lz/,  /ki/,  ... ,  /k,/)  is  bounded by  an  effectively computable
number depending only  on  the  primes p 1 ,  •.. ,  p,  and  the (constant and  non-
constant) irreducible factors of  PG  in  Z [X,  Y].

Equal  values  of binary  forms  at  integral  points  381

This is  an improvement of Theorem 7 .3  of Shorey and Tijdeman [20].
In  the next corollaries the restrictions concerning F  and G  are further
relaxed.

COROLLARY  2.  Let  F,  GE Z [X,  Y]  be  relatively  prime  non-zero  binarv
j(1rms.  Suppose  that  F  is  not  a  constant  multiple  of a  power  of a  linear  or  a~
indefinite  quadratic  form.  If x, y  are  rational  integers  such  that

F(x, y)IG(x,  y),  G(x,  y)  =P  0,  (x,  y)  =  1

then  max (lxl,  lyl)  is  bounded  by  an  effectively  computable  number  which
depends  onf.1·  on  the  degrees  and  heiphts  of'  F  and  G.

COROLLARY  3.  Let  F,GEZ[X, Y]  be  binaryjbrms  which  satisfy  the
conditions  of Corollary  2  and  also  deg F  >deg G.  Then  all  pairs  of rational
integers  x, y  with
 F(x, y)IG(x,  y),  G(x,  y)  =P  0,

are  such  that  max(lxl, lyl)  is  bounded  by  an  effectively  computable  number
which  depends  only  on  the  degrees  and  heights  of F  and  G.

Corollary 3  implies the result of Shorey and Tijdeman on equation (4).

COROLLARY  4.  Let  F,  GEZ[X,  Y]  be  distinct  non-zero  binary  forms.
Suppose  that  F/G  is  not  a  constant  multiple  of a  (positive  or  negative)  power  of
a  linear  or  an  indefinite  quadratic  form.  If x, y  are  rational  integers  such  that

(5)  F(x, y)  = G(x,  y),  (x,  y)  = 1,

then  max (lxl,  lyl)  · is  bounded  by  an  effectively  computable  number  which
depends  only  on  the  degrees  and  heights  of F  and  G.

Theorem 2  gives an upper bound for  the magnitude of the solutions of

(5)  and Theorem 3  implies an upper bound for  the number of solutions of (5)
both of which depend only on the irreducible factors of FG  in  Z [X,  Y].  In
order to  formulate these theorems we  need some further notation. Let  dll  be

an integral domain of characteristic 0  with  quotient field  K  and let

be binary forms. Then the resultant R (F,  G)  of F  and G is defined as follows:

R(F, G)  = {:o
bg
 if  p = q = 1,

if  p = 0,  q > 0,

if  p > 0,  q = 0;

where  in  the  determinant  the  first  q rows  contain  the  coefficients  of  F  and
the  other  p  rows  the  coefficients  of  G.  The  forms  F  and  G  have  a  non-
constant  common  factor  in  K  [ X,  Y]  if  and  only  if  R ( F,  G)  = 0.
Let  F1'  ... ,F,,  G1 ,  ••. ,GsEZ[X,  Y]  be  non-zero  binary  forms  with
coefficients  having  absolute  values  at  most  H  ( ~ 2).  Suppose  that  for
i  = 1,  ... ,rand j  = 1,  ... , s the  forms  F;,  Gj  have  no  non-constant  common
divisor  in  Z[X,  Y].  Let  L  denote  the  splitting  field  of F 1  •.• F,G 1  .•. G5  and
l,  RL,  hL  the  degree,  regulator  and  class  number  of  L,  respectively.  Let  t  be
the  number  of  distinct  prime  factors  of
0  R(F;,  Gj)
1 ~i~r
l~J~s

and  let  P denote  the  greatest  of these  prime factors  (with  the convention  that
P = 2  if  t  = 0).  Finally,  we  define  sets  of  binary  forms  .?,  '/J  by

r

§  =  :F:  F(X,  Y)  =  n F;(X,  Y)"i  for  certain  U1,  ... ,  U,EN},
i= 1

s

'{j  =  :c:  G(X,  Y)  =  n G;(X,  Yti  for  certain  V1,  ... ,  VsE N).
i= 1

Here  ;'\/  denotes  the  set  of  positive  rational  integers.

THEOREM  2.  Let  n  be the degree of F 1  ••• F,G 1 ••. G8 •  Suppose

w(F 1 ••• F,G 1  .•• Gs)  ~ 3,

~l x,  y  are  rational  integers with

(5)  F(x, y)  = G(x,  y),  (x,  y)  = 1,

for  some FE .?,  G E  <§,  then

(6)  max (Jxl,  JyJ)  < exp  ~(r + s) n4  (( C4  (t + 1) log P)1+ 1 Pr5 log HJ

where c ..  and  C 5  are  effectively computable positive numbers such  that  C4
depends only  on  I,  R1  and  hi>  and  C 5  depends only  on  l.

Equal  value~ of binary  forms  at  integral  points  383

Note  that  the  bound  in  the  theorem depends only  of  F1'  .. . ,  F,,
G 1 •.•• ,  Gs.  If  F  and G have a  common factor, then it  can be divided out.
Any  common factor of F  and G  is  a  binary form  which yields only  finitely
many new  solutions of (5).  In  the special case r  =  1,

Gj(X,  Y)  =  pj  for  j  = 1,  ... , s,

where p1 ,  .•. ,  Ps  are  distinct  prime  numbers, Theorem 2  gives  an  upper
bound for  the solutions of the Thue-Mahler equation (2)  for  binary forms
Fr:::  Z[X,  Y]  with  w(F)  ~ 3.  For this  case Gyory (cf.  [9],  Corollary  1)  has
proved the same estimate, but with completely explicit  values of C4  and C5 •
We call elements a1 ,  •.. ,  ak  of a field  K  multiplicatively independent  in  K

if  a 1 a 2 ..• a"  #  0  and if  the only rational integers 11 ,  ... ,  lk  for  which a~1 •.• a~
=  1  are 11  = ... = lk  = 0.  The following  consequence of  Theorem 2  relates
multiplicative independence of binary forms to  multiplicative independence of
the  values of  these forms.

COROLLARY  5.  Let  Fi(X,  Y), .. ., F,(X,  Y)EZ[X,  Y]  be  binary  forms
such  that  F 1 ,  .• .,  F,,  P/Q  are  multiplicatively independent  in  Q(X, Y)  for  all
relatively  prime  binary  forms  P,Q  in  Z[X, Y]  with  w(PQ)E'.1,2]. Then
there  exists  an  effectively computable  number  C6  depending  only on  F 1 ,  •• .,  F,
such  that  F 1 (x,  y),  .. .,  F,(x,  y)  are  multiplicatively  independent  in  Q for  all
rational  integers  x, y  with  (x, y)  =  1  and  max (lxl,  IYD  > C6 .
For binary forms FEZ [X,  Y]  with  w(F)  ~ 3,  Evertse [6]  and Evertse
and  Gyory  [7]  derived  the  upper  bounds  2 x r 3<2s+ 3)  and  4 x 71<2s+ 3\
respectively, for  the number of solutions of (2).  Here n =  deg(F) and I  is  the
degree of  the  splitting  field  of  F.  (Thus  1 ::::;  1::::; n!.)  We  shall  generalise
Evertse's result  to  the more general equation (5).

THEOREM  3.  Ler  .F,'t/,  F 1 ,  .. .,  F,,  G1 ,  .. .,  G,  and  t  be  as  above.  Let n  be
rlu.>  deyree  of'  F 1 ... F,G1  •.• G,.  Suppose  (!)(F 1  ... F,G 1 ... GJ ~ 3.  Then  the
number  of pairs  x, yEZ for  which  (5)  holds  for  some  FeF,  GE~ is  at  most
2 x  r3(2r + 3)_

This  bound can  be  compared with  the  estimate (6)  obtained for  the
solutions themselves. Note that  the upper bound in  Theorem 3  is  indepen-
dent of  r,  s,  P,  H  and L.
For  results on  exponential diophantine equations

Axm+By"' = Cx"+Dy",

see Shorey and Tijdeman [20,  Chapters 2  and 7].

2.  Equations  in  integers  from  an  algebraic  number  field.  We shall  prove
Theorems 1,  2,  3  in  the more general situation when the coefficients of the
binary forms and the unknowns of the equations assume their values in  the
ring  of integers of any given algebraic number field  K.  We shall refer to  the

384  J.-H.  Evertse.  K.  Gyi:iry,  T.  N.  Shorey  and  R.  Tijdeman

general  situation  as  the  relative  case,  and  to  the  case  K  = Q  which  was
considered  in  Section  1  as  the  ahsolute  case.
In  the  sequel  we  shall  use  the  following  notation.  If r:x  is  an  algebraic
number,  then  Iii will  denote  the  size  of  r:x,  i.e.  the  maximum  of the  absolute
values  of the  conjugates  of x.  Iff(X 1 ,  ..• ,  X,)  is  a  polynomial  with  algebraic
coefficients  then  we  denote  by 171 the  maximum  of the  sizes  of the  coefficients
of .f The  ring  of integers  of  the  algebraic  number  field  K  is  denoted  by  (r,K
and  the  group  of  units  of  (1K  by  UK.  For  x.yr=(IK  we  define

:Ydx, y)  =  inf  max(li::xl,  lcYl).(1)

""UK
If  Ct 1 •••••  xkr=K  then  the  ideal  (i.e.  cTK-module)  generated  by  r:x1, ... ,  xk  is
denoted  by  ':x 1 ,  •.. ,  xk)K.  In  .1"dx,  y)  and  /:x 1 ,  ... ,  :xk)K  we  suppress  the
subscript  K  if  no  confusion  can  arise.  If  a  is  an  jdeal  in  K  then  we  shall
denote  the  norm  of  a  over  Q by  N (a).  If  a  =I=  <O),  11 ),  then  we  define  P (a)
as  the  maximum  of  the  norms  of  the  prime  ideals  occurring  in  the  prime
ideal  decomposition  of  !'L  while  if  n =  O'  or  n =  /1  \  then  we  put  P( o)  =  1.
If  a  =  < r:x)  with  some  r:x  EK,  then  we  shall  often  write  P (r:x)  instead  of P (<a)).
Before  stating  our  results  in  this  section,  we  remark  that  Coates'  result
[3],  [4]  mentioned  in  Section  1 was  partially  extended  by  Kotov  [16]  to  the
relative case  as follows.  Let  K  be  an  algebraic  number  field,  let  FE ('K  [X,  Y]
be  an  irreducible  binary  form  of degree  at  least  5  and  let  n 1 ,  ••• ,  n.,  be  non-
zero  non-unit  elements  of  l!K.  Then  all  solutions  of  the  equation

7  F  )  VJ  "s (  )  (x,  y  =  n 1  ... 7r8  Ill  X,  }' F  (I K,  V1,  ... ,  V, E  Z

with  N (  x,  y \)  ~ N 0 ,  i· 1  ~ 0,  ....  v,  ~ 0

(where  N 0  ~ 1)  satisfy  max (M. [Yl)  <  C 7  where  C 7  is  an  effectively  compu-
table  number  depending  only  on  K,  F,  n: 1 ,  .. .,  n:s,  N 0 •  Kotov  also  proved
that  for  x,  YE  (!K  with  N(<x, y)) ~ N 0 ,

(8)  P(F(x,  _rl)  ~ C8  loglog(.1'"+2)  with  . r· = max(INK;Q(x)I.  INK;Q(Yll).

Later  Gyory  [8],  [9]  generalised  Kotov's  results  to  the  case  that
FE l7dX,  Y]  is  any  binary  form  with  w(F)  ~ 3.  Moreover,  he  proved  that
(8)  can  be  replaced  by

(9)  P(F (x,  y))  ~ C 9  log log(.:r(x,  y) + 2).

(1)  For  IX E  K,  let  IX01,  ••• ,  :<1d1 denote the conjugates  of o:  relative  to  K/ Q,  where  d  =  [ K: Q].
For  x,yECi;.  Jet  Hi;(x,y)  be  the  maximum  of  the  absolute  values  of  the  coefficients  of  the
d
binary  form  11 (yi0  X-xu 1Y).  Then  there  are  computable  positive  numbers  c;,;,  cl(,  depending
i= 1.
only  on  K,  such  that  c1' HK (x,  y)  ~ ::rK (x,  y)d  ~ cl( HK (x,  y).

Equal  values  of binary  forms  at  integral  points  385-

Here C 8  and C9  are effectively computable positive constants depending only
on K,  F  and No.  Inequality (9)  is  an improvement of (8)  since for  x,  ye  (  K
both
 .1"(x,  y)  ~ '.max(INKJQ(x)I,  INKJQ(y)l)) 11fKQJ

and (when  UK  is  infinite)
 sup  .f(x, y)  = x.
x,yEVK

Further, (9)  is  a  generalisation of (3)  to  the relative case. For related results.
see SprindZlik  [21],  Gyory  [9],  [13],  [14]  and Shorey and Tijdeman [20].
Let  F 1 ,  .•• ,  Fn  G1,  ... , Gs  be non-zero binary forms in  l' ,dX,  Y]  such
that F;,  G.i  have no common non-constant divisors in K [X,  Y] for  I  ~ i  ~ r,

l~j~s,  that  the  form  F 1  ••• F,G 1  .•. Gs  has  degree  n  and  that
co(F1 .•. F,G 1 ..• Gs)~3. Let

H  = max(2, IFJ, ... ,IF, f,  fG1!,  ... , IGsf).

Denote by  L the·splitting field  of F 1 .•. F" G 1 ... G,  over K  and let  I,  R1,,  h1.  be
the degree, regulator and class number of L,  respectively. Let  :q11  ... .,  Llu:  be
a  (possibly empty)  set  of  distinct  prime  ideals. Further, suppose that  the
number of distinct prime ideals which belong to the set  \ q1 ,  •.• ,  Llu:  or divide
the ideal TI ( R  ( F;,  G j)) is equal to t  and let  P  be the maximum of the norms
i,j
of  these prime  ideals (with  the convention that  P = 2  if  t  = 0.)
Finally,  let  N 0  ~ 2  and

.F =  :F(X,  Y):  F(X,  Y)  = rl F;(X,  Y)k;  for  certain ki. ... , k,EN],
i= 1

s
'!f =  :a(X,  Y):  G(X,  Y)  =  TI  Gj(X,  Y) 1j  for  certain Ii,  ... , l,E  N~.
j= 1

THEOREM  4.  Suppose  that  x, yE  (l_K  are  not  both  ::ero  and  satisj}•

( 10)  ( F ( X,  Y) )  ( G ( X,  Y))  "1  Vu
(  >
dcgF  = -(  )degG ql  · · · qu  ' x,y  x,y  N((x,y))~No

.fc>r  some  FE .F,  GE '.l},  v1,  ... ,  vu E Z.  Then

(  )r+l  )ell  1
(11)  :l"dx,  y)  <exp '(r+s)n4  (C10 (t+l)logP  P  log(NoH),

where  C 10 ,  C11 •  are  effectively  computable  positive  numbers  such  that  C10
depends  on  1,  RL,  hL  and  C 11  depends  only  on  L.
In  (10)  we  considered expressions with  powers of  'x,y'  in  the denomi-
nator to  provide a  convenient generalisation of equation (5)  in Theorem 2 in
which  the  variables x, YE  z  satislled the  condition  (x, y)  =  1.  Note  that

386  J.-H.  Evertse,  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman

Theorem 2 follows  at  once from  Theorem 4  by  taking  K  =  Q,  u =  0,  N 0  =  1.
The  condition  N(('<,  y)) ~ N 0  is  necessary,  since  if x, YE  (r'K  satisfy  (10)  then
so  do  ax, ay for  each  a E  (i_K  with  a ¥  0.  We  remark  that  from  Theorem  4  we
can  deduce  a  new  version  of  Gyory's  theorem  on  (7)  in  [9]  with  another
bound.
From  Theorem  4  we  shall  deduce  the  following  generalisation  of  The-
orem  1.
THEOREM  5.  Let  FE .'7,  GE Cfi.  Let  x, y  be  elements  of  CK  with
G(x, y)-:/; 0  and  N((:'<,  y)) ~No.
If w (FG)  :;;:::  3  then

(12)  P (F(x, y)). > C 12 log log(J"(x, y)+ 2).
G(x,  y)

If w(F):;;::: 3  then

(13)  P  >  C 13loglog(.:nx, y)+2). (  <F(x,y))  )
<F(x, y),  G(x,  y))

Here C 12  and C 13  are effectively computable positive numbers depending only
on  K, F1 ,  .. .,  F,,  G1 ,  •• .,  Gs  and  N0 .
Theorem  1  follows  at  once  from  Theorem  5  with  K  = Q,  N 0  =  1  and
F 1'  .. .,  F,  and  G1 ,  .. .,  G,  being  the  (constant  and  non-constant)  irreducible
factors  of  F  and  G,  respectively,  in  Z[X,  Y].  If  FE (1 K  [X,  Y]  is  a  binary
form  with  w(F):;;:::  3,  then  (13)  yields  (9).
Evertse  [5],  [6]  and  later  Evertse  and  Gyory  [7]  derived  their  upper
bounds for  the  number  of solutions  of (2)  mentioned  in  Section  1 also  in  the
relative  case.  We  shall  now  give  a  generalisation  of Theorem  3 to  the  relative
case.  If x,yEK satisfy  (10)  for  some  FE.F,  GE'IJ,  Vi,  ... ,  VuEZ then  so  do

ClX.  :xy  for  all  'X EK\ ~ 0 ~. Therefore  it  is  natural  to  consider  the  set  of points
on  the  projective  line  P 1 (K)  of  which  the  homogeneous  coordinates  (x: y)
satisfy  ( 10)  instead  of considering  the  set  of solutions  of (10)  itself.  We  shall
say  that  a  projective  point  satisfies  (10)  if its  homogeneous  coordinates  (x:y)
satisfy  (10).  In  Theorem  6  we  use  the  same  notation  as  in  Theorems  4,  5.
Moreover,  let  d =di +2d2  be the degree  of K, where  d1  is  the number  of real
and  2d2  the  number  of  complex  conjugates  of  K.

TiiEOREM  6.  The number of points on P 1 (K)  which satisfy (10)  for  some
FE .?,  G E Cfi,  v 1 ,  .•. ,  011  E Z  is  at  most

7,.3(d+2(d 1 +dz+t)).

Theorem  3  follows  immediately  from  Theorem  6  on  using  that  for  each
point  on  P1 ( Q)  there  are  exactly  two  possible  choices  for  the  homogeneous
coordinates  (x: y)  such  that  x,  y E Z  and  (x,  y)  =  1.
We  shall  prove  Theorems  4  and  6  by  reducing  (10)  to  an  appropriate

Equal  values  of binary  forms  at  integral  points  387

Thue-Mahler equation. To  this  Thue-Mahler equation we shall apply cer-

tain results of Gyory [11]  and Evertse [6].  We  note that Gyory derived his

result by  applying Baker's method concerning linear forms in  logarithms of

algebraic numbers, while  Evertse proved his  result by  applying a method of

Thue and Siegel.

3.  Proofs of Theorems 1, 2, 4 and S and their corollaries. In Lemma 1 we

state some properties of  resultants of  binary  forms  which  will  be  used

throughout the  paper. We  define the  degree of  the  binary form  which  is

identically zero to  be  - 1.

LEMMA  1.  Let  .1.#  be  an  integral  domain  of characteristic  0.

(i)  Let  F,  GE 211 [X,  Y]  be  binary forms  of degrees  p  ;;:,::  0,  q  ): 0,  respect-

ively.  Then for  each  binary  form  Q E  ,qQ [X,  Y]  of degree  p + q- 1 there  exist

hi nary  forms  AQ,  BQ E  .~ [  X,  Y]  such  that

(14)
 (ii)  Let  Fi.  F 2 ,  GE&[X,  lCJ  be  binary  forms  of degrees  ): 0.  Then

(15)  R(F 1 F 2 ,  G)  = R(F 1 ,  G) R(F 2,  G),

R ( G,  F 1 F 2)  = R ( G,  Fi) R  ( G, F 2) .

Proof. (i)  We shall prove that (14)  holds with  Aa,  Ba  having degrees at

most q-1,  p-1,  respectively. Consider the  coefficients of  AQ,  BQ  as  p+q

unknowns. By  equating the coefficients of  the  polynomials on the  left  and

right  hand side of (14),  we obtain a system of  p+q  linear equations in  p+q

unknowns:

(16)  six= b

where sd  is  a (p+q)  x(p+q)-matrix with  entries in  .-!;?,  be  .~p+q and x  is  a

vector  consisting of  the  p+q  unknowns.  It  is  easy  to  check  that  the

determinant of .w is  equal to  R (F,  G)  whereas all entries of b  are divisible by

R(F,  ·G).  This  shows that  (16)  has a  solution x E  .'?fP +q.

(ii)  Let  F,  GE .:!4! [X,  Y]  be binary forms of degree p  ~ 1,  q  ~ 1,  respect-

ively,  and take some factorisations

p  q
F(X,  Y)  =  CT (rx;X-/3;  Y),  G(X,  Y)  =  n (11iX-b1 Y)

i= 1  j= 1

m  some finite  extension K  of  the quotient field  of  .~.  Then

p  q
(17)  R(F,  G)  = CT  0 (ex; Ji-[3; Yi).
i= 1j=1

A  similar  result for  resultants of  polynomials has been proved in  van  der

Waerden [22, § 35]. Formula (17) can be obtained by  a  slight modification of

6  - Acta  Arithmetica XLVIIl.4

388  J.-H.  Evertse,  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman

this  proof.  It is  not  difficult  to  derive  (15)  from  (17)  and  the definition  of the
resultant.  •
We  shall  adopt  the  notations  of Section  2.  Further  put

E(X,  Y)  =  Fi(X,  Y) .. . Fr(X,  Y)Gi(X,  Y) . .. Gs(X,  Y)

and  let  !/={Pi. ... , Pr}  denote  the  set  of distinct  prime  ideals  in  K  which
belong  to  {ql>  ... ,  q,.}  or  divide  TI (R(Fi, Gi)).  We  recall  that,  by  assump-
i,i
tion,  deg E  =  n.  The following  elementary  lemma is  essential in the  proofs  of
our  results.

LEMMA  2.  If  (x,  y) e (!)_i \ {O,  O}  satisfies  (10)  for  some  FE ff',  Ge 'i§,
v1 ,  ... ,  vu E  Z,  then  there  are  non-negative  rational  integers  u 1 ,  .•. ,  Ur  such  that

(18)  (E(x, y))  u 1  u,
-(x_,_y_y_ = P1  ···Pr·

Proof.  Let  (x,  y)e (!)_i: \ {(O,  O)}  and  let  Fe ff',  Ge 'i§.  Since,  by  assump-
tion,  F  and  G  have  no  common  non-consta.nt  factor  in  K  [X,  Y],  we  have
R(F,  G)  =f.  0.  Put  p  = degF,  q  =deg G.  We  recall  that  an  ideal  a  divides  an
other ideal  b if and only  if b c  a.  The greatest  common  divisor  of two  ideals
a  and  b (i.e.  the  smallest  ideal containing  both  a and  b)  is  denoted  by  a+ b.
Let  K'  be  the smallest  extension  such that  (x, y >K'  is  a  principal  idea~ with
generator  {J  say.  Put  x' =  x/1J,  y' = y/b.  Then  x',  y' e (!)K,  and  (x', y')K'  =  1.
Finally,  put
 (F(x, y))K  (G(x, y))K
C=  +  .
(x, Y)i  (x, Y)i

By  (14)  there  are  binary  forms  A(X,  Y),  B(X,  Y)  in  (!)K [X,  Y]  such  that

A(X,  Y)F(X,  Y)+B(X,  Y)G(X,  Y)  =  R(F, G)Xp+q- 1 •

Hence

c(9K,  =  (F(x', y'),  G(x', y'))K'

:'.)  (A(x', y')F(x', y')+B(x', y')G(x',  y'))K'  = (R(F,  G)x'P+q-l>K'·

Similarly  we  have
 c(9K.  :'.)  (R(F, G)y'p+q-i)K ..

Therefore,  c(9K,  :'.)  (R (F,  G) )K'·  But  this  implies  that

(19)  c :'.)  (R(F,  G))K·

From  riow  on we  consider  only  ideals in K, so  we  omit the subscript  K.
Let  (x,y)eCVi\{(0,0)}  be  a  pair  satisfying  (10)  for  some  FeF,  Get;§,
v1 ,  •.• ,  v,.eZ.  Let  p  be  a  prime  ideal  not  belonging  to  {q1 ,  •.• ,  q,,}  which

Equal  values  of binary forms  at  integral  points  389

'
divides  (E (x, y) )/ (x, y )n.  Then :p  divides at  least one of the ideals

(Fi(x, y))/(x, y)degFi  (i  =  1, ... ,  r),  (Gi(x, y))/(x, y/ey,Gi  U =  1, .. ., s).

Therefore :p  divides at  least one of the ideals

(F(x, y))/(x, y)degF,  (G(x, y))/(x, y)degG.

But by (10) this implies that :p  divides c.  Together with (19) this shows that :p
divides  (R(F, G)).  By  combining this  with  (15)  we obtain, on noting that

Fe~, Ge<§, that p divides the ideal TI (R(Fj, Gi)). Hence (E(x, y))/(x, y)n
i,j
is  composed solely of  prime ideals from  Y'.  •
Let  now {J,  n 1 ,  ••. ,  nq  be non-zero elements of  {!)K  such that ni. ... , nq
are not units. Let q'  denote the number of distinct prime ideals of K dividing
(n 1 ••• nq)  and  let  P'=max(2, P(n1 ... n:q)).  Further  suppose  that
maxrn;J ~ PJJ  (.o/> ~ 2).  Let E0 (X,  Y)E {!)K  [X,  Y]  be a binary form of degree n
j
with splitting field  L over K such that w (E0)  ~ 3. In the proofs of Lemmas 3,
4,  5  and  the  proof  of  Theorem 4,  c1 ,  c2,  ••. ,  c5 ,  cl.,  c~,  c3  will  denote
effectively computable positive numbers such that ci. c2 ,  •.. ,  c5  depend only
on/, RL,  hL  and cJ.,  c~, c3  only  on  l.  As  before, N 0 ~2.

LEMMA  3.  Let  x, YE (DK  satisfy

E0 (x, y)  = f3n~1 ••• n;q,  N( (x, y))  ~ N 0

for  certain  non-negative  integers  w 1 ,  .•• ,  wq.  Then

max([X], IYJ)  <exp {n 2 (q+ l)((ci(q' + 1) logP't'+ 1 PJ1 (log &')log(Niorrolrm> }.  '

Proof. This is  an immediate consequence of Theorem 2 of Gyory [11]
(see also  [12]).

LEMMA  4.  (i)  Let  a be  an  ideal  in  K.  Then  a[L:KJhL  is  a  principal  ideal.

(ii)  Let  a  be  a  non-zero  element  of K  with  IN K/Q(tX)I  = m  and  let  v  be  a
positive  integer.  Then  there  exists  a  unit  &  in  K  such  that  la:e0 I ~ (mc~)1/[K:QI.

Proo f.  (i)  The ideal ( a(!)JhL  is  obviously principal in  L.  This  implies

that the ideal  a[L:KJhL  =  N LJK (( a(?JL)hL)  is  principal in  K.
(ii)  By  Lemma 6  of  [15],  for  each a:' EL  with  IN Lta(ix')I  =  m'  =I=  0  and
v' EN,  there exists a  unit  17  in  L  such that

kx' 11"'1  :::;;  (m') 1/[L:!ZI c3 ·

Apply this result with a'  =a,  v'  =  v [L: K].  Put e =  N LJK (17).  Then, on taking

C2  =  C~,
 laevl  =  la[L:X] ev[L:IC)I 1/[L:K] =  IN L/¥. (1X1'fv[L:.l'.J)j  1/[L:K]

:;o;  Jaliv[L:Kl}  ~JN .L,IQ(1X)l 1/[L:QI c?L:KJ  =  (mci)l/[K:<ZI,  •

390  J.-H.  Evertse,  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman
.
In  the  lemma  below,  b  will  denote  a  non-zero  integral  ideal.  As  before,
N0  ~ 2  and  P = P(p 1 ,  ... ,  p,)  if  t  ~ 0,  P =  2  if  t =  0.

LEMMA  5.  Suppose that  x, YE  (!;K  are  not  both equal to  zero and that

(20)  <Eo(X, y)) - b  "1  "t
<  - :Pt  ···:Pt, x, y)"  N( <x, y)) ~ N 0

for  certain  non-negative rational  integers u1 ,  .•• ,  u1 •  Then

~(x, y)  ~exp {n3 ((c4 (t+1) log Pf 1 Pt2 log(N olEo IN(b)) }.

Proo f.  Let  vi>  w;  be  rational  integers  such  that

0~ V;  ~ [L:K]hL-1  and  U;  = [L:K]hLw;+V;  (1  ~ i  ~ t).

By  Lemma  4  (i),  the  ideals  p~L:KlhL are  principal.  Moreover,

N (p~L:K]hL) ~ pIL:Klhi.

Hence,  by  Lemma  4  (ii)  with  v =  1,  there  exist  n 1 ,  ... ,  n1 E  {!)K  such  that
< >  [L:K]hL  d
TC;  = P;  an

(21)  for  i  =  1,  ... , t.

There  exists  a  fJ0 e (9K  such  that  <fJo)  =  bp~
1 ... :p:1  (x, y)n and

(22)

Now
 INK/Q(/3o)I  ~ N(b) N'Q  pIL:KlhL(t+  ll.

Hence,  by  Lemma  4  (ii),  there  exists  a  unit  s  in  K  such  that  for  p =  s" {30 ,

(23)

Moreover,  by  (22),

(24)

Now  Lemma  5 follows  immediately  from  Lemma  3,  (21),  (23),  (24),  by  taking
P' = P,  q' = q =  t.  •
Proof of Theorem  4.  Theorem 4 follows  at  once from  Lemmas  2 and
5  by  observing  that  there  exists  a  constant  c~ with

f£l  S: (nH)c'.3(r+s)  h  H  (2  'FI  T  fGl  'GI)
1.1.J I  - W  ere  =  max  d  r  t  I•  .. · ,  I r  r I•  Iv 1 I•  .. • ,  I v  s I  •  •

Proof  of  Theorem  2.  Take  K  =  Q,  u = 0,  N 0  = 1  in  1:heorem  4.  •

Proof of Corollary 5.  Let Fi(X,  Y),  ... , F,(X,  Y)eZ[X,  Y]  be binary
forms  such  that  F 1 ,  .. ., F,,  P/Q  are  multiplicatively  independent  in  Q(X,  Y)
for  all  relatively  prime  binary  forms  P,  Q in  Z[X,  Y]  with  ro(PQ)e {1,  2}.

Equal  values  of binary  forms  at  integral  points  391

c6  and c7  will  denote effectively computable positive numbers depending only
on  F 1 ,  •.. ,  F,.  If  x  and  y  are  rational  integers  with  (x,  y) = 1  and
F 1 (x,  y)  ... F,(x, y)  =  0  then  max(lxl, IYll  ~ c6 •  Let  x  and  y  be  rational
integers such that max(lxl, lyl) > c6 ,  (x, y)  =  1 and F 1 (x, y),  ... ,  F,(x, y)  are
multiplicatively  dependent in  Q.  Let  11 ,  .•• ,  I,  be rational integers, not  all
zero, such that

(25)
Let  r
fl Fi(X,  Yli =  P(X,  Y)/Q(X,  Y),
i=I
where P,  Q E Z  [ X,  Y]  are relatively prime  binary forms. Then (25)  implies
that
(26)  P(x, y)  =  Q(x, y),  (x,  y)  =  1.

Since F 1 ,  .•• ,  F,  are multiplicatively independent, P  =F  Q.  Moreover, P/Q  can
not be a constant =F  1 for  otherwise (26)  is  impossible. Therefore w(PQ)  ~ 3.
Let  G1 ,  ... ,  Gs  be the (constant and non-constant) irreducible factors of PQ
in  Z[X, Y].  Then w(G1 ... Gs);:::3  and  G1 ,  •.• ,  Gs  are irreducible factors
of  F 1 .•. F,.  Together  with  (26)  and  Theorem  2  this  shows  that
max(lxl, lyl)  ~ c1 .  This  proves Corollary 5.  •
Proof of  Theorem 5.  In  what  follows,  c8 ,  c9 ,  ••• ,  c18  will  denote
effectively  computable  positive  numbers  depending  only  on  K,  N 0 ,
F1 ,  ..• ,  F.,  G1 ,  .•• ,  Gs. We assume that xy :/=  0 which is  no restriction in the
proofs of (12)  and (13).
First  suppose that  F (x,  y)  =  0.  Then  F; (x; y)  =  0  for  some i  with
1 ~ i ~ r.  Together with  xy  =F  0,  this  shows that Fi(X,  Y)  has at least two
non-zero terms. Hence

max (IN K/Q(x)I,  IN K/Q(y)I)  ~ea.

By  Lemma 4 (ii),  there is  a unit  e in  K  such that I ex I ~ c9 .  Now  F; (ex,  ey). ·
=  0  implies that I ey I~ c10•  This  proves (12)  and (13)  in  case F (x, y)  =  0.
Now  suppose that  F(x, y)  ¥=  0.  Put  p =  degF, q =deg G.  In  order to
prove (12)  it  suffices to  show that

(27)  p (<F(x,  y!) /<G(x,  Y~>) ~ c11 loglog(Er(x, y)+2).
(x,  y)  (x,  y)

For if log log(.~"(x, y) + 2);,;;; c12 : = c\} N 0  then (12) holds for  an appropriate
value of  c12  and otherwise (27)  implies that

p (F(x, y)) =  p ((F(x, y))/<G(x, y))).
G(x, y)  (x, y)P  (x, y)q

and (12)  follows  from  (27).

392  J.-H.  Evertse,  K.  Gy<:5ry,  T.  N.  Shorey  and  R.  Tijdeman

We  shall  now  prove  (27).  Let

Q =  p (<F(x,  y))/(G(x, y)))
(x,  y)P,  (x, y)q

and  let  .!1  = { q1 ,  ... ,  qu}  be  the  set  of all  prime  ideals  with  norm  ~ Q.  Then

(F(x, y))  (G(x, y))  v 1  vu
<  >p  =  <  >q  -ql  ... q,.
x,y  x,y
(28)

for  certain  rational  integers  v1 ,  ... ,  v,..  Note  that  the  prime  ideals  dividing
n (R(Fj, Gj))  have  norms  at  most  C13.  For  each  prime  number  p  there  are
i,j
at  most  [K: Q]  prime  ideals  in  K  dividing  (p) and  all  of them  have  a  norm
which  is  a  power  of  p.  Since  there  are  at  most  2Q/log Q  rational  primes  not
exceeding  Q (cf.  [18])  we  have  u ~ c 14 Q/log Q.  Now  Theorem  4  implies  that

loglog(f!((x,  y)+2)  < c15 Q.

This  proves  (27).
We  shall  now  prove  (13).  Suppose  that  w(F)  ~ 3.  By  (14)  there  exist
binary  forms  A 1 ,  A 2 ,  B1 ,  B2  in  (l)K  [X,  Y]  such  that

Ai(X,  Y)F(X,  Y)+Bi(X,  Y)G(X,  Y)  =  R(F,  G)Xp+q- 1,

A 2 (X,  Y)F(X,  Y)+B 2 (X,  Y)G(X,  Y)  =  R(F,  G) p+q- 1 •

This  shows  that  the  ideal  (F(x, y),  G(x, y))  divides  (R(F,  G))(x,  y)p+q- 1.
In  view  of (15)  this  implies  that

(29)  P( (F(x, y),  G(x, y))) ~ c 16·

By  applying  (12)  with  s =  1  and  G1  =  1,  we  obtain

(30)  P(F(x,  y))  > c 17 loglog(:?C(x,  y)+2).

If log log (.~l'(x, y)+ 2)  ~ c16 c1l  =: c18 ,  then  (13)  follows.  If

loglog(f!((x, y)+2) >  c18
then  (29)  and  (30)  give

P  = P(F(x, y))  >  c 17 loglog(.¥(x, y)+2). (  (F(x, y))  )
(F(x, y),  G(x, y))

This  completes  the  proof  of  ( 13).  •
Proof  of  Theorem  1.  Take  K  =  Q.  N 0  = 1  in  Theorem  5.  Let
F 1 ,  ... ,  F,  and  G 1 ,  ... ,  Gs  be  the  (constant  and  non-constant)  irreducible
factors  of  F  and  G,  respectively.  •
Proof  of  Corollary  2.  We  have  either  (i)  w(F) ~ 3  or  (ii)  F  = c·Q"

Equal  values  of binary  forms  at  integral  points  393

where CE Q*,  aEZ,  a>  0 and Q is  a definite quadratic form with  coefficients
in  Z  or  (iii)  F  =  c.U1 IJ2  where cE Q*,  a,  bE Z,  a>  0,  b > 0  and L 1 ,  L2  are
non-proportional  linear  forms  with  coefficients  in  Z.  Put  p = deg F,
q =deg G.
Let  x, y  be integers with  (x, y)  =  1.  By  applying (14) with  Q =  xp+q-i,
we  obtain  that  (F(x, y),  G(x, y))  divides  R(F, G)xp+q- 1•  Similarly,
(F(x, y),  G(x, y))  divides R(F,  G)yp+q- 1 .  Hence

(31)  (F(x, y},  G(x, y))iR(F, G).

Now  suppose that  x, y  are  integers  with  (x, y)  =  1,  G (x, y)  #  0  and
F(x, y)IG(x, y).  Then (31)  implies that

F(x, y)IR(F, G).

We  claim  that  max(lxl, IYI)  can be  bounded by  an  effectively  computable
number depending only  on the heights and degrees of F  and G.  In  case (i)
this follows  from  Corollary 1 applied with  t  =  0.  In  case (ii)  it  follows  from
the fact  that IQ (x, y)j  ~ ·c19 {max(Jxl, lyJ) } 2  for  some effectively computable
positive number c19  depending only  on the height of Q.  Finally,  in  case (iii)
we  have
 JLi(x, y)I  ~ jc- 1 R(F, G)j,  IL 2 (x,  y)j  ~ jc- 1 R(F,  G)I.

Since L 1  and  L 2  are non-proportional, the  claim  is  also justified  in  this
case. •
Proof  of  Corollary  3.  We  have  p > q  ~ 0  where  p =  degF,  q
=deg G.  Let  x, y  be  integers with  G(x, y)  #  0  and F(x, y)IG(x, y).  Put d
= (x,  y),  x 0  =  x/d, Yo= y/d.  Then dp-qF(x 0 ,  y0)IG(x0 ,  y0 ).  Hence, by Corol-
lary  2,  max (Jx0 j,  jy 01)  and therefore d  are bounded by effectively computable
numbers depending only  on the degrees and heights of  F  and G.  111
Proof of  Corollary 4.  Let  D  be the greatest common divisor  of F
and  G  in  the  ring  Z [X,  Y].  Put  F 1  =  F/D  and  G1  =  G/D.  Let  x, y  be
rational integers with  (x, y) =  1 and F (x, y)  =  G (x, y).  If F (x, y)  =  0,  then
max(jxj, jyj)  does not exceed a  computable number depending only  on the
degree and height of F.  Suppose that F (x, y)  #  0.  Then

Fi(x, y)  = Gi(x, y).

Hence Fi(x, y)yi(x, y)  divides both {Fi(x,  y)} 2  and {Gi(x,  y)} 2 .  In view  of
(31)  this  implies

Since F JG  is  a  constant multiple  of  a  power of  a  linear  or  an indefinite
quadratic form  if  and only _if  F 1 G1  is,  Corollary  4  follows  at  once from
Corollary 2 with  F 1 G1  and {R(F 1 ,  G1)} 2  replacing F  and G,  respectively. •

394  J.-H.  Evertse,  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman

4.  Proofs  of Theorems  3  and  6.  We  shall  use  the  notation  of  Section  2.
Let  // = ( p1 ,  .•. ,  :Pt}  be  a  finite  set  of prime ideals  in  (!JK  and  let  a be ·a  fixed
ideal  in  K.  Let

W(a, 9")  =  {ccEK:  3u 1 ,  ... ,  JJiEZ  such  that  <cc>=  ap~
1 ... p(}.

Note  that  W(<l),  9")  is  just  the  group  of  S-units  where  Sis  the  set  of
valuations  containing  the  archimedean  valuations  on  K  and  the  valuations
corresponding  to  :Pi.  ... , :Pr·

LEMMA  6.  Let f/ be a .finite set of prime ideals in  mK  of cardinality t  and
let  a,  b  be .fixed non-zero ideals in  K.  Then the number of solutions of the
equation

(32)  x+ y =  1  in  (x, y)E  W(a, 9")  x W(b, ,9')

is  at  most 3  x 7d+ 2<di +dz +r>.

Proof.  Suppose that  (32)  is  solvable and  let  (A.,µ)  be  a  fixed  solution  of
(32).  Let  U  =  W( (1),  .9").  Then (x, y)  is  a solution  of (32)  if and  only if there
are  e, 1'/E U  such  that  x =  A.e,  y =  µyt  and  A.e+µ'f/ =  1.  But  by  Theorem  1

of·Evertse  [6]  there  are  at  most  3x7d+ 2<di+d 2 +t>  pairs  (e,rt)eU 2  with
..i.e+ µrt= i.  •
Let  F(X,  Y)EK[X,  Y]\{O}  be  a  binary  form.  The  content  of  F  with
respect  to  K,  denoted  by  cK (F),  is  defined  as  the ideal  in  K  generated  by  the
coefficients  of  F.  We  shall  need  the  following  generalisation  of  Gauss'
Lemma:  if  F(X,  Y),  G(X,  Y)  are  binary  forms  in  K  [X,  Y]  then

(33)  cK(FG) =  cK(F)· cdG).

This  follows  for  example  from  Lang  [17,  Proposition  2.1].
For  any  point  (x:y)E P 1 (K),  the  homogeneous  coordinates  x, y  can  be
chosen  so  that  x, YE  (!JK·  Hence  Theorem  6 is  an  immediate  consequence  of
Lemma  1  and  Lemma  7  below.

LEMMA  7.  Let  E0 (X,  Y)e K [X,  Y]  be  l;l  binary form  of degree n  with
ro(E 0)  ~ 3 and let  (p 1 ,  ... ,  p1 ]  he a set of prime ideals in  K.  Then the number
of points (x:y)eP 1 (K)  satisfying

<Eo (x, y))  u 1  u1
(E  ) <  >
n  =  :Pt  ···:Pt
ck  o  x, Y
(34)
 .  n3(d+2(d1 +d 2 +t))
for  some u 1,  •.• ,  UrE Z  is  at  most 7  .
Proo f.  There  exists  a  field  M  of  degree  at  most  n ( n - 1 )( n - 2)  over  K
which  contains  the  coefficients  of  three  pairwise  non-proportional  linear
forms  dividing  E0  in  M[X,  Y],  A(X,  Y),  B(X,  Y),  C(X,  Y)  say.  Let  s1 ,  2s2
denote  the.  number  of  real  and  complex  conjugates  of  M,  respectively,
and  let  Qi.  ... ,  q,,  be  the  prime  ideals  in  (!JM  lying  above  p 1 ,  .•. ,  :p1 .  Then

Equal  values  of binary  forms  at  integral  points  395

(35)  S1 +s2 +u ~ n(n-l)(n-2)(d1 +d2+t),  [M: Q]  ~ n(n-l)(n-2)d.

Let (x:y)EP 1 (K)  be a point satisfying (34) for certain u1 ,  ... ,  UrEZ. Since
the l~ft-hand side of (34)  is  an integral idea~ the ui  are non-negative. Since
the  lmear  forms  A, B  and  C  are  linearly  dependent, there are  non-zero
elements ex, fJ  E M  such that

ocA(X,  Y)+fJB(X,  Y)=C(X,  Y).  identically in  X,  Y.

Put  u  =  ocA(x,  y)/C(x, y),  v = fJB(x,  y)/C(x, y).  Then  u+v = 1.  Moreover,
by  (33),  the integral ideals

<A(x,  y))M

cM(A)  <x, Y)M'  <B(x,  y))M

cM(B)  <x, Y)M'  <C(x, y))M

cM(C) <x,  Y)M

divide the left-hand side of (34) and are therefore composed of prime ideals
from!/= {q 1,  .•• ,  qu}.  lt follows  easily that uEW(a,  !/),  vEW(b,  !/)where

a= <oc>M cM(A)/cM(C),  b =  <fl>M cM(B)/cM(C).

Moreover the projective point (x:y) is  completely determined by u,  v.  Now a
combination of Lemma 6 and (35) with the facts mentioned above yields that
the number of points (x:y)EP 1 (K)  which satisfy (34) for  certain u1 ,  ••• ,  14EZ
is  at  most

Proof of Theorem 3.  Apply  Theorem 6 and use that for  each point
on  P1 ( Q)  there  are  exactly  two  possible choices for  the  homogeneous
coordinates (x:y)  such that x, yEZ and (x, y)  =  1.  •

References

[l]  A.  Baker, Contributions  to  the  theory  of diophantine  equations,  Philos. Trans. Roy. Soc.
London A  263 (1968), pp.  173-208.
[2]  - 'Iranscendental  number  theory,  2nd ed., Cambridge University  Press, Cambridge etc.,
1979.
[3]  J. Coates, An effective p-adic  analogue  of a  theorem  of Thue,  Acta Arith.  15 (1969), pp.
279-305.
[4]  - An effective  p-adic  analogue  of a  theorem  of Thue  11,  The  greatest  prime factor  of a
binary  form,  ibid.  16 (1970), pp.  399-412.
[5]  J.-H. E vertse, Upper  bounds for  the  numbers  of solutions  of diophantine  equations,  Math.
Centre Tract  168, Centr. Math. Comput. Sci., Amsterdam, 1983.
[6]  - On  equations  in  S-units  and  the  Thue-Mahler  equation,  Invent. Math. 75  (1984), pp.
561-584.
[7]  J.-H.  Evertse and  K.  Gyory,  On  unit  equations  and  decomposable  form  equations,
J.  Reine Angew. Math. 358 (1985), pp.  6--19.
[8]  K.  Gyory, On  the  greatest  prime  factors  of decomposable forms  at  integer  points,  Ann.
Acad. Sci.  Fenn., Ser. A 1,  Math. 4 (1978/1979), pp. 341-355.

396  J.-H.  Evertse,  K.  Gyory,  T.  N.  Shorey  and  R.  Tijdeman

[9]  K.  Gyory, Explicit  upper  bounds for  solutions of some diophantine  equations,  ibid.  5 (1980),
pp.  3-12.
[!OJ  - Resulcats  ejfectifs  sur  la  representation  des  entiers  par  des  formes  decomposables,
Queen's  Papers  in  Pure  and  Applied  Math.,  No.  56.  Kingston,  Canada,  1980.
[11]  - On  the  representation  of  integers  by  decomposable  forms  in  several  variables,  Pub!.
Math.  Debrecen  28  (1981),  pp.  89-98.
[12]  - On  S-integral solutions  of normform, discriminant form  and  index form  equations,  Studia
Sci.  Math.  Hungar.  16  (1981),  pp.  149-161.
[13]  - Bounds for  the  solutions  of norm  form,  discriminanl form  and  index  form  equations  in
.finitely  generated  integral  domains,  Acta.  Math.  Hungar.  42  (1983),  pp.  45--80.
[14]  - On  norm  form,  discriminant  form  and  index  form  equations,  in:  Topics  in  Classical
Number  Theory,  Coll.  Math.  Soc.  J.  Bolyai  34,  North  Holland  Pub!.  Comp.,  Amsterdam
etc.,  1984,  pp.  617-676.
[15]  K.  G yo ry  and  Z.  Z.  Pa pp,  Effective  estimates for  the  integer  solutions  of norm form  and
discriminant  form  equations,  Pub!.  Math.  Debrecen  25  (1978),  pp.  311··325.
[16]  S.  V.  Kotov,  The  Thue-Mahler  equation in  relative fields  (Russian),  Acta.  Arith.  27  (1975),
pp.  293-315.
[17]  S.  Lang,  Fundamentals  ()f  diophantine  geometry,  Springer  Verlag,  New  York  etc.,  1983.
[18]  J.  B.  Rosser  and  L.  Schoenfeld,  Approximate  formulas  for  some  functions  of prime
numbers,  Illinois  J.  Math.  6  (1962),  pp.  64-94.
[19]  T.  N.  Shorey, A.  J.  van  der  Poorten,  R.  Tijdeman and  A.  Schinzel,  Applications  of
the  GeI'fond-Baker  method  to  diophantine  equations,  in:  Transcendence  Theory:  Advances
and  Applications,  Academic  Press,  London  etc.,  1977,  pp.  59-77.
[20]  T.  N.  Shorey and  R.  Tijdeman,  Exponential  diophantine  equations,  Cambridge  Univer-
sity  Press.  1987.
[21]  V.  G.  Sprindfok,  Classical  diophantine  equations  in  two  unknowns  (Russian),  Nauka
Moskva,  1982.
[22]  B.  L.  van  der  Waerden,  Algebra  !,  7.  Aull,  Springer  Verlag,  Berlin  etc.,  1966.

DEPARTMENT  OF  PURE  MATHEMATICS
CENTRE  FOR  MATHEMATICS
AND  COMPUTER  SCIENCE
I 098  SJ  Amsterdam
The  Netherlands

MATHEMATICAL  INSTITUTE
KOSSUTH  LAJOS  UNIVERSITY
40 I 0  Debrecen
Hungary

SCHOOL  OF  MATHEMATICS
TATA  INSTITUTE  OF  FUNDAMENTAL  RESEARCH
Bombay  400005
India

MATHEMATICAL  INSTITUTE
UNIVERSITY  LEIDEN
2300  RA  Leiden
The  Netherlands
 Received  on  30.12.1985  (1580)
