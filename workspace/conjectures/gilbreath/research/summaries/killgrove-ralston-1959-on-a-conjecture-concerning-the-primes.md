> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.ams.org/journals/mcom/1959-13-066/S0025-5718-59-99262-2/S0025-5718-59-99262-2.pdf | converted from PDF -->

CONJECTURE   CONCERNING   THE    PRIMES 121

9.  I.Roman,  "An  Euler  summation  formula,  "Am.  Math.  Monthly,  v.  43, 1936, p.  9-21.
10.  H.  E.  Salzer,  "A  simple  method  for  summing  certain  slowly  convergent  series,"  J.
Math  and  Phys.,  v.  33, 1954, p.  356-359.
11.  H.  E.  Salzer,  "Formulas  for  the  partial  summation  of  series,"  MTAC,  v.  X,  1956,
p.  149-156.
12.  T.  B.  Sprague,  "On  Lubbock's  formula  for  approximating  to  the  value  of  a  life  an-
nuity,"  /.  Inst.  Actuaries,  London,  v.  18,  1874, p.  305-317.
13.  J.  F.  Steffensen,  Interpolation,  Williams  &  Wilkins,  Baltimore,  Maryland,  1927,
p.  138-148.
14.  E.  T.  Whittaker,  & G.  Robinson,  The  Calculus  of Observations,  Blackie,  London,  1924,
p.  149-150.

On  a  Conjecture  Concerning  the  Primes

By  R.  B. Killgrove  and  K.  E.  Ralston

Consider  the  sequence  {Poj}, j  =  0,  1, 2,  • • • ,  where  Po¡  is  thej'th  prime  num-
ber,  Poo  =  2,  Poi  =  3,  Po2  =  5,  • • •  .  Now  define  the  absolute  differences  of  the
primes  by  the  recursion  relation

Pa  =  | P,-i,,+i  — Pi-u  I •

The  conjecture  (Norman  L.  Gilbreath,  private  communication,  July  1958)  is
then  that  P,o  =  1  for  all  i  >  0.  The  validity  of  the  conjecture  for  the  first  few
primes  can  be  seen  from  the  following  table  of  their  absolute  differences.
2     3     5     7      11      13      17
1      2     2     4       2       4
1      0     2       2       2
i      2     0       0
1      2       0
1      2
1

There  are  an  uncountable  number  of  sequences  {boy) with  the  property  that
their  absolute  differences  6¿o defined  as  above  are  unity.  In  particular  the  sequences
[k  +  I,  k,  k,  ■ ■ ■ ]  and  any  sequence  of  the  form  {¿>oo =  1;  boy =  0  or  2,  j  >  0)
have  this  property.  Furthermore  it  can  easily  be  verified  that  any  sequence,  {&o,},
with  the  required  property  has  its  first  absolute  differences  bounded  by  the  se-
quence  [2'\,  that  is,  bu  ^  2'.
Consider  again  the  absolute  differences  of  the  primes.  Since  all  primes  greater
than  2 are  odd  numbers  it  follows  that  all  differences  P,y,  j  >  0,  are  even  numbers.
Now,  if  for  some  i  and  all  j,  0  <  j  <  M,  we  have  PtJ  =  0  or  2  and  P,o  =  1,  then
all  of  the  differences  that  derive  from  them  will  be  bounded  by  2,  from  which  it
follows that
 Pt',0  ,  Pj+1,0  ,  Pi+2,0  i   " '  "   i   "t+Jf-1,0    =    I-

We  now  define  the  function  P(i)  to  be  the  largest  integer  M  such  that  P,3  ^  2
for  all j  <  M.  Thus  we  can  say  that  Pko  =  1 for  i  ^  k  <  P(i)  +  i.
A  routine  was  coded  for  the  SWAC  to  evaluate  this  function  P(i),  using  the
primes  less  than  792,722  from  a  sieve  prepared  by  D.  H.  Lehmer.  The  results  of

Received  Oct.  7,  1958.  The  preparation  of  this  paper  was  sponsored  by  the  Office  of  Naval
Research.  Reproduction  in  whole  or  in  part  is  permitted  for  any  purpose  of  the  United  States
Government.
 122 D.   S.   STOLLER   AND   L.   C.   STOLLER

this  calculation  are  shown  in  the  following  table.  From  these  results  it  is  seen  that
the  conjecture  holds  for  all  primes  less  than  792,722,  which  amounts  to  the  first
63,419 primes.
 Table  of  the  Function  P(i)   for  0  <  i  <    95

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
21
22
23
24
25
26
27
28
29
30
31
32
 P(i)

3
8
14
14
25
24
23
22
25
59
98
97
98
97
174
176
176
176
176
291
290
289
740
874
873
872
873
872
871
870
869
868
 i>(«) + »

4
10
17
18
30
30
30
30
34
69
109
109
111
111
189
192
193
194
195
311
311
311
763
898
898
898
900
900
900
900
900
900
 33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56

*[excerpt ends; 1260 characters not shown — see `research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`]*
