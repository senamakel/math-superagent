<!-- source: https://zenodo.org/records/19403738/files/aa42.pdf | converted from PDF -->

#A42 INTEGERS 26 (2026)

THE ERD ˝OS-STRAUS CONJECTURE AND THE STRUCTURE OF
PRIMES

Marc Chamberland
Department of Mathematics, Grinnell College, Grinnell, Iowa
chamberl@grinnell.edu

Received: 10/22/25, Accepted: 2/25/26, Published: 4/3/26

Abstract
The famous Erd˝os-Straus Conjecture states that every fraction 4/n, where n ≥ 2,
can be written as the sum of three unit fractions. This paper shows that if p is a
prime, then 4/p can be written as the sum of three unit fractions, where exactly
two of the denominators are multiples of p, if and only if p = qr − 4s1s2, where
q ≡ 3 mod 4 and both s1 and s2 are divisors of (q + 1)/4. It is conjectured that all
primes can be written in this form.

1. Introduction

The following unsolved number theory problem has attracted attention for decades.

Conjecture 1. (Erd˝os-Straus) For every integer n ≥ 2, we can write

4
n = 1
a + 1
b + 1
c (1)

for some a, b, c ∈ Z+.

Dating back to 1948, the conjecture has been verified [6] for all n ≤ 1017. Obvi-
ously we can write 4/n as the sum of four unit fractions (a greedy algorithm usually
produces four distinct unit fractions), but the conjecture asserts that three unit
fractions are always sufficient.
A well-studied approach has been to consider various residue classes where the
desired decomposition is possible. For example, the equation

4
n = 1
n + 1
(n + 1)/3 + 1
n(n + 1)/3

DOI: 10.5281/zenodo.19403738

INTEGERS: 26 (2026) 2

yields a solution to (1) whenever n ≡ 2 mod 3. This can be made explicit by writing
n = 3k + 2 to produce
4
3k + 2 = 1
3k + 2 + 1
k + 1 + 1
(k + 1)(3k + 2) .

Formulas of this type can be constructed to cover many residue classes, leaving one
to wonder whether covering all n ≥ 2 is possible. Indeed, Webb [8] used sieving
methods to show that 4/n can be written in the form (1) for almost all n. Covering
all the positive integers with polynomial identities, however, is impossible, as argued
by Mordell [4, pp.287–290]. A result of Schinzel [7] makes this explicit: the equation

4
ax + b = 1
F1(x) + 1
F2(x) + 1
F3(x)

has no solution in polynomials F1, F2, F3 with integer coefficients and positive lead-
ing coefficients if b is a quadratic residue modulo a.
The work of Elsholtz and Tao [3] also points to the limitations of the covering
approach. For a given n, we say (a, b, c) is a Type I solution of Equation (1) if
exactly one of the values is divisible by n, and a Type II solution if exactly two of
the values are divisible by n. They showed that if n is odd, then n
2 has neither Type
I nor Type II solutions. This does not mean that the Erd˝os-Straus Conjecture is
false; if 4/n has a solution, then multiplying each denominator by n gives a solution
for 4/n2. These limitations simply point to the need for a different approach.
Since 4
mn = 1
m · 4
n ,

it is well-known that it suffices to restrict our attention to 4/p for all prime numbers
p. It has been shown [1, 3] that if p is prime and Equation (1) is satisfied for 4/p
with a ≤ b ≤ c, then p ∤ a and p|c. Numerical evidence suggests that for all odd
primes p, 4/p has both Type I and Type II solutions. The main result of this
paper asserts that 4/p has a Type II solution if and only if p can be expressed in a
particular, simple form.

Theorem 1. Let p be a prime number. Then there exist a, b, c ∈ Z+ such that
a ≤ b ≤ c, p ∤ a, p is a divisor of both b and c, and

4
p = 1
a + 1
b + 1
c

if and only if p = qr − 4s1s2 (2)

for some q, r, s1, s2 ∈ Z
+ such that q ≡ 3 mod 4 and both s1 and s2 are divisors of
(q + 1)/4.

Other results connecting the structure of primes to the Erd˝os-Straus Conjecture
can be found in Bradford [2]. Section 2 offers a proof of the Theorem. Section 3
explores the structure of primes in light of the Theorem.

INTEGERS: 26 (2026) 3

2. Proof of the Theorem

To prove one direction of the theorem, we will use a non-obvious result due to
Bradford [1]: if 4
p = 1
a + 1
b + 1
c ,

where p is prime and a ≤ b ≤ c, then

c = abp
gcd(b, p) gcd(ab, a + b) .

For Type II solutions, this simplifies to

c = ab
gcd(ab, a + b) . (3)

Proof of Theorem 1. To settle the forward direction of the proof, assume that we
are given a, b, c ∈ Z
+ such that a ≤ b ≤ c, p ∤ a, p divides both b and c, and

4
p = 1
a + 1
b + 1
c .

Define q = 4b
p − 1, r = 4a − p,

s1 = gcd ( ab
gcd(a, b) , a + b
gcd(a, b)
 ) , s2 = gcd(a, b).

The conditions on a, b, c guarantee that q, r, s1, s2 ∈ Z
+ and q ≡ 3 mod 4. We also
have (q + 1)/4 = b/p, and since gcd(a, b) = gcd(a, b/p) is a divisor of b/p, this yields
s2|(q + 1)/4.
Showing s1|(q + 1)/4 is more involved. First note that we can write a = s2x and
b = s2y for some x, y ∈ Z
+ with gcd(x, y) = 1, thus implying s1 = gcd(s2xy, x + y).
If t is a prime such that t
k|s1 for some k ∈ Z
+, then t|(x + y). This forces t ∤ x
and t ∤ y, hence tk|s2. This argument applies to all primes t, hence s1|s2. Since
s2|(q + 1)/4, we have s1|(q + 1)/4.
Lastly, assembling these components together and using (3) yields

qr − 4s1s2 = ( 4b
p − 1) · (4a − p) − 4 gcd ( ab
gcd(a, b) , a + b
gcd(a, b)
 ) · gcd(a, b)

= 16ab
p − 4a − 4b + p − 4 gcd(ab, a + b)

= p + 4ab ( 1
a + 1
b + 1
c
 ) − 4a − 4b − 4 gcd(ab, a + b)

= p + 4 ( ab
c − gcd(ab, a + b))

= p.

INTEGERS: 26 (2026) 4

To settle the reverse direction of the proof, assume that p = qr − 4s1s2 for some
q, r, s1, s2 ∈ Z
+ such that q ≡ 3 mod 4 and both s1 and s2 are divisors of (q + 1)/4.
The following equation holds for all scalars q, r, s1, s2 when the denominators are
non-zero:
 4
qr − 4s1s2 = 1
r ( q+1
4 ) − s1s2 + 1
( q+1
4 ) · (qr − 4s1s2) (4)

+ s1s2
( q+1
4 ) · (r ( q+1
4 ) − s1s2) · (qr − 4s1s2) .

For this direction of the proof, the conditions imply (q + 1)/4 ∈ Z+ and the three
denominators of Equation (4) are positive integers. Since both s1 and s2 divide
(q + 1)/4, dividing the top and bottom of the last fraction by s1s2 and simplifying
implies that the right side of (4) is the sum of three unit fractions. The last two
unit fractions have p = qr − 4s1s2 in their denominators, thus implying

a = r ( q + 1
4
 ) − s1s2

and b and c take the values ( q + 1
4
 ) · (qr − 4s1s2) (5)

and 1
s1
 ( q + 1
4
 ) · ( r
s2
 ( q + 1
4
 ) − s1
) · (qr − 4s1s2), (6)

arranged so that b ≤ c.

Note that it is unclear which of the expressions (5) or (6) is larger. For exam-
ple, the possible Type II representations of 4/41 using Equation (4), omitting the
swapping of s1 and s2, are listed in Table 1.

3. The Structure of Primes

The theorem behooves us to determine when a prime p takes the form p = qr−4s1s2.
Indeed, the extensive testing on the Erd˝os-Straus Conjecture suggests the following
claim.

Conjecture 2. (Prime Representation Conjecture) Every prime p can be written
in the form p = qr − 4s1s2 for some q, r, s1, s2 ∈ Z+ such that q ≡ 3 mod 4 and
both s1 and s2 are divisors of (q + 1)/4.

INTEGERS: 26 (2026) 5

q r s1 s2 representation of 4/41

3 15 1 1 1
14 + 1
41 + 1
574

7 7 1 2 1
12 + 1
82 + 1
492

11 7 3 3 1
12 + 1
123 + 1
164

15 3 1 1 1
11 + 1
164 + 1
1804

15 7 4 4 1
12 + 1
164 + 1
123

47 7 6 12 1
12 + 1
492 + 1
82

Table 1: Type II representations of 4/41.

The trivial case p = 2 is settled with 2 = 3 · 2 − 4 · 1 · 1, corresponding, via
Equation (4), to 4/2 = 1/1 + 1/2 + 1/2. More interesting is when p ≡ 3 mod 4,
which can be settled in at least two ways:

p = (2p + 1) · 1 − 4 · 1 · ( p + 1
4
 ) ⇔ 4
p = 1
( p+1
4 ) + 1
( p+1
2 ) p + 1
( p+1
2 ) p

and
 p = (p + 4) · 1 − 4 · 1 · 1 ⇔ 4
p = 1
( p+1
4 ) + 1
( p+5
4 ) p + 1
( p+1
4 ) ( p+5
4 ) p .

For any prime p, the divisibility conditions required for Equation (2) are auto-
matically met when s1 and s2 are restricted to the values 1 and (q + 1)/4. Since r
is unrestricted, it can be shifted, if necessary, to r′:

q · r − 4 · 1 · 1 = q · r − 4, (7)

q · r − 4 · 1 · ( q + 1
4
 ) = q · r′ − 1, (8)

q · r − 4 · ( q + 1
4
 ) · ( q + 1
4
 ) = q · r′ − ( q + 1
4
 ) . (9)

Numerical exploration suggests that most primes can be represented with one of
these three forms. The corresponding forms for Equation (4) (without ordering b
and c) follow:

4
qr − 4 = 1
r ( q+1
4 ) − 1 + 1
( q+1
4 ) · (qr − 4) + 1
( q+1
4 ) · (r ( q+1
4 ) − 1) · (qr − 4) ,

4
qr − 1 = 1
r ( q+1
4 ) + 1
( q+1
4 ) · (qr − 1) + 1
r ( q+1
4 ) · (qr − 1) ,

4
qr − q+1
4 = 1
r ( q+1
4 ) + 1
( q+1
4 ) · (qr − q+1
4 ) + 1
r (qr − q+1
4 ) .

INTEGERS: 26 (2026) 6

q = 3 3r − 1
q = 7 7r − 1
7r − 2
7r − 4
q = 11 11r − 1
11r − 3
11r − 4
q = 15 15r − 1
15r − 2
15r − 4
15r − 8
 q = 19 19r − 1
19r − 4
19r − 5
q = 23 23r − 1
23r − 2
23r − 3
23r − 4
23r − 6
23r − 8
23r − 12
23r − 13
23r − 16

Table 2: Residue classes covered for q ≤ 23.

These forms are essentially those listed in [5, p.207] and [9].
Not all primes, however, fit one of the forms (7)-(9). The prime p = 193 is such
an example, but it can be written in four other ways (not counting swapping s1 and
s2), each with 1 < s1 < (q + 1)/4 and s2 = (q + 1)/4:

193 = 15 · 15 − 4 · 2 · 4 = 39 · 7 − 4 · 2 · 10 = 99 · 7 − 4 · 5 · 25 = 103 · 15 − 4 · 13 · 26.

For most values of q ≡ 3 mod 4, the number (q + 1)/4 is not prime, so other
choices of s1 and s2 may produce other congruence classes besides Equations (7)–
(9). Table 2 lists these congruence classes covered for q ≤ 23, where any shifted
values of r are simply written as r. The prime p = 211 cannot be written with
q ≤ 23, but one has 211 = 43 · 5 − 4 · 1 · 1. Further computation finds that the prime
p = 1009 is the smallest prime where s1 ≥ 3 and s2 ≥ 3 are necessary; one solution
is 1009 = 23 · 47 − 4 · 3 · 6.

References

[1] K. Bradford, A note on the Erd˝os-Straus conjecture, Integers 21 (2021), # A24, 10pp.

[2] K. Bradford, Elementary patterns from the Erd˝os-Straus conjecture, Integers 25 (2025), #
A54, 10pp.

[3] C. Elsholtz and T. Tao, Counting the number of solutions to the Erd˝os–Straus equation on
unit fractions, J. Aust. Math. Soc., 94 (1) (2013), 50–105.

[4] L.J. Mordell. Diophantine Equations, Academic Press, New York, 1967.

[5] P. Pollack. Not Always Buried Deep. A Second Course in Elementary Number Theory, AMS,
Providence, 2009.

[6] S. Salez, The Erd˝os-Straus conjecture New modular equations and checking up to N = 1017,
preprint, arXiv:1406.6307.

INTEGERS: 26 (2026) 7

[7] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Approx.
Comment. Math., 28 (2000), 187–194.

[8] W.A. Webb, On 4/n = 1/x1 + 1/x2 + 1/x3, Proc. Amer. Math. Soc., 25 (3) (1970), 578—584.

[9] X.Q. Yang, A Note on 4/n = 1/x+1/y +1/z, Proc. Amer. Math. Soc., 85 (4) (1982), 496–498.
