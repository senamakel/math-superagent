<!-- source: https://oeis.org/A036262 | converted from HTML -->

A036262 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A036262 - OEIS] [3]

A036262

Array of numbers read by upward antidiagonals, arising from Gilbreath's conjecture: leading row lists the primes; the following rows give absolute values of differences of previous row.

45

2, 1, 3, 1, 2, 5, 1, 0, 2, 7, 1, 2, 2, 4, 11, 1, 2, 0, 2, 2, 13, 1, 2, 0, 0, 2, 4, 17, 1, 2, 0, 0, 0, 2, 2, 19, 1, 2, 0, 0, 0, 0, 2, 4, 23, 1, 2, 0, 0, 0, 0, 0, 2, 6, 29, 1, 0, 2, 2, 2, 2, 2, 2, 4, 2, 31, 1, 0, 0, 2, 0, 2, 0, 2, 0, 4, 6, 37, 1, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 4, 41, 1, 0, 0, 0, 0, 2, 0, 0, 0

( [list][4]; [table][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

0,1

COMMENTS

The conjecture is that the leading term is always 1.

Odlyzko has checked it for primes up to pi(10^13) = 3*10^11.

From [M. F. Hasler][12], Jun 02 2012: (Start)

The second column, omitting the initial 3, is given in [A089582][13]. The number of "0"s preceding the first term > 1 in the n-th row is given in [A213014][14]. The first term > 1 in any row must equal 2, else the conjecture is violated: Obviously all terms except for the first one are even. Thus, if the 2nd term in some row is > 2, it is >= 4, and the first term of the subsequent row is >= 3. If there is a positive number of zeros preceding a first term > 2 (thus >= 4), this "jump" will remain constant and "propagate" (in subsequent rows) to the beginning of the row, and the previously discussed case applies.

The previous statement can also be formulated as: Gilbreath's conjecture is equivalent to: [A036277][15] (n) > [A213014][14] (n)+2 for all n.

CAVEAT: While table [A036261][16] starts with the first absolute differences of the primes in its first row, the present sequence has the primes themselves in its uppermost row, which is sometimes referred to as "row 0". Thus, "first row" of this table [A036262][17] may either refer to row 1 (1,2,2,...), or to row 0 (2,3,5,7,...), while the latter might, however, as well be referred to "row 1 of [A036262][17] " in other sequences or papers.

(End)

From [Clark Kimberling][18], Nov 27 2022: (Start)

Suppose that S = (s(k)), for k >= 1, is a sequence of real numbers. For n >= 1, let g(1,n) = |s(n+1)-s(n)| and g(k,n) = |g(k-1,n+1) - g(k-1,n)| for k >= 2.

Call (g(k,n)) the Gilbreath array of S. Call the first column of this array the Gilbreath transform of S. Denote this transform by G(S), so that G(S) is the sequence (g(n,1)). If S is the sequence of primes, then the Gilbreath conjecture holds that G(S) consists exclusively of 1's. More generally, it appears that there are many S such that G(S) is eventually periodic. See [A358691][19] for conjectured examples. (End)

REFERENCES

R. K. Guy, Unsolved Problems Number Theory, A10.

H. L. Montgomery, Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis, Amer. Math. Soc., 1996, p. 208.

C. A. Pickover, The Math Book, Sterling, NY, 2009; see p. 410.

Paulo Ribenboim, The Little Book of Bigger Primes, Springer-Verlag NY 2004. See p. 192.

W. Sierpiński, L'induction incomplète dans la théorie des nombres, Scripta Math. 28 (1967), 5-13.

LINKS

T. D. Noe, [Table of n, a(n) for n = 0..5049][20]

Richard K. Guy, [The strong law of small numbers][21]. Amer. Math. Monthly 95 (1988), no. 8, 697-712. [Annotated scanned copy]

R. B. Killgrove and K. E. Ralston, [On a conjecture concerning the primes][22], Math. Comput. 13 (1959), 121-122.

Leila Muney, [Holes in Valid-Extension Sets of Finite Gilbreath Sequences][23], arXiv:2606.23721 [math.CO], 2026. See p. 28 (Sect. 14.1).

Andrew M. Odlyzko, [Iterated absolute values of differences of consecutive primes][24], Math. Comp. 61 (1993), 373-380.

F. Proth, [Sur la série des nombres premiers][25], Nouv. Corresp. Math., 4 (1878) 236-240.

W. Sierpiński, [L'induction incomplète dans la théorie des nombres][26], Bulletin de la Société des mathématiciens et physiciens de la R.P de Serbie, Vol XIII, 1-2 (1961), Beograd, Yougoslavie.

N. J. A. Sloane, [My favorite integer sequences][27], in Sequences and their Applications (Proceedings of SETA '98).

N. J. A. Sloane, New Gilbreath Conjectures, Sum and Erase, Dissecting Polygons, and Other New Sequences, Doron Zeilberger's Exper. Math. Seminar, Rutgers, Sep 14 2023: [Video][28], [Slides][29], [Updates][30]. (Mentions this sequence.)

Eric Weisstein's World of Mathematics, [Gilbreath's Conjecture][31].

[Index entries for sequences related to Gilbreath conjecture and transform][32]

FORMULA

T(0,k) = [A000040][33] (k). T(n,k) = |T(n-1,k+1) - T(n-1,k)|, n > 0. - [R. J. Mathar][34], Sep 19 2013

EXAMPLE

The array begins (conjecture is leading term is always 1):

2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101

1 2 2 4 2 4 2 4 6 2 6 4 2 4 6 6 2 6 4 2 6 4 6 8 4 2

1 0 2 2 2 2 2 2 4 4 2 2 2 2 0 4 4 2 2 4 2 2 2 4 2 2

1 2 0 0 0 0 0 2 0 2 0 0 0 2 4 0 2 0 2 2 0 0 2 2 0 0

1 2 0 0 0 0 2 2 2 2 0 0 2 2 4 2 2 2 0 2 0 2 0 2 0 0

1 2 0 0 0 2 0 0 0 2 0 2 0 2 2 0 0 2 2 2 2 2 2 2 0 8

1 2 0 0 2 2 0 0 2 2 2 2 2 0 2 0 2 0 0 0 0 0 0 2 8 8

1 2 0 2 0 2 0 2 0 0 0 0 2 2 2 2 2 0 0 0 0 0 2 6 0 8

1 2 2 2 2 2 2 2 0 0 0 2 0 0 0 0 2 0 0 0 0 2 4 6 8 6

1 0 0 0 0 0 0 2 0 0 2 2 0 0 0 2 2 0 0 0 2 2 2 2 2 4

...

MAPLE

[A036262][17]:= proc(n, k)

option remember ;

if n = 0 then

ithprime(k) ;

else

abs(procname(n-1, k+1)-procname(n-1, k)) ;

end if;

end proc:

seq(seq( [A036262][17] (d-k, k), k=1..d), d=1..13) ; # [R. J. Mathar][34], May 10 2023

MATHEMATICA

max = 14; triangle = NestList[ Abs[ Differences[#]] &, Prime[ Range[max]], max]; Flatten[ Table[ triangle[[n - k + 1, k]], {n, 1, max}, {k, 1, n}]] (* [Jean-François Alcover][35], Nov 04 2011 *)

PROG

(Haskell)

a036262 n k = delta !! (n - k) !! (k - 1) where delta = iterate

(\pds -> zipWith (\x y -> abs (x - y)) (tail pds) pds) a000040_list

-- [Reinhard Zumkeller][36], Jan 23 2011

CROSSREFS

Cf. [A001223][37], [A036261][16], [A036277][15], [A054977][38], [A222310][39], [A358691][19], [A089582][13] (2nd col).

See [A255483][40] for an interesting generalization.

Sequence in context: [A380508][41] [A257918][42] [A257912][43] * [A080521][44] [A169613][45] [A176572][46]

Adjacent sequences: [A036259][47] [A036260][48] [A036261][16] * [A036263][49] [A036264][50] [A036265][51]

KEYWORD

[tabl][5], easy, nice, nonn

AUTHOR

[N. J. A. Sloane][52]

EXTENSIONS

More terms from Antonio G. Astudillo (afg_astudillo(AT)lycos.com), Mar 23 2003

Definition edited by [N. J. A. Sloane][52], May 03 2023

STATUS

approved

[Lookup][3] [Welcome][53] [Wiki][54] [Register][55] [Music][56] [Plot 2][57] [Demos][58] [Index][59] [WebCam][60] [Contribute][61] [Format][62] [Style Sheet][63] [Transforms][64] [Superseeker][65] [Recents][66]

[The OEIS Community][67]

Maintained by [The OEIS Foundation Inc.][68]

Last modified August 13 02:40 EDT 2026. Contains 398269 sequences.

[License Agreements, Terms of Use, Privacy Policy][69]


## Links

[1]: /login?redirect=%2fA036262
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A036262/list
[5]: /A036262/table
[6]: /A036262/graph
[7]: /search?q=A036262+-id:A036262
[8]: /A036262/listen
[9]: /history?seq=A036262
[10]: /search?q=id:A036262&fmt=text
[11]: /A036262/internal
[12]: /wiki/User:M._F._Hasler
[13]: /A089582
[14]: /A213014
[15]: /A036277
[16]: /A036261
[17]: /A036262
[18]: /wiki/User:Clark_Kimberling
[19]: /A358691
[20]: /A036262/b036262.txt
[21]: /A005165/a005165.pdf
[22]: https://doi.org/10.1090/S0025-5718-59-99262-2
[23]: https://arxiv.org/abs/2606.23721
[24]: https://doi.org/10.1090/S0025-5718-1993-1182247-7
[25]: http://resolver.sub.uni-goettingen.de/purl?PPN598948236_0004
[26]: http://resolver.sub.uni-goettingen.de/purl?PPN311570321_0013
[27]: http://neilsloane.com/doc/sg.txt
[28]: https://vimeo.com/866583736?share=copy
[29]: http://neilsloane.com/doc/EMSep2023.pdf
[30]: http://neilsloane.com/doc/EMSep2023.Updates.txt
[31]: https://mathworld.wolfram.com/GilbreathsConjecture.html
[32]: /index/Ge#Gilbreath
[33]: /A000040
[34]: /wiki/User:R._J._Mathar
[35]: /wiki/User:Jean-François_Alcover
[36]: /wiki/User:Reinhard_Zumkeller
[37]: /A001223
[38]: /A054977
[39]: /A222310
[40]: /A255483
[41]: /A380508
[42]: /A257918
[43]: /A257912
[44]: /A080521
[45]: /A169613
[46]: /A176572
[47]: /A036259
[48]: /A036260
[49]: /A036263
[50]: /A036264
[51]: /A036265
[52]: /wiki/User:N._J._A._Sloane
[53]: /wiki/Welcome
[54]: /wiki/Main_Page
[55]: /wiki/Special:RequestAccount
[56]: /play.html
[57]: /plot2.html
[58]: /demo1.html
[59]: /wiki/Index_to_OEIS
[60]: /webcam
[61]: /Submit.html
[62]: /eishelp2.html
[63]: /wiki/Style_Sheet
[64]: /transforms.html
[65]: /ol.html
[66]: /recent
[67]: /community.html
[68]: http://oeisf.org
[69]: /wiki/Legal_Documents
