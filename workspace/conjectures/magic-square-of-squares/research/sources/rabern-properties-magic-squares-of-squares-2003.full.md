<!-- source: https://web.archive.org/web/2023id_/https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj | converted from PDF -->

Rose-Hulman Undergraduate Mathematics Journal Rose-Hulman Undergraduate Mathematics Journal

Volume 4
Issue 1  Article 3

Properties of Magic Squares of Squares Properties of Magic Squares of Squares

Landon W. Rabern
Washington University, landonrabern@hotmail.com

Follow this and additional works at: https://scholar.rose-hulman.edu/rhumj

Recommended Citation Recommended Citation
Rabern, Landon W. (2003) "Properties of Magic Squares of Squares," Rose-Hulman Undergraduate
Mathematics Journal: Vol. 4 : Iss. 1 , Article 3.
Available at: https://scholar.rose-hulman.edu/rhumj/vol4/iss1/3

Properties of Magic Squares of Squares

Landon W. Rabern
1120 NW Harlan St.
Roseburg, OR 97470
landonrabern@hotmail.com

July 2002

A problem due to Martin LaBar is to ﬁnd a 3x3 magic square with 9 distinct
perfect square entries or prove that such a magic square cannot exist (LaBar
[1]). This problem has been tied to various domains including arithmetic pro-
gressions, rational right triangles, and elliptic curves (Robertson [2]). However,
there are some interesting properties that can be derived without ever leaving
the domain of magic squares. I will assume that a solution exists and prove
properties of such a solution. Any solution must have the form

a2 b2 c2

d2 e2 f 2

g2 h2 s2

If M denotes the magic number, then M is the sum of each row, column, or
main diagonal. We know from Gardner [3] that M must equal three times the
middle square, so M = 3e2.

Let t be the greatest common divisor of a2, b2, c2, d2, e2, f 2, g2, h2 and s2. If
t ̸= 1 then t is a square, thus we can divide all entries by t to produce a new
solution with a smaller magic number(M/t). For this reason, it will be assumed
throughout this paper that the entries are relatively prime(t = 1).

Theorem 1.1 All entries of the magic square must be odd.

Proof: Using the fact that the the entries on the left side of the square must
sum to M we get a2 + d2 + g2 = M = 3e2

Hence a2 + g2 = 3e2 − d2, and in particular,

a2 + g2 ≡ 3e2 − d2(mod 4)

With e odd and d even, we have a2 + g2 ≡ 3 − 0 ≡ 3(mod 4). Taking e even
and d odd gives a2 + g2 ≡ 0 − 1 ≡ −1 ≡ 3(mod 4). This is impossible since

1

a2 + g2 ≡ 0 or 2(mod 4). Therefore, e and d must have the same parity. Both
e and d odd gives a2 + g2 ≡ 3 − 1 ≡ 2(mod 4). This implies that a and g must
be odd. Both e and d even gives a2 + g2 ≡ 0 − 0 ≡ 0(mod 4). This implies that
a and g must be even. Thus a ≡ g ≡ e ≡ d(mod 2).

Arguing in a similar fashion for the other sides of the square we ﬁnd that
a ≡ b ≡ c ≡ d ≡ e ≡ f ≡ g ≡ h ≡ s (mod 2). Thus, if any element is even they
are all even, contradicting the fact that the elements are relatively prime. Hence,
all entries are odd. ■

Using the rows, columns and main diagonals that pass through the center of the
square we have

a2 + e2 + s2 = d2 + e2 + f 2 = b2 + e2 + h2 = g2 + e2 + c2 = 3e2

from which it follows that

a2 + s2 = d2 + f 2 = b2 + h2 = g2 + c2 = 2e2

We can now prove the following theorem.

Theorem 1.2 The only prime divisors of e are of the form p ≡ 1(mod 4).

Proof: We just need to show that no prime p ≡ 3(mod 4) can divide e. We
use the fact that the ring of Gaussian integers Z[i] is a Unique Factoriza-
tion Domain(UFD). Factoring the left side of a2 + s2 = 2e2 in Z[i], we get
(a + si)(a − si) = 2e2. Given an odd prime p ∈ Z, then p is prime in Z[i] if and
only if p ≡ 3(mod 4)(See Lemma 1.1 in the Appendix). Thus, assume we have
a p such that p ≡ 3(mod 4) and p | e. Then we must have either p | (a + si)
or p | (a − si). If p | (a + si), then a + si = pk and by complex conjugation
a − si = pk = pk. Hence p | (a − si). But then p must also divide their sum and
diﬀerence: p | 2si and p | 2a. Hence p | s and p | a since p is odd and real.

Similarly, p | d, p | f , p | b, p | h, p | g, and p | c. Hence, p divides every
entry which is impossible. ■

Theorem 1.3 If a prime p ≡ 3, 5(mod 8) divides a non-center entry then p
also divides the center and the other entry in that line.

Proof: Without loss of generality we prove the result for the a, e, s diagonal. We
use the fact that the ring Z[√2] is a UFD. Given an odd prime p ∈ Z, then p is
prime in Z[√2] if and only if p ≡ 3, 5 (mod 8)(See Lemma 1.2 in the Appendix).

Since a2 + s2 = 2e2 implies a2 = −(s2 − 2e2), we can factor the right side
of this equation in Z[√2] to get

a2 = −(s + e√2)(s − e√2).

2

If p | a and p ≡ 3, 5(mod 8), then either p | (s + e√2) or p | (s − e√2). If
p | (s + e√2), then s + e√2 = pk, and by conjugation s − e√2 = pk. Hence
p | (s − e√2). Thus p divides their sum and diﬀerence: p | 2s and p | 2e√2.
Hence p | s and p | e since p is odd and rational. ■

Corollary 1.1 No prime p ≡ 3(mod 8) divides any entry.

Proof: If p divides some non-center entry, then by Theorem 1.3, p divides e. But from
Theorem 1.2, we know that p cannot divide e since p ≡ 3(mod 8) ⇒ p ≡ 3(mod 4). ■

Gardner [3] has shown that given any 3x3 magic square of distinct positive
integers, there are three positive integers x, y, z so that the magic square can be
written in the form
 x + y + 2z x x + 2y + z
x + 2y x + y + z x + 2z
x + z x + 2y + 2z x + y

Looking at this we quickly see that d2 + h2 = 2c2 with similar relations holding
for the other corner entries. This relation can be stated as

Twice the corner entry equals the sum of the two middle-side entries that are
not adjacent to the corner.

We can now prove the following theorem.

Theorem 1.4 No prime p ≡ 5(mod 8) divides a middle-side entry.

Proof: Without loss of generality, let the middle-side entry be d2. Again, we
use the fact that the ring Z[√
2] is a UFD. Given an odd prime p ∈ Z, then p is
prime in Z[√2] if and only if p ≡ 3, 5 (mod 8) (See Lemma 1.2 in the Appendix).

Since d2 + h2 = 2c2 implies d2 = −(h2 − 2c2), we can factor the right side
of this equation in Z[√2] to get

d2 = −(h + c√2)(h − c√2)

If p | d and p ≡ 5(mod 8) then either p | (h + c√2) or p | (h − c√2). If
p | (h + c√2), then h + c√2 = pk and by conjugation h − c√
2 = pk. Hence
p | (h − c√2). Thus p divides their sum and diﬀerence: p | 2h and p | 2c√2.
Hence p | h and p | c since p is odd and rational. Since p | h we can use the
same argument to show that p | f and p | a. But then, since p | f , we can use
the same argument again to show that p | b and p | g. Since p divides both a
and s, p must also divide e. Hence p divides all entries, which is impossible. ■

Theorem 1.5 If a prime p ≡ 3(mod 4) divides a corner entry then it divides
the two middle-side entries that are not adjacent to the corner.

3

Proof: Without loss of generality, let the corner entry be c2. Again, we use the
fact that the ring of Gaussian integers Z[i] is a UFD. Factoring the left side of
d2 + h2 = 2c2 in Z[i], we get (d + hi)(d − hi) = 2c2. If p ≡ 3(mod 4) then p is
prime in Z[i] (See Lemma 1.1 in the Appendix). Thus if p | c and p ≡ 3(mod 4),
then either p | (d + hi) or p | (d − hi). If p | (d + hi), then d + hi = pk, and
by conjugation d − hi = pk. Hence p | (d − hi). Thus p divides their sum and
diﬀerence: p | 2d and p | 2hi. Hence p | d and p | h since p is odd and real. ■

All of these properties taken together severely restrict the possible placement
of primes that are not of the form p ≡ 1(mod 8). Given these restrictions, one
might conjecture that if there is a solution, then all prime divisors of all entries
are of the form p ≡ 1(mod 8). This would greatly reduce the number of possi-
bilities. It would also be interesting to disprove this conjecture by proving the
opposite; namely, that any solution must have at least one entry with prime
divisor p ≡ 5, 7(mod 8).
 APPENDIX

We need to know when an odd prime p ∈ Z is also prime in the extensions Z[i]
and Z[√2]. The following two lemmas answer this question completely.

Lemma 1.1 Given an odd prime p ∈ Z,

p ≡ 3(mod 4) ⇔ p prime in Z[i]

Proof: We use the fact that Z[i] is a UFD.

First, we assume that p ≡ 3(mod 4) and show that p must be prime in Z[i].
If p is composite in Z[i] then p has a factorization p = αβ with N (α) > 1
and N (β) > 1. Taking the norm of both sides we get p2 = N (α)N (β). It is
not possible for p2 to divide N (α) or N (β) since this would imply N (β) = 1,
N (α) = 1 respectively. Hence N (α) = p and N (β) = p. From the former we
get p = N (α) = x2 + y2 for some x, y ∈ Z. Thus p ≡ 0, 1, 2(mod 4) which is a
contradiction. ■

Now we assume that p is prime in Z[i] and show that p ≡ 3(mod 4). If
p ≡ 1(mod 4) then the equation x2 ≡ −1(mod p) has a solution. Hence
x2 + 1 = kp. Factoring in Z[i] we get (x + i)(x − i) = kp. Since p is prime,
it must divide one of the factors and by complex conjugation it divides both.
Therefore p divides their diﬀerence: p | 2i. This is impossible since p is odd and
real (Beukers [4]). ■

Lemma 1.2 Given an odd prime p ∈ Z,

p ≡ 3, 5(mod 8) ⇔ p prime in Z[√2]

4

Proof: We use the fact that Z[√
2] is a UFD.

First, we assume that p ≡ 3, 5(mod 8) and show that p must be prime in Z[√2].
If p composite in Z[√2] then p has a factorization p = αβ with |N (α)| > 1
and |N (β)| > 1. Taking the norm of both sides we get p2 = N (α)N (β). It is
not possible for p2 to divide N (α) or N (β) since this would imply |N (β)| = 1,
|N (α)| = 1 respectively. Hence |N (α)| = p and |N (β)| = p. From the former we
get p=±N (α) = ±(x2 − 2y2) for some x, y ∈ Z. Thus p ≡ 0, 1, 2, 6, 7 (mod 8)
which is a contradiction. ■

Now we assume that p is prime in Z[√2] and show that p ≡ 3, 5(mod 8).
If p ≡ 1, 7(mod 8) then the equation x2 ≡ 2(mod p) has a solution. Hence
x2 − 2 = kp. Factoring in Z[√2] we get (x + √2)(x − √2) = kp. Since p is
prime, it must divide one of the factors and by conjugation it divides both.
Therefore p divides their diﬀerence: p | 2√2. This is impossible since p is odd
and rational. ■

REFERENCES
1. Martin LaBar, Problem 270, College Math Journal,15, 1984, p. 69.
2. John P. Robertson, Magic Squares of Squares, Mathematics Magazine,
Vol. 69, No. 4, Oct. 1996, pp. 289-293
3. Martin Gardner, Riddles of the Sphinx, Mathematical Association of
America, 1987, pp. 136-137.
4. Frits Beukers, Elementary Number Theory, Lecture Notes for a course
titled ”Elementaire Getaltheorie” at Utrecht University, The Netherlands,
Sept. 2001, p. 55. Unpublished.
 5
