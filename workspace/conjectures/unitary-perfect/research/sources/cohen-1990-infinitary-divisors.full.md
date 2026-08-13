<!-- source: https://www.ams.org/journals/mcom/1990-54-189/S0025-5718-1990-0993927-5/S0025-5718-1990-0993927-5.pdf | converted from PDF -->

mathematics  of  computation
volume  54, number  189
january  1990, pages  395-411

ON AN INTEGER'S INFINITARY DIVISORS

GRAEME L. COHEN

Abstract.  The  notions  of  unitary  divisor  and  biunitary  divisor  are  extended
in  a  natural  fashion  to  give  k-ary  divisors,  for  any  natural  number  k  .  We
show  that  we  may  sensibly  allow  k  to  increase  indefinitely,  and  this  leads  to
infinitary  divisors.  The  infinitary  divisors  of  an  integer  are  described  in  full,
and  applications  to  the  obvious  analogues  of  the  classical  perfect  and  amicable
numbers  and  aliquot  sequences  are  given.

1. Introduction

A divisor  d  of  a natural  number  n  is unitary  if the  greatest  common  divisor
of  d  and  n/d  is  1, and  is biunitary  if  the  greatest  common  unitary  divisor  of
d  and  n/d  is  1.  Unitary  and  biunitary  divisors  have  been  studied  by  several
authors,  often  in  terms  analogous  to  those  of  the  classical  perfect  and  amicable
numbers.  Among  these  writers  are  E. Cohen  [2], Hagis  [4-6],  Lai  [7], Subbarao
and  Warren  [9], Suryanarayana  [11] (see also  [12]) and  Wall  [15,  16].
It  is  easily  seen  that,  for  a  prime  power  py,  the  unitary  divisors  are  1 and
py , and  the  biunitary  divisors  are  all  the  powers  1,  p  ,  p  ,  ...  , py,  except  for
py    when  y  is even.
There  is  no  difficulty  in  extending  this  notion.  Thus  we  may  call  d  a  tri-
unitary  divisor  of  n  if  the  greatest  common  biunitary  divisor  of  d  and  n/d
is  1.  We  soon  calculate  that  the  triunitary  divisors  of  py  are  1 and  py , except
if  y  =  3  or  6;  those  of  p  axe  1,  p,  p  , and  p  ; and  those  of  p  axe  1,  p  ,
p  and  p  .  In  this  way,  we  may  also  define  4-ary  divisors,  5-ary  divisors,  and
so  on.  We  shall  speak  in  general  of  k-axy  divisors.  The  lack  of  a  pattern  in  the
list  of  k-axy  divisors  of  p}  (for  small  values  of  k,  not  1 or  2,  and  y  ) would
have  inhibited  a  study  of  these.  But  as  we  increase  k,  in  fact  a  very  striking
pattern  begins  to  appear.
Figure  1 shows  the  k-axy  divisors  of  p>  for  k  =  1,  2,  ...,  6,  and  0 <  y  <
30.  The  asterisks  indicate  those  values  of  x  for  which  px  is a  k-axy  divisor
of  py .  Figure  2  is the  same  for  k  =  19  and  20,  and  0 <  y  <  80.  We notice
that  for  small  values  of  y,  to  be  characterized  later,  the  k-axy divisors  remain
fixed.  The  pattern  for  large  y  is also  fixed, and  depends  on whether  k  is odd  or
even.  Finally,  in  Figure  3, we show  the  100-ary divisors  of  py  for  0 <  y  <  120.

Received October  31,  1988.
1980 Mathematics  Subject Classification ( 1985 Revision). Primary  11A25.

©1990  American  Mathematical  Society
0025-5718/90 $1.00+  $.25  per page

395

396 G. L. COHEN
 W
ai
D
Ü
il

■s   t

ON AN INTEGER'S INFINITARY DIVISORS 397

is    s
IS    3
if I
 W

O

:s     s
Il    î

ICI    ICI      4i I   C    J    4    6
¡01       4i

c:  a
IÎ1234S67
d12  4  c
 t  I     34

6   I   01?

01      4b      I» 4S     »S     23     67

IS   ¡01     4S
 !>i 7i$C'.234iifc7îSJ Í34  ■(.   653123

¿1     31     4*     19     23     67     01     4S     (9      23
6tC24fc(0246l0246

45    101     45      19      23 23     67     01      45

!ûl?34S6~t9
C   2   4    £   I
ICI      4 S      19
 7t»o:234!  t"S9C;
10    2   4   6   10

Cl      45     19
 iDDiiniiiiiiiiiiii
131]  ]Hmï?222î22îî3J3333333244i44444445SiibiSii  16666666666777717777788  tfî((Î8i999S9S93S9!)C0000000011111U1112
<01234it7E9C:234S67tî.C12.,'45678!.01234567%5:ii;'4!6n8  90]234S£",ï93;234i67t901234i67l9!J1234V67g901234SÉ"ï?01234b67l901234S67890

100-ary divisors

Figure  3

ON AN INTEGER'S INFINITARY DIVISORS 399

The  pattern  of  divisors  for  the  small  values  of  y  would  now  appear  to  be
established,  whatever  the  value  of  k,  and  it  is  these  which  we  shall  be  calling
infinitary  divisors.  Note  that  the  figure  shows  some  collapse  in  the  pattern  for
y  >  100.  The  last  (decimal)  digit  of  x,  where  px  is  a  100-ary  divisor  of  py,
is shown  in  this  figure,  so that  the  actual  divisors  may  be  read  off; this  will be
useful later.
The  pattern  indicated  by Figure  3 has the  distinct  appearance  of a fractal.  It
may  be  compared  with  Sierpiñski's  "arrowhead"  or  "gasket"  (Mandelbrot  [8]).
See also  Sved  [13],  where  the  same  fractal  appears,  also  in  a  number-theoretic
setting.
The  pictures  would  appear  to  be  worth  a  thousand  words.  The  first  aim  of
this  paper  is  to  describe  this  unexpected  pattern  in  terms  of  our  definition  of
k-axy divisors.
 2.  Infinitary  divisors  of  prime  powers

In  the  following,  all  letters  denote  nonnegative  integers,  with  p  reserved  for
an  arbitrary  prime.  To  put  the  above  on  a  formal  footing,  we begin  with

Definition  1.  A divisor  d  of  an  integer  n  is called  a  1-ary divisor  of  n  if  the
greatest  common  divisor  of  d  and  n/d  is  1; and  d  is  called  a  k-axy divisor
of  n  (for  k  >  2 )  if  the  greatest  common  (k  -  l)-ary  divisor  of  d  and  n/d
is  1.

For  convenience,  we  shall  call  d  a  0-ary  divisor  of  n  if  d\n.  We  write
d\kn  to  indicate  that  d  is  a  k-axy divisor  of  n , and  (/,  m)k  for  the  greatest
common  k-axy  divisor  of  /  and  m .  It  has  become  common  to  write  d\\n  in
place of  d\xn.
It  should  be  mentioned  that  different  generalizations  of  unitary  divisor  have
been  given  by  Suryanarayana  [10] (who  also  used  the  term  "/c-ary divisor")  and
Alladi [1].
The  following  observations  are  immediate  and  will  be  used  later  without
special reference.

(i)  For  any  n ,   \\kn  .
(ii)  px\kpy  means  (px  ,py~x)k_x  =  1 .

(iii)  px\kpy  if  and  only  if  py~x\kpy  .

The  permanency  of  the  pattern  for  the  early  k-axy  divisors  of  py , described
in  § 1, is  accounted  for  in

Theorem 1.  For  k  > y -  1 >  0,  px\kpy  if and  only if px\    xpy .

Proof.  The  proof  is  by  induction.  The  result  is  true  when  y  =  1,  since  1 \kp
for  all  k .  We suppose  now  that  it  is true  for  y  <  Y -  1,  and  consider  y  =  Y.
For  k  =  Y — 1,  there  is nothing  to  prove,  so we suppose  also that  the  result  is
true  for  Y -  1 < k  < K -  1,  and consider  k  = K.
x  Y  x  Y
Suppose  p  \Kp  .  We  must  show  that  p  \Y-\P  ■ *f m's  ls  not  true> tnen

1 <  x  <  Y -  1  and  (px , p  ~X)Y_2 -  pa  ,  a  >  1 .  Since  pa\Y_2px  , the  induc-

tion  hypotheses  show  first  that  p"\x_xpx  ,  and  then  that  pa\K_xpx  .  Similarly,

400  G. L. COHEN

p"\y-2P  _l    and  Y  — x  <  Y  -  1,  so  pa\Y_x_xp  ~x ,  and  then  pa\K_xp

Hence  (px,  p  ~X)K_{ >  p"  >  1,  contradicting  px\Kp    .  Hence,  px\Y_xpY ,  as
required. x  ¡  Y  x  Y
Suppose  next  that  p'  \Y_{P  ■ We  must  show  that  p  \Kp  .  If  this  is  not

true,  then  x  <  Y  -  1  and  (px,  pY~x)K_x  =  pb,  b  >  1.  Then  p  \K_xpx,

and  the  induction  hypotheses  give  p  \x_xpx  and  then  p  \Y_2px ■  Similarly,

p  \Y_2P  ~x , and  we  are  contradicting  px\Y_xpY  .  The  proof  is  complete,      o

We are justified  now  in  making  the  following

Definition  2.  We  call  px  an  infinitary  divisor  of  py   (y  >  0)  if  px\v_xpy  .  We
also  define  1 to  be  an  infinitary  divisor  of  1.

We  write  px\00py  when  px  is  an  infinitary  divisor  of  py  (and  px  \  00py
when  it  is not),  and  (p1, p1)^  for  the  greatest  common  infinitary  divisor  of  p'
and  pJ  .

Theorem  2.    We have  px\00Py  if and  only  if  (px , py~x)00  -  1 ■

Proof.  This  is  trivially  true  if  y  =  0  or  1, and  generally  if  x  =  0  or  x  — y,
so  assume  now  that  y  >  2  and  that  1 <  x  <  y  — 1.  Then  x  — 1 <  y  -  2  and
y  -  x  -  i  <  y  -  2.  If  px  t  „y  ,  then  px  \  y_ xpy ,  so  (px  , Py~x)y_2  =  pa  >  \.

Then  pa\v_2px,  so  that,  by  Theorem  1,  p"\x_xpx  ;  similarly,  pa\v_x_xpy~x  .

But  then  p"\00px  and  pa\00py~x  ,  so  (p'v,  py~x)00  >  p"  >  1 •  For  the  converse,

we  assume  that  (px,  py~x)ao  =  P     >  1   and  essentially  reverse  the  preceding
argument.      D

The  theorems  and  corollaries  which  follow  will  lead  to  the  complete  charac-
terization  of  the  infinitary  divisors  of  py .  The  pattern  of  Figure  3  (excluding
the  top  nineteen  lines)  will thus  be fully  described,  although  the  characterization
we  end  with,  in  Theorem  8,  will  lead  to  a  more  efficient  means  of  constructing
tables  of  infinitary  divisors.

Theorem  3.  We have  p\oopy  if and  only  if  y  is  odd.

Proof.  Using  Definition  2,  we  have  pl^p1  and  p \  ^p".  Also,  using  Theorem
2, we have,  for  y  >  3 ,

P\ooPy    ^    (/>>/"')oo=   1    ^    P^ocPy~[

The  result follows.   D

Theorem  4.  If  y  is even and  px\00py ,  then  x  is even.

Proof.  Suppose  x    is  odd.    Then  y  -  x    is  also  odd  and,  using  Theorem  3,
(px  , py~x)oc  >  P  ■ This  contradicts  the  statement  that  px\QOpy ■     □

Theorem  5.   We have  px\oopy  if and  only  if  p2x\00p2y ■

ON AN INTEGER'S INFINITARY DIVISORS 40!

Proof.  We  use  induction  on  y.  The  result  is trivially  true  if  y  =  0.  Suppose
the  theorem  is  true  for  y  <  Y -  1,  and  consider  y  =  Y.  Clearly,  we  may
assume  1 < x  <  Y — 1.
x  Y  Ix  1Y  2y       2Y—2x
Suppose  p  \oop    , but  p     \  m/j        .  The  latter  implies  that  (p  '  , p  )00 =
pa,  say,  and,  using  Theorem  4,  a  is  even  and  positive.  Put  a  =  2b.  Since
p  l^p  x  and  p  l^p  Y~ "x,  the  induction  hypothesis  implies  that  p  \oopx  and

P  \<xP  ~X ■   Then  (px,  p  ~x)00  >  p     >  1,  contradicting  the  assumption  that
x,        Yp Lp  ■
Suppose  next  that  px  \  ^p    .   Then  (px,  p     x)00  =  pc  >  1,  from  which,

by  hypothesis,  p  c\OQp x  and  p  c\oop  "v.  It  follows  that  p  x \  ^p  .  This
completes  the  proof  for  y  =  Y,  and  thus  for  all  y.     D

Theorem  6.  If  px\aopy  and  y  is  divisible  by  2J  for  some  j  >  0,  then  x  is
divisible by  2J.

Proof.  The  result  is  trivial  when  7  =  0.  Suppose  it  is  true  when  j  -  J,  and
consider  j  =  J  +  1.  Put  y  =  2  +  a .  By Theorem  4,  x  is even,  say  x  =  2w .

Then  p  "l^P  " , so that,  by  Theorem  5,  pw\00P  a •  Then,  by  the  induction
hypothesis,  w  is divisible  by  2   , and  the  result  follows.     D

~*a  ~.a
Corollary  1.  The  infinitary  divisors  of  p        are  1 and  p      .

Proof.  This  is immediate.    D

Corollary  2.  For  0 <  k  <  2J,  P^^p2'^  \for  2J <  k  <  2j+l,  p2'  \00p2'+k  .

Proof.  The  first  statement  follows  from  Corollary    1   since,    for  these    k,
2'       k
(P    '  P  )oo =  1 ■ T°e  second  statement  follows  from  the  first.      G

's)  ...
Theorem 7.  We have  p   \oopy if and  only if  y  =  2J  or  2J +  1  or  2'  + 2  or  ■ ■ ■
or  2J+]  -  1 (mod  2J+I).
Proof.  We have

P2  \ooPy  *=>  (P2  '  P'~2  )oo =  l    ^^  P2  ^oc,Py~        (  by  Corollary  1)

<=>  (P2' ,P~      )oo >  J   ^^  P2  \ooP'~  (by  Corollary  1)

2J,         y-2J+'l^^  ■ • • *=> p  Lp

where  /  is  chosen  to  be  the  largest  integer  such  that  y  -  2J+ll  >  2J.  Then
2J < y  -  2J+[l  <  2'  +  2J+l , and  the  result  follows  from  Corollary  2.    D

The  remainder  of  the  identification  process  for  infinitary  divisors  is carried
out  mainly  in terms  of the  binary  representations  of the  exponents  on the  prime
p.  We write  a  binary  representation  in  general  fashion  as  \^q2}  ; the  sum  is
finite,  j  >  0,  each  q.  is  0  or  1, and  trailing  zeros  are  allowed  where  required.
A little  reflection  gives  us  the  following  alternative  statement  of  Theorem  7.

402 G. L. COHEN

Theorem 7   .  Let  y = JZy 2.  Then p   \n'  if and only ify¡  =  1.
J  OO  J

Theorem 8.  Let  x  =  ^2x-2J  and  y -  x  =  ¿~2 z.2J.  Then

PX\ooPy    ifand  on[y V    Sxjzj  = °-

Proof.  Suppose  first  that  ¿~^x¡z¡  /  0.    Then  x    =  z   =  1   for  some  j,  so

P2  \ooPX  and  P2  \ooPy~X > by  Theorem  7 '  •  Hence  (px,  py~x)00  >  p2    >  p  ,  so

*  L            y

For  the  converse,  suppose  px \  00py,  so  that  (px , py  x)0O =  pa  ,  say,  with
a >  1.  Put
 a = Y^aj21,    x-a  = Y^bj2J,     y -x  -  a = \S^c¡l1.

Since  a  >  1,  we  have  a,  =  1  for  some  i.  Since  pa\„px  , we have  Y,a,b,  =  0
(using  the  part  of  this  theorem  already  proved)  and  it  follows  that  b¡  =  0
and  that  x¡  -  a.  +  b.  for  each  j.  Hence  xi  =  1 .  Similarly,  pa\00py~x,  so
J2ajc,  -  0 > from which  c( = 0  and  z¡ = ai + ci■ =  1 . Thus  J2xjzj  ¥" 0 •   □

Corollary  3.  The  infinitary  divisors  of  p   ~     are  all  px  ,  0  <  x  <  2a -  1.

Proof.  Taking  y  =  2a -  1  in  Theorem  8, we see there  that  if  x.  =  0  or  1, then
z  =1  or 0, respectively, and  J2XjZ.  =  0.    D

In  the  next  theorem,  we  prove  a  very  pleasing  and  useful  property,  namely,
that  infinitary  divisors  are  transitive.  This  is  not  true  of  k-axy  divisors  in
general.  For  example,  p\5p    and  p  |5p7,but  p\ip1'.

Theorem  9.  If  px\00py  and  py\00p:,  then  px\00pz  ■

Proof.  The  result  is  trivial  if  x  =  0,  so  suppose  x  >  1.  Write  x  =  J2xj2J,
y  =  ¿Zyj2J,  y  -x  =  J2rj2J,  z -  y  =  ¿Z s^1,  and  z -  x  =  £  tj2J.  We must
show  that  J2x,tj  =  0,  given  that  Y^x.r  =  0  and  J2y/.  =  0.  Consider  any
particular  value  of  j,  say  j  =  k,  for  which  xk  =  1 .  Since  J2xjr,  =  0,  we
then  have  rk =  0  and  y ■ =  x¡  +  r  for  each  j,  so  yk =  1.  Then  sk =  0.  We
note  that  z -  x  =  (z -  y) +  (y -  x).  If  k  =  0,  then  ?0 =  50 + rQ =  0.  If  k  >  0,
then  ^  =  ^  +  rfc unless  s¿ =  r¡. =  1  for  some  i  <  k.  In  that  case,  y;  =  0,
since  î^y.5,  =  0 > and  we cannot  have  y.  =  x¡ + r¡.  Hence  tk =  sk + rk =  0,  so
XT  =  0  for  all  j,  and  the  proof  is finished.     D

Theorem  10.  Suppose    2a   <  y    <    2a+l  .    If  px\00Py~2",    then  px\00py   and

P2"+XLPy ;   ifx<y-2aand  p^/  ,  then  px\00P>"2''.

Proof.  Assume  px\CX)Py~     ■   Since  2"  <  y  <  2a+i ,  Theorem  l'  implies  that

p2  \00py ,  so  py~2  \00py ,  and  so  px\00py  ,  by  Theorem  9.
Now  put  x  =  ¿Zx^  and  y  -  2a  -  x  =  £  z,-2J.  We  have  x  <  y  -  2a  <

2fl+1 -  2a  =  2a   and  2fl  <  2a  +  x  <  2a+1 ,  so  2a  +  x  has  the  proper  binary

ON AN INTEGER'S INFINITARY DIVISORS  403

representation  2" +  2~Z-*,2;. By Theorem  8,  ¿~lxjzj  =  0> and  so, by  the  same

theorem,  p2 ^l^'.

For  the  second  part,  suppose  p  \  oopy~  ,  and  let  x  and  y  -  2a  -  x  be  as
before.  Then  x    =  z    =  0  for  j  >  a  and  xk  =  zk  =  \  for  some  /c <  a  (by

Theorem  8).  But  then  y  -  x  =  2a + J2 z¡2}  and  the  right-hand  side  is a proper

binary  representation;  since  xk  =  zk  =  1,  we  have  px  \  oopy , as  required.      D

Theorem  11.  //  2a <  y  <  2a+1  and  y  -  2a <  x  <  2a,  then  px \ ^  .

Proof.  Since  y -  2a  <  x  <  2a , we also  have  y-2a<y-x<2a.  Then,  putting
x  =  J2X:2J  and  y -  x  =  J2 zj2> > we mav  assume  in  each  sum  that  j  <  a — 1.

Put  also  y  =  y]y,2"'.  If  x,z.  =  0  for  all  /,  then  y,  = x,  +  z¡  for all  /,  and

it  is  impossible  to  have  ya -  1,, which  we  require  since  2a <  y  <  2a+  .  Hence
x  =  zj  =  1  for  some  j  , implying,  by  Theorem  8,  that  px  \  oopy .     D

Theorems  10 and  11 imply  the  "arrowhead"  of  Figure  3.  In  particular,  The-
orem  11 accounts  for  the  large  empty  triangles.
We can  use  Theorem  10 to  find  the  infinitary  divisors  of  prime  powers  very
quickly  (that  is, in polynomial  time).  For example,  the infinitary  divisors  of  p
axe the  infinitary  divisors  px  of  p  , i.e.,  p      , and  each  p    +x .  Use  Fig-
ure  3 for  the  infinitary  divisors  of  p     or  calculate  them  from  those  of  p
i.e.,  p  .  The  infinitary  divisors  of  p     are  px  for  x  =  0,  2,  4,  6 ; so  those  of
22  I SO
p     have  x  =  0,  2,  4,  6,  16,  18, 20,  22.  Then the infinitary divisors of  p
are  px  for  x  =  0,  2,  4,  6,  16,  18, 20, 22,  128, 130, 132, 134, 144, 146,
148, 150.
The  simplest  means  of  constructing  the  Sierpiñski  arrowhead  is by  means  of
Pascal's  triangle,  where  only the parity  of the binomial  coefficients need  be noted
(Sved  [13]).  This  gives  immediately  the  following  unexpected  characterization
of  infinitary  divisors.

Theorem  12.  We have  px\00Py  if and  only  if  (yx) is odd.

3.  Infinitary  divisors  of  integers

The  simplest  and  quickest  way  to  introduce  infinitary  divisors  in  general  is
as follows.

Definition  3.  Let  d  be  a  divisor  of  n  and  write  n  =  Y['j=xp/  ,  for  distinct

primes  p{ , p2,  ...  , pt,  and    d  =  n'j=xPjJ   (where  0  <  Xj  <  y¿,    j  =  I,

2,  ...  ,t).    Then  d    is  an  infinitary  divisor  of  n   if  p/l^p/    for  each  j  =
1,2,...,?.

We write  dl^n  if  d  is an  infinitary  divisor  of  n .
A  more  fundamental  approach,  parallel  to  what  has  been  done  for  prime
powers,  would  be to  write,  say,
 h(n)  =  maxy,
/II«

404 G. L. COHEN

and  to  define  d  to  be  an  infinitary  divisor  of  n  if  d\h,n)_xn  .  It  could  then  be
shown  that  d\kn  for  any  k  >  h(n)  -  1  and  after  some  work  we  would  obtain
the  result  assumed  by  Definition  3.  Conversely,  the  results  just  alluded  to  can
be  shown  to  be  a  consequence  of  our  definition.

4.  Functions  of  infinitary  divisors

We  denote  the  number  of  infinitary  divisors  of  n  by  t  («)  and  their  sum
by  <r  (/i).  Essentially  the  same  discussion  as  that  for  the  example  following
Theorem  11 gives  us

Theorem  13.  Let  y  =  ^£ly¡21.  Then

too(/)  = 2^,         ajp")  =  U  (l  +/)  .
y.= \   V  /

Proof.  Suppose  2a < y  <  2a+  .  Then,  by Theorem  10,

U/)  =  2t0O(/_2°),          <U/)  =  <U/~2")  +Pro00(py~2a).

v—2"
Applying  the  same  argument  to  the  infinitary  divisors  of  p  ,  and  repeating
it  as  often  as  necessary,  gives the  theorem.      D

This  theorem  in  fact  gives  a direct  means  of  finding  the  infinitary  divisors  of
py .  For example,  since  150=  128+  16 + 4 + 2,  we have

/    150\        it     ,      2\/i     ,      4wi     ,       16w,     ,       128,
°oo(P       ) =  (l+P   )(1+P   )(1+P      )(i+P        )•

The  terms  in  the  sum,  after  the  product  on  the  right  is  multiplied  out,  are  the
infinitary  divisors  of  p
The  functions  t^  and  a^  axe easily  seen  to  be  multiplicative,  so general  ex-
pressions  for  t^n)  and  o^n)  may  be written  down  with  the  aid  of  Theorem
13.
 5.  Infinitary  perfect  and  multiperfect  numbers

We define  an  integer  n  to  be  infinitary  perfect  if  o^n)  — 2«  and  infinitary
multiperfect  if  u^ffl)  =  sn  for  some  s  >  2 .
It is apparent  from  Theorem  13 that  for values of  n  which are not,  to take the
extreme  case,  products  of  powers  of  primes  of  the  form  p  , there  is generally
a rich  algebraic  factorization  of  o^n),  so that  more  freedom  is to  be  expected
in  searching  for  infinitary  perfect  numbers  than  is  the  case  for  k-axy  perfect
numbers  for  particular  (small)  k .  (We say  n  is  k-axy perfect  if  the  sum  of  all
k-axy  divisors  of  «  is  2n  .)  The  only  biunitary  perfect  numbers  are  6,  60,  and
90  (Wall  [15])  and  only  five unitary  perfect  numbers  are  known  (Wall  [16]).

ON AN INTEGER'S INFINITARY DIVISORS  405

Without  too  intensive  a search,  we have  found  the  following  infinitary  perfect
numbers:
 2-3,  2634537213- 17-41,

2-325,  28335- 11 -43-257,

223-5,  21032527-11-13-43-257,

24335 -17,  21034537211 • 13 • 41 • 43 • 257,

25347 • 17 • 41,  212357 • 11 • 17 • 41 • 43 • 257,

2632527- 13-17,  212365 -7-11  • 17 • 41 • 43 • 257,

26345-7-  17-41,  2I236537211 -13-17-41  -43-257.

Assuming  the  validity  of the pomments  following  the  statement  of  Definition
3,  it  will be  observed,  for  example,  that  the  last  of  the  above  numbers  is  k-axy
perfect for all  k  >  11 .
The  next  thirteen  numbers  satisfy  o^n)  =  7>n :

233-5,  21134537211 • 13-41  • 43 • 257,

25335- 17,  213357- 11- 17-41  -43-257,

2732527- 13-17,  213365-7-ll  • 17 ■ 41 • 43 • 257,

27345-7-  17-41,  21336537211- 13 • 17 • 41 • 43 • 257,

2734537213- 17-41,  214355-7-ll  • 17 • 41 -43  • 257,

29335- 11-43-257,  21435537211 -13-  17-41-43-257.

2U32527- 11 • 13-43-257,

The  next  seven  numbers  satisfy  a^n)  -  4n :

2733527- 13-17,  2n355372ll  • 13 • 41 • 43 • 257,

27355-7-  17-41,  213375-7-  11 • 17 • 41 • 43 • 257,

2735537213-17-41,  21337537211 -13-17-41  -43-257.

2U33527-  11 • 13-43-257,

The  next  two  numbers  satisfy  o^n)  -  5« :

215375-7-  11 -17-41  -43-257,      21537537211 • 13 • 17 • 41 • 43 • 257.

There  is no prize  for  finding further  examples  of  infinitary  multiperfect  num-
bers.  The  above  examples  are  all even:  a simple  adjustment  of the  proof  of The-
orem  1 in Hagis  [6] shows that  there  are  no odd  infinitary  multiperfect  numbers.
We conjecture  further  that  there  are  no  infinitary  multiperfect  numbers  not  di-
visible by 3.
It  is not  difficult  to  devise  methods  of  generating  new  infinitary  multiperfect
numbers  from  known  ones.  The  following  are  two  results  in  this  direction.

406 G.  L. COHEN

Theorem  14.  Suppose  o^n)  =  qn,  where  q  is prime,  and  that  q2a\\n, for  some
a.  Then  o^qn)  =  (q +  l)qn  .

Proof.  Using  Theorem  13 and  the  multiplicativity  of  a    , we have

(7oo(^") =  CToo (<?2a+1 • 4r)  =  (« +  ^oo^Voo  (4t

=  («  +  l)ff00(ii)  =  (9  +  l)tjn,

as  required.      D

For  example,  given  that  n  =  2  3  5  7-13-17  is infinitary  perfect  (it  appears
in  the  first list  above),  we immediately  expect  to  find  2«  in  the  second  list  and
6«  in  the  third  list,  as is the  case.

Theorem  15.  Suppose  o^n)  =  sn,  and  that  I  and  m  satisfy

/aoo(m)  =  mrj0O(/),        l\\n,        (m,n/l)  =  l.

Then  a^mn/l)  =  s(mn/l).

Proof.  We have

imn\  .    ,      tn\      o    (m)      .  .     m      .  .       mn

OO ^    '

Numbers  /  and  m  to  satisfy  the  conditions  of this  theorem  may be obtained
as  follows.  Suppose  o^u)  =  tu  and  o^v)  =  tv  for  some  t,  and  that  u\v  .
Set  w  =  (u,  v)x ,  I =  u/w  ,  m  =  v/w  .  Since  w  is  a  unitary  divisor  of  u,  we
have  (w , u/w)  =  1 ; that  is,  (/,  w)  =  1  and  similarly  (m,  w)  =  1.  Then

'  "  ffoo(")  fToo(/W)  O')

If  there  is  some  number  «  with  ox{n)  =  sn,  l\\n,  and  (m,  n/l)  =  1 ,  then
Theorem  15 implies  that  mn/l  is  also  infinitary  multiperfect.
For  example,  the  infinitary  perfect  numbers  2  3  5-7-17-41  and  2357-
13 • 17-41  may  be  taken  as  u  and  v.  Then  w  -  263417 • 41 ,  /  =  5 • 7,
and  m  — 5  7  13.  In  the  above  lists,  there  are  seven  later  occurrences  of  in-
finitary  multiperfect  numbers  n  such  that  l\\n  and  (m,  n/l)  =  1 , and  conse-
quently  there  are  seven  corresponding  infinitary  multiperfect  numbers  mn/l  =
527-13-/î.
Despite  the  apparent  ease of finding  infinitary  multiperfect  numbers,  it seems
to  be difficult  to  show that  all such  numbers  of a desired  shape  have  been  found.
We do  not  know,  for  example,  if there  are  any  infinitary  perfect  numbers  divis-
ible  by  8 but  not  16.  We  can,  however,  prove

Theorem  16.  The only infinitary  perfect  numbers  not divisible  by 8 are  6, 60, and
90.

Proof.  Let  n  be  an  infinitary  perfect  number.  If  n  — 2m  and  m  is odd,  then
the  proof  that  n  =  6  or  90  is similar  to  what  follows,  but  easier,  and  is omitted.

ON AN INTEGER'S  INFINITARY DIVISORS 407

Suppose  n  -  4m  , with  m  odd.  Since  a^  is multiplicative  and  0^(72) =  2« ,
we have

(1)  5^(771)  =  8m.

Then  5|w  and  iWa^m).  The  latter  implies,  by Theorem  13, that  m  can have
at  most  three  distinct  prime  factors.  There  are  thus  three  possibilities  for  the
shape  of  m , and  we  consider  them  in  turn.
Case  1:  m  =  5a .  From  (1),  0^(5")  =  8 • 5a_1 .  Since  the  left-hand  side  is
not  divisible  by  5, we must  have  a  =  1.  But  then  we have  no  solution.
Case  2:  m  -  5aq  ,  where  q  is  a  prime,  not  2  or  5.  By  Theorem  13,  (1)
must  take  one  of  the  following  forms:

(2)  (5a +  l)(/+l)  =  8-5a-1^,  ab>\,

(3)  (5a+l)(<7''+l)(/+l)  =  8-5a"y+rf,        fl>l,rf>c>l,

(4)  (5C+\)(5d+  l)(qh+l)  =  S-5c+d~lqb,        b>l,  d>c>l.

If  (2) holds,  then  5a + q   +1  =  3-  5a~'<?   , and  so, since  a  >  1 ,

q   =-¡-<  3.3-5a-'-l"

Then  q  =  3  and,  from  (2),  a  =  1 .  We thus  obtain  the  solution  n =  223 ■ 5 =
60,  and  this  is the  only  solution  to  arise  this  way.
c  d
Suppose  (3)  holds.  Neither  q  +  1  nor  q  +  1  can  be  divisible  by  4,  since
the  right-hand  side  of  (3)  is  not  divisible  by  16, so  we  must  have  qc >  9  and
qd >  81.  Then

4^8-5fl-1  _(qc+l)(qd  +  l)  _         1      J_         1

3  -    5a  +  1  q<+*  qc      qd       qc+d

I     _L       1     _ 820-     +  9 +  81 +  729 ~  729'

This  is a  contradiction.
Next,  suppose  (4)  holds.  Then  q    +  1  cannot  be  divisible  by  4,  so  q   >  9.
In  that  case,

9  qb  (5C-H)(5'+1)_5  /         1      J_        1

1Í1   -       /l        .  „     rr+d-\  0   I      +    «c  +    ,//   +10-^+1  S-5c+d~{  »V       5£     5d     5c+d

^  5  /,      1      1        1   \      39
£8     1 +  5 + 25 + T25    =50'

which  is a contradiction
Case 3:   m =  5'
( 1 ) takes the  form
Case  3:   m  =  5aí¡r V  , where  <? and  r  are  distinct  primes,  not  2  or  5.  Now

(5)  (5û+l)(^  +  l)(rc+l)  = 8.5fl-Vrc.

408 G. L. COHEN

Neither  q   +  1  nor  rc +  1  can  be  divisible  by  4,  so  we may  take  qb >  9  and
rc >  13.  Then
4     8-5a_1      (qb +  1)(/  +  1)  111
~ <   ,„  .  .   =-r4--=  1 +  ^-  +  ^  +3 -    5a + 1  9V  ~     V      rc     ^V
1   _L   _L   112-     +9  +  13 +  117 ~  117'

This  is a contradiction.
With  the  comment  above  that  all  infinitary  multiperfect  numbers  are  even,
the  proof  is now  complete.      D

6.  Infinitary  amicable  pairs  and  aliquot  cycles

We  call  two  integers  m  and  n  infinitary  amicable  if  a^m)  -  m  +  n  -
o^n).  A more  general  notion  is that  of  an  infinitary  aliquot  sequence  {n  }°^0 :
given  the  "leader"  n0 , we define  n-,  for  j  >  1,  by  «.  =  (r0O(nJ_l) -  «•_,  .  An
infinitary  aliquot  cycle of  order  r  is a  subsequence  nk ,  nk+x,  ...  ,  nk+r_x  with
the  property  that  nk+r  =  nk .  Such  cycles  of  order  1  are  infinitary  perfect
numbers,  and  cycles  of  order  2 are  infinitary  amicable  pairs.
A computer  run,  in  which  each  integer  less than  10  was  considered  in  turn
as  leader,  found  62  infinitary  amicable  pairs,  eight  infinitary  aliquot  cycles of
order  4, three  of order  6, and  one of order  11. These  are all given below.  In this
search,  there  were  36172  infinitary  aliquot  sequences  whose  eventual  behavior
was  unknown  in  that  a  term  of  the  sequence  exceeded  the  imposed  bound  of
1 2
9-10  .Of  the  remaining  sequences,  many  terminated  in  cycles  with  smallest
member  greater  than  10  .  There  was no systematic  search  for these,  so they  are
not  listed,  but  the  longest  observed  infinitary  aliquot  cycle was of  order  23 and
had  smallest  member  12647808.  The  computations  showed  that  there  are  no
other  cycles  of  order  less  than  17 which  have  smallest  member  less than  106.
Most  of  the  theorems  of  Hagis  [4,  6]  concerned  with  the  corresponding  no-
tions  for  unitary  and  biunitary  divisors  may  be  easily  adjusted  to  apply  also
to  infinitary  divisors.  These  give  means  of  obtaining  new  amicable  pairs  and
aliquot  cycles  from  known  ones.  A  survey  of  the  extensive  literature  on  the
corresponding  topic  for  ordinary  and  unitary  divisors  will  be  found  in  Guy  [3].
The  following  is  a  list  of  all  infinitary  amicable  pairs  with  smaller  member
less than  106:
 114 =  2-3-19  126 =  2-327

594 =  2-33ll  846 =  2-3247

1140 =  223 -5-19  1260 =  22325-7

4320 =  25335  7920 =  24325-11

5940 =  22335 - 11  8460 =  22325-47

8640 =  26335  11760 =  243-5-72

10744 = 2317-79  10856 =  2323 • 59

ON AN INTEGER'S INFINITARY DIVISORS 409

12285 = 3 5-7-13

13500 =  223353

25728 =  273- 67

35712 =  273231

44772 =  223-7-  13-41

60858 =  2•337223

62100 =  22335223

67095 = 335-7-71

67158 =  2•327-13-41

74784 =  253- 19-41

79296 = 263-7-  59

79650 =  2-335259

79750 = 2- 5311 -29

86400 =  273352

92960 = 255 -7-83

118500 = 223-5379

118944 =  25327-59
142310 = 2-5-7-  19- 107

143808 =  263-7-  107

177750 =  2-325379

185368 = 2317-29-47

204512  =  257-  11-83

215712 =  25327 • 107

298188 =  223311-251

308220 =  223-5-  11-467

356408 =  2313-23-  149

377784 =  233411 -53

420640 = 255- 11-239

462330 = 2-325-11-467
476160 = 2l03-5-31

482720 = 255- 7 -431

487296 =  273447
 14595

17700
 3-5-7-139

223-5259

43632 = 2433101

45888 = 2  3-239

,249308 = 2 3

83142 = 2-3

62700 223

71145 =  335

73962 = 2-3

96576 =  263

83904 263
 7-587

31-149

5211 - 19

17-31

7-587

503

19-23

107550 =  2-3252239

88730 = 2-5-  19-467

178800 243-52149

112672 = 2  7-503

131100 = 223 • 5219 • 23

125856 = 253219-23
168730 = 2-5-47-359

149952 =  263- 11-71

196650 =  2■325219 • 23

203432 =  2359-431

206752 =  257-  13-71

224928 =  253211 -71

306612 =  223317- 167

365700 =  223-5223-  53

399592

419256
 2  199-251

2334647

460640 = 2  5 • 2879

548550 = 2-325223-53

510720 = 283-5-7-19

574816 = 2511-23-71

516384 =  253211 • 163

410 G. L. COHEN

545238 = 2-3  23-439

576882 =  2-351187

600392 = 2313- 23 -251

608580 =  22335-7223

609928 = 2311 -29-239

624184 =  2311 -41 -173

635624 = 2311 - 31 • 233

643336 = 2329-47-59

643776 =  263-7-479

669900 =  223-527-  11-29

671580 =  22325-7-  13-41

726104 = 2317 - 19-281

784224 25327-389

785148 = 2"3 • 7 - 13 - 719

796500 =  22335359

815100 =  223-5211  •13-  1«

863360 =  275 -19-71

898216 =  2311 -59-  173

916200 233252509

947835

974400
 3  5-7-  17-59

263 • 527 -29

988038 = 2-3  19-107

998104 =  2317 - 41 • 179
 721962 = 2-3-19-2111

592110 =  2-345-  17-43

669688 = 2397-863

831420 =  22325-31-  149

686072 = 23191-449

691256 =  2371•1217

712216 =  23127- 701

652664 =  2317-4799

661824 =  2633383

827700 =  223-5231 -89

22325-7-587

2  53-1879

739620

796696

806976 =  2633467

827652 = 223-7-59-167

1075500 =  223253239

932100 =  223-5213-239

1339840 =  265 -53-79

980984 =  2347-2609

1072800 S    1    2
2  3-5-I49

1125765 =  335-31  -269

1147200 =  263-52239

1137402 =  2-347-  17-59

1043096 =  2323-5669

A  scanning  of  this  list  suggests  that  it  would  be  interesting  to  investigate  why
the  two  members  of  an  infinitary  amicable  pair  often  have  such  similar  prime
factorizations.  The  analogues  of  the  theorems  in  Hagis  [6] and  the  methods  of
te  Riele  [14]  go  part  of  the  way  in  explaining  this.
The  eight  infinitary  aliquot  cycles  of  order  4 with  smallest  member  less  than
106  are:
 (1026,  1374, 1386, 1494),
(10098,  15822, 19458, 15102),
(10260,  13740,  13860,  14940),
(41800, 51800, 66760, 83540),
(45696,  101184, 94656,  88944),

ON AN INTEGER'S INFINITARY DIVISORS 411

(100980,  158220, 194580, 151020),
(241824, 321216, 331584, 313056),
(685440,  1517760, 1419840, 1334160).
The  three  of  order  6 are:

(12420, 16380, 17220, 23100, 26820, 18180),
(512946, 869454, 891906, 933918, 933930, 769374),
(830568, 1245912, 1868928, 3288192, 5447088, 1076832).
Finally,  the  only  other  infinitary  aliquot  cycle of  order  less than  17 with  least
member  less than  10   is:

(448800,696864,  1124448, 1651584, 3636096,6608784,
5729136, 3736464,2187696,1572432,  895152).

Acknowledgment

It  is a  pleasure  to  acknowledge  the  assistance  given  by Martin  Caden  for  the
programming  involved  in  obtaining  the  figures  and  the  lists  of  infinitary  aliquot
cycles.
 Bibliography

1.  K.. Alladi,  On  arithmetic  functions  and  divisors  of higher  order,  J.  Austral.  Math.  Soc.  (Ser.  A)
23 (1977), 9-27.

2.  E. Cohen,  Arithmetical  functions  associated  with the  unitary  divisors of an  integer.  Math.  Z.  74
(1960), 66-80.
3.  R.  K.  Guy,  Unsolved  problems  in  number  theory.  Springer-Verlag,  New  York,  1981.
4.  P. Hagis, Jr.,  Unitary amicable numbers. Math. Comp. 25 (1971), 915-918.

5.  _,  Lower  bounds  for  unitary  multiperfect  numbers,  Fibonacci  Quart.  22  (1984),  140-143.

6.  _,  Bi-unitary  amicable  and  multiperfect  numbers,  Fibonacci  Quart.  25  ( 1987),  144-150.
7.  M. Lai, Iterates  of the unitary  totient function.  Math. Comp. 28 (1974), 301-302.

8.  B. B. Mandelbrot,  The fractal  geometry  of nature,  W.  H.  Freeman,  San  Francisco,  1982.
9.  M.  V.  Subbarao  and  L.  J.  Warren,    Unitary  perfect  numbers,  Canad.  Math.  Bull.  9  (1966),
147-153.

10.  D.  Suryanarayana,  The  number  of  k-ary  divisors  of  an  integer,  Monatsh.  Math.  72  (1968),
445-450.

11.  _,  The  number  of  bi-unitary  divisors  of  an  integer,  The  Theory  of  Arithmetic  Functions
(Proc.  Conf.,  Western  Michigan  Univ.,  Kalamazoo,  Mich..  1971),  Lecture  Notes  in  Math.,
vol. 251, Springer. Berlin.  1972, pp. 273-282.

12.  D.  Suryanarayana  and  R.  Sita  Rama  Chandra  Rao.  The  number  of  bi-unitary  divisors  of  an
integer. II, J.  Indian Math. Soc. (N.S.) 39 (1975), 261-280 (1976).
13. M. Sved, Divisibility—with visibility. Math. Intelligencer 10 (2) (1988), 56-64.

14.  H.  J.  J.  te  Riele,  On  generating  new  amicable  pairs  from  given  amicable  pairs,  Malh.  Comp.
42(1984),  219-223.
15. C. R. Wall, Bi-unitary perfect numbers, Proc. Amer. Math. Soc. 33 (1972), 39-42.
16._The  fifth unitary perfect number. Canad. Math. Bull. 18 (1975), 115-122.

School  of  Mathematical  Sciences,  University  of  Technology,  Sydney,  P.O.  Box  123,
Broadway,  New  South  Wales  2007,  Australia.  E-mail:  (ACSnet)  glcohen(5?utscsd.OZ  (uucp)
{ukc.mcvax,  ucb-cs,  uunct}!munnari!utscsd.  ozlglcohen
