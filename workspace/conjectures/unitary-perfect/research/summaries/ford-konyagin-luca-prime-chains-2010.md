> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/ford-konyagin-luca-prime-chains-2010.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/0904.0473 | converted from PDF -->

## What it claims

ABSTRACT. Prime chains are sequences p1, . . . , pk of primes for which pj+1 ≡ 1 (mod pj) for
each j. We introduce three new methods for counting long prime chains. The ﬁrst is used to show
that N (x; p) = Oε(x1+ε), where N (x; p) is the number of chains with p1 = p and pk ⩽ px. The
second method is used to show that the number of prime chains ending at p is ≍ log p for most
p. The third method produces the ﬁrst nontrivial upper bounds on H(p), the length of the longest
chain with pk = p, valid for almost all p. As a consequence, we also settle a conjecture of Erd˝os,
Granville, Pomerance and Spiro from 1990. A probabilistic model of H(p), based on the theory
of branching random walks, is introduced and analyzed. The model suggests that for most p ⩽ x,
H(p) stays very close to e log log x.
 1. INTRODUCTION

1.1. For positive integers a and b, write a ≺ b if b ≡ 1 (mod a). We are interested in properties
of prime chains p1 ≺ p2 ≺ · · · ≺ pk, e.g. 3 ≺ 7 ≺ 29 ≺ 59. Prime chains are multiplicative
analogs of the well-studied additive prime k-tuples (sequences p1 < · · · < pk of primes…

## Statements it makes

Theorem 1. For p ⩾ 2 and x ⩾ 20, we have the effective estimate

Theorem 1 has applications to problems which, at ﬁrst glance, have nothing to do with prime
chains. First, it is a crucial tool in the recent proof by Ford, Luca and Pomerance [22] that the
equation φ(a) = σ(b) has inﬁnitely many solutions, settling a well-known 50-year old prob-
lem of Erd˝os. In [21], Theorem 1 is used to show that for some effective q0, if π(p3a; pa, 1) −
π(p3a; pa+1, 1) ⩾ 113p 7a−3
4 / log(pa+1) for all prime powers pa ∈ (10
10, q0], then for every positive
integer n, there is another positive integer m with λ(n) = λ(m). This nearly settles a conjecture
from [5], the analog for λ of the famous Carmichael Conjecture for φ.

Theorem 1 is nearly best possible, since N (x; p) ⩾ N2(x; p) = π(px; p, 1), which is expected
to be ≫ x/(log px) unless x is very small relative to p.

Conjecture 1. We have N (x; p) ≪ x.

Conjecture 1 is easy to prove when p is bounded. Using f (2) = 1 and the recursive formula

Theorem 2. (i) We have f (p) ⩾ 0.378 log p for almost all primes p. Hence, N (x) ≫ x.

Conjecture 1 implies that for all ε > 0 and prime q > (log x)1+ε, for most p ⩽ x there is no
prime chain q ≺ · · · ≺ p. This gives, conditionally, the ﬁrst part of [19, Conjecture 1]. By contrast,
the proof of Theorem 4.5 of [19] implies that if q ⩽ (log x)
c, for some small constant c > 0, then
for almost all primes p ⩽ x, there is a prime chain q ≺ · · · ≺ p.

Theorem 3. (a) If (1.1) holds with Q = xθ and R = o(x/ log x), then for any c < 1
e−1−log θ ,
H(p) > c log2 p for almost all primes p;
(b) If (1.1) holds with Q = xθ and R = x(log x)−A for every A > 1, then for every c < 1
− log θ ,
there is a K so that H(p) > c log2 p for ≫ x/(log x)
K primes p ⩽ x. Consequently, Λ ⩾ 1
− log θ .

Corollary 1. EH implies that for every c < e, H(p) > c log2 p for almost all p.

Theorem 4. We have H(p) ⩽ (log p)
0.9503 for almost all p.

Theorem 5. For every ε > 0 and δ > 0, there is an integer k so that for large x and at least
(1 − δ)x integers n ⩽ x, P +(φk(n)) ⩽ xε.

Conjecture 2. H(p) has normal order e log2 p.

Conjecture 3. H(p) = e log2 p − 3
2 log3 p + E(p), where for some ﬁxed c, c
′ > 0 and any z ⩾ 0,
the number of p ⩽ x for which E(p) ⩾ z is ≫ e−c′zπ(x) and ≪ e−czπ(x), and E(p) ⩽ −z for
O(exp{−e
cz}π(x)) primes ⩽ x.

Theorem 6. Suppose g and h are increasing, 0 ⩽ g(x) ⩽ h(x), h(x2) − h(x) ⩽ K and g(x2) −
g(x) ⩽ K for x ⩾ 1. Suppose, for large x, that H(p) ⩾ h(p) for at least cπ(x) primes ⩽ x. Then
H(p) ⩾ h(p) − g(p) for all primes p ⩽ x with at most O(π(x) exp{− c log 2
K g(x)}) exceptions.

Conjecture 4. For each k ⩾ 3, there are inﬁnitely many prime k-tuples (p1, . . . , pk) where, for
some m, pj+1 = mpj + 1 for 1 ⩽ j ⩽ k − 1.

Lemma 5.1. There is a positive constant δ so that the following holds. Let a1, . . . , ak be positive
integers, let b1, . . . , bk be integers with (aj, bj)…


*[further statements in the full text]*

*[digest of a 63459 character source; every section, statement, and proof in full at `research/sources/ford-konyagin-luca-prime-chains-2010.full.md`]*
