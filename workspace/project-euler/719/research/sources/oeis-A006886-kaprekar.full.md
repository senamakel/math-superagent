<!-- source: https://oeis.org/A006886 | converted from HTML -->

A006886 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A006886 - OEIS] [3]

A006886

Kaprekar numbers: positive numbers n such that n = q+r and n^2 = q*10^m+r, for some m >= 1, q >= 0 and 0 <= r < 10^m, with n != 10^a, a >= 1.
(Formerly M4625)

34

1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999, 17344, 22222, 38962, 77778, 82656, 95121, 99999, 142857, 148149, 181819, 187110, 208495, 318682, 329967, 351352, 356643, 390313, 461539, 466830, 499500, 500500, 533170

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,2

COMMENTS

4879 and 5292 are in this sequence but not in [A053816][11].

Digital root is either 1 or 9. - [Ezhilarasu Velayutham][12], Jul 27 2019

Named after the Indian recreational mathematician Dattatreya Ramchandra Kaprekar (1905-1986). - [Amiram Eldar][13], Jun 19 2021

The term a(11) = 4879 is the first not in subsequence [A053816][11]. - [M. F. Hasler][14], Mar 28 2025

REFERENCES

D. R. Kaprekar, On Kaprekar numbers, J. Rec. Math., Vol. 13 (1980-1981), pp. 81-82.

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

David Wells, The Penguin Dictionary of Curious and Interesting Numbers, Penguin Books, NY, 1986, p. 151.

LINKS

Robert Gerbicz, [Table of n, a(n) for n = 1..51514][15] [T. D. Noe computed terms 1 - 1019, Nov 10 2007; R. Gerbicz computed the first 51514 terms, Jul 28 2011]

Santanu Bandyopadhyay, [Kaprekar Number][16], Indian Institute of Technology Bombay (Mumbai, India, 2020).

Nicholas John Bizzell-Browning, [LIE scales: Composing with scales of linear intervallic expansion][17], Ph. D. Thesis, Brunel Univ. (UK, 2024). See p. 142.

Ömer Eğecioğlu and Bünyamin Şahin, [On twin EP numbers][18], Transact. Comb. (2025) Vol. 14, Iss. 4, Art. No. 4, 261-270. See p. 262, also [ResearchGate][19].

Shyam Sunder Gupta, [On Some Marvellous Numbers of Kaprekar][20], Exploring the Beauty of Fascinating Numbers, Springer (2025) Ch. 9, 275-315.

Hans Havermann, [The first 11 million Kaprekar numbers (plus the region around the billionth)][21].

Douglas E. Iannucci, [The Kaprekar Numbers][22], Journal of Integer Sequences, Vol. 3 (2000), Article 1.2,

Douglas E. Iannucci and Bertrum Foster, [Kaprekar Triples][23], Journal of Integer Sequences, Vol. 8 (2005), Article 05.4.8.

Mohammad Javaheri, [On 2025 and Other Torn Numbers][24], Amer. Math. Monthly (2025).

Robert Munafo, [Kaprekar Sequences][25].

Rosetta Code, [Kaprekar numbers][26].

Walter Schneider, [Kaprekar Numbers][27], 2002.

Gérard Villemin's Almanach of Numbers, [Nombres de Kaprekar][28]

Eric Weisstein's World of Mathematics, [Kaprekar Number][29].

Wikipedia, [Kaprekar number][30].

[Index entries for Colombian or self numbers and related sequences][31]

FORMULA

a(n) = [A194218][32] (n) + [A194219][33] (n) and [A194218][32] (n) concatenated with [A194219][33] (n) gives a(n)^2. - [Reinhard Zumkeller][34], Aug 19 2011

EXAMPLE

703 is a Kaprekar number because 703 = 494 + 209, 703^2 = 494209.

MATHEMATICA

(* This Mathematica code computes five additional powers in order to be sure that all the Kaprekar numbers have been computed. This fix works for mx <= 50, which includes terms computed by Gerbicz. *)

Inv[a_, b_] := PowerMod[a, -1, b]; mx = 20; t = {1}; Do[h = 10^k - 1; d = Divisors[h]; d2 = Select[d, GCD[#, h/#] == 1 &]; If[Log[10, h] < mx, AppendTo[t, h]]; Do[q = d2[[i]]*Inv[d2[[i]], h/d2[[i]]]; If[Log[10, q] < mx, AppendTo[t, q]], {i, 2, Length[d2] - 1}], {k, mx + 5}]; t = Union[t] (* [T. D. Noe][35], Aug 17 2011, Aug 18 2011 *)

kaprQ[\[Nu]_] := Module[{n = \[Nu]^2},

MemberQ[Plus @@ # & /@

Select[Table[{Floor[n/10^j], 10^j*FractionalPart[n/10^j]}, {j,

IntegerLength@n - 1}], #[[2]] != 0 &], \[Nu]]];

Select[Range@1000000, kaprQ] (* [Hans Rudolf Widmer][36], Oct 22 2021 *)

PROG

(Haskell) -- See [A194218][32] for another version

a006886 n = a006886_list !! (n-1)

a006886_list = 1 : filter chi [4..] where

chi n = read (reverse us) + read (reverse vs) == n where

(us, vs) = splitAt (length $ show n) (reverse $ show (n^2))

-- [Reinhard Zumkeller][34], Aug 18 2011

(PARI) select( {is_ [A006886][37] (n)=my(N=n^2, m=1); while(N>m*=10, n==N%m+N\m && m!=n && return(m)); n==1}, [1..10^5]) \\ [M. F. Hasler][14], Mar 28 2025

(Python)

def is_ [A006886][37] (n):

m=1; return (N:=n**2)and any(n==sum(divmod(N, m:=m*10))!=m for _ in str(N))

print(upto_1e5 := [n for n in range(10**5)if is_ [A006886][37] (n)]) # [M. F. Hasler][14], Mar 28 2025

CROSSREFS

See [A053816][11] for another version.

Cf. [A037042][38], [A053394][39], [A053395][40], [A053396][41], [A053397][42], [A045913][43], [A003052][44].

Cf. [A193992][45] (where 10^n-1 occurs in [A006886][37]), [A194232][46] (first differences).

Subsequence of [A248353][47].

Sequence in context: [A124983][48] [A087969][49] [A044111][50] * [A053816][11] [A290449][51] [A045913][43]

Adjacent sequences: [A006883][52] [A006884][53] [A006885][54] * [A006887][55] [A006888][56] [A006889][57]

KEYWORD

nonn, nice, base, easy

AUTHOR

[Robert Munafo][58]

EXTENSIONS

More terms from [Michel ten Voorde][59], Apr 11 2001

4879 and 5292 added by Larry Reeves (larryr(AT)acm.org), Apr 24 2001

38962 added by Larry Reeves (larryr(AT)acm.org), May 23 2002

STATUS

approved

[Lookup][3] [Welcome][60] [Wiki][61] [Register][62] [Music][63] [Plot 2][64] [Demos][65] [Index][66] [WebCam][67] [Contribute][68] [Format][69] [Style Sheet][70] [Transforms][71] [Superseeker][72] [Recents][73]

[The OEIS Community][74]

Maintained by [The OEIS Foundation Inc.][75]

Last modified August 16 16:29 EDT 2026. Contains 398368 sequences.

[License Agreements, Terms of Use, Privacy Policy][76]


## Links

[1]: /login?redirect=%2fA006886
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A006886/list
[5]: /A006886/graph
[6]: /search?q=A006886+-id:A006886
[7]: /A006886/listen
[8]: /history?seq=A006886
[9]: /search?q=id:A006886&fmt=text
[10]: /A006886/internal
[11]: /A053816
[12]: /wiki/User:Ezhilarasu_Velayutham
[13]: /wiki/User:Amiram_Eldar
[14]: /wiki/User:M._F._Hasler
[15]: /A006886/b006886.txt
[16]: https://www.ese.iitb.ac.in/~santanu/RM7.pdf
[17]: https://bura.brunel.ac.uk/handle/2438/29960
[18]: https://doi.org/10.22108/toc.2024.138412.2092
[19]: https://www.researchgate.net/publication/384628439_On_Twin_EP_Numbers
[20]: https://doi.org/10.1007/978-981-97-2465-9_9
[21]: http://chesswanks.com/seq/b006886/
[22]: http://www.cs.uwaterloo.ca/journals/JIS/VOL3/iann2a.html
[23]: https://cs.uwaterloo.ca/journals/JIS/VOL8/Iannucci/iannucci45.html
[24]: https://doi.org/10.1080/00029890.2025.2561491
[25]: http://www.mrob.com/pub/seq/kaprekar.html
[26]: http://rosettacode.org/wiki/Kaprekar_numbers
[27]: http://web.archive.org/web/2004/www.wschnei.de/digit-related-numbers/kaprekar-numbers.html
[28]: http://villemin.gerard.free.fr/Wwwgvmm/Iteration/Kaprekar.htm#Nombre
[29]: https://mathworld.wolfram.com/KaprekarNumber.html
[30]: https://en.wikipedia.org/wiki/Kaprekar_number
[31]: /index/Coi#Colombian
[32]: /A194218
[33]: /A194219
[34]: /wiki/User:Reinhard_Zumkeller
[35]: /wiki/User:T._D._Noe
[36]: /wiki/User:Hans_Rudolf_Widmer
[37]: /A006886
[38]: /A037042
[39]: /A053394
[40]: /A053395
[41]: /A053396
[42]: /A053397
[43]: /A045913
[44]: /A003052
[45]: /A193992
[46]: /A194232
[47]: /A248353
[48]: /A124983
[49]: /A087969
[50]: /A044111
[51]: /A290449
[52]: /A006883
[53]: /A006884
[54]: /A006885
[55]: /A006887
[56]: /A006888
[57]: /A006889
[58]: /wiki/User:Robert_Munafo
[59]: /wiki/User:Michel_ten_Voorde
[60]: /wiki/Welcome
[61]: /wiki/Main_Page
[62]: /wiki/Special:RequestAccount
[63]: /play.html
[64]: /plot2.html
[65]: /demo1.html
[66]: /wiki/Index_to_OEIS
[67]: /webcam
[68]: /Submit.html
[69]: /eishelp2.html
[70]: /wiki/Style_Sheet
[71]: /transforms.html
[72]: /ol.html
[73]: /recent
[74]: /community.html
[75]: http://oeisf.org
[76]: /wiki/Legal_Documents
