<!-- source: https://oeis.org/A002827 | converted from HTML -->

A002827 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002827 - OEIS] [3]

A002827

Unitary perfect numbers: numbers k such that usigma(k) - k = k.
(Formerly M4268 N1783)

47

6, 60, 90, 87360, 146361946186458562560000

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

d is a unitary divisor of k if gcd(d,k/d)=1; usigma(k) is their sum ( [A034448][11]).

The prime factors of a unitary perfect number ( [A002827][12]) are the Higgs primes ( [A057447][13]). - [Paul Muljadi][14], Oct 10 2005

It is not known if a(6) exists. - [N. J. A. Sloane][15], Jul 27 2015

Frei proved that if there is a unitary perfect number that is not divisible by 3, then it is divisible by 2^m with m >= 144, it has at least 144 distinct odd prime factors, and it is larger than 10^440. - [Amiram Eldar][16], Mar 05 2019

Conjecture: Subsequence of [A083207][17] (Zumkeller numbers). Verified for all present terms. - [Ivan N. Ianakiev][18], Jan 20 2020

All unitary perfect numbers are even (for a proof see the LeanGenius link). - [Peter Luschny][19], Jun 05 2026

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, Sect. B3.

F. Le Lionnais, Les Nombres Remarquables. Paris: Hermann, p. 59, 1983.

D. S. Mitrinovic et al., Handbook of Number Theory, Kluwer, Section III.45.1.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

James J. Tattersall, Elementary Number Theory in Nine Chapters, Cambridge University Press, 1999, pages 147-148.

LINKS

[Table of n, a(n) for n=1..5.][20]

T. F. Bloom, [Erdős Problem #1052][21].

H. A. M. Frei, [Über unitar perfekte Zahlen][22], Elemente der Mathematik, Vol. 33, No. 4 (1978), pp. 95-96.

Takeshi Goto, [Upper Bounds for Unitary Perfect Numbers and Unitary Harmonic Numbers][23], Rocky Mountain Journal of Mathematics, Vol. 37, No. 5 (2007), pp. 1557-1576.

A. V. Lelechenko, [The Quest for the Generalized Perfect Numbers][24], in Theoretical and Applied Aspects of Cybernetics, TAAC 2014, Kiev.

M. V. Subbarao, [Letter to N. J. A. Sloane, Feb 18 1974][25]

M. V. Subbarao, T. J. Cook, R. S. Newberry and J. M. Weber, [On unitary perfect numbers][26], Delta, 3 (No. 1, 1972), 22-26.

G. Villemin's Almanac of Numbers, [Nombres Unitairement Parfaits][27]

C. R. Wall, [Letter to P. Hagis, Jr., Jan 13 1972][28]

C. R. Wall, [The fifth unitary perfect number][29], Canad. Math. Bull., 18 (1975), 115-122.

C. R. Wall, [On the largest odd component of a unitary perfect number][30], Fib. Quart., 25 (1987), 312-316.

Robb J. Walters, [Erdős #1052: Unitary Perfect Numbers][31], LeanGenius.

Eric Weisstein's World of Mathematics, [Unitary Perfect Number.][32]

Wikipedia, [Unitary perfect number][33]

FORMULA

If m is a term and omega(m) = [A001221][34] (m) = k, then m < 2^(2^k) (Goto, 2007). - [Amiram Eldar][16], Jun 06 2020

EXAMPLE

6 = 2 * 3.

60 = 2^2 * 3 * 5.

90 = 2 * 3^2 * 5.

87360 = 2^6 * 3 * 5 * 7 * 13.

146361946186458562560000 = 2^18 * 3 * 5^4 * 7 * 11 * 13 * 19 * 37 * 79 * 109 * 157 * 313.

.

Unitary divisors of 60 are 1, 4, 3, 5, 12, 20, 15, 60, with sum 120 = 2*60.

MATHEMATICA

usnQ[n_]:=Total[Select[Divisors[n], GCD[#, n/#]==1&]]==2n; Select[Range[ 90000], usnQ] (* This will generate the first four terms of the sequence; it would take a very long time to attempt to generate the fifth term. *) (* [Harvey P. Dale][35], Nov 14 2012 *)

PROG

(PARI) is(n)=sumdivmult(n, d, if(gcd(d, n/d)==1, d))==2*n \\ [Charles R Greathouse IV][36], Aug 01 2016

CROSSREFS

Cf. [A034460][37], [A034448][11], [A057447][13].

Subsequence of the following sequences: [A003062][38], [A290466][39] (seemingly), [A293188][40], [A327157][41], [A327158][42].

Gives the positions of ones in [A327159][43].

Sequence in context: [A324707][44] [A007357][45] [A327158][42] * [A331111][46] [A324199][47] [A137498][48]

Adjacent sequences: [A002824][49] [A002825][50] [A002826][51] * [A002828][52] [A002829][53] [A002830][54]

KEYWORD

nonn, nice, hard

AUTHOR

[N. J. A. Sloane][15]

STATUS

approved

[Lookup][3] [Welcome][55] [Wiki][56] [Register][57] [Music][58] [Plot 2][59] [Demos][60] [Index][61] [WebCam][62] [Contribute][63] [Format][64] [Style Sheet][65] [Transforms][66] [Superseeker][67] [Recents][68]

[The OEIS Community][69]

Maintained by [The OEIS Foundation Inc.][70]

Last modified August 13 06:02 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][71]


## Links

[1]: /login?redirect=%2fA002827
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A002827/list
[5]: /A002827/graph
[6]: /search?q=A002827+-id:A002827
[7]: /A002827/listen
[8]: /history?seq=A002827
[9]: /search?q=id:A002827&fmt=text
[10]: /A002827/internal
[11]: /A034448
[12]: /A002827
[13]: /A057447
[14]: /wiki/User:Paul_Muljadi
[15]: /wiki/User:N._J._A._Sloane
[16]: /wiki/User:Amiram_Eldar
[17]: /A083207
[18]: /wiki/User:Ivan_N._Ianakiev
[19]: /wiki/User:Peter_Luschny
[20]: /A002827/b002827.txt
[21]: https://www.erdosproblems.com/1052
[22]: https://www.e-periodica.ch/digbib/view?pid=edm-001:1978:33#105
[23]: https://doi.org/10.1216/rmjm/1194275935
[24]: http://taac.org.ua/files/a2014/proceedings/UA-2-Andrew%20Lelechenko-440.pdf
[25]: /A002827/a002827.pdf
[26]: http://www.math.ualberta.ca/~subbarao/documents/Subbarao_Cook_Newberry_Weber1972.pdf
[27]: http://villemin.gerard.free.fr/Wwwgvmm/Decompos/ParfUnit.htm
[28]: /A002827/a002827_1.pdf
[29]: https://doi.org/10.4153/CMB-1975-021-9
[30]: https://www.fq.math.ca/Scanned/25-4/wall1.pdf
[31]: https://leangenius.org/proof/erdos-1052
[32]: https://mathworld.wolfram.com/UnitaryPerfectNumber.html
[33]: https://en.wikipedia.org/wiki/Unitary_perfect_number
[34]: /A001221
[35]: /wiki/User:Harvey_P._Dale
[36]: /wiki/User:Charles_R_Greathouse_IV
[37]: /A034460
[38]: /A003062
[39]: /A290466
[40]: /A293188
[41]: /A327157
[42]: /A327158
[43]: /A327159
[44]: /A324707
[45]: /A007357
[46]: /A331111
[47]: /A324199
[48]: /A137498
[49]: /A002824
[50]: /A002825
[51]: /A002826
[52]: /A002828
[53]: /A002829
[54]: /A002830
[55]: /wiki/Welcome
[56]: /wiki/Main_Page
[57]: /wiki/Special:RequestAccount
[58]: /play.html
[59]: /plot2.html
[60]: /demo1.html
[61]: /wiki/Index_to_OEIS
[62]: /webcam
[63]: /Submit.html
[64]: /eishelp2.html
[65]: /wiki/Style_Sheet
[66]: /transforms.html
[67]: /ol.html
[68]: /recent
[69]: /community.html
[70]: http://oeisf.org
[71]: /wiki/Legal_Documents
