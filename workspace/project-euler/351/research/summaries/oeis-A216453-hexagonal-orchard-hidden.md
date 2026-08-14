<!-- source: https://oeis.org/A216453 | converted from HTML -->

A216453 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A216453 - OEIS] [3]

A216453

Number of points hidden from the central point by a closer point in a hexagonal orchard of order n.

1

0, 6, 12, 24, 30, 54, 60, 84, 102, 138, 144, 192, 198, 246, 288, 336, 342, 414, 420, 492, 546, 618, 624, 720, 750, 834, 888, 984, 990, 1122, 1128, 1224, 1302, 1410, 1476, 1620, 1626, 1746, 1836, 1980, 1986, 2166, 2172, 2316, 2442, 2586, 2592, 2784, 2826, 3006, 3120, 3288, 3294, 3510, 3600, 3792, 3918

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,2

LINKS

Vincenzo Librandi, [Table of n, a(n) for n = 1..5000][11]

Project Euler, [Problem 351: Hexagonal orchards][12].

FORMULA

a(n) = 6 * (C(n+1,2) - Sum_{i=1..n} phi(i)). - corrected by [Piyush Kumar][13] and [Robert Israel][14], Aug 26 2014

a(n) = 6*[A063985][15] (n). - [Jon Maiga][16], Jan 12 2019

MATHEMATICA

Table[6*Sum[k - EulerPhi[k], {k, n}], {n, 100}] (* [Jon Maiga][16], Jan 12 2019 *)

PROG

(PARI) for(i=1, 100, print1(6*(binomial(i+1, 2)-sum(X=1, i, eulerphi(X))), ", "))

CROSSREFS

Cf. [A063985][15].

Sequence in context: [A358526][17] [A069171][18] [A071611][19] * [A119500][20] [A260633][21] [A348632][22]

Adjacent sequences: [A216450][23] [A216451][24] [A216452][25] * [A216454][26] [A216455][27] [A216456][28]

KEYWORD

nonn

AUTHOR

[V. Raman][29], Sep 07 2012

STATUS

approved

[Lookup][3] [Welcome][30] [Wiki][31] [Register][32] [Music][33] [Plot 2][34] [Demos][35] [Index][36] [WebCam][37] [Contribute][38] [Format][39] [Style Sheet][40] [Transforms][41] [Superseeker][42] [Recents][43]

[The OEIS Community][44]

Maintained by [The OEIS Foundation Inc.][45]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][46]


## Links

[1]: /login?redirect=%2fA216453
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A216453/list
[5]: /A216453/graph
[6]: /search?q=A216453+-id:A216453
[7]: /A216453/listen
[8]: /history?seq=A216453
[9]: /search?q=id:A216453&fmt=text
[10]: /A216453/internal
[11]: /A216453/b216453.txt
[12]: http://projecteuler.net/problem=351
[13]: /wiki/User:Piyush_Kumar
[14]: /wiki/User:Robert_Israel
[15]: /A063985
[16]: /wiki/User:Jon_Maiga
[17]: /A358526
[18]: /A069171
[19]: /A071611
[20]: /A119500
[21]: /A260633
[22]: /A348632
[23]: /A216450
[24]: /A216451
[25]: /A216452
[26]: /A216454
[27]: /A216455
[28]: /A216456
[29]: /wiki/User:V._Raman
[30]: /wiki/Welcome
[31]: /wiki/Main_Page
[32]: /wiki/Special:RequestAccount
[33]: /play.html
[34]: /plot2.html
[35]: /demo1.html
[36]: /wiki/Index_to_OEIS
[37]: /webcam
[38]: /Submit.html
[39]: /eishelp2.html
[40]: /wiki/Style_Sheet
[41]: /transforms.html
[42]: /ol.html
[43]: /recent
[44]: /community.html
[45]: http://oeisf.org
[46]: /wiki/Legal_Documents
