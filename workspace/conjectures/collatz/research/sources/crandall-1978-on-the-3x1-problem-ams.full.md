<!-- source: https://www.ams.org/journals/mcom/1978-32-144/S0025-5718-1978-0480321-3/S0025-5718-1978-0480321-3.pdf | converted from PDF -->

MATHEMATICS  OF  COMPUTATION,  VOLUME  32,  NUMBER  144

OCTOBER  1978,  PAGES  1281-1292

On  the  "3jc + 1"  Problem

By R. E. Crandall

Abstract.    It  is  an  open  conjecture  that  for  any  positive  odd  integer  m  the  function

C(m)  =  (3m  +  l)/2e(m),

where  e(m)  is  chosen  so  that  C(m)  is  again  an  odd  integer,  satisfies  Cr(m)  =  1  for

some  h.    Here  we  show  that  the  number  of  m  <  x  which  satisfy  the  conjecture  is

at  least  x      for  a  positive  constant  c.    A  connection  between  the  validity  of  the  con-

jecture  and  the  diophantine  equation  2    — 3y  =  p  is  established.    It  is  shown  that

if  the  conjecture  fails  due  to  an  occurrence  m  =  C  (m),  then  k  is  greater  than  17985.

Finally,  an  analogous  "qx  +  r"  problem  is  settled  for  certain  pairs  (q,  r)  ¥= (3,  1).

1.  Introduction.    The  "3x  +  1"  problem  enjoys  that  appealing  property,  often
attributed  to  celebrated  number-theoretic  questions,  of  being  quite  easy  to  state  but

difficult  to  answer.    The  problem  can  be  expressed  as  follows:   define,  for  odd  posi-
tive integers  x,  the  function:

(1.1)  C(x) =  (3x  +  l)/2eM,

where  2e^  is the  highest  power  of  two  dividing  3x  +  1.  Since  C(x)  is again  an  odd

integer,  one  can  iterate  the  C  function  any  number  of  times.  The  problem:  for  any

initial  odd  positive  x  is  some  iterate  C*(x)  equal  to  one?

This  "3jc  +  1 "  problem  has  found  a  certain  niche  in  modern  mathematical

folklore,  without,  however,  having  been  extensively  discussed  in  the  literature.    The

function  C defined  in  equation  (1.1)  is essentially  Collatz'  function  [1]  but  the  true

origin  of  the  problem  seems obscure.    The  algorithm  defined  by  successive iteration
of  C has  been  called the  "Syracuse  algorithm"  [2].    Some authors  [3],  [8]  have

defined  functions  equivalent  to  C  and  proclaimed  the  conjecture,  that  Ck(x)  =  1  for

some  k(x),  a  long-standing  one.    Some  partial  results  concerning  the  conjecture  are

known,  but  for  the  most  part  the  behavior  of  the  C  function  remains  shrouded  in

mystery.    It  is  hoped  that  the  partial  results  contained  in  the  next  sections  will  shed

some  light  on  the  problem.

2.  Preliminary  Observations.    Let  Z+  denote  the  positive  integers  and  let  D +

denote  the  odd  elements  of  Z+.    Some  elementary  properties  of  the  function  C;
D+  —► D+  as defined in  (1.1)  will now be  discussed.

Definition.    For  m  E  D+  the  trajectory  of  m  is the  sequence  Tm  =
{C(m),  C2(m),  .  .  .  },   where  it  is  understood  that  the  sequence  terminates  upon  the

first  occurrence  of  Ck(m)  =  1, k  EZ  +.     If  there  is  no  such  k,  then  Tm is  an  in-

finite  sequence.

Received  March  28,  1977;  revised  March  20,  1978.
AMS  (MOS)  subject  classifications  (1970).    Primary  10A25.
Key  words  and  phrases.    Algorithm,  diophantine  equation.
Copyright  ©  1978,  American  Mathematical  Society

1281

1282  R- E- CRANDALL

Definition.    For  m  E D+  the  height  of  m,  denoted  h(m),  is the  cardinality  of

the  trajectory  Tm.    In  the  case  that  Tm is  a  finite  sequence,  h(m)  will  be  the  least
number  of  iterations  of  C required  to  reach  1.
Definition.  For  m  E D+,  we  denote  by  inf  Tm the  least  positive  integer  in

the  sequence  Tm.  Further,  if  Tm is  bounded,  we  denote  by  sup  Tm  the  greatest  in-

teger  in  the  sequence  Tm.    If  Tm  is  unbounded,  we  say  that  sup  Tm  is infinite.
The  following  table  should  serve as  an  example  for  the  previous  notation:

m  Tm  h(m)  sup  Tm

1  {1}  11
7  {11,17,13,5,1}  5  17
27  {41,...,  1}  41  3077
2iooo_1  {?}  4316  >io476
2iooo  +  1  {?j  2417  <10301

24096_j  {?}  19794  ?

It  is  partly  the  erratic  behavior  of  the  height  function  h  that  gives interest  to  the

"3x  +  1"  problem.    The  main  conjecture  is:
Conjecture  (2.1).  For  every m E D+,  h{m) is finite.
This unsolved  conjecture  has  been  verified  for  m  <  109  [1],  [5].    One  of  the

few  partial  results  concerning  the  problem  is that  of  Everett  [3] :
Theorem  (2.1) (Everett).    For  almost all  mED+,  inf  Tm <  m.

This  theorem  is  interesting  because  if  inf  Tm  <  m  for  all  1  <  m  E  D+,  then  the
main  conjecture  (2.1)  is  clearly  true.  It  should  be  noted,  however,  that  while  Theo-

rem  (2.1)  reveals  a  definite  tendency  for  trajectories  Tm  to  descend  below  their  gen-

erating  integers  m,  the  theorem  has  little  to  say  concerning  Conjecture  (2.1).  In  fact,
it  is  not  even  known  whether  a  positive  density  of  odd  integers  m  satisfy  the  conjec-
ture.
 The  next  observation  gives further  indication  of  computational  difficulties
encountered  in  the  "3x  +  1 "  problem.
Theorem  (2.2).   As m  E D+  increases,  (sup  Tm )/m  is unbounded.
Proof.   Define, for  k EZ+,  the  number mk  =  2k  -  1.   It is readily verified that
C{mk) =  3  • 2k_1  -  1 if * >  1, and in general C'{mk)  =  3/2k-/'  -  1 if*  >/.    Thus,
for k  >  1 the  number
 Ck~x{mk)  =  3k-X2-1

is  a  member  of  the  trajectory  of  mk.    Therefore,  for  k  >  1 :

sup  Tm       3fc_12-l  .   ,
-->    „ft     ,    >(3/2)*-'mk  2k  -  1

and  the  right-hand  side  grows  without  bound  as  k  runs  through  the  positive  integers.

ON  THE  "3x  +  I"  PROBLEM 1283

It  is evident  that  numerical  calculations  of  the  heights  of  various numbers  by
computer  methods  must  necessarily involve the  storage  of  trajectory  elements  which
are,  in  proportion  to  the  starting  numbers  m,  arbitrarily  large;  unless,  of  course,  some

theoretical  method  is  discovered  to  simplify  such  computations.    It  is  natural  to  ask

whether  (sup  Tm)/ma  is  unbounded  for  various  powers  a.    The  set  of  integers  used

in  Theorem  (2.2)  is  sufficient  to  show  unboundedness  only  for  a  <  log2  3.    The  ir-

rational  number  t  =  log2  3  =  log  3/log  2  will  arise  in  a  natural  way  in  later  results.

3.  A Random-Walk Argument.  An heuristic  argument  that  lends  credibility  to

the  main  conjecture  (2.1)  can  be  stated  as  follows.  Assume  that  for  odd  integers  m
sufficiently  large the  real  number  log(C(m)/m)  is a  "random  variable"  with  a  distribu-

tion  determined  by  the  behavior  of  the  function  e{m)  as  defined  in  Eq.  (1.1).

One  "expects"  that  e{m)  =  k  with  probability  2~k.  Thus,  log{C{m)/m) is  approxi-

mately  log  3  -  k  log  2  with  probability  2~k.  Therefore,  one  "expects"  the  number
log{C{m)/m) to  be:
 Z     2-Mog(3/2fc) = -log(4/3),

tEZ+

indicating  a  tendency  for  C{m) to  be  less than  m.  If  one  then  imagines  that  iteration

of  the  C function  induces  a  random  walk  beginning  at  log  m  on  the  real  number  line,
an  heuristic  estimate  for  the  height  function  h{m) might  be:

ti  i\  ^  log m
(3.1)  h{m) log(4/3)

What is notable  about  this  argument,  aside  from  its  lack  of  precision,  is  that  estimate

(3.1)  is not  too  far  from  the  mark  in  a  certain  sense.    Since  we  expect  the  h  function

to  behave  erratically,  we  define  a  smoother  function  called  the  average  order  of  h :

(3.2)  #(*) = -     Z   Km).
X    m<x
meD  +

The  heuristic  estimate  (3.1)  translates  into  an  estimate  for  H{x):

(3.3)  H{x) ~  2(log(16/9))_1 log x  =  (3.476 . . . ) log x.

This  simple  statistical  argument  seems  to  be  partially  supported  by  the  following
data:
 x  H{x)/log x

11  1.440..
101  2.546 . .
1001  3.206 . .
10001  3.330 . .
100001  3.298 . .

It  would  be  of  interest  to  compute  H(x)/log  x  for  some  much  larger  value  of x,  say

1284 R.  E.  CRANDALL

1010.    In  the  absence  of  such  knowledge,  we  simply  conjecture:

CONJECTURE (3.1).   H(x)  ~  2  log jc/log(16/9).
This  conjecture  is  stronger  than  the  main  conjecture  (2.1)  in  the  sense  that  if
there  be  even  one  m  E  D+  with  infinite  height,  then  (3.1)  is  false.

4.   Uniqueness  Theorem.    We shall  presently  establish  a  certain  uniqueness  theo-

rem  which  is  useful  in  obtaining  partial  results  concerning  the  main  conjecture  (2.1).

Define,  for  a  E  Z+  and  n  rational  the  function:

(4.1)  Ba(n)  =  (2an-l)/3.

In  general,  Ba(n)  is  not  an  integer.    Further  define,  for  (backwards-ordered)  sequences

{at\i  =  k, k -  1, . . . , 2, l;a¡,  kEZ+},

the  functions

(4-2)  Bak.,Ml(n)  =  Bak(Bak_v„ai(n))  =  (2a^afc_j...ai(«)  -  l)/3.

Every  function  Bra.\(n)  is  thus  rational  by  construction  for  any  sequence  {a-,  a¡x,

.  .  .  ,a2,ax}  =  {a¡}.

Lemma  (4.1).   Ifn  E D+  and  Ba.  ai(n)  is an  integer,  then  for  1 <i  <j  all
numbers  Baj  ai(n)  are  odd  integers;  and  further

C(Ba¡+,  ...a j («))  =  Ba.„_a , (n),       C(Ba j (n))  =  n.

Proof.    Assume  for  some  k  with  1 <k  </'  that  Bak_a  (n)  E  Z+.    Then  from

(4.2)  we  conclude  2"kBak_l    ax(n)  is  also  an  integer.    But  by  construction,

Bak_x...axin)  =  y/3         for  some  integer  y  since  n  is  an  integer.     Since  2  and  3  are
coprime  it  follows  that  Ba¡(_l...ax(n)  Is an  integer  itself.    Thus,  as ¿?a....ai(")  is  an
integer  it  follows  by  induction  that  all  Ba.    a  (n)  for  1 <  /' </  are  integers.    Further,

from  (4.2)  we  conclude  that  3Ba¡...ax(n)+  1 is  even  so  each  Ba....ax(n)  must  be  odd.
Finally,
 C(Ba¡+x...ax(n))  =  Ba....ai(n)2ai+i-e  =  Ba..,Ml(n)

from  (4.2),  (1.1),  and  the  fact  that  application  of  the  C  function  on  an  odd  integer

yields  another  odd  integer.    That  C(Ba An))  =  n  follows  from  (4.1).

Lemma  (4.2).  If  an  integer  m  =  Ba. ...ai(l)  and  ax  >  2,  then  the  trajectory  of
m is
 Tm  =  {Bahx...axH),Bai_2...ax{l),  ...,  Z?aj(l),  1}.

Proof.    From  Lemma  (4.1)  the  assumption  m  =  Ba.  _a  (1)  is  an  integer  yields
the  correct  iterations  for  the  trajectory.    It  remains  to  show  that  none  of  the

Bai...axil)  is  equal  to  1.   This  follows  from  the  fact  that  C(l)  =  1, so  that  we  only

need  show  Ba  (1)  =£ 1.   But  this  follows  from  the  assumption  ax  >  2.
Definition.      Denote  by  G  the  set  of  finite  sequences  {ay, a¡_x,  .  .  .  , ax },
where  each  a¡  E  Z + ;ax  >  2;  and  the  following  congruences  are  satisfied:

ON  THE  "3x  +  I"  PROBLEM 1285

2fli  =  1  (mod  3)

p  1  (mod 9),

2^,^(1)=!  (mod 3)     for2<I.</.1)
f  1  (mod 9)
2*»iH-i,0)s1  (mod 3).

Lemma  (4.3).   ¿er  {a¡}  =  {a-, a-_j,  .  .  .  , ax }.   77/e« 5{aj.}(l)  /'s an  integer  of
height j  if and only if {a¡} E G.

Proof.    Assume  B  =  Ba„,aX{1)  is  an  integer  of  height  /.   Then  from  Lemma

(4.2)  each  Ba.    a  (1)  is  in  the  trajectory  of  B,  and  thus  Bai{l)  =£ 1,  so  ax  >  2.    The
congruences  (mod  3)  follow  from  Eq.  (4.2)  and  the  congruences  (mod  9)  follow

from  (4.2)  applied  twice.    Thus,  the  sequence  {a¡\i  =  j,  j  -  1,  .  .  .  ,  1}  is  in  G.

Now  assume  {a¡}  is  in  G.   Then  the  last  congruence  implies  Ba.  a  (1)  is  an  in-

teger,  and  Lemma  (4.2)  shows  this  integer  has  height  /'.

The  previous  lemmas  and  definition  of  the  set  of  sequences  G  enable  us  to

prove  the  uniqueness  theorem:
Theorem  (4.1).   Consider the  set  of  integers  which satisfy  the  main  conjecture
(2.1):
 M =  {mED+,m>  l\h{m)finite}.

Then, for  each  m  EM  there  is a  unique  sequence  {a¡}  EG  such  that

m=Ban(my..axH),

and  conversely,  for  each  {a¡}  E  G, i?{a/}(l)  E M.
Proof.   If m EM,  then  define the  integers

a,. =  e(Ch<m)-'(w))     for  1 <  /  <  h(m),

where  the  e  function  is as  defined  in  (1.1).    Then  by  inspection  we  have  m  =

Bah(m)...ai(l)  an(l  by  Lemma  (4.3)  we  have  {a,}  E  G.   To  show  uniqueness,  assume
for  some  {b¡\i  =  k,  k  -  1,  .  .  .  ,  1}  we  have  m  =  Bbk    b  (1).   Then  from  Lemma
(4.2)  k  =  him)  and,  since  the  C function  is  well  defined,  the  exponents  b¡  must

agree  termwise  with  the  a¡  so  the  sequences  {a¡}  and  {£,}  are  equal.    For  the  con-

verse,  we  note  that  {a¡}  E  G implies  B{a.j(l)  has  finite  height  by  Lemma  (4.3)

5.    Numbers  with  Given  Height.   The  set  M  of  integers  m>  l,  m  E  D+  of

finite  height  is naturally  partitioned  by  the  height  function  h.   There  are  infinitely-

many  numbers  m  with  h{m)  =  1, in  fact  these  m  are just  numbers  of  the  form

(4k  -  l)/3.    It  is natural  to  ask  whether  there  are  always  numbers  of  any  given

height.    This  question  can  be  answered  in  the  affirmative.    We shall  give an  estimate

of  the  relative  density  of  the  odd  integers  with  given height.
Lemma  (5.1).   Ba     ai{\)  <  2ai+a2+-+«//3/.

Proof.    Since  Ba  (1)  =  (2ai  -  l)/3,  the  assertion  is  true  for/  =  1.   From  Eq.
(4.2)  the  result  follows by  induction.

1286 R.  E.  CRANDALL

We shall  also  need  a  lower  bound  for  the  number  of  solutions  to  the  congruences
that  define  the  set  G:

Lemma  (5.2).   For  a real  number  z  >  0  the  number  of  sequences  of  length j  in
the  set  G with  ax  +  • • • +  ay <z  is greater  than  or  equal  to  (2[(z  -  2)/6j]  )'.
Proof.   Solutions  can be  restricted  by  the  inequalities

a,  -  2 <  (z -  2)/j;   a, <  (z -  2)1)    for 1<  / < /,

which  together  force  the  sum  a2  +  • • ■ +  a-  to  be  <  z  -  ax.    The  number  of  ways  of

choosing  the  quantity  ax  -  2  <  (z  -  2)1 j  is  at  least  2[(z  -  2)/6/]  ; since  only  2"1  =

4  or  7  (mod  9)  is  required,  and  out  of  every  six  consecutive  integers  at  least  two

must  satisfy  the  congruence.    Similarly,  once  ax  is  chosen  there  must  be  at  least

2[(z  -  2)/6/]  choices  for  a2  since  the  congruence  2"2Ba  (1)  =  4  or  7  (mod  9)  has
at  least  two  solutions  a2  out  of  every  set  of  six  consecutive  integers.    In  this  way  the

number  of  solutions  to  ax  +  • • • +  a,  <  z  is  seen  to  be  at  least  the  /th  power  of  the
quantity  2  •  [(z -  2)/6/].
These  lemmas  can  be  used  to  estimate  the  number  of  m  E D+,  m  <  x  which
have a given height h.

Theorem  (5.1).   Let  nh(x)  be  the  number  of  m  EM  with  h{m)  =  h  and  m
<  x.   Then  there  exist  real positive  constants  r,  x0  independent  of  h  such  that  for
x  >  max(*0,  2h,r),
 irh(x)>(logh2(xr))/h\.

Remark.    This  theorem  shows  that  for  any  positive  integer  h  there  are  infinitely
many m E D+  with height h.

Proof.   From  the  uniqueness  theorem  (4.1)  and  Lemma  (5.1)  it  follows  that
irh(x)  is  at  least  as  large  as  the  number  of  sequences  {a¡}  E  G,  of  length  h,  with

at  +  • • ■ +  an  <  log2(3'Ijc).    By  Lemma  (5.2)  this  implies

/log,(3\/4)
"■^y——2

obtained  by  bounding  the  square-brackets  from  below.    Now  we  choose  xQ such
that  x  >  x0  implies x/4  >  xx ¡2 ; and  choose  a  real  number  r,  0  <  r  <  1, such  that

r log2(3/64)  +  l/2>3er>0.

Then,  noting  from  Stirling's  formula  that  h\eh  >  hh,  we  can  transform  our  last  in-
equality  for  ^(jc),  in  the  case  that  x  is  greater  than  both  x0  and  2hlr,  to

_.  /iog2xrlo*2(3/64)+112  W       \ogh2(xr)
«h(x)>h-iy-j     >-_

6.    An  Estimate  for  n(x).    Let  n(x)  be  the  number  of  integers  m  <  x  which

belong  to  the  set  M  of  Theorem  (4.1).    Conjecture  (2.1)  is  equivalent  to  the  statement

that  ir(x)  is  precisely  the  number  of  odd  integers  greater  than  one  but  not  greater

than  x.    We establish  here  a  lower  bound  for  the  function  n(x).

ON  THE  "3x  +  1"  PROBLEM 1287

Lemma (6.1). t"      i
lim  e  '   y      —  =  -•

«<[fl
Remark.    This  lemma  can  be  proved  using  asymptotic  expansions  of  certain

error  functions.    An  exposition  of  various  formulas  pertaining  to  the  lemma  can  be
found in  [4].

Using the  results  of  the  last  section,  we  now  prove
Theorem  (6.1).  There exists a positive  constant  c such  that  for  sufficiently
large x
 tt(x)  >  xc.

Proof.   Using Theorem  (5.1),  we  can  find  r  >  0  and  x0  >  0  such  that  x  >  x0
implies ,,       ^  l'1^]  log^iX)

hez+  h=l  «!
From  Lemma  (6.1)  we  deduce  that  for  any  d  >  0  there  is  an xx  >  x0  such  that  x  >

xx  implies
 Tr(x)>(l/2-d)erlo^x,

which  is  enough  to  obtain  the  lower  bound  xc.

7.    Cycles.   Assume  that  all trajectories  Tm  for  m  E D+  are  bounded,  and  assume

that  no  m  >  1 appears  in  its  own  trajectory.    Then  the  main  conjecture  (2.1)  is true,

for  under  the  two  assumptions,  the  iterates  C(m),  C2(m),.  .  .  , C*apTm(m)  are  dis-

tinct  except  for  possible  ones;  and  since  each  iterate  is less  than  sup  Tm,  the  number  1
must  in  fact  appear  in  the  list  of  iterates.    It  is not  known  whether  either  of  the  two
assumptions  is true.    We shall  show  that  numbers  m  >  1 which  appear  in  their  own
trajectories,  if  they  exist  at  all, are  necessarily  difficult  to  uncover.    More  precisely,
we  shall  establish  a  lower  bound  for  the  period  of  an  infinite  cyclic  trajectory  in  terms

of  its  smallest  member.

Let  m  =  5ftfc.../,j(n)  for  some  positive  integer  sequence  {b¡}.    Define

k
(7.1)  A, =    £      bf    for  1 <  i <  *;
j=k-i+  I

AQ=0.

Then  the  B  function  can  be  expanded  to  give the  identity:

fc-i
(7.2)  2A*n -  3km =  Z  2Ai3k~x->.
j=o

The  identity  always  follows  from  the  statement  that  n  ETm,  for  if  «  appears  at  the

kth  position  of  Tm  then  the  assignment  bj  =  e(Ck~'(m))  gives m  =  Bb]ç...Dx(n) and

finally  (7.2).    Conversely,  if  (7.2)  holds  for  some  monotone  sequence  of  increasing

1288 R.  E.  CRANDALL

integers  0  =  A0  <AX  <  • • ■ <  i4k,  then  the  assignment  d¡  =  Ak_¡+  x -  Ak_x  gives

m  =  Bdk    d  (n),  so  by  Lemma  (4.1)  C  {m)  =  n,  implying  either  n  =  1 or  n  appears

in  the  fcth position  of  Tm.    In  either  case  n  E  Tm  and  we  have  demonstrated
Theorem  (7.1).   Let  m,  n  E D+.    Then  nETm  if and  only  if  there  exists  a

sequence  of  integers
 0  =A0  <AX  <A2  <      ■     <Ak

such  that  Eq.  (7.2)  holds.    Further,  if  such  a  sequence  {A¡}  exists,  then  n  =  1

or  the  kth  element  of  Tm is n.
Corollary  (7.1).   If  1 <mED+  and mETm  and  the period of  Tm is k,
then  there  exists a  sequence  of  integers  0=Ao<Ax<--<Ak  such  that

(7.3)  m(2Ak  -  3k)  =  £  2Ai3k~x-'.
/=o

Conversely,  if  Eq.  (7.3)  holds  for  such  a  monotone  sequence,  then  m  E  Tm  and

either  m  =  1 or  m  is  the  kth  element  of  Tm.
It  is  of  interest  that  if  m  appears  in  its  own  trajectory,  then  in  Eq.  (7.3)
the  factor  2^fc  -  3fe must  divide  the  right-hand  side.  If Conjecture  (2.1)  is true,  the

diophantine  equation  (7.3)  must  have  no  solutions  for  m  >  1, subject  to  the  constraint

of  monotonicity  on  the  {A¡}.    It  is  known  that  the  equation  2X -  3y  =  z  has  only
finitely-many  solutions  in  integers  x,  y  for  each  value  of  z  [9]  and,  in  fact,  can  have
at  most  one  solution  for  sufficiently  large  z  [10].    But  sharp  results  for  special  prime

values  of  z  can  be  obtained  on  the  assumption  that  the  main  conjecture  (2.1)  is  true.

If  Conjecture  (2.1)  is  true,  then  the  impossibility  of  solutions  to  the  diophan-

tine  equation  (7.3)  can  be  shown  to  imply  that  if  2  is  a  primitive  root  of  a  prime  p,

any  solution  in  integers  x,  y  to  2X -  3y  =  p  must  have  y  <  p/(t  -  1),  where  t  =
log2  3.

It  is  of  interest  that  if  a  pair  of  integers  (a,  b)  can  be  found  such  that  b  >  1 and

0<2a-3ö     divides    2a-ft-l,

then  the  main  conjecture  (2.1)  is  false.  Indeed,  if  we  write

2°-»  -  1 =  d(2"  -  3b),

then  the  number  m  =  2bd  -  1 satisfies:

m(2a -  3b) =  3b -  2b =  Z  2/3*-''-1,
/=o

and  since  m  >  1,  Corollary  (7.1)  implies  h(m)  is infinite.

Corollary  (7.1)  shows  that  if  the  main  conjecture  is  true  then  powers  of  two  and

three  tend  to  be  poor  approximations  of  each  other.    The  number  r  =  log2  3  must

be  accordingly  difficult  to  approximate  with  rational  numbers.    This  notion  will  be
made  precise  shortly.    For  the  moment  we  display  the  first  50  elements  of  the  contin-
ued  fraction  for  t  =  log2  3
 ON  THE  "3x  +  1"  PROBLEM  1289

r=  [1,1,1,2,2,3,  1,5,2,23,2,2,  1, 1, 55, 1, 4, 3, 1, 1,15,
1, 9, 2, 5, 7,  1, 1, 4, 8, 1, 11, 1, 20, 2, 1, 10, 1, 4,  1, 1, 1
1,1,37,4,55,1,  1,49,  ..  .]

=  [a0,aj,a2,  .  .  .  ,a4g].

The  convergents  to  this  fraction  are  determined  by  recurrences  [6],  [7]

P0=a0;         p_x  =  l;

(7.6)  4o  =  1;       4_i=0;
Pn=anPn-l+Pn-2       for  n  E  Z+;

«n  =  Wn-l   +  Qn-2     for  «  £  Z+  ■

The  ratio  pjqn  is  called  the  nth  convergent  to  t.

The  next  three  lemmas  stem  from  the  theory  of  rational  approximation.    Rele-

vant  material  can  be  found  in  [6]  and  [7].

Lemma  (7.1).  Let  pjqn  denote  the  nth  convergent  to  t  =  log2  3.    Then for

any  pair  of  integers  (x, y)  with y  <qn,

\p„  -q„t\<  \x-yt\.

Lemma (7.2).  For  p„/q„  convergents to  t,

^Pn-lnt^iln  +  4n+lT%  •

Lemma  (7.3).   For  p„/q„  convergents  to  t,  let y  <qm.    Then

\2X-y  \>  y  log2\pm-qmt\.
Proof.
 12* -  3*1 =  3*lexp(* log 2 -y  log 3) -  11
>3J'log2ljc-yfl.

When y  <qm,  Lemma  (7.1)  implies  the  desired  inequality.

We now  focus  our  attention  on  numbers  m  >  1  for  which  m  E  Tm.    It  is  clear

that  every  infinite  cyclic  trajectory  contains  such  an  m.
Lemma (7.4).   If  1 <  m  =  inf  Tm, then for  the A¡ as defined in Eq.  (7.1),

2Ai<{3  +  l/m)>.

Proof.    From  C(x)  =  (3x  +  1)/2C**) we  infer,  since  m  <  C'{m)  for  each/,  that

C'+X(m)  <  C'(m)(3  +  l//«)/2e<c/(m».

But this implies
 m  <  C'(m)  <  w(3  +  l/m)'/2Ai

giving the  desired  inequality.
Lemma  (7.5).   Let  Km  =  inf  Tm and  let  k  be  the  period  of  the  trajectory

Tm.   Then m <ki3  +  l/mf-x  H2Ak -  3k).

1290  R.  E.  CRANDALL

Proof.    From  Corollary  (7.1)  and  Lemma  (7.4)  we  have

k-i
m{2Ak -  3k) <  Z  (3 +  l/mf-1
f=o

and  the  desired  inequality  follows  from  direct  evaluation  of  the  sum.

These lemmas  enable  us  to  establish  a  connection  between  the  size of  the  period
of  a  possible  cyclic  trajectory  and  the  continued  fraction  for  /  =  log2  3.

Theorem  (7.2).  Let  p„/qn  be  convergents  to  t.    Let  1 <  m  =  inf  Tm and  let
k be the period of  Tm.   Then for  n >  4:

k  >  min{qn,  2m/{qn  +  qn+x)).

Proof.   If k  >  q„,  the  result  is trivial so  assume k  <qn.    Then  from  Lemmas
(7.3) and (7.5) we have
 k{3 +  l/m)k-x
m  <-,
3k log 2 lp„-<?„/!

from  which  we  see  that

k  >  m{log 2)(3  +  l/m)\pn  -  qnt\{l  -  k/3m).

But  n  >  4  implies  qn  +  qn+x    >  20  using  Eq.  (7.5).    Thus,  if  k  >  m/10,  the
result  of  the  theorem  is  trivially  true.    So  we  assume  k  <  m/10.    But  this  implies
(1 -  k/3m)  >  29/30  and  from Lemma (7.2),

{3m +  1) log 2                       2m
k >  -——  (29/30) >-.
In+ln+l  In+ln+l

Corollary  (7.2).  For  any  given  k  there  are finitely  many  cyclic  trajectories
with period  k.

Proof.    This  corollary  follows  directly  from  the  observation  that

min(qn,  (2  inf  Tm)/(qn  +  qn+  x))  is  unbounded  for  any  infinite  set  of  trajectories  as
n  increases.

The  known  result  that  no  1 <  m  <  109  appears  in  its  own  trajectory  can  be  used
to  establish  a lower  bound  for  any  period  k.
Theorem  (7.3).  Assume m>  1 and  Ck(m) =  m.   Then k >  17985.

Proof.    For  1 <  m  =  Ck(m)  the  trajectory  Tm is  infinite  cyclic,  and  there  is
thus  an  m0  =  inf  Tm  with  m0  >  109.    Since  m0  =  Ck(m0),  the  number  k  is  greater
than  or  equal  to  the  period  of  Tm   .   Therefore,  from  Theorem  (7.2)  we  infer  that

A:>min(í7n,2-109/(í7n+í7n  + 1))

for  any  n>  4.    From  Eq.  (7.5)  we  compute:

qx0  =31867;       ?u  =79335;

so either k >  31867 or k >  2 •  109/111202.   The latter bound is greater than 17985.

ON  THE  "3x  +  1"  PROBLEM  1291

8.   The  "qx  +  r"  Problem.   Define for q, r E D+ ; q >  1 the  function

(8.1)  Cqr(m)  =  (qm  +  r)/2<V(m>

valid  for  m  E  D+  with  eqr(m)  always  chosen  to  force  Cqr(m)  E D+.    The  generalized
"qx  +  r"  problem  can  be  stated  thus:   given (q,  r),  for  every  m  E D+  is there  a  k

such  that  Ck(m)  =  1 ?   What is  remarkable  about  this  problem  is that  strong  evidence
points  to  the  following  rather  curious  conjecture:
Conjecture  (8.1). In  the  "qx  +  r"  problem,  with q,  r E D+  and  q  >  1, some
mED+  fails  to  satisfy  an  equation  Ck(m)  =  1 ; except  in  the  case (q,  r)  =  (3,  1).

This  conjecture  says in  a  word  that  unless  q  =  3  and  r  =  1, the  generalized

height  function  h   (m)  will be  infinite  for  some  m  E D+.    We shall  presently  attempt
to  argue the  plausibility  of  the  conjecture.

It  is  easy to  prove Conjecture  (8.1)  in  the  special  case r  >  1.   Indeed  for  such  an

r  choose  any  m  =  0  (mod  r).  Then  Cqr{m)  •  2e<7r(m^ =  qm  +  r  =  0  (mod  r)  and,  as

r  is  odd,  Cqr{m)  =  0  (mod  r).    But  this  means  all iterates  of  m  are  destined  to  be
divisible by  r,  hence  Ck(m)  =  1 is impossible  for  r  >  1 and  m  =  0  (mod  r).

The status  of  Conjecture  (8.1)  is  unsettled  for  most  of  the  remaining  "qx  +  1"

problems.    It  is known  that  the  conjecture  is  true  for  q  =  5,  181,  and  1093;  but  all
other  cases  remain  elusive.
The  case q  =  5 is settled  by  the  observation  that  m  =  13 gives rise to  a  cyclic
trajectory  {33,  83,  13,..  . }, whose  occurrence  can  be  traced  back  to  the  diophantine
equation  27  -  53  =  3; and  an  equation  similar  to  (7.3)  exists  with  3  replaced  by  5
and k  set  equal to  3.
The  case q  =  181 is  resolved  by  the  observation  that  m  =  21  gives rise  to  a  cy-
clic trajectory  {611,  27,  ...  }; arising from  the  diophantine  equation  215  -  1812
=  7.
 The  third  solvable case, q  =  1093,  is rather  peculiar.    In  this  problem,  a number
m  has  height  one  if  and  only  if  it  is  of  the  form

m  =  (2364P  -  1)/1093;

but,  as it  turns  out,  all other  m  have infinite  height.    This  follows  from  the  fact  that
in  the  "1093*  +  1"  problem,  no  m  can  have  height  2,  since  Eq.  (7.2),  with  3

replaced  by  1093,  n  =  1, and  k  set  equal  to  two,  is  easily  seen  to  be  impossible.

This  case is  the  only  one  for  which  it  is  known  that  almost  all  m  have  infinite  height.

The  examples  q  =  5,  181,  1093  being  the  only  known  q  for  which  Conjecture

(8.1)  is  true  (with  r  =  1),  why  is  the  conjecture  plausible?    The  answer  is,  simply,  it

is likely  that  for  any  q  >  3,  some  m  has  a  diverging  trajectory  in  the  "qx  +  1"  prob-
lem.   In  fact,  the  heuristic  arguments  of  Section  3 indicate  that  log{CqX{m)/m) should

be  about  log(í¡r/4), which  is  positive  for  odd  q  >  3,  so  that  numbers  should  tend  to  be

"pushed  upward"  by  application  of  the  C,  function.

In  spite  of  the  above  considerations,  it  is  unknown  whether  even  a  single m  in
a  single "qx  +  1"  problem  gives rise  to  an  unbounded  trajectory.    The  outstanding
unsolved  case  is  the  "Ix  +  1"  problem,  for  which  there  may  be  no  infinite  cyclic

1292 R.  E.  CRANDALL

trajectories.    What makes  the  "Ix  +  1"  problem  all the  more  interesting  is the  empiri-
cal observation  that  the  number  m  =  3  gives rise to  a  trajectory  reaching to  102000

and  beyond,  with  no  apparent  tendency  to  return.

Acknowledgements.    The  author  wishes  to  acknowledge  the  hospitality  of  the

administration  of  Reed  College, at  whose  Computer  Center  the  calculations  for  this
paper  were  performed.    The  author  also  wishes to  thank  Joe  Roberts  and  J.  P.  Buhler
for  their  valuable  suggestions  concerning  the  manuscript.

2234  S.  E.  20th  Street
Portland,  Oregon  97214

1.  J.  H.  CONWAY,  "Unpredictable  iterations,"  Proc.  1972  Number  Theory  Conference,
Univ.  of  Colorado,  Boulder,  Colorado,  1972,  pp.  45-52.
2.  I.  N.  HERSTEIN  & I.  KAPLANSKY,  Matters  Mathematical,  1974.
3.  C.  J.  EVERETT,  "Iteration  of  the  number-theoretic  function  f(2n)  =  n,  f(2n  +  1)  =
3n  +  2,"  Advances  in  Math.,  v.  25,  1977,  pp.42-45.
4.  M. ABRAMOWITZ  &  I.  STEGUN  (Editors),  Handbook  of  Mathematical  Functions,
9th  printing,  Dover,  New  York,  1965.
5.  Zentralblatt  für  Mathematik,  Band  233,  p.  10041.
6.  J.  ROBERTS,  Elementary  Number  Theory-  A  Problem  Oriented  Approach,  M.I.T.  Press,
Cambridge,  Mass.,  1977.
7.  Y.  A.  KHINCHIN,  Continued  Fractions,  Univ.  of  Chicago,  Chicago,  111., 1964.
8.  Pi  Mu  Epsilon  Journal,  v.  5,  1972,  pp.  338,  463.
9.  S.  S.  PILLAI,  J.  Indian  Math.  Soc,  v.  19,  1931,  pp.  1-11.
10.  A.  HERSCHEFELD,  Bull.  Amer.  Math.  Soc,  v.  42,  1936,  pp.  231-234.
