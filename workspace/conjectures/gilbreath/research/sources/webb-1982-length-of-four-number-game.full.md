<!-- source: https://www.fq.math.ca/Scanned/20-1/webb.pdf | converted from PDF -->

1982]  33

THE  LENGTH  OF  THE  FOUR-NUMBER  GAME

WILLIAM  A.  WEBB
Washington  State  University,  Pullman,  WA  99163
(Submitted  April  1980)

INTRODUCTION

Let  D  be  t h e  o p e r a t o r  d e f i n e d  on  4 - t u p l e s  of  n o n n e g a t i v e  i n t e g e r s  by

D(ws  x9  y 9  z)  =  (\w  -  z\  9  \w  -  x\  s  \x  ~  y\  9  \y  -  z\).

Given  any  initial  4-tuple  S  =  SQ  =  (wQ9  x0s  y09  z0)9  we obtain a sequence {/S^},
where  Sn  + 1  =  DSn.  This  sequence is  sometimes called the  four-number  game.  The
following  curious  fact  seems  to  have  been  discovered and  rediscovered  several
times—-[3], [4],  [5]—Sn=  (0, 0, 09 0) for all sufficiently large  n.  We can thus
make the following definition.

DEFINITION:  The length of the sequence  {Sn}9  denoted  L(S)9  is the smallest  n  such
that  Sn  = (0, 0, 0, 0).

A natural question to ask is:  "How long can a game continue before all zeros
are reached?"  Again, it is well known that the length can be arbitrarily long if
the numbers in  Sn  are sufficiently large [4]. One of the easiest ways to see this
makes use of the so-called Tribonacci numbers:

t0  = 0,  t1  = 1,  t2  = 1  and  tn  = £n_i +  tn_2  + £n-3  f° r  n  2. 3.

If we let  Tn  =  (tn,  tn_19  t n_ 2,  tn_3)9  then a simple calculation shows that

and so  _ „
L(Tn) = 3[|J.

It has also been noticed that  the sequence  beginning  with  some  Tn  seems to
have the longest length of any sequence whose original elements do not exceed  t n ,
We will prove that this is almost true.
It should be pointed out that if we allow the elements of  S0  to be real, then
we  can  obtain a game of infinite length by taking  SQ  =  (r
3,  r
2
s  v9  1 ) 9 where  r  =
1.839... is the real root of the equation  x 3 - x 2 - x - l = Q  (see [2], [6], [7]).
Moreover, this is essentially the only way to obtain a game of infinite length [7].
To obtain a long  game  with integer entries, we should  pick the initial terms to
have ratios approximating  r  [1].  The Tribonacci numbers do this very nicely.

MAIN RESULT

Before proving our main theorem, we need a few easy observations.  If

\s\  = max(w,  x,  y, z ) s
then  \S,\  2L  \SI\  >  \Si\  .*. .
The games having initial elements

(w,  x,  y9  z),  (xs  ys  z9  w),  (ys  z9  w,  x),  (z9  w,  xs  y);

(z9  y9  x9  w);  (w +  k9  x +  k9  y +  k9  z +  k);

and  (kw9  kx9  ky9  kz),  k  > 0;

all have the same length.  We now state our main theorem which will be an immedi-
ate consequence of Theorem 2.

34  THE LENGTH OF THE FOUR NUMBER GAME  [Feb.

THEOREM  1:  If  \s\  ±  \Tn\9  then£(S)  <.  L(Tn)  + 1 = 3[~1  + 1.

One of the first things to notice is that  L(S)  <. 6,  unless the  elements of  S
are monotonically decreasing,  w  >  x  >  y  >  z.  [Remember, cyclic permutations and
reversals yield equivalent games, so (5, 7, 12, 2) -(2, 5, 7, 12) -(12, 7, 5, 2 ) ,
which is monotonically decreasing.) This can be checked by simply calculating the
first six  Sn  if  S0  is not monotonic [1]. Also, if  Sn  is mono tonic decreasing, then
Sn+1  cannot be monotonic increasing.  Therefore, in a long game, all of the  Sn  at
the beginning must be monotonic decreasing.
Let  Sn  =  (wn9  xn9  yn9  zn)  «  We  say  that  Sn  is additive if  W
If  Sn_l  is monotonic  (decreasing), then a trivial calculation shows that  Sn  is ad-
ditive.  Thus, although  S  =  SQ  may not be additive,  Sl9  S29  ...  9  Sn  will be addi-
tive as long as  SQ9  Sl9  ..., £n-i  are monotonic.

LEMMA:  If  S19  S29  ••• >  S10  are all monotonic  (decreasing),  5 X  is additive, and
|5j,| £  tn9  then either  |SJ  <_  2tn_2  or  |S7| £  4tn_„ or  |S10| 1  8tn„6.

PROOF:  Write 5 X  = (a +  b + c,  a9  b9  o)  and assume a +  b + <? £ £„,

\SM\  >  2tn_2s  \S7\  > 4tn_lf, and  |S 1 0| > 8tn_6.

Since we know that £ x ... 5 1 0  are all monotonic, they can be explicitly calculated,
and we find that  \Sh\  = 22?, |57| =  ka  -42? - 4<?, and  |S 1 0| - 16c - 82?.

jsj  >  2tn_2  implies  2b  >_2tn_2  + 2  or  32? _> 3tn_2 +'3;  |S7| > 4tn_4  implies
<z-£-c?.>  £„„!+ + !; | JS^X 0 I > 8tn_6  implies  2c-b  >_  tn-$  +  \*  Adding these three
inequalities, we obtain

a  +  b  +  o _> 3tn_2 +  tn_k  + tn-6 +•• 5.

But since  a +  b + c £  t n, we have

Using the defining relation of the Tribonacci numbers repeatedly, we get

2£n_3  > 2tn.3 + 5,

which is an obvious contradiction.  This proves the lemma.

THEOREM  2:  If  S1  is additive and  |5j £  tn9  then L(5X) £ L(!Tn) = 3[~1 ,  n  •> 2.

PKCX)F:  Since S^ is  additive,  we  may  write  Sx  = (a + 2? +  o9  a, 2?, <?), where
£n-i < # + 2? +  o £ tn.  We use induction on n.  We can check the first 'few
1 cases
(by  computer)  and see that the theorem is true for  n = 2, 3,  ...,  9.  (That is,
\S1\  £ 81.)  Now, assume the result is true for all  Sx  such that  \S1\  <.tk9  where
k  < n,  n  >_ 10.
If  Sl9  ..., 5 1 0 are all monotonic, then, by the induction hypothesis and the
lemma, either
 L(SX)  =  L(SJ  + 3 £ 3p-=~^] + 3 = 3[|]

or  LiS^  =  L(S7)  + 6 £ 3 p - = ^ ] + 6 =  3 ^ ]

or  L(SO  = L(£10) + 9 < 3 p - ^ ] + 9 - 3[f ] .

Here  we  have  used  the  f a c t  that  2
t  d i v i d e s  every  element  of  S3t+i>  t  >_  1.
Thus,  for  example,  Sh  -  2S%  and  LOS^)  -  1 ( 5 $ ) .  If  | 5 k |  £  2 t n . 2 >  then  | 5 $ | £ t n _ 2 ,

a n d  S O  fn  -  21
Lost)  i  LCr„_2>  -
  3 r ^ J 9

1982]  THE LENGTH OF THE FOUR NUMBER GAME  35

by the induction hypothesis, taking  S*  as our  'new
1:S>  .  Thus, in any case,

LiS,) < 3[§],

If  S19  ...9  S10  are not all monotonic,  let  Sj  be the first which is nonmono-
tonic.  Then
 L(S±)  =  L(S3-)  +  (j - 1) < 6 +  j  - 1 = j + 5  < 1.5,

since  L(Sj)  _< 6 whenever  Sj  is not monotonic.  But since  n _> 10,

LCTn) = 3[fl  2: 15,
so LOSx) 5 £(£„).
  L Z J

This completes the proof of Theorem 2.

Theorem 1 is now an easy corollary, since:  if  S0  is monotonic decreasing and
\SQ\  <L  \Tn\*  then  \SX\  <_  \.Tn\  and  S1  is additive. If  S0  is not monotonic decreas-
ing, then  L(S0)  £  6.
There actually are examples where  L(S)  =  L(Tn)  + 1:

L(T&)  = L(13, 7, 4, 2) = 9  and  L(13, 6, 2,0)  = 10.
iy,

L(a  +  b + e, H  c, c, 0) = £(a + & 4- <?, a, 2?, a) + 1;

L(tn9  tn_2  + * n_ 3, t n_ 3, 0) = L(Tn) + 1 - 3 [ | ] + 1 .

If we begin with a fc-tuple of nonnegative integers, then it is known that
Sn  = CO, 0, ..., 0)  for  sufficiently large  n9  provided  k  =  2
t.  (If k ^  2
t,  the
sequence {£n} may cycle  [3], [4], [9].)  Thus, a natural question to ask is: "What
is the maximum length of the eight number game, or, more generally, the 2*-number
game?"
It was already mentioned  that if  S±  is additive and leads to a long four-num-
ber game, then the ratios of the elements of  'S1  should be close to the number  r  ~
1.839...  .  How  accurately can  the length of the game  be  predicted if one knows
these ratios?
 REFERENCES

1.  E. R. Berlekamp.  "The  Design of  Slowly  Shrinking Labelled  Squares."  Math.
Comp.  29 (1975):25-27.
2.  M. Bermester, R. Forcade&E. Jacobs.  "Circles of Numbers."  Glasgow-Math.  J.
19 (1978):115-19.
3.  C. Ciamberlini & A. Marengoni.  "Su una interessante curiosita numerica."  Pe-
riod.  Mat.  Ser.  4 17 (1937):25-30.
4.  Benedict Freedman.  "The Four Number Game."  Scripta  Math.  14 (1948):35-47.
5.  R. Honsberger.  Ingenuity  in  Mathematics.  New York: Random House, 1970.
6.  Hans Helmut Lammerich.  "Quadrupelfolgen."  Praxis  der  Mathematik  (1975), pp.
219-23.
7.  Moshe Lotan.  "A Problem in Differencing Sets."  Amer.  Math.  Monthly  56 (1949):
535-41.
8.  R. Miller.  "A Game with  n Numbers."  Amer.  Math.  Monthly  85 (1978) : 183-85.
9.  P. Zvengrowski.  "Iterated  Absolute  Differences."  Math.  Magazine  52 (1979):
36-37.
