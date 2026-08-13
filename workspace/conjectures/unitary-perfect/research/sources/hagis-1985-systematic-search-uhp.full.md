<!-- source: https://www.fq.math.ca/Scanned/25-1/hagis.pdf | converted from PDF -->

A SYSTEMATIC SEARCH FOR UNITARY HYPERPERFECT NUMBERS

PETER HAGIS, JR.
Temple  University,  Philadelphia,  PA  19122
(Submitted  January  1985)

1.  INTRODUCTION

If  m  and  t  are  natural numbers,  we say that  m is a unitary hyperperfect
number of order  t  if

m = 1 +  t[o*(m)  -  m - 1],  (1)

where  o* {m)  denotes  the  sum  of the unitary divisors of  m.  m is said to be a
hyperperfect number of order  t  if

m = 1 + t[a(7w) -  m  -  1],  (2)

where a is the usual divisor sum function.  Hyperperfect  numbers  (HP's)  were
first studied by D. Minoli & R. Bear  [4], while the study of unitary hyperper-
fect numbers  (UHP
?s) was initiated by the present author  [3]. H. J.J. te Riele
[6] has found  all  (151) HPTs less than 108 as well as many larger ones having
more than two prime factors.  D. Buell  [2] has found all (146) UHPTs less than
108.  More recently, W. Beck & R. Najar  [1] have studied the properties of HP's
and UHP's.  One of the results they obtained was the following.

Proposition  1: If  m is a unitary hyperperfect number of order  t ,  then (m,  t)  =
1 and  m  and  t  are of opposite parity.

The purpose of the present paper is to develop a search procedure, differ-
ent from that employed  by Buell,  which can be used to find all of the unitary
hyperperfect  numbers less  than  a  specified bound  with a  specified number of
distinct prime factors  (provided the necessary computer time is available).

2.  THE GENERAL PROCEDURE

Suppose  that  m =  ar
ys
x,  where  r  and  s  are  distinct  primes,  yX  4- 0, and
(a,  rs)  -  1.  If  m is a unitary hyperperfect number of order £, then, since a*
is multiplicative and  o*(r
y)  = 1 + rY, it follows from  (1) that

[a  -  t(o*(a)  - a)]rYsA - ta*(a)[p
Y +  s
x]  = 1 + t[o*(a) - 1].

Multiplying this equality by  a  -  t(o*(a)-a)  and then adding  [to*  (a)]
2  to each
side, we obtain

{[a -  t(o*(a)  -  a)]r
y  -  to*(a)}ila  -  t{o*{a)  -  a)]s
x  -  to*(a)}

=  [a  -  t(o*(a)  - a)][l +  t(o*(a)  -  1)] +  [to*(a)]
2.  (3)

If  AB9  where 1 <  A < B,  is the  "correct" factorization of the right-hand
member of  (3), then we see that

6  [Feb.

A SYSTEMATIC SEARCH FOR UNITARY HYPERPERFECT NUMBERS

rT =  [to*(a)  + A]/[a  -  t(o*(a)  - a)],  (4)
sA =  [to*(a)  + B]/[a  -  t(o*(a)  - a)].

Since the steps just described are reversible, given values of  a and t,  if
a  factorization  AB of the right-hand member of  (3) can be found for which the
right-hand members of (4) are distinct prime powers relatively prime to a, then
the integer  ar
ys
x  is a unitary hyperperfect number of order  t .  Of course, for
most values of  a and  t  the right-hand members of (4) will not both be integers,
let  alone  prime powers.  It should be  mentioned  that the above derivation of
(4) is basically due to Euler via H. J. J. te Riele  (see [5]).

3.  THE CASE  a = 1

If, in  (4), we set  a = 1, then, since G*(l) = 1, it follows that  r
y  -  t  +  A
and sA =  t  +  B,  where,  from  (3),  AB = 1 + t2.  Suppose  that  t  is  odd.  Then
AB E 2 (mod 8) and it follows that  A and  B are of opposite parity.  Therefore,
without loss of generality, r = 2 and, since  3\ts
x  (see Fact 1 in [3]),  we have
proved the following result.

Proposition 2:  If 77? =  r
ys
x  is  a  unitary  hyperperfect  number of odd order  t9
then 2 IT?? and either 77? = 2Y3X or 3 It.

Using the CDC CYBER 750 at the Temple University Computing Center, a search
was made for all unitary hyperperfect numbers less than 10
ltf  of the form 2Y3 •
Only two were found:

2 - 3  (t  = 1)  and  2 5 • 3 2  (t = 7).

The search required less than one second.

We now drop the restriction that  t  be odd.

Proposition  3'-  If  m  =  r
ys
x  =  RS  is a  unitary  hyperperfect number of order  t9
then  m  > 4t2.

Proof:  RS = 1 +  t(o*  (RS)  -  RS  -  1) = 1 +  t(R  +  S) .  Therefore,  R  >  t(l  + i?/£) .
Similarly,  S  >  t(l  +  S/R)9  and it follows that

RS  >  t
2(l  + i?/5 + S/i? + 1) > 4t2.

From Proposition 3, we see that all unitary hyperperfect numbers less than
1010  and of the form  r
ys
x  can be found by decomposing  1 + t 2 , for 1 <  t  < 50000,
into  two  factors  A and  B and then testing  t  +  A and  t  +  B to see if each is a
prime power.  This  was  done, and 822 UHPfs less than 10 1 0 with two components
were found.  790 were square-free and, therefore, also HPfs.  Of the remaining
32  "pure"  UHP*s, all but one, 3 2 * 2 5  (t  = 7), were of the form  r
ys  or rs A.  t
was odd for only ten of the 822 numbers, the two largest being

2 1 3 • 33413  (t  = 6579)  and  2 1 5 • 238037  (t  = 28803).

The complete search took about five minutes of computer time.

1987]  7

A SYSTEMATIC  SEARCH FOR UNITARY HYPERPERFECT NUMBERS

4.  AN  IMPORTANT  INEQUALITY

In this section, we shall generalize the inequality of Proposition 3.

Proposition 4:  Suppose  that m  is  a  unitary hyperperfect  (or  a hyperperfect)
number of order  t  with exactly  n prime-power components.  Then  m >  (nt)
n.

Proof:  Suppose first that  n  = 3  and  77? =  p
aq
&r
y  =  PQR, where  P  >  Q  >  R.  From
(1)  [and  (2)], it follows easily that

PQR >  t(PQ  +  PR  +  QR).

If  A  =  P/Q  and  B  =  P/R,  then

P  >  t(l  +  A +  B),  Q  >  t(l  +  B/A  +  1/A),  and  R  >  t(l  +  A/B  + 1/5).

Therefore,

m =  PQR >  t
3(l  +  A +  B)
3/AB.  (5)

If  F(xs  y)  =  (I  +  x  +  y)
3/xy,  where  x  > 0 and  y > 0, then

ZF/dx  = (1 +  x +  y)
2(2x  -  y  -  1)/x2y
and  8P/8z/ = (1 +  x  + 2/)
2(22/ -  x  -  l)/xy
2.

It follows easily that, if  x > 0 and z/ > 0, then POr,  y)  > P(l, 1) = 33.  From
(5), we have  m >  (3t)3.
Now suppose that  n = 4 and 777 =  p
aq$r
ys
x  =  PQRS,  where  P  >  Q  >  R > 5.  From
(1) [or (2)],

PQRS  >  t(PQR  +  PQS +  PRS  +  QRS).

If  A = P/§, 5 = P/P, and C = P/£, then

P >  t(\  + ,4 +  B  +  C),  Q  >  t(l  +  B/A  +  C/A  +  l/A)9

R  >  t(l  +  4/B  +  C/B  +  1 / 5 ) ,  and  S  >  t(l  +  A/C  +  S/C  +  1/C).

Therefore,

tfz  =  P^P5  >  t
h  (I  +  A  +  B  +  C)
h  I ABC.  (6)

If  G(x,  y,  z)  =  (1  +  x  +  y  +  z)^/xyz,  where  x  >  0,  z / > 0 ,  3  >  0,  t h e n

3£/3^  =  (1  +  x  +  z/  +  s ) 3 ( 3 x  -  y  -  z  -  l)/x
2yz,

dG/dy  =  (1  +  #  +  y  +  S) 3 ( 3T/  -  x  -  2  -  l ) / / y 2 x s 5

and  dGfdz  =  (1  +  x  +  y  +  z)
3  (3s  -  x  -  y  -  l)/z
2xy.

It follows that G(x, zy, s) has a minimum at  (1, 1, 1)  and  that  G(x>  y,  z)  ^ 4
if  x  > 0, z/ > 0, 3 > 0.  From  (6), we see that 777 >  (4t)
4.

A similar argument can be used for any value of  n  that exceeds 4.
 [Feb.

A SYSTEMATIC  SEARCH FOR UNITARY HYPERPERFECT NUMBERS

5-  THE CASE  a  =  p
a

If,  in  (4) and the  right-hand  member of  (3),  we set  a  =  p
a,  then, since
o*  (p
a)  =  p
a  + 1, it follows that

r y =  (to*(p
a)  +  A)/(p
a  -  t)  and  s
x  =  (to*(p
a)  +  B) / (p<* -  t)  (7)
where  AB = (p
a -  t)(l  + £pa) + t2(pa +  l) 2 .  (8)

If  m = papTsAis a UHP of order  t  such that 777 < 109, then it is easy to see
that if  p
a  is the smallest prime-power component of  m3  p
a  < 1000.  From Propo-
sition 4,  t  < 1000/3. All solutions of (7) and (8) (with  A<B)  were sought with
2 < p a < 9 9 7 , 1 <  t  < 333, and p a r Y s A < 1 0 9 .  The search yielded nine UHP's less
than 109.  Five of these were given in [2].  The four new ones are:

26 • 659 • 2693  (t  = 57); 67 • 643 • 792  (t  = 60);

547 • 569 • 1259  (t  = 228); 7 2 • 79 • 119971  (t  = 30).

The search required about thirty minutes of computer time.

6.  THE UHP's LESS THAN 109

Let  Mn  denote the set of all unitary hyperperfect numbers  m such that  m <
10
9  and 777 has exactly  n  distinct prime divisors.  From  Fact 2 in  [3],  M1 is
empty and, from the searches described  in Sections 3 and 5,  M2 and  M3 have 330
and 9 elements, respectively.  Since 2 • 3 • 5 • 7 • 11 • 13 • 17 • 19 • 23 • 29 > 109,
we see that  Mn is empty if  n  >  9.  If  n  = 8 or 9, then, from Proposition 4, it
follows easily that  t  = 1 so that, if  m eMQ  or  m e Ms,  then  m is a unitary per-
fect number  (o*(m)  = 2m).  Since there are no unitary perfect numbers less than
10
9  with  8 or 9 prime-power components  (see [7]), it follows that both  MQ and
M9 are empty.
If 77? < 109, then, from Proposition 4, if  n  = 4, then  t  < 44, if  n  = 5, then
t  <  12, if n = 6, then  t  < 5, if  n = 7, then  t  < 2.  Subject to these restric-
tions on £, and with  a restricted  so that rY  is greater than every prime-power
component of  a while  ar
Ys
x  <  109,a search was made for solutions of  (4).  This
search required two-and-one-half hours of computer time, and it was found that
Mk9  M6,  and  M7 are empty, while  M5 has one element, 26 • 3 • 5 • 7 • 13  (t  = 1) .
Thus, there are exactly 340 UHP's less than 109.
It  should,  perhaps, be mentioned that while  Mh is empty, one UHP with four
prime-power components  was  found: 59 °  149 * 29077 °  10991483959  (t  = 42) is both
a  UHP  and an  HP  (since it is square free).  It  does  not  appear in te Riele's
lists of HP's and may be the smallest HP with exactly four distinct prime fac-
tors .
 REFERENCES

1.  W. E. Beck & R. M. Najar. "Hyperperfect and Unitary Hyperperfect Numbers."
The  Fibonacci  Quarterly  23, no. 3 (1985):270-276.
2.  D. A. Buell.  "On the Computation of Unitary Hyperperfect Numbers."  Con-
gressus  Numerantium  34  (1982):191-206.
3.  P. Hagis, Jr.  "Unitary Hyperperfect Numbers."  Math.  Comp.  36  (1981):299-
301.
4.  D. Minoli & R. Bear.  "Hyperperfect Numbers."  Pi  Mu  Epsilon  Journal  (Fall
1975):153-157.

1987]  9

A -SYSTEMATIC SEARCH FOR UNITARY HYPERPERFECT NUMBERS

5.  H. J. J. te Riele.  "Hyperperfect  Numbers  with Three Different Prime Fac-
tors."  Math.  Comp.  36  (1981):297-298.
6.  H. J. J. te Riele.  "Rules  for  Constructing  Hyperperfect  Numbers."  The
Fibonacci  Quarterly  22,  no. 1 (1984):50-60.
7.  C. R. Wall.  "The  Fifth  Unitary  Perfect  Number."  Canad.  Math.  Bull.  18
(1975):115-122.

10  [Feb.
