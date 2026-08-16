<!-- source: https://www.maths.tcd.ie/pub/Maths/Courseware/NumberTheory/ch05.pdf | converted from PDF -->

Chapter 5

The Chinese Remainder Theorem

5.1 Coprime moduli

Theorem 5.1. Suppose m, n ∈ N, and

gcd(m, n) = 1.

Given any remainders r mod m and s mod n we can ﬁnd N such that

N ≡ r mod m and N ≡ s mod n.

Moreover, this solution is unique mod mn.

Proof. We use the pigeon-hole principle. Consider the mn numbers

0 ≤ N < mn.

For each N consider the remainders

r = N mod m, s = N mod n,

where r, s are chosen so that

0 ≤ r < m, 0 ≤ s < n.

We claim that these pairs r, s are diﬀerent for diﬀerent N ∈ [0, mn). For
suppose N < N ′ have the same remainders, ie

N ′ ≡ N mod m and N ′ ≡ N mod n.

Then m | N ′ − N and n | N ′ − N.

Since gcd(m, n) = 1, it follows that

mn | N ′ − N.

But that is impossible, since
0 < N ′ − N < mn.

5–1

Example: Let us ﬁnd N such that

N ≡ 3 mod 13, N ≡ 7 mod 23.

One way to ﬁnd N is to ﬁnd a, b such that

a ≡ 1 mod m, a ≡ 0 mod n,
b ≡ 0 mod m, b ≡ 1 mod n.

For then we can take N = 3a + 7b.

Note that a = 1 + sm = tn.

We are back to the Euclidean Algorithm for gcd(m, n):

23 = 2 · 13 − 3,
13 = 4 · 3 + 1,

giving
 1 = 13 − 4 · 3
= 13 − 4(2 · 13 − 23)
= 4 · 23 − 7 · 13.

Thus we can take
 a = 4 · 23 = 92, b = −7 · 13 = −91.

giving N = 3 · 92 − 7 · 91 = 276 − 637 = −361.

Of course we can add a multiple of mn to N; so we could take

N = 13 · 23 − 361 = 299 − 361 = −62,

if we want the smallest solution (by absolute value); or

N = 299 − 62 = 237,

for the smallest positive solution.

5.2 The modular ring

We can express the Chinese Remainder Theorem in more abstract language.

Theorem 5.2. If gcd(m, n) = 1 then the ring Z/(mn) is isomorphic to the
product of the rings Z/(m) and Z/(n):

Z/(mn) = Z/(m) × Z/(n).

5–2

Proof. We have seen that the maps

N ↦→ N mod m and N ↦→ N mod n

deﬁne ring-homomorphisms

Z/(mn) → Z/(m) and Z/(mn) → Z/(n).

These combine to give a ring-homomorphism

Z/(mn) → Z/(m) × Z/(n),

under which r mod mn ↦→ (r mod m, r mod n).

But we have seen that this map is bijective; hence it is a ring-isomorphism.

5.3 The totient function

Proposition 5.1. Suppose gcd(m, n) = 1. Then

gcd(N, mn) = gcd(N, m) · gcd(N, n).

Proof. Let d = gcd(N, mn).

Suppose pe ∥ d.

Then pe ∥ m or pe ∥ n.

Thus the prime-power divisors of d are divided between m and n

Corollary 5.1. If gcd(m, n) = 1 and N ∈ Z then

gcd(N, mn) = 1 ⇐⇒ gcd(N, m) = 1 and gcd(N, n) = 1.

From this we derive

Theorem 5.3. Euler’s totient function is multiplicative, ie

gcd(m, n) = 1 =⇒ φ(mn) = φ(m)φ(n).

This gives a simple way of computing φ(n).

Proposition 5.2. If n = ∏

1≤i er pei
i ,

where the primes p1, . . . , pr are diﬀerent and each ei/ge1. Then

φ(n) = ∏ pei−1
i (pi − 1).

5–3

Proof. Since φ(n) is multiplicative,

φ(n) = ∏

i φ(pei
i ).

The result now follows from

Lemma 5.1. φ(pe) = pe−1(p − 1).

Proof. The numbers r ∈ [0, p
e) is not coprime to pr if and only if it is divisible
by p, ie r ∈ {0, p, 2p, . . . , pe − p}.

There are [pe/p] = pe−1

such numbers. Hence
 φ(pe) = pe − pe−1 = pe−1(p − 1).

Example: Suppose n = 1000.

φ(1000) = φ(2
35
3)
= φ(2
3)φ(5
3)
= 2
2(2 − 1) 5
2(5 − 1)
= 4 · 1 · 25 · 4
= 400;

there are just 400 numbers coprime to 1000 between 0 and 1000.

5.4 The multiplicative group

Theorem 5.4. If gcd(m, n) = 1 then

(Z/mn)
× = (Z/m)× × (Z/n)×.

Proof. We have seen that the map

r mod mn ↦→ (r mod m, r mod n) : Z/(mn) → Z/(m) × Z/(n)

maps r coprime to mn to pairs (r, s) coprime to m, n respectively. Thus the
subset (Z/mn)× maps to the product of the subsets (Z/m)
× and (Z/n)
×,
from which the result follows.

In eﬀect, this is an algebraic expression of the fact that the totient function
is multiplicative.
 5–4

5.5 Multiple moduli

The Chinese Remainder Theorem extends to more than two moduli.

Proposition 5.3. Suppose n1, n2, . . . , nr are pairwise coprime, ie

i ̸= j =⇒ gcd(ni, nj) = 1;

and suppose we are given remainders a1, a2, . . . , ar moduli n1, n2, . . . , nr, re-
spectively. Then there exists a unique N mod n1n2 · · · nr such that

N ≡ a1 mod n1, N ≡ a2 mod n2, . . . , N ≡ ar mod nr.

Proof. This follows from the same pigeon-hole argument that we used to
establish the Chinese Remainder Theorem.
Or we can prove it by induction on r; for since

gcd(n1n2 · · · ni, ni+1) = 1,

we can add one modulus at a time,
Thus if we have found Ni such that

Ni ≡ a1 mod n1, Ni ≡ a2 mod n2, . . . , Ni ≡ ai mod ni

then by the Chinese Remainder Theorem we can ﬁnd Ni+1 such that

Ni+1 ≡ Ni mod n1n2 · · · ni and Ni+1 ≡ ai+1 mod ni+1

and so

Ni+1 ≡ a1 mod n1, Ni+1 ≡ a2 mod n2, . . . , Ni+1 ≡ ai+1 mod ni+1,

establishing the induction.

Example: Suppose we want to solve the simultaneous congruences

n ≡ 4 mod 5, n ≡ 2 mod 7, n ≡ 1 mod 8.

There are two slightly diﬀerent approaches to the task.
Firstly, we can start by solving the ﬁrst 2 congruences. As is easily seen,
the solution is n ≡ 9 mod 35.

The problem is reduced to two simultaneous congruences:

n ≡ 9 mod 35, n ≡ 1 mod 8,

which we can solve with the help of the Euclidean Algorithm, as before.
Alternatively, we can ﬁnd solutions of the three sets of simultaneous con-
gruences
 n1 ≡ 1 mod 5, n1 ≡ 0 mod 7, n1 ≡ 0 mod 8,
n2 ≡ 0 mod 5, n2 ≡ 1 mod 7, n2 ≡ 0 mod 8,
n3 ≡ 0 mod 5, n3 ≡ 0 mod 7, n3 ≡ 1 mod 8,

5–5

ie
 n1 ≡ 1 mod 5, n1 ≡ 0 mod 56,
n2 ≡ 1 mod 7, n2 ≡ 0 mod 40,
n3 ≡ 1 mod 8, n3 ≡ 0 mod 35,

which we can solve by our previous method. The required solution is then

n = 4n1 + 2n2 + n3,

where the coeﬃcients 4,2,1 are the required residues.

5.6 Multiplicative functions

We have seen that φ(n) is multiplicative. There are several other multiplica-
tive functions that play an important role in number theory, for example:

1. The number d(n) of divisors of n, eg

d(2) = 1, d(12) = 3, d(32) = 5.

2. The sum σ(n) of the divisors of n, eg

σ(2) = 3, σ(12) = 28, σ(32) = 63.

3. The Möbius function

µ(n) =
 {
(−1)
e if n is square-free and has e prime factors,
0 if n has a square factor n = p2m.

4. The function (−1)n.

5. The function
 θ(n) =
 



1 if n ≡ 1 mod 4,
−1 if n ≡ 3 mod 4,
0 if n is even.

5.7 Perfect numbers

Deﬁnition 5.1. We say that n ∈ N is perfect if it is the sum of all its
divisors, except for n itself.

In other words, n is perfect ⇐⇒ σ(n) = 2n.

Theorem 5.5. If M (p) = 2p − 1 is prime then

n = 2
p−1M (p)

is perfect. Moreover, every even perfect number is of this form

5–6

Remark: Euclid showed that every number of this form is perfect; Euler
showed that every even perfect number is of this form.

Proof. Note that σ(n) = n + 1 ⇐⇒ n is prime.

For if n = ab (where a, b > 1) then σ(n) ≥ n + 1 + a.
Also σ(2
e) = 1 + 2 + 22 + · · · + 2e = 2
e+1 − 1.

Thus if n = 2p−1M (p), where P = M (p) is prime, then (since 2
e and
M (p) are coprime)
 σ(n) = σ(2p−1)σ(M (p)
= (2
p − 1)(M (p) + 1)
= (2
p − 1)(2
p)
= 2n.

Conversely, suppose n is an even perfect number. Let n = 2
em, where m
is odd. Then
 σ(n) = σ(2
e)σ(m) = 2n,

ie
 (2
e+1 − 1)σ(m) = 2e+1m.

Thus 2
e+1 − 1 | m, say m = (2
e+1 − 1)x.

Then σ(m) = 2
e+1x = m + x.

But x is a factor of m. So if x is not 1 or m then

σ(m) ≥ m + x + 1.

Hence x = 1 or m If x = m then 2
e+1 − 1 = 1 =⇒ e = 0, which is not
possible since n is even.
It follows that x = 1, so that

m = 2
e+1 − 1 = M (e + 1).

Also σ(m) = m + 1.

Thus m = M (e + 1) is prime (and therefore e + 1 = p is prime), and

n = 2
p−1M (p),

as stated.

But what if n is odd? It is not known if there are any odd perfect numbers.
This is one of the great unsolved problems of mathematics.

5–7
