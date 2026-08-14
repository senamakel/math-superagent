<!-- source: http://spivey.oriel.ox.ac.uk/wiki/images/0/05/Expsearch.pdf | converted from PDF -->

Volume  5,  number  3  INFORMATIlaN  PROCESSING  LETTERS  August  1976

JonLouisBENTLEY*  Depurtment  of  Computer  Science,  University  of  North  Carolina,
Chupel  Hill  North  Carolina  2  7.5  ,‘4  :  ‘$A

and
hdrew  GMhih  YAO*
Depattr/rcnt  of  iUathematics,  ,Massachussetts  Institute  if  ‘I’echncdogy,
Cm&ridge,  Massuchussetts  02339,  USA

Received  14  November  1975,  revised  wsion  remr-kcd  7  Yune  IS176

Ordered  table  searching,  optimal  algorithms,  analysis  of  algorithms,  representations  of  integers.

1.  Intro6luctloa  .

Many  search  methods  based  on  comparisons  of  keys
ale  described  by  Knuth  in  [6,  section  6.21.  His  work,
ever,  deals  exclusively  with  searching  in  a  table  of
(that  is,  searching  in  a  bounded  key  space).
paper  we  will  consider  the  problem  of  compiari-
rching  in  an  unbounded  key  space.
e&act  formulation  of  the  problem  to  be
we  define  N+  to  be  the  s?t  of  positive  inte-
ify  the  function  F:AV+ +  {A-, Y) as

(
 x  for  j<n,

Y  forf>n,

a  b  an  integer  that  imiquely  def”mes  6;.  The
abounded  searching  is  the  follc&ng:  give
to  determine  n,  using  as  primitive  opera-
ns  of  fiti) to  X  for  a  sequence  of
algorithm.  That  is,  the  algorithm
nique  n  such  that  F(n) = Y a4
testing  different  values  of  F(i). We  !  by

-764X330,  and  by  IBM  Corporz&ion.
 that  n  is  the  scllution  to  the  unbounded  searching  prob
Ielm.  For  a  given  algorithm  A  let  us  define  the  cost
fii&:tion  CA  :N+  -*fl  as  CA(n)  =  m  iff  algorithm  /i
uses  m  evaluations  of  F  to  determine  that  rt  is  the  solu-
tion  to  the:  unbounded  search  problem,.
It  is  easy  to  see  an  isomorphism  between  the  prob
lem  of  unbounded  searching  and  the  problem  of  table
lookup  in  ati  ordered  table  of  infinite  size.  Given  S  =
s’,,Sz,SJ*.,.  ,L  9  strictly  increasing  inl’mite  sequence
of  reals  (Sk  E  R  and  Sk,  :.  >  Sk  for  all  k  E  N*),  suppose
that  we  are  asked  to  find  the  unique  fist  element  in  S
that  is  greater  than  or  equal  to  a  Fied  z  E  R using  as
a  primit%%  operation  only  the  question  *‘Is  Si  <  z?”
for  i E lb*.  To  solve  this  table  lookup  problem,  use
I$)  = X iff  Si  <  z;  the  desired  element  of  S is  then
Sn  where  n is the solution  to  the  isomorphic  problem
of  unbounded  searching,
It  is  also  easy  to  see  that  for  any  deterministic  un-
bounded  searr  il  algorithm  A  there  is  H  corresponding
binary  encoding  of  the  integers,  constructed  as  follows:
for  every  i  E  Al+,  the  codeword  representing  i  is  Si  =

V2  . . .acA(,T, where  am = 1  iff  the  23th  evaluation  of
JF  is  Y  when  \;  sing  algorithm  A  to  find  i as  the  solution
!to  the  unbouttded  search  problem.  Notice  that  the
length  of  the  codeword  Si  representing  i is  CA(i).
clearly  the  se?.  {Si}  is  a  pre$.X  set (i.e.,  Si  is  not  a  pre-
lx  of  Sj  for  j  #  i); if  it  were  not  a  prefa  set  then  al-
;g  >rithm  A  would  not  be  able  to  terrzW  ‘2  ac+zdr&y

Volume  5,  number  3  INFORMATION  PROCESSING  LETTERS  Aiqpst  !9?fi

for  the  i  in  violation  of  the  prefix  definition.
The  problem  of  unbounded  searching  arises  in
many  diverse  areas.  Suppose  that  one  wants  to  find
the  zero  of  function  G:fV+  +  R  that  is  known  to
cross  the  x-axis  only  once;  this  can  be  viewed  as  an
unbounded  searching  problem  if  one  ignores  such
(possibly  misleading)  properties  as  the  derivatives  of
G.  Testing  a  system  for  a  breaking  point  might  involve
an  unbounded  search;  one  knows  that  the  system
functions  with  zero  workload  and  wishes  to  find  that
workload  at  which  the  system  no  longer  fdncria-  >.
Unbounded  searching  could  be  used  in  searching  an
extremely  large  ordered  table  if  one  wanted  to  pay  a
search  cost  proportional  to  the  item’s  distance  from
the  front  of  the  table.  We  have  already  seen  that  every
unbounded  search  strategy  yields  a  uniquely  decipher-
able  prefer  encoding  of  the  integers;  therefore,  good
search  strategies  can  have  important  applications  in  in-
formation  theory.
We  investigate  a  number  of  algorithms  for  solving
the  unbounded  searching  problem  in  section  2.  In  sec-
tion  3  we  will  show  a  lower  botlnd  for  the  cost  func-
tion  C,(n)  for  any  unbounded  searching  algorithm  A
that  is  atmost  attained  by  one  of  the  algorithms  given
in  section  2.  Possib!e  topics  fat  further  work  in  this
area  are  mentioned  in  section  4.

2.  Unbounded  searching  algorithms

In  this  section  we  will  examine  a  number  of  algor-
ithms  for  unbounded  searching.

2.  I.  Akotithm  Bo  (wary  search)

The  most  straightforward  algorithm  for  unbounded
searching  is  to  test  F(l),  F(2),  .  .  .  ,  until  F(H)  =  I’.  It
is  easy  to  see  that  the  cost  of  this  algorithm  is  C&,(n)
=n  .

2.2.  A&withm  BI  (binary  search)

The  next  algorithm  suggested  is  the  standard
bounded  binary  search  algorithm,  uting  the  “gambler’s
stratew”  of  doubling  successive  guesses  to  provide  the
upper  bound  needed  for  the  binary  search.  More  pre-
cisely,  the  first  stage  of  the  algorithm  determines
m  =  I  lg  n  j  +  1  by  successively  evaluating  fi2”  -  1)  for
 r’=  1,2,...  unti)Ff””  -1)  =  Y,  ai  which  time  we

how  that  2”-”  *  1  II  PM  ?”  -  1.  The  becond  stage  tkien
uses  a  standaid  bounded  binary  search  OK  !Lv  :e:  P  -  1
elements  to  determine  the  exact  value  of  N.  The:  fiist
stage  will  require  m  =  [lg  zi  ./  f  1  evaluations  of  F  and
the  second  stage  will  require  lg  2m  \  -1  vz  --  1  =  1  Ig  II  1
evaluatiocs  of  F,  SO  the  total  cost  is  &,  (n)  =  21  lg  n  1
+  1.  Pt  is  helpfb\  to  view  an  unbounded  search  algorithm
as  a  decision  t:ee  in  which  the  label  i  cn  an  int~nai  node
represents  :Le  evdu&;Pion  of  F(i),  a  left  (right)  branch
corresponds  to  the  cutcome  of  the  evaluation  being
Y(X),  and  external  nodes  represent  solutions  to  the
problem.  Fig.  1  is  the  decision  tree  representation  of
algorithm  B,  .

2.3.  Algorithm  R:,  #otrble  bi:wary  search)

The  first  stage  of  algorithm  B,  essentially  uses  unary
search  (algorithm  B,  j  to  determine  m  =  Llg  n  J  +  1  by
successivley  evaluating  F(2’  -  I).  We  could,  hov,  :ver,
make  I*&  of  Ggorithm  B,  to  find  m  by  replacing  every
occurrence  of  the  expression  F(j)  in  stage  one  of  S,
with  the  expression  flu’  --  1).  The  cost  of  the  second
stage  of  the  resulting  algorithm  B,  will  be  the  same  as
the  second  stage  of  B,  (that  is,  m  -  1  =  I_lg  n;i9  but  the
cost  of  the  first  stage  will  be  reduced  fry=  l ‘,(;:z)  2
m  to  CB  I  (mj  =  2Llg(mj_/  +  1,  so  ths  total  cost  of  the
algorithm  (substituting  m  =  Llg  n  J  f  1)  is

C’$nj=  l.lgn.J+2  Llg(Llgn_J+  QJ+ 1.

(7  1

Fig.  1.  Decision  tree:  representation  <jf  algorithn  131.
 83

INFORMATION  PROCESSING  LITTERS  August  1976

2.4.  Al’rithm  l#h  (k-nested  binary  search)

To  syntheske  algorithm  B2  from  BI  we  replaced
unary  sear%  by  a  binary  search.  This  same  t&A-
que  could  be  used  to  create  a  new  algorithm  83  from

l  we  w  Duld  use  algorithm  B,  to  determine
I&J  {+  I)  _J  +  1  by  rewriting  I$!)  in  algorithm  B,

t0beN.Z  *‘-I  -  1);  (algorithm  B2  uses  a  unary  search
to  fid  &(Llg  n  J  +  1)J  +  1).  In  general  this  technique
could  be  applied  to  algorithm  Bk_f  to  yield  a  II~W  al-
rithni  Bk.
To  analyze  algorithm  Bk  we  define  Y’(n)  recursivety
by PC  1 n  en,

and rl”  (n)  =  Llg$(n)J  +  1.

We  define  Lj(n  2:  =:  l$n)  -  1  for  j  E  N.  It  is  easy  to  prove
by  induction  that
 CBk(Nj  =  L  l(n)  +  L $1)  + . . .+ L k-1(tj)  +2Lk(flj+  1

=  c  Li(n)tLk(r,)  t  1.
l<;i<k  Cl)

Our  discussion  of  algorithm  B,  provides  a  basis  for  the
induction.  We  will  not  give  a  detailed  forin  of  the  in-
ductive  part  here  but  the  spirit  of  that  proof  is  that  the
Lk(rz) t  1  in  (1)  represents  the  cost  of  a  unary  search
and  the  cost  of  the  corresponding  binary  search  is
2Lk+$z)  +  1.  Since  C’,(n)  =  n  =  LO(n)  +  1,  (1)  holds
for  any  k  EN.
It  is  helpful  to  view  the  algorithms  Bo,  B,  ,B2,.  .  .
~1s  a  progression.  To  do  this  we  have  represented  the
first  few  algorithms  in  fig.  2.  Each  box  in  the  figure
corresponds  to  what  might  be  thought  of  as  a  sub-
routine,  and  the  tree  structure  represents  the  calling
hierarchy.  Rounded  boxes  call  further  routines;  rec-
tangular  boxes  represent  basic  operations.  The  left
“subroutine”  of  a  round  box  is  called  before  the  “right”
subroutiie.
 Had  n  By
binary  nearch  4

by  binary  aaareh

Fig.  2.  Succession  of  algorithm  Bo,  B,,  B2,.  .  .  ,  Bk,  .  .  .  .

Volume  5,  number  3  INFORMATION  PROCESSING  LETTERS  August  1976

2.5.  Algorithm  6’  &,e  ultimate  algoritlvn)

Now  that  we  have  at  our  disposal  an  infinite  num-
ber  of  unbounded  searching  algorithms,  which  one
shall  we  use  for  a  particular  search?  If  we  choose  Bk
for  a  fixed  k  we  can  fall  into  either  of  two  traps:  if  k
is  small  and  11  is  large,  we  are  paying  the  high  cost  of
@(n)  when  we  could  be  paying  only  Lk(n)  +
2Lk+l(n),  which  is  quite  a  significant  difference  for
some  values  of  n  and  k.  On  the  other  hand,  if  k  is
large  and  11  is  small,  we  ;ould  be  using  “too  sophisti-
cated”  an  algorithm  and  therefore  paying  a  iot  of
comparisons  for  ver!’  little  information.  These  two
examples  hint  to  us  that  we  should  choose  k  as  a  func-
tion  of  n.
We  therefore  propose  that  algrxithm  U  consist  of
two  parts:  the  first  stage  will  chclose  an  appropriate
value  of  k  and  the  second  stage  will  then  use  algorithm
Bk  to  solve  the  problem.  The  above  two  examples  sug-
gest  that  to  avoid  both  traps  we  should  choose  the
least  k  such  that  Lk(n)  is  constant.  In  particular,  we
propose  to  choose  k  =  L*(u)  =  mini  such  that  U’(n)
=  1.  Since  L  is  defined  by  I,  it  will  be  easier  to  work
with  L*(n)  =  f(n)  =  mini  such  that  Z$r)  =  2.  By  the
defmition  of  Z$l)  we  can  see  that  I*(n)  is  the  least
j  E  I  such  that  g(j)  3b  n  where  g  is  defined  recursively
as

SlO)  =  2,

and

&+1)=2!=1.
(Notice  that  L*(n)  has  behavior  similar  to  lg*(n).)
Thus  the  first  stage  of  algorithm  U  will  determine  k
by  testing  mO)),  F(9(1)),  .  .  .  ,  until  F(g(k))  =  Y,
and  then  use  Bk  to  determine  n.
The  first  stage  of  algorithm  U  will  require  k  +  1  =
L*(n)  +  1  evaluations  of  F  to  find  L*(n).  Our  analysis
of  algorithm  Bk  tells  us  the  cost  of  the  second  stage.
Thus  the  total  cost  of  algorithm  U  is

C&I)  =  [  1  +  L*(n)]  f  [C  Bp(J”)l

=  4  +  I3.7)  +  ‘c
lGi<f,  *(n)  -1  L’(n).
 3.  A lower botlna

In  this  section  we  shaii  prove  a  lower  bound  for  the
cost  function  of  any  correct  unbounded  searching  al-
gorithm  which  shows  that  algorithm  I/  given  in  section
2  is  very  nearly  optimal.  We  domonstrated  in  section  1
that  any  unbounded  searching  algorithm  yields  an  en-
coding  of  the  integers.  For  a  given  encoding  of  the  in-
tegers,  let  An)  repreSent  the  number  of  hits  used  to
represent  t:re  integer  n.  By  the  mapping  of  search  al-
gorithms  to  codes,  any  lower  bound  for  f(n)  also  is  a
lower  bound  for  the  cost  function  C#‘(f2),  for  any  cor-
rect  unbounded  search  algorithm  A.
We  saw  in  section  1  that  the  codes  induced  by
search  algorithms  are  prefix  codes,  which  implies
Kraft’s  inequality  (see  [3]):
 (2)

We  shall  presently  show  that  (2)  implies  the  following
theoren: Theorem A:  For  infinitely  many  n,

An)  >  Igr2  f  lg(‘+r  +  .  .  .  +  lg(~*“+z  -  2(lg*  n)

Proof: Define,  for  positive  integers  I  and  n,

.2  i
k,  =  22”  1  --I  -2,

.
22  :
rt/  =  +  1,

t1;  =  22
 .’  .2  k1+1+2

1
and
 K(n)  =  lg*n  -lg*(lg’“n)  -  2.

The  following  facts  are  easy  to  verify:
Fact  1:  K(u)=klifnl<nGn;

p+  1)  ,,;  >  pr

lg(ki+l)r+  <  k,  +  I  f  3.

Fact  2:
s  dx  --
x(lgx)  (lg(2)x)  .  .  .  (lg%)  =  (In  2)”  ig(k+*)x.
 85

Vd~mct  5,  number  3  INFQRMATION  PROCESSING  LETTERS  August  1976

=  {n]n@zGz;,l=3,4,.  ..}.Then
itfly  many  n  E  A  such  that  2f@)

c  1  >  z  I

1  5  nl<  n<nS  n(lg  n)  (lg~2~*)  .  .  .  (lg(K(n”n)

ni
J  dx -  _.--_  ----
nl  x(lgx)(lg%)  l  .  .  (@Gj

i  (in  2~f)g@++ll,  .t:
 = ni =  “i

>(ln2~~(~l-kl--~-  3)

r  (21n  2YZ(l+  O(l)),  (3)
e  Facts  1  and  2  are  used  in  the  derivation  of  (3).
nce  2  In  2  >  1,  (3)  impiies  $  1/2P  =  00.  This
cloortrradkts  (2)  and  Lemma  B  is  proved.  Thus,  we
awn  that  for  infinitely  many  n  E  A,

Rn)  >  Ig  n  +  lgt2b  -t  .  .  .  +  Is’K(“‘+  ‘In

=  lgn  +  lge2),  +  .  .  .  +  lg@+%  -  k(g),

re

h(n)  3  Ig(kb)‘2)n  +  ’  .  .  .  4”  j*‘lg*“)n  .

Observe  that,  for  n:  <  n  <  ;.l;,  lg(k(n)+2)n  G  1g”n.  There
fore,

h(n)  4  lg%  +Ii9,(lg*n)  +  .  .  .  +  lg@*@*n)+lg*  n)

<  2lg*n  for  all  suff’iciently  lage  n.  (5)

l’lmxm  A  follows  from  (4)  and  (5)  immediately.
(F.  Chung  and  R.L.  Graham  have  pointed  out  that
Theorem  A  can  be  strengthened,  for  example,  to

f(n)  >  ig  n  i-  lg”n  +  .

l  =9  b

+  ig**“‘n  +  Ig(2)(lg’n)  t  O(1)

for  inEnitely  many  M,  To  do  this  they  imployed  a
theorem  stating  thirt  the  series  +

i
 c  I
 -v
na  1  /z(lg  n>(lg($  .  .  .  (lg@*“)ni(lg*n)  ,

is  divergent.  They  point  out  that  similar  techniques
can  be  employed  to  add  terms  0:‘

lgt2)lg*(n)  +  lgt3)lg*(n)  +  .  .

to  their  improved  lower  bound.)

4.  Areas  for  further  wark

There  are  many  ways  in  which  the  unbounded
search  probiem  can  be  extended.  To  model  a  multi-
comparator  system,  one  might  consider  unbounded
searching  with  primitive  operations  consisting  of  test-
ing  k  different  values  of  F.  Notice  that  the  outcome  of
such  a  test  has  k:  +  1  different  possibilities  and  hence
can  be  described  by  lg(k  +  1)  bits.  This  problem  is
similar  tc  Karp  and  k&ranker’s  generalization  of  flnd-
ing  a  maximum  of  a  function  [S]  (see  also  Linn  [4]).
We  considered  the  cost  of  evaluating  F  to  be  indepen-
dent  of  the  outcome  of  the  evaluation;  in  certain  c3p
plications,  however,  it  might  be  much  more  expensive
to  have  tested  (for  example)  a  Y  rather  than  an  X
(perhaps  in  locating  a  breaking  point  of  a  system).  In
Ageneral,  given  costs  x  and  y  of  evaluating  F  to  X  and
I’,  what  is  the  optimal  algorithm  to  use?  Knuth  de-
scribes  in  [6,  section  6.2.11  a  flbon,accian  search  for
a  finite  ordered  table.  Is  the  corresponding  unbounded
fibonaccian  search  interesting?
It  was  demonstrated  in  section  1  that  every  un-
bounded  search  strategy  suggests  a  prefii  encoding
of  the  integers.  Indeed,  Elias  [l]  has  studied  codes
that  are  isomorphic  to  each  of  the  search  strategies  in
section  2,  and  Even  and  Rodeh  [2]  have  studied  a
code  similar  to  algorithm  U.  Conversely,  does  there
exist  a  search  strategy  corresponding  to  every  prefix
code  for  the  integers?  Does  the  framework  of  un-
bounded  searching  provide  any  insight  into  problems
ion  theory?  What  are  the  implications  of  I)
the  lower  bound  derived  in  section  3  to  Elias’  work?

References
(l]  P.  Elias,  Universal  codework  sets  and  representation  >f  the
ns.  on  Information  Thetory  IT-21  (1975)
194-203.

Volume  5,  number  3  INFORMAT’ION  PROCESSING  LETTERS  August  8976

[  2  ]  S.  Even  and  M.  Rodeh,  Economical  encodifig  of  commas
between  strings.  IKHNiOilJ  Techn.  Rep.  No.  54  (July
1973),  Haifa,  Israel.
[  31  P.E.  Gallager,  Information  Theory  and  Reliable  Com-
munication,  (Wiley,  New  York,  1968).
141  J.  Linn,  General  methods  for  parallel  searchiig,  Tech.
 Rep.  No.  6  1  jb:  I  d  ‘iy41*~1s  f  ab.,  Stanford  Electronics
Lab.,  ~imtorcl  LJII~V.  (Maf#  1973).
[S]  R.M.  Karp  and  W.L.  Mirankier,  Parallel  minimax  search
for  a  maximum.  1.  of  Comb.  Theory  4,  pp.  19-35.
[6)  D.E.  Knuth,  The  Art  of  Computer  ProErramming,  vol.  3
(Sorting  and  SearcIting),  (Addison-Wesley,  1975).
