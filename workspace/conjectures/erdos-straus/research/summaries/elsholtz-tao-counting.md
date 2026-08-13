> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/elsholtz-tao-counting.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://terrytao.files.wordpress.com/2011/07/egyptian-count13.pdf | converted from PDF -->

## What it claims

Abstract. For any positive integer n, let f (n) denote the number of solutions to the Diophantine
equation 4
n = 1
x + 1
y + 1
z with x, y, z positive integers. The Erd˝os-Straus conjecture asserts that
f (n) > 0 for every n ⩾ 2. To solve this conjecture, it suﬃces without loss of generality to consider
the case when n is a prime p. In this paper we consider the question of bounding the sum ∑p<N f (p)
asymptotically as N → ∞, where p ranges over primes. Our main result establishes the asymptotic
upper and lower bounds
 N log2 N ≪ ∑

p⩽N f (p) ≪ N log2 N log log N.

In particular, f (p) = Oδ(log3 p log log p) for a subset of primes of density δ arbitrarily close to 1. Also,
for a subset of the primes with density 1 the following lower bound holds: f (p) ≫ (log p)0.549. These
upper and lower bounds show that a typical prime has a small number of solutions to the Erd˝os-
Straus Diophantine equation; small, when compared with other additive problems, like Waring’s
problem. We establish several more results on f and related quantities, for instance the bound

f (p) ≪ p 3
5 +O( 1
log log…

## Statements it makes

Theorem 1.1 (Average value of fI, fII). For all suﬃciently large N , one has the bounds

Proposition 1.4 (Average value of τ (kab2 + 1)). For any A, B > 1, and any positive integer k ≪
(AB)
O(1), one has X

Proposition 1.6 (Vanishing). For any odd perfect square n, we have fI(n) = fII(n) = 0.

Proposition 1.7 (Upper bounds). For any n ∈ N, one has

Theorem 1.8 (Lower bounds). For inﬁnitely many n, one has

Proposition 1.9 (Solvable congruences). Let q mod r be a primitive residue class. If this class is
Type I solvable by polynomials, then all suﬃciently large primes in this class belong to one of the
following sets:
• {n = −f mod 4ad}, where a, d, f ∈ N are such that f |4a2d + 1. [43]
• {n = −f mod 4ac} ∩ {n = − c
a mod f }, where a, c, f ∈ N are such that (4ac, f ) = 1.
• {n = −f mod 4cd} ∩ {n2 = −4c
2d mod f }, where c, d, f ∈ N are such that (4cd, f ) = 1.
• {n = − 1
e mod 4ab}, where a, b, e ∈ N are such that e|a + b and (e, 4ab) = 1. [1], [52]
Conversely, any residue class in one of the above four sets is solvable by polynomials.
Similarly, q mod r is Type II solvable by polynomials if…

Theorem 1.11. Let m > k ⩾ 3 be ﬁxed. Then, for N suﬃciently large, one has

Corollary 1.13. Let k ⩾ 3. The number of integer points of the following generalization of Cayley’s
cubic surface,
 0 =
 kX
 i=0
 1
ti ,

Proposition 2.1 (Description of Type I solutions). Let n ∈ N, and let (x, y, z) be a Type I solution.
Then there exists a unique (a, b, c, d, e, f ) ∈ N6 ∩ ΣI
n with abcd coprime to n and a, b, c having no
common factor, such that πI
n(a, b, c, d, e, f ) = (x, y, z).

Proposition 2.2. Let n be a natural number. Then the following are equivalent:

Proposition 2.5 (Description of Type II solutions). Let n ∈ N, and let (x, y, z) be a Type II solution.
Then there exists a unique (a, b, c, d, e, f ) ∈ N6 ∩ΣII
n with abd coprime to n and a, b, c having no common
factor, such that πI
n(a, b, c, d, e, f ) = (x, y, z).

Proposition 2.6. Let n be a natural number. Then the following are equivalent:

Lemma 2.7. Let n ∈ N, and suppose that (x, y, z) = πI(a, b, c, d, e, f ) is a Type I solution such that
y ⩽ z. Then
 a ⩽ b
1
4 n < acd ⩽ 3
4 n

Proposition 2.10. Let m
p = 1
x + 1
y + 1
z where m > 3, p is a prime not dividing m, and x, y, z are
natural numbers. Then none of x, y, z are divisible by p.

Theorem 7.1 (Erd˝os-type bound). Let N > 1, let P be a polynomial with degree D and coeﬃcients
being non-negative integers of magnitude at most N l. For any natural number m, let ρ(m) be the
number of roots of P mod m in Z/mZ, and suppose one has the bound

Lemma 7.3. Let C ′ be a ﬁxed constant. For all but at most O(N log−C′ N ) values of n in the range
1 ⩽ n ⩽ N , either (7.7) holds, or one has

Corollary 7.4. If a, b, N are natural numbers with a, b ≪ N O(1), then
X

Proposition 7.5 (Average value of τ3(ab + 1)). For any A, B > 1, one has

Proposition 7.6…

Lemma…


*[further statements in the full text]*

*[digest of a 112215 character source; every section, statement, and proof in full at `research/sources/elsholtz-tao-counting.full.md`]*
