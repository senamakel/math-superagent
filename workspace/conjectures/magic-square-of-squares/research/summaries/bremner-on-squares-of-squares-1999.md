> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/bremner-on-squares-of-squares-1999.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://pdfs.semanticscholar.org/1b0d/bd7d764ece84e9b22b462927979c6e635676.pdf | converted from PDF -->

ACTA ARITHMETICA
LXXXVIII.3 (1999)
 On squares of squares

by

Andrew Bremner (Tempe, Ariz.)

0. There is a long and intriguing history of the subject of magic squares,
squares whose row, column, and diagonal sums are all equal. There has
recently been some interest in whether there can exist a three-by-three magic
square whose nine elements are all perfect squares; the problem seems ﬁrst
to have been raised by LaBar [5]. The answer is of course yes, for example
 52 12 72

72 52 12

12 72 52
 

which is a particular case of the parametrized square
 (m2 + n2)2 (m2 − 2mn − n2)2 (m2 + 2mn − n2)2

(m2 + 2mn − n2)2 (m2 + n2)2 (m2 − 2mn − n2)2

(m2 − 2mn − n2)2 (m2 + 2mn − n2)2 (m2 + n2)2
  .

Martin Gardner [3] has oﬀered $100 for an example of a three-by-three magic
square of squares in which the nine entries are distinct, or for a proof of the
non-existence of such a square. See Sallows [7] for a recent discussion of this
topic, in which is presented (a reﬂection of) the example

(1)
  582 462 1272

942 1132 22

972 822 742
 

which fails to be magic only in that the non-principal diagonal does not have
the common sum (of 1472).
There are two diﬀerent problems that can be posed. The ﬁrst, to ﬁnd
magic squares with as many as possible of the entries being perfect squares;
and the second, to ﬁnd squares with perfect square entries (“squared
squares”) in which as many as possible of the eight row, column, and diag-
onal sums are equal. In this note, we do not treat the ﬁrst problem, other

1991 Mathematics Subject Classiﬁcation: 11G05, 11D25, 11A99.

[289]

290 A. B r e m n e r

than to exhibit the magic square
 3732 2892 5652

360721 4252 232

2052 5272 222121
 

which has seven square entries; it seems that an example with eight distinct
square entries is unknown. See Guy and Nowakowski [4]. For the second
problem, the above example (1) of Sallows gives a squared square with seven
of the eight sums equal. We here extend this example by showing how to
construct parametrized families of squared squares with a similar property,
namely, having all sums equal excepting that of the non-principal diagonal.
(Henceforth, we are only interested in squares having distinct entries, and
will refer to squares with repeated entries as trivial .)
The three smallest squared squares that are found have entries of degree
8, 16, 20 in the parameter, of which we give the ﬁrst two. We ﬁnd just one
example of a magic square in which the entries are from an algebraic number
ﬁeld of odd degree.

1. Any three-by-three magic square of rational numbers has the form

(2)
  a − b a + b + c a − c
a + b − c a a − b + c
a + c a − b − c a + b
 

with a, b, c ∈ Q. The square is trivial (has repeated entries) precisely when

bc(b2 − c2)(b2 − 4c2)(4b2 − c2) = 0.

Suppose that all the entries are perfect squares; then in particular the
three triples {a, a ± c}, {a + b, a + b ± c}, {a − b, a − b ± c} are each triples
of squares. Associate to the above square the elliptic curve

(3) E : y2 = x(x2 − c2).

A point (X, Y ) in E(Q) lies in 2E(Q) if and only if the triple {X, X ± c}
is a triple of rational squares. Accordingly, a − b, a, a + b must all be x-
coordinates of points in 2E(Q). Thus the existence of a magic square of
squares is equivalent to the existence of three points in 2E(Q) with x-
coordinates in arithmetic progression. This observation appears ﬁrst to have
been noticed by Robertson [6], and seems to be a very restrictive condition,
certainly when the rank of E(Q) is small. A small computer search found
very few examples of three points in E(Q) (not 2E(Q)) with x-coordinates
in arithmetic progression. Indeed, the only example found where none of the
three points is a torsion point on E, is the triple

(−528, 26136), (−363, 22869), (−198, 17424)

Squares of squares 291

on the curve
 y2 = x(x2 − 12542)

which has rank 3 over Q.

*[excerpt ends; 11937 characters not shown — see `research/sources/bremner-on-squares-of-squares-1999.full.md`]*
