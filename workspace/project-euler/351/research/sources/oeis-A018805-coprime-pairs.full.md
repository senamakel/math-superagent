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

A:= map(t -> 2*round(t)-1, Statistics:-CumulativeSum(P));

convert(A, list); # [Robert Israel][39], Jul 16 2014

MATHEMATICA

FoldList[ Plus, 1, 2 Array[ EulerPhi, 60, 2 ] ] (* [Olivier Gérard][40], Aug 15 1997 *)

Accumulate[2*EulerPhi[Range[60]]]-1 (* [Harvey P. Dale][41], Oct 21 2013 *)

PROG

(PARI) a(n)=sum(k=1, n, moebius(k)*(n\k)^2)

(PARI) [A018805][18] (n)=2 *sum(j=1, n, eulerphi(j)) - 1;

for(n=1, 99, print1( [A018805][18] (n), ", ")); /* show terms */

(PARI) a(n)=my(s); forsquarefree(k=1, n, s+=moebius(k)*(n\k[1])^2); s \\ [Charles R Greathouse IV][11], Jan 08 2018

(Magma) /* based on the first formula */ [A018805][18]:=func< n | 2*&+[ EulerPhi(k): k in [1..n] ]-1 >; [ [A018805][18] (n): n in [1..60] ]; // [Klaus Brockhaus][42], Jan 27 2011

(Magma) /* based on the second formula */ [A018805][18]:=func< n | n eq 1 select 1 else n^2-&+[ $$(n div j): j in [2..n] ] >; [ [A018805][18] (n): n in [1..60] ]; // [Klaus Brockhaus][42], Feb 07 2011

(Haskell)

a018805 n = length [()| x <- [1..n], y <- [1..n], gcd x y == 1]

-- [Reinhard Zumkeller][26], Jan 21 2013

(Python)

from sympy import sieve

def [A018805][18] (n): return 2*sum(t for t in sieve.totientrange(1, n+1)) - 1 # [Chai Wah Wu][43], Mar 23 2021

(Python)

from functools import lru_cache

@lru_cache(maxsize=None)

def [A018805][18] (n): # based on second formula

if n == 0:

return 0

c, j = 1, 2

k1 = n//j

while k1 > 1:

j2 = n//k1 + 1

c += (j2-j)*[A018805][18] (k1)

j, k1 = j2, n//j2

return n*(n-1)-c+j # [Chai Wah Wu][43], Mar 24 2021

CROSSREFS

Cf. [A015614][25], [A002088][27], [A100613][33] (gcd > 1), [A071778][44] (triples), [A143469][14], [A140434][13], [A013661][29], [A059956][30], [A137243][45], [A171503][46].

Cf. [A177853][47] (partial sums).

The main diagonal of [A331781][48], also of [A333295][49].

Sequence in context: [A277878][50] [A117991][51] [A118260][52] * [A191037][53] [A292083][54] [A135932][55]

Adjacent sequences: [A018802][56] [A018803][57] [A018804][58] * [A018806][59] [A018807][60] [A018808][61]

KEYWORD

nonn, nice

AUTHOR

[David W. Wilson][62]

EXTENSIONS

More terms from [Reinhard Zumkeller][26], Apr 08 2006

Link to Moree's paper corrected by [Peter Luschny][63], Aug 08 2009

STATUS

approved

[Lookup][3] [Welcome][64] [Wiki][65] [Register][66] [Music][67] [Plot 2][68] [Demos][69] [Index][70] [WebCam][71] [Contribute][72] [Format][73] [Style Sheet][74] [Transforms][75] [Superseeker][76] [Recents][77]

[The OEIS Community][78]

Maintained by [The OEIS Foundation Inc.][79]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][80]


## Links

[1]: /login?redirect=%2fA018805
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A018805/list
[5]: /A018805/graph
[6]: /search?q=A018805+-id:A018805
[7]: /A018805/listen
[8]: /history?seq=A018805
[9]: /search?q=id:A018805&fmt=text
[10]: /A018805/internal
[11]: /wiki/User:Charles_R_Greathouse_IV
[12]: /wiki/User:N._J._A._Sloane
[13]: /A140434
[14]: /A143469
[15]: /wiki/User:Gary_W._Adamson
[16]: /wiki/User:Giovanni_Resta
[17]: /wiki/User:Bernard_Schott
[18]: /A018805
[19]: /wiki/User:Tikhon_Tsvetkov
[20]: /A018805/b018805.txt
[21]: https://doi.org/10.1016/S0304-3975(02)00429-2
[22]: https://arxiv.org/pdf/math/0510003
[23]: /A115004/a115004.txt
[24]: https://mathworld.wolfram.com/CarefreeCouple.html
[25]: /A015614
[26]: /wiki/User:Reinhard_Zumkeller
[27]: /A002088
[28]: /wiki/User:Hugo_van_der_Sanden
[29]: /A013661
[30]: /A059956
[31]: /wiki/User:Benoit_Cloitre
[32]: /A000290
[33]: /A100613
[34]: /A242114
[35]: /A005728
[36]: /wiki/User:David_H_Post
[37]: /wiki/User:M._F._Hasler
[38]: /wiki/User:Ilya_Gutkovskiy
[39]: /wiki/User:Robert_Israel
[40]: /wiki/User:Olivier_Gérard
[41]: /wiki/User:Harvey_P._Dale
[42]: /wiki/User:Klaus_Brockhaus
[43]: /wiki/User:Chai_Wah_Wu
[44]: /A071778
[45]: /A137243
[46]: /A171503
[47]: /A177853
[48]: /A331781
[49]: /A333295
[50]: /A277878
[51]: /A117991
[52]: /A118260
[53]: /A191037
[54]: /A292083
[55]: /A135932
[56]: /A018802
[57]: /A018803
[58]: /A018804
[59]: /A018806
[60]: /A018807
[61]: /A018808
[62]: /wiki/User:David_W._Wilson
[63]: /wiki/User:Peter_Luschny
[64]: /wiki/Welcome
[65]: /wiki/Main_Page
[66]: /wiki/Special:RequestAccount
[67]: /play.html
[68]: /plot2.html
[69]: /demo1.html
[70]: /wiki/Index_to_OEIS
[71]: /webcam
[72]: /Submit.html
[73]: /eishelp2.html
[74]: /wiki/Style_Sheet
[75]: /transforms.html
[76]: /ol.html
[77]: /recent
[78]: /community.html
[79]: http://oeisf.org
[80]: /wiki/Legal_Documents
