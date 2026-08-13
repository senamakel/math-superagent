> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/wall-1987-largest-odd-component.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 8304 characters not shown — see `research/sources/wall-1987-largest-odd-component.full.md`]*
