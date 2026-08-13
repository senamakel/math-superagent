<!-- source: https://oeis.org/A089582 | converted from HTML -->

A089582 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A089582 - OEIS] [3]

A089582

From Gilbreath's conjecture.

4

2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

Let d_0(n) = p_n, the n-th prime, for n = 1 and let d_k+1 (n) = | d_k(n) - d_k(n+1) | for k = 0, n = 1. A well known conjecture, usually ascribed to Gilbreath but actually due to Proth in the 19th century, says that d_k(1) = 1 for all k >= 1. This sequence gives d_k(2) for all k >1 and for the conjecture to be true, this sequence must contain only 0's and 2's. Although not necessary to the conjecture's validity, the 0's and 2's are of roughly equal count.

The paper cited below by A. M. Odlyzko reports on a computation that verified this conjecture for k = p(10^13) ~ 3 * 10^11. It also discusses the evidence and the heuristics about this conjecture. It is very likely that similar conjectures are also valid for many other integer sequences.

Number of zeros in the first 10^n terms: 3, 53, 520, 4995, 49737, 500177, ... - [Robert G. Wilson v][11], Sep 29 2014

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, 2nd Ed., Springer-Verlag, NY, Berlin, 1994, A10.

Clifford A. Pickover, The Math Book, From Pythagoras to the 57th Dimension, 250 Milestones in the History of Mathematics, Sterling Publ., NY, 2009, page 410.

P. Ribenboim, The new book of prime number records, 3rd edition, Springer-Verlag, New York, NY, pp. xxiv+541, ISBN 0-387-94457-5. 1995. MR 96k:11112

LINKS

[Table of n, a(n) for n=1..105.][12]

Chris Caldwell, [The Prime Glossary, Goldbach's conjecture][13].

Andrew M. Odlyzko, [Iterated Absolute Values of Differences of Consecutive Primes][14], Math. Comp. 61 (1993), 373-380.

N. J. A. Sloane, [My favorite integer sequences][15], in Sequences and their Applications (Proceedings of SETA '98).

Eric Weisstein's World of Mathematics, [Gilbreath's Conjecture.][16]

EXAMPLE

See the triangle in [A036262][17].

MAPLE

[A089582][18]:= proc(n)

[A036262][17] (n, 2) ;

end proc:

seq( [A089582][18] (n), n=1..80) ; # [R. J. Mathar][19], May 10 2023

MATHEMATICA

mx = 105; lst = {}; t = Array[ Prime, mx+2]; Do[t = Abs@ Differences@ t; AppendTo[lst, t[[2]]], {n, mx}]; lst

CROSSREFS

See [A036262][17] for an abbreviated table of absolute differences.

Sequence in context: [A044945][20] [A238005][21] [A296509][22] * [A044946][23] [A044947][24] [A044948][25]

Adjacent sequences: [A089579][26] [A089580][27] [A089581][28] * [A089583][29] [A089584][30] [A089585][31]

KEYWORD

easy, nonn

AUTHOR

[Robert G. Wilson v][11] and [R. K. Guy][32], Nov 08 2003

STATUS

approved

[Lookup][3] [Welcome][33] [Wiki][34] [Register][35] [Music][36] [Plot 2][37] [Demos][38] [Index][39] [WebCam][40] [Contribute][41] [Format][42] [Style Sheet][43] [Transforms][44] [Superseeker][45] [Recents][46]

[The OEIS Community][47]

Maintained by [The OEIS Foundation Inc.][48]

Last modified August 13 04:40 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][49]


## Links

[1]: /login?redirect=%2fA089582
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A089582/list
[5]: /A089582/graph
[6]: /search?q=A089582+-id:A089582
[7]: /A089582/listen
[8]: /history?seq=A089582
[9]: /search?q=id:A089582&fmt=text
[10]: /A089582/internal
[11]: /wiki/User:Robert_G._Wilson_v
[12]: /A089582/b089582.txt
[13]: https://t5k.org/glossary/page.php?sort=GilbreathsConjecture
[14]: https://doi.org/10.1090/S0025-5718-1993-1182247-7
[15]: http://neilsloane.com/doc/sg.txt
[16]: https://mathworld.wolfram.com/GilbreathsConjecture.html
[17]: /A036262
[18]: /A089582
[19]: /wiki/User:R._J._Mathar
[20]: /A044945
[21]: /A238005
[22]: /A296509
[23]: /A044946
[24]: /A044947
[25]: /A044948
[26]: /A089579
[27]: /A089580
[28]: /A089581
[29]: /A089583
[30]: /A089584
[31]: /A089585
[32]: /wiki/User:R._K._Guy
[33]: /wiki/Welcome
[34]: /wiki/Main_Page
[35]: /wiki/Special:RequestAccount
[36]: /play.html
[37]: /plot2.html
[38]: /demo1.html
[39]: /wiki/Index_to_OEIS
[40]: /webcam
[41]: /Submit.html
[42]: /eishelp2.html
[43]: /wiki/Style_Sheet
[44]: /transforms.html
[45]: /ol.html
[46]: /recent
[47]: /community.html
[48]: http://oeisf.org
[49]: /wiki/Legal_Documents
