> **This summary IS the complete document** — the download system stores the A000232 page
> as the summary file itself; there is no separate `oeis-A000232-block-lengths.full.md`
> on disk (a download attempt is refused as a duplicate). The 444-character tail not
> shown below is OEIS footer boilerplate (login/license/community links), no content.

<!-- source: https://oeis.org/A000232 | converted from HTML -->

A000232 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A000232 - OEIS] [3]

A000232

Construct a triangle as in [A036262][4]. Sequence is one less than the position of the first number larger than 2 in the n-th row (n-th difference).
(Formerly M2718 N1089)

3

3, 8, 14, 14, 25, 24, 23, 22, 25, 59, 98, 97, 98, 97, 174, 176, 176, 176, 176, 291, 290, 289, 740, 874, 873, 872, 873, 872, 871, 870, 869, 868, 867, 866, 2180, 2179, 2178, 2177, 2771, 2770, 2769, 2768, 2767, 2766, 2765, 2764, 2763, 2763, 2763, 2763, 3366, 4208, 4207

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,1

COMMENTS

Related to Gilbreath conjecture.

In particular, if a(n) > 2 for every n, then the Gilbreath conjecture is true. - [Bartlomiej Pawlik][12], Nov 28 2025

REFERENCES

W. Sierpiński, A Selection of Problems in the Theory of Numbers. Macmillan, NY, 1964, p. 35.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

LINKS

T. D. Noe, [Table of n, a(n) for n=1..274][13]

Chris Caldwell, [Gilbreath's conjecture][14]

Albert N. Debono, [More on primes][15], Numbers and Computers (11).

R. B. Killgrove and K. E. Ralston, [On a conjecture concerning the primes][16], Math. Comp., 13 (1959), 121-122.

Eric Weisstein's World of Mathematics, [Gilbreath's Conjecture][17]

[Index entries for primes, gaps between][18]

FORMULA

a(n) = [A036277][19] (n) - 1. - [T. D. Noe][20], Feb 03 2007

MAPLE

[A000232][21]:= proc(n)

local k;

for k from 1 do

if [A036262][4] (n, k) > 2 then

return k-1 ;

end if;

end do:

end proc:

seq( [A000232][21] (n), n=1..40) ; # [R. J. Mathar][22], May 10 2023

MATHEMATICA

max = 10^4; triangle = NestList[Abs[Differences[#]] &, Prime[Range[max]], max]; a[n_] := (p = Position[triangle[[n + 1]], k_ /; k > 2, 1, 1]; If[p == {}, Nothing, p[[1, 1]] - 1]); Table[a[n], {n, 1, Sqrt[max]}] (* [Jean-François Alcover][23], Feb 06 2016 *)

CROSSREFS

Cf. [A001549][24].

Sequence in context: [A366071][25] [A305179][26] [A106386][27] * [A375292][28] [A361363][29] [A067789][30]

Adjacent sequences: [A000229][31] [A000230][32] [A000231][33] * [A000233][34] [A000234][35] [A000235][36]

KEYWORD

nonn

AUTHOR

[N. J. A. Sloane][37]

EXTENSIONS

Edited by [Robert G. Wilson v][38], Aug 18 2002

More terms from [Jean-François Alcover][23], Feb 06 2016

STATUS

approved

[Lookup][3] [Welcome][39] [Wiki][40] [Register][41] [Music][42] [Plot 2][43] [Demos][44] [Index][45] [WebCam][46] [Contribute][47] [Format][48] [Style Sheet][49] [Transforms][50] [Superseeker][51] [Recents][52]

[The OEIS Community][53]

Maintained by [The OEIS Foundation Inc.][54]

Last modified August 13 02:40 EDT 2026. Contains 398269 sequences.

[License Agreements, Terms of Use, Privacy Policy][55]


## Links

[1]: /login?redirect=%2fA000232
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A036262
[5]: /A000232/list
[6]: /A000232/graph
[7]: /search?q=A000232+-id:A000232
[8]: /A000232/listen
[9]: /history?seq=A000232
[10]: /search?q=id:A000232&fmt=text
[11]: /A000232/internal
[12]: /wiki/User:Bartlomiej_Pawlik
[13]: /A000232/b000232.txt
[14]: https://t5k.org/glossary/page.php?sort=GilbreathsConjecture
[15]: http://web.archive.org/web/20060215084642/http://www.eng.um.edu.mt/~andebo/numbers/numcom11.htm
[16]: https://doi.org/10.1090/S0025-5718-59-99262-2
[17]: https://mathworld.wolfram.com/GilbreathsConjecture.html
[18]: /index/Pri#gaps
[19]: /A036277
[20]: /wiki/User:T._D._Noe
[21]: /A000232
[22]: /wiki/User:R._J._Mathar
[23]: /wiki/User:Jean-François_Alcover
[24]: /A001549
[25]: /A366071
[26]: /A305179
[27]: /A106386
[28]: /A375292
[29]: /A361363
[30]: /A067789
[31]: /A000229
[32]: /A000230
[33]: /A000231
[34]: /A000233
[35]: /A000234

*[excerpt ends; 444 characters not shown — see `research/sources/oeis-A000232-block-lengths.full.md`]*
