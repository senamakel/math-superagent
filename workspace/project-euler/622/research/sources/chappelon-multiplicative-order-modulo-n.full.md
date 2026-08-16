<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL13/Chappelon/chappelon3.pdf | converted from PDF -->

23 11 Article 10.2.1
Journal of Integer Sequences, Vol. 13 (2010),2
 3

6

1

47

On the Multiplicative Order of an Modulo n

Jonathan Chappelon
1

Universit´e Lille Nord de France
F-59000 Lille
France
jonathan.chappelon@lmpa.univ-littoral.fr

Abstract
Let n be a positive integer and αn be the arithmetic function which assigns the
multiplicative order of an modulo n to every integer a coprime to n and vanishes
elsewhere. Similarly, let βn assign the projective multiplicative order of an modulo
n to every integer a coprime to n and vanishes elsewhere. In this paper, we present
a study of these two arithmetic functions. In particular, we prove that for positive
integers n1 and n2 with the same square-free part, there exists a relationship between
the functions αn1 and αn2 and between the functions βn1 and βn2. This allows us
to reduce the determination of αn and βn to the case where n is square-free. These
arithmetic functions recently appeared in the context of an old problem of Molluzzo,
and more precisely in the study of which arithmetic progressions yield a balanced
Steinhaus triangle in Z/nZ for n odd.

1 Introduction

We start by introducing some notation relating to the order of certain elements modulo n. For
every positive integer n and every prime number p, we denote by vp(n) the p-adic valuation
of n, i.e., the greatest exponent e ⩾ 0 for which pe divides n. The prime factorization of n
may then be written as n = ∏

p∈P pvp(n),

where P denotes the set of all prime numbers. We denote by rad(n) the radical of n, i.e., the
largest square-free divisor of n, namely

rad(n) = ∏

p∈P
p|n
 p.

1ULCO, LMPA J. Liouville, B.P. 699, F-62228 Calais, France and CNRS, FR 2956, France.

1

For every positive integer n and every integer a coprime to n, we denote by On(a) the
multiplicative order of a modulo n, i.e., the smallest positive integer e such that ae ≡ 1
(mod n), namely On(a) = min {e ∈ N∗ | ae ≡ 1 (mod n)}

and we denote by Rn(a) the multiplicative remainder of a modulo n, i.e., the multiple of n
deﬁned by Rn(a) = aOn(a) − 1.

The multiplicative order of a modulo n also corresponds with the order of the element πn(a),
where πn : Z −։ Z/nZ is the canonical surjective morphism, in the multiplicative group
(Z/nZ)
∗, the group of units of Z/nZ. Note that On(a) divides ϕ(n), ϕ being the Euler’s
totient function.
For every positive integer n, we deﬁne and denote by αn the arithmetic function

αn : Z −→ N

a ↦−→ { On (an) , for all gcd(a, n) = 1;
0, otherwise,

where gcd(a, n) denotes the greatest common divisor of a and n, with the convention
that gcd(0, n) = n. Observe that, for every a coprime to n, the integer αn(a) divides
ϕ(n)/ gcd(ϕ(n), n). This follows from the previous remark on On(a) and the equality
αn(a) = On(an) = On(a)/ gcd(On(a), n).
For every positive integer n and every integer a coprime to n, we denote by POn(a) the
projective multiplicative order of a modulo n, i.e., the smallest positive integer e such that
ae ≡ ±1 (mod n), namely

POn(a) = min {e ∈ N∗ | ae ≡ ±1 (mod n)} .

The projective multiplicative order of a modulo n also corresponds with the order of the
element πn(a) in the multiplicative quotient group (Z/nZ)
∗/{−1, 1}.
For every positive integer n, we deﬁne and denote by βn the arithmetic function

βn : Z −→ N

a ↦−→ { POn (an) , for all gcd(a, n) = 1;
0, otherwise.

Observe that we have the alternative αn = βn or αn = 2βn.
In this paper, we study in detail these two arithmetic functions. In particular, we prove
that, for every positive integers n1 and n2 such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2,

the integer αn1(a) (respectively βn1(a)) divides αn2(a) (resp. βn2(a)), for every integer a.
More precisely, we determine the exact relationship between the functions αn1 and αn2 and
between βn1 and βn2. We prove that we have

αn1(a) = αn2(a)

gcd (
αn2(a), gcd(n1,Rn2 (a))
n2
 ) for all gcd(a, n1) = 1

2

in Theorem 6 of Section 2 and that we have

βn1(a) = βn2(a)

gcd (
βn2(a), gcd(n1,Rn2 (a))
n2
 ) for all gcd(a, n1) = 1

in Theorem 13 of Section 3. Thus, for every integer a coprime to n, the determination of
αn(a) is reduced to the computation of αrad(n)(a) and Rrad(n)(a) if v2(n) ⩽ 1 and of α2 rad(n)(a)
and R2 rad(n)(a) if v2(n) ⩾ 2. These theorems on the functions αn and βn are derived from
Theorem 7 of Section 2, which states that

On1(a) = On2(a) · n1
gcd(n1, Rn2(a)),

for all integers a coprime to n1 and n2. This result generalizes the following theorem of
Nathanson which, in the above notation, states that for every odd prime number p and for
every positive integer k, we have the equality

Opk(a) = Op(a) · pk

gcd(pk, Rp(a))

for all integers a not divisible by p.

Theorem 3.6 of [3]. Let p be an odd prime, and let a ̸= ±1 be an integer not divisible by p.
Let d be the order of a modulo p. Let k0 be the largest integer such that ad ≡ 1 (mod pk0).
Then the order of a modulo pk is d for k = 1, . . . , k0 and dpk−k0 for k ⩾ k0.

For every ﬁnite sequence S = (a1, . . . , am) of length m ⩾ 1 in Z/nZ, we denote by ∆S
the Steinhaus triangle of S, that is the ﬁnite multiset of cardinality (m+1
2 ) in Z/nZ deﬁned
by
 ∆S =
 { i∑

k=0
 ( i
k
)aj+k
 ∣
∣
∣
∣
∣ 0 ⩽ i ⩽ m − 1 , 1 ⩽ j ⩽ m − i
}
 .

A ﬁnite sequence S in Z/nZ is said to be balanced if each element of Z/nZ occurs in its
Steinhaus triangle ∆S with the same multiplicity. For instance, the sequence (2, 2, 3, 3) of
length 4 is balanced in Z/5Z. Indeed, as depicted in Figure 1, its Steinhaus triangle is
composed by each element of Z/5Z occuring twice.

0
4 1
4 0 1
2 2 3 3

Figure 1: The Steinhaus triangle of a balanced sequence in Z/5Z

Note that, for a sequence S of length m ⩾ 1 in Z/nZ, a necessary condition on m for S
to be balanced is that the integer n divides the binomial coeﬃcient (m+1
2 ). In 1976, John
C. Molluzzo [2] posed the problem to determine whether this necessary condition on m is
also suﬃcient to guarantee the existence of a balanced sequence. In [1], it was proved that,

3

for each odd number n, there exists a balanced sequence of length m for every m ≡ 0 or −1
(mod αn(2) · n) and for every m ≡ 0 or −1 (mod βn(2) · n). This was achieved by analyzing
the Steinhaus triangles generated by arithmetic progressions. In particular, since β3k(2) = 1
for all k ⩾ 1, the above result implies a complete and positive solution of Molluzzo’s problem
in Z/nZ for all n = 3
k.

2 The arithmetic function αn

The table depicted in Figure 2 gives us the ﬁrst values of αn(a) for every positive integer n,
1 ⩽ n ⩽ 20, and for every integer a, −20 ⩽ a ⩽ 20.

n\a 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
3 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2
4 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
5 1 4 4 2 0 1 4 4 2 0 1 4 4 2 0 1 4 4 2 0
6 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0
7 1 3 6 3 6 2 0 1 3 6 3 6 2 0 1 3 6 3 6 2
8 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
9 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2
10 1 0 2 0 0 0 2 0 1 0 1 0 2 0 0 0 2 0 1 0
11 1 10 5 5 5 10 10 10 5 2 0 1 10 5 5 5 10 10 10 5
12 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0
13 1 12 3 6 4 12 12 4 3 6 12 2 0 1 12 3 6 4 12 12
14 1 0 3 0 3 0 0 0 3 0 3 0 1 0 1 0 3 0 3 0
15 1 4 0 2 0 0 4 4 0 0 2 0 4 2 0 1 4 0 2 0
16 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
17 1 8 16 4 16 16 16 8 8 16 16 16 4 16 8 2 0 1 8 16
18 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0
19 1 18 18 9 9 9 3 6 9 18 3 6 18 18 18 9 9 2 0 1
20 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0

Figure 2: The ﬁrst values of αn(a)

The positive integer αn(a) seems to be diﬃcult to determine. Indeed, there is no general
formula known to compute the multiplicative order of an integer modulo n but, however, we
get the following helpful propositions.

Lemma 1. Let n1 and n2 be two positive integers such that rad(n1) = rad(n2). Then, an
integer a is coprime to n1 if, and only if, it is also coprime to n2.

Proof. This follows from the deﬁnition of the greatest common divisor of two integers and
from the deﬁnition of the radical of an integer.

4

Proposition 2. Let n1 and n2 be two positive integers such that rad(n1)|n2 and n2|n1. Then,
for every integer a, the integer αn1(a) divides αn2(a).

Proof. If a is not coprime to n1 and n2, then, by deﬁnition of the functions αn1 and αn2 and
by Lemma 1, we have αn1(a) = αn2(a) = 0.

Suppose that a is coprime to n1 and n2. If vp(n1) = 1 for all prime factors p of n1, then
n2 = n1. Otherwise, let p be a prime factor of n1 such that vp(n1) ⩾ 2. We shall show that
αn1(a) divides αn1/p(a). By deﬁnition of αn1/p(a), there exists an integer u such that

aαn1/p(a)· n1
p = 1 + u · n1
p .

Therefore, by the binomial theorem, we have

aαn1/p(a)·n1 = (
aαn1/p(a)· n1
p )p = (
1 + u · n1
p
 )p = 1 + u · n1 +
 p∑

k=2
 (p
k
) · uk · ( n1
p
 )k.

Since vp(n1) ⩾ 2, it follows that (n1/p)
k is divisible by n1 for every integer k ⩾ 2 and so

aαn1/p(a)·n1 ≡ 1 (mod n1).

Hence αn1(a) divides αn1/p(a). This completes the proof.

An exact relationship between αn1(a) and αn2(a), for every integer a coprime to n1 and
n2, is determined at the end of this section. We ﬁrst settle the easy prime power case.

Proposition 3. Let p be a prime number and let a be an integer. Then we have

αpk(a) = Op(a)

for every positive integer k.

Proof. Let k be a positive integer. If a is not coprime to p, then we have αpk(a) = αp(a) = 0.
Suppose now that a is coprime to p. By Proposition 2, the integer αpk(a) divides αp(a). It
remains to prove that αp(a) divides αpk(a). The congruence

aαpk (a)·pk ≡ 1 (mod pk)

implies that aαpk (a)·pk ≡ 1 (mod p),

and hence, by Fermat’s Little Theorem, it follows that

aαpk (a)·p ≡ aαpk (a)·pk ≡ 1 (mod p).

Therefore αp(a) divides αpk(a). Finally, we have

αpk(a) = αp(a) = Op(ap) = Op(a).

This completes the proof.
 5

Remark 4. If p = 2, then, for every positive integer k, we obtain

α2k(a) = O2(a) = { 0, for a even;
1, for a odd.

Proposition 5. Let n1 and n2 be two coprime numbers and let a be an integer. Then
αn1n2(a) divides lcm(αn1(a), αn2(a)), the least common multiple of αn1(a) and αn2(a).

Proof. If gcd(a, n1n2) ̸= 1, then gcd(a, n1) ̸= 1 or gcd(a, n2) ̸= 1 and so

αn1n2(a) = lcm(αn1(a), αn2(a)) = 0.

Suppose now that gcd(a, n1n2) = 1 and hence that the integers a, n1 and n2 are coprime
pairwise. Let i ∈ {1, 2}. The congruences

aαni (a)·ni ≡ 1 (mod ni)

imply that an1n2 lcm(αn1 (a),αn2 (a)) ≡ 1 (mod ni).

Therefore αn1n2(a) divides lcm(αn1(a), αn2(a)) by the Chinese remainder theorem.

Let n1 and n2 be two positive integers such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2.

By deﬁnition, we know that αn1(a) = αn2(a) = 0 for every integer a not coprime to n1 and
n2. We end this section by determining the exact relationship between αn1(a) and αn2(a)
for every integer a coprime to n1 and n2.

Theorem 6. Let n1 and n2 be two positive integers such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2.

Then, for every integer a coprime to n1 and n2, we have

αn1(a) = αn2(a)

gcd (
αn2(a), gcd(n1,Rn2 (a))
n2
 )

This result is a corollary of the following theorem.

Theorem 7. Let n1 and n2 be two positive integers such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2.

Then, for every integer a coprime to n1 and n2, we have

On1(a) = On2(a) · n1
gcd(n1, Rn2(a)).

6

The proof of this theorem is based on the following lemma.

Lemma 8. Let n be a positive integer and let a be an integer coprime to n. Let m be an
integer such that rad(m)| rad n. Then, there exists an integer um, coprime to n if m is odd,
or coprime to n/2 if m is even, such that

aOn(a)·m = 1 + um · Rn(a) · m.

Proof. We distinguish diﬀerent cases based upon the parity of m. First, we prove the odd
case by induction on m. If m = 1, then, by deﬁnition of the integer Rn(a), we have

aOn(a) = 1 + Rn(a).

Therefore the assertion is true for m = 1.
Now, let p be a prime factor of m and suppose that the assertion is true for the odd
number m/p, i.e., there exists an integer um/p, coprime to n, such that

aOn(a)· m
p = 1 + um/p · Rn(a) · m
p .

Then, we obtain

aOn(a)·m = (aOn(a)· m
p )p = (1 + um/p · Rn(a) · m
p
 )p

= 1 + um/p · Rn(a) · m +
 p−1∑

k=2
 (p
k
) (
um/p · Rn(a) · m
p
 )k + (
um/p · Rn(a) · m
p
 )p

= 1 +
 (

um/p +
 p−1∑

k=2
 (p
k)

p · (um/p)
k · Rn(a)
k−1 · (m
p
 )k−1+

+(um/p)
p · Rn(a)
p−1

p · ( m
p
 )p−1)
 · Rn(a) · m

= 1 + um · Rn(a) · m.

Since n divides Rn(a) which divides

um − um/p =
 p−1∑

k=2
 (p
k)

p · (um/p)
k · Rn(a)
k−1 · ( m
p
 )k−1 + (um/p)
p · Rn(a)
p−1

p · (m
p
 )p−1,

it follows that gcd(um, n) = gcd(um/p, n) = 1. This completes the proof for the odd case.
Suppose now that n and m are even. We proceed by induction on v2(m). If v2(m) = 1,
then m/2 is odd and by the ﬁrst part of this proof,

a m
2 ·On(a) = 1 + um/2 · m
2 · Rn(a)

where um/2 is coprime to n and hence to n/2. Now assume that v2(m) > 1 and that

a m
2 ·On(a) = 1 + um/2 · m
2 · Rn(a)

7

with um/2 coprime to n/2. Then, we obtain

aOn(a)·m = (
aOn(a)· m
2 )2 = (
1 + um/2 · Rn(a) · m
2
 )2

= 1 + um/2 · Rn(a) · m + (
um/2 · Rn(a) · m
2
 )2

= 1 + (um/2 + (um/2)
2 · Rn(a)
2 · m
2
 ) · Rn(a)m

= 1 + um · Rn(a) · m.

Since n/2 divides Rn(a)/2 which divides um−um/2, it follows that gcd(um, n/2) = gcd(um/2, n/2) =
1. This completes the proof.

We are now ready to prove Theorem 7.

Proof of Theorem 7. The proof is by induction on the integer n1/n2. If n1 = n2, then we
have n1
gcd(n1, Rn2(a)) = n1
gcd(n1, Rn1(a)) = n1
n1 = 1,

since Rn1(a) is divisible by n1, and thus the statement is true. Let p be a prime factor of n1
and n2 such that n2 divides n1/p and suppose that

On1/p(a) = On2(a) · n1/p
gcd(n1/p, Rn2(a)).

First, the congruence aOn1 (a) ≡ 1 (mod n1)

implies that aOn1 (a) ≡ 1 (mod n1
p )

and so On1/p(a) divides On1(a). We consider two cases.

First Case: vp(n1) ⩽ vp (Rn2(a)).
Since n2 divides n1/p, it follows that On2(a) divides On1/p(a). Let r = On1/p(a)
On2 (a) . Hence

Rn1/p(a) = aOn1/p(a) − 1 = aOn2 (a)·r − 1 = (aOn2 (a) − 1
) ( r−1∑

k=0 akOn2 (a))

= Rn2(a)
 ( r−1∑

k=0 akOn2 (a))

and so Rn1/p(a) is divisible by Rn2(a). This leads to

vp(n1) ⩽ vp (Rn2(a)) ⩽ vp (Rn1/p(a)
) .

8

Therefore Rn1/p(a) is divisible by n1 and hence we have

aOn1/p(a) = 1 + Rn1/p(a) ≡ 1 (mod n1).

This implies that On1(a) = On1/p(a). Moreover, the hypothesis vp(n1) ⩽ vp (Rn2(a)) implies
that gcd(n1/p, Rn2(a)) = gcd(n1, Rn2(a))/p. Finally, we obtain

On1(a) = On1/p(a) = On2(a) · n1/p
gcd(n1/p, Rn2(a)) = On2(a) · n1
gcd(n1, Rn2(a)).

Second Case: vp(n1) > vp (Rn2(a)).
If v2(n1) ⩽ 1, then (n1/p)/ gcd(n1/p, Rn2(a)) is odd. Otherwise, if v2(n1) ⩾ 2, then v2(n2) ⩾
2 and every integer coprime to n2/2 is also coprime to n2. In both cases, v2(n1) ⩽ 1 or
v2(n1) ⩾ 2, we know, by Lemma 8, that there exists an integer u, coprime to n2, such that

aOn1/p(a) = aOn2 (a)· n1/p
gcd(n1/p,Rn2 (a)) = 1 + u · Rn2(a) · n1/p
gcd(n1/p, Rn2(a))

= 1 + u · Rn2(a)
gcd(n1/p, Rn2(a)) · n1
p .

As vp (Rn2(a)) ⩽ vp (n1/p), it follows that Rn2(a)/ gcd(n1/p, Rn2(a)) is coprime to p, and
hence On1/p(a) is a proper divisor of On1(a) since

aOn1/p(a) ̸≡ 1 (mod n1).

Moreover, by Lemma 8 again, there exists an integer up such that

aOn1/p(a)·p = 1 + up · Rn1/p(a) · p ≡ 1 (mod n1).

This leads to

On1(a) = On1/p(a) · p = On2(a) · n1
gcd(n1/p, Rn2(a)) = On2(a) · n1
gcd(n1, Rn2(a)).

This completes the proof of Theorem 7.

We may view Theorem 7 as a generalization of Theorem 3.6 of [3], where n2 = p is an odd
prime number and n1 = pk for some positive integer k. Note that the conclusion of Theorem 7
fails in general in the case where v2(n1) ⩾ 2 and n2 = rad(n1). For instance, for n1 = 24 =
3 · 2
3, n2 = 6 = 3 · 2 and a = 7, we obtain that On1(a) = 2 while On2(a)n1/ gcd(n1, Rn2(a)) =
24/ gcd(24, 6) = 4.
We now turn to the proof of the main result of this paper.

Proof of Theorem 6. From Theorem 7, we obtain

αn1(a) = On1(an1) = On1(a)
gcd(On1(a), n1) = On2(a) · n1
gcd(n1,Rn2 (a))

gcd (
On2(a) · n1
gcd(n1,Rn2 (a)) , n1)

= On2(a)
gcd(On2(a), n1, Rn2(a)).
 9

Thus,
 αn2(a)
αn1(a) =
 On2 (a)
gcd(On2 (a),n2)

On2 (a)
gcd(On2 (a),n1,Rn2 (a)) = gcd(On2(a), n1, Rn2(a))
gcd(On2(a), n2)

= gcd ( On2(a)
gcd(On2(a), n2), n2
gcd(On2(a), n2) · gcd(n1, Rn2(a))
n2
 ) .

Finally, since we have

gcd ( On2(a)
gcd(On2(a), n2), n2
gcd(On2(a), n2)
) = gcd(On2(a), n2)
gcd(On2(a), n2) = 1,

it follows that

αn2(a)
αn1(a) = gcd ( On2(a)
gcd(On2(a), n2), gcd(n1, Rn2(a))
n2
 ) = gcd (αn2(a), gcd(n1, Rn2(a))
n2
 ) .

Thus, the determination of αn is reduced to the case where n is square-free.

Corollary 9. Let n be a positive integer such that v2(n) ⩽ 1. Then, for every integer a,
coprime to n, we have
 αn(a) = αrad(n)(a)

gcd (
αrad(n)(a), gcd(n,Rrad(n)(a))
rad(n) ) .

Corollary 10. Let n be a positive integer such that v2(n) ⩾ 2. Then, for every integer a,
coprime to n, we have
 αn(a) = α2 rad(n)(a)

gcd (α2 rad(n)(a), gcd(n,R2 rad(n)(a))
2 rad(n) ) .

3 The arithmetic function βn

First, we can observe that, by deﬁnition of the functions αn and βn, we have

αn(a) = βn(a) = 0

for every integer a not coprime to n and

αn(a)
βn(a) ∈ {1, 2}

for every integer a coprime to n. There is no general formula known to compute αn(a)/βn(a)
but, however, we get the following proposition.

10

Proposition 11. Let n1 and n2 be two positive integers such that rad(n1) = rad(n2). Let a
be an integer coprime to n1 and n2. If v2(n1) ⩽ 1, then we have

αn1(a)
βn1(a) = αn2(a)
βn2(a) .

If v2(n1) ⩾ 2, then we have αn1(a) = βn1(a).

Proof. Let n1 be a positive integer such that v2(n1) ⩽ 1 and a be an integer coprime to n1.
Let p be an odd prime factor of n1 such that vp(n1) ⩾ 2. We will prove that

αn1(a)
βn1(a) = αn1/p(a)
βn1/p(a) .

If αn1(a) = 2βn1(a), then aβn1 (a)·n1 ≡ −1 (mod n1)

and thus aβn1 (a)·p· n1
p ≡ −1 (mod n1
p ).

This implies that αn1/p(a) = 2βn1/p(a). Conversely, if αn1/p(a) = 2βn1/p(a), then we have

aβn1/p(a)· n1
p ≡ −1 (mod n1
p ).

Since vp(n1) ⩾ 2, it follows that
 aβn1/p(a)· n1
p ≡ −1 (mod p)

and thus

aβn1/p(a)·n1+1 = 1−
(
−aβn1/p(a)· n1
p )p = (1 + aβn1/p(a)· n1
p ) p−1∑

k=0
 (
−aβn1/p(a)· n1
p )k ≡ 0 (mod n1).

This implies that αn1(a) = 2βn1(a). Continuing this process we have

αn1(a)
βn1(a) = αrad(n1)(a)
βrad(n1)(a)

and since rad(n1) = rad(n2), αn1(a)
βn1(a) = αn2(a)
βn2(a) .

Now, let n1 be a positive integer such that v2(n1) ⩾ 2, and let a be a non-zero integer.
Suppose that we have αn1(a) = 2βn1(a). Since

aβn1 (a)·n1 ≡ −1 (mod n1)

11

it follows that (
aβn1 (a)· n1
4 )4 ≡ −1 (mod 4)

in contradiction with (
aβn1 (a)· n1
4 )4 ≡ 1 (mod 4).

Thus αn1(a) = βn1(a).

If n is a prime power, then βn = βrad(n), in analogy with Proposition 3 for αn.

Proposition 12. Let p be a prime number and let a be an integer. Then we have

βpk(a) = βp(a)

for every positive integer k.

Proof. This result is trivial for every integer a not coprime to p. Suppose now that a is
coprime to p. For p = 2, then, by Proposition 11, we have

β2k(a) = α2k(a) = 1

for every positive integer k. For an odd prime number p ⩾ 3, Proposition 11 and Proposi-
tion 3 lead to
 βpk(a) = αpk(a)
αp(a) · βp(a) = βp(a)

for every positive integer k. This completes the proof.

Let n1 and n2 be two positive integers such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2.

It immediately follows that βn1(a) = βn2(a) = 0 for every integer a not coprime to n1 and
n2. Finally, we determine the relationship between βn1(a) and βn2(a) for every integer a
coprime to n1 and n2.

Theorem 13. Let n1 and n2 be two positive integers such that
{ rad(n1)|n2 and n2|n1, if v2(n1) ⩽ 1;
2 rad(n1)|n2 and n2|n1, if v2(n1) ⩾ 2.

Let a be an integer coprime to n1 and n2. Then, we have

βn1(a) = βn2(a)

gcd (βn2(a), gcd(n1,Rn2 (a))
n2
 ) .

12

Proof. If v2(n1) ⩽ 1, then Theorem 6 and Proposition 11 lead to

βn2(a)
βn1(a) = αn2(a)
αn1(a) = gcd (
αn2(a), gcd(n1, Rn2(a))
n2
 ) .

Since v2(n2) = v2(n1) ⩽ 1, it follows that gcd(n1, Rn2(a))/n2 is odd and hence, we have

βn2(a)
βn1(a) = gcd (αn2(a), gcd(n1, Rn2(a))
n2
 ) = gcd (βn2(a), gcd(n1, Rn2(a))
n2
 ) .

If v2(n1) ⩾ 2, then βn1(a) = αn1(a) and βn2(a) = αn2(a) by Proposition 11 and the result
follows from Theorem 6.

Thus, as for αn, the determination of βn is reduced to the case where n is square-free.

Corollary 14. Let n be a positive integer such that v2(n) ⩽ 1. Then, for every integer a,
coprime to n, we have
 βn(a) = βrad(n)(a)

gcd (
βrad(n)(a), gcd(n,Rrad(n)(a))
rad(n) ) .

Corollary 15. Let n be a positive integer such that v2(n) ⩾ 2. Then, for every integer a,
coprime to n, we have
 βn(a) = β2 rad(n)(a)

gcd (β2 rad(n)(a), gcd(n,R2 rad(n)(a))
2 rad(n) ) .

4 Acknowledgments

The author would like to thank Shalom Eliahou for his help in preparing this paper. He also
thanks the anonymous referee for his/her useful remarks.

References

[1] Jonathan Chappelon, On a problem of Molluzzo concerning Steinhaus triangles in ﬁnite
cyclic groups, Integers 8 (2008), #A37.

[2] John C. Molluzzo, Steinhaus graphs, Theory and Applications of Graphs, Springer,
volume 642 of Lecture Notes in Mathematics, Berlin / Heidelberg, 1978, pp. 394–402.

[3] Melvyn B. Nathanson, Elementary Methods in Number Theory, Springer, 2000, pp.
92–93.
 13

2000 Mathematics Subject Classiﬁcation: Primary 11A05; Secondary 11A07, 11A25.
Keywords: multiplicative order, projective multiplicative order, balanced Steinhaus trian-
gles, Steinhaus triangles, Molluzzo’s problem.

Received October 16 2009; revised version received January 20 2010. Published in Journal
of Integer Sequences, January 27 2010.

Return to Journal of Integer Sequences home page.

14
