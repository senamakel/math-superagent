> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A008683-mobius-function.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A008683 | converted from HTML -->

## What is in it

- Note that older versions of Maple define mobius(0) to be -1.
- This is unwise! Moebius(0) is better left undefined.
- Changing the sign of the sum gives the number of ordered factorizations of n…


## What it claims

1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0, 1, 1, -1, 0, 0, 1, 0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, 1, 1, 0, -1, -1, -1, 0, 0, 1, -1, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 1, -1, 0, -1, 1, 0, 0, 1, -1, -1, 0, 1, -1, -1, 0, -1, 1, 0, 0, 1, -1

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

Moebius inversion: f(n) = Sum_{d|n} g(d) for all n <=> g(n) = Sum_{d|n} mu(d)*f(n/d) for all n.

a(n) depends only on prime signature of n (cf. [A025487][11]). So a(24) = a(375) since 24 = 2^3 * 3 and 375 = 3 * 5^3 both have prime signature (3, 1).

[A008683][12] = [A140579][13] ^(-1) * [A140664][14]. - [Gary W. Adamson][15], May 20 2008

Coons & Borwein prove that Sum_{n>=1} mu(n) z^n is transcendental. - [Jonathan Vos Post][16], Jun 11 2008; edited by [Charles R Greathouse IV][17], Sep 06 2017

Equals row sums of triangle [A144735][18] (the square of triangle [A054533][19]). - [Gary W. Adamson][15], Sep 20 2008

Conjecture: a(n) is the determinant of Redheffer matrix [A143104][20] where T(n, n) = 0.…

From…

## Statements it makes

Conjecture: a(n) is the determinant of Redheffer matrix [A143104][20] where T(n, n) = 0. Verified for the first 50 terms. - [Mats Granvik][21], Jul 25 2008

Conjecture: Consider the table [A051731][22] and treat 1 as a divisor. Move the value in the lower right corner vertically to a divisor position in the transpose of the table and you will find that the determinant is the Moebius function. The number of permutation matrices that contribute to the Moebius function appears to be [A074206][23]. - [Mats Granvik][21], Dec 08 2008

*[digest of a 19778 character source; every section, statement, and proof in full at `research/sources/oeis-A008683-mobius-function.full.md`]*
