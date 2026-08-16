<!-- source: https://arxiv.org/pdf/1011.6083v4 | converted from PDF -->

arXiv:1011.6083v4  [math.NT]  1 Apr 2012
ON STEPHAN’S CONJECTURES CONCERNING PASCAL
TRIANGLE MODULO 2 AND THEIR POLYNOMIAL
GENERALIZATION

VLADIMIR SHEVELEV

Abstract. We prove a series of Stephan’s conjectures concerning Pas-
cal triangle modulo 2 and give a polynomial generalization.

1. Introduction

Consider Pascal triangle for binomial coeﬃcient modulo 2. If to read
every row of this triangle as a binary number, then we obtain the following
sequence {c(n)}n≥0 (cf. A001317 in [11]):

(1.1) 1, 3, 5, 15, 17, 51, 85, 255, 257, 771, 1285, 3855, 4369, 13107, 21845, ...

It is easy to see that

(1.2) c(2n) ≡ 1 (mod 4), n = 0, 1, ...

Denote

(1.3) l(n) = c(2n) − 1
4 .

In 2004, for sequence {l(n)}n≥0, R. Stephan formulated a series of the fol-
lowing conjectures (cf. his comments to A089893 in [11]):

Conjecture 1.

(1.4) l(2k) = 22k+1−2.

Conjecture 2.

(1.5) lim
n→∞ l(2n + 1)/l(2n)) = 5.

Conjecture 3.

(1.6) lim
n→∞ l(4n + 2)/l(4n + 1)) = 17/5.

Conjecture 4.

(1.7) lim
n→∞ l(8n + 4)/l(8n + 3)) = 257/85.

1991 Mathematics Subject Classiﬁcation. 11B65.
1

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 2

etc.
We add that Moscow PhD student S. Shakirov conjectured (private com-
munication) that a generating function for sequence {c(n)} is

(1.8)
 ∞∏

k=0
(1 + x
2k + (2x)2k ) =
 ∞∑

n=0 c(n)x
n.

In this paper we prove these conjectures and give a polynomial general-
izations.
 2. On sequence A001317

Consider an inﬁnite in both sides (0, 1)-sequence with a ﬁnite set of 1’s
which we call C-sequence. Removing in it all 0’s before the ﬁrst 1 and
after the last 1, we obtain some odd number which we call the kernel of C-
sequence. Every C-sequence generates a new C-sequence, if to write sums
of every pair of its adjacent terms modulo 2. If to consider inﬁnite iterations
of such process beginning with C-sequence with kern 1, then we obtain C-
sequences, the kernels {c(i)}i≥0 of which form Pascal’s triangle for binomial
coeﬃcients modulo 2. Note that, c(0) = 1 and c(i) contains i + 1 binary
digits.
Consider now sequence {d(n)} deﬁned by the formula d(0) = 1; for n ≥ 1,
if binary expansion of n is

(2.1) n =
 m∑

i=1 2ki,

then

(2.2) d(n) =
 m∏

i=1 F (ki),

where

(2.3) F (n) = 22n + 1, n ≥ 0,

is Fermat number. Such decomposition of d(n) we call its Fermat factoriza-
tion.
From (2.1)-(2.2) immediately follows a generating function for {d(i)} :

(2.4)
 ∞∏

k=0
(1 + F (k)x
2k ) =
 ∞∑

n=0 d(n)x
n, 0 < x < 1
2 .

Note that sequence {d(i)} possesses the following properties:
1) d(n) is a binary number with n + 1 (0, 1)-digits;
2) numbers {d(i)} are 1 and all Fermat numbers or products of distinct
Fermat numbers;

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 3

3) number of Fermat factors in the product equals to d(n) is the number
of 1’s in the binary expansion of n.
4) F (i) divides d(n), n > 1, if and only if it is a factor in product (2.2).
Proofs of these properties is very easy: 1) follows from a simple induction;
2) and 3) follow from the deﬁnition; 4) follows from the well known fact (cf.,
e.g., [12]) that every two Fermat numbers are relatively prime, in view of
recursion

(2.5) F (n) = 2 +
 n−1∏

i=0 F (i).

Theorem 1. For n = 0, 1, ..., we have

(2.6) c(n) = d(n).

Proof. We use induction, the base of which is c(0) = d(0) = 1, c(1) =
d(1) = 3, c(2) = d2 = 5. Suppose that c(i) = d(i), for i ≤ k. Let m
be the most number for which F (m) divides c(k) = d(k). In non-trivial
case, when c(k) ̸= F (m), using property 4), for some r < k, we have
c(k) = d(r)F (m) = c(r)F (m). Furthermore, since, by the condition, F (m)
is the most Fermat divisor of c(k) and, in view of (2.5), we have

(2.7) c(r) = c(k)
F (m) ≤
 m−1∏

i=0 F (i) = F (m) − 2.

Besides, since c(r) < c(k), then, by the inductive supposition,

c(r + 1) = d(r + 1).

Adding the case when c(k) = F (m), let us prove a recursion: c(0) =
1, c(1) = 3, c(2) = 5; for k ≥ 2,

(2.8) c(k + 1) =
 




3F (m), if c(k) = F (m),
F (m + 1), if 1 < c(r) = F (m) − 2,
F (m)c(r + 1), if 1 < c(r) < F (m) − 2.

Let c(k) = F (m), m ≥ 1. C-sequence with kernel c(k) is

...01 0...0︸︷︷︸
2m−1 10...

Thus the following C-sequence with kernel c(k + 1) is

...011 0...0︸︷︷︸
2m−2 110...

Comparing kernels c(k) and c(k + 1), we conclude that c(k + 1) = 3c(k) =
3F (m).
 ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 4

Furthermore, if c(r) = F (m) − 2, then, by (2.7), we have

c(k) = F (m)c(r) = F (m)(F (m) − 2) = F (m + 1) − 2 = 11...1︸ ︷︷ ︸
2m+1 .

Thus the C-sequence with kernel c(k) is

...0 11...1︸ ︷︷ ︸
2m+1 0...

Therefore, by the deﬁnition, the C-sequence with kernel c(k + 1) is

...01 0...0︸︷︷︸
2m+1−1 10...

and we see that c(k + 1) = F (m + 1).
Let now c(r) < F (m) − 2. Since, by the supposition of induction, c(r) =
d(r). Therefore, c(r) is a product of Fermat numbers and

c(r) ≤ ∏m−1
i=0 F (i)
F (0) = F (m) − 2
F (0) .

Hence, c(r) is not more than (2m − 1)-digits odd binary number. Since

c(k) = F (m)c(r) = 22mc(r) + c(r),

then c(k) has the binary expansion of the form

(2.9) c(k) = c(r) 0...0︸︷︷︸
l c(r),

where l ≥ 1.
Passing on to the following kernel, we have:

c(k + 1) = c(r + 1) 0...0︸︷︷︸
l−1 c(r + 1),

where l − 1 ≥ 0. Thus

c(k + 1) = c(r + 1)22m + c(r + 1) = c(r + 1)F (m).

This completes formula (2.8). From this formula we conclude that c(k + 1)
is a term of sequence {d(i)}. Moreover, since c(k + 1) contains k + 2 binary
digits, then, in view of property 1) of numbers {d(i)}, both of c(k + 1) and
d(k + 1) contain (k + 2) binary digits. Therefore, c(k + 1) = d(k + 1).■

Remark 1. In proof of Theorem 1 we essentially followed to our arguments
from preprint [9], 1991.

Remark 2. Hewgill [4], for the ﬁrst time, found a relationship between
Pascal’s triangle modulo 2 and Fermat numbers. In fact, using a simple
induction, he proved the following explicit formula for the binary represen-
tation of cn:

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 5

cn = (
⌊log2 n⌋∏

i=0 F (⌊ n
2i ⌋ (mod 2))
i )2.

Remark 3. Karttunen [6] gave a representation of cn in the Fibonacci num-
ber system.

Corollary 1. Conjectural generating formula (1.8) is true.

Proof. According to (2.4) and Theorem 1, we have

(2.10)
 ∞∏

k=0
(1 + F (k)x
2k) =
 ∞∑

n=0 c(n)x
n, 0 < x < 1
2 .

It is left to note that

1 + F (k)x
2k = 1 + x
2k + (2x)2k.■

Denote s(n) the number of 1’s in the binary expansion of n.

Corollary 2. a) Number of factors in Fermat factorization of c(n) is s(n).
b) Moreover, the following formula holds

(2.11) s(c(n)) = 2s(n).

Proof. a) follows from Theorem 1 and property 3) of numbers {d(n)}.
b) Let, ﬁrstly, c(k) be not a Fermat number and, as in proof of The-
orem 1, m be the most number for which F (m) divides c(k), such that
c(k) = F (m)c(r). Since the diﬀerence between numbers of factors in Fer-
mat factorization of c(k) and c(r) is 1, then, according to a), we have

s(k) = s(r) + 1.

Now we use induction. If the statement is true for i ≤ k − 1, then, in
particular, s(c(r)) = 2s(r). Therefore, by (2.9), we have

s(c(k)) = 2s(c(r)) = 2 · 2s(r) = 2s(r)+1 = 2s(k).

It is left to consider case c(k) = F (l). Here, by a), s(k) = 1 and (2.9) satis-
ﬁes trivially. ■
Note that point b) of Corollary 2 means that the number of odd bino-
mial coeﬃcient in n-th row of Pascal triangle is 2s(n). It is known result
of J.Glaisher [2]. His proof was based on well known Lucas (1878) com-
parison modulo 2: if the binary representations of numbers m ≥ t are
m = m1...mk, t = t1...tk (with, probably, some ﬁrst ti = 0), then

(
n
t
 ) ≡
 m∏

i=0
 (ni
ti
 ) (mod 2).

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 6

In [3] A.Granville gives a new interesting proof of Glaisher’s result. Our
proof is the third one. Generalizations in other directs see in [1], [3], [5], [8],
[10].

Corollary 3. If F (m) is the most Fermat divisor of numbers c(k − 1) and
c(l − 1) from interval (1, F (m) − 2), then

(2.12) c(k − 1)c(l) = c(l − 1)c(k).

Proof. Using (2.8), we have

c(k) = c(k − 1)F (m), c(l) = c(l − 1)F (m)

and (2.12) follows. ■

Corollary 4. If k = 2ml + 2m−1, m ≥ 1, then

(2.13) c(k) = c(2ml)F (m − 1).

Proof. From (2.1)-(2.2), we immediately have d(k) = d(2ml)F (m − 1),
and (2.13) follows from Theorem 1. ■

3. Proof of Conjecture 1

Now proof of Conjecture 1 is especially simple. Indeed, in view of (1.3)
and (2.3), formula (1.4) of Conjecture 1 can be rewritten as

(3.1) c(2n) = F (n),

where n = k + 1 ≥ 1.
According to Corollary 1a), number c(2n) has only one Fermat factor,
i.e., for some t, we have c(2n) = Ft. Besides, by the deﬁnition, c(2n) has
2n + 1 binary digits. It is left to notice that, the unique Fermat number
having 2n + 1 binary digits is F (n), i.e., t = n and c(2n) = F (n).■
In addition, prove that

(3.2) c(2n − 1) = F (n) − 2.

Indeed, by the deﬁnition of sequence {d(n)} and (2.3), we conclude that
F (n) − 2, as a product of distinct Fermat numbers, is a term of sequence
{d(i)} and thus, by Theorem 1, is a term of sequence {c(i)}. Now it is left
to notice that numbers c(2n − 1) and F (n) − 2 have the same number (2n)
of binary digits. ■

4. Proof of Conjectures 2, 3, 4, etc.

Lemma 1. For every n ≥ 0, t ≥ 1 we have identity

(4.1) (F (t − 1) − 2)c(2tn) = c(2tn + 2t−1 − 1).

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 7

Proof. As in proof of (3.2), we conclude that (F (t−1)−2)c(2tn) is a term
of sequence {c(i)}. Note that number c(2tn + 2t−1 − 1) has 2tn + 2t−1 binary
digits. Besides, number F (t − 1) − 2 = 1...1︸︷︷︸
2t−1 and c(2tn) has 2tn + 1 binary

digits. Therefore, number (F (t−1)−2)c(2tn) contains not less binary digits
than number 1...1︸︷︷︸
2t−1 0...0︸︷︷︸
2tn , i.e. (F (t − 1) − 2)c(2tn) has not less than 2t−1 + 2tn

binary digits. On the other hand, (F (t − 1) − 2)c(2tn) contains not more
binary digits than number

1...1︸︷︷︸
2t−1 1...1︸︷︷︸
2tn = (22t−1 − 1)(22tn − 1) ≤ 22t−1+2tn − 1,

i.e., (F (t − 1) − 2)c(2tn) has not more than 2t−1 + 2tn binary digits. Thus
number (F (t − 1) − 2)c(2tn) has exactly 2t−1 + 2tn binary digits. Conse-
quently, two terms (F (t − 1) − 2)c(2tn) and c(2tn + 2t−1 − 1) of sequence
{c(i)} has the same number of digits. Therefore, equality (4.1) holds. ■

Lemma 2. For every n ≥ 0, t ≥ 1, we have identities

(4.2) (F (t − 1) − 2)c(2tn + 2t−1) = F (t − 1)c(2tn + 2t−1 − 1),

(4.3) (F (t − 1) − 2)c(2tn + 2t−1) = 3F (t − 1)c(2tn + 2t−1 − 2).

Proof. Multiplying (4.1) by F (t − 1) and using formula (2.13) of Corol-
lary 4 (for l = n and m = t), we obtain (4.2). Furthermore, if to take in
Corollary 4 m = 1, l = 2t−1n + 2t−2 − 1, then, in view of F (0) = 3, we have
c(2tn + 2t−1 − 1) = 3c(2tn + 2t−1 − 2), and (4.3) follows. ■

Now we are able to get a proof of Conjectures 2, 3, 4, etc. According to
(1.3), we have

(4.4) c(2n) = 4l(n) + 1.

Let in (4.3) t ≥ 2. Then, by (4.4), we have

(F (t − 1) − 2)(4l(2t−1n + 2t−2) + 1) = 3F (t − 1)(4l(2t−1n + 2t−2 − 1) + 1),

or 4l(2t−1n + 2t−2) + 1
4l(2t−1n + 2t−2 − 1) + 1 = 3F (t − 1)
F (t − 1) − 2 .

Hence, we ﬁnally ﬁnd

(4.5) lim
n→∞ l(2t−1n + 2t−2)
l(2t−1n + 2t−2 − 1) = 3F (t − 1)
F (t − 1) − 2.

■
 ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 8

So, if t = 2, 3, 4, 5, ..., then the right hand side is
3 · 5
5 − 2 = 5, 3 · 17
17 − 2 = 17
5 , 3 · 257
257 − 2 = 257
85 , 3 · 65537
65537 − 2 = 65537
21845, ...

respectively.

5. Second proof of key identity (4.3) based on notion of
orthogonality of nonnegative integers

We can essentially simplify our proof of Stephan’s conjectures by a sim-
pliﬁcation of key identity (4.3). Put to every nonnegative integer n to one-
to-one correspondence (0, 1)-vector n by the rule: if the binary expansion
of n is n = n1...nm, then

(5.1) n = ...0...0n1...nm

with inﬁnitive 0’s before n1. For two integers u ≤ v with vectors u =
...0...0u1...ul and v = ...0...0v1...vm, l ≤ m introduce ”circ-product” by
formula ( which is, for the corresponding vectors, similar to dot-product)

(5.2) u ◦ v = uv = ulvm + ul−1vm−1 + ... + u1vm−l+1.

Deﬁnition 1. We call two non-negative integers u, v mutually orthogonal
(u⊥v), if u ◦ v = 0.

Note that if (u⊥v), then the sets of positions of 1’s in their binary repre-
sentations do not intersect.
An important source for obtaining various identities for numbers {c(n)}
is the following exponential-like ”addition theorem”.

Lemma 3. If n1⊥n2, then

(5.3) c(n1 + n2) = c(n1)c(n2).

Proof. Let n1 ≥ n2 and the binary expansions of n1 and n2 be n1 =
∑m
i=1 2ki and n2 = ∑m
j=1 2lj (with, probably, some ﬁrst li = 0). Since
n1⊥n2, then ki ̸= lj, i, j = 1, ..., m. Thus the binary expansion of n1 + n2
is ∑m
i=1 2ki + ∑m
j=1 2lj . Therefore, according to (2.1)-(2.2), we have

c(n1 + n2) = (
 m∏

i=1 F (ki))(
 m∏

j=1 F (lj)) = c(n1)c(n2).■

Second proof of (4.3).
a)Using the notion of numbers orthogonality, we immediately obtain for-
mula (4.2) by the following way.
By (3.2), we have

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 9

(5.4) F (t − 1) − 2 = c(2t−1 − 1).

Since, evidently, (2t−1 − 1)⊥(2tn + 2t−1), then, using (5.3)-(5.4), we ﬁnd

(F (t − 1) − 2)c(2tn + 2t−1) = c(2tn + 2t−1 + 2t−1 − 1) = c(2tn + 2t − 1).

On the other hand, since 2t−1⊥(2tn + 2t−1 − 1), then

F (t − 1)c(2tn + 2t−1 − 1) = c(2t−1)c(2tn + 2t−1 − 1) = c(2tn + 2t − 1).

Thus we conclude that (4.2) holds.
b) Note now that, 1⊥2tn + 2t − 2. Thus 3c(2tn + 2t−1 − 2) = c(2tn + 2t−1 − 1)
and (4.3) follows as well.■
Further we consider a polynomial generalization.

6. Polynomials pn(z), qn(z) and their properties

Consider sequence of polynomials (cf.[3])

(6.1) pn(z) = 1
2
 n∑

i=0 (1 − (−1)(n
i))zi, n = 0, 1, ..., z ∈ C,

such that

(6.2) pn(0) = 1, pn(1) = 2s(n), pn(2) = c(n).

The second equality we have in view of (2.9).
By the same way, one can prove a generalization of Theorem 1.

Theorem 2. For n ≥ 1, we have the following decomposition of pn(z) :

(6.3) pn(z) =
 m∏

i=0(z2ki + 1),

if the binary expansion of n is

(6.4) n =
 m∑

i=0 2ki.

Thus a generating function for polynomials {pn(z)} is

(6.5)
 ∞∏

k=0
(1 + (z2k + 1)x
2k ) =
 ∞∑

n=0 pn(z)x
n, 0 < x < 1
|z| .

In particular, we have

(6.6) p2n(z) = z2n + 1.

Note that, if n has binary expansion (6.4), then 2n = ∑m
i=0 2ki+1. Since
z2ki +1 = (z2)2ki , then we have

(6.7) p2n(z) =
 m∏

i=0((z2)2ki + 1) = pn(z2).

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 10

Analogously, since 2n + 1 = 1 + ∑m
i=0 2ki+1, then

(6.8) p2n+1(z) = (z + 1)
 m∏

i=0((z2)2ki + 1) = (z + 1)pn(z2).

Formulas (6.7)-(6.8) give a simple recursion for polynomials {pn(z)}, which
recently were obtained by S. Northshield (cf. [7], Lemma 3.1) in a quite
another way.
Note that every two diﬀerent polynomials in sequence {p2i(z) = z2i +1}i≥0
are respectively prime. It follows from the identity

(6.9) p2n(z) = 2 + (z − 1)
 n−1∏

i=0 p2i(z).

Put

(6.10) Fn(z) = p2n(z) = z2n + 1.

The following identity holds (cf. [9])

(6.11)
 ∞∑

n=0
 1
pn(z)s =
 ∞∏

k=0
(1 + Fk(z)−s), |z| > 1, ℜs > 0.

In particular, for z = 2, s = 1, we have

(6.12)
 ∞∑

n=0
 1
c(n) =
 ∞∏

k=0
(1 + F −1
k ) = 1.700735495... .

According to Theorem 2 and in view that s(n) ≡ mn (mod 2), where mn =
0, 1, 1, 0, 1, 0, 0, 1, 1... is Thou-Morse sequence, together with (6.11), we have
also

(6.13)
 ∞∑

n=0
 (−1)mn

pn(z)s =
 ∞∏

k=0
(1 − Fk(z)−s), |z| > 1, ℜs > 0.

Let us show that, in particular, for s = 1, we have

(6.14)
 ∞∑

n=0
 (−1)mn

pn(z) = 1 − 1
z , |z| > 1.

Indeed, since
 1 − 1
Fn(z) = (1 + 1
z2n )−1,

then ∞∏

k=0
(1 − Fk(z)−1) =
 ∞∏

k=0
(1 + 1
z2n )−1

and it is left to note that

(6.15)
 ∞∏

n=0
(1 + 1
z2n ) = 1 − 1
z .

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 11

In particular, together with (6.12), for z = 2, we ﬁnd

(6.16)
 ∞∑

n=0
 (−1)mn

c(n) = 1
2.

In addition, note that, if to consider all diﬀerent ﬁnite products of not
necessarily distinct polynomials from sequence {pn(z)}, then we obtain a
sequence of polynomials qn(z) :

q0(z) = 1, q1(z) = z + 1, q2(z) = z2 + 1, q3(z) = (z + 1)2,

(6.17) q4(z) = (z + 1)(z2 + 1), q5(z) = z4 + 1, q6(z) = (z2 + 1)2.

For these polynomials, together with (6.11), we have the following analog
of Euler identity for primes:

(6.18) ∏

F ∈F (z)
(1 − F −s)−1 =
 ∞∑

n=0
 1
qn(z))s , |z| > 1, ℜs > 0,

where F (z) = {Fn(z)}n≥0.

In particular, for s = 1, using (6.15), we have

∞∑

n=0
 1
qn(z) = ∏

F ∈F (z)
(1 − F −1)−1 =

(6.19)
 ∞∏

n=0
(1 + 1
z2n )−1 = z
z − 1, |z| > 1.

Furthermore, introducing an analog of M¨obius function

(6.20) ν(n) =
 {(−1)mn, if n is squaref ree,
0, otherwise,

we get

(6.21)
 ∞∑

n=0
 ν(n)
qn(z)s = ∏

F ∈F (z)
(1 − F −s), |z| > 1, ℜs > 0.

In particular, for s = 1, we have

(6.22)
 ∞∑

n=0
 ν(n)
qn(z) = 1 − 1
z , |z| > 1.

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 12

7. Polynomial generalization of Stephan’s relations

Now we consider a polynomial generalization of formulas of the previous
sections which leads us to the corresponding generalization of Stephan’s
relations. Since proof of the generalized formulas is quite analogous, then
we restrict ourself only by writing of the chain of them. For |z| > 1, we
have

(7.1) p2n−1 = Fn(z) − 2
z − 1 .

This formula generalizes (3.2). Furthermore, the following generalization of
(2.13) holds:

(7.2) p2ml+2m−1(z) = p2ml(z)Fm−1(z).

In particular, taking in (7.2) m = 1, l = 2t−1n + 2t−2 − 1, in view of
F0(z) = z + 1, we ﬁnd

(7.3) p2tn+2t−1−1(z) = (z + 1)p2tn+2t−1−2(z).

After that the corresponding generalization of formulas (4.1)-(4.3) is ob-
tained. We have

(7.4) (Ft−1(z) − 2)p2tn(z) = p2tn+2t−1−1(z),

(7.5) (Ft−1(z) − 2)p2tn+2t−1(z) = (z − 1)Ft−1(z)p2tn+2t−1−1(z),

(7.6) (Ft−1(z) − 2)p2tn+2t−1(z) = (z2 − 1)Ft−1(z)p2tn+2t−1−2(z).

Note that

(7.7) p2n(z) ≡ 1 (mod z2).

Put

(7.8) ln(z) = p2n(z) − 1
z2 .

Let in (7.6) t ≥ 2. Then we have
(7.9)
(Ft−1(z) − 2)(z2l2t−1n+2t−2(z) + 1) = (z2 − 1)Ft−1(z)(z2l2t−1n+2t−2−1(z) + 1),

or

(7.10) z2l2t−1n+2t−2(z) + 1
z2l2t−1n+2t−2−1(z) + 1 = (z2 − 1)Ft−1(z)
Ft−1(z) − 2
and, consequently,

(7.11) lim
n→∞ l2t−1n+2t−2(z)
l2t−1n+2t−2−1(z) = (z2 − 1)Ft−1(z)
Ft−1(z) − 2 .

In particular, for t = 2,

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 13

lim
n→∞ l2n+1(z)
l2n(z) = z2 + 1;

for t = 3,
 lim
n→∞ l4n+2(z)
l4n+1(z) = z4 + 1
z2 + 1 ;

for t = 4,
 lim
n→∞ l8n+4(z)
l8n+3(z) = z8 + 1
(z4 + 1)(z2 + 1), etc.

In case of z = 2, we again obtain formulas (1.5)-(1.7).

References

[1] W. B. Everett, Number of binomial coeﬃcients divisible by a ﬁxed power of a
prime, INTEGERS, 8 (2008), #A11.
[2] J. Glaisher, On the residue of a binomial-theorem coeﬃcient with respect to a
prime modulus, Quart. J. of Pure and Applied Math., 30 (1899), 150-156.
[3] A. Granville, Zaphod Beeblebrox’s brain and the ﬁfty-ninth row of Pascal’s tri-
angle, Amer. Math. Monthly, 99 , no. 4 (1992), 318-331; 104 , no. 9 (1997),
848-851.
[4] D. Hewgill, A relationship between Pascal’s triangle and Fermat numbers, Fib.
Quart., 15 (1977), 183-184.
[5] J. G. Huard, B. K. Spearman, K. S. Williams , Pascal’s triangle (mod 8) , Eu-
rop. J. Combin., 19 , no.1 (1998), 45-62.
[6] A. Karttunen, On Pascal’s triangle modulo 2 in Fibonacci representation, Fib.
Quart., 42, no.1 (2004), 38-46.
[7] S. Northshield, Sums across Pascal’s triangle modulo 2, Congressus Numerantium,
200 (2010), 35-52.
[8] E. S. Rowland, The number of nonzero binomial coeﬃcients modulo pα, arXiv:
1001.1783v2 (2010).
[9] V. S. Shevelev, On a combinatorial-analytical identity and some analogs of Euler
formula for zeta-function, Deposed in VINITI, no. 3481-B91 (1991), 1-6 (in Rus-
sian).
[10] V. Shevelev, Binomial coeﬃcient predictors, arXiv: 0907.3302v4 (2009); J. Inte-
ger Seq., 14 (2011), Article 11.2.8.
[11] N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences (http://oeis.org.)
[12] E. Trost, Primzahlen Birkh¨auser-Verlag, 1953.

Department of Mathematics, Ben-Gurion University of the Negev, Beer-
Sheva 84105, Israel. e-mail:shevelev@bgu.ac.il
