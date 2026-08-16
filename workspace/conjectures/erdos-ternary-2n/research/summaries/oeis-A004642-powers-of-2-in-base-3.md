> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A004642-powers-of-2-in-base-3.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A004642 | converted from HTML -->

A004642 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A004642 - OEIS] [3]

A004642

Powers of 2 written in base 3.

23

1, 2, 11, 22, 121, 1012, 2101, 11202, 100111, 200222, 1101221, 2210212, 12121201, 102020102, 211110211, 1122221122, 10022220021, 20122210112, 111022121001, 222122012002, 1222021101011, 10221112202022, 21220002111121, 120210012000012, 1011120101000101, 2100010202000202

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,2

COMMENTS

When n is odd, a(n) ends in 1, and when n is even, a(n) ends in 2, since 2^n is congruent to 1 mod 3 when n is odd and to 2 mod 3 when n is even. - [Alonso del Arte][11] Dec 11 2009

Sloane (1973) conjectured a(n) always has a 0 between the most and least significant digits if n > 15 (see [A102483][12] and [A346497][13]).

Erdős (1978) conjectured that for n > 8 a(n) has at least one 2 (see link to Terry Tao's blog). - [Dmitry Kamenetsky][14], Jan 10 2017

REFERENCES

N. J. A. Sloane, The Persistence of a Number, J. Recr. Math. 6 (1973), 97-98.

LINKS

Vincenzo Librandi, [Table of n, a(n) for n = 0..1000][15]

Yagub N. Aliyev, [Digits of powers of 2 in ternary numeral system][16], Notes on Number Theory and Discrete Mathematics, Vol. 29, No. 3 (2023), 474-485.

Paul Erdős, [Some unconventional problems in number theory][17], Mathematics Magazine, Vol. 52, No. 2 (1979), pp. 67-70.

Donald L. Kreher and Douglas R. Stinson, [On min-base palindromic representations of powers of 2][18], arXiv:2401.07351 [math.NT], 2024. See Table 4 p. 10.

Jeffrey C. Lagarias, [Ternary Expansions of Powers of 2][19], Journal of the London Mathematical Society, Vol. 79, No. 3 (2009), pp. 562-588; [arXiv preprint][20], arXiv:math/0512006 [math.DS], 2005-2008.

Terry Tao, [The Collatz Conjecture, Littlewood-Offord theory, and powers of 2 and 3][21], 2011.

Eric Weisstein's World of Mathematics, [Ternary][22].

MATHEMATICA

Table[FromDigits[IntegerDigits[2^n, 3]], {n, 25}] (* [Alonso del Arte][11] Dec 11 2009 *)

PROG

(PARI) a(n)=fromdigits(digits(2^n, 3)) \\ [M. F. Hasler][23], Jun 23 2018

(Magma) [Seqint(Intseq(2^n, 3)): n in [0..30]]; // [G. C. Greubel][24], Sep 10 2018

CROSSREFS

Cf. [A000079][25]: powers of 2 written in base 10.

Cf. [A004643][26], ..., [A004655][27]: powers of 2 written in base 4, 5, ..., 16.

Cf. [A004656][28], [A004658][29], [A004659][30], ..., [A004663][31]: powers of 3 written in base 2, 4, 5, ..., 9.

Sequence in context: [A235609][32] [A376688][33] [A018351][34] * [A346497][13] [A390019][35] [A185545][36]

Adjacent sequences: [A004639][37] [A004640][38] [A004641][39] * [A004643][26] [A004644][40] [A004645][41]

KEYWORD

nonn, base, easy

AUTHOR

[N. J. A. Sloane][42]

STATUS

approved

[Lookup][3] [Welcome][43] [Wiki][44] [Register][45] [Music][46] [Plot 2][47] [Demos][48] [Index][49] [WebCam][50] [Contribute][51] [Format][52] [Style Sheet][53] [Transforms][54] [Superseeker][55] [Recents][56]

[The OEIS Community][57]

Maintained by [The OEIS Foundation Inc.][58]

Last modified August 16 01:43 EDT 2026. Contains 398340 sequences.

[License Agreements, Terms of Use, Privacy Policy][59]


## Links

[1]: /login?redirect=%2fA004642
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A004642/list
[5]: /A004642/graph
[6]: /search?q=A004642+-id:A004642
[7]: /A004642/listen
[8]: /history?seq=A004642
[9]: /search?q=id:A004642&fmt=text
[10]: /A004642/internal
[11]: /wiki/User:Alonso_del_Arte
[12]: /A102483
[13]: /A346497
[14]: /wiki/User:Dmitry_Kamenetsky
[15]: /A004642/b004642.txt
[16]: https://doi.org/10.7546/nntdm.2023.29.3.474-485
[17]: https://www.jstor.org/stable/2689842
[18]: https://arxiv.org/pdf/2401.07351
[19]: https://doi.org/10.1112/jlms/jdn080
[20]: https://arxiv.org/pdf/math/0512006
[21]: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/

*[excerpt ends; 758 characters not shown — see `research/sources/oeis-A004642-powers-of-2-in-base-3.full.md`]*
