> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A347924-gilbreath-polynomials.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A347924 | converted from HTML -->

A347924 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A347924 - OEIS] [3]

A347924

Triangle read by rows where row m is the m-th Gilbreath polynomial and column n is the numerator of the coefficient of the n-th degree term.

2

1, 1, 0, 1, 0, 0, -1, -3, -1, 0, -5, -5, -1, 0, 0, -57, -55, -15, -2, 0, 0, -282, -232, -77, -14, -1, 0, 0, -3270, -2554, -850, -175, -20, -1, 0, 0, -41940, -30948, -10654, -2325, -325, -27, -1, 0, 0, -608580, -437772, -152180, -34174, -5285, -553, -35, -1, 0, 0

( [list][4]; [table][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,8

COMMENTS

Let S=(p_1, ..., p_m) be the ordered sequence of the first m prime numbers. The m-th Gilbreath polynomial is defined as the polynomial P_m such that the x-th term of the upper bound Gilbreath sequence of S, U(S)_x, is U(S)_x = 2^(m+x-1) + P_m where P_m = Sum_{n=1..m} T(m,n)*x^(n-1)/ [A347925][12] (m).

The values T(m,1), ..., T(m,n) are the numerators of the coefficients of the (n-th)-degree terms of the m-th Gilbreath polynomial.

LINKS

[Table of n, a(n) for n=1..55.][13]

Riccardo Gatti, [Gilbreath Sequences and Proof of Conditions for Gilbreath Conjecture][14], Preprints 2020, 2020030145.

Riccardo Gatti, [Program for the generation of the m-th Gilbreath polynomial calling GenMthGilbreathPolynomial(m)][15]

Leila Muney, [Holes in Valid-Extension Sets of Finite Gilbreath Sequences][16], arXiv:2606.23721 [math.CO], 2026. See p. 28 (Sect. 14.1).

Andrew M. Odlyzko, [Iterated absolute values of differences of consecutive primes][17], Math. Comp. 61 (1993), 373-380.

EXAMPLE

Consider the triangle T(m,n) of the first terms of the sequence:

m\n 1 2 3 4 5 6 7 8

1 1

2 1 0

3 1 0 0

4 -1 -3 -1 0

5 -5 -5 -1 0 0

6 -57 -55 -15 -2 0 0

7 -282 -232 -77 -14 -1 0 0

...

The terms associated to P_6 are -57, -55, -15, -2, 0, 0. The numerators of coefficients of P_6 are in order of degree of the term of the polynomial: -57 for the term of degree 0, -55 for the term of degree 1 and so on until 0 for the terms of degree 4 and 5. Hence P_6 = (-57 - 55x - 15x^2 - 2x^3)/3, where [A347925][12] (6)=3, in fact the x-th term of the upper bound Gilbreath sequence of S=(p_1, ..., p_6) = (2, 3, 5, 7, 11, 13) is U(S)_x = 2^(x+5) + (-57 - 55x - 15x^2 - 2x^3)/3.

PROG

(PARI) polynomialfit(data) = Pol(Vecrev(matsolve(matrix(#data, #data, i, j, i^(j-1)), data~))); \\ from [David A. Corneth][18]

isg(v, k) = {my(w = concat(v, k), vd = w); for (i=1, #w-1, vd = vector(#vd-1, k, abs(vd[k+1] - vd[k])); if (vd[1] != 1, return (0)); ); return (1); }

nextx(v) = {my(k = nextprime(nextprime(vecmax(v)+1)+1)); while (isg(v, k), k+=2); k-=2; }

row(n) = {my(vp = primes(n), v = List()); for (i=1, n, my(x = nextx(vp)); vp = concat(vp, x); listput(v, x); ); v = Vec(v); my(cp = Vecrev(polynomialfit(vector(#v, k, v[k] - 2^(k+n-1))))); my(k = lcm(apply(denominator, cp))); while(#cp != n, cp = concat(cp, 0)); cp *= k; } \\ [Michel Marcus][19], Sep 20 2021

CROSSREFS

Cf. [A347925][12].

Sequence in context: [A362564][20] [A324664][21] [A011084][22] * [A341103][23] [A021326][24] [A362885][25]

Adjacent sequences: [A347921][26] [A347922][27] [A347923][28] * [A347925][12] [A347926][29] [A347927][30]

KEYWORD

sign, frac, [tabl][5]

AUTHOR

[Riccardo Gatti][31], Sep 20 2021

STATUS

approved

[Lookup][3] [Welcome][32] [Wiki][33] [Register][34] [Music][35] [Plot 2][36] [Demos][37] [Index][38] [WebCam][39] [Contribute][40] [Format][41] [Style Sheet][42] [Transforms][43] [Superseeker][44] [Recents][45]

[The OEIS Community][46]

Maintained by [The OEIS Foundation Inc.][47]

Last modified August 13 03:37 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][48]


## Links

[1]: /login?redirect=%2fA347924
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A347924/list
[5]: /A347924/table
[6]: /A347924/graph

*[excerpt ends; 1027 characters not shown — see `research/sources/oeis-A347924-gilbreath-polynomials.full.md`]*
