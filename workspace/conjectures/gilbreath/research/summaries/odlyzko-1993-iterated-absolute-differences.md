> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/odlyzko-1993-iterated-absolute-differences.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf | converted from PDF -->

mathematics  of  computation
volume  61, number  203
july  1993, pages  373-380

ITERATED  ABSOLUTE  VALUES OF  DIFFERENCES  OF
CONSECUTIVE PRIMES

ANDREW M. ODLYZKO

Dedicated  to the  memory  of D. H.  Lehmer

Abstract.  Let  dç,(n)  =  p„  ,  the  nth  prime,  for  n  >  1 ,  and  let  dk+x(n)  =
\dk(n)  -  dk(n  +  1)|  for  k  >  0,  n  >  1 .  A  well-known  conjecture,  usually
ascribed  to  Gilbreath  but  actually  due  to  Proth  in  the  19th  century,  says that
dk(\)  =  1  for  all  k  >  1 .  This  paper  reports  on  a  computation  that  verified
this  conjecture  for  k  <  tt(1013)  »  3 x  10"  .  It  also  discusses  the  evidence  and
the  heuristics  about  this  conjecture.  It  is very likely that  similar  conjectures  are
also valid  for  many  other  integer  sequences.

1.  Introduction

Let  pi  =2,  p2 =  3,  ...    be  the  primes  in  their  natural  ordering,  and  set

do(n)  =pn,         n>\,

dk+x(n) =  \dk(n)-dk(n+l)\,         k>0,n>  1.

Table  1 (next page) shows  dk(n)  for  0  <  k  <  20,  1 <  n  <  20.  Note  that
dk(l)  =  1  for  1 <  k  <  20.  As was pointed  out by H. C. Williams, Proth  [15]
claimed  to  prove  that  dk(l)  =  1  for  all  k  >  1,  but  his  proof  was  faulty.  More
recently,  Gilbreath  (unpublished)  independently  conjectured  that  dk(l)  — 1  for
all  k  >  1 .  (See Problem  A10  in  [7], and  also  [8].)  This  is usually  referred  to  as
Gilbreath's  conjecture.
Gilbreath's  conjecture  was  verified  for  k  <  63,419,  that  is  for  all  primes
<  792,731  , by Killgrove and  Ralston  [8], who were fellow students  of Gilbreath
at  UCLA  in  the  late  1950s.  This  paper  reports  on  a verification  of  this  conjecture
for  all  primes  <  1013,  so  that  dk(l)  =  1  for  1  <  k  <  3.4  x  1011 .  The
computational  results  are  presented  in  §3,  and  the  algorithms  that  were  used
are  described  in  §4.
For  a  general  sequence  do(n),  to  compute  dk(l)  it  is  necessary  to  compute
dj(i)  for  all  i + j  <  k +  1,  so that  for  k  ~  3.4 x  10"  approximately  5 x  1022
numbers  have  to  be  computed,  far  too  many  for  the  technology  of  today  or  the
near  future.  The  computations  for  d0(n)  -  pn  were possible  because  of  special
properties  of  the  primes.  Note  that  dk(l)  is  odd  and  dk(2),  dk(3),  ...  ,  are
even  for  all  k  >  1 .  If  for  some  A^ we  find a  K  such  that  dfc(l)  -  1  while
dn(n)  =  0  or  2  for  all  1 <  n  <  N,  then  we  can  conclude  that  dk(l)  =  1  for
K<k<N  + K-l.  Let  C7(7V) denote  the  minimal  k  (if it  exists) such that
dj(l)  =1  for  1 <  j  <  k  and  dk(n)  =  0  or  2 for  1 <  n  <  N.  Computations

Received by the editor  July  15, 1992.
1991 Mathematics Subject Classification. Primary 11N05, 11Y99; Secondary 11K36, 11Y16,
68Q25.
 373  ©1993  American Mathematical Society
0025-5718/93 $1.00+  $.25 per page

374 A.  M.  ODLYZKO

Table  1.  Iterated  differences  dk(n)  for  0 <  k  <  20,  1 <  n  <  20

k\n

0

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
 10    11    12    13    14    15    16    17    18    19    20

13    17    19    23    29    31    37    41    43    47    53    59    61    67    71

show  that  G(N)  does  exist  for  all  N  that  have  been  checked  and  is  small.
Table  2  presents  some  values.  (Similar  observations  have  been  made  before,
cf. pp. 34-35 in [17].)
A  rigorous  proof  of  Gilbreath's  conjecture  appears  out  of  reach,  given  our
knowledge  of  primes.  Maximal  gaps  between  consecutive  primes  around  x  are
thought  to  be  not  much  larger  than  (logx)2.  (There  is a  conjecture  of  Cramer
[5] that  these  gaps  are  0((logx)2),  and  numerical  evidence  [3, 4,  20]  supports

*[excerpt ends; 16627 characters not shown — see `research/sources/odlyzko-1993-iterated-absolute-differences.full.md`]*
