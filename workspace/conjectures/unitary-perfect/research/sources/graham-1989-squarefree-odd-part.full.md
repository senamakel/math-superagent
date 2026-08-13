<!-- source: https://www.fq.math.ca/Scanned/27-4/graham.pdf | converted from PDF -->

UNITARY  PERFECT  NUMBERS  WITH  SQUAREFREE  ODD  PART

S.  W.  GRAHAM

Michigan Technological University, Houghton, MI 49931

(Submitted July 1987)

1 a  Introduction

A divisor  d of a natural number  n is said to be unitary  if and only if

(d,  n/d)  = 1.

The sum of the unitary divisors of n is denoted  o*(n).  It is straightforward
to show that if

n  =  pl
lp2
z  ...  pkk  ,

then
 a*(n) = (p*i + l)(p*
2 + 1) •••  (p£k + D -

A natural number  n is said to be unitary  perfect  if a*(n) = 2n.
Subbarao and Warren  [2] discovered the first four unitary perfect numbers:

6 =  2 - 3 , 60 = 2 2 • 3 • 5, 90 = 2 • 3 2 • 5, 87360 = 2 6 • 3 • 5 • 7 • 13.

Wall  [3] discovered another such number,

46361946186458562560000 = 2 1 8 • 3 • 5 4 • 7 • 11 - 13 • 19 • 37 • 79 • 109 - 157 • 313,

and  he later  showed  [4] that  this  is the fifth  unitary  perfect  number.  No
other unitary  perfect numbers are known, and Wall  [5] has shown that any other
such number must have an odd prime divisor exceeding 2 1 5 .
In this paper, we consider  the existence of unitary perfect numbers of the
form  2ms, where  s is a squarefree  odd integer.  We shall prove  that  there are
only three such numbers.

Theorem:  If 2ms is a unitary  perfect  number and s  is squarefree, then either
m  -  \  and  s  = 3,  m = 2 and  s = 3 • 5, or  m = 6 and  s = 3 • 5 • 7 s 13.

2.  Preliminaries

Throughout this paper, the  letter  s shall be used to denote an odd square-
free  number.  The letter p, with or without a subscript, shall denote an odd
prime.  The letter  q,  with  or without  a subscript,  shall  denote  a Mersenne
prime.
Our  starting  point is the observation that, for any fixed  m, it is easy to
determine  all unitary  perfect  numbers  of the form  2ms.  From the previously
stated formula for  o\n),  we see  that if s  = pYp2  - - -  P r > then  2ms  is unitary
perfect if and only if

_  a*(2
ms)_2
m  + 1  P X + 1  P 2 + 2  pr  + 1

2
ms  2m  °  pl  *  p 2  pr  '  ( }

Any odd prime dividing 2 m + l must appear as a denominator on the right-hand side.
If p is such a prime,  then all odd prime divisors of p + 1 must also appear as

1989]  317

UNITARY PERFECT NUMBERS WITH SQUAREFREE ODD PART

denominators  on  the right-hand  side.  If we  can  force  a prime  to appear more
than once, then we  can conclude that there is no unitary perfect number of the
form  2
ms.
For  example, suppose  m  =  1.  Since 2 7 + l = 3° 43, 3 and 43 must appear as
denominators  on  the right-hand  side  of  (1).  Since  ll|(43 +  1), 11 must  also
appear.  But  3 | (11  +  1), so  3  must  appear  twice.  Therefore,  there  is  no
unitary perfect number of the form 27s.
On the other hand, suppose  m = 6.  Since 2 6 + 1 = 5 • 13, both 5 and 13 must
be prime divisors of  s.  Since 3|(5 + 1) and 7|(13 +  1),  7 and 13 must be prime
divisors of s.  If any other p divides  s,  then

o*(2
ms)  >  2 6 + 1 n 3 + 1 ^ 5 + 1 ^ 7 + 1 B 13 + 1 ^ p + 1
2
ms  ~  2 6  *  3  "  5  "  7  "  13  *  P

Therefore, the only unitary perfect number of the form 25s is 2 6 • 3 • 5 • 7 • 13.
Proceeding  in this  fashion, it is easy  to show  that  the only unitary per-
fect  numbers  of  the  form  2
ms  with  m  < 10  are  those  listed  in the  theorem.
Thus, we may assume henceforth that 77? > 10.  (Alternatively, we could reduce to
the case 77? > 10 by quoting a result of Subbarao  [1].)
The method  of  the preceding  paragraphs  is "top-down": we  start with divi-
sors of  2
m  +  1 and work down.  While this procedure works well for specific  m,
it  does  not  lend  itself  well  to  a  proof  in  the  general  case.  We  therefore
introduce an alternative "bottom-up" procedure.  This procedure starts with the
Mersenne  primes  dividing  s  and  works  up  to the divisors  of  2
m  +  1.  (A Mer-
senne prime is a prime of the form 2^ - 1; the first few such primes are

3 = 2 2 - 1, 7 = 2 3 - 1, 31 = 2 5 - 1, 127 = 2 7 - 1, 8191 = 2 1 3 - 1.)

First we note that  s  does  have  Mersenne  prime  divisors.  For  in  equation
(1), all odd prime divisors of a*(s) =  V\Vo  •••  Pr
  m u s t  appear in the denomina-
tor of the right-hand  side.  But some of the  pi' s  divide  2
m  +  1,  so  at  least
one of the terms p^ + 1 must be free of any odd prime factors.  It follows that
p. is a Mersenne prime.

Suppose  q is  a  Mersenne  prime  dividing  s.  Renumber  the primes  in  (1) so
that  q = p,.  There is some  (necessarily unique) prime  p2  dividing s such  that
pl  | (p2 +  1).  Note that p 2 > 2p1 - 1.  Either  p2\(2
w  +  1)  or  there  is  some p 3
such that p2|(p3 +  !)•  Continuing in this way, we obtain a sequence of primes

Pl  <  Vz  <  '"  <  Pk>  (
2)
where p  is a Mersenne prime, p, |  (2
m  +  1), and p^ + 1 ^ 2p^. - 1.
To formalize the ideas of the preceding paragraph, we introduce the follow-
ing function /.  Let p be  an  odd  prime  in  the  denominator  of  the  right-hand
side of  (1).  We define  f(p)  to be 1 if  p\(2
m  +  1).  Otherwise, we  define  f(p)
to be the unique prime  p
r  such that  p
r\s  and p | (p ' + 1) .  We define

f0(p)  =  p.  / i ( p )  =  / ( p ) .
  a n d
  / * + I < P >  =  / ( / * ( p ) ) -
We also define

/(l) = 1  and  /w(p) = ft f. (p).
i- = 0
  %
For example, if TT? = 6 and  s  = 3 • .5 • 7 '13, then

/x(3) - 5, f2(3) = 1, and j^ (3) = 3 - 5 .

Similarly,

/co^7)  = 7 - 1 3 .

318  [Aug.

UNITARY PERFECT NUMBERS WITH SQUAREFREE ODD PART

Let  qY,  q2,  . ..,  qz  be the Mersenne primes dividing s.  Then all odd primes
dividing  s  occur in the product

At  this  point, we  cannot  rule  out  the possibility  that  this product  contains
repeated prime factors.  For example, if 41 \s,  then 41"]/^ (3)  and 4l|jf (7).  Ac-
cordingly, for each Mersenne prime  q  , we define  F(q^)  to be the product of all
primes that divide  f^iq^  but do not divide any of  fm(q{)>  f00(q2^'  • • • >  fm (?£ -1) •
With this definition, we have

2
m  + l r q * ^ ^ ) )  q*(^(^))

If we write

« < >  •  ^

then the above may be rewritten as

2m  +  x
 2.

G(<7i) ••• £(<?*) = 2.  (4)

The  idea behind  the proof  is to obtain upper bounds for  G(q)  that make  (4)
antenable.  The crucial point here is that, if p 1 5  p2,  . ..,  p  are  the  primes
described in (2), then p 2 > 2p15 p 3 > 4p1 - 3, etc.  It follows that

oo  2
ip.  - 2 ^ + 2
G(q) < II - r 1  1  •
i  = o 2
^p. - 2* + 1
^.s we  shall  show  in Lemmas  1 and  2, this product converges.  This bound for  G
is  sufficient  for  the  larger  Mersenne  primes.  A  more  elaborate  analysis  is
needed for the smaller primes.
 3.  Lemmas

Lemma  1:  If p and 6 are real numbers with p > 1, then

»  6p^ - (p + p 2 + ... + pi)  (p - 1)6

i=0  6p^ - (1 + p + p 2 + ... + pi)  (p - 1)6 - p

Proof:  The  K
th  partial product is

6  p6 - p  p^6 -  p
K  - •«- - p

6 - 1  p6 - p - 1  p
K&  -  p
K  - • ••  -,p - 1

Note that the numerator of each term after the first is p times the denominator
of the previous term.  Therefore, the  K
th  partial product is

6p*  (p - 1)6
p^6 _ p# _ ... - p _ i  (p - 1)6 - p + .p
  K'

The result follows by letting  K tend to infinity.
 o  m  - 1
Lemma  2:  If  q  =  2
m  -  1 is a Mersenne prime, then  G(q)  <  )  m  - 1

1989]  319

UNITARY PERFECT NUMBERS WITH SQUAREFREE ODD PART

Proof:  L e t  p^9  p2,  . . . ,  p  be  t h e  primes  d i v i d i n g  G (q)  .  Since  p-,  =  q  =  2m  and
and  p i + 1  ^  2p.  ,  we  s e e  t h a t

p.  >  2
m+i~
l  -  2*  +  1.

T h e r e f o r e ,
 9  tf?  9777 +  I  _  o
c(9)  < —  ^ — — -  . . . .

2 m - 1  2m + l - 3

The result now follows by applying Lemma 1 with 6 =  2m and p = 2.
Lemma  3:  Let  q.9  . .., q  be the Mersenne primes that divide  s  and are at least
8191.  Then
  J
G^  ••• < W  ^ f§yf-

Proof:  It is well  known  that, if  2m - 1 is prime, then  m must be prime.  Thus,
m = 2 or  m is odd.  Consequently

2 1 2 + 2 t
<?(„)  ...  c(^)  *  no 2l2+u  _ i

We bound this by observing that

2\2+2i  a,  2
lz+2i  - 4 - 4 2 - ...  - 4 ^
n  1 9 + 9 , —  ^  n -0 2 1 2 + 2 i  - 1  i=o  2
l2+zi  -  1 - 4 - 4 2 - . . . - 4*

The result now follows from Lemma 1 with 6 = 2 1 2 and p = 4.

Lemma  4:  Let (7., ..., q£ be the Mersenne primes that divide  s  and are at least
127.  Then  °
G(qd) ... G(qz) * g .

Proof:  We first get a bound on (7(127) .  Let p 1 5  ..., p^ be  the primes  that di-
vide F(127).  If  v  < 1, then £(127) < 128/127.  Assume  that  p > 2.  Then  px  =
127 and p~ is a prime of the form 127/z - 1, where all the odd prime divisors of
In are at least  8191.  Now 127 •  2l  - 1 is composite for 1 <  i  < 7, so p 2 > 127
• 2 8 - 1 = 32511.  Therefore,

r(  ,  < 128 "  32511 - 2i  -  2 - 2 2 - ... - 2^ = JJ28  16256
U  j " 127iV0 32511 . 2* - 1 - 2 - - - - -  2*  127 * 16255'

From this and Lemma 3, we see that

G(qj)  ...  Giqi)  ^(127)^(8191)  ... , l | f . i | | | f . f Z f , l | f .

4.  Proof of the Theorem

As stated in Section 2, we may assume that  m  > 10.

The proof breaks into three cases: (1) m odd, (2) m = 0 mod 4, and (3)  m  E 2
mod 4.

Case 1;  Assume that  m is odd.  Then 3J2™ + 1, and G(3) = 4/3.  It follows that
the left-hand side of (4) is

2
m + 1 4  r f l , r , ^ ,  .  1025 4 4 16 122 ^ .
~ ^ ~ "  3 ^ 7 ^ 3 1 >  ••• * 1024 3 3 15 121 < 2°

320  [Aug.

UNITARY PERFECT NUMBERS WITH SQUAREFREE ODD PART

Case  2:  Assume  that  m  = 0 mod 4.  Then  2
m + 1 = 2 mod 3 and  2
m + 1 E 2  mod 5.
It  follows  that  there  is  some  prime  p  such  that  p \ 2 m +  I,  p  E 2 mod 3, and
p  > 5.  Moreover, the congruence  x
1* E -1 mod p has the solution  x  E 2 m ^ , so we
have p E 1 mod 8.  By the Chinese  Remainder  Theorem, p E 17 mod 24.  We  cannot
have p = 17 since  32|a*(17).  Therefore, p > 41, and the left-hand  side  of (4)
is
 2~
  +-'  "
  P  +  l  0(7)0(31)  ... 5 i ° « * «  *!i 122 < 2.
2
m  3  p  1024 3 41 3 15 121

Case  3:  Assume  that  m E 2 mod 4.  Then  512 m + 1, and

ff(3)=-ff.

This  case  breaks  into  four  subcases:  (i) 7/fs; (ii) 71 s and 13^s;  (iii)  7|s,
13|s,  and 103|s;  (iv) 7|s, 13|s, and 1 0 3 \ s .

Subcase  3 (i)  :  Assume  that  7|s.  Then  the left-hand  side  of (4) is

^  «3)0(31)0(127)  ...<iSg$jliI|i<2.

Subcase  3 (ii)  :  Assume  that  71 s and 13|s.  Other  than  13, the least  prime  of the
form  lln  -  1 with  all odd prime  divisors  of  h  greater  than  or equal  to 31 is
7 • 32 - 1 = 223.  Therefore,

< 8 f, 224-  2
l  - (2 + 2
2• +  ••• + 2^) =  8 112
U)  ~
  n  i l  —'  ~*'  (1 + 2 +  ...  + 2*)  7 111'

Therefore, the left-hand side of  (4) is

^ 1025 4 6 8 112 21 12^ <  2
"  1024 3 5 7 111 15 121

Subcase  3 (iii)  :  Assume  that  7|s, 13 |s, and 103 \s.  Then  31 |s  since

a*(3 • 5 • 7 • 13 • 31)
7 • 13 • 31  > 2.

If  F(7) contains  any prime  factors  other  than  7  or  13, then  the least  such
factor  is of  the form  13/z -  1, where  all odd prime  factors  of  h  are > 127.
Other  than  103, the least  prime  of this  form is 13 • 2 7 - 1 = 1663.  Therefore,

G(7)  <  8 14  832
UK  J  ~  1 13  831 s

and the left-hand side of  (4) is

„ 1025 4 6 8 14 832 122
1024 3 5 7 13 831 121 < 2.

Subcase  3 (iv)  : Assume that  7 j s,  13 |s,  and 103 |s.  Then  \2l\s  since

q*(3 « 5 « 7 * 13 • 103 • 127)
3 • 5 • 7 • 13 • 103 • 127

The least prime of the form 103ft - 1 is 103 • 8 - 1 = 823.  Therefore,

C(i\  <  8 14 104  412
K  J  " 7 13 103  411'

1989]  321

UNITARY PERFECT NUMBERS WITH SQUAREFREE ODD PART

and the right-hand side of  (4) is

<
  1 Q 2 5  4  6  8 _H  JJ04 ^12  3072  <
~ 1024 3 5 7 13 103 411 3071

References

1.  M. V. Subbarao.  "Are There an Infinity of Unitary Perfect Numbers?"  Amev.
Math.  Monthly  77 (1970):389-390.
2.  M.  V.  Subbarao  &  L. J. Warran.  "Unitary  Perfect  Numbers."  Canad.  Math.
Bull.  9 (1966):147-153; MR 33 #3994.
3.  C. R. Wall.  "A New Unitary Perfect Number."  Notices  Amev.  Math.  Soc.  16
(1969):825.
4.  C.  R.  Wall.  "The  Fifth  Unitary  Perfect  Number."  Canad.  Math.  Bull.  18
(1975):115-122; MR 51 #12690.
5.  C.  R.  Wall.  "On  the Largest  Odd  Component  of  a Unitary  Perfect Number."
Fibonacci  Quarterly  25.4  (1987):312-316.

322  [Aug.
