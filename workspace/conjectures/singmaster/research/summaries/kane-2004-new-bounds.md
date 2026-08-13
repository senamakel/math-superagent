> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kane-2004-new-bounds.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://cseweb.ucsd.edu/~dakane/combinations.pdf | converted from PDF -->

## What it claims

Proof of Lemma 2.1. We proceed by induction on n. The case of n = 1 is Rolle’s Theorem.
Given the statement of Lemma 2.1 for n − 1, if there exists such an F with n + 1 zeroes,
x1 < x2 < ... < xn+1, then by Rolle’s theorem, there exist points yi ∈ (xi, xi+1) (1 ≤ i ≤ n)
so that F ′(yi) = 0. Then since F ′ has at least n roots, by the induction hypothesis there
exists a y with x1 < y1 < y < yn < xn+1, and F (n)(y) = (F ′)
(n−1)(y) = 0. □

If we let F (x) equal f (x) − p(x) where p(x) is a degree n polynomial, we get that

Corollary 2.1. If f (x) is an inﬁnitely diﬀerentiable function and if p(x) is a polynomial of
degree n so that f (x) = p(x) for x = x1, x2, ..., xn+1 where x1 < x2 < ... < xn+1, then there
exists a y ∈ (x1, xn+1) so that f (n)(y) = p(n)(y).

3. approximation of the terms in binomial coefficients equal to t

Suppose that for n ≥ 2m ( n
m
 ) = t.

BINOMIAL REPRESENTATIONS 3

We can take logs of both sides, and then we have by (2.1) that

log t + log(m!) =

log(n!) − log((n − m)!)

= (n + 1
2
 ) log(n) − n + 1
12n − (n − m + 1
2
 ) log(n − m) + (n − m) − 1
12(n − m) +…

## Statements it makes

Theorem 1. With N (t) deﬁned above,

Lemma 2.1. If F (x) : R → R is an inﬁnitely diﬀerentiable function and if F (x) = 0 for
x = x1, x2, ..., xn+1 (where x1 < x2 < ... < xn+1), then F (n)(y) = 0 for some y ∈ (x1, xn+1).

Corollary 2.1. If f (x) is an inﬁnitely diﬀerentiable function and if p(x) is a polynomial of
degree n so that f (x) = p(x) for x = x1, x2, ..., xn+1 where x1 < x2 < ... < xn+1, then there
exists a y ∈ (x1, xn+1) so that f (n)(y) = p(n)(y).

*[digest of a 11991 character source; every section, statement, and proof in full at `research/sources/kane-2004-new-bounds.full.md`]*
