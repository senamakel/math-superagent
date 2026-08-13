<!-- source: https://www.math.tugraz.at/~elsholtz/WWW/papers/papers33FINAL2013.pdf | converted from PDF -->

Illinois Journal of Mathematics
Volume 55, Number 2, Summer 2011, Pages 685–696
S 0019-2082

THE NUMBER OF REPRESENTATIONS OF RATIONALS AS
A SUM OF UNIT FRACTIONS

T. D. BROWNING AND C. ELSHOLTZ

Abstract. For given positive integers m and n,we considerthe
frequency of representations of m
n as a sum of unit fractions.

1. Introduction

This paper centres on the question of representing fractions as sums of
unit fractions. Speciﬁcally, for a positive integer k ≥ 2and given m, n ∈ N,we
would like a better understanding of the counting function

fk(m, n)=#{(t1,...,tk) ∈ Nk : t1 ≤ ··· ≤ tk and m
n = 1
t1 + ··· + 1
tk
 }.

We will be mainly concerned with upper bounds for fk(m, n) which are uni-
form in k, m and n. On observing the trivial upper bound fk(m, n) ≤ fk(1,n),
we will generally be interested in bounds for fk(m, n) that get sharper as the
size of m increases.
The easiest case to deal with is the case k =2, for which we have the
following essentially complete description.

Theorem 1. We have

f2(m, n) ≤ exp
((log 3 + o(1)) log n
log log n
 )
.

Furthermore, for ﬁxed m ∈ N, there are inﬁnitely many values of n for which

f2(m, n) ≫m exp
((
log 3 + o(1)) log n
log log n
 ).

Received December 18, 2009; received in ﬁnal form May 31, 2010.
While working on this paper the ﬁrst author was supported by EPSRC Grant number
EP/E053262/1.
2010 Mathematics Subject Classiﬁcation. 11D68.

685
 c⃝2013 University of Illinois

686 T. D. BROWNING AND C. ELSHOLTZ

When k = 3, the equation appearing in the deﬁnition off 3(m, n)has re-
ceived much attention in the context of the conjecture
1 of Erd˝os and Straus [5].
This predicts thatf 3(4,n ) > 0 for any n  2. The conjecture has since been
generalised to arbitrary numerators by Schinzel [10]. Thus, for any m  4one
expects the existence of Nm  N such thatf 3(m, n) > 0for n  Nm . Both of
these conjectures are still wide open and have generated a lot of attention in
the literature. An overview of the domain can be found in work of the second
author [4]. The following result provides an upper bound forf 3(m, n)which
is uniform inm and n.

Theorem 2. For any > 0, we have

f 3(m, n)  
 θ n
m
  ∈
3 n .

It follows from the theorem thatf 3(m, n)   n ∈3 +  . Numerical experimen-
tation reveals thatf 3(m, n) varies considerably as n varies but nonetheless
ought to correspond to a superposition of divisor functions. Indeed we would
conjecture thatf 3(m, n)   n for any > 0. Moreover, our numerical inves-
tigations lead us to expect thatf 3(m, n)  as n  , for ﬁxed m.
Once the denominators are cleared the equation appearing inf 3(m, n) takes
the shape mxyz = n(xy + xz + yz).

This is one of several ane cubic equations for which the number of solutions
in positive integers is expected to grow like the divisor function. In private
communication with the authors, Brian Conrey has asked whether the number
of solutions in positive integers to the equation

n = xyz + x + y

can be bounded by O (n  ) for any > 0. Kevin Ford 2 has posed a gen-
eralisation of this problem, in which one would like to show that there are
O ((| AB|)  ) nontrivial positive integer solutions to the equationxyz = A(x +
y)+ B, for given nonzero A, B  Z . A further problem of this type has been
posed by Pelling 3, in which it is asked whether there areO (n  ) solutions to
the cubic equation xyz = n(x + y + z),

with x, y, z  N . For this equation, it is known that the relevant counting
function grows at most likeO (n ∞∈ +  ) but the original question is open. We
shall not say anything more about these equations here.

1 The earliest reference in the literature to this conjecture appears to be a paper by Obl´ ath
[ 7], submitted in 1948.
2 First presented at the DIMACS Meeting in Rutgers in 1996.
3 Problem 10745, Solution in: Amer. Math. Monthly 108 (2001), 668–669.

SUM OF UNIT FRACTIONS 687

Recording anything meaningful forf k(m, n)when k  4 seems to be a
harder problem. Nonetheless, we are able to build Theorem2 into an induction
argument which leads us to the following result.

Theorem 3. Let k  4. For any > 0, we have

f 4(m, n)   n ﬃΣ n
m
  5
3 + n 4
3

m 2
3
 ﬀ ,

and for k  5
 f k(m, n)   (kn )  Σ k 4
3 n2

m
  5
3 × 2
k − 5
 .

The special casef k(1, 1) has received special attention in the literature. In
one direction, Croot [2] has solved a dicult problem of Erd˝os by showing that
any ﬁnite colouring of the positive integers allows a monochromatic solution
of the equation

(1) 1 =
 k

i =1
 1
ti

for unspeciﬁed k. In a dierent direction, for givenk  N ,let K (k )= f k(1, 1)
denote the number of vectors (t1,...,tk)  N k witht1  ···  tk,for which (1)
holds. Deﬁne the sequenceun via u1 =1 and un+1 = un (u n +1). This se-
quence grows doubly exponentially and one hasc0 = lim n≥∈ u
2
− n
n =1 .264 ... .
Building on earlier work of Erd˝os, Graham and Straus [6], S´ andor [8] has es-
tablished the upper bound
 K (k ) <c (1+)2 k − 1

0
for any > 0and any k  k(). Taking m = n = 1 in Theorem3, we deduce
the following estimate.

Corollary. For any > 0, we have

K (k )   k 5
9 × 2
k − 3 +  .

For intermediatek,this improves upon S´andor’s result. By revisiting
S´andor’s argument, we achieve the following sharpening for largek.

Theorem 4. Let > 0 and assume that k  k(). Then we have

K (k ) <c ( 5
12 + )2 k − 1

0 .

While interesting in its own right it transpires that the study of Egyptian
fractions has applications to various problems in topology. For example, Bren-
ton and Hall [1] have established a bijection between solutions (t1,...,tk)  N k

to the equation
 1=
 k

i =1
 1
ti +
 k

i =1
 1
ti

688 T. D. BROWNING AND C. ELSHOLTZ

and homeomorphism equivalence classes of homologically trivial complex sur-
face singularities whose dual intersection graph is a star with central weight
1and weightsti on the arms. In [1, Section 4] the authors ask for a bet-
ter understanding of the counting functionS(k )for large k, which is deﬁned
to be the number of solutions (t1,...,tk)  N k to the above equation with
t1  ···  tk. On observing thatS(k )  K (k + 1), we observe the following
trivial consequence of Theorem4.

Corollary. Let > 0 and assume that k  k(). Then we have

S(k ) <c ( 5
12 + )2 k

0 .

2. Sums of two unit fractions

In this section, we establish Theorem1. Beginning with the upper bound,
S´andor [8, Lemma 4]hasshownthat

f 2(m, n)  f 2(1,n )= 1
2δ
d
δ
n2 +1  ,

whered denotes the divisor function. To see this, we note that if
1
n = 1
t1 + 1
t2
thent2 = nt1
t1 − n = n + n 2
t1 − n , which is an integer if and only ift1 − n | n2.The
conditiont1  t2 ensures thatt1  2n,so that 0 <t 1 − n  n and indeed
f 2(1,n )= 1
2(d(n 2) + 1). Applying work of Shiu [ 9] on the maximum order of
multiplicative functions we easily deduce the upper bound in Theorem1.
We now turn to the lower bound forf 2(m, n) for ﬁxed m  N . It will
suce to examine g2(m, n), whichisdeﬁnedasfor f 2(m, n), but without the
restriction thatt1  t2 in each solution. Indeed we plainly have

g2(m, n)  2f 2(m, n).

Let n =
 s
i =1 qi ,where s is odd andqi denotes theith prime which is con-
gruent to−1mod m. Then we claim that

g2(m, n)  3
s

2 .

To see this, letx 1 be the product of any subset of an odd numberi of thes
prime factors. Letx 2 be a product of an even numberj of the remainings − i
prime factors. Thenx 12 = n
x 1 x 2 x 1 + x 2
m is an integer and we have

m
n = 1
x 1x 12 + 1
x 2x 12 .

Counting up the number of availablex 1,x 2 gives the contribution

S1 =
 s

i odd
 s− i

j even
θ s
i
 θ s − i
j
  =
 s

i odd
 θ s
i
  2
s− i − 1.

SUM OF UNIT FRACTIONS 689

Likewise we can instead choosex 1 to consist of an even numberi of thes
primes, and x 2 an odd numberj of the remainings − i primes. This gives the
contribution
 S2 =
 s

i even
 s− i

j odd
  s
i
  s − i
j
  =
 s

i even
 s
i
  2
s− i − 1.

Thus, we deduce that

g2(m, n)  S1 + S2 =
 s
 i =0
  s
i
  2
s− i − 1 = 3
s

2 ,

as required. To complete the proof of the theorem, we note that

n =
 s

i =1qi =exp
  s
 i =1 logqi

 .

By the prime number theorem for arithmetic progressions,

s
 i =1 logqi
 s
 i =1 log
 i(log i)(m)  	 s logs + s log logs + s log(m).

It follows thats 	 logn
log logn +log ( m ) 	 logn
log logn , for ﬁxed m. Therefore, there are

at least
1
43
s = exp((log 3 + o(1)) logn
log logn ) solutions counted by f 2(m, n), which
thereby completes the proof of Theorem1.

3. Sums of three unit fractions

In this section we establish the upper bound in Theorem2 for f 3(m, n).
It will clearly suce to assume that gcd(m, n) = 1. Since t1  t2  t3 in the
deﬁnition of the counting function, it is clear that

(2) n
m <t 1  3n
m .

In particular, we must havem  3n. We can get an upper bound for t2 via
the expression m
n − 1
t1 = 1
t2 + 1
t3  2
t2 .

Suppose thatm<n .Letn = mq + r for 0 <r  m − 1. We have t1 
 n
m  =
q + 1 and it follows that the left hand side is at least

m
mq + r − 1
q +1  1
(q + 1)(mq + r)  m
2(mq + r)(mq + r) = m
2n2  m
3n2 ,

giving

(3) t2  6n 2

m .

690 T. D. BROWNING AND C. ELSHOLTZ

Suppose now thatm>n ,with m  3n.Then we havet1 
 n
m  = 1, whence

m
n − 1  1
n  m
3n2 ,

whence (3) holds in this case also. Once combined with the underlying equa-
tion inf 3(m, n), the inequalities ( 2)and ( 3) are enough to show that

f 3(m, n)  3n
m 6n 2

m = 18n3

m2 .

Proceeding to the proof of the sharper bound in Theorem2, we may henceforth
assume thatt1,t2 satisfy t1  t2 and lie in the ranges given by (2)and ( 3), in
any given solution ( t1,t2,t3)  N 3 counted by f 3(m, n).
In what follows, leti, j, k denote distinct elements from the set{1, 2,3}.
Let
 x 123 = gcd(t 1,t2,t3),x ij = gcd(t i ,tj )
x 123 ,x i = ti
x ij x ik x 123,

withx ij = x ji .Then

(4) t1 = x 1x 12x 13x 123,t2 = x 2x 12x 23x 123,t3 = x 3x 13x 23x 123,

with

(5) gcd(x i x ik ,x j x jk )=1 .

Substituting these values fort1,t2,t3 into the equation in the deﬁnition of
f 3(m, n), we obtain

mx 1x 2x 3x 12x 13x 23x 123 = n(x 1x 2x 12 + x 1x 3x 13 + x 2x 3x 23).

It follows from (5)thatx 1x 2x 3 | n. Since gcd(m, n) = 1, we may conclude that

(6) n = x 1x 2x 3h12h13h23h123,

where
 hij = gcd  n
x 1x 2x 3 ,x ij
  ,h123 = gcd  n
x 1x 2x 3 ,x 123

 .

If we writex ij = hij yij and x 123 = dh123, then we obtain the simpliﬁcation

(7) mdy12y13y23 = x 1x 2h12y12 + x 1x 3h13y13 + x 2x 3h23y23.

Furthermore, we have the additional coprimality relations

gcd(y ij ,hik hjk h123) = gcd(d, h ij )=1 .

Thus, ( 5)and ( 7) imply that any two elements of the set{x 1,x 2,x 3,d} must
be coprime.
Let D> 0. It will be convenient to consider the overall contribution to
f 3(m, n)from x 1,x 2,x 3,d,hij ,h123,yij such that thatd is constrained to lie
in an interval D  d< 2D.

SUM OF UNIT FRACTIONS 691

We will write F(m, n; D) for this quantity. It follows from (2), (3)and ( 4)
that

(8) y12y13 = x 1x 123x 12x 13
x 1x 123h12h13 = t1
x 1h123dh12h13  3n
x 1mh12h13h123D ,

and similarly
 y12y23  6n 2

x 2mh12h23h123D .

We proceed to estimateF(m, n; D) in two dierent ways.

Lemma 1. For any > 0, we have

F(m, n; D)   n1+

mD .

Proof. It follows from (7) that there exists an integerr such that

y23r = x 2h12y12 + x 3h13y13.

For ﬁxed x 2,x 3,h12,h13,y12,y13, the trivial estimate for the divisor function
implies that there areO (n  ) choices for y23,r. Summing overy12,y13,we
conclude from (8) that there areO (m − 1D− 1n1+ ) choices for theyij and r.
Achoiceofd is ﬁxed by ( 7). Since there areO (n  ) possible choices for
x 1,x 2,x 3,hij ,h123,by( 6), so it follows that

F(m, n; D)   

x∞ ,x ∈ ,x 3 ,h ij ,h ∞∈3
 n1+

mD   n1+2

mD .

The statement of the lemma follows on redeﬁning the choice of> 0. ε

Lemma 2. For any > 0, we have

F(m, n; D)   D ∞
∈ n ∞∈ + 

m ∞∈ .

Proof. Assume without loss of generality thaty12  y13. Fixing y12,we
then estimate the number of integersA, B  n2 for which

mdy12AB = x 1x 2h12y12 + x 1x 3h13A + x 2x 3h23B.

But we may rewrite this equation as

(mdy 12A − x 2x 3h23)(mdy 12B − x 1x 3h13)= mx 1x 2dh12y
2
12 + x 1x 2x 2
3h13h23.

For eachx 1,x 2,x 3,d,hij ,h123,y12, there are clearlyO (n  ) possible values of
A, B, by elementary estimates for the divisor function. Moreover, (8)and the
assumptiony12  y13 together imply that y12   n
mD . Thus, we obtain the
bound
 F(m, n; D)   

x∞ ,x ∈ ,x 3 ,d,h ij
 n ∞∈ + 

(mD ) ∞∈   D ∞
∈ n ∞
∈ +2

m ∞∈ ,

692 T. D. BROWNING AND C. ELSHOLTZ

on summing over values ofd in the rangeD  d< 2D,and the O (n  )pos-
sible values ofx 1,x 2,x 3,hij ,h123 for which (6) holds. The lemma follows on
redeﬁning the choice of> 0. 

We are now ready to complete the proof of the theorem. There areO(log n)
possible dyadic ranges ford, such thatd  n. Theorem2 therefore follows on
applying Lemma 1 to deal with the contribution fromd  ( n
m ) 13 , and Lemma2
to handled< ( n
m ) 13 .
 4. Sums of k unit fractions

In this section, we establish Theorems3 and4. Beginning with the former,
let ( t1,...,tk )  N
k be a point witht1  t2  ···  tk counted by f k (m, n).
Then mt1 − n
nt1 = m
n − 1
t1 = 1
t2 + ··· + 1
tk .

It is easy to see thatf k (m, n) = 0 unless m  kn which we now assume.
Furthermore, the analogue of (2) in the preceding section is clearly

(9) n
m <t 1  kn
m .

Our induction is based on the observation that

f k (m, n)  ∞

t1 f k − 1(mt 1 − n, nt1),

where the summation is overt1  N for which (9) holds. Making the change
of variablesu = mt1 − n, we obtain

(10) f k (m, n)  ∞

0<u ( k − 1) n
m | u + n
 f k − 1
≤
u, n(u + n)
m
 →
.

Note thatu + n  kn for eachu under consideration.
Let > 0. We begin by establishing the theorem in the casek =4. It
follows from Theorem2 that

f 4(m, n)   n ∞

0<u 3n
m | u + n
 ≤ n ( u + n )
m
u
 →23   n 43 + 

m 23
 ∞

0<u 3n
m | u + n
 u
− 23 .

Given   [0, 1), we now require the estimate

S (x)= ∞

n  x
n  a mod q
 n−  = x 1− 

(1 −  )q + O (1),

which is valid uniformly fora  Z and q  N. This follows from combining
partial summation with the familiar estimateS0(x)= q
− 1x + O(1). If   1+ 

SUM OF UNIT FRACTIONS 693

for some ﬁxed > 0, then S (x)   1. We may now conclude that

(11) f 4(m, n)   n 43 + 

m 23
  n 13
m +1  .

This establishes the theorem in the casek = 4. Turning to the casek =5, we
repeat the above analysis based on (10), but use the inequality in (11)asour
bound forf 4(m, n). It follows that

f 5(m, n)   n 

0<uΣ 4n
m |u+ n
  m
− 1n2

u
  53 + (m − 1n2) 43

u 23
    n  n2

m
  53 ,

which thereby establishes the theorem whenk =5.
It remains to establish Theorem3 fork  6. We will begin by showing that

(12) f k(m, n)  ,k n  n2

m
  53 × 2
k − 5

for k  5, where the implied constant is allowed to depend onk. This will be
achieved by induction onk, the case k = 5 already having been dealt with.
When k  6, we deduce from the induction hypothesis and (10)that

f k(m, n)  ,k n 

0<uΣ ( k− 1) n
 n2(u + n) 2

um2
  53 × 2
k − 6
  ,k n  n2

m
  53 × 2
k − 5
 ,

since 5
3 × 2
k− 6  5
3 for k  6. This therefore establishes (12).
We now turn to a bound forf k(m, n) which is uniform ink, which we will
again achieve via induction onk.Let > 0. We will take for our induction
hypothesis the estimate

(13) f k(m, n)   (kn )   k
 k n2

m
  53 × 2
k − 5

for an undetermined function k. We may henceforth suppose that

(14) k  log 3− log(5 )
log 2 +5 ,

else (13) follows trivially from (12). Now for any L  k it follows from (10)
that
 f k(m, n)  

0<uΣ ( L − 1) n
m |u+ n
 f k− 1
 u, n(u + n)
m
 

+ 

( L − 1) n<uΣ ( k− 1) n
m |u+ n
 f k− 1
 u, n(u + n)
m
  .

694 T. D. BROWNING AND C. ELSHOLTZ

One notes thatu + n  Ln in theﬁrstsum andu + n  kn in the second. The
induction hypothesis therefore gives

f k (m, n)   (kn )  k
 5  k − 1
3 × 2
k − 6 ≥≤Ln2

m
 →53 × 2
k − 5
  1 + ≤kn
2

m
 →53 × 2
k − 5
  2
∈,

where

 1 = ∞

0<uθ ( L − 1) n
≤ 1
u
 →53 × 2
k − 6
  1,

 2 = ∞

( L − 1) n<uθ ( k − 1) n
≤ 1
u
 →53 × 2
k − 6
  ∞

u  L
 ≤ 1
u
 →53 × 2
k − 6
  L1− 53 × 2
k − 6 .

We deduce that

f k (m, n)   (kn )  ≤k
  k − 1
2 n2

m
 →53 × 2
k − 5 ≥
L + k
≤ 1
L
 →12 − 35 2
− ( k − 5) ∈ 53 × 2
k − 5
 .

Now (14) ensures that
1
2 − 3
5 × 2
− ( k − 5)  1
2 −  . Hence, on takingL = k 23 ,we
conclude that

f k (m, n)   k
(1+ 59 × 2
k − 4 ) n ≤k
  k − 1
2 + 23 n2

m
 →53 × 2
k − 5
 .

Redeﬁning the choice of therefore leads us to the induction hypothesis (13)
with
  k =  k − 1
2 + 2
3.

It is now easy to deduce that k < 4
3 , which completes the proof of Theorem3.
We now turn to the proof of Theorem4, for which we will modify the
argument in [8]. Recall the deﬁnition of the sequenceun from the introduction
and letc0 = lim n εϕ u
2
− n
n . Since u
2
− n
n is monotonically increasing we have
un <c 2
n
0 . Suppose that 1 =  k
i =1 1
ti ,with t1  ···  tk . Then Curtiss [3]has
shown that
 1 −
 m∞

i =1
 1
ti  1
um +1

for 1 m  k − 1. It follows thattj  (k − j +1) uj for eachj since otherwise

1=
 k∞

i =1
 1
ti =
 j − 1∞

i =1
 1
ti +
 k∞

i =j
 1
ti < 1 − 1
uj + k − j +1
(k − j +1) uj =1 ,

which is a contradiction.

SUM OF UNIT FRACTIONS 695

Let > 0and let L be chosen to be the least positive integer for which
2
4− L < 
2 . The number of tuples (t1,...,tk − L )with tj  (k − j +1) uj is
therefore k − L

j =1(k − j +1) uj  k!
 k − L

j =1 c
2
j
0 <k ! c
2
k − L +∞
0 .

For a given ( t1,...,tk − L )-tuple, it remains to estimate the number of vectors
(t k − L +1 ,...,tk ) that complete the sum
 k
i =1 1
ti =1. We write

1 − 1
t1 − ··· − 1
tk − L = m
n ,

wheren  t1 ··· tk − L <k ! c
2
k − L +∞
0 . Applying Theorem 3 we deduce that the
number of available (tk − L +1 ,...,tk )is at most

f L (m, n)    k! c
2
k − L +∞
0  ∞0 3 × 2
L − 5 +    (k !) ∞0 3 × 2
L − 5 +  c
 ∞0 3 × 2
k − 4 + 
0

for any > 0. Combining our two estimates, we may now conclude that

K (k )   (k !) e L × c
2
k − L +∞
0 × c
 ∞0 3 × 2
k − 4 + 
0   (k !) e L c
( ∞0 3 + ) × 2
k − 4

0 ,

whereeL =1 + 10
3 × 2
L − 5 +  . This therefore concludes the proof of Theorem4
on redeﬁning the choice of.
 References

[1] L. Brenton and R. Hill, On the Dio√hantine equation 1=  1/n i +1 /
 ni and a class
of homologically trivial com√lex surface singularities, Paciﬁc J. Math. 133 (1988), 41–
67. MR 0936356
[2] E. S. Croot III, On a coloring conjecture about unit fractions, Ann. of Math. 157
(2003), 545–556. MR 1973054
[3] D.R.Curtiss, On Kellogg’s Dio√hantine ∑roblem , Amer. Math. Monthly 29 (1922),
380–387. MR 1520110
[4] C. Elsholtz, Sums of k unit fractions , Trans. Amer. Math. Soc. 353 (2001), 3209–3227.
MR 1828604
[5] P. Erd˝ os, Az 1
x ∞ + 1
x ∈ + ··· + 1
x n = a
b egyenlet eg´ esz sz´ am´ u megold´ asair´ ol (On a Dio-
√hantine equation), Mat. Lapok 1 (1950), 192–210. MR 0043117
[6] P. Erd˝os and R. L. Graham, Old and new √roblems and results in combinatorial number
theory , Monographies de L’Enseignement Math´ ematique, vol. 28, Universit´ edeGen`eve
L’Enseignement Math´ ematique, Geneva, 1980. MR 0592420
[7] M.R.Obl´ ath, Sur l’ ´ equation dio√hantienne 4
n = 1
x ∞ + 1
x ∈ + 1
x 3 ,Mathesis 59 (1950),
308–316. MR 0038999
[8] C. S´ andor, On the number of solutions of the Dio√hantine equation  n
i =1 1
x i =1,
Period. Math. Hungar. 47 (2003), 215–219. MR 2025624
[9] P. Shiu, The maximum order of multi√licative functions ,Q.J.Math. 31 (1980), 247–
252. MR 0576341
[10] W. Sierpi´ nski,Sur les d´ ecom√ositions de nombres rationnels en fractions √rimaires ,
Mathesis 65 (1956), 16–32. MR 0078385

696 T. D. BROWNING AND C. ELSHOLTZ

T. D. Browning, School of Mathematics, University of Bristol, Bristol BS8
1TW, UK
E-mail address : t.d.browning@bristol.ac.uk
C. Elsholtz, Institut f ¨ur Mathematik A, Technische Universit ¨at Graz, Steyr-
ergasse 30, A-8010 Graz, Austria

E-mail address : elsholtz@math.tugraz.at
