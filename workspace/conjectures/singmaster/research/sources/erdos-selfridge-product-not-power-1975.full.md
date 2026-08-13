<!-- source: https://www.renyi.hu/~p_erdos/1975-46.pdf | converted from PDF -->

THE PRODUCT OF CONSECUTIVE INTEGERS
IS NEVER A POWER

BY
P . ERDŐS AND J . L. SELFRIDGE

We dedicate this paper to the memory of our friends H . Davenport, Ju.V .
Linnik, L. J. Mordell, L. Moser, A . Rényi and W . Sierpinski, all of whom were
alive when we started our work in 1966 at the University of Illinois at Urbana .

0. Introduction

It was conjectured about 150 years ago that the product of consecutive
integers is never a power . That is, the equation

(n+1) • • (n+k)=x`

 (1)

has no solution in integers with k >_ 2, 1 >_ 2 and n >_ 0 . (These restrictions
on k, 1 and n will be implicit throughout this paper .) The early literature on this
subject can be found in Dickson's history and the somewhat later literature in
the paper of Obláth [5].
Rigge [6], and a few months later Erdös [1], proved the conjecture for 1 = 2 .
Later these two authors [1] proved that for fixed 1 there are at most finitely
many solutions to (1). In 1940, Erdös and Siegel jointly proved that there is
an absolute constant c such that (1) has no solutions with k > c, but this proof
was never published. Later Erdös [2] found a different proof ; by improving
the method used, we can now completely establish the old conjecture . Thus
we shall prove

THEOREM 1 . The product of two or more consecutive positive integers is
never a power .

In fact we shall prove a stronger result :

THEOREM 2 . Let k, 1, n be integers such that k >_ 3, 1 >_ 2 and n + k >_ p (k) ,
where p(k) is the least prime satisfying p (k) >_ k. Then there is a prime p >_ k for
which a p # 0 (mod 1), where a p is the power of p dividing (n + 1) . . . (n + k) .

Theorem 2 implies Theorem 1, since it is easy to see that (n + 1)(n + 2) is
never an lth power and if n < k then by Bertrand's postulate the largest prime
factor of (n + 1) . . . (n + k) divides this product to exactly the first power .
Moreover, this shows that in proving Theorem 2 it will suffice to assume n > k .
One could conjecture the following strengthening of Theorem 2 : if k >_ 4
and n + k >_ p (k) , then there is at least one prime greater than k which divides

Received May 24, 1974.
 292

and
 THE PRODUCT OF CONSECUTIVE INTEGERS

 293

(n + 1) . . . (n + k) to the first power. This conjecture, if true, seems very deep .
The requirement of k >_ 4 is motivated by

(50) = 1402.
3

Now we start the proof of Theorem 2. We suppose that Theorem 2 is false

for some particular k, I and n, and show that in every case this leads to a con-

tradiction. As noted above, we assume n > k .

1 . Basic lemmas

First observe that by the well-known theorem of Sylvester and Schur [3]
there is always a prime greater than k which divides (n + 1) . . . (n + k), since
n > k . Such a prime divides only one of the k factors, so n + k >_ (k + 1) l,
whence n > k`.

 (2)

Furthermore since we suppose Theorem 2 is false, for 1 < i < k we have

n + i = a ix„

 (3)

where a i is Ith-power free and all its prime factors are less than k .
In the proof [1] for the case I = 2, it was shown that a i aj if i j. In
fact for 1 > 2 it is also known that the products a,aj are all distinct. In this
paper we need the stronger result

LEMMA 1 . For any l' < 1, the products ai, . . . ai,, (i

 are all

distinct.

In fact we prove that the ratio of two such products cannot be an lth power .
First we show that (2) ensures

(n + ü) . . . (n + ü-,) # (n + ji) . . . (n + j,-1),

 (4)

provided the two products are not identical .
Cancel any equal factors . Since (n + i, n + j) < k and n > ki, it follows

that no factor of one member of (4) divides the product of the factors remaining
in the other member, so the nonequality in (4) is proved .
Now we prove the lemma . For some rational t, suppose that

a . . . . a.,-, = ail . . . ai,_,t .

 O5

We shall show that (5) implies the subscripts must all match . Assume without
loss of generality that (n + ü) . . . (n + ü_ i) > (n + j i) . . . (n + j,_ and
put t = u/v, with (u, v) = 1 . Then
 x1
(n + i,) . . . (n + i,-i) = ai, . . . a, u,

Y~
(n + i,) . . . (n + j,-,) = a„ . . . a ~

 ui

294

 P . ERDŐS AND J . L . SELFRIDGE

where x = ux ;, . . . xi ,_, and y = vxj
,

 x;,_, in the notation of (3) . By (5),

we may put A - a . . . .a . _, - aj, . . .aj

u'

 v'

 ,

so Ax' > Ay' and therefore x >- y + 1 . Thus

(n +

 . . . (n + i,- i)

- (n + ji) . . . (n + ji-i) > A{(y + 1)' - y'} > Aly'-1

Note that (5) implies A is a positive integer . Also Ay` _ (n + j1) . . .
(n + j,_,) > n", so with (6) we have
 n1-1 (1-1)/1
(n + i,) . . . (n + ü 1) - (n + j,) . . . (n + Ji-~) > AI	 A
 (7)

> ln('-1)2/1 .

On the other hand,

(n+i,) . . .(n+i,-1)

- (n + j,) . . . (n + j,-,) < (n + k)` -i - n i-i < kln L-2 ,

where the last inequality is obvious if 1 = 2 and for l >- 3 it may be seen as

follows. Clearly it suffices to show that

'-1
kn1-2 > Y (l - 11 n,-i-'k
-z

 i

 '
that is
 1 > i-2 CI I
 1)
 Cn) -1
Now
 C
 l - 1) < l ;
i

 2'- 1

also n > k', k >_ 3 and I >- 3, so n > kl and moreover n > k1 2. Therefore

1 < l

 kl

 1 -

 k12

 < 112 <
 1 .
( i )
 (k)'-

 n(2n)

 2n - kl

 n

The lemma now follows, since (7) and (8) require k > n tl', contrary to (2).
Now we prove :

LEMMA 2. By deleting a suitably chosen subset of 7r(k - 1) of the numbers
a,(1 < i < k), we have
 a, . . . aj, , I (k - 1) !

 (9)

where k' = k - n(k - 1) .

For each prime p < k - I we omit an a,,, for which n + m is divisible by p

to the highest power. If I < i < k and i

 m, the power of p dividing n + i

(6)

(8)

THE PRODUCT OF CONSECUTIVE INTEGERS

 29 5

is the same as the power of p dividing i - m . Thus p"l Jai,

 a i,, implies

p" I (k - m)! (m - 1)!, so p" I (k - 1)! and our lemma is proved .

Change of notation. In the remainder of this paper it will be convenient to
have the a's renumbered so that a l < a2 < . . . < a,. We shall employ this
new notation in Sections 2 and 3.
Note also that to prove Theorem 2 for any particular Z it is enough to prove
it for some divisor of l, so it suffices to consider only prime l.

2. The case / > 2

2. L The case k >- 30000 . Now we show that (9) leads to a contradiction
for k >- 30000, using only the distinctness of the products a iap It is known [4]
that the number of positive integers b1 < . . . < b, < x for which the products
bib; are all distinct satisfies
 c x 34
r < ~r(x) + (log x)32 ,

 (10)

and this is best possible apart from the value of cl. However, when r is small
this result is not adequate for our needs, so we shall now establish a bound
which is sharper for small r.
First we need a graph theoretic lemma. A subgraph of a graph is called a
rectangle if it comprises two pairs of vertices, with each member of one pair
joined to each member of the other. We prove :

LEMMA 3. Let G be a bipartite graph of s white and t black vertices which
contains no rectangles. Then the number of edges of G is at most

s + (_)

Call a subgraph of G comprising one vertex joined to each of two others a
V-subgraph . Since G contains no rectangle, there can be at most one V-sub-
graph with any given pair of black vertices as its endpoints . Let si be the number
of white vertices of valence i, so 1i>1 s i = s. Counting the number of V-
subgraphs with black endpoints gives

E si (2) < (2) .

 (11)

If E is the number of edges of G, then by (11)

E= E is, =s+ E (i-I)si <s+ E, si a <s+ t
C~
i_>1

 i>2

 i>_z

 2

 (2)

which proves Lemma 3 .
Now let u 1 < . . . < u s < x and v 1 < . . . < v, <- x be two sequences of
positive integers such that every positive integer up to x can be written in the

296

 P . ERDŐS AND J . L. SELFRIDGE

form u ivj. If b 1 < . . . < b, < x are positive integers such that all the products

bib; are distinct, form the bipartite graph G with s white vertices labelled
u	 u., and t black vertices labelled v	 v, and an edge between ui and

vj if uivj = b,„ for some m . Distinctness of the products b ib; ensures that G has
no rectangles so by Lemma 3, r<s+( 2) .

 (12)

Lemma 1 shows in particular that the bound (12) applies to the sequence
a1 < . . . < a, Using (12) we next prove that the product of any k - 7r(k) of
the a's exceeds k! provided k >_ 30000. Because of Lemma 2 this implies
Theorem 2 for k >_ 30000 and l > 2 . Evidently it suffices to prove

k-n(k)

F1 ai > k! if k > 30000 .

 (13)
i=1

We shall now obtain lower bounds on a i (1 < i < k). We clearly have

ai >- i,

 (14)

and using (12) we shall show two further inequalities

ai >_ 3.5694(1 - 304),

 (15)

a i > 4.3402(1 - 1492) .

 (16)

Of these, (14) is sharpest for i < 422, (15) is sharpest for 422 < i < 6993, and
(16) is sharpest for i > 6993 . With these inequalities, a routine calculation using
Stirling's formula suffices to verify (13) when k = 30000, and (16) ensures that
(13) holds when k > 30000 .
To prove (15), we take v 1 < . . . < v, to be the t = 25 positive integers up
to 36 which have no prime factor greater than 7 (so v .1 = 1 and v21 = 36) .
Next we obtain a suitable set of positive integers u 1 < . . . < u, < x so that
every positive integer m < x is expressible in the form uivj. For convenience,
let V denote the set of v's. Clearly any positive integer m < x with all prime
factors greater than 7 must be included in the u's : let U1 denote the set of such
numbers . Next, suppose m < x is a positive multiple of 7 and m = dd', where
d is the largest divisor of m with no prime factor greater than 7 . If d ~ V then
d >- 42, since 7 1 d. Thus x >- m = dd' > 42d', so 7d' < x/6 . Hence we
include in the u's all positive integers of the form 7d' <- x/6 with least prime
factor 7 : let U2 denote this set of numbers. Similarly, if m < x is a positive
multiple of 5 and m = dd', where d is the largest divisor of m with no prime
factor greater than 5, then d ~ V requires d >- 40 and 5d' < x/8. Hence we
include in the u's all positive integers of the form 5d' <- x/8 with least prime
factor 5, and let U3 denote this set. Likewise we include in the u's all positive
integers of the form 3d' < x/14 with least prime factor 3, and all positive
integers of the form 2d' < x/20, denoting these sets by U4 and US respectively .

THE PRODUCT OF CONSECUTIVE INTEGERS

 297

Now every positive integer m < x is expressible in the form m = u ivj for some

ui c U and vj e V, where U denotes the union of U l, . . . , U5 .
The number of u's in each U i can readily be calculated . For example

IU21 = X 30 ) 42

X

 2x

+ E2(x)

 315 + E2(x),

where the error term has the bound E 2(x) < 14/15. Likewise ejx) < 53/35,

83(x) < 2/3, E4(x) < 1/2 and E5(x) < 0. Thus the total number of u's is

s=IU1= IUil=Cg +? + - + 1 + llx
35

 315

 120

 84

 40

+ Y~ 8 i(x) < 353 x + 4.
i= 1

 1260

Now (12) implies that the number of a's up to x is less than 353x/1260 + 304,
whence (15).
To prove (16), we take the v's to be the t = 55 positive integers up to 100
with no prime factor greater than 11, and the u's to be all positive integers up
to x with all prime factors greater than 11, together with all those up to x/10
with least prime factor 11, all those up to x/15 with least prime factor 7, all
those up to x/21 with least prime factor 5, all those up to x/35 with least prime
factor 3, and finally all even integers up to x/54 . The first of these subsets of
u's contains 16x/77 + ejx) numbers, where a o(x) < 194/77 . The error terms
in counting the other subsets of u's are the same as before, so the total error is
less than 7. With (12), this leads to (16) . Now we shall work upwards from
small k to resolve the cases with k < 30000 .

2.2. The case k = 3 . It is easy to see that (1) has no solution when k = 3,
for (n + 1)(n + 2)(n + 3) = m(m2 - 1), where m = n + 2, shows that the
product could only be an lth power if m and m 2 - 1 are lth powers, but
m 2 - 1 and m 2 cannot both be lth powers . But for Theorem 2 we need to
show ap # 0 (mod 1) for some prime p >- 3, where ap is the power of p in
(n + 1)(n + 2)(n + 3) . Suppose there is no such p . If n is even, (n + 1,

• + 3) = 1 ensures ai = a 2 = 1, contradicting Lemma 1 . If n is odd, (n + 1,

•

 + 3) = 2 ensures a, = 1, a2 = 2 and a3 = 2", with 1 < a < l, and Lemma

1 is contradicted by a, - 'a, = az.

2.3. The case 4 < k < 1000, 1 = 3 . Here we restrict attention to those

a's with no prime factor greater than the mth prime, say f(k, m) in number. If
• and v are positive integers with prime factors similarly restricted, there are
3' rationale u/v no two of which differ by a factor which is the cube of a rational .
The number of formally distinct expressions a ilaj is f(k, m){f(k, m) - 1}, so

there are two whose quotient yields a solution to (5), thus contradicting Lemma

1, if f(k, m){f(k, m) - 1} > 3m.

 (17)

298

 P . ERDŐS AND J. L. SELFRIDGE

Since the a's arise as divisors ofk consecutive integers, and have all prime factors
less than k, it is straightforward to calculate a lower bound for f(k, m) . Thus
we verify (17) for 4 < k < 10 with m = 2, for 10 < k < 28 with m = 3, for
28 < k < 77 with m = 4, for 77 < k < 143 with m = 5, for 143 < k < 340
with m = 6, for 340 < k < 646 with m = 7, and for 646 < k < 1000 with
m = 8 .
This method could be continued beyond k = 1000, but certainly fails before
reaching k = 10000. Fortunately we have an improvement available, and we
now proceed with it .

2.4. The case 1000 < k < 30000, 1 = 3 . Let q, < . . . < q, be the r
largest primes satisfying q, < k", where r is to be suitably chosen . We now
restrict attention to those a's, say F(k, r) in number, which have no prime
factor greater than k112, and at most one prime factor (counting multiplicity)
among the q's. If u and v are positive integers with prime factors similarly
restricted, there are 3' (",)- ' R rationale a/v no two of which differ by a factor
which is the cube of a rational. In this count the factor R = r 2 + r + 1 arises
from the fact that a and v each contain at most one of the q's as a divisor. As
in (17), the number of formally distinct expressions a,/a; is enough to ensure
that there are two whose quotient yields a solution to (5), and therefore con-
tradicts Lemma 1, if

F(k, r){F(k, r) - 1} > 3n (q ,)-1(r2 + r + 1) .

 (18)

To obtain a lower bound for F(k, r), note that for each prime p in (k1/2, k)
we omit at most [k/p] + 1 of the a's ; similarly for the products q 2 and q,qj, so

F(k, r) > k -
 kl

 <k ([
P

k] + 11

 1_ ;<r ([q qj ] + 11

>k -

 I ([p] +1 ) - [

 r
 I + (
i l
 1 2l ]
 -(
 r 2 1) .

kl/z<p<k

For example, with k = 1752 = 30625 and r = 31 (so q, = 29) this bound is
adequate to verify (18). Indeed, for 1000 < k < 30000 we can readily verify
(18), in each case taking q, around k" .

2.5. The case 4 < k < 30000, 1 > 3 . Here it is inconvenient to work with
ratios of products of a's, so we work directly with the products themselves,
since we do not need the extra sharpness .
With the a's selected as in Section 2.3, the inequality corresponding to (17) is

Cf(k, m) + I - 21 > lm .

 (19)
l-1

The left member of (19), derived by counting the number of nondecreasing
sequences of I - 1 a's, is the number of formally distinct products of I - 1 a's,

THE PRODUCT OF CONSECUTIVE INTEGERS

 299

and the right member is the number of lth-power free positive integers with all
prime factors among the first m primes . When (19) holds, (5) has a solution,
contradicting Lemma 1 . It is easy to verify by direct computation that (17)
implies (19) for 4 < k < 1000 and m chosen as in Section 2 .3 .
Similarly, with the a's selected as in Section 2.4, the inequality corresponding

to (18) is C F(k, r) + l - 2~ > 1n(q,)_1 1 + r - 11 .

 (20)
l - 1

 Z - 11

The left member of (20) is the number of formally distinct products of Z - 1 a's,
and the right member is the number of lth-power free positive integers with no
prime factor greater than k 1 / 2 and at most l - 1 prime factors among the q's
(counted by multiplicity) . When (20) holds, (5) has a solution, contradicting
Lemma 1 . For 1000 < k < 30000 and the values of r chosen as in Section 2.4,
(20) easily holds when (18) holds .
This completes the proof of Theorem 2 for I > 2 . It seems certain that one
could get a more general inequality than (19) and (20), leading to a more elegant
method valid for all k .
 3 . The case / = 2

It remains to prove that (n + 1) . . . (n + k) always contains a prime p >- k
to an odd exponent . (We already know that the product is not a square, by the
results of Rigge and Erdös cited earlier.)
The a's are now square-free and, by Lemma 1, all distinct . So, by Lemma 2,

k ai
=1 (k - 1)! [1 p

 (21)
p<k

We shall now show that for k >- 71 this leads to a contradiction.

3.1. The case k >- 71 . Since 12 of every 36 consecutive integers are
divisible by 4 or 9, at most 24 of any 36 consecutive integers are square-free .

Thus for k >- 64 we have
 11 ai > k! -~ .

 (22)
=1

 2

For any positive integer m and prime p, the power to which p divides p'! is
(p' - 1)/(p - 1). From this we can deduce that if the powers to which 2 and

3 divide (k - 1)! are a and /3 respectively, then

a >- k - 1 _1092k and Q >- 1 (k- 1) - log, k .

On the other hand, since the a's arise from k consecutive integers and are square-
free, we calculate that if the powers to which 2 and 3 divide a, a k are y and
S respectively, then

y < 3{k +log e (3k + 1)} and 6 < á{k + 1 + 21093(2k+ 1)} .

300

 P . ERDŐS AND J . L . SELFRIDGE

Since (21) implies that a i

 ak < (k - 1)!21- "3s- Q rlpIk A we now deduce

from (22) that for k >- 64,

_3 22k/3 3k/4 < 14 k2 p
2

 3

 P

However rlp<k p < 3 k, so (23) fails for k >_ 297 . Indeed, rip<k p < ek for
k < 10 $ by Theorem 18 of [7], so (23) fails for k >- 71.

3.2. The case k < 71 . For k = 3, it is impossible for the a's to be distinct .
For k = 4 the only possibility is aI = 1, a 2 = 2, a3 = 3 and a4 = 6 . Then

ala2a 3a4 = 6 2, so (n + 1)(n + 2)(n + 3)(n + 4)

must be a square ; but this product equals (n2 + 5n + 5) 2 - 1 and we have a

contradiction .
For 5 < k < 20, we will count the number of a's with no prime factor

greater than 3 ; if this is at least 5, it is impossible for the a's to be distinct, and

we have a contradiction . This works unless k = 6 and 5 I n + 1, or k = 8,

7 1 n + 1 and 5 1 n + 2 . But in either of these cases we have four consecutive

integers whose product is a square, and this was shown above to be impossible .
Similarly we obtain a contradiction for 20 < k < 56 by noting that there

are at least 9 a's with no prime factor greater than 5, and for 56 < k < 176,

where there are at least 21 a's with no prime factor greater than 7 . (This method

could be extended . For example, with 176 < k < 416 there are at least 42 a's

with no prime factor greater than 11, and with 416 < k < 823 there are at

least 65 a's with no prime factor greater than 13.)
This completes the proof of Theorem 2 .

4. Remarks and further problems

No doubt our method would suffice to show that the product of consecutive
odd integers is never a power, in the sense of (1). In fact, the proof would

probably be simpler . More generally, for any positive integer d there must be

an integer td such that (n + d)(n + 2d) . . . (n + td) is never a perfect power if

t > td. Without td this result fails since x(x + d)(x + 2d) = y 2 has infinitely
many solutions .
By our methods we can prove that for fixed t,

(n + dj . . . (n + dk) = x~, 1 = d i < . . . < dk < k + t

 (24)

has only a finite number of solutions . Our theorem shows that there is no

solution with t = 0 . With t = 1 we have the solutions 4!/3, 6!/5 and 10!/7 ;

perhaps there are no others . _Suppose that t is a function of k, or of k and 1.
How fast must t grow to give an infinite number of solutions to (24)? The

Thue-Siegel theorem implies that (24) has only a finite number of solutions when
dk and 1 are fixed, with I > 2 . For fixed k it seems probable that lim,-~ dk = oo .

(23)

Another question which arises naturally from our method is the following .
Let air) be the largest divisor of n + i which is lth-power free and has all prime
factors less than k. Our proof for 1 = 2 implies that for -1 < i < k, the a~2)
are not all distinct when k + 4, 6, 8. An easy argument also shows that the
ai2) cannot all be distinct when k = 8 . To what extent do these results extend
to I > 2? For how many consecutive values of i can the a,(I) be distinct?
We mention one final problem . Let a I be the largest divisor of n + i which
has all prime factors less than k. Our proof of Theorem 2 shows that for any
n >_ 0 and k >_ 30000, the products a,aj cannot all be distinct. Very likely this
holds for much smaller values of k, perhaps as small as k >_ 16. To see that it

THE PRODUCT OF CONSECUTIVE INTEGERS

 30 1

Acknowledgements . We wish to thank the referee for his comments and
suggestions, and R. B. Eggleton for reorganizing and writing the paper in its
final form .
 REFERENCES

1 . P. ERDŐS, Notes on the product ofconsecutive integers : I and II, J. London Math. Soc., vol .
14 (1939), pp . 194-198 and 245-249 .
2 .	 On the product of consecutive integers III, Indagationes Math ., Vol . 17 (1955),
pp . 85-90.

3.	 A theorem ofSylvester and Schur, J. London Math . Soc ., Vol . 9 (1934), pp . 282-288
4 .	 On some applications ofgraph theory to number theoretic problems, Publ . Ramanujan
Inst ., Vol . 1 (1968-69), pp . 131-136 .
5. R . OBLáTH, Über Produkte aufeinanderfolgender Zahlen, Tohoku Math . J ., Vol . 38 (1933),
pp . 73-92.
6. O . RIGCE, Über ein diophantisches Problem, 9th Congress Math . Scand., pp . 155-160.

(Rigge, in fact, proves a sharper theorem, but it is a special case of our Theorem 2 .)
7. J . B . ROSSER AND L . SCHOENFELD, Approximate formulas for some functions ofprime numbers,

Illinois J . Math., vol . 6 (1962), pp . 64-94 .

NORTHERN ILLINOIS UNIVERSITY
DEKALB, ILLINOIS

does
We

k
 not hold for 3 < k < 16, it suffices to check for k = 3, 5, 7, 11, 13, 15 .
conclude with a table of examples for these cases .

al

 a2 a3 a4 a5 a6

 a7 a8 a9

 alo ai, a12 a13 a14 a,5

3 2

 1

 2,

5 12

 1

 2

 3"1

 222

7 60

 1

 2

 3

 2"1 5,Z 2 .3
"3

11 90

 7,1 2,Z 3

 2

 5a3 12

 1 14

 3"4 40
13 90 11,1 2a2 3

 14

 5"3 12

 1

 2

 3"4 40

 7 a1 66
15 104

 11 ,1 18

 7a2 20

 3

 2

 1

 3 .2
,3 5

 14

 3,4 44 13a s 6 .5a6
