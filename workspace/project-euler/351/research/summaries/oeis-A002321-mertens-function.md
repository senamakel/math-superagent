> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A002321-mertens-function.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A002321 | converted from HTML -->

A002321 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002321 - OEIS] [3]

A002321

Mertens's function: Sum_{k=1..n} mu(k), where mu is the Moebius function [A008683][4].
(Formerly M0102 N0038)

156

1, 0, -1, -1, -2, -1, -2, -2, -2, -1, -2, -2, -3, -2, -1, -1, -2, -2, -3, -3, -2, -1, -2, -2, -2, -1, -1, -1, -2, -3, -4, -4, -3, -2, -1, -1, -2, -1, 0, 0, -1, -2, -3, -3, -3, -2, -3, -3, -3, -3, -2, -2, -3, -3, -2, -2, -1, 0, -1, -1, -2, -1, -1, -1, 0, -1, -2, -2, -1, -2, -3, -3, -4, -3, -3, -3, -2, -3, -4, -4, -4

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,5

COMMENTS

Partial sums of the Moebius function [A008683][4].

Also determinant of n X n (0,1) matrix defined by A(i,j)=1 if j=1 or i divides j.

The first positive value of Mertens's function for n > 1 is for n = 94. The graph seems to show a negative bias for the Mertens function which is eerily similar to the Chebyshev bias (described in [A156749][12] and [A156709][13]). The purported bias seems to be empirically approximated to - (6 / Pi^2) * (sqrt(n) / 4) (by looking at the graph) (see MathOverflow link, May 28 2012) where 6 / Pi^2 = 1 / zeta(2) is the asymptotic density of squarefree numbers (the squareful numbers having Moebius mu of 0). This would be a growth pattern akin to the Chebyshev bias. - [Daniel Forgues][14], Jan 23 2011

All integers appear infinitely often in this sequence. - [Charles R Greathouse IV][15], Aug 06 2012

Soundararajan proves that, on the Riemann Hypothesis, a(n) << sqrt(n) exp(sqrt(log n)*(log log n)^14), sharpening the well-known equivalence. - [Charles R Greathouse IV][15], Jul 17 2015

Balazard & De Roton improve this (on the Riemann Hypothesis) to a(n) << sqrt(n) exp(sqrt(log n)*(log log n)^k) for any k > 5/2, where the implied constant in the Vinogradov symbol depends on k. Saha & Sankaranarayanan reduce the exponent to 5/4 on additional hypotheses. - [Charles R Greathouse IV][15], Feb 02 2023

REFERENCES

E. Landau, Vorlesungen über Zahlentheorie, Chelsea, NY, Vol. 2, p. 157.

D. H. Lehmer, Guide to Tables in the Theory of Numbers. Bulletin No. 105, National Research Council, Washington, DC, 1941, pp. 7-10.

F. Mertens, "Über eine zahlentheoretische Funktion", Akademie Wissenschaftlicher Wien Mathematik-Naturlich Kleine Sitzungsber, IIa 106, (1897), p. 761-830.

D. S. Mitrinovic et al., Handbook of Number Theory, Kluwer, Section VI.1.

Biswajyoti Saha and Ayyadurai Sankaranarayanan, On estimates of the Mertens function, International Journal of Number Theory, Vol. 15, No. 02 (2019), pp. 327-337.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

J. von zur Gathen and J. Gerhard, Modern Computer Algebra, Cambridge, 1999, see p. 482.

LINKS

T. D. Noe, [Table of n, a(n) for n = 1..10000][16]

Michel Balazard and Anne De Roton, [Sur un critère de Baez-Duarte pour l'hypothèse de Riemann][17], Int'l J. Number Theory 6(4) (2010), 883-903. arXiv preprint arXiv:0812.1689 [math.NT], 2008.

B. Boncompagni, [Selected values of the Mertens function][18].

Olivier Bordellès, [Some Explicit Estimates for the Mobius Function][19], J. Int. Seq. 18 (2015), Article 15.11.1.

G. J. Chaitin, [Thoughts on the Riemann hypothesis][20], arXiv:math/0306042 [math.HO], 2003.

J. Brian Conrey, [The Riemann Hypothesis][21], Notices Amer. Math. Soc., 50 (No. 3, March 2003), 341-353. See p. 347.

Marc Deléglise and Joël Rivat, [Computing the summation of the Mobius function][22], Experiment. Math. 5(4) (1996), 291-295.

François Dress, [Fonction sommatoire de la fonction de Moebius. 1. Majorations expérimentales][23], Experiment. Math. 2(2) (1993), 89-98.


*[excerpt ends; 8903 characters not shown — see `research/sources/oeis-A002321-mertens-function.full.md`]*
