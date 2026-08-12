<!-- source: https://oeis.org/A115365 | converted from HTML -->

A115365 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A115365 - OEIS] [3]

A115365

Decimal expansion of smallest positive root of tan(x) = x.

18

4, 4, 9, 3, 4, 0, 9, 4, 5, 7, 9, 0, 9, 0, 6, 4, 1, 7, 5, 3, 0, 7, 8, 8, 0, 9, 2, 7, 2, 8, 0, 3, 2, 2, 0, 8, 2, 2, 1, 5, 5, 8, 3, 8, 7, 2, 2, 9, 0, 0, 4, 0, 8, 0, 2, 8, 9, 5, 8, 2, 3, 9, 6, 1, 9, 2, 6, 9, 5, 0, 3, 1, 4, 5, 9, 7, 1, 0, 4, 0, 9, 8, 7, 2, 9, 0, 5, 7, 8, 0, 9, 4, 5, 5, 8, 7, 9, 6, 9, 1, 5, 2, 1, 7, 6

( [list][4]; [constant][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,1

COMMENTS

Location (for x>0) of the first negative lobe of sinc(x) = sin(x)/x, where sinc(x) attains its absolute minimum of -0.217233628... The function sinc(x) is important in spectral theory (transient data truncation artifacts). - [Stanislav Sykora][12], Mar 05 2012

Also the first root of the sinc(3,x) function, that is, the radial component of the 3D Fourier transform of 3-dimensional unit sphere. Also the first root of the spherical Bessel function of the 1st kind, j_1(x). - [Stanislav Sykora][12], Nov 14 2013

Unique fixed point of the function arctan(x)+Pi, and this fixed point is attractive. - [Robert FERREOL][13], May 09 2023

Further roots (intersections of y=x with other branches of y=tan(x)) are at x=7.725251... = [A255272][14], x=10.9041216..., x=14.0661939..., x= 17.2207552.. etc. - [R. J. Mathar][15], Jul 11 2024

REFERENCES

M. Abramowitz, I. A. Stegun, Editors, Handbook of Mathematical Functions, Dover Publications, 1965, Chapter 10.

LINKS

G. C. Greubel, [Table of n, a(n) for n = 1..5000][16]

Mohammad K. Azarian, [On the Fixed Points of a Function and the Fixed Points of its Composite Functions][17], International Journal of Pure and Applied Mathematics, Vol. 46, No. 1, 2008, pp. 37-44. Mathematical Reviews, MR2433713 (2009c:65129), March 2009. Zentralblatt MATH, Zbl 1160.65015.

Mohammad K. Azarian, [Fixed Points of a Quadratic Polynomial, Problem 841][18], College Mathematics Journal, Vol. 38, No. 1, January 2007, p. 60.

Mohammad K. Azarian, [Solution to Fixed Points of a Quadratic Polynomial, Problem 841][19], College Mathematics Journal Vol. 39, No. 1, January 2008, pp. 66-67.

Stanislav Sykora, [K-Space Images of n-Dimensional Spheres and Generalized Sinc Functions][20]

Eric Weisstein's World of Mathematics, [Tangent][21]

Eric Weisstein's World of Mathematics, [Tanc Function][22]

[Index entries for transcendental numbers][23]

EXAMPLE

4.4934094579090641753...

MAPLE

Digits:=200; fsolve(x*cos(x)-sin(x), x, 4..5);

MATHEMATICA

RealDigits[FindRoot[Tan[x]==x, {x, 4}, WorkingPrecision->128][[1, 2]]][[1]] (* [Robert G. Wilson v][24], Mar 05 2012; corrected by [Harvey P. Dale][25], Mar 22 2012 *)

RealDigits[BesselJZero[3/2, 1], 10, 100][[1]] (* [Vladimir Reshetnikov][26], May 13 2016 *)

PROG

(PARI) solve(x=4, 4.5, tan(x)-x) \\ [Charles R Greathouse IV][27], Jun 10 2012

(PARI) besseljzero(3/2, 1) \\ [Charles R Greathouse IV][27], Jan 23 2025

CROSSREFS

Cf. [A102015][28] (continued fraction), [A213053][29] (amplitude at x).

Cf. [A062546][30], [A224196][31], [A207528][32], [A243108][33], [A245333][34].

Sequence in context: [A246668][35] [A021073][36] [A021961][37] * [A263491][38] [A272427][39] [A068340][40]

Adjacent sequences: [A115362][41] [A115363][42] [A115364][43] * [A115366][44] [A115367][45] [A115368][46]

KEYWORD

nonn, [cons][5]

AUTHOR

[Eric W. Weisstein][47], Jan 21 2006

STATUS

approved

[Lookup][3] [Welcome][48] [Wiki][49] [Register][50] [Music][51] [Plot 2][52] [Demos][53] [Index][54] [WebCam][55] [Contribute][56] [Format][57] [Style Sheet][58] [Transforms][59] [Superseeker][60] [Recents][61]

[The OEIS Community][62]

Maintained by [The OEIS Foundation Inc.][63]

Last modified August 12 13:20 EDT 2026. Contains 398245 sequences.

[License Agreements, Terms of Use, Privacy Policy][64]


## Links

[1]: /login?redirect=%2fA115365
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A115365/list
[5]: /A115365/constant
[6]: /A115365/graph
[7]: /search?q=A115365+-id:A115365
[8]: /A115365/listen
[9]: /history?seq=A115365
[10]: /search?q=id:A115365&fmt=text
[11]: /A115365/internal
[12]: /wiki/User:Stanislav_Sykora
[13]: /wiki/User:Robert_FERREOL
[14]: /A255272
[15]: /wiki/User:R._J._Mathar
[16]: /A115365/b115365.txt
[17]: http://www.ijpam.eu/contents/2008-46-1/3/3.pdf
[18]: https://www.jstor.org/stable/27646421
[19]: https://www.jstor.org/stable/27646572
[20]: https://doi.org/10.3247/SL2Math07.002
[21]: https://mathworld.wolfram.com/Tangent.html
[22]: https://mathworld.wolfram.com/TancFunction.html
[23]: /index/Tra#transcendental
[24]: /wiki/User:Robert_G._Wilson_v
[25]: /wiki/User:Harvey_P._Dale
[26]: /wiki/User:Vladimir_Reshetnikov
[27]: /wiki/User:Charles_R_Greathouse_IV
[28]: /A102015
[29]: /A213053
[30]: /A062546
[31]: /A224196
[32]: /A207528
[33]: /A243108
[34]: /A245333
[35]: /A246668
[36]: /A021073
[37]: /A021961
[38]: /A263491
[39]: /A272427
[40]: /A068340
[41]: /A115362
[42]: /A115363
[43]: /A115364
[44]: /A115366
[45]: /A115367
[46]: /A115368
[47]: /wiki/User:Eric_W._Weisstein
[48]: /wiki/Welcome
[49]: /wiki/Main_Page
[50]: /wiki/Special:RequestAccount
[51]: /play.html
[52]: /plot2.html
[53]: /demo1.html
[54]: /wiki/Index_to_OEIS
[55]: /webcam
[56]: /Submit.html
[57]: /eishelp2.html
[58]: /wiki/Style_Sheet
[59]: /transforms.html
[60]: /ol.html
[61]: /recent
[62]: /community.html
[63]: http://oeisf.org
[64]: /wiki/Legal_Documents
