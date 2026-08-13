<!-- source: https://arxiv.org/pdf/2503.11672 | converted from PDF -->

1

The Erdös-Straus Conjecture and Pythagorean Primes

 Bernd R. Schuh

Dr. Bernd Schuh, D-50968 Cologne, Germany, bernd.schuh@netcologne.de

keywords: unit fractions, Diophantine equations, Erdös-Straus conjecture, Pythagorean primes,

parametric solutions

Abstract

The Diophantine equation 4/n = 1/x + 1/y + 1/z  for a Pythagorean prime n is split into two

independent Diophantine equations, which correspond to two different types of solution. The

solvability of these equations forces certain restrictions on allowed Pythagorean primes. Empirical

evidence suggests that these restrictions hold for all Pythagorean primes, which I state as two

independent conjectures. One can be formulated as follows: every Pythagorean prime can be written as

p =(4ab-1)(4c-1) – 4ab2/ d, where a, b, c are natural numbers and d is a divisor of ab. The second

conjecture reads: every Pythagorean prime can be written as p =(4ab-1)(4c-1) – 4ac, where a, b, c are

natural numbers. I give a new straightforward plausibility for the latter conjecture (which has been

formulated independently by other authors) and I outline a practicle and effective algorithm to

determine a,b,c for a given p.

I Introduction

In the following I will call an equation

( , , ,..., , , ) 0n a b x y z=
  solvable in

n
  iff for a given

n 

positive integers

, ,...,a b z
 exist which fulfill this equation. These integers are called the solution.

A well known conjecture by Erdös-Straus (ESC in the following) states that the Diophantine equation

4 / (1/ 1/ 1/ ) 0− + + =n x y z
         (1)

is solvable in every integer

2n 
 . There is an impressive body of evidence for the validity of the

conjecture,  see e.g. [1,2,3,4], but no valid proof. Most approaches sought parametric solutions and

covering of  integers by arithmetic progression. Probably, different methods are needed. A key

element appear to be Pythagorean primes (Pp in the following), since solving (1) is a nontrivial task

only if

n
  is a Pythagorean prime. I list several known facts to support this assertion.

2

 (i)   If equ. (1) is solvable in

n
  it is also solvable in any multiple

'n kn=
  of

n
 . Proof:

simply set

'x kx=
  etc..

(ii)  Equ. (1) is solvable in all even

2nk=
 . Proof: simply put

,2x k y k z= = =
  .

(iii)  Equ. (1) is solvable in all

n
  of the form

41nk=−
 . Proof: set

, ( 1), 1x kn y k k z k= = + = +
 .

(See [5] for similar results.)

These three facts constitute the claim that to prove the ESC it suffices to show that a solution exists for

all primes of the form

14nK=+
 , i.e. all Pp. We neglect further progress on restrictions on

K
 , like the

well known ones by Mordell [6] and others [7], since they are of no importance for the following

arguments. A fourth fact, however, is notable and important in the following:

(iv)  There are exactly two types of solutions, say (A) and (B). In type (A) only one of the

variables

,,x y z
   is proportional to

n
 . In type (B) two variables are multiples of

n
 . [2]

II Solutions

In this section I will deduce conditions that guaranty solvability of equation (1) in Pythagorean primes.

For the rest of the paper I use the abbreviation

: 4 1w w =−
  for elements of the residue class

3mod 4
 .

The restriction to Pythagorean primes leads to more transparent results than earlier approaches using

similar reformulations of equation (1), see e.g. [9,10]. Central to our arguments is a decomposition of

(1) into two equations which correspond to one of the solution types (A) or (B) mentioned in fact (iv)

and introduced by Bernstein [2].

Theorem 1

The diophantine equation (1) is solvable in

n
  being a prime  if and only if either

( , , , ) : ( ) 0Aan a d z z n d a = − + =
                                (2a)

or

( , , , ) : 0Ban a d z z d na = − − =
         (2b)

is solvable, where

d
  is a divisor of

2a
 .  The solution of (1) then reads

, / ,z y az d x an==
           (3a)

for (2a), and

, / ,z y naz d x an==
            (3b)

for (2b).

Proof: In a first step we show that (1) is equivalent to equations (2a) and (2b) for primes. According to

fact (iv) at least one of the variables

,,x y z
  is proportional to

n
 . Thus we write

x an=
 , then

3

2 2 2 2 2

22

4 / 1/ 1/ 1/

()

()

( )( )

a

aa

aa

n x y z

yz na y z

yz na y z n a n a

z na y na n a





= + + 

= + 

− + + = 

− − =

Since

n
  is a prime either

2n
  divides one of the factors on the l.h.s. of the last equation or

n
  divides

both. In the later case we have

az na nd −=
  and

acy na nd −=
  and thus (2a) and (3a), in the former

case

az na d −=
  and

2
acy na n d −=
  and thus (2b), (3b). In both cases

d
  denotes a divisor of

2a
  and

cd
  its cofactor:

2 ca dd=
 .

It remains to be shown that

/az d
  in the formula for

y
  is a positive integer. Since any divisor of

2a

may be written as a product of divisors of

a
 ,

12d a a=
 , one can write

1 2 1/ ( )acz a n a a =+
  instead of

(2a) and

1 2 1/acz a a na =+
  instead of (2b), where the subscript c denotes cofactors, as before. Since

1( , ) 1a a =
 ,  one has

1/za 
  and thus

1 2 2 1/ / ( / )caz d az a a a z a= = 
 .

In effect theorem 1 states that finding positive integers

,,x y z
  which fulfill (1) for primes

n
  is

equivalent to finding positive integers

,,z a d
  which fulfill one of the equ. (2a)  or (2b). The solutions

of the two approaches are then related by equs. (3).

A consequence of equations (3a),  (3b) is the

Corollary:

If

n
  is a Pythagorean prime, i.e.

14nK=+
 , every solution of (3a) is a solution of type (A) in

Bernsteins notation [2]  (see fact (iv) in the introduction).

Every solution of (3b) is a solution of type (B).

proof: the second statement is obvious from (3b). To prove the first part of the corollary we observe

that according to (2a) the prime

n
  divides either

a
  or

z
 . The latter possibility can be excluded,

because in that case, according to (3a), all three variables would be proportional to

n
 , which

contradicts equ. (1). Thus

n
  divides

a
 . Since

1mod4n 
 the proportionality factor must be

congruent

1mod4−
 . So a parameter

b
 exists with

ab
 b

n

a bn K

a b K





=

= − 

=+
             (4)

Therefore

( , ) 1an =
  and

y
  in equ. (3a) cannot have a divisor

n
 .

 4

The problem of solving equ. (1) for a given prime

n
  thus amounts to finding parameters

a
  and a

divisor

d
 of

2a
  which allow for positive integer solutions

z
 either of equ. (2a) or (2b).

This reformulation of the ESC problem leads to interesting parametrizations of allowed primes. We

state this fact as two separate theorems, depending on whether (2a) or (2b) holds:

Theorem 2A

Equation (2a) is solvable in a prime

14nK=+
  if

K
  can be written

( 1)bKb  = − −
           (5)

with parameters

,,b 
 .

Proof of theorem  2A: We assume that

,,b 
 and

K
  are given as in (5). We define

a
  via (4) and get

the factorization :

( )( 1)bbab = − −
 . Defining furthermore

: ( )bdb=−
  , which obviously is a

divisor of

2a
 , one has

()bba d b + = −
 . Since (2a)  yields

bz a d =+
 ,             (6)

setting

: ( )bzb =−
  completes the proof.

Unfortunately, condition (5) is only sufficient to solve (2a) but not necessary. To see this we assume

(2a) to hold with

,,z a d
  given. We have already proven that a positive integer

b
  exists, connected to

a
  via (4), such that (2a) is equivalent to (6). Next we observe

Lemma 1:

a
  must be composite.

Proof: If it were a prime then

 
21, ,d a a
 . For

1d =
  or

bd a b K= = +
  equation  (6) yields either

1 bb +=
  or

2 bb =
  for some

 
 . Both cannot be fulfilled with

b 
 . For

2da=
  we have

from (4)

22 mod bab 
  and one gets from (6)

2
b bb −=
  with some

 
 . But

4 bb−−

never yields a perfect square (see e.g. [8,11]). Thus

a
 must be composite.

Since from (4)

mod bab 
  and

( , ) 1bb  =
  one can make a general Ansatz

12( )( )bba b b = − −
            (7)

with integer parameters


 ,




 and

12,bb


 . The latter must fulfill

12 bb b b =+
  according to (4).

Solving (4) for

K
  with

a
  replaced by  (7) one gets

12bK b b   = − − +
           (8)

5

as a necessary condition for the solvability of (2a). Of course, a six parameter-family of solutions is

not an achievement. But the foregoing steps help to understand the idea behind (5), which one gets

from (8) by the choice

12, 1, 0b b b = = =
 .

The situation for equ. (2b) is different. Here we are able to identify a four-parameter-family of

solutions which is both sufficient and necessary for the solvability of (2b).

Theorem 2B

Equation (2b) is solvable in a prime

14nK=+
  if and only if

K
  can be written as

aK a d= − −
            (9)

with parameters

,a 
  and a divisor

d
  of

2a
 .

Proof of  theorem 2B:  consider equ. (2b) and assume that a positive integer solution exists for a given

14nK=+
 . Inserting this in

an d+
 one gets from (2b)

()− = + +a z K d a K
 . With a new parameter

:=−zK
 one can write

= − −aK a d
 , as claimed. If vice versa

14nK=+
  is given by equ. (9) in

positive integers

,,ad
 one inserts this expression on the r.h.s. of (2b) and defines

z
  by

:zK =+
 ,

which is a positive integer and fulfills (2b). Done.

Note that the proof of theorem 2B does not necessitate

n
  to be a prime. It is, however, necessary for

(2b) being equivalent to (1) (together with (2a)).

III Discussion

Up to now I have identified a three-parameter family of solutions for equation (2a) and a four-

parameter family of solutions for (2b), the latter being not only sufficient but also necessary. The first

always leads to solutions of type (A), i.e. with exactly one of the variables in (1) being proportional to

n
 , whereas the second produces solutions of type (B) with two variables being multiples of

n
 .

What is the further relevance of these parametrizations? Let us consider theorem 2A first. We observe

that equation (5) is not trivial in the sense that it comprizes all odd numbers of the form

14K+
 .

There are exceptions, e.g. all perfect squares and some numbers with

2mod3K 
  like

26K =
 , and

200K =
 .

Secondly, we observe that it is usable in that it gives simple deductions for well known facts. E.g. it

shows that equation (1) is solvable for all odd

K
 . To see this, set

1b ==
  in (5) to get

21K =−
 .

Thus theorem 2A ensures that whenever

K
  is an odd integer the Diophantine equation is solvable. It

is also easy to see that

1mod3K
  is easily represented by  (5). Set

1==
  to get

32=−Kb
 .

6

Furthermore,

2mod3K 
  leads to

0mod3n 
  which is not a prime. Thus only

0mod3K 
  and

0mod 2K 
  remain as interesting possibilities, a long known restriction, which states that exceptions

(if any) to the ESC must be sought among the primes

1mod 24n 
 .

Surprisingly, the parametrization (5) worked for all Pythagorean primes we tried, extremely well. We

were able to calcultate

b
 ,


  and


  even for many-digit primes with a pocket calculator (and open

source prime factorization programs). The reason is that  the derivation of (5) offers a convenient

algorithm to determine the parameters in this equation for a given

K
 . It works as follows:

Algorithm to determine

b
 ,


  and



For given

n
  or

K
 respectively calculate

a
  from equ. (4), starting conveniently with

1b =
 .

Then factorize

a
  and check whether one of the factors is congruent

1mod b−
 . If so, the cofactor will

be congruent

mod bb −
  and from (8) with the special choice

12, 1, 0b b b = = =
   one reads off


  and


 . Store the solution

,,b 
 .

Repeat the procedure with

1bb→+
 .

The process ends, when

1b +
  exceeds a limit, e.g.

(2 ) / 3K+
 . Then all solutions are in store. If the

store is empty there is no solution and

K
  cannot be represented by (5).

The limit can be derived from a rough estimation: First rewrite (5) as

bn    = − −
           (10)

Then

( ( 1) 1)bn    − −
 . And

1 / 3( 1)bn +  −
  yields the cited limit.

Take

560281=n
  as a nontrivial example illustrating the algorithm. With

1=b
  one gets

3 1 420211 11 38201+ = = K
  and  therefore

(1 11) / 3 4+ = = 
  and

(1 38201) / 3 12734+ = = 
 .

2b =
  yields a second solution:

2, 10, 2060b = = =
 . To find all solutions one would have to go

to

46690b =
 .

Since (5) apparently represents the Pythagorean primes so extremely well, it is tempting to put forward

the following conjecture:

Conjecture A

All primes of the form

14K+
  belong to the set

AS
  defined by

 A : , 3mod4;S abc b c a b c= − −  

i.e. the parametrization given in theorem 2A.

 7

Since any member of

AS
  gives rise to a solution of equation (1) as stated in theorem 2A  it is clear that

the ESC is valid if the conjecture is.

Up to now, conjecture A is unproven. After all, one can show

Lemma 2:

AS
  contains infinitely many primes.

Proof:  We use a theorem by Iwaniec [12]. Consider (10) as a quadratic polynomial in two variables

x =
  and

y =
 .  Then obviously

( , ) bn x y xy x y= − −
  is irreducible and

/1bn x y  = −
  and

/1bn y x  = −
  are linearly independent. Thus the assumptions of theorem 1 in [12] are fulfilled.

According to conclusion (i) of that theorem the number of primes up to a given

N
 being represented

by

( , )n x y
  grows with

N
  faster than

/ logNN
 .

After completion of this work I noticed that the parametrization (5) was put forward in [10] already.

The authors of [10] made extensive calculations and verified conjecture A for Pythagorean primes up

to

1410n 
 .  They have also proven that the set

AS
  does not contain perfect squares, and they list a

finite number of non-primes which are not members of

AS
 .

I would like to point out, however, that my “derivation” of the conjecture is more straightforward and

leads to a usable algorithm to identify given Pythagorean primes as members of the three-parameter

family of solutions.

Ad theorem 2B.

To illustrate the result of theorem 2B take e.g.

1ad==
  in (9) and let


 run from 1 to 5 . This

generates the Pythagorean primes 5, 17, 29, 41, 53. The primes 13 and 37 are produced by the choice

da=
  , setting

1 =
  and letting

a
  run.

Depending on the value of

a
  there can be a huge amount of choices for the parameter

d
 . Writing

quite generally

12d a a=
 ,  we have

12a a a==
  since

1,2a
  are divisors of

a
  and condition (9) becomes

1 2
14/ana   =−
           (11)

While


 ,

1a
  and


  are independent positive integers,


  is restricted to divisors of

1a
 . With this

restriction in mind, the existence of parameters

1, , ,a  
  relating to

n
  via (11)  is a necessary and

sufficient condition for the solvability of  equation (2b).

Other than theorem 2A, theorem 2B and (11) is of restricted usefulness to search for solutions of equ.

(1) with

n
  given, since it offers no obvious algorithm for limiting the variety of choices. Nonetheless,

empirically the parametrization (11) works extremely well. All Pythagorean primes we checked had a

representation in terms of equ. (11). Thus we propose a second conjecture based on equ. (2b) and

theorem 2B:
 8

Conjecture B

All primes of the form

14K+
  belong to the set

BS
  defined by

24 : , , , ,BS    
     


= − 


i.e. the parametrization given in equ. (11).

Also conjecture B is not trivial. The set

BS
  does not include all odd numbers congruent 1mod4, e.g. it

does not include perfect squares, too.

Conclusion.

In a first step we have replaced the Diophantine equation (1) by two simpler equations (2a) and (2b)

corresponding to the two types of solutions known as type (A) and type (B) [2]. In type (A) one of the

variables is proportional to

n
 ,  in type (B) two of them are. Each equation leads to a different

parametric representation of Pythagorean primes,

ApS
  and

BpS
 , see equations (10) and (11),

respectively. Both are sufficient to guaranty the solvability of the corresponding equation. But only the

type (B) conjecture is also necessary. There is rather strong evidence that each of these representations

comprizes all Pythagorean primes. We thus propose two corresponding conjectures A and B. Should

both conjectures turn out to be valid the Erdös-Straus conjecture were proved. Should the ESC be

proven then at least conjecture B is bound to hold.

References

[1] A. Aigner, Brüche aus Summen von Stammbrüchen, J. Angew. Math. 214/215 (1964), 174-179.

[2] L. Bernstein, Zur Lösung der diophantischen Gleichung m/n=1/x+1/y+1/z insbesondere im Fall
m=4, Journal für die Reine und Angewandte Mathematik Vol. 211 (1962), 1–10.

[3] P. Erdös and R.L. Graham, Old and new problems and results in combinatorial number theory,
Monographies de L'Enseignement Mathematique de Geneve 28 (1980) pp. 30-44.

[4] Graham, R.L. (2013). Paul Erdős and Egyptian Fractions. In: Lovász, L., Ruzsa, I.Z., Sós, V.T.
(eds) Erdős Centennial. Bolyai Society Mathematical Studies, vol 25. Springer, Berlin, Heidelberg.
doi: 10.1007/978-3-642-39286-3_9.

[5] C.L. Clifton-Everest, On the Diophantine equation

/ 1/ 1/ 1/r n x y z= + +
 ,

The Mathematical Gazette, Vol. 91 (2007), No. 522, 481-492.

[6] L. J. Mordell Diophantine Equations, in:Pure and Applied Mathematics, Vol. 30, 287 (1967).

[7] E. J. Ionescu,  A. Wilson, On the Erdös-Straus Conjecture, https://arxiv.org/abs/1001.1100 (2010).

[8] T. Nagell, Introduction to Number Theory. Second edition. Chelsea Publ. Co. 1964.

 9

[9] S. Brown, On the number of sums of three unit fractions, Notes on Number Theory and Discrete
Mathematics Vol. 19, (2013), No. 4, 28–32.

[10] On Egyptian Fractions, M. B. Hernández, M. Benito, E. Fernández,
https://arxiv.org/abs/1010.2035 (2012).

[11] A. Schinzel, On sums of three unit fractions with polynomial denominators, Functiones et
Approximatio XXVIII (2000), 187 – 194.

[12] H. Iwaniec, Acta arithmetica XXIV ,435 (1974).
