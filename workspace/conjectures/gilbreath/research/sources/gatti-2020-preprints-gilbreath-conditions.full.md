<!-- source: https://web.archive.org/web/20201202160317/https://www.preprints.org/manuscript/202003.0145/v1/download | converted from PDF -->

Gilbreath’s sequences and proof of conditions
for Gilbreath’s conjecture

Riccardo Gatti1

1School of Mathematics and Statistics at Faculty of Science,
Technology, Engineering and Mathematics at Open University,
Milton Keynes, United Kingdom

Abstract

The conjecture attributed to Norman L. Gilbreath, but formulated
by Francois Proth in the second half of the 1800s, concerns an interest-
ing property of the ordered sequence of prime numbers P . Gilbreath’s
conjecture stated that, computing the absolute value of diﬀerences of
consecutive primes on ordered sequence of prime numbers, and if this
calculation is done for the terms in the new sequence and so on, every
sequence will starts with 1. In this paper is deﬁned the concept of
Gilbreath’s sequence, Gilbreath’s triangle and Gilbreath’s equation.
On the basis of the results obtained from the proof of properties, an
inductive proof is produced thanks to which it is possible to estab-
lish the necessary condition to state that the Gilbreath’s conjecture is
true.

1 Introduction to Gilbreath’s conjecture

Let the ordered sequence P = {2, 3, 5, 7, 11, 13, 17, ...} = {p1, ..., pn, ...} formed
by prime numbers, and set pb
a = |pb−1
a+1 − pb−1
a | where b ⩾ 1. Gilbreath con-
jectured that every term pb
1 = 1. In this notation, the elements of P should
be indicated with {p0
1, ..., p0
n, ...}. For brevity, the superscript with b = 0 is
omitted. It is likely that this conjecture is satisﬁed by many other sequences
of integers, so it is necessary to deﬁne the general properties of all sequences
that satisfy this conjecture.
 1

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020

©  2020 by the author(s). Distributed under a Creative Commons CC BY license.

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

©  2020 by the author(s). Distributed under a Creative Commons CC BY license.

2 Gilbreath’s sequence

Deﬁnition 1. Let a sequence S = {s1, s2, s3, . . . , sn} a sequence formed by
integer number and sb
a = |sb−1
a+1 − sb−1
a |. S is deﬁned a Gilbreath’s sequence if
sb
1 = 1∀b ⩾ 1. If S is a Gilbreath’s sequence hence S ∈ Gn where Gn is the
set of all the Gilbreath’s sequences of length n.

Let, for example, S = {2, 3, 5, 7, 11, 13, 17} a sequence of length n = 7,
the Gilbreath’s triangle of S is deﬁned by sb
a = |sb−1
a+1 − sb−1
a |. Hence:
s1 s2 s3 s4 ... sn−3 sn−2 sn−1 sn
s1
1 s1
2 s1
3 s1
4 ... s1
n−3 s1
n−2 s1
n−1
...
sn−2
1 sn−2
2
sn−1
1
or 1 2 2 4 2 4
1 0 2 2 2
1 2 0 0
1 2 0
1 2
1
The ﬁrst term of every sequence is equal to 1, hence S ∈ G7.

Theorem 1. Let a sequence S = {s1, ..., sn} ∈ Gn and a sequence S′ =
{s1, ..., sn−1}, then S′ ∈ Gn−1.

Proof. The Gilbreath’s triangle associated with S:
s1 s2 s3 s4 ... sn−3 sn−2 sn−1 sn
s1
1 s1
2 s1
3 s1
4 ... s1
n−3 s1
n−2 s1
n−1
...
sn−2
1 sn−2
2
sn−1
1
where s1
1 = ... = sn−2
1 = sn−1
1 = 1 as a consequence of S ∈ Gn. Removing the
last element of each sequence gives:
s1 s2 s3 s4 ... sn−3 sn−2 sn−1
s1
1 s1
2 s1
3 s1
4 ... s1
n−3 s1
n−2
...
sn−2
1
which is the Gilbreath’s triangle of S′, s1
1 = ... = sn−2
1 = 1 as a consequence
of S ∈ Gn, hence S′ ∈ Gn−1.
 2

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

Theorem 2. Let a sequence S = {s1, ..., sn} ∈ Gn and a sequence S′ =
{s1, ..., sn, k}, than S′ ∈ Gn+1 ⇔ k ∈ KS.

Proof. The Gilbreath’s triangle associated with S:
s1 s2 s3 s4 ... sn−3 sn−2 sn−1 sn
s1
1 s1
2 s1
3 s1
4 ... s1
n−3 s1
n−2 s1
n−1
...
sn−2
1 sn−2
2
sn−1
1
where s1
1 = ... = sn−2
1 = sn−1
1 = 1 as a consequence of S ∈ Gn. The
Gilbreath’s triangle of S′:
s1 s2 s3 s4 ... sn−3 sn−2 sn−1 sn k
s1
1 s1
2 s1
3 s1
4 ... s1
n−3 s1
n−2 s1
n−1 |sn − k|
...
sn−2
1 sn−2
2 |sn−3
3 − |sn−4
4 − |... − |s1
n−1 − |sn − k||...|||
sn−1
1 |sn−2
2 − |sn−3
3 − |sn−4
4 − |... − |s1
n−1 − |sn − k||...||||
|sn−1
1 − |sn−2
2 − |sn−3
3 − |sn−4
4 − |... − |s1
n−1 − |sn − k||...|||||
where s1
1 = ... = sn−2
1 = sn−1
1 = 1 as a consequence of S ∈ Gn and if also
sn
1 = |sn−1
1 − |sn−2
2 − |sn−3
3 − |sn−4
4 − |... − |s1
n−1 − |sn − k||...||||| = 1, then
S′ ∈ Gn+1.

|sn−1
1 − |sn−2
2 − |sn−3
3 − |sn−4
4 − |... − |s1
n−1 − |sn − k||...||||| = 1 (1)

is deﬁned as the Gilbreath’s equation of S and KS = {k1, ..., k2n} is deﬁned
as the set of all solutions for k.

Corollary 1. Let a sequence S = {s1, ..., sn} ∈ Gn and a sequence S′ =
{s1, ..., sn, k}, then there are 2
n values of k that satisfy S′ ∈ Gn+1.

Proof. The Gilbreath’s equation is a 2n degree equation, then there are 2
n

value of k that satisfy the equation (1). The solutions are:

k1,. . . ,2n = ±sn−1
1 ± sn−2
2 ± sn−3
3 ± sn−4
4 ± ... ± s1
n−1 + sn ± 1 (2)

With respect to KS, the largest value that solves the equation is max KS =
sn−1
1 +sn−2
2 +sn−3
3 +sn−4
4 +...+s1
n−1 +sn +1 and the smallest value that solves
the equation is min KS = −sn−1
1 − sn−2
2 − sn−3
3 − sn−4
4 − ... − s1
n−1 + sn − 1 =
2sn − max KS. A remarkable relation is:

max KS + min KS = 2sn (3)

3

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

Corollary 2. Let a sequence S = {s1, ..., sn} ∈ Gn and a sequence S′ =
{s1, ..., sn, sn}, than S′ ∈ Gn+1.

Proof. The Gilbreath’s equations of S′ with k = sn is:
|sn−1
1 − |sn−2
2 − |sn−3
3 − |sn−4
4 − |... − |s1
n−1|...||||| = 1 which is true because
S ∈ Gn, hence S′ ∈ Gn+1.

It is useful, for the following proofs to introduce the deﬁnition of two
important Gilbreath’s sequences. Let a sequence S = {s1, ..., sn}, from re-
lation (2), any value of k cannot be greater than max KS, so the sequence
{s1, ..., sn, max KS} is the upper bound sequence for the sequence {s1, ..., sn}.
The new sequence S′ = {s1, ..., sn, max KS, k} will have the upper limit
for k = max K{s1,...,sn,max KS }. Equally, let a sequence S = {s1, ..., sn},
from relation (2), any value of k cannot be smaller than min KS and the
new sequence S′ = {s1, ..., sn, min KS, k} will have the lower limit for k =
min K{s1,...,sn,min KS }. From this example, it is now possible to introduce the
deﬁnition of upper bound sequence and lower bound sequence.

Deﬁnition 2. Let the sequence S = {s1, ..., sn} ∈ Gn

US := {s1, ..., sn, max K{s1,...,sn}, max K{s1,...,sn,max K{s1,...,sn}}, ...} = {uS1, ..., uSm, ...}
(4)
is the upper bounds sequence for any S.

Deﬁnition 3. Let the sequence S = {s1, ..., sn} ∈ Gn

LS := {s1, ..., sn, min K{s1,...,sn}, min K{s1,...,sn,min K{s1,...,sn}}, ...} = {lS1, ..., lSm, ...}
(5)
is the lower bounds sequence for any S.

From deﬁnition 2, deﬁnition 3, corollary 2 and (3)

S = {s1, ..., sn} ∈ Gn =⇒ l{s1,...,sm} ⩽ sm+1 ⩽ u{s1,...,sm}, where m ⩽ n − 1
(6)

Lemma 1. Let a sequence S = {s1, ..., sn} ∈ Gn where s1 ∈ 2Z, then
{s2, ..., sn} ⊂ (2Z + 1)n−1

Proof. Let S1 = {s1}, where s1 ∈ 2Z. From theorem 2, corollary 1: S2 =
{s1, k} ∈ G2 if k = s1 ± 1 ∈ 2Z + 1. Now let the sequence S3 = {s1, s1 ± 1, k},
from theorem 2, corollary 1, S3 ∈ G3 if k = |±1|+(s1 ± 1)±1 = 1+s1 ±1±1.

4

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

From the previous step, s1±1 ∈ 2Z+1, hence 1+s1±1 ∈ 2Z and 1+s1±1±1 ∈
2Z+1. Iteratively, this can be proved for every element of S. Hence if S ∈ Gn
and the ﬁrst element of S is an even number, then all the other numbers of
the sequence must be odd.

Lemma 2. Let a sequence S = {s1, ..., sn} ∈ Gn where s1 ∈ 2Z + 1, then
{s2, ..., sn} ⊂ (2Z)
n−1

Proof. Let S1 = {s1}, where s1 ∈ 2Z + 1. From theorem 2, corollary 1: S2 =
{s1, k} ∈ G2 if k = s1±1 ∈ 2Z. Now let the sequence S3 = {s1, s1±1, k}, from
theorem 2, corollary 1, S3 ∈ G3 if k = |±1|+(s1 ± 1)±1 = 1+s1±1±1. From
the previous step, s1±1 ∈ 2Z, hence 1+s1±1 ∈ 2Z+1 and 1+s1±1±1 ∈ 2Z.
Iteratively, this can be proved for every element of S. Hence if S ∈ Gn and
the ﬁrst element of S is an odd number, then all the other numbers of the
sequence must be even.

Deﬁnition 4. Let A1 = 2Z and A2 = 2Z + 1, both sets are represented as
A1,2 = 2Z + ( 1
2 ± 1
2)
.

Lemma 3. Let S = {s1, ..., sn} ∈ Gn where s1 ∈ 2Z + ( 1
2 ± 1
2), then
{s2, ..., sn} ⊂ [
2Z + ( 1
2 ∓ 1
2)]n−1

Proof. Is a direct conseguence of lemma 1 and lemma 2.

Lemma 4. Let a sequence S = {s1, ..., sn, k} ∈ Gn+1 where s1 ∈ 2Z +( 1
2 ± 1
2)
, then KS = {x ∈] min KS; max KS[∧x ∈ 2Z + ( 1
2 ∓ 1
2) }

Proof. From theorem 2, corollary 1, there are 2
n values of k that satisfy
S ∈ Gn+1 and from deﬁnition 2 and deﬁnition 3, min KS ⩽ k ⩽ max KS. KS
is deﬁned as the set of all solutions of k, hence it contais elements between
min KS and max KS. From lemma 3 it has already been shown that if s1 ∈ 2Z,
than sa ∈ 2Z+1, ∀a > 1 and if s1 ∈ 2Z+1, than sa ∈ 2Z, ∀a > 1, the theorem
is proved from theorem 2, deﬁnition 2, deﬁnition 3 and lemma 3.

From lemma 4 is proved an important result regarding (2). (2) generates
2
n solutions for a sequence S = {s1, ..., sn, k}, but from lemma 43 it has been
proved that these solutions are only even or only odd according to the nature
of the sequence. Therefore, the number of distinct solutions generated by (2)
is 2
n−1 since half solutions between min KS and max KS are equally divided
between even and odd: dim KS = 2
n−1.

5

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

Theorem 3. Let a sequence S = {s1, ..., sn} ∈ Gn and S′ = {s1, ..., sn, k},
where s1 ∈ 2Z + ( 1
2 ± 1
2)
, then k ∈] min KS; max KS[∧k ∈ 2Z + ( 1
2 ∓ 1
2) ⇔
S′ ∈ Gn+1

Proof. From deﬁnition 2 and deﬁnition 3, k ∈] min KS; max KS[ and from
lemma 4, k ∈ 2Z + ( 1
2 ∓ 1
2). Hence it is true k ∈] min KS; max KS[∧k ∈
2Z + ( 1
2 ∓ 1
2) ⇒ S′ = {s1, ..., sn, k} ∈ Gn+1.
Suppose that S′ ∈ Gn+1 but k ∈] min KS; max KS[∧k ∈ 2Z + ( 1
2 ∓ 1
2) is
false, so it is true k /∈] min KS; max KS[∨k /∈ 2Z + ( 1
2 ∓ 1
2). From deﬁ-
nition 2, deﬁnition 3 and lemma 4 it is not possible to have S′ ∈ Gn+1
if k ⩾ max KS ∨ k ⩽ min KS ∨ k /∈ 2Z + ( 1
2 ∓ 1
2). Hence it is also true
k ∈] min KS; max KS[∧k ∈ 2Z + ( 1
2 ∓ 1
2) ⇐ S′ = {s1, ..., sn, k} ∈ Gn+1.

2.1 Notable upper and lower bound sequence

Deﬁnition 5. Let the sequence S = {s1, ..., sn} ∈ Gn,

U ′
S := {max K{s1,...,sn}, max K{s1,...,sn,max K{s1,...,sn}}, ...} = {u′
S1, ..., u′
Sm, ...}
(7)

Deﬁnition 6. Let the sequence S = {s1, ..., sn} ∈ Gn,

L′
S := {min K{s1,...,sn}, min K{s1,...,sn,min K{s1,...,sn}}, ...} = {l′
S1, ..., l′
Sm, ...} (8)

From deﬁnition 5 and deﬁnition 6 US = {S, U ′
S} and LS = {S, L′
S}. Let
S = {s1}, U ′
S = {s1 + 1, s1 + 3, ..., s1 + 2n−1 − 1} and L′
S = {s1 − 1, s1 −
3, ..., s1 − 2
n−1 + 1}.
No remarkable expression was found to be to analytically deﬁne the trend
of U ′
S and L
′
S for a generic sequence S but it was observed that the exponential
trend is preserved. However, this trend varies with the number of terms of
U ′
S and L′
S so it does not seem possible to establish what will be the n + 1-th
term of U ′
S and L
′
S given the previus n terms through an analytical formula.
However, it is always possible use the recursive espression (2).
Let the sequence S = {s1, ..., sn} ∈ Gn, using deﬁnition 2, deﬁnition 3,
deﬁnition 5, deﬁnition 6, the (3) can be rewritten as:

uSn+m + lSn+m = u
′
Sm + l′
Sm = 2sn (9)

equivalent to (6).
 6

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

If it is true that exponential trend is preserved, elements of U ′
S can be
written in the form u
′
Sn = αeβn or log u′
Sn = log α + βn.
The best ﬁt for a dataset D = {d1, ..., dn} in a linear regression model is

β = n ∑n
i=1 i log di − ∑n
i=1 i ∑n
i=1 log di
n ∑n
i=1 i2 − (∑n
i=1 i)
2 = 12
n(n2 − 1)
 ( n∑

i=1 i log di − n + 1
2
 n∑

i=1 log di
)

(10)

log α = 1
n
 n∑

i=1 log di − β(n + 1)
2 (11)

hence
 α = e− β(n+1)
2
 ( n∏

i=1 di
) 1
n (12)

and the coeﬃcient of determination is

R2 = 1 − ∑n
i=1 (di − αeβi)2

∑n
i=1 (
di − d)2 (13)

Note that in D if |da| < |da+1| and da < 0, it is not possible to calculate log db,
where b > a. To avoid this problem the transformation di → di+ d1
2 ( d1
|d1| − 1
)

is performed. In this way, if d1 > 0, di → di and if d1 < 0, di → di − d1.
After that, the ﬁtting curve will be dn = αeβn − d1
2 ( d1
|d1| − 1
)
.

Example 1. Let the sequence S = {2, 3, 5, 7, 11, 13} of length 6, the ﬁrst 18
terms of the upper bound sequence are U ′
S = {21, 47, 119, 297, 705, 1595, 3475,
7365, 15309, 31399, 63823, 128961, 259577, 521203, 1044907, 2092829, 4189253,
8382751} and the ﬁrst 18 terms of the lower bound sequence are L
′
S =
{5, −21, −93, −271, −679, −1569, −3449, −7339, −15283, −31373, −63797,
− 128935, −259551, −521177, −1044881, −2092803, −4189227, −8382725}.
According to (6) and to (9), 21 + 5 = 47 − 21 = 119 − 93 = 297 − 271 =
... = 8382751 − 8382725 = 26 = 2s6. Let begin ﬁtting U ′
S to αU ′
S e
βU ′
S n. From
(10), βU ′
S = 6
2907 (∑18
i=1 i log u
′
Si − 19
2 ∑18
i=1 log u
′
Si) ≈ 0.75,

from (12) αU ′
S = e
− β(19)
2 (∏18
i=1 u
′
Si) 1
18 ≈ 14.42. The model ﬁts the trend of u
′
Sn
with R2 ≈ 0.92 from (13). As regards L′
S, from (6), l′
Sn = 2s6 − αU ′
S eβU ′
S n ≈
26 − 14.42e
0.75n ≈ −7.97e
0.80n with R2 ≈ 0.99.

7

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

As explained above, the addition of a term to U ′
S leads to new values of
α and β, therefore this analysis can be carried out without pretending to
evaluate the n + 1-th element of a given U ′
S of length n.

The numerical analysis of the values of the upper limit sequence was
added only to show that no analytical formula has been found for the gener-
ations of the values of this sequence, with exception of (2).

3 Proof of conditions for P = {p1, ..., pn}

Let S = {s1, ..., sn} = {f (n)}, from theorem 1 and 2, is true the following.
The relationship s2 = s1 ± 1 must be true, otherwise it would not be true
that s1
1 = 1, hence f (2) = f (1) ± 1. As a consequence of theorem 3, for all
elements subsequent to s1, the absolute diﬀerence of two successive elements
must be an integer multiple of 2 so as to maintain the absolute diﬀerence
of two successive elements as an even value. So, if the ﬁrst element in the
sequence is even, the subsequent elements must be odd and if the ﬁrst element
is odd, the subsequent elements must be even.
As a consequence of theorem 2, solution of the Gilbreath’s equation (2)
and deﬁnition 2 and deﬁnition 3: each n-th element of a sequence S must
be within the range between the upper and the lower sequences calculated
on all the elements prior to the n-th ones. Hence, from theorem 2 and
according to the solution of the Gilbreath’s equation at (2), cannot exists a
Gilbreath’s sequence in which the n-th is larger than max K{s1,...,sn−1}, since
max K{s1,...,sn−1} is the maximum value that the n-th value can take according
to (2). The same goes for min K{s1,...,sn−1}, since it is the smallest value that
the n-th value can take, according to (2). Hence:

l{s1,...,sn−1}n ⩽ f (n) ⩽ u{s1,...,sn−1}n (14)

Following the results obtained in the previous paragraphs about Gilbreath’s
sequence and Gilbreath’s equation, let proceed discussing the Gilbreath’s
conjecture. The results obtained so far will be used to establish if theorem
(4) is true for an ordered sequence of prime numbers P .

Theorem 4. For every n-th prime number, n > 1 it is true that l{p1,...,pn−1}n ⩽
pn ⩽ u{p1,...,pn−1}n.
 8

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

Proof. By deﬁnition of L and U , l{p1,...,pn−1}n = min K{p1,...,pn−1} and u{p1,...,pn−1}n =
max K{p1,...,pn−1}, hence the statement becomes:

min K{p1,...,pn−1} ⩽ pn ⩽ max K{p1,...,pn−1} (15)

Let S = {p1, p2} = {2, 3} ∈ G2 a Gilbreath’s sequence formed by the ﬁrst
two prime numbers. As S ∈ G2, from (3), it is true that min K{p1,p2} ⩽ p2 ⩽
max K{p1,p2}, it is also true, for theorem 2 corollary 3, that {p1, p2, p2} ∈ G3
and for every prime number is true that pn > pn−1. Since min K{p1,p2} ⩽ p2,
it is certainly true that min K{p1,p2} ⩽ p3. The left inequality of (15) is proved
for n = 3.
If p3 ⩽ max K{p1,p2}, then, subtracting the quantity 2p2 from both sides,
p3 − 2p2 ⩽ max K{p1,p2} − 2p2. From Bertrand’s postulate, pn < 2pn−1, hence
p3 − 2p2 < 0. Replacing (3) in the previous inequation: min K{p1,p2} ⩽ α,
where α > 0. Hence, exist a value α > 0 such that min K{p1,p2} ⩽ α. The
value of min K{p1,p2} can be replaced using (2): min K{p1,p2} = −p1
1 + p2 − 1
where −p1
1 −1 < 0 and p2 > 0. If α = p2, the relation min K{p1,p2} ⩽ α, where
α > 0 is true, hence it is true that p3 ⩽ max K{p1,p2}. The right inequality of
(15) is proved for n = 3.
At this point the proof can process showing that (15) is true for n = 4.
Since, p4 > p3 and min K{p1,p2,p3} ⩽ p3 ⩽ max K{p1,p2,p3}, it is true that
min K{p1,p2,p3} ⩽ p4. Again, the statement p4 ⩽ max K{p1,p2,p3} is equivalent
to the statement min K{p1,p2,p3} ⩽ α, where α > 0. From the equation (2),
min K{p1,p2,p3} = −p2
1 − p1
2 + p3 − 1 where −p2
1 − p1
2 − 1 < 0 and p3 > 0. If
α = p3, the relation min K{p1,p2,p3} ⩽ α, where α > 0. Iteratively, this can be
proved to verify (15) for every prime.

Lemma 3 is already proved since p1 = 2 is even and all other elements are
odd: by deﬁnition of prime number, there are no even prime numbers except
for 2. From theorem 4 and lemma 3 is proved theorem 3 for P .

References

[1] A. M. Odlyzko. Iterated absolute values of diﬀerences of consecutive
primes. Mathematics of computation, 61 (1993), 373-380

[2] J. Bertrand. M´emoire sur le nombre de valeurs que peut prendre une fonc-
tion quand on y permute les lettres qu’elle renferme. Journal de l’Ecole
Royale Polytechnique, 18 (1845), 123-140.

9

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1

[3] F. Proth. Th´eor`emes sur les numbers premiers. C. R. Acad. Sci. Paris,
86 (1887), 329-331.

[4] P. Dusart. The kth prime is greater than k(ln k + ln ln k − 1) for k ⩾ 2.
Mathematics of computation, 68 (1999), 411-415.

[5] J. B. Rosser. Explicit bounds for some functions of prime numbers. Amer.
J. Math, 63 (1941), 211-232.

[6] J. P. Massias, G. Robin. Bornes eﬀectives pour certaines fonctions concer-
nant les nombres premiers. Journal de Th´eorie des Nombres de Bordeaux,
8 (1996), 215-242.

[7] J. B. Rosser. The n-th Prime is Greater than n log n. Proceedings of the
London Mathematical Society, 45 (1939), 21-44.

[8] F. Proth. Sur la s´erie des nombres premiers. Nouv. Corresp. Math, 4
(1878), 236-240.
 10

Preprints (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   Preprints  (www.preprints.org)  |  NOT PEER-REVIEWED  |  Posted: 8 March 2020                   doi:10.20944/preprints202003.0145.v1
