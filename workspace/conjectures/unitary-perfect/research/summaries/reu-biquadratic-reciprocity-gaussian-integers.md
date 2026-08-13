> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/reu-biquadratic-reciprocity-gaussian-integers.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://math.uchicago.edu/~may/REU2021/REUPapers/Xu,Nancy.pdf | converted from PDF -->

## What it claims

Abstract. This paper surveys four of the early reciprocity laws. We start
with a discussion of quadratic reciprocity, which we will prove using the split-
ting of primes in algebraic number ﬁelds. We then introduce Gauss and Jacobi
sums before using them to prove cubic, biquadratic, and Eisenstein reciprocity.

Contents

1. Introduction 1
2. Quadratic Reciprocity 2
3. Gauss and Jacobi Sums 8
4. Cubic Reciprocity 10
5. Biquadratic Reciprocity 14
6. Eisenstein Reciprocity 18
Acknowledgments 24
References 24

1. Introduction

For distinct primes p, q, reciprocity laws turn the question of whether q is an nth
power modulo p into the question of whether p is an nth power modulo q, hence
the name ”reciprocity.” The case n = 2 is quadratic reciprocity. The cases n = 3
and n = 4 are cubic and biquadratic reciprocity, respectively, where we move from
the familiar Z to Z[ζ3] or Z[i]. The Eisenstein reciprocity covers the case n = l for
an odd prime l in the cyclotomic ﬁeld Z[ζl].
Quadratc reciprocity can be used to solve the problem of whether a prime can
be expressed in the form x2 + ny2,…

1

## Statements it makes

Proposition 2.2. Let a, b, p ∈ Z, where p is a prime. We have the following
properties:

Proposition 2.2 (2) is a particularly nice property, since using quadratic reci-
procity it is possible to determine when an arbitrary integer is a square modulo p
by decomposing it into primes and using this multiplicative property. The law of
quadratic reciprocity is as follows:

Theorem 2.3. For odd primes p, q ∈ Z,
(
p
q
)(q
p
) = (−1) p−1
2 · q−1
2 .

Proposition 2.6. For a ring Q[α], let f be the monic irreducible polynomial for α
over Q and α1, . . . , αn be the conjugates of α. Then

Proposition 2.7. Let p ∈ Z be a prime, and deﬁne p∗ = (−1) p−1
2 p. Then √p∗ ∈
Q[ζp].

Corollary 2.8. The unique quadratic subﬁeld of Q[ζp] is Q[√p∗].

Proposition 2.13. Let Q, Q
′ ⊂ OL be prime ideals lying over the prime ideal
P ⊂ OK. Then σ(Q) = Q
′ for some σ ∈ G(L/K).

Proposition 2.14. Let n = [L : K], and write P OL = Q
e1
1 Q
e2
2 . . . Q
eg
g , where
Qi ∈ OL is a prime ideal for 1 ≤ i ≤ g and Qi = Qj if and only if i = j. Then
e1 = e2 = . . . = eg and f1 = f2 = . . . = fg. Let e and f denote these common
values. Then gef = n.

Proposition 2.14 is particularly useful in characterizing primes when n is small,
as we will see in Sections 4 and 5. For now, if we want to show that every prime
splits completely in an intermediate ﬁeld K ′, it is enough for us to prove that
[K : K ′] = g and e = f = 1.
For groups H, G, we write H ⊂ G if H is an arbitrary subgroup of G and H ▹ G
if H is a normal subgroup of G.

Proposition 2.16. Let g be the number of distinct prime ideals in the decomposi-
tion of P in OL. Let QD ∈ D(Q|P ) be a prime ideal over P . Then [LD : K] = g
and e(QD|P ) = f (QD|P ) = 1.

Corollary 2.17. If D ▹ G, P splits into g distinct primes in OLD .

Proposition 2.18. Let P ′ ⊂ OK be a prime lying over P . Then LD is the largest
intermediate ﬁeld K ′ such that e(P ′|P ) = f (P ′|P ) = 1.

Corollary 2.19. Let K ′ be a ﬁeld such that K ⊂ K ′ ⊂ L. If D ▹ G, then P splits
completely in K if and only if K ′ ⊂ LD.

Proposition 2.20. Let p ∈ Z be an odd prime. The splitting behavior of p in K
is as follows:
(1) If p ∤ d and d is a square modulo p, then (p) = P P ′, where P ̸= P ′.
(2) If p ∤ d and d is not a square modulo p, then (p) = P .
(3) If p|d, then (p) = P 2.
Here P and P ′ are prime ideals in OK.

Proposition 2.21. Suppose p = 2.
(1) If m ≡ 1 (mod 8), then (2) = P P ′, where P ̸= P ′.
(2) If m ≡ 5 (mod 8), then (2) = P .
(3) If m ≡ 3 (mod 4), Then (2) = P 2.

Proposition 2.22. Let p, m ∈ Z be such that p is a prime and and p ∤ m. Let f
be the order of p modulo m. Then (p) = P1P2 . . . Pg in OQ[ζp], where the Pis are
distinct prime ideals with f (Pi|P ) = f and g = φ(m)/f .

Proposition 2.23. Let p, q ∈ Z be odd primes such that p ̸= q. For a divisor d of
p − 1, q is a dth power modulo p if and only if q splits completely in Fd.

Proposition 3.2. Let χ be a…


*[further statements in the full text]*

*[digest of a 54536 character source; every section, statement, and proof in full at `research/sources/reu-biquadratic-reciprocity-gaussian-integers.full.md`]*
