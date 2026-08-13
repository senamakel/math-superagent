<!-- source: https://www.fq.math.ca/Scanned/23-4/tovey.pdf | converted from PDF -->

MULTIPLE OCCURRENCES OF BINOMIAL COEFFICIENTS

CRAIG  A .  TOVEY
Georgia  Institute  of  Technology,  Atlanta,  GA  30332

(Submitted   February  1984)

I.  INTRODUCTION

How  many  times  can  the  same  number  appear in  Pascal
fs triangle?  After

eliminating  occurrences  due to symmetry, (7 ) =  (  7  ), and the uninteresting
(n\  ln\  V  '   Xn  "   ;

occurrences of  1  =  (  J and  n =  f  J, the answer to this question is not clear.

More  precisely,  if 1 <  k <  n/2, w e  say that ( -, 1 is a   -proper binomial coeffi-

cient.  Are  there  integers  that  can be expressed in different ways as proper

binomial coefficients?
Enumeration by  hand or with a  computer program produces some cases, given
in Table 1.  The smallest is 120, which equals
(?)  -  (?)•

Table 1.  Small Multiple Occurrences of Binomial Coefficients

INTEGER

120

210

1540

3003

7140

11628

24310
 BINOMIAL COEFFICIENTS

Cs")- (?)
c:). (V)

(?)•  (?)
i\%  ('/)• (?)
(?). en
(?)• (T)
Cs
7
)-  (T)

There is even an instance of a  number,  3003, which  can be expressed  in three
different ways.  No clear pattern emerges; the cases just seem to be sprinkled
among  the  binomial coefficients.  W e  conjecture that,  for any t, there exist
infinitely many integers that may be expressed in  t different  (proper) ways as
binomial coefficients.
356  [Nov.

MULTIPLE OCCURRENCES OF BINOMIAL COEFFICIENTS

Here  we  prove  the  conjecture for the case t = 2.  The proof is construc-
tive and depends in an unexpected way on the Fibonacci sequence.

I.  THE CONSTRUCTION

We seek solutions to

an especially tractable situation because it leads to a second-order equation.
In particular, if  (1) holds, then  n(k  + 1 )  =  (n  -  k)(n  -  k  - 1).  Let

x =  n  -  k - 1.  (2)

Then  x(x  + 1) =  n{n  - x)  so n
2  -  xn  -  (x
2  +  x)  = 0 and

x +  V5x
2 +  kx  ,0>l
n =  ^  (
3^

(since  n  is positive).  Integer solutions to (3) therefore lead to integer so-
lutions to (1).

Since  5x
2  +  kx  is even  if  and only if  x  is even,  this means we must find
integers  x  such  that  5x
2  +  kx  is a  perfect  square.  Now  x  and  5x  + 4 have no
common factors except possibly 2 or 4, so a natural slightly stronger condition
would be that both  x  and  5x  + 4  be  perfect squares.  In other words, we  need
to  find  integers  z  such that  5z
2  + 4 is a perfect square.  These are given by
the following lemma.

Lemma  1: Let  Fj  denote the Fibonacci sequence.  Then, for all J,

(F..x  + F - + 1 ) 2  - 5F|  -4<-l)*.

Proof: A straightforward  calculation  (see, e.g.,  [2], pp. 148-149) shows

(.Fj + 1  + F..J*  -  5F/ = 4 ^  +  F.Fj_1  - F/) - -4(F? +  F^^  -  F? + 1 ),

which yields the result by induction.

The lemma tells us that for any  j  even,  z  =  Fj  gives the perfect square

5s
2 + 4 =  {F._x  +Fj+1)
2.

This completes the construction.

Theorem  1: Let  Fj  denote  the  Fibonacci sequence.  Then, for any even j , there
exists a solution to  (1), where  x  =  FJ  and  n and  k  are  given by  (2) and (3).

Remark: Letting  Lj  denote the Lucas sequence as usual, we can write this solu-
tion as  Fjh
  +FI  ,.
  FJ
Ld  - F !  ,

Theorem 2: Theorem 1 gives all solutions to (1).

Proof:  It follows from  the preceding discussion that any solution to (1) cor-
responds via  (2) to some integer  x  such that  5x
2+  kx  is a perfect square.  Let
a  (resp.  b)  be the number of times 2 divides  5x + 4 (resp.  x).  If  a > 2, then

1985]  357

MULTIPLE OCCURRENCES OF BINOMIAL COEFFICIENTS

b  -  2 and, conversely,  b > 2 implies  a  -  2.  Since 5 ^ + 4  and  x  have no common
factors except  (possibly) 2 or 4,  (5x  + 4)/2a is a perfect square, as is  x/2
b.
Therefore, a + & is even, so a and 2? are both even or both odd.  In the former
case,  x  and  5x  + 4 are perfect squares.  We claim this leads precisely to the
class  of  solutions  given  by Theorem 1.  In  the  latter case, it follows that
a  =  b = 1.  Thus, we seek integers s such that 5s2 + 2 is a perfect square.  We
further claim that no such integers exist. The two claims can be shown to fol-
lows  from  the general theory of the so-called Pell equation  (see, for example,
[1] for the first claim,  and  [3, pp. 350-358] for the second claim).  For com-
pleteness, we give a simple proof that does not rely on the general theory.

Let  {An}  denote any sequence of positive numbers satisfying the recurrence
An  +  An+1  =  An+2'
  T n e  argument from Lemma 1 shows that, for all n,

(An-i  +
  A
n+0  ~  ~>An  -  4(An_1 +  An_1An  -  An)  =  -\An  +  An  + 2)  +  5An +  1 .

Therefore, given  any  solution  s,  y  to 5s2  +  k  -  y
2,  we can construct smaller
solutions by setting

A  y " z
  A  -  y
  +  z

Ai  ~
 S>
  Ai-1  ~  2
  5  Ai  + 1 ~  2  '

and extending the sequence  {An}  backward according to the recurrence

An
  +  A
n+i
  =  An+2*
[The solutions will be  z  =  Aj,  y  =  AJ-_1  +  Aj+li  where  j  =  i  (mod 2), with
\k\  =  h\An  +  AnA
2
+1  -  A
2
+1\,  for all  n.]

Now,  let  (s, y)  be any integer solution to  5z
2  + 4 = z/
2.  Set

^  = 2  and  ^- + 1
  = — o —  (
an  integer).

Then  extend  {An}  backward to get the solution corresponding to  A^_  and  A._  .
If  z  > 3, then

.,  ^  z/5  -  z  ^  .  y  -  % ^  zy/5 +  .5 -  z  ^  _0
.61s ^  «  ^ ^i-i
 = — 9 —  2  -72s,

whence  .28s <  Ai_2  <  .39s. Therefore, if  Ai  ^ 3, the solution corresponding to
i4^_2  is smaller.  Repeatedly extend  {An}  backward until  Aj  < 3.  Since the only
such  integer  solution  is  (1, 3 ) , s  must  have been a Fibonacci Number.  This
verifies the first claim.  The second claim, that 5s2 + 2 =  y
2  has no solutions,
follows immediately from the fact that  y
2  =  2  (mod 5) has none.

REFERENCES

1.  I.Gessel.  Advanced Problem H-187.  The  Fibonacci  Quarterly  10  (1972):417-
419.
2.  G. H. Hardy & E. M. Wright.  An  Introduction  to  the  Theory  of  Numbers.  Ox-
ford: Oxford University Press, 1959.
3.  J. Uspensky & M. Heaslet.  Elementary  Number  Theory.  New York: McGraw-Hill,
1939.

358  [Nov.
