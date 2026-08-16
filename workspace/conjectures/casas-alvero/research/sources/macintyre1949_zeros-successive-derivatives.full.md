<!-- source: https://www.ams.org/journals/tran/1949-067-01/S0002-9947-1949-0032743-0/S0002-9947-1949-0032743-0.pdf | converted from PDF -->

ON  THE  ZEROS  OF  SUCCESSIVE DERIVATIVES
OF  INTEGRAL  FUNCTIONS

BY
SHEILA  SCOTT  MACINTYRE

1.  The  Gontcharoff  polynomials
 (n-D
Go(s) =  1;  Gn(z; zlt z2, ■ ■ ■ , zn) =    f    dz'  f     dz"  f         dz"»      (n  ^  1)
J  h  J  z1  J  zn

have  applications  to  a  certain  class  of  interpolation  problem  (Whittaker
[7])(0-  In  this  paper  I  obtain  some  formulae  connected  with  these  poly-
nomials  and  use  them  to  improve  and  extend  a  theorem  due  to  Levinson  [3,
4],  and  to  shorten  the  proof  of  and  extend  a  theorem  due  to  Schoenberg  [6].

Levinson's  Theorem.  If  f(z)  is  an  integral  function  satisfying

log  M(r)
lim sup—^-—  <  .7199,
r-.»  r

and  iff(z)  and  each  of its  derivatives  have  at  least  one  zero  in  or  on  the  unit  circle,
thenf(z)=0.

The  constant  .7199  is  not  the  "best  possible"  but  cannot  be  replaced  [5]
by  a  number  as  great  as  .7378.
The  "best  possible"  value  of  this  constant  is  known  as  the  Whittaker
constant  IF.  Among  new  results  in  this  paper,  I  prove  that  IF  cannot  be  less
than  .7259.

Schoenberg's  Theorem.  Iff(z)  is  an  integral  function  satisfying

log  M(r)        ir
lim sup-<  — ;
r-,»  r  4

and  if f(z)  and  each  of its  derivatives  have  at  least  one  zero  in  the  segment  — 1 ^  x
— 1 of the real  axis,  thenf(z)=0.

The  constant  x/4  is  the  "best  possible"  as  shown  by  the  example
cos  (7tz/4)  4-sin  (7tz/4).
I  have  to  thank  Mr.  M.  H.  Quenouille  and  his  staff  of  computers,  Sta-
tistics  Department,  Aberdeen  University,  for  performing  the  calculations
arising  in  §3.

Presented  to  the  Society,  October  30,  1948;  received  by  the  editors  August  17,  1948.
(')  Numbers  in  brackets  refer  to  the  references  cited  at  the  end  of  the  paper.

241

242  SHEILA  S.  MACINTYRE  [September

2.  Following  the  notation  used  by  Levinson  [3],  let

H0(z)  =  1;  H„(zx,  z2,  •  • •  ,  zn)  =  Gn(0;  Zt,  z2,  • ■ •  ,  z„)  (n  â  1),

Mn  =  max    | Gn(z0;  *t,  z2,  ■ ■ •  ,  z„)  |                         (all  |  zr |  g  1),

Ln  =  max  |  Hn(zi,  z2,  ■ •  ■ , z»)  |                             (all  | zr |  =  1).

We  first  require  two  inequalities  (2.1)  and  (2.4)  due  to  Levinson  and  (for
the  sake  of  completeness)  give  his  proof.  Since  by  definition

G„(zo;  zi,  •  •  •  ,  zn)  =  Hn(zi,  z2,  •  ■ •  ,  z„)  —  Hn(zo,  z2,  •  ■ •  ,  zn),

therefore,  by  Taylor's  Theorem

G„(Zo!  Zl,  Z2,   •   •   ■   ,  Zn)   =    ¿-J    -  Hn-r(Zr+l,  Zr+2,   •   •  •   ,  Z„)
r=i        r\

—   2-1    -  tln-r\Zr+l,  Zr+i,    '    '    •   ,  Zn).
r_i        r\

Hence
 I  A      |  2l  —  2o  |
G„(zo;  Zt,  • •  •  ,  z„)  |  Ú  2-1  -Ln-T
r-l  r\

and,  if  we  write  2a  =  arg  Zi —arg  zo,

f   "    2 | sin  rot \  )
(2.1)  Mn-è      max      {  £  —--£n_rV  .
0SaS7r/2     I  r-1  r!  j

By  Euler's  formula  for  homogeneous  functions,

«Gn  =    2-1   Zr ->
r-0  dzr

and  since
 flGn
(2.2)  -=  G„_i(zo;  Zi,  • • •  ,  zn),
dzo

dGn
(2.3)  -   =    — Gr_l(z0;  Zl,   •   •   •   ,  Zr-x)   X  Gn-rW,  Zr+X,  •   ■   ■   ,  Zn)  (fni    1),
dzr

we  have  the  inequality
 n
(2 . 4)  nMn   ^    Mn-l  +   22  Mr-xMn-r.
r-l

It  is  obvious,  as  Levinson  points  out,  that  Zi  =  l,  L2 =  3/2,  Mx =  2,  and
hence  from  (2.1)  he  obtains  ikf2^(3/2)31'2<2.5981,  Af3<3.6379.  By  special

1949]  SUCCESSIVE DERIVATIVES  OF  INTEGRAL  FUNCTIONS  243

choice  of  the  zr  he  shows  that  these  values  are  "accurate"  and  that
in  fact  Mi =  (3/2)31'2  and  M¡>3.6378.  It  can  also  be  proved  [4]  that
L3 =  2-1[2(5)1/2+3]1/2-r-6-1[6(5)1/2-2]1/2<1.9299,  and  again,  by  use  of  (2.1)
he  obtains  [4]  AÍ4<4.8414.  He  then  uses  (2.4)  to  find  upper  bounds  for  Ms,
Mi,  Mi,  Mi,  M9,  and  (by  induction)  Mn-  In  fact  Mnúrn+1  (n>l)  where
r<  1.389.  He  remarks  that  this  method  would  presumably  yield  a  better
value  of  r  if  accurate  values  of  some  further  members  of  the  sequence  Mn
were  worked  out  before  resorting  to  the  use  of  formula  (2.4).  However  the
problem  of  determining  Z,4 or  M¿  exactly  is  not  simple  and  for  higher  Ln,  Mn,
this  does  not  seem  a  very  promising  line  of  approach.
3.  It  is,  however,  possible  to  obtain  upper  bounds  for  Lt,  and  so  on,  by
using  another  interation  formula  involving  both  sequences  L„  and  Mn.  For
Euler's  formula  gives
 A        dHn
nun   =   2-,   Zr -
r=l  dZr

and  since
 dHn/dZr  =    —  Z7r_i(Zi;  Z2,  •  •  •   ,  ZT-x)  X  Gn-r(Zr',  Zr+X, '  '  '   ,  Zn),

we  have  the  inequality
 n
(3 . 1)  nLn  á    22  Lr-iMn-r.

In    particular,    when    w = 4,    4L^LoMz+LxM2+L2Mx+L%Mo,    yielding  F4
<2.7915,  and  (2.1)  gives  Afs^maxoSaáT/2  <¡>s(oi) where

<j>6(a) =  5.5830  | sin  a  \ +  1.9299  | sin  2a  \ +  (1/2)  | sin  3a  |

+  (1/12)  | sin  4a  |  +  (1/60)  | sin  5a  |.

The  maximum  on  this  curve  lies  between  70°27'  and  70°28'  and  shows  that
Mi<  6.8223.
Proceeding  in  this  way  by  alternate  use  of  (2.1)  and  (3.1),  we  find  upper
bounds  for  L8,  Le,  Li,  Ls,  Ls,  Lxo;  Mt,  Mi,  Ms,  M<¡, and  Mxo  (see  appendix).
The  curves  whose  maxima  have  to  be  determined  may  be  taken  as

<f>6(a) =  7.6112 | sin a \ +  2.7915 | sin 2a\  +  0.6433  | sin 3a\

+  (1/8)  | sin  4a  |  +  (1/60)  | sin  5a  |  +  (1/360)  | sin  6a  |

(maximum  between  69°31'  and  69°32'),

<Pi(a) =  10.5078 | sin a \ +  3.8056  | sin 2a | +  0.9305 | sin 3a |

+  0.1609 | sin 4a | +  (1/40)  | sin 5a | +  (1/360) | sin 6a | +  2/7!

(maximum  between  69°54'  and  69°55),

244  SHEILA  S.  MACINTYRE  [September

<t>s(a) =  14.4630 | sin a | +  5.25391 sin 2a | 4- 1.26861 sin 3a |

+  0.2327 | sin 4a | +  0.0322 | sin $a\  +  (1/240) | sin 6a]

+  2/7!+  2/8!  (maximum  between  69°49'  and  69°51'),
«¿»(a) =  19.9269241 sin a | +  7.2320 | sin 2a | +  1.7513 | sin 3a \
+  0.317141 sin 4a | +  0.04653] sin 5a | +  0.00537 | sin 6a |

+  3/7!  4-  2/8!  +  2/9!  (maximum between  69°49'  and  69°51'),
<f,io(a) =  27.44241 sin a | +  9.9635 | sin 2a | 4- 2.4105 | sin 6a |
+  0.437825 | sin 4a | +  0.0634267 | sin 5a | +  0.0077542 | sin 6a |

+  3.8598/7!  +  3/8!  +  2/9!  +  2/10!

(maximum  between  69°49'  and  69°51').

It  can  be  verified  by  direct  computation  that

(3.2)  M„ <  2(1.3775)*«  (¿=1,2,3),
(3.3)  Mk  <  (1.3775)*+1  (¿  =  4,5,6,7,8,9,10),

(3.4)  Lk<  (1.3775)"  (¿=1,2,3,4),

(3.5)  £*  <  0.7692(1.3775)*  (¿  =  5,6,7,8,9,10).

From  (3.1)  we  have

nLn <  Mn-t  +  Mn-2 +  1.5Mn-3  +  1.9299Mn-t  +  2.7915ilf„_6

n-6
(3.6)  +  22Lr-xMn-r  +  4.8414Zri_6 +  3.6379£n_4 +  2.5981Lre^
r=6

+   2Ln-2  +  Ln-X.

If  we  assume  (3.3)  and  (3.5)  are  satisfied  also  for  ll^¿^w  — 1,  then  (3.6)
gives,  if  we  write  7 = 1.3775,  ¡j. =0.7692,

nLn  <yn  +  y""1  +  1.5t"-2  +  1.9299t"-3  +  2.79157"-4

+  n[(n  -  10)7« +  4.8414t"-6  +  3.6379t"-4  +  2.5981t"-3

+  2t"-2  +  T""1]  <  nßyn  -  0.0005t"-5.

Hence  Ln<pyn-
This  proves  (3.5)  is  true  for  all  ¿^11,  by  induction.
From  (2.1)  for  w =  ll,
 I   •    2 | sin  ra. |  )  "2
Mn   ^        max       <   2-,   -Ln-r>     +    2-,   —Ln-r
oSai,/!    I  r-l  rl  )  r_7    r!
"     2
<  mt"-7    max    4>(a) +22  —  77_r
Oíoái/2  r-7    f\

1949]  SUCCESSIVE  DERIVATIVES  OF  INTEGRAL  FUNCTIONS  245

where '     2 | sin  ra  I
*(«) =  E  ———-y7-.
r-l  r\

which  has  its  maximum  between  69°49'  and  69°51',  giving

max   $(a)  <  16.8520.

Oâaâi/2

Hence V2       2    1
r-i  ,-
L7!       8!   t
 2    1
Mn  <  16.8520MT"-7  +  Tn_7   -  1-+
7        9!    y2
2  r        i        i  i
<  16.8520MT"-7 +  7"-7—    1 H-1-h  • • •
7!L        8t      (8t)2  J

2t"-7
=  16.8520MT""7 -\-'-
7!(1 -  I/87)

<  T"-7[12.9626  +  0.0006]

<  Tn+1-

This  proves  (3.3)  for  all  ¡fee; 11, by  induction.
Since  G„  is  analytic  in  the  zr  it  follows  that  its  maximum  modulus  is  as-
sumed  when  each  zr  is  on  the  circumference  of  the  unit  circle.  Thus  we  have
the  following  theorem.

Theorem  I.  If  zTis  a  sequence  of points  in  the  unit  circle,  then

Mn  =  max  I G„(z0; zh  z2, ■ ■ ■ , *„) |  <  (1.3775)"+1       (n  è  4).

4.  Now  consider  the  Gontcharoff  polynomials  for  the  case  discussed  by
Schoenberg,  namely  G„(x;  xi,  x2,  •  •  • ,  x„)  where

-  1  á  «r  á  +  1  (1  á  r  á  »).

Consider  any  one  of  the  2n_r  polynomials

Gn(x;  xt,  x2, ■ ■ ■ ,  xr,  +1,  ±  1,  • • • ,  +1)  (1  Ú  r  g:  n),

dGn
-=  — Gr_i(x;  xt,  Xi,  ■ ■ ■ ,  xr_i)  X  Gn-r(x„  ±1,  ±  1,  • •  •  ).
dxr

As  xr  varies  between  —1  and  +1,  keeping  Xi,  Xi,  ■ •  ■ ,  xr-x  fixed,  dGn/dxr
is  of  constant  sign,  that  is,  G„(x;  Xi,  •  ■ ■ ,  xr,  ±1,  ±1,  •  •  •  ,  ±1)  increases
or  decreases  steadily.  Hence  |G„(x;xi,  •  •  •  ,  xr,  ±1,  ±1,  •  •  •  ,  ±1)|  attains
its  maximum  when  xr  is  an  end  point.
If  we  take  r = 1,  2,  •  •  ■ , n,  it  follows  that  | G„(x;  xi,  •  •  • , x„)|  ( — 1 i=xr

246 SHEILA  S.  MACINTYRE [September

¿1)  attains  its  maximum  for  any  given  value  ofx  ( — 1 gx  g  1)  when  xr=  +1
(l=rgw).
So,  in  order  to  find  an  upper  bound  for  | G„(x;  xi,  x2,  •  •  •  ; xn)\  ( — 1 úxr
g  1),  it  is sufficient  to  consider  the  2" polynomials  |G„(x;  ±1,  +1,  •  •  -,  ±1)|
(-lgxgl).
Clearly  if  Ogxgl  and  xr=±l,

(4.1)  |G„(a;;  +1,  Xi,  ■ ■ ■ ,  xn)\  =  |G„(-x;  — 1,  — x2, • • •  ,  — xn)  \

g  |G„(0;  -1,  —x2,  ■ ■ •  ,  —Xn)  |

(4.2)  <, | Gn{x', —1, —Xt, '•'.,—Xn)  I.

I  shall  prove  that  if Ogxgl  and  xr=  ±1  (1 grgw)  for  all  n,

i  i  /4X"-1         ir
(4.3)  |G„(x;  xi,  Xi, ■ ■ ■ , xn) \ g  2Í—  J     sin  — (x +  1).

By  (4.2),  it  is  sufficient  to  prove  (4.3)  for  the  case  Xi=  —1,  that  is,  it  is
sufficient  to  prove

i  /4X"-1        x
(4.4)  \Gn(x',-l,  +1,  xt, •••  , *»)|  á2Í—  J      sin —(x+1)

and
 /4X"-1        x
(4.5)  \Gn(x; -1,  -1,  xt, ■ ■ ■ , as.) |  g  2Í— J     sin — (x +  1).

Proof  of  (4.4).

|Gn+i(x;—1,  +1,  x3, • • • ,  x„+i)  |  =    I     |G„(x';  +1,  x3, • • • ,  x„+i) | dx'

=  Ii  +  h,

where
 \Gn(x';  +1,  x3,  •  •  •  ,  xB+i)|  dx',

Ii  =   I     | G„(x';  +1,  x3, • • • ,  x„+i) | dx'.
J  0

If  we  use  (4.1),
 f°  i  i
-fi  =    I      \Gn(—x';  — 1,  — Xt, ■ ■ ■ ,  — xn+i)  | dx'.

If  we  substitute  x =  —x',

1949]  SUCCESSIVE DERIVATIVES OF  INTEGRAL  FUNCTIONS  247

It  **  I       | Gn(x;  — 1,  — x3,  • •  •  ,  — xn+x) |  dx.
J  0

Now  if we  assume  that  (4.3)  is  true  if  n  is  replaced  by  any  number  m^n,

/4X"-1    r1         *  /4\"
/iá2Í-j        I     sin  —  (x  +  l)á*  =  21'2( — ]  ,

I2  =    i    dx'  I     | G„_i(x";  x3,  ■ • •  ,  xn+1) | dx"
Jo  J   x'

/4\"-2    /•*  r1         ir
=  2Í—J       I    ¿x'  I    sin—(x"+  l)dx"

/4\"        ir  /4\"
-2(7)sinT(,+  l)-2.».(7).

Therefore  7i+72g2(4/7r)"  sin  (ir/4)(x  +  l).
But  (4.4)  is  true  when  n = 0,  1.
Hence  (4.4)  is  true  for  all  n  by  induction.
Proof  of (4.5).

G„+i(x;  — 1,  — 1,  x3, • ■ • ,  xn)  =    I      |G„(x';  — 1,  x3, • • •  ,  x„) | dx'

=  U +  U

where
 f ° i  iF> =   I      | G„(x';  — 1, x3, • • • ,  x„) | dx',

It  ■» I     | G„(x';  — 1,  x3, • • • ,  x„) | dx'.
•/  o

If  we  use  (4.1),
 -7s =    I     |G„(-x';  +1,  — x3, • • • ,  — xn) I dx'.

If  we  substitute  x=  — x',

^3  =    I      | Gn(x;  +1,  — x3, • • •  ,  — x„)  | dx
J  0

=   I       I     |G„_i(x';  — x3, ■ • • ,  — xn) | dx'.
Jo      J   x

Hence,  if  we  assume  (4.3)  is  true  if  n  is  replaced  by  any  number  m^n,

248  SHEILA  S.  MACINTYRE  [September

/4\""2    r1         r1  t
73g2Í—J        I    dx j     sin — (*' +  l)dx'

l — j  (2  -  21'2).
 x
sin  —  (x'  +  l)dx'
4

=  (iy(-2cos^(x+l)  +  2I/2).

Now  1-cos  (7r/4)(x +  l)gsin  (tt/4)(x  +  1),  Ogxgl.  Hence  h+h
g2(4/x)"sin  (tt/4)(x  +  1).
But  (4.5)  is  true  when  n  =  0,  1.  Hence  (4.5)  is  true  for  all  n  by  induction.
Since  (4.4)  and  (4.5)  are  true,  we  have  proved  (4.3).  It  follows  by  sub-
stituting  — x  for  x,  that  for  — lgxgOand  — lgxrgl  (lgrgw),

i  I        /  4 Y"1            T
(4.6)  Gn(x;  Xx, Xi,  ■ ■ ■ ,  xn)  \  g  2 I —  )     cos  —  (x  +  1),
\T/  4
and  we  have  the  following  theorem.

Theorem  II.  If  zr  is  a  sequence  of  points  on  the  real  axis,  satisfying
— 1 g  zr g  1,  then

(4.7)  \Gn(zo;zx,z2,  •••  ,zn)\  Ú  2(4/*-)»«.

5.  I  shall  now  discuss  extensions  of  Theorems  I  and  II  in  which  some  of
the  points  of  the  sequence  zT lie  outside  the  unit  circle,  and  the  segment
— 1 gx  g  1  respectively.
Let  zr=xr+yr,  where  both  xr  and  yr  may  be  complex,  then  since
G„(zo;  Zi,  ■ •  •  ,  zn)  is  a  polynomial  in  each  zr(0grg«),  we  may  apply  Taylor's
series  and  write

(5.1)        Gn(z0;  zi,  •  • •  ,  Zn)  =  exp  (  ¿J  Jr-)G„(x0;  xt,  •  • •  ,  xn)(Íyr-P¡Gn(

Now,  writing  G„(xo;  Xi,  x2,  ■ ■ ■ ,  xn)  =G„,  using  (2.2)  and  (2.3),  we  note  that
dGn/dxT  (Ogrgw)  is  either  one  multiple  integral  or  the  product  of
two  such  integrals,  in  each  case  the  total  multiplicity  being  n — 1.  Similarly
dhGn/dxrdx„  •  ■ ■ dx,,  where  r,  s,  ■ ■ ■ ,  t  may  all  take  any  values  between  0
and  n  inclusive,  is  either  zero  (for  example,  d2Gn/dxodxx)  or  the  product  of  not
more  than  ¿ +  1  multiple  integrals,  the  total  multiplicity  being  n  — k.
Now  suppose  that  positive  constants  A,  y  can  be  found  such  that

(5.2)  |G„|  <^t"+1

provided  that  the  sequence  {xr}  belongs  to  a  given  set  of  points  S  which  in-

1949]  SUCCESSIVE  DERIVATIVES  OF  INTEGRAL  FUNCTIONS  249

eludes  z =  0.  Such  a  set  exists  by  Theorem  I.
Setting  n=0,  we  see  that^4T>l.  Hence

¿>*G„ <  Ak+1yn+1.
dxrdxa  ■ •  ■ dxt

Suppose  also  that  the  values  of  yr  are  restricted  in  such  a  way  that

n
(5.3)  22\jr\=nh
r=l

for  certain  values  of  n.  Then  (5.1)  gives,  for  these  values  of  n,

i                                     ,      A    (|  yo|  +  nh)k
Gn(z0; zi,  Zi,---,Zn)\<J2  ^^^--4*+V+1
(5.4)  ,b=o  ¿!
=  Ayn+1 exp  [A(  I y01 +  nh)\.

If  the  sequence    \zr\  is  such  that  all  its  limit  points  belong  to  S,  then
(5.3)  is  satisfied  for  arbitrarily  small  h and  sufficiently  large  n,  and  (5.4)  gives

(5.5)  |G„(z0;zi,  •••  ,zn)|  <^^i«oI(t  +  0"+1,  *  £  »o(e),

and  hence  for  all  z  in  any  given  finite  domain,  and  all  n,

~(5.6)  | Gn(z;  zt,  Zi,  ■ ■ ■ ,  zn)  \  <  A'(y  +  «)•«.

6.  Suppose  now  that/(z)  =  22n=o  anZn is  an  integral  function  satisfying

log  M(r)  1
lim  sup-=  a  <  —  >
r-.«  r  y

it  follows  that  for  any  r>a,  and  sufficiently  large  n

(6.1)  n\\an\    <t".

Then,  iif(zx)  =0,/<"-1'(zn)  =0,  clearly

m  = rdz'rdz"---  f  f^\z)dz,
J  zx  J  z2  J  »„

or,  following  Levinson  [3,  §1 ],  if  we  replace/"(z)  by  its  power  series,  we  obtain

/O0  =  Z  (» +   *)! -—-   I      *<   I        ^2" • • •  2*dz
ft-0  ¿  !       J  Zl  J   Zj  •/   2„

CO
=  Z)  (w +  ¿)!an+*Gn+i(z;  zi,  z2, • • •  , zn, 0,  0,  • • •  ,  0).

Now  since  the  sequence  {zn}  is  such  that  all  its  limit  points  belong  to  S,  then
for  large  n  and  for  all  z in  any  finite  domain  we  have  by  (5.6)  and  (6.1)

250 SHEILA  S.  MACINTYRE [September

»  A'(y  +  e)"+1r"
(6.2)  | /(z)  |  <  22 T»+kA'(y +  0"+*+1 =  —-
*=o  1  —  r(y  +  e)

provided  r<l/(7+e).  But  letting  n—*<»  in  (6.2)  we  have/(z)=0.
In  the  particular  case  in  which  S  is  the  unit  circle,  Theorem  I  shows  that
(5.2)  is satisfied  with  y =  1.3775 <1/.7259  for  all  values  of  n,  so  we  now  have
the  following  theorem.

Theorem  III.  Iff(z)  is  an  integral  function  satisfying

log  M(r)
lim sup —-—-<  .7259,
r-»oo  r

and  if f(zx)  =0,/(n_1)(z„)  =0  (wS:2),  the  sequence  {zT} having  all  its  limit  points
in  the  unit  circle,  then  f(z)  =0.

In  the  particular  case  in  which  S  is  the  segment  Ogxgl,  Theorem  II
shows  that  (5.2)  is  satisfied  for  all  n  with  y=4/ir  and  we  have  the  following
extension  of  Schoenberg's  theorem.

Theorem  IV.  If  f(z)  is  an  integral  function  satisfying

log  M(r)        t
lim sup ——-  <  — )
r->«  r  4

and  iff(zx)  =0,/tn_1)(zn)  =0  (n^2),  the  sequence  [zr]  having  all  its  limit  points
on  the  segment  — 1 gx  g  1  of  the  real  axis,  then  f(z)  =0.

This  result  has  been  stated  by  Kamenetsky  [2,  Theorem  VIII]  but  I  have
been  unable  to  find  a  published  proof.  It  seems  unlikely  from  the  context  that
his  method  has  anything  in  common  with  the  one  which  I  have  used  here.
7.  A  further  theorem  follows  as  a  consequence  of  inequalities  (5.2)  and
(5.6)  for  the  case  in  which  the  limit  points  of  the  sequence  of  zeros  lie  inside
the  locus  of  points  distant  h  from  the  segment  — lgxgl  of  the  real  axis.
We  shall  call  the  domain  enclosed  by  this  curve  H.  In  this  case,  if  we  restrict
the  sequence  {xr}  to  the  segment  —lgxgl  (all  r)  and  zr=xr+yr  (all  r^l)
where  |yr|  g&  (r^l),  (5.2)  is  satisfied  with  A = x2/8,  t=4/x,  by  Theorem  II,
and  (5.3)  is  satisfied  for  all  n  since  |yr|  g/j(rèl).  Hence  (5.4)  is  satisfied
for  all  n  with  these  values  of  the  constants,  that  is,

X2/4W+1  (x2       .  .  \  _
|G„(z0;zi,  zt,  - • •  ,  z„)|  g  -t\        )       exp  Y7,  (\  y°\  +  nhH  <  A7n+1>

with  f  =  (4/x)  exp  (ir2h/8).  By  a  second  application  of  formulae  (5.2)  and
(5.6),  we  see  that,  provided  all  the  limit  points  of  the  sequence  {zr}  lie  within
H,  (5.6)  holds  with  y=(4/ir)  exp  (ir2h/8),  and  we  have  the  following
theorem.

1949]  SUCCESSIVE  DERIVATIVES  OF  INTEGRAL  FUNCTIONS  251

Theorem  V.  If  f(z)  is  an  integral  function  satisfying

log  M(r)        t  /      ir2h\
lim  sup-<  —  exp  (-■  ),
r^«  r  4  \        8/

and  if  f(zx)  =0,  f(n~1)(zn)  =0  (w^2),  where  the  sequence  {zr}  has  all  its  limit
points  in  H,  then f(z)  =0.

It  is  to  be  noted  that  the  constant  (x/4)  exp  (— ir2h/8)  is  "better"  (that
is,  greater)  than  that  obtained  from  the  circle  circumscribed  to  H,  namely,
.7259/1  +h  (which  is  obtained  from  Theorem  III  by  the  transformation
f  =  (l+h)z)  only  for  small  values  of  h.  It  is  "better"  when  h g0.23  but  not
when  A =0.24.
 Appendix

Upper  bounds for
n                Mn-i                    Ln  Ln/(1.3775)n   (1.3775)"
1  1                    1  0.7260  1.3775
2  2                    1.5  0.7905  1.8975
3  2.5981            1.9299  0.7384  2.6138
4  3.6379            2.7915  0.7753  3.6005
5  4.8414            3.8056  0.7673  4.9597
6  6.8223            5.2539  0.7690  6.8320
7  9.3973            7.2315  0.7685  9.4111
8  12.9512            9.9635  0.7686      12.9638
9  17.8413          13.7212  0.7684      17.8577
10  24.5754          18.8998  0.7683      24.5989
11  33.8472  33.8850

References

1.  I.  M.  Kamenetsky,  Sur  l'interpolation  au  moyen  des  dérivées  et sur  les  procédés  d'interpola-
tion correspondants I,  C. R. Acad. Sei. URSS vol. 25 (1939) pp. 356-358.
2.  -,  Sur  l'interpolation  au  moyen  des  dérivées  et  sur  les  procédés  d'interpolation  cor-
respondants II,  C. R. Acad. Sei. URSS vol. 26 (1940) pp. 217-219.
3.  N.  Levinson,  The Gonteharoff polynomials,  Duke  Math.  J.  vol.  11  (1944) pp.  729-733.
4.  -,  Correction to "The Gontcharoff polynomials,"  Duke  Math.  J. vol.  12 (1944) p. 335.
5.  Sheila  Scott  Macintyre,  An  upper  bound  for  the  Whittaker  constant,  J.  London  Math.
Soc. vol. 22 (1947) pp. 305-311.
6.  I.  J.  Schoenberg,  On  the  zeros  of  successive  derivatives  of  integral  functions,  Trans.  Amer.
Math. Soc. vol. 40 (1936) pp.  12-23.
7.  J.  M.  Whittaker,  Interpolatory  function  theory, Cambridge,  1935.

The  University,
Aberdeen,  Scotland
