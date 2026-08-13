> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/conrad-wieferich-primes.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/wieferich-primes.pdf | converted from PDF -->

## What it claims

Unlike the congruence in Fermat’s little theorem, (1.1) usually does not hold. When (1.1)
holds, p is called a Wieferich prime to base a.
In Section 2 we’ll present examples and heuristics related to Wieferich primes. The next
three sections give diﬀerent settings where Wieferich primes appear: Fermat’s last theorem
in Section 3 (this is how Wieferich’s name got associated to (1.1)), Catalan’s conjecture in
Section 4, and Fermat and Mersenne numbers in Section 5.
1

2. Numerical data

The only known Wieferich primes to base 2 and 1093 and 3511: they are prime and

2
1092 ≡ 1 mod 10932, 2
3510 ≡ 1 mod 35112.

These were found by Meissner [5] in 1913 and Beegner [1] in 1922. The known Wieferich
primes to a squarefree base a ≤ 10 are in Table 1. Searches for Wieferich primes have been
carried out for p < 1.25 · 1015 when a = 2 [4] and for p < 232 ≈ 109.63 when 3 ≤ a < 100 [7].
Wieferich primes to a ﬁxed base appear to be quite rare numerically, and for some bases
none are known, e.g., no Wieferich primes to base 21 or 29 have been found.

a Known Wieferich primes to base a
2 1093, 3511…

## Statements it makes

Theorem 3.1. If Case I for exponent p has a counterexample, then 2p−1 ≡ 1 mod p2.

Theorem 3.2. If Case I for exponent p has a counterexample, then 3p−1 ≡ 1 mod p2.

Theorem 5.1. If Fn is divisible by p2 where p is prime then 2p−1 ≡ 1 mod p2.

Theorem 5.2. For prime numbers p and q, the following conditions are equivalent and
each implies q | (p − 1):
(i) p2 | (2q − 1),
(ii) p | (2q − 1) and 2p−1 ≡ 1 mod p2.

Corollary 5.4. If 2q − 1 is not squarefree for inﬁnitely many primes q then there are
inﬁnitely many Wieferich primes to base 2.

Theorem 5.5. If a ≥ 2 and q is a prime, then q2 ∤ (aq − 1)/(a − 1) unless q = 2 and
a ≡ 3 mod 4.

Lemma 5.6. For a ≥ 2 and a prime q, gcd(a − 1, (aq − 1)/(a − 1)) is 1 or q.

Theorem 5.7. Let a ≥ 2. For distinct primes p and q, the following conditions are equiv-
alent 6 and each implies q | (p − 1):
(i) p2 | (aq − 1)/(a − 1),
(ii) p | (aq − 1)/(a − 1) and ap−1 ≡ 1 mod p2.

*[digest of a 16967 character source; every section, statement, and proof in full at `research/sources/conrad-wieferich-primes.full.md`]*
