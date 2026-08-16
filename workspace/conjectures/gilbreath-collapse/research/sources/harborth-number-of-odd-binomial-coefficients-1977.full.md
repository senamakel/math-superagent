<!-- source: https://www.ams.org/journals/proc/1977-062-01/S0002-9939-1977-0429714-1/S0002-9939-1977-0429714-1.pdf | converted from PDF -->

PROCEEDINGS  OF  THE
AMERICAN  MATHEMATICAL SOCIETY
Volume  62,  Number  I,  January  1977

NUMBER OF ODD BINOMIAL COEFFICIENTS

HEIKO  HARBORTH

Abstract.  Let  F(ri)  denote  the  number  of  odd  numbers  in  the  first  n  rows
of  Pascal's  triangle,  and  0  =  (log  3)/(log  2).  Then  o  =  lim  sup  F(n)/n9  =
1, and  ß  =  lim inf F(n)/ne  =  0.812 556 ...  .

It  is  known  that  almost  all  binomial  coefficients  are  even  numbers  (see  for
example  [l]-[3]).  This  means

lim   Fin)  /  (n  +  M  =  um   F(n)/n2  =  0,
n->oo  '      \       2      /       «-><»

if  F(n)  denotes  the  number  of  odd  numbers  in  the  first  n  rows  of  Pascal's
triangle.  Recently  in  [4] and  [5] it  is  asked  more  precisely  for  the  asymptotic
behavior  of  F(n).  Let

(1)  a=  lim    sup  F(n)/ne,        ß  =  lim    inf  F(n)/ne,
n—»oo  n—»co
and
(2)  9 =  (log 3)/  (log 2) =  1.584 962 ...  .

Then  it  is shown  in [5] that

1 <  a  <  1.052,    and    0.72 <  ß  < (9/7)(3/4)9<  0.815.

Furthermore  it is conjectured  that  1 and  (9/7)(3/4)*  =  3*/7  =  0.814 931 ..  .
are  the  true  values  of  a  and  ß.  In  this  note  we  will  prove  a  =  1   and
ß  =  0.812 556 ...  .

Theorem  1. a  =  1.

Proof.  Since

(2)-(")=!.    and    (")-°    (mod 2),        Ki<n-l,

for  n  =  2r, r  =  0,  1, .  . . , we  have  the  recursion
(3)  F(2r  +  x)  =  F(2r)  +  2F(x),        0  <  x  <  2r,     r  -  0,  1,...,

if,  in  addition,  F(0)  =  0  is  defined.  From  (3),  by  induction  on  r,  we  get

(4)  F{T)  =  3',
and  thus F(2r)/2H> =  372*  =  1 for  all r,  which yields a  >  1.
Next  we  assert

Received by the editors  March  19, 1976.
AMS (MOS) subject classifications (1970). Primary 10L10, 10A30.

©  American  Mathematical  Society  1977

19

20 HEIKO  HARBORTH

(5)  F(X  +  x)l  (2r +  x)"<  1    for   0  <  x  <  T,    r  =  0, 1,_

This  is  true  for  r  f= 0.  If  we  assume  the  validity  of  (5)  for  all  natural
numbers  <  r  -  1, we  can  use  F(x)  <  x9  for  0  <  x  <  2r  to  get  from  (3)  and
(4) that

-J  =  -g—  <-g  = f(x),        0 <  x  <  T.
(2r +  x)e  (2r  +  x)e  (?  +  xf

From
 à*            (2r  +  x)9+xK  }

it  follows  that/(x)  has  exactly  one  extremum.  This  together  with/(0)  =  f(2r)
=  1  and  f(2r~l)  =  5/3*  <  1  yields  f(x)  <  1  for  0  <  x  <  2r.  Thus  (5)  is
proved  by  induction  on  r,  and  from  (5)  we  conclude  a  <  1.

Theorem  2. ß  =  0.812 556_

Proof.  We  consider  the  sequence

(6)  [qr]  =  {F(nr)/nf}     with      nr  =  2nr_,  ±1,      «0 =  1,

where  +  or  — is  chosen  so  that  qr becomes  minimal.  So  for  r  =  1, 2,  .  . . , 25
we  have  to  choose
(7)  +-  +  -  +  +  -  +  -  +  +  -  +  -  +  -  +  +  -  +  -  +  +  -+.
If  tr  denotes  the  sum  of  the  binary  digits  of  nr,  the  first  eleven  values  of  nr,
F(nr),  and  /,  are
 r  nr  F(nr)             tr
0  1  11
1  3  5  2
2  5  11  2
3  11  37  3
4  21  103  3
5  43  317  4
6  87  967  5
7  173  2 869  5
8  347  8 639  6
9  693  25 853  6
10  1 387  77 623  7

Lemma.  {qr)  is  strictly  decreasing.

Proof.  We  suppose

(8)  F(2nr  +  1)/  (2nr  +  I)9>  qr    and     F(2nr  -  1)/  (2nr  -  \)e>  qr.

Using  (3),  (4),  and  the  binary  representation  of  nr  we  obtain

(9)  F(2nr  ±  1)  =  3F(nr)  ±  2\        tr=tr^+\±\.

NUMBER OF ODD  BINOMIAL COEFFICIENTS  21

(Here  the  reader  may  recognize  the  well-known  result  (see  [5] for  references)
that  the  number  of  odd  (")  is 2',  where  t  is  the  number  of  binary  digits  of  n.)
We  insert  (9)  and  (6)  in  (8),  and  substitute  2nr  =  a  and  2'r/(3F(nr))  =  b  to
get
 /        1 \*  0      6{9-\)
l  +  b>[l  +  -\    =1  +  -  +
V        a  )  a 2a1

i  \'+2(2-  »)•  ••(/  +  1 -  9)

(>-¿)f—! 0      Ö(Ö-l)-ä>I      -i=i--  +   V  .  }

+2 (2 -  9)  ■ ■ • (i  +  I  -  9)

('  +  2)!

Addition  of  the  last  two  inequalities  yields  the  contradiction

2 >  2 +  0(0  -  l)/a2+  • • •  >2.

Thus  the  inequalities  (8) cannot  both  be  true,  which  proves  the  Lemma.
Now  qr  >  0  together  with  the  Lemma  proves  the  convergence  of  {qr}.  It
follows that

(10)  B  <  q  =  lim  qr<  ql9 =  0.812 556 ...  ,
r^>cc
with

«„  =  710 317

=  219 +  217 +  215 +  214 +  212 +  210 +  29  +  27 +  25  +  23  +  22  +  1.

We  still  have  to  prove

(11)  F(n)/ne  >  0.812 556=  y.

This  is  true  for  1 <  n  <  2, and  we  assume  the  validity  of  (11)  for  1  <  n  <  2T.
To  obtain  the  step  from  r  to  r  +  1 in  a  proof  of  (11)  by  induction  on  r  we
have  to  conclude  from  this  assumption  that  (11)  also  holds  for  n  =  2r  +  x,
1  <  x  <  2r.  We  divide  this  interval  into  eleven  intervals:

n  =  2r~sm  +  x,         1  <  x  <  2r~s,

m  =  ns     for    5 =  1, 3, 6, 8,  10,
m -  n, -  1    for   j  -  2,4,  5, 7, 9, 10.

Let  t  be  the  sum  of  the  binary  digits  of  m,  and  2s <  m  <  2s+l.  Then  for
1 <  x  <  2r's  we get  from  (3) and  (4) that

F(2r~sm  +  x)        3r"i/'(w)  +  2'F{x)       y~sF(m)  +  2'yx*

(2'-J/n  +  x)e  (2r-sm  +  x)B  (2r-sm  +  x)9

The  unique  extremum  of fs(x)  is  a  minimum  at
 v i/(0-D=  2r-s(F(m)/ym2')

22  HEIKO  HARBORTH

For  m  =  ns and  s  =  \,  3,  6,  8,  10 we  check  by  calculation  that

(13)    /,(,)  > fs(xmm) = ((F(m)/m*fU-e)  + (yl'f^f^  y

is  fulfilled.  For  m  =  ns  -  \  and  i  =  2,  4,  5,  7,  9,  10 we  ascertain  that  in  these

cases  xmin  >  2r~s.  Then  for  5  i=  10,

F(»,-l)  +  Y2''-1      F(ns)  -  (1 -  y)2'--'
X (x)  > /,<*-')--ï-=--g->  y
ns  "s

is  seen  to  be  true  by  calculation.  In  the  case  m  =  «10—  1,5=10,  we  first
have
 3^(«io)  -  (3  -  Y)2'10"1
/ioW  > /io(2'-U)  =  -~-~g-  >  Y.        1 <  *  <  2
r-ll
(2/1,0 -  O

For  the  remaining  partial  interval

n  =  2'-10(w10  -  1)  +  2'-"  +  x  =  2'"11(2«10  -  1)  +  x,         1  <  x  <  2r~u,

we  choose  m  =  2«10 -  1 and  s  =  11 in  (12),  and  check  the  validity  of  (13).
Now  the  induction  on  r  is  complete,  and  we  have  proved  (11)  for  all  n.
Inequalities  (10) and  (11) then  yield  Theorem  2.
At  the  end  we  remark  that  q  from  (10)  probably  will  be  the  exact  value  of
ß.  Moreover,  we  conjecture  for  all  r,

F(n)/n"  >  qr    for     2r  <  n  <  2r+1.

It  seems,  however,  that  for  a  general  proof  we  should  know  some  more
properties  of  the  sequence  of  plus  and  minus  signs  beginning  with  (7).  Are
there  any  regularities  in  this  sequence?

References

1. N.  J.  Fine,  Binomial coefficients modulo a prime,  Amer.  Math.  Monthly  54 (1947), 589-592.
MR 9, 331.
2.  H.  Harborth,  Über  die  Teilbarkeit  im  Pascal-Dreieck,  Math.-Phys.  Semesterber.  22  (1975),
13-21.
3.  D.  Singmaster,  Notes  on  binomial  coefficients.  Ill:  -Any  integer  divides  almost  all  binomial
coefficients, J. London Math. Soc. (2) 8 (1974), 555-560.
4.  K.  B.  Stolarsky,  Digital  sums  and  binomial  coefficients,Notices  Amer.  Math.  Soc.  22  (1975),
A-669. Abstract #728-A7.
5.   _  ,  Power  and  exponential  sums  of  digital  sums  related  to  binomial  coefficient  parity,
SIAM  J. Appl.  Math,  (to appear).

INSTITUT   B  FÜR  MATHEMATIK,  TECHNISCHE  UNIVERSITÄT   BRAUNSCHWEIG,
D3300  BRAUNSCHWEIG,  WEST  GERMANY
