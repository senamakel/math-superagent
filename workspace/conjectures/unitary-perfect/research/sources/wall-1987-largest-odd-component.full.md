<!-- source: https://www.fq.math.ca/Scanned/25-4/wall1.pdf | converted from PDF -->

ON THE LARGEST ODD COMPONENT OF A UNITARY  PERFECT NUMBER*

CHARLES R. WALL
Trident  Technical  College,  Charleston,  SC  28411

(Submitted  September  1985)

1.  INTRODUCTION

A divisor  d of an integer  n is a  unitary  divisor  if gcd  (d9  n/d)  = 1.  If
d  is a unitary divisor of n we write  d\\n9 a natural extension of the customary
notation  for the case in which  d is a prime power.  Let o * (n)  denote the sum
of the unitary  divisors of n:

o*(n)  = £  d.

d\\n

Then  o* is a multiplicative  function and G*(pe)=  1 + p e for p prime and e > 0.
We  say that an integer  N is  unitary  perfect  if o* (N) = 2#.  In 1966,  Sub-
baro and Warren  [2] found the first four unitary  perfect numbers:
6 = 2 * 3 ; 60 = 2 23 - 5 ;  90 = 2 * 3 25; 87,360 = 263 • 5 • 7 • 13.

In  1969s I announced  [3] the discovery of another  such number,

146,361,936,186,458,562,560,000
= 2 1 83 • 5^7 • 11 • 13 • 19 • 37 • 79 • 109 * 157 • 313,

which I later proved [4] to be the  fifth unitary  perfect number.  No other uni-
tary perfect numbers are known.

Throughout  what  follows,  let N =  2am (with  m odd) be unitary  perfect and
suppose that  K is the largest odd component (i.e., prime power unitary  divisor)
of  N.  In this paper we outline a proof that, except for the five known unitary
perfect numbers,  K > 2
 2.  TECHNIQUES

In light of the fact that  0*(pe)  = 1 +  pe  for p prime, the problem of find-
ing a unitary perfect number is equivalent to that of expressing 2 as a product
of fractions,  with  each numerator being  1 more than its denominator, and with
the denominators being powers of distinct primes.  If such an expression for 2
exists,  then the denominator of the unreduced  product of fractions is unitary
perfect.  The main tool is the epitome of simplicity: we must  eventually  divide
out any odd prime that appears in either a numerator or a denominator.

If p is an odd prime,  then  o*(p
e)  = 1 + pe  is even.  Thus, if some of  the
odd components of a unitary perfect number  N are known or assumed, there is an
implied  lower bound for a, where  2a\\N9  since all but one of the 2 fs in the nu-
merator of o*(N)/N  must divide out. Another lower bound, useful in many cases,
is Subbarao?s  result  [1] that  a > 10 except for the first  four unitary  perfect
numbers.

*This  paper  was written  while  the  author  was  Visiting  Professor  at  The  Uni-
versity  of  Southwestern  Louisiana,  Lafayette,  LA.

312  [Nov.

ON THE LARGEST ODD COMPONENT OF A UNITARY PERFECT NUMBER

A  simple  program  was  run on a microcomputer to find9  for each odd prime
p < 2 1 5 , the smallest  A for which  2A E ±1 (mod p).  If  2A E 1  (mod p ) 9 then p
never divides 1 + 2 a.  If  2A = -1 (mod p),  then p divides 1 + 2 a if and only if
a  is an odd integer times  A,  and we refer to A as the  entry  point  of p.

If an odd prime p has entry point ^ and p2l(l + 2^), it is easy to see that
2 P _ 1  E 1 (mod p 2 ).  There are only two primes less than  3 • 109  for which this
this  phenomenon occurs,  and they are 1093 and 3511.  Then 1 +  2A would have a
component larger than 106.  Thus5  for  the primes  p < 2 1 5 under consideration
here,  either  p  never  divides 1 +  2a  or p||(l +  2A)  or 1 +  2a  has a  component
larger than 2 1 5 .

The  odd  primes  less  than  2  having  entry  points  were ordered by entry
point.  Then  it  was a fairly easy procedure to consider algebraic factors and
conclude  that  1 +  2a  has all components less than 2 1 5 for only  a < 11 and the
a  shown in Table 1.
 Table 1

2a

2 1 1

2 1 2

£ 1 3
2 "
21 5

21 8

2 2 1

2 2 2
 1 +  2a

3*683  j
17*241
3*2731
5*29*113
3
2*11*331
5*13*37*109
3
2*43*5419
5*397*2113
 2 2 \
2 2 5

226

o3 0
23 3

2 3 4

2k2
24 6

278
 97*257*673
3*11*251*4051
5*53*157*1613
5
2*13*41*61*1321
3
2*67*683*20857
5*137*953*26317
5*13* 29*113*1429*14449
5*277*1013*1657*30269
5* 13
2*53*157*313*1249*1613*3121* 21841

In  many of the proofs,  cases are eliminated because under the stated con-
ditions  o*(N)/N  would be less than 2*  A number  n for which  o*(n)  < 2n is called
unitary  deficient  (abbreviated  "u-def").  Finally, we will write  a  -  A • odd to
indicate that a is an odd integer times  A.

3*  PRELIMINARY CASES

If Z = 3 , we have 3|a*(2a), so a is odd.  But N is u-def  if a > 3, so a = l ;
hence,  N = 2 e 3 = 6, the first unitary perfect number.

If Z = 5, we immediately have  3\\N and  a = 2 • odd.  But N is u-def  if  a  > 6,
so  a  =  21 therefore, N  -  223 m 5 = 60, the second unitary perfect number.

Note that Z = 7 is impossible, because 7 never divides 1 + 2 a.  In general,
the  largest  component  cannot  be the first power of a prime that has no entry
point.

If Z = 3 2 = 9, then 511/1/, and  O*(5)  uses one of the two 3fs. To use the other
3, we must have 3|a*(2a), so a is odd. Now, 7/71/ or else 7|a*(2a)9  which is im-
possible.  Then  N Is u-def  if a  > 3, so a = 1; hence,  N  =  2 • 325 = 90, the third
unitary perfect number.

If  K = 11, then  li[a*(2
a), so  a = 5 odd; hence, 3|a*(2a).  But 3la*(ll) as
well, so 3
2ll/l/.  Then 5la*(32), so 511/1/, and since 3la*(5) we have  33\N9  contra-
dicting the maximality of  K.

If Z = 13, we have  13|a*(2a), so a = 6 odd; hence, 5|a*(2a).  Then 511/1/, so
311/1/ because  32\\N would imply  52\NS  a contradiction. Because  1311/1/, we have 711/1/,

1987]  313

ON THE LARGEST ODD COMPONENT OF A UNITARY  PERFECT NUMBER

but we cannot have  ll\\N  or else  32\N.  But N is u-def  if  a > 189 so  a  -  6, from
which  it  follows that  N = 2 63 • 5 • .7 • 13 = 8793609  the fourth  unitary  perfect
number.

We have now accounted for the first four unitary perfect numbers. In light
of SubbaraoTs  results  [1], we may assume that  a > 10 from now on.

Now  suppose  a = 78.  Because 313- 1249la*(278)  and  the  squares  of these
primes exceed  2 1 5 , we have 313* 124911/1/.  But 1572 I a* (278 313) , so  1572\\N.  How-
ever, 57la*(27815721249), so  57\N.  But 5 7 > 2 1 5 , so  a = 78 is impossible.

At  this stage, a table  was  constructed  to list all odd prime powers which
might be components  in the remaining  cases.  For the sake of brevity, the table
and most of the remaining proofs are omitted here.  However,  the  table may be
obtained  from  the author.  The table was constructed  to include:  (1) the odd
primes that appear in Table  1 (except for  a = 78); (2) all odd primes  dividing
o*(q)9  where  q  is any other number also in Table 2 below; and (3) all allowable
powers of primes also in Table 2.  A "possible sources" column listed all com-
ponents of unreduced  denominators  in  0*(N)/N  for which a particular prime might
appear in a numerator; multiple appearances were also  indicated.

Insufficient  entries  in the  "possible  sources"  column allow us to elimi-
nate some possible components,.  For example, there are only two possible sources
for 23, so 23 3 cannot occur.  We eliminate:  2 3 3 ; 3 1 2 ; 3 1 3 ; 6 7 2 and hence 449;
712  and hence 2521; 7 3 2 ; in succession, 792,3121, and 223; successively, 101 2,
5101, and 2551; successively,  1312 , 8581, 613, and 307; successively, 1392, 9661,
4831,  1512, 877, and 439; successively, 1492, 653, 109 2, 457, 229, and 23 2; and
successively,  181 2, 16381, and 8191.

k.  REMAINING  CASES

We  have  11 ^  a ^ 46, so there can be no more than 47 odd components.  The
smallest  odd  component  must  be  smaller  than  17  because a  o*(N)/N  ratio  of
1.926...  occurs if  N is the product of  2 1 1  and the following 47 prime powers:

17,  19, 23, 25, 27, 29, 31, 37, 41, 43, 47, 49, 53, 61, 67,  73,
79, 83, 97, 101, 109, 113, 121, 131, 137, 139, 149, 151,  157,
169, 181, 191, 193, 199, 211, 241, 251, 257, 269, 271,  277,
281, 313, 331, 337, 397, 421

If  832\\N9  then  331 • 829l'ltf.  If 829 is a component, then 1657 is also, and
hence  a  ~ 46.  Now, 331 is a  component  only if  a = 15 or 6611171/, and since  a  =
46, 66111/1/.  But then  1321 \\N 9  so  a = 30, a contradiction.  Therefore, 8 3 2 cannot
be a component.

Suppose  a = 46.  Then 277 • 1013 • 1657 • 3026911/1/, so 139 * 829 • 100911/1/, hence
83 • 101ll#.  Therefore, 3^5572132  \N9  so 111121/, because  there must be a component
smaller  than  17, and a*(11) contributes another 3 to the numerator of  o*(N)/N.
Now, either  55\\N or 5 6  \\N.  If  55\\N9  then 5211171/ and we have, successively, 2 9 2 ,
421, 211, and 53 as  components;  but then  310\N9  which  is impossible.  Thus,
5S\\N9  so  601IW,  hence  431/1/*  But 431171/ or else  there are too  many 5 fs. Now,
7
31171/ .would  force 43 2 \N9  and  7h  \\N would  force  12011171/, hence  60l2\\N9  so  75\\N;
however, then  ll2\N9  a contradiction.  Therefore, we may eliminate  a  -  46.  As
a  result,  we may  eliminate 277, 1657, 829, and 30269 as components, then 139
and  1009,  and then 101.

For the sake of brevity, the other cases, except  a = 24, are summarized in
Table 2.

314  [Nov.

ON THE LARGEST ODD COMPONENT OF A UNITARY  PERFECT  NUMBER

Table 2

CASE

2^2*173

2"2*7
2"t2

2 2 6

53
2

234
233
41
2

230*61
230

2 2 5

2 1 1

2 1 3

1 2 1 5
1 2
1!**29
2

2
lk
 ELIMINATED

2^2*173

2*2*7
2"2;  1132; 1277; 71
226

532;  281;  4 7 2

2
31*;  26317; 13159; 47
2 3 3 ;  67
41
2

230*61
230

2 2 5

2 1 1

2 1 3

2 1 S ;  441; 83

2 i ^ 2 9 2

2 1 4 ; 113
 CASE

212*ll"
2 1 2*11 3

2 1 2

2 2 1*43 2

2 2 1*5

2 2 1

61
2

19
3

2 2 2*19 2

22 2

2 1 8*37 2

2 1 8*19 2

!  2 1 8*5 3

!  2 1 8*5 5

, 2 1 8*5 6

218
 ELIMINATED

2 1 2*11 4

2 1 2*11 3

2 1 2

2 2 1*43 2

2 21*5

2 2 1

612; 1861
19
3

2 2 2*19 2

2 2 2

2 1 8*37 2

2 1 8*19 2

2 1 8*5 3

2 1 8*5 5

2 1 8*5 6

2 1 8  unless  N =  W;  109

The  ordering of cases  presented  in  Table 2 works fairly efficiently.  The
reader  should  rest assured  that sudden departures  from an orderly  flow are de-
liberate  and needed.  The case  a = 24 is especially difficult, and so is pre-
sented here.
Suppose  a = 24. We immediately have 257' 67311/1/, hence 337II/V, so  132\N.  To
avoid having  N u-def, the smallest  component must be 3 5 5, or 7.

If the smallest component  is 7 9 then  97
2\\N  or else  97\\N and 7 21N.  There-
fore, 94111/1/, so 19311/1/.  Then 3211 • 1711/1/ or N is u-def.  But 33la*(l7 • 257), so
3
3\N>  a contradiction.  Thus, the smallest  component is not  7.

If  the smallest component is 3,  there are no more components = -1 (mod 3)
as 3la*(257).  Then we must have  7, 19, 25, and 31 as components or N is u-def.
But then, no more than nine more odd components are allowable, and N is u-def.
Therefore, the smallest  component must be 5.

Because 511/1/, we  must have 4311/1/, since 52la*(432).  We know that  13
2l/l/,  so
either  13
2\\N  o r 13
3ll/l/ o r  I3h  \\N.

Suppose  13h\\N.  We cannot have 5 2 or 5 6 as components, so we must have 181
and  17 3.  Starting  with  2
2tf5ll/l/, we  have,  successively, as  unitary divisors,
257 • 673, 337 • 43, 13 4, 173181 • 14281, and 192193.  Because  192\\N,  we must have
3S37\\N.  But 372la*(3913281) , contradicting  3711/1/. Therefore, 13^ is not a com-
ponent.

Suppose  133\\N.  Then  15711/1/ or else  1572\\N5  hence  52\N.  Consequently, 7911/1/
and  no  more  components = -1  (mod 5) are allowable.  Then 9711/1/ or else 97  \\N9
hence 5
2l/l/. If 73\\N$  then 43
2l/7, which  cannot be, and if  7k\\N,  then  120111/1/,  so
60111/1/, and again 43
2l/l/.  Therefore,  75\\N9 so 191II/V.  But then  N is u-def.

Hence,  132\\N9  so no more components = -1 (mod 5) are allowable.  In parti-
cular, we  must  have  9711/1/ to avoid  97
2ll/l/, and then  we  must have 3
37
3l/17. But
then  N is u-def, so a = 24 is impossible.

1987]  315

ON THE LARGEST ODD COMPONENT OF A UNITARY PERFECT NUMBER

REFERENCES

1.  M. V. Subbarao. "Are There an Infinity of Unitary Perfect Numbers?"  Amer.
Math.  Monthly  77 (1970):389-90.
2.  M. V. Subbarao  &  L. J. Warren.  "Unitary  Perfect  Numbers."  Canad.  Math.
Bull.  9  (1966):147-53; MR 33 #3994.
3.  C. R. Wall.  "A New Unitary Perfect Number."  Notices  Amer.  Math.  Soc.  16
(1969):825.
4.  C. R. Wall.  "The Fifth  Unitary  Perfect  Number."  Canad.  Math.  Bull.  18
(1975):115-22; MR 51 #12690.
 •o*o#

316  [Nov.
