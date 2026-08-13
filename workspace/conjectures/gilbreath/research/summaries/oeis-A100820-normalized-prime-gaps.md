<!-- source: https://oeis.org/A100820 | converted from HTML -->

A100820 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A100820 - OEIS] [3]

A100820

Number of odd numbers between prime(n) and prime(n+1).

2

0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 2, 1, 0, 1, 2, 2, 0, 2, 1, 0, 2, 1, 2, 3, 1, 0, 1, 0, 1, 6, 1, 2, 0, 4, 0, 2, 2, 1, 2, 2, 0, 4, 0, 1, 0, 5, 5, 1, 0, 1, 2, 0, 4, 2, 2, 2, 0, 2, 1, 0, 4, 6, 1, 0, 1, 6, 2, 4, 0, 1, 2, 3, 2, 2, 1, 2, 3, 1, 3, 4, 0, 4, 0, 2, 1, 2, 3, 1, 0, 1, 5, 3, 1, 3, 1, 2, 5, 0, 8, 2, 4, 2, 2, 0, 2

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,9

LINKS

Muniru A Asiru, [Table of n, a(n) for n = 1..2000][11]

Zachary Chase, Zach Hunter, and Terence Tao, [Gilbreath's conjecture: a Cramér random model and a deterministic analysis][12], arXiv:2607.08712 [math.CO], 2026. See p. 2.

FORMULA

a(n) = (prime(n+1)-prime(n))/2-1 = [A001223][13] (n)/2-1 for n>=2. - [Robert Israel][14], Jun 01 2016

a(n) = [A028334][15] (n) - 1 for n>=2. - [Michel Marcus][16], Jan 04 2023

EXAMPLE

a(2)=0 because between 3 and 5 there are no odd numbers.

a(3)=0 because between 5 and 7 there are no odd numbers.

MAPLE

P:= select(isprime, [seq(i, i=3..1000, 2)]):

0, op(map(`-`, 1/2*(P[2..-1]-P[1..-2]), 1)); # [Robert Israel][14], Jun 01 2016

MATHEMATICA

Table[Floor[Max[(Prime[n + 1] - Prime[n])/2 - 1, 0] ], {n, 120}] (* [Ray Chandler][17], Jan 09 2005 *)

PROG

(Magma) [0] cat [(NthPrime(n+1)-NthPrime(n))/2-1 : n in [2..100]]; // [Wesley Ivan Hurt][18], Jun 01 2016

CROSSREFS

Cf. [A000040][19], [A001223][13], [A028334][15], [A036263][20].

Sequence in context: [A194305][21] [A036580][22] [A101674][23] * [A038760][24] [A337938][25] [A245825][26]

Adjacent sequences: [A100817][27] [A100818][28] [A100819][29] * [A100821][30] [A100822][31] [A100823][32]

KEYWORD

easy, nonn

AUTHOR

[Giovanni Teofilatto][33], Jan 06 2005

EXTENSIONS

Corrected and extended by [Ray Chandler][17], Jan 09 2005

STATUS

approved

[Lookup][3] [Welcome][34] [Wiki][35] [Register][36] [Music][37] [Plot 2][38] [Demos][39] [Index][40] [WebCam][41] [Contribute][42] [Format][43] [Style Sheet][44] [Transforms][45] [Superseeker][46] [Recents][47]

[The OEIS Community][48]

Maintained by [The OEIS Foundation Inc.][49]

Last modified August 13 02:54 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][50]


## Links

[1]: /login?redirect=%2fA100820
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A100820/list
[5]: /A100820/graph
[6]: /search?q=A100820+-id:A100820
[7]: /A100820/listen
[8]: /history?seq=A100820
[9]: /search?q=id:A100820&fmt=text
[10]: /A100820/internal
[11]: /A100820/b100820.txt
[12]: https://arxiv.org/abs/2607.08712
[13]: /A001223
[14]: /wiki/User:Robert_Israel
[15]: /A028334
[16]: /wiki/User:Michel_Marcus
[17]: /wiki/User:Ray_Chandler
[18]: /wiki/User:Wesley_Ivan_Hurt
[19]: /A000040
[20]: /A036263
[21]: /A194305
[22]: /A036580
[23]: /A101674
[24]: /A038760
[25]: /A337938
[26]: /A245825
[27]: /A100817
[28]: /A100818
[29]: /A100819
[30]: /A100821
[31]: /A100822
[32]: /A100823
[33]: /wiki/User:Giovanni_Teofilatto
[34]: /wiki/Welcome
[35]: /wiki/Main_Page
[36]: /wiki/Special:RequestAccount
[37]: /play.html
[38]: /plot2.html
[39]: /demo1.html
[40]: /wiki/Index_to_OEIS
[41]: /webcam
[42]: /Submit.html
[43]: /eishelp2.html
[44]: /wiki/Style_Sheet
[45]: /transforms.html
[46]: /ol.html
[47]: /recent
[48]: /community.html
[49]: http://oeisf.org
[50]: /wiki/Legal_Documents
