> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A000010-euler-totient.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A000010 | converted from HTML -->

## What is in it

- Alternative:
- Alternative: without library function


## What it claims

1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,3

COMMENTS

Number of elements in a reduced residue system modulo n.

Degree of the n-th cyclotomic polynomial (cf. [A013595][11]). - [Benoit Cloitre][12], Oct 12 2002

Number of distinct generators of a cyclic group of order n. Number of primitive n-th roots of unity. (A primitive n-th root x is such that x^k is not equal to 1 for k = 1, 2, ..., n - 1, but x^n = 1.) - [Lekraj Beedassy][13], Mar 31 2005

Also number of complex Dirichlet characters modulo n; Sum_{k=1..n} a(k) is asymptotic to (3/Pi^2)*n^2. - [Steven Finch][14], Feb 16 2006

a(n) is the highest degree of irreducible polynomial dividing 1 + x + x^2 + ... + x^(n-1) = (x^n - 1)/(x - 1). - [Alexander Adamchuk][15], Sep 02 2006, corrected Sep 27 2006

a(p) = p -…

## Statements it makes

Conjecture: Sum_{i>=2} (-1)^i/(i*phi(i)) exists and is approximately 0.558 ( [A335319][99]). - Orges Leka (oleka(AT)students.uni-mainz.de), Dec 23 2004

Conjecture: a(n) = Sum_{a=1..n} Sum_{b=1..n} Sum_{c=1..n} 1 for n > 1. The sum is over a,b,c such that n*c - a*b = 1. - [Benedict W. J. Irwin][117], Apr 03 2017

*[digest of a 29641 character source; every section, statement, and proof in full at `research/sources/oeis-A000010-euler-totient.full.md`]*
