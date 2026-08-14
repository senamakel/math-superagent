<!-- source: https://www.fq.math.ca/Scanned/30-1/chuan.pdf | converted from PDF -->

FIBONACCI  WORDS

W ai-fong  C h u a n
Chung-Yuan  Christian University, Chungli, Taiwan  32023, Republic of China
(Submitted  March 1990)

1.  Introduction

In this paper, the notion of Fibonacci word is introduced and the structure
of these words is investigated.

Let s$ be a nonempty  set and let x and y be two words in the alphabet^.  A
Fibonacci  sequence  of  words  derived from  x and  y is a sequence of words  W\9 W 29
W^y  . . .  with the property  that

wl  =  x,  w2 =  y,  wn+i  =  wnwn-i  or  wn.lwn.
The pair  x and y are called  the  initial  words  of  the Fibonacci  sequence of
words; the words  wnwn-\  and  wn-\W n  are  called  the  immediate  successors  of  wn
and  wn  is their  immediate  predecessor.  We remark  that  the Fibonacci  sequence
of words considered by Knuth  [3, p. 85] is the one obtained as above by letting

wn+i  =  wnwn„i  for all  n  > 3

and the one considered by Higgins  [1] and Turner  [4, 5] is obtained by letting

wn+i  = wn-iW n  for all n  >  3.

Let  SP be  the set of all such  sequences  of words  derived  from  x and y; let
^n  be the collec tion of words  which  happen  to be the n t h term of some members
of 5^  For example,

^i  =  {#}>  SP2 =  ty^>  -^3 =  ^yx>  xy}>  ^  =  iyxy*  yyx>  xyy}-

Denote the union of 5 ^  (n  -  1, 2,  ...) by y .  Members  of  SPn (resp.  £f)  are
called  the  nth  Fibonacci  words  (resp.  Fibonacci  words).  Note  that each word
has an obvious representation in terms of x and y  .  Throughout  this  paper, we
consider only such a representation.

Lemma  1:  Let W be a Fibonacci word.  Then the following  statements are true.

(i)  If w starts  (resp. ends) with an x9  then  w cannot end (resp. start) with
an  x.
(ii)  If  w starts  (resp.  ends) with a  y9  then  w cannot end (resp. start) with
a  yy.
(iii)  There  cannot  be three  or more  consecutive  occurrences  of  y  and there
cannot be two or more consecutive  occurrences of x in w.

Proof:  The result is proved by mathematical  induction.

Let  £/*n(x,  •) [resp. «5^(«,  y) ] denote  those  nth  Fibonacci  words  which  start
with an x  (resp. end with a  y)  and let

^n(x,  y)  = S?n(x,  •) n y n(.,  y).

Define  ^(x9  • ) ,  S^{ •,  y) , etc., in a similar way.

Corollary  2:

SPn = .££(*, z/) u yn(z/,  y)  u 5^(2/, a?)  for all n;

9> = SS(X,  y) U  y(y,  y) U  #>(y,  x)  .

Using finite binary sequences, let us label the Fibonacci words as follows:

68  [Feb.

FIBONACCI WORDS

(1.1)  wY = x  w2

and, in general, we have
 yx

1  /  *
w3  =  xy<\  n

<

<
l

»i°

<
 =  yxy

=  yyx

=  xyy

=  yxy

(1.2)  ^ • " ' - ^  J  " + 1
( w^2-.- n- 2 w
ri
r2-"'»-i  if rn - 1

where n > 4, P^, P 2 3  •••>  ^ - l € t ° '  ! } •
  W e  sometimes write 7j^lP2" '
Pn~
2  (x,  y)  to
indicate the initial words.  For simplicity we write  w®n (resp.  w\)  if  n  > 3 and
p 1 ~ p 2 = " " '
 =  rn-2  = 0 (resp. 1 ) . We sometimes write UY and it?2 for  W-, and u 2 ,
respectively.  Note that

(i)  the superscript PiP2-oaPn-2  indicates how the Fibonacci word  Wnl  z'"  n~2

is obtained  frpm  x  and  y;

(ii)  the Fibonacci word z^.^  '
 n"  is always  an immediate  predecessor  of the

Fibonacci word  w + o  " " '

(iii)  the same Fibonacci word may have several different labels;

(iv)  Knuth's Fibonacci sequence of words is  {w^}  while  Higginsf  and Turnerfs

is  wl9  w2,  w\,  ..., w^9 . . . .

Define  the reverse  operation  R  by setting  R(XiX2'  - -xm^  =  xm • -  *%ix\  ->  where
Xi>  . ..,  xm  e  {x,  y}.  A word  w =  Xix2..  «xm is said to be  symmetric  if R(w) = w.
For example, the words  yxy  and  xyyx  are  symmetric.

Theorem  3:

(i)  If w e y n, then  R(w) e ^ .  Moreover, if n > 3 and TJ =  W* lTl''  'rn~2  where

the p fs are 0 or 1, then  R(w)  =  WSnlS2"°Sn~2  where  s^  = 1 -  v^ ,  j  = 1, 2,

..., n - 2.

(ii)  If  V is an immediate  predecessor  of u, then i?(i>) is an immediate prede-

cessor of  R(w).

Proof:  Suppose that the results are true for all positive  integers less than n.
Let  w =  w^
lT2'-'
Tn-
1  where P 1 S P 2 , •••> ^ - 2 e ^ ° »  ^  •
  I f  pn-2 =  ° >  t h e n  W  =  vu
where  V = ^^l^'-^n-a  e  y  is an immediate predecessor of w
.  n-\  n-1
and
 u =  Wn^z""
  M_Lf e ^n-2 i s  a n  immediate predecessor of y.

Clearly i?(w) =  R(u)R(v).  By the induction hypothesis,

-2

is an immediate predecessor of

where s • = 1 - p •, j = 1, 2, ..., n - 3.  Hence,  R (v)  is an  immediate  prede-
cessor of  R(w) and

R(u)  = ^i a 2 2-" f l^  e y n_ 2

1992]  69

FIBONACCI WORDS

R{w)  = R{u)R{v)  =  w°nil*-••*«-•>  ww-°«-3

where sn_2 = 1.  The case rn_2 = 1 is proved similarly.

2.  Factorization of w£ into a Product of Symmetric Factors

Let i>5 =  y,  u5  =  xyyx,  yg =  yxy,  wg =  yxyxy•  For n S 7,  put

where  cn  equals  xy  if n is even and equals  yx if  n is odd.  We sometimes write
un(x9  y)  and  Vn(x,  y)  for u n and  vn,  respectively.  Plainly, all  un}' s and y„'s
are symmetric.

Theorem  4: For n > 5, we have

(i)  wO =  Vnun;  (ii)  ^„cn_1 = ZJO^;
(iii)  wn = c?n_1^.2;  (iv) tfl = Mni>n-
Proof:  Clearly the results are true for n  -  5 and 6.  Suppose  n  >  6 and that
the results hold for all integers less than  n.  Then

y „ C n - !  =  yn-2 Mn-2 yrc-2 Cn-l
  =  W n - 2 U n - 3  = "5-15
"n =  R(cn)(vn_lCn)  =  en_xw°_2;

This  proves  (i)-(iii).  Assertion  (iv) is a consequence of Theorem 3 and the
fact that  un  and  Vn are symmetric.

Let  w be a word in the alphabet^.  Designate the length of w by  / (w) .  In
the following lemma we compute the length of the words  w„9  un,  and  Vn.

Lemma  5:  For n  > 3, we have

(i)  /(*>0) = /(^.i) + /(w° _2);  n _ 2
(ii)  /(^) = Fn_2l(x)  + Fn_1l(y)  = £  /(^?(x, z/)) + /Q/).

For n > 5, we have

(iii)  /(wn(a;, 2/)) =  l(w°n_2)  + /(ar) +  Uy)  = (^n_4  + l)/(a?) +  (Fn_3  + l)/(z/);

(iv)  l(vn(x,  y))  = /(^_x) - /Or) - /(y) = (Fn„3 -  l)l(x)  + (Fn_2 -  l)l(y).
Proof:  Both (i) and (ii) are proved by induction on  n and  both  (iii) and (iv)
follow from (i) , (ii), and Theorem 4.

3.  Cyclic Shift on Fibonacci Words

In this section, our main result states that every  nth  Fibonacci word is a
cyclic shift of every other n th Fibonacci  word.  A  cyclic  shift  operation  Tn
acting on words in the alphabet si that have lengths  n is given by

Tn(clc2...cn)  =  c2c3...cncl9
where  c^>  c2,  ..., cn  e  si.

Theorem  6:  Every Fibonacci word in ^  is a cyclic shift of  w„.  More precise-
ly, for n  > 3, we have

70  [Feb.

FIBONACCI WORDS

7(w° )

k =  nL 2/(w9 + 1)^  ^ { F . ^ K x )  +Fj6(y))rj.
i =
  l  j = i

Proof:  The result is trivial for n = 3.  Suppose  that  n  > 3  and  the result  is
true for all integers less than  n and greater  than or equal to 3.

r x  =  0:

^n  ( a ,  y)  =  w „ l i  2 ( # ,  2/#)

=  T^iw^.^y,  yx))  =  T*(w°(a;,  y))
where  n - 2  n - 2  n _  2
&1  =  Z  /(w ?(j/,  2/tf))r.  =  Z / ( w 7 0 + 1 O r ,  2/))*V  =  £  / W + i ( * >  2/))*V  =  &•
J = 2
  J  J  j = 2  J  J  j=l  J + i  J

Px  = 1:

(3.D  ^ - ' - M * ,  y) = w„r13-r-2(j/, ^ )

where
 &1 = "]£  Krf.(y,  xy))r.  = ^  /(w)° y-
0(a, j/))*,- = £  A ^ + i G n ,  j/))^.
J = 2  j = 2  J = 2

By Theorem 4 and (iv) of Lemma 5, we have

w\{x>  y)  =  un(x,  y)vn(x,  y)  =  Tl(Vn)(w°n(x,  y))

•x  -  ±-z  -  •  •  •  =  r n _ 2

w\{x,  y)  =  TkHwl°---°(x,  y)),
where  n-  2
k2  = Z  l(Wj+i(x>  2/))>
J'=2
so that
 wio-••<>(*, ^) = T k 3 ( ^ ( x 5  y))s
where

(3.2)  fe3  =  -k2  +  l(w^_l(x9  y))  -  l(x)  -  Uy)

=  ^IlkwHx,  y))  =  -l(w°(x,  y))  +  l{y)

= -/(w° (a:, z/)) + / ( ^ U ,  2/)),

in  view  of  (ii) of  Lemma  5.  Combining  (3.1) and  (3.2),  we have  the desired
result.

In the case that  x and  y  are distinct  alphabets, it turns  out that 5^ con-
sists of all the cyclic  shifts of  w^.

Theorem  7:  Let  x  and  y be  distinct  alphabets  a  and  bs  respectively.  Then a
word  W in the alphabet  {a5 M  is an n t h Fibonacci  word  if and  only  if W  is a
cyclic  shift of w j .

Proof:  The "only if" part is contained  in Theorem 6.  The "if" part is a conse-
quence of the following Lemma  (about Fibonacci numbers) whose proof is easy and
is therefore  omitted.

1992]  71

FIBONACCI WORDS

Lemma  8:  Let  n  > 3.  For all 0 <  v  <  Fn  -  1, the equation

n-  2

j  =  i
has at least one solution p ^  P 2, ..., P n _ 2 in {0,  1}.

We  remark  that  this  lemma  also  leads  to the known  representation  theorem
which  states  that  every  positive  integer  can be  represented  as  a  sum  of a
finite  number  of  Fibonacci  numbers  in which  each  Fibonacci  number  occurs at
most once.
 4.  T h e Case  x  and y Are Alphabets

As  in the last  theorem  of  Section  3, let  x  and  y  be distinct  alphabets  a
and  b,  respectively.  Let  qn  = u^0101'*"  (n  -  1, 2,  . . . ) .  In this section, we
locate the a Ts in  qn  and show that all the shifts of  qn  (resp.  w%) are distinct
and hence  that 5^ consists of precisely  Fn  Fibonacci words.  The main result is
based on the following  two lemmas.

Lemma  9:  Let  n  > 3.  Then  jFn_i  (resp.  jFn.2),  0 <  j  <  Fn  -  1, is a  complete
residue system modulo  Fn.

Lemma  10:  (a)  Let  n be an odd integer  greater  than 4.

(i)  For 1 <  j  <  Fn_L±,  let  k be the unique number  such that

(4.1)  1 <  k  <  Fn_2  and  jFn-3  E  k  (mod  Fn.2).

Then there exists a unique  r-  such that

(4.2)  1 <  r^  <  Fn_2  and  k  =  rjFn.l  (mod  Fn)  .

( i i )  F o r  1  <  i  <  F w _ 3 ,  l e t  fc  b e  t h e  u n i q u e  number  s u c h  t h a t

( 4 . 3 )  Fn.2  +  1  <  k  <  Fn  and  iFn.3  =  fc  -  Fn.2  (mod  i ^ _ i ) .

Then  t h e r e  e x i s t s  a  u n i q u e  t±  s u c h  t h a t

( 4 . 4 )  1  <  t i  <  Fn.2  a n d  k  =  tiFn_1  (mod  F n ) .

F u r t h e r m o r e ,

( 4 . 5 )  {r-  :  1  <  j  <  Fn.h}  u  {tt  :  1  <  i  <  F n _ 3 }  =  { 1 ,  2 ,  . . . ,  Fn„2}.

(b)  Let n be an even integer greater  than 4.

(iii)  For 1 < j <  Fn-.3,  let  k be the unique number such that

1 <  k  <  Fn_l  and  jFn.2  =  k  (mod  Fn-i)  .

Then there exists a unique Pj such that

I  <  v.  <  Fn.2  and fe E 1 ^ - 2  (mod F„) .

(iv)  For 1 <  i,  <  Fn-.i+,  let  k be the unique number  such that

Fn_l  + 1 <  k  <  Fn  and  iFn_h  =  k  -  Fn.1  (mod  Fn_2)  .

Then there exists a unique  £^ such that

1 <  t t  <  Fn_2  and  k  =  t-iFn-2  (mod  Fn)  .

Furthermore,

{p^ : 1 < j < ^ . 3 } u { ^ : 1 <  i  <  Fn_h]  = {1, 2, ...,  Fn_2}.

Proof:  We prove  (a) only.

(i)  Let j and  k  satisfy condition  (4.1).  We show that  (4.2) holds.  Write

k  =  jFn_3  "  sF-n-2  where  s  is an inteeer.
72  [Feb.

FIBONACCI WORDS

Since  -Fn_2  <  -k  <  jFn_3  -  k  =  sFn_2  < jF„_3  -  1 < F„_iA-3  "  1 =  Fn-5
Fn-2>

we see that 0 <  s  <  Fn„5,  Thus5

k  =  jFn_3  -  sFn_2  =  (2j +  s)Fn.l  -  (j +  s)Fn  = pFn_x  (mod  Fn)  ,

where  1 < r = 2j + s < 2JP„_i+ +  Fn_5  =  Fn_2.  This proves  (4.2).

(ii)  Let  i  and  k  satisfy condition  (4.3).  We show that  (4.4) holds.  Write

(4.6)  k  =  iFn.3  +  Fn_2  -  SjPn_!  =  (2i -  s  -  D ^ - i  "  (i -  D ^

E tFn_! (mod F n ) ,

where  s is an integer  and  t  -  2i -  s  -  1.  From  (4.6), we have

Fn__2  +  1  <  k  <  tFn_l  =  fc  +  ( i  -  1)F„  <  i^n  +  ( i  -  1)F„

=  £FW  <  Fn-?~Fn  =  Fn-iFn_2  -  1  <  F n „ 1 F n _ 2 ,

so  t h a t :  1  <  t  <  Fn_2.  T h i s  p r o v e s  ( 4 . 4 ) .
Now  we  p r o v e  ( 4 . 5 ) .  I t  i s  c l e a r  t h a t  t h e  s e t s

A  =  {v-  :  1  <  j  <  F n_ i +}  and  5  =  {tt  :  1  <  i  <  Fn_3}

a r e  c o n t a i n e d  i n  { 1 ,  2 ,  .  . . ,  F n _ 2 } .  To  p r o v e  e q u a l i t y  i n  ( 4 . 5 ) ,  we  show  t h a t  A
h a s  Fn^ht  e l e m e n t s ,  B  h a s  Fn„3  e l e m e n t s ,  and  t h a t  A  and  B  are  d i s j o i n t .

(a)  I f  rj  =  Tj  ,  where  j - ^  and  j 2  l i e  b e t w e e n  1  and  Fn-i+9  t h e n

kdl  E  rJiFn.l  =  rJ2Fn.l  E  k J 2  (mod  Fn)  .

S i n c e  b o t h  kjx  and  kj2  l i e  b e t w e e n  1  and  F n _ 2 )  t h i s  i m p l i e s  t h a t  kjY  =  kj2  and
so
 Jl
Fn-S
  E  Jl
Fn-3  ( m o d  ^n-2>  •

Since  Fn-2  and i^-3  are relatively prime, we have  j \  =• J2.  Hence, all  the  rfs
are distinct.

(b)  A similar proof  shows that all the  V s are distinct.

(c)  If  Vj  €  Ay  t i  e  B9  and  r^  = t^ , then  k  =  k
r  (mod Fn) , where  VjFn-\  =  k
and  tj,Fn^i  =  k
r  (mod  Fn) , and  both fc and fc
f lie  between  1 and  Fn .  Therefore,
we have  k  =  k
r.  But this is impossible because fc ^ ^n-2 +  1 > ^f-  Thus, 4 and
B are disjoint.

This proves  (4.5), and  the proof  is complete.

In part  (a) of Lemma  10, two injective mappings

r:  j  e  {1, 2,  ...,  Fn_h]  ^  2- e {1, 2,  .. .,  Fn_2}

t : i e  {1, 2,  ...,  Fn.3]  ^  t i  e {1, 2,  ...,  Fn_2}

are  defined  by  (4.1)  and  (4.2) and by  (4.3) and  (4.4), respectively.  The dis-
joint  union  of  their  ranges  gives the whole of  {1, 2, ..., F n _ 2 }.  Part  (b) of
Lemma  10 has an analogous meaning.
Now write  qn  =  ala2>  .  .aF  where  a^  e {a,  M .

Theorem  11:  Let  n be  a  positive  integer  greater  than 3.  Let  t  =  Fn„i  if  n  is
odd and  t = ^ - 2  if n is even.  Then  ak  =  a  if  and  only  if  k  =  jt  (mod  Fn)  for
some  1 < j <  Fn..2.

Proof:  The results are clearly  true for  n  < 7.  Now suppose  that  n  >  1 and n is
odd.  Then qn  =  qn_2qn_l  where

qn_2  =  ala2...aFn_2  and  9 n - 1  = a^_2 +  1 . . . a ^ .

1992]  73

FIBONACCI  WORDS

By  t h e  i n d u c t i o n  h y p o t h e s i s ,  t h e  f o l l o w i n g  s t a t e m e n t s  a r e  t r u e :

( i )  For  1  <  k  <  Fn-2>
  w e  h a v e

ak  =  a  i f  and  o n l y  i f  k  E  j T n _ 3  (mod  F n.-2)  f ° r  s o m e  1  -  J  -  Fn-i+.

( i i )  For  F n _ 2  +  1  <  k  <  Fn  ,  we  h a v e

ak  = a if and only  If  k  -  Fn~2  -  J^n-3  (mod i^-i)  for some  1 < j <  Fn-$.

The result now follows from Lemmas  9 and  10.  For even  n  the proof  is similar.

Let  w  =  c-yC1.'*cn  where  Cj  equals  a  or  b.  We  designate  by  S(w)  the  sum
(mod  ri)  of the indices j for which  Cj  - a .

Corollary  12:  Let  n  be a positive  integer greater  than 2.  For odd  n9  let

s =  Fn _ 2  and  £ = Fn _ i;

for even n, let

s = Fn_i  and  t  =  Fn-2-

Suppose that  1 <  j  <  Fn  -  1 and  TJsqn  = ^ ^ . . . ( ^  where  c^  <E {a  Z? } and  T  =
T F  .  Then

(i)  ck  = a if and only  if fc E (j +  r)t  (mod F w)  for some  1 < r < Fn_2-

(ii)  S(T*
8qn)  -  S{T^~
l)sqn)  E 1 (mod F„),  and  S(T*
8qn)  =  S(qn)  +  j  (mod F„).

(iii)  ^J s^7n  (0 <  j  <  Fn  -  1) are Fn  distinct  shifts of  qn.

(iv)  T J^ n  (0 <  j  <  Fn  -  1) are  Fn  distinct shifts of  qn.

Proof:
(i)  By Theorem  11, we have

ck  =  a  **•  k +  js  E  vt  (mod  Fn)  for some  1 <  r  <  Fn_2
**  k  E (j + p)t  (mod F„) for some  1 <  r  <  Fn_2-

Fn-2  Fn-2
(ii)  S(T
Jsqn)  -  S{T^~
l)sqn)  =  £  (j +  r)t  -  £  U  + * ~  D *
p = l  r = l
E F n_ 2t E 1 (mod  Fn).

Statement  (iii) follows from  (ii); statement  (iv) is a consequence  of  (iii) and
Lemma 9.

Corollary  13:  Let  n,  s,  and  t  be the same as in Corollary 12.

(i)  If 0 < j <  Fn_2  ~  1>  then T J s ^ n  starts with an a.

(ii)  If  Fn_2  ^ J ^ 2F n_ 2  -  1, then  TJ'sqn  starts with a  ba.

(iii)  If 2F„_2  <  j  <  Fn  -  1,  then T*
7'
3^ starts with a  bba.

(iv)  If FM_2  < J < F„_i  - 1, then  TJsq  starts with a  b  and ends with a 2?.

Proof:  Write T ' 7 ^  = ^i^2-*-^„  where  ck  e  {a,  b].  We  shall  use  Lemma  1,  (i)
of Corollary  12, and  the fact that  i  E  iFn_2~k  (mod  Fn)  where  i  = 1, 2, and 3.

(i)  If 0 <  Q  <  Fn_2  ~  If  then cx  =  a  because j +  1 <  Fn_2  < J +  Fn_2-

(ii)  If F„_ 2  ^  j  ^  2Fn_z  ~  1J then the  inequalities

J +  1 <  2Fn_z  <  3  +  K-z

imply that  o2  =  a  and hence  e\  =  b,  according  to Lemma 1.

(iii)  If  2Fn_2  ^ J  <  Fn  -  I,  then the  inequalities

74  [Feb.

FIBONACCI WORDS

j +  1 <  Fn  <  3Fn_2  <  j  +  Fn_2

imply  that c 3  =  a  and  cF  =  a;  hence  c\  =  c2  =  b.

(iv)  If  Fn_2  < J <  Fn_l  -  1, then  cx  =  b,  by  (ii) , and since

Fn  -  1 E  -Fn.zt  E F n - 1 t  and J +  1 < Fn _ x  < 2Fn_2 < j +  F n_ 2,

we have £o _•. = a, so that c P  =  b.

Theorem  14:  Let ft be a positive  integer.  Then

L%| = ^ ;  |S^(a, fc)| = Fn_2 = |yn(6, a) |;

|yn(i, 6)| = ^n-3;  l^n(^  - ) | =  \^n(°,  b)\  =  Fn^.

Proof:  The results follow from Theorem  7 and Corollaries  12 and 13.

5.  T w o  Algorithms

In this section, the initial words are again taken to be alphabets  a  and  b.
Two  algorithms  will  be  given.  Algorithm  A  constructs  the  Fibonacci  word  for
which  the multiplications  involved  are  preassigned  by means of a finite binary
sequence  as  in  (3.1) and  (3.2).  Algorithm B tests whether  a given word  in the
alphabet:  a  and  b  is a» Fibonacci word  or not.
For  simplicity,  we  replace  a  by  1 and  b  by  0  in both  algorithms  so  that
Fibonacci words are represented by binary sequences.
Since

where  n-  2

and  ^ ~ 1

(T
Fn  ~\w^)  if  n  is odd

{T*
n~
l  L  (w®)  if  n  is even,

it follows  that  w =  TJ'sqn  where
{

Fn_2  if ft is odd

Fn„i  if n is even,
i
kFn-l  if ft is odd

(mod  F n)
kFn_i  -  1  if ft is even,
and fc = fei +  1.  Thus,  the  positions  of the  1
f s in  w can be determined by Cor-
ollary 12.
Algorithm  A:  Input  a  positive  integer ft and  a  binary  sequence  2^, r 2 ,
p  0.  This algorithm  constructs  the Fibonacci word  w
n - Z  °
 !
 Fn_x  if ft is odd  w - 2

Fn_2  if ft is even,  '
z-
=1

and j  satisfying  if ft is odd
(mod  Fn)  if ft is even,

1992]  75

FIBONACCI  WORDS

2)  For  r  = 1, 2, ...,  Fn„z,  let  cm  =  1 if  m  = (J +  r)  t  (mod F w)  and  1  <  m
<  Fn;  let <?m = 0 otherwise.
3)  w =  cx,  c2,  . . . , ^  .

We  now_ turn  to  the  identification of Fibonacci words.  First, observe  that
n  =  [(ln(/5(Fn  +  l/2)))/ln(a)], where a =  (1 +  /5)/2.

Algorithm  B:  Input a positive  integer  In and a binary  sequence  w  =  C\>  c2,  • ••>
c?^ .  This algorithm  tests whether  or not  w is a Fibonacci word.

1)  Let  n  =  [(ln(/5(fe + 1/2)))/ln(a)].
2)  If  h  *  Fn,  then  w  £  Sf.
3)  If  h = F„, let

f^n-l  if
 n  i s ° dd
(Fn_2  if
 n  i s even.

4)  Compute  the sum  S  of all indices  i  such that  c^  -  1 and  count  the  num-
ber /?? of  1
? s in  w,
5)  If  m  *  Fn-2>
  t h e n  ^  $  Sf.
6)  If /7? =  Fn„2,  let j be such that  1 <  j  <  Fn  and

J  =  S  -  Fn_2(Fn_2  + l)t/2 (mod  Fn).

7)  For p = 1, 2, . ..,  F n_ 2,  let  k  be such that  1 <  k  <  Fn  and  k  = (j + r)£
(mod ^„) .  If  ck  *  1 for some p, then ZJ ^  9
J;  otherwise  w e i^.

Note  that in step  6, j  E ^(U) -  S(q  )  (mod F w)  and so either

!
 F„_o  if n is odd  , 1 z  (the latter case

TP  .<:  .  in step  7)
i^n _ ]_  if  n  is even,
or  u ^ ^  (the former case in step 7 ) .
Acknowledgment

The author gratefully acknowledges  that this research was supported  in part
by the National  Science Council Grant NSC800208M033Q2.

References

1.  P.  M.  Higgins.  "The  Naming  of  Popes  and  a  Fibonacci  Sequence  in  Two  Non-
commuting  Indeterminates .
ff  Fibonacci,  Quarterly  25.1  (1987) : 57-61.
2.  V.  E. Hoggatt, Jr.  Fibonacci  and  Lucas  Numbers.  New York: Houghton Mifflin
Company, 1969.
3.  D.  E.  Knuth.  The  Art  of  Computer  Programming.  Vol. -I. New  York:  Addison-
Wesley, 1973.
4.  J.  C.  Turner.  "Fibonacci  Word  Patterns  and  Binary  Sequences."  Fibonacci
Quarterly  26.  3 (1988):233-46.
5.  J.  C.  Turner.  "The  Alpha  and  the  Omega  of  the  Wythoff  Pairs."  Fibonacci
Quarterly  27.1 (1989):76-86.

76  [Feb.
