> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A347925-gilbreath-polynomial-denominators.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A347925 | converted from HTML -->

A347925 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A347925 - OEIS] [3]

A347925

a(n) is the lowest common denominator of n-th Gilbreath polynomial.

2

1, 1, 1, 1, 1, 3, 6, 30, 180, 1260, 181440, 1814400, 19958400, 239500800, 3113510400, 43589145600, 43589145600, 653837184000, 177843714048000, 177843714048000, 1600593426432000, 1216451004088320000, 25545471085854720000, 25545471085854720000

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,6

COMMENTS

Let S=(p_1, ..., p_n) be the ordered sequence of the first n prime numbers. The n-th Gilbreath polynomial is defined as the polynomial P_n such that the x-th term of the upper bound Gilbreath sequence of S, U(S)_x, is U(S)_x=2^(n+x-1)+P_n where P_n = Sum_{i=1..n} T(n,i)*x^(i-1)/a(n).

LINKS

[Table of n, a(n) for n=1..24.][11]

Riccardo Gatti, [Gilbreath Sequences and Proof of Conditions for Gilbreath Conjecture][12], Preprints 2020, 2020030145.

Riccardo Gatti, [Program for the generation of the m-th Gilbreath polynomial calling GenMthGilbreathPolynomial(m)][13]

Leila Muney, [Holes in Valid-Extension Sets of Finite Gilbreath Sequences][14], arXiv:2606.23721 [math.CO], 2026. See p. 28 (Sect. 14.1).

Andrew M. Odlyzko, [Iterated absolute values of differences of consecutive primes][15], Math. Comp. 61 (1993), 373-380.

EXAMPLE

The lowest common denominator of P_6 is a(6)=3, in fact P_6 = (-57 - 55x - 15x^2 - 2x^3)/3. The x-th term of the upper bound Gilbreath sequence of S=(p_1, ..., p_6) = (2, 3, 5, 7, 11, 13) is U(S)_x = 2^(x+5) + (-57 - 55x - 15x^2 - 2x^3)/3.

PROG

(PARI) polynomialfit(data) = Pol(Vecrev(matsolve(matrix(#data, #data, i, j, i^(j-1)), data~))); \\ from [David A. Corneth][16]

isg(v, k) = {my(w = concat(v, k), vd = w); for (i=1, #w-1, vd = vector(#vd-1, k, abs(vd[k+1] - vd[k])); if (vd[1] != 1, return (0)); ); return (1); }

nextx(v) = {my(k = nextprime(nextprime(vecmax(v)+1)+1)); while (isg(v, k), k+=2); k-=2; }

a(n) = {my(vp = primes(n), v = List()); for (i=1, n, my(x = nextx(vp)); vp = concat(vp, x); listput(v, x); ); v = Vec(v); my(cp = Vecrev(polynomialfit(vector(#v, k, v[k] - 2^(k+n-1))))); lcm(apply(denominator, cp)); } \\ [Michel Marcus][17], Sep 20 2021

CROSSREFS

Cf. [A347924][18].

Sequence in context: [A157534][19] [A372024][20] [A133799][21] * [A262022][22] [A088436][23] [A088506][24]

Adjacent sequences: [A347922][25] [A347923][26] [A347924][18] * [A347926][27] [A347927][28] [A347928][29]

KEYWORD

nonn

AUTHOR

[Riccardo Gatti][30], Sep 20 2021

STATUS

approved

[Lookup][3] [Welcome][31] [Wiki][32] [Register][33] [Music][34] [Plot 2][35] [Demos][36] [Index][37] [WebCam][38] [Contribute][39] [Format][40] [Style Sheet][41] [Transforms][42] [Superseeker][43] [Recents][44]

[The OEIS Community][45]

Maintained by [The OEIS Foundation Inc.][46]

Last modified August 13 03:37 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][47]


## Links

[1]: /login?redirect=%2fA347925
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A347925/list
[5]: /A347925/graph
[6]: /search?q=A347925+-id:A347925
[7]: /A347925/listen
[8]: /history?seq=A347925
[9]: /search?q=id:A347925&fmt=text
[10]: /A347925/internal
[11]: /A347925/b347925.txt
[12]: https://www.preprints.org/manuscript/202003.0145
[13]: https://github.com/gttrcr/ResearchCode/blob/main/OEIS/A347925.cs
[14]: https://arxiv.org/abs/2606.23721
[15]: https://doi.org/10.1090/S0025-5718-1993-1182247-7
[16]: /wiki/User:David_A._Corneth
[17]: /wiki/User:Michel_Marcus
[18]: /A347924
[19]: /A157534
[20]: /A372024
[21]: /A133799
[22]: /A262022
[23]: /A088436
[24]: /A088506
[25]: /A347922
[26]: /A347923
[27]: /A347926
[28]: /A347927
[29]: /A347928
[30]: /wiki/User:Riccardo_Gatti
[31]: /wiki/Welcome
[32]: /wiki/Main_Page
[33]: /wiki/Special:RequestAccount
[34]: /play.html
[35]: /plot2.html

*[excerpt ends; 248 characters not shown — see `research/sources/oeis-A347925-gilbreath-polynomial-denominators.full.md`]*
