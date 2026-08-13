<!-- source: https://oeis.org/A057447 | converted from HTML -->

A057447 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A057447 - OEIS] [3]

A057447

a(n+1) = next prime such that a(n+1)-1 | (a(1)...a(n))^3.

6

2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 101, 107, 109, 127, 131, 139, 149, 151, 157, 167, 173, 179, 181, 191, 197, 199, 211, 223, 229, 233, 251, 263, 269, 271, 277, 281, 283, 293, 311, 313, 317, 331, 347, 349, 359

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

No prime of the form a*b^k + 1, with a > 0, b > 1 and k > 3 (including those in [A037896][11]) belongs to the sequence. - [Mauro Fiorentini][12], Aug 09 2023

LINKS

T. D. Noe, [Table of n, a(n) for n = 1..1000][13]

MATHEMATICA

NextPrime[ n_Integer ] := Module[ {k = n + 1}, While[ ! PrimeQ[ k ], k++ ]; Return[ k ] ]; f[ n_List ] := (a = n; b = Apply[ Times, a^3 ]; d = NextPrime[ a[[ -1 ]] ]; While[ ! IntegerQ[ b/(d - 1) ] && d < b+2, d = NextPrime[ d ] ]; AppendTo[ a, d ]; Return[ a ]); Nest[ f, {2}, 75 ]

CROSSREFS

Cf. [A007459][14], [A037896][11], [A057448][15].

Sequence in context: [A181160][16] [A316968][17] [A105049][18] * [A095074][19] [A042987][20] [A089189][21]

Adjacent sequences: [A057444][22] [A057445][23] [A057446][24] * [A057448][15] [A057449][25] [A057450][26]

KEYWORD

nonn

AUTHOR

[Robert G. Wilson v][27], Sep 25 2000

STATUS

approved

[Lookup][3] [Welcome][28] [Wiki][29] [Register][30] [Music][31] [Plot 2][32] [Demos][33] [Index][34] [WebCam][35] [Contribute][36] [Format][37] [Style Sheet][38] [Transforms][39] [Superseeker][40] [Recents][41]

[The OEIS Community][42]

Maintained by [The OEIS Foundation Inc.][43]

Last modified August 13 06:02 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][44]


## Links

[1]: /login?redirect=%2fA057447
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A057447/list
[5]: /A057447/graph
[6]: /search?q=A057447+-id:A057447
[7]: /A057447/listen
[8]: /history?seq=A057447
[9]: /search?q=id:A057447&fmt=text
[10]: /A057447/internal
[11]: /A037896
[12]: /wiki/User:Mauro_Fiorentini
[13]: /A057447/b057447.txt
[14]: /A007459
[15]: /A057448
[16]: /A181160
[17]: /A316968
[18]: /A105049
[19]: /A095074
[20]: /A042987
[21]: /A089189
[22]: /A057444
[23]: /A057445
[24]: /A057446
[25]: /A057449
[26]: /A057450
[27]: /wiki/User:Robert_G._Wilson_v
[28]: /wiki/Welcome
[29]: /wiki/Main_Page
[30]: /wiki/Special:RequestAccount
[31]: /play.html
[32]: /plot2.html
[33]: /demo1.html
[34]: /wiki/Index_to_OEIS
[35]: /webcam
[36]: /Submit.html
[37]: /eishelp2.html
[38]: /wiki/Style_Sheet
[39]: /transforms.html
[40]: /ol.html
[41]: /recent
[42]: /community.html
[43]: http://oeisf.org
[44]: /wiki/Legal_Documents
