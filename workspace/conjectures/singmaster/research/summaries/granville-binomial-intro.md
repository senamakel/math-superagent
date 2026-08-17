> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/granville-binomial-intro.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://dms.umontreal.ca/~andrew/Binomial/intro.html | converted from HTML -->

## What is in it

- Introduction.


## What it claims

Many great mathematicians of the nineteenth century considered problems involving binomial coefficients modulo a prime power (for instance Babbage, Cauchy, Cayley, Gauss, Hensel, Hermite, Kummer, Legendre, Lucas and Stickelberger -- see [Dickson][1]). They discovered a variety of elegant and surprising Theorems which are often easy to prove. In this article we shall exhibit most of these results, and extend them in a variety of ways. We start with a discussion of what this article contains:

In 1852 Kummer showed that the power of prime *p*that divides the binomial coefficient is given by the number of `carries' when we add *m*and *n-m*in base *p*.

In 1878 Lucas gave a method to easily determine the value of : Let and be the least non-negative residues of *m*and , respectively. Then

**(1)**

where, as usual, denotes the largest integer , and we use the convention if *r<s*. Re-writing and in base *p*(so that for each *i*), this may also be expressed as

We will give three very different proofs of Lucas' Theorem: via [number theory][2], via [cellular automata][3], and via the…

Note…

## Statements it makes

**Theorem 1.***Suppose that prime power and positive integers *m=n+r*are given. Let be the least positive residue of for each (and make the corresponding definitions for *m*and *r*). Let be the number of `carries', when adding *m*and *r*in base *p*, on or beyond the *j*th digit). Then

Theorem 1 provides a quick way to compute the value of binomial coefficients modulo arbitrary prime powers: in fact [we will show][6] that this takes just elementary operations.

**Theorem 2.***Suppose that prime *p*and positive integers *u*and *r*are given. Then

*[digest of a 7803 character source; every section, statement, and proof in full at `research/sources/granville-binomial-intro.full.md`]*
