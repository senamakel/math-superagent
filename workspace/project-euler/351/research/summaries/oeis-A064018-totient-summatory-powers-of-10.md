> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A064018-totient-summatory-powers-of-10.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A064018 | converted from HTML -->

A064018 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A064018 - OEIS] [3]

A064018

a(n) = [A002088][4] (10^n) = Sum_{k <= 10^n} phi(k), sum of the Euler totients phi = [A000010][5].

7

1, 32, 3044, 304192, 30397486, 3039650754, 303963552392, 30396356427242, 3039635516365908, 303963551173008414, 30396355092886216366, 3039635509283386211140, 303963550927059804025910, 30396355092702898919527444, 3039635509270144893910357854, 303963550927013509478708835152

( [list][6]; [graph][7]; [refs][8]; [listen][9]; [history][10]; [text][11]; [internal format][12])

OFFSET

0,2

COMMENTS

Asymptotically, [A002088][4] (n) ~ 0.30396355...*n^2 = (3/Pi^2)*n^2, see [A104141][13] and [A002088][4]. - [Michael B. Porter][14], Mar 08 2013 [corrected by [M. F. Hasler][15], Apr 18 2015]

LINKS

Lucas A. Brown, [Table of n, a(n) for n = 0..19][16] (terms 0..18 from Hiroaki Yamanouchi)

Lucas A. Brown, [Python program][17].

Lucas Augustus Brown, [Computation of the Totient Summatory Function][18], arXiv:2506.07386 [math.NT], 2025.

Eric Weisstein's World of Mathematics, [Totient Summatory Function][19].

Wikipedia, [Totient summatory function][20].

FORMULA

a(n) = Sum_{k <= 10^n} [A000010][5] (k).

EXAMPLE

a(1) = phi(1) + ... + phi(10) = 1 + 1 + 2 + 2 + 4 + 2 + 6 + 4 + 6 + 4 = 32.

MATHEMATICA

s = 0; k = 1; Do[ While[ k <= 10^n, s = s + EulerPhi[ k ]; k++ ]; Print[ s ], {n, 0, 8} ]

PROG

(Python) # See LINKS. - [Lucas A. Brown][21], Jun 08 2025

CROSSREFS

Cf. [A000010][5], [A002088][4], [A104141][13].

Sequence in context: [A220299][22] [A264115][23] [A113500][24] * [A067321][25] [A104652][26] [A395123][27]

Adjacent sequences: [A064015][28] [A064016][29] [A064017][30] * [A064019][31] [A064020][32] [A064021][33]

KEYWORD

nonn

AUTHOR

[Robert G. Wilson v][34], Sep 07 2001

EXTENSIONS

More terms from [Robert G. Wilson v][34], Sep 07 2001

a(10)-a(11) from [Donovan Johnson][35], Feb 06 2010

a(12) from [Donovan Johnson][35], Feb 07 2012

a(13)-a(14) from [Hiroaki Yamanouchi][36], Jul 06 2014

a(15) from [Asif Ahmed][37], Apr 16 2015

Name edited by [Michel Marcus][38] and [M. F. Hasler][15], Apr 16 and Apr 18 2015

STATUS

approved

[Lookup][3] [Welcome][39] [Wiki][40] [Register][41] [Music][42] [Plot 2][43] [Demos][44] [Index][45] [WebCam][46] [Contribute][47] [Format][48] [Style Sheet][49] [Transforms][50] [Superseeker][51] [Recents][52]

[The OEIS Community][53]

Maintained by [The OEIS Foundation Inc.][54]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][55]


## Links

[1]: /login?redirect=%2fA064018
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A002088
[5]: /A000010
[6]: /A064018/list
[7]: /A064018/graph
[8]: /search?q=A064018+-id:A064018
[9]: /A064018/listen
[10]: /history?seq=A064018
[11]: /search?q=id:A064018&fmt=text
[12]: /A064018/internal
[13]: /A104141
[14]: /wiki/User:Michael_B._Porter
[15]: /wiki/User:M._F._Hasler
[16]: /A064018/b064018.txt
[17]: https://github.com/lucasaugustus/oeis/blob/main/A064018.py
[18]: https://arxiv.org/pdf/2506.07386
[19]: https://mathworld.wolfram.com/TotientSummatoryFunction.html
[20]: https://en.wikipedia.org/wiki/Totient_summatory_function
[21]: /wiki/User:Lucas_A._Brown
[22]: /A220299
[23]: /A264115
[24]: /A113500
[25]: /A067321
[26]: /A104652
[27]: /A395123
[28]: /A064015
[29]: /A064016
[30]: /A064017
[31]: /A064019
[32]: /A064020
[33]: /A064021
[34]: /wiki/User:Robert_G._Wilson_v
[35]: /wiki/User:Donovan_Johnson
[36]: /wiki/User:Hiroaki_Yamanouchi
[37]: /wiki/User:Asif_Ahmed
[38]: /wiki/User:Michel_Marcus
[39]: /wiki/Welcome
[40]: /wiki/Main_Page
[41]: /wiki/Special:RequestAccount
[42]: /play.html
[43]: /plot2.html
[44]: /demo1.html
[45]: /wiki/Index_to_OEIS
[46]: /webcam
[47]: /Submit.html
[48]: /eishelp2.html
[49]: /wiki/Style_Sheet
[50]: /transforms.html
[51]: /ol.html
[52]: /recent
[53]: /community.html

*[excerpt ends; 52 characters not shown — see `research/sources/oeis-A064018-totient-summatory-powers-of-10.full.md`]*
