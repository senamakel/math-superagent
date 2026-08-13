<!-- source: https://www.fq.math.ca/Scanned/33-4/glaser.pdf | converted from PDF -->

DUCCI-SEQUENCES AND PASCAL'S TRIANGLE

Herbert  Glaser

Mathematisches Institut (Didaktik), Universitat Wurzburg, Germany

Gerd Schoffl
Korngasse  1, 97070 Wurzburg, Germany
(Submitted November  1993)

INTRODUCTION

The  so-called  Ducci-sequences (or  n-number-game) have  recently  been  studied  by  several
authors in this review (see [1] , [5], [6], [12], [17], and others).  A Ducci-sequence is a sequence
of w-tuples  Aj = (aha2,  ...,a„); the first w-tuple  4)  is any given n-tuple with nonnegative  integer
entries,  4+1 •= 2T4? where  2T is defined  as follows:

2T4  :=(\al-a2l\a2-a3l...,\a„-al\).

The w-tuple  Ai+l  is called the (direct) successor of  4 ,  whereas  4  is the predecessor  of  Ai+l.  As
the maximum  entry  of the w-tuples cannot increase under the  application  of  2T  and therefore  the
number  of  successors  of  any  4)  *
s bounded,  the  sequence  always  leads  to  a  cycle  of  repeating
w-tuples  or  to  the  n-tuple  (0,..., 0).  If  an w-tuple  4)  gives rise to  the  latter,  it  is usually  called
vanishing.
First,  it will be shown in this article that the Ducci-sequences  are closely related  to Pascal's
triangle  and  many  properties  of  their  cyclic  structures  can  be  found  and  proved  considering
Pascal's triangle modulo 2.  In the second part we will examine whether, for  a given n GN there is
such anMthat  2
M  = - 1 mod n, which is crucial for some properties of the Ducci-sequences.
We would like to thank the referee for a number of valuable suggestions.

SOME BASIC PROPERTIES AND DEFINITIONS

It  is  a well-known  fact  that  every «-tuple  with  integer  entries vanishes  if  and  only  if n  is a
power  of 2 (e.g.,  [4]).  On the other  hand, the ^-tuples in the  cycles of the Ducci-sequences  are
constant multiples of binary ^-tuples ([6], [3]).  As 2T(/L4) = X^FA  for  every  X GN0,  we can limit
any investigation of cycles to n-tuples over Z2.  Since \a -  b | = (a + b)  mod 2 for  all integers a and
ft,  we can use the linear operator  2) instead of 2T, where  Q)A : = {ax + a2, a2 + a3,..., an + a{)  mod 2
and A  is a binary 7?-tuple.  The operator  2  can be written as the sum of two linear operators over
Zj*.  2) = 3 + K,  where  $  is the identity and  KA  := (a2, ...,an,  a{).  Obviously, we get  W  = $  and
2T
1
  = ye~\  where X"1 is the inverse operator of  K.
We  denote  the  k^  successor  2^4)  °f
  a  gi y e n  binary  w-tuple  4)
  a s  A  •  ^  ^
  ls  necessary
to describe the entries of a certain successor  Ak,  we will use two indices and write  Ak  = (akly  ...9
aki„).  Then we get:
 4fc+U
  =ak,i
  +ak,i+l-

The subscripts denoting the place in the ^2-tuple are always reduced  modulo n, using n instead  of
0.

1995]  313

DUCCI-SEQUENCES AND PASCAL'S TRIANGLE

Ehrlich  proved  in  [6] that  the »-tuple  AQ = (0,..., 0,1)  (and  every cyclic permutation  of  AQ)
produces a cycle of maximum length.  The length of all other cycles of n-tuples of a given n divide
this  maximum.  The  sequence  {Ak}  is  called  the  basic-Ducci-sequence {of  n-tuples)  and  the
length  of its periodic  cycle is denoted  as  2P(»).  For  every  odd  n,  the first «-tuple  in  a  cycle is
2)4) = Ax = (0,..., 0,1,1).  Further, Ehrlich stated the following theorems:

\i1
m  = \  mod n, then <3>{n)  divides 2
m
  - 1 .

If 2
M  & - 1 mod n, then #>(«) divides n(2
M  -1).

If n is not a power of 2, then n divides 2P(«).

If»  = 2
rl,  where £  is odd, then 2P(«) = 2
r<3>(£).
 (1)

(2)

(3)

(4)

Before  we take  a closer  look  at the  properties  of Pascal's triangle,  we will  state  a theorem  that
allows a new approach to our problem.

A NEW APPROACH TO AN OLD PROBLEM

In Pascal's triangle, we find  the binomial  coefficient  (f)  of the  ?
th  place in the  k
th  row.  The
0
th  row consists of a single one.  When we place zeros left  and right of the triangle, we can obtain
any element by adding the two elements to the left  and right above its place.  This is easy to see,
knowing the formula for adding the binomial  coefficients:

k
z + 1  £ + 1
i + l

We will limit our investigation to  Z2, and thus every binomial coefficient  shall be considered
modulo  2.  Pascal's triangle modulo  2 with n  rows  (i.e., row  0 to  row  n-\)  will be  denoted  as
PTn.  The number of a chosen row shall be denoted  as k.  We fill up every k^  row of a PTn with
n - k -1  zeros on the left  side.  By shifting  to the right  and considering the rows  as w-tuples, we
obtain a square of n different  w-tuples.
 0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0 / 1
0  0 / 1  1
0/1  0  1
A l l !
 0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0 0  0/4"
0  0/1  1
0/1  0  1
A  i  i  i
0  0  0 / 1
0  0/1  1
0/1  0  1
/ f i l l
 0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0 / 1
0  0 / 1  1
0 / 1  0  1
A  i  i  i
0  0  0  0
0  0  0  0
0  0  0  0
0  0  0  0
o  o  oA
0  0/1  1
0/1  0  1
A  i i i
 0  0  0/41
0  0/1  1
0 / 1  0  1
A  i  i  i
0  0  0/L
0  0/4  1
0 / 1  0  1
A  i  i  i
0  0  0 / 1
0  0/1  1
0 / 1  0  1
A  i  i  i
0  0  0 / 1
0  0/L  1
0 / 1  0  1
A  i  i  i

314  [AUG.

DUCCI-SEQUENCES  AND PASCAL'S TRIANGLE

The 7
th entry in the k
th  row will be denoted as ak>i. We obtain:

JO  \  \<i<n-k-\

fl*''
  = lG4J  -n-k<i<n.

Adopting the above formula for the binomial coefficients,  we get ak+lJ  = akJ  +  akJ+l:

•  \<i<n-k-2:ak+li=0  =  akJ+akJ+l.

•  w-& <i  <rc:ak+lJ  =(._£J+1) = ( , 4 J  + (._^+1) = a M  + aM+1.

Considering that the ?i-tuple in the  0
th  row is  (0,..., 0,1) =  AQ,  the first /2-tuple of the basic-
Ducci-sequence, we have shown

Theorem  1:  The n rows in the modified Pascal triangle (as shown above) are the n-tuples  AQ,  Au
...,  An__l  of the basic-Ducci-sequence.

We will now take a closer look at Pascal's triangle.  This triangle shows an interesting geom-
etry which  is  closely related  to  that  of the  Sierpinski  gasket  (cf.  [14]).  Therefore,  the  PTr  for
r  GN  can  be  constructed  recursively.  For  a  given  PTr,  r  GN,  we  get  PTr+i  by  placing  two
Pier's at the corners of the base of the first PTr  and filling up the empty triangle with zeros:

2 r + l

This construction can be proved using a lemma of Hinz  ([8],  p. 541).

Lemma  1:  For  0 < k, i  <  2\  and r  GN0,  it follows that

(
2
7*M<)
mod2
'

In  [8] we  can find some  additional  facts  that  have been  stated  by Lucas  [10]  and  Glaisher
(reference  can be found  in Stolarsky  [16])  and can be proved  with the help  of the  above  lemma

([8],  p. 539):

•  For  0 <  i  < k,  the binomial coefficients  (*) are all odd if and only if k  =  2
r -1  for
some r  GN0.  (5)

•  For  0 <  i  <  k,  the binomial coefficients  (J) are all even if  and  only if A: is a power
of 2 (the outer elements are 1).  (6)
•  Let  fi(k)  be the  number  of ones in the  2~adie  expansion  of  k  GMQ.  Then  the
number of odd binomial coefficients  (J) for  0 <  i < k  is 2^
(/c).  (7)

1995]  315

DUCCI-SEQUENCES  AND PASCAL'S  TRIANGLE

The advantage of using PTn for examining the Ducci-sequences is the fact that many properties of
the  cycles can easily be seen.  Regarding the fractal  geometry  of the triangle,  the results  can be
observed for small n and generalized for higher ones.  For example, if we take a look at the PT2r,
we see that the row 2r -  1 contains only ones.  This leads us to an easy proof of the  well-known
fact that every 2r-tuple with integer entries vanishes (see [4], [7], [3], et al.).
In the same way, we can prove all the following new results.  As some of the proofs are quite
long when using exclusively Pascal's triangle, we will adopt other techniques as well.

CYCLES OF SOME  DUCCI-SEQUENCES

Following Ehrlich  [6], we say n is with  a -1 if n GN  is odd and there exists a n M e N  with
2
M  = - 1 mod n; otherwise, we call n without  a  -1.  We will now give a lower bound  for  ^(n)
for every n with a -1 [for an upper bound, see (2)].  First, we have to state the following lemma.

Lemma  2:  Let n be with a -1 and k  eN, k > 1.  Then

2>*
(2W
~
1)+1
 =  9 r t > .

Proof:  We proceed by induction using Ehrlich's Lemma  1 ([6], p.  302):

2
m^tmodn=><3)
2m  =$  +  W!.

Let k  = 1.  Then we get
 3 ( 2 - - I H I  =  # " = £  + ^ 1  =  ^ 1 3 , .

Assume now that the statement is true for k  GN.  It follows by computation that

This lemma leads to

Theorem  2:  For n with a  -1,  every cyclic permutation  of Ax = (0,..., 0,1,1)  can be found  in the
basic-Ducci-sequence.

Proof:  As n  is  odd, the w-tuple  Ax is the first w-tuple  in the  cycle  of  the basic-Ducci-
sequence and Ax = 2)(0,..., 0,1).  Using Lemma 2 above, we obtain  2J*(2A/"1)+14, = ^C
k2bA<j  and
therefore
  (db
K2M~
l)Al  =  ^CkA1 for every k eN.  D

Obviously this result implies that, for every n with a -1,  the cyclic permutations of (0,..., 0,1)
give rise to the same cycle, and so there exists only one cycle of maximum length.

Theorem 3:  For n with a -1,  we get ?P{n)  > n(n - 2).

Proof:  We have to determine the minimum  number  of applications  of 2)  for obtaining the
first cyclic permutation of Al in the basic-Ducci-cycle.  We use Pascal's triangle.  A permutation
of  Ax  consists of two adjacent  ones (where alx  and aln  are considered as being adjacent  as well).
Since the last and the first entry of Pascal's triangle are always ones, the number of ones in every

316  [AUG.

DUCCI-SEQUENCES  AND PASCAL'S TRIANGLE

row Is at least 2.  Thus, we can (possibly) find a cyclic permutation  of  Ai  for the first time when
the  first  and  the  last  entry  of Pascal's triangle  can be considered  as adjacent  ones in  an  «-tuple,
which  is  to  say  that  akl  = \.  Regarding  the  construction  of  ^-tuples  from  Pascal's  triangle,  it
follows that k = n-l9  that means after  n-2  applications of 2) on  Ai.  We use the same argument
for the successors of the first permutation of  Ax,  and the proof is complete.  •

This theorem gives rise to an important result.

Theorem  4:  For n with a -1,  it follows that

(3>(n) = n(n-2)on  = 2r+l,  r  eN.

Proof:
"<="  Ifrc = 2r + l,then  2
r = n-l  = -l  mod n and from  Theorem 3 we get  ^P{n)>  n{n-2).
On the other hand,  &(n) divides n(2
r -1) = n(n -  2)  [see property (2)], and so n(2
r -1)  = n(n -  2).
"=>"  As n is with a  -1,  the proof of Theorem 3 shows that tyQi) = n(n-2)  if and only if the
w-tuple  An_l is a permutation  of  Av  According to properties  (6) and (7), we  obtain  exactly two
ones in a row of Pascal's triangle if and only if the number of the row is of the form  2
r +1.  Con-
sidering that the ones are adjacent  if and only if the w-tuple that is formed  from  the row  2r +1  of
Pascal's triangle is not filled up by zeros, i.e., n = 2
r +1, we have shown our statement.  D

Furthermore, we can extend Theorem 4 for every even n with n = 2
r + 2
s.

Theorem  5:  If n = 2
r +2
S for r > s> 0, then 9(n)  = *n~£*l).

Proof: By using Theorem 4 and Ehrlich's formula (4), we obtain

2P(2r+20 = 2^(2r"* + l)

= 2*(2
r-* + l)(2r-*-l)

^ ( 2 r  + 2')(2 r-2')
2
s

=  n(n-2
s+l)
2
s  '

As  mentioned  above,  Ehrlich  [6]  was  able to  describe  the  first  w-tuple  in  the  cycle  of  the
basic-Ducci-sequence if n is odd.  Nothing is yet known about the case in which n  is even.  We
will be able to give a partial solution at this time.

Theorem  6:  For n -  2
r + 2\  r > s > 0, the /i-tuple

^ = ( 0 , . . . ,  0,1,0,. ..,0,1)

n-2
s-l  2 5+l

is the first «-tuple in the cycle of the basic-Ducci-sequence.

Proof:
1.  The w-tuple is contained in the cycle.

Pascal's triangle PTn shows us that

1995]  317

DUCCI-SEQUENCES  AND PASCAL'S TRIANGLE

4 ,  = ( 0 ^ , 1 , ( ^ 0 , 1 )

2 2 - l  2 r + l
is a successor of  4 ,  = ( 0 ^ , 1 , 0 ^ , 1 ) .

2 r - l  2s_x

Obviously,  Ar  is a cyclic permutation of Ar:  ^  = HC2 Ar.  On the other hand, we have  Ar  =
2)
2 ~
2 ^ 2 J.  We can conclude that
 Q^Ar=K-
nA2S  = Ar

and, therefore,  Ar  is contained in the cycle.  Keeping in mind that the first  and the last  entry of
PTn are always  1, and counting the consecutive zero-entries, we obtain that  Ar  is the only cyclic
permutation of A2,  among its successors  A^  ,..., Ani which are contained in the (modified) PTn.
Therefore, we have even shown that  Ar  is the first  of the cyclic permutations of A^  that  appears
in the cycle.

2.  Ar  is the first «-tuple in the cycle.

The n-tuple Ari  is the predecessor of A%s.  We suppose that  Ar_x  is contained in the cycle.

It follows from above that the predecessor  A^,  i.e., Ar_v  is in the cycle.  Therefore,  A^  must

be a cyclic permutation of ^ 2 M -  A look at PTn shows that  A2,  contains  2s  ones, and in A^

we can find 2r ones [see property (7)].  This is a contradiction to the assertion, as r > s.  •

Corollary 1:  If n -  2r + 2\  r > s > 0,  then there are 2s  different  cycles  of maximum  length  that
are produced by the cyclic permutations of the w-tuple AQ.

Proof:  The operators 2) and W commute, so

®
r-
rAr=®
r-
rX-
rA2S
=  K-
r®
r-
rAr='X-
2-
2°Ar.

By induction, every w-tuple Wn  A s,  £ GN, appears in the cycle of the successors of (0,..., 0,1).
Using the same argument as in the proof of Theorem 6, we conclude that for every  £  the n-
tuple  $£"^
+1)
2 Ar  is the first cyclic permutation  of ^Cn  A^  among the successors  of the  latter.

As 2
5|2P(«), no other cyclic permutation than the ones described above can be found  in the cycle
produced by (0,..., 1).
We use the same technique for the successors of %C
1A0,
  <%C2 A$,...,  K~r+1 AQ .  D

We  will  now consider  2r -1-tuples.  Using  Pascal's  triangle,  we  can  determine  &(ri) for
n =  2r-l.

Theorem 7:  If r  GN  and n = 2r -1,  then 2P(«) = n.

Proof: Using the proof of Theorem 3, we see that no cyclic permutation of Al can be found
in fewer than (n -  2)  steps.  Pascal's triangle shows that

318  [AUG.

DUCCI-SEQUENCES AND PASCAL'S TRIANGLE

^ = ^ 2 4 = a 0 , 1 , 0 ,  ...,i,o,i).  ,

Then 4  = (1,1,..., 1,0) and4,+1 = (0,0,..., 1,1) = 4 .  •

Corollary 2:  For r > 2 and n = 2r - 1 ,  no cyclic  permutation  of Ai  can be found  in  the basic-
Ducci-sequence, and there are n different  cycles of maximum length.

Again, we can extend the last theorem.

Theorem  8:  Ifn = 2
r-2\r>s>0,  then 8P(w) = n.

Proof; We prove this theorem using Ehrlich's formulas:

®(2
r -2s) = V®(2
r-
s  -l)  = 2
s(2
r-
s  -l)  = n.  D

It  can be  shown  that  only for  such  an n does the length  of the  cycle  of the basic-Ducci-
sequence equal n.

Theorem  9;  If 2P(w) = n, then n = 2r -2\  where n > 2  and r > s > 0.

Proof:  Using properties  (3) and (4), we can limit our investigation to odd numbers.  Then
the first w-tuple in the cycle is  Ax = (p,...,0,1,1).  There are only two different  (possible) prede-
cessors of Ax\  the n-tuple  (0,..., 0,1)  or the n-tuple  B := (1,..., 1,0)  (see [11]).  As the first n-
tuple is not in the cycle, the predecessor of Ax  in the cycle must be B.  As 2P(«) = n, it follows that
B-  An.  Since every binary w-tuple has exactly two predecessors, the predecessor  of B  is either
C: = (1,0,1,0,..., 1,0,1)  o r D : =  (0,1,0,1,..., 0,1,0).  We consider  PTn.  The last row represents
4,-1,  i.e., C or D.  It follows  from  Theorem  1 that the first  entry of An_1 must  be  1; thus, the
predecessor of B in the cycle is C.  If we consider PTn+v then its last row must consist entirely of
ones because C is the second to last row of PTn+l. Property (5) shows that all the entries are ones
if  and  only if n +1 is a power  of 2 and n = 2r -1  for  some  r > 2.  (For n = 21
 - 1 ,  the Ducci-
problemi makes no sense).  •

As above, we can answer the question: Which w-tuple is the first one in the cycle?

Theorem  10:  The 2r - 2
s -tuple  42, where n > 2 and r > s > 0, is the first one in the cycle of the
hasic-Ducci-sequence.

Proof:
L  The ??-tuple is contained in the cycle.

From Pascal's triangle, we can conclude (using the recursive construction given above):

4 . ^ ( 1 ^ , 0 ^ , . . . , ^ ^ .

2
s  2s  2s

We  obtain  alternating blocks of 2s  ones  and 2s zeros, the first and the last  block  consisting of
ones.  For An7 we conclude:  4 = (0 1:^,...,W

2
s  2s  2s

1995]  319

DUCCI-SEQUENCES AND PASCAL'S  TRIANGLE

As the first nil2  -I  blocks can be considered as the first elements of a basic-Ducci-sequence of
2^-tuples, the next successors are easy to determine.  After  25 - 1  applications of 2),  we  find

n-2
s  2
s
It follows that  An+r  = ( 0 ^ ,  1,0,...,0,1) =  A2,,

n-2s-l  2*+l

and the w-tuple An  is contained in the cycle.

2.  Ar  is the first w-tuple in the cycle.

Using  2P(«) = «,  we  can  conclude:  If  A2S_X  is  contained  in  the  cycle,  then  A^  = 4.  s  .
The first entry  of  A^,  must be 0 (see  construction  of w-tuples from  Pascal's triangle).  On  the
other hand, we have shown above that an+2s_x l  = I, which is a contradiction.  D

THE PROBLEM  "WITH"  OR  "WITHOUT" A  - 1

The question whether  a given n  is with  or without  a  -1  is important  for  different  theorems
and properties of Ducci-sequences [see Theorem 4, properties (1) and (2)].
As every integer n  can be considered  as a product  of prime numbers p,  the  problem  can be
divided into two separate questions:
•  Which prime numbers are with a -1, which are without?  and
•  If m,n  EM and with (-out) a -1, is the product with (-out) a -1?

Prime numbers  will be treated  first.  In the following, p  shall  denote  an  odd  prime  number  and
Op(2)  shall denote the order of 2 in a cyclic group of unities of the Galois-field  Zp.  We keep in
mind that  Op(2)  is a divisor of <p(p)—Euler's ^-function—and  <p(p) =  p-1.

The case p  = - 1 mod 4 is easier to examine.

Lemma  3:  Let p  = -l  mod 4, then Op(2) is odd if and only if —^ is even.

Proof:  We consider p  = - 1  mod 4 first and show the equivalence of three statements:

1.  Op(2)  is odd if and only if 2 is a square number in Z

is odd, we obtain "=>"  Since, by assertion,  O  (2) is odd, we obtain

and 2 is a square number in Z  .

"<="  2 = a
2  mod/? for  some a eZp.  By Fermat's theorem,  a
p~
l
  = 1  mod/7 and,  as  2\p-\
(p odd!), we conclude:  a
p-
l  = (<£f^  = l  mod/?

=2

P-\
and, further,  2
  2  = 1 mod  p.

320  [AUG.

DUCCI-SEQUENCES AND PASCAL'S TRIANGLE

Using p = - 1 mod 4, we get p - 1 = - 2 mod 4, and ^  must be odd.

2  2 is a square number in Zp if and only if (^) = 1 (Legendre-symbol), which is equivalent to

^  P
Z~I
= ( - 1 ) ^ = 1.
J?)
3.
  j^p  is even if and  only if £-^-  is even.  We can write p  as p = - 1 + 4&, k  GN.  Then it

follows that p2 = 16£
2 - 8* +1 or ^~  = 2k2 -  k.

As 2&
2 is always even, we conclude that
 £-^L is even if and only if A: is even.  D

Theorem  11:  Let p = - 1 mod 4.  Then/? is with a -1 if and only if ^  is odd.

Proof:
"<="  We consider the equation  x2 = 1 mod p.  As Zp  is a Galois-field,  the equation has

Op(2)
exactly two  solutions:  x = 1 mod p and x = -1 mod p .  2  2  is an integer solution of this  equation
D+l  Op(2)
if and only if Op(2) is even, i.e., -^j- is odd for p = - 1 mod 4 (Lemma 3).  As, by definition,  2  2
QP(2)
cannot be congruent to 1  modp, we have 2  2  = - 1 modp  mdp  is with a  -1.
"=>"  If 2M  = - 1 modp, then it follows that  2M\Op{2),  and so the order of 2 is even.  From

Lemma 3, it follows that -^p- is odd.  D

Let p be with a -1 and M be the least integer number with  2M = - 1 mod p,  M-2
kt  where
A: > 0 and t  is odd.  For our further  examination, we need to know that k = 0.  We will use a well-
known theorem from number theory.

Theorem  12:  The congruence x2 = - 1 modp has a solution in Zp if and only if p = 1 mod 4.

This theorem leads us at once to the following corollary.

Corollary 3:  M is odd for every p = - 1 mod 4.
 M.
Proof:  We assume that M is even.  Then a = 2 2  satisfies the equation  x2 = - 1 in contradic-
tion to the above theorem.  D
The case  p = 1 mod 4 is harder to treat because the above argument  cannot be used in this
case.  We will give only a partial solution.

Theorem  13:  Let p = 1  mod 4 and ^  be odd. • Thenp is with a  -1.

Pi*oof:  We again use

Since ™p is odd (p = 1  mod 4) as well as ^ p  (by assumption), we conclude that 2 is not a square

number in Z p.  Using  2  p  = 2  modp, we see that  Op(2) + l  must be odd and Op(2) is even.

q,(2)
By definition,  2  2  cannot be congruent to 1, sop must be with a -1.  D

1995]  321

DUCCI-SEQUENCES AND PASCAL'S TRIANGLE

If -£p is even, both cases are possible:

•  17,41,97,  113 are with a  -1;
•  73, 89, 233 are without a  -1.

As the problem is linked to the still unsolved Artin's Problem (see [2], p. 113), the complete solu-
tion seems to be very difficult  but interesting.
We also cannot determine whether Mis  even or odd.  In most cases, M i s even; however, for
281, we obtain M = 35.  This question will be important in our further  examination.

We will now treat products of prime numbers.

Lemma  4:  Let/? be with a -1.  Then pn  is with a -1 for every  nsN.

Proof:  By induction.  Let p" be with a -1 for some n and 2M = - 1 mod p".  Then  2M =
- 1 + kp
n  for some k.  We compute:

2pM =  QMy  = (_l  +  ^ y  =  - l + ^  + ^ - i y + ^ J i /  + / / ^ .

As (f) is divisible by p  for 2 <i <p-1,  we obtain  2 ^  = - 1 mod p
n+1.  As the lemma holds for
n -  1, the proof is complete.  •

(For a similar problem, see [13], pp. 364 ff.)

Theorem  14:  Let n = p1p2...pi,  the product  of odd prime numbers pi  (not necessarily  different
from each other) and (at least) one of the pi  without a -1,  Then the product n is without a  -1.

Proof:  Without  loss of generality, let pi  be without  a  -1.  We assume that n is with  a - 1 ,
which means that there exists an M  GN  with 2M = - 1 mod «.  This implies that  2M  = - 1 mod /?j
in contradiction to the choice of pv  D

Theorem 15:  Let ^  and m be odd integers with a -1,  (/, /w) = 1,2
L = - 1 mod £ and 2 M =s= - 1  mod
m (L and M minimal).  Then n-  £m is with a -1 if and only if, for some k  GN0, 2k  divides L and
M, and 2
k+l  divides neither of them.

Proof:
"<="  Obviously LI2
k  mdM/2
k  are odd numbers.  We compute:

M.  AL

(2
LY  = (-1)
2*  mod £ s  - 1 mod *;

(2^)2* = (-1)
2* mod w s  - 1 mod m.

LM
It follows that 2
2* = - 1 mod n &sn = £m.
" =>"  By contradiction:

Assume,  without  loss  of generality,  that  2N = - 1  mod «,  2*|Z, 2^+1|Z,  and 2/:+1|M  and N  is
minimal.  This implies that  2N  = - 1 mod w, 2^ = - 1 mod / ,  and that JV is the least common mul-
tiple of L  and M.  Therefore, Nis  divisible by 2
k+l  and N = 2LR  for some i? eN.  It follows by
computation that

322  [AUG.

DUCCI-SEQUENCES  AND PASCAL'S  TRIANGLE

2^  _ 2
2LR  — (2
L\
2R

= (-lf
R  mod t  = 1 mod  I,

which is a contradiction to  2
N  = - 1 mod I  as t  ^ 2.  •

Corollary 4:  If  ph...,p£  are prime numbers,  #• = - 1  mod 4, and  ^ ^  is odd  for  every  ! < / < / ,

then n = p\
x...p\
l  is with a -1.

Proof:  Since ^  is odd, /? is with a -1 by Theorem  11.  By Lemma 4, /?* is with  a  -1.  By
Corollary 3, Mis  odd, where 2
M  = -1 mod p.  By the proof of Lemma 4,  2
/,*~
,A/ = - 1 mod p
k;  of
course, the  exponent  p
k~
lM  is odd.  This is true  for  each prime p.  The  result  now  follows  by
Theorem  15.  •

(For a similar result, see [13], p. 364.)

REMAINING  QUESTIONS

During  our  investigation,  we  have  seen  that  the  Ducci-problem  is  closely  linked  to  the
problem of finding  the order  of 2  in a given field Zp.  It  seems that this problem is not yet  com-
pletely solved.
Going  back  to  the  Ducci-sequences,  it  is  interesting  to  ask  how  many  different  orbits  the
operator  2) (and therefore  2T) produces if all Ducci-sequences are considered.  If n is not a power
of  2,  let  k  be  the  number  of  divisors  m  of n  (where  m  < n).  Then  we  can  find  at  least  k + 2
different  cycles: the  cycle that  contains  only the n-tuph  (0,..., 0),  the  cycle  of the basic-Ducci-
sequence of w-tuples and the cycle of ^-tuples that are formed  of the nlm-ibid repetition by the m-
tuples of the corresponding basic-Ducci-sequence.
A whole range of new problems can be obtained using a variation  of the process  of  forming
the Ducci-sequence (first  done by Wong [17]), for example:

2/~(al3 ...,an):=((al+a2)  modk9...,(an^
ai)
  m^dk),  k  GN.

Many interesting  results  on that topic  can be found  in [17], but the length  of cycles  of  so-called
Ducci-processes has not been treated yet (except the above variation in [15]).

REFERENCES

1.  KD.Boklan.  "The w-Number Game."  The Fibonacci Quarterly 22.2 (1984): 152-55.
2.  P. Bundschuh.  Einfuhrung in die Zahlentheorie.  2. Auflage.  Berlin, Heidelberg, New York:
Springer-Verlag,  1992.
3.  M.  Burmester,  R.  Forcade,  & E.  Jacobs.  "Circles  of Numbers."  Glasgow Mathematical
Journal  19 (1978): 115-19.
4.  C.  Ciamberlini  & A. Marengoni.  "Su  una  interessante  curiosita  numerica."  Periodiche  di
Matematiche  17 (1937):25-30.
5.  J.  W.  Creely.  "The  Length  of  a  Three-Number  Game."  The Fibonacci  Quarterly  26,2
(1988):141-43.
6.  A. Ehrlich.  "Periods in Ducci's TV-Number Game of Differences."  The Fibonacci Quarterly
28.4 (1990):302-05.
7.  B. Freedman.  "The Four Number Game."  ScriptaMathematica  14 (1948):35-47.

1995]  323

DUCCI-SEQUENCES  AND PASCAL'S  TRIANGLE

8.  A. Hinz.  "Pascal's Triangle and the Tower of Hanoi."  Amer. Math. Monthly  99 (1992):538-
44.
9.  M. Lotan.  "A Problem in Difference  Sets."  Amer. Math. Monthly 56 (1949):535-41.
10.  E.Lucas.  Theeorie desnombres.  1891, p. 420.
11.  A. Ludington Furno.  "Cycles of Differences  of Integers."  J. Number Theory 13 (1981):255-
61.
12.  A.  Ludington-Young.  "Length  of  the  ^-Number  Game."  The Fibonacci  Quarterly  28.3
(1990):259-65.
13.  D. P. Parent.  Exercises in Number Theory. New York: Springer-Verlag,  1984.
14.  H.-O. Peitgen,  el al.  Fractale: Selbstahnlichkeit,  Chaosspiel,  Dimension;  ein  Arbeitsbuch,
Ernst  Klett  Schulbuchverlag,  Stuttgart.  Berlin,  Heidelberg,  New  York:  Springer-Verlag,
1992.
15.  G.  Schoffl.  "Duccifolgen  und  ihre Behandlung  im Unterricht,  Zulassungsarbeit  zur  Wissen-
schaftlichen  Prtifung  fur  das  Lehramt  an  den  Gymnasien  in  Bayern."  Unpublished  thesis,
Mathematisches Institut der Universitat Wurzburg, 1993.
16.  K. B. Stolarsky.  "Power and Exponential  Sums of Digital  Sums Related to Binomial  Coeffi-
cient Parity."  SIAMJ. Appl. Math. 32 (1977):717-30.
17.  F.-B. Wong.  "Ducci Processes."  The Fibonacci Quarterly 20.2 (1982):97-105.
AMS Classification Numbers:  00A08, 11B37, 11B65

• >  •!•  •*•

Author and Title Index
The  AUTHOR,  TITLE,  KEY-WORD,  ELEMENTARY  PROBLEMS  and  ADVANCED  PROBLEMS  indices
for the first  30 volumes of The Fibonacci Quarterly have been completed by Dr.  Charles K.  Cook.  Publication
of the completed indices is on a 3.5-inch  high density disk.  The price for a copyrighted version of the disk will
be $40.00 plus postage for  non-subscribers  while subscribers to The Fibonacci Quarterly will only need to pay
$20.00 plus postage.  For additional information  or to order a disk copy of the indices, write to:

PROFESSOR CHARLES K. COOK
DEPARTMENT OF MATHEMATICS
UNIVERSITY OF SOUTH CAROLINA AT SUMTER
1 LOUISE CIRCLE
SUMTER,  SC  29150

The  indices  have been  compiled  using  WORDPERFECT.  Should you wish to order a  copy of the indices  for
another  wordprocessor  or for  a non-compatible  IBM machine please  explain your  situation  to Dr.  Cook when
you place your order and he will try to accommodate you.  DO NOT SEND YOUR PAYMENT WITH YOUR
ORDER.  You will be billed for the indices and postage by Dr. Cook when he sends you the disk.  A star is used
in the indices to indicate unsolved problems. Furthermore, Dr.  Cook is working on a SUBJECT index and will
also be classifying  all articles by use of the AMS Classification  Scheme.  Those who purchase the indices will be
given  one  free  update  of  all  indices  when  the  SUBJECT  index  and  the  AMS  classification  of  all  articles
published in The Fibonacci Quarterly are completed.

3 2 4  [AUG.
