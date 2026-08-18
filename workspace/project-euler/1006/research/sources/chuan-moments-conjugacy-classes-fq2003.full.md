<!-- source: https://fq.math.ca/Scanned/41-3/chuan.pdf | converted from PDF -->

CHARACTERIZATIONS  OF  ^ W O R D S 5  MOMENTS,
AND  DETERMINANTS

Wai-feng  Chuae
Depaxtment  of  Mathematics,  Chung-yuan  Christian  University,  Chung-Li
Taiwan  32023,  Republic  of  China
(Submitted  August  2000-Final  Revision  December  2002)

1.  I N T R O D U C T I O N

Throughout  this  paper  we  consider  binary  words.  All  results  can  easily  be  stated  for

words  over  other  two-letter  alphabets.  For  any  word  w,  let  \w\  denote  the  length  of  w  and  let

\w\i,  called  the  height  of  w,  denote  the  number  of  occurrences  of  the  letter  1 in  w.  For  n  >  1  "

and  ci? c 2 ? . . . ,  cn  E  {0,1},  define  operators  T  and  ~  by

T ( c i c 2 . - . c n )  =  c 2 . . . c n c i ?

( c i C 2  . .  .Cn)~  =  Cn  .  .  . C 2 C i .

For  each  integer  j , let  T J  have  the  obvious  meaning.  The  operator  T  is  called  the  cyclic  shift

(or  rotation)  operator.  A  word  u  is called  a  conjugate  of a word  w  if u  — T^(w)  for  some  integer

j .  The  set  of  all  distinct  conjugates  of  w  is  called  the  conjugate  class  of  w  and  is  denoted  by

[w]. The  word  w  is  called  the  reversal  of  the  word  w.

A  word  w  is  said  to  be  a  palindrome  if  either  w  is  the  empty  word  or  w  =  w.  w  is  said  to

be  primitive  if  it  is  not  a  power  of  another  word,  w  is said  to  be  a  Lyndon  (resp.  anti-Lyndon

word  if  it  is  the  smallest  (resp.,  largest)  in  the  lexicographic  order  in  the  conjugate  class  of  '

w.  w  is  said  to  be  bordered if  there  are  words  x  and  y  with  x  nonempty  such  that  w  =  xyx;

otherwise,  w  is  said  to  be  unhordered.

For  w  — cic 2 ..  .Cqj where  each  a  is either  0 or  1, define  M(w)  =  ]Ci=i(<Z +  l  ~i)
ci-  M{w)

is  called  the  moment  of  w.  Define

M([«/])  =  {M(«)  : u  E  H } ?

<$(«;) =  max{M(te)  — M(t?)  : u,v  £  [w]}.

One  way  to  define  a™words  is  to  make  use  of  T  and  the  words  w ( |  J  define  below.  (See

[13] for  the  original  definition  and  basic  properties  of  a-words.)

Let  p  and  q be  two  relatively  prime  positive  integers  with  p  <  q.  Let  [0, a% + 1 , a 2 , . . . , an]

be  the  continued  fraction  expansion  of  | .  Define  a  sequence  of  words  w_i, WQ, w i , . . .  ,wn  re-  -

cursively  as  follows:  Let  w_i  =  1,  u0  =  0,  and  for  1 <  &  <  n,  let

f  ti*.-2ti2-i  (*
  i s  even)
l  "fc^iWfc-2  (A; is  odd).

194  [JUNE-JULY

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

It  is  know  that  the  word  un  depends  on  | ,  but  not  the  continued  fraction  expansion  [1, 2].

Denote  un  by  u  (|J.  Clearly,  its  first  (resp.,  last)  letter  is  0  (resp.,  1).

A  word  w  is  said  to  be  an  a-word  if  either  w  E  {0, 1}  or  there  are  two  relatively  prime

positive  integers  p  and  q  with  p  <  q  such  that  w  is  a  conjugate  of  u  (
Ej.  Conjugates  of

u  [-JF^-)  (resp.,  u  ( - J ^ - J  )  are  known  as  binary  Fibonacci  words  (see  [6]).

We  first  report  briefly  some known results  about  the  word  u  — u  (
E)  and  its reversal.  The

conjugates  w, T(u),...,  Tq~1(u)  of u  are  exactly  the  distinct  a-words  with  length  q and  height

p.  Thus  each  a-word  is  primitive.  The  word  u  (resp.,  u)  is  a  Lyndon  (resp.,  anti-Lyndon)

a-word  (see  [1,11]).  The  word  u  is  the  only  binary  word  which  has  two  factorizations  of  the

form  u  =  xy  =  Ozl,  where  x,y,  z  are  palindromes,  \z\  =  q —  2, \y\  =  s  and  1  <  s  <  q  is  such

that  ps  =  l(mod  q)  (see  [20]).  The  conjugate  class  [u] of  u  is  closed  under  taking  reversals.

Clearly  u  — T~
s{u).  Both  u  and  u  are  unbordered.  Furthermore,  the  set  of  Lyndon  a-words

and  their  reversals  are  the  only  unbordered  finite  Sturmian  words  (a  finite  Sturmian  word

is  any  finite  factor  (or  segment)  of  any  characteristic  word  (see  section  5))  [14].  The  set  of

Lyndon  a-words  coincides  with  the  set  of  Christoffel  primitives  (see  [1,2]  for  the  definition  of

Christoiffel  primitive).

Let  [0, a\  +  1, a 2,...., an]  be  the  continued  fraction  expansion  of  | .  In  [13], it  was  shown

that  a  word  w  is  a  conjugate  of  u  if  and  only  if  there  are  integers  n , . . . ,  rn  with  0  <  ri  <

a>i, 1 <  i  <  ^?  and  words  w-i,wo,w±,...,  wn  such  that

tt/-i  =  1,  Wo  =  0,  Wn  =  W,

Wi  =  w f i 7 r i W i _ 2 ^ [ i i 3  1  <  i  <  n.

In  fact,  each  conjugate  T
k{u)  of  u  corresponds  to  those  n-tuples  ( r i , . . .  , r n )  of  integers  with

0  <  n  <  a{,  1  <  i  <  n  and  k  =  ^ = 1 r < ^ _ i ( m o d  g),  where  c?_i  =  q0  =  1,  qi  =  a»gi-i  +

gj_2,  1 <  i  <  n.  Thus,  each  a-word  can  be  obtained  recursively  by  concatenation.  The  words,

having  length  q and  height  p,  obtained  with  n  =  • • •  =  rn  =  0 or  n  =  • •  •  =  r n - i  =  1 — rn  =  0

are  called  standard  Sturmian  words  (see  [1]).  It  is  not  hard  to  see  that  a  word  w  having  length

q  and  height  p  is  a  standard  Sturmian  word  if  and  only  if  w  =  T(u)  or  w  =  T(u).

Let  u  (j)  =  0  and  u(j)  =  1.  I f |  and  y  are  consecutive  fractions  in  the  Farey  sequence

of  any  order  with  |  <  |y,  then  u  (fij^r)  =
  u  H)
  u  [JT)-  -^
so  ^ n e  mapping  r  h-> w(r)  is  an
increasing  function  from  the  set  of  all  reduced  fractions  in  [0,1]  onto  the  set  of  all  Lyndon

a-words.  In  other  words,  if  r  <  r
!  then  u(r)  <  u(r
f)  in  the  lexicographic  order  (see  [2]).

2003]  195

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

More  results  -  both  old  and  new  -  about  u  11 j  will  be  presented  below.

In  an  earlier  paper,  the  present  author  proved  that  if w  is an  a™word having  length  q,  then

M([w])  is  a  set  of  q  consecutive  positive  integers  and  S(w)  =  q —  1.  Each  of  these  properties

actually  characterizes  a-words  (Theorem  4.4).  The  result  used  to  prove  this  characterization

is itself  a  characterization  of a-words  (Lemma  2.1)  with  other  interesting  consequences  besides

Theorem  4.4.  In  section  3, we obtain  characterization  of elements  of the  set  P E R  and  standard

Sturmian  words  (Corollary  3.2),  and we identify  those a-words  that  are palindromes  (Corollary

3.4).  In  section  5,  we  compute  the  determinants  of  a  class  of  matrices  involving  a-words

(Theorem  5.1).  As  a  special  case,  we  obtain  a  sequence  of  (0,l)-matrices  Ai,  A2  . . .  such  that

An  is an  Fn  x Fn  matrix  whose rows are precisely  the Fibonacci  words  having length  Fn,  height

F n _ i  (resp.,  F n _ 2 ) ,  and  det(An)  =  F n _ x  (resp.,  F n _ 2 ) .

2,  A  L E M M A

[11,14,16,18]  present  some  characterizations  of  a-words.  The  characterization  proved  in

[11]  is  restated  in  Lemma  2.1  below.  With  this  result,  we  know  exactly  where  the  ones  in

each  a-word  are  located  and  so  each  a-word  can  be  generated  directly  without  using  a-words

of  shorter  lengths.  Corollary  2.2  shows  how  all  a-words  having  the  same  length  q  and  height

p  may  be  ordered  in  such  a  way  that  consecutive  pairs  differ  in  exactly  two  adjacent  letters.

Sections  3-5  present  some  interesting  consequences  of  Lemma  2.1  and  Corollary  2.2.

L e m m a  2 . 1 :  Let  p  and  q  be  relatively  prime  positive  integers  with  p  <  q.  Define  s  as  the

unique  integer  with
 sp  =  l(mod  q)  and  1 <  s  < q.  (1)

Let  u  =  u  (A.  Then  for  0  <  j  <  q -  1,

thefc**  letter  of  Tjs(u)  is  1

<$=^k  =  (r  — j)s  (mod  q)  for  some  r  with  0 <  r  < p  —  1,

<=^k  =  1 +  (r  +  j)(q  — s)(mod  q)  for  some  r  with  1 <  r  <  p.

A  proof  of  Lemma  2.1  appears  in  the  Appendix  (see  also  [11]).

C o r o l l a r y  2.2:  Let  p ? g ? s ,  and  u  be  as  in  Lemma  2.1.  Let  0  <  j  <  q —  1.  The  words  T^s(u)

and  T^+1^s(u)  differ  by  exactly  two  adjacent  letters.  If i  =  (p— 1 —j)s  (mod  q)  and  1 <  i  < g,

then  the  (i  -  l)
th  and  the  i
th  letters  in  Tjs(u)  and  Tij+1)s(u)  are  01  and  10  respectively.
P roof:  Let  0 <  j  <  q —  1.  The  positions  of  1 in  T^s(u)  and  T^+1^s(u)  are  respectively

-j*>  (i  ™ i k .  - -,  (P  -  2 -  j)a,  (p  -1  -  j > ,

196  [JUNE-JULY

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

and
 ( - J  -  1)*, -js,  (1 -  j)s,...,  (p -  2 -  j)s

(mod g).  If (p—j—l)s  =  i  (mod q) where  1 <  i  <  g, then  clearly i  ^  1 and  (—j — l)s  =  i — 1

(mod  g).  Hence  the  words  T^(w)  and  T^+1>(u)  differ  by  exactly  two  letters.  The  (i  -  l)
th

and  the  i
th  letters  in  T*8(u)  and  r ^ + 1 ) 5 ( w )  are  01  and  10  respectively.  D

We  remark  that  when

g  =  F n  andj>  =  F n _ i ,  5 -  i  , n > 3 .
[  Fn™2  (n  odd)

Then  Lemma  2.1 and  Corollary  2.2 reduce to Theorem  2 (or Corollary  12(i) of  [6]) and  Theorem

3  of  [10]  respectively.
 3.  I M M E D I A T E  C O N S E Q U E N C E S

Throughout  this  section,  let p, g3 5, and  u  be  as in  Lemma  2.1.  We  shall  show  how  Lemma

2.1  yeilds  new  and  old  results  on  factorization,  PER,  standard  Sturmian  words,  lexicographic

order,  reversals  and  moments.

C o r o l l a r y  3.1:

(a)  u  =  xt/j  where  x  and  y  are  palindromes  with  \y\ =  s  and  \x\  =  q — s.

(b)  u  — 0^1, where  z  is  a  palindrome.

Note that,  by  taking reversals,  we immediately  derive  from  (a)  and  (b)  respectively  that  u  —  yx

and  u  =  lz0.

Proof:  The  proofs  of  (a)  and  (b)  are  almost  identical  so  we  suffice  with  the  proof  of  (b).

Let  2 <  k<q-l.

The  k
th  letter  of  u  is  1

<=$*  k  =  rs  (mod  q)  for  some  r  with  1 <  r  < p  —  1  (by  Lemma  2.1  with  j  =  0)

<=$»  g + 1  — k  =  (p — r)s  (mod  q)  for  some  1 <  r  < p  —  1  (by  equation  (1))

<=> the  (q +  1-  k)
th  letter  of  u  is  1.

Therefore  the  result  follows.  D

Let  PER=  {0,1} U {z  : Ozl  is  a  Lyndon  a»word}0  Note  that  the  empty  word  belongs  to

PER.  Let  PER01=  -f>01  : z  e  P E R } . The  set  PER10  is  defined  similarly.  The  set  of  standard

Sturmian  words  equals  {0,1}U  PER01UPER10.  Elements  of  P E R  and  standard  Sturmian

words  have  been  recently  studied  extensively  (see  [1]).  The  following  corollary  provides  char-

acterizations  of  these  words.

Corollary  3.2:

(a)  Let  z  E  PER  with  \z\  =  q -  2  and  \z\i  =  p  -  1 >  1.  Then

the  k
th  letter  of  z  is  1

2003]  197

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

k  =  rs  —  1  (mod  q)  for  some  r  with  1 <  r  <  p  —  1

fe  =  r(g  —  5)  (mod  q)  for  some  r  with  1 <  r  <  p  —  1.

(b)  Let  w  E PER01  and  «/  G PER10  with  |w|  =  |w;]  =  g  and  H i  =  \w'\!  =  p .  Then

the  fc
t/l  letter  of  w  is  1

<=4> fc =  rs  —  1  (mod  g)  for  some  r  with  1 <  r  <  p;

the  k
th  letter  of  tt/  is  1

<=^  k  =  r(q  — s)  (mod  q)  for  some  r  with  1 <  r  <  p.

P roof:  Part  (a)  follows  from  Lemma  2.1 and  the  fact  that  Ozl  =  u.  Part  (b)  follows  from

the  fact  that  w  =  T(u)  and  w'  —  T(u).  D

When  the  conjugates  of u  are  listed  as  in  (2)  below 3 we  observe  some  interesting  phenom-

ena.

C o r o l l a r y  3,3  (see  [11]):

(a)  The  sequence  of  words
 u, T
s(u),  T2s(u),...,  Tto-V*(u)  =  u  (2)

is  increasing  in  lexicographic  order.

(b)  Ti*(u)  have  increasing  moments  with  M(T*
8(u))  =  fclKi±li  +  j  -f  1  (0  <  j  <  ^ -  1).

P ro o f:  Part  (a)  and the recurrence  relation  M(T^ + 1 ) s(?i))  =  M(T^ s(w))+l ?  0  <  j  <  q-2,

follow  immediately  from  Corollary  2.2  and  the  definition  of  M .  Thus  M(T
js(u))  =  M(u)  +

J? 0  <  j  <  g —  L  We  have

- ^ ( w )  ~  ^  l ^ + l ~ "  I  —  +  1)  I + 1  (by  definition  of  M  and  Lemma  A3  of  Appendix)

: « ( p - i ) - E

P " 1  r %

P J
A=I *-
 +  1  (by  rearrangement)

=  q(p -  1) -
  {q  1}!f
  1 }  +  1 (by e.g.  [5])

( g + l ) ( p - l )
2
  + 1 '

proving  (b).  D

The  above  corollary  generlizes  Corollaries  2  and  3  of  [10].  The  following  corollary  gener-

alizes  Lemmas  6  and  7 of  [7].

198  [JUNE-JULY

CHARACTERIZATIONS  OF  Of-WORDS,  MOMENTS,  AND  DETERMINANTS

C o r o l l a r y  3.4:

(a)  Tb-i-fi'fa)  =  (Ti
s(u)y  ,  0  <  j  <  q -  1.

(b)  If  q is  odd,  then  [u]  contains  exactly  one  palindrome,  namely  TV^~")s(?i);  if  g is  even? [u]

contains  no  palindrome.

Note,  letting  j  =  0 in  (a)  yields  u  =  T~
s(u).

Proof:

Let  0 <  j  <  q —  1.  By  repeated  use  of  Lemma  2.1, for  1 <  k  < g3
the  ( g +  1 -  k)
th  letter  of T ^ " 1 - ^ 5 ^ )  is  1

<^=>- q +  1 — k  =  1 +  (r  +  (q —  1 — j))(q  — s)  (mod  g)  for  some  1 <  r  <  p

<<=>  k  =  (r ;  — j)s  (mod  g)  for  some  0 <  r
f  < p  —  1

4=>  the  k
th  letter  of T^'
s(w)  is  1.

This  proves  (a).  Part  (b)  follows  immediately  from  part  (a)  and  the  distinctness  of  the
T
j(u).  n
 4.  M O M E N T S  O F  a - W O R D S

For  any  binary  word  w,  let  S(w)  =  max{M(u)  —M(v)  : w, v  £  [w]}-  The  following  lemma

summarizing  the  properties  of  moments  of  a-words  is  an  immediate  consequence  of  part  (b)

of  Corollary  3.3.

L e m m a  4 . 1 :  Let  w  be  an  a-word  with  \w\ =  q  >  2  and  \w\i  — p.  Let  u  — u  (|  J.  Then

(a)  M(u)  =  minM([w))  =
  (p"1}2(g+1)  +  1,  Af(fi)  =  maxM([w])  =
  ( p + 1 ) 2 ( g + 1 )  -  1.

(b)  5(w)  =  g -  1.
(c)  M ([«/])  is  a  set  of  q  consecutive  positive  integers.

We  shall  prove  in  Theorem  4.4  below  that  each  of the  conditions  (b)  and  (c)  is  equivalent

to  saying  that  w  is  an  a-word.  We  need  the  following  lemma  which  is  useful  when  studying

moments  of  binary  words.

L e m m a  4.2:  Let  w  be  a  binary  word  with  \w\  =  q  and  \w\i  =  p.  Let  M& =  M(T f c («/)),  0  <

k  <  q.  Let  w  =  c\C2 . . . cq  where  each  a  is  either  0 or  1.  Define  cq+j  =  Cj for  1 <  j  <  q.  Then

for  0  <  r  <  k  <  g,  we  have
 k
Mk-MT=p(k-r)-q  ]P  c*.
t = r + l

In  particular,  Mk  -  M 0  =  pk  -  q X)t=i Cj if fc > Q»

2003]  199

CHARACTERIZATIONS  OF a-WORDS,  MOMENTS, AND DETERMINANTS

P roof:  For each  k  with  0 < k < q — 1, since  Tk(w)  = ck+ick+2  • • • c&+g? we have

q  k+q  k+q
Mk = Yl(
q +1~  ^
Ck
+J
  =  ^ ( f c  + ^ + 1~ ^
Ci
 =P(k  + q +  l ) -  J2  ici

j = l  i~k+l  i=k+l

If r  < kj  then
 k+q  r+q
Mk-Mr=p(k-Jrq-\-l)-  ] P  j C j -p(r  + q + l)+  Y*,  ici
j—k+1  «=r+l

Jb  &+g
=  p(fc -  r ) +  J ^  *Cj -  ] T  jcj-
i = r + l  j = r + g + l

k
=  p(k -r)  -q  Y2f  ci-  n

i=r+l

L e m m a  4.3:  Let w b e a binary  word  with  \w\ = q > 2 a n d \w\i = p.  If 8(w)  = q —  1 then q

and  p are relatively  prime  positive  integers  and w is an a-word  conjugate  to u (|  J.

Proof:  L et w E  [w]  with  M(u)  — minM([w]).  L et fci,&2,. --,fc9  b e a  permutation  of

0 3 1 , . . .  ,q — 1 such  that  Jfci =  0 and M ^  < M^2  <  • • • <  M&g.  Let u = c\c2 . . . c g  where  each  a

is  either  0 or 1. Define  cq+j  = Cj for 1 < j  < q.  B y th e assumption  an d Lemma  4.2?  we have

' - l  =  Mibfl  -M kl  =pkq-q^2ci,

* = i

and  so g  a n d p  are relatively  prime  positive  integers.  Again  by Lemma  4.2? th e  moments
Mkl,  Mk2,...,  Mfcg  are all distinct  and therefore  M^ m + 1  — Mkrn  =  1, f o r l < m < g  —  1.

Let  1 < m < g —  1.  Lemma  4.2  also  implies  that

1 -  Mkm+1  -  Mkrn  = { p(km  •+1 ~  km)  ~~ q l^i=krn  + l
 ci  C
1* km  <  fcm+i),

j=fcm+1+l
  C^ ~ P\km  ~~  km+l)  V
1* &m+l  <  &m)-

200  [JUNE-JULY

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

Define  s  by  equation  (1).  Then
 ,  S  -  (km<  fcm+l)
km+1  '  ™m  [  8  -  < q  (km+i  <  km)

=  5  (mod  g)

and  therefore  km  =  (m  —  l)s  (mod  q).

We  claim  that  ckr  =  0  for  p  +  1  <  r  <  q.  To  show  this,  let  1  <  m  <  q  — p.  Since

km+p —  ^TO  =  (ra +  F ~~ l ) s  —  (ra  —  l)s  =  ps  =  l(mod  q)  and  ~~q +  1  <  fcTO+p  — fem <  q —  1,

it  follows  that  fcTO+p  — <fcTO equals  either  — q +  1 or  1.  If  &TO+P —  km  =  — q +  1,  then  &TO+P =  0

(and  km  =  q —  1).  But  then  ra  + p  =  1,  a  contradiction.  Therefore  feTO+p  =  km  +  1.  According

to  Lemma  4.2,  we  have

P =  Mkm+p  -  Mkm  = p(km+p  ~km)~q  ] P  a  =  p  -  f cfcm+p;

so  c&m+p  =  0,  proving  our  claim.

Since  \U\Q =  q — p,  we  see  that

ck  =  1 «£=£- k  =  q  OT kr  for  some  r  with  2  <  r  <  p

k  =  rs  (mod  q)  for  some  r  with  0 <  r  < p  —  1.

It  follows  from  Lemma  2.1  that  w  =  u  (|  J.  Consequently  w  is  an  a-word.  D

Combining  Lemma  4.1  and  4.3, we  have  the  following  characterization  of  a-words.

T h e o r e m  4.4:  Let  w  be  a  binary  word  with  \w\  =  q  >  2.  Then  the  following  statements  are

equivalent:

(a)  5(w)  =  q-l,

(b)  w  is  an  a-word,

(c)  M([w])  is  a  set  of  q consecutive  positive  integers.

R e m a r k  4.5:  For  w  —  ciC2...c g  where  each  a  is  either  0  or  1,  define  S(w)  ~  XX=i*c*°

The  results  about  moments  can  easily  be  reformulated  using  S(w)  instead  of  M(w).  Plainly

S(w)  =  M(w),  and  S(w)  +  M(w)  =  (\w\  +  l)|w|i-  Graphically,  a  word  w  is  represented  by  a

polygonal  path  from  A(0,0)  to  B(\w\,  \w\i)  as  follows:  starting  from,  the  origin  A,  represent  a

0  (resp.,  1)  in  w  by  a  horizontal  unit  segment  going  to  the  right  (resp.,  a  vertical  unit  segment

going  upward,  followed  by  a  horizontal  unit  segment  going  to  the  right).  This  polygonal  path

2003]  201

CHARACTERIZATIONS  OF  Of-WORDS,  MOMENTS,  AND  DETERMINANTS

divides  the  rectangular  region  having  opposite  vertexes  .A
7(—1,0)  and  B  into  two  subregions.

The  one  below  (resp.,  above)  the  polygonal  path  has  area  M(w)  (resp.,  S(w))  (see  Figure).

i-----S|W)
 _ P  (^  - Q .
 M(w) ----1

0 1 1 0 1 0

5,  D E T E R M I N A N T S  O F  M A T R I C E S  I N V O L V I N G  a - W O R D S

Throughout  this  section,  let  q  and  p  be  relatively  prime  positive  integers  with  p  <  q.  Let

u  — u  I -).  Regarding  each  binary  word  as  a  vector,  we consider  the  q x q  (0, l)-matrix  whose

j t h  row  is  the  a-word  T~^"
1\u)^  1 <  j  <  q.  It  is  easy  to  see  that  this  matrix  is  a  circulant

matrix,  that  is,  a  matrix  of  the  form

Ci  C2

C2  C 3
 Cq— 1  Cq

Cq-2  Cq-i

Cl

where  Ck is  the  k
th  digit  of  «.  We  denote  this  matrix  by  circ(u)  (see  [19]).

Among  all  the  matrices  obtained  from  circ(u)  by  permuting  its  rows,  the  matrix  circ(u)

is  of  particular  interest  for  the  following  reasons.

Let  a  be  any  irrational  number  between  0  and  1  such  that
  E  is  a  convergent  of  the

continued  fraction  expansion  of  a.  The  characteristic  word  f(a)  is  an  infinite  binary  word

whose  k
th  letter  is  [(k  +  l)a]  -  [fca],  k  >  1  (see,  for  example,  [3,  13-15,  21,  23]).  When

a  =  g~ 1, /(a)  is  called  the  golden  sequence  (see,  for  example,  [4,  8,  9,  12,  17,  24,  25]).

202  [JUNE-JULY

CHARACTERIZATIONS OF a-WORDS,  MOMENTS, AND DETERMINANTS

Golden  sequence  turns  out  to  be  the  Fibonacci  binary  word  pattern  JF(1, 01)  (an  infinite  word

W1W2W3 . . . ,  where  w\  =  x  and  w^  =  y  are  binary  words,  and  wn  — wn-2wn-iy  n  >  3,  is

called  a  Fibonacci  binary  word  pattern  and  is  denoted  by  F(x,y)  (see  [17,  25])).

It  is well-known  that  for  each  k  >  1, there  are  exactly  fe+  1 distinct  factors  (or  segments)

of  f(a)  (see  [23]).  Let  y  denote  the  palindrome  that  differs  from  u  only  by  the  last  (resp.,

first)  letter  if  the  q
th  letter  o f / ( a )  is  1 (resp.,  0).  It  was  proved  in  [13] that  for  1 <  k  < q,  the

rows  of  the  upper  left  (k  +  1)  x  k  submatrix  of  the  (q +  1)  x  q  matrix

circ(u)

1  y  (resp.,  circ(u)
y

are  precisely  the  k  +  1 distinct  factors  of  / ( a )  of  length  k.

Another  interesting  fact  about  circ(u)  is  contained  in  the  following  theorem.

T h e o r e m  5.1:  det(circ(u))  — p,  if  q  >  1.  Here  u  ( j )  =  0  and  u  ( \ )  =  1.

Since  the  matrices  under  consideration  are  circulant  matrices,  their  eigenvalues  and  hence

their  determinants  can  be  computed  using  the  q
th  roots  of  unity.  However  the  following  row

rule  proof  based  on  the  combinatoric  properties  of  Corollary  2.2  is  more  elegant.

Proof:  Let  u  — c\C2 •. •  7cq  where  c i , . . .cq  E  {0,1}.  Clearly  the  result  holds  for  q  <  2.

Now  let  q >  3.  Using  (1),  for  1 <  t  <  q,  define  1 <  it  <  q such  that  it  =  l  +  (t  —  l)s  (mod  q).

Denote  circ(u)  by  A  and  its  (i,  fc)-entry  by  A(i,  k).  For  2  <  t  <  q,  since  row  it  (resp.,  it-i)  of

A  is  T"it+1(u)  =  T^-^iu)  (resp.,  r ^ - t + 1 ^ ( t i ) ) ,  Corollary  2.2  implies  that

A(it-i,it  -  1)  =  1,  i4(t t-i,«t)  =  0,

j 4 ( i t , i t - l )  =  0,  A(it,it)  =  1,

A(it,k)  =  A(it~ijk)  for  k  ^  it  and  k  ^  it  —  1.

Let  JB be  the  matrix  obtained  from  A  by  adding  (—1)  times  row  it-\  to  row  it,  for  each

t  =  g, q —  1 , . . . , 2,  in  the  order  given.  Then

B(l,fc)  =  A(l,fc)  =  Cib,

J3(it, k)  -  ( - l ) ^ ( i t _ i , fc) +  Afa,  k)

f  - 1  (fc  =  it  -  i)

=  <  l(k  =  it)
[  0  (otherwise),

2003]  203

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

where  2  <  i  <  g,  and  1  <  k  <  q.  Since  %2, i s ? . . . , iq  is  a  permutation  of  2 , 3 , . . . , g,  it  follows

that  B  is  the  matrix
 Cl
- 1
0
 C2
1
- 1
 C 3  . .
0  ..
1  ..

•  Cg-l
0
0
 cq
0
0

0  0  0  -1  1

Clearly,
 det(circ(u))  —  det(B)  =  Y ^ c& = p-  D

k=i

Here  is  a  special  case  of  Theorem  5.1.  Let  {vn}  and  {z n}  be  sequences  of  Fibonacci  words

given  recursively  by

VQ  =  l , v i  =  0,v2  =  l , v n  =  S
I  Vn_2Vn-l

t;n_i?/n_2  (n  is  odd)
(n  is  even),

Zi  =  1,^2  =  0,£ n  =  <  ^ n_2^n-i  (n  is  odd)
is  even),

Let  An  =  circ(vn)  (resp.,  circ(zn)),  n  >  1.  Since  -^r-1  =  [ 0 , 1 , 1 , . . . , ! ]  (n

^ r i - 2 1  ones)  (resp.,  -p  [ 0 , 2 , 1 , . . . , ! ]  (n  — 3  ones)),  n  >  3,  we  see  that  vn  =

(u  (^Y
12-))  (  resp.,  zn  — (u  f ^ p M  J  J ,  n  >  1.  It  follows  from  Theorem  5.1  that  each

An  is  an  Fn  x  F n  (0,1)  -  matrix  whose  rows  are  precisely  the  Fibonacci  words  having  length

Fn  and  height  F n _ i  (resp.,  F n „ 2 )  and  det(An)  =  F n _ i  (resp.,  F n_2).

A P P E N D I X .  A  P R O O F  O F  L E M M A  2.1

For each real number  0, the infinite  binary  word  f(0)  whose k
th  letter  is  [(AH-l)0] — [fc0],  k  >

1,  is  called  the  characteristic  word  of  0.

L e m m a  A l  (see  [21]):  Let  0 <  61  <  1.

204  [JUNE-JULY

CHARACTERIZATIONS  OF  O-WORDS,  MOMENTS,  AND  DETERMINANTS

(a)  If  0  is  irrational  and  k  >  1,  then
 the  k
th  letter  of  f(0)  is  1

<=>k  =  for  some  h  >  1.

(b)  If  0 =  |  is  rational,  where p, g are  relatively  prime  positive  integers,  and  k  >  1, fe  ^  0  and

k  ^  —1 (mod  g),  then
 the  fe
t/l  letter  of  / ( 0)  is  1

for  some  h>l,  h^Q  (mod  p). ^=>k  =

Throughout  the  rest  of  this  section,  let  p  and  q be  relatively  prime  positive  integers  with

p  <  q.  Let  I  <  s  <  q,l  <t  < p,  and  ps  =  qt +  1.  Let' n  =  w ( |  j .  If  w  is  a  word  and  w  =  xy

where  y  is  nonempty,  we  write  a? =  wy~
1.

L e m m a  A2 :  Let  0  be  a  real  number  between  0  and  1  such  that  ^  is  a  convergent  of  the

continued  fraction  expansion  of  0.  Let  z  be  a  palindrome  such  that  u  =  Ozl.

(a)  (see  [1,3,21])  z  is  a  prefix  of  / ( 0 ) .

(b)  If  |  >  0,  then  w l _ 1  (resp.,  u)  is  a  prefix  of  0/(0)  (resp.,  1/(0)),  but  «  is  not  a  prefix  of

0/(0).
(c)  If
  £  <  0,  then  ?i  (resp.,  « 0 _ 1 )  is  a  prefix  of  0/(0)  (resp.,  1/(0)),  but  w is  not  a  prefix  of
i/(V
(d) 0/(§)=«~

Proof:  Part  (b)  and  (c)  follow  from  (a)  and  the  fact  that  [(q — 1)0] =  p — 1, [(q +1)0]  =  p,

and
 P  ( * < * ) .

Part  (d)  follows  from  (b).  •

The  following  lemma  follows  from  Lemmas  A l  and  A2.

2003]  205

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

L e m m a  A 3 :  The  first  (resp.,  last)  letter  of  u  is  0  (resp.,  1).  For  1 <  k  <  g,

the  k
th  letter  of  u  is  1

< = » * - !  =  hq

P  for  some  1 <  h  < p  —  1.

L e m m a  A4:  For  each  h  with  1  <  h  <  p,  there  is  a  unique  r  with  1  <  r  <  p  such  that

^  =  rs  —  1  (mod  g).  The  mapping  h  \—>  r  is  a  bijection  from  { 1 , 2 , . . . ,p}  onto  itself.

Furthermore,

(a)  h  =  rt  and  r  =  h(p  — rn)  (mod  p),  where  1 <  m  < p,  and  q =  m  (mod  p).

(b)  /i =  p  <=> r  =  p.

P roof:  Let  1  <  h  <  p.  Since  s  and  q  are  relatively  prime,  there  is  a  unique  integer  r,

1  <  r  <  <Z  such  that
 hq

P  =  rs  —  I  (mod  g).

Clearly  (b)  holds.  Let  n  be  an  integer  such  that  ^  =  rs  —  1 — ng.  Then

p .  =  rps  — p — nqp

=  r(qt  + 1) — p — nqp

— q(
rt  —
 np)  + r — p.

Since p  M  <  hq  < p  f ^ l  +  p,  we  have

T  p  V
(rt  — np)  -\  <  h  <rt  — np+  -,
Q  Q  Q

that  is,  r  p
h + np  — rt<  -  <  h-hnp  —  rt-\—.
q  q

Therefore  h  +  np  —  rt=  H  = 0  and  r  -  p  <  q(h  +  np  -  rt)  =  0;  so  h  =  rt  (mod  p)  and

1  <  T < p.  The  second  part  of  (a)  follows  immediately  from  the  first  part.

206  [JUNE-JULY

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

It  remains  to  show  that  if  1 <  /n  <  h2  < p,  then  f ^ l  =£ [ ^ 1  (mod  q).  Let  k  =  h2-h1,
where  1 <  h± <  h2  < p,  i.e.,  1 <  k  < p  —  1.  Then

hiq  +  K  htq  +  kl  <  htq  kg  =  fe2g

^  ftia  »—  1  ftia
<  —  +  g  <  —  +  g -  1
p  p  p

<  hiq  + g;

so  the  result  follows.  •

Lemma  2.1  now  follows  immediately  from  Lemmas  A3  and  A4.

A C K N O W L E D G M E N T

The  author  wishes  to  express  her  gratitude  to  the  anonymous  referee  for  valuable  com-

ments  and  suggestions  which  improved  the  presentation  of  this  paper.  This  research  was

supported  in  part  by  Grant  NSC  89-2115-M-033-016,  the  National  Science  Council,  Republic

of  China.
 R E F E R E N C E S

[1]  J.  Berstel  and  A.  de  Luca.  "Sturmian  Words,  Lyndon  Words  and  Trees."  Theoret.
Comput  Sci.  178  (1997):  171-203.
[2]  J.P.  Borel  and  F.  Laubie.  "Quelques  Mots  sur  la  Droite  Projective  Reelle."  Journal  de
Theorie  des  Nombres  de  Bordeaux  5  (1993):  23-51.
[3]  T.C.  Brown.  "Descriptions  of  the  Characteristic  Sequence  of  an  Irrational."  Canad.
Math.  Bull  36  (1993):  15-21.
[4]  T.C.  Brown  and  A.R.  Preedman.  "Some  Sequences  Associated  with  the  Golden  Ratio."
The  Fibonacci  Quarterly  29.2  (1991):  157-159.
[5]  T.C.  Brown  and  P.  J-S.  Shiue.  "Sums  of  Fractional  Parts  of  Integer  Multiples  of  an
Irrational."  Journal  of  Number  Theory  50  (1995):  181-192.
[6]  W.  Chuan.  "Fibonacci  Words."  The  Fibonacci  Quarterly  30*1  (1992):  68-76.
[7]  W.  Chuan.  "Symmetric  Fibonacci  Words."  The  Fibonacci  Quarterly  31.3  (1993):  251-
255.
[8]  W.  Chuan.  "Embedding  Fibonacci  Words  into  Fibonacci  Word  Patterns."  Applications
of  Fibonacci  Numbers  5:  113-122.  Ed.  G.E.  Bergum,  et.  al.  Dordrecht:  Kluwer,  1993.
[9]  W.  Chuan.  "Extraction  Property  of the  Golden  Sequence."  The  Fibonacci  Quarterly  33.2
(1995):  113-122.
[10]  W.  Chuan.  "Generating  Fibonacci  Words."  The  Fibonacci  Quarterly  33.2  (1995):  104-
112.

2003]  207

CHARACTERIZATIONS  OF  a-WORDS,  MOMENTS,  AND  DETERMINANTS

[11]  W.  Oman.  Report  of the  National  Science  Council  Research  Project  NSC  84-2121-M033-
007,  1995.
[12]  W.  Chuan.  "Subwords  of  the  Golden  Sequence  and  the  Fibonacci  Words."  Applications
of  Fibonacci  Numbers  6:  73-84.  Ed.  G.E.  Bergum  et.  al.  Dordrecht:  Kluwer,  1996.
[13]  W.  Chuan.  "a-Words  and  Factors  of  Characteristic  Sequences."  Discrete  Math  177
(1997):  33-50.
[14]  W.  Chuan.  "Unbordered  Factors  of  the  Characteristic  Sequences  of  Irrational  Numbers."
Theoret  Comput.  Sci  205  (1998):  337-344.
[15]  W.  Chuan.  "A  Representation  Theorem  of  the  Suffixes  of  Characteristic  Sequences."
Discrete  Applied  Math.  85  (1998):  47-57.
[16]  W.  Chuan.  "Sturmian  Morphisms  and  a-Words."  Theoret.  Comput.  Sci.  225  (1999):
129-148.
[17]  W.  Chuan.  "Suffixes  of Fibonacci  Word  Patterns."  The  Fibonacci  Quarterly  38-4  (2000):
432-439.
[18]  W.  Chuan.  Report  of  the  National  Science  Council  Research  Project  NSC  89-2115-M-
033-005,  2000.
[19]  P.J.  Davis.  Circulant  Matrices.  John  Wiley  and  Sons,  New  York,  1979.
[20]  A.  de  Luca  and  F.  Mignosi.  "Some  Combinatorial  Properties  of  Sturmian  Words."  The-
oret.  Comput.  Sci.  136  (1994):  361-385.
[21]  A.S.  Fraenkel,  M.  Mushkin  and  U.  Tassa.  "Determination  of  [n0] by  Its  Sequences  of
Differences."  Canad.  Math.  Bull  21  (1978):  441-446.
[22]  M.  Lothaire.  Combinatorics  on  Words.  Addison-Wesley,  Reading,  MA,  1983.
[23]  M. Morse  and  Hedlund.  "Symbolic  Dynamics  II: Sturmian  Trajectories."  Amer.  J.  Math.
62  (1940):  1-42.
[24]  K.  Tognetti,  G.  Winley,  and  T.  van  Ravenstein.  "The  Fibonacci  Tree,  Hofstadter  and  the
Golden  String."  Applications  of  Fibonacci  Numbers  3:  325-334.  Ed.  G.E.  Bergum  et.  al.
Dordrecht:  Kluwer,  1990.
[25]  J.C.  Turner.  "Fibonacci  Word  Patterns  and  Binary  Sequences."  The  Fibonacci  Quarterly
26.3  (1988):  233-246.

AMS  Classification  Numbers:  11B83,  68R15

*  • &  ^

208  [JUNE-JULY
