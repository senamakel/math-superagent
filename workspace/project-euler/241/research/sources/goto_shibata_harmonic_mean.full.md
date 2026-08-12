<!-- source: https://www.ams.org/journals/mcom/2004-73-245/S0025-5718-03-01554-0/S0025-5718-03-01554-0.pdf | converted from PDF -->

MATHEMATICS OF COMPUTATION
Volume 73, Number 245, Pages 475–491
S 0025-5718(03)01554-0
Article electronically published on June 19, 2003

ALL NUMBERS WHOSE POSITIVE DIVISORS
HAVE INTEGRAL HARMONIC MEAN UP TO 300

T. GOTO AND S. SHIBATA

Abstract. A positive integer n is said to be harmonic when the harmonic
mean H(n) of its positive divisors is an integer. Ore proved that every perfect
number is harmonic. No nontrivial odd harmonic numbers are known. In
this article, the list of all harmonic numbers n with H(n) ≤ 300 is given. In
particular, such harmonic numbers are all even except 1.

1. Introduction

A positive integer n is said to be perfect if σ(n)=2n,where σ(n) denotes
the sum of the positive divisors of n. Itisanopenproblem whether ornot an
odd perfect number exists. In this connection, Ore [8] introduced the concept of
harmonic numbers. A positive integer n is said to be harmonic if the harmonic
mean of its positive divisors

(1) H(n)= nτ (n)
σ(n)

is an integer, where τ (n) denotes the number of the positive divisors of n.Ore
proved the following fact which represents the relationship between perfect numbers
and harmonic numbers.

Theorem 1.1 ([8]). Every perfect number is harmonic.

The converse of this theorem does not hold. For example, 140 is not perfect, but
H(140) = 5. Ore listed all harmonic numbers up to 104 and this list was extended
by Garcia [5] to 107 and by Cohen [2] to 2·109. No nontrivial odd harmonic numbers
have been discovered. Ore conjectured the following statement. If this conjecture
holds, it follows that odd perfect numbers do not exist.

Conjecture. All harmonic numbers other than 1 must be even.

Kanold [7] showed the following fact.

Theorem 1.2 ([7]). For any positive integer c, there exist only ﬁnitely many num-
bers n satisfying H(n)= c.

In [6, B2], Guy wrote: “Which values does the harmonic mean take? Presumably
not 4, 12, 16, 18, 20, 22,.. .; does it take the value 23?” Cohen [2] settled the ﬁrst of
these questions for the ﬁrst two values.

Received by the editor December 10, 2001 and, in revised form, July 17, 2002.
2000 Mathematics Subject Classiﬁcation. Primary 11A25, 11Y70.
Key words and phrases. Harmonic number, perfect number, Ore’s conjecture.

c⃝2003 American Mathematical Society

475

476 T. GOTO AND S. SHIBATA

Theorem 1.3 ([2]). Let n be harmonic and H(n) ≤ 13.Then n is one of the 13
numbers listed in Table 4 (at the end of this paper). In particular, the numbers n
with H(n)= 4 or 12 do not exist.

This result is extended to H(n) ≤ 300. For this, some propositions and a com-
puter were used. The program is written by Mathematica®, and it takes about
three months to get the result. For H(n) ≤ 200, we need only about two days.

Main result. Let n be harmonic and H(n) ≤ 300.Then n is one of the 280
numbers listed in Table 4 (at the end of this paper). In particular, such harmonic
numbers are all even except 1. The table includes the nonexistence of numbers n
with H(n) being equal to one of the numbers that Guy listed. In the table, the values
of H(n) ≤ 300 are omitted when there is no corresponding value of n.

For example, we solve the equation H(n)= 14 in §5. In §2, we recall the known
facts about harmonic numbers. Then the general method of the search for the
harmonic numbers n with H(n)= c is explained in §3. In this search, the following
proposition proved in §4is useful.

Proposition 1.4. Let p be prime. If H(n)= 2p,then 2p | n.If H(n)= 3p,then
p | n.

This is analogous to the following fact due to Cohen.

Proposition 1.5 ([2]). Let p be prime. If H(n)= p, then either p | n or n is an
even perfect number.

Cohen and Sorli [3] introduced the concept of harmonic seeds.

Deﬁnition. Let d be a divisor of an integer n.We call d a unitary divisor of n and
n a unitary multiple of d if (d, n/d) = 1. A harmonic number is called a harmonic
seed if it does not have a smaller proper unitary divisor which is harmonic (we call
a unitary divisor d proper if d> 1).

Every harmonic number is a unitary multiple of a certain harmonic seed. It is
conjectured that such a harmonic seed is unique. Table 4 includes the harmonic
seed of all harmonic numbers listed, and in all of these cases the seed is unique.

2. Known facts

In this section, we recall the known facts about harmonic numbers. The following
lemma is a fundamental property of H, and we often use it without special mention.

Lemma 2.1. Let n, m, e, f be positive integers and p, q primes.
• H is multiplicative, i.e., H(nm)= H(n)H(m) if (n, m)= 1.
• H is monotone, i.e., H(pe) <H(pf ) <H(qf ) if e< f and p< q.

Proof. The ﬁrst statement is clear from the deﬁnition (1). The second statement
is also clear from the fact that H is averaging of positive numbers (this statement
is a special case of Lemma 7 in Cohen and Deng [4]). □

We denote the number of the distinct primes dividing n by ω(n).

Theorem 2.2 ([8], [10]). Let n be a harmonic number and ω(n) ≤ 2.Then n is
an even perfect number.

INTEGRAL HARMONIC MEAN UP TO 300 477

Ore [8] proved the nonexistence of harmonic numbers n with ω(n) = 1. In 1973,
Pomerance proved that a harmonic number n with ω(n)= 2 must be an even
perfect number (cf. [10]), and Callan [1] rediscovered the proof of the same fact in
1992.

Theorem 2.3 ([8]). Let n be a harmonic number greater than 6.Then n is not
squarefree.

Theorem 2.4 ([3]). For any integer n,

H(n) > 2ω(n)+1

ω(n)+ 1 ,

with the following exceptions (in which p denotes a prime): n = p, n =2p, n =6p
(p ̸=3),n =30p (7 ≤ p ≤ 23),n =1, 15, 21, 70. By Theorems 2.2 and 2.3, a
harmonic number n greater than 6 satisﬁes the inequality.

Theorem 2.5 ([5]). Let n be an odd harmonic number and pe ∥ n.Then pe ≡ 1
(mod 4).

In order to prove Theorem 2.5, we provide the following lemma, which is often
used later. Let p be a prime and let Q be a rational number. Suppose that
Q = pem/n with p ∤ mn.Then we denote by ordp(Q) the exponent e in this paper.

Lemma 2.6. Let p be an integer (not necessarily prime). If p ≡ 1(mod 4),then

ord2(1 + p + ··· + pe)= ord2(e +1).

If p ≡ 3(mod 4) and ord2(p +1) = m,then

ord2(1 + p + ··· + pe)= { ord2(e +1) + m − 1, if e is odd,
0, if e is even.

Proof of Theorem 2.5. Let p be a prime and e a positive integer. If pe ≡ 1(mod 4).
Then ord2(H(pe)) = 0 by Lemma 2.6. If pe ≡ 3 (mod 4), then ord2(H(pe)) < 0.
Hence H(n) cannot be integral if pe ≡ 3(mod 4),pe ∥ n and 2 ∤ n. □

Lemma 2.6 is a standard fact. For example, see [9]. The following simple proof
is due to Koichi Tanaka, an undergraduate student of Kyushu University.

Proof of Lemma 2.6. Let e +1 = 2kl,where k is an integer and l is odd. The
statement is clear when k = 0. Suppose that k ≥ 1. Then

1+ p + ··· + pe =(pe+1 − 1)/(p − 1) = (p2
kl − 1)/(p − 1)

=(p2
(k−1)l +1)(p2
(k−2)l +1) ··· (p2l +1)(pl +1)(pl − 1)/(p − 1).

The last part of this expression (pl − 1)/(p − 1) = pl−1 + ··· + p + 1 is odd, and the
rest of the parts are all even. In particular, p2
(k−i)l +1 ≡ 2(mod 4)for 1 ≤ i ≤ k −1.
Since pl +1 = (p +1)(pl−1 − ··· +1),

ord2(pl +1) = ord2(p +1) = { 1, if p ≡ 1(mod 4),
m, if p ≡ 3(mod 4).

Now, the proof is complete. □

478 T. GOTO AND S. SHIBATA

3. General algorithm

In this section, we give the general algorithm of searching all integers n satisfying
H(n)= c for a ﬁxed integer c. Roughly speaking, it has three steps.
(1) List the possibilities of ω(n), the number of distinct primes dividing n.
(2) For each value of ω(n), list the possibilities of the types of exponents in the
factorization of n.
(3) For each type of exponents, list the possibilities of primes dividing n.
Then check whether or not H(n)= c for the ﬁnite possibilities of n. Practically,
the existence of this algorithm veriﬁes Theorem 1.2.
This algorithm ﬁnishes in ﬁnite time, but not always in reasonable time. We
can make this time shorter, using Propositions 1.4 and 1.5, Lemma 4.1, and some
methods explained in §5.

3.1. Possibilities of the numbers of distinct primes. Recall that we denote
the number of distinct primes dividing n by ω(n). Suppose that n is harmonic. Then
either n is an even perfect number or ω(n) ≥ 3 by Theorem 2.2. And Theorem 2.4
gives an upper bound of ω(n). But in order to get the upper bound, we may use
the following method.
For example, suppose that ω(n)=5. Then H(n) ≥ H(2 · 3 · 5 · 7 · 11). For
harmonic number n, H(n) ≥ H(22 · 3 · 5 · 7 · 11) = 13.75 because such n must not be
squarefree by Theorem 2.3 (see also Lemma 4.2). Since H(n)is integral, we have
H(n) ≥ 14. Thus, we get Table 1.
Note that Cohen [2] gives a more precise version of such a table.

Example. Suppose that H(n)= 5. Then ω(n) must be 2 or 3. Next, suppose that
H(n) = 14. Then n cannot be an even perfect number, so ω(n)must be 3, 4or 5.

3.2. Possibilities of the types of exponents. We denote by (e1,...,er)the type
of exponents of n = pe1
1 ··· per
r with e1 ≥ ··· ≥ er. Suppose a harmonic number n
has the type (e1,... ,er). Since H(pe) <e+1, we have H(n) ≤ (e1+1) ··· (er+1)−1.
We can take the round-up of the value H(2e1 · 3e2 ··· qer
r ) as the lower bound of
H(n), where qr is the rth prime.

Example. Suppose that H(n)=5 and n is not an even perfect number. Then
ω(n) must be 3. The type of exponents is not (1, 1, 1) by Theorem 2.3. When it is
(2, 1, 1), the lower bound of H is 5 since H(22 · 3 · 5) = 4.28 ··· . The upper bound
is 3 · 2 · 2 − 1 = 11. If thetypeis (2, 2, 1) or (3, 1, 1), then H(n) ≥ 6. Hence the
only possibility of the type of exponents is (2, 1, 1).

Table 1. The lower bound of integral H(n)

ω(n) Theorem 2.4 this method
3 4 5
4 7 8
5 11 14
6 19 26
7 32 49
8 57 92
9 103 176
10 187 340

INTEGRAL HARMONIC MEAN UP TO 300 479

Cohen and Deng [4] have already given the inequality H(n) ≤ τ (n) − 1for
harmonic numbers n. Using Theorem 1.3, they also showed H(n) ≤ τ (n) − 8when
n is an even harmonic number and n ̸=6, 28, 140, 496, 8128. An improved result is
possible using the main result of this paper.

3.3. Possibilities of primes. We deﬁne S(n)= σ(n)/n.Let p, q be primes and
e, f positive integers. If p<q and e< f , then it is easily veriﬁed that

1 <S(qe) <S(qf ) <S(pe) <S(pf ) < 2

and S(pe) → p/(p − 1) as e →∞. Suppose that the type of exponents of n is
(e1,... ,er). Then τ (n)=(e1 +1) ··· (er + 1). Since H(n)= c, which is ﬁxed,
S(n)must be equal to τ (n)/H(n)=(e1 +1) ··· (er +1)/c. If the smallest prime
dividing n is p,then S(n) <S(pe1 ) ··· S(per ) < (p/(p − 1))
r, so it follows that
p< S(n)
1/r · (S(n)
1/r − 1)
−1. In this way, we have the ﬁnite possibilities of the
second smallest prime dividing n, third smallest prime, and so on.

Example. Suppose that H(n)= 5 and n is not an even perfect number. Then the
type of the exponents of n must be (2, 1, 1). So we have τ (n)=3 · 2 · 2 = 12 and
S(n)= τ (n)/H(n)= 12/5. If n were odd, then S(n) ≤ S(32 · 5 · 7) = 208/105 <
12/5, a contradiction. Therefore it follows that 2 | n. Next, if the second smallest
prime dividing n were greater than 5, then S(n) ≤ S(22 · 7 · 11) = 24/11 < 12/5, a
contradiction. Therefore it follows that the second smallest prime dividing n is 3 or
5. By Proposition 1.5, we have 5 | n.If 3 | n, then the possibilities of n are 22 · 3 · 5,
2 · 32 · 5and 2 · 3 · 52, but H(n) is not integral in these cases. Let p be a prime
greater than 5. If n =22 · 5 · p,then H(p)= 5/H(22 · 5) = 7/4, so p =7. We get a
solution n =22 · 5 · 7 = 140. If n =2 · 52 · p,then H(p)= 5/H(2 · 52)= 31/20, but
this does not have a solution. Similarly, there does not exist a solution in the case
that n =2 · 5 · p2. Hence all the solutions of H(n) = 5 are 140 and an even perfect
number 496. We remark that Cohen and Sorli [3] have given a simpler proof of this
fact, but their proof is not as algorithmically viable.

4. Proof of Proposition 1.4

In this section, we give the proof of Proposition 1.4.

Lemma 4.1. If H(n) is even, then n is even.

Proof. Let p be an odd prime and e a positive integer. Then ord2(H(pe)) ≤ 0by
Lemma 2.6. Hence H(n) cannot be even for an odd integer n. □

The following lemma is a special case of Lemma 5 in Cohen and Deng [4].

Lemma 4.2. Let e, f be nonnegative integers and p, q primes. If e< f and p<q,
then H(peqf ) >H(pf qe).

Proof of Proposition 1.4. We give only the proof of the ﬁrst statement. The second
statement can be proved similarly. Let H(n)=2p. In view of Lemma 4.1, it is
suﬃcient to show that p | n. Assume that p ∤ n.Then p | τ (n)since nτ (n)=
2pσ(n). We put n = qkp−1m with a prime q and positive integers k and m.We
can assume without loss of generality that q ∤ m.Since ω(n) ≥ 3 by Theorem 2.2,
it follows that ω(m) ≥ 2. So we have H(n)= H(qkp−1m) ≥ H(2kp−1)H(6) >kp.
Hence k =1 and n = qp−1m.Since
q − 1
q p<H(qp−1) <p

480 T. GOTO AND S. SHIBATA

and H(n)= 2p,wehave
 2 <H(m) < 2q
q − 1 .

Therefore it follows that 20
9 = H(10) < 2q
q − 1 ,

so the possibilities of q are only 2, 3, 5and 7.
(i) Assume that n =7p−1 m with 7 ∤ m.Since 6p/7 <H(7p−1) <p,we have
2 <H(m) < 7/3. Therefore the only possibility of m is 10. From the equation
H(7p−1 · 10) = 2p,we have 7p−1 = 3, a contradiction.
(ii) Assume that n =5p−1 m with 5 ∤ m.Since 4p/5 <H(5p−1) <p,wehave
2 <H(m) < 5/2. But we give a better estimation below. When p =2, 3, 5, the
statement holds by Theorem 1.3. From now on, we assume that p ≥ 7. Then it
follows that
 H(5p−1)= 4 · 5p−1 p
5p − 1 ≤ 4 · 56

57 − 1 p.

Hence H(m) ≥ (57 − 1)/(2 · 56) > 2.4999.

Claim. There does not exist an integer m satisfying 2.4999 <H(m) < 2.5.

Suppose that 2.4999 <H(m) < 2.5. If ω(m) ≥ 3, then H(m) ≥ H(2 · 3 · 5) > 2.5.
So we have ω(m) ≤ 2.
Assume that ω(m)= 2 and let m = peqf be the factorization of m.If max(e, f ) ≥
2, then H(m) ≥ H(22 · 3) > 2.5 by Lemmas 2.1 and 4.2. So we have f = e =1.
If m is odd, then H(m) ≥ H(3 · 5) = 2.5, a contradiction. Assume that m is
even. Since H(2 · 13) = 2.47 ··· and H(2 · 17) = 2.51 ··· , it is impossible that
2.4999 <H(m) < 2.5. Similarly, we can deal with the case that ω(m)=1.
(iii) We can deal with the case n =3p−1 m with 3 ∤ m similarly. In fact, there
does not exist an integer m satisfying 2.998 <H(m) < 3,ω(m) ≥ 2and 3 ∤ m.
(iv) Assume that n =2p−1 m with 2 ∤ m.Since

1
2 p< H(2p−1)= 2p−1 p
2p − 1 ≤ 26

27 − 1 p,

we have 3.96875 <H(m) < 4. Such integers m satisfying ω(m) ≥ 2and 2 ∤ m are
only 32 ·23 and products of distinct two odd primes. First, put H(2p−1 32 ·23) = 2p.
Then we have 2p−1 = 104, a contradiction.
Next, put H(2p−1 p1p2)= 2p,where p1 and p2 are distinct odd primes. Then it
follows that 2p−1 p
2p − 1 · p1
p1+1
2 · p2
p2+1
2 =2p.

Therefore we have
 2p−2 p1p2 =(2p − 1) · p1 +1
2 · p2 +1
2 .

Hence the odd integer 2p − 1 is equal to either one of p1,p2 or the product p1p2.
If 2p − 1= p1,then

2p−2 p2 = p1 +1
2 · p2 +1
2 =2p−1 · p2 +1
2 ,

which has no solution. If 2p − 1= p1p2,then

2p−2 = p1 +1
2 · p2 +1
2 .

INTEGRAL HARMONIC MEAN UP TO 300 481

Hencewehave p1p2 +1 = (p1 +1)(p2 + 1), a contradiction. Now, all the possibilities
of p ∤ n are denied, so the proof is complete. □

5. Only solution of H(n)= 14

In this section, we show that n = 18620 is the only solution of H(n)= 14 using
Proposition 1.4. For such an integer n, it follows that ω(n) ≥ 3and 14 | n by
Theorem 2.2 and Proposition 1.4. Let

ord2(n)= s, ord7(n)= t.

We have 1 ≤ s ≤ 9since H(210 · 7 · 3) > 14. Similarly we have 1 ≤ t ≤ 7. Table 2
is the table of H(2s).
Suppose that s =9 and n =29 · 7tm with (m, 14) = 1. Since H(n) is an integer,
it is necessary that 31 | τ (n)or31 | m. Assume that 31 | τ (n). Then n has a prime
raised to 30th power or higher as a factor. In this case, H(n) >H(29 · 330) > 14, a
contradiction. In the case that 31 | m,we also have H(n) ≥ H(29 · 7 · 31) > 14. In
this way, the possibilities of s =7, 8, 9 are denied.
In thecasethat s = 6, it is necessary that 127 | n. We put n =26 · 127um,
where u is a positive integer and (m, 254) = 1. If u is odd, then ord2(H(n)) ≤ 0
by Lemma 2.6, hence it is impossible that H(n) = 14. If u is even, then H(n) ≥
H(26 · 1272 · 3) > 14. A similar argument denies the possibility of s =4. Put
n =24 · 31um with (m, 62) = 1. Then u must be even and it is necessary that
ord2(H(m)) = −3 by Lemma 2.6. But H(n) ≥ H(24 · 312 · 47) > 14 in this case.
From now on, the following clear fact is often used.

Lemma 5.1. Let m be a positive integer. The smallest values of H(m) are as
follows:

H(1) = 1,H(2) = 4/3=1.33 ··· ,H(3) = 3/2= 1.5,H(5) = 5/3= 1.66 ··· .

In other cases, H(m) > 1.7.

Suppose that s =5 and n =25 · 7tm with (m, 14) = 1. If t ≥ 3, then H(n) ≥
H(25·73) > 14, a contradiction. Assume that t =2. Since H(25·72)= (26·7)/(3·19),
it is necessary that 19 | n.But H(n) ≥ H(25 · 72 · 19) > 14. Assume that t =1.
Then H(m)= 14/H(25 · 7) = 1.31 ··· , a contradiction to Lemma 5.1. Therefore
the possibility of s = 5 is denied.
Next, we give Table 3, the table of H(7t).
The possibilities of 4 ≤ t ≤ 7 are denied by an argument similar to that of
the cases of 7 ≤ s ≤ 9. Assume that t =1 and n =7m with 7 ∤ m.Then
H(m)= H(n)/H(7) = 8. By Theorem 1.3, we have m =25 · 3 · 7. But thisisa
contradiction to 7 ∤ m. Hence t = 2 or 3. When t = 3, it is necessary that s =3
since ord2(H(73)) = −2. The remaining possibilities are s =3, t =2, 3, or s =1, 2,
t =2.
 Table 2.

s H(2
s) s H(2
s) s H(2
s)

1 2
2/3 4 (2
4 · 5)/31 7 2
10/(3 · 5 · 17)
2 (2
2 · 3)/7 5 2
6/(3 · 7) 8 (2
8 · 3
2)/(7 · 73)
3 2
5/(3 · 5) 6 (2
6 · 7)/127 9 (2
10 · 5)/(3 · 11 · 31)

482 T. GOTO AND S. SHIBATA

Table 3.

t H(7
t) t H(7
t) t H(7
t)

1 7/2
2 4 (5 · 7
4)/2801 7 7
7/(2
2 · 5
2 · 1201)
2 7
2/19 5 7
5/(2
2 · 19 · 43)
3 7
3/(2
2 · 5
2) 6 7
7/(29 · 4733)

Suppose that s =3 and n =23 · 7tm,where (m, 14) = 1 and t = 2 or 3. First,
assume that t =3. Since H(23 · 73)= (23 · 73)/(3 · 53), it is necessary that 5 | n.If
ord5(n) ≥ 2, then H(n) ≥ H(23 · 73 · 52) > 14. If n =23 · 73 · 5m with (m, 70) = 1,
then H(m)=14/H(23 · 73 · 5) = 1.14 ··· , a contradiction to Lemma 5.1. Secondly,
assume that t =2. Since H(23 · 72)= (25 · 72)/(3 · 5 · 19), it is necessary that 19 | n.
But we deduce a contradiction by the above argument.
Suppose that s =2 and t =2. Since H(22 ·72)= (22 ·3·7)/19, it is necessary that
19 | n.If 193 | n,then H(n) ≥ H(22 · 72 · 193) > 14. Assume that 192 ∥ n and put
n =22 · 72 · 192m with (m, 266) = 1. Then H(m)=14/H(22 · 72 · 192)=1.11 ··· .
Hence the only possibility is 19 ∥ n.Since H(22 · 72 · 19) = (2 · 3 · 7)/5, it is necessary
that 5 | n.In fact, H(22 · 72 · 19 · 5) = 14, so we get the solution n = 18620.
Suppose that s =1 and t =2. Since H(2 · 72)= (22 · 72)/(3 · 19), it is necessary
that 19 | n.If 194 | n,then H(n) ≥ H(2 · 72 · 194) > 14. If n =2 · 72 · 193m with
(m, 266) = 1, then H(m)=14/H(2 · 72 · 193)=1.07 ··· .If n =2 · 72 · 192m with
(m, 266) = 1, then H(m)= 14/H(2 · 72 · 192)= 1.43 ··· . Hence we have 19 ∥ n and
n =2 · 72 · 19m with (m, 266) = 1. Since H(2 · 72 · 19) = (2 · 72)/(3 · 5), it is necessary
that 5 | m.If 52 | m,then H(n) ≥ H(2 · 72 · 19 · 52) > 14. If n =2 · 72 · 19 · 5m′

with (m′, 1330) = 1, then H(m′)= 14/H(2 · 72 · 19 · 5) = 1.28 ··· , a contradiction.
We have checked all possibilities; hence 18620 is the only solution of H(n) = 14.

6. Open problems

The problems in this section are proposed by the pioneers or the authors.

Problem 1. Does a nontrivial odd harmonic number exist?

Ore conjectured that the answer is “no”. If the conjecture is true, then odd
perfect numbers do not exist.

Problem 2. Are there inﬁnitely many harmonic numbers? How about harmonic
seeds?

It seems that the answer to this problem is “yes”, but it is not clear. On this
topic, the authors’ question is as follows.

Problem 3. Are there inﬁnitely many harmonic seeds n with ω(n)= 3? If not,
ﬁnd all such n.Does an odd one exist?

All such numbers which the authors know are n = 270 with H(n)= 6, n = 672
with H(n) = 8, and n = 6200 with H(n) = 10. How about the same problem with
ω(n)=4, 5,... ? Note that there exist only ﬁnitely many harmonic numbers with
a ﬁxed type of exponents, because of the inequality H(n) <τ (n)and Theorem 1.2.
Cohen and Sorli [3] conjectured that a harmonic seed of a harmonic number is
always unique.
 INTEGRAL HARMONIC MEAN UP TO 300 483

Problem 4. Does every harmonic number have a unique harmonic seed?

We say that n is powerful if p | n implies p2 | n,where p is prime. Cohen and
Sorli [3] implied that nontrivial harmonic numbers are not powerful.

Problem 5. Does a nontrivial powerful harmonic number exist?

It is showed that there are no nontrivial powerful harmonic numbers less than
1012 in [3]. Euler showed that the factorization of an odd perfect number must have
the form pep2e1
1 ··· p2er
r with p ≡ e ≡ 1 (mod 4). If odd powerful harmonic numbers
other than 1 do not exist, the form of an odd perfect number must be pp2e1
1 ··· p2er
r
with p ≡ 1(mod 4).
Nontrivial harmonic numbers listed in Table 4 are perfect numbers or abundant
numbers. In other words, if H(n)is integral and 1 <H(n) ≤ 300, then S(n)=
σ(n)/n ≥ 2.

Problem 6. Does a nontrivial deﬁcient harmonic number exist?

A harmonic number n is deﬁcient if and only if H(n) >τ (n)/2. Cohen and Deng
[4] remarked that H(n) < 2τ (n)/3 for an even harmonic number n.
A positive integer n is said to be arithmetic if the arithmetic mean of its positive
divisors A(n)= σ(n)/τ (n) is an integer. For example, odd primes are arithmetic.
Ore observed that almost all (small) harmonic numbers n with ω(n) ≥ 3are arith-
metic and conjectured that all such numbers are arithmetic. But he soon found
the counterexample 950976. Such counterexamples are marked with an asterisk in
Table 4. On this topic, the following facts hold.

Proposition 6.1. Let n be harmonic. Then n is arithmetic if and only if H(n) | n.
In particular, even perfect numbers are not arithmetic.

Proof. The ﬁrst statement is clear from the equation H(n)A(n)= n.Since H(n)=
p for an even perfect number n =2p−1(2p−1), the second statement is also clear. □

In view of Proposition 6.1, Proposition 1.5 says: “If H(n) is a prime and n
is not an even perfect number, then n is arithmetic.” And the ﬁrst statement of
Proposition 1.4 says: “If H(n) is a double of a prime, then n is arithmetic.”

Problem 7. Assume that H(n) is a triple of a prime. Is n arithmetic?

If H(n) is a triple of a prime and less than 300, then n is arithmetic. But it is
not clear whether or not 3 divides n when H(n) > 300.

484 T. GOTO AND S. SHIBATA

Table 4. All harmonic numbers with H(n) ≤ 300

H(n) n factorization of n seed
1 1
2 6 2 · 3 seed
3 28 2
2 · 7 seed
5 140 2
2 · 5 · 7 2
2 · 7
496 2
4 · 31 seed
6 270 2 · 3
3 · 5 seed
7 8128 2
6 · 127 seed
8 672 2
5 · 3 · 7 seed
9 1638 2 · 3
2 · 7 · 13 seed
10 6200 2
3 · 5
2 · 31 seed
11 2970 2 · 3
3 · 5 · 11 2 · 3
3 · 5
13 105664 2
6 · 13 · 127 2
6 · 127
33550336 2
12 · 8191 seed
14 18620 2
2 · 5 · 7
2 · 19 seed
15 8190 2 · 3
2 · 5 · 7 · 13 2 · 3
2 · 7 · 13
18600 2
3 · 3 · 5
2 · 31 2
3 · 5
2 · 31
17 27846 2 · 3
2 · 7 · 13 · 17 2 · 3
2 · 7 · 13
8589869056 2
16 · 131071 seed
19 117800 2
3 · 5
2 · 19 · 31 2
3 · 5
2 · 31
137438691328 2
18 · 524287 seed
21 55860 2
2 · 3 · 5 · 7
2 · 19 2
2 · 5 · 7
2 · 19
24 30240 2
5 · 3
3 · 5 · 7 seed
32760 2
3 · 3
2 · 5 · 7 · 13 seed
25 173600 2
5 · 5
2 · 7 · 31 seed
26 242060 2
2 · 5 · 7
2 · 13 · 19 2
2 · 5 · 7
2 · 19
27 167400 2
3 · 3
3 · 5
2 · 31 2
3 · 5
2 · 31

∗950976 2
6 · 3
2 · 13 · 127 2
6 · 127

∗301953024 2
12 · 3
2 · 8191 2
12 · 8191
29 237510 2 · 3
2 · 5 · 7 · 13 · 29 2 · 3
2 · 7 · 13
539400 2
3 · 3 · 5
2 · 29 · 31 2
3 · 5
2 · 31
31 23 ·· · 8139952128 2
30 · (2
31 − 1) seed
35 2229500 2
2 · 5
3 · 7
3 · 13 seed
37 4358600 2
3 · 5
2 · 19 · 31 · 37 2
3 · 5
2 · 31
5085231579136 2
18 · 37 · 524287 2
18 · 524287
39 726180 2
2 · 3 · 5 · 7
2 · 13 · 19 2
2 · 5 · 7
2 · 19
41 2290260 2
2 · 3 · 5 · 7
2 · 19 · 41 2
2 · 5 · 7
2 · 19
42 1089270 2 · 3
2 · 5 · 7
2 · 13 · 19 seed
44 332640 2
5 · 3
3 · 5 · 7 · 11 2
5 · 3
3 · 5 · 7
360360 2
3 · 3
2 · 5 · 7 · 11 · 13 2
3 · 3
2 · 5 · 7 · 13
45 4754880 2
6 · 3
2 · 5 · 13 · 127 2
6 · 127
1509765120 2
12 · 3
2 · 5 · 8191 2
12 · 8191
46 695520 2
5 · 3
3 · 5 · 7 · 23 2
5 · 3
3 · 5 · 7

INTEGRAL HARMONIC MEAN UP TO 300 485

Table 4. (continued)

H(n) n factorization of n seed
753480 2
3 · 3
2 · 5 · 7 · 13 · 23 2
3 · 3
2 · 5 · 7 · 13
47 1421280 2
5 · 3
3 · 5 · 7 · 47 2
5 · 3
3 · 5 · 7
1539720 2
3 · 3
2 · 5 · 7 · 13 · 47 2
3 · 3
2 · 5 · 7 · 13
48 4713984 2
9 · 3
3 · 11 · 31 seed
49 5772200 2
3 · 5
2 · 7
2 · 19 · 31 2
3 · 5
2 · 31
8506400 2
5 · 5
2 · 7
3 · 31 seed
6734495875072 2
18 · 7
2 · 524287 2
18 · 524287
50 6051500 2
2 · 5
3 · 7
2 · 13 · 19 seed
51 2845800 2
3 · 3
3 · 5
2 · 17 · 31 2
3 · 5
2 · 31
16166592 2
6 · 3
2 · 13 · 17 · 127 2
6 · 127
5133201408 2
12 · 3
2 · 17 · 8191 2
12 · 8191
53 8872200 2
3 · 3
3 · 5
2 · 31 · 53 2
3 · 5
2 · 31
50401728 2
6 · 3
2 · 13 · 53 · 127 2
6 · 127
16003510272 2
12 · 3
2 · 53 · 8191 2
12 · 8191
54 ∗2178540 2
2 · 3
2 · 5 · 7
2 · 13 · 19 2
2 · 5 · 7
2 · 19
60 2457000 2
3 · 3
3 · 5
3 · 7 · 13 seed
61 14 ·· · 6537079808 2
30 · 61 · (2
31 − 1) 2
30 · (2
31 − 1)
26 ·· · 5953842176 2
60 · (2
61 − 1) seed
70 23088800 2
5 · 5
2 · 7
2 · 19 · 31 seed
73 318177800 2
3 · 5
2 · 19 · 31 · 37 · 73 2
3 · 5
2 · 31
371221905276928 2
18 · 37 · 73 · 524287 2
18 · 524287
75 18154500 2
2 · 3 · 5
3 · 7
2 · 13 · 19 2
2 · 5
3 · 7
2 · 13 · 19

∗57 ·· · 3498803200 2
30 · 5
2 · (2
31 − 1) 2
30 · (2
31 − 1)
77 11981970 2 · 3
2 · 5 · 7
2 · 11 · 13 · 19 2 · 3
2 · 5 · 7
2 · 13 · 19
78 115048440 2
3 · 3
2 · 5 · 13
2 · 31 · 61 seed
80 23569920 2
9 · 3
3 · 5 · 11 · 31 2
9 · 3
3 · 11 · 31
81 29410290 2 · 3
5 · 5 · 7
2 · 13 · 19 seed
82 44660070 2 · 3
2 · 5 · 7
2 · 13 · 19 · 41 2 · 3
2 · 5 · 7
2 · 13 · 19
83 90409410 2 · 3
2 · 5 · 7
2 · 13 · 19 · 83 2 · 3
2 · 5 · 7
2 · 13 · 19
84 32997888 2
9 · 3
3 · 7 · 11 · 31 2
9 · 3
3 · 11 · 31
85 80832960 2
6 · 3
2 · 5 · 13 · 17 · 127 2
6 · 127
25666007040 2
12 · 3
2 · 5 · 17 · 8191 2
12 · 8191
86 14303520 2
5 · 3
3 · 5 · 7 · 11 · 43 2
5 · 3
3 · 5 · 7
15495480 2
3 · 3
2 · 5 · 7 · 11 · 13 · 43 2
3 · 3
2 · 5 · 7 · 13
87 137891520 2
6 · 3
2 · 5 · 13 · 29 · 127 2
6 · 127
43783188480 2
12 · 3
2 · 5 · 29 · 8191 2
12 · 8191
88 255428096 2
9 · 7 · 11
2 · 19 · 31 seed
89 423184320 2
6 · 3
2 · 5 · 13 · 89 · 127 2
6 · 127
134369095680 2
12 · 3
2 · 5 · 89 · 8191 2
12 · 8191
19 ·· · 1548169216 2
88 · (2
89 − 1) seed
91 75038600 2
3 · 5
2 · 7
2 · 13 · 19 · 31 2
3 · 5
2 · 31
110583200 2
5 · 5
2 · 7
3 · 13 · 31 2
5 · 5
2 · 7
3 · 31

486 T. GOTO AND S. SHIBATA

Table 4. (continued)

H(n) n factorization of n seed
87548446375936 2
18 · 7
2 · 13 · 524287 2
18 · 524287
92 108421632 2
9 · 3
3 · 11 · 23 · 31 2
9 · 3
3 · 11 · 31
94 221557248 2
9 · 3
3 · 11 · 31 · 47 2
9 · 3
3 · 11 · 31
96 17428320 2
5 · 3
2 · 5 · 7
2 · 13 · 19 seed
45532800 2
7 · 3
3 · 5
2 · 17 · 31 seed

∗459818240 2
8 · 5 · 7 · 19 · 37 · 73 seed

∗10200236032 2
14 · 7 · 19 · 31 · 151 seed
97 559903400 2
3 · 5
2 · 7
2 · 19 · 31 · 97 2
3 · 5
2 · 31
825120800 2
5 · 5
2 · 7
3 · 31 · 97 2
5 · 5
2 · 7
3 · 31
653246099881984 2
18 · 7
2 · 97 · 524287 2
18 · 524287
99 23963940 2
2 · 3
2 · 5 · 7
2 · 11 · 13 · 19 2
2 · 5 · 7
2 · 19
1630964808 2
3 · 3
4 · 11
3 · 31 · 61 seed
101 287425800 2
3 · 3
3 · 5
2 · 17 · 31 · 101 2
3 · 5
2 · 31
1632825792 2
6 · 3
2 · 13 · 17 · 101 · 127 2
6 · 127
518453342208 2
12 · 3
2 · 17 · 101 · 8191 2
12 · 8191
102 37035180 2
2 · 3
2 · 5 · 7
2 · 13 · 17 · 19 2
2 · 5 · 7
2 · 19
105 69266400 2
5 · 3 · 5
2 · 7
2 · 19 · 31 2
5 · 5
2 · 7
2 · 19 · 31
81695250 2 · 3
3 · 5
3 · 7
2 · 13 · 19 seed
106 115462620 2
2 · 3
2 · 5 · 7
2 · 13 · 19 · 53 2
2 · 5 · 7
2 · 19
107 233103780 2
2 · 3
2 · 5 · 7
2 · 13 · 19 · 107 2
2 · 5 · 7
2 · 19
13 ·· · 7783728128 2
106 · (2
107 − 1) seed
108 52141320 2
3 · 3
4 · 5 · 7 · 11
2 · 19 seed
110 27027000 2
3 · 3
3 · 5
3 · 7 · 11 · 13 2
3 · 3
3 · 5
3 · 7 · 13
114 46683000 2
3 · 3
3 · 5
3 · 7 · 13 · 19 2
3 · 3
3 · 5
3 · 7 · 13
115 56511000 2
3 · 3
3 · 5
3 · 7 · 13 · 23 2
3 · 3
3 · 5
3 · 7 · 13
116 71253000 2
3 · 3
3 · 5
3 · 7 · 13 · 29 2
3 · 3
3 · 5
3 · 7 · 13
117 644271264 2
5 · 3
2 · 7 · 13
2 · 31 · 61 seed
118 144963000 2
3 · 3
3 · 5
3 · 7 · 13 · 59 2
3 · 3
3 · 5
3 · 7 · 13
120 ∗142990848 2
9 · 3
2 · 7 · 11 · 13 · 31 seed
121 8698459616 2
5 · 7
2 · 11
2 · 19
2 · 127 seed
125 ∗73924348400 2
4 · 5
2 · 7 · 31
2 · 83 · 331 seed
127 14 ·· · 1199152128 2
126 · (2
127 − 1) seed
128 1867650048 2
10 · 3
4 · 11 · 23 · 89 seed
130 300154400 2
5 · 5
2 · 7
2 · 13 · 19 · 31 2
5 · 5
2 · 7
2 · 19 · 31
132 766284288 2
9 · 3 · 7 · 11
2 · 19 · 31 2
9 · 7 · 11
2 · 19 · 31
135 163390500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 19 2
2 · 5
3 · 7
2 · 13 · 19
139 3209343200 2
5 · 5
2 · 7
2 · 19 · 31 · 139 2
5 · 5
2 · 7
2 · 19 · 31
140 164989440 2
9 · 3
3 · 5 · 7 · 11 · 31 2
9 · 3
3 · 11 · 31
143 1265532840 2
3 · 3
2 · 5 · 11 · 13
2 · 31 · 61 2
3 · 3
2 · 5 · 13
2 · 31 · 61
144 ∗1379454720 2
8 · 3 · 5 · 7 · 19 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73

∗30600708096 2
14 · 3 · 7 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
145 526480500 2
2 · 3 · 5
3 · 7
2 · 13 · 19 · 29 2
2 · 5
3 · 7
2 · 13 · 19

INTEGRAL HARMONIC MEAN UP TO 300 487

Table 4. (continued)

H(n) n factorization of n seed
16 ·· · 1465292800 2
30 · 5
2 · 29 · (2
31 − 1) 2
30 · (2
31 − 1)
147 4409499089268 2
2 · 3
3 · 7
4 · 13 · 467 · 2801 seed
149 2705020500 2
2 · 3 · 5
3 · 7
2 · 13 · 19 · 149 2
2 · 5
3 · 7
2 · 13 · 19
85 ·· · 1321676800 2
30 · 5
2 · 149 · (2
31 − 1) 2
30 · (2
31 − 1)
150 2876211000 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61 seed
152 447828480 2
9 · 3
3 · 5 · 11 · 19 · 31 2
9 · 3
3 · 11 · 31
153 499974930 2 · 3
5 · 5 · 7
2 · 13 · 17 · 19 2 · 3
5 · 5 · 7
2 · 13 · 19
155 110886522600 2
3 · 3 · 5
2 · 7 · 31
2 · 83 · 331 seed
156 428972544 2
9 · 3
3 · 7 · 11 · 13 · 31 2
9 · 3
3 · 11 · 31
158 1862023680 2
9 · 3
3 · 5 · 11 · 31 · 79 2
9 · 3
3 · 11 · 31
159 1558745370 2 · 3
5 · 5 · 7
2 · 13 · 19 · 53 2 · 3
5 · 5 · 7
2 · 13 · 19
160 51001180160 2
14 · 5 · 7 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
161 758951424 2
9 · 3
3 · 7 · 11 · 23 · 31 2
9 · 3
3 · 11 · 31
163 7279591410 2 · 3
2 · 5 · 7
2 · 13 · 19 · 41 · 163 2 · 3
2 · 5 · 7
2 · 13 · 19
164 1352913408 2
9 · 3
3 · 7 · 11 · 31 · 41 2
9 · 3
3 · 11 · 31
165 8154824040 2
3 · 3
4 · 5 · 11
3 · 31 · 61 2
3 · 3
4 · 11
3 · 31 · 61
166 2738824704 2
9 · 3
3 · 7 · 11 · 31 · 83 2
9 · 3
3 · 11 · 31
167 5510647296 2
9 · 3
3 · 7 · 11 · 31 · 167 2
9 · 3
3 · 11 · 31
168 318729600 2
7 · 3
3 · 5
2 · 7 · 17 · 31 2
7 · 3
3 · 5
2 · 17 · 31
326781000 2
3 · 3
3 · 5
3 · 7
2 · 13 · 19 seed
481572000 2
5 · 3
3 · 5
3 · 7
3 · 13 seed
169 13660770240 2
6 · 3
2 · 5 · 13
3 · 17 · 127 2
6 · 127
23 ·· · 4766487552 2
30 · 13
2 · 61 · (2
31 − 1) 2
30 · (2
31 − 1)
44 ·· · 6199327744 2
60 · 13
2 · (2
61 − 1) 2
60 · (2
61 − 1)
171 8410907232 2
5 · 3
2 · 7
2 · 13 · 19
2 · 127 seed

∗221908282624 2
8 · 7 · 19
2 · 37 · 73 · 127 seed
172 10983408128 2
9 · 7 · 11
2 · 19 · 31 · 43 2
9 · 7 · 11
2 · 19 · 31
173 23855232960 2
6 · 3
2 · 5 · 13 · 29 · 127 · 173 2
6 · 127
7574491607040 2
12 · 3
2 · 5 · 29 · 173 · 8191 2
12 · 8191
176 191711520 2
5 · 3
2 · 5 · 7
2 · 11 · 13 · 19 2
5 · 3
2 · 5 · 7
2 · 13 · 19
500860800 2
7 · 3
3 · 5
2 · 11 · 17 · 31 2
7 · 3
3 · 5
2 · 17 · 31
5058000640 2
8 · 5 · 7 · 11 · 19 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73
112202596352 2
14 · 7 · 11 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
181 13581986600 2
3 · 5
2 · 7
2 · 13 · 19 · 31 · 181 2
3 · 5
2 · 31
20015559200 2
5 · 5
2 · 7
3 · 13 · 31 · 181 2
5 · 5
2 · 7
3 · 31
15 ·· · 8794044416 2
18 · 7
2 · 13 · 181 · 524287 2
18 · 524287
184 400851360 2
5 · 3
2 · 5 · 7
2 · 13 · 19 · 23 2
5 · 3
2 · 5 · 7
2 · 13 · 19
1047254400 2
7 · 3
3 · 5
2 · 17 · 23 · 31 2
7 · 3
3 · 5
2 · 17 · 31
10575819520 2
8 · 5 · 7 · 19 · 23 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73
234605428736 2
14 · 7 · 19 · 23 · 31 · 151 2
14 · 7 · 19 · 31 · 151
186 540277920 2
5 · 3
2 · 5 · 7
2 · 13 · 19 · 31 2
5 · 3
2 · 5 · 7
2 · 13 · 19

∗14254365440 2
8 · 5 · 7 · 19 · 31 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73

488 T. GOTO AND S. SHIBATA

Table 4. (continued)

H(n) n factorization of n seed
187 407386980 2
2 · 3
2 · 5 · 7
2 · 11 · 13 · 17 · 19 2
2 · 5 · 7
2 · 19
27726401736 2
3 · 3
4 · 11
3 · 17 · 31 · 61 2
3 · 3
4 · 11
3 · 31 · 61
188 819131040 2
5 · 3
2 · 5 · 7
2 · 13 · 19 · 47 2
5 · 3
2 · 5 · 7
2 · 13 · 19
2140041600 2
7 · 3
3 · 5
2 · 17 · 31 · 47 2
7 · 3
3 · 5
2 · 17 · 31
21611457280 2
8 · 5 · 7 · 19 · 37 · 47 · 73 2
8 · 5 · 7 · 19 · 37 · 73
479411093504 2
14 · 7 · 19 · 31 · 47 · 151 2
14 · 7 · 19 · 31 · 151
189 623397600 2
5 · 3
3 · 5
2 · 7
2 · 19 · 31 2
5 · 5
2 · 7
2 · 19 · 31

∗675347400 2
3 · 3
2 · 5
2 · 7
2 · 13 · 19 · 31 2
3 · 5
2 · 31

∗995248800 2
5 · 3
2 · 5
2 · 7
3 · 13 · 31 2
5 · 5
2 · 7
3 · 31

∗787936017383424 2
18 · 3
2 · 7
2 · 13 · 524287 2
18 · 524287
191 3328809120 2
5 · 3
2 · 5 · 7
2 · 13 · 19 · 191 2
5 · 3
2 · 5 · 7
2 · 13 · 19
8696764800 2
7 · 3
3 · 5
2 · 17 · 31 · 191 2
7 · 3
3 · 5
2 · 17 · 31
87825283840 2
8 · 5 · 7 · 19 · 37 · 73 · 191 2
8 · 5 · 7 · 19 · 37 · 73
1948245082112 2
14 · 7 · 19 · 31 · 151 · 191 2
14 · 7 · 19 · 31 · 151
192 57575890944 2
13 · 3
2 · 11 · 13 · 43 · 127 seed
193 108061356200 2
3 · 5
2 · 7
2 · 19 · 31 · 97 · 193 2
3 · 5
2 · 31
159248314400 2
5 · 5
2 · 7
3 · 31 · 97 · 193 2
5 · 5
2 · 7
3 · 31
12 ·· · 7277222912 2
18 · 7
2 · 97 · 193 · 524287 2
18 · 524287
195 900463200 2
5 · 3 · 5
2 · 7
2 · 13 · 19 · 31 2
5 · 5
2 · 7
2 · 19 · 31
3221356320 2
5 · 3
2 · 5 · 7 · 13
2 · 31 · 61 2
5 · 3
2 · 7 · 13
2 · 31 · 61
8628633000 2
3 · 3
3 · 5
3 · 13
2 · 31 · 61 seed
197 4720896180 2
2 · 3
2 · 5 · 7
2 · 11 · 13 · 19 · 197 2
2 · 5 · 7
2 · 19
321300067176 2
3 · 3
4 · 11
3 · 31 · 61 · 197 2
3 · 3
4 · 11
3 · 31 · 61
198 ∗22385029489560 2
3 · 3
10 · 5 · 23 · 107 · 3851 seed
200 ∗714954240 2
9 · 3
2 · 5 · 7 · 11 · 13 · 31 2
9 · 3
2 · 7 · 11 · 13 · 31
201 2481357060 2
2 · 3
2 · 5 · 7
2 · 13 · 17 · 19 · 67 2
2 · 5 · 7
2 · 19
202 3740553180 2
2 · 3
2 · 5 · 7
2 · 13 · 17 · 19 · 101 2
2 · 5 · 7
2 · 19
203 2008725600 2
5 · 3 · 5
2 · 7
2 · 19 · 29 · 31 2
5 · 5
2 · 7
2 · 19 · 31
2369162250 2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 29 2 · 3
3 · 5
3 · 7
2 · 13 · 19
204 886402440 2
3 · 3
4 · 5 · 7 · 11
2 · 17 · 19 2
3 · 3
4 · 5 · 7 · 11
2 · 19
205 2839922400 2
5 · 3 · 5
2 · 7
2 · 19 · 31 · 41 2
5 · 5
2 · 7
2 · 19 · 31
3349505250 2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 41 2 · 3
3 · 5
3 · 7
2 · 13 · 19
207 1199250360 2
3 · 3
4 · 5 · 7 · 11
2 · 19 · 23 2
3 · 3
4 · 5 · 7 · 11
2 · 19
209 513513000 2
3 · 3
3 · 5
3 · 7 · 11 · 13 · 19 2
3 · 3
3 · 5
3 · 7 · 13
211 24362612820 2
2 · 3
2 · 5 · 7
2 · 13 · 19 · 53 · 211 2
2 · 5 · 7
2 · 19
212 2763489960 2
3 · 3
4 · 5 · 7 · 11
2 · 19 · 53 2
3 · 3
4 · 5 · 7 · 11
2 · 19
213 3702033720 2
3 · 3
4 · 5 · 7 · 11
2 · 19 · 71 2
3 · 3
4 · 5 · 7 · 11
2 · 19
214 5579121240 2
3 · 3
4 · 5 · 7 · 11
2 · 19 · 107 2
3 · 3
4 · 5 · 7 · 11
2 · 19
215 1162161000 2
3 · 3
3 · 5
3 · 7 · 11 · 13 · 43 2
3 · 3
3 · 5
3 · 7 · 13
216 43947421401888 2
5 · 3
6 · 23 · 137 · 547 · 1093 seed
217 1179832600464 2
4 · 3 · 7
2 · 19 · 31
2 · 83 · 331 seed
218 2945943000 2
3 · 3
3 · 5
3 · 7 · 11 · 13 · 109 2
3 · 3
3 · 5
3 · 7 · 13

INTEGRAL HARMONIC MEAN UP TO 300 489

Table 4. (continued)

H(n) n factorization of n seed
220 3831421440 2
9 · 3 · 5 · 7 · 11
2 · 19 · 31 2
9 · 7 · 11
2 · 19 · 31
221 10952611488 2
5 · 3
2 · 7 · 13
2 · 17 · 31 · 61 2
5 · 3
2 · 7 · 13
2 · 31 · 61
222 1727271000 2
3 · 3
3 · 5
3 · 7 · 13 · 19 · 37 2
3 · 3
3 · 5
3 · 7 · 13
224 13073550336 2
10 · 3
4 · 7 · 11 · 23 · 89 2
10 · 3
4 · 11 · 23 · 89

∗66433720320 2
13 · 3
3 · 5 · 11 · 43 · 127 seed
226 5275179000 2
3 · 3
3 · 5
3 · 7 · 13 · 19 · 113 2
3 · 3
3 · 5
3 · 7 · 13
227 10597041000 2
3 · 3
3 · 5
3 · 7 · 13 · 19 · 227 2
3 · 3
3 · 5
3 · 7 · 13
228 2716826112 2
9 · 3
2 · 7 · 11 · 13 · 19 · 31 2
9 · 3
2 · 7 · 11 · 13 · 31
229 12941019000 2
3 · 3
3 · 5
3 · 7 · 13 · 23 · 229 2
3 · 3
3 · 5
3 · 7 · 13
230 ∗3288789504 2
9 · 3
2 · 7 · 11 · 13 · 23 · 31 2
9 · 3
2 · 7 · 11 · 13 · 31
232 4146734592 2
9 · 3
2 · 7 · 11 · 13 · 29 · 31 2
9 · 3
2 · 7 · 11 · 13 · 31
233 150115204512 2
5 · 3
2 · 7 · 13
2 · 31 · 61 · 233 2
5 · 3
2 · 7 · 13
2 · 31 · 61
235 ∗6720569856 2
9 · 3
2 · 7 · 11 · 13 · 31 · 47 2
9 · 3
2 · 7 · 11 · 13 · 31
236 8436460032 2
9 · 3
2 · 7 · 11 · 13 · 31 · 59 2
9 · 3
2 · 7 · 11 · 13 · 31
237 11296276992 2
9 · 3
2 · 7 · 11 · 13 · 31 · 79 2
9 · 3
2 · 7 · 11 · 13 · 31
239 34174812672 2
9 · 3
2 · 7 · 11 · 13 · 31 · 239 2
9 · 3
2 · 7 · 11 · 13 · 31
240 1307124000 2
5 · 3
3 · 5
3 · 7
2 · 13 · 19 seed
1381161600 2
7 · 3
2 · 5
2 · 7 · 13 · 17 · 31 seed
153003540480 2
14 · 3 · 5 · 7 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
241 2096328767456 2
5 · 7
2 · 11
2 · 19
2 · 127 · 241 2
5 · 7
2 · 11
2 · 19
2 · 127
245 3622293071600 2
4 · 5
2 · 7
3 · 31
2 · 83 · 331 seed
22047495446340 2
2 · 3
3 · 5 · 7
4 · 13 · 467 · 2801 2
2 · 3
3 · 7
4 · 13 · 467 · 2801
248 57897151488 2
10 · 3
4 · 11 · 23 · 31 · 89 2
10 · 3
4 · 11 · 23 · 89
252 ∗1553357978368 2
8 · 7
2 · 19
2 · 37 · 73 · 127 seed

∗54934276752360 2
3 · 3
6 · 5 · 23 · 137 · 547 · 1093 seed
253 17624538624 2
9 · 3 · 7 · 11
2 · 19 · 23 · 31 2
9 · 7 · 11
2 · 19 · 31
254 237191556096 2
10 · 3
4 · 11 · 23 · 89 · 127 2
10 · 3
4 · 11 · 23 · 89
255 2777638500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 17 · 19 2
2 · 5
3 · 7
2 · 13 · 19
256 19209881600 2
11 · 5
2 · 7
2 · 13 · 19 · 31 seed
258 32950224384 2
9 · 3 · 7 · 11
2 · 19 · 31 · 43 2
9 · 7 · 11
2 · 19 · 31
260 2144862720 2
9 · 3
3 · 5 · 7 · 11 · 13 · 31 2
9 · 3
3 · 11 · 31
261 4738324500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 29 2
2 · 5
3 · 7
2 · 13 · 19
262 100383241728 2
9 · 3 · 7 · 11
2 · 19 · 31 · 131 2
9 · 7 · 11
2 · 19 · 31
263 201532767744 2
9 · 3 · 7 · 11
2 · 19 · 31 · 263 2
9 · 7 · 11
2 · 19 · 31
264 15174001920 2
8 · 3 · 5 · 7 · 11 · 19 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73

∗43861478400 2
10 · 3
3 · 5
2 · 23 · 31 · 89 seed
336607789056 2
14 · 3 · 7 · 11 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
265 8659696500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 53 2
2 · 5
3 · 7
2 · 13 · 19
266 3134799360 2
9 · 3
3 · 5 · 7 · 11 · 19 · 31 2
9 · 3
3 · 11 · 31
267 14541754500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 89 2
2 · 5
3 · 7
2 · 13 · 19
269 43952044500 2
2 · 3
3 · 5
3 · 7
2 · 13 · 19 · 269 2
2 · 5
3 · 7
2 · 13 · 19
270 ∗2701389600 2
5 · 3
2 · 5
2 · 7
2 · 13 · 19 · 31 2
5 · 5
2 · 7
2 · 19 · 31

490 T. GOTO AND S. SHIBATA

Table 4. (continued)

H(n) n factorization of n seed

∗71271827200 2
8 · 5
2 · 7 · 19 · 31 · 37 · 73 seed
272 23450730240 2
8 · 3 · 5 · 7 · 17 · 19 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73
520212037632 2
14 · 3 · 7 · 17 · 19 · 31 · 151 2
14 · 7 · 19 · 31 · 151
273 57648181500 2
2 · 3
2 · 5
3 · 7
3 · 13
3 · 17 seed
275 31638321000 2
3 · 3
2 · 5
3 · 11 · 13
2 · 31 · 61 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61
276 31727458560 2
8 · 3 · 5 · 7 · 19 · 23 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73
703816286208 2
14 · 3 · 7 · 19 · 23 · 31 · 151 2
14 · 7 · 19 · 31 · 151
277 888988066400 2
5 · 5
2 · 7
2 · 19 · 31 · 139 · 277 2
5 · 5
2 · 7
2 · 19 · 31
278 22933532160 2
9 · 3
3 · 5 · 7 · 11 · 31 · 139 2
9 · 3
3 · 11 · 31
279 ∗42763096320 2
8 · 3 · 5 · 7 · 19 · 31 · 37 · 73 2
8 · 5 · 7 · 19 · 37 · 73
997978703400 2
3 · 3
3 · 5
2 · 7 · 31
2 · 83 · 331 seed
282 64834371840 2
8 · 3 · 5 · 7 · 19 · 37 · 47 · 73 2
8 · 5 · 7 · 19 · 37 · 73
1438233280512 2
14 · 3 · 7 · 19 · 31 · 47 · 151 2
14 · 7 · 19 · 31 · 151
284 97941285120 2
8 · 3 · 5 · 7 · 19 · 37 · 71 · 73 2
8 · 5 · 7 · 19 · 37 · 73
2172650274816 2
14 · 3 · 7 · 19 · 31 · 71 · 151 2
14 · 7 · 19 · 31 · 151
285 42054536160 2
5 · 3
2 · 5 · 7
2 · 13 · 19
2 · 127 2
5 · 3
2 · 7
2 · 13 · 19
2 · 127
54648009000 2
3 · 3
2 · 5
3 · 13
2 · 19 · 31 · 61 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61

∗1109541413120 2
8 · 5 · 7 · 19
2 · 37 · 73 · 127 2
8 · 7 · 19
2 · 37 · 73 · 127

∗24613169545216 2
14 · 7 · 19
2 · 31 · 127 · 151 seed
287 180789462659988 2
2 · 3
3 · 7
4 · 13 · 41 · 467 · 2801 2
2 · 3
3 · 7
4 · 13 · 467 · 2801
290 83410119000 2
3 · 3
2 · 5
3 · 13
2 · 29 · 31 · 61 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61
291 427721411658996 2
2 · 3
3 · 7
4 · 13 · 97 · 467 · 2801 2
2 · 3
3 · 7
4 · 13 · 467 · 2801
293 1291983233155524 2
2 · 3
3 · 7
4 · 13 · 293 · 467 · 2801 2
2 · 3
3 · 7
4 · 13 · 467 · 2801
295 169696449000 2
3 · 3
2 · 5
3 · 13
2 · 31 · 59 · 61 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61
296 16569653760 2
9 · 3
3 · 5 · 11 · 19 · 31 · 37 2
9 · 3
3 · 11 · 31
297 ∗125356165141536 2
5 · 3
10 · 7 · 23 · 107 · 3851 seed
298 428555439000 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61 · 149 2
3 · 3
2 · 5
3 · 13
2 · 31 · 61
299 9866368512 2
9 · 3
3 · 7 · 11 · 13 · 23 · 31 2
9 · 3
3 · 11 · 31

Acknowledgments

We would like to thank Professor Masanobu Kaneko for introducing us to this
topic. We are also grateful to the referee for his/her useful advice.

References

[1] D. Callan, Solution to Problem 6616, Amer. Math. Monthly 99 (1992), 783–789.
[2] G. L. Cohen, Numbers whose positive divisors have small integral harmonic mean, Math.
Comp. 66 (1997), 883–891. MR 97f:11007
[3] G.L. Cohen and R.M.Sorli, Harmonic seeds, Fibonacci Quart. 36 (1998), 386–390; Errata,
Fibonacci Quart. 39 (2001), 4. MR 99j:11002
[4] G. L. Cohen and Deng Moujie, On a generalisation of Ore’s harmonic numbers, Nieuw. Arch.
Wisk. (4) 16 (1998), 161–172. MR 2000k:11008

INTEGRAL HARMONIC MEAN UP TO 300 491

[5] M. Garcia, On numbers with integral harmonic mean, Amer. Math. Monthly 61 (1954),
89–96. MR 15:506d
[6] R. K. Guy, Unsolved Problems in Number Theory, second edition, Springer-Verlag, New
York, 1994. MR 96e:11002
[7] H. J. Kanold, ¨Uber das harmonische Mittel der Teiler einer nat¨urlichen Zahl, Math. Ann.
133 (1957), 371–374. MR 19:635f
[8] O. Ore, On the averages of the divisors of a number, Amer. Math. Monthly 55 (1948),
615–619. MR 10:284a
[9] Solution to Problem E3445, Amer. Math. Monthly 99 (1992), 795.
[10] C. Pomerance, On a problem of Ore: Harmonic numbers (unpublished typescript); see Ab-
stract 709-A5, Notices Amer. Math. Soc. 20 (1973) A-648.

Graduate School of Mathematics, Kyushu University 33, Fukuoka 812-8581, Japan
E-mail address: tgoto@math.kyushu-u.ac.jp
Current address: Department of Mathematics, Tokyo University of Science, Noda, Chiba 278-
8510, Japan
E-mail address: goto takeshi@ma.noda.tus.ac.jp

Faculty of Mathematics, Kyushu University 33, Fukuoka 812-8581, Japan
E-mail address: ma200019@math.kyushu-u.ac.jp
