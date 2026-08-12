> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-a328227-circle-critical-speed.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A328227 | converted from HTML -->

A328227 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A328227 - OEIS] [3]

A328227

Decimal expansion of positive solution to x^2 = 1 + (Pi + arccos(1/x))^2.

1

4, 6, 0, 3, 3, 3, 8, 8, 4, 8, 7, 5, 1, 7, 0, 0, 3, 5, 2, 5, 5, 6, 5, 8, 2, 0, 2, 9, 1, 0, 3, 0, 1, 6, 5, 1, 3, 0, 6, 7, 3, 9, 7, 1, 3, 4, 1, 6, 0, 5, 3, 2, 3, 4, 6, 0, 3, 9, 4, 3, 0, 1, 1, 5, 4, 3, 8, 4, 5, 8, 7, 3, 1, 9, 6, 5, 9, 7, 0, 9, 9, 8, 7, 1, 6, 5, 4, 6, 9, 9, 7, 2, 2, 7, 2

( [list][4]; [constant][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,1

COMMENTS

We are in a rowboat on a circular lake, starting at the center. At the edge of the lake is a mean goblin. He can run k times as fast as we can row. This is the minimum value of k such that we will not be able to escape.

From [Rian Hunter][12], Jun 16 2021: (Start)

For a spirograph defined by complex function z = p * e^(-i * b * t) + b * e^(i * t), this is the value of p as b->oo such that each petal is tangent to the next one.

If we consider the set of all right triangles such that their tangent value is equal to the opposite angle in radians, this value is equal to the negative secant of the right triangle from that set with the smallest nonzero opposite angle. (End)

The envelope of the t*x = sin(t*y) family of curves contains the set of y = (-1)^n*k_n*x straight lines (n > 0), where k_n is the solution of (n*Pi + arccos(1/k))^2 + 1 = k^2. This entry is k_1. See illustration, section Links. - [Luc Rousseau][13], Mar 11 2022

Maximum negative value of x/sin(x). - [Andrew Slattery][14], Jun 29 2022

LINKS

[Table of n, a(n) for n=1..95.][15]

Rian Hunter, [The Number Hiding Inside the Spirograph][16].

IBM Research, [Ponder This Challenge - May 2001][17].

Luc Rousseau, [A328227 viewed as the |slope| of an envelope][18].

FORMULA

x=-sec(y), where decimal expansion of y is [A115365][19].

Alternatively, x=sqrt(y^2+1).

EXAMPLE

4.6033388487517003525565820291030165130673971341605323460394301154384587319659...

MATHEMATICA

NSolve[x^2==1+(Pi+ArcCos[1/x])^2, x, Reals, WorkingPrecision->100]

PROG

(PARI) solve(x=4, 5, 1 + (Pi+acos(1/x))^2 - x^2) \\ [Michel Marcus][20], Oct 08 2019

CROSSREFS

Cf. [A115365][19].

Equals 1/ [A213053][21].

Sequence in context: [A397203][22] [A096256][23] [A319091][24] * [A059750][25] [A372919][26] [A243983][27]

Adjacent sequences: [A328224][28] [A328225][29] [A328226][30] * [A328228][31] [A328229][32] [A328230][33]

KEYWORD

nonn, [cons][5]

AUTHOR

[Jack Zhang][34], Oct 08 2019

STATUS

approved

[Lookup][3] [Welcome][35] [Wiki][36] [Register][37] [Music][38] [Plot 2][39] [Demos][40] [Index][41] [WebCam][42] [Contribute][43] [Format][44] [Style Sheet][45] [Transforms][46] [Superseeker][47] [Recents][48]

[The OEIS Community][49]

Maintained by [The OEIS Foundation Inc.][50]

Last modified August 12 13:20 EDT 2026. Contains 398245 sequences.

[License Agreements, Terms of Use, Privacy Policy][51]


## Links

[1]: /login?redirect=%2fA328227
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A328227/list
[5]: /A328227/constant
[6]: /A328227/graph
[7]: /search?q=A328227+-id:A328227
[8]: /A328227/listen
[9]: /history?seq=A328227
[10]: /search?q=id:A328227&fmt=text
[11]: /A328227/internal
[12]: /wiki/User:Rian_Hunter
[13]: /wiki/User:Luc_Rousseau
[14]: /wiki/User:Andrew_Slattery
[15]: /A328227/b328227.txt
[16]: https://thelig.ht/petalnumbers/part2.html
[17]: https://www.research.ibm.com/haifa/ponderthis/challenges/May2001.html
[18]: /A328227/a328227.png
[19]: /A115365
[20]: /wiki/User:Michel_Marcus
[21]: /A213053
[22]: /A397203
[23]: /A096256
[24]: /A319091
[25]: /A059750
[26]: /A372919
[27]: /A243983
[28]: /A328224
[29]: /A328225
[30]: /A328226
[31]: /A328228
[32]: /A328229
[33]: /A328230
[34]: /wiki/User:Jack_Zhang
[35]: /wiki/Welcome
[36]: /wiki/Main_Page
[37]: /wiki/Special:RequestAccount
[38]: /play.html

*[excerpt ends; 266 characters not shown — see `research/sources/oeis-a328227-circle-critical-speed.full.md`]*
