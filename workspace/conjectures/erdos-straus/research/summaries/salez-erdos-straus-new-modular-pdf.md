> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/salez-erdos-straus-new-modular-pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1406.6307 | converted from PDF -->

## What it claims

In 1999 Allan Swett [5] checked (in 150 hours) the Erdős-Straus conjecture up to N = 10
14

with a sieve based on a single modular equation. After having proved the existence of a
"complete" set of seven modular equations (including three new ones), this paper oﬀers an
optimized sieve based on these equations. A program written in C++ (and given elsewhere)
allows then to make a checking whose running time, on a typical computer
1, range from few
minutes for N = 10
14 to about 16 hours for N = 10
17.

1 Basic formulas

A fraction is said to be k-Egyptian if it is the sum of at most k positive unit fractions (i.e with
numerator equal to 1). The Erdős-Straus conjecture claims that 4/n is a 3-Egyptian fraction for
any n > 1.

1.1 Reduction

Through the identities 1
t = 1
t + 1 + 1
t(t + 1)

2
2t − 1 = 1
t + 1
t(2t − 1)

it is equivalent (for n > 2) to require having exactly 3 diﬀerent unit fractions, what we shall do
thereafter.

On the other hand, the identities
 4
3t − 1 = 1
t + 1
3t − 1 + 1
t(3t − 1)

4
4t − 1 = 1
t + 1
t(4t − 1)

4
8t − 3 = 1
2t + 1
t(8t − 3) + 1
2t(8t − 3)

show…

T…

## Statements it makes

Proposition 1 Let p a prime element. The fraction 4/p is 3-Egyptian if and only if there exists
four elements of A+ denoted by A, B, C, D such that

Proposition 2 (Schinzel’s Theorem )
Let a > 0 and b such as (a, b) = 1. If 4/(at + b) is 3-Egyptian4 then b is a quadratic non residue
modulo a.

Lemma 1 Let p be a prime polynomial of degree 1.

Proposition 3 Let p be a prime polynomial of degree 1. The fraction 4/p is 3-Egyptian if and
only if one of the next 7 modular equations holds.

Corollary 1 Let p be an odd prime integer. The fraction 4/p is 3-Egyptian if and only if one of
the 7 modular equations of the Proposition 3 holds.

*[digest of a 30904 character source; every section, statement, and proof in full at `research/sources/salez-erdos-straus-new-modular-pdf.full.md`]*
