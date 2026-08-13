<!-- source: https://oeis.org/A213014 | converted from HTML -->

A213014 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A213014 - OEIS] [3]

A213014

Number of zeros following the initial 1 in n-th absolute difference of primes.

3

0, 1, 0, 0, 0, 0, 0, 0, 6, 5, 4, 3, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 1, 0, 3, 2, 1, 0, 0, 6, 5, 4, 3, 2, 1, 0, 0, 1, 0, 0, 1, 0, 2, 1, 0, 1, 0, 0, 0, 0, 6, 5, 4, 3, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 1, 0, 5, 4, 3, 2, 1, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 3, 2, 1, 0, 0

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,9

COMMENTS

Related to Gilbreath's conjecture: number of "0"s preceding the first term > 1 in the n-th row of the table [A036261][11] (= row n of the table [A036262][12] which starts with row 0).

Gilbreath's conjecture would be violated if the initial 1 would not always be followed by some number (>= 0) of "0"s and then a "2" as the first term > 1. See also [A089582][13].

LINKS

Robert Israel, [Table of n, a(n) for n = 1..10000][14]

MAPLE

L:= [seq(ithprime(i), i=1..120)]:

for i from 1 to 100 do

L:= map(abs, L[2..-1]-L[1..-2]);

for j from 2 do

if L[j] <> 0 then R[i]:= j-2; break fi;

od;

od:

seq(R[i], i=1..100); # [Robert Israel][15], Dec 13 2023

PROG

(PARI) my( p=primes(150), D(v)=vecextract(v, "^1")-vecextract(v, "^-1")); while(p=abs(D(p)), for(i=2, #p, p[i] & !print1(i-2", ") & next(2)); break)

CROSSREFS

Sequence in context: [A263879][16] [A085664][17] [A154007][18] * [A022962][19] [A023448][20] [A307337][21]

Adjacent sequences: [A213011][22] [A213012][23] [A213013][24] * [A213015][25] [A213016][26] [A213017][27]

KEYWORD

nonn

AUTHOR

[M. F. Hasler][28], Jun 02 2012

STATUS

approved

[Lookup][3] [Welcome][29] [Wiki][30] [Register][31] [Music][32] [Plot 2][33] [Demos][34] [Index][35] [WebCam][36] [Contribute][37] [Format][38] [Style Sheet][39] [Transforms][40] [Superseeker][41] [Recents][42]

[The OEIS Community][43]

Maintained by [The OEIS Foundation Inc.][44]

Last modified August 13 04:40 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][45]


## Links

[1]: /login?redirect=%2fA213014
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A213014/list
[5]: /A213014/graph
[6]: /search?q=A213014+-id:A213014
[7]: /A213014/listen
[8]: /history?seq=A213014
[9]: /search?q=id:A213014&fmt=text
[10]: /A213014/internal
[11]: /A036261
[12]: /A036262
[13]: /A089582
[14]: /A213014/b213014.txt
[15]: /wiki/User:Robert_Israel
[16]: /A263879
[17]: /A085664
[18]: /A154007
[19]: /A022962
[20]: /A023448
[21]: /A307337
[22]: /A213011
[23]: /A213012
[24]: /A213013
[25]: /A213015
[26]: /A213016
[27]: /A213017
[28]: /wiki/User:M._F._Hasler
[29]: /wiki/Welcome
[30]: /wiki/Main_Page
[31]: /wiki/Special:RequestAccount
[32]: /play.html
[33]: /plot2.html
[34]: /demo1.html
[35]: /wiki/Index_to_OEIS
[36]: /webcam
[37]: /Submit.html
[38]: /eishelp2.html
[39]: /wiki/Style_Sheet
[40]: /transforms.html
[41]: /ol.html
[42]: /recent
[43]: /community.html
[44]: http://oeisf.org
[45]: /wiki/Legal_Documents
