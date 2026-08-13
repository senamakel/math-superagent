<!-- source: https://mathstat.dal.ca/FQ/Scanned/13-4/singmaster.pdf | converted from PDF -->

REPEATED  BINOIVHAL  COEFFICIENTS  AND  FIBONACCI  NUMBERS

DAVID  SINGMASTER
Polytechnic of the South Bank, London and Istituto  Matematsco, Pisa, Italy

ABSTRACT

In this note, I show that there are infinitely  many solutions to the equation
(
n + 1 ) - f
  n ) [k+  1  ]  \  k+2  J  '

given by n = F2j+2F2i+3  ~  h  k
 =  ^2l^2i+3  ~  ^  where Fn  is the n
th  Fibonacci number, beginning with  F0  = 0. This
gives  infinitely  many  binomial  coefficients  occurring  at  least  6 times. The method  and results of a computer search
for  repeated binomial  coefficients, up to  248:, will  be given.

1.  INTRODUCTION

In  [ 6 ] ,  I  have conjectured  that  the  number  of  times  an  integer can occur  as a binomial  coefficient  is bounded. A
computer search up to  248  has revealed only the following seven nontrivial  repetitions:
120- ( ' / ) - ( ' / ) ;  ™ - ( ? ) - ( y ) ;  ' * * - ( ? ) - ( ? ) ;

7140=  ( ' f  ) -  ( * ) ;  11628-  ( ' f  ) -  ( j ) ;  « , » - ( * ' ) -  ( ' / ) ;

3003-  ( ? ) . ( y ) - ( y ) .

In  [ 2 ] ,  it  has been shown  that  the  only  numbers which are both triangular,  i.e., =  (  "  )  for some n, and tetrahe-

dral,  i.e.,  =  I"  )  for  some n,  are  1, 10,  120,  1540  and  7140. The first two  are trivial  and the last three were also
found  by the computer, giving a check  on the search procedure.
The coefficient  3003 occurs in the following striking pattern  in Pascal's triangle:

1001  2002  3003
3003  5005

8008

I  had noticed this pattern some years ago when  I discovered that  it  is the only solution to

( z ) ; U " 0  • • ( *"*) - , : ' ; 5 -

and  that  there  is at  most  one  solution  to  this  relation  when the  right-hand side is replaced by a : h :  c.  Hence  I was
led to  consider  determining  solutions  when the  right-hand  side was a  :  b  :  a+b,  or, equivalently and more simply,
solutions of  /  \  /  \
(1)  [V+1  )
  =  \k+2)'

2.  SOLUTION  CF  EQUATION  (1)

From  (1), we have (n + 1)(k+2)  =  (n-k)(n-k-  1). Setm = n + 1,j=  k + 2, thus obtaining m
2 +(1-3j)m  +
p  -  j  = O.  Solving for/77 gives  295

296  REPEATED  BINOMIAL  COEFFICIENTS  AND  FIBONACCI  NUMBERS  [DEC.

(2)  m  =  [-1+3ii*J~$F~=7jTT]/2  .

For this to  make sense, we must  have that 5p  -2j+  1  is a perfect  square, say s/
2. We can rewrite this as

(3)  (5j-  1)2  -5v2  =  -4.

Letting u = 5j -  1,C = -4,  we have the  Peli-like equation

(4)  u2  ~5v2  =  C.

This can be completely  solved by standard techniques  [5, section 58, p. 204 f f ] .  The basic solutions are:

9 +  4V5"whenC=  1;  2 +y/E  when £  = - 1 ;  and  1 j-%/5  and 4 + 2^5" when C = - 4  .

The  class of  solutions  determined  by  4 +  2^JB  is the  same as the class determined  by 4 -  2\/5,  i.e.,the class Is a m -
biguous, in the terminology  of  [ 5 ] .  Hence all solutions are given by

u-x  + v-rJ5  =  (-1  + y/5)(9  + 4y/5)'',  u,- + vgy/S  =  (1 + s/5)(9  + 4^/5  ) ' \  u/  + v,y/5  -  (4  + 2S/B)(9  +  4^/s)1',

and their conjugates and negatives.
Let F0  = 0, Fx  =  1, Fn+<j = Fn  + Fn„f  define the  Fibonacci  numbersand  iet£,0  =2,  Lx  =  1, Ln+f  -  Ln  + Ln„i  de-
fine the  Lucas numbers.

Lemma.  (Ln  + Fn^5)(9  + 4^/s)  =  Ln+6  + Fn+&sf5  .

Proof.  Let a=  (1+>j5)/2,  /? = (1 -  \fE)/2.  By the  Binet formulas, we have

Fn  =  (an-pn)/sj5,  Ln  -  an+Pn,

and so Ln  + Fns/5  = 2an.  Hence the lemma reduces to showing a6  = 9 + 4>j5,  which is readily done.
Since the  basic solutions u0  + vQ\f5  given above are respectively

L„.t  +  F-i>j5.  Lx+FlS/E  and  Ld+FdS/5,

the general solution  of  (4) can be written as

(5)  L2j-1  + F2i-I>j5,  i = 0 , l -

and we may now  ignore the conjugates and negatives.
To  solve  (3),  we  must  have 5 / -  1 =  L21-1.  From the  Binet formula, one may obtain  L/^2-31  (mod  5) and hence
£/ =  - 1  (mod 5)  if  and only  if/  =  3  (mod 4).  Recalling t h a t / -  k + 2  >2,  the solutions of  (3) are thus

/  =  (L4i+3  +  1)/5,  v  =  F4j+3,  1 =  1, 2,  - .

By standard  manipulations, we obtain

(6)  / =  F2jF2i+3  +1,  k = F2jF2j+3  - I  ™  =  F2J+2F2j+3=  (L4i+5  -  1)/5,  n = F2l+2F2l+3  ~  1.

Finally, observe that
 ( * ) • •  ( * " / )  =(k+1):(n-k)  =  F2i:F2i+1,

(  *  )  •'  \ k " l )  :  \kl2J  =  f 2 / •' F21H  = F2i+2-

The case/ =  1 givesn=  14, k~  4 and  ( ' / ) •  ( y ) - * » -
The case i = 2gives n=  103,  k = 38,k  + 2 = 40, and

(7®g)  =  (  1°j*  )  =  6121818274330470189  14314  82520.

This number does not occur again as a binomial  coefficient. The next values of  (n,k)  are  (713, 271) and  (4894, 1868).
Equation  (1)  has also been solved  by  Lind  [ 4 ] .  Hoggatt and  Lind  [3]  have dealt with some related  inequalities.

hence

1975]  REPEATED  BINOMIAL  COEFFICIENTS  AND  FIBONACCI  NUMBERS  297

3.  REMARKS

The  coefficients  - ( " » : ; )  • ( - » ) - ( 7 )

give us infinitely many binomial  coefficients occurring at least six times. This has also been noted  in  [1,  Theorem  3 ] .
Since  3003  happens to  be also a triangular  number,  one  might  hope that  some  more  of  these values might also be
triangular.  I first determined  by calculation  that  Cs)

was not  triangular  and  later  I  determined  that  it  did  not  occur  as any other binomial  coefficient. These determina-
tions are described  below.  I have not been able to  discern any other  patterns  in the repetitions found.
One might try to  extend the  pattern  of  Eq. (1) and try  to  find
I  "  \  « [
n  + 1 \  =  tn+2\
\  k+4  )  \  k + 3  )  \k+2  )  '

This would require two  solutions of  (1) with  consecutive values of n  and inspection of  (6) shows this  is impossible.
The lemma is a special case of  the general assertion that the solutions uj,  i/; of

UJ + v/y/5  =  fu0  + v0^D  Ha +  b^/D)'

both satisfy the same second-order recurrence relation:

un+i  =  2aun  + (b
2D  -a
2)un„i.

(In  our  particular  case: Fn+Q=  18 Fn  -  Fn-6.)  I do not see whether the fact that  the three basic solutions  happen
to  neatly fit  together  into  a single linear  recurrence is a happy accident or a general phenomenon. The converse prob-
lem  of  determining  which  pairs  of  recurrence relations give all solutions of  a Pell-like equation seems interesting but
I  have not examined  it.  4.  THE  COMPUTER  SEARCH

Two  separate  computer  searches  were  made.  First  an  ALGOL  program  was  used  to  search  up  to  223  on  the

London  Polytechnics'  ICL  1905E.  All  the  4717  binomial  coefficients  (  £  \  with  k>2,  n > 2k  and less than  223

were  formed  by  addition  and  stored  in  rows  corresponding  to  the  diagonals  of  Pascal's triangle. As each new coef-
ficient  was  created, it  was compared  with  the  elements  in the  preceding  rows. Since each row is in increasing order,
a simple  binary  search  was done  in  each  preceding  row  and the process is quite quick.  All the repeated values given
in the  Introduction  were already  determined in this search.
The  second  search  was carried  out  using a  FORTRAN  program  on  the  University  of  London  Computer  Centre's
CDC  6600.  Although  the  6600  has a 60-bit  word,  it  is difficult  to  use integers bigger than 248  and overflow occurs
with  such  integers.  Consequently,  I was only able to  search up to  2 4 8. There are about  24 x  10
6  triangular  numbers
and  about  12  x  104  tetrahedral  numbers  up to  this  limit.  It  is impractical to store all of these, so the  program had
to be modified.  Fortunately, the results of  [ 2 ] , mentioned in the  Introduction, implied that we did not  have to com-
pare these two  sets.  I wrote  a subroutine  to  determine  if  an  integer  N  was triangular  or tetrahedral. This estimates
the J  such that J(J  +  1)/2=  l\(hyJ=  fsf(2N)]  -  /  and then computes the succeeding triangular  numbers until  they
equal  or  exceed  N. Two  problems of overflow  arose.  Firstly:  if  N  is large, the calculation of the first triangular num-
ber  to  be  considered,  i.e., J(J  +  1)/2,  may cause an overflow when J(J +  1) is formed. This was resolved by examin-
ing J  ( mod 2) and computing either  (J/2)(J+  1) or jm  •

Secondly:  if  N  is  larger  than  the  largest triangular  number  less than  2 4 8, the calculation of the successive triangular
numbers  will  produce  an overflow  before  the  comparison with N reveals that we have gone far enough. This was re-
solved  by  testing the  index  of  the triangular  numbers to  see if  overflow was about to  occur. The test for  tetrahedral
numbers was similar, but  requires testing J  (mod 6).

298  REPEATED  BINOMIAL  COEFFICIENTS  AND  FIBONACCI  NUMBERS  DEC. 1975

The search then  proceeded  much as before.  AN coefficients  /
  n
k  \  with  k >  4 and n > 2k and less than 248
  ware
formed  by addition  and  stored  in rows. As each  coefficient  was formed, the subroutine  was used to see if it was tri-
angular or tetrahedral and binary search was used to see if it occurred  in a preceding row.
S  was rather  startled  that the second search produced no new results. The results 210,11628, 24310 and 3003 were
refound,  which  gave me some confidence  in the process,  i reran the program  with  output of the searching steps and
this  indicated  that  the program  works  correctly.  So I am reasonably sure of the results, although still startled. I hope
someone can extend this to higher limits, say 259
 and see if there are more repetitions.

The  calculation  of N -  (  j l 3 ]  and the computational  determination that it was not triangular were also compli-

cated  by overflow,  since N >  2
4i.  First  I attempted  to compute  only  the 103rd
  row of the Pascal triangle by use of

/  103  \  =  104-  k  I  103 }
{  k  I  k  \k-  1  J

using double  precision  real  arithmetic.  However, this  showed  inaccuracies  in the units place, beginning with k~  33. I
then  computed  the entire triangle  up to the 103rd  row (mod 10
14)  by addition. I could then overlap the two  results
to get N. The double precision calculation had been accurate to 27 of the 29  places.
I  applied the idea of the  subroutine to  determine  if N were triangular. This required some adjustments. Since 2N is
bigger  than  2 9 6, one cannot truncate  V5/v7  to an integer.  Instead sJ(N/2)  was calculated, truncated  to  an integer,
converted to a double precision  real and then doubled. Then the process of the subroutine was carried out, working in
double  precision  real form. N was found to  lie about halfway  between two consecutive triangular  numbers. These re-
sults for N were independently  checked by Cecil  Kaplinsky  using multiprecision arithmetic  on an IBM 360.

In a personal letter,  D. H. Lehmer pointed out that one could determine that N was not triangular by noting its resi-

due  (mod 13). Following up on this suggestion, I computed the Pascal triangle  (mod/?) for small primes. Since  (
  n
k  J

(mod p)  is periodic as a function  of n  [1, Theorem  38; 8; 9] , one can deduce that N ?  f  £  1  for various k'% by ex-

amination  of N  (mod p)  and the possible values of  ( J M  (mod p).  For example, N = 4  (mod  13), but  f  "A  £ 4

(mod  13) for k = 2, 4 , 6 , 7, 8, 9, 10, 11, 12. Using the primes 13, 19, 29, 31, 37, 53, 59 and 61, one can exclude all

possibilities for kf  other than 39 and 40 and hence N occurs exactly six times.
On the basis of the computer search and the scarcity of solutions of (1), I am tempted to make the following:
CONJECTURE. No binomial  coefficient  is repeated more than  10 times. (Perhaps the right number is 8 or 12?)

REFERENCES

1.  H. L  Abbott,  P. Erdos and  D. Hanson, "On the Number  of Times an Integer  Occurs as a Binomial  Coefficient,"
Amer. Math, Monthly,  81 (1974)', pp.  256-261.
2.  E.T. Avanesov, "Solution of a Problem on  Figurate Numbers," Acta Arith.,  12 (1966/67), pp. 409-420. (Russian).
See the review: MR 35, No. 6619.
3.  V.  E.  Hoggatt,  Jr., and D, A.  Lind, "The Heights  of  Fibonacci  Polynomials and an Associated  Function," The
Fibonacci Quarterly,  Vol. 5, No. 2 (April, 1967), pp. 141-152.
4.  D. A.  Lind, "The Quadratic  Field  #(>/5)and  a Certain  Diophantine  Equation," The Fibonacci Quarterly,  Vol. 6,
No.  1 (February  1968), pp. 86-93.
5.  T. Nagell, Introduction  to Number  Theory, 2nd ed., Chelsea PubL Co., New York,  1964.
6.  D. Singmaster,  "How Often  does an  Integer  Occur as a Binomial  Coefficient?" Amer. Math. Monthly,  78 (1971),
pp. 385-386.
7.  D. Singmaster, "Divisibility  of Binomial and Multinomial  Coefficients by Primes and Prime Powers," to appear.
8.  W.F. Trench, "On Periodicities of Certain Sequences of Residues," Amer. Math. Monthly,  67 (1960), pp. 652-656.

9.  S. Zabek, "Sur la periodicite  modulo  m des suites de nombres  (  "  ). Ann.  Univ. Mariae Curie-Ski odowska Sect
A,  10  (1956), .pp. 37-47,
  X  J

The  final  preparation  of  this  manuscript  was supported  by  an  Italian  National  Research  Council  research  fellowship.
