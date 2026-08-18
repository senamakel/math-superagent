<!-- source: https://oeis.org/A213975 | converted from HTML -->

A213975 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A213975 - OEIS] [3]

A213975

List of subwords of [A003842][4] arranged in lexicographic order.

9

1, 2, 11, 12, 21, 112, 121, 211, 212, 1121, 1211, 1212, 2112, 2121, 11211, 11212, 12112, 12121, 21121, 21211, 112112, 112121, 121121, 121211, 211211, 211212, 212112, 1121121, 1121211, 1211211, 1211212, 1212112, 2112112, 2112121, 2121121, 11211212, 11212112

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,2

COMMENTS

The Fibonacci word [A003842][4] is a Sturmian word, which means that there are exactly n+1 different factors (or subwords) of length n for all n.

For another version of this sequence see the Noe link at [A003849][12] (and included below).

LINKS

Alois P. Heinz, [Table of n, a(n) for n = 1..10010][13]

Wai-Fong Chuan and Hui-Ling Ho, [Locating factors of the infinite Fibonacci word][14], Theoret. Comput. Sci. 349 (2005), no. 3, 429--442. MR2183167 (2007c:68115)

James D. Currie and Kalle Saari, [Least Periods of Factors of Infinite Words][15], RAIRO - Theoretical Informatics and Applications, January 2009, 43, pp. 165-178.

M. Lothaire, [Algebraic Combinatorics on Words][16], Cambridge, 2002; see Chap. 2.

F. Mignosi, A. Restivo, M. Sciortino, [Words and forbidden factors][17], WORDS (Rouen, 1999). Theoret. Comput. Sci. 273 (2002), no. 1-2, 99--117. MR1872445 (2002m:68096).

T. D. Noe, [The first 1652 subwords of A003849, including leading zeros.][18]

Kalle Saari, [Periods of factors of the Fibonacci word][19], Department of Mathematics and Turku Centre for Computer Science, University of Turku, 2001 4 Turku, Finland.

Kalle Saari, [Periods of factors of the Fibonacci word][20], in Proceedings of the Sixth International Conference on Words (WORDS’07). Institut de Mathématiques de Luminy (2007) 273-279.

Zhi-Xiong Wen and Zhi-Ying Wen, [Some properties of the singular words of the Fibonacci word][21], European J. Combin. 15 (1994), 587-598.

FORMULA

The list S(n), say, of words of length n in this sequence can be constructed recursively as follows.

There are two words of length 1, namely S(1)={1,2}.

The n+2 words in S(n+1) are obtained from the n+1 words in S(n) thus:

if u in S(n) is the reverse of a prefix of the Fibonacci word [A003842][4] then both u0 and u1 are in S(n+1), otherwise u in S(n) has a unique extension ux in S(n+1), where x is determined by the requirement that no right factor of ux is one of the forbidden words listed in [A214216][22].

For example, [A214216][22] contains both 22 and 111. So if u ends with 2 then (since 22 is forbidden), x=1 and u1 is in S(n+1), while if u ends with 11 then (since 111 is forbidden) x=2 and u2 is in S(n+1).

On the other hand, consider for example u=21121 in S(5), which is the reverse of the first 5 digits of [A003842][4]. Now both u1 and u2 are in S(6).

EXAMPLE

[A003842][4] begins 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, ... and we can see factors 1, 2, 11, 12, 21, but not 22.

MAPLE

S:= proc(n) option remember;

`if`(n<2, [2-n], [S(n-1)[], S(n-2)[]])

end:

T:= proc(n) local k, l, m, s;

for k while nops(S(k))<n do od;

do l:= S(k); m:= nops(l);

s:= {seq(parse(cat(l[i..i+n-1][])), i=1..m-n+1)};

if nops(s) = n+1 then break else k:= k+1 fi

od; sort([s[]])[]

end:

seq(T(n), n=1..10); # [Alois P. Heinz][23], Jul 04 2012

MATHEMATICA

nmax = 10;

seq[steps_] := seq[steps] = (S = SubstitutionSystem[{1 -> {1, 2}, 2 -> {1}}, {1}, steps] // Last; T[n_] := FromDigits /@ Union[Partition[S, n, 1]]; Table[T[n], {n, 1, nmax}] // Flatten);

seq[s = 1];

While[seq[s] != seq[s-1], s++];

seq[s] (* [Jean-François Alcover][24], Apr 28 2020 *)

CROSSREFS

Cf. [A003842][4], [A214207][25], [A214208][26], [A214209][27], [A214216][22], [A214217][28].

Sequence in context: [A114034][29] [A136970][30] [A136967][31] * [A137001][32] [A136996][33] [A238109][34]

Adjacent sequences: [A213972][35] [A213973][36] [A213974][37] * [A213976][38] [A213977][39] [A213978][40]

KEYWORD

nonn

AUTHOR

[N. J. A. Sloane][41], Jul 03 2012, Jul 10 2012

STATUS

approved

[Lookup][3] [Welcome][42] [Wiki][43] [Register][44] [Music][45] [Plot 2][46] [Demos][47] [Index][48] [WebCam][49] [Contribute][50] [Format][51] [Style Sheet][52] [Transforms][53] [Superseeker][54] [Recents][55]

[The OEIS Community][56]

Maintained by [The OEIS Foundation Inc.][57]

Last modified August 17 16:12 EDT 2026. Contains 398386 sequences.

[License Agreements, Terms of Use, Privacy Policy][58]


## Links

[1]: /login?redirect=%2fA213975
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A003842
[5]: /A213975/list
[6]: /A213975/graph
[7]: /search?q=A213975+-id:A213975
[8]: /A213975/listen
[9]: /history?seq=A213975
[10]: /search?q=id:A213975&fmt=text
[11]: /A213975/internal
[12]: /A003849
[13]: /A213975/b213975.txt
[14]: https://doi.org/10.1016/j.tcs.2005.08.033
[15]: http://www.numdam.org/item/ITA_2009__43_1_165_0/
[16]: http://www-igm.univ-mlv.fr/~berstel/Lothaire/
[17]: https://doi.org/10.1016/S0304-3975(00)00436-9
[18]: /A003849/a003849.txt
[19]: https://citeseerx.ist.psu.edu/pdf/226ad5ee4e916bbddb5775d36d4d126074ca1c27
[20]: https://www.semanticscholar.org/paper/PERIODS-OF-FACTORS-OF-THE-FIBONACCI-WORD-KALLE-Saari/226ad5ee4e916bbddb5775d36d4d126074ca1c27
[21]: https://doi.org/10.1006/eujc.1994.1060
[22]: /A214216
[23]: /wiki/User:Alois_P._Heinz
[24]: /wiki/User:Jean-François_Alcover
[25]: /A214207
[26]: /A214208
[27]: /A214209
[28]: /A214217
[29]: /A114034
[30]: /A136970
[31]: /A136967
[32]: /A137001
[33]: /A136996
[34]: /A238109
[35]: /A213972
[36]: /A213973
[37]: /A213974
[38]: /A213976
[39]: /A213977
[40]: /A213978
[41]: /wiki/User:N._J._A._Sloane
[42]: /wiki/Welcome
[43]: /wiki/Main_Page
[44]: /wiki/Special:RequestAccount
[45]: /play.html
[46]: /plot2.html
[47]: /demo1.html
[48]: /wiki/Index_to_OEIS
[49]: /webcam
[50]: /Submit.html
[51]: /eishelp2.html
[52]: /wiki/Style_Sheet
[53]: /transforms.html
[54]: /ol.html
[55]: /recent
[56]: /community.html
[57]: http://oeisf.org
[58]: /wiki/Legal_Documents
