> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A260683-number-of-2s-in-2n-base3.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A260683 | converted from HTML -->

A260683 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A260683 - OEIS] [3]

A260683

Number of 2's in the expansion of 2^n in base 3.

4

0, 1, 0, 2, 1, 1, 1, 2, 0, 4, 2, 4, 3, 3, 2, 6, 5, 5, 3, 7, 4, 7, 5, 4, 1, 5, 2, 8, 8, 7, 9, 9, 8, 7, 7, 8, 4, 6, 8, 9, 11, 11, 7, 11, 10, 8, 9, 8, 8, 10, 11, 16, 13, 10, 9, 12, 13, 16, 12, 13, 15, 15, 11, 15, 16, 14, 14, 12, 14, 15, 14, 16, 11, 18, 11, 17, 10

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

0,4

COMMENTS

Erdős conjectures that a(n) > 0 for n > 8.

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, B33. [Does not seem to be in section B33.]

LINKS

Robert Israel, [Table of n, a(n) for n = 0..10000][11]

Paul Erdős, [Some unconventional problems in number theory][12], Mathematics Magazine, Vol. 52, No. 2 (1979), pp. 67-70.

FORMULA

a(n) = [A020915][13] (n) - [A104320][14] (n) - [A036461][15] (n). - [Altug Alkan][16], Nov 15 2015

a(n) = [A081603][17] ( [A000079][18] (n)). - [Michel Marcus][19], Dec 03 2015

EXAMPLE

For n=5, the expansion of 2^n in number base 3 is 1012, thus: a(n)=1

For n=10, the expansion of 2^n in number base 3 is 1101221, thus: a(n)=2

MAPLE

seq(numboccur(2, convert(2^n, base, 3)), n=0..100); # [Robert Israel][20], Nov 15 2015

MATHEMATICA

S={}; n=-1; While[n<150, n++; A=IntegerDigits[2^n, 3]; k=Count[A, 2]; AppendTo[S, k]]; S

PROG

(PARI) c(k, d, b) = {my(c=0, f); while (k>b-1, f=k-b*(k\b); if (f==d, c++); k\=b); if (k==d, c++); return(c)}

for(n=0, 300, print1(c(2^n, 2, 3)", ")) \\ [Altug Alkan][16], Nov 15 2015

(PARI) a(n) = #select(x->(x==2), digits(2^n, 3)); \\ [Michel Marcus][19], Nov 28 2018

(PARI) a(n) = hammingweight(digits(2^n, 3)\2); \\ [Ruud H.G. van Tol][21], May 09 2024

(Perl) use ntheory ":all"; sub a260683 { scalar grep { $_==2 } todigits(vecprod((2) x shift), 3) } # [Dana Jacobsen][22], Aug 16 2016

CROSSREFS

Cf. [A004642][23] (2^n in base 3), [A020915][13] (number of terms), [A036461][15] (number of 1's), [A104320][14] (number of 0's).

Cf. [A000108][24] (conjecture that [A000108][24] (n) is 6m+1 only for n = 0, 1 and 5 follows from Erdős's one).

Cf. [A005836][25] (for numbers with no 2 in base 3).

Sequence in context: [A163819][26] [A301734][27] [A281185][28] * [A337683][29] [A362451][30] [A092673][31]

Adjacent sequences: [A260680][32] [A260681][33] [A260682][34] * [A260684][35] [A260685][36] [A260686][37]

KEYWORD

base, easy, nonn

AUTHOR

[Emmanuel Vantieghem][38], Nov 15 2015

STATUS

approved

[Lookup][3] [Welcome][39] [Wiki][40] [Register][41] [Music][42] [Plot 2][43] [Demos][44] [Index][45] [WebCam][46] [Contribute][47] [Format][48] [Style Sheet][49] [Transforms][50] [Superseeker][51] [Recents][52]

[The OEIS Community][53]

Maintained by [The OEIS Foundation Inc.][54]

Last modified August 16 01:43 EDT 2026. Contains 398340 sequences.

[License Agreements, Terms of Use, Privacy Policy][55]


## Links

[1]: /login?redirect=%2fA260683
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A260683/list
[5]: /A260683/graph
[6]: /search?q=A260683+-id:A260683
[7]: /A260683/listen
[8]: /history?seq=A260683
[9]: /search?q=id:A260683&fmt=text
[10]: /A260683/internal
[11]: /A260683/b260683.txt
[12]: https://www.jstor.org/stable/2689842
[13]: /A020915
[14]: /A104320
[15]: /A036461
[16]: /wiki/User:Altug_Alkan
[17]: /A081603
[18]: /A000079
[19]: /wiki/User:Michel_Marcus
[20]: /wiki/User:Robert_Israel
[21]: /wiki/User:Ruud_H.G._van_Tol
[22]: /wiki/User:Dana_Jacobsen
[23]: /A004642
[24]: /A000108
[25]: /A005836
[26]: /A163819
[27]: /A301734
[28]: /A281185
[29]: /A337683
[30]: /A362451
[31]: /A092673
[32]: /A260680
[33]: /A260681
[34]: /A260682
[35]: /A260684
[36]: /A260685
[37]: /A260686
[38]: /wiki/User:Emmanuel_Vantieghem
[39]: /wiki/Welcome
[40]: /wiki/Main_Page
[41]: /wiki/Special:RequestAccount
[42]: /play.html
[43]: /plot2.html
[44]: /demo1.html

*[excerpt ends; 230 characters not shown — see `research/sources/oeis-A260683-number-of-2s-in-2n-base3.full.md`]*
