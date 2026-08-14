> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A002088-summatory-totient.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A002088 | converted from HTML -->

A002088 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002088 - OEIS] [3]

A002088

Sum of totient function: a(n) = Sum_{k=1..n} phi(k), cf. [A000010][4].
(Formerly M1008 N0376)

154

0, 1, 2, 4, 6, 10, 12, 18, 22, 28, 32, 42, 46, 58, 64, 72, 80, 96, 102, 120, 128, 140, 150, 172, 180, 200, 212, 230, 242, 270, 278, 308, 324, 344, 360, 384, 396, 432, 450, 474, 490, 530, 542, 584, 604, 628, 650, 696, 712, 754, 774, 806, 830, 882, 900, 940, 964

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,3

COMMENTS

Number of elements in the set {(x,y): 1 <= x <= y <= n, 1=gcd(x,y)}. - [Michael Somos][12], Jun 13 1999

Sum_{k=1..n} phi(k) gives the number of distinct arithmetic progressions which contain an infinite number of primes and whose difference does not exceed n. E.g., {1k+1}, {2k+1}, {3k+1, 3k+2}, {4k+1, 4k+3}, {5k+1, ..5k+4} means 10 sequences. - [Labos Elemer][13], May 02 2001

The quotient [A024916][14] (n)/a(n) = SummatorySigma/SummatoryTotient as n increases seems to approach Pi^4/36 = zeta(2)^2 = [A098198][15] = 2.705808084277845... . - [Labos Elemer][13], Sep 20 2004 (corrected by Peter Pein, Apr 28 2009)

Also the number of rationals p/q in (0,1] with denominators q<=n. - [Franz Vrabec][16], Jan 29 2005

a(n) is the number of initial segments of Beatty sequences for real numbers > 1, cut off when the next term in the sequence would be >= n. For example, the sequence 1,2 is included for n=3 and n=4, but not for n >= 5 because the next term of the Beatty sequence must be 3 or 4. Problem suggested by [David W. Wilson][17]. - [Franklin T. Adams-Watters][18], Oct 19 2006

Number of complex numbers satisfying any one of {x^1=1, x^2=1, x^3=1, x^4=1, x^5=1, ..., x^n=1}. - Paul Smith (math.idiot(AT)gmail.com), Mar 19 2007

a(n+2) equals the number of Sturmian words of length n which are 'special', prefix of two Sturmian words of length n+1. - [Fred Lunnon][19], Sep 05 2010

For n > 1: [A020652][20] (a(n)) = 1 and [A038567][21] (a(n)) = n; for n > 0: [A214803][22] (a(n)) = 1. - [Reinhard Zumkeller][23], Jul 29 2012

Also number of elements in the set {(x,y): 1 <= x + y <= n, x >= 0, y > 0, with x and y relatively prime integers}. Thus, the number of reduced rational numbers x/y with x nonnegative, y positive, and x + y <= n. (For n >= 1, 0 <= x/y <= n - 1, clearly including each integer in this interval.) - [Rick L. Shepherd][24], Apr 08 2014

This function, the partial sums of phi = [A000010][4], is sometimes denoted by (uppercase) Phi. - [M. F. Hasler][25], Apr 18 2015

From [Roger Ford][26], Jan 16 2016: (Start)

For n >= 1: a(n) is the number of perfect arched semi-meander solutions with n arches. To be perfect the number of arch groupings must equal the number of arches with a length of 1 in the current generation and every preceding generation.

Example: p is the number of arches with length 1 (/\), g is the number of arch groups (-), n is number of arches in the top half of a semi-meander solution

/\

/\ //\\

//\\-/\-///\\\- n=6 p=3 g=3 Each preceding arch configuration

/\ /\ is formed by attaching the arch

/\-//\\-//\\- n=5 p=3 g=3 end in the first position and the

/\ arch end in the last position.

//\\

///\\\-/\- n=4 p=2 g=2

/\

//\\-/\- n=3 p=2 g=2

/\-/\- n=2 p=2 g=2

/\- n=1 p=1 g=1. (End)

a(n) is the number of distinct lists of binary words of length n that are balanced (Sturmian). - [Dan Rockwell][27], Will Wodrich, Aaliyah Fiala, and Bob Burton, May 30 2019

2013 IMO Problem 6 shows that a(n) is the number of ways to arrange the numbers 0, 1, ..., n on a circle such that for any numbers 0 <= a < b < c < d <= n, the chord joining a and d does not intersect with the chord intersecting b and c, with rotation counted as same. - [Yifan Xie][28], Aug 26 2025

REFERENCES


*[excerpt ends; 11216 characters not shown — see `research/sources/oeis-A002088-summatory-totient.full.md`]*
