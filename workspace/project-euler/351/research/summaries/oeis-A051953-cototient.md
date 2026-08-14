> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A051953-cototient.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A051953 | converted from HTML -->

## What it claims

0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12, 1, 12, 9, 12, 1, 16, 5, 14, 9, 16, 1, 22, 1, 16, 13, 18, 11, 24, 1, 20, 15, 24, 1, 30, 1, 24, 21, 24, 1, 32, 7, 30, 19, 28, 1, 36, 15, 32, 21, 30, 1, 44, 1, 32, 27, 32, 17, 46, 1, 36, 25, 46, 1, 48, 1, 38, 35, 40, 17, 54, 1, 48, 27

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,4

COMMENTS

Unlike totients, cototient(n+1) = cototient(n) never holds -- except 2-phi(2) = 3 - phi(3) = 1 -- because cototient(n) is congruent to n modulo 2. - [Labos Elemer][11], Aug 08 2001

Theorem (L. Redei): b^a(n) == b^n (mod n) for every integer b. - [Thomas Ordowski][12] and [Robert Israel][13], Mar 11 2016

Let S be the sum of the cototients of the divisors of n ( [A001065][14]). S < n iff n is deficient, S = n iff n is perfect, and S > n iff n is abundant. - [Ivan N. Ianakiev][15], Oct 06 2023

LINKS

T. D. Noe, [Table of n, a(n) for n = 1..10000][16]

J. Browkin and A. Schinzel, [On integers not of the form n-phi(n)][17], Colloq. Math., 68 (1995), 55-58.

R. E. Jamison, [The Helly…

## Statements it makes

Theorem (L. Redei): b^a(n) == b^n (mod n) for every integer b. - [Thomas Ordowski][12] and [Robert Israel][13], Mar 11 2016

*[digest of a 7206 character source; every section, statement, and proof in full at `research/sources/oeis-A051953-cototient.full.md`]*
