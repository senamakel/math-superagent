> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://members.loria.fr/PZimmermann/papers/squares.pdf | converted from PDF -->

## What it claims

All rows and columns and the two main diagonals sum up to 8515. Contrary to classical
magic squares ﬁlled with consecutive integers, the only rule is that all elements are squares
of diﬀerent positive integers. We also require the magic square to be primitive, i.e., the gcd
of all elements is one (indeed, multiplying all elements by some integer k2 keeps the equality
between sums). In 1996, Martin Gardner asked whether there exists a 3 × 3 magic square
ﬁlled with squares, and oﬀered a $100 prize to the ﬁrst discoverer. Euler’s method, and a
detailed history of this problem is presented in [2].
Lee Sallows found in 1997 the following near miss:

127
2 46
2 58
2

2
2 113
2 94
2

74
2 82
2 97
2

where all rows and columns and main diagonals sum up to 21609, except the descending
diagonal whose sum is 38307. Christian Boyer notices in [2] that Sallows’ solution is part of
a family proposed by Lucas in 1876.
Duncan Buell shows in [3] that if a solution exists, its center cell is larger than 25 · 10
24.
In Section 1, we give a necessary condition that elements of a magic square of squares…

## Statements it makes

Lemma 1. For any magic 3 × 3 square of squares which is primitive, the corresponding sum
must be s = 3 mod 72, and the (square) elements must be 1 mod 24.

Theorem 1. Let A be a positive odd integer. Then all non-trivial arithmetic progressions of
the form x2, A
2, y2 can be found as follows, each in a unique way. Let p be a square-free divisor
of A, p = 1 mod 4. Write A = pA′, and search for all decompositions A′ = m2 + n2 with m
even and n odd, m, n > 0. Then write b = 4mn(m2 − n
2), x = √A2 − p2b, y = √
A2 + p2b.

Lemma 2. If an odd prime q divides m
2 + n
2 but does not divide m (or n) then it does not
divide m2 − 2mn − n
2.

Lemma 3. Let A > 0 be a integer equal to 3 mod 4. There exists an integer g > 1 such that
for all decompositions A = p(m
2 + n
2) with p, m, n positive integers, g divides p.

*[digest of a 11020 character source; every section, statement, and proof in full at `research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md`]*
