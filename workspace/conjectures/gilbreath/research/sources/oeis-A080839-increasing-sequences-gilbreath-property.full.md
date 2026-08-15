<!-- source: https://oeis.org/A080839 | converted from HTML -->

A080839 - OEIS

A080839

Number of positive increasing integer sequences of length n with Gilbreath transform (that is, the diagonal of leading successive absolute differences) given by {1,1,1,1,1,...}.

1, 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396, 804131875, 53833201737

(list; graph; refs; listen; history; text; internal format)

OFFSET 1,4

COMMENTS
From T. D. Noe, Feb 05 2007: (Start)
The slowest-growing sequence of length n is 1,2,4,6,...,2(n-1). The fastest-growing sequence is 1,2,4,8,...,2^(n-1).
The ratio a(n+1)a(n-1)/a(n)^2 appears to converge to a constant near 1.46, which is the approximate growth rate of A001609. Are the sequences related?
(End)

Also, a(n) is the number of (not necessarily increasing) positive integer sequences of length n-1 with Gilbreath transform (1, ..., 1). — Pontus von Brömssen, May 13 2023

LINKS
Table of n, a(n) for n=1..13.
Leila Muney, Holes in Valid-Extension Sets of Finite Gilbreath Sequences, arXiv:2606.23721 [math.CO], 2026. See p. 28 (Sect. 14.1).
Index entries for sequences related to Gilbreath conjecture and transform.

EXAMPLE
The table below shows that {1,2,4,6,10} is one of the 6 sequences of length 5 that satisfy the stated condition:
1
2 1
4 2 1
6 2 0 1
10 4 2 2 1

CROSSREFS
Cf. A001609, A036262, A363002, A363003, A363004, A363005.
Cf. also A136465, the total number of increasing sequences with the same maximum length. (Charles R Greathouse IV)

KEYWORD nonn, more

AUTHOR John W. Layman, Mar 28 2003

EXTENSIONS
More terms from T. D. Noe, Feb 05 2007
Added "positive" to definition. — N. J. A. Sloane, May 13 2023

STATUS approved

Last modified August 15 02:31 EDT 2026. Contains 398320 sequences.
