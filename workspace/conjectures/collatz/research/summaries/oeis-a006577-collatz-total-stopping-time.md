> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-a006577-collatz-total-stopping-time.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: oeis-a006577-terms
statement: The total stopping time sequence A006577 (number of halving and tripling steps to reach 1 in the 3x+1 problem, -1 if never reached) begins 0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, 7, 15, 15, 10, 23, 10, 111, 18, 18, 18, 106, 5, 26, 13, 13, 21, 21, 21, 34, 8, 109, 8, 29, 16, 16, 16, 104, 11, 24, 24, 24, 11, 11, 112, 112, 19, 32, 19, 32, 19, 19, 107, 107, 6, 27, ... (a(1)=0).
hypotheses: the plain Collatz map (n/2 if even, 3n+1 if odd); total stopping time to reach 1.
holds-here: true — the oracle must reproduce these terms.
evidence: OEIS A006577 (indexed sequence; computed by the OEIS).
status: verified-numerically
falsifies: a computation producing different values for a(n) in this range.
```

```claim
id: oeis-a006577-relations
statement: a(n) = A006666(n) + A006667(n) (halving steps + tripling steps); a(n) = A008908(n) − 1 (1-based length minus one).
hypotheses: the same map; standard definitions of the component sequences.
holds-here: true — identities to check the oracle against.
evidence: OEIS A006577 FORMULA section.
status: asserted-by-source
falsifies: a counterexample n where the identities fail (would indicate a definition mismatch).
```

<!-- source: https://oeis.org/A006577 | converted from HTML -->

A006577 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A006577 - OEIS] [3]

A006577

Number of halving and tripling steps to reach 1 in '3x+1' problem, or -1 if 1 is never reached.
(Formerly M4323)

263

0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, 7, 15, 15, 10, 23, 10, 111, 18, 18, 18, 106, 5, 26, 13, 13, 21, 21, 21, 34, 8, 109, 8, 29, 16, 16, 16, 104, 11, 24, 24, 24, 11, 11, 112, 112, 19, 32, 19, 32, 19, 19, 107, 107, 6, 27, 27, 27, 14, 14, 14, 102, 22

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,3

COMMENTS

The 3x+1 or Collatz problem is as follows: start with any number n. If n is even, divide it by 2, otherwise multiply it by 3 and add 1. Do we always reach 1? This is a famous unsolved problem. It is conjectured that the answer is yes.

It seems that about half of the terms satisfy a(i) = a(i+1). For example, up to 10000000, 4964705 terms satisfy this condition.

n is an element of row a(n) in triangle [A127824][11]. - [Reinhard Zumkeller][12], Oct 03 2012

The number of terms that satisfy a(i) = a(i+1) for i less than a power of ten from 10^1 through 10^10 are: 0, 31, 365, 4161, 45022, 477245, 4964705, 51242281, 526051204, 5378743993. - [John Mason][13], Mar 02 2018

5 seems to be the only number whose value matches its total number of steps (checked to n <= 10^9). - [Peter Woodward][14], Feb 15 2021

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, E16.

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

LINKS

N. J. A. Sloane, [Table of n, a(n) for n = 1..10000][15]

David Eisenbud and Brady Haran, [UNCRACKABLE? The Collatz Conjecture][16], Numberphile video, 2016.

Geometry.net, [Links on Collatz Problem][17]

Christian Hercher, [There are no Collatz m-Cycles with m <= 91][18], J. Int. Seq. (2023) Vol. 26, Article 23.3.5.

Jason Holt, [Log-log plot of first billion terms][19]

Jason Holt, [Plot of 1 billion values of the number of steps to drop below n][20] ( [A060445][21]), log scale on x axis

Jason Holt, [Plot of 10 billion values of the number of steps to drop below n][22] ( [A060445][21]), log scale on x axis

A. Krowne, [Collatz problem][23], PlanetMath.org.

J. C. Lagarias, [The 3x+1 problem and its generalizations][24], Amer. Math. Monthly, 92 (1985), 3-23.

J. C. Lagarias, [How random are 3x+1 function iterates?][25], in The Mathemagician and the Pied Puzzler - A Collection in Tribute to Martin Gardner, Ed. E. R. Berlekamp and T. Rogers, A. K. Peters, 1999, pp. 253-266.

J. C. Lagarias, [The 3x+1 Problem: an annotated bibliography, II (2000-2009)][26], arXiv:0608208 [math.NT], 2006-2012.

J. C. Lagarias, ed., [The Ultimate Challenge: The 3x+1 Problem][27], Amer. Math. Soc., 2010.

Jeffrey C. Lagarias, [The 3x+1 Problem: An Overview][28], arXiv:2111.02635 [math.NT], 2021.

M. Le Brun, [Email to N. J. A. Sloane, Jul 1991][29]

Mathematical BBS, [Biblography on Collatz Sequence][30]

P. Picart, [Algorithme de Collatz et conjecture de Syracuse][31]

E. Roosendaal, [On the 3x+1 problem][32]

J. L. Simons, [On the nonexistence of 2-cycles for the 3x+1 problem][33], Math. Comp. 75 (2005), 1565-1572.

N. J. A. Sloane, ["A Handbook of Integer Sequences" Fifty Years Later][34], arXiv:2301.03149 [math.NT], 2023, p. 8.

G. Villemin's Almanach of Numbers, [Cycle of Syracuse][35]

Eric Weisstein's World of Mathematics, [Collatz Problem][36]

Wikipedia, [Collatz Conjecture][37]

[Index entries for sequences related to 3x+1 (or Collatz) problem][38]

FORMULA

a(n) = [A006666][39] (n) + [A006667][40] (n).

a(n) = [A112695][41] (n) + 2 for n > 2. - [Reinhard Zumkeller][12], Apr 18 2008

a(n) = [A008908][42] (n) - 1. - [L. Edson Jeffery][43], Jul 21 2014


*[excerpt ends; 6066 characters not shown — see `research/sources/oeis-a006577-collatz-total-stopping-time.full.md`]*
