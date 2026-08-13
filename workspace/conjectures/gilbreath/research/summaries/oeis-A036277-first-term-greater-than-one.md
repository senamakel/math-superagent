<!-- source: https://oeis.org/A036277 | converted from HTML -->

A036277 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A036277 - OEIS] [3]

A036277

Position of first term > 2 in n-th row of Gilbreath array shown in [A036262][4].

4

2, 4, 9, 15, 15, 26, 25, 24, 23, 26, 60, 99, 98, 99, 98, 175, 177, 177, 177, 177, 292, 291, 290, 741, 875, 874, 873, 874, 873, 872, 871, 870, 869, 868, 867, 2181, 2180, 2179, 2178, 2772, 2771, 2770, 2769, 2768, 2767, 2766, 2765, 2764, 2764, 2764, 2764, 3367

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,1

COMMENTS

Gilbreath's conjecture is equivalent to: [A036277][12] (n)> [A213014][13] (n)+2 for all n>0. See [A036262][4] for a proof. - [M. F. Hasler][14], Jun 02 2012

REFERENCES

A. S. Fraenkel and B. J. Reuter, On certain sequences of integers and prime numbers, Proc. 2nd National Conf. Data Processing, Rehovoth, Jan 1966, pp. 450-437.

R. K. Guy, Unsolved Problems Number Theory, A10.

LINKS

T. D. Noe, [Table of n, a(n) for n=0..274][15]

A. M. Odlyzko, [Iterated absolute values of differences of consecutive primes][16], Math. Comp., 61 (1993), pp. 373-380.

FORMULA

a(n) = [A000232][17] (n)+1. - [R. J. Mathar][18], May 10 2023

EXAMPLE

Row 1 of [A036262][4] is 1 2 2 4 2 4 2 4 ... so a(1) = 4.

[N.B.: While the first row of the table [A036261][19] contains the absolute first differences of the primes, table [A036262][4] starts with the primes themselves in the uppermost row, which is obviously here referred to as the 0th row. - [M. F. Hasler][14], Jun 02 2012]

MATHEMATICA

max = 10^4; triangle = NestList[Abs[Differences[#]]&, Prime[Range[max]], max]; a[n_] := (p = Position[triangle[[n+1]], k_ /; k>2, 1, 1]; If[p == {}, Nothing, p[[1, 1]]]); Table[a[n], {n, 0, Sqrt[max]}] (* [Jean-François Alcover][20], Feb 06 2016 *)

CROSSREFS

Sequence in context: [A113862][21] [A244624][22] [A343592][23] * [A042960][24] [A266596][25] [A045975][26]

Adjacent sequences: [A036274][27] [A036275][28] [A036276][29] * [A036278][30] [A036279][31] [A036280][32]

KEYWORD

easy, nice, nonn

AUTHOR

[N. J. A. Sloane][33]

EXTENSIONS

More terms from [David W. Wilson][34], Aug 30 2000

STATUS

approved

[Lookup][3] [Welcome][35] [Wiki][36] [Register][37] [Music][38] [Plot 2][39] [Demos][40] [Index][41] [WebCam][42] [Contribute][43] [Format][44] [Style Sheet][45] [Transforms][46] [Superseeker][47] [Recents][48]

[The OEIS Community][49]

Maintained by [The OEIS Foundation Inc.][50]

Last modified August 13 04:40 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][51]


## Links

[1]: /login?redirect=%2fA036277
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A036262
[5]: /A036277/list
[6]: /A036277/graph
[7]: /search?q=A036277+-id:A036277
[8]: /A036277/listen
[9]: /history?seq=A036277
[10]: /search?q=id:A036277&fmt=text
[11]: /A036277/internal
[12]: /A036277
[13]: /A213014
[14]: /wiki/User:M._F._Hasler
[15]: /A036277/b036277.txt
[16]: https://doi.org/10.1090/S0025-5718-1993-1182247-7
[17]: /A000232
[18]: /wiki/User:R._J._Mathar
[19]: /A036261
[20]: /wiki/User:Jean-François_Alcover
[21]: /A113862
[22]: /A244624
[23]: /A343592
[24]: /A042960
[25]: /A266596
[26]: /A045975
[27]: /A036274
[28]: /A036275
[29]: /A036276
[30]: /A036278
[31]: /A036279
[32]: /A036280
[33]: /wiki/User:N._J._A._Sloane
[34]: /wiki/User:David_W._Wilson
[35]: /wiki/Welcome
[36]: /wiki/Main_Page
[37]: /wiki/Special:RequestAccount
[38]: /play.html
[39]: /plot2.html
[40]: /demo1.html
[41]: /wiki/Index_to_OEIS
[42]: /webcam
[43]: /Submit.html
[44]: /eishelp2.html
[45]: /wiki/Style_Sheet
[46]: /transforms.html
[47]: /ol.html
[48]: /recent
[49]: /community.html
[50]: http://oeisf.org
[51]: /wiki/Legal_Documents
