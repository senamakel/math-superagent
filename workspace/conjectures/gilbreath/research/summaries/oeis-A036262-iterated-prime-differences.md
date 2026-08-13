> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A036262-iterated-prime-differences.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A036262 | converted from HTML -->

A036262 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A036262 - OEIS] [3]

A036262

Array of numbers read by upward antidiagonals, arising from Gilbreath's conjecture: leading row lists the primes; the following rows give absolute values of differences of previous row.

45

2, 1, 3, 1, 2, 5, 1, 0, 2, 7, 1, 2, 2, 4, 11, 1, 2, 0, 2, 2, 13, 1, 2, 0, 0, 2, 4, 17, 1, 2, 0, 0, 0, 2, 2, 19, 1, 2, 0, 0, 0, 0, 2, 4, 23, 1, 2, 0, 0, 0, 0, 0, 2, 6, 29, 1, 0, 2, 2, 2, 2, 2, 2, 4, 2, 31, 1, 0, 0, 2, 0, 2, 0, 2, 0, 4, 6, 37, 1, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 4, 41, 1, 0, 0, 0, 0, 2, 0, 0, 0

( [list][4]; [table][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,1

COMMENTS

The conjecture is that the leading term is always 1.

Odlyzko has checked it for primes up to pi(10^13) = 3*10^11.

From [M. F. Hasler][12], Jun 02 2012: (Start)

The second column, omitting the initial 3, is given in [A089582][13]. The number of "0"s preceding the first term > 1 in the n-th row is given in [A213014][14]. The first term > 1 in any row must equal 2, else the conjecture is violated: Obviously all terms except for the first one are even. Thus, if the 2nd term in some row is > 2, it is >= 4, and the first term of the subsequent row is >= 3. If there is a positive number of zeros preceding a first term > 2 (thus >= 4), this "jump" will remain constant and "propagate" (in subsequent rows) to the beginning of the row, and the previously discussed case applies.

The previous statement can also be formulated as: Gilbreath's conjecture is equivalent to: [A036277][15] (n) > [A213014][14] (n)+2 for all n.

CAVEAT: While table [A036261][16] starts with the first absolute differences of the primes in its first row, the present sequence has the primes themselves in its uppermost row, which is sometimes referred to as "row 0". Thus, "first row" of this table [A036262][17] may either refer to row 1 (1,2,2,...), or to row 0 (2,3,5,7,...), while the latter might, however, as well be referred to "row 1 of [A036262][17] " in other sequences or papers.

(End)

From [Clark Kimberling][18], Nov 27 2022: (Start)

Suppose that S = (s(k)), for k >= 1, is a sequence of real numbers. For n >= 1, let g(1,n) = |s(n+1)-s(n)| and g(k,n) = |g(k-1,n+1) - g(k-1,n)| for k >= 2.

Call (g(k,n)) the Gilbreath array of S. Call the first column of this array the Gilbreath transform of S. Denote this transform by G(S), so that G(S) is the sequence (g(n,1)). If S is the sequence of primes, then the Gilbreath conjecture holds that G(S) consists exclusively of 1's. More generally, it appears that there are many S such that G(S) is eventually periodic. See [A358691][19] for conjectured examples. (End)

REFERENCES

R. K. Guy, Unsolved Problems Number Theory, A10.

H. L. Montgomery, Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis, Amer. Math. Soc., 1996, p. 208.

C. A. Pickover, The Math Book, Sterling, NY, 2009; see p. 410.

Paulo Ribenboim, The Little Book of Bigger Primes, Springer-Verlag NY 2004. See p. 192.

W. Sierpiński, L'induction incomplète dans la théorie des nombres, Scripta Math. 28 (1967), 5-13.

LINKS

T. D. Noe, [Table of n, a(n) for n = 0..5049][20]

Richard K. Guy, [The strong law of small numbers][21]. Amer. Math. Monthly 95 (1988), no. 8, 697-712. [Annotated scanned copy]

R. B. Killgrove and K. E. Ralston, [On a conjecture concerning the primes][22], Math. Comput. 13 (1959), 121-122.

Leila Muney, [Holes in Valid-Extension Sets of Finite Gilbreath Sequences][23], arXiv:2606.23721 [math.CO], 2026. See p. 28 (Sect. 14.1).

Andrew M. Odlyzko, [Iterated absolute values of differences of consecutive primes][24], Math. Comp. 61 (1993), 373-380.

F. Proth, [Sur la série des nombres premiers][25], Nouv. Corresp. Math., 4 (1878) 236-240.


*[excerpt ends; 4909 characters not shown — see `research/sources/oeis-A036262-iterated-prime-differences.full.md`]*
