> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A018805-coprime-pairs.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A018805 | converted from HTML -->

A018805 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A018805 - OEIS] [3]

A018805

Number of elements in the set {(x,y): 1 <= x,y <= n, gcd(x,y)=1}.

83

1, 3, 7, 11, 19, 23, 35, 43, 55, 63, 83, 91, 115, 127, 143, 159, 191, 203, 239, 255, 279, 299, 343, 359, 399, 423, 459, 483, 539, 555, 615, 647, 687, 719, 767, 791, 863, 899, 947, 979, 1059, 1083, 1167, 1207, 1255, 1299, 1391, 1423, 1507, 1547, 1611, 1659, 1763

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,2

COMMENTS

Number of positive rational numbers of height at most n, where the height of p/q is max(p, q) when p and q are relatively prime positive integers. - [Charles R Greathouse IV][11], Jul 05 2012

The number of ordered pairs (i,j) with 1<=i<=n, 1<=j<=n, gcd(i,j)=d is a(floor(n/d)). - [N. J. A. Sloane][12], Jul 29 2012

Equals partial sums of [A140434][13] (1, 2, 4, 4, 8, 4, 12, 8, ...) and row sums of triangle [A143469][14]. - [Gary W. Adamson][15], Aug 17 2008

Number of distinct solutions to k*x+h=0, where 1 <= k,h <= n. - [Giovanni Resta][16], Jan 08 2013

a(n) is the number of rational numbers which can be constructed from the set of integers between 1 and n, without combination of multiplication and division. a(3) = 7 because {1, 2, 3} can only create {1/3, 1/2, 2/3, 1, 3/2, 2, 3}. - [Bernard Schott][17], Jul 07 2019

The number of distinct y-coordinates of interior edge crossings in the straight-line drawing of the complete bipartite graph K_{n+1,n+1}, with vertices at (i,1) and (j,0), 1<=i,j<=n+1. If edges (i,1)-(p,0) and (j,1)-(q,0) cross (i<j, p>q), then the intersection has y = (p-q)/(j-i + p-q) = B/(A+B), where 1<=A,B<=n. Distinct y are exactly the reduced fractions B/(A+B); i.e., those with gcd(A,B) = 1. Hence the number of such y is [A018805][18] (n). - [Tikhon Tsvetkov][19], Jan 14 2026

REFERENCES

S. R. Finch, Mathematical Constants, Cambridge, 2003, pp. 110-112.

G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers. 3rd ed., Oxford Univ. Press, 1954. See Theorem 332.

LINKS

Olivier Gérard, [Table of n, a(n) for n = 1..100000][20] [Replaces an earlier b-file from Charles R Greathouse IV]

Jin-Yi Cai and Eric Bach, [On testing for zero polynomials by a set of points with bounded precision][21], Theoret. Comput. Sci. 296 (2003), no. 1, 15-25. MR1965515 (2004m:68279).

Pieter Moree, [Counting carefree couples][22], arXiv:math/0510003 [math.NT], 2005-2014.

N. J. A. Sloane, [Families of Essentially Identical Sequences][23], Mar 24 2021 (Includes this sequence)

Eric Weisstein's World of Mathematics, [Carefree Couple][24]

FORMULA

a(n) = 2*(Sum_{j=1..n} phi(j)) - 1.

a(n) = n^2 - Sum_{j=2..n} a(floor(n/j)).

a(n) = 2*[A015614][25] (n) + 1. - [Reinhard Zumkeller][26], Apr 08 2006

a(n) = 2*[A002088][27] (n) - 1. - [Hugo van der Sanden][28], Nov 22 2008

a(n) ~ (1/zeta(2)) * n^2 = (6/Pi^2) * n^2 as n goes to infinity (zeta is the Riemann zeta function, [A013661][29], and the constant 6/Pi^2 is 0.607927..., [A059956][30]). - Ahmed Fares (ahmedfares(AT)my-deja.com), Jul 18 2001

a(n) ~ 6*n^2/Pi^2 + O(n*log n). - [N. J. A. Sloane][12], May 31 2020

a(n) = Sum_{k=1..n} mu(k)*floor(n/k)^2. - [Benoit Cloitre][31], May 11 2003

a(n) = [A000290][32] (n) - [A100613][33] (n) = [A015614][25] (n) + [A002088][27] (n). - [Reinhard Zumkeller][26], Jan 21 2013

a(n) = [A242114][34] (floor(n/k),1), 1<=k<=n; particularly a(n) = [A242114][34] (n,1). - [Reinhard Zumkeller][26], May 04 2014

a(n) = 2 * [A005728][35] (n) - 3. - [David H Post][36], Dec 20 2016

a(n) ~ 6*n^2/Pi^2, cf. [A059956][30]. [Hardy and Wright] - [M. F. Hasler][37], Jan 20 2017

G.f.: (1/(1 - x)) * (-x + 2 * Sum_{k>=1} mu(k) * x^k / (1 - x^k)^2). - [Ilya Gutkovskiy][38], Feb 14 2020

MAPLE

N:= 1000; # to get the first N entries

P:= Array(1..N, numtheory:-phi);


*[excerpt ends; 4524 characters not shown — see `research/sources/oeis-A018805-coprime-pairs.full.md`]*
