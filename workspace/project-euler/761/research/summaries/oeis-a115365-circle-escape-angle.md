> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-a115365-circle-escape-angle.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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


*[excerpt ends; 1625 characters not shown — see `research/sources/oeis-a115365-circle-escape-angle.full.md`]*
