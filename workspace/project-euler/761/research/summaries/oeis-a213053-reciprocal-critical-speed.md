<!-- source: https://oeis.org/A213053 | converted from HTML -->

A213053 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A213053 - OEIS] [3]

A213053

Decimal expansion of the absolute minimum of sinc(x) = sin(x)/x (negated).

3

2, 1, 7, 2, 3, 3, 6, 2, 8, 2, 1, 1, 2, 2, 1, 6, 5, 7, 4, 0, 8, 2, 7, 9, 3, 2, 5, 5, 6, 2, 4, 7, 0, 7, 3, 4, 2, 2, 3, 0, 4, 4, 9, 1, 5, 4, 3, 5, 5, 8, 7, 4, 8, 2, 3, 6, 5, 4, 4, 9, 0, 2, 7, 7, 1, 4, 5, 0, 5, 3, 4, 3, 5, 8, 9, 0, 6, 3, 2, 2, 9, 1, 8, 5, 5, 6, 8, 0, 5, 0, 6, 5, 3, 9, 2, 3, 5, 4, 9, 5, 1, 5, 2, 0, 1

( [list][4]; [constant][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,1

COMMENTS

Minimum value of the first negative lobe of sinc(x), attained for abs(x) = [A115365][12].

The involute of the unit circle which starts at (1,0) crosses the x-axis for the first time at x = 1/a. - [Álvar Ibeas][13], Jul 28 2017

LINKS

[Table of n, a(n) for n=0..104.][14]

FORMULA

Equals -1 / sqrt(1 + [A115365][12] ^2) = cos( [A115365][12]). - [Álvar Ibeas][13], Jul 28 2017

EXAMPLE

min[real x](sinc(x)) = -0.2172336282112216574082...

MATHEMATICA

digits = 105; NMinimize[ Sinc[x], x, WorkingPrecision -> digits+5] // First // RealDigits[#, 10, digits]& // First (* [Jean-François Alcover][15], Mar 05 2013 *)

RealDigits[Sinc[BesselJZero[3/2, 1]], 10, 100][[1]] (* [Vladimir Reshetnikov][16], May 13 2016 *)

PROG

(PARI) y=solve(x=4, 4.5, tan(x)-x); -sin(y)/y \\ [Charles R Greathouse IV][17], Jun 10 2012

(PARI) -sinc(besseljzero(3/2, 1)) \\ [Charles R Greathouse IV][17], Jan 23 2025

CROSSREFS

Cf. [A115365][12].

Sequence in context: [A121416][18] [A317547][19] [A089329][20] * [A200236][21] [A292191][22] [A239155][23]

Adjacent sequences: [A213050][24] [A213051][25] [A213052][26] * [A213054][27] [A213055][28] [A213056][29]

KEYWORD

nonn, [cons][5]

AUTHOR

[Stanislav Sykora][30], Jun 09 2012

STATUS

approved

[Lookup][3] [Welcome][31] [Wiki][32] [Register][33] [Music][34] [Plot 2][35] [Demos][36] [Index][37] [WebCam][38] [Contribute][39] [Format][40] [Style Sheet][41] [Transforms][42] [Superseeker][43] [Recents][44]

[The OEIS Community][45]

Maintained by [The OEIS Foundation Inc.][46]

Last modified August 12 13:20 EDT 2026. Contains 398245 sequences.

[License Agreements, Terms of Use, Privacy Policy][47]


## Links

[1]: /login?redirect=%2fA213053
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A213053/list
[5]: /A213053/constant
[6]: /A213053/graph
[7]: /search?q=A213053+-id:A213053
[8]: /A213053/listen
[9]: /history?seq=A213053
[10]: /search?q=id:A213053&fmt=text
[11]: /A213053/internal
[12]: /A115365
[13]: /wiki/User:Álvar_Ibeas
[14]: /A213053/b213053.txt
[15]: /wiki/User:Jean-François_Alcover
[16]: /wiki/User:Vladimir_Reshetnikov
[17]: /wiki/User:Charles_R_Greathouse_IV
[18]: /A121416
[19]: /A317547
[20]: /A089329
[21]: /A200236
[22]: /A292191
[23]: /A239155
[24]: /A213050
[25]: /A213051
[26]: /A213052
[27]: /A213054
[28]: /A213055
[29]: /A213056
[30]: /wiki/User:Stanislav_Sykora
[31]: /wiki/Welcome
[32]: /wiki/Main_Page
[33]: /wiki/Special:RequestAccount
[34]: /play.html
[35]: /plot2.html
[36]: /demo1.html
[37]: /wiki/Index_to_OEIS
[38]: /webcam
[39]: /Submit.html
[40]: /eishelp2.html
[41]: /wiki/Style_Sheet
[42]: /transforms.html
[43]: /ol.html
[44]: /recent
[45]: /community.html
[46]: http://oeisf.org
[47]: /wiki/Legal_Documents
