<!-- source: https://arxiv.org/pdf/1011.6083v1 | converted from PDF -->

arXiv:1011.6083v1  [math.NT]  17 Nov 2010
ON STEPHAN’S CONJECTURES CONCERNING PASCAL
TRIANGLE MODULO 2

VLADIMIR SHEVELEV

Abstract. We prove a series of Stephan’s conjectures concerning Pas-
cal triangle modulo 2.
 1. Introduction

Consider Pascal triangle for binomial coeﬃcient modulo 2. If to read
every row of this triangle as a binary number, then we obtain the following
sequence {c(n)}n≥0 (cf. A001317 in [2]):

(1.1) 1, 3, 5, 15, 17, 51, 85, 255, 257, 771, 1285, 3855, 4369, 13107, 21845, ...

It is easy to see that

(1.2) c(2n) ≡ 1 (mod 4), n = 0, 1, ...

Denote

(1.3) l(n) = c(2n) − 1
4 .

In 2004, for sequence {l(n)}n≥0, R. Stephan formulated a series of the fol-
lowing conjectures (cf. his comments to A089893 in [2]):

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

etc.
In this paper we prove these conjectures.

1991 Mathematics Subject Classiﬁcation. 11B65.
1

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 2

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
Note that sequence {d(i)} possesses the following properties:
1) d(n) is a binary number with n + 1 (0, 1)-digits;
2) numbers {d(i)} are 1 and all Fermat numbers or products of distinct
Fermat numbers;
3) number of Fermat factors in the product equals to d(n) is the number of
1’s in the binary expansion of n.
4) F (i) divides d(n), n > 1, if and only if it is a factor in product (2.2).
Proofs of these properties is very easy: 1) follows from a simple induc-
tion; 2) and 3) follow from the deﬁnition; 4) follows from the well known
fact (cf., e.g.,[3]) that every two Fermat numbers are relatively prime, in
view of recursion

(2.4) F (n) = 2 +
 n−1∏

i=0 F (i).

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 3

Theorem 1. For n = 0, 1, ..., we have

(2.5) c(n) = d(n).

Proof. We use induction, the base of which is c(0) = d(0) = 1, c(1) =
d(1) = 3, c(2) = d2 = 5. Suppose that c(i) = d(i), for i ≤ k. Let m
be the most number for which F (m) divides c(k) = d(k). In non-trivial
case, when c(k) ̸= F (m), using property 4), for some r < k, we have
c(k) = d(r)F (m) = c(r)F (m). Furthermore, since, by the condition, F (m)
is the most Fermat divisor of c(k) and, in view of (2.4), we have

(2.6) c(r) = c(k)
F (m) ≤
 m−1∏

i=0 F (i) = F (m) − 2.

Besides, since c(r) < c(k), then, by the inductive supposition,

c(r + 1) = d(r + 1).

Adding the case when c(k) = F (m), let us prove a recursion: c(0) =
1, c(1) = 3, c(2) = 5; for k ≥ 2,

(2.7) c(k + 1) =
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
Furthermore, if c(r) = F (m) − 2, then, by (2.6), we have

c(k) = F (m)c(r) = F (m)(F (m) − 2) = F (m + 1) − 2 = 11...1︸ ︷︷ ︸
2m+1 .

Thus the C-sequence with kernel c(k) is

...0 11...1︸ ︷︷ ︸
2m+1 0...

Therefore, by the deﬁnition, the C-sequence with kernel c(k + 1) is

...01 0...0︸︷︷︸
2m+1−1 10...

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 4

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

(2.8) c(k) = c(r) 0...0︸︷︷︸
l c(r),

where l ≥ 1.
Passing on to the following kernel, we have:

c(k + 1) = c(r + 1) 0...0︸︷︷︸
l−1 c(r + 1),

where l − 1 ≥ 0. Thus

c(k + 1) = c(r + 1)22m + c(r + 1) = c(r + 1)F (m).

This completes formula (2.7). From this formula we conclude that c(k + 1)
is a term of sequence {d(i)}. Moreover, since c(k + 1) contains k + 2 binary
digits, then, in view of property 1) of numbers {d(i)}, both of c(k + 1) and
d(k + 1) contain (k + 2) binary digits. Therefore, c(k + 1) = d(k + 1).■

Remark 1. In proof of Theorem 1, we essentially followed to our arguments
from preprint [1], 1991.

Denote s(n) the number of 1’s in the binary expansion of n.

Corollary 1. a) Number of factors in Fermat factorization of c(n) is s(n).
b) Moreover, the following formula holds

(2.9) s(c(n)) = 2s(n).

Proof. a) follows from Theorem 1 and property 3) of numbers {d(n)}.
b) Let, ﬁrstly, c(k) be not a Fermat number and, as in proof of The-
orem 1, m be the most number for which F (m) divides c(k), such that
c(k) = F (m)c(r). Since the diﬀerence between numbers of factors in Fer-
mat factorization of c(k) and c(r) is 1, then, according to a), we have

s(k) = s(r) + 1.

Now we use induction. If the statement is true for i ≤ k − 1, then, in
particular, s(c(r)) = 2s(r). Therefore, by (2.8), we have

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 5

s(c(k)) = 2s(c(r)) = 2 · 2s(r) = 2s(r)+1 = 2s(k).

It is left to consider case c(k) = F (l). Here, by a), s(k) = 1 and (2.9)
satisﬁes trivially. ■

Corollary 2. If F (m) is the most Fermat divisor of numbers c(k − 1) and
c(l − 1) from interval (1, F (m) − 2), then

(2.10) c(k − 1)c(l) = c(l − 1)c(k).

Proof. Using (2.7), we have

c(k) = c(k − 1)F (m), c(l) = c(l − 1)F (m)

and (2.10) follows. ■

Corollary 3. If n = 2l + 2m−1, m ≥ 1, then

(2.11) c(k) = c(2ml)F (m − 1).

Proof. From (2.1)-(2.2), we immediately have d(k) = d(2ml)F (m − 1),
and (2.11) follows from Theorem 1. ■

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
of binary digits.■

4. Proof of Conjectures 2, 3, 4, etc.

Lemma 1. For every n ≥ 0, t ≥ 1 we have identity

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 6

(4.1) (F (t − 1) − 2)c(2tn) = c(2tn + 2t−1 − 1).

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

i.e. (F (t − 1) − 2)c(2tn) has not more than 2t−1 + 2tn binary digits. Thus
number (F (t − 1) − 2)c(2tn) has exactly 2t−1 + 2tn binary digits. Conse-
quently, two terms (F (t − 1) − 2)c(2tn) and c(2tn + 2t−1 − 1) of sequence
{c(i)} has the same number of digits. Therefore, equality (4.1) holds. ■

Lemma 2. For every n ≥ 0, t ≥ 1 we have identities

(4.2) (F (t − 1) − 2)c(2tn + 2t−1) = F (t − 1)c(2tn + 2t−1 − 1),

(4.3) (F (t − 1) − 2)c(2tn + 2t−1) = 3F (t − 1)c(2tn + 2t−1 − 2).

Proof. Multiplying (4.1) by F (t − 1) and using formula (2.11) of Corol-
lary 3 (for l = n and m = t), we obtain (4.2). Furthermore, if to take in
Corollary 3 m = 1, l = 2t−1n + 2t−2 − 1, then, in view of F (0) = 3, we have
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

ON STEPHAN’S CONJECTURES CONCERNING PASCAL TRIANGLE 7

(4.5) lim
n→∞ l(2t−1n + 2t−2)
l(2t−1n + 2t−2 − 1) = 3F (t − 1)
F (t − 1) − 2 .■

So, if t = 2, 3, 4, 5, ..., then the right hand side is
3 · 5
5 − 2 = 5, 3 · 17
17 − 2 = 17
5 , 3 · 257
257 − 2 = 257
85 , 3 · 65537
65537 − 2 = 65537
21845, ...

correspondingly.
 References

[1] . V. S. Shevelev, On a combinatorial-analytical identity and some analogs of Euler
formula for zeta-function, Deposed in VINITI, no.3481-B91 (1991), 1-6 (in Russian).
[2] . N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences (http:
//www.research.att.com)
[3] . E. Trost, Primzahlen, Birkh¨auser-Verlag, 1953.

Departments of Mathematics, Ben-Gurion University of the Negev, Beer-
Sheva 84105, Israel. e-mail:shevelev@bgu.ac.il
