> **Excerpt only — read this first.** The complete text is beside it at `research/zerocount.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://oeis.org/A059015 | converted from HTML -->

A059015 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A059015 - OEIS] [3]

A059015

Total number of 0's in binary expansions of 0, ..., n.

48

1, 1, 2, 2, 4, 5, 6, 6, 9, 11, 13, 14, 16, 17, 18, 18, 22, 25, 28, 30, 33, 35, 37, 38, 41, 43, 45, 46, 48, 49, 50, 50, 55, 59, 63, 66, 70, 73, 76, 78, 82, 85, 88, 90, 93, 95, 97, 98, 102, 105, 108, 110, 113, 115, 117, 118, 121, 123, 125, 126, 128, 129, 130, 130, 136, 141

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,3

COMMENTS

Partial sums of [A023416][11]. - [Reinhard Zumkeller][12], Jul 15 2011

The graph of this sequence is a version of the Takagi curve: see Lagarias (2012), Section 9, especially Theorem 9.1. - [N. J. A. Sloane][13], Mar 12 2016

LINKS

T. D. Noe and Hieronymus Fischer, [Table of n, a(n) for n = 0..10000][14] (terms up to n=1023 by T. D. Noe)

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and asymptotic solutions of the recurrence f(n) = f(floor(n/2)) + f(ceiling(n/2)) + g(n): theory and applications][15], Preprint 2016.

Hsien-Kuei Hwang, S. Janson, and T.-H. Tsai, [Exact and Asymptotic Solutions of a Divide-and-Conquer Recurrence Dividing at Half: Theory and Applications][16], ACM Transactions on Algorithms, 13:4 (2017), #47; DOI: 10.1145/3127585.

Jeffrey C. Lagarias, [The Takagi function and its properties][17], arXiv:1112.4205 [math.CA], 2011-2012.

Jeffrey C. Lagarias, [The Takagi function and its properties][18], In Functions in number theory and their probabilistic aspects, 153--189, RIMS Kôkyûroku Bessatsu, B34, Res. Inst. Math. Sci. (RIMS), Kyoto, 2012. MR3014845.

Ralf Stephan, [Some divide-and-conquer sequences ...][19]

Ralf Stephan, [Table of generating functions][20]

[Index entries for sequences related to binary expansion of n][21]

FORMULA

a(n) = b(n)+1, with b(2n) = b(n)+b(n-1)+n, b(2n+1) = 2b(n)+n. - [Ralf Stephan][22], Sep 13 2003

From [Hieronymus Fischer][23], Jun 10 2012: (Start)

With m = floor(log_2(n)):

a(n) = 2 + (m+1)*(n+1) - 2^(m+1) + (1/2)*Sum_{j=1..m+1} (floor(n/2^j)*(2*n + 2 - (1 + floor(n/2^j))*2^j) - floor(n/2^j + 1/2)*(2*n + 2 - floor(n/2^j + 1/2)*2^j)).

a(n) = [A083652][24] (n) - (n+1)*[A000120][25] (n) + 2^(m-1) - (1/4) + (1/2)*sum_{j=1..m+1} (floor(n/2^j + 1/2)^2 - (floor(n/2^j) + 1/2)^2)*2^j.

a(2^m-1) = 2 + (m-2)*2^(m-1)

(this is the total number of zero digits occurring in all the numbers with <= m places).

G.f.: 1/(1 - x) + (1/(1 - x)^2)*Sum_{j>=0} x^(2*2^j)/(1 + x^(2^j)); corrected by [Ilya Gutkovskiy][26], Mar 28 2018

General formulas for the number of digits <= d in the base p representations of all integers from 0 to n, where 0 <= d < p.

With m = floor(log_p(n)):

a(n) = 1 + (m+1)*(n+1) - (p^(m+1)-1)/(p-1) + (1/2)*sum_{j=1..m+1} (floor(n/p^j)*(2n + 2 - (1 + floor(n/p^j))*p^j) - floor(n/p^j + (p-d-1)/p)*(2n + 2 + ((p-2*d-2)/p - floor(n/p^j + (p-d-1)/p))*p^j)).

a(n) = H(n,p) - (n+1)*F(n,p,d+1) + (1/2)*sum_{j=1..m+1} ((floor(n/p^j + (p-d-1)/p)^2 - floor(n/p^j)^2)*p^j - (((p - 2*d-2)/p)*floor(n/p^j + (p-d-1)/p) + floor(n/p^j))*p^j), where H(n,p) = sum of number of digits in the base p representations of 0 to n and F(n,p,d) = number of digits >=d in the base p representation of n.

a(p^m-1) = 1 + (d+1)*m*p^(m-1) - (p^m-1)/(p-1).

(this is the total number of digits <= d occurring in all the numbers with <= m places in base p representation).

G.f.: 1/(1-x) + (1/(1-x)^2)*Sum_{j>=0} ((1-x^(d*p^j))*x^p^j + (1-x^p^j)*x^p^(j+1)/(1-x^p^(j+1))). (End)

a(n) = [A083652][24] (n) - [A000788][27] (n). - [Alan Michael Gómez Calderón][28], Sep 25 2025

MAPLE

a:= proc(n) option remember; `if`(n=0, 1, a(n-1)+add(1-i, i=Bits[Split](n))) end:

seq(a(n), n=0..65); # [Alois P. Heinz][29], Nov 11 2024

MATHEMATICA

Accumulate[ Table[ Count[ IntegerDigits[n, 2], 0], {n, 0, 65}]] (* [Jean-François Alcover][30], Oct 03 2012 *)


*[excerpt ends; 3842 characters not shown — see `research/zerocount.full.md`]*
